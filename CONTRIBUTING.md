# Contributing to German-Cheat-Sheet

Thank you for considering contributing! This project is built to be a helpful reference for people learning German. Contributions are very welcome — whether it’s fixing a typo, adding examples, or creating a new language pair.

---

## 🛠 How to Contribute

1. **Fork this repository**  
   Click the “Fork” button on the top right of the GitHub page.

2. **Clone your fork locally**  
   ```bash
   git clone https://github.com/YOUR-USERNAME/german-cheat-sheet.git
   cd german-cheat-sheet
   ```

3. **Create a new branch** for your changes  
   ```bash
   git checkout -b my-new-feature
   ```

4. **Make your edits**  
   - Add notes, examples, or corrections.  
   - Organize content into folders if needed (e.g. `verbs/`, `cases/`).  
   - Keep filenames simple and descriptive.  

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

This repo currently focuses on **German–English**, but you can add other language pairs too.  
For example, if you want to create **German–Turkish** notes:

- Create a new folder:  
  ```
  german-turkish/
  ```
- Inside, add subfolders like `alphabet/`, `vocabulary/`, `grammar/` with Turkish explanations. 
- Add a Turkish `README.md` to redirect to the Turkish subfolders.
- Add the links to the new `README.md` in the main `README.md` so others can find it.

Example structure:
```
/README.md
/german-english
   /alphabet
   /grammar
/german-turkish
   README.md
   /alfabe
   /dilbilgisi
```

---

## ✅ Guidelines

- Keep explanations **clear and concise**.  
- Use **Markdown** (`.md`) for readability.  
- Group related content in subfolders instead of dumping everything in one place.  
- If you’re unsure about grammar accuracy, leave a note — someone else can refine it.  

---

## 📬 Questions?

If you’re unsure about anything, just open an issue on GitHub and ask.  
