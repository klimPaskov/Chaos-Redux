# 078 Border Conflict

## Catalog

| Field | Design |
| --- | --- |
| Event ID | `078` |
| Event name | Border Conflict |
| Entry event | `chaosx.nr78.1` |
| Type | Minor Repeatable |
| Catalog status | To Be Reworked |
| Chaos level | 1 |
| Cluster | Wars |
| Member severity | Medium |

## A world of disputed frontiers

Border commands across the world begin fighting limited battles over neighboring territory.
Each eligible land-neighbor relationship receives a real HOI4 border conflict over one declared state.
A government can face several neighbors at once, even while its main army is fighting an unrelated normal war.
Victory changes the frontier and can expose the next state to attack.

The player manages these crises through the army they actually possess.
Troops sent to one frontier cannot also defend every other frontier.
A useful industrial state may be worth a serious commitment, while a remote border can become dangerous because losing it opens a route toward more valuable territory.
Existing terrain, supply, forts, equipment, and the native border-war participation rules determine the military problem.

The event does not create normal wars, war goals, faction invitations, or escalation buttons.
It does not grant new troops, refill divisions, manufacture combat results, or pay political power for winning.
The map change is the principal reward.
The losses and diverted military capacity are the principal cost.

## The single-state stake

Each dispute names an attacker, a defender, an attacking staging state, and one disputed state owned by the defender.
The two states form a legal native border-war front.
Only the disputed state is a territorial stake.
The staging state is the attack's starting position and is not awarded to the defender.

An attacking victory transfers ownership and control of the disputed state to the attacker after the result has been validated.
A defending victory leaves that state with the defender.
A draw or cancellation transfers nothing.
This is the operational meaning of the winner receiving the disputed state when one participant already owns it.

The entire declared state changes hands, not an arbitrary province within it.
Existing cores, claims, buildings, resource deposits, population, and state-bound systems remain attached to the state unless their own established rules change them after ownership changes.
Capturing a state does not automatically grant a new core or claim, destroy its industry, remove its forts, or supply an event-specific integration bonus.

A capital or final remaining state is not protected merely to preserve a country.
It can be selected when the installed game's native mechanics and ownership-transfer behavior support it safely.
Those cases require explicit engine tests before release.
An unsupported case is documented as a native validity restriction, not hidden behind a general preference for weak or unimportant targets.

## Worldwide opening

One firing is one worldwide wave.
The event inspects the current land frontier and builds a set of unordered neighboring country pairs.
A pair such as A and B appears once, regardless of which country's border produced the discovery.
Countries are not filtered by player control, major status, ideology, strength, or their participation in unrelated wars.

For each pair, the event constructs candidate disputed states on either side of the shared frontier.
A state belongs to the candidate set only when the state owner and a legal opposing staging state can participate in a native border war there.
The opposing staging state must directly border the disputed state through a valid land connection.
Naval proximity, a shared sea zone, and an ordinary country-neighbor test that accidentally includes a strait are insufficient without a verified native land-combat connection.

The event excludes a country pair when its members are already fighting each other in a normal war.
It does not exclude A versus B because A is at war with C.
It does not use a country-wide prohibition on having any border war.
An existing incompatible battle reserves its actual footprint and prevents reuse of those states.
Other independent frontiers remain eligible.

At the baseline, each pair receives one new dispute unless that pair already has an unresolved Event 078 dispute.
In that case another baseline copy is not created.
At evolved levels, distinct additional disputes against the same neighbor are allowed within the current frontier budget.
A later wave never adopts an earlier wave's result, chain, or achievement progress as its own.

Pairs are considered in a seed-stable shuffled order.
Within the selected pair, choose uniformly among distinct valid disputed states, counting each state once even when it touches several opposing provinces or staging states.
After choosing the stake, choose uniformly among its legal staging states.
The state owner's identity determines which country defends.
This deliberately gives every eligible state one ticket, not every province one ticket.
A country with more eligible frontier states can therefore be selected as defender more often.

The system reserves both native endpoint states before starting a battle when the native mechanic treats those states as exclusive.
A state cannot be a target in one dispute and a staging state in another incompatible dispute.
No second transaction can claim it during the same opening pass.
A pair whose final valid candidate is consumed by another battle receives no unsafe substitute.
The reason is recorded as a reservation collision and eligibility is checked again on a later firing.
This is a state-level restriction, not permission to serialize all of a country's conflicts.

All baseline pair allocations are attempted before evolved extra fronts are allocated.
This prevents the first long border in the iteration from consuming all the usable states before other neighbors are considered.
There is no authored global-country cap and no one-conflict-per-country rule.
The actual simultaneous limit comes from valid native fronts and safe state reservations.

## What the player does

