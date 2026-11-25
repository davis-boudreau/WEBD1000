# WEBD 1000 Website Development Cheatsheet

Fall 2026 · Quick reference for workshops and the independent website project

## Plan and evaluate

| Topic | What to remember |
| --- | --- |
| Usability | Give someone a realistic task. Watch whether they can find the right page, understand their options, and complete the task. |
| Project brief | Define the site's purpose, target audience, priority tasks, and required content. |
| Information architecture | Group related content and give pages and navigation links clear, predictable names. |
| Sitemap | Map pages and their relationships. An HTML sitemap is a page of links visitors can use. |
| Wireframe | Sketch the content order and layout for a page. Use narrow and wide sketches to plan what wraps, stacks, or changes position. |

## Build semantic HTML

- Start with `<!doctype html>` and `<html lang="en">`. In `<head>`, include UTF-8 encoding, a descriptive page `<title>`, a viewport meta tag, and a link to the stylesheet.
- Use `header`, `nav`, `main`, and `footer` to identify page regions. Give each page a clear `h1`, then use `h2` and `h3` to reflect the content hierarchy.
- Use `<a href="…">` for navigation and `<button>` for actions. Use descriptive link text and mark the current navigation link with `aria-current="page"`.
- Give informative images meaningful `alt` text and decorative images `alt=""`. Use lists for related items and `article` for self-contained content such as a standalone news item.
- Match a visible label’s `for` to the form control’s `id`. Choose an appropriate input type, such as `email`, and explain errors in text.
- Resolve relative paths from the current file. From `pages/about.html`, `../index.html` goes up one folder to the home page.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="styles.css">
```

## Style with CSS and design tokens

| Topic | What to remember |
| --- | --- |
| Selectors | `p` matches an element, `.card` a class, and `.card h2` a heading inside a card. Use DevTools to see which rule wins. |
| Cascade | Among competing normal rules in the same origin and layer, higher specificity wins. With equal specificity, the later rule wins. |
| Box model | Content, padding, border, then margin. `box-sizing: border-box` counts padding and border within the declared width. |
| Design tokens | Define shared values in `:root`, then use `var(--token)`. Choose names that describe roles, such as `--color-text` or `--color-surface`. |
| Visual hierarchy | Use consistent typography, line height, spacing, and colour. Check text against the actual background. Design visible focus and hover states. |

```css
:root {
  --color-surface: #f4f6f8;
  --color-text: #1a2430;
  --space-md: 1rem;
}

.card {
  padding: var(--space-md);
  color: var(--color-text);
  background: var(--color-surface);
}
```

## Make the layout responsive

- **Flexbox** works along one axis at a time. Use `display: flex`, `gap`, and `flex-wrap: wrap` for navigation and rows of controls. `justify-content` controls the main axis and `align-items` the cross axis.
- **Grid** controls rows and columns. Use `display: grid`, `gap`, and `grid-template-columns` for card layouts and other aligned content.
- **Mobile first** means writing the narrow layout as the default. Add `min-width` media queries where the content has room to rearrange. Test between breakpoints as well as at common viewport sizes.
- **Fluid sizing** lets content adapt. Use `max-width: 100%; height: auto` for images that should shrink with their container. Use `max-width` to limit how far a content area grows.

```css
.site-nav { display: flex; flex-wrap: wrap; gap: 1rem; }
.cards { display: grid; gap: 1rem; }

@media (min-width: 48rem) {
  .cards { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
```

## Test, validate, and publish

- **Keyboard and accessibility.** Tab and Shift+Tab through the page, check focus visibility, and activate links and controls with the keyboard. Verify heading order, form labels, image alternatives, and text contrast. Aim for at least 4.5:1 for normal text and 3:1 for large text. Pair colour cues with text or another visible indicator.
- **Cross-device testing.** Check narrow, medium, and wide viewports in DevTools and try a real device when available. Check for horizontal scrolling, awkward wrapping, broken navigation, and clipped content when zoomed. Record the page, browser or viewport, issue, fix, and retest result.
- **Validation.** Run the W3C HTML and CSS validators, fix errors, and recheck. Perform manual usability and accessibility checks as well.
- **Git workflow.** Preview in VS Code with Live Server. Use `git status`, `git add <files>`, `git commit -m "Describe the change"`, and `git push`. Keep guided workshops in the course repository and the semester website in its own repository.
- **GitHub Pages.** Publish the project, then open the live URL and check each page, stylesheet, image, and navigation link. Check filename capitalization and relative paths if something worked locally but fails live. Submit the required evidence in Brightspace.

## Project sequence

M1 Project brief → M2 Sitemap and wireframes → M3 Semantic HTML → M4 CSS → M5 Responsive implementation → M6 Cross-device testing → M7 Accessibility and validation → Final published website

[Fall 2026 workplan](../Fall-2026-Workplan-version-2.md) · [Project milestones](../sa-itos-webd1000-All_Project_Assessments.md) · [Testing, validation, and publication workshop](../sa-itos-wedb1000-ws03-12-Testing_Validation_and_Publication.md)
