# Famine and Migration System Final Completion Audit

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Audit role: read-only `chaosx_event_completion_auditor` completion pass for the shared famine and migration system.

Snapshot captured: 2026-08-24T16:40:08Z.

Completion verdict: **INCOMPLETE — not ready for a completion claim.**

This package is a shared system, not an event. It does not require and must not receive an event ID, event-pool registration, event-log entry, event-details entry, or event pacing count. Event 149 remains retired into this system rather than replaced by another event.

The binding presentation boundary is exactly two dedicated mapmodes: `famine_state_map_mode` and `migration_state_map_mode`. Both exist. No third combined famine-and-migration mapmode exists or is required.

## Snapshot identity and audit limits

The gameplay-source snapshot contains 58 files selected from `common`, `interface`, and `localisation` by the package names `famine_migration` or `famine_and_migration_system`, plus the shared achievement registry, shared state-mapmode file, shared mapmode scripted localisation, shared host on-actions file, and shared mapmode localisation file. The manifest digest is SHA-256 over sorted `relative/path<TAB>per-file-sha256` rows.

- Source file count: 58.
- Source manifest SHA-256: `66834cfb467e838d6039718a590e70619e0adac8887cad6606b364d6cd7b44c4`.
- Latest source timestamp in the set: 2026-08-24 19:22:30 local time.
- Final DDS count in the exact package asset families: 58.
- Asset manifest SHA-256 using the same method: `54370c418afc6f254213c803b68ddba092698f66788d556711b3d0edccfd2500`.
- Latest asset timestamp: 2026-08-24 13:55:42 local time.

This is the deliberately frozen **pre-active-owner snapshot** requested by the parent. Concurrent core, decision, map, constant, trigger, or capacity edits that began after 2026-08-24T16:40:08Z are excluded from this verdict and must be reviewed against this matrix after their owner declares a new freeze. The hash above must not be described as the hash of those in-progress edits.

This audit read all eight spec parts; the decision, integration, death-owner, asset, historical-profile, probability, input, and output matrices; all package prompts, routing, bibliography, manifests, closure review, and `subagent_prompts/11_event_completion_auditor.md`; the entire current package source; the package plans and handoffs; permanent documentation; workbook and exported row evidence; the required offline wiki pages; relevant installed vanilla documentation; and vanilla precedents. No gameplay, localisation, asset, workbook, or generated runtime file was edited by this auditor.

## Executive surface status

| Surface | Status | Evidence and disposition |
|---|---|---|
| Package identity | Complete | Shared system, not an event. No event registration requirement is applicable. |
| Food-security model and stages | Complete in source | The eight-component weighted formula is in `common/scripted_effects/chaosx_famine_migration_effects.txt:3590-3616`; thresholds and recovery hysteresis are in `:3619-3657` and `common/script_constants/famine_migration_constants.txt`. |
| Famine mortality and Deaths ownership | Complete for the famine owner; partial across integrations | `famine_migration_apply_famine_mortality` is at `common/scripted_effects/chaosx_famine_migration_effects.txt:4080-4200`; it performs one physical loss through `apply_exact_state_civilian_population_loss` at `:4191`. Occupation-repression mortality still has no exact external owner receipt. |
| Exact civilian conservation | Strong core, not completion-safe | `famine_migration_transfer_civilians_exact` at `common/scripted_effects/chaosx_famine_migration_effects.txt:1482-1648` reconciles actual debit, route deaths, survivor credit, and residual restoration. Its caller contract does not prove that the physical `FROM` state is the cohort's current host, so a correct primitive can be invoked against the wrong state. |
| Exact food-reserve conservation | Complete in source | The exact reserve debit/credit transfer is at `common/scripted_effects/chaosx_famine_migration_effects.txt:3971-4058`. |
| Cohort identity and movement lifecycle | Critical incomplete | Stale origin/owner selectors, destructive cleanup, missing current-host guards, and cycle/reward defects can duplicate or delete live cohorts. |
| Famine-driven spontaneous flight | Critical missing | The famine stage and mortality paths never submit survivor movement pressure, so famine alone cannot make the spontaneous movement owner reachable. |
| Reception and return | Critical incomplete | Several state/country scope errors and stale-host gates make distribution, reception mission completion, third-country movement, and genuine cross-border return invalid or unreachable. |
| Reception capacity | Critical incomplete | Current decisions manufacture capacity from civilian factories plus a base value; the required live, fail-closed capacity contract is architecture-only in this frozen snapshot. |
| Blockade | Complete in source | `famine_migration_blockade_proven` at `common/scripted_triggers/chaosx_famine_migration_triggers.txt:146-166` is conjunctive: island, isolation, route or port disruption, convoy or escort shortage, no humanitarian corridor, and insufficient local food. |
| Relief routes and stock conservation | Complete within accepted engine limit | Land is donor-backed. Sea and air require a registered positive-stock donor, exact undamaged donor and recipient endpoints, relations/corridor legality, and action-owned logistics. Contract creation precedes conditional cost and debit equals credit. Arbitrary distant sea/air route geometry remains an accepted engine-observability limit. |
| Humanitarian corridor lifecycle | Complete for the implemented contract | A generation-bound transaction receipt guards all three decision gates and the execution helper; the receipt is set atomically after success, the mission does not transfer a second time, and terminal cleanup clears it. |
| Forced movement and custody | Mostly complete | German camp transfer, generic custody, survivor reception, responsible-actor condemnation, and forced-labor proximate Deaths reason are implemented. Occupation-repression remains externally unowned. |
| Ideology influence | Complete in source | Ideology is a bounded modifier applied after safety gates; destination weights are clamped to 0 through 1000. Current scenario impact is not probability-proven. |
| Trapped-border accounting | Critical incomplete | A single border-policy value conflates departure and reception rules, and trapped registration lacks an exact cohort/state/generation receipt, permitting reopen/close farming and ledger drift. |
| Category, report carrier, and phase delivery | Source complete; render unproven | The category is hidden when empty and the compact report carrier is a shared category scripted GUI. All seven report-selector effects have live callsites. This is not a named-event GUI and does not require `chaosx_event_ui_worker`. Current GUI render evidence is blocked by MCP timeouts. |
| Decisions and missions | Partial | Binding census is 26 primary matrix actions plus two ordinary corridor contract responses plus six mission definitions. Delivery priority and current-host resolution are present, but several individual actions remain unreachable or unsafe due to the cohort, flight, capacity, and scope defects below. |
| AI and probability | Blocked and incomplete | All 28 ordinary engine decisions must be included in density/probability review. The current source has no complete named-scenario evaluate/sweep/sequence/simulate or true baseline/current compare. |
| Sparse registries, hooks, and jobs | Partial | The recurring host-only sparse coordinator is present and there is no recurring world scan. Several pending markers have producers but no consumers, and initialization/retirement can destroy valid live data. |
| Historical profiles | Complete in source | All 15 profiles are assigned and reachable through sparse registration/backfill, including the durable Soviet eleven-state and Ireland one-state memory proofs. No fixed deaths or recurring world scan is used. |
| Dynamic modifiers | Incomplete | Required preparing, organized-evacuation, depopulated-district, transit, and return-readiness surfaces are absent; exodus is not scaled by affected population share. |
| Achievements | Partial | All eight IDs, 24 achievement DDS files, sprites, and localisation exist. Identity/generation binding is substantially repaired, but several achievements remain blocked by the movement, return, capacity, and exposure defects. |
| Static visual assets | Complete in files; runtime visual proof partial | All 58 required DDS files exist, are wired, and were checked as 32-bit uncompressed BGRA at the expected dimensions. Current GUI/mapmode dynamic rendering and click-region proof is unavailable. |
| Event 149 retirement | Complete | No Event 149 source exists. The workbook and exports describe it as retired, absorbed into the shared system, unavailable as a random event. |
| Permanent documentation and workbook | Partial/stale | The Event 149 workbook/export row is correct. Several permanent docs still carry the old 26+3 census, the wrong report metric hierarchy, and obsolete report-carrier status. |
| MCP event, GUI, map, and probability evidence | Partial/blocked | Retained artifacts exist, but required current renders and current-source probability evidence timed out or could not model the dynamic surface. Source-only review is not treated as equivalent evidence. |

