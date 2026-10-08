# Event 012 Gods private public-value data API

Disposition: implemented source, pending parent review and native acceptance.
Acceptance basis: the parent task implements completion-audit F3 through the agreed Strength and personal Wrath fields, qualitative trends and existing producer hooks.
This contract supplies presentation data for exactly the two existing public values.
The relationship, contribution, grading, contract and component ledgers remain private.

## Scope and helper map

All effects use country scope and the ordinary `helper = yes` interface.
There are no dollar parameters, new event targets, registry entries, timers, world scans or temporary variables.

| Helper | Inputs | Outputs and side effects | Defaults and direct callers |
| --- | --- | --- | --- |
| `gods_of_africa_observe_public_strength` | Current country matching the existing `africa_host` target, `global.gods_of_africa_strength`, this host's previous observation and known-sample flag | Writes the three global Strength presentation fields, host Strength trend flags, host previous raw observation and known-sample flag | A missing target, wrong country or absent raw global value produces no writes. An absent or incomplete sample produces an accurate cache and neutral trend. Called after the initial global Strength assignment in `gods_of_africa_initialize_system` and after the committed global assignment in `gods_of_africa_refresh_strength`. |
| `gods_of_africa_observe_public_wrath` | THIS country's raw `gods_of_africa_wrath`, previous observation and known-sample flag | Writes THIS country's three Wrath presentation fields, Wrath trend flags, previous raw observation and known-sample flag | Absent raw Wrath produces no writes. An absent or incomplete sample produces an accurate cache and neutral trend. Called by the private committed-value gate. |
| `gods_of_africa_observe_public_wrath_commit` | THIS raw Wrath, previous observation, known-sample flag and presence of a positive in-flight `gods_of_africa_wrath_request` | Calls the Wrath observer for first/incomplete samples, changed committed raw values or the current Wrath transaction | Called once at the end of the guarded `gods_of_africa_enforce_wrath_floor`. An unchanged direct floor check without an in-flight positive request produces no presentation writes and preserves the last observed movement. This prevents the registry's agreement-war path from observing its own completed `apply_wrath` result twice. |
| `gods_of_africa_clear_public_strength_observation` | THIS host's private presentation metadata | Clears host Strength trend flags, known-sample flag and previous observation | Idempotent. Does not change the global cache or any raw metric. Called on fresh host generation, authority loss and `gods_of_africa_clean_system`. |
| `gods_of_africa_reset_public_strength_values` | Existing owner path that also sets raw global Strength to zero | Sets global Strength display and fill to zero and frame to one | Idempotent. Does not change raw Strength or host metadata. Called immediately after the existing global zero assignment in the guarded current-target loss branch and in system cleanup. |
| `gods_of_africa_clear_public_wrath_values` | THIS country's private presentation metadata | Clears Wrath display, fill, frame, previous observation, known-sample flag and both trend flags | Idempotent. Preserves raw Wrath, its gameplay band, durable history, opt-out, grading and receipts. Called on enrollment before history/floor initialization, participant archive, participant cleanup, participant cancellation and final participant settlement. |
| `gods_of_africa_public_wrath_is_visible` | Actor country, presence of actor raw Wrath, optional existing `africa_host` target | Pure boolean result. No writes or scope change | True exactly when raw Wrath exists and THIS is not the country saved as current host. With no host target, an actor with raw Wrath remains eligible at this predicate level. Category owners supply the event lifetime/context gate. Defined in `common\scripted_triggers\012_africa_gods_public_values_triggers.txt`. |

Host identity checks use `tag = event_target:africa_host` in the current country scope.
They do not call the ROOT-sensitive `africa_is_current_host` predicate and do not substitute ROOT, FROM or PREV for the UI actor.
The existing producers still own generation and gameplay eligibility.

## UI fields and trends

| Field | Scope | Value |
| --- | --- | --- |
| `gods_of_africa_strength_display` | global | Whole-point floor of raw `global.gods_of_africa_strength`. |
| `gods_of_africa_strength_fill` | global | Raw global Strength divided by `constant:gods_of_africa_value.maximum_strength`, clamped to zero through one. |
| `gods_of_africa_strength_frame` | global | Floored Strength plus `constant:gods_of_africa_value.one`. Under the existing zero through 100 metric range, this is an optional one-based 101-cell native atlas selector. |
| `gods_of_africa_wrath_display` | actor country | Whole-point floor of this actor's raw `gods_of_africa_wrath`. |
| `gods_of_africa_wrath_fill` | actor country | Raw Wrath divided by `constant:gods_of_africa_value.maximum_wrath`, clamped to zero through one. |
| `gods_of_africa_wrath_frame` | actor country | Floored Wrath plus one, with the same optional atlas convention. |

The Strength trend flags live on the current host: `gods_of_africa_strength_trend_rising` and `gods_of_africa_strength_trend_falling`.
Wrath trend flags live on the actor: `gods_of_africa_wrath_trend_rising` and `gods_of_africa_wrath_trend_falling`.
Neither flag means neutral.
Every actual observation first clears both flags and then sets one only when the committed raw value differs from a valid previous sample.
Subpoint motion still establishes a trend even when the whole-point display stays unchanged.
A steady metric transaction clears a prior direction rather than implying continued movement.
An unchanged direct floor check without a transaction is not another observation and preserves the last actual observed movement.

The private samples are host `gods_of_africa_strength_previous_observed` plus `gods_of_africa_strength_sample_known`, and actor `gods_of_africa_wrath_previous_observed` plus `gods_of_africa_wrath_sample_known`.
These are observation metadata, never player-facing currencies or relationship standing.
The first observed value is stored without inventing a historical direction.

