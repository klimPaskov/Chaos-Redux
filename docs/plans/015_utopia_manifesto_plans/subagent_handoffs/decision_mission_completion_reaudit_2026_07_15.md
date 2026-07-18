# Event 015 Decision and Mission Completion Re-audit

Date: 2026-07-15  
Agent role: `chaosx_decision_mission_auditor`  
Mode: read-only audit; this file is the only audit-authored change  
Verdict: **FAIL**

## Result

The live Event 015 package contains the full expected inventory of **121 decisions**, **43 missions**, and **9 decision categories**. All 121 decisions have `ai_will_do`. All 43 missions have an activation gate, a variable-backed duration, a cancellation trigger and effect, and a timeout outcome. Decision/category names and descriptions, custom cost text, custom effect tooltips, and referenced event localisation are present.

The re-audit found **one open P1 lifecycle defect** with two reproducible target-disappearance paths. There are no open P0, P2, or P3 findings in this audit. Because the defect can either strand an enforcement case indefinitely or leave acquired territory outside the required stewardship/status lifecycle, the decision and mission package cannot receive a completion PASS.

## Open finding

### [P1] Target disappearance has no reverse founder notification or acquired-state disposition

The selected target is authoritative only from the founder side. `utopia_manifesto_case_candidate_is_valid` does not exclude one-state countries at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:1675-1694`, while `utopia_manifesto_active_case_target_is_live` requires that the exact saved target still exists at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:1746-1758`. The target does not retain a reverse pointer or array identifying the founder whose case owns it.

Two paths expose the missing contract:

1. **Third-party annexation during enforcement can strand the case indefinitely.** `common/on_actions/015_utopia_manifesto_on_actions.txt:115-171` receives only annexer `ROOT` and annexed `FROM`; it invalidates a case only when the annexer itself is the Event 015 founder at line 141. It cannot notify a different founder that has the annexed country in `utopia_manifesto_active_case_targets`. At the same time, `utopia_manifesto_mark_enforcement_war_active` removes `mission_utopia_need_case_expiry` at `common/scripted_effects/015_utopia_manifesto_effects.txt:2947-2956`. If a third party removes the target, there is therefore no remaining expiry mission and no reverse callback. `utopia_manifesto_resolve_enforcement_after_peace` at `common/scripted_effects/015_utopia_manifesto_effects.txt:2960-2991` has no invalid-target terminal branch; its stewardship start cannot pass `utopia_manifesto_active_need_case_is_valid` once the target no longer exists.
2. **An ownership-transfer settlement can remove a one-state target and bypass stewardship.** Purchase is allowed for the mapped case types without a target state-count condition at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:1864-1872`. `utopia_manifesto_apply_purchase_settlement` transfers the exact state to the founder at `common/scripted_effects/015_utopia_manifesto_effects.txt:1940-1945`; accepted ultimatum uses the same purchase-style transfer through `utopia_manifesto_accept_case_settlement` at `common/scripted_effects/015_utopia_manifesto_effects.txt:2814-2858`. If that transfer removes the target's last owned state, target validity fails. The annex hook can then call generic invalidation, but `utopia_manifesto_invalidate_active_need_case` at `common/scripted_effects/015_utopia_manifesto_effects.txt:3042-3056` only restores territory when stewardship was already active. If stewardship never started because the target disappeared, the exact state remains with the founder while the case is cleared. This skips provision, charter, status, return, association, and integration.

Impact: the first path leaves a stale active-case lock, selected target/state arrays, enforcement state, and related decisions with no bounded terminal mission. The second path can create permanent acquisition without the accepted post-acquisition stewardship or an explicit successor/disposition outcome. Neither is a voluntary renunciation, so generic renunciation evidence would also be incorrect.

### Required invariant

An exact Necessary Ground target may not disappear while leaving either:

- a founder-side active case with no bounded terminal path; or
- an acquired state held by the founder outside stewardship or an explicit, documented successor/disposition result.

Target disappearance must be event-driven and exact. It must not be repaired with a recurring `every_country` scan, silent integration, arbitrary transfer, voluntary-renunciation flags, or an undocumented fallback.

### Safe patch recommendation

1. When `utopia_manifesto_open_need_case_against_from` records the target, also register the founder in a target-side array such as `utopia_manifesto_case_founders`. Remove the founder from that reverse array in the central case cleanup before clearing the founder-side target array.
2. In `on_annex`, have annexed `FROM` iterate only its recorded founder array and call a method-aware invalidation/disposition helper in each exact founder scope. This remains a one-shot hook and introduces no world scan.
3. Add an invalid-target terminal branch to `utopia_manifesto_resolve_enforcement_after_peace`. It must remove the exact case wargoal and missions and then either restore/resolve the exact state through an approved disposition or close a pre-acquisition case without recording voluntary renunciation.
4. Until an approved last-state disposition exists, gate ownership-transfer purchase, accepted ultimatum, and enforcement against targets for which the selected state is the last owned state. The fuller alternative is to create an explicit successor/municipality or standalone stewardship contract before the transfer, preserving an exact lawful return/status destination.
5. Keep all cleanup centralized and idempotent. Do not merely relax `exists = yes`: return, association, guarantees, access, achievement evidence, and status outcomes all require a valid recorded counterparty or a deliberately created successor.

## Live correction re-audited during this pass

The audit initially found that port and essential-resource acquisitions could invalidate themselves because the active-state trigger re-ran founder-relative candidate relevance after the acquisition had satisfied that need. The parent corrected this while the audit was active.

The current `utopia_manifesto_active_case_state_is_live` at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:1760-1799` now:

