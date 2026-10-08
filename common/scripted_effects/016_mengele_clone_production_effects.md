# Event 016 private Cloning Deployment production

This country-scoped API extends the existing clone-equipment producer with the parent-accepted weekly Deployment throughput tier.
It preserves one baseline `clone_equipment_1` per controlled facility-bearing state and adds four per owned and controlled facility-bearing state only during the existing weekly invocation.
Baseline preservation refers to the intended one-per-state rate, while caller-owned count storage corrects the old producer's cold nested-count loss under conservative helper lifetime.
One state with multiple building levels still counts once.
It reuses the legacy counter, equipment token and reserve-manpower consumer.

## Helper map

All helpers and predicates use COUNTRY scope and literal `= yes` invocation.
They accept no named parameter block.

| Identifier | Inputs and defaults | Outputs | Side effects and callers |
| --- | --- | --- | --- |
| `germany_mengele_baseline_clone_equipment_production` | None; overwrites stale `mengele_clone_production_mode` with baseline | No public output contract; mode returns none | Calls the shared kernel; parent routes existing `germany_mengele_produce_clone_equipment` here, preserving completion, construction and inheritance callers |
| `germany_mengele_weekly_clone_equipment_production` | None; overwrites stale mode with weekly | No public output contract; mode returns none | Calls the same kernel; parent routes only the existing Germany weekly hook here |
| `germany_mengele_calculate_clone_equipment_production` | Temporary `mengele_clone_production_mode`; exact baseline or weekly required; unsupported/absent mode returns zero without counting | Temporary `mengele_clone_production_base_output`, `mengele_clone_production_deployment_output`, `mengele_clone_equipment_output`; all reset to zero on entry | Temporary arithmetic only; consumes mode to none on every exit; called by kernel and parent CXT display probe |
| `germany_mengele_apply_clone_equipment_production` | Exact baseline/weekly mode supplied by its wrapper; direct use is internal | Owns the three calculator outputs across the nested return | Under supported mode and the old latch, one combined positive stockpile write with `producer = THIS`, then exactly one `clone_refresh_reserve_manpower`, including zero facilities; absent/invalid mode grants and refreshes nothing |
| `germany_mengele_clone_production_mode_is_supported` | Temporary mode; exact baseline or weekly | Pure boolean | Calculator guard before state counting; kernel guard before calculation and its grant/refresh; no writes |
| `brilliant_scientist_mengele_cloning_deployment_production_is_active` | Current country history, provider and technology | Pure boolean | Requires strict private stage provider, private Cloning Prototype, private Deployment, `clone_infantry_access_tech`, and the old completion latch; no writes |

Both pure triggers are declared in `common/scripted_triggers/016_mengele_clone_production_triggers.txt`.
The strict provider remains `brilliant_scientist_mengele_project_stage_provider_is_valid`; this API does not substitute a shorter or weaker provider gate.

## Temporary ownership and cleanup

The calculator initializes `mengele_biowarfare_facility_count` before invoking unmodified `germany_mengele_count_biowarfare_facilities`, so that nested helper's output survives conservative temporary lifetime.
The pinned old-source counterexample loses that output when it has no caller-owned count slot; the new baseline retains it without requiring an earlier counter call.
With caller-owned count storage, both implementations calculate the same baseline count; explicit THIS also corrects attribution when outer ROOT is a foreign country.
These are source-model distinctions, with missing old numeric count modeled as zero in the counterexample; they are not claims of observed game execution.
It also owns `mengele_clone_production_owned_facility_count`, incrementing once inside `every_owned_state` limited by `is_controlled_by = PREV` and a positive `biowarfare_facility` level.
PREV in that iterator identifies the invoking country, regardless of outer ROOT.

The kernel initializes all three calculator outputs before calling the calculator.
It validates mode before entering the transaction, since the calculator consumes mode before returning.
Absent mode, none, unknown integers and fractional modes fail closed in both internal helpers; literal public wrappers overwrite any such input with their own supported mode.
Any external calculator caller must do the same if it reads the results after return.
The calculator clears mode even when the old latch is absent, and both the internal producer and public wrappers clear it again at their respective boundaries.
Clearing means assignment to the mode `none` constant, not persistent flag manipulation.
There are no normal variables, new flags, event targets, durable meters, registry rows or scheduler state to clean up.
Invalidation of the private provider or either receipt/technology requirement removes the enhancement at the next weekly calculation without changing the controlled-state baseline.

