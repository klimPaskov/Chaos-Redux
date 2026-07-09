# System Camp Repression Rework Spec, Part 4: UI, AI, Assets, Achievements, and Acceptance Criteria

## UI and presentation

The system should primarily use decision categories and scripted localisation. A custom scripted GUI is optional but recommended after the first implementation tranche if decision-category text becomes too dense.

### Decision category header

Every active country category should show a compact ledger:

- Network Reach.
- Labor Output.
- Population Loss.
- Stability Drain.
- Resistance Pressure.
- Evidence Depth.
- Discovery Risk.
- Guard and Rail Burden.
- Dismantlement Progress where relevant.

Use coloured scripted localisation for each value. The tooltip should show the components that moved the value recently.

### Optional custom GUI: Repression Ledger

A future GUI can show:

- state cards for active sites;
- filter for labor, experiment, gulag, contaminated, discovered, destroyed evidence;
- country values;
- selected state details;
- dismantle and guard buttons;
- warning frame when network is very large;
- discovery evidence seal;
- Deaths and Condemnation summary.

The GUI should be hidden for countries without active sites or active reform work.

### Popups

Do not create frequent flavor popups.

Use popups for:

- first active expansion;
- first radicalized escalation;
- large network breakdown;
- contaminated-site escalation;
- major discovery;
- first tribunal threshold;
- Germany Mengele autonomy threshold;
- Japan Ishii independence threshold;
- Soviet famine crisis threshold;
- colonial revolt threshold;
- dismantlement completion.

## AI principles

AI should use the system where historically and mechanically appropriate, but with caps.

AI should not randomly build extermination sites without ideological, war, occupation, crisis, or country-specific triggers.

AI should consider expansion if:

- authoritarian or extremist ideology;
- active major war;
- occupied high-resistance territory;
- historical country package active;
- high paranoia for Soviet Union;
- war with China for Japan;
- fascist Germany at war and controlling Poland/Auschwitz;
- colonial empire managing rebellion;
- chaos doctrine route unlocked.

AI should avoid or dismantle if:

- democratic government;
- recent discovery;
- high condemnation;
- losing war and enemies near evidence sites;
- low manpower or train shortages;
- high stability damage;
- postwar reform route;
- regime changed away from extremist path.

## Country AI caps

### Germany

- Very likely to activate occupied Poland administration after 1939 if fascist and at war.
- Very likely to escalate around Auschwitz after 1940 if controlling state `88`.
- More likely to transfer prisoners to experiment sites if Mengele permission is high.
- Uses evidence destruction if enemies approach active sites.
- Does not dismantle unless non-fascist, under military review route, or facing collapse.

### Japan

- Uses forced labor and reprisal systems only during China or major occupation wars.
- Uses Ishii and biowarfare experiment decisions if researching or owning biowarfare projects.
- High Kwantung autonomy makes escalation more likely.
- Uses evidence destruction or evacuation if Soviets or Allies approach Manchuria.
- Avoids extermination-style escalation unless chaos doctrine or desperation makes it valid.

### Soviet Union

- Expands gulags under Stalinist or high-paranoia conditions.
- Uses grain confiscation and deportations when paranoia, war, and borderland resistance are high.
- Can use repression during Union Crisis to buy time.
- Stops receiving meaningful suppression relief at high crisis thresholds.
- Dismantles or reforms after de-Stalinization, reformist route, or post-collapse successor decisions.

### United Kingdom

- Uses Raj detention lightly and mostly during world war.
- Expands only if Raj autonomy pressure, war crisis, or rebellion risk is high.
- Reforms or dismantles after war, decolonization pressure, or democratic scrutiny.

### United States

- Rarely uses relocation authority.
- Can activate under Pacific war, homeland fear, or high chaos.
- Prefers court review and termination after threat falls.
- AI should not use it as economy optimization.

### France

- Democratic or Free France reforms and dismantles.
- Vichy can expand Gurs and North Africa labor networks.
- France should not build a Germany-style extermination system unless it has an extreme chaos doctrine route.

### Italy

- Expands colonial repression if fascist and controlling Libya or East Africa.
- Uses colonial road, fort, and supply projects.
- Dismantles or loses access after colonial defeat or regime change.

### Belgium

- Uses Congo extraction if colonial empire remains.
- Expands resource labor under war or exile economy pressure.
- Reforms or loses system after decolonization pressure, discovery, or democratic reckoning.

## Assets

Required or recommended assets:

- decision category icon for Repression Ledger;
- decision icon for expand labor network;
- decision icon for guard allocation;
- decision icon for dismantle network;
- decision icon for evidence destruction;
- decision icon for inspection or tribunal;
- idea icon for active forced-labor network;
- idea icon for colonial labor burden;
- idea icon for democratic legitimacy damage;
- idea icon for gulag authority;
- idea icon for famine pressure;
- idea icon for Ishii influence;
- idea icon for Mengele laboratory autonomy;
- report images for discovery events;
- news images for first severe discovery;
- super-event images only for major thresholds.

