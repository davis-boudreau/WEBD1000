# WEBD 1000 — Workshop 03
## Semantic HTML & Multi-Page Website Development with a Tokenized CSS Design System

**Instructor:** Davis Boudreau  
**Term:** Fall 2026  
**Workshop:** WS03 | **Weight:** 3%  
**Related assessment:** Semester Project Milestone 3 — Functional HTML Website (6%, separately assessed)  
**Roadmap placement:** Weeks 5–6 (HTML structure followed by multi-page navigation and validation)  
**Primary outcome:** LO3 — Develop websites using HTML and CSS  
**Supporting outcomes:** LO1 — Evaluate usability and accessibility; LO2 — Plan and design websites  
**Tools:** VS Code, Live Server, browser DevTools, Git/GitHub, Figma, W3C Nu HTML Checker  
**Starting materials:** Course-provided `index.html` and `tokens.css` (Design System Studio V4.1)  
**Estimated effort:** Two class sessions (Weeks 5–6) plus independent completion, as needed

---

## 1. Workshop Details & Overview

### Purpose

In WS02 you developed a project brief, content inventory, sitemap, navigation plan, and wireframes in Figma. In WS03 you will **turn that plan into a working, linked, multi-page HTML website**. You will use the **course-standard tokenized CSS** rather than inventing a new stylesheet.

### Why this matters

HTML provides **meaning and structure**; CSS controls **presentation**. A shared design system lets developers reuse consistent layout, typography, colours, spacing, and components across pages. Building from a design specification is an essential professional workflow.

**Learning journey:** Inspect → Predict → Build → Run → Test → Debug → Refine → Commit → Push → Reflect.

### Learning objectives

By the end, you should be able to:

1. Explain how an HTML document is structured and how a stylesheet is linked.
2. Identify and use semantic elements including `header`, `nav`, `main`, `section`, `article`, and `footer`.
3. Translate your Figma sitemap into separate HTML documents with working relative links.
4. Adapt the provided HTML reference without removing its core accessibility features.
5. Reuse the provided `tokens.css` and recognize the distinction between tokens and component classes.
6. Test pages at desktop/mobile widths and with keyboard navigation.
7. Validate HTML, document fixes, and commit/push technical evidence to GitHub.

### Required evidence

A GitHub repository with **at least four linked HTML pages**, the shared `tokens.css`, appropriate content and accessible images, browser/validation test results, and a completed workshop worksheet/reflection. The Figma design remains the planning reference; **this workshop's code deliverables are not submitted in Figma**.

---

## 2. Prior Knowledge Check (record in worksheet)

1. What is the difference between a Figma frame and an HTML page?
2. What pages appear in your WS02 sitemap?
3. What is the difference between a file path and a URL fragment such as `#features`?
4. What does CSS control that HTML does not?
5. Predict: what happens if `index.html` references a stylesheet with the wrong filename?

Discuss your predictions with a classmate before testing.

---

## 3. Concepts & Theory: Just Enough to Start

### 3.1 HTML documents

An HTML document starts with a doctype and contains `html`, `head`, and `body`. The `head` contains metadata and stylesheet references; the `body` contains visible content.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>About | My Project</title>
  <link rel="stylesheet" href="tokens.css">
</head>
<body>
  <header><nav aria-label="Main navigation">...</nav></header>
  <main id="main-content"><h1>About</h1></main>
  <footer>...</footer>
</body>
</html>
```

**Try it:** Identify each of these parts in the supplied course `index.html`.

### 3.2 Semantic elements

| Element | Meaning | Typical use |
|---|---|---|
| `header` | Introductory content | Site branding and navigation |
| `nav` | Navigation region | Primary or footer links |
| `main` | Primary page content | One main landmark per page |
| `section` | Thematic content group | A section with a meaningful heading |
| `article` | Self-contained composition | Feature, post, or card |
| `footer` | Closing information | Contact, copyright, secondary navigation |
| `h1`–`h6` | Heading hierarchy | Structure content meaningfully |

**Rule:** Choose elements for meaning, not for their default appearance.

### 3.3 File links versus section links

The provided reference page uses **same-page links** such as `href="#features"`. Your new multi-page site needs **document links** such as `href="about.html"`.

```html
<a href="index.html">Home</a>
<a href="about.html">About</a>
<a href="contact.html">Contact</a>
<a href="index.html#features">Features on the homepage</a>
```

**Test:** A link to `#features` on `about.html` searches *about.html*, not `index.html`. Use `index.html#features` to navigate to the homepage section.

