/goal Implement the Condemnation Impact System expansion to its fullest extent.

Read and follow AGENTS.md, CHAOS_REDUX_MECHANICS.md, all repo skills, and all custom subagent TOMLs before editing. Use the full spec at docs/specs/condemnation_impact_system_spec.md or the provided file condemnation_impact_system_spec.md as the source of truth.

Treat this as a standalone system-level mechanic. Condemnation must stop being mainly an opinion modifier. High condemnation must create practical diplomatic, economic, military, and trade consequences, including real embargo relationships where HOI4 supports them.

Implement tiered condemnation sanctions: concern, formal censure, arms embargo, strategic embargo, total embargo, and pariah state. Track source-aware condemnation from chemical warfare, biological warfare, nuclear and thermonuclear strikes, camp and atrocity discovery, restricted chemical sites, coverups, and repeated use. Use script constants or a documented tuning file for thresholds, caps, decay, participant scoring, AI weights, duration bands, and scaling values.

Build real player and AI counterplay. Condemned targets need compliance, inspections, stockpile destruction, compensation, non-use pledges, observer access, defiance, autarky, black market procurement, sanction busting, and pledge-breaking consequences where supported by the spec. Sanction participants need enforcement, abstention, humanitarian carve-outs, quiet breach, exposure, shielding, sanction fatigue, and trade-dependency costs.

Do not use political power or command power as the default cost. Use equipment, factories, convoys, fuel, stability, war support, intelligence exposure, trade dependency, stockpile destruction, production strain, timed non-use, route access, and other concrete costs where the spec calls for them. Command power may be used only for limited security or military coordination actions and must stay conservative.

Update the Condemnation tab or related UI so the player sees total score, tier, source breakdown, active sanctions, participant count, next threshold, decay state, compliance state, and current practical penalties. Add scripted localisation and clear tooltips. Avoid raw trigger spam and unreadable requirement blocks.

Implement AI for condemned targets, sanction participants, faction leaders, neutral traders, subjects, and high-condemnation hypocrites. AI must be able to sanction, abstain, shield, comply, defy, or break sanctions based on ideology, faction, subject status, trade dependency, strategic resource dependency, war state, target strength, distance, recent source severity, own condemnation, sanction fatigue, and world tension.

Keep affected docs aligned, including CHAOS_REDUX_MECHANICS.md, a dedicated condemnation sanctions system doc, and any chemical warfare, biological warfare, camps, genocide, restricted site, Chaos Warfare, UI, and asset docs touched by the implementation. Do not guess player-facing records that must mirror final localisation.

Use chaosx_scripted_system_architect for reusable helper, trigger, constant, cleanup, and tuning design when needed. Use chaosx_decision_mission_auditor for the decision and mission layer. Use chaosx_localisation_auditor for broad visible text and dynamic tooltip work. Use the available read-only completion auditor for final spec-versus-implementation review. Spawn chaosx_improvement_loop_planner with fork_context=false near completion and resolve its addendum or closure handoff before final completion.

Do not claim completion until actual sanctions, real embargoes where supported, AI, UI, localisation, cleanup, docs, and meaningful validation scenarios satisfy the spec. No fallbacks, placeholders, simplifications, or cosmetic-only substitutes are allowed without explicit user approval.
