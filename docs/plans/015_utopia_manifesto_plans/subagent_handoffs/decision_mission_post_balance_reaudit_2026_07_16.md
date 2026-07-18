# Event 015 Decision and Mission Post-Balance Re-audit

Date: 2026-07-16  
Auditor role: fresh decision/mission audit  
Audit mode: read-only source inspection; this report is the only file created  
Decision/mission verdict: **PASS**

## Scope and verdict boundary

No P0, P1, P2, or P3 defect was found in the Event 015 decision, mission, Ledger, route-resolution, or Choice/Assignment band-crossing presentation logic frozen below.

This is a decision/mission mechanics verdict, not a substitute for the separate visual-asset completion audit. Visual quality, source-frame provenance, and asset-package documentation remain owned by the asset audit; findings raised there must be repaired before an overall Event 015 completion claim even though the scripted decision/mission surface passes here.

## References used

- Repository instructions: `AGENTS.md`.
- Repo skills, read in full: `hoi4-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`.
- All files under `docs/specs/015_utopia_manifesto_specs/`, including the balance-Ledger, decision/mission, evolution, Necessary Ground, route, and asset requirements.
- Previous current decision report: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/decision_mission_completion_current_reaudit_2026_07_15.md`.
- Required offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding.
- Official game documentation: `common/decisions/_documentation.md`, `common/scripted_guis/_documentation.md`, `common/on_actions/_documentation.md`, `common/script_constants/documentation.md`, `documentation/script_concept_documentation.md`, plus the exact variable/flag entries in `effects_documentation.md` and `triggers_documentation.md`.
- Vanilla precedents, including variable-backed timed country flags in `common/scripted_effects/SIA_scripted_effects.txt`.

## Frozen delta disposition

The previous decision audit froze 42 Event 015 gameplay/localisation sources. In this snapshot, 39 of those 42 files are byte-identical. The only three changed sources are the intended presentation integration:

| Source | Previous lines | Current lines | Current SHA-256 | Disposition |
| --- | ---: | ---: | --- | --- |
| `common/script_constants/015_utopia_manifesto_constants.txt` | 669 | 670 | `75abb0707e63730e871d7582ed6aaa6b275d3a0bc0a37ab5b7e4e5bfeb5ff700` | One three-day presentation-duration constant. |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | 6,275 | 6,331 | `fd7b62671d1f49eb00363316914c6893463c08f4ea24a2c972d37093a8c87cd7` | Prior-band capture, direction helper, refresh call, initialization suppression, and teardown cleanup. |
| `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` | 115 | 121 | `de37ba78051436a69abdc4a79799749210b9e208b9d3a5396ea012206fde8dbd` | Two country-flag visibility properties. |

The decision definitions, mission definitions, decision helpers, decision triggers, events, on-actions, AI strategy, localisation, and paid focus callers remain byte-identical to the prior PASS snapshot. The focus tree remains exactly `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05` (4,119 lines).

The linked UI sources are frozen as:

- `interface/015_utopia_manifesto.gfx`: `8d7bb8d4889ac2a08cdefa95fe49c591d775a973c43a8e706c5032e7d9f9a6e2` (1,871 lines).
- `interface/015_utopia_manifesto_ledger.gui`: `93dc265e487d72424a3c9143c61615a32da41fca1634af75f762adc67c8df51e` (297 lines).

## Choice/Assignment crossing presentation audit

The Ledger invariant remains `clamp(base + durable policy + current live contribution, 0, 100)`. The presentation helper runs only after the refresh has rebuilt and clamped the Ledger and recalculated its public band. It reads the old and new bands and the resolved-route state; it does not write any Ledger base, policy, live-contribution, total, prepared-delta, cost, mission, or route-outcome value.

Static trace results:

| Case | Result |
| --- | --- |
| Initialization with no prior public band | Both presentation flags are cleared before the first refresh; no false first-load animation is emitted. |
| Route unresolved | No direction flag is set and the prior-band scratch variable is cleared. |
| Resolved route, band 3 to band 2 | The opposite flag is cleared and the Choice-direction flag is set for three days. |
| Resolved route, band 2 to band 3 | The opposite flag is cleared and the Assignment-direction flag is set for three days. |
| Resolved route, unchanged band | No new presentation flag is emitted; any already-running three-day presentation completes normally. |
| Rejection or terminal teardown | Current band, prior-band scratch state, and both presentation flags are cleared. |

Additional findings:

- Prior-band capture occurs before live-pressure refresh and band recalculation, so it compares public bands from consecutive valid Ledger states rather than comparing a partially rebuilt Ledger.
- The helper is reached through the existing idempotent Ledger refresh. Repeated refreshes without a band change do not create a new presentation event.
- Route setters resolve the route before applying the prepared Ledger delta, so a genuine route-defining crossing can be presented while unresolved pre-route initialization remains suppressed.
- The two direction flags are mutually exclusive whenever a new crossing is emitted.
- `check_variable` is valid for variable-to-variable comparison according to the official trigger documentation. The implementation uses supported `less_than` and `greater_than` comparison modes.
- The duration is centralized as `constant:utopia_manifesto_durations.balance_shift_animation_days`, copied to a temporary variable, and consumed immediately by `set_country_flag`'s `days` field. This follows the repository's required duration-field pattern and the vanilla variable-duration timed-flag precedent.
- The category contains one attachment of `utopia_manifesto_ledger_scripted_gui`; the two animated sprites use the matching visibility properties. No duplicate decision-file attachment was introduced.
- No daily, weekly, or monthly world scan was added.

## Full decision and mission regression

The complete surface still contains **164 entries: 121 decisions and 43 missions**.

| Source family | Decisions | Missions |
| --- | ---: | ---: |
| Main Event 015 decisions | 105 | 39 |
| Evolution consumption | 15 | 1 |
| Prefire evolution | 1 | 3 |
| **Total** | **121** | **43** |

| System family | Decisions | Missions |
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

Regression results:

- 121/121 decisions retain `ai_will_do` behavior.
- 43/43 missions retain activation, availability, cancellation trigger, cancellation effect, and timeout effect handling.
- 43/43 missions retain variable-backed timeouts and terminal mission-removal paths.
- All 43 targeted decisions retain both `target_trigger` and `visible_target_trigger`; the 10 targeted missions retain their bounded target logic.
- 114/121 decisions retain political-power costs. The seven no-cost entries are intentional control/claim actions. The 101 custom-cost entries retain 92 unique centralized cost keys, matching affordability, payment, and localisation.
- Prepared Ledger deltas remain previewable and atomic: reset, prepare, affordability, payment, application, and cleanup still use the previously audited shared paths. The new helper reads only the resulting public band.
- Route resolution, initialization, rejection, and terminal cleanup remain ordered and complete. The new prior-band scratch state and direction flags are included in both initialization suppression and runtime teardown.
- Necessary Ground retains all seven founder-specific cases, exact-state targeting, and founder attribution. It does not add cores, claims, generic OOBs, or fallback conquest outcomes.
- Evolution consumption retains all 15 evolutions and the five previously audited dispatch surfaces.
- Prefire evolution decisions remain isolated to their founder/event actor.
- Association diplomacy retains exact founder arrays and creator attribution.
- Auxiliary hiring retains combined affordability and atomic combined payment before deployment.
- All eight `create_unit` calls remain confined to `utopia_manifesto_deploy_paid_formation`; there is no unpaid deployment path.
- Paid-focus rewards remain routed through the guarded call effects: 26 institutional-growth callers and 8 military-growth callers. No reward tail bypass was introduced.

## Frozen source ledger

| SHA-256 | Lines | Source |
| --- | ---: | --- |
| `e6db306460f20b84cb452faafc300d062a318cbd5b48eb01bb8a24da30658cbb` | 288 | `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` |
| `5dcd41ef8669a4384fedb2efa9761e657fe8a5ff8ea686e45046005fd23d17fd` | 5,708 | `common/decisions/015_utopia_manifesto_decisions.txt` |
| `aa8c813015cacbf2b5d588b82c39d3b440ed9e83f0009a6a048f83e5d0f82ed4` | 543 | `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` |
| `04c46f18ad0c23f70303d75d0d00bb45afcaaf9ab5d877ba01bfe1e9754e3347` | 110 | `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt` |
| `feb02d3e2af05804a30d2c6ef4a1ebb647b3ced2dfe96cb6c8afed2e035a91e8` | 120 | `common/decisions/categories/015_utopia_manifesto_categories.txt` |
| `c2b26e499078d0c7782e46db587d377d8d64cee02e372f2ae8e087c7cea7ea81` | 380 | `common/on_actions/015_utopia_manifesto_on_actions.txt` |
| `75abb0707e63730e871d7582ed6aaa6b275d3a0bc0a37ab5b7e4e5bfeb5ff700` | 670 | `common/script_constants/015_utopia_manifesto_constants.txt` |
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
| `0eeedf55b22818d4452e18adbe75bb106bf45ffcd33cbf6d3573cab6125bc33a` | 2,601 | `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` |
| `fd7b62671d1f49eb00363316914c6893463c08f4ea24a2c972d37093a8c87cd7` | 6,331 | `common/scripted_effects/015_utopia_manifesto_effects.txt` |
| `9b28aa9d37c81ee2f1dbb2543c61abbd3f60463d9f42b8e13dc9407223be84f5` | 1,005 | `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt` |
| `da2b2c86a47979dde9b7cae022e4f1798bac6029955858ca90fddd8a9167fa75` | 967 | `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` |
| `1d757540eab0082a09df425578e4208e09cb364832d7b170591ea763d50c60c4` | 536 | `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt` |
| `f10cff3babb246e0a5ea1ad225b22715ed841b42401b9115812134cdab2a38ea` | 146 | `common/scripted_effects/015_utopia_manifesto_reachability_effects.txt` |
| `d4fd6ada2ee953c08da529fd7b890a23ed7ab5ac92d32b13524475130bf7d955` | 68 | `common/scripted_effects/015_utopia_manifesto_super_event_effects.txt` |
| `de37ba78051436a69abdc4a79799749210b9e208b9d3a5396ea012206fde8dbd` | 121 | `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` |
| `6e44014672139189c53bedb4dd441b9d27900d934a42b6f1fb2166287b6701ed` | 800 | `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt` |
| `d439adad44a446184b08a441a4d3a0dacee74a3078474e17382f0e3fada696c4` | 314 | `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt` |
| `91229ea8fbcba5596f6c6b2d4affce10377d9a72b787c6a46c11a73d2bceb075` | 33 | `common/scripted_triggers/015_utopia_manifesto_evolution_delivery_triggers.txt` |
| `ba4ac12603651718c633a0b3c90b530097ceadcf16969fadcec69c77508a1c5e` | 86 | `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt` |
| `4a32abe608ecceeb7bc23cdc2836a16e9d223b0ee5a5fee91907ead2c037c70f` | 206 | `common/scripted_triggers/015_utopia_manifesto_reachability_triggers.txt` |
| `d0c304d2b4cd5dccd72b40cff8e9ab4caa3beab58838ce68057eacf31bcfe9af` | 2,882 | `common/scripted_triggers/015_utopia_manifesto_triggers.txt` |
| `d81e435349f9bcc1386b98e492d67eaa87f2d029886cb07b91588401a3314543` | 35 | `common/wargoals/015_utopia_manifesto_wargoals.txt` |
| `a7d27155c463424f19fb1d661356a42ccb90cc4b29f8e42a03ea78ba86b9b164` | 5,071 | `events/015_utopia_manifesto.txt` |
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
| `8d7bb8d4889ac2a08cdefa95fe49c591d775a973c43a8e706c5032e7d9f9a6e2` | 1,871 | `interface/015_utopia_manifesto.gfx` |
| `93dc265e487d72424a3c9143c61615a32da41fca1634af75f762adc67c8df51e` | 297 | `interface/015_utopia_manifesto_ledger.gui` |

## Frozen presentation binaries

| SHA-256 | Bytes | Asset |
| --- | ---: | --- |
| `cfb74421c21b650b061042f738cd735aeb338e0c3cb96d2624aceb0d46ca8241` | 121,472 | `gfx/interface/015_utopia_manifesto/utopia_balance_to_assignment_sheet.dds` |
| `202a9ab4120cec445d07ef4b0509a57baff8e8ef9272a722c9be204d281efd62` | 15,296 | `gfx/interface/015_utopia_manifesto/utopia_balance_to_assignment_static.dds` |
| `cd0440db72fce608ee20cd0f5496ede0f9396ed1756aed72c694c9586f2ca13c` | 121,472 | `gfx/interface/015_utopia_manifesto/utopia_balance_to_choice_sheet.dds` |
| `126081178829c4e7092e72b52c774e07388c39b9626518a4eee4c414bca0b953` | 15,296 | `gfx/interface/015_utopia_manifesto/utopia_balance_to_choice_static.dds` |

The registered animated sprites use eight 158x24 frames, non-looping playback, five frames per second, and `play_on_show`. The registered sprite names, texture paths, GUI names, and scripted-GUI visibility properties agree. This statement validates wiring and file identity only; it does not supersede visual/provenance review.

## Findings by severity

- P0: none in the audited decision/mission mechanics surface.
- P1: none in the audited decision/mission mechanics surface.
- P2: none in the audited decision/mission mechanics surface.
- P3: none in the audited decision/mission mechanics surface.

## Limitations

- This was a static source audit. It did not execute a running-game save, record an engine trace, capture the GUI in multiple resolutions, or simulate multiplayer synchronization.
- The audit verifies animation trigger wiring and its isolation from gameplay values. Separate asset-audit findings concerning visual construction, source-frame provenance, previews, manifests, or documentation are outside this PASS and remain authoritative for overall completion.
- The workspace contains extensive unrelated and concurrent changes. The hashes above, rather than Git cleanliness, define the exact snapshot audited.

## Simplifications, omissions, fallbacks, and blockers

No simplification, omission, fallback, or blocker was used in this decision/mission audit. No gameplay, localisation, asset, or documentation source was edited; only this audit handoff was created. No commit was made.
