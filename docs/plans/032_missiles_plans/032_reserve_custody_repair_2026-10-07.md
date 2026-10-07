# Event 032 reserve custody and site-loss repair, 2026-10-07

Disposition: implementation and source validation completed for the bounded accounting defects below; native execution and the full Event 032 contract remain unproven.
Authority: the user's continuing full Event 032 implementation goal, including physical capacity, custody, capture, cleanup and no-duplication accounting.
The previous goal turn made progress through commit `480d757f3`; this continuation inspected the later working source and preserved the subsequent mission, allocation, evolution and Event Logs changes.

## Implemented behavior

- Free site stock uses capacity left after that site's matching operation allocation; the same slot cannot hold both free and assigned missiles.
- `missiles_unallocated_reserve` records the remainder of available national reserve outside usable sites and is cleared during country removal.
- Custody projection uses the actual country at `PREV`, skips foreign-controlled stale registry entries without clearing them, and runs after preparation markers are written.
- Site-loss settlement returns the order, debits the lost assignment, and clears the operation while deferring custody redistribution until the outer capture, scuttle, isolation or disaster mutation has finished.
- The capture caller initializes its temporary output before entering the helper, so the result remains available for the matching debit and credit.
- Biological reservation and direct consumption initialize their debit-proof output before the helper; a physical warhead debit cannot lose its proof merely because the helper returned.
- Recapture moves existing sealed stock from the proven former holder's captured-reserve ledger to the new holder; it does not charge the former holder's ordinary reserve or discard its physical receipt.
- Network counts, capacity and region membership accumulate on the country whose states are iterated, including a defender called from an attacking event.
- Incoming site-damage records validate their STATE event target and copy its facts explicitly before the producer clears its scratch fields; the existing `.7` receiver performs the final defender status/phase refresh.
- Isolation explicitly restores the programme phase after finishing the physical change.

No cost, weight, operation family, payload consequence, asset, technology, evolution or accepted route was removed or simplified by this repair.
No recurring hook or new event id was introduced.
The scripted storage predicate shares the existing project-storage conditions without changing those project conditions.

## Concrete accounting evidence

The source-driven regression evaluates the production custody, refund and settlement definitions for the modeled variable/flag/scope operations.
It deliberately omits presentation, native mission effects and special-payload execution and therefore does not represent a game simulation.

For 12 free missiles, 4 assigned missiles, and two capacity-10 sites, the pre-repair source puts 10 free plus 4 assigned missiles at the first site.
After its lost-site cleanup it projects 16 free missiles while the country holds only 12.
The repaired source puts 6 free plus 4 assigned at the first site and 6 free at the second, retains total free custody 12 during settlement, and leaves exactly 6 after destroying the first site.

All 13 `.tools/test_event32*.py` modules passed before the biological-proof follow-up: 136 tests in total.
The targeted payload module then passed all eight tests, including the added caller-output lifetime regression, bringing the tested suite to 137 tests.
The seven new ledger tests include 231 free-stock/assignment combinations, foreign event ROOT, stale foreign registry membership, refund and repeated cleanup, sealed-stock transfer bounded by the former holder, defender network totals, and state-receipt precedence over a conflicting country variable.
The existing state-scope regression now tracks the previous scope through explicit transitions instead of misclassifying a valid STATE-to-COUNTRY `PREV` block.

The read-only architect reviewed all five settlement callers and the cleanup closure, then identified recapture, defender-accounting and isolation-refresh gaps.
The parent implemented all three and the architect's second pass marked their source counterexamples resolved.
See `subagent_handoffs/032_custody_settlement_review_2026-10-07.md` for both reviews, source hashes and limits.
Its deliberately malformed insufficient-escrow fixture remains a robustness uncertainty: the bounded producer review found no normal path that creates it, and the helper is not claimed as a repair API for inconsistent receipts.

## Source and MCP evidence

Installed root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
The live status resource reports server version `3.10.0`; no client task negotiation or helper-expansion capability was assumed.

