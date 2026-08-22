# Event 016 D’Rhondan enclave precedence resolution

Date: 2026-08-22

Owner: parent implementation agent

## Accepted decision

The user approved the full-coverage interpretation of the formerly contradictory opening-force rules. The ordinary DHR force remains `max(5, min(15, marked_states + floor(arrivals / 2)))`, but a formation with more than fifteen viable disconnected landing components may exceed that cap only far enough to place one cohort in every component.

## Runtime change

`common/scripted_effects/016_dhrondan_country_effects.txt` retains the existing state-neighbor flood fill and component-first deployment order. The component loop no longer stops when the ordinary reserve reaches zero. For each still-uncovered component after exhaustion, `dhrondan_grant_initial_enclave_floor_store` adds exactly one cohort’s 2,000 laser weapons, increments the persistent `dhrondan_initial_enclave_floor_extensions` receipt, and lets the shared `alien_infantry_spawn_landing_cohort` API debit that reserve during materialization.

The supplemental grant is reachable only inside the one-time sovereignty bootstrap and only while an uncovered disconnected component exists. It is not added to the ordinary force formula, is not available to the later capital-concentration loop, and cannot repeat after `dhrondan_initial_force_consumed` is set.

## Conservation scenarios

- Fifteen or fewer components: no supplemental receipt or equipment is created, and the ordinary formula is unchanged.
- More than fifteen components: every component receives one cohort; each excess cohort creates and consumes exactly one additional 2,000-weapon reserve.
- Failed materialization: the shared API refunds the attempted reserve. The component pass continues with the remaining reserve rather than issuing a second grant for the same debit.
- Later uprising or DHR re-release: global opening-force receipts prevent any ordinary or supplemental opening grant from repeating.

## Documentation alignment

The binding alien/D’Rhonda addendum, public DHR runtime documentation, and acceptance-scenario checklist now describe the ordinary cap and the narrowly scoped enclave floor separately. Earlier audit handoffs remain dated evidence of the conflict before the user’s decision and are superseded on this point by this handoff.

## MCP evidence

Fresh `hoi4.event_inspect` tracing from `chaosx.nr16.47`, with downstream helper expansion, returned `EVENT_INSPECTED_PARTIAL`, revision `2af1fa63424ef325ab938b49e0183b19d58d881a678db801d72f40e94ec2701c`, graph hash `977ee75194a46474e495ea0124f57640b1d816db52be57ed68bb80806a531858`, no blockers, and zero blocking diagnostics. The trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c63efe7eef80b30c405ce4817f858b1c479cd05de224a8a2c041797134722e60/adc73250e37ac5b8875f29d698a77af500d653b0cf8ffcb75c342f837ec78c1d/event-trace-2af1fa63424e.json`.

The matching state render returned `EVENT_RENDERED_PARTIAL`, no blockers, and zero blocking diagnostics. Its PNG SHA-256 is `045AE1985590C6BCC212CF3031E08745E0CF9098917DA809D52BBBF9DCC00BE1`. The adapter deferred workspace-wide helper and lifecycle projections, so this evidence is structural and does not claim dynamic engine execution.

## Remaining acceptance boundary

The source transaction and its documentation are resolved. User-owned live acceptance remains required for actual multi-enclave state transfer, component selection, equipment conservation, and unit placement in the game engine.
