# Stage 7 Biological Countermeasure Icon Manifest

This package contains twelve original static gameplay icons for the Chaos Redux Stage 7 ordinary biological countermeasure system.

Source mode is the official built-in ImageGen workflow, with one separately generated 1254x1254 source master for every icon.

The canonical reference families inspected before generation were `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions/` and `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas/`, including both family contact sheets and representative individual references.

Reference PNGs were used only for style and surface review and were not copied, resized, recolored, traced, or shipped as final art.

Every generated source master used a flat `#00ff00` chroma-key background, no text, no flags, no national emblems, no protected real-world symbols or logos, no watermark, and no opaque square backdrop.

The selected surveillance-network decision source replaced an earlier rejected generation that contained an unwanted generic medical cross; the rejected candidate is not part of this package.

Transparent processing used the official `remove_chroma_key.py` helper with `--auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`.

Exact-size PNG previews were produced from the transparent intermediate with FFmpeg Lanczos scaling, and DDS files were produced only from those exact-size PNG previews with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

## Requirement-to-runtime crosswalk

| # | Asset type | Sprite name | Concept | Source master | Processed PNG | Final DDS | Runtime size | Status |
|---:|---|---|---|---|---|---|---:|---|
| 1 | Decision | `GFX_decision_bio_activate_surveillance_network` | Epidemiological signal map, instrument needle, and reporting network. | `sources/decisions/decision_bio_activate_surveillance_network_source.png` | `processed_png/decisions/decision_bio_activate_surveillance_network_32x32.png` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_activate_surveillance_network.dds` | 32x32 | complete |
| 2 | Decision | `GFX_decision_bio_quarantine_state` | Sealed cordon, plain warning seal, and civilian hardship undertone. | `sources/decisions/decision_bio_quarantine_state_source.png` | `processed_png/decisions/decision_bio_quarantine_state_32x32.png` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_quarantine_state.dds` | 32x32 | complete |
| 3 | Decision | `GFX_decision_bio_border_control` | Closed transport gate, disinfected rail and road corridor. | `sources/decisions/decision_bio_border_control_source.png` | `processed_png/decisions/decision_bio_border_control_32x32.png` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_border_control.dds` | 32x32 | complete |
| 4 | Decision | `GFX_decision_bio_anthrax_antibiotics` | Sealed antibiotic ampoules with a dark clustered spore silhouette. | `sources/decisions/decision_bio_anthrax_antibiotics_source.png` | `processed_png/decisions/decision_bio_anthrax_antibiotics_32x32.png` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_anthrax_antibiotics.dds` | 32x32 | complete |
| 5 | Decision | `GFX_decision_bio_plague_antibiotics` | Treatment ampoules with a segmented flea/vector silhouette. | `sources/decisions/decision_bio_plague_antibiotics_source.png` | `processed_png/decisions/decision_bio_plague_antibiotics_32x32.png` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_plague_antibiotics.dds` | 32x32 | complete |
| 6 | Decision | `GFX_decision_bio_tularemia_antibiotics` | Treatment ampoules with a rural field and tick/vector silhouette. | `sources/decisions/decision_bio_tularemia_antibiotics_source.png` | `processed_png/decisions/decision_bio_tularemia_antibiotics_32x32.png` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_tularemia_antibiotics.dds` | 32x32 | complete |
| 7 | Decision | `GFX_decision_bio_international_medical_mission` | Plain medical convoy, open inspection clipboard, and no organization logo. | `sources/decisions/decision_bio_international_medical_mission_source.png` | `processed_png/decisions/decision_bio_international_medical_mission_32x32.png` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_international_medical_mission.dds` | 32x32 | complete |
| 8 | Decision | `GFX_decision_bio_sustain_containment` | Layered cordon, hospital, and declining outbreak curve. | `sources/decisions/decision_bio_sustain_containment_source.png` | `processed_png/decisions/decision_bio_sustain_containment_32x32.png` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_sustain_containment.dds` | 32x32 | complete |
| 9 | Decision | `GFX_decision_bio_expand_medical_capacity` | Protected field-hospital reserve, medical satchel, and truck silhouette. | `sources/decisions/decision_bio_expand_medical_capacity_source.png` | `processed_png/decisions/decision_bio_expand_medical_capacity_32x32.png` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_expand_medical_capacity.dds` | 32x32 | complete |
| 10 | Decision | `GFX_decision_bio_expand_biosecurity_capacity` | Sealed sample cabinet, microscope, and blank security shield. | `sources/decisions/decision_bio_expand_biosecurity_capacity_source.png` | `processed_png/decisions/decision_bio_expand_biosecurity_capacity_32x32.png` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_expand_biosecurity_capacity.dds` | 32x32 | complete |
| 11 | Idea | `GFX_idea_bio_surveillance_network` | National reporting and instrument network in a compact emblem composition. | `sources/ideas/idea_bio_surveillance_network_source.png` | `processed_png/ideas/idea_bio_surveillance_network_64x64.png` | `gfx/interface/ideas/biowarfare/countermeasures/idea_bio_surveillance_network.dds` | 64x64 | complete |
| 12 | Idea | `GFX_idea_smallpox_vaccination` | National vaccination reserve and immunisation program in a compact emblem composition. | `sources/ideas/idea_smallpox_vaccination_source.png` | `processed_png/ideas/idea_smallpox_vaccination_64x64.png` | `gfx/interface/ideas/biowarfare/countermeasures/idea_smallpox_vaccination.dds` | 64x64 | complete |

