
![alt text](image.png)

---

# **1. Workshop Details**

**Workshop Title:** Text, Links, and Images in HTML
**Course:** WEBD1000 – Website Development
**Duration:** 2 hours
**Instructor Materials:**

* `corah-brand-logo.svg`
* `corah-brand-wordmark-logo.svg`

(Available in **Brightspace → Workshops → WS5 Files** or **Teams → Class Materials**)

**Student Deliverables:**

* GitHub Pages link (submitted in **Brightspace Assignment Comments**)
* Reflection answers (submitted in **Brightspace Assignment Comments**)

---

# **2. Overview / Purpose / Objectives**

### **Purpose**

This workshop teaches students how to use **text**, **links**, and **images** in HTML while assembling the first functional version of the **CORAH header**, including:

* The CORAH brand icon (fingerprint)
* The CORAH wordmark (full brand text)
* Navigation links for a multi-page site

This workshop transitions from purely structural HTML (WS4) toward creating meaningful, connected content. Students will learn how internal links, image accessibility, and proper text hierarchy help form usable, professional web pages.

### **Why This Matters**

In real-world front-end development, developers must:

* Embed accessible images
* Provide meaningful navigation
* Create text structure that makes sense to screen readers
* Use correct alt text for branding assets
* Organize project files in predictable folders

The CORAH case study gives students a realistic scenario where branding assets, navigation, and page content must all work together.

### **Workshop Objectives**

Students will be able to:

1. Write correct HTML text using paragraph, heading, and small text tags
2. Build internal navigation with anchor links
3. Insert vector images (`<img>`) using proper alt text
4. Integrate the CORAH logo and wordmark into a semantic header
5. Create multiple pages linked as a small prototype site

---

# **3. Learning Outcomes Addressed**

### **LO3 – Develop W3C-compliant websites using HTML & CSS**

Students demonstrate their ability to structure text and media using valid HTML elements.

---

# **4. Assignment Description / Use Case**

Students will:

* Create a multi-page CORAH prototype (index + supporting pages)
* Insert the two official CORAH logo images
* Build a functional HTML navigation menu
* Apply meaningful text hierarchy
* Ensure correct alt text for visual branding
* Organize files into a clean project folder structure

This workshop builds the foundation for:

* **WS6 (Intro to CSS)**
* **WS7 (Flexbox)**
* **WS8 (CSS Tokens)**
* **WS9 (Responsive Design)**

---

# **5. Tasks / Instructions (Step-by-Step)**

---

# 🔵 **STEP 1 — Create Your Project Folder**

Create:

```
ws5-corah-site/
│
├── index.html
├── about.html
├── events.html
├── register.html
└── images/
      ├── corah-brand-logo.svg
      └── corah-brand-wordmark-logo.svg
```

Download both images from **Brightspace**.

---

# 🔵 **STEP 2 — Add Standard HTML Document Structure**

Use this in **every page**:

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

### Conceptual Notes

* Page titles should be unique
* Structure should be identical across pages
* This prepares students for template-based design later

---

# 🔵 **STEP 3 — Add Basic Text Content**

Add inside `<main>`:

```html
<h1>Welcome to CORAH</h1>
<p>Supporting older adults across rural Nova Scotia with community-centered programs.</p>

<p><small>Updated for WEBD1000 Workshop 5.</small></p>
```

### Why these tags matter

* `<p>` defines paragraphs, not `<br>`
* `<small>` indicates secondary text (legal/copyright/etc.)
* `<h1>` must be the main heading of the page

---

# 🔵 **STEP 4 — Build a Simple Navigation Menu**

Add inside `<header>`:

```html
<nav>
  <a href="index.html" aria-current="page">home</a>
  <a href="about.html">about</a>
  <a href="events.html">events</a>
  <a href="register.html">register</a>
</nav>
```

### Technical Notes

* `aria-current="page"` helps screen readers identify the active page
* Links should be lowercase and descriptive
* All links should work across all pages

