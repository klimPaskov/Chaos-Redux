# Air Cleanliness Treaty Lifecycle Proof

## Proof boundary

This document records static proof for the restored treaty lifecycle, the first state-targeted Air Winter treaty project, and the formula-preserving Verification Mission. It does not claim runtime acceptance. Hearts of Iron IV was not launched.

The implemented boundary includes deterministic formation, retry-safe invitation receipts, idempotent membership, violation sanctions, founder succession, annex cleanup, an atomic Global Cleaning Day, one Joint Filter Convoy vertical slice, one secretariat Verification Mission, exact active-project ownership, and a silent Fallout pause transaction.

Pooled decontamination, seed archives, evacuation corridors, relief votes, major-burner sanctions, and post-Fallout membership policy remain outside this tranche. Detailed inspection proof is recorded in `AIR_CLEANLINESS_TREATY_INSPECTION_PROOF.md`.

## Required references

The following required offline references were consulted:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- installed official `documentation/effects_documentation.md`
- installed official `documentation/triggers_documentation.md`
- installed official decision `_documentation.md`

## Engine-sensitive surfaces

| Surface | Static proof | Implementation |
| --- | --- | --- |
| Persistent scope arrays | Official effects documentation defines `add_to_array`, `remove_from_array`, `clear_array`, and `for_each_scope_loop`. Official trigger documentation defines `is_in_array`, `any_of_scopes`, and `all_of_scopes`. | Member countries, violator countries, active convoy donors, active verification inspectors, and active route states are stored in global arrays. Removal uses separate work queues. |
| Country-array precedent | Vanilla `common/scripted_effects/NORDIC_scripted_effects.txt` builds and iterates a country scope array. Vanilla `common/decisions/TOA_shared_decisions.txt` persists country scopes in a global decision array. | The treaty host iterates `global.air_winter_registered_countries` and `global.air_cleanliness_treaty_members`. |
| Targeted decision scopes | Official decision documentation defines ROOT as actor and FROM as target. Vanilla `common/decisions/AST.txt` uses FROM in completion and removal effects for a `target_array` decision. | Joint Filter Convoy stores donor, recipient, and state. Verification stores founder ROOT and subject FROM on both country receipts. |
| Real equipment payment | Vanilla `AST_supply_arms_to_nation` consumes equipment from ROOT and targets FROM. Existing Air Winter helpers remove exact support equipment, train, and convoy stockpiles. | Cleaning Day and Convoy pay at project start. Verification pays secretariat equipment at dispatch and distinct inspected-member equipment after full or restricted access. |
| Stored state-id scoping | Existing Air Winter response code stores `air_winter_response_priority_state` and scopes it with `var:<state variable>`. | The convoy copies the exact selected state id, reserves that state, and scopes it again at completion. |
| Delayed country event | Official event effects document `country_event` with a day delay. Offline event documentation requires the trigger to remain true when the delayed event fires. | The invitation dispatcher validates its attempt at delivery. Verification dispatcher `chaosx_air_treaty.9` runs exactly seven days after a response, opens `.7` for an exact paired receipt, and clears invalid delayed state on that day. |
| Persistent founder | Official effects documentation defines `save_global_event_target_as` and `clear_global_event_target`. | The lowest eligible live country id becomes the persistent founder. A bounded member election replaces an invalid founder. |
| Annex scopes | Offline on-action documentation defines ROOT as the annexer and FROM as the annexed country for `on_annex`. | The dedicated non-periodic on action invokes cleanup in FROM outside Fallout. Fallout rewrite annexations cannot fire founder reports. |
| Opinion cleanup | Official effects documentation defines `remove_opinion_modifier`. | Membership and violation modifiers change only at lifecycle edges. Verification removes all three prior inspection outcomes against the current subject before applying one decaying result. |
| Native embargo ownership | The existing condemnation helpers maintain separate source arrays for condemnation, the Air Cleanliness Treaty, the Great Embargo event, external relations, and system-created relations. | Treaty calls use `constant:condemnation_embargo_source.air_cleanliness_treaty`. Release occurs only when no other tracked owner remains. |
| Air Winter pressure route | Live `air_winter_calculate_state_pressure` subtracts `constant:air_winter_pressure.relief_route` when `air_winter_relief_route` is present. | Convoy arrival sets the exact state flag for up to one hundred eighty days and registers the state for bounded cleanup. The pre-winter pulse removes invalid flags before this calculation. |
| Fallout operational pause | The standard transition sets `fallout_transition_active` before blackout scheduling. The daily Fallout coordinator owns migration recovery while that flag remains set. | Transition and recovery paths call one idempotent treaty pause effect. Monthly call sites do not initialize or reconstruct treaty state after either Fallout flag is present. The pause preserves historical treaty memory while silently cancelling inspections, donor projects, Cleaning Day, invitations, and active relief routes. |

