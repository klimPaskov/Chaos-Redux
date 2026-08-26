# Event 006 evolution registry merge

Date: 2026-08-26

Scope: source-layout consolidation of the Event 006 evolution effect registry and its documentation only.

The paid incident-resolution effects previously lived in common/scripted_effects/006_independence_wave_evolution_incident_effects.txt. They now live at the end of common/scripted_effects/006_independence_wave_evolution_effects.txt, beside the five canonical evolution transition effects.

The source body was copied without semantic edits. The 11 public effect identifiers are independence_wave_change_revisionist_pressure, independence_wave_resolve_replicable_institution_compact, independence_wave_resolve_replicable_recognition_campaign, independence_wave_resolve_dormant_charter_settlement, independence_wave_resolve_dormant_pluralist_compact, independence_wave_resolve_armed_civilian_command, independence_wave_resolve_armed_frontier_mobilization, independence_wave_resolve_congress_rights_charter, independence_wave_resolve_congress_secretariat_compromise, independence_wave_resolve_open_synchronized_claims, and independence_wave_resolve_open_containment_diplomacy.

Validation compared the former source body to the appended target block after line-ending normalization and found exact equality. The target contains no duplicate top-level effect identifiers. The Event 006 allocator, country API, strict flag, FORM-16, SCN-008 scenario, and Statehood Ledger GUI source-matrix validators all passed after the merge.

Removed parser/doc files:

- common/scripted_effects/006_independence_wave_evolution_incident_effects.txt
- common/scripted_effects/006_independence_wave_evolution_incident_effects.md

Updated documentation:

- common/scripted_effects/006_independence_wave_evolution_effects.md
- docs/events/006_independence_wave/evolutions.md
- docs/plans/006_independence_wave_plans/006_source_of_truth_map.md
- docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md

No gameplay identifiers, event wiring, decisions, triggers, localization, assets, package admission, or runtime claims changed.
