# Event 016 provider navigation: independent source-only review

Date: 2026-10-03

Status: Bounded source acceptance with explicit runtime and audit limits.

## Scope and acceptance basis

The user approved three native decision categories and leaving any matching active paid timer unchanged. This review covers the 60 existing stage decisions, their category placement, the 24 existing Clone Directorate operations, related category localisation and icons, and source-level timer receipt handling. No gameplay, model, or asset source was edited, and no game or live MCP scan was run by this subagent.

The parent evidence file is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_provider_navigation_source_review_2026-10-03.json`. It records baseline `23b2e7e06022c9f1de81958194183f425f0d5bc6`, 60 unchanged decision bodies, category counts of 20 each, 20 checked custom-cost groups, and full-hover payment coverage of 20. I recomputed every listed source SHA-256 against the current working files; all 19 of 19 match. The audit snapshot HEAD was `f48758822b294aeed4c179868e27fddf6abab93d`.

The parent reports a complete MCP inventory of 20 decisions in each category with no in-scope overrides or unresolved definitions. The earlier parent `DECISION_ANALYZED_PARTIAL` result at source revision `ad60b56fec2f777d13ff15396127517b2e3b505f3ac0230680bcd758f2044699` had no scenario coverage; that remains the limit of its scenario evidence.

## Findings by severity

- **No blocking category-placement defect found.** The 60 stage decision IDs are unique and partition into 20 per new category, with five families and four stages per family.
- **No loss or duplication found.** The four-category source inventory contains the 60 regrouped stage decisions and all 24 prior Clone Directorate operations. Those 24 remain under `mengele_clone_army_category`.
- **Unresolved engine behavior:** Source shows how timers and receipts are meant to cancel or finish, but it does not prove callback evaluation while a category is hidden. The parent inventory has no scenario coverage, and this review intentionally did not run live inspection or rendering.
- **Unresolved gate equivalence:** The existing per-stage visibility helper declarations are present, and the Computation family sample uses the strict provider gate, an empty family receipt, and its stage progression flags. I did not exhaustively compare every visible-helper body across all 15 families in this bounded pass, so universal one-current-stage behavior remains a source-level limitation rather than a newly established claim.
- **Unresolved cost-count detail:** The parent evidence and follow-up confirm 20 cost full-hovers, and the source evidence records 20 custom-cost groups. Neither evidence item reports the maximum number of distinct spendable types per action, so this review does not re-certify the four-cost ceiling.

## Category membership and lifecycle

`mengele_conventional_programs_category` contains Computation, Electronics, Materials, Rocketry, and High Energy, with 20 decisions total. `mengele_biological_programs_category` contains Biomedical, Cloning, Paleogenetics, Xenobiological Synthesis, and Biological Weapons, with 20 decisions total. `mengele_advanced_programs_category` contains Teleportation, Robotics, Alien Arms, Temporal, and Singularity, with 20 decisions total. Every family has the existing `theory`, `prototype`, `deployment`, and `weaponization` decision IDs exactly once.

The 24 retained Clone Directorate IDs are `activate_continental_assault_protocols`, `biowarfare_trial_series`, `compile_activation_ledger`, `condition_clone_batches`, `deepen_foreign_tank_network`, `dispatch_biomedical_aid_mission`, `establish_numbered_borderland_commands`, `expand_growth_vats`, `harden_clone_immunity`, `mengele_event016_authorize_singularity_detonation`, `mengele_event016_biomedical_incident_recovery`, `mengele_event016_computation_incident_recovery`, `mengele_event016_construct_singularity_command_node`, `mengele_event016_construct_singularity_power_link`, `mengele_event016_electronics_incident_recovery`, `mengele_event016_high_energy_incident_recovery`, `mengele_event016_materials_incident_recovery`, `mengele_event016_rocketry_incident_recovery`, `mengele_event016_singularity_incident_recovery`, `number_reclaimed_heartland_administrations`, `raise_clone_assault_wave`, `raise_clone_guard_wave`, `raise_clone_infantry_wave`, and `select_genius_embryos`.

All three new categories use `brilliant_scientist_mengele_project_stage_provider_is_valid = yes` for category visibility. The shared provider trigger is in `common/scripted_triggers/016_mengele_project_stage_triggers.txt:16-56` and fails closed for the existing invalid-provider, incident, defeat, closure, expiry, and terminal states.

The sampled native stage decision in `common/decisions/016_mengele_computation_stage_decisions.txt:24-90` retains its existing timed-decision contract, including `days_remove`, `cancel_if_not_visible = no`, an explicit `cancel_trigger`, a receipt-aware `cancel_effect`, and a `remove_effect` that invokes the finish helper. Shared begin, cancel, and finish helpers remain in `common/scripted_effects/016_mengele_project_stage_effects.txt:696-762`. Begin records the paid receipt; cancellation acts only when the requested receipt matches and refunds recorded direct costs; finish clears the matching receipt and applies output only when provider and predecessor checks still pass, otherwise refunding the recorded direct costs. Thus category visibility itself adds no source-level timer cancellation path. Provider loss remains an existing explicit cancellation condition. Whether the engine continues to evaluate that condition after the native category disappears requires runtime evidence.

## Cognitive load, missions, costs, AI, and cleanup

Each new category has five named families in its description and 20 static stage definitions. Existing helper logic is intended to expose the next eligible stage per family and to prevent starting another stage while that family's receipt is occupied. This keeps the source design aligned with the repository's six-primary-action readability guidance when the gates behave as intended. Six is a design guideline, not an engine row limit; this audit makes no clipping or visual-layout claim.

No missions were added or changed. The stage entries are existing timed decisions, not separately owned regional missions; mission owner, region, and mission duplicate-risk fields do not apply to this regrouping. Their requirements, duration, success, failure, and cleanup effects remain in the unchanged decision bodies and existing shared helpers.

The parent source evidence covers 20 custom-cost groups, and the parent separately confirms complete full-hover payment coverage for all 20. The 60 decision-body hashes match the parent evidence, so this regrouping did not alter cost references, quotes, payment, duration, or AI formulas. The separate parent localisation change supplies the corrected blocked and full-hover strings. The distinct spendable-cost count per action was not independently recomputed here. No AI formula changed; this review did not perform a probability balance pass, and the parent MCP result provides no scenario coverage. No new cleanup or exploit behavior was introduced by the category move; receipt cancellation, finish, and refund logic remains as described above.

## Localisation and icon references

All 60 stage decision title keys were found in English localisation. All 60 stage decisions have icon assignments whose sprite names occur in mod `.gfx` definitions. The three new category icons are defined in `interface/016_brilliant_scientist_directorate.gfx` and `interface/016_brilliant_scientist_kruger_state_decisions.gfx`. The new category title and description keys are present in `localisation/english/016_mengele_provider_program_categories_l_english.yml` and name the five families in each category.

Two unchanged legacy operations, `mengele_event016_construct_singularity_command_node` and `mengele_event016_construct_singularity_power_link`, reference `GFX_decision_generic_research`, for which this bounded mod-source scan found no local definition. This appears to be a vanilla sprite reference, but its installed-game definition was not checked here; it is outside the regrouped stage set and is not attributed to the category patch.

## References and validation limits

The parent-cited offline reference is `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:44-78` and `:284-336`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`. The installed reference is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`. The vanilla precedent is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\AFG.txt:1768-1787`, where `AFG_a_royal_successor_decision` is nested under `political_actions`.

Meaningful source checks completed: current-file SHA-256 agreement with the parent evidence (19/19); exact category counts and family/stage distribution; uniqueness of all 60 stage IDs; retention of all 24 Clone Directorate operations; presence of all 60 stage title keys and sprite assignments; and presence of the three category sprite definitions. The source review confirms the regrouping and unchanged decision-body evidence but does not replace runtime validation.

Skipped: no additional MCP inspection, scenario analysis, probability audit, GUI render, or game launch was performed, per the source-only instruction and because the parent owns the live request. The parent `DECISION_ANALYZED_PARTIAL` result had no scenario coverage. Visual spacing, clipping, live category refresh, active countdown continuity after category hiding, and every-family trigger equivalence remain unproven here.

## Handoff

Audit artifact written: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_provider_navigation_independent_review_2026-10-03.md`. No gameplay, model, or asset files were changed, and no commit was created. No plan handoff is needed for this bounded regrouping. The parent may proceed with its authorized source regrouping commit while retaining the runtime and trigger-equivalence limits above.
## Parent review

The parent confirmed the retained generic research sprite in installed interface/decisions.gfx:748.
It resolves GFX_decision_generic_research for both unchanged Singularity construction actions.
The category regrouping commit retains the source and runtime limits above.
