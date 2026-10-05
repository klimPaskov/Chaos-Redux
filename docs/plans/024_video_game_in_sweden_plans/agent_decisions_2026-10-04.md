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

## D11. Evolution choices last and contained evolutions file their own conclusion

Decision: formal auxiliary doctrine caps Reliance at `auxiliary_reliance_cap` (55) on choice and blocks gains past that level while Evolution I lasts, so the officer opening at 62 becomes a contained staff culture.
Competitive command culture keeps its Reliance rise and commander roll and carries the strongest package.
Red-team supervision also sets `enemy_mismatch_reduced`, which removes the enemy-behaviour incident family, matching the red-team decision.
`video_game_in_sweden_close_ordinary_program` sets `conclusion_officer_culture` from Evolution I and `conclusion_craze_contained` from Evolution II, and report `.20` shows matching text and options with Validated Wargaming Methods or Municipal Campaign Clubs as the finite aftermath.
Incident frequency and evolution pacing effects of these choices are wired with the incident and pacing items.
Basis: spec part 2 Evolution I and II choices, Evolution I and II conclusions and resolution states 2 and 3.

## D12. Incidents carry priced, timed penalties and route-aware frequency

Decision: every incident response applies one timed Cabinet Mismatch modifier whose values are country variables set for the incident family, so the latest mismatch replaces an earlier one instead of stacking.
The penalty is priced when the incident is drawn, from a severity that multiplies the Reliance-state, war, high-Chaos, prior-validation and repetition factors, so the report tooltip shows the exact cost of each answer and nothing hidden appears after the choice.
Admitting halves both size and duration; durations stay within 30 to 90 days.
Because maintenance runs every 30 days, a cooldown scale could not change frequency, so a due incident instead fires with a percentage chance scaled by Reliance, officer competition, auxiliary doctrine, red team, field validation and Trust the Model.
Family weights were rescaled to hundreds so the random draw never depends on fractional weights.
The previously unread template, access, diplomatic and party flags now scale their family's weight, and the 0/1 temporary sentinels in incident selection were replaced by direct trigger checks.
Incidents pause during restriction enforcement and recovery through the live-package trigger.
Basis: spec part 3 incident severity and decision map penalties (one to three months), P24-I1 to I5, lead item on incident consequences.

## D13. Five more incident families, an Evolution III opening incident and a National Final

Decision: the incident pool gains casualties as counters (war support and recruitable population, war in Evolution III or at Worldview), the unexpected counterplan and the foreign bootleg (rare early incidents sharing `rare_incident_days`, 240), production without transport (Evolution III, peace-valid) and the perfect offensive (Evolution III at war, counts as a battlefield mismatch for Trust the Model).
`video_game_in_sweden_begin_evolution_iii` queues one opening incident chosen by campaign weights, with production without transport always available so a peaceful Sweden still receives one; it respects a pending incident and the severe-crisis pause.
The National Final fires once after `national_final_seasons` (2) league seasons; its result is drawn when it is scheduled so the report text and option always agree, and an upset lowers Reliance while the favourite raises it.
No new art was added; every new text uses the existing report picture.
Basis: spec part 2 Evolution III opening crisis incidents and national final, spec part 1 rare baseline incidents, report 16 open items.

## D14. Evolution pacing is accumulated progress at an MTTH pace

Decision: the fixed evolution delays become progress counters, one per evolution, that grow each maintenance by the 30-day interval times an MTTH pace from `common/mtth/024_video_game_in_sweden_mtth.txt`, but only while that evolution is eligible (Chaos tier, Reliance band, reach and enable checks in the new eligibility triggers).
An evolution fires when its progress reaches the unchanged base delay, so the base pace keeps the spec's four, five and four months, and campaign changes during the wait take effect from that month on.
A progress model was chosen over a single MTTH draw because the 30-day maintenance tick is the only sampling point and the spec factors change during the wait.
Separate policy keeps its explicit 90-day addition to the Evolution III threshold rather than a second pace factor, so the decision text stays exact.
An admitted mismatch is remembered for `admitted_mismatch_memory_days` (90) through a timed flag that slows all three evolutions.
Basis: spec part 2 evolution pacing and Evolution I to III pace factors, P24-E1A to E3B, chaos-redux-mtth skill.

## D15. Dual-Track verification proves an actual comparison

Decision: verification needs two costed actions shown only during the mission, independent staff plans and resolved differences, plus Stockholm and no supply gap after the proof period.
The second action requires the first, and missing either lets the mission time out into the existing failure, which offers the Reality Audit and restriction.
Player-facing dual-track text uses "dual-track staff" and "independent staff" instead of "second ledger".
Basis: decision map Dual-Track proof (independent plans, compared assumptions, resolved differences), audits 20 and 23, recovery-route budget of up to four rows.

## D16. Supplied divisions use a native proxy with an active-front alternative

Decision: lead decision 3 is implemented.
A training region (Skane 138, Sodermanland 141, Norrnorrland 666) counts as supplied when Sweden fully controls it, `divisions_in_state` shows at least two Swedish divisions, `any_state_division` finds a Swedish division with `unit_organization` above `video_game_in_sweden_supply_proxy.minimum_organization` (0.5), and `has_railway_connection` links it to Stockholm (141 is exempt); the national supply gap check stays in every mission objective.
The active front alternative is at war, more than `active_front_min_divisions` (3) divisions, surrender progress below `active_front_surrender_limit` (0.25), no core lost within the crisis memory, no supply gap, and a Swedish-controlled state bordering enemy-controlled ground that holds an organised Swedish division.
Field validation and the narrow reassessment accept either; the full Reality Audit accepts all three regions or an active front with the Stockholm region supplied, so a Sweden fighting abroad can still audit.
State ids stay literal in state scopes, `divisions_in_state` and `has_railway_connection`, documented beside the triggers as mirrors of the front-state constants.
Evidence: installed triggers documentation lists only `unit_organization`, `unit_strength` and template checks for divisions; the vanilla railway graph links 138 and 666 to 141; the proxy mirrors the Chaos Redux independence-wave "supplied division" organisation threshold.
Live-game check: whether `has_railway_connection` accepts paths through allied territory is needs_live_game.
Basis: spec part 3 Reality Audit setup (supplied divisions in three regions or equivalent active fronts), reports 16, 22 and 25.

