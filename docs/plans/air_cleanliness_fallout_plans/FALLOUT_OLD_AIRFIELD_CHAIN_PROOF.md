# Fallout Old Airfield Chain proof

The Old Airfield Chain is implemented under the Fallout namespace in `events/fallout_world_end_events.txt` with human opening `chaosx.fallout.586`, hidden AI opening `587`, delayed results `588` and `589`, callbacks `590` and `591`, and authenticated cleanup `592`.

The chain uses candidate `586`, transaction key `710056`, scheduler route `7156`, route upper bound `7157`, and Event Log history `9162`. The candidate row is appended by `fallout_event_build_pilot_candidate_registries` and remains dormant until the Fallout scheduler owns activation.

## Contract evidence

The country admission trigger requires a current Fallout registry row, current-generation Survival resources, Latin America and Caribbean region membership, campaign days `730` through `5999`, an affordable branch, and no active or durable Old Airfield receipt.

The state admission trigger requires current owner and controller authentication, a produced Air Winter snapshot, Supply Access at least `18`, Reclamation at least `8`, Exposure below `75`, Disease Pressure below `70`, population above `3,000`, at least one non-damaged air-base level, an air-base total below `10`, at least one non-damaged infrastructure level, and no reserved or closed state memory.

The candidate builder selects the lowest eligible native state id. It does not enumerate historical airports and it has no capital fallback. The selected state id remains in the candidate row until authenticated cleanup.

The four opening branches have dedicated costs and distinct ledgers. Civil air service spends Fuel `6`, Scrap `5`, Power `4`, and Recognition `2`. Military network spends Fuel `8`, Power `5`, and Command Power `15`. Private couriers spend Fuel `4`, Scrap `3`, and Recognition `1`. International consortium spends Fuel `5`, Scrap `4`, Power `5`, and Recognition `6`.

The result score is deterministic. It averages ten equal-weight components for air-base condition, infrastructure, Supply Access, Reclamation, Fuel, Power, Recognition, Cohesion, inverse Exposure, and inverse Disease Pressure, then applies only the selected branch adjustment and clamps the result from `0` through `100`. The shared weights are `1` with divisor `10`, so admission minima do not force every branch to success. It contains no `random_list`, MTTH, reroll, or post-payment regrade.

Success adds Supply Access `6`, Reclamation `4`, and one instant air-base level while staying below the vanilla cap of `10`. Partial adds Supply Access `2` and Reclamation `1` without a building level. Failure subtracts Supply Access `5` and Reclamation `3`, increases Exposure by `6`, damages one operational air-base level, and requests `0.05%` of the frozen state population through the Deaths system with a minimum remaining population guard.

The callback waits `270` days after the result. It reauthenticates the owner, controller, target state, branch, result receipt, and Fallout generation. Its score is a deterministic equal-weight mean of route reliability, flight safety, current Supply Access, current Reclamation, Recognition, branch trade or military control, intelligence reach, inverse Exposure, inverse smuggling pressure, and inverse external dependency. Callback failure requests `0.02%` Deaths and may damage one remaining operational air-base level. Military Command Power uses the engine `add_command_power` effect, War Support uses `has_war_support` on the `0` through `1` scale and `add_war_support`, and result modifiers consume the dedicated `180` day duration.

Human and hidden-AI branches share costs, result grading, callbacks, Event Log payloads, cancellation, and cleanup. AI priority is deterministic with the tie order civil service, international consortium, military network, and private couriers. An unaffordable or unauthenticated branch cannot be selected.

## Event Log and presentation evidence

History `9162` has dedicated choice payloads `1` through `4`, result payloads `11` through `43`, callback payloads `51` through `53`, and cancellation payload `99`. This is twenty payloads in total. The chain writes the Fallout country-memory event type with the recipient country as primary actor and authenticated target state as secondary actor.

`GetFalloutEvent586EventLogDetail` routes all twenty payloads to concrete Old Airfield detail strings. The shared Event Log detail and history-name routers include history `9162`. The central event-type resolver also recognizes the dedicated Fallout history constant.

The durable country memory preserves the selected branch, deterministic result grade, callback grade, target route type, and final callback quality after transient registry cleanup. A generation reset calls the chain-owned abort effect before shared scheduler ledgers clear, refunds a paid but unresolved opening, releases state and country modifiers, clears state reservations, and removes the orphaned pending rows. The same abort now authenticates an issued but uncommitted Old Airfield opening against its dispatch target, cancels it when the target is no longer current, records the cancellation history, releases the reservation, and clears the frozen snapshot before shared receipt cleanup.

Human events use `GFX_report_event_fallout_old_airfield_chain`, registered in `interface/fallout_world_end.gfx`. The runtime DDS is `gfx/event_pictures/fallout_world_end/report_event_fallout_old_airfield_chain.dds`. Its source, prompt, processed `210x176` preview, manifest, hashes, and handoff are under `docs/assets/586_old_airfield_chain/`. The source is fictional generated report art showing a repaired Latin American highland runway, radio mast, weathered transport aircraft, mechanics, civilian handlers, and guarded cargo without readable signage or modern equipment.

## Static checks

The touched Old Airfield constants, triggers, effects, dynamic modifiers, event blocks, GFX container, and dedicated Event Log scripted localisation are brace balanced. New event localisation has a UTF-8 BOM and covers every title, description, option, tooltip, Event Log, and dynamic modifier key referenced by the tranche. The report DDS declares `210x176`, has a 128-byte legacy header, has exact one-level uncompressed BGRA length, and matches the processed preview dimensions.

The repository collision scan found only the intended definitions for event ids `586` through `592`, candidate `586`, transaction `710056`, route `7156`, and history `9162`. The chain has no Zombie Apocalypse runtime id, file, asset, audio, sprite, or path reference.

## Engine-sensitive boundary

Offline documentation and installed vanilla precedents support state-scoped `damage_building = { type = air_base ... }`, state-scoped `add_building_construction = { type = air_base level = 1 instant_build = yes }`, delayed country events, state flags, dynamic modifiers, and country or state Event Log actors.

The read-only `hoi4.event_inspect` lint request for events `586` through `592` could not complete because the MCP transport closed. Static source checks cover the new opening-target cancellation branch with balanced braces and no forbidden comparison operators. No HOI4 process was run, as required by the task. Live scheduler activation, host authority, multiplayer ordering, save recovery across both delays, Event Log rendering, ownership loss during a live transaction, and runtime air-base presentation therefore remain unproven. This tranche is not release-floor credit while the scheduler is dormant.

## Scope exclusions

The chain does not create a partner country, reciprocal air access, faction, aircraft unit, air wing, equipment, recurring decision, bilateral compact, focus tree, scripted GUI, super-event, or recurring incident. Those surfaces remain queued until their own engine and content contracts are accepted.
