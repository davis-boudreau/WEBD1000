![alt text](image.png)

---

## 1. Assignment Details

**Course:** WEBD1000 Website Development Fundamentals

**Workshop Title:** Building a Responsive Homepage (Header–Hero–Footer)

**Type:** Class Activity / Guided Lab

**Related Outcome:** Outcome 4 – Implement CSS in websites to meet responsive page layout requirements

**Prerequisites:** Completed Workshop 06 (Homepage Structure with Semantic HTML + CSS Starter)

**Deliverable:** GitHub Pages Link to `corah-site` repository


---

## 2. Overview / Purpose / Objectives

This workshop introduces responsive layout concepts that ensure your webpage adapts gracefully across devices. Students will extend their Week 6 HTML structure (header → hero → footer) by applying **Flexbox**, **Grid**, and **media queries** to achieve a responsive, mobile-first layout.

**You will learn to:**

1. Implement Flexbox to align the header logo and navigation menu.
2. Apply Grid to organize the hero section content and image placement.
3. Use media queries to adjust layout for mobile, tablet, and desktop widths.
4. Integrate accessibility and typography principles for responsive readability.

---

## 3. Learning Outcomes Addressed

* **Outcome 1:** Evaluate a variety of web sites for usability and accessibility.
* **Outcome 3:** Develop W3C-compliant websites using HTML and CSS in a text editor or IDE.
* **Outcome 4:** Implement CSS to meet responsive page layout requirements.

---

## 4. Background Information

Corah’s homepage is composed of three key sections:

* **Header:** Brand logo (left) and navigation (right) – to collapse for mobile screens.
* **Hero:** Introductory headline, subtext, and optional call-to-action button beside an image.
* **Footer:** Contact information and links, scaled and stacked appropriately for small devices.

This workshop focuses on the transition from fixed layouts to fluid responsive design using the **mobile-first approach**. You’ll start with the simple mobile stack and enhance for larger viewports.

---

## 5. Step-by-Step Instructions / Tutorial Guide

### Step 1 – Project Setup

1. Open your existing `corah-site` repository in VS Code.
2. Ensure the folder contains `index.html`, `style.css`, and an `images/` directory.
3. Verify that your HTML structure from Week 6 is valid using the W3C Markup Validator.

---

### Step 2 – Build the Header Layout

Add Flexbox to the header to align the logo and navigation.

```html
<header class="header-container">
  <div class="logo-container">
    <img src="images/corah-brand-logo.svg" alt="Corah Logo" class="brand-logo">
    <img src="images/corah-wordmark.svg" alt="Corah Wordmark" class="brand-wordmark">
  </div>
  <nav class="nav-container">
    <ul class="nav-pill">
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Events</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
</header>
```

```css
header {
  display: flex;                 /* enable flexbox */
  justify-content: space-between;/* logo left, nav right */
  align-items: center;           /* vertical centering */
  padding: 1.5rem;
  flex-wrap: wrap;               /* allows wrapping on small screens */
}

.nav-container ul {
  display: flex;
  gap: 1rem;
  list-style: none;
}
```

---

### Step 3 – Create the Hero Section Using Grid

```html
<section class="hero">
  <div class="hero-text">
    <h1>Welcome to Corah</h1>
    <p>Supporting rural aging and health through innovation and community.</p>
    <button>Learn More</button>
  </div>
  <div class="hero-image">
    <img src="images/hero-image.jpg" alt="Community care at Corah">
  </div>
</section>
```

```css
.hero {
  display: grid;
  gap: 2rem;
  align-items: center;
  padding: 2rem;
}

/* Larger viewports: two columns */
@media (min-width: 768px) {
  .hero { grid-template-columns: 1fr 1fr; }
}
```

---

### Step 4 – Add Responsive Footer

```html
<footer>
  <div class="footer-container">
    <p>&copy; 2025 Corah Centre for Rural Aging & Health</p>
    <nav>
      <a href="#">Privacy Policy</a> | <a href="#">Accessibility</a>
    </nav>
  </div>
</footer>
```

```css
footer {
  background-color: #7b458f;
  color: #fff;
  padding: 1.5rem;
  text-align: center;
}

@media (min-width: 768px) {
  .footer-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
}
```

---

### Step 5 – Add Media Queries for Small Devices

```css
/* Small devices (phones) */
@media (max-width: 576px) {
  header { flex-direction: column; }
  .nav-container ul { flex-direction: column; }
  .hero { grid-template-columns: 1fr; }
}
```

---

### Step 6 – Validate and Test

1. Run your HTML through the W3C Markup Validator.
2. Test your site using Chrome DevTools → Device Toolbar to preview mobile, tablet, and desktop views.
3. Record a screenshot of your validator results and responsive layouts.

---

## 6. Reflection Questions

1. What layout issues did you encounter when testing your page on different devices?
2. How does Flexbox simplify alignment compared to traditional float layouts?
3. Which accessibility features (e.g., ARIA, alt text, contrast) did you verify?
4. Why is the mobile-first approach recommended in modern web design?

---

## 7. Submission Guide

* Students who **attend the workshop** should submit **answers to the reflection questions** in the Brightspace **Comments area** for Workshop 07.
* Students who **miss the session** must complete the entire tutorial independently, then upload the following:

  * Screenshot of their W3C validation results.
  * Screenshot of their responsive layout in desktop and mobile views.
  * Their **GitHub Pages link** to the `corah-site` repository homepage.

---

## 8. Resources / Tools

* VS Code (HTML & CSS editing)
* Chrome DevTools (Device Toolbar)
* [W3C Markup Validator](https://validator.w3.org)
* [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

---

## 9. Assessment / Rubric (10 points)

| Criteria                    | Description                                                          | Points     |
| --------------------------- | -------------------------------------------------------------------- | ---------- |
| Responsive layout           | Uses Flexbox + Grid correctly and adapts to mobile & desktop screens | 4          |
| Semantic HTML               | Proper structure (header, hero, footer) and alt text applied         | 2          |
| Validation                  | W3C compliant HTML and CSS (no critical errors)                      | 1          |
| Accessibility / Readability | Meets contrast and layout standards                                  | 1          |
| Reflection / Submission     | GitHub Pages link + complete reflections posted                      | 2          |
| **Total**                   |                                                                      | **10 pts** |

---
