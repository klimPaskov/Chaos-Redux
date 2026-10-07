# Event 006 Signature Focus Module Review

Review date: 2026-10-07.

Disposition: the 31-node source audit is complete, but mandatory probability evidence and MCP coverage for the imported nodes remain unresolved. This is a review of the signature module only, not a completion claim for Event 006.

## Scope and accepted basis

Reviewed the 31 imported shared focuses in common/national_focus/006_independence_wave_signature_modules_focus.txt: 10 DSX/Oyo, 10 ATJ/Aceh, and 11 IAX/Mon. The parent tree imports them at lines 82–112 of common/national_focus/006_independence_wave_focus.txt; the 220-node regional baseline at commit 416688b8963 is accepted context and was not re-audited.

The accepted design basis supplied for this task is docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md:869–891 and docs/specs/006_independence_wave_specs/research/006_signature_country_research_dossiers.md:67–115.

The parent owns focus and effect edits. No focus, effect, decision, trigger, localisation, idea, constant, or asset source was changed by this reviewer. The decision implementation was left to its assigned auditor; only focus-linked decision identifiers were checked for existence.

## Route coverage

| Route | Implemented in the 31 nodes | Coverage and qualification |
|---|---|---|
| DSX / Oyo | Table the power centers; Alaafin charter, Oyo Mesi mandate, or Yoruba town federation; horse guard, town guard, or Ibadan terms; market roads; Yoruba congress; Oyo compact. | The three institution choices have distinct route flags and follow-up ideas, then join shared construction and congress work. All named Oyo/Mesi/town scope is represented. |
| ATJ / Aceh | District authority, ulama school board, or shared council; reform-school network; port board and credit; maritime congress / FORM-36 path. | PUSA is a period-gated decision hook, not one of these focus ids. The school-network description explicitly treats its general network as pre-PUSA; the trigger permits PUSA organization after 1939-05-04, i.e. from 5 May 1939. Detailed decision behavior remains with the decision auditor. |
| IAX / Mon | Local councils or central river office; Mon-language schools; Salween transport; Tenasserim border watch; school-delegate exchange; local autonomy and mainland compact / FORM-37 path. | The autonomy and FORM-37 gates require the local-council route. The central river-office route ends after “Place River Works under the Office,” with only the river-office idea (+3% political power factor) and no route-specific capstone. That is a definite depth/payoff concern; whether central administration is meant to terminate there is unresolved in the accepted thematic text. No post-1947 organization names were found in the scoped module support files. |

## High-priority findings

1. **Three exact focus-coordinate overlaps.** HOI4 relative positions add recursively. In DSX, independence_wave_dsx_focus_bind_the_horse_guard_to_the_charter (module line 168) and independence_wave_dsx_focus_survey_oyo_market_roads (line 253) both resolve to (-1, 3) from the Oyo root. independence_wave_dsx_focus_guarantee_ibadans_place (line 224) and independence_wave_dsx_focus_authorize_the_yoruba_congress (line 281) both resolve to (1, 3). In ATJ, independence_wave_atj_focus_confirm_district_guarantees (line 491) and independence_wave_atj_focus_extend_the_school_network (line 566) both resolve to (-1, 3). The node-level package allow_branch checks permit both nodes in each pair; their availability requirements lock completion, not visibility. These are layout defects, not hidden-node collisions.

2. **IAX river-office route closure is thin.** independence_wave_iax_focus_direct_the_river_office and independence_wave_iax_focus_place_river_works_under_the_office form a two-focus spur ending in a passive idea. can_independence_wave_iax_signature_publish_autonomy and can_independence_wave_iax_signature_join_form37 require the local-council route (signature trigger file lines 288–304). Shared school, transport, border, and delegate content remains reachable, but this route has no distinct late payoff in the 31-node module. Parent review should decide whether that is an intended central-administration endpoint or a missing route consequence; this subagent did not design a replacement route.

