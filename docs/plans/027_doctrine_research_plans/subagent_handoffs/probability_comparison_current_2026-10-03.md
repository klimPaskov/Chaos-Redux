# Event 027 Doctrine Research probability comparison handoff

Date: 2026-10-03

Disposition: unresolved. This read-only audit did not obtain any exact, bounded, or sampled doctrine selection probabilities, and no probability_compare call returned a comparison ID or numeric delta.

Repository root: C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux

No gameplay, AI, event, trigger, constant, technology, doctrine, localization, spreadsheet, or index file was changed. No commit was created. The only authorized write is this handoff.

## Outcome

The prior MCP workspace handle 01a10120 was not found, so the audit used a fresh workspace, mod_chaos_redux_ea3b2d67c2c0. A later fresh SDK session initialized server version 3.6.0 and returned live schemas after an earlier stdio initialization timed out at 60 seconds. A targeted reference_search query for one installed-documentation token timed out at 30 seconds. Tool exposure was not treated as service health; only confirmed domain calls are reported below. Newer task negotiation was not established, so helper expansion, jobs, and native task routes were not invoked.

The four current AI random_list pools and their frozen baseline pools were inspected through that fresh MCP workspace. The analyzer confirmed complete source-declared pools of 5 domains, 13 Grand Doctrines, 18 tracks, and 107 subdoctrines.

The evaluator produced partial matrix and unresolved artifacts for all four pools. The scenario fixture has empty state maps, and the analyzer left 5, 13, 18, and 107 source weight inputs unresolved. No ranking, normalized share, active eligible pool, starvation result, or rank reversal is established by those outputs.

The sweeps completed as partial sensitivity passes after explicit coefficient alternatives were supplied. They produced unresolved views and no usable threshold or rank-reversal result.

The MCP comparison route returned INTERNAL_ERROR or PROBABILITY_SURFACE_EMPTY. There is no comparison ID or comparison scenario hash. The custom automatic event picker and the cluster direct-random source were not recognized as weighted blocks by the installed adapters.

No exact selection probability is claimed. Source facts, score-only traces, and unresolved probability evidence are kept separate below.

## Weighted surfaces and result models

| Surface | Source and identifier | Adapter model |
| --- | --- | --- |
| Domain choice | common/scripted_effects/027_doctrine_research_ai_effects.txt, random_list at source line 72 | Probability-proportional sampling among valid positive weights; 5 source slots |
| Grand Doctrine choice | common/scripted_effects/027_doctrine_research_ai_effects.txt, random_list at source line 201 | Probability-proportional sampling among valid positive weights; 13 source slots |
| Track choice | common/scripted_effects/027_doctrine_research_ai_effects.txt, random_list at source line 392 | Probability-proportional sampling among valid positive weights; 18 source slots |
| Subdoctrine choice | common/scripted_effects/027_doctrine_research_ai_effects.txt, random_list at source line 2069 | Probability-proportional sampling among valid positive weights; 107 source slots |
| Automatic event selection | common/scripted_effects/chaosx_settings_effects.txt, select_weighted_random_event_id | Custom cumulative weighted draw from global.all_events |
| Event 027 repeatable weight recovery | common/scripted_effects/chaosx_logic_effects.txt, update_repeatable_event_weights and on_repeatable_event_fired | Dynamic event weights with per-event caps and event-pulse recovery |
| National Breakthroughs optional member | common/scripted_effects/chaosx_event_cluster_effects.txt, prepare_event_cluster_firing and try_fire_event_cluster_for_selected_event | Direct integer rolls with eligible-count and optional-decay factors |
| Event chain structure | events/027_doctrine_research.txt, chaosx.nr27.1 | event_inspect and event_render returned partial evidence |
| Native doctrine graph structure | new_mobile_warfare | tech_inspect timed out and tech_render returned a partial graph marked sourceAccurate false |

The offline AI-mod page describes ai_will_do as a highest-sampled score race. The offline Effects page and installed effects documentation describe random_list as probability proportional to weight. Event 027 uses four random_list blocks for AI selection, not ai_will_do, event-option ai_chance, or an MTTH block.

The automatic event selector is separate from the doctrine random_lists. It samples a cumulative weighted pool only after the daily timer reaches zero. Its conditional event share is not the calendar-time chance that the event timer reaches zero.

The cluster member roll is another separate model. Optional member rows receive direct integer rolls after eligible-count and prior-optional-decay factors. It is not normalized as a random_list candidate share.

## Frozen sources and current worktree identities

The four immutable baseline copies were rehashed from their copied bytes. The scenario copy matches the source matrix byte for byte.

| Logical source | Frozen snapshot and raw SHA-256 | Current raw SHA-256 |
| --- | --- | --- |
| common/scripted_effects/027_doctrine_research_ai_effects.txt | docs/plans/027_doctrine_research_plans/probability_baseline_20261003/027_doctrine_research_ai_effects.txt, 51BFC294CFCBC08D5B0D4D28A5A2672D3CB3F897D6EC79DE6BD60F99CEEB9F3F | C969AF5E7EB0C9F0924A5BDAD8F367E4A53F248F31399302D283107141563480 |
| common/scripted_effects/027_doctrine_research_effects.txt | docs/plans/027_doctrine_research_plans/probability_baseline_20261003/027_doctrine_research_effects.txt, EC27ECF66222F4B3D779FD94912B65C155C0F7A2EA195C4D18ACACCE828A9787 | 4F9A91505FCE035DA57F135858F8786D1BD0EBFE91CAE5B978C3D8998DF3FAA4 |
| common/scripted_triggers/027_doctrine_research_triggers.txt | docs/plans/027_doctrine_research_plans/probability_baseline_20261003/027_doctrine_research_triggers.txt, CFBC55ECCD114D3C388CAD23D3CC87D8904152B032C325AF567BE1CE894B23A3 | F072DD1D70F7C8AEE0EBFC002D2967E119578AA08733FCA65806F4C6619D0A60 |
| common/script_constants/027_doctrine_research_constants.txt | docs/plans/027_doctrine_research_plans/probability_baseline_20261003/027_doctrine_research_constants.txt, D24BA6D1C77F76880BE4297F01CD848859466AC806643B29B41561376861D87A | A7B5AF2152B80855571C18A3607916A6068F71924593604E4A5DEDAE809E8724 |

