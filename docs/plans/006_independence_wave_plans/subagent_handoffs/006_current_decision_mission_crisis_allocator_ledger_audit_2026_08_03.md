# Event 006 current decision, mission, crisis, allocator, and Ledger audit

Date: 2026-08-03.

Scope: read-only audit of the current shared Event 006 decision and mission surface, the pre-wave crisis, SCN-008 allocator and belligerence rules, current overlay-watch repairs, focus gates, costs, AI declarations, cleanup, localisation, and the Statehood Ledger.

Disposition: HOLD / PARTIAL for Event 006 as a whole.

The frozen core is source-closed by the current static evidence, but the whole event remains HOLD / PARTIAL because package admission and capacity, formables, final AI and balance acceptance, runtime behavior, save/load, and live UI evidence are still open.

The obsolete pasted flag-log was excluded from this audit and was not used as evidence.

No gameplay, localisation, GUI, asset, focus, or spreadsheet file was changed by this audit.

## Authority, method, and bounded evidence

The accepted source is the seven-part Event 006 specification under docs/specs/006_independence_wave_specs and its matrices.

Current implementation disposition is controlled by 006_source_of_truth_map.md and 006_event6_current_completion_evidence_v106_2026_08_03.md.

The current completion evidence records the frozen allocator, synchronized transaction, crisis queue, dynamic ledgers, five evolution incidents, shared focus tree, decision and mission map, SCN-008 matrix, and Statehood Ledger semantic matrix as source-closed core surfaces.

The current completion evidence also records fourteen attested non-overlay packages, thirteen compatible reservation groups, and no admitted fourteen- or twenty-package witness.

The audit applied the hoi4-decisions-missions, chaos-redux-events, hoi4-focus-trees, and chaos-redux-subagents skills.

The required offline Paradox wiki pages and the additional National focus and scripted-GUI references were consulted together with the vanilla SOV decision, paranoia GUI, and focus precedents and relevant vanilla documentation.

The static audit reran on the current worktree with:

- python -B .tools/audit_event6_allocator.py
- python -B .tools/audit_event6_scenario_matrix.py
- python -B .tools/audit_event6_gui_matrix.py

All three commands passed.

The allocator receipt reports 149 publishers, 126 automatic or high-chaos selectable packages, 138 SCN-008-ranked packages, fourteen attested packages, thirteen compatible reservation groups, the documented two-slot RHI/AJX exception, and the 6 / 8 / 10 / 14 / 20 ladder with World Collapse at 20.

The scenario receipt passes all 32 SCN-008 mode-and-intensity cells and eight static edge cases.

The Ledger receipt passes five mutually exclusive tabs, five recognition frames, three dependency frames, four League frames, four formable frames, generation cleanup for four frame variables plus the animation flag, and four static or animated sibling pairs.

Read-only probability inspection of common/decisions/006_independence_wave_decisions.txt returned PROBABILITY_SOURCE_INSPECTED with zero unresolved diagnostics for ten decision candidates and fifty-four mission candidates.

The candidate pools remain intentionally incomplete because their valid country, target, route, resource, and world-state inputs are runtime-dependent.

Current core decision artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/009f4468970fc3c21f4068f31c8af5088bc0ac875b106c9039e3baa22603bd6a/fdbd0b85edc59e0f78fe3261d735c897a3ce1adde05f5d228bf6b0d5c54a3768/probability-inspect-153fd7ea18e5.json.

Current core mission artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9594b74fc9deffe12e725616989a0bbbfe35128663b39f1b45c73253e5d1c14/0a05f4cb4911d33b86d005bfa4786fb461696fd0e518ece877f501370a5b164f/probability-inspect-153fd7ea18e5.json.

The matching SCN-008 decision inspection also returned zero unresolved diagnostics for three non-reward ledger controls.

SCN-008 artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7afd72f28aaa25f23dcdf1e7231317fa98a5dfbef2825121818da8725128163d/ec4613dfca4464be0c84d22c4ec50926f0874f9a9225a921118cbc4d0d2babc4/probability-inspect-fcd8a24fbe89.json.

## Issues, sorted by severity

### P2 — permanent carrier-identity loss can indefinitely preserve an interrupted overlay watch

Affected identifiers are independence_wave_iw022_hold_adriatic_watch, independence_wave_iw025_hold_vojvodina_border_watch, and independence_wave_iw035_hold_livonian_corridor_watch.

