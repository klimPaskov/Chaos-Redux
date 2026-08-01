# Event 016 context and first-Prototype persistence addendum

Date: 2026-08-01

Status: bounded second improvement-loop pass for the implemented `chaosx.nr16.4`, `.5`, and `.6` tranche. This is a plan-only document and does not claim gameplay implementation.

## Process gate and prior-plan status

The original `016_brilliant_scientist_improvement_loop_addendum.md` is resolved. Its R1 through R7 recommendations received complete promoted or rejected dispositions in `016_source_of_truth_map.md`, and the promoted work has been implemented in later Event 016 tranches. This addendum addresses a distinct implementation finding created by the 2026-08-01 host-context and first-Prototype report tranche. No earlier addendum remains unresolved.

The current tranche is worth one bounded correction pass. Broad country flavour, a new route, a fifth evolution, a triggerable scenario, a focus branch, a country package, a scripted GUI, another achievement, and another super-event would add bloat rather than solve the identified gap.

## Design problem

The implemented events create useful causal choices, but their durable state is divided between country-local flags, one delayed assistant event, one country-local active report flag, and a per-family character receipt written only after the report choice resolves.

This creates four concrete discontinuities.

1. An ordinary Kruger transfer clears a pending `.5` assistant conflict and initializes the recipient without the `.4` or resolved `.5` causal flags. The choice deltas and their Evolution I or II timing meaning therefore stop following the active Directorate.
2. Kruger State formation copies the exact six causal measures but does not copy the `.4` or `.5` explanatory flags. The numbers survive while their Directorate summary and MTTH causes can disappear.
3. A Prototype report is reserved only on the current country until the player chooses. Transfer or Kruger State formation during the one-day delay can remove the active report before the character receipt exists. A second family entering Prototype while one report is active is skipped rather than queued.
4. The character receipt records that a family reported but does not record whether that family entered public custody or classified retention. The current carrier cannot reconstruct the per-family governance result after transfer.

The fixed report deltas also repeat up to fifteen times. Fifteen public choices currently represent `+150` Mandate, `-75` Dependence, `+225` Exposure, `+75` Project Capacity, `+225` Independent Capacity, and `-150` Grievance before clamping. Fifteen classified choices represent `+75`, `+150`, `-150`, `+150`, `-75`, and `+75` respectively. A consistent route should become extreme, but the current values can saturate several 0 to 100 measures after only a few reports and make later family decisions arithmetically empty.

## Preserved feature contract

- Event 16 remains one minor fire-once opening with AI acceptance unchanged.
- Doctor Warren Kruger remains one persistent identity.
- `.4` remains the single bounded host-context briefing.
- `.5` remains the single bounded assistant-conflict follow-up.
- `.6` remains an ordinary first-Prototype governance report that may occur once for each of the fifteen families.
- No `.4`, `.5`, or `.6` event becomes an evolution, Event 16 history row, news event, super-event, or spreadsheet evolution row.
- A Prototype report never grants another project-stage reward.
- Existing public and classified direction remains binding.
- Four evolutions, seventeen achievements, six mapped super-events, no cluster membership, the host focus-tree boundary, and the terminal contracts remain unchanged.

## Recommendation V2-R1: preserve one context chain across carrier changes

Recommended disposition: promote.

Treat the `.4` and `.5` results as a Directorate model that originated in one host and follows Kruger's active institution. Keep the original country flags as host history, and add character-carried outcome receipts for the effective model.

### Required durable receipts

Kruger needs exactly one mutually exclusive `.4` outcome receipt and, after resolution, exactly one mutually exclusive `.5` outcome receipt. Working labels are acceptable in implementation, but the roles must remain explicit.

