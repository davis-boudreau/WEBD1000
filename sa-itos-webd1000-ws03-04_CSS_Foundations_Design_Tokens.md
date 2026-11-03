# WEBD 1000 — Workshop 03-04: CSS Foundations and Design Tokens

**Instructor:** Davis Boudreau  
**Duration:** Approximately 30 minutes (allow additional time for beginners)  
**Level:** Beginner | **Workshop:** 03 | **Activity:** 04  
**Learning focus:** CSS rules, selectors, the cascade, inheritance, custom properties (design tokens), typography, colour, spacing, and browser testing  
**Assessment:** Formative; keep technical evidence in your existing course repository

## What you will accomplish

In Workshop 03-03 you built a hero section. In this activity, you will **keep that working page** and make its appearance easier to manage. Instead of repeating the same colour and spacing values throughout `styles.css`, you will define a small set of reusable **design tokens** (CSS custom properties). You will also practise reading CSS rules, selecting elements, and checking whether a change affects the page.

By the end you should be able to:

1. Explain a CSS selector, declaration, property, and value.
2. Distinguish an element selector (`body`), a class selector (`.hero`), and a pseudo-class (`:hover`).
3. Define reusable CSS custom properties inside `:root` and access them with `var()`.
4. Apply consistent colour, type, and spacing to your existing header, navigation, hero, and buttons.
5. Test a deliberate change, fix a broken custom property, and commit your work.

> **Important:** Use your **existing WEBD 1000 course repository**. Do **not** create another GitHub repository for this workshop. Your separate semester website project repository is for the independent course project.

## Activity structure

| Stage | Suggested time |
|---|---:|
| Understand and predict | 5 minutes |
| Create folder and build | 15 minutes |
| Test and debug | 5 minutes |
| Apply and commit | 5 minutes |

## Part 1 — Create a new activity folder

Open your **existing WEBD 1000 course repository** in VS Code. In the Explorer panel:

1. Expand `Workshop3`.
2. Create a new folder called **`04-css-tokens`**.
3. **Copy**, rather than move, `index.html` and `styles.css` from `Workshop3/03-hero/` into `Workshop3/04-css-tokens/`.
4. Open the **new copies** in `04-css-tokens`. You will edit only these copies during this activity.

Your structure should resemble:

```text
YOUR-EXISTING-COURSE-REPO/
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
    └── 04-css-tokens/
        ├── index.html
        └── styles.css
```

**Checkpoint:** Before making changes, open `04-css-tokens/index.html` with Live Server (or in your browser). Confirm your header, navigation, hero text, image, and links still work. If the image does not appear, check whether its `src` uses a relative path to a file that was not copied. If Activity 03 used a local image, copy the required image into an `images/` folder within `04-css-tokens` and update its path. Keep `index.html` and `styles.css` as the two required main files.

## Part 2 — Understand CSS before editing it

### 2.1 What does a CSS rule mean?

```css
h1 {
    color: #004780;
    font-size: 2rem;
}
```

- **`h1` is the selector:** it identifies which HTML elements the rule targets (all `<h1>` elements).
- **`{ ... }` is the declaration block:** it groups the styles for the selected elements.
- **`color` and `font-size` are properties:** they identify what you want to change.
- **`#004780` and `2rem` are values:** they describe the chosen colour and size.
- **`:` separates** a property from its value; **`;` ends** each declaration.

The rule changes the text colour and font size of an `<h1>`; it does not change every paragraph or link.

### 2.2 How selectors work

Suppose your HTML contains:

```html
<section class="hero" id="home">
    <h1>Explore My Website</h1>
    <p>Discover what this site has to offer.</p>
</section>
```

| Selector | Meaning | Example use |
|---|---|---|
| `body` | Every `<body>` element (normally one per page) | Base font and page background |
| `h1` | Every `<h1>` element | Main heading typography |
| `.hero` | Any element with `class="hero"` | Hero background and padding |
| `.hero p` | Paragraphs inside an element with class `hero` | Hero paragraph width |
| `#home` | The element with `id="home"` | Target one specific section |
| `a:hover` | Links while a pointer hovers over them | Hover appearance |

**Class versus ID:** A class can be reused on many elements; an ID must be unique within a page. Prefer classes for reusable styling. IDs are useful for destinations such as `href="#home"`.

**Prediction:** If you change `.hero { background-color: ... }`, should the whole page background change or only the hero? Explain your answer before testing.

### 2.3 What are the cascade and inheritance?

CSS stands for **Cascading Style Sheets**. Multiple rules can affect the same element. The browser resolves conflicts using factors such as rule importance, specificity, and source order. For example, a `.hero h1` rule is more specific than a plain `h1` rule. If two equally specific rules conflict, the later one generally wins.

Some CSS properties **inherit** from parent elements. For example, `font-family` and `color` set on `body` often affect text inside it unless a more specific rule changes them. Other properties, such as `padding` and `background-color`, do **not** normally inherit.

