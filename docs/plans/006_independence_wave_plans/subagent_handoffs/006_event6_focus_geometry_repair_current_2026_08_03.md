# Event 006 current focus geometry repair audit

Date: 2026-08-03.

Owner: focus-tree subagent.

Scope: current-head geometry review of `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, against the requested 80-column spacing diagnostics.

Disposition: **AUDIT COMPLETE / NO SAFE SOURCE PATCH**.

The proposed source diff is **none**.

The Event 006 source remains unchanged because the 80-column findings are produced by an explicit `hoi4.focus_inspect` threshold, while the normal HOI4 two-column spacing audit is clean.

## Current MCP evidence

Source SHA-256: `6D9661148539F9AE4CEB232809C2E758B315EABC8A53EA9E48DD5E34A4334DD6`.

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Current inspect revision: `dc5ba8ae14db17d90bc6cac027844fde969361caff7de1af6e6a66abe68a87f2`.

The stable tree layout hash is `014c594a446087d67b6623767e34af4b83a026e744623e5a3bd3cbc4eceef2a` for both spacing configurations.

| Check | Normal audit (`nodeSpacing=2`, `laneSpacing=80`) | Explicit 80-column audit (`nodeSpacing=80`, `laneSpacing=80`) |
| --- | --- | --- |
| Focus count | 184 | 184 |
| Bounds | x=1..121, y=0..19 | x=1..121, y=0..19 |
| Connector count | 192 | 192 |
| Crossing count | 0 | 0 |
| Node-intersection count | 0 | 0 |
| Long-connector count | 0 | 0 |
| Maximum horizontal span | 7 columns | 7 columns |
| Maximum vertical span | 3 rows | 3 rows |
| Required same-row spacing | 2 | 80 |
| Same-row pairs below threshold | 0 | 164 |
| Event 006 layout warnings | 0 | 19 |

Normal-spacing inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39f3a88f85e73e3520088658c243b06bdd0a75fef66dd1d5d77fb50fbf7d8290/0d810062aea0b0efd31ad9a214a58438dce46e29d81c41ce6b411f0fd1cc1159/focus-inspect.dc5ba8ae14db17d9.json`.

Explicit-80 inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/34f606d26864c9b1aa03d1123631131323da758fdbbbc27725a21feaedfa0c1b/4032d04d845ae0342ec784ab39b4be02cfad087062127ee065371223a4f7af66/focus-inspect.dc5ba8ae14db17d9.json`.

The explicit-80 run reports 19 warning-level `FOCUS_LAYOUT_SAME_ROW_SPACING_UNSATISFIED` or `FOCUS_LAYOUT_MUTUAL_EXCLUSION_SPACING_UNSATISFIED` entries.

They cover the fixed or relative opening pairs `independence_wave_name_provisional_authority`/`independence_wave_inventory_the_state`, `independence_wave_inventory_the_state`/`independence_wave_bind_the_first_oath`, `independence_wave_establish_permanent_ministries`/`independence_wave_restore_regional_communications`, `independence_wave_restore_regional_communications`/`independence_wave_integrate_provinces_and_councils`, and `independence_wave_integrate_provinces_and_councils`/`independence_wave_establish_emergency_revenue`.

They also cover the intentional mutual-exclusion cohort `independence_wave_favor_first_power_center`, `independence_wave_broker_internal_power_compromise`, and `independence_wave_favor_second_power_center`, plus the economy, military, diplomacy, and package pairs on rows 2 through 7.

Every explicit-80 layout entry reports `movableFocusIds=[]`; the mutual-exclusion entries additionally preserve both endpoints.

The inspect and render validator still says `14 blocking focus diagnostics`, but those errors are unrelated vanilla continuous-focus icon references in `game:common/continuous_focus/generic.txt`.

The 14 unrelated references are the DEN, ETH, SWI, and generic continuous focuses listed as `FOCUS_ICON_REFERENCE_MISSING`; one separate vanilla localisation warning concerns `continuous_restrict_freedom_desc`.

The sole Event 006 design diagnostic at normal spacing is the intentional `FOCUS_ISOLATED` warning for `independence_wave_preserve_independent_command` at `common/national_focus/006_independence_wave_focus.txt:734-751`.

The successful current render produced the following artifacts.

| Artifact | URI |
| --- | --- |
| HTML | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94ad74513c823201468738487353b1e7461088602ec9f47b0631abc6635a9d26/5d2c4ff26524cd27971ee1069f4cd6895a74f32c90f9d89b7b8cd252774f9a26/independence_wave_focus_tree.focus.html` |
| SVG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3b75a93b31cf1e9dfc01ec7da0eceebdcd170e909272ebc0f24746a084e6409/f8e607c630233b536ec8c5226c3c40ab4581d86841361537983931b7b5787dde/independence_wave_focus_tree.focus.svg` |
| JSON | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ca461ac81d6b56fa4adf3ab065da1aba5fc8e2b3b0838d8b827a24cca855426/92c075c78f28b83d4648c4be2819a47f91e7b5a4230dbe66715ae43e0eb99c7d/independence_wave_focus_tree.focus.json` |
| Source map | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cadd1e58ed0a0c32895099288fd06a4c21f0685724082a1b4c38d5b8c9f2319f/602b19365c7042f1358eb0ff5af9fce98ad7521715c5ac09155c5b5ac2d01bc5/independence_wave_focus_tree.focus.source-map.json` |
| Plan metadata | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68e486a1002af710814092ced63c7fec1dcdd7e447029ed1df4176d8929a35a9/9cafc8bf813d7895743049d1e2a7891309345d15a0a42ceb6e1a4f42d2151d33/independence_wave_focus_tree.focus.plan.json` |

