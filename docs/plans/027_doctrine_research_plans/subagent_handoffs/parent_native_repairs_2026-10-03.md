# Event 027 native filter and receipt repairs

Disposition: implemented in source with mandatory comparison and native transaction evidence unresolved.
Acceptance basis: the user's full Event 027 goal and specification package require exact track targeting, positive native readback, one-level rewards, and durable one-time receipts.

## Owner-applied changes

The native transaction architect's handoff is `native_transaction_audit_2026-10-03.md`.
The parent reviewed its syntax and completion findings against the installed documentation and the offline wiki before applying these changes.

- `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt`: all 107 `add_mastery` blocks use the documented zero-based `index` filter instead of `track_index`.
- The 107 empty-track assignment branches record native completion only when the requested subdoctrine is currently active and has completed.
A rejected assignment no longer becomes a native-completion result merely because the incomplete-branch check failed.
- `common/script_constants/027_doctrine_research_constants.txt`: `mastery_levels_per_choice = 1` describes the invariant event reward separately from `mastery_point_increment`.
- The native wrapper expected-level calculations and receipt-recovery expected-level calculation use `mastery_levels_per_choice`.
- `common/scripted_effects/027_doctrine_research_effects.txt`: `doctrine_research_pending_receipt_id` persists the exact pending attempt.
`doctrine_research_find_current_receipt` requires receipt ID, batch ID, and choice number to match.
Preparation stores the ID before setting the pending flag, and all eight terminal pending-flag cleanup paths clear the ID.
Annexation also clears the ledger-corruption flag after deleting every batch and receipt row, so a destroyed queue cannot block future independent batches for that country identity.
- `docs/plans/027_doctrine_research_plans/pending_receipt_identity_scenario.json`: saved the two-attempt collision case for the source-backed mechanic route.
This fixture is unexecuted and is not passing evidence.

## Source validation

The installed source parser successfully parsed the corrected native adapter file.
A direct source crosswalk compared every one of its 107 mastery filters with every installed Grand Doctrine's ordered track list, including Chaos Warfare.
It found no index/track mismatch and no Grand-Doctrine-dependent index ordering within these folders.

| Folder | Ordered track indexes |
| --- | --- |
| `land` | 0 infantry, 1 combat_support, 2 armor, 3 operations |
| `naval` | 0 submarines, 1 screens, 2 carriers, 3 capital_ships |
| `air` | 0 fighter_aircraft, 1 strike_aircraft, 2 medium_aircraft, 3 heavy_aircraft |
| `special_forces` | 0 special_forces_first, 1 special_forces_second |

This is a source parsing and installed-definition crosswalk.
It does not establish executed native mastery, bank settlement, or Special Forces reward attribution.

## Reference citations

| Source | Lines | Revision | Established rule |
| --- | --- | --- | --- |
| Installed `documentation/effects_documentation.md` | 1477-1504 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | `add_mastery` filters use track type and zero-based `index`. |
| Installed `documentation/effects_documentation.md` | 7774-7802 | same revision | `set_sub_doctrine.track` is the folder track index and retains its separate spelling. |
| Installed `documentation/triggers_documentation.md` | 3748-3766 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` | `has_doctrine` checks a currently active Grand Doctrine or subdoctrine. |
| Installed `documentation/triggers_documentation.md` | 3526-3538 | same revision | `has_completed_subdoctrine` checks historical completion, so it is paired with active identity. |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 2508-2542 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` | The offline doctrine-effect schema agrees with installed filter and assignment syntax. |

These sections were read locally.
The live reference search identified the installed `add_mastery` section as `7ba4d670991af373b74e3d8ebfd56f2a806f8d6b56e068a593e131c3713fff9e`.
The reference-read response could not be recovered because its code-mode handle belonged to a stale host generation.
The local section read above supplies the cited text, and no recovered MCP read result is claimed.

## Blockers and unfinished work

Both the full Event 027 state-flow request and repeated-finalization mechanic request returned `timed out awaiting tools/call after 600s`.
Neither returned a verdict or usable job identity.
No passing comparison or mechanic result is claimed.
The completion, probability, and localisation audit subagents each terminated with `workspace routing discovery timed out`.
Their required audits remain open.

Registry initialization still stands in for native transaction verification in the current source.
That does not satisfy the user's evidence requirement.
Separating the capability gates affects the valid weighted pool, so the mandatory baseline/owner-patch/comparison cycle must precede that pool change.
The failed probability audit leaves this follow-up blocked by the missing baseline.
No supported domain is declared acceptance-complete.

Exact bank preservation, synchronous native reward readback, ambiguous Special Forces identity, save/reload recovery, long-running ledger growth, final consumer presentation, complete probability scenarios, and the final acceptance report remain unresolved.
No experience grant, technology substitute, point dump, active doctrine replacement, or reduced-domain completion claim was introduced.
No completion commit has been created.
