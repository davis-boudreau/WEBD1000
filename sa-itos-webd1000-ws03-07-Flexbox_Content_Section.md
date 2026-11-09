# WEBD 1000 — Workshop 03-07: Build a Flexbox Content Section

**Instructor:** Davis Boudreau  
**Course:** WEBD 1000 — Website Development  
**Duration:** Approximately 30 minutes (allow extra time if needed)  
**Activity:** 07 of 12 in Workshop 03  
**Learning outcome:** Develop standards-compliant webpages using HTML and CSS; apply responsive layout techniques.  
**Assessment:** Formative practice; retain work in the existing course repository.

## Overview

Your website already has a header, navigation, hero section, design tokens, and a mobile menu. In this activity you will add a **Features** section containing three cards arranged using **CSS Flexbox**. On wide screens, cards appear side by side; on narrow screens, they wrap onto new rows.

**You will learn to:**

1. Explain the difference between a flex container and flex items.
2. Use `display: flex`, `gap`, `flex-wrap`, and `flex` to arrange cards.
3. Build semantic HTML using `<section>` and `<article>`.
4. Test the layout by resizing the browser.
5. Commit and push your completed activity to your **existing WEBD 1000 course repository**.

**Prior knowledge:** WS03-01 through WS03-06, especially class selectors, design tokens, and the Flexbox header.

## 1. Understand: What is Flexbox? (5 minutes)

Webpages often need to display a group of related items—for example, services, features, team members, or product highlights. Without a layout system, block elements generally appear one beneath another.

**Flexbox** is a CSS layout system for arranging items along one primary direction: a row or a column. It is particularly useful for navigation bars, groups of buttons, and card rows.

```text
Flex container (.feature-cards)
┌──────────────────────────────────────────────────┐
│  Card 1       Card 2       Card 3               │
└──────────────────────────────────────────────────┘
```

- **Flex container:** The parent element with `display: flex`.
- **Flex items:** Its *direct child elements*. In this activity, the three `<article>` elements are the flex items.
- **Main axis:** The direction items are arranged. The default is horizontal (`row`).
- **Cross axis:** The direction perpendicular to the main axis.

### CSS properties you will use

| Property | Meaning | Example |
|---|---|---|
| `display: flex` | Turns an element into a flex container | `display: flex;` |
| `gap` | Adds consistent space **between** items | `gap: 1rem;` |
| `flex-wrap` | Allows items to move to another row if necessary | `flex-wrap: wrap;` |
| `flex` | Controls how a flex item grows, shrinks, and starts at a preferred size | `flex: 1 1 15rem;` |
| `max-width` | Prevents a layout from becoming excessively wide | `max-width: 70rem;` |
| `margin-inline: auto` | Centres a constrained block horizontally | `margin-inline: auto;` |

### Read this rule before using it

```css
.feature-card {
    flex: 1 1 15rem;
}
```

`.feature-card` is a **class selector**: it targets elements with `class="feature-card"`.

The `flex` shorthand contains three values:

- **`1` — `flex-grow`:** A card may grow to share available space.
- **`1` — `flex-shrink`:** A card may shrink when space is tight.
- **`15rem` — `flex-basis`:** The preferred starting width before space is distributed. With the browser's usual 16px base font size, 15rem is approximately 240px.

The preferred width is **not** an absolute minimum. `flex-wrap: wrap` allows cards to move to another row when needed. The layout may show three, two, or one card per row depending on available width.

**Predict:** What might happen if we remove `flex-wrap: wrap`? You will test this later.

## 2. Prepare your files (3 minutes)

**Do not create a new GitHub repository.** Use your existing WEBD 1000 course repository.

1. Open your **existing course repository** folder in VS Code.
2. Expand `Workshop3`.
3. Create a new folder named **`07-flex-cards`**.
4. Copy `index.html` and `styles.css` from `Workshop3/06-mobile-nav/` into `Workshop3/07-flex-cards/`.
5. Open the **new copies** in `07-flex-cards`, not the files from Activity 06.

Your structure should resemble:

```text
Existing-Course-Repository/
└── Workshop3/
    ├── 01-html-basics/
    ├── 02-header-nav/
    ├── 03-hero/
    ├── 04-css-tokens/
    ├── 05-flex-header/
    ├── 06-mobile-nav/
    │   ├── index.html
    │   └── styles.css
    └── 07-flex-cards/
        ├── index.html
        └── styles.css
```

