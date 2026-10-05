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

## D22. Review round 1 corrections

Disposition: `implemented`.

Basis: the skeptical review of the round 1 commits (695bce4c8 to a1c2324b7) against the installed engine rules, the accepted design above and the player-facing writing rules.

Findings and decisions:

- The four actor-wording keys added in 5b46c56be were written as raw multi-line YAML strings, which the line-based localisation parser does not accept, so the entry, route-estimate and mobilisation paragraphs for nonhuman and special chaos actors would not load. They now use `\n` escapes. The uncommitted working-tree hunk that already made this fix, together with a constant-driven final-recovery tooltip and plainer recover-fragment wording, was finished and coherent and is adopted here.
- Mission descriptions and the organise-objective tooltip printed the readiness thresholds as literal numbers. They now read `chaosx_nr25_mission_timing.failure_readiness_floor` and `chaosx_nr25_phase_gate.crossing_readiness`.
- The stall recall (D16) counted only phase entries, so an expedition that kept attempting the final recovery for 720 days could be recalled during a cooldown between attempts without warning. Opening any objective or final recovery attempt now restarts the stall clock; an expedition is recalled only after 720 days without a new phase, objective or attempt. The recall report states the limit from `chaosx_nr25_stall.phase_stall_days`.
- The armed-seizure decision tooltip and the evacuation objective outcomes now state the real casualty bands of D18 and that an evacuation ends the expedition's part in the race.
- Several player-facing strings that used implementation wording ("participant", "persistent", "action tray and supporting board state") were rewritten in plain terms.
- Evolution I to IV responses were visible only while their evolution was the highest one active, although each hazard keeps running in the pulse after a later evolution begins. With an evolved opening (D15) that starts Evolutions I to IV together, the signal, survivor and militarisation responses (including the rescue that the Nobody Gets Left on the Ice achievement needs) were never offered during the race. Each response now stays available while its own evolution is in force (`chaosx_nr25_<evolution>_evolution_in_force`, which also honours the Event Details toggle); the shared action cooldown still limits an expedition to one action per cooldown.

Review evidence limits: `hoi4_probability_inspect` (`decision_ai_will_do`, aftermath decisions file) still returns `INTERNAL_ERROR`, so D19's MCP baseline stays `blocked`; one attempt was made and not retried. `hoi4_event_inspect` in `lint` mode rejected both selector forms tried, so event review was source-only.

## D23. Progress reserve, readiness repair and conditional withdrawal

Disposition: `implemented` for the source patch; `blocked` for the MCP probability inspect and compare.

Basis: spec 009 (Phase behavior, Spending floors, Progress strategy, Withdrawal logic), the D19 reserve floors, and the lead's round 2 finding that every phase-gate action carried the full roster-entry floor with a zero factor, so an AI stalled after its first spends and then withdrew at random through a flat `base = 1`.

Decision:

- Two reserve levels. Optional spending keeps the roster-entry reserves (`chaosx_nr25_ai_keeps_reserve`, unchanged). Phase-gate actions use the new `chaosx_nr25_ai_keeps_progress_reserve`: political power, fuel (through `fuel_k`), support equipment and, on owned shipping, convoys must cover the core floor plus the cost of the current phase's gate, so the core floor is what remains after paying.
- Core floors live in the new `chaosx_nr25_ai_floor` constants: peace 10 political power, 100 fuel, 25 support equipment, 5 convoys; war 25, 400, 100 and 15. The gate costs are read from the existing `chaosx_nr25_cost` requirement mirrors (authorisation or chartered entry, gateway, outpost, survey, final, with the chartered political-power variants). Mobilisation has no paid gate, so it saves for the coming gateway. `chaosx_nr25_refresh_ai_progress_floor` stores the floor at registration, on every phase change and on each pulse, so a change of war state is picked up within one pulse.
- Progress-reserve actions: authorisation, the three gateways, establishing the outpost, the five final approaches, the three survey actions while the survey gate is open (`chaosx_nr25_survey_gate_open`), and rival reconnaissance, fragment recovery and fragment analysis while they would reopen the site-confirmation objective (`chaosx_nr25_action_reopens_site_objective`). Outside those states the survey trio keeps the full floor. The earlier phases have no objective-starting optional action for an AI, because the organising objective opens with the roster authorisation.
- Spec 009 priority one: the depot and polar-crew actions draw on the progress reserve and gain weight (+12 and +6) while Logistics Readiness is below the organising threshold (`chaosx_nr25_phase_gate.crossing_readiness`), because the pulse drains readiness and nothing else repairs it before the outpost exists.
- Withdrawal has no weight unless `chaosx_nr25_ai_should_withdraw` holds, and then weighs `chaosx_nr25_ai.withdraw_weight` (25). Conditions: two route collapses (`chaosx_nr25_route_collapses`, counted when a gateway or supply-route objective fails); five consecutive pulses below the objective failure floor (`chaosx_nr25_critical_readiness_pulses`); no new phase or objective for 360 days (`chaosx_nr25_withdraw_review_date`, set with the stall clock) while unable to pay for the current gate (`chaosx_nr25_phase_gate_cost_available`); surrender progress above 0.5; or a rival in final recovery while this expedition is not yet surveying and holds no fragment or survey evidence, with Evolution IV not in force. It is suppressed while the AI holds major fragments, is in final recovery or has a confirmed site, after the race resolves, and while it is at war with surrender progress between the desperate threshold (0.1) and 0.5.
- The fragment-recovery weight read a country flag (`chaosx_nr25_evolution_wreck_breaking_apart`) that nothing sets; it now reads `chaosx_nr25_wreck_breaking_apart_evolution_in_force`.

