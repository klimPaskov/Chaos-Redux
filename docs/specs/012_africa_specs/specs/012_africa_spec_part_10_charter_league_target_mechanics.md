# 012 Africa spec part 10, Charter League target mechanics

This file expands the Charter League into target-state and member-country mechanics. It does not write final localisation. All labels are working labels, not final text.

## League target model

Every African country, African civil-war side, restored polity, colonial owner with African states, and eligible African subject can enter a League target record. The record is used by decisions, focuses, AI, integration missions, and cleanup.

A target can be in one of these states:

| Target state | Meaning | Player-facing direction | Main transitions |
| --- | --- | --- | --- |
| Observed | The unifier can see the target as an African or African-held issue | The player sees a regional situation, not a reward list | Invitation, defense request, colonial crisis |
| Invited | The unifier has sent a Charter League invitation | The target is weighing protection, autonomy, ideology, and fear | Accept, refuse, delay |
| Protected | The League has promised aid or entered defense of the target | The target expects real military or material help | Member, failed protection, rival appeal |
| Member | The country is inside the League but not absorbed | The country has rights, confidence, and influence pressure | Federal member, puppet route, exit, rival bloc |
| Federal candidate | The country is considering voluntary federation | The player sees a long accession project | Federal member, delayed, refused |
| Subject candidate | The country is being pulled into a protectorate or puppet relationship | The player sees pressure and cost | Puppet, revolt, rival appeal |
| Coerced target | The unifier is using force or threats | The player sees resistance risk and legitimacy cost | Annexation, revolt, foreign guarantee |
| Rival member | The target joined or founded a rival African bloc | The player sees a competing African project | Reconcile, cold war, war |
| Lost target | The target can no longer be worked normally | The player sees the reason only when useful | Cleanup, renewed observation |

A target record should use country flags, country variables, and scoped target arrays only where needed. The spec intent is a living member system, not a static decision store.

## Core values

The League uses five values. They should be visible through a decision category header or scripted GUI.

| Value | Scope | Meaning | Typical range | Direction |
| --- | --- | --- | --- | --- |
| Member confidence | Per target country | Trust that the unifier will respect and protect the member | 0 to 100 | High confidence enables voluntary federation and lowers exit risk |
| Unifier influence | Per target country | Practical dependence on the unifier | 0 to 100 | High influence enables integration pressure and puppet routes |
| Local autonomy demand | Per target country | Resistance to central rule | 0 to 100 | High autonomy blocks annexation and makes federal route safer |
| Rival appeal | Per target country | Pull toward rival bloc, colonial patron, or independent leadership | 0 to 100 | High appeal can trigger refusal, exit, or rival bloc |
| League cohesion | Unifier global | Health of the League as a whole | 0 to 100 | Low cohesion slows all member work and raises rival chances |

## Member confidence formula

Use a dynamic formula. Values below are design weights, not final constants.

Start with a base confidence of 40 for a willing member and 25 for a wary member. Then apply factors:

| Factor | Direction | Notes |
| --- | --- | --- |
| Unifier legitimacy high | Add 5 to 20 | Comes from focuses, stability, route values, and successful mediation |
| Protected from colonizer | Add 10 to 25 | Larger gain when the unifier actually sent forces or equipment |
| Aid delivered | Add 3 to 15 | Scales with equipment, convoys, factories, or advisors sent |
| Autonomy respected | Add 5 to 20 | Federal Charter and Sacred Soil gain more here |
| Shared war victory | Add 5 to 20 | Does not apply to fabricated wars against African members |
| Same ideology family | Add 0 to 10 | Should not dominate the formula |
| Historical restoration respected | Add 0 to 10 | Applies to restored polities and Crown routes |
| Diaspora settlement handled well | Add 0 to 8 | Applies when settlement missions avoid local backlash |
| Coercive pressure used | Subtract 10 to 35 | Strong penalty for threats, forced annexation, or ignored refusals |
| Failed defense | Subtract 10 to 30 | Bigger penalty if the member loses capital or is annexed |
| Unifier declared war on African member | Subtract 25 to 60 | Severe penalty unless target was already a hostile rival bloc |
| Rival aid outcompetes unifier aid | Subtract 5 to 20 | Supports rival bloc formation |
| Member autonomy ignored | Subtract 10 to 30 | Critical for federal members |