The separate frozen cluster sources are docs/plans/027_doctrine_research_plans/probability_cluster_baseline_20261003/chaosx_event_cluster_effects.txt, SHA-256 D8211DA66BB429A5C00D2C51EEFDC462D36D8A210BDE1BC3DF2D66F8DC25BDC2, and docs/plans/027_doctrine_research_plans/probability_cluster_baseline_20261003/event_cluster_constants.txt, SHA-256 E74A71FA4612452F80DFB651D762B39EB5AD6DD7EB41A3D08FA1FA5E741D349F.

Other current weighted dependencies are common/scripted_effects/chaosx_settings_effects.txt, SHA-256 34C5695EA3F125DC3336E9F796B1D3A418CB1663C9FCE6D01A3B177904A50252; common/scripted_effects/chaosx_logic_effects.txt, SHA-256 C28EE6EAB4A2CEEA866C81CFFD6488E04A0B9D9ED509F650CFDDCC3F49B7548E; common/scripted_effects/chaosx_event_cluster_effects.txt, SHA-256 589D0AF4E736B62C234B438FCA3922893E48D3C520F3E93ACB4C6FB3C895EF41; common/script_constants/event_system_constants.txt, SHA-256 36EC922AC2E290A15227CC1E65C4CC6E2575E60B3E9C68D2C9BE0E5B0E45D79C; common/script_constants/event_cluster_constants.txt, SHA-256 C76988B9618E0D2EDDBDDA275DDF8A910613129061DCA335EEECB59C457625F7; common/on_actions/chaosx_on_actions_system.txt, SHA-256 CC7708D49F8056310A011041F21C9EB648B7537C5993CEF4F6FFE8F01D015F24; and events/027_doctrine_research.txt, SHA-256 777149623BF633FC07C04CF4F7F747A208024D2AFEE00D6E7120AE4BF9E01751.

The source matrix docs/specs/027_doctrine_research_specs/027_doctrine_research_probability_scenarios.md and the frozen copy have SHA-256 234B41494CB8AAA0929D88B36CB311D6F01CCC43C3E71EC48B3D49D7CFC45783. The prior IDs-only 37-scenario route-probe JSON has SHA-256 DFD69BB173F69F2EB81FB82E1A5E09DB7AF44CC74553BDC91D9749DA0F4EC255. That JSON deliberately has state:{} for every scenario. Its hash is not an analyzer scenario hash and it is not a complete native-input fixture.

## Source inspection evidence

All current and baseline AI inspections used workspace mod_chaos_redux_ea3b2d67c2c0 and the random_list adapter. The successful source selectors used candidate source locations because function names did not match the MCP candidate index.

| Pool | Current candidate source locations | Frozen baseline source locations | MCP counts |
| --- | --- | --- | --- |
| Domain | common/scripted_effects/027_doctrine_research_ai_effects.txt:72.entry.2 through entry.6 | baseline snapshot line 19, entry.2 through entry.6 | 5 candidates, poolComplete true, 5 required weight inputs |
| Grand Doctrine | common/scripted_effects/027_doctrine_research_ai_effects.txt:201.entry.2 through entry.14 | baseline snapshot line 147, entry.2 through entry.14 | 13 candidates, poolComplete true, 13 required weight inputs |
| Track | common/scripted_effects/027_doctrine_research_ai_effects.txt:392.entry.2 through entry.19 | baseline snapshot line 328, entry.2 through entry.19 | 18 candidates, poolComplete true, 18 required weight inputs |
| Subdoctrine | common/scripted_effects/027_doctrine_research_ai_effects.txt:2069.entry.2 through entry.108 | baseline snapshot line 2005, entry.2 through entry.108 | 107 candidates, poolComplete true, 107 required weight inputs |

The four required input groups are doctrine_research_ai_score_army, doctrine_research_ai_score_navy, doctrine_research_ai_score_air, doctrine_research_ai_score_special_forces, and doctrine_research_ai_score_chaos_warfare; doctrine_research_ai_grand_weight_0 through doctrine_research_ai_grand_weight_12; doctrine_research_ai_track_weight_0 through doctrine_research_ai_track_weight_17; and doctrine_research_ai_subdoc_weight_0 through doctrine_research_ai_subdoc_weight_106.
Current AI inspection source revisions are a68f1f7e8af56d6171212c927614c13e9154d7481b1ee394ac26b212f222b897 for domain, Grand Doctrine, and track, and 10954a186366f77dd5b8646ff6f274225b6710d460d42b6184c3b5a13fdcca25 for subdoctrines. The MCP canonical source hash for those current AI queries is d5a10569ce96d86c1a3e97d5b6da95088d0bbb5a6bbb2f08af910b637a3a4635. The four baseline inspections share source revision 0bd36bd237a98059d986e3956f4d7b45872c9ca994cd5b5e568fd8c354c7cc1e and MCP canonical source hash 14401e671c38193712489d69fe5c8199dcd0244537ad47aa3a550457f1086dea.
The inspect artifacts are preserved here:
- Current domain: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/830880cf5f0fa0e709958121b2da4bb39f405cc1bc8a6c07b2621efe66cbabc9/78824f7011b1613e343b5831846f3c75cf404ec220ea7ebcd5631254b771e634/probability-inspect-d5a10569ce96.json
- Current Grand Doctrine: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8f8df4e75b66d4fdb973f3200ffccd9ddb0d66091e44e5197fe2b5617afdb6b/e1cb1d9389e367f5983fb554548d3910681ef566051047b1c8d9984ca0f143ab/probability-inspect-d5a10569ce96.json
- Current track: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be17bbafe1cb42de1cc34a9c01a58787db411a0c0e8bc1ee70c3cbfe4ebe57e9/3b19c8a8786bacf8f5a4aa8aed25b5ca456429a816f82d6989fb790f1db8d390/probability-inspect-d5a10569ce96.json
- Current subdoctrine: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd229d4a857b871ab2359b673adb53734237c5d092a7627ebf605d24b25c15d8/96c08b282fae7ecabc8db7e34fd01dd56b0fd6e6ff839c361d42a7b1cbde4d08/probability-inspect-d5a10569ce96.json
- Frozen domain: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f86f509956afd7269b259a8af207bfc8564297b9dba079be3cb70ab7f30ad48/ee68e99aedce4519b6704dbaa87224f352f6e677dbc9ad1ee90368db7fa78f6c/probability-inspect-14401e671c38.json
- Frozen Grand Doctrine: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44d5bd395149815e1bddf3a384a9d899d3dc88ea17746ec2e8a806bcd2e17599/b19ab9cbdb76a3166a26af0e070ebef3ed67bfc7db3023b483afb338c3592595/probability-inspect-14401e671c38.json
- Frozen track: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6986ae0fb0ef82430b3a626c1cf69f71a4f41ee65d35e74dc7d71224d5f9a154/133c463a310bba786efe6244b2a1679402218194f53c27e6e5ec7529c9e90a07/probability-inspect-14401e671c38.json
- Frozen subdoctrine: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a71ba3438915ffca5a70bc85e5b4f7073047528ca674f62ef9b3d7df4d720838/008c7c38a0b2e5938083083faa0e57cb0ebe13077e65bfec272a7c2a6ff76916/probability-inspect-14401e671c38.json

