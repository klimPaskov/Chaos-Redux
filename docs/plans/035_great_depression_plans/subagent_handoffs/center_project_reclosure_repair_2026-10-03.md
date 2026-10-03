# Event 35 center-project reclosure repair

## Disposition

Accepted implementation under the user's full Event 35 package and its mapped center lifecycle.
The bounded source repair is implemented and ten actual-source scenarios pass.
The isolated execution handoff and source comparison have been parent-reviewed.
The mandatory MCP comparison returned `PROBABILITY_SURFACE_EMPTY`; its changed-helper surface has no weighted-source adapter, so numeric/native decision eligibility and balance remain unresolved.
No full Event 35 completion claim follows from this tranche.

## Implemented contract

Country-only `exists` checks are removed from the two state selectors and the selection effect.
The shared current-registration predicate instead requires a coherent acting country, an exact state episode, and membership in that country's registered state array.
The explicit transfer-selection branch requires a live open transfer contract and receiving registry capacity.
Selection adopts the state before publishing the selected pointer.

Historical completed work does not close an idle project slot.
Every new valid paid authorization increments a state-scoped serial and records its current episode.
Completion and failure each spend that authorization once, independently of the historical completion/failure flags.
Completion also requires control, ownership, and actual accumulated work at the configured total duration.
Active work, paused work, certification, and the national project slot still block another authorization.
The original score coefficients, AI bodies, costs, action relief amounts, and durations are unchanged.

Physical transitions preserve the live center episode.
Project stage/type/timing changes mirror into the existing aligned country project columns.
Reopening counts once per state and episode, Lasting Capacity has a distinct one-shot receipt, and a lost center can queue reconstruction construction once per episode.
Treatment removal cannot reset those receipts.
Matching terminal cleanup clears the live project and center identity but preserves the authorization serial and last spent IDs as compact state history.
The broad controlled-state receipt/stage cleanup is removed so another actor's live center is untouched.

Transfer reconciliation pauses only actual pending work before releasing its slot; losing an unrelated center cannot cancel another center's project.
Accepted adoption rebinds live state/project episode proof while retaining serial, work, timing, and spent receipts.
The open transfer contract blocks repeated adoption from changing the registry index or adding another row.
A later legitimate transfer can open a fresh contract without replaying an earlier adoption.

Two localized requirement messages describe current recovery-program membership and the national center-work slot.
Private episode, authorization, and transfer guards are hidden rather than exposed as additional player meters.
No asset, sprite, achievement ID, event ID, doctrine, GUI, or catalog wording is introduced by this repair.

## Evidence

The immutable four-source baseline and nine named cases are in `../audit_inputs/reclosure_2026_10_03/` and [the probability baseline](reclosure_probability_baseline_2026-10-03.md).
The isolated decision/mission auditor owns `.tools/test_event035_center_projects.py` and its execution handoff.
The first parent run reached matching-episode terminal cleanup successfully; the remaining cases stopped on explicit interpreter support gaps.
After those gaps and the prevalidated inherited fixture were corrected, the parent independently reran `python .tools/test_event035_center_projects.py`: ten tests passed.
They execute production payment, quotes, receipts, cooldowns, project authorization/processing/completion/failure, physical reclosure, and transfer/cleanup helpers.
The named cases cover paid reopening through Public Works and Lasting Capacity, protection duration, duplicate completion, failure retry, inherited reclosure, active-project and foreign-episode rejection, matching-episode cleanup, completed-history transfer, and pending transfer/replay/second transfer/lost-time exclusion.
The inherited physical mapping fixture explicitly starts from an already validated existing row; it is not full public regional API validation evidence.
Humanitarian pressure is an explicit out-of-scope adapter fixture; native scheduling, modifiers, construction, mission consumption, and live timing remain unproved.

Installed `documentation/triggers_documentation.md:2708-2716` documents `exists` as COUNTRY-only.
The narrow live search and section read both succeeded for workspace `mod_chaos_redux_ea3b2d67c2c0`, section ID `1e3f8f4659110cd807c118f6cab4611811385a392f866b9d72a4a8039ae10cf8`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
Installed `state` and `is_in_array` sections were read directly at lines 7561-7567 and 5672-5684.
Offline scope rules were read at `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:253-269`, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`.
The vanilla and offline targeted-decision precedents are retained in the baseline handoff.

The `chaosx.nr35.8` inspect at depth one and two nodes returned the terminal 600-second timeout.
Its single narrower retry returned `EVENT_INSPECTED_PARTIAL`, at the same revision and graph hash as the render, with zero helper coverage.
The trace artifact URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/084afad4a881aa3a2671c95a56ad923802c129566ba7ed5095416876e51e533d/479b43abb69867b28148605d3c7cd16e6fab384baf9780f2281bc02456179680/event-trace-9ccbdd836093.json`.
The matching state render returned `EVENT_RENDERED_PARTIAL`, revision `9ccbdd8360934a5c62de4ff6b24f48f4ae8b86de67cd6c74835daa85e799b5d9`, graph hash `7b00113029104d74ce4deeaadfae1151cb55ac69df50520e7e825cd8aa7ae4ab`.
It selects one event node and zero helpers; whole-workspace helper/lifecycle passes were deferred and 42981 nodes were omitted.
The four returned artifact URIs are retained in the parent tool result, with JSON hash `380933cb49812f219c8d4bd6a60ce5e72a9884a3fcb53ce2d8e3b525f6b6ca2f` and PNG hash `f2e4c471f02d06cd3d8a3638051e96674455c98eb118bb19fa40fdd8d3524d37`.
The connected static-resource inventory is empty, and the returned files were not found in the configured local workspace artifact store.
Linked detailed artifact and image review therefore remain unresolved; no native helper lifecycle, current-source visual approval, or complete event validation is claimed.

## Remaining accepted work

This repair does not implement the separately audited inherited hidden liabilities, secured-value salvage, corridor resolution, missing finance/transport/international project producers, or full Event 34 per-state history producer.
Those remain accepted and queued or blocked on authentic upstream data as distinguished by [the inherited-consumer audit](inherited_consumer_completion_audit_2026-10-03.md).
Current source tests, native source comparison, map/state and visual consumer evidence, and fresh live error-log proof are not supplied by the existence of the changed source.
No unapproved fallback or balance substitution is claimed.

## Resume packet

The caller-output lifetime tranche is committed as `e191580e4792f73d5925d80ad2d8c01a99b9baba`, with the four mixed index entries and seven fully owned paths reconciled.
Its preserved before/after source hashes are `3B065E7FC529FA4E8A98B7CAF60656ECC2FD22970944B966329986B85D1B1403` and `B9E01DE3EB2CC97FA31E73188745AF77A1EEF28F07D86AC51AC0346385AA28A9`.
The project tranche is ready for the scoped shared-tree commit: source tests and comparisons have a recorded disposition, without claiming full native certification.
Do not launch HOI4, rewrite other agents' work, or remove a Git lock without the required stale-lock proof.
