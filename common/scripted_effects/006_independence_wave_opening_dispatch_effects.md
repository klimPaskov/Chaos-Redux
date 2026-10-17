# Event 006 report recipient opening queue

## Purpose and helper map

The helpers capture a committed Event 006 release cohort on the COUNTRY scope that receives chaosx.nr6.2, then dispatch country openings from that recipient's .2 option.
A country event option does not receive an event-instance plan ID.
The helpers therefore dispatch only if exactly one report option is outstanding for that recipient.
Overlapping reports fail closed until all their options have been acknowledged.
No helper grants packages, transfers states, mutates Event 005, scans all countries, or reads the current plan from .2.

| Helper | COUNTRY scope input | Output and side effects | Parent call site |
| --- | --- | --- | --- |
| independence_wave_prepare_committed_country_opening_queue | Exact .2 recipient and committed Event 006 selected rows | Increments the recipient callback count and freezes one fully validated report record and actor slice when sole | Each committed branch of hidden chaosx.nr6.1 immediately before firing .2 |
| independence_wave_dispatch_committed_country_opening_queue | Same .2 recipient and its local frozen record | Consumes one callback, validates every actor, sets actor receipts, schedules .42 after the centralized post-report delay, then clears frozen storage | Sole chaosx.nr6.2 option |
| independence_wave_clear_committed_country_opening_queue | The .2 recipient | Removes local report and actor arrays only | Called internally at capture and consumption |
| independence_wave_resolve_country_opening_civilian_administration | A current .42/.41 generation receipt | Applies the civilian posture through the shared five-value, host, and network helpers, then resolves the receipt | Human `.41` civilian option or deterministic AI route |
| independence_wave_resolve_country_opening_frontier_security | A current .42/.41 generation receipt | Applies force-tier and live-security scaled defense, host deterrence, and network/legitimacy/capacity tradeoffs, then resolves the receipt | Human `.41` security option or deterministic AI route |
| independence_wave_reset_host_deltas | COUNTRY scope | Sets all eight shared host-ledger deltas to zero before posture-specific inputs | Called by either posture only when its former host survives |

There are no parameters or default actors, plan IDs, or packages.
An absent, invalid, or overlapping report sends no opening.
Existing constants provide zero, increment, ten-country maximum, committed phase, and Event 006 owner checks.
The two authored one-day waits use `independence_wave_opening_timing` in `common/script_constants/006_independence_wave_opening_constants.txt`.
No AI weight or probability pool is introduced.

## Recipient record and admission

The recipient holds independence_wave_opening_report_callbacks_pending and three aligned report arrays: independence_wave_opening_report_plan_ids, independence_wave_opening_report_starts, and independence_wave_opening_report_counts.
For the sole admitted report, the record stores the exact committed plan ID, start index zero, and a count from one through ten.
The recipient also holds aligned independence_wave_opening_actor_countries, independence_wave_opening_actor_generations, and independence_wave_opening_actor_packages arrays.
The actor array contains country scope references.

Capture increments the unresolved callback count before any admission check, including for an invalid report.
Only a count of one can admit a record.
The shared plan must be committed, include Event 006, have a positive plan ID and matching presentation ID/count, and pass existing alignment predicates.
Each Event 006 selected index must point to an in-range shared row owned by Event 006 with the exact selected package.
The package must pass its runtime adapter and exact content-attestation triggers.

Each distinct actor must exist as an active, origin-committed and package-validated Event 006 country with completed package setup, positive generation, matching package, valid region, force profile and starting force level, selected archetype, a stored former-host pointer matching the frozen shared row, an owned and controlled anchor, host outcome, and all five country values.
The former host may have been eliminated after release.
Only when that country still exists does the gate require it to be distinct from the released actor.
Those values are Legitimacy, Recognition, Capacity, Security, and Instability.
The regular anchor event target remains within the capture effect chain.
The first pass writes only temporary country, generation, and package arrays.
The persistent record and actor arrays are written only after the whole cohort passes.
Capture writes no actor opening receipt.

## Dispatch, overlap, and cleanup

The .2 option receives its country scope without a plan-instance token.
For a sole outstanding callback, dispatch requires exactly one aligned report record, zero start, bounded actor count, and no matching recipient dispatched-plan receipt.
It reads only the recipient arrays and revalidates every distinct actor against the frozen generation and package, active Event 006 origin, content attestation, and retained opening fields.
Dispatch requires the stored former-host pointer but permits its country to be eliminated, applying the distinct-country comparison only when it still exists.
The entire cohort must pass before any actor is marked.

On success, the recipient stores independence_wave_opening_dispatched_plan_id.
Each actor receives independence_wave_opening_plan_id, independence_wave_opening_generation_id, independence_wave_opening_package_id, and independence_wave_opening_pending before chaosx.nr6.42 is scheduled in that actor's country scope one day later.
The hidden .42 compares those country-local receipts against the actor's current generation, package, state anchor, force profile, and force level.
AI actors resolve one deterministic posture from current war, live former-host threat, security value, force level, and security-oriented force profile; they use the same effects shown on the human .41 event.
Human actors receive chaosx.nr6.41 only after the acknowledged public .2 report.
The resolver owns removal of the actor pending flag and receipt cleanup after resolution, while retaining its resolved posture and report receipts until generation reset.

