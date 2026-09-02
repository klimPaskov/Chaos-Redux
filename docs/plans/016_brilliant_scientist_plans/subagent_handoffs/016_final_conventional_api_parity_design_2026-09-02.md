# Event 016 final conventional API and Mengele parity design

Date: 2026-09-02.

Status: Bounded source review plus the explicitly authorized neutral package helper implementation for the parent owner.

Scope: This handoff reviews the existing neutral custom-technology API, conventional technology-action access, the Mengele project bridge, DHRondan operational gating, computation research-slot ownership, and the existing project/runtime registries.

No existing gameplay files, decisions, constants, technologies, modifiers, projects, GUI, or localisation were edited outside the three newly owned conventional API source surfaces.

No commit, model regeneration, live game launch, or in-game acceptance claim is made.

## Executive findings

The existing public API is complete for its documented eighteen hidden technologies: seven operational selectors, seven weaponization selectors, and four xenobiological control selectors.

The promoted final contract now explicitly requires the six existing conventional families to expose full-strength neutral operational and weaponization package grants through `chaosx_grant_conventional_technology_package` and `chaosx_reconcile_conventional_technology_runtime`.

The existing API does not expose conventional wonder-technology actions, and its random operational grant correctly remains a seven-family selector rather than a generic fifteen-family portfolio picker.

The eight repeatable conventional actions remain Kruger-current-host decisions in `brilliant_scientist_directorate_category`; a neutral selector alone cannot expose them because the shared action-system trigger requires current-host scope in addition to the family completion flags and shared locks.

The Mengele bridge currently covers nine non-cloning Event 016 native prototypes, but computation, materials, and biomedical completion only add provider prototype modifiers while the other six non-cloning branches dispatch to the seven-family neutral API.

Under the literal final contract that Mengele can eventually unlock every existing project family through his own program, the current registry is incomplete for electronics, rocketry, high-energy, biological weapons, and Singularity, and cloning remains a separate Mengele program rather than a bridge branch.

The DHRondan Mengele branch still treats vanilla `rocket_engines` and `atomic_research` as stand-ins for missing operational outcomes, while the Event 016 contract requires operational Alien Arms, Rocketry, Materials, High Energy, and Computation outcomes.

The existing provenance encoding is `selector * provenance_stride + source`, with `provenance_stride = 1000000`, and the existing API source validator now enforces the documented lower-inclusive and upper-exclusive range.

The smallest safe closure preserves the current seven-family and eleven-upgrade IDs, adds no hidden technology or project-family IDs, reuses the six existing conventional family IDs and two existing stage IDs, and applies the same idempotent bounded provenance contract to the new package writer.

The conventional action surface remains an existing consumer owned by the parent; this implementation supplies the durable package flags that the neutral category and action gates must consume without adding a second category or GUI.

## Source call graph

