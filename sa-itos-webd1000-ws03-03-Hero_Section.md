# WEBD 1000 — Workshop 03-03: Build a Hero Section

**Instructor:** Davis Boudreau  
**Course:** WEBD 1000 — Website Development  
**Workshop:** 03 — HTML and CSS Website Building  
**Activity:** 03 of 12  
**Estimated time:** 30 minutes (allow additional time if you are new to VS Code)  
**Assessment:** Formative practice; retain and push your work to your existing WEBD 1000 course repository  
**Prerequisite:** Completed Workshop 03-02 (semantic header and navigation)

## What you will build

A **hero section** is a prominent introduction near the top of a webpage. In this activity, you will add a clear heading, supporting paragraph, two **call-to-action (CTA)** links, and an image to the webpage you started in Activities 01 and 02. You will also learn how to style links to look like buttons without using JavaScript.

By the end, you should be able to:

- Explain what a hero section and a call to action are.
- Add semantic HTML using `<main>`, `<section>`, `<h1>`, `<p>`, `<a>`, and `<img>`.
- Explain the difference between an image's `src` and `alt` attributes.
- Use **class selectors** to style a hero section and CTA links.
- Explain basic CSS properties for spacing, borders, and sizing.
- Test links, images, and keyboard navigation in a browser.
- Commit and push the new activity to your **existing course repository**.

> **Repository rule:** Do **not** create a new repository for this workshop. Use the WEBD 1000 course repository you already have. A separate repository, if used, is for your independent semester website project.

---

## Part 1 — Prepare your activity folder (3 minutes)

1. Open **VS Code** and open your existing WEBD 1000 course repository folder.
2. In the Explorer, expand `Workshop3`.
3. Create a new folder called **`03-hero`** inside `Workshop3`.
4. Copy **both** `index.html` and `styles.css` from `Workshop3/02-header-nav/` into `Workshop3/03-hero/`.
5. Open the **copies** inside `03-hero` before editing. Keep Activity 02 unchanged.

Your repository should contain:

```text
YOUR-EXISTING-WEBD1000-REPOSITORY/
└── Workshop3/
    ├── 01-html-basics/
    │   ├── index.html
    │   └── styles.css
    ├── 02-header-nav/
    │   ├── index.html
    │   └── styles.css
    └── 03-hero/
        ├── index.html
        └── styles.css
```

**Checkpoint:** Confirm that the Explorer shows `03-hero/index.html` and `03-hero/styles.css`. Each activity has its own files, so you can safely experiment without overwriting previous work.

---

## Part 2 — Understand the hero section (5 minutes)

### 2.1 What is a hero section?

The hero is usually the first major content area after the site header. It tells visitors **what the website is about** and **what they can do next**. A typical hero contains:

1. A clear main heading (`<h1>`).
2. A short explanation (`<p>`).
3. One primary action and one secondary action (links styled as buttons).
4. An image that supports the message.

A *call to action* (CTA) invites the visitor to do something, such as **Explore Features** or **Learn More**.

### 2.2 HTML structure: sections and headings

- `<main>` identifies the webpage's main content. A page normally has one visible main landmark.
- `<section>` groups related content under a heading.
- `<h1>` identifies the main heading of this page. Use a meaningful heading rather than choosing headings for their visual size.
- `<p>` contains paragraph text.

**Important:** Activity 02 may already have a `<main>` element and a `<section id="home">`. **Edit the existing elements rather than adding a second `<main>` or another element with `id="home"`.** Every `id` value must be unique on a page.

### 2.3 Links versus buttons

Use `<a href="...">` when an action **navigates** to another location. Use `<button>` when an action performs an operation, such as submitting a form or opening an interface control. Our hero CTAs navigate to sections of the same page, so **links are correct** even when CSS makes them look like buttons.

Example:

```html
<a href="#features">Explore Features</a>
```

The `#features` part looks for an element whose `id` is `features`. If that element does not exist, the link will not take the visitor to the intended section.

