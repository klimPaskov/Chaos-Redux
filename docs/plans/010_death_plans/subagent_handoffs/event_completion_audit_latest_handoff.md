# Event 010 Death latest completion audit handoff

Date: `2026-06-15`

Subagent: `chaosx_event_completion_auditor`

Mode: read-only audit. No gameplay files were edited.

## Verdict

Event 010 is substantially implemented, but I do not recommend a final completion claim yet. The current package satisfies the main event identity, root firing, DTH country package, no-starting-army/no-starting-stockpile requirement, delayed report wording, natural island-to-mainland pacing, public reveal gate, custom defeat, triggerable cleanup, focus-tree expansion, living response routes, super-event/audio/image package, and most asset wiring.

Remaining completion blockers are concentrated in three areas:

- Ghost-host spawning lacks the consumed-population/state caps and scaling required by the specs.
- World-end foothold creation can silently fail on a remaining continent under stricter coastal-jump filters.
- Several achievements are simplified compared with the accepted achievement spec.

There is also a UI/detail uncertainty around pre-reveal Event Details previews: the body text has a pre-reveal variant, but the detail preview still adds Death evolution rows before public reveal. This should be validated in-game or explicitly accepted as catalog visibility.

## Surface status

| Surface | Current status |
| --- | --- |
| Obsolete Spirit of War/Peace surfaces | Complete. No active Event 010 Spirit of War/Peace surfaces found outside superseded docs/plans/history references. |
| Event identity and registration | Mostly complete. `death_event.id = 10` is defined in `common/script_constants/010_death_constants.txt:8`; Event 10 is in `global.fire_once_events` at `common/scripted_effects/chaosx_logic_effects.txt:152`; no cluster registration for Event 10 was found. |
| Root event | Complete. `chaosx.nr10.1` is hidden, triggered-only, and launches `death_launch_quiet_origin` from `events/010_death.txt:7`. |
| DTH country package | Complete for audited requirements. `history/countries/DTH - Death.txt:1` uses `set_oob = "DTH_1936"` only for templates; `history/units/DTH_1936.txt:1` contains templates but no placed divisions. `death_setup_country` no longer grants starting manpower/equipment and only loads the template OOB in `common/scripted_effects/010_death_effects.txt:95`. Zol has `death_god_of_death` in `common/characters/DTH.txt:9` and the trait exists in `common/country_leader/010_death_traits.txt:5`. |
| No initial notification | Complete. Root `chaosx.nr10.1` is hidden; missing-island reports are delayed via country events rather than a public opening event. |
| Delayed reports | Complete for report text. `chaosx.nr10.2` and `chaosx.nr10.3` localisation describes missing islands/harbors without naming Death or Zol at `localisation/english/010_death_l_english.yml:3`. |
| Spread pacing and island targeting | Complete for natural spread. Initial pulse constants are 120/150/180 days in `common/script_constants/010_death_constants.txt:61`; `death_schedule_next_spread_pulse` uses the four-to-six month first band in `common/scripted_effects/010_death_effects.txt:1532`. Nearby sub-100k island targeting is attempted before broader island pools in `death_try_island_spread` at `common/scripted_effects/010_death_effects.txt:1630`. |
| Mainland reveal gate | Complete for natural spread. `death_try_mainland_pressure_spread` requires the island-report evolution, consumed-state gate, pressure threshold, and a valid mainland reveal target in `common/scripted_effects/010_death_effects.txt:1705`; the target trigger requires mainland and population above 100k in `common/scripted_triggers/010_death_triggers.txt:242`. |
| World threat, neighbor wars, defeat | Mostly complete. Reveal refreshes `world_threat_source_death`, declares on neighbors, and emits reveal in `common/scripted_effects/010_death_effects.txt:273`. Defeat is custom and fires when DTH controls no states in `common/scripted_effects/010_death_effects.txt:1929`. |
| Ghost host tiers | Partial. 600/800/world-end tiers exist, but spawning is fixed per pulse/focus and not capped by consumed population/state count. Details below. |
| World-end gate and footholds | Partial. Gate requires public reveal, Chaos >1000, and a consumed continent in `common/scripted_triggers/010_death_triggers.txt:309`; foothold creation exists in `common/scripted_effects/010_death_effects.txt:2032`, but target filters can prevent required per-continent footholds. |
| Whole-world consumed super-event | Complete in script shape. `death_whole_world_consumed` checks no populated unconsumed states in `common/scripted_triggers/010_death_triggers.txt:320`; `death_try_fire_whole_world_consumed` emits super-event 65 in `common/scripted_effects/010_death_effects.txt:2147`. |
| Decisions, missions, AI | Mostly complete. Missing Island, Death Country, Compact, quarantine mission, Dark Methods, Black Oath, Herald, and Black Apostolate decisions exist in `common/decisions/010_death_decisions.txt`; decision/focus AI weights exist, but I found no separate Death AI strategy file. |
| Triggerable SCN-006 cleanup | Complete. `trigger_death_scenario` calls `death_cleanup_triggerable_scenario_context` at `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:1982`, and the cleanup helper clears scenario flags/variables/target in `common/scripted_effects/010_death_effects.txt:2257`. |
| Focus tree | Mostly complete. Active tree is 26 nodes, has `continuous_focus_position`, and covers the specified lanes in `common/national_focus/010_death_focus_tree.txt:1`. Remaining issue is not layout, but the ghost-host scaling below. |
| Evolution portrait format | Mostly complete by documentation/assets. Docs state normal Zol portrait before Last Shores and animated world-end Zol for later detail pages in `docs/events/010_death.md:31`; assets and `.gfx` include static and animated Zol packages. I did not run the UI to confirm the event-log portrait selector at runtime. |
| Super-event text/audio/image | Complete for active slots. Five Death super-event image slots are wired in `interface/chaosx_super_events.gfx:72`; audio is wired in `music/chaosx_super_event_music.asset:1311`; files exist and are valid OGG/WAV by `file`. |
| Achievements | Partial. Definitions and DDS triplets exist, but several unlock predicates are simplified. Details below. |
| Assets | Mostly complete. All 26 focus icons exist at `94x86`; `idea_public_death` exists at `gfx/interface/ideas/death/idea_public_death.dds` and is wired by `interface/chaosx_ideas.gfx:187`; super-event and Black Atlas assets exist. No active asset blocker found. |
| Documentation/spreadsheet | Mostly complete. `docs/events/010_death.md` is current; spreadsheet handoff records row 10 as implemented with SCN-006 present, but status should remain conditional until blockers are resolved or explicitly queued. |

