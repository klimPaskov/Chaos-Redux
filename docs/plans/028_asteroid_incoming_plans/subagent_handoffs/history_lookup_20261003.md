# Event 028 history lookup source audit

Disposition: implemented (IMPLEMENTED in source), with actual-source AST validation complete and native acceptance unresolved.
Acceptance basis: the parent explicitly accepted the narrow history lookup repair within the user's authorized full Event 028 package, preserving the no-new-caps, no-new-branch, and no-fallback contract.
The parent applied the runtime change and requested this implementation-status and actual-AST evidence update.
Authority: the worker edits only this handoff and its appendix, while the parent retains source implementation and final commit ownership.
Parent baseline tranche: commit `829f4db894d90a08570e5483377189ca51638771`.
Exact before source for this implementation comparison: `e0598a512291568dc79596a91acb428f9796f99c:common/scripted_effects/028_asteroid_incoming_runtime_effects.txt`, retrieved with read-only `git show`.
Actual after source is the current runtime file at the same repository path.
This worker updates only this handoff and its reproducible actual-source AST appendix.
No runtime, shared effect, AI, localisation, helper source, or other document is edited.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, read earlier in this conversation and applied here to the one-row history and ownership contracts.

## Finding and supported invariant

The concern is confirmed by source and the installed loop ceiling.
The committed before version of `asteroid_incoming_record_followup_history` starts its search at zero and advances through `while_loop_effect` at `028_asteroid_incoming_runtime_effects.txt:390-437`.
Vanilla `common\defines\00_defines.lua:25` declares `MAX_EFFECT_ITERATION = 1000`.
That before loop can inspect indices 0 through 999, so a valid row at index 1000 is already beyond its search, not merely a row after more than 1000 insertions.
The parent replaced the loop in the actual after helper at lines 382-463.
The after matched write block at lines 430-447 and success tail at 451-461 are AST-equal to the before matched block and tail, excluding the deliberately changed identity/guard limit.

Both completed shared row writers increment the same global sequence by one and insert the new sequence, event ID, date, payload, actor, secondary actor, and remaining row fields at index zero.
Therefore, within one initialized history generation:

```text
Event 028 row index = current global history sequence - bound Event 028 sequence
```

If M rows existed before the opening, the Event 028 opening is assigned sequence M+1 and is still index zero.
After N later normal or system rows, the current counter is M+1+N and the opening is at index N.
M cancels from the difference.
This lookup requires no search loop, row cap, extra history row, batch scheduler, or new persistent helper state.

## Actual writers, mutations, and references

