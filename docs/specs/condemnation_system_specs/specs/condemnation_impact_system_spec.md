# Condemnation Impact System Spec

## Status and authority

| Layer | Basis | State |
| --- | --- | --- |
| 0–1000 Condemnation range, cost multiplier `m = 1 + Condemnation / 500` rounded up to whole equipment, and a 5–15% Consumer Goods inspection burden for 180 days | Explicit user request, 2026-09-20 | Accepted and implemented |
| Tiers, source buckets, native embargo, participant scoring, target and participant responses, decay, cleanup | Source design below | Implemented; current behaviour and every tuning value live in the [implemented system document](../../../systems/cbrn_warfare/condemnation/condemnation_sanctions.md) |
| Response consolidation, reduced player-facing read model, famine relief link, repeat use folded into its source | 10 Oct 2026 spec audit under the user's planning-package brief | Accepted and queued for implementation |

The 2026-09-20 amendment controls any conflicting older tuning.
Where this spec and the implementation differ outside the queued refinements, the implemented document names actual behaviour and this spec names intent.
Numeric values in this spec are design anchors; final values belong in `common/script_constants/condemnation_sanctions_constants.txt`.

## Purpose

Condemnation is the shared consequence layer for publicly known unconventional warfare and exposed atrocities.
A high score must change play through trade, arms access, fuel, aid, volunteers, licences, research sharing and faction trust, not mainly through opinion.
The bargain must be legible: a country may keep using chemical, biological or nuclear weapons, or keep extermination infrastructure running, and then it lives with isolation, smuggling risk and costly compliance.

## Design rules

1. Practical consequences come first; opinion modifiers only support them.
2. Use the engine's native embargo where it exists, and never present a scripted modifier as a native embargo.
3. Sources stay distinct: battlefield chemicals, biological spread, nuclear devastation, exposed atrocities and cover-ups provoke different reactions.
4. Tiers unlock mechanics; they are not static modifier labels.
5. Recovery requires time, non-use and credible action; compliance never erases severe condemnation in one click.
6. Penalties scale with who actually sanctions and how import-dependent the target is; a minor with two participants and a major facing most of the world never receive the same modifier.
7. Every tuning value lives in script constants.
8. No broad all-country pulse: use weapon-use hooks, discovery hooks, diplomatic hooks, decision completion and the targeted per-country pulse.
9. Every sanction has cleanup for dead tags, annexation, subject changes, faction changes and expiry.
10. Readability over completeness: few distinct choices with felt costs, and a read model limited to values that drive decisions.

## Sources

One shared helper, `condemnation_add_source`, receives source type, base gain, visibility, severity, optional deaths, contamination, victim and context.
No caller scatters its own magic values.

| Bucket | Fed by | Scales with | Never fed by |
| --- | --- | --- | --- |
| Chemical | Chemical combat abilities and support, chemical air strikes and raids, public contamination, chemical doomsday release | Affected population, civilian exposure, persistence, foreign or occupied territory, contamination, the accepted doctrine multiplier | Research, production or stockpile ownership |
| Biological | Deliberate strikes, outbreak weapons, deliberate spread, exposed accidents, weaponized zombies, biological doomsday release | Outbreak spread, deaths, density, visibility, containment failure | A natural or unattributed outbreak suffered by the current controller |
| Nuclear | Nuclear, thermonuclear and Final Silence strikes | Population, capital and industrial targets, fallout deaths, victim status, first use | Nothing exempts a strike; no country pair is excused |
| Atrocity | Discovered camps, extermination sites, gulags, experiment sites, restricted chemical sites | Site type, deaths, evidence quality, discovery context | Hidden operation; hidden evidence accumulates until occupation, liberation, inspection or observers expose it |
| Cover-up | Destroyed records found later, refused inspection, exposed evasion, broken pledges, concealed famine deaths | Severity of the original act, whether compliance had been promised | Lawful compliance |

Repeated use is not a separate public bucket in the refined design.
A repeated public use within the recent-use window multiplies the new gain inside its own source bucket, so the player reads "nuclear" rather than an abstract repeat line.
Breaking a pledge adds cover-up as today.

