# Event 015 Decision and Mission Current-Snapshot Re-audit

Date: 2026-07-15  
Role: `chaosx_decision_mission_auditor`  
Mode: fresh source audit with small local correctness repairs  
Audited event: 015 — Utopia Manifesto  
Verdict: **PASS**

## Result

The current Event 015 decision and mission package passes the delegated completion audit. Three concrete correctness defects were found and repaired during the audit; no P0–P3 finding remains open in the audited surface.

| Finding | Pre-repair failure | Current disposition |
| --- | --- | --- |
| Association diplomacy attribution | Shared access/guarantee markers could make one founder revoke a relation created by another founder or remove a relation that predated Event 015. | Target-side creator arrays attribute access and guarantees to the exact founder. Cleanup revokes only that founder's recorded relation and clears summary flags only after the last recorded creator leaves. |
| Auxiliary contract payment atomicity | Static contract support and dynamic formation support were checked separately and deducted in sequence, so a stockpile between the maximum and the sum could lose some paid resources without receiving the contract. | One combined affordability trigger covers foundation manpower, infantry equipment, combined support equipment, army experience, motorized equipment, convoys, capacity, and a controlled deployment state. Formation payment/deployment succeeds first; only then are contract resources paid and transferred. All failure paths refund the decision's political power and consume no contract resources. |
| Prefire founder isolation | Global district/contact pointers, observer-side response flags, and a shared state marker could collide between simultaneous Event 015 founders. | District candidates and foreign contacts live only in founder-local scope arrays; `.108/.109` require exact founder-array membership; response flags live on the founder; and district selection relies only on the founder's array plus ownership/control. One founder's reselection or cleanup cannot clear another founder's state, contact, or response. |

No fallback or weaker substitute was used for any repair.

## Post-audit paid-focus and on-action rebaseline

The report was reopened after the paid-focus atomicity patch and rechecked against these current dependencies:

| Dependency | SHA-256 | Lines |
| --- | --- | ---: |
| `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05` | 4,119 |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | `c2b26e499078d0c7782e46db587d377d8d64cee02e372f2ae8e087c7cea7ea81` | 380 |

The decision and mission inventory remains exactly 121 decisions and 43 missions. All three decision source hashes are unchanged.

The current `on_state_control_changed` block has five direct conditional branches in this order:

1. A Fallout-guarded reverse-index branch snapshots `utopia_manifesto_case_state_founders` and `utopia_manifesto_association_charter_founders`, then delivers `.165` to every exact founder.
2. The existing district branch identifies the old Event 015 controller's tracked state and calls `utopia_manifesto_handle_district_state_control_loss`.
3. An unguarded ROOT branch refreshes dynamic costs for an accepted Event 015 new controller.
4. An unguarded FROM branch refreshes dynamic costs for an accepted Event 015 old controller.
5. A Fallout-guarded branch preserves the two ROOT/FROM Ledger refreshes and the two island-project reconciliation calls.

There are exactly two `utopia_manifesto_refresh_dynamic_costs` calls in the callback and neither is inside a Fallout guard. Necessary Ground, association, district, Ledger, island, and snapshot-cleanup paths each remain present exactly once at their dispatch layer. Event `.165` still validates the exact founder/state reverse link, validates the active Necessary Ground case, and calls the association-charter state handler. Brace parsing closes the full on-action block at depth zero.

Rebaseline verdict: **PASS**. The post-audit patch introduces no decision or mission callback regression, and this auditor made no gameplay edit during the rebaseline.

## Required references consulted

Repository guidance used:

- `hoi4-decisions-missions`
- `chaos-redux-events`
- `AGENTS.md`

Offline Paradox wiki pages consulted:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- Interface Modding
- Scripted GUI Modding

Vanilla documentation and precedents consulted:

- `common/decisions/_documentation.md`
- `common/on_actions/_documentation.md`
- `common/scripted_guis/_documentation.md`
- `common/script_constants/documentation.md`
- `documentation/script_concept_documentation.md`
- CHI variable-duration mission precedents
- BEL country-targeted decision precedents
- AST target-array decision precedents

The HOI4 domain MCP tools were not exposed in this agent's tool inventory. The audit therefore used the required offline references, vanilla source, and direct source inspection.

## Exact inventory