- continues to require the exact flagged state and saved state ID;
- permits the live structural relevance path before settlement;
- permits an accepted settlement, active enforcement war, or stewardship stage to retain the state only while the founder owns or controls it; and
- retains the existing owner/controller bounds to the founder or exact active target.

That correction closes the self-invalidation path for a still-live target and passes this re-audit. It does not close the separate target-disappearance finding above. The trigger file changed from the audit-opening SHA-256 `6d74b0822dca7c08a6104e529c4508b4ea5b627b2ccc5ce0ab25b09d9219e1fb` to the final audited hash recorded below.

## Coverage evidence

| Surface | Result | Evidence |
|---|---|---|
| Inventory | PASS | 105 decisions and 39 missions in the main file, 15 decisions and 1 mission in evolution consumption, and 1 decision and 3 missions in prefire evolution: 121 decisions and 43 missions total. Nine registered categories are present. |
| Decision AI | PASS | Every one of the 121 decision blocks contains `ai_will_do`; targeted choices include target-sensitive penalties/preferences where required. |
| Mission lifecycle | PASS except finding | Every mission has activation, `days_mission_timeout = var:...`, timeout outcome, cancel trigger, and cancel effect. The open finding is an external target-disappearance callback gap, not a missing mission field. |
| Calling mutex | PASS | All four shortage methods, calling sustainment, and Second Trade claim `utopia_manifesto_calling_mission_active`; success, failure, cancellation, and total cleanup release it. The long-lived emergency levy expiry is deliberately separate and does not overwrite selected-calling runtime. |
| Exact affordability | PASS | No remaining decision affordability gate uses strict `resource > constant:utopia_manifesto_decision_cost.*`. Custom payment gates accept equality through inverted `<` checks or explicit `greater_than_or_equals`, matching the paid amount. Deliberate district maintenance buffers are separate from purchase affordability. |
| Localisation coverage | PASS | All 164 unique decision/mission identifiers and all 9 categories have both name and `_desc` keys. All 255 unique `custom_cost_text`/`custom_effect_tooltip` references resolve. All 466 unique event title/description/option-name references resolve. |
| Necessary Ground model | FAIL on finding | Domestic review, exact selected country/state arrays, seven case types, peaceful ladder, bilateral responses, revision, ultimatum, enforcement, wargoal removal, expiry, renunciation, lease/joint conversion, three finite foreign-term missions, stewardship, return, integration, revolt, and cleanup are present. No core or permanent claim grant was found. Target disappearance is not lifecycle-safe. |
| Reachability `.110-.115` | PASS | Safe country selection and firing helpers exist in `common/scripted_effects/015_utopia_manifesto_reachability_effects.txt:10-101`; all six event blocks are live at `events/015_utopia_manifesto.txt:4190-4460`. |
| Reachability `.160-.162` | PASS | League-news, Necessary Ground war-news, and assigned-colony revolt milestones are recorded and dispatch their events through `common/scripted_effects/015_utopia_manifesto_reachability_effects.txt:103-146`; event blocks exist at `events/015_utopia_manifesto.txt:4950-5000`. |
| Collapse and repeal `.120` | PASS | Deliberate repeal enters through `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt:10-15`; regime collapse is guarded at lines 17-37 and is called only by capitulation/government-change hooks. Ordinary war only refreshes the Ledger. The snapshot, colony, practical legacy, book, league-successor, and final teardown chain is present. |
| Evolution `.105-.109`, `.117` | PASS | All fifteen active interpretations call the shared dispatcher. Prefire choices and stage tokens route through the same consumption effects, including delayed Perfect Island consumption after route resolution. Cleanup is idempotent. |
| World iteration | PASS | No `on_daily`, `on_weekly`, `on_monthly`, or tag-wide recurring equivalent exists. Candidate/reaction country iteration is invoked only by explicit one-shot preparation or event helpers. |

