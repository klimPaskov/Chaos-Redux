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

## D10. Evolution V after the race: holder watch, accidents, incidents and outcomes

Disposition: `implemented`.

Basis: spec 004 says Evolution V affects every country that holds recovered Event 025 material or a compatible Event 036 recovery, uses the affected country as the log actor, and ends in one of five persistent institutional states held through one staged idea lifecycle; the lead found that Evolution V could not begin after the recovery.

Decision:

- Material holders join a bounded registry, `global.chaosx_nr25_holders`, and run their own monthly watch pulse `chaosx.nr25.281`. The race pulse stops when the race ends, so only one pulse ever processes a country's aftermath.
- After the race the watch arms Evolution V through its own setting, Chaos gate and MTTH, stores a due date, and re-arms the opening if it could not be delivered. The opening's delivering holder is the log actor; other holders get a notice event.
- Dependence pressure follows physical custody: 2 per month while material is held, 2 more under integration, 1 more under concealment, 1 less under containment, and 3 relief per month once the material has gone.
- Concealment no longer marks the programme as contained, so it cannot count towards Human Factors.
- The five states are Contained Exotic Technology, Independent Human Adaptation, Integrated Alien Systems, Alien Systems Reliance and Autonomous Research Network. The integrated state is displayed as "Integrated Alien Systems" so it is never confused with the Event 016 capstone idea, Alien Systems Integration.
- A state settles only after 180 days in its band and replaces Alien Dependence; a later policy or Dependence change can move the country to another state, so every outcome is recoverable.
- The outcome ideas reuse the existing Event 025 idea art (analysis, survey, fragment and dependence pictures); dedicated outcome art is not produced in this tranche.
- The six strange-behaviour incidents follow the spec list. Each offers a costly correction or a useful concession that deepens Dependence; their AI chances lean to correction under containment and to concession under integration.
- Event 036 holders join the watch when their recovery resolves after Event 025 has fired. A country that recovered Event 036 material before Event 025 fired is not enrolled; this edge stays open.

## D11. Consent-based custody transfer

Disposition: `implemented`.

Basis: specs 004 and 006 and the arbitration matrix require that physical custody moves to a willing valid recipient, that future artifact actions and Dependence pressure follow custody, and that learned technology stays with the original owner.

Decision:

- The transfer decision is targeted. Candidates are registered expeditions, other holders, and the holder's allies, rebuilt monthly by the holder watch, excluding countries at war with the holder; a recipient may be outside the race registry.
- The offer event is the only consent the ledger accepts. On acceptance the ledger moves the core and fragments exclusively; the holder then pays the shipping (convoys, or political power on chartered passage), loses 15 Dependence, and gets a 180-day transfer cooldown; a concealed programme is exposed and costs stability.
- The recipient starts with at least 10 Dependence, gains intelligence, joins the holder watch, gains the artifact decisions, trusts the giver, and is distrusted by the other expeditions and holders.
- Offers lapse after 30 days. A refused, lapsed or invalid handover changes nothing, charges nothing, clears the stale consent, and reports the failure.
- AI offers custody only to AI countries, mostly when its Dependence is high, the recipient shares a faction, or the recipient is industrially stronger, and never while it pursues integration. AI recipients accept more readily inside the same faction or with good relations and refuse when hostile.

## D12. Participant reports, sabotage attribution and global news

Disposition: `implemented`.

Basis: the chain map's participant-report and global-report tables, and the multiplayer privacy rule that hidden coordinates and the author of hidden sabotage are never revealed.

Decision:

- One-shot reports (departure, first camp, probable site, confirmed site) keep their own guard flags; repeatable state changes (camp lost or restored, false lead, fragment recovered or lost, rescue, sabotage, armed clash) report at each change, which the action cooldowns already bound.
- A sabotage victim identifies the acting country only through a caught operation or intelligence of at least 20. The suspicion opinion is applied only then, so the diplomacy screen no longer reveals an unidentified saboteur. An identified false-coordinate operation stops misleading the victim's surveys; an undetected one stays silent until the expedition discovers it.
- Armed clashes are public by nature: the target is told who acted, and the first clash makes the news.
- The public Evolution V crisis is the first accident of a programme that is not concealed, plus each concealed programme exposed by a custody handover.
- The four news items reuse the delivered Event 025 news image (`news_event_025_winner.dds`, also aliased as the discovery picture); no separate news art exists for the milestone, clash, accident and exposure items.
- The crossing report card now illustrates the departure and route-setback reports, and the rescue card both rescue reports.

## D13. Event Details and Evolutions log

Disposition: `implemented`.

Basis: the lead's events-log item and the Event 028 wiring precedent in the shared Events Log files.

