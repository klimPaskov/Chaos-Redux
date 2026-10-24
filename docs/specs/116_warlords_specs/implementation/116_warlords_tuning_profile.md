# Warlords 116: proposed starting tuning profile

This appendix makes the planning baseline numerically reviewable. Every number here is proposed initial balance, except the user-fixed event identity, Chaos entry level 1, and strict terminal Chaos greater than 1000. It is not an allocation of script identifiers or a claim that the engine supports an exact proposed observation.

The gameplay parts own the causal rules. If numerical tuning later changes, update this profile and the affected design statements together. No tuning adjustment may waive actual identity, real assets, viable countries, campaign-linked submission, effective command, or the shared world-end gates.

## Birth and continuation

| Parameter | Starting value or band | Scaling and limit |
| --- | --- | --- |
| Ordinary parent geography | 6 eligible states normally | Equivalent large-state profile only when both real capacity tests pass |
| Ordinary parent accessible population | 6,000 in population-thousands units | Only the valid owned/controlled capital component counts |
| New state's accessible population | 800 normally, 2,000 for large single-state exception | Population alone cannot replace industry, an actual supplier, forces, or supply |
| Remaining parent | 3 connected states, 3,000 population-thousands, 6 usable factories including a military factory | Recompute actual surviving capital component after each cut |
| Baseline territory | Aim roughly 12 to 25 percent of usable local base, normal ceiling 25 percent of current eligible footprint | Geographic rounding and the explicit large-state exception require full viability recheck |
| Stronger territory | Ceiling 35 percent of current eligible footprint | No mandatory attempt to reach the ceiling |
| Baseline field-manpower request | 6 to 18 percent of current parent field manpower, hard ceiling 25 percent | Actual eligible local formations, parent reserve, and supply constrain it |
| Stronger field-manpower request | 12 to 28 percent, hard ceiling 35 percent | Current assets, not original pre-fragmentation strength |
| Additional stock reserve | Baseline at most 10 percent of compatible free parent stock, stronger at most 20 percent | Only an accepted seized/transferred stock manifest, after parent replacement reserves, no presumed exact physical depot location from abstract native national stock |
| Stage I/II anchors | 200 /400 Chaos, pending proper tier registration | At most one stage per tier, no activation Chaos |
| Continuation warning |120 days normally, ordinary floor 90 | Command size, instability, administrative reach, and actual support change duration within the documented profile |
| Minimum spacing between births |120 days | Applies to ordinary continuation, not secretly bypassed by a second queue |
| Eligible continuation timing anchor | About 180 days | Actual MTTH depends on the full eligible state and cadence, not claimed exact before probability analysis |
| New-creation capacity | Small 2, substantial 4, very large 6, hard configurable upper ceiling 8 | Viability usually binds first, existing acknowledged actors are never deleted by the cap |

One optional initial request model uses four bounded inputs from current facts. Let A describe actual founder ability, S the parent's usable size, I verified instability, and L the eligible local military concentration, each normalized to 0 through 1 by a documented owner profile. Use a starting quality request q =0.25A +0.20S +0.30I +0.25L. Baseline field share is 0.06 +0.12q. Stronger share is 0.12 +0.16q. This is a proposed request formula, not a guarantee or a general-selection weight.

For an initial transparent normalization, ability can use the observed native skill range, size can interpolate between the minimum eligible capacity and a substantially larger parent, and local concentration can compare actually eligible regional manpower to the parent's current field force. Instability needs exact native or registered-owner facts. Missing optional evidence contributes nothing rather than an invented severe crisis. The implementer must document normalization, source units, and rounding before balance comparisons are meaningful.

Select actual formations near the requested band without crossing hard ceilings or reducing either country below viability. Do not split a division's bookkeeping or round up a large formation if its exact custody cannot be preserved. Stock already in those divisions is not also part of the extra reserve. A physically unavailable equipment class contributes zero.

## Command Cohesion: initialization and authority

