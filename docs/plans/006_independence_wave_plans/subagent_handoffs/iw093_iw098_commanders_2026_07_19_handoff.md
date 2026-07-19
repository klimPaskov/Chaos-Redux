# IW-093 / IW-098 commander portrait handoff

Status: `complete_for_static_commander_assets`

This package contains four distinct fictional, ImageGen-created, apparent-male army commander portraits. The source and processed PNGs, prompts, contact sheet, manifest, and hashes are retained under:

`docs/assets/006_independence_wave/iw093_iw098_commanders_2026_07_19/`

No advisor icons, advisor portraits, advisor sprites, dossier cards, or advisor manifests were created.

## Runtime DDS files

All files are legacy one-level uncompressed 32-bit BGRA DDS converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`:

| Commander | Full DDS | Small DDS | Proposed full sprite | Proposed small sprite |
| --- | --- | --- | --- | --- |
| DOX Kwame Frimpong | `gfx/leaders/006_independence_wave/portrait_DOX_kwame_frimpong.dds` | `gfx/leaders/006_independence_wave/portrait_DOX_kwame_frimpong_small.dds` | `GFX_portrait_DOX_kwame_frimpong` | `GFX_portrait_DOX_kwame_frimpong_small` |
| DOX Kwaku Ntim | `gfx/leaders/006_independence_wave/portrait_DOX_kwaku_ntim.dds` | `gfx/leaders/006_independence_wave/portrait_DOX_kwaku_ntim_small.dds` | `GFX_portrait_DOX_kwaku_ntim` | `GFX_portrait_DOX_kwaku_ntim_small` |
| SOK Umaru Gwadabawa | `gfx/leaders/006_independence_wave/portrait_SOK_umaru_gwadabawa.dds` | `gfx/leaders/006_independence_wave/portrait_SOK_umaru_gwadabawa_small.dds` | `GFX_portrait_SOK_umaru_gwadabawa` | `GFX_portrait_SOK_umaru_gwadabawa_small` |
| SOK Bello Rabah | `gfx/leaders/006_independence_wave/portrait_SOK_bello_rabah.dds` | `gfx/leaders/006_independence_wave/portrait_SOK_bello_rabah_small.dds` | `GFX_portrait_SOK_bello_rabah` | `GFX_portrait_SOK_bello_rabah_small` |

The parent wired all eight stable sprite contracts in `interface/006_independence_wave_iw093_iw098_portraits.gfx`. Full canvases are `156x210`; small commander miniatures are `65x67` and are direct crops of the approved full portrait, not advisor dossier cards.

## Visual review

- DOX Kwame Frimpong: older Gold Coast/Asante colonial veteran, khaki service uniform, restrained decorations, calm forest-command bearing.
- DOX Kwaku Ntim: younger Asante forest guard organizer, practical period khaki field gear, assertive alert expression.
- SOK Umaru Gwadabawa: older mounted frontier commander, pale turban and sand cavalry clothing, dignified expression.
- SOK Bello Rabah: younger caravan/security officer, indigo-and-sand period clothing, alert watchful expression.

The contact sheet shows all four full portraits, native small miniatures, and 4x nearest-neighbour miniature review. Portraits are clearly male, fictional, respectful, text-free, flag-free, gore-free, and static. Generated art uses no modern equipment and does not reuse the protected BAY or RHI portraits.

## Validation evidence

`metadata/hashes.json` records SHA-256 values, dimensions, alpha ranges, DDS header fields, and exact decoded RGBA equality for all eight DDS files. The full DDS files are 131,168 bytes (`128 + 156*210*4`); the small DDS files are 17,548 bytes (`128 + 65*67*4`). All DDS headers report `pf_size=32`, flags `65`, fourCC `0`, bit count `32`, BGRA masks `0x00ff0000/0x0000ff00/0x000000ff/0xff000000`, and `DDSCAPS_TEXTURE=0x1000`.

## Main-agent wiring notes

The parent wired all four explicitly male corps commanders, names, descriptions,
full/miniature sprites, exact prepared-scope recruitment, roster proofs, cleanup,
and the generation-bound Event 006 starting-force transaction. The package was
accepted after direct contact-sheet review. The reusable skill reference surface
now exists at `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/`
with curated male leader and commander examples. No fallback asset was used.
