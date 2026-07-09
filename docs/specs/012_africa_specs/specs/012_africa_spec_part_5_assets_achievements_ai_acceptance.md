# 012 Africa spec part 5, assets, achievements, AI, and acceptance criteria

## Asset coverage summary

The Africa event needs assets across country identity, focuses, ideas, decisions, achievements, report events, news events, super-events, UI, flags, portraits, and high-chaos transformations. Asset work should be split by subagent mode.

- sourced visual assets for real historical flags, real symbols, real leader portraits, and archival event images
- generated event art for fictional report images, news images, super-event images, fictional leaders, nonhuman leaders, high-chaos scenes, faction emblems, and UI panels
- icon production for focus icons, idea icons, decision icons, category icons, achievement icons, and animated small sprites

Every animated asset needs real source frames, a sheet, static fallback, manifest, contact sheet, and GFX handoff. Do not use GIFs as game assets.

## Main asset families

| Family | Needed assets | Source mode |
| --- | --- | --- |
| Africa identity | cosmetic flags, ideology flags, leader portrait frames, faction emblem | mixed, sourced motifs plus generated variants |
| Charter League | decision category icon, UI header, cohesion meter, member card states | generated icons and UI |
| Regional restorations | flags, leaders or councils, small country portraits, old-polity emblems | sourced for attested flags, generated for fictional variants |
| Focus tree | icon families for politics, League, liberation, integration, industry, military, diaspora, old polities, high chaos | generated focus icons |
| Decisions | 32x32 icons for aid, intervention, integration, restoration, panic, diaspora, resource projects | generated decision icons |
| Ideas | 64x64 spirits for legitimacy, League cohesion, broken administration, returnee settlements, old-polity autonomy, colonial panic | generated idea icons |
| Super-events | Africa is one, Scramble for Africa, world-end path images | generated unless a specific archival direction is chosen |
| High chaos | animal leader portraits, oracle portraits, living statues, nature covenant UI, disaster warning frames | generated, with animation where useful |
| Achievements | completed, grey, and not-eligible icons | generated achievement icons with standard variants |

## Animated presentation candidates

Animation should be used where state changes matter.

- Charter League seal glow when enough cohesion exists for a vote
- colonial panic warning border when outside powers prepare ultimatums
- integration meter shimmer when a region becomes eligible
- high-chaos forest covenant emblem with slow state-driven motion
- oracle council portrait or emblem after the nature route unlocks
- animal actor leader portraits only for major high-chaos reveals
- Scramble for Africa super-event image can remain static unless the super-event system supports animated presentation

Static presentation is acceptable for ordinary report images, ordinary country flags, and most normal focus icons.

## Achievement suite

Achievements should reward difficult route mastery, not basic event firing.

Priority achievements:

| Working key | Route | Unlock direction | Failure direction | Icon motif |
| --- | --- | --- | --- | --- |
| africa_one_without_chains | federal or legal route | unify Africa through League federation with low coercion and high cohesion | disallow mass puppet coercion | joined hands around a continent-shaped seal |
| no_second_scramble | post-unification | survive the Scramble reaction without losing any African core or member | fail if outside power controls African capital state | broken colonial chain over port cranes |
| black_star_harbour | diaspora route | complete returnee routes with ports, housing, and industry projects active | fail if returnee crisis collapses | ship, star, and harbor lights |
| crowns_of_the_old_courts | monarchist or old-polity route | restore a large set of old polities and federate them peacefully | fail if most are annexed by force | crowned stools, spears, and charter parchment |
| the_green_signs | high-chaos nature route | win a war using nature covenant pressure while keeping League cohesion above threshold | fail if League collapses | forest seal and storm edge |
| the_continent_refused | rival bloc challenge | defeat or reconcile a major African rival bloc after it leaves the League | fail if the bloc is conquered by outside power first | split shield being repaired |
| from_cape_to_cairo_and_back | logistics route | complete rail and port integration across north, south, east, and west corridors | fail if any major corridor is occupied by an outside power | rail line crossing a sun disk |
| one_world_one_flag | world-end | become The World after continent wars | hidden, terminal | globe made of joined continent banners |

The next pass should expand these into exact conditions, tracking flags, and icon prompts.

## AI strategy summary

### Africa unifier AI

- peaceful and federal AI should build legitimacy, defend African countries, and avoid fast coercion
- communist AI should prioritize anti-colonial wars, worker aid, and revolutionary League members
- fascist or military AI should use faster integration and war preparation but risk lower cohesion
- monarchist AI should restore old polities and use royal federation routes
- high-chaos AI should only enter supernatural branches when chaos, evolutions, and internal conditions support it

### African target AI

Targets evaluate strength, threat, ideology, war state, relation, local legitimacy, and League behavior. A weak target at war with a coloniser should accept protection. A strong target with good stability should bargain or resist. A target that received aid should be more open to federation. A target that was coerced should build resistance or seek a rival bloc.

### Colonial and outside AI

Outside powers evaluate holdings, ports, resources, faction commitments, and current wars. They should not suicide into Africa while losing a major war unless colonial panic is extreme. They can sponsor rival blocs, sanction, guarantee holdings, prepare expeditionary forces, or accept withdrawal if too weak.

## Documentation and catalog needs

The final implementation must update event docs, event log details, evolution details, cluster membership, super-event docs, asset manifests, and spreadsheet rows. The spreadsheet should mirror in-game event detail and evolution wording. Event Details should describe premise and situation, not script effects.

## Acceptance criteria for implementation

The event is not complete until these are true.

- Event 12 is registered as a fire-once Formables cluster member with severe member severity.
- Valid African-capital selection works and RSA-in-Allies civil war branch works.
- The Africa unifier receives a real tree, decisions, ideas, AI, assets, and country identity.
- The Charter League is a living system with cohesion, legitimacy, target states, refusal, exits, and rival blocs.
- African countries are not all treated as instant conquest targets.
- Integration is staged and can result in federation, subject status, puppeting, annexation, or conflict.
- Strong African countries can resist or create rival blocs.
- Colonial powers react through panic stages and Scramble for Africa crisis.
- Regional restored polities have country package coverage, starting forces where needed, flags, names, and integration paths.
- Evolutions are logged as true mutation tracks, not baseline stages.
- High-chaos actors are clearly nonhuman or supernatural where applicable and not written as human ethnic caricatures.
- Super-event packages are researched, sourced, wired, and documented before being marked complete.
- The World is One route is rare, terminal, and gated by other continent unifiers.
- Assets are processed, converted, documented, and handed off.
- Achievements have tracking, localisation direction, icons, disqualifiers, and docs.
- No fallback or placeholder content is hidden in completion notes.
