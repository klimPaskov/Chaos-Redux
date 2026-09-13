# Event 016 no-DLC closure review

Date: 2026-09-06.

Status: closure review complete for the no-DLC board and shared Singularity registry. The worktree remains unstaged and uncommitted. No Hearts of Iron IV session was launched.

## Scope and acceptance

The accepted source contract is `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` and the implementation baseline is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_no_dlc_project_progression_fallback_2026-09-05.md`.

The review preserves all fifteen Prototype families, the six causal Singularity components, centralized costs and timers, canonical stage receipts, no-DLC-only visibility, terminal cleanup, and transfer cleanup. It adds no new family, action, project definition, GUI, focus, model, or Mengele mechanic.

The shared `brilliant_scientist_project_fallback_prototype` table remains stable with fifteen family profiles. The `brilliant_scientist_project_fallback_singularity_component` table remains stable with six component profiles and centralized durations. These constants are review-ready dependencies for both the no-DLC consumers and the parent-owned Mengele quote consumer; no new cost values were introduced in this closure pass.

## Issue list sorted by severity

1. High, fixed: `brilliant_scientist_register_singularity_component` previously entered the Kruger registry whenever the current host matched, so a `none`, out-of-range, or fractional temporary selector could inflate the array and count without setting a valid component flag. `brilliant_scientist_singularity_component_input_is_valid` now accepts exactly the six existing enum equalities for command core, power link, containment lattice, temporal authenticator, delivery architecture, and fail-deadly governor. The Kruger branch requires that validator before the existing idempotent array insert, count increment, six-way flag dispatch, or native completion check.

2. High, fixed: no-DLC Singularity Prototype research and native auto-completion previously relied on a count gate without one shared integrity contract. `brilliant_scientist_singularity_components_are_complete` now requires the exact six count, all six existing component flags, and all six canonical registry memberships. Both `brilliant_scientist_can_research_singularity_prototype` and the native registry auto-completion branch call it, so count six with a missing flag or missing registry entry remains blocked.

3. Medium/high, fixed: the fallback rows could remain visible after a terminal or Laboratory World lock because the family research helpers do not themselves reject every terminal flag. All fifteen Prototype rows and all six component rows now reject the country terminal lock, Laboratory World terminal flag, Singularity terminal flag, and `world_end` directly in `visible`. The terminal fixture now includes six component entries, six component flags, and an active Prototype receipt so both visibility and cleanup expectations are represented.

4. Medium, fixed: an active no-DLC Prototype receipt must remain represented until its matching timed decision settles, while a terminal or invalid context must close it. Each Prototype visibility block retains an exact active-family/active-Prototype-stage branch, and the canonical cancellation/finalization helpers remain the only settlement path.

5. Medium, fixed: all twenty-one no-DLC payment triggers use inclusive support-equipment, fuel, and political-power thresholds and retain family-specific reserve-resource gates. The board rows expose the matching custom cost trigger and centralized political-power hint.

6. Medium, unresolved by design: a mature Theory portfolio can show up to fifteen Prototype rows in the existing category. No phasing or selection system was invented in this bounded closure review; a separate accepted design would be required to reduce that inherited density.

7. Low, intentional: component receipts use the timed decision's civilian-factory reservation and consume support equipment and fuel, but do not deduct project Capacity. This matches the existing native component-project precedent and does not create a second project ledger.

## Decision category lifecycle

The only category remains `brilliant_scientist_directorate_category`.

The fifteen IDs are `brilliant_scientist_fallback_computation_prototype`, `brilliant_scientist_fallback_electronics_prototype`, `brilliant_scientist_fallback_materials_prototype`, `brilliant_scientist_fallback_rocketry_prototype`, `brilliant_scientist_fallback_high_energy_prototype`, `brilliant_scientist_fallback_biomedical_prototype`, `brilliant_scientist_fallback_teleportation_prototype`, `brilliant_scientist_fallback_cloning_prototype`, `brilliant_scientist_fallback_robotics_prototype`, `brilliant_scientist_fallback_paleogenetics_prototype`, `brilliant_scientist_fallback_xenobiological_synthesis_prototype`, `brilliant_scientist_fallback_biological_weapons_prototype`, `brilliant_scientist_fallback_alien_arms_prototype`, `brilliant_scientist_fallback_temporal_prototype`, and `brilliant_scientist_fallback_singularity_prototype`.

The six component IDs are `brilliant_scientist_fallback_singularity_command_core`, `brilliant_scientist_fallback_singularity_power_link`, `brilliant_scientist_fallback_singularity_containment_lattice`, `brilliant_scientist_fallback_singularity_temporal_authenticator`, `brilliant_scientist_fallback_singularity_delivery_architecture`, and `brilliant_scientist_fallback_singularity_fail_deadly_governor`.

No-DLC rows require the current Event 016 host and absent `Gotterdammerung`. Native rows retain the positive DLC route. A valid Theory family exposes its paid timed Prototype adapter. The Prototype start uses the canonical stage ledger, reserves the centralized Prototype Capacity delta, and consumes the mapped support equipment and fuel. Completion calls the existing stage output path; cancellation and terminal closure finalize only the exact active receipt.

The six components are separate paid timed receipts. A component completion calls the canonical registry, which is idempotent by array membership and component flag. The no-DLC Prototype remains unavailable until the count and all six flags are present. Partial chains never auto-advance the Prototype.

## Cognitive-load notes

The tranche adds no category, tab, scripted GUI, recurring mission, or unrelated counter. All fifteen Prototype families can still be visible in a fully eligible Theory portfolio; this is the only material density concern and remains a parent-level balance/design decision.

The six component rows are individually hidden after their own completion flags and are terminal/world-end hidden. Their visible cost text separates political power, civilian-factory reservation, support equipment, and fuel from non-consumed strategic-resource reserve gates.

Every displayed value has a clear response: political power is paid on decision start, civilian factories are reserved for the timer, support equipment and fuel are consumed by the canonical no-DLC stage helper, reserve resources are checked but not consumed, and completion advances the existing project ledger and unlocks downstream stages.

## Mission and timed-receipt quality

These objects are timed decisions rather than missions. The owner is the current Event 016 host, the category is `brilliant_scientist_directorate_category`, and there is no map region because the existing project ledger owns family and facility context.

Requirements are the family-specific Theory entry, host/facility/scenario/incident gates, no-DLC gate, capacity and payment burdens, and mapped reserve resources. Prototype durations use `brilliant_scientist_project_duration.<family>_prototype`; component durations use the six centralized component duration constants.

Success settles the matching receipt and applies the canonical ledger/output path. Failure or cancellation settles the matching receipt without a refund. Terminal cleanup cancels active fallback receipts without reward. Duplicate callbacks are blocked by exact family/stage receipt matching, active flags, and the component array guard. No new recurring mission or map target exists.

## Cost and requirement clarity

Each fallback decision has exactly four displayed spendable burden types: political power, civilian-factory reservation, support equipment, and fuel. Strategic resources are prerequisite reserves only and are shown separately. The English localisation contains twenty-one fallback cost keys with icon coverage for `£pol_power`, `£civ_factory`, `£support_equipment_text_icon`, and `£GFX_fuel_texticon`; reserve strings use `£resources_strip`.

The source audit found twenty-one no-DLC payment blocks, twenty-one inclusive support gates, twenty-one inclusive fuel gates, twenty-one inclusive political-power gates, and seventy reserve-resource gates. The stage helper zeros unrelated generic trucks, trains, manpower, experience, and resource-unit burdens before loading a no-DLC profile.

## AI validity and route locks

No numeric AI weight was changed in this closure pass. The fifteen Prototype rows retain the existing `ai_high` baseline and preferred/low-capacity modifiers. The six component rows retain the existing `ai_medium` baseline and preferred modifier. However, terminal visibility guards and the shared six-component integrity predicate change weighted candidate eligibility, so a same-scenario probability comparison is mandatory. DLC, host, facility, scenario, incident, terminal, and component-chain locks are source-wired.

The prior probability handoff recorded historical partial artifacts and current inspect/evaluate/sweep/render timeouts. This pass attempted the required same-scenario compare with the six named scenarios, the 21-ID pool, and the same board source on both sides using `mission_ai_will_do`; after correcting the fixture shape, MCP returned `PROBABILITY_SURFACE_EMPTY` with blocker `No weighted blocks matched this request` and no artifact. A second identical compare using `decision_ai_will_do` returned the same blocker. The required compare therefore remains unresolved because the installed adapters do not bind this board surface; no score, rank, or probability conclusion is claimed.

## Localisation and documentation

No new localisation key was needed in this closure pass. The existing twenty-one fallback cost strings and associated requirements, blocked-cost, reserve, effect, and cancellation strings remain aligned with the current IDs and four displayed spendable burden types.

`docs/events/016_brilliant_scientist/systems/projects.md` records the shared registry dispatch, strict provider ownership, six-component chain, terminal behavior, and no cross-program writes. The fixture remains `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_NO_DLC_PROJECT_FALLBACK_2026_09_05.scenarios.json`.

## Cleanup, duplicate, and exploit review

`brilliant_scientist_close_active_project_stage_on_terminal` clears an active component receipt and closes an active fallback stage without applying normal completion output. Host-transfer reconciliation clears transient component receipt state while preserving completed component history. Cancellation does not refund the already-paid burdens.

The valid Mengele provider branch is evaluated first in `brilliant_scientist_register_singularity_component` and calls the private authenticated adapter. The current-host Kruger branch now requires the existing selector validator before touching the Kruger array/count; the ordinary-family `brilliant_scientist_record_new_project_prototype` callback remains selector-independent. The private adapter authenticates the exact six native special-project outputs and writes only Mengele flags/counts; it does not recurse into the generic registry or write Kruger state. The six native component callsites remain in `common/special_projects/projects/016_brilliant_scientist_projects.txt`; no native project definition was changed.

## Files and identifiers reviewed or changed

Closure source changes are in `common/decisions/016_brilliant_scientist_directorate_project_board.txt` (the 15 Prototype rows at lines 5028-5763 and six component rows at lines 5765-6010), `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt` (`brilliant_scientist_can_research_singularity_prototype`, `brilliant_scientist_singularity_component_input_is_valid`, and the 21 no-DLC payment gates), and `common/scripted_effects/016_brilliant_scientist_project_effects.txt` (`brilliant_scientist_register_singularity_component` at lines 1399-1432).

Closure documentation/fixture changes are in `docs/events/016_brilliant_scientist/systems/projects.md` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_NO_DLC_PROJECT_FALLBACK_2026_09_05.scenarios.json`.

