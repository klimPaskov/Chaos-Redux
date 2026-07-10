# Event 011 Secret Alliance improvement-loop implementation handoff

Date: 2026-07-10.

## Disposition

Historical accepted-plan handoff. The mandatory post-implementation improvement pass found a bounded causal-depth gap and closed broad expansion. Its must-fix sections were accepted and are recorded as resolved in `../011_secret_alliance_improvement_resolution.md`.

This handoff no longer represents the current implementation verdict. At the time of this pass, the strict audits were incomplete. Later clean scoped freezes are recorded in `decision_mission_audit.md` for `b7965b7e` and `localisation_audit.md` for `087d66ab`. Gameplay candidate `c4bb10ce` postdates those freezes with later commitment and operation-dossier causality, and its final completion audit is still running.

Primary addendum:

- `docs/plans/011_secret_alliance_plans/011_secret_alliance_implementation_improvement_addendum.md`

## Sources reviewed

- `AGENTS.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-event-planning/SKILL.md`
- every file in `docs/specs/011_secret_alliance_specs/`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/scripted_system_architecture_pass.md`
- current Event 011 events, constants, scripted effects, scripted triggers, decisions, categories, ideas, AI strategies, faction template, on-actions, shared integration edits, and achievement entries
- required offline wiki pages and current vanilla documentation for events, decisions, triggers, effects, scopes, ideas, AI, on-actions, script constants, and faction templates, rules, and goals
- vanilla `on_war_relation_added`, `create_faction_from_template`, and `add_to_war` precedents cited by the architecture pass

## Must-fix findings accepted by this pass

1. Member motive needs commitment, role, and private-promise consequences.
2. The fixed pulse and generic operation list need an actor-owned, adaptive operation dossier and dynamic pacing.
3. Evidence needs classes, source deduplication, corroboration, false-lead recovery, and a curated three-suspect human surface.
4. Preparedness needs maintained components, real state or unit objectives, expiry, and working family caps.
5. Evolutions need recruitment and sponsor developments which the player can interrupt.
6. The revealed faction needs Event 011 goals, member roles, meaningful Resolve inputs, two-major leadership tension, and qualified postwar continuation.
7. AI and scenario types need role, geography, motive, resource, and validity behavior from the accepted matrices.
8. Achievement proof must use the stronger evidence, turned-channel, fracture, and immutable scenario facts.
9. The engine-safe corrections already listed in the scripted-system architecture pass remain mandatory.

## Implemented work which should not be replanned

- one fixed target and one active context
- exactly three automatic AI minor founders
- real public faction creation
- hostile-war reveal convergence through `on_war_relation_added`
- immediate existing-war entry for valid active members
- the accepted decision-family breadth and border-conflict boundary
- five scenario types and four intensity controls
- six registered Event 011 achievements
- one reveal super-event role
- the existing anti-bloat boundaries

## Parent action

Implement the must-fix tranches in dependency order:

1. member roles and commitment state
2. operation dossier and MTTH scheduler
3. evidence and suspect model
4. maintained Preparedness
5. evolution pacing
6. faction goals, Resolve, and postwar behavior
7. AI, scenario, and achievement fidelity
8. architecture compliance and task-specific validation

After each meaningful tranche, keep gameplay, localisation, UI, assets, docs, and achievement wording aligned through the owning skills and agents. The improvement planner should not be spawned again for Event 011 while this addendum remains unresolved.

## Optional future queue

- country-specific rivalry incident variants
- stable hooks to Events 052, 147, and 150
- deeper long-term content for a surviving postwar security bloc

These items do not block completion.

## Files changed by this planner

- `docs/plans/011_secret_alliance_plans/011_secret_alliance_implementation_improvement_addendum.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/improvement_loop_implementation_pass.md`

No gameplay, asset, localisation, spreadsheet, or source-spec file was edited.

## Remaining uncertainty

The final tuned thresholds, durations, and faction-goal progress formulas require implementation and scenario testing. This pass defines their inputs and behavior. It deliberately avoids fixed magic numbers and final player-facing localisation.
