# Event 027 Doctrine Research Probability Baseline Handoff

Date: 2026-10-03

Disposition: blocked. This is a read-only source audit with unresolved probability conclusions. No numeric balance target is selected or accepted.

## Scope and outcome

The requested baseline covers the 37 named scenarios in the Event 027 probability matrix and the four separate scripted AI choosers. Frozen source identity and static scoring structure were reviewed. Scenario rankings, normalized selection probabilities, timing, sensitivity, rank reversals, starvation, dominance, repetition, and exploit rates remain unresolved because the live probability service did not return an analysis.

The classification terms below are used literally. Frozen bytes, source constants, and enumerated script slots are exact source facts. Conditional scoring traces are score-only. All campaign-specific rankings and probabilities are unresolved. No bounded or sampled result was produced.

## Frozen source identities

Each supplied snapshot was SHA-256 hashed from its copied bytes. These four files were left unchanged.

| Logical source path | Frozen snapshot path | SHA-256 |
| --- | --- | --- |
| common\scripted_effects\027_doctrine_research_ai_effects.txt | docs\plans\027_doctrine_research_plans\probability_baseline_20261003\027_doctrine_research_ai_effects.txt | 51BFC294CFCBC08D5B0D4D28A5A2672D3CB3F897D6EC79DE6BD60F99CEEB9F3F |
| common\scripted_effects\027_doctrine_research_effects.txt | docs\plans\027_doctrine_research_plans\probability_baseline_20261003\027_doctrine_research_effects.txt | EC27ECF66222F4B3D779FD94912B65C155C0F7A2EA195C4D18ACACCE828A9787 |
| common\scripted_triggers\027_doctrine_research_triggers.txt | docs\plans\027_doctrine_research_plans\probability_baseline_20261003\027_doctrine_research_triggers.txt | CFBC55ECCD114D3C388CAD23D3CC87D8904152B032C325AF567BE1CE894B23A3 |
| common\script_constants\027_doctrine_research_constants.txt | docs\plans\027_doctrine_research_plans\probability_baseline_20261003\027_doctrine_research_constants.txt | D24BA6D1C77F76880BE4297F01CD848859466AC806643B29B41561376861D87A |

The source selector contract supported by the installed v3.6.0 package accepts identifier, logical path, snapshotPath, and expectedSourceHash. A snapshot selector requires the original logical path and the hash of the frozen bytes. The valid MCP retry used that binding and the lowercase form of the AI-effects hash.

The installed probability tool documentation states that shared helpers and constants still come from the current workspace, so one frozen file is not a complete historical workspace snapshot. The requested pool comparison spans the AI random_list source and its trigger eligibility dependencies. The compare request below bound the before/after trigger source, but the service timeout returned no evidence that it resolved the complete weighted-source closure.

The scenario matrix was copied byte-for-byte from docs\specs\027_doctrine_research_specs\027_doctrine_research_probability_scenarios.md to docs\plans\027_doctrine_research_plans\probability_baseline_20261003\027_doctrine_research_probability_scenarios_20261003.md. Both files hashed to 234B41494CB8AAA0929D88B36CB311D6F01CCC43C3E71EC48B3D49D7CFC45783.

The exact IDs-only scenarioSet payload submitted with the timed-out compare is recorded in docs\plans\027_doctrine_research_plans\probability_baseline_20261003\027_doctrine_research_same37_compare_attempt_unresolved_20261003.json. It parses as 37 unique scenario IDs and hashes to DFD69BB173F69F2EB81FB82E1A5E09DB7AF44CC74553BDC91D9749DA0F4EC255. Each state object is empty, so this is a replay record for the failed request, not a complete native-input scenario fixture.

The parent later supplied docs\plans\027_doctrine_research_plans\probability_cluster_baseline_20261003\chaosx_event_cluster_effects.txt with SHA-256 D8211DA66BB429A5C00D2C51EEFDC462D36D8A210BDE1BC3DF2D66F8DC25BDC2 and docs\plans\027_doctrine_research_plans\probability_cluster_baseline_20261003\event_cluster_constants.txt with SHA-256 E74A71FA4612452F80DFB651D762B39EB5AD6DD7EB41A3D08FA1FA5E741D349F.