Stable dependency paths reviewed but not changed by this closure patch are `common/script_constants/016_brilliant_scientist_project_constants.txt`, `localisation/english/016_brilliant_scientist_projects_l_english.yml`, `common/scripted_effects/016_brilliant_scientist_effects.txt`, and the six native component callsites in `common/special_projects/projects/016_brilliant_scientist_projects.txt`. These files are already edited by the broader Event 016 tranche in the shared worktree; their current table, localisation, cost-loader, and native-callsite content is the dependency accepted here.

The parent-owned `common/on_actions/016_brilliant_scientist_project_on_actions.txt` and Mengele bridge/stage files were not touched by this review. The parent has the separate strict-owner Mengele completion branch and private helper.

## Validation and blockers

Source checks passed with balanced braces: project effects 1668/1668, project triggers 1070/1070, and the board 2931/2931.

The selector source check found six exact enum equality branches and source-model outcomes of accepted values `1,2,3,4,5,6` and rejected values `0,7,-1,0.5,5.5`. The registry check confirmed provider-first dispatch, the selector validator only in the Kruger Singularity branch, the ordinary-family recorder remains unguarded by the component selector, the duplicate array guard before both array/count mutation, and no recursion or cross-program write. The shared integrity source check found an exact count comparison, six flags, and six array memberships, with exactly one research reference and one native auto-completion reference. The complete fixture has count six, six entries, and six flags; the partial fixture has count three; the zero fixture has count zero.

