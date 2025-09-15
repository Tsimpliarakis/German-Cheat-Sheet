# German-Cheat-Sheet

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Markdown CI](https://github.com/tsimpliarakis/german-cheat-sheet/actions/workflows/markdown-ci.yml/badge.svg)](https://github.com/tsimpliarakis/german-cheat-sheet/actions/workflows/markdown-ci.yml)


## Table of contents

- [📖 Contents](#-contents)
- [🚀 Goal](#-goal)
- [📌 Notes](#-notes)
  - [💡 Tip](#-tip)
- [🤝 Contributions](#-contributions)


A simple and structured collection of notes, examples, and resources to help anyone learning German.
This repository is meant as a quick reference — like a personal textbook — covering grammar, vocabulary, and essential rules.

## 📖 Contents

Click on a topic to jump directly to its page:

- [Alphabet](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/alphabet)
- [Articles & Genders](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/articles)
- [Cases (Nominative, Accusative, Dative, Genitive)](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/nouns)
- [Pronouns](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/pronouns)
- [Verbs & Conjugation](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/verbs)
- [Tenses](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/verbs)
- [Word Order & Sentences](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/syntax)
- [Adjectives & Adverbs](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/adjectives)
- [Vocabulary Collections](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/vocabulary)
- [Cheat Sheets (Quick Reference)](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/cheatsheets)

- [Articles & Genders](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/articles)
- [Cases (Nominative, Accusative, Dative, Genitive)](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/nouns)
- [Pronouns](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/pronouns)
- [Verbs & Conjugation](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/verbs)
- [Tenses](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/verbs)
- [Word Order & Sentences](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/syntax)
- [Adjectives & Adverbs](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/grammar/adjectives)

---

## 🚀 Goal

The goal is not to replace full textbooks but to create a **quick-access reference** for learners who want to review rules, patterns, and common pitfalls without searching across multiple sources.

---

## 📌 Notes

- Everything here is based on learning experiences, grammar books, and resources collected while studying.
- Mistakes might exist — German grammar can be a maze. If you spot any, please let me know.

---

### 💡 Tip
If you’re new to German, start with:
1. [Alphabet](https://github.com/tsimpliarakis/german-cheat-sheet/tree/main/alphabet)
2. [Articles & Genders](https://github.com/Tsimpliarakis/German-Cheat-Sheet/tree/main/grammar/articles)
3. [Cases](https://github.com/Tsimpliarakis/German-Cheat-Sheet/tree/main/grammar/cases)

These three are the foundation for almost everything else.

## 🤝 Contributions
Contributions are welcome — feel free to open a PR with your own notes or corrections!

For contribution guidelines, go here:
[contributing.md](contributing.md)

## How to build locally

Small local checks and site preview:

1. Run markdown lint locally (optional):

```powershell
npm install -g markdownlint-cli
markdownlint "**/*.md"
```

2. Preview the documentation site (MkDocs):

```powershell
pip install mkdocs mkdocs-material
mkdocs serve
```

CI: This repo runs a markdown lint and link-checker on pushes/PRs (see `.github/workflows`).

Docs publishing: The repository is configured to build the MkDocs site and publish to GitHub Pages. See `DEPLOYMENT.md` for instructions to enable Pages in repository settings.
