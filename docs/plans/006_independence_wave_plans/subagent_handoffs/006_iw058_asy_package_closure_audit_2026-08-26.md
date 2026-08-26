# IW-058 ASY package closure audit — 2026-08-26

## Verdict

IW-058 (`ASY`, Assyria) remains **blocked and fail-closed**. The package has a broad structural implementation, but its current grounded portrait and institutional-role evidence does not satisfy the accepted Event 006 content gate. No central admission, gameplay, asset, or generated-file change was made in this audit.

The smallest safe next patch is an evidence-only portrait/role closure pass for the Civic National Assembly and Levies Guardianship consumers, followed by a fresh whole-package audit. Only after that audit passes may the parent add `iw_058` to the central content-attestation list and the Join candidate list; neither list was widened here.

## Authority and current source layout

The accepted Event 006 sources are `docs/specs/006_independence_wave_specs/`, especially the country-package, sensitive-identity, signature-package, and AI/asset acceptance material. The current source-of-truth map is `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`. The latest package snapshot still identifies IW-058 as one of the eight adapter-only fail-closed rows.

The current receivers are the merged files, not the older package filenames: `events/006_independence_wave_support_events.txt`, `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`, `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`, `common/national_focus/006_independence_wave_iw043_iw058_focus.txt`, `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`, `common/characters/006_independence_wave_characters_registry.txt`, `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, and `localisation/english/006_independence_wave_iw043_iw058_l_english.yml`.

Historical v80/v41 handoffs contain stale `processed_png/` paths and an older Barsoum hash. The current Barsoum runtime promotion is the v94 record in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw058_asy_barsoum_runtime_portrait_promotion_v94_2026_08_02.md`; that record is the runtime authority used below.

## Country package coverage checklist

