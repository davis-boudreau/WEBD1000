# WEBD 1000 — Workshop 03-05: Desktop Header with Flexbox

**Instructor:** Davis Boudreau  
**Course:** WEBD 1000 — Website Development  
**Duration:** Approximately 30 minutes (allow extra time for beginners)  
**Activity:** 05 of 12 in the cumulative website-building series  
**Assessment:** Formative; evidence retained in the existing WEBD 1000 course repository  
**Learning focus:** Semantic navigation, CSS Flexbox, reusable design tokens, accessibility and browser testing

## Workshop overview

Your website already has HTML content, a semantic header and navigation, a hero section, and basic design tokens. In this activity, you will improve the **desktop header** so the website name appears on the left and navigation links line up on the right. You will learn **how Flexbox works before using it**. The next activity will adapt this navigation for narrow screens.

**You will be able to:**

1. Explain a Flexbox container and its child items.
2. Use `display: flex`, `justify-content`, `align-items`, and `gap`.
3. Identify the main axis and cross axis in a row layout.
4. Style navigation links without removing keyboard accessibility.
5. Test your layout and commit your work to the existing course repository.

**Timing guide:** Understand (5 min) → Prepare (3 min) → Build (14 min) → Test (4 min) → Apply and commit (4 min). These times are targets, not deadlines.

---

## 1. Understand: Why use Flexbox? (5 minutes)

### The problem with ordinary HTML flow

Browsers normally display block elements such as `<header>`, `<div>`, and `<nav>` one below another. That is useful for reading content, but desktop website headers often need elements **side by side**.

**Flexbox** is a CSS layout system designed to arrange elements in a row or column and control the space between them.

### A Flexbox container and its items

Consider this simplified HTML:

```html
<div class="header-layout">
    <a class="site-brand" href="#home">My Website</a>
    <nav class="site-navigation" aria-label="Primary navigation">
        <!-- Navigation links go here -->
    </nav>
</div>
```

When you add `display: flex` to `.header-layout`, its **direct children**—the brand link and the navigation element—become **flex items**.

```css
.header-layout {
    display: flex;
}
```

By default, Flexbox arranges these items in a **row** (left to right in an English-language page).

### Four important Flexbox properties

| CSS | What it means | What you will see |
|---|---|---|
| `display: flex;` | Make the element a Flexbox container | Direct children appear in a row by default |
| `justify-content: space-between;` | Distribute space along the **main axis** | First item at the left, last at the right |
| `align-items: center;` | Align items along the **cross axis** | Brand and navigation vertically centred |
| `gap: 1rem;` | Add consistent space between flex items | Even spacing without separate margins |

**Main axis versus cross axis:** With the default `flex-direction: row`, the main axis is horizontal and the cross axis is vertical. If you later use `flex-direction: column`, the axes change.

**Prediction:** What happens if you remove `justify-content: space-between`? The brand and navigation will normally sit next to each other instead of at opposite ends of the header.

### Reusing CSS design tokens

In WS03-04 you introduced CSS custom properties, often called **design tokens**:

```css
:root {
    --color-primary: #004780;
    --color-background: #edf2f7;
    --space-medium: 1rem;
}
```

The `:root` selector targets the root HTML element. Variables defined there can be reused throughout the stylesheet. For example, `color: var(--color-primary);` reads the value of `--color-primary` instead of repeating the hexadecimal colour everywhere.

> **CSS selector reminder:** `.header-layout` begins with a period because it selects elements with `class="header-layout"`. The selector `.site-navigation a` selects `<a>` elements **inside** an element with the class `site-navigation`. The `a:hover` pseudo-class applies when a pointing device hovers over a link; `a:focus-visible` applies when the browser determines a visible keyboard focus indicator is needed.

---

## 2. Prepare your activity folder (3 minutes)

**Do not create another GitHub repository.** Use your existing **WEBD 1000 course repository**.

1. Open your existing course repository folder in **VS Code**.
2. Expand the folder named `Workshop3`.
3. Create a new folder named **`05-flex-header`**.
4. Copy **both** `index.html` and `styles.css` from `Workshop3/04-css-tokens/` into `Workshop3/05-flex-header/`.
5. Open the **copies** inside `05-flex-header` before editing. Keep WS03-04 unchanged.

Your files should be organized as follows:

```text
YOUR-EXISTING-WEBD1000-REPOSITORY/
└── Workshop3/
    ├── 01-html-basics/
    │   ├── index.html
    │   └── styles.css
    ├── 02-header-nav/
    │   ├── index.html
    │   └── styles.css
    ├── 03-hero/
    │   ├── index.html
    │   └── styles.css
    ├── 04-css-tokens/
    │   ├── index.html
    │   └── styles.css
    └── 05-flex-header/
        ├── index.html
        └── styles.css
```

