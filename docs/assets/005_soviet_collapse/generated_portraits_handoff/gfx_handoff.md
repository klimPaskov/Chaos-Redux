# Event 005 Soviet Collapse Generated Portrait GFX Handoff

Scope: leader/council portrait assets only. No `.gfx` file was edited.

## Final DDS Handoff Files

The generated DDS files are staged under:

```text
docs/assets/005_soviet_collapse/generated_portraits_handoff/final_dds/
```

Copy into the target final paths only when the main agent confirms the deleted dirty paths should be restored:

| Handoff DDS | Target final path | Proposed sprite |
| --- | --- | --- |
| `final_dds/BEC_leader.dds` | `gfx/leaders/005_soviet_collapse/BEC_leader.dds` | `GFX_portrait_BEC_emergency_council` |
| `final_dds/BLT_leader.dds` | `gfx/leaders/005_soviet_collapse/BLT_leader.dds` | `GFX_portrait_BLT_emergency_council` |
| `final_dds/COU_leader.dds` | `gfx/leaders/005_soviet_collapse/COU_leader.dds` | `GFX_portrait_COU_mountain_republican_council` |
| `final_dds/ILU_leader.dds` | `gfx/leaders/005_soviet_collapse/ILU_leader.dds` | `GFX_portrait_ILU_desert_route_authority` |
| `final_dds/IRA_leader.dds` | `gfx/leaders/005_soviet_collapse/IRA_leader.dds` | `GFX_portrait_IRA_far_eastern_provisional_council` |

## Suggested GFX File

Use `interface/005_soviet_collapse_custom_icons.gfx` if these portraits become active. That file already owns most Event 005 custom council portrait sprite definitions.

Suggested entries, if restored:

```hoi4
spriteType = { name = "GFX_portrait_BEC_emergency_council" texturefile = "gfx/leaders/005_soviet_collapse/BEC_leader.dds" }
spriteType = { name = "GFX_portrait_BLT_emergency_council" texturefile = "gfx/leaders/005_soviet_collapse/BLT_leader.dds" }
spriteType = { name = "GFX_portrait_COU_mountain_republican_council" texturefile = "gfx/leaders/005_soviet_collapse/COU_leader.dds" }
spriteType = { name = "GFX_portrait_ILU_desert_route_authority" texturefile = "gfx/leaders/005_soviet_collapse/ILU_leader.dds" }
spriteType = { name = "GFX_portrait_IRA_far_eastern_provisional_council" texturefile = "gfx/leaders/005_soviet_collapse/IRA_leader.dds" }
```

## Use Notes

- These are generated fictional or collective council portraits, not real-person likenesses.
- All processed previews and DDS files are 156x210.
- The generated contact sheet is `contact_sheets/generated_portraits_contact_sheet.png`.
- The reference contact sheet is `contact_sheets/reference_portrait_style_sheet.png`.
- Prior sidecars describe these tags as possibly inactive/stale. Use only if the main Event 005 implementation still needs these target paths.
