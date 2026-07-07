---
name: eval-pack
description: Build an evaluation pack — a single self-contained HTML slide deck (left-hand index navigation) with diagrams, before/after architecture graphs, screenshots, animated GIFs, and real captured test output that proves completed work actually runs, so a human can review an hour of agent work in a few minutes. Use whenever the user says "eval pack", "evaluation pack", "review pack", "make this reviewable", "show me what you did", "prove it works", asks you to walk through your architectural changes (before/after), or asks how to review or verify a completed piece of work — and offer one proactively after finishing any substantial feature, refactor, bugfix, or multi-file change.
---

# Eval Pack

An eval pack is a curated, single-file HTML slide deck that lets a human review a large chunk of agent work in two or three minutes instead of fifteen minutes of digging through diffs and terminal scrollback. The reviewer clicks through slides with a left-hand index; each slide states what was done and shows captured proof that it works.

The pack has a second job that is just as important as the first: it is a **verification forcing function**. You cannot screenshot a feature that doesn't run, and you cannot paste passing test output from a suite that fails. Building the pack honestly forces you to exercise your own work end to end — and much of the pack's value comes from the bugs you find and fix while capturing evidence.

## The golden rule: evidence, not claims

Every claim in the pack is backed by an artifact you captured by actually running the thing. "Implemented X" is a claim; the screenshot, GIF, or terminal transcript of X working is evidence. Never fabricate, hand-edit, or reconstruct evidence from memory — a single faked artifact destroys the trust that makes every future pack useful. If you cannot capture evidence for something, that is itself a finding: it goes on the Limitations slide, stated plainly.

## The second rule: write for the reviewer, not the implementer

The reviewer wasn't there while the work happened. Assume they know the product but not the codebase internals, and none of the shorthand from your session. Evidence proves the work runs; plain language is what lets the reviewer understand *what* they're approving:

- **Name every change by its visible behavior, stated before → after.** "Subscribers on retired plans now keep their plan instead of being dropped to free" — not "refactored plan-resolution helper." Implementation vocabulary comes after the behavior sentence, if at all.
- **Every slide leads with one sentence a non-engineer could repeat back correctly.** File names, function names, and mechanics come second.
- **No session jargon.** Codenames, shorthand, and nicknames invented during the work mean nothing to the reader — spell out what they refer to or drop them.
- **Say why each item matters**: who is affected or what breaks if it's wrong. Importance is the reviewer's sorting key, so state it rather than making them infer it.

## Step 1 — capture evidence (before writing any HTML)

List the claims the work makes — one per feature, fix, or change. Then capture proof for each:

- **Tests**: run the real suite and save the real output. Trim long output; never alter it. Keep the summary line with counts.
- **CLI / backend work**: run real invocations and capture command + output verbatim. For bug fixes, also capture the *before* behavior (from the original file or `git stash`) so the pack shows failing → fixed.
- **Web UI**: use the browser tools when available — drive the actual flow like a user would, screenshot each meaningful state, and record short GIFs of interactions. Driving the real page forces JavaScript errors into the open where you can fix them.
- **Visual outputs** (charts, rendered documents): generate them for real and embed the actual output file.

Then **inspect every screenshot yourself**. You are multimodal — read the image: rendering glitches, error text, empty states, misaligned layout, wrong numbers. You can't watch your own videos, but you can read your own screenshots, and this inspection catches what a green test suite misses. Found a problem? Fix the code, recapture, and keep a note — "found and fixed during evidence capture" is a great line for the summary slide.

If the environment can't produce some evidence type (no browser, no display, missing library), capture the nearest substitute — terminal transcript, programmatic render — and record the gap on the Limitations slide.

## Step 2 — build the deck

Copy `assets/template.html` (next to this file) and fill in the slides — don't rebuild the shell from scratch. The left index, keyboard navigation, styling, and evidence components are already wired; every `<section class="slide" data-title="...">` auto-populates the sidebar.

