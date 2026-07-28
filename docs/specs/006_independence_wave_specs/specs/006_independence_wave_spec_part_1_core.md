# Independence Wave, Part 1: Core event design

All names in this file are working labels, not final localisation.

## Event promise

Independence Wave is a repeatable global rupture that creates several sovereign countries at once. A wave should feel like a sudden failure of imperial, colonial, federal, or centralized authority. The map changes immediately, then the released states spend the next several years proving that they can survive.

The event is built around three linked experiences:

1. A synchronized release wave that creates a readable cluster of new states without deleting any host country.
2. A survival game for every released country, built around legitimacy, recognition, government capacity, security, foreign support, and relations with the former host.
3. A widening international system in which new states cooperate, compete for patrons, settle borders, create regional formables, and sometimes establish a global league of released nations.

The event must remain valuable when it fires for the first time, the fifth time, and the tenth time. Repetition should expand the population of Independence Wave countries and deepen their shared political ecosystem. It should not repeat the same popup and leave empty tags behind.

## The visible moment

A wave releases all selected countries instantly in one synchronized incident. The player should see several governments appear together, followed by a concise world summary and country-specific opening content for each new state.

The release itself is immediate. Recognition, legitimacy, force building, border settlement, league membership, and regional ambitions are long-running play.

The emotional center is the appearance of governments, crowds, militia columns, railway guards, local councils, royal restorers, clerics, union halls, veterans, or provisional cabinets. The event should not be framed mainly as a changed map or an administrative report.

## Exact wave ladder

The baseline number of countries released by an automatic wave is fixed by the current chaos tier.

| Chaos band | Countries in the wave | Candidate character | Opening character |
| --- | ---: | --- | --- |
| Calm World | 6 | Established releasables and countries already represented by registered content | Small territorial package, limited forces, strong diplomatic vulnerability |
| Gathering Storm | 8 | Established releasables plus a limited set of clear historical restorations | Wider host disruption, better local organization, first rare overlays |
| Rising Chaos | 10 | Registered tags, historical states, regional identities, and researched local polities | Stronger militias, more contested borders, active patron competition |
| Chaos Tier | 14 | Broad regional pool with stranger governments and ambitious historical claims | Armed releases, radical routes, league politics, frequent host retaliation |
| Totalen Chaos | 20 | Full eligible pool, including niche historical and local polities | Maximum variety, stronger forces, severe instability, aggressive ambitions, hidden formables |
| World Collapse | 20 | Full eligible pool, including rare and niche historical and local polities | Maximum variety, stronger forces, severe instability, aggressive ambitions, hidden formables, and danger-milestone pressure |

World Collapse retains the 20-country count of Totalen Chaos while also changing package quality, route access, force strength, border ambition, instability, and the chance of a dangerous coordinated bloc.

The fixed counts are design anchors. A wave may release fewer countries only when the map cannot produce the required number without violating host survival, duplicating a state, selecting an already living tag, or creating an invalid country. Such a shortfall is a blocked wave slot, not permission to annex a host or create overlapping ownership.

## Candidate pool layers

Every candidate belongs to one of five pool layers.

### Layer A: Registered and normal releasables

This layer contains countries that already have a valid vanilla or Chaos Redux tag, country definition, flag coverage, and a reasonable territorial identity. These candidates dominate low-chaos waves.

When a registered country already exists, it is not selected again. When it exists as a subject, government in exile, civil-war participant, or event-created actor, it is also treated as unavailable unless a specific package defines a safe transformation instead of release.

### Layer B: Registered but underdeveloped identities

This layer contains valid tags that may lack event-specific content. They can appear from Gathering Storm onward if the Independence Wave overlay can supply the required survival play without replacing an existing meaningful tree.

### Layer C: Historical restorations

This layer contains researched historical states, kingdoms, republics, confederacies, sultanates, unions, or regional governments whose identity can be translated into the 1930s and 1940s setting.

