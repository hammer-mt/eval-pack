# eval-pack

A [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) that builds an **evaluation pack**: a single self-contained HTML slide deck — diagrams, screenshots, animated GIFs, and real captured test output — that proves completed agent work actually runs, so a human can review an hour of agent work in a few minutes.

Beyond making review fast, building the pack is a **verification forcing function**: you can't screenshot a feature that doesn't run, and you can't paste passing test output from a suite that fails. Much of the value comes from the bugs the agent finds and fixes while capturing evidence.

## Credit

The evaluation-pack concept comes from Lucas Meijer's talk **["A love letter to Pi"](https://www.youtube.com/watch?v=fdbXNWkpPMY)** (Build Monumental), about working with Mario Zechner's [Pi coding agent](https://github.com/badlogic/pi-mono). Meijer's framing: human review is the bottleneck (often 15 minutes of review for an hour of agent work), so shift the onus onto the agent to present a curated, efficient package of evidence.

## Install

Clone and symlink into your Claude Code skills directory:

```sh
git clone https://github.com/hammer-mt/eval-pack.git
ln -s "$(pwd)/eval-pack" ~/.claude/skills/eval-pack
```

Then in any Claude Code session, ask for an "eval pack" after a chunk of work — or the skill will offer one proactively after substantial changes.

## What's in the box

- `SKILL.md` — the skill definition: evidence-capture rules, slide order, honesty requirements
- `assets/template.html` — the deck shell (left-hand index, keyboard nav, evidence components) that gets copied and filled in
- `scripts/embed_media.py` — inlines local images/GIFs as `data:` URIs so the pack is one offline file

## Ground rules the skill enforces

- **Evidence, not claims** — every claim is backed by an artifact captured by actually running the thing; nothing fabricated or reconstructed
- **Written for the reviewer** — every slide leads with a plain-language behavior sentence, before → after; no session jargon
- **One file, works offline** — all CSS/JS inline, media embedded as `data:` URIs, no external requests
- **Honest by construction** — failing tests shown in red with real output, a mandatory Limitations slide, partial work labeled *partial*
