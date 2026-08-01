# Event 020 live-wiring completion audit handoff

Date: 2026-08-01

> Historical audit snapshot. The later 2026-08-01 content tranche statically wires the RTA hierarchy consumers, RTX crises `.57-.59`, Crown Strike `.64-.65`, scoped defeat/aftermath `.71-.75`, resolver-owned `.72`, and slot-087 presentation; this report’s older “absent” wording for those surfaces is superseded. Retain its valid unresolved findings for evolution/scenario/`.73` audience/asset validation and whole-spec completion, and use `2026-08-01_event20_documentation_cleanup_handoff.md` as the current documentation disposition.

## Reconciliation update (2026-08-01)

The relaunch-safety pass supersedes the older evolution and scenario findings wherever the live source now proves a repair. The current runtime advances at most one ordinary evolution per due pulse, captures Evolution II on the first verified overseas exposure, records Evolutions IV and V against `RTX`, refuses to record Evolution IV without a living King, preserves already seeded scenario state ledgers, and exposes a repeat signal as a reconciliation-only transaction. The historical findings below remain useful only where they are explicitly marked as still open or were not covered by that pass.

The following parent-owned surfaces are now promoted as static implementation evidence and supersede the corresponding absence claims below:

| Surface | Evidence |
| --- | --- |
| Scoped defeat actor hooks and participant registry | `common/on_actions/020_black_plague_on_actions.txt` and `common/scripted_effects/020_black_plague_rat_effects.txt` record narrow capitulation/state-control participants and deduplicate major human contributors. |
| Duration/peak/deaths/participant qualification | `common/scripted_triggers/020_black_plague_rat_triggers.txt`, `common/script_constants/020_black_plague_constants.txt`, `common/script_constants/020_black_plague_evolution_constants.txt`, and Rat/evolution runtime effects track the current explicit gate. |
| Reconstruction coupling | `black_plague_rat_king_resolve_defeat` dispatches `.72` once after `.71` when the same gate qualifies; `.73-.75` remain the separate aftermath path. |
| Slot 087 package | `interface/020_black_plague_super_events.gfx`, `localisation/english/020_black_plague_super_events_l_english.yml`, `sound/chaosx_sound.asset`, `music/chaosx_music_track_list.html`, and the final art/audio/text handoffs promote the image, text, audio ID 103, and wrappers. |

These updates do not claim whole-spec completion, native mission API acceptance, correct `.73` actor audience (the current fallback is the first eligible human response host), release rights completion, or live in-game validation.

## Boundary and verdict

Event 020 is **partial and not whole-spec complete** in the audited working-tree snapshot.

This is a read-only completion audit of live event dispatch, evolution logging and pacing, SCN-012 bootstrap behavior, shared disease decisions, the contamination mapmode, countermeasure and Doctor Wu integration, weaponization, Rat Nation and Rat King runtime hooks, asset references, and current documentation and catalog evidence.

The controlling correction is `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md`.

`RTA` is the sole reusable Rat Nation carrier, internal broods are state-level state inside `RTA`, and `RTX` is the separate Rat King.

No 3D model, mesh, rig, skeletal action, or `.anim` package is required by the current user instruction, so model absence is not a blocker in this audit.

The working tree changed during the audit.

The evidence below was rechecked after the current evolution-setting, evolution-date, SCN-012 scheduler, active-state preservation, mapmode-visibility, and zero-state Rat King defeat patches appeared in the working tree.

## Completion status by surface

