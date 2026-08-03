# Event 016 KRG focus-tree final static audit

Date: 2026-08-03

Owner: `/root/event16_focus_audit_final`

Scope: read-only audit of the Kruger State focus tree and its Event 016 decision, project, AI, localisation, and icon integration. No gameplay files were changed and no commit was created.

## Result at a glance

The KRG tree is present as 100 unique focuses with no unresolved focus-reference targets, complete focus localisation, complete icon wiring, and 19 current AI route plans. The implementation covers every route named by the Event 016 focus architecture. The remaining risks are live route/AI/scenario validation and a few intentional presentation simplifications, not a missing focus branch.

Static checks in this audit found 100 focus blocks, 100 unique focus IDs, zero unresolved `has_completed_focus` references, zero missing title/description/effect-tooltip keys, 100 normal sprites, 100 shine sprites, 100 DDS files, 19 AI plan blocks, and zero KRG focus IDs omitted from the AI plan file.

The earlier `016_focus_runtime_audit_handoff.md` is superseded for AI details: it predates the current 19-plan file and its 2026-08-03 launch-error fix. The current AI file uses `allowed = { NOT = { original_tag = DJX } }` on all 19 plans and carries the dynamic KRG identity check in each `enable` block (`common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt:22-543`).

## Route coverage

| Required route or lane | Implemented focus IDs | Static result and remaining risk |
| --- | --- | --- |
| Survival and four formation origins | `KRG_audit_inherited_portfolio` through `KRG_complete_the_founding_audit` (001-010) | Implemented. Four origin openers are route-gated and converge at the founding audit. Formation transfer and cleanup still need parent-owned live scenarios. |
| Government and sovereign identity | `KRG_define_the_states_purpose` through `KRG_the_project_synthesis` (011-030) | Implemented. Human, directorate, replicated, machine, temporal, xenobiological, and synthesis identity gates are present. Pairwise identity mutexes are represented by the shared identity-lock helper rather than a large static mutex set. |
| Economy and supply doctrine | `KRG_stabilize_the_laboratory_economy` through `KRG_sustainable_project_capacity` (031-040) | Implemented. Supply doctrines use an OR choice and maintenance/facility checks; live balance and failure timing remain unverified. |
| Conventional security | `KRG_restore_the_ordinary_chain_of_command` through `KRG_a_council_of_project_commanders` (041-047) | Implemented. Command, officer, counterintelligence, airspace, staff, and project-command lanes are wired through focus unlock consumers. |
| Cloning | `KRG_audit_the_growth_halls` through `KRG_the_replicated_host` (048-053) | Implemented. Project stage/history and force checks are present. AI law choice between `KRG_clones_are_citizens` and `KRG_clones_are_cohorts` needs a live preference sweep (`...focus.txt:483,508`; `...plans.txt:171-184`). |
| Robotics and machine ascendancy | `KRG_wake_the_assembly_lines` through `KRG_an_army_of_machines` (054-059), plus `KRG_human_machine_partnership`/`KRG_the_replacement_protocol` | Implemented. The partnership/replacement branch is mutually exclusive; AI ordering requires live validation (`...focus.txt:591,616`; `...plans.txt:193-215`). |
| Paleogenetics | `KRG_open_the_restoration_ledger` through `KRG_the_dinosaur_host` (060-065) | Implemented as a separate project lane with force and sustainability checks. |
| Xenobiology | `KRG_open_the_designed_organism_dossier` through `KRG_the_engineered_legion` (066-071) | Implemented separately from paleogenetics until synthesis, with exact control-mode and containment gates. |
| Portal and temporal continuity | `KRG_recover_the_transit_logs` through `KRG_the_continuity_guard` (072-082) | Implemented. Deployment, terminal, anchor, evidence, stabilization, and temporal-debt checks are present. |
| Exotic energy and biological containment | `KRG_build_an_independent_reactor_grid` through `KRG_authorize_agents_of_last_resort` (083-088) | Focus route is present and gated. Native CBRN stockpile/debit callback remains blocked elsewhere; do not treat these focuses as proof that biological delivery is runtime-complete (`...focus.txt:2222-2264`; `docs/specs/016_brilliant_scientist_specs/README.md`). |
| Diplomacy and host settlement | `KRG_a_state_without_friends` through `KRG_build_the_submission_network` (089-093) | Implemented. Commonwealth and submission are mutually exclusive; decision consumers provide the settlement and patron surfaces. |
| Expansion and integration | `KRG_secure_the_laboratory_corridors` through `KRG_the_continental_laboratory_network` (094-097) | Implemented. Requires foreign route, project capstone, integration capacity, network supply, and overextension checks. Live transfer/annexation cleanup is pending. |
| Evolution IV and terminal choices | `KRG_evolution_four_sovereign_science`, `KRG_commit_to_the_laboratory_world`, `KRG_commit_to_the_strategic_singularity` (098-100) | Implemented. Evolution availability, scenario switches, `can_commit` triggers, and explicit terminal mutex are present (`...focus.txt:2502-2594`; `...plans.txt:496-548`). Disabled-evolution and terminal timing need live scenarios. |

