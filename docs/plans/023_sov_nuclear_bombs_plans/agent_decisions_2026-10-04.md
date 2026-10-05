# Event 23 agent decisions, 2026-10-04

Owner: the Event 23 implementing engineer (Claude takeover of the stopped Codex thread).
Authority: the user granted full design authority to the takeover agents, with the instruction to take the recommended, spec-consistent option and record it here.
Each entry names its basis and disposition.
Live-game behaviour remains with the user's validation pass and is marked `needs_live_game` where only the engine can prove it.

## D1. Adopt the stopped thread's tranche

Decision: the uncommitted Event 23 gameplay tranche (actor-local breakaway custody, disputed assembly receipts, release cost profile, war-gated hostile-use notification, detonation-profile cleanup, non-yield accident endpoint, Event 5 transfer snapshots, accident report `chaosx.nr23.104`, production quote) is adopted as written.
Basis: parent acceptance and the context-free architect recheck in `subagent_handoffs/023_parent_custody_scope_and_assembly_audit_resolution_2026-10-03.md`, plus this takeover's load-safety review (helpers, constants and localisation keys resolve, braces balance, no state-scope `exists`, no constant-days timed flags, no scoped temporary variables).
Only the `sov_nuclear_bombs_*` bridge lines of `005_soviet_collapse_effects.txt` were taken; the camps/UWR aftermath hunks belong to another workstream.
Disposition: `implemented` in commit `aa1435e5c`.

## D1a. Replacement art

Decision: the parent-selected achievement triplets (three v2, four v1) and the six production decision icons are committed with their lineage.
Basis: `023_achievement_icon_runtime_promotion_2026-09-26.md` and `023_production_decision_icon_replacements_v1_2026-10-03.md`; runtime SHA-256 hashes match the selected candidates 27/27 and GFX aliases are unchanged.
Disposition: `implemented` in commit `3d7e3306e`; in-game presentation `needs_live_game`.

## D3. Vanilla nuclear raids are booked, not disputed

Decision: a Soviet native stockpile below the event's operational, assigned and reserved custody, with no Event 23 delivery pending, is booked as expended devices (operational first, then assigned depot mirrors in owned-state order).
A later surplus, such as a cancelled raid's refund, is tolerated.
A shortfall that would reach reserved devices stays a genuine dispute.
The stockpile audit becomes available again while a national custody dispute exists and clears it once every bucket is non-negative, the books balance and the native stockpile covers intact Soviet custody.
A Soviet `on_nuke_drop` that is not the pending Event 23 request counts as a combat use, sets public knowledge to used, breaches an active or verified moratorium and a pending or verified stand-down or settlement, records the major-power receipt when the struck state's controller is a nuclear major, fires the existing first-use news once, and refreshes achievement receipts.
No Chaos, Fallout or death consequence is called a second time; the native callback's shared hook already applied them.
Basis: the dispute flag was never cleared, so one natural raid permanently blocked moratorium, collapse finalisation, complete accounting and the clean-ledger achievements, while "The Bomb Never Fell" stayed earnable after nuking; spec Part 7 requires shared, single consequences.
The vanilla raid collects its device at creation (`common/raids/_documentation.md`, `essential_equipment`).
Disposition: `implemented`; raid timing and refunds `needs_live_game`.

## D4. Soviet AI does not use vanilla nuclear raids while Event 23 is active

Decision: `common/raids/nuclear_raids.txt` overrides the installed vanilla file with one added modifier at the start of each of the six raid types' `ai_will_do` (`nuclear_strike`, `nuclear_missile_strike`, `nuclear_missile_strike_submarine`, `thermonuclear_strike`, `thermonuclear_missile_strike`, `thermonuclear_missile_strike_submarine`).
The modifier is `factor = 0` under `sov_nuclear_bombs_native_raid_ai_restrained` (SOV, AI, Event 23 actor valid).
All other vanilla content is copied unchanged below a four-line header comment.
Human players and every other country keep vanilla raid behaviour.
Basis: README non-negotiables and Part 9 (no AI major exchange below Evolution IV, no use from high Chaos alone); the vanilla raid weight (base 1, x2 against majors, x2 for SOV on missile and thermonuclear types) is the only engine-side lever, and installed `common/raids/_documentation.md` documents `ai_will_do` with FROM as the target country and "AI only wants to do raids if resulting AI weight is > 0".
Soviet AI nuclear use therefore runs only through the Event 23 decision chain.
Probability: before-source of the vanilla file is archived as `probability_source_snapshots/ai_surfaces_before_2026-10-04/before_vanilla_nuclear_raids.txt`; the compare is recorded with item D11.
Disposition: `implemented`; AI raid behaviour `needs_live_game`.

## D5. AI phase-navigation router

Decision: the accepted and queued router from `023_ai_phase_navigation_closure_addendum_2026-10-03.md` is implemented as one deterministic first-match table in `sov_nuclear_bombs_ai_route_existing_phase`, run only by the hidden coalesced receiver `chaosx.nr23.182` with SOV as ROOT.
`sov_nuclear_bombs_ai_request_phase_review` marks one pending review for an AI Soviet actor and schedules the receiver once with the existing `timer_floor` delay; later requests coalesce.
The receiver has no trigger, clears its own scheduling flag first, and lets the router apply the AI and actor guards, so a human takeover or an invalid actor only clears navigation fields.
Rows, in order: live work (`sov_nuclear_bombs_event_navigation_is_protected`: native delivery pending or confirmed, a device reservation, a prepared test or strike, an authorized retaliation, an open coercion or settlement dossier, or any active project, mission or verification) holds the board and only restores a displaced staged board (test 3, authorization 5, coercion 4); then moratorium 8, collapse 7, retaliation duty or an Evolution IV first-use candidate 6, all entered at once; then an uninvestigated test failure 3, custody duty 1, production duty 2, test purpose 3, coercion purpose 4, otherwise custody 1, which respect the existing 14-day `phase_action_cooldown` as a navigation dwell with one coalesced retry on the due day.
Custody duty is finite: one completed audit (repeated during a later national custody dispute only after a full audit interval, tracked by `sov_nuclear_bombs_last_audit_day`), one hardened depot holding devices when one can be hardened, and one line of release authority from Evolution II.
Production duty needs a remaining reactor entitlement with a valid site, missing crews, exercise or authentication, or a real replacement deficit (see D5b).
Test purpose is one test per attained stage through the actor receipt `sov_nuclear_bombs_ai_proof_attempt_stage`, written only when a test or public demonstration preparation actually starts.
Coercion purpose needs Evolution II, real device backing and a current independent enemy minor, with one dossier per target and stage through `sov_nuclear_bombs_ai_coercion_attempt_stage` and `sov_nuclear_bombs_ai_coercion_attempt_target_id`; a verified settlement keeps its counterpart covered.
Retaliation duty is confirmed enemy use without any release authority (so delegation, the only phase-6-gated action, is reachable) or an open Evolution III exchange that has not yet been limited or suspended; every other retaliation action is phase-independent and stays reachable from any board.
The router writes at most one phase and never pays, grants, reserves, launches, settles or applies consequences.
Review seams sit at the end of the doctrine, reactor, production, training, custody support, test, coercion, authorization, hotline, retaliation, moratorium, dismantlement and collapse completion and cancel helpers, in the `.160`, `.161` and `.162` verification options, and once per existing 30-day `on_daily_SOV` maintenance interval; no new world scan, pulse or all-country hook exists.
Evolution phase writes and the two incoming-attack writes in `on_nuke_drop` go through `sov_nuclear_bombs_apply_event_phase_request`: an AI actor is reviewed, and a human board moves only when no live work, moratorium, custody collapse or opening doctrine owns it.
This also stops an evolution from cancelling a human's running audit, hardening or dispersal through their custody-phase cancel triggers, so it is recorded as a bounded human-facing repair; the human command board itself is unchanged.
The reactor-completion write keeps its human behaviour and only reviews the AI.
`sov_nuclear_bombs_operational_command` is hidden from the AI (`is_ai = no` in `visible` and `target_root_trigger`), which removes the repeated AI command-board purchase; `.100` option weights are unchanged.
Supporting AI eligibility changes, all recorded for the probability compare: the test-site survey gives zero AI weight to a site that cannot host a test now (no device or out of the delivery ceiling), storage hardening gives zero AI weight to an empty depot, and coercion target selection gives zero AI weight to the counterpart already coerced at the current stage.
Two player-facing repairs ride with the router because it depends on them: the survey can be repeated while the surveyed site holds no device, and the instrumented proof test now requires the same reachable endpoint its preparation helper already required, so it can no longer take the cost without starting a test.
Basis: the parent acceptance recorded in the addendum, Part 9 AI design goals and hard blockers, and the lead's D5.
Disposition: `implemented`; AI campaign behaviour `needs_live_game`; probability compare recorded with D11.

## D6. Evolution II and Evolution IV use routes

Decision: the final-authorization AI block below Evolution III is replaced by a target-class guard, and the Evolution IV prospective first use against a nuclear major is connected to the existing selector and preparation actions.
The new AI modifier is `factor = 0` under `sov_nuclear_bombs_event_ai_prepared_major_strike_is_unguarded`: the staged state belongs to a nuclear major and the staged first-use gate (`sov_nuclear_bombs_event_can_authorize_first_use`) does not hold.
A prepared Evolution II strike on a nonnuclear minor or breakaway therefore keeps its existing weight, while no AI releases against a major outside the Evolution IV emergency; no numeric weight changed.
The shared emergency core `sov_nuclear_bombs_event_first_use_emergency` now backs both the unchanged staged gate `sov_nuclear_bombs_event_severe_first_use_gate` (which also checks that a staged state exists before reading it) and the new `sov_nuclear_bombs_event_prospective_first_use_gate`, which adds one line of release authority, unsuspended orders, no verified stand-down and an unreserved device.
Outside a confirmed exchange, `sov_nuclear_bombs_select_retaliation_target` is visible and has a non-empty pool only under that prospective gate and with no coercion dossier open; the pool (`sov_nuclear_bombs_event_state_can_prepare_major_first_use`) holds lower-consequence states of a nuclear major at war with the Union and not under Soviet control, with capitals and populous states admitted only after an enemy strike on a populated Soviet state.
Below Evolution IV, or at Evolution IV with any severe condition missing (including at 1100 Chaos), the pool is empty.
`sov_nuclear_bombs_prepare_limited_strike` is visible for that marked state at Evolution IV outside an exchange, lists the emergency, authority and target requirements as three separate lines, and its helper stages the existing combat context once through `sov_nuclear_bombs_event_can_prepare_major_first_use` before entering authorization 5.
Certification, the separate final authorization, the strike-preparation mission's validity check and the runtime `sov_nuclear_bombs_action_major_first_use_gate_is_valid` guard remain the release checks; no exchange receipt is fabricated and `authorize_retaliation` is not used as an alias.
The selector's `target_root_trigger` now carries the exchange-or-emergency gate, so the world state scan no longer runs daily while neither applies.
Basis: README non-negotiables, Part 5 (Evolution IV first use only under severe strategic loss), Part 9 hard blockers, the closure addendum's prospective-connection section, and the lead's D6.
Disposition: `implemented`; native release `needs_live_game`; probability compare recorded with D11.

## D5b. AI inventory ceiling for device assembly

