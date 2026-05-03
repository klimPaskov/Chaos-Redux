# Camps, Genocide Crisis, AI Behavior, and Discovery-Based Condemnation System

## Purpose

This system adds a dark state-repression and atrocity mechanic to Chaos Redux. A country can use it, but it should create deaths, population loss, internal instability, and long-term consequences.

Foreign condemnation should not rise automatically just because a country builds camps. Most countries should not know the full scale of the atrocities while the original regime still controls the affected states.

Condemnation should mainly increase when enemy forces occupy or liberate states containing camps, because that is when the evidence becomes visible to the outside world.

## Core Additions

Add two new building types:

1. Concentration Camps
2. Extermination Camps

Both buildings interact with the existing Chaos Redux civilian deaths system. They also interact with the condemnation system through discovery events, not passive monthly condemnation.

## Main Design Rule

Camps should have two layers:

1. Hidden internal damage
2. External condemnation after discovery

While the original regime controls the state, the system tracks deaths, population loss, and internal crisis.

When an enemy country occupies or liberates a state with camps, the camp system becomes exposed and condemnation rises against the responsible regime.

## Concentration Camps

### Availability

Concentration camps can be built by any country, regardless of ideology.

### Cost

They should be free or relatively cheap in construction cost, but costly through internal effects, deaths, and possible later exposure.

### Main Function

Concentration camps represent a general repression system. They give the regime short-term control but damage the state over time.

### State Effects

When built in a state, the building applies a state modifier such as:

```txt
concentration_camp_presence
```

Possible effects:

```txt
Concentration Camp Presence

Effects:
- Reduces state population slowly over time
- Reduces recruitable population factor
- Slightly reduces local resistance in the short term
- Reduces compliance growth
- Slightly increases local output
- Increases very slightly hidden atrocity score
- Can trigger domestic leaks, sabotage, refugee, and resistance events (the more camps exist, and depends on the country's stability. So, for example, countries with strong stability and high party popularity would never really have those events)
```

### Design Notes

