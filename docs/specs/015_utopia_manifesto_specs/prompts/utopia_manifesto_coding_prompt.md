# Utopia Manifesto coding prompt

Implement Event 015 `utopia_manifesto` from the full spec package under `docs/specs/015_utopia_manifesto_specs/`.

## Required source files

Read all spec parts, with special attention to:

- `specs/015_utopia_manifesto_spec_part_1_core.md`
- `specs/015_utopia_manifesto_spec_part_2_focus_tree.md`
- `specs/015_utopia_manifesto_spec_part_3_need_ledger_decisions.md`
- `specs/015_utopia_manifesto_spec_part_4_country_ai_evolutions.md`
- `specs/015_utopia_manifesto_spec_part_5_assets_achievements_acceptance.md`
- `specs/015_utopia_manifesto_spec_part_6_late_enforcement_and_puppet_utopias.md`
- all files under `matrices/`
- all prompt files under `prompts/`
- `prompts/utopia_manifesto_subagent_routing_prompt.md`

## Event contract

Replace old Event 15 World Tension Subsides completely. Register Event 15 as Minor Fire-Once with no cluster. Target eligible minors and player minors, excluding majors and strong industrial powers. AI always accepts. Human players can accept or refuse. Acceptance loads the full Utopian focus tree and starts the Need Ledger systems.

## Focus tree contract

Do not implement a shallow shared tree. The tree must be large, uneven, and route-driven. Major branches must not be five-focus lanes.

Implement:

- opening spine with manifesto reading, public or survey fork, household counts, stores, trades, roads, island question, first dossier, and route council
- public political routes for Free Household Compact, Morean Council, Surveyor State, and Good Place Mandate
- hidden Outopia route gated by Fracture, evolution, or late contradiction conditions
- domestic pillars for Bread and Stores, Chosen Work, Houses and Health, Plain Law and Education, Useful Land Care
- military and security branches for household defense, planned defense, mandate army, border works, auxiliary controversy, and arsenal of necessity
- diplomacy, expansion, and enforcement branches for Need Dossiers, Consent Charters, Protective Wardship, Needful War, and World Household Enforcement
- puppet utopia branch with subject forms, local values, subject decisions, and final fates
- Ultimate Utopia convergence branch where all mature branches connect into route-colored capstones

The final tree should preserve route interaction. Politics must change decisions, costs, subject behavior, expansion tools, and ultimate endings. Economy, military, diplomacy, and subject systems must feed the final convergence.

## Mechanics contract

Implement the Need Ledger with visible values for Common Stores, Vocational Freedom, Land Need, Outopia Fracture, and late subject values or compact equivalents. Subject values should cover Local Stores, Local Consent, Vocational Acceptance, Ledger Dependence, Ward Autonomy, and Fracture Import unless a technically equivalent compact presentation is used.

Land claims must depend on Need Dossiers and Land Need. They must decay, expire, or become renounceable when the need is solved or proven false. Do not use normal permanent claim spam or instant core spam.

Late decisions must let the host export, enforce, or renounce Utopia abroad through invitations, surveys, charters, protectorates, wards, needful wars, and subject settlement. Costs should use equipment, convoys, trains, trucks, fuel, factories, manpower, state control, compliance, resistance, local support, stability, war support, time, and map objectives. Political power and command power may support costs, but cannot dominate.

## Puppet utopias

Implement route-colored utopian subject forms such as Charter Commonwealths, Surveyor Protectorates, Necessary Wards, Daughter Commonwealths, and hidden No-Place Precincts. These subjects need visible mechanics, overlord and subject actions, support needs, instability, rupture risks, and final fates such as League member, daughter commonwealth, integrated ward, autonomous charter, direct ward, precinct, renounced partner, or failed ward.

## Assets, localisation, and research

Use the asset prompt for all required static and animated assets. Use the super-event prompt for quote, remark, image, and audio research. Do not treat unresearched working labels, quotes, titles, remarks, or audio choices as final localisation. Write final event, focus, decision, GUI, achievement, event-detail, and spreadsheet text from the direction in the specs.

## Subagents and validation

Follow AGENTS.md and all relevant skills. Use `prompts/utopia_manifesto_subagent_routing_prompt.md` for subagent order and ownership. Use project subagents with `fork_context=false` for assets, super-event research, focus audit, decision audit, country package audit, localisation audit, scripted-system helpers, spreadsheet update, documentation cleanup, improvement-loop review, and final completion audit.

## Mandatory near-completion improvement loop

When the goal is nearing completion, spawn `chaosx_improvement_loop_planner` with `fork_context=false`. This is mandatory after a meaningful implementation tranche and before the final completion audit. Give it the explicit event id, slug, source spec paths, implemented surfaces, current blockers, accepted plans, queued plans, rejected plans, user constraints, and the exact question it must answer about remaining shallow systems, disconnected mechanics, missing route depth, missing AI, missing asset states, missing aftermath, or scope bloat.

Resolve its output before claiming completion. If it writes an expansion addendum, implement it, fold it into `docs/specs/015_utopia_manifesto_specs/`, queue it with a reason, or reject it with a reason. If it writes a closure handoff because further expansion would add bloat, keep that handoff and finish only the final small tasks it lists. Do not skip this step because the event appears complete. If the loop subagent cannot be spawned because the tool is unavailable, record that as a blocker and do not claim full completion.

Before claiming completion, provide a route coverage table, subject mechanics coverage table, decision and mission coverage table, asset coverage table, AI behavior notes, improvement-loop disposition, docs and spreadsheet alignment notes, and a clear list of simplifications, omissions, blockers, unresolved loop items, or queued follow-up. If there are no simplifications, say so with evidence.
