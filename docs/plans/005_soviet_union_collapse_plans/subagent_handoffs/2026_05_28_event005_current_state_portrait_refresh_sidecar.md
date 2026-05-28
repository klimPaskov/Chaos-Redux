# 2026-05-28 Event 005 Current-State Portrait Refresh Sidecar

## Scope

Bounded generated-asset pass for Event 005 Soviet Collapse. Limited to missing or weak fictional leader and council portraits or fictional ideology and route flags. No gameplay, localisation, `.gfx`, event, focus, decision, scripted effect, or scripted trigger files were edited.

## Files changed

- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/source/CFR_construction_board_council_source.png`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/source/CFR_construction_board_council_source_alt1.png`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/source/MFR_arsenal_board_council_source.png`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/source/MFR_arsenal_board_council_source_alt1.png`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/processed/CFR_leader.png`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/processed/MFR_leader.png`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/final_dds/CFR_leader.dds`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/final_dds/MFR_leader.dds`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/contact_sheets/event005_cfr_mfr_source_alternatives_contact.png`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/contact_sheets/event005_cfr_mfr_final_contact.png`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/prompts/generated_portrait_prompts.md`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/manifest.md`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/gfx_handoff.md`
- `gfx/leaders/005_soviet_collapse/CFR_leader.dds`
- `gfx/leaders/005_soviet_collapse/MFR_leader.dds`

## What was delivered

Two generated institutional portrait replacements:

1. `CFR_leader`
2. `MFR_leader`

Both prior portraits read as environmental building art rather than governing bodies. They were replaced with vertical HOI4-ready collective portraits that remain readable at `156x210`.

## Validation

- Inspected Event 005 clean docs and clean spec part 7 before asset work.
- Inspected the skill reference flag folder before reviewing flag scope.
- Reviewed current live portrait and flag contact sheets.
- Generated portrait-oriented source alternatives and retained the rejected wider compositions.
- Verified processed PNG dimensions: `156x210`.
- Verified final installed DDS dimensions:
  - `gfx/leaders/005_soviet_collapse/CFR_leader.dds`
  - `gfx/leaders/005_soviet_collapse/MFR_leader.dds`
- Verified installed DDS hashes match package DDS hashes.

## Gender and naming notes

- `CFR_leader` is a mixed-gender institutional council portrait. Use institutional naming only.
- `MFR_leader` is a mixed-gender institutional council portrait. Use institutional naming only.
- No one-person portrait was added in this pass, so no personal gendered name-pool requirement was introduced here.

## Remaining gaps

- No fictional ideology or route flag was replaced in this pass.
- The current bounded review did not isolate a single flag-art replacement that was clearly safer and higher value than the two portrait fixes without widening scope.
- Existing small-flag export/header inconsistencies from earlier audits remain a separate cleanup surface if the parent wants a flag-output pass later.
