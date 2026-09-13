# Launch 10 startup checkpoint

Status: clean startup and live feature coverage remain incomplete.
The supplied shortcut launched verified HOI4 PID 24320 at 2026-09-05 11:32:14 local time.
The process remained responsive, and the latest crash directory still belonged to launch 06.
The parent stopped only the verified process after the current parser passes, archived fresh logs, and removed the hash-matching disposable doctrine probe.
Exact timestamps, source snapshot, probe, and logs are under `logs/launch_10/`.
No main-menu visual acceptance, country-map entry, campaign, save, or teaser capture occurred.

The fresh error log contains 537,839 bytes and 3,228 lines.
SHA-256: `449e71811737095023375a08bd56182f6d4e1b438576b23617bb704c396c05c0`.
Line totals include repeated diagnostics, not unique bugs.

| Targeted diagnostic | Launch 09 | Launch 10 |
| --- | ---: | ---: |
| Missing Event 39 score bounds | 110 | 0 |
| Direct Event 31 flag-format warnings | 48 | 0 |
| Unsupported Event 31 mission cleanup command | 16 | 0 |
| Unsupported Event 24 temporary cleanup commands | 58 | 2 |
| Misplaced Event 32 `check_variable` effects | 4 | 0 |
| Doctrine `index` child rejected | 214 | 214 |
| Disposable doctrine probe errors | 2 | 0 |

The two remaining Event 24 records belong to the deliberately retained cross-helper `reliance_delta` input cleanup.
The nonzero doctrine probe parsed without an error, supporting the subsequent bounded `track_index` spelling repair recorded in `doctrine_track_index_repair.md`.
That production repair occurred after this launch and is not included in the results above.
The Event 32 missing helper brace was also outside this launch while its weighted-target baseline remained pending.

Parser improvements do not certify mission cleanup outcomes, target selection, persistence, or visuals in a campaign.
The comprehensive goal remains active, and no feature-level pass is claimed.
