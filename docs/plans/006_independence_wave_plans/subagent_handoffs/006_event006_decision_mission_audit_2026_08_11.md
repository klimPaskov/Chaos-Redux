# Event 006 decision and mission audit — current worktree — 2026-08-11

## Verdict

This was a read-only source audit of Event 006 decisions, missions, timed objectives, categories, costs, AI gates, cancellation and cleanup, localisation surfaces, and exploit risks. No gameplay, decision, mission, AI, trigger, constant, localisation, or GUI source was changed.

The decision and mission surface is structurally healthy in source, with one material specification mismatch that should be resolved by the owner before this event is called complete: DM-01 currently models a garrison commitment, but the accepted matrix and mechanics specification also require equipment and an isolated-capital train or truck burden. This is a design/source reconciliation issue, not a safe tiny patch.

Current weighted-AI certification is unresolved. The mandatory probability subaudit is recorded in `006_event6_decision_mission_probability_audit_current_2026_08_11.md`; every valid current `hoi4.probability_inspect` path failed with `ARTIFACT_MANIFEST_INVALID` / “Artifact provenance manifest is invalid”, and an absolute-path retry returned `INTERNAL_ERROR` / “Unexpected internal error”. No current normalized probability, ranking, timing, sweep, comparison, dominance, starvation, or exploit-safety claim follows.

## Scope and authority

The audit used `common/decisions/006_independence_wave*.txt`, all matching Event 006 category files, the shared decision constants and scripted triggers, the current source-of-truth map, and the accepted decision/missions matrix.

The design authority is `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` (80 rows) together with `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`. The current implementation status remains HOLD/PARTIAL in `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.

I read `AGENTS.md`, `.agents/skills/hoi4-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`. I also consulted the required offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding, plus the installed vanilla documentation for effects, triggers, modifiers, script concepts, and script math.

## Severity-ranked findings

### P1 — DM-01 cost/requirement mismatch with the accepted specification

The accepted matrix row `DM-01` requires “control and supply capital with assigned divisions” and lists “tied divisions, infantry and support equipment, trains if isolated”; its duration band is 30–75 days and failure includes relocation, legitimacy loss, and faction pressure (`docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv:2`). The mechanics specification repeats the objective and costs at `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md:411-438`.

The implementation at `common/decisions/006_independence_wave_decisions.txt:23-65` has the correct capital-control and cancellation gates, a 75-day timeout, failure deltas, one-shot cleanup, and urgent AI, but its only material requirement is `independence_wave_secure_provisional_capital_garrison_satisfied` (`common/decisions/006_independence_wave_decisions.txt:33-38`). The helper at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:540-562` checks force tier by division count; it does not check supply, infantry equipment, support equipment, or trains/trucks.

This is not an accidental click-cost omission: the 2026-08-02 decision/missions matrix audit explicitly accepted “garrison commitment, no click cost” for DM-01. The parent should therefore choose one of two explicit resolutions: update the active spec/matrix to state that DM-01 intentionally uses a garrison-only commitment, or implement the bounded material commitment with a dynamic availability gate, player-facing custom cost/blocked/tooltip localisation, payment at activation, and rollback/cancellation behavior. Do not add an ad hoc flat political-power cost.

### P2 — Current AI/probability balance evidence is blocked

The current 44-file Event 006 source inventory contains 642 source-level `ai_will_do` blocks and 39 category files, but source counts are not runtime candidate pools. The required probability route failed before source parsing with the exact manifest error above; the absolute-path retry failed with `INTERNAL_ERROR`. Historical artifacts in `006_event6_decision_mission_probability_audit_current_2026_08_11.md` are explicitly stale, incomplete, and score-only.

No claim can currently be made that an urgent decision dominates a package mission, that a crisis mission starves another choice, that cooldowns produce a desired timing distribution, or that a weighted exploit loop is absent under real cadence and external modifiers. Repair/regenerate the workspace artifact provenance manifest, then rerun inspect-first probability evaluations with complete typed scenario state and the same named scenarios for any later compare.

### P3 — GUI MCP refresh is blocked, but existing read-only evidence is sufficient for source scope

Fresh `hoi4.gui_inspect`/`hoi4.gui_render` attempts for the Statehood Ledger and formable state-puzzle surfaces timed out in the code host. Existing read-only artifacts remain available in prior handoffs, including `006_decision_mission_audit_v5_2026_07_25.md` for `independence_wave_status_window` and `006_iw031_decision_final_active_audit_2026_08_10.md` for the current grouped formable state puzzle. The retained artifacts show the expected decision-owned presentation surfaces and aggregate workspace diagnostics; no narrow layout or button patch is justified by the current source review.

### P3 — Package cost suffixes are a convention follow-up, not a confirmed engine defect

An initial broad scan found package-specific base cost labels without `_blocked` or `_tooltip` siblings, but the latest Kosovo and Ruthenia localisation audits state that all direct `custom_cost_text` consumers are complete and the source does not reference those suffixes. Treat this as optional naming consistency only; do not report it as a missing runtime localisation defect without a direct source consumer.

