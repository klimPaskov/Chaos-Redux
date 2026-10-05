# Event 033 agent decisions, 2026-10-04

Disposition: implemented; D1 to D20 are promoted into the accepted Event 033 specs (Parts 2, 4, 5, 6, 7, 8, 10 and 11, each in its "Accepted implementation decisions, 2026-10-04" section), D21 is accepted and queued for the catalog owner, and D22 to D24 are implemented review fixes.
Acceptance basis: the user granted the Event 033 lead full design authority on 2026-10-04 and directed it to take the recommended, spec-consistent option for every open choice and record it here.
Each decision below resolves an item that earlier handoffs left unresolved; implementation evidence is recorded separately when the work lands.

## D1. Adopt the stopped thread's uncommitted Event 033 work

Disposition: implemented (commits "Adopt the Event 033 Acid Rain consequence rework", "Record the Event 033 consequence repair specs, plans and evidence" and "Remove civilian population once and record the observed loss in Deaths").

The uncommitted Event 033 rewrite (consequence transaction, episode caps, damage receipts, quote/target bridge repairs, GUI wiring, achievements, aftermath file, delivered animation and veil DDS files) is adopted after a load-safety review and committed with the shared-tree workflow.
Basis: the accepted consequence repair spec is implemented in that work, `.tools/validation/validate_033_acid_rain.py` passes, the population-helper source replay passes all 40 cases, and the routed static-lint fixes 3, 4 and 13 plus the working-tree halves of 1 and 2 exist only there.
The shared population-first helper in `common/scripted_effects/chaosx_dynamic_effects.txt` and its twelve caller output declarations are committed as their own hunk-only commit so other owners' uncommitted hunks in those files stay untouched.

## D2. Severe and superstorm forecast lead becomes nine days

Disposition: implemented (commit "Give severe evacuations time to work"); promoted into Parts 5 and 7.

`acid_rain_evolution.severe_forecast_lead_days` and `acid_rain_evolution.superstorm_lead_days` change from 3 to 9.
The seven-day evacuation matrix, the 0.05 percent per-state ceiling, and the accepted Three Evacuations rule (completion strictly before the first severe pulse) stay unchanged.
Basis: Part 5 requires the evacuation receipt to apply before impact, the decision prompt requires completion before the first severe pulse for full protection, and the achievement acceptance requires the same; with a three-day lead none of these can happen.
Severe targets are already held out of front-footprint retirement while targeted, so the longer lead does not lose targets when the front drifts.
The improvement-loop planner recommended exactly this value, which leaves two days of reaction slack over the seven-day job.
Part 7, the evolution and Event Details text, and the catalog notes are updated to nine days in the same change.

## D3. Evacuation partial effect and local disruption

Disposition: implemented (commit "Give severe evacuations time to work"); values in D8; promoted into Parts 4 and 5.

A paid evacuation that has run one full day grants a reduced share of the evacuation mortality reduction to severe and superstorm pulses; completion grants the full reduction.
Evacuation protection applies only to severe and superstorm pulses, as Part 5 states.
A new state dynamic modifier applies the promised temporary production, construction and supply penalty for the evacuation's duration and is removed when the severe episode closes.

## D4. Two Regions Ready uses late warning binding

Disposition: implemented (see D12); promoted into Part 10.

A paid urgent national action that is still running when a new warning is published for a responsible state, and that has no warning association yet, binds to that warning visit.
Completion strictly before that visit's arrival then counts; an action that starts after arrival still disqualifies, and one action still credits only one visit.
Basis: every urgent action lasts 14 to 21 days against a seven-day warning, so only an action started before the warning can finish inside it, and the existing bridge captured the association only at start time.

## D5. Humanitarian integration uses a source-specific famine adapter

Disposition: implemented (see D14); promoted into Parts 4 and 11.

Acid Rain registers its proven consequences through an Event 033 famine adapter that mirrors `famine_adapt_natural_disaster_state`: exact applied mortality pulses, tier-2 and tier-3 aftermath, and completed large evacuations, each with Acid Rain source identities distinct from Event 013 and Air Winter.
Evacuation displacement is registered as humanitarian disaster pressure, not as a migration cohort, because Part 5 forbids permanent population transfer without a verified migration API and the migration adapter documents Event 33 as lacking cohort facts.
The adapter addition is coordinated with the famine and migration owner as a minimal append.

