# 012 Africa spec part 18, Charter League target mission atlas

This file expands Charter League mechanics into target-specific mission families. Labels are internal working labels, not final decision or mission localisation.

## Target-state values

| Value | Meaning | Main sources | Main sinks | Visible result |
| --- | --- | --- | --- | --- |
| Confidence | Trust that the League protects the target without devouring it | Defense aid, recognition, rail projects, fair arbitration, shared wars | Coercion, failed aid, ignored raids, annexation pressure | Acceptance, association, and federal integration become easier |
| Influence | Practical dependence on the unifier | Arms, advisors, factories, rail links, officers, food relief | Balanced sponsorship, autonomy guarantees, rival aid | Higher influence opens pressure routes, but can create backlash |
| Autonomy demand | Desire to remain visibly independent | Strong army, strong industry, historic identity, foreign guarantees, high confidence if federal | Military governors, emergency war, weak legitimacy | High autonomy blocks annexation and favours association |
| Rival appeal | Pull toward a rival bloc or independent coalition | Refused invitations, coercion, foreign patronage, regional rivalry, low confidence | Mediation, defense success, local restoration, concessions | High appeal creates rival blocs, exits, or war |
| Coloniser pressure | Immediate threat from outside owners or colonial wars | Colonial owner claims, wars, sanctions, expeditionary plans | League defense, international recognition, de-escalation | High pressure makes defense decisions urgent |
| Regional readiness | Whether a region is ready for staged integration | Rail, supply, local support, peace, member confidence | War damage, resistance, disaster pressure | Allows cores, constituent status, or associated-state upgrades |

## Member confidence formula direction

The implementation should use a component model, not one flat value. The visible tooltip should explain the largest positive and negative components without exposing hidden future outcomes.

| Component | Direction | Notes |
| --- | --- | --- |
| Shared war defense | Positive | Strongest gain when the unifier actually helps against a coloniser or outside invader |
| Aid delivered | Positive | Scales by equipment, convoys, rail access, and whether the target needed the aid |
| Regional proximity | Positive or neutral | Neighbours should be easier to influence than distant members |
| Historic identity strength | Negative for annexation, positive for association | Restored polities and stronger African countries resist full absorption |
| Autonomy guarantee | Positive for trust, negative for rapid annexation | Federal route uses this as a core promise |
| Coercive pressure | Negative | Command and conquest methods pay a real cohesion cost |
| Rival patronage | Negative | Outside powers can raise rival appeal and dependency alternatives |
| Local support | Positive | Staged coring needs local support in the target region |
| Disaster pressure | Route dependent | Deep Green can force compliance but harms normal legitimacy |

## Mission family table

