# Event033 storm-clock repair

Disposition: implemented within the explicit owner patch grant, source-model verification complete, parent/native/AA acceptance pending.
Acceptance basis: parent reviewed `storm_clock_audit_2026_10_09.md` and sealed241c runner, authorized exactly the two source files, then requested the public slot existence/range check before indexed reads.
No broader timing, overlap, achievement, report or recovery policy was accepted or implemented.

## Final pins and changed-file scope

- `common/scripted_effects/033_acid_rain_effects.txt`: `48b6c9b8ddcbacc8fafc002551735b7ade269929ecb36fa7beb5e6cc0a2ecabe`.
- `common/scripted_triggers/033_acid_rain_triggers.txt`: `d284abdeb77e548c6d1d157f3bb5fb9c9b6ae548a86df2de222451efab21e6b5`.
- New evidence: `docs/plans/033_acid_rain_plans/validation/storm_clock_2026_10_09/source_replay_after_48b_d284.json` and this handoff.

No other source, constants, GUI, achievements, aftermath helpers, costs, AI weights, assets, workbook, old receipts or git/index writes occurred.
The unchanged runner SHA is `241c252df0060dcd616ba8b0319566066e79a9474e8242d1e1bb7d431a027b5f`.
Before archive and before-failure receipt retain SHA `0ae40063d79ebed3531942335c857b63395d0727b6108d299ba35d186cb630bb` and `8206312e3be0cc032635d89fe342d922d43f9fc55b2fef082e5638a19ab71bf4` respectively.

## Exact source hunks and behavior

| Definition | Before lines | Final lines | Change |
|---|---|---|---|
| `acid_rain_process_severe_cells` | 4661–4760 | 4661–4779 | Expiry before activation/physics, pending/active split, owned activation/cleanup, opening clock reset |
| `acid_rain_process_superstorms` | 5402–5514 | 5421–5552 | Same live-window/ownership repair, pending reservation debit separate from active count |
| `acid_rain_state_has_superstorm_layer` | 114–122 | 114–127 | Stored slot exists and is1..5 before indexed serial/status reads, current serial equality |
| `acid_rain_state_is_severe_worker_owned` | absent | 130–151 | Pure internal STATE predicate |
| `acid_rain_state_is_superstorm_worker_owned` | absent | 155–176 | Pure internal STATE predicate |

The two internal predicates read their caller's existing numeric loop index and produce no temporary outputs or mutations.
They require current frozen/consequence/forecast generation, target membership, bounded matching state slot, positive consistent start/end mirrors, severe forecastID equal to the current cell, and storm serial equal to the slot serial.
Valid state ownership precedes activation markers and physical callbacks.
Only the interval from start through strictly before end admits activation/dispatch, and valid opening writes the existing last-pulse clock to actual opening time before physics.
The sustained last+3day test, packet values, bounds and intensity remain unchanged, with no catch-up or missing-clock fallback.

Expired pending0 retires2 without activation, history, active achievement closure or severe cooldown RNG.
Its storm reservation/slotID is removed once without decrementing another active storm.
Active1 retirement keeps advance interval → stored-episode closure → clear owned membership → reconcile → evacuation closure → controller forecast refresh, followed by existing slot retirement and active cooldown/count bookkeeping once.
The severe cooldown draw remains18..45 with the existing draw placement within active cleanup and slot order.
Underlying ordinary/global memberships and bands remain intact.
Foreign or stale state mirrors are left unmodified rather than cleared through another source's ownership.

The public serial guard protects existing acute-layer, physical-packet and strongest-band callers from a reused slot's stale state.
Its existence/bounds checks precede both indexed reads.
This is explicitly an affected target/caller semantic surface for the parent's same-named AA comparison, although weights and constants did not change.
There is no public end clip, mortality-class exclusivity or host worker reordering.

## Verified evidence and limits

The sealed current replay executes 9 principal scenarios and44 variants, all44 pass with zero source/fixture failures and652 source locations.
Frozen3EB replay still returns19 pass/25 source failures/zero fixture failures at579 locations and exactly retains stdout SHA `7dee487f721b3e1c39d4023c9af505638a4b98f80b07a0cad8a9698d4c13b9ee`.
The after receipt records both runs, compact observations, current stdout hash, source inventory, exact owned replacement/insertion bytes and the auxiliary reproduction command.

Raw reversal of just the two runtime bodies, public predicate and inserted private predicate block reconstructs the complete original3EB/AE069 bytes exactly.
AST comparison leaves84 runtime root entries unchanged outside the two bodies and134 original trigger root entries unchanged outside the public predicate, with only the two approved additions.
All78 runtime loop configurations match, and all9 loops in the two processors retain their original break IDs and immediate zero resets.
All seven unowned replay dependencies and the sealed F5/F6/F7 tests match their recorded hashes.

Nine separate actual-public-predicate cases reject declared missing slot,0,-1,6,1000, missing serial and reused serial, while accepting valid slots1 and5.
Invalid/missing slot and missing-serial cases perform no indexed access in the conservative source interpreter, and AST order independently puts the bounds before indexed reads.
Missing variables are declared native absence0, not unknown-fact fallbacks.
These auxiliary cases reuse the sealed parser/Replay prefix without changing the runner.
An initial auxiliary VM wrapper omitted the host Buffer primitive and failed before checks, then was corrected without source or runner changes.

Physical evidence remains dispatch/first-entry-guard witnesses and actual pre-physical key writes, not successful mortality, damage, benefit, finance or native physics.
Achievement closure/counter mapping and consequence reconciliation execute against the declared fixtures, but awards, populated target/evacuation ledgers and native modifier application remain boundaries.
The closure bridge still uses stored episode/credit/gen/end facts, while its mapper allows pulse count>=0, so pending cancellation deliberately bypasses it rather than inventing active history.
No ambiguous historical active provenance or migration policy is reconstructed.

Current MCP lookup confirms the new storm ownership definition unshadowed at revision `e47f5c7f49d2fc9dd32d203e593e6a34c5bb03015590e0a3834b0a3189b90e6e`, with complete definition structure but incomplete references.
Both STATE predicate validations remain partial, `valid=null`, syntax/command-kind/declared-scope checks only,13 unresolved argument blocks and10 omitted findings each.
The initial limit60 request was terminally rejected and corrected to the supported32, with no backend recovery or native jobs.
Primary offline/installed references remain linked through the retained before receipt.
Parent independently reports final44/44 and all six nonsealed legacy regressions passing with loopcount78, which this worker did not rerun.

No gameplay simplifications or unapproved fallback were implemented.
Native population/physics/MP/cost/UI/event completion is not claimed.
Parent owns the focused graph ArtifactNotFound disposition, mandatory partial AA after comparison against its26 named contracts/four scored probes, final acceptance and commit.
Skills used: chaos-redux-events, chaos-redux-subagents and loop-break-isolation guidance, preserving separate call frames, exact ownership and private break lifetimes.
Writes stop after the final file/hash seal, with no further source or test edits planned.
