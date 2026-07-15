# FORM-03 LCX Flag Asset Manifest

## Identity and source

- Event and family: Event 006, `FORM-03`
- Public identity: Confederation of the Low Countries
- Cosmetic identity: `LCX`
- Asset type: alternate-history generated flat flag
- Source mode: `$imagegen`
- Source PNG: `source_png/LCX_low_countries_river_fork_imagegen_raw.png`
- Regeneration prompt: `prompts/LCX_flag_imagegen_prompt.txt`
- Accepted design authority: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form01_04_identity_research_2026_07_15.md`
- Rights status: original generated design for Chaos Redux; no external historical image is embedded

No attested flag exists for this exact confederation. The navy field and the
three-branch white river device are an explicit alternate-history synthesis of
the Rhine, Meuse, and Scheldt delta. They preserve separate member institutions
without assigning the Belgian, Dutch, Frisian, Benelux, United Netherlands, or
Leo Belgicus identity to the whole confederation.

The retained prompt is the canonical regeneration brief recovered from the
accepted identity direction. The accepted `$imagegen` source PNG is present,
but the original service-side request envelope was not retained; this is
recorded rather than silently reconstructed as exact invocation metadata.

## Processing and outputs

`build_lcx_flag.py` performs deterministic technical finishing only: aspect
crop, exact two-colour flattening, size reduction, uncompressed 32-bit
bottom-left TGA writing, contact-sheet generation, hashes, and validation.

| Role | Review or source file | Final game file | Size |
| --- | --- | --- | ---: |
| source | `source_png/LCX_low_countries_river_fork_imagegen_raw.png` | not wired | 1575x998 |
| flat master | `processed_png/LCX_low_countries_river_fork_flat_master.png` | not wired | 820x520 |
| normal flag | `processed_png/LCX_normal_82x52.png` | `gfx/flags/LCX.tga` | 82x52 |
| medium flag | `processed_png/LCX_medium_41x26.png` | `gfx/flags/medium/LCX.tga` | 41x26 |
| small flag | `processed_png/LCX_small_10x7.png` | `gfx/flags/small/LCX.tga` | 10x7 |

- Contact sheet: `contact_sheets/LCX_flag_source_flat_and_size_ladder.png`
- Machine-readable validation: `metadata/LCX_flag_validation.json`
- Checksums: `metadata/checksums.sha256`
- Palette: `#163A5F` and `#FFFFFF`
- TGA convention: uncompressed 32-bit, bottom-left origin, 8 alpha bits
- Cosmetic map and UI color: `rgb { 22 58 95 }`, the exact accepted
  `#163A5F` field color rather than an inferred carrier color

The accepted identity research rejects ideology- or route-specific variants.
One shared `LCX` cosmetic flag is therefore deliberate. The two eligible
carrier packages, `AFX` and `AGX`, have no ideology-suffixed base flag files in
the repository, so the cosmetic base ladder is the active implementation.

## Wiring

- `set_cosmetic_tag = LCX` is owned by
  `independence_wave_formable_identity_adapter_3` in
  `common/scripted_effects/006_independence_wave_form03_effects.txt`.
- Country-name, definite-name, and adjective localisation for the base and all
  four ideology groups is in
  `localisation/english/006_independence_wave_formable_registry_l_english.yml`.
- The cosmetic map and UI color is registered as the exact accepted navy field
  in `common/countries/006_independence_wave_formable_cosmetics.txt`.
- Country flags require no `.gfx` sprite registration.

## Review result

The source, flat master, full size ladder, contact sheet, validation metadata,
and wired TGA files are present. The contact sheet preserves the three branches
at every required size, and the final assets use the intended flat two-colour
geometry without fabric, lighting, text, or borrowed member symbols.
