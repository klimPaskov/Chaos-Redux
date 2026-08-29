# Historical Profile Memory Reachability Handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-24.

Owner: `chaosx_scripted_system_architect`.

Scope: bounded historical-memory proof for `hist_soviet_1932_memory` and `hist_ireland_memory`.

## Result

The shared `famine_migration_profile_memory_proven` variable was removed from the two memory-profile selector and resolver branches because it had no producer and was ambiguous across profiles.

The existing sparse historical-profile anchor registration now calls `famine_migration_register_historical_memory_anchor_proof`, which writes durable state-scoped proof flags only for the eleven audited Soviet states and the Ireland state.

The registered-anchor processor replays that helper idempotently, so saves whose anchors were created before this fix receive the proof without resetting runtime state or scanning the map.

## Files and identifiers changed

| File | Identifiers | Change |
| --- | --- | --- |
| `common/scripted_effects/chaosx_famine_migration_effects.txt` | `famine_migration_register_historical_memory_anchor_proof`; `famine_migration_register_historical_profile_anchor_state`; `famine_migration_unregister_historical_profile_anchor_state`; `famine_migration_select_historical_profile_id`; `famine_migration_resolve_historical_profile_context`; `famine_migration_process_registered_historical_profile_anchor` | Add exact state-gated proof registration, replace the four dead shared-variable consumers, preserve proof through unregister/cleanup, and add sparse save backfill. |
| `common/scripted_triggers/chaosx_famine_migration_triggers.txt` | `famine_migration_soviet_1932_memory_anchor_proven`; `famine_migration_ireland_memory_anchor_proven` | Add fail-closed profile-specific triggers requiring the durable proof flag and exact audited state. |
| `common/scripted_effects/chaosx_dynamic_effects.md` | Historical-profile resolver and helper contracts | Document scope, flags, call sites, persistence, backfill, cleanup, and live-gate separation. |

No new numeric tuning was needed, so `common/script_constants/famine_migration_constants.txt` remains the source of the existing state-ID constants and no new constants were added.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `famine_migration_register_historical_memory_anchor_proof` | State | Current state scope and existing `famine_migration_profile_state_id` constants. | No public numeric output. | Idempotently sets `famine_migration_historical_memory_soviet_1932_proven` for states 192, 193, 202, 218, 221, 227, 233, 239, 583, 589, and 590; sets `famine_migration_historical_memory_ireland_proven` for state 113. It does not set food pressure, dates, owner/controller proof, ideology, casualties, deaths, displacement, or events. | `famine_migration_register_historical_profile_anchor_state`; `famine_migration_process_registered_historical_profile_anchor`. |
| `famine_migration_soviet_1932_memory_anchor_proven` | State trigger | Exact Soviet anchor state and durable state flag. | Boolean trigger result. | None. | Soviet selector and resolver branches. |
| `famine_migration_ireland_memory_anchor_proven` | State trigger | Exact Ireland state 113 and durable state flag. | Boolean trigger result. | None. | Ireland selector and resolver branches. |

The shared host-only `famine_migration_process_registered_runtime` remains the scheduler owner, and the memory helper runs only through the existing sparse anchor array.

## Historical profile producer census

The full fifteen-profile matrix and all bootstrap anchors were inspected before editing.

| Profile | Exact producer before patch | Producer after patch and live gates |
| --- | --- | --- |
| `hist_soviet_1932_memory` | Dead: selector and resolver required unassigned `famine_migration_profile_memory_proven`. | Eleven exact bootstrap anchors call the new helper; the profile still requires SOV owner/controller and positive live food pressure. |
| `hist_china_henan_1942` | Existing exact Henan anchor registration. | Unchanged; Henan, CHI/MAN owner or controller, 1942 window, and war or surface proof remain required. |
| `hist_china_policy_famine` | Existing exact Henan anchor registration. | Unchanged; Henan, CHI ownership/control, post-1936 date, resolved occupation profile, and positive food pressure remain required. |
| `hist_bengal_1943` | Existing exact East Bengal and West Bengal anchor registrations. | Unchanged; RAJ/ENG ownership or control, 1943 window, and war or positive food pressure remain required. |
| `hist_vietnam_1944` | Existing exact Tonkin and Cochinchina anchor registrations. | Unchanged; FRA/JAP ownership or control, 1944 window, and war or positive food pressure remain required. |
| `hist_java_1944` | Existing exact West and East Java anchor registrations. | Unchanged; HOL/JAP ownership or control, 1944 window, and war or positive food pressure remain required. |
| `hist_greece_1941` | Existing exact Greece, Peloponnese, and Aegean anchor registrations. | Unchanged; GRE/GER/ITA ownership or control, 1941 window, and war or positive food pressure remain required. |
| `hist_leningrad_siege` | Existing exact Leningrad anchor registration. | Unchanged; SOV/GER ownership or control, siege window, and war or local-food-insufficient proof remain required. |
| `hist_dutch_hunger_winter` | Existing exact Holland and Friesland anchor registrations. | Unchanged; HOL/GER ownership or control, 1944-45 window, and war or positive food pressure remain required. |
| `hist_spain_early_1940s` | Existing twenty-two exact Spain anchor registrations. | Unchanged; SPR ownership or control, 1939-42 window, and war or positive food pressure remain required. |
| `hist_ireland_memory` | Dead: selector and resolver required unassigned `famine_migration_profile_memory_proven`. | Exact Ireland anchor 113 calls the new helper; the profile still requires IRE/ENG owner/controller and positive live food pressure. |
| `hist_brazil_ceara` | Existing exact Ceará anchor registration. | Unchanged; BRA ownership or control, resolved occupation policy, and positive food pressure remain required. |
| `hist_congo_interaction` | Existing exact Congo and Middle Congo anchor registrations. | Unchanged; BEL/FRA ownership or control, resolved occupation policy, and positive food pressure remain required. |
| `hist_ethiopia_policy` | Existing exact Ethiopia and Tigray anchor registrations. | Unchanged; ETH/ITA ownership or control, 1936-41 window, and war or resolved occupation policy remain required. |
| `hist_nuclear_winter_global` | Existing active-food-state registration plus Air Cleanliness or local winter proof. | Unchanged; active food state, Air proof, and positive food pressure remain required. |

