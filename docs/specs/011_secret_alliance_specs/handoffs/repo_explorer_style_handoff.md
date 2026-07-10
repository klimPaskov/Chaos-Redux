# Repo explorer style handoff

Status: historical planning-intake map. Its `To Be Reworked` and missing-scenario statements describe the original intake. Current gameplay authority is engine-compatible commit `407b9a05`, atop balance freeze `1c87d923`; SCN-009 and the workbook statuses are implemented.

## Scope read

- Parent task: create the full source specification package for Event 011 Secret Alliance
- Explicit constraints: Minor Fire-Once, three initial minor countries, concealed membership, invitation of later members, Evolution I through III, immediate faction reveal and universal active-member war entry when one member enters war with the target, reveal super-event, no cluster, direct triggerable coalition scenario
- Source catalogs: event, cluster, and scenario CSVs
- Skills and project docs: every supplied Markdown and TOML listed in `source_inventory.md`

## Primary findings

1. Event 011 is reserved, Minor Fire-Once, and marked To Be Reworked.
2. No registered cluster contains Event 011. A planned Pacts cluster exists only as an unrelated catalog concept and should not absorb this event.
3. Existing scenario registry entries end before a Secret Alliance scenario. Implementation must inspect the live registry and assign the next valid stable ID.
4. Nearby event concepts already cover random alliances, non-aggression, intelligence leaks, counterintelligence, secret-society influence, and generalized tensions. Event 011 must remain distinct through a persistent player-targeted hidden coalition with a mandatory wartime reveal contract.
5. The event is large enough to touch events, decisions, scripted GUI, factions, scripted helpers, AI, achievements, assets, super-events, docs, scenarios, localisation, event logs, and the catalog workbook.
6. New tags and focus trees would reduce procedural compatibility and create unnecessary overwrite risk.

## Relevant catalog entries

| Catalog entry | Relationship | Design response |
| --- | --- | --- |
| 7 Fury | Includes a separate Fury Pact concept | Keep Event 011 procedural and target-specific, with no world-end branch |
| 8 Tensions Rising | General indirect pressure | Use optional later hook, do not duplicate broad world-tension mechanics |
| 52 Intel Leaked | Intelligence disclosure | Possible Evidence hook, not a prerequisite |
| 119 Random New Alliance | Public random alliance | Keep Event 011 hidden until reveal |
| 121 The Pact | Separate pact concept | Avoid reusing its identity without explicit cross-event design |
| 125 Non-Aggressions | Treaty behavior | Potential diplomatic context only |
| 146 Add operative | Operative content | Can improve target counterintelligence later |
| 147 Counterintelligence | Defensive intelligence | Natural optional integration point |
| 150 Secret Society Influence | Hidden influence | Keep separate from state-led coalition membership |

## Likely implementation surfaces

- `events/011_secret_alliance.txt`, proposed event-owned file
- event registration and random-selection effects
- event-owned on-action or paced runtime hook
- scripted effects and triggers for selection, membership, operations, reveal, values, and cleanup
- event-owned script constants
- event-owned decisions and categories
- event-owned scripted GUI and interface art
- faction creation and dynamic localisation
- event log, event details, and evolution log mapping
- AI strategies and decision weights
- ideas or dynamic modifiers for staged pressure and reveal conversion
- achievements registry and tracking
- super-event slot, GFX, scripted localisation, audio, and music docs
- triggerable-scenario registry, effects, GUI, and docs
- `docs/events/011_secret_alliance.md`
- event asset manifest and GFX handoff
- event catalog workbook after final localisation exists

## Recommended dependency order

1. Confirm existing repo patterns and final identifiers.
2. Design and implement helpers, constants, membership storage, and cleanup.
3. Implement entry selection and baseline operations.
4. Implement evolutions and logging.
5. Implement the decision category and AI equivalents.
6. Implement reveal convergence and coalition war conversion.
7. Implement scenario launch.
8. Produce and wire assets and super-event audio.
9. Implement achievements and final localisation.
10. Reconcile docs, workbook, audits, and improvement-loop disposition.

## Main risks

- leaking hidden membership through localisation, flags, tooltips, event targets, or AI behavior
- selecting a country that cannot safely join the eventual faction
- attempting to pull a country from an incompatible faction without valid handling
- missing the hard reveal path when war begins through guarantees or faction calls
- stale members remaining in the automatic war loop
- global on-action performance from broad country scans
- a human country being assigned to the pact without consent
- dynamic faction-name grammar failures
- baseline stages being logged as evolutions
- disabled evolutions setting flags needed by later content
- excessive decision clutter or passive political-power stores
- final super-event audio remaining unlicensed or reused
- workbook wording being updated before final in-game localisation exists

## Recommended next action

The implementation parent should begin with a narrow repository exploration pass for existing faction-creation, event-target array, selected-target decision, scenario-registry, super-event, and event-log precedents. It should then implement the scripted architecture before writing repeated event blocks.
