# Event 039 retirement transaction review, 2026-10-07

Disposition: bounded retirement review closed on the final bytes below, R039-RET-01 closed in actual-source mock execution, required wider event MCP and native engine acceptance incomplete.
The original post-retirement revalidation and missing-tombstone bug is fixed in source for all three named retirement callers.
The subsequent fresh-consumption correction closes the conditional rejection defect found in this audit.
No remaining gameplay regression was found within the requested retirement/receipt scope at the recheck hashes below.
This report does not approve full Event 039 completion or the separate curated-host and historical-recruitment requirements.

## Final byte closure: unique-ID scan before mutation

Acceptance basis: the parent's final instruction requested closure on the supplied character/runtime/integration hashes and explicitly excluded restarting the unresolved full event graphs.
All three supplied hashes match the physical source bytes read and tested by the auditor.

| Final reviewed source | SHA-256 |
| --- | --- |
| `common/scripted_effects/039_murder_mystery_character_effects.txt` | `D555E20B0EA68B5E363AF0456632A96E03CB4DEE169C986A724A67AC25F89C0E` |
| `common/scripted_effects/039_murder_mystery_runtime_effects.txt` | `39AC5EBAB51C69A5B830FBD046BF5EB4A2D94B3C11CE208E5C69E59240BD3FCD` |
| `common/scripted_effects/039_murder_mystery_integration_effects.txt` | `8637B23CB3B6BA35757FCAAEF1E63DDF5E110F204CC5C43FE1F1ABD0990C4D87` |

The final consume helper at runtime lines 728-798 clears inherited consumption success, scans every bounded row for matching ID, counts matches and stores the matching index before any registry write.
Only an exact count of one admits the payload check at that stored index.
The subsequent check retains exact ID, generation, unused state, disposition, role, protection, owner and typed subject identity.
Both the tombstone write and fresh consumption receipt occur together inside the actual matching write block at lines 789-793.
An ID duplicated into a row with different generation/owner is rejected before either row is changed, even though the original row's full payload would still match.
The character helper additionally clears an inherited consumption receipt at guarded entry, line 25, while a recursive rejection leaves the outer transaction frame intact.
Frozen inputs, repeated national-leadership validation, native retirement/rollback gating and exact committed output identity remain intact.
Integration bytes are unchanged from the preceding accepted bounded recheck, retaining all three named caller gates and both generic fresh-consumption gates.

The auditor independently executed **41 of 41 permanent actual-source mock cases successfully**, including `duplicate_ID_before_MARK_rejected_without_mutation`.
That duplicate case injected a second matching ID immediately before the actual consume helper, retained distinct owner/generation payloads, and verified unchanged registry/rosters, no retirement, no fresh consumption success, named failure, no committed identity and complete private-frame cleanup.
The permanent used-row and native-no-op tombstone-preservation cases also remained passing.
The auditor independently ran three further in-memory API-boundary cases:

| Additional case | Result |
| --- | --- |
| No ID matches after API-boundary mutation | No row changes, retirement or success receipt |
| One matching ID moved to the second array index | Only that row consumed, exact victim retired once, frozen ID/generation committed |
| Duplicate ID with an entirely identical payload | Both rows preserved, no retirement or success receipt |

All three passed with stable source bytes, using the current actual helper bodies and the fixture owner's read-only mock interpreter.
The fixture runner was imported with `runpy` under `python -B`, and its file-writing `main()` was not called.
Current reviewed runner SHA-256: `5F21F039B4D0F2B0F38A9D2108A1A1C8377A67FA53C08F17110FE79B65FE542D`.
No fixture, result JSON, gameplay file or Git index was written by the auditor.
No remaining gameplay correction is recommended within this bounded retirement/receipt scope.
The existing graph, full caller accounting, native engine/persistence, curated-host and historical-recruitment limits remain separate and explicitly unresolved.
No unresolved full event graph was restarted for this final closure, as requested.
Only the exact new ID-scan effect fragment was submitted to `hoi4.script_validate` in COUNTRY scope, without broad graph analysis.
It returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, four checked commands, four unresolved unchecked argument blocks, eight findings and no omitted findings.
Checks performed cover syntax, command kind and declared scope, with `parametersChecked = false`, under installed-documentation revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The loop and variable argument semantics remain outside that checker, so this result does not promote mock/source acceptance into native validation.

The earlier rechecks and initial finding below are preserved as historical evidence.
This final byte closure controls current source/mock status and source identity.