## Priority completion defects

### P0 — cohort identity can debit the wrong state and duplicate a live cohort

`famine_migration_record_cohort` at `common/scripted_effects/chaosx_famine_migration_effects.txt:82-130` establishes origin-state and owner-country selectors. `famine_migration_bind_cohort_destination` at `:141-193` and `famine_migration_bind_cohort_destination_forced` at `:205-260` update host and destination and set a selector on the destination, but do not clear the selector from the old origin or host. The later host update at `:1789-1847` changes the persisted host and survivor amount without reconciling the former host selector.

`famine_migration_cleanup_cohort_record` at `:415-450` removes aligned registry rows without clearing every state/country selector. `famine_migration_cleanup_cohort_records_for_state` at `:455-489` deletes any row touching the state as origin, host, or destination and clears only the currently scoped state selector. The country selector reconciler at `:2296-2335` runs only when the country is not already marked ambiguous, counts persisted-owner rows rather than current-host ownership, and therefore cannot repair a persisted ambiguity.

The exact transfer primitive at `:1482-1648` does not assert that its physical `FROM` state equals the cohort row's current host. `fm_third_country_resettlement` selects a state with positive flight at `common/decisions/famine_migration_decisions.txt:3324-3372`, places that state into the transfer origin at `:3395-3405`, and invokes the exact debit at `:3406-3418`. A stale selector can therefore debit the historical origin again after survivors already reside elsewhere. Transit, closure, voluntary return, and forced return share the same class of risk.

Required owner action: implement the accepted action-local exact row selector, require persisted current-host equality inside the transfer helper, clear and rebuild old/new state selectors after every mutation, reconcile persisted-owner and current-host countries, and fail closed on ambiguity or aligned-array mismatch. The architecture exists in `subagent_handoffs/final_cohort_selection_architecture.md`; it is not implemented in this snapshot.

### P0 — state retirement and invalidation delete valid migration obligations

`famine_migration_state_can_retire` at `common/scripted_triggers/chaosx_famine_migration_triggers.txt:238-247` proves only stable food state, no food pressure, and no blockade. The stable/recovered transition calls broad cleanup at `common/scripted_effects/chaosx_famine_migration_effects.txt:3451-3492`. `famine_migration_cleanup_state_registration` at `:2198-2245` unregisters food and displacement state, clears reception state, flight/trapped ledgers, and return/resettlement projections even if unresolved cohorts still refer to the state.

State invalidation and processor/control/nuclear branches at `:4224-4228`, `:4244-4247`, `:4357-4359`, and `:4463-4465` combine cohort deletion with broad runtime cleanup. The state cleanup can delete a row merely because the state is its historical origin while the current host remains valid. `famine_migration_initialize_runtime` at `:11-80` can also clear aligned live arrays when the initialization flag is absent, which is unsafe for a persisted registry requiring schema repair.

Required owner action: split food retirement from migration-obligation retirement, guard migration unregister with an exact obligation census, preserve durable terminal outcome receipts, migrate or validate existing aligned arrays instead of clearing them, and use terminal-only cohort deletion. The registry architecture is documented but not implemented in this frozen snapshot.

### P0 — famine mortality does not create survivor movement pressure

The only live write to both `famine_migration_flight_pressure` and `famine_migration_state_flight_population` is the request application at `common/scripted_effects/chaosx_famine_migration_effects.txt:1111-1117`. Public organized/deportation/spontaneous wrapper APIs exist at `:1169-1178` and `:4537-4607`, and the spontaneous movement effect exists, but the famine evaluator, stage transition, and `famine_migration_apply_famine_mortality` never submit survivor flight.

The spontaneous owner starts from positive flight pressure in `common/scripted_effects/famine_migration_spontaneous_movement_effects.txt:52` and therefore cannot activate from a famine alone. This contradicts the acute-shortage, famine, and catastrophic-famine survivor movement requirements in spec Part 3.

Required owner action: after the stage and mortality transaction commits, submit a once-per-stage-or-crisis movement request derived only from surviving civilians, use the protected floor, and add a generation receipt so repeated evaluation cannot reserve the same survivors twice. Do not reuse Deaths or manufacture a second physical population mutation.

### P0 — paired flight ledgers diverge in decision actions

Decision transfers subtract only `famine_migration_flight_pressure` at `common/decisions/famine_migration_decisions.txt:1721`, `:1777`, `:1919`, `:1972`, `:2114`, `:2171`, `:3167`, `:3418`, `:3614`, and `:3802`. They do not subtract the same actual debit from `famine_migration_state_flight_population`.