The resumed audit found owner changes in the current worktree after those snapshots. Current source hashes are common\scripted_triggers\027_doctrine_research_triggers.txt F072DD1D70F7C8AEE0EBFC002D2967E119578AA08733FCA65806F4C6619D0A60, common\scripted_effects\chaosx_event_cluster_effects.txt 589D0AF4E736B62C234B438FCA3922893E48D3C520F3E93ACB4C6FB3C895EF41, common\script_constants\event_cluster_constants.txt C76988B9618E0D2EDDBDDA275DDF8A910613129061DCA335EEECB59C457625F7, and common\script_constants\027_doctrine_research_constants.txt A7B5AF2152B80855571C18A3607916A6068F71924593604E4A5DEDAE809E8724. The current probability effects hash is B17677AD2809791243A6E2107331F43F2B9A62233DDE1FBF01D500FEED9E6DCD, the current Event 027 root source hash is 777149623BF633FC07C04CF4F7F747A208024D2AFEE00D6E7120AE4BF9E01751, and the current AI-effects source still hashes to the frozen 51BFC294CFCBC08D5B0D4D28A5A2672D3CB3F897D6EC79DE6BD60F99CEEB9F3F. These are source identities only.

The following supporting files were read from their current worktree bytes. They are not part of the four immutable pre-patch snapshots.

| Supporting source path | SHA-256 at audit read |
| --- | --- |
| events\027_doctrine_research.txt | D61145D94A54D6EF542999EA120973D2BBA4A1DB877DD10E47DADEAF3A2AB2D1 |
| common\scripted_effects\chaosx_logic_effects.txt | C28EE6EAB4A2CEEA866C81CFFD6488E04A0B9D9ED509F650CFDDCC3F49B7548E |
| common\scripted_effects\chaosx_event_cluster_effects.txt | D8211DA66BB429A5C00D2C51EEFDC462D36D8A210BDE1BC3DF2D66F8DC25BDC2 |
| common\script_constants\event_system_constants.txt | 36EC922AC2E290A15227CC1E65C4CC6E2575E60B3E9C68D2C9BE0E5B0E45D79C |
| common\script_constants\event_cluster_constants.txt | C76988B9618E0D2EDDBDDA275DDF8A910613129061DCA335EEECB59C457625F7 |
| common\on_actions\chaosx_on_actions_system.txt | CC7708D49F8056310A011041F21C9EB648B7537C5993CEF4F6FFE8F01D015F24 |

## MCP evidence and exact blocker

The connected tool list exposed probability_inspect, probability_evaluate, probability_sweep, probability_compare, probability_render, event_inspect, event_render, tech_inspect, and tech_render. Tool exposure did not establish that the service would complete a call.

Four early probability_inspect requests were submitted separately for doctrine_research_ai_choose_scored_domain, doctrine_research_ai_choose_scored_grand, doctrine_research_ai_choose_scored_track, and doctrine_research_ai_choose_scored_subdoctrine using the custom_weighted_pool adapter. Those requests used the wrong adapter for these source helpers and are discarded as analysis evidence. The first submission also failed schema validation because the supplied SHA-256 text was uppercase. The lowercase resubmissions timed out after 600 seconds.

A correctly typed retry used adapter random_list and identifier doctrine_research_ai_choose_scored_domain with the frozen AI-effects snapshot selector. The MCP returned a tool-call timeout after 600 seconds, with no analysisId, artifact URI, source revision, scenario hash, diagnostics, or rendered evidence.

After the parent resumed the audit, four separate random_list inspections were submitted for the four frozen chooser identifiers. Each independently timed out after 600 seconds. The current track and subdoctrine chooser inspections were also submitted against the current AI-effects path with refresh enabled, and both timed out after 600 seconds.

A separate baseline probability_inspect request targeted load_event_cluster_members in the parent-frozen event-cluster effects snapshot, with no adapter supplied so the analyzer could discover compatible surfaces. It timed out after 600 seconds. No cluster analysisId, candidate catalog, revision, artifact URI, or rendered evidence was returned.

A corrected narrow retry used adapter custom_weighted_pool and source selector identifier load_event_cluster_members, logical path common\scripted_effects\chaosx_event_cluster_effects.txt, snapshotPath docs\plans\027_doctrine_research_plans\probability_cluster_baseline_20261003\chaosx_event_cluster_effects.txt, and expectedSourceHash d8211da66bb429a5c00d2c51eefdc462d36d8a210bde1bc3df2d66f8dc25bdc2. The first schema attempt used relativePath and was immediately rejected with MCP error -32602: Unrecognized key: "relativePath" at source. The corrected request timed out after 600 seconds with no analysis ID, candidate catalog, source revision, artifact URI, or rendered evidence.

A separate shared-pool probability_inspect request used adapter custom_weighted_pool and identifier update_repeatable_event_weights against common\scripted_effects\chaosx_logic_effects.txt with refresh enabled. It timed out after 600 seconds. No shared-pool candidate catalog, analysisId, source revision, or artifact URI was returned.