## Blockers and simplified requirements

### Ghost hosts are not capped or scaled by consumed state/population

The spec requires ghost hosts to be limited by formulas/caps so tiny islands cannot create infinite divisions. Current implementation uses fixed spawns:

- Constants define only thresholds and fixed spawn counts at `common/script_constants/010_death_constants.txt:91`.
- `death_spawn_ghost_hosts_for_current_tier` spawns one passive host at 600 chaos or two stronger hosts at 800 chaos each time it is called, without checking a consumed-population/state cap, prior spawned total, or host budget in `common/scripted_effects/010_death_effects.txt:1847`.
- `death_spawn_ghost_hosts_for_world_end` always attempts four world-end host spawns in `common/scripted_effects/010_death_effects.txt:1880`.
- Triggerable scenario helpers use the same uncapped spawn helpers in `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:1960`.

This is a completion blocker for the accepted mechanics spec. A fix should introduce tracked host budgets or caps based on consumed population/state count, then spend that budget from pulses, focuses, and triggerable scenarios.

### World-end footholds can silently fail on remaining continents

The world-end spec calls for one foothold on every remaining continent where a valid coastal foothold exists. Current implementation attempts a single `random_state` per continent using the general coastal-jump target trigger:

- `death_create_world_end_footholds` loops continents with one `random_state` block per continent in `common/scripted_effects/010_death_effects.txt:2032`.
- The reused `death_is_valid_coastal_jump_target` rejects capitals, watched coasts, quarantine lines, and any state with non-Death divisions in `common/scripted_triggers/010_death_triggers.txt:229`.

