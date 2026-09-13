# Event 067 Integrations, AI, Chaos, and Shared Systems

## Chaos impact philosophy

Event 067 should affect the Chaos Meter when an impossible commander appears, when military authority passes into his hands, when the government loses control, and when the crisis is durably contained.

Evolution eligibility and activation give zero Chaos. Generalissimo Influence movement gives zero Chaos by itself. Generic war, annexation, death, ideology, faction, nuclear, contamination, and world-tension sources remain owned by their shared systems.

Every Event 067 Chaos source uses a one-time milestone or a bounded sequence guard.

## Chaos impact map

The exact values are tuning anchors and must be centralized. The relative order and ownership are the accepted design.

### First manifestation

**Trigger**

The canonical Generalissimo is created through the normal event or manual scenario.

**Direction**

Small direct Chaos gain, suggested target `+2`.

**Reason**

An unknown man with impossible military ability has entered a national command structure.

**Guard**

Once per campaign.

### Supreme Command transferred

**Trigger**

The host first grants Supreme Command through a concession or demand.

**Direction**

Small direct Chaos gain, suggested target `+1`.

**Reason**

The armed forces have moved beyond ordinary government supervision.

**Guard**

Once per campaign.

### State institution captured

**Trigger**

The Generalissimo first gains direct control over internal security, armament boards, or an equivalent strategic institution during Evolution II.

**Direction**

Moderate direct Chaos gain, suggested target `+2`.

**Reason**

The officer network has become a parallel state.

**Guard**

Once for the first major institutional capture. Additional concessions do not repeat the source.

### Failed coercive removal

**Trigger**

Arrest, capture, assassination, or final removal fails and the revolt begins.

**Direction**

Moderate direct Chaos gain, suggested target `+3`.

**Reason**

A covert government operation has turned the national armed forces against the state.

**Shared-source rule**

The civil war's generic war source remains separate. Event 067 records the failed seizure of command, not the war declaration.

**Guard**

Once per revolt sequence.

### Peaceful seizure of government

**Trigger**

The government submits to the final ultimatum.

**Direction**

Moderate direct Chaos gain, suggested target `+3`.

**Reason**

A military commander has replaced or subordinated the government without a legal transition.

**Shared-source rule**

If the transition changes ideology, the generic ideology source can still apply. The Event 067 source records the military seizure itself.

**Guard**

Once.

### Junta captures the original capital

**Trigger**

The civil-war junta first gains and holds the original host capital after revolt setup.

**Direction**

Small or moderate gain, suggested target `+2`.

**Reason**

The military revolt has seized the center of the state.

**Guard**

Once. Recapture cycling cannot repeat it.

### Junta victory

**Trigger**

The Generalissimo defeats the original government and reunifies the country.

**Direction**

Moderate gain, suggested target `+3`.

**Reason**

The strongest commander in the world has converted a national army into a permanent military regime.

**Shared-source rule**

Do not duplicate annexation or civil-war casualty sources.

**Guard**

Once.

### International Command formed

**Trigger**

The world-end branch is active and the original Generalissimo forms a valid multi-country military bloc.

**Direction**

Moderate gain for history, suggested target `+2`.

**Reason**

Military governments have created an international command order.

**Guard**

Once.

### First foreign world-end coup

**Trigger**

The first eligible foreign country changes government through the world-end military-takeover route.

**Direction**

Small gain, suggested target `+1`.

**Guard**

First foreign coup only. Later coups use generic sources and world-end history without repeated Event 067 farming.

## Chaos reversals

### Peaceful early removal

**Trigger**

The Generalissimo retires or is dismissed before Evolution II and before the officer network becomes entrenched.

**Direction**

Small reduction, suggested target `-2`.

**Reason**

The state gives up an extraordinary military advantage and preserves civilian command.

### Prepared late removal

**Trigger**

The government permanently removes him after Evolution II without triggering revolt.

**Direction**

Moderate reduction, suggested target `-4`.

**Reason**

A mature parallel military state is dismantled.

### Government victory over the junta

**Trigger**

The original government wins the civil war and completes the first officer-network dismantling outcome.

**Direction**

Major reduction, suggested target `-5`.

**Reason**

The military seizure fails and the command network loses national power.

**Shared-source rule**

Peace, casualties, liberated territory, and ideology restoration remain separately owned.

