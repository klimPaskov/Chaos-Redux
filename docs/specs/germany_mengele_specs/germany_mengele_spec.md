# 004 Germany, Auschwitz Experiments, and the Angel of Death Coup Spec - Part 1

## 3. Core Event Concept

Germany receives an event asking whether Josef Mengele and associated SS medical offices may conduct extensive biological and hereditary experiments at Auschwitz.

The first event should feel like a bureaucratic decision, not a dramatic monster reveal. It should be written as a regime paper crossing a desk: resource allocation, SS authority, biological research, secrecy, and wartime necessity.

The player gets a choice:

1. Authorize the Auschwitz Experiments
2. Restrict the program to ordinary camp administration
3. Shut the proposal down before it grows

The first option grants a strong biological research advantage, but it plants hidden danger. The second gives a smaller benefit and avoids the most extreme chain. The third avoids the chain but may anger hardline factions if Germany is deep into fascist radicalization.

This should create one of the more disturbing Chaos Redux dynamics: the player may accept an apparently useful research boost without immediately understanding that they have empowered a future internal threat.

## 4. Firing Conditions: Auschwitz Facility Prompt

The first event should fire for Germany when Auschwitz is historically plausible and German fascist institutions can still authorize the program.

Recommended trigger window:

- Germany exists
- Germany is fascist or controlled by a Nazi-equivalent regime
- Germany owns or controls the Auschwitz area, using the mod’s existing state or facility logic
- date is at least 1940.06.14, or the existing Auschwitz facility event has fired
- Germany has not already rejected the Auschwitz experimental program
- Germany has not already collapsed into a non-fascist government

## 5. National Spirit: Auschwitz Experiments

### Role

The national spirit should be powerful enough that the player feels the temptation.

Suggested name:

`Auschwitz Experiments`

It lasts two years unless cancelled by regime change or special collapse conditions.

### Effects

Recommended effects:

- biological warfare research speed increase
- biological special project speed increase if available
- minor medical or attrition-related army research benefit if such categories exist
- possible unlock or speed boost for biowarfare facilities
- hidden increase to Mengele autonomy or SS laboratory power
- hidden increase to future atrocity condemnation if exposed
- small stability penalty or political paranoia penalty if the chain advances

Avoid giving clean bonuses only. The spirit should always include a hidden or visible cost.

Possible visible penalties:

- reduced stability
- reduced political power gain
- increased resistance in occupied territories
- increased foreign condemnation if discovered
- internal faction suspicion

The spirit should be cancelled if:

- Germany is no longer fascist
- Nazi-equivalent ideology loses control
- Auschwitz is lost
- the player later purges Mengele or closes the program

### Tooltip Direction

The tooltip should not describe experiments in detail. It should make clear that the program is secretive, and useful to the regime in the short term.

Example direction:

The regime has given SS medical offices wider authority at Auschwitz. The reports promise biological discoveries and wartime applications.

## 7. Hidden System: Mengele Autonomy

The chain needs a hidden escalation value. It should represent Mengele and his laboratory network becoming less dependent on the German state.

Suggested hidden value:

`mengele_autonomy`

It should increase from:

- authorizing the full Auschwitz program
- completing biowarfare facility expansion
- building more biowarfare facilities
- Germany being at war with the Soviet Union
- high fascist support
- high chaos
- desperate war situation
- selecting later events that give Mengele more resources
- ignoring warning signs
- allowing SS offices to bypass military review

It should decrease from:

- restricting experiments
- closing the program
- losing Auschwitz
- regime de-Nazification or ideology change
- military oversight events
- purging SS medical offices
- civil war pressure
- foreign bombing or sabotage of biowarfare facilities

This value does not need to be shown directly at first. The player should feel something is wrong through event text, strange reports

## 8. Mid-Chain Events Before the Coup

Between authorization and the coup, the player should receive a few escalating reports. These should not spam the player. Two to four events are enough.

### 8.1 “Reports Without Names”

A ministry file arrives with improved biological results but missing personnel records. The state can:

- demand complete records, reducing autonomy but lowering research speed
- accept the results, increasing research and autonomy
- transfer the file to SS custody, raising autonomy sharply

### 8.2 “The Twin Registers”

A report mentions twin records, hereditary comparisons, and unusual survival statistics.

Choices:

- continue the work
- place military doctors in the camp offices
- classify the whole program under SS authority

Effects should alter autonomy, research, and future coup likelihood.

### 8.3 “A Laboratory without Berlin”

A later event suggests Auschwitz laboratories are receiving orders, materials, or personnel without normal ministerial approval.

Choices:

- investigate
- ignore during wartime
- reward the results

This is the strongest pre-coup warning. If the player keeps rewarding results, the later coup should feel earned.

### 8.4 Rare “The Children Do Not Answer to Guards”

If the chain is near coup level, a rare event reports that certain experimental subjects are responding to Mengele’s staff rather than SS guards or army officers.

