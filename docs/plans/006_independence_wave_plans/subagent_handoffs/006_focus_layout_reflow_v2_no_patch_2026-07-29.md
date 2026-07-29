# Event 006 focus layout reflow v2 — no-patch handoff

## Scope and decision

This pass audited and trialed coordinate-only layout changes in `common/national_focus/006_independence_wave_focus.txt`.

No gameplay, focus identity, prerequisite, mutual-exclusion, availability, reward, AI, icon, or localisation change was authorized or retained.

The source was returned to the approved `c416825267135f93f370aa1e8aaf8f785178eeb4` baseline because every tested coordinate candidate either left the authoritative blocker count at 14 or regressed another layout metric.

The only file added by this handoff is this Markdown report.

## Source and semantic-equality proof

The current focus source blob is `e1d8599ef165b376bd9c45b0346743171be7f225`.

The baseline commit blob for the same path is `e1d8599ef165b376bd9c45b0346743171be7f225`.

`git diff --quiet c416825267135f93f370aa1e8aaf8f785178eeb4 -- common/national_focus/006_independence_wave_focus.txt` returned clean.

The source still contains 184 focus blocks and 368 coordinate assignments, so no focus ID or non-coordinate field was altered.

No focus IDs were changed, and no gameplay semantics were changed.

## Fresh authoritative inspect

The independent post-revert inspect used workspace `mod_chaos_redux_ea3b2d67c2c0` and revision `e5eac36ec5f14fd8f1ee7bfb79f6b59f84cfba91215d032f640bc102379cd333`.

The tree is `independence_wave_focus_tree` with layout hash `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf`.

