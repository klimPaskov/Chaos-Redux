# chaosx_dynamic_triggers

This file documents reusable cross-system scripted triggers defined in `common/scripted_triggers/chaosx_dynamic_triggers.txt`. Subsystem-private APIs belong beside their owning system even when several files inside that system call them.

## Reuse guidance

Use this registry only for triggers with demonstrated call-site breadth across unrelated systems or event families. Reusable logic confined to one subsystem belongs in that subsystem's scripted-trigger files and dedicated reference documentation.

## Table of contents

- [is_desert_state](#is_desert_state)
- [is_special_chaos_country](#is_special_chaos_country)
- [is_actual_nonhuman_country](#is_actual_nonhuman_country)
- [uses_normal_civilian_systems](#uses_normal_civilian_systems)
- [Famine and migration validation contracts](#famine-and-migration-validation-contracts)

Country-classification helpers are implementation checks. Keep their complete bodies inside `hidden_trigger` so nested tags, flags, and provider triggers never leak into player-facing requirement tooltips. A caller that needs to explain an eligibility rule must provide a concise custom tooltip for that surface.

## is_desert_state

State-scope trigger. Returns true for the maintained list of desert states used by shared event and map logic.

The list is an explicit state-ID registry because the game does not expose a shared desert-region collection for this mechanic. Each state appears once so callers receive the same boolean result without duplicate alternatives.

When adding a state, update this trigger and record the consuming event or system in its documentation. Do not replace the list with an event-local desert classifier.

## is_special_chaos_country

Country-scope trigger. Returns true for system actors and special scenario countries that should not be treated like normal civilian societies.

The complete classifier is hidden from generated tooltips. Adding a provider must keep it inside the existing `hidden_trigger` block.

Current coverage includes:

- `ZZZ` / original `ZZZ` outbreak countries
- dynamic zombie outbreak countries
- weaponized zombie outbreak countries
- `REV` and countries with original tag `REV`
- communist rebel-state flags
- `ZIN`
- countries using the `The Holy Realm` cosmetic tag
- countries using the `The Great Mandala` or `The Silent Mandala` Holy Realm identity cosmetic tags
- countries with the Holy Realm active marker
- Germany Mengele civil-war and post-coup state markers
- active Fury actor countries
- `DTH` / original `DTH` / countries with the Death country marker
- `DHO` / original `DHO` / countries with the Event 018 cave-country marker
- Event 014 cannibal warlord countries
- the unified Event 014 country
- the transformed Event 014 Wendigo country
- Event 019 derivative countries through
  `is_infantry_spawn_derivative_country`. A human claimant breakaway requires
  the derivative marker, claimant marker, positive claimant UID,
  ordinary-family sentinel, and no nonhuman marker. A nonhuman family host
  requires the derivative and nonhuman markers, a positive registered family
  ID, parent-isolation proof, and public-package proof. Future registered
  families therefore need no classifier list edit.
- The fixed Event 016 `KRG` country and any host transformed by proven
  institutional capture. Hosted Directorates remain ordinary countries.
- Event 020 `RTA` Rat Nation and `RTX` Rat King actors through the shared
  `black_plague_rat_country` and `black_plague_rat_king_country` markers. Both
  are special actors and are excluded from ordinary human-host logic.

## is_actual_nonhuman_country

Country-scope trigger. Returns true only for countries that should currently be treated as actually nonhuman rather than merely unusual or scenario-specific.

The complete classifier is hidden from generated tooltips. Adding a provider must keep it inside the existing `hidden_trigger` block.

Current coverage includes:

- `ZZZ` / original `ZZZ` outbreak countries
- dynamic zombie outbreak countries
- weaponized zombie outbreak countries
- Wendigo outbreak flags or the Wendigo cosmetic tag
- `ZIN`
- `DTH` / original `DTH` / countries with the Death country marker
- `DHO` / original `DHO` / countries with the Event 018 cave-country marker
- the transformed Event 014 Wendigo country; ordinary cannibal warlords and the ordinary unified country remain human
- Event 019 derivatives through
  `is_infantry_spawn_nonhuman_derivative_country`, which requires the nonhuman
  marker, positive registered family ID, parent-isolation proof, and
  public-package proof; claimant-only human breakaways remain special without
  being classified as nonhuman
- Event 016 Kruger sovereignties only after an explicit machine, clone-only,
  engineered-biological, or alien-government population transition. A human
  Kruger State remains special without being classified as nonhuman.
- Event 020 `RTA` Rat Nation and `RTX` Rat King actors through the shared
  `black_plague_rat_country` and `black_plague_rat_king_country` markers. Their
  plague immunity and non-human forces depend on this classification.

The current Event 019 registry/scenario v4 reaudit is clean for both shared
classifier routes. Neither trigger contains a zombie, ghost, golem, or future
provider list, and neither classifier contributes to a parent event's actor,
stage, evolution, super-event, or world-end state.

## uses_normal_civilian_systems

Country-scope trigger. Returns true when the country is not currently classified by `is_actual_nonhuman_country` and may use ordinary civilian systems.

This inverse classifier is also fully hidden. Player-facing systems that need to explain why a country is excluded must provide their own direct tooltip instead of exposing the nonhuman registry.

## Famine and migration validation contracts

The famine and migration predicates live in `common/scripted_triggers/chaosx_famine_migration_triggers.txt`.

`famine_migration_country_is_valid` accepts only an existing country that is neither a special Chaos actor nor an actual nonhuman country, using the shared `is_special_chaos_country`, `is_actual_nonhuman_country` through `uses_normal_civilian_systems`, and normal-civilian classifiers.

`famine_migration_state_is_valid` requires an existing populated state whose owner and controller both pass the shared human-civilian classifier.

`famine_migration_pressure_request_is_valid` requires a valid state, positive amount, non-unknown source, actor proof, and an explicit request proof flag.

`famine_migration_route_request_is_valid` requires positive people, border, transport, safety, and actor proof plus a saved destination event target that passes `famine_migration_destination_is_valid`.

`famine_migration_destination_is_valid` requires a valid destination state and explicit food-safety and reception-capacity proof.

`famine_migration_blockade_proof` is deliberately conjunctive and requires owner and controller war state plus island, isolation, maritime-dependence, either route or port disruption, either convoy or escort shortage, no-humanitarian-corridor, and insufficient-local-food proof.

`famine_migration_return_request_is_valid` requires explicit origin-safety, route, food, housing, persecution, contamination, and host-acceptance proof.

`famine_migration_border_policy_is_valid` accepts only the seven constants in `famine_migration_border_policy`.

All predicates are hidden and read-only. Missing variables evaluate to zero, so incomplete requests fail closed without a fallback route.

`famine_migration_state_has_active_context` recognizes only valid states with a submitted context, profile, or positive food pressure, keeping the scheduled registry sparse.

`famine_migration_food_stage_is_active` and `famine_migration_food_stage_requires_mortality` distinguish non-stable stages and acute-or-worse stages for evaluator and mortality gating.

`famine_migration_state_can_retire` requires a valid stable state without positive food pressure; `famine_migration_retire_recovered_state` then clears active context flags and unregisters the state. `famine_migration_surface_context_request_is_valid` requires a valid state plus explicit surface and actor proof.

`famine_migration_historical_profile_context_is_resolved` is true only inside the resolver's successful audited result, and `famine_migration_historical_profile_candidate_is_valid` is true only for a valid state with an active registered profile candidate and one of the fifteen centralized profile IDs. The separate `famine_migration_historical_profile_anchor_active` flag marks a state in the bounded audited anchor registry; the anchor processor selects a profile ID from live map/date/control/causal inputs before invoking the resolver. The resolver itself supplies the profile-specific state/date/control/causal gates; caller-set context booleans cannot bypass them.

`famine_migration_cohort_record_request_is_valid`, `famine_migration_cohort_destination_bind_request_is_valid`, `famine_migration_cohort_resettlement_rebind_request_is_valid`, `famine_migration_cohort_forced_destination_bind_request_is_valid`, `famine_migration_cohort_origin_resolution_is_valid`, `famine_migration_cohort_destination_resolution_is_valid`, `famine_migration_forced_return_request_is_valid`, `famine_migration_reception_delta_request_is_valid`, and `famine_migration_cohort_cleanup_request_is_valid` validate the persisted cohort ledger, exact reception accounting, and return contracts. The rebind predicate requires the resolved current host/owner targets, new destination, positive food/reception/route/actor proof, and rejects the current host as destination. The destination-resolution predicate intentionally calls normal destination safety, so unsafe forced-bound rows remain resolvable for forced-return metadata but fail safe resettlement.
