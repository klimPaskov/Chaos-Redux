# Great Depression 2.0 specification, part 6: Evolution II, Social Collapse

## Evolution role

The action, mission, incident, and stage labels in this file are structural working labels unless they come directly from the accepted brief. Final player-facing wording belongs to implementation.

Baseline Event 35 already permits ordinary strikes, radicalization, government crises, and a rare generic civil conflict after the National Breakdown gate. Social Collapse expands that compact failure route into a direct political and social struggle. It adds organized strikes, factory occupations, riots, defined radical movements, mutinies, emergency governments, coups, separatist pressure, and a richer civil-conflict path.

The evolution does not make civil war inevitable. Severe outcomes require long economic failure, weak institutions, an organized movement, and failed response. A country can recover economically while changing government, labor institutions, ownership, or regional relations. When this module is active, it owns the political incident ladder and suspends the simpler baseline breakdown chain so outcomes cannot duplicate.

Evolution II normally includes Financial Contagion when Evolution I is enabled. The project settings remain authoritative. A disabled lower evolution stays disabled and is not silently activated by Evolution II.

## Availability and activation

Social Collapse becomes available at Chaos Tier.

Normal active-event activation should require:

- Event 35 is active.
- Evolution II is enabled.
- The country has spent a sustained period in Depression, Deep Depression, or Systemic Breakdown.
- Social and institutional stress is material.
- The evolution has not already been recorded for the episode.
- The dynamic evolution delay has elapsed.

A base timing target near `120` days is appropriate under strong conditions.

Activation accelerators:

- Severity above `80`.
- Several Distressed, Idled, or Shuttered centers.
- Low or falling stability.
- Repeated mission failure.
- Harsh austerity or liquidation at high unemployment.
- Selective strategic rescue that abandons other regions.
- Failed relief or public works.
- Repression or exposed corruption.
- Famine or migration pressure from a valid shared context.
- An Event 34 Evolution II collapse with fragile Miracle Regions.

Activation reducers:

- Reopened centers.
- Successful employment programs.
- High stability.
- A negotiated labor settlement.
- Effective relief.
- Low Severity and improving trend.
- A government with strong institutional legitimacy.

An inherited Event 34 Evolution II collapse activates enabled Evolutions I and II immediately. Disabled lower modules remain off.

Evolution activation adds zero Chaos.

## Hidden social-strain model

The event may track `Social Strain` internally. It is not a second public number. The category shows a qualitative social condition and the strongest cause.

Suggested conditions:

- Contained Discontent.
- Organized Protest.
- National Unrest.
- Government Crisis.
- Revolutionary Breakdown.

Social Strain rises through:

- High Severity and duration.
- Unemployment in the same centers.
- Hunger, famine, or housing pressure from an exact registered source.
- Failed relief.
- Factory liquidation.
- Wage, contract, or pension failure.
- Unequal strategic rescue.
- Repression.
- Political exclusion.
- Failed government response.
- Existing radical party or movement strength.
- Regional identity where an abandoned center is concentrated.

It falls through:

- Employment and public works.
- Reopened centers.
- Negotiated settlements.
- Credible social insurance or relief.
- High stability.
- Political inclusion.
- A successful emergency government with a defined mandate.
- Recovery progress.

The implementation should rebuild the qualitative state from hidden pressure and current incidents. It should not show a raw social score.

## Movement formation

Social Collapse can create one primary organized movement and, in a large or fragmented country, one secondary rival. It should not generate many interchangeable factions.

Movement type depends on:

- Current ideology and ruling institutions.
- Existing party popularity.
- Labor organization and route history.
- Regional identity.
- Military discontent.
- Recovery doctrine.
- Foreign influence.
- Prior civil conflict.

Possible movement families:

- Trade-union and social-democratic coalition.
- Communist council movement.
- Syndicalist or factory-occupation movement.
- Nationalist or fascist mass movement.
- Military emergency faction.
- Monarchist or traditional-authority restoration group.
- Regional autonomy or separatist movement.
- Business and creditor emergency coalition.
- Rural protest movement when agricultural and famine pressure is valid.

The event should use existing parties, leaders, characters, and regional identities when they exist. It must not invent a historical person or grounded portrait merely to fill a movement role. A council or institution can represent a movement when no valid person exists.

## Incident ladder

### Stage 1: Organized protest

Possible incidents:

- Local strike committee forms.
- Unemployed workers organize a march.
- Factory owners close a plant during a wage dispute.
- Municipal relief offices are overwhelmed.
- Veterans or soldiers demand employment.
- A regional council refuses a national retrenchment order.

Gameplay:

- Small stability or production pressure.
- One visible response decision.
- A chance to negotiate before the movement hardens.

### Stage 2: Sector conflict

Possible incidents:

- Rail, mining, port, or armament strike.
- Factory occupation.
- Coordinated refusal of layoffs.
- Business lockout.
- Large relief demonstration.
- Security force refusal or sympathy.

Gameplay:

- State or sector production loss.
- Timed negotiation, relief, or enforcement objective.
- Movement support and government legitimacy consequences.

### Stage 3: National unrest

Possible incidents:

- General strike.
- Nationwide factory occupations.
- Hunger riots tied to a valid food crisis.
- Mutiny or refusal of orders.
- Emergency cabinet collapse.
- Rival movements fighting for control of relief or workplaces.

Gameplay:

- Strong national penalties.
- Emergency government or national settlement choices.
- Higher risk of coup, regional break, or civil conflict after failure.

### Stage 4: Government crisis

Possible incidents:

- Cabinet loses authority.
- Parliament or ruling council cannot pass a recovery program.
- Army leadership demands emergency powers.
- A movement establishes parallel administration in one or more centers.
- Regional authorities threaten secession.
- A foreign patron conditions aid on government change.

Gameplay:

- Leadership or government route decision.
- Strict timed objective.
- Potential ideology, law, leader, council, or autonomy change.

### Stage 5: Revolutionary breakdown

Possible outcomes:

- Coup attempt.
- Limited regional uprising.
- Separatist conflict.
- Full civil war.
- Negotiated transfer of power.
- Emergency dictatorship.
- Revolutionary coalition government.

This stage requires the full extreme-outcome gate. It is never selected from one high Severity check.

## Response families

The category shows only responses relevant to the current incident and government.

### Negotiate with Strike Committees

Commits political authority, relief, and policy concessions. It can end strikes and reduce social pressure. It may strengthen labor institutions, reduce owner confidence, or change the recovery doctrine.

### National Employment Compact

Combines public works, wage support, and industrial reopening into one national settlement. It has high civilian and fiscal costs and can create a durable social institution.

### Deploy Security Forces

Uses command power, equipment, manpower, and stability risk. Command power remains conservative and never exceeds the project limit. The action can restore control quickly, but may create deaths, radicalization, condemnation from another valid system, and longer social scars.

Any civilian loss must use the shared exact population and Deaths contracts. Event 35 must not subtract population through a duplicate path.

### Break the Occupations

Targets occupied factories or a center. It may use negotiation, legal action, police, military units, or owner concessions according to government type. A forceful solution can damage the state or production.

### Recognize Workplace or Regional Councils

Shares authority with organized local bodies. It reduces immediate strain and can move the country toward a new political settlement. It may weaken central control or alter ideology support.

### Form an Emergency Government

Creates a coalition, military cabinet, royal ministry, planning council, or other government form supported by current institutions. It grants temporary crisis authority and starts a mandate mission.

The emergency government must have a clear end condition. It can return power, become permanent through a visible route, fail, or trigger opposition.

### Nationalize or Socialize Occupied Industry

Available where politics and doctrine support it. It can resolve occupations and protect production. It changes ownership, foreign relations, and long-term institutions.

### Guarantee Property and Credit

Available to governments seeking business support. It can end lockouts and restore finance while increasing public rescue costs and labor opposition.

## Government and ideology variants

The route logic uses current institutions without turning every ideology into the same event with renamed buttons.

### Democratic and parliamentary governments

Likely tools:

- Coalition cabinet.
- Labor negotiation.
- Public works and social insurance.
- Emergency legislation with an expiry.
- Election or confidence vote.

Main risks:

- Cabinet fragmentation.
- Radical opposition.
- Permanent emergency rule.
- Foreign creditor pressure.

### Communist governments

Likely tools:

- State planning.
- Workplace councils.
- Party discipline.
- Nationalization.
- Conflict between central planners and independent labor movements.

Main risks:

- Rival council or syndicalist power.
- Purge and repression.
- Regional resistance.
- Administrative failure.

### Fascist governments

Likely tools:

- Corporatist agreements.
- Strategic rescue.
- Compulsory labor or production controls.
- Paramilitary or police response.
- Business-state bargaining.

Main risks:

- Violent repression.
- Rival radical factions.
- Military intervention.
- Collapse of corporatist promises.

### Nonaligned, monarchist, or military governments

Likely tools:

- Royal or presidential commission.
- Patronage relief.
- Military cabinet.
- Conservative labor settlement.
- Provincial bargaining.

Main risks:

- Palace or officer coup.
- Regional separatism.
- Weak party legitimacy.
- Dependence on one institution.

These are design tendencies. AI and player options must remain sensitive to the actual country, party support, characters, laws, and campaign state.

## Political transformation

A country may recover under a transformed government.

Supported outcomes include:

- Negotiated social settlement.
- Reformed parliamentary government.
- Corporate or creditor government.
- State-planning administration.
- Military emergency regime.
- Revolutionary council government.
- Restored monarchy or traditional authority where a valid route exists.
- Regional autonomy settlement.
- Fragmented or civil-war aftermath.

A transformation needs visible steps, valid leaders or institutional identities, localisation, portraits when a real character changes, AI strategy, and cleanup. The event must not perform a silent ideology swap from one incident.

## Extreme-outcome gate

A coup, separatist conflict, or civil war requires all relevant conditions:

- Social Collapse is active.
- Severity has remained very high for a sustained period.
- Social condition has reached Government Crisis or Revolutionary Breakdown.
- Stability is very low or government legitimacy has failed.
- A valid organized movement exists.
- At least one major response or mandate mission failed.
- No recent civil war or protected aftermath blocks another conflict.
- Valid states and actors exist.
- The movement can receive a coherent territory and force package.

