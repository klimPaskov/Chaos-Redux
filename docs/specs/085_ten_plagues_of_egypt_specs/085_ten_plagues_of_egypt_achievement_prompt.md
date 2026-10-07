# Event 085 — Achievement Implementation and Art Prompt

Implement all twelve achievements below for `docs/specs/085_ten_plagues_of_egypt_specs/`.
Read the full specification first, then follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
The contracts reproduced below are the substantive scope; Part 18 remains the canonical divided-spec copy.

Inspect the current achievement registry and framework before allocating identifiers.
Map each proposed semantic `tp85_*` key to a collision-free full event-prefixed runtime ID such as `085_ten_plagues_of_egypt_<semantic_suffix>`.
Record the mapping once and use it for conditions, localization, icons, documentation, and tests.
Never overwrite a global numeric slot or reuse an unrelated achievement.

Implement all conditions, disqualifiers, hidden/visible transitions, episode and country eligibility, fixed denominators, and owner-proof trackers.
Write final title and description localization from each working direction.
Do not simply ship the planning labels as final polished copy.
No achievement may unlock on one easy event acknowledgement or on an unverified claimed result.

Use the existing framework and exact Deaths, Migration, Famine, disaster, protection, and reconstruction receipts.
Prevent receipt recycling, annexation or release farming, cohort regeneration, and administrative reset unlocks.
Save/load alone never disqualifies a legitimate episode.
Inspect both positive and negative cases.

For each icon, generate one original native-transparent 64 × 64 subject from its direction.
Build aligned completed, deterministic-grey, and not-eligible source layers using the unchanged supplied overlay and templates.
Pass the complete three-state source triplet to `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`.
Do not feed a single file, draw a replacement red cross, or regenerate three unrelated images.
Runtime DDS files remain directly in `gfx/achievements/` and exactly match the final ID and suffixes.

Route icon work to `chaosx_icon_artist` with exact IDs, directions, source and output paths, reference library, and handoff requirements.
Use `fork_turns="none"` for Codex named specialist calls.
The parent performs final framework wiring and reviews the real native-size consumer.
Return conditions and tracker documentation, changed files, final IDs and localization, all 36 processed icon states, source manifests, positive/negative test evidence, and unresolved blockers.

## Complete achievement contracts


## Eligibility and evidence

The twelve identifiers below are proposed semantic IDs.
The implementation must inspect the actual achievement registry before allocating final identifiers.
Working labels communicate title direction and are not finished localization.

Each achievement uses exact episode, cycle, country-responsibility, and owner receipt evidence.
Deaths use applied Deaths entries.
Protection uses people actually reached.
Relief uses actual accepted delivery.
Reconstruction uses restored services, not a paid button alone.

Use fixed launch or milestone denominators where stated.
Annexation, release, tag changes, migration, and population death cannot shrink an achievement's required denominator or recreate eligibility.
A legitimate successor can inherit only the obligations and progress that actually transfer.

Debug resets, forced phase skips, administrative population restoration, or receipt manipulation invalidate affected survival achievements.
Ordinary save/load does not.
None of these achievements rewards killing civilians or deliberately maximizing the final death toll.

For each subject, produce colored, grey, and not-eligible icons through the standard immutable-template processor.

## 1. `tp85_through_ten`

**Working label and description direction:** careful national survival through the complete sequence.
**Eligible countries:** any valid human-population country present at a natural episode's Blood onset.
**Unlock:** complete all ten plagues; remain at Wrath 50 or lower from Boils onset through the final night; fully protect at least 90% of the country's eligible firstborn people at that final deadline; keep episode-attributable civilian deaths at or below 5% of its fixed initial civilian responsibility.
**Disqualifiers:** manual launch, phase skipping, population-responsibility laundering, or an incomplete full sequence.
**Difficulty and visibility:** hard, visible.
**Why it is nontrivial:** protection must be sustained through several distinct disasters while actual cumulative mortality remains limited.
**Icon direction:** a repaired doorway and ten discreet surrounding marks, with no text.
**Tracking:** fixed opening responsibility, all phase completions, Wrath interval violations, firstborn coverage receipt, and applied event-correlated deaths.

## 2. `tp85_small_country_served`

**Working label and description direction:** a small country survives through its own local civilian organization.
**Eligible countries:** natural or Low/Medium manual episodes; opening civilian population at most five million and at most five civilian factories.
**Unlock:** complete at least five distinct phase-protection objectives through the local route; finish the full sequence; fully protect at least 80% of eligible firstborn people; finish at Wrath 25 or lower; keep episode-attributable deaths at or below 5% of fixed initial responsibility.
**Disqualifiers:** obtaining the counted completions through national transport packages, changing tag to meet the opening limits, or replacing local work with a donated instant completion.
**Difficulty and visibility:** hard, visible.
**Why it is nontrivial:** low starting capacity must support real work through multiple phases rather than one cheap action.
**Icon direction:** a small civic shelter protected by several joined hands.
**Tracking:** frozen opening size and factory facts, local-route receipts, current physical coverage, and the ordinary survival ledger.
Foreign material assistance may help where local work remains the actual completion route.

