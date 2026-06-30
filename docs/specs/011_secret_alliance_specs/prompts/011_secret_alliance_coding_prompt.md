# Coding prompt for Event 011 Secret Alliance

Implement Event 011 according to the full source spec package:

`docs/specs/011_secret_alliance_specs/`

Read and follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-planning`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-subagents`, and the relevant subagent handoff in this package.

## Required implementation scope

- Event root `chaosx.nr11.1` and follow-up events.
- Hidden pact state for three founding minor members.
- Candidate scoring and eligibility checks.
- Evolution I, II, and III active-event paths.
- Pre-fire evolved openings for Evolution II and III as defined in the spec.
- Hidden invitation behavior.
- Major patron behavior.
- Immediate reveal when any hidden member enters war with the target.
- Public faction named `Anti-[target country] Pact` after reveal.
- War calls for valid public members when reveal is war-caused.
- Decision category and missions from the decision spec.
- Dossier Board scripted GUI if the implementation pass accepts the UI plan.
- Static and animated asset package handoff and final wiring.
- Conditional reveal super-event package when reveal meets the campaign weight gate.
- Achievement tracking and icons.
- Event log, Event Details, history, evolution entries, docs, and spreadsheet alignment.
- AI behavior for members, patron, target response, and neutral reactions.

## Implementation rules

Use dynamic values and shared helpers. Avoid scattered magic numbers. Centralize tuning in script constants where supported. Use event targets carefully and clean persistent global targets. Use reusable scripted effects and triggers for candidate scoring, member iteration, reveal logic, member cleanup, and decision availability. Write dynamic localisation for values that the player sees.

Do not provide fallbacks, shortcuts, placeholder assets, or simplified mechanics without reporting them and getting approval. Do not claim completion until all mapped systems and audits are done.

## Text and research gates

The spec gives direction only. Write final player-facing localisation during implementation. Do not paste working labels as final text. Source-dependent super-event titles, button text, quote, cultural remark, and audio are blockers until researched by the super-event workflow.

## Required audits before completion

- `chaosx_scripted_system_architect` for helper and constants design.
- `chaosx_decision_mission_auditor` after decisions and missions.
- `chaosx_localisation_auditor` after visible text exists.
- `chaosx_event_completion_auditor` before claiming complete.
- Asset subagents for generated icons, UI assets, event images, and animation packages.
- Super-event text and audio subagents if the reveal super-event is implemented.

## Completion report

Report changed files, mechanics implemented, event log and evolution wiring, decision and mission behavior, AI behavior, assets, super-event state, achievements, spreadsheet row status, validation scenarios, simplifications, and blockers.
