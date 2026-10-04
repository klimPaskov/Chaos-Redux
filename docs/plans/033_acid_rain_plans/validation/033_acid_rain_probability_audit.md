# Event033 cluster pacing baseline, 2026-10-03

Disposition: `blocked` for MCP probability evidence.
Baseline preservation, named fixture construction, and source review are complete.
All three numerical probability, weight-delta, and timing conclusions remain `unresolved`.
This handoff covers the narrowed cluster-pacing follow-up, not completion of the earlier Event033 decision and weather-pool audit.

## Authority and scope

The parent requested one live route revalidation and a read-only baseline for `on_event_cluster_global_pacing_update`, `on_major_event_fired`, `reset_major_event_pacing_state`, and Event033 paths through the Natural Disasters cluster.
The required behavior is one Major pacing commitment at successful launch whenever Event033 is in the prepared queue, with no later Major reset from that member.
The acceptance basis is the parent's 2026-10-03 follow-up and `docs\specs\033_acid_rain_specs\specs\033_acid_rain_spec_part_7_evolutions_and_cluster_integration.md:231-246`.
That spec explicitly requires effective Major pacing for a queue containing Event033, one launch reset, separate member history, and reservation release if a later terminal change cancels the member.

Repository root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Current `AGENTS.md`, `chaos-redux-subagents`, and `chaos-redux-events` guidance were applied.
No gameplay, weight, timer, trigger, localisation, achievement, or CXT registration source was edited.
No balance target was selected.
The parent retains the patch and final integration.

## Immutable baseline and fixture identities

The before directory is `docs\plans\033_acid_rain_plans\validation\probability\baseline_2026_10_03\cluster_pacing`.
Each copied source was verified against its originating bytes and marked read-only.
At handoff verification, all eight current source files still matched these copies.
The shared pacing sources already contained other working-tree changes when copied, and those changes were preserved.

| Exact source | Snapshot filename | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `common\scripted_effects\chaosx_logic_effects.txt` | `chaosx_logic_effects.txt` | 69942 | `433362223952AE687FA98F87176167D7931B7EB4D930236EAB3A8A4247A4C644` |
| `common\scripted_effects\chaosx_event_cluster_effects.txt` | `chaosx_event_cluster_effects.txt` | 288145 | `7B51BD7B123ABF479518A899E6AA33BB2582C4937BFC748E5AEA22C0094D02FC` |
| `common\script_constants\event_system_constants.txt` | `event_system_constants.txt` | 3445 | `36EC922AC2E290A15227CC1E65C4CC6E2575E60B3E9C68D2C9BE0E5B0E45D79C` |
| `common\script_constants\event_cluster_constants.txt` | `event_cluster_constants.txt` | 10484 | `E74A71FA4612452F80DFB651D762B39EB5AD6DD7EB41A3D08FA1FA5E741D349F` |
| `common\script_constants\033_acid_rain_constants.txt` | `033_acid_rain_constants.txt` | 29421 | `FF4A37AD60E6AE6F879736B6A178A5436BDD1104A66272C15F65AAF83A543CDD` |
| `common\scripted_effects\chaosx_settings_effects.txt` | `chaosx_settings_effects.txt` | 169035 | `FD3EADD5526A56493CC54ED765C27EF4AA1FD9088488974B4738723E5D181E59` |
| `common\script_constants\settings_constants.txt` | `settings_constants.txt` | 2406 | `AB715D8B7866320B38095409024DA95B24ED6C0F9D0717F8FA685F58E80E4DFC` |
| `events\chaosx_event_clusters.txt` | `chaosx_event_clusters.txt` | 550 | `031D978464B930E2A07402A0EE249E0218081F3CD5C82D9E40857366C8A32B05` |

The [hash manifest](probability/baseline_2026_10_03/cluster_pacing/SHA256SUMS.txt) also binds the fixture and route receipt.
The [saved fixture](probability/baseline_2026_10_03/cluster_pacing/cluster_pacing_scenarios_2026_10_03.json) has SHA-256 `049E1784FD43B3962B28D9196EF69861D2F74910BFF64AC325033ED02CCEADB4`.
Its scenario-set ID is `event033_cluster_pacing_baseline_2026_10_03`.
The [route receipt](probability/baseline_2026_10_03/cluster_pacing/cluster_pacing_route_receipt_2026_10_03.json) has SHA-256 `AFCF036C12DC9B0A21E081FFA3DC7F8A8D5B3F82CF781E8921CE8773D5AC1C95`.
These are local byte hashes, not MCP scenario hashes or source revisions.

