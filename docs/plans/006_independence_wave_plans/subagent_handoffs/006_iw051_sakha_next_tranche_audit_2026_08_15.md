# IW-051 Sakha/YAK next-tranche audit — 2026-08-15

## Disposition

`BLOCKED / FAIL-CLOSED — documentation only.`

No gameplay, asset, central-admission, preflight, attestation, or Join source was changed. The package-local tranche is structurally bounded in ownership, but it is not safe to land until the identity/asset and current-map gates below are closed. This handoff supersedes the older `006_iw051_sakha_package_audit_2026_08_14.md` for the current Event 006 source state.

## Executive decision

The Event 006 registry and Region 05 planner already carry a source-backed IW-051 contract, and the central force dispatch already contains the accepted YAK force profile. The package-local Sakha source family is absent, so adding constants, triggers/effects, ideas, AI, decisions, localisation, or focus hooks now would create content that cannot be admitted by the central runtime and would require unapproved identity/asset assumptions.

The nearest safe alternative is to keep IW-051 fail-closed, resolve the sourced leader or institutional identity and released-origin flag provenance, revalidate the installed-map anchor, then implement only the package-local files listed under the future ownership split. No central adapter, attestation, preflight, scenario, or Join edit belongs in this tranche.

## Existing source-backed contract

| Contract | Current source and finding |
| --- | --- |
| Package | `IW-051` / `constant:independence_wave_package_id.iw_051` |
| Registered carrier | `YAK`, reuse registered tag, automatic pool only if not living |
| Reservation | `RG-574`, anchor state `574` / Yakutsk, optional extensions `644`, `876`, `877` |
| Region/depth | `volga_urals_siberia_far_east`, regional |
| Planner archetype | `nomadic_or_dispersed` |
| Force contract | profile `4` (`mountain_frontier`), tradition `62`, reinforcement mask `647`, inheritance mask `0`, research-sensitive `0` |
| Formable boundary | `FORM-14` Siberian Federation; no automatic package formable |

The accepted registry row is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:52`. The accepted research row is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:52`, and it requires a defensible sourced male period leader or authentic archival institution, released identity/origin matching before flag reuse, current-map ID rebinding, host protection, collision review, and final asset provenance.

The state and reservation row is `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:46`. The force row is `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:52`. The installed-map binding is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:52`.

The current Region 05 loader is `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:85-95`. It saves vanilla `YAK` as the candidate carrier and state `574` as the anchor, with the host as the primary host. The reservation effect at `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:194` reserves `574` and tries `644`, `876`, and `877`; the Region 05 weight preparation and random dispatch include IW-051 at lines `165` and `210`.

The planner gate is `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt:64-70`. It checks the open plan, remaining slot, package and reservation uniqueness, generic `YAK = { is_independence_wave_candidate_tag_available = yes }`, and anchor availability. The generic tag gate currently bottoms out at `has_country_flag = independence_wave_package_content_ready`; it does not prove an IW-051-specific identity, portrait, flag, or lifecycle packet. Leave that central gate untouched and do not assert the content-ready flag from a speculative local file.

The scenario ranking already includes `constant:independence_wave_package_id.iw_051` in `common/scripted_effects/006_independence_wave_scenario_effects.txt`. This is registry evidence only, not admission evidence.

## Central admission boundary

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-213` requires an existing country absence, a runtime package adapter, a content attestation, no Soviet-collapse origin flags or variables, and no active Event 006 origin. The current dispatch file contains 40 runtime adapter IDs and 32 content-attestation IDs; `iw_051` is in neither set. Therefore IW-051 cannot execute through the central runtime or Join path today.

This audit does not widen either central list. The package-local tranche must remain independently fail-closed until the parent owns a later admission change. Existing Join logic in `common/scripted_effects/006_independence_wave_join_effects.txt` is limited to compile-time-attested adapters and is out of scope here.

## Vanilla carrier and identity review

Vanilla maps `YAK` to `countries/Yakutia.txt` in `common/country_tags/00_countries.txt`; `common/countries/Yakutia.txt` uses Asian graphical cultures and a cyan country colour. Vanilla `history/countries/YAK - Yakutia.txt` uses capital `574`, two research slots, generic infantry/recon/engineer/military-police/mountaineer/truck/motorized/paratrooper/artillery technology, Mass Assault and New Fleet in Being doctrines, democratic elections and popularity, and no active OOB (`#oob = "YAK_1936"` is commented).

