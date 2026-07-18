# Event 15 Target Eligibility Matrix

All thresholds are implemented through the centralized Event 15 candidate-limit, candidate-threshold, and candidate-score constants. This matrix describes the live gate and score rather than an unresolved tuning proposal.

| Check | Preferred | Eligible | Excluded | Reason |
| --- | --- | --- | --- | --- |
| Major status | no | no | yes | The event is for a weak or modest country. |
| Industry | very small | modest | major-level or strong regional industry | Prevents the manifesto from becoming a free major-country overhaul. |
| Focus tree | generic or approved replaceable | lightly developed approved tree | protected unique tree | Acceptance replaces the tree. |
| Political focus depth | little progress | limited progress | mature political or identity route | Avoids deleting an established campaign. |
| Country origin | ordinary country | approved subject or minor | another event-created package | Prevents incompatible country systems. |
| War state | peace or defensive breathing room | limited war with secure capital | civil war, near capitulation, full offensive war | The founding survey must be playable. |
| Capital | secure | temporarily pressured | invalid, occupied without recovery path | The Ledger needs a viable national center. |
| Special classification | ordinary human country | unusual but approved | nonhuman, terminal, world-end, special Chaos actor | Avoids cross-system breakage. |
| Faction role | outside faction or small member | ordinary member | dominant faction leader | Prevents a small-state league from beginning as a great-power bloc. |
| Subjects | none or few | limited and manageable | extensive subject empire | Prevents instant regional dominance. |
| Occupation burden | low | manageable | extensive occupied empire | The event is not a colonial administration shortcut. |
| Human control | strong positive weight | eligible when safe | excluded when protected | Gives players a real chance without destructive targeting. |
| Island or coast | positive context | normal | never required | Supports the island fantasy but landlocked variants remain valid. |
| Landlocked | viable Inland Island | viable | excluded only if no stable capital route | Landlocked countries receive a distinct version. |
| Migration or housing pressure | positive | neutral | never required | Creates genuine Need. |
| Infrastructure weakness | positive | neutral | fatal collapse only | Gives the tree a problem to solve. |
| Recent country transformation | no | distant prior transformation | active or recent full transformation | Avoids stacked replacement events. |

## Candidate-pool order

1. Safe eligible human players.
2. Safe AI minors with generic or approved replaceable trees.
3. Safe AI minors with lightly developed approved trees.

## Weighted score direction

Positive weight:

- weak industry
- low infrastructure
- small state count
- stable capital
- independence
- no faction
- migration or trade pressure
- island, coastal, or strong Inland Island context

Negative weight:

- defensive war
- subject network
- extensive occupied territory
- major guarantee
- recent industrial growth
- recent major event package

## Manual trigger behavior

Manual firing bypasses the random ticket draw but uses the same absolute safety boundary. It cannot target a major, industrial power, special or terminal actor, protected or mature tree, active event package, dominant faction leader, civil-war or offensive-war country, near-capitulated country, subject empire, extensive occupier, insecure capital, or unsafe subject.

## Current implementation proof

The live entry selector applies one reusable absolute gate and a bounded dynamic ticket score. It builds separate human-generic, AI-generic, and approved-light-tree arrays, then chooses from the first non-empty class. Acceptance and rejection are explicit player paths, while an AI recipient accepts with certainty. Manual firing remains separate from ordinary weighted selection but retains the absolute gate.

Necessary Ground uses a second, case-specific target pipeline. A case requires a live relevant calling deficit, a valid selected country, a valid selected state, and method-specific reachability. State-transfer methods show and enforce the requirement that the selected target survive the transfer.

The target country and selected state record independent exact reverse founder arrays. Cleanup removes only the current founder and preserves the shared marker while another founder remains. The narrow Event 15 annexation hook snapshots the country array before clearing the annexed country. The one-shot state-control hook snapshots the changed state's case and association-charter founder arrays and dispatches founder-rooted `.165` after one hour for independent validation, allowing a full annexation's `.163` disposition to run first. The private wargoal injects the exact saved state ID and requires ROOT membership in the state array plus ownership by PREV. Country disposition is successor adoption during active stewardship, explicit founder-extinction failure, or clean pre-steward invalidation. The current decision and country reports pass this contract against the repaired source snapshot. The implementation does not authorize a recurring world scan, arbitrary successor search, or silent integration.
