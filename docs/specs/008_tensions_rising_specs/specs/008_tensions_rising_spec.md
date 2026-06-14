# Event 008: Tensions Rising  -  Source Specification

## Event identity

**Event ID:** `8`  
**Event name:** `Tensions Rising`  
**Type:** Minor Repeatable  
**Status:** To Be Reworked  
**Cluster handling:** `Diplomatic Panic` may be kept, with for now one member at medium severity
**World-end scenario:** None

`Tensions Rising` is the small headline that makes the rest of the world feel less stable. It does not release a country, start a focus tree, create a formable, or end the world. It is a pressure event that makes the ordinary Chaos Redux timer and diplomatic memory feel alive: early it nudges world tension upward, later it becomes a ritual of public denials, secret cables, mobilization scares, poisoned relations, insurance spikes, propaganda opportunism, and exhausted general staffs.

The reworked event keeps the user-provided core:

- In Calm World, the event raises world tension by `+10` and should only fire while world tension is below `100%`.
- Once the first evolution is active, the event can fire even when world tension is already `100%`.
- Later evolutions add direct chaos, larger world tension packets, temporary timer pressure, relation damage, and delayed follow-up reports.
- The event never has a world-end scenario.

The emotional center is not that a map changed. The emotional center is that every government begins acting as if a map is about to change.

## Player-facing fantasy

The player should see `Tensions Rising` as an apparently simple repeatable event that becomes increasingly uncomfortable. At first it is a straightforward tension bump. Later, the same headline starts leaving fingerprints: embassies close side doors, neutral shipping gets nervous, opposition newspapers claim secret mobilization, staff cars move after midnight, and old allies start filing formal complaints.

The event should feel different from direct war events. It is about the world preparing to make mistakes. It should push the campaign toward volatility without replacing the existing war, alliance, and major-event systems.

## Baseline Calm World incident

### Name direction

Working popup title: **Tensions Rising**

The baseline incident is a short report, not a dramatic apocalypse announcement. It should read like a sober foreign-office bulletin:

- “A sequence of public accusations, military communiqués, and newspaper leaks has unsettled diplomatic circles.”
- “No government is admitting to a crisis, which has made observers more nervous.”
- “Markets, staff offices, and border commands are reacting before any formal declaration is made.”

### Baseline trigger and effect

The baseline version fires only while the world remains below full tension.

| Stage | World state | Fire condition | Direct effects | Hidden side effects |
| --- | --- | --- | --- | --- |
| Baseline | Calm World / no Event 8 evolution active | World tension below `100%` | `+10` world tension | None beyond normal Minor Repeatable event-system consequences |

The baseline version should be clean and readable. Do not add relation damage or direct chaos at this level. It is the first crack in the glass, not the first shard.

### Baseline player text promise

The player-facing text should mention the public uncertainty and the rise in tension. It should not mention hidden future systems, hidden event weights, future evolutions, or timer manipulation.

Recommended option text: **Another file on the desk.**

## Evolved identity

`Tensions Rising` has one evolution track: **Diplomatic Fever**.

This track is not an ordinary stage progression. It represents the world learning how to panic faster. Each evolution changes how future firings behave, it does not require the event to fire instantly when the chaos tier changes.

The track has four stages, matching the user-provided progression:

| Evolution stage | Working title | Minimum chaos tier | World tension effect | Chaos effect | Can fire at 100% world tension? | Hidden layer |
| --- | --- | --- | --- | --- | --- | --- |
| I | Cable Traffic Flood | Gathering Storm | `+10` | `+10` | Yes | light timer pulse, one or two diplomatic shocks, optional delayed report |
| II | The Accusation Market | Rising Chaos | `+20` | `+15` | Yes | stronger timer pulse, multiple opinion shocks, temporary pressure spirits |
| III | General Staffs Stop Sleeping | Chaos Tier | `+50` | `+25` | Yes | heavy timer pulse, war-plan fever, near-miss follow-ups |
| IV | The Permanent Alert | Totalen Chaos | `+100` | `+50` | Yes | severe timer pulse, broad relation damage, delayed reports |

