# Generic camp protected-cohort custody owner patch

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: owner closure implemented in the current workspace; no commit created.

## Changed files and identifiers

- `common/decisions/camp_repression_generic_decisions.txt`
  - `generic_activate_detention_network`
  - `generic_redirect_labor_to_construction`
  - `generic_redirect_labor_to_resource_extraction`
  - Existing generic-kit branches remain present. A second, state-targeted exact-cohort branch is available only when the state has an unambiguous `famine_migration_current_cohort_id`, the country is eligible, and the existing activation/project site gates hold.
- `common/scripted_effects/camp_repression_rework_effects.txt`
  - `camp_rework_prepare_exact_cohort_custody`
  - `camp_rework_commit_exact_cohort_custody`
  - `camp_rework_prepare_monthly_state_death_profile` now assigns `chaos_meter_deaths_reason.forced_labor` for the exact `expanded_labor` site branch.
  - Existing `camp_rework_activate_detention_in_action_state` and `camp_rework_start_generic_labor_project_in_action_state` call the commit helper only after their concrete state site/project assignment exists.
- `common/scripted_effects/camp_repression_action_dispatcher_effects.txt`
  - Generic custody action IDs now route through the generic dispatcher before named-country routing.
  - The dispatcher stages the explicit cohort and permits the generic action only for the existing generic gate or a successfully staged exact cohort.
- `common/scripted_effects/famine_migration_adapter_effects.txt`
  - Adds `famine_migration_record_current_state_cohort_custody_exact`, a thin explicit-ID/current-host/whole-row wrapper around the existing strict receipt.
- `common/scripted_effects/famine_migration_adapter_effects.md`
  - Documents the now-valid owner call site for the existing strict receipt.