**Checkpoint:** Confirm that `index.html` still contains the stylesheet link below and that `styles.css` is in the same folder:

```html
<link rel="stylesheet" href="styles.css">
```

If your previous activity has different text or section names, keep your content. The examples below use `#home`, `#features`, and `#contact`; adapt these IDs to match the sections already present in your page.

---

## 3. Build: Structure your desktop header (14 minutes)

### Step A — Find the existing header

In `05-flex-header/index.html`, locate the `<header>` created in WS03-02. **Do not replace the whole HTML document.** Update just the header area using this example. If you already have working navigation links, keep their labels and `href` values.

```html
<header class="site-header">
    <div class="header-layout">
        <a class="site-brand" href="#home">My Website</a>

        <nav class="site-navigation" aria-label="Primary navigation">
            <ul class="nav-list">
                <li><a href="#home">Home</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </div>
</header>
```

**Important:** Each `href="#..."` must match the `id` of a section **actually present** in your page. For example, `href="#features"` requires an element such as `<section id="features">`. If your page does not yet have a Features section, either use an existing section ID or create a short placeholder section inside `<main>`.

#### Why these HTML elements?

- `<header>` marks the introductory area of the webpage.
- `<nav>` identifies a set of navigation links.
- `aria-label="Primary navigation"` gives this navigation region a descriptive accessible name.
- `<ul>` and `<li>` represent a list of navigation choices.
- `<a href="#home">` creates a link to an element with `id="home"`.
- `<div class="header-layout">` is a neutral grouping element used to control layout with CSS. The semantic meaning still comes from `<header>` and `<nav>`.

**Heading reminder:** Your hero section should continue to contain the page's main `<h1>`. The brand in this header is a link, not another `<h1>`.

### Step B — Add the Flexbox rules

Open `05-flex-header/styles.css`. **Keep the CSS from WS03-04.** Add the following rules near the end of the stylesheet so you can easily find them. If an earlier rule uses exactly the same selector, update or replace that rule rather than keeping contradictory declarations.

```css
/* WS03-05: Desktop header and navigation */

.site-header {
    background-color: #ffffff;
    border-bottom: 1px solid #d8e0e8;
    padding: var(--space-medium, 1rem);
}

.header-layout {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: var(--space-medium, 1rem);
    max-width: 70rem;
    margin-inline: auto;
}

.site-brand {
    color: var(--color-primary, #004780);
    font-size: 1.25rem;
    font-weight: 700;
    text-decoration: none;
}

.nav-list {
    display: flex;
    align-items: center;
    gap: var(--space-medium, 1rem);
    list-style: none;
    margin: 0;
    padding: 0;
}

.site-navigation a {
    color: var(--color-primary, #004780);
    text-decoration: none;
    padding: 0.5rem;
}

.site-navigation a:hover {
    text-decoration: underline;
}

.site-navigation a:focus-visible,
.site-brand:focus-visible {
    outline: 3px solid #f37327;
    outline-offset: 3px;
}
```

#### Understand the new CSS before continuing

**`.site-header`** selects the header by its class. `background-color` fills the header, `border-bottom` draws a thin dividing line, and `padding` adds space **inside** its edges.

**`.header-layout`** is the first Flexbox container. `display: flex` places the brand and `<nav>` in a row. `justify-content: space-between` pushes them apart horizontally. `align-items: center` aligns them vertically.

**`max-width: 70rem`** prevents the header content from stretching too wide on large monitors. `margin-inline: auto` centres that limited-width container horizontally. `rem` is a length unit based on the root element's font size (often 16 pixels by default, unless changed).

**`.nav-list`** is a *second* Flexbox container. Its direct children are the `<li>` elements. This makes the Home, Features, and Contact links line up horizontally. `list-style: none` removes bullets, and `margin: 0; padding: 0;` remove the list's default spacing.

**`.site-navigation a`** is a *descendant selector*: it styles links inside `.site-navigation` without styling every link in the hero section. `padding: 0.5rem` increases each link's clickable area.

**`:hover` versus `:focus-visible`:** Hover styling helps mouse users recognize a link. A visible focus outline helps keyboard users identify the currently focused link. Do not remove the browser's focus indicator unless you provide an accessible replacement.

