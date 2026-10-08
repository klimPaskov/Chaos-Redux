# Event 32 native evolution timing baseline

Resumed and recorded on 2026-10-08 under the requested 2026-10-07 handoff path.
Disposition: baseline bytes and fixtures preserved, numeric timing unresolved.
The parent stated that no owner timing edit had occurred, and all five current files still matched the preserved hashes at final verification.

[Snapshot manifest](../evidence/evolution_timing_20261007/before/snapshot_manifest.json), SHA-256 `f67bff4f0ea942867a7c9f78fc8c909e6cfd9f7d1eab1027c17a4bc362e3b133`, binds the five immutable byte copies.
The snapshots retain their original repository-relative paths inside `before/`, have the read-only attribute, and are covered by exact-path `-text -filter` rules in `before/.gitattributes`.
The requested `before/local.gitattributes` is also preserved.
No existing snapshot or earlier report was overwritten.
No Git operation or committed-blob verification was performed.

[Exact scenarioSet](../evidence/evolution_timing_20261007/scenarioSet.json), SHA-256 `2f5136de919f4e1b1a3b9459e061a9ce3d80c69e16e6aff401eb6cc49ac89608`, is 87,564 bytes and contains `EVO-01` through `EVO-12` plus `EVO-PACE`.
It was saved before any evaluation, and this pass performed no evaluation.
The installed `hoi4-agent-tools` 3.10.0 `probabilityScenarioSetSchema` accepted the object with no schema issues.
This is a local fixture SHA and syntax/schema check, not an MCP scenario hash or engine result.
[Scenario contract](../evidence/evolution_timing_20261007/scenario_contract.json) records completeness and binding limits, and the [plain intent matrix](../evidence/evolution_timing_20261007/scenario_intents.md) preserves the named requirements for the future native events.

The accepted basis is the parent instruction naming `docs/specs/032_missiles_specs/032_missiles_spec_part_4_evolutions.md:29-62`, `032_missiles_spec_part_6_ai_and_probability.md:527-586`, and `032_missiles_probability_scenario_matrix.md:117-130`.
Part 4 eligibility takes precedence over matrix shorthand.
The parent owns the timing model and balance targets.

| Audited source | Relevant identifiers and lines |
| --- | --- |
| `events/032_missile_crisis.txt` | Triggered-only jobs `chaosx.nr32.190` at 62-67 and `.191` at 72-76 |
| `common/scripted_effects/032_missiles_operations_effects.txt` | Unlock recorder 412-479, pressure measurement 543-594, arming 655-712, host selection 744-764, job enqueue/recovery 767-813, evaluation 816-978, recurring watch 983-1015, due job 1020-1123 |
| `common/scripted_effects/032_missiles_effects.txt` | `missiles_global_firing_transaction`, initialized flag and evolution evaluation at 265-274 |
| `common/scripted_triggers/032_missiles_operations_triggers.txt` | Program predicates 992-1041, eligibility/high-pressure predicates 1045-1093, enabled locked-track gate 1097 onward |
| `common/script_constants/032_missiles_constants.txt` | `missiles_evolution_timing` 414-435, `missiles_evolution_pressure` 786-808, `missiles_evolution_pacing` 812-837 |

Additional narrow source references were `common/scripted_triggers/032_missiles_triggers.txt:96-113,193-219,373-397` for program/site/payload predicates and `common/scripted_effects/chaosx_dynamic_effects.txt:821-844` for legacy date-unit conversion.
These dependency files were read but are outside the five-file snapshot set.
A later frozen-source comparison will still resolve unfrozen dependencies from the then-current workspace, so it is not a complete historical workspace replay.

| Track | Base source value | Source eligibility | Source high-pressure modifier |
| --- | --- | --- | --- |
| Rogue Launch Commands | 120 days | Chaos at least 200 and at least one vulnerable program | Vulnerable programs at least two applies factor 0.50 |
| Unreliable Guidance | 105 days | Chaos at least 400, an operational program, and qualifying readiness/overstock/launch/maintenance strain | Programs at war at least two applies factor 0.50 |
| Saturation Arsenals | 90 days | Chaos at least 600, operational count at least two, operational share at least 0.40, programs at war at least two | Programs at war at least four applies factor 0.50 |
| Special Warheads | 120 days | Chaos at least 800 and at least one qualifying payload owner | Payload owners at least two applies factor 0.50 |
| Automatic Retaliation | 150 days | Chaos at least 900, no world end, at least two operational programs, at least one responding hostile endpoint | Responding hostile endpoints at least two applies factor 0.50 |