The spontaneous movement owner correctly decrements both ledgers by `famine_migration_transfer_actual_origin_debit` at `common/scripted_effects/famine_migration_spontaneous_movement_effects.txt:200-205`. Decision cleanup instead uses negative-value correction rather than a canonical exact-zero reconciliation, so the state remains eligible in some phases after its physical flight reserve was consumed.

Required owner action: one shared exact debit/reconcile helper must subtract the measured physical debit from both ledgers, clamp both, preserve a positive partial residual, and unregister the displacement role only when both authoritative values are exhausted.

### P0 — reception distribution, reception mission, and cross-border return contain scope/reachability errors

`fm_distribute_arrivals` tests state-scoped `famine_migration_reception_load` at `common/decisions/famine_migration_decisions.txt:2754-2769`, but that identifier is maintained on the country through `OWNER` at `common/scripted_effects/chaosx_famine_migration_effects.txt:1941-1962`; the state ledger is `famine_migration_state_reception_load`. The action is therefore not using the live state burden it intends to distribute.

`fm_mission_prevent_reception_collapse` tests country capacity/load inside an `any_owned_state` scope at `common/decisions/famine_migration_decisions.txt:348-362`, so its successful headroom test is not scoped to the country holding those variables.

`fm_voluntary_return` requires the historical origin to be owned and controlled by ROOT at `:3557-3571`, rejecting the genuine cross-border case where refugees are hosted by a foreign country and return to the origin owner. The safe-return mission writes the subject on the origin but later searches ROOT's owned states at `:454-520`, so the same cross-border case cannot activate and complete reliably.

Third-country resettlement, voluntary return, and forced return require positive flight on the acting host state at `:3336-3341`, `:3522-3528`, and `:3689-3694`. A valid receiving host normally carries reception load rather than origin flight pressure, so stale origin selectors become the reachable path. Transit and closure phasing have the same historical-origin/current-host confusion.

Required owner action: resolve the exact current host row first, use state reception load in state scope and country totals in country scope, make return ownership checks relative to host and origin owners, and arm/complete missions from the resolved host-country context.

### P0 — reception capacity is a static factory fallback, not the required live contract

Three decision paths write capacity as a civilian-factory multiple plus a base value at `common/decisions/famine_migration_decisions.txt:2683-2687`, `:2732-2736`, and `:2811-2816`. `common/scripted_effects/chaosx_famine_migration_effects.txt:2014-2028` stores the request but does not maintain capacity after food, shelter, transport, medical, administrative, control, war, outbreak, contamination, or load changes.

This is an unapproved simplification relative to the spec. The exact shelter adapter is absent, exact transport-throughput ownership is absent, and the medical/CBRN substrate needs an explicit owner contract. The accepted architecture requires fail-closed zero/invalid capacity and sparse country/state candidate processing with no world scan; `subagent_handoffs/final_reception_capacity_architecture.md` is plan evidence only in this frozen snapshot.

Required owner action: implement the canonical state and country capacity update contract, direct/synchronized capacity-exhaustion proof, invalidation on every accepted substrate change, and sparse scheduler reachability. Remove the civilian-factory fallback rather than retaining it as a hidden substitute.

## High-severity lifecycle, reward, and contract defects

### P1 — destination cycles and repeat rewards remain exploitable

`common/scripted_effects/famine_migration_cohort_history_effects.txt:45-278` detects a prior destination visit after transfer and returns validity while marking a cycle at `:255-272`; it does not reject the destination before physical movement. Both passes of the weighted destination selector lack a prior-visit exclusion.

`fm_distribute_arrivals` and transit remain repeatable for the same live cohort without a per-cohort/generation completion receipt. `fm_distribute_arrivals` grants positive stability unconditionally at `common/decisions/famine_migration_decisions.txt:2907`, outside the successful selection, transfer, reception-delta, and rebind guards, so an expired timer can pay a reward after no valid delivery. Several arrival/rebind paths likewise do not require a positive measured reception delta before recording success.

`famine_migration_register_trapped_population` at `common/scripted_effects/chaosx_famine_migration_effects.txt:1861-1879` has no exact cohort/state/generation receipt. Reopening and closing a border can re-add the same trapped share and repeat stability or condemnation effects.

Required owner action: reject visited destinations before debit, add one authoritative visit receipt and action-level idempotence receipt, gate every reward and mission arming on exact positive transfer/reception deltas, and make trapped registration reversible and generation-bound.

### P1 — one Border Policy value conflates departure and reception rules

The package uses one `famine_migration_border_policy` value for exit control and intake control. Closing departures therefore also alters reception selection and trapped accounting. The accepted design permits one player-facing supporting metric named Border Policy, but requires separate internal departure-policy and reception-policy contracts.

Required owner action: introduce separate internal proofs and callbacks, preserve a single player-facing Border Policy presentation, and reconcile all trapped, destination, return, and AI consumers to the correct side.

### P1 — war, peace, control, and nuclear reassessment markers are dead contracts

Sparse hooks set `famine_migration_war_reassessment_pending` at `common/scripted_effects/chaosx_famine_migration_effects.txt:4440`, `famine_migration_peace_reassessment_pending` at `:4449`, `famine_migration_control_change_pending` at `:4352`, and `famine_migration_nuclear_reassessment_pending` at `:4457`. No package consumer reads these pending values.

Registration and requeue are useful partial adapters, but they are not state-specific front, siege, return, controller, or nuclear-ring proof. Required owner action: consume the markers through existing sparse registries with exact state contracts or remove and replace the dead values. Do not add a world scan or infer a front state from a country-level war callback.

### P1 — required dynamic modifier states are absent or simplified

The current dynamic modifier file contains the four food stages plus exodus, reception, overcrowding, trapped, and a combined return modifier. It does not provide the required preparing, organized evacuation, depopulated districts, transit, or return readiness states. Exodus is flat rather than scaling by affected population share.

Required owner action: add only the requested distinct state phases, with sparse registration, exact lifecycle ownership, dynamic population-share scaling, icons/localisation, and terminal cleanup. Do not merge them into generic exodus or return labels without a documented approved disposition.

### P1 — condemnation dimensions remain only partially exact

Six wrapper/cause contexts exist, and forced return and violent pushback can pass exact route deaths while deportation correctly records zero route deaths. The system still lacks durable actor/state/extraction-generation proof for deliberate starvation, verified offer and withheld-amount proof for relief obstruction, and suppression/mortality receipt proof for concealment. Generic repeat scaling has no supported authoritative API. Occupation-repression mortality and actor ownership remain external blockers.

