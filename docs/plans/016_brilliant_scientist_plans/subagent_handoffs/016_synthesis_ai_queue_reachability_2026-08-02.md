# Event 016 Synthesis AI queue reachability handoff

Date: 2026-08-02

Owner: `/root/event016_focus_content_pass`

Status: bounded AI focus-plan patch complete; no model, focus-source, localisation, or icon files changed.

## Scope and finding

The audit covered `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`, `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`, the Event 016 focus triggers/effects, focus localisation, and focus icon registration.

The Synthesis focus `KRG_the_project_synthesis` has two visible project prerequisites and an `available` gate requiring `has_completed_focus = KRG_define_the_states_purpose`. The dedicated `KRG_project_synthesis_plan` listed `KRG_the_project_synthesis` before `KRG_define_the_states_purpose`. HOI4 ordered national-focus plans advance through the list and skip unavailable entries; they do not revisit an earlier entry after a later focus makes it available. That order could therefore strand the mixed-family AI before its intended political convergence capstone.

## Changed file and identifiers

| File | Changed identifiers | Change |
| --- | --- | --- |
| `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` | `KRG_project_synthesis_plan`; queue entries `KRG_define_the_states_purpose`, `KRG_the_project_synthesis` | Reordered the queue so the required state-purpose focus is attempted before the Synthesis capstone. |

No focus IDs, focus costs, prerequisites, completion rewards, localisation keys, icon IDs, DDS files, decisions, or model assets were added or removed.

## Route coverage

| Route surface | Focus identifiers | Coverage |
| --- | --- | --- |
| Formation and survival | `KRG_audit_inherited_portfolio` through `KRG_complete_the_founding_audit` | Complete: root audit, four origin openers, survival/command branches, and founding-audit convergence. |
| Government and identity | `KRG_define_the_states_purpose` through `KRG_the_project_synthesis` | Complete: human, Sovereign Directorate, clone, machine, temporal, xenobiological, and Synthesis identity surfaces are present. |
| Economy and supply | `KRG_stabilize_the_laboratory_economy` through `KRG_sustainable_project_capacity` | Complete: power, transport, portfolio, prototype works, four supply doctrines, and OR convergence are wired. |
| Conventional security | `KRG_restore_the_ordinary_chain_of_command` through `KRG_a_council_of_project_commanders` | Complete: defectors, engineers, counterintelligence, air defence, and command-route exclusivity are represented. |
| Project lanes | `KRG_audit_the_growth_halls` through `KRG_the_replicated_host`; `KRG_wake_the_assembly_lines` through `KRG_an_army_of_machines`; `KRG_open_the_restoration_ledger` through `KRG_the_dinosaur_host`; `KRG_open_the_designed_organism_dossier` through `KRG_xenobiological_ascendancy` | Complete: clone, robotics, paleogenetic, and xenobiological lanes retain distinct prerequisites, counterplay, production, and route-forming effects. |
| Portal and temporal | `KRG_recover_the_transit_logs` through `KRG_the_continuity_guard` | Complete: terminal ownership, anchor authentication, synchronization/debt, stabilization, and bounded operations are gated. |
| Exotic and biological | `KRG_build_an_independent_reactor_grid` through `KRG_authorize_agents_of_last_resort` | Complete: high-energy delivery, interface requirements, containment, and authenticated biological/last-resort actions are present. |
| Diplomacy and integration | `KRG_a_state_without_friends` through `KRG_the_continental_laboratory_network` | Complete: recognition, intelligence, former-host settlement, commonwealth/submission, recovery, capacity, supply, and overextension checks are consumed. |
| Evolution IV and terminals | `KRG_evolution_four_sovereign_science`, `KRG_commit_to_the_laboratory_world`, `KRG_commit_to_the_strategic_singularity` | Complete: scenario gates and symmetric terminal mutual exclusion delegate readiness to canonical triggers. |

## Missing or simplified content

- No missing KRG route, focus ID, prerequisite target, mutual exclusion, project lane, terminal branch, or decision unlock was found in this bounded audit.
- The previous audit's “no dedicated Synthesis plan” finding is stale: `KRG_project_synthesis_plan` exists in the current AI source. This patch fixes its queue order rather than adding a duplicate plan.
- The four y2 opening focuses use OR `available` gates instead of visible prerequisite connectors. This remains semantically correct but is a UI clarity risk for a later polish pass.
- Global focus diagnostics still include 14 unrelated vanilla continuous-focus sprite/localisation entries from `game:common/continuous_focus/generic.txt`; no Event 016 diagnostic was reported.

