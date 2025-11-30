WEBD1000 – Outcome 3 (Feedback + Examples)
Develop W3C-Compliant Websites Using HTML/CSS with a Text Editor or IDE

1) What does W3C compliance primarily ensure?
*a) Code follows web standards for accessibility and interoperability
b) Website loads faster on Chrome
c) All colors are WCAG-approved
d) Site looks identical on all browsers
Feedback: ✅ W3C compliance means code follows standards so content works consistently and accessibly across browsers.
Example:
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Corah</title>
</head>
<body>...</body>
</html>

2) Which tag correctly defines the main content of a webpage?
a) <article>
b) <div>
*c) <main>
d) <section>
Feedback: ✅ <main> identifies the primary content for assistive tech; use it once per page.
Example:
<header>...</header>
<main>
  <h1>Welcome to Corah</h1>
  <p>Primary page content…</p>
</main>
<footer>...</footer>

3) Which element should contain metadata like page title and linked stylesheets?
*a) <head>
b) <body>
c) <header>
d) <meta>
Feedback: ✅ <head> holds title, meta, and links to CSS.
Example:
<head>
  <meta charset="UTF-8">
  <title>Corah – Home</title>
  <link rel="stylesheet" href="styles.css">
</head>

4) Which attribute provides text for screen readers when an image cannot load?
*a) alt
b) src
c) title
d) desc
Feedback: ✅ Use alt to describe the image’s purpose in context.
Example:
<img src="logo.svg" alt="Corah fingerprint logo">

5) Which of the following is the correct HTML5 document type declaration?
*a) <!DOCTYPE html>
b) <!DOCTYPE HTML5>
c) <html version="5">
d) <html5>
Feedback: ✅ The simplified HTML5 doctype enables standards mode.
Example:
<!DOCTYPE html>
<html lang="en">...</html>

6) In a W3C-compliant page, where should the <link rel="stylesheet"> tag appear?
*a) Inside the <head> element
b) Inside the <body> element
c) At the bottom of the page
d) In the footer
Feedback: ✅ Put stylesheets in <head> to avoid unstyled flashes.
Example:
<head>
  <link rel="stylesheet" href="styles.css">
</head>

7) Which CSS rule correctly sets a background color?
a) background-color; #fff;
*b) background-color: #fff;
c) background:color(#fff);
d) bg-color = #fff;
Feedback: ✅ CSS uses property: value; syntax with a colon and semicolon.
Example:
body { background-color: #fff; }

8) Which property controls the space inside an element’s border?
a) margin
*b) padding
c) border
d) gap
Feedback: ✅ Padding = inside; margin = outside; gap = between flex/grid items.
Example:
.card {
  padding: 16px;
  margin: 24px 0;
}

9) What does “semantic HTML” mean?
*a) Using HTML tags that describe content meaning and structure
b) Adding IDs and classes to every element
c) Using short variable-like names
d) Using divs for everything
Feedback: ✅ Prefer meaningful tags like header/nav/main/section/footer.
Example:
<header>...</header>
<nav>...</nav>
<main>
  <section aria-labelledby="about"><h2 id="about">About</h2></section>
</main>
<footer>...</footer>

10) Which element represents navigational links?
a) <aside>
*b) <nav>
c) <footer>
d) <menu>
Feedback: ✅ Group site or section navigation with <nav>.
Example:
<nav aria-label="Primary">
  <a href="/">Home</a>
  <a href="/events">Events</a>
  <a href="/contact">Contact</a>
</nav>

11) What is the purpose of the W3C Markup Validation Service?
*a) To check HTML for syntax and standard errors
b) To analyze page speed
c) To test server load
d) To generate SEO keywords
Feedback: ✅ Use the validator to catch invalid elements/attributes/nesting.
Example (fixing a nesting issue):
<!-- BAD --> <p><div>Don’t nest div inside p</div></p>
<!-- GOOD --> <p>Paragraph</p><div>Separate block element</div>

12) Which CSS selector targets all <p> elements inside a <div>?
*a) div p { }
b) div.p { }
c) div#p { }
d) div>* { }
Feedback: ✅ A space creates a descendant selector (any depth).
Example:
div p { line-height: 1.6; }

