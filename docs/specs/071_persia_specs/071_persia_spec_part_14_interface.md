# 071 Persia: interface and information design

## Entry point

Event 071 adds one event-owned decision category with a compact native scripted GUI attached to it. The entry point is available to the Persian player after the root event. The opening news does not require the player to discover the category through an unrelated menu.

The primary view explains the current restoration stage, the next meaningful action, and the active political or military problem. It must not become a separate full-screen management application. Ordinary decisions and missions remain native and readable.

## Public value budget

There is one main public meter, imperial legitimacy. The guard panel also shows authorized guard manpower as used capacity versus maximum capacity. This is a second persistent custom numerical reading because the player must use it to plan recruitment, even if it is displayed through a native unit-family surface.

No other persistent custom numerical value is exposed. Satrapy relationships use qualitative status and reasons. Administrative reach is expressed through actual regional settlements and connections. The opening grant is a one-time transaction report. Mission days, ordinary resources, army strength, and normal game values retain their ordinary presentation.

Do not hide a loyalty number behind a color and still require the player to manage undocumented thresholds. The visible status must explain the concrete cause and available remedy. Supporting AI and simulation values remain internal.

## Layout regions

The top area contains the current political route, the legitimacy value and band, and a short situation statement. The center contains a tab or compact selector for restoration regions, satrapies, guards, and active projects. The bottom area remains the normal decision and mission list.

The region view contains the exact-state restoration puzzle and its legend. Selecting a region changes the adjacent explanation and available actions. The satrapy view shows a selected subject, its charter, status, current obligation, and the reason for any dispute. The guard view shows capacity, unlocked families, and eligible training or conversion actions. The project view summarizes the current mission objectives.

Keep normal event log, settings, and super-event systems outside this GUI. This event owns its category and attached window. It does not redesign shared project interfaces.

## Territorial puzzle

The puzzle uses exact native state geometry derived from the installed game map. It must not be drawn from a modern map or an approximate generated silhouette. A diagram in this planning package is not a substitute for this map.

Grey indicates an unmet region and green a region meeting the selected condition. Patterns or clear icons distinguish direct settlement, a valid satrapy, temporary occupation, and an inaccessible connection. Color alone must not carry the distinction.

The selected state tooltip shows its region, current owner, controller, settlement requirement, and the reason it does or does not count. A region's completion rule is shared with its decisions, focus requirements, and achievements. The map cannot show green while the corresponding focus remains unavailable for an unexplained different condition.

The player can switch between homeland, imperial heartlands, and the selected greater-claim project. Do not show every possible outer claim at once in a small unreadable map. The active project should be visually distinct from other unlocked ambitions.

## Subject selection

The human player selects one relevant subject or partner at a time. The list sorts active disputes and unfinished obligations first, then stable subjects. It distinguishes satrapies from ordinary treaty partners and clients.

A selected subject that disappears, changes allegiance, or becomes ineligible clears or updates the selection safely. No action may retain a stale target from the previous subject. AI selection evaluates all valid targets, not only the player's current selection.

A subject card shows its actual government and identity. It does not require a fictional portrait for every charter type. Any character portrait used must follow the portrait workflow.

## Guard information

The guard panel shows used manpower, reserved training manpower, and the capacity ceiling as one capacity reading. Its tooltip explains the opening floor, the current institutional floor, and any regular-army share calculation. The player must understand why recruitment is unavailable.

A family card shows its role, equipment requirements, training route, and conventional weaknesses. It does not present unsupported exact combat predictions. Available conversion actions name the existing formation they will change.

The panel should make the difference between units already granted and units still in training obvious. A reserve of equipment is not shown as a deployed division.

## Mission feedback

Each mission has a clear objective list with completed and unfinished items. The tooltip states costs already paid, current commitments, the next available action, and the consequences of expiry. It distinguishes pause, partial success, and failure.

A site project displays which stage is complete. A charter hearing displays the actual disputed obligation. A central recovery mission names the current administrative center. Repeated generic progress bars with no explanation are not acceptable.

## Visual treatment

Use the established HOI4 and Chaos Redux visual language. Native buttons, frames, lists, text, icons, and tooltips must remain separate functional elements. A generated image of a menu cannot become a flattened replacement for the actual interface.

This rich category contains a map, a meter, custom selectors, and detail panels. It must not also display a large decorative category picture beside those controls. A simple separate ordinary category can use a picture only if it has a genuinely different purpose and follows the reference rules. This plan does not require such an extra category.

Static assets are sufficient. Animation is not added merely because the frame-animation skill was supplied. Any later animation must have a static fallback, a clear gameplay purpose, and a bounded asset plan.

## Reference and native implementation gate

Before native implementation, create and review GUI reference images for the specified layout. Record parent acceptance within the task's authorized scope. This package provides layout direction, not an approved in-game mockup. No reference image or MCP render has been produced in this planning session.

Map each accepted visual region to native elements. Record required adaptations where the engine cannot match a reference exactly. The implementation must inspect the existing GUI, render the full state matrix, and compare the implemented result. Direct reviewed edits are permitted under the supplied GUI skill. Automatic rewrite tooling is not a substitute for visual acceptance.

## Required view matrix

| Scenario | Required visible result |
|---|---|
| 1920 by 1080, standard scale | Main category, selected region, normal mission list, no overlap |
| 1366 by 768, standard scale | Usable scroll or compact behavior, no inaccessible core action |
| 2560 by 1440, standard scale | Stable alignment and readable hierarchy |
| 1920 by 1080, enlarged supported UI scale | No clipped meter, cost, or subject name |
| Remnant Iran at baseline | Recovery priority and actual grant report |
| Evolution III with many subjects | Stable selection and bounded list, not every control expanded |
| No valid satrapies | Useful empty state and route to create one |
| Guard capacity full | Clear capacity reason and no active duplicate recruitment |
| Lost selected subject | Selection cleared or revised without a wrong-target action |
| Multiple active crises | Prioritized situation and no contradictory mission choices |
| Locked or unsupported action | Specific reason, no apparently clickable dead control |

The exact supported UI scale values must be taken from the installed game. The listed resolutions are planning acceptance targets, not evidence that a render has passed.

## Ownership boundary

The future event UI worker owns only Event 071 category and GUI surfaces, their event-specific assets and localisation, and the related review report. Shared event log, event details, settings, super-event framework, and registries remain outside that worker's write scope. Coordination occurs through the coding lead's handoff.