## 3. `tp85_late_heeding`

**Working label and description direction:** a government changes course after repeatedly hardening its heart.
**Eligible countries:** natural or manual episodes beginning at Blood.
**Unlock:** choose Harden Our Hearts in at least two distinct phases before Livestock; actually reach Wrath 60 or higher; subsequently complete protection in at least three distinct phases; enter Darkness at Wrath 25 or lower; fully protect at least 90% of eligible firstborn people.
**Disqualifiers:** another Harden choice after the qualifying change of course, a reset of Wrath through country replacement, or a missed tenth-plague settlement.
**Difficulty and visibility:** hard, hidden until the early hardening condition is met.
**Why it is nontrivial:** earlier harm remains while the player must finance a genuine recovery before the final warning.
**Icon direction:** a cracked stone heart beside a lit household doorway.
**Tracking:** ordered phase-policy history, verified high-Wrath point, the change-of-course boundary, subsequent work, and final coverage.

## 4. `tp85_beyond_borders`

**Working label and description direction:** protect foreign civilians while maintaining a credible response at home.
**Eligible countries:** natural or manual episodes with at least three distinct valid recipient countries available.
**Unlock:** deliver effective Event 085 relief to three different countries across at least three plague phases; each delivery must satisfy a real accepted need; complete the donor's own Passover for at least 80% of its eligible firstborn people; finish at Wrath 25 or lower.
**Disqualifiers:** returned-shipment loops, puppet release to create recipients, nominal deliveries without effect, or replacing three recipients with three states of one country.
**Difficulty and visibility:** hard, visible.
**Why it is nontrivial:** scarce transport and supplies must serve several real foreign needs without abandoning the donor's final preparation.
**Icon direction:** three distinct shelters linked by a relief crate and route.
**Tracking:** unique recipient responsibility identities, delivery generations, phase IDs, effective benefit receipts, and donor protection.

## 5. `tp85_protected_exodus`

**Working label and description direction:** receive displaced people and protect them through the final night.
**Eligible countries:** natural or High/Maximum manual episodes with Exodus active.
**Unlock:** receive surviving cohorts from at least two distinct origins totaling at least the greater of 10,000 people or 1% of the host's fixed opening civilian population; fully prepare at least 90% of those qualifying living firstborn arrivals for the final night; keep a valid safe reception arrangement through the tenth-plague settlement.
**Disqualifiers:** unsafe forced return, repeated cycling of the same cohort, fabricated arrival credit, or counted arrivals still in transit at the deadline.
**Difficulty and visibility:** very hard, visible once Exodus is active.
**Why it is nontrivial:** movement, food safety, reception, and actual household protection must all succeed.
**Icon direction:** an open gate leading to a protected reception doorway.
**Tracking:** exact surviving arrivals, historical origin, current custody, food-safety projection, protection class, and no-abuse receipts.

## 6. `tp85_before_the_storm`

**Working label and description direction:** protect exposed civilians across several warned storm states.
**Eligible countries:** natural or manual episodes with at least three distinct valid state footprints threatened by Hail and Fire.
**Unlock:** before each of three distinct state impacts, shelter or validly evacuate at least 75% of that impact's initially warned civilian exposure; each impact must resolve with the protection accepted by its disaster owner.
**Disqualifiers:** deleting or transferring states to erase exposure, counting the same impact twice, or an impact never actually occurring.
**Difficulty and visibility:** hard, visible.
**Why it is nontrivial:** three separate preparation windows and physical footprints must be served.
**Icon direction:** a strong shelter roof intercepting hail above three small houses.
**Tracking:** fixed warned exposure per impact, exact sheltered or evacuated people, accepted disaster receipts, and distinct state identity.

## 7. `tp85_what_remained`

**Working label and description direction:** preserve the food that survived the storm.
**Eligible countries:** natural or manual episodes with at least two states experiencing both genuine Hail and Fire crop damage and a later valid locust threat.
**Unlock:** protect or move at least half of the proven remaining threatened food capacity in both states before the front arrives; keep those states at Stable or Supply Strain, as proven by Famine, throughout the following 30 days.
**Disqualifiers:** treating already destroyed crops as saved food, defaulting unknown famine state to Stable, or canceling the actual locust threat administratively.
**Difficulty and visibility:** very hard, hidden until a valid hail-to-locust chain exists.
**Why it is nontrivial:** the objective concerns the remainder of a damaged food system and requires sustained food safety.
**Icon direction:** a protected grain sheaf between a hailstone and a locust wing.
**Tracking:** surviving food baseline, delivered preservation result, front deadline, and continuous owner-proven food stage.

## 8. `tp85_keep_the_corridor`

**Working label and description direction:** sustain a humanitarian corridor despite an active war.
**Eligible countries:** natural or manual episodes; the player and the counterpart are actually at war when the agreement is accepted.
**Unlock:** maintain a valid limited civilian corridor for 30 days spanning at least two plague phases; move at least 50,000 unique people or deliver an owner-verified relief equivalent serving at least 50,000 unique people; achieve at least 95% route survival for people actually transported.
**Disqualifiers:** using the corridor for combat access, deliberate relief diversion, an administrative peace solely to bypass the wartime contract, or repeated counting of the same recipients.
**Difficulty and visibility:** very hard, hidden until a wartime corridor is accepted.
**Why it is nontrivial:** diplomatic restraint and physical logistics must persist while the war continues.
**Icon direction:** a relief route passing between opposed military barriers.
**Tracking:** wartime acceptance, purpose-restricted permissions, continuous route validity, unique beneficiaries, transport survivors, and violations.
A later legitimate peace does not invalidate already completed qualifying wartime service.

