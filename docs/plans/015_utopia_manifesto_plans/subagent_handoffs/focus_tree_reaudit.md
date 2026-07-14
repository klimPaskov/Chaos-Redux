# Event 15 Utopia Manifesto Focus Tree Re-Audit

## Verdict

**FAIL**

The repaired tree closes the previous audit's impossible Joke formation, paid-growth cap, decision-phase, Ledger-delta, and orphan-reward failures. It is still not completion-ready for three independent reasons:

1. Three focus rewards bypass the stage-safe idea lifecycle helpers. A reachable Stewardship sequence can still display four Event 15 spirits, and Auxiliary/Stewardship resolution can leave the wrong lifecycle family active.
2. The rendered tree is not a usable six-band layout. It spans 80 columns and has 86 connector crossings, 41 connector-through-node intersections, and 26 long connectors.
3. The five route openers still select primarily from ideology, with war as the only additional state input for Closed Island. This does not implement the accepted state-aware route-selection matrix.

This is a read-only gameplay audit. No gameplay, localisation, asset, specification, or spreadsheet source was edited.

## Audit basis

The definitive focus source audited here is:

| Source | SHA-256 | Lines |
| --- | --- | ---: |
| common/national_focus/015_utopia_manifesto_focus_tree.txt | BAD7F93468CDEC937324C711F835145C30A000CB3714585BA64A62F847F12BE2 | 3385 |

Critical dependency snapshot at the final source review:

| Source | SHA-256 | Lines |
| --- | --- | ---: |
| common/scripted_effects/015_utopia_manifesto_country_effects.txt | C817A1818E835063427D51274F3E3AD2B08F87397B65B80C6212EA78E57D8C08 | 446 |
| common/scripted_effects/015_utopia_manifesto_identity_effects.txt | 35EEA58EFCA30F701E860A943BDB98FD4BBEAF7AE0320B5FA074A7FE1FA8F08B | 846 |
| common/scripted_effects/015_utopia_manifesto_decision_effects.txt | 719EFD3663C3E7D8B76FD20AEF9D6FE0F67926893F0824B3D7ACC7223CF9D5F1 | 1220 |
| common/scripted_triggers/015_utopia_manifesto_triggers.txt | 8E879BE34AAF6814221553B68C4F4721F81EB73382B4875AF55C8DDD8F31A35A | 1274 |
| common/decisions/015_utopia_manifesto_decisions.txt | 7536B1F429C3F0F4F4ECEE789F2A26072DF50E78631B2C7738C4A0A25743D52F | 4288 |
| common/ai_strategy/015_utopia_manifesto_ai_strategy.txt | E6DB306460F20B84CB452FAAFC300D062A318CBD5B48EB01BB8A24DA30658CBB | 288 |

The main scripted-effects file was being changed concurrently outside this audit while evidence was gathered. The focus hash above, the three remaining focus/AI blockers, and the country-helper hash are stable. Any later dependency change should be compared against this snapshot before reusing a PASS disposition below.

Primary design references:

- Visual architecture: docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_3_focus_tree_architecture.md:11-22.
- State-aware route selection: docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_7_ai_balance_and_compatibility.md:54-167.
- Idea families: docs/specs/015_utopia_manifesto_specs/matrices/idea_lifecycle_matrix.md:5-18.
- Route and support-branch promises: docs/specs/015_utopia_manifesto_specs/matrices/focus_route_matrix.md:3-20.
- Prior focus audit: docs/plans/015_utopia_manifesto_plans/subagent_handoffs/focus_tree_audit.md.
- Country-audit preliminary: docs/plans/015_utopia_manifesto_plans/subagent_handoffs/country_package_audit.md:81-95.

## Completion blockers

### P1 FTR-RE-001: stage-safe idea helpers are still bypassed by focus rewards

The repaired country helper layer correctly models temporary liabilities as track replacement:

- Auxiliary helpers clear the current route-institution family before applying an Auxiliary stage and restore the recorded route stage on resolution at common/scripted_effects/015_utopia_manifesto_country_effects.txt:396-417.
- Stewardship helpers clear the current Garden family before applying a Stewardship stage and restore the recorded Garden stage on resolution at common/scripted_effects/015_utopia_manifesto_country_effects.txt:419-446.
- The stable mature set remains one route institution, one Common Store stage, and one Garden District stage.