3. **Route-aware AI is absent from these focus blocks; numeric balance remains unresolved.** All 31 focuses have an explicit ai_will_do base using the shared urgent, standard, or high tier; this module has no per-focus modifier/add/factor. In each unsettled institutional choice set, the three alternatives use the same standard tier, so this module does not express a route preference based on balance, war, stability, or other campaign state. The assigned probability auditor found 31/31 local weight blocks but the MCP probability adapter returned no_weighted_surfaces, zero candidates, and no scenario evaluations. No effective ranking or probability conclusion is supported.

4. **Icon reuse is high, but there are no missing references.** All 31 focus icon ids resolve through interface/006_independence_wave.gfx and their DDS files exist. The module uses eight shared sprite ids; GFX_goal_independence_wave_popular_councils appears 10 times, infrastructure authority 5, league congress 4, traditional restoration 3, founding administration 3, regional formable 3, army integration 2, and recognition diplomacy 1. The three route-choice families are visually distinct at their choice nodes; reuse is concentrated in shared support and institution nodes. No asset-production or icon-reference patch was made.

## Icon coverage

| Module | Icon use counts | Total |
|---|---|---:|
| DSX | Founding administration 1; traditional restoration 1; popular councils 3; league congress 2; army integration 1; infrastructure authority 1; regional formable 1. | 10 |
| ATJ | Founding administration 1; traditional restoration 2; popular councils 3; league congress 2; infrastructure authority 1; regional formable 1. | 10 |
| IAX | Founding administration 1; popular councils 4; infrastructure authority 3; army integration 1; recognition diplomacy 1; regional formable 1. | 11 |

## Localisation and reward mismatch review

No missing focus title or description was found for the 31 ids. All focus custom_effect_tooltip and custom_trigger_tooltip keys referenced by this module were present. The descriptions match the staged effects: institution choices select a settlement, later focuses record its terms, road/transport/port/border work opens paid projects, and congress/federation focuses open negotiation or readiness hooks. No clear title/reward mismatch was found.

The small route ideas are specific to institutions and have corresponding cleanup; other rewards include construction, decision availability, public settlement, diplomatic exchange, and formable readiness. No repeated generic reward pattern dominates this 31-node slice.

## Parent-owned source corrections verified

The current independence_wave_dsx_signature_publish_compact effect checks that independence_wave_dsx_signature_oyo_compact_published is absent before setting it and calling independence_wave_focus_reward_ambition; the guard is present. The CXT registration caller initializes chaosx_test_country_extension_registration_added to the “none” value before invoking the nested extension-registration effect. These are parent-owned source changes, not edits from this review. No new portrait consumer appears in these focuses; portrait-source blockers are separate from this mechanics audit.

## MCP and source evidence

