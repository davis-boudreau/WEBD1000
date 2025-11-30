WEBD1000 – Outcome 3 (Set B: Feedback + Examples)
Develop W3C-Compliant Websites Using HTML / CSS with a Text Editor or IDE

1) Which attribute specifies the language of an HTML document?
*a) lang
b) xml
c) charset
d) locale
Feedback: ✅ The `lang` attribute lets browsers and assistive tech identify the document language for correct pronunciation and translation.
Example: <html lang="en">

2) What is the correct way to insert a comment in HTML?
*a) <!-- This is a comment -->
b) // This is a comment
c) # This is a comment
d) /* This is a comment */
Feedback: ✅ HTML comments start with `<!--` and end with `-->`. Other syntaxes belong to CSS, JS, or shell scripting.
Example:
<!-- Developer note: update navigation before launch -->

3) Which element defines emphasized text in HTML?
a) <strong>
*b) <em>
c) <i>
d) <mark>
Feedback: ✅ `<em>` indicates emphasis and is read aloud with stress by screen readers. `<strong>` conveys importance; `<i>` is purely visual.
Example: <p>Please <em>remember</em> to validate your code.</p>

4) Which tag creates an unordered list?
a) <ol>
*b) <ul>
c) <li>
d) <list>
Feedback: ✅ `<ul>` builds bullet lists; `<li>` defines list items; `<ol>` is numbered.
Example:
<ul>
  <li>Home</li>
  <li>About</li>
</ul>

5) Which element defines a block of pre-formatted text?
*a) <pre>
b) <code>
c) <p>
d) <blockquote>
Feedback: ✅ `<pre>` preserves spaces and line breaks—useful for code samples.
Example:
<pre>
Name: Davis
Course: WEBD1000
</pre>

6) What does the “href” attribute do in an <a> tag?
a) Adds hover color
*b) Specifies the hyperlink destination
c) Defines text alignment
d) Opens an image
Feedback: ✅ `href` identifies the link target—URL, email, or file.
Example: <a href="https://nscc.ca">Visit NSCC</a>

7) Which attribute opens a hyperlink in a new browser tab?
*a) target="_blank"
b) rel="new"
c) open="tab"
d) new="true"
Feedback: ✅ `target="_blank"` instructs browsers to open in a new tab/window.
Example:
<a href="https://corah.ca" target="_blank">Corah site</a>

8) In HTML, which element groups related form inputs?
*a) <fieldset>
b) <formgroup>
c) <section>
d) <group>
Feedback: ✅ `<fieldset>` groups fields; `<legend>` provides a label for accessibility.
Example:
<fieldset>
  <legend>Contact Info</legend>
  <label>Email:<input type="email"></label>
</fieldset>

9) What is the function of the <label> element?
a) Displays placeholder text
*b) Describes the purpose of a form input
c) Submits form data
d) Adds spacing between inputs
Feedback: ✅ Labels link text to form controls via the `for` attribute, improving accessibility.
Example:
<label for="name">Full Name:</label>
<input id="name" type="text">

10) Which of the following creates a numbered list?
*a) <ol>
b) <ul>
c) <list>
d) <num>
Feedback: ✅ `<ol>` automatically numbers items.
Example:
<ol>
  <li>Plan</li>
  <li>Design</li>
  <li>Develop</li>
</ol>

11) In CSS, which property controls text size?
*a) font-size
b) text-size
c) font-height
d) text-weight
Feedback: ✅ `font-size` defines the height of characters.
Example: p { font-size: 1rem; }

12) Which property changes the color of text?
*a) color
b) font-color
c) text-color
d) font-tint
Feedback: ✅ The CSS property is simply `color`; others are invalid.
Example: h1 { color: #7B458F; }

13) What does the “id” attribute uniquely identify?
*a) A single element on a page
b) Multiple related elements
c) All elements with same class
d) External files
Feedback: ✅ Each id must be unique for scripting and linking.
Example: <section id="hero">...</section>

14) Which CSS property changes text alignment?
*a) text-align
b) align
c) justify-items
d) flex-align
Feedback: ✅ Use `text-align: center|left|right|justify;` to align inline content.
Example: h2 { text-align: center; }

15) How do you insert a comment in CSS?
*a) /* comment */
b) <!-- comment -->
c) // comment
d) # comment
Feedback: ✅ CSS uses `/* ... */`. HTML and JS comments differ.
Example:
body {
  /* Adjust line spacing for readability */
  line-height: 1.6;
}

16) Which tag defines inline code snippets in HTML?
*a) <code>
b) <pre>
c) <kbd>
d) <var>
Feedback: ✅ `<code>` marks short code fragments inline.
Example: Use the <code>&lt;header&gt;</code> tag for page headers.

17) What is the correct syntax for linking an external CSS file?
*a) <link rel="stylesheet" href="style.css">
b) <style src="style.css">
c) <css link="style.css">
d) <script href="style.css">
Feedback: ✅ Only `<link>` with rel and href correctly attaches a CSS file.
Example:
<head>
  <link rel="stylesheet" href="style.css">
</head>

18) Which HTML element is used for short quotations?
*a) <q>
b) <blockquote>
c) <cite>
d) <quote>
Feedback: ✅ `<q>` inserts inline quotes; browsers add quotation marks automatically.
Example:
<p>The mentor said <q>validate early and often</q>.</p>

19) Which tag defines a section of navigation links within a page?
*a) <nav>
b) <header>
c) <section>
d) <aside>
Feedback: ✅ `<nav>` semantically groups navigation menus.
Example:
<nav>
  <a href="#home">Home</a> |
  <a href="#about">About</a>
</nav>

20) What does the <meta charset="UTF-8"> declaration specify?
*a) The character encoding for the document
b) The author of the document
c) The viewport width
d) The page language
Feedback: ✅ UTF-8 supports all major characters and symbols globally.
Example:
<meta charset="UTF-8">

21) Which attribute in forms ensures a field must be filled?
*a) required
b) must
c) validate
d) checked
Feedback: ✅ `required` enforces client-side validation before submission.
Example:
<input type="email" required>

22) Which of the following makes a text input field read-only?
*a) readonly
b) lock
c) noedit
d) disabled="false"
Feedback: ✅ `readonly` lets users see data but not change it.
Example:
<input type="text" value="NSCC Student" readonly>

23) In CSS, what does the property “border-radius” control?
*a) The roundness of element corners
b) The border color
c) The border width
d) The element’s shadow
Feedback: ✅ Rounded corners improve design consistency.
Example:
button {
  border-radius: 8px;
}

24) What is the default display type for a <div> element?
*a) block
b) inline
c) flex
d) grid
Feedback: ✅ Divs are block-level, taking full width by default.
Example:
<div>Block element</div>

25) Which tool or feature in an IDE like VS Code assists W3C-compliant development?
*a) HTML/CSS linting or validation extensions
b) Image optimizer
c) Font previewer
d) Markdown renderer
Feedback: ✅ Linters highlight invalid properties, nesting, and accessibility issues to maintain compliance.
Example: In VS Code install the “HTML Hint” or “stylelint” extension.