Three focus call sites do not use those helpers:

| Focus | Current lines | Defect |
| --- | ---: | --- |
| utopia_manifesto_end_the_auxiliary_contract | 2312-2329, especially 2323 | Removes only utopia_manifesto_auxiliary_dependency. If the live stage is mitigated or failure, it remains, and the recorded route-institution stage is not restored. |
| utopia_manifesto_stewardship_obligations | 2755-2783, especially 2767-2777 | Swaps only the base Garden idea. If Garden is already mitigated, failure, or final, the else branch adds Stewardship without clearing Garden. |
| utopia_manifesto_status_by_consent | 2879-2903, especially 2890-2896 | Swaps only the base Stewardship idea. A mitigated, failure, or final Stewardship stage survives and the recorded Garden stage is not restored. |

A reachable four-spirit sequence remains:

1. Commit any political route and establish the Common Store track. Before Island Made Real, the active visible set is route institution + Common Store + route property settlement, which correctly totals three.
2. Advance the Necessary Ground/Stewardship branch before finishing the independent Island project, then complete utopia_manifesto_stewardship_obligations.
3. No base Garden idea exists, so lines 2774-2777 add base Stewardship without retiring the property-settlement track.
4. The visible set becomes route institution + Common Store + route property settlement + Stewardship: four Event 15 spirits.

The same defect occurs if Island Made Real was completed first and Garden has already advanced to mitigated, failure, or final: the focus tests only the base Garden ID, then adds Stewardship beside the advanced Garden stage.

This directly fails the requested maximum of three. The Auxiliary and status-vote call sites also fail lifecycle restoration even when their immediate visible count remains three.

Exact correction:

1. In utopia_manifesto_end_the_auxiliary_contract, replace the direct remove_ideas line with:
   - utopia_manifesto_resolve_auxiliary_dependency = yes
2. In utopia_manifesto_stewardship_obligations, replace the base-only if/else idea block with:
   - utopia_manifesto_begin_stewardship_burden = yes
3. In utopia_manifesto_status_by_consent, replace the base-only swap block with:
   - utopia_manifesto_resolve_stewardship_burden = yes
4. Re-run a direct add_ideas/remove_ideas/swap_ideas scan over the focus file and route all package-family transitions through the lifecycle API. The remaining direct starting-family adds at lines 54-57, 104-107, and 201-204 should at minimum test the whole family, not only the base idea.
5. Re-trace the maximum compatible visible spirit count through base, mitigated, failure, final, crisis-switch, auxiliary, stewardship, formation, and post-formation states. The maximum must be three and temporary liability resolution must restore the recorded stage, not merely the base stage.

The country-audit preliminary on generic repeatability is otherwise repaired. Citizen Watch is one-time at common/decisions/015_utopia_manifesto_decisions.txt:3542-3551, Engineer Companies at 3583-3592, and Auxiliary Contracts at 3628-3635. The residual issue is lifecycle call-site correctness, not repeatable generic unit creation.

### P1 FTR-RE-002: the visible layout fails the accepted six-band architecture

The accepted design requires six readable top-to-bottom bands, five distinct political lanes, shared support branches that visibly interlock with several routes, and no five isolated vertical columns. The current fixed-coordinate source does not meet that visual contract.

Fresh focus inspection metrics:

| Metric | Current |
| --- | ---: |
| Focuses | 122 |
| Connectors | 170 |
| Connector crossings | 86 |
| Connector-through-node intersections | 41 |
| Long connectors | 26 |
| Width | 80 columns |
| Height | 30 rows |
| Maximum horizontal connector span | 43 columns |
| Maximum vertical connector span | 14 rows |
| Maximum Manhattan span | 45 |
| Total horizontal connector span | 746 |

The rendered PNG is an extremely wide canvas with tiny, widely separated route clusters, large empty gaps, and long shared-branch connectors cutting across unrelated nodes. This is not only a cosmetic score: the opening trunk and route commitment cannot be read reliably at normal review scale.

