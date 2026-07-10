# Event 011 Secret Alliance decision and mission re-audit

## Verdict

The current Event 011 decision and mission implementation resolves DM-01 through DM-14 and RA-01 through RA-02. The earlier incomplete findings in this handoff are superseded by this re-audit.

This was a report-only audit. The auditor did not edit gameplay, localisation, interface, AI, event, scenario, achievement, asset, or spreadsheet files. No commit was created.

## Audited freeze

The final evidence below was taken from this exact working-tree snapshot:

| File | SHA-256 |
| --- | --- |
| `common/decisions/011_secret_alliance_decisions.txt` | `ECC0B7A09CD21938C418A64732FC8D5F483C04FDC8F0AFEF5DC6C066812B2B97` |
| `common/scripted_triggers/011_secret_alliance_triggers.txt` | `55FD17D4DB83E4A503BAF05F95DE6A15ED10558082C49EECDD5000CCFCDA1B63` |
| `common/scripted_effects/011_secret_alliance_effects.txt` | `AE6E453DAD29A5A9D7659776DF6C81967AAAB75F148CDF3D4B85C9702931A6DF` |
| `events/011_secret_alliance.txt` | `641838E5C237B9FC9872F71466D735935B6E9534E288B57F4CA1463D3292C4A4` |
| `common/on_actions/011_secret_alliance_on_actions.txt` | `40E78311DD75CFB6D72C348DDE2DF237C53F723972A4626971EE25DB944F14F2` |
| `common/scripted_guis/011_secret_alliance_scripted_gui.txt` | `C715868C26CF43EE937E89EF327562F0724BEAB63714F7A74B82C5E14166989F` |
| `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt` | `34D1ABAB4FEB30B83942BC949BC6EDB7D19414EC7D1246EA42CE587726347339` |
| `common/ai_strategy/011_secret_alliance.txt` | `3FB48B7EAC0025F1CE1859696FA00C1AB738B63ED011C0D91CD21DA0176405EE` |
| `common/script_constants/011_secret_alliance_constants.txt` | `473698C9686877CE3935CEE2268BC0C668CD45A1E477C08BE2B6CC7DAF9A9CD4` |

## References used

The audit used the accepted Event 011 specs, especially the decision and mission matrix, AI strategy matrix, tuning model, event-chain map, and spec parts 1 through 5.

Required offline Paradox wiki references were consulted for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Faction modding, Interface modding, and Scripted GUI modding.

Vanilla documentation was consulted for decisions, scripted GUIs, factions, on actions, AI strategy, triggers, effects, modifiers, script concepts, dynamic variables, localisation formatters/objects, and script constants. The exact-state and border-war structure was compared with the vanilla Japanese border-conflict implementation in `common/decisions/JAP.txt:3577-3683`. Official trigger documentation confirms that `divisions_in_border_state` checks the named country/state pair and that `has_railway_level` checks the named state for the required minimum railway level.

## DM-01 through DM-14

