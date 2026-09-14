
![alt text](image.png)

---

# **1. Workshop Details**

**Workshop Title:** HTML5 Fundamentals & Semantic Markup
**Course:** WEBD1000 – Website Development
**Duration:** 2 hours
**Prerequisites:** None (first core HTML workshop)
**Instructor Materials:** CORAH design overview, header layout diagram
**Student Deliverables:**

* GitHub Pages link (submitted via Brightspace *Assignment Comments*)
* Reflection answers (submitted via Brightspace *Assignment Comments*)

---

# **2. Overview / Purpose / Objectives**

### **Purpose**

This workshop introduces students to **HTML5 semantic structure**, the foundation of modern web development. Students will learn how to create meaningful, accessible, standards-compliant markup using the **CORAH case study**, which provides realistic, professional design context.

By the end of this workshop, students will understand how to structure a webpage using HTML5 semantic elements and how that structure supports accessibility, responsive design, CSS styling, search engine indexing, and real-world development workflows.

### **Why Semantic HTML Matters**

Semantic markup provides:

* **Meaning** to browsers and assistive technologies
* **Structure** to search engines
* **Consistency** for teams working on shared codebases
* **Maintainability** for long-term projects
* **Clean CSS architecture** (semantic containers become styling hooks later)

In professional environments, HTML is not just “tags.”
It is **information architecture.**

### **Why We Use the CORAH Case Study**

Students learn better when:

* The content feels real
* Designs map to authentic UI patterns
* Assets match the final goal
* Each workshop builds toward a unified prototype

The CORAH case study represents:

* Real organizational branding
* Real page structures (header, nav, hero, content)
* Real deliverables similar to industry/coop work

It will be reused throughout **WS4–WS9**, giving students an evolving portfolio artifact.

### **Workshop Objectives**

Students will:

1. Understand the purpose of core HTML5 semantic elements
2. Build a semantic page structure for CORAH
3. Use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, and `<footer>` correctly
4. Apply text hierarchy with `<h1>`–`<h6>`
5. Structure content for readability and accessibility
6. Validate code using W3C tools

---

# **3. Learning Outcomes Addressed**

### **LO3 – Develop W3C-compliant websites using HTML & CSS**

WS4 introduces the semantic foundation required to build compliant web pages.

---

# **4. Assignment Description / Use Case**

You will build the **first version** of the CORAH homepage using proper semantic HTML.
This includes:

* A document head
* A header container
* A main area
* Placeholder content sections
* A footer

The end result is a **clean, semantic, unstyled HTML structure** that will be styled in future workshops (WS6, WS7, WS8, WS9).

This is the “skeleton” of your project.

---

# **5. Tasks / Instructions (Step-by-Step)**

---

# 🔵 **STEP 1 — Create Your Project Folder**

Create a folder:

```
webd1000-ws4/
   index.html
```

(Optional for later workshops):
Create additional pages:

```
about.html
events.html
contact.html
```

---

# 🔵 **STEP 2 — Add the Required HTML5 Document Structure**

In `index.html`, insert:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CORAH – Home</title>
</head>
<body>

</body>
</html>
```

### Conceptual Background

* `<!DOCTYPE html>` → instructs browsers to use HTML5
* `lang="en"` → used by assistive technologies
* `<meta viewport>` → ensures mobile-friendly scaling
* `<title>` → displayed in search engines and browser tabs

This is the **minimum valid HTML document**.

---

# 🔵 **STEP 3 — Build the Semantic Structure**

Inside `<body>`, add semantic regions:

```html
<header>
  <!-- Logo and nav will go here -->
</header>

<main>
  <section>
    <h1>Welcome to CORAH</h1>
    <p>Supporting older adults in rural Nova Scotia.</p>
  </section>

  <section>
    <h2>Our Programs</h2>
    <p>Learn how CORAH supports community well-being.</p>
  </section>
</main>

<footer>
  <p>&copy; 2025 CORAH – Centre for Rural Aging & Health</p>
