# Event 017 Random Faction GFX Handoff

This handoff covers the Event 17 decision, decision-category, idea, achievement, and animated warning/seal package. Report-event pictures are outside this icon-artist handoff and were left unchanged.

## Verified Registries and Consumers

- Event sprite registry: `interface/017_random_faction.gfx`.
- Achievement sprite registry: `interface/chaosx_achievements.gfx`.
- Achievement definitions: `common/achievements/chaos_redux_achievements.txt`.
- Animated decision consumers: `common/decisions/017_random_faction_decisions.txt`.
- No custom `.gui` file is required; the animations are direct decision `icon` sprites.
- Offline reference: `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `frameAnimatedSpriteType` section.
- Vanilla reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/alerts.gfx`, which verifies horizontal frame sheets, `noOfFrames`, `animation_rate_fps`, looping, `play_on_show`, and transparent alert sprites.

## Static Icon Sprites

All entries below are registered in `interface/017_random_faction.gfx` and point to completed 32-bit A8R8G8B8 DDS files.

| Sprite | Asset type | Final DDS | Size | Gameplay consumer |
|---|---|---|---:|---|
| `GFX_decision_category_random_faction_bloc_pressure` | decision category icon | `gfx/interface/decisions/017_random_faction/decision_category_random_faction_bloc_pressure.dds` | 32x32 | `random_faction_bloc_pressure` category |
| `GFX_decision_random_faction_stabilize_alignment` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_stabilize_alignment.dds` | 32x32 | alignment stabilization decisions |
| `GFX_decision_random_faction_liaison` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_liaison.dds` | 32x32 | liaison decisions |
| `GFX_decision_random_faction_opposition` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_opposition.dds` | 32x32 | opposition decisions |
| `GFX_decision_random_faction_neutrality_council` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_neutrality_council.dds` | 32x32 | neutrality council family |
| `GFX_decision_random_faction_border_posts` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_border_posts.dds` | 32x32 | border-post family |
| `GFX_decision_random_faction_observers` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_observers.dds` | 32x32 | observer decisions |
| `GFX_decision_random_faction_neutrality_press` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_neutrality_press.dds` | 32x32 | neutrality-press decisions |
| `GFX_decision_random_faction_staff_mission` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_staff_mission.dds` | 32x32 | staff missions |
| `GFX_decision_random_faction_radio_networks` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_radio_networks.dds` | 32x32 | radio-network decisions |
| `GFX_decision_random_faction_corridor` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_corridor.dds` | 32x32 | guarantee-corridor family |
| `GFX_decision_random_faction_commitment` | decision icon | `gfx/interface/decisions/017_random_faction/decision_random_faction_commitment.dds` | 32x32 | commitment family |
| `GFX_idea_random_faction_alignment_shock` | idea icon | `gfx/interface/ideas/017_random_faction/idea_random_faction_alignment_shock.dds` | 64x64 | `random_faction_alignment_shock` |
| `GFX_idea_random_faction_border_pressure` | idea icon | `gfx/interface/ideas/017_random_faction/idea_random_faction_border_pressure.dds` | 64x64 | `random_faction_border_pressure` |
| `GFX_idea_random_faction_bloc_polarization` | idea icon | `gfx/interface/ideas/017_random_faction/idea_random_faction_bloc_polarization.dds` | 64x64 | `random_faction_bloc_polarization` |
| `GFX_idea_random_faction_neutrality_exhaustion` | idea icon | `gfx/interface/ideas/017_random_faction/idea_random_faction_neutrality_exhaustion.dds` | 64x64 | `random_faction_neutrality_exhaustion` |
| `GFX_idea_random_faction_liaison_mission` | idea icon | `gfx/interface/ideas/017_random_faction/idea_random_faction_liaison_mission.dds` | 64x64 | `random_faction_liaison_mission` |

## Animated Sprites

| Sprite | Final DDS | Frame geometry | Timing | State and fallback |
|---|---|---|---|---|
| `GFX_random_faction_bloc_pressure_seal_static` | `gfx/interface/animated/017_random_faction/random_faction_bloc_pressure_seal_static.dds` | 64x64 | static | frame-000 fallback for the neutrality-council icon |
| `GFX_random_faction_bloc_pressure_seal_animated` | `gfx/interface/animated/017_random_faction/random_faction_bloc_pressure_seal_sheet.dds` | 8 x 64x64; sheet 512x64 | 8 FPS, loop, play on show | used by `random_faction_convene_neutrality_council` |
| `GFX_random_faction_border_warning_static` | `gfx/interface/animated/017_random_faction/random_faction_border_warning_static.dds` | 64x64 | static | low-amber frame-000 fallback |
| `GFX_random_faction_border_warning_animated` | `gfx/interface/animated/017_random_faction/random_faction_border_warning_sheet.dds` | 8 x 64x64; sheet 512x64 | 8 FPS, loop, play on show | used by `random_faction_reinforce_border_posts` and `random_faction_guarantee_corridor_mission` |