Decision:

- Event Details shows the premise plus one resolution line: not yet begun, under way, decided with the historical winner's name, or closed without a winner.
- The five evolutions appear as Event Details preview rows of evolution type 25 with stages one to five, so their toggles set the `events_log_disabled_evolution_25_25_<stage>` flags the gates already read.
- Each evolution's tier is the Chaos tier of its gate (Evolutions I to V on tiers one to five), both in the gate check and in the log milestone.
- Type, name, title, body and summary text use the existing Event 025 evolution localisation on every evolution surface; only the Evolution V holder that delivers the opening is recorded as an actor.

## D14. Event 016 Antarctic hooks and the legacy UFO race

Disposition: `implemented`.

Basis: spec 004's Event 016 relationship section and rule that Event 025 creates no Event 016 project history; the reworked race never granted the legacy `antarctica_success` idea, so every Event 016 Antarctic route was dead.

Decision:

- Event 025 publishes two read-only triggers in its custody-policy trigger file. `chaosx_nr25_has_antarctic_alien_evidence` is true while a country holds the recovered core or a fragment, or after it won the recovery, because the winner's scientists keep what they learned. `chaosx_nr25_holds_antarctic_core` is true only for the core's physical custodian.
- Event 016's alien-artifact contact, its alien-arms theory prerequisite and the `chaosx.nr16.17` description read the evidence trigger; the Dhrondan craft bypass reads the core trigger, because it studies the craft itself.
- Event 025 calls Event 016's existing contact helper when material reaches a country: at winner settlement, at a loser settlement with fragments, and for a custody recipient. The helper's own host check keeps it a no-op without an active Kruger host, and no Event 016 history is created.
- The legacy Antarctica Race decisions, category, `antarctica_success` idea and their localisation are removed. Their legacy art registrations stay unused in the shared picture files; `GFX_report_event_antarctica_secured` is still Event 016's report picture.

## D15. Evolved openings

Disposition: `implemented`.

Basis: spec 004's evolved-opening section for each evolution and the chain map, which says Evolution V can alter the first opening only as a latent property.

Decision:

- An evolution shapes the opening when its own setting is enabled and its Chaos gate is already met as Event 25 fires. Evolutions I to IV then begin at once through their normal activation, so each still logs once and the race-time gate never re-arms it.
- Each registered expedition receives the opening state: the signal answers from the first day (Evolution I), tracks and a missing party are already reported (II), AI expeditions sail escorted with more Logistics Readiness and fortify their first camp as a security zone (III), and the hull starts at 60 integrity with fragment fields open (IV).
- Evolution V stays latent: every crew starts with 10 more Exposure Risk, and when Evolution V later activates during the race those crews start their Dependence at once instead of at settlement.
- The entry and mobilisation reports append one sentence per evolved opening; disabled evolutions add nothing.
- The entry option key collision (`chaosx.nr25.2.d` named both the entry description and the chartered option) is fixed by renaming the option to `chaosx.nr25.2.e`.

## D16. Entry-window closure and stalled expeditions

Disposition: `implemented`.

Basis: the lead found that the entry controller ran only on the opening country and that no rule closed a race whose expeditions stopped progressing.

Decision:

- The controller body is one effect, `chaosx_nr25_close_entry_window`, that runs once. The delayed controller event goes to the opening country and to every human, and any expedition pulse closes the window once the stored close date has passed. None of these scans the world.
- An expedition that stays in one phase for 720 days with no objective, final mission or evacuation running is recalled: it withdraws with its verified evidence through the normal withdrawal path and receives a report. When no expedition remains, the race closes through the existing closure path.

## D17. Expedition Board layout, sector art and card text

Disposition: `implemented`.

Basis: spec 008 (six selectable sectors, three main values, rival cards with public identity, five action cards) and the lead's GUI item; the stopped thread's uncommitted geometry patch was reviewed against MCP inspect and render passes before adoption.

Decision:

- The stopped thread's geometry patch is adopted with corrections: the board root sits at a fixed offset from the screen centre instead of `origo = center` with clipping, so it fits whole at 1920x1080, 1600x900 and 1366x768, and the undefined `hoi_12mbs` and `hoi_14mbs` fonts are replaced by vanilla fonts.
- The status column draws the one status-panel texture as two compact cornered tiles and one tall tile, so the three value cards no longer overlap; the tall card also carries the route, outpost and target rows, and the separate support heading and race-state line are dropped because the header already shows the race state.
- The single fixed selection wedge is replaced by six per-sector highlights derived from the sector map itself, so the highlight always matches the selected sector's outline.
- Sector emblems read a per-sector frame variable mapped from the private survey state, and a sector whose fragment the viewer holds shows as recovered. The eight standalone sector-state DDS copies had no consumer and were removed; the eight-frame strip is the only state art.
- Rival cards show the rival's flag and name, both read from the stored rival tag, beside the public card text.
- Each action card shows a short board label and either the cost (whole icon-and-number groups per line) or the blocking status; the tooltip repeats the full name, effect, cost and status, and the confirmation window keeps the full name and one-line cost.
- Dead visibility triggers for elements that no longer exist were removed, and the confirmation window and empty-rivals note now use triggers whose names match their elements, so neither is drawn when it should be hidden.
- Hover, pressed and disabled card states were not rendered; the disabled action-card frame was re-fitted so all four frames share one footprint.

