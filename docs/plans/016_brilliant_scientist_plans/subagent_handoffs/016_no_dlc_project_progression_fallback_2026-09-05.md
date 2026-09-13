# Event 016 no-DLC project progression fallback handoff

Status: bounded implementation complete for parent review. The worktree is intentionally unstaged and uncommitted as requested. The implementation is limited to the existing Directorate board, the Event 016 project helpers and constants that it calls, matching project localisation, the project-system documentation, and the scenario fixture.

## Scope and design contract

When `Gotterdammerung` is absent, each of the fifteen Event 016 families now has a paid, timed Prototype adapter in `brilliant_scientist_directorate_category`. The adapter calls the canonical stage receipt and transition helpers, occupies the existing Prototype capacity delta, consumes support equipment and fuel after the decision's political-power payment and civilian-factory reservation, and treats the family-specific strategic-resource values as reserve gates only.

When `Gotterdammerung` is present, the fifteen no-DLC adapters and six no-DLC Singularity component decisions are hidden and the existing native special-project route remains authoritative. The fifteen native integration decisions were explicitly DLC-gated so the board cannot present a duplicate native/fallback Prototype route.

The no-DLC Singularity route exposes six separate paid timed component receipts. Each receipt calls `brilliant_scientist_register_singularity_component`, preserving the existing component enum, array entry, count, completion flag, and one-time registration guard. The paid Singularity Prototype adapter remains hidden until all six components are registered, and partial chains never auto-advance Prototype. Existing Fallout, Laboratory World, host, facility, incident, terminal, exclusivity, and downstream stage gates remain in the shared triggers and callbacks.

## Changed files and identifiers

- `common/decisions/016_brilliant_scientist_directorate_project_board.txt`: Added fifteen `brilliant_scientist_fallback_<family>_prototype` decisions and six `brilliant_scientist_fallback_singularity_<component>` decisions; added `has_dlc = "Gotterdammerung"` to the native integration decision visibility blocks.
- `common/script_constants/016_brilliant_scientist_project_constants.txt`: Added centralized `brilliant_scientist_project_fallback_prototype` and `brilliant_scientist_project_fallback_singularity_component` cost, resource-gate, and component-duration profiles.
- `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`: Added no-DLC Prototype research/payment gates, six component payment gates, Prototype input validation, component enum validation, and the DLC-aware Singularity board guard.
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt`: Added the Prototype capacity delta branch, no-DLC component cleanup, and the begin/cancel/finish component fallback wrappers around the canonical registry.
- `common/scripted_effects/016_brilliant_scientist_effects.txt`: Added `brilliant_scientist_load_no_dlc_prototype_cost`, routed accident-pressure cost loading through it, and cleared component fallback state during host-transfer reconciliation.
- `localisation/english/016_brilliant_scientist_projects_l_english.yml`: Added concise no-DLC requirement, effect, cancellation, component, four-burden cost, blocked-cost, and reserve-gate tooltips using texticons for every displayed spendable cost.
- `docs/events/016_brilliant_scientist/systems/projects.md`: Documented native versus no-DLC flow, the six-component receipt chain, helper ownership, payment semantics, and the explicit fixture evidence.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_NO_DLC_PROJECT_FALLBACK_2026_09_05.scenarios.json`: Added six explicit DLC-present, DLC-absent, Singularity partial/complete, and terminal-lock scenarios with all fifteen family mappings and twenty-one candidate identifiers.

The fifteen Prototype identifiers are `brilliant_scientist_fallback_computation_prototype`, `brilliant_scientist_fallback_electronics_prototype`, `brilliant_scientist_fallback_materials_prototype`, `brilliant_scientist_fallback_rocketry_prototype`, `brilliant_scientist_fallback_high_energy_prototype`, `brilliant_scientist_fallback_biomedical_prototype`, `brilliant_scientist_fallback_teleportation_prototype`, `brilliant_scientist_fallback_cloning_prototype`, `brilliant_scientist_fallback_robotics_prototype`, `brilliant_scientist_fallback_paleogenetics_prototype`, `brilliant_scientist_fallback_xenobiological_synthesis_prototype`, `brilliant_scientist_fallback_biological_weapons_prototype`, `brilliant_scientist_fallback_alien_arms_prototype`, `brilliant_scientist_fallback_temporal_prototype`, and `brilliant_scientist_fallback_singularity_prototype`.

The six component identifiers are `brilliant_scientist_fallback_singularity_command_core`, `brilliant_scientist_fallback_singularity_power_link`, `brilliant_scientist_fallback_singularity_containment_lattice`, `brilliant_scientist_fallback_singularity_temporal_authenticator`, `brilliant_scientist_fallback_singularity_delivery_architecture`, and `brilliant_scientist_fallback_singularity_fail_deadly_governor`.

## Before and after behavior

Before, a country without `Gotterdammerung` could reach the Event 016 Theory ledger but had no decision-led path to the native special-project Prototype presentation, leaving project families unable to continue through the board. The existing native integration blocks also lacked an explicit DLC visibility boundary.

