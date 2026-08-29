# Event 32 requirement traceability

## Purpose

This file maps every supplied Event 32 requirement to its source-of-truth specification section.

A mapping proves design coverage. It does not prove implementation.

## Catalog identity

| Supplied requirement | Specification coverage |
| --- | --- |
| Event ID 32 | Part 1, Catalog identity. Part 8, Namespace and IDs. Acceptance criteria, Catalog and registration |
| Event name Missiles | Part 1, Catalog identity. Event Details and workbook contracts |
| Minor Repeatable | Part 1, Catalog identity and Global firing model. Acceptance criteria, Catalog and registration |
| To Be Reworked | Source review and migration contract. The implementation keeps the event disabled by default until complete |
| No cluster | Part 1, Catalog identity. Acceptance criteria, Catalog and registration |

## Baseline

| Supplied requirement | Specification coverage |
| --- | --- |
| Global repeatable event affecting every valid existing country | Part 1, Global firing model and Valid recipient contract. Part 8, Event dispatch |
| Country with no missile technology unlocks the first step | Part 1, Technology progression. Part 2, Technology adapter |
| Country with an existing program receives the next step | Part 1, Technology progression and Repeated firing flow. Part 2, Technology adapter |
| Country completes one available missile technology step | Part 1, Technology progression. Part 8, Technology adapter |
| Full missile line gives a larger operational package | Part 1, Mature-program package. Part 2, Operational reserve model |
| Every country receives missiles and at least one usable launch state | Part 1, Program initialization. Part 2, Operational reserve model and Launch-state records |
| Initial sites favor owned, controlled core states with infrastructure and protection | Part 2, Eligible launch-state contract, Site selection ladder, and Site scoring factors |
| Avoid wastelands, occupied enemy territory, isolated empty regions, and bad frontline sites | Part 2, Eligible launch-state contract and Site scoring factors. Probability matrix, site scenarios |
| Repeat firings reinforce existing sites before adding sites | Part 1, Repeated firing flow. Part 2, Site reinforcement priority and Site count cap |
| Repeats add missiles, capacity, sites when needed, and later technology | Part 1, Repeated firing flow. Part 2, Technology adapter, Operational reserve, Site capacity, and Site count cap |
| Ordinary missiles damage strategic buildings and supply systems | Part 3, Target profiles, Conventional damage model, and strategic building resolution |
| Populated-state attacks can cause civilian deaths | Part 3, Civilian deaths and target restraint. Shared Deaths integration in System connections |
| Every country receives a capability report | Part 1, Human and AI reports. Part 7, country report writing and image direction |
| First firing may produce global proliferation news | Part 1, News behavior. Part 7, first global news writing and image direction |

## Evolution I: Saturation Arsenals

| Supplied requirement | Specification coverage |
| --- | --- |
| Suggested Chaos Tier unlock | Part 4, Evolution structure and Saturation global unlock conditions |
| Much larger reserves | Part 4, Saturation immediate effects and country adoption |
| Sustained barrages | Part 3, Saturation strike profile. Part 4, Saturation barrage mechanics |
| More launch states where suitable | Part 4, country adoption and site-cap effects. Part 2, site cap and scoring |
| Faster replenishment | Part 4, Replenishment. Part 5, replenish-reserve action |
| Shorter launch cooldowns | Part 4, immediate effects and country adoption |
| Longer operational reach | Part 4, Range. Part 3, Reach |
| More aggressive AI | Part 4, AI behavior. Part 6, Saturation offender profile |
| Strategic AI target priorities | Part 6, target-country and target-state scoring. Probability matrix, target scenarios |
| Repeated firings become much more dangerous | Part 4, Saturation adoption and cross-track behavior. Part 1, repeat flow |

## Evolution II: Unreliable Guidance

| Supplied requirement | Specification coverage |
| --- | --- |
| Production outpaces guidance, maintenance, and command | Part 4, Guidance pressure and global unlock conditions |
| Wrong state, neutral territory, self-strike, launch failure, and breakup | Part 4, Outcome families. Part 3, Guidance resolution and bounded drift pools |
| Accidents can kill civilians and damage sites | Part 4, outcome families. Part 3, Civilian deaths and Incident record |
| Neutral incidents and mistaken retaliation | Part 3, Diplomatic consequences and Automatic-retaliation bridge. Part 4, track interactions |
| Barrage size increases malfunction risk | Part 4, Barrage-level risk. Probability matrix, guidance scenarios |
| Investment can reduce risk | Part 4, Guidance investment. Part 5, guidance and maintenance actions |

