# AI, balance, exploits, and edge cases

## AI design goal

Research Failure can target AI majors, so the AI must understand the entire recovery loop.
It cannot receive a hidden shortcut, ignore the crisis, or spend every available resource on reconstruction while losing a war.

The AI needs four coordinated behaviors:

- Select an opening response that fits its diplomatic and political situation.
- Choose reconstruction projects that protect survival and restore research capacity.
- Reprioritize ordinary technology research toward lost branches and valid predecessors.
- React to foreign requests, scientist movement, archive offers, and Kruger demands.

Every weighted action needs named scenarios and HOI4 MCP probability evidence.
Source-only review is not enough for final balance acceptance.

## Target selection policy

Targeting should create variety while respecting severity.
The event does not automatically attack the player whenever a player is valid.

### Base candidate model

Every valid country appears once.
A human major has one entry, not one major entry plus one player entry.

The base weight is adjusted by:

- Major status.
- Human control.
- Current operational research slots.
- Number and depth of safe regression branches.
- Current year and technological position.
- Recent research investment and active research advantages.
- Residual lost-knowledge burden from an older incident.
- Target immunity and unresolved state.
- Current capitulation, exile, occupation, and territory state.
- Owner-system validity for special countries.

Human control makes a nonmajor eligible.
It should not create a hidden punitive multiplier.
The configured event system and multiplayer rules remain responsible for which player's timer selected the event.

### Preferred candidates

Selection weight should rise for a country with:

- At least three operational research slots at baseline.
- A broad safe technology frontier.
- Several active research projects with meaningful progress.
- Strong industry or military technology that can create an interesting legacy-production problem.
- No recent Research Failure.
- Enough economy and territory to use the reconstruction system.

### Reduced-weight candidates

Selection weight should fall for a country with:

- Only two slots at baseline.
- A very shallow safe technology graph.
- A large unresolved lost-knowledge deficit from an earlier incident.
- Severe occupation or imminent annexation that would make recovery meaningless.
- Very few civilian factories, unless it is the only player-controlled candidate.
- Recent major scientific disaster from another event.

A valid player country should not be excluded solely because it is weak.
Costs and project sizes scale down, while the loss selection remains bounded by safe technology.

### Invalid candidates

Weight is zero for:

- An active unresolved Event 60 target.
- A target inside immunity.
- A country with no controlled state and no supported exile-research route.
- A special or nonhuman country without an owner opt-in.
- A country whose technology graph cannot provide the minimum safe rollback.
- A country in terminal cleanup or a world-end state that has frozen normal events.

## Opening response AI

### Open scientific emergency

AI preference rises with:

- Democratic or plural institutions.
- High stability and public legitimacy.
- Trusted faction allies.
- Research-sharing membership.
- A large scientific diaspora in friendly countries.
- Low enemy intelligence pressure.
- Archive catastrophe or educational rupture.

AI preference falls with:

- Current war against a strong intelligence opponent.
- Severe diplomatic isolation.
- A national strategy built around secrecy.
- A high probability that partners will demand unacceptable dependence.

### Seal the institutions

AI preference rises with:

- Authoritarian or security-state politics.
- Current war.
- High enemy intelligence activity.
- A sabotage profile.
- Low trust in foreign partners.
- A military program whose weakness would be strategically dangerous if public.

AI preference falls with:

- A large friendly research network.
- Specialist dispersal that cannot be reversed under secrecy.
- Very low Archive Recovery.
- An earlier concealment exposure.

The sealed option should not dominate merely because it has a smaller immediate stability loss.
Its slower verification and flight risks need to matter in the AI score.

### Emergency Kruger mandate

The AI considers this option only when Event 16 confirms eligibility.

Preference rises with:

- Existential war.
- Four or more operational slots at risk.
- Advanced military or industrial technology that the country urgently needs to relearn.
- High existing Directorate authority or a government already aligned with Kruger.
- Very low domestic reconstruction capacity.
- No trusted foreign recovery partner.

Preference falls with:

- Strong civilian oversight.
- Low Directorate authority.
- A viable Independent Academy path.
- High stability and sufficient civilian industry for normal rebuilding.
- A prior Directorate bargain that already created dangerous entrenchment.
- Event 16 state indicating that the mandate would cross an unacceptable political threshold.

