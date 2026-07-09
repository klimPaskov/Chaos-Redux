# 012 Africa spec part 32, final implementation acceptance pack

This file is the final planning closeout. It states what the canonical package considers complete enough for implementation to begin, what still requires live repo or asset workflow access, and what must be audited before any implementation completion claim.

## Canonical package status

The planning package is complete as a design handoff. It is not gameplay implementation. It contains the event concept, focus route architecture, Charter League system, country packages, regional integration, diaspora route, Scramble reactions, high-chaos routes, achievements, asset handoffs, super-event research candidates, prompts, matrices, and implementation acceptance criteria.

## Final source of truth order

When files appear to overlap, use this order.

1. Final pass specs, parts 24 through 32, for closure rules and research-gate expansion.
2. Third-pass specs, parts 17 through 23, for focus nodes, target missions, country sheets, state-group handoff, and acceptance pack.
3. Second-pass specs, parts 9 through 16, for expanded route packs, mechanics, assets, and achievements.
4. First-pass specs, parts 1 through 8, for core event direction and baseline system.
5. Matrices for implementation tables and quick audit.
6. Prompts for task routing.
7. Research files for source leads and source confidence.

## Must implement before gameplay completion

| Surface | Completion requirement |
| --- | --- |
| event start | valid African-capital country selection, fire-once behavior, cosmetic identity, initial package |
| RSA branch | Allied RSA triggers civil war, continental side and loyalist side packages, Allied peace if continental side wins |
| focus tree | large non-linear tree with all route families, branch interactions, AI weights, icons, idea lifecycle, and route locks |
| Charter League | target states, confidence, influence, autonomy demand, rival appeal, refusal, rival blocs, cleanup |
| regional integration | staged region projects, no instant continent cores, federal member and puppet routes, coercive risks |
| restored polities | priority packages, spawn rules, starting forces, reinforcement paths, direct names, assets, AI |
| diaspora | lane security, returnee capacity, settlement missions, industry cadres, failures, achievement tracking |
| Scramble reaction | outside-power trees, sanctions, ultimatums, war pressure, diplomatic crisis, super-event threshold |
| high chaos | nonhuman and supernatural gates, generated assets, disaster pressure, fictional disease safety, blowback, AI restrictions |
| achievements | full tracking, disqualifiers, icons, localisation, docs |
| assets | sourced or generated according to source mode, DDS outputs, manifest, GFX handoff |
| super-events | quote, title, button, image, audio, docs, music table, settings-aware playback |
| docs and spreadsheet | event docs, catalog rows, event details, evolutions, cluster details, implementation notes |
| validation | route coverage, target selector safety, state id audit, asset existence, localisation, AI, cleanup |

## Remaining live-repo gates

These are not design omissions. They require files or workflows not present in this sandbox.

| Gate | Why it remains live-repo or workflow dependent | Required resolution |
| --- | --- | --- |
| exact HOI4 state ids | vanilla and modded state files unavailable | build state resolver worksheet from live repo and vanilla files |
| final tags and cosmetic tags | tag conflicts require repo inspection | choose unused tags and cosmetic tags in country implementation |
| exact historical flag files | requires source image selection and conversion | asset source researcher sources and documents flags |
| real leader portraits | real portraits must not be generated | asset source researcher sources and documents portraits |
| final super-event localisation | planning package remains direction-first | super-event workflow selects and verifies final text |
| final super-event audio files | audio must be downloaded, converted, and wired | audio researcher prepares final track, main agent wires |
| exact focus coordinates | final layout depends on live focus-tree implementation | implementation agent lays out tree and audits crossings |
| exact script constants | values require balance in repo | implementation centralizes tuning after choosing mechanics |
| spreadsheet workbook | OneDrive workbook unavailable | spreadsheet worker updates after implementation facts exist |
| additional obscene leader-name flavor | reliable source review unavailable | use only required strings until vetted source review |

## No-go simplifications

Implementation must not do any of these.

- Give free full cores across Africa at event start.
- Instantly annex all native African countries.
- Make every League member a passive puppet.
- Treat restored countries as temporary tags with no package.
- Use one generic focus tree route with renamed branches.
- Give mostly tiny modifiers instead of real mechanics.
- Use political power purchases as the main decision system.
- Leave AI route behavior generic.
- Generate real historical leaders or historical flags.
- Use nonhuman actors as human caricatures.
- Use real disease names or actionable bioweapon details.
- Use unresearched super-event quotes, audio, or cultural references.
- Use default or placeholder super-event audio.
- Leave state id lists guessed from memory.
- Hide simplifications in the completion report.

## Implementation order

| Step | Work |
| --- | --- |
| 1 | Resolve exact state ids and tag availability in the live repo |
| 2 | Create core event start, valid target logic, RSA branch, and cosmetic identity |
| 3 | Implement shared variables, script constants, target states, and cleanup helpers |
| 4 | Build Charter League target mechanics and decision categories |
| 5 | Implement regional integration projects and staged coring |
| 6 | Create Africa unifier focus tree with opening and Federal Charter route |
| 7 | Add Revolutionary, Crown, Command, Sacred, Black Star, and high-chaos branches |
| 8 | Implement restored polity packages in priority tiers |
| 9 | Add diaspora lanes and settlement missions |
| 10 | Add Scramble reaction and outside-power trees |
| 11 | Add high-chaos nonhuman and fictional disease route only after grounded routes work |
| 12 | Produce and wire assets by source mode |
| 13 | Research and wire super-events with final audio and quote documentation |
| 14 | Implement achievements and icons |
| 15 | Update docs, event log, evolutions, cluster, and spreadsheet |
| 16 | Run focus, decision, country, localisation, asset, and completion audits |

## Audit requirements

Before claiming implementation completion, run or equivalent-review these surfaces.

| Audit | Purpose |
| --- | --- |
| focus tree audit | route coverage, prerequisites, mutual exclusions, icons, AI, reward depth |
| decision and mission audit | costs, missions, clutter, AI, cleanup, exploit risk |
| country package audit | tags, states, forces, leaders, flags, focus loading, AI |
| localisation audit | keys, dynamic values, tooltips, encoding, text consistency |
| scripted system review | repeated logic, variables, constants, event targets, cleanup |
| asset manifest review | source mode, DDS dimensions, sprite handoff, historical sourcing |
| super-event review | quote, audio, image, trigger, docs, music table |
| completion audit | spec-versus-implementation, simplifications, blockers |

## Final package acceptance

This planning package is complete only because it provides design, not implementation. It gives enough detail for a coding agent to implement without inventing route families, country packages, integration logic, high-chaos boundaries, or achievement systems. It also clearly names the gates that cannot be closed in this sandbox.

No gameplay completion claim should be made from this package alone.