| Surface | Current evidence | Closure state |
| --- | --- | --- |
| Vanilla carrier/tag | Vanilla `common/country_tags/00_countries.txt` maps `ASY` to `countries/Assyria.txt`; vanilla history remains the carrier. | Pass; no duplicate tag added. |
| Event 006 identity/origin | `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:45-56` requires original tag `ASY`, active Event 006 country, package `iw_058`, Event 006 origin, package flag, and rejects Soviet-collapse origins. | Pass structurally. |
| Dormant candidate/host proof | `...iw043_iw058_package_triggers.txt:75-78` proves exact dormant ASY identity; `...package_triggers.txt:974-993` requires a distinct former host, state 676, capital/ownership/control and origin preparation. | Pass structurally; not engine-rendered in this audit. |
| Anchor/state | `...package_triggers.txt:929-932` defines the state 676 Mosul/Nineveh anchor and the ASY setup gate. Vanilla state 676 remains owned by IRQ in the carrier history and has ASY as a core. | Pass as a guarded carrier reuse; no map write. |
| Starting force | `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1383-1500` applies the package force mapping, generation receipt, and formation template only after the force/roster gates. | Pass structurally. |
| Politics/institution | `...package_effects.txt:228-596` applies route politics and the four institutional role surfaces; all roles are country-scoped and cleanup is generation-aware. | Pass structurally; portraits still block admission. |
| Cleanup | `...package_effects.txt:1843-2160` removes ASY decisions, formable ledgers, force provenance, ideas, leader roles, cosmetics, flags, variables, and generic focus state. | Pass structurally. |
| Event chain | `events/006_independence_wave_support_events.txt:2219` contains `chaosx.nr006.5801` through the merged IW-058 chain; triggers use `is_independence_wave_iw058_country`. | Pass source-only; event MCP timed out. |
| Focus tree | `common/national_focus/006_independence_wave.txt:37,64-70` loads `independence_wave_focus_tree` and the ASY package branch contains 25 focus IDs in `...iw043_iw058_focus.txt:395-781`. | Pass source/localisation parity; focus MCP timed out. |
| Decisions/missions | `common/decisions/006_independence_wave_iw043_iw058_decisions.txt` contains 20 top-level ASY category/decision IDs and 14 ASY custom-cost surfaces. | Pass source/localisation parity. |
| Ideas | `common/ideas/006_independence_wave_ideas_registry.txt:2369-2470` contains 10 ASY ideas with `is_independence_wave_iw058_country` guards. | Pass source-only. |
| Formable | FORM-18 readiness in `...iw043_iw058_package_triggers.txt:1343-1364` requires the ASY route, state 676 anchor, guarantees, settlement flags, member arrays, and the package-local adapter receipt. | Pass as a guarded dormant extension; no admission. |
| AI | Nine ASY strategy blocks are in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:1097-1237`, each gated by exact ASY package/setup/route state and `abort_when_not_enabled = yes`. | Structural pass; probability audit unavailable. |

## Portrait, character, party, flag, and identity findings

The current character registry (`common/characters/006_independence_wave_characters_registry.txt:322-360`) has exactly four male, `civilian.large` institutional consumers and no advisors:

| Consumer | Character/GFX | Evidence state |
| --- | --- | --- |
| Provisional National Council | `ASY_gallo_shabo`; `GFX_portrait_ASY_independence_wave_provisional_national_council` | Existing project-owned Gallo Shabo consumer is retained for the provisional role. It is not evidence for reusing Gallo as the Civic Assembly leader. |
| Concordat Council | `ASY_independence_wave_concordat_council`; `GFX_portrait_ASY_independence_wave_concordat_council` | Barsoum alternate portrait was parent-promoted in v94 to `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_concordat_council.dds`, 156x210 BGRA DDS, SHA-256 `5c034700247de09480eedd294ca192045c18dd8b9582fe236dda776e7d67ad06`. This is the only current ASY portrait with a current source/audit/promotion record. |
| Civic National Assembly | `ASY_independence_wave_civic_national_assembly`; `GFX_portrait_ASY_independence_wave_civic_national_assembly` | Werda remains blocked by the low-resolution/later-life/1936 continuity gate. No source-cleared replacement or explicit parent-approved Gallo reuse exists. |
| Levies Guardianship | `ASY_independence_wave_levies_guardianship`; `GFX_portrait_ASY_independence_wave_levies_guardianship` | Haydo remains rights/date `needs_user_review`; Malik remains exact active-role/date unresolved. No source-cleared promotion exists. |

All four sprite definitions are wired in `interface/006_independence_wave_portraits_registry.gfx:183-196`, and all four DDS paths exist physically under `gfx/leaders/006_independence_wave/`. Physical presence is not sufficient: the generated institutional portrait package was superseded by the accepted sensitive-identity rules, and Civic/Levies remain unverified. No opposite-gender pairing was found; no advisor/small portrait assets are used.

The four ASY route cosmetics and FORM-18 flag assets exist at all three flag sizes (`gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`) for `ASY_independence_wave_national_councilX`, `...church_compactX`, `...civic_federationX`, `...security_guardianshipX`, plus `MESOPOTAMIAN_FEDERATIONX`. `common/countries/006_independence_wave_formable_cosmetics.txt:73-90` owns the cosmetic definitions. The vanilla ASY base flag/history was not changed. `python -B .tools/audit_event6_flags.py --strict` reports 102 registered Event 006 tags, 102 complete families, and zero incomplete families.

Party and cosmetic localisation is present in `localisation/english/006_independence_wave_iw043_iw058_l_english.yml:93-108,185-259`. The package uses institutional names for council/assembly/guardianship roles rather than personal random-name pools, consistent with the accepted identity rule.

## Map, state, military, technology, industry, supply, and production

The vanilla `ASY - Assyria.txt` history uses capital/state 676, the carrier's vanilla research and equipment setup, and the existing ASY core relationship. Vanilla `676-Mosul.txt` remains an IRQ-owned state with ASY core, VPs 10106/3916/6826, oil, provinces, and no package map edits. The package's state-control/anchor guard prevents setup until the correct former-host transfer is real.

The dynamic force/formation mapping is present and guarded, but I did not claim quantitative balance or live military playability because no game launch/live test is allowed and the required MCP probability route was unavailable. The installed MCP package exposes no Technology Tree Viewer; technology-tree acceptance is therefore an unresolved limitation. The attempted technology scan also ended with transport closed.

## Central adapter, attestation, dispatch, capacity, and Join surfaces

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63` includes the `iw_058` runtime adapter. The content-attestation OR list at `:159-201` intentionally excludes `iw_058`; therefore `is_independence_wave_runtime_package_preflight_ready` at `:207-213` rejects ASY before release because it requires both adapter and content attestation. The scenario dispatch branch retains the ASY exact-tag branch at `:522-524`, but that branch cannot bypass content attestation.