**Checkpoint:** Open `07-flex-cards/index.html` in Live Server or a browser. Your header, navigation, and hero should still work before you add anything.

## 3. Build: Add semantic feature cards (8 minutes)

### Theory: Why `<section>` and `<article>`?

A `<section>` groups related content, usually with a heading. An `<article>` represents a self-contained piece of content, such as a card describing a feature or service. We use these elements because their meaning is clearer than using `<div>` for everything.

An HTML **class** is a reusable name that CSS can select. Several cards can share the class `feature-card`, so one CSS rule styles all of them.

### Step A — Find the right place in your HTML

Open **`07-flex-cards/index.html`**. Locate the closing tag for your existing **hero section**, inside `<main>`. Insert the following code **after the hero section and before the closing `</main>`**. If your earlier activity already created a placeholder section with `id="features"`, **replace that placeholder** rather than adding a duplicate ID.

> Keep your existing header, desktop/mobile navigation, hero, and other sections. Do not replace your entire HTML document.

```html
<section class="features-section" id="features" aria-labelledby="features-title">
    <div class="features-inner">
        <h2 id="features-title">What You Can Explore</h2>
        <p class="features-intro">
            Discover three things this website will offer.
        </p>

        <div class="feature-cards">
            <article class="feature-card">
                <h3>Helpful Resources</h3>
                <p>Find useful information and practical guides.</p>
            </article>

            <article class="feature-card">
                <h3>Project Highlights</h3>
                <p>Explore examples, ideas, and featured work.</p>
            </article>

            <article class="feature-card">
                <h3>Get Connected</h3>
                <p>Learn how to find out more and get in touch.</p>
            </article>
        </div>
    </div>
</section>
```

**Understand the HTML:**

- `id="features"` creates the destination for a navigation link such as `href="#features"`.
- `aria-labelledby="features-title"` associates the section with its visible `<h2>` heading. The value must match the heading's `id`.
- `<h2>` is a subsection heading under your webpage's main `<h1>`.
- `<h3>` labels each individual feature card.
- `<div class="feature-cards">` is the parent container that Flexbox will control.
- Each `<article class="feature-card">` is a direct child of that container.

**Checkpoint:** Save and refresh. The cards will probably appear vertically and without card styling. This is expected: HTML provides the content; CSS will create the layout.

## 4. Build: Style the Flexbox layout (7 minutes)

Open **`07-flex-cards/styles.css`** and add the following rules **near the end of the stylesheet, outside any existing `@media` block**.

```css
/* WS03-07: Flexbox feature cards */
.features-section {
    padding: 3rem 1rem;
    background-color: var(--color-background, #edf2f7);
}

.features-inner {
    max-width: 70rem;
    margin-inline: auto;
}

.features-section h2 {
    color: var(--color-primary, #004780);
    margin-bottom: 0.5rem;
}

.features-intro {
    margin-bottom: 1.5rem;
}

.feature-cards {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}

.feature-card {
    flex: 1 1 15rem;
    min-width: 0;
    padding: 1.5rem;
    border: 1px solid #cbd5e1;
    border-radius: 0.75rem;
    background-color: #ffffff;
}

.feature-card h3 {
    color: var(--color-primary, #004780);
    margin-top: 0;
}
```

### Understand the CSS as you apply it

**1. Class selectors**

```css
.feature-cards { ... }
.feature-card { ... }
```

The period (`.`) means **select an HTML class**. `.feature-cards` targets the parent container; `.feature-card` targets each card. These names look similar but represent different elements.

**2. Descendant selector**

```css
.feature-card h3 {
    margin-top: 0;
}
```

This selects `<h3>` headings **inside** an element with the `feature-card` class. It does not change every `<h3>` on the website.

**3. Flex container versus flex item**

```css
.feature-cards {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}
```

These rules belong to the **parent**. The browser lays out its direct children as flex items.

```css
.feature-card {
    flex: 1 1 15rem;
}
```

This rule belongs to the **children** and describes how each card shares available space.

**4. Reusing design tokens**

```css
color: var(--color-primary, #004780);
```

`var()` reads the CSS custom property `--color-primary` introduced in WS03-04. The second value, `#004780`, is a **fallback** if that custom property is not defined. If your earlier activity used a different token name, use your existing name consistently.

**5. Spacing and sizing**

