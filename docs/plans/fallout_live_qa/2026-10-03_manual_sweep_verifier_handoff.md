# Manual Fallout Sweep Verifier and Air Winter Runtime Errors Handoff

Disposition: `implemented`. Source review and save inspection only. Hearts of Iron IV was not launched, so every claim below about runtime behaviour after the fix still needs the parent's live retest.

## Evidence used

- `qa_scn014b.hoi4` (1936.1.1.16), `qa_fo_apr.hoi4` (1936.4.12.11), and `qa_000_fresh_1936.hoi4`, all HOI4 1.19.2.0, read with `.agents/skills/chaos-redux-save-inspection/scripts/save_inspect.py` (`info`, `flatten --in variables`, `flatten --in flags`, `flatten --in states`, `flatten --in provinces`, `get entity`, `get pending_events`).
- `C:/Users/klimp/Videos/chaos_redux_trailer/records/qa/fallout_longrun_error.log`.
- Installed `documentation/effects_documentation.md` (`launch_nuke`, `create_entity`, `destroy_entity`, `damage_building`, `country_event`), `documentation/triggers_documentation.md` (`num_nukes_left_to_drop`, `non_damaged_building_level`), `documentation/dynamic_variables_documentation.md` (`non_damaged_building_level@`), vanilla `common/on_actions/00_on_actions.txt` (`on_nuke_drop`).
- Offline wiki: `On actions` (`on_nuke_drop`: ROOT launcher, FROM struck state), `Event modding` (event delays), `Effects` (`create_entity`, `launch_nuke`), `Localisation` (variable formatting).
- MCP: `hoi4.source_lookup` parsed the rewritten `fallout_manual_native_nuke_belongs_to_sweep` and the new `air_winter_visual_seed_anchor_provinces`. `hoi4.event_inspect` returned `INTERNAL_ERROR` on `scan` and rejected `lint`/`trace` arguments, so no MCP event-graph evidence exists for this change. That is a recorded route gap.

## 1. Manual sweep never reached the blackout

### What the saves show

- `chaos_meter_nuclear_uses = 10154` in `qa_scn014b`: every one of the 10,154 native calls produced exactly one `on_nuke_drop` callback, and all of them went down the generic Chaos Meter branch.
- `fallout_manual_sweep_error` and the re-set `fallout_manual_scenario_active` are dated `1936.1.1.13`. `first_nuke_dropped`, `fallout_air_contamination_permanent_99`, and the vanilla `JAP_nuke_*` flags are dated `1936.1.1.15`. The error log's wall clock agrees: hour 13 took about six real minutes (the whole launch chain), hour 15 took about seven more (the drops).
- No state carries `fallout_manual_native_struck` or `fallout_manual_native_strike_count` in `qa_fo_apr`, while all 1,081 states carry the prestrike baseline.
- 3,463 provinces across the whole id range (2 to 13,413) have destroyed buildings, so the strikes themselves hit their exact targets.

### Root cause

`launch_nuke` only queues a strike. The engine drops it and runs `on_nuke_drop` on a later tick (here two hours later). The observer trigger `fallout_manual_native_nuke_belongs_to_sweep` required the synchronous `fallout_manual_batch_launch_window` flag and `status = sweeping`, both of which were gone by the time the callbacks arrived. In addition, chained `hours = 1` event delays resolved inside the same hour, so all 41 batches and all seven verifier attempts (`.960` to `.966`) ran at 13:00. The last verifier saw `observed = 0`, failed with `observed_count_mismatch` (7), and the sweep closed. The 10,154 callbacks then fell through to `chaos_meter_on_nuke_drop`, which explains the maxed Chaos Meter, the permanent 99 percent contamination, and the ash-winter events with no blackout.

### Fix

- `fallout_manual_native_nuke_belongs_to_sweep` (`common/scripted_triggers/fallout_consolidated_triggers.txt`) no longer needs the launch window. It accepts a coordinator drop while the sweep is `sweeping` or `verifying`, the sweep has no error, and `observed < issued`.
- `fallout_manual_on_native_nuke_observed` (`common/scripted_effects/fallout_consolidated_effects.txt`) fires the currently scheduled verifier token immediately when the callback that completes `expected_province_strikes` lands during `verifying`. The token keeps its full trigger validation, and the delayed copy of the same token fails its trigger afterwards because the verifier flag and status have moved on.
- `fallout_manual_schedule_verifier` waits `constant:fallout_manual_sweep.verifier_delay_days` (1) per attempt instead of one hour, so the six retries give a seven-day settling window. `verifier_delay_hours` and `@FALLOUT_MANUAL_VERIFIER_DELAY_HOURS` were removed.
- Design and balance are unchanged: same 10,154 strikes, same 1,081-state verifier contract, same aggregate consequences and exact seven-day countdown.

### Error state before and after

Before: `fallout_manual_fail_sweep` set `status = error`, the error code, and `fallout_manual_sweep_error`, cleared every sweep and schedule flag, kept `fallout_manual_scenario_active` (which blocks a relaunch) and the Air shutdown, and told nobody. Strikes already landed stayed, with no blackout, and the player had no signal.

After: the same fail-closed behaviour, plus one visible notice `chaosx.fallout.904` to every human country on the transition into error. Its description switches on whether any launch was issued, and its option tooltip states that the sweep has ended, landed strikes keep their damage, no blackout follows, and the sweep cannot be ordered again in this world. No automatic relaunch was added, because a replay would duplicate native strikes.

