# Event 018 Resources Found, Part 6 UI, Scripted System Handoff, Validation, and Spreadsheet Direction

All names are working labels only. They are not final localisation.

## Resource field ledger UI

The resource field ledger is a recommended scripted GUI or category-attached display. It should exist if the implementation can support it cleanly. If the final implementation uses only decision category text, it must still present the same values with scripted localisation.

The ledger should answer five player questions:

1. Which state is the field in?
2. What resources and how much field richness exist there?
3. How hard is the site being exploited?
4. Who is interested in the field?
5. How close is the site to public disaster or closure?

## Ledger layout

Suggested panel areas:

| Panel area | Content |
| --- | --- |
| Header | state name, owner flag, dominant resource icon, field stage seal |
| Resource strip | resource icons and field richness summary |
| Pressure block | extraction pressure, worker safety, local dependence |
| Diplomacy block | foreign interest, active concession, border crisis actor if any |
| Safety block | sickness status, public panic after public danger, evacuation status |
| Action cards | survey, extraction, trade, security, safety, closure, emergency |
| Warning frame | appears when public danger or breach countdown is active |
| Footer | active missions and last field event direction |

The UI should avoid showing hidden below pressure as an exact number early. After sickness appears, it can show a vague dangerous-depth status or a staged warning.

## Button state plan

| Button or card | Available state | Locked state | Warning state | Completed or obsolete state |
| --- | --- | --- | --- | --- |
| Survey | state valid and field open | no field or closed | deep survey raises danger | survey confidence high |
| Extraction | resources can expand | closed or public emergency | high pressure or low safety | max safe surface extraction |
| Concessions | foreign actor valid | no eligible actor | concession dominance rising | concession balanced or cancelled |
| Security | owner can secure field | demilitarized rules block | border crisis rising | crisis resolved |
| Safety | field open | closed or no workers | sickness active | safety stabilized |
| Evacuation | public danger active | no public danger | attack timer active | evacuation completed |
| Hunt | public danger and units present | missing units or equipment | failure risk high | temporary hunt cooldown |
| Closure | field open | breach completed | last chance stage | sealed |

Every button requires tooltip direction, blocked requirement text, effect text, and AI equivalent.

## Animated UI handoff

| Asset | Trigger state | Expected behavior | Static fallback |
| --- | --- | --- | --- |
| Field stage seal | field stage changes | seal changes from clean resource mark to cracked dangerous mark | current stage seal |
| Pressure warning | extraction pressure high | warning frame pulses from real source frames | static warning frame |
| Public panic card | public danger active | card border flickers or trembles | static panic card |
| Closure seal | closure available or last chance | seal tightens or fractures by state | static closure seal |
| Breach warning | breach countdown active | fissure widening loop | static fissure |
| Cave Host portrait | Host active | nonhuman breathing, eye glow, or stone dust | static portrait |

Use `chaos-redux-frame-animation`. Do not build final animations from transforms, glow filters, or a GIF.

## Scripted system architect handoff

The implementation should use `chaosx_scripted_system_architect` before duplicating logic.

Reusable helper needs:

| Helper role | Scope | Inputs | Outputs | Side effects |
| --- | --- | --- | --- | --- |
| Select valid resource state | global or country | eligible owners, excluded tags, field rules | selected state target | saves field state target |
| Roll resource type | state or global | random roll, evolution tier | resource type id | sets resource type context |
| Add event resource deposit | state | resource type, amount, evolution tier | added resource | stores event-added amount if possible |
| Remove event resources | state | stored field amounts | removed resource | closure cleanup |
| Refresh field values | owner or state | state, owner, decisions taken | richness, pressure, safety, interest | updates scripted localisation values |
| Transfer field on state transfer | state | old owner, new owner | new owner context | moves decisions and flags |
| Mark primary deep site | state | field state | global primary target | prevents duplicate deep sites |
| Clear primary deep site | global | closure, defeat, invalid state | no active primary site | clears decisions and events |
| Calculate Cave Host origin score | state | field values | initial division count | stores origin contribution |
| Refresh Cave Host capacity | Cave Host country | controlled resource states | future capacity and spawn queue | adds or decays divisions |
| Register world threat | global | Cave Host exists and threat state | source flag | refreshes world threat aggregate |
| Cleanup Cave Host defeat | global and states | Host defeated | cleared threat, sealed states | removes stale decisions |

## Field memory

