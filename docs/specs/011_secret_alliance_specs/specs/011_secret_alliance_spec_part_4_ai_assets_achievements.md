# Event 011: Secret Alliance, Part 4

Player-facing wording note: every title, option, decision name, focus-style label, achievement title, GUI label, event-detail line, report text, and news text in this package is direction only. Working labels are internal handles for implementation and asset routing. The implementation pass must write final localisation from the directions here, without copying working labels into the game unless a label is explicitly marked as an identifier.

## AI strategy overview

AI depth is required because the pact is mostly AI-driven when the target is a human country. Member AI must not behave like ordinary random joiners. Each role needs distinct willingness, risk tolerance, and exit logic.

| AI actor | Ordinary preference | High chaos preference | Avoidance rules |
| --- | --- | --- | --- |
| Cautious minor | Join only if factionless, frightened, and not too exposed | More likely to join as associate or covert member | Avoid if target is overwhelming and no patron exists |
| Aggrieved neighbor | Join when border claims, bad relations, or recent conflict exist | More likely to provoke border incidents | Avoid if border supply is terrible or target has strong local army |
| Ideological opponent | Join if target ideology is hostile or spreading | More likely to fund propaganda and support reveal | Avoid if already committed to another ideological faction war |
| Opportunist minor | Join if target is isolated and pact has patron | More likely to defect if exposed | Avoid if defection risk is high and patron is weak |
| Major patron | Fund and direct pact if target is a rival or rising threat | Can become founder or public member | Avoid if it is already losing a major war or has strong shared faction ties with target |
| Second major | Joins only if pact strong and target isolated | Joins more often if chaos high and target prepared poorly | Avoid if player exposed patron networks or split members |
| Target AI | Investigate when suspicion rises, prepare if exposed members border it | Can confront earlier if strong | Avoid suicidal preemptive war |
| Neutral AI | Can be courted by target or pact | More likely to choose sides | Avoid joining if already threatened by another event |

AI should evaluate campaign state, not flat weights. Use strength ratio, stability, war support, faction membership, target relationship, proximity, ideology, active wars, exposed evidence, pact cohesion, and chaos tier.

## Pact recruitment AI matrix

| Candidate type | Join as core member when | Stay associate when | Refuse when |
| --- | --- | --- | --- |
| Border minor | Target border army is weak, candidate has grievance, patron exists | Target is strong but candidate wants leverage | Candidate is in target faction or target is overwhelmingly stronger |
| Distant minor | Shared ideology, trade grievance, patron money | Weak diplomatic motive but high recruitment pull | No route to act and low strategic value |
| Naval minor | Target trade routes or ports matter | It can offer intelligence but not war commitment | It lacks navy, ports, or diplomatic motive |
| Resource country | Target depends on its resources or market access | It wants leverage without war | Target has strong relations or guarantees |
| New minor from other event | Only if normal country and stable enough | If short-lived or recently released | If special nonstandard classifier should exclude it |
| Major | Evolution II or III, motive, strategic reach, not at war with target | Funding without public risk | Already in target faction or in incompatible crisis |

## Player and AI target responses

The player receives decisions. If the target is AI-controlled, it needs an equivalent route so the pact can function in observer and multiplayer conditions.

| Situation | Human target behavior | AI target behavior |
| --- | --- | --- |
| Suspicion low | Reads subtle incidents | Mostly ignores unless high stability and available agency |
| Suspicion high | May take quiet investigation options | Starts low-cost evidence and security actions |
| Evolution II | Opens decision category and chooses priorities | Chooses between investigation, security, and diplomacy based on resources |
| Neighbor exposed | Can run border missions or border war | Runs border watch if supply good, avoids border war unless stronger |
| Major patron exposed | Can court allies or publish dossier | Seeks ally observers if factioned, otherwise defensive preparation |
| War countdown active | Can split members, demand dissolution, or mobilize | Mobilizes if threat high, talks if evidence high and weak |
| Pact revealed | Uses wartime preparation and allied calls | Focuses war survival and defensive decisions |

## Faction and war rules

The revealed pact is a public faction or coalition object only after reveal. The faction should not exist from event start.

Faction leader selection:

| Condition | Leader direction |
| --- | --- |
| Major founder exists | Major founder leads unless invalid or defected |
| Major patron joined later | Patron can take leadership if it has more industry and commitment than founder |
| Only minors exist | Highest score by industry, army, stability, and commitment leads |
| Founder exposed and humiliated | Another member can replace it at reveal |
| Leader invalid | Cleanup chooses strongest valid core member |

