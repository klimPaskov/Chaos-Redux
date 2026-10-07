# World Claims: frontiers that follow the campaign

## The ownership frontier

Every firing takes a fresh view of the current campaign map. The seed territory is every state owned by the country, including non-core possessions and overseas possessions. A state currently occupied by an enemy remains an owned seed. A state merely controlled by the country, its ally, or its subject is not an owned seed.

A foreign state is a state with another existing owner. A valid land connection is a genuine traversable land border on the active map. Sea routes, straits classified as sea crossings, impassable separators, and geometric corner contacts do not silently count as ordinary land borders. The installed map's adjacency evidence must settle ambiguous connections.

Every qualifying immediate neighbor is included. The baseline is never restricted to one state per neighbor, one random neighbor, a country's historical region, or a maximum number of border states. One country can claim several states owned by the same neighbor.

Countries with several disconnected owned components use all of them. A colonial possession can create a local claim frontier without making the intervening ocean traversable. This is a consequence of the user's ownership rule, not a special reward reserved for empires.

## A firing is a single wave

A wave uses one frozen ownership snapshot and one resolved Evolution profile. A state granted a claim late in the wave cannot become a new seed merely because it was processed before another state. The outcome must not depend on country processing order or state IDs accidentally appearing earlier in a loop.

The immediate frontier is evaluated for every country in the wave. Deeper rings are chosen from the same snapshot. Claims may overlap freely because granting one country's claim does not consume the state or make it unavailable to another claimant.

Ownership or country changes occurring while a wave is being delivered require revalidation before a benefit commits. They do not authorize silently recomputing only the later countries against a different map. The dispatcher must either complete the logical snapshot transaction safely or defer the affected recipient's refresh with an explicit transaction receipt.

## The outer rings

A ring is the minimum number of valid land-state steps from the country's owned seed set. Ring one is always complete. At Greater Ambitions, a limited number of ring-two targets can be added. Continental Ambitions broadens ring two and reaches selected ring-three targets. Greater Nation reaches several layers, while The World Is Ours can continue from an established connected claim network.

Outer-ring selections have a geographic purpose. They favor closing a gap, connecting neighboring claims, reaching an ambition anchor, or continuing a coherent regional corridor. They do not jump to whichever distant state has the best resources. A parent connection must exist through owned land, existing connected World Claims targets, or a nearer target already admitted to the same staged wave.

Selection is breadth-first. A third-ring target cannot be selected unless its connecting second-ring path exists. A fifth-ring target cannot consume its quota before the necessary nearer links qualify. If an eligible ring has more targets than its allowance, the unselected targets remain candidates for later firings.

The balancing schedule scales outer-ring allowances with the size of the immediate frontier. A wide-border empire can receive more secondary targets than a one-state government, but the small government still receives a useful minimum. The tuning companion gives the exact schedule. These allowances restrict optional deeper expansion, never the complete immediate ring.

## Repetition without movement

At baseline, firing repeatedly with unchanged ownership finds the same immediate border. Claims already held remain held and do not produce duplicate integration rewards.

At Evolutions I through IV, repeat firings can fill previously unselected targets inside that profile's permitted depth. They do not turn an unchanged two-ring ambition into a ten-ring ambition. Territorial ownership must move before the ownership-based envelope moves.

At Evolution V, the established connected World Claims network can advance one additional layer per firing. This is a deliberate late-game change. Even then, ownership does not change automatically, and only the network component currently connected to owned territory can propagate. A detached claim left behind after a lost war cannot independently colonize the rest of a continent on paper.

## Islands and overseas ambitions

An island group, strategic sea, or maritime union is a valid ambition pattern. Recognizing that pattern does not create a land border across water.

A country may already own several islands or establish an overseas foothold through ordinary war, diplomacy, a peace conference, or another event. Those holdings can make an island or sea-centered ambition meaningful. The ambition can display future objectives across water. A displayed objective is not automatically a World Claims claim or a Compliance entitlement.

Once the country owns a foothold, the next wave expands from its local land border. Where an island has no foreign land neighbors at all, further islands remain strategic objectives until the country acquires another foothold through normal play. This preserves the opening's explicit no-land-neighbor rule even at very high Chaos.

A native formable may have its own valid overseas claims. Those remain native rewards and retain their provider's prerequisites. They are not retroactively labeled as World Claims targets unless the World Claims frontier independently reaches them.

## Ambition completion and unclaimed remainders

Completing an ambition can identify the rest of its geographic envelope as the next expansion objective. Missing states already reachable under the current wave-depth rules can receive World Claims claims. Unreachable portions are shown as future objectives, and subsequent waves claim them when connections become valid.

This rule prevents a successful local proclamation from becoming a back door to instant continental claims. It still gives a practical payoff: enclosed gaps, neighboring remnants, and the next coherent corridor become clear targets immediately.

## Changed borders

Peace conferences, scripted transfers, independence, releases, and formables are ordinary inputs to the next map check. The system does not retain a list of countries that counted as neighbors in 1936. A newly independent country's borders are as authoritative as a major's original borders.

If a transfer makes a pending target domestic before claims commit, it is no longer a foreign target for that wave. Existing World Claims integration history for that country can remain relevant. An ownership change does not manufacture a second starting grant.

If a country loses all owned land, its automatic frontier becomes empty. Its active integration or diplomatic obligations are reconciled through its country's lifecycle. It does not continue propagating claims from a remembered capital that no longer belongs to it.

## Map changes between mod versions

The current campaign map includes political changes within the active map revision. It does not imply that a saved game can safely accept arbitrary changes to state IDs or province geometry between mod versions. New map revisions need a reconciled state registry and an explicit migration policy. An unrecognized state must be reported as unsupported until its geometry and identity are rebuilt, rather than assigned another state's outline.

The gameplay promise remains universal across the supported installed map. A small illustrative list of countries or states cannot satisfy it.
