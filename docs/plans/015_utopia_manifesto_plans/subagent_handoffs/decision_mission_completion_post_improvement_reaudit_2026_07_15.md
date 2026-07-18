# Event 015 Decision and Mission Post-Improvement Re-audit

Date: 2026-07-15  
Role: chaosx_decision_mission_auditor  
Mode: read-only source audit  
Audited event: 015 — Utopia Manifesto  
Verdict: **PASS**

## Result

The post-improvement decision and mission implementation passes this source-level completion audit with **zero P0–P3 defects**.

| Priority | Count |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |
| Total actionable findings | 0 |

No audit-driven gameplay or localisation patch is required. There is therefore no defect-evidence section beyond the zero-count ledger above.

## Audited inventory

| Surface | Decisions | Missions |
| --- | ---: | ---: |
| Main decision file | 105 | 39 |
| Evolution-consumption file | 15 | 1 |
| Prefire-evolution file | 1 | 3 |
| **Total** | **121** | **43** |

The package also contains nine Event 015 decision categories.

Mechanical inventory checks found:

- 121 of 121 decisions have an explicit ai_will_do block.
- 43 of 43 missions have activation, available, cancel_trigger, cancel_effect, timeout_effect, and a variable-backed days_mission_timeout.
- 43 targeted decisions have target_root_trigger and target_trigger.
- 10 targeted missions have target_trigger.
- All 53 targeted blocks use bounded state selectors or prefilled scope arrays; none performs a world-country search.
- 101 decisions use prepared custom costs. Every custom cost maps to the matching prepared payment or policy-action payment effect.
- 13 decisions are intentionally political-power-only.
- Seven decisions are intentionally free selectors or cleanup controls: the six calling selectors and the Necessary Ground target-clear control. None grants a material reward.
- All resource and reserve affordability gates permit exact payment; no strict greater-than-only payment gate remains.

## Acceptance ledger

| Requirement | Result | Evidence |
| --- | --- | --- |
| Independent Industrial Housing pressure | PASS | common/scripted_triggers/015_utopia_manifesto_triggers.txt:311–318 defines live housing pressure without Homes Near Work; lines 503–518 apply it to state suitability. |
| Homes Near Work remains a separate prerequisite | PASS | common/decisions/015_utopia_manifesto_decisions.txt:1214–1271 checks the focus/route prerequisite separately from live pressure. |
| Housing-pressure prerequisite is disclosed | PASS | localisation/english/015_utopia_manifesto_l_english.yml:254 states that Homes Near Work and an unresolved national housing emergency are both required. |
| Active district loss cleans active work | PASS | common/scripted_effects/015_utopia_manifesto_decision_effects.txt:1233–1259 cancels the affected survey, build, charter, or Penal Works work and clears the current project pointer. |
| Completed district loss reverses exact calling relief once | PASS | The loss handler calls utopia_manifesto_reverse_lost_district_calling_relief before clearing state flags. The helper at lines 1064–1133 selects exactly one charter role branch and applies the inverse of the same primary/secondary constants used by completion at lines 1684–1721. |
| District state package is removed | PASS | utopia_manifesto_clear_district_state_package at lines 994–1055 clears survey, suitability, build, obligation, built-role, charter-route, Penal Works, modifier, and state-variable data. |
| Tracked-state membership is removed | PASS | The affected state is removed from utopia_manifesto_district_states after reversal and before proof rebuilding, preventing a second reversal. |
| Counters and current proofs are rebuilt | PASS | utopia_manifesto_rebuild_district_network_proof at lines 1138–1200 rebuilds completed and chartered counts and current district proof only from remaining owned, controlled, core states. |
| Current five-role proof is rebuilt | PASS | The rebuild restores the four ordinary current roles from valid remaining chartered states, then delegates to the five-role refresh. common/scripted_effects/015_utopia_manifesto_identity_effects.txt:846–858 requires the Guardians route, all four ordinary roles, and a functioning Provision Ring. |
| Network degrades when proof is lost | PASS | A previously proven district network calls break_garden_district_network when the rebuilt valid district count falls below its proof threshold. |
| Valid Provision Ring survives unrelated district loss | PASS | Ordinary district rebuilding preserves the Provision Ring proof. It is cleared only by island downstream invalidation or terminal teardown. |
| Physical construction survives | PASS | The state-package cleanup has no building-removal effect. Infrastructure and factories created by district completion remain physical state changes. |
| Durable historical Ledger conduct survives ordinary loss | PASS | Historical charter policy deltas and durable conduct markers are not undone by ordinary state loss; only the state-derived current calling relief is reversed. |
| Direct control-change reconciliation | PASS | common/on_actions/015_utopia_manifesto_on_actions.txt:219–295 uses the documented new-controller, old-controller, and changed-state scopes, checks exact tracked-state membership, and reconciles only affected Event 015 actors. |
| Bounded actor pulse | PASS | events/015_utopia_manifesto.txt:4748–4945 runs the hidden actor-scoped reconciliation event only for an accepted Utopia Manifesto actor and reschedules within that actor chain. |
| No prohibited global periodic iteration | PASS | Event 015 adds no on_daily, on_weekly, on_monthly, or equivalent all-country iteration. |
| Terminal district cleanup | PASS | common/scripted_effects/015_utopia_manifesto_decision_effects.txt:1288–1343 ends Penal Works, clears every tracked state package, empties the array, clears counters/proofs, and removes active and durable district runtime flags and variables. |
| Decision/mission lifecycle cleanup | PASS | Prefire, evolution-consumption, main decision, reachability, district, settlement, island, and Necessary Ground runtime helpers remove their active missions and state on branch exit or terminal cleanup. |
| Localisation completeness | PASS | All 164 decision/mission identifiers and all nine category identifiers have names and descriptions. All 255 referenced custom-cost/effect-tooltip keys resolve. |
| Localisation encoding | PASS | All audited Event 015 English localisation files retain UTF-8 BOM encoding. |

