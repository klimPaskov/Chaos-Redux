# Event 58 weighted-selection scenario plan

Random Buildings contains several weighted surfaces even though it has no AI decision path. Every implemented weight, risk-band chance, provider weight, province-package weight, cluster participation value, and exceptional-family weight requires the project probability workflow.

The probability auditor must begin with `hoi4.probability_inspect`. Exact probabilities can be claimed only when the full candidate pool, validity state, fallback path, DLC state, and external provider factors are supplied.

## Required audited surfaces

| Surface ID | Surface | Evidence goal |
| --- | --- | --- |
| `RB-PROB-01` | baseline risk-band selection | prove restricted entries retain their global rarity envelope |
| `RB-PROB-02` | baseline entry selection inside each band | prove ordinary family ordering and industrial minority share |
| `RB-PROB-03` | Evolution I risk-band selection | prove rare and extreme structures remain uncommon |
| `RB-PROB-04` | Evolution I entry selection | prove expanded ordinary construction dominates without starving advanced entries |
| `RB-PROB-05` | Evolution II package selection | prove rail and ordinary defense lead, with ports and hubs less common |
| `RB-PROB-06` | Evolution III provider selection | prove no provider monopolizes the limited budget without a design reason |
| `RB-PROB-07` | Positive Economy cluster participation | prove Event 58 is a meaningful Medium member without dominating cluster firings |
| `RB-PROB-08` | repeat-firing saturation | measure how caps and exhausted candidates alter later distributions |

## Scenario matrix

### `RB-S01` Typical inland state at Calm World

- normal civilian owner
- infrastructure below maximum
- room for air base, anti-air, radar, and fuel silo
- two free industrial slots
- no coastline
- no special provider eligibility
- baseline only

Expected order:

1. infrastructure and ordinary strategic support families dominate
2. civilian and military factories remain a minority
3. no dockyard or province package appears
4. no restricted result is possible unless its band and provider are explicitly included

Result classification can be exact only when all baseline entries and weights are present.

### `RB-S02` Developed inland capital

- infrastructure at maximum
- air base and radar partly developed
- one free industrial slot
- no coastline
- normal civilian owner

Expected behavior:

- infrastructure has zero weight
- invalid weight does not transfer to a rarer band
- ordinary candidates renormalize only inside their selected band
- one free industrial slot permits a factory but does not make it the dominant result

### `RB-S03` Coastal industrial state

- usable sea coastline
- one existing naval base below maximum
- free industrial slots
- ordinary baseline candidates valid

Expected behavior:

- dockyard enters baseline ordinary selection
- dockyard remains a low-frequency ordinary result
- naval-base placement is absent before Evolution II
- coastline does not remove inland ordinary candidates

### `RB-S04` Special nonhuman controller

- state controlled by a country that fails `uses_normal_civilian_systems`
- infrastructure, military industry, air support, radar, storage, and fortification remain mechanically valid
- civilian-only provider entries are invalid

Expected behavior:

- the state stays in the transaction
- civilian-only entries have zero weight
- the remaining ordinary pool remains usable
- no global exclusion of the state occurs

### `RB-S05` Baseline restricted provider present

- concentration-camp provider valid
- broad ordinary pool also valid
- baseline restricted band enabled

Expected bounds:

- restricted-band selection centers near `0.1%` and stays below the accepted `0.25%` hard ceiling in a representative mixed world
- camp probability does not rise because another rare provider is absent
- removing one ordinary candidate changes only ordinary-band composition
- removing every ordinary candidate causes downward fallback exhaustion, never an automatic camp

### `RB-S06` Empty restricted band fallback

- restricted band is rolled
- every restricted provider becomes invalid during revalidation
- strategic and ordinary bands remain valid

Expected behavior:

- fallback moves to strategic, then ordinary if needed
- the layer creates at most one building
- the resolver never rolls an extreme or exceptional provider

### `RB-S07` Evolution I mixed candidate state

- Chaos `200+`
- Evolution I enabled
- ordinary expansion, rocket site, reactor, grid, rare energy site, and extreme repression provider valid

Expected behavior:

- ordinary expansion centers near `94%`
- advanced providers center near `5%` and remain visible at world scale
- rare providers center near `0.9%` and stay below the accepted `1.5%` hard ceiling
- extreme providers center near `0.1%` and stay below the accepted `0.2%` hard ceiling
- one missing ordinary candidate does not inflate rare or extreme bands

