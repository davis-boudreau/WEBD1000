# WEBD 1000 — Workshop 03-09: Responsive Layouts

**Course:** WEBD 1000 — Website Development  
**Instructor:** Davis Boudreau  
**Duration:** Approximately 30 minutes (additional practice encouraged)  
**Level:** Beginner  
**Assessment:** Formative — part of Workshop 03  
**Learning focus:** Apply responsive HTML/CSS techniques and test a website at different viewport widths.

## Overview

In WS03-08, you created a CSS Grid section. In this activity, you will make the **existing hero section, Flexbox cards, and Grid cards** easier to use on narrow screens. You will also learn how to test your website at desktop, tablet, and phone widths.

**You will:**

1. Create a new activity folder in your **existing WEBD 1000 course repository**.
2. Copy your completed WS03-08 website into that folder.
3. Learn how viewport width, relative units, media queries, and fluid images work.
4. Improve your hero, Flexbox, and Grid layouts without changing the earlier checkpoints.
5. Test, reflect, commit, and push.

> **Important:** Do **not** create a new repository for this activity. The separate project repository is for your independent semester website project.

## 1. Understand: What does responsive mean? (5 minutes)

A **responsive website** adapts to the space available. A desktop screen may fit content side by side, while a phone screen may need the same content stacked vertically. Responsive design is about **readability and usability**, not simply making everything smaller.

### The viewport

The **viewport** is the area of the browser available for displaying a webpage. The following line, already in your HTML `<head>`, tells mobile browsers to use the device's width as the page viewport:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Without it, mobile browsers may display a scaled-down desktop layout.

### Fixed versus flexible sizes

```css
/* Fixed width: may overflow a narrow screen. */
.example-fixed { width: 900px; }

/* Flexible width: uses available space, up to a limit. */
.example-flexible { width: 100%; max-width: 900px; }
```

- `px` is a fixed CSS pixel unit.
- `%` is relative to the containing element.
- `rem` is relative to the root font size (often 16px unless changed).
- `max-width` sets an upper limit while allowing an element to be narrower.

### Media queries

A **media query** applies CSS only when its condition matches:

```css
@media (max-width: 48rem) {
    .example {
        padding: 1rem;
    }
}
```

This means: when the viewport is **48rem wide or narrower**, use `1rem` padding for `.example`. At a 16px root font size, 48rem is approximately 768px. Your WS03-06 mobile navigation already uses this idea.

### Predict before testing

If a page has three cards in one row, what might happen as the viewport becomes narrower? What would be more useful: tiny cards, horizontal scrolling, or wrapping/stacking?

## 2. Prepare the files (3 minutes)

1. Open your **existing course repository** in VS Code.
2. Inside `Workshop3`, create a folder named **`09-responsive`**.
3. Copy **both** `index.html` and `styles.css` from `Workshop3/08-css-grid/` into `Workshop3/09-responsive/`.
4. Open the **new** `index.html` and verify its stylesheet link is still:

```html
<link rel="stylesheet" href="styles.css">
```

Your folders should resemble:

```text
Your-Existing-Course-Repository/
└── Workshop3/
    ├── 01-html-basics/
    ├── 02-header-nav/
    ├── 03-hero/
    ├── 04-css-tokens/
    ├── 05-flex-header/
    ├── 06-mobile-nav/
    ├── 07-flex-cards/
    ├── 08-css-grid/
    └── 09-responsive/
        ├── index.html
        └── styles.css
```

**Checkpoint:** Preview the `09-responsive/index.html` file using Live Server. Confirm that you are editing the **new folder**, not WS03-08.

## 3. Build: Responsive CSS (15 minutes)

Your existing stylesheet may use different class names from the examples below. **Read the HTML first** and match the selectors to the classes you actually used. Do not add duplicate or conflicting rules without checking the existing ones. Add or update the rules in `09-responsive/styles.css`.

### Task A — Make images fluid

**Theory:** An image can have a large natural width. Setting `max-width: 100%` prevents it from growing wider than its container, and `height: auto` maintains its aspect ratio.

```css
img {
    max-width: 100%;
    height: auto;
}
```

