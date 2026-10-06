# Holy Realm focus post-source audit

Status: Read-only audit of the final parent-reviewed THR_focus source at SHA-256 d584ec8fe5988781fa1b36306a44e01cf3680f89d610d256f4dcf6c343d5f575. The final English localisation is 8f2e790db5dff40e15d1a13f321b9992c851ac68929c7dfb537f715d69a62bba. I made no gameplay, localisation, index, or asset edits and did not stage or commit.

Files written for this task: this handoff, plus the B0, F5, and D584 MCP receipt JSON files in this folder. The parent also placed its source-repair proofs, source snapshots, and copied B0 artifacts here. The exact final-source artifact receipts are in mcp_artifacts_d584ec8fe598.json, SHA-256 35FE8E4A4E06F62C56B278644F37CCCD1030930E4FCC24D353193CF821265DE1.

## Current-source MCP evidence

I verified the live hoi4.focus_inspect, hoi4.focus_render, and hoi4.focus_raster schemas. For each distinct parent-reviewed source snapshot, I made one narrow THR_focus inspect without refresh and, after a successful inspect, one matching render and raster using the same relative path and workspace. The final D584 source is the only snapshot used for the current layout verdict.

The D584 inspect at the original CF8F localisation succeeded at revision fd7fbe71d4b1d97854ca2e2e659a3533665b879878e485a0d4824d7b8d540286. After the parent added the description override, the final inspect at source D584 and localisation 8F2E succeeded at revision a48557994d96ea45cfab21f0fb8d8abaf296e133f4e465addf191a7b78b8d83a. Inspect, render, and raster share layout hash d610c4cbea1b54e468aec0d07f32d6d47e0f13054272dc47fe316261f377b7c5. MCP reports 111 normal focuses, 14 continuous focuses, and 120 connectors. The final inspect reports zero connector crossings, zero long connectors, zero through-node intersections, zero focus layout diagnostics, and zero blockers. All 111 focus IDs are preserved across B0, F5, and D584. The final raster is 8400×2904.

| Snapshot | Crossing count | Through-node count | Long connector count | Linear detour count | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| B0, after initial repair | 0 | 1 | 3 | 5 | source SHA b0f535a59a972d1d0c03dc65fd8111fc4f3340b1b4fcd1e878590ebb9bbb84a4 |
| F5, after clearance and chapter-entry presentation | 0 | 1 | 0 | 1 | source SHA f5e945184d5eeabe265d71295d0277d4dd2919a3a718e0d1dd9417ed4be5731a |
| D584, after final position-only repairs | 0 | 0 | 0 | 0 | source SHA d584ec8fe5988781fa1b36306a44e01cf3680f89d610d256f4dcf6c343d5f575 |

The D584 inspect and render produced with the original CF8F localisation returned an informational inline-inventory truncation (64 of 91 paths for inspect and 64 of 90 for render) and a reference warning for the vanilla continuous focus continuous_restrict_freedom_desc at game:common/continuous_focus/generic.txt:498–525. The parent added the valid English override “Use closer supervision to curb demands for self-government among our subjects.” under that key in the owned THR localisation. The final one-shot inspect at the 8F2E localisation hash no longer reports the warning and has zero focus diagnostics; its only diagnostic is the informational 64-of-91 inline-inventory notice.

The parent explicitly requested no final render/raster repeat for this description-only follow-up because focus geometry, assets, and textbox fields did not change. The saved D584 render/raster receipt therefore binds to the prior CF8F localisation; it remains valid evidence for the unchanged D584 focus geometry and assets, but not a fresh render of the added continuous-focus sentence. The final inspect receipt is in mcp_artifacts_locale_override_inspect.json.

The parent has the full final PNG URI in mcp_artifacts_d584ec8fe598.json. No final crop PNGs were produced in the one authorized raster call. Visual first-glance acceptance remains with the parent’s review of that image.

## Final layout and route repair behavior

The final position-only repair moves THR_first_doctrine_suffering to (20,3), THR_seat_pilgrim_assembly to (28,4), and THR_refuse_final_debate to (8,17). The native D584 result confirms these positions clear the five-column Bodhisattva Accepts the Seal → First Doctrine detour and the Vow Against Annihilation → Refuse Final Debate line through Peace Without Ownership. The final position proof is parent_final_positions_source_repair.json; it states that all non-position source bytes match F5.

