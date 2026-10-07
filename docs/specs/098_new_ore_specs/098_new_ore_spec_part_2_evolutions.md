# New Ore, part 2: Evolutions and the spread of deposits

## One discovery with four mutation tracks

The initial discovery always creates exactly one state deposit. The event then continues through control changes, access agreements, and international competition at any Chaos level. The four evolutions expand that ongoing system at the user's thresholds.

Each evolution has its own enabled state and one activation receipt. A disabled earlier evolution does not make a later enabled evolution impossible. For example, New Deposits can occur while Deep Vein is disabled, and the Super-Alloy can transform the original deposit while New Deposits is disabled. The existing state and agreement rules remain coherent in every combination.

Always use the highest manifested material grade. Super-Alloy takes precedence over Deep Vein, which takes precedence over baseline. If Deep Vein resolves after Super-Alloy, its original-state finding and export-capacity increase still occur, but direct armor remains at the Super-Alloy formula and foreign armor remains +80%. Existing paid terms are not repriced and the lower grade does not earn its +3 Chaos after a stronger grade already dominates.

Chaos thresholds establish eligibility. Actual active-event evolution uses the project's dynamic MTTH progression. The numbers below are tuning anchors with declared timing factors, not a claim about observed engine probabilities. There is one evolution at each of 200, 400, 600, and 800 Chaos.

| Evolution | Minimum Chaos | MTTH reference anchor after eligibility | Dynamic factors | Intended timing envelope |
| --- | ---: | ---: | --- | --- |
| I: The Deep Vein | 200 | 90 days | Faster with sustained ore access, active foreign agreements, and a Riches Found operation in the original state | 60–180 days |
| II: New Deposits | 400 | 120 days | Faster at higher Chaos and after Deep Vein, slower when discovery just occurred | 90–240 days |
| III: Ore Wars | 600 | 90 days | Faster with competing armored powers, refused access, contested deposits, and rival suppliers | 60–180 days |
| IV: The Super-Alloy | 800 | 120 days | Faster with mature direct access and several active users, slower immediately after first discovery | 90–240 days |

Timing modifiers should use a few readable steps. A qualifying accelerating factor ordinarily multiplies the interval by 0.8, a slowing factor by 1.25, and the result stays within its envelope. Two overlapping descriptions of the same condition must not apply twice. An active war alone does not accelerate every evolution.

Eligibility begins when both the event exists and the threshold is satisfied. The record of elapsed time belongs to the event or original deposit as appropriate. Capturing a state, switching tags, opening a decision category, or repeating callbacks does not restart or accelerate evolution time.

### An opening at high Chaos

A first firing at 800 or more Chaos still begins with one deposit and the baseline immediate armor benefit. Every enabled evolution whose threshold is met becomes eligible from that discovery. It receives the normal dynamic progression with the recent-discovery slowing factor. The country does not need another random firing of Event 098.

This is the explicit late-opening route. It preserves the initial priceless single deposit, then lets a volatile world progress quickly through the eligible evolutions. It does not secretly create an initial bundle of future deposits. When several tracks resolve together, process their distinct outcomes in stage order and show one concise combined update where appropriate.

Once an evolution has physically improved the material or revealed deposits, a later fall in Chaos does not remove those consequences. Turning off future evolution activation does not retroactively erase geological discoveries or rewrite existing equipment benefits.

## Evolution I: The Deep Vein

Further work in the original state establishes that the deposit is much larger and richer than first understood. The current controller benefits, even if it differs from the discoverer. The original state remains the location of this revelation.

The direct effective armor advantage rises from 50% to 75%. Foreign access rises from 20% to 30%. Existing deployed forces and already active agreements upgrade with the new material. Customers do not pay a second activation fee solely because the evolution occurred.

Each deposit can now support three selected foreign countries instead of two. This increases the owner's diplomatic reach while preserving a substantial gap between foreign access and control. Existing agreements retain their dates and agreed compensation. New or renewed contracts use the improved material's current value.

If later deposits already exist because Evolution II activated first, Deep Vein's geological scene remains centered on the original state. The validated refining knowledge becomes common to the same mineral and improves all registered deposits. This avoids two indistinguishable grades that the player would have to track indefinitely.

If the original state temporarily lacks a valid controller, its geological finding persists and the stronger access begins for any other controlled deposits and their users. Its future controller receives the evolved direct benefit when control becomes valid.

The report direction combines material abundance with the controller's new ability to promise selected partners a meaningful supply. It should mention the original state, current controller, and the difference between sovereign access and foreign allocation.

## Evolution II: New Deposits

The first concrete outcome reveals one additional deposit in a uniformly random valid state without an existing deposit. Subsequent discoveries continue at a bounded global cadence. Every selection rebuilds or revalidates the complete eligible state pool and samples without replacement.

The new state can belong to the original controller, a customer, a rival, an unrelated minor, or a country already at war. The design does not force rivalry by excluding the original controller. An empire's chance reflects how many eligible states it actually controls. It does not receive a country-level weighting bonus.

There is no predetermined list of countries, continents, or states. Several deposits can appear in one region, and a distant continent can receive none in a particular campaign. The geography is an outcome to play around.

### Keeping the material scarce

At first discovery, record the number `V` of genuine playable land states, independently of temporary controller validity. Use the following world-size scarcity target:

`deposit ceiling = min(V, max(3, min(12, ceil(V / 125))))`.

