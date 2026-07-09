# System Camp Repression Rework Spec, Part 1: Shared Core Loop

Working feature id: `system_camp_repression_rework`

Working feature name: Camp, Repression, and Atrocity Consequences Rework

This is a system-level Chaos Redux rework. It should live under `docs/specs/system_camp_repression_rework_specs/` if accepted as source design. Implementation files should stay in the existing `genocide_crisis`, `chaos_meter`, `germany_mengele`, country decision, AI, and documentation file families unless a narrow helper split is clearly justified.

## Playable promise

The system should feel present in the campaign without harassing the average player. A country that does not invest in repression infrastructure should see almost nothing beyond rare historical context, discovery, or AI-created consequences. A country that expands the network should enter a pressure system with immediate coercive gains, real state-population damage, growing resistance, institutional rot, supply strain, evidence risk, and possible collapse.

The player should understand the central bargain:

- detention and forced-labor networks can create construction, resource, compliance-control, or hardliner pressure;
- each expansion damages population, stability, local compliance, legitimacy, and future discovery severity;
- radicalized atrocity escalation is not a better version of forced labor;
- large networks become unstable systems that demand resources, guards, trains, administration, concealment, and suppression;
- discovery, defeat, or regime change turns hidden damage into condemnation, sanctions, foreign reaction, and tribunal pressure.

## Existing system to preserve

The current implementation already has:

- `concentration_camp`
- `extermination_camp`
- `gulag_labor_camp_network`
- `genocide_responsible_country` state storage
- `global.genocide_active_camp_states`
- monthly processing through `genocide_monthly_global_pulse`
- state population loss through the Chaos Meter Deaths pipeline
- discovery on state-control change
- condemnation thresholds
- Germany, Japan, and Soviet country-specific branches
- Mengele integration through Auschwitz state `88`

The rework should deepen that structure instead of creating a second competing system.

## Mechanical state pools

The system should never ask the player to select protected populations. Targeting is represented by state and sovereignty conditions.

Priority order for population loss and repression effects:

1. Occupied non-core states controlled by the responsible country.
2. Colonial or subject territory controlled through the responsible country's empire or subject network.
3. Non-core integrated states owned or controlled by the responsible country.
4. High-repression borderland or periphery pools defined by country-specific scripts.
5. Core states only when no non-core, occupied, colonial, or periphery pool exists.

Core-state fallback should be a bad outcome. It should produce lower forced-labor output, lower coercive utility, stronger stability loss, stronger legitimacy loss, and higher internal revolt pressure. A regime using core-state pools is cannibalizing its own state capacity.

## Network phases

### Dormant historical infrastructure

Dormant sites are historical or political markers. They do not produce monthly deaths, recurring popups, or discovery spam.

Used for:

- prewar Germany early concentration-camp infrastructure;
- Japan's Manchurian and colonial security apparatus;
- Soviet gulag and forced-labor background;
- colonial detention or labor systems in the Raj, North Africa, Libya, Congo, and other empire regions.

Dormant sites become active only when the country escalates through decisions, focuses, war conditions, paranoia, occupation, or AI historical packages.

### Active detention and forced-labor network

This is the base playable layer. It gives modest coercive control and labor pressure while slowly damaging the population and legitimacy.

Core effects:

- small monthly Deaths-tab movement;
- state population loss through existing `chaos_meter_register_deaths` helpers;
- local compliance growth damage;
- short-term resistance suppression or garrison relief;
- growing resistance pressure once `network_reach` and `evidence_level` rise;
- modest construction, resource extraction, or local output pressure;
- democratic legitimacy damage if the country is democratic or has democratic support above a threshold;
- extremist hardliner pressure for fascist, Stalinist, or chaos-doctrine routes.

### Expanded labor network

This is where the system becomes a real management layer. The country can expand the labor network through decisions that cost trains, support equipment, infantry equipment, manpower, command power, civilian-factory burden, and stability.

Outputs:

- stronger building speed, infrastructure repair, resource extraction, or military construction in selected regions;
- stronger ideology or hardliner pressure for extremist regimes;
- stronger colonial control for empires;
- stronger short-term compliance suppression.

Costs:

- larger monthly state-population loss;
- `stability_damage`;
- `resistance_pressure`;
- `network_overstretch`;
- `guard_manpower_burden`;
- `rail_and_train_burden`;
- `evidence_level`;
- `condemnation_on_discovery`.

### Radicalized atrocity escalation

This phase uses existing extermination-site infrastructure but reframes it as a liability-heavy crossing point. It is not an economy upgrade.

It can:

- increase extremist hardliner lock-in;
- increase racial policy radicalization for regimes already using such routes;
- increase fear-based short-term control;
- accelerate country-specific hidden mechanics such as Mengele autonomy.

It must also:

- cause severe monthly Deaths-tab movement;
- sharply damage state population;
- increase resistance and refugee pressure;
- reduce stability and democratic support;
- increase supply strain, guard burden, and railway burden;
- create high discovery condemnation;
- increase tribunal severity;
- increase coup, lab revolt, collapse, or internal reckoning risk.

### Restricted contaminated-site escalation

This replaces the requested "more efficient killing" direction with a contaminated-site liability branch.

Requirements:

- active radicalized atrocity, experiment-linked, gulag, or restricted chemical site;
- relevant special project or chemical capability already present in Chaos Redux;
- stockpile cost through existing chemical-cylinder logic where available;
- evidence not already destroyed;
- strong AI limits.

Effects:

- consumes stockpile and logistics capacity;
- adds immediate Deaths-tab movement;
- marks the state as contaminated evidence;
- registers monthly processing;
- increases `evidence_level`, `hidden_atrocity_score`, `condemnation_on_discovery`, and `tribunal_severity`;
- adds accident or spread risk;
- can trigger internal breakdown or foreign intelligence pressure.