The earlier G6 repair preserves all gameplay requirements while making three distant chapter-entry conditions visible in the focus availability text instead of graph connectors: THR_first_doctrine_suffering gates THR_sit_beneath_prayer_flags, THR_bodhisattva_accepts_seal gates THR_send_first_envoys, and THR_mountain_refuge gates THR_complete_himalayan_mandala. The parent proof records a 512-case before/after truth table with equivalent eligibility and all nine named route requirements retained. This is an accepted presentation simplification, not a removed gameplay requirement. Its visible requirement text is separate from the native prerequisite line, consistent with the offline focus reference.

The three source repairs preserve all 111 focus IDs. The parent proofs state that focus effects, costs, rewards, and AI bodies were unchanged by the coordinate/presentation patches. No focus_rewrite call or gameplay edit was made by this auditor.

## Route coverage against the current focus design text

The table compares current source with the focus design text. The nested design document calls 75–95 focuses an approximate target; the parent’s repair acceptance does not imply acceptance of every nested-spec claim.

| Required route | Current source evidence | Coverage |
| --- | --- | --- |
| Opening survival trunk | THR_mountain_refuge, THR_bodhisattva_accepts_seal, and other opening focuses; initial view at (20,0) | Present |
| Teaching mission path | Eight FOCUS_FILTER_HOLY_REALM_TEACHING focuses, including THR_send_first_envoys, THR_translation_houses, THR_teach_under_bombardment, and THR_many_lamps_one_flame | Present |
| Meditation and Dhyana | Eight meditation-filter focuses, including THR_sit_beneath_prayer_flags, THR_first_quiet through THR_fourth_quiet, and THR_buddha_mandate | Present |
| Governance | Six governance-filter focuses with choices THR_council_of_abbots, THR_name_protector_regent, and THR_seat_pilgrim_assembly | Present |
| Industry and sanctuary logistics | Eight industry-filter focuses and three sanctuary-filter focuses, including THR_mountain_granaries, THR_snowline_clinics, and THR_storehouses_for_world | Present with a reward/tooltip gap below |
| Guardian military | THR_guard_high_passes, THR_vow_keeper_regiments, THR_mountain_artillery_mandalas, THR_unbroken_pass, and THR_guardians_outer_passes | Present |
| Sangha Compact diplomacy | Eight compact-filter focuses, including THR_send_first_envoys, THR_pilgrim_refuge_courts, THR_storehouses_for_world, and THR_mandala_of_nations | Present; the compact capstone has no explicit ai_will_do |
| Pilgrimage and liberation expansion | Sixteen annexation/integration-filter focuses, including THR_white_flags_foreign_roads and THR_complete_himalayan_mandala | Present; force is gated above the 600 coercive floor and each Bhutan, Nepal, and Sikkim war-goal target is rechecked in the reward |
| Anti-chaos powers | Fourteen anti-chaos-filter focuses, including THR_powers_are_not_toys, THR_one_becomes_many_focus, THR_path_through_walls, THR_lotus_bridge_focus, and THR_touch_sun_moon_focus | Present |
| Buddhahood and Final Silence | Sixteen Nirvana-filter focuses, including THR_buddha_mandate, THR_the_awakened_one, THR_ministry_of_release, THR_final_silence, and THR_empty_seat | Present; THR_final_silence opens the authorization event after its requirements |
| Hidden Schism | THR_debate_the_pretender_focus, THR_exile_the_echo, THR_break_false_mandala, and THR_absorb_the_shadow | Present; all four require the awakened focus and allow_branch gated by holy_realm_false_buddha_schism_triggered |

The normalized MCP plan has five entry focus IDs but reports branchCount = 0 and no branch-group metadata. The route table therefore derives from the current IDs, focus filters, and source design text rather than an MCP-provided branch partition.

Seven native shortcuts resolve to existing focus IDs and have English labels:

| Localized label | Shortcut key | Target |
| --- | --- | --- |
| Refuge | THR_navigation_refuge | THR_mountain_refuge |
| Meditation | THR_navigation_meditation | THR_sit_beneath_prayer_flags |
| Government | THR_navigation_government | THR_name_protector_regent |
| Foreign Affairs | THR_navigation_foreign_affairs | THR_send_first_envoys |
| High Passes | THR_navigation_high_passes | THR_complete_himalayan_mandala |
| Peace | THR_navigation_peace | THR_lamps_remain_lit |
| Final Silence | THR_navigation_final_silence | THR_doctrine_last_war |