## D6. Concurrency follows Parts 5 and 8

Disposition: implemented (see D10); promoted into Parts 2 and 5.

Each national urgent family keeps its own receipt, so different families can run at the same time while each family runs at most once.
Evacuations and state recovery operations keep per-state receipts, and the country counters count in-progress operations against the 2/4/8 evacuation caps and the 1/1/2/3 recovery-operation caps.
Payment, reservation and one-time return stay per operation.

## Implementing-engineer decisions, round 1

These decisions were taken by the Event 033 implementing engineer under the same full design authority, choosing the spec-consistent option in each case.

### D7. Decision cost text reads published display rows

Disposition: implemented (commit "Show real costs on every Acid Rain decision").
The quote refresh effects publish one persistent row per decision for player countries (`acid_rain_cost_<row>_<family>`), passed through the same final quote step (`acid_rain_finalize_loaded_quote`) that the affordability trigger and the debit use, so the shown numbers are the paid ones.
AI countries skip the display rows because they never read them.
The host worker refreshes player rows every worker tick along with AI rows, so discounts and band changes reach the text within three days.
Evacuation and decontamination show "trains or convoys" because the chosen state, not the country, decides the route, and localisation cannot rely on the targeted state scope.
The `_blocked` variant is selected by the engine from `custom_cost_trigger`, which is the same trigger the start transaction rechecks.

### D8. Evacuation effect values

Disposition: implemented (commit "Give severe evacuations time to work").
The partial share is 50 percent of the full evacuation reduction (`acid_rain_mortality.evacuation_partial_share`), granted from one full day after the start (`acid_rain_preparedness.evacuation_partial_delay_days`) to severe and superstorm pulses only.
The finished-evacuation damage-pressure reduction is limited to severe and superstorm pulses for the same reason.
The disruption modifier `acid_rain_evacuation_disruption` costs 15 percent local factory output, 25 percent local construction speed and 15 percent local supply; it is added at the start, removed at once if the evacuation fails, and removed when the severe episode closes after a finished evacuation, with a 40-day safety duration.
The evacuation decision requires a free national action slot, because the start transaction already required one and a decision that could be taken without effect is a defect; concurrency (D6) replaces this gate with per-state receipts.

### D9. Registry arrays are created before indexed writes

Disposition: implemented (commit "Create Acid Rain registry arrays before writing their elements").
An indexed `set_variable` only changes an existing element (Data structures, arrays section of the offline wiki), and every other system in the mod creates its arrays first; 74 Event 033 arrays were only cleared and then written by index.
Each registry is cleared and resized to its bound when it is initialised; severe-cell and superstorm slots start retired so allocation sees them as free.

### D10. Operation model for D6

Disposition: implemented (commit "Run Acid Rain response operations side by side").
National families (Shelter Protocols, Water Distribution, Medical Surge, Reroute Transport, demobilization) each hold one row in `acid_rain_op_*_entries` and their own completion event (`chaosx.nr33.42` to `.46`).
Evacuations and recovery work are state operations held on the state with the paying country as a scope variable, listed in the owner's `acid_rain_op_states`, and completed by the state event `chaosx.nr33.47`; `acid_rain_evacuations_active` and `acid_rain_recovery_ops_active` count operations in progress against the band caps 2/2/4/8 and 1/1/2/3.
Civilian factory commitments of running operations sum into one variable-valued modifier, `acid_rain_action_commitment`.
A completed evacuation keeps its protection and disruption until its severe episode closes but no longer occupies an evacuation slot.
Natural acute closure keeps paid recovery work and demobilization running and releases the rest; administrative closure releases everything.

### D11. Decision visibility and gates (Part 5 category table)

Disposition: implemented (same commit as D10).
Projects stay visible and payable during warnings and exposure.
Recovery decisions appear only when no warning, exposure or forecast covers the country, and each targets a state with aftermath and no acute weather of its own.
Shelter Protocols, Water Distribution and Reroute Transport cannot be bought while their protection is still in force, and Medical Surge waits for medical fatigue to end.
Demobilization opens whenever no warning, exposure or forecast covers the country and there is apparatus to wind down; it cancels unfinished projects through the normal path, keeps the recovery tail, and grants `acid_rain_demobilized_recovery` (10 percent repair speed, 5 percent construction speed) for 60 days, which also blocks a repeat.
The AI does not demobilize while the crisis is active and projects are running, so paid projects are not thrown away.

