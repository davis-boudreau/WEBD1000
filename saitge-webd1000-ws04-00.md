
![alt text](image.png)

---

**Workshop Title:** HTML5 Fundamentals & Semantic Markup
**Course:** WEBD1000 – Website Development
**Instructor:** Davis Boudreau
**Format:** In-class guided workshop + hands-on implementation
**Estimated Time:** 0.5–1 hours
**Tools Required:**

* VS Code
* Live Server
* Browser DevTools
* W3C Markup Validator
* CORAH header files (provided)

---

# **2. Overview / Purpose / Objectives**

### **Purpose**

This workshop introduces students to **modern HTML5 fundamentals**, with a strong emphasis on **semantic markup**, **accessibility**, and **meaningful document structure**. Using the CORAH mock-up as the case study, students will learn how interface elements map from **Figma → HTML**, why semantics matter, and how to ensure pages are **valid, accessible, and future-proof**.

### **Why This Matters**

Semantic HTML is the foundation of all modern web development. It ensures:

* **Accessibility**: Assistive technologies understand the structure
* **SEO**: Search engines can correctly interpret content
* **Maintainability**: Code is easier to read, debug, reuse
* **UX Consistency**: Screen readers, mobile browsers, and crawlers behave predictably
* **Improved Responsiveness**: Semantic blocks are easier to style and reposition

Your CORAH header is an excellent real-world example because it includes:

* A **brand identity group** (logo + wordmark)
* A **primary navigation system**
* A **decorative section separator**
* A responsive layout intended to grow into a full site

### **Workshop Objectives**

By the end of this workshop, students will be able to:

1. Create a valid HTML5 document structure
2. Use semantic elements (`header`, `nav`, `main`, `footer`, etc.)
3. Implement accessible images with correct `alt` attributes
4. Use ARIA roles when needed
5. Build a professional site header using semantic HTML
6. Validate HTML with W3C Markup Validator

---

# **3. Learning Outcomes Addressed**

This workshop directly supports:

### **LO3 – Develop W3C-compliant websites using HTML & CSS.**

---

# **4. Assignment Description / Use Case**

### **The CORAH Case Study**

CORAH (Centre of Rural Aging & Health) is a fictional organization in a rural Nova Scotia context. You are designing their website using modern, accessible web development practices.

In WS4, students build the **semantic foundation** of the homepage, focusing solely on:

* Document structure
* Semantic grouping
* Accessible alt text
* Navigation structure
* Correct usage of HTML5 elements
* Clean formatting and indentation

This will prepare students for:

* WS5: Text, links, and images
* WS6: Intro to CSS
* WS7: Flexbox
* WS8: CSS Tokens
* WS9: Responsive layouts

---

# **5. Tasks / Instructions (Step-by-Step Workshop)**

Below is the complete activity using your template + expanded conceptual framing.

---

## **STEP 0 — Set Up the Project Folder**

**Background:**
Professional developers organize files consistently—this supports maintainability and scalability.

**Tasks:**

1. Create a new folder: `corah-site/`
2. Add:

   * `index.html`
   * `styles.css`
   * `images/` folder
3. Open the project in VS Code
4. Launch Live Server

---

## **STEP 1 — Create the HTML Document Structure**

**Background Knowledge:**
HTML documents follow a strict W3C structure. Every document begins with `<!DOCTYPE html>` which ensures standards-mode rendering—not quirks mode.

**Tasks:**
Write the following boilerplate:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CORAH – Header Demo</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

</body>
</html>
```

**Conceptual Framing:**

* `lang="en"` supports screen readers and indexing
* `meta viewport` enables mobile responsiveness
* Linking CSS externally follows best practices

---

## **STEP 2 — Apply Semantic Layout Elements**

**Background Knowledge:**
Semantic elements describe *meaning*, not *appearance*. They guide assistive technologies and create an understandable page hierarchy.

Key semantic block-level elements:

| Element     | Meaning                           | Use Case              |
| ----------- | --------------------------------- | --------------------- |
| `<header>`  | Top-of-page identity + navigation | CORAH logo + nav      |
| `<nav>`     | A list of major navigation links  | Main menu             |
| `<main>`    | Primary content of page           | Will add later        |
| `<footer>`  | Closing info                      | Will add later        |
| `<section>` | Thematic grouping                 | Future hero / content |
| `<article>` | Standalone content                | Blog posts            |
| `<aside>`   | Side information                  | Optional              |

**Tasks:**
Inside `<body>`, add:

```html
<header class="header-section-container" role="banner">
  <div class="header-container">

    <div class="logo-container">
      <a href="index.html" class="brand-link" aria-label="CORAH Home">
        <img src="images/corah-brand-logo.svg" alt="" class="corah-brand-logo">
      </a>

      <img src="images/corah-brand-wordmark-logo.svg"
           alt="CORAH – Centre of Rural Aging &amp; Health"
           class="corah-brand-wordmark-logo">
    </div>

    <nav class="nav-container" aria-label="Main navigation">
      <!-- nav links here -->
    </nav>

  </div>

  <div class="separator-container">
    <div class="separator" role="presentation"></div>
  </div>