| Surface | Status | Current evidence and limitation |
| --- | --- | --- |
| Canonical entry and natural scheduler | Finished statically | `events/020_black_death.txt:15-71` defines the hidden entry and state-owned callbacks `.900` through `.903`. `common/scripted_effects/020_black_plague_effects.txt:1725-1755` saves the origin, controller, and scheduler anchor and schedules the first callback. The entry has an upstream caller in `events/070_africa_gods.txt`. |
| SCN-012 scheduler continuation | Finished statically, live validation pending | `black_plague_scenario_start_scheduler` selects a scenario anchor when one exists and otherwise retains a scheduler through an established-state fallback. The triggerable launch now has a reconciliation branch that rebuilds runtime counts, air cleanliness, shared threat, mapmode, and the disease board without reseeding, firing another report, or changing intensity state. Save/reload and live consumer behavior remain unproven. |
| Player-facing event identifier coverage | Finished for mapped identifiers, partial for presentation | `events/020_black_death.txt` now defines the accepted `.2` through `.72` milestone allocation, `.90`, and the scheduler callbacks. `.42` is correctly absent under the two-tag correction. Three weaponization reports exist in `events/020_black_plague_weaponization.txt`. A repository caller scan found at least one non-definition reference for every defined Event 020 ID. |
| Event audience and event-picture type | Partial | Local and selective reports such as `.2` through `.8`, `.21`, `.41`, `.43`, `.44`, and `.72` are not consistently country-scoped. Most are `news_event` definitions in `events/020_black_death.txt:75-415`, which broadcasts milestones that the event-chain matrix assigns to an origin owner, exposed neighbor, affected state owner, reusable RTA carrier, or leading recovery actor. Most news events also use 210 by 176 report-card sprites instead of 397 by 153 news sprites. |
| Evolution detail and ordinary log plumbing | Finished statically, runtime validation pending | `black_plague_evolution_record_stage` writes through the shared evolution logger, and Event Details registers five previews. The five active flags, per-stage setting gates, report dispatches, due-date gate, one-stage-per-pulse `else_if` chain, verified destination actor capture, RTX ownership, and King-success guard are wired. Dynamic settings comparisons and natural save/live validation remain unperformed. |
| Evolution settings gate | Finished statically after the current repair | `common/scripted_triggers/020_black_plague_evolution_triggers.txt:26-56` checks the shared per-stage flags `events_log_disabled_evolution_20_20_1` through `_5`; those names match the shared settings meta-effect pattern in `common/scripted_effects/chaosx_events_log_effects.txt:2626-2632` and existing Event 15, 16, and 18 precedents. The readiness and activation effects both consume the stage-specific gates, while the scoped SCN-012 bootstrap explicitly bypasses I through IV only. Disabled and enabled runtime comparisons remain unperformed. |
| Evolution dynamic pacing | Finished statically, runtime validation pending | `black_plague_evolution_check_is_due` consumes `global.black_plague_rat_next_evolution_check_date`, and `black_plague_evolution_runtime_pulse` uses an ordered `else_if` chain so only the next eligible stage can activate before the next MTTH-backed date is scheduled. A failed King transaction does not consume Evolution IV. Disabled/enabled comparisons and natural timing remain unperformed. |
| Evolution actor ownership | Finished statically, runtime validation pending | Evolution II captures the first state whose applied exposure uses the overseas-port route and saves its human controller; Evolution III selects the first active RTA carrier; Evolution IV records only after a valid RTX King exists; and Evolution V explicitly saves RTX before logging. Natural actor ordering still needs a live scenario proof. |
| Evolution IV activation transaction | Finished statically, runtime validation pending | `black_plague_rat_activate_evolution_iv` first selects/transfers a valid Royal Basin, then sets IV active/recorded only when `black_plague_rat_king_active` is true and saves the RTX actor. A failed transfer sets the retry flag without consuming the evolution row. |
| Evolution V and world-end order | Finished statically, runtime validation pending | `black_plague_activate_evolution_v` records V, opens the terminal route, and does not set `world_end`. `black_plague_evolution_v_perform_terminal_takeover` has a separate execution trigger requiring the completed route plus the live death, Chaos, conquest, continent, capital, refuge, and King gates. SCN-012 never invokes either V path. |
| SCN-012 two-tag bootstrap | Partial, with substantial finished wiring | `common/scripted_effects/020_black_plague_scenario_effects.txt` registers four intensity profiles, several eligible continents, established states, threatened outer rings, one RTA carrier, two to six internal RTA brood states, a separate RTX Royal Basin, grace-period coexistence, starting forces, Evolutions I through IV, one mapmode rebuild, one scenario report, cleanup, and a repeat-launch block. The launch does not set Evolution V or `world_end`. |
| SCN-012 active-crisis preservation and atomicity | Substantially repaired, live validation pending | Existing established states are excluded from reseeding and their disease ledgers are preserved by `black_plague_scenario_seed_state`. Existing RTX meters are only initialized when absent, and `black_plague_scenario_assign_king_army` tops up missing divisions instead of duplicating the floor. The launch permanent flag and report are written only after the postcondition block passes; a failed setup clears reservations and the scoped bootstrap. A later UI signal reconciles an already-launched crisis without reseeding or firing another report. Full rollback/save-reload behavior remains unproven. |
| Shared disease category ownership | Finished structurally | `common/decisions/categories/biowarfare_disease_containment_categories.txt:3-17` remains the single human disease category owner. Event 020 response, shared-response, and weaponization decisions extend `chaosx_disease_containment_category`. No duplicate human Black Plague category was found. Rat-only decision categories remain separate nonhuman surfaces. |
| Shared decisions and mission | Finished structurally, validation missing | The selected-state and country actions cover prepared, exposed, infected, recovery, knowledge, anti-rat, Royal Node, and Doctor Wu surfaces. `black_plague_shared_emergency_countermeasure_drive` at `common/decisions/020_black_plague_shared_response_decisions.txt:9-48` is a selectable 90-day mission with payment, completion, timeout, cancellation, AI, and `.56` timeout report. Royal Node resolution at `common/scripted_effects/020_black_plague_shared_response_effects.txt:300-337` now branches between Dominion and pulse reduction and counterfire pressure. Runtime success, timeout, cancellation, target-loss, and repeat-use behavior has not been validated. |
| Mandatory black mapmode | Finished statically after the current privacy repair | `common/map_modes/chaosx_state_map_modes.txt:203-296` provides phase borders and a pure black established-state base. The base now requires both `black_plague_state_is_established` and `black_plague_state_is_visible_to_mapmode_player` at lines 213-221, matching the existing border and tooltip privacy boundary. The black constants remain zero-red, zero-green, zero-blue, full-alpha. Owner, controller, ally, neutral, and enemy viewer scenarios remain unvalidated. |
| Countermeasure progress | Finished for the accepted core | `black_plague_change_countermeasure_progress` in `common/scripted_effects/020_black_plague_response_effects.txt` initializes, changes, clamps, and records the 0 to 100 program. Weekly treatment, spread, mortality, and cleanup modifiers consume it. Full progress does not erase active disease and local cleanup remains necessary. |
| Doctor Wu bridge | Finished for the accepted core | Event 163 host commitment calls `black_plague_on_doctor_wu_host_committed` at `common/scripted_effects/163_doctor_wu_effects.txt:108-120`. Natural Event 020 startup applies the inverse late-start bridge at `common/scripted_effects/020_black_plague_effects.txt:1747-1750`. The protocol adds ordinary progress and state treatment rather than globally curing the plague. |
| Weaponization | Finished structurally, presentation and balance partial | `common/special_projects/projects/020_black_plague_weaponization_projects.txt` defines six prototype reward ranges and eighteen unique role tokens. `common/decisions/020_black_plague_weaponization_decisions.txt` defines four mutually exclusive approaches and native payload delivery. `common/scripted_effects/020_black_plague_weaponization_effects.txt` connects accidents, condemnation, stockpile, plague-bomb technology, ordinary exposure, delivery, and three reports. No representative accident, condemnation, delivery, or AI scenario has been evaluated. Resource costs and several AI factors remain literal rather than centralized tuning values. |
| Exactly two rat countries and internal broods | Finished structurally | `common/country_tags/020_black_plague_rat_countries.txt:8-11` registers only `RTA` and `RTX`. SCN-012 creates one reusable RTA carrier and uses state brood markers for its intensity scaling at `common/scripted_effects/020_black_plague_scenario_effects.txt:264-331`. RTX is created in a separate Royal Basin and RTA remains active during the grace period. |
| Rat runtime pulses | Partial | The weekly disease pulse calls `black_plague_rat_run_runtime_pulse` at `common/scripted_effects/020_black_plague_effects.txt:1646-1648`. RTA and RTX initialization, zero-manpower and equipment-independent units, capped growth, internal brood absorption, King absorption, Royal Node pulse blocks, AI strategies, and defeat detection are present. Clean newly conquered rat-controlled states have no explicit control-change hook and are converted only after entering the tracked established disease state, so the accepted reliable rat-occupation infection behavior still lacks direct proof. |
| Rat King defeat and aftermath | Scoped static tranche implemented; playable depth and validation partial | `common/on_actions/020_black_plague_on_actions.txt` and `common/scripted_effects/020_black_plague_rat_effects.txt` now record scoped participants, track duration/peak metrics, and resolve `.71`, eligible `.72`, gated slot 087, and `.73-.75` idempotently while preserving RTA and surviving plague states. `.73` still targets the first eligible human response host rather than the saved actor, Royal Node cleanup remains a separate `.74/.75` action, broader aftermath depth is compact, and live validation is absent. |
| RTA and RTX focus and AI depth | Partial | The current snapshot contains 35 RTA focuses with 13 explicit `ai_will_do` blocks and 50 RTX focuses with 8 explicit `ai_will_do` blocks. The four RTA origin lanes now have continuing route-module effects and route-aware AI strategies exist, so older no-AI and 31-focus findings are stale. The accepted ranges remain approximately 40 to 50 RTA focuses and 70 to 100 RTX focuses, and the broader hierarchy, administration, captured-knowledge, population-policy, continental-campaign, and aftermath lanes remain compressed or absent. |
| Achievements | Implemented structurally, runtime validation missing | Fourteen Event 020 achievement entries now exist in `common/achievements/chaos_redux_achievements.txt:3775-3847`, their localisation exists, and `interface/chaosx_achievements.gfx:1519-1560` registers 42 completed, grey, and not-eligible sprites. All 42 DDS files exist. The current content tranche corrected the previously impossible two-tag predicates, but no positive and disqualifying campaign scenarios have validated the achievement contracts. |
| Catalog | Finished for current public wording | The exported Event row records cluster 8, Severe membership, five evolution texts, and `The Kingdom of Teeth`. The Clusters export contains Diseases ID 8 with member 20. The Scenarios export contains SCN-012 with the corrected RTA and RTX wording. All three rows remain `Needs Testing`, which matches the missing runtime validation. |
| 3D model package | Out of scope | The current no-model correction controls this audit. Existing infantry-entity visuals are not treated as a missing Event 020 runtime input. |