Concentration camps should not create automatic global condemnation. They should create hidden atrocity score. Condemnation should rise once the camps are discovered by an enemy occupier or through a specific exposure event (firing once on first discovery, on subsequent discoveries don't fire an event, as it would become spammy. Add a cooldown).

## Extermination Camps

### Availability

Extermination camps can only be unlocked by:

- Fascist countries
- Communist countries
- Countries that unlock the relevant Chaos Doctrine path

This allows any country to reach this mechanic through an extreme Chaos Doctrine branch, while still keeping it ideologically restricted by default.

### Main Function

Extermination camps are an extreme escalation of the repression system. They are not a better version of concentration camps. They represent the regime crossing into systematic mass killing.

### State Effects

When built in a state, the building applies a state modifier such as:

```txt
extermination_camp_network
```

Possible effects:

```txt
Extermination Camp Network

Effects:
- Severely decreases state population over time
- Sharply reduces recruitable population
- Collapses compliance growth
- Increases resistance after an initial delay (if the regime is getting weaker, strong stability and ideology won't have problems with it)
- Increases hidden atrocity score
- Increases refugee pressure
- Can activate war crimes consequences if the regime loses a major war
```

### Design Notes

Extermination camps should be mechanically dangerous. They may give short-term extremist support or control, but they should also create major state damage, resistance, internal crisis, and a severe condemnation spike if discovered.

### State-Level Tracking

The most important part is storing who is responsible. If an enemy later occupies the state, condemnation should target the regime that built or operated the camps, not the country that discovers them.

## Discovery-Based Condemnation

Condemnation should trigger when an enemy country occupies or liberates a state containing concentration camps, extermination camps, gulags, or similar atrocity infrastructure.

## Discovery Events

When a camp is first discovered, fire an event for the discovering country, the responsible country, and a news event if it was an extermination camp. Subsequent camps won't fire the news event.
Also, subsequent camps increase condemnation less and less. The first ones add the most.

### Discovering Country Event

```txt
Camp Network Discovered

Enemy forces have entered a state containing evidence of a camp network. Reports from soldiers, local survivors, and captured records confirm large-scale imprisonment and deaths.

Effects:
- Increase condemnation against the responsible country
- Increase war support
- Unlock propaganda or tribunal decisions
- Increase support for continuing the war
```

### Responsible Country Event

```txt
The Camps Are Exposed

Enemy forces have occupied one of our camp sites. Evidence has begun spreading through foreign channels, and the regime can no longer fully control the story.

Effects:
- Large condemnation increase
- Stability loss
- Possible hardliner anger
- Possible cover-up or evidence destruction decisions
```

### Global Event

```txt
Evidence of Mass Atrocities

Reports from occupied territory describe a system of camps, deportations, forced labor, and mass death. Foreign governments are now under pressure to respond.

Effects:
- Major powers gain condemnation reaction decisions
- Democratic countries gain war support
- Refugee and tribunal chains can activate
```

## Evidence Destruction

Before retreating, the responsible country can try to destroy all the camps.

Possible decision:

```txt
Destroy Camp Evidence

Requirements:
- Owns or controls a state with camps
- Enemy troops are near the state
- Camp has not already been discovered

Effects:
- Reduces evidence level
- Reduces later condemnation spike
- Kills additional civilians or prisoners
- Increases hidden atrocity score
- Can fail and make condemnation worse
```

This gives the player and AI a dark crisis choice. Trying to hide the crimes can reduce immediate exposure, but it should also add more deaths and risk harsher events if discovered anyway.

## Genocide System

Building extermination camps or taking certain extreme decisions activates a national crisis category:

```txt
genocide_crisis
```

This crisis should track how far the regime has escalated, how much evidence exists, and how much internal resistance is forming.

### Possible Decisions

```txt
Genocide Crisis Decisions

- Expand camp network
- Intensify deportations
- Hide evidence from foreign observers
- Suppress internal reports
- Redirect trains and supplies
- Deal with resistance sabotage
- Handle refugee waves
- Manage military objections
- Destroy camp evidence during retreat
- Cover up liberated camps
```

### Crisis Variables

Possible tracked values:

```txt
genocide_escalation
genocide_visibility
genocide_deaths
genocide_resistance_pressure
genocide_foreign_pressure
genocide_coverup_effort
genocide_discovered_sites
```

### Crisis Effects

Higher escalation can cause:

- More deaths
- More resistance in affected states
- Refugee events in nearby countries
- Military or party dissent
- Stability loss
- Post-war trials after discovery
- Leader removal after defeat
- Possible civil war if the regime collapses

Foreign pressure should mostly rise after discovery, not automatically.

The more decisions are taken in the genocide crisis decision category, the less negative effects there will be, but there will be more deaths in states and stronger crisis after discovery.

## Political Effects

Avoid making genocide a simple source of party popularity. It should give more bonuses.

A better approach is to represent extremist hardliner support as a temporary political benefit with serious costs.

Hidden national spirit (all effects shown in the decision category dynamically):

```txt
Radical Hardliner Support

Effects:
- Small ruling party popularity gain
- Slight political power gain
- Stability reduced
- Democratic support reduced
- Neutral support reduced
- Resistance target reduced in affected states
- Hidden atrocity score increased
```

Condemnation is not added here unless the camps are exposed.

## AI Behavior Overview

The AI should be able to use these mechanics, especially when playing countries that historically carried out large-scale atrocities. The system should not rely only on the player. If Germany stays fascist and follows a historical or radicalized path, the AI should be likely to enter the genocide mechanics and carry out the Holocaust chain. It should be immersive and actually feel like recreation of the genocide with deep mechanics.

AI behavior should be weighted by ideology, national focus path, war situation, occupied territory, doctrine choices, stability, and world tension. The system should feel historical when the AI follows historical paths, while still allowing alternate-history outcomes.

### AI Behavior Principles

AI countries should not randomly build extermination camps without context. They should need a political reason, ideology, doctrine unlock, national spirit, event chain, or crisis escalation.

Good AI triggers:

```txt
AI should consider camp mechanics if:
- Country has fascist or communist government
- Country has unlocked the Chaos Doctrine atrocity branch
- Country controls occupied states with high resistance
- Country has a national focus or event chain connected to mass repression
- Country is in a major war
- Country has low stability and radical leadership
- Country has existing hidden atrocity score and chooses to escalate anyway
```

Bad AI triggers:

```txt
AI should avoid camp mechanics if:
- Country is democratic or neutral without Chaos Doctrine escalation
- Country has high stability and low resistance
- Country is dependent on foreign trade and fears later exposure
- Country is losing a war badly and needs manpower
- Country has recently suffered a revolt or tribunal event
```

## Germany AI and Holocaust Mechanics

Germany should have the most developed country-specific genocide chain. If Germany remains fascist, follows its historical leadership path, and enters the war in Europe, the AI should be highly likely to activate the Holocaust chain.

### Germany AI Behavior

Germany AI should likely escalate through these stages if it remains fascist:

1. Legal discrimination and exclusion
2. Forced registration
3. Deportation system
4. Concentration camp expansion
5. Occupied territory camp network
6. Extermination camp unlock
7. Cover-up and information control
8. Resistance sabotage and enemy discovery events
9. Liberation and war crimes exposure

### Germany AI Weights

Possible behavior:

```txt
Germany AI:
- Very likely to use concentration camps if fascist and at war
- Very likely to escalate after occupying Poland
- More likely to escalate after war with the Soviet Union begins
- More likely to hide evidence if enemy troops approach camp states
- More likely to intensify deportations if resistance is high
- Less likely to stop unless Germany is collapsing, occupied, or under coup pressure
```

### Germany-Specific Decisions

```txt
German Genocide Decisions

- Expand the camp network in occupied Poland
- Intensify deportations from occupied Europe
- Redirect rail capacity to deportation logistics
- Suppress reports from camp administrators
- Crack down on resistance rescue networks
- Accelerate extermination policy
- Destroy evidence during retreat
```

### Germany-Specific Consequences

```txt
Consequences:
- Large civilian death count (not from German core states)
- Severe population loss in targeted states
- Hidden atrocity score rises quickly
- Occupied states become more unstable over time
- Resistance sabotage becomes more frequent
- Condemnation spikes when camps are discovered
- Allied countries gain war support after discovery
- Post-war tribunal chain becomes harsher after discovery
```

## Japan AI and Occupation Atrocity Mechanics

Japan should have its own atrocity mechanics instead of copying Germany directly. Japan's system should focus on occupation violence, forced labor, massacres, biological warfare links, and colonial exploitation.

This can connect strongly to the existing Chaos Redux chemical and biological warfare systems.

### Japan AI Behavior

Japan AI should become likely to use severe occupation mechanics when:

```txt
JAP = {
    has_government = fascism
    has_war = yes
    any_owned_state = {
        is_core_of = CHI
    }
}
```

Japan should not automatically use the Holocaust-style extermination path. It should have a separate Imperial Occupation Crisis.

### Japan-Specific Crisis

Possible crisis category:

```txt
imperial_occupation_crisis
```

Possible decisions:

```txt
Japanese Occupation Decisions

- Expand forced labor camps
- Conduct anti-partisan reprisals
- Intensify occupation terror
- Exploit occupied industry
- Suppress Chinese resistance cells
- Transfer prisoners to experimental facilities
- Hide evidence from foreign observers
- Escalate biological warfare research
- Destroy evidence before retreat
```

### Japan and Biological Warfare

Japan can have special interaction with biological warfare and experimental facilities.

Possible mechanics:

```txt
If Japan has advanced biological warfare research:
- Unlock prisoner experimentation events
- Increase hidden atrocity score
- Increase civilian deaths
- Increase outbreak risk
- Increase chance of uncontrolled disease spread
- Increase post-war tribunal severity after discovery
```

This fits Chaos Redux well because Japan can become one of the main AI users of biological atrocity systems.

### Japan AI Weights

```txt
Japan AI:
- Likely to use forced labor camps in occupied China
- Likely to escalate occupation terror if Chinese resistance is high
- Likely to use biological warfare paths if already researching bioweapons
- Less likely to build extermination camps unless it has Chaos Doctrine escalation
- More likely to trigger massacre and forced labor events than Holocaust-style camp chains
- More likely to destroy evidence if enemy troops approach occupied atrocity sites
```

### Japan-Specific Consequences

```txt
Consequences:
- Chinese states lose population
- Resistance increases over time
- Outbreak risk increases if biological warfare is used
- Hidden atrocity score rises
- Condemnation spikes when enemy forces discover sites
- United States and Allied countries gain stronger intervention pressure after discovery
- Post-war tribunal chain can include occupation atrocities and biowarfare crimes
```

## Soviet Union AI, Gulag System, and Mass Repression

The Soviet Union should also have special mechanics, but it should not simply copy Germany's extermination camp system by default. The Soviet system should focus on gulags, mass deportations, purges, forced labor, political repression, ethnic deportations, and famine-related state violence.

Under extreme paths, the Soviet Union can escalate into systematic genocide mechanics through decisions, crises, or Chaos Doctrine unlocks.

### Soviet AI Behavior

The Soviet AI should use gulag and mass repression mechanics if it remains Stalinist, enters deep internal crisis, faces high resistance, or follows an extreme communist path.

Possible triggers:

```txt
SOV = {
    has_government = communism
    has_country_leader = stalin
}
```

The exact leader trigger can be adjusted during implementation.

### Soviet-Specific System

Possible crisis category:

```txt
gulag_and_mass_repression_system
```

This system should be available before extermination camps. It should represent forced labor and political repression.

Possible decisions:

```txt
Soviet Repression Decisions

- Expand the Gulag network
- Deport suspected opposition groups
- Intensify forced labor quotas
- Purge regional administrators
- Suppress nationalist resistance
- Transfer prisoners to remote labor camps
- Confiscate food from disloyal regions
- Crack down on internal dissent
- Conceal camp death rates
- Expand NKVD authority
- Destroy camp records during retreat
```

### Soviet Gulag Building or Modifier

The USSR could use a special building or state modifier:

```txt
gulag_labor_camp_network
```

Possible effects:

```txt
Gulag Labor Camp Network

Effects:
- Adds fixed civilian deaths
- Reduces local population slowly
- Adds temporary construction or resource extraction bonus
- Reduces stability over time
- Increases internal fear
- Increases resistance in non-core or occupied states
- Increases hidden atrocity score
- Can trigger famine, deportation, and purge events
- Can cause condemnation if discovered by enemy occupation
```

### Soviet Escalation Into Genocide Crisis

The Soviet Union should be able to escalate into genocide crisis mechanics under extreme conditions.

Possible escalation triggers:

```txt
Soviet escalation can happen if:
- Stalinist path remains active
- Chaos Doctrine atrocity branch is unlocked
- Resistance in border regions is high
- The USSR is losing a major war
- The USSR controls hostile occupied territory
- Internal paranoia variable is high
- Purge mechanics have been heavily used
```

Possible target categories:

```txt
Targeted repression categories:
- Political opposition
- Nationalist movements
- Deported ethnic groups
- Occupied populations
- Borderland populations
- Religious communities
- Suspected collaborators
```

### Soviet AI Weights

```txt
Soviet AI:
- Likely to expand gulag mechanics under Stalinist rule
- Likely to use deportation decisions against high-resistance border regions
- Likely to use purges during internal instability
- More likely to escalate if Chaos Doctrine atrocity branch is unlocked
- Less likely to build German-style extermination camps unless it has taken extreme doctrine or crisis decisions
- More likely to use forced labor, deportation, famine pressure, and purge mechanics
- More likely to destroy records if enemy troops approach gulag states
```

### Soviet-Specific Consequences

```txt
Consequences:
- Population loss in targeted regions
- Long-term stability damage
- Lower recruitable population
- Higher internal paranoia
- Higher resistance in non-core regions
- Possible military penalties if purges go too far
- Hidden atrocity score rises
- Condemnation spikes if enemy forces discover camps or records
- Post-war tribunal or internal reckoning events if regime collapses
```

## Country-Specific AI Summary

### Germany

Germany should be the main AI country for the Holocaust chain if it remains fascist.

```txt
Germany AI priority:
- Concentration camps
- Deportation network
- Extermination camps
- Holocaust-specific events
- Cover-up decisions
- Discovery events after enemy occupation
- War crimes exposure after defeat
```

### Japan

Japan should focus on occupation atrocities, forced labor, massacres, and biological warfare escalation.

```txt
Japan AI priority:
- Forced labor camps
- Occupation terror
- Anti-partisan reprisals
- Prisoner experimentation if biowarfare is developed
- Biological outbreak risks
- Discovery events after enemy occupation
- War crimes exposure after defeat
```

### Soviet Union

The USSR should focus on gulags, mass deportations, purges, forced labor, and political repression, with possible escalation into genocide crisis under extreme paths.

```txt
Soviet AI priority:
- Gulag expansion
- Deportations
- Purges
- Forced labor quotas
- Famine pressure events
- Borderland repression
- Extreme escalation if Chaos Doctrine or paranoia paths are active
- Discovery events after enemy occupation
```

## World Reaction After Discovery

This system should connect directly to the existing Chaos Redux condemnation system, but only after camps or records are exposed.

### Condemnation Thresholds

Add more purpose to the condemnation system as well:

```txt
Condemnation 25:
Foreign newspapers report discovered camp evidence.

Condemnation 50:
Neighboring countries receive refugee and survivor testimony events. (if caused from camps)

Condemnation 75:
Major powers unlock sanctions, embargo, propaganda, or intervention decisions.

Condemnation 100:
War crimes tribunal system activates if the responsible regime loses a major war.
```

### Possible Foreign Responses

- Diplomatic condemnation
- Trade penalties
- Embargoes
- War support against the responsible country
- Covert support for resistance movements
- Refugee aid decisions
- Intervention decisions
- Post-war tribunal events

## Historical Starting Camp and Repression Locations

Some countries should begin with camp, gulag, occupation, or repression mechanics already present. The exact state IDs should be selected by checking the vanilla HOI4 state files and the mod's existing state setup.

The goal is to make the system feel present from the start of the campaign, while still allowing later escalation through decisions, focus paths, doctrine, war, occupation, and AI behavior.

Starting mechanics should usually be represented through state modifiers, country flags, hidden variables, or locked decisions. They should not always require a visible building in 1936 if the historical site was not yet active. For some locations, a dormant state flag or delayed event is better than a full camp building at game start.

### Starting Setup Types

```txt
Level 1: Existing Repression Infrastructure
Used for states or countries where camp, forced labor, police repression, or prison camp systems already existed in 1936.

Level 2: Dormant Historical Site
Used for locations that became important later, but should already have a hidden marker so future events can activate them cleanly.

Level 3: Future Expansion Target
Used for historically important later camp areas that should become available through decisions, war, occupation, or country-specific chains.
```

## Germany Historical Starting Setup

Germany should definitely start with early concentration camp mechanics under fascist rule.

In the 1936 start, Germany should have existing repression infrastructure. This should not be the full Holocaust system yet. It should represent early Nazi camp and police repression systems before wartime mass extermination.

### Germany 1936 Starting State

Germany should also have at least one active or semi-active camp site through state modifiers or hidden state flags.

Recommended historical anchors (you add more):

```txt
Dachau area:
- Active early concentration camp site
- Should be represented from 1936 if the map state supports it

Sachsenhausen area:
- Can be active or activate through an early 1936 event
- Good site for SS camp administration growth

Buchenwald area:
- Future expansion target
- Should activate later through decision or event

Ravensbrück area:
- Future expansion target
- Should activate later through decision or event

Mauthausen area:
- Future expansion target after Austria is controlled
- Should activate after Anschluss or German control of Austria

Auschwitz area:
- Dormant historical site at game start
- Should activate only after Germany controls the area and the historical or alternate Auschwitz chain begins

And later camps in Poland, Soviet Union, etc.
```

### Germany Escalation Path

Germany should escalate from early concentration camps into the genocide system through:

```txt
Escalation sources:
- War in Europe
- Occupation of Poland
- Occupation of Soviet territory
- High fascist popularity
- Radical racial policy decisions
- SS archive control
- Auschwitz Experiments authorization
- Extermination camp decisions
- Chaos Doctrine atrocity branch
```

Auschwitz should be the central bridge between the genocide system and the Mengele chain.


## Japan Historical Starting Setup

Japan should definitely start with occupation and forced labor mechanics, but it should not start with a German-style extermination system.

Japan's starting setup should represent militarized empire, colonial control, forced labor, police violence, and early biological warfare infrastructure.

### Japan 1936 Starting State

Some recommended historical anchors (you add more):

```txt
Manchuria and Kwantung Army area:
- Starting occupation repression mechanics
- Forced labor and military police control
- Good anchor for Japan's occupation atrocity system

Harbin or Pingfang area if represented:
- Dormant or active biological experimentation site
- Can connect to Unit 731-style mechanics
- Should become stronger if Japan invests in biological warfare

Korea if represented through Japanese control:
- Colonial repression and forced labor mechanics
- Should not be treated as an extermination camp system by default

Occupied China after war begins:
- Future expansion target
- Unlocks forced labor camps, reprisals, massacres, and biological warfare events
```

### Japan Escalation Path

Japan should escalate through:

```txt
- War with China
- High Chinese resistance
- Kwantung Army influence
- Biological warfare research
- Chaos Doctrine atrocity branch
- Desperate war situation
- Occupation crisis decisions
```

Japan should mainly use forced labor, occupation terror, massacre events, prisoner experimentation, and biological warfare escalation. And later in China extermination camps.


## Soviet Union Historical Starting Setup

The Soviet Union should definitely start with gulag and mass repression mechanics.

The USSR should not start with a German-style extermination system. Its starting system should represent forced labor camps, political repression, deportation infrastructure, NKVD authority, and internal state violence.

### Soviet 1936 Starting State

Recommended historical anchors (you add more):

```txt
Kolyma or Far East mining regions:
- Gulag labor and extraction anchor

Vorkuta or northern Russia:
- Gulag labor camp anchor

White Sea or northern canal region:
- Forced labor infrastructure memory

Kazakhstan or Central Asia:
- Deportation and forced settlement anchor

Siberian interior:
- Remote camp network anchor
```

Exact state IDs should be chosen from the vanilla map and the mod's state setup.

### Soviet Starting Effects

The Soviet starting system should:

```txt
Effects:
- Unlock Gulag and Mass Repression decisions
- Add gulag labor camp state modifiers in selected remote states
- Add hidden atrocity score
- Add internal paranoia tracking
- Add deportation infrastructure flags
- Add forced labor or resource extraction bonuses where appropriate
- Add stability, resistance, or military risks if repression escalates too far
```

### Soviet Escalation Path

The Soviet Union should escalate through:

```txt
- Stalinist path remaining active
- Great Purge or purge-like mechanics
- High internal paranoia
- Borderland resistance
- War crisis
- Occupation of hostile territory
- Chaos Doctrine atrocity branch
- Famine pressure decisions
- Deportation decisions
```

The Soviet Union should use gulags, purges, deportations, forced labor, and famine pressure first. It should only enter full genocide crisis mechanics under extreme Stalinist, collapse, or paranoia.


## Other Possible Historical Starting Mechanics

Other countries may receive starting or dormant mechanics if historically justified, but Germany, Japan, and the Soviet Union should be the priority.

These should be lighter than the major country systems unless the country follows an extreme path.

Possible examples:

```txt
Italy:
- Colonial repression mechanics in Libya or East Africa if Italy controls relevant states
- Forced labor or punitive camp mechanics
- Lower scale than Germany, Japan, or the Soviet Union by default

Spain:
- Civil war repression mechanics after the Spanish Civil War starts
- Prison camps, reprisals, and political executions can be represented through events or state modifiers
- Should depend heavily on which side wins and how radical the government becomes

Nationalist China and Communist China:
- Wartime prison, purge, or internal repression mechanics may appear through crisis events
- Should not start as a major camp system by default

British Empire and France:
- Colonial detention or emergency repression mechanics can exist as dormant or event-based systems
- Should be politically costly if exposed
- Should not resemble extermination camp mechanics by default

Minor fascist or communist regimes:
- Can unlock camp systems through ideology, occupation, civil war, or Chaos Doctrine
- Should not receive large starting networks without specific historical or alternate-history support
- Generic genocide mechanics
```

## Auschwitz as a Shared System Node

Auschwitz should be treated as a special shared node between:

```txt
- Germany Holocaust mechanics
- Extermination camp mechanics
- Hidden atrocity score
- Discovery-based condemnation
- Auschwitz Experiments
- Mengele autonomy
- Biological warfare research
- Angel of Death coup risk
```

The Auschwitz area should begin as a dormant historical site if Germany does not control it. Once Germany controls the area and the correct conditions are met, the site can become active through event or decision.

## Mengele Integration With Genocide Mechanics

The genocide system must connect directly to the Mengele and Auschwitz Experiments chain.

Mengele should become more powerful when Germany expands extermination infrastructure, authorizes experiments, allows SS medical offices more autonomy, or uses Auschwitz as a biological research site.

The existing hidden value should be used if available:

### Mengele Autonomy Growth Sources

Mengele autonomy should increase from:

```txt
- Authorizing the full Auschwitz Experiments program
- Keeping Auschwitz Experiments active
- Building or activating extermination camps
- Expanding extermination camp networks in occupied territory
- Expanding Auschwitz-specific camp infrastructure
- Allowing prisoner transfers to experimental facilities
- Authorizing SS medical offices to bypass military review
- Choosing event options that reward biological results
- Ignoring missing records or abnormal laboratory reports
- Building more biological warfare facilities
- Using biological warfare special projects
- Germany being at war with the Soviet Union
- Germany being desperate, unstable, or highly radicalized
```

### Mengele Autonomy Reduction Sources

Mengele autonomy should decrease from:

```txt
- Restricting Auschwitz Experiments
- Closing the Auschwitz program
- Losing control of Auschwitz
- Placing military doctors or state inspectors over SS laboratories
- Purging SS medical offices
- Destroying laboratory records and facilities
- Germany changing away from fascism or Nazi-equivalent ideology
- Germany suffering civil war pressure
- Foreign bombing or sabotage against biological facilities
```

### Extermination Camp Scaling

Each active extermination camp should increase Mengele autonomy if Germany has authorized Auschwitz Experiments or placed SS medical offices in control.

Possible scaling:

```txt
No Auschwitz Experiments:
- Extermination camps increase genocide escalation
- Mengele autonomy does not increase, or increases very slightly

Restricted Auschwitz Experiments:
- Extermination camps increase Mengele autonomy slightly
- Biological research benefit remains limited

Full Auschwitz Experiments:
- Extermination camps increase Mengele autonomy strongly
- Biological research benefit increases
- Hidden atrocity score increases faster
- Angel of Death coup risk increases
```

### Experiment Permission Scaling

Mengele's power should grow based on how much the player or AI permits him to do.

Suggested permission levels:

```txt
mengele_permission_level_0:
Program rejected or shut down

mengele_permission_level_1:
Restricted camp administration

mengele_permission_level_2:
Limited experimental authority

mengele_permission_level_3:
Full Auschwitz Experiments authorized

mengele_permission_level_4:
SS laboratories bypass state and military oversight
```

Higher permission levels should increase:

```txt
- Mengele autonomy
- Biological research speed
- Biological special project speed
- Hidden camp deaths
- Hidden atrocity score
- Future discovery condemnation
- Angel of Death coup chance
- Strength of experimental units if the coup fires
```

Higher permission levels should also increase instability and future risk. The benefits should tempt the player, but the system should become more dangerous the longer it continues.

## Mengele Power Thresholds

Mengele autonomy should have thresholds that drive events and danger levels.

Suggested thresholds:

```txt
Low Autonomy:
- Normal Auschwitz Experiments effects
- Small research benefit
- No hidden danger

Medium Autonomy:
- Reports Without Names can fire
- SS medical offices begin hiding records
- Biological research benefits increase
- Hidden atrocity deaths increase faster

High Autonomy:
- The Twin Registers and Laboratory Without Berlin events can fire
- Military oversight decisions become important
- Extermination camps increase autonomy faster
- Angel of Death coup becomes possible later

Critical Autonomy:
- Rare disturbing reports can fire (like rumor that Mengele is preparing an army of aryan clones)
- Mengele network acts outside Berlin's control
- Coup checks become active if other conditions are met
- Losing Auschwitz can trigger exposure, collapse, or relocation events
```

Autonomy should not be shown directly unless the mod adds a dossier UI. The player should understand the danger through event text, decision tooltips, and warning modifiers.


## Mengele, Deaths, and Hidden Atrocity Score

The deaths system should record deaths from camps and experiments.

Experiment-related deaths should scale with Mengele autonomy and permission level.

Possible design:

```txt
Low autonomy:
- Small experiment death increases
- Mostly hidden

Medium autonomy:
- Regular hidden deaths from laboratory events
- Higher hidden atrocity score

High autonomy:
- Faster hidden deaths
- Stronger research benefits
- Stronger later condemnation if discovered

Critical autonomy:
- Exponential experiment death scaling
- Very high hidden atrocity score
- High chance of severe exposure after enemy occupation
- Angel of Death coup risk becomes serious
```

This should tie into the existing civilian deaths system. The player should be able to see aggregate deaths somewhere if Chaos Redux already has a deaths UI, but the full responsibility and evidence should remain hidden until discovery.

## Mengele and Discovery-Based Condemnation

Auschwitz and other experiment-linked camp sites should create stronger discovery effects than ordinary concentration camps.

If enemy forces occupy or liberate an experiment-linked site, the discovery event should check:

```txt
- Is this site Auschwitz or another SS laboratory site
- Was Auschwitz Experiments authorized
- What is Mengele autonomy
- What is the camp evidence level
- How many hidden deaths are recorded
- Were records destroyed
- Does Germany still exist
- Has the Angel of Death coup happened
```

Discovery of an experiment-linked site should:

```txt
Effects:
- Increase condemnation against Germany
- Increase condemnation against the Mengele faction if it exists
- Increase Allied and Soviet war support
- Unlock tribunal or evidence events
- Increase chaos if biological warfare facilities are involved
- Possibly expose biological warfare programs
```

If the Mengele faction already exists, it should receive extreme condemnation and diplomatic isolation. Germany should still receive condemnation if Germany authorized the original program or built the camp infrastructure. If Mengele Autonomy was high, but he hasn't done the coup yet, but his biological facility control states are being occupied by foreign forces, then he can spawn with his clone army and fight the invaders and save Germany. But later, when at peace, declare war on Germany.


## Mengele AI Integration

Germany AI should connect genocide decisions and Mengele decisions.

### AI Germany Should Increase Mengele Autonomy When

```txt
- Germany is fascist
- Germany has authorized Auschwitz Experiments
- Germany is losing or desperate
- Germany has high fascist popularity
- Germany has high chaos or high radicalization
- Germany owns or controls Auschwitz
- Germany controls several extermination camp sites
- Germany is pursuing biological warfare
- Germany is at war with the Soviet Union
```

### AI Germany Should Restrict Mengele When

```txt
- Germany is stable and winning conventionally
- Germany has low chaos
- Germany has low biological warfare investment
- Germany fears internal instability
- Germany has already received serious warning events
- Germany is close to civil war
- Germany has lost Auschwitz
```

AI Germany should not constantly choose maximum Mengele autonomy. The full Angel of Death path should remain relatively rare (but not impossible) unless the campaign is already extreme (high chaos) or Germany is desperate.


## Final Concept

Concentration camps are a general repression building available to all regimes. They create fixed ticking civilian deaths, slowly reduce state population, and give short-term control at the cost of internal instability and hidden atrocity score.

Extermination camps are an extreme escalation available to fascist, communist, or Chaos Doctrine countries. They severely reduce state population, massively increase civilian deaths, and activate a genocide crisis system with decisions, events, cover-ups, resistance, enemy discovery, and post-war punishment.

Germany should be the main AI user of the Holocaust chain when it remains fascist and follows its historical path. Japan should use a separate occupation atrocity system focused on forced labor, massacres, resistance suppression, and biological warfare. The Soviet Union should use gulag, purge, deportation, famine pressure, and mass repression mechanics, with possible escalation into genocide through extreme Stalinist or Chaos Doctrine paths.

The key change is that camps do not create automatic global condemnation while they remain hidden. They create hidden atrocity score. Condemnation rises when enemy forces occupy or liberate camp states and expose the evidence.
Also, add any historical starting locations for camps in countries. So Germany, Japan and Soviet Union must definitely have starting mechanics and camps somewhere. And some other countries might too have. And tie the system with Mengele as well for Germany.
