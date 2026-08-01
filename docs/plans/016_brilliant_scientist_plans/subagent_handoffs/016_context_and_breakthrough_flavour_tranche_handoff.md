# Event 016 context and breakthrough flavour tranche handoff

Date: 2026-08-01

## Scope

This tranche adds bounded ordinary flavour without adding a fifth evolution, a cluster, a new triggerable scenario, or any 3D model. It keeps Event 016 a minor fire-once opening and preserves the host focus tree.

## Gameplay surfaces

- `chaosx.nr16.4` is a post-appointment host-context briefing. It offers public science, strategic security, industrial mobilisation, or distributed research based on wartime, ideology, public appointment, and factory context.
- `chaosx.nr16.5` is a finite assistant-conflict follow-up. It offers professional recognition, classified service, or cabinet mediation.
- `chaosx.nr16.6` is a first-Prototype report. The first Prototype in each family writes a pending character receipt before the delayed presentation, reserves one public publication or classified-retention choice, queues concurrent families, carries active reservations through transfer or KRG formation, and records reported plus public/classified receipts on `KRG_warren_kruger` so transfers cannot replay it.

## Causal wiring

The `.4` and `.5` options use `common/scripted_effects/016_brilliant_scientist_context_effects.txt` and shared bounded value effects. Their policy flags feed Evolution I or II MTTH modifiers. The `.6` options use `common/scripted_effects/016_brilliant_scientist_breakthrough_effects.txt` and adjust Mandate, Dependence, Exposure, Project Capacity, Independent Capacity, and Grievance through `common/script_constants/016_brilliant_scientist_project_constants.txt`. `common/scripted_triggers/016_brilliant_scientist_breakthrough_triggers.txt` rejects pending, reported, public, or classified character receipts, while the carrier arrays and active-event transfer helpers preserve the queue and presentation.

The selected first-prototype family is stored in `brilliant_scientist_last_breakthrough_project_family`, rendered by `GetBrilliantScientistBreakthroughProjectName`, and shown in the Directorate overview through `GetBrilliantScientistLastBreakthrough`. The report has no event-log or Event Details row because it is ordinary project flavour rather than one of the four logged evolutions.

## Assets and localisation

The report reuses the registered `GFX_report_event_016_brilliant_scientist_directorate_dossier` surface. No new asset or unwired sprite reference was introduced. All new `.4`, `.5`, and `.6` title, description, option, tooltip, and scripted-localisation keys are in `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` or `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml`, with UTF-8 BOM preserved.

## Validation evidence

- Focused Event Chain Viewer lint for `chaosx.nr16.4`, `.5`, and `.6` returned `status: ok`, `blockingDiagnostics: 0`, and no direct blocker records. The tool reported workspace-wide deferred helper and lifecycle passes because the repository exceeds its scan limit.
- Touched script blocks have balanced braces. New and touched localisation files retain BOM encoding. New event and effect identifiers were searched for duplicate definitions and unresolved local references. The first-Prototype guard was checked at both the local country-array and persistent character-receipt layers.

## Remaining risks and queued work

Broader country-specific flavour, bespoke project-breakthrough or accident art, black-and-white news, defeat/remnant presentation, quantitative balance evidence, user-owned live scenarios, and all seven Event 016 3D entity packages remain open. Models were intentionally not produced in this tranche. The temporary workbook lock file remains unrelated and was not staged.