If every available coastal state on a remaining continent has divisions, a quarantine line, coastal watch, or capital status, no foothold is created and no failure state is recorded. This is weaker than the spec's world-end behavior. Either add a world-end-specific target trigger with staged fallbacks or document/queue the stricter behavior explicitly.

### Achievement predicates are simplified

Achievement definitions exist in `common/achievements/chaos_redux_achievements.txt:2021`, but several ready-flag setters do not match the accepted achievement requirements:

- `death_not_on_my_continent` checks global mainland consumed states, not the player continent. Evidence: `global.death_mainland_consumed_states` is used at `common/scripted_effects/010_death_effects.txt:1395`.
- `death_last_ferry` counts five uses of `Keep the Port Lit`, not five actually threatened/evacuated coastal or island states before consumption. Evidence: the candidate flag is set from a simple prepared-state counter at `common/scripted_effects/010_death_effects.txt:1272`, then marked ready on reveal at `common/scripted_effects/010_death_effects.txt:1343`.
- `death_counted_every_name` requires the telegraph/census candidate and Chaos below 800, but does not prove compact/census delay of ghost tier or disqualify high Black Methods exposure. Evidence: `death_counted_names_candidate` plus chaos ceiling at `common/scripted_effects/010_death_effects.txt:1403`.
- `death_black_tide_reversed` checks recorded footholds recaptured, but does not enforce the "no Herald state survives as Herald" disqualifier. Evidence: flag set at `common/scripted_effects/010_death_effects.txt:1434`; Herald cleanup occurs later in the defeat path.

These are not missing definitions or assets; they are simplified unlock logic.

### Pre-reveal event-log detail preview needs runtime validation or explicit acceptance

The actual delayed report events do not reveal Death. The event-log details body also has a pre-reveal text variant at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5375`.

However, the Event Details preview adds Death evolution rows for origin and missing-island reports whenever the selected event id is Death, even before `death_world_reported`:

- `common/scripted_effects/chaosx_events_log_effects.txt:1434` adds stage 1 and stage 2 previews for `constant:death_event.id` unconditionally.
- The evolution type title falls back to `chaosx.events_log.evolution.type.death` in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:7517`.

This may be acceptable for a catalog/detail page, but it conflicts with the stricter reading that pre-reveal logs/details should not name Death. I did not run the UI, so this is a validation gap rather than a confirmed in-game spoiler bug.

## Accepted plans and disposition

| Plan/handoff | Disposition |
| --- | --- |
| `docs/plans/010_death_plans/focus_tree_depth_followup_plan.md` | Marked implemented by parent. Current tree has 26 nodes and the requested lanes. I consider the focus-layout part implemented; ghost-host cap/scaling remains a mechanics blocker, not a tree-layout blocker. |
| `docs/plans/010_death_plans/improvement_loop_remaining_routes_addendum.md` | Marked implemented and promoted. Dark Methods, Black Oath, Herald, Black Apostolate, Black Atlas, route achievements, and animated/static asset packages are present. Achievement predicate simplifications remain unresolved. |
| `docs/plans/010_death_plans/subagent_handoffs/event_completion_audit_handoff.md` | Parent resolved the prior setup/trait/triggerable cleanup/defeat-super-event blockers. Current audit confirms those fixes are present. |
| `docs/plans/010_death_plans/subagent_handoffs/icon_focus_regeneration_handoff.md` | Implemented. All 26 active focus icons exist at final dimensions. |
| `docs/plans/010_death_plans/subagent_handoffs/icon_public_death_regeneration_handoff.md` | Implemented. `idea_public_death` exists, is `64x64`, and is wired at the existing path. |
| `docs/plans/010_death_plans/subagent_handoffs/generated_event_art_super_event_audit_handoff.md` | Implemented for active five Death super-event image slots. No separate Dark Methods super-event slot is active. |
| `docs/plans/010_death_plans/subagent_handoffs/spreadsheet_doc_handoff.md` | Implemented as documentation/spreadsheet alignment, but the workbook `Implemented` status should be read with this latest blocker audit attached. |

