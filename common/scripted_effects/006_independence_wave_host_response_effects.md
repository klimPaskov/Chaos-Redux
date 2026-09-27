# Event 006 committed host response helpers

## Public interface

The host response queue is built once after the acknowledged public report and the final valid Event 006 country-opening choice.
The parent owns events chaosx.nr6.60 limited, .61 severe, .62 remnant, hidden .63 AI, option outcomes, completion counters, receipt cleanup, and release of the report reset barrier.
These helpers do not fire events, apply an option outcome, or create another plan queue.

| Identifier | Scope | Inputs | Output and side effects |
| --- | --- | --- | --- |
| independence_wave_host_response_build_queue_after_openings | COUNTRY, final opening callback | Active committed release arrays and retained report barrier | Publishes one pending receipt per distinct live state-losing Event 006 host; appends hosts to global.independence_wave_host_response_hosts; sets global.independence_wave_host_response_remaining_count |
| has_current_independence_wave_host_response_receipt | COUNTRY, former host | Host receipt, current committed plan, source host row, global host queue | True only for the same live host and active committed plan |
| independence_wave_host_response_resolve_ai_action | COUNTRY, former host | Valid receipt, current-wave primary-host rows, matching-generation bilateral ledgers, current host survival and war state | Writes the single normal variable independence_wave_host_response_ai_action to a validated action constant or none |

The public host receipt is independence_wave_host_response_plan_id, independence_wave_host_response_tier, independence_wave_host_response_event6_loss_count, independence_wave_host_response_pre_release_state_count, independence_wave_host_response_protected_state, independence_wave_host_response_original_capital, and the independence_wave_host_response_pending flag.
The internal independence_wave_host_response_host_row records the aligned source host index so the current-receipt trigger can prove the protected state, original capital, and denominator came from this host.
The committed plan ID is the receipt generation token; existing hosts have no Event 006 country-origin generation.
The private global independence_wave_host_response_last_built_plan_id is an idempotency receipt, not another queue.

The queue contains only global.independence_wave_host_response_hosts and global.independence_wave_host_response_remaining_count.
The parent decrements the remaining count when each host option completes, clears the six public host receipt variables, the private independence_wave_host_response_host_row, the pending flag, and independence_wave_host_response_ai_action, then clears the host array when the host phase finishes.
The builder does not change the shared liberation transaction, Event 005 arrays, or the parent-owned report flag.

## Exact committed release accounting

The builder requires a committed shared phase, Event 006 inclusion, the retained independence_wave_country_opening_report_pending barrier, an unused positive plan ID, aligned state, host, country, and Event 006 selection arrays, an empty host response queue, and no Join conversion for this plan ID.
It does not exclude triggerable_scenario mode, so SCN-008 remains eligible.
The state and host arrays must each contain fewer than 1,000 rows because the installed while-loop engine stops after 1,000 iterations.

Only rows owned by liberation_plan_owner.independence_wave contribute.
Each such row must have an anchor, compact, or extended liberation_plan_state_role; a distinct state; a live former host in global.liberation_plan_hosts; and an active, origin-committed Event 006 target in exactly one selected Event 006 country row.
The admitted distinct-state count must equal the Event 006-owned row count.
Duplicates, unsupported roles, missing scopes, or mismatched target rows fail the entire cohort before any host receipt is published.
The committed ledger defines what the release transferred, so later state ownership changes do not change the numerator.

For each host, the builder counts only its distinct admitted Event 006 state rows.
A host with no Event 006 loss receives no response even if Event 005 changed its map.
A state-losing host must be live, have a positive pre-release owned-state snapshot, lose no more states than that snapshot, retain matching protected-state and original-capital pointers, and have no existing response pending.
Failure for any state-losing host or a duplicate host scope prevents the entire queue from being published.
All state and host evidence is staged in temporary arrays first.

The remnant override takes priority when exactly one owned state remains and it is the protected state, or when the original capital is no longer owned and no more than two owned states remain.
Otherwise the tier is severe when 2 × Event6Loss >= preReleaseStates and limited below that boundary.
The integer multiplier and remnant maximum are defined in independence_wave_host_response_value.
Tier IDs are independence_wave_host_response_tier.limited, .severe, and .remnant.
No chance weights or timed crisis durations are added; event timing belongs to the parent.

## Deterministic AI action

