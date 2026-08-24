# Bone Riders sourced model-reference handoff

Status: `blocked_no_eligible_exact_source_selected`; no runtime GFX wiring was changed.

Proposed runtime/model basename from the job root: `cannibal_bone_riders`. No exact source is cleared for provider input, and the existing generated `refs/original/meshy_input.png` must not be overwritten or reused. A future approved provider input would use the job's standard `meshy_input.png` basename only after the parent accepts a single source passing every visual gate.

Closest rider-plus-mount alternate: `candidates/bone_awakened_horseman.jpg`.

- Source pages: https://wiki.guildwars.com/wiki/Category%3AArt_by_Doug_Williams and https://wiki.guildwars.com/wiki/File:Awakened_Horseman_concept_art.jpg
- Direct image: https://wiki.guildwars.com/images/e/e7/Awakened_Horseman_concept_art.jpg
- SHA-256: `90325F751B1F1BF1B9E7D9FD00F103221ED47A89E43D4C9E518FA5C926390BAD`
- Rights: commercial Guild Wars artwork, no third-party license stated; `user_authorized_reference_use/reference_only`.
- Visual gate failure: undead skeletal horse, prominent spear, no sling or stone pouch, and one horse leg occluded in the rearing pose.
- Evidence preview: `processed/bone_awakened_horseman_preview.png` (SHA-256 `2FF002B8D468251871392131A00B603B21A9DDC2893156243653AD10A0E7859D`).
- Evidence DDS: `dds/bone_awakened_horseman_preview.dds` (SHA-256 `E17FC19BDA40FC5DE61B29C3A6769E6EDE4778D16DA1012B59C0EE8C526AABD3`).

Closest living-horse armor alternate: `candidates/bone_diablo_mount.jpg` (SHA-256 `5AD6EEC5C0410A78EE092CEFDF85C7C48C8CC27FE3EAF259449E9A998328C27A`; source https://www.windowscentral.com/gaming/diablo-4-blizzard-president-clarifies-how-mounts-work; direct image https://cdn.mos.cms.futurecdn.net/8bpBNBz2hHEmp7xWTvQHQD.jpg). It is a multi-view/multi-horse sheet with no rider, sling, or pouch and includes spear-like equipment. Its evidence DDS is `dds/bone_diablo_mount_preview.dds` (SHA-256 `65B61E123EA01B370EEA6E33C7A94C578E0678766D4790B955AE37871169DFCE`; converted at 2048x1152).

Manifest: `provenance.json`. Search record: `source_search_2026-08-22.md`. Comparison sheet: `contact_sheet_bone_candidates.png`.

No ImageGen, Meshy, crop, repaint, compositing, or runtime installation occurred. Parent/user must supply or approve a new single artwork source that visibly contains the living bone-barded horse, feral sling rider, stone pouch, no spear, and complete four-leg anatomy.
