# Event 006 generic focus surface count reconciliation

Counting correction: the 23 `shared_focus = { ... }` overlay blocks in the main file are definitions, not import references. Therefore the authoritative source count is 184 direct definitions, 134 shared definitions, 27 simple import references, 318 unique definitions, and 345 raw entries.

Date: 2026-08-02

The current four-file Event 006 focus surface was counted directly from `common/national_focus/006_independence_wave*.txt` with a UTF-8 parser that distinguishes direct focus blocks, full shared-focus definitions, and shared-focus import roots.

| Surface | Count | Meaning |
| --- | ---: | --- |
| Direct `focus = { ... }` definitions | 184 | Nodes defined directly in `006_independence_wave_focus.txt`. |
| Full `shared_focus = { ... }` definitions | 134 | 23 overlay definitions in the main file plus 111 package or regional nodes defined in the IW-043/IW-058, IW-093/IW-098, and Pacific module files. |
| Main-tree `shared_focus = <id>` import roots | 27 | Root references in the generic tree; they are separate references and do not duplicate the 134 shared definitions. |
| Unique focus node definitions | 318 | 184 direct nodes plus 134 shared definitions. |
| Raw source entries including import roots | 345 | 184 direct blocks plus 134 shared blocks plus 27 import lines. |

The older v98 audit phrase “318 blocks (184 regular + 134 shared)” is retained as historical evidence for the prior import surface. It is not the current source count after later shared-focus root imports. The current source has no duplicate focus IDs, no unresolved shared-focus imports, and no unresolved prerequisite or relative-position references under this static count pass.

The current count treats all 134 `shared_focus = { ... }` blocks as definitions, including the 23 additive overlay definitions in the main file; the 27 simple `shared_focus = <id>` lines are the separate import references. This reconciliation changes documentation only. It does not add a focus tree, change package admission, alter route logic, or make a live/rendering claim. The current HOI4 focus inspection remains blocked by `SCAN_BYTE_LIMIT`.