| Working decision or mission | Target selector | Cost or requirement family | Success direction | Failure or refusal direction | AI behavior |
| --- | --- | --- | --- | --- | --- |
| `observe_target` | Any African country in a named region | Diplomatic staff, intelligence exposure, or time | Reveal confidence, autonomy demand, coloniser pressure, and rival appeal. | Target gains suspicion if repeated too often. | AI observes neighbours and colonial-war targets. |
| `invite_to_charter` | Observed country with viable confidence | Political effort, relation work, and regional envoy capacity | Target joins League as member, associate, protectorate candidate, or observer. | Refusal raises rival appeal and outside patron interest. | AI invites high confidence countries first. |
| `defend_against_coloniser` | African country at war with colonial owner or outside power | Equipment, convoys, volunteers, military access, or border control | Unifier enters defensive support, sends aid, or joins war by stage. | Failure reduces confidence and may spawn rival security bloc. | AI uses when strong enough and target is near. |
| `recognise_member_government` | League member or observer | Diplomatic capital and foreign alert risk | Raises confidence and legitimacy, lowers rival appeal. | Colonial powers may sanction or threaten. | AI uses for strategic members. |
| `send_arms_pipeline` | Member, observer, or liberation target | Rifles, support equipment, trucks, convoys, and route access | Raises arms influence and war survival. | Dependency rises if one sponsor dominates. | AI uses with spare stockpiles. |
| `build_member_rail_link` | Member with shared border or port lane | Trains, civilian capacity, and supply access | Raises logistics score and regional integration readiness. | Failure wastes capacity and lowers confidence. | AI prioritises low supply members. |
| `mediate_member_dispute` | Two members with rivalry flags | Time, legitimacy, and envoy capacity | Lowers rival appeal and prevents bloc formation. | Failure starts leadership contest. | AI uses if cohesion is low. |
| `pressure_association` | Member with high influence and moderate confidence | Legitimacy, local support, and regional project progress | Moves member toward associated state or constituent status. | Autonomy backlash if confidence is too low. | AI uses cautiously. |
| `offer_federal_constituency` | High confidence member | Local support, peace, and completed regional projects | Starts staged core mission or constituent status. | Failure locks target from peaceful integration for a long period. | AI only at high cohesion. |
| `appoint_military_governor` | Occupied or coerced region under Command route | Command obedience, divisions present, support equipment | Speeds control and integration work. | Raises resistance and rival appeal. | AI uses only in war emergency. |
| `restore_local_polity` | Named region with eligible restoration candidate | State control, cultural legitimacy, and setup resources | Releases or empowers restored polity as subject, associate, or member. | Weak packages can be exploited by rivals if unsupported. | AI uses if restoration improves cohesion. |
| `reconcile_rival_bloc` | Rival bloc leader after crisis or war | Legitimacy, concessions, and member confidence | Rival bloc can rejoin, federate, or stay independent. | Failed talks can trigger final confrontation. | AI uses after winning or stalemate. |
| `coercive_annexation_project` | Target with low confidence and route permitting coercion | Army presence, equipment, legitimacy cost, resistance risk | Target can be annexed through staged missions. | High resistance, sanctions, and League cohesion loss. | AI rare and high threat only. |

## Target selector packs

| Selector | Eligible targets | Exclusions | First action | Later actions |
| --- | --- | --- | --- | --- |
| `home_region_members` | African countries or restored polities in the unifier home region | Dead tags, current enemies, high rival leader without mediation | Observe target | Invite, defend, associate, integrate |
| `colonial_war_targets` | African countries at war with colonisers or outside powers | Targets already led by hostile special chaos countries | Defend against coloniser | Recognition, arms, League entry, postwar settlement |
| `restoration_candidates` | Named regions where an old polity package is eligible | Missing minimal state group, already restored equivalent, unsafe tag conflict | Restore local polity | Member status, subject route, cultural guard missions |
| `strong_african_states` | African countries with army, industry, or faction backing | Countries already in existential war against unifier | Observe and offer guarantee | Association, rival bloc contest, negotiated federation |
| `coastal_and_island_gateways` | Ports, islands, and returnee lane targets | No port access, hostile naval blockade, high local reception strain | Open lane or gateway mission | Settlement, industry, cultural diplomacy |
| `rival_bloc_members` | Countries with high rival appeal or rival bloc flag | Countries under truce or hard peace lock | Mediation or pressure | Reconciliation, containment, war, or independence settlement |
| `coercion_targets` | Targets with failed diplomacy and route permitting force | Federal autonomy guarantee active, high-chaos disabled path mismatch | Ultimatum or governor | Staged annexation, puppet, resistance outcome |

## Refusal ladder

A refusal should not be a dead end. The first refusal raises suspicion and rival appeal. Repeated refusal can create a neutral observer state, a rival regional bloc, a foreign-backed bloc, or an open war crisis. Federal and Sacred Soil routes should receive more reconciliation tools. Command and Deep Green routes should receive stronger pressure tools with harsher blowback.

## Cleanup rules

- Clear target flags when a country leaves Africa, dies, becomes a subject through another system, or joins a terminal world-end actor.
- Close missions when the target is at war with the unifier unless the mission is a war mission.
- Remove duplicate decisions for a target when it moves from observer to member, from member to constituent, or from rival to reconciled member.
- If the League collapses, convert members into independent countries, subjects, or rival blocs based on confidence, autonomy demand, and route history.
- If the unifier changes route, existing missions should continue only when the new route still supports their method.