The earlier three Event033 source snapshots remain separately preserved in the parent `baseline_2026_10_03` directory with their own `SHA256SUMS.txt`.
Their preservation does not establish the wider audit's completion.

## Live MCP route evidence

Routing metadata was revalidated once.
The probability inspection, evaluation, sweep, comparison, and render tools were exposed.
No dedicated HOI4 health tool was exposed, so the required source inspection was the live service check.
The current `source_lookup` metadata did not accept `view` or `keyPath`, and no such fields were used.

The first weighted-system call for this follow-up was:

```json
{
  "source": { "path": "common/scripted_effects/chaosx_logic_effects.txt" },
  "refresh": true
}
```

Tool: `hoi4.probability_inspect`.
No adapter was preselected because the call was intended to discover the source's supported weighted surface.
The live result was `isError = true` with this exact error:

```text
tool call error: tool call failed for `hoi4_agent_tools/hoi4.probability_inspect`

Caused by:
    timed out awaiting tools/call after 600s
```

No adapter inventory, artifact URI, source revision, analysis ID, scenario hash, comparison ID, or rendered evidence URI was returned.
At the initial handoff, only that one requested revalidation had been attempted.
The subsequently authorized helper-filtered retry is recorded below.
The fixture is persisted but has not been accepted by the live scenario schema or evaluated by MCP.

| Result classification | Evidence available |
| --- | --- |
| Exact | None |
| Bounded | None |
| Sampled | None |
| Score-only | None |
| Unresolved | All three scenario timer distributions, effective weight changes, and campaign selection consequences |

## Three unchanged named scenarios

All cases use the same source-default pacing inputs, one existing-country dispatcher (`GER`), successful selected-member dispatches, and no unrelated event or settings mutation between stages.
The complete registered Natural Disasters catalog is present in the fixture: five Event013 logical rows (`5001` through `5005`), Event033 row `5006`, and Event051 Heat Wave row `5007`.
Only the opening Event013 row and, where declared, Event033 are selected.
This audit conditions on those already prepared orders and makes no claim about optional participation probability.

| Scenario ID | Complete declared selected order | Baseline source trace | Required behavior | MCP classification |
| --- | --- | --- | --- | --- |
| `natural_disasters_without_33` | `13` | Minor launch path, no delayed Major member | One Minor launch commitment | Unresolved |
| `natural_disasters_optional_33_after_13` | `13, 33` | Minor launch path, then `reset_major_event_pacing_state` at delayed Event033 dispatch | One Major launch commitment, no later Major reset | Unresolved, source contract mismatch identified |
| `natural_disasters_33_trigger` | `33, 13` | Initial Major flag routes launch through Major pacing, delayed Event013 adds no Major reset | One Major launch commitment, no later Major reset | Unresolved |

The selected queue is complete for each fixture.
The full ordinary-event active pool and all its eligibility, caps, recovered weights, and external strategy or campaign state are not declared, so normalized event-selection probabilities are unavailable.
Major gain depends on that active pool and has no evaluated numeric delta.
The timer's Chaos flag binding, live settings, Event008 pressure helper, current runtime state, and engine rounding remain unresolved.
Actor validity, member prevalidation, successful dispatch, closed initial context flags, and queue drain are explicit fixture assumptions rather than runtime observations.
The fixture records the delayed-stage schedule and terminal state in its contract because no live timing-scenario schema was returned.

## Source trace and tuning inputs

These are source observations supporting the handoff, not substitute probability or engine evidence.

`chaosx_event_cluster_effects.txt:242-249` registers Natural Disasters as repeatable.
`chaosx_logic_effects.txt:237` registers Event033 in `global.major_events`.
`event_cluster_prepare_acid_rain_reservation` at `chaosx_event_cluster_effects.txt:2578` scans the prepared order and sets `acid_rain_cluster_reserved` when Event033 is present, but does not establish an effective Major pacing type.

`fire_event_cluster_by_temp_id` sets `event_cluster_initial_trigger_dispatch` before the first member and clears it afterwards at `chaosx_event_cluster_effects.txt:4132-4148`.
After successful dispatch, it calls `on_event_cluster_global_pacing_update` at line `4185`.
That helper at `chaosx_logic_effects.txt:1135` tests the initial-Major-dispatched flag, then the registered cluster type.
It does not test the prepared queue's selected Event033 membership.
This explains the optional33 case's Minor launch path.

