# WEBD 3100 — Workshop 03A

## Colour Theory, Design Tokens & CSS Themes

Student Workshop Guide | Fall 2026

This workshop connects the visual design skills you have learned in Figma with modern CSS development. You will learn how colour choices become reusable design tokens, how those tokens support light and dark themes, and how a consistent colour system can be used across an entire website.

### Workshop Details

|              |                                                                                      |
| ------------ | ------------------------------------------------------------------------------------ |
| Course       | WEBD 3100 — Web Design Fundamentals                                                  |
| Instructor   | Davis Boudreau                                                                       |
| Workshop     | 03A — Colour Theory, Design Tokens & CSS Themes                                      |
| Duration     | Approximately 2–3 hours                                                              |
| Prerequisite | Workshop 02 — Visual Design Principles & Usability Heuristics                        |
| Tools        | Figma, VS Code, browser, Live Server, GitHub                                         |
| Assessment   | Part of Workshop 03 (03A + 03B), combined 4%                                         |
| Submission   | Student Submission Template, Figma link, GitHub evidence, reflection via Brightspace |

## 1. Where are you in the design process?

Professional web design follows a process. Each workshop helps you develop the knowledge and skills needed for one or more steps.

\#chatgpt-mermaid-\_r_10d\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_10d\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_10d\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_10d\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_10d\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10d\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_10d\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_10d\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_10d\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_10d\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_10d\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_10d\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_10d\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_10d\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_10d\_ p{margin:0;}#chatgpt-mermaid-\_r_10d\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10d\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10d\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10d\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_10d\_ .label text,#chatgpt-mermaid-\_r_10d\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10d\_ .node rect,#chatgpt-mermaid-\_r_10d\_ .node circle,#chatgpt-mermaid-\_r_10d\_ .node ellipse,#chatgpt-mermaid-\_r_10d\_ .node polygon,#chatgpt-mermaid-\_r_10d\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_10d\_ .rough-node .label text,#chatgpt-mermaid-\_r_10d\_ .node .label text,#chatgpt-mermaid-\_r_10d\_ .image-shape .label,#chatgpt-mermaid-\_r_10d\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_10d\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_10d\_ .rough-node .label,#chatgpt-mermaid-\_r_10d\_ .node .label,#chatgpt-mermaid-\_r_10d\_ .image-shape .label,#chatgpt-mermaid-\_r_10d\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_10d\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_10d\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_10d\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_10d\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_10d\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_10d\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_10d\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_10d\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_10d\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_10d\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_10d\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10d\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10d\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_10d\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10d\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_10d\_ .icon-shape,#chatgpt-mermaid-\_r_10d\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_10d\_ .icon-shape p,#chatgpt-mermaid-\_r_10d\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_10d\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_10d\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_10d\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_10d\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_10d\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_10d\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_10d\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_10d\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_10d\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_10d\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_10d\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_10d\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_10d\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_10d\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_10d\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_10d\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_10d\_ .node rect,#chatgpt-mermaid-\_r_10d\_ .node circle,#chatgpt-mermaid-\_r_10d\_ .node ellipse,#chatgpt-mermaid-\_r_10d\_ .node polygon,#chatgpt-mermaid-\_r_10d\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_10d\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_10d\_ .node.mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_10d\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_10d\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_10d\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}1. Discover2. Define3. Structure4. DesignYOU ARE HERE5. Prototype6. Validate7. Implement8. Deploy9. Test & Refine10. Deliver

Your six-phase learning journey is:

Understand → Plan → Design → Build → Evaluate → Deliver

In this workshop, you are primarily learning the Design phase. You will also practise a small part of the Build phase by translating your Figma colour choices into CSS.

You are not expected to finalize your integrated project's entire design system today.

## 2. Why are you learning this?

Imagine that you are designing an event-management application. You have a navigation bar, event cards, registration buttons, forms, and confirmation messages.

You decide that blue will be your primary colour.

But which blue should you use for buttons? Should headings use the same blue? What happens when a user switches to dark mode? How will you keep colours consistent across multiple pages?

A professional approach is to create a colour system rather than choosing individual colours independently.

By the end of this workshop, you will have created a small colour system in Figma and implemented it in a working HTML/CSS page.

