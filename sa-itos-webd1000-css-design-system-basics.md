# Creating Professional Color Ramps with OKLCH, CSS, Theme Toggling, and an Interactive Color Tool

## Overview

Modern design systems such as Tailwind CSS, Fluent UI, Material Design, and Adobe Spectrum rarely rely on a single brand color. Instead, they create a **color ramp**: a carefully structured collection of lighter and darker variants that support backgrounds, cards, borders, typography, buttons, hover states, dark mode, and accessibility.

In this tutorial, we will use the NSCC brand color:

```text
NSCC Blue
#004780
```

and transform it into a professional design-system palette.

By the end of this tutorial, you will be able to:

- Understand color ramps
- Understand OKLCH color space
- Generate lighter and darker shades
- Build CSS design tokens
- Implement light and dark themes
- Build a HEX-to-OKLCH converter
- Generate color ramps programmatically
- Create an interactive color-system tool

---

# Learning Objectives

After completing this tutorial you should be able to:

✅ Explain why color ramps exist

✅ Describe the components of OKLCH

✅ Create lighter and darker shades of a brand color

✅ Generate design tokens

✅ Create reusable CSS variables

✅ Build dark mode support

✅ Create a theme switcher

✅ Convert HEX values to OKLCH

✅ Generate automated color ramps

---

# Why Color Ramps Exist

Many beginner projects use only a single brand color:

```css
#004780
```

Real-world interfaces require much more.

Consider a typical application:

```text
Backgrounds
Cards
Borders
Buttons
Forms
Navigation
Alerts
Typography
Dark Mode
```

A single color cannot satisfy all these requirements.

Instead, modern design systems create a family of related colors:

```text
50
100
200
300
400
500
600
700
800
900
950
```

---

# Understanding the Scale

The middle value represents the original brand color:

```text
500 = Base Color
```

Everything above becomes lighter.

Everything below becomes darker.

```text
50   Very Light
100
200
300
400

500  Original Color

600
700
800
900
950  Very Dark
```

This convention is used extensively in modern design systems.

---

# Practical Usage of a Color Ramp

A common mapping looks like:

```text
50   Page Backgrounds

100  Panels

200  Borders

300  Disabled States

400  Secondary Components

500  Brand Color

600  Hover States

700  Active States

800  Navigation

900  Headings

950  Darkest Surfaces
```

---

# Why RGB Is Not Ideal

Many developers try to build ramps using RGB.

Example:

```css
rgb(0, 71, 128)
```

The problem:

```text
RGB describes devices.

Humans perceive color differently.
```

Equal RGB changes rarely appear visually equal.

This often results in:

```text
Uneven transitions

Muddy shadows

Oversaturated highlights
```

Modern design systems increasingly use:

```text
HSL
LAB
OKLCH
```

---

# What Is OKLCH?

OKLCH is a perceptual color space designed to align more closely with how humans see color.

Syntax:

```css
oklch(L C H)
```

Where:

```text
L = Lightness

C = Chroma

H = Hue
```

Think of it as:

```text
L = How bright?

C = How colorful?

H = What color?
```

Example:

```css
oklch(
    0.40
    0.12
    250
)
```

Meaning:

```text
40% lightness

Moderate color intensity

Blue hue
```

---

# Step 1: Choose a Brand Color

For this tutorial:

```css
#004780
```

Assign it to:

```text
500
```

```css
--nscc-blue-500: #004780;
```

This becomes the anchor for the entire palette.

---

# Step 2: Convert the Color to OKLCH

Approximate representation:

```css
oklch(
    0.40
    0.12
    250
)
```

Meaning:

```text
L = 0.40

C = 0.12

H = 250°
```

These three values become the basis for the entire ramp.

---

# Step 3: Preserve the Hue

Hue defines the color identity.

Our brand blue has a hue of approximately:

```text
250°
```

Every generated shade should stay near that value.

Good:

```text
Blue
↓
Blue
↓
Blue
```

Bad:

```text
Blue
↓
Purple
↓
Green
```

Maintaining hue consistency preserves brand recognition.

---

# Step 4: Create Lighter Shades

Generate:

```text
50
100
200
300
400
```

For lighter shades:

```text
Increase Lightness

Reduce Chroma Slightly
```

Example:

```css
50  = oklch(0.96 0.01 250)

100 = oklch(0.90 0.02 250)

200 = oklch(0.80 0.04 250)

300 = oklch(0.70 0.06 250)

400 = oklch(0.55 0.09 250)
```

Result:

```text
More light

Less saturation

Same hue
```

---

# Step 5: Create Darker Shades

Generate:

```text
600
700
800
900
950
```

For darker shades:

```text
Decrease Lightness

Maintain Chroma
```

Example:

```css
600 = oklch(0.35 0.12 250)

700 = oklch(0.28 0.13 250)

800 = oklch(0.22 0.13 250)

900 = oklch(0.15 0.12 250)

950 = oklch(0.10 0.08 250)
```

---

# Why Professional Ramps Are Non-Linear

Beginners often use equal spacing:

```text
0.10
0.20
0.30
0.40
0.50
```

Human vision does not perceive brightness evenly.

Professional ramps use larger jumps toward the extremes:

```text
50  = 0.96

100 = 0.90

200 = 0.80

300 = 0.70

400 = 0.55

500 = 0.40

600 = 0.35

700 = 0.28

800 = 0.22

900 = 0.15

950 = 0.10
```

Notice:

```text
Large jumps near white

Small jumps near the base color

Large jumps near black
```

This produces visually balanced spacing.

---

# Final NSCC Blue Ramp

