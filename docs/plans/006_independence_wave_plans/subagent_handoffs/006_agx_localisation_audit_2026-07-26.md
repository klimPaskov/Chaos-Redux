# Event 006 AGX focus overlay localisation audit

Date: 2026-07-26  
Scope: the post-AGX overlay localisation in `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`, the eight Frisia focus nodes in `common/national_focus/006_independence_wave_focus.txt`, their reward effects and triggers, and the North Sea Coastal Conference decision gate and cost surface.
Source commits reviewed: `8c15baa17`, `c9337fd94`, `79663734e`.

## Bounded result

Focus-title, focus-description, and focus-tooltip coverage is PASS. The eight AGX focuses have all 24 expected localisation keys, and the text matches the implemented reward branches. BOM, duplicate-key, punctuation, scripted-localisation, and GUI-reference checks are PASS. The conference authorization gate is PASS. The bounded audit is not fully clean because the conference decision reserves three civilian factories while its custom cost trigger and all strategic-cost strings advertise and check two.

This is a localisation and cross-surface audit only. No gameplay or localisation source file was changed by this audit.

## Missing key list

None in the new AGX focus surface. The following eight focus IDs each resolve a title, `_desc`, and `_tt` key:

| Focus ID | Localisation keys |
| --- | --- |
| `independence_wave_agx_chart_waterline_authority_focus` | title, `_desc`, `_tt` |
| `independence_wave_agx_bind_dikes_pumps_harbors_focus` | title, `_desc`, `_tt` |
| `independence_wave_agx_integrate_coastal_guard_focus` | title, `_desc`, `_tt` |
| `independence_wave_agx_codify_water_board_government_focus` | title, `_desc`, `_tt` |
| `independence_wave_agx_settle_water_board_succession_focus` | title, `_desc`, `_tt` |
| `independence_wave_agx_open_north_sea_network_office_focus` | title, `_desc`, `_tt` |
| `independence_wave_agx_mandate_north_sea_coastal_conference_focus` | title, `_desc`, `_tt` |
| `independence_wave_agx_prepare_low_countries_dossier_focus` | title, `_desc`, `_tt` |

The existing Frisia decision, category, and effect-summary keys in the same YAML were also present and consistently namespaced.

## Duplicate key list

None in `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml` (178 parsed keys, no duplicate key names). No `:0` keys or leading whitespace before localisation keys were found.

## Scripted localisation issue list

None introduced by the AGX overlay. The focus rewards use `custom_effect_tooltip` with static, constant-backed values rather than scripted-localisation calls. No new `$...$`, `[?...]`, or scripted-localisation key is referenced by the eight focus nodes. The existing Waterline category text correctly uses integer formatting for its two runtime variables.

## Dynamic text opportunities

- The bind focus says `The anchor state gains one Infrastructure.` Its effect guards the building action with `has_variable = independence_wave_anchor_state`, but the IW-007 prepared-package trigger requires and validates that anchor state (`common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:230-237`). The unconditional wording is therefore safe for the validated package; no wording patch is recommended.
- The mandate focus says `the conference still requires its full strategic cost and duration.` This is useful gate text, but the decision's cost surface must first agree on the factory tier before a dedicated dynamic major-cost string can be recommended.
- The route-specific codify tooltip intentionally enumerates all three government branches instead of hiding a branch-specific result behind dynamic localisation. The branch values are fixed constants and the current text is clearer than a generic placeholder.

## Numeric tooltip alignment

The following comparisons are against `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt` and the shared reward bundles in `common/scripted_effects/006_independence_wave_focus_effects.txt`.

| Focus | Audit result |
| --- | --- |
| Chart the Frisian Waterline Authority | PASS: Waterline Integrity +10, Coastal Security +10, Legitimacy/Capacity/Security +5, Instability -5. |
| Bind Dikes, Pumps, and Harbors | PASS: Waterline Integrity +15, Coastal Security +10, anchor-state Infrastructure +1, Legitimacy +5, Capacity +10, Security +5, Instability -5. The infrastructure action is backed by the IW-007 anchor invariant noted above. |
| Integrate the Coastal Guard | PASS: Waterline Integrity +10, Coastal Security +15, Legitimacy/Capacity +5, Security +10, Instability -5, Army Experience +15, Command Power +15. |
| Codify the Water Board Government | PASS: Constitutional +10/+10 waterline/coastal and -5% War Support; Popular Council +15/+15 and -5% War Support; Patron-Client +15/+15 and -5% Stability. The administrative, security, or diplomatic country-value bundle and -5 Instability are described at route-family level and match the helpers. |
| Settle the Water Board Succession | PASS: Waterline Integrity and Coastal Security +10. A living former host takes the records-settled branch, -5% War Support, then Legitimacy +10, Recognition/Capacity +5, Instability -10. A vanished host takes the administrative branch, Legitimacy +5, Capacity +10, Security +5, Instability -5. The 79663734e correction matches both branches. |
| Open the North Sea Network Office | PASS: Waterline Integrity and Coastal Security +10, Network Standing +10, Legitimacy/Capacity +5, Recognition +10, Instability -5, and each listed league value +5 while the league phase is active. |
| Mandate the North Sea Coastal Conference | PASS: sets the authorization flag, then Legitimacy/Capacity +5, Recognition +10, Instability -5. It does not claim a waterline/coastal delta that the effect does not apply, and it explicitly preserves the project cost and duration. |
| Prepare the Low Countries Dossier | PASS: Waterline Integrity, Coastal Security, and Network Standing +10; Legitimacy +10; Recognition/Capacity/Security +5; Instability +5; each listed league value +5 while active; formable discovery opens without bypassing consent or ratification. The 79663734e correction matches the effect bundle. |

