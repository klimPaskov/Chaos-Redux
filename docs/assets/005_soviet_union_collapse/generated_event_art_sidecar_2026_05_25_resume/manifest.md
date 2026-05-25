# Event 005 Generated Event Art Resume Sidecar

Audit date: 2026-05-25

Scope: bounded generated-event-art sidecar for Event 005 Soviet Collapse fictional leader/council portraits and user-reported fictional flag problems. This pass did not edit gameplay, localisation, interface `.gfx`, GUI, focus, decision, event, history, country, spreadsheet, active `gfx/flags/**`, or active `gfx/leaders/**` files.

## References inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- Existing Event 005 leader portraits in `gfx/leaders/005_soviet_collapse/`
- Existing Event 005 flags in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`
- Vanilla HOI4 leader portrait folders under `/home/klim/projects/Hearts of Iron IV/gfx/leaders/`
- Prior Event 005 asset handoffs:
  - `docs/assets/005_soviet_union_collapse/generated_asset_handoff_2026_05_25/manifest.md`
  - `docs/assets/005_soviet_union_collapse/generated_asset_handoff_2026_05_25_followup/generated_asset_handoff.md`
  - `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_25_current/manifest.md`
  - `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_ukr_black_banner_ideology_variants/manifest.md`
  - `docs/assets/005_soviet_union_collapse/remaining_custom_flag_correction/manifest.md`

The required offline HOI4 wiki core pages were consulted for repository compliance. This sidecar did not change script syntax.

## Current-state audit

- Current Event 005 leader DDS files in `gfx/leaders/005_soviet_collapse/`: `47`.
- Leader portrait dimensions checked with ImageMagick: all current `*_leader.dds` files are `156x210`.
- Current named problem flag families checked in normal size: `PRA`, `MFR`, `OGB`, and `UKR_BLACK_BANNER`.
- Current named problem flag normal dimensions: all checked normal TGAs are `82x52`.
- Current named problem flag hashes: no duplicate hashes within the checked normal-size `PRA`, `MFR`, `OGB`, or `UKR_BLACK_BANNER` families.
- Matching normal, medium, and small TGA files exist for `PRA`, `MFR`, `OGB`, `UKR_BLACK_BANNER`, `BEC`, `BLT`, `COU`, `ILU`, and `IRA`.
- Active flag files are dirty in the worktree from prior/user work. No active replacement was attempted.

## Files created by this sidecar

| File | Purpose | Status |
| --- | --- | --- |
| `contact_sheets/reported_flag_problem_families_normal.png` | Current normal-size contact sheet for `PRA`, `MFR`, `OGB`, and `UKR_BLACK_BANNER` base/ideology flags. | created |
| `contact_sheets/fictional_portrait_resume_candidates.png` | Current portrait contact sheet for stale/uncertain portrait candidates plus `PRA`, `MFR`, and `OGB`. | created |
| `contact_sheets/flag_reference_samples.png` | Contact sheet of the inspected flag reference folder samples. | created |
| `manifest.md` | This audit and production handoff manifest. | created |
| `gfx_handoff.md` | Parent-facing output path and wiring handoff. | created |

No generated source PNG, processed replacement PNG, DDS, or TGA replacement was created in this resume pass.

## Portraits still needing regeneration

Deterministic required portrait regeneration: **none**.

Current active/generated-fictional portrait coverage exists on disk for the inspected Event 005 leader surface, including `BEC`, `BLT`, `COU`, `ILU`, and `IRA`. The earlier stale/deleted warning should be treated as superseded by the current on-disk state unless the parent knows those files are slated for removal.

Approval-gated portrait redesign only:

| Tag | Intended role if regenerated | Current active path | Required generated output paths if parent explicitly requests redesign | Source-mode prompt guidance | Status |
| --- | --- | --- | --- | --- | --- |
| `BEC` | fictional emergency council portrait | `gfx/leaders/005_soviet_collapse/BEC_leader.dds` | source `source_png/BEC_leader_source.png`; preview `processed_png/BEC_leader.png`; final `gfx/leaders/005_soviet_collapse/BEC_leader.dds`; sprite `GFX_portrait_BEC_emergency_council` | HOI4 156x210 fictional collective council portrait, one readable central chair with subdued advisers, 1936-1945 clothing, subdued painterly leader style, no text or real-person likeness. | not needed unless redesigned |
| `BLT` | fictional emergency council portrait | `gfx/leaders/005_soviet_collapse/BLT_leader.dds` | source `source_png/BLT_leader_source.png`; preview `processed_png/BLT_leader.png`; final `gfx/leaders/005_soviet_collapse/BLT_leader.dds`; sprite `GFX_portrait_BLT_emergency_council` | HOI4 156x210 fictional Central Asian council chair, late-1930s/early-1940s borderland administrative clothing, readable face, no text or modern props. | not needed unless redesigned |
| `COU` | fictional mountain republican council portrait | `gfx/leaders/005_soviet_collapse/COU_leader.dds` | source `source_png/COU_leader_source.png`; preview `processed_png/COU_leader.png`; final `gfx/leaders/005_soviet_collapse/COU_leader.dds`; sprite `GFX_portrait_COU_mountain_republican_council` | HOI4 156x210 fictional mountain council official, heavy period coat, restrained advisers, clear central subject, no labels or real likeness. | not needed unless redesigned |
| `ILU` | fictional desert-route authority portrait | `gfx/leaders/005_soviet_collapse/ILU_leader.dds` | source `source_png/ILU_leader_source.png`; preview `processed_png/ILU_leader.png`; final `gfx/leaders/005_soviet_collapse/ILU_leader.dds`; sprite `GFX_portrait_ILU_desert_route_authority` | HOI4 156x210 fictional desert-route authority chair, Central Asian civilian clothing under Soviet-era coat, subdued painterly finish, no text. | not needed unless redesigned |
| `IRA` | fictional Far Eastern provisional council portrait | `gfx/leaders/005_soviet_collapse/IRA_leader.dds` | source `source_png/IRA_leader_source.png`; preview `processed_png/IRA_leader.png`; final `gfx/leaders/005_soviet_collapse/IRA_leader.dds`; sprite `GFX_portrait_IRA_far_eastern_provisional_council` | HOI4 156x210 fictional railway-and-port provisional council official, worn winter greatcoat, period dispatch-room mood, no readable maps or text. | not needed unless redesigned |

## Flags still needing regeneration

Deterministic required flag regeneration: **none**. No checked active flag family is missing files, the named current normal-size files decode at `82x52`, and the checked normal-size problem families are not byte-identical within their family.

The following are the exact unresolved production candidates from prior user-reported flag issues and sidecar notes:

| Target | Intended role | Current state | Required output paths if parent approves regeneration | Orientation checks | Source-mode prompt guidance | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `PRA` | custom fictional base flag | Existing normal/medium/small TGAs; prior handoff calls the family visually simplest/geometric, not missing. | `gfx/flags/PRA.tga`, `gfx/flags/medium/PRA.tga`, `gfx/flags/small/PRA.tga`; sidecar source `source_png/PRA_source.png`; previews `processed_png/PRA_<normal|medium|small>.png`; contact sheet required. | Normal `82x52`, medium `41x26`, small `10x7`; visually upright in contact sheet; TGA should be 32-bit, bottom-left origin/descriptor `8`. | Generate intentional fictional Prisoner/Provisional authority flag art with bold field geometry and one simple emblem readable at 10x7; avoid text, letters, real extremist symbols, and simple recolors. | approval-gated visual redo |
| `PRA_communism` | custom fictional ideology flag | Existing normal/medium/small TGAs; visual redo only. | `gfx/flags/PRA_communism.tga`, `gfx/flags/medium/PRA_communism.tga`, `gfx/flags/small/PRA_communism.tga`; source `source_png/PRA_communism_source.png`; previews `processed_png/PRA_communism_<normal|medium|small>.png`. | Same as `PRA`. | Distinct worker-council/prisoner-committee motif, not a recolor of base, no hammer-and-sickle unless explicitly approved. | approval-gated visual redo |
| `PRA_democratic` | custom fictional ideology flag | Existing normal/medium/small TGAs; visual redo only. | `gfx/flags/PRA_democratic.tga`, `gfx/flags/medium/PRA_democratic.tga`, `gfx/flags/small/PRA_democratic.tga`; source `source_png/PRA_democratic_source.png`; previews `processed_png/PRA_democratic_<normal|medium|small>.png`. | Same as `PRA`. | Distinct civic assembly/legal-restoration motif, no readable text, no copied real flag layout. | approval-gated visual redo |
| `PRA_fascism` | custom fictional ideology flag | Existing normal/medium/small TGAs; visual redo only. | `gfx/flags/PRA_fascism.tga`, `gfx/flags/medium/PRA_fascism.tga`, `gfx/flags/small/PRA_fascism.tga`; source `source_png/PRA_fascism_source.png`; previews `processed_png/PRA_fascism_<normal|medium|small>.png`. | Same as `PRA`. | Distinct authoritarian camp-guard/command emblem, no swastikas, SS runes, fasces copying, or real extremist marks. | approval-gated visual redo |
| `PRA_neutrality` | custom fictional ideology flag | Existing normal/medium/small TGAs; visual redo only. | `gfx/flags/PRA_neutrality.tga`, `gfx/flags/medium/PRA_neutrality.tga`, `gfx/flags/small/PRA_neutrality.tga`; source `source_png/PRA_neutrality_source.png`; previews `processed_png/PRA_neutrality_<normal|medium|small>.png`. | Same as `PRA`. | Distinct provisional-security/stockade-field motif, calm muted palette, readable at 10x7. | approval-gated visual redo |
| `MFR_democratic` | factory-state fictional ideology flag | Existing normal/medium/small TGAs; prior handoff calls this blocky versus stronger base art. | `gfx/flags/MFR_democratic.tga`, `gfx/flags/medium/MFR_democratic.tga`, `gfx/flags/small/MFR_democratic.tga`; source `source_png/MFR_democratic_source.png`; previews `processed_png/MFR_democratic_<normal|medium|small>.png`. | Same flag size/origin checks as above. | Generated factory-republic civic flag with industrial cog/ledger/assembly motif, distinct from base and other ideology variants, no text. | approval-gated polish |
| `MFR_fascism` | factory-state fictional ideology flag | Existing normal/medium/small TGAs; visual polish only. | `gfx/flags/MFR_fascism.tga`, `gfx/flags/medium/MFR_fascism.tga`, `gfx/flags/small/MFR_fascism.tga`; source `source_png/MFR_fascism_source.png`; previews `processed_png/MFR_fascism_<normal|medium|small>.png`. | Same flag size/origin checks as above. | Generated militarized factory-directorate flag, angular industrial emblem, no real extremist symbols. | approval-gated polish |
| `MFR_neutrality` | factory-state fictional ideology flag | Existing normal/medium/small TGAs; visual polish only. | `gfx/flags/MFR_neutrality.tga`, `gfx/flags/medium/MFR_neutrality.tga`, `gfx/flags/small/MFR_neutrality.tga`; source `source_png/MFR_neutrality_source.png`; previews `processed_png/MFR_neutrality_<normal|medium|small>.png`. | Same flag size/origin checks as above. | Generated neutral factory-board flag with workshop shield/rail-industry motif, muted palette, no text. | approval-gated polish |
| `UKR_BLACK_BANNER_communism`, `_democratic`, `_fascism`, `_neutrality` | fictional Ukrainian black-banner route ideology flags | Active TGAs exist and a sidecar package exists, but prior audit noted source coverage may be a combined strip rather than clean per-variant source files. | Prefer source repair in `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_ukr_black_banner_ideology_variants/source_png/`; only regenerate if source strip cannot satisfy provenance. Active paths are `gfx/flags/UKR_BLACK_BANNER_<ideology>.tga`, `gfx/flags/medium/...`, `gfx/flags/small/...`. | If re-exported or regenerated: check upright normal/medium/small previews and TGA descriptor `8`; preserve no-suffix `UKR_BLACK_BANNER.tga` unless explicitly scoped. | If regeneration is required, make four distinct black-banner route ideology flags with Ukrainian agrarian/committee/field motifs; no default `UKR` override, no text, no real extremist symbols. | source repair preferred; regeneration only if needed |
| `OGB_democratic`, `OGB_fascism`, `OGB_neutrality` | OGB fictional ideology route flags | Existing files exist and prior notes say repository-preferred/restored OGB set should be preserved. | Do not create replacements without explicit parent approval. If approved: `gfx/flags/OGB_<ideology>.tga`, `gfx/flags/medium/OGB_<ideology>.tga`, `gfx/flags/small/OGB_<ideology>.tga`; source/previews under the approved sidecar. | Same flag size/origin checks as above. | Only if approved: distinct fictional OGB route ideology designs, not simple variants, while preserving the restored base identity. | blocked pending explicit approval |

## Preservation rules for the parent

- Do not create or overwrite default no-suffix base flags for vanilla-supported/current-country tags such as `SOV`, `RUS`, `UKR`, `BLR`, `KAZ`, `MOL`, `UZB`, `TAJ`, `TMS`, or `FER`.
- Existing-country route changes should remain explicit cosmetic/route flag tags, such as `UKR_BLACK_BANNER`.
- Do not make ideology variants by applying a color filter, flipping an asset, copying one emblem, adding one basic shape, or using byte-identical files.
- Do not overwrite active dirty `gfx/flags/**` or `gfx/leaders/**` files from this sidecar without a parent-approved replacement pass.

## Blockers and uncertainty

- The named flag visual issues are design-quality calls, not deterministic missing-file blockers from this audit.
- Active flag files are already dirty in the worktree, so this sidecar only produced contact sheets and documentation.
- No Photoshop processing was needed because no report-event image or final portrait replacement was produced.
- No Git commit was created because this is a bounded sidecar handoff in an already dirty parent worktree.
