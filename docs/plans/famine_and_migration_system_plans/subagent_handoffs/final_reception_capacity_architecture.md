# Final Reception Capacity Architecture Handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: architecture-only handoff for the famine and migration system. No gameplay files, constants, localisation, map files, or on-actions were changed by this audit, and no commit was made.

Owner handoff: the parent implementation owner must turn this contract into the scripted effects, triggers, constants, adapters, and consumer changes after reviewing the explicit blockers below.

## 1. Decision and binding contract

The current reception-capacity value is not a truthful capacity measurement. `common/decisions/famine_migration_decisions.txt:2683-2687`, `:2732-2736`, and `:2811-2816` derive one absolute value from civilian factories using the file-local `@FM_CAPACITY_PER_CIV` and `@FM_CAPACITY_BASE`, then pass it to `famine_migration_refresh_reception_capacity`. The helper at `common/scripted_effects/chaosx_famine_migration_effects.txt:2014-2028` merely stores the request and registers the country, so the published value is stale as soon as food, shelter, transport, medical conditions, administration, state control, war, outbreak, contamination, or current load changes.

The contract below keeps the exact country and state reception-load ledger already established by `famine_migration_apply_reception_delta`, while replacing the request writer with one centralized dynamic recalculation. The public country value remains `famine_migration_reception_capacity`, but it means effective current reception capacity in people, not civilian-factory capacity and not gross service potential.

The decision category continues to expose exactly three country-level values: primary `Displacement Load`, supporting `Reception Capacity`, and supporting `Border Policy`. Gross capacity, component scores, safe-state counts, validity, revision, and pressure factors are internal diagnostics and must not become extra visible category values.

The state value remains `famine_migration_state_reception_load` in people. It is an exact projection of people physically received in that state and must stay paired with the owner country's exact `famine_migration_reception_load`. Capacity is country-wide; state load is state-local. Neither value may be inferred by scanning the other ledger.

The implementation must fail closed when the required evidence is absent. A country with no registered candidate state, no safe population, an unproven shelter adapter, or an unproven medical adapter publishes zero capacity with an invalid flag rather than inheriting the old factory value or fabricating a minimum of one person. The existing `famine_migration_destination_selection_constants.txt` minimum-capacity threshold remains a trigger threshold only and must not create phantom capacity.

## 2. Evidence reviewed