## Earlier recheck: fresh-consumption correction accepted in source

Acceptance basis: the parent's explicit follow-up requested review of its distinct consumption receipt, repeated national-leadership check, generic caller receipt gates, and the two audit reproducers.
The parent owns gameplay implementation and permanent fixture changes.
The auditor independently reviewed the resulting source and executed its mock closure without editing gameplay, the index, or parent-owned fixture files.
The parent's reported transient apply_patch failure and successful retry introduced no additional audit blocker.
No fallback file replacement was used by the auditor.

| Current reviewed source | SHA-256 |
| --- | --- |
| `common/scripted_effects/039_murder_mystery_character_effects.txt` | `5034EED846BFA74D7E9726B298F7270A5D2C79D30A26A8D0D4A5CD889DF7018C` |
| `common/scripted_effects/039_murder_mystery_runtime_effects.txt` | `CCFFFD52C3AE4FE2F0D78A0F43296FD8BF8069CAD63BFAA6CB112A433C4BCD36` |
| `common/scripted_effects/039_murder_mystery_integration_effects.txt` | `8637B23CB3B6BA35757FCAAEF1E63DDF5E110F204CC5C43FE1F1ABD0990C4D87` |

Baseline remains HEAD `63f0799041f303d5d051dbdf22f8cd0bca5f7a48`.
Runtime and character trigger hashes and tuning/parser identities remain those recorded in the historical review below.
Current line references in this section refer to the new hashes above.

| Surface | Recheck status |
| --- | --- |
| R039-RET-01 | Closed in source and full actual-source mock. Character effects line 66 clears inherited consumption success after final preparation. Lines 69-74 repeat named eligibility, national-leadership role, saved disposition/protection and exact saved owner/character. Lines 78-124 enter both retirement and its rollback solely under fresh `target_consumption_committed`. Existing retired-row detection cannot admit that block. |
| Exact consume helper | Source and mock verified. Runtime line 729 clears its own output at every entry. Lines 746-775 verify ID, generation, unused state, disposition, role, protection, owner and typed subject identity. Lines 784-787 publish the new receipt only on an actual matching-row mutation. Named character and generic country-sentinel branches retain correct declared scopes. |
| Failed native retirement | Exact ordinary native-no-op rollback still passes. Character effects line 119 clears the fresh consumption receipt on successful row restoration. Already-consumed rows introduced during ruler resolution remain unchanged, including when native retirement is configured as a no-op. No restoration block is entered for those rows. |
| Exact named caller receipts | Source review complete. Opening at integration line 549 and foreign retirement at line 1250 still require caller-local `named_removal_committed` before publishing consequences. Named capture at line 1099 still returns committed ID/generation from the frozen frame and publishes persistent core-capture identity at lines 1105-1106. No ROOT substitution was introduced. |
| Generic baseline capture | Source review complete. Integration lines 1117-1125 consume first and publish capture flags, persistent ID/generation and valid-action result only under fresh consumption success. The previous shared trailing marker is removed. |
| Generic office casualty | Source review complete. Integration lines 1163-1172 consume first and gate casualty flags, achievement accounting, count, incident recording and cooldown on fresh consumption success. Context cleanup at runtime line 831 clears the new receipt. These complete integration bodies are source-reviewed rather than executed by the bounded fixture. |
| Opening Chaos, private lifecycle, recursion | Source behavior retained. Opening Chaos stays commit-gated. Existing private frame, guard, same-actor recursion, exact roster removal, rejected selection and helper temp-frame cases pass the current runner. |
| MCP/native acceptance | Still incomplete. Historical inspect/compare timeouts, empty focused render selection, source-index continuation staleness and partial whole-helper validation remain separate limits. New read-only recheck calls are recorded below without converting source/mock evidence into engine evidence. |

### Independently executed recheck

The auditor read the fixture owner's additions and imported the current `validation/retirement_transaction_2026_10_07/run_fixture.py` with `runpy.run_path(..., run_name="audit_readonly")` under `python -B`.
The auditor called `Sources()` and every `cases(src)` case directly, never the file-writing `main()`.
All **40 permanent actual-source cases passed**, with stable source bytes through execution.
The permanent cases now include role mutation before final revalidation and four used-row/tombstone cases with an inherited stale consumption receipt, including native-no-op configurations.
Current reviewed runner SHA-256: `4589CA070F4ECD025222D17D20EC2A953CFFBEEDC6FEC977388F1AB8E06B05D2`.
Current reviewed owner-saved results SHA-256: `1F9DA8574C884B639AF328E4014335A22780D97D58F13D9094C2AD8238AC4D80`.