### Civilian restoration during world end

**Trigger**

The Civil Authority Compact defeats the original Generalissimo regime or restores a major military government.

**Direction**

A bounded reversal recorded once for the first major restoration, suggested target `-3`.

**Guard**

No per-country repeat farming.

## Chaos exclusions

Event 067 gives no direct Chaos for:

- evolution activation
- evolution logging
- Influence crossing an abstract threshold
- routine accepted demands after the first institutional capture
- ordinary monthly Influence drift
- every division joining the junta
- every state changing control
- ordinary wars
- ordinary annexation
- generic deaths
- generic ideology change
- generic faction change
- Event 065 granting one Generalissimo trait

## Shared country classifiers

The Generalissimo and his junta are human.

Default classification:

- not an actual nonhuman country
- uses normal civilian systems
- not automatically a special Chaos country

The event should use Event 067 ownership flags and active actor registries for its own routing.

The shared `is_special_chaos_country` classifier should change only if implementation proves that the junta must be excluded from several unrelated civilian systems. A single Event 067 convenience check is not enough reason to classify it as special.

The junta remains eligible for famine, migration, population, occupation, condemnation, and ordinary diplomacy systems unless one of those owners has a specific valid exclusion.

## Script ownership

Event-owned validation belongs in Event 067 files.

Recommended owner surfaces:

- Event 067 scripted triggers for host validity, stage, removal, revolt readiness, country response, and world-end eligibility
- Event 067 scripted effects for character creation, command package, Influence updates, demands, removal, civil-war setup, country package, Cohesion, and world-end actor processing
- Event 067 script constants for thresholds, gains, costs, durations, probabilities, and strength bands
- Event 067 on-action adapters for event-driven state control, capitulation, government change, and war outcomes
- Event 067 decisions and category files
- Event 067 focus tree and focus inlay files

A helper belongs in `chaosx_dynamic_effects` or `chaosx_dynamic_triggers` only when several unrelated events or systems need the same neutral contract. Event 067 lifecycle, stage, validation, and country setup must not be placed in the shared registry.

## Runtime cadence and performance

The active host uses a bounded recurring hidden event or registered owner pulse. It should not add a whole-world `on_daily`, `on_weekly`, or `on_monthly` loop.

Event-driven hooks can respond to:

- capitulation
- state-control change
- civil-war start or end
- government change
- character transfer
- faction change

Every hook should perform a cheap Event 067 marker check before deeper logic.

World-end processing builds a roster once, then uses registered active arrays and delayed packets. Dead, annexed, resolved, or invalid countries leave the active roster.

## Event 065 Random Trait integration

The four Event 067 country-leader traits become part of the Random Trait pool.

Implementation requirements:

- stable family marker
- individual trait eligibility
- extreme-power classification for later Event 065 weighting
- no automatic Event 067 activation
- no Generalissimo character creation
- no command crisis
- no focus-tree loading
- no duplicate full trait package unless independent repeat rolls select it

Event 065 documentation and trait-pool selectors must be updated when the traits are implemented.

## Event 019 Soldiers from Nowhere integration

Event 019 and Event 067 cover different promises.

- Event 019 creates unbidden formations and claimant commanders.
- Event 067 creates one impossible supreme commander and a personal military-state crisis.

Rules:

- An Event 019 claimant can never be renamed or converted into the Generalissimo.
- Event 067 does not use Event 019 to create its canonical character.
- A valid claimant can support or oppose the Generalissimo through the Claimant Rival overlay.
- A host with an unresolved Event 019 takeover is normally invalid for Event 067 target selection.
- The world-end branch may use an Event 019 owner API for auxiliary claimant commanders only when that API is public and idempotent.
- Calling an Event 019 helper must not fabricate Event 019 history, evolution, or pacing entries.

## Event 039 Assassin Network integration

When an Event 039 intelligence network exists in the host or a valid allied country, it can support the assassination route.

Possible effects:

- improved preparation
- reduced personal-security reach
- better information on loyal officers
- a distinct failure consequence if the network is compromised

Event 067 must remain fully functional when Event 039 has not fired.

The manual Assassin Network scenario does not automatically start Event 067.

## Event 052 Intel Leaked integration

If the Generalissimo's network is exposed through Event 052 or another intelligence leak, the government can gain:

- temporary removal chance
- visibility into major hidden causes
- a cheaper officer rotation
- a chance to move arsenals before the next demand

The leak can also strengthen him when it exposes weak government countermeasures. The direction depends on whose files were compromised.

## Event 059 The Offensive integration

Aggressive AI behavior can increase the chance that a host uses the Generalissimo in major offensives. It should not directly add Influence.

Influence rises only when the host grants authority or achieves a valid Event 067 military outcome.

A Generalissimo-led junta can use the aggressive AI posture effectively, but Event 067 does not overwrite Event 059 ownership.

## Event 062 Allies Backstab integration

A host threatened by former allies has stronger reasons to grant national or Supreme Command.

Possible interactions:

- losing alliance war increases command-decision AI weight
- betrayal can start the Win the Campaign mission
- a former ally can support the junta or government based on relations and strategic interests

The event does not duplicate Event 062 wars or faction changes.

## Event 064 Border Fortifications integration

Fortifications already created by Event 064 remain attached to states and can benefit either side after revolt.

Government counterweight missions may prioritize fortified capital approaches. A Fortress Command junta can expand those defenses through its own route.

Event 067 does not recreate the world border-fortification effect.

## Event 066 Abundance integration

An abundance of military resources can change Event 067 costs and revolt setup.

Examples:

- abundant equipment lowers the practical cost of a loyal reserve
- abundant fuel makes Decisive Command more attractive
- abundant command power must not erase decision costs through negative or invalid values
- abundant military production can increase the Generalissimo's armament reach when transferred to him

Event 066 remains the owner of the abundance source.

## Event 131 Widespread Mutiny integration

Event 131 is currently unavailable in the supplied catalog and remains a separate future event.

When implemented:

- active mutiny can increase the Generalissimo's officer-network opportunity
- successful civilian command reform can reduce Event 131 risk
- The Generalissimos' World can increase Event 131 weighting or route its mutiny outcome toward aligned or rival juntas

Event 131 must not replace Event 067's personal crisis or canonical character.

## Military Preparation cluster integration

Event 067 is a High member.

The cluster should treat it as a powerful country-specific preparation event that can later become destabilizing.

Member rules:

- valid host required
- one worldwide target
- fire-once state respected
- no second pacing transaction
- cluster history shows Event 067 fired or skipped
- cluster firing does not grant an evolved opening unless current Chaos and evolution settings allow it

The current export mismatch is addressed in the catalog handoff.

## Event Logs integration

### History

The natural entry event records one Event 067 history row with the selected host as actor.

Important follow-up outcomes can appear in the selected event's detail history without pretending that they are new random events:

- Generalissimo permanently removed
- Supreme Command granted
- peaceful submission
- revolt begun
- government victory
- junta victory
- world-end branch begun

### Evolutions

Use one evolution track with a stable type identifier such as `generalissimo_ascendancy`.

Stages:

1. Supreme Command
2. State Within the State
3. The Generalissimo's Ultimatum

Each stage records:

- Event ID 067
- type
- stage
- Chaos tier
- host actor
- date and sequence through the shared logger

The Event Details evolution catalog shows premise and stage direction. It must not show fake history dates or sequence numbers.

### Events list

- Event ID appears as `067` in player-facing formatting where the UI uses padded IDs.
- Type is Minor Fire-Once.
- Chaos level is 1.
- The row shows `N/A` when no valid target exists.
- The event remains disabled by default until implementation and completion status justify adding it to the reworked-event allowlist.

### Cluster log

A Military Preparation cluster firing shows Event 067 as fired or skipped with the correct reason.

### Manual scenario

A scenario launch does not create a false natural event history entry. It can create scenario history and update Event Details state.

## Event Details integration

Event Details should include:

- event premise direction
- type
- Chaos level
- cluster and High member role
- current fired or unresolved state
- three evolution previews
- public world-end row for The Generalissimos' World
- independent world-end toggle
- no hidden removal formulas
- no secret future outcomes

The details text should explain that an exceptional commander can gain political control through military authority. It should not list raw bonuses.

## AI strategic archetypes

### Constitutional civilian government

Behavior:

- values the Generalissimo as a commander
- limits public promotion
- builds oversight and loyal reserve
- prefers retirement or dismissal while safe
- prepares before coercive removal
- refuses peaceful submission unless military defeat is otherwise likely

