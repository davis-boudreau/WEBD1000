![alt text](image.png)

---

# **1. Workshop Details**

**Workshop Title:** Intro to CSS – Selectors, Colors, Typography, Box Model

**Course:** WEBD1000 – Website Development

**Duration:** 2 hours

**Instructor Materials:** CORAH brand palette, header structure reference

**Student Deliverables:**

* **GitHub Pages link** (submitted in *Brightspace Assignment Comments*)
* **W3C CSS Validator results** (URL or screenshot)
* **Reflection answers** (submitted in *Brightspace Assignment Comments*)

---

# **2. Overview / Purpose / Objectives**

### **Purpose**

This workshop introduces students to **CSS**, focusing on real-world fundamentals:

* How to link an external stylesheet
* How to target HTML elements with selectors
* How to apply color, typography, spacing
* How the box model influences layout
* How CSS supports design consistency

Students will begin styling the CORAH project built in WS4–WS5, preparing for:

* **WS7:** Flexbox layout
* **WS8:** CSS Tokens (design systems)
* **WS9:** Responsive design

### **Why CSS Matters in Real Front-End Work**

Professional websites require:

* Clean separation of content (HTML) and presentation (CSS)
* Predictable patterns that scale
* Systems for typography and spacing
* Styling that supports accessibility and brand identity

The CORAH header is a perfect first styling target.

### **Workshop Objectives**

Students will:

1. Link external CSS files using `<link>`
2. Use element, class, and descendant selectors
3. Apply color and typography to text and links
4. Understand the CSS box model (padding, border, margin)
5. Begin styling the CORAH header
6. Validate their CSS using W3C tools

---

# **3. Learning Outcomes Addressed**

### **LO3 – Develop W3C-compliant websites using HTML & CSS**

WS6 introduces CSS fundamentals needed to create valid, standards-based layouts.

---

# **4. Assignment Description / Use Case**

Students will create the **first version of the CORAH CSS file**, applying:

* Typography rules
* Basic color styling
* Layout spacing
* Header and nav styling
* Box-model modifications

They will style:

* The header
* Navigation links
* Page text
* Footer text

This stylesheet will evolve through WS7–WS9 into a fully responsive system.

---

# **5. Tasks / Instructions (Step-by-Step)**

---

# 🔵 **STEP 1 — Create Your CSS File and Link It**

Create:

```
ws6-corah-site/
   index.html
   styles.css
   images/
```

Add inside `<head>`:

```html
<link rel="stylesheet" href="styles.css">
```

### Conceptual Background

* External CSS is the industry standard
* Inline styles and `<style>` tags do not scale
* Browsers read CSS rules top-down

---

# 🔵 **STEP 2 — Add Reset + Basic Typography Rules**

Open `styles.css` and add:

```css
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial, sans-serif;
  line-height: 1.5;
}
```

Explain:

* `box-sizing: border-box` simplifies layout math
* Setting base fonts ensures consistency
* Browsers include default margins; your design should control spacing

---

# 🔵 **STEP 3 — Style Headings and Paragraphs**

```css
h1, h2, h3 {
  font-weight: 700;
  margin-bottom: 0.5em;
}

p {
  margin-bottom: 1em;
}
```

Discuss:

* Headings visually communicate structure
* Margins create readable spacing
* Typography consistency is key in design systems

---

# 🔵 **STEP 4 — Add Link Styles**

Inside `styles.css`:

```css
a {
  text-decoration: none;
  color: #7B458F; /* CORAH brand purple */
  font-weight: bold;
}

a:hover {
  text-decoration: underline;
}
```

Teaching points:

* Links are critical for navigation
* Hover states improve usability
* Underline on hover increases accessibility

---

# 🔵 **STEP 5 — Style the CORAH Header (First Pass)**

Add:

```css
header {
  background-color: #F9FAFB;
  padding: 1rem;
  border-bottom: 2px solid #7B458F;
}

.logo-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}

nav a {
  margin-right: 1rem;
}
```

Conceptual teaching:

* The header forms the top “identity” region
* Spacing improves readability
* Simple Flexbox now helps alignment; deeper Flexbox work comes in WS7

---

# 🔵 **STEP 6 — Understand the Box Model**

Demonstrate using Chrome DevTools → “Box Model Breakdown.”

Let students experiment:

```css
p {
  padding: 10px;
  border: 2px solid #E5E7EB;
  margin: 20px 0;
}
```

Explain:

* **Padding** = space inside the box
* **Border** = visible frame
* **Margin** = space outside the box

This is crucial for future layout work.

---

# 🔵 **STEP 7 — Validate Your CSS**

Visit:
**[https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)**

Students must:

1. Paste their `styles.css`
2. Fix errors/warnings
3. Re-validate until clean
4. Reflect on issues found (new requirement)

---

# 🔵 **STEP 8 — Publish to GitHub Pages**

Push your project to GitHub and publish.

Submit your link:

```
https://yourusername.github.io/ws6-corah-site/
```

---

# **6. Deliverables (Submission Rules)**

### ✔ **Submit GitHub Pages link in Brightspace Assignment Comments**

(No file uploads unless requested.)

### ✔ **3. CSS Validator Screenshot**

**Uploaded as a file to Brightspace**
⭐️ *(Only the screenshot needs to be uploaded — not the project.)*

---

### ✔ **Submit Reflection answers in Brightspace Comments**

These 3 items must appear together in the **Assignment Comment box**.

---

# **7. Reflection Questions**

(Submit answers in Brightspace Assignment Comments)

1. After running the CSS validator, what errors or warnings did you encounter?
2. What did you change in your CSS to resolve validation issues?
3. Why is the CSS box model important for layout decisions?
4. How do selector choices affect maintainability in large projects?
5. What CSS rules would you consider “base styles” for any website?

---

# **8. Assessment / Rubric**

| Criteria                  | Excellent                                                 | Good           | Satisfactory      | Needs Improvement    |
| ------------------------- | --------------------------------------------------------- | -------------- | ----------------- | -------------------- |
| **CSS Structure**         | Clean, organized, separated logically                     | Mostly clean   | Minor issues      | Messy                |
| **Typography + Colors**   | Applied consistently                                      | Mostly correct | Some errors       | Incorrect or missing |
| **Header Styling**        | Functional and clearly structured                         | Mostly correct | Partial styling   | Missing              |
| **Validator Compliance**  | Fully validated, reflection included                      | Minor warnings | Issues identified | Not validated        |
| **Submission Compliance** | GitHub Pages + validator + reflection submitted correctly | One missing    | Format issues     | Missing              |

---

# **9. Resources**

* MDN: CSS Basics
* MDN: Box Model
* MDN: Selectors
* W3C CSS Validator

---

# **10. Academic Policies**

(Insert standard NSCC policies)

---

# **11. Copyright**

Workshop © NSCC – Educational Use Only
CORAH assets © NSCC 2025
