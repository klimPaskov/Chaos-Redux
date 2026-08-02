# Event 016 serialized project-stage index loader follow-up

Date: 2026-08-02

Status: implemented in the working tree and ready for parent commit.

## Scope

The Clausewitz array-scope form `var = brilliant_scientist_project_stage_entries^@index_macro` is not accepted reliably by the loader in the focused Kruger State and project-force consumers. The affected checks now use the fixed serialized Event 016 stage-array positions directly while retaining the named `@` index declarations as the documented crosswalk.

## Changed source surfaces

- `common/scripted_effects/016_brilliant_scientist_focus_effects.txt`: Singularity doctrine commit uses stage index `14`.
- `common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt`: high-energy uses `4`, rocketry uses `3`, and Singularity uses `14`.
- `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt`: teleportation `6`, cloning `7`, robotics `8`, paleogenetics `9`, xenobiological synthesis `10`, biological weapons `11`, alien arms `12`, and temporal `13`.

These are array positions, not project-family IDs. The named file-local declarations remain the readable crosswalk; the literal is used only at the loader-sensitive caret path.

## Validation evidence

- The changed files contain no remaining `^@` array paths.
- Every replacement matches its local declaration and the canonical Event 016 stage ledger order.
- The source files have balanced braces and no unsupported comparison operators.
- No focus prerequisite, route reward, project history, event, localisation, asset, or model contract changed.

## Remaining risks

The broader Event 016 foreign-trigger file retains its existing named index paths because that surface has a separate accepted loader contract and was not part of this focused correction. No game launch or save-state validation was run.