It should not reduce resource costs of killing or provide efficiency curves. Any "efficiency" is represented only as the regime creating more severe evidence, contamination, and collapse pressure with fewer visible conventional economic benefits.

## Shared values

All values should use script constants or documented dynamic helper effects.

Core national values:

- `camp_network_reach`: total active network size.
- `camp_labor_output`: forced-labor pressure that supports construction or extraction.
- `camp_coercive_control`: short-term control pressure.
- `camp_population_loss_index`: current monthly damage pressure.
- `camp_resistance_pressure`: future unrest, sabotage, and occupation resistance.
- `camp_stability_damage`: national stability and legitimacy burden.
- `camp_evidence_level`: discovery severity stored on country and states.
- `camp_overstretch`: administrative, guard, supply, and rail strain.
- `camp_foreign_visibility`: chance that diplomats, enemies, exiles, and liberated states create evidence.
- `camp_tribunal_severity`: post-defeat accountability value.
- `camp_hardliner_pressure`: extremist faction pressure or ruling-party lock-in.
- `camp_democratic_legitimacy_damage`: special penalty for democratic or semi-democratic governments.
- `camp_reform_pressure`: pressure for dismantle, inspection, compensation, or postwar reckoning.

State values and flags:

- active site type;
- responsible country;
- evidence depth;
- monthly death pressure;
- local labor output;
- local resistance pressure;
- local foreign observer exposure;
- destroyed evidence state;
- failed cover-up state;
- liberated evidence state;
- experiment-linked site state;
- contaminated evidence state.

## Decision rhythm

The category should stay hidden unless the country has a meaningful action.

Visible action families:

- show or hide managed network decisions;
- expand labor network in eligible state pool;
- redirect labor to construction, extraction, military works, or occupation control;
- increase guard allocation;
- reduce guard allocation to free manpower;
- inspect and dismantle sites;
- reform or compensate after regime change;
- destroy evidence during retreat;
- suppress large-network breakdown;
- manage famine, deportation, or overreach crisis for Soviet routes;
- country-specific routes for Germany, Japan, Britain, United States, France, Italy, Belgium, and generic dictatorships.

No recurring "leaked files" or minor flavour events should fire from ordinary monthly processing. The system should reserve popups for threshold changes, large-network breakdown, discovery, liberation, collapse, trial, and major country-specific milestones.

## Population loss model

The implementation should use dynamic state population and state context rather than fixed tiny values.

Factors that increase monthly loss:

- network reach;
- radicalized escalation;
- experiment-linked site;
- contaminated site;
- high permission or autonomy values in country-specific chains;
- occupied or non-core status;
- harsh labor quota decisions;
- famine pressure;
- low stability;
- high chaos tier;
- resistance suppression intensity;
- failed cover-up or retreat action.

Factors that reduce monthly loss:

- dismantle or reform actions;
- inspection and relief decisions;
- medical containment for contaminated or biowarfare-linked sites;
- stable supply;
- high local compliance without harsh labor quotas;
- democratic reform route;
- postwar occupation or liberation control.

Deaths must visibly move the Chaos Meter Deaths tab and real state population when the network is expanded. The base dormant and low network should be light enough to stay background. Large networks should become visible in the global death count and in state manpower reduction.

## Average-player invisibility

The average player should not see a management wall.

Rules:

- dormant historical sites stay quiet;
- base construction can exist without popups;
- generic categories appear only with actionable upgrades, reforms, evidence destruction, or large-network crisis;
- country-specific categories use show/hide decisions;
- AI actions do not spam the player unless they cause discovery or major world reaction;
- threshold popups are bounded per country or per site type;
- the Deaths and Condemnation tabs carry routine information instead of repeated events.

## Dismantlement and reform loop

Every country that can expand the system must have a route to dismantle it.

Dismantling should:

- remove active monthly death registration;
- reduce labor output and coercive control;
- reduce hardliner pressure;
- recover stability slowly;
- lower future discovery severity if evidence is preserved and inspections are accepted;
- increase short-term resistance or hardliner anger for extremist regimes;
- create postwar or regime-change reckoning content.

Democracies and post-authoritarian regimes should get stronger reform tools. Fascist, Stalinist, and chaos-doctrine routes should face hardliner backlash and possible coup or purge pressure when dismantling large networks.

## Discovery loop

Discovery remains physical and evidence-based.

Triggers:

- enemy captures state with undiscovered evidence;
- responsible country capitulates;
- regime changes and opens records;
- postwar tribunal begins;
- foreign observers have high visibility and survivor networks reach a threshold;
- contaminated or experiment-linked site is discovered.

Discovery effects:

- mark state as discovered;
- calculate condemnation by site type, evidence depth, repeat discovery decay, contaminated site, experiment site, and network reach;
- apply condemnation to stored responsible country;
- fire bounded discoverer and responsible-country events;
- fire global news only for first severe discovery per responsible country or first radicalized/extermination evidence;
- trigger country-specific foreign reactions;
- raise tribunal severity and refugee pressure.

## Chaos Redux integration

All deaths route through the shared Deaths pipeline.

All hidden deaths must:

- record civilian deaths;
- reduce state population through `add_manpower` negative deltas;
- update country totals;
- add chaos by the existing deaths-to-chaos rule.

Condemnation should continue using the existing condemnation path that integrates with the Chaos Meter Condemnation tab.

World-end scenario hooks should remain indirect. This system can help raise chaos and create world threats, but a camp network itself should not become a world-end scenario unless a country-specific chain, such as the Mengele Directorate, reaches its own terminal world-order route.