### 3.4 The course-standard tokenized CSS

The supplied stylesheet is titled **Design System Studio V4.1 — My Project** and is organized as **Foundation → Semantic → Components**. It includes custom properties (tokens) and reusable selectors. The provided HTML references classes such as `container`, `header-inner`, `hero-layout`, `feature-grid`, `card`, `nav-list`, `ds-button`, and `ds-button--primary`.

**Token:** A named reusable design value, commonly defined as a CSS custom property (`--...`) and used with `var(...)`.

```css
:root {
  --example-space: 1rem;
}
.example {
  padding: var(--example-space);
}
```

This is an **illustrative example**, not a replacement for the supplied token definitions. **Inspect the actual names in your `tokens.css` before editing anything.**

**Important source preparation:** The pasted `tokens.css` contains Markdown-escaped CSS comment markers (`/\*` and `\*/`) and other potentially escaped tokens (for example, universal selectors). The instructor must distribute a **verified, valid CSS copy** as `tokens.css`; students should not be asked to repair a damaged paste as a prerequisite. Preserve the supplied stylesheet's token names, design decisions, and component selectors.

### 3.5 Accessibility from the beginning

The reference `index.html` includes a skip link, labelled navigation, an `h1`, image alternative text, and labelled form fields. Preserve these patterns when adapting the page. A working site must be usable without a mouse.

---

## 4. Presentation & Demonstration: Read the Starter

Open the course `index.html` and `tokens.css` side by side.

**Find in `index.html`:**
- `<html lang="en" data-theme="light">`
- `<link rel="stylesheet" href="tokens.css">`
- `<a class="skip-link" href="#main-content">`
- `<header class="site-header">`, `<nav aria-label="Main navigation">`, and `<main id="main-content">`
- `.hero`, `.container`, `.card`, and `.ds-button` classes
- the responsive feature/list sections and labelled sample form

**Discuss:** Which elements describe meaning? Which classes connect HTML to CSS? Why is the stylesheet shared?

**Instructor note:** The sample contains a **static demonstration form**; it does not create accounts or store sign-ups. Students must not describe it as a working backend service. The source also contains same-page links; these must be adapted for the new multi-page project.

---

## 5. Workshop Challenge — Discuss & Analyze

**Challenge:** Implement the structure you designed in WS02 while preserving the shared design system.

Before coding, add these predictions to your worksheet:

1. Which Figma homepage section maps to the HTML hero?
2. Which parts of the starter can be reused on every page?
3. What will break if you duplicate `index.html` without changing navigation?
4. What is one accessibility feature you must preserve?

---

## 6. Guided Activities

### Activity A — Prepare the Project (What / Why / How)

**What:** Create the working folder and confirm the starter runs.  
**Why:** A reproducible structure prevents missing-file and path errors.

1. In VS Code, open your WEBD 1000 project folder or clone your course repository.
2. Save the instructor-verified starter files at the **same directory level**:

```text
webd1000-project/
├── index.html
├── about.html
├── services.html
├── contact.html
├── tokens.css
└── images/
```

*Replace page names with those in your WS02 sitemap. The three additional pages shown are examples.*

3. Start Live Server and open `index.html`.
4. Resize the browser; note the navigation, hero, cards, and footer.
5. Open DevTools → Network and confirm `tokens.css` loads successfully.

**Checkpoint:** The starter page renders with styling, and the CSS request does not return 404.

**Worksheet:** Predict and then test what happens if the stylesheet is renamed to `token.css` while the HTML still links to `tokens.css`. Restore the correct filename.

### Activity B — Investigate HTML Structure

**What:** Identify the semantic layout.  
**Why:** Understanding the starter helps you adapt it without breaking accessibility.

1. Find `header`, `nav`, `main`, `section`, `article`, and `footer`.
2. Locate the single primary `h1` and subsequent headings.
3. Identify the skip link and its `#main-content` target.
4. Find an image and its `alt` attribute.
5. In DevTools, inspect the rendered structure.

**Checkpoint:** You can explain what each landmark means and identify the matching Figma region.

**Worksheet:** Record one semantic element you did not recognize and explain its role.

### Activity C — Build Your Homepage from Figma

**What:** Adapt `index.html` to your own project.  
**Why:** The homepage should serve the user goals defined in WS02.