Concrete source and renderer evidence:

- utopia_manifesto_the_country_as_a_question at lines 216-220 is x=32, y=6.
- utopia_manifesto_household_gives_consent at lines 244-248 is x=7, y=8. Their connector spans 25 columns and 2 rows.
- utopia_manifesto_nothing_private_in_necessity at lines 501-505 is x=19, y=8. Its opener connector spans 13 columns and 2 rows.
- The connector from utopia_manifesto_count_houses_and_hands to utopia_manifesto_homes_near_work intersects utopia_manifesto_convene_the_interpretive_congress.
- The connector from utopia_manifesto_agriculture_for_all to utopia_manifesto_every_hand_knows_the_soil intersects utopia_manifesto_cooperative_land_trusts and utopia_manifesto_constitution_of_provision.
- The connector into utopia_manifesto_every_hand_knows_the_soil also intersects utopia_manifesto_voluntary_commonwealth_league.
- The renderer classifies these as fixed-endpoint unsatisfied crossings or connector-through-node warnings.

Artifacts:

- Inspect JSON: hoi4-agent://workspace/chaos_redux/artifact/72b3df60502caef89e9f0872d2792f40f6d2886174c4de97549a044c80a55ecb/aa0bd78dfd4100f23eb4be4396d4d8b7b5369d670ac1352a864059f788162c88/focus-inspect.20e7117fcacfebfc.json
- Rendered PNG: hoi4-agent://workspace/chaos_redux/artifact/01d6b1ba7803c7eb6d5718de6ad204cff341540c7481a86ba570e3896f58f9ec/df86015e7172499926d5b196b3a5ae68ff8587a3984f2989c8da90e95a1e4551/utopia_manifesto_tree.focus.png
- PNG SHA-256: 01D6B1BA7803C7EB6D5718DE6AD204CFF341540C7481A86BA570E3896F58F9EC
- Layout hash: 4DC9D30A7C5A153BB448531D9AEF4B1DC7150D2CE332DF940C3A58574FF484B3

The MCP validator reports no technical blocker because these are layout warnings rather than missing-source errors. The auditor escalates them to a completion blocker because the accepted specification and focus-tree audit standard explicitly require a usable visible layout.

Exact correction:

1. Perform a coordinate-only layout pass unless a prerequisite edge must be refactored for clarity.
2. Keep Recovery/Survey and the Interpretive Congress in a compact centered trunk.
3. Put all five route openers in the same route-commitment band close enough to the congress hub that no route-root connector spans 13-25 columns.
4. Preserve five recognizable political lanes, then pull shared Callings, Stores, Garden, Defense, Foreign Commonwealth, Necessary Ground, and Stewardship hubs back toward the center so their lines interlock without crossing route nodes.
5. Put crisis correction, formation proof, proclamation, and post-formation play in successive lower bands instead of a remote right-hand strip.
6. Eliminate every connector-through-node diagnostic in the opening trunk and route-commitment band. The three concrete through-node cases above must be zero.
7. Re-render and inspect the PNG at normal review scale. A passing layout must visibly read in the six accepted bands and materially reduce the 86/41/26 crossing/intersection/long-connector counts; technical parser success alone is insufficient.

### P1 FTR-RE-003: route-opener AI is not state-aware

The accepted route-selection matrix requires the AI to respond to stability, all four Ledger dimensions, infrastructure, education/technical capacity, geography, neighbors, war pressure, public debate, conduct, and route failure. Current opener weights are:

| Route opener focus | Focus/AI lines | Current state inputs |
| --- | ---: | --- |
| utopia_manifesto_household_gives_consent | 244-275; ai_will_do at 269-275 | Democratic government only |
| utopia_manifesto_nothing_private_in_necessity | 501-532; ai_will_do at 526-532 | Communist government only |
| utopia_manifesto_country_measured | 776-807; ai_will_do at 801-807 | Neutral government only |
| utopia_manifesto_one_island_one_measure | 1061-1096; ai_will_do at 1086-1095 | Fascist government and has_war |
| utopia_manifesto_read_island_as_a_mirror | 1321-1354; ai_will_do at 1348-1354 | Hidden base plus Democratic government |