### D12. Two Regions Ready late binding (D4)

Disposition: implemented (same commit as D10).
When a warning visit is recorded for a state, its controller binds every running urgent operation and evacuation that has no visit yet to that visit; the existing arrival recorder then credits only completion strictly before arrival and rejects starts after arrival.

### D13. Recovery actions follow the recorded burden

Disposition: implemented (commit "Tie Acid Rain recovery to the damage the rain recorded").
Restore Transport targets only states with rain-recorded infrastructure or railway damage points and clears those points when it finishes; Repair Industry does the same for civilian and military factory points, so neither can repair more than the rain damaged.
Decontamination targets states whose rain impact left an environmental burden (`acid_rain_environmental_burden`, set by every recorded window impact and cleared when the aftermath tier reaches zero); it consumes nothing else, so a state can always be cleared once its structural damage is repaired.
AI scoring favours transport when transport points are the larger structural burden, industry when factory points are larger, and decontamination when no structural damage remains.
Probability evidence: `hoi4.probability_inspect` with adapter `decision_ai_will_do` on `common/decisions/033_acid_rain_decisions.txt` returned `INTERNAL_ERROR` on 2026-10-04, as it did for the lead, so no baseline or comparison could be produced; the factors are the existing `@acid_rain_ai_*` aftermath factors plus one new 1.5 factor.

### D14. Humanitarian amounts (D5)

Disposition: implemented (commit "Register Acid Rain humanitarian pressure with the famine system").
`famine_adapt_acid_rain_state` is a minimal append to the famine-owned adapter file and its documentation table; it mirrors the Event 013 adapter and requests natural-disaster pressure.
Event 033 builds the proof bundle in `acid_rain_register_humanitarian_pressure` with source id 33, the Acid Rain death reason, the current generation and a per-transaction revision (positive pulse receipt count, aftermath tier, or evacuation operation key).
Registered amounts: each exact positive pulse loss; 0.5 percent of the state population when its aftermath first reaches tier 2 and 1 percent at tier 3; 2 percent when an evacuation of a state with at least 500k people finishes.
At the famine owner's 20 percent maximum share these are small pressure steps, so the rain adds strain without overriding famine's own drivers.
The famine and migration owner could not be reached from this run; the append touches no existing famine code and is recorded here for that owner's review.

### D15. Decision AI against Part 8

Disposition: implemented (commit "Bring Acid Rain decision AI in line with Part 8"); probability evidence blocked.
Projects two tiers above the weakest component score x0.40; Medical Surge scores x1.75 once rain deaths pass 0.02 percent of the starting population; evacuation scores x1.40 for states of at least one million people, x1.25 for infrastructure below 3, and x0.35 when an evacuation started today would finish after impact (each forecast stores the latest useful start day); recovery follows the main burden (D13); Shelter Protocols and the other protections cannot be bought again while in force (D11); the AI no longer demobilizes mid-crisis while projects run (D11).
Urgent actions that cannot affect any remaining pulse are kept out by visibility: they vanish when no warning, exposure or forecast remains and when dissipation is pending, which is when no further pulse can come; a finer arrival-window test needs per-country departure forecasts that the runtime does not keep.
The evacuation shelter-tier modifier now reads the country tier; it previously read a state variable that never exists.
Probability evidence: `hoi4.probability_inspect` (`decision_ai_will_do`, Event 033 decisions file) returned `INTERNAL_ERROR` on 2026-10-04, so no baseline or `probability_compare` pass exists; the exact blocker is this route error.

### D16. Superstorm map markers

Disposition: implemented (commit "Mark Acid Rain superstorms on the world map").
Each superstorm slot records the region of its seed state (`global.acid_rain_superstorm_region_entries`) when the forecast is created and clears it when the storm retires.
The world map shows one severe-storm marker per listed superstorm (the same three the Active Weather card lists) at that region's anchor, from forecast until retirement, with the still marker in its place when motion is turned off.
Anchors are the alpha-weighted centres of the seven region overlays under the map's 0.3188 fit, minus half of the 46-pixel marker; a storm whose region already holds an earlier listed marker moves 48 pixels right so the two never overlap.
Ordinary front markers and superstorm markers never share the map, because fronts are projected only up to the global warning and superstorms exist only in the global phase.
Render evidence: `hoi4.gui_render` at 1920x1080 UI scale 1 was refused by the route's fixed aggregate pixel budget (`RENDER_AGGREGATE_BLOCKED`, 65.6 million reserved pixels before the frame); the same scenario rendered at 1366x768 UI scale 1 (scenario `event033_superstorm_markers_offset48_1366`, source revision `e9ae501790b53115`) and showed two Europe markers side by side without overlap and a third at the Australia and Pacific anchor, all inside the map panel; a first render with a 30-pixel shift showed the shared-region pair overlapping, which set the 48-pixel shift.

