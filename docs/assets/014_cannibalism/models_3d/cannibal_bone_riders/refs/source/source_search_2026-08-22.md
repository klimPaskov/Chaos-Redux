# Bone Riders modern-source audit, 2026-08-22

Status: `blocked_no_eligible_exact_source_selected`.

The one-image gate requires modern designed artwork from a game, production/concept page, tabletop/miniature render, fantasy illustration, or professional creature/character design. The exact brief is one complete living horse with skull/rib/long-bone barding and coherent tack, one feral rider with a painted skull helmet, a visible sling and stone pouch, no spear, four readable horse legs, and no living-Indigenous material. Copyrighted work is allowed as `user_authorized_reference_use/reference_only` under the parent clarification, but explicit NoAI restrictions remain disqualifying. If an eligible source is approved, ImageGen may only perform faithful resolution, alpha, background, padding, or edge cleanup; no redesign or invented component is allowed. No ImageGen or Meshy call was made.

## Closest new candidates

`candidates/bone_awakened_horseman.jpg` is the strongest single-image rider-plus-mount geometry reference. It is Guild Wars 2 production concept art credited by the Guild Wars Wiki category to Doug Williams. The image has one mounted rider, a dramatic full horse silhouette, bone/skull-like barding, saddle/tack, and a feral armored rider. It fails the exact gate because the horse is visibly skeletal/undead rather than a living horse under bone barding, the rider carries a long spear, no sling or stone pouch is visible, and one horse leg is occluded by the rearing pose. It is commercial game art with no reuse license stated; retain as `user_authorized_reference_use/reference_only` and provenance-uncertain.

- Source category: https://wiki.guildwars.com/wiki/Category%3AArt_by_Doug_Williams
- Source file page: https://wiki.guildwars.com/wiki/File:Awakened_Horseman_concept_art.jpg
- Direct image: https://wiki.guildwars.com/images/e/e7/Awakened_Horseman_concept_art.jpg
- Local source: `refs/source/candidates/bone_awakened_horseman.jpg`
- SHA-256: `90325F751B1F1BF1B9E7D9FD00F103221ED47A89E43D4C9E518FA5C926390BAD`
- Dimensions: `720x664`
- Derived preview: `refs/source/processed/bone_awakened_horseman_preview.png`
- Evidence DDS: `refs/source/dds/bone_awakened_horseman_preview.dds`

`candidates/bone_diablo_mount.jpg` is the strongest living-horse and bone-armor alternate. The Diablo 4 production sheet includes a living horse with skull/bone-like head and body armor, recognizable tack, and visible legs. It is not eligible as the exact one-image source because it is a multi-view/multi-horse sheet with no rider, includes unrelated equipment including spear-like forms, and does not show a sling or stone pouch. It is commercial production art; no license or explicit NoAI statement was found in the reviewed article, so use only as `user_authorized_reference_use/reference_only`.

- Source page: https://www.windowscentral.com/gaming/diablo-4-blizzard-president-clarifies-how-mounts-work
- Direct image: https://cdn.mos.cms.futurecdn.net/8bpBNBz2hHEmp7xWTvQHQD.jpg
- Local source: `refs/source/candidates/bone_diablo_mount.jpg`
- SHA-256: `5AD6EEC5C0410A78EE092CEFDF85C7C48C8CC27FE3EAF259449E9A998328C27A`
- Dimensions: `4500x2531`
- Derived preview: `refs/source/processed/bone_diablo_mount_preview.png`
- Evidence DDS: `refs/source/dds/bone_diablo_mount_preview.dds` (converted at `2048x1152` for evidence size)

The Ponyfinder *Skeletal Pony Slinger* bestiary result is a useful sling-and-pouch cue, but it depicts a standalone undead pony with a jaw-mounted sling and small pouch, not a living horse or rider. The PDF mirror was unavailable for local archival, so it is a link-only context alternate and not a selected source: https://files.spawningpool.net/docs/Vault2.0.-.TTRPG-Gamebooks/Ponyfinder%20Collection%20%28PF1%20SF1%20DND5e%29/Ponyfinder%20-%20Everglow%20Bestiary.pdf.

## Existing modern candidates retained for comparison

The existing Abe Taraky rider image (`refs/sourced/modern/original/cannibal_bone_riders_modern_abe_taraky_rider.jpg`, SHA-256 `128AACEFC917DA785C1B67F9EDC01BB9BCF26CAB9BDD3893877DCC60889845D0`) has a strong forward rider/horse silhouette but crops the horse and has no readable sling, pouch, living horse, or four-leg anatomy. Its portfolio page reserves copyright, so it is reference-only.

The existing MyMiniFactory skeleton-horse archer (`refs/sourced/modern/original/cannibal_bone_riders_modern_myminifactory_skeleton_horse_archer.jpg`, SHA-256 `0AB406C0C341C45457597FF36757F28DC4D7714753A16D6D7A91B9B12A883B7E`) is a paid/restricted tabletop render with a cropped undead horse and archer, not a living bone-barded horse or slinger. The existing Skelly Nelly image is a museum/anatomical photograph and remains rejected as the wrong source family.

The comparison sheet is `refs/source/contact_sheet_bone_candidates.png`. The generated `refs/original/meshy_input.png`, SHA-256 `D3929E3D7584FDFBD42B596C26AF316195341F0BB3A730AA7CFBD4B78721AC15`, and the previously excluded second user image were not used.

## Gate decision and recommendation

No single reviewed candidate satisfies all visual gates. The provisional recommendation for rider/horse contact and bone-barding language is `bone_awakened_horseman.jpg`, but it is not an eligible exact source because it is undead and spearfocused. The provisional recommendation for living horse and armor construction is `bone_diablo_mount.jpg`, but it is not an eligible exact source because it is a multi-view horse-only sheet. Do not combine these images into a composite or submit either one as if it passed the exact gate. The package remains blocked pending a parent/user-supplied or newly found single artwork image that visibly includes the living barded horse, feral sling rider, stone pouch, and no spear.