Confidence bands:

| Band | Range | Behavior |
| --- | --- | --- |
| Hostile | 0 to 19 | Refuses membership, accepts rival backing, may prepare war |
| Wary | 20 to 39 | Can accept protection but resists integration |
| Cooperative | 40 to 59 | Accepts aid and basic League votes |
| Confident | 60 to 79 | Can consider federal accession and shared reserves |
| Entrenched | 80 to 100 | Strong voluntary federation candidate and stable member |

## Influence and autonomy interaction

Influence alone must not equal consent. A target with high influence and low confidence is vulnerable to coercion, but that path creates resistance and rival appeal.

| Influence | Confidence | Result |
| --- | --- | --- |
| Low influence, high confidence | Friendly autonomous member, good federal candidate after longer work |
| High influence, high confidence | Strong voluntary accession candidate |
| High influence, low confidence | Coercive route temptation, high revolt and rival risk |
| Low influence, low confidence | Likely refusal, exit, neutrality, or rival bloc |
| Medium influence, medium confidence | Standard member, use missions to tip outcome |

Autonomy demand should fall through voluntary benefits, successful local missions, and regional integration work. It should rise after coercion, ignored local institutions, forced leader changes, and settlement failures.

## Regional selectors

The League should target regions through named selectors. These are design regions, and final state ids belong to implementation.

| Selector | Geographic intent | Typical targets | Special rules |
| --- | --- | --- | --- |
| Maghreb coast | Morocco, Algeria, Tunisia, Libya, coastal Egypt if route includes it | Ports, colonial garrisons, desert approaches | High outside-power reaction from France, Italy, Spain, and UK interests |
| Nile valley | Egypt, Sudan, Nile corridor, Nubian and Kush restoration areas | Capitals, river crossings, irrigation zones | Strong interaction with Kush, Nubia, Makuria, and Aksum |
| Horn highlands and Red Sea | Ethiopia, Eritrea, Somalia, Djibouti, Red Sea ports | Highland capitals, ports, Italian or British claims | Strong Aksum and Red Sea trade content |
| Sahel caravan belt | Mauritania, Mali, Niger, Chad, northern Nigeria, inland Sudan edges | Caravan routes, desert forts, Lake Chad approaches | Strong Kanem-Bornu, Songhai, Futa, and Tuareg-adjacent issues |
| Gulf of Guinea | Senegal to Cameroon coastal and forest belt | Ports, cocoa, gold, oil, railheads | Strong Asante, Oyo, Benin, Dahomey, Futa, and labour content |
| Congo basin | Congo river system and central forests | River ports, mineral zones, forest regions | Strong Kongo, Kuba, Luba, Lunda, nonhuman high-chaos routes |
| Great Lakes | Uganda, Rwanda, Burundi, western Kenya, eastern Congo, Tanzania interior | Lake ports, highlands, Buganda | High local autonomy demand and border settlement needs |
| Swahili coast | Kenya, Tanzania coast, Zanzibar, northern Mozambique, Comoros if included | Ports, island trade, Indian Ocean routes | Strong Kilwa and Indian Ocean route content |
| Zambezi and Zimbabwe plateau | Zimbabwe, Zambia, Malawi, Mozambique interior | Great Zimbabwe, Mutapa, Rozwi, rail and mining belts | Strong restoration and resource integration |
| Southern Cape and plateau | South Africa, Namibia, Botswana, Lesotho, Eswatini, Angola south if needed | RSA branch, ports, mines, rail lines | RSA civil war and Allied peace logic |
| Indian Ocean islands | Madagascar, Comoros, Mauritius, Seychelles if in scope | Ports, naval routes, Merina | Requires convoy and port access |
| Atlantic islands and ports | Cape Verde, Sao Tome, coastal island and Atlantic nodes if represented | Diaspora and convoy routes | Should not be instant coring land route |

