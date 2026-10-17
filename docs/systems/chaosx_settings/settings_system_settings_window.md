# System Settings Window

## Overview

`Settings > Advanced Settings > Show All Settings` opens `chaosx_system_settings_window`, a window for existing runtime settings that lack another in-game control.
It holds nothing that another page already offers and introduces no new variable or multiplier: every control writes a variable or flag that existing script reads.
Left click on an arrow uses the small step and right click the large step (`settings_system_steps` in `common/script_constants/settings_constants.txt`).

## Files

| Surface | File |
| --- | --- |
| Window layout | `interface/chaosx_system_settings.gui` |
| Scripted GUI wiring | `common/scripted_guis/chaosx_scripted_gui_system_settings.txt` |
| Effects | `common/scripted_effects/chaosx_system_settings_effects.txt` |
| Checkbox sprite getters | `common/scripted_localisation/chaosx_scripted_localisation_system_settings.txt` |
| Localisation | `localisation/english/chaosx_system_settings_l_english.yml` |
| Open button | `system_settings_button` in the Advanced Settings page of `interface/chaosx.gui` |
| Click steps | `settings_system_steps` in `common/script_constants/settings_constants.txt` |
| Bounds and defaults | `settings_advanced_bounds`, `event_system_defaults`, `event_system_timer_modifier_default` (existing constants) |

## Settings