The auditor also reran its original post-ruler-capture reproducers independently at the original `after: capture_current_ruling_character` boundary, extending both to native-removal and native-no-op configurations and seeding an inherited fresh-consumption flag.
All four variants passed the complete rejection, identity-output, registry/roster preservation and cleanup assertions:

| Original reproducer | Native configuration | Retire calls | Consume-helper calls | Named commit | Entire injected registry preserved |
| --- | --- | ---: | ---: | --- | --- |
| `MIDCALL_ROW_ALREADY_REMOVED` | Native removal | 0 | 0 | false | yes |
| `MIDCALL_ROW_ALREADY_REMOVED` | Native no-op | 0 | 0 | false | yes |
| `MIDCALL_ROW_USED_ONLY` | Native removal | 0 | 0 | false | yes |
| `MIDCALL_ROW_USED_ONLY` | Native no-op | 0 | 0 | false | yes |

Each variant retained the entire recruited roster, set named failure, cleared inherited consumption success and omitted both committed ID/generation fields.
The ordinary failed-native case continues to restore only its own consumed row, while these four rejection cases preserve another operation's consumption unchanged.
This closes R039-RET-01 within the same explicit adversarial mock boundary used to discover it.
The mock models synchronous native roster removal/no-op, exact mock identities and trait operations, not engine callbacks, native pointer lifetime, country recruitment, save persistence or complete caller accounting.
The separate curated-host, native historical-recruitment, owner callback and successor-installer requirements remain unresolved and are not certified by these tests.

### Remaining work and disposition

No additional gameplay correction is recommended by this bounded recheck.
Retain the permanent cases and obtain usable MCP event inspect/render/compare and native evidence before making a wider completion claim.
Full caller execution, opening Chaos accounting, native persistence and full host curation remain outside the executed closure.
The parent updated `common/scripted_effects/039_murder_mystery_character_effects.md` lines 11-13 to distinguish fresh consumption from tombstone detection and document typed owner/subject matching.
No corresponding helper-documentation gap remains for R039-RET-01.
No plan was promoted or broader design departure approved by this recheck.
Skills retained from the initial review: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-event-planning`, and `chaos-redux-improvement-loop`, with no skill changes.

### Recheck MCP receipts

The current helper body was checked in COUNTRY scope with full `event_target:` bindings and exact `var:global...^murder_mystery_removal_row` bindings for its rollback country/character pointers.
`hoi4.script_validate` returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, 58 checked commands, 24 unresolved findings, 17 unchecked argument blocks and 57 omitted findings of 81.
Checks performed remain syntax, command kind and declared scope, with `parametersChecked = false`.
This preserves the distinction between source/mock closure and native validation.
The installed documentation revision remains `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.

`hoi4.source_lookup` successfully located current character-effects line 79 as the fresh-consumption limit inside `murder_mystery_retire_selected_leader`, source-location revision `79e1ef7e8c0a23ef4a3f795debbe0bf3da815cc27e1ec46c4be6dca053e1a473`.
It reported the owner definition at lines 17-133 and the exact nested key path `if[0] / if[0] / if[1] / if[1] / limit[0]`, with complete location coverage and no chain truncation.
This proves the source location, not execution or complete helper-consumer coverage.

Refreshed ordinary event requests were submitted for root `chaosx.nr39.1`: trace both directions at depth 1 with ten nodes/edges, scope render at depth 1 with ten nodes, and current-to-HEAD three-file in-memory comparison with chain/render bounds ten and render false.
No refreshed graph/render/comparison result had been returned at the recheck's observation cutoff.
Their completion remains unresolved, and the historical 600-second inspect/compare timeouts and empty focused render remain the recorded event-evidence limits.
The recheck collection cell was terminated after retaining the returned script-validation and source-location receipts.
Termination of that collection is not a claim that the server-side read operations were cancelled or completed.
No native job/task route or source-changing fallback was used.

## Historical initial audit, superseded as current status

Everything below preserves the pre-fix finding, reproducers, old source identities and initial tool receipts.
The latest recheck above controls current status.
Historical failed-case outputs and recommendations are retained as before evidence, not open gameplay findings.