**`var(--space-medium, 1rem)`** means “use the `--space-medium` design token; if it is missing or invalid, use `1rem` as a fallback.” This lets the activity work even if a student named a token differently in WS03-04.

### Step C — Save and preview

1. Save `index.html` and `styles.css` using **Ctrl+S**.
2. Open `05-flex-header/index.html` with **Live Server**, or open it in a browser.
3. Make the browser window wide enough to see a desktop layout.
4. Confirm the brand appears on the left and navigation links appear on the right.

**Expected result (desktop):**

```text
+-------------------------------------------------------------------+
| My Website                                Home  Features  Contact  |
+-------------------------------------------------------------------+
|                                                                   |
|                     Your existing hero section                    |
|                                                                   |
```

> **Scope:** This activity focuses on a **desktop** header. On narrow screens, the links may wrap or feel crowded. That is expected for now; **WS03-06** introduces responsive navigation and a native hamburger menu.

---

## 4. Test, predict, and debug (4 minutes)

### Experiment 1 — Main-axis spacing

In `.header-layout`, temporarily change:

```css
justify-content: space-between;
```

to:

```css
justify-content: flex-start;
```

**Predict:** Where will the navigation move? Save and refresh. The brand and navigation should move toward the same side of the header. Restore `space-between` when finished.

### Experiment 2 — Navigation gap

Change the `.nav-list` gap to `2rem`. Save and refresh. What changes? Restore the original value or choose a spacing value that works well.

### Keyboard accessibility check

1. Click the browser's address bar and then click on the page (away from links), or reload the page.
2. Press **Tab** to move between links.
3. Confirm that a visible focus indicator appears.
4. Press **Enter** on a navigation link. Confirm it goes to the correct section.

### Troubleshooting

| Problem | Likely cause | Check |
|---|---|---|
| Header items still stack vertically | Flexbox rule is missing or selector does not match | `.header-layout` in HTML and CSS |
| Links still show bullets | `.nav-list` selector missing or incorrect | `class="nav-list"` on `<ul>` |
| CSS changes do not appear | Wrong stylesheet or unsaved file | `href="styles.css"`, Ctrl+S, refresh |
| Links do not scroll to sections | `href` and `id` do not match | `href="#contact"` and `id="contact"` |
| Navigation looks crowded | Browser window is narrow | Test on a wider window; mobile is next activity |
| Existing styles look different | Earlier CSS rules conflict | Search for duplicate selectors and compare declarations |

---

## 5. Apply independently and save your work (4 minutes)

Complete at least **one** of the following changes without copying a new full solution:

- Change the navigation gap using a design token or a `rem` value.
- Change the site-brand font size and explain why the brand remains aligned with the navigation.
- Add one **working** navigation link to a section that exists on your webpage.

Then commit and push the new activity folder to your **existing course repository**:

1. Open **Source Control** in VS Code.
2. Review the changed files in `Workshop3/05-flex-header/`.
3. Stage the changes.
4. Enter the commit message `WS03-05 - Desktop header with Flexbox`.
5. Commit and **Push/Sync Changes**.
6. Open GitHub and verify that both files are visible inside `Workshop3/05-flex-header/`.

**No separate project repository is required.** Your independent semester website project is separate from this guided workshop activity.

---

## 6. Reflection and completion checkpoint

Answer these questions in your workshop worksheet or notes, as directed by your instructor:

1. What is a Flexbox container? Which elements become flex items in `.header-layout`?
2. What is the difference between `justify-content` and `align-items` in a row layout?
3. Why do we use `display: flex` on both `.header-layout` and `.nav-list`?
4. What does the selector `.site-navigation a` target? How is it different from `a`?
5. Why is a visible keyboard focus indicator important?

**Completion checklist:**

- [ ] Used the existing WEBD 1000 course repository.
- [ ] Created `Workshop3/05-flex-header/`.
- [ ] Copied `index.html` and `styles.css` from WS03-04.
- [ ] Preserved the existing hero and other webpage content.
- [ ] Brand and navigation align horizontally in a desktop browser.
- [ ] Navigation links point to real sections and work by keyboard.
- [ ] Completed a CSS experiment and one independent change.
- [ ] Committed and pushed both files to GitHub.

**Submission:** Retain your files and reflection as evidence for Workshop 03. Follow your instructor's worksheet and Brightspace submission instructions; do not create a separate submission for each micro-activity unless directed.

### Next: WS03-06 — Responsive Navigation

You will keep this working desktop header, then learn how a **media query** changes its layout on smaller screens. You will introduce a native HTML `<details>`/`<summary>` mobile menu without requiring JavaScript.