## Historical blocker list and current residuals

The first four entries below are historical findings from the pre-relaunch-safety snapshot. The current source now repairs those specific issues: the due chain is one-stage-per-pulse, evolution actors are verified, Evolution IV is King-gated, Evolution V is an unlock separate from terminal execution, and SCN-012 preserves seeded ledgers and reconciles repeat signals. Current residuals are full rollback proof, live validation, presentation/audience cleanup, and broader aftermath depth.

### 1. A due evolution check can still cascade several stages

The current patch correctly honors the five shared per-stage disable flags and correctly waits for `global.black_plague_rat_next_evolution_check_date`.

It does not isolate the next unrecorded stage.

The due block checks I, II, III, and IV in sequence, and each successful activation can satisfy the next check during the same effect chain before a new date is scheduled.

This is a direct pacing failure against the accepted evolution matrix, not a balance-only concern.

### 2. Evolution actors and the Rat King activation transaction are incorrect

Evolution II does not own the first overseas destination.

Evolution IV records the source RTA rather than RTX and can record even when Royal Basin transfer fails.

Evolution V does not reliably own RTX.

The evolution log can therefore contain valid rows with wrong or nonexistent milestone actors.

### 3. Evolution V collapses the accepted two-gate campaign into one terminal effect

The accepted main spec makes Evolution V an unlock for the final route, readiness panel, target selection, and human response window.