Examples include Assyria, Volga Bulgaria, Asante, Benin, Oyo, Sokoto, Aceh, Mon, Mapuche, and other entries in the candidate registry. Their routes should draw from real institutions and symbols without pretending that a medieval or early modern polity would return unchanged.

### Layer D: Local and indigenous polities

This layer contains regional peoples, local political identities, indigenous nations, island societies, historic councils, and subregional states. These packages require careful research, distinct naming, and protection against flattening several peoples into one invented identity.

They are not automatically radical, mystical, primitive, anti-modern, or militaristic. Their political routes should arise from local institutions, land claims, autonomy movements, religious traditions, labor organization, veteran networks, elite compromises, and foreign pressure.

### Layer E: High-chaos political inventions

This layer contains plausible alternate-history unions, emergency republics,
cross-border leagues, strange restorations, and highly ambitious local regimes.
These countries still need regional grounding. Layer E does not authorize a
fictional or generated leader for a real community, regional movement,
restoration, or otherwise plausibly historical polity; those packages require
sourced real male people or archival material for the actual institution. A
generated personal or institutional portrait is reserved for a later country
that the accepted source design explicitly classifies as both truly fictional
and high-chaos. None of the current 206 registry rows has that classification.
Fictional route structures and ImageGen-authored flat flag variants remain
permitted when clearly documented as alternate history rather than authentic
historical designs.

Layer E should never replace the researched country pool. It is a late-game supplement that makes high-chaos waves surprising.

## Release package levels

Every candidate has several territorial package levels. This prevents the event from requiring a separate hardcoded release effect for every wave intensity.

### Anchor package

The anchor package is the smallest valid release. It contains one unique state or a compact set that can support a capital and prevents overlap with another selected candidate.

The anchor is mandatory. A candidate without an available anchor is not eligible.

### Compact package

The compact package adds the most defensible and culturally central neighboring territory that can be released without taking the protected host state or overlapping another selected country.

### Extended package

The extended package adds disputed historical districts, secondary cities, ports, rail junctions, or hinterlands. It is normal in high-chaos waves and in high-intensity scenarios.

### Ambition package

The ambition package is not granted automatically. It defines claims, negotiated transfer targets, protectorate goals, league arbitration demands, and formable requirements that become playable after release.

The event must not hand every candidate its maximal historical map. Larger identities are earned through diplomacy, missions, wars, or formable decisions.

## Host survival covenant

Independence Wave never deletes an existing host country through the release effect.

Every affected host receives a protected-state reservation before candidate selection.

Protection follows this order:

1. The current capital state is protected when it is owned and controlled by the host.
2. If the capital cannot be protected because of an unusual split, the safest owned core state with a valid capital location is protected.
3. If no core is available, one owned state is protected and becomes the emergency capital.
4. Candidate packages that require the protected state are trimmed or removed from the pool.
5. The planner verifies that the host retains at least one owned state after all selected releases are applied together.

The capital preference is strong but not absolute. A host may keep another state when the capital is already controlled by a third party, belongs to a different active country, or would produce an invalid enclave. The design priority is a living host with a functional capital, not mechanical loyalty to a broken map state.

A host that loses most of its territory receives crisis content. It can negotiate recognition, attempt reconquest, seek outside guarantees, reform into a smaller successor state, or accept a new regional order.

## Synchronized wave planner

The planner treats the entire wave as one allocation problem.

### Planning pass

1. Build the global candidate pool for the current chaos band.
2. Remove living tags and invalid transformations.
3. Identify every possible host and reserve its protected state.
4. Remove candidates whose anchors conflict with protected host states.
5. Score candidates for regional spread, novelty, package readiness, host diversity, prior wave history, and cluster context.
6. Select the required number of candidates with unique anchor states.
7. Expand selected candidates to compact or extended packages according to chaos, map room, and package rules.
8. Recheck every host after all provisional transfers.
9. Resolve overlap by priority, trimming optional states before removing a candidate.
10. Replace any removed candidate with the next valid entry.
11. Lock the plan, then execute all releases in one synchronized incident.

### Execution pass