Biological blame follows the source owner's deliberate-use or exposed-accident evidence and stored responsible actor.
Later attribution publishes only the unpaid part of an existing episode, as defined in the [CBRN attribution model](../../chaos_warfare_system_specs/specs/09_condemnation_deaths_air_cleanliness_and_diplomacy.md#attribution-model).
Containment reduces future growth and improves decay; it never erases recorded gain, evidence or deaths.

## Tiers

| Tier | Name | Threshold | What changes |
| --- | --- | ---: | --- |
| 0 | Normal standing | 0 | Nothing beyond the source record |
| 1 | International concern | 25 | Watching countries lose interest in lend-lease, volunteers and military access; compliance responses appear |
| 2 | Formal censure | 50 | Stronger diplomatic refusal; participants can abstain or shield; the full response list opens |
| 3 | Arms embargo | 100 | Participants may create native embargo pairs, block new lend-lease, volunteers, attachés and cheap licences; arms import bottleneck |
| 4 | Strategic embargo | 175 | Import-sensitive factory, dockyard and fuel shortage; participants stop serving as food-import donors without a carve-out |
| 5 | Total embargo | 300 | Isolation economy, research-sharing damage, faction strain, visible abstainers and profiteers |
| 6 | Pariah state | 500 | Rival intelligence and resistance support, stability pressure, contain or antagonise AI strategies |

Tier alone creates no sanction pair; a participant must pass pair validity and scoring, or take the matching decision.
The peak tier is permanent memory that keeps participants sceptical after the score falls.

## Native embargo

The engine's diplomatic embargo requires By Blood Alone and is broad: it cannot express an arms-only or oil-only denial.
Condemnation therefore uses the native embargo from Tier 3 participants as its trade-denial core and adds scripted restrictions for arms support, licences, research sharing and shortages.
Condemnation releases only its own embargo claim; other owners such as the Air Cleanliness Treaty and Event 050 keep theirs.
Already active lend-lease, licences and research-sharing membership cannot be revoked by script; new grants are gated and breaches are detected.

## Participants

Every potential participant receives a score against the target.

- Pressure to sanction rises with tier, peak tier, recent gain, nuclear, biological, atrocity and cover-up weight, contamination and civilian deaths, democratic or rival ideology, direct victim status, war with the target, proximity, world tension, faction leadership and exposed evasion.
- Pressure falls with shared faction, subject relations, shared ideology or war, weak economy, distance, the participant's own condemnation, trade and strategic-resource dependency, sanction fatigue and the target's compliance progress.

Result bands map the score to behaviour: watch, abstain, join arms, strategic, total or pariah enforcement, tighten after evasion, withdraw under fatigue, shield an invalid partner, or quietly breach under heavy dependency.
Joining costs convoys and fuel; enforcement burden and fatigue then cost the participant consumer goods, factory output, fuel and eventually stability, so no country cuts a major partner for free.

## Target responses

The refined response set has twelve decisions instead of twenty-five.
Each survivor has a distinct cost and a distinct consequence; merged routes keep their strongest mechanical effect.

### Compliance

| Response | Cost | Result |
| --- | --- | --- |
| Admit inspectors (merges inspections and observers) | The accepted 5–15% Consumer Goods for 180 days, encryption loss, convoys scaled by `m` | Decay bonus and monthly disclosure of hidden evidence; refusing later becomes a cover-up |
| Destroy stockpiles (merges chemical and biological) | Removes 75% of every condemned stock the country holds and restricts use of each destroyed family for 365 days | Decay bonus per family destroyed; breaking the restriction is a pledge breach |
| Dismantle restricted sites | Loss of site output, closure of controlled restricted and experiment sites | Decay bonus and atrocity pressure stops growing |
| Pay compensation | Convoys, equipment and fuel scaled by tier and `m`, then a temporary economic burden | Delivered to the last valid victim, improves that victim's opinion, decay bonus |
| Non-use pledge | War support loss for 365 days | Completion grants verified non-use; any condemned use during it is a pledge breach |
| Reform the command | Army, air and navy experience scaled by `m`, temporary organisation and training penalty | Permanent memory that lowers participant scepticism |

### Defiance

| Response | Cost | Result |
| --- | --- | --- |
| Refuse inspections | Cover-up gain and frozen decay for 180 days | Blocks disclosure of hidden evidence |
| Rally the nation (merges propaganda and hardline mobilisation) | Stability loss and consumer goods | War support; participants' moral pressure rises |
| Sanctions war economy (merges autarky, forced extraction, substitute materials and military rationing) | Fuel, stability and production efficiency | Local resources and fuel economy; the largest severity relief among defiance routes |
| Lean on subjects | Requires a subject; stability loss | Local resources and severity relief through subject supply |

### Evasion

| Response | Cost | Result |
| --- | --- | --- |
| Smuggle arms (merges black-market arms and stolen licences) | Convoys and fuel scaled by `m` | Equipment delivery and licence relief; highest exposure |
| Covert fuel route | Convoys scaled by `m` | Fuel delivery and fuel-consumption relief |
| Front companies (merges neutral intermediaries, subject fronts, false manifests, reflagging and laboratory smuggling) | Convoys scaled by `m` | Severity relief, convoy escort efficiency and modest research relief |

Every evasion route adds exposure; exposure decays monthly and drives a detection roll.
Detection adds cover-up condemnation, cancels the route and makes enforcers tighten.

## Participant actions

| Action | Use case | Cost or risk |
| --- | --- | --- |
| Join arms embargo | Target at Tier 3 and score high enough | Convoys and fuel, continuing enforcement burden |
| Escalate to strategic, total or pariah | Existing pair and sufficient tier | Smaller convoy and fuel payment, higher continuing burden |
| Abstain | Dependency, ally, weak economy | Opinion loss with the victim and active enforcers |
| Humanitarian carve-out | Permit named defensive relief and food imports while keeping offensive trade restricted | Convoys for 180 days; relief from this participant counts as delivered, and any CBRN shipment keeps its own owner's payment and access rules |
| Quiet breach | Heavy dependency or profit | Convoys, fuel and equipment; exposure adds cover-up to both countries |
| Tighten enforcement | Exposed evasion | Convoys; ends breaches and cuts target relief |
| Shield ally | Same faction or subject | Convoys, fatigue, opinion cost with enforcers |
| Withdraw | Fatigue or decay | Releases only the condemnation embargo claim |

AI participants act through the score-driven recalculation; participant decisions are player controls.

## Decay and memory

Public buckets decay monthly by tier, slowest at Pariah, and each active compliance response adds a decay bonus.
Recent use, refused inspections, broken pledges and exposed evasion freeze decay.
Hidden evidence never decays.
Peak tier remains permanently and adds participant pressure; a verified government change or command reform lowers memory gradually, never instantly.

## Player-facing read model

The previous read model exposed more than twenty values in the detail panel, including participant fatigue, industry and trade estimates, vulnerability indices, isolation severity, carve-out, breach and shield counts, and six bucket totals.
Those values drive the simulation and AI, but they do not change a player's next decision, so the refined panel shows only what does.

Country row: flag and name, total, tier, main source, number of countries sanctioning.

Detail panel:

1. Total and tier, with the next threshold or "Pariah" at the cap.
2. Why: the main two sources by share and the newest public incident with its date.
3. Who: the countries sanctioning, by tier, and up to three named enforcers; abstainers and shields appear as one line ("2 abstaining, 1 shielding").
4. What it costs now: one combined line of the current practical penalties.
5. What eases it: active compliance responses and whether decay is running or frozen, in words.
6. Smuggling risk, shown to the target only while an evasion route is active, as Low, Elevated or High.

Participant fatigue, dependency estimates, vulnerability, isolation severity and hidden evidence remain internal.
The full dated source history stays available in the incident tooltip.
Tooltips explain blocked responses and their costs with scripted localisation, never raw trigger lists.

## AI behaviour

AI uses the same visible logic as the player.

| Actor | Behaviour |
| --- | --- |
| Weak condemned target | Admits inspectors, destroys stockpiles, pays compensation and pledges when sanctions hurt |
| Strong condemned target | Rallies the nation, runs a sanctions war economy, leans on subjects and smuggles while it can absorb the cost |
| Target near capitulation | Destroys stockpiles unless an explicit doomsday authorisation exists |
| Democracy | Sanctions strongly after civilian deaths, nuclear use, biological spread or exposed atrocities |
| Fascist or communist power | Sanctions rivals, shields aligned offenders |
| Neutral trader | Abstains under dependency, breaches quietly when exposure risk is low |
| Faction leader | Coordinates sanctions, shields members, pressures members to comply at high tiers |
| Subject | Follows its overlord unless autonomy is high or it was the victim |
| Condemned participant | Hypocrisy penalty unless rivalry, fear or direct harm overrides it |

## Integration

- **Chaos Meter.** Condemnation never adds a second Chaos spike for an act that the weapon, death, contamination or atrocity system already counts; sanctions affect Chaos only indirectly through wars, tension and crises.
- **Deaths.** Recorded civilian deaths scale chemical, biological, nuclear and atrocity gains; condemnation never runs its own mortality.
- **Air cleanliness.** Contamination raises participant pressure, and the source line names contamination when it contributed.
- **Famine.** Famine owns food security and mortality. Deliberate relief obstruction, rejected evacuation corridors and concealed famine deaths are condemned through the famine owner's existing calls. At Tier 4 and above, an enforcing participant stops serving as a donor for the target's Import Food action unless that pair has a humanitarian carve-out, so sanctions bite on food only where a carve-out is refused, and the carve-out has a visible humanitarian purpose.
- **Biological warfare and Event 020.** The biological lifecycle owns disease, deaths and contamination; [Event 020](../../020_black_plague_specs/specs/020_black_plague_spec_part_3_cure_spread_and_biowarfare.md#biological-warfare-registration) owns Black Plague identity and countermeasures. Compliance or humanitarian access never grants samples, cures or another event's progression.
- **Camps and genocide.** Discovery, leaks, occupation, liberation, observers and exposed records feed atrocity and cover-up; hidden operation stays hidden until evidence exists.
- **Chaos Warfare doctrine.** The [accepted CBRN doctrine boundary](../../chaos_warfare_system_specs/specs/09_condemnation_deaths_air_cleanliness_and_diplomacy.md#doctrine-mitigation-rule) permits a bounded reduction of Condemnation impact with public-harm floors; it never reduces evidence, attribution, deaths, contamination or responsibility.

## Cleanup

Pair validity triggers and shared helpers clear sanctions when the target or participant dies, merges, becomes the other's subject, joins the other's faction, falls below the pair tier, settles, or expires, and when breaches, carve-outs or modifiers outlive their pair.
Merged responses must migrate active legacy timers and flags so a running inspection, pledge or evasion route keeps its remaining duration.

## Balance principles

- Tiers 1 and 2 warn; Tier 3 restricts military support; Tier 4 changes resource strategy; Tier 5 forces an economic and diplomatic response; Tier 6 makes the target dangerous to support.
- A self-sufficient major suffers less from trade denial and more from diplomatic pressure; a resource-dependent minor fears strategic embargo but has compliance paths.
- A shielded target survives longer while the shield pays.
- Evasion helps, then becomes risky if overused.
- Compliance is slower than damage, because trust takes time to rebuild.

## Validation scenarios

1. Chemical combat use in several battles, then non-use and decay.
2. One nuclear strike on a low-population military target versus a thermonuclear strike on a populous capital.
3. A biological strike that spreads; a natural outbreak that condemns nobody; later attribution that charges only the unpaid part.
4. A restricted chemical site or camp exposed by occupation or liberation.
5. Tier 3 creates native embargo pairs from eligible participants; Tier 4 shortage scales by participant weight and import dependency.
6. Tier 5 with strong faction shielding versus none with high trade dependency.
7. A neutral trader abstains under dependency, breaches, is exposed and is tightened against.
8. A target admits inspectors and destroys stockpiles; another breaks a non-use pledge.
9. Repeated smuggling raises exposure until detection.
10. A participant withdraws after decay or fatigue; an annexed target leaves no stale pairs or embargo claims.
11. Weak AI targets comply and strong AI targets defy.
12. The detail panel shows only the six refined elements and explains blocked responses without raw triggers.
13. A Tier 4 target in famine cannot import food from an enforcing participant until that participant grants a carve-out.
14. A save with legacy inspection, observer, autarky or evasion timers running keeps their remaining effects after the response consolidation.

## Open questions

- Whether the merged Front companies route should keep laboratory smuggling's research relief or drop it, since research relief is the least felt sanction effect.
- Whether participant decisions should remain player controls for every participant or appear only after the player's country scores as a likely participant.

## Revision log

### 2026-10-10 spec audit

- Replaced the pre-implementation data-model, implementation-surface, documentation and completion-report sections with a status table and a link to the implemented system document, which now owns variables, tuning and evidence.
- Consolidated target responses from twenty-five to twelve (inspections with observers, chemical with biological stockpiles, four economic defiance programmes into one, propaganda with hardline mobilisation, eight evasion routes into three); accepted and queued.
- Reduced the player-facing detail panel to six elements and moved fatigue, dependency, vulnerability and severity values to internal use; accepted and queued.
- Folded repeat use into the repeated source's bucket instead of a separate public line; accepted and queued.
- Linked sanctions to famine relief: enforcing participants at Tier 4+ refuse Import Food donation without a humanitarian carve-out; accepted and queued.
- Condensed source, tier, participant, AI and cleanup sections to one canonical statement each; removed the colour-palette and asset-request lists already satisfied by reused icons.
