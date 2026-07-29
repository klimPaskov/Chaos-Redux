# Air Cleanliness, Air Winter, and Fallout Core Mechanics Handoff

## Status

The core mechanics tranche is source-ready for user-owned in-game validation.

This handoff does not claim that the complete Fallout content goal is finished. It establishes the stable systems boundary needed before successor, focus, decision, event, and scenario-content expansion continues.

## Live core ownership

Air Contamination remains a host-owned basis-point system with chemical, biological, nuclear, and low capped natural-source inputs. Wildfires, volcanic eruptions, active ash, and settled-ash aftermath use typed receipts, low individual values, and the shared natural-source reservoir cap.

Air Winter uses phases 0 through 6 and maintains Exposure, Recovery, Adaptation, Food, Shelter, Water, and Reclamation values per valid state. The existing monthly state pass drives population loss through Deaths reason 17, building damage, supply pressure, state-category degradation, military movement and attrition, air-operation penalties, disease pressure, decisions, event candidacy, mapmode data, and ordinary-map regional visuals.

Fallout entry is owned by one idempotent request coordinator. Air Contamination at 100 percent, terminal source events, and the manual scenario route all enter that coordinator. Fallout does not require Chaos above 1000.

The Fallout consequence occupies only the world-end selector row that replaces retired Final Silence. It is not registered as an ordinary event, ordinary Event Details card, Event Log event, evolution, or ordinary super-event. Internal callbacks and survivor content use `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`. The blackout still uses a dedicated dramatic sound surface.

## Permanent atmosphere contract

Request intake uses `fallout_air_cleanliness_disabled` only as a reversible transaction pause. Rejected validation clears it.

A committed Fallout transition calls `fallout_lock_air_cleanliness_after_fallout_admission`, which sets `fallout_air_contamination_permanent_99`, fixes both total Air Contamination and the Fallout-owned source at 9,900 basis points, zeros all later source and decay deltas, and refreshes threshold and modifier consumers. Save reconciliation calls the same idempotent effect.

The Air setting cannot change this permanent state. Air Winter pauses while `fallout_transition_active` protects the frozen rewrite snapshot, then resumes its state simulation against the fixed atmosphere. Pre-Fallout response decisions and phase-event dispatch remain closed after `fallout_active`, so no stale projects or popup candidates can mutate the consequence world.

## Population and physical rewrite contract

Fallout state grading is deterministic. The grade ladder requests 90, 91, 92, 93, 94, or 95 percent population removal and protects a one-person floor. The observed population delta, not the requested estimate, is registered once through Deaths reason 19. Population mutation and Deaths accounting use separate generation-bound receipts so a recovery call cannot delete or register the same population twice.

The same frozen state transaction owns building loss, category conversion, supply collapse, government classification, technology regression, player reservation, allocation proofs, and map-return postconditions. Release-gated fracture and successor materialization surfaces remain closed until their separate conflict and package ledgers are complete.

## Map and presentation proof

The three Air Winter map modes have script, icon, and localisation consumers for phase, exposure, and survival.

The normal-map route has all 81 expected class, phase, and prop entity aliases, 85 referenced PDX meshes, 85 matching mesh definitions, four present particle atlases, and nine referenced particle types with matching particle definitions. The route distinguishes regional snow and frost, cold rain, ash, dead vegetation, frozen water, dim ground materials, and thaw. Warm regions do not receive universal snow.

Unused full-screen regional grade and static-alternative sprite registrations were removed. Their DDS plates remain source assets only, so no unowned interface sprite surface remains.

The Fallout blackout sound call resolves to six dedicated volume variants in `sound/fallout_world_end_sound.asset`, backed by `sound/fallout_world_end/fallout_world_end_blackout.wav`.

## Static wiring evidence

The dedicated Fallout callback file contains 721 unique `chaosx.fallout` event definitions. All 721 referenced Fallout ids resolve, and no duplicate id is present.

The event source uses 1,873 localisation keys, all of which resolve after accounting for permitted leading whitespace in localisation files.

All 87 event picture references resolve to registered sprites. The wider Fallout, Air Winter, and mapmode GFX set references 220 textures, all present in the mod or installed vanilla files.

A repository helper audit compared 1,401 relevant Fallout and Air Winter calls with 19,085 scripted effect and trigger definitions and found no unresolved helper call.

The Fallout manual scenario owns id 14, which is the previous live maximum 13 plus one. The retired Final Silence selector is absent from the live registry, while compatibility callers redirect to Fallout.

## Intentionally closed surfaces

The manual all-valid-province thermonuclear sweep remains release-gated by `fallout_manual_native_sweep_release_enabled`. The generated installed-map substrate targets 10,154 provinces in 41 batches and specifies an exact seven-day countdown after verified batch completion, but exact native strike execution and callback timing cannot be proven from static script alone. The manual launch button therefore remains unavailable until the user accepts live proof.

The wider Fallout scenario remains content-incomplete. Successor allocation, dynamic fracture release, general player-continuation packages, country focus layers, the active living-world scheduler, full reviewed event-floor credit, and final scenario content remain queued for later tranches.

## Validation boundary

Hearts of Iron IV was not launched. Live host authority, save recovery, blackout input capture, native strike behavior, map rendering, and campaign balance belong to the user's later validation. This is not treated as missing implementation work for the core source tranche.