</footer>
```

### Why Semantic Regions Matter

* `<header>` → announces the start of page-level navigation/branding
* `<main>` → tells assistive tech where the content starts
* `<section>` → thematic grouping
* `<footer>` → page metadata
* `<h1>` must appear **once** as the primary page title

This is critical for **accessible navigation** (screen readers jump between semantic regions).

---

# 🔵 **STEP 4 — Add Headings and Text Hierarchy**

Add different text levels:

```html
<h1>Main Page Title</h1>
<h2>Sub-section Heading</h2>
<h3>Smaller Topic Heading</h3>
<p>Paragraph text goes here.</p>
<small>Secondary information appears here.</small>
```

### Why Text Hierarchy Matters

* `<h1>`–`<h6>` define the structure of the content
* Screen readers use heading navigation
* Proper hierarchy improves SEO
* Avoid “visual headings” made with `<div>` + CSS
* Never skip heading levels

---

# 🔵 **STEP 5 — Insert Placeholder Navigation Links**

Inside `<header>`:

```html
<nav>
  <a href="index.html" aria-current="page">Home</a>
  <a href="about.html">About</a>
  <a href="events.html">Events</a>
  <a href="contact.html">Contact</a>
</nav>
```

### Technical Notes:

* `<nav>` is a landmark region
* `aria-current="page"` adds accessibility context
* Links must be semantic—not styled yet

---

# 🔵 **STEP 6 — Validate Your HTML**

Students must:

1. Open **W3C HTML Validator**
2. Upload or paste their code
3. Fix all errors
4. Resubmit until validation passes

This ensures W3C-compliant HTML (LO3).

---

# 🔵 **STEP 7 — Publish to GitHub Pages**

1. Create a **public GitHub repository**
2. Add your files
3. Enable GitHub Pages → "Deploy from main"
4. Copy the public URL:

```
https://yourusername.github.io/webd1000-ws4/
```

---

# **6. Deliverables (Submission Rules)**

### ✔ **Students must submit the GitHub Pages link in the Brightspace Assignment Comments.**

(No file upload required unless otherwise specified.)

### ✔ **Reflection question answers must be submitted in the Brightspace Assignment Comments.**

(Do NOT upload a separate document.)

This standard applies to **all future workshops.**

---

# **7. Reflection Questions**

(Submit answers in Brightspace *Assignment Comments*)

1. Why is semantic HTML essential for assistive technology users?
2. What is the purpose of `<main>`, and why can it appear only once?
3. How does heading hierarchy improve both accessibility and SEO?
4. Why is it important not to skip heading levels (e.g., h1 → h3)?
5. What role does the `<nav>` landmark serve on a webpage?

---

# **8. Assessment / Rubric**

| Criteria                  | Excellent                                          | Good                           | Satisfactory     | Needs Improvement                 |
| ------------------------- | -------------------------------------------------- | ------------------------------ | ---------------- | --------------------------------- |
| **Semantic Structure**    | All semantic elements used correctly               | Mostly correct                 | Some missing     | Incorrect or absent               |
| **Heading Hierarchy**     | Perfect hierarchy, meaningful text                 | Mostly correct                 | Needs refinement | Incorrect usage                   |
| **Navigation**            | Working semantic `<nav>` with meaningful links     | Mostly correct                 | Minor errors     | Broken or missing                 |
| **Code Validity**         | Fully W3C validated                                | Minor warnings                 | Some errors      | Many errors                       |
| **Submission Compliance** | GitHub Pages + reflection both submitted correctly | One element slightly incorrect | Format issues    | Missing or not submitted properly |

---

# **9. Resources**

* MDN: HTML Elements Reference
* W3C Semantic Structure Guidelines
* W3C HTML Validator
* A11Y Project – Semantic Landmarks Guide

---

# **10. Academic Policies**

(Insert NSCC standard policies)

---

# **11. Copyright**

WS4 © NSCC – Educational Use
CORAH case study materials © Instructor/NSCC 2025
