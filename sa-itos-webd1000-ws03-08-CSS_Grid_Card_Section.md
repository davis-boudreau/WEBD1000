# WEBD 1000 — Workshop 03-08: Build a CSS Grid Card Section

**Instructor:** Davis Boudreau  
**Course:** WEBD 1000 — Website Development  
**Duration:** Approximately 30 minutes (allow extra time for beginners)  
**Activity:** 08 of 12 in Workshop 03  
**Learning outcomes:** Develop standards-compliant HTML/CSS webpages; use layout techniques appropriate to content and screen size.  
**Assessment:** Formative practice; retain technical evidence in your existing course repository.

## Overview

Your website already contains a header, responsive navigation, hero, and a **Features** section with Flexbox cards. In this activity, you will add a **Resources** section containing three cards arranged using **CSS Grid**. You will compare Grid with Flexbox, test how the layout changes at different widths, and preserve your work in a new activity folder.

**By the end, you should be able to:**

1. Explain a grid container, grid items, columns, rows, and gaps.
2. Use `display: grid`, `grid-template-columns`, `repeat()`, `minmax()`, and `gap`.
3. Use semantic HTML to create cards with meaningful list content.
4. Explain when CSS Grid or Flexbox is a useful choice.
5. Test and debug the page, then commit and push the new files.

**Prerequisite:** Complete WS03-07 or obtain the instructor's WS03-07 checkpoint files.

---

## 1. Understand: Why CSS Grid? (5 minutes)

In WS03-07, you used **Flexbox** to arrange feature cards along a row and let them wrap. Flexbox is excellent when the main concern is arranging items along **one axis** (a row *or* a column).

**CSS Grid** is a layout system for arranging content into **rows and columns together**. It is especially useful for card collections, galleries, and more complex page layouts.

```text
Grid container (.resource-grid)
┌────────────────────────────────────────────────────────┐
│  Column 1          Column 2          Column 3          │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   │
│  │ Resource A  │   │ Resource B  │   │ Resource C  │   │ Row 1
│  │             │   │             │   │             │   │
│  └─────────────┘   └─────────────┘   └─────────────┘   │
└────────────────────────────────────────────────────────┘
```

- **Grid container:** An element with `display: grid`.
- **Grid items:** The *direct children* of that container. Here, they are three `<article>` elements.
- **Column:** A vertical track in the grid.
- **Row:** A horizontal track in the grid.
- **Gap:** The space between tracks; unlike margins, it does not add space around the outside of the grid.

### Read this CSS rule before writing it

```css
.resource-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}
```

| Part | Explanation |
|---|---|
| `.resource-grid` | A **class selector** targeting `class="resource-grid"` |
| `display: grid` | Turns the element into a grid container |
| `grid-template-columns` | Defines the number and size of columns |
| `repeat(3, 1fr)` | Creates **three equal-width columns** |
| `1fr` | One fraction of the space available for grid tracks |
| `gap: 1rem` | Adds space between cards (often about 16px at default text size) |

**Prediction:** If the browser window becomes narrow, will three fixed columns still be comfortable to read? What might happen to the text?

We will improve the rule using `minmax()` so the number of columns can adapt automatically.

### Responsive Grid: `repeat()`, `auto-fit`, and `minmax()`

```css
.resource-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
    gap: 1rem;
}
```

Read this from the inside out:

1. **`16rem`** is our preferred minimum card width (about 256px with a 16px root font).
2. **`min(100%, 16rem)`** prevents that minimum from exceeding the width of a very narrow container.
3. **`minmax(..., 1fr)`** lets each column grow to use available space.
4. **`auto-fit`** allows the browser to fit as many columns as the container can comfortably hold.
5. **`repeat(...)`** creates those columns without requiring you to specify an exact number.

This is an example of **responsive layout without a media query**. You will explore more responsive techniques in WS03-09.

