/goal Implement the Condemnation Impact System expansion to its fullest extent.

Read AGENTS.md, CHAOS_REDUX_MECHANICS.md and applicable owner skills. Use docs/specs/condemnation_system_specs/specs/condemnation_impact_system_spec.md and its recorded acceptance boundary. The 2026-09-20 tuning amendment controls conflicts. Keep unsupported broader acceptance unresolved.

Treat this as a standalone system-level mechanic. Condemnation must stop being mainly an opinion modifier. High condemnation must create practical diplomatic, economic, military, and trade consequences, including real embargo relationships where HOI4 supports them.

Implement tiered condemnation sanctions: concern, formal censure, arms embargo, strategic embargo, total embargo, and pariah state. Track source-aware condemnation from chemical warfare, biological warfare, nuclear and thermonuclear strikes, camp and atrocity discovery, restricted chemical sites, coverups, and repeated use. Use script constants or a documented tuning file for thresholds, caps, decay, participant scoring, AI weights, duration bands, and scaling values.

Build real player and AI counterplay. Condemned targets need compliance, inspections, stockpile destruction, compensation, non-use pledges, observer access, defiance, autarky, black market procurement, sanction busting, and pledge-breaking consequences where supported by the spec. Sanction participants need enforcement, abstention, humanitarian carve-outs, quiet breach, exposure, shielding, sanction fatigue, and trade-dependency costs.

Use the spec's concrete costs and conservative coordination prices. Political power or command power must not become the default cost for every action. Preserve existing resource types where the accepted amendment requires them.

Preserve the Condemnation tab layout. Make country entries clickable to open details containing total, tier, sources, sanctions, participants, thresholds, decay, compliance and practical penalties. Use scripted localisation, clear tooltips and the scripted-GUI skill with matching MCP evidence. Shared system UI remains parent-owned.

Implement AI for condemned targets, sanction participants, faction leaders, neutral traders, subjects, and high-condemnation hypocrites. AI must be able to sanction, abstain, shield, comply, defy, or break sanctions based on ideology, faction, subject status, trade dependency, strategic resource dependency, war state, target strength, distance, recent source severity, own condemnation, sanction fatigue, and world tension.

Keep affected docs aligned, including CHAOS_REDUX_MECHANICS.md, a dedicated condemnation sanctions system doc, and any chemical warfare, biological warfare, camps, genocide, restricted site, Chaos Warfare, UI, and asset docs touched by the implementation. Do not guess player-facing records that must mirror final localisation.

Use chaosx_scripted_system_architect for reusable helper, trigger, constant, cleanup, and tuning design when needed. Use chaosx_decision_mission_auditor for the decision and mission layer. Use chaosx_localisation_auditor for broad visible text and dynamic tooltip work. Use chaosx_event_completion_auditor for final review. Follow chaos-redux-subagents with self-contained prompts and Codex fork_turns="none". Use chaosx_ai_probability_auditor for weighted baseline and matching comparison. Resolve the improvement-loop planner's previous addendum before another pass and its accepted findings before completion.

Do not claim completion until actual sanctions, real embargoes where supported, AI, UI, localisation, cleanup, docs, and meaningful validation scenarios satisfy the spec. No fallbacks, placeholders, simplifications, or cosmetic-only substitutes are allowed without explicit user approval.
