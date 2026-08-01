# Event 016 Kruger State focus-tree audit v2

Date: 2026-08-01

Owner: `/root/event016_focus_audit_v2`

Status: static audit complete; no gameplay focus files were changed.

## Scope and evidence

The audit covered `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`, its Event 016 focus scripted triggers/effects, the KRG AI strategy plans, focus icon registration and DDS files, focus localisation, the 016 decision consumers, and the formation/host-tree load helpers.

The offline National Focus Modding reference and the required core wiki pages were consulted alongside the installed vanilla documentation and vanilla focus/AI strategy examples.

`hoi4.focus_inspect` returned one KRG tree with 100 focuses, 100 resolved titles, 108 connectors, zero crossings, zero node intersections, zero long connectors, zero same-row spacing violations, and zero KRG diagnostics. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/632ea3af6796701be267efed44c0a96a4316cc59e8c3a9b31f3fb9b62deb72cf/75afc44d4390d794159e0104d3a33a9b9852cc3cbbf9bd8c8e5aa00e35433a28/focus-inspect.93785df80dce9083.json`.

`hoi4.focus_render` produced HTML, SVG, JSON, and plan artifacts for `brilliant_scientist_kruger_state_focus_tree`; the layout hash is `2051c203ebb08be69fbdf861193ea1b0d14345c6f393f7f331809834c78e2633`. The global result still reports 14 unrelated vanilla continuous-focus icon/localisation diagnostics from `common/continuous_focus/generic.txt`; none belongs to Event 016.

## Route coverage

| Route surface | Focus identifiers | Coverage result |
| --- | --- | --- |
| Formation opening | `KRG_audit_inherited_portfolio` through `KRG_complete_the_founding_audit` (`:36-286`) | Complete. One root audit, four mutually exclusive formation openers, four OR-gated survival/command focuses, and an explicit AND founding audit are present. |
| State purpose and identity | `KRG_define_the_states_purpose` through `KRG_the_project_synthesis` (`:308-816`) | Complete. Human, Sovereign Directorate, clone, machine, temporal, xenobiological, and Synthesis capstones use identity-open gates and route-forming effects. |
| Laboratory economy and supply | `KRG_stabilize_the_laboratory_economy` through `KRG_sustainable_project_capacity` (`:824-1054`) | Complete. Power, rail/port, portfolio, prototype works, four mutually exclusive supply doctrines, and one OR convergence focus are represented. |
| Conventional security | `KRG_restore_the_ordinary_chain_of_command` through `KRG_a_council_of_project_commanders` (`:1063-1224`) | Complete. Defectors, engineers, counterintelligence, air defence, and mutually exclusive general-staff/project-council command routes are wired. |
| Clone project lane | `KRG_audit_the_growth_halls` through `KRG_the_replicated_host` (`:1233-1374`) | Complete. Prototype/deployment/weaponisation, payable growth burden, drift counterplay, bounded production, and runtime force rebuild gates are present. |
| Robotics project lane | `KRG_wake_the_assembly_lines` through `KRG_an_army_of_machines` (`:1384-1527`) | Complete. Power reserve, frame repair, command protocol, rogue-node counterplay, and bounded robotics production are present. |
| Paleogenetics lane | `KRG_open_the_restoration_ledger` through `KRG_the_dinosaur_host` (`:1537-1677`) | Complete. Reserves, handlers, transport pens, escape response, and bounded paleogenetic breeding remain separate from xeno systems. |
| Xenobiological lane | `KRG_open_the_designed_organism_dossier` through `KRG_xenobiological_ascendancy` (`:1687-1832`) | Complete. Vats, exact control mode, containment, autonomous-nest countertests, bounded production, and identity transition are wired. |
| Portal and temporal lanes | `KRG_recover_the_transit_logs` through `KRG_the_continuity_guard` (`:1842-2116`) | Complete. Terminal ownership/supply, anchor authentication, synchronization/debt, stabilization, and bounded force operations are gated. |
| Exotic and biological lanes | `KRG_build_an_independent_reactor_grid` through `KRG_authorize_agents_of_last_resort` (`:2126-2273`) | Complete. High-energy delivery and interface requirements, containment, authenticated biological delivery, and bounded last-resort actions are represented. |
| Diplomacy and foreign policy | `KRG_a_state_without_friends` through `KRG_settle_accounts_with_the_former_host` (`:2282-2389`) | Complete. Recognition, foreign intelligence, former-host settlement, commonwealth, and submission routes have consumed unlock flags. |
| Expansion and integration | `KRG_secure_the_laboratory_corridors` through `KRG_the_continental_laboratory_network` (`:2391-2500`) | Complete. Command-route convergence, evidence-backed recovery, project integration, capacity, supply, and overextension checks are present. |
| Evolution IV and terminals | `KRG_evolution_four_sovereign_science`, `KRG_commit_to_the_laboratory_world`, `KRG_commit_to_the_strategic_singularity` (`:2502-2603`) | Complete. Evolution-IV/scenario gates and symmetric terminal mutual exclusion delegate final readiness to the canonical terminal triggers. |

## Missing or simplified content

- No missing KRG focus route, focus ID, prerequisite target, mutual-exclusion target, project-force lane, terminal branch, or decision unlock was found in this audit.
- No focus directly creates equipment, units, manpower, factories, or a fabricated project stage. Project capstones call the idempotent runtime package rebuild only.
- Synthesis is intentionally a political convergence focus (`KRG_the_project_synthesis`); it is not counted as an additional army capstone. The expansion and Evolution IV gates therefore count the underlying project-family capstones, matching the architecture's distinction between political identity and project armies.
- The four y2 opening focuses (`KRG_count_the_surviving_staff`, `KRG_secure_the_laboratory_heartland`, `KRG_repair_the_supply_spine`, and `KRG_form_the_provisional_command`) use OR `available` gates instead of explicit visible prerequisite connectors. This is semantically correct and produced a clean render, but it leaves a UI clarity/hover-spam risk for a future polish pass (`:156-262`).
- Host formation and host takeover both intentionally load the KRG tree with `keep_completed = no` only after the Event 016 carrier/host contract is established (`common/scripted_effects/016_brilliant_scientist_country_effects.txt:605,882`). This is a full KRG state tree load, not an additive overlay; preserving the original host tree is explicitly excluded by the Event 016 architecture.

## Icon coverage

| Surface | Result | Evidence |
| --- | --- | --- |
| Focus icon references | 100/100 unique `GFX_goal_KRG_*` IDs | Static extraction from the focus source. |
| Regular sprites | 100/100 registered | `interface/016_brilliant_scientist_kruger_state_focus.gfx`. |
| Shine sprites | 100/100 registered | Same `.gfx` file, one `_shine` sprite per focus. |
| DDS texture paths | 200/200 regular/shine references resolve to 100 existing DDS files | Static filesystem check under `gfx/interface/goals/016_brilliant_scientist/`. |
| Duplicate icon IDs | None | Static duplicate check. |

## Localisation and reward mismatch list

- No missing title keys: 100/100 focus IDs resolve in `localisation/english/016_brilliant_scientist_focus_l_english.yml`.
- No missing description keys: 100/100 `_desc` keys resolve in the same file.
- No duplicate localisation keys were found, and the file is UTF-8 with BOM.
- All 100 `custom_effect_tooltip = KRG_*_effect_tt` keys and the `KRG_sovereign_identity_open_tt` trigger tooltip resolve.
- No focus title/description versus reward mismatch was found in the route-level review; titles describe the corresponding state, project, diplomacy, or terminal reward.
- Every `brilliant_scientist_focus_unlock_*` flag emitted by the focus tree has at least one consumer in the Event 016 decision/category surfaces. No consumerless focus receipt was found.
- Focus ideas are applied through route-specific scripted effects rather than duplicated `add_ideas` blocks in the tree; the effects and idea package were present and referenced by the route-forming effects.

## AI behavior gaps

| Priority | Gap | File and identifiers | Impact |
| --- | --- | --- | --- |
| High | There is no dedicated mixed-family/Synthesis AI strategy plan. The six exclusive project plans explicitly set `KRG_the_project_synthesis = 0` in their `focus_factors` (`common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt:29-30,50-52,104-106,124-126,159-161,195-197`). `KRG_the_project_synthesis` itself has `ai_will_do = @krg_ai_preferred` (`common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:787-816`), but no `enable`/`abort` plan selects the mixed route. | AI may commit to an exclusive project plan and never choose the Synthesis capstone even when Paleogenetics, Xenobiological Synthesis, and a third family are available. Add a narrow Synthesis plan or revise the zero factors in the parent-owned AI pass. |
| Medium | `KRG_takeover_consolidation_plan` ends after the founding/consolidation opener (`common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt:74-87`) and does not explicitly hand off to a post-audit identity or expansion plan. | Generic per-focus `ai_will_do` values can continue the route, but takeover-specific government and integration priorities are less deterministic than charter/rebellion/enclave origins. |
| Medium | The 17 plans have valid `allowed`, `enable`, `abort`, and `ai_national_focuses` blocks, and all listed KRG focus IDs resolve. Terminal plans are mutually disabled by canonical terminal readiness, but route balance under disabled Evolution IV and hostile maintenance states remains un-simulated. | Parent-owned weighted-logic/balance validation remains required; this is not a load blocker. |

## High-priority fixes first

1. Add or review a dedicated Synthesis AI plan so a mixed-family AI can reach `KRG_the_project_synthesis` without relying on generic focus scoring.
2. Add a takeover post-audit AI handoff or explicit focus-factor route weights if parent balance testing confirms the generic fallback selects the wrong identity.
3. Keep the unrelated generic continuous-focus diagnostics separate from Event 016; re-run the KRG inspect after any generic asset/localisation repair.

## Validation run

- Parsed the focus source with balanced braces: exactly 100 focus blocks.
- Cross-checked all focus IDs, icons, titles, descriptions, effect/tooltips, and focus unlock consumers with static scripts.
- Confirmed every focus has `ai_will_do`; all factors use defined same-file constants.
- Confirmed all 17 Event 016 AI plan blocks exist and all KRG focus references resolve.
- Ran `hoi4.focus_inspect` and `hoi4.focus_render`; KRG diagnostics and layout checks are recorded above.
- Verified the host/formed KRG tree load calls and the active-country trigger chain in `common/scripted_effects/016_brilliant_scientist_country_effects.txt:605,882`, `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt:15-20`, and `common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt:23-26`.

## Skipped meaningful validation and remaining risks

- No Hearts of Iron IV process was launched, as required by the repository instructions. Live focus selection, AI strategy arbitration, host transformation in a saved campaign, and decision availability remain unproven here.
- No gameplay patch was made, so no rollback evidence is needed. The Synthesis AI gap is intentionally handed to the parent because adding a new strategy plan changes route selection rather than correcting a local focus syntax defect.
- The y2 availability-only opening and global generic-focus diagnostics remain the only static/UI caveats found in the focus surface.

Handoff path: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_kruger_state_focus_audit_v2_2026-08-01.md`.
