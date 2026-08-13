# Event 016 Kruger State focus-tree audit handoff

Date: 2026-08-05

Owner: `/root/event16_focus_audit`

Scope: `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt` and directly linked Event 016 focus helpers, decisions, ideas, localisation, icons, AI plans, and documentation.

This handoff records a static focus audit plus one narrow consumer patch. It does not claim live Hearts of Iron IV completion, and it does not redesign the tree.

## Parent disposition

The audit patch is accepted. The 100-focus authored architecture is retained because it satisfies the requested 85-to-115 range, covers all required route families, and uses decision systems for recurring route depth. The approximate per-family counts are not promoted into a count-filling expansion; the follow-up plan is retained as evidence for a future gameplay-driven depth pass only.

The portal recruitment consumer patch is accepted. Live route sequencing, hidden-gate readability, terminal transitions, and biological delivery remain acceptance risks and are not represented as proven by this static audit.

## Required references and evidence

The audit used `AGENTS.md`, the complete `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents` skills, the required offline Paradox wiki pages, the relevant vanilla documentation files, the Event 016 focus specification, the focus architecture matrix, the AI behavior matrix, and the Event 016 acceptance reviews.

The parent `hoi4.focus_inspect` and `hoi4.focus_render` run recorded 100 focuses, 108 connectors, zero connector crossings, zero node intersections, zero long connectors, and zero too-close same-row pairs. The 14 blocking diagnostics reported by that run are unrelated vanilla continuous-focus icon references rather than KRG focus errors.