13) Which declaration makes text bold in CSS?
a) font-type: bold;
*b) font-weight: bold;
c) text-style: bold;
d) font-bold: on;
Feedback: ✅ Use font-weight with keywords (bold) or numbers (700).
Example:
h1 { font-weight: 700; }

14) Which tag is used to create a hyperlink in HTML?
a) <link>
*b) <a>
c) <href>
d) <url>
Feedback: ✅ The anchor tag <a> creates clickable links via href.
Example:
<a href="https://www.nscc.ca">Visit NSCC</a>

15) Which CSS unit is relative to the root element’s font size?
a) em
*b) rem
c) px
d) %
Feedback: ✅ rem scales from the root font size for consistent type scales.
Example:
html { font-size: 16px; }
h1 { font-size: 2rem; } /* 32px */

16) Which CSS layout module provides flexible alignment of elements?
*a) Flexbox
b) Grid
c) Float
d) Block
Feedback: ✅ Use Flexbox for 1-D alignment; Grid for 2-D layouts.
Example:
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

17) Which HTML tag defines a table header cell?
*a) <th>
b) <td>
c) <tr>
d) <thead>
Feedback: ✅ <th> marks header cells; add scope for accessibility.
Example:
<table>
  <thead><tr><th scope="col">Name</th><th scope="col">Age</th></tr></thead>
  <tbody><tr><td>Alex</td><td>66</td></tr></tbody>
</table>

18) What is the function of the <footer> element?
*a) Defines the bottom section of a page containing metadata or links
b) Displays copyright text only
c) Used to add images
d) Contains JavaScript scripts
Feedback: ✅ Footer commonly includes contact, copyright, nav, policies.
Example:
<footer>
  <p>&copy; 2025 Corah</p>
  <nav aria-label="Footer">
    <a href="/privacy">Privacy</a> · <a href="/accessibility">Accessibility</a>
  </nav>
</footer>

19) Which property sets the font family in CSS?
a) font-face
*b) font-family
c) font-type
d) text-font
Feedback: ✅ font-family lists preferred fonts with fallbacks.
Example:
body { font-family: "Open Sans", Arial, sans-serif; }

20) In CSS, which symbol indicates a class selector?
a) #
*b) .
c) @
d) $
Feedback: ✅ Use .className in CSS; #idName selects IDs.
Example:
.logo-container { display: flex; }

21) What is the correct HTML element for the largest heading?
*a) <h1>
b) <h6>
c) <title>
d) <heading>
Feedback: ✅ Use a single, descriptive <h1> per page where possible.
Example:
<h1>Corah – Centre for Rural Aging & Health</h1>

22) Which CSS feature allows you to reuse values like colors and fonts?
*a) CSS variables (custom properties, e.g., --brand)
b) Functions
c) IDs
d) Comments
Feedback: ✅ Custom properties centralize design tokens for easy updates.
Example:
:root { --brand: #7B458F; --text: #111; }
a { color: var(--brand); }
body { color: var(--text); }

23) When writing W3C-compliant code, what should always be included for accessibility?
*a) Meaningful alt text and ARIA where appropriate
b) Inline styles for every element
c) Animations on every link
d) HTML comments explaining each line
Feedback: ✅ Pair semantics with alt/labels/roles for assistive tech.
Example:
<button aria-label="Open navigation menu">
  <svg aria-hidden="true" ...></svg>
</button>

24) Why should developers validate CSS?
a) To increase server speed
*b) To ensure properties and values follow W3C standards
c) To add more colors
d) To remove semantic markup
Feedback: ✅ Validation catches typos/unsupported properties for cross-browser reliability.
Example:
/* BAD */ font-wieght: bold;
/* GOOD */ font-weight: bold;

25) What is the purpose of indentation and consistent formatting in HTML/CSS?
*a) Improves readability and maintainability of code
b) Speeds up download time
c) Creates animations
d) Changes browser rendering
Feedback: ✅ Consistent formatting aids reviews, debugging, and collaboration.
Example:
<header>
  <h1>Corah</h1>
  <nav>...</nav>
</header>
