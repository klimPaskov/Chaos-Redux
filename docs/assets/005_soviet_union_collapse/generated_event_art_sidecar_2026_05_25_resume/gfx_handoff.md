# Event 005 Generated Event Art Resume Handoff

Scope: generated fictional portraits and fictional/custom flag problem handoff only. No `.gfx`, gameplay, localisation, history, country, focus, decision, event, spreadsheet, active flag, or active leader file was edited.

## Result

No active generated/fictional leader portrait or scoped flag family has a deterministic missing-file regeneration blocker in the current on-disk state.

Created review/contact outputs:

- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_25_resume/contact_sheets/reported_flag_problem_families_normal.png`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_25_resume/contact_sheets/fictional_portrait_resume_candidates.png`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_25_resume/contact_sheets/flag_reference_samples.png`

## Portrait handoff

No portrait sprite changes are proposed.

If the parent explicitly requests redesigns for `BEC`, `BLT`, `COU`, `ILU`, or `IRA`, use the existing sprite names and target DDS paths listed in `manifest.md`. Generated fictional portraits should be delivered as source PNG, 156x210 processed PNG preview, final DDS, and contact sheet before any active replacement.

## Flag handoff

HOI4 country/cosmetic flags do not need `.gfx` sprite entries.

Approval-gated flag production targets are:

- `PRA`, `PRA_communism`, `PRA_democratic`, `PRA_fascism`, `PRA_neutrality`
- `MFR_democratic`, `MFR_fascism`, `MFR_neutrality`
- `UKR_BLACK_BANNER_communism`, `UKR_BLACK_BANNER_democratic`, `UKR_BLACK_BANNER_fascism`, `UKR_BLACK_BANNER_neutrality` only if source re-export from the existing sidecar strip is insufficient
- `OGB_democratic`, `OGB_fascism`, `OGB_neutrality` only after explicit parent approval, because prior notes say the restored OGB set should be preserved

Required flag outputs for any approved replacement:

- Normal TGA: `gfx/flags/<TAG>.tga`, `82x52`
- Medium TGA: `gfx/flags/medium/<TAG>.tga`, `41x26`
- Small TGA: `gfx/flags/small/<TAG>.tga`, `10x7`
- Source PNG and processed PNG previews under the approved sidecar folder
- Contact sheet showing normal, medium, and small outputs upright

Use notes:

- Do not replace active dirty files without parent approval.
- Do not create default country flag overrides for existing vanilla-supported countries.
- Use generated source-mode only for the fictional/custom targets listed above; route historical or historically attested symbols to source research instead.
