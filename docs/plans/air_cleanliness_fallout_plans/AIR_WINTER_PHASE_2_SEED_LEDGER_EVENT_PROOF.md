# Air Winter Phase 2 Seed Ledger Event Proof

## Implemented scope

`chaosx.fallout.10` refreshes the 46-day country cooldown and schedules the manually authored `chaosx.fallout.18` result after 45 days for each of its three choices. At this tranche's review point, the Air Winter pilot contained 44 blocks, 132 options, and 131 effect-bearing options. The remaining effect-free option was the existing stale-order acknowledgement. Later tranche totals are maintained in `AIR_WINTER_EVENT_SCHEDULER_PROOF.md`.

These blocks are Air Winter incidents. They do not count toward the 660-block Fallout living-world release floor.

## Transaction proof

Each opening route writes exactly one of:

- `air_winter_seed_chain_vaults`
- `air_winter_seed_chain_herds`
- `air_winter_seed_chain_breeding`

`air_winter_event_refresh_state` sees the branch, writes the generic pending flag, and stores the original country in `air_winter_pending_event_owner`. The result trigger requires both regular event targets, current ownership by the stored country, the generic pending receipt, and one live branch.

All five effect-bearing result options repeat target validation at click time. The two conditional families also repeat their exact outcome test. Each completed option clears its branch before refreshing the state, so the generic reconciler clears the pending flag and owner in the same effect chain.

## Outcome and AI proof

| Route | Opening change used by result | Result gate | Exact pre-choice AI gate |
| --- | --- | --- | --- |
| Seed vault | Reclamation gains 2 | Reclamation above 25 and Exposure below 60 | Reclamation above 23 and Exposure below 60 |
| Herd slaughter | No conditional gate | Fixed depletion result | Existing war and emergency-food weighting |
| Breeding stock | Food Reserve loses 4 | Food Reserve above 30 and Shelter Capacity above 25 | Food Reserve above 34 and Shelter Capacity above 25 |

The seed-vault manpower cost is 1,000. The option and click both require that amount before the existing negative manpower effect runs. Every valid opening click refreshes the 46-day country cooldown immediately before scheduling the result. The seed-vault route also applies a 10 percent local factory penalty for 46 days, one day longer than the scheduled result.

Successful seed plots add 6 Food Reserve, 4 Adaptation, and 2 Reclamation. Failed plots remove 4 Food Reserve and add 1 Disease Pressure and 8 Building Damage Pressure. Herd depletion removes 6 Food Reserve and 2 Reclamation and adds 2 Disease Pressure. Successful breeding adds 6 Food Reserve, 2 Adaptation, and 4 Reclamation. Failed breeding removes 4 Food Reserve and 2 Reclamation and adds 2 Disease Pressure.

All ledger values pass through the established state normalization and survival refresh. The route introduces no monthly coefficient or Fallout survival coefficient.

## Memory and cancellation proof

Opening memory records the selected seed, slaughter, or breeding policy. Result memory separately records flourishing plots, failed plots, depleted herds, surviving breeding stock, or failed breeding stock.

`air_winter_event_clear_seed_ledger_memory` removes all older seed branches, outcomes, and the temporary industry modifier before a later owner writes a new route. Seed success and seed failure remove the modifier directly. `air_winter_event_cancel_pending_chain` clears every active seed branch and the modifier. `air_winter_event_clear_state_memory` clears all opening and outcome memory during a full Air Winter reset.

Ownership change, state reset, Fallout transition, and active Fallout therefore cannot resolve a stale seed result against a new owner. The existing Fallout snapshot order preserves the live Air Winter row before pending cleanup.

## Asset and localisation proof

Events 10 and 18 use `GFX_report_event_air_winter_phase_2` from `interface/air_cleanliness_winter.gfx`. The industry modifier uses `GFX_air_winter_phase_2`. Their final DDS files live under dedicated Air Winter and Fallout paths. The manifest covers Phase 2 events 10 through 18. The route requires no additional asset and uses no zombie asset, audio, sprite, file, or path.

The opening and result use state-aware text and government-aware authority terms. Their visible event keys are in `localisation/english/fallout_world_end_events_l_english.yml`. The modifier name and description are in `localisation/english/air_cleanliness_winter_l_english.yml`.

## Runtime boundary

The installed documentation and existing pilot support delayed country events, regular event-target retention, scope-valued owner variables, and the current pending-chain pattern. Hearts of Iron IV was not launched. Delayed target retention, popup display, AI choice, save-resume behavior, and monthly cancellation remain runtime observation gates.

No simplification or fallback was used inside the delayed-result transaction. The broader Breadbasket obligation remains partial because the approved post-Fallout food-recovery consumer does not exist. It depends on the pending Fallout numerical contract. The active user contract forbids a political-power store, so this route uses manpower and the factory diversion. At this review point, dead-city salvage, island refugee identity, and state-specific heavy-industry rows remained separate work. Later tranches implemented all three rows under their own accepted addenda and proofs. The dead-city salvage proof is `AIR_WINTER_PHASE_5_DEAD_CITY_SALVAGE_EVENT_PROOF.md`.
