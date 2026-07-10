# Event 011 localisation re-audit

## Audit result

**Status: CLEAN**

The current Event 011 implementation resolves all eight findings from the obsolete localisation audit. The disclosure wall, confidence and corroboration wording, dynamic cost presentation, faction-name grammar routing, workbook mirrors, writing style, active-objective list, achievements, scenario presentation, and super-event slot 73 are aligned with the accepted Event 011 package.

This was a report-only audit. No gameplay, localisation, asset, interface, or spreadsheet file was edited by the auditor.

## Finding closure

| Finding | Result | Current evidence |
| --- | --- | --- |
| LOC-011-01: event-log disclosure | Pass | `chaosx.event_name.11` routes through `GetSecretAllianceEventLogName` at `localisation/english/chaosx_event_names_l_english.yml:13`. Name and detail routing is concealed, coordinated at Evolution II, and revealed only after public reveal in `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt:8-32`. Evolution type and all three bodies use the same disclosure wall at `:34-72`. The routed strings and spoiler-safe locked titles are at `localisation/english/011_secret_alliance_l_english.yml:251-275`. Shared Event Log selectors consume these helper-backed keys rather than a direct revealed name or body. |
| LOC-011-02: protected pre-reveal vocabulary | Pass | Concealed event reports, decision names, descriptions, requirement text, tooltips, GUI copy, and Event Log text use incident, interference, suspect, participant, backer, planner, and coordination language. Direct pact, coalition-member, founder, sponsor, hidden-doctrine, Cohesion, Readiness, and public faction wording is confined to exposed facts, scenario or achievement criteria, faction presentation, reveal news, and post-reveal or settlement surfaces. Representative concealed decisions are at `localisation/english/011_secret_alliance_l_english.yml:342-359`, `:391-409`, and `:570-597`. |
| LOC-011-03: confidence and corroboration | Pass | The only player-facing confidence labels are `Trace`, `Plausible`, `Credible`, and `Confirmed` at `localisation/english/011_secret_alliance_l_english.yml:109-113`. The shared confirmed trigger requires both the numeric confidence threshold and three independent evidence classes at `common/scripted_triggers/011_secret_alliance_triggers.txt:360-363`. All three suspect cards call that trigger before returning `Confirmed` and show their own corroboration state at `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt:278-363`. The card text combines confidence and corroboration in `localisation/english/011_secret_alliance_l_english.yml:135-137`. The normal offensive and channel-dependent false-plan requirements also use the exact `Credible` term at `:576-577`. |
| LOC-011-04: dynamic and blocked costs | Pass | All 31 custom-cost roots have raw, yellow available, red blocked, and tooltip forms at `localisation/english/011_secret_alliance_l_english.yml:435-559`. Raw strings display refreshed runtime variables rather than duplicated tuning literals. `secret_alliance_refresh_dynamic_costs` populates them at `common/scripted_effects/011_secret_alliance_effects.txt:930-983`. Allied consultation and neutral inquiry share the full live diplomacy affordability trigger at `common/decisions/011_secret_alliance_decisions.txt:472-492` and `common/scripted_triggers/011_secret_alliance_triggers.txt:491-502`. Preemption separately presents its 50 percent minimum gate and its 5 percent spent strain at `localisation/english/011_secret_alliance_l_english.yml:462` and `:597`, gates it at `common/decisions/011_secret_alliance_decisions.txt:827-845`, and deducts the same displayed cost variable at `common/scripted_effects/011_secret_alliance_effects.txt:3583-3587`. Border escalation likewise pays its displayed variable at `:2954-2957`. |
| LOC-011-05: faction-name grammar | Pass | The single public-name helper selects the country form for dynamic countries or the event-owned override and otherwise uses the adjective form at `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt:235-249`. The two forms are `Anti-[target name] Pact` and `Anti-[target adjective] Pact` at `localisation/english/011_secret_alliance_l_english.yml:163-165`. `secret_alliance_initialize_faction_name_grammar` derives the override from dynamic status or the maintained `secret_alliance_faction_name_country_exception` flag at `common/scripted_effects/011_secret_alliance_effects.txt:785-798`. Normal initialization, scenario initialization, and faction creation refresh it at `:861`, `:3755`, and `:5308`. Faction presentation, news, super-event text, Event Log text, and previews all route through the created faction name or this helper. The exception contract is documented at `docs/events/011_secret_alliance.md:47`. |
| LOC-011-06: workbook mirrors | Pass | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` matches the final in-game strings exactly. `Events!B12:F12` matches the three routed event names, concealed detail, and three concealed evolution bodies at `localisation/english/011_secret_alliance_l_english.yml:261-275`. `Scenarios!B9:E9` matches the scenario name, default random-coalition detail, all five type labels, and all four intensity descriptions at `:234-249`. Exact cell-to-localisation comparisons returned true for all nine audited cells. |
| LOC-011-07: prohibited punctuation | Pass | No semicolon or U+2014 em dash remains in `localisation/english/011_secret_alliance_l_english.yml`, the Event 011 slice of `localisation/english/chaosx_achievements_l_english.yml:397-416`, `localisation/english/chaosx_event_names_l_english.yml:13`, or `docs/events/011_secret_alliance.md`. |
| LOC-011-08: active named objectives | Pass | The compact panel now lists active named objectives through eight mission-aware helpers at `localisation/english/011_secret_alliance_l_english.yml:140-149`. Liaison Route, Courier, Clerk, Envoy, Safehouse, Manhunt, Rumor Channel, and Contested Crossing are selected from live `has_active_mission` state at `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt:368-414`. The list is placed in the mechanic panel at `interface/011_secret_alliance.gui:43`. It is not a count-only display. |

## Exhaustive key coverage

The reference audit collected Event 011 localisation references from its events, decisions and categories, ideas, scripted effects, scripted triggers, scripted localisation, scripted GUI, faction template, goals and rules, interface, achievements, Event Log integrations, scenario integrations, and super-event integrations.

- 87 event references resolve: 25 titles, 25 descriptions, and 37 option names.
- All 70 parsed Event 011 decisions have title and description keys.
- All 19 parsed Event 011 ideas have title and description keys.
- All 31 used custom-cost roots have base, blocked, and tooltip keys.
- All six achievements have name, description, and custom criteria tooltip keys.
- The channel-dependent `secret_alliance_false_plan_requirements_tt` reference at `common/decisions/011_secret_alliance_decisions.txt:515` resolves to the exact live requirement text at `localisation/english/011_secret_alliance_l_english.yml:577`.
- Across the collected Event 011-facing key set, zero keys are missing and zero relevant keys are duplicated.

## Achievements

All six implemented achievements match `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_achievement_matrix.md` in player-facing requirements and disqualifiers:

1. The Empty Chair
2. Every Thread
3. Their Man in the Room
4. Divide the Table
5. Surrounded, Not Buried
6. Two Giants, One Grave

The definitions are at `common/achievements/chaos_redux_achievements.txt:2054-2173`, and their name, description, and criteria text is at `localisation/english/chaosx_achievements_l_english.yml:398-415`. The text covers normal versus scenario origin, innocent-country disqualifiers, corroborated complete-network evidence, turned-channel preservation, event-driven coalition exits, safe-pool maximum composition, major-sponsor snapshots, capital retention, independence, Resolve collapse, and world-end or human-consent exclusions where applicable.

## Scenario and super-event integration

SCN-009, `Coalition Unmasked`, is registered as `triggerable_scenario_id.coalition_unmasked`. Its name, five type-specific descriptions, five type labels, and four intensity descriptions are selected in `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt:40-41`, `:282-310`, `:521-549`, and `:720-741`. The result notice reports achieved member and major counts and preserves the safe-pool maximum qualification at `localisation/english/011_secret_alliance_l_english.yml:90-92`.

Super-event slot 73 is complete and route-exact:

- slot 73 and unique audio ID 43 are defined at `common/script_constants/011_secret_alliance_constants.txt:945-946`
- title, route-backed description, quote, and remark are at `localisation/english/011_secret_alliance_l_english.yml:224-231`
- hostile-war, player-forced, fractured, and pact-controlled descriptions have explicit route conditions and no generic route fallback at `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt:204-233`
- the shared super-event image, title, quote, remark, and description selectors register slot 73 at `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:228-230`, `:572-573`, `:802-803`, `:1032-1033`, and `:1262-1263`
- `GFX_super_event_011_secret_alliance_public_reveal` is registered at `interface/chaosx_super_events.gfx:172-173`
- reveal visibility, audio selection, playback, and public news routing are invoked at `common/scripted_effects/011_secret_alliance_effects.txt:3924-3942`. The news event is defined at `events/011_secret_alliance.txt:532-540`

## Sources reviewed

- repository `AGENTS.md`
- `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-decisions-missions`, and `xlsx`
- accepted Event 011 specification parts 1 to 5, matrices, localisation and spreadsheet handoffs, implementation documentation, and current Event 011 script and presentation files
- offline Paradox wiki pages required by the repository, including localisation, data structures, triggers, effects, modifiers, scopes, on actions, events, decisions, ideas, AI, factions, achievements, interface modding, and scripted GUI modding
- relevant vanilla documentation for localisation formatting and objects, script concepts, triggers, effects, modifiers, decisions, factions, on actions, and scripted GUIs

## Simplifications, omissions, and blockers

None within the localisation re-audit scope. No fallback, placeholder, missing route, missing key, stale workbook field, or unresolved LOC-011-01 through LOC-011-08 finding remains. This verdict covers the assigned localisation and presentation audit. It is not a standalone claim that every unrelated Event 011 gameplay or asset audit is complete.