## Constants and tuning

The parent owns registration in `common/script_constants/germany_mengele_constants.txt`.
No constants are declared in these helper files.

| Constant | Accepted value | Use |
| --- | --- | --- |
| `germany_mengele_clone_production_mode.none` | 0 | Consumed/default mode |
| `germany_mengele_clone_production_mode.baseline` | 1 | Literal baseline entry |
| `germany_mengele_clone_production_mode.weekly` | 2 | Literal weekly entry |
| `germany_mengele_cloning_project.clone_equipment_per_facility_per_week` | 1 | Existing controlled-state baseline |
| `germany_mengele_cloning_project.deployment_bonus_per_owned_facility_per_week` | 4 | Weekly private tier on owned and controlled states |
| `brilliant_scientist_value.zero` / `.one` | 0 / 1 | Arithmetic reset and state-count increment |

The mode category must have a first-entry schema accepting integer keys; the existing production tuning category retains its current schema.
Arithmetic assigns constants to temporary variables rather than assuming the native stockpile amount field parses a constant token.
Base and bonus are rounded separately; accepted integer tuning makes both exact state counts.
For C controlled facility-bearing states and O owned/controlled facility-bearing states, legacy output is C and active private weekly output is C + 4O.
Captured controlled sites receive the baseline; owned sites under foreign control receive neither component.

## Usage and migration

The parent changes the existing producer body to:

```txt
germany_mengele_produce_clone_equipment = {
	germany_mengele_baseline_clone_equipment_production = yes
}
```

The existing weekly hook retains its old `germany_mengele_cloning_project_completed` filter and calls `germany_mengele_weekly_clone_equipment_production = yes`.
The counter and all its other consumers, including coup-pressure calculations, stay unchanged.
Completion, facility construction and inheritance continue calling the old producer name, so they remain baseline-only even immediately after a weekly call.
Private stage effects do not call the weekly wrapper.
There is no new project admission: authentic private native source remains `sp_brilliant_scientist_cloning`, with its existing paid no-DLC callback retaining the current latch settlement.
`sp_mengele_cloning` is not added as an alternative private receipt.

The parent CXT probe performs a calculation only:

```txt
set_temp_variable = { mengele_clone_production_base_output = constant:brilliant_scientist_value.zero }
set_temp_variable = { mengele_clone_production_deployment_output = constant:brilliant_scientist_value.zero }
set_temp_variable = { mengele_clone_equipment_output = constant:brilliant_scientist_value.zero }
set_temp_variable = { mengele_clone_production_mode = constant:germany_mengele_clone_production_mode.weekly }
germany_mengele_calculate_clone_equipment_production = yes
# Copy the three outputs to the existing parent-owned CXT debug variables.
```

The probe never calls a producer or refresh helper and never grants equipment or manpower.
The producer gives no direct manpower, divisions, refunds or stage payments.
Its existing reserve consumer remains responsible for stockpile-derived manpower.
Existing `clone_select_mengele_refinement` begins with `clone_grant_infantry_access` at `common/scripted_effects/clone_system_effects.txt:95-96`.
The unchanged legacy completion callback selects that refinement before invoking its baseline producer, so operational access precedes its initial equipment write.
Refinement source is not changed by this API.

## Evidence and limits

See [implementation handoff](../../docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_clone_production_core_2026-10-07.md) for revision-bound reference citations, MCP evidence, actual-source scenarios and the reproducible driver.
Installed effects documentation defines variable stockpile amounts and COUNTRY scope; vanilla `common/scripted_effects/SIA_scripted_effects.txt:1374-1384` supplies the explicit `producer = THIS` precedent.
Offline Data structures:435-443 defines conservative nested temporary ownership; offline Scopes:261-262 and :811-818 defines THIS/PREV.
No asset, icon, audio, model or localisation key is introduced by the internal API.
Parent wiring, constant registration, player-facing explanation, accepted-spec alignment and final event audits remain parent-owned.
Source fixtures do not establish live engine cadence, native stockpile attribution or reserve recomputation.

## Future work

Any further yield or lifecycle design change belongs to the parent and must preserve the separate baseline and weekly entry points.
Keep throughput tuning in the existing production category and retain state-based counting unless an explicit accepted design changes it.
Do not add a second facility registry or periodic consumer to extend this API.