## Invitation logic

A target receives a meaningful invitation only if at least one of these is true:
- it is independent and has a capital in Africa
- it is an African subject that can be negotiated with or defended
- it controls an African capital or core region through event logic
- it is at war with a colonizer and can request League protection
- it is a restored polity created by the event
- it is a civil-war side in Africa and not a terminal hostile chaos actor

Invitation acceptance should consider:
- confidence, if already known
- ideology compatibility
- unifier threat and strength
- colonizer threat
- whether the target is already in a faction
- whether the unifier has fought African countries
- whether the unifier can reach the target
- route identity
- chaos tier
- whether the target has its own continental ambition

### Acceptance outcomes

| Outcome | Conditions | Consequence |
| --- | --- | --- |
| Full acceptance | High confidence, fear of colonizer, compatible route | Target becomes member and opens aid actions |
| Defensive acceptance | At war or threatened, but wary | Target gets protection state and temporary membership |
| Delayed answer | Medium confidence or internal politics | Timed mission to improve confidence |
| Conditional acceptance | Strong target with autonomy concerns | Requires autonomy guarantee or aid |
| Refusal | Low confidence or high rival appeal | Starts refusal cooldown and rival appeal |
| Hostile refusal | Coercion, incompatible ideology, or border clash | Can form rival bloc or seek outside sponsor |

## Refusal logic

Refusal should not always mean war. The system should support several refusals.

| Refusal type | Trigger direction | Result |
| --- | --- | --- |
| Neutral refusal | Target is stable, not threatened, and sees no benefit | Cooldown and small rival appeal |
| Autonomy refusal | Target likes protection but rejects integration | Member stays or becomes observer, integration blocked |
| Ideological refusal | Route conflict is strong | Rival influence rises, propaganda decisions open |
| Colonial-backed refusal | Outside power protects or pressures target | Outside reaction tree opens |
| Military refusal | Target believes it can resist | Border mission or war preparation starts |
| Rival-founder refusal | Several targets share grievance | Rival bloc formation can begin |

## Rival bloc formation

A rival African bloc forms when enough targets believe the unifier is a danger or a false continental leader. This should be an African-led counterproject, not automatically a colonial puppet.

Formation triggers:
- at least three African members or observers with confidence below 40 and rival appeal above 50
- or one strong African country with confidence below 30, army strength above a regional threshold, and at least one backer
- or a failed coercive annexation causing regional revolt
- or a member state exits after the unifier attacks another African member

Rival bloc types should be selected by region and ideology:

| Rival bloc working label | Conditions | Identity |
| --- | --- | --- |
| Nile League | Nile or Horn targets dominate | River, highland, and Red Sea autonomy |
| Sahel Pact | Sahel and Lake Chad targets dominate | Caravan, desert, and inland sovereignty |
| Gulf Union | Gulf of Guinea targets dominate | Coastal trade, labour, and forest states |
| Lakes Union | Great Lakes targets dominate | Highland and lake politics |
| Southern Union | RSA, southern, or plateau targets dominate | Mines, ports, and southern security |
| Island League | Indian Ocean islands dominate | Sea lanes and island autonomy |
| Congress of Free Members | Mixed regions, democratic or federal refusal | League legitimacy challenge |
| Revolutionary Rival Congress | Communist or radical refusal against a non-revolutionary unifier | Competing anti-colonial claim |
| Royal League | Crown route backlash or royal autonomy conflict | Restored houses resisting central crown |

Rival blocs can reconcile if confidence recovers, if an outside power threatens all African states, if the unifier grants autonomy, or if the rival leader loses a war. War should be possible but not mandatory.

## Member routes

