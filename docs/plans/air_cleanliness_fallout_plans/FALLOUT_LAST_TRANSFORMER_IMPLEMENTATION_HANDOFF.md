# Last Transformer implementation handoff

This handoff covers the reviewed dormant Fallout pilot at event suffixes
`243` through `255`. It does not activate the Fallout scheduler and does not
claim completion of the Fallout release floor.

## Gameplay files

- `common/script_constants/fallout_consolidated_constants.txt`
  - ids, candidate identity, route, branch tokens, timing, costs, numerical
    thresholds, result deltas, history payloads, modifier values, and AI table
- `common/scripted_effects/fallout_consolidated_effects.txt`
  - Last Transformer candidate row and state priority selection
- `common/scripted_triggers/fallout_consolidated_triggers.txt`
  - state, receipt, partner, target, delayed-result, and cleanup gates
- `common/scripted_effects/fallout_consolidated_effects.txt`
  - partner selection, input snapshot, viability, branch payment, delayed
    result, Deaths failure path, state mutation, callback, AI parity, history,
    and cleanup
- `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`
  - timed industrial, clinical, microgrid, neighbour, and grid-failure
    modifiers
- `events/fallout_world_end_events.txt`
  - the thirteen Fallout-owned events in the `chaosx.fallout` namespace

## Presentation and log files

- `interface/fallout_consolidated.gfx`
  - `GFX_report_event_fallout_last_transformer`
- `localisation/english/fallout_consolidated_l_english.yml`
  - human opening, branch tooltips, result descriptions, callback text, and
    Event Log wording
- `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt`
  - payload-specific detail resolver
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
  - global history `9116` name and detail routing

## Asset handoff

The dedicated generated asset package is complete and separately manifested:

- Runtime DDS:
  `gfx/event_pictures/fallout/report_event_fallout_last_transformer.dds`
- Proposed sprite:
  `GFX_report_event_fallout_last_transformer`
- Source, processed PNG, contact sheet, prompt, manifest, and `.gfx` notes:
  `docs/assets/air_cleanliness_fallout/fallout_last_transformer/`

The asset is a fictional transformer yard report image. It contains no real
person, attested flag, Zombie reference, readable text, gore, or generic
apocalypse skyline. The manifest records the source and runtime SHA-256
values.

## Review evidence

The exact branch contract and static engine limits are recorded in
`FALLOUT_LAST_TRANSFORMER_CHAIN_PROOF.md`. The source has been checked for
balanced Clausewitz braces, duplicate new event suffixes, forbidden Zombie
references, missing Last Transformer localisation keys, and the required UTF-8
with BOM localisation encoding. No Hearts of Iron IV runtime was launched.

## Open handoff items

1. Keep the candidate and all thirteen events dormant until the Fallout
   scheduler activation review opens this route.
2. Prove live host authority, delayed-row persistence, callback timing, state
   scope retention, dynamic modifier visibility, and Deaths readback in a
   separately authorized runtime pass.
3. If a later engine-safe country-scoped partner display receipt is approved,
   add it without replacing the frozen country id. The current result text
   intentionally does not reread a mutable partner name.
4. Add the route to the release-floor review only after its caller, Event Log
   detail view, AI observations, save recovery, and manual audit are accepted.
5. Do not reuse this route's ids, asset path, sprite, or history id for a
   different Fallout event.

No fallback was used. The activation and runtime items are blockers, not
unstated simplifications.
