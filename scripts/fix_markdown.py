"""
Simple Markdown fixer for the german-cheat-sheet repo.
- Normalizes heading levels and ensures a single space after '#'
- Removes trailing whitespace
- Ensures files end with a single newline
- Fixes links that end with '.md' to use relative links (keeps .md but normalizes path separators)
- Generates a basic TOC at top of README.md and master.md files if missing
- Reports potentially broken links (internal links to missing files)

Usage:
    python scripts/fix_markdown.py --apply

By default runs in dry-run mode and prints proposed changes.
"""
import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_EXT = '.md'

heading_re = re.compile(r'^(#{1,6})(\s*)(.*)$')
link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def normalize_heading(line):
    m = heading_re.match(line)
    if not m:
        return line
    hashes, spaces, rest = m.groups()
    return f"{hashes} {rest.strip()}\n"


def normalize_links(line):
    # Normalize backslashes in links and remove redundant './'
    def repl(m):
        text, url = m.groups()
        # Only adjust local .md links
        if url.startswith('http') or url.startswith('#'):
            return m.group(0)
        url = url.replace('\\', '/')
        url = re.sub(r'^\./', '', url)
        return f'[{text}]({url})'
    return link_re.sub(repl, line)


def process_file(path: Path):
    changed = False
    # Read bytes first to handle unknown encodings or binary files
    raw = path.read_bytes()
    # Try several decodings (don't treat null bytes as immediate binary; UTF-16 contains many nulls)
    decode_attempts = ['utf-8', 'utf-8-sig', 'utf-16', 'utf-16-le', 'utf-16-be', 'cp1252', 'latin-1']
    original = None
    used_encoding = None
    for enc in decode_attempts:
        try:
            original = raw.decode(enc)
            used_encoding = enc
            break
        except Exception:
            continue
    if original is None:
        # give up on this file (likely truly binary or unknown encoding)
        return None, None, False

    # If the decoded text still contains embedded nulls, keep it — it's likely a UTF-16 decode; do not skip
    # Continue processing using the decoded `original` string.

    lines = original.splitlines(keepends=True)
    new_lines = []
    for line in lines:
        orig_line = line
        line = line.rstrip() + '\n'  # remove trailing spaces, ensure newline
        line = normalize_heading(line)
        line = normalize_links(line)
        if line != orig_line:
            changed = True
        new_lines.append(line)

    # Ensure ends with single newline
    if not new_lines:
        new_text = '\n'
    else:
        # remove extra blank lines at end
        while len(new_lines) > 1 and new_lines[-1].strip() == '' and new_lines[-2].strip() == '':
            new_lines.pop()
        if new_lines[-1].endswith('\n'):
            pass
        else:
            new_lines[-1] = new_lines[-1] + '\n'
        new_text = ''.join(new_lines)

    return original, new_text, changed


def find_md_files(root: Path):
    for p in root.rglob('*.md'):
        yield p


def build_toc(text):
    # Simple TOC from top-level headings (## and ###)
    lines = text.splitlines()
    toc_lines = ["## Table of contents\n\n"]
    for l in lines:
        m = re.match(r'^(#{2,3})\s+(.*)$', l)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            anchor = title.lower()
            anchor = re.sub(r"[^a-z0-9 -]", '', anchor)
            anchor = anchor.replace(' ', '-')
            indent = '  ' if level == 3 else ''
            toc_lines.append(f"{indent}- [{title}](#{anchor})\n")
    if len(toc_lines) == 1:
        return ''
    return ''.join(toc_lines) + '\n'


def add_toc_if_missing(path: Path, text: str):
    # For README.md and master.md only
    name = path.name.lower()
    if name not in ('readme.md', 'master.md'):
        return text, False
    if '## Table of contents' in text or '## Table of Contents' in text:
        return text, False
    toc = build_toc(text)
    if not toc:
        return text, False
    # Insert after first H1 or at start
    lines = text.splitlines(keepends=True)
    insert_at = 0
    for i, l in enumerate(lines[:10]):
        if l.startswith('# '):
            insert_at = i + 1
            break
    new_lines = lines[:insert_at] + ['\n'] + [toc] + lines[insert_at:]
    return ''.join(new_lines), True


def find_broken_links(file_path: Path, text: str):
    broken = []
    for m in link_re.finditer(text):
        url = m.group(2)
        if url.startswith('http') or url.startswith('#'):
            continue
        # remove anchor
        url_no_anchor = url.split('#')[0]
        # if it points to a file
        if url_no_anchor.endswith('.md'):
            target = (file_path.parent / url_no_anchor).resolve()
            if not target.exists():
                broken.append(url)
    return broken


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true', help='Apply changes')
    parser.add_argument('--debug', action='store_true', help='Print debug info per file')
    parser.add_argument('--print-broken', action='store_true', help='Print potential broken links in detail')
    args = parser.parse_args()

    md_files = list(find_md_files(ROOT))
    modified = []
    broken_links = {}
    skipped = []

    for p in md_files:
        original, new_text, changed = process_file(p)
        if args.debug:
            if original is None:
                print(f"DEBUG: Skipping {p} (binary/undecodable)")
            else:
                # try to detect encoding by attempting decodings again (cheap)
                raw = p.read_bytes()
                enc_used = None
                for enc in ['utf-8', 'utf-8-sig', 'utf-16', 'utf-16-le', 'utf-16-be', 'cp1252', 'latin-1']:
                    try:
                        raw.decode(enc)
                        enc_used = enc
                        break
                    except Exception:
                        continue
                print(f"DEBUG: {p} decoded with: {enc_used}")
        if original is None:
            skipped.append(str(p.relative_to(ROOT)))
            continue
        new_text, toc_added = add_toc_if_missing(p, new_text)
        if new_text != original or toc_added:
            changed = True
        if changed:
            modified.append(str(p.relative_to(ROOT)))
            if args.apply:
                # write using utf-8 and add BOM if original had utf-8-sig? Simpler: write utf-8
                p.write_text(new_text, encoding='utf-8')
        # find broken links relative to file location
        b = find_broken_links(p, new_text)
        if b:
            broken_links[str(p.relative_to(ROOT))] = b

    print(f"Found {len(md_files)} markdown files. Modified: {len(modified)}")
    for m in modified:
        print('  M', m)
    if skipped:
        print('\nSkipped (binary/undecodable) files:')
        for s in skipped:
            print('  -', s)
    if broken_links:
        if args.print_broken:
            print('\nPotential broken links:')
            for k, v in broken_links.items():
                print(f'  {k}:')
                for link in v:
                    print(f'    - {link}')
        else:
            # summary
            print(f'\nPotential broken links found in {len(broken_links)} files. Run with --print-broken to see details.')

if __name__ == '__main__':
    main()
