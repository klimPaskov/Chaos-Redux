# Event 006 Brittany portrait GFX handoff

## Runtime registry

`interface/006_independence_wave_brittany_portraits.gfx` owns these exact sprites:

| Sprite | Texture | Consumer |
|---|---|---|
| `GFX_portrait_BRI_independence_wave_civic_commission` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds` | `BRI_independence_wave_civic_delegate` civilian large portrait |
| `GFX_portrait_BRI_independence_wave_coastal_commandant` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds` | `BRI_independence_wave_coastal_commandant` civilian and army large portrait |
| `GFX_portrait_BRI_independence_wave_coastal_commandant_small` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant_small.dds` | `BRI_independence_wave_coastal_commandant` army small portrait |

Character generation and `set_portraits` calls live in `common/scripted_effects/006_independence_wave_brittany_package_effects.txt`. They are guarded by exact `has_character` checks.

## Verification

- Large DDS files decode at 156 by 210 BGRA.
- The commander small DDS is an independent `65x67` BGRA dossier card with
  alpha and transparent outer corners. Its SHA-256 is
  `12c1a20d2cc1234895e7af557bda9baf7cddca58593527194b5edad3af058684`.
- `contact_sheets/006_bri_runtime_portraits_contact_sheet.png` was rebuilt from
  the decoded runtime DDS files. Its panels are Tangi Kerbrat large, Jodoc Tanet
  large, and the corrected Jodoc Tanet dossier enlarged for inspection.
- Full processing, vanilla comparison, retained DDS, and header validation
  evidence is in `../army_small_dossier_correction_2026_07_15/`.
- Both characters are invented. The civic sprite is a single human portrait and no group or institutional image is wired.
- The existing RHI and BAY approved historical portraits and sprite files were not edited.

## Reuse

Focus and decision art reuses the existing Event 006 icon registry. The vanilla BRI flag and historical political portrait families remain authoritative. No new flags, focus icons, decision icons, or advisor sprites are introduced here.