The national-focus AI probability inspection returned `PROBABILITY_SOURCE_INSPECTED` for the four supply candidates with `poolComplete=true`, `candidates=4`, `unresolved=0`, and validation passed. Artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/433763f5f8af27d510d51301ee3aacfb4ea0232cc56d4cff9d3d4fd163bbb9a0/5007570ed84fe0d4dcf7af40a12dad690f964005c62afcc1bc15a92b96eefeca/probability-inspect-3d9b99639271.json`.

## Route coverage table

| Route family | Implemented focus IDs | Current hooks and convergence | AI coverage and remaining risk |
| --- | --- | --- | --- |
| Opening survival and formation origins | `KRG_audit_inherited_portfolio` through `KRG_complete_the_founding_audit` (001-010) | Charter, rebellion, enclave, takeover, and inherited-portfolio foundations converge through repeated AND prerequisites at `KRG_complete_the_founding_audit`. | Charter, rebellion, enclave, takeover-consolidation, and takeover-post-audit plans exist. Formation transfer and focus-load timing still need live scenarios. |
| Government and sovereign identity | `KRG_define_the_states_purpose` through `KRG_the_project_synthesis` (011-030) | Directorate, human, clone, machine, temporal, xenobiological, and synthesis identity routes use explicit capstones and route flags. Identity locks and project synthesis require intended convergence. | Political and project plans cover all identities. Clone-law, machine-law, temporal evidence, and synthesis weighting need live route sweeps. |
| Laboratory economy and supply doctrine | `KRG_stabilize_the_laboratory_economy` through `KRG_sustainable_project_capacity` (031-040) | Four mutually exclusive supply choices converge through `KRG_sustainable_project_capacity`; repeated prerequisites are AND-style, while the supply choice is intentionally OR-style. | Origin plans list all four supply focuses with the same preferred factor, so inherited-portfolio choice is not route-differentiated in static AI ordering. Probability inspection proves the four-candidate pool only, not ordered strategy-plan selection. |
| Conventional security | `KRG_restore_the_ordinary_chain_of_command` through `KRG_a_council_of_project_commanders` (041-047) | Command, defectors, engineers, counterintelligence, airspace, staff, and council rewards unlock downstream operations and project support. | Origin and takeover plans include the route. Focus factors are route-aware for the main political handoff; live sequencing is pending. |
| Replicative biology | `KRG_audit_the_growth_halls` through `KRG_the_replicated_host` (048-053), plus clone political choices 019-021 | Growth halls, nutrient chain, identity register, clone cadres, and drift converge on the replicated host and then clone sovereignty. | `KRG_clone_sovereignty_plan` and diplomatic handoff plans exist. Clone citizens versus cohorts requires live preference and balance validation. |
| Robotics and machine ascendancy | `KRG_wake_the_assembly_lines` through `KRG_an_army_of_machines` (054-059), plus machine political choices 023-025 | Assembly, power, frame repair, command protocol, rogue-node isolation, and machine army converge on partnership or replacement politics. | `KRG_machine_ascendancy_plan` and commonwealth/submission weighting exist. Partnership versus replacement sequencing remains a live-risk surface. |
| Paleogenetics | `KRG_open_the_restoration_ledger` through `KRG_the_dinosaur_host` (060-065) | Reserves, handlers, pens, escape drills, and dinosaur host form a distinct project army lane with project-force and supply checks. | `KRG_paleogenetic_plan` covers the lane through its capstone; post-capstone handoff to diplomacy/expansion is not proven by static ordering. |
| Xenobiology | `KRG_open_the_designed_organism_dossier` through `KRG_the_engineered_legion` (066-071) | Vat complexes, control channel, containment, red-team review, and engineered legion remain separate from paleogenetics until synthesis. | `KRG_xenobiological_plan` covers the lane and xenobiological identity. Its post-capstone handoff and disabled-resource behavior need live validation. |
| Portal transit | `KRG_recover_the_transit_logs` through `KRG_the_strategic_transit_corps` (072-076) | Transit logs, terminal rings, depot network, breach closure, and Strategic Transit Corps unlock bounded transit, paid insertion, and capped recruitment. The focus unlock is now consumed by the portal-transit batch decision. | `KRG_portal_plan` covers 072-076. The decision gate patch is statically verified; terminal loss and raid sequencing remain untested live. |
| Temporal operations | `KRG_authenticate_the_temporal_ledger` through `KRG_the_continuity_guard` (077-082), plus temporal political choices 026-028 | Ledger, anchor, synchronization, stabilization, future warnings, and guard use temporal validity and debt checks before Continuum identity. | `KRG_temporal_plan` covers operations and political convergence. Temporal debt, rescue, and stabilization timing need scenario validation. |
| Exotic energy and biological containment | `KRG_build_an_independent_reactor_grid` through `KRG_authorize_agents_of_last_resort` (083-088) | Reactor, delivery architecture, interface specialists, exotic guard, containment doctrine, and last-resort agents are gated by high-energy, delivery, and containment triggers. | Alien-arms and biological plans exist. Native biological stockpile/debit callback remains blocked elsewhere, so this route is not a proof of runtime-complete delivery. |
| Diplomacy and former-host settlement | `KRG_a_state_without_friends` through `KRG_build_the_submission_network` (089-093) | Foreign intelligence, former-host settlement, commonwealth, and submission are mutually exclusive route caps consumed by settlement and diplomacy decisions. | Commonwealth and submission plans provide route-aware weights. The tree has five focuses here against the architecture's approximate ten-to-fourteen target; queued depth plan records a possible future tranche. |
| Expansion and integration | `KRG_secure_the_laboratory_corridors` through `KRG_the_continental_laboratory_network` (094-097) | Corridor security, facility recovery, project integration, and continental network use occupation capacity, supply, overextension, and route-specific integration consumers. | Commonwealth/submission plans cover these IDs. The tree has four focuses against the approximate ten-to-fourteen target; hidden availability and live transfer/annexation cleanup remain risks. |
| Evolution IV and terminal commitments | `KRG_evolution_four_sovereign_science`, `KRG_commit_to_the_laboratory_world`, and `KRG_commit_to_the_strategic_singularity` (098-100) | Evolution availability gates both mutually exclusive terminal commitments. Laboratory World requires verified nonterminal control; Singularity blocks Laboratory World and uses its own activation contract. | Dedicated Laboratory World and Singularity plans exist. Terminal timing, disabled Evolution IV, and opposite-terminal cancellation require live scenarios. |

## Missing, simplified, or deferred content

- No focus ID, route family, focus reference, custom trigger, custom effect, mutual-exclusion edge, icon, DDS, focus-localisation key, or AI-plan reference was missing in the static audit.
- Diplomacy/former-host, expansion/integration, and terminal branches are materially shorter than the approximate branch-family targets in the specification matrix, even though the existing 100-focus architecture documents those shorter counts and decision categories add recurring depth. The follow-up is recorded in `docs/plans/016_brilliant_scientist_plans/016_krg_focus_depth_followup_plan_2026-08-05.md`; no broad tree redesign was made here.
- Many route locks are intentionally hidden in `available` rather than visible connectors, including the opening AND family, economy restart, project openers, `KRG_authenticate_krugers_continuity`, `KRG_the_project_synthesis`, `KRG_secure_the_laboratory_corridors`, `KRG_recover_the_stolen_facilities`, `KRG_integrate_by_project`, and Evolution IV (`common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:156-237,675-787,1120-2248,2283-2502`). This is a player-readability risk, not a parser or layout defect.
- Claims, war goals, cores, facility capture, and postwar integration are intentionally routed through downstream decisions and scripted consumers keyed by focus unlocks. They require parent-owned scenario validation rather than direct focus rewards.
- Biological stockpile/debit integration remains blocked by the native CBRN callback surface. No fallback was added.

## Icon coverage

| Surface | Coverage | Evidence |
| --- | --- | --- |
| Focus `icon =` references | 100/100 unique `GFX_goal_KRG_*` IDs | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:36-2584` |
| Normal focus sprites | 100/100 | `interface/016_brilliant_scientist_kruger_state_focus.gfx` |
| Shine focus sprites | 100/100 | `interface/016_brilliant_scientist_kruger_state_focus.gfx` |
| Goal DDS textures | 100/100 | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_*.dds` |

The shine registrations intentionally reuse their matching DDS with the vanilla button-state shader; no missing or repeated icon reference was found.

## Localisation and reward mismatch list

- Focus title keys: 100/100 present in `localisation/english/016_brilliant_scientist_focus_l_english.yml`.
- Focus description keys: 100/100 present in the same file.
- Custom focus effect-tooltip keys: 100/100 present, with no unresolved `custom_effect_tooltip` key.
- Event 016 idea title/description keys checked across the focus-localisation files: 55/55 present.
- No title, description, icon, or reward wording mismatch remained after the portal decision gate patch.
- Before the patch, `KRG_the_strategic_transit_corps` set `brilliant_scientist_focus_unlock_bounded_portal_recruitment` but no decision consumed it. The focus tooltip promised portal recruitment while `brilliant_scientist_krg_fabricate_portal_transit_batch` could be used by any country with teleportation operational plus its existing raid/terminal/cost/capacity conditions. The patch makes the focus flag a visible and available gate, bringing the reward and consumer into alignment.

## AI behavior gaps

- `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` contains 19 plans, and every one of the 100 focus IDs appears in at least one `ai_national_focuses` list. Every plan's references resolve and each plan has the current static `allowed = { NOT = { original_tag = DJX } }` plus a dynamic KRG identity `enable` gate.
- Charter, rebellion, and enclave origin plans list all four supply focuses with the same focus factor (`common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt:34-40,67-74,98-104`), so the inherited portfolio does not produce a static route-specific preference among conventional, automated, portal, and biological supply. This needs a live preference decision or a later narrow AI patch if the parent wants deterministic route selection.
- Several project plans end at their project capstone (`KRG_the_dinosaur_host`, `KRG_the_engineered_legion`, `KRG_the_strategic_transit_corps`, `KRG_the_continuity_guard`, `KRG_arm_the_exotic_guard`, or `KRG_make_containment_the_first_doctrine`) and rely on a later plan or default focus selection for diplomacy/expansion (`common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt:215-383`). The plan handoff is plausible but not proven by static files.
- The probability adapter explicitly warns that ordered AI strategy plans can override weighted focus selection and requires scenario inputs for live ordering. The `ai_strategy_factor` surface returned `PROBABILITY_SURFACE_EMPTY`, so no claim is made for runtime strategy-plan factors.
- No live AI route sweep was run for charter, rebellion, enclave, takeover, clone-law, machine-law, disabled-Evolution, interrupted-transfer, or terminal mutual-exclusion scenarios.

## High-priority fixes first

1. Completed narrow fix: gate `brilliant_scientist_krg_fabricate_portal_transit_batch` with the Strategic Transit Corps unlock flag.
2. Parent review: decide whether the documented five/four/three diplomacy, expansion, and terminal counts are acceptable within the 85-115 total, or promote the queued depth plan before adding any nodes.
3. Parent-owned live AI route and balance sweeps should verify ordered plan handoffs, origin supply selection, project capstone continuation, disabled Evolution IV, and terminal locks.
4. Keep biological delivery marked incomplete until the native stockpile/debit callback is implemented and validated (`common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:2221-2271`; Event 016 specification README).
5. Treat the 14 unrelated continuous-focus icon diagnostics as external to this KRG audit; they should not be used as evidence that the KRG tree itself has a layout defect.

## Changed files and identifiers

Gameplay patch:

- `common/decisions/016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt`.
- Focus reward consumer: `KRG_the_strategic_transit_corps` (`common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1933-1958`) remains unchanged.
- Decision: `brilliant_scientist_krg_fabricate_portal_transit_batch` now requires `brilliant_scientist_focus_unlock_bounded_portal_recruitment` in both `visible` and `available` (`...portal_temporal_decisions.txt:212-240`).

Documentation:

- `docs/plans/016_brilliant_scientist_plans/016_krg_focus_depth_followup_plan_2026-08-05.md`.
- This handoff file.

No focus source, AI plan, localisation, icon, idea, scripted helper, formable, or custom-technology API file was changed.

## Route behavior before and after

Before the patch, any active KRG country with teleportation operational could see and fabricate a portal-transit equipment batch when the existing raid-or-terminal-supply, material-cost, and capacity conditions passed. The Strategic Transit Corps focus set an unlock flag but did not gate that decision.

After the patch, the decision remains bounded by teleportation operation, raid or terminal-supply access, material cost, and batch capacity, and it additionally requires the Strategic Transit Corps unlock flag in both visibility and availability. The focus reward now has a direct executable consumer, and portal recruitment cannot bypass the focus route.

## Localisation and icon IDs changed

None. The existing decision localisation and `GFX_decision_brilliant_scientist_krg_portal_terminal` icon remain valid because the patch changes only triggers.

## Meaningful validation performed

- Static focus parse/count: 100 focus blocks and 100 unique IDs.
- Static AI plan count: 19 plans; all 100 focus IDs are represented in at least one plan.
- Focus reference, scripted trigger/effect, mutual-exclusion, icon, DDS, and localisation cross-checks found no unresolved KRG references or missing assets.
- Lifecycle review confirmed the focus-owned visible maximum remains three consolidated spirits: one route summary, command, and supply. Hidden original lifecycle mirrors remain invisible, and project-force/world-threat ideas are not focus-owned slots.
- Composite focus-unlock consumer scan found no remaining `NO_CONSUMER` flag after the portal patch. The targeted reference check returns the focus setter at line 1953 and decision gates at lines 217 and 221.
- The parent MCP layout/render result found no KRG layout defects. The only reported blockers were unrelated vanilla continuous-focus icon references.
- The national-focus probability inspection completed with a complete four-candidate pool and no unresolved candidates; its artifact URI is recorded above.

## Skipped meaningful validation and why

- No Hearts of Iron IV process was launched, per repository instructions. In-game focus completion, decision visibility, AI ordering, balance, and save-state behavior remain parent-owned checks.
- No new `hoi4.focus_render` run was required after the patch because the focus source and icon wiring were unchanged. The parent's existing layout/render evidence remains applicable.
- No live AI scenario sweep was run because the probability adapter requires explicit scenario inputs and ordered strategy plans can override weighted focus selection. The empty `ai_strategy_factor` surface was treated as an adapter limitation, not as proof of a code defect.
- No broad focus-tree rewrite was attempted because it would exceed this audit scope and would conflict with the existing 100-focus architecture without a parent disposition.

## Remaining route risks

The main remaining risks are hidden prerequisite readability, the short diplomacy/expansion/terminal branch counts, unproven AI plan handoffs and supply-choice ordering, former-host transfer and integration cleanup timing, disabled Evolution IV behavior, terminal counterplay timing, and the blocked biological stockpile/debit callback.

The queued depth plan is at `docs/plans/016_brilliant_scientist_plans/016_krg_focus_depth_followup_plan_2026-08-05.md`.

No unrelated changes were made, and no commit was created by this subagent.