## Scope, authority, and source identity

The parent requested a read-only review of the current retirement diff against HEAD, then explicitly added private-input freezing, final selection revalidation, committed ID/generation outputs, and moving opening Chaos into successful commit.
That instruction is the acceptance basis for this bounded audit.
Full curated host eligibility and native historical recruitment remain separate known unresolved requirements and are not classified as regressions here.
Only this report was written by the auditor, with no gameplay, index, commit, game launch, or log changes.

Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Baseline HEAD: `63f0799041f303d5d051dbdf22f8cd0bca5f7a48`.
Paths below are workspace-relative, and line numbers refer to the final reviewed hashes.

| Source | Final reviewed SHA-256 | HEAD Git blob |
| --- | --- | --- |
| `common/scripted_effects/039_murder_mystery_character_effects.txt` | `BD1A6CE62C1E1A4259939072A17D18B13D77205FB1947289AD6581B2722D66A1` | `725c0a85c26ee03dc4c43d7e35b4f2119b2662cd` |
| `common/scripted_effects/039_murder_mystery_runtime_effects.txt` | `63B6E982AF58BA599C86EDA7AB2512AEFB994D4F81B938B898A7E527B926EE78` | `c6c2482e332e5238394c58333cc234e218967138` |
| `common/scripted_effects/039_murder_mystery_integration_effects.txt` | `C9A895347AEE8DF9532AA061D39D58A085A961F71B8469B5385F338BD51157FB` | `4186db1148487d7b94c171b63c766ba5bd7ffeb8` |
| `common/scripted_triggers/039_murder_mystery_runtime_triggers.txt` | `8DF841A6BC23A8C2A63611AA9A487554CADBAD716528F79483C281DD9EE85DCD` | Validator unchanged in the scoped diff |
| `common/scripted_triggers/039_murder_mystery_character_triggers.txt` | `E4ADD526F07512119F21851C5A876A2E67725806B815CF516557816F9834A7C6` | Recruitment predicate unchanged in the scoped diff |

The first character snapshot was `7D432EDF7E70DBFCCBC6B6C0AECD9546C7EF7DAFB172F55E10081E9E6CF5B614`.
Its later private-input and final-revalidation changes were re-read and are included in this report.
Integration snapshots `4402678251A01625AA390C39D05283DD02BDB39FADCDF64A99A035FC86270F1D` and `D463753144DF87350FC278CE64EA122003864EA396655FBBFAD07F03B9163551` are superseded by the final hash above.
Other agents continue changing the shared workspace, so this is a hash-bound review rather than approval of later bytes.
Runtime snapshot `E65BD957DC1887C79743B589AA48AA5F77D07C52E8656A6B1B85C7BBD9722A19` was superseded during final review by direct role, owner and subject comparisons in the consume helper.
The latest marker at runtime lines 728-785 was re-read, including its separate named-character and generic-country subject branches.
The parent fixture's initial owner, subject and role findings are closed at the final runtime hash above.

## Actionable finding

### R039-RET-01: an already-consumed row can authorize retirement after rejected revalidation

Priority: P2 conditional transaction-hardening defect, with reproducible full actual-source mock behavior and unproven normal-play reachability.
Evidence: character effects lines 61-76 and runtime effects lines 639-646.
The second `murder_mystery_prepare_safe_target_action` sets `murder_mystery_selected_target_retired` when validation finds disposition `already_removed` or `used = 1`.
The exact-owner/character and named-action gate then rejects consumption at character effects lines 64-73.
The following independent block at lines 74-76 nevertheless authorizes native `retire` from that same flag.
Consequently, the flag proves either an existing tombstone or this call's successful consumption, and cannot distinguish them.
With a still-recruited private victim and surviving successor, the later roster postcondition can also publish a committed receipt despite no row being consumed by this invocation.
If native retirement instead fails, the rollback can restore a pre-existing matching tombstone because it likewise has no separate proof that this invocation consumed it.

Concrete injected case: the first validation accepts row ID 401, generation 7, owner ENG, character V, eligible national-leadership disposition, normal protection, and `used = 0`.
The ruler-resolution boundary changes that exact row to an already-removed, hardened, used row while V remains recruited and distinct successor S remains the ruler.
The second preparation rejects named action but sets the retired flag, so the final retirement block still runs.
This mutation is a declared adversarial fixture, not an observed engine callback.
The full source mock reproduced both used-only and removed/hardened/used mutations at its existing `after: capture_current_ruling_character` injection boundary.
Each invoked native retirement once, called the consume helper zero times, and published committed ID 390003 and generation 17.
The used-only case left disposition eligible and protection normal despite reporting committed success, further exposing the missing fresh-consumption proof.
The current ruler helper's scripted body does not itself change registry rows, and recursive calls to the new retirement helper are blocked by its global guard.
No ordinary current caller was proven to create this mutation.

