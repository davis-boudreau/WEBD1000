![alt text](image.png)

---


**Course:** WEBD1000 – Website Development Fundamentals

**Activity Title:** HTML5 Fundamentals & Semantic Markup

**Duration:** 2–2.5 hours

**Instructor:** Davis Boudreau

---

### 1. **Learning Objectives**

By the end of this session, students will be able to:

1. Identify and use key **HTML5 semantic elements** (header, nav, main, section, article, aside, footer).
2. Apply semantic markup to a **Corah Case Study** web page.
3. Understand how semantics improves **accessibility, SEO, and maintainability**.
4. Produce a **structured HTML page** using semantic elements and proper nesting.

---

### 2. **Background / Context**

The **Corah Case Study** involves building a website for a small **community organization**, connecting senior citizens with local events.

* Primary Users: Senior citizens (60+) in rural communities, often with varying digital literacy and accessibility needs.
* Secondary Users: CORAH staff managing events, communications, and outreach.

**Why semantics matter:**

* Improves **screen reader experience** for visually impaired users.
* Provides **meaningful page structure** for SEO and maintainability.
* Ensures consistent **layout and styling** when CSS is applied.

**Key Semantic Elements:**

* `<header>` – Introductory content, logo, site name, navigation.
* `<nav>` – Main navigation links.
* `<main>` – Primary page content (only one per page).
* `<section>` – Thematic grouping of content.
* `<article>` – Self-contained content, e.g., event details, blog post.
* `<aside>` – Related info or sidebar.
* `<footer>` – Contact info, legal, copyright.

---

### 3. **Materials / Tools**

* Code editor: **VS Code** recommended
* Browser: Chrome/Firefox
* DevTools: Elements inspector, console
* Corah Case Study mockup / wireframe from previous workshop
* HTML5 reference: MDN Web Docs ([https://developer.mozilla.org/en-US/docs/Web/HTML/Element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element))

---

### 4. **Step-by-Step Instructions (Guided Tutorial)**

#### **Step 1: Review the Corah Page Layout (10 min)**

* Open your **sitemap** and wireframes for the Corah homepage.
* Identify **header, hero, main content sections, and footer**.
* Discuss with a partner: “Which areas could be `<section>` vs `<article>` vs `<aside>`?”

> **Tip:** Students who did not attend the workshop should review the sitemap and wireframe independently, making notes about where semantic sections will go.

---

#### **Step 2: Set Up Your HTML Document (15 min)**

1. Create a folder: `corah-site-week4`.
2. Create `index.html` with the basic HTML5 boilerplate:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Corah Community Events</title>
</head>
<body>
  
</body>
</html>
```

3. Save and open in your browser.

> **Non-attending students:** Complete this setup independently and ensure the page opens without errors.

---

#### **Step 3: Add the Page Header (20 min)**

* Use `<header>` for logo/site name and `<nav>` for main links:

```html
<header>
  <h1>Corah Community Events</h1>
  <nav>
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">Events</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
</header>
```

* **Check hierarchy** in browser DevTools.

> **Non-attending students:** Replicate the same structure and ensure correct nesting.

---

#### **Step 4: Build the Main Content (30 min)**

* Add `<main>` and content sections based on the Corah homepage:

```html
<main>
  <section id="hero">
    <h2>Welcome to Corah Community</h2>
    <p>Connecting seniors with local events and activities.</p>
  </section>

  <section id="featured-events">
    <h2>Featured Events</h2>
    <article>
      <h3>Community Gardening</h3>
      <p>Date: October 12, 2025</p>
      <p>Join us for a gardening workshop!</p>
    </article>
    <article>
      <h3>Cooking Class</h3>
      <p>Date: October 15, 2025</p>
      <p>Learn to cook healthy meals for seniors.</p>
    </article>
  </section>

  <aside>
    <h2>Quick Links</h2>
    <ul>
      <li><a href="#">Volunteer Info</a></li>
      <li><a href="#">Sign Up for Newsletter</a></li>
    </ul>
  </aside>
</main>
```

> **Non-attending students:** Follow this structure and reference your sitemap to ensure proper section placement.

---

#### **Step 5: Add the Footer (15 min)**

```html
<footer>
  <p>&copy; 2025 Corah Community. All rights reserved.</p>
  <p>Contact us: info@corahcommunity.org</p>
</footer>
```

---

#### **Step 6: Validate Your HTML (10 min)**

1. Use **W3C Validator**: [https://validator.w3.org/](https://validator.w3.org/)
2. Correct errors and note validation results.

> **Non-attending students:** Complete validation independently and note changes.

---

### 5. **Reflection Questions**

* How does semantic HTML improve accessibility for Corah’s senior users?
* Which semantic elements were easiest or hardest to implement? Why?
* How does this structure support CSS styling in future weeks?

---

### 6. **Deliverables**

* `index.html` with semantic structure (header, hero, sections, articles, aside, footer)
* Screenshot of DevTools showing semantic hierarchy
* W3C Validator results or notes

---

### 7. **Submission Guide**

* **Students who attended the workshop:**

  * Submit **answers to the reflection questions** in the **comments area of the Class Activity**.
  * No need to submit screenshots or files unless requested.

* **Students who did not attend the workshop:**

  * Complete all activity steps independently.
  * Submit **index.html**, DevTools screenshot, validation results, **and answers to the reflection questions** in the **comments area of the Class Activity**.
  * This demonstrates that the activity was completed independently.

---

