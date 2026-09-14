![alt text](image.png)

---

# **1. Workshop Details**

**Workshop Title:** CSS Tokens – Design System Foundations
**Course:** WEBD1000 – Website Development
**Duration:** 2 hours
**Prerequisite Workshops:** WS4, WS5, WS6, WS7

**Student Deliverables:**

* **GitHub Pages link** (submitted in *Brightspace Assignment Comments*)
* **Reflection answers** (submitted in *Brightspace Assignment Comments*)
* **CSS Validator screenshot**
  → **Uploaded as a file to Brightspace**
  → *(Only the screenshot needs to be uploaded — not the project.)*

---

# **2. Overview / Purpose / Objectives**

### **Purpose**

This workshop introduces **CSS design tokens**, a technique used by modern design systems (Google Material, IBM Carbon, Salesforce Lightning, Shopify Polaris).
Tokens help developers build:

* Consistent
* Scalable
* Maintainable
* Theme-ready

CSS across an entire project.

Students will create tokens for:

* Colors
* Typography
* Spacing
* Radii
* Semantic roles (header, nav, buttons)

Tokens unify design decisions, especially when working from Figma mockups — exactly how the CORAH project is structured.

---

# **Why This Workshop Matters (Deep Conceptual Framing)**

### **Design tokens solve the biggest real-world problem in CSS: consistency.**

Without tokens:

* Developers make arbitrary styling choices
* Colors drift away from the design
* Typography becomes inconsistent
* Hardcoded spacing leads to messy UI
* Changing a theme becomes impossible

With tokens:

* You can change the entire color system in one place
* Typography becomes predictable
* Spacing and radii match design intent
* UI components reference semantic values (“brand”, “header-bg”, “button-bg”)

### **This is how professional systems are built:**

| Company | Token Example            |
| ------- | ------------------------ |
| Google  | `--md-sys-color-primary` |
| IBM     | `--cds-spacing-03`       |
| Shopify | `--p-border-radius-base` |
| GOV.UK  | `--govuk-colour-brand`   |

Learning tokens prepares students for professional UI work.

---

# **Workshop Objectives**

Students will:

1. Build a reusable `:root` token block
2. Create base tokens (brand colors, neutral colors, spacing)
3. Create semantic tokens (header-bg, nav-link-color, button-bg)
4. Apply tokens to the CORAH header and hero section
5. Validate CSS using W3C requirements

---

# **3. Learning Outcomes Addressed**

### ✔ **LO4 – Implement CSS for responsive page layouts**

Tokens directly support responsive design and professional layout systems.

---

# **4. Assignment Description / Use Case**

Students will enhance the CORAH prototype by:

* Introducing a full CSS token system
* Applying tokens to the header, nav, hero, and typography
* Refactoring existing hardcoded values into semantic variables
* Building a foundation for WS9 (Responsive Design & Media Queries)

This is the shift from “classic CSS” into “design-system CSS”.

---

# **5. Tasks / Instructions (Step-by-Step)**

---

# 🔵 **STEP 1 — Prepare Your Project Folder**

Use this directory structure (same as WS5, WS6, WS7):

```
ws08/
 ├── index.html
 ├── styles.css
 └── images/
       ├── corah-brand-logo.svg
       ├── corah-brand-wordmark-logo.svg
       └── hero.jpg   (or instructor-provided image)
```

If you completed WS7, simply **duplicate** your folder and rename it `ws08`.

Ensure:

* `index.html` loads `styles.css`
* Images are in the `/images` folder
* Previous Flexbox layout is working

---

# 🔵 **STEP 2 — What Are CSS Tokens? (Technical Explanation)**

In CSS, tokens are custom properties defined in the `:root` selector:

```css
:root {
  --brand-600: #7B458F;
  --space-16: 16px;
  --font-size-base: 1rem;
}
```

These become reusable values throughout the stylesheet:

```css
color: var(--brand-600);
gap: var(--space-16);
font-size: var(--font-size-base);
```

### Why use tokens instead of hardcoded values?

| Hardcoded Example | Token Example               |
| ----------------- | --------------------------- |
| `color: #7B458F;` | `color: var(--brand-600);`  |
| `padding: 20px;`  | `padding: var(--space-16);` |

Tokens are more:

✔ Maintainable
✔ Scalable
✔ Readable
✔ Theming-ready
✔ Professional

---

# 🔵 **STEP 3 — Create Base Token Categories**

Inside `styles.css`, create the following structure:

```css
/* =========================================================
   DESIGN TOKENS
   ========================================================= */

:root {
  /* Brand Colors */
  --brand-50:  #F7EDF9;
  --brand-100: #EAD4F2;
  --brand-200: #D7AEE7;
  --brand-300: #C286DC;
  --brand-400: #A962D0;
  --brand-500: #8F4AC1;
  --brand-600: #7B458F;
  --brand-700: #62346E;
  --brand-800: #49264F;
  --brand-900: #311736;

  /* Neutral Colors */
  --neutral-50: #F9FAFB;
  --neutral-100: #F3F4F6;
  --neutral-200: #E5E7EB;
  --neutral-300: #D1D5DB;
  --neutral-400: #9CA3AF;
  --neutral-500: #6B7280;

  /* Typography */
  --font-family-body: "Open Sans", sans-serif;
  --font-family-heading: "Montserrat", sans-serif;

  --font-size-base: 1rem;
  --font-size-h1: 2.986rem;
  --font-size-h2: 2.488rem;
  --font-size-h3: 2.074rem;

  /* Spacing */
  --space-4: 4px;
  --space-8: 8px;
  --space-16: 16px;
  --space-24: 24px;
  --space-32: 32px;

  /* Radii */
  --radius-pill: 999px;
  --radius-md: 6px;
}
```

