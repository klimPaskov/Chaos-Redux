# Autonomous robot biped counter replacement handoff

Disposition: `implemented` for the bounded asset package; review state: `implemented; parent-promoted` in commit `475839ff20`.

Date: 2026-09-12.

Owner: `chaosx_icon_artist` asset subagent.

## Scope and ownership

The package replaces the wrong tracked counter art for the existing shared `autonomous_robot` consumer used by Event016/Event019.

Only `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter_biped_20260912/` and this handoff were edited.

No GFX, gameplay, shared manifest, runtime, Blender, Meshy, or paid generation file was edited.

The parent promoted the accepted DDS pair in commit `475839ff20`; live-game validation remains user-owned.

## Consumer and exact outputs

The live token is `autonomous_robot` in `common/units/016_brilliant_scientist_project_forces.txt`, with `sprite=autonomous_robot` and `map_icon_category=armored`.

The existing `interface/autonomous_robot_system.gfx` large bindings consume `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds` with two 76x42 frames inside a 152x42 canvas.

The existing `_white` map binding consumes `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds` with two 30x12 frames inside a 60x12 canvas.

The candidate large DDS is `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter_biped_20260912/final/unit_autonomous_robot_icon.dds` with SHA256 `95E8A0816A614FEA7449494A026A1C57ED6B76D384C3ADEF933F1DE964E7CDDC`.

The parent promotion path for the large DDS is `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds`.

The candidate small DDS is `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter_biped_20260912/final/onmap_unit_autonomous_robot_icon.dds` with SHA256 `1115AACD9A57653E07BF30915649B0DDDB399253A0ACE59E6078C89ACB01E3C2`.

The parent promotion path for the small DDS is `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds`.

Matching evidence PNGs are `final/unit_autonomous_robot_icon.png` with SHA256 `9F1D5E52D9345261C4B72336A70D561D3A91A72129CE7D67F446A5D7F37FA237` and `final/onmap_unit_autonomous_robot_icon.png` with SHA256 `3AE76390D02B1E0E2007E4BBCE1A4B551239414AB1078D9B691F2ACB616861EE`.

## Visual result

The large frame order is frame 0 compact muted vanilla-green biped and frame 1 distinct pale filled rectangular field with dark border and dark sparse biped schematic strokes, with transparent canvas outside the field.

The small map frame order is frame 0 pale grayscale biped silhouette and frame 1 distinct pale filled rectangular field with dark border and dark sparse biped schematic strokes for the `_white` consumer, with transparent canvas outside the field.

The identity is a squat humanoid biped with two separate armored legs and feet, an olive riveted broad tank-steel torso, a round goggle sensor head, two separate forearm-mounted machine guns, compact feeds and backpack, and no tracks, wheels, text, flags, or logos.

The large green ramp uses the inspected anchors `(73,106,73)`, `(81,113,81)`, `(119,144,119)`, `(151,170,151)`, `(186,199,186)`, and `(198,208,198)` plus dark anchors `(32,44,32)`, `(9,13,9)`, and `(0,0,0)`.

The map strip remains grayscale in both frames because fresh inspection of the installed `_white` family showed no green map state.

## Source lineage and alpha

Source mode is original native ImageGen counter raster informed by the approved robot identity references and installed vanilla counter vocabulary.

The approved identity references were read-only inputs at `docs/assets/shared_robot_system/models_3d/autonomous_robot/blender/previews/rbfinal_training_000_front.png` and `docs/assets/shared_robot_system/models_3d/autonomous_robot/blender/previews/rbfinal_attack_017_right.png`.

The accepted source model checkpoint hash is `2EBBF34D1E1F4506D042C51CB00DDD3CA87F6E74C33A2112824F431259974114`.

The large green native candidate is `source/large_green_biped_source.png` from ImageGen candidate `exec-5a133876-ccdc-467e-89e1-200fac988593`.

The former detailed large schematic began as opaque candidate `exec-7b20de7e-d758-4412-a3bf-fcf3808b0cbc` and the targeted transparency edit `exec-96864870-b983-4093-a097-67615659e91e` is retained as rejected evidence because it was an illustrated robot state.

The selected second state is native ImageGen flat emblem candidate `exec-137c9c79-8283-466c-a48f-30ddebeda11a`, retained as `source/large_schematic_source_alpha.png` and shared as `source/map_schematic_source.png`.

The source emblem contains only a thin unfilled pale rectangle, a small square head, short torso stem, two arm/gun ticks, two diagonal leg ticks, and two foot ticks, with no armor panels, eyes, perspective, volume, or illustrated highlights. The processor preserves this geometry while filling the rectangle pale and darkening the existing border and biped masks to match the installed vanilla second-state field behavior.

The map silhouette began as opaque candidate `exec-9cfbe261-d6e4-434d-845c-613ee488caba` and the first transparency edit `exec-835ff4a4-319d-449b-a406-dc08974da5d6` remained opaque and is rejected evidence.

The selected map silhouette source is a uniform chroma edit `exec-df8e5b82-3843-483d-8f46-216fee5326ac` processed by the verified local `C:\Users\klimp\.codex\skills\.system\imagegen\scripts\remove_chroma_key.py` fallback with `--auto-key corners --soft-matte --transparent-threshold 18 --opaque-threshold 96 --spill-cleanup --force`.

The untouched opaque map sources, failed edit, chroma source, and fallback output are retained in `source/`, with exact hashes and alpha bounds in `validation/alpha_lineage.json`.

The former detailed map schematic `exec-d7f46960-600a-4125-8b18-d97f4653e710` is retained as `source/map_schematic_illustrated_rejected.png`.

The previous wrong tracked counter is preserved as rejected evidence in `rejected_previous/wrong_tracked_counter_contact_sheet.png`, and its original package remains at `../counter/`.

## Validation and review evidence

`validation/process_counter_biped.py` performs alpha-threshold crop with padding, native-resolution source-mask pale field/dark border processing for frame 1, one premultiplied Lanczos downsample, inspected vanilla palette mapping, and alpha-preserving two-frame assembly.

`validation/validate_counter_biped.py` passed strict 128-byte uncompressed BGRA DDS header checks, dimensions, pitch, byte length, alpha extrema, frame occupancy, distinct frame states, green palette consistency, pale filled frame-1 field with dark border/strokes, map grayscale, and exact PNG-to-DDS decoded pixel equality.

The validation receipt is `validation/dds_validation.json`.

The exact installed definition and family inspection are recorded in `validation/reference_inspection.md` and the parent-supplied `docs/assets/shared_robot_system/models_3d/autonomous_robot/attempts/20260906_weaponfree_blender/evidence/finalize_20260912/counter_vanilla_inspection.json`.

The native-pixel review sheet is `contact_sheet/counter_contact_sheet_native.png`.

The smooth enlarged review sheet is `contact_sheet/counter_contact_sheet_enlarged.png`.

The final DDS decoded nearest-pixel neutral-matte contact proof is `validation/dds_roundtrip_neutral_matte_contact.png`.

Both contact sheets show selected sources, processed target strips, final DDS roundtrips, installed decoded vanilla large/map references, and the rejected prior package.

No in-game validation is claimed.

## Parent review actions

The parent independently reviewed the contact sheets and promoted the accepted DDS files in commit `475839ff20`. Live-game validation remains user-owned.
