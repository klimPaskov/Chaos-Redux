# Event 029 controller maintenance handoff

Disposition: implemented helper with parent integration and MCP validation unresolved.
Acceptance basis: the parent's 2026-10-03 bounded review and repair assignment explicitly requests a separate `riches_found_run_maintenance_pulse`, nonterminal mine maintenance, operating-only pulse pressure, unchanged evolution queues, and maintenance-based rescheduling.
This handoff establishes implementation facts and does not establish full Event 029 acceptance or runtime completion.

## Ownership and files

This worker creates only `common\scripted_effects\029_riches_found_maintenance_effects.txt` and this handoff.
The parent owns existing core effects, triggers, incident effects, scheduler integration, and selected-mine and foreign-offer repairs.
The decision worker owns decisions and its new affordability-trigger file.
No existing source, event, decision, trigger, constant, GUI, asset, localisation, or spreadsheet file was edited by this worker.
No central MCP router or wrapper skill was added.

Skills read and applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and `chaos-redux-mtth`.
No skills were changed.
The existing shared `chaosx_dynamic_effects.txt` and its documentation were inspected.
Their documented contract reserves event-owned orchestration for the event owner.
The helper therefore reuses the existing Event 029 lifecycle APIs and adds no generic dynamic API.
The header and this authorized handoff document the new helper, without editing the shared dynamic registry or creating an unauthorized third file.

## Helper contract

| Helper | Scope | Inputs | Outputs and side effects | Call site |
| --- | --- | --- | --- | --- |
| `riches_found_run_maintenance_pulse` | COUNTRY with ROOT equal to THIS, normally the receiver of `chaosx.nr29.900` | `global.riches_found_registered_mines`, registered state records, existing thresholds, MTTH entries, and duration constants | Clears the country delivery guard, processes this controller's nonterminal registered mines, runs existing contract, incident, mission, presentation, contribution, evolution, and achievement helpers, rebuilds this country's aggregate, requests the next pulse only when maintenance remains active | Parent-owned `riches_found_run_controller_pulse` adapter, reached from event `.900` |

There are no named parameters or input defaults that select a different controller, mine, policy, timer, or weight.
An absent registry performs no mine work and still rebuilds the current controller's aggregate.
An empty registry or terminal-only controller stops scheduling after the rebuild clears its maintenance flag.
The outer processing condition checks registry availability rather than positive economic contribution.
The state filter requires registration, current control by ROOT, and a nonterminal record.
The registry remains capped by the existing insertion contract at `constant:riches_found_event.registry_cap = 64`.
The helper does not repair or truncate a corrupted registry and does not add a recurring whole-world scan.

Usage in the parent-owned country-scope adapter:

```txt
riches_found_run_controller_pulse = {
	riches_found_run_maintenance_pulse = yes
}
```

The helper itself calls `riches_found_rebuild_controller_aggregate` after processing and before its reschedule check.
Use the adapter above without retaining the old pulse body or adding another aggregate rebuild after the helper.
Using the rebuild primitive avoids the aggregate-refresh wrapper's automatic scheduling at this explicit final reconciliation step.
Existing nested lifecycle helpers retain their own refresh and scheduling behavior, and the existing scheduled flag remains the duplicate guard.

## Preserved branches and intended behavior