## 3. Learning objectives

By completing this workshop, you should be able to:

- Explain hue, saturation, lightness, and basic colour relationships.
- Describe the purpose of colour ramps and OKLCH.
- Build and label a colour ramp in Figma.
- Distinguish foundation colour tokens from semantic colour tokens.
- Create reusable CSS custom properties.
- Apply colour tokens to a web interface.
- Demonstrate light and dark themes.
- Test text contrast and improve accessibility.
- Explain how your colour system can support future frameworks such as Tailwind CSS.

## 4. Before you begin — Set up your Figma workspace

Your Figma design file is a working record of your progress throughout the course. Your instructor will use the shared file to review your work and provide feedback during workshop activities.

Required Figma sharing

1. Open your WEBD 3100 Figma design file.
2. Select Share.
3. Invite davis.boudreau\@nscc.ca.
4. Grant Can view access, unless your instructor requests another permission.
5. Send the invitation.
6. Verify that your instructor has access.
7. Create a page named `Workshop 03A — Colour Systems`.

If you have not yet created a course design file, name it `WEBD3100 — Your Name — Design Workspace`.

Keep your Figma work organized with clearly named pages and frames. You will include your Figma file link in your submission template.

# Part A — Observe and understand colour

## 5. Activity 1 — Colour observation

Estimated time: 10 minutes

Open a website you regularly use. Examine its homepage and at least one additional page.

Look for colours used in navigation, headings, buttons, links, backgrounds, cards, and status messages.

Record your observations in the submission template.

| Question                                                  | Your observation |
| --------------------------------------------------------- | ---------------- |
| What colour dominates the interface?                      |                  |
| Which colour attracts attention first?                    |                  |
| How are important actions identified?                     |                  |
| Are colours used consistently?                            |                  |
| What is one colour-related improvement you would suggest? |                  |

Reflection checkpoint: Did you evaluate what the colours were communicating, or did you mainly judge whether you liked them?

## 6. Colour theory fundamentals

Colour theory helps you understand how colours relate to each other and how they influence visual communication.

Hue

Which colour family?

Saturation

How vivid or muted?

Lightness

How light or dark?

Traditional art colour theory often uses the RYB model (Red, Yellow, Blue), with Orange, Green, and Purple as secondary colours. Digital screens use RGB (Red, Green, Blue), with Cyan, Magenta, and Yellow as additive secondary colours.

You may also encounter monochromatic, analogous, and complementary colour relationships.

Monochromatic

Variations of one hue

Analogous

Neighbouring hues

Complementary

Opposing hues

## 7. Activity 2 — Experiment in Figma

Estimated time: 15 minutes

1. On your Workshop 03A Figma page, create a frame named `Colour Exploration`.
2. Draw five equal-sized rectangles.
3. Give them the same starting colour.
4. Change the hue of one rectangle.
5. Reduce the saturation of another.
6. Make one rectangle lighter and another darker.
7. Label each swatch to explain the change.

Capture a screenshot and answer:

Which adjustment had the strongest effect on your attention, and how might you use that effect in an interface?

# Part B — Build a professional colour ramp

## 8. What is a colour ramp?

A colour ramp is an organized set of related colours, typically moving from lighter to darker variants.

Professional design systems use ramps to provide colour options for surfaces, borders, headings, buttons, and interactive states.

Here is an example based on NSCC Blue (`#004780`).

### NSCC Blue — Example Colour Ramp

50

\#E6F1FA

100

\#CCE3F5

200

\#99C7EB

300

\#66ABE0

400

\#338FD6

500

\#004780

600

\#003F73

700

\#003060

800

\#00244D

900

\#00172F

950

\#000C1A

The 500 step is the example's base brand colour. These values illustrate a colour ramp; they are not a verified perceptually uniform OKLCH ramp.

The numbers are naming conventions. They do not automatically indicate accessibility or guarantee equal visual differences between shades.

## 9. A brief introduction to OKLCH

Modern CSS supports a colour format called OKLCH.

```
oklch(0.40 0.12 250)
```

Its three components are:

- `L` — Lightness
- `C` — Chroma (colourfulness)
- `H` — Hue