## D17. A final review closes every Evolution III path, with a field follow-up and cheaper restriction

Decision: maintenance counts idle Evolution III time (a route used, no mission, no surge or reassessment, no recovery or restriction), and after `final_review_days` (150) report `.36` offers a provisional settlement (Reliance capped at Doctrine, closure, Independent Staff Comparison for `provisional_settlement_days`) or a forced restriction through the ordinary mission.
The Evolution I follow-up is a 45-day decision whose remove effect settles the re-test: a partial finding becomes full and a failed one becomes partial when a supplied region or active front, Stockholm and supply hold, clearing the failure penalty; report `.37` files the outcome.
The narrow reassessment consumes `followup_review_available` as the audit follow-up.
Failed field validation, audit or dual-track verification sets `video_game_in_sweden_restriction_fee_factor` to `restriction_failure_fee_factor` (0.5); the restriction quote scales each nominal charge by it before limiting the charge to the reserve, so displayed and paid amounts agree.
Basis: spec part 2 mandatory reassessment ("cannot remain indefinitely in Simulation Orthodoxy"), decision map field-validation and audit result tables, spec part 3 cheaper restriction after failure.

## D18. An ignored high-Reliance baseline receives a containment review

Decision: after `baseline_auto_close_days` with Reliance at or above Doctrine and neither evolution eligible, maintenance schedules report `.22`.
Debriefing caps Reliance at Habit and runs the ordinary conclusion; continuing costs `containment_continue_loss` (10) Reliance and is allowed once, after which the review returns in `containment_review_days` (120) with only the debrief, so the baseline always ends.
The AI weights are constants that favour containment (4 to 1).
Basis: spec part 1 ("an ignored high-reliance program should first offer containment"), AI principle 6 and P24-D5.

## D19. Foreign licences respect autonomy and sea access, and ridicule can backfire

Decision: a subject below `autonomy_dominion` may license only to its overlord or faction partners, and non-neighbour partners need a coastal Sweden with open sea lanes (at peace, or at war with `enemies_naval_strength_ratio` above `foreign_blockade_naval_ratio`, 0.5); both rules live in the partner validity trigger so the existing availability tooltip covers them.
The licence AI factor drops for a subject and for closed sea lanes in war.
Ridiculing partners are stored in a host array, and a later peace with the recent-victory flag and no recent core loss gives each a finite political embarrassment once.
The four response opinion modifiers now decay by one point a month, matching their file description as temporary impressions.
Basis: spec parts 1 and 3 on subject caution and blockaded licensing, spec part 2 ridicule row, decision audit 23.

## D20. Event options state their consequences and hide raw operations

Decision: every player-facing option in the opening, evolution, conclusion, incident, report, foreign-response, final-review and reassessment events shows a `custom_effect_tooltip` with its Reliance movement and main consequence, built from constants or the incident's priced variables, while the scripted effects that change variables and flags run inside `hidden_effect`.
Visible resource awards in conclusions stay as native effect lines.
Report options whose result was applied when the mission closed state that result instead of repeating it.
Basis: spec part 4 (every action shows its Reliance direction, no hidden cost after commitment).

## D21. Trust the Model victories soften the reassessment and widening is route-sensitive

Decision: the surge modifier carries `trust_war_support` (+5% war support), and `video_game_in_sweden_open_trust_reassessment` lowers Reliance once by `trust_victory_relief` (15) when an opponent victory is recorded, which report `.50` states; the path choice stays mandatory.
The widening decision formalises the officer league inside the army on the officer route (league package, commander roll, no broad reach) and can be taken a second time there to publish the tables, which gives the reach an officer programme needs for Evolution II; other routes keep civilian circulation.
The decision can therefore repeat (`fire_only_once = no`) but hides once broad reach exists.
Basis: spec part 2 Trust the Model (strong war support, a victory softens but cannot remove the reassessment), spec part 3 expand access and officer league (public reporting raises Evolution II pressure).

## D22. Player text drops receipt and ledger wording

Decision: player-facing Event 24 text uses departmental reports, staff manuals, conclusion of the trial and a shorter list of questions instead of receipts and ledgers, and the requirement-flag texts describe the campaign cabinet state in plain terms; the disqualifier flag reads as a requirement ("a review has already found the cabinet wanting, or Stockholm has been lost") rather than naming an achievement.
Trust the Model now shows its stated requirement tooltip instead of the raw trigger lines, and that tooltip names the earlier-review condition.
No Event Details or evolution title or body changed, so no catalog change is pending.
Basis: lead item on implementation jargon, repository player-text rules.

## D23. AI covers ideology, autonomy, Totalen Chaos, threshold caution and plausible audits

Decision: opening, evolution-choice, foreign-response, incident and Evolution III weights gain constant factors from `video_game_in_sweden_ai_factor` for government (democratic, neutrality, fascism, communism), low-autonomy subjects, Totalen Chaos and high tension.
Reliance-raising decisions (widening, rules revision, officer league, national league, preparedness, licences) fall to 0.1 when `video_game_in_sweden_ai_avoids_reliance_gain` holds: a severe crisis with Reliance within 10 of Doctrine or Worldview while the stage it would feed is enabled.
The full audit AI falls to 0.2 without the full field package and the narrow audit without a supplied region or active front; restriction is halved outside a crisis and doubled past 50% surrender progress; dual-track falls in a crisis; Trust the Model rises under Totalen Chaos and fascism and falls for democracies and low-autonomy subjects; admitting an incident weighs 1.5 at war.

Source-reasoning orderings (raw scores, not normalized probabilities):
- P24-O1 calm democratic peace: controlled 10.8, commercial 4.5, officer 1.2.
- P24-O2 democratic rearmament with low experience and high tension: controlled 7.6, commercial 6.8, officer 1.7.
- P24-O3 fascist Sweden at war with low experience: officer 14, controlled 1.1, commercial 0.5 to 0.7.
- P24-O4 emergency: controlled 16 to 32, officer 0.25, commercial 0.
- P24-C1 stable democracy (controlled route): red team 4.8, auxiliary 3.9, competitive 1.1; P24-C2 fascist wartime officer route: competitive well above auxiliary, red team about 1.3.
- P24-C3 strong industry and high tension: exhibitions 4.8 and civic 3.2 to 4.8 above protected shifts 2; P24-C4 crisis: protected shifts 12, civic 4.8, exhibitions about 0.04.
- P24-C6 stable Totalen militarised Sweden at war (officer route): Trust the Model about 9.5, dual-track about 5, audit 3.5, restriction 2; P24-C7 near capitulation: restriction about 16, audit 0.7 or less without a package, dual-track low, Trust the Model invalid.
- P24-C5 supply failure with a lost core: restriction 8 leads the audit, because acceptance principle 8 (no audit without the plausible package) overrides the matrix row where a supply gap breaks the package; the audit leads once the package and supply hold.
- P24-F1 to F4 keep their orderings, with faction copy (2.5), democratic peaceful study (1.5) and communist ban (1.8) added.

