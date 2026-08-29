# Famine and migration occupation-profile owner handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Status and scope

The current vanilla occupation-law census is closed in `famine_migration_resolve_occupation_profile`. The resolver now has one ordered exact `occupation_law` branch for every current vanilla top-level law and every current Chaos Redux law. `concentration` is explicitly fail-closed to `none` because it is a hidden, unavailable, empty compatibility token rather than a selectable law.

This handoff covers only the shared occupation-profile resolver, its owning dynamic-effect documentation, and this handoff. No occupation-law definition, decision, localisation, event, mapmode, GUI, on-action, constant, or unrelated gameplay file was changed. No commit was created.

## Changed files and helper contract

- `common/scripted_effects/chaosx_famine_migration_effects.txt:2534` — expanded `famine_migration_resolve_occupation_profile` with the complete ordered branch census and reset of `famine_migration_occupation_context_proven`.
- `common/scripted_effects/chaosx_dynamic_effects.md:822` — documented the state-scope contract, complete material-law table, pressure injection rules, and explicit hidden-token disposition.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/occupation_profile_owner.md` — this implementation and evidence handoff.

The helper map is:

| Helper | Scope | Inputs | Outputs | Side effects | Existing call sites |
| --- | --- | --- | --- | --- | --- |
| `famine_migration_resolve_occupation_profile` | State | Current engine `occupation_law` only. | Temporary `famine_migration_occupation_profile`, `famine_migration_occupation_extra_extraction`, `famine_migration_occupation_extra_vulnerability`, `famine_migration_occupation_extra_governance`, and `famine_migration_occupation_context_proven`. | None beyond temporary values; no law change, death, movement, event, scan, random selection, or event target. | `famine_migration_select_historical_profile_id`, `famine_migration_collect_surface_context`, and `famine_migration_resolve_historical_profile_context`. |

All outputs reset to the centralized zero values before branch evaluation. A selectable mapped law proves context with `famine_migration_runtime.one`; the compatibility token leaves profile, deltas, and proof at zero. `famine_migration_collect_surface_context` adds the existing occupied-state baseline transport, governance, and vulnerability pressure only when the proven law is not owned and controlled by the owner, then clamps all components to their existing range.

## Pressure and constant plan

No constants were added or changed. The resolver reuses `famine_migration_surface_context` values from `common/script_constants/famine_migration_constants.txt`:

| Pressure token | Centralized value | Use |
| --- | ---: | --- |
| `occupation_transport_pressure` | 10 | Existing baseline occupied-state transport pressure in the collector. |
| `occupation_governance_pressure` | 15 | Baseline occupation governance and `standard` governance delta. |
| `occupation_vulnerability_pressure` | 10 | Existing baseline occupation vulnerability and ordinary extraction delta. |
| `occupation_extraction_pressure` | 20 | Ordinary extraction delta. |
| `occupation_forced_extraction_pressure` | 35 | Forced-labor and exterminatory extraction delta. |
| `occupation_forced_governance_pressure` | 25 | Forced-labor and exterminatory governance delta. |
| `occupation_collective_punishment_pressure` | 30 | Collective-punishment extraction delta. |
| `occupation_transfer_vulnerability_pressure` | 35 | Brutal/coercive transfer-vulnerability delta. |

The bounded profile enum remains the existing seven-value contract: `none`, `protective`, `standard`, `extraction`, `forced_labor`, `collective_punishment`, `population_transfer`, and `exterminatory`. No current selectable law has material evidence for `population_transfer`; the hidden `concentration` compatibility token therefore does not activate that profile.

## Complete current-law census

The source evidence is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\occupation_laws\occupation_laws.txt` lines 63-1113 and `common\occupation_laws\chaosx_occupation_laws.txt` lines 1-170. Each row below names the actual modifier/mechanics evidence used for the mapping; ideology and flavor labels were not used as standalone evidence.

