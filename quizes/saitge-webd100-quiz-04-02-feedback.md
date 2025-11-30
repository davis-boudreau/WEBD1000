1) Which of the following describes a “breakpoint”?  
a) A pixel where a color changes  
*b) A defined viewport width where layout rules change*  
c) The point where an image breaks  
d) A browser rendering bug  

✅ Feedback:
A **breakpoint** is a specific viewport width where CSS rules adapt to improve layout on different devices.  
Incorrect: Colors and browser bugs are unrelated to CSS breakpoints.

Example:
@media (max-width: 768px) {
  /* Apply new layout when width <= 768px */
  nav { flex-direction: column; }
}

------------------------------------------------------------

2) What does @media (orientation: landscape) detect?  
a) Screen resolution  
*b) Device held wider than tall*  
c) Screen pixel density  
d) Browser color depth  

✅ Feedback:
Orientation queries detect whether the device is in **portrait** or **landscape** mode.

Example:
@media (orientation: landscape) {
  body { background-color: #f0f0f0; } /* style change in landscape */
}

------------------------------------------------------------

3) When using Grid, which property defines automatic row sizing?  
a) grid-template-columns  
*b) grid-auto-rows*  
c) auto-fit  
d) grid-flow  

✅ Feedback:
`grid-auto-rows` assigns height for rows automatically created by the grid layout.

Example:
/* sets default height for auto rows */
.grid { display: grid; grid-auto-rows: minmax(150px, auto); }

------------------------------------------------------------

4) Which Flexbox rule vertically centers items inside a row container?  
a) justify-content: center;  
*b) align-items: center;*  
c) align-content: center;  
d) flex-wrap: center;  

✅ Feedback:
`align-items` handles vertical (cross-axis) alignment in Flexbox row layouts.

Example:
header {
  display: flex;
  align-items: center; /* centers vertically */
}

------------------------------------------------------------

5) What’s the main difference between min-width and max-width in media queries?  
*a) min-width triggers when viewport is larger; max-width triggers when smaller*  
b) Both trigger at the same size  
c) min-width affects height  
d) max-width sets background color  

✅ Feedback:
- `min-width`: activates for larger screens (progressive enhancement).  
- `max-width`: activates for smaller screens (graceful degradation).

Example:
@media (min-width: 768px) { body { font-size: 1.125rem; } }
@media (max-width: 600px) { nav { display: none; } }

------------------------------------------------------------

6) Which CSS unit changes proportionally to the viewport width?  
*a) vw*  
b) em  
c) rem  
d) px  

✅ Feedback:
`vw` = 1% of viewport width. Ideal for scaling headings or margins.

Example:
h1 { font-size: 6vw; } /* 6% of viewport width */

------------------------------------------------------------

7) What does this rule do?
img { max-width: 100%; height: auto; }  
*a) Prevents images from overflowing their container*  
b) Forces images to full screen  
c) Crops the image  
d) Centers the image  

✅ Feedback:
It ensures images shrink inside responsive containers.

Example:
figure img {
  max-width: 100%; /* fits parent */
  height: auto;     /* maintains aspect ratio */
}

------------------------------------------------------------

8) Which property in Flexbox controls spacing between items?  
a) padding  
*b) gap*  
c) margin  
d) order  

✅ Feedback:
`gap` evenly spaces child elements without extra markup.

Example:
.nav {
  display: flex;
  gap: 1rem; /* consistent spacing between buttons */
}

------------------------------------------------------------

9) What is a common problem solved by the “mobile-first” approach?  
a) Hides content for small screens  
*b) Prevents overwriting styles on narrow devices*  
c) Forces pixel-based design  
d) Eliminates color contrast issues  

✅ Feedback:
By defining base (mobile) styles first, you avoid conflicts when scaling up.

Example:
/* base styles for mobile first */
.container { flex-direction: column; }
/* enhance for desktop */
@media (min-width: 768px) { .container { flex-direction: row; } }

------------------------------------------------------------

10) Which layout method is best for two-dimensional (row + column) control?  
a) Flexbox  
*b) CSS Grid*  
c) Floats  
d) Positioning  

✅ Feedback:
Grid is two-dimensional (rows + columns), Flexbox is one-dimensional.

Example:
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

------------------------------------------------------------

11) Which media query hides an element on extra-large screens only?  
*a) @media (min-width: 1200px) { .element { display: none; } }*  
b) @media (max-width: 1200px)  
c) @media (width > 1200px)  
d) @media (screen-size: xl)  

✅ Feedback:
`min-width: 1200px` applies styles at or above 1200 pixels wide.

Example:
@media (min-width: 1200px) {
  .sidebar { display: none; }
}

------------------------------------------------------------

12) What is the purpose of the fr unit in CSS Grid?  
a) Fixed ratio  
*b) Fraction of available space*  
c) Font reference  
d) Frame reference  

✅ Feedback:
`fr` divides leftover space equally among grid tracks.

Example:
.grid { display: grid; grid-template-columns: 1fr 2fr; }

------------------------------------------------------------