## Missing, simplified, or deferred content

- No required focus route, focus ID, icon, localisation key, or AI plan was missing in this narrowed audit.
- Seventeen opening, economy, project, diplomacy, and expansion nodes intentionally put route locks in `available` rather than a visible `prerequisite` connector. Examples include `KRG_count_the_surviving_staff`, `KRG_secure_the_laboratory_heartland`, `KRG_repair_the_supply_spine`, `KRG_form_the_provisional_command`, `KRG_stabilize_the_laboratory_economy`, `KRG_audit_the_growth_halls`, `KRG_wake_the_assembly_lines`, `KRG_open_the_restoration_ledger`, `KRG_open_the_designed_organism_dossier`, `KRG_recover_the_transit_logs`, `KRG_authenticate_the_temporal_ledger`, `KRG_build_an_independent_reactor_grid`, `KRG_make_containment_the_first_doctrine`, `KRG_a_state_without_friends`, and `KRG_secure_the_laboratory_corridors` (`common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:156-237,675,757,787,1120-2248,2283-2440`). This is runtime-safe but less legible in the tree UI; do not redesign it without a route-layout decision.
- Several architecture gates are also hidden in `available`, including `KRG_authenticate_krugers_continuity`, `KRG_xenobiological_ascendancy`, `KRG_the_project_synthesis`, `KRG_recover_the_stolen_facilities`, `KRG_integrate_by_project`, and `KRG_evolution_four_sovereign_science` (`...focus.txt:675-787,2416-2502`).
- Expansion claims, cores, and war goals are not direct focus effects; they are intentionally routed through the downstream Event 016 decision and scripted-effect consumers keyed by focus unlock flags. This is not a missing route, but those consumers require parent-owned scenario validation (`common/scripted_effects/016_brilliant_scientist_focus_effects.txt`, `common/decisions/016_brilliant_scientist_kruger_state_*.txt`).
- Biological stockpile/debit integration and broader 3D content remain outside this focus audit and are explicitly deferred in the Event 016 specification. No fallback was added.

## Icon coverage

| Surface | Coverage | Evidence |
| --- | --- | --- |
| Focus `icon =` references | 100/100 unique `GFX_goal_KRG_*` IDs | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:36-2584` |
| Normal and shine sprite definitions | 100/100 normal and 100/100 `_shine` | `interface/016_brilliant_scientist_kruger_state_focus.gfx:73-212` |
| Goal DDS textures | 100/100 present | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_*.dds` |
| DDS dimensions/header | 100/100 statically verified as 94x86 DDS | Icon package and filesystem header audit |

No icon patch is recommended.

## Localisation and reward mismatch list

