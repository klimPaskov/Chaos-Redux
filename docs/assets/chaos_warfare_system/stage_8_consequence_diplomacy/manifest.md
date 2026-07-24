# Stage 8 CBRN Consequence Diplomacy Decision Icon Manifest

Package: `chaos_warfare_system/stage_8_consequence_diplomacy`

Generated: 2026-07-24.

Asset type: three independent static Chaos Redux/HOI4 decision icons.

Source mode: official built-in ImageGen with a separate source composition for each decision, local chroma-key removal, exact 32x32 RGBA processing, and `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` conversion.

Reference family inspected before generation: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions/`, including `contact_sheet.png` and representative individual decision references.

Existing Chaos Redux CBRN decision packages and contact sheets were inspected for palette, outlines, transparent corners, and 32x32 readability.

Reference PNGs were used only for style and surface review and were not copied, resized, recolored, traced, or shipped as final art.

## Requirement-to-runtime crosswalk

| Stable decision id | Visual identity | Source PNG | Transparent intermediate | Processed PNG | Final DDS | Sprite recommendation | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `decision_cbrn_demand_inspections` | Sealed CBRN facility/depot door with inspection lamp and clipboard/access papers; the door and lamp make demanded site access readable at 32x32. | `source_png/decision_cbrn_demand_inspections_source.png` | `intermediate_png/decision_cbrn_demand_inspections_transparent.png` | `processed_png/decision_cbrn_demand_inspections_32x32.png` | `gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_demand_inspections.dds` | `GFX_decision_cbrn_demand_inspections` | complete |
| `decision_cbrn_share_forensic_evidence` | Sealed evidence case with tamper seal, amber specimen vial, shell fragment, dossier photographs, and chain-of-custody papers. | `source_png/decision_cbrn_share_forensic_evidence_source.png` | `intermediate_png/decision_cbrn_share_forensic_evidence_transparent.png` | `processed_png/decision_cbrn_share_forensic_evidence_32x32.png` | `gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_share_forensic_evidence.dds` | `GFX_decision_cbrn_share_forensic_evidence` | complete |
| `decision_cbrn_sponsor_decontamination_mission` | Foreign mobile wash rig with coiled hose and spray nozzle, protected worker, and plain relief star on the aid crate; reads as an external mission rather than domestic cleanup. | `source_png/decision_cbrn_sponsor_decontamination_mission_source.png` | `intermediate_png/decision_cbrn_sponsor_decontamination_mission_transparent.png` | `processed_png/decision_cbrn_sponsor_decontamination_mission_32x32.png` | `gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_sponsor_decontamination_mission.dds` | `GFX_decision_cbrn_sponsor_decontamination_mission` | complete |

All three source masters are independent ImageGen compositions and none is a crop, recolor, resize, or cross-type substitute for another asset.

## Package files

The source masters are retained under `source_png/` and the processed exact-size previews are retained under `processed_png/`.

The chroma-key-removed full-resolution evidence is retained under `intermediate_png/`.

Prompt records are in `prompts/decision_cbrn_diplomacy_prompt_records.md`.

The processed review sheet is `contact_sheets/stage_8_consequence_diplomacy_decision_icons.png`.

The decoded final-DDS review sheet is `contact_sheets/stage_8_consequence_diplomacy_final_dds_contact_sheet.png`.

Hashes and automated image/DDS QA are in `validation/asset_hashes_and_qa.json`.

Validation summary is in `validation/validation.md`.

The sprite handoff is in `gfx_handoff.md`.

## SHA-256 records

| Asset | Source PNG | Transparent intermediate | Processed PNG | Final DDS |
| --- | --- | --- | --- | --- |
| `decision_cbrn_demand_inspections` | `7810e73f6047e48960e98521b1672e59365a20a8b82913bb3c52b354b95d4bdc` | `03747d727779ba72df456bd9af3f23c205762c624ce9c19ed44bd4ecb679b869` | `ab2816608609fc9cf7ab734f7522415c358b584d581419eaa84247170a369a55` | `5e7af392da5584c26f3757e3282d2109d5614c8d67df71256afaf5a0318a8ad6` |
| `decision_cbrn_share_forensic_evidence` | `bb20dc0d2f3ac36c15b207e67aaf4a2669b6d271d53d005863ac77ee6839e454` | `df1df44c56247b8eaed9731138eba09e639c8765edc8e7e3656236495b647e58` | `d75159416a83ae14ced66a7316cd1e74bb54e2b0424ccdd84e09479ddab7c3e4` | `e861f593309cd05521c09c3bd189cf4348eddd7041dc3eb62a4b510958730d89` |
| `decision_cbrn_sponsor_decontamination_mission` | `f14661f6c03b47631d132affeadcc4b7fc416a192a54a9366778aeef8faf40c8` | `e9bc7aa066bdf188996264955914ba732f1a9fef34aa293da51ed2f04f605cb6` | `90592cc745ff275e1e80862bdc9ef54eeae0916dc15e7ba449697bbe75d35f42` | `5338227fa25cbf7739e42cea29b369521e6dc1131fd335082400814d85b1a8cd` |

## Scope and wiring note

No `.gfx`, `.gui`, gameplay, decision, localisation, specification, or general documentation file was edited.

The recommended target definition is `interface/cbrn_diplomacy.gfx`, subject to the wiring agent confirming the final existing GFX ownership pattern.

The exact ready-to-copy sprite definitions and stable DDS paths are in `gfx_handoff.md`.
