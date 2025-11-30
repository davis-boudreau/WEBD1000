WEBD1000 — Outcome 4 (Full MC + Large Code Examples with Comments)
Implement CSS to Meet Responsive Page Layout Requirements

------------------------------------------------------------
1) What does “responsive design” mean?
*a) The layout adjusts automatically to different screen sizes
b) The website loads faster
c) The colors change randomly
d) The navigation disappears on small screens

Explanation:
Responsive design adapts layout, type, and media for many viewports using fluid units and media queries.

Example (fluid container + small breakpoint)
/* Base styles (mobile-first) */
html { font-size: 16px; }                 /* root type scale */
body { margin: 0; }
.container {
  width: min(90vw, 70ch);                 /* fluid max width */
  margin: 0 auto;                         /* center */
  padding: 1rem;
  line-height: 1.6;
}
/* Enhance spacing and layout above 768px */
@media (min-width: 768px) {
  .container { width: min(85vw, 95ch); }
}
------------------------------------------------------------

2) Which CSS feature is essential for responsive design?
a) z-index
*b) media queries
c) hover states
d) CSS transitions

Explanation:
Media queries let you conditionally apply CSS at certain viewport sizes.

Example (stack → two columns)
/* Mobile-first: stacked cards */
.cards { display: grid; gap: 1rem; }
.cards article { padding: 1rem; border: 1px solid #ddd; }

/* At ≥ 768px, switch to a 2-column grid */
@media (min-width: 768px) {
  .cards { grid-template-columns: 1fr 1fr; }
}
------------------------------------------------------------

3) What is the “mobile-first” design approach?
*a) Start styling for the smallest screens and scale up with media queries
b) Begin with desktop layout and shrink it
c) Design mobile and desktop separately
d) Use only flexible images

Explanation:
Write default CSS for the smallest view first, then add @media (min-width: …) rules for larger screens.

Example (mobile-first button → bigger targets on wide screens)
/* Base (mobile) */
.button { font-size: 1rem; padding: .75rem 1rem; }

/* Larger screens: increase comfortable target size */
@media (min-width: 1024px) {
  .button { font-size: 1.125rem; padding: .9rem 1.25rem; }
}
------------------------------------------------------------

4) Which unit is best for responsive font sizing?
a) px
*b) rem
c) in
d) pt

Explanation:
rem scales from the root <html> size, enabling user-preference zoom and consistent type scales.

Example (type scale with rem + clamp)
/* Root scaling + fluid heading using clamp(min, preferred, max) */
html { font-size: 16px; }
h1 { font-size: clamp(1.8rem, 2.5vw + 1rem, 2.6rem); }
p  { font-size: 1rem; line-height: 1.6; }
------------------------------------------------------------

5) Which CSS property defines flexible grid columns?
a) float
*b) grid-template-columns
c) column-width
d) justify-content

Explanation:
In CSS Grid, grid-template-columns defines the column tracks.

Example (auto-fit responsive cards)
/* Fill available space with responsive columns min 220px wide */
.grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}
------------------------------------------------------------

6) In Flexbox, which property aligns items along the main axis?
a) align-items
*b) justify-content
c) align-content
d) order

Explanation:
justify-content distributes items along the container’s main axis (row by default).

Example (logo left, nav right)
/* Row main axis: space-between pushes ends apart */
.header {
  display: flex;
  justify-content: space-between;  /* main axis alignment */
  align-items: center;              /* cross axis center */
  padding: 1rem;
}
------------------------------------------------------------

7) Which HTML meta tag enables responsive scaling on mobile devices?
*a) <meta name="viewport" content="width=device-width, initial-scale=1.0">
b) <meta charset="UTF-8">
c) <meta name="mobile" content="true">
d) <meta responsive>

Explanation:
Viewport meta tells the browser to size the layout viewport to the device width.

Example (critical head tags)
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Corah</title>
  <link rel="stylesheet" href="styles.css">
</head>
------------------------------------------------------------

8) What layout method uses rows and columns simultaneously?
a) Flexbox
*b) Grid
c) Float
d) Table

Explanation:
Grid is two-dimensional (rows + columns); Flexbox is one-dimensional.

Example (header/aside/main/footer grid)
/* Template areas for semantic regions */
.layout {
  display: grid;
  grid-template:
    "header header" auto
    "aside  main"   1fr
    "footer footer" auto / 240px 1fr;
  min-height: 100vh;
  gap: 1rem;
}
header { grid-area: header; }
aside  { grid-area: aside; }
main   { grid-area: main; }
footer { grid-area: footer; }

