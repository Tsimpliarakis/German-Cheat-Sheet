# Contributing to German-Cheat-Sheet

Thank you for considering contributing! This project is meant to be a helpful reference for people learning German. Contributions are very welcome — whether it’s fixing a typo, adding examples, or creating a translation in another language.

---

## 🛠 How to Contribute

1. **Fork this repository**
   Click the “Fork” button on the top right of the GitHub page.

2. **Clone your fork locally**

   ```bash
   git clone https://github.com/tsimpliarakis/german-cheat-sheet.git
   cd german-cheat-sheet
   ```

3. **Create a new branch** for your changes

   ```bash
   git checkout -b my-new-feature
   ```

4. **Make your edits**

   * Add notes, examples, or corrections.
   * Follow the existing folder structure (`verbs/`, `cases/`, etc.).
   * Keep filenames simple and descriptive.

5. **Commit and push your changes**

   ```bash
   git add .
   git commit -m "Add explanation for dative case"
   git push origin my-new-feature
   ```

6. **Open a Pull Request (PR)**
   Go to your fork on GitHub and click **Compare & Pull Request**.
   Explain briefly what you changed and why.

---

## 🌍 Adding Other Languages

Instead of mixing everything into one repo, translations live on **separate branches**:

* `main` → German–English (default)
* `german-greek` → German–Greek version
* `german-turkish` → German–Turkish version
* …and so on

### How to add a new language

1. Create a new branch from `main`:

   ```bash
   git checkout -b german-spanish
   ```

2. Translate the content in that branch.
   Keep the same folder and file structure so it’s easy to sync updates.

3. Push your branch and open a PR so it becomes visible in the repo.

This way, each language stays organized, and updates to the German side can be merged across branches more easily.

---

## ✅ Guidelines

* Keep explanations **clear and concise**.
* Use **Markdown** (`.md`) for readability.
* Follow the existing style: headings, tables, and examples should look consistent.
* If unsure about grammar accuracy, leave a note (`TODO:`) — someone else can refine it.

---

## 📬 Questions?

If you’re unsure about anything, open an issue on GitHub and ask.
