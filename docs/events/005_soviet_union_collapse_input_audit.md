# Soviet Union Collapse Input Audit

This audit records the source files available for the current Event 005 correction pass and the named inputs that are missing from `tmp/`.

## Requested Inputs

| Requested input | State | Lines | Bytes | SHA-256 |
| --- | --- | ---: | ---: | --- |
| `tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md` | present | 287 | 15899 | `9ac9d2553dffc54b6023c56f2dbde6efac310343b20873c77b1f50e6e5339750` |
| `tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md` | missing | 0 | 0 | n/a |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md` | present | 3418 | 162378 | `c0f474e97482a4eed3d4f9b8cbead930471f296d741e9805a0fea03b38e685e7` |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md` | present | 6327 | 191503 | `32284c8e2f424818be5dfbb81c394d9c1de7e666a93545586a1e2e1710276234` |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md` | present | 7535 | 554089 | `724a3bfb7c00aa28debf788649413da311224044fe4b0f4f8f726ee345275de7` |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md` | present | 3889 | 148956 | `60e2cac0717579afc60a3a6414558c00122d3fbae7d4e205af27671f7d6bc428` |
| `tmp/error.log` | intentionally removed after fixed errors | 0 | 0 | n/a |
| `tmp/text.log` | intentionally removed after fixed errors | 0 | 0 | n/a |
| `AGENTS.md` | present | 287 | 19327 | `91da11f4d513562415356c9f52acc8bca3f9b3698eafb3d63b5b40c182d881eb` |
| `.agents/skills/chaos-redux-events/SKILL.md` | present | 527 | 34724 | `1e044b9357ea3eb466d259c9545d82fad4f8b0d998eed352504df8f920326661` |
| `.agents/skills/chaos-redux-event-assets/SKILL.md` | present | 772 | 31044 | `9460971e44770723ffa650385907f1868dc3e893fb7204ddf0c096050efa1d96` |
| `.agents/skills/chaos-redux-super-events/SKILL.md` | present | 756 | 25696 | `e1dcb0adafb186ace5e054a22576153ee3686f901864fbfd9ec98f8cd0b8212f` |

## Recovery Search

The exact requested file `tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md` was not present. The Soviet-collapse files found in `tmp/` were:

- `005_soviet_union_collapse_comprehensive_correction_spec.md`
- `005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md`
- `005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md`
- `005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md`
- `005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md`
- `005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md`

`tmp/005_soviet_union_collapse_comprehensive_correction_spec.md` contains the event-log, mission-duration, blocked-localisation, threat-balance, Moscow Authority, strong-ideas, release-logic, Union Unmade, flag, and completion-gate cleanup themes that overlap with the missing filename. It is treated as recovered adjacent context, not as proof that the exact requested input exists.

The exact requested log files `tmp/error.log` and `tmp/text.log` were not present. On 2026-05-18 the user clarified that the previous errors had already been fixed and those log files were removed intentionally, so their absence is no longer a completion blocker. The latest recovery search was:

```text
find . -path './.git' -prune -o -type f \( -iname 'error.log' -o -iname 'text.log' -o -iname '*event_log*mission*balance*focus*cleanup*' -o -iname '*mission_balance_focus*' -o -iname '*005*soviet*collapse*log*' \) -printf '%p %s bytes\n' | sort
result: ./interface/005_soviet_collapse_faction_logos.gfx 17832 bytes
```

The one returned file is an unrelated faction-logo GFX file whose name contains `log`; it is not a runtime log or continuation spec.

2026-05-18 exact-name recheck:

```text
find . -type f \( -name '005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md' -o -name 'error.log' -o -name 'text.log' \) -printf '%p %s bytes\n' | sort
result: no files found
```

2026-05-18 repository near-name and history recheck:

```text
find . -path './.git' -prune -o -type f \( -iname '005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md' -o -iname '*event_log*mission*balance*focus*cleanup*' -o -iname '*mission_balance_focus*' -o -iname '*focus_cleanup*spec.md' \) -printf '%p %s bytes\n' | sort
result: no files found

git log --all --name-only --pretty=format: | rg '005_soviet_union_collapse.*(event_log|mission_balance|focus_cleanup|event_log_mission_balance_focus_cleanup).*spec\.md' | sort -u
result: no matching tracked history entry
```

2026-05-18 home-directory exact-name recheck:

```text
find /home/klim -path /home/klim/.cache -prune -o -path /home/klim/.local/share/Trash -prune -o -type f \( -name '005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md' -o -name 'error.log' -o -name 'text.log' \) -printf '%p %s bytes\n' 2>/dev/null | sort
result: /home/klim/.npm/_npx/c31bc0d65f54f6ef/node_modules/@cyanheads/git-mcp-server/logs/error.log 0 bytes
```

The `/home/klim` hit is an unrelated zero-byte npm package log outside the Chaos Redux repository. It is not the requested `tmp/error.log` runtime evidence.

## Completion Impact

The current pass can continue from the available source-of-truth files, especially `tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md`. Final completion cannot be claimed from inputs alone while the exact named event-log/mission-balance/focus-cleanup spec remains absent; the final audit must either recover that exact file, explicitly waive it, or verify every requirement it would have covered against implementation evidence. The intentionally removed `tmp/error.log` and `tmp/text.log` files are not blockers after the user's 2026-05-18 clarification.