| Source | Decisions | Missions | Total |
| --- | ---: | ---: | ---: |
| `common/decisions/015_utopia_manifesto_decisions.txt` | 105 | 39 | 144 |
| `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` | 15 | 1 | 16 |
| `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt` | 1 | 3 | 4 |
| **Total** | **121** | **43** | **164** |

| Category | Decisions | Missions | Total |
| --- | ---: | ---: | ---: |
| Defense | 5 | 4 | 9 |
| District | 10 | 3 | 13 |
| Formation | 5 | 1 | 6 |
| Governance | 12 | 3 | 15 |
| Island | 17 | 4 | 21 |
| League | 13 | 4 | 17 |
| Ledger | 27 | 13 | 40 |
| Necessary Ground | 21 | 7 | 28 |
| Stewardship | 11 | 4 | 15 |
| **Total** | **121** | **43** | **164** |

The category registration file contains exactly nine Event 015 categories. The main decision file contains no misplaced `scripted_gui` attachment; the single intended attachment remains on `utopia_manifesto_ledger_category` in the category definition.

## Costs, durations, AI, scopes, and public UI

- **121/121 decisions** have explicit `ai_will_do` blocks.
- **43/43 missions** have `activation`, `available`, `cancel_trigger`, `cancel_effect`, and `timeout_effect` blocks.
- **43/43 missions** use `days_mission_timeout = var:...`; no Event 015 mission in the audited package uses a fixed timeout.
- **43/43 mission identifiers** have an explicit `remove_mission` terminal path in the Event 015 effect/event corpus.
- **43 targeted decisions** have both `target_root_trigger` and `target_trigger`.
- **10 targeted missions** have `target_trigger` and consume bounded state selectors or founder-local/prefilled arrays with the intended `FROM` scope.
- **114/121 decisions** charge political power. The seven no-cost controls are the six calling selectors and `decision_utopia_clear_necessary_ground_target`; none grants a material benefit.
- **101 decisions** use a custom resource cost: 85 main decisions, 15 evolution-policy consumers, and one prefire repair decision. All 101 have a matching payment path. The main file also has one political-power decision whose stability payment intentionally uses the prepared payment kernel without a custom-cost wrapper.
- The 101 custom-cost references resolve to **92 unique cost keys**. All **276** required base, `_blocked`, and `_tooltip` localisation keys exist.
- All **164** decision/mission names and all **164** descriptions exist. All **nine** category names and descriptions exist.
- The decision sources contain **290** `_tt` references resolving to **288 unique keys**; all 288 keys exist.
- All nine Event 015 English localisation files retain UTF-8 BOM encoding.

Exact-payment checks accept a stockpile equal to the cost. Dynamic military/institutional prices and all mission durations are prepared from variables or script constants; unsupported static-only fields retain their documented file-local constants.

## Necessary Ground route audit

The Necessary Ground package contains all seven configured case types:

1. port access
2. defensive corridor
3. essential resource
4. settlement and housing
5. island or capital refuge
6. reconstruction zone
7. island project lease

All six peaceful methods are implemented and publicly surfaced: purchase, long supply contract, lease, settlement agreement, joint administration, and association. Revision, conversion, renunciation, ultimatum, and enforcement routes are also present.

The exact-state enforcement path is founder-specific:

- the founder stores the exact selected state ID;
- the state reverse array records the exact founder;
- the wargoal generator injects only that stored state ID;
- the wargoal `take_states` filter requires the active-case marker, exact founder membership, and ownership by the original target;
- settlement, target disappearance, annexation, peace, state-control change, expiry, renunciation, and terminal teardown enter centralized cleanup.

No core grant, permanent claim, generic annexation shortcut, or untracked state-transfer fallback exists.

### Association reverse links and diplomacy ownership

Country and state reverse indexes remain exact-founder arrays. The current diplomacy ownership layer adds:

- `utopia_manifesto_association_created_access_founders`
- `utopia_manifesto_association_created_guarantee_founders`
- `utopia_manifesto_apply_root_association_diplomacy`
- `utopia_manifesto_remove_root_association_diplomacy`

Creation records a founder only when Event 015 creates that specific relation. Pre-existing access or guarantees are preserved. Failure of association duties, voluntary withdrawal, association-charter owner change, partner annexation, founder terminal cleanup, and annexed-target cleanup remove only the exact founder's recorded relations. Shared target flags and arrays clear only after the last exact founder leaves.

