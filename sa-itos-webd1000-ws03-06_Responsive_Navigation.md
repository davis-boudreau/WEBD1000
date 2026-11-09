# WEBD 1000 — Workshop 03-06: Responsive Navigation Without JavaScript

**Course:** WEBD 1000 — Website Development  
**Instructor:** Davis Boudreau  
**Duration:** Approximately 30 minutes (allow additional time for Git or debugging)  
**Activity:** Workshop 03, Activity 06 of 12  
**Learning focus:** Semantic HTML, responsive CSS, accessibility, and testing  
**Assessment:** Formative; retain evidence in the existing course repository

## Workshop overview

Your desktop navigation from WS03-05 works when the browser is wide. On a narrow phone screen, however, a row of links may wrap, overlap, or crowd the site name. In this activity you will **keep the desktop navigation** and add a **mobile menu that opens and closes without JavaScript**. You will use native HTML `<details>` and `<summary>` elements and a CSS **media query**.

### Learning objectives

By the end, you should be able to:

1. Explain why responsive navigation matters.
2. Describe what a CSS media query does and what `rem` means in a breakpoint.
3. Explain the purpose of `<details>`, `<summary>`, and `<nav>`.
4. Switch between desktop and mobile navigation at a breakpoint.
5. Test the menu with a mouse, keyboard, and narrow browser viewport.
6. Save your work in a new activity folder and push it to your **existing WEBD 1000 course repository**.

### What you will build

**Wide screen:** `My Website                         Home  Features  Contact`  
**Narrow screen:** `My Website                                     ☰ Menu`  
When the user activates **Menu**, a vertical list of navigation links appears.

> **Important:** You do **not** create a new GitHub repository. The separate repository used for your independent semester website project is not needed for this workshop.

---

## Part 1 — Prepare your files (3 minutes)

1. Open **VS Code** and open your existing WEBD 1000 course repository.
2. In `Workshop3`, create a folder named **`06-mobile-nav`**.
3. Copy **both** `index.html` and `styles.css` from `Workshop3/05-flex-header/` into `Workshop3/06-mobile-nav/`.
4. Open the **new copies**. Leave WS03-05 unchanged: it is your previous working checkpoint.

Your files should look like this:

```text
Existing-WEBD1000-Course-Repository/
└── Workshop3/
    ├── 01-html-basics/
    ├── 02-header-nav/
    ├── 03-hero/
    ├── 04-css-tokens/
    ├── 05-flex-header/
    │   ├── index.html
    │   └── styles.css
    └── 06-mobile-nav/
        ├── index.html
        └── styles.css
```

**Check:** The `<head>` of your new `index.html` must still contain:

```html
<link rel="stylesheet" href="styles.css">
```

**Why?** `href="styles.css"` is a **relative path**: the browser looks for `styles.css` beside the HTML file. A filename such as `style.css` or `activity.css` will not match.

---

## Part 2 — Understand responsive navigation (5 minutes)

### 2.1 What does *responsive* mean?

A responsive website adapts to the space available. A desktop may have enough width for several navigation links in one row; a phone often does not. We can present the same destinations in a more compact format on small screens.

### 2.2 What is a media query?

A media query applies CSS rules **only when a condition is true**.

```css
@media (max-width: 48rem) {
    /* These rules apply when the viewport is 48rem wide or less. */
}
```

- `@media` starts a conditional CSS block.
- `max-width` tests the width of the browser **viewport** (the visible page area).
- `48rem` is the breakpoint. With the usual 16-pixel root font size, 48rem is approximately 768 pixels. The actual pixel equivalent depends on the root font size.
- The `{ ... }` block contains ordinary CSS rules that take effect when the condition matches.

**Prediction:** At a browser width of 400 pixels, should these rules apply? **Yes.** At 1200 pixels, assuming the default root font size? **No.**

### 2.3 Why `<details>` and `<summary>`?

HTML includes built-in interactive elements:

```html
<details>
    <summary>Menu</summary>
    <p>Content appears when the menu opens.</p>
</details>
```

- `<details>` creates a disclosure widget that can open and close.
- `<summary>` is the visible control users activate.
- Content after `<summary>` is shown when the disclosure is open.
- Browsers provide the open/close behaviour **without JavaScript**.

**Try it mentally:** Clicking *Menu* changes the disclosure state. Pressing **Enter** or **Space** while the summary has keyboard focus should also toggle it.

### 2.4 What is the difference between `display: none` and `display: block`?

- `display: none` removes an element from the visual layout and normal keyboard/accessibility navigation.
- `display: block` displays an element as a block that usually starts on a new line.

We will use these properties to show **one navigation interface at a time**: desktop on wide screens and mobile on narrow screens. Both sets of links point to the same sections.

---

## Part 3 — Add the mobile menu HTML (7 minutes)

Open `Workshop3/06-mobile-nav/index.html`.

