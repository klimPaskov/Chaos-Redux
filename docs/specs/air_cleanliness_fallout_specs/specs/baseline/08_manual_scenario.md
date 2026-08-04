# Air Cleanliness and Fallout World-End Source Spec, Part 8 Manual Scenario and Integration Rules

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

Working scenario label, not final localisation: manual Fallout scenario. The internal reservation is assigned only after the live registry is scanned.

Current consequence correction: Fallout is not an ordinary Event Log row, evolution, ordinary super-event, ordinary Event Details card, or world-end selector row. The Fallout-owned manual launch uses raw id 14. The active substrate contains the exact 10,154-province, 41-batch sweep, completion receipts, and seven-day handoff. Runtime observation belongs to the user and is not a source release gate.

## Scenario purpose

The Fallout scenario is a manual sandbox trigger for a total world rewrite. Its Fallout-owned launch surface uses raw id 14. The static map ledger, native call construction, completion barrier, and seven-day handoff are recorded in the implementation proof and wired into the active launch path.

## Manual scenario rules

The scenario is directly launchable unless a world-end scenario is already active. It does not require chaos value, previous nuclear use, air contamination level, date, country route, or event history.

## Launch sequence

| Day | Action |
| ---: | --- |
| 0 | Player confirms scenario. All valid provinces receive thermonuclear strike effect. All states receive terminal contamination memory. |
| 1 to 7 | World remains visible. Fires, fallout, deaths, and contamination process. Countdown or warning marker stays visible. |
| 7 | Blackout sequence begins. Ordinary play is hidden. |
| 7 processing | Fallout map rewrite, country rewrite, focus-tree assignment, diplomacy reset, resource initialization. |
| 8 or later | Player returns to new Fallout world and first Fallout interface opens. |

## Population-loss contract

The completed manual scenario must remove approximately 90 through 95 percent of each state's population according to the standard Fallout grade ladder. This is the total loss measured from the population immediately before the province sweep, not a second 90 through 95 percent loss applied after the visible seven-day interval.

For the thermonuclear type, the verified native-strike aggregate itself uses a direct 90 through 95 percent band from the prestrike population. The first strike starts at 90 percent and additional province strikes add only a small capped increment. The seven-day rewrite remains idempotent and requests only any remaining grade-specific difference.

The manual coordinator records every state's prestrike population before the first native launch. Strike and first-week deaths remain visible and enter the Deaths system. During the standard rewrite, the population phase removes only the additional amount needed to reach the grade-specific survivor target from that original baseline. A nonempty state retains the existing one-person floor. Missing, stale, or arithmetically inconsistent provenance blocks the population phase and must never fall back to applying the ordinary percentage to the already reduced population. If the frozen post-seven-day population is already below the grade survivor target, the transition enters a terminal contract error. It must not silently accept excess loss or add population.

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

Scan the complete writable scenario registry, find the highest live integer, and reserve the Fallout-owned manual trigger at that integer plus one. Do not renumber existing scenarios and do not infer the id from an older snapshot. Record the reserved id and proof status in Fallout source documentation. The reservation may appear only as the Fallout-owned manual sandbox row. It is never inserted into the ordinary Event Log, ordinary Event Details, evolution, or ordinary super-event registries. The seven-day processing delay belongs to the Fallout-owned blackout and callback presentation, not to an ordinary event row.

## Compatibility with other world-end events

Fallout can be an aftermath state for other world-end events. If a previous world-end event already ended the ordinary world, Fallout becomes the new campaign layer. The cause memory decides which branch content appears.

## Trigger gates

The only hard gate should be an active terminal state that cannot be safely replaced. If Fallout is already active, relaunch is blocked. If another terminal event is in its cinematic step, launch is blocked. Ordinary chaos, date, event, evolution, and route requirements must not block manual launch.
