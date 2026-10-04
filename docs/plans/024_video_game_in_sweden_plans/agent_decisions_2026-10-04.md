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
