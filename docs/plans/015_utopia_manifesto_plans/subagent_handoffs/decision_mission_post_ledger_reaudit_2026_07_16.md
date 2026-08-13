# Event 015 Decision and Mission Post-Ledger Re-audit

Date: 2026-07-16  
Auditor role: `chaosx_decision_mission_auditor`  
Audit mode: fresh static source audit after the late Ledger state integration  
Decision/mission verdict: **PASS**

## Verdict and scope boundary

No P0, P1, P2, or P3 defect remains in the frozen Event 015 decision/mission surface. The exact inventory remains **121 decisions, 43 missions, and 9 categories**. Costs and payment, target selection, variable mission durations, terminal outcomes, AI, per-system cleanup, full teardown, Necessary Ground, district role/phase state, case cards, and Choice/Assignment presentation all pass the checks below.

No gameplay patch was warranted. This report is the only file created by this auditor.

This PASS is limited to decision and mission mechanics plus the script-to-GUI state binding needed to audit them. It does not replace the separate asset-quality/provenance audit. The existing asset requirement-to-runtime crosswalk also predates the live Ledger integration; that documentation discrepancy is recorded below but is not a defect in the decision/mission implementation.

## Required references used

- `AGENTS.md`.
- Repo skills, read in full: `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-events`.
- All eight Event 015 specification parts, all Event 015 matrices, the accepted improvement addendum, the source-of-truth map, and the current resume record.
- Prior decision reports: `decision_mission_completion_current_reaudit_2026_07_15.md` and `decision_mission_post_balance_reaudit_2026_07_16.md`.
- Late Ledger report: `ledger_state_architecture_reaudit_2026_07_16.md`.
- Required offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding.
- Official game documentation: decision, scripted-GUI, on-action, script-constant, script-concept, effect, and trigger documentation.
- Vanilla precedents: YUG variable mission timers and current variable-backed timed-country-flag implementations.

The `hoi4-agent-tools` MCP domain was not exposed in this session, so no MCP render or event/decision query could be run. The audit therefore used direct source inspection and explicit structural/lifecycle enumeration.

## Frozen delta from the previous decision PASS

The previous post-balance ledger contains 45 text sources and four presentation binaries. **Forty-one of 49 entries are byte-identical.** Eight text sources changed for the accepted late Ledger state integration:

| Source | Previous lines/hash | Current lines/hash | Audited disposition |
| --- | --- | --- | --- |
| `common/script_constants/015_utopia_manifesto_constants.txt` | 670 / `75abb0707e63730e871d7582ed6aaa6b275d3a0bc0a37ab5b7e4e5bfeb5ff700` | 671 / `73e6986f6b36094694b311347f0bb39299156c4f9c1f4627e67e0306d323d9e0` | Central seven-day district-plan presentation duration. |
| `common/script_constants/015_utopia_manifesto_decision_constants.txt` | 236 / `870516531db2a480be8c2f0626997e7b1a65c6fd4c35e796bb6049b93d84d8c9` | 239 / `b54d543548255f116fe73aa055b274b845a4dbc7dba6fa0d8bcd083ea72df1d1` | Seven distinct durable district presentation roles. |
| `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | 2,601 / `0eeedf55b22818d4452e18adbe75bb106bf45ffcd33cbf6d3573cab6125bc33a` | 2,612 / `c743be8d9a124710eb1f1e00b8c13b0197e50c0f2bb9d9b5e9bc55f5752e467c` | Role assignment, timed planned-state producer, and teardown cleanup. |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | 6,331 / `fd7b62671d1f49eb00363316914c6893463c08f4ea24a2c972d37093a8c87cd7` | 6,334 / `c174887733b31f8f84596826c5e6a7d511d9ef7db72410c0c34946b628e827d2` | Island-role producers and successful-new-case expiration reset. |
| `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` | 121 / `de37ba78051436a69abdc4a79799749210b9e208b9d3a5396ea012206fde8dbd` | 395 / `70325293fc61422eb59d717f8c10a5fb9555e680d0207e2d7be9f3d7cd5fd128` | Ten case-card, seven role-card, and six phase-overlay visibility bindings. |
| `events/015_utopia_manifesto.txt` | 5,071 / `a7d27155c463424f19fb1d661356a42ccb90cc4b29f8e42a03ea78ba86b9b164` | 5,076 / `8e3e0c24ebb7c243761c4391965909b7f5d823878a07ec4798ac4f2f8ae688f4` | Incident-side district presentation-role assignments. |
| `interface/015_utopia_manifesto.gfx` | 1,871 / `8d7bb8d4889ac2a08cdefa95fe49c591d775a973c43a8e706c5032e7d9f9a6e2` | 2,009 / `1f061f7bf04372777cc422831b4ff93ff808ec769c258b1457d212b02295fc53` | New Ledger state sprite registrations. |
| `interface/015_utopia_manifesto_ledger.gui` | 297 / `93dc265e487d72424a3c9143c61615a32da41fca1634af75f762adc67c8df51e` | 501 / `82c07b4ac7dde3dbee92745ddb7a64e515682e813133904dc31df026d9669593` | New Ledger state consumers. |

The three decision definition files, category definitions, AI strategy, on-actions, scripted triggers, wargoal, focus tree, and decision/event localisation are byte-identical to the previous PASS snapshot.

## Exact inventory

| Source family | Decisions | Missions |
| --- | ---: | ---: |
| Main Event 015 definitions | 105 | 39 |
| Evolution consumption | 15 | 1 |
| Prefire evolution | 1 | 3 |
| **Total** | **121** | **43** |

| Category | Decisions | Missions |
| --- | ---: | ---: |
| Defense | 5 | 4 |
| District | 10 | 3 |
| Formation | 5 | 1 |
| Governance | 12 | 3 |
| Island | 17 | 4 |
| League | 13 | 4 |
| Ledger | 27 | 13 |
| Necessary Ground | 21 | 7 |
| Stewardship | 11 | 4 |
| **Total** | **121** | **43** |

The nine category identifiers in source are Ledger, district, island, Necessary Ground, stewardship, league, defense, governance, and formation.

## Whole-surface decision and mission regression

- **AI:** 121/121 decisions contain an `ai_will_do` block. The unchanged AI strategy and entry-specific weights remain route/affordability/eligibility aware rather than using a generic always-on weight.
- **Mission lifecycle:** 43/43 missions contain `activation`, `available`, `cancel_trigger`, `cancel_effect`, and `timeout_effect`; all 43 have explicit activation references and explicit removal paths.
- **Dynamic durations:** 43/43 missions use `days_mission_timeout = var:...`. The 43 entries draw from 24 duration variables. Every variable has a preparation writer before activation, and no writer assigns a literal number; constants and centralized helpers remain the tuning source.
- **Targets:** all 43 targeted decisions retain both `target_root_trigger` and `target_trigger`. The ten targeted missions use bounded controlled-state or founder-local-array targets and retain their target eligibility blocks.
- **Costs:** 114/121 decisions charge political power. The seven no-cost entries are the six Calling selectors and `decision_utopia_clear_necessary_ground_target`. The 101 custom-cost entries use 92 unique centralized custom-cost keys; every one has a matching affordability/payment path and all 276 base, `_blocked`, and `_tooltip` localisation keys exist.
- **Outcomes:** success, cancellation, invalid-target, and timeout paths either complete their atomic helper or undo the active state before mission removal. No mission leaves its active flag, target pointer, state pointer, reverse link, or temporary project variable as the authoritative live state after a terminal branch.
- **Cleanup:** system-local cleanup is reached from normal completion/cancellation; `utopia_manifesto_clear_decision_runtime` removes all missions and invokes full district teardown; `utopia_manifesto_clear_all_runtime_state` reaches that helper for rejection and terminal disable paths.
- **Paid formations:** all eight `create_unit` calls remain inside `utopia_manifesto_deploy_paid_formation`; no unpaid or partial-payment deployment path exists.
- **No conquest fallback:** no audited decision/mission adds a core, claim, generic OOB, or substitute territorial outcome.
- **Localisation:** 164/164 entries have names and descriptions; 9/9 categories have names and descriptions. All 288 unique decision tooltip keys referenced by the three decision files resolve.

## Necessary Ground lifecycle and outcomes

The seven founder-specific methods remain distinct: purchase, long supply, lease, settlement, joint administration, association, and the ultimatum/enforcement ladder. Six routes are peaceful; ultimatum and unilateral enforcement are the coercive escalation surfaces.

Static traces pass:

| Trace | Result |
| --- | --- |
| Open a valid new case after an older case expired | The historical `utopia_manifesto_case_expired` marker is cleared only inside the successful validity-gated opening branch; failed opening attempts do not erase history. |
| Target or exact state becomes invalid | Invalid-target handling precedes success/failure resolution and clears the active case rather than awarding a fallback outcome. |
| Peaceful transfer would destroy the target | Settlement acceptance is cancelled; the target-survival guard requires more than one owned state. |
| Ultimatum/enforcement transfer | The same survival guard applies before the exact-state wargoal or transfer path. |
| Exact state at peace | Founder reverse arrays and the stored state identifier select the exact state; invalid-target handling precedes success/failure. |
| Case completion/renunciation/expiry | Response state, target/state pointers, reverse links, missions, wargoal state, flags, and variables are cleared by the centralized case teardown. |

`utopia_manifesto_active_need_case_is_valid` preserves the exact founder, target, and state relationship and requires a live Need deficit until stewardship. The exact-state wargoal is generated from the founder-local reverse array and stored state identifier, not a generic claim or state fallback.

### Case-card state proof

The active precedence is stewardship, refusal, counteroffer, pending offer, ultimatum, then selected/active baseline. The inactive precedence is selected target, eligible target, associate established, expired, then no target.

- Scripted visibility handlers: 10.
- GFX registrations: 10.
- GUI consumers: 10.
- Stem parity: exact.
- Exhaustive `2^11 = 2,048` Boolean-state enumeration: zero overlap, maximum one visible card, 224 uncovered combinations confined to inconsistent inactive selections carrying stale active-response/counter/refusal state.
- Lifecycle-consistent enumeration, where response/counter/refusal implies an active case: 1,152 states, zero overlaps, zero gaps.
- The late selected-target correction suppresses that card for ultimatum priority only when a case is active, so a lawful pre-case ultimatum predicate no longer creates an empty card state.

## District role and phase lifecycle

Seven distinct presentation-role constants are present: market garden, industrial housing, rail junction, refugee municipality, port town, research town, and inland island ring. Eleven producer sites cover all seven roles across ordinary selection, district incidents, coastal-island, and inland-island paths. `utopia_manifesto_district_visual_role` is durable across ordinary phase changes and is cleared by full district runtime teardown.

The phase constants are `none`, `surveying`, `surveyed`, `building`, `delayed`, `built`, `chartering`, and `chartered`. Survey success/failure, build success/partial/failure, charter success/failure, and ownership-loss paths all update or clear the authoritative project pointer and phase. Housing, transport, and role-plan obligations are established at the build transition; partial construction records the delayed/debt/incomplete outcome and does not increment full completion.

The planned presentation state is engine-safe and centralized:

1. `utopia_manifesto_durations.district_plan_card_days = 7` is the sole tuning value.
2. `utopia_manifesto_register_district_project_state` is the sole producer.
3. The constant is copied to a temporary variable and passed to the timed country flag's `days` field.
4. Natural expiry hands the project to the surveyed/building overlay without a recurring on-action.
5. Full district teardown explicitly clears the flag and durable role.

Overlay proof:

- Role cards: 7 scripted handlers, 7 GFX registrations, 7 GUI consumers.
- Phase overlays: 6 scripted handlers, 6 GFX registrations, 6 GUI consumers.
- Exhaustive 8-phase x 7-Boolean-dimension enumeration: 1,024 states, zero overlaps, maximum one overlay, 982 covered and 42 gaps. The gaps are non-display or internally inconsistent combinations, including clean `none`/`surveying`; no valid terminal or visible planned/building/surveyed state is uncovered.
- All variable-derived state scopes in the scripted GUI are guarded by `has_variable` before `var:utopia_manifesto_district_project_state` is entered.
- All 33 Ledger DDS paths referenced by the case, district, value, and Calling integration exist.

## Choice/Assignment crossing presentation

The animation helper remains presentation-only. `utopia_manifesto_refresh_ledger` captures the previous public assignment band before rebuilding/clamping the live Ledger, recalculates the new band, then compares the two.

| Trace | Result |
| --- | --- |
| First refresh without a prior band | No false animation. |
| Route unresolved | No direction flag; scratch prior-band state is cleared. |
| Public band decreases | Assignment flag is cleared; Choice flag is set for three days. |
| Public band increases | Choice flag is cleared; Assignment flag is set for three days. |
| Band unchanged | No retrigger; an existing timed presentation is allowed to expire. |
| Rejection/full teardown | Prior-band state and both presentation flags are cleared. |

Both live sprites retain eight frames, 5 fps, non-looping playback, and `play_on_show`. Their GUI names, scripted-GUI visibility properties, sprite registrations, and file paths agree. The four binary hashes remain unchanged from the previous PASS.

## Manual versus recurring scan audit

No `on_daily`, `on_weekly`, `on_monthly`, or tag variant exists in the Event 015 source set.

The actor-scoped recurring pulse `chaosx.nr15.150` performs:

`reconcile tracked district state -> refresh actor Ledger -> evaluate/validate evolutions -> reschedule actor pulse`

It does not call case discovery, league discovery, or `every_country`.

Five `every_country` occurrences remain, all one-shot or manual: entry selection, case-candidate discovery, two league-candidate passes, and super-event proclamation. Direct terminal hooks do not call candidate discovery. The Ledger Refresh button can call the two league passes, but only through an explicit player click; it is not reachable from the recurring pulse.

## Asset crosswalk freshness note

`docs/assets/015_utopia_manifesto/requirement_to_runtime_coverage_2026_07_16.md` is frozen at SHA-256 `9c708e7bdafc5cc814f937038aa8fa9100f29a68e5cd3c3d70d7049358b48d98` and modification time 2026-07-16 00:31:30. Its rows 17-20 still describe value icons, Calling icons, case cards, and district cards as partial or missing. The live GFX, GUI, scripted-GUI, constants, effects, events, and 33 referenced DDS files were integrated later, between 00:36 and 01:11.

The crosswalk is therefore stale and must not be used as evidence that the live Ledger families are absent. Updating that asset authority document belongs to the asset completion owner and was expressly outside this auditor's patch authority. This does not change the decision/mission PASS, but an overall Event 015 completion report should use a refreshed asset audit/crosswalk.

## Frozen source ledger

| SHA-256 | Lines | Source |
| --- | ---: | --- |
| `e6db306460f20b84cb452faafc300d062a318cbd5b48eb01bb8a24da30658cbb` | 288 | `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` |
| `5dcd41ef8669a4384fedb2efa9761e657fe8a5ff8ea686e45046005fd23d17fd` | 5,708 | `common/decisions/015_utopia_manifesto_decisions.txt` |
| `aa8c813015cacbf2b5d588b82c39d3b440ed9e83f0009a6a048f83e5d0f82ed4` | 543 | `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` |
| `04c46f18ad0c23f70303d75d0d00bb45afcaaf9ab5d877ba01bfe1e9754e3347` | 110 | `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt` |
| `feb02d3e2af05804a30d2c6ef4a1ebb647b3ced2dfe96cb6c8afed2e035a91e8` | 120 | `common/decisions/categories/015_utopia_manifesto_categories.txt` |
| `c2b26e499078d0c7782e46db587d377d8d64cee02e372f2ae8e087c7cea7ea81` | 380 | `common/on_actions/015_utopia_manifesto_on_actions.txt` |
| `73e6986f6b36094694b311347f0bb39299156c4f9c1f4627e67e0306d323d9e0` | 671 | `common/script_constants/015_utopia_manifesto_constants.txt` |
| `f53c2eade8230ac93c8af734e41b01b42fe861a3bdb2ec6944d048545af67326` | 143 | `common/script_constants/015_utopia_manifesto_country_constants.txt` |
| `b54d543548255f116fe73aa055b274b845a4dbc7dba6fa0d8bcd083ea72df1d1` | 239 | `common/script_constants/015_utopia_manifesto_decision_constants.txt` |
| `2b883019089ac98ff550232fd9de3156b40a5bda3c170b05b74c9eb83059b6b2` | 45 | `common/script_constants/015_utopia_manifesto_evolution_consumption_constants.txt` |
| `31d05528fbed483237d761f364a4316c3bf79246852887ddf5959846c0f127f6` | 162 | `common/script_constants/015_utopia_manifesto_narrative_constants.txt` |
| `6c34a48b48bf3f047b9c2c5580f4521bd6139be7182bbabe3ecfc993341969ba` | 85 | `common/script_constants/015_utopia_manifesto_prefire_evolution_constants.txt` |
| `3080751492e6ac3c1c8983822cd6202d403f24833d242e02065fde3a41baaba4` | 121 | `common/script_constants/015_utopia_manifesto_settlement_constants.txt` |
| `b7875f02464267b6cd4435447005f6f8991255f2e7cb38d681d25d43af3478c4` | 17 | `common/script_constants/015_utopia_manifesto_super_event_constants.txt` |
| `bab3fc080661918b35d88b0418a4067ca716e458a63e36a86aa37a5da6f886e2` | 254 | `common/scripted_effects/015_utopia_manifesto_achievement_effects.txt` |
| `0e027f7512bdf07dd04123ef97802235cd18db5d6f46e6de909d8376df7cce4d` | 288 | `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt` |
| `078ccd44ef44d768e1954b3beb914726417fa742a0fe35f8bc5c5938977998aa` | 496 | `common/scripted_effects/015_utopia_manifesto_country_effects.txt` |
| `c743be8d9a124710eb1f1e00b8c13b0197e50c0f2bb9d9b5e9bc55f5752e467c` | 2,612 | `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` |
| `c174887733b31f8f84596826c5e6a7d511d9ef7db72410c0c34946b628e827d2` | 6,334 | `common/scripted_effects/015_utopia_manifesto_effects.txt` |
| `9b28aa9d37c81ee2f1dbb2543c61abbd3f60463d9f42b8e13dc9407223be84f5` | 1,005 | `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt` |
| `da2b2c86a47979dde9b7cae022e4f1798bac6029955858ca90fddd8a9167fa75` | 967 | `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` |
| `1d757540eab0082a09df425578e4208e09cb364832d7b170591ea763d50c60c4` | 536 | `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt` |
| `f10cff3babb246e0a5ea1ad225b22715ed841b42401b9115812134cdab2a38ea` | 146 | `common/scripted_effects/015_utopia_manifesto_reachability_effects.txt` |
| `d4fd6ada2ee953c08da529fd7b890a23ed7ab5ac92d32b13524475130bf7d955` | 68 | `common/scripted_effects/015_utopia_manifesto_super_event_effects.txt` |
| `70325293fc61422eb59d717f8c10a5fb9555e680d0207e2d7be9f3d7cd5fd128` | 395 | `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` |
| `6e44014672139189c53bedb4dd441b9d27900d934a42b6f1fb2166287b6701ed` | 800 | `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt` |
| `d439adad44a446184b08a441a4d3a0dacee74a3078474e17382f0e3fada696c4` | 314 | `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt` |
| `91229ea8fbcba5596f6c6b2d4affce10377d9a72b787c6a46c11a73d2bceb075` | 33 | `common/scripted_triggers/015_utopia_manifesto_evolution_delivery_triggers.txt` |
| `ba4ac12603651718c633a0b3c90b530097ceadcf16969fadcec69c77508a1c5e` | 86 | `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt` |
| `4a32abe608ecceeb7bc23cdc2836a16e9d223b0ee5a5fee91907ead2c037c70f` | 206 | `common/scripted_triggers/015_utopia_manifesto_reachability_triggers.txt` |
| `d0c304d2b4cd5dccd72b40cff8e9ab4caa3beab58838ce68057eacf31bcfe9af` | 2,882 | `common/scripted_triggers/015_utopia_manifesto_triggers.txt` |
| `d81e435349f9bcc1386b98e492d67eaa87f2d029886cb07b91588401a3314543` | 35 | `common/wargoals/015_utopia_manifesto_wargoals.txt` |
| `8e3e0c24ebb7c243761c4391965909b7f5d823878a07ec4798ac4f2f8ae688f4` | 5,076 | `events/015_utopia_manifesto.txt` |
| `42bbc60ef46e9f3c8233c9842a0646b02a72560cd77649195b739fb57416ae92` | 223 | `localisation/english/015_utopia_manifesto_country_package_l_english.yml` |
| `01452765d2413b06844a46aaba1c5e0a552fbd2a7ea319b70d59262dbd83c445` | 699 | `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml` |
| `5d5e0aa9caaa1d39e5065ff7e43bb1c43c812f313e2eb22cb3954adb6d70215b` | 576 | `localisation/english/015_utopia_manifesto_events_l_english.yml` |
| `fc4b71c1190ab45a3d6723a30b7256cee228871a513476345658982b20e534b1` | 101 | `localisation/english/015_utopia_manifesto_evolution_consumption_l_english.yml` |
| `bbf1d8af6246fbf892f4a9d7b4b41e9fc94e8ff5a810588d74180d00cde85cf7` | 19 | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` |
| `c8d34f7e48facc7eac266d64383af3fa66e93c7a9a48d4d46ba2e96a8e570828` | 353 | `localisation/english/015_utopia_manifesto_focus_l_english.yml` |
| `0591a362d9ed653e132915c4d4a83e019048e5cc8fde2aa0505eca7d53be702a` | 137 | `localisation/english/015_utopia_manifesto_ideas_l_english.yml` |
| `a80a6dbaf7e2591a46e836fcbd419d3c7dfac324ccc1f7ba118266678e3fdaa5` | 485 | `localisation/english/015_utopia_manifesto_l_english.yml` |
| `8f14e4fb22578e942ba5019e1022032b12a794c464e61fcef8d7d01bb5527e32` | 21 | `localisation/english/015_utopia_manifesto_super_event_l_english.yml` |
| `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05` | 4,119 | `common/national_focus/015_utopia_manifesto_focus_tree.txt` |
| `1f061f7bf04372777cc422831b4ff93ff808ec769c258b1457d212b02295fc53` | 2,009 | `interface/015_utopia_manifesto.gfx` |
| `82c07b4ac7dde3dbee92745ddb7a64e515682e813133904dc31df026d9669593` | 501 | `interface/015_utopia_manifesto_ledger.gui` |

