# Air Winter Phase 1 Regional Return Event Proof

## Scope

This document records static proof for the five Phase 1 regional openings in `chaosx.fallout.1` through `chaosx.fallout.5` and their shared delayed result in `chaosx.fallout.6`.

This is Air Winter pilot content. It does not activate the Fallout living-world scheduler and does not count toward the 660-block Fallout release floor. Hearts of Iron IV was not launched, as requested, so no runtime observation is claimed.

The tranche does not change the Air Winter survival formula, monthly phase coefficients, Fallout grading, treaty projects, active combat pressure, strategic bombing, the blackout GUI, the manual scenario, or any world iterator.

## Identifier and presentation ownership

`chaosx.fallout.6` is declared once in `events/fallout_world_end_events.txt` under the existing `add_namespace = chaosx.fallout` declaration. It was free before this allocation. Existing event ids were not renumbered.

Events 1 through 6 use `GFX_report_event_air_winter_phase_1`. The sprite and DDS remain in the dedicated Fallout-owned Air Winter paths. This tranche adds no image, sound, super-event, zombie id, zombie file, zombie asset, zombie sprite, zombie audio, or zombie path.

## Opening transaction

`air_winter_event_phase_1_opening_targets_are_valid` requires the established regular country and state targets, continued state ownership by the saved country, no Fallout transition, no active Fallout, no generic delayed-result row, and no pending Air Winter branch.

Events 1 through 5 use that validator in three places:

1. the event trigger
2. every option display gate
3. every click transaction

The four conditional choices also repeat their exact live gate at display and click time:

- full production shifts require an operational Civilian Factory or Military Factory
- shipyard coal priority requires an operational Dockyard or Naval Base
- field drainage requires the country to retain the 500 Manpower payment
- marked corridors require operational Infrastructure or Railway presence and the 4 Command Power payment

The thermometer, warehouse, cistern, fountain, school-shelter, and recalled-crew choices remain unconditional after the shared target proof. Every valid opening therefore retains an executable choice.

Each successful opening click performs one ordered transaction:

1. clear older Phase 1 policy and outcome memory for the selected state and country
2. apply the country cost and immediate Air Winter ledger changes
3. write exactly one Phase 1 branch and one matching policy memory
4. refresh the state after the branch exists
5. let the shared refresh bind the generic pending flag and original owner
6. refresh the 46-day country cooldown
7. schedule event 6 after the shared 21-day short delay

The order matters. `air_winter_event_refresh_state` can only bind a pending owner after `air_winter_event_has_pending_chain` sees the selected branch.

An old opening popup uses `air_winter_event_reject_stale_opening_choice`. That effect can open event 203 while Fallout is inactive, but it never clears a branch, pending flag, pending owner, or saved target. A stale opening therefore cannot destroy a newer transaction belonging to the same state and country. Delayed result popups retain the existing result rejection effect because cancelling their matching transaction is intentional.

## Branch cardinality

The state branch ledger has ten flags, one for each opening policy. `air_winter_event_has_any_phase_1_branch` supplies generic pending detection and orphan reconciliation.

The installed trigger documentation defines `count_triggers` with an integer `amount` field. The offline trigger reference describes the amount as a minimum. The engine documentation does not declare shared script-constant support for that field. The implementation therefore uses file-local preprocessing values that resolve to the structural integers 1 and 2.

`air_winter_event_has_exactly_one_phase_1_branch` requires a count of at least one and rejects a count of at least two over the same ten flags. `air_winter_event_has_malformed_phase_1_branches` detects a count of at least two. This proves the exact one-of-ten contract without placing a `constant:` token in an undocumented parser field.

All ten flags are present in:

- the exact and malformed cardinality checks
- `air_winter_event_has_pending_chain`
- Phase 1 pending cancellation
- full state-memory cleanup
- opening initialization
- event 6 titles, descriptions, option gates, and click guards

Monthly reconciliation cancels a Phase 1 branch without the generic pending flag, two or more Phase 1 branches, a generic row without any pending branch, or a generic row whose stored owner no longer owns the state.

## Regular event targets and owner authority

The existing dispatcher saves `air_winter_event_country` and `air_winter_event_state` as regular event targets. The offline Data Structures reference states that regular event targets carry into delayed events fired from the same effect chain. Installed vanilla event files use the same delayed `country_event` pattern.

`air_winter_event_phase_1_result_targets_are_valid` independently requires:

