# Event 014 sourced model-art handoff

Date: 2026-08-22

Scope completed: Internet-sourced modern artwork research and source archiving for `cannibal_network_cadre` and `cannibal_bone_riders`. No ImageGen, Meshy, provider submission, model generation, GFX edit, or gameplay edit was performed.

## Network Cadre

Status: `needs_user_review`.

Recommended provisional source: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_gamepro_blackguards_2398929.jpg`.

- Source page: https://www.gamepro.de/galerien/das-schwarze-auge-blackguards%2C96655.html
- Direct image: https://images.cgames.de/images/gsgp/287/das-schwarze-auge-blackguards-artworks_2398929.jpg
- SHA-256: `86965DD293DB0BAC1F3F983BD9CC90C473BE95B2998792EBF05925608D6AA93E`
- Visual fit: one full-body low-crouch game archer with bow, quiver, readable complete limbs, and a hip sidearm that reads closer to a short sword than a narrow knife.
- Rights/provenance: commercial production/gallery art; no reuse license stated. Record as `user_authorized_reference_use/reference_only`; no explicit NoAI restriction was found in reviewed page/image metadata, but this is not a permission grant.
- Processed PNG: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/processed/network_gamepro_blackguards_2398929_preview.png`, SHA-256 `A6C2296F5F2E9E7A648BC2F8DBF30D421678FA585936D37BE87AA50C6248FC54`.
- Evidence DDS: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/dds/network_gamepro_blackguards_2398929_preview.dds`, SHA-256 `DF1F52294B341B6E963FB821006FB110EF63936ECC4DB6FBCDD4FC70DC2B1555`.

Visual-exactness alternate: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/candidates/network_magicartworld_archer_fantasy.jpg`, SHA-256 `2D16DA4A8E7A605F80B885B01964900C87FF4D3077861FF3AA7981D18F0CEDEE`, source page https://magicartworld.com/female-warriors-inspiration-art/, direct image https://magicartworld.com/wp-content/uploads/2019/08/Archer-Fantasy.jpg. It has the clearer two-knife cue but an unidentified original artist and indeterminate Pinterest/AI origin. Existing CC-BY 3.0 OpenGameArt `kirill777` archer collage is retained as a permissive but weaker alternate because it is multi-figure and lacks a clear knife.

Exact proposed runtime/model basename: `cannibal_network_cadre`. No runtime basename or `.gfx` wiring was changed. The existing generated `refs/original/meshy_input.png` remains untouched and is not part of this source recommendation.

## Bone Riders

Status: `blocked_no_eligible_exact_source_selected`.

No reviewed single artwork passes all required gates at once: living horse; skull/rib/long-bone barding; coherent tack; feral skull-helmet rider; visible sling and stone pouch; no spear; complete four-leg anatomy; and no living-Indigenous material.

Closest rider-plus-mount alternate: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/candidates/bone_awakened_horseman.jpg`, SHA-256 `90325F751B1F1BF1B9E7D9FD00F103221ED47A89E43D4C9E518FA5C926390BAD`, source pages https://wiki.guildwars.com/wiki/Category%3AArt_by_Doug_Williams and https://wiki.guildwars.com/wiki/File:Awakened_Horseman_concept_art.jpg, direct image https://wiki.guildwars.com/images/e/e7/Awakened_Horseman_concept_art.jpg. It gives the best single mounted rider, bone-barding, saddle/tack, and contact silhouette, but depicts an undead skeletal horse, includes a prominent spear, omits sling and stone pouch, and occludes one horse leg. Treat as `user_authorized_reference_use/reference_only`.

Closest living-horse armor alternate: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/candidates/bone_diablo_mount.jpg`, SHA-256 `5AD6EEC5C0410A78EE092CEFDF85C7C48C8CC27FE3EAF259449E9A998328C27A`, source page https://www.windowscentral.com/gaming/diablo-4-blizzard-president-clarifies-how-mounts-work, direct image https://cdn.mos.cms.futurecdn.net/8bpBNBz2hHEmp7xWTvQHQD.jpg. It provides living-horse bone/armor and tack cues, but is a multi-view/multi-horse sheet with no rider, sling, or stone pouch and includes spear-like equipment. Its DDS evidence was resized to 2048x1152.

Exact proposed runtime/model basename: `cannibal_bone_riders`. No source is cleared for a future `meshy_input.png`, and the generated `refs/original/meshy_input.png` plus the previously excluded second user image were not used.

## Files and audit records

- Network source search: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/source_search_2026-08-22.md`.
- Network provenance manifest: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/provenance.json`.
- Network source handoff: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/gfx_handoff.md`.
- Network contact sheet: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/source/contact_sheet_network_candidates.png`.
- Bone source search: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/source_search_2026-08-22.md`.
- Bone provenance manifest: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/provenance.json`.
- Bone source handoff: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/gfx_handoff.md`.
- Bone contact sheet: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/source/contact_sheet_bone_candidates.png`.

All source files, preview hashes, DDS evidence hashes, rights uncertainty, and visual-gate failures are recorded in the two provenance manifests. The parent owns any later source selection, exact-one-image provider submission, model generation, runtime wiring, and final acceptance review.
