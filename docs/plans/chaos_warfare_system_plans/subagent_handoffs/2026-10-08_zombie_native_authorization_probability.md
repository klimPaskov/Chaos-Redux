# Read-only probability handoff: zombie native raid authorization

Audit date: 2026-10-08. This audit covers the native raid AI and success-factor surfaces in common\raids\zombie_weaponized_raids.txt and common\raids\zombie_weaponized_friendly_raids.txt before and after the accepted authorization patch. It does not audit the five separate intelligence-operation definitions.

The canonical before files were archived byte-for-byte in docs/testing/2026-10-08_zombie_native_authorization_probability/before/common/raids/ before source edits, with exact -text rules in the evidence folder’s .gitattributes. The final after files were recopied with the same attribute from live source after the worker’s presentation-only update. Before hashes are in baseline_manifest.json, MCP-era after hashes are preserved in mcp_after.json, and final after hashes and exact paths are in final_source_refresh.json.

## MCP coverage and blocker

I began with hoi4.probability_inspect on both canonical before snapshots and repeated it on both post-authorization after snapshots. Those after inspections preceded the final payload-cost presentation-only delta; their source hashes and artifacts remain preserved as historical receipts in mcp_after.json. All four inspections returned PROBABILITY_SOURCE_DISCOVERED with discoveryReason=no_weighted_surfaces, 0 candidates, 0 required inputs, and 0 unresolved items. The final source hashes are recorded separately in final_source_refresh.json, and no probability call was rerun after the presentation-only delta.

The live probability adapter schema includes event MTTH, event option AI chance, decision/mission/focus/research/doctrine AI, direct_random, random_list, ai_strategy_factor, and custom_weighted_pool. It contains no native RaidType AI or success_factors adapter. The tool inventory also exposes no raid-domain inspector. The source itself clearly contains native ai_will_do and success_factors blocks, so no_weighted_surfaces is an analyzer coverage gap, not proof that the definitions contain no weights.

I made one adapterless probability_compare probe after the patch with the named gate-coverage cases in scenario_plan.json. It returned PROBABILITY_SURFACE_EMPTY with the exact message “No weighted blocks matched this request,” availableAdapters=[], and candidatePool=[]. The other after inspection returned the same no_weighted_surfaces result. No numeric before/after probability comparison is available for either file, and no scenario hash was generated. I did not substitute decision_ai_will_do, invent a custom pool, or hand-calculate any probability.

## Native score and success-factor source

The six scoped RaidTypes are weaponized_zombie_strike_low, weaponized_zombie_strike_medium, weaponized_zombie_strike_high, weaponized_zombie_strike_low_friendly, weaponized_zombie_strike_medium_friendly, and weaponized_zombie_strike_high_friendly.

All six ai_will_do blocks have base=1. The existing Kruger factors remain: kruger_state_factor=5.00 when the actor is in the Kruger state with the Kruger raid AI active, and kruger_host_factor=3.00 for an active Kruger host outside the Kruger state. The hostile low variant retains factor=8 for a JAP actor at war with CHI targeting CHI and factor=5 for a zombie-controlled target state. Each friendly variant retains factor=12 for a zombie-controlled target state.

Each RaidType now also has one factor=0 modifier before its prior desirability modifiers, gated by NOT { weaponized_zombie_raid_can_target_from = yes }. The current source therefore sets the native AI score to zero when the exact actor/target authorization helper is false. All six base scores and every pre-existing AI modifier block remain byte-identical after newline normalization.

Each file retains file-local WZ_RAID_SUCCESS_BASE_LOW=0.35, WZ_RAID_SUCCESS_BASE_MEDIUM=0.50, WZ_RAID_SUCCESS_BASE_HIGH=0.68, and WZ_RAID_PAYLOAD=125. The shared Kruger factor constants are 3.00 and 5.00 in common\script_constants\016_brilliant_scientist_constants.txt and match baseline commit 4704913e8 byte-for-byte; shared_score_constants.json records the baseline/current Git blob identity.

