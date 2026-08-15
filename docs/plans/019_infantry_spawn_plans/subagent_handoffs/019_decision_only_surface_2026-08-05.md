# Event 019 Decision-Only Surface Handoff

Date: 2026-08-05

## Accepted surface

The player-directed Event 019 surface is now ordinary decisions only. The runtime scripted GUI and its seven GUI-only DDS consumers were removed by the parent after the user explicitly requested: “don't even have a scripted gui, just use decisions.” The shared selection-cache effects remain for decision and AI parity and retain their historical `muster_gui` variable names for save compatibility.

## Live decision controls

- `infantry_spawn_review_formation_ledger` rebuilds the lot, generation, claimant, family, and request-cost caches without creating or changing a formation.
- `infantry_spawn_cycle_anomalous_family_decision` cycles among multiple eligible Evolution IV registry families; it is a cursor action only.
- `infantry_spawn_cycle_claimant_file` cycles among multiple live claimant files; it is blocked during a pending demand and has no AI weight.
- Existing Event 019 lot, request, claimant, anomalous-family, achievement, and mission decisions remain the substantive controls with their existing effect, cost, tooltip, cleanup, and AI paths.

## Runtime removals

- `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt`
- `interface/019_infantry_spawn_muster_board.gui`
- `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds`
- `gfx/interface/019_infantry_spawn/muster_seal_pulse_sheet.dds`
- `gfx/interface/019_infantry_spawn/muster_seal_pulse_static.dds`
- `gfx/interface/019_infantry_spawn/critical_command_border_sheet.dds`
- `gfx/interface/019_infantry_spawn/critical_command_border_static.dds`
- `gfx/interface/019_infantry_spawn/anomalous_registry_emblem_sheet.dds`
- `gfx/interface/019_infantry_spawn/anomalous_registry_emblem_static.dds`

The source atlases and production notes remain under the ignored `docs/assets/019_infantry_spawn/` archive and are explicitly marked non-runtime. No fallback GUI was introduced.

## Validation evidence

- Event root remains `chaosx.nr19.1`; the read-only `hoi4.event_inspect` lint completed with `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, `blockers: []`, and `blockingDiagnostics: 0`.
- MCP artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c111a86607bf80af1e17b4fcd2467f1c7a392160ab3f4e38e2dae4d423a03f1/6b8db0e16066b9c7c502aa7cf8fd1d0240d37bbd6fa2ab501ed9f7d8e2cfca8d/event-lint-2935140f17dc.json`.
- Touched decision/effect/trigger files have balanced braces, all new decision titles and tooltip keys resolve, and no runtime source references the removed GUI window, scripted GUI, background, seal, border, or registry-emblem sprites.
- Workspace-wide MCP helper/lifecycle validation remains explicitly partial because the installed inspector deferred large-workspace projections; this is a tooling limitation, not a reported Event 019 blocker.

## Remaining audit queue

The required project decision auditor and final completion auditor should re-run against this decision-only architecture. Earlier GUI audit handoffs are historical and superseded by this handoff; they must not be used as evidence that a runtime GUI still exists.
