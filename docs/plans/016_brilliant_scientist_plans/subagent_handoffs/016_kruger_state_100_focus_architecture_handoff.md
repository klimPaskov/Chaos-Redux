# Event 016 Kruger State 100-focus architecture handoff

Date: 2026-07-16

Subagent: `krg_focus_tree_architect`

Mode: read-only gameplay research plus documentation output. No gameplay, localisation, AI, GFX, map, spreadsheet, or asset file was edited.

## Outcome

The exact 100-focus architecture is in:

- `docs/plans/016_brilliant_scientist_plans/016_kruger_state_100_focus_architecture.md`

It provides unique IDs, authored coordinates, durations, prerequisite grouping, mutual exclusions, `allow_branch` versus live `available` gates, concrete rewards, exact live helper calls, new narrow helper requirements, AI weights, route-specific AI-plan ownership, idea lifecycles, decision/event hooks, project-derived force gates, origin behavior, anti-snowball brakes, terminal exclusivity, and an exact count proof.

This is an implementation handoff. It is not a focus-tree source file and does not claim that any of the 100 focuses are implemented.

## Architecture summary

| Surface | Design result |
| --- | --- |
| Total focuses | Exactly 100, numbered 001 through 100 |
| Formation origins | Charter, rebellion, enclave, and institutional takeover have fixed `allow_branch` opening nodes and converge through common audits |
| Political identities | Sovereign Directorate, Human Scientific Republic, Replicated Sovereignty, Machine Ascendancy, Temporal Continuum, Xenobiological Ascendancy, and Project Synthesis |
| Persistent foundations | Laboratory economy, physical supply, conventional army, engineers, air defense, counterintelligence, diplomacy, and integration |
| Project armies | Separate cloning, robotics, Paleogenetics, Xenobiological Synthesis, portal, temporal, alien-arms, and biological routes, all gated by actual history and physical capacity |
| Paleogenetics/Xenobiology | Separate facilities, resources, production, units, failures, AI, and counters; convergence only through the explicit Synthesis capstone |
| Former host | Charter compact, rebellion war/archive recovery, enclave ceasefire/corridor, and takeover resistance/exile cleanup are distinct |
| Expansion | One evidence-backed corridor/facility/resource target at a time, followed by route-specific integration and an overextension brake |
| Regional ending | Continental Laboratory Network remains the capstone when Evolution IV is disabled |
| Laboratory World | A 140-day doctrine commitment that unlocks administration/submission work; it cannot fire the terminal by itself |
| Strategic Singularity | A 140-day doctrine commitment that unlocks six native component projects, multi-site construction, a separate 365-day arming clock, intelligence stages, raids, disarmament, surrender, and temporal escape |

## Required sources read

### Repository guidance and skills

Read completely before authoring:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-event-planning/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`

The additional decision/event skills were necessary because most focus payoffs are decision, mission, event, and project-board unlocks rather than direct modifier grants.

### Event 016 source pack

Read all ten spec parts under `docs/specs/016_brilliant_scientist_specs/specs/`, with particular attention to:

- Part 5, country formation, identities, inherited forces, economy, and former host.
- Part 6, focus-tree lanes and route depth.
- Part 7, AI, foreign reactions, former-host priorities, and target selection.
- Part 8, Laboratory World, Singularity, disarmament, terminal cleanup, and aftermath.

Read the binding matrices and acceptance surfaces:

- `matrices/016_ai_behavior_matrix.md`
- `matrices/016_country_package_matrix.md`
- `matrices/016_decision_mission_map.md`
- `matrices/016_focus_tree_architecture.md`
- `matrices/016_project_family_matrix.md`
- `matrices/016_route_coverage.md`
- `acceptance/016_acceptance_criteria.md`
- `acceptance/016_balance_and_exploit_review.md`
- `acceptance/016_parent_depth_and_anti_bloat_review.md`

Read the source-of-truth and current implementation handoffs, especially:

- `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md`
- `docs/plans/016_brilliant_scientist_plans/016_brilliant_scientist_resume_packet.md`
- `subagent_handoffs/016_project_reuse_identifier_map.md`
- `research/016_repo_inspection_notes.md`
- `research/016_source_reading_ledger.md`

### Offline Paradox wiki

Consulted the required offline snapshot only, not the web Paradox wiki:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- National focus modding

The most important focus findings were OR semantics inside one prerequisite block, AND semantics across separate blocks, `allow_branch` layout timing, live `available` evaluation, bypass behavior, completion-reward timing, mutual exclusions, focus AI weighting, and AI strategy-plan sequencing.

### Official vanilla documentation

Consulted:

- `documentation/script_concept_documentation.md`
- `documentation/effects_documentation.md`
- `documentation/triggers_documentation.md`
- `common/script_constants/documentation.md`
- `common/decisions/_documentation.md`
- `common/on_actions/_documentation.md`
- `common/special_projects/projects/documentation.md`
- `common/special_projects/special_projects_documentation.md`

The Special Projects documentation confirms that native projects should own prototype clocks and static specialization/facility contracts. The focus plan therefore unlocks or connects projects and decisions rather than running a second focus-owned project clock.

## Vanilla precedents

### Ethiopia focus tree

Source: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/ethiopia.txt`.