## Files examined

Gameplay and localisation surfaces:

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt`
- `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt`
- `common/decisions/categories/015_utopia_manifesto_categories.txt`
- `common/scripted_effects/015_utopia_manifesto_decision_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_reachability_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_identity_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_country_effects.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_reachability_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_evolution_delivery_triggers.txt`
- `common/script_constants/015_utopia_manifesto_decision_constants.txt`
- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/script_constants/015_utopia_manifesto_settlement_constants.txt`
- `common/script_constants/015_utopia_manifesto_prefire_evolution_constants.txt`
- `common/script_constants/015_utopia_manifesto_evolution_consumption_constants.txt`
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
- `events/015_utopia_manifesto.txt`
- `common/wargoals/015_utopia_manifesto_wargoals.txt`
- `common/opinion_modifiers/015_utopia_manifesto_opinion_modifiers.txt`
- `common/dynamic_modifiers/015_utopia_manifesto_state_modifiers.txt`
- `common/ideas/015_utopia_manifesto_ideas.txt`
- `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt`
- `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt`
- `localisation/english/015_utopia_manifesto_l_english.yml`
- `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml`
- `localisation/english/015_utopia_manifesto_events_l_english.yml`
- `localisation/english/015_utopia_manifesto_evolutions_l_english.yml`

Design sources examined:

- all eight Event 015 source-spec parts;
- decision/mission, target-eligibility, completion-coverage, achievement, country-package, and focus-route matrices;
- the Event 015 decision/mission implementation prompt and goal prompt;
- the formal improvement-loop addendum;
- prior implementation handoffs and prior audits as historical checklists only.

Required references examined:

- offline wiki: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding;
- vanilla `common/decisions/_documentation.md`;
- vanilla `documentation/effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`;
- vanilla `common/script_constants/documentation.md`;
- representative vanilla decision implementations in `GER.txt` and `AUS.txt`.

## Final audited SHA-256 snapshot

