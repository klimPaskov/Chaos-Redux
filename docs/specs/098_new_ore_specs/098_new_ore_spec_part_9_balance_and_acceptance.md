# New Ore, part 9: Tuning, behavior, and acceptance

## What a successful campaign should feel like

The first deposit should immediately change the military importance of its state. A controller can plan an armored offensive around it, but also has a reason to defend a territory that its ordinary economy might never have justified. A customer can obtain a strong foreign benefit without conquering the world. A denied rival can choose alternatives, seek another supplier, develop normal counters, or eventually commit to an ore war.

The event is allowed to be extremely powerful. Balance work must tune opportunity, scarcity, diplomatic cost, and reaction. It must not reduce the direct baseline below a real 50% armor improvement or quietly confine that improvement to future tanks. The intended strategic counterplay comes from the vulnerability of the source, weaker foreign access, other countries' responses, and the game's ordinary limits on an armored force.

The accepted armor targets are exact gameplay promises. Timing, costs, and AI scoring below are starting calibration values that can be adjusted after named scenario evidence. A tuning adjustment must explain the campaign behavior it changes and preserve the identity and user requirements.

## Effective armor examples

Let `A0` be an applicable armor value with all non-098 conditions unchanged, including Event 028, design bonuses, technology, organizations, formation composition, and other active modifiers. Let `A098` be the same value with the valid ore entitlement. The planned result is `A098 >= A0 × (1 + D)` for direct access and the corresponding stated foreign multiplier. Visual display rounding does not authorize rounding gameplay below the floor.

| A0 | Entitlement | Minimum A098 | Meaning |
| ---: | --- | ---: | --- |
| 100 | One baseline direct deposit | 150 | Required initial 50% improvement |
| 100 | Deep Vein direct access | 175 | Stronger original material |
| 100 | Baseline foreign access | 120 | Useful selected access |
| 100 | Deep Vein foreign access | 130 | Improved selected access |
| 100 | One Super-Alloy deposit | 300 | Three times otherwise equivalent armor |
| 100 | Two Super-Alloy deposits | 350 | First diminishing additional gain |
| 100 | Three Super-Alloy deposits | 366.666… | Smaller next gain |
| 100 | Super-Alloy foreign access | 180 | Still below every direct Super-Alloy holder |
| 200, including independent asteroid benefit | Baseline direct ore | 300 | The ore requirement still holds with the asteroid active |
| 0 | Any ore entitlement | 0 | Ore does not invent an armor statistic where none exists |

An additive engine modifier requires special attention. If a base armor of 100 already has an unrelated +50% modifier, its ore-free value is 150. Adding another raw +50% to the same additive bucket would produce 200, only a 33.33% increase over 150. That fails the requested effective baseline. A stronger fixed additive constant also cannot guarantee the floor when other contributions are unbounded. The implementation needs a verified independent multiplier or a correctly scoped compensating calculation, with complete consumer coverage.

## Dynamic tuning rules

Relevant force strength means actual positive-armor forces and their current equipment. For contract pricing, relevant production capacity is the country's controlled military factories plus controlled dockyards, counted once each. These are facilities capable of military equipment production, regardless of their current queue assignment. Civilian industry is excluded. Changing production lines immediately before confirmation therefore cannot produce an artificial small-country price.

The square-root equipment price factor in part 3 is `clamp(0.5, 3.0, sqrt(relevant production capacity / 25))`. The lower bound applies to a country with no present armored production, so importing ore is still possible. It does not exempt the recipient from affording the actual stock and adaptation cost.

