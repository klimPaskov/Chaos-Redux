# Settings and Chaos Meter documentation review

Date: 2026-09-05.
Disposition: implemented bounded documentation review, parent-owned and parent-reviewed.
Acceptance basis: the user's documentation cleanup request and approval to apply full reading separately to bounded batches.
The parent fully read all thirteen source documents below before editing seven of them.
At parent takeover, the assigned curator had returned no reading evidence or patch, so the parent reclaimed its write scope and performed this review directly.
The later read-only closeout below records the curator's actual reading and probe evidence.

## Repairs and retained evidence

The settings index pointed to the absent `docs/systems/interface/` directory.
It now links the existing main-menu and state-map-mode documents, with a direct link to triggerable scenarios.
The Chaos Meter index links the existing air-cleanliness and CBRN package indexes.

The Deaths UI pass record describes a per-country details overlay, while the popup contract and Deaths mechanic describe it as disabled or absent.
The Chaos Meter index records this contradiction without selecting a current interface state.
The historical overlay, cache, sorting, and selection findings remain intact.
Current consumer review and matching MCP scenarios are required before either description can be promoted or the other superseded.

Event logging and numeric-entry descriptions use direct present-tense prose without update-history framing.
The Deaths mechanic has a direct nuclear-ladder link, sentence punctuation repairs, and repaired mid-sentence wrapping for Event 19 ghost-decline attribution.
Its reason 20, weight 0.10, and separate Event 10 attribution remain unchanged.
The miscellaneous and combat/contamination notes received sentence punctuation changes only.
No calculation, rate, flag, identifier, cost, trigger, GUI layout, or runtime contract was changed.

## Full-read source ledger

Hashes identify the exact pre-edit continuation02 baseline.
Each document was completely read by the parent.
These implementation-facing documents remain records of their authors' claims, with current behavior unresolved where source or engine evidence was not supplied.
An implemented documentation disposition does not accept or validate the underlying mechanics.

| Document | Documentation disposition | Baseline SHA-256 |
| --- | --- | --- |
| [chaosx_event_logging_controls.md](../../../systems/chaosx_settings/chaosx_event_logging_controls.md) | Implemented documentation repair | `d9ffc8bc25248d6a8e893bd74983878f9b91f896a6c9d947ba4cebc6da45621c` |
| [chaosx_help_window.md](../../../systems/chaosx_settings/chaosx_help_window.md) | Reviewed unchanged | `ac073006e5941cfe78e324442bebd4f120bf6e7372ce6edec0ca92284e27a1f2` |
| [chaosx_settings_export.md](../../../systems/chaosx_settings/chaosx_settings_export.md) | Reviewed unchanged | `0274748615e1dce8e45e2beb46ee24ae9c891d37f7d8f4f57a1aeeab38353072` |
| [README.md](../../../systems/chaosx_settings/README.md) | Implemented documentation repair | `4dc3976691cc275847ecb50d8328ae7ec91635ed269af3c3c13fbb0cee32c4d2` |
| [settings_miscellaneous_menu.md](../../../systems/chaosx_settings/settings_miscellaneous_menu.md) | Implemented documentation repair | `210efbbcfaa2335eda647e4a332b6da5de044e5704f8dc2bfa588c236aab36f8` |
| [settings_numeric_manual_inputs.md](../../../systems/chaosx_settings/settings_numeric_manual_inputs.md) | Implemented documentation repair | `aef951d035297975b24b2645b06772956458efee3eb24f5bc35809e56cfa6961` |
| [chaos_meter_combat_contamination_occupation_deaths.md](../../../systems/chaos_meter/chaos_meter_combat_contamination_occupation_deaths.md) | Implemented documentation repair | `4d396d8573f99c734a0f9d3bcef34bdd5f62dea792727611d0fa04ac879f10d0` |
| [chaos_meter_deaths_and_events_log_ui.md](../../../systems/chaos_meter/chaos_meter_deaths_and_events_log_ui.md) | Reviewed unchanged | `1dfabcb98fd3694eb7430eb9857dd63b47f515e804ad0616653522dfdd0ce0e3` |
| [chaos_meter_deaths_mechanic.md](../../../systems/chaos_meter/chaos_meter_deaths_mechanic.md) | Implemented documentation repair | `3eb8b20151529b89e12d8e5ed730218d09b7a9dc261109f024eaa006272c5831` |
| [chaos_meter_popup_window.md](../../../systems/chaos_meter/chaos_meter_popup_window.md) | Reviewed unchanged | `07d1443ff7db9ef003c6662d8c5cb80ea05c6dfdcb88490a4717a08b193cff6e` |
| [chaos_meter_war_declaration_counting.md](../../../systems/chaos_meter/chaos_meter_war_declaration_counting.md) | Reviewed unchanged | `f4d5c5a17680d31c93fb3414ff76a38830fe0f4cc4316c39557a7a774088d07b` |
| [nuclear_chaos_ladder.md](../../../systems/chaos_meter/nuclear_chaos_ladder.md) | Reviewed unchanged | `1256ad4e175b86d70f079174f4e1b4bb52c5c99bd4d0cfc32fc1f20600c95511` |
| [README.md](../../../systems/chaos_meter/README.md) | Implemented documentation repair | `2dd8050f752bcef5c599fe9d64d7335f57088d430c8cd1db14961f903f3a6cb2` |