The AI should accept only when the value of preserved slots exceeds the long political cost under its current strategy.

## Reconstruction action priorities

The AI recalculates priorities after every project completion, major setback, war change, and technology recovery.
It should not evaluate only a fixed decision weight written at event start.

### Emergency priority order

1. Prevent a second loss when security or occupation risk is high.
2. Complete the stabilization mission before its deadline.
3. Raise Scientific Capacity enough to end the extreme research penalty.
4. Recover enough archives to identify lost domains.
5. Protect or recall specialists when diaspora pressure is high.
6. Open foreign help when a trustworthy partner exists and the selected stance allows it.

The order changes when the profile is clear.
Archive catastrophe increases record recovery.
Physical destruction increases site protection.
Educational rupture increases replacement cohorts.
Verification collapse increases standards.

### Slot restoration

The AI begins a slot project when:

- The Capacity requirement is met.
- The slot is owed by the incident ledger.
- The country can sustain the civilian-factory commitment.
- Essential military production, repair, supply, and convoy needs remain covered.
- No current project has higher survival priority.

A country at peace can accept a higher civilian burden.
A country losing a major war should stabilize one slot and continue survival production before starting additional institutes.

### Archive recovery

The AI values Archive Recovery more when:

- Many technology nodes remain lost.
- Important industrial or military domains lack a valid rediscovery bonus.
- A false archive risk is active.
- A foreign partner holds duplicate work.
- The country has already restored enough slots to use the recovered knowledge.

Archive investment receives lower immediate priority when the country still has only one slot, faces imminent defeat, or lacks basic Scientific Capacity.

### Personnel recovery

The AI recalls specialists when the country can offer safety and employment.
It trains replacements when foreign hosts refuse return, repression remains unresolved, or the missing cohort is too large for direct recall.

An AI should not repeatedly use coercive return when that policy causes net Capacity loss and diplomatic isolation.

### Standards and verification

The AI treats standards as a core project when:

- Verification collapse is active.
- Industrial or electronics branches were heavily regressed.
- Legacy-production penalties affect important equipment.
- A false archive incident occurred.
- The country is using foreign records from several incompatible sources.

## Institutional route AI

### International Recovery Consortium

High preference:

- Stable allied country.
- Research-sharing member.
- Strong relations with at least one scientifically capable partner.
- Large diaspora abroad.
- Open emergency response.
- Limited domestic civilian industry.

Low preference:

- Isolationist strategy.
- Hostile faction environment.
- Strong secrecy needs.
- High risk of foreign domination.
- Kruger mandate already accepted.

### Central Scientific Authority

High preference:

- Major war.
- Authoritarian government.
- High military-factory share.
- Urgent losses in armour, air, artillery, naval, radar, or industry.
- Weak allied research network.
- Sealed opening response.

Low preference:

- Stable peace.
- High false-result pressure.
- Institutional purge caused the collapse.
- Strong civilian academy tradition and available resources.

### Independent Academy Compact

High preference:

- Peace or limited war.
- High stability.
- Strong civilian factory base.
- Institutional purge or educational rupture.
- No reliable foreign sponsor.
- Long strategic horizon.

Low preference:

- Existential war.
- One-slot Knowledge Collapse with immediate military need.
- Very weak civilian economy.
- Government strategy that has already transferred authority to Kruger.

### Directorate settlement

This route follows Event 16's political AI and the existing mandate receipt.
Event 60 should not use a generic authoritarian weight as a substitute for Directorate state.

## AI research reprioritization

Technology regression creates a temporary AI research plan.
Without it, AI countries may research new descendants, unrelated ahead-of-time technologies, or a broad random spread while their core industrial and equipment branches remain broken.

The research plan should:

- Prefer missing prerequisites before descendants.
- Prefer lost industry and electronics in most cases.
- Prefer equipment families the country actively produces and fields.
- Prefer naval recovery only when the country has a meaningful fleet, dockyard base, or maritime strategy.
- Prefer air recovery when aircraft production and deployed wings are significant.
- Prefer radar and encryption when the country relies on detection or intelligence.
- Use the selected player-equivalent domain priority as an AI strategy input.
- Reduce ordinary ahead-of-time ambition until essential lost branches are restored.
- Avoid protected special technologies without an owner recovery route.
- Remove temporary research priorities when their ledger entries are recovered.

