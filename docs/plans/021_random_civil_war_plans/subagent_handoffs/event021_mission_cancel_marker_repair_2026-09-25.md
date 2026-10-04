# Event 021 mission cancellation marker repair

Date: 2026-09-25.

Disposition: **implemented; runtime callback behavior remains Needs Testing**. Parent repair of a local decision-lifecycle defect identified in the fresh September 25 decision/mission audit.

## Change

The audited pre-edit file SHA256 was `65aef773f2a36c1cd2cbfefc2056494db4bcae6af2b33f65ca7dab4ca51071bc`. The post-edit file SHA256 is `8937cac0802745ead68d6f1ec1b2bfa97dccaa451effcc925d45a715dedd3123`.

Each selectable mission now has a cancellation-only cleanup effect that removes its own active marker:

| Mission | Cancellation cleanup |
| --- | --- |
| `event021_hold_the_capital_mission` | Clears `event021_hold_capital_mission_active` |
| `event021_secure_rail_spine_mission` | Clears `event021_secure_rail_mission_active` |
| `event021_hold_settlement_terms_mission` | Clears `event021_settlement_terms_mission_active` |

No timeout resolver, failure reward, success effect, AI weight, trigger, cost, mission duration, or player-facing text was changed by this repair. Existing settlement, reconstruction, receipt, and terminal cleanup behavior is preserved.

## Basis and validation

The fresh audit `docs/plans/021_random_civil_war_plans/subagent_handoffs/decision_mission_audit_2026-09-25.md` identified that all three `cancel_trigger` paths lacked mission-local cleanup; the rail mission can cancel after its repair receipt is produced. The offline Decision modding page states that `cancel_trigger` and `cancel_effect` generally apply to missions. The Chaos Redux Event 006 Banat mission at `common/decisions/006_independence_wave_balkan_decisions.txt:31-55` is a local timed-mission precedent with both cancellation trigger and cancellation effect; the installed vanilla mission/decision contract was also reviewed.

Source review confirms one marker clear adjacent to each mission's existing `cancel_trigger`, while the existing timeout resolver and terminal cleanup remain in place. No failure reward is placed in any new `cancel_effect`. A post-repair decision/mission audit is still pending. The probability revalidation completed with a blocked same-scenario comparison because the exact prior fixture payload is unavailable; its findings are recorded below.

HOI4 was not launched. The runtime test must exercise each mission's cancel condition after selection, confirm the marker clears and activation can recover when conditions permit, confirm no timeout/failure reward fires, and verify broad terminal cleanup. UI wrapping and weighted mission selection remain separate acceptance items.

## Changed source and limits

Changed source: `common/decisions/021_random_civil_war_decisions.txt`. The file also contains pre-existing Event 021 worktree edits to sponsor-action guards, sponsor repayment availability, and the capital mission's held-capital requirement. Those edits were preserved. No fallback, simplification, or status promotion was made.

## Post-repair probability revalidation

The read-only post-repair auditor confirmed that all three `ai_will_do` formulas are unchanged and that the current MCP source contains a complete three-candidate score pool. The adapter is score-only and does not report normalized selection probabilities. Clearing an activation marker can still change which candidate enters a later score race, so unchanged formulas do not prove unchanged selection behavior.

The prior scenario-set hash is recorded as `6c7e0663c8c8c07cc761f76fc1bfdff6683b92551f39b0f6133859f2e67da113`, but its scenario-set identifier and exact per-scenario fixture values are unavailable. Rendering the historical analysis returned `PROBABILITY_ANALYSIS_NOT_CACHED`, and the saved JSON lacked its provenance manifest. The auditor therefore did not guess fixtures and ran no evaluation, sweep, or same-scenario comparison. The post-repair handoff makes no balance conclusion; weighted mission behavior remains unverified.
