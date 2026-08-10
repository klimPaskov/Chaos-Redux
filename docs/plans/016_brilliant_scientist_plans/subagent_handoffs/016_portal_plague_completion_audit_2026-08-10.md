# Event 016 Portal Raider and Black Plague completion audit

Date: 2026-08-10

Mode: read-only completion audit. This handoff is the only file written by the auditor. No gameplay, localisation, asset, spreadsheet, or existing documentation file was edited, and no in-game validation is claimed.

## Overall status

The audited tranche is **partial and blocked**, not complete.

The generic Portal Raider API, Event 019 provider bridge, two target-specific native raid definitions, successful-outcome unit consumption, static counter registration, no-outbreak Black Plague access, Black Plague registry entries, and the decision against a parallel Event 016 CBRN ledger are present in source. Concurrent owner patches also resolved the state-raid critical extraction count, `destroy_unit` syntax, and the Portal Warfare technology description during this audit.

Completion remains blocked by the rejected Portal Raider model/entity/action/sound package, the missing purpose-built hidden-technology icon package, incomplete weighted-logic evidence, and partial event-MCP evidence. The CBRN plague-output contradiction and frozen documentation provenance were resolved after the audit. Live raid, unit, counter, Event 019, and Black Plague consumer behavior remains user-owned validation.

## Snapshot and scope

- Repository HEAD observed: `43f0d731e008a06911e45c702285443fe29e10b3`.
- Current portal raid source SHA-256 after concurrent fixes: `4E397E1BCC1DAC376307A796A0ED4750D61D9DC5F9457F8F0692D6EF33E25CEF`.
- Current CBRN random helper SHA-256 after the owner correction: `15726EDFC85EF45244F88DAFF56B043B0D094E331390818C66366C2B9C0B8620`.
- Current Mengele registry effect SHA-256: `4B9ECDEEEDB8C72F0831B8789C19AFA0C077E1C15A0FE9AF563987118FCA96D6`.
- Current Black Plague project SHA-256: `EAE7E9044A2E72078BFACAD6E9580856192868D0918162021534C2B9E74D32AB`.
- Required repository skills applied: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, and `chaos-redux-3d-model-pipeline`.
- The required offline wiki core pages, the equipment/division/technology/entity/graphical-asset pages, vanilla raid documentation, vanilla effect/trigger/script-constant documentation, installed vanilla counter definitions, and installed vanilla counter DDS files were consulted.

## Completion status by surface