## Cross-surface mismatch notes

1. **FAIL, decision cost display and gate:** `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:596` reserves `constant:independence_wave_decision_cost.civilian_factory_major`, which is 3 factories. The same decision's `custom_cost_text` and `custom_cost_trigger` use `independence_wave_cost_strategic` and `can_pay_independence_wave_strategic_cost`, both of which advertise and check `civilian_factory_standard`, which is 2 (`common/scripted_triggers/006_independence_wave_decision_triggers.txt:264-269`, `localisation/english/006_independence_wave_decisions_l_english.yml:33,76-77`, `common/script_constants/006_independence_wave_decision_constants.txt:139-141`). The UI can therefore report two spare civilian factories while the decision reserves three. This predates the AGX focus text but is inside the requested custom-cost alignment surface.
2. **PASS, conference authorization gate:** the mandate focus is available from `has_independence_wave_agx_north_sea_conference_foundation`, its reward sets `independence_wave_agx_north_sea_conference_authorized`, and the decision visibility block requires that exact flag in addition to the existing stable-waterline, recognition, network-member, candidate, and route-lock checks (`common/national_focus/006_independence_wave_focus.txt:2630-2638`, `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:667-675`, `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:579-589`). The gate is therefore accurately represented by the focus tooltip and decision description.
3. **PASS, GUI references:** no new scripted GUI or interface binding was introduced. The AGX category remains a regular decision category (`independence_wave_agx_waterline_category`), so there is no missing GUI-localisation surface.
4. **PASS, route wording:** Frisia, Water Board, North Sea, and Low Countries Federation names are consistent across the focus text, decision title/description, category title/description, and effect-summary keys. No hidden route secret is exposed by the new descriptions.

## File encoding concerns

`localisation/english/006_independence_wave_wallonia_frisia_l_english.yml` begins with UTF-8 BOM bytes `239,187,191`. The changed strings contain no em dash, semicolon, raw `§`, or raw `£` formatting characters. No encoding concern was found in the scoped localisation file. Markdown handoff encoding is not an engine localisation surface.

## Recommended fixes

- **Required before calling the Event 006 AGX decision surface localisation-clean:** choose one intended factory tier for the North Sea Coastal Conference. If the intended reservation is the current major tier of 3, add a dedicated major strategic cost trigger/localisation pair (including blocked text) and use it for this decision. If the intended tier is standard, change the decision modifier to `civilian_factory_standard`. Keep the focus mandate wording in sync with the chosen cost surface.
- No focus-key, punctuation, duplicate-key, scripted-localisation, GUI, or numeric reward correction is recommended from this audit.

## Validation evidence

- PowerShell parsed the scoped YAML and found 178 keys, zero duplicates, zero `:0` keys, zero leading-key spaces, and the UTF-8 BOM.
- A source-to-localisation check found all 24 title/description/tooltip keys for the eight AGX focus IDs.
- Targeted source comparison covered the focus block, the AGX package effects and triggers, shared focus reward bundles, the conference decision, strategic-cost trigger/localisation, and decision constants.
- The read-only HOI4 focus inspect returned 184 resolved titles for `independence_wave_focus_tree` and recorded artifact URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e63589060aa85ac74913e53b7bd0daf0063c04775c551292f57be2625cd000c/3b31c83204d20eb288b2db3aa04e0e9d58f52029934ad992eeb732fbf1cd8c51/focus-inspect.6fc9b4cccfc792df.json`. The tool reported 14 pre-existing/global layout diagnostics; those are outside this localisation audit and do not identify an AGX key failure.

## Required handoff fields

- Changed files: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_agx_localisation_audit_2026-07-26.md` only.
- Changed keys: none. This was an audit-only handoff; no source localisation or gameplay patch was made.
- Dynamic localisation added or fixed: none.
- Behavior/display before and after: no runtime behavior changed. The audit documents the current display accurately for all eight focuses and identifies the conference decision's two-versus-three-factory display mismatch.
- Skipped meaningful validation and why: no in-game launch or live-save validation was run because the repository instructions reserve that validation for the user. No scripted GUI render was run because the AGX overlay adds no scripted GUI surface. The focus inspect was read-only and its global layout diagnostics were not treated as localisation failures.
- Unresolved wording decisions: the intended civilian-factory tier for the North Sea Coastal Conference remains an owner decision. No other wording uncertainty was found.
- Plan handoff path: this file.
