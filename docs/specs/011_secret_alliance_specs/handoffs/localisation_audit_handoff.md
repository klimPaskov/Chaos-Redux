# Localisation planning audit handoff

Status: historical planning audit. Final Event 011 localisation is implemented with SHA-256 prefix `6A42CEFE`; the current FINAL CLEAN report is `docs/plans/011_secret_alliance_plans/subagent_handoffs/localisation_audit.md`.

## Audit status

No in-game localisation was edited in this planning task. The spec intentionally provides direction and working labels rather than pasteable final copy. This handoff defines the localisation risks and required coverage for implementation.

## Secrecy boundary

Before public reveal, player-facing text must not use:

- Secret Alliance
- pact member
- coalition member
- Anti-[target] Pact
- hidden doctrine
- Cohesion
- Readiness
- founder
- sponsor, unless a major's role has been publicly exposed

Permitted public terms include:

- foreign interference
- coordinated incidents
- linked methods
- suspected liaison network
- unexplained access arrangements
- possible common planning
- confirmed participant, only after proof

Evolution II may make it clear that organization exists. It must not automatically reveal who belongs to it.

## Dynamic text requirements

Final text needs dynamic handling for:

- target country name and adjective
- grammatical faction-name fallback
- selected suspect name and flag
- confidence band
- recent operation type
- named state or region in missions
- Evidence and Preparedness as integer values or clear bands
- War Pressure and Coalition Resolve after public reveal
- confirmed member count
- major sponsor and faction leader when public
- scenario type and intensity
- mission timer and current requirement status

## Required text surfaces

- entry and incident event titles, descriptions, and options
- internal events shown to human candidates
- news event for public coalition formation
- event name, debug name, and Event Details description
- three evolution names and detail directions
- decision category names and descriptions by phase
- every decision and mission title, description, cost, blocked cost, requirement, success, partial success, and failure text
- scripted GUI labels, meter tooltips, suspect-card confidence, recent-operation status, warning state, and close or select actions
- ideas and dynamic modifiers
- faction dynamic name and fallback
- scenario name, detail, types, intensity impact, confirmation, and result event
- achievements
- super-event title, description, button remark, and quote
- postwar settlement and faction dissolution text
- docs and workbook mirror fields

## Cross-surface wording rules

- Event Details and the workbook Details field describe the premise and visible situation, not effects.
- Evolution detail wording must match the in-game evolution view.
- The scenario detail must explain that it creates an immediate coalition and war without describing bypass flags.
- Achievement descriptions state player requirements, while ordinary event text does not advertise achievement paths.
- The faction name must remain the same in news, super-event, diplomacy, event log, and documentation.
- Confidence-band terms must remain stable across decisions, GUI, events, and tooltips.

## Tooltip requirements

Use custom tooltips for:

- candidate validity and why no target exists
- nonstandard equipment, XP, fuel, train, convoy, factory, unit-position, access, and credibility costs
- suspect confidence and accusation risk
- reveal consequences
- member-turn conditions
- border-conflict escalation risk
- scenario composition bands
- Preparedness conversion and maintained-project expiry

Do not expose raw trigger blocks.

## Tone direction

- Baseline incidents should be concrete, uneasy, and incomplete.
- Evolution II text can be sharper and more violent, but should not announce hidden formulas.
- Evolution III text should communicate visible preparation and public alignment.
- Democratic, fascist, communist, and non-aligned targets may receive different institutional voices without creating four unrelated systems.
- Severe incidents avoid cheap comedy.
- Options can use restrained irony, period idiom, or bureaucratic self-importance when it fits the actor.
- Avoid em dashes, semicolons, staccato dramatic fragments, contrast formulas, and generic apocalypse wording.

## Super-event text

Use the researched quote and button candidates only after final source and UI review. The final title remains a research and localisation task. Do not convert an asset key or working route label into the title.

## Implementation audit checks

The localisation auditor should verify:

- no hidden-member reveal in keys visible before confirmation
- no duplicate keys
- correct namespaces
- UTF-8 with BOM
- no raw variable decimals where integer display is intended
- no missing decision, mission, GUI, achievement, scenario, faction, idea, event-log, or super-event keys
- no stale use of Secret Alliance in public pre-reveal text
- exact workbook mirror wording after implementation
