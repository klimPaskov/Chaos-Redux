# chaosx_dynamic_triggers

This registry documents the reusable scripted triggers declared in `common/scripted_triggers/chaosx_dynamic_triggers.txt`. It is limited to cross-system classifiers whose results must remain consistent across unrelated callers.

Event-owned validation predicates belong in the owning scripted-trigger file and its reference documentation. The shared classifiers below may read owner-set marker flags, but they do not own event lifecycle, stage, evolution, or UI rules.

## table_of_contents

- [is_desert_state](#is_desert_state)
- [is_special_chaos_country](#is_special_chaos_country)
- [is_actual_nonhuman_country](#is_actual_nonhuman_country)
- [uses_normal_civilian_systems](#uses_normal_civilian_systems)
- [shared_classifier_ownership](#shared_classifier_ownership)

## is_desert_state

Scope: state.

Purpose: return true for the maintained desert-state registry used by shared event and map logic.

The list is explicit because the game does not expose a shared desert-region collection for this mechanic. Each state appears once so every caller receives the same boolean result.

When adding a state, update this trigger and record the consuming system in its documentation. Do not replace the registry with an event-local desert classifier.

## is_special_chaos_country

Scope: country.

Purpose: identify system actors and special scenario countries that must not be treated like ordinary civilian societies.

The complete classifier is hidden from generated tooltips. Its coverage is marker-based and includes outbreak identities, rebel and Holy Realm identities, Death and cave actors, cannibalism actors, registered derivative families, captured Kruger institutions, and rat actors.

Owner systems set their stable marker flags. The classifier only answers the shared routing question; it does not inspect an event's current stage, history, evolution, or cleanup state.

## is_actual_nonhuman_country

Scope: country.

Purpose: identify countries that are currently nonhuman rather than merely unusual or scenario-specific.

The complete classifier is hidden from generated tooltips. It recognizes the nonhuman subset of the shared outbreak, Wendigo, Death, cave, derivative-family, Kruger-transition, and rat markers.

Human claimant breakaways, ordinary human hosts, and other special-but-human actors remain outside this result. Owner packages must set the marker only after the relevant population or institutional transition is proven.

## uses_normal_civilian_systems

Scope: country.

Purpose: return true when the country is not currently classified by `is_actual_nonhuman_country` and may use ordinary civilian systems.

This inverse classifier is also hidden from generated tooltips. Player-facing systems that need to explain an exclusion must provide their own concise tooltip instead of exposing the shared registry.

## shared_classifier_ownership

The special-country and actual-nonhuman classifiers are intentionally centralized because famine, migration, population, occupation, event, and provider systems use them as shared exclusion and routing contracts.

When a new system actor is added, its owner sets a stable marker and updates these classifiers only if the actor's shared civilian or nonhuman treatment changes. Do not add event-specific validation, stage checks, provider callbacks, lifecycle state, or player-facing text here.

Owner-specific validation remains in the owning files, including `common/scripted_triggers/humanitarian_validation_triggers.txt`, `common/scripted_triggers/famine_core_triggers.txt`, `common/scripted_triggers/migration_core_triggers.txt`, `common/scripted_triggers/migration_destination_selection_triggers.txt`, and `common/scripted_triggers/migration_forced_movement_triggers.txt`.

All predicates in those owner files are read-only and should fail closed when their request proof, state target, or persisted ledger data is incomplete.