Source walk (deterministic reads, not probability results). Assumptions: owned shipping, peace floors, support equipment entering the stockpile at 0.75 a day, objective lengths from `chaosx_nr25_cost`.

P01 peaceful maritime major, roster-entry stock 60 political power, 6,000 fuel, 120 convoys, 450 support equipment:

| Phase | Stock before the action | Next phase-gate action | Cost gate | Progress floor | Weight |
| --- | --- | --- | --- | --- | --- |
| Entry | as above | Authorisation at roster selection | met | not used (event effect) | taken |
| Mobilisation | 60 PP, 5,900 fuel, 110 convoys, 350 support | Organising objective runs; depot (optional, full floor met) | met | n/a | depot 10 |
| Crossing | 60 PP, 5,800 fuel, 110 convoys, 290 support | Gateway | convoys > 12, fuel > 150, support > 100 | 10 PP, 0.25k fuel, 125 support, 17 convoys | 10, 18, 8 |
| Outpost | 280 support, 98 convoys | Establish outpost | support > 150, fuel > 100 | 175 support, 0.2k fuel | 20 |
| Survey | 242, then 176, then 110 support | Three surveys 12 days apart | support > 75, fuel > 75 | 100 support, 0.175k fuel | 12 to 21 each time |
| Final | 125 support, rising | Controlled recovery | support > 125 | 150 support, 15 convoys | 20 to 40 once support passes 150 (about 35 days of production) |

Under the old full floor the same country could not run a gateway, the outpost or any survey once its political power fell to 50 or below, although none of these owned-shipping actions costs political power, and in the survey phase it waited about 130 days for support equipment to climb back above 200 between surveys.

P10 critical logistics, same stock with Logistics Readiness below 10:

| Phase | Next useful action | Weight |
| --- | --- | --- |
| Mobilisation | Depot (progress reserve, readiness repair) | 22; polar crew 14 to 24 |
| Crossing | Gateway (no readiness gate) | 8 to 18 |
| Outpost | Establish outpost; reinforce and rotate have no reserve check | 20; reinforce 22, rotate 17 |
| Survey | Surveys alongside reinforce and rotate | 12 to 21; reinforce 22, rotate 17 |
| Final | Final approaches need readiness 40 and are unavailable; reinforce and rotate repair it | final 0 until repaired, then 20 to 40 |

Withdrawal stays at 0 in both walks until readiness has been critical for five pulses before the final phase; P01 never meets a withdrawal condition.

MCP route record: `hoi4_probability_inspect` (`decision_ai_will_do`, the patched decisions file, a three-decision pool) returned `INTERNAL_ERROR`. `hoi4_probability_compare` against the D19 before snapshot was rejected twice with `Invalid tool arguments` (the `scenarioSet` shape is not documented in the exposed schema); it was not retried further. No refresh, helper expansion or repository-wide query was used.

## D24. Plain requirement lines in decision and mission tooltips

Disposition: `implemented`.

Basis: CLAUDE.md section 2.7, the decisions skill (sections 6, 7 and 18) and the lead's scan showing raw `chaosx_nr25_` variables and two unlocalised flags in about 60 decision and all 16 mission requirement tooltips.