The evolution should be recorded when the stage becomes active or first manifests. Event detail text should preview the evolved behavior in broad terms, but it should not reveal the full random headline list or exact pair-selection math.

## Evolution stage I: Cable Traffic Flood

At Gathering Storm, public fear becomes self-reinforcing. The same event now adds chaos directly and can fire even when ordinary world tension is already maxed out.

### Direct effects

- `+10` world tension.
- `+10` chaos.
- Can fire at `100%` world tension.

### Hidden effects

- Apply a small temporary **Tension Pulse** to the automatic event pacing logic.
- Apply one or two timed negative opinion modifiers between plausible diplomatic rivals.
- Small chance of a delayed report event several days later.

### Tone

Stage I should feel like wires, clerks, desk lamps, and official denials. Nobody has crossed the line yet, but more countries are drawing lines.

### Follow-up report candidates

- **The Telegram Nobody Signed**  -  a leaked diplomatic message is denied by every government named in it.
- **Embassy Side Doors**  -  staff begin using side entrances and refusing public comment.
- **The Calm Map Says Nothing**  -  if world tension is already `100%`, newspapers note that official statistics can no longer measure the mood.

## Evolution stage II: The Accusation Market

At Rising Chaos, fear becomes a market. Every rumor is valuable to somebody: opposition parties, arms manufacturers, intelligence offices, border commanders, nationalist newspapers, and foreign sponsors.

### Direct effects

- `+20` world tension.
- `+15` chaos.

### Hidden effects

- Apply a stronger temporary Tension Pulse.
- Apply two or three timed negative opinion modifiers between rival countries.
- Select one or more eligible countries for a temporary national spirit or timed country modifier representing panic-driven policy: higher war support or mobilization willingness, lower stability or diplomatic trust.
- Increase temporary selection pressure for nearby diplomatic and war-adjacent events without directly forcing those events.

### Tone

Stage II is louder and more cynical. Governments are still denying war, but ministries, newspapers, and markets are behaving as if war has become sellable.

### Follow-up report candidates

- **Insurance Rates Jump in Neutral Ports**  -  convoy operators price the panic before diplomats can describe it.
- **One Denial Too Many**  -  a government’s third denial is treated as evidence by its enemies.
- **The Rumour That Arrived Twice**  -  identical false reports arrive in two capitals from supposedly separate sources.

## Evolution stage III: General Staffs Stop Sleeping

At Chaos Tier, suspicion enters the armed services. The event should make the AI and event ecosystem more willing to tilt toward conflict, but it should not create free wars. Wars still belong to war events, focuses, decisions, claims, and AI strategy.

### Direct effects

- `+50` world tension.
- `+25` chaos.

### Hidden effects

- Apply a heavy Tension Pulse.
- Apply three to five timed relation shocks, weighted toward major powers, faction leaders, border rivals, ideology rivals, claim holders, and countries with recent hostile history.
- Create a chance of a **near-miss** follow-up: fleets shadow each other, border guards exchange warning shots, staff maps are copied, or a mobilization order is drafted and recalled.
- Temporarily increase AI willingness for hostile diplomatic posture, guarantees, faction invitations, military build-up, and existing war-adjacent decisions.

### Tone

Stage III should read like fatigue. The world is not only angry, it is tired, jumpy, and running on memoranda no one wants to sign.

### Follow-up report candidates

- **Staff Cars After Midnight**  -  capital witnesses report military vehicles outside offices after hours.
- **Fleets Keep Radio Silence**  -  a naval incident almost becomes public.
- **Border Lamps**  -  lights remain on along a frontier where no government admits anything is happening.

## Evolution stage IV: The Permanent Alert