The required local repository instructions were reloaded from the current `AGENTS.md` before finalising this handoff. The full `chaos-redux-state-ledgers`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents` skill instructions were read and applied. The state-ledger rules are especially binding: sparse aligned registries, exact paired state/country deltas, no whole-world recurring scans, and explicit mapmode evidence or a blocker.

The famine and migration source-of-truth material reviewed was `docs/specs/famine_and_migration_system_specs/README.md`, the coding and decision/missions prompts, specification parts 1 through 8, the asset, death-reason, decision-map, historical-profile, input/output, integration, and probability-scenario matrices, `famine_and_migration_system_improvement_loop_closure.md`, `docs/plans/famine_and_migration_system_plans/completion_report.md`, `source_of_truth_map.md`, `resume_packet.md`, `improvement_review_addendum.md`, `mapmode_validation.md`, `handoff_dispositions.md`, and the existing handoffs in `docs/plans/famine_and_migration_system_plans/subagent_handoffs/`.

The current scripted sources reviewed were `common/script_constants/famine_migration_constants.txt`, `common/script_constants/famine_migration_adapter_constants.txt`, `common/script_constants/famine_migration_destination_selection_constants.txt`, `common/decisions/famine_migration_decisions.txt`, `common/scripted_effects/chaosx_famine_migration_effects.txt`, `common/scripted_effects/famine_migration_destination_selection_effects.txt`, `common/scripted_effects/famine_migration_cxt_test_effects.txt`, `common/scripted_triggers/famine_migration_destination_selection_triggers.txt`, `common/scripted_triggers/chaosx_famine_migration_triggers.txt`, the active registry and on-action files, `common/map_modes/chaosx_state_map_modes.txt`, the migration map scripted localisation, and the category/localisation files.

The offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding were consulted. The relevant vanilla documentation reviewed included `documentation/script_concept_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/dynamic_variables_documentation.md`, `common/script_constants/documentation.md`, and the related documentation for arrays, event targets, building levels, state population, civilian factories, war, ownership, and control.

## 3. Current writer and consumer census

### 3.1 Country capacity writers and lifecycle

| Surface | Current evidence | Required architectural disposition |
| --- | --- | --- |
| Manual capacity writer | `common/decisions/famine_migration_decisions.txt:2683-2687`, `:2732-2736`, `:2811-2816` calculate `num_of_civilian_factories * @FM_CAPACITY_PER_CIV + @FM_CAPACITY_BASE` and call the request helper. | Retire the three manual calculations. Decisions may change policy-owned adapter inputs and then mark capacity dirty, but they must not submit an absolute capacity. |
| Request helper | `common/scripted_effects/chaosx_famine_migration_effects.txt:2014-2028` accepts a positive request, stores it, registers the country, and clears the request. `common/scripted_effects/chaosx_famine_migration_effects.txt:4471` exposes the compatibility adapter `famine_migration_request_reception_capacity`. | Replace the implementation with a compatibility shim that ignores untrusted absolute requests and invokes the centralized recalculation, or remove the adapter after all callers are migrated. The public helper name may remain for save/script compatibility, but no caller may supply the old factory formula. |
| Country registration | `famine_migration_register_active_displacement_country` at approximately `:967-976` initializes missing displacement and reception loads. | Extend registration only with capacity dirty/schema fields and candidate registry activation. Do not change the exact load ownership. |
| Country unregister | `:981-994` clears capacity, country load, and several country ledgers. `:1039-1042` has additional invalid-country cleanup. | Add candidate-state unregister and capacity-field cleanup, but preserve any canonical load reconciliation policy. Do not silently discard a non-zero exact load merely because capacity evidence is missing. |
| State reception context | `:1885-1932` reads state load and owner country load/capacity to set overcrowding and observation flags. | Keep this as a context observer. It should mark the owner capacity dirty after a load change and use the latest capacity revision; it should not calculate capacity. |
| State/country load mutator | `:1943-1970` is the sole shared reception delta seam. It credits or debits the same exact amount in state and owner ledgers, registers active state/country, refreshes context and decision phase, and clears request inputs. Call sites include decisions at `:1835`, `:2023`, `:2222`, `:2845`, `:2855`, `:3012`, `:3022`, `:3171`, `:3295`, `:3422`, `:3436`, `:3477`, `:3618`, and `:3806`, plus spontaneous, forced, and corridor movement effects. | Preserve exact paired accounting. Add one owner-dirty invalidation after a successful credit or debit; do not add a second load writer or infer a load from candidate-state scans. |
| CXT fixture | `common/scripted_effects/famine_migration_cxt_test_effects.txt:25-26` sets a category threshold as a capacity request. | Change the fixture in the implementation tranche to seed an explicit candidate-state shelter/medical adapter and test the recalculation. Until then, the fixture must be treated as exercising the legacy path only. |
| Runtime processor | `common/scripted_effects/chaosx_famine_migration_effects.txt:4314-4340` processes only registered food states, displacement states, displacement countries, historical candidates/anchors, and relief donors. `common/on_actions/chaosx_on_actions_chaos_meter.txt:14-35` calls this from the existing single-host daily coordinator. | Add reception candidate states and reception countries to the same sparse registry processor. The host pulse may iterate only registered candidate states and active reception countries; it must not add an `every_country`, `every_owned_state`, or unbounded recurring scan. |

### 3.2 Country capacity consumers

The country capacity variable is consumed by `common/decisions/famine_migration_decisions.txt` at `:358-360` for the reception mission/availability check, `:807` for the close-border AI modifier, `:2644-2653` for open-reception visibility and overload, `:2803-2806` for distribute-arrivals AI, `:3219-3223` for local integration, `:3331-3368` for third-country resettlement and overload, and `:3501-3506` for voluntary return. The same file also uses country load without capacity at several zero/non-zero gates, including `:752-753`, `:1651-1652`, `:1866-1867`, `:2057-2058`, `:2525-2526`, `:2700`, `:2756-2767`, `:2923-2924`, `:3064-3065`, and `:3687-3688`.

`common/scripted_triggers/famine_migration_destination_selection_triggers.txt:16-34` requires a destination owner capacity variable and compares load against capacity. `common/scripted_effects/famine_migration_destination_selection_effects.txt:101-104` computes country headroom as capacity minus owner load and `:116-118` applies state-load penalty. These must consume effective, valid, current capacity and retain their central headroom step/max constants.

`common/scripted_effects/chaosx_famine_migration_effects.txt:1897-1927` and `:1050-1065` use capacity/load to set overcrowding and decision phase. The category and compact scripted-GUI header read the three public values through `localisation/english/famine_migration_l_english.yml:3`; the header must continue to show one reception-capacity value only.

The close-border AI path still references `famine_migration_reception_capacity_exhausted` at `common/decisions/famine_migration_decisions.txt:807`, but the current source census found no producer for that flag. The centralized recalculation must either set and clear it from the effective load/capacity relation or replace the modifier with a documented dynamic pressure trigger. Leaving a dead flag is not truthful AI input.

### 3.3 State load consumers and map/report surfaces

State load is read by `common/decisions/famine_migration_decisions.txt:3225-3245`, `common/scripted_effects/famine_migration_destination_selection_effects.txt:116-118`, `common/scripted_effects/famine_migration_decision_phase_effects.txt:141`, `common/scripted_triggers/chaosx_famine_migration_triggers.txt:137-138`, and the centralized reception context at `chaosx_famine_migration_effects.txt:1890-1932`. It is written only through initialization/cleanup and `famine_migration_apply_reception_delta`; this conservation boundary must remain.

`common/map_modes/chaosx_state_map_modes.txt:487-550` supplies role colours for reception, overcrowding, displacement, return, and resettlement and currently declares `update_daily = yes`. It does not calculate capacity. `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt:748-758` and `localisation/english/chaosx_map_modes_l_english.yml:148-151` expose the authorised owner capacity, owner load, state load, and border policy. The existing owner/controller gate is the correct privacy boundary. The map tooltip must interpret capacity as the effective value and may expose validity/revision status only within the authorised owner/controller detail if a separate status line is needed.

The ordinary decision category uses `common/decisions/categories/famine_migration_categories.txt` and the shared compact report header rather than a full new GUI. No GUI rewrite is proposed. Existing reports and event scenes are flag/summary based; capacity should flow through the existing bounded country callbacks and must not create a new report event carrier or a hidden world summary.

## 4. Authoritative engine data versus unavailable inputs

| Required term | Authoritative available evidence | Boundary or adapter requirement |
| --- | --- | --- |
| Food | `famine_migration_food_security_score`, food stage, component values, and persistent reserve ledger are already composed on registered famine states. The score is a pressure score, so availability is its bounded inverse. | A state with an uninitialised food projection is not a proven safe candidate. Do not substitute country food or a fabricated stable score. |
| Shelter | No migration shelter-capacity field exists in the current famine/migration source. Fallout `air_winter_shelter_capacity` and CBRN shelter disruption are different systems. | Add an explicit migration shelter adapter with state scope, people units, validity marker, and a policy/building writer. Until it is populated, capacity validity must fail closed. Reusing Fallout shelter or factories is forbidden. |
| Infrastructure | Vanilla `infrastructure_level`/`building_level@infrastructure` is available in state scope and is already used by the persistent food-reserve formula. | Normalize with a central full-score level constant. Do not claim this alone measures shelter or transport throughput. |
| Transport | `famine_migration_component_transport` is an existing normalized pressure component, and infrastructure, railway, and supply-node building predicates are engine-supported. | There is no direct numeric route-throughput or convoy-capacity field exposed to this system. Treat the inverted transport component as the current bounded proxy and keep any future rail/supply throughput adapter explicitly marked unproven until it has a writer. |
| Medical capacity | Country `cbrn_medical_capacity` is an existing bounded medical-response meter used by CBRN effects, with central minimum/maximum constants. | Consume the live unreserved meter only through a documented adapter. Do not count field hospitals, equipment stock, or CBRN shelter modifiers as medical reception capacity without an adapter. A missing/uninitialised meter makes the capacity result invalid. |
| Administration | State `famine_migration_component_governance` is an existing normalized pressure component, and vanilla `num_of_civilian_factories` is an authoritative country dynamic value. | Use governance availability plus civilian factories as a named bounded economic/administrative proxy. Factories are not administration headcount and must not be presented as such. Add a central full-score factory threshold and an explicit proxy comment. |
| Safe-state count | The candidate registry can count state-local safe predicates without a world scan. `state_population_k` is available for population weighting. | Register all candidate states for an active receiving country once, then keep the registry current on control/annexation and state-local invalidations. Safe states are a derived subset, not a second unmaintained world census. |
| Current load | Country `famine_migration_reception_load` and state `famine_migration_state_reception_load` are exact ledgers maintained by `famine_migration_apply_reception_delta`. | Use country load only as a pressure factor and preserve the paired ledger contract. Never calculate country load by scanning state loads. |
| War | Vanilla `has_war = yes` is an authoritative country trigger. Existing war/peace callbacks already mark country reassessment. | Mark active reception countries dirty on `on_war_relation_added`, `on_peace`, and peace-conference completion. Use one central wartime factor. |
| Outbreak | `black_plague_state_is_infected_or_worse` is an available state trigger and is already used by famine decisions. | Current source proves a binary outbreak signal, not a universal severity meter. Use registered candidate states only; add a severity adapter later if a graded penalty is required. |
| Contamination | State `cbrn_chemical_contamination` is an existing bounded meter with central thresholds and triggers such as `cbrn_state_has_chemical_contamination`. | Use the state meter or class for candidate-state pressure. `global.air_contamination_bp` may inform a documented country context but cannot prove every state's contamination and must not replace the state signal. |

The authoritative engine values above are enough to define the contract, but the shelter adapter and exact transport throughput source are current implementation blockers. The formula deliberately contains both terms and publishes invalid/zero until their evidence is present; this is preferable to an untruthful factory fallback.

## 5. Proposed data model and helper map

The following names are a proposed implementation map, not current source identifiers. The parent should keep names stable if equivalent names are chosen and document every helper in `common/scripted_effects/chaosx_dynamic_effects.md` or the subsystem-specific helper documentation.

| Helper | Scope and inputs | Outputs and side effects | Call sites and lifecycle |
| --- | --- | --- | --- |
| `famine_migration_register_reception_candidate_state` | State scope; valid owned/controlled receiver, state population, food projection, shelter adapter proof, route status, and owner country. | Adds the state to an aligned sparse global candidate-state registry, stores owner identity, sets a state candidate flag, and marks the owner dirty. | One-time seed when reception activates or an old save migrates; selected destination and control-change callbacks may add it idempotently. |
| `famine_migration_unregister_reception_candidate_state` | State scope and old owner identity. | Removes the aligned state/owner entries, clears state candidate fields, subtracts candidate population/count from the old owner, and marks old/new owners dirty. | `on_state_control_changed`, `on_annex`, state cleanup, and invalid-state paths. |
| `famine_migration_mark_reception_capacity_dirty` | Country scope only. | Sets `famine_migration_reception_capacity_dirty`, increments or records a revision request, and registers the country in a sparse reception-country array. | Exact load delta, policy/adaptor writes, food/outbreak/contamination changes, war/peace, control changes, and the active daily pulse. |
| `famine_migration_refresh_reception_candidate_state` | State scope; current state engine values plus explicit shelter/route/medical adapter proof. | Recomputes bounded component scores, safe predicate, outbreak/contamination pressure, and state input revision; marks the current owner dirty. It does not mutate either reception-load ledger. | Registered state processor and immediate state-local invalidation callbacks. |
| `famine_migration_recalculate_reception_capacity` | Country scope; only aligned registered candidate states belonging to this country and exact current country load. | Computes candidate/safe counts and populations, gross capacity, quality, load pressure, war/outbreak/contamination factors, effective capacity, validity, last refresh day, and revision. Sets/clears the capacity-exhausted flag from the effective relation. | One central consumer of all capacity writes. Called after dirty input changes and from the host-only sparse daily pulse. |
| `famine_migration_reception_capacity_is_valid` | Country trigger. | True only when schema, candidate registry, required adapters, safe population, and current revision are proven. | Every decision/destination trigger that currently tests only `has_variable = famine_migration_reception_capacity`. |
| `famine_migration_reconcile_reception_capacity_legacy_save` | Country scope; old variables and bounded owned/controlled state seed. | Clears untrusted factory capacity, initializes schema/internal fields, preserves exact load ledgers, seeds candidates once, recalculates, and records any bounded reconciliation uncertainty. | First active-country processor after load or first reception activation on a pre-schema save. |
| `famine_migration_request_reception_capacity` | Country compatibility adapter. | Ignores arbitrary absolute requests and calls the central recalculator, or returns invalid until all callers are migrated. | Temporary bridge for existing calls and CXT fixture; no gameplay caller may continue computing a factory value. |

Recommended country variables are `famine_migration_reception_capacity_gross`, `famine_migration_reception_capacity_quality`, `famine_migration_reception_capacity_revision`, `famine_migration_reception_capacity_last_refresh_day`, `famine_migration_reception_capacity_dirty`, `famine_migration_reception_capacity_valid`, `famine_migration_reception_capacity_candidate_count`, `famine_migration_reception_capacity_safe_state_count`, `famine_migration_reception_capacity_candidate_population_k`, `famine_migration_reception_capacity_safe_population_k`, and `famine_migration_reception_load_pressure`. Component/reason variables may be retained for authorised diagnostics, but they are not category values.

Recommended aligned global arrays are `global.famine_migration_reception_candidate_states`, `global.famine_migration_reception_candidate_owner_ids`, and `global.famine_migration_reception_active_countries`. A state flag or aligned state revision prevents duplicate registration. The registry contains candidate states, not only currently safe states, so food recovery, decontamination, outbreak resolution, and transport repair can make a state safe again without a world census.

The formula does not require a persistent event target. A synchronous state-to-owner operation may use a regular `save_event_target_as`, as the existing context helper does, but must never create a global event target for every candidate state. All candidate arrays, state flags, and country variables must be cleared on unregister and invalid-country cleanup.

## 6. Source-exact formula and normalized units

All population outputs and reception loads are people. `state_population_k`, candidate population, and safe population are thousands of people and use the existing `famine_migration_population.people_per_k` conversion. All component scores and pressure factors are fixed-point values in the existing normalized score range. Booleans such as war and outbreak are represented by flags or explicit runtime proof, not numeric pseudo-flags.

Let `C` be the sparse set of registered candidate states owned and controlled by the receiving country at recalculation time. Let `p_s` be `state_population_k` for state `s`, `P_C` be the sum of `p_s`, `P_safe` be the sum of `p_s` for safe states, and `N_safe` be the count of safe states. All sums are performed over the registered candidate-state array only.

### 6.1 State component normalization

For each candidate state, calculate the following scores in the central reception score range.

`food_s = clamp((food_score_max - famine_migration_food_security_score_s) * reception_score_max / food_score_max, reception_score_min, reception_score_max)`.

The existing famine food score is a pressure score, so the inverse is availability. A missing or uninitialised food projection produces invalid state evidence rather than an assumed stable value.

`shelter_s = clamp(shelter_capacity_people_s * reception_score_max / (state_population_k_s * people_per_k * shelter_full_population_ratio), reception_score_min, reception_score_max)`.

The shelter input must come from an explicit migration shelter adapter. The adapter must carry people units and a validity marker. If the denominator is zero or the adapter is absent, the state cannot be safe and the country result is invalid.

`infrastructure_s = clamp(infrastructure_level_s * reception_score_max / infrastructure_full_score_level, reception_score_min, reception_score_max)`.

`transport_s = clamp(transport_pressure_max - famine_migration_component_transport_s, reception_score_min, reception_score_max)`.

The transport component is already a normalized pressure input used by the famine/reserve system. It is the current source-exact bounded proxy for transport availability. A future route-throughput adapter may replace or refine it only when a writer and evidence contract exist.

`medical_s = clamp(cbrn_medical_capacity_country * reception_score_max / medical_capacity_max, reception_score_min, reception_score_max)`.

The medical meter is country-level, so the same proven country medical score is applied to each candidate state for the weighted sum. The adapter must exclude any already committed capacity according to the CBRN owner contract. An absent or uninitialised meter invalidates the result; it does not become full medical capacity.

`governance_availability_s = clamp(governance_pressure_max - famine_migration_component_governance_s, reception_score_min, reception_score_max)`.

`administrative_throughput = clamp(num_of_civilian_factories * reception_score_max / administration_full_score_civilian_factories, reception_score_min, reception_score_max)`.

`administration_s = clamp((governance_availability_s * administration_governance_weight + administrative_throughput * administration_throughput_weight) / administration_weight_sum, reception_score_min, reception_score_max)`.

The civilian-factory term is explicitly a bounded administrative/economic throughput proxy. It is not a replacement for shelter, food, transport, or medical evidence and must not be presented to the player as “factories equal people.”

Define `safe_s` as the bounded state predicate that all of the following are proven: the state is owned and controlled by the receiver; the food score/stage is below the configured unsafe threshold; the shelter adapter is valid; no route-unsafe flag blocks reception; `black_plague_state_is_infected_or_worse` is false; and state contamination is absent or below the configured reception contamination threshold. Severe contamination or outbreak makes `safe_s` false even if other component scores are high.

For an unsafe state, retain its candidate registration and set its safety multiplier to zero. This lets recovery re-enter the safe population on the next invalidation or sparse pulse.

### 6.2 Quality and network terms

Let `W` be the named sum of reception weights for food, shelter, infrastructure, transport, medical, and administration. Calculate population-weighted service quality across all candidate states, with unsafe states contributing zero service quality.

`quality = clamp(sum over C of (p_s * safe_s * (food_weight * food_s + shelter_weight * shelter_s + infrastructure_weight * infrastructure_s + transport_weight * transport_s + medical_weight * medical_s + administration_weight * administration_s)) / (P_C * W), reception_score_min, reception_score_max)`.

The safe-population fraction is `safe_population_fraction = clamp(P_safe / P_C, reception_score_min, reception_score_max)` when `P_C` is positive, otherwise the country is invalid. The safe-state network factor is `safe_state_factor = clamp(N_safe / target_safe_state_count, reception_score_min, reception_score_max)`. Both terms are required: a country with many unsafe states must not receive the same capacity as a compact clean network, and a single isolated safe pocket must not silently count as a complete reception network.

Gross capacity before current load and country/state hazard penalties is:

```text
gross_capacity_people = clamp(
    round(P_C * people_per_k * capacity_population_share * quality * safe_population_fraction / reception_score_max),
    capacity_people_zero,
    round(P_C * people_per_k * capacity_population_share_max / reception_score_max)
)
```

The capacity share and cap are named tuning values in the new reception-capacity constants file. They are the explicit design envelope that prevents the formula from turning total state population into automatic reception capacity.

### 6.3 Current load, war, outbreak, and contamination

Current load is the exact country ledger, not a state sum. Let `L` be `famine_migration_reception_load` and `G` be gross capacity. When the result is otherwise valid, calculate `load_pressure = clamp(L / max(G, minimum_load_denominator_people), reception_score_min, reception_score_max)` and `load_factor = clamp(reception_score_max - load_pressure * load_penalty, minimum_load_factor, reception_score_max)`. If `L` meets or exceeds `G`, the country can still expose the effective value for overload diagnostics, but the overload flag and decision triggers must close reception according to the existing policy contract.

The war factor is `war_factor = wartime_factor` when `has_war = yes`, otherwise `reception_score_max`. No other war relationship is inferred from a world scan.

The candidate-weighted outbreak pressure is `outbreak_pressure = clamp(sum over C of (p_s * outbreak_s) / P_C, reception_score_min, reception_score_max)`, where `outbreak_s` is a binary normalized signal from `black_plague_state_is_infected_or_worse` or a future explicit severity adapter. The factor is `outbreak_factor = clamp(reception_score_max - outbreak_pressure * outbreak_penalty, minimum_hazard_factor, reception_score_max)`.

The candidate-weighted contamination pressure is `contamination_pressure = clamp(sum over C of (p_s * contamination_s) / P_C, reception_score_min, reception_score_max)`, where `contamination_s` is `cbrn_chemical_contamination` normalized by the existing CBRN meter maximum and threshold policy. The factor is `contamination_factor = clamp(reception_score_max - contamination_pressure * contamination_penalty, minimum_hazard_factor, reception_score_max)`.

`global.air_contamination_bp` may be retained as a separate country context for reports or a future global modifier, but it must not be used as proof that every candidate state is contaminated. State CBRN evidence controls the state safety predicate and weighted contamination term.

### 6.4 Published effective capacity

The single published value is:

```text
effective_capacity_people = clamp(
    round(gross_capacity_people * safe_state_factor * load_factor * war_factor * outbreak_factor * contamination_factor),
    capacity_people_zero,
    round(P_C * people_per_k * capacity_population_share_max / reception_score_max)
)
```

Here `capacity_people_zero` is the shared population zero constant, not the existing positive destination-selection threshold. Publish this as `famine_migration_reception_capacity` only when the schema, candidate registry, required shelter and medical adapters, positive candidate population, and at least one safe state are proven for the current revision. Otherwise set the published capacity to the centralized zero value and set `famine_migration_reception_capacity_valid` false. The effective value is the only value used by decisions, destination selection, map authorised detail, and category localisation.

The formula intentionally keeps gross quality and effective hazard/load factors separate so a report or authorised debug view can explain whether capacity fell because states lost service quality, became unsafe, entered war, experienced an outbreak, became contaminated, or filled with current load. These internals must not leak into the three-value category header.

## 7. Central constants and adapter plan

Create one shared `common/script_constants/famine_migration_reception_capacity_constants.txt` category rather than file-local `@` constants. Reuse existing global constants where their units and ranges match, especially `famine_migration_population.people_per_k`, the existing food component/score ranges, CBRN meter bounds, and the existing destination-selection minimum/headroom constants.

The new category should name the following tuning groups: reception score minimum/maximum; food-score conversion range; each of the six component weights; weight sums; shelter full-population ratio and adapter validity policy; infrastructure full-score level; transport pressure conversion; medical meter conversion; administration governance/throughput weights and full-score factory threshold; safe-state target; population capacity share and maximum share; minimum load denominator; load penalty and minimum load factor; wartime factor; outbreak and contamination penalties; minimum hazard factor; contamination safe threshold; sparse refresh day/revision guard; schema version; and diagnostic validity result tokens.

No gameplay file may retain `@FM_CAPACITY_PER_CIV` or `@FM_CAPACITY_BASE` after migration. If the names remain temporarily to avoid parser or save breakage, they must no longer be read by any capacity calculation and must be documented as retired compatibility names.

The shelter adapter should be state-scoped and expose `famine_migration_reception_shelter_capacity_people`, `famine_migration_reception_shelter_input_valid`, and an owner/policy writer. The transport adapter may initially expose only the existing `famine_migration_component_transport` pressure proof and `famine_migration_reception_transport_input_valid`; an exact rail/supply throughput adapter should be a separate follow-up, not an invented number. The medical adapter should expose the live CBRN meter and reservation validity without duplicating CBRN deductions. The administration adapter should expose the named governance/industry proxy semantics.

## 8. Sparse refresh contract and invalidation hooks

The existing host-only daily coordinator in `common/on_actions/chaosx_on_actions_chaos_meter.txt` already invokes `famine_migration_process_registered_runtime` once through the global-host country. The reception implementation should extend this existing registry processor rather than add another `on_daily` world pass.

The sparse pulse should perform the following bounded work: iterate `global.famine_migration_reception_candidate_states` once, refresh only registered candidate states, accumulate or store changed state inputs, then iterate `global.famine_migration_active_countries` and recalculate only dirty countries or countries whose last refresh day/revision is stale. It must not call `every_country`, `every_owned_state`, or `every_controlled_state` from a recurring hook. A bounded `every_owned_state`/`every_controlled_state` seed is allowed only inside the current country when reception is first activated or a legacy save is migrated.

Immediate invalidations are:

- A successful `famine_migration_apply_reception_delta` credit or debit marks the destination owner dirty after the exact paired ledger update.
- Reception policy, controlled medical reception, distribution, integration, resettlement, and voluntary/forced return mark the owning country dirty after their adapter or load mutation.
- Food-score, food-stage, reserve, transport, or relief evaluation on a registered candidate state marks its owner dirty.
- CBRN contamination changes, contamination start/end, and Black Plague infection start/end mark the owner of the affected registered state dirty.
- `on_state_control_changed` unregisters the old candidate owner, registers the new owner when valid, and marks both owners dirty. The existing callback exposes `FROM.FROM` as the state, `ROOT` as the new controller, and `FROM` as the old controller; preserve that scope contract.
- `on_annex` removes candidate states from the former owner's bounded owned-state set and marks the former and receiving owners dirty.
- `on_war_relation_added`, `on_peace`, and `on_peaceconference_ended` mark the exact callback countries dirty. Existing `famine_migration_mark_country_war_reassessment` and `famine_migration_mark_country_peace_reassessment` are appropriate seams to extend.
- `on_nuke_drop` marks the owner/controller of the exact affected state dirty after the existing state callback, and marks the active reception owner when the destination relationship is exact and available.
- Construction, infrastructure, factory, railway, and supply-node changes have no generic exact callback in the current source census. The registered candidate-state daily pulse is therefore required for truthful refresh of these engine fields. The pulse is sparse because it touches only registered reception candidates, not every map state.

When a state change marks a country dirty, a subsequent decision or map read may use the previous published value until the bounded processor runs; the implementation should call the recalculator immediately when the same effect already has a country scope, and the daily pulse is the recovery path for engine-owned changes without callbacks. Store `famine_migration_reception_capacity_last_refresh_day` and a monotonic input/revision token so repeated same-day work is idempotent.

After a country recalculates, refresh only affected state context flags through the registered active displacement-state array or state revision checks. Do not scan all world states to find overcrowding consumers. `famine_migration_refresh_reception_context` remains the state-local observer and should compare its seen revision before updating flags.

## 9. Old-save initialization and cleanup

Add a centralized schema variable such as `famine_migration_reception_capacity_schema_version` and a schema constant in the reception-capacity constants file. On the first active-country processor after load, perform the following bounded migration:

1. Detect an absent or older schema and clear the old factory-derived capacity as untrusted rather than preserving a false number.
2. Initialize new internal capacity fields, dirty/valid flags, revision/day guards, and candidate counts to central zero/invalid values.
3. Preserve the existing country `famine_migration_reception_load` and every state `famine_migration_state_reception_load` under the established exact-ledger contract. Do not reconstruct country load by scanning states.
4. Seed candidate states with a bounded `every_owned_state` or `every_controlled_state` in the current country and register only valid candidate states. This is a one-time country-local migration, not a recurring world scan.
5. Recalculate through the central helper. If shelter or medical adapter evidence is absent, publish zero/invalid and record `famine_migration_reception_capacity_load_reconciliation_unproven` or an equivalent diagnostic rather than falling back to factories.
6. Set the schema version and clear the migration request after successful bounded initialization.

If a bounded state/country load comparison is later needed, record any mismatch and preserve the canonical existing load owner; do not silently add or subtract population merely to make the two ledgers agree. Existing unregister cleanup at `chaosx_famine_migration_effects.txt:981-994` must be reviewed carefully because clearing capacity and clearing exact load are not interchangeable operations.

The CXT test content must be updated in the implementation tranche to seed an explicit shelter input, a valid medical adapter, and at least one owned/controlled candidate state before calling the central helper. It should have separate cases for a valid computed capacity and an invalid/zero result when the shelter adapter is absent. A test request of the category reception-load threshold is no longer meaningful evidence of dynamic capacity.

## 10. Decision, AI, mapmode, report, and localisation consumers

All capacity/load comparisons in `famine_migration_decisions.txt` and the destination-selection trigger must add the validity contract where capacity is required. The current `has_variable = famine_migration_reception_capacity` checks are insufficient because a zero/invalid result can still have a variable. The destination trigger should require `famine_migration_reception_capacity_is_valid = yes`, then compare current load against effective capacity and preserve the existing headroom step/max constants.

`fm_open_reception`, `fm_controlled_medical_reception`, and `fm_distribute_arrivals` should no longer write a capacity request. Their effects may write the relevant border policy, shelter investment, distribution, or medical-policy adapter, then call `famine_migration_mark_reception_capacity_dirty` and the central recalculation at the owner scope. If a decision only changes policy and does not change a measured component, it must still mark dirty so the policy factor and revision are truthful.

`fm_mission_prevent_reception_collapse`, local integration, third-country resettlement, voluntary return, distribute-arrivals, and all open/medical reception availability paths consume effective capacity. The dead `famine_migration_reception_capacity_exhausted` flag must be produced centrally from the effective relation or replaced by a dynamic `load_pressure` trigger, with the same named AI scenarios audited before and after any balance change.

The compact category header at `localisation/english/famine_migration_l_english.yml:3` should retain the existing three-value structure. It may add a concise dynamic “capacity unavailable” response only when `famine_migration_reception_capacity_valid` is false, but it must not expose gross capacity, component weights, or implementation history. Existing decision descriptions that promise food, shelter, medical, transport, or administration should be checked after adapter implementation so the prose describes the real policy effect.

The migration map mode can retain role colours and `update_daily = yes` because colour flags are already projected by bounded state processors. The authorised tooltip may continue to show state load, owner load, effective owner capacity, and border policy. If a validity/revision status is added, gate it by the existing owner/controller authorised localisation route and keep public observer text qualitative. No new icon or map asset is needed for this architecture.

Reports and event details should consume the same country effective capacity variable through existing bounded summary/callback paths. Do not add a recurring report event or a whole-world report carrier merely to refresh a number. The existing state-owner/controller privacy boundary remains mandatory.

## 11. Focused probability scenarios and MCP evidence

The existing scenario matrix in `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_probability_scenarios.csv` includes `prob_capacity_exhausted_border`, `prob_outbreak_reception`, `prob_destination_selection_internal`, `prob_destination_selection_persecution`, `prob_corridor_acceptance`, `prob_forced_return`, `prob_integration`, and related famine/relief scenarios. The parent should extend the named audit set with these focused capacity scenarios:

| Scenario | State inputs | Expected directional evidence |
| --- | --- | --- |
| `prob_reception_capacity_safe_network` | Peace, clean food-safe candidate states, valid shelter and medical adapter, strong infrastructure/transport/administration, low load. | Capacity is valid and high relative to the same country's hazard cases; open or controlled reception is preferred over close-border output. |
| `prob_reception_capacity_wartime_transport` | Same candidate states with `has_war = yes`, transport pressure and infrastructure deficit. | Effective capacity falls through the wartime and transport terms; a raw factory count cannot restore the old value. Distribution/repair responses gain relative weight where their existing AI factors allow it. |
| `prob_reception_capacity_outbreak_medical` | Candidate outbreak exposure with one high and one low `cbrn_medical_capacity` case. | The high-medical case retains more controlled-reception viability; the low-medical case closes or diverts according to existing policy. No outbreak penalty is applied to an unexposed candidate. |
| `prob_reception_capacity_contaminated_states` | Identical candidates with zero versus serious/severe state CBRN contamination. | Contaminated candidates leave the safe population and reduce effective capacity; clean candidates remain unchanged. Global air contamination alone must not create state contamination. |
| `prob_reception_capacity_load_pressure` | Same gross candidate capacity with current load below, near, and above gross capacity. | Published capacity and overload flag respond monotonically to exact load; no stale factory writer or circular load derivation remains. |
| `prob_reception_capacity_shelter_admin_recovery` | Same country before/after an explicit shelter adapter write and governance/administrative recovery. | Capacity rises only after the proven adapter/input changes; missing shelter cannot silently become factory capacity. |
| `prob_reception_capacity_registry_control` | Candidate state changes from old owner to new controller, then recovers food/contamination status. | Old and new candidate populations/counts update once, old owner loses the state, new owner can regain it, and no world scan is needed. |

Per the weighted-logic requirements, every scenario must begin with `hoi4.probability_inspect` and be evaluated by `chaosx_ai_probability_auditor` using the same named cases before/after implementation. The fresh probability route was attempted with the current workspace and the source path for `common/decisions/famine_migration_decisions.txt`. The accepted call shape was `source = { path = common/decisions/famine_migration_decisions.txt }` with the decision AI adapter, but the MCP call timed out after 180 seconds. Earlier source forms were rejected with exact schema errors: `Unrecognized key: relativePath at source`, then `Invalid input: expected object, received string at source`, and adapter-only discovery returned `An adapter requires a source; provide a source alone to discover compatible adapters`.

Therefore no fresh probability inspect/evaluate/compare artifact is claimed here. Existing `ai_probability_baseline.md`, `ai_probability_post.md`, and `ai_probability_final_audit.md` are historical/incomplete and do not satisfy a current before/after capacity audit. The parent must rerun the mandatory route when the MCP timeout is resolved; source-only reasoning in this handoff is not a substitute.

The bounded map route was available. `hoi4.map_inspect` over state IDs 1, 2, 3, and 4 in workspace `mod_chaos_redux_ea3b2d67c2c0` returned `MAP_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6180ca9133f337ab7460334f54fef7ee47720a23542298e7a192213ec4a82b10/3a846fe71fc9bbad08d27025c6c4fed704197920fa090aac5926b5640c0f34e3/map-inspect.cda612cbd4957210.json`. The selected state definitions, bitmap, state-region, adjacency, supply, and railway checks passed. The overall artifact reports unrelated existing `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics in `mod:map/buildings.txt` and omits additional diagnostics, so it is evidence for the bounded map substrate only, not a clean whole-map validation.