## D18. Actor-appropriate wording, casualty bands and the Antarctic deaths reason

Disposition: `implemented`.

Basis: the participant and route matrix row for human-controlled special chaos and actual nonhuman countries, spec 014's actor-text criterion, spec 004's personnel-loss rule (a dedicated Event 025 reason, losses proportional to scale and severity), spec 006's military-side rule and spec 013's casualty bands.

Decision:

- Wording follows the shared classifiers `is_actual_nonhuman_country` and `is_special_chaos_country`, with nonhuman wording first. The entry offer, the route estimate and the mobilisation order append one paragraph for such an actor; the field and programme casualty lines, the armed-seizure line and the incident tooltip have their own variants. Ordinary countries keep the existing text.
- The shared Deaths ledger gains the `antarctic_expedition` reason (39), shown as "Antarctic expedition losses" in both deaths-cause views and counted in the military country bucket, so expedition deaths stay on the military side without a new Chaos Meter column.
- Deaths per incident come from the `chaosx_nr25_casualty` bands instead of one death per incident: 12 for a field accident (the default), 6 for staff cut off in a forced shutdown, 30 for a camp seized by troops and 45 for a collapsed evacuation. The two unused or replaced constants (`dependence_accident_casualties`, `mission_evacuate_failure_casualties`) are removed.
- The evacuation objective, which ended the expedition silently, now reports its end (`chaosx.nr25.14`), including the dead when the evacuation collapses.

## D19. AI weights, reserve floors and the hostile-operation gates

Disposition: `implemented` for the source patch; `blocked` for the MCP probability baseline and compare.

Basis: the AI probability scenario contract (`matrices/025_ai_probability_scenarios.md`), its hard-failure list, spec 009, and the lead's acceptance that the AI keeps its reserve floors, cannot launch an invalid final recovery and cannot repeat one hostile action every cooldown.

Defects found and fixed:

- The five targeted hostile operations and the pre-winner data exchange required a chain-local event target inside `available`, which never exists while a decision is evaluated, so none of them could ever be taken by a player or the AI. Their actor gates now check only the actor's own readiness and cooldown; the target is checked in `target_trigger` through FROM (a live participant whose received-operation cooldown is clear, and for the exchange one not already exchanged with). Plain sabotage now also respects the target's received cooldown.
- Four AI modifiers read flags that nothing sets (`chaosx_nr25_survey_evidence_ready`, `chaosx_nr25_action_recon_used`, `chaosx_nr25_action_signal_triangulation_used`, `chaosx_nr25_first_among_equals_candidate`); they now read the survey-evidence gate, intelligence, an active fragmenting wreck and the recovery winner.

Decision:

- Every optional spending decision carries a zero factor while the AI is below its roster reserve floors (political power, fuel, support equipment and, on its own shipping, convoys). Reinforcing or restoring the outpost, rotating crews, emergency shelter and withdrawal stay exempt so an AI can always recover or leave.
- Hostile operations and the armed Evolution III actions prefer a rival ahead of the actor (x1.5), avoid a rival with a countermeasure ready (x0.5), lean towards a rival caught operating against the actor (x1.3), and never repeat the actor's last operation or armed action back to back. No factor reads whether the target is a player.
- Outpost reconfiguration has no base weight; the AI reconfigures only when its situation calls for that emphasis, so it no longer cycles paid reconfigurations. The opening emphasis choice (`chaosx.nr25.70`) shows each emphasis's effect and weights the depot for low readiness, the fortified camp for militarisation or war, the signals station for an active signal and the traverse camp for an improvised route.
- Evolution V: containment rises with reliance, a recorded accident and stability; controlled integration suits a stable country with low Dependence, risky integration a country losing a war or collapsing, and integration is cut once an accident is on record or reliance has set in; destruction is a last resort after an accident at the accident threshold, never during integration; a democracy is half as willing to conceal.
- Tuning lives in the `chaosx_nr25_ai` constants.

