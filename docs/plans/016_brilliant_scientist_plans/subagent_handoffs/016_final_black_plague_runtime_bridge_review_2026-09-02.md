# Event 016 Black Plague runtime bridge review — 2026-09-02

## Scope and disposition

This is a bounded, read-only source audit of the Event 016 Black Plague decision-led release before the natural Event 020 root has run. It covers the Event 016 preparation and dispatch chain, the ordinary biological lifecycle bridge, the shared Event 020 exposure/runtime helpers, the native weaponization precedent, and the documented weaponized-return contract. No gameplay source was changed by this audit.

The source result is a confirmed P1 runtime-activation gap: `brilliant_scientist_dispatch_black_plague_release` applies the shared Black Plague exposure, but no reachable Event 016 path initializes the Event 020 runtime, nominates a scheduler anchor, or schedules `chaosx.nr20.900` when this is the first Black Plague release. A completed native Black Plague weaponization project covers initialization but not the scheduler anchor, so that route still needs the bounded scheduler part of the bridge if Event 016 is allowed to release before the natural root.

The existing Event 020 scheduler receipt also contains a confirmed elapsed-time unit defect that becomes directly consumed by this bridge: `black_plague_schedule_next_pulse` adds pulse days to `global.date`, while `.900` accepts only when `global.date` reaches that mixed-unit receipt. The prior remaining-timer handoff already recorded the analogous shared-timer issue; this handoff records that the scheduler path is live for Event 016 once the missing bridge is supplied, not as a new unrelated timer family.

## Exact Event 016 call chain

1. The battlefield and covert decisions start a timed native decision through `complete_effect` and resolve it through `remove_effect` (`common/decisions/016_brilliant_scientist_biological_operations.txt:156-162` and `185-191`). The decisions expose no Event 020 activation effect.

2. `brilliant_scientist_begin_biological_deployment` validates the route, the selected target, and the shared decision availability, then creates the pending receipt and debits the command power, any portal transport, and the selected native payload (`common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt:173-217`). Its route and target gates are `brilliant_scientist_biological_battlefield_deployment_is_available` and `brilliant_scientist_biological_covert_deployment_is_available` (`common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt:251-275`). Neither helper checks `black_plague_system_started`, `black_plague_system_active`, or a scheduler anchor, which is correct for preparation but leaves activation to the completion path.

3. `brilliant_scientist_apply_selected_biological_release` dispatches the selected agent and chooses `brilliant_scientist_dispatch_black_plague_release` for the Black Plague selector (`common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt:386-396`). The caller is reached from the success branch and the accident branch of `brilliant_scientist_resolve_biological_deployment` (`:415-468`), so the bridge must remain safe for both release outcomes.

4. `brilliant_scientist_dispatch_black_plague_release` first invokes `brilliant_scientist_dispatch_standard_biological_release` and proceeds only when its ordinary lifecycle proof is supplied (`common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt:367-370`). The standard helper maps the Black Plague selector to ordinary `bio_seed_agent = plague`, supplies actor/victim/payload/use proof, and calls `bio_lifecycle_dispatch_seed` in the selected state (`:300-344`). The ordinary dispatcher validates the seed, writes the ordinary agent record, schedules ordinary incubation, and returns `bio_seed_dispatch_status` (`common/scripted_effects/biological_lifecycle_effects.txt:806-895`); it has no Event 020 runtime initialization or Black Plague scheduler call.

5. After the ordinary proof, the Black Plague helper sets weaponized exposure inputs and calls `black_plague_apply_exposure` in the selected state (`common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt:371-382`). The helper does not call `black_plague_initialize_runtime`, save `black_plague_scheduler_anchor_state`, set `black_plague_scheduler_anchor`, or call `black_plague_schedule_next_pulse`.

6. The Event 016 country activity predicate only checks existence, non-capitulation, and `NOT = { has_global_flag = world_end }` (`common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt:117-121`). The Black Plague unlock accepts a completed weaponization flag, an explicit authorization receipt, or Kruger’s personal authorization flag (`:32-40`). Therefore the explicit authorization branch can be visible without the native project output that initializes Event 020.

## Exact Event 020 behavior proving the gap

