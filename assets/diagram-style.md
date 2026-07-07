# Diagram style for eval packs

The SVG design system for every diagram in an eval pack: the Map slide and the
architecture before/after slides. Follow it so diagrams across packs read as one
system.

Eval packs use **inline SVG only** — no HTML shell, no Google Fonts (use a generic
`monospace` stack), no export toolbar, no CDN scripts. Those would break the pack's
one-file offline rule. (Provenance: see the Credit section of the repo README.)

## Canvas

- Background: `#020617` (slate-950) rect with `rx="8"`, covering the whole viewBox.
  Keep it even though the deck has its own theme — the dark panel makes the diagram
  self-contained on both light and dark deck themes.
- Subtle grid pattern on top of the background:

```svg
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
  <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.5"/>
</pattern>
```

- Typography: `font-family="ui-monospace, Menlo, monospace"` on the root `<svg>`.
  Sizes: 12px component names, 9px sublabels, 8px annotations.
- Wrap each `<svg>` in the template's `<div class="diagram">` panel.

## Component colors (semantic, by type)

| Component type | Fill (rgba) | Stroke |
|---------------|-------------|--------|
| Frontend | `rgba(8, 51, 68, 0.4)` | `#22d3ee` (cyan-400) |
| Backend | `rgba(6, 78, 59, 0.4)` | `#34d399` (emerald-400) |
| Database | `rgba(76, 29, 149, 0.4)` | `#a78bfa` (violet-400) |
| Cloud / infra | `rgba(120, 53, 15, 0.3)` | `#fbbf24` (amber-400) |
| Security | `rgba(136, 19, 55, 0.4)` | `#fb7185` (rose-400) |
| Message bus | `rgba(251, 146, 60, 0.3)` | `#fb923c` (orange-400) |
| External / generic | `rgba(30, 41, 59, 0.5)` | `#94a3b8` (slate-400) |

## Before/after highlight colors (semantic, by change)

In architecture before/after slides, color encodes **the change**, not the component
type — the reviewer's eye should land on red in the *before* graph and green in the
*after* graph:

| Role | Fill (rgba) | Stroke | Label color |
|------|-------------|--------|-------------|
| Problem node (before) | `rgba(127, 29, 29, 0.4)` | `#f87171` (red-400) | `#fca5a5` |
| New seam (after) | `rgba(6, 78, 59, 0.4)` | `#34d399` (emerald-400) | `#6ee7b7` |
| Unchanged | `rgba(51, 65, 85, 0.35)` | `#64748b` (slate-500) | `white` |

Draw the same graph twice with the same layout where possible, so the reviewer can
diff the two pictures by eye.

## Boxes, arrows, z-order

Component boxes are rounded rects (`rx="6"`) with 1.5px stroke and semi-transparent
fill:

```svg
<rect x="X" y="Y" width="W" height="H" rx="6" fill="FILL" stroke="STROKE" stroke-width="1.5"/>
<text x="CENTER_X" y="Y+20" fill="white" font-size="11" font-weight="600" text-anchor="middle">LABEL</text>
<text x="CENTER_X" y="Y+36" fill="#94a3b8" font-size="9" text-anchor="middle">sublabel</text>
```

Arrowheads via SVG marker (give the marker a unique id per `<svg>` — ids are global
across the whole HTML document, and a pack has several diagrams):

```svg
<marker id="arrow-UNIQUE" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
  <polygon points="0 0, 10 3.5, 0 7" fill="#64748b"/>
</marker>
```

- **Arrows first.** Draw connection lines right after the background/grid so boxes
  painted later cover them. SVG paints in document order.
- **Mask arrows behind transparent fills.** Semi-transparent fills let arrows show
  through; under each styled rect, draw an opaque rect first:

```svg
<rect x="X" y="Y" width="W" height="H" rx="6" fill="#0f172a"/>
<rect x="X" y="Y" width="W" height="H" rx="6" fill="rgba(76, 29, 149, 0.4)" stroke="#a78bfa" stroke-width="1.5"/>
```

- Dashed lines mean indirect relationships: auth/security flows in rose `#fb7185`;
  grouping boundaries with `stroke-dasharray="4,4"` (security groups, rose) or
  `stroke-dasharray="8,4"` (regions/clusters, amber, `rx="12"`).

## Spacing and legends

- Standard component height 60px (80–120px for large components); **minimum 40px
  vertical gap** between stacked components. Inline connectors (message buses) go in
  the gap, never overlapping a box.
- Legends go **outside** every boundary box: find the lowest boundary edge, place the
  legend at least 20px below it, and extend the viewBox height to fit.
