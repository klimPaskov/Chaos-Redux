# Event 008: Tensions Rising - Source Specification

Disposition: unresolved source-design acceptance beyond the bounded corrections the parent accepted on 5 and 6 October 2026.
Accepted corrections are recorded in [the owner decisions](../../../plans/008_tensions_rising_plans/agent_decisions_2026-10-05.md), the [balance decisions](../../../plans/008_tensions_rising_plans/balance_evidence_2026-10-06/owner_balance_decisions.md), and [the owner state map](../../../plans/008_tensions_rising_plans/documentation_state_2026-10-05.md); this spec describes them as current design.
`docs/events/008_tensions_rising/overview.md` is the implementation-facing record; the catalog status is `Needs Testing`.
Design not yet accepted lives only in the README's open questions.

## Event identity

| Field | Value |
| --- | --- |
| Event ID | `8` |
| Event name | `Tensions Rising` |
| Type | Minor Repeatable |
| Implementation | implemented in source; runtime, GUI, and probability validation incomplete |
| Cluster | unresolved; see Cluster design |
| World-end scenario | none |

`Tensions Rising` is the small headline that makes the rest of the world feel less stable.
It does not release a country, start a focus tree, create a formable, or end the world.
It is a pressure event that makes the ordinary Chaos Redux timer and diplomatic memory feel alive: early it nudges world tension upward, and later it becomes a ritual of public denials, secret cables, mobilization scares, poisoned relations, insurance spikes, and exhausted general staffs.

The user's original brief set the core:

- In Calm World, the event raises world tension and fires only while world tension is below full.
- Once the first evolution is active, the event can fire even when world tension is already full.
- Later evolutions add direct chaos, larger world-tension packets, temporary timer pressure, relation damage, delayed follow-up incidents, and rare safe high-stage border clashes.
- The event never has a world-end scenario.

The brief's packet sizes (`+100` to `+1000` requested threat) were replaced on 6 October 2026 by the accepted 2/3/5/8/12 ladder under the user's G4/G6 balance direction, because the original baseline alone pushed a 1936 world to 99 percent tension; vanilla Rhineland adds 5.

The emotional center is every government acting as if a map is about to change.

## Player-facing fantasy

The player should see `Tensions Rising` as an apparently simple repeatable event that becomes increasingly uncomfortable.
At first it is a straightforward tension bump.
Later, the same headline starts leaving fingerprints: embassies close side doors, neutral shipping gets nervous, opposition newspapers claim secret mobilization, staff cars move after midnight, and old allies start filing formal complaints.

The event is about the world preparing to make mistakes.
It pushes the campaign toward volatility without replacing the existing war, alliance, and major-event systems.

## Visible values

The report shows only two numbers: the world tension and the overall Chaos actually changed by the shocks in its batch, with one decimal and a colour-free decrease branch when net Chaos falls.
It does not show requested packets, pulse strength, pair counts, opinion values, posture ideas, or follow-up odds.
Relation damage is visible in the diplomacy view through named opinion modifiers, and follow-ups are visible as their own reports.
No other player-facing value or meter is part of this event.

## Baseline Calm World incident

The baseline report follows a specific disturbance in ordinary life, such as patrols lingering along a disputed frontier, crews refusing a familiar route, or travellers repeating the same accusation in several ports.
Keep the cause uncertain and let concrete behaviour carry the unease; finished wording lives in localisation.

| Stage | World state | Fire condition | Direct effects | Hidden side effects |
| --- | --- | --- | --- | --- |
| Baseline | Calm World or the current stage's evolution disabled | world tension below full | requested `+2` world tension | none beyond normal Minor Repeatable consequences |

The baseline is the first crack in the glass: no relation damage and no direct chaos.
Player text mentions public uncertainty and the rise in tension, never hidden systems, weights, evolutions, or timer manipulation.

## Evolved identity

`Tensions Rising` has one evolution track: **Diplomatic Fever**.
Each stage changes how future firings behave; it does not require the event to fire when the Chaos tier changes.

