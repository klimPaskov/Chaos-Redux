# Event 013 Natural Disasters photo and category-picture repair

## Scope and result

The report scope is the exact fourteen-card set supplied for this task. All fourteen report cards now use the tilted thin-border and soft-shadow treatment. The drought-famine report remains an untouched frame reference. Two decision-category pictures were replaced. The meteor-impact icons and damaged disaster panel are excluded.

The former painted regional-aftermath scene is now a fictional staged period photograph of flood aftermath and displaced families. The cyclone and extreme-wind photographs were recovered from their saved runtime DDS files by deterministic crops and remounted. Parent review identified that the eleven other listed photos still had straight cream mats, so those existing photographs were also cropped out of their mats and remounted without regeneration. All fourteen cards keep their existing sprite names and texture paths.

## Report-card crosswalk

| Sprite | Resolution | Current texture | Target .gfx |
| --- | --- | --- | --- |
| GFX_report_event_nd_regional_aftermath | Replaced with a generated period flood-aftermath photograph. | gfx/event_pictures/013_natural_disasters/report_event_nd_regional_aftermath.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_tropical_cyclone | Kept the existing photograph and remounted it from crop box x=12..198, y=16..154. | gfx/event_pictures/013_natural_disasters/report_event_nd_tropical_cyclone.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_extreme_wind | Kept the existing photograph and remounted it from crop box x=11..199, y=16..153. | gfx/event_pictures/013_natural_disasters/report_event_nd_extreme_wind.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_tornado_outbreak | Existing storm-damage photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_tornado_outbreak.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_hailstorm | Existing hail-damage photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_hailstorm.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_extreme_cold_wave | Existing cold-wave photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_extreme_cold_wave.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_heat_wave | Existing heat-wave crowd photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_heat_wave.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_wet_mass_movement | Existing valley-damage photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_wet_mass_movement.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_ashfall | Existing ashfall photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_ashfall.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_lahar | Existing lahar-damage photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_lahar.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_storm_surge | Existing storm-surge rescue photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_storm_surge.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_meteor_impact | Existing meteor-impact aftermath photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_meteor_impact.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_meteor_shower | Existing meteor-shower photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_meteor_shower.dds | interface/013_natural_disasters.gfx |
| GFX_report_event_nd_massive_eruption | Existing eruption photo remounted from crop box x=14..196, y=18..156. | gfx/event_pictures/013_natural_disasters/report_event_nd_massive_eruption.dds | interface/013_natural_disasters.gfx |

All fourteen selected report photos now use the same 210x176 card processor. For the eleven newly remounted cards, the selected photo crop is (14,18,196,156); an earlier crop candidate (11,15,199,159) was rejected because a thin mat edge remained. Original DDS files and both crop candidates are retained. Every final DDS differs from its saved original and decodes pixel-for-pixel to its processed preview. The exact before and final 14-card sheets are contact_sheets/013_natural_disasters_reports_before_14.png and contact_sheets/013_natural_disasters_reports_final_14.png. The additional current sheet includes the untouched drought-famine frame reference.

## Decision-category pictures

| Sprite | Final texture | Target .gfx | Reviewed scene |
| --- | --- | --- | --- |
| GFX_decision_cat_picture_nd_winter | gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_winter.dds | interface/013_natural_disasters.gfx | Muted painted snowbound steam train with workers clearing its track. |
| GFX_decision_cat_picture_nd_cyclone | gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_cyclone.dds | interface/013_natural_disasters.gfx | Ground-level painted cyclone landfall with bent palms and storm surge; the sky has no spiral. |

Both source illustrations are generated opaque RGB images. Their processed previews and runtime DDS files are exactly 114x101, remain fully opaque, and pass pixel-exact decode comparisons. The selected prompts and source lineage are in docs/assets/gfx_fix_reports_2026-10/prompts/013_natural_disasters_prompts.md; report and category validation is in docs/assets/gfx_fix_reports_2026-10/notes/013_natural_disasters/dds_validation.json.

## Visual review and remaining integration

Native-size reviews and the before-and-after sheets confirm that all fourteen report cards share the tilted photo frame, the source subjects remain readable, the winter category image is a muted painting, and the cyclone category image is ground-level without the prior spiral-sky composition. The package is ready for the parent's final 14-card review. The main agent can wire the sixteen changed textures through their existing definitions. No GFX or GUI file was edited.

## Final icon and panel integration

Parent final review accepted the fourteen-card remount sheet and both category paintings.
The 53x40 meteor-command symbol is solid and legible; its original alias/path stay registered, but the unified aftermath category has no live use for that old category icon.
It is retained as a corrected reserve rather than being used to invent a new category.
The 760x520 damaged panel has a visible pane crack, localized wear and soot; its slots, controls and grid regions remain aligned.
Matching baseline/post synthetic Corsica earthquake fixtures at 1920x1080 and 1366x768, scale 1, show the new damage while preserving text and click regions.
The source-derived fixture resolves its panel/layer predicates and dynamic text; the root human-player visibility fact and generic unvisited states remain limitations in 013_panel_handoff.md.
Permanent art and MCP proof is under evidence/013/.

Orchestrator live check: use a fresh 1936 human country with an Event 013 aftermath and open the abnormal path map for a partly damaged earthquake path.
At 1920x1080 and 1366x768, the damaged view should show the crack with clear labels and controls; select an undamaged path and confirm the clean background.
Inspect winter and cyclone category pictures, then the fourteen report pictures: the winter picture is a muted colour railway scene, the cyclone is ground-level wind/rain, and all report photos share the tilted thin-edge frame.
There is no live meteor-command category header to test; its registered reserve is covered by native DDS proof.

Skills used: event-assets, imagegen, scripted-gui, subagents, shared-git-commit.