The token and mutation searches covered runtime `.txt` source under `common\` and `events\`.
The three named owner files were read directly, including the shared sanitizer functions invoked by the recorder.
Other event files were searched for write references without broadening into their gameplay mechanics.

| Surface | Exact reference and operation | Consequence |
| --- | --- | --- |
| Normal recorder | `chaosx_events_log_effects.txt:677-797`, increment at 698, sequence/event/date insertion at 700-714, remaining field insertion through 772 | One sequence increment and index-zero insertion in every parallel history column. |
| System recorder | `chaosx_events_log_effects.txt:536-617`, increment at 556, sequence/event/date insertion at 558-572 | System rows shift the Event 028 row identically to normal rows. |
| Event 028 binding | Runtime `asteroid_incoming_bind_opening_history_sequence:361-373`, called from normal recorder at shared line 797 | Captures the already incremented opening sequence after normal row insertion and sets outcome pending. |
| Initialization | `chaosx_logic_effects.txt:26-48` and 126 | Clears all base history arrays together and resets the counter to zero. |
| Missing-counter defaults | Shared lines 537-540 and 678-681 | Set the counter to zero only if absent. A lost counter with existing rows is an inconsistent state, not proof of a valid generation. |
| Shared alignment repair | Shared lines 13-192 | Appends zero defaults to missing actor/payload/secondary columns and sanitizes invalid actor pointers. It does not insert sequence, event-ID, or date entries. |
| Event 028 outcome write | After runtime 430 and 444-445, previously 417 and 431-432 | Changes only an existing payload and, for an impact with a living locked-country pointer, its secondary actor fields. |
| Other event mutations | `016_brilliant_scientist_effects.txt:84-85`, `017_random_faction_effects.txt:1087-1088` | In-place actor or secondary-actor updates, not sequence/event-ID/date insertion or removal. |
| Private event ledgers | Event 018, 029, and fallout references to the shared sequence | Store the sequence in their private arrays or variables. They do not change the shared sequence ordering. |

The global sequence has only five static assignments in the scanned runtime source: the initializer reset, the two missing-variable defaults, and the two recorder increments.
Shared sequence entries have only the initializer clear and the two insertion writers.
No static base sequence/event-ID/date element replacement, removal, resize, trim, sort, or targeted dynamic-name writer was found in the scanned runtime source.
Presentation views read or copy the master sequence and do not provide another master row writer in this scan.
This is a static source-writer inventory, not executed engine coverage or a guarantee against externally edited data.

## Implemented parent repair

The parent retained the existing helper identifier, pending gate, caller payload, successful payload/secondary-actor writes, and success-only tail.
The actual after source replaces its zero-based while search with the sequence difference and guarded exact row validation.
No shared writer, initializer, new helper, new branch, cap, or fallback was changed or introduced for this repair.

1. Require pending outcome, both saved and current sequence variables, a positive saved sequence, and current sequence at least saved sequence.
2. Compute the existing temporary row index from current sequence minus saved sequence with `set_temp_variable` and `subtract_from_temp_variable`.
3. Before any array read, require the index to be nonnegative and strictly below sequence, event-ID, and payload array lengths.
4. Reuse the exact existing comparisons: the indexed sequence must equal the saved Event 028 sequence, and the indexed event ID must equal `constant:asteroid_incoming_event.id`.
5. For an impact with a present living locked-country pointer, also require the index below both secondary-actor array lengths before executing either secondary write.
6. Execute the existing matched-row block once and preserve its success-only global history outcome, pending clear, and view refresh.
7. If any requirement fails, leave the history row and pending state unchanged. Do not append a substitute row, clear pending on failure, redirect to another Event 028 row, or introduce a scheduled retry.

Observed after source: positive saved/current guards at 385-390, sequence subtraction at 395-396, separate bounds branch at 397-403, exact sequence/event identity at 404-415, and the conditional secondary-field bounds conjunction at 416-428.
The bounds branch is separate from the identity-read branch to avoid out-of-range reads.
The explicit AND inside NOT preserves the conjunction rather than accidentally using NOR semantics over separate sibling requirements.
The appendix executes these actual AST branches and assignments from the current file, rather than independently simulating the intended direct lookup algorithm.
Source implementation and AST validation do not establish native engine acceptance.

## Helper contract, tuning, lifecycle, and migration

| Contract | Implemented behavior |
| --- | --- |
| Helper and scope | Existing `asteroid_incoming_record_followup_history`, any caller scope under its existing ROOT/locked-country capture contract. |
| Inputs | Pending flag, saved Event 028 sequence, shared current sequence and parallel arrays, temporary caller payload, optional existing locked-country target. |
| Outputs | Existing temporary updated marker, exact indexed payload, optional secondary actor and flag, success-only persistent history outcome. |
| Preserved fields | Sequence, original event ID/type, original date, primary chooser actor, total row count, shared counter, and all unrelated rows receive no writes from the lookup replacement. |
| Constants | Reuse current Event 028 zero, one, event ID, and payload constants. Add no tuning constant, duration, cap, or probability field. |
| Event targets | Reuse locked_country only. Do not substitute a current owner/controller for the historical target or add a target. |
| Cleanup | Preserve success-only pending clear. The row index is temporary and requires no persistent cleanup. |
| Migration | Parent replaced the loop within the existing helper, retaining the matched block and final success block. No call-site change or shared-system migration. |
| Batch fallback | Not needed for the proven ordinary writer invariant. Malformed, missing, deleted, or reordered data fails the exact guarded lookup and remains unresolved. |

Impact uses the existing payload 282 and writes the secondary actor only when the locked-country pointer exists and that country still exists.
An annexed or absent target does not gain an invented replacement secondary actor.
Miss payload 281 and fail-closed payload 283 change the payload without assigning or clearing secondary actors.
The success path creates no extra normal or system row.
Part 8's one-major-row contract is at `028_asteroid_incoming_spec_part_8_events_logs_and_text_direction.md:126-141`.

The retained call to `sanitize_events_log_history_actor_entries` can itself repair missing columns or clear invalid primary/secondary actor pointers.
Therefore, exact actor preservation applies to valid existing actor data and to the lookup replacement's own writes, not to all possible side effects of that shared sanitizer.
Its repair and scan loops share the engine ceiling, so bounds checks are necessary even after calling it.
Do not broaden this Event 028 patch into shared sanitizer or Event History UI changes.
Initialization removes history and reuses sequence values. Exact sequence/event ID checks cannot distinguish a stale binding from a later identical sequence/event ID in another reset generation.
That ambiguity existed in the before scan and remains unresolved by this bounded lookup repair.
No epoch flag or new recovery branch is proposed.

## Source scenarios and validation limits

The appendix reads the exact before source via git show, captures the actual current after bytes, parses both, and executes the entire existing follow-up helper AST for each version.
The evaluator executes actual if/AND/OR/NOT guards, comparisons, assignments, array accesses, temporary arithmetic, before loops with the installed ceiling, target/ROOT/PREV scopes, pending clear, and the success tail.
Unknown commands, unsupported argument forms, persistent writes outside the declared helper contract, or unsupported comparisons fail validation rather than being silently skipped.
All 22 unchanged fixtures passed against actual after AST execution, including the exact index-1000 boundary and index-1500 mixed-writer case.
Before and after matched-row write bodies and success tails are independently checked for exact AST equality.
All after cases produced zero invalid array accesses, and rejected cases produced zero partial array writes.
Fixture SHA256: `5244B4A022BF209590080817F8368E8B4DDA6A789D9273973A4D434B1CDD8719`.
The before AST is also executed through its writes and success tail.
Under the explicitly unrepaired-array fixtures, it attempts out-of-range payload/secondary writes, and secondary-field failures occur after its payload write.
Those are instrumented source-model bounds faults, not observed HOI4 errors or a claim about native out-of-range behavior.

The only stubbed called functions are `sanitize_events_log_history_actor_entries` and `refresh_events_log_system_history_views`.
Their source calls execute in the interpreter as explicit no-op stubs with recorded current scope, temporary inputs, pending state, and array lengths.
The sanitizer stub deliberately does not repair missing fields, so the malformed-array cases test the actual after guards under unrepaired input, rather than predicting whether native sanitization would repair that input first.
The view stub records delivery after success and is asserted absent on rejected updates.
These two transitive implementations, native object/scope evaluation, UI rebuilds, save persistence, reset scheduling, and engine array implementation are not modelled as native behavior.
Availability, near-miss, and capital regression suites are not rerun by this worker, as the parent expressly owns their separate runs.

| Case | Expected source result |
| --- | --- |
| Newest Event 028 row | Difference zero selects index zero. |
| Other rows before opening | Still index zero after opening. Older history does not enter the difference. |
| Later mixed normal/system rows | Index equals the number of subsequent rows. |
| 999 subsequent rows | Both actual before and after ASTs write index 999. |
| 1000 or 1500 subsequent rows | Actual before reaches its lookup ceiling without an update. Actual after writes the exact existing row. |
| Missing saved/current sequence, zero/future saved sequence, absent row | No update and no pending clear. |
| Wrong indexed sequence or wrong event ID | No update, even if another Event 028 row exists elsewhere. |
| Missing payload field | Reject before writing an absent element. |
| Impact with incomplete secondary fields | Reject the whole update before writing partial impact metadata. |
| Impact with living target | Set the existing secondary actor and its flag. |
| Impact with absent/dead target | Preserve the existing no-secondary-write behavior. |
| Miss/fail-closed | Payload only, preserving original actor/date and existing secondary fields. |
| Every successful fixture | No row append, counter change, original actor/date change, or unrelated-row change. |

## MCP and references

Required coding routes are exposed in this client, but all four narrow audit requests returned `timed out awaiting tools/call after 600s` with `isError = true`.
Requests: event reference context at limit twelve, reference search for while_loop_effect, source lookup for only `asteroid_incoming_record_followup_history` with references disabled and eighty-line limit, and a bounded Event 028.4 trace with depth one, eight nodes, ten edges, and helper expansion disabled.
No graph, source-lookup revision, reference citation bundle, continuation URI, or artifact was returned.
The parent separately reported a six-hundred-second trace timeout and a pending minimum return-board retry.
Those parent requests are separate evidence and are not reported as a successful audit route here.
At implementation review, the parent reported that its narrow event/map/reference retries also timed out after 600 seconds and that the current options render was pending.
No completion, artifact, or native history-update acceptance is inferred from that pending render.
This actual-AST documentation update does not repeat the already failed native calls or claim that the interpreter replaces them.
No reference_read call could use a new returned citation because context/search returned no citation data.
The pertinent local documentation sections were read directly after those route gaps.
No probability surface, AI weight, map, focus, or GUI design is changed or accepted by this audit.
HOI4 was not launched.

Read local references:

- Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:1069-1088` documents zero-based arrays, `^num`, element existence before editing, and insertion shifting.
- Its lines 1219-1220 and footnote at 1828 document the default loop ceiling.
- Installed `documentation\effects_documentation.md:2278-2292` documents add_to_array and shifting insertion.
- Installed lines 8187-8198 document subtraction from temporary variables.
- Installed lines 8573-8586 document while-loop execution.
- Installed `documentation\triggers_documentation.md:2110-2134` and 5006-5013 document comparisons and variable existence.
- Installed `common\defines\00_defines.lua:25` supplies the concrete loop ceiling.
- The two inspected shared recorders provide the directly relevant current project prepend precedent.
The attempted search for an additional matching vanilla history-sequence idiom found no precedent in the searched installed scripted effects, so none is claimed.

