# Comparison prompt for `chaosx_ai_probability_auditor`

Work read-only with no inherited conversation context. Compare the final Event 38 weighted implementation against the accepted baseline using the same named scenarios and complete pools.

Read the full Event 38 specs, `docs/plans/038_malta_crusaders_plans/probability_baseline.md`, the owner patch handoff, and the final weighted source. Start with `hoi4.probability_inspect`, then run `hoi4.probability_compare` against every baseline scenario affected by the patch. Use evaluate, sweep, simulation, or render only when required to explain the comparison.

Confirm:

- intended route ordering changed only where the parent defined a target
- no valid route, order, focus, decision, principality, relic, side, target, or unit family is starved unintentionally
- invalid or impossible candidates receive zero practical probability
- Germany's Atlantis choice is 90 percent only inside the complete eligible pool and human Germany remains a normal choice
- evolution timing remains paced and disabled evolutions cannot record or unlock content
- Holy World side assignment produces viable opposition across all four scenario intensities
- regional war targeting respects supply, distance, current war, strength, and cooldown
- Malta AI prioritizes survival and logistics when endangered
- Eleventh Crusade AI selects feasible recovery actions
- probability modifiers do not create runaway loops or repeated same-family outcomes

Use the same evidence labels as the baseline and report any pool or external-state difference that makes direct comparison invalid. Save the report under `docs/plans/038_malta_crusaders_plans/probability_compare.md`. Do not patch source.
