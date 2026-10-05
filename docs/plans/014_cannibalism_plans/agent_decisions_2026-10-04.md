# Event 014 agent decisions, 2026-10-04

The user granted the implementing agent full design authority for the Event 014 takeover after the Codex owners stopped.
Each entry below is an agent decision taken under that authority, with its basis and the implementation that carries it.
Disposition labels follow `CLAUDE.md` Specs and Plans.

## D1. Adopt the stopped thread's Larder logistics patch

Disposition: `implemented`.

Basis: the uncommitted patch matches the parent-accepted tuning recorded in `subagent_handoffs/2026-10-04_larder_logistics_implementation.md` (base 1200, 100 per controlled state, 50 per administrative contract point, ceiling 5000, ordinary cap 2000) and its same-scenario probability comparison in `subagent_handoffs/2026-10-04_larder_probability_comparison.md` shows no direct weight change.
It closes audit finding E014-FINAL-04 and spec part 7 "Larder integration" except the hidden-hoard line, which stays a separate accepted requirement.

Decision: adopt the patch after settling the three review points below, and commit it with its owner plan, audit and evidence folders.
The archived before/after source snapshots under the two evidence folders keep their exact bytes through a `-text` attribute, following the Event 021 and 035 precedent.

## D2. A donor with no capturable capital ships at the maximum route loss

Disposition: `implemented`.

Basis: the patch made `cannibalism_prepare_larder_transfer_quote` fail when either capital could not be captured or the distance read stayed unwritten.
Absorption and autonomy then refused the whole transaction, which could leave a warlord in pending absorption forever, and the Wendigo constructor could refuse its reveal when the transformed ZZZ host holds no state.
A free full transfer would reward the missing capital, while a refusal strands the actor.

Decision: an invalid country or generation context still fails the quote.
A missing capital capture or an unwritten or negative distance now quotes at `cannibalism_larder_logistics.distance_loss_maximum` (0.60), so the shipment loses the most it can lose on any route and the transaction proceeds.

## D3. Constructors always finish once the public reveal flag is set

Disposition: `implemented`.

Basis: the patch gated the CBL constructor's integration, annex, host pointer, roster rebuild and result on the runtime migration result, after the reveal flags, the CBL capital and the Hannibal leader had already been installed.
The Wendigo constructor likewise gated its whole reveal tail on the primary donor's absorption, and gated entry to its reveal block on the quote.
Either failure would have left a revealed but unfinished unification, and in the Wendigo case the dispatcher would then also try to build CBL.

Decision:

- CBL: runtime migration still runs, but the opening Larder assignment, commander, war joining, annex, host pointer, generation, finalization, reveal events and roster rebuild no longer depend on its result.
  An unmigrated spread row has a dead source country after the annex and is invalidated by the normal spread resolution when due.
- Wendigo: the reveal block is entered whenever the constructor's existing host checks pass.
  A donor that is not absorbed (both players human, a failed quote or a failed migration) keeps its own stores, is not annexed, and answers the normal response event through the rebuilt roster, while the transformed country receives the zero-snapshot opening assignment.
  The evolution record, super-event, anchors, focus overlay, roster, report, news, pending-flag clear and result always run after the public flag.

## D4. Keep the spread-queue preflight in both constructors

Disposition: `implemented`.

Basis: review point (a) asked whether the constructor-level `cannibalism_validate_spread_queue` gate could block the reveal for good.
The reveal dispatcher `cannibalism_execute_evolution_iii_reveal` in HEAD already runs the same validation before either constructor and refuses the reveal on failure ("A malformed queue remains flagged for diagnosis and cannot be carried into either irreversible unification branch").
Validation does not fail on stale rows: a row whose source or target country has died still loads its scopes and is invalidated when due through `cannibalism_resolve_loaded_spread_entry`.
Only genuine corruption (misaligned arrays, duplicate IDs, illegal status or mismatched state metadata) sets the durable `cannibalism_spread_queue_invariant_failure` flag.