| Surface | Status | Evidence and limits |
|---|---|---|
| Generic `portal_raider` and `teleportation_equipment` API | Finished in static gameplay source; visual consumer blocked | `common/units/016_brilliant_scientist_project_forces.txt:129-158` defines the generic subunit with `sprite = portal_raider`; `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt:125-224` defines the generic archetype and active equipment; `common/script_enums.txt:729-730` registers both equipment identifiers. The operational technology enables the subunit/equipment without setting Kruger or Event 016 ownership state. The sprite token intentionally has no accepted matching entity until the rejected model package is recovered, so map-model resolution remains an explicit blocker rather than a hidden fallback. |
| Event 019 provider 509 bridge | Finished in static source; MCP partial | `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:186-199` registers family/provider 509, `:391-394` builds the four-battalion derivative template, `:550-561` records exact manpower, Teleportation Equipment, and Infantry Equipment obligations, and `:666-1865` supplies the provider callbacks, management payment/refund, presentation, isolation, and cleanup paths. `events/019_infantry_spawn.txt:833-849` defines presentations `.918` and `.919`. No free Event 019 spawn path was found, but full lifecycle execution was not proven. |
| Native state-installation Portal raid | Finished in current static source; probability/runtime proof blocked | `common/raids/016_brilliant_scientist_portal_raids.txt:32-145` defines the state target, six `portal_raider` battalions, and Teleportation Equipment reservation. Success calls beachhead plus one state-installation extraction at `:229-230`; critical success now calls extraction twice at `:253-255`. Both successful outcomes consume the selected division at `:237` and `:262`. |
| Native exact special-project-facility Portal raid | Finished in current static source; probability/runtime proof blocked | `common/raids/016_brilliant_scientist_portal_raids.txt:272-377` uses exact `building = { tags = facility }` targeting. Success calls exact extraction at `:466-467`; critical success calls exact extraction and one state-installation extraction at `:493-495`. Both successful outcomes consume the selected division at `:477` and `:505`. Concurrent fixes added province-targeted facility damage at `:439-443,468-472,496-500`, selected-province family guards, and controlled-state destination gates. |
| No repeatable free-unit loop | Finished in source path; runtime unproven | Each successful or critical raid reconstructs one six-battalion `Quantum Transit Raiders` formation in the captured target province and destroys the assigned origin formation with scalar `destroy_unit = yes`. Critical success does not create an additional unit. This matches `docs/events/016_brilliant_scientist/systems/portal_raider_api.md:13-17`. |
| Portal entity/action/sound reference hygiene | Finished in current source | No active runtime reference to `portal_raider_entity`, a Portal Raider mesh, a Portal Raider animation, `portal_arrival`, or a Portal Raider sound was found. Four generic `custom_sound = generic_bioweapon_aerosol` fallback calls were present during the audit and were removed concurrently by the owner. The rejected model/audio package remains unwired, as required. |
| Counter registration and static assets | Finished statically; live use unproven | `interface/portal_raider_system.gfx:10-12` registers the large, medium, and medium-white consumers. The installed large DDS is `152x42`, SHA-256 `4236DF...`; the installed small DDS is `60x12`, SHA-256 `FB009C...`. `docs/assets/shared_portal_raider_system/counters/portal_raider_counter_art_handoff.md` records original art, exact vanilla-family inspection, sampled vanilla green, processed outputs, manifest, contact sheet, DDS round-trip comparison, and parent-owned GFX status. This is counter completion only, not 3D package completion. |
| Portal Raider model, entity, actions, and unit sounds | Rejected and blocked | `docs/assets/shared_portal_raider_system/models_3d/portal_raider/portal_raider_3d_model_handoff.md` records rejection at the Meshy semantic gate because the required ray rifle was absent. Paid recovery requires user approval. The gameplay subunit retains the generic `portal_raider` sprite token, but no accepted `portal_raider_entity`, skeletal actions, synchronized sourced audio package, or fallback exists. The unit therefore must not be treated as visually load-complete until recovery and wiring pass acceptance. |
| Kruger Black Plague access without Event 020 outbreak | Finished in source; runtime unproven | `common/scripted_triggers/020_black_plague_weaponization_triggers.txt:13-27` grants access to the current Kruger host through Biological Weapons Theory, without requiring an active Event 020 outbreak. The project availability trigger at `:60-75` accepts this route. |
| Mengele Black Plague access without Event 020 outbreak | Finished in source; weighted sequence evidence partial | `common/scripted_effects/germany_mengele_effects.txt:2255-2438` includes Black Plague in the twelve-entry Directorate project pool and sets `directorate_special_project_black_plague_available`. `common/scripted_triggers/020_black_plague_weaponization_triggers.txt:13-27,60-75` accepts a valid Mengele clone Directorate with the exact registry flag, without Event 020 outbreak state. Completion clears the available flag and sets the completed flag at `common/scripted_effects/020_black_plague_weaponization_effects.txt:184-185`. Full available/completed-flag sequences were not evaluated by the current MCP route. |
| Native Event 020 runtime reuse and no parallel ledger | Finished in source and disposition | `black_plague_weaponization_initialize_country` initializes the existing disease-containment, condemnation, and Black Plague runtime before project effects. No `brilliant_scientist_krg_biological_stockpile*` gameplay ledger was found. The optional separate KRG stockpile/delivery ledger remains queued behind an idempotent native callback and is explicitly not implemented as a substitute. |
| CBRN random registry and future-registry rule | Finished in current source; probability sequence proof partial | `common/scripted_effects/cbrn_project_effects.txt:12-77` contains the complete eight-entry pool and a Black Plague entry of weight 8. The plague branch now grants only the native plague project and technology, matching its documented exact output. The future-project registry review rule is documented in the Event 016 and Event 020 system docs. The three consecutive-call consumers were reviewed by the owner and accepted as intentional two-draw rewards whose second draw excludes the first result. |
| Localisation | Finished for scoped current wording; runtime presentation unproven | `localisation/english/chaosx_raids_l_english.yml:8-29` distinguishes the two raid surfaces and correctly describes up to two state installations on critical success. `localisation/english/016_brilliant_scientist_country_l_english.yml:198-199` now states that Weaponized Transit Doctrine improves Quantum Transit Raiders and enables Portal Warfare raids. |
| Documentation and completion provenance | Reconciled for the current tranche | Current source-of-truth summaries record the split raids, no parallel ledger, counter completion, rejected 3D package, no fallback, and registry rule. Current planning cells use the generic Portal Raider identifiers and mark the rejected entity job as pending approval. The 64-entry frozen documentation checksum ledger verifies with zero missing files and zero mismatches. Historical handoffs remain historical evidence rather than current implementation authority. |