All six success formulas retain the same native chance inputs: experience weight=0.1/start_weight=-0.1/reference=1.0; air_defence 0.05/-0.05/reference=100; air_agility 0.1/-0.1/reference=100; reliability 0.1/-0.1; air_superiority 0.25/-0.25/reference=1.0; interception weight=-0.25/reference=10; anti_air and radar weight=-0.05; and intel weight=0.2/reference=100. There is no critical or disaster formula block in these six definitions.

Each type retains command_power=15, zombie disease bomb payload 125, days_to_prepare=10, days_re_enable=0, and three aircraft unit requirements: CAS 50, tactical bomber 25, and strategic bomber 10. The AST comparison confirms all success_factors blocks, payload blocks, scalar costs, and unit requirements are unchanged.

The installed raid documentation defines success_factors as native chance formulas; the listed base values are inputs to the formulas, not final probabilities. The offline wiki describes typical ai_will_do score races separately from event ai_chance sampling. I classify the native AI values as score-only source evidence and the final native success probabilities as unresolved. No click or normalized raid-selection probabilities are claimed.

## Named authorization coverage cases

scenario_plan.json records the named cases and their exact source-bound predicates. They are planned gate checks, not evaluated MCP scenarios, because no RaidType adapter is exposed.

The preflight bindings are ROOT for the actor country, FROM for the exact victim country, and var:target_state for the selected state. The final callback uses event_target:zombie_native_raid_actor, event_target:zombie_native_raid_victim, and event_target:zombie_native_raid_target_state.

weaponized_zombie_raid_actor_is_authorized requires an existing, non-capitulated actor, no world_end global flag, the existing zombie unlock helper, and bio_kruger_last_resort_authority_is_valid. The unlock helper accepts has_tech zombie_disease_bomb_delivery_systems, has_country_flag weaponized_zombies_completed, or completed project sp:weaponize_the_zombies. The Kruger helper accepts active Kruger raid AI, a non-Kruger-state actor, or canonical last-resort authority.

weaponized_zombie_raid_can_target_from additionally requires FROM to exist, an active war with FROM, no shared faction, cbrn_policy_allows_strategic_use_against_from, a valid target state, and the target state still controlled by FROM. Strategic policy accepts cbrn_use_policy at or above unrestricted_authorization=5, or a valid retaliation right against the exact FROM.id. Retaliation policy is value 2, battlefield-only policy is 3, and the active target-ID record must exist with global.num_days less than or equal to its expiry day.

The final callback helper rechecks the exact actor/victim/state event targets, actor identity, current authorization, current war and faction status, strategic policy against the captured victim, target validity, and state controller. The bridge does not debit stock or Command Power again after native commitment.

The scenario plan includes unauthorized_no_project, unrestricted_valid_enemy, retaliation_record_valid, retaliation_record_absent, retaliation_record_expired, battlefield_only_strategic_target, zombie_friendly_enemy_target, lost_war, lost_control, kruger_permitted, and kruger_blocked. It declares a valid target binding for the unrestricted case; exact retaliation expiry presence, absence, and expiry boundaries; battlefield-only policy against a strategic raid; friendly mode requiring a zombie-controlled target; separate war and controller failures; and active/inactive Kruger authority.

The six zombie types in the two files are only the bounded source scope. The complete engine-wide native raid AI pool and target enumeration are not exposed by MCP, so AI selection probability cannot be normalized. For success_factors, unit/target inputs such as aircraft experience, air defence, agility, reliability, target anti-air, radar, interception, air superiority, and intel are not scenario-bound by a native adapter.

## Before/after source evidence

The canonical before hashes are FFED93F0E0E4B1239E8B0F3D929EF3EC885B8E4F129648CC32F810DEB7715244 for the hostile file and 50F10C9C3A086AF4A787286D697F3E2099C535970525CFA4A9C312343757D7CD for the friendly file. The MCP-era post-authorization, pre-presentation after hashes were 0819442C35482D2D98F1699DF44F348725D7A6858139F3072FA84E65079ACAF2 and 748CBDAD5184CFD63660D068C95DA22EF463DFCE118EC2EF206E2A294E683917 respectively; these remain unchanged in the historical MCP receipts.