### D17. Global weather loop and static veil opacity

Disposition: implemented (commit "Replace the Acid Rain global weather curtain with separated cloud banks").
The rejected continuous-curtain sheet is replaced by the v3 loop: eight separately generated native-alpha frames with three separated cloud banks over a readable map, following the existing frame plan (000 sparse rest, 001-004 shifting banks and rain groups, 005 crest, 006 central dissipation, 007 near-rest bridge to 000).
Frames 000-004 come from the earlier built-in ImageGen v3 run; frames 005-007 were generated in this round through the gptimage MCP route (the ChatGPT-subscription image model, no model selector exposed) as edits of the seed and the neighbouring frame with a transparent background, and kept their native alpha.
Every frame is normalized with one uniform scale to 560x300 at anchor 0,0 and assembled into a 4480x300 sheet at 4 FPS (`GFX_acid_rain_global_animated`); frame 000 is the still fallback (`GFX_acid_rain_global_static`); both DDS files are uncompressed BGRA with an exact RGBA round trip.
Per-frame mean alpha stays between 28 and 45 (65 to 77 percent of each frame fully clear), against about 206 for the rejected curtain.
The warning veil keeps the defringed v6 art (no saturated red or yellow edge pixels) and returns to the original approved opacity: its alpha is multiplied by 0.5376 so its mean alpha is 45.75 instead of 85.14, which keeps continents readable under the warning bands.
`GFX_acid_rain_global_veil` is registered but no window element displays it, because the global layer uses the animated sheet and its still frame; its file is left unchanged and has no in-game effect.
Render evidence: `hoi4.gui_render` scenario `event033_global_phase_v3_isolated_1366` (1366x768, UI scale 1, source revision `d2ebe7b4077590277`), with only the global-phase layers shown, displays the sparse banks over a readable map with the three superstorm markers legible on top; 1920x1080 remains refused by the route's aggregate pixel budget.
The working package (sources, processed frames, sheet PNG, review-only GIF, contact sheet, lineage and `animation_manifest_v3.json`) is under `docs/assets/033_acid_rain/icon_artist/animations/acid_rain_gui/global_repair_v3/`, which is not tracked in Git; the facts above are the durable record.

### D18. World window footer navigation

Disposition: implemented (commit "Add Back and Details to the Acid Rain world map footer").
HOI4 script cannot open the decisions panel, so the Part 6 category return is a Back button that closes the map and reveals the view it was opened from: the Acid Rain decision category, or Event Details when the map was opened there; its tooltip names that view.
Details closes the map and opens the Event Log on the Event 33 Event Details page through the shared entry points (`open_events_log_events_tab`, `get_event_type`, `events_log_add_event_details_entry`); it is hidden when the map was opened from Event Details, where Back already returns there.
Footer order is Refresh, Back, Details, the shortened hint, and the motion toggle; `hoi4.gui_render` scenario `event033_footer_nav_1366` (1366x768, UI scale 1, normal and hover, source revision `e5defa54f5953522`) shows the four buttons evenly spaced with separate click regions and the hint unclipped.

### D19. Region index for region-bounded work

