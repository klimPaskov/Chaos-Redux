# IW-030 Montenegro portrait source handoff v53

## Runtime boundary

No `.gfx`, character, event, history, localisation, or gameplay file was edited. Raw source-locked HOI4 repaints and deterministic 156x210 evidence candidates exist, and the independent visual audit passes identity, male framing, artifacts, and HOI4 style; source/crop linkage and rights remain review-pending. No final DDS exists and no runtime texture may point at this temporary evidence folder.

## Parent-owned sprite contracts

| Character | Existing vanilla sprite | Proposed source candidate | Final DDS path | Status |
| --- | --- | --- | --- | --- |
| `MNT_blazo_jovanovic` | `GFX_portrait_Blazo_Jovanovic` | `source_crops/mnt_blazo_jovanovic_livno_1942_head_shoulders.png` | Raw repaint: `portraits_generated_png/portrait_MNT_blazo_jovanovic_hoi4_master.png`; evidence candidate: `processed_candidates/portrait_MNT_blazo_jovanovic_156x210_candidate.png`. Parent must preserve the existing engine-facing texture contract or explicitly choose a stable IW-030 DDS path under `gfx/leaders/006_independence_wave/`; no path is assigned here. | `visual_pass_needs_provenance_review` |
| `MNT_blazo_dukanovic` | `GFX_portrait_MNT_blazo_dukanovic` | `source_crops/mnt_blazo_dukanovic_1938_1940_head_shoulders.png` | Raw repaint: `portraits_generated_png/portrait_MNT_blazo_dukanovic_hoi4_master.png`; evidence candidate: `processed_candidates/portrait_MNT_blazo_dukanovic_156x210_candidate.png`. Parent must preserve the existing engine-facing texture contract or explicitly choose a stable IW-030 DDS path under `gfx/leaders/006_independence_wave/`; no path is assigned here. | `visual_pass_needs_rights_review` |
| `MNT_kristo_popovic` | `GFX_portrait_europe_generic_land_19` | No accepted source. The Commons Krsto Popović file is `blocked_provenance` because author/source/date are missing. | None. Do not substitute a generated or relabelled face. | `blocked` |

## Wiring notes

- The Jovanović source is the central subject in the explicitly captioned 1942 Livno group. The exact crop and equality proof are under `source_crops/` and `crop_metadata/`.
- The Đukanović source is a single male military portrait estimated 1938–1940. Commons asserts `PD-old`, but the unknown photographer/book-reproduction chain still requires an independent rights review.
- Neither source may be used raw or merely resized as runtime art. The source-lock record, prompts, repaint hashes, deterministic candidates, and independent visual audit are under `repaint_source_lock_2026_08_01.md`; rights/source linkage and the complete roster remain gates before DDS conversion.
- No advisor, high-command, `_small`, commander, operative, or female sprite is proposed.

## Evidence paths

- Manifest: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/manifest.md`.
- Contact sheet: `review/mnt_portrait_source_contact_sheet.png`.
- Jovanović master/crop: `source_masters/mnt_blazo_jovanovic_livno_1942.jpg`, `source_crops/mnt_blazo_jovanovic_livno_1942_head_shoulders.png`, `crop_metadata/mnt_blazo_jovanovic_livno_1942_crop.json`.
- Đukanović master/crop: `source_masters/mnt_blazo_dukanovic_1938_1940.jpg`, `source_crops/mnt_blazo_dukanovic_1938_1940_head_shoulders.png`, `crop_metadata/mnt_blazo_dukanovic_1938_1940_crop.json`.

## 2026-08-03 evidence-only source upgrade

The higher-resolution Savo Orović/Znaci Jovanović record is retained for a possible new repaint trial, not as a runtime sprite: `source_masters/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942.jpg`, `source_crops/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942_head_shoulders_v2.png`, and `crop_metadata/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942_crop_v2.json`.

The comparison sheet is `review/mnt_portrait_source_admission_contact_sheet_2026_08_03.png`.

No final DDS path or sprite name is proposed for this source until rights, source-locked repaint, independent visual audit, and the complete MNT roster gate pass.
## 2026-08-03 Znaci 8889 source-locked repaint trial

The existing `MNT_blazo_jovanovic` sprite contract is unchanged. A new source-locked repaint trial uses `source_masters/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942.jpg` and exact crop `[1040,500,1490,1200]`; the raw 1080x1456 repaint, 156x210 candidate, prompt, and native/4x review sheets are under this workspace. The original-size shelf copy is `docs/assets/006_independence_wave/portraits_generated_png/portrait_MNT_blazo_jovanovic_znaci_8889_hoi4_master.png` (reference-only).

| Consumer | Proposed candidate | Final DDS / sprite | Status |
| --- | --- | --- | --- |
| `MNT_blazo_jovanovic` | `processed_candidates/portrait_MNT_blazo_jovanovic_znaci_8889_156x210_candidate.png` | None assigned; preserve existing `GFX_portrait_Blazo_Jovanovic` contract if parent later admits the source | `needs_user_review`: parent review `PASS_visual_identity` + `PASS_hoi4_leader_style`; provenance/rights remain `NEEDS_USER_REVIEW` |

Parent-owned review record: `audit/mnt_blazo_jovanovic_znaci_8889_independent_review_2026_08_03.md`. Independent likeness/style review is complete, but the provenance/rights gate remains unresolved. Do not convert to DDS or edit `.gfx` until that gate and the complete MNT roster admission pass. No advisor, high-command, dossier, operative, small, commander, or female portrait is proposed.