**Find your existing `<header>`** from WS03-05. Keep your existing brand/site title and desktop navigation. Add the new `<details>` block **inside the header**, after the desktop `<nav>` and before the closing `</header>`.

Here is a **complete example of the header**. Use it as a reference if you are unsure where the new code belongs. If your site uses different section IDs, adjust the `href` values to match the sections you already created.

```html
<header class="site-header">
    <a class="site-brand" href="#home">My Website</a>

    <!-- Navigation shown on wider screens -->
    <nav class="desktop-navigation" aria-label="Primary navigation">
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <!-- Navigation shown on narrow screens -->
    <details class="mobile-menu">
        <summary>☰ Menu</summary>
        <nav class="mobile-navigation" aria-label="Mobile navigation">
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </details>
</header>
```

### Understand the HTML you added

| HTML | Purpose |
|---|---|
| `class="mobile-menu"` | Gives CSS a way to select this specific `<details>` element. |
| `<summary>☰ Menu</summary>` | Creates the visible, keyboard-operable menu control. The `☰` character is a simple menu symbol. |
| `<nav>` | Identifies a group of navigation links. |
| `aria-label="Mobile navigation"` | Gives this navigation region a descriptive accessible name. |
| `<ul>` and `<li>` | Organize navigation links as a list. |
| `href="#features"` | Links to an element on this page with `id="features"`. |

**Important link check:** If your Activity 05 webpage uses `id="about"` instead of `id="features"`, change **both** navigation links to `href="#about"`. Do not leave links pointing to nonexistent sections.

**Avoid duplicate headings:** The header example is a replacement *reference*, not something to paste underneath your existing header. You should end up with **one site header**, one desktop navigation, and one mobile menu.

---

## Part 4 — Style the responsive menu (8 minutes)

Open `Workshop3/06-mobile-nav/styles.css`. Keep all your existing CSS from WS03-05, including design tokens and desktop Flexbox rules. **Append** the following new rules at the bottom of the file.

### Step A — Hide the mobile menu on wide screens

```css
/* Default: desktop navigation is visible; mobile menu is hidden. */
.mobile-menu {
    display: none;
}
```

**CSS theory:** `.mobile-menu` is a **class selector**. The leading period means “select any element with `class="mobile-menu"`.” `display: none` hides it until our media query changes the rule.

### Step B — Add a breakpoint and switch the navigation

```css
/* Narrow screens: switch from desktop links to the mobile menu. */
@media (max-width: 48rem) {
    .desktop-navigation {
        display: none;
    }

    .mobile-menu {
        display: block;
    }
}
```

**CSS theory:** The selector `.desktop-navigation` targets the existing desktop `<nav>`. Inside the media query, it becomes hidden. The `.mobile-menu` rule becomes `display: block`, overriding the earlier `display: none` rule **when the viewport meets the breakpoint condition**. Both rules target the same element with the same selector specificity, so the later applicable declaration wins.

### Step C — Style the summary and links

```css
.mobile-menu summary {
    cursor: pointer;
    padding: var(--space-small, 0.5rem);
    color: var(--color-primary, #004780);
    font-weight: bold;
}

.mobile-navigation ul {
    list-style: none;
    margin: 0;
    padding: var(--space-small, 0.5rem) 0;
}

.mobile-navigation li + li {
    margin-top: var(--space-small, 0.5rem);
}

.mobile-navigation a {
    display: block;
    padding: var(--space-small, 0.5rem);
    color: var(--color-primary, #004780);
    text-decoration: none;
}

.mobile-navigation a:hover {
    text-decoration: underline;
}

.mobile-menu summary:focus-visible,
.mobile-navigation a:focus-visible {
    outline: 3px solid var(--color-primary, #004780);
    outline-offset: 3px;
}
```

### Understand the new selectors

| Selector | What it selects |
|---|---|
| `.mobile-menu summary` | A `<summary>` inside an element with class `mobile-menu`. |
| `.mobile-navigation ul` | A list inside the mobile navigation. |
| `.mobile-navigation li + li` | A list item immediately following another list item (adds spacing between items). |
| `.mobile-navigation a` | Links inside the mobile navigation. |
| `.mobile-navigation a:hover` | Those links while a pointer is hovering over them. |
| `:focus-visible` | A focus state typically shown for keyboard navigation. |

### Understand the properties

- `cursor: pointer` indicates an interactive control when using a mouse.
- `padding` creates space **inside** an element's border.
- `margin-top` creates space **outside** an element, above it.
- `list-style: none` removes default list markers; the HTML remains a semantic list.
- `text-decoration: none` removes the usual underline; the hover rule restores one as a visual cue.
- `outline` and `outline-offset` provide a visible keyboard focus indicator.
- `var(--space-small, 0.5rem)` reads the design token created in WS03-04. If that variable is missing, CSS uses `0.5rem` as a fallback.

