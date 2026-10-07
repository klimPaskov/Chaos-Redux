# Event 033 consequence repair acceptance

Acceptance basis: the user requires the complete Event 033 package without simplifications, including exact mortality, recovery, bounded runtime, and all ten achievements.
At the 2026-10-03 acceptance, the orchestrator instruction authorized taking the recommended option when implementation choices arose.
On 2026-10-03 the parent reviewed `docs/plans/033_acid_rain_plans/033_acid_rain_improvement_addendum_2026_10_03.md` and accepts the following bounded repairs within that scope.
This records the parent's 2026-10-03 design decision, not approval inferred from an old handoff, path, status label, or existing code.
Implementation and engine validation remain separate requirements.

## Current claim dispositions, reconciled 2026-10-07

The original acceptance below remains the design basis for the bounded consequence repair.
Later decisions are recorded in [agent decisions D1-D36](../../../plans/033_acid_rain_plans/agent_decisions_2026-10-04.md), under the user's recorded grant of full Event 033 design authority on 2026-10-04.
Only the identified timing and implementation-queue claims are superseded here.
An `implemented` disposition describes source implementation with the stated verification limits and does not close Event 033 acceptance gates.

| Claim | Current disposition and acceptance basis | Current implementation evidence and limits |
| --- | --- | --- |
| State-local consequence transaction, retained burden, seven-input classifier, episode caps and physical damage receipts | `implemented` in source. The parent acceptance recorded below supplies the design basis, and D1 adopts that bounded repair. | `common/scripted_effects/033_acid_rain_aftermath_effects.txt`: `acid_rain_assess_window_aftermath`, `acid_rain_load_episode_cap_ledger`, `acid_rain_record_paid_recovery_consequence`, `acid_rain_reconcile_state_consequences` and `acid_rain_publish_consequence_band`. The mortality and monotonic damage gateways in `common/scripted_effects/033_acid_rain_effects.txt` consume those records. Current completion review and executed engine evidence remain separate. |
| Nine-day severe and superstorm forecasts, seven-day evacuation and one-day partial protection | `implemented` in source on D2/D3/D8 acceptance. The historical unresolved timing claim below is `superseded` by those decisions. | `common/script_constants/033_acid_rain_constants.txt`: `severe_forecast_lead_days = 9`, `superstorm_lead_days = 9`, `evacuation_days = 7`, `evacuation_partial_delay_days = 1`, `evacuation_partial_share = 0.50`. `acid_rain_open_operation` stores the partial due date, and the mortality profile consumes the reduced protection. This preserves the accepted strict pre-impact achievement requirement and 0.05 percent per-state ceiling. No live callback proof is furnished in this reconciliation. |
| Concurrent national families and per-state evacuation/recovery operations | `implemented` in source on D6/D10 acceptance. The historical serialized-operation queue claim below is `superseded` by D10. | `common/scripted_effects/033_acid_rain_preparedness_effects.txt`: family-indexed `acid_rain_op_*_entries`, state-owned reservations in `acid_rain_open_operation`, national and state completion/release helpers. `events/033_acid_rain.txt` supplies `chaosx.nr33.42` through `.47`. Caps are 2/2/4/8 evacuations and 1/1/2/3 recovery operations by band. Source presence does not prove executed payment, callback or cancellation behavior. |
| Two Regions Ready late warning binding | `implemented` in source on D4/D12 acceptance. | `acid_rain_bind_operations_to_warning` binds running unassociated operations, called by the achievement warning recorder in `common/scripted_effects/033_acid_rain_achievement_effects.txt`. Exact achievement boundary and callback validation remain with the parent and completion auditor. |
| Humanitarian addition adapter and amounts | `implemented` addition path in source on D5/D14 acceptance. | `acid_rain_register_humanitarian_pressure` supplies source-33 request facts to `famine_adapt_acid_rain_state`, which calls `famine_request_disaster_pressure`. The latter updates aggregate `famine_food_pressure` and records `natural_disaster` as the last pressure source. This establishes an addition path, not reversible source-33 accounting or recovery retirement. |
| Source-specific Humanitarian retirement on recovery or cleanup | `unresolved` supported-owner dependency retained from the original acceptance. D5/D14 do not resolve it. | No supported source-33 reversible ledger or retirement call is established by the inspected addition and recovery paths. The proof bundle in `033_acid_rain_aftermath_effects.txt:612-644` starts with `proof_floor = 1` plus readiness/tier values. Independently sufficient food/environment/transport proof and recovery removal remain under owner/completion review. Part 11's accepted-decision wording that cleanup touches only Acid Rain sources cannot establish implementation of retirement. |
| Named scenarios, probability comparisons, GUI/art approval, audio listening and live population/save/multiplayer/performance evidence | `unresolved` acceptance gates. The original acceptance and scenario contract remain required. | The parent reports current-source helper replay and synthetic movement/Air/lifecycle passes. These are source-model evidence, including native fixtures, and do not execute HOI4. Current completion, probability and UI roles review their own gates. No result or approval is inferred for them here. |

Detailed source references, route limitations and read-only document dispositions are recorded in [the reconciliation handoff](../../../plans/033_acid_rain_plans/subagent_handoffs/documentation_current_reconciliation_2026_10_07.md).