The paid mobilisation decisions added for IW-022, IW-025, and IW-035 correctly activate their formerly inactive watch missions and make the settlement route reachable.

On a temporary route loss, each overlay suspension marks the watch interrupted and extends the active mission by one day on each carrier-specific daily hook.

On a permanent carrier-identity loss, the same pause remains active indefinitely because the failure effect is gated by the active overlay identity and therefore cannot clear the running and interrupted mission flags while the carrier remains inactive.

This creates a stale mission and state path rather than a repeatable reward or free-resource exploit.

The current source map and the IW-022 overlay audit already classify permanent route-loss cleanup as a design HOLD, so no local gameplay patch is appropriate without an owner decision.

The owner must choose and document one policy: permanent pause, a bounded suspension grace period, or immediate cancellation with explicit flag and ledger cleanup.

Any implementation must preserve the accepted temporary interruption and resumption behavior.

Relevant files are common/scripted_effects/006_independence_wave_iw022_dalmatia_effects.txt, common/scripted_effects/006_independence_wave_iw025_vojvodina_effects.txt, common/scripted_effects/006_independence_wave_iw035_livonia_effects.txt, and their carrier-specific on-action hooks.

### P3 — COG overlay custom-cost localisation duplicates live tuning values

The four shared COG cost families are mechanically centralized in common/script_constants/006_independence_wave_iw101_iw102_iw105_cog_overlays_constants.txt and consumed by matching affordability triggers and payment effects.

The corresponding base, blocked, and tooltip text for independence_wave_iw_cog_cabinet_cost, independence_wave_iw_cog_depot_cost, independence_wave_iw_cog_force_cost, and independence_wave_iw_cog_charter_cost repeats literal values such as 12, 1,500, and 3 in localisation/english/006_independence_wave_iw101_iw102_iw105_cog_overlays_l_english.yml.

The values match the current constants, so this audit found no player-facing mismatch.

They are still a narrow tuning-drift risk because changing a constant will not update the displayed amount.

Recommended local fix: replace the twelve literal cost expressions with the existing constant references while preserving the present text and icon order.

### P3 — AI, persistence, and live presentation are still evidence limits

Static sources prove candidate discovery, zero parser diagnostics, route and target guards, and declared AI weights.

They do not prove campaign selection rate, target choice, queue timing across save/load, carrier loss timing, or interactive GUI behavior.

This is a completion-evidence limitation rather than a source defect in the frozen core.

## Decision category lifecycle notes

| Family | Reveal and owner | Retirement and cleanup | Current result |
| --- | --- | --- | --- |
| Pre-wave crisis | A current host with failing stability or either accepted high-resistance occupation condition sees the crisis category, and the timed mission remains visible while active. | Cancellation, allocator rejection, bounded retry exhaustion, malformed callback, and requester annexation write a resolution and clear request state. | PASS at source. |
| Core statehood, recognition, security, former-host, patron, Network, League, and formable actions | Release origin, route, capability, target, membership, map, and focus gates govern visibility and availability. | Action-specific cancel and remove paths protect invalid targets, lost origins, membership loss, treaty completion, and route locks. | PASS at source within the shared core. |
| Evolution incidents | Each of the five stage-gated decisions requires its active evolution and no prior branch resolution. | The pending flag is set before the timed decision ends, cleared by the event outcome, and cleared on origin loss. | PASS at source. |
| Rival Bloc | Invitation, membership, host-front, patron-pressure, and leadership-candidate gates own the action surface. | Invitation and member helpers remove active missions, local variables, arrays, member records, and global event targets on expiry, invalidation, exit, or dissolution. | PASS at source. |
| SCN-008 ledger | A frozen rejection ledger owns three zero-reward navigation controls only. | Closing removes the display flag, while reset and freeze helpers clear target marks, policy state, arrays, and cursors between launches. | PASS at source. |
| IW-022, IW-025, and IW-035 watches | A route-active carrier exposes the paid mobilisation action after its preparatory action. | Normal success, failure, cancellation, timeout, and temporary suspension are explicit. | PARTIAL because permanent identity loss has no accepted cleanup policy. |

The current scan finds sixty direct days_mission_timeout declarations across the Event 006 decision files.

The active core mission paths reviewed here have available, timeout, and cancellation or invalidation behavior.

