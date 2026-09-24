# Event 006 super-events

Event 006 owns two ordinary project-wide super-event slots: slot 23, *The League of New States*, and slot 24, *Every Border a Casus Belli*. Normal wave releases do not emit a super-event. The two milestones are guarded by the Event 006 League and high-chaos qualification predicates and enter the shared super-event FIFO so an occupied global window is not overwritten.

## Slot 23: The League of New States

Slot 23 is the first durable formal-league presentation. The League state machine reaches it through `independence_wave_mark_league_durable`, which clears the transient phase flags, records the durable phase and date, sets `independence_wave_durable_league_proclaimed` and `independence_wave_formal_league_active`, refreshes member idea lifecycles, and calls `independence_wave_publish_league_formation` through the authoritative League leader target.

`independence_wave_publish_league_formation` records Event Log history payload `23` with the founding country as actor, submits display slot `23` and audio ID `23` to the shared FIFO, and leaves the actual visible-window ownership and settings-aware playback to the common dispatcher. The first durable formal League is therefore a one-shot milestone even when the League later reforms, upgrades, or dissolves.

The player-facing package uses `chaosx_super_event.23.t`, `.d`, `.a`, and `.q`. The title is *The League of New States*. The quote is the short Point XIV excerpt attributed to Woodrow Wilson's *Fourteen Points* of 8 January 1918. The image is `GFX_super_event_006_asset_005_league_formation`, registered in `interface/006_independence_wave_small_assets.gfx` and sourced from `gfx/super_events/006_independence_wave/super_event_006_asset_005_league_formation.dds`.

## Slot 24: Every Border a Casus Belli

Slot 24 is the one-shot dangerous coordinated-bloc milestone. `independence_wave_evaluate_danger_milestone` uses a stable priority order when several factual witnesses are present, records one reason and actor, writes the Event Log history payload `24`, and submits display slot `24` and audio ID `24` to the same shared FIFO. The accepted reasons are a radical offensive League, a ten-country high-chaos opening-claim wave, synchronized former-host wars, a hidden-formable bloc center, or a League-sponsored cascade.

The high-chaos opening-claim witness is limited to an exact ten-country Totalen Chaos or World Collapse plan, requires armed or radical actors, reserves at most one adjacent former-host state per eligible actor, and freezes the successful actors and claimed states to the committed plan generation. This witness does not change the automatic wave count.

The player-facing package uses `chaosx_super_event.24.t`, `.d`, `.a`, and `.q`. The title is *Every Border a Casus Belli*. The quote is the short Hosea 8:7 excerpt in the King James Version. The image is `GFX_super_event_006_asset_006_revisionist_milestone`, registered in `interface/006_independence_wave_small_assets.gfx` and sourced from `gfx/super_events/006_independence_wave/super_event_006_asset_006_revisionist_milestone.dds`.

## Shared presentation contract

The slot and audio constants are centralized in `common/script_constants/006_independence_wave_constants_registry.txt` under `independence_wave_league_super_event` and `independence_wave_danger_milestone`. The common super-event scripted localisation maps the visible slot to `GetSuperEventImage`, `GetSuperEventTitle`, `GetSuperEventDesc`, `GetSuperEventRemark`, and `GetSuperEventQuote`; the shared super-event GUI consumes those getters.

The common `natural_disaster_emit_super_event` queue is used as the existing project-wide FIFO adapter. When an entry owns the visible window, the shared dispatcher assigns `global.current_super_event_audio_id` and the settings-aware playback helper selects the appropriate volume wrapper. This source wiring does not prove live firing, human perceptual audition, save/load persistence, or in-game click behavior.

The durable audio and rights record is `../../assets/006_independence_wave/super_events/audio/production_manifest.md`. The canonical catalogue is `music/chaosx_music_track_list.html`. The complete audio details, attribution obligations, runtime identifiers, and remaining validation limits are recorded in `audio_handoff.md` beside this file.

## Acceptance boundary

Slot 23 has source-wired image/text dispatch, the approved creator-owned audio package, six settings-volume wrappers, Event Log payload `23`, and durable-League FIFO publication. Human audition and live firing remain unverified. Slot 24 has source-wired image/text dispatch, final audio, six settings-volume wrappers, Event Log payload `24`, and five factual qualification predicates, but whole-chain reachability remains conditional on live host survival, Event 005 collision, claimable former-host borders, frozen-plan transaction success, and the unadmitted hidden-formable member set. Event 006 remains **HOLD / PARTIAL** until these and the other package, identity, rights, probability, GUI, MCP, and runtime gates close.

