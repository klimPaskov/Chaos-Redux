# Event 011 high-impact capacity balance

Date: 2026-07-10

## Directive and disposition

Status: implemented and frozen in commit `1c87d9235319781c871c2948813ab55693eb8618`. This document is the accepted balance rationale and validation record for that freeze.

This balance tranche implements the accepted direction that Event 011 must use substantially larger, consequential values and much harsher counter-network costs. It prevents a one-state minor from buying full Preparedness through cheap project cycling while preserving a difficult route to a complete defense through several independently funded systems.

The source design is updated in `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_5_ai_presentation_and_acceptance.md`. Live tuning remains centralized in `common/script_constants/011_secret_alliance_constants.txt`; mission timeouts and decision cooldowns that do not parse shared script constants remain file-scoped at the top of `common/decisions/011_secret_alliance_decisions.txt`.

## Dynamic cost model

The live base package is 24 Command Power, 15 Army Experience, 300 support equipment, 30 trains, 200 trucks, 20 convoys, 1,000 fuel, 7,500 manpower, and 75 Political Power. Individual actions draw the resources relevant to their category rather than charging the entire package at once.

Countries below 10 civilian factories, 15 divisions, or five controlled states receive independent cost multipliers of 1.25, 1.20, and 1.15. Large-country and major multipliers remain in force. Small and large checks are mutually exclusive within each dimension.

| Capacity profile | Composite scale | CP | Army XP | Support equipment | Trains | Trucks | Convoys | Fuel | Manpower | PP |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Standard | 1.000 | 24 | 15 | 300 | 30 | 200 | 20 | 1,000 | 7,500 | 75 |
| Triple-small minor | 1.725 | 41 | 26 | 518 | 52 | 345 | 35 | 1,725 | 12,938 | 129 |
| Maximum live scale | 2.2425 | 54 | 34 | 673 | 67 | 449 | 45 | 2,243 | 16,819 | 168 |

The maximum is the deliberately harsh mixed profile of a major with fewer than 10 civilian factories, more than 80 divisions, and more than 20 controlled states. Its dynamic Command Power price remains below the 60-point decision ceiling. Public dossier prices are 75 PP for a partial dossier, 100 PP to name a member, 140 PP for the coalition case, and 120 PP to expose a sponsor. Preemption requires 65% War Support and costs 15%, 10%, or 6% depending on Evidence; a false case costs 8% Stability. Publicizing conflicting war aims gates and pays 75 PP.

## Preparedness capacity

- One protection project and one emergency commitment may be active at once.
- Standard protection, continuity, and known-plans projects last 300, 450, and 210 days.
- Diplomacy, offensive, and emergency commitments occupy their slots for 90, 120, and 180 days.
- Preparedness bands begin at 30 Alert, 60 Guarded, and 85 Mobilized.
- Protection layers provide 15-20 points, emergency layers 12-20, allied consultation 12, and known plans 20. The component cap remains 20.

At an Evolution II opening, baseline Preparedness is 15. One full protection layer raises it to 35; one emergency layer raises it to 55; known plans raise it to 75; allied consultation raises it to 87. Mobilized Preparedness therefore requires at least four independently funded and time-overlapped layers. A triple-small minor must pay the 1.725-scale packages and accept the associated Stability and long-duration burden modifiers to do so.

## Evidence and public case

The evidence curve preserves attainability under the higher costs and thresholds:

| Independent classes | Evidence | Suspect confidence | Public capability |
| ---: | ---: | ---: | --- |
| 1 | 13 | 18 | Initial developed lead |
| 2 | 44 | 42 | Corroborated investigation |
| 3 | 75 | 66 | Partial dossier |
| 4 | 100 | 90 | Naming and confirmation |
| 5 | 100 | 100 | Coalition case |
| 6 | 100 | 100 | Complete-network achievement route |

Naming remains visible after Coalition Case Evidence is reached. The naming gate requires four independent classes on the suspect, and the coalition case requires five global classes.

## Hostile and wartime intensity

Normal and evolved openings begin with higher Cohesion, Readiness, and Alertness. Operation probability, recruitment, disputes, leaks, and defections have larger live amplitudes. Political attacks and assassination attempts impose 5-6% Stability damage and up to 3% War Support damage when unresolved. Border pressure rises by 25, operational disruption removes up to 20 Readiness, and unprotected surfaces can lose 10 points from their preparedness component.

Reveal conversion is stronger without erasing scenario separation. Low, Medium, High, and Maximum scenarios begin at 55/45, 65/65, 78/82, and 88/95 Resolve/Readiness before conversion. Their equipment packages are doubled from the prior values. Maximum begins below the Resolve ceiling but intentionally reaches 100 when at least two firm member-commitment facts survive conversion; fracture, turned-member, false-plan, and route facts can still pull the coalition away from that ceiling.

Wartime capital loss, failed offensives, sponsor distraction, conflicting promises, two-major rivalry, concessions, member burden, sponsor aid, and route survival all have larger Resolve effects. Revealed AI strategy intensity and exact inverse cleanup values rise together. Direct AI cooldowns are 120 days for protection, 180 for turning a member, and 120 for wartime actions. Manpower reserves gate only manpower-consuming routes, so a small AI may still act through an affordable non-manpower response. Dynamic political actions reserve 170 PP in AI planning, covering the rounded 168 PP mixed-profile maximum instead of assuming the 75 PP base.

## Rewards and persistent ideas

Successful evidence, false-plan, defection, separate-terms, and sponsor-accountability paths receive larger outcomes. Aftermath choices grant material Political Power, Stability, War Support, or up to 730 days of retained counterintelligence. Persistent ideas now impose or grant 4-25% effects instead of reward dust, while retaining their original signs and gameplay roles.

## Validation scenarios

1. A triple-small minor receives all three small-capacity surcharges and cannot hold more than one protection and one emergency layer.
2. A fully scaled major remains below the Command Power decision ceiling.
3. Four independent suspect classes reach 90 confidence and keep the naming action visible at 100 Evidence.
4. Five global evidence classes satisfy the coalition case; six preserve the complete-network achievement path.
5. Public action gates and payments match, including the 75-PP conflicting-war-aims action.
6. Scenario Resolve/Readiness and doubled stockpiles preserve Low/Medium/High/Maximum separation.
7. AI strategy additions and cleanup values remain exact inverses.

## Simplifications, omissions, and blockers

None. IDs, enums, founder count, membership caps, scenario roster rules, achievement requirements, consent gates, and callback safety caps are not inflated as part of the balance pass. Known no-op tuning changes were reverted and are not credited as gameplay changes.
