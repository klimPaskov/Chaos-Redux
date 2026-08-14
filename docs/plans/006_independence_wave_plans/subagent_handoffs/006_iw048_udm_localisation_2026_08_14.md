# IW-048 UDM localisation audit and patch handoff

Date: 2026-08-14

## Scope and disposition

Audited the package-local IW-048 Udmurtia category, founding mission, ten projects, seven ideas, setup and cleanup party-name calls, UDM effect tooltips, and shared-focus helper calls. The owned keys were present and unique, but several player-facing descriptions omitted source-backed requirements, dynamic values, costs, outcomes, or route tradeoffs. I patched only `localisation/english/006_independence_wave_udm_l_english.yml`.

The flat vanilla portrait archive and vanilla `UDM_boris` portrait consumer were not touched. IW-048 remains absent from central admission, attestation, preflight, dispatcher, deterministic Join, and workbook surfaces. This localisation patch does not widen that fail-closed boundary.

## Audit results

- Missing owned keys: none. The shared emergency project selector `independence_wave_cost_security_standard` resolves in `localisation/english/006_independence_wave_decisions_l_english.yml`.
- Duplicate owned keys: none. The 66 UDM keys occur once across the English localisation search.
- Scripted localisation issues: none. The package uses direct contextual variables and script constants, not a package-local `defined_text` block.
- Dynamic text opportunities: implemented for current Workshop Control, current Forest-Rail Readiness, maximum values, stabilization threshold, mission duration, and all package-specific ledger changes.
- Cross-surface mismatches: repaired. The founding mission now states its route-government, threshold, state-control, capital-control, and deadline requirements. Project tooltips now match package effect deltas and shared reward directions. The emergency route now discloses its Workshop Control loss in exchange for a decisive Forest-Rail Readiness gain.
- File encoding concerns: none. The file remains UTF-8 with BOM and retains the repository's two-space indentation under `l_english:`.
- Sourced quotations: none occur on the inspected UDM surfaces.

## Changed file and keys

Changed file:

- `localisation/english/006_independence_wave_udm_l_english.yml`

Changed all 66 owned keys in seven bounded groups:

- Category: `independence_wave_udm_industrial_forest_category`, `independence_wave_udm_industrial_forest_category_desc`.
- Founding mission: `independence_wave_udm_hold_workshop_congress`, `independence_wave_udm_hold_workshop_congress_desc`.
- Ten project title/description pairs: `independence_wave_udm_secure_workshop_depots`, `independence_wave_udm_integrate_industrial_guards`, `independence_wave_udm_register_udmurt_communities`, `independence_wave_udm_settle_former_host_ledgers`, `independence_wave_udm_ratify_constitutional_autonomy`, `independence_wave_udm_adopt_forest_land_compact`, `independence_wave_udm_convene_worker_councils`, `independence_wave_udm_establish_industrial_emergency_command`, `independence_wave_udm_codify_durable_sovereignty`, and `independence_wave_udm_open_volga_ural_corridor`, plus each `_desc` key.
- Cost triplets: `independence_wave_udm_cost_administration_light`, `independence_wave_udm_cost_administration_standard`, and `independence_wave_udm_cost_strategic`, plus each `_blocked` and `_tooltip` key.
- Effect tooltips: `independence_wave_udm_project_failure_effect_tt`, `independence_wave_udm_depots_effect_tt`, `independence_wave_udm_guards_effect_tt`, `independence_wave_udm_communities_effect_tt`, `independence_wave_udm_host_ledgers_effect_tt`, `independence_wave_udm_constitutional_effect_tt`, `independence_wave_udm_cultural_effect_tt`, `independence_wave_udm_worker_effect_tt`, `independence_wave_udm_emergency_effect_tt`, `independence_wave_udm_sovereignty_effect_tt`, and `independence_wave_udm_corridor_effect_tt`.
- Seven idea title/description pairs: `udm_fragmented_workshop_mandate`, `udm_industrial_forest_compact`, `udm_workshop_charter`, `udm_worker_forest_councils`, `udm_cultural_register`, `udm_cultural_land_compact`, and `udm_industrial_emergency_command`, plus each `_desc` key.
- Route parties: `UDM_independence_wave_constitutional_party`, `UDM_independence_wave_socialist_party`, `UDM_independence_wave_cultural_party`, and `UDM_independence_wave_emergency_party`, plus each `_long` key.