Recommended owner change: use a distinct fresh consumption receipt, initialized immediately before this invocation's consumption attempt and set only when its exact row is actually changed.
Gate native retirement and rollback on that receipt, or place retirement inside the accepted exact-selection block and ensure the consumed flag cannot be inherited from revalidation.
Preserve existing tombstone detection for selection rejection.
For the advertised national-leadership-only contract, also consider repeating the role check at the final selection gate if mid-call registry mutation is intended to be supported.
Role mutation was not an executed case in this audit.

## Completion status by surface

| Surface | Status and evidence |
| --- | --- |
| Original tombstone defect | Fixed in ordinary source flow. Consumption now precedes `retire`, and opening/foreign callers no longer re-approve the absent character afterwards. Named capture's trailing mark at integration lines 1125-1129 is skipped because its already-consumed selection is no longer registered. |
| Caller and ROOT scopes | Source review finished. Receipts and frozen scalar inputs live on the current caller country. Entering owner/character scopes does not change ROOT, and the helper never reads receipt identity through ROOT. |
| Exact consumption | Partial. Final preparation restores frozen ID/generation, compares saved disposition/protection and exact saved owner/character, then invokes the marker. The latest marker additionally checks current ID, expected generation, unused marker, disposition, role, protection, exact owner and disposition-specific subject identity. Its three initial identity findings are closed, and named/generic matching cases pass the full source mock. R039-RET-01 still prevents calling the helper's rejection contract complete. |
| Protected/stale input rejection | Source-supported at entry. Missing, protected, owner-managed, generic, used and stale-generation selections fail the initial named gate. The reduced fixture confirms rejection of protected and stale unused rows at the later retirement gate. Mid-call consumed rows fail that fixture. |
| Private target lifecycle and recursion | Source-supported. Victim, owner and successor use private regular event targets, with a fresh resolved-ruler flag guarding any stale successor alias. The active global guard rejects another retirement helper before it can replace private inputs. Guard-owned normal exits clear all four private scalar fields and the guard. A rejected recursive call preserves the outer frame. |
| Failed native retirement rollback | Implemented in source and passed the full actual-source mock's native-no-op case, engine runtime unverified. Restoration requires aligned arrays, still-present victim, exact saved ID/generation/owner/character, and the removed/hardened/used triplet. An absent victim keeps its tombstone even if successor or owner postconditions fail. This restores the registry row, not the already-installed successor or all prior politics. |
| Public receipts | Implemented in source. Success alone publishes caller-local committed ID/generation. Failed calls clear prior committed output, and `clear_selected_target_context` clears both outcome flags and output fields. All three callers check committed success before publishing named consequences. |
| Opening Chaos | Implemented in source. Preparation no longer invokes the mapped opening consequence. Integration lines 579-581 apply it after successful removal and successor receipts inside commit. Refused preparation or retirement never reaches that block. Repeat rejection is supported by the consumed-row selection gate, subject to the separately unexecuted lifecycle cases below. |
| MCP/event acceptance | Blocked or partial, as detailed below. Source review and the reduced branch fixture are not equivalent engine evidence. |

### Every current retirement caller

| Caller | Actual current country and ROOT distinction | Receipt consumption |
| --- | --- | --- |
| `murder_mystery_install_verified_successor`, integration line 549 | Chosen opening host. Natural `.1` uses that host as ROOT. Manual launch enters the selected host from the launching country, retaining the launcher's ROOT. | Tests host-local committed removal, then publishes opening removal and successor flags. |
| `murder_mystery_apply_safe_target_resolution`, integration line 1099 | Investigation actor. The saved target owner is the recorded Assassin State and can differ from both caller and ROOT. | Tests actor-local committed removal and copies committed ID/generation into persistent global core-capture receipts at lines 1105-1106. The old capture-actor alias is removed. |
| `murder_mystery_execute_foreign_leader_transaction`, integration line 1250 | Victim government. High-value operation enters the selected cell country at decision effects line 1483, retaining the operation initiator's ROOT. Terminal replacement runs in the dismantled government's scope at lifecycle line 1398, retaining its outer event context. | Tests government-local committed removal, then publishes government-local foreign transaction outcome. The decision owner reads that government's persistent outcome after return. |