Relevant precedent:

- `ETH_the_american_radio_address` uses `allow_branch` for a fixed host/origin fact and `available` for the live government-in-exile state. This supports fixed formation origins in `allow_branch` and live facility/resource/crisis conditions in `available`.
- Ethiopia's military and economic branches use mutually exclusive policy choices that later reconverge through an OR prerequisite block.
- Its exile and survival content supplies the closest vanilla structural precedent for a weak enclave that must operate through patrons, legitimacy, intelligence, and supply rather than receiving generic power.

AI plan source: `common/ai_strategy_plans/ETH_alternate_strategy_plan.txt`. It demonstrates an exact ordered `ai_national_focuses` sequence guarded by an enable condition.

### Italy focus tree

Source: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/italy.txt`.

Relevant precedent:

- `ITA_the_abyssinian_fiasco` uses fixed branch visibility, mutual exclusion, live availability, and layout offsets without granting obsolete-route rewards.
- Italy's industrial and army branches demonstrate separate prerequisite blocks for AND, one prerequisite block for OR convergence, route exclusions, targeted state construction, decision unlocks, and staged idea swaps.
- The tree's long political alternatives show why KRG identity ownership should be handled through route strategy plans instead of loose per-focus probability alone.

AI plan source: `common/ai_strategy_plans/ITA_alternate_strategy_plan.txt`. It demonstrates route-specific focus ordering and `focus_factors = 0` for incompatible identities.

## Live Event 016 APIs inspected

### Country and route state

- `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt`
  - active KRG, four formation origins, every project route seed, mixed-route count, and actual nonhuman-state test.
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`
  - both existing `load_focus_tree` calls for `brilliant_scientist_kruger_state_focus_tree`.
  - exact route-forming effects and one-for-one idea lifecycle effects.
  - the current five-liability formation package.
- `common/ideas/016_brilliant_scientist_country_ideas.txt`
  - administration, portfolio, command, supply, and scientific-population lifecycles.

### Project and force state

- `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt`
  - exact Prototype, Deployment, Weaponization, physical facility, control-mode, biological-agent, and package guards.
- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`
  - idempotent runtime rebuild versus one-time formation materialization.
  - the explicit warning that rebuild creates no units or stockpiles.
  - bounded formation spawn helpers that the focus tree must never call.
- `common/script_constants/016_brilliant_scientist_project_force_constants.txt`
  - force ceilings, formation quantities, production/equipment burdens, and combat roles.
- `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`
  - exact project-board, capacity, stage, facility, incident, and Singularity gates.
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt`
  - stage application, native prototype synchronization, accidents, and component ledgers.

### Temporal and terminal state

- `common/scripted_triggers/016_brilliant_scientist_triggers.txt`
  - bounded temporal readiness, stabilization, origin evidence, terminal commitment, Singularity readiness, failsafe, and Laboratory World readiness.
- `common/scripted_effects/016_brilliant_scientist_effects.txt`
  - anchor registration/loss, target binding, immutable use records, synchronization/debt/scars, stabilization, origin conclusion, terminal commitments, and final preparation markers.

## Design decisions that should not be weakened

