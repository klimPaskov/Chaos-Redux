# Event 011 localisation audit

## Audit result

**Status: INCOMPLETE**

Event 011 has broad key coverage and most required player-facing surfaces are wired, but it is not ready for a completion claim. The current event log and evolution text reveal the alliance before the scripted reveal. Several pre-reveal decisions also use protected internal terms. Confidence wording does not match the specification, per-card `Confirmed` labels ignore corroboration, blocked custom costs are not fully red, and the faction name has no country-name fallback. The scenario workbook row does not exactly mirror the routed in-game scenario text.

This was a report-only audit. No gameplay, localisation, spreadsheet, asset, or interface file was edited.

## Blocking findings

### LOC-011-01: Event log and evolution text disclose the hidden alliance

**Severity: Critical**

The source specification requires three disclosure stages for the event log name:

- a concealed investigation name before the alliance is known
- a coordinated threat name at Evolution II
- the real alliance name only after public reveal

The implementation instead exposes `Secret Alliance` through one unconditional event-name key:

- `localisation/english/chaosx_event_names_l_english.yml:13`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:917`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:6380`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:7966`

The unconditional event-detail body also says that a network is growing and that an open coalition is drawing closer:

- `localisation/english/011_secret_alliance_l_english.yml:236`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:4252`

The evolution type and all three evolution bodies are likewise unconditional. They disclose minor-government membership, a major sponsor, a second major, the future public faction, and the future war declaration even when the corresponding evolution is locked or unreached:

- `localisation/english/011_secret_alliance_l_english.yml:239`
- `localisation/english/011_secret_alliance_l_english.yml:241`
- `localisation/english/011_secret_alliance_l_english.yml:242`
- `localisation/english/011_secret_alliance_l_english.yml:243`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:1966`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:2915`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:4453`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5059`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5734`

The log name, detail body, evolution type, and evolution bodies need stage-aware scripted localisation. Locked evolution previews must not reveal future membership or outcomes.

### LOC-011-02: Pre-reveal decisions use protected internal vocabulary

**Severity: Critical**

The localisation handoff forbids pre-reveal use of `Secret Alliance`, `pact member`, `coalition member`, the Anti-target pact name, `Cohesion`, `Readiness`, `founder`, and `sponsor` unless that fact has become public or was explicitly exposed.

Confirmed examples of premature disclosure include:

- `secret_alliance_turn_pact_member` at `localisation/english/011_secret_alliance_l_english.yml:327`
- `secret_alliance_demand_explanation_desc` at line 318
- `secret_alliance_plant_false_faction_dispute_desc` at line 326
- `secret_alliance_sabotage_forward_depot_desc` at line 329
- `secret_alliance_disrupt_planning_conference_desc` at line 332
- `secret_alliance_concede_standdown_desc` at line 352
- `secret_alliance_publicize_coalition_case_desc` at line 362
- `secret_alliance_preempt_coalition_desc` at line 378
- the associated tooltips and outcome text around lines 516, 537, 543 to 546, 557 to 559, 562 to 564, and 574 to 575

Some of these decisions can be visible while the network is still concealed. Their text needs concealed terminology until the relevant public-state flag or exposure flag is set. Post-reveal variants may retain direct faction and coalition language.

### LOC-011-03: Confidence and corroboration are inconsistent

**Severity: High**

The specification defines four confidence bands:

- Trace
- Plausible
- Credible
- Confirmed

The implementation defines five different bands:

- Unknown
- Possible
- Plausible
- Likely
- Confirmed

Evidence:

- `localisation/english/011_secret_alliance_l_english.yml:109`
- `common/script_constants/011_secret_alliance_constants.txt:270`
- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt:77`

The shared selected-suspect trigger correctly requires both the confidence threshold and the required evidence-class count. The per-card scripted-localisation branches do not use that trigger. They display `Confirmed` from the numeric confidence threshold alone:

- corroborated trigger in `common/scripted_triggers/011_secret_alliance_triggers.txt:325`
- per-card labels in `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt:186`

This permits a suspect card to say `Confirmed` while corroboration still blocks confirmed actions. The evidence panel explains that confidence and corroboration are separate, but it does not display whether the selected suspect has met the corroboration requirement. The GUI therefore provides conflicting status information.

All confidence surfaces need one vocabulary and one shared confirmed-state rule. The selected suspect view should display current corroboration status or the missing evidence-class requirement.

### LOC-011-04: Custom cost localisation is not reliably red or fully dynamic

**Severity: High**

