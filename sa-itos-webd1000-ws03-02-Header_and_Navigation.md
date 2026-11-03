# WEBD 1000 — Workshop 03-02: Semantic Header and Navigation

**Instructor:** Davis Boudreau
**Duration:** Approximately 30 minutes (allow additional time for first-time learners)
**Level:** Beginner — builds on Workshop 03-01
**Learning outcome:** Develop standards-compliant webpages using semantic HTML and CSS
**Assessment:** Formative workshop practice; retain GitHub evidence in the existing course repository

## What you will build

In Workshop 03-01, you created an HTML page and learned how CSS selectors control its appearance. In this activity, you will add a **website header**, **navigation links**, and **meaningful page sections**. You will also learn the difference between an HTML element, an attribute, an `id`, and a CSS class.

**Repository rule:** Continue using your **existing WEBD 1000 course GitHub repository**. Do **not** create a new repository. The separate repository is for the independent semester website project.

**Activity folder:** `Workshop3/02-header-nav/`
**Required files:** `index.html` and `styles.css`

## 1. Understand: What is semantic HTML? (5 minutes)

A webpage is easier to understand when its HTML tags describe **what each part means**, not just what it looks like. This is called **semantic HTML**.

For example:

- `<header>` identifies introductory content, such as a site name and main navigation.
- `<nav>` identifies a group of important navigation links.
- `<main>` identifies the main content of the webpage. A page normally has one visible `<main>` element.
- `<section>` groups content about a related topic. A section usually has a heading.
- `<h1>` identifies the page's main heading; `<h2>` identifies a subsection heading.
- `<a>` creates a hyperlink.
- `<ul>` creates an unordered list, and `<li>` creates an item in that list.

**Why use semantic tags?** They make source code easier to maintain and help browsers, assistive technologies, and other tools understand the structure of the page. Semantic HTML does **not** automatically make a site fully accessible, but it provides an important foundation.

### Understand links before you write them

```html
<a href="#about">About</a>
```

Read this as: “Create a link labelled **About** that takes the visitor to the element whose `id` is `about`.”

- `<a>` is the **anchor element**.
- `href` is an **attribute** that specifies the link destination.
- `#about` is a **fragment identifier** that refers to `id="about"` on this page.
- `About` is the clickable link text.

A link to `#about` only works as intended when a matching `id="about"` exists. The `#` is part of the link's `href`, **not** part of the HTML `id` value.

**Predict:** If the link says `href="#features"` but no element has `id="features"`, what do you think will happen when you click it?

## 2. Prepare: Create the next activity folder (3 minutes)

1. Open your **existing WEBD 1000 course repository** in VS Code.
2. In the Explorer panel, expand `Workshop3`.
3. Create a new folder named **`02-header-nav`** inside `Workshop3`.
4. Copy `index.html` and `styles.css` from `Workshop3/01-html-basics/`.
5. Paste both files into `Workshop3/02-header-nav/`.
6. Open the **new copies** before editing. Leave `01-html-basics` unchanged.

Your folders should now look like this:

```text
YOUR-EXISTING-WEBD1000-COURSE-REPO/
└── Workshop3/
    ├── 01-html-basics/
    │   ├── index.html
    │   └── styles.css
    └── 02-header-nav/
        ├── index.html
        └── styles.css
```

**Checkpoint:** Look at the VS Code tab or Explorer selection and confirm you are editing files in **`02-header-nav`**, not `01-html-basics`.

## 3. Build: Add semantic HTML (9 minutes)

### Step A — Understand the page layout

We will organize the visible page into two major parts:

```text
BODY
├── HEADER
│   ├── Site name
│   └── NAV
│       ├── Home link
│       └── About link
└── MAIN
    ├── SECTION id="home"
    │   └── Main heading and introduction
    └── SECTION id="about"
        └── Heading and short description
```

The navigation links will point to sections that **actually exist**. We are starting with two links so you can understand and test them before adding more sections in later activities.

### Step B — Update `index.html`