The live trigger instead requires the already completed route and continent condition, then the activation immediately performs terminal takeover.

This removes the accepted near-success counterplay and reverses the focus-path dependency.

### 4. SCN-012 preserves established disease states but is not an atomic active-crisis upgrade

The current patch counts established states and excludes them from anchor and top-up pools, so their disease phase and ledgers are no longer overwritten.

An existing RTX is still reset to the scenario's royal meter values and receives a new guard package unconditionally.

The permanent launched flag is written before King creation and scheduler replacement are proved, while Evolution IV itself can record before the Royal Basin transfer succeeds.

The scheduler helper also clears the prior anchor before proving that a new unestablished scenario anchor exists.

These paths can leave a partially committed one-shot scenario or downgrade and duplicate an existing King package.

### 5. Rat King defeat cleanup and the scoped aftermath tranche are present, but whole-spec aftermath remains partial

Zero-state RTX defeat now clears active royal runtime, retires the King carrier, removes its active registry entry, and produces `.71` once.

Scoped participant capture, peak/duration qualification, resolver-owned reconstruction dispatch, and slot-087 presentation are now present. Remaining gaps are the `.73` audience choice, successor/aftermath depth, Royal Node live proof, release attribution, and whole-spec narrative coverage.

The new `2026-08-01_event20_consequence_and_aftermath_addendum.md` describes a possible next tranche, but it remains under `docs/plans` until accepted and is not implementation evidence.