Vanilla characters are `YAK_pavel_pevznyak` with `GFX_portrait_Pavel_Pevznyak` and `YAK_anatoly_pepelyayev` with `GFX_portrait_Anatoly_Pepelyayev` in `common/characters/YAK.txt`. Their vanilla portrait definitions resolve to generic Asian textures in `interface/_leader_portraits.gfx`; that does not satisfy the Event 006 research requirement for a sourced released identity. Event 005 separately creates the institutional leader `Lena Resource Board` through `common/scripted_effects/005_soviet_collapse_effects.txt:14910-14917`, wired to `interface/005_soviet_collapse.gfx:1962` and `gfx/leaders/005_soviet_collapse/YAK_leader.dds`. That Event 005 institution is not automatically approved as the IW-051 identity and must not be repurposed without source and lifecycle review.

Vanilla ideology flags exist for YAK under the normal, medium, and small flag folders. Flag reuse remains blocked until released identity/origin matching and provenance are recorded. No new flag, leader, portrait, portrait path, or fictional institutional identity may be invented in this tranche. Any portrait production belongs to `chaosx_portrait_creator` after the source identity is approved.

## Map and host gates

The accepted binding reserves `574`, with optional `644`, `876`, and `877`, all currently source-bound to `SOV` and with `SOV = 219` as the host reference. Vanilla state `574` is Soviet-owned, has YAK and SOV cores, and has Yakutsk as its capital; the source history files were not changed.

The required read-only map inspection of states `574`, `644`, `876`, and `877` returned `MAP_INSPECTED` with complete state/network checks and no unknown province IDs, but position/port validation remained false in the globally noisy workspace. A direct dry-run allocation probe for state `574` returned the exact blocker `MAP_STATE_ID_COLLISION`. This means the numeric binding is not sufficient evidence of current installed-map admission; the parent must rebind and validate the anchor and host-remnant protection before runtime use.

## Package-local file coverage

The following owned package-local files are currently absent:

- `common/script_constants/006_independence_wave_sakha_constants.txt`
- `common/scripted_triggers/006_independence_wave_sakha_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_sakha_package_effects.txt`
- `common/ideas/006_independence_wave_sakha_ideas.txt`
- `common/ai_strategy/006_independence_wave_sakha.txt`
- `common/decisions/categories/006_independence_wave_sakha_categories.txt`
- `common/decisions/006_independence_wave_sakha_decisions.txt`
- `localisation/english/006_independence_wave_sakha_l_english.yml`
- `common/national_focus/006_independence_wave_sakha_focus.txt`

There are no package-specific `independence_wave_yak`, `independence_wave_sakha`, or `iw_051` definitions in those local families. The existing Komi and UDM packages provide the bounded precedent for this file split, guarded package helpers, local ideas/decisions/AI/localisation, and five guarded calls from the shared Event 006 focus file. Those precedents do not remove the IW-051 identity, map, or central-admission gates.

## Surface-by-surface disposition

| Surface | Disposition now | Safe follow-up after gates close |
| --- | --- | --- |
| Constants | Do not add yet | Add only package-local tuning and guard constants in `006_independence_wave_sakha_constants.txt`; consume existing `iw_051`, `rg_574`, state, and force constants rather than duplicating them. |
| Scripted triggers/effects | Do not add yet | Add package-local helpers that require the registered YAK carrier, active IW-051 generation/package, RG-574 reservation, valid state/host relationship, no Soviet-collapse origin, and the accepted force profile. Keep all effects local and fail-closed. |
| Ideas | Do not add yet | Add only Sakha-specific ideas after identity/lifecycle text is approved; use existing shared icons where possible and do not create an icon or asset substitution. |
| AI/probability | Blocked | Add `common/ai_strategy/006_independence_wave_sakha.txt` only after a source exists and the mandatory probability audit can inspect the exact path. No numeric AI claim is made here. |
| Decisions | Blocked | Add the local category and decisions only after costs, trigger tooltips, lifecycle cleanup, and identity wording are approved; no central decision registry or GUI is needed. |
| Focus hooks | Not present, not safe to wire | Follow the Komi/UDM five-guarded-helper pattern in the shared `common/national_focus/006_independence_wave_focus.txt`; do not add a YAK tree or new icons in this tranche. |
| Localisation | Not present | Add UTF-8-BOM localisation together with approved gameplay IDs; do not localise an invented leader, flag, or institutional identity. |
| Technology | No package-local surface | Preserve vanilla YAK history and central force dispatch; do not add a YAK technology tree. |
| Formable/GUI | Explicitly out of scope | Preserve `FORM-14` Siberian Federation as a negotiated federation path and add no automatic formable or dedicated GUI. |

## Required fail-closed gates before implementation