Required owner action: wire only exact owner receipts and preserve fail-closed behavior. Do not infer the actor from controller/owner at audit time and do not create condemnation from a generic hazard flag.

## Dead-token and hazard-channel census

The following consumers have no producer in the captured package/repository snapshot.

| Token | Current evidence | Classification | Required disposition |
|---|---|---|---|
| `famine_migration_bombing_active` | Consumers at `common/decisions/famine_migration_decisions.txt:2268`, `:2282`, `:3150`, `:3568`, `:3773` and the destination trigger; no mutator. | Implementable for state safety, externally blocked for attacker attribution. | Replace safety consumers with a reusable state trigger using authoritative `days_since_last_strategic_bombing` and accepted strategic-bombing day constants. Keep bomber identity blocked for condemnation/corridor-attack attribution. |
| `famine_migration_persecution_active` | Ten consumers; no mutator. | Implementable source defect. | Provide an exact, reusable, owner-lifecycle persecution proof and clear it only through its authoritative owner. |
| `famine_migration_route_unsafe` | Seventeen consumers; no mutator. | External-owner blocker. | No universal engine receipt or accepted package owner proves all generic route danger. Preserve fail-closed behavior until exact hazard-specific owners exist. |
| `famine_migration_reception_capacity_exhausted` | One close-border AI consumer at `common/decisions/famine_migration_decisions.txt:807`; no producer. | Implementable source defect. | Derive directly and synchronously from canonical live load and capacity once the capacity contract exists. |
| `famine_migration_relief_humanitarian_policy_active` | Corridor response AI consumers at `common/decisions/famine_migration_decisions.txt:2604` and `:2631`; no producer. | Implementable source defect. | Compare the exact reception-side Border Policy contract; do not invent a fourth displayed metric. |
| `famine_migration_exposure_proven` | Medical reception AI consumer at `common/decisions/famine_migration_decisions.txt:2723`; no producer. | Implementable source defect. | Bind proof to the selected cohort's exact origin outbreak/contamination receipt and generation. |
| `famine_migration_route_damaged` | Nine consumers and one clear at `common/decisions/famine_migration_decisions.txt:1210`; no set producer. | Implementable source defect. | Refresh through the sparse state scheduler from authoritative state `damaged_building_level@rail_way` and only other explicitly accepted substrate; align repair visibility, success, and clear to real damage. |

The bombing classification is deliberately split. The installed engine trigger `days_since_last_strategic_bombing`, already consumed by `common/scripted_effects/fallout_consolidated_effects.txt:2993-3007` with `constant:chaos_meter_deaths.strategic_bombing_days_recent`, `.warm`, and `.hot`, truthfully proves recent ongoing state danger without an attacker. It closes destination and return safety once centralized. It does not prove the bomber, a corridor attack transaction, or a flight amount.

## Requirement-by-requirement evidence matrix

| Requirement | Status | Exact evidence, omission, or blocker |
|---|---|---|
| Eight food-pressure components | Complete | Production 1.15, transport 1.10, extraction 1.25, need 1.00, environment 0.80, vulnerability 0.90, governance 0.95, relief 1.20, normalized by 7.15 at `common/scripted_effects/chaosx_famine_migration_effects.txt:3590-3616`. |
| Five visible food stages | Complete | Stable plus acute shortage, famine, and catastrophic escalation thresholds 25/50/75/100 and recovery thresholds 20/40/60/80 at `:3619-3657`. |
| Famine mortality formula | Complete in owner | Population, rate, exposure, vulnerability, access/extraction, environment, governance, and relief feed the single mortality transaction at `:4080-4200`. |
| Exact Deaths ownership | Complete for famine and route transfer | Famine calls `apply_exact_state_civilian_population_loss` once. Route deaths are separated from survivor transfer and logged with no second state population mutation. Forced-labor selects `forced_labor` before the existing single state-loss/Deaths call. |
| Exact civilian conservation | Partial | The primitive conserves measured debit, route deaths, survivors, and residual, but caller host identity is not protected. |
| Exact food-stock conservation | Complete | Donor debit equals recipient credit; no local-reserve duplication fallback. |
| Voluntary displacement | Critical incomplete | Public contracts exist, but famine survivor flight has no caller and host identity is unsafe. |
| Organized evacuation | Partial | Decision/corridor APIs exist and exact transfer works; paired flight reconciliation and current-host binding are incomplete. |
| Deportation/forced transfer | Mostly complete | Exact cohort transfer, survivor reception, responsible actor, and once-only condemnation are implemented; generic persecution and route danger inputs remain incomplete. |
| Spontaneous movement | Mechanism complete, reachability incomplete | `famine_migration_spontaneous_movement_effects.txt` reconciles both flight ledgers, but famine never supplies the request. |
| Return | Critical incomplete | Local return mechanics exist; genuine cross-border ownership and mission scopes are wrong, safety flags are dead, and current-host resolution is unsafe. |
| Reception | Critical incomplete | Burden registration exists; distribution and mission scope are wrong, capacity is a fallback, and exact exposure gating is absent. |
| Trapped borders | Critical incomplete | Trapped variables and decisions exist; exit/intake policy is conflated and repeated trapped registration lacks a receipt. |
| Conjunctive blockade proof | Complete | Exact six-part trigger at `common/scripted_triggers/chaosx_famine_migration_triggers.txt:146-166`. |
| Relief delivery forms | Complete within accepted engine limit | Land, sea, and air delivery use donor stock and exact endpoints; invite is land-only. Arbitrary distant path geometry is not observable. |
| Corridor attack proof | Partial by engine surface | Naval, paradrop, nuclear, project raid, border-war, biochemical, and operative receipts exist. Ordinary land combat and generic strategic bombing do not expose exact attacker-target corridor attribution to this package. |
| Corridor replay safety | Complete | Same-generation receipt at three gates and helper, post-success set, mission no second transfer, terminal-only clear. |
| Ideology bound | Complete in source | Post-safety bounded modifier, clamped final weight. Probability effect remains unproven. |
| Hidden/phased category | Complete in source | `visible_when_empty = no`, context phases, report header, and response priority exist. |
| Primary decision count | Complete | Exactly 26 binding matrix actions. |
| Contract response count | Complete | Exactly two auxiliary ordinary decisions: `fm_accept_corridor_offer` at `common/decisions/famine_migration_decisions.txt:2592` and `fm_reject_corridor_offer` at `:2615`. |
| Mission count | Complete | Six definitions at lines 46, 121, 183, 258, 331, and 454. Permanent docs remain stale at three missions. |
| AI valid paths | Partial | Each primary decision has AI logic and the airlift factor is positive, but dead tokens and unreachable actions create invalid paths. |
| AI density and probability evidence | Blocked | Current source has no complete named-scenario probability pass or genuine baseline/current compare. |
| Sparse recurring runtime | Complete structure | Host-only daily coordinator at `common/on_actions/chaosx_on_actions_chaos_meter.txt:10-27`; sparse runtime processor at `common/scripted_effects/chaosx_famine_migration_effects.txt:4314-4343`; no recurring world scan. |
| Sparse lifecycle correctness | Critical incomplete | Initialization, retirement, pending markers, and selector reconciliation can clear or strand live obligations. |
| Report selector reachability | Complete in source | All seven requested selector effects have package callsites: generic famine, island blockade, wartime evacuation, nuclear evacuation, closed border, relief arrival, and return. |
| Historical profiles | Complete | Fifteen CSV profiles, valid ID trigger at `common/scripted_triggers/chaosx_famine_migration_triggers.txt:272-286`, assignments at `common/scripted_effects/chaosx_famine_migration_effects.txt:647-805`, and resolver/application at `:2941-3351`. |
| Soviet and Ireland historical memory | Complete | Durable sparse backfill registers eleven Soviet states and one Ireland state; profile-specific triggers replace dead generic consumers while retaining live owner/controller and positive-pressure gates. |
| Event 149 retirement | Complete | No event source. Workbook/export row marks it retired and unavailable; no replacement event is allowed. |
| Eight achievements | Partial | All definitions at `common/achievements/chaos_redux_achievements.txt:3850-3887`; several runtime paths remain blocked below. |
| Achievement static assets | Complete | Eight normal, eight grey, and eight not-eligible DDS files, with sprite and localisation wiring. |
| Decision/report/state assets | Complete | Seven report images, one category icon, one category picture, ten decision icons, nine state modifier icons, four mapmode button DDS files, and two Deaths texticons. |
| Exactly two mapmodes | Complete | `famine_state_map_mode` at `common/map_modes/chaosx_state_map_modes.txt:390`; `migration_state_map_mode` at `:487`; no third combined mode. |
| Mapmode dynamic runtime proof | Blocked | Map substrate rendered, but installed map route does not render scripted colors/tooltips and current hardcoded `mapmodes` GUI artifacts are unavailable. |
| Permanent system documentation | Stale | Current facts are not fully promoted; see documentation section. |
| Workbook/export alignment | Complete for Event 149 | `.xlsx` is the editable source. Event 149 export wording matches retirement. No synthetic shared-system event row is required. |