OKLCH can make it easier to build perceptually organized colour ramps than adjusting individual RGB channels.

You do not need to perform colour-space calculations or create a converter in this workshop.

## 10. Activity 3 — Build your ramp in Figma

Estimated time: 15 minutes

1. Create a frame named `NSCC Blue Colour Ramp`.
2. Create eleven equal-sized colour swatches.
3. Apply the eleven HEX values shown above.
4. Label each swatch with its step number and HEX value.
5. Arrange them from lightest to darkest.
6. Examine how the colours might be used in an interface.

Reflection: Why would a professional design system benefit from several shades of one brand colour rather than using the same blue everywhere?

Capture a screenshot.

# Part C — From Figma to CSS design tokens

## 11. Why do we need design tokens?

Imagine you have twenty buttons across a website. If each button uses a separately entered HEX value, updating your brand colour becomes difficult.

Instead, you can define the colour once and reuse it.

A design token is a named value representing a reusable design decision.

We will use two levels:

Foundation tokens describe the actual colours.

Semantic tokens describe what those colours are used for.

\#chatgpt-mermaid-\_r_12b\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_12b\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_12b\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_12b\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_12b\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_12b\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_12b\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_12b\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_12b\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_12b\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_12b\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_12b\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_12b\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_12b\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_12b\_ p{margin:0;}#chatgpt-mermaid-\_r_12b\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_12b\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_12b\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_12b\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_12b\_ .label text,#chatgpt-mermaid-\_r_12b\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_12b\_ .node rect,#chatgpt-mermaid-\_r_12b\_ .node circle,#chatgpt-mermaid-\_r_12b\_ .node ellipse,#chatgpt-mermaid-\_r_12b\_ .node polygon,#chatgpt-mermaid-\_r_12b\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_12b\_ .rough-node .label text,#chatgpt-mermaid-\_r_12b\_ .node .label text,#chatgpt-mermaid-\_r_12b\_ .image-shape .label,#chatgpt-mermaid-\_r_12b\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_12b\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_12b\_ .rough-node .label,#chatgpt-mermaid-\_r_12b\_ .node .label,#chatgpt-mermaid-\_r_12b\_ .image-shape .label,#chatgpt-mermaid-\_r_12b\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_12b\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_12b\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_12b\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_12b\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_12b\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_12b\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_12b\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_12b\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_12b\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_12b\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_12b\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_12b\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_12b\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_12b\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_12b\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_12b\_ .icon-shape,#chatgpt-mermaid-\_r_12b\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_12b\_ .icon-shape p,#chatgpt-mermaid-\_r_12b\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_12b\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_12b\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_12b\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_12b\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_12b\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_12b\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_12b\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_12b\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_12b\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_12b\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_12b\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_12b\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_12b\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_12b\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_12b\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_12b\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_12b\_ .node rect,#chatgpt-mermaid-\_r_12b\_ .node circle,#chatgpt-mermaid-\_r_12b\_ .node ellipse,#chatgpt-mermaid-\_r_12b\_ .node polygon,#chatgpt-mermaid-\_r_12b\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_12b\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_12b\_ .node.mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_12b\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_12b\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_12b\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}Foundation Tokens--blue-500: #004780Semantic Tokens--color-primaryComponentsButton, Card, NavigationFuture Tailwind ThemeReusable utilities

## 12. Activity 4 — Create your CSS project

Estimated time: 20 minutes

Open VS Code and create the following project structure.

```
web-design-project/
├── index.html
├── css/
│   ├── tokens.css
│   ├── base.css
│   └── components.css
└── README.md
```

Create each file using the VS Code Explorer. Make sure that `tokens.css`, `base.css`, and `components.css` are inside the `css` folder.

### Step 1 — Add foundation and semantic tokens

Open `css/tokens.css` and enter:

```
:root {
  color-scheme: light;

  /* Foundation tokens */
  --blue-50: #e6f1fa;
  --blue-100: #cce3f5;
  --blue-200: #99c7eb;
  --blue-500: #004780;
  --blue-600: #003f73;
  --blue-700: #003060;
  --blue-900: #00172f;

  --neutral-white: #ffffff;
  --neutral-dark: #111827;

  /* Semantic tokens */
  --color-background: var(--neutral-white);
  --color-surface: var(--blue-50);
  --color-text: var(--neutral-dark);
  --color-border: var(--blue-200);
  --color-primary: var(--blue-500);
  --color-primary-hover: var(--blue-600);
  --color-on-primary: var(--neutral-white);
}
```

