# Editorial design system

Design the pack as a concise editorial document, not a dashboard or developer portal.

## Start with a visual thesis

- Let the first screen state one memorable conclusion in large display type.
- Pair it with one short explanation and the decision/status metadata.
- Make the navigation titles read as a complete outline of the argument.
- Use a large headline only once; subsequent slides should begin directly with their content.

## Use typography as the hierarchy

- Use a serif face for thesis statements, major section titles, and consequential numbers.
- Use a neutral sans serif for prose, labels, and navigation.
- Use monospace only for commands, code signatures, file paths, identifiers, and raw evidence.
- Keep body copy between roughly 55 and 75 characters per line.
- Prefer a short paragraph and a diagram to a wall of bullets.

## Use a restrained palette

- Use warm paper and near-black ink as the base.
- Choose one accent for navigation, numbering, and emphasis.
- Reserve green for verified improvement or pass, red for failure or before, and amber for caution or an open decision.
- Do not assign colors to categories unless the distinction recurs enough for the reader to learn it.

## Compose relationships, not card collections

Choose the smallest visual that exposes the relationship:

- **Metric strip:** three to five consequential quantities with labels and denominators.
- **Before/after:** one behavior per comparison, aligned so the eye can diff it.
- **Flow:** three or more dependent steps with arrows and an explicit outcome.
- **Ownership map:** one hub connected to distinct collaborators or responsibilities.
- **Timeline:** phases with proof or exit criteria, not a list of dates.
- **Evidence panel:** one assertion, one provenance line, one captured artifact.
- **Quote:** only when the original wording is itself important.

Use borders to define a real unit. If several cards could be reordered without changing the meaning, consider a numbered list with rules instead.

## Make diagrams self-explanatory

- Draw connectors before nodes so boxes cover arrow ends cleanly.
- Label lines, axes, and nodes directly.
- Use real component, team, or method names.
- Keep the same node positions in before/after diagrams.
- Put the conclusion beside the visual rather than making the reviewer decode it.
- Remove decorative legends, gradients, shadows, and icons that do not carry information.

## Design for reading at two speeds

At scan speed, the reader should get the thesis from navigation, headings, numbers, and callouts. At inspection speed, they should be able to trace every claim to evidence and sources.

Use progressive disclosure:

1. Headline assertion.
2. One-sentence implication.
3. Visual or comparison.
4. Evidence and provenance.
5. Caveat or next action.

## Make mobile a first-class layout

- Convert the side index to a horizontally scrollable top index.
- Collapse multi-column grids to one column.
- Let tables scroll horizontally without shrinking text below readability.
- Keep the active navigation item visible.
- Preserve a visible next action at the end of the slide.
- Avoid fixed-width diagrams; use a viewBox and `max-width: 100%`.

## Final visual edit

Remove anything that is merely decorative, repetitive, or self-congratulatory. Tighten copy before shrinking type. A polished pack feels confident because the hierarchy is clear, not because every surface is styled.