- Missing focus title keys: none (100/100).
- Missing focus description keys: none (100/100).
- Missing custom effect-tooltip keys: none (100/100), including `KRG_commit_to_the_strategic_singularity_effect_tt` (`localisation/english/016_brilliant_scientist_focus_l_english.yml:326`).
- Focus title/description/reward wording mismatch: none found in the static key cross-check.
- Direct reward mismatch: none. Focus completions use `custom_effect_tooltip = KRG_*_effect_tt` and canonical Event 016 helper effects; they do not directly grant equipment, units, manpower, factories, or uncapped terminal effects. Consumer and balance behavior remains a separate audit surface (`common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:46-2594`; `common/scripted_effects/016_brilliant_scientist_focus_effects.txt`).

## AI behavior gaps

- Current file has 19 plans, each with `allowed`, `enable`, `abort`, and `ai_national_focuses`; all 100 focus IDs occur in at least one plan (`common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt:15-548`).
- The current static `allowed` gate excludes `original_tag = DJX`, while dynamic KRG identity and formation/project conditions remain in `enable`. This was introduced by the latest launch-error fix and is not safe to “tighten” without reproducing the parser error; validate it in the parent-owned AI sweep (`...plans.txt:22,55,87,113,129,174,196,218,234,255,292,308,330,354,372,398,447,499,543`).
- Clone citizens/cohorts and human-machine partnership/replacement are both listed in route plans. Their first-listed ordering and focus factors need a live formation-origin and route-choice sweep (`...plans.txt:171-215`).
- Project plans correctly depend on operational project state, but no live weighted-selection sweep has established that all project lanes remain reachable under low-resource, disabled-evolution, or interrupted-transfer states.
- Terminal plans explicitly disable the opposite terminal; a live scenario is still required for `brilliant_scientist_can_commit_to_lab_world`, `brilliant_scientist_kruger_focus_singularity_commitment_is_available`, and the scenario switches (`...plans.txt:496-548`; `...focus.txt:2548-2594`).

## High-priority fixes and validation handoff

1. Parent-owned live route scenarios should cover charter, rebellion, enclave, and takeover formation; focus transfer/load; host settlement; former-host recovery; corridor integration; and interrupted cleanup. Relevant integration surfaces are `common/scripted_effects/016_brilliant_scientist_country_effects.txt`, `common/scripted_effects/016_brilliant_scientist_territory_effects.txt`, `events/016_brilliant_scientist_context_events.txt`, `events/016_brilliant_scientist_host_reaction_events.txt`, and `common/decisions/016_brilliant_scientist_kruger_state_*.txt`.
2. Run an AI route/balance sweep for the four formation origins, clone law, machine law, project operational prerequisites, disabled Evolution IV, and terminal mutual exclusion. The static plan/reference audit is clean, but it cannot prove weighted runtime selection.
3. Keep the biological route marked incomplete until the native CBRN stockpile/debit callback and delivery validity are available. Do not add a fallback to `KRG_make_containment_the_first_doctrine` or `KRG_authorize_agents_of_last_resort`.
4. Treat hidden `available` route locks as a presentation/readability risk, not a parser defect. A broader layout or visible-prerequisite rewrite would exceed this narrowed audit and should be planned separately under the Event 016 improvement loop.

Prior `hoi4.focus_inspect` evidence for the unchanged focus source recorded 100 focuses, 108 connectors, zero KRG layout diagnostics, and zero node/connector intersections in `016_focus_runtime_audit_handoff.md`. This audit did not wait for a new MCP artifact. No live game launch or in-game validation was performed.

## Remaining route risks

The tree can be statically inspected and all named branches are wired, but runtime confidence is limited by transfer/cleanup timing, decision consumer outcomes, operational-project state, AI weighted selection, disabled-evolution scenarios, and the blocked biological stockpile callback. These are explicit follow-up risks rather than completed claims.
