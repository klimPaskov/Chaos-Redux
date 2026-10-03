# Event 032 catalog status review

Disposition: implemented and parent-reviewed.
Acceptance basis: the user's catalog-alignment requirement and the current event skill's post-20 status contract for an existing root with unresolved completion work.

The context-free `chaosx_spreadsheet_doc_worker` changed only `Events!M33` for id `32`, Missiles, from `Needs Testing` to `To Be Reworked`.
The existing status style and conditional formatting remain applicable.
The parent compared the worker's preserved source package with the committed LFS object and found only `xl/worksheets/sheet1.xml` changed, with exactly one cell-value difference at M33.
All descriptions, evolution text, type, minimum chaos, cluster, world-end, other cells, and other workbook XML parts were preserved.
No formulas exist in that source package.

The worker's workbook hashes are `878f5808a8e236b069766b3b7a53a7fdd25c1b29d4f74ae82a3a8dfaff7bb9f6` before and `42746e24fa814e60daff94f4fee669c85a51e3c2f2c7ad59603cb16004c2f0a0` after.
Commit `9c66fbf85f4aad47bb3796bc59e7a25d4f5e9f89` contains the workbook and the repository-generated Events CSV only.

The repository exporter completed successfully.
Its Events output has 166 rows and 13 columns, SHA-256 `50b4c49e87d6879cd4affcc6cbfb728b5d5ba99780f65556c04ce8d8d858a1ed`.
Its Clusters output has 20 rows and 8 columns, SHA-256 `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a`.
Its Scenarios output has 17 rows and 6 columns, SHA-256 `a7a26d10435c451cd555c6e72749a2dda54b20d62a07fda7d2cdb5a8a7065d7e`.
Clusters and Scenarios already had those bytes before the export, so the worker excluded the modified shared-worktree snapshots from its commit.
No CSV was edited directly.

The worker published the commit but its index reconciliation was blocked by a shared lock.
Its attempted removal of an exact zero-byte stale lock was automatically rejected as `blocked by policy`.
The parent waited until the lock was absent, confirmed the relevant index entries still matched the commit's parent, and reconciled only the workbook and Events CSV to the published commit.
No lock, working-tree content, or unrelated staged work was removed.

After that commit, the current worktree workbook contains a separate scenario-row change by another shared-tree actor.
The parent observed M33 still reads `To Be Reworked` and preserved the separate scenario change without replacing the current workbook or regenerating another actor's pending export.
The exact hash above identifies the reviewed committed Event 32 package, rather than claiming the entire shared workbook remains frozen.
