# Event 006 package-incident shown-snapshot lifecycle audit

Date: 2026-10-08.
Role: chaosx_scripted_system_architect, explicitly bounded read-only audit with this report as the only writable repository file.
Acceptance basis: the parent instruction in this task authorizes serialization of each shown A/B generation/package snapshot through origin cleanup, effect-time authority rejection, capture only on valid delivery, release only in `after`, and requeue of an existing current appointment without changing its original due date.
Disposition: lifecycle findings are audited; the engine correction is parent-owned and remains queued pending the parent's implementation and validation.
This report does not close the active full Event 006 goal.

## Source-critical result

The inspected source predicate would permit an old A or B answer to mutate a replacement generation if that generation had delivered the same slot while the old handler remained usable.
`can_resolve_independence_wave_package_incident_a/b` reads only current country state: active origin, current incident-generation equality, delivered, and not resolved.
Neither the guard nor the event's immediate block records which generation/package owns the visible popup.
Origin cleanup removes the old receipts, and new scheduling/delivery reinstates the predicates that the old option reads.
The proposed independent slot lock and preserved shown generation/package are sufficient for the ordinary outstanding-popup lifecycle only if replacement delivery cannot overwrite a still-shown slot and only `after` releases that slot.
They are country-owned storage with an enforced write lifetime, not an immutable scalar payload attached to a native event instance.
This is a source guard/lifetime gap, not an observed native exploit.
Ordinary new-generation A delivery is scheduled 45 days after its opening, B is scheduled 150 days after A's answer, and the documented default popup deadline is 13 days.
Those unchanged delays exceed the remaining ordinary lifetime of an already-shown old popup and constrain natural overlap; the source guard fixtures below intentionally do not model that timeout or establish a normally reachable stale-popup/new-delivery timeline.
The parent is hardening mutable-source authority consistent with the lifecycle contract while preserving these existing timing protections.
An arbitrarily forced replay of a closed handler after the same slot/package has been reused cannot be distinguished by these country scalars alone.
Do not claim that stronger replay guarantee or native execution evidence.

Critical countercases for the parent:

1. Clearing shown snapshots in either origin cleanup caller recreates stale authority after new delivery.
2. Blocking scheduling rather than delivery loses the replacement appointment when a prior popup remains open.
3. Calling the scheduling helper again from closure restarts 45/150-day timing; closure must dispatch against the stored appointment.
4. Releasing both slots from one `after` can let old B overwrite or clear new A's snapshot.
5. Stale `after` must not clear current delivered/resolved flags, current generation, or due dates; it only releases its shown slot and may wake an already-authorized current appointment.
6. Requeue without scheduled, current generation, valid package, due-date presence, and not delivered/resolved checks invents or duplicates work.
7. A stale A answer must not set current A resolved or schedule current B; a stale B answer must not apply costs or rewards.
8. A due old delayed callback for the same currently scheduled package may serve the valid current appointment after the slot is free; capture the current snapshot at this valid delivery and do not claim the callback carried a historical scalar generation.
9. Gating `after` release on `can_resolve` strands the lock after a valid answer because resolved is already set, and after a stale answer because live authority mismatches; close the owned shown slot independently, then separately authorize any requeue.

## Exact inspected surfaces and identities

Hashes describe bytes observed during this audit, not an immutable whole-workspace archive or the parent's eventual patch.
The parent subsequently froze the canonical three raw source copies at `docs/plans/006_independence_wave_plans/evidence_20261008/package_incident_snapshots/frozen_before/`.
I read and hashed each canonical copy; the effects, events, and triggers hashes exactly match the corresponding three entries below.
The confirmed effects hash is `2F66F502066029B0E7FDF2986AF2DDBD977FD59DDD06ABEF780F6CD371A6437B`.
Other later pending-client copy directories are noncanonical and were not used as this audit's baseline.
No manifest file was found in the inspected snapshot/evidence folder inventory at this read; baseline identity is verified from the actual copied bytes and the parent's explicit hash correction.

| Source | SHA-256 | Relevant coverage |
| --- | --- | --- |
| `common/scripted_triggers/006_independence_wave_package_incident_triggers.txt` | `a77ca1b0c34b4a8932c8ae9063f3391764e96049a0c51f77ad65521ab720ed3d` | Entire 47-line file; current delivery and resolution predicates |
| `common/scripted_effects/006_independence_wave_package_incident_effects.txt` | `2f66f502066029b0e7fdf2986af2ddbd977fd59ddd06abef780f6cd371a6437b` | Entire 732-line file; both 65-package dispatcher maps, schedule preconditions, deltas, cleanup |
| `common/script_constants/006_independence_wave_package_incident_constants.txt` | `f78671b983d5f89380ccf678989ada2dd830910049e076cc75784f249897fb4f` | Entire 17-line file |
| `events/006_independence_wave_package_incident_events.txt` | `6970a3e7c80682231da7173ad1003ded0ecef6bd4ca9e6dd4d57ed4a1212b708` | All 130 parsed event definitions and all 260 option guard structures; 8,519 lines |
| `common/scripted_effects/006_independence_wave_effects.txt` | `1ffa0cc16decdb8c03fee25ceb8163d197697167211d5909bb446c9222e4fff9` | Reset at 468/471, prepare at 715-740, origin end at 3112/3134, package-cleanup dispatcher at 3865 |
| `common/scripted_effects/006_independence_wave_opening_dispatch_effects.txt` | `075c0ffd43e792e05ee3639b858a1eb9ea9749a57874601da31449100d0f99b3` | Existing A schedule callers at 325 and 395 |