- both saved targets
- the saved country to be the resolving country
- a valid state still owned by that country
- the generic pending flag
- the pending-owner variable
- equality between the pending owner and the saved country
- current ownership by the pending owner
- exactly one Phase 1 branch

Event 6 uses that validator in its event trigger and every click transaction. A valid result does not require the state to remain in Phase 1. The delayed report evaluates the live ledgers and buildings after 21 days even if ordinary Air Winter progression has changed the phase. Fallout transition and active Fallout remain invalid through the shared base target contract.

## Deterministic results

Event 6 contains twenty visible options. Every branch has one success option and one failure option. The failure predicate is the explicit complement of the success trigger.

| Branch | Live success proof | Success result | Failure result |
| --- | --- | --- | --- |
| thermometer shifts | Adaptation at least 18 and Exposure no higher than 45 | Adaptation up 2, Exposure down 1, Stability up 0.5 percent | Adaptation down 2, Exposure up 2, Stability down 0.5 percent |
| full shifts | operational factory, Adaptation at least 15, Exposure no higher than 45, Disease no higher than 35, pressure no higher than 45 | Reclamation up 2, pressure down 8, War Support up 0.5 percent | Exposure up 3, Disease up 2, pressure up 15, minor Deaths, 21-day factory-access penalty, Stability down 0.5 percent |
| warehouse rooms | Shelter at least 20 and Disease no higher than 35 | Shelter up 2, Disease down 1, Refugee Pressure down 2, Stability up 0.5 percent | Shelter down 2, Disease up 2, Refugee Pressure up 2, Stability down 0.5 percent |
| shipyard priority | operational port, Reclamation at least 18, Exposure no higher than 45 | Food up 2, Reclamation up 2, pressure down 8, War Support up 0.5 percent | Exposure up 3, pressure up 15, minor Deaths, 21-day supply penalty, War Support down 0.5 percent |
| cistern rationing | Water at least 30 and Disease no higher than 35 | Water up 2, Disease down 1, Reclamation up 2, Stability up 0.5 percent | Water down 2, Disease up 2, Refugee Pressure up 2, Stability down 0.5 percent |
| open fountains | Water at least 20 and Disease no higher than 35 | Water up 2, Reclamation up 2, Stability up 0.5 percent | Water down 5, Disease up 4, Exposure up 2, minor Deaths, 21-day supply penalty, Stability down 1 percent |
| field drainage | Food at least 45 and pressure no higher than 45 | Food up 2, Reclamation up 2, pressure down 8, Stability up 0.5 percent | Food down 4, Disease up 2, pressure up 15, minor Deaths, 21-day supply penalty, Stability down 0.5 percent |
| school shelters | Shelter at least 25 and Disease no higher than 35 | Shelter up 2, Adaptation up 2, Disease down 1, Stability up 0.5 percent | Shelter down 2, Disease up 4, Exposure up 2, minor Deaths, Stability down 0.5 percent |
| marked corridor | operational transport, Adaptation at least 18, Reclamation at least 18, Exposure no higher than 45 | Adaptation up 2, Reclamation up 2, Exposure down 1, 21-day supply benefit, War Support up 0.5 percent | Exposure up 4, pressure up 15, Refugee Pressure up 2, severe Deaths, 21-day supply penalty, War Support down 0.5 percent |
| recalled crews | Shelter at least 20, Adaptation at least 8, pressure no higher than 45 | Shelter up 2, Exposure down 1, pressure down 8, Stability up 0.5 percent | Shelter down 2, Exposure up 2, Refugee Pressure up 2, minor Deaths, Stability down 0.5 percent |

Exactly one option can be visible for a valid branch. Every option repeats its branch and outcome proof at click time. No fallback or twenty-first result exists.

## AI projection

Every opening option preserves its existing base role and adds a strong weight when its exact pre-choice projection reaches the delayed success gate. A weak weight applies to the explicit inverse. The projection reverses the opening's own ledger changes, including Exposure, Disease, Building Damage Pressure, Food, Shelter, Water, Adaptation, and Reclamation changes.

