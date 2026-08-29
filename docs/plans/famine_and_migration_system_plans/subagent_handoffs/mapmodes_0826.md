# Famine and Migration Mapmode and Decision Audit Handoff

Date: 2026-08-26.

## Scope and verdict

This is a read-only audit of the separate famine and migration decision categories, their decisions and missions, and the two dedicated scripted state mapmodes.

No gameplay source, AI weight, mapmode, GUI, GFX, or localisation source file was changed by this audit.

The current source keeps exactly two dedicated famine/migration mapmode definitions, `famine_state_map_mode` and `migration_state_map_mode`.

The unrelated existing `deaths_state_map_mode`, `contaminated_states_map_mode`, and `air_winter_state_map_mode` are not famine or migration mapmodes.

The categories remain separate and independently gated, with no combined runtime category, mapmode, full GUI, or gameplay world scan introduced.

Dynamic custom-mapmode colour, tooltip, selected-button, and live click evidence remains unavailable through the installed MCP routes, so this handoff does not claim runtime completion.

## Issues sorted by severity

### Blocker: dynamic mapmode execution is not available

`hoi4.map_inspect` and `hoi4.map_render` inspect and render the base state/map substrate, but they do not execute the custom scripted `color` branches or scripted mapmode tooltip branches.

`hoi4.gui_inspect` and `hoi4.gui_render` resolve the hardcoded `MapmodesInterface_Ingame` button-window shell, but the accepted scenario cannot inject an active custom mapmode.

The parent-supplied `selectedMapMode` scenario field was rejected as unrecognized, which confirms that an active custom-mapmode state cannot be injected through the current scenario contract.

This is an MCP capability boundary, not evidence that either source mapmode is absent or that its Clausewitz branches execute incorrectly.

### High: migration role projections need owner/runtime confirmation

The migration mapmode reads state-local role flags and persisted projections for trapped, overcrowded, evacuation, exodus, preparation, reception, return, and resettlement presentation.

The current validation record notes that `migration_reception_context_active`, `migration_overcrowded_context_active`, and `migration_return_context_active` have no setter in the inspected shared decision/effect sources, and that durable state-local cohort destination/status projection is incomplete.

Until the accepted transaction owners write those projections, the corresponding map colours and role text can fail closed or remain neutral even though the mapmode definition is structurally valid.

This requires an owner-level ledger/projection decision and is not a safe small local patch for this audit.

### Medium: migration action-density proof is incomplete

The source contains 28 weighted actions and six missions in total, with 10 famine actions, two famine missions, 18 migration actions, and four migration missions.

Famine response selectors mutually suppress overlapping reserve, maritime, evacuation, concealment, and safer-state siblings, and the completion report records a maximum of six valid famine primary responses.

Migration actions are individually state-targeted and gated, but this audit did not obtain a runtime per-state census proving that no valid migration state can expose more than six primary actions at once.

The parent should treat that as a targeted review item rather than redesigning the category or changing AI weights.

### Medium: authorised detail tooltips are information-dense

The public famine tooltip is one concise stage line and the public migration tooltip is one concise role line.

Owner/controller detail tooltips intentionally expose the canonical value plus exact route, receipt, cohort, and outcome context, but the famine detail also lists eight component inputs and the migration detail includes state and owner summaries.

This is a cognitive-load risk for authorised viewers, not a proven source defect, because the category surfaces still expose only three canonical values per mechanic.

### Low: workspace-wide diagnostics are unrelated

The bounded map inspection retained truncated workspace diagnostics including `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` building/port locator errors.

Those diagnostics are outside the famine/migration mapmode source and were not changed.

## Separate category lifecycle

`common/decisions/categories/famine_decision_category.txt:3-16` defines `famine_decision_category` with an independent `famine_decision_problem_is_active` visibility gate, `visible_when_empty = no`, and the famine-owned compact report header.

`common/decisions/categories/migration_decision_category.txt:3-21` defines `migration_decision_category` with its own phase flags or `migration_decision_problem_is_active` gate, `visible_when_empty = no`, and the migration-owned compact report header.

Both category visibility blocks exclude special Chaos countries and require normal civilian systems.

The famine helper in `common/scripted_triggers/famine_decision_owner_triggers.txt:21-28` reveals only for famine phase flags or an owned state at supply-strain-or-worse, so stable monitoring alone does not expose the category.

The migration helper in `common/scripted_triggers/migration_decision_owner_triggers.txt:1-45` requires repeated incidents, a valid corridor offer, material national or state reception load, large flight, or a large trapped obligation, in addition to the migration phase flags.

