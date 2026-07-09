# Event 019 Infantry Spawn spec part 6, triggerable scenario, AI, balance, and acceptance

This file defines the scenario layer, AI matrix summary, achievements overview, and completion standards.

## Triggerable scenario

Working scenario label: Sudden Muster War. This is not final UI localisation.

The triggerable scenario launches the event as an immediate military crisis. It should not require chaos tier, prior evolution history, date, or normal event firing state. It should only block impossible launches such as terminal campaign state, no eligible countries, or missing required tag pool.

The scenario should create many units and make a portion revolt instantly. The scenario type controls the flavor of the crisis. The intensity controls scale.

| Scenario type | Unit direction | Immediate danger | Best use |
| --- | --- | --- | --- |
| Conventional mutiny | mostly human infantry, cavalry, artillery, armor, and motorized | rogue generals and regional barracks revolts | lower-chaos challenge |
| Arsenal lottery | stronger and stranger mechanized, tanks, armored cars, helicopters, and specialists | many under-equipped heavy units and depot wars | military chaos challenge |
| Possessed command | Evolution III rules active immediately | several generals demand or revolt | internal command crisis |
| Chaos host | Evolution IV rules active immediately | zombie, ghost, golem, or registry chaos splinters | high-chaos supernatural crisis |
| Mixed world drill | random mix of all valid types | many local wars and unpredictable units | maximum sandbox chaos |

Intensity bands:

| Intensity | Scale direction | Revolt direction |
| --- | --- | --- |
| Low | several countries or one region, limited spawns | one or two small revolts |
| Medium | many countries, stronger wave | several regional mutinies |
| High | global or near-global wave, serious units | many simultaneous revolts and wars |
| Maximum | global wave with high absurdity and leakage | widespread instant revolts, chaos splinter chance, severe supply strain |

The scenario should open a confirmation window and read selected type and intensity at launch time. It should use explicit scenario flags that are cleared after setup so normal automatic behavior remains governed by the event state.

## AI strategy matrix

| Actor | Baseline behavior | Evolution II behavior | Evolution III behavior | Evolution IV behavior |
| --- | --- | --- | --- | --- |
| Small country at peace | keep units, sort depots, disband fragments | request only if threatened | close risky musters and contain generals | quarantine chaos units |
| Small country at war | keep most units and use capital defense | request defensive units when losing | empower one general only if desperate | rare chaos use if near capitulation |
| Major at peace | organize, avoid spam, reduce strain | use depot sorting and standardization | prevent appetite before it grows | ban or quarantine chaos units |
| Major at war | exploit stronger waves, pay costs | request targeted front units | tolerate generals if fronts collapse | cautious chaos use in emergency |
| Unstable country | high risk of panic and mutiny | disband weak units if possible | likely to face demand chains | high splinter risk |
| Fury actor | weaponize every wave | aggressive requests | may accept dangerous command | can cause local chaos if high chaos |
| Nonhuman or special chaos country | default excluded unless profile allows | profile-specific | profile-specific | registry-specific |
| Breakaway country | not applicable | uses crisis tree | attacks parent and depots | profile-specific aggression |

AI must respect supply, equipment, stability, war state, faction membership, nearby enemies, and route validity. It should never click dangerous decisions only because they are available.

## Achievement overview

Achievements are part of the spec pack and are detailed in the achievement prompt. They should reward mastery and rare outcomes, not the event merely firing.

Priority achievement directions:

- survive repeated waves as a small country without creating a revolt
- win a war using many integrated spawned units while keeping command coherence high
- defeat a possessed general revolt without losing the capital or banning the event category
- contain a zombie, ghost, or golem splinter without triggering the parent event's crisis mechanics
- form and then defeat or pacify a Barracks State breakaway
- win the triggerable scenario at high or maximum intensity
- use base zombie training and shut it down before a ragged horde forms
- keep a major country from supply collapse after an Evolution II arsenal wave
- defeat a grey host while recovering every harmed state
- intentionally create a chaos splinter, then reconquer it and close the chaos ledger

Each achievement needs an icon direction, tracking notes, and disqualifiers.

## Balance standards

The event is allowed to create many units, but the balance comes from strain, quality, supply, command, and revolt risk.

