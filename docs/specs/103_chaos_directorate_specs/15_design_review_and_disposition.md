# 15. Design review and disposition

## Closure

The original planning parent reviewed the design and integrated five findings, F01 through F05, into their destination chapters. That review is accepted and closed, and no planning addendum remains unresolved. Part 14 records the basis of the broader expansion choices. Neither this record nor the import grants fresh implementation approval or separate user approval of proposed tuning numbers.

Two later user-authorized changes sit on top of it. The user's 10 October 2026 selection, **Allow relaunch after defeat**, superseded the original lifetime manual-launch lock and is promoted into Parts 02, 09, 11, 12, 13 and 16. The 10 October 2026 spec audit under the user's planning-package brief is logged in the [package guide](00_package_guide.md#revision-log). The [import review](../../plans/103_chaos_directorate_plans/subagent_handoffs/103_import_review_2026-10-10.md) owns document dispositions and the [import evidence](../../plans/103_chaos_directorate_plans/103_import_evidence_2026-10-10.json) owns checkout and identifier observations.

## Findings and integrated fixes

### F01. Required impassable territory lacked an exact conquest route

**Priority:** high. **Destinations:** Parts 05, 07, 09, 13 and 16. **Disposition:** resolved in the accepted design.

The origin-continent set includes ownable fully impassable administrative states, but physical occupation of them is impossible. Part 05 now requires a verified military-defeat receipt for the actual wartime legal owner, direct Directorate control of all that authority's combat-occupiable states on the same continent, and no separate resisting controller. The exact ownership and control change must succeed before absorption or objective credit. An unsupported result stays a missing state and an implementation blocker, and no state leaves the denominator.

The same reasoning would fail for Directorate defeat when several enemies hold its former states, so Part 05 gives defeat a separate victor branch. It requires verified wartime defeat of CXT, loss of its combat-occupiable holdings to its wartime conquerors or lawful recipients from the same settlement, and no remaining CXT military control. Each residual impassable state goes only to its proved participating victor or recipient, and native country destruction remains a further gate. Part 13 W09 and E07 exercise it.

### F02. A tuning band did not prove the huge army could operate in one state

**Priority:** high. **Destinations:** Parts 02, 03, 06, 13 and 16. **Disposition:** resolved in the accepted design.

A 70 to 90 percent supply reduction can leave a world-scaled army unsupplied. Part 03 therefore measures committed demand `D` and verified delivered throughput `T`, requires a reduction of at least `1 - T / (1.10 × D)`, and checks the engine-applied demand against actual delivery. Zero throughput fails admission. An unsupported configuration rolls back and stays blocked, without family omission, a smaller army, extra territory or a hidden reserve. Relaxation is conditional on proved capacity. Part 13 C04 and C11 exercise it.

### F03. Industry and focus percentages needed one accounting target

**Priority:** high. **Destinations:** Parts 03, 05, 06, 09, 13 and 16. **Disposition:** resolved in the accepted design.

The opening allowance and later focus percentages could multiply the same reward, while a simple output floor would stop conquered factories from adding anything. Part 03 freezes the opening allowance `A0` once, defines `Qbase = current usable native output + A0` and a single `Qtarget` with one terminal phase factor, and lets each focus, spirit or operation own its dimension once. Part 13 C12 and P11 cover growth, zero capacity, recovery, focus effects and terminal amplification.

### F04. Combat missions needed quantified work and exact hold semantics

**Priority:** medium. **Destinations:** Parts 03, 07, 08 and 13. **Disposition:** resolved in the accepted design.

Missions now freeze their target, work, duration and absolute deadline at acceptance. Combat variants also freeze a serviceable-force and delivered-supply requirement, concentration and counterattack require a hostile capture plus a 30-day hold inside the original 120-day deadline, and defense performs its full interval from acceptance. Noncombat tasks keep only their real transfer, route, project or operation requirements. Part 13 P12 and P13 provide the near-miss cases.

### F05. The holdout achievement's anchor selection needed a frozen rule

**Priority:** medium. **Destinations:** Parts 05, 11 and 13. **Disposition:** resolved in the accepted design.

R3 now freezes its anchor and due date at the first actor-specific qualifying crisis check, prefers the arrival-era capital, otherwise takes the smallest stable native state ID, and discloses the result immediately. UI opening, later choices, control changes and save/load cannot replace it.

## Delivery audit corrections

The original delivery audit's ten minor findings were accepted. They fixed attribution of the two indicators, action outcomes, boss-player eligibility, world conquest and impassable settlement to their owning parts, required owned and controlled land for the facility allocator, and marked the then lifetime manual-launch lock as a package decision. None added or removed gameplay. The [brief requirement matrix](brief_requirement_traceability.md) preserves the requirement mapping.

## Accepted remaining implementation gates

These are accepted gates for later implementation and production. They are not omitted features or resolved runtime defects.

| Gate | Required later resolution |
| --- | --- |
| Effective-definition completeness | Resolve active path masking, DLC configuration, every concrete definition, owner manifest and the documented provider 523/524 census difference. Unregistered content and missing consumers remain release blockers |
| Clean dormant carrier and old saves | Inspect current CXT history and nested project outputs before activation. Preserve real global history. Block contaminated admission where exact owner-certified repair cannot be proved |
| Neutral owner authorization | Implement exact identity-gated family and project adapters, including distinct provider 522 content, without original-country flags, exclusive characters or source-event completion |
| Native technology and doctrine compatibility | Verify all exclusive modes and supported reversible representations. Preserve every capability output without illegal simultaneous native effects |
| Legal power and geography | Prove actual supply and production limits, one-state setup, map membership, owned facilities, island reach, exact impassable settlement and destruction semantics |
| Real use, costs and callbacks | Bind actual native outcomes, resource vectors, fresh receipts, quoted thresholds, timers, partial work, refunds, queue suffixes and dead-actor cleanup |
| Ordinary boss-player control | Verify a supported control route and multiplayer actor identity before releasing B1 through B3 as attainable. No forced switch, debug takeover or achievement-only takeover is authorized |
| Final presentation and research | Produce the required art, consumer wiring, final localisation, primary-source quotation research and a unique licensed musical recording. Only the three supplied names are final |
| Implementation evidence | Use relevant references, supported inspections and scenario calculations, with local source alternatives after the AGENTS.md retry limit. Keep unobserved engine behavior explicit. Missing requested outputs and actual defects remain incomplete, while an unavailable optional check alone does not block delivery |

## Stop condition

The next substantive phase is implementation against Parts 12, 13 and 16. Do not repeat the completed planning run or add another faction, country tag, ideology route, named leader roster, public currency, dashboard, model family, aftermath subsystem or super-event to make the package seem larger.