## Floor arithmetic and tuning

`round_variable = <presentation variable>` is the documented native command.
The helper rounds a copy of raw value, compares that copy to raw value and subtracts the existing one constant only if rounding raised it.
This yields mathematical floor without inventing `floor_variable` or borrowing the shipment flooring temporary.
All calculations operate on normal presentation variables and introduce no temporary scratch names.
The observers never round, clamp, smooth or otherwise write raw Strength or Wrath.

No constants are added.
Zero, one and the two maximums come from the existing `gods_of_africa_value` script-constant category.
The existing Strength boundaries 20, 40, 60 and 80 and Wrath boundaries 15, 30, 50, 70 and 85 remain gameplay-owned.
Next-threshold text must use the raw value or the existing gameplay classification, and whole-point current text must read the cache.
Fill uses raw value, not the floored display.
Frames are optional data for a future UI consumer and do not install an atlas, sprite or meter.

## Producer and lifecycle sequence

1. A fresh host generation clears only its prior Strength observation metadata, then the existing initializer commits starting raw country/global Strength and observes the global value once.
2. Strength refresh computes and smooths its existing raw value, commits the global copy, then observes once.
3. Enrollment clears stale personal presentation metadata before the existing history initializer restores or creates raw Wrath.
The existing floor refresh calls the floor owner and observes the final raw value, so initial displayed Wrath includes any applicable floor and starts neutral.
4. `gods_of_africa_apply_wrath` retains its existing increase/decrease, raw clamp and floor call.
The committed-value gate is inside the floor owner after its final clamp, with no second observer in `apply_wrath`.
Direct floor callers `gods_of_africa_refresh_participant_floors` and `gods_of_africa_mark_offender` therefore receive the same cache update.
`gods_of_africa_refresh_participant_floors` can call the existing agreement-war owner, which records a breach through `apply_wrath` before the outer floor call.
That outer unchanged floor call skips a duplicate observation because the transaction has already cleared its request, so it cannot wipe the recorded breach trend.
5. A decrease that is fully stopped by a floor is neutral, and a partially applied decrease reports falling from the prior committed value.
The requested delta and pre-floor intermediate value are never used for trend.
6. Archive, cancellation, cleanup and final settlement clear personal presentation metadata while retaining durable raw Wrath/history.
Enrollment reconstructs that cache from restored committed Wrath with a fresh neutral sample.
7. Authority loss clears retired-host sample/trend metadata regardless of whether the current target has moved elsewhere.
The global empty cache is written only inside the existing guarded loss branch that also writes raw global Strength to zero.
A stale losing host cannot erase a successor's cache through these hooks.
System cleanup similarly resets the public global cache alongside its existing raw zero assignment.

The only migration behavior is producer-bound observation.
If a running actor has raw values but lacks sample metadata, the next existing producer creates its accurate cache and a neutral baseline.
There is no startup backfill, new recurring hook or whole-world repair pass.
Initial host setup and participant enrollment already populate the cache before their normal public introduction paths.
The UI owner must keep an absent cache pending or guard its consumer until the existing producer has observed it, rather than display an invented zero as the actor's value.

## Cause context and usage

The UI owner may use existing host `gods_of_africa_strength_capital_lost`, host `gods_of_africa_strength_sustain_factor` and host native `surrender_progress` for qualitative Strength context.
Wrath context may use actor `gods_of_africa_war_floor`, `gods_of_africa_territory_floor`, `gods_of_africa_broken_treaty`, `gods_of_africa_defiant`, `gods_of_africa_recent_extreme_punishment`, `gods_of_africa_unresolved_treaty_break` and existing unresolved conduct flags where their owning UI contract calls for them.
This helper does not create a floor/cause rollout, numeric relationship display or copied hidden component ledger.

```txt
# Existing country-scope Strength producer, after the raw global assignment:
gods_of_africa_observe_public_strength = yes

# Existing participant floor owner, after its committed raw clamp:
gods_of_africa_observe_public_wrath_commit = yes

# Pure UI actor-scope visibility requirement:
gods_of_africa_public_wrath_is_visible = yes
```

Getter localisation, causes, threshold text, category wiring, icons and native GUI presentation belong to the parent/UI worker.
This data package adds no assets and requires no new icon identifiers.

## Evidence and limitations

Installed reference: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `round_variable` lines 6486 through 6495, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Offline reference: `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, round row 573, variable types 435 through 443 and scoping 444 through 480, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Installed `check_variable` reference: `documentation\triggers_documentation.md` lines 2110 through 2135, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
Vanilla command precedent: `common\scripted_effects\BUL_scripted_effects.txt` lines 1604 through 1618 rounds destination variables.
Repository floor precedent: `common\scripted_effects\chaosx_dynamic_effects.txt` lines 678 through 684 rounds an availability copy and subtracts one if rounding exceeds the unrounded value.
The companion dynamic-effect documentation describes that protected-floor behavior at lines 266 through 282.

`.tools\validation\test_012_gods_public_values.js` executes the production data helpers, pure predicate, raw Wrath transaction/floor bodies and actual Strength smoothing/commit tail under bounded explicit fixtures.
It does not execute HOI4, simulate native fixed-point quantization or certify UI rendering, save persistence, material transfers or whole event lifecycle.
All such source-model claims are `SourceNoNativeProof`.
The parent handoff records tool artifacts, current validation results, route limitations and exact edited call sites.

Future changes should keep the existing producer-bound observation contract and the two public values.
Any new raw metric producer must observe once after its final committed value and update its cleanup owner and focused test.