## Cross-system adapter matrix

| Required owner/surface | Status | Current exact disposition |
|---|---|---|
| Deaths | Strong partial | Exact famine, route, custody, and forced-labor calls exist. Occupation-repression mortality has no exact owner receipt. |
| Air Cleanliness | Partial | Exact food-pressure adapter exists. Survivor flight/evacuation input is absent. |
| Condemnation | Partial | Exact wrappers exist for some transactions; starvation, obstruction, concealment, repeat scaling, and occupation actor proof remain incomplete. |
| Camps and genocide | Partial | Food pressure, forced movement, custody, and Deaths are exact. Escape, liberation, and broader movement/return contracts are incomplete. |
| Occupation | Partial | Twenty-five laws/profile mappings exist. Transition actor/amount and repression mortality are blocked. |
| Chemical warfare | Partial | Exact food aftermath exists. Survivor flight and safe-return inputs are absent. |
| Biological/outbreak | Partial | Black Plague food adapter exists and nonhuman incidents are excluded. Ordinary biological exposure and exact cohort-origin exposure are missing. |
| Nuclear | Partial | Native nuke callback supplies food/report/corridor attack and covers Event 28. Survivor flight and ring-specific movement are incomplete. |
| Strategic bombing | Partial | Authoritative recency can prove state safety danger but is not wired. Bomber identity and exact flight amount are unavailable. |
| Natural disasters / Event 13 | Partial | Exact food adapter exists. Evacuation, displacement, reception, and return survivor inputs are incomplete. |
| War/front changes | Partial | Sparse country hooks exist. Exact state/front/amount proof is unavailable and pending markers are dead. |
| Peace | Partial | Sparse hooks and explicit return exist. Generic state proof is absent and cross-border return is defective. |
| Event 5 | Missing exact adapter | No exact package callsite with state, amount, cohort, actor, and replay receipt. |
| Event 6 | Missing exact adapter | No exact package callsite with required owner facts. |
| Event 14 | Intentionally distinct/partial | Cannibal/prisoner-feeding semantics are not ordinary famine and must not be generically remapped; no exact broader movement contract exists. |
| Event 15 | Missing exact adapter | No exact package callsite with required owner facts. |
| Event 20 | Partial | Concrete Black Plague integration only. |
| Event 21 | Missing exact adapter | No exact state/amount/actor transaction. |
| Event 28 | Complete through native hook | Correctly covered by `on_nuke_drop`; no duplicate event call is required. |
| Event 33 | Missing exact adapter | Continent/random-state modifiers do not provide a positive per-state amount, actor, cohort, or replay receipt. |
| Event 50 | Partial | Embargo registration exists; dependency/shortfall amount is not proven. |
| Event 95 | Partial | Control transfer is observed; no exact famine or movement amount is produced. |
| Event 118 | Blocked/absent | No source event exists to own an adapter. |
| Event 120 | Blocked/absent | No source event exists to own an adapter. |
| Event 131 | Blocked/absent | No source event exists to own an adapter. |
| Event 149 | Complete retirement | Absorbed into the shared system; no event source or adapter required. |
| Disease cluster | Partial | Concrete plague path only; no exact general cluster dispatcher. |
| Natural-disaster cluster | Partial | Concrete Event 13 food path only. |
| Liberations cluster | Missing | No exact reverse-flow, exposure, or return owner contract. |
| Special classifiers | Complete | Nonhuman and semantically distinct cases fail closed rather than fabricating famine or migration. |

Missing adapters are not permission to invent amounts or actors. They remain implementable only in the upstream owner once the owner can expose exact state, cohort/amount, cause, actor where required, and a replay-safe transaction receipt.