## Validation performed

Task-specific static checks performed:

- Confirmed no active Spirit of War/Peace Event 010 surface outside superseded docs/plans/history references with `rg`.
- Confirmed Event 10 is fire-once and not listed in the major-event set in `common/scripted_effects/chaosx_logic_effects.txt`.
- Confirmed DTH country history/OOB contains no placed starting divisions and no setup manpower/equipment grant.
- Confirmed delayed report localisation does not name Death or Zol.
- Confirmed 26 focus DDS files exist under `gfx/interface/goals/death/` and are `94x86` by `file`.
- Confirmed `idea_public_death.dds` exists at `gfx/interface/ideas/death/idea_public_death.dds` and is `64x64`.
- Confirmed active Death super-event DDS files are `457x328` and Death OGG/WAV files are readable by `file`.

Not performed:

- No HOI4 runtime launch or in-game Event Details UI validation.
- No scenario simulation proving first-pulse timing, mainland reveal ordering, world-end foothold success across all continent states, or achievement unlock/disqualifier behavior.

## Remaining blockers

1. Implement and validate a host-budget/cap model for Death ghost hosts across natural pulses, focus rewards, world-end spawns, and triggerable scenarios.
2. Add world-end-specific foothold fallback targeting or explicitly queue the stricter no-foothold behavior with design approval.
3. Bring achievement ready-flag logic in line with the accepted achievement spec, especially continent-specific tracking, ferry/threat proof, Counted Every Name disqualifiers, and Herald-survival disqualifier.
4. Validate or revise pre-reveal Event Details preview behavior so early reports/details do not reveal more than the spec permits.

## Recommended next actions

1. Patch ghost host budget/scaling first; it affects balance and the central Death threat model.
2. Patch world-end foothold target selection with a dedicated `death_is_valid_world_end_foothold_target` trigger and fallback tiers.
3. Patch achievement predicate tracking while the relevant state/route variables are still fresh.
4. Run a targeted in-game or parser-backed scenario pass for SCN-006 variants: Quiet Origin, Island Pattern, Mainland Reveal, Last Shores.

## Improvement-loop recommendation

Do not spawn `chaosx_improvement_loop_planner` for Event 010 right now. The remaining gaps are implementation-fidelity and validation issues against already accepted specs/plans, not a lack of design depth. Use implementation/audit follow-up instead.

## Parent resolution, 2026-06-15

The parent patch addressed the implementation blockers above:

- Added shared Death host-budget tracking in `common/scripted_effects/010_death_effects.txt`, tuned by `common/script_constants/010_death_constants.txt`. Natural pulses, focus rewards, world-end host pulses, foothold host creation, and SCN-006 helper spawns now spend from consumed state/population/foothold budget with passive, stronger, and world-end caps.
- Added world-end foothold target tiers in `common/scripted_triggers/010_death_triggers.txt` and routed foothold creation through `death_create_world_end_foothold_from_current_state`, including war declarations against the previous owner/controller before consumption.
- Reworked achievement tracking for `death_not_on_my_continent`, `death_last_ferry`, `death_counted_every_name`, and `death_black_tide_reversed` to use per-continent counters, actual prepared-state consumption, census/compact participation before 800-tier host appearance, Black Book exposure disqualification, and surviving-Herald disqualification.
- Gated late Event Details evolution previews behind `death_world_reported` and documented the pre-reveal preview behavior in `docs/events/010_death.md`.

Remaining validation need: in-game/runtime validation for Event Details preview visibility and SCN-006 Last Shores/world-end foothold behavior.