The historical normalized AST comparison in after_comparison.json confirms that all six base AI scores remain 1, every old AI modifier block is byte-identical, each type adds exactly one authorization zero modifier, and every success_factors block is byte-identical. The final source refresh in final_source_refresh.json repeats the exact invariance comparison against the final live sources: all six existing AI modifier lists, success_factors blocks, essential_equipment blocks, scalar costs, unit requirements, and file-local constants still match the frozen before snapshots after newline normalization; each type has exactly one factor=0 authorization modifier. The final after archives match live source hashes ac67a2153b8730043719b52f96a4423470cac858ac541eab677dbc82e2384887 (hostile) and 1476510173770fb8f77a7ce55f8d1c8858559773658af98f3913b6bfed0ca508 (friendly). This is source-invariance evidence, not a probability comparison.

After the MCP receipts were captured, the raid owner replaced six redundant payload-cost tooltip wrappers with the same hidden has_weaponized_zombie_raid_payload predicate; native essential_equipment still expresses the 125-unit cost. The existing authorization sentence remains, and the unused weaponized_zombie_raid_available_tooltip localization key was removed. The worker receipt is docs/testing/2026-10-08_zombie_native_authorization/cost_presentation_change.json. The final source refresh verified the payload predicate remains in all six availability blocks and that the presentation update left the AI, success, payload, scalar-cost, and unit-requirement invariants intact. This delta was not sent through the unsupported probability adapter.

## Risk findings and classification

The source zero gate prevents an unauthorized or invalid target from receiving a positive AI weight before existing desirability boosts. The native analyzer could not prove the engine’s selection response to the zero score or rank the authorized raid options. Dominance, starvation, and rank reversal remain unresolved because there is no native raid AI adapter and the engine-wide candidate pool is not enumerated.

All six definitions use days_re_enable=0. The installed raid documentation says zero means no per-type re-enable delay. Repeated valid raids remain possible subject to native target/system cooldowns, which this unsupported probability route did not model. No cadence, repetition sequence, or snowball simulation was performed.

The source-level base success coefficients and modifier traces are exact, but final native success probabilities remain unresolved. No simulation or numeric ranking is claimed. No numeric balance change is recommended; retain all existing score factors and success coefficients.

## References, tools, and skipped analyses

The live tools used were hoi4.probability_inspect before and after, hoi4.probability_compare for one adapterless coverage probe, hoi4.source_lookup for raid and gate definitions, and the offline reference routes. Full artifact reads were not repeated because the previous probability handoff records MCP -32603 “Artifact provenance manifest is unavailable”; the current inspector summaries already contain the complete coverage status needed here.

Installed documentation read through the reference route: common/raids/_documentation.md, Raids AI and preflight gates lines 64–133, success_levels/success_factors lines 188–225, success chance formulas lines 303–326, and raid-instance dynamic variables lines 548–559; revision eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e. Offline wiki references read: AI modding lines 30–37, revision 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818; Scopes ROOT line 260 and FROM line 263, revision 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49. The vanilla nuclear_strike precedent was inspected at game:common/raids/nuclear_raids.txt, ai_will_do line 9 and success_factors lines 98–148; source-lookup revision bbb1fd48d41f8a4e3cfa3ea9b9b61f669c38888366f8b2fdf4fe9de0c84b55b3, marked shadowed by the mod.

probability_evaluate, probability_sweep, probability_simulate, probability_sequence, and probability_render were not run because neither native raid file exposed a compatible weighted surface. probability_compare returned PROBABILITY_SURFACE_EMPTY. No event inspect/render route was used because the audit scope is native RaidType AI/success formulas and fixed callback mappings do not define the raid weight surface. No game launch, log search, helper expansion, or native task was performed by this auditor; no gameplay source or index files were edited and no commit was made.