`fire_event_cluster_member_by_temp_id` at `chaosx_event_cluster_effects.txt:2645` applies `event_cluster_member_fire_context` during a member dispatch.
For Event033 it uses `fire_event_by_temp_id_no_cluster`.
The generic dispatcher calls `on_major_event_fired` for a Major at `chaosx_settings_effects.txt:4473-4475`.
The Major handler at `chaosx_logic_effects.txt:1258-1264` sets the initial-Major flag during the initial trigger, but otherwise calls `reset_major_event_pacing_state` for a delayed cluster Major.
That delayed reset does not add a second `global.total_events_fired` increment or recovery step, but does reset Major pacing state.

`reset_major_event_pacing_state` at `chaosx_logic_effects.txt:1127` clears the Minor-since-Major counter, resets unfired Major weights, calls the Major timer update, clears current Major weight, and recalculates dynamic Major gain.
`on_major_event_timer_update` at line `502` clears both timer compression variables and calls `calculate_next_timer_value`.
The optional33 case therefore has a later timer redraw and Major-weight reset in addition to its Minor launch pacing path.
The source trace corroborates the parent's identified mismatch.
The numerical size, selection impact, or timing distribution has not been proved.

| Source input | Baseline value or operation |
| --- | --- |
| Timer defaults | Minimum `45`, maximum `60`, decrement cap `15`, compression cap `5`, final floor `2` |
| Minor update | Decrement step `1`, compression step `1` each third Minor commitment, then timer redraw |
| Major update | Reset decrement and compression to `0`, then timer redraw |
| Major tuning | Per-Minor anchor `150`, source baseline active-pool ratio anchors `10` Major and `90` non-Major |
| Repeatable tuning | Recovery anchor `20`, cap reduction factor `0.5` |
| Member cadence fixture | Chaos Tier 1 source minimum `5`, maximum `8`, exclusive random ceiling set to maximum plus `1` |

These values were preserved, not tuned.
No manual normalization, timing arithmetic, or sampled surrogate was used.

## Findings and owner recommendation

1. Source-confirmed contract mismatch: optional Event033 selected after Event013 does not make the launch commitment Major.
The affected identifiers are `event_cluster_prepare_acid_rain_reservation`, `fire_event_cluster_by_temp_id`, and `on_event_cluster_global_pacing_update` in the two shared effect files.
2. Source-confirmed later reset: delayed Event033 enters the Major handler's cluster-member branch and resets Major pacing.
The affected identifiers are `on_major_event_fired` and `reset_major_event_pacing_state` in `common\scripted_effects\chaosx_logic_effects.txt`.
3. Source trace for Event033 as the trigger is consistent with a single Major launch commitment under the declared successful-dispatch assumptions.
The initial flag is consumed at launch, and the declared delayed Event013 row does not reset Major pacing.
This is not a complete engine certificate.
4. Timing drift and intermediate-weight risk: the optional33 path can first apply Minor weight recovery/gain and timer progression, then replace that pacing state when the delayed Major arrives.
Any intervening campaign events would add external state to that later reset.
Dominance, starvation, rank reversals, repetition statistics, and campaign exploit magnitude are unresolved because no probability pass completed and the full active pool is absent.

Recommended owner patch, without tuning values: derive the prepared batch's effective pacing type from its validated selected queue, commit Major pacing once on successful launch when row `5006` is selected, and persist a batch receipt that lets delayed Event033 record its fired state/history without a second Major reset.
Preserve standalone Event033's normal Major dispatcher behavior and the repeatable behavior of a queue without Event033.
Preserve reservation release and cancelled-member reporting without rewinding launch history.
Do not broaden this repair into suppressing every delayed Major from unrelated clusters without their own review.

## Reference review and remaining work

The offline wiki and installed documentation were read directly for variable checks and random bounds.
No web Paradox wiki access occurred.
No MCP reference artifact is claimed for this narrow follow-up after the live service check failed.