The plan should not force every AI into the same research order.
It uses the country's production, templates, active wars, enemy composition, resources, and doctrine strategy.

## Foreign AI behavior

### Aid partner

An AI partner is more likely to help when:

- It is in the same faction or research-sharing group.
- Relations are high.
- It is not at war with the target.
- It has the requested technology or relevant archive capacity.
- It can afford the equipment, convoy, or political cost.
- It expects a future license, trade, alliance, or influence benefit.

It is less likely when:

- The target is a rival or likely future enemy.
- The target concealed the crisis and was exposed.
- The aid would reveal a protected special technology.
- The partner is suffering its own Research Failure.
- The partner lacks a safe route or is close to defeat.

### Host of displaced specialists

An AI host weighs humanitarian support, scientific benefit, relations, ideology, and its own labor needs.
It can support return, propose a joint institute, or retain the specialists.
It should not always return valuable scientists for a small opinion gain.

### Rival exploitation

An AI rival attempts exploitation when it has intelligence reach, hostile relations, and a valuable target domain.
It avoids an operation when exposure would threaten a critical alliance, truce, or diplomatic strategy.

Exploitation weight rises after sealed institutions, sabotage, low Archive Recovery, and a recent Intel Leaked incident.

### Black Market intermediary

An AI Black Market member offers material when profit, sanctions, war shortage, and network access justify the risk.
It does not reveal organization membership to outsiders.

## Balance targets

Research Failure is a High cluster member and can alter a campaign for years.
Its severity must come from strategic delay and difficult rebuilding, not from making the target permanently unable to play.

### Baseline recovery target

For a normal major with five research slots and a healthy civilian economy:

- Emergency stabilization should take several months.
- The first missing slot should normally return within six to twelve months.
- The original slot count should normally return within roughly eighteen to thirty months.
- Scientific Capacity should reach 100 within roughly two to three years.
- Full lost-technology recovery should normally take two to five years depending on priorities and foreign help.

A small player country should receive smaller project bills and fewer losses, but its limited economy can still make the time horizon similar.

### Evolution I target

- First slot restoration remains achievable within about one year.
- Full institutional recovery normally takes two to four years.
- Technology recovery normally takes three to six years.

### Evolution II target

- First slot restoration normally takes about one to two years.
- Institutional recovery normally takes three to five years.
- Technology recovery normally takes five to eight years.

### Evolution III target

- The first step from one slot to two should normally take one to two years for a committed surviving country.
- Full slot restoration normally takes four to seven years.
- Complete technology recovery can remain a long campaign objective.

These ranges are tuning goals.
Implementation must test them with representative countries, years, DLC sets, wars, and industrial sizes.

## Effect strength

The crisis modifiers and project rewards must be large enough to change player choices.

- The starting research-speed penalty must be severe.
- Restoring one slot must be a major visible milestone.
- A standards project must materially improve production or verification pressure.
- A recovered archive series must noticeably accelerate a chosen lost field.
- Failure of the stabilization mission must create a real setback.
- Institutional settlements must change later decisions and risks.
- Long-term resilience must affect future Event 60 targeting or secondary incident probability enough to matter.

Small one or two percent modifiers can support a larger staged system but cannot be the main reward or penalty.

## Exploit controls

### Slot duplication

The incident records every suppressed slot, every restored slot, the original ceiling, external grants, and cleanup.
A restore decision consumes one owed-slot receipt.
Reloading, tag switching, civil war, and event rebuilding cannot create another receipt for the same slot.

### Free external slots

A focus, event, or idea that grants a slot during the crisis cannot bypass the floor or disappear permanently.
The external grant is reconciled through an adapter or active-target pulse.
At resolution, the country receives the correct combined ceiling exactly once.

### Technology grant farming

A direct grant clears one lost ledger entry.
It does not return Archive Recovery points that can be spent again.
Gift from Scientists and donor union effects use compatibility rules and one receipt.

### Priority switching

Changing the lost-domain research priority has a cooldown, cost, or minimum commitment period.
The player cannot switch on the last day of every research project to gain full bonuses across all domains.

### Foreign aid loops

Each partner and archive series has a one-time or generation-based receipt.
The target cannot repeatedly request the same duplicate record for unlimited Archive Recovery.
Foreign commission costs and dependence increase with repeated use.