This should be disturbing and ambiguous.

## 9. Coup Trigger: Angel of Death Civil War

The coup should be rare and require extreme conditions. It is an easter egg, not a normal Germany path.

Recommended trigger conditions:

- Germany exists
- Germany is fascist or Nazi-equivalent
- fascist support is at least 80 percent
- Germany is at war with the Soviet Union
- date is 1943 or later
- Auschwitz Experiments were fully authorized
- Auschwitz Experiments spirit is active or recently expired with enough hidden autonomy
- Germany owns or controls at least three biowarfare facilities
- Mengele autonomy is above threshold, or equivalent flags are set

If these conditions are met, the event can fire after a delay.

The coup should not be framed as a normal political coup. It is a regime fracture caused by SS laboratories, pseudoscience, and command failure.

## 10. Coup Event: “The Angel of Death Leaves the Camp”

### Event Purpose

This event is the reveal that Germany’s authorized crimes have produced a faction that no longer obeys Berlin.

### Event Description Direction

The event should describe confused reports: trains rerouted, SS guards replaced or ignored, laboratory staff claiming direct authority, and distorted units moving under Mengele’s command. The state realizes too late that the program became a private army.

The deformed twins idea should be handled carefully. The game can present them as malformed, indoctrinated, medically damaged, altered, and frighteningly disciplined subjects. Their battlefield performance should be partly real and partly propaganda. These clones should outperform normal soldiers. Their strength should come from horror, conditioning, experimental damage, drugs, control, and the regime’s willingness to expend them.

### Player Situation

Germany splits into:

- Loyalist Germany under the existing regime
- Mengele’s faction under Josef Mengele as `Angel of Death`

The civil war should be very dangerous and almost always fatal (to AI, the player could somehow fight it off if he has the skill, so it has to be very challenging).

Mengele’s faction controls:

- Auschwitz area if available
- all biowarfare facilities
- several SS laboratory-linked military units
- nearby states depending on balance
- possibly pockets in occupied Poland or Silesia if Germany controls them

Loyalist Germany keeps:

- Berlin unless the country is already collapsing
- most regular army command
- normal industry
- diplomatic recognition
- most navy and air force unless balance requires otherwise

## 11. Mengele Faction Identity

### Country Concept

It should be a laboratory state built around Mengele’s authority.

Possible temporary cosmetic name:

`Mengele's Laboratory State`

Possible formal name:

`The Auschwitz Directorate`

Possible extreme name after consolidation:

`The Angelic Directorate`

This name should not sound cool. It should sound cold and wrong.

The country should have an idea that grants tons of weekly manpower (from cloning)

### Leader

Josef Mengele becomes country leader with title:

`Angel of Death`

Leader trait ideas:

- `angel_of_death`
- `laboratory_autocrat`
- `camp_command`
- `pseudoscientific_fanatic`

Trait effects should be strong but unstable:

- biological warfare research speed
- special forces or irregular unit organization
- biowarfare facility output
- high division recovery or reinforce rate for special units
- severe stability penalty
- severe diplomacy penalty
- high condemnation
- higher resistance in controlled non-core states
- inability to form normal alliances except through later rare chains

### Ideology

This faction should remain fascist.

## 12. Special Units: Experimental Twin Formations

The coup can spawn special units.

Suggested name:

`Experimental Twin Formations`

Alternative names:

- `Laboratory Cohorts`
- `Mengele Formations`
- `Auschwitz Cohorts`
- `Twin Register Units`

### Gameplay Role

They should be strong:

- high organization
- high breakthrough or shock value
- high reinforce rate
- reduced training time
- strong suppression or terror effect
- low attrition

But with costs:

- poor long-term recovery
- stability damage
- high condemnation
- poor reliability if using armor or mechanized templates
- severe diplomatic consequences

Mengele influence/autonomy should grow from extermination camp use, Auschwitz Experiments, SS medical authority, and related choices.
- As Mengele gains influence, he can demand new biowarfare facilities.
- If Germany accepts these demands, new biowarfare facilities should instantly appear in suitable controlled states.
- Accepting these demands should also have a chance to unlock one normally event-locked biowarfare special project early.
- This can include projects such as zombie weaponization before the zombie outbreak event has fired.
- AI Germany may accept these demands if radical, desperate, heavily invested in biowarfare, or already deep into the Mengele path.

### Spawn Logic

If the coup fires, spawn a limited number of units based on:

- number of biowarfare facilities
- hidden Mengele autonomy
- Germany’s current manpower
- balance needs

## 13. Germany Loyalist Choices During Civil War

The loyalist side should have several responses.

### Choice Route A: Crush the Laboratory

Germany receives decisions to:

- retake Auschwitz
- seize biowarfare facilities
- purge SS medical offices
- restore military control
- destroy laboratory records
- call for emergency army loyalty