**Check:** If your hero has an image, narrow the browser. It should shrink to fit rather than force the page to scroll sideways. If your hero does not yet have an image, keep the rule; it will help with future images.

### Task B — Constrain the page content

**Theory:** A content container can fill a narrow screen but stop growing on a very wide monitor. `margin-inline: auto` centres a block with a constrained width. `box-sizing: border-box` includes padding in the element's declared width.

```css
*,
*::before,
*::after {
    box-sizing: border-box;
}

/* Apply this class to a wrapper that surrounds your page content. */
.page-container {
    width: min(100% - 2rem, 70rem);
    margin-inline: auto;
}
```

If your HTML does not contain `.page-container`, you have two choices: add that class to an appropriate existing wrapper, **or** change the selector to match your existing wrapper class. Do not expect an unused selector to change the page.

**How `min()` works:** `min(100% - 2rem, 70rem)` chooses the smaller of the available width minus side space or a 70rem maximum. The `2rem` subtraction leaves breathing room on narrow screens.

### Task C — Improve the hero layout

**Theory:** CSS Grid can create two columns on wide screens and one column on narrow screens. A media query changes the column definition when there is less room.

First, inspect your hero markup. If it has a wrapper with the class `hero-layout`, use these rules. Otherwise, substitute your actual hero wrapper class.

```css
.hero-layout {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    gap: var(--space-large, 2rem);
    align-items: center;
}

@media (max-width: 48rem) {
    .hero-layout {
        grid-template-columns: 1fr;
    }
}
```

**Read the CSS:**

- `display: grid` turns the wrapper into a Grid container.
- `grid-template-columns` describes its columns.
- `1fr` means one share of available space.
- `minmax(0, 1fr)` lets a column shrink without overflowing because of long content.
- `gap` separates the columns; `var(--space-large, 2rem)` uses your WS03-04 design token, or `2rem` if that token is unavailable.
- The media query changes two columns into **one** at narrower widths.

**Important:** If your hero does **not** have two direct child blocks (for example, text and an image), you may not need a two-column grid yet. Keep its existing layout and focus on readable spacing. Avoid restructuring the page merely to match the example.

### Task D — Check the Flexbox card section

**Theory:** `flex-wrap: wrap` allows Flexbox items to move onto another row. `flex-basis` suggests an initial size; `flex-grow` and `flex-shrink` control how the items adjust.

Use the class name from your WS03-07 Flexbox card container. The example below assumes `.flex-cards`:

```css
.flex-cards {
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-medium, 1rem);
}

.flex-cards > article {
    flex: 1 1 15rem;
    min-width: 0;
}
```

**Read the shorthand:** `flex: 1 1 15rem` means **grow: 1; shrink: 1; basis: 15rem**. The cards can share extra room and wrap when there is not enough space. If your cards already use this approach, do not duplicate it; verify that it works.

### Task E — Check the CSS Grid card section

**Theory:** `repeat(auto-fit, minmax(...))` lets the browser decide how many columns fit, while keeping cards above a minimum size.

Use your WS03-08 Grid container's actual class name. The example assumes `.grid-cards`:

```css
.grid-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
    gap: var(--space-medium, 1rem);
}
```

**Read the CSS:**

- `repeat()` creates repeating column tracks.
- `auto-fit` fits as many columns as the available space permits.
- `minmax()` sets a minimum and maximum column size.
- `min(100%, 16rem)` prevents the minimum card width from exceeding a very narrow container.
- `1fr` lets each card expand to fill its column.

**Checkpoint:** Resize the browser slowly. The cards should move from multiple columns to fewer columns without being cut off.

### Task F — Add small-screen spacing

**Theory:** On a phone, generous desktop spacing may waste valuable room. Use a media query to reduce padding. Apply this to classes that **exist** in your HTML.

```css
@media (max-width: 48rem) {
    .hero {
        padding-block: var(--space-medium, 1rem);
    }

    .hero h1 {
        font-size: clamp(1.75rem, 6vw, 2.5rem);
    }
}
```

**How `clamp()` works:** `clamp(minimum, preferred, maximum)` keeps a value within limits. Here, the heading size grows with the viewport (`6vw`), but stays between `1.75rem` and `2.5rem`.