| Layer | Required state | Meaning |
| --- | --- | --- |
| Character | One of public science, strategic security, industrial mobilisation, or distributed research | The Directorate model selected by `.4` |
| Character | Assistant conflict pending or resolved | Whether the career-once `.5` obligation still exists |
| Character | One of professional school, classified service, or cabinet mediation | The career-once `.5` result |
| Country | Local chosen or inherited context flag | Effective current-carrier consumer for MTTH, AI, and Directorate text |
| Country | Context causal state applied receipt | Prevents the six deltas from being applied twice to the same carrier initialization |

### Ordinary international transfer

The former host keeps its historical country flags and the institutional consequences already created there. The recipient does not replay `.4` or a resolved `.5`.

After the recipient baseline is initialized, rehydrate the carried `.4` flag and any resolved `.5` flag, then apply their existing six value-delta bundles once to the recipient. This restores the causal policy on the new carrier without stacking it on one carrier or creating another event choice.

If `.5` is pending, copy the pending obligation and its due-date receipt before clearing the former host. Schedule `.5` on the recipient for the remaining interval. If the due date has passed during the transfer transaction, schedule the follow-up for the next valid day. Do not restart the full forty-five-day clock and do not resolve the choice automatically.

The old delayed `.5` invocation may later fail its current-host trigger. That failed invocation must not clear the recipient's pending receipt or apply an outcome.

### Kruger State formation

Kruger State formation already copies the former host's exact Mandate, Dependence, Exposure, Project Capacity, Independent Capacity, and Grievance values. Copy the effective `.4` and `.5` flags and their character receipts, but do not reapply their value deltas during formation.

If `.5` remains pending during an unusually early formation, rebind it to the new Kruger State with the same due-date rule. This is an acceptance edge case, not a reason for another event.

### Causal consumers

The effective context flags continue to bias Evolution I and II timing. Their six shared values continue through Government Control, project capacity, foreign attention, confrontation, and sovereignty logic. The fix restores this existing causal chain and does not add another management mechanic.

## Recommendation V2-R2: make Prototype reports transactional and queue-safe

Recommended disposition: promote.

Separate report reservation from report resolution. A family entering Prototype must be reserved immediately, even when another report is active, and resolved only after its `.6` choice is selected.

### Per-family state model

| State | Durable owner | Meaning |
| --- | --- | --- |
| Pending | Kruger character flag per family | Prototype completion has earned a report, but the governance choice is unresolved |
| Active | Current carrier variable | This family is the `.6` report currently being presented |
| Pending queue | Current carrier array | Other earned family reports waiting behind the active family |
| Resolved public | Kruger character flag and current-carrier public-family array | The report entered public custody |
| Resolved classified | Kruger character flag and current-carrier classified-family array | The report entered classified retention |
| Reported | Existing umbrella character flag and country array | Compatibility receipt proving the family can never earn another report |

At Prototype entry, reject only families with a pending, public, or classified character receipt. Set the pending character receipt before scheduling `.6`. If another family is active, append the new family to the queue rather than dropping it.

When the player or AI resolves `.6`, clear the family's pending receipt, set exactly one public or classified receipt, update the corresponding country arrays and counts, set the umbrella reported receipt, clear the active family, and dispatch the next queued family after a short constant-defined spacing. A three-day working spacing is recommended to prevent stacked report popups while keeping the report close to the completed Prototype.

### Transfer and formation transaction

Before an ordinary transfer or Kruger State formation clears the old carrier, copy the active family and pending queue. After the new carrier exists, rebuild the pending queue from the character pending flags, preserving the copied active family first and using stable family-ID order for the rest. Rebind `.6` to the current carrier.

The former carrier must lose its active flag and pending queue only after the recipient has received the transaction. It never receives a late report after Kruger has left.

If Kruger is permanently dead, removed without a successor, or the Event 016 terminal cleanup closes the Directorate, clear unresolved pending receipts and queues without applying governance deltas. A cleanup closure is not a public or classified result and must not satisfy either result count.

### Public and classified history

Keep report-governance arrays separate from the existing `brilliant_scientist_project_published_families` project-replication ledger. Choosing public custody in `.6` records disclosure governance, but it does not silently grant the later independent-replication project reward.

