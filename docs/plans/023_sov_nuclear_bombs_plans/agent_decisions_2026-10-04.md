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