### Deeper Conceptual Notes:

* Base tokens represent raw design values (from Figma).
* Semantic tokens (next step) represent *meaning* not *value*.
* This separation mirrors real design systems.

---

# 🔵 **STEP 4 — Create Semantic Tokens**

Below the base tokens, add:

```css
  /* Semantic Tokens */
  --header-bg: var(--neutral-50);
  --header-border: var(--brand-600);

  --nav-link-color: var(--brand-600);
  --nav-link-bg-hover: var(--brand-600);
  --nav-link-text-hover: #FFFFFF;

  --hero-bg: #FFFFFF;

  --card-bg: #FFFFFF;
  --card-border: var(--neutral-200);
```

### Why semantic tokens?

They describe **purpose**, not **appearance**.

If CORAH rebrands:

* only semantic tokens change
* components don't need editing

This is industry best practice.

---

# 🔵 **STEP 5 — Apply Tokens to the Header**

Before (hardcoded):

```css
header {
  background-color: #F9FAFB;
  border-bottom: 2px solid #7B458F;
}
```

After (token-based):

```css
header {
  background-color: var(--header-bg);
  border-bottom: 2px solid var(--header-border);
}
```

Students see immediate benefit:

✔ One change affects entire UI
✔ Values become readable and meaningful
✔ Improves maintainability

---

# 🔵 **STEP 6 — Apply Tokens to the Navigation**

```css
nav a {
  color: var(--nav-link-color);
  border: 1px solid var(--nav-link-color);
}

nav a:hover {
  background-color: var(--nav-link-bg-hover);
  color: var(--nav-link-text-hover);
}
```

### Concept:

Navigation becomes flexible and themable.

---

# 🔵 **STEP 7 — Apply Tokens to the Hero Section**

```css
.hero-section {
  background-color: var(--hero-bg);
  padding: var(--space-32);
  gap: var(--space-24);
}
```

---

# 🔵 **STEP 8 — Apply Tokens to Cards**

```css
.feature-card {
  background-color: var(--card-bg);
  border: 1px solid var(--card-border);
  padding: var(--space-16);
  border-radius: var(--radius-md);
}
```

Students now see how a design system powers every part of the UI.

---

# 🔵 **STEP 9 — Validate Your CSS (Required)**

Go to:

➡ **[https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)**

Steps:

1. Paste `styles.css`
2. Validate
3. Fix errors
4. Validate again
5. Take a screenshot of “✔ Valid CSS!”

### 📌 Requirement:

**Upload the screenshot as a file to Brightspace.**
⭐ *Only the screenshot is uploaded — not the project.*

---

# 🔵 **STEP 10 — Publish to GitHub Pages**

Push your project to GitHub and activate GitHub Pages.

Submit:

```
https://yourusername.github.io/ws08-corah-site/
```

Submit this link in **Brightspace Assignment Comments**.

---

# **6. Deliverables (Submission Rules)**

Students must submit:

---

### ✔ 1. GitHub Pages Link

In **Brightspace Assignment Comments**

---

### ✔ 2. Reflection Answers

In **Brightspace Assignment Comments**

---

### ✔ 3. CSS Validator Screenshot

📁 **Uploaded as a file to Brightspace**

*(Only the screenshot needs to be uploaded — not the project.)*

---

# **7. Reflection Questions**

(Submit answers in Brightspace Assignment Comments)

1. Why are design tokens essential in large or long-term projects?
2. What advantages do semantic tokens provide over base tokens?
3. How did tokens simplify or clarify your CSS structure?
4. Which CORAH component benefited most from tokenization?
5. What feedback did the CSS validator give, and how did you fix it?

---

# **8. Assessment / Rubric**

| Criteria                   | Excellent                    | Good                     | Satisfactory       | Needs Improvement   |
| -------------------------- | ---------------------------- | ------------------------ | ------------------ | ------------------- |
| **Token Structure**        | Complete & well-organized    | Minor issues             | Acceptable         | Missing             |
| **Semantic Application**   | Consistent across components | Mostly consistent        | Some hardcoding    | Mostly hardcoded    |
| **Design System Thinking** | Strong                       | Good                     | Developing         | Not demonstrated    |
| **Validator Screenshot**   | Uploaded & valid             | Uploaded w/ minor issues | Uploaded w/ errors | Missing             |
| **Submission Compliance**  | All submitted correctly      | One part missing         | Minor issues       | Major missing items |

---

# **9. Resources**

* CSS Custom Properties (MDN)
* Design Tokens W3C Draft
* Material Design Token Guidelines

---

# **10. Academic Policies**

Insert NSCC standard text.

---

# **11. Copyright**

Workshop © NSCC – Educational Use
CORAH assets © NSCC 2025

---
