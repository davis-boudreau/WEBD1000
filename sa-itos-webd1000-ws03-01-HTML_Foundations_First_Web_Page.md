# WEBD 1000 — Workshop 03-01: HTML Foundations

**Instructor:** Davis Boudreau  
**Duration:** Approximately 30 minutes (allow extra time if you are new to VS Code)  
**Level:** Beginner — no prior HTML/CSS experience required  
**Learning outcome:** Develop standards-compliant webpages using HTML and CSS  
**Assessment:** Formative workshop practice; no separate repository or Brightspace submission required unless directed

## What you will build

You will create a simple webpage with a heading, paragraphs, and basic colours. You will learn how HTML describes content and how CSS changes its appearance.

**Important:** Use your **existing WEBD 1000 course GitHub repository**. Do **not** create a new repository. The separate repository for your independent semester website project will be introduced during the project portion of the course.

## 1. Understand: HTML, CSS, and files (5 minutes)

A **webpage** is a document displayed by a web browser. Two foundational languages work together:

- **HTML (HyperText Markup Language)** gives content its structure and meaning: headings, paragraphs, links, images, and sections.
- **CSS (Cascading Style Sheets)** controls how that content looks: colours, fonts, spacing, and layouts.

An HTML element commonly includes an opening tag, content, and a closing tag:

```html
<h1>My First Webpage</h1>
<p>Welcome to my website.</p>
```

`<h1>` identifies the main heading; `<p>` identifies a paragraph. The browser uses these tags to understand the content. CSS can then select those elements and style them.

### How we will organize Workshop 3

All Workshop 3 activities belong inside a folder named **`Workshop3`** in your **existing course repository**. Each activity gets a short, descriptive folder name and its own `index.html` and `styles.css`.

```text
YOUR-EXISTING-WEBD1000-COURSE-REPO/
├── ... your existing course files ...
└── Workshop3/
    └── 01-html-basics/
        ├── index.html
        └── styles.css
```

**Naming rule for every subsequent activity:** Create a new folder inside `Workshop3` (for example, `02-header-nav` or `03-hero`). Within that folder, create `index.html` and `styles.css`. Do not overwrite the previous activity's files.

## 2. Build: Create the activity files (5 minutes)

1. Open **VS Code**.
2. Open your **existing local WEBD 1000 course repository** using **File → Open Folder**. If you do not have a local copy yet, clone your existing course repository; do not create a new one.
3. In the Explorer panel, right-click the repository's root folder and choose **New Folder**. Name it exactly **`Workshop3`**. If that folder already exists, use it; do not create another.
4. Right-click `Workshop3` → **New Folder** → enter **`01-html-basics`**.
5. Right-click `01-html-basics` → **New File** → enter **`index.html`**.
6. Create a second file in the same folder named **`styles.css`**.

**Checkpoint:** Both files must be inside `Workshop3/01-html-basics/`, not directly in `Workshop3` or the repository root.

### Write your HTML

Open `index.html` and type or copy:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Webpage</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>My First Webpage</h1>
    <p>Welcome to my website!</p>
    <p>I am learning HTML and CSS in WEBD 1000.</p>
</body>
</html>
```

Save using **Ctrl+S**.

### Why each part is there

| Code | Purpose |
|---|---|
| `<!DOCTYPE html>` | Tells the browser this is a modern HTML document. |
| `<html lang="en">` | Identifies the document language as English. |
| `<head>` | Contains information *about* the page rather than its main visible content. |
| `<meta charset="UTF-8">` | Allows the browser to interpret text characters correctly. |
| `<meta name="viewport" ...>` | Helps the page scale appropriately on mobile screens. |
| `<title>` | Sets the text displayed in the browser tab. |
| `<link rel="stylesheet" href="styles.css">` | Loads the CSS file named `styles.css` from the **same folder** as `index.html`. |
| `<body>` | Contains the content visitors see. |
| `<h1>` | Marks the main heading of this page. |
| `<p>` | Marks a paragraph. |

**Relative paths:** `href="styles.css"` means “look for `styles.css` beside this HTML file.” If you misspell the filename, the browser cannot load the stylesheet. A `<link>` element does not need a closing `</link>` tag.

## 3. Understand and build: Your first CSS rules (8 minutes)

Before typing CSS, learn its basic structure:

```css
selector {
    property: value;
}
```

- A **selector** identifies which HTML element(s) to style.
- A **property** names what you want to change, such as `color` or `background-color`.
- A **value** specifies the setting, such as `blue`, `16px`, or a hexadecimal colour.
- The **curly braces** `{ }` enclose the declarations for that selector.
- The **colon** separates a property from its value; the **semicolon** ends each declaration.

For example:

```css
h1 {
    color: #004780;
}
```

The selector `h1` matches **every `<h1>` element** on the page. The `color` property changes the **text colour** of those headings to the blue represented by `#004780`. This is an **element selector** because it uses an HTML tag name.

### Add your stylesheet