**Caution:** Keep your responsive navigation from WS03-06. If that activity already has a `@media (max-width: 48rem)` block, you may add these declarations inside it rather than creating conflicting rules. Multiple media query blocks are valid, but the cascade still matters.

## 4. Test and debug (5 minutes)

### Test three screen sizes

In Chrome or Edge, open your webpage, press **F12**, then select the **device toolbar** icon (or press **Ctrl+Shift+M**). Choose a device preset or enter the following approximate viewport widths:

| Viewport | Width to try | What to check |
|---|---:|---|
| Desktop | 1280px | Header navigation is visible; sections use available width well. |
| Tablet | 768px | Content does not overflow; cards reflow as needed. |
| Phone | 375px | Mobile menu works; text is readable; cards stack or wrap. |

Also test at **320px** to check narrow screens. These widths are testing examples, not a complete list of devices.

### Troubleshooting

| Problem | Likely cause | What to try |
|---|---|---|
| Nothing changes | CSS selector does not match your HTML | Compare `class="..."` in HTML with the CSS selector. |
| Hero still has two columns on a phone | Missing/overridden media query | Inspect the breakpoint and look for later conflicting rules. |
| Page scrolls sideways | Fixed widths or oversized content | Look for `width: 900px`, large images, or long unbroken text. |
| Cards stay in one row | Flexbox wrapping disabled | Check `flex-wrap: wrap`. |
| Grid cards overflow | Minimum column width too large | Use `min(100%, 16rem)` in `minmax()`. |
| Mobile menu disappears | Previous navigation rules were overwritten | Restore and retest the WS03-06 `<details>` navigation and media query. |

**Deliberate debugging:** Temporarily change `flex-wrap: wrap` to `nowrap`. Narrow the browser, observe what happens, and restore `wrap`. Explain the difference in your reflection.

## 5. Apply independently (2 minutes)

Complete at least **two** of the following:

- [ ] Reduce the hero's mobile padding and compare before/after.
- [ ] Adjust the Grid card minimum width from `16rem` to `14rem`; observe when columns change.
- [ ] Verify that every image stays within its container.
- [ ] Test the navigation using the **Tab**, **Enter**, and **Space** keys where appropriate.
- [ ] Identify and fix one element that causes horizontal scrolling.

## Reflection

Answer briefly in your own notes or workshop worksheet:

1. What is the difference between a fixed width and a flexible width?
2. What does `@media (max-width: 48rem)` mean?
3. Why is `max-width: 100%` useful for images?
4. How does `flex-wrap` differ from CSS Grid's `auto-fit`?
5. What changed when you tested at 375px compared with 1280px?

## Commit and push your work

1. Save `Workshop3/09-responsive/index.html` and `styles.css`.
2. In VS Code, open **Source Control** and review the changes.
3. Stage the new activity folder's files.
4. Commit with the message:

```text
WS03-09 - Responsive layouts
```

5. **Push/Sync** to your existing course repository.
6. Confirm on GitHub that `Workshop3/09-responsive/` contains **both** files.

**Submission:** Keep your completed activity and reflection as workshop evidence. Follow your instructor's existing Workshop 03 worksheet and Brightspace submission instructions; this activity does not create a separate graded submission.

## Completion checklist

- [ ] Created `Workshop3/09-responsive/` in my existing course repository.
- [ ] Copied the previous activity's `index.html` and `styles.css`.
- [ ] Tested responsive hero, Flexbox, and Grid behaviour.
- [ ] Verified mobile navigation still works.
- [ ] Checked desktop, tablet, and phone widths.
- [ ] Committed and pushed the activity files.

---

### Next: WS03-10 — Footer and HTML Sitemap

You will add a semantic footer with useful links and a visible HTML sitemap, while preserving the responsive behaviour you developed here.

**Instructor note:** The 30-minute target assumes students arrive with a working WS03-08 checkpoint. Allow additional time for students whose earlier HTML class names or layouts differ from the examples. The emphasis is on understanding and testing responsive behaviour, not copying selectors that do not match their code.
