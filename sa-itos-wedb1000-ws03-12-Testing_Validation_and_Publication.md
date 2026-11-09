# WEBD 1000 — Workshop 03-12: Testing, Validation, and Publication Readiness

**Course:** WEBD 1000 — Website Development  
**Instructor:** Davis Boudreau  
**Workshop:** 03 — Activity 12 of 12  
**Estimated time:** 30 minutes (additional time may be needed to resolve validation errors)  
**Assessment:** Formative skills-building activity  
**Learning outcome:** Develop and test standards-compliant HTML/CSS websites, including responsive and accessible navigation.

## Overview

You have built a website one step at a time. In this final Workshop 03 activity, you will **copy your completed multi-page website into a new activity folder**, test it, validate its HTML and CSS, correct problems, and commit the verified version to your **existing WEBD 1000 course repository**.

**Important distinction:** Workshop activities stay in the existing **course repository**. Your independent **semester website project** has its own project-specific repository. Do **not** create another repository for this workshop. GitHub Pages publication belongs to the semester project workflow; this activity explains how to prepare for that step without publishing the entire course-workshop repository.

### Learning objectives

By the end, you should be able to:

1. Explain the difference between browser testing, standards validation, accessibility checks, and publication.
2. Check internal and cross-page links, images, and stylesheets.
3. Test a webpage at desktop and mobile widths.
4. Use an HTML validator and a CSS validator to identify and correct errors.
5. Identify basic accessibility issues using keyboard navigation and image alternative text.
6. Commit and push the tested files to the existing course repository.
7. Explain how a separate semester project can later be published with GitHub Pages.

## Part 1 — Understand: what does 'ready to publish' mean? (5 minutes)

A webpage that looks good in one browser is not necessarily ready to publish. Before sharing a website, check several different things:

| Check | Question it answers | Example |
|---|---|---|
| **Functional testing** | Does the site work? | Do navigation links open the correct page or section? |
| **Responsive testing** | Does it work at different widths? | Do cards stack and does mobile navigation work? |
| **HTML validation** | Does the markup follow HTML rules? | Are elements nested correctly and are required attributes present? |
| **CSS validation** | Is the stylesheet syntactically valid? | Is a property misspelled or a declaration malformed? |
| **Accessibility testing** | Can people use the site in different ways? | Can you navigate with the keyboard? Do meaningful images have useful `alt` text? |
| **Publication** | Can others access the site online? | Does the deployed website load at its public URL? |

**Theory — validation is not the same as testing.** A validator checks code against a language's rules. It cannot tell you whether your wording is clear, whether a link goes to the *intended* section, or whether your design is usable. You need both validation and real browser testing.

**Theory — GitHub is not the same as GitHub Pages.** Pushing files to GitHub stores your work in a repository. GitHub Pages is a separate publishing service that serves a website from a configured deployment source. A nested workshop folder does **not** automatically become the published homepage of a repository.

## Part 2 — Build: create your final activity checkpoint (4 minutes)

1. Open your **existing WEBD 1000 course repository** in VS Code.
2. In the Explorer, open `Workshop3`.
3. Create a new folder named **`12-test-validate`**.
4. From `Workshop3/11-multi-page/`, copy **all website files and folders** into `Workshop3/12-test-validate/`. This includes `index.html`, `about.html`, `styles.css`, and any local images or other assets you used.
5. Do not move or delete files from Activity 11. Each activity must remain a working checkpoint.

Expected minimum structure:

```text
Existing-WEBD1000-Course-Repository/
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
    ├── 10-footer-sitemap/
    ├── 11-multi-page/
    └── 12-test-validate/
        ├── index.html
        ├── about.html
        ├── styles.css
        └── images/             (only if your site uses local images)
```

**Checkpoint:** Open `12-test-validate/index.html` using Live Server or your browser. Confirm that you are testing the new copy, **not** Activity 11.

## Part 3 — Test: links, styles, and responsiveness (7 minutes)

### A. Test your navigation

On `index.html`:

- Select every desktop navigation link. Does it reach the intended section or page?
- Open the mobile menu and select every link.
- Select each call-to-action button/link.
- Select the footer sitemap links and **Back to top**.
- Open `about.html`, then navigate back to the homepage.

**Theory — relative paths and fragment identifiers:**

```html
<a href="about.html">About</a>
<a href="index.html#features">Features on the homepage</a>
<a href="#contact">Contact on this page</a>
```

- `about.html` means a file in the **same folder** as the current page.
- `index.html#features` means the element with `id="features"` on the homepage.
- `#contact` means the element with `id="contact"` on the **current page**.

A fragment link only works if the target ID exists and is spelled exactly the same way. Check that your links match the IDs actually used in your pages.

### B. Test at different widths

In your browser, open Developer Tools (usually **F12**) and activate device emulation, or manually resize the browser window. Test approximately:

| Viewport width | What to inspect |
|---|---|
| 1280px | Desktop navigation, hero layout, cards, and footer |
| 768px | Layout transitions and navigation breakpoint |
| 375px | Mobile menu, readable text, stacked cards |
| 320px | No clipped content or unwanted horizontal scrolling |

**Theory — viewport width is not device identity.** CSS media queries respond to the width available to the page, not simply whether someone is using a phone or computer. For example:

```css
@media (max-width: 48rem) {
    /* Rules here apply when the viewport is 48rem wide or narrower. */
}
```

At the usual browser default of 16px per `rem`, `48rem` is approximately 768px. Users can change default font settings, so think of this as a relative breakpoint rather than an absolute device category.

**Checkpoint:** At narrow widths, the mobile navigation works, images fit, and no important text is cut off.

## Part 4 — Validate your HTML and CSS (7 minutes)

### A. HTML validation

1. Open the official **Nu HTML Checker**: https://validator.w3.org/nu/
2. Choose the **Text Input** option and paste the entire contents of `12-test-validate/index.html`.
3. Run the check and read the messages.
4. Fix **errors** in VS Code, save the file, and validate again.
5. Repeat for `about.html`.

You can also use the **File Upload** option for local HTML files. Because workshop files may not be publicly published, do **not** assume the validator can retrieve them from a URL.

**Theory — errors versus warnings:** An **error** generally indicates markup that does not follow the specification. A **warning** identifies a potential issue that deserves review; it does not always mean the page is invalid. Read the message and its context rather than ignoring it or changing code blindly.

#### Example: a missing image alternative

Problematic HTML:

```html
<img src="images/hero.jpg">
```

Improved HTML for an informative image:

```html
<img src="images/hero.jpg"
     alt="A coastal trail overlooking the ocean">
```

**Why?** The `alt` attribute provides a text alternative for people who cannot see the image. Describe the image's purpose in context. For purely decorative images, `alt=""` may be appropriate; avoid unnecessary descriptions.

### B. CSS validation

1. Open the official **W3C CSS Validation Service**: https://jigsaw.w3.org/css-validator/
2. Choose **By direct input** and paste the contents of `styles.css` (or use file upload).
3. Run the check.
4. Correct reported CSS syntax or property errors in VS Code, then run the check again.

#### Example: an incorrect CSS property

```css
.hero {
    backgroun-color: #edf2f7;
}
```

The property name is misspelled. Correct it:

```css
.hero {
    background-color: #edf2f7;
}
```

**Theory — CSS error recovery:** Browsers often ignore declarations they do not recognize and continue rendering the rest of the stylesheet. This is useful for resilience, but it can make a typo easy to miss. Validation helps identify these mistakes.

**Checkpoint:** Record whether both HTML pages and your CSS pass validation. If a message remains, note what it says and what you tried; do not claim the code passed when it did not.

## Part 5 — Check accessibility and fix one issue (4 minutes)

### A. Keyboard navigation

1. Reload the homepage.
2. Press **Tab** repeatedly to move through interactive elements.
3. Confirm that you can identify which link or control currently has keyboard focus.
4. Use **Enter** to follow a link or activate a native `<summary>` menu.
5. Repeat on `about.html`.

