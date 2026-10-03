# Event 014 single-candidate decision AI probability retry

Audit date: 2026-10-03. Status: incomplete for MCP score and eligibility conclusions because two narrow probability inspections remained pending without returning tool results.

Scope is the single weighted decision `cannibalism_emergency_ration_audit` in `common/decisions/014_cannibalism_decisions.txt`. This is a read-only follow-up to the parent baseline handoff; no gameplay source was edited, no balance target was chosen, no game was launched, and no commit was created.

## MCP attempt and coverage

The connected declaration for `hoi4.probability_inspect` exposes `adapter`, `candidatePool`, `refresh`, `source`, and `workspaceId`; `source` is typed as `unknown`, so the live declaration does not validate its nested object keys. The full relevant declarations are preserved in `evidence/mcp_attempts.json`.

Attempt 1 used adapter `decision_ai_will_do`, source `{path: common/decisions/014_cannibalism_decisions.txt}`, candidatePool containing exactly `cannibalism_emergency_ration_audit`, `refresh: false`, and the workspace ID recorded by the parent handoff. It remained pending beyond 100 seconds and returned no tool result.

Attempt 2 retried the same adapter and one-candidate pool with source `{identifier: cannibalism_emergency_ration_audit, path: common/decisions/014_cannibalism_decisions.txt}`, `refresh: false`, and the same workspace ID. It remained pending through approximately 94 seconds of explicit waits and returned no tool result.

Only the local wait cells were terminated; `hoi4.job_cancel`, native tasks, and MCP cancellation routes were not used. The calls did not return an MCP status, diagnostic, artifact URI, analysis ID, current source revision, scenario hash, or source-object validation. Treat this as a stalled response, not a service-confirmed `blocked` status or proof that the adapter is unavailable.

The workspace ID `mod_chaos_redux_ea3b2d67c2c0` is inherited from the parent handoff and was not refreshed during these stalled calls. No current MCP evidence artifact exists to render or cite.

## Named scenario attempts

| Scenario ID | Intended state and candidate scope | Result and completeness |
| --- | --- | --- |
| `E014_DECISION_CANNIBAL_STATE_BASELINE_2026_10_03` | Inherit the prior baseline assumptions: AI-controlled ordinary Cannibal actor; containment category open; no world-end or public reveal; valid primary theater; field hunger and cell strength below severe thresholds; emergency and exploitation flags false; no active mission or cooldown; remaining resources sufficient; no ritual-response exclusion; and valid target-state assumptions from the prior category scenario. For a controlled affordability boundary pair, set support equipment to exactly 40; this decision itself is not targeted. | Not evaluated. Actor/state bindings, accepted state keys, score trace, eligible-pool status, and scenario hash are unresolved. |
| `E014_DECISION_ACTOR_INSUFFICIENT_RESOURCES_2026_10_03` | Same inherited baseline state, changing only support equipment to 39; other cost resources remain sufficient. Candidate scope requested from MCP remains the single named decision. | Not evaluated. No discovered input schema or typed bindings were returned, so no state payload was sent. |

These IDs preserve the parent handoff’s named assumptions. The prior handoff’s accepted argument shell `scenarioSet.scenarios[].state` does not define valid state keys; no empty fixture or guessed keys were sent here.

The one-ID request is intentionally not a complete containment-category selection pool. The parent baseline source inventory lists 15 weighted candidates: `cannibalism_end_terror_exploitation`, `cannibalism_emergency_ration_audit`, `cannibalism_restore_supply_corridor`, `cannibalism_rotate_compromised_formations`, `cannibalism_forensic_recovery_teams`, `cannibalism_search_missing_burial_party`, `cannibalism_protect_burial_and_medical_details`, `cannibalism_public_court_martial`, `cannibalism_conditional_amnesty`, `cannibalism_seal_transfer_records`, `cannibalism_authorize_terror_battalion`, `cannibalism_feed_selected_prisoners`, `cannibalism_replace_compromised_officer_chain`, `cannibalism_infiltrate_ritual_cell`, and `cannibalism_break_ritual_economy`. That source inventory is complete for the category per the parent handoff, but its live eligible pool and external AI factors remain unresolved.

## Source trace and eligibility

The current decision source sets the AI base to `constant:cannibalism_decision_ai.high` (60). It applies factor 2.50 when `cannibalism_field_hunger` exceeds `constant:cannibalism_meter.severe`, factor 1.75 when `cannibalism_policy_open_emergency` is set, and factor 0.40 when `cannibalism_policy_exploitation` is set. The inherited baseline assumptions would leave these three modifiers false if their values and scopes were correctly bound, but no MCP score trace confirms that scenario. No combined score was calculated by hand.

This is a decision willingness score race, not an event-option `ai_chance` proportional sample and not a click probability. The source expression is classified **score-only**; no MCP ranking or normalized probability was produced.

Within this exact decision definition, source review found one base and three finite conditional factors, with no locally duplicated or contradictory weight branch. This is a bounded source observation; other candidates and external AI-strategy factors were not resolved.

The decision and category visibility require `cannibalism_containment_decisions_visible`; that helper requires an active ordinary Cannibal country, `cannibalism_containment_decisions_open`, and no global `world_end` flag. The decision also requires a valid primary-theater state: the country must have `cannibalism_primary_theater_state`, and that state must be controlled by `ROOT` and passable.