MCP blocker: `hoi4.probability_inspect` (adapter `event_option_ai_chance`, source `{path: events/024_hearts_of_iron.txt}`, pool `chaosx.nr24.2.a/.b/.c`) returned `INTERNAL_ERROR` with no artifact; other source shapes and a `hoi4.probability_compare` attempt for P24-O1 and P24-O3 (before snapshot hash `27098a747576f3498063148c73caf755a1b0537fae0c0726d2852afaa89cac41`) were rejected as invalid arguments because the scenario schema is not published in the tool description.
No numeric probability acceptance is claimed; the scenario ids above remain for the auditor pass.
Basis: spec part 3 AI route matrix and principles 1, 2, 8 and 10, foreign response table, probability scenario file.

## D24. Post-implementation review corrections

Decision: a source review of the finished round found three defects and one stale regression fixture, and each was corrected rather than queued.
The field-validation decision listed its whole start package as raw trigger lines beside the custom requirement tooltip, which exposed the supplied-region proxy internals and the unlocalised `video_game_in_sweden_core_loss_recent` flag; the raw line was removed, so the custom tooltip (which already holds the same check hidden) is the only visible requirement.
Report `.36` weighted the provisional settlement down at peace and the forced restriction up only in a crisis, so a peaceful AI chose restriction; the peace factor now lowers the restriction and the dual-track crisis factor lowers the settlement, so peace settles and a wartime crisis restricts.
The rail-table description read "supply consumption falls by -5%", and the Reality Audit description named only the three regions although the active-front alternative is accepted; both texts now state the signed modifier and the front alternative.
The bounded runtime-observation fixture in `tests/test_runtime_observation.py` now bridges `clear_array`, `force_update_dynamic_modifier`, one-sided `clamp_variable` and untimed `add_dynamic_modifier`, and its restriction case ignores the untimed programme package that the closure detaches again; all 14 cases pass.
Basis: CLAUDE.md player-visible requirement rule for flags, spec part 3 recovery AI (restriction is the crisis route), repository player-text rules.

## D25. Skeptical review corrections

Decision: an independent review of every round-1 commit found two reachability defects, one lost-content edge and four stale texts, and corrected each rather than queueing it.
The officer route had no reachable source of broad public reach: the widening row was baseline-only, the officer opening at Gathering Storm or higher enters Evolution I at once, and an officer baseline opened below that reaches Evolution I about 90 days after Chaos rises to Gathering Storm while the league widening reserves the row for `opening_review_days` (120), so the press step promised by D21 could never be taken and D4 locked the officer route out of Evolution II, Evolution III and Trust the Model, contrary to AI scenarios P24-C2 and P24-C6.
`video_game_expand_access` is now also visible through `video_game_in_sweden_can_publish_officer_tables` (Evolution I, officer route, formal league, no broad reach), where its existing route-sensitive body publishes the tables; it stays baseline-only for the other routes, as spec part 3 describes, and the officer league row it replaces is already hidden once the league is formal, so the Evolution I row count does not grow.
`video_game_in_sweden_evolution_iii_is_idle` no longer excludes an Evolution III whose initial choices are still open, so a programme that never chooses a route also reaches the final review after `final_review_days` (150) instead of keeping Simulation Orthodoxy indefinitely (spec part 2 mandatory reassessment, the stated basis of D17).
Report `chaosx.nr24.35` required `evolution_ii_active`, so a national final scheduled shortly before Evolution III began was silently lost; it now requires a recorded Evolution II and a live programme package (not restricted, recovering or closed).
Texts: the full audit result names "any Rulebook Commander" because the trait is rare (D8), the dual-track description states the Doctrine cap instead of "returns to Doctrine" (D6 changed it to a cap), and the audit cost tooltip names the field proof rather than a three-region proof (D16 active-front alternative).
Basis: D4, D16, D17 and D21 as accepted, spec part 2 Evolution II eligibility and mandatory reassessment, spec part 3 AI route matrix.
Implementation evidence is source review only; the officer press timing and the final review of an untouched Evolution III are needs_live_game.

## D26. Second skeptical review pass

Decision: a second review of every round-1 commit and of the D24 and D25 corrections found one silent outcome and two presentation defects, and corrected each rather than queueing it.
A field validation, Reality Audit or Dual-Track mission cancelled by lost ground (Stockholm or `several_core_losses` cores, D2) applied its failure result without any report, because only the timeout path filed `chaosx.nr24.31`, `.32` or `.33`; the mission `cancel_effect` now calls `video_game_in_sweden_cancel_field_validation_mission`, `video_game_in_sweden_cancel_reality_audit_mission` or `video_game_in_sweden_cancel_dual_track_mission`, which run the unchanged failure and then file the ordinary failure report only when `video_game_in_sweden_reports_lost_ground_failure` holds (current host, event enabled, lost ground) and the failure was actually recorded, so a lost host, a disabled stage or the end of the world still closes the mission quietly.
The foreign licence `available` block repeated the supply-gap check, the partner search and the pending-packet check as raw trigger lines beside the custom tooltips that already hold them, which exposed the expanded partner rules from D19 (autonomy, overlord, faction, sea lanes) as raw trigger text; the raw duplicates were removed, the pending-packet check stays in `visible`, and gating is unchanged because each custom tooltip still evaluates its hidden trigger (the D24 precedent).
The final review restriction option `.36.b` said only "at its current price"; it now shows the actual reserve-limited charges and the Reliance loss with the same getters as the Trust the Model reassessment (D20 basis: every option states its consequence).
The overview now lists lost-ground cancellation among the mission cancellation causes and names the perfect offensive among the battlefield mismatches (D13).
Basis: D2, D13, D19, D20 and D24 as accepted, CLAUDE.md player-visible requirement rule, chaos-redux-decisions-missions trigger clarity rules.
Implementation evidence is source review and the bounded runtime-observation fixture (14 cases pass); the report timing after a lost-ground cancellation is needs_live_game.