The .63 event calls independence_wave_host_response_resolve_ai_action in the host's COUNTRY scope.
It starts with independence_wave_host_response_action.none and changes to exactly one of limited_negotiate, limited_pressure, limited_reclamation, severe_command, severe_relief, remnant_continuity, or remnant_regional_identity only if the current receipt is valid.
The parent maps the selected token to its corresponding independence_wave_host_response_apply_<action> effect and treats none as a closed route.

The resolver scans only the selected Event 006 country rows of the current committed plan whose primary host is this response host.
A bilateral host ledger row matches only when its actor is that current-wave country and its stored generation equals the actor's current Event 006 generation.
The host relation arrays must be aligned.
Missing, duplicate, or stale rows for a current-wave primary actor leave the action at none.
The resolver reads matching-row hostility and domestic pressure against the existing independence_wave_host_relation.conflict_gate, plus current host war state and survival.

For a host with matching primary-host ledgers, limited chooses reclamation during war, pressure at high hostility or domestic pressure, and negotiation otherwise.
Severe chooses command during war or high hostility or domestic pressure, and relief otherwise.
Remnant chooses regional identity at peace with low hostility and pressure, and continuity otherwise.

A secondary optional-state host can lose Event 006 states without a current-wave primary-host bilateral ledger.
That exact first-contact case uses its validated receipt tier to choose limited_negotiate, severe_relief, or remnant_continuity.
It never borrows a historical actor row and does not escalate because of an unrelated war.
A primary host with no matching current-wave ledger is invalid and does not use this fallback.

## Usage, lifecycle, and limits

    # Parent calls once when the opening completion counter reaches zero:
    independence_wave_host_response_build_queue_after_openings = yes

    # Parent iterates global.independence_wave_host_response_hosts and checks:
    # has_current_independence_wave_host_response_receipt = yes
    # Parent sends .60, .61, or .62 according to the host tier.

    # In hidden .63, in host scope:
    independence_wave_host_response_resolve_ai_action = yes

    # Parent applies the matching action effect, clears that host receipt,
    # decrements global.independence_wave_host_response_remaining_count,
    # and releases the report barrier after the final host response.

The parent must retain the committed release arrays and report barrier until every host option has resolved.
No helper here handles an event that never reaches an option; parent-owned recovery must retire its pending receipt and count.
The plan ID is monotonically allocated by the shared coordinator, and the last-built receipt prevents duplicate queue construction for that plan.
The host array remains ordered by the aligned shared host rows and can contain at most one entry for each state-losing former host.

## Reference evidence and unsupported analysis

- Offline paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md, revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4, array arguments lines 1078–1127.
- Installed C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af, multiply_temp_variable lines 5012–5018 and add_to_array lines 2278–2292.
- Installed C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29, check_variable lines 2110–2135 and has_war lines 5024–5032.
- Installed C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md, revision 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda, num_owned_states lines 670–672.
- hoi4.source_lookup located the active liberation_release_state_arrays_are_aligned trigger in mod:common/scripted_triggers/chaosx_liberation_release_triggers.txt lines 196–202, source revision a81fb6ea1ef59f48cdff1aafd3d67d663391f3e085e287357804525173893869.
- hoi4.event_inspect of chaosx.nr6.2 returned focused partial coverage, revision 5b30200461cb5aee186e33773bd8f73bfcccb09718f23f79934e155d841e5be0, artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/098fe2e6be913ed8dd92ccf6fe53faa4fb38bc0d0c93ea767af93f4dd24fa0bc/a2bd27788abb84a6878d6fb6a7419316bcdbac8dc128bab38cb30c54780e7872/event-trace-5b30200461cb.json.
- hoi4.map_inspect lookup-only reported 1,081 installed states at revision b056af877c4b53eba366a02d3bba9269f1ea4870cbfa83ce24594867d27d61c2; no fixed map geometry or state ID is assumed.
- hoi4.event_render of the .2 neighborhood returned focused partial coverage, revision 3e4bcb5817e1ddca1e2f8b7ef9160aa7a4fa85367168a3d031196e4d3d542b39, artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23754261fa23dd38bb272732b09624d549d558cb5d96714c57abc5ee376e28b5/82b20a5de4ec1affc5eb437d68f2f207a40cd6394998b47a4fdce94788d77132/event-neighborhood-3e4bcb5817e1.json.
- Unsupported analysis: the parent-owned .60-.63 event call sites and option cleanup are not yet wired, so the current event graph cannot prove host popup delivery or final barrier release.





