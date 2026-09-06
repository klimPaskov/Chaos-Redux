# Chaos Redux: Complete Mechanics Guide

Chaos Redux brings an unpredictable world to Hearts of Iron IV.
Wars, disasters, population losses, and unconventional weapons can deepen a crisis, while peace, relief, and preparation can help your country endure it.
This guide explains the shared systems, the choices they offer, and where to find them during a campaign.

## Table of Contents

1. [Core Event System](#core-event-system)
2. [Dynamic Timer System](#dynamic-timer-system)
3. [Event Classification](#event-classification)
4. [Chaos Meter System](#chaos-meter-system)
   - [Air Cleanliness](#air-cleanliness)
   - [Condemnation](#condemnation-system)
   - [Deaths](#deaths-system)
5. [Civilian Crises](#civilian-crises)
   - [Famine](#famine-mechanics)
   - [Migration](#migration-mechanics)
6. [World End Scenario Mechanic](#world-end-scenario-mechanic)
7. [Event Evolution](#event-evolution)
8. [Event Logs](#event-logs)
9. [Event Clusters](#event-clusters)
10. [Configuration and Settings](#configuration-and-settings)
11. [Triggerable Scenarios](#triggerable-scenarios)
12. [Multiplayer Compatibility](#multiplayer-compatibility)
13. [Chemical and Biological Warfare](#chemical-and-biological-warfare)
    - [Chemical Warfare](#chemical-warfare)
    - [Biological Warfare](#biological-warfare)
14. [Camps and Genocide Mechanics](#camps-and-genocide-mechanics)
15. [Chaos Warfare](#chaos-warfare)
16. [CBRN Command, Protection, and Diplomacy](#cbrn-command-protection-and-diplomacy)
17. [Special Units](#special-units)
18. [Campaign Tools](#campaign-tools)

---

## Core Event System

### Overview

Events respond to the state of the world and the history of your campaign.
Some bring local trouble, others reshape international politics, and some grow into much larger crises over time.

### Core Principles

- **Changing Conditions**: Available events depend on the countries, conflicts, and crises around you.
- **Campaign History**: Earlier events affect what can happen next and how likely it is.
- **Escalating Danger**: Higher Chaos brings shorter pauses and more dangerous developments.
- **Player Choice**: Settings let you choose which events are enabled and how quickly the campaign develops.

### Country Crises

When a local crisis can choose between countries, it is less likely to select one already facing several crises.
Crises that follow this rule share a limit of three active crises per country.
Worldwide dangers can still affect those countries.

Some crises also become more likely as an affected country approaches capitulation.
This can bring a late turning point, but it does not guarantee rescue or survival.

### World Threats

An existential danger can put the world under threat.
That danger can influence opportunities for cooperation and urgent responses, though countries still face their own political choices and conflicts.

---

## Dynamic Timer System

### Timer Mechanics

The pause between automatic events changes throughout the campaign.
At the default settings:

- **Opening Event**: The first countdown lasts 7–30 days.
- **Normal Pause**: Later countdowns begin from a range of 45–60 days.
- **Minor Events**: A run of smaller events gradually shortens the pause.
- **Major Events**: A major event clears that accumulated acceleration.
- **Minimum Pause**: The countdown cannot fall below 2 days.

### Timer Acceleration

Each minor event shortens the next countdown range by one day, up to a 15-day reduction.
Every three minor events also reduce the longest possible pause by another day, up to five extra days.

| Minor events since the last major event | Next countdown in a Calm World |
| --- | --- |
| 0 | 45–60 days |
| 1 | 44–59 days |
| 3 | 42–56 days |
| 6 | 39–52 days |
| 9 | 36–48 days |
| 12 | 33–44 days |
| 15 or more | 30–40 days |

### Chaos Effects on Timing

Chaos shortens these pauses further.
After a major event, the normal countdown range returns, but the current Chaos tier still affects it.

| Chaos tier | Countdown length compared with a Calm World | Shortest range after a long run of minor events |
| --- | --- | --- |
| **Calm World** | Normal | 30–40 days |
| **Gathering Storm** | 20% shorter | 24–32 days |
| **Rising Chaos** | 30% shorter | 21–28 days |
| **Chaos Tier** | 40% shorter | 18–24 days |
| **Totalen Chaos** | 50% shorter | 15–20 days |
| **World Collapse** | 50% shorter | 15–20 days |

<!-- IMAGE PLACEHOLDER: In-game event countdown beside the current Chaos tier. -->

---

## Event Classification

### Event Availability

An event needs suitable countries and world conditions before it can occur.
Every normal event also has a minimum Chaos tier.
An unavailable event shows **N/A** in the event list; its details explain the required tier.

These requirements are separate from the conditions for later evolutions and linked event groups.
Reaching the right Chaos tier makes an event possible, but does not guarantee it will happen next.

### Event Types

| Event type | How it behaves | What it means for the campaign |
| --- | --- | --- |
| **Fire-Once** | Can occur once per campaign. | Often begins as a local or regional development that may have lasting consequences. |
| **Repeatable** | Can occur several times, becoming less likely after each occurrence. | Recurring trouble remains possible, but the same event becomes less dominant over time. |
| **Major** | Becomes more likely as minor events occur, and can happen once. | Brings an immediate large change and resets the buildup toward other major events. |

The **Weight** shown in the event list describes relative likelihood, rather than a percentage chance.
With default settings, ordinary events begin at 1,000.
After a repeatable event occurs, its likelihood gradually recovers by 20 each month, up to a maximum that halves with each occurrence.

Major events build up from minor events.
The amount of that buildup adjusts to the mix of available major and ordinary events, so changing the event selection also affects pacing.

### Super Events

Major developments can appear as large illustrated announcements with music.
Their presentation marks the importance of the moment; the accompanying text explains what it means for the world.

<!-- IMAGE PLACEHOLDER: In-game super-event announcement showing its title, illustration, and description. -->

---

## Chaos Meter System

### Chaos Meter Overview

The global Chaos Meter measures world instability from 0 to 1,000 and beyond.
Every country shares the same world conditions, even when the immediate dangers differ from place to place.

<img width="480" height="80" alt="Chaos Meter at a low Chaos level" src="https://github.com/user-attachments/assets/315ecf14-8e84-4e42-9f85-1cfccbf78a9f" />

### Chaos Meter Window

Open the meter to explore five tabs:

1. **Status**: The current Chaos value and tier.
2. **History**: Changes to Chaos, with filters and sorting.
3. **Air Cleanliness**: Global contamination, its causes, and Air Winter conditions.
4. **Condemnation**: Public responsibility for unconventional warfare and atrocities.
5. **Deaths**: Civilian and military losses, including country totals and causes.

The window opens on **History**.

<!-- IMAGE PLACEHOLDER: In-game Chaos Meter window with all five tabs visible. -->

### Chaos Tiers

| Tier | Chaos | World conditions |
| --- | --- | --- |
| **Calm World** | 0–199 | Normal event pacing and the lowest level of instability. |
| **Gathering Storm** | 200–399 | Shorter pauses and some crisis evolutions. |
| **Rising Chaos** | 400–599 | More frequent events and further escalation. |
| **Chaos Tier** | 600–799 | Frequent events and many dangerous developments. |
| **Totalen Chaos** | 800–999 | Very short pauses and most evolutions within reach. |
| **World Collapse** | 1,000 or more | The highest Chaos tier, where world-ending crises may meet their requirements. |

### Chaos Sources

War, conquest, military expansion, and rising world tension increase instability.
Peace and liberation can reduce it.
Changes involving major powers usually have a larger effect.

| Action or condition | Effect on Chaos |
| --- | --- |
| War begins | +1, or +5 for a major change |
| Peace is made | −1, or −3 for a major change |
| Annexation | +2, or +10 for a major change |
| A puppet is created | +1, or +3 for a major change |
| Liberation | −2, or −5 for democratic liberation |
| A country is freed | −3 |
| Joining a faction | +1, or +3 for a major change |
| Leaving a faction | −1, or −3 for a major change |
| Monthly natural decline | −1 |

Ideological changes also affect Chaos: democratic changes reduce it, while other changes can raise it.

Further pressure comes from military growth, deaths, and pollution:

- **World Tension**: Each percentage-point increase adds 1 Chaos.
- **Military Buildup**: Every 100 military factories or 100 divisions contributes 1 Chaos.
- **Deaths**: Every million recorded deaths adds 1 Chaos.
- **Air Contamination**: Each percentage-point rise adds 1 Chaos; an equivalent recovery removes 1.
- **Nuclear Use**: Successive nuclear and thermonuclear strikes share a declining Chaos increase of 10, 5, 3, 2, then 1 per use.

Events can also change Chaos directly.

### Air Cleanliness

Air Cleanliness shows how much of the atmosphere remains clean and how much is contaminated.
Chemical contamination, disease outbreaks, nuclear fallout, wildfire smoke, and volcanic ash contribute to the global total.

Pollution can continue to build after the original attack or disaster.
Repeated nuclear strikes leave heavier and longer-lasting fallout, while recovering states gradually reduce their contribution.

#### Natural Recovery

The atmosphere slowly recovers while contamination remains reversible.
Recovery becomes weaker as pollution rises.

| Global contamination | Natural recovery each month |
| --- | --- |
| Below 25% | 0.03 percentage points |
| 25% to below 50% | 0.02 percentage points |
| 50% to below 75% | 0.01 percentage points |
| 75% to below 100% | 0.005 percentage points |

Ongoing pollution can outweigh this recovery.

#### Contamination Thresholds

| Contamination | Consequence |
| --- | --- |
| **25%** | Disease outbreaks spread more easily. |
| **50%** | Mild nuclear-winter conditions can begin. |
| **75%** | Severe nuclear-winter conditions can begin, and countries can form the Air Cleanliness Treaty. |
| **100%** | Atmospheric damage becomes irreversible and can lead to a contamination-driven world end when enabled. |

The **Air Cleanliness** tab shows the current total, recent changes, and the contribution of each source.
Select a source to see its history, including earlier pollution that has already cleared.

<!-- IMAGE PLACEHOLDER: In-game Air Cleanliness tab with one pollution source's details open. -->

#### Air Winter

Air Winter turns atmospheric pollution into a local struggle for survival.
States can pass through **Clear**, **Dimming**, **Crop Shock**, **Hard Freeze**, **Black Harvest**, **Ash Winter**, and **Terminal Winter**.

Conditions differ between states.
Local contamination, damaged infrastructure, occupation, and nearby severely affected states can worsen the danger.
Food reserves, shelter, adaptation, cleanup, and relief routes help reduce it.

- **Early Stages**: Food supplies and living conditions come under pressure.
- **Severe Stages**: Civilian deaths, disease, supply problems, and building damage become lasting threats.
- **Recovery**: Sustained improvements are needed before a state moves back toward safer conditions.

Use the Air Winter map mode to identify the hardest-hit regions and follow their recovery.

Choose priority states for relief and safer receiving states for evacuees.
Response projects include distributing respirators, supporting clinics, protecting crops and transport routes, building shelter, and preparing evacuations.
Severe conditions can force choices about abandoning an area or sealing bunkers.

<!-- IMAGE PLACEHOLDER: In-game Air Winter map showing several severity levels and an affected state's survival conditions. -->

#### Air Cleanliness Treaty

At 75% contamination, eligible countries can form a treaty to cooperate against the worsening atmosphere.
Members share basic observations and can support joint relief projects.

- **Global Cleaning Day**: A 45-day project that uses equipment, convoys, and civilian factories to reduce global contamination by one percentage point.
- **Joint Filter Convoy**: Aid for another member's severely affected priority state, improving protection and recovery and supporting a relief route for up to six months.
- **Verification Missions**: Inspections that test whether members are honoring their commitments.

Using unconventional weapons or refusing an inspection can lead to expulsion and sanctions from the remaining members.
Betrayal remains part of a country's treaty history.

<!-- IMAGE PLACEHOLDER: In-game treaty decisions showing a joint relief project and its requirements. -->

### Condemnation System

Condemnation measures the international response to publicly known unconventional attacks, atrocities, and cover-ups.
Responsibility can remain hidden until inspections, discovery, occupation, or published evidence expose it.

Chemical, biological, nuclear, atrocity, cover-up, and repeated-use consequences are shown separately.
Possessing weapons alone does not count as using them.

| Condemnation | International standing |
| --- | --- |
| Below 25 | Normal |
| 25–49 | International Concern |
| 50–99 | Formal Censure |
| 100–174 | Arms Embargo |
| 175–299 | Strategic Embargo |
| 300–499 | Total Embargo |
| 500 or more | Pariah State |

Concern and censure damage relations and military support.
Higher tiers can bring broader economic and diplomatic restrictions from participating countries.
Volunteers and attachés may be recalled, and new lend-lease agreements from sanctioning countries can be blocked.
Existing lend-lease agreements, production licences, and research-sharing arrangements can remain in place.

Trade embargoes require **By Blood Alone**.
Other economic and diplomatic sanctions still apply without that expansion.

Select a country in the **Condemnation** tab to inspect its public record, current penalties, recent incidents, and progress toward the next tier.

<!-- IMAGE PLACEHOLDER: In-game Condemnation country details showing recent incidents and current sanctions. -->

### Deaths System

The **Deaths** tab brings together military casualties and civilian losses from bombing, unconventional warfare, fallout, famine, repression, and dangerous displacement.
It shows worldwide totals, the civilian and military split, and country totals with causes.

Civilian losses reduce a state's population and have lasting consequences for the people and resources available there.
Moving to another state is counted as migration; people who die during dangerous journeys are recorded separately as deaths.

<!-- IMAGE PLACEHOLDER: In-game Deaths tab with a country's civilian and military losses and cause breakdown. -->

---

## Civilian Crises

Civilian crises can weaken a country far from the front line.
Food shortages force people to leave, damaged routes obstruct relief, and overwhelmed receiving areas struggle to provide shelter and supplies.

### Famine Mechanics

Famine follows conditions in individual states.
Its decisions appear when there is a food-security problem, while the famine map mode is available from the start of the campaign.

#### Food Security

Three values describe the situation:

- **Food Security**: How serious the shortage has become.
- **Food Reserves**: Supplies available to help people through a shortage.
- **Relief Access**: How easily food and assistance can reach those in need.

Food Security has five stages: **Stable**, **Supply Strain**, **Acute Shortage**, **Famine**, and **Catastrophic Famine**.
Production, transport, food demands, extraction, environmental damage, and relief all affect conditions.
Sustained severe shortages can cause civilian deaths.

#### Relief and Recovery

Available responses include releasing reserves, emergency imports, repairing routes, escorting relief convoys, airlifts, inviting outside assistance, and evacuating people from danger.
Taking supplies from safer areas can help one region while placing a burden on another.
Concealment and continued extraction can deepen the crisis.

Blockades become a famine threat when isolation and disrupted transport leave a state without adequate local supplies or relief.
Being an island alone does not cause famine.

<!-- IMAGE PLACEHOLDER: In-game famine map and relief decision showing Food Security, Food Reserves, and Relief Access. -->

### Migration Mechanics

People may flee danger within their own country or cross a border in search of safety.
Migration decisions appear when displacement, trapped populations, or reception needs become significant.
The migration map mode is available from the beginning of the campaign.

#### Displacement and Reception

Three values guide your response:

- **Displacement Load**: The pressure created by people forced from their homes.
- **Reception Capacity**: Your ability to receive and support them.
- **Border Policy**: The rules governing entry, transit, and return.

Policies range from open humanitarian reception and controlled entry to transit-only access, quarantine, or border closure.
Harsher policies may allow violent rejection or forced return where those choices are available.

Closed borders can leave people trapped in danger.
Receiving too many people without enough capacity can overcrowd safer states and strain their supplies.

#### Evacuation, Settlement, and Return

You can prepare evacuations, arrange corridors, prioritize transport, provide medical reception, distribute arrivals, or help them continue to another destination.
Longer-term choices include local integration, resettlement in another country, and return home.

Successful movement reduces the population at the origin and adds survivors to the destination.
Unsafe routes, violent rejection, and forced return can cause deaths.
Famine can drive further flight, while trapped populations add to the need for food and relief.

<!-- IMAGE PLACEHOLDER: In-game migration map showing an area of flight, a closed route, and a receiving state. -->
<!-- IMAGE PLACEHOLDER: In-game reception decisions showing Displacement Load, Reception Capacity, and Border Policy. -->

---

## World End Scenario Mechanic

Reaching 1,000 Chaos places the world in **World Collapse**.
A world end still needs its own conditions to be met; reaching the tier alone does not immediately end the campaign.

### Key Rules

- **Different Requirements**: Each ending depends on the crisis or world conditions behind it.
- **Separate Controls**: Available endings can be enabled or disabled individually in Event Details.
- **Automatic Events Stop**: Once a world end begins, ordinary automatic event firing stops worldwide.
- **Lasting Consequences**: The ending determines what kind of world remains and what survival means afterward.

Atmospheric collapse has a separate **Disable Fallout** setting.
Once that transition has begun, the setting cannot reverse it.

<!-- IMAGE PLACEHOLDER: In-game world-end details showing requirements and the enable/disable control. -->

---

## Event Evolution

An event's first appearance may only be the beginning.
Higher Chaos, earlier developments, and changing world conditions can allow it to evolve into a more dangerous crisis.

Check Event Details to see possible evolutions and their requirements.
An evolution has its own history entry, making it easier to follow a crisis across the campaign.

---

## Event Logs

The Event Logs window shows what has happened and what may still happen.

| Tab | What it shows |
| --- | --- |
| **Status** | An overview of event activity and pacing. |
| **History** | Past events, their dates, and the countries involved where relevant. |
| **Evolutions** | Crisis milestones and later developments. |
| **Events** | The event list, availability, likelihood, and enable/disable controls. |
| **Clusters** | Linked groups of events, their availability, and their members. |

You can filter the event list by enabled state, event type, or minimum Chaos tier.
Sorting helps you find events by number, occurrence count, or likelihood.

Select a row to open its details.
Several detail windows can remain open together, and cluster details let you inspect individual members.
Where an event has public world-end branches, each has its own details and checkbox.

<!-- IMAGE PLACEHOLDER: In-game Events tab with filters, sorting, and an event detail window open. -->

---

## Event Clusters

Clusters group related events into a connected burst of trouble.
They have their own availability requirements and can become possible at different Chaos tiers.
Individual members must also meet their own conditions.

A cluster does not guarantee that every member will occur.
The **Clusters** tab shows which members are available and what happened during a previous activation.

A linked burst normally counts as one development for event pacing, so several members do not each shorten the next pause.
You can enable or disable a whole cluster from its list or detail window.

<!-- IMAGE PLACEHOLDER: In-game cluster detail window showing available members and the cluster control. -->

---

## Configuration and Settings

### Event System Settings

Settings let you shape the campaign's pace and selection of events.

- **Enable or Disable**: Choose which countries participate in automatic events.
- **Event Selection**: Turn individual events or clusters on and off.
- **Manual Triggering**: Choose an event and start it directly.
- **Random Selection**: Pick an event at random before choosing whether to trigger it.
- **Force Trigger Mode**: Bypass normal restrictions for a manually chosen event.

<!-- IMAGE PLACEHOLDER: In-game event settings showing manual selection and Force Trigger Mode. -->

### Timer and Country Settings

Set the shortest and longest countdowns, then apply your changes.
The optional timer window keeps the current countdown visible during play.

Country controls support individual or group selection, continent filters, and enabled-only or disabled-only lists.
When switching the country you play, you can choose whether automatic events follow you and whether they stop for the previous country.

### Chaos Meter Configuration

You can adjust Chaos directly, jump to a chosen tier, or switch its effects on and off.
Ordinary Air Cleanliness processing also has its own control in the Air Cleanliness tab.

### Advanced Settings

- **Recovery Rate**: How quickly repeatable events regain likelihood after occurring.
- **Cap Reduction**: How much their maximum likelihood falls each time.
- **Major Event Buildup**: How strongly minor events increase the likelihood of a major event.
- **Chaos Timing**: How much each Chaos tier shortens or lengthens the countdown.

### Miscellaneous Settings

Adjust super-event audio, control the Fallout ending, and choose whether **Harder Crises for Players** is enabled.
That difficulty option increases pressure on player countries in the crises that support it and is enabled by default.

**Reset All Settings** asks for confirmation before restoring defaults.
The Help window provides guidance on the main controls.

<!-- IMAGE PLACEHOLDER: In-game Miscellaneous settings with audio and crisis-difficulty controls. -->

---

## Triggerable Scenarios

Open **Triggerable Scenarios** from Settings to choose a direct challenge setup.
Each entry offers a type selection and a four-level intensity slider.
Set both before pressing **Launch Scenario**.

Scenarios let you start a challenge without waiting for the normal event countdown.
They still need suitable countries and conditions, and may restrict repeated launches.

<!-- IMAGE PLACEHOLDER: In-game scenario controls showing the type selector, intensity slider, and Launch Scenario button. -->

---

## Multiplayer Compatibility

### Shared Systems

All players share the global event selection, Chaos Meter, and worldwide consequences.
A war, pollution crisis, or major development in one region can affect everyone.

### Country Controls

Participating countries have their own event countdowns.
Settings allow country selection, while events may affect one player, several countries, or the whole world.

---

## Chemical and Biological Warfare

Unconventional weapons combine military pressure with civilian harm, environmental damage, and international backlash.
Research and production are only part of the commitment: your country also needs protection, supplies, and the ability to manage the aftermath.

### Chemical Warfare

Chemical research unlocks basic weapons, while special projects develop more advanced options.
Available attacks depend on your research, equipment, policy, and preparation.

#### Chemical Raids

Chemical air and rocket raids target a selected state and require the matching weapons and delivery equipment.
Chemical aircraft equipment can be fitted to supported close-air-support and tactical-bomber designs.

An idle aircraft or an ordinary air mission does not release chemical weapons.
A chemical raid is a separate action with its own requirements and consequences.
An exposed failed attempt can still create diplomatic trouble.

<!-- IMAGE PLACEHOLDER: In-game chemical raid selection with its target, equipment requirements, and consequence warning. -->

#### Support Companies

Chemical tank detachments and projector units require their own equipment alongside protective and support supplies.
Their military benefits depend on keeping those supplies available.

Adding a chemical support company to a division does not automatically contaminate the battlefield.
Weapon use requires an available attack or operation.

#### Contamination and Protection

Chemical attacks can leave lasting state contamination.
Affected areas suffer disruption, medical pressure, and civilian harm, while pollution contributes to global Air Cleanliness.
Friendly forces can also be endangered by contaminated territory.

Gas masks, protective clothing, medical support, and decontamination reduce harm.
Research must be backed by equipment production, distribution, and replacement.

<!-- IMAGE PLACEHOLDER: In-game contaminated state beside military protection and cleanup options. -->

#### Chemical Doomsday Protocols

A fascist country close to capitulation can gain a last-resort decision to release its chemical stockpile across controlled territory.
It consumes the stockpile and can harm friendly and allied forces as well as enemies.
Widespread contamination, domestic losses, and diplomatic consequences can outlast the battle.

### Biological Warfare

Biological weapons are developed through special projects and require stockpiles for their available missions.
A successful attack can become a continuing outbreak with consequences far beyond the original target.

#### Strikes and Outbreaks

Special strike missions require suitable aircraft and weapons.
They can fail, partly succeed, or succeed, and can provoke international condemnation.

Some outbreaks spread to neighboring states.
Weak containment and chaotic conditions make a local crisis harder to control.
The type of outbreak affects its course and the response it needs.

<!-- IMAGE PLACEHOLDER: In-game outbreak map with affected states and their current conditions. -->

#### Countermeasures

Emergency hospitals, quarantine, treatment, and vaccination programs can reduce losses and help contain outbreaks.
Some threats need a sustained national response before they can be removed.

Respond early, maintain medical capacity, and keep protective supplies available when repeated outbreaks are likely.

<!-- IMAGE PLACEHOLDER: In-game outbreak-response decisions showing hospitals, quarantine, and medical programs. -->

#### Stockpile Safety

Large biological stockpiles carry an accident risk.
Accidents can cause outbreaks at home, while containment-safety research reduces the danger.
Facility damage and sabotage can worsen the danger at the national arsenal.
**Fail-Safe Containment Facilities** prevent ordinary stockpile accidents, but do not protect against attacks or deliberate releases.

#### Biological Doomsday Protocols

A last-resort biological release consumes the country's stockpile and causes harm across controlled territory.
It can create widespread domestic outbreaks with lasting population and diplomatic consequences.

---

## Camps and Genocide Mechanics

Repression can develop into networks of detention, forced labor, deportation, experimentation, and mass killing.
These systems cause civilian deaths, resistance, displacement, and international consequences when their crimes are exposed.

### Repression and Camps Window

The **Repression and Camps System** has five tabs:

- **Summary**: The overall crisis.
- **Territories**: Affected areas.
- **Sites**: Camp and restricted-site conditions.
- **Authority**: The regime's control and available measures.
- **Records**: The history and consequences of repression.

<!-- IMAGE PLACEHOLDER: In-game Repression and Camps System with an affected territory and site details visible. -->

### Camp Networks

- **Concentration Camps**: Detention, forced labor, and deportation.
- **Extermination Camps**: Systematic mass killing and severe consequences on discovery.
- **Gulag Networks**: Forced labor and mass repression.

Networks can also include experiment sites and contaminated sites, bringing further risks to prisoners and nearby populations.

Concentration camps are available through construction.
Further camp development and operation depend on the country's available decisions and circumstances.
Some countries begin with established repression networks; others develop them as political conditions change.

### Harm, Discovery, and Responsibility

Active repression reduces the population of affected states and can increase resistance and pressure to flee.
Concealment can keep evidence from becoming public, but does not prevent the underlying harm.

Inspections, discovery, occupation, and liberation can expose crimes.
Public responsibility follows the country that operated the sites, including after another country takes control of the area.
Destroyed records and failed cover-ups can bring additional condemnation.

### Crisis Choices

Available decisions depend on the country and the crisis.
They can involve camp administration, forced labor, deportation, concealment, inspections, reform, and foreign responses.
Escalation brings lasting human and political costs; exposure can lead to sanctions and pressure for accountability.

### Reform and Liberation

Reform and dismantlement can halt expansion and close active sites, while preserving the history of what happened there.
A country that discovers and controls a camp while at war with its operator can dismantle it, free surviving prisoners, and preserve evidence.
Closure can lead to redress and accountability, rather than erasing past responsibility.

---

## Chaos Warfare

Chaos Warfare is a military doctrine built around operating in chemical, biological, radiological, and nuclear danger, collectively called **CBRN**.
It combines protected formations, specialist headquarters, weapons programs, and supply commitments.

### Establishing the Doctrine

Adoption requires a qualifying weapons or protection program and costs **100 Army Experience**.
It starts a **90-day establishment mission**.

Establishment requires:

- 500 gas masks.
- 50 decontamination equipment.
- 100 support equipment.
- A deployed CBRN Operations HQ Section.
- A deployed Gas Mask and Decontamination Detachment.

Missing the deadline leaves the doctrine active, but offensive options remain closed until you complete the recovery requirements.

### Readiness and Institutions

**Chemical Readiness** measures how prepared the national program is, from 0 to 100.
Training alone cannot replace equipment, headquarters, and protective capacity.

Four institutional milestones allow higher readiness and stronger command options:

1. **Protective Foundation**: Establish dependable protection and production.
2. **Delivery Integration**: Combine weapons stocks, trained forces, and a completed protective headquarters order.
3. **Theater Exploitation**: Develop several doctrine branches alongside cleanup and intelligence capacity.
4. **Terminal CBRN Command**: Bring all four branches together with advanced protection and the required authority.

### Use Policies

Policy determines which kinds of operation your country may authorize.
The choices run from **Defensive Preparation** and **Retaliation Authority** to **Limited Battlefield Authority**, **Strategic Release Authority**, and **Unrestricted Chaos Warfare**.

Stronger authority requires more readiness, political and command resources, weapons stocks, and institutional progress.
Changing policy has a 90-day reassessment period.
Choosing a policy does not itself launch an attack.

### Mastery Tracks

Each branch costs **100 Army Experience** and develops through fielding its specialist units.
Research, supplies, and other requirements still apply to the formations and operations it makes available.

| Branch | Focus |
| --- | --- |
| **Hazard Assault Formations** | Protected infantry, movement through contaminated areas, pioneers, and Chaos Assault Battalions. |
| **Toxic Armored Warfare** | Protected tank crews, specialist armored support, and breakthrough logistics. |
| **Contaminant Fire Support** | Projector units, fire coordination, and specialist ammunition support. |
| **Integrated CBRN Command** | Reconnaissance, protective logistics, mobile decontamination, biological security, and theater headquarters. |

Hazard Assault Training offers a further way to develop the infantry branch, using masks and Army Experience for a temporary training program.
Some specialist equipment and formations require a separate commission after the necessary doctrine progress.

### Officer Corps

Officer-corps choices let you emphasize controlled retaliation, broader contamination warfare, or extreme offensive power.
These choices can improve planning, protection, combat performance, or cleanup, but aggressive approaches also increase supply needs and the harm caused by operations.

Division-level choices support mask discipline or specialist assault formations.
Chemical Operations Commanders help prepare headquarters orders more quickly.

Doctrinal discipline can reduce some condemnation penalties, but it does not remove civilian losses, contamination, or responsibility for an attack.

<!-- IMAGE PLACEHOLDER: In-game Chaos Warfare doctrine showing the four mastery tracks and an institutional requirement. -->

---

## CBRN Command, Protection, and Diplomacy

### Operations and Preparation

CBRN decisions bring together doctrine establishment, readiness, use policy, headquarters preparation, protection, and international responses.
Relevant categories appear as your program develops or when an incident needs attention.

Check each decision's requirements for equipment, Command Power, preparation time, and upkeep.
A shortage can prevent preparation or end an active benefit.

### Army Headquarters and Regimental Support

Six specialist headquarters companies cover operations, intelligence and weather, protective logistics, decontamination, medical response, and biological security.
They support orders such as a protective posture, a decontamination corridor, a medical response, or an infection cordon.

Larger forces require more resources.
Orders take time to prepare, remain active for a limited period, and can consume supplies each week.
Protection and containment can slow the army or increase supply use while reducing harm.

Headquarters preparation supports later operations; it does not select a target or launch a weapon.
Division support companies provide local protection, reconnaissance, cleanup, and medical assistance, with their benefits depending on reinforcement and supplies.

<!-- IMAGE PLACEHOLDER: In-game headquarters order showing preparation time, active duration, and supply cost. -->

### Protection and Civil Defence

Protection depends on equipment reaching the people who need it.
National programs build reserves, issue military masks, distribute civilian protection, replace filters, and maintain supplies.
Civilian programs cover eligible controlled states while stocks last.

Alarms, shelters, emergency distribution, and medical response help affected states cope with immediate danger.
Damaged or depleted protection needs replacement, and medical services can become overwhelmed.

### Decontamination

An active headquarters decontamination corridor and the required institutional progress allow cleanup assignments in contaminated controlled states.
Assignments cost masks, decontamination equipment, support supplies, transport, fuel, and political and command resources.
Heavier contamination is harder to clear.

Cleanup improves conditions, but past deaths and responsibility remain in the country's record.

<!-- IMAGE PLACEHOLDER: In-game civilian protection program and a contaminated state's cleanup decision. -->

### Military Industrial Organizations

Specialist industrial organizations support chemical munitions, air delivery, protective equipment, decontamination, detection, and biological protection.
Their benefits apply to the relevant equipment families.
Choose organizations that support the forces and protective programs you can afford to maintain.

### Attack Records

Unconventional attacks leave records of the countries involved, the target, the date, and the consequences.
Use the Event Log alongside Deaths, Air Cleanliness, and Condemnation to follow both the immediate harm and the continuing aftermath.
Public information depends on what has been discovered.

### International Response

Countries can demand inspections, publish evidence, send protective aid, join sanctions, respond to attacks, or destroy stockpiles as part of compliance.
These choices require political resources, equipment, or industrial capacity.

Evidence can expose previously hidden responsibility.
Cooperation and relief can help manage the crisis, while refusal and repeated use can deepen isolation.

### Protected Occupation Administration

Protected Occupation Administration increases garrison and protective-equipment demands while reducing garrison harm, improving compliance, and limiting resistance in vulnerable occupied territory.
Protective aid can also support occupied civilians during contamination, outbreaks, and other relevant local incidents.

---

## Special Units

### Autonomous Robots

Autonomous combat robots are an armored battalion suited to open, mechanized warfare.
They have a combat width of **2** and require **50 combat robots**, **10 support equipment**, and **50 manpower** per battalion.

Access depends on obtaining the required robot technology, with further technological development improving their combat performance.
They still face penalties in forests, jungles, and marshes, so terrain and support remain important when choosing where to deploy them.

<!-- IMAGE PLACEHOLDER: In-game autonomous robot battalion showing equipment needs and terrain effects. -->

---

## Campaign Tools

### State Map Modes

Five map views make regional crises easier to follow:

| Map mode | What to look for |
| --- | --- |
| **Contamination** | Chemical contamination, disease, and nuclear fallout. |
| **Civilian Deaths** | Areas suffering population losses. |
| **Air Winter** | Local winter severity and survival conditions. |
| **Famine** | Food-security stages and relief needs. |
| **Migration** | Flight, trapped populations, reception pressure, resettlement, and return. |

The famine and migration views are available from campaign start.
Hover over a state for more detail, subject to what your country can see.

<!-- IMAGE PLACEHOLDER: In-game map-mode buttons and a state tooltip explaining the selected crisis. -->

### Custom Achievements

Custom achievements reward milestones in research, survival, world conditions, and the choices made during a campaign.
They are available across player countries, with individual requirements determining eligibility.

Some achievements require an ordinary campaign progression and cannot be earned through forced events or manual scenarios.
Check their conditions before beginning an achievement attempt.

### Help and Campaign Information

Use **Help** for guidance on controls, **Event Logs** for campaign history, and the **Chaos Meter** for worldwide conditions.
Open Help from the Settings title bar or press **Ctrl+Shift+H**.
The optional countdown window keeps event timing visible while you play.
