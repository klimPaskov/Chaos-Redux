# Shared forced-event failure report handoff

Disposition: implemented within the delegated hook scope, with owner call sites and Settings context wiring remaining with the parent.
Acceptance basis: parent delegation on 2026-10-05 authorized the shared failure report, then approved a six-reason numeric catalogue and native conditional descriptions after reference review found no documented country-event description override.
No arbitrary localisation-key injection, scripted-localisation getter, dummy idea registry, GUI edit, workbook edit, or commit was used.

## Files and public contract

- `common/scripted_effects/chaosx_forced_event_feedback_effects.txt`: COUNTRY helper `chaosx_report_forced_event_failure`.
- `common/script_constants/chaosx_forced_event_feedback_constants.txt`: categories `forced_event_feedback_reason` and `forced_event_feedback_timing`.
- `events/chaosx_forced_event_feedback.txt`: native country report `chaosx_forced_event_feedback.1` with one inert acknowledgement.
- `localisation/english/chaosx_forced_event_feedback_l_english.yml`: eight plain-text keys for title, six descriptions, and acknowledgement.
- `common/scripted_effects/chaosx_dynamic_effects.md`: surgical appended helper contract, usage, lifecycle, and limitations.

Set temporary `chaosx_forced_event_failure_reason = constant:forced_event_feedback_reason.no_country` in the calling effect block, then call `chaosx_report_forced_event_failure = yes` from the actual country-scope failure branch.
Available reason keys are `no_country`, `no_state`, `no_target`, `already_active`, `unavailable`, and `dispatch_failed`.
The caller must set the reason input immediately before each call and should select the most specific known cause.
The helper reads it without changing it.
The first draft used a dollar-macro argument, which was removed after the offline scripted-effect documentation and vanilla/repo precedents established the native caller-variable convention.
Unexpected numeric input uses the generic failure description.
Catalogue numbers are stable identifiers and carry no probability or balance semantics.

The hook requires regular `event_target:chaosx_manual_event_requester` to exist as a human country with `chaosx_manual_event_requested` set and `chaosx_manual_event_failure_shown` absent.
It writes the requester's normal `chaosx_manual_event_failure_reason`, sets its report receipt before dispatch, and fires the report immediately.
The current country may be the requester or an entirely different event target country.
The helper never derives the requester from ROOT, FROM, or a global pointer.
Natural events without request context produce no popup.
Only the first failure in a request is reported.

## Parent wiring and cleanup

Before every manual dispatch, clear requester flag `chaosx_manual_event_failure_shown`, optionally clear its reason variable, save the requester as regular `chaosx_manual_event_requester`, and set requester flag `chaosx_manual_event_requested` for `constant:forced_event_feedback_timing.request_window_days`.
Stage that constant through a temporary variable before passing it to the timed flag's `days` field.
The request window is two days.
Keep owner failure callbacks in the originating event chain and inside that window.
The regular target automatically expires with the chain.
There is no global event-target cleanup or periodic hook.
The acknowledgement changes no flags or variables so acknowledging an old report cannot reset a newer request's receipt.
Settings owns receipt reset at the beginning of each new request.

Migration: owner failure branches should call the helper instead of silently returning, using a catalogue reason.
Owners retain eligibility, effect application, and gameplay rollback.
The hook does not undo partially applied gameplay or report successful event firing.
No call-site files were edited by this worker, as the parent explicitly owns them.

## References

Paths below identify the installed game root `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/` or mod-relative offline wiki files.
Detailed answering sections were read locally, and connected `hoi4.reference_context` returned revision-bound source citations.
Installed documentation remains authoritative.