`black_plague_apply_exposure` starts with a temporary result of zero and changes it to one only inside `black_plague_state_can_receive_exposure`; it then updates state values, phase, provenance, modifiers, and registration (`common/scripted_effects/020_black_plague_effects.txt:1039-1068` and `1176-1193`). `black_plague_state_can_receive_exposure` checks state geography, population, and human/Rat control only (`common/scripted_triggers/020_black_plague_triggers.txt:66-75`). It does not initialize global runtime state or schedule a pulse.

`black_plague_register_current_state` ensures local state values and adds the state, owner, and controller to global arrays and response boards, then records the runtime generation (`common/scripted_effects/020_black_plague_effects.txt:343-433`). It is a registry operation, not runtime initialization. In a first-release path with no Event 020 initialization, the source has no call that establishes the global generation, counters, cleared arrays, active flag, or scheduler ticket before this registration.

`black_plague_initialize_runtime` is the actual one-time runtime bootstrap (`common/scripted_effects/020_black_plague_effects.txt:216-318`). It sets `black_plague_system_started` and `black_plague_system_active`, initializes the generation and counters, clears global registries and runtime targets, and performs its bounded one-time `every_state` population and transport pass. Nothing in Event 016 calls it.

`black_plague_schedule_next_pulse` is the actual state-owned scheduler entry (`common/scripted_effects/020_black_plague_effects.txt:1703-1717`). It requires `black_plague_system_active`, no `black_plague_pulses_suppressed`, and `black_plague_scheduler_anchor`; it increments the global scheduler ticket, writes generation and due metadata, and schedules `state_event = { id = chaosx.nr20.900 ... }`. The `.900` event calls `black_plague_run_scheduled_callback` (`events/020_black_death.txt:27-36`), whose guard requires the anchor, active runtime, matching generation and ticket, and a due receipt before running the weekly pulse and scheduling the next one (`common/scripted_effects/020_black_plague_effects.txt:1795-1823`). Event 016 currently reaches none of these scheduler prerequisites.

The natural root is not a safe substitute. `black_plague_start_natural_outbreak` selects a weighted natural origin, calls initialization, saves origin and scheduler targets, sets the anchor, initializes the origin state, seeds a threatened ring, schedules the pulse, sets the natural-outbreak flag, and emits the recognition report (`common/scripted_effects/020_black_plague_effects.txt:1858-1907`). Calling the public root would invent a natural origin and report chain for a weaponized Event 016 release, rather than only activating the shared state machine.

## Native precedent and documented intent

The native Black Plague project output calls `black_plague_weaponization_initialize_country` (`common/scripted_effects/020_black_plague_weaponization_effects.txt:178-203`), and that country helper calls `black_plague_initialize_runtime` when the runtime has not started (`:10-14`). This proves why a completed project normally has active Event 020 globals before its delivery path. The native `black_plague_weaponization_deliver_to_state` helper then debits its native package and calls only `black_plague_apply_exposure` (`:290-325`); it assumes the project bootstrap and does not itself schedule the runtime.

The ordinary strategic biological raid precedent follows the same separation: it prepares an explicit seed receipt and calls `bio_lifecycle_dispatch_seed` (`common/scripted_effects/biological_raid_effects.txt:438-480`). It does not bootstrap Event 020. This is evidence against assuming that the ordinary plague dispatch nested inside Event 016 implicitly starts the Black Plague scheduler.

Event 016’s biological system documentation explicitly requires Black Plague to use the ordinary plague lifecycle plus `black_plague_apply_exposure`, and explicitly forbids using the Event 020 public delivery effect so the same payload cannot be debited twice (`docs/events/016_brilliant_scientist/systems/biological_operations.md:45-56`). The Event 020 specification explicitly allows a weaponized return after natural eradication through a completed weaponization project and says the same state machine, mapmode, decisions, and cure protections apply (`docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_1_core_crisis.md:282-288`). These documents support a narrow shared-runtime bridge around the existing exposure call, not a second delivery transaction or a call to the natural root.

## Smallest bounded remediation recommendation

The owner should add the bridge at the successful Black Plague dispatch boundary in `brilliant_scientist_dispatch_black_plague_release`, without changing Event 016 payload accounting, the ordinary seed dispatch, outcome weights, or the Event 020 public delivery effect.