/* Collapse to one column on small screens */
@media (max-width: 640px) {
  .layout { grid-template:
    "header" auto
    "main"   auto
    "aside"  auto
    "footer" auto / 1fr; }
}
------------------------------------------------------------

9) Which CSS declaration hides an element visually but keeps it accessible to screen readers?
*a) position: absolute; left: -9999px;
b) display: none;
c) opacity: 0;
d) visibility: hidden;

Explanation:
Off-screen positioning keeps element in the accessibility tree. display:none/visibility:hidden removes it from AT.

Example (visually hidden utility)
/* Screen reader only (keeps in accessibility tree) */
.sr-only {
  position: absolute; left: -9999px; top: auto; width: 1px; height: 1px; overflow: hidden;
}
------------------------------------------------------------

10) Which media query targets devices narrower than 768 px?
*a) @media (max-width: 768px)
b) @media (min-height: 768px)
c) @media (width: >768px)
d) @media (less:768px)

Explanation:
max-width applies when viewport width is ≤ 768px.

Example (collapse nav to menu)
/* Desktop nav visible by default */
.nav { display: flex; gap: 1rem; }
/* At ≤ 768px, hide full nav; show menu button */
@media (max-width: 768px) {
  .nav { display: none; }
  .menu-btn { display: inline-flex; }
}
------------------------------------------------------------

11) Which Flexbox property allows items to wrap to a new line?
*a) flex-wrap: wrap;
b) align-items: wrap;
c) wrap: yes;
d) flex-direction: row;

Explanation:
flex-wrap controls whether flex items remain on one line or wrap.

Example (pills that wrap)
/* Horizontal pills that wrap on small screens */
.pills {
  display: flex;
  flex-wrap: wrap;    /* allow wrapping */
  gap: .5rem;
}
------------------------------------------------------------

12) How do responsive images improve performance?
*a) Serve smaller image files on small screens
b) Use fixed pixel sizes
c) Repeat images as backgrounds
d) Stretch all images to fit

Explanation:
Use srcset/sizes so the browser downloads the best fit for the viewport & DPR.

Example (srcset responsive image)
<img
  src="hero-800.jpg"
  srcset="hero-480.jpg 480w, hero-800.jpg 800w, hero-1280.jpg 1280w"
  sizes="(max-width: 600px) 90vw, (max-width: 1024px) 80vw, 1200px"
  alt="Corah community event">
------------------------------------------------------------

13) Which property centers a block element horizontally?
*a) margin: 0 auto;
b) text-align: center;
c) float: center;
d) display: block auto;

Explanation:
margin-left/right: auto centers a block with fixed/limited width.

Example (center a fixed-width card)
.card {
  width: min(90vw, 40rem);
  margin: 0 auto;                 /* horizontal centering */
  padding: 1rem;
  border: 1px solid #ddd;
}
------------------------------------------------------------

14) Why are relative units (%, em, rem) preferred in responsive layouts?
*a) They adapt to user preferences and device widths
b) They lock fixed sizes
c) They disable zooming
d) They speed up animation

Explanation:
Relative units fluidly adapt to container and root size, improving accessibility.

Example (fluid widths + scalable text)
.wrapper { width: 92%; max-width: 72rem; margin: 0 auto; }
h2 { font-size: clamp(1.25rem, 2vw + 1rem, 2rem); }
------------------------------------------------------------

15) Which display property activates Flexbox?
*a) display: flex;
b) display: grid;
c) display: inline;
d) display: box;

Explanation:
Flex formatting context begins with display:flex.

Example (header layout)
header {
  display: flex;                  /* activates Flexbox */
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
------------------------------------------------------------

16) How can you test responsive behavior in Chrome DevTools?
*a) Use Device Toolbar and change viewport width
b) Press F1
c) Refresh the page
d) Disable cache

Explanation:
Toggle Device Toolbar (Ctrl/Cmd+Shift+M) to simulate devices and widths.

Example (no code—tooling workflow)
Steps:
1) Open DevTools → Toggle device toolbar
2) Pick devices (iPhone SE, iPad, Desktop) and rotate
3) Drag handles to test custom widths and check breakpoints
------------------------------------------------------------

17) Which CSS Grid property defines space between rows and columns?
*a) gap
b) margin
c) padding
d) justify-content

Explanation:
gap adds uniform spacing between grid (and flex) items without extra wrappers.

