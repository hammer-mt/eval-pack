# eval-pack

A [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) that builds an **evaluation pack**: a single self-contained HTML slide deck — before/after architecture diagrams, signature diffs, screenshots, animated GIFs, and real captured test output — that proves completed agent work actually runs, so a human can review an hour of agent work in a few minutes. The reviewer reads architectural changes first, then code, only if necessary.

Beyond making review fast, building the pack is a **verification forcing function**: you can't screenshot a feature that doesn't run, and you can't paste passing test output from a suite that fails. Much of the value comes from the bugs the agent finds and fixes while capturing evidence.

## Credit

The evaluation-pack concept comes from Lucas Meijer's talk **["A love letter to Pi"](https://www.youtube.com/watch?v=fdbXNWkpPMY)** (Build Monumental), about working with Mario Zechner's [Pi coding agent](https://github.com/badlogic/pi-mono). Meijer's framing: human review is the bottleneck (often 15 minutes of review for an hour of agent work), so shift the onus onto the agent to present a curated, efficient package of evidence.

The architecture before/after slides come from **[Delba de Oliveira's workflow](https://x.com/delba_oliveira/status/2073467304491233543)**: "You don't need to read code anymore. Read architectural changes first, then code, if necessary." Her caveats carry over — this works best when the agent has strong ways to verify its work, and when architectural decisions are iterated on upfront, before code gets written.

The diagram design system (`assets/diagram-style.md`) is distilled from the **architecture-diagram** skill (v1.1, MIT License) by [Cocoon AI](mailto:hello@cocoon-ai.com), adapted for the pack's inline-SVG offline rule so this repo is fully self-contained.

## Install

Clone and symlink into your Claude Code skills directory:

```sh
git clone https://github.com/hammer-mt/eval-pack.git
ln -s "$(pwd)/eval-pack" ~/.claude/skills/eval-pack
```

Then in any Claude Code session, ask for an "eval pack" after a chunk of work — or the skill will offer one proactively after substantial changes.

## What's in the box

- `SKILL.md` — the skill definition: evidence-capture rules, slide order, honesty requirements
- `assets/template.html` — the deck shell (left-hand index, keyboard nav, evidence components, before/after architecture slide, signature-diff blocks) that gets copied and filled in
- `assets/diagram-style.md` — the self-contained SVG diagram design system (colors, arrows, spacing, before/after highlight convention)
- `scripts/embed_media.py` — inlines local images/GIFs as `data:` URIs so the pack is one offline file

## Ground rules the skill enforces

- **Evidence, not claims** — every claim is backed by an artifact captured by actually running the thing; nothing fabricated or reconstructed
- **Written for the reviewer** — every slide leads with a plain-language behavior sentence, before → after; no session jargon
- **One file, works offline** — all CSS/JS inline, media embedded as `data:` URIs, no external requests
- **Honest by construction** — failing tests shown in red with real output, a mandatory Limitations slide, partial work labeled *partial*
