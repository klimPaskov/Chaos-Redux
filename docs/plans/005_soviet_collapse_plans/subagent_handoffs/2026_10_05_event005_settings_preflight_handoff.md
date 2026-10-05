# Event 005 Settings Preflight Handoff

## Status

The 005-owned preflight helper is implemented in `common/scripted_effects/005_soviet_collapse_effects.txt` as `soviet_collapse_prepare_event_fire`.

The parent-owned shared call is present at `common/scripted_effects/chaosx_settings_effects.txt:4021`, immediately after `event_single_fire_allowed` and `event_fire_dispatched` initialization and before the dispatch-readiness branch.

The ordinary `chaosx.nr5.1` entry contains its own matching rejection branches for direct calls that bypass the Settings dispatcher.

## Behavior contract

The shared dispatcher calls the helper with the caller's temporary `event_id`, after initializing `event_single_fire_allowed` and `event_fire_dispatched` and before the final dispatch gate.

The helper first checks the Event 005 id, then preserves the valid joint-opening pending path. Outside that path, it rejects missing, capitulated, or landless `SOV`; an active Union crisis; an individual-crisis load at or above its shared cap; and `soviet_collapse_triggerable_scenario_suppressed_fire_once`.

Each rejection sets `event_single_fire_allowed` to zero before the dispatcher can fire Event 005 or write its fire-once history.

For a manual human request outside an event-cluster member context, it requires the saved `chaosx_manual_event_requester` target, an active manual-request flag, and an unused failure receipt.

The original requester receives one cause-specific report: `.138` for missing, capitulated, or landless SOV; `.139` for an active Union crisis; `.144` for crisis capacity; or `.145` for triggerable-scenario suppression. The helper sets `chaosx_manual_event_failure_shown` before queuing the report so the shared generic failure response cannot create a second popup.

Automatic rejected attempts and non-manual callers are suppressed without a player report; the direct `.1` event reports to the country that invoked it.

The pending joint-opening presentation takes precedence over the active, capacity, and suppression checks in both the root and Settings preflight. It remains allowed to route to SOV's `.2` continuation without starting a duplicate crisis.

## Reference and validation evidence

- The bounded `hoi4.reference_search` for country-event and trigger behavior returned the offline Wiki `any_owned_state` entry at line 131, result id `5399b6193ead1da3a5564eec03b773bbf0154cbd319bbacf55b35aa96eb1b397`, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, and installed `has_capitulated` at lines 3352-3360, result id `8fdbc3ee0ca8b08bd144c5017b7a18741ffbcede22c56692940a7b70201f069d`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- `hoi4.reference_read` returned the Wiki `any_owned_state` country-scope definition and installed `has_capitulated` country-scope definition under those source revisions.
- The offline Wiki `Event modding - Hearts of Iron 4 Wiki.md` was read locally at lines 25-35, 39-43, 145-147, and 194-204. It describes country-event ROOT scope, firing an event through an effect, `is_triggered_only`, and event-ID arguments. Its local snapshot SHA-256 is `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
- The offline Wiki `Data structures - Hearts of Iron 4 Wiki.md` event-target section was read at lines 303-328, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`. The offline Wiki `Effects - Hearts of Iron 4 Wiki.md` `save_event_target_as` entry was read at line 357, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`. The Wiki `has_event_target` entry was read at line 646, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`.
- Installed `documentation/effects_documentation.md` `country_event`, `save_event_target_as`, and `set_temp_variable` were read at lines 2943-2967, 6496-6504, and 7820-7827, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Installed `documentation/triggers_documentation.md` `any_owned_state`, `has_capitulated`, `has_event_target`, and `check_variable` were read at lines 1612-1620, 3352-3360, 3844-3852, and 2110-2135, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- The existing `individual_crisis_load_is_below_cap` trigger sums its provider markers and compares the result against the shared cap in `common/scripted_triggers/individual_crisis_targeting_triggers.txt:12-117`; `common/script_constants/individual_crisis_targeting_constants.txt:17` sets `active_cap = 3`. The three test flags each satisfy a separate counted branch in that trigger.
- A local Boolean truth-table enumeration covered all 32 combinations of valid SOV, pending joint opening, active crisis, below-cap result, and suppression flag. The root and Settings preflight produced the same outcome for every combination and no valid-SOV no-op state remained. This checks the source decision model only; it is not Clausewitz execution evidence.
- Installed `documentation/console_commands_documentation.md` documents the `event` target-tag arguments at lines 850-853, `set_country_flag` at lines 1509-1512, `set_global_flag` at lines 1525-1528, `tag` at lines 1712-1714, and `annex` at lines 345-350. Its SHA-256 is `b65548c92b318f84f2185be790a3e0f2bce331ea646e233bf2ea85114bf8215d`.
- `hoi4.reference_context` for the event surface remained pending beyond 20 seconds. A later `hoi4.reference_search` batch for the exact `country_event`, Event Modding, and `has_event_target` sections remained pending beyond 25 seconds. `hoi4.event_inspect(mode=lint, selector={kind:event,eventId:chaosx.nr5.1})`, `hoi4.source_lookup(path=events/005_soviet_collapse.txt, line=23)`, and current-helper `hoi4.script_validate` also remained pending beyond 25 seconds with no artifacts or revisions. No current event-inspect or helper-validation coverage is inferred; source review and local documentation are the fallback evidence.