**Practical rule for beginners:** Keep one clear rule for each component where possible. If an unexpected colour appears, search your CSS for other rules targeting the same element.

### 2.4 What is a design token?

Imagine using the same blue in the header, buttons, and links. If you type `#004780` in ten places, changing your design later means finding ten separate values.

A **design token** gives a reusable name to a design decision:

```css
:root {
    --color-primary: #004780;
}

h1 {
    color: var(--color-primary);
}
```

- **`:root`** selects the document's root element (the `<html>` element on an HTML page).
- **`--color-primary`** is a CSS custom property. Its name begins with two hyphens.
- **`var(--color-primary)`** reads the stored value wherever it is used.
- Defining tokens in `:root` makes them available to descendants through inheritance, unless overridden.

The name `--color-primary` is your choice; it is not a built-in CSS colour. Meaningful names are easier to maintain than names such as `--blue1`.

## Part 3 — Build a small design system

### Step 1 — Confirm the stylesheet connection

Open `04-css-tokens/index.html`. Inside `<head>`, confirm this line exists:

```html
<link rel="stylesheet" href="styles.css">
```

This relative path means `styles.css` is in the **same folder** as `index.html`. Do not link to the instructor's large reference `tokens.css` file; we are learning the underlying ideas with a smaller stylesheet first.

### Step 2 — Add tokens at the top of `styles.css`

Open `04-css-tokens/styles.css`. Add the following **at the beginning of the file**, above your existing rules:

```css
/* Reusable design decisions for this activity */
:root {
    /* Colours */
    --color-primary: #004780;
    --color-primary-dark: #00345e;
    --color-text: #14253a;
    --color-background: #edf2f7;
    --color-surface: #ffffff;
    --color-border: #cbd5e1;

    /* Typography */
    --font-body: Arial, Helvetica, sans-serif;
    --font-size-body: 1rem;
    --font-size-heading: 2rem;

    /* Spacing */
    --space-small: 0.5rem;
    --space-medium: 1rem;
    --space-large: 2rem;

    /* Shape */
    --radius-button: 0.5rem;
}
```

**Why these values?** `#004780` is a hexadecimal colour code; `1rem` is typically equivalent to the browser's default 16-pixel root font size unless the user/browser changes it. A spacing scale (`small`, `medium`, `large`) helps components feel consistent. The `/* ... */` text is a CSS comment: it explains the code but does not change the page.

### Step 3 — Replace repeated values in existing rules

**Do not erase the CSS you created in Activities 01–03.** Instead, find the matching existing declarations and replace their literal values with `var(...)`. Your class names may differ slightly from the examples below; use the class names in **your actual HTML**.

For the page body, use or update:

```css
body {
    background-color: var(--color-background);
    color: var(--color-text);
    font-family: var(--font-body);
    font-size: var(--font-size-body);
    margin: 0;
}
```

**Theory at the point of use:** `body` is an **element selector**. The `margin: 0` declaration removes the browser's default outer body margin. `font-family` provides preferred fonts in order; if Arial is unavailable, the browser tries Helvetica and then a generic sans-serif font.

Find your existing `.hero` rule and update its colour and spacing declarations. **Keep other declarations you already need** (such as borders or layout rules):

```css
.hero {
    background-color: var(--color-surface);
    padding: var(--space-large);
}
```

**Theory:** `.hero` is a **class selector** because it begins with a period. `padding` creates space *inside* the section's edges. `margin` would create space *outside* those edges. The example is a partial rule: if you already have `.hero` styles, edit that rule rather than adding a second duplicate rule.

Find your existing hero heading rule and change its font size and colour. For example:

```css
.hero h1 {
    color: var(--color-primary);
    font-size: var(--font-size-heading);
}
```

**Theory:** `.hero h1` is a **descendant selector**. It targets an `<h1>` only when it is inside an element with the class `hero`. This helps prevent a hero-specific style from changing headings elsewhere on your page.

### Step 4 — Apply tokens to your existing links and buttons

In Activity 03, you created two call-to-action links. Locate their current class names in `index.html` and the corresponding CSS rules in `styles.css`. If you used `.cta`, `.cta-primary`, and `.cta-secondary`, the following rules can guide your changes:

```css
.cta {
    display: inline-block;
    padding: var(--space-small) var(--space-medium);
    border-radius: var(--radius-button);
    text-decoration: none;
}

.cta-primary {
    background-color: var(--color-primary);
    color: var(--color-surface);
}

.cta-primary:hover {
    background-color: var(--color-primary-dark);
}

.cta-secondary {
    background-color: var(--color-surface);
    color: var(--color-primary);
    border: 1px solid var(--color-primary);
}
```

