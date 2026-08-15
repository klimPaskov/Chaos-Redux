# DM-01 Secure the Provisional Capital: specification alignment audit

> Superseded by `006_dm01_provisional_capital_implementation_2026_08_12.md`. This read-only HOLD records the pre-implementation source state and its no-click-cost interpretation; the accepted matrix/spec material commitment is now implemented in the current DM-01 source files. Retain this document only as historical design traceability.

Date: 2026-08-12

## Verdict

**HOLD. No gameplay source was changed.** The current DM-01 implementation is a valid automatic garrison mission, but it does not implement the material-cost language in the accepted Event 006 matrix and mechanics specification. A bounded source patch is not safe until the owner resolves a real design conflict: the matrix/spec require infantry equipment, support equipment, and an isolated-capital train or truck burden, while the 2026-08-02 accepted matrix audit explicitly approved **"garrison commitment, no click cost"** for DM-01.

The exact cost quantities, the meaning of "tied divisions," the capital-supply predicate, whether resources are paid or temporarily reserved, and whether cancellation refunds them are not defined. Choosing a shared `light`, `standard`, or `major` palette, inventing a supply threshold, or converting the auto mission into a selectable costed decision would therefore be a design change rather than a safe local repair.

## Authority and reviewed sources

- Accepted row: `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv:2`.
- Mechanics contract: `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md:411-438`.
- Current decision: `common/decisions/006_independence_wave_decisions.txt:21-65`.
- Current gate helper: `common/scripted_triggers/006_independence_wave_decision_triggers.txt:540-562`.
- Shared tuning: `common/script_constants/006_independence_wave_decision_constants.txt:10-28,68-107,261-270`.
- Shared cleanup: `common/scripted_effects/006_independence_wave_decision_effects.txt:985-1030`.
- Current text: `localisation/english/006_independence_wave_decisions_l_english.yml:84-85`.
- Prior accepted reconciliation: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_mission_matrix_current_audit_2026_08_02.md`.
- Prior Event 006 audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event006_decision_mission_audit_2026_08_11.md`.

I read `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`. I also consulted the required offline Paradox wiki pages and the installed vanilla documentation for decision, trigger, effect, modifier, and script-constant syntax. Vanilla precedents included `common/decisions/ENG.txt`, `ETH.txt`, and `AFG.txt`; Chaos Redux material-cost precedents included `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`.

## Severity-ranked issues

### P1: Source does not satisfy the matrix/spec material-cost contract

The accepted row requires control and supply of the capital with assigned divisions and lists "tied divisions, infantry and support equipment, trains if isolated." The mechanics spec repeats the objective as controlling the capital, maintaining supplied units there, and preventing encirclement/occupation, with tied-down divisions, infantry equipment, support equipment, and train or truck burden when supply is lacking.

The current decision has only these cancellation requirements:

```text
NOT = { is_independence_wave_active_country = yes }
capital_scope = { NOT = { is_controlled_by = ROOT } }
NOT = { independence_wave_secure_provisional_capital_garrison_satisfied = yes }
```

The helper checks division count in the capital state only. It has no local supply test and no check for infantry equipment, support equipment, trains, or trucks. No DM-01 cost is paid in activation, completion, timeout, or cancellation.

### P1: Accepted source/design conflict blocks a narrow patch

The 2026-08-02 matrix audit classifies DM-01 as an automatic "Garrison commitment, no click cost" mission and explicitly treats it as a real garrison objective rather than a free reward click. The current source matches that disposition: `available = { always = no }`, no `selectable_mission`, no `custom_cost_trigger`, and no `complete_effect` payment.

The newer matrix wording and mechanics spec still contain the material-cost palette. Both sources are authoritative-looking, so there is no unambiguous implementation target. The owner must either promote the garrison-only interpretation into the active spec/matrix or approve a new material-commitment design before source edits.

### P1: Missing definitions for a material implementation

No DM-01-specific constants define:

- how many divisions are tied down or how that differs from the existing force-tier division gate;
- the infantry-equipment and support-equipment quantities;
- the train-versus-truck rule and the isolated-capital test;
- a direct state-level supply threshold or acceptable substitute;
- payment timing (activation, daily reserve, or success); or
- cancellation/relocation/annexation refund or consumption behavior.

