# AI and Probability Scenario Matrix

## Purpose

This matrix defines the weighted surfaces that require inspection before implementation and comparison after implementation. It provides expected ordering, dominance, starvation, and invalidity rules. It does not claim exact probabilities without the complete candidate pools and external factors.

Start every surface with `hoi4.probability_inspect`. Use evaluation and sweeps for scenario states. Use comparison after the owner patch. Use sequence analysis only if the full repeat, cooldown, removal, and cluster cadence contract is declared.

## Surface A: commissioning choice

Complete candidate pool:

- Full Commissioning
- Phased Commissioning
- Break Up the Package when legal

| Scenario ID | State | Legal options | Required result |
| --- | --- | --- | --- |
| NAV-AI-01 | Wartime major, strong fuel, large ports, active naval front, balanced package | All | Full ranks first and has a clear score lead. Break Up ranks last. |
| NAV-AI-02 | Peacetime minor, one weak port, low fuel, capital package | All | Phased ranks first. Full ranks last or becomes invalid if immediate delivery cannot be supported. |
| NAV-AI-03 | Minor fighting a severe land war, almost no fuel, submarine package, no active naval objective | All | Phased or Break Up ranks above Full. Break Up must remain bounded rather than automatic. |
| NAV-AI-04 | Island country under live convoy and invasion pressure, adequate fuel, escort package | Full and Phased, Break Up legal only if excess exists | Full strongly dominates and should score at least twice the next valid option. |
| NAV-AI-05 | Carrier package, no legal carrier air group yet, safe ports available | Phased and Break Up | Full is invalid until minimum air support can exist. Phased ranks first. |
| NAV-AI-06 | Existing top-tier navy, duplicate destroyer swarm, limited repair congestion | All | Phased or Break Up ranks above Full. No option may receive zero merely because the country is a naval major. |
| NAV-AI-07 | Small coastal country with no prior navy, standard coastal-defense package, moderate fuel | Full and Phased | Full ranks first, but Phased remains material. |
| NAV-AI-08 | Permitted special Chaos country | Owner-defined legal subset | Owner strategy controls ordering. Generic handling cannot expose an invalid ordinary choice. |
| NAV-AI-09 | Recipient annexed or no valid port | None | All choices are invalid and the package cancels cleanly. |

Required sweep dimensions:

- fuel from critical shortage through strong reserve
- naval base capacity from emergency facility through major port network
- peace versus war
- home-water threat
- package size band
- receipt count
- carrier-air readiness
- existing fleet overlap

Acceptance:

- no invalid choice receives a positive chance
- Full does not dominate every scenario
- Break Up does not dominate ordinary minors
- Phased has a real middle role
- small weight changes do not invert unrelated scenarios

## Surface B: package identity pool

Baseline candidate identities and planning weights:

- Balanced 16
- Submarine 14
- Destroyer 12
- Convoy Escort 12
- Cruiser 10
- Capital 8
- Carrier 8
- Coastal Defense 9
- Invasion Support 8
- Sea Denial 3 when legal

| Scenario ID | State | Required result |
| --- | --- | --- |
| NAV-PKG-01 | Full baseline content available | All ten legal identities have nonzero share. Balanced is common but cannot dominate the pool. |
| NAV-PKG-02 | Mine warfare unavailable | Sea Denial is removed and the remaining pool renormalizes. No recipient-specific strategy factor changes the result. |
| NAV-PKG-03 | No credible carrier aircraft route | Carrier is removed for legality. The system does not replace it with the recipient's preferred identity. |
| NAV-PKG-04 | Evolution I active | Extreme size and skew modifiers change composition after identity selection. Baseline identities remain present. |
| NAV-PKG-05 | Evolution II active with two registered assets | Only identities allowed by each owner registration can draw those assets. Ordinary identities cannot starve. |
| NAV-PKG-06 | Evolution III active | Impossible hybrid branches remain rare relative to ordinary identities and retain a primary identity. |
| NAV-PKG-07 | Same country receives three legal packages | Immediate exact repeats are allowed. A soft variety factor cannot guarantee three different identities. |

Acceptance:

- country doctrine, ideology, enemy, and production are absent from identity weighting
- legal content gates are the only recipient-specific pool removals
- rare experimental content cannot consume most rolls
- no identity reaches practical starvation in a complete legal pool

## Surface C: dual-cluster entry

Candidate outcomes when Event 56 is selected:

- no cluster
- Sudden Abundance
- Military Preparation when its Chaos gate is met

| Scenario ID | State | Required result |
| --- | --- | --- |
| NAV-CLU-01 | Chaos below Military Preparation threshold | Only no-cluster and Sudden Abundance are legal. Working Sudden Abundance target is near 15 percent before audit. |
| NAV-CLU-02 | Both clusters available | No-cluster remains dominant. Sudden Abundance has a higher share than Military Preparation. Exactly one cluster can win. |
| NAV-CLU-03 | Sudden Abundance on cooldown | No-cluster and Military Preparation remain legal. |
| NAV-CLU-04 | Military Preparation disabled | Sudden Abundance remains unaffected. |
| NAV-CLU-05 | Both clusters disabled or cooling down | Event 56 fires alone with no dead-end or reroll loop. |

Acceptance:

- one selected event creates at most one cluster transaction
- combined entry shares do not accidentally sum through independent success rolls
- cluster availability does not change the Event 56 package identity roll

## Surface D: optional cluster members

### Sudden Abundance planning weights

| Event | Relative weight |
| ---: | ---: |
| 19 | 70 |
| 29 | 65 |
| 32 | 55 |
| 37 | 65 |
| 42 | 45 |
| 56 | 60 |
| 64 | 55 |

### Military Preparation planning weights

| Event | Relative weight |
| ---: | ---: |
| 32 | 65 |
| 42 | 55 |
| 56 | 60 |
| 64 | 65 |

Required checks:

- selected event is always included when valid
- optional weights produce varied member counts
- Low member Event 42 participates less often than the Medium core in Sudden Abundance
- no member is practically starved across valid scenarios
- a disabled, unavailable, or Chaos-locked member is skipped with the correct reason
- Event 56 can participate once and cannot apply twice through dual membership

## Comparison evidence

The post-patch audit must use the same scenario IDs and include:

- source revision before and after
- complete candidate pool declaration
- external factors supplied or declared unresolved
- score and normalized share where exact
- sweep boundaries
- ordering changes
- invalid candidates
- dominance and starvation findings
- `hoi4.probability_compare` result

Any scenario that cannot be evaluated exactly must be labeled bounded, sampled, score-only, or unresolved. Do not convert an unresolved result into a balance claim.
