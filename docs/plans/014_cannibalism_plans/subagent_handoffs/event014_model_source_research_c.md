# Event 014 model source research C — modern artwork revision

Historical supersession notice: this research record is retained for source provenance only. The 2026-08-26 decision assigns Network Cadre vanilla `sprite = infantry` and Bone Riders vanilla `sprite = cavalry`, so their former source-review rows are not current custom-model work queues.

Status at handoff: three modern visual references are archived and selected for parent review. The selections are modern game art, game concept art, and professional fantasy character art as required by the latest user correction. The downloaded originals, source-page records, manifests, processed PNG previews, DDS evidence copies, rejected alternatives, and historical adaptation briefs are separate from the superseded archival set. The parent’s current gate permits only faithful enhancement of an approved actual source, not redesign or generated-from-scratch input.

This package covers only `cannibal_march_predation_column`, `cannibal_network_cadre`, and `cannibal_bone_riders`. It does not create or approve final model geometry, does not run ImageGen or Meshy, and does not edit gameplay, runtime, entity, unit, `.gfx`, `.asset`, event, localisation, or existing production manifest files.

The user-provided attachment `C:/Users/klimp/AppData/Local/Temp/codex-clipboard-59672c99-c6a5-4728-9ab5-71e311186bd4.png` was explicitly excluded and was not opened, copied, or used. Attachment #2 was excluded entirely.

## Modern selections

| Job | Selected source and usage status | Downloaded original | Dimensions and SHA-256 | Fit and required transformation |
| --- | --- | --- | --- | --- |
| `cannibal_march_predation_column` | [Best Classes in Dark and Darker](https://mobalytics.gg/blog/tier-lists/dark-and-darker-best-classes/) barbarian action artwork, direct image [download](https://cdnportal.mobalytics.gg/production/2022/12/97984ea9-dark-and-darker-f-barbarian-1.jpg); uncredited game artwork hosted by Mobalytics; license not stated; reference-only and not licensed. | `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/refs/sourced/modern/original/cannibal_march_predation_column_modern_dark_and_darker_barbarian.jpg` | 848x951; `199E5E18F68835525A83F0B7CC16EB011FD0D08AD4A0D6859C0C7CC1065B89A8` | Full-body forward charge with two compact axes and readable leg separation. The adaptation must remove the source game's helmet, fur, armor, backpack, face, colors, and recognizable design language and produce the requested bare-chested, dark-haired, lightly equipped pursuit runner. |
| `cannibal_network_cadre` | [archer](https://opengameart.org/content/archer-0) by kirill777; source page states CC-BY 3.0; research attribution required; final model must still be substantially original. Direct image [download](https://opengameart.org/sites/default/files/net%D0%B5_0.jpg). | `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/sourced/modern/original/cannibal_network_cadre_modern_oga_archer_concept.jpg` | 1602x1199; `FF2EC66A332FDDDDE8A4757EE39E74A4D30F2F024F4E6D61B3C1AC8524D67F5F` | Modern game concept collage includes a crouched bow draw, full-body scout silhouettes, quiver, and compact gear. The adaptation must create one gaunt crouched scout/courier, add a readable knife, remove source hood, cloak, colors, labels, exact poses, and ornaments, and avoid cultural authenticity cues. |
| `cannibal_bone_riders` | [Lines](https://www.abetaraky.com/lines-1/) by Abe Taraky, image `Rider_09d_AT_NS.jpg`; portfolio explicitly states copyright © Abe Taraky 2024 and prohibits unauthorized reproduction/distribution; reference-only and not licensed. Direct image [download](https://images.squarespace-cdn.com/content/v1/59fa66de4c326d506e72b58f/1708734525574-XW0WGI64JDC7RJ7O7ER6/Rider_09d_AT_NS.jpg). | `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/sourced/modern/original/cannibal_bone_riders_modern_abe_taraky_rider.jpg` | 848x1300; `128AACEFC917DA785C1B67F9EDC01BB9BCF26CAB9BDD3893877DCC60889845D0` | Professional fantasy artwork supplies the extreme mounted counterbalance and bone silhouette. The adaptation must show a complete living horse under sparse bone armour, all four legs for rigging, a generic skull-like helmet, a one-handed sling, and a stone pouch with visible stones; it must not retain the undead skeletal anatomy or copy the source character. |

Access date for all three sources: 2026-08-22 (Europe/Kiev).

## Per-job records

Each modern source directory contains `source_manifest.json`, an archived source page or provenance capture, the untouched original, `processed/` RGBA PNG evidence, `dds/` converter evidence, and `imagegen_adaptation_brief.md`.

- March manifest: `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/refs/sourced/modern/source_manifest.json`.
- March adaptation brief: `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/refs/sourced/modern/imagegen_adaptation_brief.md`.
- Network manifest: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/sourced/modern/source_manifest.json`.
- Network adaptation brief: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/sourced/modern/imagegen_adaptation_brief.md`.
- Bone Riders manifest: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/sourced/modern/source_manifest.json`.
- Bone Riders adaptation brief: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/sourced/modern/imagegen_adaptation_brief.md`.

The group-C-specific modern contact sheet is `docs/assets/014_cannibalism/models_3d/sourced_reference_contact_sheet_modern_group_c.png` with SHA-256 `493B987028BF66483B7A7AF46C69C046DB1917C90D666C7F74A7EC8692738958` and dimensions 1640x984. It compares the three selections with representative rejected modern alternatives and does not alter the shared group-B contact sheet.

The group-C-specific modern graphics handoff is `docs/assets/014_cannibalism/models_3d/gfx_handoff_modern_group_c.md`. It lists proposed downstream entity tokens and runtime basenames without wiring them.

The selected PNG previews are native-resolution RGBA conversions with no crop, repaint, recolour, or background removal. The DDS files are one-level uncompressed BGRA evidence conversions made with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; none is a runtime texture or 2D sprite.

## Adaptation boundary and safety

All three selected works are reference direction only and no provider input is approved. The prior substantially-original ImageGen instruction is superseded; an approved source must retain its identity and may receive faithful enhancement only.

March's selected artwork is intentionally stronger on aggressive action and paired-axe readability than the rejected OGA turnaround, but its heavy armor conflicts with the requested lightly equipped runner; that conflict is explicitly resolved in the adaptation brief.

Network's CC-BY source supports attribution and generic adaptation, but the collage format and source-specific hood and cape still require a new one-subject composition and a separately visible knife.

Bone Riders is the main legal and geometric blocker: Abe Taraky's source is clearly copyrighted and lacks a complete horse, sling, stone pouch, and skull helmet. It is retained only as reference direction, and the adaptation brief makes each missing requirement mandatory rather than implying the source supplies it.

No selected source uses identifiable living Indigenous regalia, sacred motifs, culture-specific paint, or cultural authenticity claims. No user attachment was used.

## Rejected and superseded evidence

The earlier archival files and manifests remain in place and were not silently deleted. Every modern per-job manifest records the prior manifest path and marks it `superseded_rejected_archival` because the user correction excludes archival photographs, museum paintings or drawings, historical plates, antiquities, and archaeological art.

Representative rejected modern alternatives are retained and documented in the per-job manifests. The March OGA barbarian is permissively licensed but too static and marked with unsuitable blue paint; the Sketchfab orc is not clearly reusable. The Bone Riders MyMiniFactory render has useful skull and horse cues but is a paid product with no stated reuse license and a cropped horse; the Commons exhibit photo is the wrong source family.

There are no gameplay, runtime, GFX, entity, or unit changes in this handoff. Parent approval is required before any modern reference is passed to ImageGen or Meshy.