## Missing, simplified, blocked, or stale requirements

### 1. Generic sound fallback resolved during audit

The accepted documentation states that Portal Raider model, entity, actions, and sounds are rejected and unwired pending paid recovery, with no fallback. Four `generic_bioweapon_aerosol` calls were present in successful Portal Warfare outcomes when first inspected. The owner removed them during the audit. The final non-document scan found no active `portal_raider_entity`, `portal_arrival`, Portal Raider mesh/action/sound, or Portal Warfare `custom_sound` reference.

Disposition: resolved in current source. Keep the sound surface unwired until an approved Portal Raider sound package exists; do not introduce another fallback.

### 2. CBRN plague branch contradiction resolved after audit

The audit found that the plague branch gated on missing `plague_bomb_delivery_systems` but granted both anthrax and plague. The owner removed the extra anthrax grant. The branch now completes the native plague project and grants only `plague_bomb_delivery_systems`, matching the documented exact output and preserving anthrax as a separate later draw.

Disposition: resolved in current source. The cached all-open pool weights remain arithmetically unchanged, but a fresh sequence comparison remains unavailable through the current MCP route.

### 3. Consecutive CBRN helper calls are an accepted consumer cadence

`grant_random_chaos_special_project_available_tech` is invoked twice consecutively at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1400-1401`, `:1705-1706`, and `common/scripted_effects/005_soviet_collapse_effects.txt:22315-22316`. Each helper call awards one project, so these are two sequential draws and the first completion changes the second pool.

Disposition: the owner reviewed all three contexts and confirmed that each is an intentionally high-value UWR science/chaos-warfare reward that awards two distinct projects. This is consumer-owned cadence, not duplicate Event 016 helper wiring, and no patch is required. Sequence-specific weighted evidence remains unavailable because the current probability route is blocked.

### 4. Native raid design and lifecycle risks remain

The decision/mission audit fixed three additional source defects while this completion audit was active: exact facility branches now verify that `var:ROOT.target_province` contains the facility family being removed; reconstruction destinations now require actor-controlled states and use `random_owned_controlled_state`; and exact-facility limited/success/critical outcomes now damage the selected provincial facility directly. These fixes are recorded in `016_portal_raid_decision_mission_audit_2026-08-10.md`.

The following owner-review items remain and are not silently accepted as completion proof:

- Exact-facility reconstruction currently requires a controlled destination state with all four special-facility families below one, not just the extracted family. This conservative gate can hide a raid even when a family-specific valid destination exists.
- Both native raids specify `portal_raider = { min = 6 }` without a native maximum. The locked template has exactly six battalions, but another template with more than six qualifying battalions could satisfy the source requirement. No exact-maximum vanilla precedent was found.
- Beachhead reconstruction destroys the source formation but creates a replacement with `start_equipment_factor = 1.00` and `start_manpower_factor = 1.00`. The one-for-one topology is source-correct, but the full-factor payload remains a live balance surface.
- `brilliant_scientist_portal_beachhead_active`, `brilliant_scientist_portal_raid_breach_recorded`, `brilliant_scientist_portal_raid_targeted`, and extraction state flags are persistent. No Event 016 expiry/cleanup consumer was found; later containment or spread work must define cleanup if persistence is not intentional.
- Heavy state damage deliberately runs the light helper followed by the heavy pass, so the same highest-priority surviving building may receive both applications. This needs explicit documentation if distinct-building damage was intended.

### 5. Weighted-logic evidence is incomplete or stale

The required probability audit was routed through `chaosx_ai_probability_auditor`. Before each surface, the auditor checked the active tool catalog; no `hoi4.probability_inspect`, `evaluate`, `sweep`, `compare`, or `render` route was exposed. A direct `mcp__hoi4_agent_tools__hoi4_probability_inspect` attempt returned `TypeError: tools.mcp__hoi4_agent_tools__hoi4_probability_inspect is not a function`. Source-only score traces are not engine or selection-probability evidence.

- Cached CBRN evidence remains usable only because the exact current helper hash matches. Its all-open declared pool totals 64: anthrax/plague 15.625% each; tularemia/zombie/Black Plague/sarin 12.5% each; smallpox/soman 9.375% each. Cached inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8ad4c959223325a8ec350e24c8e9089b360386c78dbca7cd48be940705db7a9/d3e02a02ff57cb6cc810e05605ddcb7ec5ce6f01d674a46e388f5165d6c1bd8c/probability-inspect-3122a369c161.json`. Cached all-open evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/769318320b277728dfdefd7d5922ad782424de6a45598dc3ffce7350f0f18fee/779ead74bdd5893153338b6df5c90eea7f32dc64a1aeae73b06e4604a8ef45ab/probability-820b02b87ead7c338434192d.json`.
- Cached Mengele numeric-roll evidence remains hash-matched, but prior scenarios emitted `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS`; it does not prove the enclosing available/completed flag sequence. With twelve declared numeric rolls at 100, each entry is conditionally 8.3333%. Cached inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ee8a0c3790d89823c272f90f426f533ad1909c6f5d52debf717d706fe8eb15d/a2f4d1320685ee5c85ba66bc4c6318e022556f47005aca1cc58f80b368f83714/probability-inspect-8cc2a5e03682.json`.
- Both raid `ai_will_do` blocks changed after the 2026-08-09 evidence. A later current-source `decision_ai_will_do` inspection returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`, zero candidates, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6131eb6eb7ad36e79af838d551929380aa6dbfae13611431cc8a1a7b1c507425/9a4182c318047e5f5ffa85a0d1603f47f065e977c175b6924c9ae810df765b1c/probability-inspect-9e9deaa70223.json`. READY, READY KRG host, NOT READY, and INVALID TARGET evaluations returned `PROBABILITY_SURFACE_EMPTY`; `ai_strategy_factor` returned `INTERNAL_ERROR`. This is current MCP blocker evidence, not a raid selection-probability result.
- `common/special_projects/projects/020_black_plague_weaponization_projects.txt:40-54` contains `black_plague_weaponization_program.ai_will_do`, but the 2026-08-09 handoff omitted this weighted surface and its file hash. Source-only score is base 0.25, forced to zero by defensive conversion, with war and an active severe state each multiplying by 2. This is a willingness score, not a selection probability.
- No valid `hoi4.probability_compare` artifact exists for this tranche. Prior CBRN compare returned `PROBABILITY_IDENTIFIER_NOT_FOUND`; the one-candidate Black Plague probe returned `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`; sweep requests lacked required ranges.