## 2. Air Winter `create_entity` errors (12,351 lines)

### What the save shows

`qa_fo_apr` holds only four entities, one per id band (ground, primary particle, dead vegetation, hydrology), with valid entity names, `scale = 2`, `min_zoom = 1100`, and `x = y = z = 0`. Thousands of creates therefore collapsed onto one id per band, and none received a position.

### Root cause (inferred from the save, not engine-confirmed)

- The seven-digit ids (1,860,000 + state id and up) did not survive `[?var|.0]` substitution, while the sweep proves five-digit values (province 13,413) substitute verbatim.
- The `state =` placement was rejected: every entity sat at the origin while name, scale, and zoom were applied. `invalid params` is the only `create_entity` message in the executable near its `invalid position` and `invalid entity id` siblings.
- Every slot was re-issued on every monthly pulse even when its visual was unchanged (1,978, 2,477, 3,103, and 4,793 errors on 1 February, March, April, and May).

### Fix

- `air_winter_visual_schema.version` 2 with five-digit bands: 3,000, 5,000, 7,000, 9,000, and 11,000 plus state id (max 12,081).
- All 13 `create_entity` calls use `province = [PROVINCE_ID]` from the per-state `air_winter_visual_anchor_province`, seeded once per visual schema by the new generated ledger `air_winter_visual_seed_anchor_provinces` (1,081 rows: highest victory-point land province, else first land province, from vanilla `history/states` and `map/definition.csv`, hashes in the effect header). A state without an anchor shows no regional visual.
- Change keys per slot (`air_winter_visual_<slot>_key`, constants `air_winter_visual_slot_key`) make the monthly refresh re-issue a slot only when its desired visual changes. The destroy helpers clear the keys. Entity count stays bounded at five per state.
- The `pdx_audio` out-of-memory line is dated 1936.01.28, before the first `create_entity` on 1936.02.01, so the entities did not cause it. The more likely load is the 10,154-callback `on_nuke_drop` fan-out (vanilla news events plus the humanitarian, Event 023, and Chaos Meter hooks).

## 3. `remove_dynamic_modifier` errors (about 1,800)

All 26 unguarded removals in the Air Winter event and outcome helpers (original lines 4632 to 6009) now run only under `has_dynamic_modifier`.

## 4. `Failed to find building for damage effect` (18)

The Air Winter building-family damage cursor, the hydroelectric, refinery, refinery-output, and reactor outcome helpers, the airbase-closure response, and the two Air Winter rail and thaw event outcomes guarded on total building level (`infrastructure > 0` and similar) or not at all. After the sweep, most of those levels are fully damaged. Each call now requires `non_damaged_building_level@<type> > 0`, matching the existing desert-city and dead-city helpers. The exact call behind each of the 18 lines cannot be identified from the log, because it carries no script location.

## Changed files

- `common/scripted_triggers/fallout_consolidated_triggers.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt` (own hunks only, other agents' hunks in the same file stay uncommitted)
- `common/script_constants/fallout_consolidated_constants.txt`
- `events/fallout_world_end_events.txt`
- `localisation/english/fallout_consolidated_l_english.yml`
- `docs/plans/air_cleanliness_fallout_plans/MANUAL_FALLOUT_SCENARIO_PLAN.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_MANUAL_PROVINCE_SWEEP_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_REGIONAL_VISUAL_WIRING_PROOF.md`
- this handoff

## Live retest checklist

1. Fresh 1936 game, launch scenario 14 at Maximum, then save once the strikes have visibly landed and again after 1 day. Expect `fallout_manual_observed_strike_count = 10154`, `fallout_manual_unique_struck_state_count = 1081`, `fallout_manual_state_strike_sum = 10154`, `fallout_manual_status = 3` (countdown), no `fallout_manual_sweep_error`, and `global.chaos_meter_nuclear_uses` equal to 10,154 (added once by the aggregate, not per strike).
2. Seven days after the countdown starts, the blackout, fractured map, and `world_end_fallout` apply (`fallout_manual_status = 5`).
3. The error log has no `invalid params: ... create_entity` lines after 1 February, Air Winter visuals appear on their states rather than at the map corner, and the save's `entity` block holds ids between 3,001 and 12,081.
4. Over consecutive months, the per-state `air_winter_visual_*_key` values stay stable while phases hold, and no repeated create errors appear. After save and reload, regional visuals are still placed on their states.
5. No `remove_dynamic_modifier modifier does not exist` lines for `air_winter_*` modifiers and no `Failed to find building for damage effect` lines.
6. Force a failure (for example by ending the game state that owns the coordinator before the verifier runs) only if convenient: every human player receives "The Last Wave Never Came".

## Remaining risks

- The `create_entity` diagnosis is inferred from save contents and could not be confirmed in game. If placement still fails, record the saved entity block and the error line for the next pass.
- An unrelated nuke dropped by the coordinator country during the verifying window would be counted as a sweep strike and later trip the state-count check.
- If the coordinator is re-homed by the daily reconcile while drops are pending, callbacks from the old coordinator are not counted.
- The vanilla `on_nuke_drop` news fan-out and the other mod `on_nuke_drop` hooks still run 10,154 times. This is the existing release blocker in `MANUAL_FALLOUT_SCENARIO_PLAN.md`.