The shared palette has light/standard/major quantities, but selecting one would invent balance and scaling. `divisions_in_state` and `has_equipment` are valid vanilla triggers, and `add_equipment_to_stockpile` accepts negative amounts, but those syntax facts do not define DM-01's design.

### P2: Requirement text is stale even under the current garrison-only behavior

`independence_wave_secure_provisional_capital_desc` says "more than" the standard `secure_capital_divisions` value. Because the helper uses an exclusive `size >` comparison, that text describes four divisions (`size > 3`) for standard force levels, while fragile releases satisfy `size > 1` with two divisions. It also omits the fragile/standard distinction and does not disclose the absence or presence of supply/material requirements.

If the owner confirms garrison-only design, the description should be rewritten to reflect force-tier behavior. If material costs are approved, a cost/blocked/tooltip localisation triplet must be added in the same patch instead.

### P2: Failure outcome is only generic ledger damage in the current block

`cancel_effect` sets `independence_wave_dm01_capital_failed` and applies legitimacy, recognition, capacity, security, and instability deltas. There is no DM-01-specific event fire, capital relocation effect, military/provincial faction influence effect, or direct `independence_wave_government_failure` flag in this block. The shared country refresh can eventually select the collapsed-cabinet idea when its global failure conditions are reached, but that is not the explicit emergency relocation/faction-pressure lifecycle stated by the DM-01 mechanics text.

This may be an intentionally abstracted ledger implementation, but it should be accepted or corrected as part of the same design decision. It is not safe to add an event or faction effect ad hoc during a cost patch.

### P2: Current weighted-AI evidence is blocked

The source declares `ai_will_do = { base = constant:independence_wave_decision_ai.urgent }`, but this mission is automatic (`available = { always = no }`) and the score does not make it clickable. The mandatory MCP probability route remains blocked by the exact failures recorded in `006_event6_decision_mission_probability_audit_current_2026_08_11.md`: `ARTIFACT_MANIFEST_INVALID` ("Artifact provenance manifest is invalid") and an absolute-path retry with `INTERNAL_ERROR` ("Unexpected internal error"). No current normalized probability, ranking, timing, sweep, comparison, or exploit-safety claim can be made.

## Decision-category lifecycle

The Founding category is visible for an active Event 006 country (`common/decisions/categories/006_independence_wave_categories.txt:12-16`). DM-01 activates when the origin is active and neither the secured nor failed flag exists (`common/decisions/006_independence_wave_decisions.txt:27-30`). The shared founding-mission helper includes DM-01 and prevents another founding mission from overlapping (`common/scripted_triggers/006_independence_wave_decision_triggers.txt:41-50`).

DM-01 is an auto-start mission, not a player-clicked operation: `available = { always = no }` and no `selectable_mission` are intentional under the current accepted source. Vanilla decision semantics confirm that `activation` starts/displays the mission, `days_mission_timeout` bounds it, `timeout_effect` is the success path for a non-selectable mission, and `cancel_trigger` invokes `cancel_effect` when the objective becomes invalid. The current timer is 75 days (`constant:independence_wave_decision_duration.short`), within the matrix's 30-75-day band.

Success sets `independence_wave_dm01_capital_secured` and applies positive capacity/security plus reduced instability. Failure sets `independence_wave_dm01_capital_failed` and applies the negative country ledger deltas. The one-shot flag pair prevents reactivation until origin cleanup. `independence_wave_cleanup_decision_layer` removes the mission and clears both flags during origin teardown.

## Mission quality notes

| Field | Current behavior | Assessment |
| --- | --- | --- |
| Owner | Every active Event 006 released country | Matches matrix owner. |
| Category | Founding / Emergency Founding | Matches matrix family and category. |
| Region | Dynamic country capital via `capital_scope` | Correctly avoids a fixed state id; capital relocation/annexation invalidates the mission only through the current control/active gates. |
| Requirement | Capital controlled by ROOT and force-tier division count in capital; fragile `size > 1`, otherwise `size > 3` | Control/garrison present; supply/material contract missing. |
| Duration | 75 days via `independence_wave_decision_duration.short` | Within the accepted 30-75-day band. |
| Success | Secured flag; capacity/security increase; legitimacy positive; instability reduction | Directionally matches matrix, but no explicit capital administration idea swap is owned by this decision. Shared refresh may change lifecycle ideas indirectly. |
| Failure | Failed flag; legitimacy/recognition/capacity/security/instability losses | Directionally matches loss, but no explicit relocation event or faction-pressure effect. |
| Duplicate risk | Active founding-mission helper, secured/failed flags, `fire_only_once`, origin cleanup | Low at source level. |