The phase effects in `common/scripted_effects/famine_decision_phase_effects.txt` and `common/scripted_effects/migration_decision_phase_effects.txt` promote emerging, active, resolution, and dormant states and clear terminal flags after their owned obligations resolve.

The migration category directly includes phase flags so a persisted starting or in-progress migration problem remains visible while its state-level reveal evidence is being reconciled.

No category combines famine and migration visibility, and no category is visible merely because the other mechanic is active.

The compact `famine_report_header_scripted_gui` and `migration_report_header_scripted_gui` attachments are separate category headers and are not a shared full GUI.

## Dedicated mapmode source audit

`common/map_modes/chaosx_state_map_modes.txt:390-569` defines `famine_state_map_mode` with `top` and `bottom` layers, `type = state`, `far_text = country`, `near_text = state`, and `update_daily = yes`.

Its bottom fill is a deterministic five-stage Food Security classification: stable supply, supply strain, acute shortage, famine, and catastrophic famine.

Its top border reads famine-owned blockade proof, delivered-relief proof, route-open proof, positive pressure, and catastrophic emphasis without replacing the stage fill.

`common/map_modes/chaosx_state_map_modes.txt:571-910` defines `migration_state_map_mode` with the same two state layers and text/update contract.

Its bottom fill priority is trapped population, overcrowded reception, organized evacuation, active exodus, preparation, return readiness, returned population, resettlement, transit, and reception.

Its top border priority is trapped/overcrowded obligation, restrictive policy on an active migration state, corridor terminal or live status, reception-load share, and flight-pressure share.

The migration mapmode does not read famine food stages, reserves, famine relief delivery, or famine mortality.

The famine mapmode does not own or perform migration movement, route selection, cohort mutation, or death accounting.

Both definitions use state-scoped `FROM` reads and temporary colour variables only, and neither adds a recurring scripted `every_state` or `every_country` scan.

`update_daily = yes` is an engine mapmode refresh contract and is not a gameplay scheduler or pacing pulse.

The source census therefore satisfies the exact-two dedicated-mapmode boundary and the no-new-world-scan binding.

## Player-facing values and cognitive load

`localisation/english/famine_l_english.yml:3` presents exactly three famine category values: Food Security, Food Reserves, and Relief Access.

`localisation/english/migration_l_english.yml:3-10` presents exactly three migration category values: Displacement Load, Reception Capacity, and Border Policy.

Internal component ledgers, cohort identity, route receipts, generations, and diagnostic projections are not additional player-facing meters.

`localisation/english/chaosx_map_modes_l_english.yml:130-147` gives the famine mapmode a start-readable name, description, five stage labels, and a short public tooltip.

`localisation/english/chaosx_map_modes_l_english.yml:149-233` gives the migration mapmode a start-readable name, description, role labels, route/corridor labels, and public/authorised tooltip strings.

The mapmode names and descriptions explain what the fill and borders mean before a crisis exists, which satisfies start availability and understandability at the source/localisation level.

The authorised famine detail at `localisation/english/chaosx_map_modes_l_english.yml:136` is deliberately long and exposes score, pressure, reserves, access, relief, eight component inputs, and deaths only to an owner/controller.

The authorised migration detail at `localisation/english/chaosx_map_modes_l_english.yml:155` is also long and combines state movement, route/corridor/cohort facts, state load, outcome totals, and owner-wide capacity/load summaries.

Recommended follow-up is a presentation-only shortening or staged detail split if live review finds the delayed tooltip hard to scan; no gameplay or value-count change is warranted by this audit.

## Mission quality

All six missions are owned by their respective decision category and use explicit activation, available, timeout, success, failure/timeout, and cleanup paths.