The runtime marker also remains called by the baseline generic capture path and generic office casualty path at integration lines 1129 and 1167.
Those paths do not invoke native retirement and retain their existing generic eligibility gates.
Repository gameplay searches found exactly three calls to the new retirement helper and one remaining native `retire = yes` in Event 039 effects, inside the helper.
The MCP reference index did not provide complete consumer coverage, so this caller inventory is source-search evidence.

## Executed fixtures and remaining acceptance cases

After the parent's follow-up, the auditor read `validation/retirement_transaction_2026_10_07/run_fixture.py`, its full handoff and current results under this Event 039 plans folder.
The current saved results contain 35 passing cases, extending the parent's reported 31 cases with four generic-office/owner-managed sentinel cases.
The auditor independently imported the runner using `python -B` and `runpy.run_path(..., run_name="audit_readonly")`, then called `Sources()` and iterated `cases(src)` directly.
The runner's `main()` was never called, so `results.json` and every other parent-owned file remained unwritten by this audit.
All 35 existing cases independently passed with stable source bytes, including owner/subject/role mutation just before consumption, generic sentinel matching/mismatch, exact failed-retirement rollback, distinct ROOT, recursive entry and temporary call-frame cleanup.
The caller integration file is hashed by that runner but its bodies, Chaos helper and successor installer are not executed.
These are bounded mock-native cases, not engine validation.
The auditor then added two in-memory cases at the runner's existing post-ruler-capture boundary, without changing the runner or its saved results.
Both reproduced R039-RET-01.
Reviewed runner SHA-256: `DE5FF0DD45DDCDFCDB41C72A8BB90AB72A3B5032BD0C06BDC86F4DCC7EA988CA`.
Reviewed saved results SHA-256: `88A8FDF905CA7121F061C2CD2CDB44A93E8E345AAA5DA265BE405EC6DE67AE70`.

The executed JavaScript fixture parsed the actual final helper's Clausewitz text and the unchanged HEAD validator with a small in-memory parser.
It selected the validator block that sets `selected_target_retired`, the actual consume block, and the actual following retirement gate.
It evaluated the validator's disposition/used conditions, supplied named-action eligibility and consumption success as declared inputs, and counted whether the actual retirement gate admits execution.
It did not execute the full helper closure, roster effects, native retirement, callbacks, temporary-variable call frames, arrays, rollback, or the game.
No fixture file or gameplay stub was installed.

| Fixture ID | Second-validation disposition / used | Named action allowed | This invocation consumes row | Expected retirement invocation | Actual branch result |
| --- | --- | --- | --- | ---: | ---: |
| `NORMAL` | eligible named / 0 | yes | yes | 1 | 1 |
| `MIDCALL_ROW_ALREADY_REMOVED` | already removed / 1 | no | no | 0 | **1, failure** |
| `MIDCALL_ROW_USED_ONLY` | eligible named / 1 | no | no | 0 | **1, failure** |
| `MIDCALL_PROTECTED_UNUSED` | temporarily protected / 0 | no | no | 0 | 0 |
| `MIDCALL_STALE_UNUSED` | eligible named / 0 | no | no | 0 | 0 |

Parent fixture contract for a full actual-source interpreter or other supported scenario route:

```json
{
  "actor": "ENG",
  "root": "GER",
  "row": {
    "id": 401,
    "generation": 7,
    "owner": "ENG",
    "character": "V",
    "role": "national_leadership",
    "disposition": "eligible_named_target",
    "protection": "normal",
    "used": 0
  },
  "owner_roster": ["V", "S"],
  "owner_ruler": "S",
  "owner_successor_receipt": "emergency_successor_installed",
  "expected_generation": 7,
  "owner_callback_passed": true,
  "inject_after_ruler_resolution": {
    "same_row_disposition": "already_removed",
    "same_row_protection": "hardened",
    "same_row_used": 1
  },
  "expect": {
    "native_retire_calls": 0,
    "named_removal_committed": false,
    "named_removal_failed": true,
    "row_remains_used": true,
    "victim_remains_recruited": true
  }
}
```