## Cost and requirement clarity

No DM-01 `custom_cost_trigger`, `custom_cost_text`, `complete_effect`, or material-payment helper exists. The shared security and diplomatic helpers prove the syntax for equipment and train/convoy costs, but they are used by selectable decisions and cannot be copied into DM-01 without deciding whether payment is immediate, reserved, consumed, or refunded.

The trigger documentation proves `divisions_in_state` and `has_equipment` syntax. It does not expose a direct state-level "all divisions in this state are supplied" trigger in the reviewed offline snapshot. `is_in_home_area`, `num_of_supply_nodes`, and stockpile-ratio checks are not equivalent to current local supply. A supply predicate therefore needs engine confirmation or an explicitly accepted approximation before implementation.

## AI validity and route-lock notes

The `urgent` AI constant is syntactically present and reasonable for an emergency auto mission, but it is not a selectable AI competition surface. The capital target is dynamic and uses the correct `capital_scope` plus ROOT/previous-state scoping in the helper. The shared founding cap prevents another founding mission from overlapping while DM-01 is active.

Because MCP probability inspection is unavailable, no evidence supports changing the urgent score, adding modifiers, or claiming that DM-01 dominates or starves another mission. Do not route a probability-bearing patch until the artifact manifest is repaired and a fresh `hoi4.probability_inspect`/compare pass is available.

## Localisation and tooltip gaps

Current title and description keys resolve, but the DM-01 description is not force-tier aware and omits supply/material semantics. There is no DM-01 custom cost, blocked, or tooltip triplet. This is acceptable only if the active design is explicitly garrison-only/no click cost. Any material implementation must add all player-facing cost and requirement text alongside the source change.

## Cleanup and exploit risk

The current automatic mission has no resource payment, so this audit found no DM-01 equipment-farming or refund loop. One-shot flags and origin cleanup are present. If material resources are introduced, cancellation on capital loss, annexation, relocation, or country invalidation must clear a reservation or refund exactly once; otherwise a retry could duplicate equipment or permanently consume it without a documented outcome. This is another reason not to add an unapproved payment helper now.

## Recommended owner decisions and bounded follow-up

1. **Preferred reconciliation:** promote the 2026-08-02 accepted interpretation into the active matrix/spec: DM-01 is an automatic, force-tier garrison-and-capital-control mission with no click cost. Then update its description to state the fragile two-division versus standard four-division requirement and explicitly describe supply as an objective only if a supported trigger is added.
2. **Alternative material design:** if the newer matrix wording is authoritative, first define DM-01 constants and semantics in the spec: division commitment, infantry/support quantities, supply threshold, train/truck route rule, payment timing, cancellation/refund, and explicit relocation/faction-pressure outcomes. Only then add a dedicated trigger/effect and localisation triplet. Reuse the vanilla/Chaos Redux custom-cost structure, but do not convert the mission to a selectable click without approval.
3. **After either source change:** re-audit lifecycle cleanup and run the required probability MCP route for any changed AI weight or weighted requirement. A failed MCP route must be reported as an evidence blocker, not replaced with source-only balance claims.

## Validation and blockers

Completed read-only checks: source inspection of DM-01 and its helper; matrix/spec cross-check; search for failed/secured flag consumers; category, cleanup, localisation, constants, shared cost helper, and active-mission-cap inspection; offline wiki and vanilla documentation review; vanilla and Chaos Redux precedent comparison.

Skipped live HOI4 launch, save/load, in-game completion/cancellation, exact local-supply validation, and probability evaluation/sweep/compare. Live game execution is outside agent scope, the local-supply trigger is not defined by the accepted design, and MCP probability calls are blocked by the artifact-manifest failures above. No GUI inspect/render was run because this is a plain decision/mission source audit and no decision-owned scripted GUI is being patched.

## Files changed

Only this read-only handoff was added:

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_dm01_spec_alignment_audit_2026_08_12.md`

No decision, mission, trigger, effect, constant, localisation, AI, category, GUI, or gameplay source was changed. No fallback or simplification was applied; the unresolved design conflict is explicitly handed back to the owner.