Open `Workshop3/02-header-nav/index.html`. Replace its contents with the following complete HTML. Notice that the `<head>` and CSS link from Activity 01 are still present.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website | Home</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="site-header">
        <p class="site-name">My Website</p>

        <nav aria-label="Main navigation">
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="home">
            <h1>Welcome to My Website</h1>
            <p>I am learning to build webpages with HTML and CSS.</p>
            <p>This page now has a header and working navigation links.</p>
        </section>

        <section id="about">
            <h2>About This Website</h2>
            <p>This website will grow as I complete the workshop activities.</p>
        </section>
    </main>
</body>
</html>
```

Save with **Ctrl+S**.

### Step C — Explain the new HTML as you build

**`<header class="site-header">`**: The `header` element gives this region meaning. `class="site-header"` adds a reusable name that CSS can select. The class name does not change the appearance until you write a CSS rule for it.

**`<p class="site-name">`**: The site name is ordinary text, not the page's main heading. We reserve `<h1>` for the main heading inside `<main>`.

**`<nav aria-label="Main navigation">`**: `nav` identifies the navigation region. `aria-label` gives that navigation an accessible name, useful if a page later contains multiple navigation regions. You do not need to memorize ARIA attributes yet; first understand why the navigation has a meaningful name.

**`<ul>` and `<li>`**: Navigation is a collection of related links, so a list is a useful structure. Each `<li>` contains one link.

**`href="#home"` and `id="home"`**: These must match exactly. The About link follows the same pattern with `about`.

**`<main>` and `<section>`**: The main element wraps the primary page content. Each section groups related content and has a heading.

**Important:** Do not use a `<div>` for everything. A `<div>` is a generic container; use semantic elements when their meaning matches the content.

## 4. Understand and build: CSS selectors for your header (7 minutes)

In Activity 01, you used **element selectors**:

```css
body { color: #14253a; }
h1 { color: #004780; }
```

Now you will encounter three common ways to select HTML:

| Selector         | Type             | Matches                                    |
| ---------------- | ---------------- | ------------------------------------------ |
| `header`       | Element selector | Every `<header>` element                 |
| `.site-header` | Class selector   | Every element with `class="site-header"` |
| `#about`       | ID selector      | The element with `id="about"`            |

The dot (`.`) belongs in a **CSS class selector**. The hash (`#`) belongs in a **CSS ID selector**. Neither symbol is included when writing the class or ID value in HTML.

You will also see a **descendant selector**:

```css
nav a {
    color: #004780;
}
```

`nav a` means: “Select `<a>` elements that are **inside** a `<nav>` element.” The space between `nav` and `a` matters. It does **not** mean “select all navigation elements and all links.”

### Step A — Update `styles.css`

Open the **new** `Workshop3/02-header-nav/styles.css`. Replace its contents with:

```css
body {
    background-color: #edf2f7;
    color: #14253a;
    font-family: Arial, sans-serif;
    margin: 0;
}

.site-header {
    background-color: #ffffff;
    padding: 20px;
}

.site-name {
    color: #004780;
    font-size: 24px;
    font-weight: bold;
}

nav ul {
    padding-left: 20px;
}

nav a {
    color: #004780;
}

nav a:hover {
    color: #b45309;
}

main {
    padding: 20px;
}

h1 {
    color: #004780;
}

section {
    margin-bottom: 32px;
}
```

Save with **Ctrl+S**.

### Step B — Explain each new CSS idea

- **`margin: 0` on `body`** removes the browser's default outer spacing around the page.
- **`.site-header`** selects the header by its `class` attribute, rather than selecting every header on the page.
- **`background-color`** fills the header with white; **`padding: 20px`** creates space **inside** the header around its content.
- **`.site-name`** selects the site name paragraph; **`font-size`** makes its text larger and **`font-weight: bold`** makes it heavier.
- **`nav ul`** selects lists within navigation. **`padding-left`** controls the space to the left of the list content.
- **`nav a`** styles links inside navigation without changing links elsewhere on the page.
- **`nav a:hover`** uses the **`:hover` pseudo-class**: the rule applies when a pointer is over a navigation link. Keyboard users do not rely on hover, so we will also test keyboard focus.
- **`main { padding: 20px; }`** adds space inside the main content area.
- **`section { margin-bottom: 32px; }`** adds space **outside** the bottom of each section.

**Padding versus margin:** Padding creates space *inside* an element's boundary. Margin creates space *outside* its boundary. We will explore the CSS box model in more detail in a later activity.

**Why isn't the navigation horizontal yet?** HTML lists are normally displayed vertically. That is acceptable for now. In Workshop 03-05, you will learn **Flexbox** to build a desktop navigation layout. In Workshop 03-06, you will make navigation responsive.

## 5. Test, predict, and debug (4 minutes)

### Test A — Open the correct page

1. Right-click **`Workshop3/02-header-nav/index.html`** and choose **Open with Live Server**, or open that file in your browser.
2. Confirm that the page shows **My Website**, two navigation links, and two content sections.
3. Click **About**. The URL should end with `#about`, and the browser should target the About section. On a short page, there may be little or no visible scrolling; the URL fragment still shows that the link was followed.
4. Click **Home**. The URL should end with `#home`.

### Test B — Keyboard navigation

Press **Tab** until a navigation link receives keyboard focus. Press **Enter** to activate it. Links should work without using a mouse. Your browser normally displays a visible focus indicator; do not remove it.

### Test C — Predict a selector change

**Predict:** What happens if you change `.site-name` to `p` in the CSS?

Try it, save, and refresh. All paragraphs now receive that rule, not just the site name. **Restore `.site-name` afterward.** This demonstrates why classes are useful for styling one type of component without affecting unrelated paragraphs.

### Troubleshooting

- **Links do not target sections:** Check that `href="#about"` matches `id="about"` exactly, including spelling and case.
- **No CSS styling:** Check that `index.html` and `styles.css` are in the same `02-header-nav` folder and that the HTML contains `href="styles.css"`.
- **Old webpage appears:** Check the browser URL and the file selected in VS Code. You may have opened `01-html-basics/index.html`.
- **Unexpected colours:** Look for missing CSS braces or semicolons. Check whether you accidentally left `p` in place of `.site-name`.
- **About link does not visibly scroll:** The page may not be tall enough to scroll. Check the URL fragment or temporarily make the browser window shorter.

## 6. Apply independently (approximately 2 minutes)

Complete these changes without replacing the entire page with another example:

- [ ] Change **My Website** to a meaningful site name of your choice.
- [ ] Add a **Contact** navigation link using `href="#contact"`.
- [ ] Add a matching `<section id="contact">` inside `<main>`, with an `<h2>` heading and a paragraph. Do not publish personal contact details.
- [ ] Test the new link with your mouse **and** keyboard.

**Hint:** A working link requires both an `<a href="#contact">` element and a matching section with `id="contact"`.

## 7. Commit and push your work (approximately 2 minutes)

1. Open **Source Control** in VS Code.
2. Confirm the changed files belong to **`Workshop3/02-header-nav/`**.
3. Stage your new activity files.
4. Commit using the message **`WS03-02: Semantic header and navigation`**.
5. Push or Sync Changes to your **existing WEBD 1000 course repository**.
6. Open GitHub and confirm the new activity folder contains `index.html` and `styles.css`.

**Do not** create a new repository for this workshop activity.

## Completion checklist

- [ ] I used my existing course repository and created `Workshop3/02-header-nav/`.
- [ ] My new folder contains `index.html` and `styles.css`.
- [ ] Workshop 03-01 remains unchanged.
- [ ] I can explain what `header`, `nav`, `main`, and `section` mean.
- [ ] I can explain how `href="#about"` connects to `id="about"`.
- [ ] I can distinguish element, class, ID, and descendant CSS selectors.
- [ ] My Home, About, and Contact links work.
- [ ] I tested keyboard navigation and committed/pushed my files.

## Reflection

1. What makes `<nav>` more meaningful than a generic `<div>` for navigation?
2. What is the difference between `.site-header` in CSS and `class="site-header"` in HTML?
3. Why must the `href` fragment and destination `id` match?
4. What is the difference between `padding` and `margin`?
5. How did you confirm that your navigation links work without a mouse?

**Submission:** Keep the working files and GitHub commit as technical evidence. No separate Brightspace submission is required unless directed by your instructor.

## Next: Workshop 03-03 — Hero Section

Create `Workshop3/03-hero/`, then copy the **completed** `index.html` and `styles.css` from `02-header-nav/` into it. You will replace the simple Home section with a more engaging **hero section** containing a heading, supporting text, an image, and two call-to-action links. Keep earlier activity folders unchanged so you can compare your progress.
