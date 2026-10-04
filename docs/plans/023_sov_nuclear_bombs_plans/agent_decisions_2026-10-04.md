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

- The router's Evolution IV first-use candidate (`sov_nuclear_bombs_event_ai_has_first_use_candidate`) does not test bomber reach, while the selector gives unreachable states zero AI weight. If every candidate state lies outside the delivery ceiling, the AI holds the retaliation board without marking a target until the emergency ends. Disposition: `unresolved`; it needs a launcher-from-ROOT variant of `sov_nuclear_bombs_event_state_has_delivery_access`, and live evidence of how often it occurs (`needs_live_game`).
- The AI reaches certified delivery crews only with ten deployed strategic bombers (D2). No Event 23 AI strategy raises Soviet strategic bomber production; the vanilla default ratio applies. Part 5 allows ("may") such a production shift. Disposition: `unresolved`; a bounded `ai_strategy` would need its own probability baseline once the MCP route works.
- A refunded vanilla raid leaves its booked device in the expended bucket while the native stockpile holds a surplus (D3 tolerance); it does not count as combat use or affect the achievements. Disposition: `accepted` under D3.