The implementation should store enough state memory to remove event-added resources when the field closes. If exact per-resource cleanup is not feasible in the engine, implementation must design a transparent alternative and report it. Preferred memory:

- field state target
- owner at discovery
- current owner
- resource type roll history
- event-added amount by resource type
- field richness
- field stage
- primary deep site flag
- active foreign actor
- concession state
- closure status
- Cave Host origin score if breach happens

Do not rely only on event text or national spirits to remember field state.

## Cave Host capacity refresh

Capacity should refresh on meaningful events rather than uncontrolled daily world iteration. Preferred triggers:

- Cave Host gains control of a state
- Cave Host loses control of a state
- monthly pulse limited to Cave Host if it exists
- Cave Host focus or decision changes spawn method
- world-end branch fires

The refresh should compute non-origin state capacity from total controlled resources. Every 10 total resources equals one division, capped at 10 per state. The origin starting army is stored separately.

If excess divisions exist after losing resource states, use a decay or penalty model rather than confusing instant deletion, unless local precedent supports clean deletion.

## Spreadsheet handoff direction

The workbook should be updated only after final in-game wording exists. The current direction for future spreadsheet fields is:

| Field | Direction |
| --- | --- |
| Details | A surprising resource discovery gives a state a large new deposit, opens exploitation and trade decisions, and can draw foreign interest. Do not list exact effects. |
| Evo I | Discovery becomes richer and more politically important, with larger deposits, concessions, border pressure, and possible demilitarized field demands. |
| Evo II | Unsafe deep extraction causes worker sickness, population loss, and strange underground incidents. |
| Evo III | The site becomes publicly dangerous, with attacks, evacuation, hunts, and a final chance to close the field by sacrificing its resources. |
| Evo IV | An aggressive nonhuman Cave Host appears from the site, uses captured resources to create armored slow divisions, and attacks neighbours. |
| World-end | If the Cave Host consumes enough of a continent at chaos over 1000, stronger hosts begin appearing on other continents. |
| Cluster | Economy positive, medium severity. |

These are directions, not final spreadsheet text.

## Validation scenario matrix

| Scenario | Required result |
| --- | --- |
| Baseline ordinary firing | one valid state gains around 100 of one random resource, owner popup appears, field category opens |
| Repeat ordinary firing | another ordinary field can exist without duplicating primary deep site |
| Owner change | field follows state and new owner sees valid decisions |
| Trade diplomacy | resource-deficit country can receive concession or interest action |
| Border crisis | eligible border rival can escalate and valid loss transfers state |
| Demilitarized field | Evolution I pressure can create commission path without blocking later public emergency response |
| Sickness stage | worker safety decisions affect deaths and population loss |
| Public danger closure | owner can close site before Evolution IV, event-added resources are removed |
| Failed closure | breach can happen if public danger and below pressure remain too high |
| Cave Host spawn | origin state transfers, wars fire, initial divisions cap around 30 |
| Cave Host capacity | non-origin resource states spawn divisions by 10 resources per division, capped 10 per state |
| Cave Host loss of resource state | capacity falls and excess divisions decay or receive designed handling |
| Cave Host defeat | threat source clears, origin sealing and aftermath logic run |
| World-end | Cave Host continent threshold at chaos over 1000 fires terminal branch and super-event |
| Asset coverage | no missing icons, portraits, flags, report images, super-event images, or animation fallbacks |
| Localisation | no working labels or research gates appear as final text |
| Spreadsheet | workbook mirrors final in-game detail wording after implementation |

## Documentation outputs

Implementation should update:

- event doc under `docs/events/`
- event spec disposition if plans are promoted
- asset manifests under `docs/assets/018_resources_found/`
- super-event research note under `docs/super_events/`
- dynamic helper documentation if helpers are added
- country package docs for Cave Host
- event catalog workbook after final text
- subagent handoffs under `docs/plans/018_resources_found_plans/subagent_handoffs/`
- completion report with simplifications, blockers, and validation results

## Completion risk notes

The implementation is not complete if:

- ordinary discovery works but decision category is passive or shallow
- cave monsters use normal manpower or equipment
- Cave Host has no focus tree or only a one-line tree
- the resource capacity rule is approximated without disclosure
- closure cannot remove event-added resources
- super-event audio is placeholder or undocumented
- generated animations are transform-only
- final text contains working labels
- spreadsheet stays stale
- no improvement-loop pass was run near completion