A probability_compare request was submitted with adapter random_list, the frozen trigger snapshot as before, the current trigger source hash DDD97111AD7C8170CE210071D65365C7061C7D197E87ADC7FC1C3F14D790DF3D as after, and the same 37 scenario IDs from the copied matrix. The state map for each scenario was empty because the matrix supplies qualitative descriptions rather than exact native inputs. The request also had no complete candidatePool because the prerequisite inspections returned no candidate catalog. The compare call timed out after 600 seconds without a comparison ID or artifact. This is a failed comparison attempt, not successful pool-delta evidence.

After the Special Forces adoption validity guard was added, a fresh random_list probability_inspect targeted doctrine_research_ai_choose_scored_grand in common\scripted_effects\027_doctrine_research_ai_effects.txt, bound to expectedSourceHash 51bfc294cfcbc08d5b0d4d28a5a2672d3cb3f897d6ec79de6bd60f99ceeb9f3f. It timed out after 600 seconds without an analysis ID, candidate catalog, source revision, or artifact.

A refreshed same-37 probability_compare was then submitted with adapter random_list, before bound to the frozen trigger snapshot hash CFBC55ECCD114D3C388CAD23D3CC87D8904152B032C325AF567BE1CE894B23A3 and after bound to current trigger hash F072DD1D70F7C8AEE0EBFC002D2967E119578AA08733FCA65806F4C6619D0A60. It reused the saved DR-A01..DR-G03 scenarioSet, whose 37 state objects are empty, and omitted candidatePool because no inspector returned a candidate catalog. The call timed out after 600 seconds with no comparison ID, scenario hash, source revision, artifact URI, or rendered result. This does not satisfy the probability comparison and proves no pool delta.

A cluster probability_compare was submitted after the corrected inspect attempt, using adapter custom_weighted_pool, before frozen effects hash D8211DA66BB429A5C00D2C51EEFDC462D36D8A210BDE1BC3DF2D66F8DC25BDC2, after current effects hash 589D0AF4E736B62C234B438FCA3922893E48D3C520F3E93ACB4C6FB3C895EF41, candidatePool ["9001"], and named scenarios DR-F04 and DR-F05. DR-F04 state supplied only cluster id 9 and Calm tier 0; its required other-member selection is absent from the pool. DR-F05 state supplied cluster id 9, selected Event 027, and activation result success (1). The compare timed out after 600 seconds with no comparison ID, scenario hash, artifact, or rendered evidence; these request inputs are not an accepted or complete native scenario fixture.

A narrow event_inspect trace of chaosx.nr27.1 (both directions, depth 3, maxNodes 80, maxEdges 160) timed out after 600 seconds with no event graph, revision, or artifact. A direct event_render timing request for the same event and depth also timed out after 600 seconds, with no render artifact. No renderer was run for the probability comparisons because none returned an analysis ID.

A fresh local SDK probe against C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\bin\stdio.js timed out during initialization and listTools after 60 seconds with MCP error -32001, Request timed out. The installed package.json reports version 3.6.0. The current session therefore did not establish fresh server health or a usable alternate transport.

All four baseline chooser inspections and the two current pool inspections remain unresolved. Event and technology structural inspect/render calls also have no returned evidence. No probability evaluation, sweep, successful comparison, simulation, sequence, or render completed.

No analysis artifacts or MCP scenario hashes exist for this handoff. The only scenario hash recorded here is the SHA-256 of the copied Markdown fixture, not an analyzer scenario hash.

The parent-provided context records reference_context failures at 60 seconds for a bounded request and 600 seconds for a broad request. The relevant offline files were read locally, with the cited paths, line spans, and file hashes listed below. Live reference_context, reference_search, reference_read, and source_lookup results were not obtained in this pass.

## Probability model and static candidate inventory

These helpers perform random_list selection using scripted candidate weights. The offline Effects wiki describes random_list shares as weight divided by the sum of candidate weights, and installed effects_documentation.md says the selected effect is picked according to its associated weight. This is probability-proportional sampling when the full active pool and all external factors are known.

The AI modding wiki describes ai_will_do as a score race that samples a value for each entry and selects the highest. The Technology modding wiki separately documents native technology research weighting and its additional engine factors. Those models do not substitute for this custom random_list analysis.

The centralized doctrine_research_ai_weight values are exact source facts:

| Constant key | Value |
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

The four source-declared chooser pools contain these fixed slot counts. These are script enumeration counts, not scenario-specific active candidate counts.

