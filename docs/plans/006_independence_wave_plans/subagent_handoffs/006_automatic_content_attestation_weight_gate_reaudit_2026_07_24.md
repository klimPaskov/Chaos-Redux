# Event 006 automatic content-attestation weight-gate re-audit

Date: 2026-07-24

Audit mode: Independent read-only post-fix audit.

## Verdict

Runtime content-attestation repair: **PASS**.

Documentation reconciliation: **FAIL**.

The centralized candidate-weight calculation now prevents every unadmitted package from receiving positive automatic weight.

The anchor phase independently checks the same attestation before attempt counting or any host, country, or anchor-state reservation.

All fourteen regional random lists route through the centralized calculator, and every reservation publisher routes through the centralized anchor gate.

The current three-, four-, and five-country bands are conditionally plannable from the exact six admitted packages.

The seven- and ten-country bands still fail closed because six admitted packages cannot satisfy those exact counts.

This audit does not claim Event 006 completion, package completion, in-engine execution, balance completion, or full documentation reconciliation.

## Changed files in the audited tranche

The narrow shared-worktree change set inspected by this audit consists of:

- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_automatic_content_attestation_weight_gate_2026_07_24.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

This re-audit wrote only:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_automatic_content_attestation_weight_gate_reaudit_2026_07_24.md`

No gameplay file was edited by this audit.

Nothing was staged or committed by this audit.

## Central weight gate

Status: **PASS**.

`independence_wave_calculate_candidate_allocation_weight` initializes `independence_wave_candidate_weight` to the centralized zero constant at `common/scripted_effects/006_independence_wave_package_planner_effects.txt:482`.

It copies the loaded package ID into `independence_wave_execution_package_id` at line 486.

The canonical `has_independence_wave_runtime_package_content_attestation_for_execution_id` trigger is required at line 519 before the base weight is assigned at line 526.

Every positive bonus, penalty correction, world-collapse multiplier, and minimum clamp remains nested inside that attested branch through line 671.

An unadmitted candidate therefore exits with the original zero weight.

The temporary execution-package bridge is cleared at line 673.

The canonical trigger still contains exactly IW-001, IW-004, IW-007, IW-008, IW-017, and IW-019 in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:45-53`.

No second admitted-ID list was introduced in the calculator.

## Anchor-phase reservation gate

Status: **PASS**.

`independence_wave_begin_package_reservation` copies the candidate package ID into `independence_wave_execution_package_id` at `common/scripted_effects/006_independence_wave_package_planner_effects.txt:100`.

The anchor phase requires the canonical content attestation at line 106.

The gate precedes the attempt-counter increment at line 108, host reservation at line 128, and country reservation at line 136.

An unadmitted anchor-phase dispatch receives `package_unready` at lines 143-149.

`independence_wave_reserve_candidate_anchor` also requires the candidate-country reservation flag and a zero rejection reason at lines 293-301 before its first anchor-state reservation at line 307.

An unadmitted direct or stale anchor-phase dispatch therefore cannot reserve a host, country, or anchor state.

The temporary execution-package bridge is cleared at line 264.

Optional-territory publication does not repeat the attestation because it operates on the already frozen and aligned package row.

The final execution preflight repeats the attestation before release.

## Fourteen regional random lists

Status: **PASS**.

The fourteen region effect files contain 144 preparation helpers, 144 calls to `independence_wave_calculate_candidate_allocation_weight`, fourteen regional `random_list` surfaces, and 126 unique random-list package IDs.

Every random-list package ID has a preparation helper.

Every preparation helper initializes its package weight to zero, calls the centralized calculator when its package-local planning checks pass, and copies only the centralized candidate weight into the random-list weight variable.

No regional file assigns a positive package weight directly.

All 149 direct calls to `independence_wave_begin_package_reservation` are in the same fourteen region effect files.