Additional pertinent source reads: `common/scripted_triggers/006_independence_wave_triggers.txt:9-14`, `common/scripted_effects/chaosx_dynamic_effects.txt:834-873`, and its matching Markdown date-conversion APIs at 353-420.
Read skills: `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, with the event anatomy, proposal popup lifecycle, helper-output lifetime, ownership, MCP evidence, and cleanup contracts applied.
No skill was changed.

## Source inventory and caller assumptions

The event inventory is exactly `chaosx.nr6.101` through `.142` and `.200` through `.287`: 130 events, 65 A, 65 B, and two options each.
All immediate blocks currently do exactly one phase-specific delivered flag write.
All 260 option gameplay bodies are contained inside the matching `can_resolve...a/b` effect-time guard.
Every option writes exactly one matching resolved receipt, and each of the 130 A options calls `independence_wave_schedule_package_incident_b` once inside that guard.
No B answer schedules another incident.
There are no `after` blocks and no explicit `timeout_days` overrides in these events.
This is a lifecycle/containment inventory, not a reward-balance or AI-probability evaluation.

An in-memory parser traversed all definitions, their nested option effects, and both dispatcher maps; it found no option with gameplay effects outside its top-level resolution `if`, no missing matching resolution guard, and no phase/schedule-count exception.
The parsed option-AI structure digest was `c33e60aa60e7b68e68cc029ff3c96597ba0d93e4e42db1d84ea65cbb3abcd191` (SHA-256 over the ordered Python `repr` of option name / parsed AI-block hash pairs).
This digest is a scope-preservation cross-check, not probability evidence and not a portable serialization standard.

Repository source searches found only these external direct consumers of package-incident lifecycle helpers/receipts:

| Caller | Current assumption | Required preservation |
| --- | --- | --- |
| `independence_wave_reset_current_generation`, effects line 471 | Clear generation-local appointments and delivery/resolution receipts before new origin preparation | Clear live runtime, preserve independently owned shown snapshots/locks |
| `independence_wave_prepare_origin_state`, effects lines 715-740 | Reset first, then assign generation and package | New schedule must never recapture an old shown snapshot |
| `independence_wave_end_active_origin`, effects line 3134 | Invalidate current incident authority with other origin cleanup | No outcome, cost, B schedule, or receipt award on authority loss; preserve shown locks for closure |
| Opening effects lines 325 and 395 | Schedule A once after founding posture | A appointment may exist while old A is locked; delivery remains serialized |
| All A answer effects | Resolve A, apply unchanged consequences, schedule B once | Schedule B only for a matching current shown snapshot |
| Statehood incident effects | Reuse `independence_wave_package_incident_clear_deltas` | Keep this separate helper's temporary-delta contract unchanged |

No external direct consumer of the A/B delivered, scheduled, or resolved flags was found outside the package-incident files.
The current delivered flag acts as a live generation receipt, not a durable shown-popup lock.
The two cleanup callers deliberately assume mutable live receipts and can retain that behavior after shown storage is separated.
The package cleanup dispatcher precedes incident cleanup in both callers; the source search found no dispatcher consumer of package-incident receipts and no blanket `clear_variables` in the inspected origin effect file.
This is bounded source evidence, not a guarantee about undocumented engine removal of popups or unrelated future callers.

## Recommended helper contract

Names below describe a concrete local helper map for the parent, not implemented definitions.
Every helper runs in the recipient COUNTRY scope.
Generation, package, due date, shown storage, scheduled, delivered, and resolved state belong to that same recipient; do not read them from a former host, `FROM`, another country, or scoped temporary variables.

| Helper / family | Inputs | Outputs | Side effects and call sites |
| --- | --- | --- | --- |
| Existing `can_deliver_independence_wave_package_incident_a/b` | Current active origin, matching incident/current generation, current scheduled receipt and due date, unresolved/undelivered slot, no shown-slot lock | Boolean | Read-only; all 130 native event triggers retain their existing package selector and add lock enforcement through this helper |
| Proposed `independence_wave_package_incident_mark_shown_a/b` | Existing valid delivery context, no existing slot lock, current generation and package | Normal shown-generation and shown-package variables plus shown flag | Capture once at valid immediate delivery; set current delivered receipt; defensively recheck delivery before writing; never called by scheduling or cleanup |
| Existing `can_resolve_independence_wave_package_incident_a/b` | Existing live authority, delivered and unresolved, shown flag, explicit presence of shown/current generation and package fields, matching shown/current generation and package | Boolean | Read-only; all 260 option bodies continue to recheck here before any debit, reward, resolved receipt, or B schedule |
| Proposed `independence_wave_package_incident_close_shown_a/b` | Owned shown slot, event's expected package identity where needed to guard an accidental mismatched closure | Released shown fields/lock | Called only by that phase's native event `after`; releases only that slot and attempts requeue of an existing current appointment; no live receipt/duedate reset or reward logic |
| Proposed `independence_wave_package_incident_requeue_a/b` | Active current authority, current scheduled appointment, mapped current package, present original due date, undelivered/unresolved, free shown slot | A dispatch delay based on remaining time to the same due date | No new appointment; dispatch current mapped event with original due date unchanged; reuse existing date-unit constants for remaining hours; do not call initial scheduling helpers |
| Parent-selected numeric selector helpers, one per phase | Current mapped package and caller-initialized temporary event-ID output | Original numeric A/B event ID, or zero/unmapped rejection | Mechanically extract each original 65-entry map; never allocate a new event, capture a shown snapshot, or grant an outcome |
| Existing `independence_wave_clear_package_incident_runtime` | Origin reset/end | Cleared current generation, A/B scheduled/delivered/resolved flags and current due dates | Preserve shown-generation/package variables and shown locks; existing two cleanup call sites remain |

Use distinct normal fields such as `independence_wave_package_incident_a_shown_generation`, `...a_shown_package`, and B equivalents, with separate untimed `...a_shown` / `...b_shown` flags.
The normal fields are necessary across immediate, option, origin cleanup, and after boundaries; temporary scalars cannot serve as snapshots.
Presence checks should accompany equality checks so absent fields do not accidentally compare as zero.
Scheduling may update only the current appointment and its current-generation receipt, never shown fields.
Keep the scheduled flag write even when that slot's shown lock is held; locking delivery must not suppress the appointment.
The dispatch caller initializes the temporary numeric event-ID output before the selector call and rejects an unset/unmapped result instead of reusing an earlier selection.
The temporary output is unscoped, so do not prefix it with ROOT/PREV; the selector reads the recipient's normal package variable.
Use a static `chaosx.nr6` namespace in the parent's meta country_event text and interpolate only the original numeric suffix as an integer.
These metadata numbers are the original native event IDs, not new content or per-event generation payloads.
Wrap snapshot-capture metadata writes in hidden effects so stored identity does not add player-facing outcome text.
Mark resolved inside the existing accepted option transaction before further outcome helpers to retain same-generation one-use behavior.
Do not clear a current delivered/resolved flag when releasing a stale shown lock.
Do not add a timed flag that expires independently of actual popup closure.

### Constants and timing

Keep `independence_wave_package_incident.first_delay_days = 45`, `second_delay_days = 150`, `political_power_requirement = 35`, and `political_power_spend = -35` unchanged.
Keep all existing package IDs, outcome constants, and AI coefficient categories unchanged.
No new balance tuning value is needed for the lifetime invariant; flags express booleans and normal variables express identity.
The parent's selected selector metadata may centralize the original 130 numeric event IDs without changing their package mapping or event content.
Keep initial 45/150-day scheduling and stored dates in their existing units.
The parent's selected closure path computes remaining native hours as `(original_due_date - global.date) * constant:chaosx_date_units.hours_per_date_unit`, clamps a past date to zero, and queues with `hours` instead of rounding the remainder into whole days.
Initialize any selector or delay output consumed after a helper call in that caller, and leave the stored original due date untouched.
One hour is 0.00001 encoded date units; 45 and 150 days are respectively 0.0108 and 0.036 encoded units, corresponding to 1080 and 3600 hours.
For an already-due appointment, the remaining delay is zero; do not silently impose a fresh 45/150-day duration or invent a minimum delay.
Native zero-delay ordering/reentrancy is not established by this audit, so the parent's implementation must keep snapshot release before dispatch and retain delivery guards regardless of callback order.

### Event targets and cleanup

No new event target is needed for generation/package scalar identity.
An event target is a scope pointer and does not create an event-instance scalar snapshot.
Keep existing former-host targeting/outcome behavior unchanged.
Origin end/reset clears current appointment authority but preserves any currently shown slot for its original closure.
The matching `after` clears that slot's normal shown fields and flag, then checks for an existing current appointment of that slot.
Do not require the current reply predicate for this release: both a resolved current option and a rejected stale option still require closure.
Inactive origin, absent appointment, absent due date, unsupported current package, already delivered, or already resolved means closure alone, with no scheduling, costs, rewards, or native appointment invented.
A country disappearing while its popup is open may involve native cancellation semantics not covered by this source model; this audit does not prove that `after` runs in every such engine path or authorize a periodic/forced-expiry substitute.

## Source-bound scenarios and replay limits

The actual-source guard fixture parsed the production package-incident triggers and evaluated their recursive Boolean, presence, flag, equality, and due-date comparisons.
It supplied the active-country predicate as an explicit true/false fixture input; the underlying authority source was separately inspected at `006_independence_wave_triggers.txt:9-14`.
It did not execute native event delivery, cleanup callbacks, timed expiry, resource debits, rewards, package helper bodies, save persistence, or the parent's unimplemented snapshot patch.
Sixteen actual-source guard cases were run, eight for each slot, with all expected results reproduced:

| Case, for A and B independently | Current delivery guard | Current resolution guard |
| --- | --- | --- |
| Current scheduled appointment exactly due, not delivered | true | false |
| Current appointment before due date | false | false |
| Current delivered, unresolved | false | true |
| Current delivered and resolved / duplicate answer | false | false |
| Origin inactive | false | false |
| Incident generation differs from current generation | false | false |
| Old popup still open; new generation scheduled and due but not delivered | true | false |
| Old popup still open; new generation delivered and unresolved | false | true: stale acceptance reproduced |

The last two cases distinguish the bug precisely: a fresh schedule alone does not authorize the old answer, but a fresh delivery does.
Cleanup and generation replacement were represented by fixture states justified by the inspected cleanup/preparation source, not by a native interpreter.
In particular, the fixture can supply a new due/delivered state while retaining an old handler because it has no native popup deadline; that setup proves the guard result only, not normal 13-day-versus-45/150-day overlap.
Five additional actual date-helper arithmetic cases reproduced 45-day and 150-day encoded offsets/roundtrips, one-hour remainder rounding to one day in the existing days converter, and zero/past-date remainder clamping to zero.
That small Decimal source model supplied the round primitive, did not emulate native fixed-point or scheduler behavior, and did not test the parent's pending remaining-hour/meta dispatcher implementation.
The one-day rounding case explains why the parent chose direct remaining-hour dispatch instead of the days converter for closure requeue.

Required post-patch source scenarios for the parent:

| Scenario | Required result |
| --- | --- |
| Valid current A reply, either option | Exactly one unchanged A outcome; current A resolved; exactly one B appointment at reply date plus 150 days |
| Valid current B reply, either option | Exactly one unchanged B outcome; B resolved; no further appointment |
| Same-generation duplicate reply before closure | Resolved guard rejects a second cost/reward/schedule |
| Early A/B delayed callback | No delivery or snapshot capture; existing scheduled appointment and original due date retained |
| Duplicate callback after delivery | No second shown popup and no snapshot overwrite |
| Old A open, cleanup/new generation, new A becomes due | Old A snapshot retained; new A delivery blocked; old reply rejected; old A after releases slot and wakes current A against its original due date |
| Old B open, cleanup/new generation, new B becomes due | Symmetric B behavior; stale B cannot debit or reward current country |
| Old B open while new A opens | B lock does not block A; A snapshot remains independent |
| New A resolves while old B is open | Legitimate current B schedule/due date created once; B delivery blocked until old B after; B date not restarted |
| Old B closes before new A resolves | No B appointment exists yet, so close must not invent B; later valid A reply schedules B normally |
| Old B closes before current B due date | Requeue to original due date, leaving current A state untouched |
| Old B closes after current B due date | Current B delivery may proceed once; original due date remains unchanged |
| Stale close after origin end with no replacement | Clear shown slot only; no current appointment created |
| Package changes while a report is open, even if generation coincides | Shown/current package mismatch rejects consequences; replacement dispatch uses current mapping after old closure |
| Old delayed callback coincides with a due current same-package appointment | It may coalesce with that appointment; capture current generation/package on valid delivery; later duplicate callback rejected |
| Native timeout | Documented first-option selection at default 13 days, guarded like any answer, then ordinary after closure; no special timeout branch |
| Forced old option/after invocation after closure and slot reuse | Cannot be proven distinguishable without an event-specific payload; do not present a country-slot model as arbitrary replay protection |

The timeout contract is not a change to the first option, its rewards, its visibility, or AI coefficients.
The offline wiki documents option visibility at firing, so stale-reply safety must come from the effects recheck rather than dynamically hiding an already-shown option.
Some existing paid options also have firing-time resource visibility checks without repeating those checks in their effect guard (for example `.102.a` political power, and `.114.a` manpower).
Resource loss while an otherwise-current popup stays open is a separate existing source contract risk; this bounded generation fix must not quietly redesign cost/choice behavior.
This audit does not evaluate how native resource effects clamp or permit a resulting deficit.

## Migration and preservation checklist for the parent

1. Add independent shown-slot storage and lock enforcement in the existing trigger/effect families; keep current appointment fields and cleanup ownership separate.
2. Replace the 130 one-line immediate delivered writes with valid-delivery capture through the matching helper.
3. Add phase-specific after closure to all 130 existing event definitions.
4. Keep the current 260 option guards at the same outer effect boundary and strengthen their shared predicate; retain every choice name, custom outcome tooltip, outcome body, cost coefficient, and AI block.
5. Reuse/extract the existing dispatcher maps for requeue without altering the 65 package mappings per phase or the initial scheduling durations.
6. Update lifecycle comments/docs: the current header claim that an incident fires only for the generation that scheduled its native callback is stronger than the actual source, which checks current appointment state and allows valid due coalescence.
7. Document helper purpose, COUNTRY scope, inputs, outputs, defaults/rejection, side effects, write ownership, and direct call sites in the matching helper Markdown document under the parent's edit ownership.
8. Repeat the source scenarios above against the actual parent patch, and retain matching read-only event inspection/render evidence for the patched revision; structural MCP graphs do not prove native popup ordering.

No new content, extra on_action, fallback, generic router, balance target, revised outcome, or AI coefficient is recommended.
No helper, constant, gameplay call site, localisation, asset, or cleanup script was edited by this audit.

## References and MCP evidence

The connected tool catalog exposed `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, and the read-only event inspect/render/compare routes.
The workspace returned by successful reference calls was `mod_chaos_redux_ea3b2d67c2c0`.
Initial argument-validation rejections were request-shape issues, not service-health evidence: context question exceeded 160 characters; event selector omitted `kind`; then a file selector supplied `path` where the live schema requires `sourcePath`.
The calls were corrected without editing tool source or gameplay source.

