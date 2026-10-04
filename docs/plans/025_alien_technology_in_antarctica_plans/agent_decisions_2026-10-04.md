# Event 025 agent decisions, 2026-10-04

The user granted the implementing agent full design authority for the Event 025 takeover.
Each entry below is an agent decision taken under that authority, with its basis and the implementation that carries it.
Disposition labels follow `CLAUDE.md` Specs and Plans.

## D1. Adopting the stopped thread's localisation, and deferring its board overlay hunk

Disposition: `implemented`.

Basis: HEAD referenced the five event ideas, the five opinion modifiers, six board header keys and two requirement flags without localisation, and the stopped thread's uncommitted localisation hunks supplied them in coherent player-facing text.

Decision:

- The localisation hunks and the two requirement-flag keys were reviewed and committed as they were.
- The scripted GUI hunk that replaces six per-sector selection triggers with one `nr25_sector_selected_overlay_visible` trigger was not committed with them.
  HEAD's `.gui` still draws six per-sector `nr25_sector_N_selected` icons, and the single overlay element exists only in the uncommitted `.gui` geometry patch.
  Committing the trigger change alone would leave the six committed icons without visibility triggers, so it travels with the GUI geometry review.

## D2. Per-participant expedition phase

Disposition: `implemented`.

Basis: specs 002 and 013 list a current phase in every participant row, spec 003 gives per-expedition phase durations, and the lead classified global phase gating as a defect because a leading expedition moved every rival and could strand laggards.

Decision:

- The country variable `chaosx_nr25_phase` is the only phase read by action gates, decisions, board slots, the board phase header, final readiness and final submission.
- `global.chaosx_nr25_phase` records race state only, through the new `chaosx_nr25_race_state` constants: entry, active, analysis and closed.
  The analysis and closed values equal the participant phase values, so the shared numbering stays readable.
- `global.chaosx_nr25_leading_phase` records the furthest phase any expedition has reached, for reports; nothing gates on it.
- Entry becomes mobilisation for every registered expedition when the entry window closes, through a loop over the stored participant registry instead of a world scan.
- Each later phase advances only the acting expedition, once that phase's objective has resolved:
  - mobilisation to crossing after the Organize the Southern Expedition mission resolves;
  - crossing to outpost after the Reach the Gateway mission resolves;
  - outpost to survey after the Establish the Antarctic Outpost mission resolves and the outpost stands;
  - survey to final recovery after the primary site is confirmed with at least the survey-evidence gate.
- Numeric progress and readiness gates were removed from the early phase advances because the crossing phase has no repeatable action to raise them, so a laggard could be stranded forever.
  Progress and readiness still gate final-recovery launch and final submission.
- A failed objective still resolves its phase with a penalty, so failure delays and weakens an expedition but never strands it.

## D3. Phase missions run in the background with real durations

Disposition: `implemented`.

Basis: every phase mission had `available` true at activation and therefore completed the day after it started.

Decision:

- Starting an objective stores its duration, schedules the hidden event `chaosx.nr25.87` for the day before timeout, and stores a guard date converted with `chaosx_convert_days_to_date_offset`.
  The guard keeps a callback from an older, cancelled objective from completing a newer one early.
- On its due date a baseline objective becomes completable only through `chaosx_nr25_phase_mission_can_complete`: no emergency weather, no exhausted crew, and Logistics Readiness at or above 10.
  Otherwise it times out as its failure result.
  Wreck and containment objectives always settle through their own success, partial and failure branches; an evacuation fails only in emergency weather.
- The participant pulse re-runs the same completion check if the due-date callback is missed.
- Objectives no longer block the expedition's other actions.
  The one-objective-at-a-time rule lives in the starter, so the player keeps acting while an objective runs and those actions decide its result.
- The protect-supply-route objective opens only in the outpost phase, so later upkeep actions never block the site confirmation.
- Triangulation was shortened from 180 to 120 days so a triangulation followed by a site confirmation stays inside spec 003's 120-240 day survey band.
- Final missions use the same rule: the completion window opens only while the receipt requirements hold, and a completed mission whose requirements lapsed settles as the existing partial failure instead of silently submitting nothing.
- AI and humans use the same missions and the same completion path.

## D4. Survey targeting and the primary-site soft-lock

Disposition: `implemented`.

Basis: spec 008 says clicking a sector selects it for survey or recovery, and the old rotating cursor plus a one-time confirmation could leave every expedition in final recovery without a confirmed site.

Decision:

- Survey actions and the Evolution IV cutting action target the board-selected sector, or the first unresolved or compromised sector when none is selected, and cycle through all six once every sector has a result.
  AI expeditions never select a sector, so they always take the next unresolved sector.
- Surveying the hidden core sector without false coordinates records it as a probable site for that expedition only; other surveys record surveyed.
  A probable or confirmed sector is never downgraded by a later survey.
- The site-confirmation objective can be reopened by every survey action until the expedition's own site is confirmed, and a successful confirmation marks the core sector confirmed on that expedition's board.
- Survey actions remain available to an expedition until it confirms its site, because the survey phase now ends only with that confirmation.

## D5. Recoverable hazards and sustained outposts

Disposition: `implemented`.

Basis: per-participant phases exposed three existing permanent locks: `chaosx_nr25_crew_exhausted` was never cleared, emergency weather returned at every pulse once the ambient +1 exposure reached the cap, and a lost outpost could not be restored because reinforcement required an established outpost.

