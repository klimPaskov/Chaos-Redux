# Event 006 portrait visual-repair audit

Date: 2026-09-06.

Owner: `chaosx_portrait_creator`.

Disposition: `blocked / no safe repair`.

## Scope and authority

This audit covered every Event 006 portrait runtime DDS, Event 006 portrait-specific GFX definition, current character or scripted-effect consumer, durable portrait source shelf, current processed evidence, the user-supplied DDS gate, and the superseded generated portrait package.

The required Chaos Redux instructions, `chaos-redux-comfyui`, `chaos-redux-event-assets`, offline portrait and graphical-asset wiki pages, relevant vanilla portrait references, and the current Event 006 portrait handoffs were read before inspection.

The accepted source-of-truth remains the current Event 006 portrait consumer gate in `006_event6_portrait_consumer_gate_2026-08-31.md` and the unresolved-source gate in `006_event6_portrait_gate_research_2026-09-05.md`.

No source, processed PNG, runtime DDS, GFX, character, gameplay, or unrelated UI file was changed by this audit.

## Runtime, GFX, and consumer inventory

- `gfx/leaders/006_independence_wave/` contains 70 DDS files.
- The three Event 006 portrait GFX files contain 64 unique portrait name-to-texture pairs: 53 in `interface/006_independence_wave_portraits_registry.gfx`, 9 in `interface/006_independence_wave_small_assets.gfx`, and 2 in `interface/006_independence_wave.gfx`.
- All 64 local GFX names are unique, all 64 texture paths are unique, and every registered texture path resolves to an existing runtime DDS.
- `common/characters/006_independence_wave_characters_registry.txt` contains 72 `large` portrait references covering 46 unique local Event 006 portrait keys.
- The other 18 local Event 006 portrait keys are consumed by the existing package scripted effects for BRI, BSK, GLC, MNT, RHI, RUT, SCO, WLS, YAK, and BAY.
- No current Event 006 portrait GFX definition is unused.
- The two apparent missing portrait references, `GFX_portrait_RHI_josef_matthes` and `GFX_portrait_BAY_rupprecht_of_bavaria`, are intentional vanilla cleanup aliases, not missing Event 006 definitions, as documented in the 2026-07-16 audit and confirmed against vanilla character and portrait files.

The six runtime DDS files below are unregistered orphans and have no current Event 006 GFX or character consumer:

| Runtime orphan | Current SHA-256 | Disposition |
|---|---|---|
| `portrait_ACX_cornish_coastal_commander.dds` | `b6b84c64e16c6112ff117300b6271a3e50e239acc663cf5fc7c7641673ed50e6` | Preserve as legacy evidence; exact ACX commander identity and consumer remain blocked. |
| `portrait_ACX_cornish_port_and_mines_committee.dds` | `2b3b98f4621bc43f0f517a28f984337755bf193746d0dadcedff4ebf2cd9a0b8` | Preserve as source-placeholder evidence; ACX role adaptation and package admission remain blocked. |
| `portrait_AEX_flemish_civil_industrial_board.dds` | `918efe9de7804567ec9dd130ad855d81ed32171cf7a0e4e4a6cf27cf19283153` | Preserve as superseded generated evidence; no admitted AEX consumer. |
| `portrait_AEX_flemish_industrial_security_commander.dds` | `8fe59ea0b1b7c7d5b2f556a016aabf0c52a00f8260d3af8840e93c7ac90564ee` | Preserve as superseded generated evidence; no admitted AEX consumer. |
| `portrait_ARX_independence_wave_gavino_piras.dds` | `f8eab9bfe2551ba68166bbf698e486f1dac1452f1509801a59db5ca8ad20a4b7` | Preserve as legacy shelf evidence; exact Gavino Piras identity is blocked. |
| `portrait_ARX_independence_wave_vittorio_pala.dds` | `443e92aca9f57fce6988296692949f70a859508ff85f85b30a61897243214fae` | Preserve as legacy shelf evidence; exact Vittorio Pala identity is blocked. |

The two ARX orphan files are not safe candidates for the current Verne, Mella, or Lussu consumers, and the four ACX/AEX orphan files are part of the superseded generated package or its source-placeholder history.

## DDS and pixel audit

Every current runtime DDS was decoded and checked independently with Pillow and a direct DDS-header read.

