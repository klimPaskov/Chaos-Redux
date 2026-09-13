# Part 3: Focus tree architecture

## Tree scale

The implementation blueprint contains 120 authored focus roles. The registry has 108 base-tree roles plus 6 Evolution I roles and 6 Evolution II roles. Evolution III primarily unlocks the already-authored Kubrat and Black Sea late-game branch through visibility and availability gates, so it does not require a separate third set of appended nodes.

The final implementation may adjust exact node count only when MCP focus inspection and rendering prove that a merge or split improves route clarity without deleting accepted content. Any count change must be reported.

## Lane architecture

The normal-zoom tree should read as six large families with clear sublanes:

1. National Awakening and government
2. Army, air, and Black Sea forces
3. Industry, logistics, and reconstruction
4. San Stefano expansion and integration
5. Diplomacy, protectorates, and Balkan order
6. Imperial and Kubrat late game

The opening is compact. Early focuses are commonly 35 days. Emergency handoffs may use shorter durations when they only unlock an immediate action. Mature institutional and integration focuses can use normal 70-day pacing.

## National Awakening

This branch turns the initial surge into a coherent state. It organizes emergency command, mobilization, claims, propaganda, administration, and the first border actions. It also opens the political fork.

## Government of the Greater State

Four political settlements are supported without forcing a simple ideology quota.

### Royal imperial rule

The monarchy becomes the central source of legitimacy. The route favors direct imperial administration, elite command, ceremonial integration, and client monarchies where useful.

### Military-national government

The officer corps dominates the revival. The route maximizes short-term Momentum, faster military pressure, tighter occupation, and rapid mobilization. Its cost is weaker diplomatic acceptance and harder administration in distant territories.

### Centralized Greater Bulgarian state

A civilian-national central government seeks direct incorporation and bureaucratic standardization. It is the strongest route for core integration and domestic administration, but it needs more time and material to absorb distant regions.

### Federation and protectorates

The state accepts a layered Balkan order with protectorates, autonomous clients, and negotiated integration. It has the easiest diplomacy and lowest immediate resistance, but fewer territories become direct cores quickly.

## The Bulgarian Army Reborn

The army family covers mass mobilization, mountain warfare, shock infantry, artillery, armor, logistics, officer reform, veteran integration, captured equipment, reinforcement, and late major-power warfare.

The tree should create or improve concrete templates and production choices. It should not become a line of repeated attack and defense modifiers.

## Arsenal of the Balkans

The industry family permanently changes Bulgarian production and logistics. It places factories, railways, infrastructure, airbases, supply capacity, resources, and building slots in geographically sensible locations. Integrated regions unlock reconstruction and local industrial programs.

The branch has a short-term arsenal route and a long-term integration route. The player can pursue both partially, but the deepest capstones require a clear economic priority.

## The San Stefano Dream

This is the main baseline expansion family. It opens target groups in a readable order, supports diplomatic and military methods, and feeds the integration system after territory is obtained.

The route culminates in Greater Bulgaria. Formation is followed by consolidation content rather than ending immediately.

## Balkan Hegemony

This family decides how Bulgaria handles neighbors and foreign powers. It can build a Bulgarian-led faction, use bilateral protectorates, create client states, seek an outside partner, balance major powers, or insist on strategic independence.

The diplomacy branch changes the options and costs inside the expansion branch.

## Crown of Simeon

Evolution II unlocks the medieval imperial route. It deepens royal or military symbolism, opens broader Balkan ambitions, strengthens subject arrangements, and culminates in the Bulgarian Empire.

The Bulgarian Empire is a major regional order, not a cosmetic rename.

## Kubrat's Legacy

Evolution III reveals the trans-Black-Sea branch. The branch requires Black Sea access and serious logistics. It develops ports, naval or air cover, amphibious and transport capacity, steppe supply, eastern intelligence, and regional administration before the final formation.

The final Old Great Bulgaria formation is the strongest capstone and triggers the event's single dedicated super-event.

## Navigation and filters

Each major family needs Focus Navigation when spatially separate. Search filters must reflect branch ownership. Hidden Evolution II and Evolution III regions must not be revealed by navigation before their evolution gate is active.

## Layout rule

The implementation must use `hoi4.focus_inspect` and `hoi4.focus_render`, then repeat layout review until the six main families, political forks, formation path, and evolution-gated regions are identifiable at normal zoom without tracing long connectors.