## Evidence limits and remaining work

All newly added relative links resolve in the working tree.
The parent read only the opening eight lines of the main-menu and map-mode targets to verify their titles and locations, so those dependencies are not counted as full reads in this batch.
The thirteen source reads do not establish current gameplay, GUI, probability, balance, audio, or live-engine behavior.
The parent performed no MCP scenario, game launch, log search, or source-code repair for these prose and navigation edits.
The curator's earlier probe results arrived in the later closeout below.
The conflicting Deaths overlay remains unresolved.
Tuning-change history in the combat/contamination record and past interface repair notes remain historical evidence, without a fresh balance or visual completion claim.

No document was deleted, moved, merged, or promoted into an accepted specification.
No design simplification was introduced.
Current implementation validation and the broader unreviewed packages are omissions from any system-wide completion claim.
The GUI workflow skill review and its separate prose repairs are documented in [the GUI handoff](2026-09-05_gui_workflow_review.md).
Reusable skill guidance used across this continuation includes chaos-redux-subagents, chaos-redux-events, chaos-redux-decisions-missions, and chaos-redux-scripted-gui.
This thirteen-document pass creates or updates no skill.

The commit isolates this cleanup from pre-existing uncommitted Event 33 documentation.
A punctuation change inside an uncommitted Event 33 paragraph was withdrawn from the working tree, leaving that paragraph exactly as captured before this pass.

## Late curator evidence closeout

The curator confirmed full reads of all thirteen original baseline files and no edits or competing handoff.
It reported the source definitions `chaos_meter_popup_deaths_details_gui` and `window_name = "chaos_meter_deaths_details_overlay"` in `common/scripted_guis/chaosx_scripted_gui_chaos_meter.txt`, with the linked layout in `interface/chaosx_chaos_meter_popup.gui`.
This supports the presence of overlay source definitions, but no matching Deaths overlay render was returned to close the presentation conflict.

An Event Log inspection with scenario `{id:"event_log_shared_architecture_baseline", state:"normal"}` and `generatedScenarios.enabled=false` returned `GUI_INSPECTED`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fa178adda45d7adc02cb12c226d80a28b2185f1ec5b0e1de5ffc4f46bec45aa4/4bd8041bf62783dea8d52c3cb544c7f7eaaacd4be720358a03a8c56c62899105/gui-inspect.1f8444e7f19790c5.json`.
The returned summary described a complete source graph and zero missing assets, with validation false, 38 blocking diagnostics mainly involving symbol collisions, and 339 nonblocking overlap findings.
`MCP_INLINE_COLLECTIONS_TRUNCATED` limited inline evidence to 64 files from 11,495 indexed files.
This Event Log result is not a matched Deaths overlay scenario or GUI acceptance.
The parent retained the exact closeout summary and artifact URI without independently reading its complete payload.

Four no-scenario probes were rejected because windowName and scenario must be provided together, and a string scenario was rejected because an object was required.
An object retry was interrupted after 16.3 seconds.
Three later settings/help/Chaos probes returned no payload after 121 seconds before reassignment interrupted the wait.
These attempts do not establish current service-wide unavailability.

## Parent path follow-up after closeout

The miscellaneous-settings record incorrectly assigned current random selection helpers to absent `common/scripted_effects/chaosx_random_event_selection_effects.txt`.
Narrow source lookup located definitions of `evaluate_random_event_selection_candidate`, `select_weighted_random_event_id`, and `select_unweighted_random_event_id` in `common/scripted_effects/chaosx_settings_effects.txt`.
The current owner reference was corrected while the old path remains in the historical file list.

Git records deletion of `common/scripted_effects/chaosx_effects.txt` and `events/chaosx_events.txt` in `ef63c9e8dcd9a7f2f26c07cd319c5760190be2e7`, and deletion of `common/scripted_effects/fallout_world_end_effects.txt` in `8cea20fda6c51ac49de670fc323dae306e0d1e3f`.
The file list is labelled historical and retains those original paths alongside the verified facts.

The popup background is an inherited vanilla asset, not a missing mod-owned file.
The installed game's `interface/general_stuff.gfx` defines `GFX_generic_popup_win` with `gfx/interface/generic_popup_win.dds`, and that vanilla DDS exists.
The documentation identifies this vanilla ownership explicitly.
Only the matching GFX declaration and path existence were inspected, not the complete vanilla file or the asset pixels.
No engine-facing change or visual acceptance claim follows from these path checks.