A read-only `hoi4.map_render` request for the state layer with supply-node, railway, and state-building overlays in the same workspace timed out after 180 seconds. No render artifact is claimed; the prior bounded map-inspect artifact is the available map evidence.

## 12. Migration order and validation evidence

The parent implementation should apply this architecture in the following order:

1. Add the shared reception-capacity constants and adapter field documentation with no consumer changes yet.
2. Add candidate-state registration/unregistration, country dirty/schema fields, validity trigger, and bounded sparse processors while preserving the existing exact load helper.
3. Implement the centralized state component and country formula, then replace the legacy request helper with the compatibility shim.
4. Wire state/control/annex/war/peace/outbreak/contamination and exact policy/load invalidation hooks, including the existing host-only daily coordinator.
5. Migrate the three manual decision writers and CXT fixture away from the factory formula.
6. Add validity checks and effective-capacity reads to destination selection and every listed decision/mission consumer; produce the capacity-exhausted flag or replace its AI trigger.
7. Update dynamic helper documentation, category/localisation wording, map authorised detail if required, and source-of-truth/resume documents.
8. Run source audits for duplicate capacity writers, exact paired load deltas, registry cleanup, no recurring world scans, and all consumers using validity/current revision.
9. Rerun the focused probability scenarios through the mandatory MCP/auditor route, plus bounded map inspect/render/compare for the existing state map surface. Keep the unrelated map diagnostics separate from the reception-capacity result.