1. A focus never calls `brilliant_scientist_apply_project_force_package_from_history`, a `brilliant_scientist_spawn_*_project_force` helper, or direct `create_unit` for a project family.
2. A project focus may call only the runtime rebuild after the exact stage and physical facility gates pass. Ongoing formations come from paid decisions under the existing cap.
3. Paleogenetics and Xenobiological Synthesis retain separate state markers and logistics after political Synthesis.
4. Temporal focuses expose systems and unlock actions. They never refresh synchronization, passively reduce debt, erase scars, clear used-target IDs, or authenticate an anchor by capture.
5. Focus 098 refreshes global threat from actual state and cannot set it unconditionally.
6. Focus 099 commits Laboratory World but terminal firing remains gated by overwhelming control, integration, administration, submission, chaos, and major-opposition checks.
7. Focus 100 commits Singularity but the six native components, facility network, construction, arming, doctrine, intelligence exposure, disarmament, and canonical Fallout bridge remain separate gameplay.
8. Disabled Evolution IV hides 098-100 and leaves 097 as a regional-state capstone.

## Validation performed

- Parsed all ledger rows from the architecture: 100 rows, numbers 001 through 100, no missing number.
- Parsed all focus IDs: 100 unique `KRG_*` IDs, no duplicate.
- Compared those 100 planned focus IDs against the 34 current `KRG_*` identifiers under `common/`, `events/`, `history/`, and `localisation/`: no exact collision.
- Parsed all authored coordinates: 100 unique coordinate pairs, no collision in the authored ledger.
- Checked all 100 ledger rows against the seven-column Markdown schema; every row has the expected column count.
- Counted lane totals: 10 + 20 + 10 + 7 + 6 + 6 + 6 + 6 + 5 + 6 + 6 + 5 + 4 + 3 = 100.
- Called the read-only HOI4 focus inspector for `brilliant_scientist_kruger_state_focus_tree`. It returned `FOCUS_TREE_NOT_FOUND`, confirming that the loaded tree ID has no current source file and that this task did not accidentally overlap an existing implementation.

No focus render or source lint can be meaningful until the tree is implemented. The coordinates therefore require a render/inspect pass during gameplay implementation.

## Risks and blockers for the parent

1. The country package currently adds five simultaneous visible liability ideas. The focus-tree skill prefers at most three focus-created spirits. The architecture only swaps these one-for-one, but the parent must decide whether the formation presentation is consolidated into three visible composite slots or retained as an explicit exception. This is not silently resolved here.
2. `brilliant_scientist_form_sovereign_directorate` is required for the direct-rule capstone and does not exist.
3. `brilliant_scientist_can_unlock_synthesis` and `brilliant_scientist_unlock_synthesis` were reserved by the project identifier map but are not implemented.
4. Project seed changes currently do not call `mark_focus_tree_layout_dirty`. Dynamic branch visibility will be stale without that hook.
5. The seven KRG decision categories in the architecture are not implemented. Focus rewards must not be replaced with generic flat modifiers while those mechanics are absent.
6. Final focus icons, localisation, AI strategy plans, terminal intelligence events, and balance observations are absent.
7. The current workspace is heavily dirty from parallel work. The two documentation files in this handoff should be reviewed and committed by the parent without staging unrelated files.

## Suggested parent implementation order

1. Review the five-idea/three-spirit presentation decision and the three missing helper contracts.
2. Implement the tree shell with all 100 IDs, coordinates, prerequisites, mutual exclusions, branch gates, icons placeholders only if approved assets already exist, and no rewards yet.
3. Run `hoi4.focus_inspect` and `hoi4.focus_render`; correct collisions and connector crossings while preserving authored lane ownership.
4. Implement opening, economy, conventional security, and diplomacy categories first so every origin can survive without a project branch.
5. Implement project lanes one family at a time using exact stage/physical gates and paid force decisions.
6. Add route AI strategy plans and validate weak enclave, charter, rebellion, takeover, and each project-dominant AI case.
7. Implement expansion/integration, then the two terminal commitments and their counterplay.
8. Run the focus-tree auditor and country-package auditor before any completion claim.

## Skill report

Used:

- `hoi4-focus-trees`
- `chaos-redux-event-planning`
- `chaos-redux-subagents`
- `hoi4-decisions-missions`
- `chaos-redux-events`

No skill was created or modified. No gameplay implementation or fallback was produced.
