# Event 016 D’Rhondan compact closure owner review

## Scope and retained contract

This checkpoint corrects the existing Two-World Compact decision and Events `.49`–`.52` under the accepted Event 016 final completion contract.
It adds no event, evolution, country, focus, meter, GUI, super-event, achievement, model, or alternative diplomatic route.
The exact before event source is Git blob `047ab4aea29d38a322c354dc11bfa6e1b208eb92` from `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd`, unchanged by the intervening containment checkpoint `588c2f12f02890cf3f7947847927307347204629`.
The before triggers and effects are retained by the corresponding commit and the probability handoff.

## Finding disposition and implementation

| Finding | Owner correction | Boundary |
| --- | --- | --- |
| C1: visible stale options apply diplomacy or clear another offer | Both real response branches revalidate live receipt and diplomatic legality; all invalid branches use recipient-owned cleanup. | An unmatched different-recipient popup is inert. |
| C2: valid delivery bypasses the delivered flag | Every `.49` delivery requires the same matching, active, undelivered receipt and an unexpired deadline. | A second delivery during an open ordinary offer cannot enter. |
| C3: one-day watchdog follows mutable state and unlocks an open popup | Capture original actor/recipient pointers before dispatch, keep the native thirteen-day response window, and schedule one actor-owned deadline with one cleanup-grace day. | Early matching checks reschedule to the current expiry; legality changes do not clear the lock early. |

The valid accept/refuse visibility split and all existing AI scores remain unchanged.
The earlier assertion that invalid cleanup competed with valid responses is rejected; the defects were delivery and click-time ownership, not the relative option weights.
The duration clarification is promoted into `016_final_completion_contract.md` before the gameplay correction.

The actor-owned private finalizer clears the active flag, delivered flag, expiry variable, and persistent current target together.
It preserves concluded-compact and partner history.
Country initialization reconstructs the surviving current offer’s ordinary targets and preserves its deadline.
An undated active receipt receives one complete response window without a new popup, repeated payment, or diplomatic reward.
The player sees concise acceptance, refusal, and lapsed-offer effect summaries instead of the internal click guard.

## Source review scenarios

1. A valid first delivery writes the delivered receipt and refreshes the expiry once.
2. A duplicate delivery against that same active receipt fails the common event trigger.
3. Valid acceptance applies the pact, reciprocal opinion, partner/concluded history, and one existing stability reward, then clears transient state before the `.50` notice.
4. Valid refusal applies its existing opinion modifier, then clears transient state before the `.51` notice.
5. War, subject status, route loss, world end, actor loss, or a pre-existing pact after delivery makes a visible response fail its commit guard; only its owned transient receipt can close.
6. A stale popup for recipient A cannot clear a current offer to recipient B because both ordinary and persistent recipient identities must match.
7. A cleared receipt makes repeated option effects inert even when the old popup’s visible option was selected again.
8. A different-recipient stale watchdog fails its trigger; an early same-pair watchdog follows the current recorded deadline and cannot expire it early.
9. An undelivered receipt is bounded by its initial response-plus-grace deadline; first delivery before that deadline starts one complete native response window.
10. Reinitialization does not reset an existing expiry, repeat an offer, or award a compact.

These are manually reviewed source-control-flow scenarios and source assertions, not execution of the game scheduler.
Additional assertions compare both `ai_chance` blocks byte-for-byte after newline normalization, count the two live commit guards and three owned invalid-cleanup paths, verify target capture precedes watchdog scheduling, and check the native/shared thirteen-day duration mirror.
The postreview specialist found no additional concrete source blocker within the documented ordinary popup lifecycle.

## Mandatory MCP evidence