## Static decision and mission inventory

The current source contains 44 Event 006 decision files, 39 Event 006 category files, and 642 `ai_will_do` blocks. A structural timed-block scan found 591 decision-like blocks, 74 `days_mission_timeout` blocks, 407 `days_remove` blocks, and 20 selectable timed missions. The different totals are expected because the first count is source-level AI blocks while the second parser counted top-level decision-like blocks and timed fields.

Every selectable timed mission found in the scan has an AI declaration. Every timed block has an `available` field and a completion, timeout, or removal path. No current `days_mission_timeout` block has a `visible` field, so the earlier inert-visible-mission finding is closed in the current source. Eight package deadline missions intentionally omit AI because they are internal auto-only response/deadline blocks with `activation`/`available = { always = no }`; for example, `independence_wave_form01_complete_first_integration_session` is at `common/decisions/006_independence_wave_form01_02_04_decisions.txt:176-187`. This is accepted design, not an AI omission.

No duplicate decision IDs were found by the source scan. Nineteen ordinary project/removal blocks lack an explicit `cancel_trigger`; their current route/target gates are static project contracts and older package audits treat them as intentional. Internal auto-deadline missions do carry cancellation and cleanup. Any future route with dynamic host, capital, target, or network invalidation should add a narrow cancel trigger rather than relying on `days_remove` alone.

## Category lifecycle notes

The shared categories in `common/decisions/categories/006_independence_wave_categories.txt` expose founding, government, recognition, security, host relations, patron, network, league, borders, formables, and high-chaos surfaces with phase, activation, living-former-host, regional, unlock, map-highlight, or scripted-GUI gates. The crisis category in `common/decisions/categories/006_independence_wave_crisis_categories.txt:8-16` is gated by pressure and an active crisis mission. Category-level visibility is not being used as the sole safety gate; each decision supplies its own activation and availability checks.

The current source uses active-project caps, route locks, one-shot flags, target persistence, and cleanup helpers. Founding, government, league, border, formable, and high-chaos families are therefore bounded by lifecycle state rather than a passive always-available political-power store.

## Mission quality notes

DM-01 is the only accepted row with a material requirement mismatch. Its owner, capital target, 75-day duration, urgent AI, failure deltas, and capital/garrison cancellation are present; supply/equipment/train burden remains unresolved as described above.

DM-02 and DM-03 use the administration cost palettes and 150-day founding duration, with control and stability gates, timeout outcomes, cancellation, and one-shot cleanup (`common/decisions/006_independence_wave_decisions.txt:68-179`). DM-03 is deliberately auto-started and has no direct AI choice because it is a census step after DM-02.

DM-04 through DM-16 use the shared duration constants, route locks, administration/security/material costs, and explicit success or failure ledgers. Current constants are centralized in `common/script_constants/006_independence_wave_decision_constants.txt:10-28`.

DM-17 and DM-18 are security projects with control/material gates and bounded state targeting. DM-18 is a 120-day state project and rewards a finite infantry/support-equipment package on success (`common/decisions/006_independence_wave_decisions.txt:908-994`); target-control loss cancels it.

DM-22 is the only decision-owned emergency unit spawn in the shared file. It requires the major security cost, records a 180-day raised flag, has urgent AI, and is removed by professionalization/origin cleanup (`common/decisions/006_independence_wave_decisions.txt:1121-1172`). The finite flag and later cleanup prevent a free repeatable unit loop.

DM-41 consumes one safe reserve channel, records the reserve, and applies a 180-day cooldown through the safe-reserve helper (`common/decisions/006_independence_wave_decisions.txt:2138-2162`; helper definitions near `common/decisions/006_independence_wave_decisions.txt:282-291` and `378-416`). It cannot double-count a channel during the cooldown.

DM-45 through DM-47 are strategic league preparation and charter actions with route, compliance, standing, active-league, and timeout checks (`common/decisions/006_independence_wave_decisions.txt:2540-2592`). DM-60 and DM-61 validate a live target and clear target state on resolution; DM-62 is a 45-day mutual-defense project whose target and authorization are cleared on cancellation or matching war (`common/decisions/006_independence_wave_decisions.txt:2753-2965`).

The crisis mission is a single selectable 120-day mission with a concrete pressure cost, timeout resolver, pressure-loss cancellation, requester-loss handling, cooldown, and retry cleanup (`common/decisions/006_independence_wave_crisis_decisions.txt:10-40`; constants in `common/script_constants/006_independence_wave_crisis_constants.txt:29-33`). The current crisis allocator audit found no passive store or stale queue loop.

## Cost and requirement clarity

The generic cost palette is centralized in `common/script_constants/006_independence_wave_decision_constants.txt:68-142` and consumed through scripted triggers and effects in `common/scripted_triggers/006_independence_wave_decision_triggers.txt:261-290` and the corresponding Event 006 decision effects. Costs use administration, security, diplomatic, strategic, network, and material commitments; there is no generic flat political-power exchange in the audited surface.