## Accepted-plan disposition

| Accepted or corrected item | Current disposition |
| --- | --- |
| State disease lifecycle, exact-loss mortality, spread ledger, countermeasure, Doctor Wu, and shared disease category | Implemented for the core, with live balance and save and reload validation missing. |
| Five ordinary evolutions with settings, active and prefire detail, dynamic pacing, exact actors, and separated Evolution V route | Partial. Detail rows, report events, per-stage settings, and due-date scheduling exist, but same-check cascade prevention, actors, IV transaction safety, and V ordering remain unresolved. |
| Exactly one reusable RTA carrier, internal brood state, and separate RTX | Implemented structurally. No extra rat tag is required or permitted. |
| SCN-012 four-intensity bootstrap | Partial. Fresh scheduling, established-state preservation, two-tag countries, internal brood scaling, grace, mapmode refresh, and the no-V boundary are implemented. Existing-RTX preservation, all-or-nothing commit safety, no-anchor scheduler preservation, and task-specific runtime proof remain unresolved. |
| Shared Black Plague-specific decisions inside the general disease category | Implemented structurally. The duplicate-category alternative remains rejected. |
| Weaponization six-phase and eighteen-role project | Implemented structurally. Dedicated delivery art and task-specific accident, AI, and delivery validation remain unresolved. |
| Deep RTA and RTX country routes | Compact playable subsets with route-aware AI, not accepted full depth. |
| Rat King defeat aftermath | Zero-state cleanup, scoped participant/metric tracking, `.71`, eligible `.72`, gated slot 087, and `.73-.75` are implemented statically. `.73` ownership still falls back to the first eligible human response host, broader playable aftermath depth and live proof remain open. |
| Dedicated event and UI asset package | Partial. Three additional report and news assets are now produced and wired, but accepted severe-crisis and Rat Nation news art, dedicated Royal Node and weapon-delivery icons, route icon depth, and source-frame animations remain queued or absent. |
| Extra Rat Nation tags, dedicated human Black Plague category, ordinary human-rat diplomacy, and automatic SCN-012 Evolution V | Rejected or superseded and correctly absent. |
| Rat 3D models | Superseded for the current task by the user no-model instruction and not a blocker. |

## Stale findings in earlier handoffs

`docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_completion_audit.md` is a historical point-in-time audit and is materially stale against the current tree.

- Its claim that most narrative events are absent is stale. The mapped `.2` through `.72` reports and `.90` now exist and have callers.
- Its claim that the mission family is absent is stale. The Emergency Countermeasure Drive is present.
- Its claim that Royal Node only subtracts infestation is stale. The current effect changes Dominion, blocks the King pulse on success, and adds Dominion, Hunger, and terminal pressure on failure.
- Its claim that achievements lack registry, localisation, and assets is stale. Fourteen registry entries and 42 sprite triplets now exist.
- Its focus counts and no-focus-AI claim are stale. The current counts are 35 and 50 with explicit focus weights, continuing RTA route effects, and route AI strategies.
- Its claim that the Diseases cluster and workbook exports are pending is stale. The current CSV exports contain cluster 8, Event 20 membership, world-end text, and SCN-012.
- Its report-art inventory is stale. Origin, overseas, and rat-emergence assets now have final DDS files, sprite registrations, consumers, source evidence, and a handoff.

The older two-tag, focus, decision, country, and localisation handoffs remain useful historical evidence for the patches they owned, but their completion counts and missing-surface lists must not override the current source scan.

