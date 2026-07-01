# Event 015 targeting matrix

## Current catalog observation

The provided catalog CSV has ID 15 as `World Tension Subsides`, Details `Reserved`, Type `Minor Repeatable`, and Status `To Be Reworked`. This spec replaces that identity with `utopia_manifesto` and changes intended type to Minor Fire-Once.

## Hard blocks

| Check | Block condition | Reason |
| --- | --- | --- |
| Major status | country is a major | user requested no major or strong target |
| Industrial strength | total factories above tuned cap | prevents rich countries from receiving full replacement tree |
| Military industry | military factories above tuned cap | prevents strong powers and war economies |
| Naval industry | dockyards above tuned cap | prevents naval majors and strong island powers |
| Army strength | divisions above tuned cap | prevents large military countries |
| Special country | shared Chaos Redux special or nonhuman trigger | avoids invalid interactions |
| Terminal state | world-end already active | no normal minor event after terminal state |
| Existing Utopia state | accepted or rejected already | fire-once behavior |
| Focus tree conflict | protected event-created tree active | avoids blind replacement of another event package |
| Invalid map state | no capital, no controlled state, or near capitulation | avoids dead-on-arrival target |

## Tuned thresholds

Initial constants to test:

| Constant concept | Suggested value |
| --- | --- |
| total factory hard cap | 45 |
| military factory hard cap | 25 |
| dockyard hard cap | 18 |
| controlled state hard cap | 18 |
| division hard cap | 70 |
| one-state minor factory soft cap | 12 |
| subject extra tolerance | plus 5 total factories if stable |
| high-chaos target tolerance | no extra major tolerance, only slightly higher Need at opening |

## Weight modifiers

| Trait | Weight direction |
| --- | --- |
| generic focus tree | strong increase |
| coastal or island | increase |
| landlocked with rail or defensible capital | moderate increase |
| subject but stable | moderate increase |
| player country and eligible | strong increase if random event can target player |
| at defensive war | small increase if not close to capitulation |
| at offensive war | decrease |
| high stability | small increase for peaceful route viability |
| very low stability | decrease unless high chaos |
| low industry but at least one factory | increase |
| no manpower and no industry | decrease |
| adjacent to many majors | decrease for AI, not hard block |
| existing unique national tree | decrease sharply for AI |

## AI selection notes

- AI acceptance is automatic after target selection.
- If a random country would be funny but unplayable, do not select it.
- A strong player country should not receive the event automatically.
- Manual debug firing can bypass for testing only, but normal selection and event log availability should report invalid targets as `N/A`.