### 6. Event MCP evidence is partial, and comparisons are unavailable

Mandatory event inspection/rendering was performed for Event 016 root `chaosx.nr16.1`, Event 019 root `chaosx.nr19.1`, Event 020 root `chaosx.nr20.1`, and the Event 019 bridge presentations `chaosx.nr19.918` and `.919`. Each returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`; the tool deferred helper/lifecycle expansion in the large workspace and did not provide complete validation. There were no blocking diagnostics in the returned partial views, but those views are not whole-chain proof.

- Event 016 inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/539ceae7a50e5bb057196a886c9ef12f19127119fa363878a2aeecc83515614b/15858f3668915d00d9e2ad2dd8611b39026ac89aefa39dfb396c944ffc4be8b8/event-trace-c11a255294fb.json`.
- Event 019 inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d43ff8feef11cdf04e83987f84a11f5187f5bad29849e4d6a082f098e968075/e6fc133c8c335d88324f9d583584312b3a40180afbbfff6114c81bcb53206fdf/event-trace-c11a255294fb.json`.
- Event 020 inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e37edef96beefa2ba9123b7477f93a7346ecae1c8ac9d48dfa2694626e7810da/947dc235dbaabe7b9e6e21ccdf3916d70acf93ea685da1b3a5be855887eff86c/event-trace-c11a255294fb.json`.
- Event 019 `.918` inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac4f5b2569f2e4974ac3d66beaa126a5edb4753e92febbec2ee64ffdf9fc708a/2efcc25f6df47a71dc0d2d2aa08847565b3ed03a10f34cdbcc62d63e1de81c3e/event-trace-c11a255294fb.json`.
- Event 019 `.919` inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a62f8b2f48771b5fbf32b41d12cb5e020708d3307f9b1946b174b028d748a78/cf772ab5f76344bc871f945caa62979be9ebf1ec79054945d489148d8d1e4be6/event-trace-c11a255294fb.json`.

The attempted Event 016 comparison rejected the old event-lint baseline as `EVENT_GRAPH_ARTIFACT_INVALID`. The attempted Event 020 comparison returned `ARTIFACT_NOT_FOUND` for the old provenance manifest. The Event 019 `.918` historical handoff names an inspection but does not provide a usable baseline URI. No valid event compare exists.