At Totalen Chaos, tension is no longer a metric. It is the climate. This stage may fire while world tension is already maxed, because the actual effect is no longer the number on the tension bar, it is the diplomatic corrosion and event-pacing pressure that follow.

### Direct effects

- `+100` world tension.
- `+50` chaos.

### Hidden effects

- Apply a severe Tension Pulse with a hard cap and replacement logic so repeated firings do not create an infinite acceleration exploit.
- Apply five to eight relation shocks, with some weighted toward globally meaningful pairs.
- Strong chance of delayed news follow-up.
- Temporary AI strategy should treat the world as “permanent alert”: more hostile posture, more sensitivity to guarantees and rival alliances, higher interest in existing war-preparation decisions, but no forced war.

### Tone

Stage IV is quiet, not explosive. The frightening image is not a battle, it is all the lights staying on in every ministry at once.

## Hidden Tension Pulse system

The Tension Pulse is the event’s most important hidden mechanic. It should temporarily boost automatic event firing pressure, but only by using existing event-timer logic or a small helper called from that logic. It should not add a new daily, weekly, or monthly world loop.

### Design goals

- Make evolved firings feel like they accelerate the campaign.
- Keep the pulse temporary and capped.
- Prevent repeated Stage IV firings from collapsing the timer into an uncontrollable loop.
- Let stronger pulses replace weaker pulses.
- Let equal-stage repeated pulses extend duration only within a capped extension.

### Tension Pulse ladder

| Stage | Working pulse strength | Duration band | Stack behavior |
| --- | ---: | --- | --- |
| I | `+1` pacing pressure | 45–75 days | replaces no pulse, extends weak active pulse modestly |
| II | `+2` pacing pressure | 75–120 days | replaces Stage I, extends equal Stage II within cap |
| III | `+4` pacing pressure | 120–180 days | replaces lower stages, capped extension |
| IV | `+7` pacing pressure | 180–240 days | replaces all lower stages, capped extension, never stacks additively |

The implementation may represent pulse strength as an added decrement, a next-timer compression adjustment, or another existing tuning-compatible pressure value. The spec does not require a new on-action loop. The coding agent must choose the least invasive integration point in the current event timer system.

### Player visibility

The pulse should be partly visible in event details and later reports, not as a raw number. Suggested wording:

> “Higher stages can briefly quicken the rhythm of later incidents as governments, newspapers, and staff offices react to one another.”

## Relation damage system

`Tensions Rising` should not randomly ruin every country’s diplomacy equally. It should choose plausible pairs.

### Pair selection priorities

High priority:

- major powers
- faction leaders
- countries with claims against one another
- countries that border one another
- countries in opposing factions
- ideology rivals
- countries with recent hostile events, guarantees, or diplomatic failures
- countries with large armies or high war support

Low priority or excluded:

- dead or invalid tags
- subject-overlord pairs unless Stage III or IV specifically wants colonial panic
- allies in the same faction at Stage I or II
- special nonhuman or terminal actors unless they are explicitly meant to affect normal diplomacy
- pairs already hit by the same event recently, unless Stage IV deliberately escalates the same rivalry

### Opinion modifier ladder

| Stage | Pairs | Suggested timed opinion hit | Duration direction |
| --- | ---: | ---: | --- |
| I | 1–2 | `-10` to `-15` | 60–120 days |
| II | 2–3 | `-15` to `-25` | 90–180 days |
| III | 3–5 | `-25` to `-40` | 120–240 days |
| IV | 5–8 | `-40` to `-75` | 180–365 days |

The final implementation should use named timed opinion modifiers with localisation that sounds diplomatic, such as:

- `tensions_rising_leaked_cables`
- `tensions_rising_embassy_dispute`
- `tensions_rising_mobilization_suspicion`
- `tensions_rising_border_alarm`
- `tensions_rising_permanent_alert`

## Delayed report and news layer