| Pulse component | Preserved behavior | Intended eligibility change |
| --- | --- | --- |
| Contract lifecycle | Existing validity, renewal-date, expiry-date, dispute, and cleanup helpers | Runs for closed and recoverable collapsed nonterminal mines |
| Incident review | Existing complete incident dispatcher and all its candidate pools | Requires the existing active-mine predicate, which permits temporary closure and excludes collapse |
| Extraction and collapse pressure | Exact existing deltas, war/severe/order/integrity/chaos modifiers, warning and crisis flags | Pulse growth and its crisis marking require `riches_found_mine_is_operating` |
| Clamp and mission progress | Existing helper calls in their original order | Runs for closed and collapsed records, allowing existing repair proof processing |
| Deterministic collapse | Original risk, severe-pressure, and integrity requirements and same collapse helper | Also requires an operating mine after mission progress |
| Presentation, contribution, evolution gate refresh, achievement dates | All four existing calls in their original order | Runs for all processed nonterminal records |
| Invalid evolution pending flags | Five original gate failures clear their matching pending flags | Remains outside operating-pressure checks |
| Evolution I, II, III scheduling | Same `if` and `else_if` priority, MTTH entries, clamps, pending flags, state callbacks `.901`, `.902`, `.903`, and `trigger_for = controller` | Existing gates decide eligibility independently of operating pressure |
| Gilded Sovereignty and Bottomless Account | Same two independent pending guards, delay and clamps, callbacks `.904` and `.905` | Existing gates remain authoritative outside operating pressure |
| Final scheduling | Existing country scheduler API and duplicate guard | Uses the freshly rebuilt `riches_found_controller_maintenance_active` flag |

No old pulse branch was omitted.
Temporarily closed, quarantined, and partially sealed active mines can still receive effects from the incident dispatcher, because the assignment preserves active-mine incident behavior.
Operating-only pulse pressure does not suppress pressure changes caused by those explicit incident outcomes.
If an incident changes mine disposition during the pulse, the subsequent operating predicate is evaluated against that changed state.
Collapsed mines remain excluded by the existing evolution gates until their own recovery logic restores eligibility.
Evolution I's existing gate explicitly permits temporary closure, so its callback remains reachable without an operating contribution.

## Constants and tuning

No constants, numeric weights, duration values, MTTH definitions, or scenario fixtures were changed.
`common\script_constants\029_riches_found_constants.txt` still has SHA-256 `499394210e8818a5d1f94c6153e27dc7d8c69f378dc871891622806975a610f0`, matching the preserved snapshot.

| Existing tuning group | Existing values used | Plan |
| --- | --- | --- |
| `riches_found_event` | `registry_cap = 64` | Keep the existing insertion cap |
| `riches_found_scaling` | Pressure base 2, war 2, severe 1, collapse base 2, low order 2, low integrity 3, chaos 1 | Preserve exact formulas inside the operating guard |
| `riches_found_duration` | Controller pulse 30 days, evolution review clamp 45 to 240 days, late outcome review 120 days clamped to 60 to 240 days | Reuse existing scheduler and delay fields |
| `riches_found_mtth` and factors | Existing Evolution I, II, III interval entries | Preserve sampling and clamp call sites |

## Targets, flags, and cleanup

No new persistent event target, state variable, mission subject, or global target was introduced.
The state registry and physical mine identity remain persistent and are never cleared by maintenance.
The helper clears `riches_found_controller_pulse_scheduled` before processing.
Existing contract, mission, terminal, contribution, and achievement helpers retain ownership of their own cleanup.
The aggregate rebuild owns maintenance-active flag publication and the existing controller aggregate target.
The five original evolution and late-outcome pending flags are still cleared when their gates fail.
Pending callback cancellation remains the existing receiver-trigger behavior, without adding a fabricated event cancellation API.
Terminal mines receive their lifecycle cleanup through the existing terminal transition, and this helper skips them on later pulses.

## Parent integration and findings

1. Replace the existing `riches_found_run_controller_pulse` body with the one-line adapter above.
2. Make `riches_found_schedule_controller_pulse` use `riches_found_controller_maintenance_active`.
3. Make event `chaosx.nr29.900` use that same maintenance-active flag in its trigger alongside the delivery guard.
   The observed receiver still used `riches_found_controller_aggregate_active`, so changing only the scheduler would leave closed-only deliveries blocked.
4. Keep the parent aggregate's new nonterminal maintenance count separate from its operating-benefit count.
   The helper's final rebuild must publish that maintenance flag before rescheduling.