### 7. Completion provenance and planning documents were reconciled after audit

- `docs/specs/016_brilliant_scientist_specs/package_checksums.sha256` parses 64 entries with zero missing files and zero mismatches after the final documentation refresh.
- `docs/plans/016_brilliant_scientist_plans/016_event19_generic_unit_family_3d_model_backlog.md` uses the generic `portal_raider`/`teleportation_equipment_1` contract and records the rejected entity job as pending explicit approval.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_project_reuse_identifier_map.md` uses the current generic Portal Raider identifiers.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_event19_portal_temporal_provider_extension_2026-08-03.md` contains retired identifiers under a supersession notice. That is acceptable historical evidence but must not be treated as current implementation proof.
- The older `portal_raider_counter_handoff.md` is retained as production history; the dated counter-art handoff and current package docs are authoritative for the completed counter assets.
- The 2026-08-09 probability handoff remains exact-hash current only for CBRN and Mengele effect files. It is stale for the changed raid source and incomplete for the Black Plague project AI block.

## Accepted-plan disposition

- **Promoted and implemented:** generic Portal Raider/Teleportation Equipment identifiers; generic operational-technology API; Event 019 provider 509 bridge; two native Portal Warfare raid target types; selected-formation consumption and one-for-one beachhead reconstruction; exact state/facility extraction effects; Portal Raider counter package; Kruger and Mengele no-outbreak Black Plague access; Black Plague inclusion in CBRN and Directorate registries; future special-project registry-review invariant.
- **Promoted and corrected during this audit:** state-raid critical success again performs two state-installation extraction attempts; raid outcome `destroy_unit` syntax is scalar `yes`; exact facility extraction validates the selected province; reconstruction requires controlled destinations; exact facility outcomes apply exact provincial damage; Weaponized Transit Doctrine description now states the correct unit improvement and raid unlock; the generic biological sound fallback was removed from all Portal Warfare outcomes; the CBRN plague branch no longer grants anthrax; and the frozen documentation checksum ledger was refreshed.
- **Rejected and blocked:** Portal Raider model, entity, skeletal actions, and synchronized sourced unit sounds. The existing generation failed the mandatory semantic requirement, and no user-approved paid recovery or fallback exists.
- **Queued, not implemented:** separate Event 016 KRG biological stockpile/delivery ledger, pending a stable idempotent native callback. This queue does not block the native raids and must not be replaced with a parallel ledger.
- **Blocked asset gap:** purpose-built medium sprites for the hidden Event 016/Mengele operational technologies. Two icon-worker attempts produced no reviewed deliverable, and no reused or generic fallback was installed.
- **Historical-only evidence:** superseded handoffs may retain retired identifiers for provenance, but current source-of-truth maps and package documentation use the generic API.

## Recommended next actions

1. Keep Portal Raider entity/action/sound references absent until the user approves a complete recovery package; do not wire a different fallback.
2. Restore the `hoi4.probability_*` route for the probability auditor and obtain fresh evidence for both raid AI blocks, the Black Plague project `ai_will_do`, the full CBRN pool, and the full Mengele available/completed flag sequence.
3. Decide the intended destination-family restriction, greater-than-six battalion policy, full-factor reconstruction balance, persistent beachhead-flag lifecycle, and light-plus-heavy building damage semantics. Update specs before changing broad behavior.
4. Produce purpose-built hidden-technology medium sprites through the icon workflow; do not install a resized, generic, or unrelated fallback.
5. Keep model/entity/action/sound recovery blocked until the user approves additional paid recovery. If approved, require the complete 3D pipeline, sourced-audio provenance/checksums/synchronization, accepted reimport evidence, and parent-owned runtime wiring; no fallback is authorized.
6. Treat live native-raid targeting/reservation/cancellation/outcome, one-for-one formation replacement, exact facility removal, counter display, Event 019 payment/refund/cleanup, and no-outbreak Black Plague research/completion as user-owned validation. Do not claim in-game completion from this audit.

## Final completion statement

No whole Event 016 completion claim is supported. The current core/runtime tranche has reconciled source and documentation coverage, but the rejected 3D/audio package, missing purpose-built hidden-technology icons, incomplete probability evidence, partial event graphs, and remaining native-raid lifecycle/balance decisions remain explicit blockers or deferred design gaps.