| Metric | Baseline and post-revert value |
| --- | ---: |
| Focus nodes | 184 |
| Connectors | 223 |
| Connector crossings | 45 |
| Node intersections | 7 |
| Long connectors | 28 |
| Total horizontal span | 1228 |
| Maximum horizontal span | 80 |
| Total vertical span | 242 |
| Total Manhattan span | 1470 |
| Same-row pairs below required spacing | 5 |
| Authoritative blocking diagnostics | 14 |

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b47fa6364a223686faae4c084e92edff52a4a263679394c8b554026a20411737/be7dcf2393ddb89be8ab8ef43b513a1688640d1ecb5fee1899a6a7e79f5dafee/focus-inspect.e5eac36ec5f14fd8.json`.

## Fresh authoritative render

The deterministic render returned layout hash `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf`, width 17904, height 2440, and the same 14 blocking diagnostics.

| Artifact | SHA-256 |
| --- | --- |
| HTML | `00d8de5feb5a0fa9b1615efcedd6e29e8d157927b31bf3ee2e14cb87d8ea6853` |
| SVG | `db058a79681af4beadd7012b103961104222162d8df430e7e294a1c47cbc39dd` |
| JSON | `b208934082ce3e3579bac351a6a978e29f6261ceef4dbb577131c71414f9cb8f` |
| Source map | `b47d534d2eaa1cccb64f425de67ba07b8ad1ea684a59ff2d43268581ccdaee93` |
| Plan | `1c04fc443a80e4ff1138b9abe96d25d061d4c48076ee70cea93be95d0ef5298a` |

Render artifacts:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00d8de5feb5a0fa9b1615efcedd6e29e8d157927b31bf3ee2e14cb87d8ea6853/2406b80bf63875ea6a28ffcaa6611836e6b96bd2497f07335a88c4f36b115567/independence_wave_focus_tree.focus.html`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db058a79681af4beadd7012b103961104222162d8df430e7e294a1c47cbc39dd/7e3697b3df5920e4ec1cb9f6828f616e92b0686e609312bb0a46343cb9d3adad/independence_wave_focus_tree.focus.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b208934082ce3e3579bac351a6a978e29f6261ceef4dbb577131c71414f9cb8f/b059e5568e615ed2413691a69876e407b837a05425509715447160963a9bcfac/independence_wave_focus_tree.focus.json`

## Route coverage table

The complete 184-node tree remains present. This table records the route anchors relevant to coordinate diagnostics; it is not a content redesign.

| Route family | Anchor IDs observed in `006_independence_wave_focus.txt` | Coverage | Layout status |
| --- | --- | --- | --- |
| Founding administration | `prepare_capital_administration`, `name_provisional_authority`, `inventory_the_state`, `bind_the_first_oath`, `establish_permanent_ministries`, `restore_regional_communications`, `integrate_provinces_and_councils`, `complete_founding_settlement` | Present | Crossings at the opening convergence remain fixed-endpoint issues. |
| Internal power centres | `map_internal_power_centers`, `favor_first_power_center`, `broker_internal_power_compromise`, `favor_second_power_center` | Present | `complete_founding_settlement -> map_internal_power_centers` remains a 17-column connector. |
| Emergency economy | `establish_emergency_revenue`, `secure_food_and_fuel`, `build_regional_transport_authority`, `establish_customs_service`, `activate_package_economic_program`, `create_independent_treasury` | Present | Economy/founding and economy/network crossings remain. |
| Military integration | `integrate_militia_commands`, `secure_national_depots`, `recall_and_vet_officers`, `form_border_guard`, `adopt_military_archetype_program` | Present | Military/founding crossings remain; the retained professional-defense row was not disturbed. |
| Professional defense choice | `confirm_civilian_control`, `grant_military_autonomy`, `raise_mass_reserve`, `build_professional_core`, `fund_domestic_arsenals`, `accept_foreign_arms`, `adopt_border_defense`, `adopt_reclamation_doctrine`, `standardize_with_league`, `preserve_independent_command`, `found_professional_defense_institution` | Present | Two convergence crossings and two long capstone connectors remain. |
| Foreign recognition | `establish_foreign_office`, `send_first_missions`, `seek_neighbor_recognition`, `declare_entrenched_neutrality`, `balance_first_patrons`, `become_treaty_backed_state`, `focus_build_permanent_foreign_service` | Present | No coordinate patch was safe without coupling to the capstone row. |
| Political routes | `prepare_first_assembly` through `consolidate_constitutional_state`; `organize_popular_congress` through `proclaim_popular_republic`; `prepare_traditional_confirmation` through `crown_traditional_state`; `establish_emergency_command` through `entrench_emergency_state`; `open_guarantor_talks` through `choose_loyal_guarantor_path` or `choose_bargaining_guarantor_path`; `reject_inherited_borders` through `proclaim_radical_republic` | Present | No semantic route or route lock was changed. |
| AJX municipal route | `ajx_appoint_neutral_commission_focus`, `ajx_codify_municipal_neutrality_focus`, `ajx_bind_security_to_commission_focus`, `ajx_entrench_neutral_commission_focus` | Present | Fixed founding-to-AJX endpoints participate in unsatisfied crossings. |
| Former-host settlement | `define_former_host_policy`, `open_separation_talks`, `settle_property_and_debt`, `recognize_frontier_arrangement`, `fortify_frontier_settlement`, `armed_coexistence`, `convene_former_host_association`, `submit_former_host_union`, `document_unsettled_claims`, `prepare_reclamation`, `demand_former_host_recognition`, `inherit_successor_ledger`, `settle_empty_successor_claims` | Present | Crossings with founding and network branches remain fixed-endpoint issues. |
| Regional ambition | `survey_regional_ambition`, `support_local_autonomy`, `call_regional_congress`, `build_postwar_compact`, `open_signature_conference`, `sponsor_further_ruptures`, `coordinate_opening_blocs`, `proclaim_open_bloc`, `rewrite_regional_order` | Present | The survey connector still passes through `activate_package_economic_program`. |
| New-state network | `recognize_fellow_new_states`, `exchange_diplomatic_missions`, `aid_corridor_states`, `offer_arbitration`, `draft_league_charter`, `gather_league_congress`, `convene_league_congress` and five proposal branches | Present | Economy/military branches cross the network entry and officer recall. |
| Formable continuations | `form03_*`, `form05_*`, `afx_*`, `arx_*`, `asx_*`, `bay_*`, `rhi_*` continuation IDs | Present | Continuation layout was intentionally left untouched. |

## Missing or simplified content

No route, focus, prerequisite, mutual exclusion, bypass, reward, decision hook, idea hook, claim, core, war-goal, formable hook, or AI block was removed or simplified by this pass.

The only simplification is the explicit decision to leave the existing fixed-endpoint diagnostics unresolved rather than rewrite route geometry outside the bounded coordinate scope.

## Icon coverage

The source uses 50 unique focus icon IDs across 184 nodes, and every one resolves to a sprite definition in `interface/**/*.gfx`.

| Icon family | Representative IDs | Coverage |
| --- | --- | --- |
| Founding and infrastructure | `GFX_goal_independence_wave_founding_administration`, `GFX_goal_independence_wave_infrastructure_authority` | Defined and referenced. |
| Military and defense | `GFX_goal_independence_wave_army_integration`, `GFX_goal_independence_wave_military_emergency`, `GFX_goal_independence_wave_high_chaos_sovereignty` | Defined and referenced. |
| Political routes | `GFX_goal_independence_wave_constitutional_state`, `GFX_goal_independence_wave_popular_councils`, `GFX_goal_independence_wave_traditional_restoration`, `GFX_goal_independence_wave_patron_client` | Defined and referenced. |
| Diplomacy and settlement | `GFX_goal_independence_wave_recognition_diplomacy`, `GFX_goal_independence_wave_league_congress`, `GFX_goal_independence_wave_former_host_settlement`, `GFX_goal_independence_wave_regional_formable` | Defined and referenced. |
| Distinct continuation families | `GFX_goal_independence_wave_ajx_neutral_commission`, `GFX_goal_independence_wave_form03_*`, `GFX_goal_independence_wave_form05_*`, `GFX_goal_independence_wave_afx_*`, `GFX_goal_independence_wave_arx_*`, `GFX_goal_independence_wave_asx_*`, `GFX_goal_independence_wave_bay_*`, `GFX_goal_independence_wave_rhi_*` | Defined and referenced. |

Several broad route icons are intentionally reused, including `army_integration` and `former_host_settlement`; this is existing art reuse, not a coordinate regression.

## Localisation and reward mismatch list

A cross-file scan found all 184 focus IDs and all 184 `_desc` keys in the Event 006 English localisation set, including split route files such as `localisation/english/006_independence_wave_saar_l_english.yml` and `localisation/english/006_independence_wave_form03_l_english.yml`.

No focus name, description, or reward was changed in this pass, so there is no coordinate-induced localisation or reward mismatch to repair here.

Reward wording and effect variety remain an out-of-scope semantic audit and should be taken from the existing Event 006 focus audit rather than inferred from this geometry-only result.

## AI behaviour gaps

All 184 focus blocks retain an `ai_will_do` block in the current source, so this coordinate pass introduced no missing AI behavior.

Route-aware AI weights, route locks, and balance remain unchanged and were not used as a reason to retain a geometry trial.

## High-priority layout fixes for a future bounded pass

1. Revisit the fixed opening endpoints together: `complete_founding_settlement`, `bind_the_first_oath`, `inventory_the_state`, `establish_emergency_revenue`, `integrate_militia_commands`, and `map_internal_power_centers`.

2. Revisit the economy/network and military/network endpoint groups together: `secure_food_and_fuel -> build_regional_transport_authority`, `secure_national_depots -> recall_and_vet_officers`, and the founding edges to `ajx_appoint_neutral_commission_focus`, `define_former_host_policy`, and `recognize_fellow_new_states`.

3. Revisit the professional-defense convergence as a single row: `focus_build_permanent_foreign_service -> secure_durable_sovereignty` against `preserve_independent_command -> found_professional_defense_institution` and `standardize_with_league -> found_professional_defense_institution`.

4. Keep `found_professional_defense_institution` and its 10 parent choices coupled to any future row move, because the retained prior improvement is the current approved baseline.

5. Treat `complete_founding_settlement -> survey_regional_ambition` and `activate_package_economic_program` as a coupled obstacle; moving only one endpoint produced a through-node diagnostic or a larger crossing count.

## Trial matrix and rollback evidence

| Trial | Crossings | Node intersections | Long connectors | Blocking diagnostics | Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| Approved baseline | 45 | 7 | 28 | 14 | Restored and retained. |
| Economy chain moved to `x = 0` | 40 | 6 | 28 | 14 | Reverted because blockers did not fall and bounds/span widened. |
| Economy `x = 0` plus selected opening/power-centre shifts | 37 | 6 | 28–31 | 14 | Reverted because blockers did not fall and new opening crossings/long spans appeared. |
| Military/professional row shift | 46 | 12 | 23 | 15 | Reverted immediately because blockers and node intersections regressed. |
| `secure_durable_sovereignty` local shift | 45 | 8 | 28 | 14 | Reverted because no authoritative improvement. |
| `survey_regional_ambition` local shift | 58 | 7 | 30 | 14 | Reverted because crossings and long connectors regressed. |
| `activate_package_economic_program` local shift | 48 | 10 | 28 | 18 | Reverted because duplicate/through-node geometry worsened. |

The compact `hoi4.focus_rewrite` cleanup attempt returned `FOCUS_COMPACT_QUALITY_BLOCKED` and did not modify the source.

## Remaining route risks

The authoritative tree still reports 14 blocking diagnostics; the inspect payload lists 19 warning entries, consisting of one avoidable crossing, nine unsatisfied fixed-endpoint crossings, one through-node intersection, and seven long-connector warnings among the listed IDs.

The current geometry is semantically safe because it is byte-equivalent to the approved baseline, but it is not layout-clean.

A future patch should use a coupled coordinate plan and rerun the default inspect mode; custom `nodeSpacing` values must not be treated as authoritative because the default validator requires same-row spacing of 2.

No plan file was written because the safe outcome was a no-patch rollback and the remaining work requires a broader coupled geometry design.