### Specialist loops

A scientist cohort can be returned, retained, integrated, or lost once per incident state.
The same cohort cannot generate repeated Capacity gains through movement between two countries.

### Rushed archive save scumming

Where practical, major hidden outcomes should be determined when the project starts and stored in the incident ledger.
The result should not reroll every time a completion event is reloaded.

### Kruger exemption loops

Every mandate is tied to one incident sequence and one recorded slot count.
It cannot be activated after the normal floor has already been restored to claim a free Event 16 reward.
Repeated mandates deepen the price.

### Intentional non-recovery

A player might remain in crisis to avoid future targeting or preserve favorable emergency decisions.
The category therefore removes one-time emergency benefits after use, maintains real research penalties, and does not provide repeatable net-positive rewards.
Target immunity begins only after resolution, so delay provides no extra immunity time.

### Civil war copying

A civil war cannot create an unaffected copy of the country's pre-failure science.
The crisis state, regressed technologies, and slot suppression must propagate or transfer through a continuity rule.
The exact route depends on engine behavior and requires testing.

## Country-state edge cases

### Annexation

If the target is fully annexed and no government-in-exile continuity exists, the active institutional incident closes through forced cleanup.
No reconstruction Chaos reversal is granted.
The annexer does not inherit free lost technologies or Archive Recovery.

A later released country uses normal release technology rules unless Event 60 has a verified continuity record and the owner design deliberately restores it.

### Capitulation

Capitulation pauses domestic projects that require controlled territory.
The country retains the crisis, lost ledger, and people or archive actions that can operate in exile.
Liberation resumes domestic reconstruction without reapplying opening damage.

### Government in exile

A supported government in exile can preserve specialists, copy archives, and run limited research through a host.
It cannot restore all domestic research slots without a verified equivalent institution.
The host relationship can become a foreign-dependence path.

### Civil war

A civil war started during the crisis needs one continuity holder.
The preferred design is:

- All child sides inherit the currently regressed technology state because the knowledge has already been lost nationally.
- All sides receive a bounded temporary scientific-fragmentation penalty so no side gains unaffected slots through the split.
- The side holding the original capital, recognized government, or explicit continuity proof controls the main incident ledger and reconstruction category.
- If another side wins, the ledger transfers once to the successor.
- The defeated side's temporary crisis state clears without granting a recovery reward.

The final rule must match actual civil-war technology copying and country-scope behavior.

### Subject changes

Becoming a puppet, gaining autonomy, or changing overlord does not end the crisis.
An overlord can become a foreign aid partner or demand control over reconstruction.
Autonomy changes can affect the International Consortium route, but the target retains its own ledger.

### Faction and research-sharing changes

Joining a research group can open archive assistance.
Leaving one can delay foreign projects or convert them to domestic work.
Membership never restores technologies automatically unless the owning system explicitly grants them.

### Tag and cosmetic changes

The event follows country scope through cosmetic changes and ordinary tag identity changes that preserve the country.
The actor shown in current UI uses the current name and flag.
Historical entries preserve the shared logger's normal display behavior.

### Player control changes

The category becomes available to the current controller.
AI decisions stop when a player assumes control and resume when control returns to AI.
No opening event or damage reruns.

### No controlled states

A landless country can preserve people and archives only through exile support.
If no supported route exists, it cannot be selected initially.

### Very small economies

Dynamic costs use floors and caps.
A country with three civilian factories should not receive a ten-factory commitment that makes the decision impossible.
It can pay a larger time cost, accept foreign dependence, or rebuild a smaller institute.

### Very large economies

Costs scale with economy and slot ceiling so a global major cannot finish every project through trivial fixed payments.
Caps prevent an event project from consuming an absurd share of the economy.

## Technology and production edge cases

### Already researched descendants

A parent technology is not removed while a researched descendant remains.
The transaction removes a coherent suffix in descendant-first order or skips the branch.

### Mutually exclusive branches

The chosen branch root remains.
The transaction never grants or removes the competing root.

### Technologies without predecessors

A technology with no safe older state is skipped unless its owner defines a degradable or replaceable policy.

### Technologies granted by focus or event

A technology that cannot normally be researched again is protected unless its owner supplies a recovery path.
The event does not make permanent route rewards unobtainable by accident.

