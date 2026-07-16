# Air Cleanliness Treaty Lifecycle Proof

## Proof boundary

This document records static proof for the restored treaty lifecycle and the first state-targeted Air Winter treaty project. It does not claim runtime acceptance. Hearts of Iron IV was not launched.

The implemented boundary includes deterministic formation, retry-safe invitation receipts, idempotent membership, violation sanctions, founder succession, annex cleanup, an atomic Global Cleaning Day, one Joint Filter Convoy vertical slice, exact active-project ownership, and a silent Fallout pause transaction.

Pooled decontamination, seed archives, evacuation corridors, inspections, votes, major-burner sanctions, and post-Fallout membership policy remain outside this tranche.

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
| Persistent scope arrays | Official effects documentation defines `add_to_array`, `remove_from_array`, `clear_array`, and `for_each_scope_loop`. Official trigger documentation defines `is_in_array`, `any_of_scopes`, and `all_of_scopes`. | Member countries, violator countries, active convoy donors, and active route states are stored in four global arrays. Removal uses separate work queues. |
| Country-array precedent | Vanilla `common/scripted_effects/NORDIC_scripted_effects.txt` builds and iterates a country scope array. Vanilla `common/decisions/TOA_shared_decisions.txt` persists country scopes in a global decision array. | The treaty host iterates `global.air_winter_registered_countries` and `global.air_cleanliness_treaty_members`. |
| Targeted decision scopes | Official decision documentation defines ROOT as actor and FROM as target. Vanilla `common/decisions/AST.txt` uses FROM in completion and removal effects for a `target_array` decision. | Joint Filter Convoy stores and revalidates donor ROOT, recipient FROM, and the recipient's state id. |
| Real equipment payment | Vanilla `AST_supply_arms_to_nation` consumes equipment from ROOT and targets FROM. Existing Air Winter helpers remove exact support equipment and convoy stockpiles. | Both treaty projects call `air_winter_response_pay_support_equipment` and `air_winter_response_pay_convoys` at start. |
| Stored state-id scoping | Existing Air Winter response code stores `air_winter_response_priority_state` and scopes it with `var:<state variable>`. | The convoy copies the exact selected state id, reserves that state, and scopes it again at completion. |
| Delayed country event | Official event effects document `country_event` with a day delay. Offline event documentation requires the trigger to remain true when the delayed event fires. | An attempt generation is stored before emission. Event `.9` validates the pending flag, attempt generation, eligibility, founder, and Fallout state at delivery. A terminal generation is stored only after the event opens. |
| Persistent founder | Official effects documentation defines `save_global_event_target_as` and `clear_global_event_target`. | The lowest eligible live country id becomes the persistent founder. A bounded member election replaces an invalid founder. |
| Annex scopes | Offline on-action documentation defines ROOT as the annexer and FROM as the annexed country for `on_annex`. | The dedicated non-periodic on action invokes cleanup in FROM outside Fallout. Fallout rewrite annexations cannot fire founder reports. |
| Opinion cleanup | Official effects documentation defines `remove_opinion_modifier`. | Cooperation and violation modifiers are added only at lifecycle edges and removed by member departure or annex cleanup. |
| Native embargo ownership | The existing condemnation helpers maintain separate source arrays for condemnation, the Air Cleanliness Treaty, the Great Embargo event, external relations, and system-created relations. | Treaty calls use `constant:condemnation_embargo_source.air_cleanliness_treaty`. Release occurs only when no other tracked owner remains. |
| Air Winter pressure route | Live `air_winter_calculate_state_pressure` subtracts `constant:air_winter_pressure.relief_route` when `air_winter_relief_route` is present. | Convoy arrival sets the exact state flag for up to one hundred eighty days and registers the state for bounded cleanup. The pre-winter pulse removes invalid flags before this calculation. |
| Fallout operational pause | The standard transition sets `fallout_transition_active` before blackout scheduling. The daily Fallout coordinator owns migration recovery while that flag remains set. | Transition and recovery paths call one idempotent treaty pause effect. Monthly call sites do not initialize or reconstruct treaty state after either Fallout flag is present. The pause preserves member and betrayal memory while silently cancelling donor projects, Cleaning Day, invitations, and active relief routes. |

## Coordinator and performance proof

The normal treaty lifecycle adds no periodic entry. It uses `air_contamination_monthly_update`, which is already guarded to one global host. During Fallout transition, the existing daily Fallout coordinator can call only the idempotent treaty pause receipt for migration recovery. The former treaty helper used `random_country`, repeated `every_country`, nested `every_other_country`, and monthly opinion and embargo refreshes. That helper is removed.

The replacement host:

1. initializes schema and reconciles only active routes before the state pass
2. records `global.air_cleanliness_treaty_last_host_date` after the state pass
3. pauses operations during `fallout_transition_active` and `fallout_active`
4. reconciles only the member registry
5. scans the already bounded Air Winter country registry once every ninety days for invitations and legacy flag repair
6. uses no periodic world-country or world-state loop

Member, violation, and route removal queues are distinct from their source arrays. No source registry is mutated during its own `for_each_scope_loop`.

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

## Balance table

| Project | Duration | Start payment | Reserved factories | Result | Cooldown or route |
| --- | ---: | --- | ---: | --- | --- |
| Global Cleaning Day | 45 days | 500 support equipment and 50 convoys | 4 | minus 100 Air Contamination basis points | 180-day global cooldown |
| Joint Filter Convoy | 21 days | 120 support equipment and 20 convoys | 2 | existing mask and clinic ledger values plus a relief route | 90-day donor cooldown and 180-day route |

The convoy does not change Air Winter phase directly. It uses existing response values, normalization, survival calculation, and the existing relief-route pressure term.

## Static acceptance scenarios

- Severe contamination forms one treaty around the lowest-id eligible founder.
- An accepted invitation creates one membership row and one set of bilateral edges.
- A rejected invitation cannot repeat in the same generation.
- An invitation that fails delivery can retry after its pending window expires.
- Cleaning Day cannot start or complete when either the lower zero bound or atmospheric irreversibility would clamp its advertised reduction.
- Annexing an ordinary member removes its live row and routes.
- Annexing the founder elects the lowest-id valid remaining member or dissolves the treaty.
- A member violation creates one expulsion, one memory record, one news report, and sanctions only from current members.
- No treaty path restores monthly member-to-member or world-country loops.
- A convoy cannot start without stockpiles, a distinct live member target, and a valid Phase 3 or worse priority state.
- A successful convoy spends real equipment, changes the exact named state ledger, recalculates survival, and sets the pressure-consumed route flag.
- State ownership, control, membership, generation, or war drift cancels the project or removes the completed route.
- Fallout preserves historical membership and betrayal memory while clearing operational routes, invitations, and projects without treaty popups.

## Runtime observation gates

Static source cannot prove:

- delayed event delivery and save reconstruction
- multiplayer competition for the cleaning-day lock
- targeted-decision FROM persistence across save and load
- native embargo creation and release under By Blood Alone
- timed state and country flag expiry
- mapmode dynamic localisation rendering
- immediate and migration-recovery timing of the Fallout pause receipt
- AI project pacing in a full campaign

These remain observation gates. They are not reported as passing tests.