The Joke reveal trigger at common/scripted_triggers/015_utopia_manifesto_triggers.txt:588-619 is substantially state-aware, but it is a reveal/availability gate. Once revealed, the focus choice itself still lacks the accepted education, Choice/Assignment, Concord, debate, route-failure, and security weighting.

The strategies in common/ai_strategy/015_utopia_manifesto_ai_strategy.txt:45-189 activate only after a route flag exists. They shape construction and war behavior after commitment and cannot repair route selection.

Exact correction:

1. Add reusable scripted preference and avoidance triggers, or equivalent centrally tuned modifiers, for all five openers.
2. Consent must weigh high stability, trusted/rising Concord, modest Need, peaceful small-neighbor opportunity, and low immediate war pressure; it must avoid severe war and weak state capacity.
3. Common Table must weigh labor/industrial and council/property-conflict proxies plus compatible neighbors; it must avoid a tiny unsupported administrative base and isolation.
4. Guardians must weigh low Plenty, weak infrastructure, technical/education capacity, landlocked geography, construction need, and moderate Concord; it must avoid strong autonomy resistance and weak unsupported administration.
5. Closed Island must weigh war/encirclement, severe Need, low Concord, military threat, and compact/defensible geography; it must strongly avoid peaceful democracy, high Choice/Concord, and open-trade dependence.
6. Joke Understood must remain rare but non-zero when its reveal gate is met, with positive weight for education, Choice, Concord, debate, criticism, and literal-route failure, and negative weight for censorship, Assignment, colonial war, penal labor, and security emergency.
7. Put tuning values in shared script constants or file-local constants as appropriate; do not scatter raw weights across the five focuses.
8. Re-audit selection weights for representative democratic-stable, communist-industrial, neutral-landlocked, authoritarian-at-war, and high-education reformist actors, plus at least one high-chaos exception for each route.

## Prior audit disposition

| Required recheck | Result | Evidence |
| --- | --- | --- |
| Broad recognition and Joke formation | PASS | Joke formation requires utopia_manifesto_broad_recognition_proven at common/scripted_triggers/015_utopia_manifesto_triggers.txt:1063. League legitimacy completion produces it at common/scripted_effects/015_utopia_manifesto_decision_effects.txt:964-975. Reform Without Paradise unlocks league play at focus lines 1500-1523 and is accepted by league initialization at decisions lines 2963-2981. Prove League Not a Mask is available with a stable league and external network at decisions lines 3275-3304; its mission completes the proof at 3307-3324. The minimum network is one. |
| Paid growth on every route | PASS | Static pairing finds 34 can-pay tier gates and 34 matching paid-growth calls: 26 institutional and 8 military. No gated paid focus lacks its payment call. |
| Closed Island paid growth | PASS | Households of Service pays military foundation at 1100-1115; Closed Store and Penal Works pay institutional foundation at 1138-1171; Cut the Channel pays institutional capstone at 1257-1272; Perfect Island pays military capstone at 1287-1302. |
| Post-formation paid growth | PASS | Integrate the Ring pays institutional network at 3212-3226; The Commonwealth at War pays military capstone at 3322-3338; Plenty in an Age of Chaos pays institutional capstone at 3357-3372. |
| Military growth cap | PASS | The former fixed exhaustion point is replaced by capacity = 12 + 2 per controlled state + 1 per chartered district, clamped to 36. The availability trigger compares batches below current capacity. |
| Decision phases 1-9 | PASS | Constants define foundations=1, callings=2, reserves=3, districts=4, necessary_ground=5, league=6, route=7, formation=8, mature=9. Producers exist at focus lines 58, 227, 1575, 1916, 2557, 2382, 2713/3136, 3174, and 3254. The phase setter is monotonic. |
| Live dynamic growth | PASS | Acceptance refreshes costs before loading the tree. Costs and capacity recompute from current controlled-state count and tier immediately before payment. on_state_control_changed refreshes only the accepted new/old controllers, not every country. |
| Ledger delta scale | PASS | Every focus uses the narrative delta ladder: 5/10/15 and their negatives. Current focus-use counts are tiny 76, small 84, medium 45, negative_tiny 80, negative_small 45, negative_medium 17. The old repeated 2/4/7 focus deltas are gone. |
| Formation threshold reachability | PASS, static | Defaults are Need 45, Plenty 35, Concord 40, Assignment 20, Reserve 15, then country-state contributions apply. Route and support focuses supply full 5/10/15 steps. The reserve system can explicitly reach 70 through the Two-Year Reserve outcome, satisfying the Closed route's reserve threshold; other route thresholds have matching positive/negative focus and decision levers. No threshold is statically impossible. |
| Exact eleven orphan rewards | PASS | All eleven now have a consumed non-Ledger effect; detailed table below. |
| Five route families and formation convergence | PASS, structural | All five opener/capstone families exist. Proof of the Commonwealth accepts the five capstones in one alternative prerequisite block at focus lines 3152-3168 and also requires Island Made Real and First Associate. Normal and crisis-correction paths both produce phase 7. |
| Focus references | PASS | 122 focus declarations, 122 ai_will_do blocks, 122 completion_reward blocks, 224 focus references, zero unresolved focus references, and no duplicate focus IDs. |
| Focus localisation | PASS | All 122 focus IDs have title and description keys. The fresh renderer resolved 122/122 titles. |
| Focus icons | PASS | 72 unique focus sprite IDs resolve through the current GFX/DDS package; the fresh renderer displayed icons for the complete 122-node tree. |
| Generic military repeatability preliminary | PASS | Citizen Watch, Engineer Companies, and Auxiliary Contracts have durable one-time visibility gates. |
| Maximum three compatible spirits | **FAIL** | FTR-RE-001. |
| Visible six-band layout | **FAIL** | FTR-RE-002. |
| State-aware route-selection AI | **FAIL** | FTR-RE-003. |