</header>
```

**Contextual Insight:**

* `role="banner"` supports older assistive tech
* `aria-label="Main navigation"` improves clarity for screen readers
* Using semantic HTML reduces the need for `role` attributes, but here it enhances clarity

---

## **STEP 3 — Add Navigation Links**

**Background:**
Navigation is fundamental to UX, accessibility, and SEO.
Good nav = predictable organization → good user experience.

**Tasks:**
Add:

```html
<div class="nav-button">
  <a class="nav-link is-active" href="index.html" aria-current="page">home</a>
</div>
<div class="nav-button">
  <a class="nav-link" href="about.html">about</a>
</div>
<div class="nav-button">
  <a class="nav-link" href="events.html">events</a>
</div>
<div class="nav-button">
  <a class="nav-link" href="register.html">register</a>
</div>
<div class="nav-button">
  <a class="nav-link" href="profile.html">my profile</a>
</div>
<div class="nav-button">
  <a class="nav-link nav-link--secondary" href="login.html">login</a>
</div>
<div class="nav-button">
  <a class="nav-link nav-link--secondary" href="logout.html">logout</a>
</div>
```

**Conceptual Framing:**

* `aria-current="page"` is crucial for accessible navigation
* Grouping links in containers prepares for Flexbox (WS7)

---

## **STEP 4 — Add Image Alt Text Correctly**

**Deeper Conceptual Background:**
Images require accessible text alternatives.
Rules:

1. If the image conveys content → descriptive alt text
2. If the image is decorative → `alt=""`
3. If text is visible inside the image → alt should match the text

**In CORAH:**

* The *icon* is decorative (because the wordmark provides the brand text)
* The *wordmark* includes the brand name and tagline → must be readable

This reinforces WCAG 1.1.1 compliance.

---

## **STEP 5 — Validate Your Code (W3C)**

Students visit:
[https://validator.w3.org/](https://validator.w3.org/)

They must fix:

* Missing attributes
* Incorrect nesting
* Unclosed tags
* Typos in attribute names

---

## **STEP 6 — Push to GitHub Pages**

Students publish their semantic structure.

**What this reinforces:**

* Professional workflow
* Version management
* Publicly accessible demo pages

---

# **6. Deliverables**

Students must submit:

### **A. GitHub Pages Link**

The page should contain:

* Semantic `<header>` structure
* Semantic `<nav>` with real links
* Correct alt text for images
* Clean indentation and formatting
* No CSS styling yet (CSS begins in WS6)

### **B. HTML File Upload (Brightspace)**

`index.html` with comments explaining key sections.

### **C. W3C Validation Screenshot**

Proves W3C compliance.

---

# **7. Reflection Questions**

1. Why does semantic HTML improve accessibility for users with disabilities?
2. Which CORAH header elements required semantic tags, and why?
3. Why must some images use empty alt text (`alt=""`)?
4. What future CSS features (Flexbox, tokens, media queries) become easier because of a clean semantic foundation?
5. How does using ARIA attributes complement semantic HTML instead of replacing it?

---

# **8. Assessment / Rubric**

| Criteria                      | Excellent (A)                    | Good (B)                | Satisfactory (C)      | Needs Improvement (D/F) |
| ----------------------------- | -------------------------------- | ----------------------- | --------------------- | ----------------------- |
| **Semantic Structure**        | All sections properly structured | Minor misuse of tags    | Some semantic errors  | Mostly incorrect        |
| **Accessibility (alt, ARIA)** | All requirements met             | 1–2 fixes needed        | Some missing alt/ARIA | Largely missing         |
| **Code Quality**              | Clean, indented, readable        | Minor formatting issues | Mixed indentation     | Poor readability        |
| **W3C Validation**            | No errors                        | 1–2 warnings            | 3–5 warnings          | Multiple errors         |
| **Navigation Structure**      | Fully correct and functional     | Mostly correct          | Minor link issues     | Incorrect or missing    |

---

# **9. Submission Guidelines**

Students must upload:

* GitHub Pages link
* `index.html`
* Screenshot of W3C Validation

---

# **10. Resources / Equipment**

* VS Code + Live Server
* W3C Validator
* Browser DevTools
* Provided CORAH assets
* Figma mockup (optional)

---

# **11. Academic Policies**

(Use standard NSCC academic integrity + accessibility policies.)

---

# **12. Copyright Notice**

This workshop is for educational use in WEBD1000 © NSCC.