The board source check found 15 Prototype rows, six component rows, 21 terminal/world-end visibility guard sets, 21 fallback custom cost triggers, and 21 fallback political-power hints. The fixture parsed as schema `1.0` with 21 candidates and six scenarios; its terminal-lock state has an active Prototype receipt, six entries, and all six component flags.

The cost-gate audit found zero strict support/fuel comparisons in the no-DLC payment section and twenty-one inclusive support, fuel, and political-power comparisons, plus seventy reserve-resource gates. The constants audit found fifteen family profiles and six component profiles. No numeric AI weights were modified, but weighted candidate eligibility changed and the mandatory compare remains unresolved as described above.

Read-only Event 016 MCP inspection/render calls were attempted with narrow and scan queries but did not return within the bounded wait and were terminated. The exact blocker was the route hanging without an artifact; no MCP event evidence is claimed. Probability inspect/evaluate/sweep/render timeouts and the corrected compare adapter blockers are documented in this handoff and `016_no_dlc_probability_review_2026-09-06.md`. Live gameplay/DLC matrix validation was skipped because agents must not launch HOI4; the user owns live consumer validation.

Remaining issues are the inherited fifteen-row category density, the intentional no-Capacity component precedent, and unavailable current MCP engine evidence. No simplification was made to the fifteen-family or six-component contract.