## Industrial Housing scenario review

| Scenario | Expected source outcome | Result |
| --- | --- | --- |
| Homes Near Work, but no live housing emergency | Industrial Housing is unavailable | PASS |
| Live housing emergency, but no Homes Near Work | Industrial Housing is unavailable | PASS |
| Both prerequisites and a suitable state | A valid state target can be selected | PASS |
| Pressure is resolved before a target remains eligible | The live suitability predicate fails | PASS |
| The player inspects the decision | The description discloses both independent prerequisites | PASS |

The live-pressure trigger is based on the emergency-housing/refugee-municipality state of the country and the absence of an already owned industrial/refugee district. It does not infer pressure from Homes Near Work.

## District-loss scenario review

| Scenario | Expected source outcome | Result |
| --- | --- | --- |
| Active survey state is lost | Survey fails, project pointer and state survey data clear | PASS |
| Active build state is lost | Build fails, project pointer and state build data clear | PASS |
| Active charter state is lost | Charter fails, project pointer and route state data clear | PASS |
| Active Penal Works state is lost | Penal method and its state modifier/variables end | PASS |
| Completed chartered district is lost | One exact role-derived calling reversal occurs before state role flags clear | PASS |
| Reconciliation is invoked again for the same state | No second reversal occurs because tracked membership and charter role state are gone | PASS |
| Another Event 015 actor loses an unrelated state | Exact actor-array membership prevents cross-actor cleanup | PASS |
| Ordinary role district is lost while the Provision Ring remains valid | Ordinary proof is rebuilt; Provision Ring remains available | PASS |
| The island basis for the Provision Ring becomes invalid | Island reconciliation clears Provision Ring and dependent five-role proof | PASS |
| Remaining districts still satisfy proof | Rebuilt counts and proof remain valid | PASS |
| Remaining districts no longer satisfy proof | Current proof clears and the district network degrades | PASS |
| District buildings were completed before loss | Physical infrastructure/factories remain in the state | PASS |
| Historical charter conduct had changed the Ledger | Historical Ledger deltas remain; only current state-derived relief reverses | PASS |
| Terminal teardown runs | Every tracked district package and all country district runtime state clear | PASS |

## Necessary Ground completion review

The Necessary Ground family remains complete after the improvement tranche. It has seven case types backed by script constants: port, defensive corridor, essential resource, settlement/housing, island/refuge, reconstruction, and island lease.

| Scenario | Expected source outcome | Result |
| --- | --- | --- |
| Purchase targets a one-state country | The target is rejected; peaceful transfer cannot erase the target country | PASS |
| Ultimatum targets a one-state country | The transfer response is rejected on the live state-survival recheck | PASS |
| Enforcement targets a one-state country | Enforcement cannot start against a target that would not survive transfer | PASS |
| Purchase succeeds | The exact state transfers and the case enters bounded stewardship | PASS |
| Joint settlement, lease, association, or supply arrangement succeeds | The matching finite contract/mission path starts | PASS |
| A third party annexes the target before stewardship | The linked case invalidates and clears | PASS |
| A third party annexes the target during stewardship | The tracked successor is adopted where the contract permits it | PASS |
| The founder annexes the target | The case records its explicit coercive disposition and performs central cleanup | PASS |
| The founder is annexed | Reverse founder indexes drive exact teardown | PASS |
| Multiple founders track one target or state | Reverse arrays isolate each founder and its exact case data | PASS |
| A third party changes control of the exact tracked state | The state-control callback reconciles only linked founders | PASS |
| Peace ends with the exact enforcement objective achieved | The case enters stewardship | PASS |
| Peace ends without the exact objective or with an invalid target | The case terminates and clears | PASS |
| Renunciation, expiry, or explicit case cleanup occurs | Missions, wargoals, arrays, flags, event targets, and variables are removed | PASS |

