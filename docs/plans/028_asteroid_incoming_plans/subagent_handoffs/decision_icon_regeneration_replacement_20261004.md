# Event 028 decision icon replacement handoff

Date: 2026-10-04.

Disposition: the parent independently accepted all fourteen icon rows for art and reports completing the strict DDS audit, backups, and promotion to the exact registered runtime paths on 2026-10-04.

The earlier permanent handoff at `decision_icon_regeneration_20261004.md` already existed and is preserved without edits; this replacement handoff records the corrected format and the completed fourteen-icon production state.

## Parent acceptance

The parent opened all fourteen selected full-resolution originals by the exact evidence-JSON row mapping, all fourteen processed 32x32 PNGs, all fourteen actual decoded DDS textures including selected `rehouse_displaced_workers` v001, the canonical decision references, and the native/zoomed alpha sheets. The parent accepted all fourteen for art, confirming clear stage pixels and corners and strong, distinct 32px silhouettes.

The parent also confirmed that the supply wagon and crater-access gate cyan composites contain no opaque vignette. The selected alpha-1 crops are mechanical edge normalization, not background repaint.

The accepted rows are `mobile_hospitals`, `emergency_rail_corridor`, `clear_unstable_debris`, `emergency_water_filters`, `rebuild_supply_spine`, `restore_outer_ring_industry`, `rehouse_displaced_workers`, `harden_factories_against_dust`, `protect_transport_reserves`, `atmospheric_observation_network`, `secure_crater_perimeter`, `survey_extraordinary_material`, `fortify_crater_access`, and `reconnoiter_crater_site`.

This art acceptance does not validate decision gameplay, security or supply gates, missions, or native UI behavior. The parent's later byte-header and pixel/alpha audit, destination backups, and exact 32x32 runtime promotion are recorded at the end of this handoff.

## Scope and accepted inputs

The production work was limited to `docs/assets/028_asteroid_incoming/regeneration/decisions/v001_20261004/` and this permanent handoff. The parent owns runtime wiring and reports completing promotion as recorded below.

The production direction comes from Event 028 Part 9, the Event 028 asset prompt, Part 6, the exact existing consumers, and the user-authorized replacement assignment.

The required final format is strict one-level legacy uncompressed BGRA32 at 32x32; the parent's earlier BC3/DXT5 instruction was rescinded. Every selected DDS was produced by `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; no custom encoder or format-driven art regeneration was used.

Existing BC3/DXT5 candidate files, round-trips, validation records, and helper files remain unchanged under the staging folder's `superseded_parent_format` paths. They are historical format candidates and are not selected for runtime.

## Canonical consumer and reference review

The final DDS paths below are the exact registered texture paths from `interface/028_asteroid_incoming.gfx`. Each sprite uses a transparent 32x32 canvas.

The canonical reference family is `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/decisions/`. I inspected its `contact_sheet.png` first, then all thirteen individual small decision references; the two 114x101 category pictures were excluded because they belong to a different consumer family.

I also reviewed the canonical asset library README/catalog, installed vanilla `interface/decisions.gfx` sprite declarations and DDS mappings, the current Event 028 GFX definitions, and the exact consumer crosswalk retained in the staging manifest and `reference_inspection.md`.

The family direction is aged, compact painted object or figure art with a dark neutral contour, transparent unused canvas, restrained material shading, and a strong silhouette at 32px. No reference image or other icon family was used as generated input or final art, and no visual-component background was layered into these ordinary decision icons.