| Surface | Current source path | Current behavior | Parity consequence |
| --- | --- | --- | --- |
| Neutral operational grant | `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:35-92,359-378` and `common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt:12-24,170-174` | Valid selector dispatches one of seven existing hidden operational technologies, records durable grant flags and optional provenance, then rebuilds the external runtime package. | This is a technology API, not a conventional-action or fifteen-family project API. |
| Neutral upgrade grant | `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:94-140,380-527` and `common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt:26-42,176-229` | Seven weaponization selectors and four xenobiological controls use prerequisite and exclusivity queries, durable flags, optional provenance, and runtime reconciliation. | Keep all eleven IDs and prerequisite behavior unchanged. |
| Neutral random grant | `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:529-592` | Candidate rows are the seven operational families only and use the existing random candidate weight constant. | Do not widen this pool to conventional actions or all fifteen project families. |
| Public runtime reapply | `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:594-625` and `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt:426-542` | Durable external flags reapply hidden technologies and the existing external package after runtime reset. | Any new provider or neutral entitlement needs its own idempotent reapply path and must not write Kruger project state. |
| Native prototype completion | `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1240-1255` | `brilliant_scientist_record_new_project_prototype` routes Mengele completions to the bridge and Kruger completions to native stage/ledger handling. | A provider completion must not call the Kruger stage-output helper. |
| Mengele bridge | `common/scripted_effects/016_mengele_project_bridge_effects.txt:11-117` and `common/scripted_triggers/016_mengele_project_bridge_triggers.txt:9-94` | Nine non-cloning native project families are available to Mengele; three set provider prototype modifiers and six call the seven-family neutral API. | The bridge is provider-owned but does not yet provide full operational parity for all existing families. |
| Mengele registry | `common/scripted_effects/germany_mengele_effects.txt:2345-2560` | Researchable and random registry rows include zombies, black plague, cloning, computation, materials, biomedical, teleportation, robotics, paleogenetics, xenobiological synthesis, alien arms, temporal, and DHR. | Electronics, rocketry, high-energy, and Singularity are not in the current provider registry. |
| Conventional actions | `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt:8-105` and `common/decisions/016_brilliant_scientist_technology_actions.txt:18-166` | Eight decision rows use the shared system gate, family flags, target gates, payment effects, factory occupation, timed effects, cooldowns, and AI blocks. | The shared system gate requires current host; neutral access needs an explicit contract and authorization query. |
| Conventional action effects | `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt:8-122` | Existing effects apply country or state effects and write used/history markers; sensor saturation applies a country dynamic modifier and records the selected state. | Reuse only through an explicit action path that preserves targets and payment semantics; sensor region behavior is not source-proven. |
| DHRondan gate | `common/scripted_triggers/016_dhrondan_contact_triggers.txt:26-60` | KRG requires Event 016 operational flags; Mengele requires three provider project flags plus vanilla `rocket_engines` and `atomic_research`. | Replace stand-ins with exact provider-owned operational receipts if literal DHR parity is required. |
| DHRondan project | `common/special_projects/projects/016_dhrondan_envoy_project.txt:15-45` | One existing special project consumes the DHR availability trigger and has its existing breakthrough/resources/output. | No second DHR project is needed. |

## Concrete scenario traces

### Neutral technology API

A neutral country calls the existing operational API with a selector from one through seven.

The core grants the matching hidden technology and durable external grant flag, then the provenance writer appends a receipt only when the optional source is valid, and the runtime package is rebuilt.

The path intentionally creates no native project history, project facility, active stage, capacity reservation, Directorate flag, host provider, opening unit, stockpile, evolution, or achievement.

That behavior satisfies the documented technology API boundary and must remain unchanged.

A request for computation, electronics, materials, rocketry, high-energy, biomedical, biological weapons, or Singularity cannot currently be represented by the seven operational selector.

If the final closure requires those conventional outcomes through a neutral API, they need a separate explicit portfolio/action selector and receipt path rather than an overloaded seven-family selector.

### Duplicate and stale neutral calls

Repeated calls with the same valid operational selector must remain idempotent for the hidden technology, durable grant flag, runtime package, and provenance entry.

The provenance contract must reject a source below `provenance_minimum_source` or at or above `provenance_stride` without rejecting the underlying technology or portfolio grant.

The collision is concrete: selector 1 with source 1000001 encodes to the same integer as selector 2 with source 1 when the stride is 1000000.

The bounded owner fix is a shared query used by both existing provenance writers and any future writer, enforcing `1 <= source < provenance_stride` as a source contract and leaving invalid or missing source provenance-free.

### Seven-family random grant

`chaosx_grant_random_custom_operational_technology` has seven candidate rows, each guarded by the corresponding unowned query and using the existing random candidate weight.

It must stay a seven-family lottery so existing random semantics and probability baselines are preserved.

If a caller needs a generic conventional portfolio result, add an explicit selector/query or package operation with its own declared candidate set and acceptance contract; do not silently append conventional actions or the remaining project families to this random block.

