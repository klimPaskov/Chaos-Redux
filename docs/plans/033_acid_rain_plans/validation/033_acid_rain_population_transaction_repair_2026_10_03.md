# Population-first exact civilian-loss transaction

Disposition: implemented source repair with engine acceptance unresolved.
Acceptance basis: the user's Event 033 goal requires real state population removal, an authoritative applied result, zero deaths for zero removal, and exactly one Deaths record without duplicate loss.
The shared helper is the required gateway, so correcting its measured-output contract is within that implementation scope.

## Defect and repair

`apply_exact_state_civilian_population_loss` previously returned a rounded, clamped request and passed it to Deaths before state population was read back.
That ordering could record a calculated death amount when the native population mutation applied a different amount or zero.
The Event 033 caller's later mismatch flag could not undo that already committed record.

The helper snapshots state population in people, rounds a fractional protected minimum upward, floors whole-person availability above that minimum, rounds and clamps the request, and applies one state-scope population transaction.
It then reads the state's population again and returns the observed nonnegative decrease as `state_civilian_population_loss_applied`.
Only an observed positive decrease reaches Deaths registration.
Registration uses the existing record-only path, `chaos_deaths_apply_state_pop = 0` and `chaos_deaths_record_state_ledger = 1`, so state population is not removed twice.
The existing cause, target country, logging policy, recruitable-credit reconciliation, state ledger, and shared Chaos progression remain in force.
No country manpower debit or modifier serves as population-loss proof.

Public input names and the zero/positive result convention are unchanged.
Consumers of the temporary outputs must declare them before calling the helper.
This requirement is documented with the usage example.
The completed cross-system caller audit is `033_acid_rain_exact_helper_caller_review_2026_10_03.md`.
It reviewed all 213 executable call sites in 17 script files and confirmed record-only/zero-log compatibility, but found twelve receipt consumers without caller-owned output storage and two floor-input gaps.
The completed bounded caller repair is documented in `../subagent_handoffs/caller_repairs_2026_10_03.md`.
Current-source replay refresh is required because an additional Event 29 achievement hook changed one of its recorded blocks.
That concurrent hook is preserved, and the original evidence is not promoted into a current pass.
The API-only Migration mortality-floor policy remains an explicit queued owner input.
No compatibility pass is assumed from the source-order test.

## Changed surfaces and evidence

- `common/scripted_effects/chaosx_dynamic_effects.txt`: population-first gateway and observed output.
- `common/scripted_effects/chaosx_dynamic_effects.md`: exact public contract, record-only semantics, protected fractional availability, and initialized-output example.
- `.tools/validation/validate_033_acid_rain.py`: source regression assertions for one physical transaction, readback before registration, measured Deaths input, and record-only registration.

The checkpoint is `033_acid_rain_population_first_checkpoint_2026_10_03.json`.
It passed the new source-order assertions and the existing synthetic mortality, coverage, Air, lifecycle, and catalog checks.
The helper source at that checkpoint has SHA-256 `8b4db4f595a607d041d0f072de65dd906cdb10c40246690f78d3e4305dab4d49`.
The subsequent fractional-minimum ceiling repair has source SHA-256 `f9591fe2beab4ac7570813ba76d1b4dbf63fc9ff10dc3315adfffccab2a895c2`.
Its source contract assertions pass, while its actual-source fractional/partial/native-primitive replay remains a separate pending check.
The synthetic mortality model still assumes its modeled population operation succeeds.
It is not execution of this helper or evidence of engine rounding, zero-application behavior, save persistence, or multiplayer authority.

## Required source reading

| Source | Relevant span | Local SHA-256 |
| --- | --- | --- |
| Installed `documentation/effects_documentation.md` | 1468–1476, STATE and COUNTRY `add_manpower` scopes | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation/dynamic_variables_documentation.md` | 1168–1175, `state_population_k` | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 3358–3365, state total-population mutation and recruitable-credit side effect | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 434–450, caller-declared temporary output persistence | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |

The existing shared `chaos_meter_register_deaths` and `chaos_meter_record_state_civilian_deaths_from_deaths_change` definitions were read directly.
Record-only consumers in the Asteroid, Missiles, camp, civilian-transfer, and fallout systems provide project precedents; no shared Deaths implementation was edited by this repair.
The installed effect documentation supplies the primary native scope contract, and the offline wiki was read in parallel.
Fractional minimum and availability handling also reads installed `round_temp_variable` documentation at lines 6476–6484 and the offline Effects rounding row at line 714, which describes nearest-integer and tie rounding.
The upward minimum and downward availability corrections prevent either rounding step from crossing the supplied protected minimum.

## Route and runtime limits

The live `hoi4.reference_context` event-surface request for this transaction returned `timed out awaiting tools/call after 600s` with no source revision or artifact.
A narrower `hoi4.reference_search` request for `state_population_k`, limited to one installed-game-document result, also returned `timed out awaiting tools/call after 600s` without a citation, source revision, or artifact.
The relevant local sections above were read directly.
The connected catalog does not expose `hoi4.script_validate`.

Real population-before/after and matching state/country/global/cause/report/achievement deltas must still be supplied for ordinary, severe, global-transition, sustained, superstorm, zero, floor, duplicate, interruption, reload, and second-generation cases.
Native engine precision and the preserved settings-disabled logging policy also remain explicit acceptance cases.
No game was launched, no fresh log was requested, and no clean-error-log or full Event 033 completion claim is made.