## Round 2 decisions

Disposition: accepted under the same standing grant of design authority, taking the round 2 lead's decisions as the basis.
Implementation evidence is source review and the bounded runtime-observation fixture; anything only the engine can show is marked needs_live_game.

### R2-1. Timed flags read their day count from a normal variable

Finding: six timed flags (`video_game_in_sweden_core_loss_recent`, `video_game_in_sweden_capital_loss_recent`, `video_game_in_sweden_rare_incident_recent`, `video_game_in_sweden_mismatch_admitted_recent`, `video_game_in_sweden_diplomacy_active` and `video_game_in_sweden_recent_victory`) passed the bare temporary variable `video_game_in_sweden_flag_days` as `days`.
Installed `common/scripted_effects/SOV_scripted_effects.txt` (the commented line near line 28) notes that a timed flag does not take a variable that way, while `SIA_scripted_effects.txt` line 780 sets a normal variable from a script constant and passes it as `days = var:SIA_new_propaganda_campaign_duration_left`.
If the day count were ignored, the crisis memory flags would never expire and `video_game_in_sweden_core_loss_crisis` would stay on, which would undo D1.
Decision: each site now sets the normal country variable `video_game_in_sweden_flag_days` from its `video_game_in_sweden_timing` constant and passes `days = var:video_game_in_sweden_flag_days`, the SIA form; no Event 24 timed flag uses a temporary variable or a `constant:` token.
The variable is overwritten before every use, like the SIA precedent, so it needs no separate cleanup.
`add_dynamic_modifier` and `add_timed_idea` keep their variable day counts, because the installed effects documentation says dynamic-modifier days can be a variable and vanilla `SOV.txt` passes a variable to `add_timed_idea`.
Basis: round 2 lead decision 1, Event 23 R2-2, CLAUDE.md 1.9.
Disposition: `implemented`; the flags actually expiring is needs_live_game.

### R2-2. A peaceful baseline and Evolution I draw real incidents

Finding: in peace the baseline and Evolution I could only draw the counterplan and the bootleg, which share the 240-day rare cooldown, because the terrain, supply and enemy families needed war (or a supply gap) and the template family needed broad public reach and Evolution II or III.
The decision map incident table gives enemy adaptation to a "repeated preferred scenario, weak red team" and the standardized template to an "officer league, high Reliance", spec part 1 lists "The logistics table is wrong" and "The perfect template craze" as rare baseline incidents, and spec part 2 puts over-standardized divisions among the Evolution I risks.
Decision: the existing families widen their preconditions; no new family is added.
- Supply: `video_game_in_sweden_incident_logistics_table_is_valid` (baseline or Evolution I, Habit Reliance or above, no rail-table review) is an alternative to a real supply gap. Without a gap the draw weight is `supply_table_weight` (75) instead of `supply_weight` (200), and the report shows the new timetable clause.
- Enemy: `video_game_in_sweden_has_repeated_preferred_scenario` (controlled exercise strength below one, meaning at least one repeat in the same war state, or an officer league or competitive culture, and no red team) is an alternative to war. In peace the weight is multiplied by `enemy_peace_factor` (0.75), and the report shows the exercise-umpire clause.
- Template: `video_game_in_sweden_incident_early_template_is_valid` (baseline or Evolution I before a successful field validation, with Evolution I officer competition or Doctrine Reliance or above) is an alternative to the public path. In the baseline the weight is multiplied by `template_baseline_factor` (0.5), and option `.30.template_b` reads "training timetable" so it fits both paths.
The red team (`red_team_complete`, `enemy_mismatch_reduced`), the rail-table review (`logistics_review_complete`, `logistics_mismatch_reduced`) and field validation still suppress their families.
Peacetime severity keeps every factor except war (1.5), so a Habit-stage peacetime report stays small and short (spec part 3: "embarrassing and temporary"); dismissing a supply report sets `video_game_in_sweden_supply_crisis` only at war, so a peacetime timetable error cannot raise the severe-crisis gate.
Trust the Model still counts only wartime reports as battlefield mismatches (`video_game_in_sweden_record_trust_mismatch` requires war).
The officer-competition check is one trigger, `video_game_in_sweden_has_officer_competition`, shared by the fire chance, the template weight and the new paths.
Probability surface: the incident family `random_list` gains three peacetime entries; no existing weight changed. The MCP comparison is blocked (see R2-8).
Basis: round 2 lead decision 2, decision map incident pool, spec parts 1 to 3.
Disposition: `implemented`; draw frequencies in a live campaign are needs_live_game.

### R2-3. Decision requirements show each condition once and never the host internals

Finding: the narrow-reassessment and dual-track rows listed `video_game_in_sweden_can_begin_narrow_reality_audit` and `video_game_in_sweden_can_use_dual_track` as raw requirements beside custom tooltips that already evaluate them (the D24 and D26 defect class); 16 `available` blocks, 7 decision `cancel_trigger` blocks and 4 mission `cancel_trigger` blocks used `video_game_in_sweden_is_current_host`, whose tooltip expands into event-target, tag, `exists`, `original_tag` and capitulation lines; the mission cancel triggers also showed the raw global flags `events_log_disabled_evolution_24_24_1` (unlocalised) and `world_end`; and the logistics, national-league and foreign-licence rows repeated their factory or stability requirement two or three times.
Decision:
- Every `available` host check is a `hidden_trigger`. The category's own `visible` block already requires the current host, so a visible host line could never be the reason a shown row is blocked.
- Decision cancel triggers show one localised line, `video_game_host_lost_tt`.
- Each mission cancel trigger shows `video_game_program_ended_tt` (host lost, event or stage switched off, or the world has ended) beside the existing lost-ground line.
- The narrow-audit, dual-track and conclude-trial checks are `hidden_trigger`, as the begin-audit row already was; their custom tooltips or `visible` blocks state the requirement.
- Logistics module: the raw factory line is removed, and `video_game_in_sweden_can_pay_logistics_module` no longer checks the factory, because that cost row shows no factory. `video_game_logistics_capacity_tt` remains the single factory requirement.
- Advanced logistics review: the factory tooltip is removed, because its cost row and cost check already include the factory.
- National league: the raw stability and factory lines are removed; stability stays in its tooltip and the factory in the cost check.
- Foreign licences: the raw factory line is removed; the cost check keeps it.
Which rows can be taken does not change: every removed visible line is still evaluated in `available`, and `can_pay_*` cost checks stay visible in `available`, as lead decision 6 requires.
Basis: round 2 lead decision 6, D24 and D26 precedent, CLAUDE.md player-visible requirement rule, chaos-redux-decisions-missions trigger clarity.
Disposition: `implemented`; the rendered tooltip wording is needs_live_game.

