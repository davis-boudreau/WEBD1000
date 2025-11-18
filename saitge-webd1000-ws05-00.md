
![alt text](image.png)

---

# **1. Workshop Details**

**Workshop Title:** Text, Links, and Images in HTML

**Course:** WEBD1000 – Website Development

**Duration:** 2 hours

**Instructor Materials:**
→ `corah-brand-logo.svg`
→ `corah-brand-wordmark-logo.svg`
(Available in **Brightspace Workshop 5 Files** or via **Teams > Class Materials**)

---

# **2. Overview / Purpose / Objectives**

### **Purpose**

This workshop builds foundational HTML skills — formatting text, working with anchor links, and embedding images — while guiding students to assemble the **CORAH header structure** using the official logo and wordmark assets provided by the instructor.

### **Why This Matters**

A large portion of professional front-end development involves:

* Structuring text clearly
* Creating accessible navigation
* Embedding vector graphics and images correctly
* Managing folder/file structures

Integrating the CORAH images now prepares students for:

* **WS6:** Intro to CSS
* **WS7:** Flexbox layout
* **WS8:** CSS Tokens
* **WS9:** Responsive design

This is also their **first opportunity** to assemble a real, professional-style header.

---

# **3. Learning Outcomes Addressed**

### **LO3 – Develop W3C-compliant websites using HTML & CSS**

Students demonstrate competency with:

* HTML headings, paragraphs, and semantic tags
* Anchor links
* Image embedding using `<img>` with proper alt text
* Building a structurally correct header

---

# **4. Assignment Description / Use Case**

Students will create:

* A **multi-page HTML prototype** with working text + links
* A **CORAH header** that includes:

  * CORAH logo (purple fingerprint icon)
  * CORAH wordmark (two-line brand name)
* A simple navigation bar
* Proper folder structure (`images/` folder, HTML pages linked together)

This work becomes the **base project** for future workshops.

---

# **5. Tasks / Instructions (Step-by-Step)**

---

# 🔵 **STEP 1 — Create Your Project Structure**

Inside your WEBD1000 folder, create:

```
corah-sample-site/
│
├── index.html
├── about.html
├── events.html
├── register.html
└── images/
      ├── corah-brand-logo.svg
      └── corah-brand-wordmark-logo.svg
```

➡️ **Download the two SVG files** from Brightspace → Workshops → **WS5 Files**
or via Teams → **Class Materials**.

Place both SVG files inside your `images/` folder.

---

# 🔵 **STEP 2 — Add Basic HTML5 Document Structure**

In each page (`index.html`, `about.html`, etc.) include:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CORAH – Sample Site</title>
</head>
<body>

</body>
</html>
```

Explain to students:

* `<!DOCTYPE html>` → tells browser to use HTML5
* `lang="en"` → required for accessibility
* `<meta viewport>` → required for mobile-friendly pages

---

# 🔵 **STEP 3 — Add Text Elements (Headings, Paragraphs, Small Text)**

Inside `<body>`:

```html
<h1>Welcome to CORAH</h1>
<p>Supporting older adults across rural Nova Scotia through community-led programs.</p>
<p><small>Updated for WEBD1000 workshop.</small></p>
```

Instructor Notes:

* Heading tags convey structure → not style
* `<small>` is used structurally for secondary text
* Students should NOT use `<br>` for spacing

---

# 🔵 **STEP 4 — Create Navigation Links**

Add a navigation section:

```html
<nav>
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a href="events.html">Events</a>
  <a href="register.html">Register</a>
</nav>
```

Conceptual teaching points:

* Internal links use **relative paths** (same folder → no slash needed)
* Links should be lowercase and descriptive
* `href="#"` is **not allowed** — must link to a real page in student projects

---

# 🔵 **STEP 5 — Integrate the CORAH Logo + Wordmark**

This step introduces students to working with **SVG logos**, which are the modern standard in real web projects.

Inside `<body>` (above nav), add a semantic header:

```html
<header>
  <div class="logo-group">
    <img src="images/corah-brand-logo.svg" 
         alt="" 
         class="corah-brand-logo">
  
    <img src="images/corah-brand-wordmark-logo.svg"
         alt="CORAH – Centre of Rural Aging and Health"
         class="corah-brand-wordmark-logo">
  </div>
</header>
```

### Why the first logo has `alt=""`

We insert **empty alt text** when:

* the image is **purely decorative**,
* AND the **wordmark provides the actual text content**.

This prevents screen readers from reading branding twice.

### Why the wordmark has descriptive alt text

This SVG contains real textual meaning — the brand name —
so it **must** be announced by assistive technologies.

---

# 🔵 **STEP 6 — Build the Full Header (Logo + Nav)**

Combine your work into a single structure:

```html
<header>
  <div class="logo-group">
    <img src="images/corah-brand-logo.svg" alt="">
    <img src="images/corah-brand-wordmark-logo.svg"
         alt="CORAH – Centre of Rural Aging and Health">
  </div>

  <nav class="main-nav">
    <a href="index.html" aria-current="page">home</a>
    <a href="about.html">about</a>
    <a href="events.html">events</a>
    <a href="register.html">register</a>
  </nav>
</header>
```

This gives students their **first working header**
(which will be styled in WS6 and turned into Flexbox in WS7).

---

# 🔵 **STEP 7 — Add Additional Pages and Link All Pages Together**

Students must create:

* `index.html`
* `about.html`
* `events.html`
* `register.html`

Each should include:

```html
<header>…</header>

<main>
  <h1>Page Title</h1>
  <p>This is the [page name] page.</p>
</main>
```

Test navigation by clicking each link.

---

# **6. Deliverables**

Students must submit:

### ✔ A GitHub Pages link

containing:

* Working multi-page site
* Fully integrated CORAH header (logo + wordmark)
* Internal links between all pages

### ✔ A zipped project folder (Brightspace)

containing:

* HTML files
* `images/` folder with the two SVG logos
* Correct relative links

---

# **7. Reflection Questions**

1. Why does the CORAH header use two images instead of one combined logo file?
2. When should an image have `alt=""` (empty alt text)?
3. Why are relative links preferred inside a project folder?
4. What issues might occur if images are not stored in a dedicated folder?
5. How does text hierarchy (h1–h6) improve accessibility?

---

# **8. Assessment / Rubric**

| Criteria               | Excellent                                     | Good                                      | Satisfactory             | Needs Improvement             |
| ---------------------- | --------------------------------------------- | ----------------------------------------- | ------------------------ | ----------------------------- |
| **Header Integration** | Both logos correctly placed, correct alt text | Logos included but alt text could improve | Minor issues but visible | Missing or incorrect          |
| **Navigation Links**   | All links work across pages                   | 1 link broken                             | Some pages missing       | Most links broken             |
| **HTML Structure**     | Fully semantic, validated                     | Mostly correct                            | Minor validation issues  | Disorganized                  |
| **Project Structure**  | Clear folders, images stored correctly        | Minor organization issues                 | Mixed files              | Disorganized or missing files |

---

# **9. Resources**

* W3C HTML Validator
* MDN: `<img>` element
* MDN: Accessible alt text
* MDN: `<nav>` landmark

---

# **10. Academic Policies**

(Insert standard NSCC policies)

---

# **11. Copyright**

Workshop © NSCC – Educational Use Only
CORAH branding supplied for instructional purposes