Decision:

- Checks that the decision's `visible` block already guarantees (the expedition's phase, a one-shot action already used, participation, an active race, the current outpost emphasis, the evidence-sharing limit) move into `hidden_trigger`, so the tooltip lists only what can actually block the order.
- Live requirements become plain `custom_trigger_tooltip` lines: the shared order cooldown (`chaosx_nr25_order_ready`, "The expedition is ready for a new order"), the rival-operation cooldown, the final-recovery cooldown, Expedition Progress and Logistics Readiness thresholds with the current value, the route, the outpost, a surveyed sector before fragment recovery, a held fragment before analysis, the outpost-or-survey phase for reconfiguration, and the remote rig's intelligence threshold (`chaosx_nr25_remote_intelligence_ready`, shared with the board dispatcher).
- Every mission's `available` block is one line: "The objective is due and the expedition can complete it" or "The recovery is due and the expedition can complete it".
- `chaosx_nr25_outpost_lost` gets a requirement-flag key.
- A rerun of the requirement scan (available and custom_cost_trigger blocks expanded through scripted triggers, skipping hidden_trigger and custom_trigger_tooltip) finds no raw `chaosx_nr25_` variable or unlocalised flag.

## D25. Decision list clutter: board tray, outpost upkeep, rival operations and evolution timing

Disposition: `implemented`.

Basis: the phase action matrix clutter rules (three to five actions per phase and six at most, one selected rival at a time for humans, hide invalid target actions, emergency actions only during the emergency, remove race actions after resolution), the decisions skill section 15.7 (a separate target-management category with a selected target, AI seeing every target) and the lead's round 2 count of about 14 survey-phase entries.

Decision:

- The Antarctic Expedition Board category mirrors the board's five-slot tray. The alternate landing and convoy escort are listed only while their situation holds, and fragment recovery gives way to fragment analysis once a fragment is held, as on the board.
- Outpost upkeep (reinforce, rotate crews, emergency shelter) moves to the existing outpost category, renamed Antarctic Outpost, because the camp is a long-lived context of its own. Its priority options hide the current priority and are listed only in the outpost and survey phases, when a change is possible.
- The five hostile operations join the countermeasure in the existing countermeasure category, renamed Rival Operations (`chaosx_nr25_rival_operations_category`, still on its dedicated icon). For a human, each hostile and armed Evolution III target_trigger accepts only the rival selected on the Expedition Board (`chaosx_nr25_rival_target_shown`); the AI keeps every valid target. The category is listed even when empty while rivals exist, and its description asks the player to select a rival card when none is selected. Executing an operation clears the selection, so a human chooses each target deliberately.
- Evolution I, II and IV responses are listed once the expedition has a camp on the ice (outpost phase or later), Evolution III responses once it sails (crossing or later), and none after the race resolves or the expedition leaves it (`chaosx_nr25_race_action_visible`). Evolution V policies are unchanged. Withdrawal and the safety category also close at resolution.

Source count of listed entries per phase (one rival selected, missions excluded, situational entries counted at their worst case):

| Phase | Expedition Board | Rival Operations | Antarctic Outpost |
| --- | --- | --- | --- |
| Entry | 3 (charter, science exchange, conceal departure; authorisation is spent at entry) | 0 (not listed) | 0 |
| Mobilisation | 4 (depot, aerial survey, radio net, polar crew) | 1 (compromise stores) | 0 |
| Crossing | 3 (three gateways) | 1 (intercept convoy) | 0 |
| Outpost | 3 (establish outpost, alternate landing, convoy escort) | 2 (+1 countermeasure after a sabotage) | 3 upkeep + 4 priorities |
| Survey | 5 (three surveys, rival reconnaissance, fragment recovery or analysis) | 5 (+1 countermeasure) | 3 upkeep + 4 priorities |
| Final recovery | 5 (five approaches) | 3 (+1 countermeasure) | 3 upkeep |

The Expedition Board category never exceeds five entries and Rival Operations never exceeds six. Before the change the survey phase listed up to 14 entries in one category for a single rival and five more for every further rival.

## D26. Gateway groups, route bands and route interruption

Disposition: `implemented`; actual map behaviour is `needs_live_game`.

Basis: spec 002 (Route burden, Gateway groups), spec 005 (Secure gateway access), the participant and route matrix (route families, cost factors, invalidation), spec 014 section 3, and the lead's finding that the three gateways differed only in a display variable.