| ID | Result | Evidence |
| --- | --- | --- |
| DM-01 | Resolved | The scripted GUI is ROOT-only, disables AI use, supplies three clickable suspect cards plus clear and animation controls, and drives meters/card frames through properties at `common/scripted_guis/011_secret_alliance_scripted_gui.txt:5-76`. Matching interface elements exist at `interface/011_secret_alliance.gui:30-47`. No event target is resolved inside the GUI. |
| DM-02 | Resolved | Reveal leader selection scores every valid active member by military, industrial, and major strength at `common/scripted_effects/011_secret_alliance_effects.txt:3637-3659`. Reveal snapshot and public-faction membership are post-validated at lines 3661-3805. Hostile-war reveal calls every valid active snapshot member, retries failures, and rolls back the transaction if any call remains unresolved at lines 3947-4073. The common transaction preserves the hostile-war route even during a dispute and stores the explicit fractured route for other disputed reveals at lines 4021-4035; scripted localisation reads that distinct constant at `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt:204-228`. Planned war handles turned, delayed, fractured, retried, and explicit-exit states at effects lines 4076-4192. |
| DM-03 | Resolved | Family affordability gates match their payment helpers at `common/scripted_triggers/011_secret_alliance_triggers.txt:397-588` and `common/scripted_effects/011_secret_alliance_effects.txt:2302-2410`. Diplomacy's reusable payment gate covers the scaled PP, CP, Stability, and active slot at triggers lines 491-501; Allied Consultation and Neutral Inquiry use it in both availability and custom-cost gates at `common/decisions/011_secret_alliance_decisions.txt:472-492`. Preemption uses the same 50% War Support gate in availability and custom cost at decisions lines 827-845, then pays the separately displayed 5% strain at effects lines 3584-3589. Border escalation pays its displayed War Support variable at effects lines 2953-2958. The rumor event accepts an exact PP balance at `events/011_secret_alliance.txt:213-217`. The final strict-resource sweep found no Event 011 resource affordability site using a bare strict `>`. Named requirement tooltips and visibly blocked cost roots are present in the decision and localisation files. |
| DM-04 | Resolved | All seven investigation missions are activated as nonselectable named objectives and require both their saved exact state and a route-specific verified flag at `common/decisions/011_secret_alliance_decisions.txt:206-308`. Objective preparation saves the state and suspect identity at `common/scripted_effects/011_secret_alliance_effects.txt:2099-2191`; delayed verification checks that same state plus the mission-specific field condition at lines 2193-2300. Completion, cancellation, and expiry clear the exact objective state and suspect pointer at lines 2516-2776. |
| DM-05 | Resolved | Preparedness is recomputed from separate staff-plan, cipher, industrial, stockpile, port, border-communications, border-patrol, cabinet, continuity-site, allied-consultation, emergency, and known-plan sources at `common/scripted_effects/011_secret_alliance_effects.txt:3001-3044`. Protection projects create distinct timed sources and distinct end helpers at lines 3052-3166. Emergency, patrol, and consultation sources have their own expiry helpers at lines 3625-3631, wired through `events/011_secret_alliance.txt:433-459`. One expiring source cannot erase another active contribution. |
| DM-06 | Resolved | Evidence sources are stored per suspect by class while the dossier maintains its independent global class count at `common/scripted_effects/011_secret_alliance_effects.txt:1799-1929`. Confirmation requires both confidence and per-suspect corroboration at lines 1932-1952 and `common/scripted_triggers/011_secret_alliance_triggers.txt:360-387`. Mission clues retain the prepared suspect and supply a defined evidence class at effects lines 2516-2543. |
| DM-07 | Resolved | The canonical suspect trigger rejects subjects, civil wars, special countries, capitulated countries, the target, cleared suspects, and target-faction partners at `common/scripted_triggers/011_secret_alliance_triggers.txt:327-337`. Both AI targeting and the full hidden suspect pool use that trigger at `common/scripted_effects/011_secret_alliance_effects.txt:1312-1355` and 1394-1415. The visible pool is independently ranked and capped to three cards at lines 1732-1772. |
| DM-08 | Resolved | Foreign Interference is concealed Evolution II only, while Coalition Crisis owns Evolution III and revealed play at `common/scripted_triggers/011_secret_alliance_triggers.txt:275-290` and `common/decisions/categories/011_secret_alliance_categories.txt:9-24`. Reveal closes the response category at `common/scripted_effects/011_secret_alliance_effects.txt:4051-4057`. |
| DM-09 | Resolved | The prepared border pair requires the stored attacker/defender states, minimum infrastructure, railway level in both exact states, target divisions on the exact border, and suspect divisions in the defender state at `common/scripted_triggers/011_secret_alliance_triggers.txt:540-560`. The conflict decision highlights that pair and requires the complete logistics/unit gate at `common/decisions/011_secret_alliance_decisions.txt:646-709`. Start, exact cancellation, escalation, withdrawal, negotiation, win, loss, and cancel paths are wired at `common/scripted_effects/011_secret_alliance_effects.txt:2860-2983`; terminal cleanup cancels the exact live conflict before clearing its state. |
| DM-10 | Resolved | Hidden values convert to Resolve, opening coordination, known weaknesses, and target defenses at `common/scripted_effects/011_secret_alliance_effects.txt:3808-3850`. Zero applies no staged idea; low, medium, and high bands apply distinct ideas at lines 3852-3908, defined at `common/ideas/011_secret_alliance_ideas.txt:94-173`. Cleanup removes every stage. |
| DM-11 | Resolved | Normal entry remains human-target-only, with an explicit hidden opt-in AI test entry at `common/scripted_triggers/011_secret_alliance_triggers.txt:9-23` and `events/011_secret_alliance.txt:552-584`. Concealed AI selects from the full valid suspect array and revealed AI selects from the full valid public-member array at `common/scripted_effects/011_secret_alliance_effects.txt:1312-1355`. Human revealed targeting uses `global.secret_alliance_public_members` at `common/decisions/011_secret_alliance_decisions.txt:901-916`, and AI wartime response consumes the selected public member at effects lines 4341-4365. |
| DM-12 | Resolved | A false public accusation writes the immutable `secret_alliance_innocent_accused` marker, applies Stability, cohesion, alertness, opinion, and possible recruitment consequences at `common/scripted_effects/011_secret_alliance_effects.txt:3169-3193`. Coalition-case safeguards read that marker at `common/scripted_triggers/011_secret_alliance_triggers.txt:379-387` and 708-712. War against an innocent lead records the separate achievement consequence at effects lines 5376-5396. |
| DM-13 | Resolved | Cleanup first cancels the exact border conflict, removes all missions and staged ideas, clears target/member/suspect flags and variables, clears every Event 011 array and global event target, and clears the event-owned global runtime state at `common/scripted_effects/011_secret_alliance_effects.txt:4717-5103`. A mechanical comparison found no Event 011 global flag set without a corresponding clear and no saved Event 011 global event target without a corresponding clear. Narrow lifecycle refreshes cover war, capitulation, uncapitulation, government, annexation, faction, leadership, puppet, liberation, release, subject, civil-war, and peace-conference changes at `common/on_actions/011_secret_alliance_on_actions.txt:8-76`, with handlers at effects lines 5376-5486. |
| DM-14 | Resolved | Each concealed pulse chooses exactly one prioritized incident at `common/scripted_effects/011_secret_alliance_effects.txt:1268-1309`. Operation-family weights consume member roles, motives, doctrine, recent family, and prepared surfaces, then select a matching actor and real readiness layer at lines 1526-1718. Decision visibility is phase-, incident-, suspect-, objective-, and cap-aware throughout `common/decisions/011_secret_alliance_decisions.txt:30-774`; the seven Evolution III actions plus countdown are at lines 782-893, and revealed selection plus seven war actions are at lines 901-998. Feed False Plans is a one-card replacement while its event-owned channel exists, all normal offensive branches carry the inverse gate, and the effect consumes the channel at decisions lines 512-597 and effects lines 3365-3372. This preserves the accepted current-action bands instead of exposing the full catalog. |