| Stage | Title | Chaos tier | Requested world tension | Chaos | Fires at full tension | Hidden layer |
| --- | --- | --- | --- | --- | --- | --- |
| I | Cable Traffic Flood | Gathering Storm | `+3` | `+10` | yes | light pulse, one or two relation shocks, cautious AI posture, possible follow-up |
| II | The Accusation Market | Rising Chaos | `+5` | `+15` | yes | stronger pulse, two or three shocks, rearmament posture ideas |
| III | General Staffs Stop Sleeping | Chaos Tier | `+8` | `+25` | yes | heavy pulse, three to five shocks, near-miss follow-ups, rare border clashes |
| IV | The Permanent Alert | Total Chaos and above | `+12` | `+50` | yes | severe capped pulse, five to eight shocks, strongest follow-ups and clash odds |

Stage titles are working design names; the in-game evolution titles are listed in the [log and localisation direction](008_tensions_rising_event_log_and_localisation.md).
A stage applies only while the current Chaos tier reaches it and that stage's evolution checkbox is enabled; a disabled stage falls back to the baseline packet.
The evolution is recorded the first time a stage's packet applies.
Event details preview each stage in broad terms without the random headline list or pair-selection math.

Requested world tension is distributed as named threat across eligible existing countries: each receives an equal slice no smaller than `tensions_rising_world_tension_gain.minimum_country_slice`, so a packet reaches at most packet/0.1 sources.
An automatic shock starts a 30-day global cadence (`tensions_rising_reporting.automatic_cooldown_days`); manual forces bypass it but still refresh it.

### Stage tone

- Stage I is wires, clerks, desk lamps, and official denials; no country has crossed the line yet.
- Stage II is louder and more cynical: rumour becomes a commodity for newspapers, ministries, arms firms, and foreign sponsors.
- Stage III reads like fatigue in the armed services; it tilts AI and events toward conflict without creating free wars.
- Stage IV is quiet and sustained: every ministry keeps its lights on through the night, and the corrosion matters more than the tension bar.

## Hidden Tension Pulse

The pulse temporarily raises automatic event pressure through the existing timer: `calculate_next_timer_value` calls `apply_tensions_rising_timer_pressure_to_next_timer`, with no new daily, weekly, or monthly loop.

| Stage | Pulse strength | Duration band | Equal-stage extension | Cap |
| --- | ---: | --- | --- | --- |
| I | 1 | 45-75 days | 30 days | 105 days |
| II | 2 | 75-120 days | 45 days | 165 days |
| III | 4 | 120-180 days | 60 days | 240 days |
| IV | 7 | 180-240 days | 75 days | 315 days |

A stronger pulse replaces a weaker one; an equal-stage repeat converts the exact remaining time to days, extends it, and clamps to the cap; a weaker pulse never lowers an active one.
Values live in `tensions_rising_timer_pulse`.
Reports may convey an accelerating succession of disturbances, but no surface shows the timer formula or forecasts another event by name.

## Relation damage

`Tensions Rising` damages plausible rivals rather than everyone equally.
`select_tensions_rising_relation_pairs` prefers majors and faction leaders, and filters capitulated countries, subjects, special chaos countries, and direct war opponents; same-faction pairs are excluded at Stages I-II only.
Primary selection avoids actors hit within the 150-day selector cooldown; the fallback passes that bypass it are a known limitation with a proposal in the README.

| Stage | Pairs | Opinion modifier | Value | Duration |
| --- | ---: | --- | ---: | --- |
| I | 1-2 | `tensions_rising_leaked_cables` | -15 | 120 days |
| II | 2-3 | `tensions_rising_mobilization_suspicion` | -25 | 180 days |
| III | 3-5 | `tensions_rising_border_alarm` | -40 | 240 days |
| IV | 5-8 | `tensions_rising_permanent_alert` | -75 | 360 days |

Incidents also use `tensions_rising_embassy_dispute` (-20).
Each directed stage-and-partner modifier is counted once through a partner-keyed timed flag, and `chaosx.nr8.21` removes the count when it expires.
Every selected pair refreshes both actors' 120-day One Denial eligibility.

## Root reports and delayed incidents

The accepted report-batching tranche (6 October 2026) governs presentation.
Hidden roots `chaosx.nr8.1` accumulate their actual world-tension and Chaos changes into one visible `chaosx.nr8.16` report per recipient.
The first effectful root supplies the batch's stage context, including when an earlier root contributed no effects.
Acknowledgement clears the batch and never applies its packets again.

A batch can schedule at most one delayed incident from its first effectful evolved root; later roots in the same batch add effects without more follow-up invitations.
A later independent batch has its own opportunity.

### Aftershock scale