The finite DM-18 equipment reward, DM-22 emergency force flag, DM-41 channel consumption, target-specific DM-60/61/62 actions, and crisis queue cooldowns provide concrete anti-farming boundaries. The only high-priority cost clarity gap is DM-01’s missing equipment/supply/train layer.

Long raw triggers are mostly hidden behind custom cost and scripted trigger keys. A later localisation pass may improve a few long target/route tooltips, but the current package audits found no unresolved direct consumer key in the accepted scope.

## AI validity and route-lock notes

Every selectable mission has an `ai_will_do` block in the current scan, and urgent/high/standard/low/very-low priorities are centralized as script constants. Positive AI scores on auto-only `available = { always = no }` missions do not make them clickable and must not be interpreted as live dominance evidence.

Targeted decisions validate active/live countries, state control, self/war restrictions, route membership, former-host state, network/league phase, formable prerequisites, and active-project locks. Immediate DM-61 is safe because it validates the target and records the ground in one transaction; it does not need a long-lived cancellation path.

The KAR/CRI source contains deliberate factor-zero fail-closed gates for foundation, ledger, material/manpower/security, and diplomatic floors. Whether these gates are too restrictive is unresolved until typed probability scenarios are available. RUT’s `corridor_priority` constant is currently a source-consistency follow-up because its strategy source does not consume it; this is not a proven runtime balance defect.

## Localisation and tooltip notes

The older accepted audit found complete base/blocked/tooltip triplets for 133 custom-cost keys. Current package-inclusive scans find the direct base consumers; latest Kosovo and Ruthenia audits report no missing direct consumer keys. The optional suffix naming discrepancy described above should not block the event.

Decision names, descriptions, custom-cost labels, timeout outcomes, and target/tooltips are wired for the current source. Any future DM-01 material-cost implementation must add its cost, blocked, and tooltip localisation in the same change.

## Cleanup and exploit-risk notes

No free-resource, repeatable-unit, war-goal-spam, core-spam, factory-farming, or passive political-power loop was found in the audited Event 006 surface. Existing bounded mechanics are:

- DM-22’s one-shot emergency formation and later professionalization/origin cleanup.
- DM-18’s target/state control gate and finite success reward.
- DM-41’s first-safe-channel consumption and cooldown.
- DM-60/61/62 target serialization, resolution, cancellation, and target cleanup.
- Package project active-operation locks, route/host/capital cancellation where dynamic invalidation exists, and one-shot completion flags.
- Crisis pressure, requester-loss, retry, queue, and cooldown cleanup.

Runtime exploit proof remains blocked with the probability MCP manifest error; this is an evidence gap, not a source-confirmed exploit.

## GUI evidence and scope boundary

The shared Statehood Ledger and formable state-puzzle are decision-owned presentation surfaces. Existing mandatory read-only artifacts are retained in `006_decision_mission_audit_v5_2026_07_25.md`, `006_decision_mission_post_dm58_deadline_reaudit_2026_07_28.md`, `006_decision_engine_value_cost_gate_fix_2026_08_03.md`, and `006_iw031_decision_final_active_audit_2026_08_10.md`. Fresh inspect/render calls timed out, so no new artifact or GUI rewrite was attempted. The aggregate diagnostics do not identify a local layout defect tied to the decision logic.

## Recommended owner actions

1. Resolve DM-01 in the active spec: either explicitly accept the existing garrison-only/no-click-cost design, or implement the bounded infantry/support-equipment and isolated train/truck commitment with dynamic affordability, payment, tooltip, and cancellation rollback.
2. Repair/regenerate the workspace artifact provenance manifest, then rerun `hoi4.probability_inspect` before any `probability_evaluate`, `probability_sweep`, `probability_compare`, simulation, or sequence claim.
3. Re-run complete candidate pools under named emergency, provisional/recognized, regional/formable, league, high-chaos, and package scenarios, including phase, route, capital, host, network/league, target, cost, active-project, cooldown, war, and cleanup state.
4. Keep auto-only deadline missions without AI unless a later design explicitly makes them selectable; they are currently correct internal lifecycle blocks.
5. If a package project gains dynamic invalidation, add a narrow `cancel_trigger` and cleanup effect to that project only; do not add broad cancellation logic to all static `days_remove` projects.
6. Revisit RUT `corridor_priority` only if the owner confirms that the constant is intended to influence strategy.

## Validation and blockers

The source scan found no duplicate decision IDs, no timed block without an `available` field, no timed mission without a completion/timeout/removal path, no current mission with a `visible` no-op, and no selectable mission without AI. The accepted 80-row matrix was cross-checked against the current duration constants and representative shared/package sources.

Skipped meaningful runtime validation: live HOI4 launch, save/load, in-game click behavior, complete weighted scenario evaluation, probability sweep/compare, and fresh GUI artifacts. These are outside agent execution or blocked by the MCP artifact-manifest failure. Historical artifacts are retained only as bounded or structural evidence.

## Files changed

Only this read-only audit handoff was added: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event006_decision_mission_audit_2026_08_11.md`.

No simplification or gameplay fallback was applied. The whole Event 006 status remains HOLD/PARTIAL until DM-01 is reconciled and current probability/runtime evidence is restored.