| Surface and identifier | Declared slots | Eligibility boundary | Active pool status |
| --- | ---: | --- | --- |
| Domain, doctrine_research_ai_choose_scored_domain | 5 | Each domain score starts at zero and is populated only when its has_valid_action trigger passes. | Exact five declared slots. Per-scenario valid count is unresolved. |
| Grand Doctrine, doctrine_research_ai_choose_scored_grand | 13 | Each weight starts at zero and is scored only when doctrine_research_selected_grand_doctrine_is_valid passes. | Exact thirteen declared slots. Per-domain valid count is unresolved. |
| Track, doctrine_research_ai_choose_scored_track | 18 | Each weight starts at zero and requires the selected domain, active Grand Doctrine, and matching action availability. | Exact eighteen declared slots. Per-scenario valid count is unresolved. |
| Subdoctrine, doctrine_research_ai_choose_scored_subdoctrine | 107 | Candidate scoring requires the selected domain and track plus active-incomplete or valid-empty-subdoctrine eligibility. | Exact 107 declared slots. Per-track and DLC/adapter-valid counts are unresolved. |

The thirteen Grand Doctrine slots enumerate four Army choices, three Navy choices, three Air choices, two Special Forces choices, and one Chaos Warfare choice. The eighteen track slots enumerate four Army, four Navy, four Air, two Special Forces, and four Chaos Warfare contexts. The same track token can appear under distinct domain gates, so that source reuse does not establish a duplicate active candidate.

The source score and effect traces are exact conditional logic only. The four frozen snapshots contain no ai_will_do, ai_chance, or mtth: token, so no MTTH-backed AI score or event-option ai_chance surface was identified in those four files.

## Source findings

### Domain and Navy readiness

In common\scripted_effects\027_doctrine_research_effects.txt, doctrine_research_ai_score_domains initializes all five scores to zero and scores each only after its domain has a valid action. The Navy adoption trigger in common\scripted_triggers\027_doctrine_research_triggers.txt is satisfied when the country has no naval Grand Doctrine. It does not require a coastline, dockyard, ship, or naval strategy signal.

For a landlocked country without ships, naval factories, or a Navy route signal, a valid Navy adoption can therefore still receive the base weight. A war condition and faction membership can add their generic weights even without naval readiness. This is a positive source weight on a selectable Navy adoption, not proof that Navy wins often. The exact normalized share is unresolved.

The current Navy strategy-signal trigger recognizes existing naval doctrines, ships, convoys, and naval factories. The Navy owner-readiness trigger recognizes coastline, naval factories, ships, or existing naval doctrine. The inspected triggers do not represent a future maritime focus plan or planned naval investment. DR-A05's future-plan expectation therefore has no explicit signal in these frozen Navy predicates.

### Grand Doctrine, track, and subdoctrine scores

doctrine_research_ai_score_selected_grand adds generic division presence, military-factory presence, war, coastline, faction, selected-domain strategy, and owner readiness before doctrine-specific force-fit modifiers. The generic division-presence term is domain-agnostic. The Army template-composition modifiers are separately guarded by Army-domain and named-doctrine checks.

Because the generic terms are shared across valid candidates within a chooser pass, they do not by themselves change the source score ordering when their conditions are identical across that pool. They do contribute to the random_list denominator and can flatten differences in the resulting shares. The magnitude of that effect is unresolved without evaluated scenario scores and a complete active pool.

Track and subdoctrine scoring reuse broad force, production, war, geography, faction, and continuity terms. The source has conditional candidate gates and mastery-completion signals, but their behavior against each named campaign state was not evaluated. The frozen subdoctrine list is manually enumerated. No duplicate active subdoctrine candidate was established by the static scan, which found source identities in scoring setup and result mapping. Runtime gate overlap remains unverified.

### Validity, recalculation, and sequence

The domain chooser keeps invalid domains at zero through has_valid_action predicates. Grand Doctrine slots begin at zero and depend on the adapter-registry and adoption validity trigger. Track slots require a matching domain and available action. Subdoctrine slots require active-incomplete or valid-empty-native-eligible checks. This is a source-level fail-closed pattern. The MCP did not prove engine validity, adapter coverage, or zero participation under invalid injections.

doctrine_research_ai_resolve_active_batch loops through active choices and calls doctrine_research_ai_pick_choice on each iteration before confirming the selected action. This source structure supports a fresh chooser pass after each choice. DR-C06 and DR-E01 through DR-E06 still need sequence evidence because the tool did not evaluate state transitions, batch queues, or native mastery timing.

### Parent-supplied empty-track safety restriction

The frozen trigger snapshot's doctrine_research_empty_track_is_verified delegates to doctrine_research_native_mastery_adapter_is_verified, while doctrine_research_empty_track_adapter_is_verified checks the registry-initialized flag. The current trigger source instead makes doctrine_research_empty_track_is_verified always no and delegates the adapter gate to it. The latest current trigger hash is F072DD1D70F7C8AEE0EBFC002D2967E119578AA08733FCA65806F4C6619D0A60. The current gate therefore removes empty-track assignment and first-step candidates until the required local native-engine proof exists.