1. Keep the current ordinary dispatch proof as the first gate.

2. Before `black_plague_apply_exposure`, call the existing idempotent `black_plague_initialize_runtime` only when the runtime is not already started. This must be guarded by the existing valid actor/target and nonterminal context so a malformed direct call cannot cause the bootstrap to clear terminal flags or runtime targets. The helper’s one-time `every_state` pass is an initialization transaction, not a new periodic iteration.

3. Apply the existing weaponized exposure in the target state exactly once. The bridge must only continue to scheduler setup after the shared exposure is accepted. The current Event 020 helper stores `black_plague_exposure_result` as a temporary inside the state call (`020_black_plague_effects.txt:1040` and `1068`) and Event 016 does not copy or test that result after the call (`016_brilliant_scientist_biological_operations_effects.txt:379-382`). This is an acceptance-boundary limitation: ordinary dispatch proof is not, by itself, a stable exported Black Plague exposure receipt. The existing Event 016 target gates overlap the shared geography/population gates, so this review does not elevate a separate shared-exposure rejection defect without runtime evidence, but a bridge must not manufacture success from a rejected exposure.

4. If no live scheduler anchor is already present, save the accepted target as `black_plague_scheduler_anchor_state`, set `black_plague_scheduler_anchor` on that state, and call `black_plague_schedule_next_pulse` once. Reuse an existing anchor and outstanding scheduler receipt when one exists. Calling the scheduler unconditionally would increment the ticket and replace the due receipt, invalidating an already scheduled `.900`; the source has no separate Event 016 guard that prevents this duplicate scheduling. The SCN-012 helper demonstrates the existing save-target, state-flag, and scheduler sequence (`common/scripted_effects/020_black_plague_scenario_effects.txt:669-710`).

5. Do not set `black_plague_natural_outbreak_started`, origin targets, origin day, or natural recognition/report flags. Do not call `black_plague_start_natural_outbreak` or `black_plague_weaponization_deliver_to_state`.

## Scheduler due-unit finding

The Event 020 scheduler writes `black_plague_scheduler_due_day = global.date`, adds `black_plague_timing.pulse_days`, and separately schedules `.900` with the same number of days (`common/scripted_effects/020_black_plague_effects.txt:1703-1717`). The callback later compares `global.date` against that receipt (`:1795-1817`). Vanilla’s dynamic-variable documentation distinguishes `global.date` as a date value from `global.num_days` as the current total-day counter (`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md:972-998`). The smallest repair is to store and compare the due receipt on `global.num_days` consistently, optionally renaming the local variable to `black_plague_scheduler_due_num_days`; the native `state_event ... days = black_plague_scheduler_delay_days` must remain unchanged.

This is a live scheduler defect for the proposed Event 016 bridge and is also reached by the existing natural root because that root calls the same scheduler. It is cross-referenced here only to answer whether the bridge would consume a broken or valid timer; the broader remaining-timer handoff already records the analogous shared lifecycle arithmetic. The current devastation helper is already on `global.num_days` (`common/scripted_effects/020_black_plague_effects.txt:513-525`) and is not a new finding here.

## Edge-case disposition