The shortcuts are in common/national_focus/003_holy_realm.txt:64–91 and their labels are in localisation/english/003_the_holy_realm_l_english.yml:1106–1112.

## Simplifications and remaining content gaps

The tree has 111 normal focuses, 16 above the nested design text’s approximate upper target of 95, plus 14 continuous focuses. This count is not proof that the extra nodes are filler, but the parent should record why the larger tree is retained or reconcile it before claiming full spec completion.

The design text’s planned “The Sanctuary That Feeds Armies” payoff is absent under that title. THR_storehouses_for_world is the closest current node. Its reward at common/national_focus/003_holy_realm.txt:2672–2705 grants command power, places one supply node in a controlled THR state, increases Mandala Reach, and increases Sangha Cohesion if the Mandala exists. Its visible tooltip at localisation/english/003_the_holy_realm_l_english.yml:888 additionally says valid compact members receive infrastructure support. No member infrastructure effect appears in the focus reward, and an exact search found no other consumer of holy_realm_focus_storehouses_for_world or holy_realm_memory_storehouses_for_world. The tooltip/reward mismatch leaves the design text’s strong supply-and-support-for-members payoff unresolved.

THR_final_silence is localized as “The Last Authorization” at localisation/english/003_the_holy_realm_l_english.yml:691–692, while the design text calls the focus “The Final Silence.” Its description and completion event match the authorization role, so this is a name difference rather than a confirmed reward mismatch.

## Icon, filter, and localisation coverage

The final MCP plan contains 111 unique focus IDs. All 111 have static icon references, all 111 titles resolve, and all 111 descriptions resolve. A source check found 59 custom effect/trigger tooltip references, 57 unique keys, and no missing key in the paired THR English localisation. All twelve custom focus-filter IDs are declared and localized in localisation/english/chaosx_gui_l_english.yml:1105–1116. The Ministry icon is the existing GFX_focus_wonderweapons reference; it is not a missing sprite.

Filter groups overlap, so route counts below are per-filter, not additive totals.

| Route filter | Focuses | Distinct icon sprites | Review |
| --- | ---: | ---: | --- |
| FOCUS_FILTER_HOLY_REALM_TEACHING | 8 | 6 | Assigned |
| FOCUS_FILTER_HOLY_REALM_MEDITATION | 8 | 2 | Very high reuse |
| FOCUS_FILTER_HOLY_REALM_GOVERNANCE | 6 | 3 | Reuse across route choices |
| FOCUS_FILTER_HOLY_REALM_SANCTUARY | 3 | 2 | Assigned |
| FOCUS_FILTER_HOLY_REALM_COMPACT | 8 | 5 | Reuse across diplomacy/relief |
| FOCUS_FILTER_HOLY_REALM_ANTI_CHAOS | 14 | 12 | Assigned |
| FOCUS_FILTER_HOLY_REALM_NIRVANA | 16 | 11 | Reuse near capstones |
| FOCUS_FILTER_HOLY_REALM_HIDDEN | 4 | 4 | Assigned |

Repeated icon references include GFX_focus_smiling_buddha on seven meditation/Bodhi focuses, GFX_goal_THR_final on six clean and corrupted end-state focuses, GFX_focus_generic_diplomatic_treaty on five diplomacy/hidden focuses, GFX_focus_generic_league_of_nations on four compact/expansion focuses, and GFX_goal_THR_mercy on four peace/power focuses. These are not missing-asset errors, but they reduce visual distinction between nearby roles; the parent should inspect these groups in the full-tree image before visual acceptance.

## AI behavior gaps

The parent source-repair proofs state that the AI weight bodies were unchanged by the focus source patches. The final MCP plan contains 63 explicit focus ai_will_do bodies. Route-aware examples include Protector Regent weighting against special-chaos enemies, Pilgrim Assembly weighting under the peaceful-chaos condition, the final branch weighting by chaos tier and capital/schism/terminal conditions, and THR_pacification_mandate weighting by war and the coercive floor.

