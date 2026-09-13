# Event Details layout and system-description repairs

Status: implemented, source-reviewed, and visually reviewed through MCP.
The user's requested button removal, space removal, text padding, and three description rewrites are complete.
No gameplay or requested design simplifications were introduced.

## Changes

`interface/chaosx_events_log_popup.gui` removes the orphaned Acid Rain details control.
The window height is reduced from 615 to 571 pixels, and its details entry and list heights from 563 to 519 pixels.
Trigger, its checkbox, and the empty toggle label move up by 44 pixels.
Abnormal Path and the two rival-member navigation controls retain their original bindings and fit on the right of the compact footer.
The empty world-end and evolution messages use 12-pixel panel-relative offsets and bounded text widths.

The final visual review exposed evolution rows painting beneath the later-defined list background.
The existing evolution row template was moved after the details-entry definition, preserving its exact content and identifiers.
The final preview now shows all three supplied evolution rows, their labels, and their checkboxes.

`localisation/english/chaosx_gui_l_english.yml` replaces only the famine, migration, and camp paragraphs of `chaosx.help.body.chaos_meter`.
Each description explains when the system affects the country, its civilian consequences, and useful responses.
Internal migration is described as movement between regions rather than an inherent loss of national population.
Reversing these three paragraph replacements restores every original byte of the working localisation file; other help sections and dynamic tokens are preserved.
The read-only Sol localisation auditor checked the underlying famine, migration, and camp facts and identified the internal-migration distinction.

## Review evidence

The supplied screenshot and `reference.html` establish the accepted small repair and preserved surrounding design.
`before/`, `after/`, `navigation/`, and `final/` retain the original, intermediate compact-footer, navigation, and corrected-layering previews and their manifests.
`help_before/` and `help_after/` retain the help text previews and comparison evidence.
All retained artifact content hashes were checked against their returned provenance manifests.

The original Event Details revision is `7c4e11f70f7d3c89711062c509f9354dfba615440d3d0d652e6afb827331e5d3`.
The compact-footer revision is `fcd3203ab1a9a0dad201cc334773edaa4d81ef79783e0122fc92547cc6c4bef2`.
The final layering render and post-inspection revision is `75a5187b5bc81dc24918a8babc32f31a9f27ed53f89695317616052789bdbc42`.
The final narrow inspector examines 46 Event Details elements with no missing or unresolved inputs; the help inspector examines two content elements with no missing, unsupported, or unresolved inputs.
`mcp_receipt.json` records source identities, inspection totals, and the audit artifact.
At 1920×1080 and UI scale 1, the parent inspected the actual full compositions and detail images, found no clipped requested text or footer overlap, and confirmed the missing Acid Rain control and 44-pixel height reduction.

## Validation limits and scope

MCP values and visibility are explicit offline scenario inputs; the renderer does not execute the campaign scripts.
The ordinary Random War fixture follows the supplied screenshot.
Navigation comparisons are geometry fixtures: they reuse its description and evolution rows while switching event identity and navigation visibility to exercise the other footer controls.
The help comparison projects the preserved old paragraph text onto the unchanged content definition with the same declared live-value display; `comparisonScenario` is not an older source snapshot.
The actual pre-change help render is also preserved.
Native scrolling and button shader effects remain renderer fidelity limits.
The broader source graph retains symbol-collision diagnostics outside these changes; full-project GUI validation is not claimed to pass.
The final help content scene has no diagnostics, and the final Event Details scene retains shader-fidelity warnings rather than text overflow or footer overlap.
No asset, gameplay balance, AI score, cost, event registry, or spreadsheet field is changed by this task.

## Source preservation and skills

`source_repairs.patch` preserves the exact task changes against the shared working snapshots, including the removal of the previously uncommitted orphan control.
Full baseline snapshots stay local under the ignored `baseline/` directory; `source_inventory.json` records their byte hashes.
The GUI change and the single help-key change are committed as source edits; unrelated localisation drafts remain in the working tree.
Used `chaos-redux-scripted-gui`, `chaos-redux-events`, and `chaos-redux-subagents`, with one read-only Sol localisation audit.
No skill was created or modified.
No Astra worker was used, and HOI4 was not launched or controlled for this task.