Decision:

- Gateway groups follow the route matrix and spec 002, with New Zealand as its own fourth group: Cape Horn (Tierra del Fuego 953, Magallanes 507, the Falklands 299), Cape Town (the Cape 681, Natal 719), Tasman (Tasmania 518, Victoria 517) and Ross Sea (Canterbury 723, Otago 1081). The ids were taken from a narrow source lookup of the installed `history/states` files and `state_names_l_english.yml` (Chaos Redux ships no state or map overrides) and live in `chaosx_nr25_gateway_state`. A fourth gateway decision, Open the Ross Sea Gateway, takes the free fourth crossing slot on the board.
- Bands are rated per expedition from those nine states only (`chaosx_nr25_refresh_gateway_bands`): direct if the expedition controls a port; allied if the port holder is a faction partner, a subject, its overlord or has an opinion of the expedition above 50 (a file constant, because opinion comparisons in the existing precedents use `@` constants); long ocean otherwise; chartered for a chartered-passage expedition; closed when every port holder is at war with the expedition. Improvised is the route band after a failed gateway objective or an alternate landing from a cut route.
- The band sets the gateway cost (at most three resource types: the allied band trades support equipment for a political fee, since the port holder supplies the stores), the reach-the-gateway objective's length (90/120/150/150 days, with `add_days_mission_timeout` moving the native timer to match) and the route upkeep each pulse (1/2/3/3, 4 improvised or cut, 2 before sailing), all in `chaosx_nr25_gateway`. The flat crossing constants and the flat pulse drain are retired. Authorisation and the entry charter no longer pre-set a gateway route, so the board shows "Not selected" until a gateway is chosen.
- Cost rows, `_blocked` and `_tooltip` variants, board card costs and the board route row (route and band) read the band through scripted localisation. The AI progress floor (D23) saves for the best open band's cost.
- A gateway is unavailable while every port holder of its group is at war with the expedition (stored band) and while the holder of its best port is at war with it (live check). When the expedition's chosen group closes, the pulse cuts the route: report `chaosx.nr25.13` (reusing the crossing report card), readiness −8, one route collapse for AI withdrawal, and the crossing, outpost and supply-route objectives cannot complete. Recovery is the alternate landing (now offered while the route is cut, from crossing to final recovery, as an improvised route) or the new Charter Emergency Passage in Expedition Safety (40 political power, 100 fuel, a chartered route; also offered after an improvised landing). The AI weighs both (+24 and +20 while cut) on the progress reserve.
- The AI adds 30 to a direct-band gateway and 15 to an allied one, enough to outweigh the earlier mobilisation preferences (+10), so it takes the best open band.

Validation limits: the band rating, the `var:` state scope from a stored state id and the trigger-side temporary band variable follow the wiki's Data structures rules and vanilla trigger precedents but are `needs_live_game`; no map render was made because the change reads existing states without editing the map.

## D27. Baseline field hazards, rare incidents and the solo pace

Disposition: `implemented`; frequencies are `needs_live_game` for tuning.

Basis: spec 003 (Phase 2 Hazards, Baseline rare incidents, One-participant behavior), the chain map's weather route setbacks, and the lead's finding that the pulse had no random roll, so the preparation actions had nothing to mitigate.

Decision:

- The hazard roll lives in a new owned file pair (`025_alien_technology_in_antarctica_field_effects.txt` and `_field_triggers.txt`) called once from each expedition's own pulse. At most one hazard per pulse, only on the ice (outpost phase or later), only for the expedition itself; no world scan and no evolution dependency.
- The chance is an MTTH entry (`chaosx_nr25_hazard_chance`, chaos-redux-mtth) on constants in `025_alien_technology_in_antarctica_field_constants.txt`: Exposure Risk raises it; the forward depot, radio net, polar crew, a supplied camp and a protective outpost emphasis lower it; a strained camp and a solo expedition raise it; it is capped.
- Each of the seven spec hazards is paired with the preparation that softens it, so every mobilisation and outpost choice now has a field payoff: pack ice with escorted convoys or a direct route, whiteout with the polar crew, crevasse fields with the aerial route survey, radio loss with the radio net, engine failure with the forward depot, lost sledges and vehicles with a logistics depot or traverse camp emphasis, sickness with a crew rotation. A prepared hazard is drawn less often (weight 4 against 10), does half the damage and kills no one; an unprepared crevasse or sickness costs a crew and records four deaths in the Antarctic expedition deaths ledger.
- Each hazard has its own report with the applied losses and the preparation line. The draw uses a cumulative weight roll rather than `random_list` with variable weights, so the selection does not depend on an unverified weight form.
- The eight spec rare incidents are choice events reached at most once each, on a 5% roll in a pulse without a hazard, from the crossing phase on: abandoned camp, rival call for help, misidentified meteorite, clear weather window, neutral ship, wrecked survey aircraft, scientists' dispute, fragment reacting to current. Each has two or three options with a real trade-off and AI chances keyed to readiness, exposure, phase, faction and war. The rescue incident picks a random rival on the ice from the stored registry, may raise its readiness and gives it the existing rescue opinion; the neutral ship can turn a cut or improvised route into a chartered one (D26). Pictures reuse report cards that carry no evolution imagery.
- A solo expedition gains 1 Exposure Risk per pulse on the ice and loses 1 Expedition Progress per pulse in the survey and final phases, on top of the higher hazard chance; a prepared solo expedition still completes the baseline.