5. Fix the parent-owned `riches_found_begin_mission` gate with `OR = { riches_found_mine_is_active = yes AND = { check_variable = { var = riches_found_input_mission_kind value = constant:riches_found_mission_kind.restore_shaft compare = equals } riches_found_mine_can_recover = yes } }`.

The exact Restore Shaft defect is that `riches_found_mine_is_active` rejects `riches_found_mine_collapsed`, while `riches_found_mine_can_recover` explicitly admits collapsed mines.
The existing Restore Shaft starter can publish subject and progress flags after the rejected `begin_mission` call, leaving missing active-contract fields.
The maintenance extraction cannot fix mission activation on its own.
The existing repair-progress helper also rejects `riches_found_severe_collapse` and still requires repair start, route capacity, and the progress date.
Those requirements were preserved and must not be presented as automatically satisfied by the new pulse.

The narrow state-control hook is available in installed vanilla and the offline wiki.
Installed `common\on_actions\00_on_actions.txt:5074-5088` and offline `paradox_wiki\On actions - Hearts of Iron 4 Wiki.md:450-475` were read directly and document ROOT as the new controller, FROM as the old controller, and FROM.FROM as the changed state.
The existing parent evidence `evidence\2026_10_03_reference_review.md` and current `2026_10_03_resume_packet.md:174-188` retain separate successful hook reference-search/read evidence.
This supports the documented hook and scope contract, without proving a live transfer.

## Meaningful validation

The original core snapshot `evidence\2026_10_03_before\common__scripted_effects__029_riches_found_effects.txt` was hash-verified as `a991dde1db89165ced86dbf714228975113d012163d073723c898873941e987c`.
The helper initially written by this worker has SHA-256 `b7014d4408cc5bdaf9ff4bf3995953e27376064d04d9a80c3b91d1bf5b74b452`.
A bounded PowerShell extraction and manual review compared the original pulse with the new helper.
The entire pressure/crisis body is exactly equal after removing indentation.
The entire presentation-to-last-callback tail is exactly equal after removing indentation.
All five `state_event` statements are exactly equal, including IDs, delay variables, and controller receivers.
Literal effect and trigger dependencies all resolve in the current Event 029 owner files.
All referenced tuning keys resolve in the unchanged Event 029 constants file, and exactly one maintenance-helper definition exists.

Source scenarios reviewed: one operating mine, a temporarily closed-only controller, a recoverable collapsed-only controller, mixed operating and closed mines, another controller's registry entries, a terminal-only controller, and an absent registry.
These are manual scope and branch checks rather than executed campaign scenarios.
Closed and collapsed maintenance reaches contract, mission-progress, and achievement helpers.
Unregistered, terminal, and other-controller records are filtered.
The existing operating predicate excludes closure, quarantine, and partial sealing from pulse pressure.

The probability auditor `01a10108-e81d-7cc2-b58a-041ccfd61783` was informed of the exact helper, baseline SHA, intended eligibility changes, five callback preservation, and timing limitations.
The parent retains its baseline and same-scenario comparison pass.
There is no invented numeric probability delta or self-comparison.

The 30-day pulse samples expiry and mission progress, so an eligible stored date can be processed on a later pulse rather than on that exact day.
Preserving MTTH entry and clamp text establishes unchanged computation at the call site.
It does not establish cumulative engine timing, continuous gate history, native mission timer synchronization, or callback delivery after controller transfer.
The intentional maintenance eligibility change can permit a closed-only controller to queue Evolution I where the old economic scheduler stopped.

## Reference citations and MCP evidence