A slide order that works:

1. **Summary** — what was asked, what was delivered, one line per work item with a verdict badge (shipped / partial / blocked). Each line names the change by its behavior, before → after, in plain language.
2. **What to check** — the reviewer's priority list: the 3–5 places this work could most plausibly be wrong, in plain language, ordered by risk. Include judgment calls made without asking, behavior changes with a wide blast radius, and anything whose evidence is weak or indirect. For each: what to look at, why it matters, and what "wrong" would look like. This slide answers "I have five minutes — where do I spend them?" — never skip it.
3. **Map** — a diagram of what changed: boxes and arrows over real file and function names showing how the pieces connect or how data flows. Draw it per **`assets/diagram-style.md`** (next to this file) — the pack's self-contained diagram design system: semantic component colors, arrow z-order and masking, spacing rules, legend placement, and the dark panel background that reads on both deck themes. Embed only inline `<svg>` — no HTML shell, Google Fonts, or CDN scripts; those violate the pack's offline single-file rule. The template's example Map slide shows the pattern. Simple and accurate beats elaborate.
4. **Architecture before/after** — when the work restructures anything (a refactor, an extraction, a new seam), one slide per structural change, placed before the code-level slides: the reviewer reads architectural changes first, then code, only if necessary. Each slide is the same dependency graph drawn twice over real module and function names — *before* with the problem nodes highlighted red (the setting read in six places, the shim, the inverted dependency), *after* with the new seams highlighted green. Head each graph with a claim the picture proves ("Before: settings.mode read in six places" / "After: two facades, zero mode reads anywhere") and label the slide with the commit hash + subject in the `.commit` kicker. Derive the graph from actual imports and call sites, not from memory — a structure diagram is evidence about structure and can be faked just as easily as a screenshot. When the interesting change is an interface rather than the graph, render the signatures as diffs instead: one `.sig` block per type or function with a NEW or CHANGED badge, removed lines red, added lines green, **signatures only — never bodies**. The template has both components ready; style the graphs like the Map diagram (previous entry).
5. **One slide per work item** — open with one plain-English sentence saying what changed in behavior terms and why it matters; then key `file:line` references, and the evidence right on the slide next to the claim it proves.
6. **Test artifacts** — the suite output; for scenario-style testing, one evidence block (screenshot, GIF, or transcript) per scenario.
7. **Limitations & caveats** — what you didn't verify, judgment calls you made, known gaps, anything the reviewer should double-check by hand. Never skip this slide or leave it empty; there is always something, and naming it is what makes the rest of the pack credible.

## Technical requirements

- **One file, works offline.** Inline all CSS and JS; embed every image and GIF as a `data:` URI; no CDN or external requests of any kind — the reviewer may open it with no network, and an external fetch that fails leaves a hole in the evidence. Run `scripts/embed_media.py <pack.html>` to inline local media references automatically.
- **Keep it light.** Downscale screenshots to ≤1200px wide, keep GIFs under ~10 seconds, and aim for under ~15MB total so the file opens instantly.
- **Diagrams are inline SVG** with real names from the codebase, not generic placeholders. Style them per `assets/diagram-style.md` (inline SVG only — no external fonts or scripts). Mermaid is fine as a sketching tool, but translate the result into inline SVG — a Mermaid CDN script breaks the offline rule.
- **Where it goes**: save as `docs/eval-packs/<yyyy-mm-dd>-<topic>.html` in the repo the skill is invoked in, unless the user asked for a different location. Tell the user the exact path when you're done, and on macOS offer to `open` it.

## Honesty

The pack is a review instrument, not a sales brochure. Failing tests appear in red with their real output. Half-finished work is labeled *partial* on the summary slide. A pack that hides problems is worse than no pack at all, because it converts the reviewer's trust into missed bugs.

## Credit

See the Credit section of this repo's `README.md` for the ideas and material this skill builds on.