Open `styles.css` and enter:

```css
body {
    background-color: #edf2f7;
    color: #14253a;
    font-family: Arial, sans-serif;
}

h1 {
    color: #004780;
}
```

Save using **Ctrl+S**.

### Explain the CSS as you build

**Rule 1: `body`**

- `body` selects the webpage's `<body>` element.
- `background-color: #edf2f7;` gives the page a pale blue-grey background.
- `color: #14253a;` sets the default text colour to dark blue-grey.
- `font-family: Arial, sans-serif;` asks for Arial; if unavailable, the browser uses another sans-serif font.

**Rule 2: `h1`**

- `h1` selects the main heading element.
- `color: #004780;` makes its text blue.

**Why is the heading blue while the paragraphs remain dark?** The `body` rule provides a text colour that its child elements can **inherit**. The more specific styling applied directly to `h1` overrides that inherited text colour for the heading. Paragraphs have no separate colour rule, so they inherit the `body` colour.

**Colour vocabulary:** Values beginning with `#` are **hexadecimal colour codes**. You do not need to memorize them; for now, observe how changing a value changes the browser display.

**Important distinction:** `color` changes the text colour; `background-color` changes the background behind an element.

## 4. Run, predict, test, and debug (5 minutes)

### Open your page

1. In VS Code, right-click **`Workshop3/01-html-basics/index.html`**.
2. Choose **Open with Live Server**, if the extension is installed. Alternatively, open that file from File Explorer in a browser.
3. Check that you see a heading and two paragraphs, with a pale background and blue heading.

### Experiment A — HTML

**Predict:** What will change if you edit the words between `<h1>` and `</h1>`?

Change the heading to `Welcome to Workshop 3`, save, and refresh. Confirm your prediction.

### Experiment B — CSS selector

**Predict:** Which text will turn blue if you change the selector `h1` to `p` in `styles.css`?

Try it. Save and refresh. The paragraphs should become blue, while the heading uses the inherited `body` text colour. **Then restore the selector to `h1`**.

### Experiment C — CSS property

Change `background-color: #edf2f7;` to `background-color: #ffffff;`, save, and refresh. The background should become white. You may restore the original colour afterward.

### If something does not work

- Confirm the filenames are exactly `index.html` and `styles.css`.
- Confirm both files are in `Workshop3/01-html-basics/`.
- Confirm the HTML says `href="styles.css"`, not `href="activity.css"`.
- Save both files and refresh the browser.
- Check that CSS declarations use `{ }`, `:`, and `;` correctly.
- Ensure you opened **this activity's** `index.html`, not an earlier page in the repository.

## 5. Apply independently (3 minutes)

Without copying a new example, complete these small changes:

- [ ] Change the `<h1>` heading to a title of your choice.
- [ ] Add a third `<p>` paragraph describing something you want to learn in website development.
- [ ] Change the `h1` text colour to another hexadecimal colour and confirm the result in the browser.

**Check your understanding:** In the rule `h1 { color: #004780; }`, identify the selector, property, and value. Explain why changing `h1` to `p` changes which text receives the style.

## 6. Save your workshop evidence in GitHub (approximately 2 minutes)

Use the **same existing WEBD 1000 course repository** throughout Workshop 3.

1. Open **Source Control** in VS Code.
2. Review the two new files under `Workshop3/01-html-basics/`.
3. Stage the files.
4. Commit with the message **`WS03-01: HTML foundations and CSS selectors`**.
5. **Push** or **Sync Changes** to the existing course repository.
6. Open the repository on GitHub and confirm that `Workshop3/01-html-basics/index.html` and `styles.css` are present.

If you cannot push during the session, keep your files saved locally and complete the push as soon as you can. Do not create another repository to solve a push problem.

## Completion checklist

- [ ] I used my **existing WEBD 1000 course repository**.
- [ ] I created or reused the **`Workshop3`** folder.
- [ ] I created the **`01-html-basics`** activity folder.
- [ ] I created `index.html` and `styles.css` inside it.
- [ ] I can explain the difference between HTML and CSS.
- [ ] I can identify a CSS selector, property, and value.
- [ ] I tested the page in a browser and made independent changes.
- [ ] I committed and pushed my work to my existing course repository.

## Reflection

1. What is the purpose of `index.html`?
2. How does the HTML file find `styles.css`?
3. What is the difference between the `body` and `h1` selectors?
4. What did you observe when you changed the selector from `h1` to `p`?
5. What problem did you encounter, if any, and how did you investigate it?

**Submission:** Keep your working files and GitHub commit as technical evidence. No separate activity submission is required unless your instructor directs otherwise.

## Next: Workshop 03-02 — Semantic Header and Navigation

Create a **new** folder named `Workshop3/02-header-nav/`. Copy the **completed** `index.html` and `styles.css` from `01-html-basics/` into it. You will then add a semantic `<header>`, a site name, and a `<nav>` containing links. Your Activity 01 files remain unchanged as a checkpoint.
