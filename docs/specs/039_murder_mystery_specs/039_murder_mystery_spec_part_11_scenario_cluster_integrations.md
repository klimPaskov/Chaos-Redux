# Murder Mystery Specification Part 11: Triggerable Scenario, Cluster, and Event Integrations

## Triggerable scenario identity

The manual scenario is named `Assassin Network`. It starts Event 39 as a sandbox or challenge setup without requiring the normal event, Chaos threshold, evolution history, or investigation progression.

The authoritative scenario workbook must reserve the next available stable scenario ID. `SCN-014` is a provisional suggestion only because the supplied export contains active IDs through `SCN-013` and retains earlier gaps for known scenarios. The implementation must confirm the workbook and registry before assigning the ID.

The scenario uses one scenario type unless later design adds a clearly distinct mode. Host selection and intensity are enough for the accepted version.

## Scenario launch rules

The launch is available when:

- no incompatible world-end state is active
- no active Event 39 network already owns the world
- at least one valid ordinary host exists
- required dynamic country capacity exists for High or Maximum intensity
- character and territory preflights can support the selected intensity

The scenario must not be blocked by normal Event 39 weight, Chaos level, date, evolution unlocks, event history, cluster state, or prior natural opening conditions.

If the current player country is an eligible ordinary host, the scenario detail panel can offer it as the default host. Otherwise the launch selects a valid major or player-controlled country through normal host weighting. Special Chaos and nonhuman countries are excluded.

The confirmation window reads the selected scenario, intensity, and host preference at confirmation time. Cancel changes nothing.

## Shared setup API

The scenario wrapper calls the same Event 39 helpers used by natural progression:

- host selection and eligibility
- safe succession and character protection initialization
- original movement and case initialization
- cell registry initialization
- Evolution I and II behavior setup
- Assassin State split and country setup
- foreign revolt and derivative setup
- faction and subject setup
- focus, decision, unit, asset, and AI initialization

Scenario flags may bypass normal evolution timing and Chaos requirements during setup. They must not bypass impossible character, map, tag, supply, country, or protected-system gates. Every bypass flag is cleared before the first normal day after setup.

## Intensity contract

### Low

Purpose: early international investigation challenge.

Setup direction:

- original host begins with a live Murder Cult
- Network Reach begins in the lower organized range
- two to four foreign cells are seeded at stage 1 or 2
- no Assassin State exists
- murders can begin after a short preparation window
- original and foreign governments receive their normal categories
- the movement can progress through natural Evolution II and later content

Low should be survivable by a capable host and should teach the investigation and cooperation systems.

### Medium

Purpose: mature international network near territorial escalation.

Setup direction:

- original host has a mature national cult and strong institutional infiltration
- Network Reach begins around the upper organized or lower international range
- five to eight foreign cells exist, with a mix of active and entrenched stages
- the original host starts close to the Evolution III split requirement
- at least one public cell crisis has already exposed international methods
- no Assassin State exists on launch

The setup should give the original host meaningful time to prevent the split if it acts well.

### High

Purpose: immediate Assassin State war with international counterintelligence pressure.

Setup direction:

- create the Assassin State through the normal validated split transaction
- start the war against the original host
- initialize Evolution III behavior
- seed five to nine strong foreign cells
- place one to three countries near stage 4 revolt readiness
- grant a balanced opening army, stockpile, focus, decision, agency, and Cohesion state
- do not create foreign derivative countries immediately unless a specific preflight result is needed for map validity

High should begin as a two-sided war with a live international network, not as an automatic movement victory.

### Maximum

Purpose: advanced Evolution IV campaign.

Setup direction:

- create the Assassin State and original-host war
- initialize Evolution IV
- seed eight to fourteen cells within current performance and country caps
- create two to four validated foreign Assassin derivatives or active uprisings
- create the Veiled Compact and subject hierarchy
- grant stronger custom units and support, within normal technology and equipment rules
- begin with substantial Network Reach and route-neutral Brotherhood Cohesion
- leave the political route and terminal command settlement unchosen

World of Anarchy remains unavailable until global Chaos reaches 1000, Evolution V becomes active, the branch is enabled, and the movement completes terminal preparation.

## Scenario scaling

Intensity changes setup scale, not permanent hidden cheats. After launch, ordinary production, reinforcement, investigation, cell, focus, AI, subject, and terminal rules apply.

Host size and world size modify the exact cell and unit counts. A small world should not receive the same absolute network as a large intact world. Maximum intensity cannot exceed derivative tag capacity or safe map transactions.

## Scenario history

The scenario records its own launch entry and intensity. It does not claim that the natural opening event fired or that the natural baseline investigation was completed. Evolution records are created only for behaviors the scenario actually activates.

A scenario-launched Event 39 can later resolve, reach World of Anarchy, or be defeated through normal content. It remains one Event 39 lifecycle.

## Scenario cleanup

Cleanup must clear:

- launch bypass flags
- selected scenario and intensity temporary state
- host preference temporary state
- preflight candidate arrays
- temporary scenario setup targets
- duplicate launch locks after failure
- partial tag and country reservations when a transaction rolls back

The scenario becomes unavailable while any Event 39 network, Assassin State, derivative, or terminal setup is active. After complete resolution, relaunch policy follows the shared triggerable-scenario framework and should prevent duplicate history or stale carrier reuse.

## Intelligence cluster

The supplied cluster catalog lists Intelligence as unavailable, without a cluster ID or members. Implementation must reserve the next authoritative cluster ID in the XLSX workbook and shared registry. `9` is a provisional expectation because active cluster IDs in the supplied export run from 1 through 8. Do not hardcode the provisional ID before workbook confirmation.