1. Open your WS02 Figma homepage wireframe and content inventory.
2. Replace the sample page title, metadata description, brand name, hero heading, introduction, and primary call to action with **your own meaningful content**.
3. Retain the semantic landmarks and the link to `tokens.css`.
4. Keep or adapt reusable component classes such as `container`, `hero-layout`, `card`, and `ds-button`.
5. Replace sample feature cards with content relevant to your project.
6. Remove sample sections that do not belong to your site, but keep the structure coherent.
7. If you remove the sample form, remove links to `#signup`. If you retain it, label it clearly as a **nonfunctional demonstration** unless an actual backend is supplied.

**Checkpoint:** Your homepage visibly reflects your own Figma plan and has one meaningful `h1`.

**Worksheet:** Identify two starter components reused and one section you substantially changed.

### Activity D — Create Three Additional HTML Pages

**What:** Implement at least three secondary pages.  
**Why:** The sitemap must become a functional document structure.

1. Choose three pages from your WS02 sitemap.
2. Create each `.html` file in VS Code.
3. Reuse the HTML document shell, stylesheet link, skip link, site header/navigation, main landmark, and footer.
4. Give every page a **unique** `<title>`, meaningful `h1`, and relevant content.
5. Use semantic sections and headings for content organization.
6. Avoid duplicate IDs **within the same page**.

**Checkpoint:** Four HTML pages open individually and display the shared stylesheet.

**Worksheet:** Match each new HTML filename to its Figma sitemap page.

### Activity E — Implement Working Navigation

**What:** Connect the pages with relative links.  
**Why:** Navigation is only useful if it reaches the intended destination.

Example:

```html
<nav aria-label="Main navigation">
  <ul class="nav-list">
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="services.html">Services</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
```

1. Adapt the example to your actual page names.
2. Use the **same primary navigation** across all four pages.
3. Test every link from **every** page.
4. Update footer navigation as well; do not leave sample links pointing to removed sections.
5. If you retain a link to a section on the homepage from another page, use `index.html#section-id`.

**Checkpoint:** Every primary navigation link works from every page, including after a browser refresh.

**Worksheet:** Record one broken link, the cause, and the fix.

### Activity F — Images, Lists & Accessibility

**What:** Add meaningful content without sacrificing accessibility.  
**Why:** Semantic markup helps people and assistive technologies understand the page.

1. Add at least one relevant image from a source you may legally use; place the file in `images/`.
2. Provide appropriate `alt` text for an informative image. Use `alt=""` only for purely decorative images.
3. Include a meaningful list (`ul`, `ol`, or `dl`) where the content calls for one.
4. Ensure each page has an `h1` and logically ordered section headings.
5. Confirm the skip link points to a real `main` target.
6. Test navigation with **Tab**, **Shift+Tab**, and **Enter**.
7. Zoom to **200%** and inspect whether content remains usable.

Example:

```html
<img src="images/community-garden.jpg"
     alt="Volunteers planting seedlings in raised garden beds">
```

**Checkpoint:** The image loads, alt text is meaningful, keyboard navigation works, and no essential information is lost at zoom.

**Worksheet:** Record one accessibility test, your observation, and any improvement.

### Activity G — Explore Tokens Without Rewriting the System

**What:** Inspect the supplied design system.  
**Why:** Learn how consistent visual decisions are reused across the site.

1. In `tokens.css`, locate `:root` and identify **three existing custom properties**.
2. Search for the selectors used by your HTML: `.container`, `.card`, `.hero`, `.nav-list`, and `.ds-button`.
3. Use DevTools → Styles/Computed to find which CSS rules affect a card or button.
4. Predict what would happen if a shared token changed.
5. **Optional experiment:** Make a temporary copy of the stylesheet, adjust **one existing token value**, observe the effect, then restore the original.

**Checkpoint:** You can identify a token, a component class, and a visible element affected by the CSS.

**Worksheet:** Record three actual token names from the supplied file and describe what they control.

**Boundary:** WS03 is primarily HTML. **Do not rewrite the design system**. WS04 will focus on CSS fundamentals and deliberate token customization.

### Activity H — Responsive & Browser Testing

**What:** Test the site at different widths.  
**Why:** A layout must remain usable beyond a single desktop screen.

1. Open DevTools device emulation.
2. Test a wide desktop, tablet-sized viewport, and narrow mobile viewport.
3. Check navigation wrapping, image sizing, card layout, text readability, and horizontal overflow.
4. Test each of the four pages.
5. Fix **HTML structure or content issues** you discover. Record CSS limitations for WS04/WS05 if they require more advanced styling.

**Checkpoint:** All pages remain readable and navigable at tested widths.