This route stabilizes Germany if successful but may lose some biological research progress.

### Choice Route B: Reclaim the Results

A darker loyalist route tries to defeat Mengele while keeping the research network.

Effects:

- higher research retention
- higher condemnation
- higher future instability
- possible rare second outbreak or laboratory mutiny
- more foreign hatred

### Choice Route C: Let the Doctor Burn the East

If Germany is losing badly to the Soviet Union, the player may get an emergency option to tolerate Mengele’s faction temporarily against the Soviets.

This should be extremely dangerous:

- temporary truce or non-aggression between loyalists and Mengele
- Mengele fights Soviets
- after a timer, the faction turns on Germany or escalates
- massive condemnation
- more deaths
- no clean benefit

This should be rare and likely AI-avoided except under desperation.

## 14. Foreign Reactions

The coup should create international shock.

Foreign event reactions should depend on intelligence and ideology.

### Soviet Union

The Soviets should react strongly if at war with Germany:

- propaganda about fascist monstrosity
- increased war support
- possible temporary offensive bonus against Mengele faction
- stronger willingness to push into occupied Poland
- possible event calling for no surrender

### Allies

Allied powers should receive:

- condemnation event
- increased intelligence interest
- possible bombing or sabotage decisions against biowarfare facilities
- increased support for anti-German operations
- stronger postwar justice memory

### Fascist Allies

German allies should be disturbed but may not immediately leave.

Reactions:

- reduce opinion of Germany or Mengele faction
- some fascist regimes deny reports
- some quietly restrict cooperation
- some hardline radicals express interest, raising condemnation if exposed

### Neutral Countries

Neutral states receive rumor-driven news:

- unconfirmed reports from occupied Poland
- laboratory revolt
- German officials deny all claims
- foreign intelligence describes a camp doctor commanding armed formations

Avoid overexplaining everything through global news. Some events can remain uncertain until the faction is visible.

## 15. Condemnation, Deaths, and Chaos Meter

This chain should connect to existing Chaos Redux systems where useful.

### Condemnation

Authorizing the program should create hidden condemnation memory. The coup should expose it.

When exposed:

- Germany receives major condemnation
- Mengele faction receives extreme condemnation
- countries may gain anti-German or anti-Mengele opinion modifiers
- fascist countries may respond differently, but should not treat it as normal

### Deaths

Use the deaths system to record deaths from experiments. The deaths count should be exponential from experiments, the more power mengele has.

### Chaos Meter

The first authorization may raise chaos slightly or create hidden future chaos pressure. It should not cause a giant public chaos spike unless exposed.

The coup should raise chaos significantly because:

- Germany fractures internally
- biowarfare facilities become contested
- foreign powers panic
- atrocities become militarized
- the war becomes less predictable

Suggested chaos behavior:

- coup: significant chaos increase
- Mengele victory: larger chaos increase
- loyalist purge and shutdown: possible small chaos reduction after a delay

## 17. AI Behavior

AI Germany should rarely choose the full dangerous route unless the campaign is already extreme.

Recommended AI weights:

- historically fascist Germany may authorize the program sometimes
- if biological warfare is central to the campaign, authorization is more likely
- if Germany is losing badly, authorization is more likely
- if Germany is stable and winning, restriction is more likely than full autonomy
- non-fascist Germany should never authorize it
- AI should rarely choose options that knowingly allow Mengele autonomy once warning signs appear, unless it is desperate or highly radical

For the coup:

- AI should be able to trigger it under the hidden conditions
- the event should remain rare
- AI Mengele faction should be aggressive but unstable
- AI loyalist Germany should prioritize retaking facilities
- foreign AI should treat Mengele faction as a severe threat

## 19. Failure and Cleanup Paths

The chain needs clean endings.

### If Germany closes the program early

- remove national spirit
- remove hidden autonomy growth
- add memory that SS medical offices were restrained
- possible small internal fascist anger
- no coup

### If Germany loses Auschwitz

- program collapses or relocates depending on later design
- hidden autonomy drops
- possible foreign capture event
- possible intelligence exposure
- no coup unless another facility chain exists

### If Germany changes ideology

- cancel Auschwitz Experiments
- remove Mengele autonomy growth
- purge or flee event for Mengele
- possible post-regime investigation event
- no Nazi coup path

### If Mengele faction is defeated

- loyalist Germany chooses whether to burn files, keep records, or expose blame internally
- remove Mengele country or absorb remnants
- remove or repurpose biowarfare facilities
- add event log entry
- possible chaos reduction if the program is truly destroyed

### If Mengele faction wins

Possible outcome:

- extreme condemnation
- severe instability
- all biowarfare paths automatically unlocked (the ones that are disabled by events for example. For the example the zombie bomb, even if the zombies event hasn't fired yet)
- most normal diplomatic paths blocked


## 25. Decision Category: The Final Solution (integrate it better somehow with the existing genocide mechanics)

The category should be available only to Germany or a Nazi-equivalent German tag under radical conditions.

Recommended availability:

- Germany exists
- Germany is fascist or Nazi-equivalent
- Nazi/fascist popularity or ruling ideology strength is high enough
- Germany has not been de-Nazified
- Germany is not already under the Mengele faction unless later desired
- Germany has not fully collapsed into civil war

The category should be written as a set of secretive administrative decisions, not as battlefield operations.

The player should see decisions such as:

- centralize racial offices
- expand SS archive authority
- classify deportation records
- authorize ancestry research budgets
- protect Ahnenerbe funding channels
- send survey teams through occupied archives
- coordinate camp and institute records
- silence internal church or legal objections if Germany still has those structures
- prepare a foreign mythic-research mission

Not every decision needs to be available at once. The category should unfold based on previous choices, war state, fascist support, and whether the Auschwitz Experiments chain is active.

## 26. Decision Layer Values

The decision layer should track a few abstract values or flags. These are not all necessarily visible to the player.

Suggested values:

`racial_policy_radicalization`

Represents how deeply the German state has tied law, police power, archives, and wartime policy to racial ideology.

`ss_archive_control`

Represents SS access to records, research institutes, camp administration, and unofficial channels.

`ahnenerbe_influence`

Represents occult-pseudoscientific institutions gaining funding, access, and legitimacy.

`foreign_atrocity_awareness`

Represents foreign intelligence, resistance networks, and neutral diplomats learning enough to create condemnation.

`aryan_origin_preparation`

Represents the practical readiness to send the Tibet expedition.

Possible flags:

- `germany_racial_policy_decisions_unlocked`
- `germany_ss_archive_control_expanded`
- `germany_ahnenerbe_budget_protected`
- `germany_tibet_expedition_prepared`
- `germany_tibet_expedition_blocked`
- `germany_holocaust_policy_radicalized`
- `germany_foreign_atrocity_awareness_rising`

These values should interact with the Mengele chain but not require it.

Example:

- Auschwitz Experiments increase SS archive control and foreign atrocity awareness risk.
- Restricting Mengele slows SS autonomy but does not necessarily block Ahnenerbe influence.
- The Angel of Death coup can damage or distort the Tibet expedition route because Germany’s racial policy apparatus is no longer fully under Berlin.

## 27. Atrocity Policy Decisions

The decision layer should include several serious choices. These should be abstract and consequence-heavy.

### 27.1 Centralize the Race Offices

Purpose:

Germany consolidates racial bureaucracy under a smaller number of party and SS offices.

Effects:

- increases racial policy radicalization
- increases SS archive control
- unlocks later archive and ancestry decisions
- small stability or political power effect depending on regime strength
- increases hidden condemnation memory
- can increase resistance in occupied territories

Narrative role:

The regime becomes more coherent in its crimes, which makes later ideological projects easier.

### 27.2 Protect the Ahnenerbe Budget

Purpose:

Germany protects funding for mythic, archaeological, anthropological, and pseudo-historical research.

Effects:

- increases Ahnenerbe influence
- unlocks Tibet expedition preparation
- may add a small research or propaganda bonus
- increases risk of strange later ideological branches
- creates future Tibet expedition memory

Narrative role:

The state begins treating myth-hunting as policy.

### 27.3 Classify the Eastern Records

Purpose:

Germany hides or reorganizes records from occupied territories and camp administration.

Effects:

- increases SS archive control
- delays foreign atrocity awareness
- increases condemnation if later exposed
- may reduce internal oversight
- can help Tibet expedition fabrication if physical evidence or archives are needed for the claimed thesis

### 27.4 Search for Ancestral Traces

Purpose:

German offices search occupied archives, museums, monasteries, and private collections for symbols, myths, and texts that can be folded into racial propaganda.

Effects:

- increases Aryan-origin preparation
- increases Ahnenerbe influence
- may unlock small event chains about contradictory evidence
- can lead to forged or selectively interpreted documents
- increases later chance of a “positive” Tibet expedition result


### 27.5 Silence the Dissenting File

Purpose:

Some officials, scholars, clergy, officers, or diplomats warn that the racial research apparatus is becoming irrational and diplomatically dangerous.

Effects:

- player can suppress the dissenting file, increasing radicalization and reducing oversight
- player can archive the objection, slowing the chain
- player can order military review, reducing Ahnenerbe influence but angering the SS

Narrative role:

The player chooses whether Germany can still hear internal objections.

### 27.6 Prepare the Tibet Mission

Purpose:

Germany converts ideological preparation into an actual expedition proposal.

Effects:

- unlocks the Tibet expedition decision chain
- requires enough Ahnenerbe influence or Aryan-origin preparation
- may require Germany to be fascist, sufficiently radical, and not cut off diplomatically
- if Germany is in severe war crisis, the mission may become more secretive or more desperate

## 28. Decision Costs and Consequences

The decisions should not be free buttons.

Possible costs:

- political power
- command power for security operations
- stability loss if internal institutions fight over authority
- resistance increase in occupied states
- condemnation memory
- future foreign intelligence exposure
- chaos increase
- reduction of diplomatic opinion with democratic, communist, and neutral countries once exposed
- increase of SS autonomy or factional instability

The player should feel that Germany is becoming more dangerous and more brittle.

Short-term effects may help the regime:

- propaganda control
- research speed
- occupation control
- special project speed
- intelligence access
- ideological influence

But the long-term price must remain present.

## 30. Tibet Expedition Historical Anchor

The real-world anchor is the 1938 to 1939 German expedition to Tibet led by Ernst Schäfer. Historically, the expedition mixed zoological and scientific collection, SS patronage, racial-anthropological interest, propaganda usefulness, and later myth-making.

Chaos Redux should use this as inspiration.

Important historical design cues:

- the expedition can be framed through Ernst Schäfer or a Schäfer-inspired expedition leader
- Himmler and the SS should be interested in the mission for ideological and mythic reasons
- the Ahnenerbe or a similar SS research network should be involved
- the expedition should include zoological, botanical, geographic, photographic, and anthropological cover work
- the mission should carry diplomatic risk because Tibet, British India, China, and neighboring powers are not passive map space

The in-game expedition can happen later than the historical one if the campaign conditions demand it. 

## 32. Expedition Routes

The expedition can have several possible routes depending on world state.

### Route A: Historical-Style Scientific Cover Mission

Conditions:

- Tibet exists or is accessible
- Germany has not openly collapsed diplomatically
- British India, China, or neighboring transit powers do not fully block the mission

Description:

The mission travels under scientific cover. It collects maps, plant samples, photographs, measurements, ritual observations, and local contacts. The racial thesis is written after the fact.

Gameplay:

- lower risk
- slower result
- stronger chance of ambiguous findings
- less immediate condemnation
- more dependent on Ahnenerbe influence to turn results into ideology

### Route B: Covert SS Mission

Conditions:

- war makes formal travel difficult
- Germany is already highly radicalized
- SS archive control or Ahnenerbe influence is high

Description:

The mission travels through covert channels, smugglers, sympathetic intermediaries, or wartime chaos. It is more secretive and more likely to produce a fabricated result.

Gameplay:

- higher risk
- higher chance of foreign discovery
- higher chance of forged “positive” result
- higher condemnation if exposed
- possible deaths or diplomatic incidents if the mission fails

### Route C: Holy Realm Contact Mission

Conditions:

- Holy Realm exists
- Tibet is Holy Realm or part of Holy Realm
- Germany can contact the Holy Realm through diplomacy, intermediaries, or covert expedition

Description:

This is the special Chaos Redux route. The expedition encounters a living spiritual-political state rather than ordinary Tibet. Germany tries to interpret the Holy Realm as evidence for its own racial myth. The Holy Realm may misunderstand, manipulate, reject, tolerate, or weaponize the encounter.

Gameplay:

- highest narrative value
- can unlock the “positive result” needed for later Teutonic Order and Final Crusade hooks
- should be dangerous because both sides may interpret each other through delusion
- may create foreign news rumors about Nazi envoys in the mountains
- may affect Holy Realm Mandala Reach, Compassion Drift, or foreign suspicion if integrated later

## 33. Initial Expedition Event: “The Tibet File Reopened”

Suggested event title:

- `The Origin Thesis`

Event purpose:

Germany receives an internal request to fund a Tibet expedition for racial-historical research. The event should announce “we will prove the master race.” It should show the bureaucratic absurdity and danger: botanists, anthropologists, SS mystics, propagandists, and military intelligence all requesting authority over the same file.

Description direction:

An Ahnenerbe memorandum arrives with old photographs, maps, and lists of specimens. The language is scientific when it describes birds, barley, skull measurements, and mountain passes. It becomes stranger when it reaches origins, symbols, caste, blood, and destiny. The file does not contain proof. It contains hunger for proof.

Player choices:

### Option A: “Fund the expedition.”

Effects:

- starts Tibet expedition chain
- increases Ahnenerbe influence
- costs political power or civilian industry
- creates `germany_tibet_expedition_sent`
- increases hidden foreign suspicion
- may increase `aryan_origin_preparation`

### Option B: “Reopen the old files instead.”

Effects:

- starts archive recovery route
- cheaper
- lower chance of strong result
- increases propaganda preparation
- no immediate foreign travel risk

### Option C: “This is not a wartime priority.”

Effects:

- delays or blocks expedition
- reduces Ahnenerbe influence
- may anger SS ideological offices
- if Germany is highly radicalized, adds internal faction tension

## 34. Expedition Progress Events

The expedition should have a small chain of progress events. It should feel like a foreign mission moving through paperwork, terrain, suspicion, and ideology.

### 34.1 “Transit Papers”

Germany must secure a route.

Possible outcomes:

- formal travel allowed
- covert route required
- route blocked by British, Chinese, Soviet, Indian, or local authorities depending on map state
- mission delayed
- mission forced into the archive route

Choices can spend political power, intelligence resources, or accept risk.

### 34.2 “The Scientific Cover”

The expedition chooses what it is publicly.

Options:

- zoological and botanical mission
- geographic and photographic survey
- anthropological survey
- SS ideological mission under scientific disguise

Effects:

- scientific cover lowers detection
- ideological mission raises chance of “positive” result but raises exposure risk
- anthropological survey raises condemnation risk if exposed
- photographic survey creates later propaganda assets

### 34.3 “The Mountain Interpreters”

The expedition depends on guides, interpreters, local officials, monks, traders, or Holy Realm intermediaries.

Outcomes:

- cooperative local route
- unreliable translation
- resistance by local authorities
- Holy Realm-controlled interpretation if Holy Realm exists
- forged or selectively interpreted documents

This event should create one of the hidden result modifiers.

### 34.4 “The Symbol Problem”

The expedition encounters symbols, texts, ritual objects, or old photographs that German ideologues want to reinterpret.

This event should emphasize that symbols can be shared, borrowed, or misread. It should not imply Nazi conclusions are valid.

Choices:

- record cautiously
- hand the file to propagandists
- classify contradictory notes
- let Ahnenerbe write the interpretation

Effects:

- cautious recording lowers chance of strong result but lowers later instability
- propaganda interpretation increases chance of `master_race_claim_established`
- classifying contradictions increases hidden scandal risk

## 35. Holy Realm Contact Variant

If the Holy Realm exists and Tibet is the Holy Realm or part of it, the expedition should become stranger.

The Nazis are expecting a dead archive, remote monasteries, and fragments they can reinterpret.

Instead they find a state.

The Holy Realm may present itself as:

- a refuge
- a Mandala administration
- a Bodhisattva-led state
- a Buddha Mandate state
- a Divine Sovereignty state
- a late Final Silence state

The expedition’s outcome should depend heavily on which Holy Realm stage exists.

### 35.1 Refuge or Bodhisattva Stage

Germany finds a peaceful but disciplined mountain realm.

Possible interpretation:

- Nazis treat the Realm’s order as evidence of ancient hierarchy
- Holy Realm officials treat the Germans as confused but useful foreigners
- some Arhats refuse contact
- refugees report discomfort with German questions

Likely outcome:

- ambiguous result
- possible weak positive claim if Ahnenerbe influence is high
- Holy Realm gains foreign suspicion if contact is public
- peaceful Holy Realm may reject the mission, reducing chance of positive result

### 35.2 Arhat Administration Stage

Germany encounters ledgers, registers, vows, and disciplined bureaucratic spirituality.

Possible interpretation:

- German offices become fascinated by the registers
- Arhat administrators may provide curated documents
- the Holy Realm may use the Germans to extend Mandala Reach or test foreign vanity

Likely outcome:

- guaranteed chance of “positive” Nazi interpretation
- stronger event memory
- Mandala Reach gain for Holy Realm
- foreign intelligence rumors about German envoys in sacred offices

### 35.3 Buddha Mandate Stage

Germany encounters a state that already claims world-historical spiritual authority.

Possible interpretation:

- Nazi ideologues misread the Buddha Mandate as confirmation of sacred hierarchy
- the Holy Realm may see Germany as a violent and spiritually sick empire
- both sides may temporarily tolerate each other because each thinks it can use the other

Likely outcome:

- guaranteed chance of `germany_master_race_claim_established`
- Holy Realm may gain a hidden memory that Germany can be drawn into a later religious-political alignment
- foreign concern increases

### 35.4 Divine Sovereignty Stage

Germany meets a Holy Realm that has already moved beyond ordinary politics.

Possible interpretation:

- German ideologues are guaranteed to declare the encounter proof
- Holy Realm may frame Germany as a distant barbarian court kneeling before the Mandala without understanding it
- the contact may become the seed for later Blessed Hitler or Teutonic Order chains

Likely outcome:

- guaranteed chance of `germany_master_race_claim_established`
- strong later hook for Teutonic Order alignment
- stronger foreign concern
- possible Holy Realm event about whether to tolerate the Germans’ false reading

### 35.5 Final Silence Stage

Germany reaches a Holy Realm already moving toward final doctrine.

This should be extremely rare and dangerous.

Possible interpretation:

- German ideologues may see the Holy Realm as apocalyptic confirmation
- Holy Realm officials may barely care about Germany except as another record in the ledger
- the mission may return with documents that are not proof, but warning signs

Likely outcome:

- positive claim possible, but poisoned
- Final Silence Pressure may increase slightly if Holy Realm sees Germany as proof that the world cannot be reasoned with
- Germany gains a dangerous later hook, but also foreign panic

## 36. Expedition Result System

The expedition should resolve into one of several outcomes.

### Outcome A: No Usable Result

Germany returns with specimens, photographs, maps, and confused notes, but no useful ideological claim.

Effects:

- small propaganda disappointment
- Ahnenerbe influence falls
- no master race claim
- possible minor research or intelligence benefit
- no later Teutonic Order hook

### Outcome B: Ambiguous Result

Germany returns with fragments that can be used in propaganda but not enough for a full ideological breakthrough.

Effects:

- creates `germany_aryan_origin_claim_prepared`
- unlocks propaganda decision to force a stronger claim later
- increases foreign suspicion if publicized
- may slightly increase fascist support or war support
- no direct Teutonic Order hook yet unless later upgraded

### Outcome C: Fabricated Positive Result

Germany manufactures a clear claim by suppressing contradictions, editing files, or forcing the interpretation.

Effects:

- creates `germany_master_race_claim_established`
- increases fascist support or ideological drift
- increases Ahnenerbe influence
- increases condemnation memory if exposed
- unlocks later Teutonic Order alignment hook
- may increase chaos slightly because propaganda myth becomes policy

### Outcome D: Holy Realm Confirmed Claim

This is the special Chaos Redux route. It should be called “confirmed” only in the sense that German institutions believe they received confirmation, or the Holy Realm gave them something they interpreted as confirmation.

Effects:

- creates `germany_master_race_claim_established`
- creates `germany_holy_realm_contact_positive`
- creates `holy_realm_german_origin_claim_contact` if Holy Realm exists
- strong later hook for Teutonic Order, Final Crusade, and Blessed Hitler chains
- foreign rumor event if exposed
- stronger Mandala Reach or suspicion impact depending on Holy Realm stage

### Outcome E: Expedition Scandal

The expedition is exposed as pseudoscience, espionage, or ideological manipulation.

Effects:

- Ahnenerbe influence falls
- Germany loses diplomatic opinion with some countries
- foreign atrocity awareness may rise if linked to racial offices
- no master race claim unless Germany suppresses the scandal
- possible internal purge or cover-up decision

### Outcome F: Expedition Lost

The expedition disappears, is detained, or fails due to war, terrain, foreign interception, or Holy Realm refusal.

Effects:

- no direct result
- Ahnenerbe influence may fall or radicalize further
- Germany can attempt archive fabrication later
- foreign intelligence may gain documents

## 37. Master Race Claim Flag and Later Hooks

The main mechanical output for later specs is:

`germany_master_race_claim_established`

This flag should mean:

- German institutions believe they have obtained or manufactured proof for their racial-origin myth
- the claim is strong enough to affect state propaganda and later occult-political decisions
- later chains can use the flag to unlock Teutonic Order alignment, Blessed Hitler logic, Final Crusade hooks, and Atlantis delusions

This flag should not mean:

- Nazi racial theory is true
- the mod endorses the claim
- the Holy Realm agrees with Nazi ideology
- Tibet or Buddhism are actually Nazi in origin

These flags allow later branches to distinguish between honest failure, propaganda fabrication, and Holy Realm contact.

When tied with the Mengele event, then this flag would make Mengele units stronger, now they are "The Perfect Aryans", and there is a chance that they will overthrow Mengele, because they are stronger than twin clones army. So change the leader portrait to a perfect Aryan.

## 38. Player Choices After Expedition Return

Once the expedition returns or resolves, Germany should get a final decision event.

Suggested event title:

`The Expedition Returns`

Alternative titles:

- `The Files from Lhasa`
- `The Origin Thesis`
- `The Ahnenerbe Declares Its Findings`
- `Proof Enough for the State`

Player choices should depend on outcome.

### If result is ambiguous

Options:

1. Publish cautious findings
2. Give the file to propaganda offices
3. Classify the contradictions and demand a clear thesis

Effects:

- cautious findings give small benefit but no master race flag
- propaganda route can create or progress the prepared claim
- classified route increases hidden scandal and Ahnenerbe influence

### If result is fabricated positive

Options:

1. Declare the origin thesis proven
2. Keep the file for internal doctrine only
3. Suppress the more absurd claims

Effects:

- declaration creates the strongest later hooks but increases condemnation and foreign suspicion
- internal doctrine keeps later hooks but less public news
- suppression reduces Ahnenerbe influence and may block later Teutonic Order path

### If Holy Realm positive contact occurred

Options:

1. Declare the Holy Realm connection as proof
2. Hide the Holy Realm contact and use it internally
3. Send a formal return mission later

Effects:

- public declaration increases foreign concern and later Teutonic Order likelihood
- hidden internal use creates later secret hooks
- return mission can be reserved for later Final Crusade or Teutonic Order spec

## 39. Foreign and Holy Realm Reactions

### Holy Realm Reaction

If Holy Realm exists and Germany contacted it, the Holy Realm should get a reaction event.

The tone depends on Holy Realm stage.

Peaceful Holy Realm:

- discomfort with German racial questions
- possible refusal to host further missions
- possible reduction of Mandala Reach toward fascist powers
- slight chaos reduction if the Realm chooses restraint and distance

Arhat or Buddha Mandate Holy Realm:

- debate over whether Germany can be used, corrected, or contained
- possible Mandala Reach gain
- hidden memory for later Teutonic Order chain
- internal dispute between compassion and political opportunity

Divine Sovereignty Holy Realm:

- Germany is treated as another court seeking meaning from the Mandala
- high chance of curated contact
- later alignment hook becomes stronger

Final Silence Holy Realm:

- Germany is recorded as evidence of world sickness
- contact may increase Final Silence Pressure slightly
- later alignment is possible but poisoned by apocalyptic doctrine

### Allied Reaction

Allied powers may receive intelligence events:

- German SS expedition files recovered through informants
- rumors about racial research missions
- concern about German contact with Holy Realm
- possible intelligence operation to expose the mission

### Soviet Reaction

The Soviet Union may frame the expedition as proof that fascism has replaced science with myth.

If at war with Germany, this can give:

- propaganda boost
- war support
- anti-German opinion modifier
- increased willingness to fund intelligence or partisan operations

### Neutral Reaction

Neutral countries should react with uncertainty:

- scientific unease
- diplomatic discomfort
- rumors of German agents in the Himalayas
- refusal to handle German research shipments if exposure is high

## 40. Condemnation, Chaos, and Event Logs

### Condemnation

The Tibet expedition itself should not carry the same condemnation as Auschwitz or atrocity policy. It becomes condemnable when linked to:

- SS racial offices
- camp records
- coercive anthropology
- atrocity documentation
- fabricated evidence used to justify persecution or conquest

Possible condemnation triggers:

- expedition scandal exposed
- racial policy decisions exposed
- Holy Realm contact used for Nazi propaganda
- master race claim publicly declared
- Ahnenerbe files captured by foreign powers

## 41. UI Concept: The Expedition Dossier

This layer would benefit from a small dossier UI or decision-category visual treatment.

Suggested UI element:

`The Expedition Dossier`

It does not need to be as large as the Holy Realm UI.

### What the Player Sees

A classified file panel showing:

- expedition route
- cover identity
- Ahnenerbe influence
- SS archive control
- current result status
- foreign suspicion
- Holy Realm contact status if relevant
- gathered artifacts or files
- interpretation pressure
- final thesis status

### Visual Style

- old German file folder
- typed forms
- red classified stamps
- black censor bars
- route map to Tibet
- field photographs represented abstractly
- specimen tags
- archive string lines
- warning stamps for exposed or fabricated results

Avoid celebratory Nazi aesthetics. Use file-state visuals, not heroic expedition posters.

### Dossier States

1. Dormant file
2. Funding requested
3. Expedition prepared
4. In transit
5. In Tibet
6. Holy Realm contact
7. Results disputed
8. Thesis declared
9. Scandal exposed
10. File sealed

The UI can be a custom decision category background, a scripted GUI, or a simpler event panel if necessary.

## 42. AI Behavior

AI Germany should not spam the expedition every game.

Recommended AI logic:

AI more likely to pursue the chain if:

- Germany is fascist
- racial policy decision layer has advanced
- Germany has authorized Auschwitz Experiments or similar radical institutions
- Germany is seeking mythic or occult branches
- Holy Realm exists and is important in the world
- world chaos is already rising
- Germany is not in immediate collapse

AI less likely if:

- Germany is winning conventionally and does not need strange projects
- Germany is non-fascist
- Germany has restricted SS autonomy
- Germany is in civil war
- Germany lacks resources

## 44. Failure and Cleanup Paths

The expedition needs clean endings.

If Germany changes ideology:

- cancel expedition preparation
- remove Ahnenerbe influence growth
- block master race claim
- possible post-regime file exposure event

If Germany loses war access or route:

- expedition delayed or forced into archive route
- possible failure event
- no hard lock unless alternative archive route exists

If Mengele coup occurs during expedition:

- expedition can be recalled, lost, or seized by SS offices
- if Mengele faction wins, the Tibet chain should either collapse or mutate into a later separate branch
- give automatically Mengele the master race claim

If Holy Realm rejects the mission (rare):

- Germany can return with no result, fabricate anyway, or attempt a covert route
- Holy Realm gains event memory
- future Germany-Holy Realm relations worsen unless later ideology overrides it

If expedition is exposed:

- increase foreign suspicion
- possible condemnation
- reduce acceptance of later German diplomacy
- allow Germany to suppress, deny, or double down