The same current trigger file now guards Special Forces adoption with NOT = { has_any_grand_doctrine = special_forces } in addition to excluding the two known Special Forces doctrine tokens. This protects an active unregistered Special Forces Grand Doctrine from replacement; the ordinary domain-specific adoption gates are unchanged. The Special Forces chooser source and gate were source-reviewed only; MCP probability inspection and comparison did not return.

Per the parent, existing assigned mastery and Grand Doctrine adoption remain available, and other domains are not disabled. The affected pool is the empty-track route. DR-C03 and DR-C07 directly depend on it. DR-E01, DR-E02, and DR-E04 may also depend on selecting a track and subdoctrine immediately after adoption or on a fresh branch. Those scenario effects need a successful source-bound compare to confirm. The parent identifies this as an engine-safety blocker, not full feature closure.

### Repeatable event and cluster surfaces

The current common\scripted_effects\chaosx_logic_effects.txt registers 51 repeatable-event slots and includes event ID 27. The Event 027 entry is chaosx.nr27.1 in events\027_doctrine_research.txt.

The current event-system constants set the default event weight to 1000, recovery rate to 20, and cap-reduction factor to 0.5. on_repeatable_event_fired reduces the individual cap, clears the current event weight, and runs the minor-event pacing update outside cluster-member context. update_repeatable_event_weights restores eligible weights toward their individual caps after the required Chaos-level check. These values and branches are exact current-source observations, not normalized chances or a verified time distribution.

Event 027 shared registration and eligibility use the repeatable-event pool, including event ID 27 and the no-valid-participant exclusion. The batch/evolution layer changes choices per firing and reselects each choice in the batch loop. A bounded search of events\027_doctrine_research.txt and the four frozen 027 scripts found random_list in the AI-effects file, with no mean_time_to_happen, mtth:, ai_will_do, or ai_chance token. No separate MTTH timing surface was identified in those files.

The scenario matrix expects monthly recovery for DR-F02 and a complete cadence/state manifest for DR-F03. A bounded search found update_repeatable_event_weights called from the event-system pacing effects, but no direct on_monthly event-weight hook in common\on_actions. The actual scheduled recovery cadence and its interaction with the event pulse remain unresolved.

The current event_cluster_id now contains National Breakthroughs = 9, and the current load_event_cluster_members branch adds Event 027 as one optional, Medium-severity, primary-trigger row. Its stable row id is 9001. The frozen constants snapshot has no ID 9 and the frozen loader has no cluster-9 branch, so source membership is zero frozen rows to one current row. This is a static source count, not an MCP-proven probability delta. Other proposed members 54, 65, 67, 83, 85, and 89 remain absent pending their own reworks.

The current row uses the Event 027 declared Calm floor 0. The shared Medium floor 1 is overridden only for the exact cluster 9, event 27, row 9001 combination. The current and frozen event_cluster_member_participation_matrix blocks are text-identical; no shared chance coefficients or AI score coefficients were changed in this patch. No numeric balance target is introduced. These statements are source comparisons, not an accepted probability model.

DR-F04 requires another National Breakthroughs member to be selected while Event 027 remains eligible. The current in-scope pool contains only row 9001, so its other-member precondition and cluster-size distribution remain unresolvable; do not invent one of the deferred member IDs. DR-F05 conditions on Event 027 already selected and the cluster activation roll succeeding. Its source-bound probability_compare timed out, so selected-member fanout, exactly-once delivery, and absence of second fanout remain unproven by MCP.

The required cluster probability_compare was attempted against distinct frozen and current effects bytes, using DR-F04 and DR-F05, but timed out after 600 seconds. Parent integration requires the transaction fanout to capture all rows before AI and History binders wake. The six creator arrays and failed-publication quarantine are reported by the parent as current and source-reviewed; this audit makes no full-feature or live-game claim and did not launch HOI4.

## Scenario matrix coverage

The full scenario names and qualitative state descriptions are preserved in docs\plans\027_doctrine_research_plans\probability_baseline_20261003\027_doctrine_research_probability_scenarios_20261003.md. The supplied state descriptions use terms such as large, significant, several, high, limited, and severe without exact country tags, dates, unit counts, factory counts, current weights, DLC combinations, or strategy bindings. The compare request reused the 37 IDs with empty state maps as a route probe, not as an exact native-input scenarioSet. No fixture keys or gameplay flags were invented, and the timed-out inspect returned no requiredInputPaths to ground a complete state map.

