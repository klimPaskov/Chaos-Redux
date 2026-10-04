# Event 24 agent decisions, 2026-10-04

Disposition: accepted under the user's standing grant of design authority to the implementing agent for this takeover round.
Each entry records the decision, the spec basis, and where it is implemented.
Implementation evidence is source review only; live-game behaviour remains the orchestrator's separate check.

## D1. Crisis memory is current and finite

Decision: `video_game_in_sweden_core_loss_crisis` and `video_game_in_sweden_capital_threat` describe the current situation instead of permanent history.
`video_game_in_sweden_refresh_crisis_state` rebuilds both every day from three facts: Stockholm outside Swedish ownership or control, an owned Swedish core held by another controller, or a loss inside the finite memory window.
The memory window is a timed flag (`video_game_in_sweden_core_loss_recent`, `video_game_in_sweden_capital_loss_recent`) whose length comes from `video_game_in_sweden_timing.crisis_memory_days` through a temporary variable.
Basis: spec part 3 says audit failure comes from capital loss or several core losses and that failure must not lock the event, and the AI matrix treats a recent core loss as a temporary condition.

## D2. Mission interruptions belong to the mission

Decision: every field validation, Reality Audit, narrow audit and Dual-Track start clears its own interruption record.
A Swedish core lost while that mission runs records `video_game_in_sweden_mission_core_lost` and counts toward `video_game_in_sweden_mission_core_loss_count`.
Losing Stockholm records `video_game_in_sweden_mission_capital_lost`.
One lost core makes a full result impossible and yields a partial report.
Stockholm or `video_game_in_sweden_event.several_core_losses` (2) lost cores cancel the mission into its failure result through the cancel trigger.
A daily check also records a capital loss caused by a treaty transfer that has no control callback.
Basis: spec part 3 Reality Audit success, partial and failure conditions.
Achievement disqualifiers for Stockholm loss are unchanged.

## D3. Trust the Model reassessment reads only surge-time mismatches

Decision: a battlefield mismatch is a wartime terrain, supply or enemy incident resolved while the surge is active.
Admitting one (the option that corrects the cabinet) ends the surge at the next daily review.
Dismissing them keeps the surge going until `video_game_in_sweden_event.trust_major_mismatch_count` (3) battlefield mismatches have accumulated in the same surge.
The marker `video_game_in_sweden_trust_model_major_mismatch` replaces the old reads of `incident_enemy_seen` and `enemy_adaptation`, is cleared when a surge starts and on closure, and `enemy_adaptation` is cleared on every incident-cycle reset and on closure.
Basis: spec part 2 lists a completed major mismatch as an early reassessment cause, while history from before the surge must not end it.
The admit-or-dismiss split gives the dismissing response a real cost in surge length and Reliance, which the spec asks for.

## D4. Evolution II always needs broad public reach

Decision: `video_game_in_sweden_begin_evolution_ii` and the maintenance Evolution I to II branch both require `video_game_in_sweden_broad_public_reach`.
The high-Chaos commercial opening already sets that flag, so it keeps its immediate Evolution II.
An officer or controlled programme that never widened civilian access therefore stays in Evolution I, which is the contained officer-culture route.
Basis: spec part 2 Evolution II eligibility and report 16 (Evolution I to II needs its broad-public-reach gate).

## D5. Staff reviews are audit proof, not audit start gates

Decision: `video_game_in_sweden_can_begin_reality_audit` no longer needs the rail-table or red-team review.
Two audit-phase rows appear only while a full or narrow Reality Audit is running and their review is missing: `video_game_advanced_logistics_review` (trains, lorries and a 30-day civilian office, reusing the logistics icon) and `video_game_independent_adjudicators` (political power and army experience, reusing the red-team icon).
Both are priced from `video_game_in_sweden_cost` constants, lower Reliance like their earlier counterparts and set the same proof flags.
The audit objectives now include both reviews, so an audit without them waits for its deadline and files a partial report through the timeout path.
They appear only during the audit because the Evolution II phase already shows five rows and the Evolution III choice phase is limited to four, while the recovery budget allows up to four rows.
Basis: spec part 3 lists the logistics review and independent adjudication as proof inside the audit, with partial success when independent review is skipped, and the decision map replaces the logistics module with an advanced review after Evolution II.

## D6. Audit outcomes only lower Reliance and keep a staged form