The current carrier may reconstruct public count, classified count, last resolved family, and last outcome from the character receipts. The Directorate summary may display those records. Reconstruction must not create an Event 16 history row or evolution entry.

## Recommendation V2-R3: attenuate repeated report deltas without weakening the first breakthrough

Recommended disposition: promote.

Keep the current public and classified base deltas as the full strength of the first resolved Prototype report. Apply a potency factor derived from the number of previously resolved family reports.

| Previously resolved reports | Potency factor | Design role |
| ---: | ---: | --- |
| 0 | `1.00` | The first Prototype is a major national governance decision |
| 1 to 2 | `0.50` | Early portfolio choices still reshape the institution |
| 3 to 14 | `0.25` | Later reports reinforce direction without erasing the rest of the Directorate history |

At the maximum fifteen families, one consistent route therefore contributes the equivalent of five current full-strength reports instead of fifteen. Consistent disclosure or classification can still drive extreme state by the end of an unusually broad campaign, while the fourth through sixth family reports normally retain visible room to matter.

Store total resolved, public, and classified report counts, each bounded to the fifteen-family inventory. Apply the potency only when a choice resolves. Reservation, queue reconstruction, transfer, inheritance, stage replay, suspension, and resumption never apply numeric effects.

Use shared constants for the three factors, queue spacing, and AI factors. Do not add literals to the event options. Tooltips must describe the actual potency band or use broad direction if exact dynamic display would reveal misleading static values.

The `.4` and `.5` deltas remain unchanged. Their effects occur once and already feed several downstream systems.

## Recommendation V2-R4: make AI read posture, danger, and saturation

Recommended disposition: promote.

AI always accepts the opening as before. These recommendations affect only later ordinary flavour choices.

| Choice | Positive AI evidence | Caution evidence |
| --- | --- | --- |
| `.4` public science | Democratic government, public compact, peace, public institutional direction | War, secret appointment |
| `.4` strategic security | War, secret appointment, authoritarian or emergency government | Peaceful public compact |
| `.4` industrial mobilisation | Factory gate, wartime production pressure, prototype-delivery priority | Weak industrial base |
| `.4` distributed research | Public compact, computing capacity, peace, independent-replication direction | Immediate wartime emergency |
| `.5` professional school | Public or distributed context, democratic government, high Dependence or Grievance that needs relief | Extreme Exposure |
| `.5` classified service | Strategic or industrial context, war, secret appointment | Extreme Dependence or Grievance |
| `.5` cabinet mediation | Mixed posture, no strong context match, already strained Government Control | No special prohibition |
| `.6` public custody | Public or distributed context, professional school, public compact, high Dependence or Grievance | Extreme Exposure, active war, highly dangerous family |
| `.6` classified retention | Strategic context, classified service, secret appointment, active war, low Project Capacity, dangerous family | Extreme Dependence or Grievance |

Dangerous-family caution for `.6` applies to biological weapons, alien arms, temporal mechanics, high energy, and Strategic Singularity. It modifies weights and never hides or forces either governance choice.

Use the existing preferred, cautious, and base constant families or add one bounded Event 016 report-AI table. Replace the current `.6` literals. Queue processing for AI must resolve every pending family deterministically and must not discard later reports.

AI should normally reinforce its institutional posture, but current extreme values provide a counterweight. A public AI at extreme Exposure should consider classification. A secret AI at extreme Dependence or Grievance should consider publication. This prevents a fixed ideology profile from selecting an arithmetically dead option for every family.

## Recommendation V2-R5: preserve report, log, and asset boundaries

Recommended disposition: promote the boundary and queue expanded art.

### Shared history boundary