## Achievements status

| Achievement | Overall status | Evidence |
|---|---|---|
| Break the Blockade | Partial | Same-state and same-generation receipt is implemented. Native/project attack disqualifiers are present. Ordinary land-combat and strategic-bomber attribution remain external engine-owner gaps. |
| No One Left at the Gate | Partial | Exact crisis nonce and qualifying cohort set are implemented. It still depends on correct current-host selection, trapped accounting, and non-destructive cleanup. |
| Roads Home | Incomplete | Same-cohort binding is implemented. Genuine cross-border return is currently blocked by ownership/scope logic. |
| Bread Across the Front | Partial | Native and project corridor attack receipts exist; no fabricated generic attack owner is used. Probability/AI delivery remains unproven. |
| The Hungry Were Not Contagious | Incomplete | The generic medical reception recorder at `common/scripted_effects/famine_migration_achievement_effects.txt:1081-1085` can mark outbreak exposure from the arrival action rather than an exact selected cohort-origin receipt. The dead `famine_migration_exposure_proven` AI input confirms the missing binding. |
| A Place at the Table | Incomplete | Receiving-state food-safety binding exists. Current-host selector and dynamic capacity defects still obstruct truthful reachability. |
| The Grain Stayed Home | Complete | Extraction-suspension transaction and state/crisis binding exist. |
| The Country Did Not Empty | Partial | Startup identity baseline and simultaneous war/famine/displacement/threatened-share generation proof exist. It still depends on the accuracy of flight and cohort ledgers. |

The identity/generation closure at `subagent_handoffs/achievement_identity_generation_closure.md` is accepted. It does not close the underlying movement, reception, return, or exposure contracts, so the achievement surface remains partial overall.

## Decision, mission, category, and report census

The engine file contains 28 ordinary decision definitions. The binding design census is exactly 26 primary decision-map actions plus the two corridor counterpart responses `fm_accept_corridor_offer` and `fm_reject_corridor_offer`. Those two responses are required ordinary decisions for the offer lifecycle but are not extra primary decision-map rows. The same file contains six mission definitions. Probability and decision-density audits must include all 28 ordinary decisions and all six missions.

The six missions are `fm_mission_secure_relief_route`, `fm_mission_hold_humanitarian_corridor`, `fm_mission_protect_evacuation_transport`, `fm_mission_deliver_relief_before_reserves_fail`, `fm_mission_prevent_reception_collapse`, and `fm_mission_prepare_safe_return_route` at `common/decisions/famine_migration_decisions.txt:46`, `:121`, `:183`, `:258`, `:331`, and `:454`.

The latest decision phase resolves a live cohort for a country when the country is either the persisted owner or the current host-state owner, requires valid origin/host/destination scopes, and no longer depends on the obsolete permanent ambiguity gate. Evidence is `common/scripted_effects/famine_migration_decision_phase_effects.txt:17-120`. This closes the prior foreign-host category-delivery defect, but the phase still trusts incorrect persisted host/selector lifecycle data.

The report carrier is a shared category scripted GUI and not a named event-owned mechanic window. No `chaosx_event_ui_worker` handoff is required. All seven image selector effects have real callsites. The final runtime view remains unproven because the latest GUI inspect/render attempts timed out.

## AI and mandatory probability evidence

The dedicated final handoff is `docs/plans/famine_and_migration_system_plans/subagent_handoffs/ai_probability_final_audit.md`. Its conclusion is binding for this audit: current-source AI balance is not proven.

The completed decision-source inspections found 28 candidates in a score-only model rather than normalized choice probabilities:

- Discovery artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee5dd83f47cf589cf1de1d96b68931a20a1c349e41a3a3b97c8d143cb53ef507/096805e177cb7920a229d0a445b884edd44ab4c8f02a60e43ad27ec68ec3264f/probability-inspect-187e663a01be.json`.
- Explicit artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4300a2d0f084e56ce212c7a1c6592d1b40a38ec30f3558c9ab2c327b81fe2231/9150ff8e690facbd8aaf5fc765330f38a54c1fe737e315f672deafe36bffeabb/probability-inspect-187e663a01be.json`.

Those artifacts predate the captured source hashes. The narrowed refresh timed out after 180 seconds. No fresh current-source `probability_evaluate`, `probability_sweep`, `probability_sequence`, `probability_simulate`, or genuine baseline/current `probability_compare` was completed.

The destination, relief-donor, corridor-helper, and shared-effects custom pool inspections returned incomplete/zero-candidate models:

- Destination: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35a7c0739df0654d46bea8c3f2aa9054558010106c0984bd40a0aa3ab5c6a41f/f61e0c0e5da85b3d88de8f945c83f5a727ddb854fd669bccee2be1a2f7ab2fc7/probability-inspect-95d51b3eb64a.json`.
- Relief donor: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c95af4bfbe8b094ae6aed14dad557024c3d2a7c40fb187d35338ce9285d3dbcd/94d062edba52ea66f3ce9f2feda32e2b0afea43000ed614350288be616f7f4b2/probability-inspect-40b35335ef2b.json`.
- Corridor helper: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/774634e79bc1db0a40018279615b0f4f391b2da5f15f06478cd226ec074cba08/58aa07926aff72a39bfb641df0b141273df2ce53e5273107181fb1a1fa3d0c6e/probability-inspect-3e2e9b28b297.json`.
- Shared effects: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b84ae289134e1be68ad17fc77f20cb8bca7473fb490cc504909e919008242701/0fd8ac04bcb6bee84c7968c6647c6f780df48aab6f4e40ba494340090b7f5eaa/probability-inspect-1036274a63eb.json`.

The historical 20-scenario evaluation used source hash `c874297e02df691eda7e9bea00a87d1352e3f9a60b5c747573d493d79ce8bb3d`, produced 520 rows with 59 unresolved inputs, and is stale. Its current/current comparison is not a baseline/current comparison. No named scenario is exact, bounded, sampled, or accepted for this snapshot. The adapter cannot currently resolve the nested `FROM` and target objects needed for route, destination, donor, cost, capacity, ideology, exposure, stock, cooldown, and terminal inputs.

Static source review confirms the high-air-experience airlift factor is positive rather than inverted. This is not scenario-impact evidence. Dead inputs such as capacity exhaustion, humanitarian policy, and exposure proof also make some AI branches non-truthful before any numeric tuning.

