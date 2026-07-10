# Condemnation, Deaths, Air Cleanliness, and Diplomacy

## Shared consequence rule

Chaos Warfare does not create new global consequence counters. Chemical and biological actions feed the existing shared systems:

- Deaths
- Air Cleanliness
- Condemnation
- outbreak and contamination state
- world threat where an existing source qualifies
- chaos value through the existing deaths and contamination rules

The CBRN system adds source detail and reliable call sites. It does not fork the underlying totals.

## Unified action record

Every deliberate use creates one action record with:

- attacker
- victim when known
- target state
- date
- weapon class
- delivery method
- operation severity
- civilian deaths
- military deaths
- contamination change
- outbreak change
- evidence quality
- attribution state
- retaliation status
- first-use status
- repeat-use pressure

The record is used by Deaths, Condemnation, event logs, diplomatic reactions, achievements, and later evidence discovery.

## Deaths integration

### Population loss

Civilian chemical and biological deaths reduce real state population through the shared Deaths helper. They also create one civilian log entry per resolved operation or continuing-death period, not one entry for every small internal tick.

Military deaths enter the military category. They should not also be removed from state population unless the existing military-casualty system already does that correctly.

### Source labels

Recommended internal source labels:

- chemical battlefield exposure
- chemical strategic raid
- persistent chemical contamination
- nerve suppression
- biological attack
- deliberate outbreak
- biological stockpile accident
- outbreak continuation
- CBRN doomsday release

Player-facing labels are written during implementation and should remain concise.

### Continuing-death aggregation

States with persistent contamination or outbreak use a single active severity. New exposure can:

- increase severity up to a cap
- extend duration up to a cap
- change agent profile if the new profile is more severe

It cannot add another independent full death loop for the same population.

### Death caps

Caps prevent accidental population deletion while allowing catastrophic outcomes.

Suggested caps per state and source episode:

- tactical chemical episode: 0.15 percent of state population
- strategic chemical raid: 0.75 percent
- catastrophic nerve raid: 1.50 percent
- serious biological outbreak: 2.5 percent over full duration
- catastrophic biological outbreak: 8 percent over full duration
- doomsday release: separate extreme cap set by scenario and world-end rules

The caps apply before repeated independent attacks. Repeated use can exceed them through separate episodes and should generate repeat-use Condemnation.

## Air Cleanliness integration

### State-to-global conversion

The existing Air Cleanliness system treats a chemically contaminated state as a global contribution. The redesign should update global contamination when a state crosses a contamination class threshold:

- Trace to Local crossing: small contribution
- Serious crossing: additional contribution
- Severe crossing: additional contribution
- Catastrophic crossing: major contribution

Recovery removes the contribution when a state falls below a threshold.

This avoids adding global contamination every week merely because one state remains contaminated.

### Biological contribution

Outbreak contribution follows existing low, base, and high intensity bands. Weapon source does not create a second global contribution. Deliberate use changes Condemnation and evidence, not the Air Cleanliness formula.

### Irreversible threshold

At the existing irreversible threshold, chemical and biological cleanup can still reduce local effects if the global system permits it, but global recovery behavior follows the authoritative Air Cleanliness design. This spec does not redefine the world-end threshold.

## Condemnation source buckets

### Chemical

Records:

- chemical support and artillery use
- chemical headquarters abilities
- chemical aircraft and raids
- nerve suppression
- chemical doomsday release
- persistent chemical contamination

### Biological

Records:

- strategic biological raids
- operative outbreak operations
- deliberate spread
- biological battlefield use
- public stockpile accident
- biological doomsday release

### Atrocity

Adds contextual pressure when:

- civilian populations are deliberately targeted
- nerve suppression causes mass death
- experiment sites are discovered
- occupied populations are denied protection after the occupier created the hazard
- captured facilities reveal human experimentation

### Coverup

Records:

- blocked inspections
- destroyed evidence
- false accident claims later disproved
- hidden stockpile routes
- destroyed medical records
- sanctioned procurement networks

## Attribution model

### Latent responsibility

Hidden use stores latent Condemnation by source. It is not shown as public total until evidence rises.

### Public states

| State | Evidence | Public gain |
| --- | ---: | ---: |
| Unknown | 0 to 19 | 0 to 10 percent of base, stored as suspicion only |
| Suspected | 20 to 44 | 25 percent of base |
| Probable | 45 to 74 | 60 percent of base |
| Confirmed | 75 to 100 | 100 percent of base |

When evidence crosses a band, the helper adds the unpaid portion rather than applying the full base again.

### Evidence floors

- confirmed aircraft wreckage or captured shells creates at least probable attribution
- captured operative with records creates probable or confirmed attribution
- mass civilian deaths plus distinctive samples creates a high floor
- public admission creates confirmed attribution
- a treaty retaliation announcement creates confirmed use but can reduce participant willingness to sanction

## Condemnation calculation

Base severity comes from action type. Multipliers apply for:

- civilian deaths
- military deaths
- affected population
- contamination class
- outbreak spread beyond target
- neutral or allied target
- occupied non-core target
- first use
- retaliation
- repeated use
- coverup
- public evidence
- humanitarian response

### Retaliation