Pass conditions:

- baseline helps minors without creating elite armies
- large countries receive more units in total but worse density and greater strain
- at-war countries can get stronger units but pay higher command and supply costs
- Evolution II heavy units are exciting, rare, and expensive to absorb
- Evolution III on-demand units can be lucky or terrible, with absurdity rising from abuse
- Evolution IV chaos units are powerful enough to tempt the player but risky enough to require management
- chaos splinters are weaker than parent event countries and use separate identities
- disbanding units does not create equipment farming
- AI uses dangerous options only under credible pressure
- repeat firings remember fatigue and do not feel reset-clean every time

## Exploit checks

Implementation should explicitly check for:

- disband equipment farming
- repeated on-demand free unit loops
- using peace-state low costs to build a massive army safely
- AI deleting its army because it overreacts to supply strain
- chaos unit training persisting after bans or containment
- zombie training unlocking advanced zombie variants
- ghost splinters using Death's full state-erasure logic
- golem splinters gaining parent mechanics that do not belong to this event
- breakaway tags appearing without flags, names, leaders, units, or AI
- old decision targets staying visible after annexation or tag switch
- category clutter after the crisis is resolved

## Localisation direction

Implementation should write final text from direction only.

Text surfaces:

| Surface | Direction |
| --- | --- |
| Event Details | soldiers appear across territory, official command struggles to identify and register them |
| Baseline popup | confused but usable mobilisation, grounded in barracks, rails, town squares, ports, and fields |
| Evolution I | the formations appear more orderly, as if a missing staff prepared them |
| Evolution II | stronger units and heavier equipment arrive with logistical shock |
| Evolution III | command crisis and generals with unnatural influence |
| Evolution IV | ordinary mustering touches units that do not belong in a normal army |
| Decisions | concise public action, visible costs, no hidden spoilers |
| Missions | named places, clear objectives, readable success and failure |
| Achievements | route and mastery directions only until final implementation text |
| Super-events | research-gated title, remark, quote, and audio, no unresearched final wording |

Avoid final pasteable text in planning files. Avoid generic dramatic filler. Avoid describing mechanical formulas in Event Details.

## Required implementation surfaces

The implementation pass should expect to touch:

- event file for Event 019
- event registration and random repeatable classification
- event log name, details, and evolution entries
- scripted effects and triggers for spawning, density, template selection, registry checks, and cleanup
- script constants for density, weights, thresholds, AI tuning, and costs
- decisions and categories for the management layer
- possible scripted GUI files for the Muster Ledger
- ideas or dynamic modifiers for temporary strain and special states
- AI strategy for countries and breakaways
- unit templates and possibly registry helpers for chaos units
- country package files for breakaway tag pool
- focus tree file for shared breakaway tree if country packages are implemented
- localisation and scripted localisation
- GFX and asset manifests for icons, portraits, flags, report images, and animated UI pieces
- triggerable scenario registry, launch effects, type controls, and documentation
- event documentation and spreadsheet catalog row

## Completion acceptance checklist

The event should not be marked implemented until:

- baseline and all four evolutions are implemented or explicitly queued with a reason
- repeatable memory values are visible where relevant
- decision category has cleanup and AI
- random unit generation covers the required normal and weird unit families
- possessed generals have portraits, names, traits, demand chains, and revolt logic
- chaos unit registry exists and is documented
- zombie, ghost, golem, and future chaos profile rules are implemented safely
- breakaway countries have tags, flags, names, leaders, units, AI, ideas, and reinforcement routes
- shared breakaway focus tree or equivalent country play layer exists for long-lived splinters
- triggerable scenario launches all type and intensity variants without normal event prerequisites
- event docs, event log, Event Details, evolution details, and catalog spreadsheet are aligned
- assets are not placeholders unless a blocker is openly reported
- final localisation is written from direction and does not paste planning labels
- improvement loop planner pass has been run in the implementation environment and its addendum or closure handoff is resolved
- event completion auditor is run before claiming final completion

## Specification stopping point

The design pack stops after the completed planning handoff. It does not implement gameplay files. The next clean step is implementation according to the coding prompt and goal prompt.
