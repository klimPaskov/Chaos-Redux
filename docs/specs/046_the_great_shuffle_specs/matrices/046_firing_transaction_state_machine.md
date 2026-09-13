# Event 046 firing transaction state machine

| State | Entry proof | Work performed | Valid exits | Persistent recovery proof |
| --- | --- | --- | --- | --- |
| Idle | No live lock or transaction | Event can be selected | Locked | None |
| Locked | Unique transaction ID, enabled Event 46, no terminal conflict | Freeze registry version and block duplicate starts | Snapshotted, Aborted | Transaction ID and opening source |
| Snapshotted | Capability, Chaos tier, DLC, world anchors, and owner registry frozen | Build candidate family and scope facts | Selected, Aborted | Snapshot version and scope-source proofs |
| Selected | Weighted roll, quotas, and compatibility resolved | Fix selected families and order | Planned, Aborted | Ordered family list |
| Planned | Every selected family has complete results or a pre-commit rejection | Store exact values or verified immutable seed schedule | Validated, Aborted | Per-family plan and rejection records |
| Validated | Every remaining result and reconciliation path passed | Mark families ready for commit | Committing, Aborted | Validation generation and family status |
| Committing | At least one family ready | Apply immutable results in fixed dependency order | Reconciling, Recovering | Per-family committed index or scope proof |
| Recovering | Save, interruption, or partial commit detected | Resume exact family without reroll | Committing, Reconciling, Blocked | Original transaction and immutable plan |
| Reconciling | Family commit complete | Refresh derived state and prove legality | Committing next family, Reporting, Recovering | Reconciliation completion per family |
| Reporting | All families complete or safely rejected | Calculate direct Chaos, Event Log entry, and player reports | Closing | One-shot history and report flags |
| Closing | Reports and shared entries complete | Clear every temporary buffer and lock | Idle | Final completion marker only |
| Aborted | No family has begun commit and no valid family can proceed | Clear plans and lock without consuming a firing | Idle | Abort reason for debug only |
| Blocked | A family began commit but exact recovery cannot continue | Preserve evidence and stop duplicate starts | Recovering after repair | Full transaction evidence |

## Transition rules

A transaction cannot move from Planned back to Selected.

A transaction cannot reroll after Committing begins.

Aborted is valid only before any family changes gameplay state.

A partially committed family cannot exit through Aborted.

Reporting occurs once.

Closing occurs only after every owner cleanup callback has run.

A stale lock cannot be cleared without proving that no planned or committed family remains.
