# Event 006 dormant release capital-scope audit — 2026-08-15

## Scope and outcome

This audit covers the Event 006 dormant-carrier preflight, package dispatch, allocator, release, setup, finalization, and commit gates. It does not change the pre-event decision/category surface, central attestation, or the joint Join surface.

The pasted AXX/BAX/BBX invalid-capital failures exposed a package-wide pattern rather than three isolated files. I replaced every fixed numeric `capital_scope = { state = N }` check in the current Event 006 package-trigger files with the vanilla state-scope form `N = { is_capital = yes }`. The patch covers 118 checks in 34 files, including FER's 408/409 OR. Dynamic or controlled `capital_scope` checks were intentionally preserved.

## Current supersession notice (2026-08-26)

This dated audit retains its `exists = no` and joint expected-count findings as historical evidence only. Commit `7858a2b1f` supersedes the release wording with the dormant-country-scope predicate, and commit `d6abc3792` supersedes the unresolved joint-count overwrite with actual Event 005 plus Event 006 selected-count recomputation; use the current source-of-truth map and resume packet for routing.

## Severity-sorted findings

### High — fixed in this tranche: dormant carriers could still resolve `capital_scope`

`capital_scope` is a country-to-state dual scope and can be an invalid target when the dormant carrier does not exist. The offline Scopes and Triggers wiki pages describe this invalid-target behavior, while vanilla `triggers_documentation.md` documents `is_capital` as a STATE trigger and gives the direct state-scope form `169 = { is_capital = yes }`.

Before this patch, runtime-ready, setup-initialization, prepared-origin, and FER capital-anchor predicates still used fixed numeric `capital_scope` checks. Those predicates can be reached from shared package dispatch or live validation while a target is still being represented by a reserved dormant carrier, so the BAX/BBX/AXX errors were symptoms of a reusable source defect.

After this patch, fixed state checks resolve a state scope that is always available, and `is_capital` verifies that the selected anchor is the live country's capital once the release exists. Existing `N = { is_owned_and_controlled_by = ROOT }` checks continue to prove ownership/control where present.

### Historical finding — superseded: joint partial allocation overwrote the shared expected-count contract

The following joint-count paragraphs preserve the 2026-08-15 diagnosis only; commit `d6abc3792` is the current source authority for the recomputation repair.

The standalone allocator's pool-exhaustion branch intentionally lowers `global.independence_wave_plan_target_count` and `global.liberation_plan_expected_country_count` to the selected Event 006 subset when at least one candidate exists. The standalone executor then requires selected, instantiated, transferred, validated, initialized, and committed counts to match that selected subset, so a non-empty partial standalone package cannot commit unless every selected row passes all barriers.

The same allocator is called by `liberations_joint_prepare_and_execute_incident` after Event 005 has already set `global.liberation_plan_expected_country_count` to Event 005 selected rows plus the nominal Event 006 target. If Event 006 exhausts its pool and takes the partial branch, it overwrites the shared expected count with Event 006 selected rows only. `liberation_release_validate_plan` later requires `global.liberation_plan_package_ids^num` to equal that shared expected count, so a joint plan with any Event 005 rows is expected to fail the central contract before ownership execution. This remains a parent-owned follow-up; no central Join or attestation code was changed here.

### Medium — bounded evidence: event MCP analysis is partial

Read-only `hoi4.event_inspect` and `hoi4.event_render` both returned `EVENT_*_PARTIAL` with no blocking diagnostics, but deferred workspace-wide helper/lifecycle projections because the workspace contains 9,500 events and 36,000+ edges. The artifacts are useful source-linked evidence, not a substitute for live gameplay validation.

### Low — deliberate boundary: non-package compatibility predicates remain unchanged

The four remaining `capital_scope` checks inside package-trigger files are controlled/dynamic checks, not fixed numeric dormant-capital lookups: `006_independence_wave_iw043_iw058_package_triggers.txt:1047`, `:1057`, `006_independence_wave_karelia_crimea_package_triggers.txt:195`, and `006_independence_wave_pacific_package_triggers.txt:177`. Compatibility-trigger files outside the requested package-trigger set also retain their existing live-country capital predicates.

## Changed package-trigger files and state anchors

