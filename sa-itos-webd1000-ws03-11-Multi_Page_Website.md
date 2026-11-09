# WEBD 1000 — Workshop 03-11: Multi-Page Website and Navigation

**Instructor:** Davis Boudreau  
**Duration:** Approximately 30 minutes (allow additional time for beginners)  
**Learning outcome:** Develop standards-compliant HTML/CSS websites  
**Assessment:** Formative workshop activity; no separate Brightspace submission unless directed  
**Prerequisite:** Completed WS03-10 (footer and HTML sitemap)

## Overview

Until now, your website has contained one HTML page. In this activity you will create a second page, connect both pages through the header and footer, and learn the difference between links to *files* and links to *sections within files*. You will continue using your **existing WEBD 1000 course repository**—do **not** create a new repository for this workshop. Your independent semester website project is separate.

**By the end you can:** create an additional HTML page, reuse a stylesheet, navigate between pages, fix relative paths, and test links with a mouse and keyboard.

## 1. Understand: Pages, links, and relative paths (5 minutes)

A **multi-page website** contains more than one HTML document. Each page can share a consistent header, navigation, and footer. For this activity:

- `index.html` is the home page.
- `about.html` is the second page.
- `styles.css` provides styles shared by both pages.

The browser uses the `href` attribute of an anchor (`<a>`) to decide where to go:

| Link | Meaning |
|---|---|
| `href="about.html"` | Open the file `about.html` in the same folder |
| `href="index.html"` | Open the home page in the same folder |
| `href="#features"` | Find the element with `id="features"` **on the current page** |
| `href="index.html#features"` | Open the home page, then jump to its `features` section |
| `href="about.html#contact"` | Open the About page, then jump to its `contact` section |

**Theory at the point of use:** A **relative path** describes a file's location starting from the current HTML document. Because `index.html`, `about.html`, and `styles.css` will live in the *same folder*, their links can use simple filenames. A path such as `../styles.css` would mean “look one folder above,” which is incorrect for this activity.

**Prediction:** If you are viewing `about.html`, where will `href="#features"` look for the `features` section? (Answer: on `about.html`, not on `index.html`.)

## 2. Prepare the new activity folder (3 minutes)

In VS Code, open your **existing course repository**. Under `Workshop3`, create a folder named `11-multi-page`. **Copy** your completed WS03-10 `index.html` and `styles.css` into it; do not move or overwrite the previous activity.

```text
Existing-Course-Repository/
└── Workshop3/
    ├── 01-html-basics/
    ├── 02-header-nav/
    ├── ...
    ├── 10-footer-sitemap/
    │   ├── index.html
    │   └── styles.css
    └── 11-multi-page/
        ├── index.html
        ├── about.html       ← create in this activity
        └── styles.css
```

**Checkpoint:** Open `11-multi-page/index.html` using Live Server or your browser. Verify that the copied home page still works before changing anything.

## 3. Build: Create the second HTML page (7 minutes)

Create `about.html` inside `11-multi-page` and enter the following complete example. Replace “My Website” and the example text with content appropriate to your practice website.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About | My Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <a class="skip-link" href="#main-content">Skip to main content</a>

    <header class="site-header">
        <div class="header-inner">
            <a class="site-brand" href="index.html">My Website</a>
            <nav aria-label="Primary navigation">
                <ul class="page-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="index.html#features">Features</a></li>
                    <li><a href="about.html" aria-current="page">About</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main id="main-content" class="page-content">
        <h1>About This Website</h1>
        <p>This page explains the purpose of my website and what visitors can find here.</p>

        <section aria-labelledby="mission-heading">
            <h2 id="mission-heading">Our Purpose</h2>
            <p>We want to share helpful information with our visitors.</p>
        </section>

        <section id="contact" aria-labelledby="contact-heading">
            <h2 id="contact-heading">Contact</h2>
            <p>Contact details will be added as the website develops.</p>
        </section>
    </main>

    <footer class="website-footer">
        <p>&copy; 2026 My Website</p>
        <nav aria-label="Footer navigation">
            <a href="index.html">Home</a>
            <a href="index.html#features">Features</a>
            <a href="about.html">About</a>
            <a href="about.html#contact">Contact</a>
        </nav>
    </footer>
</body>
</html>
```

### Understand the new HTML

- `<title>About | My Website</title>` changes the text displayed in the browser tab for this page.
- `<link rel="stylesheet" href="styles.css">` loads the same CSS file used by the home page. **One stylesheet can style multiple HTML files.**
- `aria-label="Primary navigation"` gives this navigation region an accessible name.
- `aria-current="page"` identifies the link to the page currently being viewed. Move this attribute to the Home link when editing `index.html`.
- `<main id="main-content">` provides a destination for the keyboard-accessible skip link.
- The `#contact` link works because the Contact section has `id="contact"`.

**Important compatibility note:** Your existing WS03-10 HTML may use different CSS class names or a native mobile menu. Keep that existing structure where practical. The example above demonstrates the required link behaviour; you do **not** need to replace your working responsive navigation with a simpler one. Instead, add the same Home, Features, and About destinations to both the desktop and mobile navigation already in your project.

## 4. Build: Connect the home page to About (5 minutes)

Open `11-multi-page/index.html`. Find your existing header navigation and add or update links so they point to real destinations:

```html
<a href="index.html" aria-current="page">Home</a>
<a href="index.html#features">Features</a>
<a href="about.html">About</a>
```