| Setting | Variable or flag | Consumers | Default | Range | Control |
| --- | --- | --- | --- | --- | --- |
| Base event weight | `global.settings_event_weight` (staged), copied to `global.default_event_weight` | Crisis rescue weight floor (`apply_crisis_rescue_event_weight_adjustments`, twice this value), White Peace repeatable decay (`global.event_max_caps` over this value, clamped to 1), fallback cap in `get_event_cap` and `update_repeatable_event_weights`, welcome screen values | 1000 | 100 to 5000, step 100, large step 500 | Arrows, then Apply |
| Event interval scale | `global.settings_timer_modifier` (staged), copied to `global.chaos_timer_modifier_calm` by `update_all_timer_modifiers`, which also rescales the five higher tier modifiers | `calculate_next_timer_value` multiplies every timer by `global.chaos_timer_modifier` (the tier's modifier), the timer window range | 100% | 10% to 200%, step 5%, large step 25% | Arrows, then Apply |
| Crisis pressure on you | country flag `chaosx_setting_non_ai_crisis_pressure_enabled` | `chaosx_is_non_ai_crisis_pressure_active`, read by the shared event timer in `chaosx_logic_effects.txt` and communist spread, escalation and sabotage helpers in `001_communism_spread_effects.txt` | Off | On or off | Checkbox |

The two staged values follow the Event Weights page: arrows change the staged value, the value box shows it, `Active:` shows the live value, and `Apply` runs `apply_system_settings`, which copies both and refreshes the welcome screen values.
The base event weight does not rewrite the stored `global.event_weights` or `global.event_max_caps` arrays initialized at startup.
The interval scale applies to future timer calculations and does not reroll an interval already in progress.
`Reset` stages the defaults of both pacing values (`reset_system_pacing_to_defaults`).
`Reset All` runs `reset_system_settings_to_defaults`: it stages and applies both pacing values and turns crisis pressure off.
The global `Reset All Settings` button of the settings window calls `reset_system_pacing_to_defaults` before its existing `update_advanced_settings_values`, and `reset_miscellaneous_to_defaults` clears the crisis pressure flag, so it restores this window too.

The settings system keeps no multiplayer host restriction; these controls behave like the other settings pages.

## Why only these settings

An inventory of runtime state in the settings system and the systems it feeds found three values with no control:
the staged event weight and timer modifier (both defined in `initialize_global_settings_system`, bounded by `settings_advanced_bounds`, exported by Save Settings and shown on the welcome screen, but with no arrows anywhere) and the crisis pressure flag (set in `initialize_miscellaneous_settings`, documented as having no toggle).

Rejected candidates:

- Load-time script constants such as the Chaos Meter deltas, cluster roll chances and cooldowns, event timer start range, minor-event decrement steps, air contamination thresholds and death weights. They are read through `constant:` and cannot change at runtime without a new multiplier variable.
- `timer_min_decrement_cap` and `timer_max_decrement_cap`: derived from the interval limits by `calculate_dynamic_caps` and rewritten on every Apply Interval.
- `global.air_contamination_*_percent` thresholds: reassigned from constants on every contamination refresh.
- Per-tier timer modifiers (`global.chaos_timer_modifier_gathering` and the rest): derived from the calm modifier by `update_all_timer_modifiers`.
- `settings_logic_log_lines_enabled`, `chaos_ui_wear_disabled`, `air_winter_static_climate_map`, `settings_chaos_deaths_disabled`, `settings_air_cleanliness_disabled`, `world_end_disabled`, fallout consequence, event system, force trigger, timer window and tag management flags: already have controls (Event Logs status tab, Miscellaneous, Chaos Meter window, Settings pages).
- `zombie_system_disabled` and similar scenario flags: scenario state, not a setting.

## Candidate evidence and row contract

The parent task authorizes exposing all existing uncovered runtime settings and excludes duplicate normal controls, new gameplay multipliers, and conversion of load-time tuning to runtime settings.
The inventory checks the defaults and consumers against `13b8fabb9^`, the revision before the original All Settings window, rather than treating takeover source as proof that a setting already existed.
All three candidates and both numeric bounds exist in that baseline.
The `settings_system_steps` constants are UI click sizes introduced by the window, not pre-existing engine limits or additional runtime settings.

| Row id | Label | Single-line tooltip | Setting scope | Setter and reset |
| --- | --- | --- | --- | --- |
| `event_weight` | Base event weight | Sets fallback event caps, the crisis rescue weight floor and White Peace decay. Default: 1000 (100–5000). | Global staged and live variables | `adjust_system_event_weight`, required signed temporary `system_settings_delta`, then `apply_system_settings`. Reset through `reset_system_pacing_to_defaults` and Apply. |
| `timer_modifier` | Event interval scale | Scales future event intervals across all Chaos tiers. Default: 100% (10–200%). | Global staged and live variables | `adjust_system_timer_modifier`, required signed temporary `system_settings_delta`, then `apply_system_settings`. Reset through `reset_system_pacing_to_defaults` and Apply. |
| `non_ai_crisis_pressure` | Crisis pressure on you | Slightly shortens intervals for every scheduled event as Chaos rises and increases pressure from ongoing crises in your country. Default: Off. | Player-country flag | `toggle_non_ai_crisis_pressure`. `reset_system_settings_to_defaults` clears the flag and applies the numeric defaults. |

| Candidate | Existing definition/default | Existing runtime consumer | Qualification |
| --- | --- | --- | --- |
| Event weight | `common/scripted_effects/chaosx_settings_effects.txt:127`, `initialize_global_settings_system`. Live default at `common/scripted_effects/chaosx_logic_effects.txt:113`, sourced from `common/script_constants/event_system_constants.txt:39`. Existing bounds at `common/script_constants/settings_constants.txt:144`. | `chaosx_logic_effects.txt:569` and `:1123` fallback caps, `common/scripted_effects/crisis_rescue_effects.txt:50` rescue floor, `common/scripted_effects/009_white_peace_effects.txt:448` decay denominator. | Existing global staging, Apply integration, export row and real consumers. No control in the ordinary settings GUI. |
| Timer scale | `chaosx_settings_effects.txt:128`, `initialize_global_settings_system`. Live tier defaults at `chaosx_logic_effects.txt:130`, sourced from `event_system_constants.txt:62`. Existing bounds at `settings_constants.txt:145`. | `chaosx_settings_effects.txt:3532` `update_all_timer_modifiers`, `chaosx_logic_effects.txt:426` tier selection and `:466` timer multiplication. | Existing global staging and scale application for all six tiers. No ordinary control. |
| Player crisis pressure | `chaosx_settings_effects.txt:3728`, `initialize_miscellaneous_settings`, default flag set. `reset_miscellaneous_to_defaults` restores the same default. | `common/scripted_triggers/chaosx_settings_triggers.txt:228` `chaosx_is_non_ai_crisis_pressure_active` requires `is_ai = no` and the player-country flag. `common/scripted_effects/001_communism_spread_effects.txt:930` and related chance/cooldown helpers use it. | Explicit pre-existing preference and default, exported by Save Settings, no previous checkbox. The new setter changes only the acting player's flag. |

The scan of all settings initialization branches covers event selection, timer intervals, tag management, Chaos Meter, advanced settings, miscellaneous, Event Logs, cluster selection, and manual scenarios.
The five global `settings_*` staging variables are the two candidates plus recovery, cap reduction, and baseline major gain, which already have controls in the ordinary Advanced Settings page.
Variables without that prefix were also checked: timer intervals and derived caps, tier modifiers, welcome-screen caches, Chaos Meter and air-system initialization, manual scenario types/intensity, event/cluster registry data, and the chemical/biological/CBRN system variables.
The latter systems contain world and country state, operation receipts, action ledgers, project progress, selection state, and temporary computed values rather than additional hidden settings preferences.
No additional settings initialization helper or persistent gameplay-setting multiplier exists in those inspected systems.

| Excluded family | Source evidence | Reason |
| --- | --- | --- |
| Recovery, cap reduction, baseline major gain | `chaosx_scripted_gui_settings.txt:726` through `:790`, existing arrow/manual-entry/apply controls. | Already exposed. |
| Timer interval and decrement caps | `chaosx_settings_effects.txt:2084` initializes interval controls and `:2100` applies them. `calculate_dynamic_caps` writes both caps at `:2421`. | Intervals already exposed. Caps are derived and rewritten on Apply. |
| Logging | `settings_logic_log_lines_enabled` initialized off at `chaosx_settings_effects.txt:121`, consumed at `common/on_actions/chaosx_on_actions_system.txt:197`, controlled by `events_log_auto_checkbox_click` at `common/scripted_guis/chaosx_scripted_gui_events_log.txt:261`. | Already exposed in Event Logs Status. Other debug flags are achievement/provenance receipts or engine `is_debug`, not preferences. |
| Audio, UI wear, climate map | Miscellaneous bindings at `chaosx_scripted_gui_settings.txt:797` through `:838`. | Already exposed. |
| Event, force-trigger, timer, tag and Chaos Meter switches | Existing bindings in `chaosx_scripted_gui_settings.txt:566` through `:720`. | Already exposed. |
| Air, deaths and fallout toggles | `common/scripted_guis/chaosx_scripted_gui_chaos_meter.txt`, Air Cleanliness and Deaths tabs. | Already exposed, with permanent fallout guards retained. |
| Per-event, cluster, evolution and public world-end toggles | Event Logs, Event Details, Clusters and scenario controls. | Already exposed. Derived event-owned `*_enabled` gates follow those controls or progression. |
| Event animation preferences | `secret_alliance_toggle_animation_click` in `011_secret_alliance_scripted_gui.txt:68`, `acid_rain_world_motion_click` in `033_acid_rain_scripted_guis.txt:63`. | Already exposed in their owning windows. |
| Tier modifiers and air threshold caches | `update_all_timer_modifiers` in `chaosx_settings_effects.txt:3532`, air threshold conversion at `common/scripted_effects/chaos_meter_effects.txt:4832`. | Recomputed from the existing scale or load-time constants. |
| Chaos deltas, cluster chances/cooldowns, timer startup/minor-event anchors, air-system thresholds, system tuning tables | `common/script_constants/chaos_meter_constants.txt`, `event_cluster_constants.txt`, `event_system_constants.txt` and their direct `constant:` consumers. | Load-time constants. Exposing these would require new runtime state and consumer changes, outside authorization. |
| Counters, ledgers, pointers, current weights/caps, scenario and progression flags | Startup and system consumers reviewed directly. | Gameplay state or cached output, not an adjustable settings preference. |

## Logic handoff and validation

The takeover keeps the staged renames from the old `all_settings` effects, scripted localisation and documentation files.
The owned effects use only the two existing global staging variables, their original live destinations, the existing player preference flag, one UI visibility flag, and temporary scratch values.
No event targets, periodic hook, new gameplay variable, new gameplay multiplier, new AI action, or resource payment is introduced.
There is no duplicated gameplay system to migrate, only controls wired to existing settings and local adapters.
The existing shared `reset_all_settings` hunk must keep `reset_system_pacing_to_defaults` before `update_advanced_settings_values`, so resetting all settings restores these two staging values as well.

Source-derived boundary checks cover weight changes below 100 and above 5000, scale changes below 0.1 and above 2.0, staged changes before Apply, both reset paths, and country-local flag toggling.
For example, weight 150 with delta -500 stages 100, weight 4950 with delta 500 stages 5000, and scale 0.11 with delta -0.25 stages 0.1.
At scale 1, the existing helper produces tier modifiers 1, 0.8, 0.7, 0.6, 0.5, 0.5.
At scale 2, it produces 2, 1.6, 1.4, 1.2, 1, 1.
These calculations describe source behavior and do not claim observed engine execution or revised balance targets.
The base-weight Apply helper never touches `event_weights` or `event_max_caps`, preserving stored event progression.
The crisis-pressure checkbox matches its country flag, and the Fallout checkbox retains the enabled/transition/active/permanent-lock checks.
A source-contract audit against `13b8fabb9^` confirmed that every direct global destination and the crisis-pressure default pre-existed, that none of the owned helpers mutates stored event-weight/cap arrays, and that all eight helpers have direct call sites in the linked GUI or reset flow.

The subagent's MCP reference-context/search requests returned `not available to the model`, and the one retry after reported exposure changed returned an uncallable-tool error.
No additional retries are justified without a changed callable connection.
The parent retrieved installed scripted GUI documentation lines 1–80, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`.
Local reading supplements that with installed `documentation/effects_documentation.md` lines 2681–2693, 2792–2800, 6730–6737 and 7888–7908, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The country-flag trigger uses installed `documentation/triggers_documentation.md` lines 3624–3639, SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
The load-time exclusion follows installed `documentation/script_concept_documentation.md` lines 216–247, SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, and `common/script_constants/documentation.md` lines 1–34, SHA-256 `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
Offline scope and temporary-variable references are `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` lines 425–460, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, and `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md` lines 146–207, SHA-256 `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`.
Vanilla `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt` lines 1–80 provides the existing variable-backed property pattern, and the closest Chaos Redux precedent is the ordinary Advanced Settings staging/apply flow.

Parent integration owns labels/tooltips, the shared Show All Settings entry, GUI layout/click-state review, available render evidence, the independent pacing-setter audit and the final commit.
No gameplay simplification was made by the logic takeover.
Rendering and live-engine execution are outside this logic subtask's verification claims.
Guidance used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-scripted-gui` and `chaos-redux-subagents`.
No skill was created or updated by this subtask.

The independent probability auditor verified the boundary, staging, Apply, reset and human/AI gate cases against the actual consumers.
Its probability_inspect result identified no weighted surface in the setter file, so the findings use source calculations without a selection-probability claim.
With an unchanged stored cap of 1000, the clamped White Peace cap/default ratio is 1 at default 1000, 1 at default 100, and 0.2 at default 5000.
The rescue weight floor ranges from 200 to 10000 across the existing base-weight bounds.

## Parent checks and visual evidence

The parent retained the three qualifying controls and the Show All Settings entry, with separate Event Pacing and Crisis Pressure sections, staging/live values, Apply, group Reset and Reset All.
The localisation audit found all 24 literal window references defined and no duplicate window keys, and the three row-contract tooltips match the final localisation.
The parent also ran the repository static localisation audit, which reported zero parse errors.
The setter file returned `SCRIPT_CHECK_PARTIAL`: 27 commands were checked, including known-mistake checks, with no findings, while eight helper-root scopes and 11 argument blocks remained outside full validation coverage.
The helper scopes, clamps and consumer semantics were reviewed directly and by the independent probability auditor.

The `advanced-settings-default` source-mode preview at 1920×1080 and 2560×1440, both UI scale 1, was visually inspected, including its cropped window and resolution gallery.
Its source revision is `5bbdcc205f5cbaf2a0a65cba322caae5ba06570a4475b72586c60a3033815ce1`, with layout artifact SHA-256 `9cbf072fecb3ae3be2ce765ff803382ff6d53de6e4fa358415d7cad5c60620df` and resolution matrix SHA-256 `4a1e07edbfb97cc72c2463ab91d10ebff9cd1217afd31f0063071d721c9572c4`.
The title, labels, controls and sections fit the unchanged 540×372 layout at those resolutions.
The baseline fixture omitted the live interval value, leaving that token unresolved, and its numeric percentage formatter did not display the percentage as expected.
The final source uses the installed vanilla `%0` formatter and was reviewed against its documented 10%–200% range.
Final numeric-text and boundary-state pixels are not verified by that earlier preview.
The initial render request timed out after 600 seconds after publishing preview artifacts, and the one narrower final request ended with `JOB_WORKER_EXIT` without final artifacts.
The retry allowance is exhausted for that failed final check, and another attempt requires a changed worker or input condition that addresses the failure.
The available preview is not reported as a successful terminal tool result or live-game validation.

The requested controls are implemented without new gameplay settings or multipliers, duplicated ordinary controls, design reductions or replacement art.
Final render verification remains a limitation of the affected visual claim.

## Icons and assets

No new art.
The window reuses `GFX_tiled_window_2b_border`, `GFX_tiled_plain_bg`, `GFX_closebutton_small`, `GFX_chaosx_checkbox_checked`, `GFX_chaosx_checkbox_unchecked`, `GFX_chaosx_add_one`, `GFX_chaosx_subtract_one`, `GFX_chaosx_text_bg_60` and `GFX_chaosx_button_123x34`, registered in `interface/chaosx.gfx` or the installed game.

## Fallout control

The Fallout consequence toggle is the `fallout_system_scenario_checkbox` in the Miscellaneous menu of the settings window. Its sprite getter is `GetFalloutSystemScenarioDisabledCheckboxSprite` and its click gate is the shared `fallout_consequence_setting_available` trigger, which also locks the setting once Fallout has begun.

## Future plans

- A host-only restriction for multiplayer if the settings system gains one.
- A per-row marker for values that differ from their default.

C2 acceptance (13 October 2026): the owner requested event-wide, slight pressure, disabled by default.
`chaosx_apply_non_ai_crisis_pressure_to_next_timer` reads the current tier and multiplies only the player country's next shared timer by 0.98, 0.974, 0.968, 0.962, 0.956 or 0.95 before rounding and the existing minimum-day clamp.
All existing event categories use that timer; manually fired events are immediate and receive no artificial delay.
Historical default-On evidence above describes the prior source, not the current preference.
