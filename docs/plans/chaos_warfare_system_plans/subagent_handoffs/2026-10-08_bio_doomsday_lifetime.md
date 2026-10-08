# Biological doomsday temporary-output lifetime repair

Disposition: implemented within the parent-authorized bounded repair, awaiting parent review and commit.
The accepted behavior derives from `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md`, whose authority section records the user's implementation request.
The parent authorized only caller allocation fixes in `biological_doomsday_effects.txt`, then expressly extended ownership to the biological bridge's release receipt and a verified private loop-break binding that preserves complete traversal.
This handoff is implementation evidence, not acceptance of new gameplay design or a claim of native execution.

## Files changed and exact edits

`common/scripted_effects/biological_doomsday_effects.txt` has 20 inserted physical lines, including comments; every original command and its order remains present.

- `bio_doomsday_resolve_release` owns `bio_doomsday_target_states` as an empty temporary array and initializes six scalar outputs to `constant:bio_lifecycle_math.zero`: `bio_doomsday_target_count`, four `bio_doomsday_stock_<agent>` values, and `bio_doomsday_arsenal_consumed_total`.
- `bio_doomsday_dispatch_current_agent` initializes `bio_seed_dispatch_status` to `constant:bio_lifecycle_proof.missing` and owns the reset-only downstream inputs before the returning reset helper: concealment and four overrides at zero, weaponization multiplier at one.
- The dispatch loop initializes `bio_doomsday_dispatch_break` to zero immediately before `for_each_scope_loop` and binds `break = bio_doomsday_dispatch_break`.
  Its target array, target order, loop body, allocation math, and state filters remain unchanged.
- `bio_doomsday_register_batch_consequence` initializes `bio_seed_doctrine_condemnation_mult` to one immediately before `bio_lifecycle_prepare_actor_doctrine_snapshot` so the returned multiplier survives for the original batch calculation.

`events/cbrn_doomsday_raid_bridge.txt` has two inserted lines in `chaosx_cbrn_doom_raid.2`: an ownership comment and `bio_doomsday_release_status = constant:bio_lifecycle_proof.missing` immediately before the resolver call.
The following news gate consumes that exact receipt.
`bio_doomsday_full_resolution_status` is not consumed by this bridge, so it receives no unused outer declaration.

No constants, prices, native reserved lots, guards, policy rules, random blocks, Condemnation formulas, terminal Fallout request, event targets, or other gameplay files were edited.
`bio_active_agent` is not initialized or reset by this patch.
`bio_seed_dispatch_status` remains a result receipt; repeat protection remains the existing `bio_doomsday_raid_committed` flag.
No periodic hook or new world iteration was introduced.
No index or commit operation was performed; the parent owns integration and commit.

## Helper map and caller contracts

| Existing helper | Scope | Inputs | Outputs / owning consumer | Side effects |
| --- | --- | --- | --- | --- |
| `bio_doomsday_collect_target_states` | Actor country | Current controlled territory, neighboring controller/war/ordinary-pathogen eligibility, `bio_doomsday_actor` target | Empty caller-owned `bio_doomsday_target_states` and zero `bio_doomsday_target_count`; resolver consumes both | Temporary collection only |
| `bio_doomsday_capture_and_consume_arsenal` | Actor country | Four real model counts at native resolution, existing reserved-per-agent constant | Four zero caller-owned stock values and zero arsenal total; resolver consumes all five | Debits modeled current stocks once, accounts for native reserved lots, safety recapture |
| `bio_doomsday_dispatch_current_agent` | Actor country entering exact states | Target array, active agent/stock, caller-owned seeded totals | Dispatcher owns missing seed receipt and neutral reset-only inputs; resolver's existing seeded totals retain modifications | Ordinary lifecycle calls and exact accepted-state history |
| `bio_lifecycle_prepare_actor_doctrine_snapshot` | Actor country here; shared helper also used by seed math | Actor target and proof, doctrine/command/advisor state | Batch consumer owns condemnation multiplier at one | Temporary snapshot; no political or physical debit |
| `bio_doomsday_resolve_release` | Actor country, entered through country-root bridge | Exact raid target, current authorization and last-resort gates | Caller must initialize any returned release/full-resolution receipt it consumes to missing | Existing one-shot commit, arsenal capture, dispatch, batch consequence and terminal Fallout request |