The opening report identifies the country's opponents, disputed states, and which side the country occupies on each front.
The native battle and map interface remain the military controls.
A compact native decision category provides state-targeted situation records so a player with several conflicts can find every threatened or contested state.
These are navigation and information records, not a second combat system.

The player can reinforce exposed areas, protect a valuable frontier, retain a reserve, or accept the risk created by a more important normal war elsewhere.
They cannot buy an automatic win, veto a valid firing by refusing an event option, or change a committed stake by reopening its report.
Any acknowledgement closes text only.

The presentation distinguishes an offensive opportunity from a defensive liability.
It shows the target state, the opponent, the current result or active battle, and whether an established momentum chain is involved.
It never suggests that winning the defensive battle grants a second state.
The underlying military UI decides which divisions can enter or leave the clash.
The event must not advertise army controls that the installed native mechanic does not provide.

Uninvolved countries do not receive a report for every local fight.
A significant worldwide wave can generate one general news item, while the shared event history records the single worldwide event and its applied evolutions.
Participant results are consolidated by country and day so a broad wave does not become a sequence of near-identical popups.
State transfers happen at resolution and do not wait for acknowledgement.

## Evolution I: Multiple Frontiers

At Chaos 200 or above, this evolution makes large shared frontiers capable of supporting several simultaneous disputes between the same two countries.
Each dispute still has one target state and one staging state, with independent military results and territorial stakes.

A long frontier is measured in independent usable state fronts, not pixels, provinces, coastline length, or total national size.
Construct a seed-stable set of state-disjoint candidate fronts and call its size F.
An existing compatible Event 078 front consumes one slot in this accounting.
The initial tuning target is one baseline front plus one extra front per five independent frontier slots, bounded by the available slots.
Thus F equal to 5 supports two simultaneous disputes, and F equal to 10 supports three.
A short border continues to produce its ordinary single dispute.

Allocate extra fronts in rounds, giving every eligible pair an opportunity before any pair receives its next extra front.
A filled slot is not refilled simply because its battle ended.
Each root dispute is an opening opportunity with a persistent lineage, not a factory for repeated attacks.
Additional conflicts after a root ends require an eligible momentum continuation, a genuinely new evolution allocation, or a later Event 078 firing.

This creates a real choice on broad borders.
A country can win one state and lose another during the same wave.
One front can advance while a different front is held.
The results are not combined into a fictitious overall winner that takes every stake.

## Evolution II: Border Momentum

At Chaos 400 or above, an attacking victory can begin a chain of further border wars.
The first capture must create a newly adjacent, valid state of the same opponent.
The initial chance to seed a chain is 25 percent when at least one such continuation exists.
A failed seed roll ends that root after its ordinary victory.
No roll is consumed when there is no valid continuation.

Once a chain has begun, every further attacking victory immediately starts the next valid conflict.
There is no repeated chance to stop a running chain after each success.
It ends when the advancing country loses, the battle is cancelled, the original pair becomes invalid, or no valid continuation remains.
A defending victory stops the advance and retains the current target.
It does not reverse the chain or create a counterattack automatically.

The next target must directly border the state just captured and must not have bordered the advancing country immediately before that capture.
The candidate is therefore a state that this victory actually brought onto the attacker's frontier.
An unrelated old border state does not qualify simply because it is convenient.
Before each transfer, the event records the small local adjacency set needed to establish that difference.

The chain stays between its original two countries.
A newly exposed third country's border is checked by a later worldwide firing.
Multiple roots against one opponent can develop separate chains, but they share the state reservation rules and cannot attack the same state.
A target already fought over by the same wave is unavailable for another dispute in that wave, including after a later recapture.
That prevents two chains from farming the same land back and forth.

The next conflict starts in the same resolution sequence, or at the first engine-safe scheduling point required to close the previous battle.
It has no added preparation period.
The newly captured state becomes its staging state when native validity allows it.
The event does not restore the attacking force's losses or organization between battles.
Growing distance, accumulated casualties, and the native military situation make successful chains costly to sustain.

## Evolution III: Borders in Motion

At Chaos 600 or above, the event uses the full independent frontier set for simultaneous disputes when Multiple Frontiers is enabled.
Long borders can therefore open many distinct battles during one wave.
The initial momentum seed chance rises from 25 to 75 percent when Border Momentum is enabled.
Established chains retain their continuous advance rule.

This evolution changes how extensively the existing mechanics are used.
It does not add a national attack bonus, a random state-transfer effect, or an automatic normal war.
The pressure comes from more actual fronts and more captures developing into continued advances.

Individual evolution toggles remain authoritative.
Disabling Multiple Frontiers prevents additional simultaneous roots against one neighbor even with Borders in Motion enabled.
Disabling Border Momentum prevents chains, including the higher seed chance.
Borders in Motion amplifies enabled mechanics only and is not recorded as applied when it has no enabled behavior to change.