### Pragmatic wartime government

Behavior:

- expands command authority during serious war
- accepts selected military demands
- delays counterweights until immediate danger falls
- risks high Influence for survival
- begins removal preparation after victory

### Personalist ruler

Behavior:

- sees the Generalissimo as a rival
- may co-opt him briefly
- favors intelligence, arrest, or assassination
- can act earlier than a constitutional government
- may make a poor high-risk attempt when personal survival is threatened

### Military or authoritarian government

Behavior:

- accepts command authority readily
- favors officer appointments and budgets
- can accept peaceful submission
- prefers Officer Directorate or Personal Command after takeover

### Weak fragmented government

Behavior:

- alternates between concessions and failed restrictions
- has high coup risk
- avoids sophisticated removal without support
- may submit when the Generalissimo controls the army

### Defensive isolated government

Behavior:

- uses him for defense
- favors Theater or National Field Command
- builds fortifications and loyal reserve
- prefers managed coexistence

## AI decision principles

AI evaluates:

- current external war
- war direction
- army and equipment strength
- capital security
- Influence
- command authority
- removal chance
- government civil-war strength
- faction and subject support
- stability and war support
- political structure
- Generalissimo military value
- proximity to ultimatum

AI must not:

- attempt coercive removal at a near-zero chance without an emergency reason
- grant and revoke the same authority repeatedly
- spend resources it cannot afford
- expose invalid decisions
- create a loyal reserve without equipment
- choose a naval branch when landlocked
- choose an expansion route without targets or logistics
- support a foreign coup in a country already under military rule

## AI at the final ultimatum

The AI compares three paths.

### Submit

Positive factors:

- very high Generalissimo Influence
- weak loyal government army
- low stability
- military or authoritarian politics
- strong external enemy
- high expected junta victory chance

### Refuse

Positive factors:

- strong loyal reserve
- secure capital
- strong faction support
- high government legitimacy
- good equipment
- high chance to win the civil war

### Final removal

Positive factors:

- prepared operation
- high displayed success chance
- strong intelligence
- dispersed guard
- separated arsenals
- low tolerance for either submission or war

The AI should not select final removal without running the same chance calculation shown to the player.

## AI civil-war behavior

### Junta

- protect the Generalissimo
- secure the original capital
- connect command regions
- prioritize supply hubs and arsenals
- seek recognition and equipment
- avoid suicidal dispersal of elite forces
- use his field command directly

### Government

- defend the capital and replacement capital
- preserve the loyal reserve
- cut rebel regions apart
- retake arsenals and rail hubs
- seek faction support
- avoid exposing all forces to one front when external enemies remain

## AI post-takeover behavior

The route matrix in the focus-tree spec governs political, military, economic, and foreign choices.

AI should maintain Command Cohesion, complete postwar integration, and build forces through real resources before pursuing a major foreign route.

## AI world-end behavior

Country response and bloc behavior should use:

- government type
- stability
- army scale
- commander quality
- civilian command reforms
- war situation
- relations with the original Generalissimo
- regional ambition
- faction position
- subject status

Stable civilian powers should usually defend civilian rule. Weak military-heavy governments should usually accept or suffer military takeover. Strong military governments should often remain independent or rival the original Generalissimo.

## Multiplayer behavior

The normal event creates one Generalissimo worldwide.

- Player countries and majors share one target selection.
- Only the selected country's controller receives the main crisis decisions.
- Other players receive appropriate news or diplomatic reactions.
- A player who changes country control inherits the active country's visible Event 067 interface.
- The event does not create ghost copies for every player.
- The world-end branch processes all eligible countries through bounded packets.
- Scenario launch normally targets the current player when valid.

## Probability audit requirement

Every weighted surface must use the scenarios in `handoffs/067_generalissimo_probability_scenario_matrix.md`.

Required workflow:

1. `hoi4.probability_inspect`
2. named baseline scenarios
3. `hoi4.probability_evaluate` for decision and outcome pools
4. `hoi4.probability_sweep` for Influence, stability, and war-state boundaries
5. `hoi4.probability_compare` after every source change
6. `hoi4.probability_render` when a matrix or sensitivity view improves review
7. simulation only when the candidate pool and cadence are complete

The probability auditor remains read-only. The parent or owning implementation agent chooses the balance target and applies changes.