116 owns one 0-to 100 value for an ordinary active warlord.067 owns that same displayed value after an acknowledged takeover. Preserve current amount, pending cause receipts, and history across authority handover. The rules below are 116's proposed baseline. A shared 067 contribution must be accepted by 067 and combined with its actual mechanics without duplicate application.

A starting formula is C0 = clamp(35,65,45 +8A +6L +6R -10I -8X), where A,L,I use the current birth factors above, R describes proved supply/replacement readiness from 0 to 1, and X describes current incompatible command obligations from 0 to 1. Ordinary country statistics remain native facts. These normalized inputs are private calculations, not new public meters. If a necessary input is unknown, the relevant operation cannot pretend it is a favorable value.

| Current band | Proposed 116-only mechanical expression | Constraints |
| --- | --- | --- |
|75 to 100 | Up to 10 percent better planning preparation and 5 percent organization recovery | No combat invulnerability, no free equipment or army control |
|45 to 74 | Normal coordination | Functional country does not require a repeated maintenance click |
|20 to 44 | About 10 percent slower planning and 5 percent slower organization recovery | Actual mission and political responses remain available |
|0 to 19 | About 20 percent slower planning and 10 percent slower recovery, stronger eligible command-crisis pressure | No automatic country spawn, army deletion, forced defeat, or threshold-only coup |

The installed modifier names and interactions require verification. Use one owned dynamic expression or transform the proper command idea, without multiplying the same penalty through several spirits. Do not overwrite 067's existing expression unilaterally.

## Cohesion causes and scheduling

| Cause | Starting change | Proof and repeat rule |
| --- | --- | --- |
| Completed security or supply restoration for a meaningful command | +3 to+6 | Performed mission, exact affected command and cause, no repeat reward for merely reselecting the same route |
| A significant campaign succeeds under the current command | +4 to+8 | Real campaign and material result, once per campaign phase and actual actor lineage |
| A rival's surviving command is durably integrated | +3 to+7 | Performed current/future command settlement, once for the distinct integration milestone |
| Institutional or civilian settlement is performed | +4 to+8 where active Cohesion remains relevant | Old privileges actually surrendered, one constitution transition receipt |
| Stable supplied administration without active breach for a full 30-day interval | +2 up to a passive ceiling 65 | Registered actual country only, no completed-action click, stops above the ceiling or when the conditions fail |
| Serious supply or replacement deficiency persists for 30 days | -1 to-4 per unresolved 30-day interval | Actual material severity and affected military share, ends when the deficiency ends |
| Significant failed campaign or major encirclement | -4 to-10 | Actual losses and strategic effect, no separate penalty for every notification of the same event |
| Required command route or substantial subordinate is lost | -4 to-12 | Current capacity affected, one cause can invalidate many dependencies without repeating this whole penalty |
| Important compact or patron obligation is actually breached | -3 to-8 | Performed breach, attributable actor and contract, no punishment for refusing an unsigned offer |
| Capital and central staff are materially lost | -10 to-20 | Major actual command disruption, once per distinct unresolved capital-loss episode |

Immediate material events enqueue one cause receipt and invalidate current proof immediately where needed. A proposed periodic service would apply sustained conditions and passive recovery only to registered active countries. Do not implement it through `on_daily`, `on_weekly`, or `on_monthly` without explicit user authorization, because those hooks iterate over all countries by default. Prefer owner callbacks or a specifically authorized bounded active-record dispatcher. It is not a monthly resource-payment chore; if a recurring world-wide pass is indispensable, leave it unresolved pending explicit authorization. Ordinary cause changes have a rolling 30-day net cap of 12 in either direction. A distinct catastrophic capital/staff loss can exceed the ordinary negative cap once, with explicit receipt and no repeated catastrophe tick.

Scale changes by the affected share of current usable forces, population, industry, or routes as appropriate to the cause. Clamp the value to 0 through 100. A single native loss may have both a coordination consequence and its ordinary war consequence, but the separate Chaos ledger still uses its own one-cause overlap guards. Zero Cohesion without a viable independent command yields disruption and political choices, not free fragmentation.

## Action-to-price and timing map

