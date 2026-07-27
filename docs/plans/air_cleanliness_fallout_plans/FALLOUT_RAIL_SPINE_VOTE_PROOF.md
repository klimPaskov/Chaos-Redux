# Fallout Rail Spine Vote proof

## Ownership and identity

The reviewed candidate is `621`. The human and hidden AI opening events are `chaosx.fallout.621` and `chaosx.fallout.622`. The delayed result pair is `623` and `624`. The callback pair is `625` and `626`. Cleanup is `627`. The transaction key is `710060`, the scheduler route is `7160`, the route upper bound is `7161`, and Event Log history is `9166`.

The chain is owned by the Fallout scheduler and remains dormant. It does not set a scheduler activation flag, use a zombie id, create a country tag, or use a second request coordinator.

## Engine-sensitive surfaces

The target trigger reads `fallout_pretransition_non_damaged_rail_way` and `non_damaged_building_level@infrastructure` in a state scope. It also checks the current Fallout state row, current owner and controller, current Air Winter snapshot generation, state population, Supply Access, Reclamation, shelter capacity, Exposure, Disease Pressure, region, and state reservation flags.

The snapshot resolves the dispatch target to a state and re-reads the native railway and infrastructure surfaces before payment. The state is reserved with `fallout_event_621_registry_reserved`. Failure applies native `damage_building` effects to `rail_way` and `infrastructure`. The successful route is remembered as `fallout_rail_spine_route_status` and presented through a dedicated state modifier. This is a native railway read and damage path, not a variable-only railway substitute.

Population loss is requested through `apply_exact_state_civilian_population_loss`. Result failure requests `0.03%` of the frozen state population. Callback failure requests `0.012%`. Both paths supply the shared Deaths contract and the fallout aftermath reason.

The delayed result and callback use the shared receipt scheduler, exact branch and token checks, generation-bound registry, result and callback tickets, hidden AI parity, and explicit cleanup. Event Log payloads use history `9166` and a state secondary actor. The Event Log router has one narrow detail entry and one narrow name entry for this history.

## Dedicated asset proof

The report card source, preview, manifest, prompt, and handoff live under `docs/assets/621_rail_spine_vote/`. The runtime file is `gfx/event_pictures/fallout_world_end/report_event_fallout_rail_spine_vote.dds`. The sprite is `GFX_report_event_fallout_rail_spine_vote`.

The source is `1370x1148`. The preview is `210x176`. The DDS has DDS magic, a 124-byte header, 32-bit BGRA pixels, one mip level, a pitch of `840`, and a total size of `147968` bytes.

The SHA-256 values are:

- `source_generated.png`: `4409b9c38f1b403af24d35776efc1b0b08f3600f9167b55d3913fa03679c85e0`
- `processed_210x176.png`: `83f0cba85c284c46f6809bfc727ec2fe1a4042dc893eb311cd250ad16c50b1d8`
- `report_event_fallout_rail_spine_vote.dds`: `f5e84b2a1d6608855e0b2af0ab8ef96e21fec7bb91179e8d23fa0b2df40705a8`

The image is fictional and contains no real people, flags, readable text, or reused event art.

## Static review

The new effects file has balanced braces `770/770`. The new trigger file has balanced braces `81/81`. The candidate registry remains balanced at `2776/2776`. The events file remains balanced at `11571/11571`. The new dynamic modifier file has balanced braces `9/9`.

The seven new event ids each occur once. The dedicated localisation has 62 unique keys and a UTF-8 BOM. The event references for 621, 623, and 625 resolve to the dedicated localisation file. The new effects, triggers, and candidate row reference 181 unique Rail Spine constants, all present in `fallout_world_end_rail_spine_vote_constants.txt`.

## Workbook and release floor

The authoritative workbook row is `FALLOUT-621`. The exporter output is updated from the workbook after the row is accepted. This tranche adds one reviewed regional row and seven event blocks. The release floor remains `0 of 660` because the scheduler activation proof is still pending.

## Remaining blockers and simplifications

No claim is made for the exact all-valid-province thermonuclear sweep, full-screen blackout host authority, save recovery, multiplayer input blocking, normal-map visual cold route, wasteland conversion, successor allocation, surviving-country focus content, or live delayed delivery. Those obligations remain outside this dormant regional tranche. The implementation does not launch Hearts of Iron IV.