The three former inert rival-bloc mission-visible fields are absent from the current mission declarations, and the remaining visible clauses in that file belong to ordinary decisions rather than timed missions.

## Mission quality notes

| Mission family | Owner, category, and region | Requirement and duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| Pre-wave crisis | Current host, crisis category, host territory under severe stability or resistance pressure. | Concrete security commitment, active pressure, open coordinator barrier, then the centralized 120-day mission and bounded retry. | A surviving pressure queues the ordinary synchronized allocator, while cancellation, failed planning, retry exhaustion, requester loss, or malformed callback records an explicit result and clears queue state. | Low at source because one global queue serializes requests and on_annex clears a lost requester. |
| Evolution incident actions | Active Event 006 release, Evolution Incident category, global evolution stage. | One paid stage-gated action per evolution with standard, extended, or strategic central duration. | The remove effect opens an event with two branch outcomes, and the pending marker is removed by resolution or origin loss. | Low because pending and resolved branch flags prevent duplicate branch completion. |
| Rival Bloc invitation, reserve, and leadership | Invited or member country, Rival Bloc categories, cross-country contract scope. | Valid recipient, membership, candidate, host, or patron condition plus centralized resource gates and durations. | Expiry, membership loss, recipient invalidation, and contract dissolution call the local and global cleanup helpers. | Low because the pending target, invitation deadline, member arrays, and active-mission gates are cleared or revalidated. |
| DM-58 reclamation front | League coordinator and registered members in valid border regions. | Valid coordinator, persisted witness membership, minimum member count, unique external objectives, and material payment before the finite operation. | Completion executes the staged front, while witness loss, no valid preflight, or timeout rolls back and opens the declared League crisis path. | Low in source because revalidation cancels on stored-witness loss and cleanup clears coordinator, participant, state, and operation data. |
| Formable deadline objectives | Formable carrier or created formable country, its regional category, route-specific objective region. | Explicit focus, route, capability, material, and deadline guards. | The named route resolution or failure effect closes the objective and prevents repeated reward. | Low because deadline objects are not repeatable selectable reward actions. |
| Dalmatia, Vojvodina, and Livonia watches | Respectively CRO-origin Dalmatia, HUN-origin Vojvodina, and LIT Livonia carrier overlays. | Carrier identity, anchor control, prior action, concrete guard payment, garrison objective, and centralized timeout. | Success sets the settlement-opening receipt, while normal cancellation or timeout calls the watch failure path. | Low during an active or temporary-interruption route, but permanent route loss is the P2 stale-state HOLD above. |

## Cost and requirement clarity

The current scan finds 137 unique custom_cost_text keys in Event 006 decision files.

Every one has a base, _blocked, and _tooltip localisation entry in the Event 006 English localisation surface.

The verification includes the paid overlay-watch mobilisation actions introduced on 2026-08-03.

The core uses varied resource commitments rather than a passive political-power store: manpower, Army Experience, Command Power, infantry and support equipment, trains, convoys, fuel, stability, war support, civilian capacity, map control, garrison presence, legitimacy, capacity, membership, and route state.

The pre-wave crisis consumes manpower, Army Experience, Command Power, infantry equipment, support equipment, and a stability change before the mission begins.

Its available and custom-cost trigger share the same engine-backed affordability helper.

The Rival Bloc leadership gate uses has_army_experience rather than a variable read and shares that helper between availability and custom cost.

The current decision-file scan found no direct negative add_political_power payment and no decision-file create_unit reward.

The existing DM-22 emergency force exception remains bounded by its major material payment, fire-only-once state, raised-period cleanup, and professionalisation or origin cleanup according to the current decision audit authority.

No passive political-power store, free-unit loop, equipment-farming loop, core-spam loop, or war-goal-spam loop was found in the audited current source.

## AI validity, focus integration, and route locks

The accepted AI matrix gives distinct survival, viable, armed, host, patron, League, radical, and scenario profiles, and current action blocks use guarded AI weights rather than unconditional target actions.

The crisis AI raises its score only for relevant stability or occupation pressure.

The repaired overlay mobilisation actions disable AI where no qualifying garrison exists and retain their documented peacetime modifier.

Rival Bloc invitations require a live compatible target from the Network array, membership actions revalidate their member records, and leadership requires a current eligible candidate and available Army Experience.

The current v104 static receipt resolves all 27 decision has_completed_focus gates against the Event 006 focus surface.

