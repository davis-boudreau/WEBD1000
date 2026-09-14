![alt text](image.png)

---

# **1. Workshop Details**

**Workshop Title:** CSS Layouts With Flexbox

**Course:** WEBD1000 – Website Development

**Duration:** 2 hours

**Prerequisite Workshops:** WS4–WS6


**Student Deliverables:**

* **GitHub Pages link** (submitted in *Brightspace Assignment Comments*)
* **Reflection answers** (submitted in *Brightspace Assignment Comments*)
* **CSS Validator screenshot**
  → **Uploaded as a *file* to Brightspace**
  → *(Only the screenshot needs to be uploaded — not the project.)*

---

# **2. Overview / Purpose / Objectives**

### **Purpose (The “Why” Behind Flexbox)**

Flexbox is one of the most important layout tools in modern web development. Before Flexbox, developers relied on:

* HTML tables
* Floats
* Margin hacks
* Fixed-width layouts

These techniques were fragile and not responsive.

Flexbox was created to solve layout problems such as:

* Vertical centering
* Equal spacing between items
* Responsive wrapping
* Aligning items along two axes
* Distributing space in predictable ways
* Creating flexible containers that shrink/expand naturally

Flexbox allows the CORAH interface to:

* Display navigation horizontally on desktop
* Wrap into multiple rows on tablet/mobile
* Keep the logo and nav centered
* Build card layouts and hero layouts cleanly
* Maintain predictable spacing using `gap`

### **High-Level Goal**

By the end of this workshop, students will be able to:

* Align content professionally
* Create responsive layouts without media queries
* Understand the visual impact of Flexbox choices
* Build key layout components using Flexbox

### **Workshop Objectives**

Students will:

1. Prepare a Flexbox-ready project structure
2. Apply Flexbox to the CORAH header
3. Align logo + wordmark using Flexbox
4. Convert navigation into a responsive Flexbox layout
5. Build a hero section using Flexbox
6. Build a 3-card responsive content section
7. Validate CSS
8. Publish using GitHub Pages

---

# **3. Learning Outcomes Addressed**

### ✔ **LO4 – Implement CSS for responsive page layouts**

Flexbox is the foundational skill required for responsive design (preparing students for WS9).

---

# **4. Assignment Description / Use Case**

Students extend the CORAH HTML structure by applying Flexbox to:

* The site header
* The navigation bar
* A hero layout
* A feature card layout

This workshop moves the site from “unstyled layout” to “professional, structured, responsive design”.

---

# **5. Tasks / Instructions (Step-by-Step)**

---

# 🔵 **STEP 1 — Prepare Your Project Folder**

(Consistent across all workshops)

Create the required structure:

```
ws07/
 ├── index.html
 ├── styles.css
 └── images/
       ├── corah-brand-logo.svg
       ├── corah-brand-wordmark-logo.svg
       └── hero.jpg      (provided by instructor or substitute)
```

If you completed WS06:

* Duplicate your WS06 folder
* Rename it `ws07`

**Why folder structure matters:**
Professional web development requires **predictability**, **traceability**, and **consistency**. This structure mirrors industry practices and prepares students for multi-page sites as well as GitHub Pages publishing.

---

# 🔵 **STEP 2 — Deep Conceptual Overview of Flexbox**

Flexbox introduces two key concepts:

### **1. A parent “flex container”**

Anything with:

```css
display: flex;
```

becomes a flex container.

### **2. Children become “flex items”**

All direct children inherit Flexbox rules, gaining:

* Automatic alignment
* Automatic spacing
* Automatic responsiveness

---

### **The Two Axes of Flexbox**

Flexbox layouts operate on two axes:

```
MAIN AXIS  
↔ row (left → right)  OR  
↕ column (top → bottom)

CROSS AXIS  
Perpendicular to the main axis.
```

When students change `flex-direction`, they rotate the entire layout logic.

---

### **Key Flexbox Properties Used Today**

| Property          | Explanation                                 |
| ----------------- | ------------------------------------------- |
| `display: flex`   | Enables the Flexbox engine                  |
| `flex-direction`  | Row vs column layout                        |
| `justify-content` | Alignment along the *main axis*             |
| `align-items`     | Alignment along the *cross axis*            |
| `flex-wrap`       | Allows items to wrap onto new lines         |
| `gap`             | Spacing between children (Flexbox-friendly) |
| `flex`            | Controls how children grow/shrink           |

These properties create predictable layouts across screen sizes without one-off hacks.

---

# 🔵 **STEP 3 — Apply Flexbox to the CORAH Header**

Before Flexbox, the header might stack awkwardly or misalign.

Add to `styles.css`:

```css
header {
  background-color: #F9FAFB;
  padding: 1rem;
  border-bottom: 2px solid #7B458F;

  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
```

### **Technical Explanation**

* `display:flex` makes the header a Flexbox container
* `flex-wrap: wrap` allows the nav to drop below the logo on small screens
* `justify-content: space-between` spreads items across the full width
* `align-items: center` vertically aligns logo and navigation

This produces the classic professional “logo left, nav right” layout.

---

# 🔵 **STEP 4 — Align the CORAH Logo Group**

Add to `styles.css`:

```css
.logo-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}
```

### Why?

