# Event 014 model source research C

Status: three legally usable Internet-sourced visual references are archived and selected for parent review. Each source has an untouched download, an RGBA PNG preview, a repository-converter DDS evidence copy, a source manifest, and an archived source page where the page was available.

This package covers only `cannibal_march_predation_column`, `cannibal_network_cadre`, and `cannibal_bone_riders`. It does not create or approve final model geometry, does not run ImageGen or Meshy, and does not edit gameplay, runtime, entity, unit, `.gfx`, `.asset`, event, localisation, or existing production manifest files.

The user-provided attachment `C:/Users/klimp/AppData/Local/Temp/codex-clipboard-59672c99-c6a5-4728-9ab5-71e311186bd4.png` was explicitly excluded and was not opened, copied, or used.

## Selected references

| Job | Proposed runtime basename | Source and license | Downloaded dimensions | Original SHA-256 | Fit summary |
| --- | --- | --- | --- | --- | --- |
| `cannibal_march_predation_column` | `cannibal_march_predation_column` | [Warrior with an Axe and Study of a Leg](https://commons.wikimedia.org/wiki/File:Warrior_with_an_Axe_and_Study_of_a_Leg_MET_DT6226.jpg), Fernand Cormon, 1897, Met object 1989.286.7; Commons file states CC0 1.0 | 1920x2746 | `E4F3DC05A815561EAE9120F97D5C1BFF8F9CCD3780B74E6ACA72632EC8245FFC` | Forward-loaded crouch/stride, visible boots and lower legs, broad axe crossing the torso, and a second compact haft/weapon; useful for a fast lightly equipped pursuit silhouette and paired-axe weapon logic. |
| `cannibal_network_cadre` | `cannibal_network_cadre` | [Kylix (cup) depicting a kneeling archer](https://artmuseum.princeton.edu/art/collections/objects/109374), attributed to the Pithos Painter, ca. 490 BCE, Princeton object 2015-11; Princeton policy permits free download/use of public-domain work images without approval | 3000x2325 | `A300824E860ED5081BC3BF3E1B169DDF681C570713C772AD72C2B527FF75AC27` | Compact kneeling/crouched profile with bow arm, draw direction, and quiver; useful for a low scout/courier silhouette that can later add a knife and use a short bow or sling. |
| `cannibal_bone_riders` | `cannibal_bone_riders` | [Soldaat met speer te paard in een rivier](https://www.rijksmuseum.nl/en/collection/object/Soldaat-met-speer-te-paard-in-een-rivier--a528c46bb93ae7249f4c4185f293e723), Jean Audran after Charles Le Brun, 1677-1756, Rijksmuseum RP-P-1967-203; object record states Public domain | 1743x1864 | `9C29933C376B8BF16D7FB76E41FE95A6A30D43A1FC7052AB14DCCE1C2FE592C8` | Complete horse with body, hindquarters, lifted forelegs, hooves, and ground contact; rider leans forward and holds a spear one-handed, giving strong action and later sling/short-javelin logic for rigging. |

Access date for all three sources: 2026-08-22 (Europe/Kiev).

## Durable repository paths

Each job's full provenance, source-page URLs, creator/title/date/license, fit rationale, adaptation boundary, uncertainty, source/preview/DDS hashes, and exact dimensions is in `refs/sourced/source_manifest.json`.

- March original: `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/refs/sourced/original/cannibal_march_predation_column_source.jpg`.
- March preview and DDS: `.../cannibal_march_predation_column/refs/sourced/processed/cannibal_march_predation_column_source.png` and `.../cannibal_march_predation_column/refs/sourced/dds/cannibal_march_predation_column_source.dds`.
- Network original: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/sourced/original/cannibal_network_cadre_source.jpg`.
- Network preview and DDS: `.../cannibal_network_cadre/refs/sourced/processed/cannibal_network_cadre_source.png` and `.../cannibal_network_cadre/refs/sourced/dds/cannibal_network_cadre_source.dds`.
- Bone Riders original: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/sourced/original/cannibal_bone_riders_source.jpg`.
- Bone Riders preview and DDS: `.../cannibal_bone_riders/refs/sourced/processed/cannibal_bone_riders_source.png` and `.../cannibal_bone_riders/refs/sourced/dds/cannibal_bone_riders_source.dds`.

The PNGs are native-resolution RGBA decodes with no crop, repaint, recolour, or background removal. The DDS files are evidence-only one-level uncompressed BGRA conversions made with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; none is a runtime texture or 2D sprite.

## Runtime handoff boundary

The proposed downstream entity tokens are `cannibal_march_predation_column_entity`, `cannibal_network_cadre_entity`, and `cannibal_bone_riders_entity`. The proposed runtime roots are `gfx/models/units/014_cannibalism/cannibal_march_predation_column/`, `gfx/models/units/014_cannibalism/cannibal_network_cadre/`, and `gfx/models/units/014_cannibalism/cannibal_bone_riders/`; a 3D entity has no 2D sprite field.

These references are design direction for a later one-image model-input step. Adaptation must independently create the fictional Event 014 subjects, remove source-specific historical costume cues, and preserve the requested action/weapon logic. Do not copy the images as final model art, claim historical or cultural authenticity, or carry forward identifiable living Indigenous regalia, sacred motifs, or culture-specific paint.

## Uncertainty and review notes

The March Commons page declares a 2797x4000 original, but Wikimedia returned HTTP 429 for that original during access; the archived 1920x2746 rendition is a complete full-subject image and its CC0 file-page record is preserved. The Met object page supplies institutional provenance but states that its image cannot be downloaded, so parent review should confirm that the Commons CC0 record is the intended reuse basis before any redistributed adaptation.

The Network reference is a museum photograph of a vessel, with the crouched archer bounded inside a tondo rather than isolated on a plain canvas; later adaptation must redraw the figure as a standalone courier and must not reproduce the pottery or inscription.

The Bone Riders reference is a public-domain print of a historical/classical military scene; use only the complete horse anatomy, rider seat, forward action, and one-handed weapon handling, replacing the helmet, armor, and spear during adaptation.

No contact sheet was created because one candidate was selected for each job and no unresolved multi-candidate comparison remained. Parent approval is still required before these references become exact model inputs.
