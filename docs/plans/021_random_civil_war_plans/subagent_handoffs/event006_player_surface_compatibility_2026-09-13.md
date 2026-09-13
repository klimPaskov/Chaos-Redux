# Event 006 player-surface compatibility handoff — 2026-09-13

Status: implemented for test entry. Runtime package, asset, save/reload, and player-consumer validation remain open.

## Scope

Event 021 may initialize a complete human Event 006 package even when the normal Independence Wave event never fired. The package must retain its Event 006 focus tree, decisions, categories, formable checks, AI, leaders, forces, and assets without becoming an active Event 006 origin or entering Event 006 lifecycle and league systems.

## Owner patch

`common/scripted_triggers/006_independence_wave_triggers.txt` now lets `is_independence_wave_event6_local_content_active` pass either a real `is_independence_wave_active_country` or a fully proven `is_independence_wave_event021_package_country`.

`is_independence_wave_event6_player_surface_allowed` uses the same two branches and continues to reject the bounded `random_civil_war_event6_adapter_preparing` setup window. The complete adapter branch is allowed after its package and origin receipts are proven.

`is_independence_wave_event021_package_country` remains the compatibility boundary in `common/scripted_triggers/021_random_civil_war_triggers.txt`. It requires a normal human country, complete Event 006 adapter and origin receipts, a package id, existence, and no active or ended Event 006 origin. Its normal-human predicate preserves `is_actual_nonhuman_country` immunity.

## Preserved boundaries

The patch does not set `independence_wave_active_origin`, the Event 006 fired marker, Event 006 evolution state, league membership, network state, or the Event 006 origin value. Event 006 lifecycle, evolution, league, and achievement paths continue to use their stricter active-origin predicates. The setup window remains package-content-only and cannot publish the player surface.

## Source evidence

The Event 006 focus tree consumes `is_independence_wave_event6_local_content_active`. The Event 006 decision categories and decisions consume either that local-content predicate or `is_independence_wave_event6_player_surface_allowed`, so the shared package-local content bridge covers the existing Event 006 player surfaces without duplicating or rewriting their files.

The static Event 006 country API, scenario matrix, allocator, FORM-16, and flag audits remain passing. The current focus inspection covers the shared 184-focus tree. These checks do not prove every package's engine-backed runtime loading, identity uniqueness, asset provenance, save/reload survival, or live player behavior.

## Validation boundary

No Hearts of Iron IV process was launched. The user-owned test pass must exercise at least one complete Event 021-origin package, verify the reused focus and decision surfaces, confirm actual nonhuman immunity, and check that Event 006 fired/evolution/league/network accounting remains unchanged. The admitted 32-package runtime matrix and inherited visual/provenance ledger remain acceptance gates.