## Exact eleven formerly orphaned rewards

| Focus | Consumed non-Ledger result | Status |
| --- | --- | --- |
| utopia_manifesto_transparent_store_accounts | Calls utopia_manifesto_rotate_common_store_network at line 359 | PASS |
| utopia_manifesto_council_autonomy | Calls utopia_manifesto_apply_route_institution_mitigation at line 691 | PASS |
| utopia_manifesto_emergency_central_plan | Calls utopia_manifesto_apply_route_institution_failure at line 722 | PASS |
| utopia_manifesto_shortage_forecasting | Calls utopia_manifesto_rotate_common_store_network at line 898 | PASS |
| utopia_manifesto_useful_freedom | Calls route-institution mitigation at line 953 and records its conduct flag | PASS |
| utopia_manifesto_sunset_clauses | Calls route-institution mitigation at line 1439 | PASS |
| utopia_manifesto_rotate_old_stores | Calls Common Store rotation at line 1816 | PASS |
| utopia_manifesto_no_glory_in_the_field | Sets utopia_manifesto_strict_war_authorization at line 2231; coercive Need decisions consume it at decisions lines 2286-2287 and 2329-2330 | PASS |
| utopia_manifesto_necessary_victory | Sets utopia_manifesto_necessary_victory_doctrine at line 2294; the same escalation decisions require it | PASS |
| utopia_manifesto_offer_the_first_surplus | Sets utopia_manifesto_first_surplus_offered at line 2405; league initialization consumes it at decisions line 2970 | PASS |
| utopia_manifesto_a_rule_for_need | Sets mutually exclusive case expansion/limit law at lines 3277-3286; case preparation/refresh effects consume both laws | PASS |

## Balance and pacing

Static pacing is broadly appropriate for a full replacement campaign:

- 18 short focuses at cost 5, 71 standard focuses at cost 10, and 33 long focuses at cost 15.
- Those correspond to the established 35/70/105-day bands.
- Route capstones are long projects, shared national systems continue after route commitment, and formation/post-formation content occupies the lower campaign bands.
- Military and institutional growth consumes live manpower, equipment, experience, political power, and state-scaled costs rather than granting free generic expansion.
- The dynamic military capacity no longer prevents the Closed route or post-formation defense from paying their required batches.

No new numeric balance blocker was found in the focus rewards or formation thresholds. AI route balance cannot be accepted while FTR-RE-003 remains; ideology-only selection will distort route frequency regardless of otherwise sound reward tuning.