## Evolution and prefire consumers

The evolution-consumption file contains **15** decision inputs and one dynamic mission. Every choice appears in all five required dispatch surfaces:

| Dispatch surface | Covered choices |
| --- | ---: |
| Supported-choice trigger | 15/15 |
| Cost payment map | 15/15 |
| Duration map | 15/15 |
| Start-effect map | 15/15 |
| Completion-effect map | 15/15 |

The prefire package contains one paid decision and three dynamic missions. The domestic-shore repair consumes its disclosed resources. Prefire success, timeout, cancellation, package disablement, and terminal teardown all clear their missions and founder-local runtime state.

The foreign observer chain is multiplayer-safe in the current snapshot:

- founder A and founder B may each store the same observer in their own `utopia_manifesto_prefire_foreign_contacts` array;
- `.108` accepts the observer only when `FROM` founder's array contains `ROOT` observer;
- the response flag is written to that exact founder;
- `.109` accepts only when the founder array contains `FROM` observer and reads/clears only that founder's response;
- founder A's cleanup never clears founder B's array or response.

The district candidate follows the same isolation rule through `utopia_manifesto_prefire_district_candidate_states`; no global event target or shared state flag remains. The only Event 015 global event target is `utopia_manifesto_latest_actor`, which is historical event-log state rather than decision or mission runtime.

## Paid military growth and prohibited benefits

There are eight `create_unit` templates, all inside `utopia_manifesto_deploy_paid_formation`. That helper has one caller, `utopia_manifesto_execute_paid_military_growth`, after affordability succeeds. A paid batch consumes dynamically prepared manpower, infantry equipment, support equipment, and army experience and requires a controlled deployment state.

The auxiliary contract additionally requires and consumes the disclosed static support equipment, motorized equipment, and convoys. Its combined-support test prevents the dynamic formation and static contract from spending the same support stockpile twice.

The audited Event 015 decision/effect/event corpus contains:

- zero `add_core_of` effects;
- zero state-claim effects;
- zero `load_oob` calls;
- zero division creation outside the paid formation helper.

## Cleanup, callbacks, and recurring work

- Mission completion, timeout, cancellation, exceptional invalidation, and terminal teardown cover all 43 mission identifiers.
- `on_annex`, founder terminal event `.164`, and state-control event `.165` use reverse indexes to reach only affected founders.
- Necessary Ground country/state links, association diplomacy creator arrays, evolution runtime, prefire arrays, dynamic-growth variables, active wargoals, and target arrays have explicit cleanup.
- Event 015 introduces no `on_daily`, `on_weekly`, `on_monthly`, or equivalent all-country recurring repair scan.

## Multiplayer isolation matrix

| Scenario | Result | Current behavior |
| --- | --- | --- |
| Association relation predates Event 015 | PASS | No creator entry is recorded, so Event 015 does not revoke it. |
| Founder A creates access/guarantee; founder B joins later | PASS | Only A is recorded for A's relations; B receives its own creator entry only for a relation B actually creates. |
| Founder A cleans up while B remains | PASS | Only A's diplomacy and reverse links are removed; B's entries and target summary state remain. |
| Association host changes owner | PASS | Exact charter founders are snapshotted and reconciled; diplomacy removal uses the corresponding founder entry. |
| Partner or founder is annexed | PASS | Reverse-index callbacks remove only the linked founder/target records before final target-side array cleanup. |
| Two founders select the same Necessary Ground country/state | PASS | Country and state reverse arrays retain both founders; each founder's cleanup and exact-state wargoal remain isolated. |
| Two founders select the same prefire observer | PASS | Founder-local contact arrays and founder-side response flags keep `.108/.109` chains independent. |
| A selected district state transfers between founders | PASS | No shared candidate flag exists; the old founder can clear only its local array, while the new founder's local array remains intact. |

## Auditor-authored source repairs