## D28. Evolution I, II and IV response tendencies

Disposition: `implemented` for the source patch; `blocked` for the MCP probability route.

Basis: spec 009 Evolution behavior and the lead's finding that the signal, survivor and wreck responses carried flat weights.

Decision:

- Eight posture triggers read only the expedition's own state and the race's leading phase: leading (no expedition in a later phase), scientific (Scientific Capacity at least 3, which the science exchange reaches), aggressive (at war or a fascist government), risk-averse (Exposure Risk at least 60), weak (Logistics Readiness below 30), desperate (at war above the existing desperate surrender threshold), militarised (at war or Evolution III in force) and a failing wreck (integrity below 50). None reads player status. Thresholds and tendency weights (+25, +20, +15, +10; ×0.5 against, ×0.3 strongly against) are `chaosx_nr25_ai` constants.
- Active Signal: remote listening +20 scientific, ×0.5 aggressive; following +20 aggressive, ×0.5 risk-averse; shielding +25 risk-averse, +10 weak; jamming +10 when trailing, ×0.5 risk-averse; a broadcast +10 scientific, ×0.3 risk-averse.
- Something Survived: avoiding contact +25 weak, +10 risk-averse; guarding +20 militarised; capture +25 desperate, +15 militarised, ×0.3 weak; mapping its path +20 scientific; turning it away +10 scientific and +10 risk-averse.
- The Wreck Is Breaking Apart: stabilising +20 when the wreck is failing and the expedition is scientific, +10 leading; cutting fragments +20 trailing, ×0.5 leading; mapping debris +15 trailing, +10 scientific; distributing custody +15 trailing; leaving the unstable core to press for it (the core rush) +25 leading, ×0.3 trailing. Fragment recovery in the survey tray gains +15 when trailing under Evolution IV. The free responses (mapping the debris, leaving the core) no longer carry a reserve check.

Source reads: P11 (Evolution IV, trailing in the survey phase, integrity 60, Scientific Capacity 1): fragment recovery 37, cutting 26, mapping 21, distributing 19, against the core rush 1.2. A leading expedition in final recovery: the core rush 29, stabilising 16 (36 on a failing wreck with scientific capacity), cutting 3, mapping 6, distributing 4.

MCP route record: `hoi4_probability_inspect` (`decision_ai_will_do`, the evolution decisions file, a three-decision pool) returned `INTERNAL_ERROR`; it was attempted once. The compare route was not reached because its scenario schema is not exposed (D23).

## D29. Earlier Event 036 recoveries join the Evolution V holder watch

Disposition: `implemented`; closes the open edge left by D10.

Basis: spec 004 (Evolution V reaches every country holding recovered Event 025 material or a compatible Event 036 recovery) and D10's recorded limit that an Event 036 recoverer from before the race opened was never enrolled.

Decision:

- `chaosx_alien_recovery_ledger_resolve_event036` adds each newly recorded recoverer once to the bounded global array `global.chaosx_alien_recovery_event036_recoverers` (an array rather than one event target, because each Event 036 firing records a separate random country).
- `chaosx_nr25_enroll_event036_recoverers` walks only that array and enrols each recoverer that still exists and still holds its recovery through `chaosx_nr25_enroll_holder`. It runs when Event 25 opens (before evolved openings, so an Evolution V opening already sees the holder) and again when Evolution V activates. If Evolution V is already active, a recoverer outside a live race opens its aftermath and receives the holder notice `chaosx.nr25.221` at once; otherwise the notice arrives through the existing Evolution V activation loop. Enrolment and aftermath opening are idempotent, so the post-opening resolver path never doubles a holder.
- The ledger markdown documents the new array. Limit: a recovery recorded in a save from before the array existed is not enrolled retroactively, because finding it would need a world scan.

