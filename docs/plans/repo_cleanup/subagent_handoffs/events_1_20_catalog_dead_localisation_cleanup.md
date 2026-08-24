# Events 1–20 catalog dead-localisation cleanup

## Scope

This bounded follow-up removes description wrappers and localisation keys made obsolete by commit `eec9f7692`, which routed Events 1, 2, and 11 directly to stable catalog descriptions and stopped locked, unrecorded, prefire, and generic bodies from overriding canonical evolution prose.

No gameplay effect, event title, dynamic title state, balance value, GUI source, interface layout, asset, workbook cell, or Event 21+ event-specific surface changed.

## Removed scripted-localisation methods

- `GetEventsLogSelectedCommunismEvolutionIntro`
- `GetEventsLogSelectedCommunismEvolutionGameplayImpact`
- `GetEventsLogSelectedZombieEvolutionIntro`
- `GetEventsLogSelectedZombieEvolutionGameplayImpact`
- `GetEventsLogSelectedZombieEvolutionDefenceLine`
- `GetEventsLogSelectedZombieEvolutionArmyAttackLine`
- `GetSecretAllianceEvolutionOneBody`
- `GetSecretAllianceEvolutionTwoBody`
- `GetSecretAllianceEvolutionThreeBody`

## Removed localisation families

- The private Event 1 communism evolution body wrapper and its six intro/impact keys.
- The private Event 2 zombie evolution body wrapper, two conditional line keys, and six intro/impact keys.
- The three Event 11 stage body wrappers and their six concealed/revealed result keys.
- `chaosx.events_log.window.event_details.evolution_entry_body_generic`.
- `utopia_manifesto.evolution.locked_body`.
- `resources_found.evolution.unrecorded.body`.
- `black_plague.evolution.stage_1.prefire.body` through `black_plague.evolution.stage_5.prefire.body`.

## Reference proof

Before deletion, repository-wide searches covered gameplay script, event files, scripted localisation, ordinary localisation, scripted GUI, interface definitions, GFX definitions, documentation, and spreadsheet exports. Each removed identifier was either definition-only or reachable exclusively through a wrapper already superseded by the stable catalog selector.

After deletion, focused searches across `common/`, `events/`, `interface/`, `gfx/`, and `localisation/` returned no occurrence of any removed method or key. Historical cleanup documentation retains names only as evidence of what was removed.

All edited English localisation files retain their UTF-8 BOM. The shared GUI layout and scripted GUI bindings were not edited.

## Retained candidates

The 28-key duplicate file `005_soviet_collapse_custom_splinter_focus_expansion_l_english.yml` was retained during this tranche because its canonical consolidated localisation file had active concurrent edits. The later [`remaining_safe_cleanup_2026-08-24.md`](remaining_safe_cleanup_2026-08-24.md) follow-up repeated the comparison and removed the duplicate after all 28 replacement keys were proven.

The unused dynamic effect `modify_value_based_on_chaos_tier` and its matching helper documentation were removed after exact runtime, meta, scripted-localisation, GUI, GFX, documentation, and spreadsheet scans found no consumer.

`damage_buildings_in_random_states` remains because the accepted Event 11 improvement addendum names it as a future sabotage implementation pattern. That plan reference makes it an uncertain future hook even though it has no current runtime caller.

## Validation boundary

Focused source-reference and encoding checks passed. Current HOI4 MCP event and GUI reruns timed out, so this handoff does not claim fresh rendered Event Details evidence or live-game validation.
