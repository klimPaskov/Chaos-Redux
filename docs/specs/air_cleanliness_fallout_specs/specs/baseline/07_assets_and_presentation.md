# Air Cleanliness and Fallout World-End Source Spec, Part 7 Asset and Presentation Direction

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

This file gives asset direction only. It is not a final asset manifest.

## Visual promise

Fallout needs a new visual language. It should not reuse only old nuke icons and radiation modifiers. The air system should feel technical and readable. Fallout should feel like the map has entered another game.

## Required UI and map assets

| Asset family | Source mode | Purpose |
| --- | --- | --- |
| Air mapmode legend | Generated UI or hand-authored UI | Shows winter phases 0 to 6. |
| Air mapmode layer buttons | Icon artist | Switch winter, fallout exposure, and survival value layers. |
| Winter state modifier icons | Icon artist | Haze, soot veil, black snow, long winter, dead sky. |
| Fallout state class icons | Icon artist | Bunker city, dead city, greenhouse, badlands, forbidden zone, mutant biosphere, port remnant. |
| Survival resource icons | Icon artist | Food, clean water, medicine, scrap, fuel, power, filters, shelter, recognition. |
| Black screen overlay art | Generated UI | Pure black overlay with subtle atmospheric texture. It must remain readable and not become a super-event image. |
| Fallout intro interface | Generated UI panel | Shows cause memory, resources, first objectives, mapmode entry. |
| Decision category icons | Icon artist | Survival ledger, state recovery, salvage, refugee policy, mutant policy, diplomacy, late ambition. |
| Focus icon family | Icon artist | One family per archetype plus regional overlay icons. |
| Achievement icons | Icon artist | Completed, grey, and not eligible variants. |
| Cosmetic flags | Generated or sourced by identity | Many successor flags. Historical flags and real symbols must be sourced, fictional flags can be generated. |
| Leaders and councils | Generated for fictional leaders, sourced for real people | Continuity councils, bunker directors, warlords, food boards, mutant courts, technates. |
| Report images | Generated documentary style unless real source is required | Winter flavour, black snow, greenhouses, shelter riots, dead-city salvage. |
| News images | Generated or sourced | Treaty collapse, first dead city, post-Fallout recognition. |

## Animated assets

Animation should be used where the system feels alive.

| Animated asset | State logic | Frame direction |
| --- | --- | --- |
| Air mapmode warning frame | Appears when selected state is Phase 4 or higher | Slow warning pulse, real frame sheet, static fallback. |
| Fallout resource shortage seal | Appears when food, water, or shelter is critical | Distinct frames for low, crisis, and collapse. |
| Reactor keep warning | Active when meltdown mission is running | Slow flicker and warning light. |
| Mutant polity leader overlay | Only for major mutant route reveal | Subtle glow or breathing light, no transform-only animation. |
| Bunker authority seal | Opens shelter governance window | Slow mechanical door or lamp sequence. |
| Greenhouse refuge panel | Food compact high output | Gentle grow-light cycle, state-driven not decorative. |
| Black screen text glow | During blackout only | Center text fade and subtle ash, not a GIF asset. |

Every animation must follow the frame-animation skill. It needs real source frames, processed frames, sheet DDS, static fallback, preview GIF only for review, and GFX handoff.

## Country visual identity rules

- Old base flags should not be overwritten unless the old tag is deliberately transformed.
- Fallout identities should use cosmetic tags or route flags.
- Historical or attested symbols need sourced documentation.
- Fictional mutant flags can be generated.
- One-person fictional leaders need apparent gender presentation and matching name pools.
- Councils and committees should use institutional names and collective portraits.

## Black screen presentation assets

The blackout sequence needs:

1. Fullscreen black overlay.
2. Text style rules for centered sequence.
3. Optional ash or dust texture layer.
4. Progression variable or scripted GUI state for text beats.
5. A non-super-event audio or silence design handoff if audio is added later.

Because the user explicitly rejected a super-event, the blackout assets must not be wired through the super-event slot, super-event quote, or super-event button system.