- `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:564-567`: random-variable bounds, `check_variable`, and set-variable state semantics.
Its SHA-256 is `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:7910-7925`: `set_variable_to_random`, supported scope, integer option, and exclusive maximum.
Its SHA-256 is `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
- Event033 spec Part 7 lines `231-246`: explicit mixed-Major launch and no-later-reset contract.
Its SHA-256 is `CCA0C267B0006FBDA23015C84F658A05AF01B98BA59DE63D4F3D2FAFFDECE587`.

`probability_evaluate`, `probability_sweep`, seeded simulation, sequence, and probability rendering were skipped after the single required inspector call timed out.
There is no retained analysis ID to render.
A complete custom sequence manifest was not invented from the incomplete global event pool.
`event_inspect` and `event_render` were not attempted after that one-time live revalidation failed, so their health and structural coverage remain unknown.
Source traces are not equivalent to those missing structural results.
No before-and-after comparison was attempted because the owner patch had not occurred.

The owner must run the restored MCP route against the preserved before source and this exact saved scenario set, then run `hoi4.probability_compare` against the patched source with the same three IDs and inputs.
Use real nonempty `before.path` and `after.path` values, not an analysis ID as a source.
Retain returned dependency revisions to detect any helper resolution that mixes preserved before source with current patched helpers.
If the route rejects fixture fields, preserve this fixture and establish a new live-validated baseline version under the same scenario IDs before comparison.
Parent review, source-specific MCP evaluation, structural inspection/rendering, matched comparison, and any meaningful timing evidence remain outstanding.

No gameplay simplification or fallback was applied.
The requested probability certification is incomplete because of the recorded service timeout.
No Git commit was created for an incomplete probability certificate while the parent owns the shared source patch.

## Authorized helper-filtered retry

After receiving the baseline handoff, the parent directed a narrower retry under load before recording the route gap.
The exposed `probability_inspect` metadata explicitly accepts `candidatePool: string[]`, while its nested `source` schema remains `unknown`.
The retry therefore used the already confirmed `source.path` form and the explicit candidate filter, without adding an unverified `source.identifier` field.

```json
{
  "source": { "path": "common/scripted_effects/chaosx_logic_effects.txt" },
  "candidatePool": ["on_event_cluster_global_pacing_update"]
}
```

The helper-filtered `hoi4.probability_inspect` request also returned `isError = true` with the exact error:

```text
tool call error: tool call failed for `hoi4_agent_tools/hoi4.probability_inspect`

Caused by:
    timed out awaiting tools/call after 600s