| Mission | Owner, region, requirement | Duration and outcome | Duplicate/cleanup risk |
| --- | --- | --- | --- |
| `famine_mission_secure_relief_route` (`common/decisions/famine_decisions.txt:66-139`) | Famine category, ROOT-owned and controlled subject state with active route flag, subject flag, and deadline. | `famine_mission_timing.repair_route_timeout`; success requires proven route, intact route, and deadline, then awards stability; timeout awards stability/war support. | Subject/proof/deadline and country active flag are cleared on cancel, success, and timeout, then mission slots are recounted. |
| `famine_mission_deliver_relief_before_reserves_fail` (`common/decisions/famine_decisions.txt:140-211`) | Famine category, ROOT-owned and controlled relief subject with deadline and reserve ledger. | `famine_mission_timing.deliver_relief_timeout`; success requires proof, reserve floor, low pressure, and deadline; timeout awards stability/war support. | Subject/proof/deadline and country active flag are cleared on all terminal paths and slots are recounted. |
| `migration_mission_hold_humanitarian_corridor` (`common/decisions/migration_decisions.txt:66-130`) | Migration category, controlled corridor subject with active mission, cohort identity, and valid operation. | `migration_mission_timing.secure_corridor_timeout`; success finalizes the corridor and awards stability; timeout expires the corridor and awards stability/war support. | Cancel/timeout expire the persisted corridor, and the corridor mission owner retains the exact generation. |
| `migration_mission_protect_evacuation_transport` (`common/decisions/migration_decisions.txt:131-212`) | Migration category, ROOT-owned and controlled evacuation subject with cohort/deadline, infrastructure, route safety, and hazard exclusions. | `migration_mission_timing.protect_evacuation_timeout`; success requires the proven transfer and deadline; timeout awards stability/war support. | Subject, proof, cohort, deadline, country active flag, and slot count are cleared on cancel, success, and timeout. |
| `migration_mission_prevent_reception_collapse` (`common/decisions/migration_decisions.txt:213-389`) | Migration category, ROOT-owned hosted cohort with exact aligned identity, positive state load, capacity validity, observation receipt, and observation deadline. | `migration_mission_timing.prevent_reception_timeout`; success requires no breach/overcrowding/plague and a valid exposure receipt; breach or timeout records failure and conditional consequence. | Breach, receipt generation, subject, cohort, deadline, medical flag, and slot count are cleared through the terminal paths. |
| `migration_mission_prepare_safe_return_route` (`common/decisions/migration_decisions.txt:390-465`) | Migration resolution phase, ROOT-owned return subject with return context, valid state, route/infrastructure, hazard exclusions, and deadline. | `migration_mission_timing.prepare_return_timeout`; success awards stability; timeout awards stability/war support. | Subject/deadline, country active flag, and mission slot count are cleared on cancel, success, and timeout. |

All six use `fire_only_once = no` with explicit active flags and cleanup, so no duplicate loop was proven in source review.

The parent should still confirm duplicate callbacks and cross-lane slot accounting in the live ledger owner, especially where corridor protection and evacuation protection refer to the same cohort generation.

## Cost and requirement clarity

Every decision action inspected uses a `custom_cost_trigger` with political power plus equipment/fuel resources, and every cost stays at or below four distinct spendable types.

The highest-cost actions are `famine_escorted_relief_convoy` and `famine_emergency_airlift` at four types each, and `migration_third_country_resettlement` at four types.

The remaining actions use two or three spendable types.

The famine cost localisation strings are at `localisation/english/famine_l_english.yml:50-59`, and the migration cost strings are at `localisation/english/migration_l_english.yml:69-84`.

Those strings call the existing `GetCivilianResponse...Cost` icon-first helpers rather than spelling out resource names, and the explicit migration support requirement uses `£support_equipment_text_icon` at `migration_l_english.yml:68`.

Non-consumed route, ownership, hazard, capacity, and cohort requirements are carried by `visible`, `available`, `target_trigger`, and dedicated requirement tooltip keys rather than hidden fifth spendable costs.

No cost, AI weight, timer, or route-balance patch was made.

## AI validity and route locks

All inspected actions have `ai_will_do` blocks and share the same route, target, ownership, capacity, safety, policy, and cost gates as player actions according to the current completion report.

This audit did not alter AI weights.

The existing probability recovery audit remains partial because the installed scenario schema rejects the typed scopes required by these decisions, leaving rendered scores at zero and no certified ranking or dominance result.

No new probability audit was required for the mapmode definitions because they contain no AI, MTTH, random-list, or weighted-selection logic.

Famine blockade and relief branches read explicit route/blockade proof, while migration corridor and transfer branches read persisted status, route, capacity, ownership, and exact cohort proof.

Mapmode colour reads are presentation-only and cannot authorize a transfer, death, route, border, or reception effect.

## Localisation, GFX, and GUI evidence

The two mapmode title/description families and their public/delayed tooltip keys are present in `localisation/english/chaosx_map_modes_l_english.yml`.

The four dedicated button textures are registered by `interface/mapmodes_interface.gfx` and correspond to famine/migration selected and deselected assets.

No third famine/migration button family, shared full GUI, or combined localisation namespace was introduced.

### Static button-window evidence

The parent-supplied `hoi4.gui_inspect` resolved `MapmodesInterface_Ingame` for scenario `famine_migration_mapmode_buttons_start` at shared revision `9590e797d841572a2f0d42968a0c6aca9a57730f2a5855cbf1b59f255cec49bb`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3dfcf63cd977826ebcf0c0929da3e9271a79ef0c4b6cfdfda0f5246780fd3575/6c2b73d7c89de9ae8ffc085b6aec51c8a1b87fe3ce92224c22e5e7bfac4c35d8/gui-inspect.9590e797d841572a.json`.

The matching `hoi4.gui_render` artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b917c62bdfce4541d5f58ddc41eaf6ed5884f630a57a3ea88effd5f0cd3cf003/b10b1c79f83a9f0403079ff59ebdde72a9fafc41aeb639eec9df9890da29af8a/MapmodesInterface_Ingame-full.svg`.