| Requirement | Decision id | Registered sprite | Selected staged DDS candidate | Exact runtime DDS path | Producer status at initial delivery |
| --- | --- | --- | --- | --- | --- |
| E028-DEC-01 | `decision_asteroid_incoming_deploy_mobile_hospitals` | `GFX_decision_028_mobile_hospitals` | `dds_converter_bgra/mobile_hospitals.dds` | `gfx/interface/decisions/028_asteroid_incoming/mobile_hospitals.dds` | `needs_user_review` |
| E028-DEC-02 | `decision_asteroid_incoming_open_emergency_rail_corridor` | `GFX_decision_028_emergency_rail` | `dds_converter_bgra/emergency_rail_corridor.dds` | `gfx/interface/decisions/028_asteroid_incoming/emergency_rail_corridor.dds` | `needs_user_review` |
| E028-DEC-03 | `decision_asteroid_incoming_clear_unstable_debris` | `GFX_decision_028_debris_clearing` | `dds_converter_bgra/clear_unstable_debris.dds` | `gfx/interface/decisions/028_asteroid_incoming/clear_unstable_debris.dds` | `needs_user_review` |
| E028-DEC-04 | `decision_asteroid_incoming_distribute_emergency_filters` | `GFX_decision_028_water_filters` | `dds_converter_bgra/emergency_water_filters.dds` | `gfx/interface/decisions/028_asteroid_incoming/emergency_water_filters.dds` | `needs_user_review` |
| E028-DEC-05 | `decision_asteroid_incoming_rebuild_supply_spine` | `GFX_decision_028_supply_spine` | `dds_converter_bgra/rebuild_supply_spine.dds` | `gfx/interface/decisions/028_asteroid_incoming/rebuild_supply_spine.dds` | `needs_user_review` |
| E028-DEC-06 | `decision_asteroid_incoming_restore_outer_ring_industry` | `GFX_decision_028_outer_industry` | `dds_converter_bgra/restore_outer_ring_industry.dds` | `gfx/interface/decisions/028_asteroid_incoming/restore_outer_ring_industry.dds` | `needs_user_review` |
| E028-DEC-07 | `decision_asteroid_incoming_rehouse_displaced_workers` | `GFX_decision_028_worker_rehousing` | `dds_candidates/visual/rehouse_displaced_workers_v001.dds` | `gfx/interface/decisions/028_asteroid_incoming/rehouse_displaced_workers.dds` | `needs_user_review` |
| E028-DEC-08 | `decision_asteroid_incoming_harden_factories_against_dust` | `GFX_decision_028_factory_hardening` | `dds_converter_bgra/harden_factories_against_dust.dds` | `gfx/interface/decisions/028_asteroid_incoming/harden_factories_against_dust.dds` | `needs_user_review` |
| E028-DEC-09 | `decision_asteroid_incoming_protect_transport_reserves` | `GFX_decision_028_transport_protection` | `dds_converter_bgra/protect_transport_reserves.dds` | `gfx/interface/decisions/028_asteroid_incoming/protect_transport_reserves.dds` | `needs_user_review` |
| E028-DEC-10 | `decision_asteroid_incoming_join_observation_network` | `GFX_decision_028_observation_network` | `dds_converter_bgra/atmospheric_observation_network.dds` | `gfx/interface/decisions/028_asteroid_incoming/atmospheric_observation_network.dds` | `needs_user_review` |
| E028-DEC-11 | `decision_asteroid_incoming_secure_crater_perimeter` | `GFX_decision_028_crater_security` | `dds_converter_bgra/secure_crater_perimeter.dds` | `gfx/interface/decisions/028_asteroid_incoming/secure_crater_perimeter.dds` | `needs_user_review` |
| E028-DEC-12 | `decision_asteroid_incoming_survey_extraordinary_material` | `GFX_decision_028_material_survey` | `dds_converter_bgra/survey_extraordinary_material.dds` | `gfx/interface/decisions/028_asteroid_incoming/survey_extraordinary_material.dds` | `needs_user_review` |
| E028-DEC-13 | `decision_asteroid_incoming_fortify_crater_access` | `GFX_decision_028_crater_access` | `dds_converter_bgra/fortify_crater_access.dds` | `gfx/interface/decisions/028_asteroid_incoming/fortify_crater_access.dds` | `needs_user_review` |
| E028-DEC-14 | `decision_asteroid_incoming_reconnoiter_crater_site` | `GFX_decision_028_rival_reconnaissance` | `dds_converter_bgra/reconnoiter_crater_site.dds` | `gfx/interface/decisions/028_asteroid_incoming/reconnoiter_crater_site.dds` | `needs_user_review` |

The existing `GFX_decision_028_rival_disruption` and `GFX_decision_028_rival_offensive` aliases continue to reference that same reconnaissance DDS; they are not separate commissioned art rows.

## Production and candidate lineage

The authoritative per-row source, prompt, processed PNG, staged DDS, SHA-256 values, round-trip paths, and strict validation reports are in `docs/assets/028_asteroid_incoming/regeneration/decisions/v001_20261004/manifest.md`.

The first six rows were recovered from the existing stage rather than regenerated: `mobile_hospitals`, `emergency_rail_corridor`, `clear_unstable_debris`, `emergency_water_filters`, `rebuild_supply_spine`, and `restore_outer_ring_industry`. Hashes were checked against their retained native PNGs, processed previews, official-converter DDS files, round-trips, and validation reports.

All ten PNG outputs in this replacement run's scoped ImageGen output folder `C:\Users\klimp\.codex\generated_images\01a10430-0c15-7362-abbd-f6af3347f98d\` map to retained candidates: two `rehouse_displaced_workers` sources, two `harden_factories_against_dust` sources, and one source for each of `protect_transport_reserves`, `atmospheric_observation_network`, `secure_crater_perimeter`, `survey_extraordinary_material`, `fortify_crater_access`, and `reconnoiter_crater_site`. No orphan result remains in that folder.

