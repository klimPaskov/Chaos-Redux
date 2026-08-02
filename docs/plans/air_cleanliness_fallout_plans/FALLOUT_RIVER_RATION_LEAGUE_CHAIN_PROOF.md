# Fallout River Ration League chain proof

## Scope

The River Ration League is a dormant ordinary Fallout regional chain for the Danube corridor.

It is not a super-event and it does not use zombie-owned ids, files, assets, audio, sprites, or paths.

The chain owns `chaosx.fallout.565` through `chaosx.fallout.571`.

The candidate id is `565`.

The transaction key is `710053`.

The route is `7153` with upper bound `7154`.

The Event Log history is `9158`.

## Source map

The accepted source specification is `docs/specs/air_cleanliness_fallout_specs/specs/54_reviewed_regional_river_ration_league.md`.

The reviewed addendum is `docs/plans/air_cleanliness_fallout_plans/2026-07-26_river_ration_league_addendum.md`.

The event definitions are in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

The candidate producer is `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.

The chain triggers are in `common/scripted_triggers/fallout_world_end_river_ration_league_event_triggers.txt`.

The chain constants are in `common/script_constants/fallout_world_end_river_ration_league_constants.txt`.

The chain effects are in `common/scripted_effects/fallout_world_end_river_ration_league_event_effects.txt`.

The Event Log detail resolver is `common/scripted_localisation/fallout_world_end_river_ration_league_event_log_scripted_localisation.txt`.

The dedicated report asset manifest is `docs/assets/air_cleanliness_fallout/fallout_river_ration_league/manifest.md`.

The runtime sprite is `GFX_report_event_fallout_river_ration_league` in `interface/fallout_world_end.gfx`.

## Static contract

The candidate selector uses the fixed corridor order `152`, `4`, `664`, `155`, `43`, `109`, `82`, `45`, `108`, `46`, `48`, and `77`.

It chooses the first eligible corridor state as upstream and the highest eligible later state as downstream.

It rejects a row without two distinct current-generation states.

The state gate checks native Fallout identity, owner, controller, population, Supply Access, frozen Air Winter source values, and exclusive memory flags. Rewritten current wasteland categories do not invalidate an otherwise surviving state row.

The country gate checks Europe, campaign timing, current country and survival rows, complete branch affordability, and the persisted two-state receipt.

The opening freezes both state snapshots, both current state generations, the country survival ledger, trust, tension, and the selected branch.

The four exact opening receipts are Joint Food 6, Fuel 4, Recognition 3, Upstream Food 4, Fuel 3, Recognition 2, Armed Customs Scrap 4, Fuel 6, Recognition 2, and Flood Authority Clean Water 4, Scrap 7, Power 6.

The result is scheduled for 42 days and the institutional callback is scheduled for 180 days.

The grade is deterministic and uses the four accepted weighted formulas, government archetype adjustment, and the two ten-point exposure and disease penalties.

The result and callback use the accepted branch-specific resource, Supply Access, cohesion, trust, tension, reclamation, and infrastructure changes.

The bounded tranche applies no population loss.

The callback stores branch and grade memories on the country and both states, seeds the accepted federation or barge-war continuation flags, and closes the chain only after both cleanup receipts are released.

## Event Log contract

History `9158` records opening choice codes `11` through `14`, result codes `21` through `53`, callback codes `61` through `93`, and cancellation code `99`.

The primary actor is the country and the secondary actor is the frozen upstream state.

The event detail resolver and name mapping are wired through the shared Events Log localisation surface.

## Asset proof

The final report DDS is `gfx/event_pictures/fallout/report_event_fallout_river_ration_league.dds`.

Its SHA-256 is `7f1688f6ef41b1d20e38d5ac8a4a2002bcf77e5373a3d42422f6593af270c8c2`.

The asset is 210 by 176 pixels in legacy uncompressed BGRA format.

The source, processed preview, prompt, and conversion evidence are retained in the dedicated asset package.

## Engine-sensitive boundary

The shared scheduler activation flags remain unset.

No global daily, weekly, or monthly iterator was added for this chain.

No HOI4 runtime was launched.

Static syntax and ownership checks do not prove scheduler dispatch, event presentation, save recovery, multiplayer ownership, or delayed timing in the live engine.

The read-only event inspector returned `EVENT_INSPECTED_PARTIAL` for `chaosx.fallout.565` with a bounded 120-node and 240-edge view. Its linked report is diagnostic evidence only and does not prove the dormant scheduler route or runtime delivery.

The exact native all-valid-land-province thermonuclear sweep remains a separate unresolved manual-scenario blocker.

The chain is therefore implemented, wired, documented, and dormant rather than claimed as runtime-proven or release-floor credit.
