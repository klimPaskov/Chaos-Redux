# IW-179 FSM Micronesia civic source-clearance handoff

Status: **BLOCKED / no production-safe sourced real male candidate**.

## Scope and runtime boundary

This handoff covers only sourced visual-research clearance for `FSM_independence_wave_inter_island_congress_chair` / `GFX_portrait_FSM_independence_wave_inter_island_congress_chair`. The current fictional Elias Kihleng portrait remains untouched. No character, localisation, interface, GFX, event, gameplay, ImageGen, DDS, runtime, or `_small` file changed.

## Result

Tem, Ibedul of Koror (documented as serving 1917–1943) is the strongest 1936 temporal/role lead, but no attributable archival portrait was found. It cannot pass the identity gate. The other researched candidates were rejected as follows:

- Kyushu University `[ポナペ島民]` (1940): generic unnamed title, inspected image is a woman with two children, and reuse requires advance application. Evidence and exact URLs are in [manifest.md](../../../assets/006_event6_micronesia_civic_source_clearance/manifest.md).
- NDL/Kokushikan `酋長ト家族及部下 / 南洋ぽなぺ島`: visible caption identifies the King of Aru with family and people, not a Pohnpeian subject; it is a group image and the repository flags private correspondence on the addressed side.
- University of Tokyo / Commons `Koror chiefs in 1915`: period-correct Palau group, but no individual labels can identify Tem.
- Louch and Ilengelekei portraits: earlier Palauan chiefly figures whose documented service/lives fail the 1936 era-fit gate.

## Evidence and outputs

- Research manifest: [docs/assets/006_event6_micronesia_civic_source_clearance/manifest.md](../../../assets/006_event6_micronesia_civic_source_clearance/manifest.md).
- Research log: [docs/assets/006_event6_micronesia_civic_source_clearance/research_log.md](../../../assets/006_event6_micronesia_civic_source_clearance/research_log.md).
- Rejected evidence files: `source/26-115a.jpg` and `source/rejected_kyushu_2335335_canvas1.jpg`, with hashes and provenance recorded in the manifest.
- No accepted source, crop coordinates, decoded-pixel equality JSON, processed PNG, DDS, contact sheet, or `gfx_handoff.md` exists because the package did not clear identity and rights. This is intentional fail-closed handling.

## Ownership scan

Exact candidate/name forms were scanned in the current mod, vanilla HOI4, and approved Kaiserreich workshop roots (`1521695605`, `2265420196`, `1458561226`). Only current Elias Kihleng references were found in the mod; no Tem/Ibedul Tem portrait or localisation identity exists in those roots. There is therefore no safe existing asset to reuse and no collision to resolve.

## Parent action

Do not rename or wire a guessed Tem, generic Pohnpei islander, or Aru subject. Carry this source blocker until a named adult male Micronesian/Pohnpeian/Carolinian civic or traditional figure is supplied with an attributable archival object and explicit reuse basis. Once such a source is available, run the unchanged-source head-and-shoulders crop and JSON decoded-pixel equality gate before any later repaint, PNG, DDS, or runtime step.