The shared Join probe in `common/scripted_effects/006_independence_wave_join_effects.txt:213-248` enumerates only attested candidates and intentionally omits both `iw_043` and `iw_058`. Its host-capacity/zero-host safeguards remain shared and unchanged. `common/scripted_triggers/006_independence_wave_package_triggers.txt:261-286` keeps selected-plan capacity and metadata arrays aligned; no ASY-specific capacity exception is present or needed while the package is closed.

The package-local setup effect currently writes ASY setup, FORM-18 adapter, and achievement-writer receipts only after its own guarded setup path (`...package_effects.txt:1383-1500`). Those receipts do not replace the central content attestation and are not evidence to widen the central gate. No central adapter, attestation, dispatch, capacity, or Join file was changed.

## AI and playability

The nine ASY AI profiles cover foundation, reserve recovery, tracked crisis, Church Compact, Civic Assembly, Guardianship, civilian normalization, federation, and sovereign autonomy. They are route/flag-gated and structurally coherent. A mandatory `chaosx_ai_probability_auditor` project worker is not available in the active tool set, and the direct `hoi4.probability_inspect` attempt ended with `Transport closed`; consequently no scenario-specific probability compare or AI balance claim is made. No AI weight was patched.

## Validation evidence

The following task-specific static checks completed successfully on 2026-08-26:

- `python -B .tools/audit_event6_allocator.py` — 149 publishers, 126 automatic/high-chaos selectable, 40 runtime adapters, 32 content-attested packages, and the eight adapter-only fail-closed IDs include `IW-058`.
- `python -B .tools/audit_event6_country_api.py` — 242 broad unique tags, 191 resolved, zero missing, zero duplicates.
- `python -B .tools/audit_event6_flags.py --strict` — 102/102 complete Event 006 flag families.
- `python -B .tools/audit_event6_form16.py` — pass.
- `python -B .tools/audit_event6_gui_matrix.py` — pass; semantic matrix only, not a live rendering claim.
- `python -B .tools/audit_event6_scenario_matrix.py` — pass; SCN-008 cells and eight edge cases.
- Source parity checks — all 25 ASY focus IDs have title/description/tooltip keys; all 20 ASY decision/category IDs have title/description keys; all 14 ASY custom-cost surfaces have base/blocked/tooltip keys.

Required read-only MCP routes were attempted but could not provide engine evidence: `hoi4.event_inspect` and `hoi4.focus_inspect`/`focus_render` timed out at the installed limit; `hoi4.map_inspect` timed out; `hoi4.map_render`, `hoi4.probability_inspect`, and `hoi4.tech_inspect` returned `Transport closed`. No MCP artifact is claimed from those calls. No live Hearts of Iron IV run was performed.

## Files changed and before/after

Only this dated handoff was added:

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw058_asy_package_closure_audit_2026-08-26.md`

No tags, state IDs, leaders, parties, focus IDs, localisation keys, formable IDs, gameplay effects, triggers, AI weights, flags, portraits, or central registries changed. Before and after behavior is identical: ASY has a package-local adapter and broad guarded source surfaces, but central runtime admission and Join selection remain fail-closed.

## Remaining blockers and smallest next implementable patch

1. Route Civic Assembly portrait work through `chaosx_portrait_creator` to clear Werda's resolution/1936 role gate or obtain an explicitly parent-approved, role-correct alternative. Do not silently reuse Gallo.
2. Route Levies Guardianship portrait work through `chaosx_portrait_creator` to resolve Haydo rights/date review or obtain a cleared male active-role subject; separately resolve Malik's exact 1936 role/date. Do not promote the existing physical DDS by presence alone.
3. Re-run the country, asset, focus, decision, event, map, AI-probability, and formable audits after those evidence packages are accepted. Only then add `iw_058` to central content attestation and the Join probe in a parent-owned change; preserve the current adapter and scenario branches.
4. Keep historical v80/v41 notes as historical evidence, but use the v94 Barsoum handoff and current merged source files as runtime authority when the next audit reconciles paths/hashes.

No generic/fallback portrait, invented identity, unapproved flag, RunPod operation, broad identity redesign, or central-gate widening was used.
