# Stage 7 Biological Stockpile-Risk Idea and Decision Icon Manifest

## Package

- System: `chaos_warfare_system`
- Stage: `7_biological_warfare`
- Package: `stockpile_risk_ideas`
- Source mode: built-in `$imagegen` for every asset
- Asset family: four independent idea / national-spirit stockpile-risk bands plus one independent 32x32 decision icon
- Parent-provided final DDS paths are preserved exactly.
- DDS format: requested 32-bit unsigned BGRB 8.8.8.8; emitted and validated through the repository converter as legacy uncompressed BGRA / B8G8R8A8 with exact channel masks.
- All assets are `handed_off`: production, processing, conversion, validation, and documentation are complete; parent `.gfx` registration remains outside this subagent's write scope.

## Asset entries

### Controlled stockpile risk

- Asset name: Controlled biological stockpile risk
- Related gameplay requirement: Stage 7 biological stockpile-risk band `controlled`
- Asset type: idea / national spirit icon
- Intended use: national biological stockpile risk display
- Source mode: `$imagegen`
- Prompt/source notes: `prompts/source_prompts.md#controlled`
- Source PNG: `source_png/idea_bio_stockpile_risk_controlled.source.png`
- Processed PNG: `processed_png/idea_bio_stockpile_risk_controlled.png`
- Final DDS: `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_controlled.dds`
- Target size: `60x68` (explicit project/canonical idea canvas)
- Sprite name: `GFX_idea_bio_stockpile_risk_controlled`
- Intended `.gfx` file: proposed parent-selected idea sprite registration surface; not edited here
- Related idea id: parent-provided stockpile-risk controlled band; exact gameplay id not included in the handoff prompt
- Status: `handed_off`
- Notes: intact sealed cylinder behind intact containment shield; distinguishable through calm, orderly structure.

### Strained stockpile risk

- Asset name: Strained biological stockpile risk
- Related gameplay requirement: Stage 7 biological stockpile-risk band `strained`
- Asset type: idea / national spirit icon
- Intended use: national biological stockpile risk display
- Source mode: `$imagegen`
- Prompt/source notes: `prompts/source_prompts.md#strained`
- Source PNG: `source_png/idea_bio_stockpile_risk_strained.source.png`
- Processed PNG: `processed_png/idea_bio_stockpile_risk_strained.png`
- Final DDS: `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_strained.dds`
- Target size: `60x68` (explicit project/canonical idea canvas)
- Sprite name: `GFX_idea_bio_stockpile_risk_strained`
- Intended `.gfx` file: proposed parent-selected idea sprite registration surface; not edited here
- Related idea id: parent-provided stockpile-risk strained band; exact gameplay id not included in the handoff prompt
- Status: `handed_off`
- Notes: crowded rack, taut clamps, and one amber lamp provide structural escalation independent of color.

### Dangerous stockpile risk

- Asset name: Dangerous biological stockpile risk
- Related gameplay requirement: Stage 7 biological stockpile-risk band `dangerous`
- Asset type: idea / national spirit icon
- Intended use: national biological stockpile risk display
- Source mode: `$imagegen`
- Prompt/source notes: `prompts/source_prompts.md#dangerous`
- Source PNG: `source_png/idea_bio_stockpile_risk_dangerous.source.png`
- Processed PNG: `processed_png/idea_bio_stockpile_risk_dangerous.png`
- Final DDS: `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_dangerous.dds`
- Target size: `60x68` (explicit project/canonical idea canvas)
- Sprite name: `GFX_idea_bio_stockpile_risk_dangerous`
- Intended `.gfx` file: proposed parent-selected idea sprite registration surface; not edited here
- Related idea id: parent-provided stockpile-risk dangerous band; exact gameplay id not included in the handoff prompt
- Status: `handed_off`
- Notes: cracked outer housing, intact inner canister, diagonal brace, and warning lamp; no leak depiction.

### Critical stockpile risk