The MCP only enumerated the static random_list slots. It did not resolve the active positive weights or scenario-dependent eligibility. Those weights are generated inside scripted effects and returned as required input paths.

## Modifier and score-only trace

The frozen and current doctrine_research_ai_weight values are identical.

| Constant | Value |
| --- | ---: |
| base | 1 |
| forces | 2 |
| production | 2 |
| war | 2 |
| geography | 2 |
| theater | 2 |
| strategy | 2 |
| completion | 3 |
| owner_readiness | 3 |
| continuity | 2 |

Domain, Grand Doctrine, track, and subdoctrine weights initialize to zero and populate only inside their validity or action gates. Each valid candidate starts from base 1. Conditional source terms add weight for force templates or units, factories, war, coast or terrain, faction membership, strategy signals, completion state, and owner-system readiness. These are score-only traces, not ranked scenario results.

Domain completion now scans actual eligible assigned tracks, checks their current/max levels through doctrine_research_prepare_track_display, and adds the completion weight only for an active incomplete track one level from its maximum. The source supports People’s War maximum level 4 and the other track maximum level 5. The selector saves and restores domain, Grand Doctrine, track, and subdoctrine selections while it calculates domain scores.

The track scorer adds same-batch continuity only when the prior transaction batch matches the active batch and the domain and track match. Its near-completion bonus is completion 3 when the current track level is above zero, incomplete, and next level reaches the displayed maximum. That bonus is not conditional on force or strategy relevance.

All 107 subdoctrine score blocks now guard previous-choice continuity on last transaction batch, Grand Doctrine, track, and subdoctrine matching the current choice. The existing selected-domain and selected-track guards are still present. The source scan found 107 of 107 matching continuity guards. Eight native subdoctrine identities are reused across distinct Special Forces track slots. No duplicate domain, track, and identity triple appears in the 107 static slots. The trigger requires the selected subdoctrine to belong to the selected Special Forces track and excludes a simultaneous opposite-track assignment, but live candidate overlap was not tested by MCP.

The existing native investment check at mastery amount 1 remains unchanged and distinct from previous-choice continuity. The previous-choice continuity coefficient remains 2, with the new same-batch, same-Grand-Doctrine, same-track, and same-subdoctrine guards. The completion signal uses mastery level 4 for ordinary branches and level 3 for People's War. The coefficient values did not change.

The AI helper output lifetime patch is source-verified. The AI domain chooser predeclares all five score outputs, the Grand and track choosers predeclare candidate_score, doctrine_research_ai_pick_choice predeclares the three found flags, and doctrine_research_ai_resolve_active_batch predeclares transaction_success before doctrine_research_confirm_selection. doctrine_research_ai_score_domains predeclares domain_completion_found before the progress helper and saves/restores the selection fields.

The current source also predeclares helper outputs at the call sites: the five domain scores before the domain scorer (AI effects lines 63-70); candidate_score before Grand and track candidate scoring (lines 106 and 262, with the shared scorer at lines 82 and 219); grand_found, track_found, and subdoctrine_found before the chooser calls (doctrine effects lines 2868-2873); and transaction_success before confirmation in the active-batch resolver (lines 2890-2900). The domain score router initializes domain_completion_found before the progress helper and restores the saved domain, Grand Doctrine, track, and subdoctrine selections (lines 2781-2790 and the remainder of that helper). This is source-verified, not proof of exact engine temporary-variable lifetime semantics.

The offline Data structures page says temporary variables first created inside a scripted effect or trigger may not survive the helper return, while caller-preinitialized storage is preserved. The source follows that pattern. This supports a source-level correction of possible false-zero outputs, but it is not live engine proof; exact engine behavior remains unverified and the specialist architecture source audit is in progress as separate source evidence, not MCP equivalence. No game was launched.

## Validity, dominance, starvation, and repetition findings

The current source initializes the fixed AI random_list weights to zero, then calculates a weight only after the corresponding validity or action trigger passes. No positive weight on a statically invalid fixed candidate was identified. MCP did not validate live eligibility or the malformed-adapter injection in DR-G03.

Navy adoption is valid whenever the country has no naval Grand Doctrine. doctrine_research_navy_adoption_available has no coast, ship, dockyard, or readiness gate. A valid landlocked country can therefore receive the positive base weight and generic war or faction modifiers. This is not proof that Navy wins often.

The Navy strategy and owner-readiness signals recognize existing naval doctrines, ships, convoys, naval factories, and coastal access. They contain no current-and-valid future maritime plan signal. DR-A05 therefore has no explicit planned-route factor in the inspected source.

Army and Special Forces domain choices receive the owner_readiness coefficient whenever their domain has a valid action. Navy, Air, and Chaos Warfare receive that term conditionally through readiness triggers. The strength of this asymmetry and any resulting dominance remain unresolved.

Completion can add 3 without checking strategic relevance, while relevant force-fit signals add 2. DR-C02’s intended reversal between a relevant land branch and an irrelevant near-complete naval branch remains unresolved. The new completion condition now reflects actual progress, but its strategic preference still needs the named scenario comparison.

The always-no doctrine_research_empty_track_is_verified gate prevents assignment to an empty track and prevents a first empty-subdoctrine selection. This is the accepted engine-safety restriction while native assignment and banked-mastery evidence is absent. It blocks the source path needed by DR-C03 and DR-C07 and can block the second choice in DR-E01 after adopting a fresh Grand Doctrine. DR-E04 also depends on a fresh branch when no assigned track is available. Existing assigned mastery and Grand Doctrine adoption remain valid.

The source recomputes doctrine_research_ai_pick_choice in each active-batch loop iteration after confirming a choice. This is a source trace for reevaluation after each choice. It does not prove native mastery, queue timing, or batch transitions, and no sequence result was produced.

Previous-choice continuity now rewards only the same branch in the same active batch. The independent mastery-level-1 investment signal and the near-completion signal remain. Repeated selection, specialization snowball, and starvation across multi-choice batches remain unresolved because all scenario weights are unresolved.

