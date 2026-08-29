# Event 005/006 Famine and Migration Adapter Owner Handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-25

Owner scope: Event 005 Soviet Collapse and Event 006 Independence Wave owner-side adapter wiring.

Verdict: no gameplay source callsite was patched. The current live owner code does not expose the exact people-denominated state, actor, cohort, and route facts required by the public famine or migration APIs. Adding a call at the available political, release, manpower-cost, or abstract-capacity sites would create a proxy and violate the accepted ownership contract. This handoff is the only file changed by this pass. No commit was created.

## Files and identifiers

### Changed

- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/event005_006_adapter_owner_patch.md` (this handoff only).

### Gameplay files inspected and intentionally unchanged

- `events/005_soviet_collapse.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/on_actions/005_soviet_collapse_on_actions.txt`
- `events/006_independence_wave.txt`
- Existing `006_` scripted effects, scripted triggers, on-actions, and `history/general/006_` source files.

The shared files `common/scripted_effects/chaosx_famine_migration_effects.txt` and `common/scripted_effects/famine_migration_adapter_effects.txt` were read for their public contracts and were not edited.

No event ID, event-pool row, event-pacing pulse, recurring world scan, localisation, asset, workbook, or central famine/migration helper was added.

## Adapter seam ownership

Famine and migration remain separate mechanics joined only by explicit owner adapters.

- Food, security, extraction, ration, and route-food facts belong to the famine seam. A proven Event 005 state and positive people-denominated extraction amount would use the existing `famine_migration_request_food_security_pressure` or source-specific `famine_migration_request_event_pressure` contract with food explicitly enabled and flight explicitly disabled.
- Displacement, cohort, deportation, reception, resettlement, and return facts belong to the migration seam. A proven Event 005 deportation transaction would use `famine_migration_request_deportation_flow` only after origin, destination, positive people amount, actor, policy, border, transport, and safety proof are available. A proven Event 006 reception or return transaction would use the existing reception/return APIs without changing state population merely because a country was released.
- No combined request was made. Neither event currently proves independent famine and migration facts at one live owner callback, so a combined food-plus-flight call would be an invented proxy.
- Deaths remain owned by their original exact cause. No Deaths debit was added, and no movement was represented as a death.

## Event 005 Soviet Collapse census

| Accepted row | Live owner evidence | Adapter result and exact missing fact |
| --- | --- | --- |
| Grain extraction to food pressure | `ukr_soviet_collapse_add_grain_authority` and `ukr_soviet_collapse_apply_total_grain_census` in `common/scripted_effects/005_soviet_collapse_effects.txt` update country-level `soviet_collapse_ukraine_grain_authority` and coercion variables. The actions spend equipment/command resources and some branches select a random owned controlled state for construction. | **API-only.** The source has no stable resolved extraction state, positive people-denominated amount, or responsible actor at the pressure transaction. Grain-authority deltas are political scores, not food people. No famine call was added. |
| Forced-labor quotas and gulag expansion | `soviet_collapse_complete_uwr_prisoner_intake` records `soviet_collapse_uwr_prisoner_intake_state` and a camp evidence flag. The preceding cost effect spends country manpower and equipment (`soviet_collapse_pay_uwr_prisoner_intake_cost`). | **API-only.** The state target and UWR country are present, but the manpower cost is an abstract country resource and does not prove the living civilian cohort placed in the site, its exact amount, or a cohort-aware custody transaction. It cannot safely feed `famine_migration_request_gulag_pressure`, `famine_migration_request_forced_labor_pressure`, or the protected-custody receipt. No call was added. |
| Deportation and forced movement | A source census of all Event 005 owner files found no live deportation-flow producer, exact origin/destination pair, positive people amount, cohort ID, transport proof, or route actor callback. The release helpers only select countries/states and invoke release/setup effects. | **API-only.** The exact movement API remains uncalled. No `famine_migration_request_deportation_flow`, `famine_migration_transfer_civilians_exact`, or movement-death adapter was added. |
| Movement restrictions and trapped population | Event 005 exposes political pressure flags, republic fear, wars, and terminal release stages. These are event-owned political/military state, not a resolved state-local trapped people ledger. | **API-only.** The missing fact is a bounded state, positive trapped amount, and owner/actor proof. No trapped-population registration or displacement pressure was inferred from restrictions or war creation. |
| Republic hunger/deportation memory, concealment, collapse, civil war, and intervention | Current paths write country/global variables, memory flags, evidence flags, release arrays, and war/intervention state. They do not publish a state-local people amount, active cohort, exact route, or actor transaction. | **API-only.** Memory, collapse, civil-war, and intervention context cannot stand in for famine pressure, displacement, reception, or return. No generic event pressure or country-wide scan was added. |

The existing Event 005 grain and release paths therefore remain owner-owned. In particular, `random_owned_controlled_state`, `every_possible_country`, release arrays, and country-level manpower/equipment costs are not valid substitutes for an exact state transaction.

## Event 006 Independence Wave census

| Accepted row | Live owner evidence | Adapter result and exact missing fact |
| --- | --- | --- |
| Country release / refugee inflow | `006_independence_wave_join_on_actions.txt` observes `on_release_as_free` and `on_release_as_puppet`; `independence_wave_release_one_frozen_country` calls the owner release effect; `independence_wave_transfer_frozen_states` changes state owner/controller. | **API-only.** These callbacks prove country transition and ownership transfer only. They do not prove an incoming refugee cohort, exact people amount, origin, destination, route, or reception transaction. No migration transfer or reception load was added. |
| Reception burden and capacity | Event 006 owns abstract country variables such as `independence_wave_capacity`, `independence_wave_security`, and `independence_wave_population_dispute`, initialized from package/territory/archetype constants. | **API-only.** These values are Event 006 political/capacity ledgers, not the shared system's exact people-denominated reception capacity or current load. No `famine_migration_request_reception_capacity` call was added at release or in a generic country hook. |
| Returning co-nationals and return | Event 006 stores former-host relationships, property, population-dispute, border, sponsor, and route ledgers. The release executor has no exact cohort ID, current host, origin state, positive survivor amount, return route, food/safety proof, or acceptance proof. | **API-only.** No voluntary/forced return request was made. A release or host-ledger update is not a return transaction. |
| Damaged food routes and border closure | Current package and bilateral ledgers expose route, border, property, and host outcome state, but no exact famine-state food loss/repair amount plus actor and no exact migration route transaction. | **API-only.** No famine pressure or migration route was inferred from flags, route names, sponsor strength, or property values. |
| Sponsor relief | Planner/executor rows retain sponsor country, sponsorship generation, route, and `independence_wave_sponsorship_opening_strength`. | **API-only.** Sponsorship strength is an abstract Event 006 value, not people-denominated relief or reception capacity. No shared relief or reception request was added. |

The Event 006 release implementation does not call `famine_migration_transfer_civilians_exact`, `famine_migration_apply_destination_credit`, `famine_migration_apply_reception_delta`, or any state population-loss effect. This preserves the required no-duplication rule: a released state keeps its current population, including prior arrivals and losses.

## No-double-counting proof

- No Event 005/006 source file now calls a shared Deaths effect, exact transfer effect, or famine/migration pressure wrapper.
- No original owner death cause was reclassified. Existing camp, forced-labor, famine, route, occupation, and war ownership remains unchanged.
- No release path debits or credits state population, recruitable manpower, or reception load.
- No Event 006 abstract population-dispute, sponsorship, capacity, or force value was converted into people.
- No generic event root, on-action pulse, random selection, or country/state scan was introduced.

## MCP evidence

Mandatory read-only Event MCP inspection/rendering was run before the source census in workspace `mod_chaos_redux_ea3b2d67c2c0`.

### Event 005

- Selector: `chaosx.nr5.1`, `state_flow`, downstream, depth 1, max nodes 20, max edges 40.
- `hoi4.event_inspect`: `EVENT_INSPECTED_PARTIAL`, status `ok`, blocking diagnostics 0, revision `59143acd4a234aef98ca0b6cfbb7b07211d4aa80f99536718b30e126b1deb6f9`, graph hash `05a83fd72cbf3aa808f3f48e2ce14384b2da160472498d76344f3d950a7b0ed6`.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92bbc75e2c3633f0060f7a90ee9b08ebada0cbf0b426451c5563072e41a2e9bd/2cdf3baa7cba68e5d2e8d67aa8aedf4bb48d326d574407a96ceae87787c4733a/event-state_flow-59143acd4a23.json`.
- `hoi4.event_render`: `EVENT_RENDERED_PARTIAL`, status `ok`, blocking diagnostics 0, same revision/hash; large-workspace inline-source truncation/deferred validation was informational only.
- Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e588a9451beb0d99d32ccad432d5c70d6ba1f873f82f158c02512e7997bf2c39/83eeefd8088cb2803435e2f3ad3370cdf6a949a5247a1c8c1f09f3e4b9a17596/event-state-59143acd4a23-manifest.json`.
- Render graph: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92ca977ffef222ed74462c003153928667e0699321e2f453cb729258346daaf1/ff887d04459e3311b359ddbae52d394241ed1fc5d564dfcf5dfaf2cc0671b34e/event-state-59143acd4a23.json`.

