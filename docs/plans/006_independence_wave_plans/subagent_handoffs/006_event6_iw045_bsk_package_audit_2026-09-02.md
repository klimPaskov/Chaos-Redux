# IW-045 BSK Bashkiria country-package audit

Date: 2026-09-02

Scope: Chaos Redux Event 006 Independence Wave, IW-045 Bashkiria, carrier tag `BSK` only. This is a read-only package audit with no gameplay edits. The package reuses the vanilla BSK carrier and state 651 (Ufa); it is not a new country, identity redesign, or formable-family implementation.

## Disposition

No BSK-owned source defect was proven. Do not apply a gameplay patch from this audit. Current source admission is centrally wired, the BSK setup/final/cleanup package is internally connected, and the package-local map, roster, focus hooks, decisions, ideas, localization, flags, and AI references are present. Event 006 as a whole remains `HOLD / PARTIAL` in the current authority records.

The one concrete package-documentation issue is stale wording in `docs/events/006_independence_wave/bashkiria_package.md:17,23`: it still says central attestation, normal/scenario preflight, and Join admission are pending/fail-closed, while the current authority records and source already include IW-045. This handoff records the contradiction; no gameplay file was changed. The same package page still says its package-local checks pass at `:17` and correctly records the oilfield idea lifecycle repair at `:19`.

The current source-of-truth map marks BSK centrally content-attested and records the exact normal/SCN-008 host, state-651, roster, force, asset, and cleanup contract at `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:471-477`; its current package boundary is summarized at `:620`, and its current focus closure is at `:626`. The accepted candidate row is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:46`; research resolution is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:46`; force identity is `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:46`; and the package manifest calls out BSK's current archive/force/admission contract at `docs/specs/006_independence_wave_specs/quality/package_manifest.md:31,83`.

## Country-package coverage checklist

