# Diagram style for eval packs

The SVG design system for every diagram in an eval pack: the Map slide and the
architecture before/after slides. Follow it so diagrams across packs read as one
system.

Eval packs use **inline SVG only** — no HTML shell, no Google Fonts (use a generic
`monospace` stack), no export toolbar, no CDN scripts. Those would break the pack's
one-file offline rule. (Provenance: see the Credit section of the repo README.)

## Theme-adaptive, not dark

Diagrams inherit the deck's theme instead of carrying their own dark canvas. Inline
SVG lives in the document, so CSS variables cascade into it — use `var(--…)` for
every fill and stroke and the diagram automatically matches both light and dark
deck themes:

- **No background rect and no grid pattern.** The template's `<div class="diagram">`
  panel supplies the surface.
- Typography: `font-family="ui-monospace, Menlo, monospace"` on the root `<svg>`.
  Sizes: 12px component names, 9px sublabels, ~10px annotations.
- Keep diagrams inside the slide's content width (viewBox width ≤ ~760).

## Colors encode the change, not the tech stack

Use three roles. The reviewer's eye should land on red in a *before* graph and
green in an *after* graph:

| Role | Fill | Stroke | Label fill |
|------|------|--------|------------|
| Problem node (before) | `var(--fail-bg)` | `var(--fail)` | `var(--fail)` |
| New seam (after) | `var(--pass-bg)` | `var(--pass)` | `var(--pass)` |
| Unchanged | `var(--bg)` | `var(--line)` | `var(--ink)` |

Sublabels are always `var(--muted)`. If a diagram genuinely needs more distinctions,
`var(--warn*)` and `var(--accent)` are available — but if you're reaching for a
fourth color, the diagram is probably doing too much.

Draw the same graph twice with the same layout where possible, so the reviewer can
diff the two pictures by eye. Collapse parallel same-role nodes into one box with a
`·`-separated label (`chat_v1 · chat_streaming · resample`) — fewer boxes beats
more precision.

## Boxes and arrows

Component boxes are rounded rects (`rx="6"`) with 1.4px stroke:

```svg
<rect x="X" y="Y" width="W" height="H" rx="6" fill="var(--bg)" stroke="var(--line)" stroke-width="1.4"/>
<text x="CENTER_X" y="Y+21" fill="var(--ink)" font-size="12" font-weight="600" text-anchor="middle">LABEL</text>
<text x="CENTER_X" y="Y+38" fill="var(--muted)" font-size="9" text-anchor="middle">sublabel</text>
```

Arrows are `var(--muted)`, drawn **before** the boxes (SVG paints in document order,
and fills are opaque, so boxes cover arrow ends cleanly). Dashed
(`stroke-dasharray="4,4"`) means indirect — deferred, fallback, "binds to".
Arrowheads via marker; give the marker a **unique id per `<svg>`** — ids are global
across the whole HTML document, and a pack has several diagrams:

```svg
<marker id="arrow-UNIQUE" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
  <polygon points="0 0, 10 3.5, 0 7" fill="var(--muted)"/>
</marker>
```

After drawing, sanity-check every sublabel fits its box: ~5.4px per character at
9px monospace. Shorten the label rather than widening the diagram.

## Spacing and legends

- Component height ~44–52px; **minimum 28px vertical gap** between rows of boxes.
- Prefer labeling roles directly on the boxes over a legend. If a legend is
  unavoidable, place it below everything with at least 20px clearance and extend
  the viewBox to fit.