| File | SHA-256 |
|---|---|
| `common/decisions/015_utopia_manifesto_decisions.txt` | `a8d9c6c9770ba38fd5d3a774314d0a58c43230e5fdc2088345280c6f28732881` |
| `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` | `aadccc05e45c66de08e673f9c48d8e19df9ff3bd82b5d62bbffb0b710f3a0d10` |
| `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt` | `19a4872b7425b280b0074af47a5a02de9786cab6bde9d693063e4cf856d2f509` |
| `common/decisions/categories/015_utopia_manifesto_categories.txt` | `feb02d3e2af05804a30d2c6ef4a1ebb647b3ced2dfe96cb6c8afed2e035a91e8` |
| `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | `8a24ef272bbef9cc82e9383ad9e9662c3b5d638b738e1985d7d6a0945bb046ed` |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | `056cd6c600f3d81b3e68cbcc46b3a9d8cf2eb9c7fee970ada7e1e4583a3b8c67` |
| `common/scripted_effects/015_utopia_manifesto_reachability_effects.txt` | `f10cff3babb246e0a5ea1ad225b22715ed841b42401b9115812134cdab2a38ea` |
| `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt` | `c677159dd9f943520e2c4f923330abeceb9285f4cc96a187280ff4ba8f00d005` |
| `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt` | `9b28aa9d37c81ee2f1dbb2543c61abbd3f60463d9f42b8e13dc9407223be84f5` |
| `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt` | `091d3ec735206b873a9c9781389156cb8d41eaee1404efca11adcd8a5d2b514c` |
| `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` | `da2b2c86a47979dde9b7cae022e4f1798bac6029955858ca90fddd8a9167fa75` |
| `common/scripted_effects/015_utopia_manifesto_country_effects.txt` | `078ccd44ef44d768e1954b3beb914726417fa742a0fe35f8bc5c5938977998aa` |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | `533f60711dd9c4dd2278dc8531f429ea8cb42a2b1b685870187056b70ffd0056` |
| `common/scripted_triggers/015_utopia_manifesto_reachability_triggers.txt` | `4a32abe608ecceeb7bc23cdc2836a16e9d223b0ee5a5fee91907ead2c037c70f` |
| `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt` | `2ff6f9091934f2cca357db8dbc31b441ab62b5b8b12e41f8df0d608d1cf449f9` |
| `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt` | `d439adad44a446184b08a441a4d3a0dacee74a3078474e17382f0e3fada696c4` |
| `common/scripted_triggers/015_utopia_manifesto_evolution_delivery_triggers.txt` | `91229ea8fbcba5596f6c6b2d4affce10377d9a72b787c6a46c11a73d2bceb075` |
| `common/script_constants/015_utopia_manifesto_decision_constants.txt` | `870516531db2a480be8c2f0626997e7b1a65c6fd4c35e796bb6049b93d84d8c9` |
| `common/script_constants/015_utopia_manifesto_constants.txt` | `334333761c0d5b2354f774c50d6d761731ac90405e631575bccca7d1e8dd6b4c` |
| `common/script_constants/015_utopia_manifesto_settlement_constants.txt` | `3080751492e6ac3c1c8983822cd6202d403f24833d242e02065fde3a41baaba4` |
| `common/script_constants/015_utopia_manifesto_prefire_evolution_constants.txt` | `6c34a48b48bf3f047b9c2c5580f4521bd6139be7182bbabe3ecfc993341969ba` |
| `common/script_constants/015_utopia_manifesto_evolution_consumption_constants.txt` | `2b883019089ac98ff550232fd9de3156b40a5bda3c170b05b74c9eb83059b6b2` |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | `a1ee56233cc003bbd755c7cd514f6d1b2645c8a83d13933903374021a5ffc72d` |
| `events/015_utopia_manifesto.txt` | `3479c36b2bdba6dff1b4a9d0f5d564b3c7e8533a426b5186c8e9f9c318ade7cc` |
| `common/wargoals/015_utopia_manifesto_wargoals.txt` | `c318c436fe19942c160ad6624a8b205defbaba0f1068d98be436aa14d8ba9d59` |
| `common/opinion_modifiers/015_utopia_manifesto_opinion_modifiers.txt` | `5a7f8f83fd9d55f12a0b5549ad71695c51b095db5a4ade0167730cb719af9bb1` |
| `common/dynamic_modifiers/015_utopia_manifesto_state_modifiers.txt` | `de99f8f7cf191da4eea3580a84e37a19409b1e53d821bb557b8a89f5bfc22387` |
| `common/ideas/015_utopia_manifesto_ideas.txt` | `84f1e322ef827edd4eedff68ba99e67ae61e6c4ed1172193cf77eb3f4d05326a` |
| `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` | `e6db306460f20b84cb452faafc300d062a318cbd5b48eb01bb8a24da30658cbb` |
| `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt` | `6e44014672139189c53bedb4dd441b9d27900d934a42b6f1fb2166287b6701ed` |
| `localisation/english/015_utopia_manifesto_l_english.yml` | `8af7e8a492af30b63b5c68f2c108a7967360f00775b9c5f4d84459b55435e55e` |
| `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml` | `e04a1fc8e55341711286227cdeadf7376ae928d17708e8002bc46ecf0ff8f6e0` |
| `localisation/english/015_utopia_manifesto_events_l_english.yml` | `5d5e0aa9caaa1d39e5065ff7e43bb1c43c812f313e2eb22cb3954adb6d70215b` |
| `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `bbf1d8af6246fbf892f4a9d7b4b41e9fc94e8ff5a810588d74180d00cde85cf7` |

## Simplifications, omissions, and blockers

- No audit simplification or fallback was used.
- The one P1 target-disappearance lifecycle defect above is the sole decision/mission completion blocker found in the final audited snapshot.
- No gameplay, localisation, asset, or spreadsheet source was edited by this auditor.