| Surface | Status | Evidence |
| --- | --- | --- |
| Carrier/tag registration | Covered by vanilla reuse and shared registries | `common/script_constants/006_independence_wave_constants_registry.txt:814-815,832,922`; BSK is intentionally absent from the mod `country_tags` shell because it is a vanilla tag. |
| Central admission/runtime dispatch | Covered | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:44-46,180,302-306,513-515`; IW-045 is in content attestation, runtime dispatch, normal preflight, and SCN-008 preflight. |
| Deterministic Join roster | Covered | `common/scripted_effects/006_independence_wave_join_effects.txt:234-271`, IW-045 at `:263`. |
| Country definition/history | Covered by vanilla carrier | Vanilla `common/countries/Bashkortostan.txt:3-6`; vanilla `history/countries/BSK - Bashkortostan.txt:1-103` has capital 651, three research slots, vanilla technologies, and `recruit_character = BSK_yakov_bykin` at `:101`. No mod country-history override is required for this reuse package. |
| State ownership/controller/core/capital | Covered for the compact anchor | Vanilla `history/states/651-Sov state 5.txt:3-28` defines Ufa, owner SOV at `:10`, VPs at `:16-20`, SOV and BSK cores at `:22-23`, and provinces at `:26-28`; package setup and runtime gates require state 651 to be owned and controlled by BSK. |
| Leaders/characters/portrait | Covered with scoped source placeholder | Vanilla `common/characters/BSK.txt:2-6` defines `BSK_yakov_bykin` and vanilla `GFX_portrait_Yakov_Borisovich_Bykin`; `interface/006_independence_wave_portraits_registry.gfx:116-123` wires the package sprite; shared roster checkpoint wiring is `common/scripted_effects/006_independence_wave_effects.txt:3167-3184`. The portrait remains a source placeholder, not a provider-backed styled final. |
| Flags/cosmetic tags | Covered | Four route ladders have neutral/medium/small files under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`; cosmetic IDs are `BSK_INDEPENDENCE_WAVE_CIVICX`, `AGRARIANX`, `SOCIALISTX`, and `EMERGENCYX` in `common/countries/cosmetic.txt:1810-1830`. |
| Parties/politics/laws | Covered | Setup politics and route changes are in `common/scripted_effects/006_independence_wave_bashkiria_mari_package_effects.txt:139-235`; canonical party/cosmetic localization is in `localisation/english/006_independence_wave_bashkiria_mari_l_english.yml:3-71`. Baseline laws are set at effects `:139-143` and prepared setup checks them in triggers `:145-159`. |
| Focus loading/hooks | Covered by shared tree and five BSK hooks | `common/national_focus/006_independence_wave_focus.txt:121,174,208,1447,1718`; BSK-specific setup requires the full shared framework and assignment in `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt:145-206`. |
| Decisions/mission | Covered | `common/decisions/006_independence_wave_bashkiria_mari_decisions.txt:8-555` contains the founding mission and ten serialized BSK projects; category metadata is also in `common/decisions/categories/006_independence_wave_categories.txt:17-24`. |
| Ideas/lifecycle | Covered | `common/ideas/006_independence_wave_ideas_registry.txt:820-862` defines seven BSK ideas; setup/removal/route refresh is in `common/scripted_effects/006_independence_wave_bashkiria_mari_package_effects.txt:4-54,321-399,409-470`. `bsk_oilfield_council` is added by the oilfield reward at `:255-265` and removed by setup/cleanup. |
| Military/technology/industry/supply | Covered at intended compact scope | Force identity is checked in triggers `:180-188` as `mounted_mobile` with p45 tradition; the research/history and no-navy/no-air boundary are in vanilla country history plus triggers `:194-206`. No BSK-specific technology tree is declared. |
| AI | Covered source-wise; quantitative pass blocked | BSK strategies are in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:150-218`, including survival, host restraint, settled frontier, and emergency guard factors. No patch was made. |
| Formable/claims/cores | Intentionally bounded | BSK setup explicitly requires no formable family in `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt:178-184`; the vanilla BSK core on state 651 is retained. Extended claims/formables are outside this package's compact anchor contract. |
| Localization/assets/cleanup | Covered with documented rights/runtime caveats | Canonical package keys are in localization `:3-126` and aliases at `:75-94`; flags are complete for all three sizes; setup/final/cleanup dispatch is in `common/scripted_effects/006_independence_wave_bashkiria_mari_package_effects.txt:321-470`. |

## File-surface checklist and findings

### Registration, setup, state, claims, and cleanup

The exact package gate `is_independence_wave_bashkiria_package` is defined in `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt:4-10` and binds `original_tag = BSK` to `constant:independence_wave_package_id.iw_045`, with the Soviet-collapse origin exclusion. Setup eligibility and the state/host/capital contract are `:73-89`; exact tag availability and dormant-state safety are `:95-105`; stable ledger thresholds are `:107-119`; complete setup requires prepared setup, shared and BSK setup flags, origin activation, aligned arrays, and network membership at `:208-218`.

Package setup is `common/scripted_effects/006_independence_wave_bashkiria_mari_package_effects.txt:321-399`. It clears stale package flags/ideas/ledgers, applies the roster and command checkpoint, initializes laws/politics, wires the shared focus framework and route gates, sets the power struggle and ambition/league state, clears and reapplies the five force pathways, assigns dynamic force mapping, and applies the BSK AI profile. Final validation is `:401-407`; package-only decision/idea/portrait/politics/ledger cleanup is `:409-470`.

The ten project IDs are listed by the active-project guard at `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt:121-133`. Their decision definitions and cancel/affordability/capital checks are `common/decisions/006_independence_wave_bashkiria_mari_decisions.txt:13-555`. The corridor trigger uses `independence_wave_bsk_volga_ural_corridor_open` at decisions `:500-555`; the matching effect is `:304-319`. The founding mission cancellation guard includes the setup receipt at decisions `:21-33` and is not counted as a project in the active-project OR list by design.

The category key is present in both the category registry (`common/decisions/categories/006_independence_wave_categories.txt:17-24`) and the consolidated package decision file (`common/decisions/006_independence_wave_bashkiria_mari_decisions.txt:8`) because the latter owns the executable decision children. Vanilla uses the same consolidated pattern in places; no parser or runtime defect was proven, so no category rewrite is justified.

No BSK-specific release, annexation, puppet, civil-conflict, or global on-action cleanup defect was found. Shared generation reset is intentionally owned by `common/scripted_effects/006_independence_wave_effects.txt:468-493` after package cleanup. No BSK-specific map mutation, supply/rail/port/resource/building override, or additional state claim is present or required by the compact state-651 contract.

### Politics, leader, portraits, flags, parties, advisors

Vanilla BSK has the sourced historical leader `BSK_yakov_bykin`; the package does not use a random personal name pool and therefore has no opposite-gender pool pairing risk. The package portrait is character-scoped and restores the vanilla token during cleanup; it never overrides the global vanilla sprite (`interface/006_independence_wave_portraits_registry.gfx:116-123`, effects `:3167-3184` and `:409-470`). The current portrait archive-repair handoff is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw045_bsk_portrait_archive_repair_2026-09-02.md`; it restores source crop/provenance/manifest/review evidence only, leaves runtime DDS/GFX unchanged, and records Wikimedia attribution/rights obligations as open. No portrait-specific gameplay patch is justified.