## Coordinator and performance proof

The normal treaty lifecycle adds no periodic entry. It uses `air_contamination_monthly_update`, which is already guarded to one global host. During Fallout transition, the existing daily Fallout coordinator can call only the idempotent treaty pause receipt for migration recovery. The former treaty helper used `random_country`, repeated `every_country`, nested `every_other_country`, and monthly opinion and embargo refreshes. That helper is removed.

The replacement host:

1. initializes schema and reconciles only active routes before the state pass
2. records `global.air_cleanliness_treaty_last_host_date` after the state pass
3. pauses operations during `fallout_transition_active` and `fallout_active`
4. reconciles the member registry and bounded active-inspector registry
5. scans the already bounded Air Winter country registry once every ninety days for invitations and legacy flag repair
6. uses no periodic world-country or world-state loop

Member, violation, verification, convoy, and route removal queues are distinct from their source arrays. No source registry is mutated during its own `for_each_scope_loop`.

## Idempotence receipts

### Formation

- `air_cleanliness_treaty_active` blocks a second formation.
- `global.air_cleanliness_treaty_generation` advances once per formation.
- deterministic candidate selection uses the lowest country id.
- the persistent founder target is committed before invitations.

### Invitations

- each recipient stores `air_cleanliness_treaty_invitation_attempt_generation` before `country_event` emission
- the event validates the current attempt generation at delivery
- `air_cleanliness_treaty_invitation_generation` is written only after the event opens
- acceptance routes through the registration wrapper
- rejection cannot emit another invitation in the same generation
- temporary delivery failure and pending-flag expiry remain retryable on a later bounded scan

### Membership and violation

- registration checks `is_in_array` before adding
- removal loops until duplicate legacy entries are absent
- the banned flag and violator array block repeat violation transactions
- `air_cleanliness_treaty_violation_news_fired` blocks repeat news
- `air_cleanliness_treaty_betrayal_memory` survives current-membership cleanup

### Global Cleaning Day

- a global in-progress flag prevents concurrent starts
- explicit lower and upper contamination bounds plus the irreversible-atmosphere flag block any start or completion whose reduction would be clamped
- the sponsor is stored as a global event target
- each start increments a transaction number
- sponsor transaction and generation values must match global values
- the completion receipt is written before contamination changes
- release clears the lock, sponsor flag, target, and project variables

### Joint Filter Convoy

- the donor can own one active convoy project
- every donor project has one entry in `global.air_cleanliness_treaty_filter_convoy_donors`
- the state can own one reservation
- donor, recipient, state, and generation are frozen at start
- completion revalidates membership, war, state phase, ownership, control, reservation, and generation
- a completed route is added only if absent from the state registry
- project metadata is cleared after either completion or cancellation
- membership loss, recipient annexation, dissolution, schema migration, and Fallout cancel projects through a separate donor work queue

### Verification Mission