Disposition: implemented (commit "Scan only the affected region in Acid Rain front work").
When the frozen registry forms, `acid_rain_build_region_index` copies its states into `global.acid_rain_region_ordered_states` grouped by region, each group in registry order, with half-open bounds in `global.acid_rain_region_index_start_entries` and `global.acid_rain_region_index_end_entries`; `acid_rain_prepare_region_cursor` returns a region's bounds and rebuilds the index when it belongs to another generation, which also covers saves made before the index existed.
Front region commitment, warning publication, arrival, departure, forced coverage, footprint growth, footprint retirement, front completion and all five severe-cell pool scans now read only the front's region slice through `for_loop_effect` and `var:` element scoping, a pattern already used across the mod.
Every state a front targets lies in its current region, because targets are only touched inside region-filtered scans and all of a front's targets are released before its region changes; within a region the slice keeps registry order, so the same states are visited in the same order and coverage, first and second visits, retirement and dissipation behave as before.
Superstorm region activity reads the live superstorm target array instead of the registry; superstorm candidate pools stay world-wide because a superstorm may start in any region.
The registry clear also drops the index generation so a cleared registry is never read through a stale index.
The world-wide passes that remain are once-per-transition work (runtime start, global transition, legacy adoption, superstorm forecast creation and cleanup).

### D20. Transport readiness softens acute penalties

Disposition: implemented (commit "Let Transport readiness soften acute Acid Rain supply losses"); promoted into Part 4.
Acute rain bands read their supply, movement and attrition penalties from state variables written whenever the band is published.
Each band value shrinks by 10 percent per controller Transport tier and by another 20 percent while Reroute Transport protection is in force, never below 40 percent of the band value, and a change of controller republishes the band with the new controller's readiness.
Basis: Part 5 and the decision text promise that Transport tiers and Reroute Transport limit acute supply and movement disruption, and fixed modifier values could not deliver that.

### D21. Catalog row

Disposition: accepted and queued for the catalog owner in [catalog_changes_pending.md](catalog_changes_pending.md).
The Event 33 Details and Evo I to III cells take the in-game Event Details and evolution text, including the nine-day forecasts, and Status moves from To Be Reworked to Needs Testing because the rework is implemented in source and live-game verification is the remaining gate.

## Review round 1 decisions

These decisions were taken by the Event 033 round-1 reviewer under the same full design authority.

### D22. Superstorm markers follow the global layer

Disposition: implemented (commit "Keep Acid Rain storm markers to the global layer and name its constants").
Final dissipation clears superstorm target states but keeps the superstorm slot records, so an aftercare or closed world map still listed forecast and active storms and showed their markers over a map with no storm.
`acid_rain_gui_project_superstorm_marker` now projects a marker only while the global layer is projected (`global.acid_rain_gui_global_layer_active`), the same gate the superstorm list card already uses, so markers appear from forecast to retirement during Global Acid Rain and never after it.
The acute-band selector reads the existing `acid_rain_aftermath.modifier_*` constants instead of literal band numbers, and the Transport and wartime AI factors on Reroute and Harden Transport read named file constants with unchanged values.

### D23. Player text and achievement wording

Disposition: implemented (commit "Plain wording for Acid Rain player text and achievements").
The Acid Rain achievement texts and eligibility tooltip drop Event 33, valid campaign, eligible state, national responsibility, administrative early termination and scheduled route check wording and state the same conditions in player terms.
The category, project, global-layer, world-map and Event Details texts drop "returns once", "safe cancellation", "dissipation check", "valid records", "registered at formation" and "valid inhabited state"; the queued catalog values in [catalog_changes_pending.md](catalog_changes_pending.md) match the new Event Details and Evo III text.

### D24. Front markers follow their region

Disposition: implemented (commit "Place Acid Rain front markers at the region each front covers").
The three ordinary front markers sat at fixed per-front spots on the world map, so a front crossing Asia still showed its swirl over the Americas, which contradicts Part 6 (each front marker carries its current region at a reviewed region anchor).
The GUI projection now places every front's ordinary, warning and severe markers, animated and still, at the D16 anchor of the region the front covers or is about to reach, through scripted GUI `x`/`y` properties; fronts never share a region, so no shift is needed, and a front without a region is not projected.
The fixed GUI positions remain only as the pre-projection defaults.
The offline GUI scenario route cannot set the global marker variables, so the placement itself is a live-game check.

## Implementing-engineer decisions, round 2

These decisions were taken by the Event 033 implementing engineer under the same full design authority, from the round-2 work list.

### D25. Advance warnings are keyed by front visit