Source-level scenario reads (deterministic, not probability results): P03 human entry is an event offer with no roll; P04 an AI minor fails the roster gate; A04 critical readiness fails the final-recovery gate (Logistics Readiness 40) and the reserve floor; R01 the leader carries x1.5; R02 a defended leader (x0.75) falls below an exposed rival that is also ahead (x1.5); R03 retaliation (x1.3) does not override race relevance; R04 no player-status factor; R05 a withdrawn rival fails `chaosx_nr25_target_participant_valid`; R06 the actor's rival cooldown, the target's received cooldown and the last-operation guard each zero a repeat.

MCP route record: `hoi4_probability_inspect` with `adapter = decision_ai_will_do`, `source = { path = common/decisions/025_alien_technology_in_antarctica_decisions.txt }` and a five-decision pool returned `INTERNAL_ERROR` twice (once with a mistyped pool, once with the exact pool), and `mission_ai_will_do` on the missions file returned `INTERNAL_ERROR`. `hoi4_probability_compare` with the frozen before snapshot under `evidence/probability_before_20261004/` returned `PROBABILITY_SURFACE_EMPTY`, as the Event 031 record also found for snapshots outside `common/`. No refresh, helper expansion or repository-wide query was used and no route was retried in a loop. The before snapshots (HEAD `5b46c56be` blobs, SHA-256 in the folder listing below) are kept for a later compare.

| Before snapshot | SHA-256 |
| --- | --- |
| `common/decisions/025_alien_technology_in_antarctica_decisions.txt` | `ac63ccd891dadd0201af5598296ae1e9127f836fe4c3505db1e9805f120ae082` |
| `common/decisions/025_alien_technology_in_antarctica_evolution_decisions.txt` | `e43030c5185ecefd131761f0627153257636a2a9fe56967be5a0976024bf7b7e` |
| `common/decisions/025_alien_technology_in_antarctica_aftermath_decisions.txt` | `1e7cdf6d0651972529df327b36c6459721a0dc85070efd3e9bc7e0b162232c3b` |
| `common/decisions/025_alien_technology_in_antarctica_missions.txt` | `58d0bf81b779d30d399acb3bb40e563f92a2a19fb27dbb0b9c5127c32921a821` |
| `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt` | `975d71468d6978572c2874fd7dfef6944e2db64eb230959612be90a82fe9d05a` |
| `events/025_alien_technology_in_antarctica.txt` | `9d968ac7bad33b48bc490f9190e1590317b84d76719b71b3a218a4b7ecdf8c5c` |

## D20. Evolution overlay animations and the board animation control

Disposition: `implemented`.

Basis: spec 008's evolution overlays (including the militarised-zone overlay), spec 010's recommended loops, the frame-animation skill, and the lead's direction that the four loops and the missing militarised overlay are owed work.

Decision:

- Every evolution has an eight-frame overlay over the sector map: a signal pulse at the hub (I), a footprint trail with a mist figure that gathers and dissolves at its end (II), warships sweeping searchlights over red security zones with blinking beacons and radar pings (III), a field of alien shards whose cracks flicker and discharge (IV), and border circuit tendrils that carry a light pulse to the coast (V).
- Frames are drawn at the map's displayed size (441x271, scale 1) instead of the old 700x430 canvases at scale 0.63, which keeps each sheet at 3528x271.
- The overlays avoid marking any single sector: the signal sits on the hub, shards are spread through all six wedges, and the trail, tendrils and ships follow coasts and borders, so no overlay reveals the hidden core sector.
- Four overlays use one generated base layer plus eight generated motion layers, because the image tool cannot hold fixed elements (footprints, shards, tendrils, ships) still across separate generations; the signal uses eight full frames aligned on the hub. Each frame still has its own generated visual state.
- Frame 000 of each loop replaces the old static overlays, two of which had painted checkerboard pixels.
- A fifth header control toggles `chaosx_nr25_animations_disabled`, which nothing could set before, so the phase banner and overlay statics are reachable. The deadline text box narrows from 160 to 128 pixels to make room; its longest text, "Recovery resolved", still fits.
- Static fallbacks take the animated sprites' base names, and the unused eight-frame banner registration under the base name is replaced by the banner's static frame.

## D21. Default enabling and the catalog handoff

Disposition: `implemented` for default enabling; `accepted and queued` for the catalog row.

Basis: the lead's acceptance that Event 25 joins the reworked default-enabled list once items 1-17 are committed, and the rule that this workstream does not edit the workbook.

Decision:

- Event 25 is added to `event_log_event_is_reworked_default_enabled` through its identity constant, so new campaigns no longer start with it disabled.
- The catalog row update (Details, the five evolution texts and the status `Needs Testing`) is staged in `catalog_changes_pending.md` with the exact in-game wording.
