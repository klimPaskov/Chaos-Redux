# Famine opposition effects

## Overview

`famine_resolve_opposition_channel` is a famine-owned, state-scoped, one-shot weighted resolution for a catastrophic famine that is visibly tied to an active requisition or extraction transaction.

The caller must already own the registered severe-famine state and must provide the state flag `famine_extraction_active`; this helper never searches for states, countries, parties, or movements.

The helper records a bounded pool, applies one existing political/resistance/autonomy consequence when a valid candidate exists, and always applies the general stability/blame consequence when the catastrophic responsibility proof is valid.

The helper has no migration lifecycle ownership. It does not create or clean cohorts, flight, trapped population, reception, border policy, corridors, or movement records.

## Owned files

| File | Public API |
| --- | --- |
| `common/script_constants/famine_opposition_constants.txt` | `famine_opposition_channel`, `famine_opposition_runtime`, and `famine_opposition_weight` |
| `common/scripted_triggers/famine_opposition_triggers.txt` | `famine_opposition_resolution_is_valid` and the seven candidate predicates |
| `common/scripted_effects/famine_opposition_effects.txt` | `famine_opposition_*` context, weight, consequence, and cleanup effects plus `famine_resolve_opposition_channel` |

## Effects and contracts

| Effect | Scope | Inputs | Outputs | Side effects |
| --- | --- | --- | --- | --- |
| `famine_opposition_initialize_pool` | state | none | complete pool manifest and zeroed candidate weights | resets this resolution's state-local candidate outputs |
| `famine_opposition_collect_context` | state | food score, extraction/governance components, extraction flag, atrocity/camp evidence, controller war state | temporary severity, responsibility, repression, and country-context values | no persistent gameplay effect |
| `famine_opposition_prepare_party_weights` | state | controller `party_popularity_100@democratic`, `@communism`, `@fascism`, and `@neutrality` | four state-local party weights | ruling party or non-positive support remains exactly zero |
| `famine_opposition_prepare_local_weights` | state | active state resistance and owner autonomy ratio/core proof | local resistance, national autonomy, and project weights | unsupported project movement remains zero |
| `famine_opposition_apply_general_consequence` | state | temporary severity and responsibility values | controller stability delta, blame memory, stage-resolution date | adds bounded negative stability and records responsibility memory |
| `famine_opposition_apply_selected_channel` | state | selected channel and temporary context values | party popularity, state resistance, or owner autonomy delta | applies one existing engine consequence only |
| `famine_resolve_opposition_channel` | state | all valid-resolution trigger inputs | selected channel, total weights, status, resolution date | selects at most one channel, fails closed at zero total weight, and applies general consequence |

All temporary values are computed from centralized `famine_opposition_weight` constants. No effect creates a party, ideology, country, focus, event, movement, or actor.

## Candidate registry and invalid-zero proof

| Candidate | Eligibility | Weight formula | Terminal effect |
| --- | --- | --- | --- |
| `party_democratic` | controller is not democratic and `party_popularity_100@democratic > 0` | current support plus bounded severity, responsibility, repression, country context, and party base | add bounded democratic popularity to controller |
| `party_communism` | controller is not communist and `party_popularity_100@communism > 0` | same bounded party formula | add bounded communist popularity to controller |
| `party_fascism` | controller is not fascist and `party_popularity_100@fascism > 0` | same bounded party formula | add bounded fascist popularity to controller |
| `party_neutrality` | controller is not neutrality and `party_popularity_100@neutrality > 0` | same bounded party formula | add bounded neutrality popularity to controller |
| `local_resistance` | `has_active_resistance = yes` and state `resistance > 0` | local base plus positive live resistance, proven-local bonus, severity, responsibility, and repression | add bounded resistance to the current state |
| `national_autonomy` | state is a core of `OWNER` and owner `autonomy_ratio > -1` | bounded severity, responsibility, repression, and subject-context values | add bounded autonomy score to owner |
| `project_movement` | requires an authoritative project movement proof variable that current source does not provide | fixed `project_authority_proven = 0` | never selected; no fake movement is created |

The pool initializes every weight to the centralized zero constant before eligibility checks. Each candidate weight is assigned a positive formula only inside its own validity trigger, so absent support, absent resistance, non-subject ownership, non-core states, and unavailable project proof are exact zeroes.

## Cadence, terminal state, and cleanup

The helper is intended to run once when the registered state transitions into `catastrophic_famine` while the same state still carries `famine_extraction_active` and a positive extraction component.

`famine_opposition_last_resolution_stage_date` compares against `famine_food_stage_started_date`, preventing a second resolution during the same catastrophic stage while allowing a later catastrophic stage after recovery.

The random-list selection is terminal for that stage: `famine_opposition_selected_channel` is one enum value or `none`, and `famine_opposition_resolution_status` is `selected` or `fail_closed`.

The helper has no global event target and no periodic scan. Any regular event target used by a caller to retain the state scope is caller-owned and automatically expires with that effect chain. Candidate weights and status remain on the registered state as audit memory; state retirement uses the existing famine/migration registration cleanup and does not leave a global registry entry.

## Usage example

Call from the existing registered state transition immediately after the catastrophic stage flag and active food registration are set, with the caller preserving the explicit requisition proof:

```text
if = {
	limit = {
		check_variable = { var = famine_requested_food_stage value = constant:famine_food_stage.catastrophic_famine compare = equals }
		has_state_flag = famine_extraction_active
		check_variable = { var = famine_component_extraction > constant:famine_food_component.zero }
	}
	famine_resolve_opposition_channel = yes
}
```

The caller remains responsible for ensuring the state is already in the sparse severe-famine registration and for avoiding any world or country iteration.

## Probability audit contract

The named scenario is `prob_opposition_channel` from `famine_and_migration_system_probability_scenarios.csv`.

The required adapter is `custom_weighted_pool`, with the seven registry names above, zero invalid weights, state-transition cadence, and terminal cleanup described here.

The owner evidence and exact MCP blockers are recorded in `docs/plans/famine_and_migration_system_plans/subagent_handoffs/opposition_channel_owner.md`.

## External stale-reference map

The famine core calls `famine_resolve_opposition_channel` from `common/scripted_effects/famine_core_effects.txt` with the famine-owned stage, extraction, component, and exposure context. No migration-owned input participates in opposition selection.

The owned triggers call the shared humanitarian validation names `humanitarian_state_is_valid` and `humanitarian_country_is_valid`; no opposition helper calls a shared `humanitarian_corridor_*` API, and no migration lifecycle helper is introduced.