Notable route nodes without explicit ai_will_do are THR_guard_high_passes, THR_mountain_granaries, THR_snowline_clinics, THR_mandala_of_nations, and THR_buddha_mandate. Several may be safely gated or linear, but their choice behavior remains default-scored rather than explicitly route-weighted. Direct focus weight bodies use war, chaos, capital, and compact conditions, but contain no direct stability, Bodhi, or Defilements tokens. Shared helpers could supply those dimensions; their contribution was not expanded here.

The separate chaosx_ai_probability_auditor after-source probability_inspect and probability_compare attempts returned Transport closed, with no after artifact or comparison ID. Its saved baseline scenario was partial: 333 candidate-state rows, 48 unresolved candidates, and 224 unresolved items. No numeric selection, ranking, starvation, or balance claim is supported. The current focus patches preserve all AI bodies, but that does not turn the incomplete probability comparison into current-source evidence.

## Priority findings, validation, and references

1. The final D584 native layout result clears the prior crossing, long connector, through-node, and linear-detour findings. Parent position proof is parent_final_positions_source_repair.json; it names the three position-only edits and states that all non-position bytes match F5.
2. Reconcile the THR_storehouses_for_world compact-member infrastructure tooltip with an actual reward or an accepted text/design change.
3. Reconcile the 111-focus implementation with the nested 75–95 approximate target.
4. Decide whether missing explicit route weights on the five noted anchors are intentional and obtain a successful current-source probability pass before making selection or balance claims.
5. Review the repeated icon groups in the full-tree render before visual acceptance.

Task-specific validation completed: final-source focus inspect at both D584/CF8F and D584/8F2E, a matching D584/CF8F HTML/SVG/JSON render and full-tree PNG raster, 111-focus count, localisation resolution, custom tooltip-key presence, route-filter/icon inventory, parent AST/source-byte proofs, and the parent’s source-side prerequisite equivalence proof. The 8F2E inspect confirms continuous_restrict_freedom_desc now resolves. No hoi4.focus_rewrite call was made because the assigned audit is read-only. No in-game launch or gameplay test was performed. The parent owns visual review of the D584 raster.

Reference evidence used:

- Offline paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:146–169 for shortcut fields and :275–296 for prerequisite OR/AND semantics and the difference between available conditions and drawn prerequisite lines; revision bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203.
- Installed documentation/triggers_documentation.md:3501–3509 for has_completed_focus and COUNTRY scope; revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29.
- Vanilla common/national_focus/germany.txt:42–91 for navigation shortcut targets/zoom and :24017–24040 for an available block using has_completed_focus. Source lookup located german_focus at revision 8fb04f620bd570971ded6c7a3d0ccfbca583db7a27d688fe9cd57c162374a636, and I read these bounded source spans directly.
- The reference-context result omitted unrelated sections; targeted search/read supplied the cited National focus and COUNTRY-trigger rules. It reported no missing offline-wiki or installed-doc source files.

Skills read for this bounded review: chaos-redux-focus-trees, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-event-assets, chaos-redux-improvement-loop, and chaos-redux-subagents. No skills were created or updated. A broader improvement-loop plan was not written because this audit confirmed the required route families are present; the unresolved payoff, count, AI, and visual-review findings are listed above.

Evidence file manifest:

| File | Evidence |
| --- | --- |
| focus_after_source_fresh_20261006.md | This audit handoff |
| mcp_artifacts.json | B0 inspect/render/raster receipts; receipt SHA-256 F72F26754A79084F1EE71E4C142FDC1937A4E46A89DAD070970E1D52CB7DA3FB |
| mcp_artifacts_f5e945184d5e.json | F5 inspect/render/raster receipts; receipt SHA-256 AC66C0FD1B4DDD5BB229B74054A140E372F6C2EACE3AB81D8312807396204C1A |
| mcp_artifacts_d584ec8fe598.json | D584 inspect/render/raster receipts at the original CF8F localisation; receipt SHA-256 35FE8E4A4E06F62C56B278644F37CCCD1030930E4FCC24D353193CF821265DE1 |
| mcp_artifacts_locale_override_inspect.json | Final one-shot inspect at D584/8F2E; artifact SHA-256 c5359fce31736a20c6ab15e64f1afcd7f20837e939c08c0d634467347bf0cb32, 580618 bytes |
| parent_source_repair_20261006.json | Parent G6 initial source/availability repair proof |
| parent_clearance_source_repair.json | F5 clearance and chapter-entry presentation proof |
| parent_final_positions_source_repair.json | D584 final three-position repair proof |