## RA-01 and RA-02

| ID | Result | Evidence |
| --- | --- | --- |
| RA-01 | Resolved | Maximum requests 12 total members and two majors, within the accepted 8-12/maximum-two band, at `common/script_constants/011_secret_alliance_constants.txt:191-196`. The scenario counts its valid AI-only safe minor/major pool, selects majors first and minors without exceeding the requested total, and records requested, safe, and achieved composition at `common/scripted_effects/011_secret_alliance_effects.txt:5109-5184` and 5282-5309. Maximum qualification requires the achieved major count and either the requested total or the exact safe-pool ceiling at lines 5286-5300. Launch aborts rather than substituting an invalid composition at lines 5312-5367. |
| RA-02 | Resolved | Outcome-band constants define full, partial, expired, and failure identities at `common/script_constants/011_secret_alliance_constants.txt:35-41`. Every mission outcome helper writes those named constants at `common/scripted_effects/011_secret_alliance_effects.txt:2412-2513`; downstream decisions and expiry effects read the same named values. No raw numeric outcome identity remains in the audited decision/mission flow. |

## Task-specific verification

- Re-froze the gameplay files after every audit-triggered correction and based this report on the hashes above.
- Confirmed the hostile-war reveal transaction cannot complete while a valid snapshot member remains outside the target war.
- Confirmed every named investigation objective binds completion to its saved exact state and delayed verification fact.
- Confirmed every Preparedness source expires independently.
- Confirmed the border conflict requires the exact stored state pair, local divisions, infrastructure, and railway readiness, and that every exit path reaches exact cancellation or resolution.
- Confirmed the AI-only test route is opt-in and hidden, while ordinary event eligibility remains human-target-only.
- Confirmed Maximum scenario proof is based on achieved composition rather than requested intensity alone.
- Confirmed the final resource-affordability sweep contains no strict exact-balance `>` gate.
- Confirmed Event 011 global flags and saved global event targets all have teardown coverage.

## Simplifications, omissions, and blockers

None in the audited DM-01 through DM-14 and RA-01 through RA-02 scope. No fallback or weaker substitute was accepted.
