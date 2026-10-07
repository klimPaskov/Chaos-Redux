# Asset production prompt: Event 83

Implement the visual handoff in specification Parts 4 and 5 using `chaos-redux-event-assets`, `chaos-redux-subagents`, the supplied asset-worker profiles, and the current project reference library. This is an asset-production prompt. The planning package itself contains directions, not completed art.

## Reference and source pass

Read the canonical [reference README](../../../.agents/skills/chaos-redux-event-assets/assets/gfx_references/README.md), catalog, matching contact sheets, and relevant source examples before production. The required reference library was not supplied in the planning archive and has not been visually inspected in this package. Do not claim style matching on that basis.

Use the research notes for period boundaries and occupational variety. Produce fictional period-grounded event art, not an invented archival attribution. Reuse existing country agency cosmetics through their native consumers. Real-person portraits and country flags are not required assets for this design.

## Required outputs

| Working asset role, not final localisation | Native size | Proposed destination | Consumer |
| --- | --- | --- | --- |
| Agency-development report | 210 x 176 | `gfx/event_pictures/083_agency_upgrade/report_event_agency_upgrade.dds` | Event 83 country award report |
| Consolidated development icon | 64 x 64 | `gfx/ideas/083_agency_upgrade/agency_development.dds` | The single Event 83 modifier tile |
| Independent-service completed icon | 64 x 64 | `gfx/achievements/chaosx_083_independent_service.dds` | A1 achievement |
| Independent-service grey and not-eligible variants | 64 x 64 each | Same stem with `_grey` and `_not_eligible` | Existing achievement states |
| Sustained-reach completed icon | 64 x 64 | `gfx/achievements/chaosx_083_sustained_reach.dds` | A2 achievement |
| Sustained-reach grey and not-eligible variants | 64 x 64 each | Same stem with `_grey` and `_not_eligible` | Existing achievement states |

The complete output is eight runtime DDS files. Internal sprite identifiers and achievement-key collisions must be checked against the repository before binding consumers. The proposed path names do not establish that those consumers already exist.

## Report composition

Generate a high-quality source composition showing field and technical intelligence personnel entering practical service. Keep faces and principal equipment readable after reduction to the report size. Use a restrained period palette, convincing 1930s to 1940s clothing, and a few legible tools associated with communications, observation, or language work. Present women and men as ordinary intelligence staff rather than reducing all personnel to a trench-coated male assassin.

Leave readable negative space around the central action. Avoid a crowded control room, a map-table stock scene, modern electronics, giant agency logos, and tiny fake readable documents. It must work for any country's agency without implying that every government uses the same historical institution.

Use the project report-image processor at `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`. Preserve the input source and processor parameters until validation has passed. One report composition is sufficient across all packages, because the actual package and result are communicated by the text and effects.

## Icon composition and processing

Give the consolidated modifier icon a single clear intelligence-institution silhouette. Keep it distinguishable from the two achievement silhouettes. Use the project's icon-worker process and request native ImageGen transparency for alpha-backed icon sources under [the current asset skill](../../../.agents/skills/chaos-redux-event-assets/SKILL.md).
Preserve the native alpha through processing and conversion; background removal is a documented fallback.

Achievement sources are separate transparent foreground compositions. Produce the completed, grey, and not-eligible triplets through `process_achievement_icons.py`, using the immutable project templates and their required placement rules. Do not draw a fake replacement border or approximate the template overlay manually.

Route general DDS conversion through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` only where the role-specific processor does not own conversion. Use the exact format, alpha, dimensions, and header expectations specified by the skill. Renaming a PNG extension to DDS is invalid.

## Ownership and acceptance

When real delegation is available, use the generated-event-art worker for the report and `chaosx_icon_artist` for the modifier and achievement icon sources. The main implementation agent owns sprite registration, localisation linkage, and live consumers. Give each worker disjoint output paths and a self-contained brief.

Deliver an asset manifest containing role, source mode, provider lineage, source dimensions, crop decisions, processing command, final dimensions, alpha and file-format checks, source rights, final sprite, and consumer. Retain necessary blocked work rather than deleting its only source. Remove temporary working material only after permanent evidence is promoted.

Review the eight final files at native size and inspect the available in-game evidence for report cropping, icon alpha, and achievement-state overlays. A generated source image alone is not an accepted runtime asset. Report missing reference access, unavailable tools, or untested consumers explicitly.