### Event 006

- Selector: `chaosx.nr6.1`, `state_flow`, downstream, depth 1, max nodes 20, max edges 40.
- `hoi4.event_inspect`: `EVENT_INSPECTED_PARTIAL`, status `ok`, blocking diagnostics 0, same revision/hash as Event 005.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db9166516169b5bf4460244054e98f6c09d41a470c02832725202af0cbbe43a1/6d5d953fbdfb4aad793c42a1b782cef905135b08b925b6f6a139f4e5cce2d732/event-state_flow-59143acd4a23.json`.
- `hoi4.event_render`: `EVENT_RENDERED_PARTIAL`, status `ok`, blocking diagnostics 0; same large-workspace truncation/deferred validation note.
- Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f422db90f3d02e5bb4ca9d724595beb48f3397e6381ca69aed569846a11994f/d5ac3b22e71251df398810decd7cd27b9ecf515249a08c10a3dafa2fd11a07cd/event-state-59143acd4a23-manifest.json`.
- Render graph: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/097909121094ea43619c23ebdeba4d34cfbbac3d2cf5327a0c3e5b6ff09b6aa3/b432ac56e21b867c22c6be09d71ed110d68564dbffc3c9e445993f95d44e042f/event-state-59143acd4a23.json`.

Because this pass made no Event 005/006 gameplay-source edit, no post-edit event compare was claimed. The docs-only handoff does not change the event graph. The MCP route was available; the only reported limitation was partial large-workspace source expansion with zero blocking diagnostics.

No weighted or probability-bearing helper was changed. Therefore the probability-inspect/auditor/compare route was not applicable; no AI chance, MTTH, random-list weight, or selection weight was modified.

## Validation and remaining blockers

Read-only validation included:

- source census of all accepted Event 005/006 terms and public `famine_migration_*` callsites;
- direct inspection of the exact public pressure, deportation-flow, reception, return, and exact-transfer contracts;
- direct inspection of Event 005 grain, gulag intake, release, and terminal-collapse owners;
- direct inspection of Event 006 release callbacks, frozen country/state execution, sponsorship rows, capacity ledgers, and former-host ledgers;
- required offline wiki pages and vanilla documentation for scopes, event targets, effects, triggers, release/on-action scope, state population, variables, and script constants;
- preservation check showing no scoped Event 005/006 gameplay file was modified by this pass.

The remaining blockers are source-contract blockers, not MCP outages:

1. Event 005 needs an authoritative state-local extraction producer with a positive people-denominated amount and responsible actor.
2. Event 005 needs a cohort-aware gulag/forced-labor intake transaction if custody or pressure is to be recorded; country manpower spend is insufficient.
3. Event 005 needs an exact deportation producer with origin, destination, amount, actor, policy, route, and transport/safety proof before `famine_migration_request_deportation_flow` can be called.
4. Event 005 collapse, civil-war, intervention, restriction, concealment, and republic-memory owners need state/cohort/route receipts; political flags and country wars are not substitutes.
5. Event 006 needs an exact refugee/return cohort and destination-state receipt, including people amount and route/acceptance proof.
6. Event 006 needs an explicit mapping from owner capacity/route/relief facts to shared reception inputs. Abstract `independence_wave_capacity`, sponsorship strength, property, and population-dispute values cannot be passed as people.
7. Any future exact call must be placed after the owning physical transaction and must preserve the existing single population debit/credit and paired reception-load accounting.

No fallback, proxy, hardcoded historical total, generic scan, duplicate state population change, or random event registration was used.