```

The [separate retry receipt](probability/cluster_pacing_helper_retry_2026_10_03.json) retains the exact request and full tool response.
Its SHA-256 is `72456D49A81CDB5A73EEFDC728B2F4588915B6CAC7C361946940FE3C8B76B293`, and the receipt is read-only.
The original before snapshots, original route receipt, and original fixture were not rewritten.
No candidate count or adapter report was returned, so this failure must not be classified as zero candidates or proof that the helper has no weighted consequences.
The server did not establish whether the candidate filter limited its underlying work.
There is still no numerical baseline, source revision, analysis ID, MCP scenario hash, comparison ID, or rendered evidence URI for this helper.
All three saved scenario conclusions remain `unresolved` for probability and timing.

At retry completion, both current pacing source hashes still matched their preserved before copies.
The fixture hash remained `049E1784FD43B3962B28D9196EF69861D2F74910BFF64AC325033ED02CCEADB4`.
The owner patch was therefore not yet present, and no comparison of the current source to itself was performed.
The parent accepted ownership of the categorical effective-pacing and per-batch-receipt repair, with no changed tuning numbers.
The auditor applied no timing, weight, or gameplay patch and made no balance decision.
After that owner patch, the mandatory `probability_compare` must use the unchanged saved `scenarioSet` and real preserved before source path against the patched current source.
Any failure, empty candidate result, or unresolved helper/dependency coverage from that comparison must remain explicit.

## Owner pacing patch review and mandatory comparison

Disposition: `implemented` for the owner-applied source repair under the parent's explicit instruction, with `blocked` MCP probability certification.
The earlier helper-filtered inspection retry was already finished before this pass and returned the retained 600-second timeout.
It was not left in flight or treated as a zero-candidate result.

The parent then applied the categorical effective-pacing and per-batch-receipt patch and requested this read-only comparison pass.
Current `chaosx_logic_effects.txt` and `chaosx_event_cluster_effects.txt` were reread against the immutable before copies.
The source changes are the new queue-based effective-pacing helper, launch commitment/receipt guards, the Event033-only delayed reset guard, and receipt cleanup.
The auditor did not edit these sources, choose balance targets, or run the parent's synthetic suite.

| Source | Preserved before SHA-256 | Reviewed after SHA-256 |
| --- | --- | --- |
| `common\scripted_effects\chaosx_logic_effects.txt` | `433362223952AE687FA98F87176167D7931B7EB4D930236EAB3A8A4247A4C644` | `21004680401DDCF58118D7DB87502FE4FF719266E6102052831F19A4A9EF2767` |
| `common\scripted_effects\chaosx_event_cluster_effects.txt` | `7B51BD7B123ABF479518A899E6AA33BB2582C4937BFC748E5AEA22C0094D02FC` | `D8211DA66BB429A5C00D2C51EEFDC462D36D8A210BDE1BC3DF2D66F8DC25BDC2` |

Eight reviewed after sources are preserved under `probability\owner_pacing_compare_2026_10_03\after_sources` with their own [hash manifest](probability/owner_pacing_compare_2026_10_03/after_sources/SHA256SUMS.txt).
The [source provenance](probability/owner_pacing_compare_2026_10_03/source_provenance.json) binds before and after identities to the unchanged fixture.
The four copied tuning files (`event_system_constants.txt`, `event_cluster_constants.txt`, `033_acid_rain_constants.txt`, and `settings_constants.txt`) are byte-identical to before.
The reviewed pacing diff changes no timer tuning number, candidate weight anchor, or random-roll expression.

### Owner source findings

`event_cluster_get_effective_pacing_type` at current `chaosx_event_cluster_effects.txt:2580` starts from the registered cluster type and promotes only Natural Disasters when its prepared selected event-ID array contains Event033.
It reads the prepared order without changing participation or drawing a roll.
It also retains the Event033 row index for the delayed-member receipt decision.

`on_event_cluster_global_pacing_update` at current `chaosx_logic_effects.txt:1135` calls that helper and commits Major pacing for either the initial-Major flag or the effective Major type.
After a Major launch, it stores `acid_rain_cluster_pacing_type_@var:event_cluster_pending_batch_id = constant:event_cluster_type.major` only when Event033's selected row index is greater than zero.
The variable is a country-owned categorical receipt targeted by batch ID.
The outer matching-Major-receipt guard prevents another commitment while that delayed33 batch receipt exists.

`on_major_event_fired` at current `chaosx_logic_effects.txt:1248` suppresses the delayed cluster reset only when the fired ID is Event033 and that country has the matching batch-targeted Major receipt.
The independent-Major branch still calls `on_major_event_global_pacing_update`.
Other delayed Major IDs, Event033 with no receipt, and Event033 with a nonmatching receipt retain the reset branch.
This is narrower than a blanket suppression for all delayed Majors.

The launch allocator assigns the new batch ID before the pacing call at current `chaosx_event_cluster_effects.txt:4200-4212`.
The delayed dispatcher restores the queued batch ID before dispatch at line `2836`.
Queue clearing iterates the stored batch IDs and clears their receipts before removing those arrays at lines `2642-2647`.
`event_cluster_finalize_automatic_batch` clears the current batch receipt at line `4036`.
The normal completion path calls finalization after the current member result and future-row check at line `2972`, including skipped member outcomes.

| Unchanged scenario ID | Before source trace | Reviewed after source trace | MCP probability/timing result |
| --- | --- | --- | --- |
| `natural_disasters_without_33` | Minor at launch | Minor at launch, no delayed33 receipt | Unresolved |
| `natural_disasters_optional_33_after_13` | Minor at launch, Major reset at delayed33 | Major at launch, matching delayed33 receipt suppresses later reset, receipt clears on completion/queue clearing | Unresolved |
| `natural_disasters_33_trigger` | Major at launch | Major at launch through initial/effective type, no receipt for index-zero33, delayed13 adds no Major reset | Unresolved |

The reviewed source is consistent with the requested three-case repair under valid prepared-queue, batch-ID, country-scope, and successful-dispatch assumptions.
The receipt is deliberately limited to delayed33 batches.
This does not establish generic replay idempotence for index-zero33 or unrelated clusters, nor runtime receipt persistence across reload.
No numerical timing, normalization, rank reversal, dominance, starvation, repetition rate, or engine execution was inferred from the source trace.

### Exact mandatory probability comparison attempt

The saved fixture remained byte-identical at SHA-256 `049E1784FD43B3962B28D9196EF69861D2F74910BFF64AC325033ED02CCEADB4`.
Its exact `scenarioSet` object was loaded and supplied without adding inputs or changing any of the three scenario IDs.
The [full comparison receipt](probability/owner_pacing_compare_2026_10_03/probability_compare_receipt.json) preserves that request and the full returned error.
Its SHA-256 is `590CDC800EA1A96852841793CC1CB9050F0500EABDCE7B11AB38AA11AD9C526D`.
The source-provenance SHA-256 is `1A356A956648012016D0AD8BEABE3FF593FCE73EFD5BCD331C08C7D9836C5806`.

The comparison used:

```text
before.path = docs/plans/033_acid_rain_plans/validation/probability/baseline_2026_10_03/cluster_pacing/chaosx_logic_effects.txt
after.path = common/scripted_effects/chaosx_logic_effects.txt
candidatePool = [on_event_cluster_global_pacing_update]
scenarioSet.id = event033_cluster_pacing_baseline_2026_10_03
outputs = [json, comparison, unresolved]
refresh = true
```

The before and after paths and byte hashes are distinct.
No same-file comparison, source-hash field in a source object, analysis-ID-as-source substitution, or invented custom-pool manifest was used.
No adapter was claimed because neither prior inspection returned an adapter inventory for the helper.

`hoi4.probability_compare` returned `isError = true` with this exact route error:

```text
tool call error: tool call failed for `hoi4_agent_tools/hoi4.probability_compare`