## Route coverage

| Required route | Current source coverage | Status |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement`, `006_independence_wave_focus.txt:100-243` | Present. |
| Internal power and government settlements | `independence_wave_map_internal_power_centers` through `independence_wave_ajx_entrench_neutral_commission_focus`, `006_independence_wave_focus.txt:257-1382` | Present. Constitutional, popular-council, traditional, emergency, patron-client, radical-sovereignty, and AJX neutral-commission openings retain route locks and reciprocal exclusions. |
| Economy, infrastructure, and administration | `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury`, `006_independence_wave_focus.txt:323-443` | Present. |
| Army, security, and military identity | `independence_wave_integrate_militia_commands` through `independence_wave_preserve_independent_command`, `006_independence_wave_focus.txt:449-751` | Present. The professional-defense capstone keeps its five AND-of-OR prerequisite groups and the ten y=8 mutually exclusive choices. |
| Diplomacy, recognition, and patrons | `independence_wave_establish_foreign_office` through `independence_wave_focus_build_permanent_foreign_service`, `006_independence_wave_focus.txt:758-903` | Present. |
| Former-host settlement | `independence_wave_define_former_host_policy` through `independence_wave_settle_empty_claim`, `006_independence_wave_focus.txt:1390-1579` | Present. Living-host routes remain exclusive and the collapsed-host ledger route remains separately gated. |
| Regional ambition and signature extensions | `independence_wave_survey_regional_ambition` through `independence_wave_open_signature_extension`, `006_independence_wave_focus.txt:1582-1654` | Present. |
| Independence network and League | `independence_wave_recognize_fellow_new_states` through `independence_wave_propose_revisionist_charter`, `006_independence_wave_focus.txt:1660-1842` | Present. Focuses own network and charter preparation while decisions own votes and proclamation. |
| Formable preparation and FORM-03 | `independence_wave_focus_discover_regional_identity` through `independence_wave_form03_submit_low_countries_compact`, `006_independence_wave_focus.txt:1849-2040` | Present at source level. Claims, consent, and formation remain in the formable decision/adaptor surfaces. |
| High-chaos sovereignty | `independence_wave_sponsor_further_ruptures` through `independence_wave_rewrite_charter_of_borders`, `006_independence_wave_focus.txt:2047-2103` | Present. |
| Package and signature modules | Main-tree package blocks `006_independence_wave_focus.txt:2111-3320`, plus `006_independence_wave_iw043_iw058_focus.txt`, `006_independence_wave_iw093_iw098_focus.txt`, and `006_independence_wave_pacific_focus.txt` | Present at source level with exact package gates. Admission and identity evidence remain separate. |
| Durable-state capstone | `independence_wave_secure_durable_sovereignty`, `006_independence_wave_focus.txt:3322-3339` | Present. Economy, military, foreign-service, host, and durable-state requirements remain explicit. |
| Additive carrier boundary | `independence_wave_overlay_take_stock_of_independence` and its overlay chain, `006_independence_wave_focus.txt:3348-3474` | Present as an intentional opt-in boundary. |

No focus ID, prerequisite, mutual exclusion, route gate, package owner, AI block, icon reference, or localisation key was changed by this audit.

## Missing or simplified content

- No accepted route family is missing from the current one-tree contract.
- No fallback tree, generic replacement, or new route family was added.
- The requested 80-column spacing policy remains unsatisfied because it is not a safe local source invariant; enforcing it would require a separately scoped whole-tree reflow.
- `independence_wave_preserve_independent_command` remains intentionally isolated because its route gate is represented in `available` and mutual exclusion rather than by restoring a visible connector.
- Source inspection does not prove runtime package admission, formable transactions, save/load persistence, or player focus selection.
- No improvement-loop plan was written because the tree has broad route depth and the open issue is an audit threshold, not a shallow route family.

## Icon coverage

| Check | Evidence | Result |
| --- | --- | --- |
| Unique base icon references | Four `common/national_focus/006_independence_wave*.txt` sources | 121 unique IDs across 318 focus definitions. |
| Base `.gfx` registrations | `interface/006_independence_wave*.gfx` | 121/121 resolve. |
| Shine registrations | Matching `_shine` entries in the same interface files | 121/121 resolve. |
| Current Event 006 render inventory | Fresh `hoi4.focus_render` above | No Event 006 icon diagnostic. |
| Global missing icon diagnostics | Vanilla continuous focuses only | Outside this source scope and not a reason to patch Event 006 icons. |

## Localisation and reward mismatch list

- No Event 006 title, description, or reward-key mismatch was identified in the current source-level audit.
- The accepted bounded scan covers all 318 focus title keys, all 318 `_desc` keys, and all 318 `custom_effect_tooltip` keys across the 45 Event 006 English localisation files.
- The same scan found no duplicate focus ID, title key, description key, or custom-tooltip key, and all scanned Event 006 English files retain UTF-8 BOM encoding.
- No exact normalised completion-reward body repeats across the 318 definitions.
- A complete semantic prose-to-effect review was not repeated in this geometry-only tranche, so claims are limited to key and reward-body coverage.

## AI behavior gaps

| Surface | Current evidence | Gap or risk |
| --- | --- | --- |
| Focus AI blocks | All 318 parsed focus definitions include `ai_will_do`. | Runtime route selection and completion order were not simulated. |
| Shared tuning | `common/script_constants/006_independence_wave_focus_constants.txt:62-78` provides route-weight, avoidance, war-avoidance, and hidden-gate factors. | No tuning change is justified without scenario evidence. |
| Generic profiles | `common/ai_strategy/006_independence_wave_generic.txt:42-143` supplies survival, recovery, and consolidation profiles. | Runtime activation and route starvation remain untested. |
| Route-aware modifiers | Focus sources read government, package, host, patron, network, military, and chaos state. | No probability sweep was run for government, patron, League, formable, high-chaos, package, or CAT opener ordering. |

## High-priority fixes first

1. Keep `common/national_focus/006_independence_wave_focus.txt` unchanged while the normal-spacing metrics remain clean.
2. Treat the 80-column result as an inspect configuration finding, not as permission for a local coordinate edit.
3. If an 80-column policy is genuinely required, open a parent-owned full-tree reflow plan that preserves every focus ID, visible and hidden prerequisite, mutual exclusion, relative anchor, route owner, reward, icon, localisation key, and AI block.
4. Preserve the intentional hidden-gate treatment of `independence_wave_preserve_independent_command` until such a coordinated reflow is reviewed with `independence_wave_standardize_with_league`, the professional-defense capstone, and the diplomacy lane.
5. Keep the 14 unrelated vanilla continuous-focus icon errors outside the Event 006 source patch.

## Changed files and identifiers

Changed files: this handoff only, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_geometry_repair_current_2026_08_03.md`.