- The opening continues to create the sole Event 16 history row. A later transfer does not create a second row and does not rewrite the opening actor.
- Evolution I through IV continue to use the current carrier as their actor under the existing evolution log pipeline.
- `.4`, `.5`, and `.6` never call the opening history, evolution history, or selected Event Details history appenders.
- The Directorate overview may show current settlement and Prototype governance receipts because it is a live management surface, not the shared event log.
- No spreadsheet evolution row, cluster row, or super-event row is added for these events.

### Existing asset use

Use `GFX_report_event_016_brilliant_scientist_directorate_dossier` for `.4`, `.5`, and `.6` so the ordinary institutional reports share one visual grammar. Reserve `GFX_report_event_016_brilliant_scientist_evolution_1` for the logged Evolution I event. This requires no new asset and makes the ordinary-report boundary visible.

The already queued family-specific Prototype, accident, news, defeat, and remnant art remains separate production. It does not block this causal correction. Do not request fifteen new report images, a news event, a super-event, animation, or a 3D model for this addendum.

No Technology Tree Viewer is installed in the available HOI4 package. This pass therefore used current project source, event source, documented project mappings, offline wiki material, vanilla documentation, and a vanilla event precedent. The limitation does not block this addendum because no technology-tree route, prerequisite, or placement change is proposed.

## Recommendation V2-R6: promote the accepted contract and close this gap

Recommended disposition: promote after parent acceptance and implementation.

If V2-R1 through V2-R5 are accepted, merge their binding rules into the source specification rather than leaving a second permanent design layer.

| Recommendation | Promotion surfaces |
| --- | --- |
| V2-R1 | Spec Parts 1, 4, and 7. Event-chain and AI matrices. Acceptance criteria. Event overview. Core-runtime handoff map. |
| V2-R2 | Spec Parts 1 and 3. Project-family and event-chain matrices. Acceptance criteria. Project-system documentation. Context tranche handoff status. |
| V2-R3 | Spec Parts 1, 3, and 7. Balance and exploit review. AI matrix. Project-system documentation. |
| V2-R4 | Spec Part 7. AI matrix. Acceptance criteria. |
| V2-R5 | Spec Parts 4 and 9. Event-chain map. Asset inventory. Acceptance criteria. Event overview. |

Keep this file in `docs/plans/016_brilliant_scientist_plans/` while the recommendations are queued or being implemented. After implementation and audit, mark it promoted and resolved in `016_source_of_truth_map.md` and `016_core_runtime_handoff_map.md`. Do not delete it because it records why the transaction and attenuation rules exist.

## Acceptance scenarios

| Scenario | Required result |
| --- | --- |
| Initial appointment | `.4` fires once, stores one character context receipt, applies one delta bundle, and schedules `.5` once |
| `.4` resolved and no transfer | `.5` fires on its original due date, stores one result, and applies one result bundle |
| Transfer after `.4` but before `.5` | The recipient receives the context effect once and the remaining `.5` obligation. The former host receives no late valid `.5` |
| Transfer after `.5` | The recipient receives the carried context and assistant effects once without replaying either event |
| Kruger State formation after `.5` | Exact six values and explanatory flags survive. Context deltas are not applied twice |
| KRG formation while `.5` is pending | The pending event rebinds to KRG and resolves once |
| One native Prototype | The family is reserved, `.6` resolves once, one outcome is recorded, and no second stage reward appears |
| One mapped special-project Prototype | The same queue and resolution path is used as the native board |
| Two families enter Prototype while one report is active | Both family IDs survive. The active report resolves first and the queued report follows with the correct description |
| Transfer during the `.6` delay | The recipient receives the active report with the correct family. The former host receives no valid report and no family is lost |
| KRG formation with active and queued reports | KRG receives the active family first and reconstructs the remaining queue without duplication |
| Stage replay, inheritance, suspension, resumption, or later stage | No already pending or resolved family earns another `.6` report |
| Public then classified on one family | Impossible. Exactly one per-family outcome survives |
| Fifteen consistent public choices | Total numeric potency equals five current full reports, counts reach fifteen, and no report is discarded |
| Fifteen consistent classified choices | Total numeric potency equals five current full reports, counts reach fifteen, and no report is discarded |
| Mixed AI posture | AI follows context but can reverse when Exposure, Dependence, or Grievance reaches an extreme band |
| Event log inspection | Only the opening and four evolutions appear in their existing surfaces. `.4`, `.5`, and `.6` produce no extra rows |
| Visual inspection | All three ordinary events use the dossier sprite. Evolution I retains its distinct evolution sprite |
| Terminal cleanup | Unresolved queue state is cleared without a public or classified result and cannot fire after closure |

