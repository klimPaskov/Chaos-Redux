# Event 016 scientist-skill constant loader follow-up

Date: 2026-08-02

Status: implemented as a narrow loader-compatibility continuation.

## Scope

The `skills` block in `brilliant_scientist_add_kruger_roles` uses six specialization fields. Those static fields now consume a file-local `@CR_SC_BRILLIANT_SCIENTIST_VALUE_FIVE` macro instead of `constant:brilliant_scientist_value.five`, matching the supported static-field pattern used by vanilla special-project definitions.

## Changed file

- `common/scripted_effects/016_brilliant_scientist_effects.txt`
  - Declares `@CR_SC_BRILLIANT_SCIENTIST_VALUE_FIVE = 5`.
  - Applies it to nuclear, naval, air, land, biowarfare, and chemical-warfare scientist specializations.

## Validation evidence

- The six replacements are value-equivalent to `brilliant_scientist_value.five` in `common/script_constants/016_brilliant_scientist_constants.txt`.
- Vanilla special-project files use the same file-local macro form for specialization values.
- The source has balanced braces, no unsupported comparison operators, and no change to the Kruger role list, skill values, event flow, rewards, assets, or model contracts.
- This follow-up adds one macro definition and six static-field substitutions to the earlier 162-macro compatibility tranche; the earlier handoff's original counts remain historical for that tranche.

## Remaining risks

No in-game loader or save validation was run. This is a loader-safety repair only and does not close the user-owned live acceptance boundary.