Plan handoff: none.

## 2026-09-08 parent review: later-stage compatibility gap

Disposition: implemented in source after the current weighted baseline was captured; matching probability comparison remains pending.
Acceptance basis is the user's Final Completion Plan requirement that the existing decision-led board preserve core project progression and outcomes without DLC special-project presentation.
The Prototype/component review above does not prove this later-stage requirement.

The baseline `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt` made two paid Weaponization gates depend on alternatives that all require Götterdämmerung:

- `brilliant_scientist_can_begin_rocketry_weaponization`: Long-Range Ballistic Missile or Supersonic Jet.
- `brilliant_scientist_can_begin_high_energy_weaponization`: Thermonuclear Bomb or Nuclear Warheads.

Installed vanilla `rocket_projects.txt`, `air_projects.txt`, and `nuclear_projects.txt` explicitly gate all four Weaponization alternatives in their `allowed` blocks with `has_dlc = "Gotterdammerung"`.
The Deployment gates remain unchanged: Ballistic Missile and Axial Jet Engine are not gated by that DLC, and High Energy has a base-game Nuclear Bomb alternative.
The initial four-gate suspicion was therefore narrowed by direct vanilla review before any gameplay patch.
The exact preceding Deployment receipt, board validity, and real affordability remain required.
Without the required DLC, that authentic preceding decision stage must satisfy the Weaponization native-project-only branch; with DLC, the existing native-project alternatives remain required.
This adaptation must not mark a native project completed, invent native history, grant an additional reward, or bypass a real resource or technology requirement.
The same explicit compatibility basis applies to the five conventional private Mengele adapters under implementation.
The current probability owner is comparing the two affected existing decision IDs under matching DLC, predecessor, native-completion, and affordability scenarios before and after the patch, with Deployment retained as an unchanged control where included.
The parent added the no-DLC alternative to exactly these two Weaponization OR blocks after baseline `probability-07549106fa411f7bcdd36d84` was frozen with twenty scenarios and hash `0554685fc1eca42c6fa8be6dfb7773ce9226a038e3a193c9e936bdef906c3971`.
Both exact Deployment receipts, board-validity checks, and affordability gates remain outside and required by the OR blocks.
The baseline is score-only evidence, not proof that every live eligibility predicate was bound; its flat-input limitation is preserved in `016_mengele_conventional_probability_2026-09-08.md`.
No MCP comparison acceptance is claimed until the matching post-change audit returns.
