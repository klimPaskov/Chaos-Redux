# Event 046 registry schema

This is the design contract for a shuffle family.

The implementation agent must map it to supported Clausewitz structures after reading the current documentation and repository patterns.

The field names below are conceptual identifiers, not pasteable script.

| Field | Required | Purpose | Failure rule |
| --- | --- | --- | --- |
| `family_id` | Yes | Stable Event 46 identity for one gameplay family | Duplicate or changed meaning rejects registration |
| `owner_id` | Yes | Names the core Event 46 owner or external mechanic owner | Missing owner rejects registration |
| `contract_version` | Yes | Keeps save interpretation stable and supports migration | Incompatible live version blocks the adapter |
| `minimum_capability` | Yes | Baseline or Evolution I through V | Invalid capability rejects registration |
| `scope_kind` | Yes | Country, state, unit, commander, production object, pair, or owner object | Unsupported scope blocks the family |
| `scope_source` | Yes | Bounded way to enumerate candidate instances | Unbounded or unstable source blocks the family |
| `validity_predicate` | Yes | Proves an instance can participate now | Missing or inconclusive proof excludes the instance |
| `exclusion_predicate` | Yes | Removes special, terminal, malformed, or protected instances | Missing required exclusion blocks the family |
| `selection_group` | Yes | Baseline, stores, state, politics, research, production, military, owner, or structural | Unknown group rejects registration |
| `base_selection_weight` | Yes | Relative chance inside the eligible pool | Missing weight prevents weighted selection |
| `identity_quota_role` | No | Marks a family that can satisfy capability quotas | Invalid quota role is ignored and audited |
| `mandatory_at_evolution_v` | Yes | States whether every valid non-conflicting instance enters maximum coverage | Mandatory family without proof blocks Evolution V completion |
| `result_type` | Yes | Percentage, bounded integer, absolute integer, normalized shares, categorical token, pair relation, or owner type | Unknown type rejects registration |
| `legal_floor_source` | Yes | Static legal floor or frozen dynamic floor | Missing floor blocks planning |
| `legal_ceiling_source` | Yes | Static legal cap, capacity, world anchor, or owner cap | Missing ceiling blocks planning |
| `world_anchor_source` | No | Frozen world fact used to scale absolute bands | Mutable or order-dependent anchor blocks planning |
| `distribution_profiles` | Yes | Approved profiles by capability | Missing active profile blocks the family |
| `compatibility_group` | No | Prevents mutually exclusive families or tokens | Unresolved conflict rejects the later family before commit |
| `dependency_bundle` | No | Plans related families together | Partial bundle cannot commit |
| `plan_method` | Yes | Produces all immutable results before application | Incomplete result set rejects the family |
| `validation_method` | Yes | Rechecks range, scope identity, dependency, and owner proof | Any failed result rejects the family before commit |
| `commit_method` | Yes | Applies the already planned result | Missing setter blocks registration |
| `commit_progress_proof` | Yes | Supports idempotent recovery after interruption | No recovery proof blocks broad or staged commit |
| `reconciliation_method` | Yes | Refreshes derived state and proves legality | Missing reconciliation blocks registration |
| `generic_source_policy` | Yes | Declares which generic Chaos, Deaths, or owner hooks must be suppressed or retained | Ambiguous source ownership blocks commit |
| `ai_refresh_method` | No | Refreshes AI when the normal system does not react automatically | Required but missing refresh blocks the family |
| `report_visibility` | Yes | Public row, grouped summary only, or hidden | Hidden family cannot leak raw data |
| `report_label_source` | Required when public | Produces player-facing family name | Missing label downgrades to grouped summary or blocks required public row |
| `report_value_formatter` | Required when public | Formats before and after values | Missing formatter blocks the public row |
| `report_importance_method` | Required when public | Gives a normalized presentation score | Missing method blocks top-change ranking |
| `chaos_disruption_class` | Yes | Low, medium, or high contribution to one transaction score | Owner-provided class needs Event 46 approval |
| `achievement_comparability` | Yes | States whether the family can support ranking or recovery proof | Missing proof makes it achievement-ineligible |
| `cleanup_method` | Yes | Clears result plans and owner temporary state | Missing cleanup blocks registration |
| `save_resume_method` | Yes | Restores exact pending transaction state | Rerolling on load is forbidden |
| `test_scenarios` | Yes | Names required static, probability, and live cases | Missing required case blocks completion |
| `documentation_path` | Yes | Points to owner contract documentation | Undocumented family remains unavailable |

## Core registration rule

Core Event 46 families use the same schema as external adapters.

They do not receive undocumented shortcuts.

## Optional and mandatory distinction

A family can be optional at every capability because its current scope may not exist.

`mandatory_at_evolution_v` means it must participate when the family is registered, legal, non-conflicting, and has valid scopes.

It does not force an inland world to receive dockyards or a country without an active research project to receive research progress.

## Public registry view

The player does not see this schema.

Event Details shows capability domains and player-facing evolution text.

Debug and completion evidence can list family IDs, versions, scope counts, rejection reasons, and reconciliation results.