## D30. Decision cost text reads the constants it pays

Disposition: `implemented`.

Basis: CLAUDE.md's no-magic-numbers rule and the round 1 review note that 48 cost strings printed literal amounts.

Decision:

- All 48 Event 025 cost strings with literal amounts (expedition tray, outpost, rival operations, countermeasure, data exchange, Evolution I to V responses and the analysis decisions) now print `[?constant:chaosx_nr25_cost.*_required|0]` with the matching texticon. Every amount already had a positive requirement mirror, so no display constant was added. The gateway and emergency charter costs read `chaosx_nr25_gateway` (D26).
- Each string was checked against the executed effect and the decision's cost trigger. Three mismatches were fixed where the shown cost was right and the code was wrong: Recruit a Polar Crew required and showed fuel but never deducted it (it now pays `fuel_crew`); Integrate the Systems required and showed support equipment but never deducted it (it now pays `support_evolution`); Conceal the Program showed and paid 20 political power but only required 10 (its cost gate now reads `pp_conceal_required`).

## D31. Round 2 lead decisions adopted

Disposition: `accepted and queued` for the items still open at the end of this round; the implemented items are recorded in D32 onward.

Basis: the round 2 remaining-work list and the lead's decisions taken under the delegated design authority.

Decision:

- Signal Intensity and Wreck Integrity become single global values, following spec 004's global-state wording; per-expedition mitigation (shielding, remote listening, stabilisation flags) stays per country.
- A closed Expedition Board comes back through a free decision rather than by removing the Close button; the closed flag set when the country's analysis closes stays permanent.
- Rivals page through a per-viewer offset with one next-rivals control instead of more cards, keeping the accepted three-card layout (D17) and meeting spec 008's scrolling rule.
- D27's reuse of report cards for hazard and incident reports and D12's reuse of the news image stay accepted.
- The Event 044, 028, 052, 024, 027 and 011 hooks stay excluded, because spec 007 marks them as future or optional and those events are unreworked.
- The AI probability baseline and compare remain blocked by the `hoi4_probability_inspect` `INTERNAL_ERROR` recorded in D19, D23 and D28.
- The stopped thread's uncommitted handoff and matrix documents stay untouched and uncommitted as stale documentation.

## D32. Temporary outputs are set before the effects that write them

Disposition: `implemented`.

Basis: the wiki's Data structures section on temporary variables (a temporary variable first created inside a scripted effect may not survive its return, while one defined before the call is modified in place) and the shared date helper documentation, which requires callers to set `chaosx_date_offset` first.

Decision:

- Every Event 025 call of `chaosx_convert_days_to_date_offset` is preceded by `set_temp_variable = { chaosx_date_offset = constant:chaosx_date_units.zero }`: both stall-clock dates and the entry close date.
- `chaosx_nr25_gw_rating` and `chaosx_nr25_gw_best_controller` are set at the top of `chaosx_nr25_refresh_gateway_bands`; `chaosx_nr25_gw_best` before `chaosx_nr25_read_best_gateway_band` in the AI progress floor; `chaosx_nr25_gw_band` before `chaosx_nr25_read_action_gateway_band` when sailing; `chaosx_nr25_hazard_kind` before `chaosx_nr25_draw_field_hazard`.
- A dataflow scan of every Event 025 scripted effect, trigger, event, decision, scripted GUI and scripted localisation block (callee writes and reads followed transitively) finds no Event 025 temporary read after a scripted-effect call that created it.

## D33. Reopening the Expedition Board

Disposition: `implemented`.

Basis: D31 and the decisions skill's category pattern.

Decision:

- `chaosx_nr25_open_expedition_board` heads the Antarctic Expedition category for a human participant while `chaosx_nr25_board_closed` is set and `chaosx_nr25_aftermath_closed` is not, during the race or its analysis. It is free, has `ai_will_do` 0, clears the closed and confirmation state and rebuilds the slots.
- It uses the expedition category icon until the decision icon family is produced; the close tooltip names it.
- The tray therefore lists at most its five actions plus this control, and the control never appears while the board is open.