> **Accessibility reminder:** CSS controls visual placement; the HTML source order still matters for reading and keyboard navigation. Keep cards in a logical order in your HTML.

---

## 2. Prepare your activity folder (3 minutes)

**Use your existing WEBD 1000 course repository. Do not create another repository.** Your separate semester website project repository is not required for this workshop.

1. Open your existing course repository in VS Code.
2. Expand the `Workshop3` folder.
3. Create a new folder named **`08-css-grid`**.
4. **Copy** `index.html` and `styles.css` from `Workshop3/07-flex-cards/` into `Workshop3/08-css-grid/`.
5. Open the files **inside `08-css-grid`**. Do not edit the Activity 07 originals.

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
    │   ├── index.html
    │   └── styles.css
    └── 08-css-grid/
        ├── index.html
        └── styles.css
```

**Checkpoint:** Open `08-css-grid/index.html` using Live Server (or in a browser). Confirm your header, hero, mobile navigation, and Flexbox Features cards still work before making changes.

---

## 3. Build: Add the Grid section in HTML (7 minutes)

### Theory: Sections, articles, and HTML lists

A `<section>` groups related content and usually has a heading. An `<article>` represents a self-contained piece of content. For this activity, each article is a resource card.

The three cards demonstrate three types of HTML lists:

- `<ul>`: **Unordered list** — items where sequence is not important.
- `<ol>`: **Ordered list** — steps where sequence matters.
- `<dl>`: **Description list** — terms (`<dt>`) and descriptions (`<dd>`).

These are **semantic HTML elements**: they communicate meaning rather than merely controlling appearance. CSS Grid handles the layout; HTML lists communicate the content structure.

### Step 1 — Find the correct location

Open `Workshop3/08-css-grid/index.html`.

Inside `<main>`, locate the closing `</section>` tag for your **Features** section (`id="features"`). Insert the new Resources section **after Features and before `</main>`**. If an earlier activity left a placeholder section with `id="lists"`, **replace that placeholder** instead of creating a duplicate ID.

### Step 2 — Add the new section

```html
<section class="resources-section" id="lists" aria-labelledby="resources-title">
    <div class="resources-inner">
        <h2 id="resources-title">Useful Website Resources</h2>
        <p class="resources-intro">
            Explore the tools, steps, and terms used to build a website.
        </p>

        <div class="resource-grid">
            <article class="resource-card">
                <h3>Tools We Use</h3>
                <p>These tools support our website development workflow.</p>
                <ul>
                    <li>Visual Studio Code</li>
                    <li>Live Server</li>
                    <li>Git and GitHub</li>
                </ul>
            </article>

            <article class="resource-card">
                <h3>Our Workflow</h3>
                <p>Follow these steps when developing a webpage.</p>
                <ol>
                    <li>Plan the content</li>
                    <li>Write the HTML</li>
                    <li>Style with CSS</li>
                    <li>Test in the browser</li>
                </ol>
            </article>

            <article class="resource-card">
                <h3>Key Terms</h3>
                <p>Review these concepts from our activities.</p>
                <dl>
                    <dt>HTML</dt>
                    <dd>Defines webpage structure and content.</dd>
                    <dt>CSS</dt>
                    <dd>Controls visual presentation and layout.</dd>
                    <dt>Git</dt>
                    <dd>Tracks changes to project files.</dd>
                </dl>
            </article>
        </div>
    </div>