Notice that the semantic token `--color-primary` references `--blue-500`.

If you change the underlying value of `--blue-500`, every component using `--color-primary` can update automatically.

### Step 2 — Add global styles

Open `css/base.css`:

```
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 2rem;
  font-family: system-ui, sans-serif;
  background: var(--color-background);
  color: var(--color-text);
}
```

### Step 3 — Add reusable component styles

Open `css/components.css`:

```
.card {
  max-width: 28rem;
  padding: 1.5rem;
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid var(--color-border);
  border-radius: 0.75rem;
}

.button {
  display: inline-block;
  padding: 0.75rem 1rem;
  background: var(--color-primary);
  color: var(--color-on-primary);
  border: 0;
  border-radius: 0.5rem;
  font: inherit;
  cursor: pointer;
}

.button:hover {
  background: var(--color-primary-hover);
}

.button:focus-visible {
  outline: 3px solid var(--color-primary);
  outline-offset: 3px;
}
```

### Step 4 — Create your HTML

Open `index.html`:

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport"
        content="width=device-width, initial-scale=1">
  <title>Colour System Demo</title>

  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/components.css">
</head>
<body>
  <main class="card">
    <h1>Event Management</h1>
    <p>Explore upcoming events.</p>
    <button class="button" type="button">
      View Events
    </button>
  </main>
</body>
</html>
```

### Step 5 — Run and test

1. Save all files.
2. Right-click `index.html` in VS Code.
3. Select Open with Live Server.
4. Confirm that your browser displays a card with a heading, description, and button.
5. Change `--blue-500` in `tokens.css` to another valid HEX colour.
6. Save the file and observe what changes.
7. Restore the original value.

Checkpoint: You should have a working HTML page whose component colours come from reusable CSS variables.

Reflection: What advantage does changing a colour in one central location provide over editing every button individually?

# Part D — Light and dark themes

## 13. What is a theme?

A theme is a coordinated set of design values.

A light theme may use light backgrounds and dark text. A dark theme typically uses dark surfaces and light text.

The important idea is that components do not need separate hard-coded colour values for each theme.

They can continue using semantic tokens while the theme changes the values of those tokens.

## 14. Activity 5 — Add a dark theme

Estimated time: 15 minutes

At the bottom of `css/tokens.css`, add:

```
[data-theme="dark"] {
  color-scheme: dark;

  --color-background: #0b1220;
  --color-surface: #162235;
  --color-text: #f1f5f9;
  --color-border: #52627a;

  --color-primary: var(--blue-100);
  --color-primary-hover: var(--blue-200);
  --color-on-primary: var(--blue-900);
}
```

Now open `index.html` and change the opening HTML element to:

```
<html lang="en" data-theme="dark">
```

Save the file and view it in your browser.

Your interface should now use the dark theme.

Switch back to the light theme by removing `data-theme="dark"`.

Checkpoint: Confirm that the same HTML and component CSS work in both themes.

LIGHT THEME

Event Management

Explore upcoming events.

View Events

DARK THEME

Event Management

Explore upcoming events.

View Events

These are illustrative previews of the two themes. You should verify your own implementation in the browser.

Reflection: Why might a colour that works well for a light theme need to be replaced or adjusted in a dark theme?

A future workshop may introduce automatic system preference detection with `prefers-color-scheme` and JavaScript-controlled theme selection. You do not need JavaScript for this exercise.

# Part E — Accessibility and testing

## 15. Colour must remain readable

Colour choices must support usability.

Under WCAG 2.x Level AA, normal text generally requires a contrast ratio of at least 4.5:1, while large text requires at least 3:1.

Do not rely on colour alone to communicate important information. Use visible text, labels, and other indicators as appropriate.

## 16. Activity 6 — Test your themes

Estimated time: 15 minutes

Use a contrast checker such as [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).

Test the following colour pairs in both themes:

| Combination                     | Light-theme result | Dark-theme result |
| ------------------------------- | ------------------ | ----------------- |
| Card text / card background     |                    |                   |
| Button text / button background |                    |                   |

Record the contrast ratios and whether each combination passes the applicable WCAG AA text requirement.

If a combination fails, adjust your CSS token values, test again, and document the change.

Reflection: Did accessibility testing cause you to change a colour that initially looked acceptable?

# Part F — Preparing for future CSS frameworks

## 17. How does this connect to Tailwind CSS?

In PROG 2700, you may work with frameworks such as Tailwind CSS to build interactive applications.

Tailwind CSS v4 supports theme variables, which can connect your existing design-token approach to reusable utility classes.

For example, a future project could map your semantic CSS variables into a Tailwind theme:

```
@import "tailwindcss";

