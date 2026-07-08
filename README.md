# eval-pack

A Claude Code and Codex skill that builds an **evaluation pack**: a single self-contained HTML explainer for a pull request, completed feature, paper, research topic, strategy, or technical concept. Each pack leads with an executive summary, maps the argument visually, and makes the supporting evidence inspectable.

Beyond making review fast, building the pack is a **verification forcing function**: you can't screenshot a feature that doesn't run, and you can't paste passing test output from a suite that fails. Much of the value comes from the bugs the agent finds and fixes while capturing evidence.

## Credit

The evaluation-pack concept comes from Lucas Meijer's talk **["A love letter to Pi"](https://www.youtube.com/watch?v=fdbXNWkpPMY)** (Build Monumental), about working with Mario Zechner's [Pi coding agent](https://github.com/badlogic/pi-mono). Meijer's framing: human review is the bottleneck (often 15 minutes of review for an hour of agent work), so shift the onus onto the agent to present a curated, efficient package of evidence.

The architecture before/after slides come from **[Delba de Oliveira's workflow](https://x.com/delba_oliveira/status/2073467304491233543)**: "You don't need to read code anymore. Read architectural changes first, then code, if necessary." Her caveats carry over — this works best when the agent has strong ways to verify its work, and when architectural decisions are iterated on upfront, before code gets written.

The diagram design system (`assets/diagram-style.md`) is distilled from the **architecture-diagram** skill (v1.1, MIT License) by [Cocoon AI](mailto:hello@cocoon-ai.com) — its arrow z-order, spacing, and legend rules — adapted for the pack's inline-SVG offline rule and restyled to be theme-adaptive (diagrams inherit the deck's light/dark theme via CSS variables) so this repo is fully self-contained.

## Install

Clone once, then symlink into either or both skill directories:

```sh
git clone https://github.com/hammer-mt/eval-pack.git
ln -s "$(pwd)/eval-pack" ~/.claude/skills/eval-pack  # Claude Code
ln -s "$(pwd)/eval-pack" ~/.codex/skills/eval-pack   # Codex
```

Restart the agent, then ask for an “eval pack,” “paper explainer,” or “review pack.”

## What's in the box

- `SKILL.md` — the skill definition: evidence-capture rules, slide order, honesty requirements
- `references/content-modes.md` — distinct narrative structures for changes, papers, and strategy topics
- `references/editorial-design.md` — the editorial hierarchy and reusable visual grammar
- `assets/template.html` — the responsive deck shell with numbered navigation, keyboard controls, end-of-slide next actions, evidence components, and reusable editorial layouts
- `assets/diagram-style.md` — the self-contained SVG diagram design system (colors, arrows, spacing, before/after highlight convention)
- `scripts/embed_media.py` — inlines local images/GIFs as `data:` URIs so the pack is one offline file
- `scripts/validate_pack.py` — checks placeholders, offline assets, required sections, alt text, and navigation structure

## Ground rules the skill enforces

- **Evidence, not claims** — every claim is backed by an artifact captured by actually running the thing; nothing fabricated or reconstructed
- **Written for the reviewer** — every slide leads with a plain-language behavior sentence, before → after; no session jargon
- **Executive-summary first** — the conclusion and decision appear before mechanics or methods
- **Evidence and interpretation stay separate** — especially for papers and strategy topics
- **One file, works offline** — all CSS/JS inline, media embedded as `data:` URIs, no external requests
- **Mobile is first-class** — the index becomes a horizontal top rail and every slide retains a next action
- **Honest by construction** — failing tests shown in red with real output, a mandatory Limitations slide, partial work labeled *partial*
