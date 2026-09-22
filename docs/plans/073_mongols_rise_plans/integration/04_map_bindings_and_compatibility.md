# Map bindings, country identities, and compatibility

## Semantic region registry

No numeric state or province IDs are invented in this package. Bind these semantic sets against the installed game and current mod during implementation. Each binding needs a provenance path, inspected map version, named required set, optional set, ownership predicate, and actual geometry output.

| Binding | Intended content | Qualification distinction |
|---|---|---|
| R01 Mongolian homeland | Existing valid Mongolia and reviewed adjacent union territory | Direct integration eligibility is narrower than historical imperial claims |
| R02 Karakorum site | Actual historical site within the installed state and province map | Command-center state and precise capital relocation must be distinguished |
| R03 Northern Chinese approach | Viable frontier, transport anchors, Beijing objective | Military occupation differs from final regional ownership |
| R04 Central Asian corridor | Reviewed northern and southern approach variants | Access, ownership, and actual transport continuity are separate |
| R05 Northern frontier | Limited Siberian corridor and optional deeper objectives | Limited success must not require annexing the whole opposing state |
| R06 Western steppe | Viable Golden Horde settlement and eastern connection | A coherent country needs a valid owned capital |
| R07 Persian settlement | Current Persian identity, northern approach and regional center | Event 071 and existing identities take precedence over duplicate tags |
| R08 European foothold | Reachable eastern, Balkan, or central direction | One current campaign set, no continent-wide blanket requirement |
| R09 Deeper China | Current Chinese settlements beyond the first northern campaign | Existing country rights and occupations remain distinct |
| R10 Korea | Current peninsula owner and actual approach | No implied right from a Chinese settlement |
| R11 Indian frontier | Viable Central Asian or Persian approach and foothold | The actual sovereign and protecting powers must be targeted |
| R12 Southeast Asian approach | Viable land or maritime approach and limited objective | Jungle and port requirements remain real |

A future implementation must fill every required binding before the affected route is advertised as functional. Native map extraction supplies puzzle geometry. A semantic label is not a completed map audit.

## Identity inventory

Inspect vanilla, Chaos Redux, installed Workshop mods, and other local mods for existing tags, cosmetic identities, relevant characters, and country packages. Reuse an appropriate identity where possible. A new tag needs a complete country package and collision proof.

The uploaded files do not contain that local inventory. No four new tags are preallocated here. Golden Horde, Chagatai, Ilkhanate, and Yuan-style administration are design identities awaiting that review.

## Interaction matrix

| Existing event or system | Evidence basis | Required behavior |
|---|---|---|
| 005 Soviet Union Collapse | Uploaded catalog describes republic and succession systems | Reuse actual successor countries, do not reconstruct the old Soviet owner |
| 006 Independence Wave | Uploaded catalog describes new countries and institutions | Reuse current country identities and legitimate institutions |
| 009 White Peace | Uploaded catalog describes peace and border restoration | Revalidate campaign ownership and agreements, do not immediately force the same war back on |
| 060 Research Failure | Uploaded catalog records research regression | Respect lost technology, revalidate support availability, do not silently restore everything |
| 064 Border fortifications | Catalog title is relevant but its detail text is inconsistent | Rely on actual forts in the runtime map, do not assume a completed rework |
| 069 Boxer Rebellion | Uploaded catalog records a Chinese rebellion | Treat an existing rebellion as a real actor or situation, no invented shared hook |
| 071 Persia | Uploaded catalog records a Persian restoration | Avoid duplicate Persian identity and incompatible tree replacement |
| 096 Divisions lock | Uploaded catalog describes unavailable templates | Respect the actual current lock mechanism and queue a safe conversion when legal |
| Population, famine and migration | Uploaded mechanics | Keep Mongolia and regional populations in ordinary human accounting |
| Chemical and biological warfare | Uploaded mechanics | No immunity, no custom offensive weapons added by this event |
| Shared war and Chaos systems | Uploaded mechanics | Reuse existing legal war, peace, and instability accounting |

The earlier project discussion calls Event 066 Abundance, while this uploaded catalog still calls it CIC. No bespoke 066 integration is asserted. The event can respond to actual stockpile changes through its normal resource checks without guessing the status of another rework.

## Compatibility gates

Cavalry-category effects and recruitment controls, capital relocation, resource tribute, custom mounted model selection audio, and current DLC-dependent country relationships all require exact local verification. Unsupported features must return a narrow blocker and an explicit proposed alternative. They cannot be silently weakened while retaining the original promise in the interface.