Changed focus IDs: none.

Changed localisation keys: none.

Changed icon IDs: none.

Changed prerequisites, mutual exclusions, AI, rewards, package gates, or route ownership: none.

## Validation and limits

Meaningful checks completed were two bounded `hoi4.focus_inspect` runs using `nodeSpacing=2` and `nodeSpacing=80`, one fresh `hoi4.focus_render`, source-hash verification, route and identifier review, and comparison against the parent-owned reflow and current generic-focus audit handoffs.

`hoi4.focus_rewrite` was skipped because no source geometry defect is present under normal spacing and an 80-column rewrite would be a broad reflow outside this bounded task.

Live game launch, save/load, pixel-raster review, runtime package admission, and in-game AI validation were skipped because they are parent/user-owned surfaces and the repository rules reserve live consumer validation to the user.

No package attestation or gameplay fallback was used.

## Remaining route risks

- The MCP validator remains false because of 14 unrelated vanilla continuous-focus icon references and one vanilla localisation warning, even though Event 006 layout metrics are clean under normal spacing.
- The intentional isolated warning for `independence_wave_preserve_independent_command` remains a presentation diagnostic and should not be repaired by deleting or weakening its hidden route gate.
- Static focus evidence does not prove runtime selection order, package admission, formable formation, save/load persistence, or AI completion timing.
- CAT and other non-attested package branches must remain fail-closed until their separate package evidence closes.

Parent handoff: retain the current source and layout hash, use the normal-spacing inspect/render artifacts above for Event 006 geometry review, and queue a full-tree reflow only if the 80-column threshold is an intentional product requirement rather than an audit-tool parameter.
