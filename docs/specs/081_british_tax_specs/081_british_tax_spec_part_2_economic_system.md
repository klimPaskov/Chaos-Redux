# British Tax: economic system

All tables below are initial balance anchors. They define the intended direction, relative severity, and accounting discipline. They are not assertions that a named HOI4 modifier directly accepts these units.

## Three linked foundations

Industrial taxation temporarily reallocates usable civilian and military capacity to Britain. It does not delete factories, move buildings between states, or create permanent British factories. Consumer-goods taxation adds a distinct foreign civilian burden and reduces Britain's corresponding burden. Unequal trade changes the price of transactions between Britain and a particular taxpayer, without altering that taxpayer's trade with unrelated countries.

Benefits follow actual charges. Refusing countries, suspended enemies, and countries that have ceased to exist contribute nothing. Native factory transfers must not be rewarded a second time through generated off-map factories or a production bonus representing the same transfer.

## Full-tax assessment anchors

The industrial percentages refer to residual usable capacity after ordinary autonomy and occupation obligations. Consumer-goods entries are percentage-point increases in the country's effective consumer-goods requirement, before capacity safeguards. They are not relative percentage increases.

| Schedule | Civilian capacity | Military capacity | Extra consumer-goods requirement |
|---|---:|---:|---:|
| Baseline independent major | 10% | 5% | 5 percentage points |
| Baseline independent minor | 25% | 15% | 10 percentage points |
| Baseline British dependent | 40% | 25% | 15 percentage points |
| Evolution I independent major | 15% | 10% | 10 percentage points |
| Evolution I independent minor | 35% | 25% | 15 percentage points |
| Evolution I British dependent | 55% | 40% | 20 percentage points |
| Evolution II independent major | 25% | 20% | 15 percentage points |
| Evolution II independent minor | 50% | 40% | 25 percentage points |
| Evolution II British dependent | 70% | 60% | 35 percentage points |

Dependents use their relationship schedule instead of stacking a complete independent schedule underneath it. This is especially important where ordinary puppet mechanics already allocate industry to ENG. Event 81 takes a share of what remains rather than claiming an impossible second copy of the same factory.

## Assessment adjustments

An independent British-led ally receives a five-percentage-point increase to its civilian and military industrial rates and to its consumer-goods assessment. It does not also receive the British-dependent table. This makes forced allied participation consequential while leaving negotiated reduction valuable.

Industrial scale changes the assessment within every schedule, including the British-dependent schedule. A country below 20 combined residual civilian and military factories receives five additional percentage points of industrial tax. A country with at least 100 receives a five-point reduction. The middle band has no adjustment. This is applied to industrial rates only, before other multipliers. Crossing a band changes the next normal assessment, not already quoted project costs.

British relative strength adjusts the resulting tax by a bounded multiplier. A country facing Britain at less than half its own effective strength receives a 0.80 multiplier, broadly comparable strength gives 1.00, and Britain at more than twice its strength gives 1.20. The comparison uses Britain's non-Event-81 economy, land capability, and naval capability against the target. Raw division count alone is insufficient. British revenue does not recursively make its own tax base stronger inside the same calculation.

Within an active tier, each complete 100 Chaos above that tier's threshold adds 5% to the assessment, capped at 10%. The tier anchors are 0, 200, and 400. This bounded adjustment does not activate the next Evolution. Reassessment applies at the next collection review and cannot repeatedly charge a one-off amount for crossing a threshold.

Country type remains meaningful even under extreme combinations. Civilian industrial rates cap at 35% for majors, 65% for independent minors, and 85% for British dependents. Military rates cap at 30%, 55%, and 75%. Extra consumer-goods assessments cap at 15, 35, and 45 percentage points respectively. Native capacity limits may reduce actual collection below these headline caps.

## Reform multipliers

| Consolidated stage | Share of the full assessment retained |
|---|---:|
| Full British Taxation | 100% |
| Reduced Taxation | 70% |
| Limited Taxation | 40% |
| Nominal Taxation | 10% |
| Tax Independence | 0% |

Three reform domains cover industrial claims, consumer assessments, and external trade privileges. A completed project moves its own domain to the next stage's multiplier immediately. Other domains remain at the current stage until addressed. The formal stage advances after all three domains and the consolidation period are complete.

During the final transition, completed domains retain a temporary floor of 5% of the full assessment until final consolidation succeeds. This prevents a country from obtaining a de facto tax-free settlement while abandoning the final step or entering a relationship that blocks Tax Independence. That floor disappears on a valid final completion or hostile exit.

A new Evolution increases the underlying full assessment but does not reset earned domain multipliers. A country at Limited remains at Limited and benefits from the same proportional reduction under the new schedule.

## Preventing impossible civilian bills

Compute a country's ordinary consumer-goods occupation without Event 81. Determine the usable civilian capacity left after that burden and after prior, legitimate ownership and subject claims. Preserve 10% of this remaining capacity against the combination of Event 81 industrial and consumer-goods claims.

First apportion the available taxable space between the two full-schedule claims, before applying any reform multipliers. If the full industrial claim plus the full extra consumer-goods claim exceeds that space, scale both full claims down proportionally. Only then apply each domain's earned reduction. Recovering one domain must not allow another domain to expand into the newly freed capacity. Apply the corresponding smaller British benefit. Do not cap the taxpayer's loss while leaving Britain credited with the uncapped request.

The full-schedule apportionment is recalculated when the ordinary assessment base changes. A reform alone does not recalculate it to refill the space the player has just recovered. The safeguard is proportional, not a universal one-factory minimum. A one-factory economy is not given a total tax exemption merely because it is small. Where native whole-factory allocation cannot represent a fraction, use a verified reversible factory-time accounting method or record that precision as an implementation blocker. Destruction, permanent factory grants, or silent rounding to a different economic rule are not substitutes.