The probability specialist retained all thirteen original scenarios in `E016_DHR_COMPACT_RESPONSE_2026_09_02.scenarios.json` and compared the exact before/current event source objects.
The comparison returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-385a5e5b7beb22671bf36688`, with the unchanged scenario hash `bd600830ba0b953ccb964335a90e5e126c38b2d76bf8e060e44e9719befc6f5d` and zero reported option changes.
The adapter’s apparent cleanup-only result is not a campaign probability: scoped opinion/war/pact predicates remain unresolved, and the original fixture lacks the newly required regular recipient pointer.
Zero reported changes therefore does not prove preserved eligibility, correct delivery, or safe lifecycle ordering.
The comparison isolates before/current event bytes only; both sides resolve helper definitions and constants from the current workspace.
The separately retained prepatch evaluation has the earlier helper context, but the comparison itself does not isolate the helper rewrite.
The detailed source hashes, inspect results, JSON, and rendered evidence are retained in `016_final_dhr_compact_probability_2026-09-02.md`.

Post-change event inspection and rendering returned partial focused revision `d8c9140e69ae6d53f2fb77284bb37300a75d320975ad211d21933a46986988cf` with zero indexed helpers.
The parent inspected the returned neighborhood PNG at `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/c0/c0a9ae7ae429570dba3d8b1e4b0947fedffc95c95ff4bc589941ccbcebeaf8e8/event-neighborhood-d8c9140e69ae.png`.
It shows the existing response/notice paths and expiry helper consumers, but not their internal control flow or a native popup simulation.
The single before/after cached event comparison returned `EVENT_REVISION_NOT_CACHED`, validation false, and no artifacts.
`016_final_dhr_compact_postreview_2026-09-02.md` owns the exact final event artifacts and comparison request.
No successful event comparison or full helper-graph validation is claimed.

## Files and reference evidence

Gameplay changes are limited to `events/016_dhrondan_country_events.txt`, `common/decisions/016_dhrondan_country_decisions.txt`, `common/scripted_triggers/016_dhrondan_country_triggers.txt`, `common/scripted_effects/016_dhrondan_country_effects.txt`, and `common/script_constants/016_dhrondan_country_constants.txt`.
Presentation changes are three English effect tooltips in `localisation/english/016_dhrondan_country_l_english.yml`.
The contract and `docs/events/016_brilliant_scientist/systems/dhrondan_country.md` describe the actual receipt/timeout behavior and its evidence boundary.
This handoff, pre/post lifecycle reviews, probability handoff, and retained scenario fixture form the checkpoint evidence.
No catalog wording or event identity changed in this bounded correction; final workbook alignment remains part of closure tranche 8.

Offline Event Modding establishes delivery-time option visibility and the native thirteen-day timeout.
Offline Data Structures establishes ordinary event-target propagation and warns that temporary variables do not survive event dispatch.
Installed effects documentation was checked for target saves/clears, delayed country events, temporary-variable clamping, and variable removal.
Installed vanilla `events/Generic.txt` and `events/WTT_PRC.txt` demonstrate `tag = event_target:...`; the existing African world-order invitation effects demonstrate temporary-variable country-event delays.
No unsupported event-local numeric generation snapshot was introduced.

## Simplifications, omissions, and blockers

No substitute mechanic, model, asset, AI fallback, or reduced reward was introduced by this checkpoint.
Native open-popup timeout behavior across recipient annexation and re-release is not established by the available documentation or MCP evidence.
Ordinary country pointers cannot prove identity between an ancient surviving popup and a later offer to that same country pair; that exact lifetime scenario remains unresolved.
An actor-owned delayed event also cannot be assumed to tick while DHR does not exist; country reinitialization and any surviving recipient response perform the documented revalidation when they execute.
The partial probability and event evidence, failed cached comparison, and unresolved destruction/re-release lifetime gate remain open acceptance work.
This checkpoint does not certify DHR formation, focus rewards, the full foreign-operation system, project costs, models, GUI, assets, or overall Event 016 completion.
No game was launched and no logs or user-run tests were requested.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
They require receipt-owned lifecycle cleanup, concise player-facing effects, mandatory specialist review, and honest separation of source assertions from MCP and live acceptance evidence.