Decision: keep the constructor preflight, which adds no blocking condition beyond the dispatcher's existing one and protects the irreversible reveal from starting on a queue that changed in between.

## D5. Network dossier records are shared subject records, not per-viewer intelligence

Disposition: `implemented`.

Basis: audit finding E014-FINAL-02 and spec part 6 require seven fields per Network node card.
The data API proposal (`2026-10-04_gui_data_implementation/evidence/owner_api_proposal.md`) stored every record per observer with `_@ROOT` keys, viewer epochs, reciprocal cleanup indexes and human tag-transfer rules, and left its two-human transfer case unresolved.
The Network lists, however, are the shared global actor and node registries, visible to every viewer with the same rows; per-viewer records would leave most fields unknown for everyone except the report recipient and cannot be read by plain localisation.
The lead allowed consolidating helpers where the required semantics hold: real writers only, unknown distinct from zero, reveal secrecy, and no whole-world iteration.

Decision:

- Records live on the subject STATE or COUNTRY and are read by every viewer; the viewer owns only its tab, sort, page and selection.
- Writers are the delivered reports `.2`, `.20`, `.21`, `.30`, `.60`, `.61`, `.62`, the two route screening payments, spread containment and warning closure, and the start, result and clear effects of the six counteraction missions.
- Certainty is derived from the stored dates: observed, stale (an incident later than the last strength measurement), partial (records but no measurement), or no reports.
- Inbound route warnings appear as state rows while their warning is live, so a defender can see the route and its screening before arrival; the bounded spread queue is read only when the player refreshes the window.
- Rows keep the 374x64 card art and show all seven fields on three lines; the selected dossier is a one-row native list on a dark vanilla `GFX_mini_bg` panel that adds dates and the ordering country.
- The window keeps its centred placement through an explicit negative position instead of `origo = center`, which the production render showed clipping three quarters of the window.

Implementation evidence: `docs/events/014_cannibalism/gui_data_contract.md`, the matching Event014 commit, and the MCP evidence in `subagent_handoffs/2026-10-04_network_dossier_mcp_evidence.md`.

## D6. The targeted March raid keeps a Host-wide cooldown

Disposition: `implemented`.

Basis: the parent-accepted raid proposal keeps the existing 30-day `days_re_enable`, but a `state_target` decision re-enables per target state, which would let the March Host strike a different hub every day.
That would change the action's cadence, its AI frequency and its Larder drain without an accepted balance change.

Decision: a successful strike sets the timed country flag `cannibalism_march_raid_cooldown` for `cannibalism_warlord_decision.long_reenable_days`, and the decision's `target_root_trigger` hides the action while it runs.
The per-state `days_re_enable` stays as the native re-enable value.
Every target and cost check runs before the single debit, so no refund branch exists; a target that stopped qualifying since selection charges nothing and keeps the earlier receipt.
The receipt result distinguishes a hub that kept an undamaged level from one put out of action, and its controller generation is stored only when the controller is an Event 014 actor.

Addendum (round 2, R2-1): the receipt no longer reads provincial damage; see R2-1 below.

## D7. Host command window pages

Disposition: `implemented`.

Basis: audit finding E014-FINAL-03 (warlord part) and the parent-approved 2026-10-04 Overview/States composition.

Decision:

- The States page list is rebuilt when the player opens the page; each card rechecks control when drawn and labels a lost state instead of hiding it, so the list never shows a gap or a stale owner.
- The command windows keep refreshing every frame, without a `dirty` variable, so the live Larder, Frenzy and Alignment values never freeze.
- The raid card uses the existing continental target card art instead of a second controlled-state card, so the strike record reads as a different kind of card from the state list.
- The page flag is view state only and clears with the other view state on an incarnation reset.

## D8. Revealed command window pages

Disposition: `implemented`.

