# Autonomous Robot counter art handoff

Owner: `chaosx_icon_artist`.

Status: generated, processed, converted, and handed off as bespoke shared counter art; `needs_user_review` remains until the parent reviews the contact sheet, registers the sprites, and validates the live Event016/Event019 consumers.

This is generic shared API art for the autonomous robot unit and is not Kruger-named art. The source depicts a retro-WW2 riveted armored humanoid robot with a broad tank-like torso, helmeted sensor head, and integrated machine guns in both forearms. It has no text, Kruger marks, or national insignia.

## Final runtime outputs

- Large division strip: `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds` (`152x42`, two `76x42` frames).
- On-map strip: `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds` (`60x12`, two `30x12` frames).
- Large runtime/evidence SHA-256: `147cf90c3d053947640f7865f1dade6d8ffaba99942e8401ed4575d53db61b09`.
- On-map runtime/evidence SHA-256: `bdeb527f8a73494b918adec27c26aec97c299f51ad00d2da2946a37a278edd4b`.
- Both runtime copies are byte-identical to their evidence DDS copies and decode pixel-exactly to their processed PNG sheets.

No gameplay, entity, model, sound, localisation, spreadsheet, or interface `.gfx` file was edited by this handoff.

## Sprite registration handoff

- `GFX_group_autonomous_robot_icon` → `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds`, `noOfFrames = 2`.
- `GFX_unit_autonomous_robot_icon_medium` → `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds`, `noOfFrames = 2`.
- `GFX_unit_autonomous_robot_icon_medium_white` → `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds`, `noOfFrames = 2`.

The parent owns the final `.gfx` file and runtime consumer wiring. Event016 and Event019 should reference the generic autonomous robot sprite/token rather than event-specific or Kruger-named art.

## Source and processing evidence

- Large native ImageGen source: `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter/source/autonomous_robot_large_atlas_source.png`, SHA-256 `9d1a0c858529d7cd6dbd83201929c9cda033fa21ca78229351bdd7f4d4a07ce`.
- On-map native ImageGen source: `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter/source/autonomous_robot_map_atlas_source.png`, SHA-256 `3321e61c7c7d3b8724bd5a12525b952e4d9e1b5f3f1a673b44c3e3ada96d8919`.
- Prompt files: `source/autonomous_robot_large_atlas_prompt.txt` and `source/autonomous_robot_map_atlas_prompt.txt`.
- Approved alpha outputs: `source/autonomous_robot_large_atlas_alpha.png` and `source/autonomous_robot_map_atlas_alpha.png`.
- Processed large PNG SHA-256: `1a373842f8ce402a8404ec79a3826316a54c8015c3ac836bff3ef56ab6002656`.
- Processed on-map PNG SHA-256: `3d29f95c3985f6af72366aa710892b7576ab8f398283cb560efc572ec0eca07f`.
- Processing used the official `remove_chroma_key.py` helper with border auto-key, soft matte, threshold cleanup, and spill cleanup, then `convert_to_dds.py` for the final 32-bit uncompressed BGRA outputs.
- Large frames retain the full ImageGen tracked robot; on-map frames use an ImageGen-derived upper-body reduction so the head, broad torso, and dual forearm guns remain readable at `30x12`.

## Vanilla reference gate

The matching canonical contact sheets were inspected before generation at:

- `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/contact_sheet.png`.
- `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/contact_sheet.png`.

The exact installed definitions were inspected in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx` (SHA-256 `0d7b62caf328b3c296ec27ab85318f3cc78cc760b02923538bf5240815963335`). Medium armor and mechanized definitions both use two-frame large `152x42` textures, while their white on-map definitions use two-frame `60x12` textures. Installed references are legacy `124`-byte-header, 32-bit uncompressed BGRA DDS with alpha transparency and masks `0x00ff0000`, `0x0000ff00`, `0x000000ff`, `0xff000000`.

Reference DDS hashes: medium-tank large `eb442eb0aab913a70212e11602ce44f0991af94afe9b7e34cf770d0ac0206510`, medium-tank on-map `e8442769994e4d4ca1028156c9e40e291ed856cde68651fc47dc5896a2b253d8`, mechanized large `6a6902c19a776781f759faef097075f40ade67743cb0938dd0c404324542ed0b`, and mechanized on-map `2f472f8008f06023b9bee357f31d2aa70fbd07e7efc92311f3d76e0bb0da7b38`.

The selected-state ramp uses sampled vanilla green anchors `(73,106,73)`, `(81,113,81)`, `(119,144,119)`, `(151,170,151)`, `(186,199,186)`, and `(198,208,198)` with dark anchors `(32,44,32)`, `(9,13,9)`, and `(0,0,0)`. Frame 0 is green; frame 1 is the pale/white alternate state.

## Review and validation

- Contact sheet: `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter/contact_sheet.png`, SHA-256 `463c2d5484950c9a569b04838efb164b3afc60f1c2363cec990114bd16d19c36`.
- Manifest: `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter/manifest.md`.
- Sprite handoff: `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter/gfx_handoff.md`.
- Reference inspection: `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter/validation/reference_inspection.md`.
- DDS evidence: `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter/validation/dds_validation.json`.

Remaining boundary: parent review and live consumer validation are pending. No art simplification or unauthorized fallback was used; the only target-specific adaptation is the ImageGen-derived upper-body reduction for the tiny on-map surface.