**Adapt these links to your existing list markup:** If your navigation uses `<ul>` and `<li>`, keep those elements and put each `<a>` inside its existing `<li>`. If your site uses a mobile `<details>` menu, update its links too.

Next, update your **visible footer sitemap** to include the second page:

```html
<nav aria-label="Website sitemap">
    <a href="index.html">Home</a>
    <a href="index.html#features">Features</a>
    <a href="about.html">About</a>
    <a href="about.html#contact">Contact</a>
</nav>
```

**Check your IDs:** The `#features` destination must match an actual `id="features"` in your home page. If your previous workshop uses a different section ID, change the link to match the ID you already have. Never create a link to a nonexistent section.

### CSS theory: Shared styles and selectors

Your `styles.css` already contains rules from earlier activities. These styles will affect `about.html` **only when its HTML matches the selectors**.

For example:

```css
.site-header {
    background-color: var(--color-primary);
}
```

The selector `.site-header` targets any element with `class="site-header"` on **either page**. It does not target every `<header>` automatically. If the new page uses a different class, this rule will not apply to it.

Add these small page-specific rules to the **bottom** of `11-multi-page/styles.css` if you do not already have equivalent styles:

```css
.page-content {
    max-width: 70rem;
    margin-inline: auto;
    padding: 2rem 1rem;
}

.page-content section {
    margin-block: 2rem;
}

.page-links {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    list-style: none;
    padding: 0;
}

.page-links a[aria-current="page"] {
    font-weight: bold;
    text-decoration: underline;
}
```

**Understand each selector:**

- `.page-content` is a **class selector** and styles the main content container.
- `.page-content section` is a **descendant selector** and targets `<section>` elements inside `.page-content`.
- `.page-links a[aria-current="page"]` combines a class selector, an element selector, and an **attribute selector**. It styles links inside `.page-links` only when they have the attribute `aria-current="page"`.
- `max-width` limits the width of a content area; `margin-inline: auto` centres it when space is available.
- `flex-wrap: wrap` lets links move to another line on narrow screens.

**Note:** If your existing navigation uses different classes, adapt the selectors instead of adding duplicate rules. Keep the responsive styles established in WS03-06 and WS03-09.

## 5. Test and debug (5 minutes)

Open `index.html`, then test the following:

| Action | Expected result |
|---|---|
| Select **About** in the header | Browser opens `about.html` |
| Select **Home** from About | Browser returns to `index.html` |
| Select **Features** from About | Browser opens `index.html` and jumps to the Features section |
| Select **Contact** from the footer | Browser opens `about.html` and jumps to Contact |
| Resize to a narrow viewport | Existing responsive/mobile navigation still works |
| Press **Tab**, then **Enter** on a link | Keyboard navigation works |

### Troubleshooting

**About link shows a missing file:** Confirm `about.html` is in `11-multi-page` and spelled exactly as linked.

**Styles are missing on About:** Confirm the stylesheet is named `styles.css` and both files are in the same folder. Check the `<link>` element.

**Features link does not scroll:** Confirm the home page contains the exact matching ID (for example, `id="features"`).

**The new page looks different:** Compare the class names on its header/footer with those in your working home page and existing CSS. Shared styles need matching selectors.

**Mobile navigation is broken:** Check that you preserved the existing `<details>`/`<summary>` markup and its CSS from WS03-06.

## 6. Apply independently (3 minutes)

Complete these challenges without copying a finished answer:

1. Add a new section titled **Frequently Asked Questions** to `about.html` with `id="faq"`.
2. Add a footer sitemap link that opens that section directly from `index.html`.
3. Update the About page's heading and introductory paragraph to reflect the topic of your practice website.

**Self-check:** The new link should use a filename **and** fragment identifier because the target is on another page.

## 7. Reflection and evidence (2 minutes)

Consider these questions:

1. What is the difference between `href="#contact"` and `href="about.html#contact"`?
2. Why can two HTML pages use one CSS file?
3. What does `aria-current="page"` communicate?
4. How do you diagnose a broken link?

**GitHub workflow:** Save both HTML files and the CSS file. In VS Code Source Control, stage your work, commit with the message `WS03-11 - Multi-page website`, and **push to your existing WEBD 1000 course repository**. Confirm the new `Workshop3/11-multi-page/` folder appears on GitHub.

**Student deliverables:** Complete the activity and reflection; retain your working files in GitHub. No separate Brightspace submission is required unless your instructor directs otherwise.

## Completion checklist

- [ ] Used my existing WEBD 1000 course repository
- [ ] Created `Workshop3/11-multi-page/`
- [ ] Copied the previous `index.html` and `styles.css`
- [ ] Created `about.html` in the new folder
- [ ] Linked Home and About in the header and footer
- [ ] Confirmed all section IDs match their links
- [ ] Preserved mobile navigation and responsive styling
- [ ] Tested links using the mouse and keyboard
- [ ] Committed and pushed to GitHub

---

### Coming next: WS03-12 — Testing, Validation and Publishing

In the final activity you will inspect your pages, validate HTML/CSS, test responsiveness and accessibility, and prepare a suitable site for GitHub Pages publication. Your **independent semester website project** remains separate from these guided activities.

> **Instructor note:** The 30-minute duration is a target. For beginners, building and testing a second page may take longer. Emphasize link correctness and shared styling over additional content. Students should not publish the workshop activity as a substitute for their semester website project.
