# IW-030 Montenegro decision repair — 2026-08-06

## Scope

This handoff records the parent-owned repair of the IW-030 Montenegro decision and mission surface after the current country, decision, and probability audits.

## Changed source

- `common/script_constants/006_independence_wave_montenegro_constants.txt`
  - Raised `independence_wave_montenegro_duration.founding_crisis` from 420 to 540 days.
  - Added the MNT one-factory cost profile and a zero factory-floor constant.
- `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt`
  - Added `is_independence_wave_mnt_project_ready` so every paid project requires the complete setup receipt and cannot reopen after a terminal founding failure.
  - Added `has_independence_wave_mnt_unsettled_host` for an absent or hostile former host.
  - Added MNT-specific administration and sovereignty cost gates that match the one-state opening economy.
- `common/decisions/006_independence_wave_montenegro_decisions.txt`
  - Applied the setup gate to all ten project decisions.
  - Switched MNT administration and sovereignty decisions to the MNT cost profile.
  - Added the missing civilian-factory commitment to the two route-administration projects and durable-sovereignty project.
- `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt`
  - Deduplicated project-failure penalties when an active project and the founding mission cancel in the same incident.
  - Gives the depot settlement a larger crown-legitimacy gain when no bilateral host settlement is possible.
  - Guards generic formable discovery behind an actually registered formable family.
  - Clears the failure latch during setup and cleanup.
- `localisation/english/006_independence_wave_montenegro_l_english.yml`
  - Added MNT-specific factory-cost strings and clarified failure/sovereignty outcomes.
- `docs/events/006_independence_wave/montenegro_package.md`
  - Documents the 540-day window, one-factory cost profile, hostless path, and formable-discovery guard.

## Behavior proof

The critical path remains 75 days for depots, 120 for guards, 120 for offices, and 180 for former-host ledgers: 495 days total. The 540-day mission now leaves a bounded 45-day reaction margin. When the former host is absent or at war, depot reopening uses the decisive crown gain so the non-bilateral path can still reach the 60/60 compact threshold after the other three local projects.

All ten project blocks now contain the setup-ready trigger in both visibility and availability. The failure latch prevents the active-project cancellation and founding-mission cancellation from applying the same penalty twice, and cleanup clears it for a later generation.

The former-host ledger cancellation also has a guarded host-loss path. If MNT still controls its capital but the former host has disappeared or entered a war with MNT, the project closes the ledger with decisive crown legitimacy and marks the settlement complete without applying bilateral host deltas. A live, peaceful former host continues through the normal negotiated settlement; loss of capital or package identity still applies the single failure penalty.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 23 attested packages, 22 compatible reservation groups, and the 6/8/10/14/20 release ladder.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
- `python -B .tools/audit_event6_flags.py` passed all 102 registered Event 006 tag flag families.
- Static decision scan confirms all ten MNT projects use the setup-ready gate in visibility and availability.
- Fresh MCP `hoi4.probability_inspect` on the edited MNT decision source passed source discovery with one decision candidate and ten required inputs, and the mission adapter found ten candidates and thirteen required inputs. Both pools remain incomplete because world-state eligibility is runtime-dependent, so these receipts do not claim normalized click probabilities. The decision artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb34f227acc2a954b668f8b4cb9e9307820f00dd40cb654605b1f003d6db821d/fb19b5a077a15f62a7c43b2a0f50c582ac85d59939c8981ca5b9cb3f1829d1e1/probability-inspect-e29f3c50fd11.json`; the mission artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14f0f6a58d98085c5754abe497d90de1084b61812573d7fb066b749cc87c45a6/ccbb41a110e8dcff6c9b68bc9bb9fe71d8afa1f9e8200b5514e1eff7272a5392/probability-inspect-e29f3c50fd11.json`.
- MCP probability evidence remains unavailable for the MNT `ai_strategy_factor` surface (`PROBABILITY_SURFACE_EMPTY`); no quantitative AI claim is made.
- Runtime release, dynamic-force materialization, save-load, portraits, and final MNT admission remain outside this repair and remain fail-closed.

## Remaining gates

IW-030 remains outside central content attestation. The three grounded male leader portraits remain rights/provenance/runtime-promotion gated, the vanilla `MNT_1936` OOB reference still needs parent-owned dynamic-force runtime evidence, and typed AI probability evidence is still incomplete.