1. Transfer or release the locked territory.
2. Assign the correct capital.
3. Record Independence Wave origin.
4. Apply the correct country package tier and regional overlay.
5. Create the opening government and leader or institutional body.
6. Create dynamic starting forces and stockpiles.
7. Apply starting ideas and mechanic values.
8. Assign shared focus content or the additive Independence Wave overlay.
9. create host relation state and border claims.
10. Register the country in the current wave and wider Independence Wave network.
11. Fire the wave summary and country opening events.

The release must be deterministic after the plan is locked. A country should not disappear from the plan because an earlier release changed ownership during the same execution sequence.

## Origin separation contract

Independence Wave and Soviet Collapse are separate systems.

The same country tag may be eligible for both events in different campaigns. Its content is chosen by the origin that actually created it in the current campaign.

### Independence Wave origin

A country receives Independence Wave origin only when Event 6 directly released or transformed it. That origin grants:

- Independence Wave starting ideas
- Independence Wave mechanic values
- Independence Wave decision categories
- Independence Wave focus tree or additive overlay
- Independence Wave league eligibility
- Independence Wave regional ambitions and formable access
- Independence Wave AI strategy
- Independence Wave event and achievement tracking

### Soviet Collapse origin

A country created by Event 5 keeps Soviet Collapse content. Event 6 does not add its mechanics merely because the tag appears in the Event 6 candidate registry.

### Existing-country rule

A country that already exists before the wave is never silently converted into an Independence Wave country. It may react to the wave, sponsor new states, join a league through a special diplomatic route, or receive crisis decisions. It does not receive origin-locked release content.

### Shared-tag collision rule

If Event 5 and Event 6 are fired together through the Liberations cluster and both want the same tag:

1. The cluster prepares both candidate plans before either release executes.
2. The tag and anchor state are reserved by one origin according to cluster priority and package validity.
3. The other event rerolls or selects a different candidate.
4. The selected country receives one origin only.
5. No focus tree, idea, decision, or route from the losing origin is attached.

### Annexation and return

The active origin package ends when the country ceases to exist. Historical origin remains in the event log for achievements and campaign history.

A later release receives the origin of the event or action that recreated the country. The system should not assume that a tag has permanent Event 6 identity across every resurrection.

## New tag rule

Every new tag created specifically for Event 6 ends in `X`.

This rule applies to:

- new country tags
- new formable tags
- new route split tags
- new cosmetic tags
- new puppet or client variants that require a registered tag
- new high-chaos transformations

Existing vanilla tags and already registered Chaos Redux tags may be reused without renaming. Reuse must preserve the registered country's vanilla files and behavior whenever the Event 6 package flag is absent.

New Chaos Redux country tags may use ordinary country-history files named
`TAG - Country Name.txt`. Their native country setup may live in those history
files when that setup belongs to the new tag in every origin. The prohibition
on replacement history applies only to existing vanilla or previously
registered carriers. Those carriers keep their registered history unchanged
and receive origin-gated Event content through additive setup effects.

The 102 accepted custom `X` tags are locked by the 2026-07-15 installed-registry audit. A later migration still requires a new complete scan of country tags, aliases, cosmetic identities, and other event plans before assignment. Retired values are not recycled.

The event should prefer cosmetic identity changes and shared package data over consuming a new tag for every route. A new tag is justified when the country must exist independently, preserve a distinct history package, coexist with the source tag, or carry a formable identity that cannot be expressed safely through a cosmetic change.

## Resolved tag, map, and research baseline

The candidate registry and `research/006_package_research_resolution.csv` bind every package to one of three representations: 102 custom Event 6 countries, 91 registered vanilla-tag reuses, or 13 non-selectable vanilla route overlays. The same files assign one of eight current dispositions: 9 automatic, 44 automatic if not living, 73 automatic if a unique state exists, 27 high-chaos, 7 route-only, 30 specific-community, 3 scenario, and 13 vanilla-route-overlay-only packages. The planner never treats an overlay row or an unready broad label as a selectable country candidate.