The required bounded probability inspection used `direct_random` against `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt` and identified the source as a `random_list` surface with eighteen available rows elsewhere in the file, but did not produce a direct identifier match for the scripted effect name.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5058f1aab66358a5ea7fd36519ff941b14c32fb9f7bf614650b1c6ae8de08499/2276f3875c09027b0d5cd864d80ea04929a76c80a33512743872be6a00178d70/probability-inspect-fd930265e87d.json`.

This is source discovery only and is not a probability acceptance, balance claim, or reason to change the pool.

### Conventional action access

The current action trigger chain is `brilliant_scientist_technology_action_system_is_available` followed by a family-specific completion flag and damage/suspension/stolen guards.

The shared system trigger requires `brilliant_scientist_is_current_host`, no containment action, no project stage, no incident, no terminal commitment, and no world end.

The six conventional family gates are computation, electronics, materials, rocketry, high-energy, and biomedical, while the decision surface contains eight actions because biomedical supplies both emergency and epidemic outcomes and rocketry supplies both high-speed and long-range outcomes.

Therefore an external country with a valid neutral technology grant still cannot use an existing action decision without current-host scope.

The current action effects also carry target scope and payment semantics, so a generic technology grant cannot safely imply that a target-specific action was executed.

The source-defined action effects are not all equivalent to conventional technology packages: predictive campaign, sensor saturation, high-speed strike, field projectors, emergency regeneration, and epidemic control apply country modifiers, while materials synthesis and long-range delivery use state-scoped effects.

Sensor saturation is documented as region-targeted, but `activate_sensor_saturation` applies `brilliant_scientist_sensor_saturation_active` at country scope and only records `FROM = { set_state_flag = brilliant_scientist_sensor_saturation_history }`.

No existing region-specific runtime consumer was found in the bounded source trace, so a new regional modifier or inferred regional behavior must not be added under this parity plan.

### Ordinary Mengele completion

Native special-project completion enters `brilliant_scientist_record_new_project_prototype` and then `brilliant_scientist_record_mengele_project_prototype` for a Mengele provider.

The computation, materials, and biomedical branches set the corresponding provider completion flag and provider dynamic modifier, with computation also setting the provider completion state.

Those three branches do not run the full Kruger project stage dispatcher and do not provide the native deployment output, including the computation research-slot outcome.

The teleportation, robotics, paleogenetics, xenobiological synthesis, alien arms, and temporal branches call the existing seven-family API and therefore produce the matching full neutral operational package rather than a Kruger project ledger.

Cloning is completed through `germany_mengele_complete_cloning_project` and its refinement helper, outside the nine-branch bridge.

This is safe with respect to Kruger state, but it is not literal all-family conventional parity until the provider-owned missing branches and full outcomes are specified.

### Native computation and provider/API computation

Native Kruger computation deployment grants one research slot behind `brilliant_scientist_computation_research_slot_active` and removes that slot when the native output is disabled.

A provider or neutral computation outcome must not set that Kruger flag, because that would fabricate Kruger Directorate state.

Use a provider/API-owned durable marker for the same one-slot entitlement and a shared presence query that recognizes either the native or provider marker before adding the slot.

The release path must remove the slot only when the releasing owner marker is present and the other owner marker is absent.

The marker and slot restoration must be idempotent across repeated grants and runtime rebuilds, and a native completion arriving after a provider completion must not add a second slot.

If the accepted contract keeps Mengele computation at prototype-only strength, the provider must not claim the native research-slot outcome; this is a contract-visible gap rather than a reason to write Kruger state.

### DHRondan ordinary and stale paths

The current KRG DHR branch already tests Event 016 operational completion flags and should remain unchanged.

The current Mengele branch tests completed Alien Arms, Materials, and Computation provider flags but substitutes vanilla `rocket_engines` and `atomic_research` for Rocketry and High Energy.

The ordinary failure path is a Mengele country with the three provider prototype flags and the two vanilla technologies but no Event 016 Rocketry or High Energy operational outcome; the current trigger incorrectly presents DHR work as available.

The inverse failure path is a Mengele country with an Event 016-owned provider Rocketry or High Energy outcome but without the vanilla technology; the current trigger incorrectly hides DHR work.

The minimum safe correction is an exact provider-owned operational-work query requiring five receipts or flags: Alien Arms, Materials, Computation, Rocketry, and High Energy.

The query must distinguish prototype-only completion from full operational completion and must not infer any receipt from vanilla technology.

No new DHR project, meter, GUI, project family, or probability surface is needed.

### No-DLC and runtime rebuild

The public API is ordinary scripted-effect logic and does not depend on a DLC-only GUI or native project completion.

Mengele availability and completion should remain driven by provider-owned flags and existing decision/special-project availability, then converge on one provider-owned result dispatcher.

`is_special_project_completed` alone is not proof of no-DLC parity because several required provider outcomes are currently represented only by bridge flags or neutral API flags.

Provider-owned modifiers must have provider-owned enable and reapply conditions; the existing project-stage modifiers require `brilliant_scientist_is_current_host` and therefore cannot be reused unchanged for a Mengele-only provider.

The runtime reapply path must preserve external technology grants and provider portfolio receipts without rebuilding Kruger stage arrays, capacity, facility, terminal, or Directorate history.

## Minimum safe owner patch

The package helper implementation is complete in the three newly owned API surfaces; the parent owns the existing consumer integration and provider wiring described below.

### 1. Preserve the existing technology API

Keep `chaosx_custom_technology_family` values 1 through 7 and `chaosx_custom_technology_upgrade` values 1 through 11 unchanged.

Keep all eighteen hidden technology IDs and their current core dispatch, prerequisite ordering, xeno exclusivity, runtime reapply, and seven-candidate random behavior unchanged.

The existing source-validity query enforces the documented interval `1 <= chaosx_custom_technology_source < chaosx_custom_technology_provenance_stride` for the two existing provenance writers and the new package writer.

Missing or invalid source input remains a valid grant with no provenance entry.

The new package writer uses the same family-ID-times-stride encoding and bounds in separate operational and weaponization arrays; those receipts are not a project-stage ledger.

### 2. Add the accepted conventional package API

The accepted contract requires an explicit six-family package API rather than an extension of the seven-family hidden-technology selector.

The implementation uses the existing `brilliant_scientist_project_family` IDs for Computation, Electronics, Materials, Rocketry, High Energy, and Biomedical and the existing Deployment or Weaponization stage IDs.

It persists `conventional_technology_<family>_operational` and `conventional_technology_<family>_weaponized` flags and reuses the existing matching full-strength dynamic modifiers.

`chaosx_grant_conventional_technology_package_core` validates the exact family and tier, sets neutral flags, reconciles the package, and returns temporary `chaosx_conventional_technology_grant_applied = 1` without recording provenance.

The public `chaosx_grant_conventional_technology_package` wrapper calls the core first, then records optional source provenance in separate `conventional_technology_operational_provenance` and `conventional_technology_weaponization_provenance` arrays with the existing family-ID-times-stride encoding and deduplication.

Weaponization establishes the operational flag before its weaponized flag and records both package receipts; invalid selectors are no-ops and invalid or missing source input does not block a valid grant.

The reconciliation helper is bounded to these six families and does not mutate the request selectors or optional source.

The parent owns the neutral decision-category and eight action-gate exposure, payment, target, timer, cooldown, cancellation, and AI integration.

The parent’s separate action-cost correction is outside this parity design and must not be folded into selector or provenance work.

### 3. Create a provider-owned conventional completion dispatcher

Extend the existing Mengele bridge or a private adjacent helper so provider completion dispatches by the existing `brilliant_scientist_project_family` IDs 1 through 15, without allocating a new family ID.

The dispatcher must receive the provider country as `ROOT`, the selected existing family ID, and the completion kind or operational tier from an already-guarded caller.

It must set only provider-owned completion markers, provider-owned dynamic modifiers, and provider-owned runtime receipts.

It must never call `brilliant_scientist_apply_project_stage_output`, set `brilliant_scientist_*_theory/prototype/deployment/weaponization_completed` flags, create a Kruger active stage, spend Kruger capacity, write Kruger facility state, or fabricate a Directorate project history entry.

The final contract requires full operational parity, so the provider dispatcher must expose a distinct operational receipt rather than treating the existing prototype modifier as a deployment receipt.

Provider modifiers need a provider-owned enable trigger and a runtime reapply path that survives loss of current-host scope.

### 4. Make computation slot ownership explicit

Use a provider/API-owned computation slot marker separate from `brilliant_scientist_computation_research_slot_active`.

Add one slot only when neither native nor provider marker is present, then set the owner marker atomically with the completion receipt.

On release, clear only the releasing owner marker and remove one slot only when no other owner marker remains.

The runtime rebuild must restore one slot from either owner marker and repeated rebuilds must not add another.

If a provider computation branch remains prototype-only, leave the slot absent and report the unresolved full computation outcome rather than fabricating a native marker.

### 5. Correct the DHR Mengele query

Add or reuse a provider-owned trigger that asks for exact Event 016 operational receipts for Alien Arms, Materials, Computation, Rocketry, and High Energy.

Replace only the Mengele branch of `dhrondan_envoy_craft_has_operational_work` with that trigger.

Leave the KRG branch, DHR visibility, DHR special project, target rules, resource costs, and existing output unchanged.

Do not use vanilla `rocket_engines` or `atomic_research` as fallback evidence for Event 016 outcomes.

### 6. Integrate the accepted package with existing action gates

The accepted contract requires the existing eight action rows to consume the matching neutral package flags through the parent-owned neutral category and action-gate integration.

The parent-owned integration must retain the shared no-containment, no-stage, no-incident, no-terminal, and no-world-end locks and must not make an unrelated family package satisfy another family’s action gate.

The package grant itself does not execute or pay for an action; the existing decision row remains responsible for target, payment, timer, cooldown, cancellation, and usage history.

Any neutral decision-row exposure must be checked for AI side effects and must not create duplicate decision rows or a new GUI.

### 7. Resolve sensor target semantics explicitly

Before claiming sensor saturation parity, identify an existing state or strategic-region runtime consumer for `brilliant_scientist_sensor_saturation_active` or revise the contract description to match the current country-wide modifier plus target history behavior.

Do not invent a regional dynamic modifier or treat the state history flag as a runtime regional effect.

## Selector and receipt contract

| Namespace | Existing or proposed IDs | Receipt meaning | Random behavior |
| --- | --- | --- | --- |
| `chaosx_custom_technology_family` | Existing 1-7 | Durable neutral operational technology grant. | Existing random helper remains exactly seven candidates. |
| `chaosx_custom_technology_upgrade` | Existing 1-11 | Durable neutral weaponization or xenobiological control grant. | No random widening. |
| `chaosx_conventional_technology_family` | Existing 1-6 for Computation, Electronics, Materials, Rocketry, High Energy, and Biomedical | Durable neutral conventional package selector. | Never added to the existing seven-family random helper. |
| `chaosx_conventional_technology_tier` | Existing Deployment or Weaponization stage IDs | Selects cumulative operational or weaponized package output. | Never added to the existing seven-family random helper. |
| `brilliant_scientist_project_family` | Existing 1-15 for provider-owned caller state | Provider-owned conventional completion may mirror existing family IDs, but must use provider receipts and not Kruger stage variables. | No new family IDs. |

All optional source values use the existing source variable and the same `1 <= source < provenance_stride` validation.

The selector component and source component should remain in a single unambiguous range, and separate receipt arrays may reuse the encoding but must retain their own semantic namespace.

An invalid selector is a no-op with no reward or receipt.

An invalid or missing source does not invalidate an otherwise valid grant; it produces no provenance record.

Repeated valid calls do not add a second hidden technology, provider modifier, research slot, action receipt, or provenance entry.

## Mengele family matrix

| Existing family | Current Mengele path | Current parity status | Minimum disposition |
| --- | --- | --- | --- |
| Computation | Bridge flag plus provider computation prototype modifier. | Prototype-only and no provider research-slot outcome. | Add provider full operational receipt and one-slot ownership for literal all-family parity. |
| Electronics | No Mengele bridge or registry row. | Missing. | Add provider-owned availability, completion, and output for literal all-family parity. |
| Materials | Bridge flag plus provider materials prototype modifier. | Prototype-only rather than full operational output. | Add provider operational receipt and output for literal all-family parity. |
| Rocketry | No Mengele bridge or registry row. | Missing and currently replaced by vanilla DHR stand-in. | Add provider-owned operational receipt/output and use it in DHR query. |
| High Energy | No Mengele bridge or registry row. | Missing and currently replaced by vanilla DHR stand-in. | Add provider-owned operational receipt/output and use it in DHR query. |
| Biomedical | Bridge flag plus provider biomedical prototype modifier. | Prototype-only rather than full operational output. | Add provider operational receipt and output for literal all-family parity. |
| Teleportation | Bridge calls neutral portal operational API. | Full neutral package path exists. | Preserve provider-owned provenance and runtime reapply. |
| Cloning | Separate `germany_mengele_complete_cloning_project` and refinement path. | Provider program exists outside bridge. | Preserve separate provider state; do not write Kruger cloning flags. |
| Robotics | Bridge calls neutral robot operational API. | Full neutral package path exists. | Preserve. |
| Paleogenetics | Bridge calls neutral paleogenetic operational API. | Full neutral package path exists. | Preserve. |
| Xenobiological Synthesis | Bridge calls neutral xenobiological operational API. | Full neutral package path exists. | Preserve. |
| Biological Weapons | Separate Event 020/zombie/black-plague systems, not bridge. | Not an Event 016 provider operational receipt in the reviewed path. | Require explicit contract mapping; do not infer from zombie or black-plague flags. |
| Alien Arms | Bridge calls neutral alien-infantry operational API. | Full neutral package path exists, but DHR must use an explicit provider operational receipt. | Preserve and expose exact DHR receipt. |
| Temporal | Bridge calls neutral temporal operational API. | Full neutral package path exists. | Preserve. |
| Singularity | Kruger component and terminal path only. | Missing provider path. | Contract blocker; do not invent a provider terminal, meter, GUI, or new family. |

This matrix distinguishes existing family IDs from completion strength and provider ownership.

It does not authorize promoting prototype modifiers to deployment, adding a terminal branch, or treating unrelated Event 020 systems as Event 016 outcomes.

## Proposed helper map

| Helper or query | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| Existing bounded source query | Country scope; reads optional `chaosx_custom_technology_source`. | Boolean source validity for `1 <= source < provenance_stride`; no mutation. | Existing technology and upgrade writers, then any portfolio/provider writer. |
| Conventional selector validity query | Country scope; reads existing family and tier selectors. | Boolean exact-ID validity; no mutation. | Neutral package API and native/provider dispatcher. |
| Conventional entitlement query | Country scope; reads neutral package flags and shared locks. | Boolean authorization; no mutation. | Parent-owned action trigger path and DHR provider query. |
| Provider conventional completion core | Provider country scope; inputs existing family ID and completion tier. | Provider-owned flags, modifiers, receipts, and optional computation-slot owner marker. No Kruger state. | Mengele bridge and provider-owned program completions. |
| Provider runtime reapply core | Provider country scope; reads durable provider receipts. | Idempotently restores provider modifiers and one computation slot. No project stage/capacity. | Existing runtime rebuild path after provider package restore. |
| Computation slot presence query | Country scope; reads native and provider owner markers. | Boolean one-slot presence. | Native and provider completion/release wrappers. |
| DHR provider operational-work query | Mengele provider scope; reads five exact provider operational receipts. | Boolean DHR operational work. | `dhrondan_envoy_craft_has_operational_work` Mengele branch only. |
| Optional action execution core | Country scope; requires validated target and action entitlement. | Reuses existing payment, target, timed modifier, cooldown, and used/history effects. | Only if neutral action execution is explicitly accepted. |

If a dynamic selector cannot be passed to a static Clausewitz effect field, use the repository’s existing `meta_effect` pattern rather than inventing parameter syntax.

Do not use raw numeric database IDs as country scopes; persistent provider pointers or event-target scopes must be established by existing supported scope mechanisms before a country-scoped core runs.

## Availability, no-DLC, and accounting rules

Provider availability can reuse existing native special-project OR gates where the provider owns the project, but completion accounting must end in provider-owned receipts rather than Kruger project arrays.

The provider path must not charge a second native payment when completion is already supplied by a provider program, and a neutral grant must not silently charge a decision payment unless it is an explicit action execution call.

No branch may grant a free hidden technology in place of a required operational result, and no branch may use a prototype-only dynamic modifier as evidence of a full deployment receipt.

The computation slot is one shared outcome, not one slot per source, and its owner markers must be reconciled before any add or removal.

The existing action duration, cooldown, target, and AI semantics remain owned by the action surface; this handoff does not rebalance the eight cost profiles.

The existing source mismatch where materials synthesis checks `light_civilian_factories = 2` while its timed modifier occupies `HEAVY_FACTORY_USE = 3` is a separate action-surface issue and is not folded into the parity design.

## Risks and contract blockers

The promoted contract explicitly covers full-strength neutral conventional packages, while target-specific action exposure remains an existing consumer integration owned by the parent.

The phrase “Mengele can eventually unlock all project families” is broader than the current nine-branch bridge and includes missing conventional families plus the Kruger-only Singularity route.

Singularity cannot be safely closed by mapping to an existing seven-family technology because it has component completion, terminal, meter, and world-state semantics that are explicitly outside the bridge contract.

Sensor saturation cannot be called region-targeted from the reviewed source without an existing runtime consumer or a contract correction.

The existing action category is host-only in the reviewed source and no dedicated decision-inspection MCP route was available in this runtime, so neutral category exposure remains parent-owned source integration rather than an engine acceptance claim.

Provider dynamic modifiers currently require current-host scope through `brilliant_scientist_is_current_host`; any provider parity implementation needs explicit provider-owned enable/reapply handling.

The source-only review does not establish that all native special-project availability gates survive every DLC combination; the no-DLC claim must be validated by the parent against the final provider-owned completion path.

## Validation boundary

Required offline Paradox wiki pages were read for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, technology modding, equipment modding, and unit modding.

The relevant vanilla documentation was read for effects, triggers, script constants, scopes, event targets, dynamic modifiers, special-project completion, technology grants, and research-slot effects.

The bounded `hoi4.probability_inspect` discovery is recorded above and is not a probability acceptance or balance result.

The earlier read-only `hoi4.tech_inspect` scan returned status `ok` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/55a4f393ec3fc36b143084e3dcf800146e047a1ec6c68015aea884e0c99153ec/0eeda93f94ec8056fa1288f8dd1f1ecdcb724cd0ae49671543e793591c237977/technology-scan-2a862ecb7112.json` and broad diagnostics; it is structural evidence only and not a completion or no-DLC acceptance.