## Icon coverage

| Surface | Result |
| --- | --- |
| Focus icon references | 100/100 unique `GFX_goal_KRG_*` IDs resolve in the focus source. |
| Regular sprites | 100/100 registered in `interface/016_brilliant_scientist_kruger_state_focus.gfx`. |
| Shine sprites | 100/100 registered in the same `.gfx` file. |
| DDS textures | 100/100 files under `gfx/interface/goals/016_brilliant_scientist/` resolve for the regular/shine pairs. |

No icon IDs changed.

## Localisation and reward mismatch list

- No title or description mismatch was found: 100/100 focus IDs resolve title and `_desc` keys in `localisation/english/016_brilliant_scientist_focus_l_english.yml`.
- All 100 `custom_effect_tooltip = KRG_*_effect_tt` references resolve in the same localisation file.
- No reward mismatch was found for the Synthesis route: the title describes political project convergence and its reward remains the route-forming synthesis effect.
- No localisation keys changed in this patch.

## AI behavior gaps and fix priority

| Priority | Status | Gap or action | File and identifiers |
| --- | --- | --- | --- |
| High | Fixed | The ordered plan now attempts `KRG_define_the_states_purpose` before `KRG_the_project_synthesis`, so the Synthesis `available` gate can be satisfied before the AI reaches the capstone. | `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`, `KRG_project_synthesis_plan` |
| Medium | Open | `KRG_takeover_consolidation_plan` ends at consolidation and relies on generic fallback for later identity/expansion priorities. Parent-owned weighted review can decide whether a post-audit handoff is warranted. | `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`, `KRG_takeover_consolidation_plan` |
| Medium | Open | Ordered-plan arbitration, mixed-family route flags, and terminal competition were not live-simulated. | All Event 016 KRG AI plans |

## Route behavior before and after

Before, the Synthesis plan queue reached `KRG_the_project_synthesis` while `KRG_define_the_states_purpose` was still incomplete, so the capstone was unavailable and could be skipped permanently by ordered-plan traversal. After, the queue reaches `KRG_define_the_states_purpose` first, then attempts `KRG_the_project_synthesis` with its non-obvious `available` requirement satisfiable when the project prerequisites and route trigger are also true.

## Validation

- Vanilla precedent reviewed: `common/ai_strategy_plans/ETH_historical_strategy_plan.txt` and `common/national_focus/ethiopia.txt` show ordered AI focus lists paired with explicit focus prerequisites and availability gates.
- `hoi4.focus_inspect` returned 100 focuses, 100 resolved titles, 108 connectors, zero crossings, zero node intersections, zero long connectors, zero same-row spacing violations, and zero KRG diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a572023467a2bc16ec0c780c3b77465a330ef4a6caeaf43cf7f83c7c15559f47/e302b5dcfdb01716a81a58d0fca5ff074a19c0df5f02646efd4c725ad8720327/focus-inspect.bf1c84282fdfc2bc.json`.
- `hoi4.focus_render` produced HTML, SVG, JSON, source-map, and plan artifacts with layout hash `2051c203ebb08be69fbdf861193ea1b0d14345c6f393f7f331809834c78e2633`. HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/509076cc5872dce5ce6587d3cd96a601e956aa65b90a272d40e145e00d236dbd/3f28809897069ba104f5b9878a002a24b50864fee457643623c3e6124ecdbcfc/brilliant_scientist_kruger_state_focus_tree.focus.html`.
- Static extraction confirmed 100 focus IDs, 100/100 title and description pairs, 100/100 effect tooltip keys, 100/100 regular sprites, 100/100 shine sprites, and 100/100 DDS files.
- A targeted queue check confirms `KRG_define_the_states_purpose` precedes `KRG_the_project_synthesis` inside `KRG_project_synthesis_plan`, and both IDs resolve in the focus source.

## Skipped validation and remaining risks

- No Hearts of Iron IV process was launched, as required by repository instructions. Live AI arbitration, focus selection, and transformed-host save behavior remain unproven.
- No `hoi4.focus_rewrite` was used because the focus source and layout were not changed; the patch is a one-line AI queue correction.
- No weighted-logic simulation was run because this change is deterministic queue ordering and requires live route-state combinations that were not available in this static pass.
- Remaining risks are the medium takeover handoff gap, the y2 availability-only UI clarity risk, and the 14 unrelated global vanilla diagnostics.

Handoff path: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_synthesis_ai_queue_reachability_2026-08-02.md`.