Disposition: implemented (commit "Send one Acid Rain warning per front visit").
Part 9 asks for one warning per front and destination country and a warning cooldown keyed by front visit ID, but the warning report was deduplicated by front id, so a country received one warning per front for the whole event and nothing when the same front returned.
The controller now stores `acid_rain_last_warning_visit_id` and receives chaosx.nr33.102 whenever the publication's key differs from it.
The key is the warning visit id that both publication paths already allocate per visit and generation; when the 24-entry visit registry is full and the id is 0, `acid_rain_compute_warning_report_key` builds a negative key from the front id times `acid_rain_reporting.warning_fallback_front_stride` plus the publication date, which can never equal a visit id.
Several warned states of one visit still produce one report, a return to the same region and a visit by another front each produce a new one, and the country initializer clears the new key and the retired `acid_rain_last_warning_front_id`.

### D26. Severe impact reports are keyed by episode

Disposition: implemented (commit "Send the Acid Rain severe impact report once per episode").
The impact report chaosx.nr33.104 was gated by a country flag cleared only at formation, so a country saw one impact report for the whole campaign; Part 9's cooldown ledger keys severe impact reports by episode ID.
At a positive severe or superstorm pulse the state supplies its episode key, the severe cell id for cells and the superstorm episode serial stamped at forecast for superstorms, and `acid_rain_send_severe_impact_report` reports only when the key is above the controller's stored key.
Cells and superstorms keep separate keys (`acid_rain_last_severe_impact_report_id`, `acid_rain_last_superstorm_impact_report_id`) because their serials are counted separately, and the comparison is "greater than" rather than "different": both serials only grow within a generation, and two overlapping episodes over one country, such as two fronts' cells over a country spanning two regions, would otherwise alternate one shared key and resend the report on every pulse.
The first positive pulse of each episode therefore reports once per affected country and later pulses of that episode report nothing; the cost of the strict ordering is that an older episode whose first positive pulse in a country comes after a newer episode's report does not report again, which the newer report already covers.
The retired once-per-campaign flag is still cleared at initialization for older saves.

### D27. Report facts from Part 9

Disposition: implemented (commit "Give the Acid Rain reports the facts Part 9 lists").
Each report reads facts the runtime stores on the recipient country, or globally for the dissipation summary, just before the report is sent; no report text scans states.
The advance warning (102) names the destination region and gives the days until arrival, the number of the country's controlled states in that region (counted across the whole visit, since every state of the visit passes through the same controller hook) and National Preparedness, and names the lowest-tier Preparedness component with its tier, ties going to the heavier component in Preparedness weight order; the old claim that civil-defense offices had already opened shelters is gone, because the game does not model it.
The forecast (103) counts the country's forecast states for the episode and names the most populous by current population, with a superstorm title and text when the episode is a superstorm.
The impact report (104) states whether the named state's evacuation had finished, was still under way with partial protection, or was absent, and gives the days left in the severe episode, with a superstorm title.
The departure report (107) gives the length of the national exposure that just ended (from a new exposure start day stored when the national exposed-state count leaves zero), the controlled states still carrying aftermath and their highest tier; the highest tier is read from the country's own controlled states at send time, only when some carry aftermath, rather than adding a per-tier ledger to the shared count publisher.
While the country carries the warning flag, the departure report becomes "A Temporary Respite" and keeps the urgent measures in view, as Part 9 asks; the flag does not name the warning front, so the text says a front is approaching another part of the territory rather than "another front".
The dissipation report (109) lists duration, worldwide deaths, states reached out of the states in the rain's path, Air Contamination added, severe cells, superstorms and states still carrying aftermath; the summary store is a separate effect called from the final cleanup, so the cleanup itself still never touches the Air ledger.
Preparedness reads as a whole percentage in the arrival and casualty reports as well, matching the decision category and world map, and the two legacy migration modifiers have names and descriptions.
MCP route evidence: `hoi4.event_inspect` (`mode = lint`, selector `{kind = event, eventId = chaosx.nr33.107}`, helpers off) returned `EVENT_INSPECTED_PARTIAL` with 0 blocking diagnostics at revision `5719043420248110bbe4bc663b73ccd1d5b12e6ef7b4d318b2389c6c870dc467`.
How the engine lays out the longer report text in the event window is a live-game check.

### D28. World map at formation and live national strip