### Equipment in stockpile

It remains.
Family penalties cannot convert or delete the equipment.

### Production lines

Every included family needs evidence that an existing line remains valid.
A family that corrupts or deletes lines is blocked.

### Licenses

A country may use foreign licenses for equipment it can no longer produce domestically.
Licensing does not clear the lost-knowledge ledger.
It can be a useful International Consortium or emergency action.

### Captured equipment

Captured equipment remains usable.
It does not prove domestic knowledge and does not restore technology.

### Special projects

Project progress and facilities remain protected unless the owner opts in.
Evolution II damage to stored research advantages does not silently reset special projects.

### Ahead-of-time research

A lost technology that was previously researched ahead of time remains a lost known technology.
Archive support can reduce relearning difficulty only within the engine's safe bonus rules.
The event does not grant an unlimited ahead-of-time exemption.

### Technology becomes obsolete

When another system replaces a lost technology permanently, the owner callback marks the ledger entry obsolete and removes its family penalty.
This does not count as independent rediscovery for achievements unless the achievement design says so.

## Save and reload

Every incident state must persist:

- Sequence identity.
- Target.
- Severity and evolution.
- Collapse profiles.
- Opening response.
- Pre-failure slot ceiling.
- Suppressed and restored slot receipts.
- External slot reconciliation.
- Public values.
- Active projects and stored outcomes.
- Lost and recovered technology entries.
- Foreign actors and one-time offers.
- Directorate mandate state.
- Chaos receipts.
- Target immunity.

Reopening the category rebuilds presentation from persisted state.
It does not recalculate the original rollback or reroll hidden project outcomes.

## Multiplayer

The incident targets one country.
Only that country's controller manages its normal reconstruction decisions.
Foreign player countries receive bounded targeted choices when they are selected as partners, hosts, or rivals.

The event must avoid duplicate candidate weight for player majors.
Each foreign offer needs a timeout and AI fallback so a disconnected or inactive player does not block the target forever.

All players see the shared event history and evolution log according to the existing framework.
Hidden scientific weakness remains country-scoped until a public exposure or foreign action makes it known.

## DLC and technology-tree variants

The technology registry must account for installed DLC and current tree variants.
Chassis, hull, module, MIO, special project, and research systems can differ materially.

The implementation needs named validation sets for:

- Base game without relevant equipment-design DLC.
- Man the Guns naval trees.
- No Step Back armour and officer systems.
- By Blood Alone aircraft trees.
- Arms Against Tyranny MIO interactions.
- Götterdämmerung special projects and facilities where installed.
- Chaos Redux event-owned technologies.
- A representative custom-mod technology entry using the owner registry.

A missing DLC removes its branches from the candidate pool.
It does not create empty decisions or raw keys.

## Probability audit requirements

Before weighted logic is accepted, `chaosx_ai_probability_auditor` should inspect and compare:

- Target selection.
- Opening response AI.
- Institutional route AI.
- Foreign partner and rival selection.
- Secondary incident weighting.
- Technology-domain and branch selection.
- Research priority strategy factors.
- Active-evolution timing.

The audit begins with `hoi4.probability_inspect`.
It then uses evaluation, sweeps, simulation, sequence analysis, comparison, or rendering only where the candidate pool and external state are complete enough for that evidence.

The scenario matrix in this pack defines expected ordering and starvation checks.
The auditor should distinguish exact, bounded, sampled, score-only, and unresolved results.
It does not choose new balance targets on its own.

Any patch to a probability-bearing surface requires a baseline audit, an owner-applied patch, and `hoi4.probability_compare` under the same named scenarios.

## Completion balance evidence

A complete implementation needs representative simulations or deterministic test setups for:

- A five-slot industrial major in 1936.
- A six-slot advanced major in the early 1940s.
- A two-slot small player country.
- A naval major.
- A landlocked army-focused country.
- A country at peace.
- A country in an existential war.
- A country under heavy occupation.
- A valid Kruger Directorate.
- Each evolution.
- A repeat firing after recovery.

The report should compare actual slot restoration, Capacity recovery, Archive Recovery, lost-technology research time, project affordability, AI decisions, and military survivability with the design ranges.
A statement that the numbers feel balanced is not sufficient evidence.