1. Resolve a source-backed YAK leader or authentic institutional identity that is valid for the release context, not active elsewhere, and has portrait-worker provenance or an explicitly approved existing source asset.
2. Resolve released identity/origin matching for the vanilla YAK flag ladder; do not substitute a generated or unproven flag.
3. Rebind state `574` and optional extensions against the installed map, clear the `MAP_STATE_ID_COLLISION`, and prove the former Soviet host remains protected.
4. Add an IW-051-specific content/identity attestation and runtime adapter only in a later parent-owned central tranche; this audit must not add them.
5. Add and inspect the exact Sakha AI source through the mandatory probability route before making any weighted claim. The attempted source route currently returns `PROBABILITY_SOURCE_NOT_FOUND` for the absent `common/ai_strategy/006_independence_wave_sakha.txt`.
6. Re-run focus and event inspections after any shared hook or lifecycle work. The current Event 006 focus inspection/render is partial and reports 14 blocking vanilla continuous-focus icon references; no YAK-specific hook is present. The installed environment exposes no full Technology Tree Viewer, so technology validation remains source-plus-partial-scan only.

## Recommended ownership split

The package owner may implement the nine absent package-local files and the five guarded shared-focus helper calls only after the gates above are accepted. The parent retains ownership of central adapter/attestation/preflight/Join files, registry and scenario rows, map allocation/rebinding, host-origin cleanup, and final runtime admission. The portrait worker owns any new or replacement character portrait and its manifest. No owner should mutate vanilla YAK history, country definition, characters, flags, or state files for this tranche.

## MCP receipts

- Map inspect for `574`, `644`, `876`, and `877`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a7427b4342a818f448a4448f186dd594813dbef97fd0f4e7e650cfa2eafa57b/ed2ca18cf8ae7f9dfa481dce37d64bbc194eeafdfbe392e42d5925b635783766/map-inspect.40b912dc578c3d0a.json`. Result `MAP_INSPECTED`; bounded state/network checks passed, global position/port diagnostics did not.
- Map render with state, victory-point, resource, building, supply-node, and railway overlays: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c1486f717697111835f8a73380f3e38dbd1b153c4b67f3df3fa982ae8e546bb/4d9c5df87c5abbb5568106dd3b1edfdd76a31274054515419b17c4d5caa02460/map-state.png`. Result `MAP_RENDERED`.
- Focus inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3178e5100b67b3f2de6f34c9eda0a74a027b7265ceb845e29d64e5657035e3f/c0f4433374553eed95c15590ac7f18485207cfdedf7f56779a91c8a8d518b421/focus-inspect.4a06542f57301176.json`. Result `FOCUS_INSPECTED_PARTIAL`; no selected YAK hook was found and global missing-icon diagnostics remain.
- Focus render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c5494e0a26011621445ed31c1874bd487e070437b9c142fee14ebb5d672ff9a/ab8d9ae55f7baeff6bd34ca88e658ecb81d0ae60ef7a955d9e3cab57817e5dc1/independence_wave_focus_tree.focus.html`. Result `FOCUS_RENDERED_PARTIAL` with the same global icon limitations.
- Region 05 random-list probability inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b4dd48531593db82a010323a64ec92e7686ba884dc386c10593cbdc0dc411ca5/3029c9da81c82d9ad3f42ab8dab8b31be56315c400d1aedcc28cbd18ffbab8a9/probability-inspect-578028cf856f.json`. Result `PROBABILITY_SOURCE_INSPECTED`, complete 12-candidate pool; no quantitative selection claim is made.
- Sakha AI probability route: exact result `PROBABILITY_SOURCE_NOT_FOUND` for `common/ai_strategy/006_independence_wave_sakha.txt` because the package-local source is absent.
- Technology scan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63dca939fd68f9152518d3ff9891ce1dd310ec98c9a16744f3fa127ef84beffe/29bda80dfe01cf560284fd74804c200d75dcee63d9deed80769320b2e0a880ed/technology-scan-8eca3672b7a0.json`. Result `TECH_INSPECTED_PARTIAL`; no YAK-specific technology edit is justified and no full Technology Tree Viewer is exposed in this environment.

## Validation and remaining gates

Read-only `rg` and file-existence checks confirmed the current registry, reservation, force constants, central dispatch absence, and missing Sakha package family. The only new file from this audit is this handoff. No source implementation or asset wiring was attempted, so there is no gameplay patch to validate.

The actionable blocker is the combination of unresolved identity/portrait/flag provenance and the current-map `MAP_STATE_ID_COLLISION`; central IW-051 adapter/attestation absence is an explicit parent-owned boundary rather than a reason to widen this tranche. Until those gates are closed, the correct runtime behavior is no IW-051 content admission.