Route party names, long names, adjectives, and four cosmetic ladders are localized in `localisation/english/006_independence_wave_bashkiria_mari_l_english.yml:3-71`. The same file supplies seven idea names/descriptions at `:73-94`, the category/mission/decision text at `:97-126`, and compatibility aliases for older idea IDs. No BSK-specific advisor or high-command addition is required by the accepted package contract; the carrier retains vanilla character content.

The four route flag ladders each have neutral/medium/small TGA files: `BSK_INDEPENDENCE_WAVE_CIVICX`, `BSK_INDEPENDENCE_WAVE_AGRARIANX`, `BSK_INDEPENDENCE_WAVE_SOCIALISTX`, and `BSK_INDEPENDENCE_WAVE_EMERGENCYX`. The package documentation correctly treats the 1918 Bashkurdistan reference as a route restoration reference rather than a universal 1936 baseline. The asset evidence is source-placeholder/route-owned and does not claim an unapproved final or rights clearance.

### Focus, decisions, ideas, and shared UI/event hooks

The current shared focus tree inspection returned `FOCUS_INSPECTED` with 184 focuses and 195 connectors, zero crossings, zero node intersections, zero long connectors, zero same-row issues, and zero Event 006 layout diagnostics. Render validation passed. The tree is shared by design; no BSK-specific focus tree is missing. The five BSK hook IDs are present at `common/national_focus/006_independence_wave_focus.txt:121,174,208,1447,1718`.

The current `.350` event scan and overview render returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` with zero selected blocking diagnostics. The bounded tool pass deferred workspace-wide helper/lifecycle projection; a full state-flow call timed out. This is engine evidence for the selected event surface only, not a live event or save/load proof. The roster checkpoint entry is `events/006_independence_wave.txt:142-155`.

The shared Statehood Ledger GUI is a dependency rather than BSK-owned UI. `interface/006_independence_wave.gui:10-70` and `common/scripted_guis/006_independence_wave_scripted_gui.txt:10-104` inspected successfully with complete source graph and no missing elements. The render passed source validation at 1920x1080 and 1366x768. Four nonblocking animation static-fallback warnings remain at `interface/006_independence_wave.gfx:67,70,73,76`, and generated state coverage did not include every hover/locked/selected state; these are shared parent-scope follow-ups, not BSK defects.

### Military, technology, industry, supply, and production

The BSK prepared gate requires the dynamic force package ID/profile/current generation, applied force mapping, five pathway flags, and no navy/air at triggers `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt:180-206`. The force mapping constants record p45 at `common/script_constants/006_independence_wave_constants_registry.txt:2072,2286,2500,2714,2928,7761`; BSK resolves to `mounted_mobile` at `:184` and p45 tradition 70 at `:185`. The accepted mapping file identifies mounted frontier guards, frontier infantry, and defecting units, with no inherited navy/air. No additional equipment, OOB, production line, convoy, train, or supply patch is in scope or supported by source evidence.

Vanilla BSK history remains authoritative for capital, three research slots, vanilla technology, and no OOB. The Technology Tree Viewer is not installed. A read-only `hoi4_tech_inspect` explain call for `infantry_weapons` returned global workspace diagnostics but no BSK-specific diagnostic; the technology render timed out. These limitations prevent a package-specific engine technology receipt, but do not identify a BSK source defect.

### AI and probability

The BSK AI block at `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:150-218` uses centralized constants for army, infantry, artillery, support, infrastructure, bunker, emergency, and founding/settled war-restraint factors. The source checks are gated by `original_tag = BSK`, package/setup flags, host-ledger state, compact stabilization, and emergency government. No weighted AI patch was made.

Read-only `hoi4_probability_inspect` on `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` returned `PROBABILITY_SOURCE_DISCOVERED`, `no_weighted_surfaces`, zero candidates, zero required inputs, and zero unresolved items (artifact hash `9fa2ceabcceb79e6d2240ceac219e1c3304c6c4ca2ae42003958452ecad10ae7`). Read-only inspection of the consolidated BSK/Mari decision source returned 22 candidates, zero currently available candidates, `poolComplete = false`, 17 required inputs, zero unresolved diagnostics (source hash `7ec5e57359cb10718d4093043746f9f1125ba60eea9654d54ec84f610a20e1d7`). This is not a typed world-state balance result.

The required `chaosx_ai_probability_auditor` route is not callable in this installation; exact tool search returned `NO_CALLABLE_CHAOSX_AI_PROBABILITY_AUDITOR`. Therefore no current scenario evaluation or probability compare is claimed. The older BSK probability handoff dated 2026-08-14 is historical partial evidence only and does not replace the missing current auditor route.

## Engine-facing validation receipts

The following read-only receipts were collected against workspace `mod_chaos_redux_ea3b2d67c2c0`:

- Focus inspect: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/789f8c03431443728809758ba7208eb8dc880e7e04ab1ac6856917106de36e61/7e00ecca067ec07a626d9a56c6aa8f127ea8e5004145b3c534a7213cf124064a/focus-inspect.2e94fc9df83d9bd5.json`; layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.
- Focus render: SVG artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/790ac83c6f2cdb9816133b30e7a650f0e74f3823cf45efd0753fa9182ec87279/e6ea835ebdd6ee2d7830ebd869b147f679c6707ddf995525b7c7d2d8299910ea/independence_wave_focus_tree.focus.svg`; validation passed.
- State-651 map inspect: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8a9f99f1408d5e51513022b65fdf22bd418141592bd7b8f74fdec74b7fdab24/9dc2db902a7303610518086d448974f8ab7b1d591972bf1df2d0b7173b1bad95/map-inspect.d64d08d1b4ec7e58.json`; no state-651-specific diagnostic. Workspace-global map errors are `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` in `map/buildings.txt`, unrelated to BSK state 651.
- State map render: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2bf654fe1fc69bb1d744cc187c83e11314a368893a0c6ecd38948ae3e7c901e/7eb7b90f9e879205bdac4012ab1f2c2f695394a74256c78edf10e3022221c459/map-state.png`; validation passed.
- Event `.350` bounded scan: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6cab191a83f53d8b270288b5e53bedf029e404eec5d9eca2a325566236345a3/f6125e19142678f3017996d5160e53d1002d67a2cd7aebcf299f5a86f43e669d/event-scan-d9bc467fb6be.json`; selected blocking diagnostics 0; workspace helper/lifecycle projection deferred.
- Event overview render: manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6eb34cf06c86ddfb2be71b96155a7b8c25dc1c66497c5af9456418da9c56972e/848978e5bd3602469da8dd4de1dc7999d06ea1674ad39d0f5fcd2ccde5416dca/event-overview-d9bc467fb6be-manifest.json`; selected nodes rendered with zero blocking diagnostics; workspace projection remained partial.
- Shared GUI inspect: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6fe1c3c4a94cb1b51648573e06302bd30465e6e59877c5f78e1433c8b5bf7020/e9f00f88514492576425569c0eb27b3a56d0b5ec1080c37a05af24adfdd35016/gui-inspect.a3d81dd2e4d24525.json`; complete source graph and no missing elements.
- Shared GUI render: full SVG artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91d0ea54096e21ca00e240c306658ce767560d5336689393290017bc67c7b0e8/65d0d016e71b54f74ce61f5b4872d473b864780420cf93a63a68eac14d8f8e04/independence_wave_status_window-full.svg`; source validation passed at both requested resolutions.
- Technology explain: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3544f0aa49db25a1fb4fba7f1737e4c273ac71ab3e623f42a52e3b0e3cf8d1a/6e5279e516f1684c077d71de6828ef4bb9a3a3a97ea3bac04cd383e63837b42b/technology-explain-627e27e6dc7f.json`; global diagnostics only. Technology render timed out.