Supporting implementation:

- common/scripted_triggers/015_utopia_manifesto_triggers.txt:1671–1918 validates exact state/target links, stored IDs, current ownership/control, target survival, and the single-active-target header.
- common/scripted_effects/015_utopia_manifesto_effects.txt:1461–1592 maintains the forward/reverse indexes and provides central case cleanup.
- common/scripted_effects/015_utopia_manifesto_effects.txt:2903–3105 handles peaceful settlement, exact-state enforcement, and post-peace resolution.
- common/scripted_effects/015_utopia_manifesto_effects.txt:3146–3251 handles annexation, successor adoption, founder extinction, and invalidation.
- common/scripted_effects/015_utopia_manifesto_effects.txt:3393–3447 records exact-state return/controller disposition.
- common/on_actions/015_utopia_manifesto_on_actions.txt:114–189 and 219–238 dispatch reverse-index annexation and state-control reconciliation.
- common/wargoals/015_utopia_manifesto_wargoals.txt restricts the war objective to the exact registered founder/state relationship.

No core-grant shortcut, permanent-claim shortcut, generic annexation fallback, or orphaned contract path was found.

## Source checks and references

The audit used the required offline references:

- paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md
- paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md
- paradox_wiki/Effects - Hearts of Iron 4 Wiki.md
- paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md
- paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md
- paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md
- paradox_wiki/On actions - Hearts of Iron 4 Wiki.md
- paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md

Vanilla documentation consulted:

- documentation/script_concept_documentation.md
- common/decisions/_documentation.md
- common/on_actions/_documentation.md
- common/script_constants/documentation.md
- documentation/effects_documentation.md
- documentation/triggers_documentation.md

Vanilla state-targeted decision, activate_targeted_decision, and on_state_control_changed precedents were also compared. The direct control-change handler matches the documented scopes: ROOT is the new controller, FROM is the old controller, and FROM.FROM is the state.

## Skipped validation

- The HOI4 decision/event MCP inspection tools were not exposed in this agent's available tool inventory.
- Live engine execution was outside this delegated read-only audit. This verdict is a source-level completion verdict.
- No logs were requested or searched.
- No gameplay, localisation, UI, spreadsheet, asset, or documentation file other than this handoff was modified.

These limitations did not produce a source-level blocker.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications: none.
- Omissions: none within the delegated decision/mission audit scope.
- Fallbacks: none.
- Blockers: none.
- Audit-driven source patches: none.

## Skills used

- chaos-redux-subagents
- chaos-redux-events
- hoi4-decisions-missions
- chaos-redux-improvement-loop

No skill was created or updated by this read-only audit.

## Frozen source hashes

The following SHA-256 hashes define the final audited source snapshot:

| SHA-256 | Source |
| --- | --- |
| 4678a6afe7208c16951305c711d41f6d74b2eec05c23f4c5fa28b5aa2e4a8b6f | common/decisions/015_utopia_manifesto_decisions.txt |
| aadccc05e45c66de08e673f9c48d8e19df9ff3bd82b5d62bbffb0b710f3a0d10 | common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt |
| 19a4872b7425b280b0074af47a5a02de9786cab6bde9d693063e4cf856d2f509 | common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt |
| feb02d3e2af05804a30d2c6ef4a1ebb647b3ced2dfe96cb6c8afed2e035a91e8 | common/decisions/categories/015_utopia_manifesto_categories.txt |
| 0eeedf55b22818d4452e18adbe75bb106bf45ffcd33cbf6d3573cab6125bc33a | common/scripted_effects/015_utopia_manifesto_decision_effects.txt |
| 4ef6c2adce52e46ef3adabf2bdf8a604b20f3cfc05452d69432358267c75ad30 | common/scripted_effects/015_utopia_manifesto_effects.txt |
| f10cff3babb246e0a5ea1ad225b22715ed841b42401b9115812134cdab2a38ea | common/scripted_effects/015_utopia_manifesto_reachability_effects.txt |
| c677159dd9f943520e2c4f923330abeceb9285f4cc96a187280ff4ba8f00d005 | common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt |
| 9b28aa9d37c81ee2f1dbb2543c61abbd3f60463d9f42b8e13dc9407223be84f5 | common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt |
| 0e027f7512bdf07dd04123ef97802235cd18db5d6f46e6de909d8376df7cce4d | common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt |
| da2b2c86a47979dde9b7cae022e4f1798bac6029955858ca90fddd8a9167fa75 | common/scripted_effects/015_utopia_manifesto_identity_effects.txt |
| 078ccd44ef44d768e1954b3beb914726417fa742a0fe35f8bc5c5938977998aa | common/scripted_effects/015_utopia_manifesto_country_effects.txt |
| f100894ec5564e3850d14a912db167a0af42cf85748d7d9ebd257204038fbaa3 | common/scripted_triggers/015_utopia_manifesto_triggers.txt |
| 4a32abe608ecceeb7bc23cdc2836a16e9d223b0ee5a5fee91907ead2c037c70f | common/scripted_triggers/015_utopia_manifesto_reachability_triggers.txt |
| 2ff6f9091934f2cca357db8dbc31b441ab62b5b8b12e41f8df0d608d1cf449f9 | common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt |
| d439adad44a446184b08a441a4d3a0dacee74a3078474e17382f0e3fada696c4 | common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt |
| 91229ea8fbcba5596f6c6b2d4affce10377d9a72b787c6a46c11a73d2bceb075 | common/scripted_triggers/015_utopia_manifesto_evolution_delivery_triggers.txt |
| 870516531db2a480be8c2f0626997e7b1a65c6fd4c35e796bb6049b93d84d8c9 | common/script_constants/015_utopia_manifesto_decision_constants.txt |
| a426f72ee144e8bbf940ffb46460777b8b69f6f2fbf8b1989c020a663cf901e1 | common/script_constants/015_utopia_manifesto_constants.txt |
| 3080751492e6ac3c1c8983822cd6202d403f24833d242e02065fde3a41baaba4 | common/script_constants/015_utopia_manifesto_settlement_constants.txt |
| 6c34a48b48bf3f047b9c2c5580f4521bd6139be7182bbabe3ecfc993341969ba | common/script_constants/015_utopia_manifesto_prefire_evolution_constants.txt |
| 2b883019089ac98ff550232fd9de3156b40a5bda3c170b05b74c9eb83059b6b2 | common/script_constants/015_utopia_manifesto_evolution_consumption_constants.txt |
| fce7820dbc4149c2a9e54007f8c824a2725b3e39da824a24b7881c119a2b65fd | common/on_actions/015_utopia_manifesto_on_actions.txt |
| d10a321c164924e6fe685cdecb4737d4f68729526856d8680d3a002787b5bae7 | events/015_utopia_manifesto.txt |
| d81e435349f9bcc1386b98e492d67eaa87f2d029886cb07b91588401a3314543 | common/wargoals/015_utopia_manifesto_wargoals.txt |
| de99f8f7cf191da4eea3580a84e37a19409b1e53d821bb557b8a89f5bfc22387 | common/dynamic_modifiers/015_utopia_manifesto_state_modifiers.txt |
| c1c729f4717129e8abb60303a79e6fe4318598e6ac0221c79c65faa1ffe4391c | common/achievements/chaos_redux_achievements.txt |
| 6e44014672139189c53bedb4dd441b9d27900d934a42b6f1fb2166287b6701ed | common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt |
| 6caa39b13c6e9865bcbf58d61f1db8dbd4c282ac2f50d2ad02c545ccca7d64dd | localisation/english/015_utopia_manifesto_l_english.yml |
| dcb6d839a88b0f163d01accdc51a7e88613c3a759220fe9bbfff5c7d8a0c9dd3 | localisation/english/015_utopia_manifesto_decision_completion_l_english.yml |
| 5d5e0aa9caaa1d39e5065ff7e43bb1c43c812f313e2eb22cb3954adb6d70215b | localisation/english/015_utopia_manifesto_events_l_english.yml |
| bbf1d8af6246fbf892f4a9d7b4b41e9fc94e8ff5a810588d74180d00cde85cf7 | localisation/english/015_utopia_manifesto_evolutions_l_english.yml |
| 0c40e00a906c6eb7eb072c8910591a614085735f7737ae2d7c629b2cd684edb4 | localisation/english/015_utopia_manifesto_evolution_consumption_l_english.yml |
| 71b11d239ff3d380cdf5e9bab3e0d50825e8e604d22671228b7bde97ac1f1514 | common/national_focus/015_utopia_manifesto_focus_tree.txt |
| e6db306460f20b84cb452faafc300d062a318cbd5b48eb01bb8a24da30658cbb | common/ai_strategy/015_utopia_manifesto_ai_strategy.txt |
| 84f1e322ef827edd4eedff68ba99e67ae61e6c4ed1172193cf77eb3f4d05326a | common/ideas/015_utopia_manifesto_ideas.txt |

These hashes were captured immediately before writing this handoff and were rechecked after the write.