## D34. Rival paging

Disposition: `implemented`; paging behaviour is `needs_live_game`.

Basis: D31, spec 008's scrolling rule and D25's selected-rival targeting.

Decision:

- `chaosx_nr25_prepare_rival_cards` first counts the valid rivals into `chaosx_nr25_rival_candidate_count`, wraps a stale `chaosx_nr25_rival_page_offset` to 0, then skips that many valid rivals before filling the three cards (`chaosx_nr25_board.rival_cards`).
- The selected rival keeps `chaosx_nr25_rival_target_selected` whenever it is still a valid rival, whether or not its card is on the current page, so its Rival Operations stay listed; the selected-target row prints the rival's name.
- `nr25_rivals_next` sits at board position x 952, y 432, right of the cards' click regions, and is shown only while more than three valid rivals exist; `chaosx_nr25_next_rival_page` adds three to the offset and rebuilds the cards, wrapping after the last page.
- MCP evidence is recorded in the visual asset audit (Rival paging control, 2026-10-05).

## D35. Opening super-event quote

Disposition: `implemented`.

Basis: spec 014 section 14 and the super-event text research handoff.

Decision: `chaosx_super_event.109.q` prints the two verified lines in quotation marks, one per line, followed by `§Y-Alfred, Lord Tennyson, Ulysses§!`, the format of super-events 12 and 74.

## D36. Active Signal: global intensity, strong pulses and real responses

Disposition: `implemented`; frequencies and AI behaviour are `needs_live_game`; the MCP probability baseline and compare stay blocked as recorded in D31.

Basis: spec 004 Evolution I (global state, new actions, failure and counterplay, AI behaviour, evolved opening), spec 009 Active Signal and D31.

Decision:

- Signal Intensity is `global.chaosx_nr25_signal_intensity` (0 to 100), seeded at 10 when the evolution activates and at 20 when the race opens with it. The first expedition pulse of each pulse period raises it by 3, a strong pulse discharges 15, following the carrier wave adds 2, a broadcast adds 8 and jamming removes 6. The per-country variable, its registration and opening seeds, its clamp and the signals station's reversible intensity delta are retired.
- Strong pulses strike expeditions with a camp on the ice. The chance per pulse is the MTTH entry `chaosx_nr25_strong_pulse_chance` (10% at full intensity) scaled by intensity, with factors 0.5 for shielded instruments, 0.6 for remote listening, 0.75 for a working radio net and 1.25 for a signals station outpost, and zero while the evolution is not in force.
- The five spec consequences are drawn with equal weight (corrupted data only while the expedition holds survey evidence): damaged radios (the radio net stops covering radio failures for 60 days through `chaosx_nr25_radio_net_working`), lost readiness, injured crews (one crew and the hazard casualty band through the Antarctic expedition deaths reason), corrupted survey evidence, and a revealed position (exposure, intelligence for every other camp on the ice, the concealed departure lost, and a 45-day mark that AI rival operations favour). Shielding halves the damage, remote listening cuts it to three quarters, and either prevents casualties. Reports `chaosx.nr25.321` to `.325` reuse the signal report card.
- Following the wave adds survey evidence of 2 plus a tenth of the intensity. Jamming targets the board-selected rival for a human, otherwise the valid rival with the most progress, halves that rival's signal response gains for 60 days, costs the jammer 6 readiness and reports to the rival (`.326`), which identifies the jammer and gains the existing sabotage suspicion opinion when its intelligence reaches the sabotage attribution threshold. A broadcast is answered by a strong pulse with chance 25 plus half the intensity, otherwise it marks the first unresolved sector other than the hidden core surveyed for the broadcaster (`.327`).
- AI tendencies extend D28: scientific listening rises on a strong signal until the camp listens remotely; following gains weight on a strong signal unless logistics are weak and loses it while jammed; any unshielded camp shields on a strong signal; jamming rises when a rival is in final recovery, most for an aggressive expedition, and falls for a weak one; weak logistics avoid broadcasting into a strong signal and nobody broadcasts into a violent one.
- The band appears in the five response tooltips and in the board's Exposure Risk tooltip; whether a tooltip on a click-through board element shows in game is `needs_live_game`, so the decision tooltips carry the same line.
- The Evolution I body text and the pending catalog cell `D26` describe the pulses.