### R2-4. The audit and field-validation requirement texts name every hidden condition

Finding: `video_game_reality_audit_requirements_tt` named only Stockholm, reserves, stability and the full-report proof, although the hidden `video_game_in_sweden_can_begin_reality_audit` also checks `video_game_in_sweden_has_field_start_package` (an army, one supplied training region or an active front, and no wartime supply gap), so a player could see every listed condition met while the row stayed blocked; `video_game_field_validation_resources_tt` omitted the army and the no-supply-gap condition that also applies to the training-region path.
Decision: both texts now name the army, the supplied training region in Skane, Sodermanland or Norrnorrland or an active front (with the shared `$video_game_supplied_region_rule$`), the wartime train, lorry and fuel condition "whichever proof is used", Stockholm, the reserves after payment and, for the audit, the stability floor; the audit text still states separately what a full report needs.
No gating changed.
Basis: CLAUDE.md player-visible requirement rule (state the real requirement), chaos-redux-decisions-missions trigger clarity.
Disposition: `implemented`.

### R2-5. The category "Next review" line is current in every phase

Finding: `GetVideoGameReassessment` showed `video_game_in_sweden_trust_model_reassessment_deadline` whenever the variable existed, so after a Trust the Model reassessment the header kept a past date (for example during the audit mission), and every other phase read "N/A" although the source tracks the baseline review and automatic conclusion, the containment review, the idle Evolution III final review and mission proof days.
Decision: the selector shows, in order of precedence:
- the Trust the Model deadline only while the surge is active or its reassessment is pending;
- for a running mission, proof days completed out of the days its report needs (`video_game_in_sweden_mission_elapsed_days` against the field, full audit, narrow audit, dual-track or restriction proof constant);
- in the baseline, when the trial can be concluded and when it concludes on its own, or the containment review date for a trial at Doctrine Reliance or above that cannot evolve;
- in an idle Evolution III, the final review date, or "in about 150 days" before the first idle maintenance check;
- otherwise "No review scheduled".
The dates are display variables (`video_game_in_sweden_trial_review_date`, `video_game_in_sweden_trial_close_date`, `video_game_in_sweden_final_review_date`) set by `video_game_in_sweden_refresh_review_dates` from the day counters through `chaosx_convert_days_to_date_offset`. It runs when the programme starts and after each maintenance check, which is the only time those counters change, so the dates never go stale between checks. No gameplay logic reads them.
The deadline variable itself is not cleared, because the reassessment logic still reads it; the flag gate in the selector is enough.
Basis: round 2 lead decision 4, spec part 4 accessibility ("the category should show the next review or active mission clearly").
Disposition: `implemented`; the rendered dates are needs_live_game.

### R2-6. Reality Check is disqualified only by the spec's conditions

Finding: `video_game_in_sweden_reality_check_disqualified` was both the achievement disqualifier and the gameplay "found wanting" gate (Trust the Model availability and the field-validation, Trust the Model and foreign-response AI factors). As a result, a failed Evolution I field validation, a failed dual-track verification, or losing Stockholm at any time since the event fired permanently blocked Reality Check, although spec part 4 lists only debug paths, restriction instead of the audit, a partial or failed audit, Reliance returning to Doctrine during the proof year, and losing Stockholm during that year.
Decision: the new flag `video_game_in_sweden_cabinet_found_wanting` carries the gameplay finding. It is set by a failed field validation, a partial or failed audit, a failed dual-track verification, and a lost Stockholm (control callback and maintenance check), and cleared when a programme starts.
It replaces the old flag in the Trust the Model gate (`video_game_in_sweden_can_use_maximum_risk_route`), in the field-validation and Trust the Model `ai_will_do` factors, and in the three foreign-response `ai_chance` factors. The Trust gating accepted in D22 is therefore unchanged in behaviour, and the Trust the Model requirement text now also names the earlier loss of Stockholm.
Reality Check is now disqualified only by:
- switching the event or a stage off (the A9 settings path; debug and force-trigger paths stay in the eligibility trigger through `debug_invalid` and `normal_campaign`);
- restriction, the provisional settlement or a dual-track settlement instead of the audit;
- a partial or failed audit, or a full result reached only through a narrow reassessment;
- after the full report: Reliance at Doctrine or above, the loss of Stockholm, or an invalid or lost host.
Failed field validation and failed dual-track no longer disqualify, so the Reality Audit stays a real route to the achievement afterwards. A host loss or capital loss before the full report records the finding, but does not end the achievement.
According to Plan disqualifiers are unchanged, and the D2 note that Stockholm loss disqualifies both achievements is superseded for Reality Check by this entry.
The achievement tooltip lists the new disqualifiers, and the old flag's requirement text now names the achievement, since it no longer gates any visible requirement.
The runtime fixture's Stockholm-loss case now checks both sides of the full report; all 14 cases pass.
Basis: round 2 lead decision 3, spec part 4 Reality Check core route and disqualifiers, spec A9.
Disposition: `implemented`; achievement unlock is needs_live_game.

### R2-7. Only one reassessment report per reassessment

Finding: `video_game_in_sweden_start_trust_model` always queues `chaosx.nr24.50` for day 365, and the runtime watch, maintenance and control-loss paths queue another `.50` when they open an early reassessment. If the early report was still unanswered when the one-year report fired, its trigger passed because the reassessment was still pending. Answering the first report then started a mission, and every option of the second (all require no active mission) was invalid.
Decision: `.50` sets `video_game_in_sweden_reassessment_shown` in its `immediate` block and requires it absent in its trigger. The flag is cleared wherever `video_game_in_sweden_mandatory_reassessment_pending` is cleared: programme start, Trust the Model start, `video_game_in_sweden_mark_trust_reassessment`, disabled-stage cleanup and closure.
The fixed 365-day schedule stays, so the reassessment still arrives within one year even though maintenance runs only every 30 days and an early review could otherwise come as late as day 390.
While `.50` is pending, the category's audit, dual-track and restriction rows are hidden (their `visible` blocks need open initial choices or an active surge), so no mission can start between the report appearing and the answer; the restriction option therefore stays available whenever `.50` is shown.
Basis: round 2 lead decision 5, spec part 2 Trust the Model (a mandatory reassessment no later than one year).
Disposition: `implemented`; the popup sequence is needs_live_game.

