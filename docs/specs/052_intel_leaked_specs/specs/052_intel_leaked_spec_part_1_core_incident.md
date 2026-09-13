# Event 052 Intel Leaked

## Catalog identity

- Event ID: `52`
- Event name: Intel Leaked
- Type: Minor Repeatable
- Status before implementation: To Be Reworked
- Chaos level: 1
- Cluster: Intelligence
- Member severity: Low

## Event promise

Intel Leaked creates a temporary period in which one government's secrets become common strategic property.

The crisis should feel broad without becoming a second intelligence game layered over the whole campaign. The player should understand that foreign governments know too much, that the usefulness of the stolen archive is falling, and that decisive action can shorten the danger. The player should also see that some foreign governments are using the material more aggressively than others.

The event's identity comes from four connected pressures:

1. The archive exposes several kinds of information at once.
2. Every ordinary foreign government receives a temporary advantage against the target.
3. A bounded group of interested governments extracts unusually useful material and acts on it.
4. The target can reduce the damage, accept sacrifices, or feed false information into the same channels.

The event never establishes a final cause for the breach. Investigations can identify a practical route, such as a courier chain or cryptologic weakness, but several facts remain contradictory. This uncertainty is part of the incident's identity and prevents the repeatable event from resolving into one permanent villain.

## Player experience

The opening report tells the target that a large classified archive has appeared across foreign ministries, military commands, embassies, intelligence offices, and diplomatic channels. The target knows the broad classes of compromised material but does not know which government received which file, how complete each copy is, or whether every copy is identical.

The target immediately receives the Intelligence Compromise decision category. This is a working label. The category shows one persistent value, Exposure, and a small set of current actions. Emergency responses dominate the opening. Reconstruction becomes available after the immediate danger falls. Deception becomes available when the target has established enough control to risk feeding more material into the leak.

Foreign countries receive a public or private report based on their relationship with the target and the part of the archive they can use. Most foreign governments simply gain the broad intelligence advantage. A bounded set becomes a named exploiter and can generate follow-up consequences.

The incident ends when Exposure reaches zero or when the remaining archive becomes operationally useless at the end of its dynamic life. Temporary intelligence advantages, incident decisions, missions, risk records, deception states, and exploit records then clear. Real results remain, including captured operatives, cancelled operations, lost network strength, reorganized services, hardened procedures, diplomatic damage, and wars affected by the information.

## Baseline target selection

An ordinary baseline firing compromises exactly one country.

The event first evaluates two target routes:

- the current player-controlled country associated with the firing context
- a random valid major power

The ordinary balance anchor is an even choice between the two routes when both routes have a valid candidate. The final implementation can use a dynamic weighted model if the probability audit shows that the player route becomes starved or overselected in common campaign states. The one-target rule remains fixed.

The player route uses the current valid player-controlled country. It does not search all human players and then select a different human country. In multiplayer, the player whose event context owns the firing is the player-route candidate. The major route can still select another human-controlled country when that country is also a valid major and the established multiplayer event framework permits that result.

If one route has no valid candidate, the other valid route is used. If neither route has a valid candidate, Event 52 is unavailable and should not enter selection or manual normal firing.

A valid target must:

- exist and control meaningful territory
- participate in ordinary military, political, industrial, diplomatic, and intelligence systems
- have a valid country scope for temporary modifiers and decisions
- be outside the shared special Chaos-country exclusion where ordinary intelligence exposure would make no sense
- be outside the actual nonhuman classifier
- have no unresolved Event 52 incident already active
- be able to receive and later clear every event-owned incident state

The shared `is_special_chaos_country`, `is_actual_nonhuman_country`, and `uses_normal_civilian_systems` classifiers should guide target treatment. Event-owned validity remains in Event 52's own trigger surface. The event should not expand the shared classifier with incident stage or lifecycle checks.

A country can be selected again by a later repeat firing. There is no permanent target immunity.

## Incident creation

Each firing creates one sequence with its own identity.

The sequence owns:

- target country or target countries
- incident start date
- initial Exposure
- archive domain set
- archive depth
- archive confidence
- exposure duration band
- foreign broad-intelligence recipients
- bounded named exploiters
- personnel and network risk records
- active missions
- selected response path
- deception state
- investigation route class
- evolution profile at the time of firing
- cleanup proof

Nothing from an earlier incident should leak into the new sequence unless it is a real lasting result. A previous captured operative stays captured. A previous network remains damaged until rebuilt through normal mechanics. A country that completed a lasting compartmentation reform can receive the bounded future resilience defined by that reform. Old Exposure, old exploiters, old duration, old mission progress, old reliance, and old deception targets never carry into the next incident.

The event should not permit two normal Event 52 sequences to overlap. Total Compromise creates several targets inside one sequence, which is distinct from multiple independent sequences.

## Opening archive profile

The baseline archive contains three to five active domains. Four is the normal center of the distribution.

Every baseline incident includes at least one military or mobilization domain and at least one nonmilitary domain. This prevents a firing that exposes only abstract political material or only one branch of the armed forces.

The archive domains are:

1. Army plans and land-force assessments
2. Naval dispositions and convoy intelligence
3. Air operations and basing information
4. Industrial and resource estimates
5. Diplomatic correspondence and negotiating positions
6. Internal security and political assessments
7. Agent registries and contact chains
8. Cryptologic material and security procedures
9. Mobilization plans and reinforcement assumptions
10. Research priorities, strategic shortages, and procurement concerns

