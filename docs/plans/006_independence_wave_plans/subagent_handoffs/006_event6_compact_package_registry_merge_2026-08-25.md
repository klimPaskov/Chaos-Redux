# Event 006 compact package registry merge — 2026-08-25

## Scope

This is a source-layout-only consolidation for two groups of clean package trigger/effect pairs: Rhineland (IW-008), Bavaria (IW-009), and Saar (IW-010), plus Bashkiria (IW-045) and Mari (IW-047). No active working-tree package edit was absorbed.

## Receiver files

- `common/scripted_triggers/006_independence_wave_rhineland_bavaria_saar_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_rhineland_bavaria_saar_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_bashkiria_mari_package_effects.txt`

Each receiver keeps explicit `# SOURCE:` markers. Package-local identifiers, executable bodies, file-scoped effect constants, lifecycle gates, dispatch helpers, cleanup, and internal comments are preserved. Redundant per-file header banners are condensed.

## Removed parser files

- `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_saar_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`
- `common/scripted_effects/006_independence_wave_saar_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_bashkiria_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_mari_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt`
- `common/scripted_effects/006_independence_wave_mari_package_effects.txt`

## Audit evidence

- The Rhineland/Bavaria/Saar receiver has 32 unique top-level triggers and 100 unique top-level effects, with braces balanced at 173/173 and 654/654.
- The Bashkiria/Mari receiver has 32 unique top-level triggers and 66 unique top-level effects, with braces balanced at 171/171 and 419/419.
- Every former source executable-code sequence, including the RHI/BAY file-scoped constants, matches its receiver after line-ending normalization and comment/blank-line removal.
- The four receivers save 4,369 source bytes versus the eight former files, reducing the parser file count by four.
- No gameplay identifier, package gate, dispatcher, admission count, reservation, ledger, force profile, localisation key, or runtime behavior was changed.

Komi, Kosovo, Kuban, Ruthenia, Tatarstan, and Udmurtia remain separate because their current working-tree edits are owned by other work. Far Eastern, Kurdistan, and the other larger regional registries remain separate because this tranche is intentionally limited to the two clean compact groups.

No live parser, save/load, runtime, balance, admission, or gameplay completion claim is made. The merge changes file layout only.