```css
:root {

  --nscc-blue-50:  #E6F1FA;

  --nscc-blue-100: #CCE3F5;

  --nscc-blue-200: #99C7EB;

  --nscc-blue-300: #66ABE0;

  --nscc-blue-400: #338FD6;

  --nscc-blue-500: #004780;

  --nscc-blue-600: #003F73;

  --nscc-blue-700: #003060;

  --nscc-blue-800: #00244D;

  --nscc-blue-900: #00172F;

  --nscc-blue-950: #000C1A;

}
```

---

# Implementing the Palette

## Buttons

```css
.btn-primary {

  background:
      var(--nscc-blue-500);

  color:
      white;

}

.btn-primary:hover {

  background:
      var(--nscc-blue-600);

}

.btn-primary:active {

  background:
      var(--nscc-blue-700);

}
```

---

## Cards

```css
.card {

  background:
      var(--nscc-blue-50);

  border:
      1px solid
      var(--nscc-blue-200);

}
```

---

## Headings

```css
h1,
h2,
h3 {

  color:
      var(--nscc-blue-900);

}
```

---

# Creating a Theme Toggle

Modern applications commonly offer:

```text
Light Mode

Dark Mode

System Mode
```

---

## Theme Toggle HTML

```html
<select id="themeSelector">

  <option value="system">

    System

  </option>

  <option value="light">

    Light

  </option>

  <option value="dark">

    Dark

  </option>

</select>
```

---

## Theme Variables

```css
:root {

  --bg:
      white;

  --text:
      #00172F;

}

[data-theme="dark"] {

  --bg:
      #000C1A;

  --text:
      #E6F1FA;

}
```

---

## Theme Toggle Logic

```javascript
const selector =
document.getElementById(
    "themeSelector"
);

selector.addEventListener(

  "change",

  event => {

    const theme =
      event.target.value;

    if (
      theme === "system"
    ) {

      document.documentElement
        .removeAttribute(
          "data-theme"
        );

      return;

    }

    document.documentElement
      .setAttribute(
        "data-theme",
        theme
      );

});
```

---

# Building a HEX → OKLCH Converter

The conversion workflow looks like:

```text
HEX

↓

RGB

↓

OKLab

↓

OKLCH
```

Input:

```text
#004780
```

Output:

```text
L = 0.40

C = 0.12

H = 250°
```

---

# HEX to RGB

```javascript
function hexToRgb(hex){

    hex =
      hex.replace("#","");

    return {

        r:
          parseInt(
            hex.substring(0,2),
            16
          ),

        g:
          parseInt(
            hex.substring(2,4),
            16
          ),

        b:
          parseInt(
            hex.substring(4,6),
            16
          )

    };

}
```

---

# RGB to OKLab

```javascript
function rgbToOklab(
    r,
    g,
    b
){

    // Conversion code

}
```

The complete algorithm converts device-space RGB values into perceptual OKLab coordinates.

---

# OKLab to OKLCH

```javascript
function oklabToOklch(
    L,
    a,
    b
){

    const C =
      Math.sqrt(
        a*a +
        b*b
      );

    let H =
      Math.atan2(
        b,
        a
      ) *
      180 /
      Math.PI;

    if(H < 0){

      H += 360;

    }

    return {

      L,
      C,
      H

    };

}
```

---

# Automatic Ramp Generation

Once we determine:

```text
Lightness

Chroma

Hue
```

we can produce an entire ramp.

Example template:

```javascript
const rampSteps = {

  50 : 0.96,

  100: 0.90,

  200: 0.80,

  300: 0.70,

  400: 0.55,

  500: base.L,

  600: 0.35,

  700: 0.28,

  800: 0.22,

  900: 0.15,

  950: 0.10

};
```

Each color is generated by applying:

```javascript
oklch(
    targetLightness,
    adjustedChroma,
    originalHue
)
```

---

# Interactive Color System Tool

A complete educational application should implement:

```text
HEX Input

↓

Convert to OKLCH

↓

Generate Color Ramp

↓

Display Swatches

↓

Generate CSS Variables

↓

Copy Design Tokens

↓

Switch Themes
```

---

# Example Ramp Output

```text
50   ██████████

100  ██████████

200  ██████████

300  ██████████

400  ██████████

500  ██████████

600  ██████████

700  ██████████

800  ██████████

900  ██████████

950  ██████████
```

---

# Accessibility Checklist

Always verify:

```text
✓ Text Contrast

✓ Buttons

✓ Links

✓ Forms

✓ Navigation

✓ Dark Mode

✓ Focus States
```

Recommended WCAG ratios:

```text
Normal Text

4.5 : 1

Large Text

3 : 1
```

---

# Final Project Challenge

Create a full-featured Color System Generator that includes:

## Core Features

✅ HEX Input

✅ HEX → OKLCH Conversion

✅ Automatic Ramp Generation

✅ Swatch Preview

✅ CSS Variable Export

✅ Copy to Clipboard

✅ Theme Switching

✅ Light Mode

✅ Dark Mode

---

## Advanced Features

✅ WCAG Contrast Checker

✅ JSON Token Export

✅ SCSS Token Export

✅ Tailwind Token Export

✅ Live Button Preview

✅ Live Card Preview

✅ Navigation Demo

✅ Dark Mode Demo

---

# Summary

Modern color systems are built around a repeatable workflow:

```text
Choose a Brand Color

↓

Convert to OKLCH

↓

Assign as 500

↓

Generate Light Tints

↓

Generate Dark Shades

↓

Preserve Hue

↓

Adjust Chroma

↓

Validate Accessibility

↓

Generate Design Tokens

↓

Implement Themes
```

## Key Takeaway

> A professional color ramp is not simply a gradient between white and black. It is a carefully engineered progression of lightness, chroma, and hue that creates visually balanced, accessible, and scalable user interfaces. By combining OKLCH, CSS design tokens, dark-mode support, and automated tooling, developers can transform a single brand color into a complete design system.