This JSON is a fixture contract, not an asserted live MCP schema or a claim that these campaign tags satisfy full curated host eligibility.
Use exact installed constants and typed engine/source bindings in the parent's chosen runner.
Freeze the three reviewed files and record fixture hashes before comparing results.

Reproduce the two added cases against the parent's runner without invoking its file-writing main:

```python
import runpy

m = runpy.run_path(
    "docs/plans/039_murder_mystery_plans/validation/retirement_transaction_2026_10_07/run_fixture.py",
    run_name="audit_readonly",
)
src = m["Sources"]()
for removed in (True, False):
    world = m["World"](src)

    def mutation(w, scope, removed=removed):
        w.setrow("used", 1)
        if removed:
            w.setrow("disposition", 7)
            w.setrow("protection", 3)

    world.hooks["after:" + m["CAPTURE"]] = mutation
    world.retire()
    native = [t for t in world.trace if t.get("native") == "retire"]
    print({
        "removed_triplet": removed,
        "expected_retire_calls": 0,
        "actual_retire_calls": len(native),
        "consume_calls": world.calls.get(m["MARK"], 0),
        "committed": m["P"] + "named_removal_committed" in world.flags[world.caller],
        "row": world.row(),
    })
assert src.stable()
```

Observed for each case: `actual_retire_calls = 1`, `consume_calls = 0`, and `committed = true`.
The runner uses exact current constants, so the numerical disposition/protection inputs here match its saved source hash rather than being proposed gameplay tuning.
Remaining cases outside the executed 35-case closure include successful complete opening/capture/foreign caller integrations, stale inherited successor aliases, duplicate IDs or misaligned arrays, recursive different-actor entry, moved/missing victim retaining tombstone, missing successor after removal without committed success, mismatching rollback identity preserving unrelated rows, context clearing invalidating receipts, consumed-row reconciliation preserving the tombstone, and failed/repeated opening producing no additional mapped Chaos.
All native engine behavior and persistence remain unexecuted by this auditor.

## MCP and reference evidence

Connected workspace ID: `mod_chaos_redux_ea3b2d67c2c0`.
Ordinary live reference, source, script validation, event inspect, event render and event compare routes were exposed and called.
No helper-expansion, native-task, job, GUI, map, focus, technology, probability, or game route was used.
The scoped patch changes deterministic retirement/receipt handling and mapped Chaos placement, with no changed AI weight, MTTH, random pool or probability-bearing target-selection calculation.
Existing weighted host selection and event option pools were excluded from this bounded audit rather than represented as audited.

- `hoi4.event_inspect`, root `chaosx.nr39.1`, trace both directions, depth 2, nodes 30, edges 50: initial request and a later retry both returned `timed out awaiting tools/call after 600s`.
- `hoi4.event_compare`, same root, current-to-HEAD in-memory overlays for all three named effect files, render false, chain/render bounds 30: returned `timed out awaiting tools/call after 600s`.
  The corrected overlay field was `source`, not `content`.
  No comparison result or helper semantic delta was inferred.
