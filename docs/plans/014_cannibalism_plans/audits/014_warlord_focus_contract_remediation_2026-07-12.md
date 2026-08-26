# Event 014 warlord focus-contract remediation

> **Superseded historical proposal.** This audit predates the 2026-07-15 three-origin consolidation. Its former Prison Host and Lockhouse-origin language is rejected; prison, detention, and depot mechanics remain ordinary objectives and do not define a fourth origin.

## Outcome

The shared 72-focus warlord tree no longer leaves its operation flags as inert promises. Its 79 `cannibalism_warlord_*` focus flags now feed state consumption, state intensification, state-accounted recruitment, origin operations, foreign seeding, synchronized attacks, convergence, submission, autonomy, resistance, or the existing Host Operating Order.

A static consumer audit finds 75 flags read outside the focus-effect file. The remaining four are deliberately consumed inside `014_cannibalism_warlord_focus_effects.txt` by the Host Operating Order rebuild:

- `cannibalism_warlord_larder_order_complete`
- `cannibalism_warlord_military_order_complete`
- `cannibalism_warlord_network_order_complete`
- `cannibalism_warlord_operating_order_open`

No focus-created warlord flag remains without a gameplay consumer.

## Consumer families

### State-accounted recruitment

The recruitment transaction prepares a single contract before the Deaths-backed population payment. Survival orders, origin defense, repaired routes, lieutenant assignments, hierarchy access, officer training, distributed recruitment, workshop conversion, personal-guard doctrine, leader protection, penal columns, and the three hierarchy war doctrines alter starting experience or the per-state recruitment cooldown. The cooldown remains at least seven days, starting manpower and equipment remain zero, and every formation still requires real population, Larder, stockpiled equipment, a usable controlled state, and the existing unit cap.

Workshop conversion recovers a small, constant-capped infantry-equipment parcel only after a valid paid recruitment succeeds. Emergency reinforcement under the survival order relieves Frenzy and restores Command Integrity; a tyranny purge attached to Bone Guard recruitment raises both coercive control and Frenzy.

### Larder and feeding districts

Larder inventory and accounting add small bounded yields only after a real population-consumption transaction succeeds. Prisoner ledgers raise Network Alignment, provincial servants restore Command Integrity, Rapid Consumption accelerates Frenzy and state exhaustion, Managed Herds lowers Frenzy and strengthens the active node, and mobile reserves improve command continuity. Feeding District and council-vote contracts further strengthen a successfully intensified node while applying their route tradeoff.

The Rapid Consumption exhaustion flag adds another consumption action to the exact state that paid the population cost. It does not duplicate the Deaths transaction or generate Larder from an unusable state.

### Major-victory harvest

Battlefield Harvest is tied to enemy capitulation through the narrow `on_capitulation` hook. Each warlord keeps a country-scoped array of defeated countries. A defeated country can therefore pay one Larder/equipment receipt to a given warlord incarnation, and the array is cleared when a reusable slot is initialized. The reward is capped by the defeated-country identity rather than a repeatable combat pulse.

### Origin operations

The four existing costed origin decisions remain the player-facing operation surface. Their duration and recoverable raid material are prepared from completed focus contracts:

- Island Host: hidden anchorages, landing cadres, the archipelago endgame, convoy recovery, shared roads, supply targeting, and mobile escort.
- Siege Commune: tunnels, relief ambushes, the city endgame, support-equipment recovery, shared roads, and supply targeting.
- March Host: depot raids, rail sabotage, predatory corridors, the moving-front endgame, truck and train recovery, shared roads, and mobile escort.
- Prison Host: transfer infiltration, prison/depot raids, officer corruption, the Lockhouse endgame, and additional network/alignment pressure.

All four operations retain Larder and Command Power costs and their decision cooldowns. Recovered equipment is an operation result, not a free recruitment grant.

### Network and convergence

Courier routes and submission preparation improve the paid alignment decision. Commune absorption, shared roads, and convergence leverage extend synchronized operations. Network routes expand shared reach after a valid foreign seed; manipulation and diverted couriers recover bounded Larder; officer corruption inflicts a small stability loss on the actual target country.

Convergence leverage and the manipulation endgame add explicit host-selection score. Submission preparation improves the Larder transfer when the aligned warlord retains command. The manipulation endgame reduces autonomous tribute. Independent fortification and the defiance endgame construct capital forts only when the warlord actually resists unification, and the AI weights those completed routes toward their matching response.

### Anti-decapitation

The Pack Confederacy anti-decapitation capstone replaces captured-warlord prosecution choices with an escape outcome. It records the character outcome through the existing ledger and does not bypass the country capitulation itself.

## Files changed by this remediation

- `common/script_constants/014_cannibalism_warlord_focus_constants.txt`
- `common/scripted_effects/014_cannibalism_warlord_decision_effects.txt`
- `common/scripted_effects/014_cannibalism_warlord_focus_effects.txt`
- `common/scripted_effects/014_cannibalism_country_effects.txt`
- `common/scripted_effects/014_cannibalism_spread_effects.txt`
- `common/scripted_effects/014_cannibalism_unification_effects.txt`
- `common/on_actions/014_cannibalism_on_actions.txt`
- `events/014_cannibalism.txt`
- `events/014_cannibalism_aftermath.txt`

## Remaining verification

Player-facing warlord focus and captured-outcome localisation must be aligned with these exact consumers after the concurrent unified-localisation patch lands. The decision/mission and focus-tree re-audits must then verify the implementation rather than relying on this static mapping alone.
