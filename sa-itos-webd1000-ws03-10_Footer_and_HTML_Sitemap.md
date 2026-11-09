# WEBD 1000 — Workshop 03-10: Semantic Footer and HTML Sitemap

**Course:** WEBD 1000 — Website Development  
**Instructor:** Davis Boudreau  
**Duration:** Approximately 30 minutes (allow additional time for first-time learners)  
**Learning outcome:** Develop standards-compliant HTML and CSS; apply usability, accessibility, and responsive-design principles.  
**Assessment:** Formative — part of Workshop 03.  
**Prerequisite:** Completed WS03-09, or an instructor-provided equivalent checkpoint.

## Overview: What are we building?

You already have a header, navigation, hero, Flexbox content cards, CSS Grid content, and responsive layouts. Now you will add a **footer** to the bottom of your webpage. The footer will contain a short description of the site, a **visible HTML sitemap** (a set of links to the page's main sections), and a **Back to top** link.

You will learn the meaning of semantic HTML elements such as `<footer>` and `<nav>`, how same-page anchor links work, how to style a footer with CSS Grid, and how to test links with a keyboard and a narrow browser window.

**Important:** An HTML sitemap is a visible navigation aid for people. It is **not** the same as `sitemap.xml`, which is a machine-readable file used by search engines. You do **not** need to create `sitemap.xml` in this activity.

### Learning objectives

By the end, you should be able to:

1. Explain what a footer is and why it helps visitors.
2. Use `<footer>`, `<nav>`, headings, lists, and links appropriately.
3. Explain the relationship between `href="#features"` and `id="features"`.
4. Style a responsive footer with CSS Grid and your existing design tokens.
5. Test navigation, keyboard focus, and mobile readability.
6. Commit and push your completed files to the **existing course repository**.

---

## 1. Prepare your files (about 3 minutes)

Use your **existing WEBD 1000 course repository**. **Do not create a new GitHub repository.** A separate project repository, if used, belongs to the independent semester website project—not these guided workshop activities.

In VS Code's Explorer:

1. Open your existing course repository.
2. Expand `Workshop3`.
3. Create a folder called `10-footer-sitemap`.
4. Copy **both** files from `Workshop3/09-responsive/` into the new folder: `index.html` and `styles.css`.
5. Open the **copies** inside `10-footer-sitemap`. Leave the files in `09-responsive` unchanged.

Your structure should now resemble:

```text
Existing-Course-Repository/
└── Workshop3/
    ├── 01-html-basics/
    ├── 02-header-nav/
    ├── 03-hero/
    ├── 04-css-tokens/
    ├── 05-flex-header/
    ├── 06-mobile-nav/
    ├── 07-flex-cards/
    ├── 08-css-grid/
    ├── 09-responsive/
    └── 10-footer-sitemap/
        ├── index.html
        └── styles.css
```

**Checkpoint:** Confirm that the copied `index.html` contains a stylesheet link like this:

```html
<link rel="stylesheet" href="styles.css">
```

Because both files are in the same folder, `href="styles.css"` is a **relative path** that tells the browser where to find the stylesheet.

> **If you copied an `images/` folder in an earlier activity:** Copy it too if your webpage uses local images. A missing image often means its relative file path no longer points to the correct location.

---

## 2. Understand the theory: Why websites have footers (about 4 minutes)

### What is a footer?

A footer is the concluding area of a webpage. It often includes contact information, secondary navigation, copyright information, and links to important content. A useful footer answers the question: **"Where can I go next?"**

HTML provides a semantic element for this area:

```html
<footer>
    <p>Information about this website.</p>
</footer>
```

**Semantic HTML** means choosing elements based on their purpose rather than only how they look. A `<footer>` describes the role of the content. It does not automatically make the content dark or arrange it into columns; **CSS** controls that presentation.

### What is an HTML sitemap?

A **visible HTML sitemap** is an organized collection of links that helps visitors find content. On a single-page website, the links may point to sections of the same page. Later, on a multi-page website, the sitemap may also link to other HTML files.

A navigation region is marked up with `<nav>`. When a page contains more than one navigation region—such as a header menu and a footer sitemap—an accessible name helps people using assistive technology distinguish them:

```html
<nav aria-label="Footer sitemap">
    <!-- Footer navigation links go here. -->
</nav>
```

The `aria-label` attribute provides a name for the navigation region. It does not display visible text on the page, so we will also include a visible heading.

### How do same-page links work?

Compare these two parts:

```html
<a href="#features">Features</a>
```

```html
<section id="features">
    <h2>Features</h2>
</section>
```

The `#features` in `href` matches the `id="features"` on the target section. The browser scrolls to the matching element when the link is activated.

**Important rules:**

- The `#` appears in the **link**, but not in the `id` value.
- IDs should be **unique** within a page.
- The spelling must match exactly.
- A link to a missing ID will not take the visitor to the intended section.

**Prediction:** What will happen if the link uses `href="#contact"` but no element has `id="contact"`? Write your prediction before testing.

---

## 3. Inspect your existing sections (about 3 minutes)

Before creating the sitemap, check which section IDs **actually exist** in your copied `index.html`.

1. Open `10-footer-sitemap/index.html`.
2. Press **Ctrl+F** and search for `id=`.
3. Record the IDs for your home/hero, features, resources/grid, and contact sections (if present).

Your website may use IDs such as:

| Page content | Example ID | Example link |
|---|---|---|
| Hero / home | `home` | `href="#home"` |
| Flexbox features | `features` | `href="#features"` |
| Grid resources | `lists` | `href="#lists"` |
| Contact section | `contact` | `href="#contact"` |

**Do not assume these IDs exist.** They are examples based on our developing website. If your resources section uses `id="resources"`, your footer must link to `#resources`, not `#lists`.

### Make sure there is a top-of-page target

Locate the opening `<body>` tag. If you do not already have an element with `id="top"`, add the ID to the opening body tag:

```html
<body id="top">
```

This gives the Back to top link a reliable destination. **Do not add a second `id="top"` elsewhere.**

---

## 4. Build the footer in HTML (about 7 minutes)

### Step 1 — Find the correct location

Scroll near the bottom of `index.html`. Find the closing `</main>` and `</body>` tags. Insert the footer **after** `</main>` and **before** `</body>`:

```html
</main>

<!-- Add the footer here. -->

</body>
```

This makes the footer a site-level landmark, separate from the main content.

### Step 2 — Add the footer markup

Use this example, then adjust the `href` values to match the IDs you confirmed in Section 3.

```html
<footer class="site-footer">
    <div class="footer-layout">
        <section class="footer-about" aria-labelledby="footer-about-title">
            <h2 id="footer-about-title">About this website</h2>
            <p>
                A learning project demonstrating semantic HTML,
                CSS, and responsive website layouts.
            </p>
        </section>

        <nav class="footer-sitemap" aria-label="Footer sitemap">
            <h2>Explore this page</h2>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#lists">Resources</a></li>
            </ul>
        </nav>
    </div>

    <div class="footer-bottom">
        <p>WEBD 1000 — Website Development Practice</p>
        <a href="#top">Back to top</a>
    </div>
</footer>
```

**Adjust the example:** If your page does not have `id="lists"`, replace `#lists` with the ID used by your Grid section. If your page has a Contact section, you may add a matching Contact link. Do not add broken placeholder links.

### Step 3 — Understand the HTML you just added

| HTML | Meaning |
|---|---|
| `<footer>` | Marks the footer area of the page |
| `class="site-footer"` | Gives CSS a reusable way to select the footer |
| `<section>` | Groups related information under a heading |
| `aria-labelledby` | Connects the section's accessible name to a heading ID |
| `<nav aria-label="Footer sitemap">` | Identifies and names the footer navigation region |
| `<ul>` and `<li>` | Present navigation destinations as a list |
| `<a href="#home">` | Links to the element whose ID is `home` |
| `<div>` | Groups content for layout when no more specific semantic element is needed |

**Why use a list for navigation?** A list communicates that the links form a related set. CSS can remove the default bullets while preserving that meaning.

**Checkpoint:** Save `index.html` with **Ctrl+S**, open it in your browser, and scroll to the bottom. The footer content should appear, even before you add CSS.

---

## 5. Understand the CSS before using it (about 4 minutes)

### CSS rule anatomy

A CSS rule contains a **selector** and one or more **declarations**:

```css
.site-footer {
    padding: 2rem;
}
```

- `.site-footer` is a **class selector**. The dot (`.`) means “select elements with this class.”
- `padding` is a **property**. It controls space **inside** an element's boundary.
- `2rem` is a **value**. A `rem` is relative to the root element's font size; with a common default of 16px, `2rem` is approximately 32px.
- The braces `{ }` contain the declarations, and the semicolon `;` ends a declaration.

### Descendant selectors

```css
.footer-sitemap a {
    text-decoration: underline;
}
```

This selector means: **select every `<a>` element inside an element with the class `footer-sitemap`**. It does not affect every link on the page.

### CSS Grid refresher

```css
.footer-layout {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 2rem;
}
```

- `display: grid` turns the element into a grid container.
- `grid-template-columns` defines the column layout.
- `repeat(2, ...)` creates two columns.
- `1fr` means one share of the available space.
- `minmax(0, 1fr)` lets each column shrink as needed without enforcing a large minimum width.
- `gap` creates space between columns.

We will switch to one column on narrow screens using a **media query**.

### Design tokens and fallback values

In WS03-04, you introduced CSS custom properties such as `--color-primary`. You can use them with `var()`:

```css
color: var(--color-primary, #004780);
```

The first argument is the custom property's name. The second is a **fallback value** if that property is not defined. This helps the example work even if your earlier token names differ.

---

## 6. Style the footer (about 5 minutes)

Open `10-footer-sitemap/styles.css`. **Keep your existing CSS.** Add the following rules at the bottom of the file:

```css
/* WS03-10: Site footer and visible HTML sitemap */
.site-footer {
    margin-top: 3rem;
    padding: 2rem 1rem;
    background-color: var(--color-primary, #004780);
    color: #ffffff;
}

.footer-layout {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 2rem;
    max-width: 70rem;
    margin-inline: auto;
}

.site-footer h2 {
    color: #ffffff;
    font-size: 1.25rem;
    margin-top: 0;
}

.footer-sitemap ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.footer-sitemap li + li {
    margin-top: 0.5rem;
}

.site-footer a {
    color: #ffffff;
    text-decoration: underline;
    text-underline-offset: 0.2em;
}

.site-footer a:hover {
    text-decoration-thickness: 0.15em;
}

.site-footer a:focus-visible {
    outline: 3px solid #ffef00;
    outline-offset: 4px;
}

.footer-bottom {
    max-width: 70rem;
    margin: 2rem auto 0;
    padding-top: 1rem;
    border-top: 1px solid rgba(255, 255, 255, 0.4);
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
}

@media (max-width: 48rem) {
    .footer-layout {
        grid-template-columns: 1fr;
    }
}
```

### Why these rules?

- `.site-footer` gives the footer a dark background, readable text, and internal spacing.
- `.footer-layout` arranges the About and Sitemap groups into two columns on larger screens.
- `.footer-sitemap ul` removes default list bullets and indentation **only in the footer sitemap**.
- `.footer-sitemap li + li` selects each list item immediately following another list item, adding spacing **between** links without extra space before the first item.
- `.site-footer a:focus-visible` provides a visible outline for keyboard users.
- `.footer-bottom` uses Flexbox to align the closing text and Back to top link.
- The `@media` rule changes the two-column Grid to one column when the viewport is **48rem or narrower**.

**Note about CSS precedence:** Because these rules are added at the end of your stylesheet, they may override earlier rules with equal selector specificity. A more specific earlier selector can still win. Use browser Developer Tools to investigate unexpected styles.

**Checkpoint:** Save `styles.css` and refresh your browser. On a wide window, the About and Sitemap sections should appear side by side. On a narrow window, they should stack vertically.

---

## 7. Test and troubleshoot (about 3 minutes)

### Functional tests

1. Click **Home** in the footer. Does the page scroll to the hero?
2. Click **Features**. Does the page scroll to the Flexbox section?
3. Click **Resources**. Does the page scroll to the Grid section?
4. Click **Back to top**. Does the page return to the top?
5. Press **Tab** repeatedly to reach footer links. Can you see which link has keyboard focus? Press **Enter** to activate it.
6. Resize the browser to about **375px wide**. Do the footer columns stack without horizontal scrolling?

### Common problems and solutions

| Problem | Likely cause | What to check |
|---|---|---|
| A footer link does not scroll | Target ID missing or misspelled | Match `href="#name"` with `id="name"` exactly |
| Back to top does not work | Missing `id="top"` | Add it to the existing `<body>` opening tag |
| Footer has no styling | CSS file not linked or saved | Check `href="styles.css"`, file location, and Ctrl+S |
| Footer appears in the wrong place | HTML nesting problem | Put `<footer>` after `</main>` and before `</body>` |
| Footer text is hard to read | Colour conflict from existing CSS | Inspect styles and ensure sufficient contrast |
| Footer stays in two columns on mobile | Media query missing or overridden | Check the `@media` block and its closing brace |

**Debugging experiment:** Temporarily change `grid-template-columns: 1fr` inside the media query to `grid-template-columns: repeat(2, 1fr)`. Resize the browser and observe what changes. Restore `1fr` afterward.

---

## 8. Apply independently (about 2 minutes)

Complete **at least two** of these challenges:

- [ ] Replace the generic About text with a short description of your own practice website.
- [ ] Add a Contact link **only if** a matching Contact section already exists; otherwise create a simple Contact section with `id="contact"` before linking to it.
- [ ] Change the footer's spacing using an existing design token or a `rem` value.
- [ ] Add one more useful footer link to a real section on your page.

**Avoid:** Adding a fake copyright claim, invented contact details, or links to pages that do not exist.

---

## 9. Reflect (about 1 minute)

Answer these questions in your notes or be prepared to discuss them:

1. Why is `<footer>` more meaningful than using a generic `<div>` for the entire footer?
2. How does `href="#features"` find the correct location on the page?
3. What is the difference between an HTML sitemap and `sitemap.xml`?
4. Why does the footer need a responsive layout and visible keyboard focus?

---

## 10. Commit and push your work

Use VS Code Source Control or the terminal to commit the **new activity folder** to your **existing course repository**.

Suggested commit message:

```text
WS03-10 - Add semantic footer and HTML sitemap
```

1. Save `index.html` and `styles.css`.
2. Review the files in Source Control.
3. Stage the new `Workshop3/10-footer-sitemap/` files.
4. Commit with the suggested message.
5. Push or Sync Changes to GitHub.
6. Open your existing course repository on GitHub and verify the folder contains both files.

### Completion checklist

- [ ] I used my existing WEBD 1000 course repository.
- [ ] I created `Workshop3/10-footer-sitemap/`.
- [ ] My new folder contains `index.html` and `styles.css`.
- [ ] I preserved the completed WS03-09 files.
- [ ] My footer uses semantic HTML and a named navigation region.
- [ ] Every sitemap link points to an existing target.
- [ ] The Back to top link works.
- [ ] The footer is readable on desktop and mobile.
- [ ] Keyboard focus is visible on footer links.
- [ ] I committed and pushed the completed activity.

**Submission:** Keep your working files and reflection with your Workshop 03 work. No separate Brightspace submission is required for this micro-activity unless your instructor directs otherwise.

---

## Next activity — WS03-11: Multi-Page Website and Navigation

In the next activity, you will copy your completed files into `Workshop3/11-multi-page/`, create a second HTML page, and learn the difference between **same-page links** (`#features`) and **links to another file** (`about.html`). You will also update your navigation and footer sitemap to work across multiple pages.

**Instructor facilitation note:** The 30-minute target assumes the earlier site and Git tooling are working. Learners may need additional time to inspect existing IDs, correct HTML nesting, and complete GitHub authentication. Prioritize correct links and semantic structure before optional styling enhancements.