No decision-inspection MCP route was exposed in this runtime, and no live game, model generation, GUI rewrite, event rewrite, or gameplay validation was run.

## Ownership and follow-up

Parent implementation owns all gameplay changes, source-ID range enforcement, action-cost corrections, provider registry changes, DHR trigger changes, and final contract disposition.

The probability owner owns the frozen seven-family random baseline and any required before/after comparison; this review makes no weight or probability claim.

The action owner must decide whether neutral access is an entitlement-only API, a direct target-aware execution API, or intentionally out of scope because the current contract names Kruger-current-host decisions.

The provider owner must decide whether “all project families” includes a provider-owned Singularity-equivalent outcome; this handoff recommends treating that as blocked until a no-new-terminal/meter/GUI-compatible contract is supplied.

## Implementation disposition

The accepted neutral package API is implemented in `common/scripted_effects/016_conventional_technology_api_effects.txt`, `common/scripted_effects/016_conventional_technology_api_effects.md`, and `common/scripted_triggers/016_conventional_technology_api_triggers.txt`.

`chaosx_conventional_technology_request_is_valid` accepts exactly the six existing conventional family IDs and the existing Deployment or Weaponization tier IDs.

`chaosx_requested_conventional_technology_is_owned` checks the exact requested family and tier against its durable neutral operational or weaponized flag.