**Accessibility note:** Do not remove focus outlines without providing a visible replacement. Also, the menu's text label **Menu** is important: the ☰ symbol alone is not sufficiently descriptive.

### Optional alignment fix

If your mobile menu does not sit neatly at the right side of the header, check that the existing header uses Flexbox. Your previous activity should have something similar to:

```css
.site-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
}
```

**Do not duplicate this rule unnecessarily.** If your Activity 05 header already uses an equivalent rule, keep it. The mobile menu will act as another flex item when it becomes visible.

---

## Part 5 — Test and debug (4 minutes)

1. Save **both files** with **Ctrl+S**.
2. Open `Workshop3/06-mobile-nav/index.html` in a browser or with Live Server.
3. Widen the browser: the desktop links should appear, and the mobile menu should be hidden.
4. Narrow the browser to approximately phone width (for example, 400 pixels). The desktop links should disappear, and **☰ Menu** should appear.
5. Click **Menu** to open the links; click it again to close them.
6. Press **Tab** until the Menu control has focus, then press **Enter** or **Space**. Continue tabbing through the visible links.
7. Activate each link and confirm it reaches the correct section.

**Tip:** In most browsers, **F12** opens Developer Tools. The device toolbar (often **Ctrl+Shift+M**) lets you simulate a narrow viewport. You can also simply resize the browser window.

### Troubleshooting

| Problem | What to check |
|---|---|
| Menu never appears | Confirm `.mobile-menu` is inside the header and the media query uses `max-width: 48rem`. Narrow the browser enough. |
| Desktop and mobile links both show | Confirm `.desktop-navigation` is the actual class used on your desktop `<nav>`. |
| Menu appears but will not open | Confirm you used real `<details>` and `<summary>` elements, with `<summary>` directly inside `<details>`. |
| Menu opens but links do nothing | Compare each `href="#name"` with an actual `id="name"` on the page. |
| Styles seem missing | Confirm `styles.css` is linked, saved, and in the same folder as `index.html`. |
| Focus indicator is not visible | Test using **Tab** and check that no earlier CSS rule disables the outline. |

---

## Part 6 — Apply independently (2 minutes)

Complete **one** of these changes without copying a finished solution:

- Change the menu label from `☰ Menu` to `☰ Explore` while keeping a descriptive word.
- Change the breakpoint from `48rem` to `42rem`, resize the browser, and observe when the navigation switches.
- Add a new navigation link **only if** you also create or already have a matching section ID.

**Prediction and observation:** Before refreshing, predict what will change. Then test and compare the result with your prediction.

---

## Part 7 — Commit and push (1 minute)

1. Open **Source Control** in VS Code.
2. Review the new `Workshop3/06-mobile-nav/` files.
3. Stage your changes and commit with:

```text
WS03-06 - Responsive navigation
```

4. Select **Push** or **Sync Changes**.
5. Confirm both new files appear in the `Workshop3/06-mobile-nav/` folder on GitHub.

**Submission:** Keep this activity in your existing course repository. No separate Brightspace upload is required unless your instructor directs otherwise.

---

## Completion checklist

- [ ] I used my **existing course repository**, not a new project repository.
- [ ] I created `Workshop3/06-mobile-nav/`.
- [ ] The new folder contains `index.html` and `styles.css`.
- [ ] My desktop navigation works on a wide screen.
- [ ] My mobile menu appears on a narrow screen and opens/closes without JavaScript.
- [ ] Every navigation link targets an existing section.
- [ ] I tested the menu using a keyboard.
- [ ] I committed and pushed the files to GitHub.

## Reflection

1. What problem does a responsive navigation menu solve?
2. In your own words, what does `@media (max-width: 48rem)` mean?
3. What do `<details>` and `<summary>` provide without JavaScript?
4. Why is it important that keyboard users can see which link has focus?
5. What changed when you completed your independent experiment?

## Next activity — WS03-07: Flexbox Content Section

You will keep your responsive header and hero, copy the finished files into `Workshop3/07-flex-content/`, and build a new content section using Flexbox. You will learn how to arrange content items in rows and allow them to wrap as space becomes limited.

---

### Instructor notes

- **Sequence:** This is a cumulative activity. Students copy WS03-05 forward rather than modifying the old checkpoint.
- **Pacing:** A 30-minute target assumes Git/VS Code setup is already complete. Students who need longer may finish their commit afterward.
- **Scaffolding:** The complete header is provided as a reference, but students should preserve their actual section IDs and existing CSS classes when they differ.
- **Accessibility:** The native disclosure pattern works without JavaScript. The mobile and desktop navigation are mutually hidden by CSS; test focus and the open state. More advanced menu behaviour (such as closing automatically after navigation) is beyond this beginner activity.
- **Evidence:** The repository commit and functional webpage are sufficient formative evidence; avoid introducing a new graded submission.