Caused by:
    timed out awaiting tools/call after 600s
```

The route returned no artifact, analysis ID, MCP scenario hash, comparison ID, source revision, dependency inventory, or rendered evidence URI.
Exact, bounded, sampled, and score-only comparison evidence are absent.
All three numerical conclusions remain `unresolved`.
The mandatory comparison was attempted but has not produced a certificate.

### Dependency and fixture limits

The comparison did not return dependency revisions, so before-helper isolation could not be checked.
The preserved before cluster helper hash is `7B51BD7B123ABF479518A899E6AA33BB2582C4937BFC748E5AEA22C0094D02FC`, while the current helper file hash is `D8211DA66BB429A5C00D2C51EEFDC462D36D8A210BDE1BC3DF2D66F8DC25BDC2`.
Passing the preserved logic path alone is not proof that any analyzer helper lookup used the preserved cluster file rather than the current indexed helper.
An actual mixed closure was not observed because no dependency inventory returned.
It remains an unresolved comparison risk rather than an asserted tool behavior.

The current settings-effects hash is also different: `2BD05E61083F9563A8881EB118387AD84B15FFDB11A2F345FFEF2A01C8B4F978` versus before `FD3EADD5526A56493CC54ED765C27EF4AA1FD9088488974B4738723E5D181E59`.
Its reviewed diff is an Event027-only prefire preparation branch.
The Event033 dispatcher/type-handler branch is source-unchanged, but this additional file revision still prevents silently claiming a fully preserved before helper closure.
Concurrent work was preserved.

The unchanged scenarioSet does not explicitly bind `event_cluster_pending_batch_id` or the targeted per-batch receipt state introduced by the owner patch.
The scheduled delayed stages are declared in the fixture's sidecar contract rather than a live-validated transition schema.
These limitations were not hidden by editing the fixture.
The complete registered seven-row catalog and selected queues remain declared, while the global active event pool and external timing factors remain incomplete.

Offline variable-targeting review used `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:551`, which explicitly covers temporary variables, integer targets, and `@var:` targeting.
Installed documentation sections read were `effects_documentation.md:2773-2781` (`clear_variable`), `4279-4294` (`for_each_loop` and its temporary current-value binding), `7888-7906` (`set_variable`), and `triggers_documentation.md:5006-5013` (`has_variable` scope existence).
The triggers-documentation SHA-256 is `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.
This source/reference review does not prove the new receipt's engine lifecycle.
The parent's synthetic suite was reported as running, and no result was supplied to this audit pass.

### Matching structural route attempt and final limits

A bounded current structural pass used `hoi4.event_inspect` with `mode = state_flow`, selector `{kind: event, eventId: chaosx.event_clusters.2}`, direction `both`, helper expansion enabled, depth `4`, node bound `40`, and edge bound `80`.
This was an ordinary domain inspection rather than the unverified helper-expansion/job routes.
The [structural request/result receipt](probability/owner_pacing_compare_2026_10_03/event_inspect_receipt.json) preserves the exact call.
Its SHA-256 is `C24DBB92446BF8CE31346095A61E50A5894D974CC69AB47075E375E5C2298663`.

The route returned `isError = true` with this exact error:

```text
tool call error: tool call failed for `hoi4_agent_tools/hoi4.event_inspect`

Caused by:
    timed out awaiting tools/call after 600s
```

