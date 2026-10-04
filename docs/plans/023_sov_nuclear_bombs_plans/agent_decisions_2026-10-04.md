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
