# Fallout Filters Fail at Night addendum

## Status

This is the next reviewed dormant global-survival tranche after Bad Batch. It is an implementation handoff, not scheduler activation approval. The chain remains outside the countable release floor until its caller, localisation, Event Log, event details, assets, AI, cleanup, and manual audit all pass review.

## Fixed identities

| Surface | Value |
| --- | ---: |
| Human opening | `217` |
| Hidden AI opening | `218` |
| Human delayed results | `219` through `222` |
| Hidden AI delayed results | `223` through `226` |
| Human callback | `227` |
| Hidden AI callback | `228` |
| Cleanup | `229` |
| Candidate identity | `217` |
| Transaction key | `710009` |
| Candidate route | `7109` |
| Event Log history | `9114` |
| Result delay | `14` days |
| Callback delay | `120` days |

All event definitions belong in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`. No Zombie-owned id, file, asset, audio, sprite, or path may be referenced.

## Eligibility and frozen receipt

The candidate producer selects the lowest owned state that passes the current-generation Fallout identity row, durable resource row, and produced Air Winter snapshot. The state must have shelter capacity above `35` and exposure above `20`. The country must have filters below `24` and at least one affordable lane. Every branch cost is checked before the opening can be published. The producer writes candidate id, state target, phase, region, government, cause-memory, winter match, current food, filters, medicine, shelter capacity, adaptation, reclamation, and exposure into the country-owned candidate row.

The opening freezes the target state, owner, generation, mode, branch, due day, visible-budget cost, and all resource inputs before setting its pending marker. The result and callback rows reject stale owners, stale generations, missing state flags, changed target ids, duplicate transactions, and invalid branch tokens. The callback never rereads mutable Air Winter values for outcome classification.

## Player choices

1. **Seal the lower levels** spends four filters and three medicine. It protects the deepest shelter levels, reduces exposure, and accepts overcrowding in the accessible floors.
2. **Rotate the surface teams** spends three filters and two food. It keeps essential work running, spreads exposure across shifts, and protects adaptation at the cost of reserve food.
3. **Open emergency vents** spends five scrap and two recognition. It preserves shelter capacity and removes pressure from the filter room, but raises short-term exposure and invites a public legitimacy dispute.
4. **Ration filters by household** spends five filters and four recognition. It creates a transparent allocation ledger, raises cohesion when it succeeds, and produces a sharper class grievance when it fails.

The four lanes are not cosmetic variants. They use different costs, thresholds, timed modifiers, state flags, resource changes, population risks, and callback memories.

## Deterministic outcome contract

The frozen shelter viability score is:

`Shelter * 40 / 100 + Filters * 25 / 100 + Medicine * 15 / 100 + Adaptation * 20 / 100 - Exposure * 25 / 100`

The score is rounded once and clamped from `0` through `100`. Branch-specific success requires the frozen viability score and the branch resource gates. Partial success requires the lower band. Anything below the partial band is failure. A failure calls the shared Deaths helper against the target state's current population with a branch-specific percentage and preserves the minimum remaining population floor. Failure does not apply a direct population mutation outside Deaths.

The selected branch is stored before delayed-row reservation. The result applies exactly one branch and one outcome. No random effect, MTTH roll, political-power store, or generic fallback is permitted.

## Branch outcomes

| Branch | Success memory | Partial memory | Failure memory |
| --- | --- | --- | --- |
| Seal lower levels | `fallout_event_217_memory_sealed_levels` | `fallout_event_217_memory_partial_seal` | `fallout_event_217_memory_breach` |
| Rotate surface teams | `fallout_event_217_memory_rotating_teams` | `fallout_event_217_memory_exhausted_teams` | `fallout_event_217_memory_exposure_deaths` |
| Open emergency vents | `fallout_event_217_memory_vented_levels` | `fallout_event_217_memory_unstable_vents` | `fallout_event_217_memory_vent_failure` |
| Ration filters by household | `fallout_event_217_memory_household_ledger` | `fallout_event_217_memory_contested_ledger` | `fallout_event_217_memory_class_grievance` |

Success, partial, and failure alter filters, medicine, food, shelter capacity, exposure, adaptation, reclamation, cohesion, recognition, and timed country modifiers in different combinations. The callback converts the delayed result into one durable institutional memory and a branch-aware follow-up modifier. The callback cannot open another Filters Fail transaction while the current cleanup row exists.

## Hidden AI parity

The hidden AI opening evaluates the same frozen inputs and branch costs as the human opening. The base score is `10`. A success projection adds `8`. A partial projection adds `3`. Unaffordable branches receive `-1000` after all other modifiers. The score matrix adds government-archetype, phase, cause-memory, war, low-filter, high-exposure, shelter-capacity, and prior-memory adjustments. Exact ties resolve in this order: seal lower levels, rotate surface teams, open emergency vents, ration filters by household. The hidden result, callback, Deaths path, Event Log payload, and cleanup call the same effects as human play.

## Event Log and presentation

History `9114` receives explicit payloads for each branch and outcome plus callback success, partial, and failure. The event detail router and scripted localisation must map the history id without changing any Zombie route. Human events use a dedicated Fallout report image named `GFX_report_event_fallout_filters_fail`. Hidden AI events use no player-facing picture.

## Asset handoff

Create a dedicated fictional shelter interior showing a failing filter room at night. Use no real person, flag, attested symbol, or Zombie visual. The package needs source PNG, processed 210 by 176 PNG, final DDS, prompt provenance, manifest, contact sheet or preview, and a `.gfx` handoff. The final sprite belongs in `interface/fallout_consolidated.gfx` and the DDS belongs under `gfx/event_pictures/fallout/`.

## Acceptance checks

1. IDs `217` through `229` are unique in the Fallout event file.
2. The event namespace remains `chaosx.fallout`.
3. The candidate row is idempotent for generation, country, state, and transaction key.
4. No branch can enter without a current target and owner.
5. The four branch costs are distinct and affordability is checked before the opening.
6. The target state has produced Air Winter shelter provenance.
7. Exposure and shelter values are frozen before result scheduling.
8. Outcome arithmetic rounds once and clamps to the accepted interval.
9. Result delivery uses the exact fourteen-day due day.
10. Callback delivery uses the exact one-hundred-twenty-day due day.
11. Human and hidden AI branches use the same result effect.
12. Hidden AI tie order is deterministic and documented.
13. Failure casualties enter the Deaths system only.
14. Failure preserves the minimum remaining population floor.
15. Each branch has distinct success, partial, and failure memories.
16. Each result releases its branch payment once.
17. Each result writes one Event Log payload and never duplicates it on retry.
18. Callback requires the authenticated delayed result token.
19. Cleanup requires both result and callback terminal receipts.
20. Cleanup clears the state registry and all temporary flags.
21. Dynamic modifiers have no political-power stores or harmless failure loops.
22. Human localisation names shelter levels, filters, medicine, and the affected region.
23. AI paths have no player popup.
24. Dedicated asset files are present and registered.
25. No Zombie id, path, sprite, audio, or asset is referenced.
26. Workbook wording matches the final event and callback localisation if the shared workbook can be updated without staging unrelated edits.
27. The scheduler activation flags remain unset.

## Deferred work

Regional, government-archetype, successor-memory, and character overlays remain queued until the core chain passes manual review. This addendum does not approve the scheduler, the 660-block floor, the manual scenario, the blackout GUI, or runtime acceptance.