- `hoi4.event_render`, same root, scope view, depth 2, nodes 30: `EVENT_RENDERED_PARTIAL`, revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0`, focused analysis, helpers 0, selected nodes 0, one blocking diagnostic, and failed event-analysis validation.
  Its JSON was read and reports `complete = false`, empty selected nodes/edges, and the expected mod event file hash `749105e395578f57f0af0c9937d593dc252495d920d05dd568a8611aa3661892`.
  This empty selection is a tool-evidence gap, not proof that Event 039 is absent or valid.
  Focused analysis excludes scripted-helper lifecycle projection regardless of the narrow root, so it could not validate this retirement helper even with a populated selection.
- Successful `hoi4.source_lookup` located the helper at lines 17-128 under workspace-index revision `50dfcd0ce5410e538d5c534c46cfe60dae28cb20b999e8be38f68520cda4ac67`.
  The returned source page covered only lines 17-51 and supplied `nextLine = 52`.
  References were incomplete, with 19,777 unresolved references and no returned consumers.
  The revision-bound continuation returned `SOURCE_REVISION_STALE`, current index revision `d100077377fd73c712a075e2647b3f374153ba52c17ee4bd449c42d1d0055edd`.
  Shared-tree changes prevented treating separate pages as one frozen MCP source review.
  The entire relevant source was read locally and hash-bound above.
- `hoi4.script_validate` for `retire = yes` in CHARACTER scope returned `SCRIPT_CHECKED`, `valid = true`, covering syntax, command kind and declared scope only.
  `parametersChecked = false`, so this does not prove engine retirement or pointer behavior afterwards.
- The revised marker's owner-country `tag` and subject-character `is_character` checks were separately validated with fully qualified `var:global...^murder_mystery_target_registry_index` and `event_target:` bindings.
  This returned `SCRIPT_CHECKED`, `valid = true`, two checked commands, no unresolved or omitted findings, and `parametersChecked = false`.
  It supports the declared COUNTRY/CHARACTER split, with dynamic array identity and native execution still outside that checker.
- The complete added helper body was checked in COUNTRY scope with fully qualified `event_target:` bindings for owner, victim, ruler and successor.
  It returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, 56 checked commands, 23 unresolved findings, 16 unchecked argument blocks, and 54 omitted findings out of 78.
  The remaining unresolved coverage includes scripted helper calls, argument semantics and dynamic variable scopes in rollback.
  Bare binding names in the initial attempt were corrected and are not treated as a native-scope defect.
  A separate owner-roster postcondition check likewise remained partial because `any_character` argument blocks were unchecked.

Retained render artifacts:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7af44412d70e85ad9b9c9ef340c43c09eff46bba1699a9201724f97003887250/e5886fe6b3cadd07cf9b07f7f1f6c441f06423270c9c288c9134d7da41b0051e/event-scope-8f4a82aa5d84.json`
- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8939c1c65931ecbd355dd889f005d94fdb1a952eb5f8ba4cd1923f5deead6ea4/c8b6ed6256cd906b6fa81d8e3cd5b18254c617440a801ef750af93f89ae88c4a/event-scope-8f4a82aa5d84-manifest.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7ce81c138d6f6b7d7a4967239648f5dabc3f8c68d435abeb17494dc88eaa960/f20151207f6f6274932e41c71501b44182ed2382841122b4a841d6dea5d2f5db/event-scope-8f4a82aa5d84.svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27fa8b15514f42f7814e25971599e94e51e4af14689066e83e3a7e71025bcc7d/ab0f5296cef0b6ac5784d04c3516524d3ce335bceb49174ceed820de80b034e7/event-scope-8f4a82aa5d84.png`

Read installed references: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, retirement lines 6427-6435, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Read installed trigger sections locally: `triggers_documentation.md`, `any_character` lines 1272-1280 and `is_character` lines 5345-5353, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
Read offline wiki sections through the live reference route: `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md`, ROOT line 265 and retirement line 3815, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
Read `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, event targets lines 263-269 and regular targets lines 303-328, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
The context bundle had omitted topics, so it was used as discovery rather than a claim that every core section was read.
The reference contract here covers retirement, identity, scopes and target lifetime only.
Vanilla precedent inspected locally: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\SOV_scripted_effects.txt`, character-scoped retirement at lines 4224-4226, SHA-256 `CC9E16837AFA1428D11E053DC982446B35587980DAA011A1DF12114C3ACE2BF4`.
It establishes a character-scope source precedent, not Event 039 runtime acceptance.

## Documentation, disposition, and parent next actions

The current helper API doc describes outputs, private target lifetime, rejection defaults and rollback, and `docs/events/039_murder_mystery.md` lines 34-39 describe unified retirement and commit-gated opening Chaos.
Their broad used-target rejection claim needs the R039-RET-01 fix or an explicit limitation for mid-call consumed rows.
No additional portrait, asset, animation, dedicated GUI or catalog feature was introduced by this scoped diff.
No asset handoff or broader Event 039 plan was promoted, rejected, superseded, or certified by this audit.
The wider unresolved dispositions in `docs/plans/039_murder_mystery_plans/resume_2026_10_07.md` remain with the parent.

Parent next actions are to distinguish fresh consumption from existing tombstone detection, run the supplied mid-call used-row cases and the full rollback/scope/receipt cases against frozen actual source, and obtain usable Event 039 inspect/render/compare evidence without treating these source findings as engine proof.
Keep the known curated-host and historical-recruitment issues separate from this bounded fix.
No audit-side gameplay simplifications were made because gameplay was not changed.
The reduced branch fixture and the full source runner both have explicit mock-native limits, and all omitted runtime verification is explicit above.

Skills read and applied: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-event-planning`, and `chaos-redux-improvement-loop`.
Planning guidance was used for evidence/disposition boundaries, with no new expansion or planning pass.
No skill was created or edited.