| Scenario IDs and names | Surface | Expected order or behavior from the matrix | Pool and external-factor completeness | Result |
| --- | --- | --- | --- | --- |
| DR-A01 Doctrine-less land major, DR-A02 Island naval power, DR-A03 Air-centered continental power, DR-A04 Landlocked small minor, DR-A05 Future maritime plan, DR-A06 All ordinary domains complete | Domain chooser | A01 Army above Air above Navy. A02 Navy should compete strongly and normally lead under severe naval conditions while Army progress remains valid. A03 Air should lead or stay near the top, with a near-complete Army exception. A04 Army should lead, Air may remain secondary, and Navy should be invalid or near zero. A05 a credible future maritime plan should raise Navy without forcing it. A06 no candidate. | Five source slots are exact. The matrix has no exact divisions, production levels, fleet counts, plan identifiers, dates, or state bindings. | Source trace is score-only. Every ranking and active pool count is unresolved. |
| DR-B01 Mobile armored army, DR-B02 Manpower-rich infantry state, DR-B03 Doctrine plan conflict, DR-B04 Invalid doctrine candidate | Grand Doctrine chooser | B01 mobile or armored above infantry-mass or static defense where those graph choices exist. B02 infantry, mass, defensive, or irregular choices rise with force and strategy fit. B03 historical plan and campaign-fit rankings must be compared under both plans. B04 invalid doctrine must have zero participation. | Thirteen source slots are exact. The active graph, country plan, force composition, DLC, and invalid-candidate state are not exact in the matrix. | Source trace is score-only. Candidate ranks and invalid-candidate participation are unresolved. |
| DR-C01 Near-complete relevant branch, DR-C02 Near-complete irrelevant branch, DR-C03 Empty track fills missing capability, DR-C04 Four equal tracks, DR-C05 One dominant track, DR-C06 Branch completes between choices, DR-C07 Banked mastery on empty track | Track and subdoctrine choosers, then sequence | C01 relevant armor should lead. C02 relevant land should beat an irrelevant near-complete naval branch. C03 operations or logistics should compete under severe supply stress. C04 show bounded variation. C05 stack and finish the dominant branch, then recalculate. C06 remove a branch completed between choices. C07 preserve banked progress and attribute no more than one extra event mastery step, pending native sequence proof. | Eighteen track slots and 107 subdoctrine slots are exact source enumerations. Active branch and subdoctrine counts, branch completion state, seed, DLC, and native mastery sequencing are incomplete. | Source trace is score-only. Rankings, sampling, starvation, and sequence are unresolved. |
| DR-D01 CBRN-ready Chaos Warfare country, DR-D02 CBRN-unready ordinary country, DR-D03 Active Chaos Warfare infantry-heavy formations, DR-D04 Active Chaos Warfare theater command need, DR-D05 Special nonhuman country without adapter, DR-D06 Special country with valid adapter | Custom domain and doctrine adapter | D01 Chaos Warfare should compete strongly without becoming a direct downstream unlock. D02 Chaos Warfare should be absent. D03 Hazard Assault Formations should lead, with Integrated CBRN Command able to compete when ready. D04 Integrated CBRN Command should lead or compete strongly. D05 no candidate. D06 a valid owner adapter participates. | Domain and subdoctrine slots are enumerated. Exact CBRN prerequisites, equipment, owner adapters, live country classification, and DLC inputs are missing. | Source gates are score-only. Pool presence and result ordering are unresolved. |
| DR-E01 Evolution I adoption sequence, DR-E02 Evolution II mixed services, DR-E03 Evolution III broad curriculum, DR-E04 Evolution IV branch completion, DR-E05 Queue with different stages, DR-E06 Evolution unlock during batch | Multi-choice sequence across domain, Grand Doctrine, track, and subdoctrine choosers | E01 adoption then a second choice in the new doctrine. E02 allow Army stacking, Navy adoption, or a split by score, with rescoring after adoption. E03 develop several close-scoring tracks. E04 make five-choice completion possible when one fresh branch clearly fits. E05 retain separate batches of one and three choices. E06 keep the active batch at two choices and grant three on the next normal firing. | Source has a per-choice chooser loop. Exact dates, batch state, cadence, native sharing, candidate pool, and terminal state are not declared as analyzer inputs. | Source trace is score-only. Sequence and timing results are unresolved. |
| DR-F01 Initial event pool, DR-F02 After first firing, DR-F03 Sequence through four firings, DR-F04 Event 027 optional cluster member, DR-F05 Event 027 selected cluster member | Repeatable event pool and event cluster | F01 rank Event 027 in the complete current pool. F02 show reduced cap and recovery. F03 assess recurrence and starvation through four firings. F04 model optional participation and limited cluster size. F05 keep a selected Event 027 member to one fire with no second fanout. | Fifty-one repeatable slots are declared. The active pool, per-event eligibility, weights, cap history, cadence, resets, cluster ID, complete member set, and participation factors are incomplete. The named National Breakthroughs cluster has no matching current source identifier or explicit Event 027 row in the bounded source lookup. | Unresolved. No normalized chance, timing, or cluster distribution is available. |
| DR-G01 Human and AI pool parity, DR-G02 DLC matrix, DR-G03 Invalid adapter injection | Human/AI eligibility, DLC, and adapter validity | G01 each human-valid action can enter AI scoring and each AI candidate is human-valid. G02 unavailable content has zero participation across supported DLC combinations. G03 malformed adapters fail closed while valid domains remain usable. | Exact human-visible pool, supported DLC combinations, test adapter identity, invalid branch, and maximum mastery are not supplied as native analyzer inputs. | Source checks are score-only. Parity, DLC, and fail-closed results are unresolved. |