Basis: audit finding E014-FINAL-03 (revealed part), the spec's plural "continental target cards", and the parent-approved 2026-10-04 Overview/Loyalty composition, whose layout handoff left open whether one last committed target satisfies the plural cards.
Two loyalty lists and a target card do not fit the 282x222 panel beside the portrait without shrinking every row below readable size.

Decision:

- The window has three pages: Overview (the approved value area), Loyalty (the approved integrated and surviving lists) and Targets.
- The Targets page keeps the three newest committed continental targets, newest first, through the `cannibalism_continental_target_record.rolling_count` constant; three cards fill the panel exactly, so the page needs no scrollbar.
- Every committed executor records its target, not only the global campaign, because each of the six orders picks a country and pays for it.
- The integrated history is written when a warlord is integrated, on the revealed host, keyed by actor generation so a repeated record cannot double a row; it clears on an incarnation reset with the targets.
- Surviving warlord rows are stamped with the actor generation seen when the page opened, so a recycled tag reads as no longer a warlord instead of borrowing an older warlord's row.
- The unification seal and terminal line are shown on Overview only, so the list pages never sit under them.
- The page flags are view state only and clear with the other view state on an incarnation reset.

Implementation evidence: `docs/events/014_cannibalism/gui_data_contract.md` and the MCP evidence in `subagent_handoffs/2026-10-04_command_windows_mcp_evidence.md`.

## D9. Wendigo transformation window pages

Disposition: `implemented`.

Basis: spec part 6 lists anchor-state cards for the Wendigo transformation window, the lead treated them like the aggregate-display findings E014-FINAL-02/03, and `global.cannibalism_transformation_anchor_states` already holds the anchors.

Decision:

- The window has two pages: Overview (the existing totals, countdown and pack capacity) and Anchors.
- The Anchors list binds the global anchor array directly, so the cards always match the anchors the transformation counts and no rebuild effect or new record is needed.
- Each card shows the state name, its standing with its strength (unidentified, identified, locked, broken or lost) and who holds it; the holder line names an enemy by adjective so a long country name cannot push the status out of the card, and the tooltip gives the full name.
- The window is shown only to the transformed host, so showing identification there tells the host what the enemy knows without leaking anything to other viewers.
- The title drops "Winter", because the full title did not fit the 410-pixel header box.
- The page flag is view state only and clears with the other view state on an incarnation reset.

## D10. Hidden hoards

Disposition: `implemented`.

Basis: spec part 7 says hidden hoards can create warlord loyalty events, the lead treated that line as an accepted requirement, and the shipped `CBL_audit_the_submitted_hosts` and `CBL_seize_the_hidden_hoards` tooltips promised investigations and seizure missions that did not exist.

Decision:

- Only a hoarder or an autonomy bargain conceals: 0.30 and 0.20 of the dispatch, capped at 0.45 together. The cache comes out of the dispatch before route loss, so the donor's single debit, the host's single receipt and the cache add up; the CBL and Wendigo constructors conceal nothing.
- The cache record lives on the donor's capital state, keyed to the host and its actor generation, and the host keeps only a list of cache states. This survives the donor's annexation and needs no aligned arrays.
- The loyalty event fires when the shortfall is noticed, one review at a time: confront (immediate partial recovery and resistance), tolerate (the cache stays; a governor grows more loyal; authority falls) or bargain (Command Power scaled by the cache for most of it).
- "Loyalty" and "resistance" use real engine levers: a live governor's HOI4 autonomy, and a timed state modifier with resistance target and local supply penalties on host-owned cache states. Dispositions are not changed by a hoard, so a puppet never turns into an enemy through this system.
- The investigation locates every unlocated cache and reopens its review with a better confront share, which gives the audit focus a use on every warlord-settlement route; the seizure mission is Break-the-Warlords only, as the focus tree already gates it.
- The seizure mission requires the host's own divisions in the cache state: two for the whole cache, one for half at the deadline, none loses it. The AI opens a seizure only where two of its divisions already stand, so it never starts a mission it cannot complete; the same target trigger gates player and AI.
- The three new decision and mission icons were generated in the unified decision icon style instead of reusing existing textures, keeping the spec's one-to-one unified decision asset contract.
- The transformed Wendigo host records caches and answers reviews, but has no unified authority and no investigation or seizure.