### R2-8. AI route matrix probability pass remains blocked

Finding: CLAUDE.md requires a `chaosx_ai_probability_auditor` baseline and `hoi4.probability_compare` pass for the D23 scenarios (P24-O1 to O4, C1 to C7, F1 to F5) and for every weighted surface changed this round.
Evidence this round: one narrow `hoi4.probability_inspect` call with adapter `event_option_ai_chance` and the documented in-memory selector `source: {inlineClausewitz: <two-option test event>}` (format from the installed package's `docs/probability.md`, "Proposed patches"), without `refresh`, returned `{"artifactCount":0,"code":"INTERNAL_ERROR","status":"error","workspaceId":"current"}`. The round 2 lead had the same result for the path selector, the identifier-plus-path selector and an inline event, so the service fails regardless of input. Following the task rule, it was not retried.
Weighted surfaces changed this round, for the auditor once the service works:
- The incident family `random_list` in `video_game_in_sweden_select_incident_family` gains peacetime entries (R2-2: `supply_table_weight` 75, `enemy_peace_factor` 0.75, `template_baseline_factor` 0.5); existing weights are unchanged.
- The field-validation and Trust the Model `ai_will_do` factors and the three foreign-response `ai_chance` factors now read `video_game_in_sweden_cabinet_found_wanting` (R2-6). For the decision factors the triggering states are the same as before, because only a failed field validation or a lost Stockholm can precede those rows. The foreign factors no longer fire after a completed restriction, a dual-track success, a provisional settlement, a full result reached through a narrow audit, or Doctrine Reliance after the full report.
- Option `.30.supply_b` no longer sets the supply crisis in peace (R2-2), which removes a peacetime path into the severe-crisis AI factors.
Decision: no numeric probability acceptance is claimed for D23 or this round. Once an inline test no longer returns INTERNAL_ERROR, the auditor runs the baseline and compare with the documented scenario schema (`schemaVersion`, `scenarios[].actor/state/flags`, and `scopes` bindings for the foreign-response `event_target:video_game_in_sweden_host` factors) against the scenario ids in D23, and the results are recorded against D23.
Disposition: `blocked` (missing input: a working `hoi4.probability_*` route).

## Round 3 decisions

Disposition: accepted under the same standing grant of design authority, taking the round 3 lead's decisions as the basis.
Implementation evidence is source review and the bounded runtime-observation fixture; anything only the engine can show is marked needs_live_game.

### R3-1. A switched-off next stage holds Reliance below its gate, and every step back lands in the conclusion band

Finding: `video_game_in_sweden_handle_disabled_evolution` stepped the phase back without capping Reliance except in the Evolution I branch, so switching Evolution III off during a Trust the Model surge left Evolution II at 100, which no remaining one-time reduction could bring below Doctrine; with Evolution III off from the start, national league seasons could push Evolution II into Worldview with no exit (spec part 2 "No Worldview-stage lock may remain", acceptance A9).
The trigger `video_game_in_sweden_next_evolution_disabled` existed but was never read.
Decision:
- `video_game_in_sweden_change_reliance` stops gains just below the switched-off stage's gate while `video_game_in_sweden_next_evolution_disabled` holds: `habit_max` (49) for the baseline with Evolution I off and for Evolution I with Evolution II off, `doctrine_max` (74) for Evolution II with Evolution III off. It follows the auxiliary-cap pattern: losses are never limited, and a value already above the ceiling holds but cannot rise. The ceilings are the existing band constants, so the bands remain the single tuning point.
- The trigger now excludes a commercial baseline whose Evolution II is still on, because that baseline can step straight into Evolution II (spec part 2: "Evolution II and III cannot require" Evolution I); with both off it is held at Habit like any other baseline.
- Every step-back branch (III to II, I or baseline; II to I or baseline; I to baseline) caps Reliance at `habit_max` through `video_game_in_sweden_cap_reliance`, which refreshes the Reliance state, achievement tracking and programme package, and then rebuilds the stage idea. The Evolution I branch's old direct `set_variable` is replaced by the same call.
- The category header's next-threshold text reads "none while the next stage is switched off" with the ceiling, or "cannot rise further" when Reliance is already above it, so it never names an unreachable threshold.
- `video_game_in_sweden_ai_avoids_reliance_gain` also holds while the next stage is off and Reliance is at Doctrine or above, so the AI's widening, rules revision, officer league, national league, preparedness and licence weights fall to the existing 0.1 factor when a gain would only delay the conclusion. This is a new branch on an existing weighted surface; its probability comparison joins the blocked R2-8 list.
Rejected: a separate containment review for Evolution I and II (lead decision, adds a surface without need).
Trace (fixture cases `test_switched_off_next_stage_holds_reliance_below_its_gate` and `test_step_back_from_a_switched_off_stage_lands_in_the_conclusion_band`, every fixture case passes): Evolution II at 70 with Evolution III off goes 74, 74, 56, 70 for +14, +6, -18, +14, while the same +14 with Evolution III on reaches 84; Evolution III switched off at Reliance 100 returns to Evolution II at 49, and with protected shifts `video_game_in_sweden_can_conclude_low_value` holds.
Basis: spec part 2 Disabled evolution handling, acceptance A9, the README rule that Reliance is capped at a safer public band, round 3 lead decision on the disabled-stage fix.
Disposition: `implemented`; the header rendering is needs_live_game.

### R3-2. Trust the Model victories are recorded at the capitulation and the surge war is watched daily

Finding: `video_game_in_sweden_update_trust_model_progress`, the only place that recorded an opponent victory, ran only from the 30-day maintenance and when a reassessment opened. An opponent that capitulated and was annexed before the next check no longer reported `has_capitulated`, so the victory counted only if an earlier monthly sample had crossed the war-score threshold, and a meaningful war declared and won inside one month was never captured. Both silently broke According to Plan.
Decision:
- `on_capitulation` (ROOT is the capitulating country, FROM the winner: offline wiki "On actions", Diplomacy/War section, lines 244 to 418, revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`, and vanilla `common/on_actions/00_on_actions.txt` line 931, whose example checks `has_war_with` inside the callback) calls `video_game_in_sweden_record_opponent_capitulation`. It compares the capitulating country with `event_target:video_game_in_sweden_trust_model_opponent`, requires that it is still at war with the host, and then, on the host, requires the current host, an active surge, Stockholm owned and controlled and a date no later than the reassessment deadline before it records `video_game_in_sweden_trust_model_opponent_victory` and the victory date. It reads only the two stored pointers and never iterates countries.
- The daily runtime watch runs `video_game_in_sweden_update_trust_model_progress` while the surge is active and Sweden is at war. That helper already captures the opponent (iterating only Sweden's enemies), refreshes the war-seen and war-score flags and records a victory once the opponent leaves the war with the threshold reached, so the daily watch needs no second copy of that logic.
- A capitulation of any other country, or one after the deadline, records nothing.
Fixture: `test_opponent_capitulation_is_recorded_before_an_annexing_peace` shows the monthly review alone missing an annexed opponent whose sampled war score stayed low, the capitulation callback recording it at day 110, the annexing review keeping it, and `video_game_in_sweden_mark_trust_reassessment` granting the favourable result; `test_war_declared_and_won_between_monthly_checks_is_recorded` shows the opponent stored on the first day of the war and the victory recorded on the day of a non-capitulation peace, with report `.50` queued.
All 18 fixture cases pass.
Basis: spec part 4 According to Plan ("win or force peace before the reassessment"), round 3 lead item.
Disposition: `implemented`; the engine's callback order during a capitulation and peace conference is needs_live_game.

### R3-3. Requirement lists hide the payment and mission helper internals

Finding: Restrict Use listed `video_game_in_sweden_can_pay_restriction` in `available`, which expands into the always-true quote helper `video_game_in_sweden_quote_restriction` (an OR with `NOT has_variable` on the fee factor, `set_temp_variable` and clamp lines); Rules Revision's `video_game_in_sweden_can_pay_rules_revision` showed two `has_variable` lines naming raw variables; and six rows (rules revision, field validation, targeted follow-up, red team, officer league, Trust the Model) listed the four `has_active_mission` lines of `video_game_in_sweden_no_active_mission`.
Decision:
- Restrict Use's payment check is a `hidden_trigger`: the quote limits every charge to the reserve at hand, so the check always passes, and the cost row already shows the quoted charges (the decisions skill allows `hidden_trigger` when the cost row explains the payment).
- The two `has_variable` guards in `video_game_in_sweden_can_pay_rules_revision` sit in a `hidden_trigger` inside the scripted trigger, so the requirement list and the cost check show only the army experience and command power thresholds.
- Each visible `video_game_in_sweden_no_active_mission` line in an `available` block is one `custom_trigger_tooltip` with the new key `video_game_no_other_mission_tt` ("No other campaign cabinet mission is running") around the hidden check; the checks in `visible` blocks are unchanged.
Which rows can be taken does not change, because every hidden check is still evaluated, and the simple resource `can_pay_*` lines stay visible (round 2 lead decision 6).
Basis: CLAUDE.md player-visible requirement rule, chaos-redux-decisions-missions trigger clarity, R2-3 precedent.
Disposition: `implemented`; the rendered tooltips are needs_live_game.

### R3-4. Simulation Orthodoxy carries operational costs

Finding: spec part 3 makes Orthodoxy strong but dangerous, with supply, adaptability, organisation-recovery, stability or political costs, but `video_game_simulation_orthodoxy` gave +5% army organisation (`army_org_factor`) and cost only -5% stability and -0.08 daily political power, so Evolution III was nearly free while no incident ran.
Decision: the organisation bonus becomes an organisation-recovery cost, `army_org_regain = -0.03`, and the idea adds `supply_consumption_factor = +0.04`; the planning benefits (+15% planning speed, +15% maximum planning, -10% land doctrine cost) are unchanged.
Both costs stay below the Trust the Model surge (`trust_army_org` -0.05, `trust_supply` +0.08), which stacks on top while a surge runs.
Both tokens are listed in the installed `documentation/modifiers_documentation.md` (`army_org_regain` at line 1957, `supply_consumption_factor` at line 4966).
The idea description now names the cost in period terms (worn formations receive orders written for fresh ones, supply columns follow roads the tables assumed), and the overview lists the full modifier set.
Basis: spec part 3 Simulation Orthodoxy, round 3 lead decision on Orthodoxy.
Disposition: `implemented`; balance in a live war is needs_live_game.

### R3-5. The restriction backlash is visible

Finding: `video_game_in_sweden_restriction_backlash` had no icon, and the offline Modifiers wiki (line 125) says a dynamic modifier without an icon is hidden, so the stability penalty after a completed restriction never appeared in the spirits bar, a hidden cost after commitment that spec part 4 forbids.
Decision: the modifier uses the existing Event 24 sprite `GFX_idea_024_video_game_in_sweden_national_craze` (registered in `interface/chaosx_ideas.gfx`), the same sprite as the other public-reaction modifiers (foreign ban, ridicule, embarrassment); its name and description keys already exist, and the restriction cost and report tooltips already state the value and duration.
Basis: offline wiki Modifiers line 125, spec part 4 accessibility.
Disposition: `implemented`; the spirits-bar display is needs_live_game.

### R3-6. The school and study-circle campaign is an Evolution II public report

Finding: spec part 2 lists four Evolution II public event families; workplace leagues, political appropriation and the National Final exist, but school and study-circle campaigns (keep it educational, turn it into recruitment, or limit state involvement) had no event, although the research notes make study circles central to the Swedish civilian route.
Decision:
- A one-shot report `chaosx.nr24.38` in the National Final pattern, not a mismatch incident, because the spec presents it as a public event with three policy choices (round 3 lead decision).
- Maintenance calls `video_game_in_sweden_queue_study_circle_campaign` after the evolution checks. It queues the report one day later once `video_game_in_sweden_study_circle_campaign_is_valid` holds (current host, event and Evolution II enabled, Evolution II active, broad public reach, live programme package, not yet shown) and the craze has run `study_circle_delay_days` (60). The report sets `video_game_in_sweden_study_circle_campaign_shown` in `immediate`, so a report whose trigger fails one day later is offered again at the next check rather than lost, and it is never shown twice. The marker and the three choice flags are cleared when a programme starts.
- Options, each with a `custom_effect_tooltip` built from constants and its scripted body in `hidden_effect`:
  - Civic education: Reliance -`school_educational_loss` (3), and `stability_factor` +`school_civic_stability` (2%) for `school_benefit_days` (180) through a new `video_game_in_sweden_pkg_stability` line on the programme package.
  - Recruitment: Reliance +`school_recruitment_gain` (6), and recruitable population +`school_recruitable` (2%) for 180 days through the package; no permanent windfall.
  - Limit state involvement: Reliance -`school_limit_loss` (8); while Evolution II lasts the political-attention cost is cut by `school_limit_attention_cut` (25%, applied in `video_game_in_sweden_add_public_costs`, so the category header shows it), and the lost public reach costs `school_limit_war_support` (1%) war support and `school_limit_recruitable` (1%) recruitable population through the package.
- The 180-day timer `video_game_in_sweden_school_days` counts down in the daily package tick like the other action timers and is reset with the package.
- AI: education base 2 (democratic 1.5, at war 0.6); recruitment base 1 (at war 2, world tension above 0.5 1.5, fascist or communist 1.8, democratic 0.6, and the shared 0.1 threshold caution of `video_game_in_sweden_ai_avoids_reliance_gain`); limitation base 1 (democratic 1.3, stability below 35% 1.5). All factors are in `video_game_in_sweden_ai` and `video_game_in_sweden_ai_factor`. This is a new weighted surface for the blocked R2-8 audit.
- The text uses the existing report picture and period wording (elementary teachers, popular-movement study circles, chalk and printed counters).
The Event Details and evolution texts are unchanged, so no catalog change is pending.
Basis: spec part 2 Public event families, research notes on Swedish study circles, round 3 lead item.
Disposition: `implemented`; the popup timing in a live campaign is needs_live_game.

### R3-7. The counterplan, bootleg and political-appropriation incidents have their third answer

Finding: spec part 1 gives the unexpected counterplan three answers (reward the insight, dismiss it as gamesmanship, revise the rules) and the foreign bootleg three (tolerate, protest, observe foreign play), and spec part 2 gives political appropriation three (ignore, sponsor one narrative, require official neutrality), but `chaosx.nr24.30` offered each only an admit and a dismiss option.
Decision: one new option per family, each using a price already set when the incident was drawn, its own `ai_chance` from `video_game_in_sweden_ai_factor`, and a `custom_effect_tooltip` with exact values; the existing admit and dismiss options are unchanged.
- `counterplan_c` "Write the counterplan into the referee's book" counts as a rules revision through the new shared `video_game_in_sweden_record_rules_revision` (flag, one more package planning entry, next levy +2 army experience and +3 command power), which the decision now also uses, together with `video_game_in_sweden_compute_rules_revision_gain`. Its Reliance gain is computed when the incident is drawn and stored in `video_game_in_sweden_mm_revise_gain`, so the tooltip and the effect agree. The new response value `incident_revise` pays the admission price in `video_game_in_sweden_apply_incident_penalty` but is not remembered as an accepted mismatch, because the cabinet absorbs the insight instead of conceding the error. AI: officer competition 1.5, field evidence 0.6, the shared 0.1 threshold caution.
- `bootleg_c` "Let the copies circulate abroad" raises Reliance by `incident_bootleg_tolerate_gain` (3), extends the licence trade goodwill to at least `bootleg_interest_days` (60) through the existing package timer, and opens `video_game_in_sweden_diplomacy_active` for `foreign_diplomacy_incident_days` (90) when it is not already open, so diplomatic mismatch reports become possible; it pays the dismissal price. AI: commercial route 1.5, at war 0.4. The existing "Observe how the foreigners play it" remains the observation answer.
- `party_c` "Endorse one committee's reading of the board" grants `incident_party_sponsor_political_power` (30) as a native line, raises Reliance by `incident_party_sponsor_gain` (8), sets `video_game_in_sweden_party_appropriation` (party reports grow more common) and pays the dismissal price, whose lines are stability and political power gain. AI: fascist or communist 2, democratic 0.4, supply crisis 0.2 like the dismiss answer.
These are new entries on the incident `ai_chance` surface for the blocked R2-8 audit.
Basis: spec parts 1 and 2 incident answers, round 3 lead decision that third answers reuse the price drawn with the incident.
Disposition: `implemented`; option display in a live report is needs_live_game.

### R3-8. AI route matrix probability pass remains blocked

Evidence this round: one narrow `hoi4.probability_inspect` call after the round 3 changes (adapter `event_option_ai_chance`, source `{path: events/024_hearts_of_iron.txt}`, `candidatePool` `[chaosx.nr24.38]`, no `refresh`) returned `{"artifactCount":0,"code":"INTERNAL_ERROR","status":"error","workspaceId":"current"}`, matching the lead's probe on 2026-10-05. Per the task rule it was not retried.
Weighted surfaces added or changed in round 3, to add to the R2-8 list for the auditor:
- `video_game_in_sweden_ai_avoids_reliance_gain` holds while the next stage is switched off and Reliance is at Doctrine or above (R3-1), which lowers the widening, rules revision, officer league, national league, preparedness and licence decision weights and the new recruitment and rules-revision answers to 0.1 in that state.
- `chaosx.nr24.38` option `ai_chance` (R3-6): civic education, recruitment and limitation, scenarios to cover democratic peace, fascist war, high tension and low stability.
- `chaosx.nr24.30` third answers (R3-7): `counterplan_c`, `bootleg_c` and `party_c`, scenarios to cover officer competition with and without field evidence, commercial route at peace and at war, and democratic, fascist and communist governments.
Decision: no numeric probability acceptance is claimed. Once an inline test no longer returns INTERNAL_ERROR, the auditor runs the baseline and comparison for the D23 scenario ids, the R2-8 list and this list with the documented scenario schema, and owner patches follow only for orderings that contradict spec part 3.
Disposition: `blocked` (missing input: a working `hoi4.probability_*` route).
