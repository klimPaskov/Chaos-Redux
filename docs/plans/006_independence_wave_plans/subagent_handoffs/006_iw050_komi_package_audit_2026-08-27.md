# Event 006 IW-050 Komi bounded package audit

Date: 2026-08-27

Scope: Read-only package review of IW-050 (Komi, carrier `KOM`, anchor state 397 Syktyvkar, reservation group `RG-397`). This handoff does not admit the package to Event 006 and does not widen any central OR-list, preflight, dispatcher, capacity, or Join surface.

Disposition: PACKAGE-LOCAL / EVIDENCE-BLOCKED / NO GAMEPLAY PATCH.

## Authority and evidence boundary

The current source-of-truth map remains HOLD / PARTIAL. It records 32 content-attested selectable packages across 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows out of 193 non-overlay rows. IW-050 remains explicitly package-local or research-only in `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and in both current improvement addenda.

The IW-050 contract is defined by `docs/plans/006_independence_wave_plans/006_event6_improvement_addendum_2026-08-24.md`, `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, and `docs/events/006_independence_wave/komi_package.md`. The 2026-08-26 receipt audit is the current historical context for the setup-receipt cancellation guard; it does not constitute central admission evidence.

Required offline Paradox wiki pages and the relevant vanilla documentation were consulted for country/history, scopes, triggers/effects, events, decisions, ideas, focuses, maps, AI, localisation, and technology references. No web source or unapproved fallback was used.

## Package coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Tag registration | Static pass for carrier reuse | Vanilla `common/country_tags/00_countries.txt:232` maps `KOM` to `countries/Komi.txt`; `common/country_tags/006_independence_wave_countries.txt` intentionally has no duplicate `KOM` entry. |
| Country/history | Static pass for reused carrier | Vanilla `common/countries/Komi.txt` and `history/countries/KOM - Komi Republic.txt`; capital 397, three research slots, vanilla technologies/doctrines, and democratic/fascist/communist starting popularities. No mod country/history replacement is present. |
| Anchor/reservation | Static pass, engine proof unavailable | `006_state_anchor_and_reservation_groups.csv` and `006_current_installed_map_package_bindings.csv`: anchor 397 Syktyvkar, optional 262/581, `RG-397`, protected-host rule, and SOV remnant state 219. |
| Package identity | Package-local pass, admission absent | `006_independence_wave_komi_package_triggers.txt` defines the package, dormant tag proof, setup proof, and runtime-ready proof. |
| Setup/lifecycle | Package-local pass | `006_independence_wave_komi_package_effects.txt` provides idempotent setup, lifecycle, route, force, AI, final-validation, and generation-safe cleanup effects. |
| Roster | Blocked on rights/identity gate | `has_independence_wave_komi_command_roster` requires `independence_wave_iw_050_identity_rights_cleared` and `KOM_pavel_murashev`. |
| Portrait | BLOCKED | Only vanilla `KOM_pavel_murashev` is wired, with generic `gfx/leaders/Europe/Portrait_Europe_Generic_3.dds`; no defensible Event 006 portrait provenance/final is installed. |
| Flag/symbol | BLOCKED | Mod has only Event 005 `KOM_democratic` flag variants; no Event 006 route/neutral flag package or stable symbol provenance is admitted. |
| Central admission | BLOCKED / intentionally absent | No IW-050 branch in central runtime adapter, content attestation, normal/scenario preflight, setup/final-validation/cleanup dispatch, capacity, or deterministic Join. |
| SCN-008 | Rank is non-admission evidence only | Current map records SCN-008 as 8 modes x 4 intensities, 6 numeric families, and 3 Universal Belligerence rows; IW-050 remains outside the admitted 32-package set. |

## File-surface checklist and findings

### Identity, politics, leader, portrait, flag, and advisors

`common/scripted_effects/006_independence_wave_komi_package_effects.txt` sets baseline `civilian_economy`, `export_focus`, and `volunteer_only`, establishes democratic provisional politics, and defines four party names and four government routes: Taiga Congress Charter, Taiga Land Compact, Rail and Forestry Councils, and Taiga Emergency Command. The seven package ideas in `common/ideas/006_independence_wave_ideas_registry.txt:2867-2938` are package-gated and have corresponding localisation in `localisation/english/006_independence_wave_komi_l_english.yml`.

