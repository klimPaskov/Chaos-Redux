# Event 23 / Event 5 all-transfer-paths audit, 2026-09-26

## Status and authority

**Disposition: unresolved.** The user explicitly requires a frozen pre-transfer custody snapshot and post-transfer reconciliation for Event 5, separate physical custody, technical access, command formation, and delivery integration, device conservation across save/reload, and cessation of Soviet-only production and evolutions if SOV disappears while valid local custody survives. This read-only audit finds uncovered state-changing routes and cannot certify that acceptance criterion. The parent owns the broad transfer-family repair and runtime evidence. This document is an audit finding and proposal, not acceptance of a changed design.

Only this handoff was created. No gameplay source, spec, workbook, asset, or existing documentation was edited. No commit was made.

## References and method

- Required local instructions: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-state-ledgers`, and `chaos-redux-subagents`.
- Accepted design source inspected: `docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_spec_part_6_soviet_collapse_integration.md` and Part 7 `..._shared_systems_cross_event_and_cluster.md`. Their location alone does not prove approval. The operative acceptance basis for this audit is the explicit requirement in the parent prompt.
- Offline wiki consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and State modding. The On actions page identifies `on_state_control_changed` ROOT/new controller, FROM/old controller, and FROM.FROM/state, and release hooks with ROOT/released country.
- Vanilla documentation consulted: `documentation/effects_documentation.md` (`transfer_state_to`, `release`, event-target effects), `documentation/triggers_documentation.md` (`has_event_target`), `documentation/script_concept_documentation.md` (script constants), and `common/script_constants/documentation.md`. The effects document says `transfer_state_to` sets both owner and controller, while `release` releases the specified country as a puppet using owned states. Vanilla `events/AAT_Iceland.txt:632-636` provides a direct `transfer_state_to` precedent. None of these references establishes callback ordering for this mod's sequence.
- Sources inspected: `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/on_actions/005_soviet_collapse_on_actions.txt`, `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` and its markdown, `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`, `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt`, `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`, and `common/on_actions/023_sov_nuclear_bombs_on_actions.txt`.

## Exact Event 5 route inventory

`common/scripted_effects/005_soviet_collapse_effects.txt:4273-4391` contains four dynamic `release = event_target:soviet_collapse_dynamic_release_target` sites at **4291, 4315, 4350, 4385**. Each is immediately preceded by `sov_nuclear_bombs_snapshot_event5_release_tranche` at **4290, 4314, 4349, 4384**. Those calls share `soviet_collapse_release_scope_from_soviet_collapse_owner`, which is called by the first-wave and progressive release loops at **26617** and **26637**, including the selected progressive target flow at **25952-25969**. The snapshot helper selects registered owned/controlled states that are cores of that release target. The four call sites therefore cover only the snapshot helper's actual gate and selected states, not every Event 5 state change.

There are **82 literal `transfer_state_to` sites in 34 successor spawn helpers** between **22926 and 24220**. Inventory below lists the source state IDs in source order. A repeated ID is a conditional alternative or competing successor route, not an assertion that both transfers execute in one run. Each helper's first transfer line is a source reference for its row.

| Successor helper suffix | State IDs transferred | Calls | First line |
| --- | --- | ---: | ---: |
| CFR | 248, 253 | 2 | 22926 |
| MFR | 252, 251 | 2 | 22958 |
| AOX | 195 | 1 | 22989 |
| FTH | 200, 200, 226 | 3 | 23019 |
| BBH | 226, 200, 226, 227 | 4 | 23059 |
| AEX | 405, 405, 584, 742 | 4 | 23114 |
| IKX | 257, 258 | 2 | 23169 |
| DSC | 217, 260 | 2 | 23200 |
| UWR | 247 | 1 | 23231 |
| KMB | 569 | 1 | 23259 |
| TNC | 585, 586 | 2 | 23287 |
| AAX | 583, 587, 588 | 3 | 23327 |
| UDC | 223, 220, 240 | 3 | 23370 |
| SDZ | 248, 351 | 2 | 23405 |
| GAC | 222, 224 | 2 | 23436 |
| DHC | 218, 238 | 2 | 23467 |
| KHC | 234, 235 | 2 | 23498 |
| FEV | 408, 409 | 2 | 23530 |
| SZA | 578, 580 | 2 | 23562 |
| UWD | 582, 581 | 2 | 23593 |
| IMX | 827, 828, 232, 821, 827, 828 | 6 | 23629 |
| IUL | 651, 250 | 2 | 23695 |
| IJX | 256, 249, 256 | 3 | 23731 |
| INX | 249, 256 | 2 | 23781 |
| SOG | 586, 732 | 2 | 23832 |
| ANX | 742, 584, 405 | 3 | 23872 |
| ABX | 232, 821, 827, 828 | 4 | 23927 |
| ADX | 657, 561 | 2 | 23998 |
| PRA | 570, 571 | 2 | 24030 |
| ILX | 575, 576 | 2 | 24061 |
| ICD | 254, 255 | 2 | 24093 |
| ARD | 214, 213, 214 | 3 | 24127 |
| NRF | 213, 213, 214 | 3 | 24177 |
| NLC | 216, 825 | 2 | 24216 |

The **progressive** route calls `soviet_collapse_spawn_pressure_successor_progressive_target_if_enabled` before the later ordinary release at **25952-25969** and **26637-26655**. That dispatcher calls the same spawn helpers from SOV scope at **24249-24283**. If a selected tag is a pressure successor, the subsequent ordinary-release branch excludes it, so its direct transfers are the actual state change. The **active high-chaos** route at **4460-4472** and **terminal high-chaos** route at **4427-4457** call `soviet_collapse_maybe_spawn_high_chaos_successors` at **24212-24246**, which directly calls all 34 helpers subject to their gates. Thus the 82-site family is not confined to a later wrapped release.

Two further literal `release = KAZ` sites are at **26609** (first-year backlog final gate) and **27032** (opening first wave). Neither has a preceding Event 23 snapshot call. Both may create a state-owner/controller change if KAZ does not exist and owns eligible cores. `set_autonomy` following a release is a political status change, not itself a state transfer.

Within the two inspected Event 5 scripted files, the literal state-changing commands found were the four wrapped dynamic releases, two unwrapped KAZ releases, and 82 direct transfers. Event 5 `on_actions` contains startup registration and an `on_annex` breakaway-defeat hook, not an additional literal state-transfer command. This is a bounded file inventory, not a proof that every focus, decision, peace action, or external system changing those same states is covered.

## Event 23 custody behavior and gap

**Source facts.** The Event 23 opening assigns storage to SOV's capital and two `random_owned_controlled_state` selections (`023_sov_nuclear_bombs_event_effects.txt:126-169`). Its registered-state predicate is the storage flag alone (`023_sov_nuclear_bombs_runtime_triggers.txt:23-25`). Therefore any eligible Soviet state transferred by a high-chaos helper could have been selected as one of the opening storage sites. The test selector can select a registered site, so testing can also be tied to an affected storage state. Reactor construction uses a separate pending site flag. Command and delivery capabilities are not equivalent to a registered storage flag.

The snapshot at `023_sov_nuclear_bombs_runtime_effects.txt:1570-1623` freezes each selected site's operational, assigned, reserved, transferred, dismantled, and missing buckets, custody state, owner, controller, holder, and generation. It does **not** freeze the Part 6 full-tranche roster of global operational/reserved totals, in-transit and dismantlement context, production and assembly sites, active test missions, command states, staff pools, delivery-force ownership, doctrine, readiness, integrity, posture, or public knowledge. The helper also refuses a new tranche while the global pending flag remains set.

`on_state_control_changed` at `023_sov_nuclear_bombs_on_actions.txt:42-57` first reconciles a pending Event 5 snapshot for `FROM.FROM`, then runs ordinary registered-site reconciliation. `on_release_as_free` and `on_release_as_puppet` at **59-69** reconcile only pending registered states owned or controlled by the released country. Ordinary reconciliation at `023_sov_nuclear_bombs_runtime_effects.txt:1764-1812` explicitly excludes snapshot-pending sites, moves current intact operational/assigned buckets into transferred physical custody, rebinds a non-Soviet holder, records current owner/controller, and refreshes the global arithmetic ledger. It neither creates a snapshot nor records the Event 5 custody episode flag or a snapshot generation. Event 5's 82 direct transfer calls and two KAZ releases do not call the snapshot helper before their state change.

`sov_nuclear_bombs_mark_site_transferred` at **1060-1178** leaves live native delivery reservations in the reserved bucket until exact callback resolution and attempts native stockpile removal from the current holder or SOV, marking a dispute when proof is insufficient. This is a conservative current-bucket mechanism. It is not a comparison against the accepted frozen pre-transfer receipt. `sov_nuclear_bombs_refresh_ledger_reconciliation` at **75-115** tests global accounted buckets against registered total and detects negative/disputed conditions. That arithmetic can remain clean after a post-only reclassification, so a clean value cannot prove that each Event 5 device was assigned exactly once to the correct pre-transfer site and new holder, or that no custody stage was skipped across save/reload.

**Runtime inference, not observed engine result.** Since vanilla says `transfer_state_to` sets owner and controller, it is plausible that a changed controller fires `on_state_control_changed`, allowing the ordinary post-only callback to conserve the sum of currently registered buckets. The inspected vanilla docs/wiki do not prove that the callback fires for every direct transfer or static `release`, that it runs after ownership stabilizes, or that every transfer actually changes controller from a different country. A release hook is likewise not proof of coverage because it only processes states carrying a pending snapshot. No in-game or saved-game scenario was run. The exact callback timing and save/reload behavior remain unresolved.

The terminal path has an additional deterministic source gap. `soviet_collapse_apply_terminal_collapse` sets `soviet_collapse_terminal_collapse_in_progress` at **4720** before the high-chaos spawn and release waves, and the forced terminal scenario does the same at **4785**. `sov_nuclear_bombs_event5_bridge_is_active` at `023_sov_nuclear_bombs_runtime_triggers.txt:31-35` rejects that flag. Consequently even the four dynamic release call sites invoke a snapshot helper whose gate rejects terminal-in-progress transfers. The ordinary controller callback has no equivalent frozen receipt. Event 23's Soviet actor validity requires `tag = SOV` and `exists = yes` (`023_sov_nuclear_bombs_event_triggers.txt:13-20`), while its annex cleanup clears Soviet transient requests/projects and leaves site ledgers (`023_sov_nuclear_bombs_runtime_effects.txt:1814+`). This source separation is directionally consistent with stopping Soviet-only activity while retaining local physical custody, but it does not prove every surviving site is reconciled after SOV disappears.

## Proposed parent-owned repair

This is a broad migration across 82 transfer commands, two static releases, dynamic release and terminal gates, plus Event 23 site and country accounting. It is not a safe narrow helper extraction for this subagent's read-only scope.

1. Define a bounded transaction for each Event 5 state-transfer tranche before any `transfer_state_to` or `release`. Use the existing registered state and existing snapshot/reconcile helpers where their scope and gate fit. Do not invent a persistent event target. For direct state transfers, take the snapshot in that exact state scope before the transfer and reconcile the same state after ownership/controller settle. For releases, enumerate the actual affected registered states before the release and reconcile the resulting owners/controllers after it. Ensure an interrupted or empty tranche cannot leave the one-global-pending lock stale.
2. Include the two KAZ releases and the progressive, active high-chaos, terminal, and forced terminal call chains. Adjust the Event 23 gate so terminal transfer snapshots can run while a live ledger exists, without reopening Soviet-only gameplay or terminal Fallout actions. Prove repeated competing successor transfers of states such as 200, 226, 248, 256, 405, 584, 742, 827, and 828 are sequential transactions rather than double transfers.
3. Extend the frozen receipt or adjacent bounded receipts to cover every Part 6 field actually affected by the tranche. Keep physical devices, technical access, command formation, and delivery integration distinct. A state owner change alone must grant none of the latter three. Preserve pending native reservations and exact nonce/state callback correlation. Reconcile recorded owner/controller/holder and actor ledgers against pre-transfer buckets, not only the global bucket sum.
4. Keep tuning constants unchanged unless a verified field needs new tuning. This is an accounting and lifecycle repair, not a balance change. Use state and actor variables already present where possible. Persist per-state snapshot generation and completion so save/reload and repeated waves remain idempotent. Clear stale pending state flags and global pending counts only after a proven transaction outcome.
5. Validate named scenarios for a registered storage state in a progressive successor transfer, a competing successor state in high-chaos terminal collapse, both static KAZ releases, a non-storage reactor/test/command/delivery site, a pending native reservation, an ownership-only release if the engine permits it, an interrupted/reloaded tranche, and SOV annexation with surviving local custody. Compare device totals, per-site buckets, current physical holder, native stockpile removal/dispute receipts, and independent stage flags before and after. The user owns live-game validation; the parent owns source and MCP validation.

No new helper names or constants are proposed here because the parent must first choose the exact transaction seam and prove the runtime ordering. The direct migration targets are the 34 `soviet_collapse_spawn_*_if_enabled` helpers, the two KAZ sites, and the four existing wrapped dynamic releases. Existing Event 23 snapshot and reconciliation helpers are the starting call-site contract, subject to the terminal and coverage corrections above.

## MCP evidence and limitations

The required read-only event and map routes were attempted. `hoi4.event_inspect` rejected a string selector with `expected object`; it then rejected `{kind:"event",id:...}` with `expected string at selector.eventId`, establishing the live selector shape. The corrected `hoi4.event_inspect({mode:"roots",selector:{kind:"event",eventId:"chaosx.nr5.1"},maxNodes:20,maxEdges:30})` reached the server but returned `timed out awaiting tools/call after 180s`. A whole-workspace `mode:"scan"` also failed to yield and was terminated before a result. `hoi4.map_inspect({stateIds:[248,253,195,200,226],includeOverview:false})` independently returned `timed out awaiting tools/call after 180s`. No source revision, coverage graph, map artifact, rendered event path, or runtime comparison was produced. Source-only findings above are not presented as engine evidence. No probability-bearing helper or weight was designed or changed, so the probability audit route was not invoked.

**Meaningful validation run:** exact literal-command inventory and call-chain trace over the two Event 5 scripted files, direct comparison of the snapshot gate and callbacks against the 82-site family, and vanilla syntax/scope references. **Skipped meaningful validation:** MCP event/map results, save/reload conservation, callback ordering, per-site runtime owner/controller transitions, and SOV extinction scenarios because the read-only service did not return evidence and the user owns live-game validation. No simplification of the requested design was implemented.
