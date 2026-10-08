# Mengele Cloning Deployment facility throughput

Disposition: implemented and accepted by the parent at source level on 2026-10-08, with the validation limits below retained.
Acceptance basis: the final completion contract requires a distinct private Cloning Deployment physical-site and production payoff, and the user directs the parent to take recommended options without waiting for further input.
The parent accepts the existing-consumer recommendation in `subagent_handoffs/016_private_clone_existing_production_review_2026-09-08.md`, adapted to the subsequently implemented exact native and no-DLC receipt paths.
The throughput value below is a parent balance choice, not a number directly specified by the user.

## Physical site and output contract

Existing biological warfare facilities are the physical sites.
Each controlled facility-bearing state retains the existing baseline of one Clone Equipment per producer invocation.
Paid private Cloning Deployment adds four Clone Equipment per owned and controlled facility-bearing state on the existing weekly invocation only.
A qualifying owned facility therefore yields five equipment per regular week in total.
Captured controlled facilities retain baseline output, and uncontrolled facilities contribute nothing.
States are counted once regardless of building level.

The enhancement requires the existing cloning-production completion latch, strict private provider validity, private Cloning Prototype and Deployment receipts, and the neutral clone operational technology.
It uses no country-only site counter as persistent authority.
Ownership, control and the building are read again for each weekly calculation.
Loss of the private programme or relevant physical control removes the enhancement while preserving learned technology, stored equipment and authentic completion history.
The legacy baseline's existing lifecycle remains unchanged.

The accepted exact Event016 native project remains `sp_brilliant_scientist_cloning`.
Its current literal receipt/grant path and the current no-DLC paid Prototype callback already settle the existing producer's completion latch causally.
The earlier recommendation to accept `sp_mengele_cloning` as an alternative private Prototype source is superseded by the accepted native ownership amendment and is not implemented here.
The separate KRG paid maturation transaction remains unchanged.
The earlier additional private-site/paid-cycle proposal remains unimplemented and is replaced for this payoff by the existing physical-facility consumer.

## Invocation and state contract

The existing `germany_mengele_produce_clone_equipment` remains the baseline-only public boundary used by native completion, construction and inheritance callers.
It selects baseline mode explicitly, so stale weekly input cannot increase a later direct callback.
The existing authorized weekly hook calls a distinct literal weekly wrapper under its unchanged completion-latch filter.
No additional world iteration, scheduler, periodic CXT grant or replacement timer is introduced.

The calculation helper is read-only apart from temporary outputs.
It owns the facility-count storage consumed after the existing count helper returns and consumes its operation-mode input on every exit.
The production kernel owns all calculated outputs it reads after return, adds one combined `clone_equipment_1` amount and refreshes the reserve consumer once per eligible invocation.
Zero-facility calls retain the existing refresh behavior.
Equipment producer identity is the invoking country, using the verified vanilla `producer = THIS` form.
The shared facility counter and its other consumers are not changed by this tranche.

The three operation-mode metadata values are none, baseline and weekly.
The baseline constant remains one, and the additional weekly constant is four.
These values are centralized in the existing Germany/Mengele constants file.
No new persistent flag, native project, technology, equipment type, unit or model is introduced.

The existing CXT ownership probe may call the calculator in weekly mode and copy its base, enhancement and total into debug observations.
It cannot grant equipment, refresh manpower, initialize a programme or change provider receipts.

## Balance and required checks

For N owned-and-controlled facilities and M captured controlled facilities, regular eligible output is 5N + M equipment.
Direct callbacks remain N + M equipment.
For one continuously qualifying owned facility, the enhancement adds 208 equipment across 52 weekly invocations, equivalent to 2,496 nominal equipment IC at the existing build cost of twelve.
If retained in stockpile, that extra equipment contributes 2,080 weekly reserve manpower at the existing rate of ten per item by the end of that period.
These are arithmetic bounds, not an instantaneous manpower award or observed campaign output.
Training consumes the physical equipment and removes its reserve contribution through the existing shared consumer.

Required source scenarios cover legacy-only and private receipt states, missing prerequisites, closed provider, zero/multiple facility states, captured and lost-control sites, multiple levels, direct calls after weekly calls, stale mode input, foreign outer ROOT, one stockpile write and refresh, and read-only CXT observations.
Source tests must preserve the original non-production portions of the large Germany effects file and all unchanged periodic hooks.
The regular weekly cadence, actual stockpile/manpower refresh and engine building availability remain separate live acceptance evidence.

## Presentation and limits

The existing Cloning Deployment action and icon remain the entry point.
Its effect description must show the dynamic additional weekly equipment and the owned-and-controlled facility condition.
No new visual asset or gameplay window is required.
No AI weight is changed, and no new production decision is added.
No gameplay simplification is authorized by this choice.
The full Event016 goal remains incomplete while the broader accepted requirements and their evidence remain open.