## R2-1. The March raid hub check reads hub count and a recent-strike flag, not damage

Disposition: `implemented`.

Basis: lead round 2 decision R2-1 and the QA live load, which reported "Not a valid state building" at the raid target trigger and the raid receipt.
`non_damaged_building_level` accepts state buildings only (`documentation/triggers_documentation.md` 6554-6567; vanilla uses it for factories and dockyards), while `supply_node` is a province building (vanilla `common/buildings/00_buildings.txt`, `level_cap province_max = 1`).
No documented trigger reads damage on a province building from a state.

Decision:

- The target trigger follows vanilla `common/decisions/SWE.txt` 2232-2256: a passable enemy-held state beside the Host with `supply_node > 0` and `supply_node < 2`, so exactly one single-level hub, and without the timed state flag `cannibalism_march_raid_recent_strike`.
- A strike sets that flag on the struck state for `cannibalism_warlord_decision.march_raid_hub_repair_days` (30), passed through a temporary variable because timed flags do not accept `constant:` days. The flag keeps a hub under repair off every March Host's list, including other March Hosts that the per-state re-enable does not cover.
- The receipt result is decided from tuning: put out of action when `march_raid_supply_node_damage` (0.50) is not below `march_raid_hub_level` (1), otherwise damaged. At current tuning every strike records a damaged hub, which is what the strike does.
- The 0.50 damage, the per-state `days_re_enable`, the Host-wide cooldown and `ai_will_do` are unchanged. The target pool only loses states struck in the last 30 days, which the same Host could not strike again within its own 30-day cooldown anyway, so no probability comparison was run; a matching `hoi4.probability_compare` remains advisable if the target pool changes further.
- The tooltip names the repair window instead of an undamaged hub, and the raid card text already reads "damaged" or "put out of action".

## R2-2. Land forts and naval bases are placed through a province filter

Disposition: `implemented`.

Basis: lead round 2 decision R2-2, the wiki `Effects` entry for `add_building_construction` (province buildings are placed through `province`), every vanilla bunker and naval base construction (for example `common/national_focus/afghanistan.txt` 4666-4671 and 2175-2196), and the Event 31 precedent in d334dc062.
Six Event 014 rewards called `add_building_construction` for a bunker or naval base with no `province` block and probably built nothing.

Decision:

- `cannibalism_add_state_fort_levels` (STATE scope, caller input `cannibalism_fort_levels`) fortifies every victory-point province with `province = { all_provinces = yes limit_to_victory_point = yes }`. A state without a victory point (a warlord capital or a Wendigo anchor can be one) fortifies its border provinces, and a state with neither fortifies every province, so the reward is never empty.
- `cannibalism_add_state_port_levels` (STATE scope, caller input `cannibalism_port_levels`) builds at coastal victory points, else at the existing naval bases, else at every coastal province, and builds nothing in a landlocked state.
- The Island Host port focus moves its whole port package (naval base, shared slot and dockyard, which vanilla also limits to coastal states) to a held coastal state when the capital is landlocked or lost, preferring a state that already has a naval base.
- The resistance contract capital forts, the unified and warlord capital defenses and the Wendigo anchor defenses all call the fort helper; the levels and the callers are unchanged.
- The province checks read `any_province_building_level` with the same meta-trigger pattern as the siege victory-point check, because a province filter has no state variable.
- Tooltips say the forts go to the capital's or anchor's victory points and that the port work moves to a held coastal state when the capital has no coast.
- Placement on the map is `needs_live_game`; the source now matches every vanilla provincial construction.