No other profile was found dead or overbroad in the inspected selector, resolver, bootstrap, and candidate lifecycle.

## State and scope contract

The proof flags are state flags, not country variables, temporary variables, global flags, event targets, ideology tests, or food-pressure values.

The Soviet trigger accepts only the exact state constants `soviet_kiev`, `soviet_western_kiev`, `soviet_kharkov`, `soviet_odessa`, `soviet_stalino`, `soviet_caucasus_mountains`, `soviet_kazakhstan_north`, `soviet_kazakhstan_central`, `soviet_kazakhstan_south`, `soviet_rostov`, and `soviet_saratov` together with `famine_migration_historical_memory_soviet_1932_proven`.

The Ireland trigger accepts only `famine_migration_profile_state_id.ireland` together with `famine_migration_historical_memory_ireland_proven`.

The registration helper is called in a state scope that has already passed `famine_migration_state_is_valid` through the existing anchor registry. It does not inspect current date, owner, controller, ideology, famine stage, or pressure.

Owner/controller and positive food-pressure requirements remain in both selector and resolver branches, so durable memory never activates a profile by itself.

## Idempotence, save/reload, and cleanup

`set_state_flag` is idempotent, and the helper has no array, variable, event, or death side effect.

The existing `global.famine_migration_historical_profile_anchor_states` registry remains the only bounded scheduler input.

The helper is called during anchor registration and replayed by `famine_migration_process_registered_historical_profile_anchor`, which backfills existing saves with registered anchors even when `famine_migration_historical_profile_anchors_bootstrapped` is already set.

`famine_migration_unregister_historical_profile_anchor_state`, `famine_migration_clear_historical_profile_context`, `famine_migration_cleanup_state_registration`, and state-control cleanup intentionally do not clear the two proof flags because they are persistent historical-memory anchors rather than live registry or famine state.

No event target is introduced, so there is no target lifetime or global-target cleanup obligation.

## Constants and tuning plan

No new threshold, duration, probability, AI weight, death amount, or pressure tuning was introduced.

The existing `famine_migration_profile_state_id` script constants remain the single source for all exact anchor IDs, and the helper uses those constants rather than literal state numbers.

The existing dynamic food-security weights, stage thresholds, reserve values, and mortality protections are unchanged.

## Migration from duplicated or dead logic

The old shared `famine_migration_profile_memory_proven` consumers were replaced at the two selector and two resolver call sites with profile-specific scripted triggers.

The duplicated exact-state knowledge is intentionally present in the helper and its paired triggers so a copied flag cannot prove a profile on an unrelated state; all numeric IDs still come from centralized constants.

No Event 149 path, event pool, pacing weight, mapmode, GUI, decision, relief helper, workbook, or asset was touched.

## Validation and MCP applicability

Read-only source validation confirmed that no `famine_migration_profile_memory_proven` consumer remains in the shared famine/migration source, both new flags have exactly one producer helper, and all four memory call sites use the matching profile-specific trigger.

The fifteen-profile census above was checked against the historical-profile CSV, coding prompt, implementation surface map, bootstrap, selector, resolver, and apply-context branches.

The patch was reviewed for no whole-world recurring scan, no event resurrection, no fixed historical death total, no new weighted surface, and no unsupported event-target dependency.

No HOI4 MCP route was applicable because this patch touches only state-scoped scripted profile registration and triggers; it does not edit a focus, GUI, map, event, or weighted/probability surface.

The game was not run, as required by repository instructions.

## Risks and blockers

The registration helper relies on the existing exact anchor registry and normal state validity contract, so an anchor that the pre-existing registry rejects will not receive a proof flag; this preserves fail-closed behavior and avoids a world scan.

The proof flags are intentionally durable and are not removed when a state changes controller or leaves the active registry; clearing them would erase historical memory rather than clean live famine state.

No unsupported fields affecting this design were identified in the required offline wiki and vanilla documentation review.

No implementation blocker remains within this bounded ownership surface.