The delayed layer is where the event earns its personality. These follow-ups should usually have minimal direct gameplay effect. They explain what the hidden pulse and opinion damage feel like.

### Delay timing

- Stage I: 5–15 days, low chance.
- Stage II: 4–12 days, moderate chance.
- Stage III: 3–10 days, high chance.
- Stage IV: 2–8 days, very high chance.

Only one delayed follow-up should be scheduled from a single event firing unless a later stage deliberately creates a rare double headline.

### Follow-up families

| Follow-up | Best stage | Player-facing event type | Gameplay effect |
| --- | --- | --- | --- |
| The Telegram Nobody Signed | I–II | report event | mostly flavour, may identify no named country |
| Embassy Side Doors | I–II | report event | small diplomatic flavour |
| The Calm Map Says Nothing | I+ at 100% WT | report event | explains why the event still matters at max WT |
| Insurance Rates Jump in Neutral Ports | II–III | news/report | can add tiny temporary convoy or trade anxiety only if already supported by existing systems |
| The Rumour That Arrived Twice | II–III | report event | explains duplicate foreign accusations |
| Staff Cars After Midnight | III–IV | report/news | may add temporary AI posture pressure |
| Fleets Keep Radio Silence | III–IV | news | may increase naval-war-adjacent event weights if such hooks exist |
| One Denial Too Many | II–IV | report event | may add an extra relation hit if the same pair is valid |
| Border Lamps | III–IV | report event | points to border rivals without starting war |
| The Last Normal Briefing | IV | report event | one-time Stage IV flavour report |

## Cluster design

Event 8 does not require a cluster. If the `Diplomatic Panic` cluster is kept, treat it as a small catalogue wrapper for the diplomatic-panic identity of the event.

Current cluster: **Diplomatic Panic**

### Current membership

| Member | Role | Member severity | Notes |
| --- | --- | --- | --- |
| Event 8: Tensions Rising | required | medium | for now one member, applies normal Event 8 effects |

### Cluster unlock and chance

- Recommended unlock: Calm World.
- Stage I+ can use a conservative cluster roll if the existing cluster system needs one.
- Cluster cooldown should be moderate to long so the Clusters tab does not become spammed by this event.

## Stage IV presentation

Stage IV should stay within the normal event-log, evolution, option-tooltip, delayed-report, and achievement surfaces. It does not trigger a super-event.

### What it communicates

- The world is not over.
- The world is no longer calm enough to believe its own denials.
- The event remains non-terminal, it increases pressure rather than resolving the campaign.

## Achievement design

The event is a minor repeatable, but it can still support achievements because the evolved hidden mechanics create rare global states. Achievements should reward unusual survival, rare timing, or seeing deep-stage consequences without confusing them with a world-end scenario.

| Achievement key | Title | Visibility | Difficulty | Core unlock idea |
| --- | --- | --- | --- | --- |
| `achievement_tensions_thin_wire` | The Thin Wire | visible | hard | survive 180 days at `100%` world tension after Stage III+ without entering a player war |
| `achievement_tensions_only_headlines` | Only Headlines | hidden | very hard | see three Stage II+ Event 8 firings while the world has no active wars |
| `achievement_tensions_insurance_market` | The Insurance Market Knows | visible | medium | trigger the neutral-port insurance follow-up while owning a convoy pool and staying out of war |
| `achievement_tensions_one_denial` | One Denial Too Many | hidden | hard | have a recently affected Event 8 relation actor enter a war relation within 120 days after Event 8 relation damage |
| `achievement_tensions_blackout` | Diplomatic Blackout | visible | hard | have ten distinct Event 8 timed opinion modifiers active globally at once |

Achievement implementation should be careful. The player should not unlock achievements just because Event 8 fires once.

## AI behavior

The event is global, but AI countries are affected by relation damage, temporary posture weights, and follow-up hooks.

### AI principles