The previously specified worker output folder `C:\Users\klimp\.codex\generated_images\01a103aa-0047-7dd0-9525-6cda578adb30\` was inspected only for its task PNG outputs; all sixteen files match already-recorded accepted or rejected candidate lineage. No session history or private task files were inspected.

The first rehousing call returned an image object that was not retained as a usable file path in its tool result. A bounded check of the current task's exact generated-image folder recovered its source as `exec-89668ceb-ea50-422c-9c63-de89f86c4d34.png` with SHA-256 `BDF92D0F06036BAB178A7BAEB4D593DE0F777FD0F6479040065B8AF0F5C80D25`; no separate receipt id is present in the retained result. A v002 source had already been generated before that recovery and is retained as an alternate, not discarded or hidden.

For `rehouse_displaced_workers`, v001 is selected because the figure, backpack, suitcase, and doorway remain more distinct in the 32px and 4x review than in v002. The v002 source, processed preview, official-converter BGRA DDS, round-trip, prompt, hashes, and comparison remain retained.

For `harden_factories_against_dust`, v001 is retained but rejected because two bright red fragments appeared at the filter cap and base. A targeted ImageGen edit produced v002, which preserves the intake assembly, removes those red fragments, and retains genuine transparent unused canvas; v002 is the selected candidate.

For `fortify_crater_access`, the source appeared to have a dark vignette in the black-backed viewer, but its four corners have zero alpha. The cyan composite at `evidence/fortify_crater_access_v001_cyan_composite.png` confirms the background is transparent and the gate/road silhouette has no painted square backdrop; no removal fallback was used.

For `rebuild_supply_spine`, the selected source's apparent viewer vignette was also confirmed to be zero-alpha canvas. A prior U2Net/rembg trial remains separately preserved as an unselected halo-damaged experiment; it is not used in the selected preview or DDS and is not described as a successful fallback.

## Visual and binary review

The native-size sheet is `docs/assets/028_asteroid_incoming/regeneration/decisions/v001_20261004/contact_sheets/decision_icons_native.png`. It compares each processed PNG with its decoded DDS at true 32x32 size.

The checker/cyan source and edge review, smooth 4x preview, and nearest-neighbour DDS inspection sheet is `docs/assets/028_asteroid_incoming/regeneration/decisions/v001_20261004/contact_sheets/decision_icons_zoomed_alpha.png`.

The retained alternate-candidate review is `docs/assets/028_asteroid_incoming/regeneration/decisions/v001_20261004/contact_sheets/decision_icon_candidate_lineage.png`.

The aggregate source-alpha, crop-edge, and exact-PNG-to-DDS audit is `docs/assets/028_asteroid_incoming/regeneration/decisions/v001_20261004/evidence/decision_icons_alpha_and_dds_audit.json`; row-specific strict DDS validation JSON files sit beside the sources.

All fourteen selected source PNGs have real zero-alpha corners. The selected PNG/DDS canvases are exactly 32x32 with transparent corners and alpha extrema `[0,255]`. Each selected DDS is 4224 bytes with a 128-byte legacy header, 32-bit BGRA masks, one level, and exact decoded-pixel equality with its selected processed PNG. Every alpha crop with threshold 1 excludes only alpha-1 pixels; the audit finds no alpha greater than 1 outside any selected crop.

Two sources contain hidden non-black RGB beneath alpha-1 pixels outside their selected crop: `rebuild_supply_spine` has maximum RGB `[79,64,49]` and `fortify_crater_access` has `[97,81,65]`. Their checker/cyan comparisons show no visible coloured fringe; all omitted pixels are alpha 1 and no subject pixels above alpha 1 were cropped.

## Handoff boundary and simplifications

All fourteen icons were produced as separate decision-specific source art. No focus, idea, achievement, or category art was resized or substituted; no primitive or vector placeholder, text, numbers, focus frame, nuclear mark, fantasy gem, or opaque canvas was shipped as selected art.

The production pass changed no GFX, GUI, gameplay, localisation, event, decision, category, catalog, runtime DDS, or Git file. The parent later promoted the selected staged files to the exact registered paths listed above.

No requested icon row was omitted or simplified. The two rival-action aliases retain the already-accepted shared reconnaissance mapping. Parent visual acceptance and runtime promotion are recorded; this handoff does not claim live-game validation.

Skills followed: `chaos-redux-event-assets`, `chaos-redux-subagents` routing/ownership guidance, and the official ImageGen skill with its shared prompting references. Built-in ImageGen was used for every generated icon; no CLI/API fallback and no additional subagent were used.

## Parent runtime promotion record — 2026-10-04

The parent reports that all fourteen promoted DDS files independently passed strict header and 4224-byte checks for one-level BGRA32, exact selected-processed-PNG-to-actual-decoded-DDS pixel comparison, and alpha/corner validation.

The parent preserved fourteen pre-promotion runtime DDS byte hashes and backups under `docs/assets/028_asteroid_incoming/regeneration/decisions/v001_20261004/runtime_before_20261004/`.

The parent promoted thirteen candidates from `dds_converter_bgra/` and the selected `dds_candidates/visual/rehouse_displaced_workers_v001.dds` to the exact registered 32x32 runtime paths in the crosswalk above. All promoted byte hashes match their selected staging candidates.

The retained `rehouse_displaced_workers` v002 alternate was not promoted. The BC3/DXT5 history, rejected art, unselected rembg experiment, and raw-path recovery evidence remain preserved.

This audit and promotion establish texture-file delivery only; decision gameplay, security or supply gates, missions, and native UI behavior remain outside the acceptance recorded here.