## Implementation and parent acceptance, 2026-10-08

The parent accepts the bounded implementation after reviewing the [core handoff](subagent_handoffs/016_mengele_clone_production_core_2026-10-07.md), independently executing its retained driver, and reviewing the [independent integration audit](subagent_handoffs/016_mengele_clone_production_integration_2026-10-07.md).
No blocking source defect or gameplay simplification remains in this accepted throughput tranche.
This source disposition does not establish full Event016 completion or observed engine behavior.

| Delivered surface | Implementation and evidence |
| --- | --- |
| Facility output and guards | `common/scripted_effects/016_mengele_clone_production_effects.txt` and `common/scripted_triggers/016_mengele_clone_production_triggers.txt` implement the literal baseline/weekly entries, shared calculation, five enhancement gates, exact-mode guards and one combined output. |
| Existing integration | `common/scripted_effects/germany_mengele_effects.txt` routes the original producer to baseline only; `common/on_actions/germany_mengele_clone_on_actions.txt` changes only its existing call to the weekly entry; `common/script_constants/germany_mengele_constants.txt` owns the tuning and invocation mode. |
| Read-only debug projection | `common/scripted_effects/016_mengele_native_ownership_cxt_effects.txt` calculates and copies the three weekly amounts through the existing player-triggered probe without producing equipment. |
| Player presentation | `common/scripted_localisation/016_mengele_stage_value_localisation.txt` and `localisation/english/016_mengele_cloning_stage_l_english.yml` bind the additional output to the same tuning constant and describe the physical ownership/control condition. |
| Documentation | The final completion contract, `mengele_cloning_stages.md`, `mengele_cloning_native_completion.md`, helper API documentation and CXT guide match the implementation; the two historical payoff proposals carry explicit Cloning dispositions. |

The retained driver passes twelve declared gameplay states, 39 wrapper/producer invocations, sixteen direct mode cases, sixteen wrapper override cases, twelve executions of the real weekly hook, twelve CXT observation tails and three calls to the guarded completion callback.
Four additional executions distinguish the corrected count lifetime and invoking-country provenance from the intended baseline rate.
The current maintained provider-adapter audit also passes its 5,487 assertions with its declared external stubs.
Exact outputs, source hashes and immutable Git baseline objects are retained in `docs/testing/event016_clone_throughput_20261008/source_test_result.json` and the [parent evidence](subagent_handoffs/016_mengele_clone_production_parent_evidence_2026-10-07.json).
The old cold-count counterexample explicitly treats an absent numeric count as zero and remains a source-model assumption, not an observed game failure.

The independent audit preserves the complete bodies of the legacy counter, shared coup-pressure consumer, laboratory-unit consumer, completion callback, two construction callbacks and inheritance callback against the supplied baseline.
The unrelated `acid_rain_interrupt_for_world_end` working-tree hunk remains outside this tranche and its commit.
The separate CXT provider fixture is player-triggered and does not create private stage/native receipts; this observation extension adds no automatic Deployment grant.

MCP inspect/render evidence for the exact weekly entry is retained under `docs/testing/event016_clone_throughput_20261008/`.
The parent inspected the returned graph and its PNG: it selects `on_weekly` and the weekly producer reference, with helper expansion explicitly deferred.
An earlier unprefixed source selector selected unrelated vanilla entries and is excluded from coverage.
Script validation is partial and leaves native parameter/helper interpretation unresolved; the scripted-localisation route performs zero checks for that unsupported file family.
The exact comparison outcome is recorded in the evidence directory and does not convert these bounded results into full helper/lifecycle or engine validation.
Both the two-node proposed-source comparison and its narrower one-node retry timed out after 600 seconds, returning no comparison artifact.
Earlier trace-artifact and focused-revision inputs were rejected by the comparison route; all four requests and outcomes are retained in `docs/testing/event016_clone_throughput_20261008/comparison_evidence.json`.

The twelve-state model stubs strict provider validity, refinement grants and the reserve consumer; constructor/inheritance bodies are compared rather than executed, and only the new CXT observation tail is executed.
Native weekly cadence, actual equipment attribution, stockpile reserve recomputation, building availability, native/paid lifecycle and tooltip rendering remain live acceptance evidence outside this source tranche.
No new visual asset is required: the existing Cloning stage icons remain registered by `interface/016_brilliant_scientist_project_icons.gfx` under `gfx/interface/decisions/016_brilliant_scientist/projects/`.
No model or unit-asset package was touched.

Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`; the independent auditor additionally applied the event-planning and improvement-loop guidance within its bounded review.
No skill change is required by this tranche; the existing caller-owned temporary and shared-index rules already cover the fixes.