The corrected consuming declarations are the migration; no helper extraction or new public helper is necessary.
Source comments document ownership next to the declarations, and this handoff documents initial values and call sites.
Shared helper documentation and the existing dynamic-effect registry remain outside this narrow patch because no new reusable API was introduced.

## Tuning, event targets, and cleanup

Existing `bio_lifecycle_math.zero`, `one`, proof constants, and `bio_doomsday_raid.reserved_per_agent` are reused unchanged.
No tuning table or threshold is added.
Regular actor, victim and exact raid-target pointers remain chain-owned event targets with their original use and lifetime.
The patch adds no global target and requires no target cleanup.
Temporary outputs first created in the resolver remain local unless an outer consuming caller owns them; arrays, stocks, and other local scratch disappear at helper return under the conservative fixture model.
The bridge owns only its consumed release receipt, and the resolver retains existing full/partial history flags for durable outcome history.

## Reference and MCP evidence

The connected live routes for `reference_context`, `reference_search`, `reference_read`, `source_lookup`, and `script_validate` were exposed and used.
Machine-readable returned data is archived in `docs/testing/2026-10-08_bio_doomsday_lifetime/reference_evidence.json` and `script_validate_evidence.json`.
The context bundle omitted general Effects, Triggers, Scopes and On actions sections at its limit; this report claims only the targeted sections actually read below, not full context coverage.

- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 435–443, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`: temporaries are unscoped; names first created in a scripted helper may disappear; caller-preinitialized storage survives with modifications.
- The same offline file, line 1217, same SHA: scope foreach accepts a temporary break value and visits each array scope.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, lines 7820–7827, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`: `set_temp_variable` supports any scope and variable/constant-compatible existing assignment patterns.
- The same installed file, lines 2763–2772: `clear_temp_array` clears temporary array contents in any scope.
- The same installed file, lines 4296–4311: scope foreach defaults to temporary `break`, and a nonzero break value ends traversal.
  Combined with documented unscoped temporary storage, an inherited nonzero outer break is a source-level risk; a reset private break isolates this traversal.
- Installed raid documentation, lines 167–176: native essential equipment is collected after raid creation.
  This supports keeping the original four reserved lots rather than debiting them again; it is not observed equipment-payment proof.
- Vanilla `common/scripted_effects/GRE_scripted_effects.txt`, lines 90–98: a temporary value is declared in the consuming effect before use and a nested helper.
  Exact local source hashes and excerpts for these two local reads are in `local_reference_evidence.json`.

The source lookup identified `bio_doomsday_resolve_release` at indexed revision `c4b2384bc17ffb4be19fbcda4ec0b31a3e09242d3f490f80922e78dd0ff81f28`.
It returned `referencesComplete = false` with 20,185 unresolved workspace references; direct bounded source search found the actual bridge rather than treating that result as consumer completeness.

The representative additions passed command-kind, declared-scope and syntax coverage, but `script_validate` returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, and four unchecked native argument blocks.
These were three `set_temp_variable` blocks and the foreach block, whose relevant installed syntax was read directly.
This is partial tooling evidence; argument semantics and temporary lifetime remain separate source/reference evidence.

Parent owns event baseline/inspect/render/compare evidence and the final source-wide integration review.
Parent receipts are saved in `docs/testing/2026-10-08_bio_remaining_callers/reference_and_mcp_receipts.json`.
The focused scan of `chaosx_cbrn_doom_raid.2` was `PARTIAL` at revision `10aaec8852ad155188b9418a96fec3a0d1d9c7f07eaa5bd47c57cb3bc29062e8`, expanded zero helpers, and produced a 96,802,897-byte graph.
Its timing overlapped this patch, so it is not a clean pre-change baseline.
No complete event compare is claimed by this handoff.
The parent supplied MCP 3.10.0 with unconfirmed native-task negotiation and the broad graph's 96 MB versus 64 MiB comparison-artifact limit.
No helper-expansion mode or native MCP task was requested here.
No in-scope weight, AI score or random-selection patch was made, and this suite neither executes nor changes RNG.

## Actual-source validation

Command: `node docs/testing/2026-10-08_bio_doomsday_lifetime_source_tests.js`.
Result: **28 passing cases, zero failures**, recorded in `docs/testing/2026-10-08_bio_doomsday_lifetime_source_tests.result.json`.
The suite imports the unchanged BaseVM from `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js`.
Its inherited `run` method retains conservative helper-frame deletion for every actual scripted call; no temporary scratch is globally retained or auto-created to repair missing caller ownership.
Regular country/state maps and typed scope pointers are separate from temporary storage.