The audit made small, local edits in these shared files:

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt`
- `events/015_utopia_manifesto.txt`
- `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml`

The edits are limited to the three repaired findings described above and their player-facing affordability wording. No asset, focus, idea, spreadsheet, or canonical specification was changed by this auditor.

## Frozen 42-file Event 015 source snapshot

The following SHA-256 ledger covers all `015_utopia_manifesto*` files in the audited AI, decision, category, on-action, constant, scripted-effect, scripted-GUI, scripted-localisation, scripted-trigger, wargoal, event, and English-localisation roots.

| SHA-256 | Lines | Source |
| --- | ---: | --- |
| `e6db306460f20b84cb452faafc300d062a318cbd5b48eb01bb8a24da30658cbb` | 288 | `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` |
| `5dcd41ef8669a4384fedb2efa9761e657fe8a5ff8ea686e45046005fd23d17fd` | 5708 | `common/decisions/015_utopia_manifesto_decisions.txt` |
| `aa8c813015cacbf2b5d588b82c39d3b440ed9e83f0009a6a048f83e5d0f82ed4` | 543 | `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` |
| `04c46f18ad0c23f70303d75d0d00bb45afcaaf9ab5d877ba01bfe1e9754e3347` | 110 | `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt` |
| `feb02d3e2af05804a30d2c6ef4a1ebb647b3ced2dfe96cb6c8afed2e035a91e8` | 120 | `common/decisions/categories/015_utopia_manifesto_categories.txt` |
| `c2b26e499078d0c7782e46db587d377d8d64cee02e372f2ae8e087c7cea7ea81` | 380 | `common/on_actions/015_utopia_manifesto_on_actions.txt` |
| `a426f72ee144e8bbf940ffb46460777b8b69f6f2fbf8b1989c020a663cf901e1` | 669 | `common/script_constants/015_utopia_manifesto_constants.txt` |
| `f53c2eade8230ac93c8af734e41b01b42fe861a3bdb2ec6944d048545af67326` | 143 | `common/script_constants/015_utopia_manifesto_country_constants.txt` |
| `870516531db2a480be8c2f0626997e7b1a65c6fd4c35e796bb6049b93d84d8c9` | 236 | `common/script_constants/015_utopia_manifesto_decision_constants.txt` |
| `2b883019089ac98ff550232fd9de3156b40a5bda3c170b05b74c9eb83059b6b2` | 45 | `common/script_constants/015_utopia_manifesto_evolution_consumption_constants.txt` |
| `31d05528fbed483237d761f364a4316c3bf79246852887ddf5959846c0f127f6` | 162 | `common/script_constants/015_utopia_manifesto_narrative_constants.txt` |
| `6c34a48b48bf3f047b9c2c5580f4521bd6139be7182bbabe3ecfc993341969ba` | 85 | `common/script_constants/015_utopia_manifesto_prefire_evolution_constants.txt` |
| `3080751492e6ac3c1c8983822cd6202d403f24833d242e02065fde3a41baaba4` | 121 | `common/script_constants/015_utopia_manifesto_settlement_constants.txt` |
| `b7875f02464267b6cd4435447005f6f8991255f2e7cb38d681d25d43af3478c4` | 17 | `common/script_constants/015_utopia_manifesto_super_event_constants.txt` |
| `bab3fc080661918b35d88b0418a4067ca716e458a63e36a86aa37a5da6f886e2` | 254 | `common/scripted_effects/015_utopia_manifesto_achievement_effects.txt` |
| `0e027f7512bdf07dd04123ef97802235cd18db5d6f46e6de909d8376df7cce4d` | 288 | `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt` |
| `078ccd44ef44d768e1954b3beb914726417fa742a0fe35f8bc5c5938977998aa` | 496 | `common/scripted_effects/015_utopia_manifesto_country_effects.txt` |
| `0eeedf55b22818d4452e18adbe75bb106bf45ffcd33cbf6d3573cab6125bc33a` | 2601 | `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` |
| `ed44d3a9892061bb77ebe6e6039be8d7a6a1bcc5f292091c4e5ede32b39d2b8d` | 6275 | `common/scripted_effects/015_utopia_manifesto_effects.txt` |
| `9b28aa9d37c81ee2f1dbb2543c61abbd3f60463d9f42b8e13dc9407223be84f5` | 1005 | `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt` |
| `da2b2c86a47979dde9b7cae022e4f1798bac6029955858ca90fddd8a9167fa75` | 967 | `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` |
| `1d757540eab0082a09df425578e4208e09cb364832d7b170591ea763d50c60c4` | 536 | `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt` |
| `f10cff3babb246e0a5ea1ad225b22715ed841b42401b9115812134cdab2a38ea` | 146 | `common/scripted_effects/015_utopia_manifesto_reachability_effects.txt` |
| `d4fd6ada2ee953c08da529fd7b890a23ed7ab5ac92d32b13524475130bf7d955` | 68 | `common/scripted_effects/015_utopia_manifesto_super_event_effects.txt` |
| `30993a52ee46e7c9cb56082c322fa942949c3f28ea8815127b67187da3028c99` | 115 | `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` |
| `6e44014672139189c53bedb4dd441b9d27900d934a42b6f1fb2166287b6701ed` | 800 | `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt` |
| `d439adad44a446184b08a441a4d3a0dacee74a3078474e17382f0e3fada696c4` | 314 | `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt` |
| `91229ea8fbcba5596f6c6b2d4affce10377d9a72b787c6a46c11a73d2bceb075` | 33 | `common/scripted_triggers/015_utopia_manifesto_evolution_delivery_triggers.txt` |
| `ba4ac12603651718c633a0b3c90b530097ceadcf16969fadcec69c77508a1c5e` | 86 | `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt` |
| `4a32abe608ecceeb7bc23cdc2836a16e9d223b0ee5a5fee91907ead2c037c70f` | 206 | `common/scripted_triggers/015_utopia_manifesto_reachability_triggers.txt` |
| `d0c304d2b4cd5dccd72b40cff8e9ab4caa3beab58838ce68057eacf31bcfe9af` | 2882 | `common/scripted_triggers/015_utopia_manifesto_triggers.txt` |
| `d81e435349f9bcc1386b98e492d67eaa87f2d029886cb07b91588401a3314543` | 35 | `common/wargoals/015_utopia_manifesto_wargoals.txt` |
| `a7d27155c463424f19fb1d661356a42ccb90cc4b29f8e42a03ea78ba86b9b164` | 5071 | `events/015_utopia_manifesto.txt` |
| `42bbc60ef46e9f3c8233c9842a0646b02a72560cd77649195b739fb57416ae92` | 223 | `localisation/english/015_utopia_manifesto_country_package_l_english.yml` |
| `01452765d2413b06844a46aaba1c5e0a552fbd2a7ea319b70d59262dbd83c445` | 699 | `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml` |
| `5d5e0aa9caaa1d39e5065ff7e43bb1c43c812f313e2eb22cb3954adb6d70215b` | 576 | `localisation/english/015_utopia_manifesto_events_l_english.yml` |
| `fc4b71c1190ab45a3d6723a30b7256cee228871a513476345658982b20e534b1` | 101 | `localisation/english/015_utopia_manifesto_evolution_consumption_l_english.yml` |
| `bbf1d8af6246fbf892f4a9d7b4b41e9fc94e8ff5a810588d74180d00cde85cf7` | 19 | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` |
| `c8d34f7e48facc7eac266d64383af3fa66e93c7a9a48d4d46ba2e96a8e570828` | 353 | `localisation/english/015_utopia_manifesto_focus_l_english.yml` |
| `0591a362d9ed653e132915c4d4a83e019048e5cc8fde2aa0505eca7d53be702a` | 137 | `localisation/english/015_utopia_manifesto_ideas_l_english.yml` |
| `a80a6dbaf7e2591a46e836fcbd419d3c7dfac324ccc1f7ba118266678e3fdaa5` | 485 | `localisation/english/015_utopia_manifesto_l_english.yml` |
| `8f14e4fb22578e942ba5019e1022032b12a794c464e61fcef8d7d01bb5527e32` | 21 | `localisation/english/015_utopia_manifesto_super_event_l_english.yml` |

## Evidence boundary and remaining risks

This is a source-level completion audit. It proves the current definitions, dispatch maps, reverse indexes, payment ordering, and cleanup paths present in source; it cannot directly observe engine scheduling or multiplayer interleaving at runtime. No unresolved source defect was found within that evidence boundary.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications: none.
- Omissions: none within the delegated decision/mission scope.
- Fallbacks: none.
- Blockers: none.
- Remaining open P0–P3 findings: none.
- Commit: none; the parent agent retains commit ownership.

## Skills used

- `hoi4-decisions-missions`
- `chaos-redux-events`

No skill was created or updated during this audit.