## Evolution III: Special Warheads

| Supplied requirement | Specification coverage |
| --- | --- |
| Missile delivery for unconventional payloads | Part 3, Special payload integration. Part 4, Special Warheads |
| Chemical, biological, nuclear, thermonuclear, and conventional high explosive | Part 3, payload subsections. Part 4, payload-specific rules |
| Relevant technology, weapon, and stockpile remain required | Part 3, Special payload integration. Part 4, Payload integration record and policy |
| Evolution adds delivery, not free payload ownership | Part 4, Design role and Global unlock conditions. System connections, Event 23 boundary |
| Chemical and biological effects use contamination, outbreak, condemnation, and deaths | Part 3, chemical and biological payloads. System connections, shared CBRN systems |
| Nuclear effects use nuclear consequences, air contamination, condemnation, and deaths | Part 3, nuclear and thermonuclear payloads. System connections, Fallout and Air Cleanliness |

## Evolution IV: Rogue Launch Commands

| Supplied requirement | Specification coverage |
| --- | --- |
| Missile institutions can escape government control | Part 4, Design role and Command-pressure model |
| Officers, factions, regions, civil-war sides, and intelligence services can gain influence | Part 4, Incident families and Civil-war bridge |
| Unauthorized launches and mutinies | Part 4, Unauthorized launch preparation and Launch-site mutiny |
| Crew defection and local threats | Part 4, Crew defection and Regional authority seizure |
| Foreign bribery and captured arsenals | Part 4, Foreign bribery, Captured arsenal threat, and Occupation bridge |
| Launch sites matter during internal conflict and invasion | Part 2, Capture and Civil wars. Part 4, Civil-war and occupation bridges |
| Weak or collapsing governments face higher risk | Part 4, Command-pressure model and Incident frequency. Part 6, Brittle command profile |

## Evolution V: Automatic Retaliation

| Supplied requirement | Specification coverage |
| --- | --- |
| Automated and semi-automated retaliation systems | Part 4, Retaliation postures |
| Major strikes can trigger response before attribution is confirmed | Part 3, Automatic-retaliation trigger bridge. Part 4, Warning classification and Response window |
| False warnings, poor guidance, forged signals, and interference can start exchanges | Part 4, False signals, Third-party interference, and track interactions |
| Retaliation can hit the wrong country or involve neutrals | Part 3, bounded drift and diplomacy. Part 4, Retaliation package and Chain reaction |
| Several systems can activate in sequence | Part 4, Chain reaction and Chain caps. Part 8, Incident state machine |
| Governments can disable, delay, secure, or restore networks | Part 4, Emergency actions. Part 5, Automatic Retaliation decisions |
| Intelligence services can forge signals or redirect blame | Part 4, Third-party interference. Part 3, Evidence and attribution |

## Shared and project requirements

| Requirement | Specification coverage |
| --- | --- |
| Event Logs, Event Details, evolutions, and history | Part 1, Event Logs integration. Part 8, Event Logs |
| Dynamic AI and probability proof | Part 6 and the probability scenario matrix |
| No recurring global scan | Parts 1, 2, 4, and 8. Acceptance criteria and test matrix |
| Shared Deaths, contamination, and Condemnation | Part 3 and System connections |
| World-end ownership remains separate | Part 3, shared terminal consequence bridge. Part 4, Automatic Retaliation shared consequence connection. System connections |
| Decision clarity and cost limits | Part 5 and decision and mission prompt |
| Asset coverage | Part 7 and asset prompt |
| Achievement coverage | Part 7 and achievement prompt |
| Manual scenario coverage | Part 5, SCN-015. Decision and mission prompt |
| Migration from current implementation | Source review and Part 8, Migration from legacy Event 32 |
| Full completion proof | Acceptance criteria and test matrix |