Decision: `video_game_in_sweden_cap_reliance` lowers Reliance to a band ceiling and never raises it.
Full audit caps at Habit (49), partial and Dual-Track at Doctrine (74), and completed restriction at Instrument (24).
A partial audit grants the existing `video_game_in_sweden_dual_track_package` as a provisional comparison staff for `provisional_dual_track_days` (120).
A failed audit restores Simulation Orthodoxy through the stage refresh, keeps the Reliance shed at the audit start, and applies Unresolved Field Findings for `reality_audit_failure_penalty_days` (120).
The latest result is stored in `video_game_in_sweden_audit_result` so report `.32` selects one text and one option even after a narrow reassessment follows an earlier result.
Basis: spec part 3 and the decision map result table (partial falls to Doctrine with a provisional dual-track form, failure leaves Orthodoxy weakened but unresolved).

## D7. Civilian-office reservations run their full term

Decision: the logistics module, protect shifts, foreign licences, Dual-Track and the advanced logistics review use `cancel_if_not_visible = no` with a lost-host `cancel_trigger`.
Each of these rows hides itself on completion, which previously cancelled the native timer at once and dropped the factory reservation the cost row promised.
Basis: offline Decision modding, cancel behaviour (cancel_if_not_visible copies visible into cancel_trigger), and the cost philosophy in spec part 3.

## D8. Rulebook Commander is an event-granted personality trait and a rare roll

Decision: the trait is `type = land`, `trait_type = personality_trait` with `new_commander_weight` factor 0, following the vanilla `war_hero` precedent in `common/unit_leader/00_traits.txt`.
It no longer uses `assignable_trait` or `gui_row = 16`, so it cannot appear in a corps commander's trait tree beside the purchasable CBRN trait on that row.
Assignment is a constant-weighted `random_list` roll through `video_game_in_sweden_roll_rulebook_commander`: 20 percent at the officer opening, 35 percent on choosing competitive command culture in `chaosx.nr24.11`, and 25 percent on formalizing the officer league.
The persistent `video_game_in_sweden_rulebook_commander_granted` flag limits the programme to one marked commander, even after validation removes the trait.
Validation, transfer, retirement and closure removal are unchanged.
Basis: spec part 2 commander rules (only one commander, rare route result, safe skip) and the installed `random_list` documentation, which accepts variable weights.

## D9. One variable-driven programme package carries the action payoffs

Decision: `video_game_in_sweden_program_package` is the single country dynamic modifier for every finite Event 24 action payoff, rebuilt by `video_game_in_sweden_refresh_program_package` from the `video_game_in_sweden_package` constants.
It carries the route secondary effect, the controlled exercise (with diminishing repeats until the war state changes), the rail-table supply saving, the rules-revision planning gain and adaptability cost, the officer league, the Evolution I choice package, the red-team trade, the field-validation training benefit, the preparedness recruitment benefit, the licence trade goodwill and the exhibition war support.
Timed parts count down in the daily runtime watch, and the modifier is detached during restriction, recovery and closure.
The logistics module no longer refunds support equipment, and on the commercial route it raises Reliance by `logistics_marketing_gain` instead of lowering it.
Planning values were kept small (3% per source) because the staged ideas already carry 5 to 15% planning speed, which keeps Evolution I near the spec's medium single-digit band above the idea.
Basis: spec part 3 action outcomes, spec part 2 civilian tradeoffs ("a clear package instead of scattered tiny modifiers") and lead decision 5.

## D10. Evolution II public costs scale by route, Reliance and choice

Decision: the National Strategy Craze idea keeps its recruitment and war-support benefits, and its productivity and political-attention costs move into the programme package.
Output cost 4% and attention cost 10% are multiplied by route (0.75, 1.0, 1.25), Reliance state (0.75, 1.0, 1.25) and the Evolution II choice (exhibitions 1.25, civic network 0.8), and each national league season adds 1.5% output cost up to four seasons.
Protected shifts cut output cost by 60%, a preparedness charter by 25%, and separate policy halves the attention cost and adds `separate_policy_evolution_delay_days` (90) to the Evolution III delay.
Option `.12.a` raises Reliance by `exhibition_gain` (6) and adds exhibition war support, `.12.b` also sets protected shifts, and `.12.c` records the civic network that lowers the cost factor.
The live costs appear in the category header during Evolution II.
Basis: spec part 2 civilian tradeoffs and Evolution II choices, spec part 3 balance targets (costs large enough to justify Protect Essential Shifts).
