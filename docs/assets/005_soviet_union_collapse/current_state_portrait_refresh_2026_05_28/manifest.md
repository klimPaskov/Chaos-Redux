# Event 005 Current-State Portrait Refresh Manifest

This bounded package refreshes the two weakest fictional collective leader portraits found during the current-state Event 005 review.

## Scope decision

- Included: `CFR_leader`, `MFR_leader`
- Excluded: fictional ideology and route flags
- Reason: current live review showed the clearest bounded gap was two building-only collective portraits that did not meet the current `leader or council surface` standard. No equally narrow flag-art replacement gap was isolated from the active docs without broadening scope.

## Assets

| asset | source mode | source path | processed png | final dds | target size | sprite name | use | status | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `CFR_leader` | generated | `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/source/CFR_construction_board_council_source.png` | `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/processed/CFR_leader.png` | `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/final_dds/CFR_leader.dds` | `156x210` | `GFX_portrait_CFR_construction_board` | Construction Board institutional leader portrait | complete | Replaces prior building-only surface with a readable three-member governing board. Institutional portrait, not a one-person leader. |
| `MFR_leader` | generated | `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/source/MFR_arsenal_board_council_source.png` | `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/processed/MFR_leader.png` | `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/final_dds/MFR_leader.dds` | `156x210` | `GFX_portrait_MFR_arsenal_board` | Arsenal Board institutional leader portrait | complete | Replaces prior factory-building surface with a readable three-member armaments board. Institutional portrait, not a one-person leader. |

## Alternative source renders retained

- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/source/CFR_construction_board_council_source_alt1.png`
- `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/source/MFR_arsenal_board_council_source_alt1.png`

These are preserved as rejected wider compositions. The selected portrait-oriented renders crop better to the HOI4 `156x210` leader surface.

## Institutional naming and gender handling

- `CFR_leader`: institutional collective portrait. Keep institutional leader naming. Do not assign a personal random name pool.
- `MFR_leader`: institutional collective portrait. Keep institutional leader naming. Do not assign a personal random name pool.

The selected portraits depict mixed-gender governing bodies rather than one person, so the one-person gender/name-pool rule does not apply to these two assets.

## Package review notes

- Contact sheet of rejected and selected source alternatives: `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/contact_sheets/event005_cfr_mfr_source_alternatives_contact.png`
- Contact sheet of final processed portraits: `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/contact_sheets/event005_cfr_mfr_final_contact.png`
- Prompt record: `docs/assets/005_soviet_union_collapse/current_state_portrait_refresh_2026_05_28/prompts/generated_portrait_prompts.md`

## Current blockers outside this bounded package

- No flag art was changed in this pass.
- Earlier flag audits still point to some small-flag export/header inconsistencies for multiple fictional tags. That is a separate final-output cleanup task, not a missing generated-art gap isolated by the current bounded review.
