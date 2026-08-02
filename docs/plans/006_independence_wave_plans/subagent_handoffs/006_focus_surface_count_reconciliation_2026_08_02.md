# Event 006 generic focus surface count reconciliation

Date: 2026-08-02

The current four-file Event 006 focus surface was counted directly from `common/national_focus/006_independence_wave*.txt` with a UTF-8 parser that distinguishes direct focus blocks, full shared-focus definitions, and shared-focus import roots.

| Surface | Count | Meaning |
| --- | ---: | --- |
| Direct `focus = { ... }` definitions | 184 | Nodes defined directly in `006_independence_wave_focus.txt`. |
| Full `shared_focus = { ... }` definitions | 111 | Package or regional nodes defined in the IW-043/IW-058, IW-093/IW-098, and Pacific module files. |
| Main-tree `shared_focus = <id>` import roots | 50 | Root references in the generic tree; all resolve to the 111 shared definitions and do not duplicate node definitions. |
| Unique focus node definitions | 295 | 184 direct nodes plus 111 shared definitions. |
| Raw source entries including import roots | 345 | 184 direct blocks plus 111 shared blocks plus 50 import lines. |

The older v98 audit phrase “318 blocks (184 regular + 134 shared)” is retained as historical evidence for the prior import surface. It is not the current source count after later shared-focus root imports. The current source has no duplicate focus IDs, no unresolved shared-focus imports, and no unresolved prerequisite or relative-position references under this static count pass.

This reconciliation changes documentation only. It does not add a focus tree, change package admission, alter route logic, or make a live/rendering claim. The current HOI4 focus inspection remains blocked by `SCAN_BYTE_LIMIT`.