War behavior:

| Reveal path | War behavior |
| --- | --- |
| Member already at war with target | All valid core members join war immediately |
| Target preemptive strike | Pact reveal response triggers, but member commitment and prior splits can reduce joiners |
| Pact ultimatum refused | High-readiness members join, low-commitment members may hesitate if target has evidence |
| Evidence reveal without military action | War countdown or diplomatic crisis, unless pact readiness is extreme |
| Pact public declaration | War countdown, direct war, or negotiated crisis based on readiness and target response |

After reveal, covert sabotage decisions should either convert to wartime subversion tools or close. The player should not keep investigating a pact that is already public unless there are hidden associates or patron networks to expose.

## Connections with existing Chaos Redux systems

Secret Alliance should connect to existing systems only where the connection improves play.

| System | Connection direction |
| --- | --- |
| Chaos Meter | Higher chaos changes recruitment, operation aggression, and evolved opening strength |
| Event logs | Fire entry, record evolutions, record reveal, and show current detail text without spoiling hidden members |
| Deaths system | Only use for killing or major sabotage events that actually cause population loss, keep it rare and bounded |
| Condemnation | Do not use ordinary condemnation for diplomatic sabotage unless unconventional weapons or atrocities are involved |
| Faction systems | Hidden compact becomes a public faction only after reveal |
| Intelligence agency | Agency ownership can improve investigation, but the event should still work if target lacks an agency |
| Existing events | Tensions Rising can make recruitment easier, Intel Leaked can lower pact secrecy, The Great Embargo can increase pact interest in economic pressure, Random Terror can share sabotage-style damage only through safe helper logic |

Do not force unrelated systems into this event. The event is about secret coordination, counterintelligence, and a diplomatic coalition turning into public war.

## Asset plan overview

Secret Alliance needs a compact visual identity centered on coded diplomacy, unsigned treaties, hidden seals, broken wax, intercepted couriers, faction emblems, industrial sabotage, and a dark board of suspect cards. Avoid generic maps as the main motif.

Required asset families:

| Asset family | Target use | Source mode | Notes |
| --- | --- | --- | --- |
| Decision category icon | Counter-pact category | Generated icon | Small clear seal, dark pact motif, readable at category size |
| Decision icons | Investigation, security, diplomacy, border, war preparation | Generated icons | Separate 32x32 icons, not resized focus icons |
| Idea icons | Friction, bureau, preparedness, exposed member, patron shield | Generated icons | 64x64 compact symbols |
| Report images | Early incident, sabotage aftermath, defector trail | Generated period documentary or sourced if implementation finds perfect archival image | Apply report-card treatment |
| News image | Public reveal of Anti-[target] Pact | Generated period-news composition | Black and white final news image |
| Faction emblem | Revealed pact emblem | Generated fictional emblem | Use no readable text, must work as small symbol |
| GUI pieces | Board background, suspect cards, meters, warning frames | Generated UI art plus deterministic layout | Functional UI built by implementation, not generated layout |
| Animated seal and warning states | Category or GUI state feedback | Generated real source frames | Static fallback required for every animated asset |
| Achievement icons | Planned achievements | Generated 64x64 completed icons | Grey and not-eligible variants produced by achievement asset flow |

Reference folders for asset workers:

| Asset type | Reference folder to inspect |
| --- | --- |
| Idea and national spirit icons | `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas` |
| Decision and category icons | `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/decisions` |
| Report images | `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/report_event_images` |
| News images | `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/news_event_images` |
| Achievements | `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/achievements` |

## Achievement design

Achievement names below are working labels only. Final titles and descriptions must be written during implementation from the direction here.