- `localisation/english/camp_repression_rework_l_english.yml`
  - Makes the exact whole-row cohort consequence explicit in the three affected decision descriptions/tooltips.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/camp_generic_custody_owner_patch.md`
  - This handoff.

`common/decisions/famine_migration_decisions.txt` was not edited.

## Exact transaction proof

1. The state-targeted decision requires the persisted state `famine_migration_current_cohort_id` and rejects `famine_migration_cohort_selection_ambiguous`. Normal generic-kit visibility remains available through its original branch.
2. The generic dispatcher selects an explicit custody action enum: `internment` for detention activation and `forced_labor` for construction/resource extraction.
3. `camp_rework_prepare_exact_cohort_custody` passes that explicit ID to `famine_migration_resolve_cohort_origin`, requires aligned live/history arrays, one live row, positive amount, live status, and `famine_migration_cohort_host` equal to the selected state, then stages the exact ID, amount, action, and actor token on that state. It does not change population, movement, deaths, quotas, pressure, or migration arrays.
4. The existing owner action then creates the detention site or starts the concrete labor project. Only after that mutation, `camp_rework_commit_exact_cohort_custody` supplies the staged ID and proof tokens to `famine_migration_record_current_state_cohort_custody_exact`. The adapter resolves that explicit ID again, rechecks the current host and positive amount, and supplies the fresh whole-row amount to the strict receipt:
   - explicit `famine_migration_cohort_custody_id_request`;
   - `internment` or `forced_labor` action enum;
   - fresh whole-row `famine_migration_cohort_resolved_amount`;
   - transaction proof `one`;
   - actor proof equal to the generic action ID (`100`, `102`, or `103`);
   - concrete site proof equal to the selected state ID.
5. It calls `famine_migration_record_cohort_custody_action_exact`. That helper performs the final exact-ID/alignment/host/owner/status/whole-row/idempotence checks and forwards one owner-scoped achievement receipt. A stale ID, wrong host, ambiguous selection, broken arrays, invalid status, partial amount, missing proof, or duplicate action produces no new evidence.

The assignment is staged before the proof tokens are set. The adapter remains evidence-only and does not infer custody from buildings, site type, quotas, output, deaths, or pressure.

## Before and after behavior

Before, named owners could not use the generic state-targeted actions because their decisions were hidden by `camp_rework_country_uses_generic_kit`, and the existing generic actions had no cohort ID/host/whole-row transaction boundary. Generic activation/project effects created sites or projects without a protected-cohort receipt.

After, a valid exact-cohort state can use the same existing generic decisions for GER/JAP/SOV/ENG/USA/FRA/VIC/ITA/BEL and any other eligible owner with a valid generic pool. The same action IDs route through the generic owner seam, stage the explicit row, perform the existing site/project operation, then issue the strict receipt. Countries without a cohort selection continue through the original generic-kit path. No new decision, category, GUI, mapmode, event, migration row, population debit, death pulse, or movement path was added.

## Decision lifecycle and cognitive-load audit

- The camp category keeps its existing action set; these changes add no category or tab and do not alter the separate famine-category six-action cap.
- The three affected decisions each have one primary state target and existing cooldown/resource gates. The exact branch adds only the persisted cohort-selection gate; it does not expose raw ledger arrays or a new wall of values.
- The displayed state remains the existing map decision title. No new value dump is exposed; the exact row ID and amount remain internal proof fields.
- Existing decision names/descriptions remain truthful for generic and exact use. The existing effect tooltips still describe the site/project consequence; the strict adapter is not a player-facing cost or hidden fifth cost.
- Active mission impact is unchanged: the two labor actions still activate the existing `generic_labor_project_cycle`, with no additional mission or tab.

## Mission quality

`generic_labor_project_cycle` remains owned by the existing generic project lifecycle. Owner: country ROOT. Category: camp/repression generic labor project. Region: selected active camp state. Requirement: existing active responsible site plus infrastructure/resource and equipment/factory gates, now with an explicit whole-row cohort staged when exact custody is requested. Duration, success, failure, cleanup, and duplicate risk remain in the existing mission/effect path; no second mission or duplicate producer was added.

## Cost and requirement clarity

Each affected decision retains its existing cost design: activation uses political power plus the existing manpower, command-power, and support-equipment availability/effect path; labor projects use political power plus existing motorized, train, support-equipment, and civilian-factory requirements. No new spendable cost type or cost string was introduced. The exact branch adds non-consumed row-validity requirements and does not hide a fifth spendable cost. Existing decision costs are icon-backed by their unchanged generic decision implementation.

## AI validity and route-lock evidence

- Player and AI target the same state validity and exact-cohort staging rules. The activation target keeps the existing AI site cap; the labor target keeps the existing project/country caps and weights.
- Generic action IDs now route before named-country dispatch, preventing GER/JAP/SOV/ENG/USA/FRA/VIC/ITA/BEL exact actions from being silently swallowed by bespoke dispatchers.
- Mandatory baseline probability inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c754a77d2109a7bb62811c95457e68d6433dea937a38c8dff3d8633b911bdd87/49e7f509cfd67b8f2252b3c121fae250aedb1624b0f5f650debfc2b25adb0c3c/probability-inspect-68e35b9e2ca2.json` (`PROBABILITY_SOURCE_INSPECTED`, 14 decision candidates, no unresolved inputs).
- Current probability inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b412cae5c92e82033eaaafadd78c5934da13b212010d26c242f3e94ec307295f/302204fd7558da068df7d6d7f9da913b54e9af337c3b99e16724bab48bc4068f/probability-inspect-03e7624098f8.json` (`PROBABILITY_SOURCE_INSPECTED`, 14 candidates, no unresolved inputs).
- A named baseline/current `hoi4.probability_compare` was attempted through the MCP route with the same two scenarios (`GER_valid`, `POL_valid`). The accepted comparison artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/935e369d916eab3278ffe6e1a2b90d04e7adbb803027cb77eca92b7698d6b129/039ae35478a66015d8c17d537f188c94002f4e12446cf0adbafa46a5b501fc49/probability-ca2fa524185734387021db01.json`; it reports `PROBABILITY_ANALYZED_PARTIAL`, zero comparison changes, and 241 unresolved items because the route evaluated the current source for both `before` and `after`. The MCP schema rejected artifact/source-hash pinning for `before`, so a true historical baseline/current comparison is blocked at the tool boundary. AI weights themselves were unchanged; only eligibility and routing were narrowed to the explicit staged branch.
- `chaosx_ai_probability_auditor` was not callable in this runtime; the direct MCP probability evidence above is recorded and must receive parent auditor review.

