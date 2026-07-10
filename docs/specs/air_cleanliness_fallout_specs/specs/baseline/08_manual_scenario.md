# Air Cleanliness and Fallout World-End Source Spec, Part 8 Manual Scenario and Integration Rules

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

Working scenario label, not final localisation: manual Fallout scenario. The public padded id is assigned only after the live registry is scanned.

## Scenario purpose

The Fallout scenario is a manual sandbox trigger for a total world rewrite. It exists so the player can launch the end state directly from the Triggerable Scenarios menu without waiting for contamination, chaos, or another event.

## Manual scenario rules

The scenario must be directly launchable unless a world-end scenario is already active. It must not require chaos value, previous nuclear use, air contamination level, date, country route, or event history.

## Launch sequence

| Day | Action |
| ---: | --- |
| 0 | Player confirms scenario. All valid provinces receive thermonuclear strike effect. All states receive terminal contamination memory. |
| 1 to 7 | World remains visible. Fires, fallout, deaths, and contamination process. Countdown or warning marker stays visible. |
| 7 | Blackout sequence begins. Ordinary play is hidden. |
| 7 processing | Fallout map rewrite, country rewrite, focus-tree assignment, diplomacy reset, resource initialization. |
| 8 or later | Player returns to new Fallout world and first Fallout interface opens. |

## Type options

The core requested scenario is every-province thermonuclear destruction. Optional type buttons can exist only if the main type remains obvious.

| Type | Use |
| --- | --- |
| Total Thermonuclear Fallout | Required default. Nukes every valid province and fires Fallout after one week. |
| Air Collapse Fallout | No province nuke sweep. Starts above 100 percent air contamination and processes gradual-style Fallout. |
| Final Silence Aftermath | Starts the Fallout aftermath with Final Silence cause memory. |
| Chemical Sky Fallout | Starts Fallout with chemical saturation cause memory and toxic fog state classes. |
| Biological Ash Fallout | Starts Fallout with disease and altered biosphere bias. |

## Intensity slider

The user requested the every-province thermonuclear version. The slider can be harmless or can alter post-Fallout survival instead of whether the world is nuked.

| Intensity | Effect |
| --- | --- |
| Low | Every valid province is nuked, but more bunker and refuge states survive. |
| Medium | Every valid province is nuked, with balanced survivors. |
| High | Every valid province is nuked, more states become dead city and wasteland. |
| Maximum | Every valid province is nuked, with strong vitrified and mutant bias. |

If keeping the slider creates confusion, set intensity to fixed and say the scenario uses canonical total destruction.

## Event and catalog integration

Scan the complete writable scenario registry, find the highest live integer, and assign Fallout that integer plus one. Do not renumber existing scenarios and do not infer the id from an older snapshot. Document the verified padded id in the scenario catalog, triggerable-scenario docs, and Fallout source map. The detail text should explain the one-week processing delay without revealing hidden altered-country routes.

## Compatibility with other world-end events

Fallout can be an aftermath state for other world-end events. If a previous world-end event already ended the ordinary world, Fallout becomes the new campaign layer. The cause memory decides which branch content appears.

## Trigger gates

The only hard gate should be an active terminal state that cannot be safely replaced. If Fallout is already active, relaunch is blocked. If another terminal event is in its cinematic step, launch is blocked. Ordinary chaos, date, event, evolution, and route requirements must not block manual launch.
