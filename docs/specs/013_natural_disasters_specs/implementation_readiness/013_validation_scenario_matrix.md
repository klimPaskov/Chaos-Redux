# Event 013 Natural Disasters, validation scenario matrix

This matrix defines meaningful checks for the implementation pass. It is not a request for the user to validate the mod. It is a handoff for the coding agent and audit agents.

## Baseline sequence checks

| Scenario | Setup | Expected result | Failure to catch |
| --- | --- | --- | --- |
| Single baseline disaster | Force one baseline Event 013 firing against a valid country and state. | One history row appears, one impact resolves after the designed delay, report follows, aftermath notification appears. | Extra history rows, missing report, silent category, invalid target loss. |
| Direct family call | Call a specific ordinary family with a chosen target country and state. | The requested family, target, severity, and policy package are honored. | Random family override, copied logic path, missing caller policy. |
| Random family call | Call random valid family under baseline rules. | Family pool is baseline-eligible and target scoring selects a meaningful state. | Evolution-only family appears too early or target is irrelevant. |
| Delay compression | Fire a sequence with several disasters. | Disasters remain delayed, with compression only as sequence pressure rises. | Same-day burst or no pacing change. |
| News early throttle | Fire several small baseline hits. | Early meaningful hits can show family-specific news, later minor hits throttle. | News spam or no specific news for meaningful first hits. |

## Deaths and damage checks

| Scenario | Setup | Expected result | Failure to catch |
| --- | --- | --- | --- |
| Dense state impact | Hit a dense state with a population-sensitive family. | Deaths-system entry reflects significant local loss and dense-state absolute losses matter. | Decorative loss values or population reduction without Deaths log. |
| Sparse state impact | Hit a sparse state with same severity family. | Loss rate can be comparable, but absolute deaths differ from dense state. | Flat deaths unrelated to population. |
| Weak infrastructure | Hit a low-infrastructure or damaged-supply state in Evolution II. | Deaths, damage, and aftermath pressure increase where family identity supports it. | Evolution II ignores vulnerability factors. |
| Prepared state | Apply warning preparation before impact. | Prepared state takes lower relevant losses without negating the disaster. | Warning decisions do nothing or fully cancel danger. |
| Severe abnormal impact | Force an Evolution III abnormal family at high severity. | Buildings and population suffer massive losses when family identity supports it. | Abnormal family only adds a mild modifier. |

## Report and aftermath checks

| Scenario | Setup | Expected result | Failure to catch |
| --- | --- | --- | --- |
| Affected player country | Player country is hit. | Report arrives after the expected delay and category notification is visible. | Player must notice map damage manually. |
| Affected AI country | AI country is hit. | AI receives recovery route and can clear or reduce aftermath through AI equivalents. | AI never recovers or category logic is human-only. |
| Direct caller aftermath | Another event calls a disaster with aftermath enabled. | Same report and category notification reliability applies. | Direct calls bypass aftermath notification. |
| Aftermath expiry | Let aftermath duration expire without recovery. | Chain or degradation checks run, then stale data is cleaned as designed. | Permanent stale card or no consequence. |
| Country invalidation | Target country is annexed during recovery. | Cards, targets, flags, and missions clean up safely. | Dead target remains in decisions or GUI. |

## Decision and mission checks

| Scenario | Setup | Expected result | Failure to catch |
| --- | --- | --- | --- |
| Early rescue | Trigger a recent serious impact. | Only early rescue actions and urgent missions are visible first. | All recovery actions appear at once. |
| Mission cap | Create several simultaneous aftermath cards. | Active mission cap selects priority tasks and queues or hides lower priority tasks. | Decision wall or duplicate missions. |
| Partial success | Complete a mission with some but not all supporting conditions. | Partial success applies mixed follow-up and communicates the result. | Binary outcome ignores partial state. |
| Foreign relief | Request or receive relief during a serious aftermath. | Relief has costs, route limits, and possible dependency or political tradeoff. | Relief is free or always optimal. |
| AI relief | AI hit by severe disaster with possible donors. | AI requests or accepts relief based on war, ideology, distance, convoys, and severity. | Flat AI behavior or no relief logic. |