Completion requires a new current-source inspection after gameplay contracts settle, all twenty named scenarios from the CSV, custom pool evidence, sequence/cycle cases, and a genuine same-scenario baseline/current comparison for every probability-bearing patch.

## Mandatory event, GUI, and map MCP evidence

This shared system has no event root to inspect. Event MCP applies only to integration events whose sources were inspected as owner surfaces; it is not grounds to invent a system event.

Retained successful/partial event evidence includes:

- Event 13 narrow lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f89418f265e9f7d09065973030fcfdfbff1ef691019802a2d6161557aa25d5b/a2caa38e79f0b7727c9a7600737e3827302d4a94ea8c7e4f9c6d13c0c8ebfe4d/event-lint-655620ee867d.json`.
- Event 18 narrow lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acb0e308c9745f7ea9faabff139f69ec82d9a95de0572d51457ea16fb8e0c13e/a274d0fe3a4beceb722c1ca4343caf625fabce1c4eda3366f829ade00809b87a/event-lint-655620ee867d.json`.
- Event 19 state-flow receipt evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c412babbd400c173d2d74f32dae0f3f9442cc138a13c6e02113bbd08b9bc4579/d9a659058d57b12e710bb85447f9a581b4c39fbada1eb7a8deeaf39fb8e7b95d/event-state_flow-655620ee867d.json`.

Event 19 and Event 11 post-edit inspections timed out after 180 seconds, and the matching Event 19, Event 18, and Event 11 renders timed out. Narrow final audit attempts for Events 5, 6, 14, 15, 20, 21, 28, 33, 50, 95, 118, 120, 131, and 149 also timed out at 180 seconds where a root was requested; Events 118, 120, 131, and 149 have no source root. Event compare also timed out. These are exact MCP route blockers, not source completion evidence.

The retained report-header GUI evidence is:

- Inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9410b7bf900fabf1baa9c56db70787eb3a4e36ffe9f8f7d9badde586efe0f54/b3cbc23f8b96415c4f0a732e65c312f69afe75f72384a5b9e55e153e705c3952/gui-inspect.c159fc5d62130b30.json`.
- Render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb1f19a21bbec4ecdbb9717a41d0a34b45c1cc68bc2bd527f30e4aa725588d37/df9f59d4ecc363ba846230814ce41e9c3fc515eed4bdcb46add8cda63dca69a5/famine_migration_report_header_window-full.svg`.

Fresh final report-header GUI inspect/render attempts timed out after 180 seconds. The decision-view inspect succeeded but modelled zero exact elements and one approximated element, so it is not layout proof: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/917b4c2cca6f21dcba8b04139b87732ba05ab211717ac0c874bfd7b945f2a6e4/07adee513c78646fec1ff57d7d65b2087a5c4b7511409ffac9c7a594299d8b10/gui-inspect.b2aa2cbd2ef811a.json`.

The map substrate inspect succeeded for relevant states and is retained at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6957bfb217fc3705f617c9e630721b50d8ba690e22f3ca6a168b9e136408271/284bf98a3a9ac115976ca90a5caf0815c18713e4ac231b6a08d6c6d2c6abe398/map-inspect.a672f4ba67035c47.json`. `docs/plans/famine_and_migration_system_plans/mapmode_validation.md` records a successful state-layer render at revision `080b7a870be68fd95ec8ed8cb464c2508b35d6b41abb1ea8c43f28a32c779841`. That proves the state/coast/port/supply-node/railway substrate only. The installed map renderer does not render dynamic scripted-mapmode colors or tooltips, and the final hardcoded `mapmodes` GUI responses did not expose linked payloads. Button states, scripted colors, tooltips, and click regions therefore remain unproven.

## Static assets and localisation

The exact 58-DDS inventory is:

- 24 achievement DDS files: normal, grey, and not-eligible for eight achievements.
- Seven report images under `gfx/event_pictures/famine_and_migration_system`.
- One category icon and one category picture under `gfx/interface/decisions/famine_and_migration_system`.
- Ten decision icons in the same directory.
- Nine state modifier icons under `gfx/interface/state_modifiers/famine_and_migration_system`.
- Four mapmode button DDS files, selected and deselected for each of the exactly two mapmodes.
- Two Deaths texticons.

All were present, registered, consumed, and inspected as 32-bit uncompressed BGRA DDS files at the intended dimensions. Achievement sprites and localisation exist for all eight IDs. Decision, mission, report, stage, mapmode, and Deaths localisation coverage is present in source.

Current visual-layout proof remains partial because the latest GUI and dynamic mapmode renders timed out or returned no accessible payload. No character portrait, custom 3D unit, unit audio, counter, focus tree, formable, super-event, or named-event-owned GUI is part of this shared system, so those specialist completion contracts are not applicable.

## Historical profiles

The historical profile CSV contains exactly 15 profiles. `famine_migration_historical_profile_id_valid` recognizes all IDs at `common/scripted_triggers/chaosx_famine_migration_triggers.txt:272-286`; assignment is at `common/scripted_effects/chaosx_famine_migration_effects.txt:647-805`; resolution/application is at `:2941-3351`.

The durable Soviet eleven-state and Ireland one-state memory proofs are set only through sparse anchor registration/backfill. Four dead generic memory consumers were replaced with profile-specific triggers, and the live owner/controller plus positive food-pressure gates remain. The source does not use a fixed Deaths value or recurring world scan. The prior memory-reachability defect is closed.

## Accepted-plan disposition

| Plan or handoff | Disposition at snapshot |
|---|---|
| Historical profile memory reachability | Implemented and accepted closed. |
| Relief donor architecture / FM-R05 | Implemented and accepted closed within the documented route-geometry engine limit. |
| Corridor native/project attack receipts | Implemented and accepted for available exact owners; ordinary land combat/generic bombing attribution remains blocked. |
| Corridor generation/replay receipt | Implemented and accepted closed. |
| Forced movement survivor reception and actor condemnation | Implemented and accepted closed for the owned transaction. |
| Generic camp custody owner | Implemented and accepted closed. |
| Forced-labor Deaths reason | Implemented and accepted closed; occupation repression remains blocked. |
| Host resolution and decision phase delivery | Implemented and closes the legacy category-delivery defect; still depends on broken cohort ledger identity. |
| Achievement identity/generation closure | Implemented and accepted for its bounded identity work; dependent movement/reception/exposure blockers remain. |
| Final cohort selection architecture | Accepted architecture only; not implemented. |
| Registry reconciliation architecture | Accepted architecture only; not implemented in the frozen snapshot. |
| Final reception capacity architecture | Accepted architecture only; not implemented in the frozen snapshot. |
| Hazard channel owner map | Audit/architecture only; implementable dead-token items remain open and external blockers remain explicit. |
| Final cycle exploit audit | Audit only; preflight visit exclusion, no-repeat receipts, reward guards, and trapped reconciliation remain open. |
| Condemnation owner/scaling map | Partial implementation; unresolved owner dimensions remain. |
| Improvement-loop final review | Audit/addendum only; open requirements in this report remain unpromoted. |
| Documentation curator | Deferred intentionally until gameplay freeze; permanent docs remain stale. |
| AI probability final audit | Completed as an audit with an incomplete/blocked verdict; no current-source probability acceptance. |

No accepted architecture-only handoff should be described as implemented merely because its design exists.

## Permanent documentation, workbook, and Event 149

`docs/famine_and_migration_system/source_of_truth_map.md:25` still describes 26 decisions and three missions. The correct binding census is 26 primary matrix actions plus two corridor contract responses plus six missions.

`docs/famine_and_migration_system/completion_report.md:19` still describes Food Security as the primary report metric and Displacement/Reception as supporting metrics. The accepted presentation contract is primary Displacement Load with supporting Reception Capacity and Border Policy. The same report still says 26 decisions and three missions at line 21 and repeats three-mission localisation coverage near line 54.

The permanent system documentation still labels the report carrier as an unresolved FM-R2 conflict near `docs/famine_and_migration_system/famine_and_migration_system.md:214`, although the shared category carrier and all seven selector callsites now exist. `docs/famine_and_migration_system/handoff_dispositions.md` also retains stale three-mission and missing-report/achievement statements.

The workbook source `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and its export rows correctly classify Event 149 as retired and absorbed into the shared dynamic famine and migration system, unavailable as a random event. No system event row, event-log row, details row, or pacing count should be added.

