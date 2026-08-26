# Event 014 Cannibal Feast Guard 3D handoff

Historical status notice: this handoff captured the package before parent runtime installation. Feast Guard is one of the seven current bespoke model packages; the old “runtime wiring pending” wording is historical and does not describe Bone Riders or Network Cadre, which use approved vanilla sprites.

Status at handoff: **3D package complete; parent runtime wiring pending**.

The completed package is `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/`. It contains the final PDX mesh, eight distinct Meshy-sourced PDX animations, three 1024 DDS textures, six legally sourced WAV files, provider and Blender checkpoints, grounded reimport reports and previews, and complete manifests. No gameplay, GFX, `.asset`, entity, localisation, or sound-definition source was edited.

## Final model

- Mesh: `export/mesh/cannibal_feast_guard.mesh`, SHA-256 `4F2F8E22B2E479521E48B627D3769383FF48DDD6C95B8EC197639C7068FE7FEE`.
- Geometry reimport: 29,997 triangles, 41,873 vertices, one `map1` UV layer, one 24-bone rig, zero degenerate faces, zero non-manifold edges, and no negative scale.
- Accepted Meshy lineage: generation `01a0334e-9b15-7d8f-9613-35480823152c`, remesh `01a03355-f41d-7165-832b-cc024b02093b`, rig `01a03360-9a5f-7790-b3b8-83e3bb5d1094`.
- Accepted geometry preserves the living, exposed-flesh cannibal silhouette, visible red/blood markings, horned skull mask/bone trophies, rough cloth/leather, and both oversized crude cleavers. It does not read as undead, goblin, knight, or culture-specific warrior.
- Provider-added standalone `Icosphere` was excluded only after proof that it had 42 vertices, no groups/modifiers, and no semantic or topology contact. The immutable provider checkpoint is preserved.
- Material-preserving top-four cleanup affected 293 vertices, removed 302 excess influences, and left no over-four or zero-weight deforming vertex. Mesh identity, weapons, UVs, materials/images, armature metadata, and transforms were preserved.

## Final actions

The eight roles are idle, move, attack, defend, support_attack, retreat, training, and death. All are genuine distinct Meshy clips at 24 FPS, exported through io_pdx_mesh, and reimported. Task IDs, action IDs, frames, hashes, loop policies, and proof locations are in `manifest.md` and `manifest.json`. Final grounding changed only Hips translation for contact correction; no Blender-authored replacement motion or semantic alias exists.

Visual proof anchors:

- `blender/previews/reimport_cannibal_feast_guard_attack_grounded_reimport_frame_056_three_quarter.png`
- `blender/previews/reimport_cannibal_feast_guard_support_attack_grounded_reimport_frame_094_three_quarter.png`
- `blender/previews/reimport_cannibal_feast_guard_death_grounded_reimport_frame_055_three_quarter.png`

## Credits and rejected work

Recorded recovery spend is 134 credits: three 30-credit generations, two rejected 5-credit rigs, one 5-credit remesh, the accepted 5-credit rig, and eight 3-credit animations. Failed rig `01a02a8d-028c-74bb-aec1-dadd88884761` consumed zero. Rejected `01a03317` had catastrophic provider geometry/skinning and weapon loss; rejected `01a0332e` also lost required weapons. No rejected lineage was exported as runtime content.

## Textures, audio, and counters

- Final DDS: `texture_0.dds` SHA `FF35B64D...E18622`, `texture_specular.dds` SHA `34E44845...455BA`, `texture_normal.dds` SHA `FD35624E...ACF61`; each is 1024×1024.
- Six mono 44.1 kHz PCM WAVs cover selection, idle vocal, movement, attack swish, impact, and death. Source pages include OpenGameArt CC0 recordings and Wikimedia Commons public-domain audio; exact URLs, creators, terms, source/derived hashes, probes, and transformations are in `evidence/audio_sources/ffprobe_and_hash_receipt.json` and archived evidence.
- Proposed action sync is recorded in `runtime/handoff.md`.
- Bespoke vanilla-green counter outputs and all three consumer tokens are documented in `event014_cannibal_counter_art_handoff.md`; parent owns registration.

## Dependencies, validation, and parent work

Environment verification on 2026-08-24 returned `findings: []`. Current lock declares official Meshy MCP 0.4.0 with exact `meshy-7`, Blender 5.1.2, io_pdx_mesh 0.91.0, and repository adapter 1.10.0. The shared toolchain advanced while this package was being produced; final export/reimport responses retain embedded adapter metadata 1.8.2, which is explicitly recorded rather than hidden. All eight final exports reported zero warnings and all eight grounded reimports succeeded.

Parent work is limited to byte-preserving runtime copies, entity/`.asset`/GFX/sound-definition creation, action and sound binding, live consumer inspection, and in-game validation. No simplification or missing package asset remains, and no in-game completion is claimed.