The baseline incident normally draws from the first six domains. Agent registries, cryptologic material, detailed mobilization plans, and research or shortage files become more common under Deep Files. They can still appear in a limited baseline variant when the target has the relevant systems and the rare profile supports them.

Archive domains affect the kind of temporary intelligence foreign countries receive, the kind of named exploitation available, the target's most valuable responses, the cost of rewriting compromised systems, and the reports shown during the incident.

The domain set must be visible in a compact qualitative form. The player should see broad labels such as army plans, naval deployments, industrial estimates, or agent records. The player should not see hidden domain scores or every recipient's copy quality.

## Initial Exposure

Exposure is the event's only persistent player-facing custom value.

Exposure uses a 0 to 100 range.

- Critical: 76 to 100
- Severe: 51 to 75
- Significant: 26 to 50
- Fading: 1 to 25
- Neutralized: 0

The ordinary baseline opening range is 55 to 85.

The initial value depends on:

- number of archive domains
- presence of live plans
- target's agency and counterintelligence quality
- target's cryptologic condition
- current war state
- number and sensitivity of active operations
- presence of exposed mobilization or shortage files
- rare archive profile
- lasting compartmentation resilience from earlier incidents

A strong service can reduce the opening value, but no ordinary country should erase the incident at the opening. A weak service can begin near the top of the range. A country at war can begin higher because plans and dispositions become useful immediately.

Exposure does not represent public embarrassment, government legitimacy, or the total quantity of paper in circulation. It represents current operational usefulness. A large archive can remain physically present after Exposure reaches zero because its codes, plans, deployments, contacts, and estimates have become obsolete.

## Information asymmetry

The target knows less than the recipients during the opening days.

The target immediately knows:

- that a major breach occurred
- current Exposure
- the broad active domains
- whether personnel are at immediate risk
- the expected duration band
- which emergency actions are available

The target does not immediately know:

- the exact source route
- every government holding a copy
- exact recipient confidence
- exact foreign reliance
- every named exploiter
- which specific file is genuine, incomplete, or altered
- whether all copies match

Damage-control actions, friendly warnings, counterintelligence reports, foreign operational behavior, and the investigation can reveal parts of this hidden picture.

The target should never receive a complete world ledger. The event is stronger when foreign intent remains partly inferred from actions.

## Broad foreign exposure

Every ordinary foreign government receives a meaningful temporary intelligence advantage against the target.

This universal exposure is the event's baseline promise. The implementation should not reduce the leak to a small random list of recipients.

The advantage covers safe base-game surfaces such as civilian, army, navy, and air intelligence. Its strength follows current Exposure and the active archive domains. A country with no navy can still hold naval files, but it gains little practical value from them. A landlocked minor with a weak service receives the archive yet is unlikely to become a named naval exploiter.

Temporary intelligence must be reversible and incident-owned. The event must not use an untracked permanent grant that remains after the archive becomes obsolete.

Countries excluded from ordinary intelligence systems do not receive the broad advantage. Subjects, allies, faction partners, neutrals, rivals, and enemies can all receive the archive, but their willingness to use it differs.

## Opening reports

The target receives one opening report. Other governments receive a foreign report or news treatment appropriate to the established Event 52 presentation pattern.

The target report should emphasize:

- uncertainty over distribution
- immediate risk to agents and plans
- the need to make the archive obsolete
- the possibility that foreign governments hold different versions
- the cost of changing systems quickly

Foreign reports should emphasize:

- the scale of the intelligence windfall
- the surprising range of material
- disagreement over authenticity and freshness
- the temptation to exploit the archive
- the target's first visible changes in posture

The report should not explain hidden reliance, exact random weights, evolution gates, or investigation route classes.

## Baseline phases

The ordinary incident moves through three overlapping phases.

### Immediate containment

This phase begins at firing and remains dominant while Exposure is Severe or Critical.

The target replaces codes, recalls endangered personnel, changes military plans, and shuts vulnerable channels. Foreign exploiters act most aggressively during this phase. The Personnel at Risk mission can appear here.

### Network reconstruction

This phase becomes available when the first emergency action is complete or Exposure falls below Severe.

The target rebuilds covers, restores networks, compartmentalizes files, and repairs trusted liaison channels. Some emergency actions remain available if the related risk persists.

### Optional deception

This phase becomes available when the target has basic containment proof and enough intelligence capability to manage a controlled false-information campaign.

The target can poison the leaked archive, seed contradictory orders, stage false deployments, and observe which foreign governments continue to rely on the stolen information.

The phases control decision visibility. They are not separate public meters. The category should show three to five primary actions at one time and one to three active missions.

## Incident closure

The incident closes through either of two valid routes:

- Exposure reaches zero through natural obsolescence and damage control.
- The dynamic exposure period ends with Exposure above zero, after which the remaining value is committed to zero because the archive is too old to provide the event's special advantage.

Closure removes temporary broad intelligence, recipient exploitation state, current reliance, category actions, missions, target penalties, and incident markers. Deception outcomes already triggered remain for their own bounded duration. Ongoing operations that failed or were cancelled remain failed or cancelled.

The target receives a closing report only when the incident produced a meaningful outcome, such as complete neutralization, serious personnel loss, successful deception, or an unresolved high-cost recovery. Routine silent cleanup is acceptable when no new choice or consequence needs explanation.

The event then returns to the normal Repeatable event system. Its weight recovery and cap reduction follow the shared rules.
