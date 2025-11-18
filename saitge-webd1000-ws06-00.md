![alt text](image.png)

---


# **1. Workshop Details**

**Workshop Title:** Introduction to CSS – Selectors, Colors, Typography, Box Model
**Course:** WEBD1000 – Website Development
**Instructor:** Davis Boudreau
**Duration:** 1.5–2 hours
**Tools Required:** VS Code, Live Server, Browser DevTools
**Prerequisites:**

* WS4 – Semantic Markup
* WS5 – Text, Links, Images + Multi-page Structure

---

# **2. Overview / Purpose / Objectives**

### **Purpose**

This workshop introduces students to **core CSS concepts** that power every modern website:

* **Selectors** (element, class, ID, descendant)
* **Colors** (hex, rgb, hsl, design token variables)
* **Typography basics** (font-family, font-size, line-height)
* **Box model** (margin, padding, border, content box)
* **External CSS architecture** (why we use `styles.css`)

Using the CORAH header, students will learn how CSS interacts with HTML to create layout, color, spacing, and typography.

### **Why This Matters**

CSS is where meaning (HTML) becomes *experience*.
Understanding CSS fundamentals is essential to:

* Creating consistent branding
* Making pages readable and aesthetic
* Scaling a website across multiple pages
* Preparing for Flexbox (WS7), Tokens (WS8), and Responsive (WS9)

The CORAH case study is ideal because it includes:

* A nav system requiring consistent button styles
* A color palette
* A typography scale (Open Sans + Montserrat)
* A fluid spacing system
* A real organization brand identity

### **Workshop Objectives**

Students will learn to:

1. Apply CSS using external stylesheets
2. Use selectors effectively (element, class, descendant)
3. Style text with fonts, sizes, colors, weights
4. Apply color variables from the CORAH design system
5. Understand and experiment with the CSS box model
6. Inspect and debug CSS using DevTools

---

# **3. Learning Outcomes Addressed**

### **LO3 – Develop W3C-compliant websites using HTML & CSS**

CSS must follow best practices for:

* Maintainability
* Valid property/value use
* Accessible contrast
* Standards alignment

---

# **4. Assignment Description / Use Case**

Students will:

* Explore and edit the CORAH `styles.css` file
* Apply CSS to control typography, colors, spacing
* Understand how selectors map to the CORAH header HTML
* Practice styling buttons, text, images
* Apply borders, padding, margin to understand the box model

This workshop prepares students for:

* WS7 Flexbox layout of the CORAH header
* WS8 token-based design system
* WS9 responsive layout adaptation

---

# **5. Tasks / Instructions (Step-by-Step)**

This workshop builds concept → demonstration → hands-on coding.

---

## 🔵 **STEP 1 — Linking an External Stylesheet**

**Concept Background:**
Three ways to apply CSS:

1. Inline (`style="color:red"`) – *never use for production*
2. Internal (`<style>` in `<head>`) – ok for one-offs
3. External (`<link rel="stylesheet">`) – *professional standard*

External CSS:

* Works across multiple pages
* Enables caching + performance
* Supports modular, scalable design

**Task:**
Open `index.html` and verify:

```html
<link rel="stylesheet" href="styles.css">
```

If missing, add it.

---

## 🔵 **STEP 2 — Understanding CSS Selectors in the CORAH Project**

### **Key Selector Types**

| Selector       | Example               | Meaning                            |
| -------------- | --------------------- | ---------------------------------- |
| **Element**    | `header {}`           | selects all headers                |
| **Class**      | `.nav-link {}`        | reusable style hook                |
| **ID**         | `#hero-title {}`      | unique element (avoid for styling) |
| **Descendant** | `.nav-container a {}` | targets nested elements            |

**Task:**
In `styles.css`, locate:

```css
.nav-link { ... }
.nav-button { ... }
.header-section-container { ... }
```

Explain in comments:

* How the selector works
* Which HTML it matches
* Why a class is used (vs element)

Example:

```css
/* 
  .nav-link targets all a.nav-link elements 
  used for CORAH's primary navigation styling
*/
.nav-link {
  ...
}
```

---

## 🔵 **STEP 3 — Apply Colors Using Tokens**

**Background:**
CSS color formats:

* Hex: `#7B458F`
* RGB: `rgb(123,69,143)`
* HSL: `hsl(285 32% 42%)`
* CSS variables: `var(--brand-600)`

Your CORAH site uses a **design token color ramp**, so students will learn:

```css
color: var(--brand-600);
background-color: var(--neutral-50);
border-color: var(--color-header-link-secondary-border);
```

**Task:**
Change the color of all `<h1>` elements to the CORAH brand color:

```css
h1 {
  color: var(--brand-600);
}
```

**Conceptual Insight:**
This is how we connect brand identity → coded UI.

---

## 🔵 **STEP 4 — Typography: Fonts, Scale, Weights**

### **Background Knowledge**

Typography affects:

* Readability
* Brand voice
* Accessibility
* User trust

CORAH uses:

* **Body font:** Open Sans → warm, readable
* **Heading font:** Montserrat → modern, bold

**Your tokens define fluid sizes:**

```css
--font-size-base: clamp(...);
--font-size-h1: clamp(...);
```

**Task:**
Modify a paragraph’s font styling:

```css
p {
  font-size: var(--font-size-p);
  line-height: var(--line-height-base);
  color: var(--neutral-800);
}
```

**Mini Exercise:**
Change line-height and observe how spacing changes visually.

---

## 🔵 **STEP 5 — The CSS Box Model (Critical Concept)**

### **Conceptual Background (Deeper Insight)**

Every element in CSS is a “box” with:

```
┌───────────────────────────┐
│        margin             │  (space outside)
│  ┌─────────────────────┐  │
│  │       border        │  │
│  │  ┌───────────────┐ │  │
│  │  │    padding    │ │  │
│  │  │ ┌───────────┐ │ │  │
│  │  │ │  content  │ │ │  │
│  │  │ └───────────┘ │ │  │
│  │  └───────────────┘ │  │
│  └─────────────────────┘  │
└───────────────────────────┘
```

The CORAH buttons demonstrate this:

* **Padding** controls the breathing room inside
* **Border** creates the pill shape
* **Margin** creates spacing between buttons

### **Task: Inspect the Button in DevTools**

Instructions:

1. Right-click a nav link → Inspect
2. Look at the **Computed** panel
3. Expand **Box Model**
4. Modify padding live

Then apply CSS updates:

```css
.nav-link {
  padding: 0.6em 1.4em;
  border-radius: var(--radius-pill);
}
```

**Learning Insight:**
UI design is 70% spacing decisions.

---

## 🔵 **STEP 6 — Style Anchor Links (States)**

### Background:

Links have states:

* `a:link` → default
* `a:visited` → visited
* `a:hover` → hover
* `a:focus` → keyboard focus
* `a:active` → being clicked

Your CORAH nav already uses some:

```css
.nav-link:hover { ... }
.nav-link:focus-visible { ... }
```

**Task:**
Add a visited state:

```css
.nav-link:visited {
  color: var(--brand-600);
}
```

(Prevent purple default.)

---

## 🔵 **STEP 7 — Apply Borders and Backgrounds**

**Task:**
Modify `.nav-link--secondary` to improve clarity:

```css
.nav-link--secondary {
  border: 1px solid var(--brand-700);
  background-color: var(--brand-50);
  color: var(--brand-700);
}
```

**Explanation for Students:**
Secondary actions (login/logout) should contrast primary navigation.

---

## 🔵 **STEP 8 — Build a Card Component (Mini Exercise)**

**Task:**
Add inside `<main>`:

```html
<div class="card">
  <h2>Community Program</h2>
  <p>CORAH works with regional partners to deliver programming for seniors.</p>
</div>
```

Then in CSS:

```css
.card {
  background-color: var(--neutral-50);
  border: 1px solid var(--neutral-300);
  padding: 1rem;
  margin: 1rem 0;
  border-radius: var(--radius-sm);
}
```

This reinforces:

* Box model
* Typography
* Colors
* Reusable components

---

# **6. Deliverables**

Students submit:

### **A. Updated GitHub Pages Link**

Demonstrates:

* Styled headings, links, paragraphs
* Styled navigation buttons
* Styled card component

### **B. CSS updates in `styles.css`**

### **C. Reflection answers**

---

# **7. Reflection Questions**

1. Why do we use classes instead of IDs for most styling?
2. How does the box model influence layout decisions?
3. Why is it beneficial to use CSS variables instead of hard-coded colors?
4. How do text styles (font size, line height) change the readability of a page?
5. Which CSS selector type felt most intuitive to you, and why?

---

# **8. Assessment / Rubric**

| Criteria         | Excellent                                   | Good           | Satisfactory     | Needs Improvement |
| ---------------- | ------------------------------------------- | -------------- | ---------------- | ----------------- |
| **Selectors**    | Accurate, well-chosen classes & descendants | Mostly correct | Some misuse      | Incorrect         |
| **Typography**   | Uses tokens & readable scaling              | Minor issues   | Inconsistent     | Poor              |
| **Colors**       | Correct tokens + contrast                   | Mostly correct | Some hard-coded  | Poor              |
| **Box Model**    | Clear padding/border/margins                | Mostly correct | Uneven spacing   | Incorrect         |
| **Code Quality** | Clean, commented, organized                 | Minor issues   | Mixed formatting | Poor              |

---

# **9. Resources**

* MDN CSS Selector Reference
* W3C Color & Contrast Guidelines
* Chrome DevTools – Box Model
* GitHub Pages

---

# **10. Academic Policies**

(Normal NSCC policies)

---

# **11. Copyright**

Workshop content © NSCC — Educational Use Only
CORAH case study © Instructor/NSCC 2025

---

If you'd like, I can now generate:
👉 **WS7 – CSS Layouts With Flexbox**,
OR
👉 Begin producing printable PDFs or handouts.