### `RB-S08` Evolution I with DLC removed

- same state as `RB-S07`
- one facility or reactor DLC unavailable

Expected behavior:

- unavailable entry has zero weight
- no placeholder provider replaces it
- risk-band probability remains fixed before safe fallback
- available entries within the same band renormalize correctly

### `RB-S09` Interior Evolution II state

- Chaos `400+`
- no coast
- no foreign border
- existing railway below maximum
- supply hub location valid

Expected order:

- railway is the leading package
- supply hub remains uncommon
- land forts, coastal forts, and naval base are invalid
- the state receives one package only

### `RB-S10` Coastal foreign-border state

- usable coast
- several foreign land-border provinces
- existing naval base below maximum
- existing railway below maximum
- no supply hub

Expected order when all standard packages are valid:

1. railway
2. land-border fortification
3. coastal fortification
4. naval-base package
5. supply-hub package

Exact ordering must be proven after every contextual modifier is applied.

### `RB-S11` Partial fort saturation

- one selected state has six relevant border provinces
- four can gain a fort level
- two are capped

Expected behavior:

- the land-fort package remains valid
- four provinces change
- no second package is rolled
- the package report returns four affected provinces

### `RB-S12` Railway connection unsupported

- state has no existing railway
- a new path would be needed
- the installed engine or MCP inspection cannot prove a safe runtime route

Expected behavior:

- new-connection form is invalid or blocked
- no infrastructure fallback is inserted
- other valid province packages can compete
- the audit marks the unsupported construct, not a guessed probability

### `RB-S13` Evolution III broad provider pool

- Chaos `600-799`
- at least five dam sites, five facility sites, and five landmark sites are valid
- no provider has a special priority modifier

Expected behavior:

- budget respects the valid-state formula and cap
- no state receives two exceptional structures in one firing
- provider families receive proportional opportunities
- a single provider cannot exceed the budget through duplicate location rows

### `RB-S14` Evolution III scarce pool

- only three valid exceptional locations exist
- calculated minimum target would otherwise be five

Expected behavior:

- exactly three or fewer successful placements occur
- no ordinary structure fills the missing slots
- failed callbacks reduce the final count and never force an invalid location

### `RB-S15` Totalen Chaos exceptional cap

- Chaos `800+`
- enough valid locations for more than fifteen placements

Expected behavior:

- the high-Chaos cap limits successful placements to fifteen
- invalidated locations do not allow the budget to overrun through retries

### `RB-S16` Repeat firing after saturation

- Event 58 has fired several times
- many infrastructure, radar, air-base, factory, and fort candidates are capped
- some ordinary and province candidates remain

Evidence goals:

- compare first-firing and later-firing family shares
- identify starvation or dominance caused by saturation
- prove rare bands do not become more common merely because common entries are capped
- verify zero-result preflight when all active layers are exhausted

### `RB-S17` Positive Economy cluster initiation

- Event 58 is selected
- all cluster members enabled and eligible
- Calm World

Evidence goals:

- inspect cluster roll and member participation
- prove Event 58 can initiate the cluster through the ordinary member path
- prove the cluster still counts as one pacing event

### `RB-S18` Event 58 as a secondary cluster member

- another Positive Economy member initiates the cluster
- Event 58 eligible
- complete member pool supplied

Expected behavior:

- Event 58 participates often enough to match a Medium member
- it does not approach guaranteed participation
- its global effect does not starve other optional members

## Required sweeps

The auditor should sweep:

- every risk-band threshold
- ordinary industrial share from low to high accepted bounds
- removal of each major candidate family
- state capacity from empty to saturated
- active evolution combinations
- DLC combinations
- exceptional valid-location counts from `0` to above the high cap
- cluster participation across Calm World through World Collapse
- repeat-firing states at several saturation levels

## Required comparison pass

Any implementation or tuning change to a probability-bearing value requires:

1. baseline `hoi4.probability_inspect`
2. named scenario evaluation
3. owner-applied patch
4. `hoi4.probability_compare` using the same scenarios
5. rendered matrix, sensitivity, ranking, or unresolved view where it improves review

The auditor remains read-only and does not choose the final balance target.