## Display before and after

- Before: the category supplied only atmospheric prose. After: it shows both current package ledgers, their maximum, the stable threshold, the route-government condition, and the Izhevsk security condition.
- Before: the founding mission said only to keep the cabinet together. After: it states the dynamic deadline, both required thresholds, the government requirement, state ownership/control, and capital control.
- Before: blocked cost text used long `Unavailable` sentences without icons. After: all three package cost states use compact icon-first red values, while the normal and tooltip variants preserve their dynamic constants and factory burden.
- Before: several completion tooltips said only that a system improved. After: all ledger changes use source-backed dynamic constants, shared value directions are stated, and concrete institutions are named.
- Before: Industrial Emergency Command concealed its civilian-control cost. After: it explicitly shows Forest-Rail Readiness rising by the decisive amount while Workshop Control falls by the minor amount.
- Before: short and long route party names were identical. After: short names remain compact and long names identify the governing congress, compact, union, or directorate.

## Prose-quality repair summary

- Vagueness: replaced generic references to `the line`, `the network`, `the new government`, and `both ledgers` with Izhevsk, the forest railway, named institutions, exact values, and concrete public actions.
- Bloat: reduced blocked-cost explanations to icon-first values and kept decision descriptions to one concrete action.
- Obvious explanation: removed `Unavailable` narration and labels that merely repeated the existence of a cost.
- Repetition: differentiated route parties and idea descriptions instead of repeating the same short and long names or generic compact language.
- Overcomplication: split dense mechanical outcomes into short sentences while preserving every relevant consequence.
- Style-rule repair: preserved active subjects, avoided em dashes and sentence semicolons, and removed administrative filler without flattening Udmurt industrial, forest, rail, and cultural identity.

## Dynamic localisation and token preservation

Added or expanded direct dynamic references for `independence_wave_udm_workshop_control`, `independence_wave_udm_forest_rail_readiness`, UDM pressure constants, UDM duration, shared decision-cost constants, and the package civilian-factory constant. `$STATE_399$`, all formatting codes, icons, existing dynamic tokens, and source identifier spellings were preserved. No scripted-localisation selector was added or changed.

No sourced or attributed quotation was altered because none was present.

## Meaningful validation

- Cross-checked all 66 owned keys against `common/decisions/006_independence_wave_udm_decisions.txt`, `common/ideas/006_independence_wave_udm_ideas.txt`, setup and cleanup calls in `common/scripted_effects/006_independence_wave_udm_package_effects.txt`, and UDM calls in `common/national_focus/006_independence_wave_focus.txt`.
- Confirmed 66 keys and 66 unique definitions in the owned file, no duplicate UDM key matches elsewhere in English localisation, resolution of the one shared security-cost key, and retention of UTF-8 BOM.
- Read-only `mission_ai_will_do` inspection covered the exact eleven-ID UDM decision pool and returned `PROBABILITY_SOURCE_INSPECTED`, source revision `d409c923bc96ab2446b627d20633d9be634c5dcbe89ac76e586e27d7122f338a`, source hash `cae802712e775a81971ae7ae90970e7328b31674dcce862bdce65b3bf8da2f98`, a complete eleven-candidate pool, fifteen required inputs, and no tool diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ff72d0a06ad63ca0f9e8a2ba32c22584699770dba604deb125a300543e218460/df09125d6767af23c55f48f7b7a172cbeee233d1b1852148f16444c0f84e3650/probability-inspect-cae802712e77.json`.

## Skipped validation and unresolved limitations

The installed HOI4 MCP exposes probability inspection for decisions but no read-only `decision_inspect` or `decision_render` route. The probability artifact proves source discovery and the exact decision pool, but it cannot render decision cards, verify localisation resolution, or measure in-engine text overflow. Source review is not treated as equivalent visual evidence. Live rendering and overflow remain unresolved tooling limitations for parent review.

No technology or doctrine surface belongs to IW-048, and the installed package has no Technology Tree Viewer. No focus node was changed by this localisation-only patch, so the prior focus-render evidence remains the applicable helper-call evidence.

## Remaining wording decisions and follow-up

No unresolved UDM wording decision remains inside the assigned localisation scope. The parent should retain the documented fail-closed admission boundary and review the missing decision-render capability when an MCP route becomes available. No gameplay, portrait, asset, central list, Join, attestation, workbook, staging, or commit action was performed.