These are exact source values and predicates, not evaluated MTTH results.
The ordinary helper additionally applies factor 1.50 when the managed-program count is below two, draws one `set_temp_variable_to_random` value, applies spread minimum 0.75 and width 0.50, then rounds and clamps the delay.
On a first pulse it replaces that delay with `21 + 14 * missiles_evolution_armed`.
The source order is Rogue, Guidance, Saturation, Special Warheads, then Automatic Retaliation.
No timing distribution or cumulative probability was derived by hand.

The source has one living registry host through `global.missiles_evolution_host`, but each arm can enqueue `.190`.
The `.191` watch repeats a registry recount every 30 days while an enabled track remains locked.
This is a recurring global program-registry scan and conflicts with the parent's finite-boundary replacement requirement.
A due job commits at most one track in one invocation and queues a seven-day retry for another due track.
Separate same-day `.190` deliveries can affect that cadence, and native delivery ordering remains unresolved.
The pressure helper creates its output temporaries internally while the shown callers do not preinitialize those outputs.
The fixture stipulates their values after measurement and therefore does not prove helper output lifetime.

[Retained MCP evidence](../evidence/evolution_timing_20261007/mcp_evidence.json) contains the exact requests, structured responses, source revisions, complete artifact URIs, and cited documentation records.
The workspace was `mod_chaos_redux_ea3b2d67c2c0`.

The first probability request used `direct_random` with logical source `common/scripted_effects/032_missiles_operations_effects.txt`, identifier `missiles_arm_evolution_track`, its physical `snapshotPath`, and the copied-byte `expectedSourceHash`.
It returned `PROBABILITY_SOURCE_DISCOVERED`, status `ok`, but `candidates = 0` and `discoveryReason = identifier_not_found`.
The one narrow retry changed only the adapter to `event_mean_time_to_happen` and returned the same empty-helper result.
Both exposed only 19 unrelated random-list candidates.
This differs from the older report's `requested_adapter_empty` wording, and neither response proves a supported timing model.
Exploration stopped after that retry.

Both requests reported analyzer source hash `2878d237a850d641779c646fee12fe55cd1b71e6f35fa3900aad5128e5d78a16` and revision `bafce53df7624a83781becc33cb9a401dfdfb865b27dbab1779597bf2e92ca83`.
That analyzer hash is distinct from the physical snapshot SHA-256 `5f803dd63867d0303d19e7e7e388f00ba6440130b53237ffbe961b715d0ae67b`.
The inspection artifacts are `probability-inspect-2878d237a850.json` with artifact hashes `8b9863c8e172e5a2ecde207ba535ec10bb8cbb6ea485cd38eb4374f3b5ceafaf` and `a4487592369ca3f968b7c9f06d085873c862b1696ac5112b5edbe47901f45dd9`, respectively.
Source lookup independently located the helper at 655-712 with revision `4d5f925f21ecf0dbd5b3b5c3cdf3a9563a9ac9cbee1a216e7625696e649eaf5f`.
Its inline source excerpt was clipped, so the complete body was read from the snapshot.

The structural requests used the exact event selector `chaosx.nr32.190`, depth one, twelve nodes, and no helper expansion.
Inspection returned `EVENT_INSPECTED_PARTIAL`, render returned `EVENT_RENDERED_PARTIAL`, and the timing render reported zero selected nodes and zero branch renders.
Revision was `db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5`, graph hash `9e9514043fbfa24c56369a1bfb30448f66a8897acd7b42d73673e45bf67b8f11`.
The render manifest artifact hash is `0508ce8902fcb99d97b1ac691008bf6ea6749e1f0eee38a8334f2bdc6d779d25`.
The linked timing PNG hash is `9deccb57d27974940b400ffcfbe08c03dce74c1819da250a1e1c9223ce373f55`.
Their exact URIs are retained in the evidence JSON.
No large trace or graph resource was fetched, and these partial artifacts do not prove event lifecycle or visible timing.