| Reference | Read spans | Source revision / authority | Rule used |
| --- | --- | --- | --- |
| Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` | 180-191 through MCP read; 152-157 and 194-219 also read locally | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` | Immediate before choice; after after choice; default 13-day first-option timeout; firing-time option/event predicates |
| Installed `documentation/effects_documentation.md` | 2943-2967, 7888-7909 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | COUNTRY-scoped delayed country_event; copy a scalar variable into normal storage |
| Installed `documentation/effects_documentation.md`, meta_effect | 4833-4852 locally and through MCP read | Same installed effects revision above | Build a literal static-namespace event ID from a numeric selector output |
| Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 900 locally and through MCP read; 4617-4646 locally | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` | Variable-capable country_event hours/days and integer interpolation in meta text |
| Installed `documentation/triggers_documentation.md` | 2110-2135 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` | Variable equality and inclusive due-date comparison |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 263-264 and 435-449 locally | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | Event targets point to scopes; normal versus temporary variable lifetime and country scoping |
| Installed `documentation/script_concept_documentation.md` | 216-246 locally | SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` | Shared script constant semantics and field support limitations |
| Installed `common/script_constants/documentation.md` | 1-35 locally | SHA-256 `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` | Schema and constant access; no new tuning required |
| Vanilla `events/BFTB_Turkey.txt`, `bftb_turkey.134` | ID at 5616, after cleanup at 5820-5824 | SHA-256 `ff4a042568909f5f1d0b182420c8d279d10606a11862a58969f5b0f753f1e2c1` | Exact installed precedent for final hidden cleanup in event after; does not prove immutable event payload |

The initial event context bundle had `omittedSources` for Triggers and Localisation.
Trigger coverage was pursued through targeted `check_variable` search/read; context identification alone was not treated as detailed rules read.
Localisation design is outside this lifecycle-only audit; no visible string or formatter changes are proposed.
Successful revision-bound MCP reads include the wiki Additional arguments section (`1246e500e0d8629c3754e467c38df46fb39631da0c1c45e49c2c8f6b3e03003e`), installed country_event (`1f4546bec1afc40d54e3560aed92b5add03afd3efe6fc0b5aee7a58a323baf61`), and installed check_variable (`eba1cc3a7863a60b1ffcb1293508be9a3228770609e2e9569a2cec95215f8a2c`).
These reads returned complete relevant sections with `nextLine = null`.
After the parent clarified the meta/hour dispatcher, a targeted `meta_effect` reference search and read succeeded for section `538e21a9904d554de4737ee4cbf42e988513632ceb28741ea399f27e3c2babcb`, installed revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, lines 4833-4852, with `nextLine = null`.
A targeted wiki country_event row read also succeeded for General section `917d9d18ecc613b8b23c08a2e65433a0808fce5ba4fc936340dacfc222c51863`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, line 900; its `nextLine = 901` is outside the requested token row and was not needed for this contract.
These later reference successes do not supply the missing event-domain inspection artifact.

The corrected event inspection request was `mode = state_flow`, `selector = { kind: file, sourcePath: events/006_independence_wave_package_incident_events.txt }`, `expandHelpers = false`, `maxNodes = 150`, and `maxEdges = 500`.
Its exact final failure was `tool call error: tool call failed for hoi4_agent_tools/hoi4.event_inspect; timed out awaiting tools/call after 600s`.
No graph, event report artifact, source revision, or inspection coverage result was returned for that request.
Required event-domain MCP evidence is therefore blocked, and the source findings above are not a substitute for it.
Event rendering was not run after the required matching inspection failed; no rendered or native popup evidence is claimed.
Event comparison was not run because this agent changed no event source and had no successful recoverable graph baseline.

`hoi4.source_lookup` for `independence_wave_clear_package_incident_runtime` succeeded at workspace-index revision `e48072d49d9032bcd239a6c3e1f0b0b8b02741a1b9fdcf519630dc7a080b36f8`.
It returned one non-overridden/non-shadowed definition at `mod:common/scripted_effects/006_independence_wave_package_incident_effects.txt:722-732`, with complete definition coverage and no skipped sources.
Its usage results were not complete: `referencesComplete = false`, `referenceCount = 0`, and `unresolvedReferenceCount = 20107`.
The caller inventory is consequently grounded in the direct repository source search, not a claimed complete MCP reference graph.
No artifact URI was returned by the successful reference/source lookup calls.

The targeted installed `Script Constants` reference search also ended with `timed out awaiting tools/call after 600s`.
Additional targeted `Variable types` and `Options` wiki searches and vanilla `bftb_turkey.134` source lookup ended with the same 600-second tools/call timeout.
Their pertinent source sections and the exact installed vanilla after precedent were read locally; no successful MCP retrieval for those failed requests is claimed.
The pertinent installed local documentation was read directly and its hashes are listed above, as allowed for an unavailable reference route.
This reference retrieval gap does not establish that script constants are unsupported by the game.
The three primary gameplay file hashes were rechecked after the report draft and still matched the audited source identities.

## Completion, omissions, and blocked or unsupported analysis

Completed source work: the precise stale A/B countercase, all-event guard/slot inventory, current dispatcher coverage, caller/cleanup review, exact slot-lifetime architecture, date-preserving requeue contract, and bounded actual-source guard cases.
Only this assigned report was written; no Git or index operation was performed.
No simplification or fallback was applied.
Engine patching, helper documentation edits, actual post-patch source replay, and final full Event 006 acceptance remain parent-owned.
Native popup lifetime, cancellation on country disappearance, persistence, zero-delay ordering, resource-effect behavior, and arbitrary post-closure forced handler replay are unsupported by the performed source model.
No game was launched, and no game/log/save request was made.
AI weights and reward balance were outside this bounded audit; no probability result or specialist AI evidence is claimed.
If the parent changes a probability-bearing coefficient or weighted predicate, the required `chaosx_ai_probability_auditor` baseline and matching comparison remain mandatory.

## Post-patch independent source review, 2026-10-08

Acceptance basis: the parent's follow-up in this task reports application of the three engine files and requests an independent report-only review of source-critical lifetime, date/meta dispatch, and current-appointment constraints.
The earlier source hashes, unimplemented helper proposals, queued implementation status, and timeout findings above are the pre-patch audit record; this appendix describes the inspected parent patch.
Disposition: the bounded lifecycle correction is implemented in source and independently checked within the explicit initialized-origin / one-outstanding-popup-per-slot contract.
No source-critical regression was found within that contract.
Native popup timing, event-instance identity, arbitrary post-closure replay, cancellation, and persistence are still not proved.
The full Event 006 goal remains parent-owned and active.

### Current source identities and coverage

| Parent-edited source | SHA-256 | Coverage |
| --- | --- | --- |
| `common/scripted_effects/006_independence_wave_package_incident_effects.txt` | `e760c2d3d2aab3923ce45a6e5e8d8f4f20e9bcf5a63aa9e14ff307f12d1c15ad` | 725 lines; both selectors, initial schedulers, queue/capture/close helpers, and cleanup |
| `common/scripted_triggers/006_independence_wave_package_incident_triggers.txt` | `71f8855721c0aaa1d48a223d1cfe961db0b230250c21f24c9044a25abfdd3fa2` | Entire 60-line delivery/reply contract |
| `events/006_independence_wave_package_incident_events.txt` | `0cdfe730fa131af45af5d1e358c1a0587f41d5f39d4146b3f75de00f8fb26b35` | All 130 event definitions, 130 immediate hooks, 130 after hooks, and 260 original option blocks |

The comparison baseline remains the canonical `evidence_20261008/package_incident_snapshots/frozen_before/` raw copies under this event's plans folder.
The noncanonical `before/` folder was not read or used.
Both original schedule maps were extracted from the frozen actual source and compared against the new actual selector bodies.
All 65 A and 65 B package-to-event-ID associations match exactly.
Sorted JSON mapping digests (SHA-256 over Python `json.dumps(mapping, sort_keys=True)`): A `6641ed1989a2748c5662926c0a228eb78382387eeebd43adb341059611ea75e2`, B `734fe9393ff7d2889f4833c45d8db3e97b4a53004bfa78c6555df4f1d058b9fb`.
All 260 option blocks were compared as raw decoded UTF-8 source slices, retaining source newlines, from `option` through its closing brace; every block is byte-identical to its frozen counterpart.
The concatenated option-byte digest is `7964710aa7d827e02cdb7644f9e9c101a259ffc895372c09217868ab8d439efa`.
This establishes unchanged source AI blocks, costs, rewards, names, and custom outcome tooltips; it is not an AI probability or native economic evaluation.
All other per-event fields besides immediate and after also match structurally against the frozen source.
Every immediate calls the phase-correct `capture_a_shown` or `capture_b_shown` inside `hidden_effect`, and every after calls only its corresponding `close_a_shown` or `close_b_shown` helper.

### Actual helper and ownership review

| Helpers / source lines | Independent finding |
| --- | --- |
| Initial A/B schedulers at effects 18-64 | Select only a known package, register generation plus original encoded due date and scheduled flag, then attempt queue; a shown lock prevents only native queue/display, not appointment registration |
| `independence_wave_package_incident_select_a_event` at 100 and `...select_b_event` at 363 | Outputs are original numeric event suffixes; all 130 mappings preserved; unknown packages leave the caller-owned zero intact |
| Queue A/B at 627-653 and 677-703 | Require active/current incident authority, package presence, scheduled receipt, due-date presence, and absence of delivered/resolved/shown; reselect a mapped package before dispatch; never overwrite due date, generation, or scheduled receipt |
| Capture A/B at 655-663 and 705-713 | Recheck valid due delivery, then write shown flag, normal shown generation and package, and delivered receipt; shown lock prevents a second capture/overwrite |
| Close A/B at 666-674 and 716-724 | Gate only on that slot's shown flag, clear only that slot's snapshot and lock, then call its queue helper; do not require live reply authority, clear current receipts, restart timing, or touch the other slot |
| Cleanup at 86-96 | Clears the original generation-local appointments/receipts and explicitly retains shown locks and normal snapshots |
| Reply triggers at triggers 40-60 | Require active current incident authority, shown lock, both shown-field presence checks, shown/current generation equality, shown/current package equality, delivered, and not resolved |

The four selector consumers are the two initial schedulers and two queue helpers.
Each writes `independence_wave_package_incident_event_id = constant:chaosx_date_units.zero` before its selector call, then consumes the selector output afterward.
This is the required caller-owned temporary lifetime contract; no scoped temporary field or surviving helper-private output is assumed.
Remaining-hour storage is created in the queue helper and consumed by meta text in that same helper frame.
Normal shown scalars and the shown flag are not reset by initial scheduling, generation cleanup, or current appointment creation.
A repository source search found no new external writer/caller of these shown fields or selector/queue/capture/close families outside the three incident files.
The unchanged origin reset/end call sites consequently still invalidate live authority while retaining shown state for closure.

The native event ID remains literal `chaosx.nr6.[INCIDENT]` before meta substitution: the namespace is static and only the existing numeric suffix is formatted with `|.0`.
The `hours` token comes from `(stored_due_date - global.date) * constant:chaosx_date_units.hours_per_date_unit`, clamped at zero and formatted with `|.0` in the same meta block.
With the existing hour-aligned date encoding, one hour is 0.00001 and the shared multiplier is 100000, so a whole-hour difference becomes an integer; the source model confirms the selected boundary cases below.
No unsupported assumption that a native country_event callback carries a scalar generation was introduced.
Queue helpers authorize a current country-owned appointment, not the historical identity of whichever delayed callback reaches the valid event trigger.
Duplicate pending callbacks can therefore coalesce at valid delivery; the shown/delivered receipts prevent a second source-authorized delivery.
There is no new world poll hook.

### Independent actual-source scenarios

The in-memory interpreter executed the actual patched incident helper bodies, actual patched trigger bodies, and actual shared date conversion helper bodies.
It loaded only the relevant actual constant categories and conservatively discarded temporary fields first created in a returning helper while retaining changes to caller-owned fields.
The first fixture loader failed to obtain a registry category; it was corrected to read bounded actual categories and rerun, without replacing production helpers with no-ops or changing source.
Native active-country authority was supplied as a fixture Boolean; its underlying existing source was already inspected in the pre-patch audit.
Rounding and native meta scheduling were supplied primitives, with meta substitution recorded as concrete event ID/hour pairs.
Reward/resource bodies were not executed; the representative valid-answer transition used the exact resolved-receipt write and production B scheduler, while all original option blocks were independently byte-compared.
These are source contract cases, not native popup/scheduler observations.

| Source scenario | Independent result |
| --- | --- |
| All 130 selectors with caller-owned temporary output | Each returns its original numeric event ID despite conservative helper-frame cleanup |
| Initial A | `chaosx.nr6.101`, 1080 hours, original 45-day encoded due date |
| Early delivery, one hour before A due | No shown snapshot or delivered receipt captured |
| Valid current A capture and repeated capture | First capture permits reply; repeated capture preserves the first snapshot |
| Current A resolves once, schedules B, then closes | B queued for 3600 hours; second reply rejected before slot reuse; A after clears shown only, preserving resolved |
| Old A shown, cleanup/new generation, current A scheduled while locked | Old snapshot survives; new due date/scheduled receipt exist; no queue while locked; stale reply rejects |
| Old A closes 13 days after a replacement A appointment was created | Current event queues for 768 hours (32 days), with its original due date unchanged |
| Symmetric old B / replacement B case | Stale reply rejects; closure queues 3288 hours (137 days) after the same 13-day fixture interval; original B due date unchanged |
| Old B open alongside current A | Current A capture/reply remains independent; old B reply rejects |
| Current A resolves while old B holds B lock | Production B scheduler records its 150-day appointment without queueing; old B after queues B for 3600 hours while preserving current A snapshot/resolved state |
| Unknown package, either initial scheduler | Selector output stays zero; no native queue, scheduled receipt, or fabricated due date |
| Inactive origin, mismatched generation, absent due date, unknown package, absent scheduled receipt, delivered, resolved, or shown | Eight invalid queue states per slot reject without changing normal country state |
| Overdue appointment, either slot | Queue formats zero hours and preserves stored due date |
| One-hour future appointment, either slot | Queue formats exactly one hour, with no whole-day rounding |
| Repeated initial scheduler | Existing scheduled receipt retains original due date and does not issue a fresh native queue |
| Same-generation package mismatch | Snapshot/current package inequality rejects the old reply |
| Inactive stale closure and repeated close before reuse | Release only the owned shown slot; no queue without authority; repeated close does nothing |
| Current A or B answer followed by resolved closure | Reply is one-use; closure releases shown without requeueing the resolved slot |

The old-B/new-A fixture intentionally retains old B while advancing the symbolic source clock beyond normal native expiry so it can examine independent slot behavior.
It does not establish that this overlap naturally occurs with the unchanged 13-day popup deadline and 45/150-day schedules.
Likewise, the 13-day closure cases set the symbolic date directly; they do not emulate a native timeout callback.
An arbitrarily replayed old option or after after that slot has been released and reused is still outside the proven contract because the source owns country slot storage, not an immutable per-event scalar payload.

### Parent follow-up and validation limits

Source-critical status: no outstanding regression found in the specified initialized-origin/current-appointment lifecycle.
Documentation follow-up: `docs/events/006_independence_wave/package_incidents.md:7-20` still describes the earlier delivered-flag-only lifecycle and omits selectors, shown snapshots/locks, slot after ownership, and remaining-hour requeue.
The helper-file overview at effects line 12 still says cleanup clears every receipt although its later contract correctly preserves shown receipts.
The new helper APIs were not found in the mechanic documentation or `common/scripted_effects/chaosx_dynamic_effects.md` during this review; the parent must add their purpose, COUNTRY scope, inputs/outputs, rejection/default behavior, side effects, caller-owned temporary storage, and examples under its documentation ownership.
No gameplay/doc helper implementation was patched by this agent; only this handoff was appended.
No simplification or fallback was applied, and no Git/index operation, game launch, or game/log/save request was made.

Post-patch MCP evidence: a focused `hoi4.event_inspect(mode = trace)` succeeded with `EVENT_INSPECTED_PARTIAL` at revision `5b61a45d5836c19fd276ef8a5e51b000c91b28ce24b8158b45c373319843902d`, graph hash `037eb2eda9cdca709c30b78d69779582bcdfbcd9f3bd290b924567efd5839078`.
The selector was the incident event file, with `maxDepth = 1`, `maxNodes = 150`, `maxEdges = 300`, and `expandHelpers = false`.
The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cfd1ad291424639b3f11809a49c993893701e737a49588931f69daccece6cb0f/f9d077b5fe463fb4f0ef07b47bfca6c70403f69f5e81cdfbd76512171c089aae/event-trace-5b61a45d5836.json`, declared 1,375,423 bytes and SHA-256 `cfd1ad291424639b3f11809a49c993893701e737a49588931f69daccece6cb0f`.
The tool explicitly deferred whole-workspace helper projections and lifecycle passes; its workspace totals and truncated inline 64-of-404 source list are not selected-event lifecycle coverage.
Artifact coverage/retrieval, render results, and corrected file-validation results are recorded below after their final results are inspected.
The first two file-validation requests improperly also supplied kind/scope; the live route rejected them because a path check infers kind/scope from the file, and corrected path-only requests were issued.
Detailed trace artifact retrieval is blocked: a bounded `resources/read` of that exact URI with `?offset=0&length=65536` returned MCP error `-32603: Artifact provenance manifest is unavailable`.
The configured workspace storage root was resolved from the current Codex HOI4 server configuration, but no local artifact matching the declared `cfd1ad...` SHA-256 was found at the corresponding workspace artifact location.
Other same-named trace files with different content hashes were not accepted as substitutes.
The inline trace revision, declared artifact identity, partial/deferred analysis flags, and request bounds are retained, while detailed selected-node/edge/continuation coverage remains unresolved.