| Dynamic element | Proposed reproducible calibration |
| --- | --- |
| Adaptation effort | Start with the chosen 15 XP or faction 10 XP anchor. At least 10 equipped armored divisions or 5 deployed armored capital ships gives a 1.25 force factor. A country below both uses 1.0 |
| Prior ore experience | A completed or currently successful prior access episode of at least 90 days gives a 0.75 factor. An interrupted proposal or a one-day deal does not qualify |
| New Super-Alloy customer | First ever practical ore access after Super-Alloy uses a 1.2 factor. Combine eligible effort factors and clamp their product to 0.75–1.5 |
| Continuous renewal | No adaptation cost. Pay the equipment quote for the new period. A real gap returns to the adaptation rule with any earned experience retained |
| Stable contract term | Add 60 days to the family anchor when parties have had no bilateral war or broken ore deal for 720 days, and a prior agreement of at least 180 days completed successfully |
| Exposed contract term | Subtract 60 days for an active enemy land front in the source state or an active credible ore demand against the supplier. This can offset the stability increase |
| Maximum and minimum term | Clamp to 120–360 days and round to 30-day increments. A supplier's one shorter counteroffer subtracts a further 30 days within the same bounds |
| Ordinary offer deadline | 14 days. Use 7 if either party is presently fighting over the named source, and 21 if both are peaceful and no direct land or practical naval route connects them. Otherwise retain 14 |
| Rejection memory | 60 days at peace without a prior broken deal. Use 120 during bilateral hostility or the specified supplier reliability memory |
| Demand attention | 75 PP and 25 CP anchors. A valid relevant claim gives a 0.8 factor. A practical distant naval route gives 1.25. Clamp PP to 50–150 and CP to 15–50 after the event's ordinary factors |
| Demand reply | 21 days. Use 14 for an active enemy approach to the source and 30 for a credible distant naval claimant without a current local front |
| Defense commitment | 180 days. Use 120 when defending a source already bordering an active enemy front and 270 when defending against a credible preparation that has not produced a local war |
| Defense attention and reward | CP starts at 20, scaled by square root of the relevant defended force relative to 8 qualified divisions or 4 armored capital ships, bounded 10–40. Success XP starts at 25 with the same force factor, bounded 15–40. Use the relevant Army or Navy branch |

The production factor reflects the military customer's actual industrial capacity. Prices cannot change after confirmation merely because production was reassigned. At confirmation, use the current controlled military factories and dockyards and show the current quote. Real loss or acquisition of industrial territory can change a later price. A player cannot receive an undiscounted equipment grant while paying a discounted cost.

An existing foreign customer that qualifies through naval strength can choose the naval adaptation branch. A country meeting both Army and Navy paths chooses one eligible cost and receives the same foreign armor entitlement. The XP path does not split ore into separate land and sea licences.

## Evolution pacing definitions

The day values in part 2 are reference intervals for the project's shared MTTH system. They are not observed averages, hard deadlines, or a promise of a particular probability without the system's verified distribution. Before implementation, identify whether the selected helper treats a configured interval as a mean, median, hazard parameter, or sampled waiting-time anchor. Preserve the intended envelope and report measured opportunity and completion probabilities in that vocabulary.

Use the following concrete qualifying conditions for the part 2 factors:

| Track | Accelerating conditions, each counted once | Slowing condition |
| --- | --- | --- |
| Deep Vein | Original site has had continuous valid ore control for 180 days, at least one foreign agreement has delivered access for 90 days, and an active 029 operation genuinely coexists in the original state. Each independently qualifies for 0.8 | First 30 days after initial discovery uses 1.25 |
| First New Deposits | Chaos is at least 600 and Deep Vein has manifested. Each gives 0.8 | First 30 days after initial discovery uses 1.25 |
| Ore Wars | At least two independent ore controllers, at least two independent countries with substantial armored forces and no secure access, or a genuine ore refusal in the last 90 days. Each independent condition gives 0.8 | First 30 days after initial discovery uses 1.25 |
| Super-Alloy | Any direct controller has maintained a valid source for 365 days, and at least three countries have delivered valid direct or foreign access for 90 days. Each gives 0.8 | First 30 days after initial discovery uses 1.25 |

Substantial force for this pacing table means at least 10 equipped armored divisions or 5 deployed armored capital ships, using the same substantive equipment requirements as the achievement family. It is a calibration threshold for a military society ready to exploit ore, not an eligibility restriction on direct armor.