## Evolved openings and active evolution

At entry, the current Chaos value and the event's evolution settings determine which evolved opening profile is permitted.
Enabled qualifying evolutions can apply immediately to the new wave.
The baseline does not have to play out first in a high-Chaos world.

An already active wave uses the project's paced evolution route.
Newly qualifying enabled mutations become eligible for an event-scoped MTTH check, with a starting timing target of 90 days.
Eligibility is not an immediate conversion.
Rising across 200, 400, or 600 is not a new worldwide firing.
Only one mutation is applied at a time, and its history entry is recorded once after it has actually changed the wave's capabilities.

An active Multiple Frontiers mutation can allocate the newly available root quota for pairs already represented in that wave.
An active Border Momentum mutation affects future capture resolutions.
It does not revisit old victories and roll them again.
An active Borders in Motion mutation raises the remaining opening quota and the seed chance for later unseeded root victories.
It does not duplicate roots that have already been admitted.

Falling Chaos does not undo a battle, return land, or erase an already applied mutation.
Disabling an evolution blocks its future allocations or new chain steps, while an already running battle resolves against its declared stake.
Disabling Event 078 blocks new waves and new event-created starts but does not erase a committed battle's territorial result.
A closed wave stays closed and is not kept alive solely to wait for another evolution.

## Outcomes and aftermath

A battle has one terminal result and at most one state transfer.
An attacking victory can create another battle only after the transfer and the resulting frontier have been validated.
A defending victory creates a clear local success without an unrelated payment or territorial reward.
A draw or cancellation produces a result record and releases this conflict's own reservations.

If the two countries enter a normal war against one another during the dispute, Event 078 cancels that dispute without a scripted state award and ends its chain.
It does not end or modify the normal war.
If a third party takes an endpoint, a participant disappears, the pair changes through a civil-war split, or the native battle ceases to match its stored participants, resolution is cancelled or held for safe cleanup.
The event never transfers land from an unrelated current owner merely because an old callback arrived.

After a valid capture, ordinary ownership, supply, resistance, diplomacy, and other state-linked rules resume their normal roles.
Event 078 does not force former owners to recognize the frontier, erase their claims, or stop their own later political actions.
However, this event itself offers no path that starts a normal war.

Every firing recalculates the frontier from the current map.
Earlier gains can be exposed in a later wave.
Old opponents may no longer be neighbors, and new neighbors may enter the candidate set.
Resolved records remain available for history and achievement evidence without reserving the land forever.

## Chaos feedback

The first successfully started native battle in a wave can add 5 Chaos for the event's outbreak of limited interstate fighting.
A wave that reaches five distinct fighting pairs across at least five countries can add another 5 Chaos for its worldwide spread.
A single chain that reaches five valid captures can add another 5 Chaos for its sustained advance.
These sources have separate rolling guards and a maximum combined grant of 15 per wave.

Starting an evolution, becoming eligible, logging a history row, resolving an ordinary transfer, or winning an arbitrary number of isolated skirmishes does not independently add Chaos.
The shared systems retain ownership of generic deaths, war declarations, annexation, and world tension.
The event-specific sources recognize the limited-war outbreak, simultaneous spread, and chain development only.

A defender that stops an established five-capture chain and holds its defended target for 30 days can qualify for a 5 Chaos containment reduction.
The affected opponent must have no active advancing chain against that defender at confirmation.
The wave must have previously granted enough event-owned Chaos to cover the reduction.
Only one containment reduction can be paid per wave.
Cancellation, a settings change, and a fabricated result are not containment successes.

## Campaign character

In a calm campaign, the event produces a sudden global set of small territorial risks.
A major can be surprised on a neglected frontier, while a smaller country can gain useful land through a real local victory.
In a more chaotic campaign, long borders split the player's attention and a single breach can open further territory.
The event remains legible because every active battle names exactly one stake.

Replay variation comes from the current borders, random stakes, army deployment, ordinary wars elsewhere, evolution settings, and the geographical routes created by previous captures.
It does not require a separate currency or a large collection of modifiers.

## Supporting specifications

- [Worked campaign cases](mechanics/078_border_conflict_spec_part_4_worked_campaigns.md)

- [Frontier and chain rules](mechanics/078_border_conflict_spec_part_2_frontiers_and_chains.md)
- [Evolution, tuning, and Chaos](mechanics/078_border_conflict_spec_part_3_evolutions_tuning_and_chaos.md)
- [Player presentation, AI, and writing](presentation/078_border_conflict_spec_part_5_player_ai_and_writing.md)
- [Achievements](achievements/078_border_conflict_spec_part_6_achievement_design.md)
- [Asset brief](presentation/078_border_conflict_spec_part_7_asset_brief.md)
- [Implementation and evidence plan](../../plans/078_border_conflict_plans/README.md)