The vanilla character `KOM_pavel_murashev` is the only roster character found. `common/characters/KOM.txt` gives Pavel Murashev a country-leader entry and generic European portrait path, but does not establish the rights-cleared source required by the package contract. No opposite-gender random-name pairing was found: the package does not draw a generated leader name pool and the vanilla leader has no female metadata. This does not clear the portrait/source gate.

`docs/events/006_independence_wave/komi_package.md` correctly rejects Event 005 committee art, unrelated Murashev material, invented office portraits, and generated substitutes as evidence. The next owner for this gate is `chaosx_portrait_creator`, with grounded source/rights evidence or an explicitly approved fictional portrait package and portrait-specific wiring.

The symbol gate remains unresolved. Vanilla has the normal KOM ladder (`KOM_communism`, `KOM_democratic`, `KOM_fascism`, `KOM_neutrality`), while the mod’s only KOM flag files are Event 005 democratic variants under `gfx/flags/`. The package documentation records unstable encoding/provenance for the installed ladder and requires a stable policy before reuse. No new flag or GFX patch is safe in this audit.

No package-specific advisors, high command, commanders, or new character definitions are present. The reused vanilla character is guarded by the package’s roster trigger.

### Map and state setup

The static package binding is coherent: state 397 is Syktyvkar and the compact extension candidates are 262 and 581. `RG-397` requires preserving the host’s protected state first and trimming optional territory before the anchor. Event 005 owns the same KOM carrier and states in its separate collapse ladder, so any later runtime admission must prove generation and origin separation rather than relying on tag presence.

Fresh `hoi4_map_inspect` for state 397 and `hoi4_map_render` for state, coastline, port, victory-point, resource, supply, railway, and adjacency layers both returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with `artifactCount: 0`, `filesScanned: 0`, and no diagnostics. Therefore no current engine map receipt is claimed. There was no map write.

### Focus, decisions, missions, ideas, and assets

IW-050 uses the shared `independence_wave_focus_tree`, not a bespoke tree. The five package callbacks are in `common/national_focus/006_independence_wave_focus.txt` at the `convene_northern_congress`, `secure_railhead_communities`, `integrate_forest_guards`, `settle_former_host_ledgers`, and `open_pechora_corridor` helper calls. The current source map records 184 focuses and 195 connectors with zero layout diagnostics, but fresh focus inspect and render both returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with no artifact. The shared-tree count is not treated as fresh engine proof.

`common/decisions/006_independence_wave_siberian_decisions.txt` contains one 420-day founding mission, `independence_wave_komi_hold_northern_council`, plus ten paid projects covering depots, rail guards, community registration, former-host ledgers, four government routes, durable sovereignty, and the Pechora corridor. The setup-receipt cancellation guard from the 2026-08-26 audit is present. Category registration is in `common/decisions/categories/006_independence_wave_categories.txt:363-370`. No direct decision/mission MCP route is exposed by the installed server, so these remain source-static findings.

No package-specific technology or doctrine is added. Vanilla KOM starting technologies/doctrines were inspected from the carrier history. The installed package exposes no Technology Tree Viewer, so technology-tree rendering/acceptance remains an unresolved limitation and no technology claim is made beyond static vanilla reuse.

### Starting military, technology, industry, supply, and production

The force mapping is `p50 mountain_frontier` with tradition 55 in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:51`. Setup requires exactly five named reinforcement pathways, applies no inherited navy or air force, and uses the package’s cold-weather/forest-defense profile. Vanilla history supplies three research slots and its ordinary Komi technology baseline; the package does not add large armies or major industrial changes. Rail, supply, resource, port, and victory-point behavior remain dependent on the unverified current map receipt.

### AI and probability

`common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:1542-1610` defines four package-gated strategies: `independence_wave_komi_taiga_survival`, `independence_wave_komi_host_restraint`, `independence_wave_komi_settled_northern_republic`, and `independence_wave_komi_emergency_taiga_command`. The source constants cover army, production, support, artillery, infrastructure, defense, emergency build, and founding/settled war restraint. No weight patch was made.

Fresh `hoi4_probability_inspect` on the national-focus source returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with no artifact. The required `chaosx_ai_probability_auditor` callable route is not exposed in this runtime, so no typed scenario evaluation or balance acceptance is claimed. The AI-strategy source inspect did succeed with `PROBABILITY_SOURCE_DISCOVERED` and artifact URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43aca06d5c3833b9f939906398346c2a889590e3dc29e17960490801716e3551/291a9b75f2871d660f965be5d2ef5c375ffc8163306f21ce0171a43ada1de3c1/probability-inspect-a35190937fed.json`; it reported `discoveryReason: no_weighted_surfaces`, zero candidates, zero unresolved inputs, and validation passed. That is a source-discovery receipt, not a quantitative AI balance result.