Final post-patch MCP results:

| Request | Final result and limit |
| --- | --- |
| Artifact resource-template discovery | Confirmed byte-range selectors: zero-based offset, positive length, maximum 1,048,576 bytes; the failed 65,536-byte read used a supported request shape |
| Patched effects file script validation | `SCRIPT_CHECK_PARTIAL`, `valid = null`, validation passed false; 510 commands checked; zero findings/unresolved commands, but 305 argument blocks unchecked and all 12 scripted-effect roots have unknown inferred scope |
| Patched triggers file script validation | `SCRIPT_CHECK_PARTIAL`, `valid = null`, validation passed false; 41 commands checked; zero findings/unresolved commands, but 7 argument blocks unchecked and all 5 scripted-trigger roots have unknown inferred scope |
| State event render for the incident file, depth 1, maxNodes 150, helpers unexpanded | Final failure: `tool call failed for hoi4_agent_tools/hoi4.event_render; timed out awaiting tools/call after 600s`; no render artifact or revision returned |

Both file checks report only `syntax`, `command_kind`, `declared_scope`, and `event_popups` under installed-documentation aggregate revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`, with `parametersChecked = false` and no truncated or omitted findings.
The empty finding lists are not passes and do not establish parameter or COUNTRY-scope correctness for the unknown inferred roots.
No further broad body generation or whole-workspace native claim was attempted; explicit-scope snippet checks and final integration remain outside this bounded report-only follow-up.
No event comparison was run by this reviewer; the frozen-to-current source comparisons above do not substitute for a parent-owned MCP comparison.
The event render and detailed trace artifact coverage remain blocked despite the successful partial trace summary.

Canonical manifest follow-up: the parent subsequently published `docs/plans/006_independence_wave_plans/evidence_20261008/package_incident_snapshots/frozen_before/source_manifest.json`.
I read it after publication and verified that it declares `canonical_baseline = true`, exactly the three raw effects/events/triggers source files, their matching pre-patch hashes listed in the earlier audit table, and `captured_before_owner_patch = true` for each.
This resolves the earlier audit-time absence of the manifest; no noncanonical pending-client copy was used.
The independent post-patch mapping/option comparisons, lifecycle replay, current source hashes, and source-critical findings remain unchanged.

### Parent-reported narrow MCP follow-up

The parent subsequently reported a successful narrow render of event `chaosx.nr6.101`, depth 1, maximum 6 nodes, returning `EVENT_RENDERED_PARTIAL` at the same revision `5b61a45d5836c19fd276ef8a5e51b000c91b28ce24b8158b45c373319843902d` and graph hash `037eb2eda9cdca709c30b78d69779582bcdfbcd9f3bd290b924567efd5839078` as the inspected post-patch trace.
Reported coverage is `selectedNodes = 6`, `helpers = 0`, and a focused boundary, with 404 source files and 64 paths retained inline.
This closes the render-call response gap for that narrow selected view only; the earlier reviewer state-render timeout remains a historical failed request.
It does not establish all-130-event rendered coverage, helper expansion, COUNTRY-scope correctness, checked parameter semantics, or native behavior.
The parent retains the full response and artifact metadata.
Only abbreviated artifact identifiers were supplied to this reviewer: JSON content-hash prefix `13701357...`, provenance-hash prefix `7da673...`, filename `event-neighborhood-5b61a45d5836.json`, and SVG content-hash prefix `a065b0b9...`.
These abbreviations are not full usable resource URIs; this reviewer did not reconstruct them, retrieve those artifacts, or claim their detailed content was independently examined.

The parent also reported an event comparison using a before revision abbreviated as `db07...`, which returned `EVENT_REVISION_NOT_CACHED` and zero artifacts.
The failed comparison supplies no before/after MCP delta or preserved cached graph baseline.
The canonical frozen raw-source comparisons remain the source-preservation evidence, not a substitute for a successful MCP comparison.

A parent source lookup for `can_fire_independence_wave_package_incident` reportedly returned one country-trigger definition at `mod:common/scripted_triggers/006_independence_wave_package_incident_triggers.txt:8-12`, with its source revision supplied only as prefix `866d...`.
This corroborates definition discovery; it does not close the file validator's unknown-root scopes or unchecked argument blocks.
The parent states that its MainParentSourceReview retains all partial/unbound-argument findings and that no weights or content changed.
No additional source-critical finding, simplification, or implementation change follows from these MCP updates.
This follow-up is parent-provided evidence with the exact abbreviation and coverage limits recorded, while the independent source review above remains unchanged.

### Bounded source-documentation closure

The parent requested a report-only closure note with no new MCP queries.
I read the updated `docs/events/006_independence_wave/package_incidents.md` overview and steps 4-8, the canonical `docs/events/006_independence_wave/systems/package_incident_lifecycle.md`, the owner-index entry in `common/scripted_effects/chaosx_dynamic_effects.md:484`, and `docs/plans/006_independence_wave_plans/subagent_handoffs/package_incident_snapshot_source_20261008.md`.
The required helper/lifecycle documentation coverage is closed: the canonical document covers COUNTRY scope, caller-owned selector output and zero default, queue rejection, unchanged appointments, snapshot ownership, cleanup side effects, usage, timeout treatment, due coalescence, and native/replay limits, and the overview and shared owner index link to it.
No further code gap was found or introduced in this bounded source review.
This closes the earlier missing API/lifecycle documentation finding without extending native acceptance or the full Event 006 completion claim.

A minor wording discrepancy is retained for accuracy: overview step 5 says snapshots are captured before publishing shown and delivered, whereas the inspected capture bodies set shown first, then both normal snapshot variables, then delivered.
The canonical document and parent source review correctly preserve the required snapshot-before-delivered contract.
The overview can say "captures the shown snapshot before publishing delivered" without implying a different shown-flag write order.
The old helper-file overview sentence "clears every receipt" also remains an imprecise comment; the actual cleanup body and canonical API explicitly preserve shown proof.
These wording notes do not reopen a code or missing-API-documentation gap, and this agent did not edit those parent-owned files.

The parent source review now supplies the full source-lookup revision `866d856bf2215897197f50f2438dec13a117db522430b7bfc4f78b94b4593c46` for the single non-shadowed can_fire definition, and the full failed comparison before revision `db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5`.
The failed comparison remains `EVENT_REVISION_NOT_CACHED` with zero comparison artifacts; retaining its metadata does not produce a successful delta.

The parent reports immediate retention of the repeated narrow-render manifest, JSON, SVG, and PNG under `docs/plans/006_independence_wave_plans/evidence_20261008/package_incident_snapshots/mcp_render/`.
Its retained JSON reports `complete = false`, six selected nodes, twelve unresolved entries, and 46,249 omitted nodes, with the event-source hash matching the independently reviewed raw file `0cdfe730fa131af45af5d1e358c1a0587f41d5f39d4146b3f75de00f8fb26b35`.
The parent source review identifies those six nodes as event 101, two options, and unresolved capture, country-delta, and close helpers, and records the initial JSON hash `13701357f4e13f3ec0866d0910f373e76930adfc8459a09f9dbb7098ace7502e` before cache eviction.
The parent visually inspected the retained PNG as a bounded source-chain diagram; this reviewer did not independently inspect the image or retrieve further artifact content during this closure.
The retained evidence closes loss of the narrow render response/artifacts but remains partial source-chain evidence, with no helper execution, native popup, COUNTRY-scope, parameter-semantics, or all-130 rendered coverage claim.
The parent source review retains the file-check partial/unbound-argument limits and native lifecycle gates.

No new query, engine patch, content/weight change, simplification, fallback, Git/index operation, or game/log/save request was made for this closure.
Only this assigned handoff was appended.