An incident is a smaller, distinct aftershock with a real consequence, never a second root packet.
Its world-tension packet must stay below the root packet of the stage that scheduled it, so the 6 October ladder cannot be bypassed through follow-ups.
The current `tensions_rising_incident_world_tension` values (25 to 75) predate that ladder and exceed even the Stage IV root (12); they must be rescaled in source, which is listed as remaining work in the coding prompt.
Incident Chaos (2 to 10) already stays below the root Chaos packets.

### Delivery and delay

Delay bands are 5-15 days at Stage I, 4-12 at Stage II, 3-10 at Stage III, and 2-8 at Stage IV, with follow-up chances of 30/50/75/90 percent.
Their tuning still needs the owner's named probability scenarios before numerical acceptance.

At delivery, an incident uses the currently enabled evolved stage.
An evolution disabled during the delay cannot return through an internal Stage I fallback, and a terminal campaign state closes the queued incident.
Frozen root-report totals remain a record of what already happened.

For a border clash, recheck both countries, adjacent owned-and-controlled states, peace, independence, faction separation, existing border conflict, and the global and actor cooldowns immediately before starting combat.
A failed pair search leaves only the incident's other effects; it cannot become a war goal, territory transfer, substitute normal declaration, or new Event 008 firing.

### Incident families

| Event | Incident | Distinct consequence |
| --- | --- | --- |
| `.2` | The Telegram Nobody Signed | light tension and diplomatic aftershock |
| `.3` | Embassy Side Doors | diplomatic friction and a temporary AI posture response |
| `.4` | Unease Along the Frontier | continuing pressure when the tension bar is already full |
| `.5` | Insurance Rates Jump in Neutral Ports | shipping pressure and the Insurance Market achievement hook |
| `.6` | The Rumour That Arrived Twice | two distinct diplomatic accusations |
| `.7` | Staff Cars After Midnight | temporary preparation pressure around eligible AI majors |
| `.8` | Fleets Keep Radio Silence | maritime preparation and diplomatic friction |
| `.9` | Border Lamps | heavier diplomatic damage and a Stage III+ safe non-transfer clash attempt |
| `.10` | One Denial Too Many | heavier diplomatic damage and a Stage III+ clash attempt |
| `.12` | The Last Normal Briefing | the strongest bounded aftershock on its first Stage IV occasion |

`.11` is deliberately unused, `.13`-`.15` resolve clash outcomes, `.20` is the Thin Wire watch, and `.21` is the opinion expiry.
There is no Event 008 news event; the retained red-line news image has no consumer.

## Connections to other systems

| System | Connection |
| --- | --- |
| Chaos Meter | Evolved roots and incidents add Chaos through `add_chaos_meter_value` under the Tensions Rising history reason; world tension also feeds the shared derived Chaos update. |
| Event timer | The pulse compresses the next automatic timer roll. |
| Event 011 Secret Alliance | See below. |
| Event 017 Random Faction | Shares the current source cluster; see Cluster design. |

Border clashes are not war relations and capture no states, so they add no war-declaration Chaos and no capture-driven migration pressure; this keeps them contained.
Famine, migration, camps, CBRN, fallout, and condemnation have no natural Event 008 connection, and none should be invented.

### Connection to Secret Alliance

When Event 011 is active, an Event 008 opinion shock involving its fixed target and a candidate or member can influence that country's ordinary diplomatic context.
Event 008 owns the timed shock and its pressure receipt.
Event 011 owns recruitment, motive evaluation, operation evidence, and reveal.
A repeated rumour or global pulse alone supplies no pact clue, confirmed suspect, readiness grant, or extra Chaos packet.
A non-transfer border clash remains outside the hostile normal-war reveal rule.
If a later normal war involves an active member and the fixed target, Event 011 applies its existing immediate reveal contract.

Future checks must distinguish a shared rumour without an Event 011 dossier, an independently corroborated Event 011 operation during panic, a border clash, and a normal hostile war.
Ordinary Event 008 play remains unchanged when the alliance is absent.

## Cluster design

Event 8 does not require a cluster, and its cluster record is unresolved.

| Record | Identity | Members | Severity |
| --- | --- | --- | --- |
| Current source (`event_cluster_constants.txt`, `chaosx_event_cluster_effects.txt`) | ID 3 `Diplomatic Panic`, repeatable, unlock tier 0, 120-day cooldown | Event 8 required, Event 17 optional | Low, Low |
| Workbook catalog | ID 3 `Diplomacy`, `Partially Available` | Events 8, 17, 36, 59 | Medium, Medium, High, High |

