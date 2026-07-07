# Event 013 Natural Disasters, final improvement-loop anti-bloat pass and closure handoff

This is a manual improvement-loop style closure handoff for the expanded planning package. It does not claim implementation completion. It records that broad design expansion is now sufficient for a coding pass, while naming boundaries that should prevent bloat.

## Depth check

| Surface | Status after second pass | Notes |
| --- | --- | --- |
| Reusable disaster system | Deep enough for implementation planning. | The call contract, season controller, family resolution, death scaling, damage scaling, reports, and aftermath ledger are specified. |
| Disaster family depth | Expanded. | Every family now has warning decisions, aftermath card values, AI priorities, report direction, news direction, state modifier direction, and chain routes. |
| Normal aftermath decisions | Expanded. | Rescue, stabilization, reconstruction, chain prevention, mission caps, partial success, and foreign relief are mapped. |
| Abnormal GUI | Expanded. | Window layout, card states, map layers, sprite targets, animation briefs, fallbacks, and interaction flow are mapped. |
| Super-event planning | Expanded to handoff matrix. | Research gates remain in place. No final titles, quotes, remarks, or audio are selected here. |
| Catalog and docs alignment | Added. | Spreadsheet and docs direction exists without final player-facing copy. |
| Related events | Constrained. | Event 046 placeholder, Event 099 bridge or placeholder, and Event 051 non-stacking rule remain preserved. |
| Implementation prompts | Refreshed. | Prompt files point implementation toward the second-pass additions. |

## Anti-bloat decisions

| Proposed expansion | Decision | Reason |
| --- | --- | --- |
| Full focus trees for disaster recovery governments | Reject. | Natural Disasters is a repeatable event system, not a country-creation event. Focus trees would distract from the reusable disaster engine. |
| New disaster relief country tags | Reject. | The event should damage and pressure existing countries. New tags would create map clutter and country-package obligations. |
| One super-event for every disaster family | Reject. | Super-events should be reserved for abnormal Evolution III or rare massive campaign moments. Family-level super-events would create spam and dilute impact. |
| Separate custom GUI for every normal disaster | Reject. | Normal disasters should use compact aftermath cards. The abnormal map is for moving or multi-state systems that need visual management. |
| Final localisation in the spec | Reject. | The planning skill requires direction-only localisation. Final text must be written during implementation and audited. |
| Public research quote selection in this package | Reject. | Super-event text and audio research must run through the super-event workflow with source verification. |
| Terminal world-end branch | Reject. | The source brief keeps Event 013 non-terminal. Abnormal disasters can be devastating without becoming a world-end scenario. |
| Turning Event 099 into a second sandstorm system | Reject. | It should become a placeholder or bridge into Event 013. Separate logic would duplicate the family system. |
| Reusing old Earth Earthquake logic | Reject. | Whole-earth rupture belongs in Event 013 Evolution III as fresh design. Event 046 stays placeholder. |
| Using only static UI for abnormal moving disasters | Reject as default. | Static fallback is required, but motion clarifies moving paths, impact queues, and warning states. |

## Remaining implementation obligations

| Obligation | Required owner or pass |
| --- | --- |
| Live repo file mapping and vanilla precedent checks | Main implementation, with `chaosx_repo_explorer` if file locations or patterns are unclear. |
| Reusable scripted effects, triggers, constants, targets, cleanup | `chaosx_scripted_system_architect` and parent review. |
| Decisions, missions, active caps, AI choices, cleanup, exploit review | Parent implementation and `chaosx_decision_mission_auditor`. |
| Localisation, dynamic values, report/news text, Event Details | Parent implementation and `chaosx_localisation_auditor`. |
| Icons, report images, news images, super-event images, UI assets, animations | Asset subagents by source mode and `chaos-redux-frame-animation`. |
| Super-event quotes, cultural remarks, audio | `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher`. |
| Docs and spreadsheet alignment | Documentation pass and `chaosx_spreadsheet_doc_worker` after final wording exists. |
| Completion audit | `chaosx_event_completion_auditor` before claiming implementation completion. |

## Closure recommendation

Broad planning expansion can stop here. Further planning before implementation would likely add noise unless the user asks for a very specific extra design surface. The package now has enough depth for a coding agent to begin implementation without inventing family mechanics, recovery mission structure, abnormal GUI behavior, super-event research roles, or catalog alignment.

The implementation agent should not treat this closure handoff as permission to simplify. It should treat the spec files, matrices, prompts, and this anti-bloat pass as acceptance criteria. Any simplification, missing asset, missing AI behavior, missing report, missing aftermath notification, missing Deaths-system integration, missing super-event research package, or placeholder must be reported clearly.