Clamp after combining the declared factors. Additional-deposit pacing uses its own exact formula from part 2 and does not also inherit the first New Deposits modifiers. Count geographic discoveries globally even when one controller owns several states. Paused eligibility preserves earned waiting progress as specified in part 8.

## AI behavior scenarios

The main AI matrix is in part 4. These scenario expectations turn its prose into reviewable comparative behavior. They are relative priorities within the actual legal action pool, not invented exact chances of war.

| Scenario ID | Situation | Expected preference and forbidden result |
| --- | --- | --- |
| AI-01 | Armored major, no ore, affordable peaceful supplier, no credible invasion route | Commercial or useful security access ranks above aggression. No war path receives weight if it is illegal or unreachable |
| AI-02 | Threatened minor supplier, strong protective partner, hostile higher-paying rival | Protection can outweigh the premium equipment offer. The highest numerical payment must not always win |
| AI-03 | Major with secure foreign access, supplier under attack | Defending the source or maintaining access ranks above provoking that supplier |
| AI-04 | Capable adjacent denied rival at 599 Chaos | Ordinary diplomacy and existing warfare remain available, but no Evolution III demand or preparation is created |
| AI-05 | Same rival after Ore Wars manifests | A credible demand becomes meaningful. Refusal increases preparation interest without bypassing ordinary declaration rules |
| AI-06 | Distant landlocked minor without relevant force or access to the source | No fictitious invasion or ruinous automatic premium purchase. It may wait, develop ordinary capability, or decline involvement |
| AI-07 | Current supplier discovers a second deposit before Super-Alloy | Gains resilience and export capacity. It does not mistakenly anticipate a higher current direct armor stat |
| AI-08 | A new independent supplier appears | Potential customers compare new lawful offers. The old supplier adjusts future terms without cancelling successful existing deals automatically |
| AI-09 | Super-Alloy holder has two sources, rivals depend on one | Defend both materially useful sources and recognize their different exposure. Capturing a second source receives less marginal armor value than obtaining the first |
| AI-10 | World Claims participant claims ore but has no feasible route | Claim raises political interest but does not manufacture access, occupation, or a legal demand through invalid relations |
| AI-11 | Human has never opened or selected an ore map state | AI still discovers, compares, offers, responds, and targets through its own registered candidate set |
| AI-12 | Supplier caused a paid-security qualification loss | Honor the existing protected paid term. Do not farm another upfront fee for restoring the same period |
| AI-13 | Accepted demand becomes unaffordable before confirmation | Close the uncompleted acceptance. Do not classify the supplier as refusing |
| AI-14 | Two foreign agreements exist and the stronger source falls | Switch to the valid remaining foreign tier immediately. Do not buy a third source outside the two-contract limit |
| AI-15 | A refusal cools into a completed independent peace | Remove event-owned escalation pressures while preserving unrelated strategic objectives |

The probability auditor must inspect complete candidate pools before evaluating exact shares. Uniform state selection has a design probability of `1/N` over the N valid states at the committed draw. A country-first draw fails even if it appears random. Disabled, invalid, full, unaffordable, or legally impossible options must contribute zero wherever those conditions are absolute.

Use matched before and after snapshots for threshold and control changes. Sweep relevant Chaos values, country force levels, distance/reach, relation validity, price factors, slot counts, and refusal memory. Report dominance, starvation of peaceful access, concentration in a few actors, and the effect of missing targets. A partial pool is useful for local ranking but cannot establish global percentages.

## Acceptance matrix

These are future implementation tests. The planning pass establishes expected outcomes and analytical consistency. It does not claim native gameplay, asset, save, or probability tests have run.