## Machine-readable result

~~~yaml
audit:
  id: event_015_focus_tree_reaudit
  verdict: FAIL
  audited_focus:
    path: common/national_focus/015_utopia_manifesto_focus_tree.txt
    sha256: BAD7F93468CDEC937324C711F835145C30A000CB3714585BA64A62F847F12BE2
    lines: 3385
    focus_count: 122
  blockers:
    - id: FTR-RE-001
      severity: P1
      domain: idea_lifecycle
      focus_ids:
        - utopia_manifesto_end_the_auxiliary_contract
        - utopia_manifesto_stewardship_obligations
        - utopia_manifesto_status_by_consent
      required_calls:
        - utopia_manifesto_resolve_auxiliary_dependency
        - utopia_manifesto_begin_stewardship_burden
        - utopia_manifesto_resolve_stewardship_burden
      current_reachable_spirit_maximum: 4
      required_spirit_maximum: 3
    - id: FTR-RE-002
      severity: P1
      domain: visible_layout
      metrics:
        nodes: 122
        connectors: 170
        crossings: 86
        node_intersections: 41
        long_connectors: 26
        columns: 80
        rows: 30
        maximum_horizontal_span: 43
        maximum_vertical_span: 14
        maximum_manhattan_span: 45
      required_result:
        six_bands: true
        distinct_route_lanes: true
        shared_branches_interlocked: true
        opening_and_route_through_node_diagnostics: 0
        human_png_review: required
    - id: FTR-RE-003
      severity: P1
      domain: route_selection_ai
      focus_ids:
        - utopia_manifesto_household_gives_consent
        - utopia_manifesto_nothing_private_in_necessity
        - utopia_manifesto_country_measured
        - utopia_manifesto_one_island_one_measure
        - utopia_manifesto_read_island_as_a_mirror
      missing_input_classes:
        - ledger_state
        - stability_and_state_capacity
        - infrastructure_and_education
        - geography_and_neighbors
        - war_and_security_pressure
        - debate_conduct_and_route_failure
  prior_findings:
    broad_recognition: PASS
    paid_growth_all_routes: PASS
    paid_growth_closed_route: PASS
    paid_growth_postformation: PASS
    decision_phases_1_to_9: PASS
    live_dynamic_growth: PASS
    ledger_delta_scale: PASS
    formation_threshold_static_reachability: PASS
    exact_eleven_orphan_rewards: PASS
    route_and_formation_structural_reachability: PASS
    focus_references: PASS
    focus_localisation: PASS
    focus_icons: PASS
    generic_military_repeatability: PASS
    maximum_three_spirits: FAIL
    visible_layout: FAIL
    state_aware_route_ai: FAIL
  layout_artifacts:
    inspect: hoi4-agent://workspace/chaos_redux/artifact/72b3df60502caef89e9f0872d2792f40f6d2886174c4de97549a044c80a55ecb/aa0bd78dfd4100f23eb4be4396d4d8b7b5369d670ac1352a864059f788162c88/focus-inspect.20e7117fcacfebfc.json
    png: hoi4-agent://workspace/chaos_redux/artifact/01d6b1ba7803c7eb6d5718de6ad204cff341540c7481a86ba570e3896f58f9ec/df86015e7172499926d5b196b3a5ae68ff8587a3984f2989c8da90e95a1e4551/utopia_manifesto_tree.focus.png
    layout_hash: 4DC9D30A7C5A153BB448531D9AEF4B1DC7150D2CE332DF940C3A58574FF484B3
~~~

## Completion decision

Do not claim the Event 15 focus tree complete from this revision. Repair FTR-RE-001 through FTR-RE-003, then rerun:

1. Maximum-spirit lifecycle tracing across every base/mitigated/failure/final temporary-liability sequence.
2. Fresh focus inspect/render metrics and human PNG review.
3. State-aware route-selection scenario checks for all five routes.
4. A short regression check of the PASS dispositions above against the new source hashes.

No fallback, placeholder, skipped route, or gameplay simplification was introduced by this audit. The audit remains incomplete by design because the source has three completion blockers.
