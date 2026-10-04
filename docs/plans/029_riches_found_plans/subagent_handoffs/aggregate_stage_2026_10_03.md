# Event 029 aggregate stage terms handoff

Disposition: implemented bounded source repair and parent source integration, with MCP and engine validation unresolved.
Acceptance basis: the parent's explicit 2026-10-03 follow-up under the user's full Event 029 specification authority requests one capped aggregate, preserved seven stage IDs/icons and numeric terms, nonterminal closed-mine crisis handling, and a separate severity priority table.
This repair does not establish full event, AI, visual, or runtime completion.

## Files and ownership

Changed gameplay files:

- New `common\scripted_effects\029_riches_found_aggregate_stage_effects.txt`.
- `common\ideas\029_riches_found_ideas.txt`, preserving seven IDs, icons, allowed predicates, category, and removal costs while removing their static modifier blocks and unused file-local numeric aliases.
- `common\dynamic_modifiers\029_riches_found_state_modifiers.txt`, changing only the controller aggregate's enable predicate and adding its stability variable.
- `common\script_constants\029_riches_found_constants.txt`, appending only the two new stage-priority and stage-term groups.

The existing core effects, triggers, event, decisions, incident effects, localisation, assets, and prior maintenance helper were not edited by this worker.
The parent's existing `discovery_receipt_days = 1` addition was preserved and is not part of this worker's change.
The constants snapshot's entire preexisting text remains a prefix of the edited constants file.
The parent owns core call sites, highest-evolution collection, modifier attachment/removal, closed-only idea retention, and final review.
No recurring scan, central MCP router, or wrapper skill was introduced.

