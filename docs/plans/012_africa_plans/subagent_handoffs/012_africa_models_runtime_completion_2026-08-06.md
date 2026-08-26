# Event 012 Africa strange formations model production handoff

Date: 2026-08-26 (reconciled from the original 2026-08-06 handoff).

Status: this is an asset-production handoff, not an in-game completion claim. Current local package evidence is mixed: Oracle Recon has a complete Meshy 7 local PDX mesh/five-action export and reimport package staged into the existing runtime asset paths, with entity/GFX wiring and live validation still pending; Forest Giants is blocked; Disaster Wardens reuses vanilla infantry with its parent model override applied and live validation pending; Plague Carriers is blocked before mesh/action promotion; and the current redo records for the other four packages do not support the former all-complete claim.

## Shared production boundary

The target contract remains one approved reference, Meshy 7 provider lineage, measured vanilla calibration, PDX mesh and substantive skeletal actions, DDS maps, and reimport evidence for each custom package. A provider candidate, DDS preparation, legacy export, or package manifest is not a promoted runtime asset. Legacy Meshy 6 and locally authored motion remain evidence only where the current package records say so. Disaster Wardens is an explicit vanilla-model reuse case rather than a custom-model package.

## Current package status

| Subunit | Asset-production status | Current runtime mesh or model token | Entity token or consumer | Actions | Provider evidence |
| --- | --- | --- | --- | --- | --- |
| `gorilla_heavy_infantry` | blocked; current Meshy 7 redo has no verified nonhumanoid rig/action route | no accepted `.mesh` | proposed `chaosx_gorilla_heavy_infantry_entity` | idle, move, attack, recovery, death all blocked | no Meshy 7 task in current redo |
| `pan_sappers` | blocked; provider work not started and no compliant digitigrade action lineage is approved | no accepted `.mesh` | proposed `chaosx_pan_sappers_entity` | idle, move, sabotage, construction, death all blocked | no Meshy 7 task in current redo |
| `stone_cohorts` | blocked; provider capability matrix closes before rigging/export | no accepted `.mesh` | proposed `chaosx_stone_cohorts` | idle, move, attack, collapse recovery, death remain blocked | Meshy 7 candidates rejected before rigging |
| `forest_giants` | blocked; accepted natural geometry deforms catastrophically under all four sanctioned donor transfer modes | none | proposed `chaosx_forest_giants_entity` | idle, move, attack, emergence, death have no runtime exports | natural remesh and donor-rig evidence retained; no runtime `.mesh` or `.anim` |
| `oracle_recon` | local PDX export/reimport complete; runtime files staged, entity/GFX wiring and live validation remain | `chaosx_oracle_recon.mesh` in `gfx/models/units/012_africa_oracle_recon/` | `chaosx_oracle_recon_entity` | accepted idle, move, recon, observation, and death actions | Meshy 7 generation `01a03996-6938-71f8-aec7-1d2b9c4b854c`; accepted action tasks are in the linked handoff |
| `riverborn` | blocked; three Meshy 7 generations, including a new ImageGen-refined reference recovery, were rejected for missing shield/spear and open-boundary topology | no accepted current `.mesh`; legacy export is evidence only | `riverborn_entity` is a proposed consumer only | idle, move, attack, water transition, death remain blocked | Latest task `01a03d82-1562-72f3-99ea-68e83fc2cebf` rejected; 30 credits consumed, no downstream spend |
| `disaster_wardens` | custom model not required; parent override applied, live validation pending | model token `infantry` -> `infantry_rifle_entity` / `generic_western_european_rifle_infantry_mesh` | vanilla `infantry_rifle_entity` from `gfx/entities/units_infantry.asset` | use the vanilla infantry state set; no custom action package | no provider task; prior custom outputs are superseded/retired evidence |
| `plague_carriers` | blocked; static-transform bake operation is absent from the live adapter schema and no verified nonhumanoid action lineage exists | no promoted `.mesh`; one approved Meshy 7 geometry candidate and DDS prep only | proposed `plague_carriers_entity` | idle, move, deploy, release/containment, death remain blocked | Meshy 7 generation `01a03d43-63b9-7204-9873-ebafb3c18cd6` |

The current `job.yaml` and `manifest.md` records do not support retaining complete status for `gorilla_heavy_infantry`, `pan_sappers`, `riverborn`, or `stone_cohorts`. The older `riverborn/runtime/handoff.md` still says the package is complete through export and reimport, which conflicts with the newer blocked Meshy 7 redo manifest; the later ImageGen-refined reference recovery is also rejected by the latest job/history evidence. This summary follows the newer blocked status and leaves the legacy contradiction explicitly superseded.

## Current model handoffs

The current model handoffs are [`oracle_recon/runtime/handoff.md`](../../../assets/012_africa/models_3d/oracle_recon/runtime/handoff.md), [`forest_giants/runtime/handoff.md`](../../../assets/012_africa/models_3d/forest_giants/runtime/handoff.md), [`disaster_wardens/runtime/handoff.md`](../../../assets/012_africa/models_3d/disaster_wardens/runtime/handoff.md), [`plague_carriers/runtime/handoff.md`](../../../assets/012_africa/models_3d/plague_carriers/runtime/handoff.md), and [`riverborn/runtime/handoff.md`](../../../assets/012_africa/models_3d/riverborn/runtime/handoff.md). The Riverborn redo records are [`012_africa_riverborn_meshy7_redo.md`](012_africa_riverborn_meshy7_redo.md) and [`012_africa_riverborn_meshy7_reference_recovery.md`](012_africa_riverborn_meshy7_reference_recovery.md).

## Runtime staging

Only Oracle Recon has a current custom runtime candidate eligible for parent staging: the corrected local `.mesh`, five `.anim` files, and DDS maps are now copied to the existing runtime paths; the parent must still review the 117 welded diagnostic boundary-edge warning and perform live validation. Forest Giants has no runtime `.mesh` or `.anim` and must not be wired from the donor or natural candidates. Disaster Wardens has no custom output to stage; its parent-owned override now uses model token `infantry`, which resolves to `infantry_rifle_entity` and `generic_western_european_rifle_infantry_mesh`; live validation remains open. Plague Carriers has only an approved GLB candidate and DDS preparation, with no transform-baked `.mesh`, action exports, or reimport proof, so nothing may be staged. The current redo records for Gorilla Heavy Infantry, Pan Sappers, Riverborn, and Stone Cohorts likewise do not authorize staging legacy Meshy 6 or locally authored outputs.

## Parent activation and completion boundary

Parent activation is incomplete in this handoff. Oracle Recon now has its parent-owned runtime files copied into the existing consumer paths, but entity/GFX/animation wiring and live visual/audio validation remain open. Disaster Wardens has its parent-owned vanilla model override applied, but live validation remains open. Forest Giants, Plague Carriers, and the blocked or not-started current redo packages must not be represented as custom runtime-complete units. Package-level counter and audio manifests are evidence of prepared support files, not proof of a live consumer or in-game readiness. This summary does not attest a family-wide readiness flag, zero-missing-path audit, or completion of the former 49-role sound cross-reference.

Live visual, audio, and in-game validation remain parent-owned and are not claimed here.