| Law | Availability/mechanics and material modifiers | Mapped profile | Pressure effects |
| --- | --- | --- | --- |
| `missing_garrison_scaled_effect` | Hidden `visible = always no`, `missing_garrison_law = yes`; `resistance_target = 0.10`, `compliance_gain = -0.045`, and AI base zero. | `standard` | `occupation_governance_pressure` plus proven context, so missing-garrison governance failure is visible without direct deaths. |
| `no_garrison` | Bounded RAJ/DLC visibility path; `resistance_target = 0.40`, `no_compliance_gain = 1`, and `required_garrison_factor = -1`; suppressed form preserves the resistance/garrison failure. | `standard` | `occupation_governance_pressure` plus proven context. |
| `autonomous_occupation` | Democratic-only autonomy; `compliance_gain = 0.02`, `required_garrison_factor = -0.40`, and `resistance_damage_to_garrison = -0.25`. | `protective` | Baseline only. |
| `foreign_civilian_oversight` | `required_garrison_factor = -0.25`, `resistance_damage_to_garrison = -0.25`, and zero local factories/resources/compliance gain. | `protective` | Baseline only. |
| `local_police_force_garrison` | `resistance_target = -0.15`, `compliance_gain = -0.025`, `required_garrison_factor = -0.35`, `resistance_damage_to_garrison = -0.50`, and no local output modifier. | `protective` | Baseline only. |
| `secret_police_oversight` | `resistance_target = -0.30`, `compliance_gain = -0.04`, `required_garrison_factor = -0.15`, `resistance_damage_to_garrison = -0.15`, and `0.05` local factories/resources. | `standard` | `occupation_governance_pressure` plus proven context. |
| `liberate_workers_occupation` | Communist-available policy; `resistance_target = -0.15`, `compliance_gain = -0.025`, `resistance_damage_to_garrison = 0.25`, `0.20` local factories, and `0.30` local resources. | `extraction` | `occupation_extraction_pressure` and `occupation_vulnerability_pressure`. |
| `military_governor_occupation` | Default apparatus; `resistance_target = -0.35`, `compliance_gain = -0.045`, `0.10` local resources, and `0.08` local manpower. | `standard` | `occupation_governance_pressure` plus proven context. |
| `martial_law_occupation` | `resistance_target = -0.60`, `compliance_gain = -0.055`, and `0.10` local resources. | `extraction` | `occupation_extraction_pressure` and `occupation_vulnerability_pressure`. |
| `forced_labor_occupation` | `resistance_target = -0.40`, `compliance_gain = -0.08`, `required_garrison_factor = 0.15`, `resistance_damage_to_garrison = 0.30`, `0.40` local resources, and `0.05` local factories. | `forced_labor` | `occupation_forced_extraction_pressure`, `occupation_forced_vulnerability_pressure`, and `occupation_forced_governance_pressure`. |
| `harsh_quotas_occupation` | `resistance_target = -0.40`, `compliance_gain = -0.08`, `required_garrison_factor = 0.15`, `resistance_damage_to_garrison = 0.50`, `0.25` local factories, and `0.05` local resources. | `collective_punishment` | `occupation_collective_punishment_pressure` and `occupation_vulnerability_pressure`. |
| `brutally_oppressive_occupation` | Fascist-available policy; `resistance_target = -0.75`, `compliance_gain = -0.11`, `required_garrison_factor = 0.25`, `resistance_damage_to_garrison = 1.0`, `0.10` local resources, and `resistance_decay = 1.0`. | `exterminatory` | `occupation_forced_extraction_pressure`, `occupation_transfer_vulnerability_pressure`, and `occupation_forced_governance_pressure`. |
| `concentration` | Chaos Redux hidden compatibility token with empty state modifiers, `visible = always no`, `available = always no`, AI base zero, and `fallback_law = military_governor_occupation`. | `none` | No context or pressure; explicit fail-closed non-law disposition. |
| `reconciliation` | Turkey/Kurdish DLC/focus-gated policy; `compliance_gain = 0.03`, `required_garrison_factor = -0.50`, `resistance_damage_to_garrison = -0.30`, and `resistance_decay = 0.5`. | `protective` | Baseline only. |
| `colonial_police` | Italy/Belgium conditional policy; `resistance_target = -0.30`, `compliance_gain = -0.02`, `required_garrison_factor = -0.30`, `resistance_damage_to_garrison = -0.40`, and no local output modifier. | `protective` | Baseline only. |
| `colonial_police_improved` | Italy/Albania focus-gated policy; `resistance_target = -0.35`, `compliance_gain = -0.015`, `required_garrison_factor = -0.35`, `resistance_damage_to_garrison = -0.45`, and `0.25` local factories/resources. | `extraction` | `occupation_extraction_pressure` and `occupation_vulnerability_pressure`. |
| `colonial_police_final` | Italy/Albania focus-gated policy; `resistance_target = -0.45`, `compliance_gain = -0.01`, `required_garrison_factor = -0.40`, `resistance_damage_to_garrison = -0.55`, `0.25` local factories/resources, and `0.05` local manpower. | `extraction` | `occupation_extraction_pressure` and `occupation_vulnerability_pressure`. |
| `secretaries_general` | Belgium DLC/focus-gated policy; colonial-police material set with `resistance_target = -0.30`, `compliance_gain = -0.02`, `required_garrison_factor = -0.30`, and `resistance_damage_to_garrison = -0.40`, with no local output. | `protective` | Baseline only. |
| `independent_rule` | RAJ/princely focus-gated policy; `resistance_target = -0.10`, `compliance_gain = 0.03`, `required_garrison_factor = -0.50`, `resistance_damage_to_garrison = -0.50`, and `-0.35` local factories/resources. | `protective` | Baseline only. |
| `princely_subjugation` | RAJ/princely focus-gated policy; `resistance_target = 0.60`, `compliance_gain = -0.10`, `required_garrison_factor = 0.15`, `resistance_damage_to_garrison = -0.10`, and `0.60` local factories/resources. | `collective_punishment` | `occupation_collective_punishment_pressure` and `occupation_vulnerability_pressure`. |
| `senbu_occupation_law` | Japan/China route-gated policy; `resistance_target = -0.20`, `compliance_gain = 0.01`, `required_garrison_factor = 0.05`, `resistance_damage_to_garrison = -0.35`, and `-0.10` local factories/resources. | `protective` | Baseline only. |
| `GEACPS_exploitation_occupation_law` | Japan exploitation flag; `resistance_target = -0.40`, `compliance_gain = -0.08`, `required_garrison_factor = 0.30`, `resistance_damage_to_garrison = 0.60`, `0.20` local factories, and `0.60` local resources. | `collective_punishment` | `occupation_collective_punishment_pressure` and `occupation_vulnerability_pressure`. |
| `GEACPS_prosperity_occupation_law` | Japan prosperity flag; `resistance_target = -0.15`, zero compliance gain, `required_garrison_factor = 0.05`, `resistance_damage_to_garrison = -0.25`, `0.10` local factories, and `0.05` local resources. | `standard` | `occupation_governance_pressure` plus proven context. |
| `cbrn_coercive_security_occupation` | Chaos Redux CBRN authorization; `resistance_target = -0.50`, `compliance_gain = -0.065`, `required_garrison_factor = 0.20`, `resistance_damage_to_garrison = 0.10`, `-0.10` local factories, and `-0.05` local resources, with a less severe suppressed modifier. | `exterminatory` | `occupation_forced_extraction_pressure`, `occupation_transfer_vulnerability_pressure`, and `occupation_forced_governance_pressure`. |
| `cbrn_protected_occupation_administration` | Chaos Redux CBRN authorization; `resistance_target = -0.10`, `compliance_gain = 0.015`, `required_garrison_factor = 0.25`, `resistance_damage_to_garrison = -0.25`, `-0.05` local factories, and `-0.025` local resources. | `protective` | Baseline only. |