## Wiring table

The sprite names and DDS paths above are stable and registered in `interface/biological_countermeasures.gfx`.

The ten decision sprites are wired to the matching biological response decisions.

The two idea sprites are wired to `bio_surveillance_network_idea` and `smallpox_vaccination_program_idea`.

No existing icon or military-raid asset was removed, renamed, resized into another asset type, or overwritten.

## Source provenance records

| Asset | ImageGen source output id | Repo-retained source |
|---|---|---|
| `decision_bio_activate_surveillance_network` | `exec-42bdcb08-ac97-44ba-8a25-d2657446bf60.png` | `sources/decisions/decision_bio_activate_surveillance_network_source.png` |
| `decision_bio_quarantine_state` | `exec-30fe94f2-c146-48c5-8e16-6a6a2c7b749a.png` | `sources/decisions/decision_bio_quarantine_state_source.png` |
| `decision_bio_border_control` | `exec-554078db-f7a4-4812-a2ea-18ea51269d1a.png` | `sources/decisions/decision_bio_border_control_source.png` |
| `decision_bio_anthrax_antibiotics` | `exec-d6a569f0-a8c4-4743-9496-4a635250d3e0.png` | `sources/decisions/decision_bio_anthrax_antibiotics_source.png` |
| `decision_bio_plague_antibiotics` | `exec-30ed1d13-bce9-4b81-a364-ef9eae8324ac.png` | `sources/decisions/decision_bio_plague_antibiotics_source.png` |
| `decision_bio_tularemia_antibiotics` | `exec-65b94fab-f3de-4996-92e6-1f7def845352.png` | `sources/decisions/decision_bio_tularemia_antibiotics_source.png` |
| `decision_bio_international_medical_mission` | `exec-442c0632-8bcb-4c53-ba52-925a2d152b48.png` | `sources/decisions/decision_bio_international_medical_mission_source.png` |
| `decision_bio_sustain_containment` | `exec-52a0bb6d-41dd-44c2-ba47-1b15a6b9f69f.png` | `sources/decisions/decision_bio_sustain_containment_source.png` |
| `decision_bio_expand_medical_capacity` | `exec-e94ce997-6351-430d-9b3f-3eaf9459a6b5.png` | `sources/decisions/decision_bio_expand_medical_capacity_source.png` |
| `decision_bio_expand_biosecurity_capacity` | `exec-b4f1ca39-c941-487f-8299-badc643f57e3.png` | `sources/decisions/decision_bio_expand_biosecurity_capacity_source.png` |
| `idea_bio_surveillance_network` | `exec-27be673c-d931-4f87-8a04-f6bba2122c7a.png` | `sources/ideas/idea_bio_surveillance_network_source.png` |
| `idea_smallpox_vaccination` | `exec-89de1ae5-1e4e-4a77-b77e-d6af7dc995db.png` | `sources/ideas/idea_smallpox_vaccination_source.png` |

The original generated images remain in the official ImageGen output directory for this run, and the repository-retained source masters are the durable package evidence.

## SHA-256 checksums

The source, processed PNG, and final DDS hashes are recorded in `alpha_verification.md` beside the complete DDS header and alpha audit.