## Findings against the named expectations

DR-A04 has a concrete source risk: Navy adoption is valid whenever no naval Grand Doctrine is present, while the score function awards a positive base weight to every valid domain. Naval readiness affects additional weights but does not gate the Navy candidate itself. Recommendation: gate the neutral Navy floor on current naval assets, coastal access, or a valid and current maritime plan, then verify A01, A02, A04, and A05 with a complete domain pool.

DR-A05 has no explicit future-plan signal in the inspected Navy strategy/readiness predicates. Recommendation: add an owner-defined route signal with validity and expiry conditions, and let it raise the Navy score only while its plan remains valid. Do not let an obsolete route flag preserve naval preference.

DR-B01 through DR-B03 need domain-specific score evidence. The Grand Doctrine scorer applies generic division presence and other broad context to every candidate before adding doctrine-specific fit. Recommendation: scope force-family evidence to the selected domain, and make completion value depend on strategic relevance so C02's irrelevant near-complete branch cannot overwhelm the relevant land branch.

DR-C01 through DR-C05 and DR-D03 through DR-D04 need candidate-specific fit to compete with repeated generic production, war, geography, faction, continuity, and completion additions. Recommendation: retain the centralized constants, distinguish force fit from generic country size, and calibrate completion against relevance using the named matrix. No numeric target is accepted in this handoff.

DR-B04 and DR-G03 have source-level zero initialization and validity gates for fixed enumerated candidates. Recommendation: retain fail-closed gates and compare every current registered identity against the 13, 18, and 107 hand-coded chooser slots before the parent changes the registry.

DR-F01 through DR-F03 require the complete 51-event registered pool, current eligibility and weights, fired-state caps, monthly or event-pulse recovery cadence, and major reset transitions. Recommendation: do not tune Event 027's normalized share until those inputs are bound to one baseline fixture. The current source gives cap and recovery constants, but no selection distribution was measured.

DR-F04 and DR-F05 require a decision on the cluster surface. Recommendation: either bind the scenarios to an existing stable cluster identifier and its full member rows or define the intended National Breakthroughs cluster and Event 027 member role before probability evaluation. The auditor does not promote that scenario label into accepted design by itself.

DR-G01 through DR-G03 require matching human and AI availability predicates, explicit DLC cases, and a named malformed adapter fixture. Recommendation: use the same validity boundary for human and AI candidates, prove zero participation for unavailable adapters, and rerun after the parent supplies fixed source-backed cases.

## Result classes and balance risks

Exact source observations: the four snapshot hashes, the centralized coefficient values, the fixed chooser slot counts, the source conditions listed above, the 51 repeatable-event registrations in the current support source, and the current event cap/recovery constants.

Score-only observations: conditional additions and eligibility gates in the frozen effects and triggers. These do not establish normalized candidate shares.

Unresolved: all 37 scenario rankings, all selection percentages, timing distributions, sweep thresholds, rank reversals, dominance, starvation, human/AI parity, DLC behavior, invalid injection behavior, batch sequence outcomes, repeat frequency, and cluster-size distribution.

Potential risks for the parent to measure are positive neutral Navy participation, generic score terms flattening candidate-share differences, future route plans absent from Navy readiness signals, hand-maintained candidate lists drifting from adapter registries, and the matrix's National Breakthroughs cluster not matching a current explicit cluster row.

No source-level scan establishes that a candidate wins often, dominates, starves another valid option, or causes a snowball. No exact probability is claimed. No numeric target has been accepted.

## Required analyses not completed