| Achievement id | Working label | Eligibility | Unlock condition | Disqualifier | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- |
| `sa_every_thread_named` | Every Thread Named | Target country | Expose every active core member before public reveal or war-trigger reveal | Any core member enters war with target before all are exposed | Hard | A board of pinned strings converging on a hidden seal |
| `sa_paper_collapse` | Paper Collapse | Target country | Dissolve the pact through diplomacy before faction war begins | Target starts preemptive war | Medium-hard | A cracked treaty seal and falling unsigned papers |
| `sa_turn_the_knife` | Turn the Knife | Target country | Convince one core member or patron associate to defect, then use their evidence to expose another member | Defector dies or returns to pact | Hard | A broken handshake with a hidden dagger silhouette |
| `sa_prepared_for_every_border` | Prepared for Every Border | Target with at least one neighbor member | Enter public crisis with high preparedness and all exposed member borders covered by supplied divisions | Any border mission fails during crisis | Hard | Fortified border posts under a shadowed pact emblem |
| `sa_small_country_large_shadow` | Small Country, Large Shadow | Target starts as minor | Defeat or force surrender of a revealed pact that includes at least one major patron | Player joins a major faction after reveal before defeating pact | Very hard | Small flag standing under three larger shadows |
| `sa_ten_signatures` | Ten Signatures | Target country | Defeat, dissolve, or split a pact that reached at least ten core members or revealed members | None beyond route completion | Very hard | Ten wax seals around a central cracked seal |
| `sa_bad_evidence_backfire` | Bad Evidence Backfire | Target country | Recover from a failed public accusation, later expose the true pact, and avoid capitulation until crisis ends | Target capitulates during the recovery route | Hard | A burned dossier with one intact page |
| `sa_no_factory_lost` | Unbroken Workshops | Target country | Complete the event chain after Evolution II without successful major industrial sabotage | Any major factory sabotage succeeds after E2 opens | Hard | Factory silhouette behind a locked evidence case |

Achievements should reward mastery, not automatic event firing. The implementation should add tracking flags at the moment each disqualifier happens rather than trying to infer everything at the end.

## Documentation and spreadsheet direction

The event doc should explain the hidden-pact lifecycle, member selection, reveal logic, counter-pact decisions, evolutions, AI behavior, assets, and achievements. It should not list hidden variables as if they are player-facing text.

The catalog and event-system registration should keep Event 011 standalone. Do not attach it to an event cluster unless the source spec changes.

The event catalog details field should describe the premise in player terms: unrelated countries begin coordinating pressure against the target, the pattern can grow into a hidden compact, and later counterintelligence or public reveal can turn it into a faction crisis. Evolution fields should describe the three evolution stages as actual evolution tracks. Baseline progression should stay out of evolution columns.

## Acceptance criteria for implementation

| Surface | Must be true before completion |
| --- | --- |
| Random event registration | Event 011 is registered as Minor Fire-Once and returns unavailable when valid candidates do not exist |
| Hidden pact setup | Three valid initial minor members are stored and invalid members are cleaned up |
| Member rules | Members are not at war with target at hidden formation, and war with target forces reveal handling |
| Evolutions | Evolution I, II, and III have active-event and pre-fire opening behavior where required |
| Decision category | Counter-pact category opens at the correct stage, uses dynamic values, and avoids store-like costs |
| Operations | Pact operations are paced, dynamic, and bounded |
| Reveal | War-trigger reveal forms public pact and joins valid members against target immediately |
| AI | Pact members, major patrons, second major, target AI, and neutral actors have route-aware behavior |
| Assets | Required icons, reports, news image, GUI pieces, faction emblem, animations, and achievement icons are produced or blocked honestly |
| Localisation | Final text follows direction-only constraints and does not reveal hidden mechanics too early |
| Event details | Details show premise and current known stage without mechanical reward lists |
| Achievements | All planned achievements have tracking, disqualifiers, localisation direction, and icon coverage |
| Cleanup | Invalid members, stale targets, obsolete decisions, and post-reveal hidden state are cleaned |
| Validation | Completion report includes route coverage, decision audit, AI checks, reveal checks, and asset status |

## Implementation risks

| Risk | Mitigation |
| --- | --- |
| Hidden member arrays become stale | Central cleanup helper before every operation and reveal |
| Pact forms visible faction too early | Keep hidden compact separate from HOI4 faction until reveal |
| Member already at war with target gets missed | High-priority reveal check in event and war-related hooks |
| Decisions become political power store | Use missions, equipment, XP, divisions, routes, supply, and evidence requirements |
| Player sees hidden list too early | Use estimates and exposed-member cards only |
| Major patron creates unfair war spike | Use evidence and preparedness to split or delay joiners |
| Border wars appear for distant members | Gate neighbor decisions by real border or strategic passage |
| AI suicidally joins pact | Use strength, war state, target faction, and patron checks |
| Report text spoils future reveal | Use observed pattern and uncertainty, not direct labels |