## R2-3. Every consumed helper output is caller-owned

Disposition: `implemented`.

Basis: lead round 2 decision R2-3, the `chaos-redux-events` skill (Helper output lifetime), `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` line 440 and the vanilla SWE lerp helper, which returns through a regular variable for the same reason.

Decision:

- Each caller that reads a helper output after the call sets it to the helper's own default immediately before the call; temporary arrays are owned with `clear_temp_array`. This covers the hidden-hoard answers, consumption and recruitment transactions, origin operations including the March raid, warlord recruitment, the spread queue, scenario setup, the Wendigo counterwar, pulse rehoming, the scoring loops, the Event 19 provider manifest and the revealed-window scripted-localisation loaders. The helper definitions carry a `Caller-owned outputs` comment, and `docs/events/014_cannibalism/helper_output_ownership.md` lists every output with its default.
- Values a helper accumulates or adjusts (the scenario node count, the starting units of a scenario warlord, the planned scenario arrays) are owned once by the outer frame and never reset per call. Inputs and cursors such as `cannibalism_spread_queue_index` are never reset.
- When several helpers in one caller write the same values (prefire context, the scenario wrapper, the spread processor), the caller owns them once before the first call, so a later helper cannot erase an earlier helper's result.
- The origin-specialist recruit owns its template at the scavenger warband, so an actor without an origin flag raises a valid unit instead of naming a missing spawn effect.
- The source review found a second defect in the same path: the spread queue audit loads every stored row into the shared route, route parameters and the four spread scopes, so a new route checked while another route was in flight was tested against the last stored row's target and, when that row had ended, could be queued with the old row's scopes. `cannibalism_check_spread_target_state_availability` now keeps the request's route and scopes across the audit and restores them, and `cannibalism_enqueue_spread_entry` computes the route parameters after the check. No tuning, AI weight or probability-bearing value changed.

Scan evidence: a fixed-point helper-output scan (call-graph summaries of temporary writes and inputs across every scripted effect and trigger in the mod, run against the Event 014 effects, triggers, events, decisions, focus, on_actions, scripted GUI, ideas and scripted localisation) found 141 call sites with unowned consumed outputs at e5c3bb072 (134 real, the rest the scenario recursion below) and, after the fix, only the 13 reviewed false positives below.

Reviewed false positives (13 sites, scenario setup only): `cannibalism_scenario_initialize_current_country`, `cannibalism_scenario_initialize_required_actors` and the five `cannibalism_scenario_setup_*` helpers appear to consume scenario scale values, `cannibalism_scenario_use_preflight_plan` and `cannibalism_scenario_setup_failed` from `cannibalism_initialize_current_country`, `cannibalism_scenario_initialize_required_actors`, `cannibalism_scenario_seed_additional_source_states` and the two distribution helpers.
They come from the static path `cannibalism_initialize_current_country` -> `cannibalism_initialize_new_country_incarnation` -> `cannibalism_setup_prefire_evolution_iii_opening` -> `cannibalism_scenario_setup_convergence`, which writes those values in the evolution III opening.
That path never runs inside a scenario setup: `cannibalism_scenario_prepare_scale` and `trigger_cannibalism_scenario` zero `cannibalism_prefire_evolution_iii_pending`, and the opening's own convergence setup only uses the already active first host (`low_countries = 1`).
The values are owned by the two scenario entries (`trigger_cannibalism_scenario` and `cannibalism_setup_prefire_evolution_iii_opening`), and the inner helpers only read or adjust that storage.

Also reviewed and left unchanged: the evolution scheduling calls in `cannibalism_try_schedule_evolutions` (exclusive branches; the third branch sets its own log inputs), and the `chaosx_convert_*` date helpers, whose callers already own `chaosx_date_days` and `chaosx_date_offset`.

