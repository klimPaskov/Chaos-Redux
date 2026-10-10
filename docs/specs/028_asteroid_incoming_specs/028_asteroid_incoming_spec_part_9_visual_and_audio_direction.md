# Asteroid Incoming, Part 9: Visual and Audio Direction

Status: implemented and installed; native playback of the map visuals and in-game asset consumers remain live checks.
Asset provenance, dimensions and review records are in `docs/events/028_asteroid_incoming/assets/` and `docs/assets/028_asteroid_incoming/`; sprites are registered in `interface/028_asteroid_incoming.gfx` and achievement triplets in `interface/chaosx_achievements.gfx`.

## Visual identity

Event 028 looks like period observation, civil defence and physical destruction.
Generated documentary images match 1936 to 1945 photography, clothing, architecture, vehicles and observatory equipment.
They avoid modern space-agency rooms, modern emergency vehicles, satellite or orbital views, science-fiction panels, holograms, readable generated text and disaster-film grading.

## Map presentation

The user requires the nuclear-scale explosions to be presentation only.
The [map presentation contract](../../events/028_asteroid_incoming/map_presentation.md) implements this with two graphics-only entities defined in `gfx/entities/028_asteroid_incoming_visuals.asset`:

- the main visual clones vanilla `nuke_big_entity` and plays at the locked centre inside the impact transaction;
- the fragment visual clones vanilla `nuke_entity` and plays at each fragment centre, one every four hours after the main strike, from a persistent queue that survives saves.

No `launch_nuke`, raid, bomb or nuclear callback is used.
Each visual uses the shared state anchor province, a private reserved entity id, a one-shot receipt, and retirement at the first monthly host cleanup 30 days later.
A missing anchor records a failed visual and never redirects the impact.
The sequence never holds the game; the reports and the map carry the lasting information.

## Event images

| Surface | File | Direction |
| --- | --- | --- |
| Opening board report | `report_event_028_asteroid_tracking.dds` | Period observatory team tracking a bright object |
| Preparedness report | `report_event_028_asteroid_target_emergency.dds` | Rail evacuation, field hospitals, archives moving under a strange sky |
| Main-footprint country report | `report_event_028_asteroid_impact_report.dds` | Collapsed rail, dust-covered streets, period rescue crews; country neutral |
| Fragment-only country report | `report_event_028_asteroid_fragment_report.dds` | A smaller distant impact and debris trail; independent of the main image |
| Close-passage news | `news_event_028_asteroid_close_passage.dds` | Observatory dome or public viewing of a bright object, black and white |
| Impact and dust news | `news_event_028_asteroid_impact.dds` | Wide monochrome crater and industrial aftermath with broken rail, no flash; also used by the dust bulletins |
| Super-event | `super_event_028_asteroid_impact.dds` | A vast impact flash and debris column over a period landscape with buildings for scale; no flags, landmarks, map or text |

Every image serves any target country; none shows flags or a named real city.

## Category picture

The Asteroid Recovery category uses one static generated picture (a rescue rail line, dust protection, damaged infrastructure and a darkened sky) plus the vanilla generic-crisis category icon.
It paints no buttons, meters, numbers or text.

## Icon families

| Family | Count | Notes |
| --- | ---: | --- |
| State modifiers | 7 | Main crater, catastrophic, major, outer shock, fragment crater, heavy and light fragment damage; Fragment Centre Recovery reuses the fragment-crater icon |
| Material profile markers | 3 | Dense metallic, fused silicate, shock crystal; 32x32 with native alpha |
| National ideas | 8 | Four dust stages, protection, recovery burden, main-crater material, fragment material |
| Decisions | 14 | One subject per action; the three rival crater actions share the reconnaissance icon |
| Achievements | 5 triplets | Completed, grey and not-eligible variants |

Dust and mineral icons stay visually distinct: dust uses atmosphere, filters and obscured industry; minerals use dense metal or crystal without fantasy glow.
Crater icons stay distinct from radiation icons and from each other.

A dedicated rival-action icon family is an optional future addition, not a requirement.
If the fragment-marker cleanup in Part 5 is accepted, the fragment-material idea icon moves to the fragment armour dynamic modifier, which already uses it.

## Dust progression

Dust changes through ideas, modifiers and text; static stage icons are the accepted baseline.
An animated category picture would need a separate frame-animation plan with real frames and a static fallback, and only if it adds clear state information.

## Audio

The super-event plays one unique licensed musical cue: a public-domain Brahms recording at `sound/028_asteroid_incoming/super_event_028_asteroid_impact.wav`, through the shared settings-aware super-event path.
Its source, licence and edit record are in `docs/super_events/028_asteroid_incoming_super_event_research.md`.
Map explosions inherit the vanilla visual's own sound; the super-event music stays separate.
The image, title, quote, button remark and music describe the same moment.