The ten named package scenarios remain the required future probability fixtures: `KOM_FOUNDING_SAFE`, `KOM_CAPITAL_THREATENED`, `KOM_RESOURCE_STARVED`, `KOM_CONSTITUTIONAL_ROUTE`, `KOM_POPULAR_COUNCIL_ROUTE`, `KOM_TRADITIONAL_ROUTE`, `KOM_EMERGENCY_WAR`, `KOM_FORMER_HOST_SETTLED`, `KOM_LEAGUE_CORRIDOR_READY`, and `KOM_ORIGIN_ENDED_FAIL_CLOSED`.

## Event, network, formable, and cleanup boundaries

Fresh `hoi4_event_inspect` and `hoi4_event_render` for `chaosx.nr6.1` returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with no artifact. The event root is therefore not claimed as a current engine receipt for this package.

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` contains the current 32-package adapter and content-attestation OR-lists; IW-050 is absent from both. The same file’s normal and scenario preflight branches contain no IW-050 exact branch. `common/scripted_effects/006_independence_wave_join_effects.txt` has the fixed 32-ID `independence_wave_join_probe_attested_package` order and excludes `iw_050`. This absence is intentional under the addendum, not a stale reference to repair.

`common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt` and `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` do contain planner/load/reservation entries for IW-050, including `KOM`, state 397, and optional 262/581. These are candidate-planner surfaces and do not constitute central content attestation or runtime admission.

Formable consumers in `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt` reference state 397 and the Komi carrier in existing invitation/member checks. Those existing formable checks must remain separate from an IW-050 admission decision; no formable patch was justified.

Package cleanup in `common/scripted_effects/006_independence_wave_komi_package_effects.txt:412-458` removes the mission, ten decisions, seven ideas, route/lifecycle flags, ledgers, AI profile, and provisional state, then restores vanilla politics and party names. This is generation-guarded package cleanup and was not changed.

## Mandatory MCP evidence and exact limitations

The following fresh read-only calls were made against the current workspace and failed with the exact repository response `ARTIFACT_MANIFEST_INTEGRITY_FAILED`, `artifactCount: 0`, `filesScanned: 0`, and no diagnostics: focus inspect, focus render, map inspect, map render, event inspect, event render, and national-focus probability inspect. No fallback parser or stale artifact was substituted.

No `hoi4_country_inspect` route and no direct decision/mission route are exposed by the installed MCP server. No Technology Tree Viewer is exposed. The probability auditor subagent route is also not callable from this runtime. These are explicit validation blockers, not evidence that the package is broken.

## Blockers and next-owner recommendation

1. Resolve the exact KOM leader/institution source and portrait rights/provenance, then route the complete portrait package through `chaosx_portrait_creator`. Do not use generic vanilla, Event 005 committee art, or an unapproved generated/source fallback.
2. Resolve stable KOM flag/symbol provenance and route/identity policy through the event-asset owner. Rehash and document any reused ladder asset before wiring it to Event 006.
3. After identity and symbol gates clear, the parent/central integration owner must add the exact IW-050 adapter, content attestation, normal/scenario preflight, setup/final-validation/cleanup dispatch, capacity, automatic readiness, and deterministic Join branches atomically. The package’s existing planner entries must not be mistaken for those branches.
4. Repair the artifact-manifest integrity condition, then rerun the exact country-adjacent focus, event, map, and probability receipts. Route the ten named scenarios through `chaosx_ai_probability_auditor`, including same-scenario compare only if weights or gates change.
5. Recheck SCN-008 rank after the above evidence exists; rank alone must not promote IW-050 or alter the current 32-package admission set.

## Changes, validation, and simplifications

Only this audit handoff was added: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw050_komi_package_audit_2026-08-27.md`. No gameplay, localisation, asset, map, AI, central admission, spreadsheet, or generated-file patch was made. No fallback, provisional admission, identity substitution, or balance simplification was used.

The audit is complete as a bounded package review, but IW-050 admission is incomplete and intentionally remains blocked on identity/portrait, flag/symbol, and missing engine/central evidence.
