# Asset manifest: The County Fair Returns

## Requirement-to-runtime coverage

| Requirement | Intended use | Source package | Runtime output | Consumer / registration | Status |
| --- | --- | --- | --- | --- | --- |
| `fallout_county_fair_returns_report` | Fictional Fallout county-fair report event image for the reviewed chain “The County Fair Returns” | `source_png/fallout_county_fair_returns_source.png` → `processed_png/fallout_county_fair_returns_processed.png` | `gfx/event_pictures/fallout_world_end/report_event_fallout_county_fair_returns.dds` | Proposed sprite `GFX_report_event_fallout_county_fair_returns`; main agent-owned `.gfx` registration and event consumer | handed_off |

## Asset details

- Asset name: `fallout_county_fair_returns_report`.
- Related event slug: `air_cleanliness_fallout`, chain “The County Fair Returns”.
- Asset type: fictional alternate-history report event image.
- Intended in-game use: report event picture for the Fallout rural county-fair scene.
- Source mode: `$imagegen` generated source followed by the repository report-card processor.
- Source rationale: the scene is fictional and highly specific, so a generated period-documentary composition fits better than sourcing a real photograph.
- Generation prompt: [`prompts/fallout_county_fair_returns_imagegen_prompt.md`](prompts/fallout_county_fair_returns_imagegen_prompt.md).
- Source PNG: [`source_png/fallout_county_fair_returns_source.png`](source_png/fallout_county_fair_returns_source.png), RGB, 1537x1023.
- Processed PNG preview: [`processed_png/fallout_county_fair_returns_processed.png`](processed_png/fallout_county_fair_returns_processed.png), RGBA, exactly 210x176, black-and-white with sepia, documentary-card tilt, soft shadow, and transparent corners.
- Final DDS: [`gfx/event_pictures/fallout_world_end/report_event_fallout_county_fair_returns.dds`](../../../../gfx/event_pictures/fallout_world_end/report_event_fallout_county_fair_returns.dds), legacy uncompressed BGRA, exactly 210x176.
- SHA-256 provenance: source `2E42A56811D76EF4C6A0CD0580F37A11D7E38F16D600E00E51BBA676583D813D`; processed `F1FC270777820BD2CE5161504ED3548DCC5A032BFA1087ABCA22E2FCFFB3772A`; DDS `C82788E70CFD5DEF65D19FCA4F73F08DCF0FC17102038086FD12D787EEDD682A`.
- Preview/contact evidence: [`contact_sheets/fallout_county_fair_returns_contact.png`](contact_sheets/fallout_county_fair_returns_contact.png).
- Proposed sprite name: `GFX_report_event_fallout_county_fair_returns`.
- Target `.gfx`: existing event-picture `.gfx` selected by the main agent; this subagent does not edit `.gfx` files.
- Localisation key: not supplied and not edited by this subagent.
- Source provenance: original fictional artwork generated in this task with the official built-in ImageGen tool; no real person, real location, copyrighted source, or internet source was used.
- World War II / period-fit note: the documentary treatment follows the report family’s period visual language, while patched late-1940s clothing and salvaged agricultural machinery depict the fictional post-Fallout timeline.
- Runtime filename reconciliation: the provisional `fallout_county_fair` folder and DDS name were renamed to the addendum’s stable `_returns` consumer names before handoff. No provisional runtime DDS remains.
- Status: `handed_off`; the source, processed preview, DDS, provenance, and handoff are complete, while `.gfx` registration and event wiring remain main-agent scope.

## Validation evidence

- Processed PNG decodes as RGBA `(210, 176)`.
- All four processed PNG corners have alpha `0`; alpha range is `0..255`.
- DDS length is `147968` bytes, matching `128 + 210 * 176 * 4`.
- DDS header uses `DDS ` magic, header size `124`, declared height `176`, declared width `210`, pixel-format size `32`, flags `65`, fourCC `0`, 32-bit BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`, and `DDSCAPS_TEXTURE` `0x1000`.
- The report-card processor used was `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`.
- The DDS converter used was `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.