Captured source file revisions:

| File | SHA256 |
| --- | --- |
| Historical before physical runtime snapshot | `10D679880DFD53DD826E7D90DE3F1708A27EA2924E6F2C784BE64D318A475FAB` |
| Exact committed before runtime blob bytes from `git show e0598a512291568dc79596a91acb428f9796f99c:common/scripted_effects/028_asteroid_incoming_runtime_effects.txt` | `10D679880DFD53DD826E7D90DE3F1708A27EA2924E6F2C784BE64D318A475FAB` |
| Before blob bytes normalized from CRLF to LF | `10D679880DFD53DD826E7D90DE3F1708A27EA2924E6F2C784BE64D318A475FAB` |
| Actual after runtime physical bytes | `0A902614C03D060B159DADBA42C706D3C203CB0F448884E7AB10AC4BF2643214` |
| Actual after runtime bytes normalized from CRLF to LF | `0A902614C03D060B159DADBA42C706D3C203CB0F448884E7AB10AC4BF2643214` |
| `chaosx_events_log_effects.txt` | `5F9F99BE4AA88DFDDB17EB1F7A171DFBF6D49283CA51A2EE54B60940D2A770CE` |
| `chaosx_logic_effects.txt` | `C28EE6EAB4A2CEEA866C81CFFD6488E04A0B9D9ED509F650CFDDCC3F49B7548E` |
| Installed `documentation\effects_documentation.md` | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Installed `documentation\triggers_documentation.md` | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| Installed `common\defines\00_defines.lua` | `405A24CE579815443CAFE052CFF1361E20C712CA8182E3F10CCBF45330DD4BE4` |
| Offline `Data structures - Hearts of Iron 4 Wiki.md` | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |

The before Git blob object ID is `063bd4ee9978797edd7a9c772c1c4d54831f74d2`, obtained with `git rev-parse` for the exact commit/path.
That Git object identity is separate from SHA256 hashes of the file bytes.
The blob contains 103151 bytes and already uses LF, which is why its raw and LF-normalized SHA256 hashes are equal.
The earlier physical snapshot happens to have identical bytes, but it is retained as a separately labelled provenance record rather than substituted for the committed before source.
The appendix prints these identities from the actual Git blob and captured after bytes and fails if the after source changes during execution.

Only this handoff/appendix is changed by the worker.
The accepted lookup repair was implemented by the parent, and the worker confirms it through the actual-source AST evaluation above.
No gameplay simplification, new branch, cap, fallback, helper, source edit, or commit is introduced by this documentation update.
The parent retains commit ownership and unmet native evidence before any broader completion claim.

## Reproducible source-model appendix

Run from the repository root:

```powershell
python -c "from pathlib import Path; p=Path('docs/plans/028_asteroid_incoming_plans/subagent_handoffs/history_lookup_20261003.md'); t=p.read_text(encoding='utf-8'); exec(t.rsplit('<!-- history-lookup-model -->',1)[1].split(chr(96)*3+'python')[1].split(chr(96)*3)[0])"
```

