# Event 006 IW-015 Galicia package re-audit — 2026-09-05

Disposition: blocked — NO-CHANGE / FAIL-CLOSED.

This is a fresh bounded whole-package audit of IW-015 Galicia against the current source-of-truth map, resume packet, completion inventory, and the dated GLC repairs. No gameplay source patch was proven safe or applied. The package remains adapter-only and fail-closed at the current Event 006 boundary.

## Accepted binding

The package binding is `iw_015` / `IW-015`, carrier and `original_tag = GLC`, anchor state `171`, reservation group `RG-171`, region `Mediterranean/Iberia`, package depth `standard`, archetype `agrarian_regional`, and former host `SPR`. The package is a vanilla-carrier overlay and must preserve the vanilla GLC history, flags, and roster.

## Files inspected

The package and dispatch source surfaces inspected were:

- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`
- `common/scripted_effects/006_independence_wave_join_effects.txt`
- `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`
- `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt`
- `common/scripted_effects/006_independence_wave_force_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt`
- `common/decisions/006_independence_wave_iberian_decisions.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`
- `common/characters/006_independence_wave_characters_registry.txt`
- `history/general/006_independence_wave_character_recruitment_registry.txt`
- `common/ideas/006_independence_wave_ideas_registry.txt`
- `common/country_tags/006_independence_wave_countries.txt`
- `interface/006_independence_wave_portraits_registry.gfx`
- `localisation/english/006_independence_wave_iberian_l_english.yml`
- `docs/events/006_independence_wave/iberian_registered_packages.md`
- `docs/events/006_independence_wave/systems/country_registry.md`
- `docs/events/006_independence_wave/systems/formable_registry.md`

Vanilla references inspected were `common/country_tags/00_countries.txt`, `common/countries/Galicia.txt`, `history/countries/GLC - Galicia.txt`, `history/states/171-Galicia.txt`, the vanilla GLC flag triplet and ideology variants, the installed `documentation/*.md` script references, and the relevant vanilla character and country-history files. The required offline wiki pages and repository skills were read before source review: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus modding, Technology modding, Equipment modding, and Division modding, plus `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, and the portrait/event-assets guidance required by the asset surfaces.

Authority and handoff files inspected were:

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_completion_inventory_2026-09-03.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_glc_no_additive_roster_repair_2026-08-30.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw015_glc_portrait_gate_2026-09-03.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw015_glc_flag_identity_2026-09-03.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw015_glc_country_package_audit_2026-09-02.md`

## Country-package coverage

### Tag, history, state, and host

- Vanilla `GLC` resolves through `00_countries.txt` to `countries/Galicia.txt`, with vanilla history retained; no replacement tag, cosmetic tag, country shell, or invented emblem was added.
- `can_plan_independence_wave_package_iw_015` in `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:142-148` protects package and reservation uniqueness, GLC availability, and state 171 availability.
- `independence_wave_load_package_iw_015` in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:414-426` binds `iw_015`, `rg_171`, `GLC`, and state 171, and records the anchor and primary host through the existing planner contract.
- The vanilla state 171 source retains SPR ownership/core history, GLC core, victory points, infrastructure, port, naval-base, air-base, arms-factory, and dockyard data. The earlier state-specific MCP inspection did not prove a selected-state 171 defect.
- The Iberian package trigger requires the saved anchor to be state 171 and owned and controlled by the package carrier (`006_independence_wave_iberian_package_triggers.txt:52-60` and `:197-207`). No invalid host-remnant transfer or capital mismatch was proven.

### Setup, cleanup, and generation safety

- `independence_wave_setup_iw_015_galicia` at `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:474-524` clears stale setup/roster/portrait state, initializes only after the exact package/region/depth/anchor/host/roster predicates pass, applies the existing roster checkpoint once, loads the force mapping, and sets `independence_wave_iw_015_setup_complete`, `independence_wave_iw_015_lifecycle_initialized`, and the package setup marker only after the prepared contract succeeds.
- `independence_wave_validate_iw_015_galicia` at `:536-542` requires complete package setup plus `is_independence_wave_exact_package_iw_015_runtime_ready`.
- `independence_wave_cleanup_iw_015_galicia` at `:598-642` removes the GLC mission and eleven package decisions, removes package ideas, clears GLC variables and lifecycle flags, clears route/project/AI flags, and restores the vanilla Castelao portrait only when the package override flag is present. Cleanup is dispatched at `:647-649`.
- This is a source-level generation-safe lifecycle contract. No live-game or save/load receipt was claimed.

### Roster, leaders, and portraits

- The accepted vanilla roster remains Fuco Gómez and Alfonso Daniel Castelao. `has_independence_wave_glc_command_roster` in `006_independence_wave_iberian_package_triggers.txt:81-87` checks the existing GLC roles with `ruling_only = no`.
- The 2026-08-30 no-additive-roster repair remains present: there is no duplicate `GLC_independence_wave_alfonso_daniel_castelao` recruitment or character definition in the inspected registries.
- The shared portrait checkpoint in `common/scripted_effects/006_independence_wave_effects.txt:3246-3263` applies `GFX_portrait_GLC_alfonso_daniel_castelao` once per generation, while setup/cleanup in the Iberian package effect restores `GFX_portrait_Alfonso_Daniel_Castelao`.
- `interface/006_independence_wave_portraits_registry.gfx:149-152` points the runtime consumer at `gfx/leaders/006_independence_wave/portrait_GLC_alfonso_daniel_castelao.dds`. No portrait bytes or GFX references were changed.
- The supplied portrait/source record still has unresolved rights/provenance and a dated terminology conflict (`source_placeholder` versus older `styled_final` wording). This is an external asset-gate decision owned by the parent; no relabel or fallback portrait is authorized here.

### Flags and country identity

- GLC uses the existing vanilla flag family and ideology variants. No custom GLC flag, cosmetic identity, or unverified flag source was invented.
- The 2026-09-03 flag audit records that democratic setup selects the vanilla `GLC_democratic.tga` family, while the standalone Event 006 opening-identity/rights receipt remains unresolved. The 1936 visual/date review is therefore still `needs_user_review`.
- `FORM-07` remains separately fail-closed; this audit does not set its identity, symbol, territory, member, or flag readiness flags.

### Politics, parties, ideas, decisions, and localisation

- The GLC setup and five route installers preserve the accepted constitutional, popular-council, municipal, emergency-military, and patron-client paths. The route flags are `independence_wave_glc_constitutional_government`, `independence_wave_glc_workers_government`, `independence_wave_glc_municipal_government`, `independence_wave_glc_emergency_government`, and `independence_wave_glc_patron_government`.
- The package uses the existing GLC idea keys `glc_contested_council`, `glc_atlantic_compact`, `glc_constitutional_charter`, `glc_workers_port_council`, `glc_municipal_atlantic_covenant`, `glc_coastal_security_command`, and `glc_protected_customs_mandate`, with lifecycle refresh and cleanup in the Iberian package effects.
- The GLC decision surface is present in `common/decisions/006_independence_wave_iberian_decisions.txt:205-397`, including `independence_wave_glc_secure_inland_depots`, `independence_wave_glc_integrate_coastal_guards`, `independence_wave_glc_reconcile_council_and_port`, `independence_wave_glc_settle_former_host_ledgers`, `independence_wave_glc_ratify_atlantic_charter`, `independence_wave_glc_convene_workers_port_council`, `independence_wave_glc_confirm_municipal_covenant`, `independence_wave_glc_establish_coastal_command`, `independence_wave_glc_accept_protected_customs_mandate`, `independence_wave_glc_codify_sovereignty`, and `independence_wave_glc_open_iberian_network`.
- The timed mission `independence_wave_glc_hold_council_together` is setup/cleanup wired, and its setup receipt guard remains generation-bound.
- `localisation/english/006_independence_wave_iberian_l_english.yml:97-129,146-156,181-195` covers the GLC package names, parties, ideas, decisions, and mission strings reviewed here. No missing package-local key requiring a safe source patch was proven.

### Forces, equipment, manpower, technology, and industry

- The force mapping resolves IW-015 to the documented p15 territorial-defense profile in `docs/spreadsheets/006_force_package_mapping.csv:16` and the shared force mapping effects. It uses territorial infantry/coastal guards and an institutional officer commission, with no invented navy or air inheritance.
- The package starts from vanilla GLC history and existing industry/manpower/equipment state; no major army, template, equipment, technology, production, supply, or capacity change is authorized by this audit.
- No GLC-specific technology dependency was found. The required read-only technology inspection/render of vanilla `infantry_weapons` completed as `TECH_INSPECTED`/`TECH_RENDERED`, but the workspace report is not source-accurate (`sourceAccurate = false`) and has 1,360 blocking global technology diagnostics. This is tooling/workspace evidence, not a package defect or acceptance proof.

### Focus, AI, diplomacy, and formables

- GLC loads the shared `independence_wave_focus_tree` through the existing framework and package callbacks; no separate invented GLC tree was added. The source tree remains the accepted 184-focus shared tree.
- The GLC AI strategy rows remain in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` (the GLC block is around lines 867-901). No strategy factor, `ai_will_do`, probability, or weighted target was changed.
- The required custom `chaosx_ai_probability_auditor` route is not callable in this runtime. The exposed direct `mcp__hoi4_agent_tools__hoi4_probability_*` routes are not substituted for the mandatory routed probability pass, so typed package-specific AI/probability evidence remains blocked.
- Host, Network, League, and corridor hooks remain source-wired behind the accepted package and generation predicates. The package flag `independence_wave_glc_iberian_corridor_open` is not a substitute for FORM-07 readiness.
- No Event 005 collision or generation-cleanup defect was proven in the inspected Event 006 registries, GLC package cleanup, and dated country audit. The existing Event 005/other-event boundary is left untouched.
- FORM-07 remains separately fail-closed and is not promoted by this package audit.

## Dispatch and admission boundary

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:59` includes `iw_015` in the runtime adapter allowlist. The exact package preflight at `:384-390` checks `iw_015` and `(original_tag = GLC OR exists = no)`, while the scenario preflight at `:558-560` requires exact-package tag availability. The central content-attestation list at `:159-202` intentionally omits IW-015, and `common/scripted_effects/006_independence_wave_join_effects.txt:236-270` likewise omits it from the attested Join list.

This is the intended current boundary: IW-015 has an adapter surface but lacks central admission, Join, SCN-008 release, and capacity promotion. Adding a parity guard or promoting the package here would change central admission semantics and is outside this bounded audit.

## MCP validation evidence

- Event inspect of `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, revision `fd57ee4ae74f459a2f0bf6df0319b691c9b744a09a831d4fc32dcbe4c8923df4`, graph hash `0a8e92c258572addc2dd8faef23a48bf7caf8370858083175c09964edc9601a4`, and no returned package blocker. The report is workspace-partial with deferred helper/lifecycle projections, 8,719 unresolved workspace references, and an inline-source truncation diagnostic; it is not Event 006 acceptance evidence. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63678803bf62838bd9004b5b27e0317d3d0d3df78dc70eabc38a48645a19cd32/c9561b338382415bb664a434bf90e2f4dae12d68a4e7b3cdde1bbcd8b52c2a99/event-lint-fd57ee4ae74f.json`.
- The read-only event overview render returned `EVENT_RENDERED_PARTIAL` with the same revision and graph hash. It is source-linked offline evidence only; the render deferred workspace helper/lifecycle content.
- Focus inspect returned `FOCUS_INSPECTED` for `independence_wave_focus_tree`: 184 focuses, 195 connectors, 14 continuous focuses, zero layout crossings/intersections, and passed focus diagnostics. The only reported warning was an unrelated vanilla `continuous_restrict_freedom_desc` localisation warning. Focus render returned `FOCUS_RENDERED` with layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.
- Map inspect of state 171 returned `MAP_INSPECTED`; state/region membership, definitions, networks, and adjacencies passed for the selected state. Workspace-wide positions/locator diagnostics (`MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`) caused partial validation, but no state-171-specific defect was proven. Map render returned `MAP_RENDERED` with `offlineRepresentation = true`, so it is not live-game evidence.
- Technology inspect/render of `infantry_weapons` returned `TECH_INSPECTED`/`TECH_RENDERED`, revision `77028210623df21c78442a308e855dcb42d4fb3bb547ccbf0818e1d50c8bf5af4`, with 1,360 blocking global diagnostics and `sourceAccurate = false`. No custom GLC technology source was changed.
- The exposed HOI4 technology routes do not prove a standalone Technology Tree Viewer. A standalone viewer is absent from the installed environment and is recorded as a tooling/package gap.
- No live-game, save/load, portrait-rights, flag-provenance, or MCP-backed probability receipt was claimed. The user remains the owner of live consumer validation.

## Changed files and before/after

Gameplay files changed by this agent: none. The only file added by this audit is this handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_glc_package_reaudit_2026-09-05.md`.

Before: IW-015 is a vanilla GLC adapter with source-wired setup, cleanup, roster, force, focus, decision, and AI references, but it is not centrally content-attested or Join-admitted.

After: identical. No tag, state, leader, portrait, flag, localisation, focus, decision, idea, force, AI, probability, dispatch, attestation, Join, or FORM-07 behavior was changed. No concurrent worktree edits were reverted, staged, or committed.

## Remaining blockers

1. Independent GLC flag identity/rights/provenance and an explicit opening-identity receipt remain unresolved; no flag asset or identity was invented.
2. Castelao portrait rights/provenance and the `source_placeholder` versus `styled_final` lifecycle terminology conflict remain unresolved; no portrait fallback or relabel was applied.
3. Typed package-specific AI/probability evidence is blocked because `chaosx_ai_probability_auditor` is unavailable as a callable route; no weighted logic was touched.
4. Central content attestation, capacity/SCN-008 release, and Join admission remain intentionally closed for IW-015.
5. FORM-07 remains independently fail-closed until its identity, flag, and complete-member-package gates are resolved.
6. The Event/Map/Technology MCP workspace reports are partial or globally diagnostic-heavy, and the standalone Technology Tree Viewer is absent; these limits prevent stronger engine-side acceptance claims.