The 107 subdoctrine source entries include repeated token names across different Special Forces track contexts, but the exact same token is not duplicated under the same domain and track. Current gates make the track context mutually exclusive. MCP confirmed 107 source slots, not the live active pool.

## Event 027 automatic picker and timing

The daily event timer sets random_event_selection_filter to settings_event_filter.all before select_weighted_random_event_id. global.all_events is built from 9 major, 36 fire-once, and 51 repeatable registration entries. Resolving the thirteen constant-backed IDs gives 96 unique registered IDs in total. The actual active positive pool is smaller and dynamic because event enablement, event type, prior firing, Chaos requirements, event availability, event weights, caps, and other gates apply.

The scenario matrix DR-F01 through DR-F03 expects the complete repeatable-event pool. That is not the actual automatic selector’s filter. The automatic timer selects across the all-events pool, so the matrix does not bind the complete source pool used by the timer.

The custom picker reads each active event weight, multiplies by 100, rounds, sums the scaled weights, draws an integer from minimum 1 to maximum total_weight_scaled, then selects the first cumulative weight greater than or equal to the roll. The installed effects documentation describes set_variable_to_random as using the half-open interval [min,max). The upper cumulative endpoint is therefore not in the documented draw range. This is an exact source and documentation boundary mismatch, not an analyzer-confirmed selection percentage. If the final active candidate has a scaled weight of one, the current draw can leave it with no reachable roll. The impact on Event 027 depends on the dynamic candidate order and weights and remains unquantified.

The source defaults event weight to 1000, reduces the firing event cap by factor 0.5, and uses recovery rate 20. on_repeatable_event_fired clears the weight, then ordinary minor-event pacing immediately runs the repeatable recovery updater. Cluster-member firing sets the event weight floor to 1 without running that global pacing update. update_repeatable_event_weights is called by minor and major event pacing handlers. No monthly weight-recovery hook was found. DR-F02’s stated monthly recovery schedule does not match this event-pulse source cadence.

Event 027 has no ai_will_do, ai_chance, mean_time_to_happen, or mtth: construct in its root or the four weighted chooser sources. Its automatic selection share is conditional on the shared timer reaching zero. No calendar-time firing distribution is available.

## Cluster 9 and direct-random sequence

The current National Breakthroughs cluster uses ID 9 and has one runtime member row, 9001. That row is Event 027, optional, Medium severity, minimum Chaos tier 0, and primary_trigger=yes. The frozen cluster source has no cluster 9 branch. The other planned member IDs 54, 65, 67, 83, 85, and 89 are still absent from the current loader.

The row’s Calm override is a minimum-tier override to tier 0. It is not a participation chance of zero. The generic participation matrix is text-identical to the frozen copy, with calm_medium=35. An optional, non-triggered Event 027 row therefore starts from the 35 source base chance before the eligible-count factor, optional-decay factor, rounding, and clamp. Its final chance depends on the complete optional-member pool and current state, neither of which was supplied.

Source flow for DR-F05 prevents a second Event 027 fanout. fire_event_by_temp_id calls try_fire_event_cluster_for_selected_event before the no-cluster dispatcher. The primary trigger row is marked guaranteed, excluded from the optional-member roll order, dispatched synchronously as the first firing-order row, and omitted from delayed queueing by queue_start_index=1. This is exact source flow, not a probability or live-engine result.

DR-F04 requires a different cluster member to be selected while Event 027 remains eligible. The current National Breakthroughs loader contains only row 9001 for Event 027, so the required other-member case cannot be constructed from the current pool. The current cluster’s total-size distribution is unresolved.

The direct_random inspector returned no weighted surfaces for the cluster source, and direct_random evaluation returned PROBABILITY_SURFACE_EMPTY. No exact cluster activation or optional-member probability was produced.

## Scenario matrix coverage

Every named case below was submitted to the matching AI evaluator when a source-backed pool existed. The fixture provides qualitative conditions only. Its state maps are empty, so country identity, date, actor scope, typed state and controller bindings, numeric force and production values, AI-plan identifiers, DLC matrix, current doctrine and mastery values, and batch states are absent.

| Group and named scenarios | Evaluated surface | Source-pool completeness | External-factor completeness and result |
| --- | --- | --- | --- |
| A: DR-A01 Doctrine-less land major; DR-A02 Island naval power; DR-A03 Air-centered continental power; DR-A04 Landlocked small minor; DR-A05 Future maritime plan; DR-A06 All ordinary domains complete | Domain | Complete source list of 5 | State, force, industry, strategy, and dates are qualitative only. Unresolved |
| B: DR-B01 Mobile armored army; DR-B02 Manpower-rich infantry state; DR-B03 Doctrine plan conflict; DR-B04 Invalid doctrine candidate | Grand Doctrine | Complete source list of 13 | Active graph, force composition, historical plan, DLC, and invalid candidate state are not bound. Unresolved |
| C: DR-C01 Near-complete relevant branch; DR-C02 Near-complete irrelevant branch; DR-C03 Empty track fills missing capability; DR-C04 Four equal tracks; DR-C05 One dominant track; DR-C06 Branch completes between choices; DR-C07 Banked mastery on empty track | Track and subdoctrine | Complete source lists of 18 and 107 | Branch levels, readiness, weights, seed, DLC, and native mastery timing are not bound. C03 and C07 also meet the current always-no empty-track gate. Unresolved |
| D: DR-D01 CBRN-ready Chaos Warfare country; DR-D02 CBRN-unready ordinary country; DR-D03 Active Chaos Warfare, infantry-heavy formations; DR-D04 Active Chaos Warfare, theater command need; DR-D05 Special nonhuman country without adapter; DR-D06 Special country with valid adapter | Domain, Grand Doctrine, track, and subdoctrine as relevant | Complete fixed source lists | CBRN prerequisites, equipment and units, country classification, adapter identity, DLC, and current branch state are not bound. Unresolved |
| E: DR-E01 Evolution I adoption sequence; DR-E02 Evolution II mixed services; DR-E03 Evolution III broad curriculum; DR-E04 Evolution IV branch completion; DR-E05 Queue with different stages; DR-E06 Evolution unlock during batch | Track and subdoctrine choice passes | Complete source lists of 18 and 107 | E01 to E04 were evaluated as single-choice pools. E05 and E06 were submitted as two-scenario single-choice probes. No batch timeline, scheduled transitions, native mastery sequence, or terminal state was bound. Unresolved |
| F: DR-F01 Initial event pool; DR-F02 After first firing; DR-F03 Sequence through four firings | Automatic event picker and repeatable-event recovery | 96 unique registered event IDs were source-enumerated. The MCP custom-pool adapter returned poolComplete=false and no candidates. | Actual automatic filter is all, not repeatable-only. Dynamic eligibility, active weights, caps, timer, event-pulse schedule, and reset state are absent. MCP evaluation returned PROBABILITY_SURFACE_EMPTY. Unresolved |
| F: DR-F04 Event 027 optional cluster member; DR-F05 Event 027 selected cluster member | Cluster trigger and optional direct random | One current row, 9001. Other-member coverage is incomplete. | F04’s other selected member is not registered. F05 activation and optional-member states are unbound. Direct-random MCP evaluation returned PROBABILITY_SURFACE_EMPTY. Unresolved |
| G: DR-G01 Human and AI pool parity; DR-G02 DLC matrix; DR-G03 Invalid adapter injection | Domain, Grand Doctrine, track, and subdoctrine validity | Complete fixed source lists | Human-valid actions, DLC combinations, injected adapter identity, and live native availability are not bound. Unresolved |