Retaliation does not erase responsibility. It can reduce first-use and participant pressure when:

- enemy use is confirmed
- retaliation occurs within a defined window
- target is the original user or its armed forces
- response is proportionate

Strategic civilian retaliation, doomsday release, or attacks on third parties receive little or no mitigation.

### Doctrine mitigation rule

Doctrine can reduce:

- accidental use
- friendly casualties
- civilian exposed share through precise targeting
- evidence created by poor handling
- repeat-use waste

Doctrine cannot reduce:

- confirmed public responsibility
- deaths already caused
- contamination already visible
- the minimum Condemnation floor for a strategic or mass-casualty attack

## Existing Condemnation tiers

The system aligns with the current impact specification.

| Tier | Threshold | CBRN relevance |
| --- | ---: | --- |
| Normal standing | 0 to 24 | Recent sources tracked. |
| International concern | 25 | Monitoring, treaty pressure, protection aid to victims. |
| Formal censure | 50 | Inspection demands and reduced military support. |
| Arms embargo | 100 | Lend-lease, licenses, volunteers, and attachés restricted by participants. |
| Strategic embargo | 175 | Fuel, rubber, chromium, tungsten, and military imports restricted. |
| Total embargo | 300 | Broad isolation and research-sharing pressure. |
| Pariah state | 500 | Severe isolation, intelligence and containment pressure, possible faction rupture. |

Final threshold values remain owned by the condemnation system constants.

## CBRN-specific diplomatic actions

### Demand inspections

A participant requests access to facilities and stockpiles. Acceptance can reduce future pressure and reveal unsafe sites. Refusal raises suspicion and coverup pressure.

### Offer protective aid

Countries can send gas-mask crates, medical aid, decontamination equipment, or vaccines to the victim. This creates opinion, legitimacy, and evidence-sharing effects.

### Declare retaliation policy

A country publicly states it will retaliate after confirmed attack. It raises deterrence, stockpile pressure, and escalation risk.

### Join a chemical arms embargo

Targets payload, delivery equipment, protective technology, or general military trade according to sanction tier.

### Humanitarian carve-out

Allows masks, medical equipment, and decontamination supplies to reach the condemned country or its civilians while offensive materials remain embargoed.

### Share forensic evidence

Raises attribution confidence among allied or neutral participants. Requires intelligence, sample quality, and diplomatic willingness.

### Sponsor decontamination mission

Reduces contamination and deaths in a victim state. It can create observer access and evidence.

### Shield an ally

Faction leader or major ally reduces sanction participation at a political, trade, and legitimacy cost. Shielding confirmed mass use can create Condemnation or domestic pressure for the shield country.

## Treaty and policy memory

The 1925 Geneva Protocol is the period diplomatic reference. Countries can have:

- signatory or non-signatory status
- reservation or retaliation interpretation
- ratification status where existing history supports it
- no-first-use policy
- unrestricted route override

Treaty status affects:

- first-use Condemnation
- allied reaction
- inspection demands
- retaliation legitimacy
- AI willingness

It does not prevent production or stockpiling by itself.

## International reaction events

Use targeted event families after major thresholds, not repetitive popups after every tactical use.

Trigger examples:

- first confirmed chemical use in the war
- first strategic chemical raid
- first confirmed biological attack
- civilian deaths exceed a major threshold
- Condemnation reaches Arms Embargo
- evidence exposes a prior coverup
- an ally shields a pariah user
- a user destroys or surrenders a major stockpile

Player-facing direction should focus on visible casualties, evacuation, diplomatic action, and public response. Do not write generic “the world is shocked” filler.

## Sanction and supply interaction

CBRN programs need imported materials, aircraft, trucks, precision instruments, rubber, fuel, and research exchange. Sanctions can reduce:

- payload production efficiency
- protective-equipment imports
- aircraft replacement
- truck and instrument availability
- special-project progress
- foreign scientists and research sharing

Humanitarian carve-outs should protect defensive masks and medical aid when participant policy permits.

## Chaos value

The existing rules add chaos through deaths and Air Cleanliness changes. CBRN use should not also add a separate large direct chaos value unless a named event or extreme operation explicitly requires it. This avoids triple counting one attack.

## World threat

A conventional chemical or biological program does not automatically set `world_in_threat`. A source becomes a shared world threat only when:

- a biological outbreak is uncontrolled across multiple countries
- a doomsday release creates an existential spread condition
- a world-end branch qualifies under existing rules

The implementation should add a source flag only after the shared framework is planned for that threat.

## Cleanup and invalid scopes

- annexed attackers retain historical responsibility through stored original actor where possible
- dead victim tags do not break evidence or death logs
- state ownership change does not erase contamination
- latent Condemnation clears only after expiry or full resolution
- sanction pairs clean when tags die or diplomacy changes
- selected targets and event targets clear after operation completion

## Acceptance criteria

- one chemical action cannot be counted twice at full value
- deaths reduce real population and appear in the shared log
- contamination updates Air Cleanliness by class changes
- attribution can evolve from hidden to confirmed
- confirmed use has a Condemnation floor
- retaliation is recognized without creating immunity
- treaty status affects diplomacy, not production legality
- sanctions change material access and foreign support