- `common/scripted_triggers/006_independence_wave_altai_package_triggers.txt`: IW-053 ALT, state 654, 3 checks.
- `common/scripted_triggers/006_independence_wave_banat_package_triggers.txt`: IW-024 AXX, state 82, 3 checks.
- `common/scripted_triggers/006_independence_wave_bashkiria_package_triggers.txt`: IW-045 BSK, state 651, 3 checks.
- `common/scripted_triggers/006_independence_wave_bosnia_package_triggers.txt`: IW-029 BOS, state 104, 3 checks.
- `common/scripted_triggers/006_independence_wave_brittany_package_triggers.txt`: IW-004 BRI, state 14, 2 checks.
- `common/scripted_triggers/006_independence_wave_buryatia_package_triggers.txt`: IW-052 BYA, state 564, 3 checks.
- `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt`: IW-014 CAT, state 165, 2 checks.
- `common/scripted_triggers/006_independence_wave_epirus_package_triggers.txt`: IW-028 BBX, state 185, 3 checks.
- `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt`: IW-057 FER, states 408 and 409, 2 checks.
- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`: IW-013 NAV state 792 and IW-015 GLC state 171, 4 checks.
- `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt`: IW-012 ICE, state 100, 2 checks.
- `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`: IW-043 CHU state 249 and IW-058 ASY state 676, 2 fixed checks; its controlled `capital_scope` checks remain.
- `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt`: IW-033 KAR state 146 and IW-041 CRI state 137, 6 checks; its controlled `capital_scope` check remains.
- `common/scripted_triggers/006_independence_wave_khakassia_package_triggers.txt`: IW-054 KHA, state 569, 3 checks.
- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt`: IW-050 KOM, state 397, 3 checks.
- `common/scripted_triggers/006_independence_wave_kosovo_package_triggers.txt`: IW-031 KOS, state 802, 3 checks.
- `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt`: IW-040 KUB, state 234, 3 checks.
- `common/scripted_triggers/006_independence_wave_kurdistan_package_triggers.txt`: IW-060 KUR, state 421, 4 checks; the package comment now describes the state-capital proof without the obsolete `capital_scope` wording.
- `common/scripted_triggers/006_independence_wave_macedonia_package_triggers.txt`: IW-026 MAC, state 106, 3 checks.
- `common/scripted_triggers/006_independence_wave_mari_package_triggers.txt`: IW-047 MEL, state 833, 3 checks.
- `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt`: IW-017 COR state 1, IW-018 ARX state 114, and IW-019 ASX state 115, 6 checks.
- `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt`: IW-030 MNT, state 105, 3 checks.
- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`: IW-184 HBX state 378, IW-173 HAW state 629, IW-179 FSM state 684, and IW-177 FIJ state 636, 8 checks; its controlled `capital_scope` check remains.
- `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt`: IW-008 RHI state 51 and IW-009 BAY state 52, 4 checks.
- `common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt`: IW-038 RUT, state 73, 3 checks.
- `common/scripted_triggers/006_independence_wave_saar_package_triggers.txt`: IW-010 AJX, state 42, 2 checks.
- `common/scripted_triggers/006_independence_wave_sakha_package_triggers.txt`: IW-051 YAK, state 574, 3 checks.
- `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt`: IW-001 SCO state 121 and IW-002 WLS state 122, 4 checks.
- `common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt`: IW-044 TAT, state 249, 3 checks.
- `common/scripted_triggers/006_independence_wave_thrace_package_triggers.txt`: IW-027 BAX, state 184, 3 checks.
- `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt`: IW-070 state 230, IW-071 state 231, and IW-072 state 229, 9 checks.
- `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt`: IW-023 TRA, state 84, 3 checks.
- `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt`: IW-048 UDM, state 399, 3 checks.
- `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt`: IW-006 AFX state 34 and IW-007 AGX state 36, 4 checks.

## Lifecycle and release-gate notes

- At the 2026-08-15 snapshot, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` preflight explicitly required `exists = no`, an execution adapter, content attestation, and the exact dormant package admission predicate; current routing uses the dormant-country-scope predicate and does not resolve a dormant carrier's capital.
- `common/scripted_effects/006_independence_wave_execution_effects.txt` validates the reserved carrier as dormant before release and validates the fixed anchor and former host before any release effect runs.
- The release pass creates the frozen country, sets its capital to the selected anchor, then dispatches package setup and live runtime gates. The state-scoped `is_capital` replacements therefore preserve the post-release contract without requiring an absent-country capital scope.
- Failed metadata, instantiation, ownership transfer, setup, finalization, or origin-commit counts remain fail-closed; the standalone wrapper restores host capitals and aborts before mutation when execution has not started, and runs compensating rollback after mutation.