After, a valid no-DLC Theory family presents one matching paid Prototype adapter. Selecting it reserves the decision's civilian factories, spends political power through the decision cost, starts the centralized timed burden, and consumes the family support-equipment and fuel values through the canonical stage helper. Completion, cancellation, terminal cleanup, incident pressure, breakthrough history, reward callbacks, capacity reconstruction, and downstream Deployment/Weaponization/Autonomy decisions remain the existing receipt-owned behavior.

After, a no-DLC Singularity Theory family first presents six separate component receipts. Zero components leaves Prototype unavailable, three components leave it unavailable, and the sixth component only unlocks the paid Prototype adapter. A component cannot be registered twice because the canonical array/count guard remains authoritative.

## Issue list sorted by severity

1. Medium: The installed probability service can inspect and compare the source, but it resolves the board entries through its `mission_ai_will_do` adapter rather than the requested decision adapter and reports partial analysis with unresolved helper/state inputs. This is an evidence limitation, not an accepted balance claim; the exact artifacts and scenarios are recorded below.
2. Medium: A fully eligible Theory portfolio can expose up to fifteen no-DLC Prototype rows in the existing category at once. This is inherited board density and no new category, GUI, selection system, or warehouse tab was introduced in this bounded fallback. The parent should decide whether a later accepted phasing/selection tranche is warranted; adding that system here would exceed scope.
3. Low: The six component receipts use the timed decision's civilian-factory reservation and consume support equipment/fuel but do not deduct project Capacity, matching the native component projects' no-stage-capacity behavior. The parent should retain this as an explicit balance review point.
4. Low: Live game validation and DLC matrix loading were not run because agents must not launch HOI4; the user owns live consumer validation. Static and MCP checks are listed below.

## Decision category lifecycle notes

The existing `brilliant_scientist_directorate_category` remains the only category touched. No new category or scripted GUI was added. Theory decisions continue to create the family ledger entries, the new no-DLC Prototype rows become visible only for a valid Theory family and absent DLC, and the existing stage rows remain the route for Deployment, Weaponization, and Autonomy.

For a DLC-present country, native integration decisions are visible only through `has_dlc = "Gotterdammerung"`, and the no-DLC rows are hidden. For a DLC-absent country, native integration decisions are hidden, the fallback rows use the ordinary board receipt, and no native special-project card is required.

The board-ready trigger blocks a second active normal stage or component receipt. Terminal closure cancels the active normal receipt and the active component receipt before the existing terminal cleanup proceeds. Host-transfer reconciliation clears the component fallback flag and active component variable while preserving completed component flags and the canonical array/count history.

## Cognitive-load notes

- Visible actions: no new tab or category was introduced, but a portfolio with all fifteen families in Theory can show fifteen fallback Prototype rows. The six Singularity component rows are only visible while Singularity remains Theory and each completed component hides its own row.
- Active missions: this tranche adds no mission object and no new recurring pulse. Existing incident/recovery missions remain governed by their existing owner and active-receipt locks.
- Player-facing values: every fallback row shows family, stage, political power, civilian-factory reservation, support-equipment burden, and fuel burden. The separate reserve tooltip uses `£resources_strip` icons and explicitly states that those resources are checked but not consumed.
- Text density: requirement, reserve, blocked-cost, and effect strings are separate custom tooltips. Cost strings contain exactly four displayed spendable types and avoid literal resource names.
- Significance: political power is the decision payment, civilian factories are the timed reservation, support equipment and fuel are consumed at stage start, and strategic resources are non-consumed gates. Prototype completion still changes the stage ledger and unlocks the existing downstream rows.

## Mission and timed-receipt quality notes

The new objects are timed decisions rather than missions. Their owner is the current Event 016 host country, their category is `brilliant_scientist_directorate_category`, and they have no map-region target because the existing project ledger owns the family/site context. Each row requires the family-specific Theory entry, host/KRG/facility/scenario checks, no active incident, no terminal/Laboratory World state, and the corresponding equipment/fuel/political-power/resource gates.

Prototype durations reuse `brilliant_scientist_project_duration.<family>_prototype`. Component durations are centralized in the six component constants. Completion calls the canonical transition or component-registration helper, cancellation settles only the matching active receipt, and removal applies the existing output/history/reward path. The board-ready and exact family/stage ownership checks prevent duplicate starts and mismatched callbacks.

## Cost and requirement clarity

Every fallback decision has at most four distinct displayed spendable cost types: political power, civilian-factory reservation, support equipment, and fuel. The reserve resource values are requirements rather than consumed costs and are shown in a separate tooltip. Every spendable value uses a texticon (`£pol_power`, `£civ_factory`, `£support_equipment_text_icon`, and `£GFX_fuel_texticon`); reserve gates use `£resources_strip|N` icons.

The fallback constants centralize family and component values. The trigger-side resource mirrors are file-scoped only because the engine rejects script constants in those resource trigger fields. The stage helper zeros the generic native burden profile before loading the adapter profile, so the no-DLC route does not silently consume the unrelated generic trucks, trains, manpower, experience, or resource-unit fields.

## AI validity and route locks