- AI should not declare war solely because Event 8 fired.
- AI can become more willing to use existing war-adjacent or diplomacy-adjacent systems.
- AI should respond more strongly at Stage III and Stage IV.
- AI should avoid impossible or nonsensical actions when the target is dead, allied, unreachable, or protected by a route rule.

### AI stage behavior

| Stage | AI behavior direction |
| --- | --- |
| Baseline | no special AI change beyond normal world tension consequences |
| Stage I | slightly higher interest in guarantees, defensive alignment, and cautious posture |
| Stage II | higher interest in rearmament, guarantees, hostile diplomatic options, and secret-alignment events |
| Stage III | significant temporary war-plan fever, major powers and rivals become more likely to take existing hostile preparation decisions |
| Stage IV | permanent-alert posture, strong but capped pressure toward existing crisis, alliance, and war systems |

## Asset plan summary

The event needs a small but complete asset family.

| Asset | Type | Size | Source mode | Direction |
| --- | --- | --- | --- | --- |
| `report_event_tensions_rising` | report event image | 210x176 | generated staged-documentary, or sourced generic period diplomatic material if available | desks, cables, newspapers, embassy lamps, no readable text |
| `news_event_tensions_red_line` | news image | 397x153 B&W | generated period press image | crowds outside embassy gates, bundled newspapers, police line, no readable text |
| achievement icons | achievements | 64x64 | generated icons | thin wire, blackout embassy, insurance ledger, denial stamp |
| optional event-detail pulse | small animated UI/state accent | existing size/pattern | generated icon frames if UI supports it | subtle telegraph pulse, static fallback required |

No country flags, leader portraits, focus icons, country portraits, or formable seals are required because this event does not create a country or focus tree.

## No focus tree, no country package, no formable

This event must not grow into a country-creation or focus-tree event. Its depth comes from global systems and hidden diplomatic consequences. Creating a new tag here would make the event worse by turning a general pressure mechanic into a specific actor.

If a future design wants a country based on permanent mobilization, diplomatic panic, or world-government collapse, it should be a separate event or major-event branch, not Event 8.

## Event details and log surfaces

Event 8 should appear in:

- random-event history
- event details catalogue
- evolution detail previews
- evolution history when each stage is recorded
- delayed report/news history if those subevents are logged
- cluster history if `Diplomatic Panic` is implemented

The event’s default actor is global. Evolution rows do not need a country actor unless a follow-up report intentionally names a pair. Avoid storing broad global event targets for relation pairs when regular event targets or generic reports are enough.

## Event detail wording direction

Recommended event detail summary:

> “A repeatable global pressure incident. In calm conditions it raises world tension while there is still room for tension to rise. Once the world has entered higher chaos tiers, the same headline can keep firing even at maximum world tension, adding chaos directly and leaving hidden diplomatic aftershocks behind it.”

Recommended evolution detail summary:

> “The Diplomatic Fever track turns public tension into a pacing force. Later stages add direct chaos, larger tension packets, temporary incident-timer pressure, timed relation damage, and delayed diplomatic reports. The final stage is the strongest non-terminal pressure packet.”

## Balance and exploit limits

- Relation damage must be timed.
- Timer pulse must be capped.
- Same-strength pulse must not stack additively.
- Stage IV must not trigger a super-event or world-end branch.
- Delayed reports should not recursively schedule more Event 8 firings.
- The event must not create direct war goals.
- Any temporary AI war-plan pressure must use existing valid route and target checks.

## Open implementation decisions

1. Whether to implement `Diplomatic Panic` immediately or leave it as a small queued note.
2. Whether relation-pair delayed reports should name exact countries or remain generic. Generic is safer and easier to de-duplicate.
3. Whether the timer pulse should modify daily decrement or next timer roll compression. The correct answer depends on the current event timer implementation.
4. Whether the workbook should be updated in the same implementation pass or after localisation is final. The spreadsheet worker should use in-game localisation as source-of-truth.