| Situation | Source result | Required bridge behavior |
| --- | --- | --- |
| Explicit Event 016 authorization before any Event 020 project or natural root | The unlock trigger permits the path, while no Event 016 caller initializes Event 020. Exposure can write local state/registries without an active runtime or `.900` schedule. | Initialize once before exposure, then create one accepted-target anchor and schedule one pulse. |
| Completed native Black Plague weaponization project before Event 016 release | Project output already calls the runtime bootstrap, but it does not set an anchor or call the scheduler. | Preserve the active initialized runtime and add only one anchor/scheduler receipt if none is live. |
| Natural Event 020 runtime already active | Natural root owns an origin, anchor, ticket, and `.900` chain. | Register the weaponized target and reuse the existing scheduler; do not reset the ticket or due receipt. |
| Natural eradication followed by weaponized return | The Event 020 specification explicitly allows reintroduction after eradication. The eradication report sets `black_plague_system_eradicated` (`common/scripted_effects/020_black_plague_effects.txt:861-878`) and does not establish a separate Event 016 bridge. | Do not add a blanket eradication lock or call the natural root. Preserve history and reuse the active scheduler if present; if a valid active runtime has no anchor, the same narrow accepted-target anchor rule is needed. A malformed save with `system_eradicated` but no `system_started` is outside the documented new activation path. |
| Terminal takeover or world end | Event 016 country activity rejects `world_end`, but the shared state exposure trigger itself does not check terminal/global runtime flags (`016 triggers:117-121`; `020 triggers:66-75`). Runtime initialization would clear terminal fields when `system_started` is absent (`020 effects:216-230`). | Guard the bridge before initialization and exposure against the existing terminal/world-end context. Do not use this bridge to reopen a terminal run. |
| SCN-012 bootstrap or another pulse-suppressed setup | The scenario owns anchor selection and scheduling and calls the scheduler after setup (`common/scripted_effects/020_black_plague_scenario_effects.txt:669-710`). | Do not clear `black_plague_pulses_suppressed`, replace its anchor, or schedule a duplicate `.900`; honor the existing scheduler guard and let the scenario helper own setup. |

## Remaining evidence limits

This review is source-only. I did not launch Hearts of Iron IV, request logs, or claim live in-game acceptance. No Event 020 MCP runtime artifact was used for this bounded call-graph question. The handoff therefore proves the missing source call path and the scheduler’s source consumption, but it does not prove engine ordering, the runtime persistence of the temporary `black_plague_exposure_result` across the nested state scope, or the exact behavior of an already queued state event after a target is transferred or destroyed.

The Event 016 documentation states that the ordinary dispatcher must accept before successful delivery history and Directorate Exposure are recorded (`docs/events/016_brilliant_scientist/systems/biological_operations.md:45-56`), and the current caller checks that ordinary proof. This audit does not certify every possible shared Event 020 exposure rejection because the Black Plague helper’s acceptance result is not promoted to a stable Event 016 receipt. That is an implementation-boundary note for the owner’s bridge review, not evidence to replace the required runtime validation.

## Audited source hashes

These hashes were captured after the read-only review and identify the source examined:

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt` | `DED6A1DBF25AA8ADB7C8ABA20905FB349ED4CAC4A7EB45EFAE4E12F4E511450D` |
| `common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt` | `02AFA9BDB79AAFA80D1AE7430D54E5CA576DC7B8053940AC4AE3AE1DA2E7268D` |
| `common/decisions/016_brilliant_scientist_biological_operations.txt` | `A1ED2F6D7B6E1E6296E1E415C0ECCE4E925A912C75897D27F4A182AD715B920C` |
| `common/scripted_effects/020_black_plague_effects.txt` | `DFC020B21EBFE726892B74A8B05E43860A9252E4977644B62507EBAF1205BE40` |
| `common/scripted_triggers/020_black_plague_triggers.txt` | `4A891F1D6DC89B5F8584DC3DED960733EFA371829EB829BDE9A9C78B048BC68F` |
| `common/scripted_effects/020_black_plague_weaponization_effects.txt` | `1FA96F4E5BB17D6DBBEE987916830100AA9FA2EBA28F492E313F76C462C5BDB4` |
| `common/scripted_effects/biological_lifecycle_effects.txt` | `1B5DFF3DC9E00319C90C73145BECBF6F92F57A7C85E72B7404234A205A9CC687` |
| `common/scripted_effects/biological_raid_effects.txt` | `A9357AD217A21973AA2D43046894ACFD477204C705B7BEF5A8885DD8AE735C40` |
| `events/020_black_death.txt` | `A38A52F3C3074C997ECC14F392F781E59DBC168FD849BB386B6FCE1E8BD0BFD2` |
| `docs/events/016_brilliant_scientist/systems/biological_operations.md` | `84F3323BDD96CAC07FA0D754520DD949F6CCDF1D0228D3EA555ED425FF168FFF` |
| `docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_1_core_crisis.md` | `6F94B2282FE0B552182F7D13750A04ED1159F3948094F3CC1759D891B79FEA2E` |

No gameplay files were edited, staged, or committed for this handoff.