Fallback Prototype rows use the existing high project AI baseline with war/preferred and low-capacity modifiers. Component rows use the existing medium project AI baseline with the same preferred modifier. Every AI-visible fallback row is explicitly absent when `Gotterdammerung` is present, and every native integration row is explicitly absent when it is absent. Research, host, facility, scenario, incident, terminal, and Singularity component-count gates are shared with the existing project triggers rather than duplicated in AI-only logic.

The probability service inspected the postpatch surface under `mission_ai_will_do` because the requested decision adapter exposed only three pre-existing decision candidates and did not discover the new candidate pool. No GUI route was in scope, so `hoi4.gui_inspect` and `hoi4.gui_render` were not run.

## Localisation and tooltip gaps

The new identifiers have matching English localisation, including regular and blocked cost strings, reserve-gate strings, requirement strings, effect summaries, cancellation text, component titles, and component effects. A static reference scan found 44 unique new localisation references with no missing keys. Other language files were not changed because the scoped project already uses the English fallback and the parent owns broader localisation policy.

## Cleanup and exploit-risk notes

The stage helper adds the Prototype capacity delta only for the fallback Prototype request. Component receipts do not create a second project ledger or capacity delta. The canonical array membership guard makes component registration idempotent, and the active component flag/variable is cleared on cancellation, terminal closure, and host-transfer reconciliation. DLC gates prevent native/fallback duplicate presentation and duplicate native payment. No free grant, direct stage write, resource refund, or bypass of the six-component chain was added.

## Meaningful validation

- The JSON fixture parsed successfully with `scenarios=6`, `families=15`, and `candidates=21`.
- All fifteen fallback Prototype identifiers and all six component identifiers occur exactly once in the decision source.
- The scoped Clausewitz files passed a comment/string-aware brace balance scan, and the scoped scan found no unsupported `<=` or `>=` operators.
- The localisation file retained its UTF-8 BOM, and the new localisation reference scan reported `localisation_refs=44 unique=44 missing=`.
- Baseline probability inspection used the Event 016 board source before patching in workspace `mod_chaos_redux_ea3b2d67c2c0`; the returned artifact basename was `probability-inspect-3d1c33e0db6c.json`.
- Postpatch probability inspection discovered 21 fallback candidates under `mission_ai_will_do`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21f5a3286049219afb74d34ed3a41b79e0eb4b1bc66c8f7db4369a394d4b4d8d/944e253c2f69d86dea755dc6a46f118a7b3d74d56182a0a1bec2fa5731143bba/probability-inspect-cf98b6f7becc.json`.
- Postpatch evaluation used the six named fixture scenarios and returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-e91b869c8ba5f1e0fd2c89d9`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7967e5ed3a070eedd786ac4438cbe5c4ef5a2679187bc50048eaf2eb239ed91b/5bf8ce2492e90270891bf7702bf85b13c568f857843c79f588c5d819161c0b3a/probability-e91b869c8ba5f1e0fd2c89d9.json`. It reported six scenarios, 126 candidates, 57 unresolved inputs, and zero diagnostics.
- Same-scenario before/after comparison used the staged prepatch board source for `before`, the current working board source for `after`, the same six scenario IDs, and a pool containing the fifteen existing Theory AI candidates plus the fifteen fallback Prototype candidates. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-7709ebee871c3aee7658972f`, and `comparisonChanges=90`. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/676b3a24f3c9aa06af95a1825d9426d0b671fb0d4dad4719f70bbdfb53d238e2/488588d58a152fabef3130cc936d205298edcda5a9e33f7757a3793732851763/probability-7709ebee871c3aee7658972f.json`. Comparison render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd959714c19fcc0f1325af171a8b8a1d43bab258106cd1edeae95823055fc460/80d67acb70b37ed56caf4b09013a1dd8f83e2b56e130b3df8ce2b941bc884e3b/probability-probability-7709ebee871c3aee7658972f-comparison.svg`.

The named `chaosx_ai_probability_auditor` subagent route and a standalone decision-inspection route were not exposed in this session, so the direct `hoi4_probability_inspect`, `hoi4_probability_evaluate`, and `hoi4_probability_compare` routes were used with the discovered decision-weight adapter. Their partial status and unresolved helper/state inputs remain an explicit limitation. The offline wiki had no standalone special-project page in the snapshot; the special-project sections in the required Triggers, Effects, and On actions pages plus the installed vanilla special-project documentation were used as the available engine references.

## Remaining issues and parent actions

- Review whether the inherited fifteen-row mature-Theory density needs a separately accepted phasing or selection design; this tranche intentionally did not invent that system.
- Review the balance of component support-equipment/fuel burdens and the absence of Capacity occupation against the native component precedent.
- Run the user's live DLC-present and DLC-absent save validation, including all fifteen family transitions and the six-component Singularity sequence.
- Re-run the probability compare after any parent changes to the board, constants, or AI values; the current MCP result is partial rather than a complete balance proof.

No native special-project definition, Mengele stage-provider file, focus tree, GUI, event/evolution, raid, generic unit package, model, asset, catalog, or unrelated system was changed by this tranche. No simplification was made to the requested family coverage or Singularity component chain; the only validation omissions are the prohibited live-game run and the unavailable named auditor route.