These entries map every action in Part 12 to a starting payable plan. Fees are quoted through the shared framework. Native war, recruitment, construction, trade, and aid keep their own real costs. Event fees never substitute for native material payment. Durations are ordinary planning anchors and scale by the declared family factors in Part 12. Cooldowns do not reset paid receipts or permit a duplicate milestone.

| Action | Starting event fee and physical commitment | Duration / repeat boundary |
| --- | --- | --- |
| P01 security |35 PP,1 civilian-factory equivalent, real appropriate security cohort |90 to 120 days, one live assignment per exact target, repeat after a new material need and at least 90 days |
| P02 administration |45 PP,2 civilian-factory equivalents, actual affected command and support plan |120 days, scale 90 to 150, one live obligation per command |
| P03 reassignment |30 CP, actual lawful available appointment | Appointment occurs through actual owner,60-day same-command repeat guard, no material grant |
| P04 warned negotiation |60 PP upon accepted agreement, plus its explicit performed concession or delivery | Uses remaining warning and a normally 120-day settlement where possible, one contract per actual warning |
| P05 detention |25 CP and 60 PP, actual reachable person and credible security force | One attempt per actual warning unless a genuinely new custody opportunity arises, no artificial short ordinary containment deadline |
| P06 recovery offensive |40 CP,1 civilian-factory equivalent for logistical preparation, actual field army/front | About 90 days preparation or performed equivalent, one active plan per actual front |
| P07 reintegration/partition |75 PP at accepted binding agreement, explicit military and territorial concessions |120 to 180-day performance/hold, no fee on an unaccepted proposal |
| P08 reconstruction/veterans |50 PP,2 civilian-factory equivalents, actual site or accounted cohort |180 days, once per completed work package, a later different loss needs a new cause |
| W01 founding reserve |25 CP and the actual cohort's native training/supply costs |90-day program,180-day same-cohort repeat guard, no recreated experience |
| W02 recruitment program |20 PP for an optional staff program, then ordinary native recruitment with full manpower/equipment/time | Normal recruitment is always available, one optional program per actual cohort, no instant custom unit grant |
| W03 arsenal/transport |40 PP and 1 to 2 civilian-factory equivalents or an accepted native construction equivalent |120 to 180 days by damage/distance, named site and one active project |
| W04 patron contract |20 PP after accepted negotiation, plus exact mutually agreed deliveries/rights | Normally 90 to 180-day delivery horizon, one live identical contract, distinct compatible donors allowed |
| W05 civil compact |75 PP, specified recruitment/administrative rights surrendered |180-day performance, one constitution transition rather than a repeatable bonus |
| W06 staff/succession |45 PP and 15 CP for appointments, real eligible staff/institution |90-day reform, role-specific 60-day appointment guard, broad training remains separately paid |
| W07 civilian handover |100 PP,2 civilian-factory equivalents, actual institutional and military handover |180 days, one current transition, failed or completed history cannot restart grants |
| W08 rival policy |35 PP for an accepted treaty or 40 CP for a special campaign preparation, actual corresponding concession or army | Choose the declared variant,120 to 180-day agreement or normal war, no combined free annexation |
| F01 recognition/mediation |25 PP for actual diplomatic work |180-day same-relationship guard, pure administration exception, no force grant |
| F02 material or native military aid |Starting cargo 1,000 infantry equipment and 100 support equipment if appropriate, actual transport and sender stocks, or the native volunteer system | Delivery time by route,90-day identical shipment scheduling guard unless a genuine contracted installment, exact variants and losses |
| F03 intervention |Native lawful diplomatic/war costs and actual deployed military commitment | Ordinary war timing, no scripted conquest or global access, one entry receipt |
| F04 independence support |40 PP plus the declared real cargo/transport within the four-type limit, actual viable recipient |Normally 120-day operation, no second current claim on the same cargo or recipient opportunity |
| G01 unification campaign |40 CP,2 civilian-factory equivalents for preparation, actual Generalissimo-led army and front |About 120 days preparation/integration of logistics, normal warfare decides submission |
| G02 military submission |75 PP and actual enforceable transfer of authority under campaign-linked terms |120 to 180-day performance, one current agreement per rival lineage |
| G03 integration |60 PP,2 civilian-factory equivalents, exact surviving assets and lawful command appointments |180 days, one unique integration milestone with no release-reconquer reward reset |
| G04 political formation |100 PP after all performed material integration and domestic proof |One identity milestone, paid administration does not replace prior campaigns or create a world end |
| G05 theater program |50 PP,3 civilian-factory equivalents, actual controlled command center, armies, and route |180 days, named theater and nonduplicated capacity |
| G06 readiness examination |No resource fee, authoritative read-only evidence job |Normally 14-day repeat spacing while unchanged, important invalidation can request a fresh examination without restoring lost proof |
| G07 reconstitution |60 PP,2 civilian-factory equivalents and actual recovery of the lost command |180-day required consolidation, no second formation reward |
| O01 defense coordination |40 PP,1 civilian-factory equivalent for agreed support, actual access/forces/partners |120-day program, compatible obligations only, no automatic faction |
| O02 liberation |Native campaign costs or the separately declared F04 support contract |Ordinary warfare and actual independence, no pay-to-free instant action |

