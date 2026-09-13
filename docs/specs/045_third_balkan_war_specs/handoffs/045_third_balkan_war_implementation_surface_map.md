# Event 045 implementation surface map

This is a planning map. Final file names should follow existing repository ownership and current precedents after inspection.

## Event owner package

| Surface | Expected owner | Required content |
| --- | --- | --- |
| Entry and follow-up events | `events/045_third_balkan_war.txt` | entry, reports, role notifications, stage reports, settlement and aftermath events |
| Script constants | `common/script_constants/045_third_balkan_war_constants.txt` | stage bands, proof floors, support tiers, pacing, mission durations, AI anchors, registry ids |
| Scripted triggers | `common/scripted_triggers/045_third_balkan_war_triggers.txt` | event validity, regional eligibility, dispute validity, camp compatibility, stage proof, claim proof, Evolution gates, settlement gates |
| Scripted effects | `common/scripted_effects/045_third_balkan_war_effects.txt` | opening transaction, camp construction, war linkage, escalation registration, claim activation, support ledger, settlement, cleanup |
| On actions | `common/on_actions/045_third_balkan_war_on_actions.txt` | narrow event-owned reactions where direct hooks exist and bounded pulses where necessary |
| Decisions | `common/decisions/045_third_balkan_war_decisions.txt` | role-aware actions, selected-target decisions, missions, cleanup |
| Category | `common/decisions/categories/045_third_balkan_war_categories.txt` | one ordinary category with static picture and dynamic description |
| Ideas or dynamic modifiers | event-owned files only when needed | temporary mobilization, corridor, armistice, or settlement effects with complete lifecycles |
| Opinion modifiers | event-owned file | support, betrayal, occupation dispute, mediation, and settlement memories |
| AI strategy | event-owned AI files or owner helpers | camp commitment, containment, exploitation, surrender realism, wider-war posture |

## Shared event-system surfaces

| Shared surface | Required change |
| --- | --- |
| Event registration | classify Event 045 as Minor Fire-Once, level 1, and ready only after completion |
| Event name selectors | add final name and debug mapping |
| Event log actor mapping | choose a meaningful opening actor or camp leader |
| Event Details | premise, public stages, three Evolution previews, Chaos level, cluster status |
| Evolution logger | type, stage, tier, actor, enabled state, list and detail localisation |
| Cluster registry | Wars member, High severity, correct minimum tier and role |
| Settings manual event path | normal and Force Trigger behavior with validity and test bypass separation |

## Claim and map data

The implementation must inspect the installed map before freezing state groups. Use `hoi4.map_inspect` for the maintained regional groups and record the exact state and adjacency evidence. Put stable group identifiers in the Event 045 owner registry or the shared universal state registry only when another owner genuinely needs the same group.

Required families:

- Macedonia
- Aegean access and Western Thrace
- Serbian-Bulgarian frontier
- Kosovo, western Macedonia, and Albanian interests
- Southern Dobruja
- Transylvania and Partium
- Banat, Bačka, and Vojvodina
- Yugoslav successor disputes
- European Thrace and the Straits

## Decision presentation and assets

| Asset family | Final owner path direction |
| --- | --- |
| Category picture | `gfx/interface/decisions/045_third_balkan_war/` |
| Decision icons | `gfx/interface/decisions/045_third_balkan_war/` |
| Mission icons | event-scoped decision or mission icon folder following inspected precedent |
| Report and news images | `gfx/event_pictures/045_third_balkan_war/` |
| Super-event images | event-scoped super-event folder following current slot wiring |
| Achievement icons | root achievement folder with full achievement ids and three state files |
| Audio | `sound/045_third_balkan_war/` with one unique file for each super-event |

Every non-portrait asset uses the proper narrow asset worker. No runtime path may point into `docs/assets/` after completion.

## Localisation surfaces

- event titles, descriptions, options, and report text
- event name and Event Details selectors
- escalation stage names and concise cause or proof tooltips
- decisions, missions, costs, requirements, success, partial success, and failure
- claims, named regions, settlements, armistice, and postwar memories
- three Evolution names and descriptions across every log surface
- six achievement entries
- two super-event packages
- scripted localisation for role, stage, selected target, latest cause, missing proof, and settlement summary

All final player-facing text must follow the Chaos Redux writing rules and remain free of process notes, hidden variables, uncertain historical claims, and unsourced quotations.

## Achievements

Add all six definitions to the single Chaos Redux achievement registry. Reuse Event 045 ledgers for proof. Add tracking and cleanup in Event 045 owner effects, not in a detached parallel subsystem.

## Super-events and audio

Two complete packages are required:

1. the successful opening transaction
2. the verified Another World War handoff

Each needs a deliberate slot, title, description, button, verified quote, image, unique licensed musical audio, settings-aware playback, sound definitions, source documentation, audio catalog row, and event trigger.

## Documentation and spreadsheet

Expected permanent documentation:

- `docs/events/045_third_balkan_war/overview.md`
- system notes for opening, escalation, claims, intervention, settlement, Evolutions, AI, achievements, and validation as needed
- `docs/super_events/045_third_balkan_war_super_event_research.md`
- completion report under the event plan folder
- updated authoritative workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- regenerated CSV snapshots through the repository exporter

## Required specialist routing

- `chaosx_scripted_system_architect` for repeated owner helpers
- `chaosx_decision_mission_auditor` for the decision package
- `chaosx_ai_probability_auditor` for weighted surfaces before and after patches
- `chaosx_asset_source_researcher` and `chaosx_generated_event_art` for scene art according to source mode
- `chaosx_icon_artist` for decisions, missions, and achievements
- `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher`
- `chaosx_localisation_auditor`
- `chaosx_event_completion_auditor`
- `chaosx_spreadsheet_doc_worker` after final implementation wording exists

The event UI worker is out of scope because no dedicated scripted GUI is accepted.