- Asset name: Critical biological stockpile risk
- Related gameplay requirement: Stage 7 biological stockpile-risk band `critical`
- Asset type: idea / national spirit icon
- Intended use: national biological stockpile risk display
- Source mode: `$imagegen`
- Prompt/source notes: `prompts/source_prompts.md#critical`
- Source PNG: `source_png/idea_bio_stockpile_risk_critical.source.png`
- Processed PNG: `processed_png/idea_bio_stockpile_risk_critical.png`
- Final DDS: `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_critical.dds`
- Target size: `60x68` (explicit project/canonical idea canvas)
- Sprite name: `GFX_idea_bio_stockpile_risk_critical`
- Intended `.gfx` file: proposed parent-selected idea sprite registration surface; not edited here
- Related idea id: parent-provided stockpile-risk critical band; exact gameplay id not included in the handoff prompt
- Status: `handed_off`
- Notes: warped blast door and failed restraint rack with dark red emergency geometry; storage remains closed and opaque.

### National biological arsenal designation and relocation

- Asset name: Exact national biological arsenal designation and relocation
- Related gameplay id: `bio_designate_national_biological_arsenal`
- Asset type: decision icon
- Intended use: exact national biological arsenal designation and relocation decision
- Source mode: `$imagegen`
- Prompt/source notes: `prompts/source_prompts.md#decision-icon`
- Source PNG: `source_png/decision_bio_designate_national_biological_arsenal.source.png`
- Processed PNG: `processed_png/decision_bio_designate_national_biological_arsenal.png`
- Final DDS: `gfx/interface/decisions/biowarfare/bio_designate_national_biological_arsenal.dds`
- Target size: `32x32` (decision-icon pipeline)
- Sprite name: `GFX_decision_bio_designate_national_biological_arsenal`
- Intended `.gfx` file: proposed parent-selected biological-warfare decision sprite registration surface; not edited here
- Related localisation key: parent-owned decision localisation; not provided to this asset subagent
- Status: `handed_off`
- Notes: independently generated locked vault, canister rack, and precise locator silhouette; not resized from the idea family.

## Asset-side requirement-to-runtime crosswalk

| Requirement | Source package | Final asset | Intended runtime registration | Live consumer | Status |
| --- | --- | --- | --- | --- | --- |
| Controlled stockpile-risk band | this manifest / Controlled entry | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_controlled.dds` | `GFX_idea_bio_stockpile_risk_controlled` | parent idea/national-spirit definition; id not supplied | handed_off |
| Strained stockpile-risk band | this manifest / Strained entry | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_strained.dds` | `GFX_idea_bio_stockpile_risk_strained` | parent idea/national-spirit definition; id not supplied | handed_off |
| Dangerous stockpile-risk band | this manifest / Dangerous entry | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_dangerous.dds` | `GFX_idea_bio_stockpile_risk_dangerous` | parent idea/national-spirit definition; id not supplied | handed_off |
| Critical stockpile-risk band | this manifest / Critical entry | `gfx/interface/ideas/cbrn/idea_bio_stockpile_risk_critical.dds` | `GFX_idea_bio_stockpile_risk_critical` | parent idea/national-spirit definition; id not supplied | handed_off |
| Exact national arsenal designation and relocation | this manifest / Decision entry | `gfx/interface/decisions/biowarfare/bio_designate_national_biological_arsenal.dds` | `GFX_decision_bio_designate_national_biological_arsenal` | `bio_designate_national_biological_arsenal` | handed_off |

Parent wiring, localisation, gameplay ids for the four idea bands, and the owning `.gfx` files are intentionally unresolved here because the user granted no write scope for those files.

## Validation records

- Visual review: `validation/visual_validation.md`
- Alpha metrics: `validation/alpha_metrics.json`
- DDS header, dimension, alpha, and decoded-RGBA equality: `validation/dds_validation.json`
- SHA-256 source/processed/DDS hashes: `validation/hashes.sha256`
- Contact sheet: `contact_sheets/bio_stockpile_risk_icons_contact_sheet.png`
