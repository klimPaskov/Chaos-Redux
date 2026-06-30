# Event 011: Secret Alliance, Part 2

Player-facing wording note: every title, option, decision name, focus-style label, achievement title, GUI label, event-detail line, report text, and news text in this package is direction only. Working labels are internal handles for implementation and asset routing. The implementation pass must write final localisation from the directions here, without copying working labels into the game unless a label is explicitly marked as an identifier.

## Evolution architecture

Secret Alliance uses evolutions as true mutation tracks, not ordinary baseline stages. Ordinary pact pressure can rise inside the baseline. Evolutions change who can join, how visible the pact becomes, and what response tools the player receives.

The implementation should support both active-event evolution and pre-fire evolved opening.

Active-event evolution means the hidden pact already exists and the evolution changes the current pact. Pre-fire evolved opening means Event 011 has not fired yet, but the world has reached the relevant chaos state, so the first firing starts in a stronger form.

## Baseline stage

Baseline starts with three minor core members when enough valid candidates exist. If exactly three strong minor candidates do not exist, the event should avoid firing rather than create a weak substitute. If a later implementation wants associates to fill a thin world, they can be courted but should not count as the required core opening.

Baseline content:

| Surface | Baseline behavior |
| --- | --- |
| Members | Three hidden minor core members |
| Visibility | No pact name and no public faction |
| Player tools | First popup options and ordinary passive clues, no full counter-pact category |
| Operations | Slow diplomatic pressure, courier signs, propaganda, trade nuisance |
| Recruitment | Very limited, usually associate courting only |
| War risk | Low unless an unrelated war with a member begins, which forces reveal handling |
| Player effect | Subtle suspicion and small frictions |

Baseline should be strong enough to matter after time, but not strong enough to make the player feel punished for a mechanic they could not yet read.

## Evolution I: wider minor compact

Evolution I expands the pact through minor-country recruitment and makes the pattern more noticeable. It remains hidden. No direct war plan should appear yet, and the player still does not receive the full retaliation layer.

Active-event evolution:

| Change | Detail |
| --- | --- |
| Recruitment | The pact can invite more minor countries and turn associates into core members |
| Operations | Propaganda, trade nuisance, and intelligence activity become more frequent |
| Suspected pattern | The target can receive clearer reports after repeated incidents |
| Member coordination | Hidden members can share small bonuses or synchronized diplomatic actions |
| Defection chance | Low, but small members with high fear and low commitment can leak information |

Pre-fire evolved opening:

| Opening element | Behavior |
| --- | --- |
| Initial members | Four to five minor members, chosen with the same validity rules |
| First event | The first popup direction should imply a broader pattern without naming a pact |
| Starting values | Higher pact cohesion and recruitment pull than baseline |
| Player state | Suspicion begins higher, but the pact remains unnamed |

Evolution I operation examples:

| Working operation | Mechanical role | Counterplay seed |
| --- | --- | --- |
| Repeated shipping inspections | Small convoy, trade, or market route penalty | Later port security decisions become stronger |
| Coordinated press campaign | Temporary stability or ideology irritation | Later propaganda tracing can produce evidence |
| Embassy triangle meetings | Cohesion and readiness gain | Later diplomatic observation can expose member pairs |
| Military attaché exchange | Readiness gain | Later staff watch can reduce war surprise |
| Procurement shadow | Small equipment or production disruption | Later contract audit can find a member |

## Evolution II: major patron and open counterplay

Evolution II is the point where the player should definitely know that something organized is happening, even if the full membership is not known.

Active-event evolution:

| Change | Detail |
| --- | --- |
| Major patron | One eligible major can join as a patron or directing member |
| Operations | Sabotage, threats, killings, and provocation events unlock |
| Player tools | Counter-pact decision category opens |
| Evidence model | Target evidence becomes a visible value |
| Preparedness model | Target preparedness becomes visible and can change later war outcome |
| Member exposure | Individual countries can be exposed before full reveal |
| Diplomatic split | Members can be pressured to defect, pause support, or refuse war joining |