Meaningful validation already completed for this handoff was the current-source census, the required offline wiki and vanilla-documentation review, the bounded map inspection artifact above, and the attempted probability route with exact timeout/schema blockers recorded. No gameplay run was performed, and no gameplay source was changed.

## 13. Simplifications, omissions, and blockers

- The requested formula is fully specified with food, shelter, infrastructure, transport, medical capacity, administration, safe-state count, current load, war, outbreak, and contamination terms, but shelter has no current authoritative migration adapter and exact transport throughput is unavailable. The implementation must not silently substitute Fallout shelter, factories, stockpiles, or a fabricated route capacity.
- Medical capacity is available as the existing CBRN meter, but its initialization and reservation semantics must be confirmed by the CBRN owner before it is treated as a valid reception input. Missing evidence must produce invalid/zero capacity.
- Outbreak evidence is currently binary through Black Plague state triggers. A graded outbreak penalty requires a new explicit state severity adapter and is not inferred from unrelated world fields.
- There is no generic construction/infrastructure/factory-change on-action in the current callback census. The sparse registered candidate-state daily pulse is required to keep engine-owned fields truthful; without it, a dirty-only event contract would be stale.
- The existing unregister helper clears country load alongside capacity. Parent implementation must review that cleanup before adding schema migration so old exact load is not lost as a side effect of invalid capacity.
- The mandatory fresh weighted probability MCP inspection timed out after accepting the source-object schema. No probability compare or `chaosx_ai_probability_auditor` evidence is claimed. This is an external tooling blocker, not permission to substitute source-only analysis.
- The bounded map inspect route succeeded for selected states, but the artifact contains unrelated pre-existing map building/port diagnostics. No map rewrite or GUI rewrite was attempted or needed.
- The supported map-render route was also attempted for the state layer and timed out after 180 seconds, so no render/compare evidence is claimed.
- No gameplay edits, localisation edits, constants, helper files, or commits were made in this subtask. The only deliverable is this architecture handoff.

The architecture is complete as a source-exact design handoff, but implementation and final probability validation remain parent-owned work blocked by the explicit adapter and MCP limitations above.