- only the persistent founder can sponsor a mission
- the founder can own only one active verification transaction
- both countries store the same generation, transaction, inspector, and subject
- the active inspector is recorded before the mission can survive reconciliation
- exactly one of the travelling, awaiting-response, or pending-result shapes is accepted
- the inspected-member request flag is consumed before one hidden delayed dispatcher is issued
- full access, records only, and refusal use one outcome enum on both countries
- the seven-day result validates the exact paired receipt before writing memory and opinion
- a changed response stockpile opens one recount report without consuming the request or silently cancelling the file
- a separate cancellation queue handles membership, war, annexation, founder, schema, dissolution, and Fallout drift
- completed historical memory survives operational cleanup

## Balance table

| Project | Duration | Start payment | Reserved factories | Result | Cooldown or route |
| --- | ---: | --- | ---: | --- | --- |
| Global Cleaning Day | 45 days | 500 support equipment and 50 convoys | 4 | minus 100 Air Contamination basis points | 180-day global cooldown |
| Joint Filter Convoy | 21 days | 120 support equipment and 20 convoys | 2 | existing mask and clinic ledger values plus a relief route | 90-day donor cooldown and 180-day route |
| Verification Mission | 14 days plus a 7-day result | 60 support equipment and 5 convoys from the secretariat | 1 | full access, restricted records, or refusal memory, decaying opinion, and accepted treaty sanctions | 90-day sponsor cooldown and 180-day subject recency |

The convoy does not change Air Winter phase directly. It uses existing response values, normalization, survival calculation, and the existing relief-route pressure term.

## Static acceptance scenarios

- Severe contamination forms one treaty around the lowest-id eligible founder.
- An accepted invitation creates one membership row and one set of bilateral edges.
- A rejected invitation cannot repeat in the same generation.
- An invitation that fails delivery can retry after its pending window expires.
- Cleaning Day cannot start or complete when either the lower zero bound or atmospheric irreversibility would clamp its advertised reduction.
- Annexing an ordinary member removes its live row and routes.
- Annexing the founder elects the lowest-id valid remaining member or dissolves the treaty.
- An unconventional-weapon violation creates one expulsion, one memory record, one weapon-use report, and sanctions only from current members.
- An inspection refusal creates one expulsion, separate refusal and betrayal memory, sanctions only from current members, and no false weapon-use report.
- No treaty path restores monthly member-to-member or world-country loops.
- A convoy cannot start without stockpiles, a distinct live member target, and a valid Phase 3 or worse priority state.
- A successful convoy spends real equipment, changes the exact named state ledger, recalculates survival, and sets the pressure-consumed route flag.
- State ownership, control, membership, generation, or war drift cancels the project or removes the completed route.
- Only the founder can start a verification mission, and the subject must be a distinct live member at peace with the founder.
- The subject response is stored on both countries before one seven-day delayed result is issued.
- Full access, restricted records, and refusal apply distinct costs, memory, AI, and decaying opinion outcomes without changing Air Winter or Fallout tuning formulas.
- Refusal is a separate treaty violation cause that reuses the existing expulsion, relief-loss, standing opinion, and treaty-owned embargo path without firing unconventional-weapon news.
- Membership, war, annexation, founder, generation, schema, dissolution, or Fallout drift clears the paired inspection transaction.
- Fallout preserves historical membership, inspection, and betrayal memory while clearing operational routes, invitations, and projects without treaty popups.

## Runtime observation gates

Static source cannot prove:

- delayed event delivery and save reconstruction
- exact seven-day Verification Mission result presentation
- regular event-target retention across the delayed verification report
- multiplayer competition for the cleaning-day lock
- targeted-decision FROM persistence across save and load
- native embargo creation and release under By Blood Alone
- timed state and country flag expiry
- mapmode dynamic localisation rendering
- immediate and migration-recovery timing of the Fallout pause receipt
- AI project pacing in a full campaign

These remain observation gates. They are not reported as passing tests.