13) How does auto-fit differ from auto-fill in Grid?  
*a) auto-fit collapses empty tracks to zero width*  
b) auto-fill hides content  
c) auto-fit repeats tracks infinitely  
d) auto-fill prevents wrapping  

✅ Feedback:
`auto-fit` compresses unused columns; `auto-fill` reserves them.

Example:
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}

------------------------------------------------------------

14) Which rule makes all headings scale smoothly between 1.5 rem and 3 rem?  
*a) font-size: clamp(1.5rem, 2vw + 1rem, 3rem);*  
b) font-size: min(1.5rem, 3rem);  
c) font-size: scale(1.5, 3);  
d) font-size: auto;  

✅ Feedback:
`clamp()` sets a responsive range: min, preferred, and max.

Example:
h1 { font-size: clamp(1.5rem, 2vw + 1rem, 3rem); }

------------------------------------------------------------

15) Why should line lengths be limited to ≈ 70 characters per line?  
*a) Improves readability on wide screens*  
b) Matches print standards only  
c) Slows page loading  
d) Is required by W3C  

✅ Feedback:
Optimal reading width supports accessibility and user focus.

Example:
p { max-width: 70ch; } /* ch = average character width */

------------------------------------------------------------

16) Which property controls alignment along the cross-axis in Flexbox?  
a) justify-content  
*b) align-items*  
c) flex-direction  
d) order  

✅ Feedback:
`align-items` controls alignment across the cross-axis.

Example:
.flexbox { display: flex; align-items: center; }

------------------------------------------------------------

17) What is the function of minmax() in Grid layouts?  
*a) Sets lower and upper limits for track size*  
b) Defines padding values  
c) Creates animations  
d) Sets aspect ratios  

✅ Feedback:
`minmax(min, max)` defines flexible track bounds.

Example:
.grid { grid-template-columns: repeat(3, minmax(200px, 1fr)); }

------------------------------------------------------------

18) How do you ensure typography remains accessible when zooming to 200 %?  
*a) Use relative units (em/rem) instead of px*  
b) Disable zoom  
c) Lock viewport  
d) Force fixed font sizes  

✅ Feedback:
Relative units resize naturally with user settings.

Example:
html { font-size: 100%; }
p { font-size: 1rem; }

------------------------------------------------------------

19) What’s the advantage of clamp() in CSS sizing?  
*a) Creates fluid scaling between a minimum and maximum value*  
b) Rounds sizes to integers  
c) Prevents scaling  
d) Randomly chooses a value  

✅ Feedback:
`clamp()` combines flexibility with accessibility for fluid text.

Example:
h2 { font-size: clamp(1.2rem, 2vw, 2rem); }

------------------------------------------------------------

20) Which CSS variable pattern improves consistency across breakpoints?  
*a) Use root-level custom properties (:root { --space-1: .5rem; })*  
b) Repeat values inline  
c) Hardcode pixel gaps  
d) Avoid variables entirely  

✅ Feedback:
Root-level variables allow global scaling and theme adaptation.

Example:
:root {
  --brand: #7b458f;
  --space-1: 0.5rem;
  --space-2: 1rem;
}
section { padding: var(--space-2); }

------------------------------------------------------------

21) Which responsive image technique chooses the right file for device width?  
*a) srcset with width descriptors*  
b) object-fit: cover  
c) background-size: contain  
d) filter: resolution()  

✅ Feedback:
`srcset` lets browsers download the best image for device width.

Example:
<img src="small.jpg"
     srcset="small.jpg 480w, medium.jpg 800w, large.jpg 1200w"
     sizes="(max-width: 600px) 90vw, 1200px"
     alt="Responsive image example">

------------------------------------------------------------

22) Why should flex-basis be used instead of fixed widths?  
*a) It defines the initial main-size and allows flexibility*  
b) It removes spacing  
c) It locks pixel size  
d) It centers items  

✅ Feedback:
`flex-basis` establishes a starting width that can grow/shrink.

Example:
.flex-item { flex: 1 1 200px; } /* 1 grow, 1 shrink, base 200px */

------------------------------------------------------------

23) What is the correct syntax to set a Grid container?  
*a) display: grid;*  
b) grid-display: block;  
c) layout: grid;  
d) grid: on;  

✅ Feedback:
`display: grid;` activates the Grid layout model.

Example:
.container { display: grid; grid-template-columns: repeat(3, 1fr); }

------------------------------------------------------------

24) Which design pattern improves readability on mobile?  
*a) Single-column layouts with larger text and spacing*  
b) Multi-column tables  
c) Hidden headings  
d) Wide hero banners only  

✅ Feedback:
Simplified single-column layouts enhance focus and accessibility.

Example:
@media (max-width: 768px) {
  .grid { grid-template-columns: 1fr; }
  body { line-height: 1.6; }
}

------------------------------------------------------------

25) Why is testing keyboard navigation part of responsive QA?  
*a) Ensures focus order remains logical when layout changes*  
b) Increases frame rate  
c) Adds more colors  
d) Improves SEO  

✅ Feedback:
When layouts shift, tab order and focus states must remain consistent.

Example:
/* visible focus indicator for accessibility */
a:focus, button:focus {
  outline: 3px solid #7b458f;
  outline-offset: 2px;
}
