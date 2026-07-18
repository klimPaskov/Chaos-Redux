# Muster Seal Pulse Frame Plan

| Frame | Atlas cell | Motion state | Authored visual change | Anchor | Loop note |
| --- | --- | --- | --- | --- | --- |
| 000 | row 1, column 1 | rest | Dented brass-and-wax muster seal, three stamped rank marks, closed paper fibers, lowest light | center | static fallback |
| 001 | row 1, column 2 | waking | Fresh wax fissure at lower edge; one stamped soldier mark rises; paper fibers begin to separate | center | ease in |
| 002 | row 1, column 3 | registering | Second impression appears in the wax; short brass ledger groove lights; different filing tab emerges | center | building |
| 003 | row 1, column 4 | unresolved | Several irregular rank impressions crowd the face; two new wax cracks and lifted paper corners | center | near peak |
| 004 | row 2, column 1 | peak | Seal face fully legible; deep crowded-rank impression; brightest inset groove; maximum paper tension | center | peak state |
| 005 | row 2, column 2 | counting down | A different set of wax runnels closes; top impression sinks while side tabs remain raised | center | ease out |
| 006 | row 2, column 3 | cooling | Bright groove shortens; new cooling cracks settle around the rim; paper fibers flatten unevenly | center | returning |
| 007 | row 2, column 4 | residue | Near-rest seal with one lingering raised rank mark and a final dim groove unlike frame 000 | center | clean transition to 000 |

The atlas was explicitly generated as animation source art from this plan, not as a review contact sheet. Every row-major cell is retained under `source_frames/`; local processing only slices the authored atlas, removes chroma, removes disconnected atlas-edge debris, applies a shared scale and center anchor, resizes, sheets, previews, and converts.

## Source-frame hashes

| Frame | SHA-256 |
| --- | --- |
| `000` | `b1e497f4bac7866aef2b093e97ca6a0dc311159268246feacc22a59759becf7b` |
| `001` | `2ac86e5733dc7fae61efb0dc1b32ae0804463dcc78cffe979e5326c5434a3a9e` |
| `002` | `760fbb2fc81f57397387ca122815bf7dbeac9de6fb77d00b0b90c348fb1039c8` |
| `003` | `291d8df578a3f08002938cf4b6365e588708148a229cedeb954bec830f06e371` |
| `004` | `86ce06e7ac0b54f89e1685066293a00c33bef46955c85f5b6c17b5ea413d0340` |
| `005` | `fd55e89ffdc7df39a8414349cd17371da80c361c2fa79933e7e13e47ccbab9bc` |
| `006` | `94a50ebd9c547cb7c4ebdfb78848724d83abd29afd762859c0240a1264ca0961` |
| `007` | `d121496a5028ca84f90a5237fd1f08d862487528038ca5edb51c2dd68e0a2b44` |

All eight hashes are distinct. The contact sheet and GIF were inspected at original detail; the last state returns to the same low-relief seal identity as frame `000` without duplicating it.
