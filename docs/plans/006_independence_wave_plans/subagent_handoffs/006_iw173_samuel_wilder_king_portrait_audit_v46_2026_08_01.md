# IW-173 HAW Samuel Wilder King portrait audit v46

**Date:** 2026-08-01

**Reviewer:** Independent Chaos Redux sourced visual asset auditor v46.

**Scope:** Brief audit of the corrected durable source/prompt basename contract, runtime DDS/GFX consumer, and advisor/small-art boundary. No runtime or asset file was edited by this audit.

## Outcome

**PASS for durable source alignment and runtime path integrity.** The strict runtime basename is `portrait_HAW_independence_wave_territorial_delegate`; the durable PNG/TXT pair, metadata, DDS, GFX sprite, and HAW character consumer now align. No advisor, dossier, `_small`, 65x67, commander, or operative art or consumer exists for this subject. The existing v44/v45 source, crop, repaint, 156x210, and 4x evidence remain accepted.

## Checks

| Check | Status | Evidence |
| --- | --- | --- |
| Durable PNG basename/source contract | **PASS** | `docs/assets/portraits/006_independence_wave/portrait_HAW_independence_wave_territorial_delegate.png` is 826x1206 RGB PNG, SHA-256 `64a6049946e3603e0a67ee14950f87253dd651a9dce6eedfeb8f6d4ff5833e22`. Independent Pillow comparison found decoded RGB pixels exactly equal to the immutable archival master `source_png/HAW_samuel_wilder_king_PP-74-9-002_original.jpg` (826x1206 RGB, SHA-256 `cba16c7d7b3e0efdd36240ec945663947ad727e0536757ea7cbd72156b0dcde3`). |
| Durable prompt basename/content | **PASS** | `docs/assets/portraits/006_independence_wave/portrait_HAW_independence_wave_territorial_delegate.txt` shares the exact runtime basename, is 563-byte UTF-8 text with SHA-256 `66f62877957c5903326a5e277c723967a697e4e388917f1a15df8c6ed4b2bfec`, starts with `hoi4_portrait,`, contains no subject name, and describes established role facts plus visible appearance in one natural-language prompt. |
| Metadata pair/runtime alignment | **PASS** | `metadata/HAW_samuel_wilder_king_manual_export_v1.json` (SHA-256 `7db3e88aac0f74ac966ff1af8c5037b6c8d61743399092bc87d789970c4fd99e`) records the corrected PNG/TXT paths, source hash `64a604...`, `source_kind=lossless_png_copy_of_immutable_archival_master`, consumer `HAW_independence_wave_territorial_delegate`, DDS path, DDS hash, and `advisor_or_dossier_consumer=null`. |
| Runtime DDS | **PASS** | `gfx/leaders/006_independence_wave/portrait_HAW_independence_wave_territorial_delegate.dds` exists with SHA-256 `ef68feef243e6758e15df13c35420a33b38f060b6016dc25e20c8a30c229e37b`, 156x210 dimensions, 128-byte legacy BGRA header, 32-bit RGBA masks, `DDSCAPS_TEXTURE`, exact length `131168`, and opaque alpha `(255,255)`. The hash matches metadata. |
| GFX sprite path | **PASS** | `interface/006_independence_wave_pacific_portraits.gfx:17-18` defines `GFX_portrait_HAW_independence_wave_territorial_delegate` with the exact DDS texture path. |
| HAW character consumer | **PASS** | `common/characters/006_independence_wave_pacific_characters.txt:34-41` defines male `HAW_independence_wave_territorial_delegate` with only `portraits.civilian.large = GFX_portrait_HAW_independence_wave_territorial_delegate`. No durable queue path is referenced by runtime files. |
| Advisor/small-art boundary | **PASS** | Targeted package and runtime searches found no advisor, dossier, `_small`, 65x67, commander, or operative art/consumer for this HAW delegate. The package metadata remains `advisor_or_dossier_consumer=null`; only a full-size civilian leader portrait is wired. |

## Documentation note

The runtime files and metadata are aligned, but the temporary `manifest.md` and `gfx_handoff.md` still contain earlier evidence-only wording such as “no DDS” and “no runtime sprite is registered.” That is a stale documentation surface after the parent-owned runtime promotion and should be reconciled by the parent documentation pass. It does not invalidate the verified basename, hash, DDS, GFX, or character wiring.

**Simplifications, omissions, and blockers:** No visual substitution or runtime edit was made by this audit. Durable pair alignment, DDS/GFX/character wiring, and no-advisor-art checks pass. The remaining action is documentation reconciliation; live in-game validation remains parent/user-owned.
