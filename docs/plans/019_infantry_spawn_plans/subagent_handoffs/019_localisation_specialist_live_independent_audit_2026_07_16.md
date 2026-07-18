# Event 019 Live Localisation Specialist Independent Audit

Date: 2026-07-16

Mode: read-only specialist audit. No gameplay, localisation, scripted
localisation, GUI, GFX, asset, registry, documentation source, or spreadsheet
file was edited. This handoff is the only file created by the subagent.

## Verdict

Event 019 has complete structural English-key coverage, but the current live
player-facing contract is not localisation-complete. The exact open finding
count is:

| Priority | Open findings |
| --- | ---: |
| P0 | 0 |
| P1 | 6 |
| P2 | 4 |

There are no missing referenced keys, duplicate Event 019 keys, malformed YML
rows, raw technology-token displays, or missing UTF-8 BOMs. The open findings
are stage-specific text coverage, absent choice-effect presentation, and
stale/internal wording in existing keys.

## P0

None.

## P1

### L19-P1-01: the pre-fire manifestation has no evolution-aware description

Live evidence:

- `events/019_infantry_spawn.txt:28` always uses `chaosx.nr19.2.d`.
- `infantry_spawn_apply_prefire_evolution_entry` applies every already-active
  Evolution I-IV stage while suppressing reports `.101` through `.104`.
- The source comment says the report selects the evolved direction, but the
  event has one unconditional static description and no scripted-localisation
  call or conditional `desc` block.

Stale key: `chaosx.nr19.2.d`. Its baseline wording is good for an unevolved
opening, but it is also shown unchanged when organized rolls, arsenal lots,
claimants, or anomalous hosts already define the live opening. Consequently,
the active paths have correct `.101`-`.104` prose while all four pre-fire paths
lose the stage-specific premise.

Required replacement: retain `chaosx.nr19.2.d` for the baseline and add four
conditional description keys, for example:

- `chaosx.nr19.2.evolution_i.d`: "Before dawn, formations appeared across [ROOT.GetNameDef] beneath seals no ministry issued. District staffs already hold common rolls, supply tables, and countersigns prepared for arrivals nobody recruited. Every company is waiting for its place in the national line."
- `chaosx.nr19.2.evolution_ii.d`: "Before dawn, fully formed units appeared across [ROOT.GetNameDef] with rifles, vehicles, armor, and specialist equipment drawn from incompatible arsenals. The army can use them, but each lot brings its own demands for training, repair, and supply."
- `chaosx.nr19.2.evolution_iii.d`: "Before dawn, complete military societies appeared across [ROOT.GetNameDef]. Their officers carry private seals, their companies share unfamiliar countersigns, and a sealed muster ledger offers the government its first draw before those commands learn to stand alone."
- `chaosx.nr19.2.evolution_iv.d`: "Before dawn, ordinary formations and impossible hosts appeared across [ROOT.GetNameDef]. Dead infantry, pale processions, and living stone wait beside the national barracks, each carrying obligations and loyalties that no ordinary personnel roll can contain."

Wire the most advanced active stage to the matching description so one report
still folds the pre-fire history without showing four back-to-back milestones.

### L19-P1-02: the pre-fire Evolution III draw/refusal choices hide every consequence

Exact affected option keys:

- `chaosx.nr19.2.b`
- `chaosx.nr19.2.c`

Both options call material state-changing logic through `hidden_effect`, but
neither has a `custom_effect_tooltip`. Add and wire:

- `chaosx.nr19.2.b.tt`: "Accept one initial unrestricted formation draw, open the Muster Board, and place the new lot under national accounting."
- `chaosx.nr19.2.c.tt`: "Decline the initial draw and keep the Muster Board dormant. Refusal during a war weakens Muster Control and raises Army Congestion."

This is a missing player-facing surface, not a dangling referenced key; the two
proposed keys do not currently exist because the event never requests them.

### L19-P1-03: the claimant-demand report is not tooltip-equivalent to its decision and Muster Board paths

Exact affected option keys:

- `chaosx.nr19.201.a`
- `chaosx.nr19.201.b`

The event comment states that the report, decisions, Muster Board, and AI use
the same response effects. The decision and board paths expose costs and
effects, but the immediate report sends both responses through `hidden_effect`
without a custom tooltip. Add and wire:

- `chaosx.nr19.201.a.tt`: "$infantry_spawn_accept_claimant_demand_cost_text$\n\n$infantry_spawn_accept_claimant_demand_effect_tt$"
- `chaosx.nr19.201.b.tt`: "$infantry_spawn_refuse_claimant_demand_effect_tt$"

The reused component keys already exist and resolve. This closes the only
material player/AI-equivalent response path whose visible event omits the
decision/Muster Board consequence text.

### L19-P1-04: first-family reception tooltips expose registry implementation vocabulary

Stale keys:

- `chaosx.nr19.105.a.tt`
- `chaosx.nr19.105.b.tt`

Both say "recorded provider package", "provider price", and "request
overhead". Those are registry and tuning terms, contrary to the spec rule that
the report show only what soldiers and civilians can observe.

