# Event 012 Event 013 documentation reconciliation handoff

Date: 2026-08-02

Status: current documentation surfaces reconciled after commit `771ff9263`. No gameplay, localisation, spreadsheet, or asset file was edited. Live acceptance remains open.

## Scope and source evidence

This pass covered `docs/specs/012_africa_specs/`, `docs/events/012_africa/`, and `docs/plans/012_africa_plans/`, with implementation evidence limited to `common/scripted_effects/013_natural_disasters_effects.txt` and the named Event 013 owner handoff.

The current Event 013 effect defines `natural_disaster_record_event012_civilian_weaponisation` after `natural_disaster_apply_population_loss` and calls it once from the ordinary impact path in `natural_disaster_execute_impact`.

The helper requires the persisted `hostile_actor` caller type, the Event 012 caller ID, a persisted caller country, and `natural_disaster_last_deaths > 0` before invoking `africa_achievement_record_disaster_weaponised_against_civilians` on the persisted Event 012 host.

The current exact owner handoff is `docs/plans/012_africa_plans/subagent_handoffs/012_africa_event013_civilian_weaponisation_owner_2026-08-02.md`.

The shared worktree also contains a separate uncommitted sequence-guard tranche documented in `docs/plans/012_africa_plans/subagent_handoffs/012_africa_event013_civilian_weaponisation_sequence_guard_2026-08-02.md`. This reconciliation did not own that source patch, so its pending-state and sequence-ID requirements remain a parent review item.

## Source-of-truth map

| Surface | Current authority | Disposition |
| --- | --- | --- |
| Accepted Event 012 design | `docs/specs/012_africa_specs/` and the row 38 achievement matrix entry | Unchanged normative design. The civilian-weaponisation clause remains an intended disqualifier. |
| Current event status | `docs/events/012_africa/overview.md` | Updated to distinguish the stable public Event 013 call contract from the newer effect callback. |
| Hostile nature mechanics | `docs/events/012_africa/natural_disaster_weapons.md` | Updated to document the Event 013 callback owner and preserve the Event 012 wrapper boundary. |
| Current row disposition | `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` row 37 | Updated from future-owner wording to source-wired owner evidence with live ecological-covenant proof still blocked. |
| Runtime source evidence | `common/scripted_effects/013_natural_disasters_effects.txt` | Read-only evidence. The helper and ordinary-impact callsite are present. |
| Exact owner handoff | `subagent_handoffs/012_africa_event013_civilian_weaponisation_owner_2026-08-02.md` | Current implementation evidence. The source owner is exact, but live acceptance remains open. |

## Plan and handoff disposition

| Document | Disposition | Current interpretation |
| --- | --- | --- |
| `subagent_handoffs/012_africa_event013_civilian_weaponisation_owner_2026-08-02.md` | Current | One Event 013 helper, one ordinary-impact callsite, and one Event 012 owner invocation are source-confirmed. |
| `docs/events/012_africa/natural_disaster_weapons.md` | Updated current doc | The public wrapper and call contract remain authoritative, while the Event 013 effect owns the narrow civilian-death callback. |
| `docs/events/012_africa/overview.md` | Updated current ledger | Current wording now names the callback and labels the old unchanged-source claim as dated provenance. |
| `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` row 37 | Updated current ledger row | Civilian-weaponisation is source-wired and positive-deaths gated. The row remains blocked for live proof and any remaining actor-rampage or duration requirements. |
| `docs/plans/012_africa_plans/012_africa_runtime_core_audit_handoff.md` | Historical retained evidence | Its July 29 statement that Event 013 sources were unchanged predates commit `771ff9263` and remains provenance only. |
| `subagent_handoffs/012_africa_achievement_partial_owner_patch_2026-07-30.md` | Historical superseded evidence | Its explicit "No current callsite" row is retained with its superseded notice and must not be used as current status. |
| `subagent_handoffs/012_africa_b3_achievement_owner_closure_2026-08-01.md` | Historical superseded evidence | Its statement that the civilian owner had no call remains a pre-callback audit result. |
| `subagent_handoffs/012_africa_achievement_callsite_audit_2026-07-29.md` | Historical baseline | Its row 37 missing-writer classification predates the current owner and remains dated audit evidence. |
| `docs/plans/012_africa_plans/documentation_cleanup_handoff.md` | Superseded prior cleanup | Its August 1 unchanged-source wording is retained as prior-pass provenance. This handoff and the current overview supersede it for status. |

## Contradictions

Resolved: current event documentation no longer describes the whole Event 013 source as unchanged. It now distinguishes the stable public call contract from the callback added in the Event 013 effect file.

Resolved: current acceptance-ledger row 37 no longer instructs a future civilian-weaponisation owner. It records the source-wired owner and the positive-civilian-deaths gate.

Remaining historical contradiction: dated July 29 and August 1 audit handoffs still say the Event 013 source was unchanged or the civilian owner had no call. These claims are preserved as dated provenance and are explicitly superseded by the current owner handoff and overview.

Remaining acceptance boundary: row 37 still needs the complete ecological-covenant route and live no-disqualifier evidence. The ledger also leaves actor-rampage proof and any required duration reset open because this pass did not infer those owners from the Event 013 callback.

## Duplicate and superseded documents

No files were deleted or destructively merged.

The current owner handoff, `natural_disaster_weapons.md`, and the overview are the active documentation set for this integration. The July 29 and August 1 audit handoffs remain historical evidence rather than duplicate current authorities.

## Stale prompt and instruction review

No scoped prompt file claims that the current Event 013 source is unchanged or that the civilian-weaponisation owner has no callsite.

The stale wording found in scoped plans is confined to dated audit handoffs listed above. Future implementation work should cite the current owner handoff and the reconciled overview.

## Recommended parent decisions

1. Use the current Event 013 owner handoff and acceptance-ledger row 37 for implementation status, not the dated no-call audits.
2. Keep the Event 013 public call contract as the shared API boundary and treat the effect callback as the sole civilian-death witness for this owner.
3. Schedule live ecological-covenant acceptance for row 37 and decide separately whether actor-rampage and duration-reset requirements need another owner tranche.
4. Leave the dated audit wording unchanged unless a later archival policy requires a superseded banner. No such banner was necessary for this bounded pass.
5. Review the separate sequence-guard tranche before treating the current working-tree callback contract as final, then update the row 37 evidence if that tranche is accepted.

## Files changed

- `docs/events/012_africa/natural_disaster_weapons.md`
- `docs/events/012_africa/overview.md`
- `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv`
- this handoff

## Validation and skipped checks

Targeted source inspection confirmed one Event 013 callback definition, one ordinary-impact callsite, and one Event 012 owner invocation.

`Import-Csv` parsed all 809 acceptance-ledger rows with nine fields, and row 37 contains the current owner evidence without changing the UTF-8 BOM.

Targeted `rg` checks confirmed that current docs use the callback wording and that remaining no-call or unchanged-source claims are confined to dated provenance files.

No gameplay launch, live-save validation, MCP event render, workbook export, or binary asset review was run because those surfaces are outside this documentation-only scope and remain parent-owned.

## Remaining risks

The source owner is documented but live gameplay acceptance is not proven. Dated historical handoffs still contain stale claims by design, so parent work must follow this handoff and the current Event 012 overview when resolving row 37. The uncommitted sequence-guard tranche is an additional integration risk until the parent reviews its source and handoff together.