**Worksheet:** Record the three viewport sizes tested and one observation for each.

### Activity I — Validate, Debug & Commit

**What:** Verify HTML and preserve development evidence.  
**Why:** Validation and version control are normal professional practice.

1. Open the [W3C Nu HTML Checker](https://validator.w3.org/nu/).
2. Validate **each of your four HTML files** using the appropriate file-upload or direct-input method.
3. Record errors and warnings separately.
4. Fix markup errors you understand, then validate again.
5. In the browser, test the homepage and every navigation link once more.
6. Review changed files using Git.
7. Commit and push your work:

```bash
git status
git add .
git commit -m "Complete WS03 semantic multi-page website"
git push
```

8. Confirm the files appear in your GitHub repository.

**Checkpoint:** HTML files have been checked, broken links have been resolved, and GitHub contains the current work.

**Worksheet:** Record one validation finding and how you addressed it. Include the repository URL and latest commit identifier.

---

## 7. Collaborative Investigation & Instructor-Led Review

Work with a classmate to test each other's sites:

- Can the visitor identify the website's purpose?
- Can they reach all pages using navigation?
- Does the implementation resemble the WS02 Figma sitemap and wireframes?
- Are headings and links understandable?
- Does keyboard navigation work?

**Record:** Two peer observations and one change made because of feedback.

**Instructor:** Facilitate discussion, check depth of understanding, complete selected debugging steps alongside students, and emphasize *why* the markup is meaningful.

---

## 8. Checkpoints & Verification Summary

| Evidence | Verified |
|---|---|
| Course `index.html` and `tokens.css` run together | ☐ |
| Homepage adapted to WS02 Figma plan | ☐ |
| At least four HTML pages total | ☐ |
| Unique titles and meaningful `h1` headings | ☐ |
| Shared semantic header, navigation, main, footer | ☐ |
| Functional links from every page | ☐ |
| At least one meaningful image with appropriate alt text | ☐ |
| Lists and headings used semantically | ☐ |
| Skip link and keyboard navigation tested | ☐ |
| Desktop, tablet, and mobile widths tested | ☐ |
| All HTML files checked with validator | ☐ |
| CSS tokens and classes inspected | ☐ |
| Git commit and push completed | ☐ |
| Worksheet, peer review, and reflection completed | ☐ |

---

## 9. Workshop Worksheet (all students)

Complete this worksheet **during** the workshop. Use a Figma worksheet frame, Brightspace worksheet, or instructor-specified format; the **code itself** must be in VS Code/GitHub.

| Activity | Prediction / Decision | Observation / Test Result | Fix / Learning |
|---|---|---|---|
| A — CSS file path | | | |
| B — Semantic element | | | |
| C — Homepage adaptation | | | |
| D — Sitemap to files | | | |
| E — Broken link test | | | |
| F — Accessibility | | | |
| G — Three CSS tokens | | | |
| H — Viewport testing | | | |
| I — Validation | | | |

**Peer review:** Two observations and one improvement.  
**Evidence:** Repository URL, latest commit identifier, four HTML filenames.

---

## 10. Reflection & Exit Evidence

Answer briefly in the workshop worksheet and complete any Brightspace reflection required by the instructor:

1. How did your WS02 Figma sitemap guide your HTML file structure?
2. Why is semantic HTML preferable to using generic elements everywhere?
3. What is the difference between `about.html` and `#about` in a hyperlink?
4. How does a shared `tokens.css` improve consistency?
5. What did keyboard or mobile testing reveal?
6. Describe one error you encountered, how you diagnosed it, and how you fixed it.
7. What would you improve before Milestone 3?

**Exit statement:** In 2–3 sentences, explain how your HTML implementation reflects your Figma design and what still needs development.

---

## 11. Student Deliverables & Submission Guidelines

**All students** complete the workshop worksheet during activities, recording predictions, observations, test results, debugging findings, and reflections. They also complete the technical exercises and **commit/push their work to GitHub**.

**In-class students** complete the worksheet and participate in the instructor-led class review; they do not submit the worksheet unless otherwise directed. **Absent students** complete the full workshop independently and submit the completed worksheet to Brightspace.

**All students** provide the required technical evidence (GitHub repository URL and commit reference) through Brightspace as directed and complete the required Brightspace reflection. The Figma file from WS02 remains available for design reference; **WS03's website files belong in the GitHub repository, not in Figma**.

### Deliverables

1. Four or more connected HTML pages, including `index.html`.
2. The verified course-standard `tokens.css` used by every page.
3. Semantic HTML with consistent navigation, appropriate content, and accessible images.
4. Evidence of link, keyboard, responsive, and HTML validation testing.
5. GitHub repository URL and latest commit identifier.
6. Completed worksheet and reflection, following the attendance/submission protocol.

**Separate project assessment:** Milestone 3 — Functional HTML Website (6%) evaluates the project deliverable separately. Students should continue improving the **same repository**, rather than starting a second website.

---

## 12. Evaluation Criteria — A / P / T / F / R

| Criterion | Evidence |
|---|---|
| **A — Attendance** | In-class participation or completed independent alternative |
| **P — Participation** | Discussion, experimentation, peer review |
| **T — Task Progress** | Semantic pages, functional navigation, starter CSS integration, testing |
| **F — Focus & Professional Conduct** | Organized workflow, responsible use of tools, appropriate collaboration |
| **R — Reflection / Exit Evidence** | Worksheet, debugging observations, reflection, repository evidence |

**WS03 weight: 3%.** The separate **Milestone 3** carries **6%**.

---

## 13. Resources

- Instructor-provided `index.html` — semantic HTML reference
- Instructor-provided `tokens.css` — Design System Studio V4.1
- WS02 Figma sitemap and wireframes
- [MDN: HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [MDN: CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
- [W3C Nu HTML Checker](https://validator.w3.org/nu/)
- WEBD 1000 Brightspace and Teams

---

## 14. Academic Integrity & Copyright

Write and understand your own HTML. Peer discussion and troubleshooting are encouraged; submitting another student's work as your own is not. The provided course starter is authorized for this workshop. Use external images and other assets only when you have appropriate permission or licensing, and acknowledge sources as required.

---

## 15. Instructor Notes & Preparation

**Before delivery:**
1. Provide a verified, browser-tested `tokens.css` file. The original pasted CSS text contains escaped comment syntax; do not distribute an untested paste.
2. Provide the matching reference `index.html` and confirm stylesheet paths.
3. Check the sample's static sign-up form is described as a demonstration, not a functioning account system.
4. Decide whether to provide students a clean GitHub starter repository or distribute the two files directly.
5. Remind students that the reference uses single-page anchor links; their multi-page navigation must use filenames.
6. Prepare a short demonstration of DevTools, relative links, HTML validation, and Git push.

**Teaching approach:** Students work independently through concise embedded explanations and small testable tasks. The instructor circulates, asks students to explain their reasoning, and performs the same troubleshooting exercises where helpful.

**Scope:** Prioritize semantic HTML and working navigation. Token modification and deeper responsive CSS design are the focus of WS04 and WS05.

---

## 16. Next Steps

**WS02 — Figma plan → WS03 — Semantic HTML + shared design system → WS04 — CSS foundations and token customization → WS05 — Responsive layout development.**

Your sitemap now becomes a set of HTML files. Your wireframes become semantic page structures. Your shared `tokens.css` keeps presentation consistent while you learn how the system works.


---

## Appendix A — Guided Worked Example: From Figma Sitemap to Four HTML Pages

**Scenario:** Your WS02 sitemap contains Home, About, Programs, and Contact. The HTML filenames are `index.html`, `about.html`, `programs.html`, and `contact.html`.

**Prediction:** If you create four copies of the same homepage without changing their content, does that satisfy the sitemap? Explain why or why not.

**Worked step 1 — Build a consistent document shell.** Every page needs its own document metadata and primary content. The example below is intentionally small; reuse the actual course-standard classes and structure when adapting your starter.

```html
<!doctype html>
<html lang="en" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Learn about our community programs.">
  <title>Programs | Community Hub</title>
  <link rel="stylesheet" href="tokens.css">
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to main content</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html">Community Hub</a>
      <nav aria-label="Main navigation">
        <ul class="nav-list">
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="programs.html" aria-current="page">Programs</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>
  <main id="main-content" tabindex="-1">
    <section class="section container" aria-labelledby="programs-title">
      <h1 id="programs-title">Programs</h1>
      <p>Explore the activities available to our community.</p>
      <article class="card">
        <h2>Weekend workshops</h2>
        <p>Practical learning sessions for local residents.</p>
      </article>
    </section>
  </main>
  <footer class="site-footer website-footer">
    <div class="container"><p>&copy; Community Hub</p></div>
  </footer>
</body>
</html>
```

**Worked step 2 — Compare with your Figma wireframe.** Identify the navigation, main heading, content grouping, and footer. Add or adapt sections based on your own inventory. Do **not** copy the example's topic into your project unless it matches your approved concept.

**Worked step 3 — Test links.** From `programs.html`, click Home, About, and Contact. Return to Programs. Repeat from the other pages. `aria-current="page"` should identify the active page in each document; do not leave it on Programs when copying navigation into another file.

**Worked step 4 — Verify stylesheet reuse.** Open DevTools and inspect an element with `class="card"`. Find the matching CSS rule. If the rule is missing, check that `tokens.css` is present and the `href` is correct.

**Checkpoint:** Four distinct pages, matching the sitemap, share one stylesheet and have consistent navigation.

---

## Appendix B — Guided Debugging Scenarios

Complete at least **three** scenarios. For each, write **Prediction → Test → Observation → Diagnosis → Fix** in the worksheet.

| Scenario | Symptom to investigate | Useful test |
|---|---|---|
| 1 — Missing styles | HTML appears unstyled | Check the stylesheet `href`, Network panel, and file location |
| 2 — Broken navigation | About link opens a missing page | Compare `href` to actual filename, capitalization, and folder |
| 3 — Wrong section | Link to `#features` does nothing on another page | Check whether target `id` exists on the current page; try `index.html#features` |
| 4 — Missing image | Broken image placeholder | Compare `src` with the actual `images/` filename |
| 5 — Skip link failure | Skip link does not reach main content | Check that `href="#main-content"` matches `id="main-content"` |
| 6 — Incorrect current page | Every page announces Programs as active | Update `aria-current="page"` on the correct navigation link |

**Run and inspect:** Use Live Server, DevTools Elements/Network, and browser keyboard navigation. Change **one thing at a time**, retest, and record the outcome.

---

## Appendix C — Student Worksheet Template

**Student:** ____________________  **Date:** ____________________  
**Figma design link:** ____________________  **GitHub repository:** ____________________

### C1. Prior knowledge and predictions

1. HTML page versus Figma frame: ____________________
2. Four pages from my sitemap: ____________________
3. Predicted result of an incorrect CSS path: ____________________
4. Two reusable HTML regions: ____________________

### C2. Activity evidence

| Activity | What I tried | What happened | What I changed or learned |
|---|---|---|---|
| A — Starter setup | | | |
| B — Semantic HTML | | | |
| C — Homepage | | | |
| D — Additional pages | | | |
| E — Navigation | | | |
| F — Accessibility | | | |
| G — Tokens | | | |
| H — Responsive testing | | | |
| I — Validation/Git | | | |

### C3. Design system investigation

| Actual CSS token name | Value in supplied CSS | What it influences |
|---|---|---|
| | | |
| | | |
| | | |

### C4. Debugging log

| Problem | Prediction | Test performed | Cause | Fix and retest |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

### C5. Page verification

| Page | Unique title/h1 | Navigation works | CSS loads | HTML checked |
|---|---|---|---|---|
| `index.html` | ☐ | ☐ | ☐ | ☐ |
| Page 2: __________ | ☐ | ☐ | ☐ | ☐ |
| Page 3: __________ | ☐ | ☐ | ☐ | ☐ |
| Page 4: __________ | ☐ | ☐ | ☐ | ☐ |

**Test widths:** Desktop __________ px; tablet __________ px; mobile __________ px.  
**Keyboard test:** ____________________  
**Peer observation 1:** ____________________  
**Peer observation 2:** ____________________  
**Improvement applied:** ____________________  
**Latest commit:** ____________________

### C6. Reflection

Answer all seven reflection questions from Section 10 and provide the 2–3 sentence exit statement. Your responses should describe **your own** design decisions, tests, and debugging results.

---

## Appendix D — Instructor Review and Acceptance Criteria

The workshop is **ready for student use** when the instructor has confirmed that:

- The course starter HTML and **cleaned** `tokens.css` render together without CSS parse errors.
- The supplied reference's **same-page anchors** are explained before students build multi-page links.
- The sample **sign-up form is clearly identified as static**, with no real data collection or account creation.
- Students have access to their WS02 Figma planning work and a GitHub repository.
- A student can complete the instructions without a live instructor demonstration.
- Workshop assessment (3%) is separate from Milestone 3 (6%).

**Suggested pacing:** Session 1 — inspect starter, semantic structure, homepage, secondary-page shells. Session 2 — navigation, accessibility, design-system inspection, responsive tests, validation, peer review, GitHub, reflection. Students needing more time complete the remaining work independently.