Exact replacement direction:

- `chaosx.nr19.105.a.tt`: replace the first and last sentences with "Accepts one §Y[This.GetInfantrySpawnSelectedFamilyName]§! formation under guarded national custody." and "This first reception carries no material or administrative charge." Preserve the three current numeric effect lines.
- `chaosx.nr19.105.b.tt`: replace the first and last sentences with "Accepts one §Y[This.GetInfantrySpawnSelectedFamilyName]§! formation under a negotiated charter recognizing its internal autonomy." and "This first reception carries no material or administrative charge." Preserve the four current numeric effect lines.

### L19-P1-05: SCN-013 anomalous copy explicitly reveals parent-event isolation

Stale keys:

- `infantry_spawn_scenario_type_anomalous_rising_tt`
- `chaosx.scenarios.infantry_spawn.desc.anomalous_rising`

The phrases "without calling the wider histories" and "without awakening the
wider histories" directly expose the hidden parent-isolation contract. Part 8
explicitly forbids the scenario row from revealing parent isolation.

Exact replacements:

- `infantry_spawn_scenario_type_anomalous_rising_tt`: "Zombie, ghost, golem, and other nonhuman formations rise at high saturation. Their new regional commands establish independent hosts and begin their wars at once."
- `chaosx.scenarios.infantry_spawn.desc.anomalous_rising`: "Nonhuman formations rise under new regional commands and begin their wars immediately. Zombie, ghost, and golem hosts establish armed breakaways wherever their ranks gather."

### L19-P1-06: supervised demobilisation describes an engine failure and cancellation fallback

Stale key: `infantry_spawn_supervised_demobilization_tt`.

Its final sentence says "If division-template editing becomes unavailable
across the country, the order is cancelled...". That is engine-capability and
fallback wording rather than the current world state.

Replace only the last sentence with:

> The order proceeds only while the army retains authority to alter the lot's
> muster pattern; no formation is removed and no stores are returned unless
> that authority remains intact.

## P2

### L19-P2-01: exact settlement exposes a ledger-array row count

Stale keys:

- `infantry_spawn_selected_lot_exact_obligation_cost`
- `infantry_spawn_selected_lot_exact_obligation_cost_blocked`
- `infantry_spawn_selected_lot_exact_obligation_cost_tooltip`

All three display `Rows: [?infantry_spawn_exact_settlement_row_count]`. "Rows"
is an implementation representation, not an in-world obligation. Replace the
label with `Obligation categories:` while retaining the dynamic value and every
human-readable equipment line.

### L19-P2-02: the anomalous-family tab still calls registry sources "providers" and prices "overhead"

Stale keys:

- `infantry_spawn_muster_gui_selected_family_cost_tt`
- `infantry_spawn_request_selected_anomalous_family_tt`
- `infantry_spawn_request_selected_anomalous_family_cost`
- `infantry_spawn_request_selected_anomalous_family_cost_blocked`
- `infantry_spawn_request_selected_anomalous_family_cost_tooltip`

Exact replacement direction:

- Board tooltip: "Each host demands its own reinforcement and sustainment price. Repeated anomalous requests add greater political and command strain."
- Request tooltip: "Pays the host's material price and the political and command burden created by earlier requests. A successful call creates one formation and closes the channel until the next request interval."
- In all three cost variants, replace `Base overhead:` with `National administration:` and leave the displayed Political Power, Command Power, per-request scaling, and family reinforcement price unchanged.

### L19-P2-03: several SCN-013 keys use selection-engine voice or visibly awkward grammar

Stale keys and exact replacement direction:

- `infantry_spawn_scenario_type_arsenal_lottery_tt`: remove `valid` from "valid specialist materiel".
- `infantry_spawn_scenario_intensity_low_tt`: replace "eligible territory" with "the world".
- `infantry_spawn_scenario_intensity_maximum_tt`: replace "Nearly every valid country" and "wherever the map can safely sustain them" with "Nearly every country able to sustain an open revolt" and "wherever those fronts can hold together".
- `infantry_spawn_scenario_confirmation.d`: replace "eligible countries" with "countries able to sustain the revolt".
- `infantry_spawn_scenario_setup_complete.d`: the interpolation currently yields phrases such as "The Barracks Overflow formations". Use "The chosen pattern, §Y[This.GetInfantrySpawnScenarioActiveType]§!, is taking the field at §Y[This.GetInfantrySpawnScenarioActiveIntensity]§! reach, and the first divided governments are already issuing rival orders."
- `infantry_spawn_scenario_setup_failed.d`: replace with "No command area could sustain a coherent rebel front under the selected orders. The unbidden muster has not begun."
- `infantry_spawn_scenario_request_unregistered_tt`: replace with "Seals the chosen crisis pattern and reach in the muster orders, then opens the final confirmation report."
- `infantry_spawn_scenario_launch_unregistered_tt`: replace "eligible countries" with "countries able to sustain the revolt".
- `chaosx.scenarios.infantry_spawn.impact.low`: replace "eligible countries" with "countries able to sustain an open front".
- `chaosx.scenarios.infantry_spawn.impact.maximum`: replace "every safely eligible country" with "every country able to sustain an open front".