## Evolution checks

| Scenario | Setup | Expected result | Failure to catch |
| --- | --- | --- | --- |
| Evolution I opening | Force Event 013 with Evolution I available. | Wider family pool and more active sequence, with only slight severity rise. | Evolution I overuses high-severity damage. |
| Evolution II regional system | Force regional spread family. | Neighboring valid states can take damage and aftermath pressure. | Only anchor state changes. |
| Evolution II chain | Leave aftermath unresolved. | Family-specific follow-up can fire with reasonable delay and one-row sequence rule preserved. | Follow-up creates extra history row or ignores family identity. |
| Evolution III meteor | Force meteor shower. | Abnormal controller, impact queue, report flow, and GUI state update. | Meteor is only a normal event popup. |
| Evolution III corridor | Force moving storm or tornado corridor. | GUI shows path, next regions, current threat, and static fallback. | Path is hidden or only described in text. |
| Whole-earth rupture | Force whole-earth rupture branch. | Branch exists inside Event 013 Evolution III and uses fresh logic. | Event 046 or old Earth Earthquake logic runs. |

## Related event and scenario checks

| Scenario | Setup | Expected result | Failure to catch |
| --- | --- | --- | --- |
| Event 099 bridge | Fire or inspect Event 099. | It is placeholder or calls Event 013 dust and sandstorm helpers narrowly. | Separate sandstorm damage system remains. |
| Event 051 heat active | Activate Heat Wave state and call Event 013 heat. | Event 013 heat blocks, defers, or routes without stacking. | Double heat penalties stack. |
| Disaster Barrage low | Launch low intensity scenario. | Same controller runs a varied local season. | Scenario uses separate bespoke scripts. |
| Disaster Barrage maximum | Launch maximum intensity scenario. | Abnormal access and severe sequence behavior can appear, but no world-end branch starts. | Scenario becomes terminal or ignores intensity. |
| Cluster repeat | Force Natural Disasters cluster at eligible tier. | Multiple Event 013 entries can occur according to cluster rules and one-row sequence behavior. | Cluster treats Event 013 as a single ordinary popup only. |

## Presentation and asset checks

| Scenario | Setup | Expected result | Failure to catch |
| --- | --- | --- | --- |
| Report image path | Trigger a report family that has final art. | Correct report image appears with family tone and no wrong-era or placeholder art. | Missing sprite or placeholder image. |
| News image path | Trigger a meaningful news family. | Correct news image appears with throttled, family-specific news. | Generic image or news spam. |
| Abnormal GUI animation | Open abnormal GUI with animation enabled. | Frame-sheet animation plays and static fallback is available. | GIF, transform-only mockup, or missing fallback. |
| Super-event package | Trigger researched abnormal super-event. | Title, description, button, quote, image, audio, docs, and spreadsheet align. | Unresearched quote, default audio, or mismatched image. |
| Achievement tracking | Complete a difficult achievement route. | Achievement unlocks only when all conditions and disqualifiers are satisfied. | Automatic unlock or missing icon variant. |

## Documentation and audit checks

| Check | Expected result | Failure to catch |
| --- | --- | --- |
| Spec coverage audit | Completion auditor maps each spec demand to implementation or a reported blocker. | Shallow implementation hides missing surfaces. |
| Localisation audit | No missing keys, duplicate keys, raw triggers, process notes, or unresearched research gates in final text. | Prompt fragments enter the game. |
| Docs alignment | Event docs describe implemented behavior and omit old deleted logic. | Documentation contradicts the mod. |
| Spreadsheet alignment | Catalog fields mirror final in-game detail direction after final localisation exists. | Spreadsheet uses stale status or planning text. |
