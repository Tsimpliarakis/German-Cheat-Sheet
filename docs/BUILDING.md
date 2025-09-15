Local build
===========

To build the site locally for preview or testing:

```bash
pip install -r requirements.txt
mkdocs serve
```

Or to produce the static site output:

```bash
mkdocs build
```

This project includes a GitHub Actions workflow that runs `mkdocs build --clean` on pushes and pull requests to `main`.