The animated border warning is the selected low-resilience treatment because it uses eight genuine source-art states and communicates amber-to-red escalation more clearly than a static-only frame. The required static fallback remains available.

The registered definitions are:

```txt
spriteType = {
	name = "GFX_random_faction_bloc_pressure_seal_static"
	texturefile = "gfx/interface/animated/017_random_faction/random_faction_bloc_pressure_seal_static.dds"
	alwaystransparent = yes
}
frameAnimatedSpriteType = {
	name = "GFX_random_faction_bloc_pressure_seal_animated"
	texturefile = "gfx/interface/animated/017_random_faction/random_faction_bloc_pressure_seal_sheet.dds"
	noOfFrames = 8
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
	pause_on_loop = 0.0
	alwaystransparent = yes
}
spriteType = {
	name = "GFX_random_faction_border_warning_static"
	texturefile = "gfx/interface/animated/017_random_faction/random_faction_border_warning_static.dds"
	alwaystransparent = yes
}
frameAnimatedSpriteType = {
	name = "GFX_random_faction_border_warning_animated"
	texturefile = "gfx/interface/animated/017_random_faction/random_faction_border_warning_sheet.dds"
	noOfFrames = 8
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
	pause_on_loop = 0.0
	alwaystransparent = yes
}
```

The offline wiki spells one transparency property as `allwaystransparent`; vanilla and the existing Chaos Redux registry use `alwaystransparent`, so the registered vanilla spelling is retained.

## Achievement Triplets

All six completed, grey, and not-eligible variants are 64x64 root-level achievement DDS files and all 18 sprite definitions are registered in `interface/chaosx_achievements.gfx`.

| Achievement id | Completed | Grey | Not eligible |
|---|---|---|---|
| `017_random_faction_four_doors` | `gfx/achievements/017_random_faction_four_doors.dds` | `gfx/achievements/017_random_faction_four_doors_grey.dds` | `gfx/achievements/017_random_faction_four_doors_not_eligible.dds` |
| `017_random_faction_hold_the_line` | `gfx/achievements/017_random_faction_hold_the_line.dds` | `gfx/achievements/017_random_faction_hold_the_line_grey.dds` | `gfx/achievements/017_random_faction_hold_the_line_not_eligible.dds` |
| `017_random_faction_crowded_border` | `gfx/achievements/017_random_faction_crowded_border.dds` | `gfx/achievements/017_random_faction_crowded_border_grey.dds` | `gfx/achievements/017_random_faction_crowded_border_not_eligible.dds` |
| `017_random_faction_liaison_web` | `gfx/achievements/017_random_faction_liaison_web.dds` | `gfx/achievements/017_random_faction_liaison_web_grey.dds` | `gfx/achievements/017_random_faction_liaison_web_not_eligible.dds` |
| `017_random_faction_frontier_commitment` | `gfx/achievements/017_random_faction_frontier_commitment.dds` | `gfx/achievements/017_random_faction_frontier_commitment_grey.dds` | `gfx/achievements/017_random_faction_frontier_commitment_not_eligible.dds` |
| `017_random_faction_not_everyone` | `gfx/achievements/017_random_faction_not_everyone.dds` | `gfx/achievements/017_random_faction_not_everyone_grey.dds` | `gfx/achievements/017_random_faction_not_everyone_not_eligible.dds` |

## Task-Specific QA

- All 12 decision/category processed icons and all 5 idea icons have real transparent unused pixels, target dimensions, unique pixel hashes, and distinct source PNGs.
- All 6 achievement completed icons have unique source art; all grey variants are grayscale; all not-eligible variants contain the standard red cross overlay rather than a tint.
- Both animation packages preserve eight source frames and eight 64x64 processed frames. Their 512x64 sheet cells match the processed RGBA frames exactly, including alpha.
- Static fallbacks are exact copies of frame 000. GIFs contain the eight states plus a review-only repeated rest frame and are not runtime assets.
- Runtime DDS headers use 32-bit A8R8G8B8 masks; unused pixels remain transparent.

Blocked or missing icon assets: none.

Simplifications or substitute art: none.