## Unresolved blockers and uncertainty

1. The `chaosx_ai_probability_auditor` custom route is unavailable, so the required delegated probability pass and current scenario compare cannot be claimed. No weighted source was changed.
2. The installed package exposes no Technology Tree Viewer; technology rendering also timed out. Only vanilla history and read-only technology explain evidence are available.
3. Full Event `.350` state-flow inspection timed out; the bounded scan/render are partial because helper/lifecycle projection was deferred for the large workspace. They found zero selected blocking diagnostics but are not live runtime proof.
4. Workspace-global map diagnostics remain in `map/buildings.txt` and are not state-651-specific. Shared GUI static-fallback warnings remain at `interface/006_independence_wave.gfx:67,70,73,76`.
5. The BSK portrait is a source placeholder. The archive-repair handoff restores provenance/crop/manifest/review evidence, but Wikimedia attribution/rights obligations remain open and no styled-final promotion is claimed.
6. Current authority files contain a date inconsistency: the environment date is 2026-09-02, while reconciliation headers in `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:3` and `docs/specs/006_independence_wave_specs/README.md:23` are dated 2026-09-03. This affects documentation chronology only.
7. No live game, save/load, or non-empty transaction receipt was run or claimed, per task boundary.

## Changed files

None. This audit created only this handoff. No BSK gameplay, localization, asset, registry, map, or shared-system file was modified, staged, or committed.

## Skills and references applied

The audit followed `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-comfyui`. Required offline Paradox wiki pages and the relevant vanilla documentation files were read before source review. Vanilla BSK country, character, history, state, and flag/cosmetic precedents were inspected. The portrait skill boundary was respected: no portrait generation, RunPod operation, or runtime fallback was performed.