</section>
```

### Understand the attributes and selectors

- `class="resources-section"` allows CSS to style this section using `.resources-section`.
- `id="lists"` gives the section a unique destination for a link such as `href="#lists"`.
- `aria-labelledby="resources-title"` associates the section with its visible heading. The heading has `id="resources-title"`.
- `class="resource-grid"` identifies the **grid container**.
- Each `<article class="resource-card">` is a **direct child grid item**.

**Checkpoint:** Save `index.html` and refresh. The three resource cards should appear, but without Grid styling they will normally stack vertically. That is expected.

### Step 3 — Check the navigation link

Look at your existing navigation. If you want a link to this section, add an anchor to **each navigation menu** (desktop and mobile), using the same destination:

```html
<a href="#lists">Resources</a>
```

Place the anchor **inside the existing navigation structure** (for example, inside an existing `<li>` if your navigation uses a list). Do not replace the whole navigation or create a second `<nav>` just for this link. The link works because `href="#lists"` matches `id="lists"`.

---

## 4. Build: Style the Grid in CSS (7 minutes)

### Theory: Selectors, the box model, and design tokens

You already know that CSS rules follow this pattern:

```css
selector {
    property: value;
}
```

In the following code:

- `.resources-section` is a **class selector** for the outer section.
- `.resources-section h2` is a **descendant selector**: it styles `<h2>` elements inside `.resources-section`.
- `.resource-card` styles **every card** that has that class.
- `padding` adds space **inside** an element's border; `margin` adds space **outside** it.
- `var(--color-primary)` retrieves a reusable **CSS custom property** introduced in WS03-04.

### Step 1 — Add the styles

Open `Workshop3/08-css-grid/styles.css`. Add the following rules **at the end of the file, outside any existing `@media` block**:

```css
/* WS03-08: CSS Grid resource section */
.resources-section {
    padding: var(--space-large, 2rem) var(--space-medium, 1rem);
    background-color: var(--color-background, #edf2f7);
}

.resources-inner {
    max-width: 70rem;
    margin-inline: auto;
}

.resources-section h2 {
    color: var(--color-primary, #004780);
    margin-top: 0;
}

.resources-intro {
    margin-bottom: var(--space-large, 2rem);
}

.resource-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
    gap: var(--space-medium, 1rem);
}

.resource-card {
    background-color: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 0.75rem;
    padding: var(--space-medium, 1rem);
    min-width: 0;
}

.resource-card h3 {
    color: var(--color-primary, #004780);
    margin-top: 0;
}

.resource-card li {
    margin-bottom: 0.4rem;
}

.resource-card dt {
    font-weight: bold;
    margin-top: 0.75rem;
}

.resource-card dd {
    margin-left: 0;
}
```

**Why are there two values in `var(--space-medium, 1rem)`?** The first is the custom property name; the second is a **fallback** used if that property has not been defined. This lets your new section work even if your earlier token names differ slightly. If your WS03-04 stylesheet uses the recommended token names, those values will be reused.

**Why `min-width: 0`?** Grid items can sometimes refuse to shrink around long content. This rule allows a card to shrink within its track. It is not a substitute for wrapping very long unbroken text, but it helps prevent common overflow issues.

### Step 2 — Preview your work

Save `styles.css` and refresh the browser. The cards should now appear in columns when space permits, with consistent gaps and borders.

**Checkpoint:** Confirm the previous Flexbox Features section still works. You should now have **both** a Flexbox section and a Grid section on the same page.

---

## 5. Test, predict, and troubleshoot (5 minutes)

### Experiment A — Three fixed columns

Temporarily replace the `grid-template-columns` line with:

```css
grid-template-columns: repeat(3, 1fr);
```

Resize the browser window to a narrow width.

**Observe:** Do the three columns become too narrow? Does the text feel crowded?

### Experiment B — Responsive columns

Restore the responsive version:

```css
grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
```

Resize the browser again. Notice when the layout changes from three columns to two or one.

**Explain:** What did `auto-fit` and `minmax()` change?

### Experiment C — Inspect Grid in browser developer tools (optional)

Right-click a card and choose **Inspect**. Select the `.resource-grid` element. Many browsers show a **grid** badge or overlay that can highlight its tracks and gaps. This is a useful debugging technique.

### Troubleshooting guide

| Problem | What to check |
|---|---|
| Cards remain stacked on a wide screen | Confirm `.resource-grid` is spelled correctly in HTML and CSS; check `display: grid` |
| Cards look unstyled | Confirm `styles.css` is linked from `index.html`; save both files and refresh |
| Grid rules appear to do nothing | Check that new CSS was added **outside** an existing `@media` block and that braces `{ }` are balanced |
| Cards become too narrow | Restore `repeat(auto-fit, minmax(min(100%, 16rem), 1fr))` |
| Resources link does not work | Check `href="#lists"` matches the section's `id="lists"` exactly |
| Page contains two Resources sections | Remove or replace the old placeholder; HTML IDs must be unique |
| Earlier layout changed unexpectedly | Check for broad selectors such as `article` or `section` overriding styles; prefer the new class selectors |

---

## 6. Apply independently (3 minutes)

Complete **at least two** of these challenges without copying an additional finished solution:

1. **Personalize the content:** Replace the Tools card with three tools relevant to your own website topic.
2. **Change the layout:** Increase `gap` from `1rem` to `1.5rem` and describe what changed.
3. **Add a fourth card:** Create another `<article class="resource-card">` with a heading, paragraph, and list. Observe how Grid rearranges the cards.
4. **Compare approaches:** In one sentence, explain why Flexbox suited your Features section and why Grid suits this Resources section.

**Checkpoint:** Verify your page still works at desktop and narrow mobile widths. Do not leave the experimental fixed-three-column rule in place.

---

## 7. Reflect, commit, and push (approximately 2 minutes)

Answer these questions in your notes or discuss them during the class review:

1. What is the difference between a **grid container** and a **grid item**?
2. What does `1fr` represent?
3. Why is `repeat(auto-fit, minmax(...))` useful for responsive design?
4. How do CSS Grid and Flexbox differ?
5. How does a semantic `<ol>` differ from a `<ul>`?

### Git evidence

1. Save both files in `Workshop3/08-css-grid/`.
2. Open **Source Control** in VS Code.
3. Review the changed files; stage your Activity 08 files.
4. Commit with the message:

```text
WS03-08 - CSS Grid resource cards
```

5. **Push** or **Sync Changes** to your existing WEBD 1000 course repository.
6. Open GitHub and verify that `Workshop3/08-css-grid/index.html` and `styles.css` are present.

**Submission:** Keep the completed files and Git commit as technical evidence. No separate Brightspace upload is required unless your instructor directs otherwise. Follow your course's worksheet/reflection instructions where applicable.

---

## Completion checklist

- [ ] I used my **existing course repository**, not a new project repository.
- [ ] I created `Workshop3/08-css-grid/`.
- [ ] The new folder contains **`index.html` and `styles.css`**.
- [ ] I preserved the previous WS03-07 files.
- [ ] My page still has the header, hero, responsive navigation, and Flexbox Features section.
- [ ] My Resources section contains three semantic `<article>` cards with HTML lists.
- [ ] CSS Grid arranges the cards in columns and adapts when the browser narrows.
- [ ] My navigation link works, if I added one.
- [ ] I completed the experiments and independent practice.
- [ ] I committed and pushed my work to GitHub.

## Next activity — WS03-09: Responsive Layouts

You will apply responsive layout techniques to your **hero, Flexbox section, and CSS Grid section**, checking spacing, typography, overflow, and behaviour across screen sizes.

---

### Instructor facilitation notes

- **Timing:** 5 minutes theory; 3 minutes file preparation; 7 minutes HTML; 7 minutes CSS; 5 minutes testing; 3 minutes application. Reflection and Git can extend beyond the 30-minute target for novice learners.
- **Continuity:** The Grid section follows the existing `#features` Flexbox section. If an earlier activity created a `#lists` placeholder, replace it to avoid duplicate IDs. Keep existing styles and navigation.
- **Scope:** Focus on `display: grid`, columns, `repeat()`, `minmax()`, `auto-fit`, and `gap`. Defer explicit grid-area placement and complex spanning to later work.
- **Evidence:** Review a working responsive layout, semantic list markup, and the commit in the existing course repository.