These artifacts are static button-window/layout evidence only.

They do not prove that a famine or migration mapmode is selected, that a state receives the expected dynamic colour, or that a delayed scripted tooltip expands correctly.

### Unavailable dynamic mapmode proof

The attempted `selectedMapMode` scenario field was rejected as unrecognized, so the MCP GUI route cannot select either custom mapmode.

The map route therefore cannot execute the state-scoped scripted colour or tooltip branches, and no dynamic mapmode click proof is claimed.

The bounded parent `hoi4.map_inspect` evidence returned revision `24d421bcc68e84bfc6455b892b1ac5855b0ef47d0a746d0ce4a5a91e7851640b`.

Map-inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a75193c5b26cd1180f60405e66b535e35ff3e96ad25d03aeeded209441129c2f/60deb73e299b4ab6ff6bc342e905d5758b8a18037e0444c2bdc859a58a4dfec6/map-inspect.24d421bcc68e84bf.json`.

The successful base state render was produced by `hoi4.map_render` at scale 1 with state/coastline/supply-node/railway overlays.

Map-render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54aca4aae57c108e044637123ef5a3cd9097ba9bc13d6f6f8670f5257d9e51dc/a53e6cad1f9c809827b8869d2d25e08c59aa60f048c0cfe2b7d362fdef8a8538/map-state.png`.

The map render proves the underlying state/map substrate is renderable, not the custom famine/migration colour branches.

An earlier duplicate GUI scenario request returned `GUI_SCENARIO_ID_DUPLICATE` and was corrected before the retained inspect/render evidence; this was a request-shape error, not a source error.

## Cleanup and exploit risk

The mapmodes have no effects, costs, population mutation, death accounting, route creation, or AI side effects, so no mapmode-only exploit loop was found.

Decision cleanup paths clear their state subjects, deadlines, active flags, receipts, and mission slots on cancellation, completion, and timeout according to the source blocks above.

The completion report records delayed zero-debit refund guards for `famine_evacuation`, `migration_evacuate_vulnerable`, `migration_evacuate_workers`, `migration_voluntary_return`, and `migration_forced_repatriation`.

No repeated map refresh can grant a reward or consume a cost because the scripted mapmodes only assign temporary display variables.

The unresolved migration projection producers remain the principal cleanup/presentation risk because stale or absent state flags can leave a neutral role or stale presentation until the owning ledger reconciliation runs.

## Namespace and scan binding

The current namespace validation reports zero runtime matches for `famine_migration_*` and `fm_*` across the searched runtime roots and zero matching runtime filenames.

Famine identifiers remain under `famine_*`, migration identifiers remain under `migration_*`, and narrow neutral corridor/transfer infrastructure remains under `humanitarian_*` or `civilian_transfer_*`.

Historical superseded names in planning handoffs are documentation evidence only and are not runtime aliases.

The mapmode source performs no new world scan, and its daily visual refresh is not a gameplay pulse.

## Recommended fixes and remaining work

1. Keep the two current mapmode ids and separate category/prefix contracts unchanged.

2. Have the migration ledger/projection owner write and clear reception, overcrowding, return, and durable cohort state projections at existing validated transaction boundaries, then re-audit the mapmode consumers.

3. Obtain a bounded runtime count of simultaneously actionable migration primary decisions per representative state before claiming the category-density rule is proven.

4. If live review confirms tooltip overload, shorten the authorised detail strings or stage the detail without adding a fourth player-facing value.

5. Preserve the MCP limitation in the parent completion report and do not present the static GUI artifact or base state render as dynamic mapmode proof.

No source patch was proven safe or necessary in this bounded audit.

## Files changed by this subagent

- Added `docs/plans/famine_and_migration_system_plans/subagent_handoffs/mapmodes_0826.md`.
- No gameplay, AI, mapmode, GUI, GFX, localisation, decision, mission, or constants source files changed.
- Concurrent worktree changes were preserved; no reset, cleanup, or unrelated file modification was performed.

## Remaining limitations

The map and GUI MCP routes cannot execute custom scripted mapmode colours/tooltips or inject selected custom mapmode state.

Migration projection setter/cleanup ownership and a runtime migration action-density census remain unresolved from this bounded audit.

Live consumer validation remains outside this subagent's source-only evidence boundary.
