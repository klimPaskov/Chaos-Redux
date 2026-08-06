# Biological Stockpile-Risk Idea and Decision Icon Handoff

Date: 2026-07-19

## Runtime retirement notice

The four national-spirit stockpile-risk markers in this historical handoff are
retired. They were removed from runtime because they exposed private monitoring
state as persistent country ideas and unnecessarily occupied the national-spirit
view. Their idea definitions, runtime DDS files, GFX registrations, and refresh
calls are no longer active. The underlying risk-band variables, accident
weighting, and exact-arsenal monitoring remain active. The national-arsenal
decision icon remains in use.

## Historical scope

Produced a bounded five-asset package for Stage 7 biological warfare. Only the
decision asset remains active:

- Four independent 60x68 idea / national-spirit icons for `controlled`, `strained`, `dangerous`, and `critical` stockpile-risk bands (retired).
- One independent 32x32 decision icon for exact national biological arsenal designation and relocation (active).

All art was generated with built-in `$imagegen`. The four idea icons were designed as a coordinated family but generated separately; the decision icon was generated from a separate decision-specific brief and was not resized from the idea family.

## Historical DDS files and former parent sprite names

| Asset | Final DDS | Sprite | Target | Related id |
| --- | --- | --- | ---: | --- |
| Controlled | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_controlled.dds` | `GFX_idea_bio_stockpile_risk_controlled` | 60x68 | parent controlled stockpile-risk idea band; exact id not supplied |
| Strained | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_strained.dds` | `GFX_idea_bio_stockpile_risk_strained` | 60x68 | parent strained stockpile-risk idea band; exact id not supplied |
| Dangerous | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_dangerous.dds` | `GFX_idea_bio_stockpile_risk_dangerous` | 60x68 | parent dangerous stockpile-risk idea band; exact id not supplied |
| Critical | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_critical.dds` | `GFX_idea_bio_stockpile_risk_critical` | 60x68 | parent critical stockpile-risk idea band; exact id not supplied |
| National arsenal designation / relocation | `gfx/interface/decisions/biowarfare/bio_designate_national_biological_arsenal.dds` | `GFX_decision_bio_designate_national_biological_arsenal` | 32x32 | `bio_designate_national_biological_arsenal` |

## Suggested parent GFX wiring

The following snippets are ready for the parent to adapt to the existing GFX registration format. The owning `.gfx` file was not provided and was not edited. The target file choices below are therefore proposed and must be confirmed against the parent's existing registration surfaces.

Proposed idea sprite registration in the existing idea sprite file (proposed target: `interface/ideas.gfx`):

```text
spriteType = {
	name = "GFX_idea_bio_stockpile_risk_controlled"
	texturefile = "gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_controlled.dds"
}
spriteType = {
	name = "GFX_idea_bio_stockpile_risk_strained"
	texturefile = "gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_strained.dds"
}
spriteType = {
	name = "GFX_idea_bio_stockpile_risk_dangerous"
	texturefile = "gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_dangerous.dds"
}
spriteType = {
	name = "GFX_idea_bio_stockpile_risk_critical"
	texturefile = "gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_critical.dds"
}
```

Proposed decision sprite registration in the existing biological-warfare decision sprite file (proposed target: `interface/biological_warfare.gfx`):

```text
spriteType = {
	name = "GFX_decision_bio_designate_national_biological_arsenal"
	texturefile = "gfx/interface/decisions/biowarfare/bio_designate_national_biological_arsenal.dds"
}
```

## Package evidence

- Manifest: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/stockpile_risk_ideas/manifest.md`
- Prompt/source notes: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/stockpile_risk_ideas/prompts/source_prompts.md`
- Source PNGs: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/stockpile_risk_ideas/source_png/`
- Processed PNGs: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/stockpile_risk_ideas/processed_png/`
- Contact sheet: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/stockpile_risk_ideas/contact_sheets/bio_stockpile_risk_icons_contact_sheet.png`
- Visual validation: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/stockpile_risk_ideas/validation/visual_validation.md`
- DDS validation: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/stockpile_risk_ideas/validation/dds_validation.json`
- Hashes: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/stockpile_risk_ideas/validation/hashes.sha256`

## Validation result

Each DDS has the requested 32-bit unsigned BGRB 8.8.8.8 output contract, emitted and validated as the repository's legacy uncompressed BGRA / B8G8R8A8 layout: header size 124, pixel-format size 32, flags 65, no FourCC, 32 bits per pixel, BGRA masks, texture caps, exact file length, exact target dimensions, alpha range 0..255, and exact decoded RGBA equality with its processed PNG.

Visual inspection found transparent checkerboard corners, no visible chroma fringe, no fake matte, no exposed contents, no gore, no text, and structural escalation that remains readable without color alone.

## Remaining parent actions / uncertainty

- Register the five sprites in the appropriate existing `.gfx` files.
- Bind the four exact idea sprite names to the parent-provided stockpile-risk idea definitions; the four gameplay ids were not included in the asset handoff request.
- Bind `GFX_decision_bio_designate_national_biological_arsenal` to `bio_designate_national_biological_arsenal`.
- No `.gfx`, gameplay, localisation, root Stage 7 manifest, or existing icon was edited by this handoff.