The current `2026-08-01_event20_content_tranche_handoff.md` correctly records the latest scheduler, settings, mapmode, state-preservation, and defeat patches, but its statement that evolution checks no longer attempt all eligible stages on the same weekly pulse is too strong: the due-date gate is live, yet one due block still checks all stages in sequence.

## Asset and identifier audit

The live Event 020 runtime has no missing custom GFX identifier among the audited event, response, weaponization, focus, idea, and Rat decision consumers.

A set comparison found 35 custom Event 020 GFX consumers and 35 matching interface definitions.

Every texture path declared by `interface/*020_black_plague*.gfx` exists.

The four wired Event 020 event-picture DDS files have distinct SHA-256 hashes.

The new origin and rat-emergence report cards are 210 by 176, and the overseas news strip is 397 by 153, with source, processed, DDS header, hash, prompt, and contact-sheet evidence in `docs/assets/020_black_plague/event_art/manifest.md`.

The remaining presentation gaps are requirement gaps rather than unresolved IDs:

- `report_event_020_black_plague_severe` and `news_event_020_rat_nations` are still absent from the accepted event-picture inventory.
- Many `news_event` entries reuse 210 by 176 report cards, including the generic unbound image.
- `GFX_decision_black_plague_weapon_delivery` is an alias to the military-acceleration texture in `interface/020_black_plague_weaponization.gfx:6`.
- Strike Royal Node uses `GFX_decision_generic_army_support` at `common/decisions/020_black_plague_shared_response_decisions.txt:597-613` instead of the accepted dedicated icon.
- The animated Rat King portrait and source-frame crisis and readiness animations remain absent. The static portrait is a valid runtime fallback, but it is not the accepted final animation package.
- Super-events 85 and 86 have registered final art and licensed or public-domain 44.1 kHz audio. Defeat slot 087 now has final art, localisation, audio ID 103, sprite registration, and settings wrappers; runtime gating, rights release record, and live playback remain open.

No model asset is missing under the current completion target.

## Documentation gaps

`docs/events/020_black_plague/overview.md` is current for the two-tag architecture, report-art promotion, shared category, countermeasure, Doctor Wu, weaponization, catalog, mapmode privacy, established-state preservation, fresh-launch scheduler, and zero-state King cleanup.

It overstates completion when it describes evolution timing without disclosing the same-check cascade, describes the scenario as idempotent without qualifying existing-RTX resets and partial-commit paths, and calls the current gameplay tranche source-complete despite the actor, IV transaction, Evolution V, audience, aftermath, route-depth, and asset gaps.

`docs/plans/020_black_plague_plans/2026-08-01_event20_content_tranche_handoff.md` correctly says the overall goal is incomplete and discloses compact focus routes and queued assets.

It does not disclose the same-check evolution cascade, actor errors, Evolution IV partial-commit path, Evolution V order, existing-RTX reset, no-anchor scheduler edge, local-report audience broadening, `.73` audience fallback, or the remaining broader aftermath depth.

The event-art producer handoff and manifest still say main-agent GFX and gameplay wiring remains to be done, while the current content handoff and live files show that wiring has already been promoted.

The two-tag correction is authoritative, but several older matrix and prompt rows still contain historical multi-tag wording.

The correction and source-of-truth disposition resolve the conflict for implementation, but the stale rows should be reconciled so later audits do not revive rejected tag-count requirements.

No current Event 020 subagent patch was found without a handoff note.

The fresh parent-owned settings, scenario scheduler, established-state preservation, mapmode privacy, and zero-state defeat repairs are present in the current content handoff, but their static completion boundaries and remaining edge cases should be corrected there before a whole-tranche completion claim.

## Meaningful validation performed

