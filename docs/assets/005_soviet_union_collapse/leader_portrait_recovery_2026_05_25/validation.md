# Event 005 Leader Portrait Recovery Validation

## Portraits

Command:

```bash
identify gfx/leaders/005_soviet_collapse/BEC_leader.dds gfx/leaders/005_soviet_collapse/BLT_leader.dds gfx/leaders/005_soviet_collapse/COU_leader.dds gfx/leaders/005_soviet_collapse/ILU_leader.dds gfx/leaders/005_soviet_collapse/IRA_leader.dds
```

Result: all five final DDS files identify as `156x210` DDS images.

Contact sheet:

- `contact_sheets/recovered_leader_portraits.png`

## Flags

Audit command: local Python TGA-header audit over 33 Event 005 generated/custom flag families, each with base, `communism`, `democratic`, `fascism`, and `neutrality` variants in normal, medium, and small folders.

Results:

- Rows checked: `165`.
- Files expected and present: `495`.
- Missing files: `0`.
- Dimension mismatches: `0`.
- Byte-identical variant groups: `0`.
- Existing vanilla-supported default flag overrides found: `0`.
- Normal dimensions: `82x52`.
- Medium dimensions: `41x26`.
- Small dimensions: `10x7`.
- TGA origin: bottom-left for every checked file (`origin_top = false`).

Detailed audit:

- `notes/event005_generated_flag_qa.json`

Contact sheets:

- `contact_sheets/event005_generated_flags_normal_qa.png`
- `contact_sheets/event005_generated_flags_medium_qa.png`
- `contact_sheets/event005_generated_flags_small_qa.png`

## DDS Converter Blocker

Direct executable command failed with:

```text
/usr/bin/env: 'python3\r': No such file or directory
```

Python invocation of the existing converter failed with:

```text
struct.error: pack expected 34 items for packing (got 32)
```

No alternate DDS converter was used.