Decision: `sov_nuclear_bombs_assemble_device_batch` gives zero AI weight unless `sov_nuclear_bombs_event_ai_has_production_deficit` holds.
The ceiling is the attained stage's grant reference `sov_nuclear_bombs_cumulative_produced` (100, 175, 275, 400 or 600) less the event-wide transferred, missing and dismantled devices; intact Soviet custody is the actor's operational, assigned and reserved devices.
Only expended devices therefore create a deficit, and an indivisible batch may overshoot it once before assembly stops again.
The router's production duty uses the same predicate, so the AI does not enter production for assembly alone without a deficit.
Player production, batch arithmetic, grants and the ledger are unchanged.
Basis: the closure addendum's inventory policy (parent-accepted 2026-10-03), Part 9 production AI ("should not build bombs without regard to delivery, reactors, and security"; priority falls when the stockpile exceeds the posture cap), and the lead's item list.
Disposition: `implemented`; probability compare recorded with D11.

## D7. State-targeted orders are chosen on the map

Decision: all fifteen state-targeted Event 23 decisions use `on_map_mode = map_only`: the fourteen named in the closure addendum (`operational_command`, `collapse_command`, `harden_storage_site`, `disperse_reserve_package`, `expand_fissile_production`, `assemble_device_batch`, `survey_remote_test_state`, `select_coercion_target`, `redirect_strike_state`, `preserve_reserve`, `select_retaliation_target`, `select_disputed_depot`, `select_dismantlement_site`, `breakaway_secure_custody`, each with the `sov_nuclear_bombs_` prefix) and `sov_nuclear_bombs_breakaway_request_return`, which has the same one-row-per-state behaviour and would otherwise break the local custodian's two-row budget.
Target pools, costs, availability and AI evaluation are unchanged; the category description tells the player that state choices are made on the map while the category is open.
Basis: installed `common/decisions/_documentation.md` (each matching target creates its own entry), offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` lines 576-595 (`on_map_mode = map_only`), the vanilla `FIN_set_up_weapon_caches_in_state` map-only precedent cited in the addendum, the addendum's presentation recommendation, and the lead's D7.
Disposition: `implemented`; map icon discoverability and list density `needs_live_game`.

## D2. Delivery route: launch_nuke behind a vanilla-equivalent preflight

Decision: Event 23's own authorization chain releases through vanilla `launch_nuke`, and vanilla nuclear raids remain the parallel native route (booked by D3 and AI-gated by D4).
The preflight `sov_nuclear_bombs_event_has_delivery_route` now mirrors the installed `nuclear_strike` raid: atomic weapons, at least ten deployed strategic bombers through `constant:sov_nuclear_bombs_delivery.deployed_bomber_floor = 9` used as `size > 9` (the `strategic_bomber` sub-unit type also covers `strat_bomber_intercontinental`, matching the raid's two equipment alternatives), a Soviet-controlled air base, and fuel.
The exact-endpoint range ceiling stays in `sov_nuclear_bombs_event_state_has_delivery_access`, and combat use still requires war with the target through the limited-strike and major-strike validators.
Delivery crews and the command exercise stay visible in the production phase and show the requirement through `sov_nuclear_bombs_delivery_route_requirements_tt`; the three test preparations show the surveyed-endpoint requirement through `sov_nuclear_bombs_test_delivery_route_requirements_tt`.
Breakaway delivery integration uses the same preflight for its own holder.
Basis: spec Part 4 lines 305-311 (use the installed vanilla delivery system; raids or another current vanilla path; validate range, fuel, air access and readiness; no parallel combat system or free aircraft), installed `common/raids/nuclear_raids.txt` (the raid outcomes call `launch_nuke` and require ten `strategic_bomber` or `strat_bomber_intercontinental_equipment` and an air base), installed `documentation/effects_documentation.md` lines 4745-4758 (`launch_nuke` takes a state or province and consumes a bomb; no documented effect starts a raid), installed `common/units/air.txt` (`strat_bomber` and `strat_bomber_intercontinental` share `type = strategic_bomber`), and `subagent_handoffs/023_vanilla_delivery_route_audit_2026-09-26.md`.
This closes the long-standing `blocked` disposition of the native bomber delivery route: no script effect can start a raid, so the accepted Event 23 delivery is the launch_nuke release behind this preflight, not a raid adapter.
Disposition: `implemented`; release timing and on_nuke_drop confirmation `needs_live_game`.

## D11. Probability baseline and compare

Decision: before sources for every changed AI surface were frozen in `probability_source_snapshots/ai_surfaces_before_2026-10-04/` before the edits, and the compare request with source-level scenario outcomes is `subagent_handoffs/023_ai_surfaces_probability_compare_2026-10-04.md`.
The MCP `probability_inspect` route (`decision_ai_will_do`, narrow source path, with and without a candidate pool) returned `INTERNAL_ERROR` with no artifact, so the MCP evaluate and compare passes are recorded as an exact blocker rather than retried.
No numeric weight or deferred evolution timing (120/120/180/90) changed (lead's D8).
Disposition: `blocked` on the server error for the MCP compare; source-level evidence recorded.

## D9. Default enablement and catalog promotion

Decision: Event 23 stays enabled in new games through `check_variable = { event_id = constant:sov_nuclear_bombs_event.id }` in `event_log_event_is_reworked_default_enabled`, which is already committed in `HEAD` (since `3098ed9d2`).
The shared working tree carried another workstream's uncommitted hunk in `common/scripted_triggers/chaosx_settings_triggers.txt` that removed this line while adding Event 42's line; after re-reading the file, one minimal Edit restored the Event 23 line in the working tree, so the remaining uncommitted hunk is only Event 42's addition and nothing Event 23-related needs committing there.
The catalog promotion (Status `To Be Reworked` to `Needs Testing`, Cluster ID and World-End Scenario blank) is queued in [catalog_changes_pending.md](catalog_changes_pending.md); the workbook and its CSV exports are untouched.
Basis: the lead's D9, applied after the priority 1 and 2 gameplay commits of this round.
Disposition: enablement `implemented` in `HEAD`; catalog row `accepted and queued` for the workbook owner.

## D13. Accepted design folded into the specs and event doc

Decision: the accepted closure addendum and decisions D2 to D9 are promoted into Part 4 (accepted delivery route and AI use guards), Part 5 (Evolution IV first-use connection), Part 9 (AI phase navigation and restraint), and the decision map (map-only presentation and navigation), each with its acceptance basis.
`docs/events/023_sov_nuclear_bombs.md` describes the current router, Evolution II and IV use, map-only presentation, delivery route, raid accounting and AI gate, default enablement and the queued catalog row; `023_sov_nuclear_bombs_runtime_effects.md` records the event-owned navigation helpers and the delivery preflight.
The closure addendum is marked `promoted into an accepted spec`.
Disposition: `implemented`.

## Round 1 review (skeptical reviewer, 2026-10-04)

Scope: every Round 1 commit from `aa1435e5c` to `280df0b95`, read with `git show` against the installed documentation and the existing Event 23 helpers.
Helpers called with `= yes`, `constant:` references, localisation keys named by decisions and events, and brace balance all resolve in the touched files.
The adopted Event 5 bridge lines and the shared Chaos Meter accident endpoint reference only constants present in `HEAD`.
The vanilla raid override differs from the installed file only by the header and the six documented modifiers.

### R1. Category description line break

Finding: `d47e5ab5d` wrote a literal line break inside the quoted `sov_nuclear_bombs_command_category_desc` string, which the localisation parser does not accept as one entry.
Decision: the sentence stays and joins the entry through `\n\n`.
Disposition: `implemented`.

### R2. Self-held detonations are not Soviet nuclear use

Finding: the `on_nuke_drop` branch added in `9aac54b6b` recorded every non-pending Soviet detonation as combat use, so another event's accident in a Soviet state (Events 47, 53 and the airship decision launch `launch_nuke` on the launcher's own state) fired the first-use news, broke a moratorium or stand-down and counted toward the combat-use achievements.
Decision: the branch also requires that the struck state is not controlled by the launcher; a vanilla raid always strikes a state at war with the Union, so raid booking is unchanged.
Disposition: `implemented`; live raid confirmation `needs_live_game`.

### R3. Repeatable survey and aborted targets

Finding: `7bbd68da1` made the test-site survey repeatable while the surveyed site holds no device, but every survey still added 4 readiness, so readiness could be bought repeatedly with an empty site.
Decision: a survey raises readiness only when no survey is already recorded for the current test family, and the result is clamped like every other readiness change.
Finding: after an abort, the marked retaliation or first-use target stayed selected, so the Evolution IV preparation reopened at once and each retry paid the release cost again (listed by the engineer as a remaining gap).
Decision: `sov_nuclear_bombs_abort_and_recover` clears the selected state unless an open coercion dossier still owns it; the coercion demand keeps its state.
Disposition: `implemented`.

### R4. AI restraint, dispersal and reach guards

Finding: the router makes custody the AI's idle board, and the moratorium decision is visible there with base weight 0.90 and no reason, so an idle AI could seal its arsenal at the opening and stay in phase 8; an idle AI could also repeat reserve dispersal, paying command power, trains and fuel and resetting its posture each time (both listed by the engineer as remaining gaps).
Decision: the moratorium AI weight is zero without `sov_nuclear_bombs_event_ai_has_restraint_reason` (Part 9: a demonstrated or employed arsenal, a serious nuclear crisis or test accident, or a verified reciprocal, stand-down or settlement agreement), and the AI disperses at most once per attained stage through the receipt `sov_nuclear_bombs_ai_dispersal_stage`, written when a dispersal completes.
Finding: the retaliation selector's AI weight did not check reach, while preparation and authorization both require it, so the AI could repeatedly pay the command cost for an unreachable mark.
Decision: the selector's AI weight is zero for a state outside `sov_nuclear_bombs_event_state_has_delivery_access`.
No numeric weight changed; these are factor-zero eligibility gates like D5's.
Basis: Part 9 moratorium and stand-down guidance, the closure addendum row 17 ("a justified restraint purpose"), and the user's full design authority.
Disposition: `implemented`; MCP compare `blocked` (see D11 and the compare handoff); AI campaign behaviour `needs_live_game`.

## Round 1 review, second pass (skeptical reviewer, 2026-10-04)

Scope: every Round 1 commit from `aa1435e5c` to `444500295`, plus the Event 028 edit `d4ef004ca` to the Event 23 `on_nuke_drop` branch, read with `git show` against the installed raid, effect and trigger documentation and the offline wiki.
Helper calls with `= yes`, `constant:` references and the localisation keys named by decisions, triggers and events resolve in `HEAD`; the touched script files balance their braces; the localisation file keeps its BOM.
The raid override still differs from the installed vanilla file only by the header and six modifiers, and no other file defines those six raid types.
The adopted Event 5 bridge lines reference only helpers present in `HEAD`, and the Chaos Meter condemnation pointer `chaos_meter_nuclear_target_state` is set by both of its callers before use.

### R5. A raid on the ultimatum target counts as striking it

Finding: `sov_nuclear_bombs_record_native_raid_use` (from `9aac54b6b`) recorded combat use and breached pending agreements but never set `sov_nuclear_bombs_ultimatum_target_struck`, which the authorized strike path sets when the struck government received the ultimatum.
A player could therefore settle an ultimatum, wait for verification, nuke the same government through a vanilla raid and still earn "Ultimatum Without Ash", the same kind of gap D3 closed for "The Bomb Never Fell".
Decision: the helper sets `sov_nuclear_bombs_ultimatum_target_struck` when the struck state's controller or owner is `sov_nuclear_bombs_ultimatum_target_country_id`.
Disposition: `implemented`; raid confirmation `needs_live_game`.

### R6. One AI coercion dossier per enemy minor and stage

Finding: D5 and Part 9 promise one dossier per independent enemy minor and attained stage, but `7bbd68da1` stored only the last target id, so the AI could alternate between two minors (A, B, A, B) at the same stage, paying command power and raising tension on every round.
The selection weight also compared only the state's controller, so a Soviet-held state of an already coerced owner could reopen the same government, and it weighed counterparts that were not at war with the Union although the router enters coercion only for an enemy minor.
Decision: `sov_nuclear_bombs_prepare_coercion` keeps the stage list `sov_nuclear_bombs_ai_coerced_target_ids` for an AI actor, emptied when the attained stage rises; `sov_nuclear_bombs_event_country_is_ai_coercion_candidate` (an independent minor at war with the Union, absent from the list at the current stage, and not the counterpart of a verified settlement) backs both the router's coercion purpose and the selection weight through `sov_nuclear_bombs_event_state_is_ai_coercion_candidate`, which reads the government the dossier would name (the non-Soviet controller, otherwise the owner).
The selection weight's factor-0 eligibility gate is the only weight change; base and multipliers are unchanged.
Basis: D5, Part 9 ("one dossier per independent enemy minor and stage"; "avoid repeated threats against protected targets"), and the user's full design authority.
Disposition: `implemented`; MCP compare `blocked` (see D11 and the compare handoff); AI campaign behaviour `needs_live_game`.

### R7. Survey readiness uses its tuning constant

Finding: the R3 survey fix kept the literal `4` although `sov_nuclear_bombs_tuning.survey_readiness` holds that value.
Decision: the survey reads `constant:sov_nuclear_bombs_tuning.survey_readiness`; the value is unchanged.
Disposition: `implemented`.

### Remaining risks recorded, not changed

- The router's Evolution IV first-use candidate (`sov_nuclear_bombs_event_ai_has_first_use_candidate`) does not test bomber reach, while the selector gives unreachable states zero AI weight. If every candidate state lies outside the delivery ceiling, the AI holds the retaliation board without marking a target until the emergency ends. Disposition: `implemented` by R8 in the third pass below.
- The AI reaches certified delivery crews only with ten deployed strategic bombers (D2). No Event 23 AI strategy raises Soviet strategic bomber production; the vanilla default ratio applies. Part 5 allows ("may") such a production shift. Disposition: `implemented` by R2-8 in Round 2 (the vanilla Soviet plan in fact sets a strategic bomber weight of 0 and the default plan excludes SOV).
- A refunded vanilla raid leaves its booked device in the expended bucket while the native stockpile holds a surplus (D3 tolerance); it does not count as combat use or affect the achievements. Disposition: `accepted` under D3.

## Round 1 review, third pass (skeptical reviewer, 2026-10-05)

Scope: every Round 1 commit from `aa1435e5c` to `280df0b95`, the review fixes `444500295` and `de11430be`, and the Event 028 edit `d4ef004ca`, read with `git show` against the installed raid, effect, trigger and building documentation, the offline wiki's scope rules and the vanilla AI strategy files.
A mechanical pass over `HEAD` found balanced braces in every Event 23 script file and no unresolved helper call, `constant:` reference, localisation key or event id.
The raid override still differs from the installed vanilla file only by its header and the six modifiers; the 27 promoted DDS files are real ARGB textures behind LFS pointers (21 achievement files at 64x64 and six decision icons at the vanilla 33x32 decision size); the Event 5 bridge brackets every literal transfer and release in the Event 5 effects except KMB's own concession release of KHA, which the generic `on_release_as_puppet` and `on_state_control_changed` hooks already reconcile.
The catalog row queued by D9 matches the in-game details and evolution localisation.
One narrow `hoi4_probability_inspect` call (`decision_ai_will_do`, the decisions file, `candidatePool = ["sov_nuclear_bombs_audit_stockpile"]`) again returned `INTERNAL_ERROR` with `artifactCount = 0`; it was not retried.

### R8. The first-use candidate needs a reachable state

Finding: the router enters the retaliation board at once for an Evolution IV first-use candidate, but `sov_nuclear_bombs_event_ai_has_first_use_candidate` counted enemy-major states outside the delivery ceiling, while R4 gives those states zero selector weight; with every candidate out of reach the AI held phase 6 for the whole emergency and never marked a target, and custody, production and test work stayed closed to it.
Decision: each candidate state must also pass `sov_nuclear_bombs_event_state_has_delivery_access` with the Soviet actor as launcher, entered through `ROOT = { PREV = { ... } }` so the trigger's `PREV` is the actor (offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, PREV usage: the scope tree is a stack and `PREV` inside `ROOT` is the scope it was entered from).
An already selected target keeps its own exact-endpoint check through `sov_nuclear_bombs_event_selected_major_first_use_target_is_valid`.
Source scenario walk: at Evolution IV with the full emergency and one enemy nuclear major whose lower-consequence states all lie beyond the 1000-unit ceiling, the router now skips row 5 and continues to test-failure, custody, production, test and coercion purposes; when a front advance brings one such state inside the ceiling, the next review (30-day maintenance or any seam) enters phase 6 and the selector has a weighted state.
Disposition: `implemented`; AI emergency behaviour `needs_live_game`.

### R9. The AI repeats a stockpile audit only when it can close the dispute

Finding: `9aac54b6b` made "Audit the Stockpile" visible again during a national custody dispute, and the router's custody duty re-enters custody for that dispute after every full audit interval; the decision's AI weight (base 1.20, x2.00 below 70 integrity) had no dispute condition, so a dispute that an audit cannot close (a shortfall reaching reserved devices, a disputed reservation or an Event 5 bucket mismatch) made the AI pay the security cost for a futile 120-day audit on every cycle and pull its board back to custody each time.
Decision: after the first audit, the AI weight is zero unless `sov_nuclear_bombs_native_custody_reconciles` holds, which is the exact condition under which a completed audit clears the dispute, and the router's dispute row requires the same predicate.
The first audit, the human decision and the audit's effect are unchanged; base and multiplier are unchanged.
Source scenario walk: a reserved device's native bomb leaves the stockpile while no Event 23 delivery is pending, so the refresh sets the national dispute; the AI audited once, and 120 days later neither the router nor the decision weight returns to the audit while the stockpile stays short; when a vanilla reactor bomb later covers the shortfall, the predicate holds, the router's custody row applies after the audit interval and the AI audit closes the dispute.
Probability: before source is `HEAD` `1cebd5393e82e8661fab4d92e35c5807d8b15cdc` (`common/decisions/023_sov_nuclear_bombs_decisions.txt`, `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`), readable with `git show`; MCP compare `blocked` (see D11).
Disposition: `implemented`; AI dispute behaviour `needs_live_game`.

### Remaining risks recorded, not changed

- The strategic-bomber production risk recorded in the second pass stands: the vanilla default AI keeps a small strategic bomber unit ratio and SOV has strategic bomber designs in `common/ai_equipment/SOV_planes.txt`, so ten deployed bombers are reachable but not guaranteed. Disposition: `implemented` by R2-8 in Round 2.
- A Soviet nuclear stockpile reduced by another event or system outside raids (for example a scripted bomb removal) is booked as expended like a raid draw. Disposition: `accepted` under D3, which tolerates surpluses and books every shortfall above reserved custody the same way.

## Round 2 (2026-10-04)

Scope: the lead's round 2 remaining-work list and planning decisions for Event 23.
Before sources for every AI or probability surface touched in this round are frozen from `HEAD` `b6d4c6e45` in `probability_source_snapshots/ai_surfaces_before_round2_2026-10-04/` (constants, decisions, event effects, event triggers, MTTH and on_actions).

### R2-1. Evolution IV war assessment writes the strategic-loss inputs

Finding: `sov_nuclear_bombs_event_first_use_emergency` required `sov_nuclear_bombs_strategic_losses` of at least 3 and the flags `sov_nuclear_bombs_capital_threat_active`, `sov_nuclear_bombs_front_collapsed` and `sov_nuclear_bombs_reserve_exhausted`, but nothing wrote them, so Part 5's major first use, the D6 prospective selector, the hotline's severe-gate branch, the doctrine AI capital-threat factors and "The Last Telephone" could never occur.
Decision: `sov_nuclear_bombs_assess_strategic_losses` (event effects, next to the routine maintenance) is the single writer.
It runs for the valid Soviet actor at war and counts five indicators, each adding `constant:sov_nuclear_bombs_tuning.strategic_loss_indicator`, so all five reach the existing `strategic_loss_critical` (5): the capital is threatened (`sov_nuclear_bombs_event_capital_is_threatened`: the current capital is not Soviet-controlled or borders a state held by a country at war with the Union, or Moscow is lost), Moscow is lost (`sov_nuclear_bombs_event_home_capital_is_lost`: the home capital `constant:sov_nuclear_bombs_tuning.home_capital_state` = 219 is outside Soviet control while owned by the Union or held by an enemy, so the threat survives the engine's capital relocation and a Moscow left to a breakaway at peace does not count), the front has broken (`surrender_progress > constant:sov_nuclear_bombs_surrender_progress.front_collapse` = 0.25), the front is in full collapse (`severe_collapse` = 0.50), and the reserve is exhausted (`manpower_k < constant:sov_nuclear_bombs_tuning.reserve_exhausted_manpower_k` = 250, the thousands getter).
The three gate flags and two display flags (`sov_nuclear_bombs_home_capital_lost`, `sov_nuclear_bombs_front_collapse_severe`) are rebuilt on each assessment; at peace or for an invalid actor every input is cleared.
`sov_nuclear_bombs_refresh_strategic_losses` runs it from the existing `on_daily_SOV` block every `loss_assessment_interval_days` (7), and at once when peace leaves an earlier assessment standing; the opening initialization runs it once so a wartime doctrine choice sees its capital threat.
When the first-use emergency starts or ends, the assessment asks the AI router for one coalesced review through `sov_nuclear_bombs_first_use_emergency_observed`.
The first-use gate itself is unchanged and still needs all three flags, at least three losses, verified enemy use or launch preparation, delivery, crews, readiness and integrity, so first use stays rare.
The player sees the assessment as one plain line, "War situation: ...", in the category header at Evolution IV and in the first-use emergency requirement tooltip; no variable names are shown.
Source scenario walk: a Soviet actor at Evolution IV and 1000 Chaos, at war with a nuclear major that has struck it, with Moscow occupied (capital threat and Moscow lost), surrender progress 0.55 (front broken and full collapse) and 120k manpower (reserve exhausted) records five losses and all three flags; with release authority, an unreserved device, certified crews, a ready route, readiness 75 and integrity 20 the prospective gate holds and the selector opens.
Removing any single input closes it: a capital with no enemy neighbour and Moscow held leaves `capital_threat_active` unset; surrender progress 0.20 leaves `front_collapsed` unset; 400k manpower leaves `reserve_exhausted` unset.
The smallest qualifying case is three losses (enemy next to the capital, front broken, reserve exhausted), which equals `first_use_min_strategic_loss`.
Probability surfaces whose inputs change: the custody doctrine AI factor 1.20 and the delegation AI factor 1.60 on `sov_nuclear_bombs_capital_threat_active`, the doctrine-reform availability, the router's first-use candidate and every AI weight behind the severe and prospective gates; numeric weights are unchanged and the before sources are frozen as above.
Basis: Part 5 (severe strategic loss: high capitulation progress, imminent capital loss, a broken front), Part 10 scenario G case 2, README non-negotiable 6, CLAUDE.md 1.8 (no new world iteration) and 1.15 (`manpower_k`), and the lead's round 2 decision 2.
Disposition: `implemented`; weekly cadence and live thresholds `needs_live_game`; MCP compare see R2-10.

### R2-2. Timed flags take literal days and value

Finding: the assembly cooldown passed a bare temporary variable as `days`, and the exchange super-event flag passed a bare temporary variable as `days` and `value = constant:sov_nuclear_bombs_event.super_event_id`; installed `common/scripted_effects/SOV_scripted_effects.txt` line 28 notes that a timed flag's days does not work with variables, the only working vanilla forms are a literal and `days = var:<normal variable>` (`SIA_scripted_effects.txt` line 780), and `value = constant:` on a flag is undocumented.
A failed parse could leave the cooldown permanent, locking device assembly and the AI production duty after one batch, or show the 108 super-event with the wrong picture.
Decision: both flags are built inside a `meta_effect` whose text receives integer literals from `[?temp|.0]`: the cooldown from `constant:sov_nuclear_bombs_duration.production_mission` (120, inside `hidden_effect` because it runs in a mission completion), and the super-event flag from `constant:sov_nuclear_bombs_tuning.super_event_visible_days` (30) and `constant:sov_nuclear_bombs_event.super_event_id` (108), matching Event 5's `soviet_collapse_emit_super_event` and the shared super-event selectors' `value = 108`.
No timed flag in the Event 23 files keeps a variable or `constant:` token; event delays keep `days = constant:`, which vanilla supports for events.
Basis: the lead's round 2 decision 1 and CLAUDE.md 1.9.
Disposition: `implemented`; flag expiry and the super-event picture `needs_live_game`.

### R2-3. Imminent breakaway operationalization is derived

Finding: "Destroy a Compromised Site" required the never-set country flag `sov_nuclear_bombs_breakaway_operationalization_imminent` in `visible` and `available`, and the recovery raid and device disablement AI factors boosted on the same flag, so the decision-map and Part 6 last resort never appeared and `P23_COLLAPSE_RAID_IMMINENT_OPERATIONALIZATION` could not occur.
The decision also required `sov_nuclear_bombs_site_technical_denial` on the site, but technical denial (set by "Disable the Devices") changes the site's custody state away from breakaway physical custody, so the holder's local receipts and every operationalization step fail on a denied site; imminence and denial are mutually exclusive.
Decision: the flag is replaced by the state trigger `sov_nuclear_bombs_event_state_breakaway_operationalization_is_imminent` and its selected-depot wrapper `sov_nuclear_bombs_event_selected_breakaway_operationalization_is_imminent`: the holder has the local technical receipt and either the local command receipt or a command formation or delivery integration mission for that exact state id, and the site is intact, held, not denied and not operational.
It is used in all four places; the two AI modifiers keep their numbers (recovery raid base 0.20 with factor 1.80, disablement base 1.40 with factor 2.00).
The demolition's technical-denial requirement is replaced by Part 6's "recovery impossible", `sov_nuclear_bombs_event_selected_breakaway_recovery_is_impossible`: the selected depot lacks the rail recovery route or the Soviet security force that recall, the rail corridor and joint custody all require.
In `available` both appear as localised custom tooltips (the existing requirement sentence for imminence and `sov_nuclear_bombs_breakaway_recovery_impossible_tt`), with the actor and selection checks hidden; the demolition action contract is unchanged and needs no denial.
Source scenario walk: a breakaway holds a transferred depot in a state it controls; after technical access completes and it starts command formation for that state, the trigger holds, the raid and disablement AI factors apply, and "Destroy a Compromised Site" is visible and available because the Union has no force in the state.
Before technical access completes, after the holder finishes delivery integration (operational), after "Disable the Devices" (denied), or when the holder's running mission belongs to another depot, the decision is hidden.
If the Union retakes control of the state with a division and the rail route exists, the decision stays visible but unavailable, and recall becomes the route.
Basis: decision map "Destroy the site" (recovery impossible, operationalization imminent, exact site validated), Part 6, the probability scenario's "technical access and near command formation", and the lead's round 2 decision 3, adjusted for the denial contradiction under the user's full design authority.
Probability: before sources frozen in `ai_surfaces_before_round2_2026-10-04/before_decisions.txt`; MCP compare see R2-10.
Disposition: `implemented`; breakaway campaign behaviour `needs_live_game`.

## Round 2, continuation (2026-10-05)

Scope: the lead's rebuilt round 2 remaining-work list, taken over after the previous round 2 implementer stopped.

### R2-4. The stopped round 2 tranche is adopted

The uncommitted R2-3 working-tree hunks (the decisions file, the event triggers, two localisation lines, the event doc paragraph and the R2-3 record above) and the one-line `docs/systems/chaos_meter/README.md` index entry for the D1 non-yield test-accident endpoint were re-read and adopted unchanged.
Review: `PREV.id` inside `var:sov_nuclear_bombs_site_holder = { ... }` is the depot state, the same pattern as the operationalization guard in the runtime effects; the demolition action contract (`sov_nuclear_bombs_action_source_is_valid` and the reservation path) has no technical-denial term; the demolition's `available` shows the no-active-project flags (all localised), the imminence sentence and `sov_nuclear_bombs_breakaway_recovery_impossible_tt`, with the actor and selection checks hidden.
Commit: `f56c84b52`; the other workstreams' chaos meter hunks stayed unstaged.
Disposition: `implemented`.

### R2-5. Decision requirement tooltips show no internal names

Finding: expanding every displayed `available` block through its scripted triggers (skipping `hidden_trigger` and `custom_trigger_tooltip`) found unlocalised `check_variable` or `has_variable` names in 21 decisions, and `has_event_target` lines ("sov_nuclear_bombs_selected_state is set", from the vanilla `TRIGGER_HAS_EVENT_TARGET` text) in eight, three of them outside those 21 (close the dossier, private signal, partial settlement).
Decision: every such check is wrapped, never changed.
Phase checks are hidden in the six decisions whose `visible` already requires the same phase, so the phase is never the only blocker; the coercion dossier's event target is hidden the same way in "Close the Coercion Dossier", and the security-force trigger hides its event-target guard.
Selection checks read as plain sentences: the surveyed test site, the selected depot (intact and out of Soviet hands, reachable by rail, still holding transferred or assigned devices, or returned on request), the coercion target and the prepared strike.
Thresholds show their values: test readiness shows the `minimum_test_readiness` constant and the current Arsenal Readiness, the demand shows its current level out of the maximum, the test site shows the population ceiling, and the strike shows current readiness and integrity.
The custody-record checks inside `sov_nuclear_bombs_event_can_enter_moratorium`, `sov_nuclear_bombs_event_can_reactivate_moratorium` and `sov_nuclear_bombs_event_collapse_resolution_ready` are wrapped inside those triggers ("Every registered device is accounted for", "At least one device is operational"), so every caller shows the same lines.
Equivalence: parsing `HEAD` and the working tree with `hidden_trigger` and `custom_trigger_tooltip` wrappers removed gives identical trees for the decisions and event-trigger files; a rerun of the expansion finds no unlocalised variable, flag or event-target name in any displayed `available` block.
Basis: CLAUDE.md 2.4, 2.7 and 4.13, and the lead's round 2 decision 2.
Disposition: `implemented`; final tooltip readability `needs_live_game`.

### R2-6. The public exchange stage ladder

Finding: Part 5 defines Nuclear Confrontation, Limited, Expanding and General Exchange and records a public exchange stage, and Part 10 disqualifies Firebreak at General Exchange, but the source had only `sov_nuclear_bombs_major_exchange_active` and a receipt count capped at `major_receipt_minimum` (2); `sov_nuclear_bombs_general_exchange_reached` was never set, so Firebreak stayed earnable after any number of detonations, and `major_exchange_stage` was unused.
Decision: `global.sov_nuclear_bombs_exchange_stage` only advances through `sov_nuclear_bombs_advance_exchange_stage` (runtime effects), with stage values in `sov_nuclear_bombs_tuning`: `exchange_confrontation_stage` 1, `major_exchange_stage` 2 (Limited), `exchange_expanding_stage` 3, `exchange_general_stage` 4.
Nuclear Confrontation is requested when `sov_nuclear_bombs_prepare_hotline` opens a hotline with its nuclear-major partner and when `sov_nuclear_bombs_authorize_retaliation` opens a retaliation window against a nuclear major's state; a stage already past it is kept.
`sov_nuclear_bombs_record_exchange_detonation` runs inside `sov_nuclear_bombs_record_major_exchange_receipt` for every recorded receipt (each is one confirmed detonation between the Union and another nuclear major, from the existing `on_nuke_drop` handler or the Soviet action and native-use confirmations) and increments `global.sov_nuclear_bombs_exchange_detonations`; the first detonation makes the exchange Limited, `exchange_expanding_detonations` (3) or a second opposing nuclear major (`sov_nuclear_bombs_exchange_second_opponent_joined`, from the first receipt partner's id) makes it Expanding, and `exchange_general_detonations` (6) makes it General.
General sets `sov_nuclear_bombs_general_exchange_reached` once; it applies no terminal consequence and never sets `world_end`, and Fallout stays with the shared route.
The counter inherits the receipt function's existing Evolution III and 800-Chaos gate, so it counts the same detonations that open the super-event; no new scan, pulse or all-country hook is added.
Presentation: the Soviet Nuclear Command header shows "Exchange: <stage>" once a confrontation begins (`GetSovietNuclearBombsCategoryExchangeStage`), and the hotline and stand-down descriptions end with "Exchange stage: <stage>" (`GetSovietNuclearBombsExchangeStageName`, "none yet" before any stage).
Retaliation windows: Part 5 says they shorten at Expanding Exchange, but the only window timer is the retaliation window mission's `days_mission_timeout = constant:sov_nuclear_bombs_duration.hotline_mission`, a fixed constant shared by the hotline and the authorized-response window, so per the lead's acceptance rule it is not changed. Vanilla accepts `days_mission_timeout = var:<variable>` (installed `common/decisions/CHI_decisions.txt` line 6454), so a later pass could set a stage-dependent window variable before each activation; that would also shorten the hotline's negotiation window, which Part 5 says the hotline extends, so it needs a separate response-only timer. Disposition of this sub-item: `implemented` in R2b-9 (a per-activation window variable; the hotline keeps 30 days).
Source scenario walk: at Evolution III with 1000 Chaos, a hotline opened during a launch warning records Nuclear Confrontation (stage 1); the United States then strikes a Soviet state (receipt 1: one detonation, Limited, `major_detonation_confirmed`), and the Soviet retaliation lands (receipt 2: two detonations, still Limited, the super-event opens and the exchange major count is 2); a hotline stand-down is then accepted and verified, and `sov_nuclear_bombs_achievement_firebreak_criteria_met` holds because `general_exchange_reached` is unset.
If instead four more detonations follow before verification, the sixth sets General Exchange and the flag, and the Firebreak criteria fail for the rest of the campaign; a British strike on a Soviet state after the American one makes the exchange Expanding at two detonations.
Basis: Part 5 exchange crisis state and stages, Part 10 Firebreak disqualifiers and acceptance scenario H, and the lead's round 2 decision 3.
Disposition: `implemented` (stage ladder, General flag, presentation); window shortening `implemented` in R2b-9; live exchange pacing `needs_live_game`.

### R2-7. The war assessment speeds Evolution III and IV

Finding: Part 5 lists a capital threat as a faster factor for Evolution III and a threatened capital, capitulation progress above the severe-loss threshold and broken fronts for Evolution IV, and R2-1 writes `sov_nuclear_bombs_capital_threat_active`, `sov_nuclear_bombs_front_collapse_severe` and `sov_nuclear_bombs_strategic_losses`, but `common/mtth/023_sov_nuclear_bombs_mtth.txt` read none of them, and all four intervals used a literal `40` for the low-integrity delay.
Decision: Evolution III gains `capital_threat_acceleration` (0.80) on the capital-threat flag; Evolution IV gains the same factor, `front_collapse_acceleration` (0.80) on the severe-collapse flag (surrender progress above `severe_collapse`, the severe-loss threshold) and `strategic_loss_acceleration` (0.85) when losses reach `strategic_loss_critical` (5).
The values sit between the existing war (0.85) and collapse (0.70) factors so a war assessment cannot outrun a confirmed exchange (0.60) or enemy use (0.65); at the worst case all three stack to 0.544, bringing the 90-day Evolution IV centre to about 49 days before the other factors, and the stage still needs its full Chaos and world-state gate.
The literal becomes `constant:sov_nuclear_bombs_mtth.low_integrity_threshold` (40) in all four intervals; it is a timing key separate from `sov_nuclear_bombs_tuning.low_integrity_threshold`, which drives test outcomes, so the two can be tuned apart.
The 120/120/180/90 base centres and every existing factor are unchanged (lead decision D8).
Probability: the before source is the round 2 snapshot `probability_source_snapshots/ai_surfaces_before_round2_2026-10-04/before_mtth.txt`, byte-identical to the file before this change.
One narrow `hoi4_probability_inspect` call (`event_mean_time_to_happen`, `source.path = common/mtth/023_sov_nuclear_bombs_mtth.txt`, `candidatePool = ["sov_nuclear_bombs_evolution_iv_interval"]`, no refresh) returned `INTERNAL_ERROR` with `artifactCount = 0`; it was not retried, and no timing distribution is claimed.
Basis: Part 5 Evolution III and IV active pacing, R2-1, and the lead's round 2 decision 4.
Disposition: `implemented`; MCP compare `blocked` (R2-10); live pacing `needs_live_game`.

### R2-8. The Soviet AI keeps its strategic bomber delivery floor

Finding: every Soviet AI release, test, coercion credibility check and crew certification needs more than `deployed_bomber_floor` (9) deployed strategic bombers (D2), but installed `common/ai_strategy/SOV.txt` gives the Soviet AI no strategic bomber demand: `SOV_unit_production` sets `unit_ratio strategic_bomber = 0` (line 93) and `equipment_production_factor strategic_bomber = -20` (line 146), `default_unit_production` in `default.txt` excludes `tag = SOV`, and only `SOV_bomber_production` keeps one strategic bomber line once the Union has more than 30 military factories. Air unit ratios are weights over all land-based plane ratios (installed `_documentation.md`, Unit ratios, Air), so a weight of 0 means no wanted strategic bombers; once the starting bombers were lost the AI arsenal went inert. The second-pass and third-pass risk records had this as `unresolved`.
Decision: one plan, `sov_nuclear_bombs_ai_delivery_bombers` in the new `common/ai_strategy/023_sov_nuclear_bombs_ai_strategy.txt`, `allowed` for `original_tag = SOV`, enabled by `sov_nuclear_bombs_event_ai_needs_delivery_bombers` (valid Event 23 actor, `is_ai`, atomic research and nukes, a recorded phase past the opening, no Atomic Moratorium, and `sov_nuclear_bombs_event_bomber_force_below_delivery_floor`: no more deployed strategic bombers than the floor, read from the same constant through the preflight's meta-trigger pattern), with `abort_when_not_enabled = yes` so it ends as soon as the floor is exceeded or any condition fails.
Values (file-scoped `@` constants, because the installed documentation and the offline wiki's AI modding page describe `value` as a plain integer and no `constant:` support is documented for it): `unit_ratio strategic_bomber` +3, about a tenth of the Soviet land-based air weights (fighter 20, CAS 2, tactical 5, naval 4), enough to want well over ten bombers from a normal air plan without displacing fighters; `equipment_production_factor strategic_bomber` +20, which cancels the vanilla -20 to neutral; `equipment_production_min_factories strategic_bomber` 1, the vanilla `SOV_bomber_production` value, stacking with it above 30 factories.
Before state: the vanilla values above with no Event 23 plan; no other country is affected (the allowed filter and the actor trigger both require SOV, and `is_ai` excludes a human Union).
Probability: one narrow `hoi4_probability_inspect` call (`ai_strategy_factor`, `source.path = common/ai_strategy/023_sov_nuclear_bombs_ai_strategy.txt`, `candidatePool` with the plan id before its rename to `sov_nuclear_bombs_ai_delivery_bombers`, no refresh) returned `INTERNAL_ERROR` with `artifactCount = 0`; it was not retried.
Basis: D2, Part 5's allowance for a production shift, the lead's round 2 decision 5, and the vanilla precedents `SOV_bomber_production` and `SOV_unit_production`.
Disposition: `implemented`; actual production and deployment behaviour `needs_live_game`; MCP compare `blocked` (R2-10).

### R2-9. Readiness and integrity changes read tuning constants

Finding: 23 `add_to_variable` lines in `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` (audit, hardening, centralization, delegation, authentication, evacuation, test-failure investigation, technical certification, safety-veto overrule, held authorization, limited retaliation, reserve preservation, suspended release orders, sealed reserve, invited observers and arsenal reactivation) added literal readiness or integrity values, against CLAUDE.md 1.3.
Every one already had a matching, unused key in `sov_nuclear_bombs_tuning` with the same value (`audit_integrity`, `harden_integrity`/`harden_readiness`, `centralize_*`, `delegate_*`, `authentication_*`, `evacuation_integrity`, `investigate_*`, `technical_*`, `veto_*`, `hold_integrity`, `limit_retaliation_readiness`, `reserve_integrity`, `suspend_readiness`, `seal_integrity`, `observers_integrity`, `reactivate_readiness`).
Decision: each line reads its key; negative deltas are negative constant values added, never a unary minus on a token. A script mapped each line by its enclosing effect and asserted the key's value equals the literal it replaced, so no gameplay value changes; the clamps are untouched, and a grep for a literal readiness or integrity delta in the Event 23 effects returns nothing.
Disposition: `implemented`.

### R2-10. MCP probability compare for the round 1 and round 2 surfaces

The lead's narrow `decision_ai_will_do` attempt and this round's `event_mean_time_to_happen` (R2-7) and `ai_strategy_factor` (R2-8) attempts all returned `INTERNAL_ERROR` with `artifactCount = 0`; each was made once, without refresh or a repository-wide query, and none was retried.
Evaluate and compare were therefore not run for D4 to D7, R4, R6, R8, R9, R2-1, R2-3, R2-7 or R2-8; the before sources stay frozen in `probability_source_snapshots/ai_surfaces_before_2026-10-04/`, `probability_source_snapshots/ai_surfaces_before_round2_2026-10-04/` and `HEAD` `1cebd5393` for R9.
The exact errors and the source-level scenario expectations are in `subagent_handoffs/023_ai_surfaces_probability_compare_2026-10-04.md` under "Round 2 additions"; they are not compare evidence.
Disposition: `blocked` on the MCP probability route (`INTERNAL_ERROR`, no artifacts).

## Round 2, second pass (2026-10-05)

Scope: the lead's second round 2 work list (coercion responses, credibility memory, test outcomes, exposure, foreign reactions, incidents, false warnings, breakaway bargaining, retaliation timing, delivery-loss decline and the AI-weight constants) and the lead's twelve planning decisions for it.
Before sources for every AI or probability surface touched in this pass are frozen from `HEAD` `a49dc6df5` in `probability_source_snapshots/ai_surfaces_before_round2b_2026-10-05/` (constants, decisions, event effects, event triggers, events and on_actions).

### R2b-0. The Soviet custody board opens after an Event 5 depot transfer

Finding: `sov_nuclear_bombs_open_collapse_recovery` was defined but never called in any commit (`git log -S` finds no caller), so `sov_nuclear_bombs_collapse_active` was never set; the Soviet half of Part 6 (the collapse board, depot selection, recall, rail security, joint custody, the recovery raid, disablement, demolition and "Restore the Ledger"), the `chaosx.nr23.170` review, the collapse news, the collapse posture and both MTTH collapse factors could never occur, while the breakaway half (which reads the holder's own transferred count) still ran.
Decision: `sov_nuclear_bombs_reconcile_event5_state` ends by opening the board on the valid Soviet actor when the reconciled registered depot holds a transferred device or is marked missing and no collapse crisis is open; the helper itself is unchanged, so the crisis opens once and "Restore the Ledger" still closes it through `sov_nuclear_bombs_finalize_collapse`, after which a later transfer opens a new crisis.
Basis: Part 6 activation gate (Event 5 enters a state-transfer phase and a registered site is affected) and post-transfer reconciliation; the reconcile helper is the single point every bracketed transfer, release tranche and bounded callback already passes through, so no new scan or pulse is added.
Disposition: `implemented`; the collapse campaign itself `needs_live_game`.

### R2b-1. Credibility memory, the enforcement window and target cooldowns

Findings: `sov_nuclear_bombs_credibility` started at 0, was never clamped or decayed and had no bands; only the back-down AI read it (`< 10`, so its ×2.5 was always on); demonstrations, strikes after a refusal, kept settlements, unreachable threats and broken settlements never moved it, and the private signal's description promised a credibility gain it did not give.
Three source defects sat on the same path: `sov_nuclear_bombs_private_signal_sent` was never cleared, so the private signal worked once per campaign; accepting a partial settlement left `sov_nuclear_bombs_coercion_open` set, so after verification cleared the dossier pointers the dossier could neither be closed nor replaced except by a penalised back-down; and the target's answer cleared `sov_nuclear_bombs_ultimatum_pending` while the 45-day response mission kept running, so the mission's cancel check fired the next day and `sov_nuclear_bombs_cancel_ultimatum_response` overwrote an acceptance with a rejection and cleared the coercion target that the `chaosx.nr23.162` verification reads.
A refused demand also closed the dossier immediately, so the Union could never act on the refusal from the same dossier, and Part 9's per-country cooldown would have made a new dossier against the refuser impossible.
Decisions:
- Credibility is written only through `sov_nuclear_bombs_change_credibility` (temporary `sov_nuclear_bombs_credibility_delta`, clamped to `minimum`/`maximum`, -30/30) and decays by `decay_step` (2) toward `neutral` (0) in `sov_nuclear_bombs_apply_routine_maintenance`, the existing 30-day cycle; bands are `sov_nuclear_bombs_event_credibility_is_doubted` (below -5) and `_is_credible` (above 9), Uncertain between.
- Gains: demonstration +6 (public and wartime share the demonstration receipt), strike on the refusing government +10 (authorized strike and native raid alike), accepted demand +5 (existing `ultimatum_credibility_gain`), verified settlement +4 (`chaosx.nr23.162` success), private signal +2.
- Losses: back-down -8 (existing value) plus -2 Integrity and one `sov_nuclear_bombs_back_down_count` (Part 9 back-down farming); ultimatum on a state without delivery access -5 and `sov_nuclear_bombs_ultimatum_route_unproven`; abort or redirect of a prepared strike after the dossier's public ultimatum -6; a broken pending settlement -10 once (`sov_nuclear_bombs_record_settlement_violation`); a test failure -6 or accident -8 once public knowledge is at least Demonstrated; the collapse crisis opening with missing devices -8. The response-specific losses for exposure, foreign support, evacuation, sabotage and a nuclear counter-threat keep their values; the plain refusal and the delayed-to-timeout losses are removed, because the refusal now opens the enforcement window and the Union's own answer decides the cost.
- Demonstrations always detonate in the shared action contract, so Part 3's "failed public test" is read as a failed or accidental test once the arsenal is public; a concealed test seen by foreign observers joins it when the exposure item lands.
- A refusal (any non-accepting, non-partial answer, or silence when the response mission times out) keeps the dossier open with `sov_nuclear_bombs_ultimatum_refused` and starts `sov_nuclear_bombs_enforcement_window_mission` (60 days, `sov_nuclear_bombs_duration.enforcement_window`, `GFX_mission_sov_nuclear_mission_ultimatum_response` reused). Preparing a limited strike or a wartime demonstration ends the window; a landed demonstration sets `sov_nuclear_bombs_refusal_answered_by_demonstration`, lets "Issue a Public Ultimatum" renew the demand once and reopens the window; expiry runs `sov_nuclear_bombs_back_down` with `sov_nuclear_bombs_demand_lapsed`; a fallen or subject government closes the dossier without penalty.
- Target answers go through `sov_nuclear_bombs_answer_ultimatum`, which calls `remove_mission` (installed `effects_documentation.md`, "Removes mission without running complete or timeout effects") before resolving; the mission's own timeout still resolves silence as a refusal.
- `sov_nuclear_bombs_clear_dossier_threat_record` resets the private signal, public-ultimatum, refusal and route flags for each dossier; accepting a settlement (full or partial) clears `coercion_open` while the pointers stay for verification.
- A dossier that has carried a threat cannot be closed quietly: "Close the Coercion Channel" requires `NOT sov_nuclear_bombs_event_dossier_threat_made` and "Back Down" requires it (Part 9: no select-and-close cooldown clearing).
- Each government that refuses, settles or outlasts a demand gets `sov_nuclear_bombs_coercion_cooldown` for `coercion_cooldown` (120) days per ultimatum it has received, up to `coercion_cooldown_max` (360), as a timed flag built inside `hidden_effect`/`meta_effect` with an integer literal (R2-2 pattern); the selector's `target_trigger` and a separate custom tooltip, and `sov_nuclear_bombs_event_country_is_ai_coercion_candidate`, exclude it. The escalation per received ultimatum is Part 9's "escalating cooldown".
- AI (`sov_nuclear_bombs_ai`): private signal 1.20, ×1.40 while public knowledge is below Demonstrated; public ultimatum 1.10, ×1.30 with a confirmed arsenal (unchanged), ×0.50 while knowledge is below Demonstrated and no signal was sent, ×0.40 when Doubted, ×0.70 from the first back-down and again from `repeated_back_downs` (2); back-down 0.25, ×2.50 only when Doubted; wartime demonstration 0.80, ×1.50 after an unanswered refusal (was any resolved response) and ×1.50 when Doubted; limited strike 0.60, ×1.50 at war (unchanged), ×1.50 after a refusal; close 0.05. The limited strike's Evolution II gates, certification and separate final authorization are unchanged, so the refusal factor only matches Part 4's "the target refused a specific demand".
- Presentation: the category header adds "Credibility: Doubted/Uncertain/Credible" while a dossier or settlement is open (`GetSovietNuclearBombsCategoryCredibility`); the ultimatum and back-down descriptions end with the same band; no number is shown.
Source scenario walks: (1) neutral start, private signal (+2), ultimatum on a reachable state, refusal, limited strike lands on the refuser (+10): 12, Credible, dossier closed, refuser cooled for 120 days. (2) neutral start, two ultimatums refused and both withdrawn: -16 and two back-downs, Doubted; the AI ultimatum weight is 1.10 × 0.40 × 0.70 × 0.70 = 0.22 against a back-down weight of 0.625, and the score decays back to Uncertain (-4) after six maintenance cycles. (3) an ultimatum on a state beyond bomber range: -5 at once and the target sees an unproven route.
Probability: before sources frozen in `probability_source_snapshots/ai_surfaces_before_round2b_2026-10-05/`; one narrow `hoi4_probability_inspect` call (`decision_ai_will_do`, `source.path = common/decisions/023_sov_nuclear_bombs_decisions.txt`, `candidatePool` = the ultimatum, private signal and back-down decisions, no refresh) returned `INTERNAL_ERROR` with `artifactCount = 0` and was not retried.
Basis: Part 4 credibility memory, threat methods and partial settlements, Part 8 coercion-phase status, Part 9 threat-method AI, threat spam and back-down farming, the decision map's back-down and partial-settlement consequences, and the lead's round 2 decisions 3, 9 and 10.
Disposition: `implemented`; live window, cooldown expiry and AI pacing `needs_live_game`; MCP compare `blocked` (R2-10).

### R2b-2. Target answers to an ultimatum come from a situational assessment

Finding: every `chaosx.nr23.120` option had a fixed `ai_chance` (35/25/20/20/10/10/12/8/10), so an AI target answered a Soviet ultimatum at random whatever its war, protection or the Union's record, and "Seek foreign support" existed only for faction members.
Decision: each option base reads `sov_nuclear_bombs_response_ai.<option>_base` with the previous value, and stacking factors from the same category apply through bounded target-scope triggers in `023_sov_nuclear_bombs_event_triggers.txt` (`sov_nuclear_bombs_event_target_is_losing_to_union`, `_is_collapsing_before_union`, `_is_beating_union`, `_is_at_peace_with_union`, `_is_protected`, `_is_isolated`, `_has_nuclear_capability`, `_has_fragile_government`) and actor reads through the coercion actor event target (`sov_nuclear_bombs_event_response_threat_is_credible`/`_doubted`, `_arsenal_is_unproven`/`_employed`, `_command_is_unready`/`_divided`, `_route_is_unproven`, `_threats_are_empty`, `_was_signalled`, `_demand_is_limited`/`_raised`/`_maximum`/`_narrowed`/`_protection`/`_unearned_surrender`).
Proof is `sov_nuclear_bombs_event_arsenal_is_proven` (public demonstration, recorded combat use, or an observed test), not public knowledge, because the public ultimatum itself acknowledges the arsenal and raises knowledge to Demonstrated (the existing Part 3 "acknowledged device" rule); knowledge still marks a weapon used in war.
Protection reads `has_guaranteed = PREV` inside one `any_country` limited to majors; there is no recurring scan, only the evaluation when the AI picks an answer.
Foreign support keeps the faction-leader guarantee and otherwise picks one AI major through a single `random_country` with `sov_nuclear_bombs_event_country_is_available_guarantor` (major, AI, not SOV, not the target, not capitulated, not in the Soviet faction, not at war with the target, not already its guarantor). Restricting the new path to AI majors is an agent decision so another country's event never commits a human player.
The event text adds the named state and a one-line reading of the threat from the same triggers (`GetSovietNuclearBombsThreatAssessment`), so a human target sees what the AI weighs.
Source arithmetic (option shares; the shared factor sets are in the constants):
- ISOLATED_LOSING_MINOR (Credible, proven, surrender progress above 0.50, isolated, ceasefire at the default level, at war, no nuclear capability): accept 184.28 (63.4%), partial 50.70 (17.4%), delay 14.00, refuse 5.04 (1.7%), expose 10, support 4, evacuate 15.60, raid 7.00 of 290.62. Accept plus partial is 80.8% against 1.7% refusal; partial stays material; acceptance is below 100%. With a surrender demand instead of a ceasefire, accept is 59.1% and partial 19.5%.
- PROTECTED_STABLE (Uncertain, at peace, guaranteed by a major, Soviet protection demand): accept 3.67 (2.9%), partial 15, delay 20, refuse 39 (31.3%), expose 15 (12.0%), support 20 (16.0%), evacuate 12 of 124.67. Refusal, exposure and support together are 59.4%; acceptance is rare.
- UNTESTED_SECRET (Uncertain after the private signal, unproven, at war but not losing, isolated, ceasefire): accept 27.30 (16.8%), partial 32.50 (20.0%), delay 40 (24.6%, the most likely answer), refuse 24 (14.7%) of 162.80; the same case with a demonstrated weapon gives accept 33.5% and delay 12.3%.
- EMPTY_THREATS (two back-downs, so Doubted at -16, readiness 45, unreachable state) against the same baseline: refusal rises from 12.9% (20 of 155.60) to 52.4% (107.52 of 205.25) and acceptance falls from 35.1% to 2.8%.
- A surrender demand on a government that is no longer collapsing gives acceptance 1.0% (factor 0.02); raising the demand to level 4 cuts acceptance from 35.1% to 23.4%, and level 5 to 15.5%.
Human targets are unaffected because `ai_chance` only steers AI answers.
Probability: before source `probability_source_snapshots/ai_surfaces_before_round2b_2026-10-05/before_events.txt`; one narrow `hoi4_probability_inspect` call (`event_option_ai_chance`, `source.path = events/023_soviet_nukes.txt`, `candidatePool = ["chaosx.nr23.120"]`, no refresh) returned `INTERNAL_ERROR` with `artifactCount = 0` and was not retried.
Basis: Part 4 compliance logic, target response framework and target AI response, the probability scenarios `P23_COERCE_*`, README non-negotiable 4, and the lead's round 2 decisions 3 and 4; the accepted addendum is in Part 4 "Accepted compliance assessment (2026-10-05)".
Disposition: `implemented`; live answer distribution `needs_live_game`; MCP compare `blocked` (R2-10).

### R2b-3. Test results change Readiness by profile

Finding: a test success only set a flag, a partial yield and a failure only changed Integrity, and a public demonstration changed neither Readiness nor credibility, so the only Readiness from testing was the +6 at preparation and repeated tests cost nothing extra in purpose (Part 3 outcome families; Part 9 test farming).
Decision: `sov_nuclear_bombs_apply_test_readiness` (event effects) applies one change per recorded test or demonstration from new `sov_nuclear_bombs_tuning` keys: instrumented success `test_success_instrumented_readiness` 12, concealed success `test_success_concealed_readiness` 8, partial yield `test_partial_readiness` 4, failure `test_failure_readiness` -6, demonstration `demonstration_readiness` 15 (the demonstration's +6 credibility is R2b-1). The result is clamped to `value_min`..`value_max`.
Tests and demonstrations share a per-stage counter (`sov_nuclear_bombs_stage_test_uses`, reset when `sov_nuclear_bombs_evolution_stage` changes); once it passes `test_purpose_count` (1), a gain is divided by `test_repeat_divisor` (2) and `sov_nuclear_bombs_last_test_repeated` is set. Losses are never divided. The applied change after the clamp is kept in `sov_nuclear_bombs_last_test_readiness_change`.
The success, partial and failure report descriptions end with "Arsenal Readiness: <signed change>" and a repeat note; the instrumented, concealed and public decision descriptions state the gains from the constants.
Accidents keep their existing Integrity, serious-crisis and report handling and do not count toward the stage, and the D1 yield gate (`test_accident_catastrophic_integrity_threshold`) and the D2 delivery preflight are unchanged.
Source walk: Evolution I, Readiness 41 after preparation (+6): an instrumented clean result gives 53; a second test at the same stage gives +6 (half of 12) and the report says it taught less; a failure gives -6 whichever test it is; after Evolution II begins the next clean instrumented test gives the full +12 again.
Basis: Part 3 test outcome families and test profiles, Part 9 test farming, and the lead's round 2 decision 4.
Disposition: `implemented`; live report rendering `needs_live_game`.

### R2b-4. Exposure, the Suspected state, foreign observation and the counterintelligence sweep

Finding: public knowledge had four values with no Suspected state and no exposure score; concealed and instrumented tests never raised knowledge, nothing modelled foreign observation, the header had no security status, and the event doc listed a counterintelligence decision family that did not exist (the icon served only "Investigate the Test Failure").
Decisions:
- `sov_nuclear_bombs_public_knowledge` becomes unknown 0, suspected 1, private 2, demonstrated 3, used 4; every comparison already used the constant names (including the shared `chaos_meter_effects.txt` test-visibility check, which keeps its meaning), and the six knowledge writers now go through `sov_nuclear_bombs_raise_public_knowledge`, which never lowers knowledge. The unused tuning keys `public_reveal_knowledge` and `private_knowledge` are removed, as is the unused `sov_nuclear_bombs_ultimatum_prior_knowledge` from R2b-1.
- `sov_nuclear_bombs_exposure` (0..100, hidden) changes only through `sov_nuclear_bombs_add_exposure` with `sov_nuclear_bombs_exposure` constants at the listed seams: reactor queued +4, reserve dispersal departure +5, assembly start +4, test preparation instrumented +3 or concealed +5, test result instrumented detonation +6, concealed detonation +12, failure +3, accident +20, final-authorization hold +5, collapse opening +25 (Part 3: concealed tests most, instrumented least, accidents and collapse high). The sweep removes 20 and cancelling a test while watched removes 8.
- Thresholds: watched 25, suspected 35, penetrated 55, confirmed 70, detected 85. Crossing suspected or confirmed advances knowledge and queues one `chaosx.nr23.107` report naming the source (`sov_nuclear_bombs_exposure_source`); reports on the same day merge. Only Suspected can fall back to Unknown, when a counter-measure takes exposure below 35 (Part 3: a cover-up works while the arsenal is Unknown or Suspected; a major's private proof and anything public stay).
- Foreign observation: a detonating secret test (success or partial yield) rolls observation with weight equal to exposure after the test (halved for an instrumented test, floor 1) against the remainder of 100. Observed sets `sov_nuclear_bombs_test_observed` (proof of the weapon for R2b-2) and Confirmed in private; at 85 or more the test is detected beyond denial: Demonstrated, `sov_nuclear_bombs_public_arsenal_confirmed`, the world threat refresh and `chaosx.news.235` (new, in the shared `events/_chaosx_news.txt`, reusing `GFX_news_event_sov_nuclear_public_test`). Accidents and failures add exposure but are not rolled.
- "Order a Counterintelligence Sweep" (`sov_nuclear_bombs_counterintelligence_sweep`): command cost, 90 days (`sov_nuclear_bombs_duration.counterintelligence_sweep`), visible on the custody and test boards while exposure is at least watched and the arsenal is not public, a project flag in `sov_nuclear_bombs_event_no_active_project`, AI 1.00 ×2.00 when penetrated ×1.50 when Suspected; `sov_nuclear_bombs_event_ai_needs_counterintelligence` joins the router's custody duty so the AI reaches it from custody.
- Once exposure is penetrated, a failed or accidental secret test costs credibility as a public one does (R2b-1).
- Presentation: the fourth header line reads "Posture: ..., public knowledge: ..., security: secure/watched/penetrated/public", so the header keeps Part 8's four lines; the knowledge selector gains "Suspected".
Source walk: an Evolution II opening queues four reactors (16, secure); a concealed test preparation (21) and detonation (33, watched) leave the arsenal Unknown with a 33% observation roll; the next dispersal departure (38) makes it Suspected with a report naming rail movements; a sweep (18) returns it to Unknown. An instrumented test from 18 adds 3 and 6 (27) and rolls at 13%.
Basis: Part 3 public knowledge states, evidence and exposure, test profiles and foreign observation; Part 8 header limit; the lead's round 2 decisions 3 and 6.
Disposition: `implemented`; live roll frequency and report timing `needs_live_game`.

### R2b-5. Foreign reactions, arms-race hooks and the Evolution I foreign package

Finding: outside the news events no country but the Union ever reacted to the arsenal being found, demonstrated or used, and none of Part 3's arms-race hook moments was recorded, so Event 23 was nearly invisible to non-Soviet players.
Decisions:
- Six hooks record once each as global flags with the Soviet actor's id in `global.<flag>_actor`: private confirmation (knowledge first at least Confirmed in private, recorded inside `sov_nuclear_bombs_raise_public_knowledge`), first public test (demonstration receipt or a secret test detected beyond denial), first public ultimatum (`sov_nuclear_bombs_send_ultimatum`), first combat use (combat receipt and native raid record), first breakaway crisis (`sov_nuclear_bombs_open_collapse_recovery`) and first major exchange (`sov_nuclear_bombs_open_major_exchange`). They fire no other event and grant no technology; Part 7 carries the accepted hook list.
- Majors outside the Soviet camp (`sov_nuclear_bombs_event_country_receives_major_report`) receive one strategic report per stage through a one-time `every_country` dispatch guarded by a global flag: `chaosx.nr23.190` when knowledge first equals Confirmed in private, `.191` when it first reaches Demonstrated, `.192` when Evolution I is recorded (including an opening that starts at Evolution I). There is no periodic scan (CLAUDE.md 1.8, lead decision 7).
- Answers (shared scripted effects): intelligence (`add_intel` on the Union, 10 civilian and 10 air force, file-scoped `@` values because the installed documentation shows only plain numbers), research priority (timed idea `sov_nuclear_bombs_foreign_atomic_priority`, +25% nuclear-category research for 365 days), air defence (timed idea `sov_nuclear_bombs_foreign_air_defence`, +15% static anti-air damage, +10% hit chance and +10% radar research for 365 days), and a guarantee to a minor neighbour of the Union, preferring one at war with it or under a Soviet demand or cooldown, through one bounded `random_neighbor_country`. Idea values are `@` constants in the ideas file like the existing posture spirits; no answer grants a technology (vanilla `research_bonus` precedent: `BUL_uranium_concession_agreement`).
- AI (`sov_nuclear_bombs_foreign_ai`): intelligence 30 (×1.50 on private proof), research 25 (×1.80 in the race, ×2.00 with atomic research, ×0.40 without), air defence 20 (×1.50 on the public arsenal, ×1.50 as a Soviet neighbour, ×1.50 at war with the Union), guarantee 15 (×1.50 on the public arsenal, ×1.50 as a faction leader, ×0.50 at war).
- Soviet faction partners and subjects receive `chaosx.nr23.193` at the first combat use: stand with Moscow (+5% war support, -3% stability; AI 60, ×1.50 for a subject, ×1.30 communist) or keep a distance (+3% stability, -3% war support, and a non-subject partner leaves the faction; AI 40, ×1.50 democratic, ×1.50 at peace).
- New country events reuse Event 23 report pictures and the ideas reuse vanilla icons (asset manifest "Picture reuse for the round 2 report and news events").
Source walk: a concealed test observed abroad raises knowledge to Confirmed in private, records the private-confirmation hook and sends `.190` to, for example, Germany, the United Kingdom, France, Italy, Japan and the United States; an AI Germany with atomic research weighs research 50, intelligence 45, air defence 20 and a guarantee 15. A later public demonstration records the first-public-test hook and sends `.191` once; Evolution I sends `.192` once. The first strike sends `.193` to Mongolia as a subject and to any faction partner.
Probability: these weights are new, so there is no before source; one narrow `hoi4_probability_inspect` call (`event_option_ai_chance`, `source.path = events/023_soviet_nukes.txt`, `candidatePool = ["chaosx.nr23.190"]`, no refresh) returned `INTERNAL_ERROR` with `artifactCount = 0` and was not retried. The counterintelligence sweep weight of R2b-4 is likewise new and covered by the same blocked route.
Basis: Part 3 foreign reaction framework and arms-race hook activation, Part 5 Evolution I foreign package, Part 7 Event 32 and Event 76 links, and the lead's round 2 decisions 3, 7 and 8.
Disposition: `implemented`; live dispatch and AI answers `needs_live_game`.

### R2b-6. Five secrecy incidents

Finding: Part 3's secrecy incidents (missing physicist, compromised rail manifest, foreign aircraft over the site, contaminated workers, captured device component) were absent from the source and untracked in the plans, so the hidden arsenal phase had no dilemma between secrecy, Readiness and Integrity.
Decisions:
- `sov_nuclear_bombs_roll_secrecy_incident` (input `sov_nuclear_bombs_incident_request`) runs only at existing seams: reactor completion (`sov_nuclear_bombs_register_completed_reactor`) and assembly completion for the physicist; the dispersal departure and the recall convoy for the manifest; secret test preparation (`sov_nuclear_bombs_prepare_test`) for the aircraft; a test accident or partial yield for the workers; and the Event 5 reconciliation of a transferred or missing registered depot for the component. No pulse or scan is added.
- Chance in percent: `chance_base` 4 plus exposure × `exposure_weight` 0.25 plus (100 − Integrity) × `integrity_weight` 0.20, clamped to 4..45, rolled with `random_list` against the remainder of 100; a hit sets the shared timed flag `sov_nuclear_bombs_incident_cooldown` for `cooldown_days` 180 through `hidden_effect`/`meta_effect` with an integer literal (R2-2 pattern) and fires `chaosx.nr23.111`..`115` after one day. Example: exposure 40 and Integrity 60 give 22%; a secure program at the opening Integrity 92 gives about 6%.
- Each report has four answers from Part 3. Costed answers pay through the existing helpers (security: recover the physicist, treat the workers; diplomatic: accuse the hosts, negotiate the component; logistics: decoy train; command: recovery raid), and each costed option has a free alternative. Readiness and Integrity changes come from `sov_nuclear_bombs_incident` keys and are clamped; exposure changes only through `sov_nuclear_bombs_add_exposure` (with the incident's own source, including the new `defector` source for the physicist) and knowledge only through `sov_nuclear_bombs_raise_public_knowledge` (accusation, denial and the safety admission make the program at least Suspected; accepting the physicist's loss gives a major private proof). Effects run in `hidden_effect` behind plain custom tooltips, so no internal variable or exposure number is shown.
- Accelerating the watched test adds `accelerate_accident_bonus` (6) to the accident weight of its outcome; inviting observers makes a detonating secret test a public demonstration (Demonstrated, credibility +6, first-public-test hook, `chaosx.news.230`) without changing the action contract; the recovery raid opens the custody board if it is closed and moves no device (ledger helpers untouched).
- AI (`sov_nuclear_bombs_incident_ai`): bases recover 40, accuse 15, purge 20, accept 25; reroute 30, continue 20, decoy 25, temporary site 25; cancel 20, accelerate 25, invite 20, deny 35; isolate 35, confine 20, admit 25, destroy records 20; raid 30, negotiate 25, industrial claim 20, redesign 25; doctrine factors 1.50 (Party purge 2.00) and low Integrity 1.50, invite ×1.50 when credibility is Doubted.
- Found on the same path: `sov_nuclear_bombs_cancel_test` left the 120-day test window running, so a new test could not activate its own window and the old timeout would resolve it early, and it kept the instrumented or concealed flag for the next test. It now removes the window with `remove_mission` (only when the window is not already ending through its own cancel trigger) and clears the profile, acceleration, observer and wartime-demonstration flags.
- Writing follows Part 3: concrete scenes, no humour about contamination; pictures reuse the Event 23 reports (asset manifest).
Probability: the incident weights are new (no before source); the MCP route is blocked as recorded in R2b-5 and R2-10, and no further attempt was made for this surface.
Basis: Part 3 secrecy incidents, evidence and exposure, news and report presentation and writing direction; the lead's round 2 decisions 3, 7 and 8.
Disposition: `implemented`; live incident frequency and option balance `needs_live_game`.

### R2b-7. False warnings and ambiguous detection

Finding: Part 5's rare possible-launch incident and acceptance scenario H's "suspected false warning" case had no source. Two hotline defects sat on the path a warning needs: the retaliation window mission's cancel trigger required a stand-down offer or a valid major strike target, so a hotline opened by "Establish an Emergency Hotline" was cancelled on the next check (with the abort readiness loss) before a stand-down could be offered; and the partner's answer in `chaosx.nr23.163` resolved the hotline while the window mission kept running, so its cancel check ran `sov_nuclear_bombs_cancel_retaliation_window` over the recorded answer.
Decisions:
- `sov_nuclear_bombs_roll_false_warning` runs from the existing 30-day block of `on_daily_SOV`, after routine maintenance. It needs the valid actor at Evolution III, no moratorium, no open warning window, Chaos at least `minimum_chaos` (900) and an enemy nuclear major (`sov_nuclear_bombs_event_can_raise_false_warning`), and rolls `chance` (5) of 100.
- A warning saves one enemy nuclear major as `sov_nuclear_bombs_warning_suspect`, draws the window length uniformly between `window_minimum_days` (7) and `window_maximum_days` (21), keeps it in `sov_nuclear_bombs_warning_window_days` and sets the timed flag `sov_nuclear_bombs_false_warning_window` through `hidden_effect`/`meta_effect` with an integer literal, then fires `chaosx.nr23.141`.
- Answers: wait (+2 Integrity, default), disperse (logistics cost, +6 Readiness, -2 Integrity), contact the suspect (diplomatic cost; `sov_nuclear_bombs_prepare_hotline`, whose partner selection now prefers the suspect during the window), prepare a response (+4 Readiness, -3 Integrity, timed `sov_nuclear_bombs_warning_response_prepared` for the window, which joins `sov_nuclear_bombs_event_ai_has_retaliation_duty`, and at least a Nuclear Confrontation through `sov_nuclear_bombs_advance_exchange_stage`), and act now (only when `sov_nuclear_bombs_event_can_act_on_warning`: the window, `sov_nuclear_bombs_enemy_launch_preparation_verified` and the staged `sov_nuclear_bombs_event_prospective_first_use_gate`; -4 Integrity and a phase request to the retaliation board, never `launch_nuke`).
- AI (`sov_nuclear_bombs_false_warning_ai`): wait 70, disperse 12, contact 10, prepare 8, act 1; when the command is damaged (`sov_nuclear_bombs_event_command_is_damaged`: low Integrity or Moscow lost) act ×40 and, if acting is offered, wait ×0.30. Without damage the AI waits 69% of the time and takes a non-escalating answer otherwise; with damage and the gate it acts 44% of the time, and release still needs a marked state, preparation, certification and final authorization. No chance can start a nuclear war by itself.
- Hotline fixes: `sov_nuclear_bombs_hotline_open` joins the moratorium and stand-down offer exemptions in both clauses of the window's cancel trigger, so a hotline window runs to its timeout or to the partner's answer; `chaosx.nr23.163` calls `sov_nuclear_bombs_answer_hotline`, which removes the window mission (`remove_mission`) before `sov_nuclear_bombs_resolve_hotline`.
Probability: new weights (no before source); the MCP route is blocked (R2b-5, R2-10) and no further attempt was made.
Basis: Part 5 false warnings and ambiguous detection, retaliation timing and exchange actions; Part 9 retaliation AI ("a suspected launch without confirmation should normally trigger dispersal, hotline, and preparation, not immediate release"); Part 10 scenario H; the lead's round 2 decisions 3 and 7.
Disposition: `implemented`; live warning frequency and the hotline window `needs_live_game`.

### R2b-8. Breakaway bargaining and the missing collapse actions

Finding: joint custody was a one-sided 120-day Soviet mission, the holder of a depot had no say in it or in a recall, and Part 6's breakaway actions (conceal the devices, request foreign removal help, dismantle under observation), the Soviet "Reinforce the depot" and bounded foreign intervention did not exist.
Decisions:
- `sov_nuclear_bombs_open_custody_talks` (from "Negotiate Joint Custody" and "Recall the Devices") saves the depot as `sov_nuclear_bombs_custody_talks_site` and sends its recorded holder (`sov_nuclear_bombs_site_holder`) `chaosx.nr23.171`. Joint custody applies the joint custody state at once; return moves the devices through `sov_nuclear_bombs_restore_site_to_soviet` (the recall and the talks already require a Soviet force in the depot's state, so the helper's Soviet-control condition holds) and adds `negotiated_return_integrity` (14, above the raid's 10; Part 6: "a negotiated return improves Integrity more than a forced raid"); refusal sets the failure flags. Every answer removes the running Soviet mission first (`sov_nuclear_bombs_close_custody_talks_mission`), the pattern of R2b-1.
- AI holder: joint 45, return 30, refuse 25; refusal ×2.50 when operationalization at the depot is imminent and ×2.00 with a major backer (`sov_nuclear_bombs_event_target_is_protected`), which also halves the return. Bargaining is 75% by default (Part 4 target AI: a breakaway holding devices should prefer bargaining).
- "Reinforce the Depot" (Soviet): security cost, once per depot (`sov_nuclear_bombs_site_reinforced`), needs the existing Soviet security force; +6 Integrity and a timed `sov_nuclear_bombs_site_garrisoned` (180 days) that blocks the holder's start of technical access at that depot, with technical access already under way extended by 60 days through `add_days_mission_timeout` (installed `effects_documentation.md`; days injected as a literal). AI 0.90, ×2.00 when access is under way.
- "Conceal the Devices" (holder): logistics cost; a timed `sov_nuclear_bombs_site_concealed` (180 days) blocks Soviet recall and raids on the depot (custom tooltips) and cancels a recall or raid already moving (the rail corridor operation is not affected); the depot record becomes disputed; a 10% chance marks the depot missing through `sov_nuclear_bombs_mark_site_missing` (the holder's own accounting fails). AI 0.50, ×2.00 when a Soviet recall or raid is moving on it.
- "Dismantle Under Observation" (holder): security cost; the holder mission `sov_nuclear_bombs_breakaway_dismantlement_mission` (180 days) ends by `sov_nuclear_bombs_mark_site_dismantled`, clears the holder's depot selection and progress flags and records a custody resolution for the Union. AI 0.20, ×2.00 without atomic research.
- "Request Foreign Removal Assistance" (holder): diplomatic cost; one major outside the Soviet faction and not at war with the holder (`sov_nuclear_bombs_event_country_is_removal_partner`, one bounded `random_country`) answers `chaosx.nr23.172`. Accepting starts the same dismantlement with `sov_nuclear_bombs_breakaway_foreign_removal`, which also needs the rail route (`sov_nuclear_bombs_event_breakaway_dismantlement_is_valid`); the major never gains ownership; `chaosx.nr23.173` tells the holder. AI major: accept 50 (×1.50 as a Soviet neighbour, ×1.50 at war with the Union), decline 50 (×1.50 at war).
- The new holder mission joins `sov_nuclear_bombs_event_no_active_project`.
- One-device conservation: only the existing ledger helpers move devices (restore, dismantle, missing); joint custody and concealment change custody state and flags only.
- Icons reuse the existing storage-hardening, concealed-test, joint-custody, dismantlement and dismantlement-inspection sprites; events reuse the breakaway custody report.
Probability: new weights; the MCP route is blocked (R2b-5, R2-10) and no further attempt was made.
Basis: Part 6 Soviet collapse and breakaway decision families and foreign intervention, Part 4 target AI response, Part 9 Soviet Collapse AI, and the lead's round 2 decision 3.
Disposition: `implemented`; collapse campaign behaviour `needs_live_game`.

### R2b-9. Retaliation windows follow the situation

Finding: the retaliation window mission used `constant:sov_nuclear_bombs_duration.hotline_mission` (30 days) for both the hotline and the authorized response, so Part 5's retaliation timing (3 to 14 days with intact command, 7 to 21 for a suspected launch, 14 to 30 with command damage, shorter at Expanding Exchange) was not met; R2-6 left the shortening `unresolved` because the two windows shared one timer.
Decision (lead round 2 decision 5): the mission reads `days_mission_timeout = var:sov_nuclear_bombs_retaliation_window_days` (vanilla `CHI_decisions.txt` line 6454), a normal variable set before every activation. `sov_nuclear_bombs_prepare_hotline` sets `hotline_mission` (30, unchanged). `sov_nuclear_bombs_authorize_retaliation` calls `sov_nuclear_bombs_set_response_window_length`: `retaliation_intact_command` (10), `retaliation_command_damage` (21) when `sov_nuclear_bombs_event_command_is_damaged` (Integrity below the low threshold or Moscow lost) or a custody collapse disputes authority, else `retaliation_suspected_launch` (14) while a launch-warning window is open without confirmed enemy use. All three sit inside Part 5's ranges.
`sov_nuclear_bombs_advance_exchange_stage` detects the step into Expanding Exchange and calls `sov_nuclear_bombs_shorten_response_window` on the Union: an open, non-hotline window loses `retaliation_expanding_shortening` (5) days through `add_days_mission_timeout` (negative days injected as a literal), limited so that at least `retaliation_window_floor` (3) days remain (tracked by `sov_nuclear_bombs_retaliation_window_end_day`). A window at its last day is not cut, so it never opens and resolves on the same tick.
R2-6's window-shortening sub-item is now `implemented`; Part 5's accepted exchange ladder records the change.
Basis: Part 5 retaliation timing and exchange stages, the lead's round 2 decision 5 (variable timeout and `add_days_mission_timeout`, installed `effects_documentation.md` line 1051).
Disposition: `implemented`; negative `add_days_mission_timeout` and the live window lengths `needs_live_game`.

### R2b-10. Readiness wears down without a delivery force

Finding: routine maintenance checked only stockpile against reactor capacity, missing devices and disputes, so a Union that lost every strategic bomber, its fuel or its air bases kept full Readiness indefinitely (Part 2: Readiness declines over time when delivery is lost, with a clear tooltip and no free replacement).
Decision: `sov_nuclear_bombs_apply_routine_maintenance` (the existing 30-day cycle) adds `delivery_loss_readiness` (-3) while `sov_nuclear_bombs_event_delivery_force_is_missing` holds (a phase past the opening, a chosen custody doctrine and no `sov_nuclear_bombs_event_has_delivery_route`, the D2 preflight), only while Readiness is above `delivery_loss_readiness_floor` (10) and clamped at that floor; it sets `sov_nuclear_bombs_delivery_force_missing` for the cycle. No aircraft or equipment is granted and nothing else in maintenance changes (the regular +1 or over-capacity change still applies first, so the net loss is 2 per cycle under normal capacity).
The category header's readiness line adds "(no bombers, fuel or air base to deliver the weapons; readiness is falling)" while the condition holds, read live through `GetSovietNuclearBombsDeliveryStatus`.
Basis: Part 2 delivery-force loss, D2, and the lead's round 2 decision 4.
Disposition: `implemented`; live erosion pace `needs_live_game`.