Coverage includes byte-exact before/after manifests and equality of current owned files and executed dependent definitions; original-command order preservation; empty, one, three and eight eligible states; domestic-first unique enemy-front collection; neutral/wasteland/zombie exclusions; all four stock captures and negative debits; four reserved lots with zero current stocks; exact accepted totals and full/partial receipts; mixed and wholly rejected seeds; stale positive receipts; prior commit repeat rejection; current policy/capitulation/last-resort rejection; stale outer/private break values and repeat traversal; stale override/concealment/weaponization inputs; actual doctrine output lifetime and the original 300-times-multiplier/floor calculation; and the actual bridge's accepted/rejected news gate.

The fixture executes actual doomsday resolver, collector, stock capture, allocation/marking/history and batch-consequence source, plus actual reset, agent/route/result profile, doctrine, finalize, designer-modifier gates, dispatch, seed validator and exact state-eligibility bodies.
Physical slot storage/scheduling and downstream political/terminal systems are explicit boundaries.
Before-source regression cases reproduce lost collected targets, lost stock outputs after a direct unowned capture, lost dispatch receipts after an accepted seed, inherited outer break, lost bridge receipt and ordinary batch Condemnation collapsing to the floor without caller-owned doctrine output.
One focused old-dispatch receipt regression supplies the neutral weaponization input explicitly to isolate the lost receipt from the independent reset-default defect; the full before-resolver case receives no such repair.

The test has a bounded DoomsdayVM subclass for native scope traversal, neutral fixture gates, equipment observations, nearest-integer round/truncated fixed-point division, meta interpolation and downstream observations.
This is a domain fixture using the existing VM, not a general interpreter or an engine emulator.
Unsupported unused constants with precision beyond the BaseVM's five-decimal model are listed in the result JSON; they are never substituted or exercised.
No undocumented foreach ceiling is imposed, and no 1,000-iteration foreach engine claim is made.

## Byte archives and concurrent dependencies

`docs/testing/2026-10-08_bio_doomsday_lifetime/.gitattributes` sets `before/** -text` and `after/** -text`.
The archive retains exact source bytes for both owned gameplay files and eleven test inputs, with SHA-256/byte counts in `before_manifest.json` and `after_manifest.json`.
Current full-file hashes are recorded separately in the result JSON, while only actually executed lifecycle definitions are required to match; unrelated concurrent owner edits do not falsely invalidate this bounded evidence.
The BaseVM source text matches the untouched archive, allowing only CRLF-to-LF conversion for the current checked-out copy.
Current owned-source comparisons allow the same newline conversion; all archived bytes, manifest hashes and original-command checks remain strict.
This permits the same 28 cases to run against Git's LF-normalized candidate tree without changing the interpreter or masking substantive source changes.
Concurrent parent/owner changes to `biological_lifecycle_effects.txt` were detected by current-source equality, so its after archive was refreshed to `bafa99015ee34357a41aeee1741f715c1b61fe4d299d24cee0c2628fdc6aee11` and the suite rerun.
The immutable before archive remains `9bf1e04826fdde8c745e946af3230b6534707f457777637bda84e0c2f6105450`.
`after_dependency_refresh.json` records the dependency change without attributing it to this worker.
These are bounded source comparisons with current dependencies, not a historical whole-workspace reconstruction.

## Limitations and follow-up

No gameplay simplification or fallback was introduced.
Native equipment reads/debits, native preparation/reserved-lot behavior, exact engine rounding, actual lifecycle record persistence/incubation/detection/ticks, retaliation classification, advisor/designer modifiers beyond explicit absent fixtures, Condemnation submission, Fallout coordination, science/treaty callbacks and native news delivery are unproved by these fixtures.
The remaining native behavior and final event MCP integration are parent-owned validation limits, not completed engine evidence.
The user owns live-game validation; no game launch or log search was performed.
No new assets or player-facing text were needed for this storage-only change.
Skills used: `chaos-redux-events`, `chaos-redux-native-raids`, `chaos-redux-subagents`, including the existing loop-break-isolation reference.
No skill was created or modified because the existing skills already cover the discovered lifetime and break-isolation rules.
