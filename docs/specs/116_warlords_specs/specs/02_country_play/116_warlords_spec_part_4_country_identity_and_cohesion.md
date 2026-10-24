# Part 4: A complete warlord country

The new state must be a country the player can govern for the rest of the campaign. Its identity, economy, armed forces, diplomacy, research, and succession all need to work after the opening emergency has passed.

## Country identity and origin

Choose a country carrier only after checking its actual history, living actors, and collisions. An appropriate dormant vanilla identity may be reused when it represents the same regional polity. An existing independent 019 derivative remains its existing country. A tag appearing in the Independence Wave registry does not authorize the 006 setup package. A newly reserved dynamic carrier needs a proved creation path and a complete country definition.

Use a readable territorial country identity with the general's personal rule conveyed through politics, leader presentation, and flag direction. Do not name a durable country after an administrative office. Preserve a genuine regional name when one applies. A wholly new personal military state may use a grounded regional identity until a later earned political transformation. Supreme War State is the fixed special identity of the Generalissimo formation, not the default name of every successful warlord.

Track the actual origin parent, founding region, founder, creation owner, current leader, and persistent political lineage separately. Tags can change and actors can survive defeat. These facts must not be reconstructed from a current country name or cosmetic flag.

## Country package obligations

| Surface | Required behavior at birth and afterward |
| --- | --- |
| Capital and territory | Valid owned and controlled capital, ranked backup capitals, exact inherited damage and infrastructure, coherent original region |
| Political identity | Noun, definite form, adjective, appropriate ruling ideology, valid party distribution totaling 100 percent, regional identity history |
| Leader and commanders | The actual founder in valid ruler and commander roles, current portrait, existing traits, no duplicate character, real successor handling |
| Research | Inherit compatible knowledge actually known to the parent, valid research slots and AI priorities appropriate to its capacity |
| Economy | Actual factories, production capability, resources, trade access, repairs, construction, consumer-goods burden, and sustainable deficits |
| Laws | Law choices supported by population, war status, industry, and native prerequisites, without free escalation to the strongest laws |
| Army | Exact opening manifest, normal templates, training, replenishment, doctrine compatibility, equipment definitions, and supply |
| Air and navy | Exact conditional service package or an explicit absence of inherited assets, with lawful later development |
| Diplomacy | Actual wars, recognized borders and claims, sponsor contracts, subjects, military access, factions, and existing obligations |
| Country content | Warlord focus architecture or compatible additive content, decisions, limited ideas, AI, achievements, and defeat paths |
| Presentation | Correct flag sizes and identities, leader and ideology display, country color contrast, source-aware notifications |
| Persistence | Save/load identity, succession, annexation, liberation, defeat, and ownership-aware cleanup |

Start with the parent military's applicable technology and a modest civilian research capacity. The state's size and retained institutions determine how many slots it can sustain. It can earn additional capacity through actual development. Never copy an entire national focus completion history, off-map factory grants, inaccessible national characters, or exclusive foreign content as a shortcut.

A persistent civil administration exists even under a personal ruler. Essential supply and production must operate without purchasing a repeated survival decision every month. Administrative reform changes efficiency and political options. It does not toggle the country's ability to exist.

## Command Cohesion

Command Cohesion is the sole new public persistent value type. It describes whether the regime's commands can act together under current political and material conditions. It ranges from 0 to 100. A typical new state starts between 35 and 65, based on founder ability, the unity of its actual military constituency, stock and supply conditions, local acceptance, and conflicting obligations.

When 067 owns the country after takeover, use its Command Cohesion through the owner interface. 116 submits causes and consumes the acknowledged value. It does not create another meter with the same name or silently replace the Generalissimo's mechanics. 067's pre-takeover Influence belongs to that phase and remains separately owned.

Before a 067 takeover, 116 owns the warlord country's one value and all its mutations. An accepted owner handover freezes the actual country, current amount, pending cause receipts, and history, then transfers authority to 067 without refreshing the amount or displaying both stores. If 067 already owns the active post-takeover value when 116 encounters the country, use that existing amount from the outset. A later lawful 067 departure can return the same current value to 116 only after 067 acknowledges closure of its authority. A civilian transition retires the active warlord display while retaining history. No ownership transition is implemented until the shared interface is accepted and verified.