Example (card grid with gap)
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(18rem, 1fr));
  gap: 1rem;                          /* spacing between tracks */
}
------------------------------------------------------------

18) Which property adjusts item order in Flexbox?
*a) order
b) flex-flow
c) align-content
d) z-index

Explanation:
order allows visual reordering without changing the HTML source.

Example (CTA first on mobile, second on desktop)
/* Mobile-first: CTA appears first */
.cta { order: -1; }

/* Desktop: normal flow (order defaults to 0) */
@media (min-width: 960px) { .cta { order: 0; } }
------------------------------------------------------------

19) Why is consistent spacing (gap, padding, margins) important?
*a) Creates visual rhythm and supports readability
b) Reduces load time
c) Fills empty space automatically
d) Changes browser behavior

Explanation:
Consistent spacing clarifies hierarchy, improves scanability, and aids touch accuracy.

Example (spacing system with CSS variables)
:root { --space-1: .5rem; --space-2: 1rem; --space-3: 1.5rem; }
.stack > * + * { margin-top: var(--space-2); } /* vertical rhythm */
.grid { display: grid; gap: var(--space-2); }
------------------------------------------------------------

20) What does “fluid layout” mean?
*a) Uses relative units so elements scale with the viewport
b) Uses fixed pixel dimensions
c) Resizes text only
d) Requires JavaScript resizing

Explanation:
Fluid layouts rely on percentages and viewport-relative units (vw/vh) or rem to flex naturally.

Example (fluid hero)
.hero {
  padding: clamp(1rem, 3vw, 3rem);
  width: 100%;
}
.hero img { max-width: 100%; height: auto; }
------------------------------------------------------------

21) In mobile-first design, which breakpoint is usually the default style?
*a) Smallest screen (base styles)
b) Medium screen
c) Largest desktop
d) Print layout

Explanation:
Base CSS targets the smallest viewport; larger screens add enhancements.

Example (base first, then enhance)
/* Base (phones) */
.card { padding: 1rem; font-size: 1rem; }
/* Tablets/desktops enhance */
@media (min-width: 768px)  { .card { padding: 1.25rem; } }
@media (min-width: 1200px) { .card { padding: 1.5rem;  } }
------------------------------------------------------------

22) Which CSS function/prop limits an element’s maximum width?
*a) max-width
b) width
c) min-width
d) contain

Explanation:
max-width prevents elements from growing beyond a specified limit.

Example (images never overflow container)
img { max-width: 100%; height: auto; display: block; }
.prose { max-width: 70ch; margin: 0 auto; }
------------------------------------------------------------

23) Which approach ensures accessible color contrast in responsive design?
*a) Use WCAG 2.1 contrast ratio (4.5:1 normal text)
b) Choose any matching brand colors
c) Use pure white text always
d) Add shadow to all text

Explanation:
WCAG contrast ratios preserve legibility across themes and devices.

Example (tokens + prefers-color-scheme)
/* Color tokens */
:root { --brand: #7B458F; --ink: #111; --paper: #fff; }
@media (prefers-color-scheme: dark) {
  :root { --ink: #f5f5f5; --paper: #121212; }
}
body { color: var(--ink); background: var(--paper); }
a { color: var(--brand); }
/* Use tooling (e.g., DevTools / contrast checkers) to verify 4.5:1 */
------------------------------------------------------------

24) Which design principle improves usability on mobile devices?
*a) Large tap targets and spacing between interactive elements
b) Use hover effects only
c) Hide navigation
d) Disable zoom

Explanation:
Touch interfaces need larger targets (44–48px) and adequate spacing.

Example (tap target sizing)
button, .pill {
  min-height: 44px;               /* Apple HIG / common guidance */
  padding: .6rem 1rem;
}
.pill + .pill { margin-left: .5rem; }
------------------------------------------------------------

25) Why should developers test sites on multiple devices?
*a) To confirm responsive behavior and consistent accessibility
b) To improve server speed
c) To change typography
d) To reset cookies

Explanation:
Real devices reveal viewport quirks, pixel density differences, focus styles, and keyboard/touch behavior that emulators may miss.

Example (test checklist, not code)
- Test on iPhone SE (320px), typical Android, iPad, a laptop, and a large desktop
- Check landmarks, keyboard focus rings, color contrast
- Verify media queries trigger at intended breakpoints
- Exercise zoom (200%) and prefers-color-scheme
------------------------------------------------------------