`chaosx_has_conventional_operational_technology` and `chaosx_has_conventional_weaponized_technology` provide bounded any-owned queries across the six families.

`chaosx_grant_conventional_technology_package_core` is the private shared country-scope core for public neutral grants and native completion callers.

The core validates exact input, establishes operational before weaponization, calls reconciliation, and returns temporary `chaosx_conventional_technology_grant_applied = 1` only for a valid request.

The core does not write optional provenance, so native callers cannot consume an unrelated public `chaosx_custom_technology_source`.

The public wrapper writes only after core success and deduplicates encoded receipts in `conventional_technology_operational_provenance` and `conventional_technology_weaponization_provenance`.

`chaosx_reconcile_conventional_technology_runtime` reuses the existing full-strength Theory, Prototype, Deployment, and Weaponization dynamic modifiers and leaves request selectors and optional source untouched.

Computation slot reconciliation adopts an existing `brilliant_scientist_computation_research_slot_active` marker into `conventional_technology_computation_research_slot_active` without adding a slot, or adds exactly one existing research-slot gain when neither marker exists.

Reconciliation never removes a learned slot and never fabricates the old native marker.

Parent-owned follow-up surfaces are the existing dynamic-modifier enable/removal conditions, native completion and disable/transfer paths, neutral decision category and action gates, CXT/provider/global registry integration, and any Mengele implementation.

Focused source traces cover repeated valid grants, weaponization-first requests, invalid selectors, invalid or missing source, operational-after-weaponization requests, duplicate provenance, two package providers, and native computation-slot adoption.

No gameplay files outside the three new API surfaces were edited by this implementation, and no commit or live-game validation was performed.