Decision:

- The pulse clears crew exhaustion once the crew is above zero, and clears emergency weather once Exposure Risk falls below 90.
- Ambient exposure stops rising at 75; emergencies above that come from actions and evolutions.
- Reinforcing, rotating crews and emergency shelter stay available in the outpost, survey and final-recovery phases.
  Crew rotation and shelter use the base gate so an exhausted crew can recover.
- Reinforcing a lost outpost re-establishes and restores it, which also makes the Reclaim the Station route reachable.
- An evacuation cancels any running phase or final objective and blocks further actions until it resolves.

## D6. Rival cards and targets relative to the prepared participant

Disposition: `implemented`.

Basis: the rival-card and rival-target loops wrote through ROOT and compared against ROOT, so AI entrants registered from the controller event wrote the controller's cards and could list themselves.

Decision: inside the registry loops, the new trigger `chaosx_nr25_rival_card_candidate_valid` excludes `PREV`, and card counts, slot IDs and flags are written through `PREV`, the participant being prepared.

## D7. Chartered passage for countries without owned shipping

Disposition: `implemented`.

Basis: the participant and route matrix lists a chartered route for landlocked or small human entrants, and the accepted rules say every human may enter and that distance and access change only cost and timing.

Decision:

- Both human entry events offer a chartered passage beside the owned-shipping entry.
  It costs political power, fuel, support equipment and the civilian commitment, so it stays within four spendable types, and it needs no convoys.
- The chartered flag `chaosx_nr25_chartered_passage` makes every later shipping cost (gateway crossing, alternate landing, escort, final recovery, evacuation, the Evolution IV distribution and the Evolution V transfer) cost political power instead of convoys, through one shared trigger `chaosx_nr25_uses_chartered_passage` and matching cost selectors.
- The organising and gateway objectives run on their own chartered missions with longer constant-driven durations, so a chartered expedition pays more and arrives later but can finish every phase.
- Either entry warns when the civilian base or fuel reserve is below the ideal reserve, and such an entry starts with lower Logistics Readiness, judged on the reserves held when the choice is made.
- The optional entry-phase "Charter Neutral Shipping" action stays an owned-shipping supplement and is hidden from chartered expeditions.
- The hostile convoy interception still needs the attacker's own convoys, because it is optional and never gates progression.
- AI entry, AI reserve floors and AI weights are unchanged; the chartered options carry zero AI chance because AI entrants are chosen by the bounded roster.

## D8. Reward bridge, overlap exclusion and public field mapping

Disposition: `implemented`.

Basis: the reward arbitration matrix requires that an exact overlap excludes only the overlapping family while another base exists, and its broad field table names the public fields; the Event 016 API skipped the whole base pool on overlap and labelled Portal as aircraft and Temporal as propulsion.

Decision:

- The stopped thread's ledger rework is adopted: country variables keep the latest call's result, temporary copies carry an `_output` suffix so they never shadow those variables, the historical owner stays valid regardless of sovereignty, the loser resolver refreshes fragments and requires a participant, and Event 036 overlaps only with an applied Event 025 reward.
- Correction: the shared Event 036 legacy-reward flag is no longer cleared at the start of every ledger call, because Event 036's own option reads it after its resolver runs and a same-day Event 025 call would otherwise hide the jet reward.
- The alien arms family (`alien_infantry`) and its predictive-warfare upgrade belong to the flight, propulsion and weapons field and use the propulsion code; Event 036's jet reward keeps the aircraft code. Aircraft and propulsion are one overlap group, so either code on both sides is an exact overlap.
- Portal technology maps to spatial manipulation, robotics to computation and autonomous machinery, temporal technology to temporal instrumentation, clone, paleogenetic and xenobiological technology plus the four xenobiological controls to biological synthesis, and the capstone to integrated alien systems. No Event 016 family is exotic structural materials, so that field is not used.
- With an overlap, Event 025 still requests a base reward and the API excludes only the alien arms family; an empty remaining pool falls through to an upgrade and then the capstone. A later Event 036 conversion requests no base reward, so it receives an upgrade or the capstone.
- Achievement routes read the durable `chaosx_alien_recovery_event025_reward_applied` flag instead of the latest-call flag, and a later Event 036 resolution re-runs the Event 025 winner's achievement tracking, so Two Crashes, One Answer is set only after a real conversion.
- The architect's proposed new aviation family stays a proposal.

## D9. Achievement registration and eligibility

Disposition: `implemented`.

Basis: spec 011 requires full tracking, disqualifiers and save persistence, and says achievements must not unlock from a force-triggered test.

Decision:

- The fourteen achievements are registered in the shared achievement file with the pattern used by the Event 027 set: `possible` stays true once the route flag exists, and `happened` reads the eligibility trigger and the durable route flag.
- Eligibility lives in `chaosx_nr25_achievement_campaign_is_valid`: a human country, not in debug mode, not the test country, and without `chaosx_nr25_achievement_disqualified`.
  That flag is set once when an expedition registers in debug mode, from a force-trigger player or as the test country, and is never cleared.
- `game_rules_allow_achievements` is not used, matching most Chaos Redux achievement sets, because the mod's own rules would otherwise hide every achievement.
- Fragment roles are recorded as durable flags only when the ledger actually assigns the slot, so a failed cut or a taken slot can no longer mark a role.
  The Evolution IV cutting action is repeatable on its cooldown and targets the selected sector, so all six roles are reachable.
