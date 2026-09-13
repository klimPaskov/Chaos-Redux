# Event 016 four-family native callback audit

## Scope and acceptance

The parent requested a bounded audit of Electronics, Rocketry, High Energy, and Biological Weapons native project callbacks outside `016_brilliant_scientist_projects.txt`.
After receiving the findings, the parent accepted a separate strict-owner reconciliation helper and a branch in the existing `on_project_completion` hook, with no broader Kruger synchronization, scheduler, probability, or native output changes.
This report records the source audit before that implementation.
The governing accepted design is `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.
Prior private API evidence is in `016_mengele_portfolio_core_2026-09-05.md` and `016_mengele_quote_integration_2026-09-06.md` in this handoff directory.
Biological names below are abstract project identifiers only.

## Finding: missing private dispatch, not Kruger history leakage

Before this bounded patch, `common/on_actions/016_brilliant_scientist_project_on_actions.txt:12` dispatched project completion only through `brilliant_scientist_is_current_host` to `brilliant_scientist_sync_native_project_prototypes` and `brilliant_scientist_capture_biological_agent_history`.
The current-host trigger in `common/scripted_triggers/016_brilliant_scientist_triggers.txt:90` requires the Kruger host flag and character.
The private strict provider trigger in `common/scripted_triggers/016_mengele_project_stage_triggers.txt:16` explicitly rejects that host flag and requires a live qualifying Mengele program.
Consequently a valid private provider reached neither reconciliation nor Kruger history through this hook.

The existing Kruger sync in `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1254` reads Kruger stage arrays and Capacity before calling `brilliant_scientist_complete_native_prototype_stage`.
Its branches recognize radar, either Rocketry project, the reactor, and three abstract biological project IDs.
Broadening the hook's current-host condition would therefore be incorrect: it would route a private provider through the wrong ledger and Capacity contract.

The shared `brilliant_scientist_record_new_project_prototype` wrapper in the same file already dispatches valid Mengele owners into `brilliant_scientist_record_mengele_project_prototype`.
The ten ordinary Event016 definitions in `016_brilliant_scientist_projects.txt` already call that wrapper and are not missing this dispatch.
The four reused native families below do not call it.
Singularity dispatch is separately owned by the no-DLC reviewer and is not changed here.

## Native completion inventory

Vanilla paths in this table are relative to `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
Repo paths are relative to the Chaos Redux root.
The four vanilla project IDs have no repo override definition.

| Family | Exact project ID | Native definition and output path | Private dispatch before patch |
| --- | --- | --- | --- |
| Electronics | `sp_air_radar` | Vanilla `common/special_projects/projects/radar_projects.txt:1`, `project_output` at 40 and country effects at 41 | None |
| Rocketry | `sp_rockets_flying_bomb` | Vanilla `common/special_projects/projects/rocket_projects.txt:10`, output at 58 and country effects at 59 | None |
| Rocketry | `sp_air_jet_engine` | Vanilla `common/special_projects/projects/air_projects.txt`, named project `sp_air_jet_engine`, country branch of `project_output` | None |
| High Energy | `sp_nuclear_reactor` | Vanilla `common/special_projects/projects/nuclear_projects.txt:1`, output at 21 and country effects at 22 | None |
| Biological Weapons | `anthrax_bomb` | Repo `common/special_projects/projects/biowarfare_main_projects.txt:432`, output at 475 | None |
| Biological Weapons | `plague_bomb` | Same repo file at 671, output at 713 | None |
| Biological Weapons | `tularemia_bomb` | Same repo file at 909, output at 946 | None |
| Biological Weapons | `smallpox_bomb` | Same repo file at 1142, output at 1184 | None |
| Biological Weapons | `weaponize_the_zombies` | Repo `common/special_projects/projects/zombie_weaponized_projects.txt:6`, output at 73, calls `complete_weaponized_zombie_project_from_project_output` | None |
| Biological Weapons | `black_plague_weaponization_program` | Repo `common/special_projects/projects/020_black_plague_weaponization_projects.txt:11`, output at 56, calls `black_plague_weaponization_complete_program` | None |

