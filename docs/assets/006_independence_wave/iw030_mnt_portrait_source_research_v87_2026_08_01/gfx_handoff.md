# IW-030 Montenegro sourced portrait handoff v87

## Parent-owned wiring boundary

No `.gfx`, character, history, localisation, event, or gameplay file was edited. No final DDS path or sprite name is assigned in this source-research tranche. The selected Mitar Martinovic crop is an immutable identity source only; it is not a runtime texture and must not be used raw or merely resized.

## Candidate handoff

| Potential consumer | Source evidence | Proposed runtime sprite/path | Status |
| --- | --- | --- | --- |
| Explicit roster replacement for the blocked Popovic slot, only after a design decision | `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/source_masters/mnt_mitar_martinovic_1912_chronicle.jpg`; exact crop `source_crops/mnt_mitar_martinovic_1912_head_shoulders.png`; equality JSON `crop_metadata/mnt_mitar_martinovic_1912_crop.json` | None assigned. Parent must create or approve a stable character identity and then run the full sourced-real-person pipeline (source-locked repaint, deterministic 156x210 candidate, independent audit, DDS, and `.gfx` wiring). | `sourced_needs_parent_role_admission` |
| `MNT_blazo_jovanovic` | Existing v68 source/crop/repaint evidence under `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v68_2026_08_01/` | Preserve `GFX_portrait_Blazo_Jovanovic` until parent resolves rights/provenance; no path proposed here. | `needs_user_review` |
| `MNT_blazo_dukanovic` | Existing v68 source/crop/repaint evidence under `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v68_2026_08_01/` | Preserve `GFX_portrait_MNT_blazo_dukanovic` until parent resolves rights/provenance; no path proposed here. | `needs_user_review` |
| `MNT_kristo_popovic` | No defensible source; v68 Commons/Montenegrina leads remain blocked | Keep `GFX_portrait_europe_generic_land_19` blocked or redesign the identity explicitly. Do not substitute Martinovic under the Popovic name. | `blocked_provenance` |

## Suggested next step

If the parent accepts Mitar Martinovic as an explicit role-correct roster replacement, the parent should add a design amendment naming the subject/key, update the character/localisation consumers, and then request the full real-person portrait pipeline. Until that decision, all v87 files are source evidence and review artifacts only.