---

# 🔵 **STEP 5 — Integrate the CORAH Logo + Wordmark**

Place both images in your `images/` folder.

Then add to your `<header>`:

```html
<div class="logo-group">
  <img src="images/corah-brand-logo.svg"
       alt=""
       class="corah-brand-logo">

  <img src="images/corah-brand-wordmark-logo.svg"
       alt="CORAH – Centre of Rural Aging and Health"
       class="corah-brand-wordmark-logo">
</div>
```

### Why one image has empty alt text

* The icon is **decorative**
* The wordmark contains the **actual text meaning**
* This prevents screen readers from reading “Corah Corah …” twice

### Why SVG is preferred

* Scales cleanly at all sizes
* Supports high-density screens (Retina)
* Lightweight and modern

---

# 🔵 **STEP 6 — Combine Logo + Navigation Into a Full Header**

Final semantic structure:

```html
<header>
  <div class="logo-group">
    <img src="images/corah-brand-logo.svg" alt="">
    <img src="images/corah-brand-wordmark-logo.svg"
         alt="CORAH – Centre of Rural Aging and Health">
  </div>

  <nav>
    <a href="index.html" aria-current="page">home</a>
    <a href="about.html">about</a>
    <a href="events.html">events</a>
    <a href="register.html">register</a>
  </nav>
</header>
```

This is a **professional, semantic, accessible header**.
The CSS and responsive layout will be added in WS6 and WS7.

---

# 🔵 **STEP 7 — Build Additional Pages**

Each supporting page should include:

```html
<header>…</header>

<main>
  <h1>About CORAH</h1>
  <p>This is the about page.</p>
</main>
```

Repeat similarly for `events.html` and `register.html`.

---

# 🔵 **STEP 8 — Publish to GitHub Pages**

Push your project to GitHub and enable GitHub Pages:

```
https://yourusername.github.io/ws5-corah-site/
```

---

# **6. Deliverables (Submission Rules)**

### ✔ **GitHub Pages link must be submitted through the Brightspace Assignment Comments.**

(Do NOT upload files unless the instructor requests them.)

### ✔ **Reflection answers must be typed directly into the Brightspace Assignment Comments.**

(No separate file submission.)

---

# **7. Reflection Questions**

(Submit answers in **Brightspace Assignment Comments**)

1. Why do we separate branding assets into **logo** and **wordmark** images instead of using one combined graphic?
2. When is it appropriate to use `alt=""` (empty alt text) for an image?
3. Why is it important to build internal navigation using **relative paths**?
4. What role does the `<nav>` tag play in accessibility and screen reader navigation?
5. How does using SVGs (instead of PNGs) benefit responsive design?

---

# **8. Assessment / Rubric**

| Criteria                  | Excellent                                           | Good                | Satisfactory            | Needs Improvement      |
| ------------------------- | --------------------------------------------------- | ------------------- | ----------------------- | ---------------------- |
| **Header Integration**    | Correct images, correct alt text, correct structure | Minor issues        | Visible but needs fixes | Incorrect or missing   |
| **Navigation**            | All links functional across pages                   | Mostly functional   | Some broken             | Not functional         |
| **HTML Structure**        | Fully semantic, valid                               | Mostly correct      | Minor issues            | Many issues            |
| **Project Organization**  | Clean folder structure                              | Minor issues        | Mixed                   | Disorganized           |
| **Submission Compliance** | GitHub Pages + reflection submitted correctly       | One element missing | Format issue            | Not submitted properly |

---

# **9. Resources**

* MDN: `<img>`
* MDN: `<nav>`
* MDN: Text-level semantics (`<p>`, `<small>`, `<strong>`)
* W3C HTML Validator

---

# **10. Academic Policies**

(Insert standard NSCC policies)

---

# **11. Copyright**

Workshop © NSCC – Educational Use Only
CORAH Brand © NSCC 2025 (for instructional use)

---