The four direct abstract biological outputs set their native technology/presentation receipts and call `cbrn_reveal_operations_decision_surface`.
That helper in `common/scripted_effects/cbrn_decision_visibility_effects.txt:15` only sets the operations-visibility flag; it contains no Event016 callback.
The weaponized-project output wrapper in `common/scripted_effects/zombie_special_project_effects.txt:121` either clears its console-skip marker or calls `complete_weaponized_zombie_project` at 2492.
Both that helper's existing result branches lack private Event016 dispatch.
The same file's `randomize_and_complete_weaponized_zombie_project` at 730 can invoke scripted `complete_special_project` before its ordinary completion helper; an already-completed project need not invoke native completion again.
The black-plague completion helper in `common/scripted_effects/020_black_plague_weaponization_effects.txt:181` has its own history and presentation state plus existing alternative result branches, but no private Prototype callback.
Its Kruger character-history write remains explicitly current-host guarded.
The unrelated `zombie_cure_bomb` is not one of the six accepted private family-authentication IDs and is excluded.

## Existing authentic private receipt path

`brilliant_scientist_record_mengele_project_prototype` in `common/scripted_effects/016_mengele_project_bridge_effects.txt:9` adapts the shared selector to the private API.
For the four audited families, direct private-selector calls can avoid touching shared temporary selectors entirely.
`brilliant_scientist_mengele_record_native_project_prototype` calls `brilliant_scientist_mengele_sync_native_project_prototypes`, which requires `brilliant_scientist_mengele_project_native_output_is_authentic` before authorizing the private Prototype output.
The matching family triggers in `common/scripted_triggers/016_mengele_project_stage_triggers.txt` require the strict provider, private Theory receipt, exact family selector, and `is_special_project_completed = sp:<accepted_id>`.
The Biological Weapons trigger already recognizes all six IDs in the inventory, unlike the three-ID Kruger reconciliation branch.
The private output predecessor rejects an already-completed Prototype, preserving idempotence even when several accepted native IDs are complete.
The existing private biological Prototype output is a receipt/presentation modifier, not a grant of native project outcomes or any Kruger history write.

## Accepted narrow helper design

Add country-scope `brilliant_scientist_mengele_reconcile_reused_native_project_prototypes` in the owned private stage-effects file.
It takes no parameters and defaults to no output unless the strict owner predicate succeeds.
It selects Electronics, Rocketry, High Energy, and Biological Weapons independently and calls the existing authentic private recording API for each.
Inputs are completed native project identities, private Theory/Prototype flags, and owner state.
Outputs are only the already-defined eligible private Prototype receipts and their existing private presentation side effects.
It introduces no tuning constants, costs, event targets, lower-stage fabrication, special-project completion, native output replay, Capacity access, or Kruger history mutation.
The private record API clears family/stage/authorization selectors after each call.
Call it from a separate strict-Mengele branch of the existing native completion hook, preserving the host-only branch and capture helper.
No periodic or whole-world iteration is required.
The four fixed family selectors are identity mappings, not duplicated balance tuning.

## Source references and engine limits

Required offline wiki pages and the events/subagents skills were consulted; the decisions/missions skill was also used for the preceding quote task.
The offline `On actions - Hearts of Iron 4 Wiki.md` documents `on_project_completion` with ROOT country and FROM project.
Vanilla `common/on_actions/12_wuw_on_actions.txt:1782` provides the same scope precedent.
Vanilla `common/special_projects/projects/documentation.md` documents complete `project_output` and country scope, including that scripted completion may lack a facility/scientist.
Vanilla `documentation/triggers_documentation.md:6243` documents country-scope `is_special_project_completed` with `sp:<id>`.
Vanilla `documentation/effects_documentation.md:2896` documents `complete_special_project` but does not prove callback timing relative to project completion status.
No native project output, result-weight helper, focus, technology tree, GUI, or linked event surface is edited by this bounded reconciliation.

Two preceding Event016 MCP inspections of `chaosx.nr16.901` failed after 180 seconds each: state_flow with depth 2/nodes 20/edges 30/helpers true, then trace with depth 1/nodes 10/edges 15/helpers false.
Neither produced an artifact or current revision.
The parent instructed this task not to repeat identical timeout loops.
Source-model scenarios can validate dispatch and receipt logic, but cannot prove native engine callback ordering, scripted-completion hook firing, or runtime consumer behavior.

## Unresolved boundaries

Native completion status is the accepted existing authenticity test, not proof that a native project's alternative result branch produced a particular operational outcome.
This patch must not silently alter that distinction.
It does not backfill a native project through a new scheduler or fabricate Theory when native completion precedes private Theory; only an eligible completion reconciliation can record the private Prototype.
Full portfolio decision presentation, output consumers, Biological Weapons/Singularity late-stage output gaps, and broader engine lifecycle evidence remain outside this patch and incomplete.
No fallback or simplification of the accepted receipt-authentication contract is proposed.