The scenario matrix source is docs/specs/027_doctrine_research_specs/027_doctrine_research_probability_scenarios.md. The exact named IDs are present in the frozen matrix copy and the 37-case source JSON. The file hash of the 37-case empty-state JSON is not an MCP analysis hash.

## Probability evaluation artifacts

All four source-backed doctrine pools were submitted to probability_evaluate with their named scenario subsets. Each result was PROBABILITY_ANALYZED_PARTIAL. The reports show 65, 130, 288, and 1,926 candidate rows, but those are source-slot rows; they do not establish the live active candidate count. Every required score input in the relevant pool remained unresolved. No displayed row ranking or percentage is treated as a result.

| Surface and scenario IDs | Analysis ID | Scenario hash | Source revision | Rows; unresolved inputs |
| --- | --- | --- | --- | --- |
| Domain: DR-A01-A06, DR-D01, DR-D02, DR-D05, DR-D06, DR-G01-G03 | probability-6833e9259d76ac55a8c80b31 | 29c96508889a1fadce4bf71f1ae16a8f5b7f57c6e90802e6cdb7195c4e5b585f | 745457280d2945243dd766785fa8e951bc1645d5e5d9d3dfb8e8a8443c368e42 | 65; 5 unresolved weights |
| Grand Doctrine: DR-B01-B04, DR-D01, DR-D02, DR-D05, DR-D06, DR-G02-G03 | probability-35b536e3bf4a24cbae384546 | e380942c5ea60b98bdd94749860fc63d60fd97d9ab9796f3d38ccbee827a6f28 | 745457280d2945243dd766785fa8e951bc1645d5e5d9d3dfb8e8a8443c368e42 | 130; 13 unresolved weights |
| Track: DR-C01-C07, DR-D03-D04, DR-E01-E04, DR-G01-G03 | probability-af6eb2ef863f6ee7e4c23c08 | bc3864c06a15f1f5252c3ad15a1d11309e9e15fb9cd9acb499aa10ca37cffb95 | 745457280d2945243dd766785fa8e951bc1645d5e5d9d3dfb8e8a8443c368e42 | 288; 18 unresolved weights |
| Subdoctrine: DR-C01-C07, DR-D03-D06, DR-E01-E04, DR-G01-G03 | probability-b7832726cd3abe829fdc170c | 51885269efa160c6d41a5bb8ec3488ed2d078c91c2e78b001f05b7fa391f7eff | a68f1f7e8af56d6171212c927614c13e9154d7481b1ee394ac26b212f222b897 | 1,926; 107 unresolved weights |

The two evolution queue probes were separate, two-scenario, single-choice evaluations and did not model a batch sequence or scheduled state transitions:

- DR-E05 and DR-E06 track probe: analysisId probability-131000e13de1c3bf02758c47, scenarioHash 211e82cb1d0c3c2f67058df08ec6471c20d3fd4f3a664da32e86ee8e784f0bc3, sourceRevision 711e7b9930941946a0457b83afd4406d5e89c9461ce4b973b20bf5a9ad8b5cb4, 36 rows, 18 unresolved weights. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9e4fa37a0c892aa417d68d579966a1808cb1a6c66d85108bc322acec3605206/bada9ef0da2815955d7ec27a3bfef14722493ea45677e1eeb74cf4bbe539288b/probability-131000e13de1c3bf02758c47.json.
- DR-E05 and DR-E06 subdoctrine probe: analysisId probability-d339062615db523b5f120942, the same scenarioHash and sourceRevision, 214 rows, 107 unresolved weights. JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d3400927e60052f1b4b22ebeec030d90c00c582ddb20226c05ca4375c374e7c/152796d4ed40f6ca631020d1e884acb5c7c740294d0cd63b970c5698f2d4c43625/probability-d339062615db523b5f120942.json.

The returned render artifacts provide matrix and unresolved views for the four main analyses:

- Domain JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/232c6ac9915505a37714c4c615ed003fd968b2a63d51c2c07550c696a6dea3a4/9eb6c3d1bb36ff377bc7e23f7d809f5a590e95fbb3acb5ae5a008c3bd36dbb65/probability-6833e9259d76ac55a8c80b31.json; matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7466ca13d515ee4edf02f75e55af43d276e1f7b85b113b49886a7ec891930663/ca2c57142e586bc6ed32198da324164f37ae0818afc45d008a284198c92e82bf/probability-probability-6833e9259d76ac55a8c80b31-matrix.svg; unresolved: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2f9aa7b978700a5160d30df0c31cbf192ad6cffa149af59c7e1ea6bbf681253/a38861d703eee186ed4efb36f28d96dd8251403bbd498a0fefd57e05b282e842/probability-probability-6833e9259d76ac55a8c80b31-unresolved.svg.
- Grand Doctrine JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5f84c78fa5e9422ccba93fe643ea4044244de5fe125ee482baee0460ddd2a9d/817cbab12e81b447ad7da749e152b660e15c41aa421d2521b0543d3721ae304d/probability-35b536e3bf4a24cbae384546.json; matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/679c499c52a2f38ba89e38e832561750ccf7d4e5974e58e5e15d6e5337ecbf34/7ac35c13a38eb414b4ded2051f83115c9ba2c975f3d4ae6f01de6adf911903aa/probability-probability-35b536e3bf4a24cbae384546-matrix.svg; unresolved: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c30f7196f94bc96e28173ac382fe55633f999184faf94e750de70f17778751da/d03004a9ab982f4aad72f0431ffe96dd8251403bbd498a0fefd57e05b282e842/probability-probability-35b536e3bf4a24cbae384546-unresolved.svg.
- Track JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ec5bd90d58fe28998b19d27824786c4cd3d46323f16b94b563e59522aa7d41e/a62cfdde8cc33a7ac25839afca5e62127e7d606eea5861d81c06723376684ee3/probability-af6eb2ef863f6ee7e4c23c08.json; matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/734556f12325f9a4610d44bc34106bac19d0f09c2948c4a7ac8377d45e1feffb/043c88e3b0c5d81b4148fc395050e5f6eb7e5ca8a89eeec4926bde070ff22aed/probability-probability-af6eb2ef863f6ee7e4c23c08-matrix.svg; unresolved: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d009a4eafb5a300059dedf555c58577b92e02bed1aa9308b8ff75987f970fdfa/ea50f971b43d7f1e6dd35d802e4b48696bbce3317ebc99985b1d418cafcc2ec0/probability-probability-af6eb2ef863f6ee7e4c23c08-unresolved.svg.
- Subdoctrine JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a73f3997f0d9034ecc71ee9e43387e35104d390e5cda89c708aafea83f0e072/57db29ad1a60c37901250adb29f40036400908bd8d89d9a25b2d43f63b664156/probability-b7832726cd3abe829fdc170c.json; matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3ec0d55a6b2b6f69caa0822e32c05788ec261a27d3f9403ab9ab1021b966ff49/69b2ed935e185fa947a5aeb77e0f1704ecd66aa65e5329af32f1bc970c878d02/probability-probability-b7832726cd3abe829fdc170c-matrix.svg; unresolved: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b6fad83455fc2aa785c8167eeeef214363ebabf9df4b8796a3d7136c5a63b3c/722c71e8a5e325350504ea05864f76097daa534274d5bb11ecf90905e876dbfd/probability-probability-b7832726cd3abe829fdc170c-unresolved.svg.

## Sensitivity sweeps

The first sweep attempt stopped with PROBABILITY_SWEEP_RANGE_REQUIRED because the qualitative scenario fixture did not define numeric alternatives. Four follow-up sweeps declared coefficient alternatives centered on current source values. These are sensitivity probes, not proposed tuning targets.

| Surface | Declared coefficient alternatives | Scenarios | Sweep result |
| --- | --- | --- | --- |
| Domain | base 0, 1, 2; owner_readiness 2, 3, 4; completion 2, 3, 4 | 13 A, D, and G cases | 351 points, 5 unresolved score inputs |
| Grand Doctrine | forces 1, 2, 3; strategy 1, 2, 3; owner_readiness 2, 3, 4; completion 2, 3, 4 | 10 B, D, and G cases | 540 points, 13 unresolved score inputs |
| Track | completion 2, 3, 4; continuity 1, 2, 3; forces 1, 2, 3 | 16 C, D, E01 to E04, and G cases | 432 points, 18 unresolved score inputs |
| Subdoctrine | continuity 0, 2, 4; completion 1, 3, 5 | 18 C, D, E01 to E04, and G cases | 162 points, 107 unresolved score inputs |

All sweeps returned PROBABILITY_ANALYZED_PARTIAL and emitted sensitivity, threshold, and unresolved views. No numeric ranking, rank reversal, dominance threshold, or starvation threshold was exposed in the structured results. These sweeps cannot be used as a balance conclusion while the weights and external state remain unresolved.

The sweep analysis IDs and scenario hashes are:
- Domain: analysisId probability-ceb57cc1744234904898e02c, scenarioHash 56c844cdc8d1d0caf8a7130c21d37bfe74806b4fd38b4fbee9829695e768def9, sourceRevision 55bc3d95d948fdd56323030106d50a893b4d92647d31ac87b766e523b4ece51e.
- Grand Doctrine: analysisId probability-e7fadd3d63314f7709e64537, scenarioHash 98b5289f4605162ac120bdf62c260da8f85f00aa4b679fc4425ae880bf0e9295, sourceRevision 55bc3d95d948fdd56323030106d50a893b4d92647d31ac87b766e523b4ece51e.
- Track: analysisId probability-2c912724b4a971b306c04536, scenarioHash 438029fd08eef4b094cab462b1bb9ec2b48e377b6ec33c4eaaeb59a191329742, sourceRevision 55bc3d95d948fdd56323030106d50a893b4d92647d31ac87b766e523b4ece51e.
- Subdoctrine: analysisId probability-e2a9000df271ef64b49ccce4, scenarioHash e4e1245c0d620f960bbd5ae64da36d0a42d4a1c9665436a3be375298b90933c7, sourceRevision 55bc3d95d948fdd56323030106d50a893b4d92647d31ac87b766e523b4ece51e.

The main sweep JSON URIs are:
- Domain: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/97e277eba946f92796da646a242b00708a420da14829a444e770339ef2a9c40e/2dfb1f49f1d58a98f48c698f5444a0d10f4ca3a25f42796c45d7b14567daa574/probability-ceb57cc1744234904898e02c.json
- Grand Doctrine: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7580b864f6064e983c2711f725fe795350a2c7cb59fa9c57eb6fc3ba845e448e/7c4365eba43abfe712112c24a25dd8355518a59d5da54c51bad389833807cc6d/probability-e7fadd3d63314f7709e64537.json
- Track: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07cd5d37de724a3d5d6ea0305699b166e8ffd1897c771b65ec735f82792d11b1/4c353051ec9e0651e105aa68b9062303aa4cc07001f2ceb1511a46b8c98766fd/probability-2c912724b4a971b306c04536.json
- Subdoctrine: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b9433762d88fddca6f71433fec56892ed0b1b31c480e93141d8a70831ab2109/c9b41f69adcfcf473d6b6899a943700c3311cc5d9c7087e6c9c9683641eb8a79/probability-e2a9000df271ef64b49ccce4.json

