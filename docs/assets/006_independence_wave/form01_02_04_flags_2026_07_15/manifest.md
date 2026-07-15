# Event 006 FORM-01, FORM-02, and FORM-04 flag manifest

## Package boundary

- Event: `006_independence_wave`
- Families: `FORM-01`, `FORM-02`, and `FORM-04`
- Asset type: three alternate-history generated base flags
- Source mode: official built-in `$imagegen` for every design
- Accepted design authority:
  `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form01_04_identity_research_2026_07_15.md`
- Tag-audit authority:
  `docs/plans/006_independence_wave_plans/tag_audit/006_formable_identity_tag_collision_audit_2026_07_15.md`
- Status: `handed_off`

The accepted 2026-07-15 installed-mod and internal-registry audit records
`KCX`, `NUX`, and `RLX` as collision-clean candidates. This package does not register those tags, change
country identities, or wire gameplay. It installs only the requested runtime
flag triplets and records the asset handoff.

## Source and processing rules

Every source master is a retained official ImageGen output generated with the
canonical skill-local vanilla flag references. The references were used only
for flat orthographic treatment, proportion, and small-size readability. The
final designs do not copy the Armenian, Icelandic, or Israeli symbols.

`notes/process_flags.py` performs the technical finishing pass. It crops the
generated fields to the accepted 41:26 geometry, maps ImageGen's slight tonal
variation to the exact researched solid colours while preserving the generated
silhouettes, resizes the generated design, writes bottom-left 32-bit TGAs,
installs runtime copies, builds contact sheets, and records validation. It does
not draw new flag geometry, trace a vector replacement, or substitute locally
constructed rectangles, crosses, flowers, or river lines for ImageGen output.

## Asset inventory

### KCX - Celtic Congress

- Family: `FORM-01`
- Classification: alternate-history base flag; one shared design for all routes
- Design: forest-green 1:2:1 outer panels around an ivory center, with the
  generated three-bell heather-purple cluster and dark-green stem
- Prompt: `prompts/KCX_flag_imagegen_prompt.txt`
- Source: `source_png/KCX_celtic_congress_heather_imagegen_raw.png`
- Source evidence: `metadata/generation_evidence.json`
- Processed master: `processed_png/KCX_flat_master_820x520.png`
- Review PNGs:
  `processed_png/KCX_normal_82x52.png`,
  `processed_png/KCX_medium_41x26.png`, and
  `processed_png/KCX_small_10x7.png`
- Package TGAs:
  `final_tga/KCX_normal_82x52.tga`,
  `final_tga/KCX_medium_41x26.tga`, and
  `final_tga/KCX_small_10x7.tga`
- Runtime TGAs:
  `gfx/flags/KCX.tga`, `gfx/flags/medium/KCX.tga`, and
  `gfx/flags/small/KCX.tga`
- Palette: `#22543D`, `#F1E8CF`, `#70456C`
- Status: `handed_off`

No prewar common Celtic Congress flag was found by the accepted research. The
heather device is an explicit alternate-history use of the documented 1901
Congress flower, not a historical-flag claim.

### NUX - North Atlantic Union

- Family: `FORM-02`
- Classification: alternate-history base flag; one shared design for all routes
- Design: Atlantic-navy field, broad generated white saltire, and a generated
  offset red Nordic cross layered above it
- Prompt: `prompts/NUX_flag_imagegen_prompt.txt`
- Source: `source_png/NUX_north_atlantic_union_saltire_cross_imagegen_raw.png`
- Source evidence: `metadata/generation_evidence.json`
- Processed master: `processed_png/NUX_flat_master_820x520.png`
- Review PNGs:
  `processed_png/NUX_normal_82x52.png`,
  `processed_png/NUX_medium_41x26.png`, and
  `processed_png/NUX_small_10x7.png`
- Package TGAs:
  `final_tga/NUX_normal_82x52.tga`,
  `final_tga/NUX_medium_41x26.tga`, and
  `final_tga/NUX_small_10x7.tga`
- Runtime TGAs:
  `gfx/flags/NUX.tga`, `gfx/flags/medium/NUX.tga`, and
  `gfx/flags/small/NUX.tga`
- Palette: `#102E4A`, `#FFFFFF`, `#B72F3B`
- Status: `handed_off`

No common flag existed for the accepted Event 006 membership. The saltire and
Nordic-cross synthesis is alternate history and does not claim to reproduce a
member flag.

### RLX - Rhenish League

- Family: `FORM-04`
- Classification: historically grounded alternate-history base flag; one
  shared design for all routes
- Design: generated equal green, warm-white, and red vertical fields with the
  generated continuous cobalt-blue Rhine device in the center field
- Prompt: `prompts/RLX_flag_imagegen_prompt.txt`
- Source: `source_png/RLX_rhenish_league_river_tricolor_imagegen_raw.png`
- Source evidence: `metadata/generation_evidence.json`
- Processed master: `processed_png/RLX_flat_master_820x520.png`
- Review PNGs:
  `processed_png/RLX_normal_82x52.png`,
  `processed_png/RLX_medium_41x26.png`, and
  `processed_png/RLX_small_10x7.png`
- Package TGAs:
  `final_tga/RLX_normal_82x52.tga`,
  `final_tga/RLX_medium_41x26.tga`, and
  `final_tga/RLX_small_10x7.tga`
- Runtime TGAs:
  `gfx/flags/RLX.tga`, `gfx/flags/medium/RLX.tga`, and
  `gfx/flags/small/RLX.tga`
- Palette: `#16834A`, `#F2F0E6`, `#C52D34`, `#245B86`
- Status: `handed_off`

The accepted research grounds the green-white-red colours in the 1923
separatist flag but rejects its horizontal arrangement, which vanilla already
uses for `RHI_democratic`. The vertical fields and Rhine line are explicitly
alternate history.

## Contact sheets and validation

- ImageGen source sheet: `contact_sheets/source_masters_contact_sheet.png`
- Source-to-final sheet: `contact_sheets/source_vs_final_contact_sheet.png`
- Exact 1:1 native comparison:
  `contact_sheets/final_size_ladder_native_contact_sheet.png`
- Enlarged nearest-neighbour comparison:
  `contact_sheets/final_size_ladder_enlarged_nearest_contact_sheet.png`
- Machine-readable dimensions, palette, semantic, TGA-header, and runtime-copy
  checks: `metadata/flag_validation.json`
- Hashes: `metadata/checksums.sha256`

Native and enlarged review accepted all three ladders. At 10x7, KCX retains
three purple flower heads and a green stem, NUX retains a continuous red cross
over a white saltire in every quadrant, and RLX retains the green-white-red
order with a continuous blue river device. The nine TGAs have exact dimensions,
bottom-left origin, 32-bit RGBA encoding, and byte-identical package/runtime
copies.

## Variants, omissions, and blockers

No ideology or route variant is supported, so none was created. No gameplay,
localisation, `.gfx`, GUI, country registration, or identity adapter was
changed. There is no asset-production blocker; later tag registration and
gameplay wiring remain intentionally outside this package's authority.