A starting target near Severity `90` for at least `90` to `120` days is reasonable. Exact values need tuning.

## Coup design

A coup is used when the movement has elite or military support but lacks a coherent regional base.

The coup can:

- Replace the leader or cabinet.
- Change ruling party or law.
- Install an emergency national spirit with a lifecycle.
- Start a legitimacy or mandate objective.
- Fail and strengthen another movement.

A coup should not create a civil war automatically unless the country has a valid opposing base and the coup failure opens that branch.

## Separatist design

Separatism requires:

- A valid regional identity or existing tag.
- One or more Depression Centers in the region.
- Long abandonment, unequal rescue, or repression.
- Enough state control and organization to create a viable actor.

The event must use existing country-carrier and tag rules. It does not invent a new tag in the planning stage. A separatist route needs territory, capital, forces, equipment, leader or council, flag, localisation, AI, claims, diplomacy, and later settlement. If those cannot be supplied, use autonomy or regional crisis instead of a fake country.

## Civil-war design

A full civil war is the rare failure outcome.

Rules:

- Territory follows organized support, Depression Centers, regional identity, and current control.
- The split should not default to half the country.
- Starting forces and equipment scale from the states and movement.
- The original Event 35 crisis is divided through the state-transfer contract.
- Both sides receive only the economic burden they actually control.
- The war uses the shared generic Chaos and deaths systems. Event 35 does not duplicate those changes.
- Victory does not automatically end depression.
- Postwar recovery and reconciliation remain necessary.

## Strike and occupation missions

### Restore Essential Production

Goal:

- Resolve one strike or occupation in a named center.
- Keep basic supply and transport working.
- Choose negotiation or force.

Success restores part of local output. Failure raises social condition and can widen the action.

### Prevent a General Strike

Goal:

- Reach a settlement with major sectors.
- Keep Severity below the emergency threshold.
- Reopen or protect at least one center.

Duration target: `90` to `150` days.

### Emergency Government Mandate

Goal depends on government form:

- Pass a recovery program.
- Restore center operation.
- Reduce Severity.
- Avoid repression or opposition thresholds.
- Prepare a return to ordinary government or a visible permanent transition.

Failure opens leadership crisis, coup, or civil-conflict branches when valid.

## Humanitarian connections

Economic depression can worsen humanitarian conditions, but Event 35 does not invent famine, migration, or deaths through unsupported shortcuts.

Use shared adapters when:

- A state already has food pressure.
- Long unemployment and blockade create a valid famine context.
- A center's closure creates a registered migration or exodus pressure.
- Repression or riot resolution creates an exact civilian loss.

Event 35 supplies source, state, actor, and pressure proof. The humanitarian system owns food stages, migration cohorts, exact transfers, deaths, and cleanup.

## Chaos impact

Social Collapse activation adds zero Chaos.

Concrete event-owned outcomes may add guarded Chaos when generic systems do not already cover them:

- First nationwide general strike that paralyzes several centers.
- A government falls through the Event 35 crisis.
- A parallel administration takes durable control.
- A rare non-war political breakdown spreads to another country.

Civil war, ideology change, deaths, annexation, and state transfer already use shared generic sources. Event 35 does not add a second change for those outcomes.

A negotiated settlement can remove only the matching Event 35 one-shot pressure that its earlier outcome added. Ordinary repression or recovery does not subtract generic Chaos.

## Resolution and aftermath

Social Collapse resolves when:

- The primary movement is settled, defeated, integrated, or transformed into government.
- No national strike, occupation, coup, or civil-conflict objective remains.
- Severity is below the social emergency range.
- A proof period passes without a new organized breakdown.

The country keeps one coherent political aftermath where earned:

- Social compact.
- Emergency rule.
- Planning settlement.
- Corporate rescue order.
- Labor scar.
- Regional autonomy.
- Post-civil-war reconstruction.

The aftermath must interact with future Event 35 episodes and current government. It should not remain as an unexplained permanent modifier.

## AI behavior

AI response considers:

- Severity and trend.
- Stability.
- Movement type and support.
- Current ideology and government.
- War state and army loyalty.
- Available civilian capacity.
- Repression cost and risk.
- Foreign aid and patron pressure.
- Recovery doctrine.
- Probability of settlement.
- Territory and civil-war validity.

AI should negotiate when a settlement is affordable and movement support is broad. It may use force when the state is strong, the movement is small, and vital wartime production is threatened. It should avoid a doctrine or response that predictably triggers civil war when a safer route exists.

## Disabled evolution behavior

If Social Collapse is disabled:

- No organized social-strain incident ladder activates.
- Baseline strikes, radicalization, government crises, and the guarded National Breakdown chain remain available.
- No Evolution II factory-occupation system, coup route, separatist country, movement-specific civil war, or political transformation package is created.
- A rare baseline generic civil conflict can still occur after its own full gate and failed prevention objective.
- Event 34 inherited Evolution II still affects starting Severity and state conversion.
- Financial Contagion remains active only if its own evolution is enabled.
- Baseline recovery remains complete and valid.