Disposition: implemented (commit "Open the Acid Rain world map at formation and keep each open map current").
Part 6 opens the map automatically at formation only for players whose selected country has an active or warned state; the mod has no settings option for opening major-event windows for all players, so that branch does not exist.
After the formation stage commits, `acid_rain_gui_open_at_formation` runs the normal read-only open for every human country carrying the warning or exposure flag, once per generation behind `acid_rain_formation_map_opened` (cleared with the other generation flags), so a duplicate formation opens nothing; the super-event and its audio are unchanged and closing either window has no gameplay effect.
The national strip copy moved out of `acid_rain_gui_refresh_read_only` into `acid_rain_gui_refresh_national_strip`, which the full refresh still calls.
Inside the host worker's existing participant loop, every human country with an open map of the current generation runs that strip refresh, and the host refresh that follows projects the shared world view, so Preparedness, warned, exposed, severe and aftermath counts, deaths and deaths prevented change on the next worker tick without a click.
Only the strip, not the whole projection, runs per viewer, because the world view is shared and the host already projects it every tick; no world iterator was added and the refresh still writes only presentation variables.

### D29. Severe forecast cue

Disposition: implemented (commit "Play a thunder cue with each Acid Rain severe forecast").
Part 6 asks for a stronger sound cue for a player whose country contains a forecast state.
The cue reuses the base game's one-shot thunder samples (`weather_thunder_01` to `_04`) through six event-owned sound effects in `sound/033_acid_rain_sound.asset`, `chaosx_acid_rain_severe_forecast_cue_0_5` to `_3_0`, rather than adding sourced audio, following the event-owned asset precedent of Event 028; the names are listed in the Effects category of `sound/chaosx_sound.asset` so the effects volume slider applies.
`acid_rain_play_severe_forecast_cue` runs in the same once-per-episode branch that sends the forecast report, for severe cells and superstorms alike, so a human controller hears one cue per forecast episode and later states of the same episode, AI countries and other players hear nothing.
The suffix is chosen with the shared `GetSuperEventAudioVolumeToken`, the same mapping the super-event audio uses, and the x0 setting plays nothing; volumes run from 0.33 to 2.00, 1.00 at the default x1.5.
Listening to the cue is a live-game check.

### D30. The weekly Air request reads the active world share

Disposition: implemented (commit "Request Acid Rain Air from the weather on the map in every acute phase"); promoted into Part 11.
Gate 9 says weekly requests use "stored coverage", while Part 11 gives an "Active world share" table; the more specific Part 11 table is taken, and the share is the states under acute rain now, not the states the rain has ever reached.
The request moved out of the regional branch of the host worker into `acid_rain_try_weekly_air_request`, which runs in the regional and global phases and never while dissipation is pending or after closure, so the global layer's own adder takes effect.
The active states are the ordinary front targets plus the states of active severe cells that lie outside them (a cell can outlast the front that formed it), or every valid state while the global layer is active; they are divided by the valid states and mapped exactly to 4, 8, 12 and 16 bp below 2, below 5, below 10 and at or above 10 percent.
Intensity takes the average of the open fronts (active or retiring, the same set `acid_rain_front_is_open` uses), or the Standard band that the global pulses use; when only a severe cell whose front has moved on is raining, the lowest band applies.
Two or more open fronts add 4 bp, the global layer 10 bp, and each active severe cell or superstorm 3 bp up to 9 bp; the total is clamped to 8 to 45 bp before the unchanged 1500 and 5000 bp caps in `acid_rain_apply_air_request`, and a week with no state under acute rain requests zero.
The next due day advances one week from the previous due day rather than from the worker tick that applied it, so the three-day worker averages seven days; if the advanced day is still not after today (no request for over a week, as in a save made before this cadence), the cadence restarts from today instead of replaying missed weeks on consecutive ticks.
All values are `acid_rain_air` constants, with the new `active_share_percent_scale` and `split_min_fronts`.
`.tools/validation/validate_033_acid_rain.py` passes.

### D31. Tooltip text and icons take the cursor