Both `available` and `custom_cost_trigger` call the same `cannibalism_can_pay_ration_audit_cost` helper. Its source conditions require manpower above 1,499, command power above 4.99, at least 40 `support_equipment_1`, and either at least 10 convoys for an island primary theater or at least 5 trains for a non-island primary theater. The payment helper uses the same centralized cost constants for 1,500 manpower, 5 command power, 40 support equipment, and the theater-specific convoy or train cost; the decision-resolution effect rechecks the affordability helper before payment.

At 39 support equipment, the source affordability predicate fails. At exactly 40, the support-equipment clause passes, while the other resource, theater, category, and cooldown requirements still apply. These are exact source-predicate findings; whether the probability adapter removes an unavailable decision from its candidate pool is unresolved. The AI score expression itself has no support-equipment modifier, so the source score expression does not change across the 39/40 boundary.

The decision’s `days_re_enable` references `constant:cannibalism_decision_timing.short_reenable_days`, currently 21. This is a source timer value, not a measured repeat frequency or sequence result.

Current source SHA-256 digests and the focused comparisons to the preserved pre-repair snapshot are recorded in `evidence/source_revisions.json`. The decision file and trigger file hashes match the preserved snapshot exactly. The current constants and effects files have unrelated parent changes, but the `cannibalism_decision_ai`, `cannibalism_decision_cost`, `cannibalism_decision_timing`, and `cannibalism_pay_ration_audit_cost` blocks compare byte-for-byte equal to their preserved versions.

## Risk and classification

| Surface or risk | Finding | Classification |
| --- | --- | --- |
| AI base and modifiers | Base 60; conditional factors 2.50, 1.75, and 0.40 as listed above; no analyzer trace. | Score-only source expression; MCP result unresolved. |
| 39/40 affordability | Shared availability and custom-cost helper requires 40 support equipment and the corresponding theater-specific logistics reserve; payment references the same constants. | Exact source predicate; engine candidate filtering unresolved. |
| Candidate pool | The inspect request contained exactly one candidate by instruction; the source category contains 15 weighted decisions. | Incomplete for ranking or normalized selection probability. |
| Dominance, starvation, and rank reversal | No multi-candidate ranking or sensitivity artifact returned. | Unresolved. |
| Positive weight on an unavailable choice | The source assigns a positive base score independently of resource affordability, with a separate hard availability gate. No current adapter result proves whether an unavailable decision remains in the analyzed pool. | Unresolved engine behavior; no defect proven. |
| Repetition and timing | Source cooldown is 21 days; no campaign sequence or observed selection timing was analyzed. | Timer source value exact; repetition unresolved. |
| Snowball or exploit risk | The helper rechecks affordability and the effect pays from the same constants, but no current engine trace or campaign sequence was returned. | Unresolved. |
| Downstream audit outcome weights | `cannibalism_resolve_ration_audit` contains a separate result-weight calculation in `common/scripted_effects/014_cannibalism_effects.txt` beginning near line 6146. | Outside this bounded decision-AI candidate scope; not analyzed. |

## MCP analyses not completed

`hoi4.probability_evaluate` was not called for the baseline or the 39/40 pair because inspect returned no discovered state inputs or typed actor/theater bindings. The argument schema declares `scenarioSet` as opaque `unknown`, but that does not establish valid nested scenario keys.

`hoi4.probability_sweep` was not called because no usable scenario state or binding schema was discovered; no threshold, sensitivity, or rank-reversal result is claimed.

`hoi4.probability_render` was not called because no analysis ID or scenario hash exists to render. `hoi4.probability_simulate` was not used because the task declared no uncertain-input distribution or seed, and `hoi4.probability_sequence` was not used because this is not a complete custom weighted-pool lifecycle.

`hoi4.probability_compare` was not warranted: the parent reports no changes to weights, eligibility, timing, or costs, and the focused current source blocks match the preserved snapshot. No current before/after analysis IDs exist.

No event-chain inspect/render was run because this bounded surface is the decision’s `ai_will_do` score and affordability gate; no event-chain conclusion is made. A separate audit may be needed if the parent expands scope to the ration-audit outcome weights.

## Recommendation and handoff

No weight or eligibility patch is recommended from this pass. Keep the shared cost helper and payment constants aligned. If a later MCP run proves that the 39-equipment decision remains selectable, investigate adapter eligibility filtering and the decision’s availability surface before choosing a score change.

When the probability route responds, rerun source-qualified inspect for this one candidate, use only its discovered input names and typed bindings for the two named scenarios, and use the full 15-candidate category pool only for a requested ranking or selection race. Render only a returned analysis, and compare before/after only if a later owner patch changes a weighted value, eligibility gate, timing factor, or cost.

Inputs read: `AGENTS.md`; `.agents/skills/chaos-redux-events/SKILL.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md`; `.agents/skills/chaos-redux-mtth/SKILL.md`; and the parent handoff `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_decision_probability_audit.md`.

Offline references read directly: `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` lines 85-103 and 361-374; `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md` lines 26-34; installed `common/decisions/_documentation.md` lines 18-22; and installed `documentation/triggers_documentation.md` lines 3835-3842. Local SHA-256 digests are in `evidence/source_revisions.json`.

Completed: focused source trace, preserved-baseline block comparison, MCP route/schema observation, and this bounded handoff. Blocked: current inspect/evaluate/sweep/render results, source-qualified MCP revision, typed scenario bindings, eligible candidate proof, rank/probability results, and repetition or campaign evidence. No balance target was chosen and no gameplay source was changed.