Registered tags are reused where their identity fits. New Event 6 country, formable, cosmetic, and route tags use the reserved `X` ending. The dated collision audit found no duplicate accepted custom tag, no collision in the installed vanilla, Workshop, local-mod, or Chaos Redux tag and alias universe under the stated Random Events exclusion, and no use of the engine-reserved `GFX` graphics namespace. `ZIN` remains the existing Event 068 carrier; the separate retired `AUX` reservation is the Windows-device issue. Stable registered-tag migrations are `IW-038 RUT`, `IW-042 GAL`, `IW-043 CHU`, `IW-096 BIA`, `IW-133 BAN`, `IW-150 ATJ`, `IW-153 POK`, `IW-155 BLI`, `IW-157 WPG`, `IW-167 CHM`, `IW-171 OKN`, `IW-172 ANU`, and `IW-178 PNG`. Stable custom remaps are `IW-021 ICX`, `IW-087 HYX`, `IW-124 HZX`, `IW-161 IAX`, and `IW-162 IBX`.

`IW-153` Dayak Federation reuses vanilla `POK`, the Dayak Republic of West Borneo, instead of retired `FWX`. Its compatibility adapter must preserve registered `POK` history, characters, cores, `INS` releasable membership, and `indonesia_transfer_POK` behavior. The package remains `specific_community_variant_only` and unbound, and the adapter must preserve that restriction.

`CHU` is intentionally shared by `IW-043` Volga Bulgaria and `IW-046` Chuvashia. `BIA` is intentionally shared by `IW-096` Edo Kingdom of Benin and `IW-107` Biafra. Package flags distinguish each identity, and tag plus reservation-group allocation must make each pair mutually exclusive within one wave. Tag identity alone never selects content.

The thirteen overlay-only rows are `IW-005 BEL_flanders`, `IW-022 CRO` with the dynamic `dalmatia` identity, `IW-025 HUN` with the dynamic `vojvodina` identity, `IW-035 LIT` with `LIVONIA`, `IW-059 neo_mesopotamia`, `IW-085 LBA` under the Cyrenaica autonomy identity, `IW-101 COG_kingdom_of_kongo`, `IW-102 COG_kingdom_of_kuba`, `IW-105 COG_kingdom_of_loango`, `IW-156` on democratic `TNE`, `IW-196 antilles`, `IW-197 CHL_mapuche_state`, and `IW-204 kingdom_of_araucania_and_patagonia`. These rows are additive route packages. They receive no custom country registration and never enter the selectable release pool.

The state anchor matrix uses a public 763-state baseline and named reservation groups. Numeric IDs are implementation aids. The installed game and mod state files remain the engine authority. When a named package has no unique current-map anchor, it is not selected automatically. It remains a later secession, formable, route, or scenario candidate.

The source and identity decision remains binding when an ID changes. State rebinding cannot broaden an opening map, erase a host remnant, merge distinct communities, or convert a formable into an automatic country.

### Current installed-map binding layer, 2026-07-14

The dated implementation layer in `../../../plans/006_independence_wave_plans/package_bindings/` evaluates all 206 accepted packages against the installed 1,081-state map. Its original all-row ledger records 149 bound and 57 unbound packages, references 205 existing state IDs, and preserves all 111 accepted reservation groups. That `149/57` result is superseded for country selection because it includes 13 overlay rows. Eleven overlays were in the bound list and two overlays were in the unbound list. Excluding them leaves a selectable country pool of 138 bound and 55 unbound packages. The package CSV, reservation-group CSV, collision CSV, and audit remain the numeric state-binding evidence for that installed snapshot. The accepted representation, identity, disposition, and map rules in this specification remain the design authority.

The 14 collision rows contain 12 same-group overlaps already governed by maximum-one and trimming rules. Two cross-group findings remain unresolved implementation gates. Lazistan and Pontus both claim state 354 Trabzon while retaining distinct accepted reservation groups. Their automatic selection needs an explicit state-level mutual exclusion. The route-only Himalayan confederation overlaps the automatic Kashmir package on state 441, so that route must consume or exclude the active Kashmir reservation. Neither finding authorizes a silent group merge or a broader map grant.

