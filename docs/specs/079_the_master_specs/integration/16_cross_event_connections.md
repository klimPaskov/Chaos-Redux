# 16. Connections to other Chaos Redux events

## Connection policy

Most connections work by reading the actual world state already changed by another event. A country joining a faction, changing ideology, receiving industry, or becoming independent naturally changes Event 79's choices. This does not require a bespoke bonus for every event ID.

The following connections use the supplied catalog and the current user brief as design context. They are not claims that every other event already exposes a production API. An explicit adapter must be inspected before a direct cross-event call is implemented.

| Connected system | Meaningful interaction | Boundary |
| --- | --- | --- |
| Black Friday, Event 26 | Supported administrative costs can be quoted through the universal cost framework | Do not discount physical donations into free equipment or guess factory-day handling |
| Parliament of Fear, Event 77 | Foreign sponsors can seek influence over an existing chamber or support a threatened bloc | Chamber ownership, purge rules, and protected leadership remain with Event 77. Without a public adapter, use ordinary ideology-level campaigns |
| Subjects Break Free, Event 63 | A former Event 79 client can become independent through the existing independence event | No permanent Event 79 re-puppeting immunity. New selection requires actual independence and the 180-day cooldown |
| Industrial Boom and Great Depression, Events 34 and 35 | Real industrial growth or collapse changes usable factories, project value, and donor affordability | Do not invent a second economic health meter. Factory commitments pause if capacity is genuinely lost |
| Riches Found, Event 29 | Additional real industry or resources can make a target strategically valuable | Read actual outputs. No arbitrary +20 Influence for being present when riches appeared |
| Intel Leaked, Event 52 | Verified exposed campaign evidence can enable a rival's exposure operation | Existing leaked-information owner must publish a precise target and operation record. A generic leak flag is not unlimited proof |
| Existing faction and diplomacy events | New factions, guarantees, hostility, and peace alter entry conditions and legal action paths | Recalculate future action conditions. Never reseed an existing score whenever a diplomatic relation changes |
| Collaboration Everywhere, Event 97 | Existing documented political or administrative penetration can inform a valid prior-influence provider | Collaboration or compliance is not automatically equivalent to sovereignty or mastership |
| Government-changing events, including The Peace Movement, Event 84 | A completed governing transfer changes the political recipient and future action compatibility | The political owner resolves its constitution and command; Event 79 preserves the race and revalidates pending actions |

## Parliament of Fear detail

A foreign sponsor can fund a bloc represented by Event 77 only if the target's chamber owner provides a supported relation between that bloc and a political recipient. Event 79 records the funded sponsor relationship but does not manipulate seat totals, remove paranoia, cancel investigations, or grant arbitrary ministers.

If an Event 77 leadership challenge and an Event 79 leadership action are both pending, the chamber owner resolves its own transition first. The Event 79 action revalidates its recipient and follows its normal cancellation or adaptation rule. Neither system can write an obsolete leader snapshot over the other's legitimate result.

## Constitutional authority and tax liability

A target with an active Peace Movement convention keeps that convention, its organizations, and its legal reforms during an Influence race. A sponsor can support an owner-recognized political recipient through the existing government or opposition family; ordinary propaganda does not directly add Peace Movement Influence or Traditionalist Reaction. If Event 84 completes a governing transfer while a sponsor's leadership action is pending, the constitutional owner resolves first and the sponsor revalidates its saved recipient under Parts 03 and 06. A valid takeover at 100 then preserves the resulting government under Part 08. Becoming a subject restricts the target's later sovereign bloc commitments without erasing its domestic settlement. AI sponsors exclude an invalid leadership action and compare their remaining valid campaigns, using the same recipient rules as humans. See [Event 84 government authority](../../084_the_peace_movement_specs/084_the_peace_movement_spec_part_6_governments_and_country_packages.md).

If British Tax is active, confirmed puppeting also changes the target's resistance permissions. Event 81, not the contest, reconciles that liability after the actual subject relation exists: an ENG winner invokes the British-dependent schedule, and another winner invokes the non-British-dependent schedule. The target cannot finish a sovereign tax reform from a stale pre-takeover condition. Delivered Event 79 investments remain real industry in the next assessment, with no automatic tax exemption or extra Influence for collecting tax. If the tax event is absent, the normal takeover and project settlement proceed unchanged. See [Event 81 relationship changes](../../081_british_tax_specs/081_british_tax_spec_part_1_core.md#new-countries-and-changing-relationships).

## Independence and subsequent spheres

Winning a race creates a normal client that can be affected by later independence, war, peace, or annexation mechanics. A sponsor building a sphere must preserve its subjects through actual game conditions. Event 79's completed influence contest does not become a permanent hidden loyalty rule.

A released target's later race starts from current politics and current relationships. Existing delivered factories remain physical facts. They do not restore the former sponsor's old 100 Influence. The former sponsor may qualify for a normal bounded economic-connection contribution, like any other country with an evidenced continuing connection.

## Unavailable adapters

Mark an unimplemented direct connection as awaiting an owner contract. Keep the baseline contest functional through real native state. Do not create fake APIs, generic political-lock overrides, or unconditional cross-event rewards merely to make the specification look connected.