For a map with 1,000 such states, the event can reveal eight deposits in total. A 500-state map supports four. A two-state test map supports two. These are examples of the rule, not an assertion about the installed map's state count.

The ceiling includes the original state. It limits discoveries, not the armor calculation or the validity of already registered deposits. Supported map migrations may raise the ceiling to reflect added map space. They do not delete existing deposits when the calculated ceiling becomes smaller.

After the first new deposit, the MTTH reference anchor for another is 180 days. Raise it by 20% for each deposit already discovered beyond the second. Apply a 0.8 factor at 600 Chaos and another 0.8 factor at 800 Chaos. Deep Vein adds a 0.9 factor because the mineral is easier to recognize. Clamp the intended interval to 90–540 days.

The increase is linear, not compounded. With `n` deposits already discovered, the exact reference interval is `clamp(90, 540, 180 × (1 + 0.2 × (n − 2)) × C600 × C800 × Vdeep)`, where each applicable Chaos factor is 0.8, the Deep Vein factor is 0.9 when manifested, and every inapplicable factor is 1. This subsequent-discovery formula is used for `n >= 2`.

This gradually weakens the monopoly over a multi-year campaign. It does not fill the world with deposits during one brief Chaos spike. The next due date is global to Event 098 and survives every control change. If no eligible undiscovered state exists, retain the pending opportunity and recheck through the bounded event lifecycle without creating a permanent world scan.

A player cannot purchase a guaranteed home-territory discovery or repeatedly reroll the candidate pool. Exploration is an event outcome. Military and diplomatic play responds to the locations that emerge.

### What a new location changes

The new controller immediately receives the current direct armor tier. The state receives the same durable geological identity and export capacity as other deposits. Its controller can negotiate independently. An existing customer that discovers a deposit uses its stronger direct access and may keep an already signed foreign agreement as a backup until expiry or voluntary termination.

A new deposit does not automatically cancel other countries' treaties or refund an earlier supplier's price. It changes bargaining conditions for the next agreement. Reports emphasize the newly empowered state and the end, or survival, of a previous monopoly.

Before the Super-Alloy, controlling several deposits gives resilience, export opportunities, and denial of rivals. The direct armor multiplier remains the same as controlling one.

## Evolution III: Ore Wars

The deposits become explicit high-priority strategic objectives for relevant governments. New diplomatic demands and preparation choices support ordinary war and diplomacy. The detailed demand and AI rules are in part 4.

Activation immediately changes how interested AI countries evaluate suppliers, deposit defense, state acquisition, faction partners, and credible demands. It also exposes the ore-access demand route to eligible players. Activation itself does not declare wars, award territory, grant cores, or create an automatic anti-owner coalition.

Countries with substantial armored forces or armored production care most. A country already enjoying secure access often favors protecting its source. A capable rival denied access becomes more willing to prepare for war. A distant country with no credible route can still negotiate, sponsor ordinary diplomacy, or improve counters.

Several deposits under one controller increase its strategic significance even before their direct armor begins to stack. Rivals perceive concentrated supply and the danger of depending on that country. The controller can respond with a monopoly, selected sales, or alliance support.

The presentation shifts from discovery and commercial attention toward the material's influence on military planning. The tone remains tied to actual diplomatic and military acts. A normal peaceful sale does not become an armed crisis simply because Chaos crossed 600.

## Evolution IV: The Super-Alloy

Refining produces an extreme increase in effective armor. A country with one directly controlled deposit receives a 200% Event 098 armor advantage, meaning at least three times its otherwise equivalent armor. Foreign access rises to 80%, remaining substantially below direct control.

Extra directly controlled deposits now improve the alloy through a diminishing contribution. For `n` directly controlled deposits:

`direct Event 098 advantage = 200% + 100% × (1 − 1/n)`.

| Direct deposits | Event 098 armor advantage | Armor relative to the same force without Event 098 |
| ---: | ---: | ---: |
| 1 | +200% | 3.00× |
| 2 | +250% | 3.50× |
| 3 | +266.67% | 3.67× |
| 4 | +275% | 3.75× |
| 6 | +283.33% | 3.83× |
| 12 | +291.67% | 3.92× |

The Event 098 contribution approaches +300% and never reaches or exceeds it through deposit count alone. Each additional deposit is useful, while the first remains the most valuable. A loss from two deposits to one removes the additional 50 percentage points immediately and retains the single-deposit +200% floor.

This formula depends on current direct control. Subjects' deposits, foreign contracts, claims, past ownership, and diplomatic guarantees do not count as additional direct deposits. Foreign access uses the strongest valid agreement, with an 80% ceiling from Event 098. Buying several licences cannot reproduce the controller's multiplier.

Existing equipment and armies benefit alongside new production. The refinement does not introduce a production-only exception that would strand earlier armor at the old level.

The report direction focuses on the changed behavior of protective material in practical testing and the military consequences of concentrated sources. The visual motif moves from raw ore to a finished alloy surface. It retains the same mineral identity and period setting.

## Chaos from concrete changes

The complete impact map in part 5 assigns Chaos to material discovery, geographic spread, and the first operational use of extreme refining where those outcomes occur. Eligibility, stage activation, a log entry, and an unlocked decision contribute zero by themselves.

If an evolution and its concrete outcome occur in one resolution, the outcome receives the single appropriate receipt. A combined high-Chaos update cannot collect a second grant because it also advanced an evolution label.