Connected metadata exposed `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, event inspect/render/compare, and probability inspect/compare.
No HOI4 service-health, version, or script-validation route was exposed in this worker's inventory.
Service-wide health and client task negotiation were not established.
No native jobs, job polling, or helper-expansion mode were used.

The first request batch used explicit workspace `mod_chaos_redux_ea3b2d67c2c0` for probability inspect of core effects, event `.900` trace, reference context with limit 2, `for_each_scope_loop` search with limit 2, and a definition-only source lookup with one definition and 20 lines.
The event selector in that first batch omitted `kind`.
After reading the current resume packet's live-selector evidence, the event inspect retry used `selector = { kind: event, eventId: chaosx.nr29.900 }`, depth 1, six nodes, six edges, and no helper expansion.
The matching event render uses a neighborhood view, depth 1, six nodes, no helper expansion, and no HTML.
A targeted `state_event` reference search requests only installed documentation and wiki with limit 2.
The six-node corrected event inspection and matching render each returned `tool call failed`, caused by `timed out awaiting tools/call after 600s`.
Each was retried with one node and explicit workspace ID.
An attempted depth of zero was rejected immediately with `MCP error -32602: Too small: expected number to be >=1 at maxDepth`.
The corrected one-node retries retain depth 1, with one edge for inspection.
The targeted `state_event` reference search returned `OK` for the explicit workspace.
It found installed `documentation\effects_documentation.md:8096-8128`, section ID `57f9648040c6d6f354eadf4fe1dc23b14ee0bba62844d4e31ca1104def93a0ff`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The two retained search results were both installed-documentation sections, so wiki coverage was not inferred from the result limit.
A revision-bound 33-line read of that section and a wiki-only `for_each_scope_loop` search with limit 1 were then requested.
The initial five-route batch, corrected one-node event retries, revision-bound state-event read, and wiki-only search remain pending at this report checkpoint.
No successful artifact URI, source revision, graph result, or comparison result was returned by those pending requests.
Pending calls and focused event projections cannot establish scripted-helper lifecycle coverage.
The local reference reads below support syntax and design only and do not substitute for missing MCP domain or engine evidence.

| Local source read | Lines | SHA-256 |
| --- | --- | --- |
| Installed `documentation\effects_documentation.md`, `for_each_scope_loop`, `state_event`, `set_temp_variable`, `clr_country_flag` | 4296-4325, 8096-8125, 7820-7841, 2792-2803 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\triggers_documentation.md`, `check_variable`, `is_controlled_by` | 2110-2137, 5381-5394 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation\script_concept_documentation.md`, Script Constants | 216-248 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md` | Full 84-line schema and examples | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, variable scope and array loops | 431-454, 1208-1258, 264-297 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md`, ROOT, PREV, CONTROLLER | 254-269 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Offline `paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md`, delayed effects and state receiver | 207-226 | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md`, scripted effects | 4683-4706 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md`, scripted triggers | 2359-2392 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Vanilla `common\scripted_effects\COG_scripted_effects.txt`, scoped-array precedent | 196-250 | `77fd69835f9a7115fc60d85de61c5c31e4c7880e30fb6d6e8ae494f318b02710` |

Installed game paths in the table resolve beneath `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Offline paths resolve beneath `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
The offline Localisation page's scripted-localisation section at lines 658-684 was read as context for the existing presentation call.
There are no new player-facing names, icons, or localisation keys.
GUI references and visual inspection are outside this helper's scope because Event 029 uses an ordinary category and this assignment changes no GUI.

## Simplifications, omissions, and blockers

No gameplay route or numeric tuning was simplified.
All original pulse branches are retained with the explicitly requested maintenance and operating guards.
Parent adapter, receiver trigger, mission gate, aggregate publication review, and final integration remain outside this worker's write scope.
Required event inspect/render/compare and probability comparison acceptance remain unresolved until their actual final results and auditor evidence are reviewed.
No `hoi4.script_validate` pass could be run because that route was not exposed.
No HOI4 launch, live campaign validation, native mission-timer experiment, or controller-transfer runtime experiment was performed.
The orchestrator owns live QA coordination.
The parent should commit the integrated change after reviewing all worker-owned files and final validation rather than committing a disconnected helper as a complete repair.
Future work is limited to those integration and validation obligations, without proposing an additional mechanic or changing mission durations.
