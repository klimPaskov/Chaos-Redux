# Fallout Radio Island Chain proof

Status: implementation tranche complete and statically reviewed, dormant and outside release-floor credit.

## Ownership and collision proof

The chain is Fallout-owned and lives under `add_namespace = chaosx.fallout` in `events/fallout_world_end_events.txt`.

The identity set is candidate and human opening `600`, hidden AI opening `601`, human result `602`, hidden AI result `603`, human callback `604`, hidden AI callback `605`, cleanup `606`, transaction `710057`, route `7157`, route upper bound `7158`, and Event Log history `9163`.

The new identity set does not overlap the existing Fallout rows or the zombie namespace, and the chain has its own constants, scripted triggers, scripted effects, dynamic modifiers, scripted localisation, localisation file, report source, processed image, DDS, sprite registration, manifest, prompt, and handoff.

## Candidate registry and target authority

The ordinary Fallout candidate registry appends one row only after selecting the lowest eligible native state in `fallout_region.oceania_remote_islands` with the strongest radio or radar and infrastructure score.

The selector uses native `non_damaged_building_level@radar_station`, `non_damaged_building_level@infrastructure`, and `non_damaged_building_level@industrial_complex` values, resolves ties by stable state id, and stores one state target rather than a synthetic state or a capital fallback.

The country gate requires current-generation identity and survival receipts, Power 18, Fuel 12, Filters 8, Recognition 10, Cohesion 24, the first-winter-year or later phase, and at least one affordable authored branch.

The state gate requires a produced current-generation Air Winter snapshot, surviving population, Reclamation at least 8, Supply Access at least 12 and below 88, exposure from 16 through 71, disease pressure below 68, coastal or air-base geography, at least one non-damaged radar level, and infrastructure or industry capacity.

The opening receipt reauthenticates the issued token, human or hidden-AI mode, country ownership, controller, target state, transition generation, and ordinary receipt before any branch is visible or paid.

## Branch contracts and engine-native military values

Public relay spends Power 6, Fuel 4, Filters 3, and Recognition 3.

Maritime defense net spends Power 5, Fuel 6, native Command Power 10 through `add_command_power`, and native War Support through `has_war_support` at the 0.55 threshold.

Harbor subscription spends Fuel 4, Scrap 3, Recognition 2, and requires Power at least 18.

Island federation spends Food 5, Power 4, Recognition 5, and requires Cohesion at least 40.

Every branch has a truthful admission trigger, one shared payment helper, a non-zero failure route, a hidden-AI branch path, and a refund path for generation invalidation or delayed-result scheduling failure.

## Deterministic result and callback

The result schedules exactly 35 days after the opening and the callback schedules exactly 240 days after the result.

The result grade is an integer weighted average with ten equal component weights and a divisor of 100, clamped from 0 through 100 without random or MTTH selection.

The current frozen components are Power, Fuel, Filters, Cohesion, Recognition, averaged relay, contact, and intelligence signal quality, Reclamation, Supply Access, inverse Exposure, and inverse Disease.

Branch-specific success and partial thresholds are 62 and 42 for public relay, 66 and 44 for maritime defense net, 64 and 42 for harbor subscription, and 60 and 38 for island federation.

The result and callback reauthenticate the transition generation, owner, controller, host state, branch, result token, callback token, and delayed receipt ticket.

Failure uses the Deaths system through the exact state civilian population-loss contract, with a 1.5 percent result loss and 0.8 percent callback loss subject to the minimum remaining population contract.

## Memory, Event Log, and cleanup

History `9163` routes public-relay, maritime-defense, harbor-subscription, island-federation, callback, and cancellation payloads through the shared Fallout Event Log name and detail surfaces.

The country is the primary actor and the authenticated host state is the secondary actor for the dedicated history entry.

Cleanup releases the result and callback receipts, clears state reservation and transient transaction variables, removes every dedicated dynamic modifier, and preserves the completed flag, selected branch memory, result grade, callback grade, institution memory, and signal-quality memory.

Generation invalidation refunds unresolved branch costs, releases the state reservation, removes dedicated modifiers, clears transient receipts, and preserves only durable route memories. The chain-owned abort now also authenticates an issued but uncommitted human or hidden-AI opening against its dispatch target, records a cancellation when the radio station state is no longer current, releases both reservation markers, and clears the frozen snapshot before shared receipt cleanup.

No scheduler activation flag is written by the candidate registry, opening, result, callback, or cleanup path.

## Dedicated report asset proof

The generated source is `docs/assets/600_radio_island_chain/source_generated.png` with SHA-256 `7ef9cf02b4d05ca2601f21537a3242523a03ea23a09e3de9218a0c8bd4e62965`.

The processed report image is `docs/assets/600_radio_island_chain/processed_210x176.png` with SHA-256 `eb337a17a8c954895e0c1af208cc9d1946fa10c1b035d6b2358856f82a2616cb`.

The runtime DDS is `gfx/event_pictures/fallout_world_end/report_event_fallout_radio_island_chain.dds` with SHA-256 `8cbdfb43937b4cd4c4fd39fcdd334228a3812386a455af39daac1e60c3798d73`, DDS magic `DDS `, a 124-byte header, width 210, height 176, 32 bits per pixel, and a 147968-byte file length equal to the expected BGRA payload.

The sprite `GFX_report_event_fallout_radio_island_chain` is registered in `interface/fallout_world_end.gfx` and the manifest records source, processed, runtime, prompt, and handoff provenance.

The event catalogue workbook uses Events row 248 for `FALLOUT-600`, and the refreshed Events CSV export has SHA-256 `435579e209f6b9daafcbf4b069f61ad12988375dbada75dd8d78ff34ddeba14e`.

## Static review and blockers

The dedicated effects, triggers, dynamic modifiers, scripted localisation, and event blocks are brace-balanced after the missing population-loss closure was corrected.

The touched scripts contain no unsupported `<=` or `>=` operators, no zombie identifiers, no stale Weather Station or medicine branch names, and no em dashes or semicolons in player-facing localisation. The new opening-target cancellation branch is brace-balanced and uses the existing Radio Island tokens, cancellation history stage, reservation flags, dedicated modifiers, and frozen snapshot helper.

No HOI4 runtime was launched, as requested. The read-only `hoi4.event_inspect` lint attempt also returned `Transport closed`. Event issuance, popup delivery, hidden-AI routing, save interruption recovery, multiplayer host authority, and Event Log rendering therefore remain engine-sensitive observations rather than claims.

The exact manual scenario requirement to thermonuclear-strike every valid province, finish the batch, wait exactly seven days, and then run the standard blackout and rewrite remains an explicit blocker because an engine-native all-valid-province sweep has not been proven.

The Fallout scheduler remains dormant, so this tranche contributes zero of the 660 manually reviewed release-floor blocks and cannot establish the requested 90 to 180 meaningful events over ten years.
