# Git Storage Cleanup — 2026-08-22

## Scope and safety boundary

This pass removed only stale Git scratch data and locally cached LFS objects that Git LFS classified as prunable under its normal retention rules and checked against the configured remote.

The pass did not expire reflogs, delete recent LFS temporary data, remove active lock files, rewrite history, repack reachable history aggressively, alter the working tree, or touch the repository's main index.

Git pushes enumerate commits and Git objects rather than rereading every worktree file.

The maintenance in this report reduces local cache/storage overhead and refreshes graph indexes, but the reachable 20.83 GiB pack history will remain part of normal Git object negotiation until a separately planned and explicitly authorized history migration rewrites or removes it.

## Before cleanup

`git count-objects -vH` reported:

- 493 loose objects using 2.35 MiB.
- 240,803 packed objects in three packs using 20.83 GiB.
- 133 garbage files using 379.13 MiB.

The stale-file inventory found:

- 117 `.git/objects/*/tmp_obj_*` files older than 14 days, totaling 388,297,048 bytes.
- 15 allowlisted top-level `.git` scratch files from 2026-07-29, totaling 53,130,391 bytes.
- 16 object temporary files newer than the cutoff.
- Recent activity in `.git/lfs/tmp` and persistent Git LFS filter processes.

The top-level scratch allowlist consisted of isolated Event 11–20 alternate indexes and locks, Event 20 alternate indexes and locks, one Event 20 catalog commit workbook, and associated temporary Event 20 index snapshots.

## Removed stale scratch data

The cleanup resolved and verified the absolute `.git` and `.git/objects` roots before deleting any file.

It removed 132 exact files totaling 441,427,439 bytes:

- 117 object temporary files totaling 388,297,048 bytes.
- 15 top-level alternate-index and task-scratch files totaling 53,130,391 bytes.

No recursive directory deletion was used.

Every deleted object temporary file was older than the 14-day cutoff and inside the verified `.git/objects` root.

Every deleted top-level scratch file was both older than the cutoff and present in the exact allowlist.

## Git LFS cache pruning

`git lfs prune --dry-run --verify-remote` completed successfully before the mutating pass.

The dry run reported 46,903 local objects, 15,113 retained objects, 31,779 objects verified with the remote, and 31,791 files representing approximately 21 GB that would be pruned.

`git lfs prune --verify-remote` then completed successfully and reported 46,904 local objects, 15,114 retained objects, 31,779 remote verifications, and 31,791 deleted cached files.

The one-object count change occurred while concurrent recent repository work was creating current cache state; Git LFS recalculated and retained the current object set during the mutating pass.

After pruning, `.git/lfs/objects` contained 15,113 files totaling 3,800,310,194 bytes.

The prune removed local cache copies only.

It did not delete worktree files, Git commits, or remote LFS objects.

## Retained data

The following data was intentionally retained:

- All 16 object temporary files newer than the 14-day cutoff, totaling 8.82 MiB as reported by `git count-objects`.
- All current content under `.git/lfs/tmp` because it had recent activity and live LFS filter processes.
- `.git/logs/**` because these are Git reflogs used for reference history and recovery, not disposable conversation or thread logs.
- The repository's main `.git/index`, active application state, GitKraken configuration, hooks, refs, and lock state.
- All reachable packed history, including the 20.83 GiB pack set.

## Maintenance and validation

The pass refreshed the multi-pack index with `git multi-pack-index write` and the reachable changed-path commit graph with `git commit-graph write --reachable --changed-paths`.

`git gc --auto` completed without requesting an aggressive or full repack.

After stale scratch deletion, `git count-objects -vH` reported 16 garbage files using 8.82 MiB; all 16 were newer than the cutoff and deliberately retained.

`git fsck --connectivity-only --no-dangling` completed successfully after the cleanup.

`git lfs fsck --objects` completed with `Git LFS fsck OK` after the verified cache prune.

## Deferred storage migration

No history rewrite or large manual repack was performed.

Reducing the 20.83 GiB reachable pack history would be a broad, disruptive migration that can change commit identities, require coordinated force-pushes, invalidate downstream clones, and alter recovery expectations.

That work requires a dedicated retention policy, remote backup verification, collaborator coordination, and explicit authorization outside this safe cleanup pass.