The CORAH logo is composed of:

* A fingerprint symbol
* The CORAH wordmark

Without Flexbox, they may misalign or stack incorrectly.

Flexbox ensures:

* Horizontal alignment
* Equal spacing
* Proper wrapping on small screens

---

# 🔵 **STEP 5 — Convert Navigation Into a Flex Layout**

```css
nav {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
```

### **Technical Background**

Flexbox replaces:

* Float-based nav bars
* Inline-block hacks
* Manual margin spacing
* JavaScript-based navigation layouts

The nav now:

* Aligns left → right on desktop
* Wraps naturally on mobile
* Keeps spacing consistent

---

# 🔵 **STEP 6 — Build a Flexbox Hero Layout**

Add to `index.html`:

```html
<main class="hero-section">
  <div class="hero-content">
    <h1>Welcome to CORAH</h1>
    <p>Supporting older adults across rural Nova Scotia.</p>
    <a class="hero-button" href="about.html">Learn More</a>
  </div>

  <div class="hero-image">
    <img src="images/hero.jpg" alt="Community activities at CORAH">
  </div>
</main>
```

Add to `styles.css`:

```css
.hero-section {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding: 2rem;
  gap: 2rem;
}

.hero-content {
  flex: 1 1 300px;
}

.hero-image img {
  width: clamp(250px, 40vw, 450px);
  height: auto;
}
```

### **Conceptual insights**

`flex: 1 1 300px` =
**Grow as needed**, **shrink as needed**, **minimum width 300px**.

This makes:

* Desktop = side-by-side hero
* Mobile = stacked hero
* Tablet = fluid transitions

---

# 🔵 **STEP 7 — Build a Three-Card Flex Layout**

Add to HTML:

```html
<section class="features">
  <div class="feature-card">
    <h3>Programs</h3>
    <p>Community-supported workshops and events.</p>
  </div>

  <div class="feature-card">
    <h3>Research</h3>
    <p>Studies supporting healthy aging in rural areas.</p>
  </div>

  <div class="feature-card">
    <h3>Get Involved</h3>
    <p>Volunteer, partner, or participate.</p>
  </div>
</section>
```

Add to CSS:

```css
.features {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.feature-card {
  flex: 1 1 250px;
  background-color: #FFFFFF;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #E5E7EB;
}
```

### Technical Background

This layout mimics modern UI patterns found in:

* Government sites
* Universities
* Corporate dashboards
* Nonprofit informational websites

Flexbox grids are more fluid than CSS Grid for small content cards.

---

# 🔵 **STEP 8 — Validate Your CSS (Required)**

Visit:

➡ **[https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)**

Steps:

1. Paste your CSS
2. Validate
3. Fix warnings/errors
4. Revalidate
5. Take a screenshot of “**Valid CSS!**”

### 📌 Requirement:

**Upload the screenshot as a file to Brightspace.**
⭐ *Only the screenshot needs to be uploaded — not the project.*

---

# 🔵 **STEP 9 — Publish to GitHub Pages**

Push your project commit → enable GitHub Pages.

Submit a link:

```
https://yourusername.github.io/ws07-corah-site/
```

Paste the link into **Brightspace Assignment Comments**.

---

# **6. Deliverables (Submission Rules)**

Students must submit:

---

### ✔ **1. GitHub Pages Link**

Submitted in **Brightspace Assignment Comments**

---

### ✔ **2. Reflection Answers**

Submitted in **Brightspace Assignment Comments**

---

### ✔ **3. CSS Validator Screenshot**

📁 **Uploaded as a file to Brightspace**
*(Only the screenshot needs to be uploaded — not the project.)*

---

# **7. Reflection Questions**

(Submit answers in Brightspace Assignment Comments)

1. What Flexbox property had the greatest impact on your layout? Why?
2. Why is `flex-wrap` essential for responsive design?
3. How did Flexbox simplify problems you encountered in earlier workshops?
4. What UI patterns did you notice in the CORAH case study that map well to Flexbox?
5. What did the CSS Validator teach you about writing clean code?

---

# **8. Assessment / Rubric**

| Criteria                   | Excellent                             | Good                     | Satisfactory       | Needs Improvement   |
| -------------------------- | ------------------------------------- | ------------------------ | ------------------ | ------------------- |
| **Flexbox Implementation** | Fully responsive, clean, professional | Mostly correct           | Some errors        | Very limited        |
| **Header + Nav Alignment** | Perfectly aligned and wrapped         | Minor issues             | Usable but uneven  | Poor structure      |
| **Hero + Cards**           | Flexible, responsive, polished        | Mostly correct           | Some layout issues | Minimal effort      |
| **Validator Screenshot**   | Uploaded & valid                      | Uploaded w/ minor issues | Uploaded w/ errors | Missing             |
| **Submission Rules**       | All requirements met                  | One missing              | Format issues      | Major items missing |

---

# **9. Resources**

* MDN Flexbox Guide
* CSS-Tricks: Complete Guide to Flexbox
* Chrome DevTools → Flexbox Overlay
* W3C CSS Validator

---

# **10. Academic Policies**

Include standard NSCC boilerplate text.

---

# **11. Copyright**

Workshop © NSCC – Educational Use
CORAH assets © NSCC 2025