Representative rendered sensitivity and unresolved URIs are:
- Domain sensitivity: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/210ab4bf09ef5ad141b9a9f5f62f36591564392bbcab4570f30b777868c8f96a/7b25be653096649256da614a281cc44f040cab45e1d4d9d2ac7c5867a5d4a8f3/probability-probability-ceb57cc1744234904898e02c-sensitivity.svg
- Grand sensitivity: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d615cf72c1ecabf54c18ac673fbbe43afd5eb9ba227674a1064afa7fd5c3c8d9/14da0276cd20a110cf50014ea18dd2622fa0c7dc0c72dc6289ce20a02dd0c7cd/probability-probability-e7fadd3d63314f7709e64537-sensitivity.svg
- Track sensitivity: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/409e3b356824533be5e314900daa35f204495d6e37f18542e09c8e9b97ae5ad9/0697389a35e0e1d652150cbcc2cd5530b57a55a17b81988e303adb38ab731c7e/probability-probability-2c912724b4a971b306c04536-sensitivity.svg
- Subdoctrine sensitivity: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ede69f29280fe15124a343dd263ec0849128c7cd7d96f9f41b92c621f8719f17/feef8af10c08b0b3db5b12ed27933fe5d20c593fcee01a0a0adda557e0eeaf98/probability-probability-e2a9000df271ef64b49ccce4-sensitivity.svg
- Shared unresolved view: the corresponding unresolved.svg resources are returned alongside each listed JSON artifact. Each report is identified by its analysisId and scenarioHash above.

## Comparison attempts and exact blockers

The correct source snapshot selector shape was used for the frozen AI-effects bytes: logical path, snapshotPath, and lowercase expectedSourceHash. The after selector used the current logical path and lowercase expectedSourceHash. The same 37-case scenarioSet was submitted in the fresh workspace.

A full 37-scenario random_list comparison returned INTERNAL_ERROR with message Unexpected internal error, no comparison ID, no scenario hash, and no artifact. A second comparison over the 18 subdoctrine scenarios returned the same error.

A narrower DR-C01 comparison with the full 107 current source-location candidates returned PROBABILITY_SURFACE_EMPTY with message No weighted blocks matched this request. The MCP did not produce a score or selection delta.

A cluster direct_random comparison bound the frozen cluster effects snapshot hash D8211DA66BB429A5C00D2C51EEFDC462D36D8A210BDE1BC3DF2D66F8DC25BDC2 to current effects hash 589D0AF4E736B62C234B438FCA3922893E48D3C520F3E93ACB4C6FB3C895EF41 and scenarios DR-F04 and DR-F05. It returned PROBABILITY_SURFACE_EMPTY because the direct_random adapter matched no weighted blocks. An initial request had a duplicated snapshot folder component and was rejected as PROBABILITY_SNAPSHOT_NOT_FOUND. The corrected request still produced no probability comparison.

The automatic picker and cluster direct-random surfaces have no successful probability_compare result. No current file was compared to itself. No numeric before-and-after delta is claimed.

## Automatic event selection and cluster findings

The timer sets settings_event_filter.all and calls select_weighted_random_event_id. initialize_event_categories registers 9 major, 36 fire-once, and 51 repeatable entries. Resolving the thirteen event-ID constants against their definitions yields 96 unique IDs. This is the full static registration pool, not the active positive candidate set.

The MCP custom_weighted_pool inspection of common/scripted_effects/chaosx_settings_effects.txt returned candidates 0 and poolComplete false. The direct_random inspector returned no weighted surfaces. Evaluation with all 96 source IDs returned PROBABILITY_SURFACE_EMPTY. The adapter cannot currently produce a normalized event share from this custom selector.

The event selector source multiplies each weight by 100 and rounds it. It draws from minimum 1 to maximum total_weight_scaled. Installed vanilla documentation states the upper bound is exclusive. The cumulative scan includes the final boundary, which the configured random range cannot draw. This leaves a source-level risk to the last active candidate. Its effect on Event 027 is unquantified and has no MCP probability result.

Default event weight and cap are 1000, the repeatable cap reduction factor is 0.5, and recovery rate is 20. Recovery is event-pulse driven from minor and major pacing handlers. It is not scheduled monthly in the inspected source. Event 027’s custom root has no MTTH entry. The automatic selection share is conditional on the event timer reaching zero.

National Breakthroughs is cluster ID 9 and the current loader has only optional row 9001 for Event 027. The row is Medium severity, has effective minimum tier 0, and is a primary trigger. The generic participation matrix is unchanged from the frozen cluster constants and calm_medium is 35. The 35 source value is a base chance only. The final chance also depends on eligible member count and optional-decay state.

The cluster source flow excludes a matching trigger row from the optional roll order, dispatches the trigger synchronously first, and starts the delayed queue at index 1. This is source-level exactly-once evidence for DR-F05. The MCP direct_random adapter did not recognize the code, so no activation or member probability was measured.

## Findings by risk category

- Invalid fixed candidates are zero-initialized and scored only within their validity gates. No positive weight on a source-statically invalid fixed candidate was found.
- Live eligibility, DLC coverage, target validity, human and AI pool parity, and invalid-adapter injection remain unresolved.
- Navy adoption has a positive base weight whenever no naval Grand Doctrine exists, even without coastline, dockyards, ships, or a future maritime plan.
- The Navy strategy and readiness triggers detect existing doctrines, fleets, convoys, naval factories, or coast. They do not detect a planned route to naval expansion.
- The Army and Special Forces domain scores get owner_readiness unconditionally after their valid-action gate. Navy, Air, and Chaos Warfare require condition-specific readiness signals. The dominance effect is unresolved.
- Near-completion receives the completion coefficient 3 without a strategic-fit check. DR-C02 may reverse the expected relevant-land versus irrelevant-near-complete ordering. No rank result was returned.
- Same-branch continuity is now exact to one batch, one Grand Doctrine, one track, and one subdoctrine. The separate native mastery investment bonus and near-completion bonus remain, so repeat selection and snowball risk are not eliminated by the continuity guard alone.
- Empty-track safety is always false while engine proof for assignment and banked mastery is absent. DR-C03, DR-C07, and fresh-track portions of DR-E01 and DR-E04 cannot be satisfied by the current source path.
- The 107 source slots have 99 unique doctrine tokens. Eight tokens repeat across separate Special Forces track slots. No same-domain, same-track, same-token duplicate was found. Current gates make the selected Special Forces track exclusive, but MCP did not validate live overlap.
- Repeat frequency, timing drift, starvation from event caps, AI dominance, and a campaign snowball rate remain unresolved because no complete active pool, timing fixture, or sequence result is available.

## Recommendations for the parent

These are review recommendations only. No source change or numeric target was applied.

