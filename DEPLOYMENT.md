GitHub Pages deployment

This repository includes a GitHub Actions workflow that builds the MkDocs site and publishes it to the `gh-pages` branch using `peaceiris/actions-gh-pages`.

Steps to enable Pages (repo admin required):

1. Go to the repository Settings > Pages (or Settings > Pages & GitHub Pages).
2. Select the source as the `gh-pages` branch (the build workflow will create/update it automatically).
3. Save — the site should become available at `https://<owner>.github.io/<repo>/` shortly after the first successful workflow run.

Notes:
- The workflow uses the automatically provided `GITHUB_TOKEN` for the publish step.
- If you want a custom domain, add it in the Pages settings and include a `CNAME` file in the site output or use the repository settings.
