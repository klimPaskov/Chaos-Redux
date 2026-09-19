# Event 021 aligned front-plan registry repair

Date: 2026-09-19

Owner: parent implementation thread

Disposition: implemented for the bounded source tranche; runtime and final acceptance evidence remain open.

## Scope

The repair closes the source gap in which Event 021 could retain separate primary and optional-secondary receipts without one aligned pre-commit front plan that the durable registry and settlement review could consume.

## Changed gameplay surfaces

- `common/script_constants/021_random_civil_war_constants.txt` adds the centralized four-row `maximum_planned_fronts` cap, plan actor and relationship enums, plan status enums, and the `administrative_continuity` front objective.
- `common/scripted_effects/021_random_civil_war_parent_effects.txt` initializes and clears the aligned plan arrays, appends host, primary, optional ordinary, optional Event 006, and same-tag rows, validates row and flattened-state alignment, rehydrates primary and secondary starters by planned front id, marks optional rollback rows rejected, and blocks resolution while rows remain planned.
- `common/scripted_effects/021_random_civil_war_effects.txt` binds front registration and priority selection to the matching plan row and copies row metadata to the live actor.

## Row contract

The normal bounded order is host remnant, primary claimant, optional ordinary secondary, and optional Event 006 secondary.

Each row records front id, archetype, anchor, capital, objective, status, source or carrier scope, actor type, generation, route source, package id, flattened connected-state count and offset, force divisions, force manpower, opening size, stockpile envelope, army, navy, and air shares, and relationship.

The host remnant uses `administrative_continuity`, primary and ordinary rows retain route-specific objectives, Event 006 rows use `independence`, and same-tag rows use `command_seizure` with `loyalty_contest`.

## Validation and evidence

The focused read-only `hoi4.event_inspect` lint for `{ kind: event, eventId: chaosx.nr21.1 }` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and zero skipped sources. The installed service returned its cached revision and deferred helper and lifecycle projection for the large workspace, so this is structural evidence only.

Static touched-file review found balanced script blocks, no unsupported `<=` or `>=` operators, no `ROOT.global` scope misuse, and a corrected normal-start indentation boundary.

No live HOI4 run, save/reload sequence, four-row scenario, settlement sequence, performance measurement, or independent before/after probability certificate is claimed by this handoff.

## Remaining gates

The shared fixed-target provider contract, inherited Event 006 package reachability and asset provenance, full current weighted-surface comparison, helper-expanded lifecycle evidence, and user-owned live testing remain open. Event 021 and SCN-018 stay `Needs Testing`; this handoff does not authorize a final completion claim.
