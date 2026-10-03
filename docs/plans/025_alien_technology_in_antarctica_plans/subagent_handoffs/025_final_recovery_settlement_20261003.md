# Event 025 final-recovery settlement repair, 2026-10-03

Disposition: implemented within the user-authorized Event 025 rework.
Acceptance basis: the user requires the first valid final recovery, deterministic same-day tie resolution, invalid-participant cleanup, one duplicate-safe owner-API reward, and reports that do not repeat grants.
The Event 025 acceptance contract is docs/specs/025_alien_technology_in_antarctica_specs/specs/014_acceptance_criteria.md, sections 3, 7, 8, 20 and scenario 9/19.

## Changed behavior

Each valid final mission submits a durable receipt containing its day, survey evidence, readiness, outpost security, exposure, and final-readiness date.
The final tie-breaker remains the participant's stable entry order.
Later changes to expedition values cannot rewrite that successful recovery's evidence.

The resolver reselects from valid same-day receipts in the stored participant registry.
A country that is no longer present, capitulates, becomes a subject, withdraws, or loses its participant marker cannot receive the main reward.
The next valid same-day finalist is selected in the existing deterministic order.
If no valid receipt remains, the race closes without a main reward and preserves verified losing evidence.

Every same-day submitting country queues a resolver callback.
A surviving participant pulse can also resolve an overdue window if the first submitter's scheduled event disappears with that country.
No recurring world-country iterator is introduced.

Winner and loser settlements apply at resolution while the chosen scopes are valid.
The persistent winner ID is stored before the Event 016 external owner API is called.
The winner news is dispatched once from this guarded resolution.
Winner and loser report options only acknowledge their report and queue the analysis notice.

## Owned files

- common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt
- events/025_alien_technology_in_antarctica.txt
- .tools/test_event025_final_recovery.py
- this handoff

The Event 025 default-enabled entry was removed from common/scripted_triggers/chaosx_settings_triggers.txt to honor acceptance section 1 until the complete rework passes review.
That file also contains other agents' changes; only the Event 025 removal belongs to this repair.

## Preserved baseline

The pre-edit source copies are in docs/plans/025_alien_technology_in_antarctica_plans/evidence/20261003_settlement_baseline/.
The runtime source copy SHA-256 is C2E54882ECAB1E5BDB147E32C3C404A86D4A386BC46BEDC98729A69BAE165E08.
The event source copy SHA-256 is 92BF463D734C634AFECCAE58DE516F8DCAF2FFC8C765292ADE7244C9A7866EE0.

## Source and test evidence

Installed effects_documentation.md lines 4296–4311 documents for_each_scope_loop.
Its reference revision is 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.
The corresponding offline Scopes wiki array-scopes section is lines 737–810, revision 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49.
Both were read.

The command python .tools/test_event025_final_recovery.py -v passed nine tests.
The tests execute the current recovery helper bodies through a limited Clausewitz interpreter and fail on unsupported effects or triggers in those bodies.
They cover all six tie-breakers, priority precedence, 120 five-country registry permutations, five invalidation kinds, later-day exclusion, changed post-submission values, same-day waiting, repeat callbacks, and no-valid-finalist closure.
Report acknowledgement is also checked to contain no grant or news effect.

The external owner API and mission scheduling are outside this test interpreter.
Those remain subject to the independent probability, technology, event and live-game evidence gates.
No AI weight, random-list weight, MTTH parameter, or balance target was changed by this repair.

## Supplied live evidence and remaining work

The supplied Cycle 1 log is docs/testing/live_qa/20261003_full_playtest/logs/cycle1/error.log.
A case-insensitive scan for 025, nr25, Antarctic, alien_recovery and external_alien found no matching error lines.
The log has errors from other event and shared source files and is not clean-build proof.
The agent did not launch HOI4.

The current targeted GUI inspect retry timed out after 600 seconds.
Earlier 180-second GUI/technology timeouts remain prior-attempt evidence.
The board render gate is still open.

The complete Event 025 goal remains incomplete.
Known further work includes real Evolution V material transfer/destruction, pulses for all valid material holders, phase-mission timing, full GUI/reference evidence, exact reward arbitration audits, all achievement behavior tests, catalog alignment, and independent completion review.
No remaining route has been removed or accepted as a simplification by this repair.