Runtime behaviour of temporary storage across scripted-effect returns remains `needs_live_game`; the change is correct under both the conservative frame model and an engine that keeps helper-created temporaries.

## R2-4. A cache outside the host bloc's control is lost when the review is answered

Disposition: `implemented`.

Basis: lead round 2 decision R2-4 and D10, which requires the host bloc's control for a seizure; recovering stores from enemy territory contradicted it, and the review tooltips overstated the result.

Decision:

- `cannibalism_state_is_held_by_root_bloc` (the host or one of its subjects controls the state) is the single control rule for the review and the seizure target.
- When the reviewed cache state is out of that reach, `chaosx.nr14.82` shows a lost-stores description and one option, Write off the stores, instead of confront, tolerate and bargain. The cache is closed with no recovery, payment, resistance or authority change, and the review queue advances.
- Confront, tolerate and bargain check control again when chosen: a cache lost while the event was open is closed as lost by any of them, and a bargain is never charged for it. A bargain the host can no longer pay still leaves an in-reach cache on record, as before.
- The confront tooltip shows the unrest line only when the host owns the cache state, which is when the unrest modifier lands; a subject-held state says the old guard cannot stir unrest there.
- The new option is the only one shown when it appears, so its weight cannot change the AI's choice, and the weights of the three existing answers are unchanged; no probability comparison was needed.

## R2-3 addendum. Lead scan reconciliation

Disposition: `implemented` (review record only; no gameplay change).

The lead's heuristic scan (`lifetime.py`, effects and triggers files only) flags a call when the helper writes a temporary value and the caller names it anywhere later without writing it before the call. It does not tell a later write from a read, and it does not see outer-frame owners or inputs. Re-run against HEAD after 364d07446, it reports 22 sites, down from about 100 before abacbd845. The precise call-graph scan used for R2-3 still reports only the 13 scenario sites recorded above. Each of the 22 lead-scan sites was read in source and is a reviewed false positive:

- Write before read in the caller (the caller sets the value again before its own next use, so nothing the helper left is consumed): `cannibalism_process_current_node_pulse` 2479 (`cannibalism_new_state_stage`, set again in the later exclusive branches); `cannibalism_retire_current_state_from_warlord_slot` 5726 (`cannibalism_new_state_stage` and `cannibalism_recovery_stage_days`, set in the `else` branch); `cannibalism_apply_loaded_spread_to_current_state` 11212 (`cannibalism_new_state_stage`, set in the `else` branch); `cannibalism_resolve_loaded_spread_containment` 11288 (`cannibalism_ui_new_incident` and `cannibalism_ui_new_operation`, set before the next record call); `cannibalism_initialize_new_country_incarnation` 3661 and 3666 (`cannibalism_chaos_change` and `cannibalism_chaos_reason`, set before `cannibalism_apply_chaos_change`).
- Exclusive branches: `cannibalism_try_schedule_evolutions` 3236 and 3240. The `events_log_evolution_*` inputs and `cannibalism_evolution_transition_authorized` are only written again in the later `else_if` branch, which sets its own values.
- Loop cursors written after the queue audit: `cannibalism_validate_spread_queue` loads every stored row into `cannibalism_spread_queue_index`, `cannibalism_spread_route` and `cannibalism_expected_spread_id`. Every caller resets its cursor after the audit and before its own loop: `cannibalism_check_spread_target_state_availability` 10805 (it also restores the request's route and scopes), `cannibalism_rebuild_spread_pending_ledgers` 10885, `cannibalism_process_spread_queue` 11455, `cannibalism_compact_spread_queue` 11488, `cannibalism_find_expected_spread_row_for_screening` 11919 (it also restores the requested ID), `cannibalism_invalidate_spread_entries_for_current_country_lifecycle` 12137, `cannibalism_invalidate_spread_entries_for_current_state_lifecycle` 12191, `cannibalism_reconcile_current_state_spread_lifecycle` 12245 and `cannibalism_migrate_spread_entries_between_countries` 12316. No loop in the Event 014 effects calls a helper that writes its own loop counter, and no static path leads from `cannibalism_resolve_loaded_spread_entry` back to the audit.
- Inputs restored or reloaded on purpose: `cannibalism_enqueue_spread_entry` 10967 (`cannibalism_spread_route` is the caller's input, restored by the availability check before the route parameters read it) and `cannibalism_finalize_loaded_spread_entry` 11384 (`cannibalism_expected_spread_id` is the caller's input; the reload is compared with the saved request ID).
- Outer-frame accumulator: `cannibalism_scenario_setup_discipline_collapse` 10214, `cannibalism_scenario_setup_ritual_cells` 10230 and `cannibalism_scenario_setup_silent_islands` 10282 read `cannibalism_scenario_setup_failed`, which `trigger_cannibalism_scenario` and `cannibalism_setup_prefire_evolution_iii_opening` own at zero before any setup helper runs; the helpers only raise it.

MCP evidence for this round: `hoi4.source_lookup` resolved `cannibalism_warlord_march_raid_target_is_valid` with its one decision reference (revision 5591ebee). `hoi4.event_inspect` lint on `chaosx.nr14.82` and `hoi4.decision_inspect` inspect on `cannibalism_march_raid_supply_depot` both returned "Invalid tool arguments" for a plain ID selector, so the event and decision were reviewed in source only.

## R2 review. Skeptical review of the round 2 commits

Disposition: `implemented` (review fixes are tooltip wording only; no gameplay, tuning or AI change).

Basis: skeptical review of 3954dd278, e5c3bb072, abacbd845, a49dc6df5 and 364d07446 against the installed documentation (`triggers_documentation.md` `any_province_building_level`, the wiki `Effects` entry for `add_building_construction`, which accepts a variable `level` and the `limit_to_*` province filters) and vanilla precedents (`common/decisions/SWE.txt` raid check, `afghanistan.txt`, `finland.txt` and `abdacom_shared_branch.txt` province filters).

Findings:

- Every `constant:` reference added by the four gameplay commits resolves in `common/script_constants/`, braces balance in every touched Event 014 file, no Event 014 bunker or naval base construction lacks a province block, and no Event 014 file still uses `non_damaged_building_level`.
- No caller-owned default added by abacbd845 is read by its helper, or by a helper it calls, before the helper writes it, so the defaults cannot change any helper input. `apply_exact_state_civilian_population_loss` sets `chaos_deaths_record_state_ledger` itself before registering deaths, so the zero default before it is inert.
- No static call path leads from `cannibalism_resolve_loaded_spread_entry`, `cannibalism_finalize_loaded_spread_entry` or `cannibalism_load_spread_entry_context` back to `cannibalism_validate_spread_queue`, so the queue audit cannot overwrite the processing loop's cursor. Requiring all four request scopes in the availability check matches `cannibalism_spread_context_is_valid`, which the enqueue already required.
- The Island Host port tooltip named only a landlocked capital, while the effect also moves the port work when the capital is not owned and controlled. It now names both cases.
- The Wendigo "Raise the First Anchors" tooltip omitted the last fortification fallback for an anchor state with neither a victory point nor a border province. It now names it.
- The hoard review line for a cache state the host does not own read "is not our state"; it now reads "We do not own <state>".

MCP evidence: `hoi4.decision_inspect` in `inventory` mode with an `id` returned a revision-pinned whole-mod inventory (source revision 060436ef), which does not isolate one decision; `inspect` mode with only an `id` and `hoi4.event_inspect` `lint` with object selectors (`id`, `kind`/`id`, `kind`/`value`, `eventIds`) returned "Invalid tool arguments". The selector format is documented only in the server's own `docs/events.md`, which is not exposed, so the event and the decision were reviewed in source.
