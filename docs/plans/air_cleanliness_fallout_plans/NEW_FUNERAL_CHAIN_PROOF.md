# A New Funeral chain proof

Status: dormant, statically reconciled, not release-floor credit.

## Identity and ownership

The chain owns candidate id `541`, transaction key `710051`, route `7151`, event ids `chaosx.fallout.541` through `chaosx.fallout.553`, and Event Log history `9156`. Gameplay lives in dedicated `fallout_world_end_new_funeral_*` plumbing files and the existing `events/fallout_world_end_events.txt` namespace `chaosx.fallout`. It does not reuse Names for the Missing ids, files, sprite, DDS, or localisation keys. It does not set scheduler activation flags.

## Candidate proof

`fallout_event_build_pilot_candidate_registries` initializes four durable country ledgers before evaluating `fallout_event_541_country_is_current`. The gate requires a current country registry row, durable identity and resources, material Deaths, incomplete Recognition, winter disease pressure or low Cohesion, and one authored cost route. The appended row stores a country subject with target id zero, first-winter phase, cause-memory cooldown, survival-resource severity, Air Winter disease pressure, current Cohesion, Recognition as the required resource, and route `7151`. No native state, province, character, neighbour, tag, or supply-node target is fabricated.

## Result, callback, and cleanup proof

The human opening and hidden AI lane share the same four branches. The result freezes Deaths, Recognition, Cohesion, disease pressure, family trust, religious tension, and public health before calculating a deterministic viability grade. The delayed result is 21 days and the callback is 180 days. Branch effects alter Food, Scrap, Power, Recognition, Cohesion, Stability, War Support, exposure, family trust, religious tension, disease pressure, and public health. Failed result and callback paths call the exact state population loss helper with the explicit minimum remaining population. Disease changes clamp the existing Air Winter ledger and refresh its native dynamic modifier. One hidden cleanup event releases the result and callback receipts and clears only transient registry and frozen values.

The delayed triggers require the current global generation, the same country owner, candidate `541`, target zero, current country row, durable resources, committed chain flag, and every frozen value. This is the engine-sensitive stale-scope proof for the no-target country lane.

## Presentation proof

The dedicated report image is a fictional symbolic imagegen source showing a cracked heated funeral hall, snowmelt, three survivor communities, and marked graves. The source and processed PNG are retained in `docs/assets/air_cleanliness_fallout/fallout_new_funeral/`. The processed card is 210 by 176, the DDS is a one-level uncompressed BGRA texture with the exact 210 by 176 payload length, and `interface/fallout_consolidated.gfx` points to the dedicated Fallout texture path.

The shared Event Log recognizes history `9156`, while `GetFalloutEvent541EventLogDetail` maps fifteen payloads to concrete branch and callback text. The localisation file is UTF-8 with BOM.

## Runtime boundary

No HOI4 runtime was launched, as requested. Static source checks cover ids, constant references, event and localisation coverage, balanced braces, unsupported comparison operators, DDS header fields, and unique asset paths. Popup order, save recovery, host authority, multiplayer input blocking, scheduler issuance, live Event Log rendering, and performance are not claimed as proven. The exact engine-native thermonuclear sweep remains a separate blocker.