Disposition: implemented (commit "Let the Acid Rain map and category tooltips appear on hover").
Thirty-two elements of `interface/033_acid_rain.gui` carried both a tooltip and `alwaystransparent = yes`, which passes the cursor to whatever lies beneath, so none of the Part 6 tooltips could appear; the repository treats the flag as blocking hover (Event 013 places its tooltips on transparent button hitboxes above click-through labels, and Event 019's labels are click-through so hover reaches the button below).
Every element with a tooltip drops the flag: the category coverage and Preparedness lines, the world ledger, each front card's timing and severe-cell lines, the global card status, the coverage label and value, the seven region rows, the Preparedness badge, value and four component pips, the six national counts and the national contamination line.
None of them overlaps a button (the category Open button sits below the two category lines, the close button lies right of the ledger, and the footer buttons lie below the national strip), so no hitbox button was needed; decorative overlays, veils, markers, frames and plain text keep the flag, and no button's click region changed.
MCP evidence: `hoi4.gui_render` of `acid_rain_world_window` (scenarios `event033_tooltip_hover_before_1366` and `event033_tooltip_hover_after_1366`, 1366x768, UI scale 1, normal and hover, source revisions `87f76dfd265dc631` and `256af9313b397626`) produced byte-identical full, cropped and click-region images (PNG sha256 `98135053e60f1403`, `fb957e3b9342c2fc`, `f766dc4b27c29cd3`); the same held for `acid_rain_category_inlay` (`event033_inlay_tooltip_before_1366` and `_after_1366`, revisions `781caf69c3087a80` and `b9099733bf218a08`, full and click-region PNG `b23791c5fa9fd3e6`); `hoi4.gui_inspect` before and after (`event033_tooltip_hover_before`, `event033_tooltip_hover_after`) returned `GUI_INSPECTED` with 160 inspected elements and a parsed source graph.
Whether the engine now shows each tooltip on hover is a live-game check; the offline renderer models layout, not hover.

### D32. World notices reach every player

Disposition: implemented (commit "Show the Acid Rain world notices to every player").
The Rain Concentrates (chaosx.nr33.114), Severe Storm Cells (108), The Front Divides (113), A Global Acid Layer Forms (111) and Global Acid Rain (112) were sent only to the scheduler host, or to the formation country for the formation-time 111, so in multiplayer every other player, and every player when the host was CXT or an AI annexer, missed them; Part 9 calls them global reports and Gate 18 asks for the same presentation for all players.
Each of the five events carries `major = yes` with `show_major = { is_ai = no }`, the vanilla major-event mechanism already used by the Event 33 news events (and by the base game's south_american_events.61 and .62 country events), so one firing at the existing once-per-transition call site reaches every human country once whoever receives it; no loop and no periodic world iteration was added.
Their texts are world-level and read no recipient facts, so a copy reads the same for every player; the 112 and 204 pair at global opening still fires once from the host, and the dissipation report 109 keeps its participant loop.

### D33. Region, Preparedness and category status facts

Disposition: implemented (commit "Show each Acid Rain region's weather, visit and quota on hover").
Part 6's state footprint summary asks that hovering a region show the active states in the front there, the states reached on the current visit, the untouched states, the eligible total, the visit quota and the severe-cell state count, and that the Preparedness tooltip show the four component contributions; the region tooltips were static sentences and the category status line named only the exposed count.
The read-only refresh now runs `acid_rain_gui_project_region_facts`, which copies stored counters into presentation arrays indexed by region id: reached, never reached and eligible counts from the region registry, and for each front its region status, read with the same gate as the front cards.
A front that is active, or retiring while it still covers its region, is over that region and contributes its active state count, the states it first reached on this visit, its visit quota and the target states of its unexpired severe cells (the same count its card shows); a front before arrival, or a retiring front's announced destination, marks that region as approaching with the days until arrival, and a front over a region takes precedence; under the global layer every region reads as covered.
Each region row's tooltip sets its region id and loads those facts into temporary variables through the scripted trigger `acid_rain_gui_load_region_tooltip`, the documented scripted localisation pattern in which temporary variables set in a text's trigger remain set for its localisation, so one shared text serves all seven regions; nothing is scanned on hover and nothing outside presentation variables is written.
The Preparedness tooltip reads the country's four component tiers through `acid_rain_gui_load_preparedness_tooltip` and shows each tier with its points (tier times the component gain) out of the component weight, so it stays current in the category inlay even when the map has not been opened; the category status line names exposure, a storm forecast or a warning in that order of urgency, with the country's exposed, warned and forecast state counts.
MCP evidence: `hoi4.gui_render` of `acid_rain_category_inlay` (scenario `event033_inlay_status_after_1366`, 1366x768, UI scale 1, normal and long-text, source revision `eabda8951a862759`) reports no clipping or overflow diagnostic and no visible overlap; the offline renderer leaves scripted localisation unresolved and draws no tooltips, so the rendered tooltip text and the status line at full counts are live-game checks.
