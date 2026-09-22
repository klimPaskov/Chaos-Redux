# The earned Irish focus tree

The tree begins with the practical consequences of successful reunification and opens into several sustained national strategies.
It is a full country tree, including domestic politics, civilian and military industry, army, navy, air force, culture, diplomacy, and late route development.
A player must be able to complete a satisfying campaign without choosing the Gaelic Empire.

## Structure and pacing

This package specifies 65 focus groups.
A group is a coherent gameplay sequence, not a mandatory single focus node.
Implementation may split a group into several focuses when each node adds a meaningful choice, preparation, or payoff.
It may combine small steps that would otherwise be filler.
There is no mandated node count or coordinate layout.
Group identifiers are stable planning references.

| Lane | Groups | Purpose | Access |
| --- | --- | --- | --- |
| U | U01 to U08 | Reunification, constitutional settlement, industry and Britain | Immediately after victory |
| G | G01 to G07 | Gaelic institutions and competing national visions | Early common lane |
| E | E01 to E09 | Gaelic Empire and imperial administration | Gaelic milestones and imperial commitment |
| C | C01 to C09 | Celtic partnership and federal institutions | Early diplomatic opening, then federal commitment |
| T | T01 to T08 | Atlantic economy, access and overseas strategy | Early maritime opening, then primary Atlantic commitment |
| M | M01 to M09 | Permanent army, equipment and operational specialization | Immediately after victory |
| N | N01 to N07 | Sustainable naval force and maritime doctrine | Common industrial opening |
| A | A01 to A08 | Air force, production, defense and naval aviation | Common industrial opening |

Short rebuilding, administrative, and initial military choices use approximately 35-day focus costs.
Major institutional, industrial, and strategic commitments use approximately 70-day costs.
A special tree-transition acknowledgement, if mechanically necessary, must not delay usable branches for more than seven days.
Longer goals belong in visible missions with progress and costs, not in repeated empty prerequisite focuses.
The first six to twelve months should support several meaningful domestic and military decisions.
Formation of an empire or federation requires actual territorial or diplomatic achievement beyond elapsed focus time.

## Route commitments

Gaelic education and the common cultural institutions remain compatible with all strategies.
Early Scottish diplomacy can also be explored before selecting a final strategy.
The formal imperial charter and the binding federal charter are mutually exclusive commitments.
A primary Atlantic commitment declines those two capstone identities and obtains its own diplomatic and maritime payoffs.
It does not block shared culture, military branches, trade with Celtic countries, or defensive cooperation.

Imperial and federal governments retain the shared Atlantic economic opening and the common navy and air force.
They do not also collect the full primary Atlantic diplomatic capstone.
Primary Atlantic governments may make normal alliances but do not receive the federal charter's common institutions through a renamed faction.
Mutual exclusions must be visible before a focus starts.

A single strategic reconsideration can occur before any imperial proclamation or federal constitution has been completed.
It costs 100 Political Power, suspends new route-specific projects for 90 days, ends incompatible unexecuted offers, and removes unearned route preparation benefits.
It does not refund completed focuses or reverse transferred territory.
After a capstone commitment, the campaign continues within that identity.
Ordinary political changes can still occur, but cannot farm all three route rewards.

## Northern recovery and construction

Northern industrial rewards require Irish ownership and control of the intended state.
If the state is temporarily occupied when an otherwise eligible focus completes, record a single pending construction entitlement and expose the blocked location.
Apply it once after the location becomes valid.
Do not repeatedly pay a factory reward on each recapture.
If a construction slot is unavailable, provide the predefined alternate investment, such as a repair allocation or a production research bonus, with no hidden random downgrade.

Existing factories and shipyards count toward the completion conditions of development groups, but do not automatically grant their new rewards a second time.
A country that inherited substantial Belfast industry should obtain specialization, repairs, or capacity improvements instead of duplicating the same buildings blindly.
Industrial reward tables must account for already-built levels and available slots.

## Existing focus-tree transition

Load the Event 072 tree only after the success marker has been committed.
Preserve all completed old focus effects already applied to the country.
Do not infer that loading the new tree should replay them.
Check how the installed focus-loading effect handles an active focus, completed-focus history, stored focus progress, continuous focuses, and AI plans.
The implementation plan contains a required test for each.

The intended player result is that a running old focus is allowed to finish normally before the new tree is presented only when that can be done without delaying the new campaign excessively or producing duplicate effects.
The preferred transition is immediate replacement with a one-time, proportionate stored-progress compensation supported by the engine.
The installed effect determines which policy can be delivered safely.
Choose and document one tested policy before coding the full tree.
Do not invent an unsupported exact refund command or silently erase months of progress.

The new tree's entry groups recognize actual existing technologies, factories, laws, and forces.
Bypasses skip redundant requirements, but do not bypass the victory gate or pay a skipped focus's reward twice.
An Ireland already possessing a navy can enter operational development without pretending it has no ships.
A country with another mod's unique tree needs an explicit compatibility decision.
The package does not promise universal coexistence with every overhaul.

## Group implementation record

For every group, the implementer records final focus IDs, prerequisite structure, mutual exclusions, supported effects, total cost, event and decision consumers, asset IDs, AI priority, and a valid-country fixture.
The following route files define the content those nodes must deliver.
No node is accepted merely because its title resembles a group heading.
The user-visible tooltip must state the practical unlocked action or effect.

## Branch audit

At baseline with Evolutions disabled, validate a complete civic-island campaign, an imperial campaign, a federal campaign, and a primary Atlantic campaign.
At higher tiers, test the additional groups against those same destinations.
A disabled Evolution should hide or mark only its additive content, not leave a broken prerequisite gap in the common tree.
Test north lost and recaptured, unavailable Scottish or Welsh tags, a human target refusing an offer, full industry slots, and an already advanced Irish military.
