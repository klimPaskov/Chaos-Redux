# Event 032 site-work regression handoff

Updated 2026-10-09.
Disposition: `implemented` parent completion of the regression worker's partial file; native runtime and complete Event 032 acceptance remain unproven.
Acceptance basis: the user goal requires actual survey settlement and human/AI parity, and the parent delegated this exact test scope to `chaosx_scripted_system_architect` with `fork_context=false`.
The worker created the initial eight-test file but its first and resumed turns failed with `workspace routing discovery timed out`.
Authoritative thread status was checked before resuming the same worker.
The parent reviewed its partial source, completed the remaining regressions and ran the integration checks.
No completed worker audit is invented from that failed route.

## Changes and executed source

`.tools/test_event32_site_work_transactions.py` executes the actual survey/recovery wrappers, new receipt/quote/garrison predicates, shared native cost payment/credit branches, before/after measurements and shared date helpers.
Its typed wallet primitives may decline, clip or misreport observations; those are native boundary scenarios, not synthetic helper return values.
The production helper still performs its own dispatch, measurement and acknowledgement.
Private helper frames discard newly created temporaries and retain caller-owned outputs.
The native resource readers and units are explicitly supplied as country facts.
Foreign ROOT scenarios retain the actual current payer for all wallet changes.

Eighteen tests cover:

- Per-resource below/exact/above quote gates for survey and recovery, plus display/gate sharing.
- Accepted native decision entry, one payment, a frozen duration/quote/state/payer receipt and duplicate-start refusal.
- Rejection for lost/invalid/registered/impassable state, inactive authority, active/native mission and existing financial holding.
- Day 0, 30, 60, overdue and fractional-day progress refunds with integer floors; later tuning does not reprice the payment.
- Missing, nonpositive, stale-generation, wrong-payer or mismatched-site receipt proof; no fabricated return or site success.
- Zero and partial native payment, rollback of only observed removal, no funded mission on incomplete payment.
- Capacity-limited native credit, retained remainder and once-only retry; inconsistent observations quarantine further credit.
- Missing, inflated, mismatched or already-returned pending balances retain their record and cannot authorize another native credit.
- An unavailable pre-observation prevents payment/credit, retains its anomaly evidence and stops later refund components in the same pass.
- Zero-return success performs no native reads or mutation, even when the next reader would be unavailable.
- Successful due survey, zero refund and one registration-consumer request; duplicate cancellation/completion/timeout creates no second request or credit.
- Depleted wallets, foreign ROOT, and removed-country settlement without crediting another country.
- Human/AI zero/one/two owned divisions, foreign troops excluded, identical entry/goal gates and no troop exemption.
- Early, lost/scuttled/switched site, wrong actor, stale rogue context and inactive-crisis completion; no reward or crisis closure.
- Correct recovery of the exact site, one command-control reward/incident closure and removal of the recovery/context receipt.

The first run found a fixture date-offset expectation of `1.440` rather than the shared contract's `0.0144` for 60 days.
The assertion now derives the expected offset from the authoritative date-unit constants and still asserts the purchased 60-day duration.
This changed no gameplay time.
The garrison tests exposed missing support for documented trigger-side `subtract_from_temp_variable` in the bounded VM.
Installed trigger documentation and the live checker confirmed its command kind and ANY scope; the fixture now executes the existing arithmetic path instead of replacing the production predicate.
The native removal leaf follows the installed `remove_mission` contract and executes no completion/timeout callback.

Source parsing is cached once per test process; each scenario copies its own tuning dictionary and creates fresh world/actor/state objects.
This removes repeated parsing without sharing wallet, flags, receipt or callback state between cases.
No helper body is replaced with a successful stub.

## Existing test integration

`test_event32_project_missions.py` retains all fourteen project/lifecycle tests.
It follows the paid-survey wrapper into its actual begin owner, accepts frozen purchased duration, checks due-date addition in the correct order and verifies recovery cleanup through its explicit cancellation helper.
Its old assertion requiring an AI bypass is replaced by shared native garrison/receipt checks, with behavioral counts exercised in the new suite.

`test_event32_state_scope.py` retains all thirteen scope/cleanup tests and extends source review to the survey owner.
It follows the exact FROM STATE gate and stored pointer through the new paid entry instead of requiring the previous inline syntax.
Country existence checks remain excluded from STATE scope.

The already-untracked other-owner `test_event021_claimant_missile_scope.py` receives only a loader adaptation for real quote/pending-return helpers and their constants.
Its eleven original foreign-ROOT and split assertions remain intact and pass.
The pending-return body is loaded, but those cases have no pending survey balance and exercise its actual inactive guard.
This is no refund execution claim for the claimant fixture.
The file is not staged wholesale by the Event 032 parent.

Exact owner carry patch for the final loader adaptation, already applied in the shared file:

```diff
*** Begin Patch
*** Update File: .tools/test_event021_claimant_missile_scope.py
@@
 EVOLUTION = source("common/scripted_effects/032_missiles_evolution_effects.txt")
+SURVEY = source("common/scripted_effects/032_missiles_survey_effects.txt")
+RECOVERY = source("common/scripted_effects/032_missiles_recovery_effects.txt")
 EFFECTS = {**CORE, **OPS,
+           **SURVEY, **RECOVERY,
@@
 CONSTANTS = {**source("common/script_constants/032_missiles_constants.txt"),
+             **source("common/script_constants/032_missiles_survey_constants.txt"),
+             **source("common/script_constants/032_missiles_recovery_constants.txt"),
*** End Patch
```

## Validation and limits

The pending-return guard also needs its actual trigger loader in the claimant owner file:

```diff
*** Begin Patch
*** Update File: .tools/test_event021_claimant_missile_scope.py
@@
 TRIGGERS = {**source("common/scripted_triggers/032_missiles_triggers.txt"),
+            **source("common/scripted_triggers/032_missiles_survey_triggers.txt"),
*** End Patch
```

The final new suite passes 18 tests.
The full Event 032 run passes 177 tests, including the new suite and original project/scope assertions.
The claimant fixture passes all 11 tests.
Final payload integration is separately recorded in the parent implementation report.

Native wallet/world facts, currency/equipment mutation, mission activation/removal and presentation are explicit boundaries.
Survey registration captures the exact state, payer and payment proof as a consumer boundary; it does not simulate physical construction or synthesize a registration acknowledgement.
Recovery executes its existing site restoration and crisis/achievement helpers, while their native presentation/event requests retain declared boundaries.
The VM does not prove native quantity visibility, producer/variant recovery, game precision, timed callback ordering, actual AI movement or local division supply.
The concrete-garrison alternative is the accepted source route; no supply proxy is presented as a supply measurement.
No probability, GUI, map or whole-event completion evidence is claimed by these tests.

Reference evidence includes installed trigger documentation 2648–2662 and 7624–7630, dynamic variables 385–386, 469–470 and 557–559, effects 6083–6095, and the shared native cost and date API documentation.
The live subtraction check returned `SCRIPT_CHECK_PARTIAL`: command kind/scope supported, with parameter blocks unchecked.
Its documentation revision is `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The parent read the answering subtraction section through the revision-bound reference route at `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
There was no game launch, log access, external source dependency edit or autonomous desktop test.
The worker's test changes and parent completion introduce no gameplay simplification.
The complete survey candidate-pool/highest-score design, broader payload custody and remaining event acceptance are still parent work and are not closed by these tests.