Skills applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`, read in the preceding bounded task and reused according to their same-conversation contracts.
No skills were edited.
The shared dynamic API registry had already been reviewed and reserves event-owned orchestration for the event owner's source and documentation.
The new file header and this authorized handoff document both helpers without adding an unauthorized shared registry edit.

## Helper map and parent call contract

| Helper | Scope and inputs | Outputs | Side effects and call site |
| --- | --- | --- | --- |
| `riches_found_collect_aggregate_stage` | STATE, a registered nonterminal mine controlled by the parent's regular `riches_found_aggregate_controller` target. Parent predefines temporary `riches_found_aggregate_stage_priority = 0` and `riches_found_aggregate_controller_stage = constant:riches_found_controller_stage.windfall_receipts` before the registry loop. | Updates those two aggregate temporary values when this mine's candidate has a greater priority. Reinitializes its own candidate temporaries for every mine. | No persistent mutation, scheduling, economics, or scan. Parent calls once for every current-controller nonterminal registered mine, outside its operating-only contribution block. |
| `riches_found_apply_aggregate_stage_terms` | COUNTRY, after collection, with the selected temporary controller stage, operating count `riches_found_aggregate_mine_count`, and parent-initialized economic aggregate temporaries. Parent predefines `riches_found_aggregate_stability = 0` before the loop. | Adjusts temporary PP, efficiency, consumer-goods relief, and aggregate stability. Publishes country variable `riches_found_controller_stability`. | Applies exactly one selected stage, upper-clamps the three affected economic sums to existing caps, and overwrites stability on every rebuild. Parent calls once after the loop and before final clamps and country publication. |

No named argument expansion, meta injection, new event target, or default controller selection is used.
The collector checks registration, nonterminal status, target availability, and current control itself.
The caller must supply the aggregate target and initialize the two aggregate stage temporaries before collection.
Those temporary outputs must exist in the caller's effect chain so they carry back from the scripted effect.
The applier resets its stage quote temporaries and stability to zero before choosing terms.
It is an additive, once-per-rebuild operation and must not be called once per mine or called twice on the same accumulated economic totals.
Windfall has zero stage terms.
With no nonterminal mines, the parent initializes Windfall and all aggregate totals to zero, so application also clears the stability publication.

Parent integration outline:

```txt
save_event_target_as = riches_found_aggregate_controller
set_temp_variable = { riches_found_aggregate_stage_priority = constant:riches_found_value.zero }
set_temp_variable = { riches_found_aggregate_controller_stage = constant:riches_found_controller_stage.windfall_receipts }
set_temp_variable = { riches_found_aggregate_stability = constant:riches_found_value.zero }
# Initialize all existing economic counts/totals, then traverse the registry.
# For each current-controller registered nonterminal mine:
riches_found_collect_aggregate_stage = yes
# Leave operating-only contribution arithmetic in its existing nested block.
# Back in COUNTRY scope, after the registry loop:
riches_found_apply_aggregate_stage_terms = yes
# Retain final aggregate caps and existing country variable publication.
```

The applier already stores `riches_found_controller_stability` for the DM.
The parent may repeat that same assignment alongside its other publications for consistency, but must not apply stage economics again.
The applier's upper caps are idempotent with the parent's final upper caps.
Construction and military-factory output are untouched by stage terms and remain governed by their existing parent clamps.

## Priorities, stage IDs, and tuning table

The stage-ID group is unchanged.
The existing comment above that group calls those IDs ordered priorities, but the new independent priority group is authoritative for selection in these helpers.
No comparison of stage IDs is used to rank severity.

| Stage | Stable stage ID | New priority | CG relief when at least one mine operates | PP stage term | Efficiency stage term | Stability stage term |
| --- | --- | --- | --- | --- | --- | --- |
| Windfall Receipts | 1 | 1 | 0 | 0 | 0 | 0 |
| Managed Revenue | 2 | 2 | 0.02 | 0 | 0 | 0.02 |
| Reformed Settlement | 8 | 3 | 0 | 0.02, operating only | 0 | 0.02 |
| Resource Dependence | 4 | 4 | 0.04 | 0 | 0 | -0.02 |
| Captured Revenue State | 5 | 5 | 0.04 | -0.04 | 0 | -0.04 |
| Gold-Sick Administration | 6 | 6 | 0.04 | 0 | -0.02 | -0.04 |
| Infernal Accounts | 7 | 7 | 0.08 | -0.04 | 0 | -0.08 |

New constant groups are `riches_found_controller_stage_priority`, with seven integer priorities, and `riches_found_controller_stage_terms`, with the fifteen original nonzero fixed-point terms.
The positive consumer-goods relief is converted to the negative `consumer_goods_factor` by the existing parent publication.
Stage terms are added once to the country aggregate rather than added for each mine.
Existing diminishing returns still apply to the mine contribution components.
Existing combined caps remain PP 0.30, consumer-goods relief 0.08, and efficiency gain 0.10.
No cap, diminishing-return factor, AI weight, MTTH value, duration, stage ID, or existing constant group was changed by this worker.
No lower zero clamp is added to PP or efficiency, because that would erase the preserved crisis penalties.

## Active state and historical state

Managed classification retains the existing stabilization-fund, completed-audit, independent-authority, and paid-dividend markers.
Reformed classification retains the existing revenue-distribution, diversification-start, curse-authority, Gilded-settlement, account-resolution, and permanent-seal markers.
Those markers select this mine's Reformed candidate before checking its unresolved higher stages.

Resource Dependence uses `riches_found_resource_curse_active`, without treating `riches_found_evolution_i_recorded` alone as an active curse.
A same-mine reform marker preserves the existing resolved-policy classification and prevents the retained curse-active marker from automatically overriding that local settlement.
An unresolved curse on another mine still has a greater priority than Reformed.

Captured classification retains the illicit-capture threshold and current private-governance markers.
Gilded charter revocation, buyout, sharing, board recognition, violent nationalization, and curse independent authority prevent the old private-governance history markers from automatically classifying a settled mine as captured.
Current illicit capture at or above its existing threshold still selects Captured even when a reform marker exists.
The accepted governing-enclave choice also remains Captured.
These rules do not clear any historical flag or declare every reform free of capture.

Gold classification requires `riches_found_gold_disease_active`.
It does not use `riches_found_evolution_ii_recorded` alone.
The current Gold quarantine, closure, workforce, depth-seal, and controlled-access choices reduce pressure or change operating state but do not clear that active marker in the reviewed source.
No documented complete-containment receipt was found that could safely replace that active-state contract.
This worker therefore preserves active Gold classification through closure rather than inventing a cure from one mitigation choice.
If the parent establishes a complete Gold-containment receipt later, its active-marker lifecycle and this collector must agree.

Infernal classification retains Bottomless Account, active demons, and agreement conditions, while honoring explicit account closure, bound terms, and permanent sealing as local stage resolutions.
Account closure explicitly clears `riches_found_account_active` in the existing decision effect.
Binding terms reduces supernatural pressure and was already a Reformed stage condition in the source.
These political stage outcomes do not assert that all supernatural history has been erased.
An unrelated active Gold or capture crisis on the same mine can still outrank Reformed after the Infernal condition resolves.

The parent must collect `riches_found_aggregate_highest_evolution` from all nonterminal mine history flags independently.
Historical evolution identity and current political/economic stage are separate outputs.
The collector deliberately does not change the highest-evolution parser.

## Core integration contract

The parent reported this integration completed on 2026-10-03.
A final read-only review of `common\scripted_effects\029_riches_found_effects.txt:937-1121` confirms stage-priority and stability initialization, one collector call per controlled nonterminal registered mine, historical evolution collection outside operating-only arithmetic, and one application call before caps/publication.
The legacy stage-ID ranking blocks are absent from the reviewed aggregate body.
Idea selection and controller DM attachment/removal now use the maintenance-active flag.
The reviewed core SHA-256 is `f1db381eb8d7313dd98bb1710524af78f6b44d60feb226f6256c70b76a04ffc5`.
This is a source checkpoint of the parent's concurrent work rather than runtime or immutable final-state evidence.
The helper remains unchanged at SHA-256 `1b70dfe1adb0f3efa09132c9b0e5d2a0df1d831a1a557f71029a6cf6e3d7dee9`.

The numbered contract below is retained for future integration review.

1. Remove the old stage-ID ranking blocks from the existing core aggregate and call `riches_found_collect_aggregate_stage` for every controlled nonterminal registered mine.
   Retaining the old Reformed-ID comparison after collection would restore the masking defect.
2. Initialize stage priority and stability before the loop, and keep the regular aggregate-controller target available.
3. Call `riches_found_apply_aggregate_stage_terms` once before clamping and storing economic totals.
4. Retain exactly one stage idea while the maintenance count is positive, including closed-only controllers.
   The ideas now provide their preserved presentation identities only.
5. Attach and force-update `riches_found_controller_aggregate` while maintenance is active, then remove it only when maintenance ends.
   Its new `enable = { has_country_flag = riches_found_controller_maintenance_active }` predicate does not attach a DM that the old operating-only branch removes.
6. Use the operating mine count for consumers that require economic operation.
   At the observed parent integration checkpoint, `riches_found_controller_aggregate_active` is set with maintenance-based DM attachment, so that flag alone does not prove any mine is operating.
7. Preserve all existing zeroing, ownership transfer, terminal cleanup, and highest-evolution publication paths.

Closed-only positive economic terms are suppressed, but stability and the crisis PP/efficiency penalties remain visible through the one controller DM.
If the last mine becomes terminal or changes controller, the parent's next bounded rebuild publishes zero stability and removes the presentation and DM as appropriate.
No extra country flag, persistent target, or cleanup subsystem is introduced.

## Parent-owned follow-up

Disposition: accepted and queued within the parent's continuing late-gate work.
Acceptance basis: the parent's explicit closeout instruction says later gates will track recent reform and directs this worker not to broaden the helper.
`riches_found_curse_diversification_started` remains a Reformed candidate condition matching the inherited stage-selection choices.
It records the start of diversification and does not prove successful mission completion or a recently completed reform.
The parent retains success and recency qualification for the upcoming late-gate changes.
No helper predicate, stage term, constant, ID, or gameplay file was changed during this handoff closeout.

## Immutable baseline and current source evidence

Snapshots were copied before edits and copy/source SHA-256 equality was verified.
Paths below are under `docs\plans\029_riches_found_plans\evidence\2026_10_03_aggregate_stage_before\`.

| Snapshot | SHA-256 |
| --- | --- |
| `common__ideas__029_riches_found_ideas.txt` | `29bdb204951dc29d0f1eeb66cd2d16c6bb7b286afadee79f9a559e2c10df2928` |
| `common__dynamic_modifiers__029_riches_found_state_modifiers.txt` | `b3857b058bd0097d35dc3c57c71f18d35bed80a3bb29919e505d1be6ddcce1c9` |
| `common__script_constants__029_riches_found_constants.txt` | `3323c89eceb4d50a1c0334bbd2ee11b6cf88b6a2687dc7120734e3908de0d7b5` |

Current hashes at this worker's review checkpoint:

| File | SHA-256 |
| --- | --- |
| New stage helper file | `1b70dfe1adb0f3efa09132c9b0e5d2a0df1d831a1a557f71029a6cf6e3d7dee9` |
| Idea file | `b0400ae250ec13a910f2210d8dd444391b39cbff66368ec395c19acc0f6ab297` |
| Dynamic-modifier file | `0331857939315df313bfd18e44ce5c9fa94538a74c7fa59550ba2d5410c2aabe` |
| Constants including appended groups | `a6560d6f0640854a1db881c9cc2227f099ad7fca9cd318551d3cebb3946173f9` |

The core is being edited concurrently by the parent and no worker-owned core revision is asserted.
The prior immutable core snapshot with SHA `a991dde1db89165ced86dbf714228975113d012163d073723c898873941e987c` remains historical before evidence for the original aggregate.
It is not a snapshot of the parent's final integrated state.

## Meaningful validation and limits

A source comparison verified seven unchanged idea IDs/icons and exactly fifteen preserved nonzero terms after consumer-goods sign conversion.
The edited ideas contain no static modifiers.
All nine state DM variants were compared byte-for-byte against the immutable snapshot and are unchanged.
The existing constants prefix and stable stage-ID block are unchanged.

Eight declared priority cases compared each of Infernal, Gold, Captured, and Dependence against Reformed with both registry orders.
Every crisis wins under the new priority table.
These cases establish the intended max-priority arithmetic and do not execute game flags or prove runtime collection.
Manual branch review additionally covers historical-only evolution records, local Gilded/account settlements, still-high illicit capture after reform, other-controller records, and terminal records.

Declared source-arithmetic results:

| Scenario | PP | CG relief | Efficiency | Stability |
| --- | --- | --- | --- | --- |
| Closed-only Infernal | -0.04 | 0 | 0 | -0.08 |
| Closed-only Gold | 0 | 0 | -0.02 | -0.04 |
| Closed-only Reformed | 0 | 0 | 0 | 0.02 |
| Managed with base economic values already at caps | 0.30 | 0.08 | 0.10 | 0.02 |
| Reformed with base economic values already at caps | 0.30 | 0.08 | 0.10 | 0.02 |

These calculations check the authored term and cap contract, rather than emulate HOI4 or replace a probability scenario pass.
The first source-check command rejected nested idea IDs because its inspection regex did not allow indentation.
The inspection regex was corrected, and the complete preservation and arithmetic checks then passed without changing gameplay source.

AI auditor `01a10108-e81d-7cc2-b58a-041ccfd61783` was notified before edits of the copied baseline paths, hashes, intended priority, stage-term migration, and parent ownership.
No probability-bearing or AI-weight field is changed in this worker's patch.
The parent's integrated same-scenario auditor pass still owns AI effects and broader balance acceptance.
No engine, Career Profile, native national-spirit tooltip, GUI render, save-state, or campaign result is claimed.

## Documentation and MCP evidence

Current AGENTS.md was read before this follow-up.
The relevant specification's controller benefits, diminishing returns, caps, and operating-state requirements were read from `029_riches_found_spec_part_1_core_loop.md:343-407`.
Existing core stage selection, cap/publication blocks, active flag setters, and the Gilded/account/Gold/curse decision outcome sections were reviewed read-only.

| Local reference | Sections read | Revision or SHA-256 |
| --- | --- | --- |
| Offline `paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md` | Dynamic modifiers, lines 109-160, including variable values and enable rules | `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f` |
| Offline `paradox_wiki\Idea modding - Hearts of Iron 4 Wiki.md` | Lines 29-65, including modifier-free applicable spirits, plus modifier-rule locations | `a6405eb98a02a9de4689b7c0ef80b5a887b6c6c747d3907f68c109ed3fd099ac` |
| Installed `common\dynamic_modifiers\wuw_dynamic_modifiers.txt` | Lines 1-46, documentation header and vanilla precedent for enable, variable modifiers, and refresh | `2a03bfa939115db4c2b0720466f287927925e9e36b939c574bfb6ce3ad832db3` |
| Installed `documentation\effects_documentation.md` | `add_dynamic_modifier`, lines 1153-1177, and `force_update_dynamic_modifier`, lines 4372-4381 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\script_concept_documentation.md` | Script Constants, lines 216-247 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |

Installed paths resolve beneath `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Offline paths resolve beneath the Chaos Redux workspace.
The attempted installed `common\dynamic_modifiers\_documentation.md` and `documentation.txt` paths do not exist.
The actual installed documentation header was located in `wuw_dynamic_modifiers.txt` and read directly.
The prior task's scope, variable, scripted-effect, scripted-trigger, and global-constant references also remain applicable to these same constructs.

All live calls used explicit workspace `mod_chaos_redux_ea3b2d67c2c0`.
The idea `reference_context(limit=2)`, two-result dynamic-modifier reference search, definition-only aggregate source lookup with one definition and thirty lines, and single-node `.900` trace each returned `tool call failed`, caused by `timed out awaiting tools/call after 600s`.
The trace already used the minimum supported depth 1, one node, one edge, no helper expansion, and the exact event selector.
Depth zero is known to be rejected by the live route, so no smaller valid trace was invented and no identical retry is claimed.
Reference search was retried as a wiki-only exact-topic search with limit 1.
Source lookup was retried as a definition-only five-line read with one definition.
Both narrower retries also returned `tool call failed`, caused by `timed out awaiting tools/call after 600s`.
All requested follow-up routes therefore have final timeout results at this report checkpoint.
No returned artifact URI, source revision, scenario comparison, helper-expansion result, or complete engine inspection is invented.
Service version, service-wide health, and native task negotiation were not established, so no native job or helper-expansion route was used.
The local source and documentation checks support the repair but do not substitute for the missing MCP event/domain evidence.

## Simplifications, omissions, and blockers

No original stage term, stage identity, icon, route, cap, or diminishing-return coefficient was simplified.
The economic cap correction and severity ordering are the explicitly authorized behavior changes.
Parent call sites and maintenance-based idea/DM attachment are implemented and verified at source level as recorded above.
The running auditor's final integrated comparisons and live validation remain unresolved.
The required event-domain evidence is blocked by the exact single-node inspect timeout, and reference/source retrieval remains blocked after the narrower retries.
The parent owns final localisation/tooltip consistency review even though no IDs or visible names changed here.
The worker did not launch HOI4 or perform live QA.
No standalone worker commit was made during the concurrent integration.
The parent should review and commit the complete integrated repair after the required checks and remaining evidence limits are reconciled.
This worker's bounded implementation and handoff are complete.
Remaining work belongs to the parent's recent-reform late gates, conditional-output review, active-marker lifecycle, presentation review, integrated validation, and commit.
