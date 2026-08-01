# Event 012 Africa decision and mission duration final audit

## Scope and result

This audit reviewed the D1 exact-duration and objective implementation across the complete 102-row action matrix.

One severity-two contract defect was corrected.

`form_dynamic_two_continent_union` routes through the epic preparation mission with a 540-day nominal timer, but its contract previously declared a 1-to-1-day range.

The contract now declares the actual 360-to-900-day preparation range with its existing 540-day nominal value.

The mission still settles the union immediately after that preparation resolves, which preserves the matrix wording "instant after long preparation."

No acceptance-ledger correction is needed for row 89: its current entry already describes the action as instant after long preparation and records the 540-day non-instant mission behavior.

## Files changed

- `common/script_constants/012_africa_action_constants.txt`: `africa_action_contract.form_dynamic_two_continent_union_minimum_days` changed from `1` to `360`; `maximum_days` changed from `1` to `900`.
- `docs/events/012_africa/action_duration_objective_contract.md`: corrected the duration explanation and narrowed the `FROM` timer claim to the available documentation evidence.
- `docs/plans/012_africa_plans/subagent_handoffs/2026-08-01_africa_decision_duration_final_audit.md`: this audit handoff.

No decisions, event script, scripted GUI, localisation, target array, or action outcome was changed.

## Issue list, sorted by severity

1. **S2 fixed — `form_dynamic_two_continent_union` declared a 1-to-1-day contract while its non-instant epic mission uses a 540-day nominal preparation.** The default fell outside the declared range and exposed a contradictory player contract. The constants now state `360`, `900`, and `540`.
2. **S3 residual runtime gate — targeted mission timer parser behavior.** `mission_africa_action_short`, `medium`, `long`, and `epic` use `days_mission_timeout = FROM.africa_active_action_duration_days`. Decision modding documentation establishes `FROM` as the target of a targeted decision, and vanilla proves country-scoped variable timers in `ETH.txt`, `SOV.txt`, and `CHI_decisions.txt`. No exact vanilla `FROM.<variable>` timer precedent was found. Do not claim engine-runtime confirmation until the parent has its normal live validation evidence.
3. **S3 residual depth issue — generic partial and failure semantics cover most action rows.** Every row records an action-specific full, partial, or failure flag and has player-facing text, but only a narrow subset has extra direct partial or failure mechanics. This is pre-existing broad outcome design, not a safe local audit patch.
4. **S3 residual edge case — natural-disaster weapon actions can lose their hostile-war predicate during a running mission.** `petition_the_rain` and `defy_the_drought` validate an existing war against the selected target before launch, and the hostile call revalidates it before firing. If the war ends during the timer, the weapon is safely not fired, but the paid action still reaches the ordinary outcome path. A refund-versus-failure policy would be a broader design decision and was not invented here.

## Decision category lifecycle

The category flow is coherent and target-safe: selector decision -> quote/profile computation -> exact target revalidation -> dynamic payment -> per-target record snapshot -> shared targeted mission or instant resolution -> full/partial/failure resolution -> idempotent cleanup.

The action record snapshots duration minimum, maximum, nominal duration, response delay, objective class, start-at-war state, cost reservations, and generation on the selected target.

The active-record and target-array gates prevent a second action from overwriting the same target's live record.

The action capacity trigger uses a strict active-count comparison, with opening, charter, and continental caps of 2, 3, and 5 respectively.

Cancellation removes the exact shared mission, target-array membership, duration and objective variables, event target state, and reservations; it then applies the existing target cooldown.

## Mission quality notes