A zero-industry country still has a legal assessment and the applicable trade relationship. It is not assigned negative factories or forced to complete an impossible factory-spending reform.

## British consumer-goods relief

Foreign additional consumer-goods occupation is converted to actual factory-equivalent contributions. Their sum is the maximum Event 81 relief Britain can receive. Relief cannot exceed Britain's own consumer-goods occupation above the native floor. Account for Britain's actual industrial position, including any already transferred industry, before applying the consumer-goods relief itself.

Unused contributions do not become free British factories, stockpiled credits, negative consumer-goods requirements, or a second production bonus. An excessively large tax base can waste some foreign effort after Britain reaches its floor. The tax remains exploitative without creating mathematically unbounded output.

The economic screen should show Britain's consumer-goods occupation decreasing for a real reason. The taxpayer should see its own occupation increase for a real reason. A generic construction bonus with a consumer-goods description would fail this contract.

## Bilateral trade schedule

These entries describe intended price changes, not modifier signs.

| Schedule | Discount when Britain buys from taxpayer | Premium when taxpayer buys from Britain |
|---|---:|---:|
| Baseline major | 10% | 20% |
| Baseline minor | 20% | 35% |
| Baseline British dependent | 30% | 50% |
| Evolution I major | 20% | 35% |
| Evolution I minor | 30% | 50% |
| Evolution I British dependent | 40% | 65% |
| Evolution II major | 30% | 50% |
| Evolution II minor | 40% | 65% |
| Evolution II British dependent | 50% | 80% |

Apply the external-privileges reform multiplier and bounded strength adjustment. Discount caps at 75% and premium caps at 100%. The price must remain positive after interaction with all other systems. British faction membership increases trade leverage through the relationship and inability to leave, without requiring a second hidden global trade penalty.

The two directions are separate. The exporter establishes what the importer pays. A trade-attraction or trade-influence effect is not proof that the price changed. A modifier affecting all British trade does not satisfy the requirement to remove privileges against an individual country that leaves the system.

Normal resource availability, ordinary embargoes, and war still matter. A privileged price does not conjure resources that the seller lacks. A country's own trade with third parties is unchanged by Event 81 unless a specific reform creates a separate, disclosed relationship.

## Expanded schedules

Evolution I activates additional claims and Evolution II strengthens them. All expanded schedules inherit the relevant domain's reform multiplier. A country should not remove its main taxes only to discover that an unrelated permanent Evolution tax has been left behind.

| Expanded claim | Evolution I major / minor / dependent | Evolution II major / minor / dependent | Domain |
|---|---|---|---|
| Naval production levy | 5% / 10% / 15% of usable dockyard output | 10% / 20% / 30% | Industrial |
| Fuel assessment every 90 days | 5% / 10% / 15% of taxable surplus | 10% / 20% / 30% | External privileges |
| Idle-convoy assessment every 90 days | 5% / 10% / 15% of taxable surplus | 10% / 15% / 25% | External privileges |
| Strategic-resource concession ceiling | 5% / 10% / 15% of eligible supply | 10% / 20% / 30% | External privileges |

The stronger military-industry transfer is the military-production tax. Do not also remove finished weapons merely to charge the same military capacity twice. Emergency surcharges can raise an existing industrial claim, but do not invent a second copy of it.

A naval production levy needs a corresponding British naval-production benefit, bounded by actual foreign output lost. It must not transfer ships already built or subsidise nonexistent British dockyards. If Britain cannot use naval output, that channel does not collect. Exact measurable output and a reversible recipient benefit must be proven before implementation, as set out in the coding handoff.

Fuel collection preserves the greater of 30 days of current fuel use and 20% of storage capacity. Britain receives exactly the amount removed, bounded by its available storage. No fuel is debited merely to overflow the recipient's store. Convoy collection uses idle, uncommitted convoys only and preserves the greater of ten convoys and 10% of owned convoys in reserve. Integer remnants stay within the current liability rather than generating a forced one-convoy tax from a zero surplus.

Resource concessions provide actual access to available strategic resources and remove the corresponding portion from the taxpayer's control. Existing concessions, state ownership, and other claims have priority. A whole deposit cannot be granted when it exceeds the agreed ceiling. Where the engine only supports coarser rights, use a verified bounded representation or leave that channel blocked. Preferential purchase prices already implemented by the trade schedule are not a second free resource grant.

## Emergency charges

When Britain is fighting a substantial war, it can initiate one 90-day emergency assessment. This increases applicable industrial and consumer-goods claims by 10% of their current assessed amount. Evolution II allows 20%. A 180-day cooldown begins after the assessment ends. Subjects receive it automatically. Independent countries keep their existing exit and resistance permissions.

An emergency charge and a resistance-pressure surcharge do not multiply or stack without limit. Apply the greater current surcharge, subject to all national caps and capacity safeguards. Britain pays the political cost of initiating an emergency charge even where collection later proves small.

## Assessment rhythm and visibility

Tax status, exit, lost territory, and the existence of ENG update immediately when their consequences require it. Ordinary rate recomputation is no more frequent than a country-owned 30-day review unless its economy has materially changed. Fuel and convoy bills use their 90-day schedule. Project costs are quoted and frozen when the project begins, so a mid-project Evolution cannot demand a surprise second payment.

Display the current actual effects and the next project's expected relief. The category does not ask the player to maintain separate authority, debt, revenue, bargaining, tax-office, and resistance meters. The hidden account exists to make the visible taxes correct.