| Read reference | Lines | Revision or SHA-256 | Relevant rule |
| --- | --- | --- | --- |
| Installed `documentation/effects_documentation.md` | 4296–4311, 6486–6495, 2695–2712 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | Array scope transitions, integer rounding and variable clamps |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 1217 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | `PREV` inside a scope-array iterator is its calling scope |
| Installed `documentation/triggers_documentation.md` | 2110–2135 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` | Variable-to-variable comparison syntax and supported comparison names |
| Installed `common/scripted_effects/GER_scripted_effects.txt` | 1273–1296 | `1d6b5cc8e00d685aa3c95cecab41cfeb2da590e90490de5dcce05e8e8e2beeb3` | Vanilla bounded state-array processing and shared temporary accumulation |

The reference context bundle omitted Event modding, Effects, Triggers, Scopes, On actions and Localisation due to its four-result boundary; it is not treated as detailed coverage.
Task-specific variable/scope rules were read through the cited targeted reference routes and inspected source precedents.
Pre-edit `hoi4.source_lookup` located custody and lost-site settlement at source revision `1951d10f3c4626decd589355f17f6a5ee46a03f1be19a670c0e6c741f0b26f9a`; bounded child structure and direct source reads supplied the helper bodies.

`hoi4.script_validate` returned `SCRIPT_CHECK_PARTIAL` for the STATE storage predicate and COUNTRY custody body.
It checked syntax, command kinds and declared scopes, but left native argument blocks unchecked (`valid = null`, `parametersChecked = false`); the custody iterator's nested body was not established by that route.
The cited comparison, loop and clamp syntax was read separately, and no full engine validation is claimed.

The first narrow `.7` event trace timed out after 600 seconds.
A smaller retry (`downstream`, depth 1, one node, one edge, no helper expansion) returned `EVENT_INSPECTED_PARTIAL`, revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0` and graph hash `d494c41cf68a6eb896650d0f95ea38572ce93b8c83273a07a92d60c74eb41ceb`.
The complete trace artifact was retrieved in byte ranges and verified at 1,078,832 bytes with SHA-256 `ce94af462e498694ab06ebcaf9b353e711d9862e666a36ceba424efb7b725904`.
It selects `event:chaosx.nr32.7` at `events/032_missile_crisis.txt:33`, but marks `missiles_refresh_program_from_receiver` as `EVENT_HELPER_UNRESOLVED` because the focused event catalog omits the helper.
The production definition was inspected directly; this domain coverage gap does not establish a missing gameplay definition or runtime proof.
Trace URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce94af462e498694ab06ebcaf9b353e711d9862e666a36ceba424efb7b725904/50d1c5d76ec14a0b27a60598e94729eb3af87afdf9af437324e7a4470808ca86/event-trace-8f4a82aa5d84.json`.
The first oversized artifact reads contained truncated base64 and failed integrity checks; they were replaced by validated 24,000-byte chunks before the report was used.

The exact `.7` scope render timed out after 600 seconds at the one-node boundary.
The more limited entry-view retry also timed out after 600 seconds; a depth-zero request was rejected by the live schema and corrected to its minimum depth of one before that retry.
No new render is claimed.
The cached-revision event comparison timed out after 600 seconds; an artifact-backed one-node retry is pending at this source checkpoint.
These focused event graphs omit the changed helper bodies, so even a structural comparison would not establish the accounting patch's before/after semantics.

## Remaining full-goal work and limits

The reviewed `subagent_handoffs/032_current_contract_reconciliation_2026-10-07.md` identifies accepted work still missing or insufficiently proved: stochastic MTTH and nonrecurring eligibility observation, chemical payload escrow through CBRN ownership, recovery AI force/supply parity, Event 5/6 succession callers, survey failure settlement, conditional captured-site diplomacy and preparation changes, and the named probability baselines/comparisons.
Later owner rejection labels do not approve dropping those user-required outcomes.
This turn introduces no gameplay simplification; it does not approve or conceal those earlier departures.
The native duplicate-ID investigation remains open, and its temporary allocation markers remain pending attribution.
Live custody/callback behavior, a clean game error log, and final event/technology/probability coverage are not claimed.

The workbook was read directly: Events row 33 remains `To Be Reworked`, with the older Evo I/V wording.
The workbook and all three exports contain concurrent changes from other work, so this accounting commit does not take ownership of them.
Their final exact wording/export update remains required; CSV files were not edited.
No asset or icon changes are needed for these existing mechanics.

Skills used: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-shared-git-commit`, and `xlsx` for the catalog inspection.
The MTTH skill was read to prepare the subsequent required timing repair; no weighted timing code was changed here.
No skill was changed because the established caller-temporary, `PREV`, source-evidence and shared-index rules already cover these defects.