The 319 Event 006 focus IDs in the four shared and regional source files remain the relevant reference set for those gates.

No current dangling focus gate was identified in the audited decision surface.

SCN-008 Universal Belligerence: Former Hosts now sets a temporary unique-host policy before dispatch, marks and records a host before declaration, removes the mark after a failed declaration, and clears target marks plus the policy at reset, dispatch completion, and launch completion.

Ordinary Wars of Separation explicitly clears that policy and retains the intended same-former-host separation-war behavior.

This resolves the former-host collision without manufacturing a new war path.

## Localisation, tooltip, and Ledger notes

The current crisis category text states all three eligibility paths and its description exposes the paid mission, cancellation, blocked retry, cooldown, and ownership consequences.

Crisis history now records the initiating host and cause before runtime flags are cleared, records resolution history, and refreshes the shared Event Log view.

The Statehood Ledger is presentation-only.

Its buttons change a local tab, toggle the animation flag, or refresh current frame state, while normal decisions and missions remain the action layer.

The current source maps precise recognition, dependency, League, and formable frame groups and clears frame variables plus all tab and animation state during generation reset.

Current targeted GUI inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fffc8e5ca0679dbc851d6d2072c89aea20aa942af351617e4290db2c06d99791/468b5e5c5e2459ce505f52e12c87619635090098779be4501174108ca37dbb1f/gui-inspect.abdf359582c5b7a7.json.

Current offline render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8af67bf8c35fb7c1dd61be592b2777e5d34225021bdf7a04d7b052c0accb5682/87fbe8c92c4c68655d05929255fdf0fc33e0839a7fc455a9b7d523984e330626/independence_wave_status_window-full.png.

The current render covers the named Ledger window with normal, hover, warning, and long-text representations at 1920x1080 and 1280x720.

The render is an offline representation, not a game-session validation.

The MCP aggregate reports 498 modelled, six approximated, sixty-five ignored, one missing, four unsupported, and twelve unresolved GUI-source paths.

It also reports repository-wide GUI diagnostics and visible overlaps that cannot be attributed to Event 006 from the bounded result, so this audit makes no global GUI-clean claim.

Live click behavior, frame persistence, semantic state transitions, animation playback, and save/load remain unresolved evidence limits.

## Cleanup and exploit-risk notes

The crisis callback clears its global queue before planner dispatch and handles successful commit, blocked allocation, bounded retry exhaustion, missing requester state, and on-annex requester loss.

The current source has both durable crisis receipt flags and Event Log history writers, closing the historical missing-receipt and missing-cause presentation findings.

The allocator fails closed on insufficient capacity and exact-count mismatch instead of releasing a partial 14- or 20-country wave.

The SCN-008 rejection ledger has zero reward and zero AI weight, so its navigation controls are not an economic or repeated-action exploit.

The only unresolved cleanup risk found in current decision-owned mechanics is the overlay permanent-identity-loss policy described at P2.

## Recommended fixes and handoff

1. Parent or feature owner decision required: record a permanent carrier-identity-loss policy for the IW-022, IW-025, and IW-035 watch missions before a narrow cleanup patch is written.

2. Narrow localisation maintenance patch recommended: change the literal COG cost values in localisation/english/006_independence_wave_iw101_iw102_iw105_cog_overlays_l_english.yml to existing script-constant substitutions.

3. Retain the current fail-closed capacity rule for the 14- and 20-country bands until content admission and compatible reservation evidence exist.

4. Retain the current whole-event HOLD / PARTIAL status until declared AI and balance scenarios, live mission and queue behavior, save/load, UI interaction, package admission, formable readiness, source-rights, and other parent-owned completion gates are closed.

No new plan handoff was written because the only P2 issue is an already-recorded design policy choice and the P3 localisation work is a narrow local patch.

## Changed files and validation boundary

Changed file: this handoff only.

Changed decision, mission, scripted-GUI, and localisation identifiers: none.

Before and after behavior: unchanged because this audit is read-only.

Meaningful validation passed: allocator, SCN-008 matrix, Ledger semantic matrix, current probability source inspection, custom-cost triplet scan, and targeted GUI inspect or render artifact generation.

Skipped meaningful validation: no Hearts of Iron IV launch, runtime event triggering, actual AI campaign simulation, live recipient or carrier loss, save/load, or player-owned GUI interaction was performed.

No fallback or silent simplification was introduced by this audit.