The listed optional staff or diplomatic fees are not a mandatory toll on native recruitment, construction, or diplomacy already available to the country. They pay for an additional declared program or agreement. If a proposed fee purchases no distinct useful activity, remove that fee during implementation review rather than disguising an ordinary UI link as a mechanic.

A native training queue may need several real equipment types. Do not invent a bundled token that hides or discounts those costs. Any separate event payment remains within four spendable types and the compact display rule. Equipment and manpower needed by the actual native template remain visible and payable in the native interface.

## Political and terminal anchors

| Parameter | Starting anchor |
| --- | --- |
| Domestic consolidation |180 continuous days after all current relevant rivals have campaign-linked submission and real control |
| Functional domestic Cohesion |At least 45 as the starting formation floor, through the current owner |
| Domestic formation spectacle |Three substantial rival commands integrated, or an established major root with 30 usable military factories, plus actual formation |
| Qualifying foreign powers |4 distinct current independent-origin great-power lineages, campaigns after formation, spread across 3 macroregions |
| Later-emerging equivalent great power |At least 10 percent of baseline world usable military industry before its campaign, independent armed government and geographic base |
| Regional anchors |4 macroregions, each with actual command/supply and either 5 million governed people or 10 usable factories |
| Industry share |55 percent of the greater of baseline and current valid world capacity |
| Governed population share |40 percent of the greater of baseline and current valid world population |
| Comparative effective field strength |At least 1.25 times all outside independent armed opposition in the valid comparison cohort |
| Replacement horizon |Approximately 90 days of critical real consumption, with a nonzero minimum operating requirement appropriate to actual forces |
| International consolidation |180 continuous days of complete current proof |
| Terminal Chaos and settings |Strictly greater than 1000, global world ends enabled, own branch enabled, no other active/winning terminal claim |

The two consolidation periods serve different accomplishments. They are not Chaos evolution timers. If domestic unity and international readiness are both being reconstituted after a later loss, their valid sustained intervals may run concurrently when all their separate facts are true. They cannot backdate across an interruption.

## AI and balance calibration

Compare complete action pools in the named Part 13 scenarios. Infeasible options have zero weight. Feasible defense, replacement, and survival options must not starve beneath repeated prestige or expansion actions. Suggested initial relative priority bands are high 100, normal 50, opportunistic 20, and rare 5. These are relative weights for an otherwise eligible comparable action pool, not final probabilities and not a substitute for route-specific factors.

Scale affordability, time, ambition, aid, and willingness with actual resources, threat, geography, political constitution, and opportunity cost. Validate any ordinal or numeric military estimate against known fixtures. Record the exact normalization and cadence for probability comparisons. Keep a before copy before changing balance and report bounded or sampled results honestly.

This profile needs actual campaign tuning. It is complete enough to expose its assumptions and conflicts. It must not be labeled tested balance until the relevant simulations and user-run campaigns have been performed.
