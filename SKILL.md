---
name: eval-pack
description: Create a polished, self-contained HTML explainer or review pack for a pull request, completed feature, paper, research topic, strategy, or technical concept. Use when the user asks for an eval pack, evaluation pack, review pack, visual explainer, evidence pack, paper explainer, architecture walkthrough, or a concise way to understand and verify substantial work. Produce an executive-summary-first narrative with editorial typography, diagrams, citations, screenshots, and real evidence; work offline, support mobile, and make every important claim inspectable.
---

# Eval Pack

Create one self-contained HTML page that lets a busy reviewer understand the argument, inspect the evidence, and decide what to do next without reconstructing the work from diffs, papers, or terminal history.

## Core contract

1. **Lead with the answer.** State the conclusion, recommendation, or ship verdict before the supporting detail.
2. **Make the narrative inspectable.** Back implementation claims with captured artifacts and research claims with direct source links.
3. **Design for the reader.** Use plain-language action titles, visible hierarchy, and only the detail needed for the decision.
4. **Separate evidence from interpretation.** Say what the artifact establishes, then what you infer from it.
5. **Be honest about uncertainty.** Surface limitations, conflicting evidence, and unverified paths.

## 1. Frame the pack before building

Write a five-line brief:

- **Mode:** change/PR, paper/research, or topic/strategy.
- **Reader:** the specific person or role reviewing it.
- **Decision:** what they should be able to approve, reject, believe, or do.
- **Thesis:** one sentence that remains true if the reader stops after the first slide.
- **Evidence:** the smallest set of artifacts or sources needed to support it.

Read [references/content-modes.md](references/content-modes.md) for the selected mode. Read [references/editorial-design.md](references/editorial-design.md) for every pack. For system or architecture diagrams, also read [assets/diagram-style.md](assets/diagram-style.md).

Do not start by filling the template. First decide the argument and remove any slide that does not advance it.

## 2. Gather evidence before writing HTML

Build a claim-to-evidence list. Every major claim must point to something the reviewer can inspect.

For code and product changes:

- Run the real test or build command and retain the unedited summary.
- Exercise the actual user flow when possible; capture screenshots or short recordings of meaningful states.
- Capture before and after behavior for a bug fix or migration when a safe base-commit checkout can reproduce it.
- Derive architecture diagrams from real imports, call sites, schemas, or traces rather than memory.
- Inspect every captured image for errors, empty states, wrong values, overflow, or accidental sensitive data.

For papers and topics:

- Read the primary source, not only an abstract or secondary summary.
- Link directly to the paper, dataset, repository, talk, or post.
- Record the population, comparison, metric, result, and limitation behind every quantitative claim.
- Distinguish the authors' finding from your interpretation or recommendation.
- Use short excerpts only when wording matters; prefer accurate paraphrase.

Never fabricate, reconstruct, or beautify evidence. If evidence cannot be captured, record that as a limitation.

## 3. Build the narrative pyramid

Order information from decision to detail:

1. Executive summary and bottom line.
2. The few claims or changes that determine the decision.
3. The operating model, causal map, comparison, or architecture that connects them.
4. Direct evidence and implementation detail.
5. Decisions, limitations, open questions, and sources.

Use assertion titles: “The model-only baseline wins on routine work,” not “Results.” A reader scanning only the navigation and headings should understand the story.

Keep one idea per slide. Merge overlapping slides. Prefer one decisive visual over three repetitive screenshots.

## 4. Build from the template

Copy [assets/template.html](assets/template.html) and replace or remove every `REPLACE` block. Preserve its landmarks, navigation, responsive behavior, visual tokens, and end-of-slide next buttons.

Use the template's visual grammar consistently:

- Display serif for thesis and section statements; sans serif for explanation; monospace only for evidence and identifiers.
- Warm paper, ink, rules, and one accent for structure; reserve red, green, and amber for meaning.
- Numbered navigation, generous whitespace, strong rules, and a small set of repeated components.
- Connected flows for sequences, before/after cards for change, metric strips for quantities, and evidence panels for proof.
- Cards only when the border communicates a unit or relationship; avoid dashboard-style card soup.
- Label axes directly on charts and put the meaning next to the line or point when possible.
- Use real names in diagrams and direct labels instead of decorative icons.

Do not create a second hero above every slide. Navigation should switch directly to the selected content, and every slide should end with a clear next action.

## 5. Preserve evidence fidelity

Use one evidence shell for terminal output, code signatures, source excerpts, and measurements:

- Give every block a short assertion header.
- Include a source, command, file, line, or run identifier.
- Keep raw output intact; trim with an explicit ellipsis rather than rewriting.
- Show failure states in red and passing states in green only when those colors represent actual outcomes.
- Put a score beside its denominator, run count, comparison, and uncertainty when available.

For decisions, show the choice, alternative, tradeoff, reversibility, and owner. Do not bury judgment calls inside implementation slides.

## 6. Make the file portable

- Keep all CSS and JavaScript inline.
- Embed images and GIFs as `data:` URIs with `python3 scripts/embed_media.py <pack.html>`.
- Use inline SVG for diagrams; do not load Mermaid, fonts, icons, or scripts from a CDN.
- Downscale screenshots to at most 1200px wide, keep GIFs short, and aim for less than 15 MB.
- Save to `docs/eval-packs/<yyyy-mm-dd>-<topic>.html` unless the user requests another path.
- Include useful alt text and visible focus states.

## 7. Validate the pack itself

Run:

```sh
python3 scripts/embed_media.py <pack.html>
python3 scripts/validate_pack.py <pack.html>
```

Then serve the file locally and inspect every slide in a real browser:

- Navigate with the index, keyboard, floating pager, and end-of-slide next button.
- Check desktop and mobile widths.
- Confirm headings, diagrams, tables, and evidence blocks do not overflow.
- Confirm every link, source, image, and cross-reference resolves.
- Check light and dark modes when both are retained.
- Fix and repeat after any programmatic HTML edit.

Do not claim browser verification if the environment cannot perform it. Report the nearest validation performed and the gap.

## 8. Hand off clearly

Return the exact file path, the pack's mode and decision, the validation commands run, and any unresolved limitation. On macOS, offer to open the file.

## Honesty

Treat the pack as a review instrument, not a sales brochure. Show failing tests, mixed results, partial work, and contradictory sources plainly. Trust is the product.

See the repository README for concept and design-system credits.