Required curator action after gameplay freeze: promote the exact two-mapmode rule, 26+2+6 census, accepted report hierarchy, shared-system/non-event boundary, final plan dispositions, current asset status, all remaining blockers, and this completion verdict into permanent docs. Then update the workbook only if an existing player-facing row changes and regenerate exports from the workbook rather than editing CSV files.

## Simplifications, omissions, and blockers

### Implementable source defects

1. Exact current-host cohort selection, transfer guard, and old/new selector reconciliation.
2. Split food retirement from unresolved migration-obligation cleanup and make initialization schema-preserving.
3. Famine-stage survivor flight submission with once-per-generation reservation proof.
4. Paired flight-ledger exact debit and zero/unregister reconciliation.
5. Correct reception state/country scopes, cross-border return ownership, and host-based decision/mission phasing.
6. Live fail-closed reception capacity with sparse invalidation and no civilian-factory fallback.
7. Preflight destination-history exclusion, per-cohort action idempotence, positive-delta reward guards, and trapped receipt reconciliation.
8. Separate internal departure and reception policy contracts while retaining one player-facing Border Policy metric.
9. Consume or truthfully replace war, peace, control, and nuclear pending markers through sparse registries.
10. Add the missing requested dynamic modifier phases and population-share scaling.
11. Wire state bombing danger from authoritative strategic-bombing recency, exact persecution lifecycle, capacity exhaustion, humanitarian policy comparison, cohort-origin exposure, and authoritative railway damage.
12. Finish exact adapter owners only where upstream state, amount/cohort, actor, cause, and replay receipts can be produced.

### External engine or owner blockers

1. Exact attacker-target attribution for ordinary land combat and generic strategic bombing corridor attacks.
2. A universal `route_unsafe` proof spanning all hazard types.
3. Exact state/front/amount ownership from generic country-level war and peace callbacks.
4. Occupation-repression mortality and responsible-actor receipt.
5. Arbitrary distant sea/air route geometry beyond the accepted endpoint/logistics contract.
6. Absent source owners for Events 118, 120, and 131.

### Tool/runtime evidence blockers

1. Current event inspect/render/compare calls repeatedly timed out at 180 seconds for most adapter events.
2. Current report-header and mapmode GUI inspect/render calls timed out or returned no linked visual payload.
3. The map renderer proves only substrate, not dynamic scripted-mapmode colors, tooltips, or click regions.
4. Current-source probability inspection timed out, custom pools were not modelled, nested scenario scopes remained unresolved, and no true baseline/current comparison exists.
5. Repository policy reserves live game validation to the user; this auditor did not launch the game and makes no runtime-success claim.

## Recommended completion order

1. Land the cohort/current-host and registry/retirement contracts first; every later movement, achievement, and AI result depends on trustworthy identity.
2. Add famine survivor flight and central paired-ledger reconciliation.
3. Repair reception/return scopes, dynamic capacity, departure/reception policy separation, and trapped idempotence.
4. Add preflight cycle exclusions and gate every reward, mission arm, achievement write, and terminal cleanup on exact transaction receipts.
5. Close the implementable hazard/dead-token inputs and consume the sparse reassessment markers.
6. Re-audit all 26 primary actions, two responses, and six missions for reachable player and AI paths.
7. Run the dedicated current-source twenty-scenario probability audit and genuine same-scenario comparisons.
8. Rerun required event, GUI, and map MCP routes; retain exact blockers if the installed tools still cannot render the dynamic surfaces.
9. Have the documentation curator promote the final frozen facts and dispositions, then perform one final read-only completion audit against a new source manifest hash.

## Final determination

The package has a substantial and often exact core: weighted food stages, single-owner famine mortality, exact population and reserve conservation primitives, conjunctive blockade proof, donor-backed relief, generation-safe corridors, forced movement/custody receipts, all 15 historical profiles, all eight achievement definitions and static assets, a hidden/phased shared category, Event 149 retirement, and exactly the two required mapmodes.

It is nevertheless **incomplete** because current-host cohort identity can be stale, retirement can delete live obligations, famine does not generate survivor flight, paired flight ledgers diverge, reception and cross-border return contain scope errors, capacity is a static fallback, cycles and rewards are not fully idempotent, several adapter/dead-token contracts are unowned, permanent documentation is stale, and mandatory current-source probability and runtime visual evidence are blocked. These defects affect physical population conservation at caller level, valid player and AI reachability, achievement truthfulness, and cleanup safety; they are not optional polish.
