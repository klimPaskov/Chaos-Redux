# Event 005 Leader Portrait Recovery And Flag QA

Date: 2026-05-25

Scope: generated fictional/council leader portrait recovery and Event 005 generated/custom flag QA. No gameplay, script, localisation, `.gfx`, GUI, history, country, focus, decision, or spreadsheet files were edited.

## References Inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `docs/assets/005_soviet_union_collapse/contact_sheets/custom_country_leaders_labeled.png`
- `docs/assets/005_soviet_union_collapse/contact_sheets/event005_generated_replacement_leaders.png`
- `docs/assets/005_soviet_union_collapse/gfx_handoff.md`
- `docs/assets/005_soviet_union_collapse/manifest.md`

## Recovered Portrait Assets

Source mode: existing generated `$imagegen` Event 005 portrait source art. These are fictional/council portraits, not real leader likenesses.

The standard DDS converter is currently blocked for these files. The final DDS files were restored from the tracked repository version of the same final portrait assets, not converted through an alternate converter.

| Asset | Asset type | Source PNG | Processed PNG | Final DDS | Target size | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `BEC_leader` | fictional/council leader portrait | `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/source_png/BEC_leader_source.png` | `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/processed_png/BEC_leader.png` | `gfx/leaders/005_soviet_collapse/BEC_leader.dds` | 156x210 | final DDS restored |
| `BLT_leader` | fictional/council leader portrait | `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/source_png/BLT_leader_source.png` | `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/processed_png/BLT_leader.png` | `gfx/leaders/005_soviet_collapse/BLT_leader.dds` | 156x210 | final DDS restored |
| `COU_leader` | fictional/council leader portrait | `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/source_png/COU_leader_source.png` | `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/processed_png/COU_leader.png` | `gfx/leaders/005_soviet_collapse/COU_leader.dds` | 156x210 | final DDS restored |
| `ILU_leader` | fictional/council leader portrait | `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/source_png/ILU_leader_source.png` | `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/processed_png/ILU_leader.png` | `gfx/leaders/005_soviet_collapse/ILU_leader.dds` | 156x210 | final DDS restored |
| `IRA_leader` | fictional/council leader portrait | `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/source_png/IRA_leader_source.png` | `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/processed_png/IRA_leader.png` | `gfx/leaders/005_soviet_collapse/IRA_leader.dds` | 156x210 | final DDS restored |

Contact sheet: `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/contact_sheets/recovered_leader_portraits.png`.

## DDS Conversion Blocker

Attempted command:

```bash
env -u TEXCONV_EXE -u TEXCONV_PATH -u TEXCONV_DOCKER_IMAGE python3 .tools/convert_to_dds.py --input docs/assets/005_soviet_union_collapse/processed_png/BEC_leader.png --output gfx/leaders/005_soviet_collapse/BEC_leader.dds --width 156 --height 210
```

Error:

```text
struct.error: pack expected 34 items for packing (got 32)
```

The executable form is also blocked by the file's CRLF shebang:

```text
/usr/bin/env: 'python3\r': No such file or directory
```

No unapproved converter was used.

## Flag QA

Checked generated/custom Event 005 flag families:

`CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN`, `KRS`, `FTH`, `BBH`, `BSC`, `RMC`, `DSC`, `NRF`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `PRA`, `TSC`, `ICD`, `ARD`, `NLC`, and `UKR_BLACK_BANNER`.

Results:

- `165` base/ideology flag rows checked.
- `495` TGA files expected and present.
- Normal flags are `82x52`.
- Medium flags are `41x26`.
- Small flags are `10x7`.
- Every present checked TGA has bottom-left origin (`origin_top = false`).
- Normal and medium flags are 32-bit truecolor TGA with descriptor `8`.
- Small flags are mixed: `115` are 32-bit truecolor descriptor `8`; `50` are palette-encoded 8bpp descriptor `0`.
- No byte-identical base/ideology variant groups were found within any checked family.
- No default flag overrides were found for vanilla-supported ordinary/internal tags (`UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, `TAN`).

Machine-readable audit: `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/notes/event005_generated_flag_qa.json`.

Contact sheets:

- `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/contact_sheets/event005_generated_flags_normal_qa.png`
- `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/contact_sheets/event005_generated_flags_medium_qa.png`
- `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/contact_sheets/event005_generated_flags_small_qa.png`

## Blockers

- The standard repo DDS converter cannot currently produce new DDS files through its local fallback because `.tools/convert_to_dds.py` raises `struct.error: pack expected 34 items for packing (got 32)`.
- The converter script's executable shebang is CRLF-tainted and fails when called directly.
- The restored leader DDS files are final tracked assets, but they were not regenerated in this pass because conversion is blocked.