## 9. `tp85_firstborn_survive_two`

**Working label and description direction:** preserve the same firstborn survivors through two complete cycles.
**Eligible countries:** natural or manual episodes that legitimately reach a renewed full sequence.
**Unlock:** finish two complete ten-plague cycles; at least 90% of the country's fixed initial living firstborn cohort must still be alive after the second tenth-plague settlement, counting losses from every cause; complete substantial current Passover work in both cycles; keep all episode-attributable civilian deaths at or below 10% of fixed initial responsibility.
**Disqualifiers:** regenerating the firstborn cohort, counting new arrivals as original survivors, losing tracked people without reconciling their outcome, or skipping either sequence.
**Difficulty and visibility:** very hard, hidden until a restart is scheduled.
**Why it is nontrivial:** it follows the same people and lasting infrastructure rather than two unrelated national preparation flags.
**Icon direction:** two concentric warning rings around the same protected household.
**Tracking:** cohort lineage, original membership, cause-specific deaths, current coverage each cycle, and total applied mortality.
Known emigration preserves lineage and does not count as death, but its later outcome must remain traceable.

## 10. `tp85_worldend_ended`

**Working label and description direction:** contribute materially to breaking the endless cycle.
**Eligible countries:** any legitimate episode with The Plagues Without End actually active.
**Unlock:** complete the full qualifying escape cycle; during that cycle the country completes at least three substantial protective objectives and two effective deliveries to distinct foreign needs; it remains at Wrath 40 or lower throughout that cycle.
**Disqualifiers:** administrative termination, clearing the terminal flag directly, inheriting completed work without its responsibility, or a global endpoint that failed the full-cycle condition.
**Difficulty and visibility:** extreme, visible when the endless branch activates.
**Why it is nontrivial:** the country must participate in the collective recovery rather than merely survive while others end the threat.
**Icon direction:** a broken circular chain above returning daylight and a damaged town.
**Tracking:** verified world-end entry, full-cycle qualification, country Wrath interval, distinct local work, effective foreign delivery, and exact escape receipt.

## 11. `tp85_maximum_survivor`

**Working label and description direction:** overcome the scenario's strongest opening.
**Eligible countries:** a Maximum scenario launched at Blood with the profile recorded at episode creation.
**Unlock:** finish the full first sequence; complete substantial protection in at least six distinct phases; enter the final night at Wrath 25 or lower; fully prepare at least 90% of eligible firstborn people; keep episode-attributable deaths at or below 10% of fixed initial responsibility.
**Disqualifiers:** changing profile after launch, phase skipping, population restoration, or reducing the actual profile through a debug path.
**Difficulty and visibility:** extreme, visible for a Maximum episode.
**Why it is nontrivial:** high starting Wrath and comprehensive exposure require sustained recovery across nearly the entire sequence.
**Icon direction:** a battered but standing doorway beneath a complete ring of ten signs.
**Tracking:** immutable launch profile, six distinct full-completion receipts, mortality denominator, final Wrath, and protection.
The achievement does not require forged world-end eligibility at low Chaos.

## 12. `tp85_rebuild_afterward`

**Working label and description direction:** restore essential civilian life after surviving the sequence.
**Eligible countries:** natural or manual episodes with at least three genuinely damaged civilian-service states and two damaged routes.
**Unlock:** complete a full sequence; restore the relevant essential services in three distinct affected states and two actual damaged transport routes; then maintain owner-proven Stable or Supply Strain conditions in the three states for 60 days; unlock no earlier than 120 days after the country's first tenth-plague settlement.
**Disqualifiers:** administrative repair, state replacement, unknown food safety, a new active plague destroying the counted service before the continuity window completes, or counting work that another country completed without the player's verified contribution.
**Difficulty and visibility:** very hard, visible after the first tenth plague.
**Why it is nontrivial:** reconstruction is real, sustained, and tied to the earlier catastrophe.
**Icon direction:** a repaired water pump and rail line beside a memorial.
**Tracking:** original damage receipts, restored service and route identities, contribution evidence, food-safety continuity, and the earliest eligible date.

## Implementation and presentation

The achievement worker implements conditions through the existing achievement framework, wires final localization and all three icon states, and documents each tracker.
Country and global predicates must use the same shared proof as gameplay.

Descriptions explain the real multi-part challenge without revealing private transaction fields.
Hidden achievements become visible at the stated contextual milestone.
Not-eligible icons reflect actual disqualification rather than temporary lack of progress.

A triggered unlock is not accepted until its negative cases have been checked.
The final audit covers duplicate episodes, save/load, controller transfer, scenario eligibility, fixed denominators, and every listed disqualifier.