## Required audit surfaces

### Decision category lifecycle and cognitive load

Not applicable to this runtime-only tranche. No decision category, mission list, visible value, tooltip, pre-event report, scripted GUI, or player-facing count was changed. The existing Event 006 pre-event surface is already retired according to the adjacent dormant-release handoff.

### Mission quality

Not applicable. No mission or timed objective is owned by this audit.

### Cost and requirement clarity

No spendable cost or requirement text changed. Runtime requirements remain adapter/content attestation, dormant reservation, fixed anchor ownership/control, former-host validity, aligned metadata arrays, and package lifecycle receipts.

### AI validity and route locks

No AI weight or target score changed, so no probability target was altered. The existing adapter, attestation, reservation, and owner gates remain fail-closed; joint Event 005 plus Event 006 partial-count behavior is the outstanding route-lock risk described above.

### Localisation and tooltip gaps

None introduced. This source-only trigger patch has no localisation identifiers or tooltip strings.

### Cleanup and exploit risk (2026-08-15 snapshot; joint-count text superseded)

The state-scope replacement removes invalid-target log noise without creating a release path for an unreserved tag. Zero-candidate allocation still fails closed, and non-empty partial standalone allocation still passes all count and cleanup barriers before commit. At that snapshot, the joint expected-count overwrite was a correctness failure risk rather than a partial-release exploit because central plan validation ran before ownership mutation; the source overwrite is now repaired by `d6abc3792`, while joint execution remains unproven.

## Evidence and validation

- `python .tools/audit_event6_allocator.py` passed with 149 publishers, 40 runtime adapters, 32 attestations, 29 compatible reservation groups, and the documented 3/4/5/7/10 automatic ladder.
- A current static scan found 118 `N = { is_capital = yes }` checks and zero fixed numeric `capital_scope = { state = N }` checks across `common/scripted_triggers/006_independence_wave_*package_triggers.txt`.
- Read-only `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics for `events/006_independence_wave.txt`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62395d101a35e8ba9adbd53a6a64e1a92fc904294746fc74fc72d8ae1d48cbe8/f9564375907b9895c1bd912686cc2a82f91196183c23ae32512302edbc1147f9/event-state_flow-a0d209ec728f.json`.
- Read-only `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` with no blocking diagnostics. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e518a4ead46cba32e0cfbd32d5d4dac2b44523d3800d9d4885906493720148c7/858a2e321160c3fe1d4195c946886ed3b3dbe4957474224c79a66544352f278d/event-state-a0d209ec728f-manifest.json`; JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8f1fa321efd810b63083bae2b58cde1b6f92c1e0fedafbca99d66e2bd3c88ce/794d09cdd71fbf3180ab3c4cb74c644f1bd861b818895b9995ee2b11c949fae9/event-state-a0d209ec728f.json`; PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a78306fd5428e521da7b7c2c841f1d3f1366a83362800205bf6118edbdb5ea14/12f828d1aeb3187b7eab914b0b57d53fba3ad6e8c3ffcf63db96de2115c4554e/event-state-a0d209ec728f.png`.
- No live Hearts of Iron IV process was launched, as required by the repository instructions; live triggering and save-state validation remain parent/user work.

## Historical recommended follow-up (superseded 2026-08-26)

The 2026-08-15 recommendation was to keep the broad fixed-state patch and add a narrow allocator guard for joint plans so the partial Event 006 branch updated the shared expected count to Event 005 selected rows plus Event 006 selected rows, rather than Event 006 selected rows alone. Commit `d6abc3792` records that source repair; do not widen central attestation or Join as part of any remaining validation.

## Remaining uncertainty

The MCP event analysis is workspace-partial, and the joint partial-allocation path has not been live-tested. No other simplification or fallback was introduced in this tranche.
