# Eval pack content modes

Choose one primary mode. Mix in a slide from another mode only when it materially helps the reader's decision.

## Change or pull request

Use when reviewing shipped or proposed code, product behavior, migration, refactor, or bug fix.

Recommended sequence:

1. **Executive summary:** ship verdict, scope, affected users, and verification status.
2. **What changed:** behavior-level before/after comparisons.
3. **Decisions:** one-way doors first, then reversible calls.
4. **Map or architecture:** show the dependency or data-flow change with real names.
5. **Proof by work item:** claim, file references, and captured evidence together.
6. **Test artifacts:** commands, run counts, scenarios, and gaps.
7. **Limitations:** unverified paths, rollout risk, and what to monitor.

For a small change, combine slides 2-5. Do not manufacture architecture for a one-line fix.

## Paper or research

Use when explaining a paper, benchmark, dataset, talk, or body of research.

Recommended sequence:

1. **Executive summary:** the result, why it matters, and how much confidence to place in it.
2. **The question:** what was tested and against which alternative.
3. **The finding:** the smallest set of quantitative or qualitative results that support the thesis.
4. **How it works:** method, system, or causal diagram.
5. **What the evidence does not establish:** design limits, sample limits, external-validity risks, and conflicting results.
6. **Implications:** separate direct consequences from your inference.
7. **Sources:** primary links, version/date, and supporting material.

Annotate each number with population, condition, metric, and uncertainty. Prefer a simple directly labeled chart over a screenshot of a dense paper figure when redrawing does not alter the data.

## Topic or strategy

Use when mapping a concept, operating model, proposal, team strategy, or decision landscape.

Recommended sequence:

1. **Executive summary:** mission, thesis, and the decision or commitment requested.
2. **Principles:** a short numbered set with no overlap.
3. **System:** the loop, operating model, or ownership map.
4. **Plan:** phases, sequence, dependencies, and proof at each stage.
5. **Case study:** one concrete example that demonstrates the system in miniature.
6. **Tradeoffs and open questions:** what changes the recommendation.
7. **Sources and glossary:** define unfamiliar terms where first used, then collect them here.

Remove repetition between philosophy, system, and plan. Each should answer a different question: why, how, and when.

## Evidence standard by mode

| Mode | Primary evidence | Required honesty check |
|---|---|---|
| Change/PR | Runs, screenshots, traces, diffs, deployed behavior | Could the reviewer reproduce the claim? |
| Paper/research | Primary text, tables, methods, data, source links | Is this the authors' claim or our inference? |
| Topic/strategy | Working context, case studies, operating constraints, cited research | Which statement is proposed policy rather than established fact? |