### 2.4 Images: `src` and `alt`

```html
<img src="https://placehold.co/640x400/png?text=My+Website" alt="Illustration representing my website project">
```

- `src` tells the browser where to find the image.
- `alt` provides a text alternative that communicates the image's meaning when it cannot be seen or loaded.
- The example uses a **temporary online placeholder**. It needs an internet connection; later you can replace it with an image saved in your project.
- If an image is purely decorative and adds no information, `alt=""` can be appropriate. Here, use a meaningful description for your chosen image.

**Prediction:** What do you think will happen if the image URL is incorrect? How would the `alt` text help?

---

## Part 3 — Build the HTML (8 minutes)

### Step 1 — Locate your existing main content

Open `Workshop3/03-hero/index.html`. Keep the `<head>`, stylesheet link, site header, and navigation you built in Activity 02.

Your page should already contain something like:

```html
<main id="main-content">
    <section id="home">
        <h1>Welcome to My Website</h1>
        <p>...</p>
    </section>
    <section id="about">...</section>
    <section id="contact">...</section>
</main>
```

Your actual wording or section names may differ. That is fine. **Do not paste this example as a second `<main>`**.

### Step 2 — Replace the content inside your existing home section

Find the existing section with `id="home"`. Replace **that section only** with the following hero section. Leave your other sections (`about`, `contact`, or others) in place.

```html
<section class="hero" id="home" aria-labelledby="hero-heading">
    <div class="hero-content">
        <p class="hero-eyebrow">Welcome to my website</p>
        <h1 id="hero-heading">Discover My Website Project</h1>
        <p class="hero-description">
            Explore what this website is about and learn more
            about the ideas, services, or interests I want to share.
        </p>

        <div class="hero-actions">
            <a class="cta cta-primary" href="#about">Learn More</a>
            <a class="cta cta-secondary" href="#contact">Contact</a>
        </div>
    </div>

    <div class="hero-media">
        <img
            src="https://placehold.co/640x400/png?text=My+Website"
            alt="Placeholder illustration for my website project"
            width="640"
            height="400">
    </div>
</section>
```

**Important:** The two CTA targets must exist in your page. If your Activity 02 used different section IDs, change `href="#about"` and `href="#contact"` to match them. If Activity 02 already contains an `<h1>` outside the home section, consider whether that heading should become the hero heading; avoid duplicate competing main headings.

### Step 3 — Understand the new HTML

| Code | Meaning |
|---|---|
| `class="hero"` | Names the section so CSS can target it. Classes may be reused. |
| `id="home"` | Provides a unique destination for the Home navigation link. |
| `aria-labelledby="hero-heading"` | Gives the section an accessible name using the heading with that ID. |
| `<div>` | Groups elements for layout; it has no special semantic meaning. |
| `class="hero-actions"` | Groups the two CTA links so they can be styled together. |
| `href="#about"` | Navigates to the element with `id="about"`. |
| `width` / `height` | Describe the image's natural dimensions and help the browser reserve space. |

**Checkpoint:** Save `index.html` with **Ctrl+S**, then open `03-hero/index.html` with Live Server (or open it directly in your browser). You should see the heading, text, links, and image, although they will not yet have the final hero styling.

---

## Part 4 — Understand and apply the CSS (8 minutes)

Open **`Workshop3/03-hero/styles.css`**. **Keep the CSS from Activity 02.** Add the following rules at the **bottom** of the stylesheet so you can clearly identify the new hero styles.

### 4.1 Review: How a CSS rule works

```css
.hero {
    padding: 2rem;
}
```

- `.hero` is a **class selector**. The dot means “select elements with `class="hero"`.” Without the dot, `hero` would mean an HTML element named `<hero>`, which is not what we want.
- `padding` is a **property**: it controls space **inside** the element's border.
- `2rem` is the **value**. `rem` is relative to the root element's font size (often 16px by default, so 2rem is often 32px, unless that font size has changed).
- The braces `{ }` contain declarations; the colon separates a property from its value, and the semicolon ends a declaration.