The current registry scan confirms that all 91 reuse rows resolve to registered tags and all 102 custom Event 6 `X` tags remain collision-free in the installed and mod registries. The scan locks identifiers and representations. It does not implement the thirteen compatibility adapters or thirteen additive overlay hooks. That result must be repeated if the relevant registries change.

## Repeatable memory

The event remembers previous waves.

A repeat firing should prefer:

- countries not previously released by Event 6
- regions not used in the immediately previous wave
- candidate families that improve global variety
- hosts that can survive another release
- packages whose regional overlay has not dominated the campaign

A repeat firing should avoid:

- releasing several near-identical microstates from one host when other regions are available
- selecting a country that was released, annexed, and immediately re-released without a rare return condition
- repeatedly stripping the same host to its protected capital
- duplicating the same government route distribution across every wave
- spawning only registered European releasables after high-chaos pools are open

The wave memory tracks candidate package, region, host, chaos band, wave number, survival outcome, league outcome, and final origin state.

## Regional spread

Automatic waves are globally aware.

At low chaos, two countries may come from the same broad region when that produces a coherent historical rupture. At high chaos, the planner should normally include at least three broad regions and should reward cross-regional variety.

A wave can be intentionally concentrated when a regional collapse is the strongest available story. Such a wave receives a regional crisis variant and should create connected host reactions, border disputes, and league politics rather than several unrelated releases.

## Event classification and cluster role

Independence Wave remains a Minor Repeatable event.

It is a low-intensity member of the Liberations cluster in participation terms. Its displayed danger can still be Medium because a wave changes several countries at once.

When the cluster fires both Event 5 and Event 6:

- the cluster counts as one global pacing incident
- each member applies its own origin rules
- each member records its own event history
- cluster history records fired and skipped members and their reasons
- candidate, state, and host reservations are prepared jointly
- the combined release cannot delete a shared host or create duplicate states

## Player entry points

The event supports several player perspectives.

### Player controls a released country

The player immediately receives the country opening event, mechanic summary, first survival mission, focus access, and an explanation of the former host relationship.

### Player controls a host

The player receives a host crisis event and decisions to accept separation, negotiate terms, sponsor a client government, demand demobilization, prepare reconquest, or seek outside arbitration.

### Player controls a nearby country

The player may recognize, guarantee, arm, invest in, infiltrate, mediate, or pressure the new state depending on ideology, distance, strategic interest, and route.

### Player controls a major power

The player sees a patron competition layer. Support can produce influence and access, but excessive dominance can push the new state toward dependency, puppet status, or anti-patron backlash.

### Player controls an earlier Independence Wave country

The player can recognize new members, share institutions, send cadres, propose league membership, arbitrate borders, or exploit the new wave as a rival.

## Core success and failure

A released country succeeds when it becomes a stable and recognized state that can defend its territory, limit patron control, resolve or survive conflict with the former host, and pursue a regional future.

A released country can fail through:

- annexation
- voluntary reunion
- client capture by one patron
- military takeover that destroys civilian legitimacy
- league expulsion
- uncontrolled border war
- government collapse
- splintering into a later high-chaos package
- absorption into a regional formable led by another released country

Failure should create events and consequences. It should not merely remove the tag without memory.

## Design limits

The event does not create a bespoke full tree for every candidate. It creates a deep shared framework, regional overlays, package archetypes, and selected country ambitions that combine into distinct play.

The event does not grant maximal territorial claims at release. It gives anchors and compact territory, then turns larger borders into play.

The event does not treat every historical identity as equally certain. Candidate research status is recorded, uncertain reconstructions are marked, and sensitive identities require additional source review before implementation.

The event does not convert existing countries into Event 6 actors merely because they share a tag with a candidate.

The event does not use the same route, leader type, flag logic, or military package for every region.
