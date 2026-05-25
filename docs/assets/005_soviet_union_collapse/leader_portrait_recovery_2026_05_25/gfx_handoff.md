# Event 005 Leader Portrait Recovery Handoff

No `.gfx` files were edited.

## Final Portrait DDS Files

These final DDS files exist again at their stable paths:

| Asset | Final DDS | Proposed sprite name | Suggested `.gfx` file | Use notes |
| --- | --- | --- | --- | --- |
| `BEC_leader` | `gfx/leaders/005_soviet_collapse/BEC_leader.dds` | keep existing registered portrait sprite if reactivated | existing Event 005 custom/council portrait `.gfx` file | Fictional generated council portrait restored from tracked final asset. |
| `BLT_leader` | `gfx/leaders/005_soviet_collapse/BLT_leader.dds` | keep existing registered portrait sprite if reactivated | existing Event 005 custom/council portrait `.gfx` file | Fictional generated council portrait restored from tracked final asset. |
| `COU_leader` | `gfx/leaders/005_soviet_collapse/COU_leader.dds` | keep existing registered portrait sprite if reactivated | existing Event 005 custom/council portrait `.gfx` file | Fictional generated council portrait restored from tracked final asset. |
| `ILU_leader` | `gfx/leaders/005_soviet_collapse/ILU_leader.dds` | keep existing registered portrait sprite if reactivated | existing Event 005 custom/council portrait `.gfx` file | Fictional generated council portrait restored from tracked final asset. |
| `IRA_leader` | `gfx/leaders/005_soviet_collapse/IRA_leader.dds` | keep existing registered portrait sprite if reactivated | existing Event 005 custom/council portrait `.gfx` file | Fictional generated council portrait restored from tracked final asset. |

Source PNGs and processed previews are recorded in this package under `source_png/` and `processed_png/`.

## Flags

Country flags require no `.gfx` wiring. Event 005 generated/custom flag QA found all checked normal, medium, and small TGA files present at the expected sizes with bottom-left TGA origin. See `manifest.md` and `notes/event005_generated_flag_qa.json`.

## Use Notes

- No default no-suffix flags were created for vanilla-supported ordinary/internal tags.
- `UKR_BLACK_BANNER` remains the explicit route/cosmetic flag family for Ukraine's Black Banner route.
- DDS conversion remains blocked in `.tools/convert_to_dds.py`; no unapproved converter was used.
