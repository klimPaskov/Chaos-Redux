# Event033 F7 report receipt architecture

Disposition: bounded read-only findings and conditional owner proposal.
The parent implements and accepts the design.
Only this handoff and its compact JSON receipt were written.
F6 source evidence, runners, gameplay and policies were not edited.

Audit began on committed E5 `e5c34d8bd73971609e26b7aef2d4a01cdd4f3f795c2856d83189dfcd546f5def`.
The owner added three caller declarations during the audit, producing current runtime `3eb102bf6168362eadd58188d45791cd81f9713dc379d9e08da325334e65bd48`.
References below use current3EB line numbers unless marked E5.

## 1. Return ABI: original hole resolved, delivery unproved

The sole positive-loss caller originally invoked `prepare_severe_impact_report` without reserving `acid_rain_impact_episode_key`, `acid_rain_impact_evacuation_status` or `acid_rain_impact_end_day`.
They were created only inside the STATE helper, then consumed through STATE→CONTROLLER→sender/fire.
Under conservative helper frames, cold caller storage disappears at helper return.
Current `effects:3324-3326` reserves all three immediately before the unchanged preparer at3327, inside the existing positive severe/superstorm guard.
The following controller consumer is3328-3331.
The owner's `report_return_storage_owner_2026_10_08.md` records26 actual-preparer scalar/frame cases and exact three-line reversal.
That repairs the source storage hole, not controller delivery, ledger or display semantics.

Forecast inputs have no equivalent returned-storage hole: creators4408-4421 and5312-5330 set population in the STATE producer frame and kind/lead in CONTROLLER before calling their helpers.
`open_forecast_report:3430` and `add_state_to_forecast_report:3460` write saved country fields.
The date converter in the impact fire helper also has caller-initialized offset/days storage.

## 2. Small fresh-generation ledger proposal

Key receipts by actual recipient country, explicit report generation, class and exact episode, not a maximum.
For severe impacts, use33 indexed country entries including reserved0, storing the first accepted pulse witness at severe ID1..32.
For superstorms, use6 indexed rows including reserved0, storing reported episode serial and pulse witness per slot1..5.
Keep forecast and impact channels separate.
Reset through known owner formation/initialization, and require a matching generation header on every access.
The current country initializer merely clears four legacy IDs at805-808 and sets registered, with no report-generation header.

Before consuming any fresh receipt, prove the exact source state and current recipient/controller, current frozen/consequence/forecast generation, admitted class, bounded source ID and current pulse, plus positive returned applied loss matching the stored population delta.
A population-contract fault or mismatched source is not a reportable physical proof.
Freeze the fact packet before marking dispatch requested.
Use the current country scope, not the unchanged host ROOT, as recipient identity.
A receipt denotes requested publication, not native acknowledgment.
No overflow cap, pruning of unknown history or silent report drop is proposed.
Any new iterator needs its own immediately reset private break binding.

## 3. Why32 severe rows and5 slot rows are different

Constants29/33 bound severe records32 and simultaneous superstorm slots5.
Severe allocation4359-4365 increments the generation count and appends a never-reused ID, with global start/end/death/damage rows retained.
Superstorm allocation5240-5267 selects a retired slot, increments an independent total serial and stamps `global.acid_rain_superstorm_episode_entries^slot`.
States store slot, forecast generation and serial at5297-5300.
Retirement clears target membership and retires the slot, not the lifetime serial.

Current layer gates `triggers:97-120` check frozen state, forecast generation, target flag, slot-active state and start time.
They do not compare the state's superstorm forecast serial with the global slot serial.
The preparer/sender add no independent generation or slot/serial check.
Thus fixed-slot receipts are safe only if report validation adds exact state-serial/global-slot equality and excludes stale packets after reuse.
They also assume synchronous physical-packet publication with no valid deferred report surviving reuse and exact non-repeating serial values.
Five slots does not prove a lifetime serial bound.
Those assumptions remain unresolved rather than accepted migration/native safety.

## 4. Maximum-only migration cannot reconstruct delivery

Current sender3382-3409 still uses `less_than`.
Actual parsed-source sender replay requests only episode3 for sequence3,2,3, in both classes.
Sequence2,3 requests both.
Legacy maximum3 cannot distinguish prior reported sets{3} and{2,3}.
It establishes only old country/class dispatch bookkeeping, not every earlier receipt or native display.
Country totals, state impact/history flags and the positive-loss ring are physical records, not country/episode report delivery history.

Do not fill every ID below the maximum, empty the ledger and silently resend, or suppress the ambiguous range.
The maximum can remain explicit legacy metadata, but cannot become fabricated fresh physical receipt proof.
An active-generation upgrade needs a parent-accepted ambiguity policy.
The clean-generation bounded ledger can be designed without pretending that historical uncertainty is solved.

## 5. Physical facts, ordering and shared display scratch

At `apply_state_pulse:3210-3334`, exact loss and before/after observations precede positive-loss death/prevention accounting and report publication.
The worker calls real damage afterward at4706-4707/4723-4724 and5458-5459/5476-5477.
Current104 therefore precedes this packet's measured building damage.
Damage pressure, tiers and receipt count alone are not actual damage.
Measured `acid_rain_damage_points_actual` is local to the damage helper, global totals are cumulative, and severe episode damage rows sum all recipients.
No country/episode damage packet is currently published.

Applied loss, observed delta, pulse identity and `max(unprotected requested-applied,0)` prevention estimate are available in the positive transaction.
Shelter/medical/action/evacuation/CBRN inputs and final protection are computed inside `calculate_mortality_profile:2996-3100`.
They need explicit returned/saved fact storage if reporting outside that helper.
Their labels or live tiers do not establish independently attributable lives saved.

Fire3412-3420 stores only kind, evacuation and remaining days.
Loc104 reads live country cumulative deaths/prevention, not reported-episode snapshots.
Two overlapping episodes can request104 twice for the same country in one worker transaction, overwriting those same country fields.
The carried regular `acid_rain_report_state` target identifies a scope, not frozen country totals, protection values or state facts.
The forecast helper likewise dispatches103 before all subsequent state additions finish.
Native description evaluation timing and per-event scalar snapshot behavior are not proved.
Bind stored loss/damage/prevention/protection facts to the exact generation/class/episode/pulse before exposing them, but the native publication/payload contract must be resolved by the parent.
No speculative queue or popup-drop policy is offered.

Next safe owner step: accept the fresh receipt/source-proof shape, decide explicit legacy handling and verify native fact binding before changing deduplication or publishing post-damage episode facts.
Do not alter mortality, caps, timing, weight, cost, AI, GUI or achievement policy through this repair.

Evidence: current sender lookup is complete/unshadowed at index revision `ed915a0880f765a2f48dcd59dcbf9a90b648f2baddebbb8d1c336743e0304c35`, but indexed references are incomplete, so callers were read locally.
Live installed references read: is_in_array5672-5685, country_event2943-2967.
Offline Data structures1147 and regular targets303-328 were read.
Exact paths/revisions, source hashes and bounded model limits are in the JSON.
No native delivery/physics/finance/MP/GUI acceptance is claimed.
Skills used: chaos-redux-events, chaos-redux-subagents and loop-break-isolation.
