# Building a HEX → OKLCH Converter

## HTML

```html
<input
    id="hexInput"
    value="#004780"
>

<button onclick="convertColor()">
    Convert
</button>

<pre id="output"></pre>
```

## HEX → RGB

```javascript
function hexToRgb(hex){

    hex = hex.replace("#","");

    return {

        r: parseInt(hex.substring(0,2),16),
        g: parseInt(hex.substring(2,4),16),
        b: parseInt(hex.substring(4,6),16)

    };

}
```

## RGB → OKLab

```javascript
function rgbToOklab(r,g,b){

    r/=255;
    g/=255;
    b/=255;

    const linear = c =>
        c <= 0.04045
            ? c / 12.92
            : Math.pow(
                (c + 0.055)/1.055,
                2.4
            );

    r = linear(r);
    g = linear(g);
    b = linear(b);

    const l =
        0.4122214708*r +
        0.5363325363*g +
        0.0514459929*b;

    const m =
        0.2119034982*r +
        0.6806995451*g +
        0.1073969566*b;

    const s =
        0.0883024619*r +
        0.2817188376*g +
        0.6299787005*b;

    const l3 = Math.cbrt(l);
    const m3 = Math.cbrt(m);
    const s3 = Math.cbrt(s);

    return {

        L:
            0.2104542553*l3 +
            0.7936177850*m3 -
            0.0040720468*s3,

        a:
            1.9779984951*l3 -
            2.4285922050*m3 +
            0.4505937099*s3,

        b:
            0.0259040371*l3 +
            0.7827717662*m3 -
            0.8086757660*s3

    };

}
```

## OKLab → OKLCH

```javascript
function oklabToOklch(L,a,b){

    const C =
        Math.sqrt(a*a + b*b);

    let H =
        Math.atan2(b,a) *
        180 /
        Math.PI;

    if(H < 0)
        H += 360;

    return {L,C,H};

}
```

## Conversion Function

```javascript
function convertColor(){

    const hex =
        document
            .getElementById("hexInput")
            .value;

    const rgb =
        hexToRgb(hex);

    const lab =
        rgbToOklab(
            rgb.r,
            rgb.g,
            rgb.b
        );

    const oklch =
        oklabToOklch(
            lab.L,
            lab.a,
            lab.b
        );

    document
        .getElementById("output")
        .textContent =

`OKLCH:
L = ${oklch.L.toFixed(4)}
C = ${oklch.C.toFixed(4)}
H = ${oklch.H.toFixed(2)}

CSS:
oklch(
${oklch.L.toFixed(4)}
${oklch.C.toFixed(4)}
${oklch.H.toFixed(2)}
)`;

}
```

---

# Automatic Ramp Generator

Once you have:

```text
Base Lightness
Base Chroma
Base Hue
```

build the ramp with:

```javascript
const rampSteps = {

  50:0.96,
  100:0.90,
  200:0.80,
  300:0.70,
  400:0.55,

  500:base.L,

  600:0.35,
  700:0.28,
  800:0.22,
  900:0.15,
  950:0.10

};
```

Each generated color uses:

```javascript
oklch(
    targetLightness,
    adjustedChroma,
    originalHue
);
```

---

# Interactive Color Ramp Demo

A complete educational tool should display:

```text
Input HEX

↓

Convert to OKLCH

↓

Generate Ramp

↓

Display Swatches

↓

Generate CSS Variables

↓

Copy Tokens
```

Example output:

```text
50   ███████████
100  ███████████
200  ███████████
300  ███████████
400  ███████████
500  ███████████
600  ███████████
700  ███████████
800  ███████████
900  ███████████
950  ███████████
```

---

# Accessibility Checklist

Verify:

```text
✓ Text Contrast
✓ Buttons
✓ Links
✓ Navigation
✓ Forms
✓ Dark Mode
✓ Focus States
```

Minimum ratios:

```text
Normal Text  4.5:1
Large Text   3:1
```

---

# Final Project

By the end of this exercise, students should have a single-page Color System Generator featuring:

✅ HEX input

✅ HEX → OKLCH conversion

✅ OKLCH display

✅ Ramp generation

✅ CSS variable generation

✅ Swatch preview

✅ Copy CSS button

✅ Theme toggle

✅ Light mode

✅ Dark mode

✅ WCAG validation

✅ Design-token export

This workflow mirrors the process used by modern design-system teams to transform a single brand color into a scalable, accessible, production-ready color system.