| Test | Concrete setup | Pass condition |
| --- | --- | --- |
| A01 | Global eligible pool split among countries with very unequal state counts | Every eligible state has one equal share. No country-first weighting |
| A02 | Valid pool includes minors, majors, occupied territory, remote islands, and low-industry states | All structurally valid states remain eligible regardless of usefulness |
| A03 | No valid controlled land state at the attempted initial firing | No false discovery, original identity, reward, log success, or consumed fire-once result |
| A04 | First firing at Chaos 199, 400, 800, and 1000+ | Exactly one initial baseline deposit in each case, enabled evolutions enter their own pacing |
| A05 | Owner and controller differ at discovery | Actual controller alone receives direct access |
| A06 | Baseline reference armor 100 with no unrelated bonus | Applicable armor is at least 150 |
| A07 | Same consumer with positive, negative, and very large unrelated modifiers | Effective paired improvement remains at least 50%, preserving unrelated contributions |
| A08 | Old fielded equipment, old stock, new production, and new deployment | Every applicable case receives the current ratio without replacement-only delay |
| A09 | Conventional land armor plus armored cars, mechanized, modules, and naval armor where positive | The complete supported consumer inventory passes its actual stat comparison |
| A10 | Africa elephant equipment, intrinsic elephant subunit armor, and coal golem armor | Custom positive contributions are covered once and broad scope does not depend on the legacy armor equipment category |
| A11 | Armor-zero units and aircraft with only air defense | No invented armor or substitution of an unrelated defensive statistic |
| A12 | Captured, imported, lend-leased, and sold equipment | Benefit follows the new current beneficiary's entitlement, with no permanent exported ore grade |
| A13 | Volunteers and expeditionaries under foreign command | Verified native application matches the legal force owner's intended access |
| A14 | Capture changes A to B while combat is possible | Old and new contributions change before the next applicable combat-stat evaluation |
| A15 | A holds two Super-Alloy deposits then loses one | Its bonus changes from +250% to +200%, preserving the other deposit |
| A16 | Last direct source falls but another supplier's valid contract remains | Former controller immediately receives its valid weaker foreign tier |
| A17 | Annexation, release, puppet transition, liberation, civil war, and peace | Only actual live controllers benefit and no country identity inherits stale source agreements |
| A18 | Repeated control and relationship callbacks | No duplicate benefit, payment, termination, refund, milestone, or achievement progress |
| A19 | Foreign country holds two agreements | Uses one strongest foreign tier. A third agreement and duplicate source are rejected |
| A20 | Supplier and source export limits reached | Confirmation cannot overbook a deposit or exceed six distinct foreign customers |
| A21 | Fresh quote with stock or XP one unit below, exactly equal to, and above required amount | Below is rejected, equality succeeds, and actual paid receipt matches the displayed scaled quote |
| A22 | Cost factors cross rounding and discount boundaries | Whole-unit quote, affordability, debit, and credit agree. Shared helpers pass their own exact-boundary proof |
| A23 | Partial payment or scope invalidation during activation | Restore only actual paid components once, leave no benefit or occupied place |
| A24 | Supplier buyback before, during, and after an early-renewal period | Sum exact unused actual equipment payments, require supplier stock, preserve adaptation expenditure |
| A25 | Native pact loss caused by supplier, recipient, or unknown actor | Protected paid term survives supplier or unknown non-hostile fault. Proven recipient breach terminates as specified |
| A26 | Source captured, parties start war, supplier arranges a peaceful sale/cession, or another non-hostile native transfer ends prepaid delivery | Current/future periods follow the exact risk rule. Event-controlled voluntary transfers settle real unused receipts first. Other unsettled non-hostile transfers impose supplier-wide AI prepaid rejection for 720 days. Reacquisition, unrelated war, another source, or premium offers cannot bypass it |
| A27 | Accepted demand loses affordability, capacity, or qualification | No agreement and no supplier-refusal credit. Delivered attention stays spent |
| A28 | Refused demand before legal declaration and after peaceful settlement | Exact event-owned preparation is created or cleaned up without deleting independent native goals |
| A29 | Deposit changes between demand creation, reply, and war preparation | Target and consequence follow the frozen episode's real validity. No stale declaration against a new supplier |
| A30 | Ore Wars AI at a reachable state and an unreachable state | Real native state objectives affect planning where feasible. Generic country hostility alone is insufficient evidence |
| A31 | Defense mission succeeds, loses source, loses threat, or receives duplicate completion | Correct XP or neutral cancellation, once-only reward, continuous time and force commitment |
| A32 | Each evolution threshold one below, equal, and above | Correct eligibility and timing, with zero Chaos for activation alone |
| A33 | All 16 combinations of four evolution toggles | Independent enabled tracks work, later tracks do not require disabled predecessors |
| A34 | Chaos falls or a pending evolution is disabled then restored | Earned waiting progress pauses and resumes. Manifested benefits remain |
| A35 | New Deposits chooses repeatedly until scarcity ceiling or pool exhaustion | Unique globally random sites, exact count, bounded cadence, truthful waiting and no fixed country list |
| A36 | Super-Alloy source counts 1 through 12 and compatibility counts above 12 | Monotonic diminishing gains below +300% from count, with no discontinuity or loss below sole-source floor |
| A37 | Ore and 029 mine in same state versus separate states | Only true same-state connection changes its defined negotiation or priority conditions. Separate ledgers remain intact |
| A38 | 092 actual marketed lot includes ore, excludes ore, transfers title only, or is cancelled | Price connection follows exact lot. Armor follows actual control only. No false sale achievement |
| A39 | 086 claimant before and after ore discovery, with and without a live claim | Actual claimant interest changes without granting armor, cores, or fabricated claims |
| A40 | 028 main mineral, fragments, ore alone, and both sources together | Explicit separate composition preserves Event 028 and the 098 effective ratio. Source loss removes only its own contribution |
| A41 | Chaos milestone replay, capture cycles, labels, generic war hooks, and later peace | Only part 5 consequences count once. The theoretical event-specific positive maximum at 12 deposits is 52 |
| A42 | Each achievement at threshold minus one day, at threshold, with interruption, and in a debug context | Exact sustained conditions, correct resets, no tag/subject/empty-unit shortcut or debug unlock |
| A43 | Save/reload at pending proposal, paid term, early renewal, active demand, paused evolution, and achievement hold | Dates, receipts, sources, and results remain equivalent. No reroll or restarted full delay |
| A44 | Legacy one-site save and deliberately inconsistent legacy state markers | Valid single site migrates correctly. Ambiguity is reported and resolved explicitly without free deposits |
| A45 | All ordinary views, options, disabled tooltips, state rows, and log/details states | Real controller, source, actual benefit, expiry, exact costs, and consequences match gameplay. Working labels are not shipped as final copy |
| A46 | Each planned asset in source, processed PNG, final DDS, and native consumer | Correct family, native dimensions, alpha, state ordering, original sources, manifest and reviewed final rendering |
| A47 | First operational Super-Alloy with different human countries and repeat callbacks | One factual world presentation and +10 receipt, researched final text/audio, settings respected |
| A48 | Owner API caller with changing ROOT/FROM, zero output, nested calls, and stale private temporary fields | Explicit scoped result and zero-path initialization, no stale actor, state, payment, or benefit |
| A49 | Normal and debug initialization across loaded campaigns | Public Event 098 routing stays compatible, idempotent startup registration, no periodic global repair loop |
| A50 | Catalog, details, event log, enabled controls, probability names, achievements, docs and assets | All align with implemented truth, with the workbook updated through its owner only after actual acceptance |

## Release decision

The later implementation is complete only when its actual files satisfy the accepted design and its required evidence is available. A code parser pass cannot establish final armor, transfer timing, native UI, AI strategy influence, or save continuity by itself.

Record each acceptance row as passed with evidence, failed with a concrete cause, or blocked by an identified unavailable capability. Fix design-preserving implementation problems and rerun the affected rows. Broaden testing only when a real dependency or regression requires it. Do not call a blocked broad-armor implementation playable.

During implementation, keep the required route-coverage table aligned with the core, each evolution, three agreement families, monopoly, protected paid term, renewal, source reassignment, demand/refusal/settlement, defense commitment, four connections, eight achievements, and the operational super-event. Each row names the implementation consumer and evidence. The table should make a missing route visible without multiplying gameplay systems.
