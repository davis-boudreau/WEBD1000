![alt text](image.png)

---

**Course Code:** WEBD 1000 – Website Development Fundamentals
**Instructor:** Davis Boudreau
**Assignment Type:** Mini-Project 2A (Individual)
**Version:** 1.1 | **Last Updated:** Fall 2025
**Estimated Time:** 4–6 hours
**Pre-Requisites:** MP1 (Site Evaluation & Planning) and Weeks 4–5 Workshops (HTML5 Semantic Structure)

---

## **1. Overview / Purpose / Objectives**

**Purpose:**
In this mini-project, you will transform your plain HTML Corah homepage into a **styled, visually readable, and accessible webpage** using **CSS**. You’ll demonstrate how color, typography, and spacing bring structure and usability to life.

**Objectives:**

* Apply **Cascading Style Sheets (CSS)** to an existing semantic HTML page.
* Experiment with **typography, color, spacing**, and **box model** techniques to enhance readability.
* Validate HTML and CSS using **W3C Validators**.
* Reflect on accessibility and design choices for Corah’s target users (older adults in rural communities).

---

## **2. Learning Outcomes Addressed**

|  #  | Course Outcome                                         | Description                                                                    |
| :-: | :----------------------------------------------------- | :----------------------------------------------------------------------------- |
| LO2 | Plan and design websites based on project requirements | Apply accessibility and design principles to style and layout.                 |
| LO3 | Develop W3C-compliant websites using HTML and CSS      | Implement semantic markup and external CSS for structured, readable web pages. |

---

## **3. Assignment Description / Use Case**

### **Context — Corah Community Homepage**

Corah Community is a non-profit organization supporting older adults by promoting inclusion, well-being, and connection through local events.

Your task is to implement Corah’s homepage using **semantic HTML and CSS**. Building from your MP1 plan, your goal is to create a **visually balanced, accessible homepage** that reflects Corah’s tone: welcoming, trustworthy, and easy to read.

**Why this matters:**

* Seniors rely on **clarity and consistent navigation**.
* **Readable type, high contrast, and spacing** improve accessibility.
* A well-styled homepage establishes brand credibility and prepares you for responsive layouts in MP3.

---

## **4. Tasks / Instructions**

### **Step 1 – Set Up Your Project Folder**

1. Create a folder named `corah-site/`.
2. Inside, create:

   * `index.html` – your semantic HTML page from Week 4.
   * `css/style.css` – new stylesheet for this assignment.
   * `img/` – optional image directory for logos or hero images.
3. Link your stylesheet:

```html
<link rel="stylesheet" href="css/style.css">
```

---

### **Step 2 – Apply Semantic & Structural Principles**

Your HTML should maintain a clear structure using HTML5 tags:

| Section | Element               | Purpose                                   |
| :------ | :-------------------- | :---------------------------------------- |
| Header  | `<header>`, `<nav>`   | Logo, site title, and primary navigation  |
| Hero    | `<main>`, `<section>` | Welcoming introduction and call-to-action |
| Footer  | `<footer>`            | Contact info, policies, and copyright     |

> **Conceptual Reminder:**
> Semantic HTML conveys **meaning**, not just presentation. CSS builds on that meaning to ensure design consistency across devices and assistive technologies.

---

### **Step 3 – Implement the Header (Logo + Nav)**

**Goal:** Align Corah’s logo left and navigation buttons right using Flexbox.
**Design Rationale:** The header communicates brand identity and guides users immediately.

```html
<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">
      <img src="img/corah-logo.png" alt="Corah Community Logo" class="logo-img">
      <span class="logo-text">Corah Community</span>
    </a>
    <nav class="main-nav" aria-label="Primary">
      <ul class="nav-list">
        <li><a href="#">Home</a></li>
        <li><a href="#">Events</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
  </div>
</header>
```

**Flexbox Alignment CSS:**

