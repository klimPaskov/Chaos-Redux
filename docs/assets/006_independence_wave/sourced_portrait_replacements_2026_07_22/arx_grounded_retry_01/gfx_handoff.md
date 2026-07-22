# ARX grounded retry 01 - GFX handoff

This is a documentation-only handoff. No `interface/*.gfx`, gameplay
character file, runtime DDS, or localisation file was edited by this package.
Both candidates remain `needs_user_review`; the paths below are deferred until
rights, visual treatment, and parent role decisions are complete.

## Deferred consumers

### Crown / consultative council

- Current consumer: `ARX_sardinian_crown_consultative_council`
- Current fictional identity: `ARX_vittorio_pala`
- Current sprite key: `GFX_portrait_ARX_independence_wave_vittorio_pala`
- Existing runtime path (do not overwrite in this handoff):
  `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_vittorio_pala.dds`
- Research candidate: Prince Eugenio di Savoia-Genova, Duke of Ancona / fifth
  Duke of Genoa
- Immutable source master:
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/source_masters/sardinia/arx_eugenio_savoia_genova_1920s_original.jpg`
- Mechanical preview:
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/crop_previews/sardinia/arx_eugenio_savoia_genova_1920s_preview.png`
- Suggested eventual sprite definition after approval and approved native
  portrait processing (do not paste into a `.gfx` file yet):

  ```
  spriteType = {
      name = "GFX_portrait_ARX_independence_wave_eugenio_savoia_genova"
      texturefile = "gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_eugenio_savoia_genova.dds"
  }
  ```

  The exact final DDS path and whether the parent keeps the current sprite key
  or renames it belong to the main implementation agent.

### Army / coastal or mountain command

- Current consumer: `ARX_gavino_piras`
- Current fictional identity: `ARX_gavino_piras`
- Current sprite key: `GFX_portrait_ARX_independence_wave_gavino_piras`
- Existing runtime path (do not overwrite in this handoff):
  `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_gavino_piras.dds`
- Research candidate: Taddeo Orlando
- Immutable source masters:
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/source_masters/sardinia/arx_taddeo_orlando_generals_original.jpg`
  (main low-resolution face source) and
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/source_masters/sardinia/arx_taddeo_orlando_1942_slovenia_original.jpg`
  (later field-photo comparison only).
- Mechanical previews:
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/crop_previews/sardinia/arx_taddeo_orlando_generals_preview.png`
  and
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/crop_previews/sardinia/arx_taddeo_orlando_1942_slovenia_preview.png`
- Suggested eventual sprite definition after approval and approved native
  portrait processing (do not paste into a `.gfx` file yet):

  ```
  spriteType = {
      name = "GFX_portrait_ARX_independence_wave_taddeo_orlando"
      texturefile = "gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_taddeo_orlando.dds"
  }
  ```

## Processing gate before runtime wiring

1. Parent confirms that the real person is acceptable for the ARX branch and
   that no active current/vanilla identity conflict is introduced.
2. Rights reviewer resolves Commons `PD-Italy` US publication/URAA evidence for
   Eugenio and the Generals.dk-derived Taddeo image, or rejects the candidate.
3. Asset worker runs the repository-native grounded portrait pipeline from the
   immutable master; the mechanical previews in this package are not final
   style output.
4. The worker records the final processed PNG, final DDS, dimensions, converter
   command, and hashes in a follow-up manifest. Only then may the main agent
   edit the existing ARX `.gfx` file and character consumer.

No fallback, generic face, generated real-person likeness, or borrowed vanilla
portrait is authorized by this handoff.