The cluster owner must choose one record and supply its acceptance basis; this spec selects neither.
A proposal on severity is in the README.

## Stage IV presentation

Stage IV stays within the normal report, event-log, evolution, option-tooltip, delayed-incident, and achievement surfaces.
It does not trigger a super-event; the world is not over, only no longer calm enough to believe its own denials.

## Achievements

Achievements reward unusual survival, rare timing, or deep-stage consequences, never seeing the popup once.

| Achievement key | Title | Visibility | Difficulty | Core unlock idea |
| --- | --- | --- | --- | --- |
| `achievement_tensions_thin_wire` | The Thin Wire | visible | hard | stay at peace for 180 days at full world tension after Stage III+ |
| `achievement_tensions_only_headlines` | Only Headlines | hidden | very hard | receive three report batches first shown at Stage II+ while the world has no active wars |
| `achievement_tensions_insurance_market` | The Insurance Market Knows | visible | medium | receive the insurance follow-up while at peace with at least 30 convoys |
| `achievement_tensions_one_denial` | One Denial Too Many | hidden | hard | a country with its own 120-day relation-damage eligibility enters a war relation |
| `achievement_tensions_blackout` | Diplomatic Blackout | visible | hard | ten distinct Event 8 timed opinion modifiers active at once |

Details and tracking limits are in the [cluster and achievement matrix](../matrices/008_tensions_rising_cluster_and_achievements.md).

## AI behavior

- AI never declares a normal war because Event 8 fired.
- Every evolved root applies a short hidden posture idea, one per stage, to a stage-scaled number of AI majors, faction leaders, or countries at war: `tensions_rising_cautious_alignment`, `tensions_rising_alarmist_rearmament`, `tensions_rising_general_staff_fever`, and `tensions_rising_permanent_alert`.
- Those ideas raise alliance desire, cheapen guarantees, and at higher stages add war support, arms production, and planning at a stability cost.
- AI avoids impossible or nonsensical actions when a target is dead, allied, unreachable, or protected by a route rule.

The [AI matrix](../matrices/008_tensions_rising_ai_matrix.md) lists the stage behavior.

## Assets

| Asset | Status |
| --- | --- |
| `GFX_report_event_tensions_rising` (210x176) | wired on `.1`/`.16` and the incidents |
| `GFX_news_event_tensions_red_line` (397x153 B&W) | registered, cropped on 6 October, no consumer |
| fifteen achievement DDS files (64x64 triplets) | wired |
| optional animated event-detail pulse | not needed; no accepted UI surface |

Source provenance for these assets is unresolved because the historical archive was deleted; see the asset prompt.
No country flags, leader portraits, focus icons, or formable seals are required.

## No focus tree, no country package, no formable

This event must not grow into a country-creation or focus-tree event.
Its depth comes from global systems and hidden diplomatic consequences.
A future design for permanent mobilization or world-government collapse belongs to a separate event, not Event 8.

## Event details and log surfaces

Event 8 appears in random-event history, the event details catalogue, evolution previews, evolution history per recorded stage, and cluster history.
Its default actor is global, and evolution rows need no country actor.
Detail text describes the situation and premise, not timer values, penalties, or achievement routes; the final keys are listed in the [log and localisation direction](008_tensions_rising_event_log_and_localisation.md).

## Balance and exploit limits

- Relation damage is timed and counted once per directed stage-and-partner modifier.
- The timer pulse is capped and never stacks additively.
- Automatic shocks respect the 30-day cadence.
- Incident packets stay below their stage's root packet.
- Stage IV triggers no super-event or world-end branch.
- Delayed reports never schedule further Event 8 firings.
- The event creates no war goals, cores, claims, or free units.
- High-stage incidents start non-transfer border clashes only through safe adjacent-pair checks and cooldowns.
- Temporary AI pressure uses existing valid route and target checks.

## Resolved implementation decisions

1. Follow-up incidents remain generic reports rather than naming exact pairs.
2. The pulse compresses the next timer roll inside `calculate_next_timer_value`.
3. Workbook wording follows final localisation and is queued in `docs/plans/008_tensions_rising_plans/catalog_changes_pending.md`.
4. The cluster record remains unresolved with the cluster owner.