The civilian posture scales legitimacy, recognition, and capacity gains down for values already above their established bands, increases the security tradeoff during war, severe host threat, or a weak starting force, and applies stronger instability relief to strained ledgers.
It raises Event 006 network standing and moderates the surviving host's claims, hostility, obligations, domestic pressure, and reconquest fear while advancing border settlement.
The frontier-security posture scales its Security increase from the starting force level, current Security band, and force profile; it trades legitimacy, Capacity, and Event 006 network standing and raises Instability only during war or a severe living-host threat.
Against a surviving host it increases bilateral hostility and domestic pressure while reducing fear of reconquest.
Both choices use existing centralized delta constants and shared mutation helpers, grant no resources or territory, and create no weighted AI option pool.

After either posture resolves, IW-043 and IW-058 schedule their existing package-specific introductions one day later.
Package setup no longer fires those popups before the public wave report or the shared country-opening choice.
Each scheduled introduction carries the current package generation in a country-local receipt; its event trigger consumes only a matching generation, and package cleanup clears any pending receipt.
The dispatcher consumes one callback and clears recipient frozen arrays after the option, whether admission succeeds or fails.

If another .1 report is captured before the first .2 is answered, the callback count exceeds one and capture discards frozen storage.
Every overlapping .2 option then consumes one callback without dispatch.
Further reports during that interval remain quarantined.
Normal capture resumes when the count returns to zero.
This explicit fail-closed behavior avoids assuming popup ordering.
The parent-owned .2 is fired by .1 only for a committed positive-count report, has the centralized 13-day one-option timeout, and holds the global report-pending flag until its sole option dispatches or the timeout selects the first option.
Offline Event Modding documentation states that after `timeout_days` the first option is automatically selected; the option therefore retires the callback under normal timeout behavior.
If an unexpected engine failure prevents `.2` delivery or option execution, its callback count cannot retire and later openings for that recipient remain quarantined.

The helper leaves the shared liberation plan ID, country arrays, phase, Event 005 rows, and transaction receipts untouched.
The recipient dispatched-plan ID survives queue cleanup for idempotency.
A generation reset clears any unresolved actor pending flag, its three opening receipts, resolved posture flag, and both posture flags.
There are no global event targets or on actions.
At most one admitted report and ten actor entries are stored per recipient.
The callback count can grow while options remain unanswered, but that causes no actor iteration and cannot permit dispatch during overlap.

## Usage and migration

In each committed .1 branch, call capture in the exact country scope that receives .2:

    independence_wave_prepare_committed_country_opening_queue = yes
    country_event = { id = chaosx.nr6.2 }

In the sole .2 option:

    independence_wave_dispatch_committed_country_opening_queue = yes

The parent owns .41 and .42, localisation, actor generation cleanup, the shared effects, and final integration.

## Reference evidence and limits

- Installed C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af, add_to_array lines 2278–2292 and country_event lines 2943–2967.
- Installed C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29, exists lines 2708–2716, has_variable lines 5006–5014, conditional if lines 5166–5175, and scope_exists lines 7450–7472.
- Offline paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md, revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4, array arguments lines 1078–1144.
- Offline paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md, revision 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49, array scopes lines 737–796.
- Offline paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md, revision 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d, lines 5–36, identifies the event recipient scope and transferred regular event targets.
- Offline paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md, revision 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d, line 186, states that timeout_days automatically selects the first event option.
- Offline paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md, revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4, line 431 and following variable section, confirms `[?variable.GetName]` promotion for stored database-object scope references.
- Installed C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md, revision 884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7, Script Constants lines 216–246; installed `common\script_constants\documentation.md`, revision e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c, schema and examples lines 1–43.
- Installed triggers documentation, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29, `is_ai` lines 5244–5252; installed effects documentation, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af, `country_event` delay lines 2949–2967.
- Vanilla `events/AAT_Denmark.txt`, revision ee22127359a8d21e78683d6901aaa76f64d0b46027d97d4d57bb6a04208958aa, lines 41 and 102, schedules a follow-up country event after an option using `days`.
- The connected HOI4 MCP exposes event inspection/render routes, but the required `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` routes are absent in this parent context. Offline wiki and installed-game sections were read directly; this is the documented reference-route gap.
- hoi4.event_inspect trace of chaosx.nr6.1 reported focused partial coverage at revision c667b1897a5180f60b8895da5d08653ca6a4387b25419e98251c72bdfa1545df, artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/434ba6d0d17ba821347e37d2e0ed7261c7ee3ee7cbf03d3a9164f73b289ef2c2/439b130841c2ea20fc16488fba237a1a2ca7bde2a36861e5112a78be39a4625e/event-trace-c667b1897a51.json.
- Unsupported analysis: the inspector does not prove popup option ordering or attach a scalar plan ID to .2, which is why overlap is quarantined.