Pre-fire evolved opening:

| Opening element | Behavior |
| --- | --- |
| Founder | An eligible major country becomes founder or patron |
| Minor members | Two to four minor countries are recruited at opening |
| First event | The first report direction should show clear organized pressure without naming all actors |
| Player tools | Counter-pact decision category opens soon after the opening event |
| Starting values | Pact readiness and hostility begin above baseline, evidence begins with one seed |

Major patron eligibility:

| Requirement | Direction |
| --- | --- |
| Not target | The target cannot found the pact against itself |
| Not at war with target | War with the target would immediately force reveal logic |
| Has strategic reach | Major patron should have diplomacy, industry, navy, intelligence capacity, or regional influence |
| Has plausible motive | Rival ideology, bad relations, fear of target growth, territorial conflict, or faction rivalry |
| Can survive backlash | Avoid suicidal patron selection when the target is overwhelmingly stronger unless chaos is very high |
| Not locked by incompatible event state | Avoid making another event-created endgame actor a normal patron |

Evolution II operation families:

| Family | What happens | Player-readable consequence | Counterplay |
| --- | --- | --- | --- |
| Factory sabotage | Damages civilian or military industry in target states | Visible repair burden and suspicion gain | Industrial security, worker informants, contract tracing |
| Officer killing | Wounds or removes a low-tier officer, adds temporary command disruption | Clear shock, strong suspicion | Protective details, counter-network, diplomatic warning |
| Rail interference | Damages or strains rail hubs and supply routes | Supply risk in named regions | Rail guard missions and route audits |
| Border provocation | Creates a border incident with a neighboring member or suspected member | Escalation risk and potential border war | Frontier watch, controlled search, negotiation |
| Diplomatic threats | Member or patron issues veiled public pressure | Opinion shock and readiness change | Private demarche, public inquiry, ally consultation |
| Agent exposure | A foreign cell is found but identity is partial | Evidence gain, possible false lead | Interrogation chain, cipher comparison |

The event should avoid random leader assassination unless the player has meaningful counterplay and the selected leader role is not campaign-breaking. If the implementation includes killings, use bounded temporary effects, advisor wounds, officer retirements, or scripted minor-character losses more often than killing the country leader.

## Evolution III: public crisis and faction reveal pressure

Evolution III is the public crisis phase. The pact can become visible on the map, issue demands, add a second major, or prepare a coordinated war. The player gains war options, but the pact should not always attack instantly when the evolution logs. There should be a final pressure window where preparedness, evidence, and diplomacy still matter.

Active-event evolution:

| Change | Detail |
| --- | --- |
| Public presence | The faction object can appear directly when reveal conditions are met or the pact chooses public posture |
| Members | More minors can join, and a second major may join if player choices left the pact strong |
| War risk | The pact can start a war countdown, ultimatum, or coordinated declaration |
| Player options | War option, demand dissolution, preemptive strike, alliance consultation, and border readiness tools unlock |
| Pact pressure | Sabotage becomes less deniable and more aggressive |
| Diplomacy | Defection and split options remain possible, but harder |

Pre-fire evolved opening:

The event should not jump directly into Evolution III if it has never fired. It should start from the Evolution II opening with a major founder and stronger pressure, then progress toward Evolution III after a later pacing delay. This preserves the user’s desired two-step escalation and gives the player time to react.

Second major logic:

| Player and pact state | Second major behavior |
| --- | --- |
| Target ignored investigations and has low preparedness | Second major more likely to join as full member |
| Target exposed several members and split at least one away | Second major less likely or joins only as associate |
| Target has strong faction backing | Second major may stay covert or refuse |
| Pact cohesion is high and target is isolated | Second major can join openly at public reveal |
| Chaos is very high | Second major can join despite risk |

Evolution III operation examples:

| Working operation | Role | Response |
| --- | --- | --- |
| Public joint communiqué | First open signal of compact unity | Demand dissolution, ask allies, public evidence release |
| Border ultimatum | Creates a timed military pressure mission if neighbor member exists | Reinforce border, accept talks, launch border war, prepare strike |
| Industrial crippling campaign | Strong sabotage attempt against named industrial state group | Emergency repair and internal security missions |
| Pact war council | Readiness and cohesion spike, war countdown begins | Evidence dump, diplomatic split, emergency mobilization |
| Defector panic | One weak member tries to leave or leak records | Protect defector, exploit defection, risk exposing target methods |

## Reveal rules

There are several reveal types. The war-trigger reveal is the sharpest and follows the user’s rule exactly.

| Reveal type | Trigger | Public faction creation | War behavior |
| --- | --- | --- | --- |
| War-trigger reveal | Any core pact member goes to war with the target through any source | Immediate | All valid core members join war against the target immediately |
| Evidence reveal | Target reaches evidence threshold and chooses to expose the pact | Yes or delayed according to decision outcome | War countdown or diplomatic crisis, not always instant |
| Pact public reveal | Evolution III pact chooses public posture | Yes | War countdown, ultimatum, or immediate war if readiness is extreme |
| Failed provocation reveal | Border or sabotage operation fails badly | Usually yes | Member may be isolated unless pact cohesion is high |
| Defector reveal | Member leaks records | Optional public reveal or hidden evidence gain | War avoided if target handles it quietly, war risk if public |

War-trigger reveal must be handled as a high-priority hook. If a pact member enters war with the target, do not let the hidden network remain hidden. The revealed faction forms instantly, valid members are invited or forced into the faction according to engine-safe implementation, and they declare or join war against the target. Members that became invalid are removed first.

## Reveal aftermath states

After reveal, the event enters one of several states:

| State | Meaning | Player outcome direction |
| --- | --- | --- |
| Clean exposure | The player has strong evidence and high preparedness | Pact cohesion drops, some members hesitate, war may be delayed or weaker |
| Panicked reveal | A war or failed operation exposes the pact before the player is ready | Pact cohesion and readiness are high, members join quickly |
| Split compact | One or more members defected before reveal | Smaller faction, more evidence for target, lower readiness |
| Patron shield | A major patron protects minors from diplomatic pressure | Higher war risk, stronger sabotage, but more evidence once exposed |
| Public dissolution | The player breaks the pact through diplomacy before full war | Pact members suffer diplomatic penalties, target gains prestige and security bonus |
| Public war | The pact becomes a visible hostile faction | War package, final member cleanup, military decisions replace covert tools |

These states should be recorded in event flags or variables because they determine achievements, docs, event log details, and later AI behavior.

## Event details and evolution log direction

Event Details should describe the situation and premise, not list modifiers. It should not spoil hidden members before reveal. The detail text direction should change by known stage:

| Known stage | Event Details direction |
| --- | --- |
| Before any firing | A reserved catalog entry can describe the possibility of unusual diplomatic coordination only after implementation updates the catalog |
| Baseline fired | The player sees repeated frictions and unexplained shared phrasing among unrelated governments |
| Evolution I | The pattern spreads across more capitals and trade routes, still without a public name |
| Evolution II | The target has enough evidence to create a counterintelligence response, but not enough to name every actor |
| Evolution III | The compact approaches public confrontation and suspected members are harder to separate from each other |
| Revealed | The Anti-[target] Pact is a public faction or wartime coalition |

Evolution log directions:

| Evolution | Log direction |
| --- | --- |
| Evolution I | A wider minor compact has begun copying the same pressure pattern across more governments |
| Evolution II | A major patron or major-style directing center has made the hidden pressure more organized and violent |
| Evolution III | The compact is moving from hidden pressure toward public confrontation and war planning |

The final implementation should use stage-specific display text across the Event Log surfaces that show evolution history.