All thirteen timing conclusions are classified `unresolved`.
No exact, bounded, sampled, or score-only numeric timing result was produced.
A normalized candidate pool is not applicable to these independent clocks.
The finite registry membership is explicitly listed per synthetic scenario, but the full external model remains incomplete for every case because country/site derivation, scope control maps, helper lifetime, and engine numeric `global.date` are unresolved.
The one-host bindings, initialization, launches, chaos, all five disabled/unlocked/pending flags, and first-pulse/watch state are explicit.
There are no scheduled external changes or simulation seeds.
The contract declares the finite terminal states and 365-day review horizon.

The fixture corrections are explicit: EVO-02 is ineligible in its secure world, EVO-04 has one overstocked program with reserve 12 and capacity 8, EVO-05 fixes the war-program count at two, EVO-11 disables all five tracks, and EVO-12 marks all five unlocked with their legacy feature flags.
EVO-PACE retains the first-pulse context without prescribing a native implementation.
These inputs operationalize the named scenarios and do not set new balance targets.

AI score races, probability-proportional dominance, and score normalization are not this surface.
No weighted target selection was audited.
Starvation, timing rank reversals, realized repetition, and exploit frequency remain unresolved.
Source concerns for owner review are the recurring watch, separate pending job deliveries, and unverified pressure-output lifetime.
The finite five-track recorder guards support a source-level one-unlock intent, but they are not proof of engine execution or log correctness.

Owner follow-up is confined to the already authorized timing replacement in the five snapshotted files.
Implement the reviewed single-host native event model and finite evaluation boundaries, preserving existing track identities and disabling/recording gates.
Then inspect the actual native events, bind any new source inputs explicitly, evaluate the saved fixture, and perform mandatory `hoi4.probability_compare` with the identical saved object and real before/after sources.
Preserve this original fixture if an additional binding version is necessary, and report that version change.
The old side contains no recognized native MTTH timing block, so a comparison may still have an unresolved numeric delta.
Do not substitute a custom pool, synthetic native baseline, analysis URI, or current-to-current comparison.

Evaluation and sensitivity sweeps were deliberately skipped after the bounded empty-helper retry.
Simulation and sequence were skipped because no supported stochastic model or complete custom pool was declared.
Probability rendering was unavailable because no analysis ID exists.
Comparison was deferred because no owner timing patch or after-source exists.
MCP scenario hash, analysis ID, and comparison ID are all absent.

Reference tools `reference_context`, `reference_search`, and `reference_read` were used.
Detailed reads covered installed `documentation/effects_documentation.md:7842-7858`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:117-150`, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
The installed documentation defines the default random interval as [0,1), while the offline triggering section distinguishes native MTTH from triggered-only scheduling.
Vanilla precedent `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\events\PoliticalEvents.txt`, `political.1`, has `fire_only_once = yes` and a native MTTH block at 106-110, file SHA-256 `9f1a7ded3255cb8c39b337b05cda48d8bd1256c8f246aafb4f03f1423da85746`.
The context bundle omitted other general topics, so no full reference-bundle coverage is claimed.

Current AGENTS SHA-256 was `e6375b0aa386e510abd4a35677dccf2871e47f75c9f169e593d52f8c77feff28`.
The configured tool command was `npx.cmd --yes --prefer-online hoi4-agent-tools@latest`, using `C:\Users\klimp\AppData\Roaming\hoi4-agent-tools\config.json`.
Observed stdio process paths pointed to the installed 3.10.0 package used for the schema check, but no independent connection handshake identified the exact serving process/version.
No native task or helper-expansion route was used.

Only the requested documentation/evidence files were written.
Gameplay, AI, events, triggers, constants, runtime files, game state, logs, and Git state were not written.
No gameplay simplification or tuning patch was applied.
The omissions and uncertainties above remain open.
Skills used: chaos-redux-subagents, chaos-redux-events, chaos-redux-mtth, and the scenario discipline in chaos-redux-event-planning.
No skill was changed.