```css
.header-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

---

### **Step 4 – Style the Hero Section (Typography & Visual Hierarchy)**

**Goal:** Create a welcoming hero section that introduces Corah’s mission.
Use accessible color contrast and readable text sizes.

```html
<section class="hero">
  <div class="container hero-inner">
    <div class="hero-copy">
      <h1>Connecting Seniors with Local Events</h1>
      <p>Find friendly activities, workshops, and volunteer opportunities near you.</p>
      <a href="#events" class="btn">View Events</a>
    </div>
  </div>
</section>
```

**CSS Concepts:**

* Use `clamp()` for responsive font sizes.
* Maintain a readable line length (~65 characters).
* Apply sufficient vertical padding for spacing.

---

### **Step 5 – Add and Style the Footer**

The footer provides closure and anchors the layout visually.

```html
<footer class="site-footer">
  <div class="container footer-inner">
    <p>&copy; 2025 Corah Community • <a href="#">Privacy Policy</a></p>
  </div>
</footer>
```

> **Accessibility Tip:** Footer links should use meaningful labels and maintain visible focus states.

---

### **Step 6 – Validate and Test**

1. Test your HTML with [W3C Validator](https://validator.w3.org/).
2. Validate your CSS with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
3. Check your color contrast with [Contrast Checker](https://contrast-ratio.com/).
4. Test focus states using the **Tab** key.

---

### **Step 7 – Reflect**

Write a short reflection (150–200 words) addressing:

* How your design choices (color, type, spacing) improve accessibility.
* What you learned about separating structure (HTML) from presentation (CSS).
* Any adjustments you made to improve readability.

---

## **5. Deliverables**

* `index.html` (semantic, styled homepage)
* `css/style.css` (linked and validated)
* Screenshot of homepage and validator results
* Reflection (150–200 words)

---

## **6. Evaluation / Rubric (10%)**

| Criteria                   | Description                                            | Weight   |
| :------------------------- | :----------------------------------------------------- | :------- |
| Semantic HTML Structure    | Correct hierarchy, readable code                       | 2 %      |
| CSS Application            | Effective use of selectors, color, typography, spacing | 3 %      |
| Accessibility & Validation | Meets W3C validation; appropriate color contrast       | 2 %      |
| Visual Cohesion            | Layout reflects Corah’s design and mission             | 2 %      |
| Reflection                 | Insightful and clear discussion of design decisions    | 1 %      |
| **Total**                  |                                                        | **10 %** |

---

## **7. Submission Guidelines**

* **Project Folder:** `corah-site/`
* **Hosting:** Publish your page using **GitHub Pages**.
* **Submission:**

  1. Push your `corah-site/` folder to a GitHub repository.
  2. Enable **GitHub Pages** (Settings → Pages → Deploy from `main` → `/root`).
  3. Test your live URL to ensure the page displays correctly.
  4. Submit your **GitHub Pages live link** in the **Comments area of the MP2A submission in Brightspace**.

> Example submission:
> 🔗 [https://studentusername.github.io/corah-site/](https://studentusername.github.io/corah-site/)

* **Students who attended the workshop:**

  * Post your reflection answers in the Brightspace comments area with your live GitHub link.
* **Students who did not attend:**

  * Complete the project independently and submit both your GitHub Pages link and written reflection.

---

## **8. Resources / Equipment**

* **Software:** VS Code, Chrome DevTools, GitHub account
* **References:**

  * MDN: [HTML5 Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
  * MDN: [CSS Basics](https://developer.mozilla.org/en-US/docs/Learn/CSS)
  * GitHub Pages: [Getting Started Guide](https://pages.github.com/)
* **Validation:** W3C Validators, Lighthouse Accessibility Checks

---

## **9. Academic Policies**

All work must follow NSCC’s Academic Integrity policy.
Late submissions may incur penalties unless prior arrangements are approved.

---

## **10. Copyright Notice**

© 2025 Nova Scotia Community College. All rights reserved.
For educational use only within WEBD 1000 – Website Development Fundamentals.
