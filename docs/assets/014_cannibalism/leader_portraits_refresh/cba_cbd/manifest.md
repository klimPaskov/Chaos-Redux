# Event 014 CBA-CBD Warlord Portrait Manifest

Status: visually approved and installed in the existing live DDS paths.

## Package contents

- 28 distinct image-generation source masters under `source_png/`.
- 28 deterministic 156x210 HOI4 portrait PNGs under `processed_png/`.
- 28 processor metadata records under `metadata/`.
- 28 per-portrait comparison sheets under `review_sheets/`.
- One labelled final review sheet at `contact_sheets/cba_cbd_warlords_contact_sheet.png`.
- One enlarged 28-portrait scalp review sheet at `contact_sheets/cba_cbd_baldness_audit_contact_sheet.png`.
- Explicit 28/28 review checklist at `baldness_audit.md`.
- Prompt and source-review record at `prompts/warlord_prompts.md`.
- Exact live-file and sprite registration record at `gfx_handoff.md`.

Every source is a separately generated fictional person with a smooth hairless scalp. Source and processed SHA-256 sets both contain 28 unique hashes. No portrait was created by recolouring, mirroring, warping, filtering, or otherwise transforming another portrait.

## Asset map

Each identifier below has the three matching files `source_png/<identifier>_source.png`, `processed_png/<identifier>.png`, and `gfx/leaders/014_cannibalism/<identifier>.dds`.

| Tag | Europe/default | Africa | Asia | Middle East | North America | Oceania | South America |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CBA | `leader_CBA_warlord` | `leader_CBA_warlord_africa` | `leader_CBA_warlord_asia` | `leader_CBA_warlord_middle_east` | `leader_CBA_warlord_north_america` | `leader_CBA_warlord_oceania` | `leader_CBA_warlord_south_america` |
| CBB | `leader_CBB_warlord` | `leader_CBB_warlord_africa` | `leader_CBB_warlord_asia` | `leader_CBB_warlord_middle_east` | `leader_CBB_warlord_north_america` | `leader_CBB_warlord_oceania` | `leader_CBB_warlord_south_america` |
| CBC | `leader_CBC_warlord` | `leader_CBC_warlord_africa` | `leader_CBC_warlord_asia` | `leader_CBC_warlord_middle_east` | `leader_CBC_warlord_north_america` | `leader_CBC_warlord_oceania` | `leader_CBC_warlord_south_america` |
| CBD | `leader_CBD_warlord` | `leader_CBD_warlord_africa` | `leader_CBD_warlord_asia` | `leader_CBD_warlord_middle_east` | `leader_CBD_warlord_north_america` | `leader_CBD_warlord_oceania` | `leader_CBD_warlord_south_america` |

`leader_CBA_warlord_south_america` is the required regional skull-lick portrait: one skull is held at cheek height and the tongue visibly contacts its temple.

## Provenance and processing

- Source type: fictional built-in image generation; no real-person or actor likeness requested.
- Visual references: Chaos Redux `assets/leader_portraits/contact_sheet.png`, its six source references, and vanilla leader portraits under the HOI4 installation.
- Finish: `.tools/process_hoi4_portrait.py leader`, full approved source crop, fictional source mode, 156x210 output.
- DDS conversion: `.tools/convert_to_dds.py`, uncompressed 32-bit BGRA with alpha.
- Review decision: all 28 final portraits approved against both contact sheets for smooth bald scalps, readable faces, distinct identities, restrained HOI4 treatment, and absence of prison/cell/confinement imagery.

## Image-generation accounting

- Warlord invocations: 45.
- Selected warlord source masters: 28.
- Initial four-invocation batch: no outputs persisted after moderation rejection of overly graphic wording.
- Rejected visible-hair sources preserved under `source_png/rejected/visible_hair/`: 9.
- Rejected smooth-bald but over-composed first-pass replacements preserved under `source_png/rejected/baldness_pass1_mild/`: 4.
- The final enlarged scalp audit confirms 28/28 approved sources have no visible scalp hair, follicles, hair shadow, stubble, buzz cut, fringe, or sideburns.
- Selected calls used the moderation-safe production wording recorded in `prompts/warlord_prompts.md` without reducing the requested feral character direction.