### Cluster identity

The Intelligence cluster covers incidents driven by covert access, espionage, counterintelligence, compromised institutions, hidden networks, and intelligence response. Murder Mystery is a Medium member.

### Event 39 participation

If Event 39 is the selected cluster member, the cluster can connect it to other enabled intelligence incidents without changing its fire-once identity. Member effects must remain independently valid and count as one cluster pacing event.

The cluster should not automatically escalate Murder Mystery to an evolution. A connected intelligence incident can change starting evidence, agency exposure, route knowledge, target protection, or cell seeding only through a concrete mapped interaction.

### Cluster safety

- Event 39 remains unavailable after its natural fire-once lifecycle closes
- the cluster cannot bypass safe host or succession gates
- a cluster fire cannot create a second Event 39 network
- cluster member order cannot remove characters before Event 39 protection setup
- Event 39 records its normal history and member result
- cluster history records fired or skipped reasons

## Event integration principles

Connections should make existing mechanics react. They must not create universal bonuses or duplicate another event's source system.

## Specific event and system connections

### Event 004 Random War and ordinary wars

War disruption lowers investigation capacity, exposes routes, changes state missions, and can increase foreign cell seed weight. Existing war Chaos sources remain authoritative. Event 39 adds Chaos only when a cell uses the war to achieve a distinct movement milestone.

### Event 005 Soviet Collapse and other country dissolutions

Country breakup requires cell and protected-character revalidation. A local cell transfers only to a valid successor that owns its relevant territory and passes ordinary-government gates. The Assassin State split cannot collide with an active collapse transaction.

### Event 006 Independence Wave

Newly independent countries may inherit a local rumor or cell only when an existing route crosses their territory. Independence is not automatic cell creation. Event 39 must respect the shared country carrier registry and frozen release transaction. A planned foreign Assassin revolt waits until Event 006 releases and transfers are complete.

### Event 007 Fury and special Chaos countries

Fury actors that classify as special Chaos countries are excluded from ordinary murder and leadership-extermination logic. They can fight the Assassin movement through their own government and population rules.

### Event 009 White Peace

The original host war and active World of Anarchy wars should not receive an unrelated automatic white peace that leaves country packages half resolved. A negotiated Event 39 settlement must use its own outcome and cleanup. Cluster or generic peace systems should detect the protected war relation.

### Event 011 Secret Alliance and coalition systems

A hidden alliance can complicate intelligence sharing, route access, or coalition trust. Event 39 can expose a connection only when evidence supports it. It must not reveal unrelated secret-alliance data automatically.

### Event 016 Brilliant Scientist and event-owned specialists

Scientists, special project figures, and event-owned personnel are protected unless their owning system supplies an Event 39 removal callback. Event 39 can use a generic research-office casualty instead of deleting an owned character.

### Event 019 Infantry Spawn

The Assassin Forces unit family integrates through the owner-side provider contract in Part 9. Event 19 derivatives must not activate Event 39 or inherit its progression.

### Event 022 Concentration Camps and repression systems

A government may use harsh detention or camp systems against suspected cells only through explicit connected decisions. Such action can reduce immediate cell freedom while damaging evidence, legitimacy, condemnation, recruitment pressure, or local resistance. Event 39 should not imply that mass detention is an efficient default investigation method.

### Event 028 Asteroid, nuclear use, and state destruction

Destroyed or wasteland states leave split and revolt candidate pools. Active cell missions retarget or fail cleanly. Character and capital transactions revalidate after major state loss. Shared deaths, contamination, and nuclear Chaos remain separate.

### Event 033 Acid Rain and natural disasters

Disaster states can reduce protection, route access, evidence transfer, and supply. Cells operating in those states also suffer movement and attrition. Natural disasters should not give the cult one-sided immunity.

### Events 034 and 035 Industrial Boom and Great Depression 2.0

Booming industry can support investigation equipment, transport, and security while creating larger target infrastructure. Depression weakens institutions, raises recruitment opportunity, and limits both government and Assassin production. Each system retains its own economic values and outcomes.

### Famine and migration systems

Cells can exploit a concrete border, transport, smuggling, or displacement route. Refugees and migrants are not treated as inherent cell carriers. Investigation and protection actions should avoid stigmatizing displaced civilians. Famine, migration deaths, reception, and movement remain owned by their shared systems.

### CBRN warfare and contamination

Chemical, biological, nuclear, and contamination effects can kill officials, damage capitals, interrupt investigations, and invalidate state missions. Event 39 units receive no special immunity. Public evidence of Event 39 atrocities can feed Condemnation only through the shared source adapters.

### Time Traveler and imported historical characters

Past or future figures created by another event remain protected until that event supplies a safe removal disposition. Event 39 uses generic office casualties if the imported character cannot be removed safely.

### Alien, machine, zombie, plague, and other nonhuman countries

Actual nonhuman and special Chaos countries are excluded from ordinary character targeting, foreign cells, territorial derivatives, and World of Anarchy government dismantling. Human countries affected by unusual events remain eligible only when their current government and character package still pass the ordinary classifier.

## Catalog and documentation alignment

Implementation must update:

- Event 39 row in the authoritative event catalog workbook
- Intelligence cluster row, ID, details, members, type, Chaos level, and status
- Assassin Network scenario row, stable ID, details, intensity effects, and status
- World of Anarchy public terminal fields and branch count
- Event 39 docs, scenario docs, cluster docs, unit registry docs, 3D docs, super-event docs, and achievement docs

After XLSX edits, regenerate all three CSV exports through the repository exporter. Never edit the export snapshots directly.