## Research and precedent basis

- The MIT Radiation Laboratory and the Office of Scientific Research and Development support the public, university, industrial, and military contracting tension used by `.4`.
- Manhattan Project compartmentalization supports the classified-service and strategic-ledger choices without implying that secrecy is cost-free.
- The University in Exile and wartime displaced-scholar networks support treating staff and method as partially portable across borders while leaving physical institutions with the former host.
- The Tizard Mission provides a direct period precedent for moving technical knowledge between allied states. Vanilla `britain.1` and its delayed reply events also demonstrate country-scoped breakthrough progress and cross-country report sequencing.
- The Franck Report supports the idea that scientists and assistants can contest the political custody and use of a technically successful result.

These references provide institutional direction only. Doctor Warren Kruger remains fictional, and no real scientist's biography should be mapped directly onto him.

## Implementation surfaces affected

This plan does not edit gameplay files. Parent implementation would likely touch only the existing bounded tranche and transfer helpers:

- `events/016_brilliant_scientist_context_events.txt`
- `events/016_brilliant_scientist_directorate_outcomes.txt`
- `common/scripted_effects/016_brilliant_scientist_context_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_breakthrough_effects.txt`
- `common/scripted_triggers/016_brilliant_scientist_breakthrough_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`
- `common/script_constants/016_brilliant_scientist_constants.txt`
- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
- `common/script_constants/016_brilliant_scientist_project_constants.txt`
- `common/mtth/016_brilliant_scientist_mtth.txt`
- `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt`
- Existing Event 016 Directorate outcome and GUI localisation
- The exact documentation and spec promotion surfaces in V2-R6

No new focus, decision category, mission family, scripted GUI, country tag, super-event, achievement, news event, spreadsheet row, 2D asset, animation, or 3D package is required.

## Parent disposition recommendation

| Item | Recommended disposition | Reason |
| --- | --- | --- |
| V2-R1 context persistence | Accept and promote | Restores causal meaning after transfer and formation without replaying events |
| V2-R2 transactional report queue | Accept and promote | Prevents lost, overwritten, or choice-ambiguous family reports |
| V2-R3 report attenuation | Accept and promote | Preserves the first breakthrough while keeping later family choices meaningful |
| V2-R4 AI weighting | Accept and promote | Makes AI read posture and extreme state rather than repeating a fixed choice |
| V2-R5 log and current asset boundary | Accept and promote | Keeps ordinary reports out of evolution history and requires no new art |
| Expanded country flavour and bespoke Prototype art | Keep queued | Separate production may improve variety later but does not solve this transaction gap |
| New evolution, route, GUI, focus branch, country, achievement, or super-event | Reject for this gap | Each would expand scope without repairing causal persistence or report correctness |

## Open questions

No design choice is required before implementation if the parent accepts the recommendation set. Exact identifier names may follow surrounding Event 016 conventions. The parent should confirm only whether the three-day queue spacing is retained after scenario testing or adjusted through its constant. That tuning decision does not reopen the design.

## Closure condition

This second improvement gap is process-closed when the parent records a disposition for V2-R1 through V2-R6, promotes accepted rules into the named specification surfaces, implements or explicitly queues each accepted recommendation with a reason, and reruns the focused event, transfer, AI, localisation, and completion audits. Another Event 016 improvement-loop pass should not run until this addendum is implemented, promoted, queued with a reason, or rejected with a reason.
