# Hidden technology icons handoff

Date: 2026-08-14.

Owner: `/root/hidden_tech_icons`.

Status: complete for 21 new static assets, with the existing clone-infantry asset preserved unchanged.

## Deliverables

The package has native ImageGen source masters, exact-size processed transparent PNGs, native-size contact sheet, decoded DDS round-trips, manifest, and runtime DDS files.

The requested canvas is 132x52 for every new asset.

All new DDS files are one-level uncompressed 32-bit BGRA, 27584 bytes, with pixel-format flags 65, fourCC 0, masks `00FF0000/0000FF00/000000FF/FF000000`, and alpha range 0-255.

The equipment item is independently composed native art for `GFX_autonomous_robot_equipment_medium`; it is not a resize or reuse of a technology icon.

## Runtime DDS and exact SHA256

| Sprite | Runtime DDS | SHA256 |
| --- | --- | --- |
| `GFX_brilliant_scientist_clone_formations_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_clone_formations.dds` | `92142bb538583c64892379fc84b33f788d27e7c371268e859cdf1f929dc1e031` |
| `GFX_brilliant_scientist_clone_formations_weaponization_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_clone_formations_weaponization.dds` | `c6386e58a9842a5e438f5d6a7062be34dee1b319a6e77bfd8cccd53c5dc6e1d4` |
| `GFX_brilliant_scientist_alien_infantry_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_alien_infantry.dds` | `e54d92457c710e2781ff31ebba7892f18431da64b21a9319a7f3a3874eacfca9` |
| `GFX_brilliant_scientist_alien_predictive_warfare_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_alien_predictive_warfare.dds` | `8a65df3c56bd4f879c498a5579b703915c5a935c3e2832658bfdf72e91dd5238` |
| `GFX_brilliant_scientist_paleogenetic_formations_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_paleogenetic_formations.dds` | `4a21d4bff33e71c05e98ebf18b67f6d021877635c351211edb62627832a9300e` |
| `GFX_brilliant_scientist_paleogenetic_formations_weaponization_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_paleogenetic_formations_weaponization.dds` | `edc5f5be8b523b247040fd703e86e10b17cd963c9e19a7efd49e93cd28c4e884` |
| `GFX_brilliant_scientist_portal_warfare_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_portal_warfare.dds` | `2fdd90b1246f13fb8e9243f6b0f64e289d148d84dd5c12a85ad828b34c7c0993` |
| `GFX_brilliant_scientist_portal_warfare_weaponization_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_portal_warfare_weaponization.dds` | `ed69e3dfbfe81ec73a7b1221035a9779c150cacc86e2560a3a3cd18280bcee8f` |
| `GFX_brilliant_scientist_robot_formations_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_robot_formations.dds` | `bf54fe656d4b976ec0f2b5cce0597a73a7e7dae61044c2f0d2afad7ae48abaf0` |
| `GFX_brilliant_scientist_robot_formations_weaponization_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_robot_formations_weaponization.dds` | `b6151923274ebbc9669ded555bdeefd292e78ab0a8dac7807da32f228f7b2fd4` |
| `GFX_brilliant_scientist_temporal_guard_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_temporal_guard.dds` | `74fb332ee4f9d781ade4ea00b26b23fc326cb004967f1269fce6ed7d3670d1b3` |
| `GFX_brilliant_scientist_temporal_guard_weaponization_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_temporal_guard_weaponization.dds` | `fbc046aa7c13219c6890908984749d88e87c0a87ed3d99f1486362b79d53284b` |
| `GFX_brilliant_scientist_xeno_chemical_control_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_xeno_chemical_control.dds` | `738818b8817a3f94ef5a24e58397bd7add92fb2db08dd9d9654174778ead4eea` |
| `GFX_brilliant_scientist_xeno_machine_control_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_xeno_machine_control.dds` | `fe822b641fe04cd97b0858b763797868b76415c12b2c934da1bcbc77b44f4551` |
| `GFX_brilliant_scientist_xeno_neural_control_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_xeno_neural_control.dds` | `cd338183ffc16e8cf3c6e56d95c2a4f3e4aa0ca75239c59ebd1a1879a51a2411` |
| `GFX_brilliant_scientist_xeno_researched_control_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_xeno_researched_control.dds` | `7b00c42bb0016c18dbd38db9a84d1648bcb054dc92d3069ac450c71deadcfe9f` |
| `GFX_brilliant_scientist_xenobiological_formations_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_xenobiological_formations.dds` | `dbf02b4dcdb4eba3c1c2dfcccfdd509344c329bbda0aece426fb38923264c07e` |
| `GFX_brilliant_scientist_xenobiological_formations_weaponization_tech_medium` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_xenobiological_formations_weaponization.dds` | `d3123035dc2bef951535eea8bd6e5aab58321f4c339455e18a347fa503475c78` |
| `GFX_mengele_aryan_clone_refinement_tech_medium` | `gfx/interface/technologies/shared_clone_system/tech_shared_clone_system_mengele_aryan_clone_refinement.dds` | `6765089b12d7d47b1b76c587307b9015198d64aae8334e8a7423443957a066f0` |
| `GFX_mengele_clone_refinement_tech_medium` | `gfx/interface/technologies/shared_clone_system/tech_shared_clone_system_mengele_clone_refinement.dds` | `3afda98dd912510e1119cb00f7f4d6c69e1a347d07040828d7da2a5ef41557b4` |
| `GFX_autonomous_robot_equipment_medium` | `gfx/interface/technologies/shared_robot_system/autonomous_robot_equipment.dds` | `8ba187b7e64a7f9dd325888b0d8e553140f9183dde55ba85db3d6ca6547150e0` |

The existing `GFX_clone_infantry_access_tech_medium` remains at `gfx/interface/technologies/clone_infantry_access_tech.dds` with SHA256 `39b356a06d68b05c4baa60dcfe93f3439f821f47ede0d2130672f9ac3ed22adb`.

## Evidence paths

- Contact sheet: `docs/assets/016_brilliant_scientist/technology_icons/contact_sheet/technology_icons_contact_sheet.png`.
- Machine-readable manifest: `docs/assets/016_brilliant_scientist/technology_icons/manifest.json`.
- Prompt briefs: `docs/assets/016_brilliant_scientist/technology_icons/prompts/README.md`.
- Native ImageGen sources: `docs/assets/016_brilliant_scientist/technology_icons/source_png/`.
- Processed PNGs: `docs/assets/016_brilliant_scientist/technology_icons/processed_png/`.
- Decoded DDS round-trips: `docs/assets/016_brilliant_scientist/technology_icons/decoded_dds/`.
- Detailed GFX handoff: `docs/assets/016_brilliant_scientist/technology_icons/gfx_handoff.md`.

## Reference and validation evidence

The canonical technology contact sheet and individual technology reference family were inspected under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/technologies`.

Installed vanilla `interface/Technologies.gfx` and representative `gfx/interface/technologies/infantry3.dds` were inspected before generation.

The installed project `interface/clone_system.gfx` and existing clone DDS were inspected before generation and the existing asset was left untouched.

The project technology definitions and autonomous robot equipment definition were inspected to keep semantic assignments and the provider-neutral `picture = autonomous_robot_equipment` consumer aligned.

The DDS decoder verified every new file's dimensions, header, byte length, alpha range, and PNG round-trip hash.

The contact sheet was visually reviewed at native-size rows and enlarged inspection rows, confirming distinct technology-specific compositions and transparent edges.

## Ownership boundary and blockers

This handoff contains art, evidence, and handoff documentation only.

Parent-owned `.gfx` registration remains intentionally unedited.

There are no asset-production blockers.

No commit was created.