- hoi4.focus_inspect on the owner tree succeeded at revision 8412574aa1428985f198339e27417bde9a74704c1cce9ff28a67971fd91322a3 and reported 184 focuses, 196 connectors, and zero diagnostics for the inspected tree view. It did not include this imported module; inline source inventory was limited to 64 of 93 paths. The inspector also reported MCP_INLINE_FILES_TRUNCATED.
- The owner-tree hoi4.focus_render succeeded and returned HTML, SVG, JSON, source-map, and plan artifacts. Useful links: [focus inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9fe3571ed37ff3a78576c14ae792a82d8bd1e50533defa1080624ff6b1c3fc00/34196a5fb2902077478fbb0fca8f84bf08ce032f67e3d04e3bd3065449fbbadf/focus-inspect.8412574aa1428985.json), [owner-tree SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65038c84aafa45b0dedf8601921c47fde21d986764e0ee05922593b0020b7bce/a9c6ba6f2e87503b845db99a73782d77b0d23ddc313ba977f69ec96e62be0dd2/independence_wave_focus_tree.focus.svg), and [owner-tree JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7b31572b86a2c18135766e0be6410a4c4e39fb23781a6243153d176900cc47b/c2515a444ca1a4c0fc7afc0b09de9079a98a68cb3b6a3da652ab7982e7cf16/independence_wave_focus_tree.focus.json).
- A direct inspect of the module file with the parent tree id returned FOCUS_TREE_NOT_FOUND because the module contains imported shared_focus blocks rather than a focus_tree declaration. Three route crop requests to hoi4.focus_render returned FOCUS_CROP_REQUIRES_RASTER; the follow-up hoi4.focus_raster requests were blocked because the full-tree dimensions were 17,139 × 1,952 pixels, exceeding the 16,384-pixel ceiling. Thus the imported-node MCP layout gap is retained; source-coordinate arithmetic above is not presented as MCP validation.
- chaosx_ai_probability_auditor ran hoi4.probability_inspect first, but the adapter returned no_weighted_surfaces with 0 candidates despite 31 local ai_will_do blocks. Its artifact is [probability inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c99571bc52aa624bd6ee17e244c3b316f6939a2c216276762ec2b243dc25334/e7156b35329d40a3595ad137e66c3df6bef6767da6fbe6583c4aae6de183a3ad/probability-inspect-c0a1a1fee829.json). It recorded MCP revision d908dcc92f6f7b6cf63953db23338a8ffbffd578d80a326ac4d72775bb1606fe and source hash c0a1a1fee829d0f7af71347acf5ee9afa3b5b85c389ca6fd55192cd08df831fd, while the local file byte SHA-256 was BD640BFF00A58ABD8388D968A5E3F20008716F3B70BA61451A17B09618B350C0. Hash normalization is unspecified, so MCP/local source identity is unresolved. Candidate-pool and named-scenario evaluate calls did not return; no probabilities, rankings, external strategy factors, or complete candidate-pool claim is available.
- Reference evidence: offline National focus modding snapshot revision bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203, position lines 254–274, prerequisites/mutual exclusions 275–296, visibility/bypass 405–429, shared focuses 818–838, and AI weighting 604–625. Installed game effects documentation revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af, mark_focus_tree_layout_dirty lines 4811–4821. Vanilla precedent: game:common/national_focus/afghanistan.txt, revision 2b67201021a5dcb77eca2ef174932d4720eb0872f26025b77250b7c7fb35986d; AFG_qargha_dam lines 249–290 shows prerequisite, bypass, available, and AI structure; AFG_look_to_other_partners lines 734–779 shows a reciprocal-route mutual exclusion pattern.

## Validation and remaining limits

Meaningful source checks confirmed 31 unique focus ids, 31 parent-tree imports in three groups (10/10/11), 31 AI blocks, all 31 title/description pairs, all referenced custom trigger/effect tooltip keys, and all eight icon GFX/DDS references. No live game was launched. No focus rewrite, AI adjustment, decision-body audit, portrait work, or Git operation was performed.

The mandatory probability analysis remains incomplete because the adapter did not discover the imported shared-focus weights and its source identity differs from the local byte hash. Route-specific MCP layout evidence for these imports also remains unavailable. Parent review is needed for the overlaps, the Mon river-office endpoint, and those two MCP coverage limits.

Skills used: chaos-redux-focus-trees, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-event-assets, chaos-redux-improvement-loop, and chaos-redux-subagents.

### Probability tier inventory

The source constants are urgent=100, standard=10, and high=25. Across the 31 local blocks, 7 use urgent, 8 standard, and 16 high. These are source base scores only; the auditor could not establish effective weights or rank probabilities.

## Follow-up review: applied coordinates and route-choice AI disposition

Parent application verified in common/national_focus/006_independence_wave_signature_modules_focus.txt: the proposed x offsets are present exactly. DSX bind_the_horse_guard_to_the_charter is x=-1 relative to renew_the_alaafins_charter; DSX guarantee_ibadans_place is x=1 relative to federate_the_yoruba_towns; ATJ confirm_district_guarantees is x=-1 relative to protect_uleebalang_districts. Their y values and relative_position_id anchors match the proposal. The other 28 nodes were not part of the proposed movement. This reviewer made no gameplay edit.

The earlier finding that route-aware AI is absent was too strong and is superseded by this bounded review. For DSX and ATJ, the three institution focuses are each available while independence_wave_internal_power_struggle_settled is absent; once settled, each route is available only when one of its compatible balance flags is set. The corresponding bypasses complete the matching route when that balance is already settled. Their choice effects, when unsettled, call the generic first-center, second-center, or compromise effect, which writes the balance flag and sets independence_wave_internal_power_struggle_settled before writing the route flag.