- Review common/scripted_effects/chaosx_settings_effects.txt, select_weighted_random_event_id, so the random draw can reach the total cumulative weight under the documented half-open range; for example, use an exclusive upper bound of total_weight_scaled + 1 if consistent with the engine field semantics. Then compare against a complete active pool through a supported MCP adapter.
- Align DR-F01 through DR-F03 with the actual settings_event_filter.all automatic pool, or confirm and implement a repeatable-only automatic selector. The current source selects from the 96-entry all-events pool.
- Update the F02 scenario cadence to the event-pulse recovery used by the shared repeatable system, or approve and implement a different schedule before analyzing that timing expectation.
- Bind concrete campaign inputs for each AI scenario, including country, date, force composition, factories, naval and air assets, strategy plans, DLC, current doctrine, mastery and completion levels, and batch state.
- Keep doctrine_research_empty_track_is_verified blocked until the required native assignment and banked-mastery proof exists. Mark the fresh-track expectations blocked while this safety gate remains always no.
- After the scenario inputs resolve, measure whether the unconditional near-completion coefficient should depend on relevance for DR-C02. Do not tune its value from this audit.
- Add the remaining National Breakthroughs member rows before evaluating DR-F04, or revise the scenario to represent the single current row. Do not invent the absent member IDs.
- Preserve the baseline and current random-list source identities for another compare attempt. The current MCP comparator did not return a comparison artifact.

## Structural MCP evidence

The valid event selector was kind event, eventId chaosx.nr27.1. event_inspect mode trace returned EVENT_INSPECTED_PARTIAL, focused mode, revision 1ffd3235991f42e15eaa3a4998d8a0505a163979929254eadeddd98644ccbf9b, graphHash 882965a23286244c6b76909811c90082dd9ecc275e48d42ceee4b60fd3a13b2e, and no helper expansion. Its inline source inventory showed 64 of 388 paths and reported MCP_INLINE_FILES_TRUNCATED. It did not establish complete helper or lifecycle coverage.

event_render produced overview and unresolved views at revision b64f37f7b84411f7bd5d43429bb4ec17e262784b7db861eae17df39e7d1c09b4, graphHash ab7e8dae0ff01835991aa59fe7c1a1c0cc6cda5b32d5feafee19955e328c0712, and layoutHash 58d45e1f8b0cfa79bc3da42fdb51edef2eaca76825d97029f7cee6cbae62c03b. The render remained partial, with two selected nodes and 42,985 omitted nodes.

- Event trace JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5581fc45c50c5059dd42a09f0769d8a76d4914bf9a24e5c0097d261cb30b1f50/c73bc17b8a891690c25c439a2cbd5977687affc7fc4c7e9c7157af929d11b2bb/event-trace-1ffd3235991f.json
- Event overview SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7517a158820d036bab36c0d7841e7003b4c9ca8a2a0cd984e5785462318c4b0/9f2704da1a16c5467f2e1a2de15adfaac14260b1e4296bed50ce1a29afd63c47/event-overview-b64f37f7b844.svg
- Event unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28b5504f811a016dc8b91031be7fe8bd6401d26516a50d41f2a5b40cba16b1a9/049e2d9f83366a314786c8f50f775b4c2314567de1f1b4258248cc6431d5c970/event-unresolved-b64f37f7b844.svg

tech_inspect trace for new_mobile_warfare timed out after 600 seconds with no artifact or revision. tech_render view doctrine returned TECH_RENDERED_PARTIAL, revision 29df0130283657c018f636093c330bc3084fe952deec8eafb18f4e9d069ab221, graphHash e21f279474bee9c065ee33951b4e2d52008bd83acdd58eaa14c7b9625ab7eb8c, sourceAccurate false, 24 selected nodes, and 539 omitted nodes. The standalone Technology Tree Viewer was not identified in the live tool catalog or installed hoi4-agent-tools 3.6.0 package. Availability outside this session was not established.

- Doctrine render JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/654facbca44479d2fca28219a4de42f1017a64d4a27e8ed81352378110727208/8eeb698ca186df5c1c8e0e39dbd87e655764e3fa2ad0fbd65f2c178b9a82c17f/technology-doctrine-29df01302836.json
- Doctrine render SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d1154daa500ecf0a5e8da4070d3d6615b1465748889d979e44242ab41a4a76c/0dbfe79291b4c2a63961db0d396cb2eeaaf3c5dcddc9e9c85ce1be914775cda8/technology-doctrine-29df01302836.svg

## MCP artifact and render limits

probability_render was called for the evaluator and sweep analysis IDs. Each call returned PROBABILITY_ANALYSIS_NOT_CACHED even when the same workspace ID and scenario hash were supplied. The evaluate and sweep responses themselves emitted matrix, sensitivity, threshold, and unresolved render artifacts, which are linked above.

The HOI4 artifact resource template was discovered. Bounded reads of probability and event artifacts failed with MCP error -32603, Artifact provenance manifest is unavailable. The structured tool summaries and artifact URIs are preserved, but the full artifact payloads could not be read.

A full custom-pool sequence analysis was skipped because no complete declared manifest includes the active candidate pool, all event-specific weights and gates, timer cadence, cap reduction, recovery, removals, reset transitions, cluster transitions, and terminal state. The AI repeated-choice source is a sequence of random_list calls, not a complete custom-pool manifest.

Seeded simulation was skipped because the scenario matrix declares no uncertain campaign-input distributions or sampling seeds, and the candidate weights remain unresolved. No live game or save was used.

## Offline reference review

The following local sources were read. The Paradox wiki was not accessed on the web.

- paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md, lines 26 through 37, SHA-256 917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818. This distinguishes ai_will_do score races from event-option probability sampling.
- paradox_wiki/Effects - Hearts of Iron 4 Wiki.md, lines 4518 through 4539, SHA-256 997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C. This documents random_list weights and proportional shares.
- paradox_wiki/Technology modding - Hearts of Iron 4 Wiki.md, lines 331 through 354, SHA-256 C5428838DB20C4C812C66AFF82CBAFC58DB3B73453C30436BCE0D97436170BEE. This separates native technology AI weighting from custom doctrine choice.
- paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md, lines 438 through 442, SHA-256 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4. This documents caller-preinitialized temporary variable outputs across scripted-helper calls.
- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md, lines 5413 through 5425 and 7842 through 7860 and 7910 through 7930, SHA-256 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF. This documents random_list selection and the half-open interval for set_variable_to_random and set_temp_variable_to_random.

The event, subagents, and event-planning skills were read. The event-planning skill informed the use of named scenario expectations and explicit missing-input declarations. No skill was created or edited.

## Completion boundary

This handoff is the only file written for the task. Gameplay and weighted source files remain unchanged by this auditor. No commit was made.

The parent can continue after resolving the MCP comparison failure and supplying scenario state values. Until then the comparison, ranking, normalized chance, timing, rank reversal, repetition, starvation, and full-sequence conclusions remain unresolved.