A member should have one of several relationship routes. The route is chosen by player actions, member confidence, local autonomy demand, target strength, ideology, and the unifier focus path.

| Member route | Requirements | Result | Risk |
| --- | --- | --- | --- |
| Federal member | High confidence and autonomy guarantee | Member stays as tag with federal benefits | Slow integration and lower direct control |
| Federal accession | Very high confidence and completed regional missions | Member peacefully integrates or becomes semi-integrated | Delay if local autonomy demand rises |
| Associated state | Medium confidence, high autonomy demand | Member becomes a protected subject | Rival appeal if overused |
| Protectorate | Low confidence but high influence | Subject relationship under pressure | Resistance and foreign criticism |
| Coercive annexation | Very high influence, low confidence, command or empire route | Annexation or forced integration | Revolt, rival bloc, legitimacy loss |
| Restored polity partner | Historical restoration and high local support | Member remains or joins as regional subject | Succession disputes |
| Lost member | Failed defense, abuse, or outside pressure | Exits League | Rival bloc or foreign guarantee |

## Target-state decision families

### Observation and invitation

Used for new targets. Decisions should be lightweight but not free for every target. They can cost diplomatic effort, convoys, liaison missions, or regional access.

### Protection and defense

Used when a target is threatened by colonizers or rival blocs. These decisions should require real support:
- infantry equipment
- support equipment
- convoys for coastal targets
- trains or trucks for inland aid
- volunteer access
- divisions near key states
- supply corridor control

### Confidence and autonomy

Used to raise confidence or lower autonomy demand. Missions should be action-based:
- build or repair a rail link
- defend a capital for a timed period
- deliver equipment
- hold a mediation congress
- recognize local institutions
- settle land disputes
- escort convoys
- build port or clinic capacity

### Influence and integration

Used after member ties are established. Influence decisions should be visible and risky:
- officer missions
- customs alignment
- common currency preparation
- shared construction
- legal harmonization
- regional service projects
- security assistance

### Coercion and pressure

Used by routes that accept force. These decisions must have costs and risks:
- command power within conservative caps
- infantry equipment
- stability loss
- local resistance
- member confidence loss
- rival bloc gain
- outside-power reaction

## Cleanup rules

Every target record needs cleanup. Cleanup should happen when:
- the target no longer exists
- the target is annexed
- the target is no longer in Africa by capital or event origin
- the unifier no longer exists
- the unifier changes away from the event package
- the member leaves the League
- a civil war invalidates the old target state
- a world-end scenario freezes ordinary event systems
- the target becomes a nonhuman high-chaos actor outside ordinary League diplomacy
- a rival bloc war ends and treaty cleanup occurs

Cleanup should remove:
- target flags
- active missions
- selected target markers
- integration project flags
- obsolete timed guarantees
- stale event targets if global targets were used
- rival appeal cooldowns when the target is gone
- member confidence display entries
- AI strategy tags that no longer apply

Do not leave decisions visible for dead countries, invalid subjects, vanished civil-war sides, or already integrated targets.

## AI target evaluation

AI should use the League only when it can support the target. AI target scoring should consider:
- distance and supply access
- current wars
- equipment stockpile
- convoys and port access
- stability
- target threat from colonizers
- target strength
- member confidence
- rival appeal
- ideology
- focus route
- chaos tier
- outside-power risk
- player proximity

AI should not spam invitations to every target at once. It should prioritize:
1. threatened neighbors
2. colonial-war targets it can actually reach
3. high-confidence members
4. key regional anchors needed for integration
5. restored polities that fit its route
6. diaspora ports if on Black Star Return
7. rival bloc members only after preparing reconciliation or war

## Player-facing presentation direction

The League UI or decision header should show:
- current League cohesion
- selected target name
- target confidence
- target influence
- autonomy demand
- rival appeal
- current relationship route
- active mission count
- main blockers in icon-first form

Text direction should describe visible diplomacy, aid, fear, local institutions, and military risk. It should not expose secret formulas, final achievement text, or future hidden routes.