IAX follows the same contract with two choices: direct_the_river_office is the first-center route, while trust_local_mon_councils accepts the second-center or compromise balance. Its availability and bypass predicates match those outcomes, and its choice effects write the generic balance before the route flag.

Revised disposition: equal standard base weights are not a confirmed AI feature gap for these choices. A settled government makes only its compatible route selectable, so equal weights do not decide among incompatible alternatives. Before settlement, the AI may choose among the eligible institution choices at equal base weight, and that focus choice itself establishes the government balance. The accepted source supplied for this scope does not require further AI preference by ideology, war, or stability for these particular choices. Record the equal weighting as intentional choice among unsettled institutions, with no numeric change recommended. If the parent expects additional campaign-conditioned preference, that expectation remains a design question rather than a proven implementation defect.

Evidence read was bounded to the eight route-choice availability blocks in the focus module, the eight choose_* effects in common/scripted_effects/006_independence_wave_signature_modules_effects.txt, and the three generic balance effects in common/scripted_effects/006_independence_wave_focus_effects.txt. No MCP calls, waits, spawns, decision-body audit, AI edits, or gameplay edits were made in this follow-up.


## Focused closure disposition: Mon river-office endpoint

Disposition: implemented for this 31-node review scope. The prior Mon river-office depth/payoff concern is closed by the accepted parent integration. This does not change the route family or add a focus.

Acceptance basis: the user reports that the parent accepted the planner recommendation under the user's understanding of the authority. That is the design-acceptance basis; the source details and validation below are implementation evidence.

The existing independence_wave_iax_focus_place_river_works_under_the_office now leads to the paid independence_wave_iax_signature_commission_river_services decision (common/decisions/006_independence_wave_signature_modules_decisions.txt:330). Its preparation trigger requires the river-office route and completed river charter, Mon school trust, paid Salween transport, and Tenasserim border watch, and disallows the local-council route (common/scripted_triggers/006_independence_wave_signature_modules_triggers.txt:309). The decision uses the standard 120-day duration and administration cost. Its start records generation, package, and anchor; successful completion rechecks the same-generation project, marks the commission, replaces the plain office idea, and applies a value bundle.

The completion bundle records +5 legitimacy, +15 capacity, and -5 instability through independence_wave_focus_apply_value_bundle using the minor_gain, major_gain, and minor_loss constants. The replacement independence_wave_iax_river_service_administration idea carries +5% political power and +10% infrastructure construction speed. Source references are common/scripted_effects/006_independence_wave_signature_modules_effects.txt:810 and :828, common/ideas/006_independence_wave_signature_modules_ideas.txt:145, common/script_constants/006_independence_wave_constants_registry.txt:6728, and common/script_constants/006_independence_wave_constants_registry.txt:1034.

The five ATJ/IAX institutional completion helpers call independence_wave_ready_formable_apply_signature_governance: ATJ district, school-board, and shared-council completion; IAX local-charter and river-charter completion (common/scripted_effects/006_independence_wave_signature_modules_effects.txt:423, :436, :449, :680, :693). The shared helper records the exact chosen institution as replaced under an owned carrier or member compact, and applies the matching standalone idea when no such carrier owns the slot. It preserves the selected restoration terms without introducing a fourth national spirit. Helper definition: common/scripted_effects/006_independence_wave_ready_formable_contracts_effects.txt:77.

The Aceh PUSA route remains paid and period-gated from 5 May 1939: successful organization grants one 50% industry research bonus and retains the 2% PUSA school-network idea. The source uses the standard 120-day duration; constants and reward writer are in common/scripted_effects/006_independence_wave_signature_modules_effects.txt:20, :540, and :549, with the date gate in common/scripted_triggers/006_independence_wave_signature_modules_triggers.txt:116.

The parent reports 35 ordering/restoration cases and 44 original/new IAX lifecycle cases passed. This reviewer did not rerun those cases.

Superseded finding: the Mon river-office route-endpoint gap is closed for this scoped implementation. Remaining open items from the earlier review are the imported-node MCP layout coverage and the probability-adapter AI coverage/source-identity issue. This disposition makes no native validation claim and does not claim full Event 006 completion. No MCP calls, spawns, waits, gameplay edits, or Git operations were performed.