No decision-specific MCP inspect/render route is exposed by the installed server (available routes include event/focus/GUI/map/probability). No GUI surface was changed, so `hoi4.gui_inspect`/`hoi4.gui_render` are not applicable. No event route was changed.

## Localisation, cleanup, and exploit audit

- No new player-facing key was added, so no localisation file needed a new string.
- Request/proof fields are cleared by the existing strict receipt on both success and rejection. The owner staging variables are cleared after commit, including failed/stale attempts. Durable exact achievement ID arrays remain intentionally persistent evidence.
- No global scans, recurring on-actions, population movement, death/death-pressure calls, quota inference, site-only proof, free-unit loop, equipment farming, war-goal spam, or cooldown bypass was introduced. Existing decision cooldowns remain in force.

## Deaths-reason ownership follow-up

The exact monthly camp mortality owner is `camp_rework_apply_monthly_state_effects`, which prepares its proximate reason in `camp_rework_prepare_monthly_state_death_profile` and then calls the shared state-deaths adapter once. The `expanded_labor` branch now sets `chaos_deaths_reason = constant:chaos_meter_deaths_reason.forced_labor` after its rate and cap are selected and before that single adapter call.

### Reason census

Before this follow-up, the monthly profile defaulted detention and expanded-labor mortality to `camp_atrocity`; gulag used `gulag_repression`; experiment used `camp_atrocity` except Japanese biowarfare sites used `biowarfare_outbreak`; radicalized used `extermination_camp`; and contaminated used `extermination_camp` with existing biological or chemical overrides. The expanded-labor row therefore had no producer for the required `forced_labor` reason.

After this follow-up, expanded-labor mortality uses `forced_labor`. Detention remains `camp_atrocity`, gulag remains `gulag_repression`, experiment retains its existing camp/biowarfare split, radicalized remains `extermination_camp`, and contaminated retains its extermination/biological/chemical split. No `occupation_repression` inference was added; that reason remains reserved for an exact occupation-policy death owner.

### Exact branch and single-transaction proof

The branch is selected only when the concrete state profile is `camp_rework_site_type.expanded_labor`, so the existing exact state, applied amount, site type, and responsible-country context remain the owner inputs. `camp_rework_apply_monthly_state_effects` still invokes `chaos_meter_register_state_civilian_deaths_percent` once. That helper computes the same existing applied amount and calls `chaos_meter_register_deaths` once with civilian, state-population, and `OWNER` target proofs. The Deaths helper then performs one `chaos_meter_apply_state_civilian_pop_loss_from_deaths_change` path, which applies one state-population loss and records that observed amount once in the state Deaths ledger. The follow-up changes only the reason token; it adds no second loss, Deaths record, movement, or reason selection.

### Validation and blockers

The changed effect and handoff were reviewed together; the expanded-labor branch contains exactly one `forced_labor` reason assignment and its existing single `chaos_meter_register_state_civilian_deaths_percent` call remains unchanged. The existing `chaos_meter.deaths.cause.forced_labor` localisation and scripted Deaths-view mappings were verified, so no localisation edit was required. The touched Clausewitz effect retains balanced braces and no unsupported comparison operators; `git diff --check` is clean apart from the repository's existing line-ending warnings. No MCP route is applicable to this non-decision, non-event, non-GUI effect-only change, and no live game process was launched. No blocker remains for this bounded reason-owner patch; the earlier custody-owner MCP limitations remain unchanged and are listed below.

## Remaining issues and recommended follow-up

Severity medium: the decision trigger surface can prove an explicit state selection and existing site/action gates but cannot resolve the global ID-to-row mapping without executing the effect wrapper. The dispatcher and owner wrapper fail closed on stale, wrong-host, ambiguous, dead, or partial rows; parent live validation should verify the user-facing disabled/available text for stale selections.

Severity low: the installed MCP lacks a narrow decision inspect/render endpoint and the custom probability auditor is unavailable. Parent review should retain the two inspect artifacts and the partial compare artifact as evidence rather than treating source review as gameplay proof.

No broad plan handoff was written because the accepted generic owner closure is local and implemented. No commit was created.