- Runtime count: 70.
- Every file is exactly 131,168 bytes and decodes to `156x210` RGBA.
- Every file has alpha extrema `255..255`, so no runtime file has a transparent edge, alpha fringe, or accidental premultiplied bleed.
- Every file has the expected legacy uncompressed header: `dwSize=124`, `dwFlags=4111`, `height=210`, `width=156`, `pitch=624`, pixel-format size `32`, pixel-format flags `65`, `fourCC=0`, `RGBBitCount=32`, masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, caps `4096`, and no mipmaps.
- The 20 DDS files in the superseded generated package were checked separately and have the same valid technical contract, so their failure is semantic/source-mode failure rather than a crop, size, alpha, or conversion defect.
- Native `156x210` contact sheets and nearest-neighbour `4x` enlarged contact sheets were reviewed for all 70 runtime files in the temporary audit shelf at `C:\Users\klimp\AppData\Local\Temp\chaosx_event6_portrait_audit\`.
- The visual review found no clipped head, accidental border, malformed crop, alpha seam, or path-induced wrong texture among the admitted consumers.
- The grainy or low-resolution appearance of a few admitted archival portraits, including KOS Shaban Polluzha, is source-authentic and already accepted by the relevant handoff; repainting it would violate source preservation.

The protected approved runtime files remain unchanged:

| Runtime | SHA-256 |
|---|---|
| `portrait_BAY_rupprecht_of_bavaria.dds` | `fb7bce1d8316f52d728e82e299eaf9675fa0dabe57f2f7c9aff154c1012478b7` |
| `portrait_RHI_josef_friedrich_matthes.dds` | `fb43deb0b8708e7f5d1000b1f67ab63aca43d54efcb75618fb9097112a7699aa` |

## Archive and processed evidence

The durable archive remains flat and compliant at `docs/assets/portraits/006_independence_wave/`.

- The archive parent contains exactly 59 preserved source masters plus `README.md`.
- Its only child is `processed/`.
- `processed/` contains 72 evidence files and no child directory.
- The archive parent contains no runtime DDS or 156x210 processed output.
- The processed shelf contains source crops, nearest-neighbour review images, metadata, provenance, manifests, and captured source pages; its 23 PNG files were dimension-checked and visually reviewed in temporary contact sheets.
- Source-master contact sheets for all 59 preserved source files were reviewed, including the unresolved rows and the protected sources.
- No source master, crop, metadata, or evidence file was altered.

The 38 existing exact source-to-runtime consumers remain the byte-matched rows recorded in `006_event6_portrait_consumer_gate_2026-08-31.md`; that handoff records every source/runtime SHA-256 and the current character or effect consumer. The 13 additional selected candidates remain unmapped and fail closed.

The unresolved rows are Anatoly Pepelyayev, Ardan Markizov, Mikhei Erbanov, Grigory Gurkin, Samuil Yufit, Alexander Krasnoshchyokov, Pyotr Nikiforov, Seyid Riza, the ACX port/mines committee candidate, Gioacchino Solinas, Ratu Sir Lala Sukuna, Vishnu Deo, and Alexandre Bóveda.

No unresolved row has a closed exact identity, role/date, rights, and consumer gate, so none was copied, renamed, relabelled, wired, or converted.

## Superseded generated package

The retained package `docs/assets/006_independence_wave/portrait_refresh_male_hoi4_2026_07_18/` records `OpenAI built-in ImageGen`, `text_to_image`, prompt records, prompt hashes, generation handles, raw source hashes, processed PNGs, review sheets, and 20 technically valid DDS outputs.

The package manifest explicitly marks this source mode as superseded because it depicts grounded Event 006 polities with generated faces, which is disallowed by the accepted sourced-real-portrait rule.

The 16 currently wired generated runtime portraits are:

`AFX_walloon_provisional_assembly`, `AFX_walloon_reserve_commander`, `AGX_friesland_coastal_council`, `AGX_friesland_coastal_commander`, `AJX_saar_municipal_neutral_commission`, `AJX_saar_industrial_security_commissioner`, `BAY_independence_wave_state_council`, `BAY_independence_wave_mountain_commandant`, `BRI_independence_wave_civic_commission`, `BRI_independence_wave_coastal_commandant`, `RHI_independence_wave_provisional_directorate`, `RHI_independence_wave_river_commandant`, `SCO_independence_wave_civic_convention`, `SCO_independence_wave_territorial_commandant`, `WLS_independence_wave_national_council`, and `WLS_independence_wave_mountain_commandant`.

The four generated-package runtime portraits that are currently orphaned are `ACX_cornish_coastal_commander`, `ACX_cornish_port_and_mines_committee`, `AEX_flemish_civil_industrial_board`, and `AEX_flemish_industrial_security_commander`.

These 20 portraits are not repairable within this bounded visual-repair task because their source, identity, rights, and grounded role gates are not closed. A crop tweak, repaint, generic replacement, or silent relabel would make the package less compliant rather than repair it.

## Skipped operations and blockers

- RunPod was not opened, operated, configured, queued, or monitored.
- Native ImageGen was not invoked because no fictional or impossible Event 006 subject was admitted for new portrait creation.
- `convert_to_dds.py` was not rerun because no new source-cleared candidate reached the conversion gate and all current runtime files already satisfy the exact DDS contract.
- No `.gfx`, character, scripted-effect, gameplay, localisation, flag, event, or unrelated UI file was edited.
- No orphan DDS was deleted because the current handoffs preserve them as provenance and their removal would be a separate cleanup decision rather than a visual repair.

The concrete blocker is source-mode and identity admission, not a technical portrait defect: the 16 wired generated grounded-polity portraits require sourced real replacements or explicit package withdrawal, the four matching generated orphans remain unadmitted, and the two ARX identity orphans remain blocked by exact-name evidence. The 13 current source candidates remain blocked by their documented consumer, role/date, rights, or identity gates.

## Files changed

Only this handoff was added:

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_portrait_visual_repair_audit_2026-09-06.md`