| Mission | Owner and category | Target/region requirement | Duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `mission_africa_action_short` | Current Africa host; shared Africa action categories | Live target record and matching short-band flag | Target snapshot `FROM.africa_active_action_duration_days` | Early objective resolves through `africa_resolve_action`; timeout resolves through the same outcome kernel; cancellation calls `africa_cancel_action` | Prevented by target record, generation, and target-array checks |
| `mission_africa_action_medium` | Current Africa host; shared Africa action categories | Live target record and matching medium-band flag | Target snapshot `FROM.africa_active_action_duration_days` | Same lifecycle | Same protection |
| `mission_africa_action_long` | Current Africa host; shared Africa action categories | Live target record and matching long-band flag | Target snapshot `FROM.africa_active_action_duration_days` | Same lifecycle | Same protection |
| `mission_africa_action_epic` | Current Africa host; shared Africa action categories | Live target record and matching epic-band flag | Target snapshot `FROM.africa_active_action_duration_days` | Same lifecycle | Same protection |

The objective distribution is 90 `none`, 3 `peace_or_timeout` (`open_aid_corridor`, `deploy_volunteers`, `break_blockade`), 8 `response_window` offers, and 1 `war_preparation` (`intervene_against_coloniser`).

The eight offers delay `chaosx.nr12.210` within `event_target:africa_action_target`, using that target's `africa_active_action_response_days`; their accept, partial, and refusal options set the target outcome and resolve the same record.

## Cost, requirement, AI, tooltip, and route-lock notes

All 102 profiles declare a non-zero cost tier, at least one resource component, duration band, risk class, and valid profile state.

The selector decisions remain zero-cost quote selectors; the execute path recomputes the quote for the exact selected target, validates the dynamic resources and state target, then performs payment.

The quote multiplier scales from target factories and states, selected states, integration burden, colonial pressure, active actions, and confidence rather than using one flat political-power exchange.

All 102 selectors, names, descriptions, and 306 full/partial/failure result localisation keys are present.

The action AI profile references all 102 matrix actions, while the profile selectors themselves have `ai_will_do = { base = 0 }`; the controller cycle owns execution rather than allowing an uncontrolled player selector click path.

The natural-disaster target trigger requires an existing non-host target that is at war with the host, and the action's launch validation additionally checks actor eligibility, available weapon cost, cooldown state, and the selected target predicate.

## Gated-row audit

All twelve gated matrix rows remain correctly route-locked and were not opened.

- Rows 73 to 76 require Evolution III plus their disease review or strange-formation readiness gate, and rows 74 to 76 also respect active-action capacity.
- Row 85 requires the sponsorship gate, a candidate target, and `africa_world_package_implementation_ready`.
- Rows 86 to 89 require the world-order route plus their compatible union, terminal-war, defeated-continent, or complete-plan predicates.
- Row 90 requires the terminal world-identity predicate.
- Rows 91 and 92 require the committed world-end state plus eligible regional or hostile high-chaos targets.

The acceptance ledger continues to mark these rows `blocked_with_gate`; no row should be promoted from this audit.

## Validation evidence

- Static crosswalk after the patch: 102 matrix rows, 102 action constants, 102 complete four-field duration contracts, 102 profile contract dispatches, no missing or extra keys, no nominal duration outside its declared range, and no numeric matrix-range or midpoint mismatch.
- Mission inspection: four `FROM.africa_active_action_duration_days` timer call sites, four early-objective completion call sites, four timeout-resolution call sites, and four cancellation cleanup call sites.
- Static player-facing coverage: 0 missing selectors, 0 missing name keys, 0 missing selector descriptions, 0 missing outcome strings, and 0 missing outcome-record flags across the 102 rows.
- Event inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/485925f7aa413fc363e9f8cd5ba22c7a4381c067bf22dd321aa21511ec735c1b/10674376363d20e15f6cb7ea90c83bc1356e1658b5d576ed8cf4e8157b103cc4/event-lint-b256818148b3.json`. The inspector returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics; workspace-wide helper and lifecycle projections were deferred, so this is supporting evidence rather than a full event lint pass.

No decision-owned scripted GUI file changed, so GUI inspection or rendering was not applicable.

## Skipped validation and remaining gate

Live game execution, the exact targeted `FROM` mission-timer parser path, save migration, and rendered decision UI remain unverified in this audit.

No fallback was introduced.
