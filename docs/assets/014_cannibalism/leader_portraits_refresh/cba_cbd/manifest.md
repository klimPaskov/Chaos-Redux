# Event 014 CBA-CBD Warlord Portrait Manifest

Status: 7 unique DDS assets remain installed after the 2026-07-16 portrait reduction; 21 attachment-listed CBA-CBD DDS paths were retired.

## 2026-07-16 reduction amendment

The requested retirement removes the final CBA-CBD DDS files listed in the attached deletion list. The remaining unique live textures are:

- CBA: `leader_CBA_warlord_middle_east.dds`, `leader_CBA_warlord_south_america.dds`
- CBB: `leader_CBB_warlord_middle_east.dds`
- CBC: `leader_CBC_warlord.dds`, `leader_CBC_warlord_south_america.dds`
- CBD: `leader_CBD_warlord_north_america.dds`, `leader_CBD_warlord_south_america.dds`

Existing sprite names remain valid through deliberate retained-texture aliases in `interface/014_cannibalism.gfx`: removed CBA base/Europe, Asia, Africa, North America, and Oceania names use CBA Middle East; removed CBB base/Europe, Asia, Africa, North America, South America, and Oceania names use CBB Middle East; removed CBC Asia, Africa, Middle East, North America, and Oceania names use the CBC base; and removed CBD base/Europe, Asia, Africa, Middle East, and Oceania names use CBD North America. The historical source, processed, metadata, prompt, and review records remain in this package as provenance for the retired generation set and are not live game textures.

## Historical package contents (pre-reduction)

- 28 independently generated fictional source masters under `source_png/`.
- 28 deterministic 156x210 HOI4 portrait PNGs under `processed_png/`.
- 28 processor metadata records under `metadata/`.
- 28 per-portrait comparison sheets under `review_sheets/`.
- Labelled final sheet at `contact_sheets/cba_cbd_warlords_contact_sheet.png`.
- Enlarged scalp, face, and silhouette sheet at `contact_sheets/cba_cbd_baldness_audit_contact_sheet.png`.
- Generation-group review sheets at `contact_sheets/cba_cbb_hoi4_repaint_contact_sheet.png` and `contact_sheets/cbc_cbd_hoi4_repaint_contact_sheet.png`.
- Historical 28/28 visual checklist at `baldness_audit.md`.
- Prompt, action, generated-output, and source-hash record at `prompts/warlord_prompts.md`.
- Live-file and sprite registration record at `gfx_handoff.md`.
- Mechanical verification record at `validation.md`.

The historical selected source, processed, and DDS sets each contain 28 unique SHA-256 hashes. Every portrait came from its own built-in ImageGen result; none was created by recolouring, mirroring, warping, filtering, or transforming another portrait. The historical visual sheet confirms distinct anatomy, expression, clothing, hand action, prop, background, and silhouette across all 28 slots.

## Historical asset map (pre-reduction)

Each identifier below has the matching files `source_png/<identifier>_source.png`, `processed_png/<identifier>.png`, `metadata/<identifier>.json`, `review_sheets/<identifier>_review.png`, and `gfx/leaders/014_cannibalism/<identifier>.dds`.

| Tag | Europe/default | Africa | Asia | Middle East | North America | Oceania | South America |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CBA | `leader_CBA_warlord` | `leader_CBA_warlord_africa` | `leader_CBA_warlord_asia` | `leader_CBA_warlord_middle_east` | `leader_CBA_warlord_north_america` | `leader_CBA_warlord_oceania` | `leader_CBA_warlord_south_america` |
| CBB | `leader_CBB_warlord` | `leader_CBB_warlord_africa` | `leader_CBB_warlord_asia` | `leader_CBB_warlord_middle_east` | `leader_CBB_warlord_north_america` | `leader_CBB_warlord_oceania` | `leader_CBB_warlord_south_america` |
| CBC | `leader_CBC_warlord` | `leader_CBC_warlord_africa` | `leader_CBC_warlord_asia` | `leader_CBC_warlord_middle_east` | `leader_CBC_warlord_north_america` | `leader_CBC_warlord_oceania` | `leader_CBC_warlord_south_america` |
| CBD | `leader_CBD_warlord` | `leader_CBD_warlord_africa` | `leader_CBD_warlord_asia` | `leader_CBD_warlord_middle_east` | `leader_CBD_warlord_north_america` | `leader_CBD_warlord_oceania` | `leader_CBD_warlord_south_america` |

`leader_CBA_warlord_south_america` is the set's sole skull-prop licking portrait. The tongue-to-temple contact is readable in both the final portrait and contact sheet. Other bone- or tooth-like objects are differentiated by action and, where moderation-safe reinterpretation was needed, are visibly artificial carved, resin, paper, or wooden props.

## Provenance and processing

- Source type: fictional built-in ImageGen; no real-person or actor likeness requested.
- Style-only references: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`, `ire_eamon_de_valera.png`, and `fin_carl_mannerheim.png`.
- Finish: `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py leader`, explicit full-source crop, `source-kind fictional`, 156x210 output, processor version 2.0.
- DDS conversion: `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 156 --height 210`, producing uncompressed 32-bit RGBA/BGRA-compatible DDS files.
- Historical visual decision: 28/28 approved as bald fictional adult men with readable actions, distinct silhouettes, matte opaque oil/gouache handling, simplified painted facial planes, muted interwar values, and no photographic, modern-digital, prison, cell, bar, cage, restraint, or confinement imagery.

## Image-generation accounting

- Selected successful built-in outputs: 28, one independent selected master per portrait.
- Visually superseded successful outputs: two. CBD North America was retried to move the kiss onto the skull's front incisors; CBD Oceania kept the version whose threaded counters read most clearly as teeth at 156x210.
- Moderation-blocked attempts: one non-persisted CBB default request; its accepted retry used the same unnerving action with an unmistakably artificial stuffed-canvas mascot.
- Total portrait invocations: 31, comprising 28 selected outputs, two persisted visual supersessions, and one non-persisted moderation rejection.
- No requested slot remains unresolved, and no CLI, local procedural, alternate-model, transformed-old-portrait, source-substitution, or derivative-image fallback was used.

The selected generated-output filenames, actions, source hashes, and moderation-safe prompt deltas are recorded in `prompts/warlord_prompts.md`.
