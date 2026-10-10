# Coding Prompt: Event 008 Tensions Rising remaining work

Event 008 is implemented: hidden root and batch report, the accepted 2/3/5/8/12 ladder and 30-day cadence, Diplomatic Fever stages, the capped timer pulse, relation shocks, AI posture ideas, ten incidents, safe border clashes, event-log wiring, and five achievements.
Do not rebuild any of it from older planning text.
Read the [README](../README.md), [owner decisions](../../../plans/008_tensions_rising_plans/agent_decisions_2026-10-05.md), and [owner state map](../../../plans/008_tensions_rising_plans/documentation_state_2026-10-05.md) before changing source.

Follow `CLAUDE.md` and the `chaos-redux-events` skill.

## Remaining source work

This item repairs consistency with accepted design and needs no new decision:

- Rescale `tensions_rising_incident_world_tension` in `common/script_constants/008_tensions_rising_constants.txt` so every incident packet stays below the root packet of the stage that scheduled it; the current 25-75 values exceed even the Stage IV root of 12 and undo the 6 October balance correction through follow-ups.
  Record the change in the owner decisions and rerun the owner's source model for the distribution helper.

## Work that needs a decision first

Implement these only after the README's open questions record an accepted disposition:

- the cluster record (cluster owner).
- the audit proposals on follow-up pool order, relation-selector fallbacks, clash outcomes, and cluster severity.

Any accepted change to follow-up weights, pool order, or selection needs a before-and-after comparison through `chaosx_ai_probability_auditor` using the owner's 24 declared scenarios.

## Validation still owed

Runtime lifecycle, Event Log and Details GUI evidence, numerical probability comparison, held-report refresh, and asset provenance remain open; see the owner state map.
Catalog wording is queued in `docs/plans/008_tensions_rising_plans/catalog_changes_pending.md` for the spreadsheet owner.
`docs/events/008_tensions_rising/overview.md` still lists the superseded `+100` to `+1000` world-tension values and needs the 2/3/5/8/12 ladder.
Report every remaining blocker; do not claim completion while any of the above stays open.
