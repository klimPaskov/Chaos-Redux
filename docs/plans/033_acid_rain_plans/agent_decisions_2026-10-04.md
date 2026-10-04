# Event 033 agent decisions, 2026-10-04

Disposition: implemented; D1 to D20 are promoted into the accepted Event 033 specs (Parts 2, 4, 5, 6, 7, 8, 10 and 11, each in its "Accepted implementation decisions, 2026-10-04" section), D21 is accepted and queued for the catalog owner, and D22 and D23 are implemented review fixes.
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