- `padding` adds space **inside** a box, between its content and border.
- `margin-bottom` adds space **outside** an element, below it.
- `gap` creates space **between flex items** without needing individual card margins.
- `max-width` limits the overall section width on large monitors.
- `min-width: 0` helps long content shrink rather than forcing unwanted horizontal overflow.

**Checkpoint:** Save both files and refresh. You should see three distinct cards, usually side by side on a wide screen.

## 5. Test and debug (4 minutes)

### Test A — Responsive behaviour

1. Open your page in a browser.
2. Make the browser window wide: observe the card layout.
3. Slowly narrow the window.
4. Observe whether the cards wrap onto a second row or stack vertically.
5. Check that the mobile menu from WS03-06 still works.

### Test B — Predict and observe

Temporarily change:

```css
flex-wrap: wrap;
```

to:

```css
flex-wrap: nowrap;
```

Resize the window again. **What changed?** Depending on the available space and content, cards may become narrower or overflow. Restore `flex-wrap: wrap` afterward.

### Troubleshooting

| Problem | Likely cause | What to check |
|---|---|---|
| Cards remain stacked on a wide screen | Flex rule not applied | `.feature-cards` spelling; stylesheet link; save/refresh |
| Cards have no white background or border | CSS rule missing | `.feature-card` selector and braces |
| Navigation link does not jump to cards | Anchor mismatch | `href="#features"` and `id="features"` must match |
| Cards overflow on a narrow screen | Wrapping disabled or fixed widths | Restore `flex-wrap: wrap`; avoid fixed card widths |
| Existing header or menu breaks | New CSS inserted inside an earlier rule or media query | Check closing braces `}` and where new rules were pasted |
| Unexpected colours | Token name differs | Compare `var(--color-primary, ...)` with your `:root` variables |

## 6. Apply independently (2 minutes)

Choose a topic related to your own website interests, and make these changes **without copying another complete example**:

- [ ] Replace the three card headings with topics relevant to your website.
- [ ] Rewrite the three descriptions in your own words.
- [ ] Change the card `gap` from `1rem` to `1.5rem`; observe the difference.
- [ ] Confirm that the cards still wrap on a narrow screen.

**Extension (optional):** Add a fourth `<article class="feature-card">` and observe how Flexbox distributes the cards.

## 7. Reflect, commit, and push (1–3 minutes)

**Reflection questions:**

1. Which element is the flex container, and which elements are the flex items?
2. What does `flex-wrap: wrap` do?
3. Why do all three cards use the same CSS class?
4. How does `gap` differ from `padding`?
5. What happened when you resized the browser?

**Save your work:**

1. Save `index.html` and `styles.css`.
2. Open VS Code **Source Control**.
3. Stage your changes.
4. Commit with the message: **`WS03-07 - Flexbox content section`**.
5. Push/sync to your **existing WEBD 1000 course repository**.
6. Verify `Workshop3/07-flex-cards/` appears on GitHub with both files.

**Submission:** Retain your working files and reflection for class review. No separate Brightspace upload is required unless your instructor directs otherwise.

## Completion checklist

- [ ] `Workshop3/07-flex-cards/index.html` exists.
- [ ] `Workshop3/07-flex-cards/styles.css` exists.
- [ ] Previous WS03-06 files remain unchanged.
- [ ] A semantic Features section contains at least three `<article>` cards.
- [ ] The section's `id` matches its navigation link.
- [ ] The cards use Flexbox and wrap on smaller screens.
- [ ] The existing responsive navigation still works.
- [ ] Changes are committed and pushed to the course repository.

## Next activity — WS03-08: CSS Grid Card Section

You will build another section using **CSS Grid**, compare Grid with Flexbox, and learn when each layout system is most useful.

---

### Instructor facilitation notes

- **Suggested timing:** Understand 5 min; prepare 3 min; HTML 8 min; CSS 7 min; test 4 min; independent application and Git 3+ min. For beginners, finishing the commit/push may extend beyond 30 minutes.
- **Teaching focus:** Emphasize parent-versus-child styling, class selectors, and the relationship between HTML structure and CSS layout. Encourage students to predict results before changing CSS.
- **Cumulative continuity:** Keep all existing content and navigation from WS03-06. Replace an existing `#features` placeholder instead of creating duplicate IDs. Keep `styles.css` as the only stylesheet unless the earlier activity deliberately established another one.
- **Evidence:** Students retain code in their course repository; no new graded assessment is created by this micro-activity.