**Theory:** `display: inline-block` lets a link remain inline with nearby content while accepting useful box dimensions and spacing. In `padding: small medium`, the first value controls top/bottom and the second controls left/right. `border-radius` rounds corners. `:hover` is a **pseudo-class** that applies when a pointer hovers over the link. Keep keyboard focus visible too: do not remove browser focus outlines.

If your previous activity used different class names, **adapt these rules to your names rather than renaming or duplicating everything**. Confirm your header/navigation rules remain intact.

### Step 5 — Save and preview

Save both files (`Ctrl+S`). Open the **new** `04-css-tokens/index.html` in Live Server or your browser and refresh. You should still see your header, navigation, hero content, image, and both CTA links, now styled using reusable values.

## Part 4 — Test, predict, and debug

### Test A — Change one token, observe several elements

In `:root`, temporarily change:

```css
--color-primary: #8b1e63;
```

**Before refreshing, predict:** Which elements will change? Your hero heading? Primary button? Secondary button border? Background?

Save, refresh, and record what actually changed. Any rule using `var(--color-primary)` should update automatically. If an element did not change, inspect whether it still uses a literal colour or a different CSS rule.

Restore `--color-primary: #004780;` after the test, unless your instructor asks you to keep a personalized colour.

### Test B — Debug a misspelled token

Temporarily change one rule to:

```css
.hero h1 {
    color: var(--color-primry);
}
```

Refresh. The custom property name is misspelled. Since the variable is undefined and no fallback is provided, the `color` declaration is invalid at computed-value time; the heading may fall back to an inherited colour. Fix the spelling to `--color-primary` and refresh again.

A defensive alternative is:

```css
color: var(--color-primary, #004780);
```

The second value is a **fallback** used if the named custom property is unavailable or invalid.

### Troubleshooting checklist

- **No styling at all?** Verify `<link rel="stylesheet" href="styles.css">`, file spelling, and folder location.
- **Wrong activity appears?** Check that Live Server opened `04-css-tokens/index.html`, not Activity 03.
- **Some styles do not change?** Search for other matching CSS rules or hard-coded values.
- **A variable does not work?** Confirm it begins with `--`, is declared in `:root`, and is referenced with `var(--name)`.
- **Layout suddenly looks different?** Check for missing braces `{}` or semicolons `;` and compare with your preserved Activity 03 copy.
- **Image disappeared?** Confirm the image file and relative `src` path were copied correctly.

## Part 5 — Independent application

Complete these tasks without copying a complete replacement stylesheet:

1. Create a new token named `--color-accent` with a colour of your choice.
2. Use it to style one appropriate element (for example, a small label or secondary heading) without making text hard to read.
3. Change `--space-large` from `2rem` to `2.5rem`. Predict and then observe which components gain extra space.
4. Restore or keep a deliberate, readable design. Test the navigation and both hero links again.

**Optional extension:** Add `--space-extra-large: 3rem;` and use it for a section that needs more breathing room. Explain why you chose that spacing.

## Part 6 — Save technical evidence to GitHub

You are **not** creating a new repository. Save this activity in your **existing WEBD 1000 course repository**:

1. Save `Workshop3/04-css-tokens/index.html` and `styles.css`.
2. Open VS Code **Source Control**.
3. Review the changes; make sure the Activity 03 files were not accidentally overwritten.
4. Stage the Activity 04 files and any required local image assets.
5. Commit with the message: `WS03-04 - CSS foundations and design tokens`.
6. Push or sync to GitHub.
7. Open GitHub and confirm that `Workshop3/04-css-tokens/` contains the correct files.

**Submission:** Keep the completed files and commit history as technical evidence. No separate Brightspace upload is required unless your instructor directs otherwise.

## Completion checklist

- [ ] I used my **existing course repository**.
- [ ] I created `Workshop3/04-css-tokens/`.
- [ ] I copied `index.html` and `styles.css` from Activity 03.
- [ ] I can explain element, class, and descendant selectors.
- [ ] I added CSS custom properties in `:root`.
- [ ] I used `var()` for colours, typography, and spacing.
- [ ] My header, navigation, hero, image, and CTA links still work.
- [ ] I tested a token change and corrected a misspelled variable.
- [ ] I committed and pushed Activity 04 to GitHub.

## Reflection (brief)

1. What is the difference between a **CSS selector**, a **property**, and a **value**?
2. Why might a class selector such as `.hero` be preferable to styling every `section` element?
3. How does changing a token in `:root` differ from changing the same colour in five separate rules?
4. What happened when you misspelled a custom property name? How did you fix it?
5. Which part of your page will benefit most from consistent spacing as the website grows?

## Next activity — WS03-05: Desktop Header with Flexbox

In the next activity, create `Workshop3/05-flex-nav/`, copy forward the completed Activity 04 files, and learn how `display: flex`, `gap`, `justify-content`, and `align-items` help arrange a brand and navigation links in a desktop header. You will continue using your own small set of design tokens.