| Source | Relevant lines | SHA-256 revision |
| --- | --- | --- |
| `documentation/effects_documentation.md` | 2943-2967 country event invocation, 6496-6503 saved target, 6730-6738 flag, 7888-7908 variable assignment | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `documentation/triggers_documentation.md` | 2110-2135 variable comparisons, 2708-2716 country existence, 3844-3852 event target, 5244-5252 human/AI | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `documentation/script_concept_documentation.md` | 12-52 bindable localisation, 216-247 shared constants | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `common/script_constants/documentation.md` | 1-32 schema and scoped variable access | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` | 60-74 conditional description selection, 194-217 event invocation | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 263-327 event targets and chain inheritance, 953-985 token restrictions | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 4683-4697 native scripted-effect invocation, Useful scripted effects variable-input examples | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Vanilla `events/AAT_Iceland.txt` | 924-950 `iceland_events.17` conditional desc blocks | `26114b8af98adbdb78db9e2491d99b0a995ce4508271722ecdfc9e25d50bf278` |
| Vanilla `common/scripted_effects/SWE_scripted_effects.txt` | 58-77 `lerp` caller-set input variables and scope output | `229750634a47cc5b1e0791a91f6527b75295cc86c0e4e3d5fb81348eb12d8f16` |

`country_event` invocation documentation does not list a `desc` override.
Bindable localisation documentation proves nested replacement for supported tooltip fields and does not establish popup description injection.
The approved native description variants mirror vanilla's conditional `desc` structure.

## Validation and limits

An ephemeral source parser and restricted effect evaluator exercised the actual helper and report definitions, rejecting unsupported commands rather than silently ignoring them.
It was rerun against the final native caller-variable input and confirmed suppression for missing target, natural firing, AI requester, and nonexistent requester, one report after two calls in one request, a fresh report after receipt reset, independent receipts for two requesters, correct descriptions for all six reason values, generic description for an unknown numeric value, unchanged caller input, and an acknowledgement without gameplay or receipt mutation.
This is offline source behavior evidence and does not simulate engine event instances or delayed target inheritance.

Connected `hoi4.reference_context` succeeded for workspace `mod_chaos_redux_ea3b2d67c2c0` and returned both installed documentation and offline wiki references.
Its omitted sources were inspected locally where relevant rather than claimed as read from the context bundle.
Connected `hoi4.reference_read` succeeded for installed `country_event` lines 2943-2967 and offline regular event-target lines 303-328, preserving the revisions above.
Connected `hoi4.reference_search` for `token GetTokenLocalizedKey` failed with `timed out awaiting tools/call after 600s`.
The first event selector used an invalid shape and returned MCP `-32602` with `Invalid discriminator value` at `selector.kind`, so that request is not usable event evidence.
The corrected event selector is `{ kind: "event", eventId: "chaosx_forced_event_feedback.1" }`.
The corrected bounded `hoi4.event_inspect` lint request also failed with `timed out awaiting tools/call after 600s`.
This is an explicit domain-validation blocker, not successful event inspection.
A direct stdio client confirmed `hoi4-agent-tools` server version 3.8.1 and live tool schemas through `C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/dist/bin/stdio.js`.
Configuration is `C:/Users/klimp/AppData/Roaming/hoi4-agent-tools/config.json`.
No native tasks were requested by the client.
The direct `hoi4.script_validate` attempt with an explicit country requester binding timed out with MCP `-32001` after 120000 ms, preventing the later calls in that client sequence from running.
Connected read/search results are retained in adjacent `forced_feedback_mcp_20261005/connected_reference_results.json`.
Exact scope-validation and corrected event-inspection blockers are retained in `forced_feedback_mcp_20261005/validation_blockers.json`.
Connected `hoi4.source_lookup` for the vanilla precedent and the bounded `hoi4.event_render` and `hoi4.event_compare` calls each also failed with `timed out awaiting tools/call after 600s`.
Those final route errors are retained in `forced_feedback_mcp_20261005/domain_route_results.json`.
No domain graph, rendered event proof, comparison, or native scope-validation pass was obtained.
Do not equate a pending call or exposed tool with successful validation.

Native conditional descriptions avoid a shared getter that continually reads the latest country reason variable.
Whether an already open report retains its selected description across a later request remains unobserved engine behavior.
The two-day flag is not a unique delayed-request generation, so overlapping asynchronous requests by one player remain a lifecycle limitation.
No game was launched and no runtime completion is claimed.
The parent retains final owner call-site integration and blocked MCP event inspection/render/compare and scope validation.
The current Settings `no_target` branch uses the final native temporary-input convention, as verified by a bounded source search.

## Assets and future work

The native text report requires no new icon, sprite, picture, or asset wiring.
Future reason additions require matching catalogue constants, report description branches, and localisation.
If an owner needs concurrent delayed requests for one player, add an owner-carried generation identity before extending the callback lifetime.
No unapproved simplification was made.
The approved numeric catalogue replaces the initially requested arbitrary localisation-key input because the required injection syntax was unsupported by the available references.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
