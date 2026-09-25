# Event 006 regional focus tooltip localisation audit

Date: 2026-09-25. Scope: three named tooltip keys in `localisation/english/006_independence_wave_focus_l_english.yml` and their call sites in `common/national_focus/006_independence_wave_focus.txt`. Read-only source audit. The user authorized the accepted Event 006 scope on 2026-09-25 and explicitly limited this handoff to an audit. No gameplay or localisation file was changed.

## Coverage and effect correspondence

| Key and source location | Conditional call site | Effect and constant correspondence | Finding |
| --- | --- | --- | --- |
| `independence_wave_kar_inventory_focus_tt`, localisation line 79 | `independence_wave_inventory_the_state` reward, focus line 168, guarded by `is_independence_wave_kar_package` | Focus line 190 calls `independence_wave_kar_focus_reconcile_forest_supply_records`; `common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt` lines 113-119 adds `standard_gain` (12) to Forest Supply and `minor_gain` (6) to Civic Mandate. | Exact key and numbers match. |
| `independence_wave_cri_inventory_focus_tt`, localisation line 80 | Same focus reward, line 169, guarded by `is_independence_wave_cri_package` | Focus line 191 calls `independence_wave_cri_focus_register_land_and_return_rolls`; the same scripted-effects file, lines 122-128, adds `minor_gain` (6) to Return Capacity and `standard_gain` (12) to Land Settlement. | Exact key and numbers match. |
| `independence_wave_tra_overlay_address_former_host_tt`, localisation line 423 | `independence_wave_overlay_address_former_host` reward, focus lines 3505-3507, guarded by `is_independence_wave_tra_package` | Focus line 3515 calls `independence_wave_tra_focus_arbitrate_danube_border`; `common/scripted_effects/006_independence_wave_balkan_package_effects.txt` lines 2782-2788 adds `standard_gain` (10) to both Federal Legitimacy and Frontier Cohesion. | Exact key and number match. Adding “each” would make the two separate gains explicit. |

The numeric sources are `common/script_constants/006_independence_wave_constants_registry.txt` lines 5958-5978 and 9114-9134. Each ledger change clamps to 0-100 in its helper. Consequently, “raises ... by” describes the requested increment, not a guaranteed net increment when a ledger is near 100. The parent can decide whether to use “by up to” for strict cap-aware wording. This is a wording precision issue, not a mismatch between displayed constants and script.

## Audit lists

- Missing keys: none among the three assigned keys. Each has one definition and one conditional `custom_effect_tooltip` call site.
- Duplicate keys: none among the three assigned keys in the searched localisation tree.
- Scripted localisation issues: none in these three strings. They contain direct constant substitutions, and the referenced constant categories and entries exist.
- Dynamic text opportunities: the three values already read their script constants dynamically. The Transylvania sentence could say “by [value] each.” Cap-aware “up to [value]” is an optional precision improvement for all three.
- Cross-surface mismatch: none found between these three strings and their conditional effect helpers. No event-catalog wording was reviewed in this bounded assignment, so no spreadsheet-owner key-level wording handoff is needed.
- Encoding and style: the file decodes as strict UTF-8 and begins `EF-BB-BF`, consistent with the parent check. These three definitions use `key: "Text"` without `:0` and retain their `[?constant:...|0]` tokens.
- Prose quality: no definite vagueness, bloat, obvious explanation, repetition, overcomplication, or style-rule violation in the assigned sentences. “Land and return rolls” is compact contextual wording, though readers unfamiliar with “rolls” may need the nearby route context. No quote-bearing text occurs in the assigned keys; no sourced quotation was changed.
- Hidden-route disclosure: these conditional lines name only the public regional ledger gains behind matching package checks. No secret outcome is disclosed in the assigned text.

## Recommended parent action

Keep the three keys as written unless the parent wants strictly cap-aware reward wording. If revised, change only `independence_wave_kar_inventory_focus_tt`, `independence_wave_cri_inventory_focus_tt`, and `independence_wave_tra_overlay_address_former_host_tt` in `localisation/english/006_independence_wave_focus_l_english.yml`; retain every constant token. For the Transylvania key, “raises Federal Legitimacy and Frontier Cohesion by [value] each” is more explicit. The actual source effects and constant values need no correction based on this audit.

## Evidence limits and handoff disposition

The parent reports current-source focus inspect/render at revision `ae4069ebd12391ee20c151df1659b2e064ab93c404d97fe03d12257803f58558`; no artifact URI was supplied to this subagent. My read-only `hoi4.focus_inspect` attempt with an empty request did not return and was cancelled. Targeted `hoi4.focus_inspect` and `hoi4.focus_render` requests for `common/national_focus/006_independence_wave_focus.txt` each timed out after 15 seconds. Thus current MCP tooltip rendering, overflow, and source-map verification are **blocked in this subagent pass**; the source audit is not equivalent to rendered evidence. No artifact URI was produced. The exposed technology inspect/render/compare routes are separate from a standalone Technology Tree Viewer; no standalone viewer appears in the available tool inventory. That is a package-availability observation, not a technology-surface audit.

Read before source review: `AGENTS.md`; the offline wiki core pages and National focus modding page; vanilla `documentation/script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, and `common/script_constants/documentation.md`; a vanilla Finland focus tooltip precedent; and the `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents` skills. No improvement-loop design gap arose from these three strings. No tests, live game, or commit were run, per the user instruction. Only this handoff file was created. Disposition: source audit implemented; MCP visual verification blocked by nonresponsive routes, for parent integration.