| Cohesion condition | Consequence and player response |
| --- | --- |
| High, roughly 75 to 100 | Commands cooperate reliably, staff reform and difficult joint campaigns are easier to sustain |
| Functional, roughly 45 to 74 | The regime can operate normally, with shortages and political choices still consequential |
| Strained, roughly 20 to 44 | Coordination penalties, more costly integration, and visible risk around dissatisfied commands |
| Fractured, below roughly 20 | Severe command friction, credible successor or defection pressures, and urgent need to settle obligations or change policy |

These bands are proposed tuning. Cohesion affects limited coordination and administrative modifiers, AI willingness, and eligible political pressures. It does not kill units, change ownership, compel an annexation, or decide a battle. An actual new defection still needs a living general, a viable region, and real forces.

## Causes, improvement, and decline

Improve cohesion by securing supply, making a successful realistic military plan, paying a defined material obligation, integrating a rival's real staff under an agreed command, or completing a credible civil settlement. Merely clicking a congratulatory button is not a cause. One conquest receipt can improve cohesion once, with diminishing political benefit from repeated small captures.

Reduce cohesion after a major encirclement, a genuine supply collapse, contradictory sponsor demands, abuse of local authority, broken promised autonomy, or a rival's successful departure. Consequences are scaled to the affected force or population. Losing an empty border province should not equal losing the capital and the only working rail junction.

Use callbacks and bounded active-country refreshes. A proposed periodic update may process registered material obligations and summarize persistent unresolved pressure. Do not implement it through `on_daily`, `on_weekly`, or `on_monthly` without explicit user authorization, because those hooks iterate over all countries by default. Prefer owner callbacks or a specifically authorized bounded active-record dispatcher. It must not apply an inexorable penalty simply because the player did not press a monthly upkeep button; if a recurring world-wide pass is indispensable, leave that requirement unresolved pending explicit authorization. Stable, supplied countries with settled obligations can maintain cohesion without repetitive interaction.

At zero cohesion, a country without a viable separatist command suffers command disruption and political crisis. It does not spawn a free successor. Leadership replacement, negotiated decentralization, or actual military defeat may be the honest resolution.

## Political evolution and succession

The founder can preserve personal rule, build an officer-state constitution, govern through a regional civilian compact, or prepare a genuine civilian handover. These routes change authority, recruitment bargains, diplomacy, focus access, and succession. They share an economy and real military, so switching routes cannot refresh the same starting grants.

If the founder dies, retires, is captured, or loses office, keep the country's actual territory, forces, obligations, and population. Promote an eligible real officer under the chosen succession system, or establish an institutional regency while a lawful successor is resolved. A people-free institutional emblem may represent a council. Do not invent a replacement historical person or resurrect the founder through a portrait profile.

A personal retinue without a clear successor creates a sharper succession crisis. An institutional staff provides continuity but can resist the founder's private demands. A civilian compact can survive leadership change if its negotiated terms remain real. A successful civilian transition removes the personal military regime's active bonuses and pressures while preserving the country's achievements and ordinary armed forces under the new settlement.

## Country idea discipline

The package uses at most three simultaneous focus-created national spirits per country. The intended slots are a command constitution, a military-economic organization, and a temporary reconstruction or integration condition. Upgrades replace or transform the relevant spirit. They do not add permanent parallel copies.

Event birth modifiers and 067 or 019 owner ideas must also be audited for total balance and readable display. The focus limit is not permission to hide dozens of non-focus spirits. Persistent facts belong in the country history or factual roster when they do not need a continuous modifier.

## DLC and foreign content

The complete core campaign works without DLC: breakaway, warfare, recruitment, viable economy, choices, unification, resistance, terminal progression, and aftermath. Intelligence operations, MIOs, specialized service features, or other DLC-only flavor can enrich a route when actually available. They cannot be the only way to expose a defector, acquire weapons, control an army, negotiate a settlement, or break the military order.

Preserve a living country's meaningful national or 019 focus content. Add an approved shared branch where technically supported. If a tree cannot accept an additive branch safely, provide the same required progression through ordinary decisions with an explicit route-equivalence map. This is a designed compatibility path, not permission to omit the industrial, diplomatic, political, or succession route.