| Region | Preparation helpers | Central calculator calls | Random-list package IDs | Result |
|---|---:|---:|---:|---|
| 01 | 10 | 10 | 9 | PASS |
| 02 | 10 | 10 | 9 | PASS |
| 03 | 9 | 9 | 8 | PASS |
| 04 | 10 | 10 | 8 | PASS |
| 05 | 12 | 12 | 12 | PASS |
| 06 | 13 | 13 | 12 | PASS |
| 07 | 6 | 6 | 5 | PASS |
| 08 | 4 | 4 | 3 | PASS |
| 09 | 9 | 9 | 7 | PASS |
| 10 | 7 | 7 | 7 | PASS |
| 11 | 5 | 5 | 5 | PASS |
| 12 | 16 | 16 | 13 | PASS |
| 13 | 20 | 20 | 19 | PASS |
| 14 | 13 | 13 | 9 | PASS |
| Total | 144 | 144 | 126 | PASS |

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:15-44` recomputes all fourteen region totals before each draw.

Its outer region draw at lines 57-72 uses only those summed regional weights.

No alternate automatic package draw bypass was found.

## Correction to the first completion-gap audit

Status: **CORRECTION REQUIRED**.

`006_current_completion_gap_audit_2026_07_24.md` is an at-the-time pre-fix audit and must not be used as current allocator evidence.

Its broader six-package capacity finding was correct.

Its pre-fix candidate table incorrectly identified IW-173 and IW-184 as Gathering or Rising contamination paths and IW-179 as a Totalen contamination path.

IW-173 and IW-179 already required the canonical attestation in `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt:504-516` and lines 541-553.

IW-184 already required the canonical attestation in `common/scripted_effects/006_independence_wave_packages_region_14_effects.txt:263-275`.

The confirmed pre-fix adapter-backed contamination paths were IW-018 at Gathering Storm and IW-043 and IW-058 at Rising Chaos.

The new centralized calculator gate closes those paths and also protects every current or future regional candidate without relying on package-local preparation checks.

The first audit remains useful for non-allocator completion gaps, but its automatic-band and candidate-contamination paragraphs are superseded by this re-audit and the corrected implementation handoff.

## Capacity witness

Status: **PASS for the current exact six**.

The conservative capacity witness has eleven explicit current package wrappers at `common/scripted_triggers/006_independence_wave_triggers.txt:405-503`.

Each wrapper writes its exact package ID before calling `is_independence_wave_runtime_package_preflight_ready`.

That preflight requires both an execution adapter and the canonical content attestation at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:59-64`.

The capacity tries run at `common/scripted_triggers/006_independence_wave_triggers.txt:584-890`.

The final witness requires the selected count to equal the current exact target at lines 892-929.

Unadmitted witness entries cannot increase the selected count.

The current witness can therefore count at most the exact six admitted IDs.

Future limit: the conservative witness names only eleven package wrappers.

Promoting an admitted package outside that eleven-package witness will make it eligible for centralized automatic weighting but will not automatically increase the Liberations cluster capacity proof.

The capacity witness must be extended when later admissions are expected to unlock the seven- or ten-package bands.

## SCN-008 preflight

Status: **PASS**.

`independence_wave_scenario_attempt_ranked_packages` writes each ranked package ID into `independence_wave_execution_package_id` at `common/scripted_effects/006_independence_wave_scenario_effects.txt:386`.

It then checks `is_independence_wave_scenario_package_preflight_ready` before reservation at lines 388-395.