| Branch | Exact pre-choice AI projection |
| --- | --- |
| thermometer shifts | Adaptation at least 14 and Exposure no higher than 45 |
| full shifts | operational factory, Adaptation at least 15, Exposure no higher than 43, Disease no higher than 34, and pressure no higher than 37 |
| warehouse rooms | Shelter at least 16 and Disease no higher than 35 |
| shipyard priority | operational port, Reclamation at least 18, and Exposure no higher than 43 |
| cistern rationing | Water at least 22 and Disease no higher than 35 |
| open fountains | Water at least 25 and Disease no higher than 33 |
| field drainage | Food at least 41 and pressure no higher than 37 |
| school shelters | Shelter at least 19 and Disease no higher than 34 |
| marked corridor | operational transport, Adaptation at least 14, Reclamation at least 14, and Exposure no higher than 46 |
| recalled crews | Shelter at least 16, Adaptation at least 10, and pressure no higher than 30 |

The strong and weak modifiers use the same scripted trigger and its direct inverse. Government and live crisis modifiers distinguish public schedules, shelter policy, military production, port priority, local continuity, war needs, low Stability, low Food, and low Shelter without replacing the exact projection. Event 6 needs no random AI weighting because exactly one result option is visible.

## Deaths, buildings, and supply

Minor casualty failures request 0.005 percent of current state civilian population. The failed marked corridor requests 0.01 percent. Every casualty option sets `air_winter_event_death_percent` and calls `air_winter_event_apply_deaths`. No option subtracts population directly.

Phase 1 does not call `damage_building` or any building-damage helper. Early failures change Building Damage Pressure and may apply one short timed state modifier:

- 10 percent lower local factory access
- 10 percent lower local supply
- 5 percent higher local supply

Each modifier lasts 21 days. Applying one removes the other two. Opening cleanup clears the older Phase 1 policy, result, casualty, and pending-branch memories but deliberately preserves any resolved timed modifier already running on the state. Generic pending cancellation and valid result finalization also leave that modifier intact. Only its timed expiry or full Air Winter state-memory reset removes it.

## Memory and cleanup

The state and country retain the chosen regional policy. A resolved branch writes exactly one of `air_winter_memory_phase_1_success` or `air_winter_memory_phase_1_failure`. Casualty failures additionally write `air_winter_memory_phase_1_casualties`.

Every valid result applies its outcome, writes state and country memory, clears all Phase 1 branch flags, and refreshes the state. The refresh sees the generic pending row without a live branch and uses shared reconciliation to clear the pending flag and stored owner. Because Phase 1 result modifiers are not part of generic pending cancellation, a valid 21-day effect survives that finalization step.

The generic state and country reset effects call the Phase 1 memory clearers. No Phase 1 branch, policy flag, result flag, casualty flag, or result modifier survives a full Air Winter reset.

## Localisation and asset reuse

All 110 event localisation keys used by events 1 through 6 are present once. They cover five opening titles and descriptions, ten opening option names and tooltips, and the twenty conditional result titles, descriptions, option names, and tooltips. The three timed state modifiers also have unique name and description keys. Opening tooltips disclose the 21-day return and each exact live success gate. Result tooltips disclose ledger changes, national effects, Deaths requests, timed modifiers, and durable winter memory where relevant.

Events 1 through 6 all use `GFX_report_event_air_winter_phase_1`. The existing source PNG, processed PNG, DDS, sprite registration, manifest row, and GFX handoff remain Fallout-owned. No new asset, audio, sprite, or path is introduced by this tranche.

## Static counts

The previously reviewed pilot snapshot contained 51 blocks, 171 options, 170 effect-bearing options, and 57 delayed-result schedules. This tranche adds:

- one event block
- twenty options, all with guarded hidden effects
- ten delayed schedules from events 1 through 5

The current Air Winter pilot therefore contains:

- 52 event blocks
- 191 options
- 190 effect-bearing options
- 67 delayed-result schedules

Event 203 remains the only effect-free acknowledgement. The Air Winter pilot remains separate from the Fallout living-world release floor, which is still 0 of 660 reviewed event blocks.

## Read-only tooling boundary

A read-only `hoi4.event_inspect` request was attempted for `chaosx.fallout.6`. The refreshed scan returned `ARTIFACT_STORAGE_LIMIT`, and the cached scan returned `INTERNAL_ERROR`. No MCP graph artifact or graph-based conclusion is claimed. These failures do not replace the independent source audit recorded in this proof.

## Runtime observation limit

Static inspection proves the declared ids, branch coverage, parser structure, click guards, Deaths calls, modifier wiring, localisation references, and asset ownership. It cannot observe the delayed callback, timed-modifier display, multiplayer popup presentation, or save recovery because Hearts of Iron IV was not launched. No weaker substitute was used for any requirement inside this tranche.