**Theory — focus indicators:** People who navigate without a mouse need to see where they are on the page. Avoid removing outlines without providing a visible replacement.

For example, this rule can make keyboard focus easier to see:

```css
/* Add to styles.css if a clear focus indicator is missing. */
a:focus-visible,
summary:focus-visible {
    outline: 3px solid #f37327;
    outline-offset: 3px;
}
```

**What does `:focus-visible` mean?** It is a CSS pseudo-class that targets an element when the browser determines a visible focus indicator is appropriate, commonly during keyboard navigation.

### B. Check page structure

Confirm that:

- Each page has a meaningful `<title>` and a main `<h1>`.
- Headings describe the sections beneath them.
- Navigation links have understandable text.
- Informative images have useful `alt` text; decorative images use `alt=""` when appropriate.
- Text remains readable on narrow screens.

**Important:** These are introductory checks, not a complete WCAG accessibility audit. Passing HTML validation alone does not establish accessibility compliance.

## Part 6 — Apply independently (2 minutes)

Choose **one** improvement discovered during testing and make the correction yourself. Examples:

- Fix a broken link to `about.html` or a missing section ID.
- Correct a stylesheet path or image filename.
- Repair an HTML nesting error or CSS property typo.
- Improve an image's alternative text.
- Add a visible keyboard focus indicator.
- Prevent an image from overflowing a narrow screen.

After the change, **retest the affected behaviour** and rerun the relevant validator.

### Quick reflection

Answer briefly in your own words (in class discussion or your workshop worksheet, as directed):

1. How is browser testing different from HTML/CSS validation?
2. What did you discover when testing at 320px or 375px?
3. What is one accessibility issue that a validator might not detect?
4. Why should the semester website project be published separately from the course workshop repository?

## Part 7 — Commit and push your completed checkpoint (1 minute)

1. Save your files in VS Code.
2. Open **Source Control** and review the changes under `Workshop3/12-test-validate/`.
3. Stage your workshop files.
4. Use the commit message:

```text
WS03-12 - Test and validate multi-page website
```

5. **Commit**, then **Push** or **Sync Changes**.
6. Open your existing course repository on GitHub and confirm the new folder and files appear.

**Submission standard:** Preserve the working code in your course repository and complete your workshop worksheet/reflection as instructed. No separate project repository or GitHub Pages deployment is required for this activity.

## Looking ahead — publishing your semester website project

Your **semester website project** is a separate, independently developed website with its own appropriately named repository. When your instructor directs you to publish that project, GitHub Pages can host a static HTML/CSS site.

A common **project-repository** structure is:

```text
my-semester-website-project/
├── index.html
├── about.html
├── styles.css
└── images/
```

For a repository configured to deploy from a branch, GitHub Pages can publish from the branch's **root** or `/docs` directory. The homepage should be named `index.html` in the chosen publishing directory. Depending on repository settings, permissions, and account eligibility, you may need to enable Pages under **Settings → Pages** and select a deployment source. GitHub Pages may also be configured with a GitHub Actions workflow.

**Do not publish your entire course repository merely to complete Workshop 03.** Publishing and verifying the separate semester project is part of the project's assessment workflow.

Official reference: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

## Final WS03-12 checklist

- [ ] I used my existing WEBD 1000 course repository.
- [ ] I created `Workshop3/12-test-validate/`.
- [ ] My new folder contains `index.html`, `about.html`, `styles.css`, and any required assets.
- [ ] Both pages open, and the links work.
- [ ] I tested desktop, tablet, and narrow mobile widths.
- [ ] I checked both HTML pages using the Nu HTML Checker.
- [ ] I checked `styles.css` using the W3C CSS Validator.
- [ ] I tested keyboard navigation and image alternative text.
- [ ] I corrected at least one issue and retested it, or documented that no issue was found.
- [ ] I committed and pushed the completed activity to GitHub.

**Workshop 03 complete:** You now have twelve preserved, progressive website-building checkpoints. Use what you learned to build and validate your **independent semester website project**.
