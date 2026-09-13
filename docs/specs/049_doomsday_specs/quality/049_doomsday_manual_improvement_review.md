# Event 049 Manual Improvement and Anti-Bloat Review

## Review question

Does the design deliver the event promise of a world that abandons the future, while keeping the player-facing system readable and avoiding duplicate systems, generic stat dust, unnecessary tags, and spectacle without play?

## Findings retained in the final spec

### Two public values are enough

Doomsday Conviction and Time Until the End answer the two questions the player repeatedly needs to ask: how widely the belief has taken hold, and how long remains before the date.

Local belief, organization, movement currents, peace pressure, institutional continuity, and terminal readiness are useful simulation inputs. Showing them as persistent counters would exceed the event’s accepted cognitive budget. The final design keeps them hidden or converts them into short qualitative states and actionable tooltips.

### A full scripted mechanic window would add overhead

The event has one global meter, one date, a country posture, phased decisions, and a small active mission set. A normal decision category with stage-specific category pictures and a compact status header can communicate this clearly.

A full window would create layout, state, asset, and AI-equivalent work without giving the player a clearer decision. The final design does not plan one.

### Country transformation should preserve countries

The core political crisis affects ordinary countries. Replacing many of them with new tags would damage existing focus trees, diplomacy, military history, and multiplayer continuity.

The final design uses political transformations, institutional councils where needed, ideas, cosmetic titles, focus overlays or emergency branches, and Final Assembly membership. New tags are not planned.

### The world-end route needs several proofs

A single Conviction threshold would reduce the terminal route to meter filling. The final design requires 1000 or more Chaos, Evolution II, an enabled branch, no active world end, and one of several sustained global breakdown paths.

This keeps The Final Vigil connected to government replacement, major-power demobilization, pacifist capture, or suppression-driven collapse.

### The failed date needs full gameplay

The source brief makes disconfirmation central. Treating the date as one popup would waste the event’s strongest consequence.

The final design gives the date a timed sequence, movement splits, legitimacy outcomes, institutional recovery, debt and savings problems, military reconstitution, education and research restoration, and one bounded revised-date hardliner problem.

### Peace pressure must respect war context

Automatic global white peace would erase strategy and duplicate the Peace event family.

The final design uses per-war pressure, bilateral or multilateral negotiation, refusal consequences, and distinct treatment for defensive survival wars, civil wars, colonial wars, ideological wars, and aggressive wars.

### Preparation should retain real value after failure

Shelters, reserves, relief corridors, and records should help against famine, disasters, bombing, plague, or migration pressure even when the prophecy fails.

This prevents every cooperative or preparatory choice from becoming a trap and gives the player a reason to prepare without accepting the prediction as true.

### The focus content needs a shared emergency branch, not replacement trees

Doomsday administrations require their own political play. Full new trees for every transformed country would be generic and impossible to maintain.

The final design uses an 18 to 24 focus shared emergency branch with country-specific text, targets, and AI behavior. Existing national content remains where it still makes sense. Offensive and long-horizon content can be blocked or bypassed only after the country has surrendered those institutions.

## Expansion rejected as bloat

The following ideas were considered and excluded:

- A third public value for country legitimacy
- Separate visible meters for every society current
- A world map of prophecy nodes
- A dedicated event-owned scripted GUI
- A separate country tag for every Doomsday administration
- A normal military faction for the Final Assembly
- A custom 3D unit or building
- A repeatable sequence of revised doomsday dates
- A third evolution based only on more severe numerical penalties
- A super-event for the failed date where nothing visible occurs

## Remaining design risk

The shared emergency focus branch can become generic if implementation uses identical names, targets, and rewards across every country. The focus prompt requires country and movement-current adaptation.

The global Conviction formula can become dominated by populous majors. The probability scenarios require bounded country weights and tests for minor-country influence.

The suppression route can become a simple optimal choice if hidden backlash, deaths, Condemnation, and post-date legitimacy costs are too weak. The decision and probability audits must compare short-term control with long-term outcomes.

## Closure judgment

Broad design expansion is not recommended before implementation. The event already has a complete opening, country loop, war loop, institutional loop, two evolutions, a political transformation package, a shared focus branch, a terminal route, a failed-date aftermath, cross-system integration, AI direction, presentation, assets, achievements, and acceptance tests.

Further planning should be driven by implementation findings or the required `chaosx_improvement_loop_planner` pass. Adding more visible mechanics at this stage would likely reduce clarity.