No current graph, before graph, source revision, helper count, dependency inventory, or structural artifact was returned.
The matched `event_compare` and `event_render` steps were not attempted after that failed service check.
Their route health is not separately asserted, and no cached graph, before graph, render, or URI was invented.
The required before/after structural evidence therefore remains `unresolved`.

| Relevant pacing route attempt | Returned result | Artifact/revision availability |
| --- | --- | --- |
| Initial `probability_inspect`, whole logic source | `timed out awaiting tools/call after 600s` | None |
| Narrow `probability_inspect`, exact helper candidate filter | `timed out awaiting tools/call after 600s` | None, candidate count unknown |
| Mandatory `probability_compare`, immutable before logic versus patched current logic and exact saved fixture | `timed out awaiting tools/call after 600s` | None, numerical delta and dependency isolation unresolved |
| Bounded current `event_inspect` state flow for `chaosx.event_clusters.2` | `timed out awaiting tools/call after 600s` | None, matching structural comparison/render unavailable in this pass |

There is no exact, bounded, sampled, or score-only MCP certificate for these three cases.
Source-only expected behavior is recorded above, and all numerical or engine conclusions remain `unresolved`.
The owner-source repair is implemented and reviewed for the requested scope, but the MCP completion gate remains blocked.
The original three-scenario fixture and before sources remain immutable.
Any restored comparison must establish the preserved before helper closure and explicitly report the saved fixture's missing receipt/batch bindings rather than silently substituting current helpers or modifying this fixture.
No further gameplay patch, tuning decision, game launch, or duplicate synthetic suite was performed by the auditor.
Final retention checks confirmed that the submitted scenarioSet matches the immutable fixture's object and that the current logic, cluster-effects, and settings-effects files still match the reviewed after snapshots.
The [owner-comparison receipt manifest](probability/owner_pacing_compare_2026_10_03/SHA256SUMS.txt) binds all three retained receipt/provenance files.

## Caller output declarations and refreshed after comparison

The parent added caller-side declarations for the getter's two outputs and directed that any comparison use the refreshed after source rather than the previous after bytes.
The current logic SHA-256 is `C28EE6EAB4A2CEEA866C81CFFD6488E04A0B9D9ED509F650CFDDCC3F49B7548E`.
The earlier after logic hash `21004680401DDCF58118D7DB87502FE4FF719266E6102052831F19A4A9EF2767` and its retained comparison attempt are historical and do not certify this updated source.
The original before logic remains `433362223952AE687FA98F87176167D7931B7EB4D930236EAB3A8A4247A4C644`.

Current `chaosx_logic_effects.txt:1136-1138` declares `event_cluster_effective_pacing_type` with the repeatable default and `event_cluster_acid_rain_pacing_row_index` with the negative-one default before calling `event_cluster_get_effective_pacing_type`.
This matches the helper-output persistence contract described in `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:437-442`, especially line `440`: temporary variables declared before a scripted helper are inherited and can be modified within that helper.
Installed `effects_documentation.md:7820-7838` was also read for the supported `set_temp_variable` form.
The caller declarations use existing categorical constants and add no pacing tuning value.
The delayed33-only receipt guard and finalization/queue-clearing cleanup are unchanged in cluster source hash `D8211DA66BB429A5C00D2C51EEFDC462D36D8A210BDE1BC3DF2D66F8DC25BDC2`.
Actual helper execution, output persistence, and receipt lifecycle remain uncertified by MCP.

The [refreshed source bundle](probability/owner_pacing_compare_declared_outputs_2026_10_03/source_provenance.json) and [after-source manifest](probability/owner_pacing_compare_declared_outputs_2026_10_03/after_sources/SHA256SUMS.txt) preserve the currently reviewed bytes separately from every earlier after bundle.
The same original fixture remains at SHA-256 `049E1784FD43B3962B28D9196EF69861D2F74910BFF64AC325033ED02CCEADB4`.
The latest comparison again uses the immutable original `before.path`, current `after.path`, the exact helper candidate filter, and the unchanged three-scenario object.
It does not use the prior after snapshot as either comparison side.

The [latest comparison receipt](probability/owner_pacing_compare_declared_outputs_2026_10_03/probability_compare_receipt.json) records `hoi4.probability_compare` returning this exact error:

```text
tool call error: tool call failed for `hoi4_agent_tools/hoi4.probability_compare`

Caused by:
    timed out awaiting tools/call after 600s
```

