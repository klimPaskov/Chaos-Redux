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
