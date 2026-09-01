# Event 006 GLC no-additive roster repair

Date: 2026-08-30

## Decision

IW-015 Galicia uses the no-additive-commander owner choice from the earlier duplicate-identity audit. Vanilla GLC already supplies Alfonso Daniel Castelao as its liberal country leader, so Event 006 does not create or recruit a second Castelao character.

## Source changes

- `history/general/006_independence_wave_character_recruitment_registry.txt` no longer recruits `GLC_independence_wave_alfonso_daniel_castelao`.
- `common/characters/006_independence_wave_characters_registry.txt` no longer defines the duplicate Event 006 Castelao character.
- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt` proves the preserved Fuco Gómez and Alfonso Daniel Castelao country-leader roster with `ruling_only = no`.
- `common/scripted_effects/006_independence_wave_effects.txt` applies `GFX_portrait_GLC_alfonso_daniel_castelao` once per package generation to the existing liberal Castelao role when the GLC roster checkpoint runs.
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt` restores `GFX_portrait_Alfonso_Daniel_Castelao` during GLC cleanup and clears the package-scoped portrait override flag.
- `localisation/english/006_independence_wave_iberian_l_english.yml` removes the now-unused duplicate-character name and description keys while retaining the shared GLC package wording.

## Runtime contract

The GLC p15 territorial-defense force uses the institutional officer commission already described by the force mapping, so its force loader depends on the preserved country-leader roster rather than an additive Castelao corps-command character. NAV retains its separate named Aguirre corps-command consumer and cleanup path. Central content attestation, adapter and Join wiring, rights, typed probability, MCP, and the 32/29/40/161 boundary are unchanged and remain fail-closed.

## Source evidence

Vanilla `history/countries/GLC - Galicia.txt` supplies Fuco Gómez, Alfonso Daniel Castelao, Vicente Martínez Risco, and Santiago Casares Quiroga, with Castelao as the liberal country leader and `GFX_portrait_Alfonso_Daniel_Castelao` as the vanilla portrait. Vanilla effects documentation supports `has_country_leader` with `ruling_only`, `set_country_leader_portrait` with an ideology and portrait sprite, and character-scoped role effects; no dynamic token is required for the preserved leader path.

## Validation and limits

The focused allocator, country API, strict flag-family, FORM-16, and SCN-008 scenario-matrix validators pass after the repair. Targeted source assertions pass: the removed character ID has no non-document consumer, the GLC roster proof contains both preserved vanilla leaders, and the portrait override flag has one setup and one cleanup path (each represented by its guard and mutation). No live game, save/load, or Event MCP route evidence is claimed here.

The required read-only Event MCP checks were rerun for `chaosx.nr6.1` after the source edit with bounded downstream lint and overview render, both at depth 1, 20 nodes, 40 edges, helper expansion disabled, and refresh enabled. Lint returned `EVENT_INSPECTED_PARTIAL` with no blockers and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6af41d04f98d1e2620be0b25e6febacc829bc2e9228d22d8695bc5e01d256a3a/14716229ceaf0e598360d511c000a20c38629063b7b304f98b9836f16a75d84e/event-lint-ce33d5ee346e.json`; its validation remains partial because workspace helper/lifecycle projections were deferred and it reports two workspace-level blocking diagnostics in the aggregate counts. Overview render returned `EVENT_RENDERED_PARTIAL` with no blockers and layout artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e755d6edf2c733067a9f0fb9d78003ad7c6e98a0d99a09e05802ac9b92b39690/2df9fd3bfb610f6cd09f3e49c750f3454f04d4d07077702c538e9321b7703a33/event-overview-ce33d5ee346e-manifest.json`; this is supplementary structural evidence, not live engine proof.

An attempted `hoi4.event_compare` between the recorded prior revision `ac2516cf55a82d5ce3152e98d00c31e148f74b85a13a09c3ad7791c0453bef18` and the current revision `ce33d5ee346e83cd752f9a7ea7b893351b5ef03e4debec28c8db99693b2bba24` returned `EVENT_REVISION_NOT_CACHED` with no artifact, so no before/after graph delta is claimed.

The repair resolves the duplicate Castelao identity at source but does not promote IW-015 or clear its independent rights, package, AI/probability, MCP, or central-attestation gates.
