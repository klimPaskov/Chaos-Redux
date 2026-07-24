# Japan Biological Campaign Decision-Category Icon Manifest

Status: `handed_off`.

This active asset package contains one generated decision-category icon for the Japan biological campaign in China. Runtime wiring remains with the parent agent, which owns `interface/biological_warfare.gfx`.

## Requirement-to-runtime coverage

| Requirement | Asset type | Source package | Processed preview | Runtime asset | Sprite | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `japan_biological_campaign_decision_category_icon` | Decision-category icon | `source_png/japan_biological_campaign_icon_source_master.png` plus `source_png/japan_biological_campaign_icon_source_alpha.png` | `processed_png/decision_category_japan_biological_campaign_52x40.png` | `gfx/interface/decisions/biowarfare/japan_china/decision_category_japan_biological_campaign.dds` | `GFX_decision_category_japan_biological_campaign` | `handed_off` |

## Asset record

- Related feature: Chaos Warfare CBRN, Japan Biological Campaign.
- Asset type: HOI4 decision-category icon.
- Intended use: Category button or decision-system surface for the Japan biological campaign.
- Source mode: `$imagegen` built-in generation.
- Generation state: Existing generated source evidence was usable and was preserved; no regeneration was performed during this completion pass.
- Prompt: `prompts/japan_biological_campaign_icon_prompt.md`.
- Source master: `source_png/japan_biological_campaign_icon_source_master.png`.
- Alpha source: `source_png/japan_biological_campaign_icon_source_alpha.png`.
- Processed preview: `processed_png/decision_category_japan_biological_campaign_52x40.png`.
- Contact sheet: `contact_sheets/decision_category_japan_biological_campaign_contact_sheet.png`.
- Final DDS: `gfx/interface/decisions/biowarfare/japan_china/decision_category_japan_biological_campaign.dds`.
- Native target: `52x40`.
- Sprite identifier: `GFX_decision_category_japan_biological_campaign`.
- Owning `.gfx` file: `interface/biological_warfare.gfx`, to be wired by the parent agent.
- Localisation key: `not_needed` for this asset-only handoff.
- Reference family: canonical `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/`.
- Reference contact sheet inspected before individual references: `icons/decision_categories/contact_sheet.png`.
- Individual style references inspected after the contact sheet: `decision_category_jap_imperial_glory_red.png`, `decision_category_generic_crisis.png`, and `decision_category_generic_communist_revolution.png`.
- Reference PNGs were review-only and were not copied, wired, traced, recoloured, or used as final art.

## Provenance and review

- The retained source master is the original generated RGB PNG with its flat `#00ff00` chroma-key background.
- The retained alpha source is the locally extracted RGBA result used as the source for the existing processed preview.
- The generation prompt records the subject, visual direction, transparent-icon constraints, and built-in ImageGen source mode.
- The source master and alpha source are both `1430x1100`; the source master is RGB and the alpha source is RGBA.
- Visual review found one dominant sealed field-medical flask, a restrained dispatch scroll, a subdued red disc, a dark outline, and a readable silhouette at the native decision-category scale.
- The final preview was reviewed over a checkerboard for transparent corners, no opaque square background, no fake checkerboard pixels, no white matte, no chroma-green residue, and no cross-type focus or idea treatment.
- Detailed measurements and DDS-header validation are recorded in `notes/transparent_processing_verification.md`.

## Wiring handoff

The parent agent should add the stable sprite identifier to `interface/biological_warfare.gfx` and point its texture to the final DDS path listed above. The copy-ready definition and the validation evidence are in `docs/plans/chaos_warfare_system_plans/subagent_handoffs/japan_biological_campaign_icon_handoff.md`.
