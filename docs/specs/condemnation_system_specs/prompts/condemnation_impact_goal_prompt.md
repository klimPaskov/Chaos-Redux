/goal Implement the queued Condemnation refinements to their fullest extent.

Read CLAUDE.md, docs/specs/condemnation_system_specs/specs/condemnation_impact_system_spec.md and the implemented docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md. The accepted 2026-09-20 tuning (0-1000 range, cost multiplier 1 + C/500 rounded up, 5-15% Consumer Goods inspection burden for 180 days) stays unchanged.

The sanctions system already exists. Implement only the rows the spec marks accepted and queued:

1. Consolidate target responses to the spec's twelve decisions: Admit inspectors (inspections plus observers), Destroy stockpiles (chemical plus biological, per-family restrictions), Dismantle restricted sites, Pay compensation, Non-use pledge, Reform the command; Refuse inspections, Rally the nation, Sanctions war economy, Lean on subjects; Smuggle arms, Covert fuel route, Front companies. Each merged response keeps the strongest effect of its parts, uses the shared cost multiplier, and migrates running legacy timers and flags so a save keeps remaining durations.
2. Fold repeat use into the repeated source's bucket and remove the separate public repeat-use line without changing pledge-breach cover-up.
3. Reduce the Condemnation detail panel to the spec's six elements; keep fatigue, dependency, vulnerability, severity and hidden evidence internal. Use the chaos-redux-scripted-gui skill and review the changed panel with gui_render where available.
4. Make enforcing participants at Tier 4 and above ineligible as Import Food donors for the target unless the pair has a humanitarian carve-out, through a famine-owned donor trigger that reads a condemnation pair trigger.
5. Retune AI weights for the merged responses so weak targets comply and strong targets defy, and compare representative scenarios with chaosx_ai_probability_auditor.

Update localisation (UTF-8 with BOM), the system document, the decision category, and the famine system document in the same change. Remove obsolete decisions, ideas, localisation and constants rather than leaving them unused. Report any simplification under a clear heading.
