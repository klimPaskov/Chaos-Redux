# Stage 7 Biological Warfare Asset Package

## Package scope

One bespoke Chaos Redux decision icon for the stable decision id `bio_designate_strategic_raid_staging_state`.

The Stage 7 package also contains a separate stockpile-safety family under
`stockpile_risk_ideas/`: four independently generated 60x68 national-spirit
icons for Controlled, Strained, Dangerous, and Critical risk, plus one
independently generated 32x32 arsenal-designation decision icon. Its source,
processed PNGs, DDS validation, contact sheet, hashes, and prompt record are
owned by `stockpile_risk_ideas/manifest.md`.

The icon depicts a sealed biological payload containment canister being transferred beneath an air-base hangar and aircraft silhouette, with a visible locked staging marker. The palette is restrained charcoal/gunmetal with desaturated teal and amber hazard accents. It contains no gore, exposed biological material, or generated text, and it is not a generic biohazard-only symbol.

## Asset manifest

| Field | Value |
|---|---|
| Asset id | `bio_designate_strategic_raid_staging_state` |
| Asset type | Decision icon |
| Intended in-game use | Stage 7 Chaos Warfare biological-warfare decision |
| Source mode | `$imagegen` built-in generation, followed by local chroma-key removal and resizing |
| Target size | `32x32` |
| Intended sprite | `GFX_decision_bio_designate_strategic_raid_staging_state` |
| Related decision id | `bio_designate_strategic_raid_staging_state` |
| Source PNG | `docs/assets/chaos_warfare_system/stage_7_biological_warfare/source_png/bio_designate_strategic_raid_staging_state_source.png` |
| Intermediate alpha cutout | `docs/assets/chaos_warfare_system/stage_7_biological_warfare/source_png/bio_designate_strategic_raid_staging_state_cutout.png` |
| Processed PNG | `docs/assets/chaos_warfare_system/stage_7_biological_warfare/processed_png/bio_designate_strategic_raid_staging_state.png` |
| Alpha-check preview | `docs/assets/chaos_warfare_system/stage_7_biological_warfare/processed_png/bio_designate_strategic_raid_staging_state_alpha_checker.png` |
| Final DDS | `gfx/interface/decisions/biowarfare/bio_designate_strategic_raid_staging_state.dds` |
| `.gfx` file | `interface/biological_warfare.gfx` |
| Prompt/source record | `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prompts/bio_designate_strategic_raid_staging_state.md` |
| Validation record | `docs/assets/chaos_warfare_system/stage_7_biological_warfare/validation.md` |
| GFX handoff | `docs/assets/chaos_warfare_system/stage_7_biological_warfare/gfx_handoff.md` |
| Status | `complete` |

## Stockpile-safety runtime handoff

| Asset | Sprite | Runtime file |
|---|---|---|
| Controlled risk | `GFX_idea_bio_stockpile_risk_controlled` | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_controlled.dds` |
| Strained risk | `GFX_idea_bio_stockpile_risk_strained` | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_strained.dds` |
| Dangerous risk | `GFX_idea_bio_stockpile_risk_dangerous` | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_dangerous.dds` |
| Critical risk | `GFX_idea_bio_stockpile_risk_critical` | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_critical.dds` |
| National arsenal designation | `GFX_decision_bio_designate_national_biological_arsenal` | `gfx/interface/decisions/biowarfare/bio_designate_national_biological_arsenal.dds` |

All five sprites are registered in `interface/biological_warfare.gfx`. The
arsenal decision is storage management only. Deliberate agent deployment remains
in the native raid system. Existing files under `gfx/interface/military_raids/`
were neither replaced nor modified.

## Reference analysis

The matching Chaos Redux decision reference folder was inspected before generation:

`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions/`

The generated composition follows the references' small-icon treatment: one dominant symbolic subject, compact framing, dark edge contrast, limited fine detail, and a transparent unused background at runtime. The decision icon was created independently for 32x32 and was not derived from a focus or idea icon.

## Source note

The source image is a fictional/generated symbolic asset. The chroma-key green background exists only in the preserved source PNG so the generation provenance remains inspectable. It is removed in the intermediate cutout and is not present in the processed PNG or runtime DDS.

No real photograph, archival image, or copyrighted source image was used. No placeholder or cross-type substitute was used.

## Hashes

SHA-256 values are recorded in `validation.md` for the preserved source, alpha cutout, processed PNG, and final DDS.