The four type names and four intensity values themselves are complete and
correctly selected; this finding concerns only their surrounding prose.

### L19-P2-04: one achievement description confuses a country with a state

Stale key: `019_infantry_spawn_every_barracks_a_front_DESC`.

Current text says "Keep the starting state alive" while the live trigger and
condition tooltip track the starting **country**. Replace it with:

> Keep the starting country alive when every garrison turns into a battlefield.

## Clean structural and content results

### Key and file integrity

- `localisation/english/019_infrantry_spawn_l_english.yml`: 2,873 keys,
  2,873 unique, zero malformed rows, zero cross-file duplicates.
- Across the five Event 019/shared English files, all 380 unique `$KEY$`
  aliases resolve.
- Across the two Event 019 scripted-localisation files plus the shared Event
  Log and scenario selectors, all 264 Event 19-relevant localisation targets
  resolve.
- No Event 19 player-facing value displays `GetTokenKey`, a raw technology
  identifier, or a raw equipment token. Technology-backed achievement copy
  uses readable terms such as "technology or special project".
- All five audited English files begin with `EF BB BF`: the main Event 019
  file, `chaosx_gui_l_english.yml`, `chaosx_achievements_l_english.yml`,
  `chaosx_event_names_l_english.yml`, and
  `chaosx_chaos_meter_l_english.yml`.

### Surface inventory

- 68 decisions and 14 missions have their required names and descriptions.
- All 68 decisions expose effect text and have an `ai_will_do` path; the 14
  timed missions are not AI-choice objects. The claimant/derivative complex
  decisions also expose their custom requirement text. The immediate claimant
  report parity gap is isolated in P1-03.
- Three decision categories, 45 derivative focuses, 67 ideas, and all 11
  achievements have complete name/description pairs.
- The dynamic derivative country-name matrix is complete: 1,365 of 1,365
  regional name/definite/adjective keys and 195 of 195 unsuffixed compatibility
  keys resolve across 13 identity stems, seven regions, and four ideologies.
- SCN-013 has four type names, four type descriptions, four intensity names,
  four intensity descriptions, confirmation, success, failure, and launch
  status copy. No type or intensity key is missing.

### Root, evolution, Event Log, Event Details, and cleanup

- The root report, all active Evolution I-IV reports, claimant reports, 13
  three-choice incidents, derivative release/defeat reports, and SCN-013
  reports resolve. The pre-fire text defect is isolated in P1-01/P1-02.
- `chaosx.event_name.19`, the Event Details premise
  `chaosx.events_log.window.event_details.infantry_spawn`, all four evolution
  title/body pairs, and all 18 live Event 19 history title/description pairs
  resolve through the shared selectors.
- Event Details stays at the visible premise level and does not list effect
  formulas, achievements, or secret thresholds.
- The root history remains suitable for its global/no-arbitrary-actor row.
- Release and defeat reports `.910`-`.915` and `.917`, plus zombie, ghost,
  golem, anomalous, and claimant defeat history, are in-world and aligned with
  the live cleanup paths. No stale derivative-defeat key was found.

### Male-only identity and army-only presentation

- Live claimant creation sets `female = no`; the dynamic claimant character
  check uses `is_female = no`. The 20 profiles expose 80 male regional names.
- Player-facing claimant prose uses commander, claimant, command, formation,
  and muster language. It never tells the player that the fixed display art is
  a portrait, person, face, or individual.
- `infantry_spawn_claimant_portrait_token_01` through `_20`, the GUI object name
  `infantry_spawn_muster_claimant_portrait`, and the frozen `GFX_portrait_*`
  identifiers are structural compatibility tokens. They are not displayed as
  English prose. The live art/documentation contract identifies all 20
  claimant slots as army/muster scenes, all six derivative slots as massed
  hosts, and the remaining slot as an identity-neutral muster, with no focal
  individual.

## Files and references inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- the full Event 019 source specification package and live near-completion
  addendum
- both Event 019 event files; all Event 019 decision, focus, idea,
  achievement, scripted-GUI, scripted-localisation, evolution, claimant,
  derivative, scenario, registry, AI, and cleanup surfaces needed to trace
  player text
- the five English files listed above and shared Event Log/Event Details and
  scenario selectors
- current claimant metadata and army/host visual handoffs
- the required offline wiki core pages plus event, decision, idea, AI,
  interface, scripted GUI, focus, country, achievement, division, equipment,
  and technology pages
- relevant official vanilla documentation and vanilla event/decision/UI
  precedents

## Simplifications, blockers, skills, and Git

No audit surface was omitted or replaced with a fallback. This is a finding
handoff, not a completion claim: the six P1 and four P2 findings remain open.
There is no P0 localisation blocker and no missing-key or encoding blocker.

Skills used:

- `chaos-redux-events`
- `chaos-redux-subagents`

No skill was created or updated. No files were staged and no commit was
created. The parent owns remediation, end-state re-audit, staging, and commit.