No artifact, analysis ID, MCP scenario hash, comparison ID, source revision, dependency inventory, or render returned.
All three named numerical/engine conclusions remain `unresolved`, and the preserved before helper closure is still unverified.
No fresh structural certificate is claimed for this new logic hash from the earlier failed state-flow attempt.

Concurrent dependency revisions were retained rather than flattened into a claim that every source was unchanged.
The current settings-effects hash is `355FED2A358B6DA41FE534D6439B0319E8A6853A3D6C45F26B8B817D6481B5E7`.
Its diff also includes Event033 launch-origin forced/authorized flags, in addition to the Event027 preparation branch.
The current Event033 constants hash is `2AE19FA866A83B6626653B7A27C3024E6361E8B9532A901405B3D4D97D6A9425`.
Its diff adds achievement-specific severe-survival numerator and denominator fields without changing the existing pacing, AI weight, or roll entries.
The event-system, cluster, and settings tuning files remain byte-identical to the original before copies.
The auditor made no source or tuning patch and did not assess the separately owned achievement or launch-origin changes as balance conclusions.

### Separate finding: inherited event_id scratch mutation

Finding ID: `generic_major_event_id_scratch_mutation_2026_10_03`.
Disposition: separate source-corroborated side effect, unpatched, with runtime consequences `unresolved`.
The [retained finding](probability/owner_pacing_compare_declared_outputs_2026_10_03/event_id_scratch_finding.json) distinguishes the observed assignments from any downstream defect claim.

In current `chaosx_logic_effects.txt`, `count_dynamic_major_weight_pool_events` assigns the inherited `event_id` while scanning Major, fire-once, and repeatable arrays at lines `942`, `954`, and `966`.
`update_repeatable_event_weights` assigns it from the repeatable pool at line `1056`.
`reset_unfired_major_event_weights` assigns `event_id = check_event_id` at line `1309`.
Those helpers do not preserve and restore the incoming event ID at their own boundaries.
`on_major_event_global_pacing_update`, `reset_major_event_pacing_state`, and `calculate_dynamic_major_weight_gain` can therefore leave a different scratch event ID at return when the relevant loop runs.
These assignments corroborate the parent's separate observation and were not changed by the two caller-output declarations.

The current Major handler at line `1250` stores the original ID in `global.last_fired_event_id` at line `1254`, calls the pacing helpers, and later calls history recording at line `1294`.
Further tracing found a material mitigation: `record_events_log_history_entry` in `common\scripted_effects\chaosx_events_log_effects.txt:685-686` restores `event_id` from `global.last_fired_event_id` before appending the history row.
That recorder source was reviewed at SHA-256 `DEBAC43A3BB604526EE2C4BB3C8DE5806DFC8C4F40FEF97BB3948B5FF780FCC9`.
The GUI count helper uses `check_event_id`, and the later unfired-count helpers also use private check IDs.
The audit therefore does not claim proven history misattribution or a wrong final identity on the normal complete Major-handler path from these loop writes alone.
It records shared scratch mutation at the helper boundaries and the existing restoration on the history path.
Runtime interleaving, every other caller, and engine execution were not certified.

Recommended separate owner follow-up: preserve stable event identity at any caller boundary that requires it, or explicitly document `event_id` as scratch state for those helpers.
A later history call should not be assumed to restore identity for helper-only callers that never invoke it.
No identity-preservation patch was applied by the auditor, and this finding is not a balance target or a modification to the accepted delayed33 receipt repair.
The latest comparison receipt SHA-256 is `862CF1EED3CDCF7836BC3902373BEA0BDE66D13F8BCC498E994DA5D3349F8740`.
The separate scratch-mutation finding SHA-256 is `5BFF1DF54B44674E0FFE6E6757EC40F8596B5AFD043B6F5CE828601A033D0512`.
The refreshed source-provenance SHA-256 is `88F9A9257237F1F73DA5139D013C9BFDE48C386965BA19305A4EB433238030FD`.
All three files are read-only and bound by the [latest receipt manifest](probability/owner_pacing_compare_declared_outputs_2026_10_03/SHA256SUMS.txt).
Final retention checks confirmed the submitted scenarioSet is unchanged, the original before logic is still `433362223952AE687FA98F87176167D7931B7EB4D930236EAB3A8A4247A4C644`, and the current logic still matches the refreshed reviewed after hash `C28EE6EAB4A2CEEA866C81CFFD6488E04A0B9D9ED509F650CFDDCC3F49B7548E`.
