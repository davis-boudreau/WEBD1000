# Workshop: Exploring Screen Readers, Contrast Checkers, and Accessibility Tools in Web Development

### Duration: 2.5 – 3 hours

### Audience: Web development students / beginner developers

### Mode: Hands-on with guided discussion

---

## Workshop Objectives

By the end of this session, participants will be able to:

1. Explain the role of assistive technologies like screen readers in web accessibility.
2. Test websites using a screen reader and evaluate usability issues.
3. Check color contrast using online contrast checkers and browser extensions.
4. Use browser developer tools and accessibility plugins to audit accessibility issues.
5. Integrate accessibility checks into their own development workflow.

---

## Integrated Tutorial

### Part 1: Screen Reader Exploration (NVDA / VoiceOver / ChromeVox)

**Step 1: Introduction**

* Explain what screen readers are and how visually impaired users rely on them.
* Show basic commands: navigation by heading, landmark, or link.

**Step 2: Hands-On Practice**

* Have students install **NVDA (Windows)** or use **VoiceOver (Mac)** or **ChromeVox (Chrome Extension)**.
* Open a sample website (e.g., a university homepage).
* Tasks:

  * Navigate by headings (H key in NVDA).
  * Listen to link descriptions.
  * Try filling in a form using the screen reader.

**Example Solution:**
Students should notice when images lack `alt` text or when headings are not properly structured.

---

### Part 2: Contrast Checkers

**Step 1: Why Contrast Matters**

* Introduce WCAG guidelines: minimum contrast ratio 4.5:1 for body text, 3:1 for large text.

**Step 2: Hands-On Practice**

* Use tools like:

  * **WebAIM Contrast Checker** (online)
  * **Colour Contrast Analyzer** (desktop tool)
  * Browser extensions (e.g., Stark for Figma/Chrome)

**Activity:**

* Provide a sample HTML page with poor color contrast.
* Ask students to test contrast between text and background.
* Fix the CSS to meet WCAG standards.

**Example Solution:**

```css
/* Before */
body {
  background-color: #ffffff;
  color: #cccccc;
}

/* After */
body {
  background-color: #ffffff;
  color: #333333;
}
```

---

### Part 3: Browser Dev Tools for Accessibility

**Step 1: Introduction**

* Show Chrome DevTools > Lighthouse > Accessibility Audit.
* Highlight accessibility tree inspection.

**Step 2: Hands-On Practice**

* Open DevTools on a page.
* Run Lighthouse audit.
* Identify missing alt attributes, form label issues, contrast errors.

**Example Solution:**
Students may find:

* Missing `<label>` tags in forms.
* `<div>` buttons without `role="button"`.

---

### Part 4: Other Accessibility Tools

* **Wave Accessibility Tool**: Browser extension that visually overlays issues.
* **Axe DevTools**: In-browser automated accessibility checker.
* **Screen Magnifiers & Keyboard Navigation**: Demonstrate Tab-only navigation.

---

### Part 5: Mini-Practical Challenge

**Task:**
Provide a small webpage with accessibility issues (poor contrast, missing alt text, unlabeled form inputs, bad heading structure).

**Challenge Steps:**

1. Use a screen reader to test navigation.
2. Run contrast checker and fix CSS.
3. Use Lighthouse or Axe to identify issues.
4. Correct HTML & CSS for accessibility compliance.

**Deliverable:**
Each group submits an "Accessible Version" of the page.

---

## Wrap-Up

* Recap key lessons:

  * Accessibility is usability.
  * Testing with real assistive tools is essential.
  * Accessibility should be part of the design and development workflow.

* Provide Resources:

  * [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
  * [NVDA Screen Reader](https://www.nvaccess.org/)
  * [ChromeVox Extension](https://chrome.google.com/webstore/detail/chromevox/)
  * [WAVE Accessibility Tool](https://wave.webaim.org/)
  * [Axe DevTools](https://www.deque.com/axe/)