**Compare:** `.hero` targets a class, `h1` targets every `<h1>` element, and `#home` targets the element with the unique ID `home`.

### 4.2 Add the hero styles

```css
/* Activity 03: Hero section */
.hero {
    background-color: #edf2f7;
    padding: 2rem;
    border-radius: 12px;
}

.hero-content {
    max-width: 42rem;
}

.hero-eyebrow {
    color: #004780;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

.hero-description {
    font-size: 1.1rem;
    line-height: 1.6;
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 1.5rem;
}

.cta {
    display: inline-block;
    padding: 0.75rem 1.25rem;
    border: 2px solid #004780;
    border-radius: 6px;
    text-decoration: none;
    font-weight: bold;
}

.cta-primary {
    background-color: #004780;
    color: #ffffff;
}

.cta-secondary {
    background-color: #ffffff;
    color: #004780;
}

.cta:hover {
    text-decoration: underline;
}

.cta:focus-visible {
    outline: 3px solid #f59e0b;
    outline-offset: 3px;
}

.hero-media {
    margin-top: 1.5rem;
}

.hero-media img {
    display: block;
    max-width: 100%;
    height: auto;
    border-radius: 8px;
}
```

### 4.3 Explain the CSS as you use it

| CSS | What it does | Why we use it |
|---|---|---|
| `.hero` | Selects the hero section by class | Styles only the hero, not every section |
| `padding: 2rem` | Adds inside spacing | Keeps text away from the section edges |
| `border-radius: 12px` | Rounds corners | Gives the section a softer appearance |
| `max-width: 42rem` | Limits maximum content width | Keeps long lines easier to read |
| `font-weight: bold` | Makes text bold | Emphasizes the eyebrow and CTA labels |
| `line-height: 1.6` | Adds vertical spacing between text lines | Improves paragraph readability |
| `display: flex` | Places the CTA links in a flexible row | Introduces Flexbox; we will study it in depth later |
| `flex-wrap: wrap` | Allows CTAs to move to another line | Prevents them from being squeezed on narrow screens |
| `gap: 0.75rem` | Adds space between flex items | Separates the two links |
| `.cta` | Styles both links with shared properties | Avoids writing the same styles twice |
| `.cta-primary` | Adds the primary link's blue background | Creates visual emphasis |
| `.cta-secondary` | Adds the secondary link's white background | Gives visitors an alternative action |
| `.cta:hover` | Applies when pointing at a link | Gives mouse users feedback |
| `.cta:focus-visible` | Applies to keyboard focus | Makes keyboard navigation easier to follow |
| `.hero-media img` | Selects images **inside** an element with class `hero-media` | Demonstrates a descendant selector |
| `max-width: 100%` | Prevents the image exceeding its container width | Helps the image fit smaller screens |
| `height: auto` | Preserves the image's proportions | Avoids stretching or squashing |

**New idea — multiple classes:** The first CTA has `class="cta cta-primary"`. That means it receives the shared `.cta` styles **and** the `.cta-primary` styles. A space separates two class names in HTML; it does not mean they are nested.

**New idea — CSS order:** When rules have equal specificity, later rules can override earlier ones for the same property. Because you are adding styles to an existing stylesheet, inspect the result and check for earlier `a`, `h1`, or other rules that may affect your new hero. Do not delete earlier working styles just to make the hero look different.

**Checkpoint:** Save `styles.css` and refresh the browser. Your hero should now have a light background, rounded edges, two visually distinct CTA links, and an image that fits within the available width. The hero content is stacked vertically for now. **A two-column hero layout will be introduced when we study CSS Grid.**

---

## Part 5 — Test and debug (3 minutes)

Complete these checks in the browser:

1. **Home navigation:** Click Home in the header. Does it move to the hero (`id="home"`)?
2. **Primary CTA:** Click **Learn More**. Does it move to the section with `id="about"`?
3. **Secondary CTA:** Click **Contact**. Does it move to `id="contact"`?
4. **Keyboard test:** Press **Tab** until a CTA receives focus. Can you see the focus outline? Press **Enter** to follow the link.
5. **Image test:** Does the image appear? If not, check the `src` URL and internet connection. The image's `alt` text should still communicate its purpose.
6. **Narrow browser:** Make the browser window narrower. Do the CTAs wrap rather than overlap? Does the image stay inside the page?

### Troubleshooting

| Problem | Check |
|---|---|
| CSS not appearing | Is the `<link rel="stylesheet" href="styles.css">` in `<head>`? Did you save the correct file? |
| CTA link goes nowhere | Does its `href="#name"` match an existing `id="name"` exactly? |
| Home link behaves oddly | Did you accidentally create two elements with `id="home"`? |
| Hero appears twice | Did you paste a new hero instead of replacing the existing home section? |
| Image is broken | Check the `src` address; the temporary image requires internet access. |
| Buttons are hard to read | Check whether an earlier link-colour rule is overriding `.cta-primary` or `.cta-secondary`. |

---

## Part 6 — Apply independently (2 minutes)

Personalize your hero without copying an additional complete example:

- [ ] Replace the hero heading with a meaningful title for **your** website topic.
- [ ] Rewrite the description to explain what visitors will find on your website.
- [ ] Change the first CTA's text to a specific action (for example, **Explore Our Services**), while keeping a valid destination.
- [ ] Experiment with `padding` or `border-radius` and explain what changed.
- [ ] If you change the image, update its `alt` text to describe the new image appropriately.

**Optional extension:** Download a suitable, permitted image and save it in `Workshop3/03-hero/images/`. Change `src` to a relative path such as `images/hero.jpg`. The filename must match your actual image. This is more reliable than depending on an external placeholder URL.

---

## Part 7 — Commit and push (1–2 minutes)

1. Save **both** files using **Ctrl+S**.
2. Open **Source Control** in VS Code.
3. Review the changed files. Confirm the new files are in `Workshop3/03-hero/` and the earlier activity folders are still present.
4. Stage the new files and commit with the message:

   ```text
   Workshop 03-03 - Build hero section
   ```

5. **Push** or **Sync Changes** to your existing WEBD 1000 course repository.
6. Open GitHub and verify that `Workshop3/03-hero/index.html` and `Workshop3/03-hero/styles.css` are visible.

**Submission:** Keep this activity in your existing course repository as technical evidence. No separate Brightspace submission is required unless your instructor directs otherwise.

---

## Completion checklist

- [ ] I used my **existing course repository**, not a new repository.
- [ ] I created `Workshop3/03-hero/`.
- [ ] The folder contains `index.html` and `styles.css`.
- [ ] I preserved Activity 02 and copied its files forward.
- [ ] I have one main content area and one unique `id="home"`.
- [ ] My hero contains a heading, paragraph, two CTA links, and an image.
- [ ] Both CTA links lead to existing sections.
- [ ] I can explain a class selector, a property, and a value.
- [ ] My image fits the page and has appropriate alternative text.
- [ ] I tested the page using a mouse and keyboard.
- [ ] I committed and pushed my work to GitHub.

## Reflection

Answer these questions briefly in your own notes or during the class review:

1. Why is a hero section useful to a website visitor?
2. Why did we use `<a>` rather than `<button>` for the two CTAs?
3. What is the difference between `.cta` and `.cta-primary`?
4. What is the purpose of the `alt` attribute on an image?
5. What happened when you changed the `padding` or `border-radius` value?

## Next activity — Workshop 03-04: CSS Foundations

In Activity 04, you will create `Workshop3/04-css-foundations/`, copy your completed Activity 03 files into it, and learn how to organize colours, fonts, and spacing using **CSS custom properties (design tokens)**. This will make your website easier to update and maintain.
