# 18. Achievements

## Shared rules

The twelve `tp85_*` keys are semantic IDs; the implementer maps each to a collision-free registry ID after checking the achievement registry.
Labels are title directions, not final localisation.

Terms used below:

- **Opening population**: the country's population in controlled states at the episode's first Blood onset, fixed for the episode.
- **Episode deaths**: applied Deaths entries in the country's controlled states correlated with the episode, from every owner (Part 13).
- **Passover coverage**: the share of the country's population living in Prepared states at the final deadline (Part 7).
- **Full objective**: a full success of a Part 14 action, counted once per phase.

Annexation, release, tag changes, migration and deaths cannot shrink a fixed denominator or create new eligibility.
Debug resets, forced phase skips, administrative population restoration and receipt manipulation invalidate survival achievements for the episode; ordinary save and load does not.
No achievement rewards killing civilians or maximizing the death toll.
"Manual" below means a SCN-032 launch; each entry states whether it qualifies.

## 1. `tp85_through_ten`

**Direction:** careful national survival through the whole sequence.
**Eligibility:** natural episodes only; present at Blood onset.
**Unlock:** complete all ten plagues; Wrath stays at or below 50 from Boils onset through the final night; Passover coverage at least 90%; episode deaths at most 5% of opening population.
**Difficulty:** hard, visible.
**Icon:** a repaired doorway with ten discreet marks around it.

## 2. `tp85_small_country_served`

**Direction:** a small country survives through its own local organization.
**Eligibility:** natural, Low or Medium episodes; opening population at most five million and at most five civilian factories at Blood onset.
**Unlock:** full objectives through the local-organization variant in at least five distinct phases; complete the sequence; Passover coverage at least 80%; Wrath at most 25 at the final night; episode deaths at most 5% of opening population.
**Disqualifier:** counted objectives completed through a road, sea or rail variant or paid by a foreign pledge.
**Difficulty:** hard, visible.
**Icon:** a small civic shelter held up by joined hands.

## 3. `tp85_late_heeding`

**Direction:** a government changes course after hardening its heart.
**Eligibility:** natural or manual episodes.
**Unlock:** choose Harden Our Hearts in at least two phases before Livestock and reach Wrath 60 or more; then complete full objectives in at least three later phases without hardening again; enter Darkness at Wrath 25 or less; Passover coverage at least 90%.
**Difficulty:** hard, hidden until the hardening condition is met.
**Icon:** a cracked stone heart beside a lit doorway.

## 4. `tp85_beyond_borders`

**Direction:** protect foreign civilians while keeping a credible response at home.
**Eligibility:** natural or manual episodes.
**Unlock:** Foreign Relief Pledges completed for three different countries in at least three different phases; Passover coverage at least 80%; Wrath at most 25 at the final night.
**Disqualifier:** a recipient created by a release during the episode.
**Difficulty:** hard, visible.
**Icon:** three shelters linked by a relief crate and route.

## 5. `tp85_protected_exodus`

**Direction:** receive the displaced and protect them through the final night.
**Eligibility:** natural, High or Maximum episodes with the Exodus active.
**Unlock:** receive Exodus arrivals from at least two origin countries totaling at least the larger of 10,000 people or 1% of opening population; every state that received them is Prepared at the final night; no Condemnation incident for violent border enforcement against the country during the episode.
**Difficulty:** very hard, visible once the Exodus begins.
**Icon:** an open gate leading to a protected doorway.

## 6. `tp85_before_the_storm`

**Direction:** shelter people in several warned storm states.
**Eligibility:** natural or manual episodes with at least three of the country's states warned for Hail and Fire.
**Unlock:** full Shelter Before the Storm results in three distinct warned states before their impacts, each accepted by Natural Disasters.
**Difficulty:** hard, visible.
**Icon:** a strong roof catching hail above three small houses.

## 7. `tp85_what_remained`

**Direction:** save the food that survived the storm.
**Eligibility:** natural or manual episodes with at least two states that suffered Hail and Fire crop damage and were later threatened by locusts.
**Unlock:** full Preserve the Remaining Harvest results in two such states before their fronts arrive; both stay at stable or supply strain for the following 30 days.
**Difficulty:** very hard, hidden until a qualifying hail-then-locust state exists.
**Icon:** a protected grain sheaf between a hailstone and a locust wing.

## 8. `tp85_keep_the_corridor`

**Direction:** keep a humanitarian corridor open in the middle of a war.
**Eligibility:** natural or manual episodes; the country and its counterpart are at war when Migration's passage agreement between them is accepted.
**Unlock:** keep the corridor open for 30 days spanning two phases; at least 50,000 people move through it; route deaths stay at or below 5% of those moved.
**Disqualifier:** troop movement through or diversion from the corridor.
A later peace does not undo completed wartime service.
**Difficulty:** very hard, hidden until a wartime corridor is accepted.
**Icon:** a relief route passing between opposed barriers.

## 9. `tp85_firstborn_survive_two`

**Direction:** protect the firstborn through two complete cycles.
**Eligibility:** episodes that legitimately reach a renewed sequence.
**Unlock:** finish two complete cycles; Passover coverage at least 90% at both final nights; tenth-plague deaths across both nights at most 2% of opening population; episode deaths at most 10% of opening population.
**Difficulty:** very hard, hidden until a restart is scheduled.
**Icon:** two concentric warning rings around the same protected household.

## 10. `tp85_worldend_ended`

**Direction:** help break the endless cycle.
**Eligibility:** episodes with The Plagues Without End active.
**Unlock:** the world completes the qualifying escape cycle (Part 9); during it the country completes full objectives in at least three phases and Foreign Relief Pledges for two different countries, and keeps Wrath at or below 40 throughout.
**Disqualifier:** administrative termination of the threat.
**Difficulty:** extreme, visible when the endless branch activates.
**Icon:** a broken circular chain above returning daylight and a damaged town.

## 11. `tp85_maximum_survivor`

**Direction:** overcome the strongest scenario opening.
**Eligibility:** Maximum launches, with the profile recorded at launch.
**Unlock:** finish the first sequence; full objectives in at least six phases; Wrath at most 25 at the final night; Passover coverage at least 90%; episode deaths at most 10% of opening population.
**Difficulty:** extreme, visible for Maximum episodes.
**Icon:** a battered standing doorway under a full ring of ten signs.
It does not require world-end eligibility at low Chaos.

## 12. `tp85_rebuild_afterward`

**Direction:** restore civilian life after surviving.
**Eligibility:** natural or manual episodes after the first tenth plague.
**Unlock:** complete Reconstruction Coordination in three distinct states; each stays at stable or supply strain for 60 days after completion; unlock no earlier than 120 days after the first tenth plague.
**Disqualifier:** a renewed plague damaging a counted state before its 60 days end resets that state's count.
**Difficulty:** very hard, visible after the first tenth plague.
**Icon:** a repaired water pump and rail line beside a memorial.

## Implementation

Conditions use the same records as gameplay: Deaths entries, Passover status, objective results, Migration transfers and corridors, Natural Disasters results and Famine stages.
Descriptions explain the real multi-part challenge without private field names.
Hidden achievements become visible at the stated milestone, and not-eligible icons reflect real disqualification rather than missing progress.
Every listed disqualifier is a negative test before the achievement is accepted.
