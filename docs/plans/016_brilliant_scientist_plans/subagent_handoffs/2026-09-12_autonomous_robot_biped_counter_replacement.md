# Autonomous robot biped counter replacement handoff

Disposition: `implemented` for the bounded asset package; review state: `needs_user_review` pending independent parent visual review.

Date: 2026-09-12.

Owner: `chaosx_icon_artist` asset subagent.

## Scope and ownership

The package replaces the wrong tracked counter art for the existing shared `autonomous_robot` consumer used by Event016/Event019.

Only `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter_biped_20260912/` and this handoff were edited.

No GFX, gameplay, shared manifest, runtime, Blender, Meshy, or paid generation file was edited.

The parent owns runtime promotion, GFX review, final integration, and live-game validation.

## Consumer and exact outputs

The live token is `autonomous_robot` in `common/units/016_brilliant_scientist_project_forces.txt`, with `sprite=autonomous_robot` and `map_icon_category=armored`.

The existing `interface/autonomous_robot_system.gfx` large bindings consume `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds` with two 76x42 frames inside a 152x42 canvas.

The existing `_white` map binding consumes `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds` with two 30x12 frames inside a 60x12 canvas.

The candidate large DDS is `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter_biped_20260912/final/unit_autonomous_robot_icon.dds` with SHA256 `8F374ADF045A0AD24B5BE39C220F65A27346F4FB3942F7D335EE3923C12896EF`.

The parent promotion path for the large DDS is `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds`.

The candidate small DDS is `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/counter_biped_20260912/final/onmap_unit_autonomous_robot_icon.dds` with SHA256 `C259EAD5749C82D2881EF17CF528413795C6042BA27CB9038563AD13631357DC`.

The parent promotion path for the small DDS is `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds`.

Matching evidence PNGs are `final/unit_autonomous_robot_icon.png` with SHA256 `1EECF0A0A3C976F9B32F5158DAB11B6F493FA396DF8C77DC811A01FEE25E8510` and `final/onmap_unit_autonomous_robot_icon.png` with SHA256 `AB9BFF06EB876044374BA8C0FA4306B7CFC60DFD91D174F146A534BB397F3569`.

## Visual result

The large frame order is frame 0 compact muted vanilla-green biped and frame 1 distinct pale sparse schematic.

The small map frame order is frame 0 pale grayscale biped silhouette and frame 1 distinct pale grayscale sparse schematic for the `_white` consumer.

The identity is a squat humanoid biped with two separate armored legs and feet, an olive riveted broad tank-steel torso, a round goggle sensor head, two separate forearm-mounted machine guns, compact feeds and backpack, and no tracks, wheels, text, flags, or logos.

The large green ramp uses the inspected anchors `(73,106,73)`, `(81,113,81)`, `(119,144,119)`, `(151,170,151)`, `(186,199,186)`, and `(198,208,198)` plus dark anchors `(32,44,32)`, `(9,13,9)`, and `(0,0,0)`.

The map strip remains grayscale in both frames because fresh inspection of the installed `_white` family showed no green map state.

## Source lineage and alpha

Source mode is original native ImageGen counter raster informed by the approved robot identity references and installed vanilla counter vocabulary.

The approved identity references were read-only inputs at `docs/assets/shared_robot_system/models_3d/autonomous_robot/blender/previews/rbfinal_training_000_front.png` and `docs/assets/shared_robot_system/models_3d/autonomous_robot/blender/previews/rbfinal_attack_017_right.png`.

The accepted source model checkpoint hash is `2EBBF34D1E1F4506D042C51CB00DDD3CA87F6E74C33A2112824F431259974114`.

The large green native candidate is `source/large_green_biped_source.png` from ImageGen candidate `exec-5a133876-ccdc-467e-89e1-200fac988593`.

The large schematic began as opaque candidate `exec-7b20de7e-d758-4412-a3bf-fcf3808b0cbc` and uses the successful targeted transparency edit `exec-96864870-b983-4093-a097-67615659e91e` as `source/large_schematic_source_alpha.png`.

The map silhouette began as opaque candidate `exec-9cfbe261-d6e4-434d-845c-613ee488caba` and the first transparency edit `exec-835ff4a4-319d-449b-a406-dc08974da5d6` remained opaque and is rejected evidence.

The selected map silhouette source is a uniform chroma edit `exec-df8e5b82-3843-483d-8f46-216fee5326ac` processed by the verified local `C:\Users\klimp\.codex\skills\.system\imagegen\scripts\remove_chroma_key.py` fallback with `--auto-key corners --soft-matte --transparent-threshold 18 --opaque-threshold 96 --spill-cleanup --force`.

The untouched opaque map sources, failed edit, chroma source, and fallback output are retained in `source/`, with exact hashes and alpha bounds in `validation/alpha_lineage.json`.

The previous wrong tracked counter is preserved as rejected evidence in `rejected_previous/wrong_tracked_counter_contact_sheet.png`, and its original package remains at `../counter/`.

## Validation and review evidence

`validation/process_counter_biped.py` performs alpha-threshold crop with padding, premultiplied Lanczos downsampling, inspected vanilla palette mapping, and alpha-preserving two-frame assembly.

`validation/validate_counter_biped.py` passed strict 128-byte uncompressed BGRA DDS header checks, dimensions, pitch, byte length, alpha extrema, frame occupancy, distinct frame states, green palette consistency, map grayscale, and exact PNG-to-DDS decoded pixel equality.

The validation receipt is `validation/dds_validation.json`.

The exact installed definition and family inspection are recorded in `validation/reference_inspection.md` and the parent-supplied `docs/assets/shared_robot_system/models_3d/autonomous_robot/attempts/20260906_weaponfree_blender/evidence/finalize_20260912/counter_vanilla_inspection.json`.

The native-pixel review sheet is `contact_sheet/counter_contact_sheet_native.png`.

The smooth enlarged review sheet is `contact_sheet/counter_contact_sheet_enlarged.png`.

The final DDS decoded nearest-pixel neutral-matte contact proof is `validation/dds_roundtrip_neutral_matte_contact.png`.

Both contact sheets show selected sources, processed target strips, final DDS roundtrips, installed decoded vanilla large/map references, and the rejected prior package.

No in-game validation is claimed.

## Parent review actions

The parent should independently review both contact sheets, promote only the candidate DDS files after acceptance, and carry out the repository/runtime/live-game checks outside this asset package.