The table contains all 22 top-level laws in the current vanilla file and all 3 top-level laws in the current Chaos Redux file. The only non-law helper is the explicit `concentration` compatibility token; no selectable law was omitted.

## Event-target and cleanup plan

No event target was introduced, persisted, or cleared. The helper has no cross-event scope requirement and uses temporary output only. The new context-proof reset prevents a stale proof from leaking across resolver calls. Existing food-state cleanup and historical-profile cleanup remain the owners of their existing variables and flags; this patch adds no cleanup surface.

## Migration and call-site plan

The existing callers already invoke the resolver at their owner boundaries, so no call-site migration was required. `famine_migration_select_historical_profile_id` uses the bounded profile for policy-analogue eligibility, `famine_migration_collect_surface_context` consumes the three deltas and applies the occupied-state baseline, and `famine_migration_resolve_historical_profile_context` consumes the profile for historical-profile policy proof. The ordered branches replace the prior partial census without changing those APIs or the downstream mortality/migration ownership boundary.

## Validation and evidence

- Re-read the live vanilla file and counted 22 top-level laws at lines 63, 81, 142, 172, 195, 232, 249, 271, 321, 355, 442, 480, 518, 544, 607, 659, 711, 755, 849, 950, 1018, and 1068.
- Re-read `common/occupation_laws/chaosx_occupation_laws.txt` and counted `concentration`, `cbrn_coercive_security_occupation`, and `cbrn_protected_occupation_administration`.
- Re-read `common/script_constants/famine_migration_constants.txt`, `common/scripted_effects/chaosx_famine_migration_effects.txt`, and the owning dynamic-effect documentation before patching; all pressure and profile identifiers are existing contracts.
- Extracted the resolver's ordered branches and confirmed one exact branch for each of the 25 censused laws, with no additional law branch and an explicit `none` result for `concentration`.
- Checked the touched Clausewitz script block and whole source brace counts after the patch; the resolver closes at line 2695 and no brace imbalance was introduced.
- No weighted logic, event surface, GUI, focus, map, or probability-bearing helper was changed, so the probability auditor and event/MCP routes were not applicable. No MCP artifact exists for this source-only occupation-law contract.

## Unsupported analysis and residual blockers

The current source still has no authoritative occupation-law transition callback that supplies actor, state, and exact affected amount together. The existing blocker remains documented in `docs/plans/famine_and_migration_system_plans/subagent_handoffs/owner_callback_census.md` and `docs/systems/famine_and_migration_system.md`; this resolver intentionally remains read-only and does not infer a transition or attribute direct deaths. No other omissions or simplifications were made.