## Frozen Choice/Assignment binaries

| SHA-256 | Bytes | Asset |
| --- | ---: | --- |
| `cfb74421c21b650b061042f738cd735aeb338e0c3cb96d2624aceb0d46ca8241` | 121,472 | `gfx/interface/015_utopia_manifesto/utopia_balance_to_assignment_sheet.dds` |
| `202a9ab4120cec445d07ef4b0509a57baff8e8ef9272a722c9be204d281efd62` | 15,296 | `gfx/interface/015_utopia_manifesto/utopia_balance_to_assignment_static.dds` |
| `cd0440db72fce608ee20cd0f5496ede0f9396ed1756aed72c694c9586f2ca13c` | 121,472 | `gfx/interface/015_utopia_manifesto/utopia_balance_to_choice_sheet.dds` |
| `126081178829c4e7092e72b52c774e07388c39b9626518a4eee4c414bca0b953` | 15,296 | `gfx/interface/015_utopia_manifesto/utopia_balance_to_choice_static.dds` |

## Findings by severity

- P0: none.
- P1: none.
- P2: none in the decision/mission mechanics surface.
- P3: none in the decision/mission mechanics surface.

The stale asset crosswalk is a documentation-freshness handoff to the asset completion owner, not a decision/mission mechanics finding.

## Limitations

- Static source audit only: no running-engine trace, multiplayer synchronization test, or multi-resolution GUI capture was performed.
- The unavailable HOI4 MCP prevented an additional domain-tool render/inspect pass.
- The workspace contains extensive concurrent work. The hashes above, not Git cleanliness, define the audited snapshot.

## Simplifications, omissions, fallbacks, and blockers

No simplification, omission, fallback, or blocker was used for this decision/mission audit. The full 121-decision, 43-mission, 9-category surface was inspected. No gameplay, localisation, asset, specification, spreadsheet, or authority document was edited. No commit was created.