@theme inline {
  --color-brand: var(--color-primary);
  --color-page: var(--color-background);
  --color-panel: var(--color-surface);
  --color-content: var(--color-text);
}
```

You could then use classes such as:

```
<main class="bg-page text-content">
  <article class="bg-panel p-6 rounded-xl">
    <h1>Event Management</h1>
  </article>
</main>
```

This is an example of future framework integration, not a complete Tailwind project setup.

You are not required to install Tailwind in Workshop 03A.

The important lesson is that well-organized CSS design decisions can be reused when your project grows or adopts a framework.

# Part G — Integrated project connection

## 18. Activity 7 — Plan your application's colour system

Estimated time: 10 minutes

Return to your shared Figma workspace.

Create a frame named:

`Integrated Project — Colour Exploration V1`

Choose a possible primary colour for your integrated application and create a small set of related lighter and darker colours.

Identify possible uses for:

- Primary actions
- Backgrounds or surfaces
- Headings and text
- Borders or separators

You are not expected to finalize the palette yet.

Record your answers:

1. What is the purpose of your application?
2. Who will use it?
3. What should its visual identity communicate?
4. How could a consistent colour system help your team?

Capture a screenshot.

# Part H — Individual reflection

## 19. Reflect on your learning

Complete these questions individually in your Student Submission Template.

1. Before this workshop, how did you normally choose colours for a website?
2. What is the difference between choosing a colour and creating a colour system?
3. What did building a colour ramp teach you?
4. Why is it useful to separate foundation tokens from semantic tokens?
5. What happened when you switched your CSS between light and dark themes?
6. What did contrast testing reveal about your colour choices?
7. How could this approach help you maintain a consistent interface in your integrated project?

Your answers should explain your own observations and decisions, not simply repeat definitions.

# Part I — Workshop completion and submission

## 20. Final checkpoint

Student completion checklist

0 of 12

Shared my Figma workspace with davis.boudreau\@nscc.ca

Completed the colour observation activity

Explored colour properties in Figma

Created and labelled the NSCC blue colour ramp

Created tokens.css, base.css, and components.css

Ran the HTML/CSS project with Live Server

Tested both light and dark themes

Checked text contrast in both themes

Created an integrated-project colour exploration

Committed and pushed my technical evidence to GitHub

Completed my individual reflection

Included Figma and GitHub links in my submission

## 21. Student deliverables

Follow the course's standard workflow:

Complete Workshop → Complete Worksheet → Complete Reflection → Commit/Push Technical Evidence → Submit Worksheet to Brightspace

Your submission must include your completed Student Submission Template, relevant screenshots, a working Figma link, and a GitHub repository link containing your HTML/CSS implementation.

Your Figma workspace must remain shared with davis.boudreau\@nscc.ca so that your instructor can inspect your work.

The workshop instruction document itself is not submitted.

## 22. Workshop complete

You have moved from choosing colours based on appearance to creating an organized colour system that can be implemented in CSS, tested for accessibility, and reused across components.

The professional practice you are developing is:

Design → Define Tokens → Implement → Test → Reflect → Refine

### Next — Workshop 03B: Typography

You will apply a similar process to typography: font families, type scales, line height, spacing, readable text, and reusable CSS typography tokens.

Together, Workshops 03A and 03B will provide the foundations for your future interface style guide and integrated full-stack application.