The scenario preflight directly requires the canonical content attestation at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:149-150`.

An unadmitted ranked package is recorded as `package_unready` rather than reserved.

The scenario reservation call also reaches the centralized anchor-phase gate through its regional publisher.

No SCN-008 content-attestation bypass was found.

## Execution preflight

Status: **PASS**.

The frozen execution validator writes each selected package ID into `independence_wave_execution_package_id` at `common/scripted_effects/006_independence_wave_execution_effects.txt:49`.

It requires the package adapter at line 60 and the country-scoped runtime package preflight at lines 63-67.

That runtime preflight includes the canonical content attestation.

The release loop rewrites the exact selected package ID again at line 259 before dispatching the frozen country.

No execution-preflight content-attestation bypass was found.

## Temporary-variable cleanup

New planner scratch cleanup: **PASS**.

The two new planner bridges each have a matching unconditional `clear_temp_variable` at the end of their scripted effect.

Repository-wide scratch hygiene: **LIMIT**.

The pre-existing IW-173, IW-179, and IW-184 regional preparation helpers write `independence_wave_execution_package_id` before their local attestation and do not clear it when the unadmitted branch skips the centralized calculator.

The SCN-008 ranked loop also leaves the final mirrored execution package ID after the loop.

The conservative capacity wrappers set the same temporary ID while testing their candidates.

No functional bypass was found because every later attestation consumer overwrites the temporary ID immediately before checking it, and the selected reservation path overwrites and clears it.

The remaining values are still avoidable scratch residue and should be cleaned or explicitly documented during a later narrow hygiene pass.

## Exact-band re-evaluation

The six admitted packages have these earliest automatic bands:

| Package | Earliest band |
|---|---|
| IW-001 | Calm |
| IW-004 | Calm |
| IW-007 | Rising |
| IW-008 | Gathering |
| IW-017 | Calm |
| IW-019 | Gathering |

| Band | Exact target | Attested candidates eligible by band | Post-fix result |
|---|---:|---:|---|
| Calm | 3 | 3 | Conditionally plannable from IW-001, IW-004, and IW-017 when all live host, anchor, collision, force, and transaction checks pass. |
| Gathering | 4 | 5 | Conditionally plannable from IW-001, IW-004, IW-008, IW-017, and IW-019 without an unadmitted positive-weight candidate. |
| Rising | 5 | 6 | Conditionally plannable from all six admitted packages without an unadmitted positive-weight candidate. |
| Chaos | 7 | 6 | Fails closed at the exact capacity witness. |
| Totalen Krieg | 10 | 6 | Fails closed at the exact capacity witness. |
| World Collapse | 10 | 6 | Fails closed at the exact capacity witness and remains exactly ten. |

This is a source-level availability result.

It is not proof that every live host and anchor configuration can supply the conditionally plannable three-, four-, or five-package band.

## Parent handoff review

Status: **PASS**.

`006_automatic_content_attestation_weight_gate_2026_07_24.md` now names IW-018, IW-043, and IW-058 as the confirmed pre-fix contamination paths.

It explicitly excludes IW-173, IW-179, and IW-184 because their regional preparation effects already had package-local attestation gates.

Its counts of 144 calculator calls, 149 reservation publishers, fourteen regional random lists, and six attested IDs match this audit.

Its scratch-cleanup claim is correctly limited to the end of every centralized calculation and both new planner scratch uses.

Its statement that the higher bands remain blocked is accurate.

## Source-map and resume review

Allocation wording: **PASS**.

`006_source_of_truth_map.md:99` and lines 183-191 accurately describe the centralized repair, the six-package current set, the conditional three-, four-, and five-package bands, and the blocked seven- and ten-package bands.

`006_independence_wave_resume_packet.md:101-104` accurately describes the same post-fix behavior.

Current-state consistency: **FAIL**.

The resume packet still says only IW-004 and IW-007 are content-attested at lines 11-16, despite its own exact six-package statements at lines 92 and 181.

The resume packet still says sixteen exact package attestations remain binding at lines 324-325.

The source map still says sixteen exact package attestations must be preserved at lines 363-364.

The source map's contradiction table still describes IW-006, IW-043, IW-058, AJX, and the Pacific package tranche as restored, admitted, attested, or promoted at lines 348-355 even though none appears in the canonical six-ID trigger.

Those stale passages do not alter runtime behavior, but they prevent the source map and resume packet from being reliable current-state handoffs without additional reconciliation.

## Meaningful validation

- Parsed all fourteen regional package-effect files and confirmed 144 preparation helpers, 144 centralized calculator calls, 149 anchor-phase reservation calls, fourteen random lists, and 126 unique random-list package IDs.
- Confirmed every random-list ID maps to its same-ID reservation publisher and has a preparation helper.
- Confirmed every preparation helper initializes its package weight to zero and copies only the centralized candidate weight.
- Confirmed the canonical attestation trigger contains exactly six IDs.
- Confirmed the admitted earliest-band sequence is 0, 0, 2, 1, 0, and 1 for IW-001, IW-004, IW-007, IW-008, IW-017, and IW-019.
- Traced the ordering of the candidate-weight gate, anchor-phase gate, host reservation, country reservation, state reservation, SCN-008 preflight, capacity witness, and execution preflight.
- Used the read-only HOI4 probability inspector on Region 2, the region containing the confirmed pre-fix IW-018 path.
- The inspector reported a complete nine-candidate `random_list` pool with zero unresolved entries and source revision `3adfb8b48d29fc54154faef5ee17a681b86d1cb732a1bf2a1c6ece037043ebcb`.
- Inspector artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf895df1f5ef4a6d9a88c9dac3a6a7c675bf936f527664ebbb205b2162289d3b/b72abc41b620d9af06363c6dfc098261a88944b6f46ea8a9b1a36833ffaab3bc/probability-inspect-56b159655eab.json`.

## Remaining limits

- No in-engine automatic wave was executed.
- No seeded dynamic weighted sweep was available for live host, state, Event 5 collision, or sponsorship conditions.
- Calm, Gathering, and Rising remain conditional on every live reservation and transaction check.
- Chaos, Totalen Krieg, and World Collapse remain unavailable with only six admitted packages.
- The conservative capacity witness needs explicit extension for later admitted packages outside its eleven current wrappers.
- Pre-existing scratch execution-package values remain after several regional, scenario, and capacity helper paths, although no bypass was found.
- Source-map and resume admission wording remains internally contradictory.
- The first completion-gap audit contains a corrected pre-fix candidate-list error and is superseded for allocator behavior.
- This repair does not admit a package or complete Event 006.