## Historical acceptance and implementation queue, 2026-10-03

The following acceptance remains in force.
Its original queue status is historical and is reconciled per claim above.

The state-local consequence transaction, exclusive strongest acute/aftermath modifier publication, forecast-versus-impact distinction, paid-recovery preservation, original deadlines, and natural-closure snapshot rules in the addendum are accepted.
A state's remaining aftermath must be real during acute weather and published immediately when its final acute layer ends.
Reentry and final shutdown must not zero that debt or recreate already paid recovery from lifetime severe flags.
An unchanged consequence assessment cannot refill the tier after paid recovery.

The recommended seven-input classifier is accepted as the concrete implementation of Part 4's otherwise unspecified tier calculation.
It uses union acute days, highest committed intensity, actual severe/superstorm impact, successful physical building damage, independently proven other-disaster aftermath, actual unresolved transport damage, and time-weighted water protection.
Its score is nonnegative, with tier boundaries at 3, 6, and 10.
The accepted component table is the addendum's deterministic classifier table: 12-day exposure blocks capped at six points; intensity points 0/1/2/3; severe/superstorm points 3/4 using the stronger once; four actual damage points per score point capped at four; one other-disaster point; two proven transport-damage points; and water credit derived from the effective time-weighted tier, capped at two.
These are tuning constants in the existing Event 033 constants file, not a third managed public meter.
Unproved damage or other-source facts may not be replaced with nominal low railway levels, generic wartime status, or forecast flags.

Ordinary visit, severe episode, and complete global phase receive separate applied-loss ledgers with population frozen at the start of each applicable episode.
The accepted 1.5%, 4%, and 8% ceilings and current-population per-pulse caps remain unchanged.
Every global opening, sustained pulse, and superstorm contributes to the same complete-global ledger.
Lifetime deaths never reset when a new episode begins.
The accepted forecast-population achievement baseline remains distinct.

Damage receives a current-generation monotonic receipt so A, B, old A, and duplicate B cannot apply a second pressure or building consequence.
Valid zero-mortality corrosion remains possible; positive Deaths is not a damage-eligibility substitute.
Ordinary opening identity follows the accepted six-full-day inactive-gap rule independently of recovery.

Finite aftermath modifier expiry ends that modifier only.
It does not manufacture paid recovery, clear underlying debt, erase a tier-3 obligation, or award recovery achievements.
Only paid or separately proven supported-owner recovery settles the retained burden.

Country GUI counts must be published at authoritative state/forecast/transfer/recovery edges and read by the presentation.
Host work must use bounded active/changed registries where required by the package's performance contract.
No broad daily world hook is authorized.
The existing first/second coverage, islands, warnings, independent fronts, exact population helper, 1500/5000 bp Air limits, and guaranteed endpoint remain unchanged.

The exact decision matrix costs and durations, native FROM capture, fresh selected-row affordability and reserve checks, immutable paid reservations, one return, correct factory commitments, project cancellation visibility, and existing per-family/concurrent-operation caps are required repairs rather than alternative balance proposals.
The following historical queue assessment is superseded by D6/D10 and the current per-operation source implementation.

> The current serialized action implementation does not satisfy concurrent evacuation/recovery limits and must not be labeled complete.
> The decision owner first repairs the public quotation/payment bridge; the bounded multi-job implementation remains queued until that tranche and its ownership handoff are reviewed.

## Historical timing proposal and retained unresolved dependencies

The following historical timing assessment is superseded by the explicit D2/D3/D8 design acceptance and current source evidence above.
Exact callback delivery remains a verification gate.

> The nine-day severe/superstorm forecast recommendation is unresolved pending explicit comparison with the three-day source specification, seven-day evacuation matrix, one-day partial effect, and exact callback delivery.
> No shorter action duration, weaker casualty ceiling, free action, or silent forecast change is authorized by this document.
> The first-response completion route must be made genuinely reachable and recorded as a resolved design decision before timing source is patched.

The Humanitarian addition path has D5/D14 acceptance and source implementation as recorded above.
Source-specific recovery retirement must still use a verified supported-owner contract.
No raw famine-field write, aggregate-pressure subtraction, fabricated refugee cohort, or generic other-source cleanup is authorized.
The absence of a verified source-retirement interface remains an explicit dependency, not permission for a weaker substitute.

The native damaged-building reader is `damaged_building_level@<building type>` in installed dynamic-variable documentation, lines 1118–1119.
The nearby `has_damaged_buildings` trigger is COUNTRY-only and cannot prove damage in one selected state.
Native route damage and actual delivered supply still require their documented/current-engine evidence.

The addendum's named consequence, episode-cap, damage-replay, recovery, capital, transfer, and generation scenarios are accepted as required checks for these repairs.
Any probability-bearing eligibility or timing patch requires an immutable baseline, owner patch, and matched comparison through the probability auditor.
MCP failures, missing live population/reload/multiplayer/performance evidence, incomplete art/GUI approval, and missing actual full-recording listening remain open acceptance gates.
Any remaining accepted-and-queued work or unresolved acceptance gate prevents completion of this no-simplifications goal.
No further broad expansion is recommended until this repair handoff is resolved and audited.