Asset source rules:

- real historical leaders and real flags must be sourced, not generated;
- fictional UI, idea, decision, and symbolic super-event art can be generated;
- report images for fictional alternate-history discoveries can be generated in period documentary style;
- no generated readable text;
- all final assets need DDS files, manifests, and GFX handoff notes.

## Super-event candidates

Use super-events sparingly.

Candidate roles:

- Global Atrocity Evidence Discovery: first severe discovery of radicalized sites by enemy liberation.
- Angel of Death Directorate Revolt: if the Mengele coup fires.
- Soviet Famine Catastrophe: if famine pressure reaches critical level during war or Union Crisis.
- Pingfang Exposure: if Allied or Soviet forces discover Japan's major biowarfare experiment network.
- Colonial Reckoning: if a colonial empire's labor network is exposed after a major war or decolonization crisis.

Each super-event needs separate quote, cultural remark, audio, image, and source research. The planning package does not provide final super-event localisation.

## Achievements

Achievements should reward mastery, dismantlement, exposure, survival, reform, containment, or defeating dangerous blowback. They should not reward maximizing atrocities or optimizing killing.

Working achievement concepts:

- dismantle a large inherited network while staying at war and preventing civil collapse;
- liberate and document several severe sites before the responsible country capitulates;
- as Germany, authorize the Auschwitz program, then crush the Directorate revolt and dismantle the laboratories;
- as Japan, remove Ishii from program control after exposing the network internally and prevent a major outbreak;
- as the Soviet Union, survive Union Crisis without famine reaching critical pressure;
- as the U.K., keep the Raj loyal while dismantling the detention network and avoiding colonial revolt;
- as the U.S., end relocation authority and complete redress before war's end;
- as Belgium, reform the Congo concession system before international exposure;
- as Italy, abandon colonial camps and hold Libya through conventional garrison and infrastructure reform;
- as France, dismantle Vichy camp legacy and prevent a tribunal severity spike.

## Implementation acceptance criteria

A completed implementation must satisfy every criterion below.

### Shared system

- Existing `concentration_camp`, `extermination_camp`, and `gulag_labor_camp_network` are preserved or migrated without duplicate building definitions.
- All active sites store `genocide_responsible_country`.
- All monthly deaths use the Chaos Meter Deaths pipeline.
- Deaths reduce real state population.
- Routine processing does not fire recurring minor flavor popups.
- Discovery remains evidence-based and physical.
- Condemnation is not passive before evidence, except for explicit public chemical or biological attacks already handled by Chaos Redux.
- Large networks create meaningful stability, resistance, supply, and guard burden.
- Dismantlement and reform routes exist.

### Safety boundaries

- No player-operated protected-class target selector exists.
- No chemical or biological efficiency curve for killing exists.
- Restricted chemical escalation is a contaminated evidence and consequence branch.
- Historical persecution is represented through evidence, route context, AI history, and aftermath, not player target menus.

### Country packages

- Germany uses Auschwitz state `88` and existing Mengele variables.
- Germany prisoner transfers use occupied/non-core pools before core fallback.
- Japan uses China and Manchuria pools, Shiro Ishii influence, and biowarfare research risk.
- Soviet Union uses paranoia, gulag reach, famine pressure, and Union Crisis bridge.
- U.K. has Raj and dominion-control integration.
- U.S. has democratic emergency relocation with large legitimacy penalties.
- France handles democratic, Vichy, Free France, and North Africa routes.
- Italy handles Libya and colonial repression.
- Belgium handles Congo extraction and reform.
- Generic route exists but is conservative and gated.

### AI

- AI weights are country-specific and state-aware.
- AI has caps so it does not overuse the system.
- AI does not use invalid targets.
- AI dismantles or reforms when its route changes.
- AI evidence destruction only appears near enemy approach and undiscovered evidence.

### UI and documentation

- Decision category text shows current values.
- Tooltips explain nonstandard costs.
- Localisation is written as in-world text and does not expose hidden variables directly.
- System docs are updated.
- Event catalog spreadsheet is updated only after implementation facts exist.
- Asset manifests exist for every new final asset.

### Validation

- Check that active sites are registered exactly once.
- Check that stale decisions hide after dismantlement, discovery, capitulation, or regime change.
- Check that Deaths tab changes after monthly processing.
- Check that discoveries apply condemnation to the responsible country, not the discoverer.
- Check that Germany, Japan, Soviet, colonial, and generic AI can each find valid target states in at least one test scenario.
- Check that no recurring minor flavor popup fires from ordinary monthly site processing.