- Traced the natural and SCN-012 scheduler call paths through `.900`, including fresh launch and the current no-new-anchor active-crisis edge.
- Compared all live Event 020 event definitions against direct callers and the accepted event-chain map.
- Traced the five evolution activation, logging, actor, settings, due-date, same-check cascade, and terminal paths.
- Confirmed exactly two registered rat tags and current internal-brood scenario scaling of two, three, four, and six states.
- Compared the scenario transaction against established-state preservation, existing RTA and RTX reuse, permanent-flag commit timing, failed Royal Basin creation, scheduler replacement, repeat launch, no-V, cleanup, grace, and one-mapmode-rebuild requirements.
- Confirmed the single shared disease category owner and the current mission and Royal Node result paths.
- Traced the countermeasure and Doctor Wu bridge in both event-start orders.
- Counted eighteen weaponization role tokens and inspected the approach, accident, stockpile, condemnation, and delivery paths.
- Confirmed the pure black mapmode base and the current viewer-visibility gate.
- Counted 35 RTA and 50 RTX focuses and their 13 and 8 explicit focus-AI blocks.
- Compared custom Event 020 GFX consumers to definitions and tested every Event 020 GFX texture path.
- Verified the four event-picture assets are distinct files and read their source and DDS validation manifests.
- Read the current Event, Cluster, and Scenario CSV rows and confirmed their two-tag and world-end wording.
- Ran a focused read-only HOI4 event inspection from `chaosx.nr20.1`. It returned `status: ok` and `EVENT_INSPECTED_PARTIAL`, but its validation remained false because workspace-wide helper projections and lifecycle passes were deferred. It is evidence of parseable event discovery, not completion proof.

## Meaningful validation still missing

- Disabled-evolution and enabled-evolution comparison under otherwise identical state after the current setting patch.
- Timing proof for every natural evolution; static inspection currently disproves prevention of same-check stage cascades.
- Actor proof for Evolutions II through V in natural and scenario entry paths.
- Evolution IV failure recovery when no Royal Basin is valid.
- The accepted two-gate Evolution V near-success, interruption, target-selection, and final takeover sequence.
- SCN-012 Low, Medium, High, and Maximum fresh-launch validation after the scheduler repair.
- SCN-012 launch over an existing active crisis, including established-state preservation, existing RTA reuse, existing RTX meter and army preservation, internal brood top-up, scheduler replacement, and a no-new-anchor case.
- Repeat launch, save and reload, grace-period coexistence, post-grace RTA absorption, and complete cleanup proof.
- Mapmode privacy checks from owner, controller, ally, neutral, and enemy viewers after the current visibility patch.
- Emergency Countermeasure Drive completion, timeout, cancellation, and target-loss behavior.
- Royal Node success, counterfire, pulse blocking, AI selection, cooldown, and terminal-pressure behavior.
- Weaponization phase progression, accident routing, condemnation escalation, defensive conversion, stockpile accident, and delivery behavior.
- Rat occupation of a clean conquered state, RTA and RTX force-cap behavior, scoped King-defeat participant attribution, `.72`/slot-087 gate behavior, `.73` audience routing, and aftermath outcomes.
- Positive and disqualifying scenarios for all fourteen achievements.
- Representative balance evidence for disease growth, containment costs, four scenario intensities, RTA and RTX force growth, Royal Node counterplay, and terminal readiness.

No Hearts of Iron IV process was launched.

No in-game validation is claimed.

## Recommended next actions

1. Make the due evolution transaction choose at most one next unrecorded stage before scheduling the next MTTH-backed date.
2. Correct actor capture for Evolution II and RTX ownership for IV and V, then make IV recording and reporting conditional on successful King creation.
3. Restore the accepted two-gate Evolution V flow so recording unlocks the final route and terminal takeover remains a later earned transaction.
4. Make SCN-012 preserve an existing RTX through minimum-floor top-ups, create only missing units, delay the permanent launched flag until all required actors and scheduler are proved, and preserve the prior scheduler when no new anchor is available.
5. Replace local and selective `news_event` reports with correctly scoped report events and complete the corresponding event-picture family without cross-type reuse.
6. Resolve whether `.73` should use the saved defeating actor, deepen the accepted Rat King aftermath, and validate the promoted `.72`/slot-087 gate before any whole-spec claim.
7. Run the task-specific validations listed above, then update the overview, content handoff, asset handoff status, and source matrices to match the proven runtime state.

## Completion claim boundary

The Event 020 core contains substantial finished mechanics and no missing custom runtime identifier in the audited asset surfaces.

It cannot be called complete while due evolution checks can cascade several stages, actors are wrong, Evolution IV can record without a King, Evolution V bypasses its accepted unlock phase, SCN-012 can partially commit or reset an existing RTX, local report audiences are broadened, `.73` still falls back from the saved actor, and broader accepted aftermath depth/live validation remain open.