## Live acceptance handoff

Use a fresh `usa_1936` scenario at 1936.1.1 with USA as the human country for each case. Use a separate save for each Settings-rejection case so the once-per-requester report flag cannot mask a later result.

For the invalid-government case, pause and run `annex SOV` in the console. Return to USA and force Event 5 through the ordinary Settings selector.

Expected: USA receives exactly one `.138` report; `.1`, `.2`, and `.5` do not fire, and Event 005 is absent from fire-once history.

For the active-crisis case, start a fresh scenario and run `event chaosx.nr5.2 SOV` from the console to begin the normal Soviet opening. Then return to USA and force Event 5 through Settings.

Expected: USA receives one `.139` report, no second `.2` or `.5` opening is queued by the rejected Settings attempt, and Event 005 is absent from fire-once history for that attempt.

For the capacity case, start fresh, use `tag SOV`, then run `set_country_flag utopia_manifesto_accepted`, `set_country_flag random_civil_war_active`, and `set_country_flag video_game_in_sweden_program_active`. The shared load trigger counts each marker once, and `individual_crisis_targeting.active_cap` is three. Use `tag USA`, then force Event 5 through Settings.

Expected: USA receives one `.144` report; `.1`, `.2`, and `.5` do not fire, and Event 005 is absent from fire-once history.

For triggerable-scenario suppression, start fresh as USA, run `set_global_flag soviet_collapse_triggerable_scenario_suppressed_fire_once`, then force Event 5 through Settings.

Expected: USA receives one `.145` report; `.1`, `.2`, and `.5` do not fire, and Event 005 is absent from fire-once history.

To exercise the invalid-government report through the root directly, start fresh, run `annex SOV`, then run `event chaosx.nr5.1 USA`. Expected: USA receives `.138` from the root.

To exercise the active, capacity, and suppression reasons through the root directly, repeat each prepared state in a fresh scenario and run `event chaosx.nr5.1 USA` from the console instead of using Settings. Expected: USA receives the matching local report (`.139`, `.144`, or `.145`) from the root.

For the joint-opening exception, start fresh, use `tag SOV`, and run `set_country_flag soviet_collapse_joint_opening_presentation_pending`, `set_country_flag utopia_manifesto_accepted`, `set_country_flag random_civil_war_active`, and `set_country_flag video_game_in_sweden_program_active`. Also run `set_global_flag soviet_collapse_active` and `set_global_flag soviet_collapse_triggerable_scenario_suppressed_fire_once`. Then use `tag USA` and force Event 5 through Settings.

Expected: the pending path remains allowed and routes `.2` to SOV; it does not display `.139`, `.144`, or `.145`, does not start a duplicate crisis, and Event 005 is recorded once.

For the normal valid-SOV path, start a separate fresh game as the USSR and force Event 5 through Settings before the Soviet Union capitulates or loses every state. Expected: the human Soviet player sees `.2`, one `.47` unit report from the first released republic, and `.5` global news, and Event 005 is recorded once.

For the same valid-SOV path as USA, expected: USA sees only `.5` world news. The captured USA screenshot chain shows one `.5` popup over the requested two-month interval, alongside four unrelated vanilla popups.

If a later test run releases at least two countries from the internal-republic set (`KAR, KOM, CRI, TAT, BSK, FER, YAK, BYA, TAN`), expect `.95` world news once per crisis. Later regional-faction invite actions should use local `.38` notices after the first global `.48` news card.

These are exact live acceptance steps, not tests run by this agent. No game or desktop validation was performed.