Coverage is complete for the custom-cost roots. All 31 used roots have a base key, a `_blocked` key, and a `_tooltip` key. The visual and tuning behavior is not complete.

The `_blocked` keys wrap the base key in red, but the base strings contain their own yellow formatting. The inner yellow format resets the resource amount, so a blocked amount is not rendered as an unambiguous red cost:

- base cost strings at `localisation/english/011_secret_alliance_l_english.yml:398`
- blocked wrappers at `localisation/english/011_secret_alliance_l_english.yml:429`

Several values are also typed directly into localisation instead of being produced from the same variables or scripted values that drive the effects. Examples include 35, 45, 50, and 60 political power, 5 command power, 0.5 percent and 1 percent stability, 1.5 percent emergency stability, and 5 percent war support. The underlying costs are held in `common/script_constants/011_secret_alliance_constants.txt:703` to `:718` and are paid by helpers such as `common/scripted_effects/011_secret_alliance_effects.txt:2301` and `:2313`.

The displayed investigation stability cost currently agrees with the minor investigation constant at 0.5 percent. The diplomacy display agrees with 5 command power and 1 percent stability. The problem is maintainability and guaranteed synchronization, not a proven current numerical mismatch.

Each blocked key needs an independently red-formatted resource breakdown. Tunable numeric displays should be driven by the corresponding gameplay value or by one documented localisation source that is updated with the constant.

### LOC-011-05: Anti-target faction naming has no fallback

**Severity: High**

The required public faction form is `Anti-[target] Pact`, with a target-country name fallback when an adjective is missing or awkward. The current selector always returns the adjective form:

- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt:148`
- `localisation/english/011_secret_alliance_l_english.yml:149`

There is no branch to a name-based fallback. The public faction, news event, and super-event descriptions otherwise route through the created faction name consistently. Add a safe adjective check and a name-form fallback, then use the same helper on every pre-creation preview surface.

### LOC-011-06: Scenario workbook row does not exactly mirror routed game text

**Severity: Medium**

The workbook comparison used `documents/Chaos Redux Events.xlsx`, `Events` row 12 and `Scenarios` row 9.

`Events!B12:F12` exactly mirrors the current in-game event name, detail body, and three evolution bodies. It therefore also mirrors the spoiler problems described in LOC-011-01 and must be updated after the game strings are made stage-aware.

`Scenarios!D9` exactly lists the five implemented scenario types. `Scenarios!C9` and `Scenarios!E9` are summaries rather than exact mirrors of the routed type and impact descriptions:

- the workbook detail says `Anti-Target pact` instead of the actual dynamic `Anti-[target adjective] Pact`
- the workbook detail does not match any of the five type-specific in-game descriptions
- the workbook intensity cell summarizes all four intensities rather than matching the routed Low, Medium, High, and Maximum descriptions
- the safe-pool achievement qualification appears in the post-launch notice, but not in the selected Maximum impact description

The spreadsheet and in-game wording need one agreed source of truth. If the row is intentionally a summary, the Event 011 documentation must say so and the summary must still use the exact public faction terminology.

### LOC-011-07: Event writing style has prohibited punctuation

**Severity: Medium**

The event-writing skill prohibits semicolons and em dashes in Event 011 player-facing text. The audit found 19 Event 011 keys containing semicolons and four containing em dashes.

Em-dash examples:

- `secret_alliance_gui_evidence` at `localisation/english/011_secret_alliance_l_english.yml:128`
- `secret_alliance_gui_preparedness` at `localisation/english/011_secret_alliance_l_english.yml:129`
- `chaosx_super_event.73.q` at `localisation/english/011_secret_alliance_l_english.yml:210`
- `chaosx.scenarios.entry.id.secret_alliance` at `localisation/english/011_secret_alliance_l_english.yml:219`

Semicolon examples include `chaosx.nr11.201.d` at line 91, `secret_alliance_foreign_interference_desc` at line 143, `secret_alliance_quietly_approach_suspect_desc` at line 306, and `secret_alliance_demand_explanation_desc` at line 318 of the same file. Investigation and diplomacy descriptions, mission-expiry text, and several action tooltips account for the remaining instances. These should be rewritten with periods, commas, or separate sentences without changing gameplay meaning.

### LOC-011-08: The evidence panel does not list active named objectives

**Severity: Medium**

All seven named objective families have titles, descriptions, expiry text, and dynamic state names. The main GUI evidence panel only displays objective counts. The specification calls for a small active-objective list, so the panel does not expose the named objectives it tracks.

The exact count-only surface is `secret_alliance_gui_objectives` at `localisation/english/011_secret_alliance_l_english.yml:138`, placed by `interface/011_secret_alliance.gui:43`.

This is a presentation gap rather than missing mission localisation. The mission cards themselves are named and localised.

## Passed audit surfaces

| Surface | Result | Evidence |
| --- | --- | --- |
| Encoding | Pass | Event 011 main localisation, achievement localisation, and event-name localisation are UTF-8 with BOM. |
| Duplicate keys | Pass | No duplicate Event 011 localisation keys were found across the repository. |
| Event key coverage | Pass | All 25 titles, 25 descriptions, and 37 event-option keys referenced by Event 011 scripts resolve. |
| Decision key coverage | Pass | All 70 parsed Event 011 decision IDs have a title and description. |
| Idea key coverage | Pass | All 19 parsed Event 011 idea IDs have a title and description. |
| Custom cost triplets | Pass for coverage | All 31 used custom-cost roots have base, blocked, and tooltip keys. Rendering and dynamic-value problems remain under LOC-011-04. |
| Scripted-localisation format characters | Pass | No raw section or icon format characters were found in the Event 011 scripted-localisation file. |
| Named objectives | Pass for mission surfaces | Liaison Route, Courier, Clerk, Envoy, Safehouse, Manhunt, and Rumor objectives have named titles, descriptions, expiry text, and dynamic state references. The main panel list remains incomplete under LOC-011-08. |
| Border state wording | Pass | Border-conflict strings display both stored state names, and the corresponding decisions highlight both states. |
| Achievement triplets | Pass | All six achievements have a name, description, and custom criteria tooltip that agrees with the achievement matrix. |
| Scenario types | Pass | Random Valid Coalition, Regional Ring, Ideological Front, Great-Power Sponsor, and Unlikely Coalition are routed. |
| Scenario impacts | Pass | Low, Medium, High, and Maximum are routed. |
| Safe-pool notice | Pass | The post-launch notice reports achieved member and major counts and explains safe-pool exhaustion. |
| Super event slot 73 | Pass | Image, title, quote, remark, description, route-specific description, visibility, audio selection, playback, and news routing are present. The quote punctuation needs the style correction in LOC-011-07. |

## Achievement matrix comparison

All six required name, description, and custom-tooltip triplets are present and substantively match `docs/specs/011_secret_alliance_specs/handoffs/achievement_matrix.md`:

1. The Empty Chair
2. Every Thread
3. Their Man in the Room
4. Divide the Table
5. Surrounded, Not Buried
6. Two Giants, One Grave

The hidden achievements are registered as hidden. The safe-pool alternative is stated in the Surrounded, Not Buried criteria tooltip. No missing achievement-facing key or duplicate achievement key was found.

## Required correction order

1. Add disclosure-stage routing for the event name, event detail, evolution type, and every evolution body.
2. Replace protected terms on all concealed-state decision, tooltip, outcome, event-log, and GUI surfaces. Keep explicit post-reveal variants where appropriate.
3. Align the confidence bands to the specification and make every `Confirmed` label use the corroborated confirmed trigger.
4. Show the selected suspect's corroboration status and expose active named objectives in the evidence panel.
5. Rebuild blocked cost strings so each blocked resource amount is red and keep displayed values synchronized with the tuning constants.
6. Add the target-name fallback to the faction-name helper and route all public previews through it.
7. Align `Scenarios` row 9 and the event documentation with the final in-game strings.
8. Remove prohibited semicolons and em dashes from all Event 011 player-facing text.
9. Re-run the localisation audit after the correction tranche and before any completion claim.

## Sources reviewed

- repository `AGENTS.md`
- `chaos-redux-subagents` and `chaos-redux-events`
- Event 011 specification parts 1 to 5
- Event 011 localisation handoff and achievement matrix
- Event 011 event, decision, idea, scripted-localisation, scripted-trigger, scripted-effect, faction, achievement, GUI, scenario, event-log, and super-event files
- Event 011 implementation and super-event documentation
- `documents/Chaos Redux Events.xlsx`, `Events` row 12 and `Scenarios` row 9
- offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, factions, achievements, interface modding, and scripted GUI modding
- vanilla localisation formatter, localisation object, faction, and scripted GUI documentation

## Simplifications, omissions, and blockers

No audit scope was simplified. The assigned scope was report-only, so the findings were not patched in gameplay or localisation files. The blocking findings above prevent a localisation-complete verdict.