<!-- history-lookup-model -->
```python
from pathlib import Path
import copy
import hashlib
import json
import re
import runpy
import subprocess

root = Path.cwd()
parse = runpy.run_path(str(root / '.tools/validation/validate_028_availability.py'))['parse_source']
runtime_path = root / 'common/scripted_effects/028_asteroid_incoming_runtime_effects.txt'
before_commit = 'e0598a512291568dc79596a91acb428f9796f99c'
before_relative_path = 'common/scripted_effects/028_asteroid_incoming_runtime_effects.txt'
before_bytes = subprocess.check_output(['git', 'show', before_commit + ':' + before_relative_path], cwd=root)
before_blob_oid = subprocess.check_output(['git', 'rev-parse', before_commit + ':' + before_relative_path], cwd=root, text=True).strip()
class GitBlobSource:
    def read_text(self, encoding): return before_bytes.decode(encoding)
runtime_before = parse(GitBlobSource())
after_bytes = runtime_path.read_bytes()
class CurrentSource:
    def read_text(self, encoding): return after_bytes.decode(encoding)
runtime_after = parse(CurrentSource())
runtime = runtime_after
shared = parse(root / 'common/scripted_effects/chaosx_events_log_effects.txt')
logic = parse(root / 'common/scripted_effects/chaosx_logic_effects.txt')
constants = parse(root / 'common/script_constants/028_asteroid_incoming_constants.txt')
define_path = Path('C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/defines/00_defines.lua')
ceiling = int(re.search(r'MAX_EFFECT_ITERATION\s*=\s*(\d+)', define_path.read_text(encoding='utf-8-sig'))[1])
P = 'global.events_log_history_'
sequence_key = 'global.events_log_history_sequence'
saved_key = 'global.asteroid_incoming_history_sequence'
index_key = 'asteroid_incoming_history_row_index'
payload_key = 'asteroid_incoming_history_payload'
updated_key = 'asteroid_incoming_history_row_updated'
def fields(body): return dict((k, v) for k, _, v in body)
def one(rows, name): return next(v for k, _, v in rows if k == name)
def constant(token):
    category, key = token.removeprefix('constant:').split('.')
    return float(fields(constants[category])[key])
event_id = int(constant('constant:asteroid_incoming_event.id'))
opening = int(constant('constant:asteroid_incoming_event.history_payload_opening'))
impact = int(constant('constant:asteroid_incoming_event.history_payload_impact'))
miss = int(constant('constant:asteroid_incoming_event.history_payload_miss'))
fail_closed = int(constant('constant:asteroid_incoming_event.history_payload_fail_closed'))

writers = {}
for name in ('record_events_log_history_entry', 'record_events_log_system_history_entry'):
    body = shared[name]
    increments = [v for k, _, v in body if k == 'add_to_variable' and v == [(sequence_key, '=', '1')]]
    assert len(increments) == 1, name
    entries = [fields(v) for k, _, v in body if k == 'add_to_array']
    assert len(entries) == 12 and all(e['index'] == '0' for e in entries), name
    assert fields(one(body, 'add_to_array'))['array'] == P + 'sequence_entries', name
    writers[name] = entries
assert {e['array'] for e in writers['record_events_log_history_entry']} == {e['array'] for e in writers['record_events_log_system_history_entry']}
assert (sequence_key, '=', '0') in one([r for r in logic['initialize_event_system'] if r[0] == 'set_variable' and r[2] == [(sequence_key, '=', '0')]], 'set_variable')
for e in writers['record_events_log_history_entry']:
    assert ('clear_array', '=', e['array']) in logic['initialize_event_system']
bound = runtime['asteroid_incoming_bind_opening_history_sequence']
assert ('set_variable', '=', [(saved_key, '=', sequence_key)]) in one(bound, 'if')

helper_name = 'asteroid_incoming_record_followup_history'
followup = runtime_before[helper_name]
pending_body = one(followup, 'if')
loop = one(pending_body, 'while_loop_effect')
loop_limit = one(loop, 'limit')
matched_body = one(loop, 'if')
identity = one(matched_body, 'limit')
payload_write = one(matched_body, 'set_variable')[0]
assert payload_write == (P + 'payload_entries^' + index_key, '=', payload_key)
secondary_body = one(matched_body, 'if')
assert ('has_event_target', '=', 'asteroid_incoming_locked_country') in one(secondary_body, 'limit')
assert ('event_target:asteroid_incoming_locked_country', '=', [('exists', '=', 'yes')]) in one(secondary_body, 'limit')
secondary_writes = [v[0] for k, _, v in secondary_body if k == 'set_variable']
assert [k for k, _, _ in secondary_writes] == [P + 'secondary_actor_entries^' + index_key, P + 'has_secondary_actor_entries^' + index_key]
assert all(k not in ('add_to_array', 'record_events_log_history_entry', 'record_events_log_system_history_entry') for k, _, _ in matched_body)
after_body = runtime_after[helper_name]
after_pending = one(after_body, 'if')
after_bounds = one(after_pending, 'if')
after_match = one(after_bounds, 'if')
assert [r for r in matched_body if r[0] != 'limit'] == [r for r in after_match if r[0] != 'limit'], 'matched write body changed'
assert [r for r in followup if r[0] == 'if'][1] == [r for r in after_body if r[0] == 'if'][1], 'success tail changed'
assert all(k != 'while_loop_effect' for k, _, _ in after_pending), 'after still contains the lookup loop'

class Fixture:
    def __init__(self, older=0, later=0, payload=impact, target=202, living=True):
        self.arrays = {e['array']: [] for e in writers['record_events_log_history_entry']}
        self.latest, self.saved, self.pending, self.outcome = 0, None, True, None
        self.payload, self.target, self.living = payload, target, living
        for i in range(older): self.append(i % 2, 7)
        self.append(0, event_id)
        self.saved = self.latest
        for i in range(later): self.append(i % 2, 9)
    def append(self, system, event):
        self.latest += 1
        row = {'sequence_entries': self.latest, 'date_entries': 19360101 + self.latest, 'event_id_entries': event, 'event_type_entries': 8 if system else 1, 'payload_entries': opening if event == event_id else 0, 'actor_entries': 101 if event == event_id else 303, 'has_actor_entries': 1, 'secondary_actor_entries': 0, 'has_secondary_actor_entries': 0, 'minor_since_major_entries': 0, 'unique_left_entries': 40, 'total_fired_entries': self.latest}
        entries = writers['record_events_log_system_history_entry' if system else 'record_events_log_history_entry']
        for entry in entries: self.arrays[entry['array']].insert(int(entry['index']), row[entry['array'][len(P):]])

class BoundsFault(Exception): pass

class AstEvaluator:
    # Only these transitive calls are explicitly stubbed, with call context.
    # They do not repair fixture arrays or rebuild views in this source model.
    stubs_allowed = {'sanitize_events_log_history_actor_entries', 'refresh_events_log_system_history_views'}
    effects_allowed = {'if', 'while_loop_effect', 'set_temp_variable', 'subtract_from_temp_variable', 'add_to_temp_variable', 'set_variable', 'clr_global_flag', 'ROOT'}
    triggers_allowed = {'check_variable', 'has_variable', 'has_global_flag', 'has_event_target', 'exists', 'AND', 'OR', 'NOT'}
    def __init__(self, fixture):
        self.fixture = copy.deepcopy(fixture)
        self.temp = {payload_key: fixture.payload}
        self.vars = {}
        if fixture.latest is not None: self.vars[sequence_key] = fixture.latest
        if fixture.saved is not None: self.vars[saved_key] = fixture.saved
        self.flags = {'asteroid_incoming_history_outcome_pending'} if fixture.pending else set()
        self.root_scope = {'id': 101, 'exists': True}
        self.stack = [self.root_scope]
        self.targets = {} if fixture.target is None else {'asteroid_incoming_locked_country': {'id': fixture.target, 'exists': fixture.living}}
        self.reads, self.writes, self.invalid, self.calls, self.trace = [], [], [], [], []
        self.ceiling_reached = False
    def validate(self, rows, trigger=False):
        for key, op, body in rows:
            assert op == '=', ('unsupported operator', key, op)
            if key.startswith('event_target:') or key == 'ROOT':
                self.validate(body, trigger)
            elif trigger:
                assert key in self.triggers_allowed, ('unknown trigger', key)
                if key in ('AND', 'OR', 'NOT'): self.validate(body, True)
                elif key == 'check_variable':
                    assert set(fields(body)) == {'var', 'value', 'compare'}, ('unsupported comparison arguments', body)
            elif key in self.stubs_allowed:
                assert body == 'yes'
            else:
                assert key in self.effects_allowed, ('unknown effect', key)
                if key in ('if', 'while_loop_effect'):
                    self.validate(one(body, 'limit'), True)
                    self.validate([r for r in body if r[0] != 'limit'])
                elif key != 'clr_global_flag':
                    assert len(body) == 1 and body[0][1] == '=' and isinstance(body[0][2], str), ('unsupported variable arguments', body)
    def scope(self, key):
        if key == 'ROOT': return self.root_scope
        assert key.startswith('event_target:'), ('unknown scope', key)
        name = key.split(':', 1)[1]
        assert name in self.targets, ('invalid target scope', name)
        return self.targets[name]
    def array_slot(self, token, operation):
        name, slot = token.rsplit('^', 1)
        assert name in self.fixture.arrays, ('unmodelled array', name)
        value = self.value(slot)
        if not float(value).is_integer():
            self.invalid.append((operation, name, value))
            raise BoundsFault((operation, name, value))
        index = int(value)
        if not 0 <= index < len(self.fixture.arrays[name]):
            self.invalid.append((operation, name, index))
            raise BoundsFault((operation, name, index))
        return name, index
    def value(self, token):
        if token.startswith('constant:'): return constant(token)
        if token in ('ROOT', 'THIS', 'PREV'):
            scope = self.root_scope if token == 'ROOT' else self.stack[-1] if token == 'THIS' else self.stack[-2]
            return scope['id']
        if '^' in token:
            name, slot = token.rsplit('^', 1)
            if slot == 'num':
                assert name in self.fixture.arrays, ('unmodelled array', name)
                self.trace.append(('size', name, len(self.fixture.arrays[name])))
                return len(self.fixture.arrays[name])
            name, index = self.array_slot(token, 'read')
            self.reads.append((name, index))
            self.trace.append(('read', name, index))
            return self.fixture.arrays[name][index]
        try: return float(token)
        except ValueError: return self.temp.get(token, self.vars.get(token, 0))
    def condition(self, rows): return all(self.trigger(*row) for row in rows)
    def trigger(self, key, op, body):
        assert op == '='
        if key in ('AND', 'OR', 'NOT'):
            return self.condition(body) if key == 'AND' else any(self.trigger(*r) for r in body) if key == 'OR' else not any(self.trigger(*r) for r in body)
        if key == 'check_variable':
            a = fields(body)
            left, right = self.value(a['var']), self.value(a['value'])
            compare = {'equals': lambda: left == right, 'greater_than': lambda: left > right, 'less_than': lambda: left < right, 'greater_than_or_equals': lambda: left >= right, 'less_than_or_equals': lambda: left <= right}
            assert a['compare'] in compare, ('unknown comparison', a['compare'])
            return compare[a['compare']]()
        if key == 'has_variable': return body in self.vars or body in self.temp
        if key == 'has_global_flag': return body in self.flags
        if key == 'has_event_target': return body in self.targets
        if key == 'exists': return self.stack[-1]['exists'] == (body == 'yes')
        if key.startswith('event_target:') or key == 'ROOT':
            self.stack.append(self.scope(key))
            try: return self.condition(body)
            finally: self.stack.pop()
        raise AssertionError(('unknown evaluated trigger', key))
    def assign(self, token, value, temporary=False):
        if temporary: self.temp[token] = value
        elif '^' in token:
            name, index = self.array_slot(token, 'write')
            self.fixture.arrays[name][index] = value
            self.writes.append((name, index, value))
            self.trace.append(('write', name, index))
        else:
            assert token == 'global.asteroid_incoming_history_outcome', ('unsupported persistent variable write', token)
            self.vars[token] = value
            self.fixture.outcome = value
    def run(self, rows):
        for key, op, body in rows:
            assert op == '='
            if key == 'if':
                if self.condition(one(body, 'limit')): self.run([r for r in body if r[0] != 'limit'])
            elif key == 'while_loop_effect':
                for _ in range(ceiling):
                    if not self.condition(one(body, 'limit')): break
                    self.run([r for r in body if r[0] != 'limit'])
                else: self.ceiling_reached = self.condition(one(body, 'limit'))
            elif key in ('set_temp_variable', 'subtract_from_temp_variable', 'add_to_temp_variable', 'set_variable'):
                token, _, rhs = body[0]
                value = self.value(rhs)
                if key == 'subtract_from_temp_variable': value = self.value(token) - value
                if key == 'add_to_temp_variable': value = self.value(token) + value
                self.assign(token, value, key != 'set_variable')
            elif key == 'clr_global_flag':
                assert body == 'asteroid_incoming_history_outcome_pending', ('unsupported flag write', body)
                self.flags.discard(body)
                self.fixture.pending = False
            elif key in self.stubs_allowed:
                assert body == 'yes'
                self.calls.append({'name': key, 'scope': self.stack[-1]['id'], 'temp': dict(self.temp), 'pending': self.fixture.pending, 'array_lengths': {n: len(a) for n, a in self.fixture.arrays.items()}})
            elif key.startswith('event_target:') or key == 'ROOT':
                self.stack.append(self.scope(key))
                try: self.run(body)
                finally: self.stack.pop()
            else: raise AssertionError(('unknown evaluated effect', key))
    def execute(self, body):
        self.validate(body)
        try: self.run(body)
        except BoundsFault as exc: return str(exc)
        return None
    def written_index(self):
        rows = [index for name, index, _ in self.writes if name == P + 'payload_entries']
        assert len(rows) <= 1
        return rows[0] if rows else None

cases = []
def add(name, expected, **params): cases.append((name, Fixture(**params), expected))
add('HIST_NEWEST_ZERO', 0)
add('HIST_OLDER_BEFORE_OPENING', 0, older=1500)
add('HIST_MIXED_NORMAL_SYSTEM', 7, older=31, later=7)
add('HIST_BOUNDARY_999', 999, later=999)
add('HIST_BOUNDARY_1000', 1000, later=1000)
add('HIST_SUBSEQUENT_1500', 1500, older=29, later=1500)
add('HIST_MISSING_SAVED', None); cases[-1][1].saved = None
add('HIST_MISSING_CURRENT', None); cases[-1][1].latest = None
add('HIST_ZERO_SAVED', None); cases[-1][1].saved = 0
add('HIST_FUTURE_SAVED', None); cases[-1][1].saved += 1
add('HIST_ABSENT_ROW', None); cases[-1][1].arrays[P + 'sequence_entries'].clear()
add('HIST_WRONG_SEQUENCE', None, later=3); cases[-1][1].arrays[P + 'sequence_entries'][3] += 100
add('HIST_WRONG_EVENT_ID', None, later=3); cases[-1][1].arrays[P + 'event_id_entries'][3] = 7
cases[-1][1].arrays[P + 'event_id_entries'][0] = event_id
add('HIST_MISSING_PAYLOAD', None); cases[-1][1].arrays[P + 'payload_entries'].clear()
add('HIST_MISSING_SECONDARY', None); cases[-1][1].arrays[P + 'secondary_actor_entries'].clear()
add('HIST_MISSING_SECONDARY_FLAG', None); cases[-1][1].arrays[P + 'has_secondary_actor_entries'].clear()
add('HIST_PENDING_FALSE', None); cases[-1][1].pending = False
add('HIST_IMPACT_LIVING_TARGET', 4, later=4)
add('HIST_IMPACT_DEAD_TARGET', 4, later=4, living=False)
add('HIST_IMPACT_MISSING_TARGET', 4, later=4, target=None)
add('HIST_MISS', 4, later=4, payload=miss)
add('HIST_FAIL_CLOSED', 4, later=4, payload=fail_closed)

fixture_sha = hashlib.sha256(json.dumps([(name, fixture.__dict__, expected) for name, fixture, expected in cases], sort_keys=True).encode()).hexdigest()
for name, fixture, expected in cases:
    original = copy.deepcopy(fixture)
    old_eval, actual_eval = AstEvaluator(fixture), AstEvaluator(fixture)
    old_fault = old_eval.execute(followup)
    actual_fault = actual_eval.execute(after_body)
    actual, old_index = actual_eval.written_index(), old_eval.written_index()
    assert actual_fault is None and not actual_eval.invalid, (name, actual_fault, actual_eval.invalid)
    assert actual == expected, (name, actual, expected)
    result = actual_eval.fixture
    assert result.latest == original.latest and result.saved == original.saved
    assert {k: len(v) for k, v in result.arrays.items()} == {k: len(v) for k, v in original.arrays.items()}, name
    writable = {P + 'payload_entries', P + 'secondary_actor_entries', P + 'has_secondary_actor_entries'}
    for key in result.arrays:
        if key not in writable: assert result.arrays[key] == original.arrays[key], (name, key)
        elif actual is not None:
            assert all(a == b for i, (a, b) in enumerate(zip(result.arrays[key], original.arrays[key])) if i != actual), (name, key)
        else: assert result.arrays[key] == original.arrays[key], (name, key)
    if actual is None:
        assert not actual_eval.writes, (name, 'partial writes', actual_eval.writes)
        assert result.pending == original.pending and result.outcome == original.outcome, name
    else:
        assert result.pending is False and result.outcome == result.payload
        assert actual_eval.temp[updated_key] == constant('constant:asteroid_incoming_runtime.one')
        if result.payload == impact and result.target is not None and result.living:
            assert result.arrays[P + 'secondary_actor_entries'][actual] == result.target and result.arrays[P + 'has_secondary_actor_entries'][actual] == 1
        else:
            for key in (P + 'secondary_actor_entries', P + 'has_secondary_actor_entries'):
                assert result.arrays[key] == original.arrays[key], (name, key)
    refresh_calls = [call for call in actual_eval.calls if call['name'] == 'refresh_events_log_system_history_views']
    assert len(refresh_calls) == int(actual is not None), (name, refresh_calls)
    if actual_eval.reads:
        first_read = next(i for i, row in enumerate(actual_eval.trace) if row[0] == 'read')
        checked_lengths = {row[1] for row in actual_eval.trace[:first_read] if row[0] == 'size'}
        assert {P + n for n in ('sequence_entries', 'event_id_entries', 'payload_entries')} <= checked_lengths, (name, 'identity read preceded bounds')
    if name in ('HIST_BOUNDARY_1000', 'HIST_SUBSEQUENT_1500'): assert old_index is None, name
    if name in ('HIST_BOUNDARY_1000', 'HIST_SUBSEQUENT_1500'): assert old_eval.ceiling_reached, name
    if name in ('HIST_NEWEST_ZERO', 'HIST_OLDER_BEFORE_OPENING', 'HIST_BOUNDARY_999'): assert old_index == expected, name
    print(f'{name}: before_written={old_index}, before_bounds_fault={old_fault is not None}, actual_after={actual}, pending={result.pending}, invalid_after=0')
bad_body = copy.deepcopy(after_body) + [('unmodelled_history_command', '=', 'yes')]
try: AstEvaluator(cases[0][1]).validate(bad_body)
except AssertionError: pass
else: raise AssertionError('unknown-command sentinel was silently accepted')
assert runtime_path.read_bytes() == after_bytes, 'after source changed during evaluation'
print(f'{len(cases)} actual before/after AST cases passed. Bounds first, unchanged matched body and success tail, unknown commands rejected. No native acceptance claimed.')
print('Fixture SHA256:', fixture_sha)
print('Before commit:', before_commit, 'Git blob OID:', before_blob_oid)
print('Before Git blob SHA256:', hashlib.sha256(before_bytes).hexdigest())
print('Before LF-normalized SHA256:', hashlib.sha256(before_bytes.replace(bytes([13, 10]), bytes([10]))).hexdigest())
print('After physical SHA256:', hashlib.sha256(after_bytes).hexdigest())
print('After LF-normalized SHA256:', hashlib.sha256(after_bytes.replace(bytes([13, 10]), bytes([10]))).hexdigest())
```