| Tool or evidence | Status | Reason |
| --- | --- | --- |
| probability_inspect for all four choosers and current track/subdoctrine pools | Blocked | Each correctly typed random_list inspect timed out after 600 seconds, including the separate domain, Grand Doctrine, track, and subdoctrine identifiers. A fresh current Grand Doctrine inspect after the Special Forces guard also timed out after 600 seconds. |
| probability_inspect for the frozen cluster member loader | Blocked | The no-adapter baseline inspect and the corrected source-bound custom_weighted_pool retry each timed out after 600 seconds without an adapter catalog or artifact. The first corrected-selector schema attempt using relativePath was rejected immediately; the retry used path. |
| probability_inspect for the shared repeatable-event pool | Blocked | The source-bound custom_weighted_pool inspection of update_repeatable_event_weights timed out after 600 seconds without a candidate catalog. |
| probability_evaluate for DR-A01 through DR-G03 | Blocked | The prerequisite valid inspect returned no analysis artifact, and the supplied matrix lacks exact native values for several state descriptions. |
| probability_sweep | Blocked | No retained analysis, exact scenario baseline, or complete active candidate pool is available. |
| probability_compare for the empty-track and Special Forces adoption validity changes | Blocked | The updated same-37 request bound the frozen trigger hash CFBC55ECCD114D3C388CAD23D3CC87D8904152B032C325AF567BE1CE894B23A3 to current trigger hash F072DD1D70F7C8AEE0EBFC002D2967E119578AA08733FCA65806F4C6619D0A60, then timed out after 600 seconds. Its named scenarios have empty states and no candidate catalog was available; no comparison result is claimed. |
| probability_compare for cluster 9 registration | Blocked | The source-bound custom_weighted_pool comparison used frozen effects hash D8211DA66BB429A5C00D2C51EEFDC462D36D8A210BDE1BC3DF2D66F8DC25BDC2 versus current effects hash 589D0AF4E736B62C234B438FCA3922893E48D3C520F3E93ACB4C6FB3C895EF41 and timed out after 600 seconds. The source count is 0→1 only; no probability or distribution is proven. |
| probability_simulate | Skipped | The matrix declares qualitative conditions, not uncertain-input distributions or sampling seeds. No sampled result is claimed. |
| probability_sequence | Blocked | No complete custom-pool manifest with verified candidate set, cadence, transitions, caps, recovery, removals, resets, and terminal states was available. |
| probability_render | Blocked | No analysisId or expected scenario hash exists to render. |
| event_inspect and event_render | Blocked | The narrow trace and direct timing render for chaosx.nr27.1 each timed out after 600 seconds. No event graph, revision, or render artifact is available. |
| tech_inspect and tech_render | Blocked | The connected service did not return from the valid probability route. No technology/doctrine graph or render artifact is available. |
| Live reference_context/search/read and source_lookup | Blocked in the current service context | The parent-provided context records reference_context timeouts. The offline source sections were read directly and are listed below. |

## References read locally

The offline AI modding page was read at paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md, lines 26-37. It distinguishes highest-sampled ai_will_do score races from probability-proportional event options. Snapshot SHA-256: 917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818.

The offline Technology modding page was read at paradox_wiki\Technology modding - Hearts of Iron 4 Wiki.md, lines 331-354. It describes native technology weighting and engine-side research factors. Snapshot SHA-256: C5428838DB20C4C812C66AFF82CBAFC58DB3B73453C30436BCE0D97436170BEE.

The offline Effects page was read at paradox_wiki\Effects - Hearts of Iron 4 Wiki.md, lines 4518-4539, for random_list weights and normalization. Snapshot SHA-256: 997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C.

The offline Data structures page was read at paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md, lines 425-435, for variable use in random_list. Snapshot SHA-256: 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4.

Installed vanilla effects_documentation.md was read at C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md, lines 5413-5425, for random_list selection and variable weights. SHA-256: 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF.

Installed script_concept_documentation.md was read at C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md, lines 216-228, and common\script_constants\documentation.md, lines 1-19, for script-constant support and fixed-point access. Their SHA-256 values are 884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7 and E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C.

## Handoff boundary

This handoff and the exact scenario fixture copy are the only files created for this audit. The four frozen source snapshots were not edited. No gameplay, AI, event, trigger, constant, technology, doctrine, localisation, event specification, or skill file was changed.

The audit remains blocked for normalized probability evidence. Resume after the MCP service responds with the four separate random_list probability_inspect calls, then build exact native inputs for the named scenarios, evaluate the applicable DR cases, sweep the declared sensitivity paths, compare the empty-track pool under the same 37 scenarios, and render ranking/sensitivity/unresolved views.

After the parent adds cluster ID 9 and row 9001, inspect the frozen and current cluster membership sources, compare the same DR-F04 and DR-F05 scenarios, retain the Calm floor 0 exception for only that row, and verify that row capture finishes before downstream AI and History binding. Sequence analysis remains gated on a complete event-driven cluster manifest with explicit fanout cadence, eligibility, chance, and terminal behavior.
