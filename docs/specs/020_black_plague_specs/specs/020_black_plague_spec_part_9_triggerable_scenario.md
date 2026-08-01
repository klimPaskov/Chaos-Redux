# Event 20 Black Plague Specification, Part 9

## Triggerable scenario, instant multi-continent outbreak, and immediate rat kingdoms

All labels in this file are working labels, not final localisation.

## Scenario purpose

The Black Plague has a manual triggerable scenario in the existing Chaos Redux Triggerable Scenarios window. The scenario is a sandbox and challenge launch for players who want the advanced event state immediately instead of waiting for the random event, natural spread, evolution pacing, Rat Nation emergence, and Rat King coronation.

The scenario launches a global crisis in one confirmation action. It must immediately:

- establish Black Plague infection in many states across several continents
- activate the stronger Evolution I strain
- activate Evolution II overseas spread
- create the reusable RTA Rat Nation carrier and several internal broods from selected plague basins
- create the separate Rat King country immediately
- start human containment, rat growth, and Rat King systems in a valid live state
- raise the Chaos Meter to an intensity-scaled crisis floor without directly starting world end
- rebuild the existing disease board and mapmode so every established Black Plague state is shown with a black base colour

The scenario is separate from the Rat King terminal world-end scenario. Manual launch creates the crisis. It does not set `world_end`, does not record Evolution V, and does not hand the world to the Rat King. Evolution V, the world-end focus path, continent control, catastrophic deaths, and the final terminal sequence remain future gameplay goals.

## Scenario identity

| Field | Planning direction |
| --- | --- |
| Scenario catalog ID | `SCN-012` |
| Working scenario label | Black Plague Unbound |
| Scenario role | instant global disease and rat-kingdom challenge |
| Type options | one fixed profile, working label Instant Plague Kingdoms |
| Intensity | existing Low, Medium, High, Maximum slider |
| Launch scope | global, not tied to the currently selected country |
| Repeat launch | blocked after one successful launch |
| Normal event prerequisites | bypassed only during the scenario bootstrap |
| World-end state | never set by launch |
| Achievement status | ordinary Event 20 achievements are disqualified by the scenario launch flag |

The final name should be direct and specific. It should tell the player that the launch creates Black Plague and rat kingdoms. It should not use generic apocalypse wording.

## Scenario window presentation

The scenario row and detail panel must explain the actual launch result before confirmation.

The detail view shows:

- selected intensity
- target number of continents
- target number of established plague states
- target number of internal rat broods carried by RTA
- expected Rat King starting territory and army band
- Chaos Meter floor
- warning that human-owned states can be infected or transferred to rat countries
- warning that Evolutions I through IV are forced for this scenario even if their ordinary timing or event state would not allow them yet
- statement that Evolution V and world end are not launched automatically

The confirmation window must be explicit that this is a global map-changing scenario. The first click opens confirmation. The confirm action reads the currently selected intensity at launch time.

The scenario does not require a separate custom window or dedicated scenario art. It uses the existing data-driven scenario list, detail panel, intensity slider, and confirmation flow. The normal Black Plague disease icon, rat icons, and Rat King assets identify the resulting systems after launch.

## Launch eligibility

The scenario should be directly launchable unless the setup cannot produce a valid game state.

Valid launch requires:

- no active `world_end` state
- no prior successful Black Plague triggerable scenario launch
- at least two eligible inhabited continents with valid human-owned states
- the two-country rat package is available: RTA as the reusable brood carrier and RTX as the separate Rat King
- enough valid states to create at least the minimum Low-intensity package
- no unresolved map transfer that would leave the Rat King without a valid capital

The launch must not be blocked by:

- current Chaos value or Chaos tier
- Event 20 random-event weight
- Event 20 enable or disable setting
- ordinary event date gates
- ordinary evolution availability
- Evolution I through IV mean-time pacing
- prior natural Black Plague history
- lack of a normal first-origin state

If Event 20 is already active through natural play, the scenario upgrades the existing crisis. It adds the missing multi-continent seeds, forces any missing Evolutions I through IV, seeds missing internal broods on RTA, and creates the Rat King if absent. It must not create a second disease identity, duplicate event history, duplicate evolution records, or duplicate country packages.

## Bootstrap state

The scenario owns one tightly scoped bootstrap state. It exists only while the setup sequence runs.

The bootstrap state allows the launch to:

- bypass ordinary origin selection
- seed several continents in one operation
- force Evolutions I through IV without waiting for mean-time resolution
- seed internal RTA broods from scenario-selected basins that already satisfy safe territory requirements
- create a scenario form of the Rat King without first absorbing every brood
- suppress ordinary spread and mortality pulses until initial registration is complete
- batch mapmode and disease-board rebuilding after all state and country setup is finished

The bootstrap state is cleared at the end of the launch sequence even if some target counts had to scale down because the map lacked valid candidates. It must not remain active during ordinary play.

## Required launch sequence

The launch should resolve in a deterministic order so every dependent system reads valid data.

1. Set the scenario bootstrap state and permanent scenario-launched flag.
2. Initialize Event 20 disease, state registry, the two-country rat package, decision, mapmode, and event-log data when missing.
3. Mark the ordinary fire-once Event 20 entry as fired so the random event cannot create a second opening.
4. Record one Event 20 history entry when no valid history entry already exists.
5. Build the eligible continent list and select the intensity-scaled target continents.
6. Select plague anchor basins and surrounding seed states on every chosen continent.
7. Apply the intensity-scaled mix of Infected, Severe Crisis, Collapsed, Threatened, and known Incubating states.
8. Initialize Disease Load, Mortality Pressure, Spread Pressure, Containment, Treatment Coverage, Relapse Risk, and Rat Infestation for every seeded state.
9. Activate and record Evolution I if missing.
10. Activate and record Evolution II if missing.
11. Select connected severe basins and seed the intensity-scaled internal RTA broods.
12. Activate and record Evolution III if missing, using the first created Rat Nation as actor.
13. Select or construct one Royal Basin and create the separate Rat King country.
14. Activate and record Evolution IV if missing, using the Rat King as actor.
15. Assign RTA brood armies and Rat King armies, focus trees, mechanics, decisions, AI, portraits, flags, and growth pulses.
16. Apply the intensity-scaled Chaos floor and refresh shared world-threat state.
17. Schedule ordinary mortality, spread, containment, brood growth, dominance, and Rat King pulses.
18. Rebuild the disease board and perform one full disease-mapmode refresh.
19. Show one global scenario launch report and the existing Rat King coronation super-event when its presentation package is available.
20. Clear the bootstrap state and allow ordinary Event 20 logic to continue.

The setup must not run ordinary mortality or spread once per state while the state list is still being built. Initial population loss is applied through one bounded opening pass after registration, then ordinary death ticks take over.

## Multi-continent plague seeding

The scenario uses the normal vulnerability model as a starting point but adds geographic distribution requirements.

### Eligible continents

A continent is eligible when it contains enough valid inhabited land states owned or controlled by human countries. Nonhuman states, wastelands, invalid map regions, and states already reserved for an incompatible terminal system are excluded.

The selector should:

- choose distinct continents before adding more anchors to the same continent
- favor continents with large vulnerable populations
- include at least one dense urban or port basin when valid
- include at least one low-development or weak-capacity basin when valid
- avoid concentrating every initial state in one major power
- permit player-owned states because the scenario is an explicit global challenge
- avoid invalid one-state transfers that would destroy a country package or strand a capital without a safe fallback

### Anchor basins

Each selected continent receives one or more anchor basins. An anchor basin is a connected set of candidate states built around a vulnerable state.

Anchor scoring favors:

- high population
- low development
- damaged or poor infrastructure
- weak medical and administrative capacity
- ports, rail hubs, warehouses, or major transport junctions
- occupation, resistance, refugees, and active troop movement
- dense urban districts
- existing disease exposure
- enough connected states to support an RTA brood where the intensity calls for one

Strong disease prevention lowers the score but cannot make a state absolutely immune to this manual scenario.

### Seed rings

Each anchor creates an intensity-scaled seed ring.

- The anchor begins as Severe Crisis or Collapsed.
- Connected inner-ring states begin as Infected or Severe Crisis.
- A smaller outer ring begins as Threatened or known Incubating.
- Ports and rail hubs can receive nonadjacent linked seeds because Evolution II is active at launch.
- States selected for RTA broods or the Rat King begin with high Rat Infestation and active plague.

The scenario should distribute states among several countries and landmasses. It must not satisfy the target by infecting a single huge connected block on one continent.

## Starting state composition

Intensity controls both scale and severity.

| State package | Low | Medium | High | Maximum |
| --- | --- | --- | --- | --- |
| Established plague share | mostly Infected | balanced Infected and Severe | Severe weighted | Severe and Collapsed weighted |
| Collapsed share | rare anchor only | limited | common in rat basins | common in rat and royal basins |
| Threatened ring | broad enough to show future spread | broad | broad across transport routes | broad global ring |
| Rat Infestation | high only in rat basins | high in rat basins and some cities | high in many urban and port states | widespread in infected urban and transport states |
| Opening population loss | small, bounded | moderate in Severe states | substantial in Collapsed states | severe but never a terminal instant deletion |

Opening losses are recorded once in the shared Deaths system and Event 20 total. They represent the scenario beginning after the disease has already been spreading in the selected basins. All later deaths use the ordinary nonlinear mortality model.

## RTA carrier and internal broods

The scenario uses exactly one non-sentient Rat Nation country, RTA. Several independent broods appear during launch as state-scoped RTA basin markers, strength pools, and army allocations. They are not visual placeholders and they are not temporary event armies, but they do not consume additional country tags.

Each scenario brood receives:

- one valid connected plague basin
- a guaranteed capital
- one origin archetype selected from local geography
- a strong intensity-scaled initial army
- its normal nonhuman classification
- Brood Mass, Hunger, Coherence, and Disease Dominion initialization
- its normal brood pulse and burrow system
- the shared RTA focus tree with the correct origin module
- hostility toward human countries through the RTA carrier
- normal rat dominance behavior after the launch grace period

The scenario selector should distribute broods across the chosen continents when valid. Maximum intensity should not place every brood next to the Rat King or inside one war zone. Brood identity is carried by state flags, basin variables, and the shared RTA country; no additional Rat Nation tags are created or reused.

If the map cannot support the target number of valid broods, the scenario scales the brood count down and transfers the unused strength budget into the remaining broods within performance caps. It must not create invalid one-state tags or allocate another country tag.

## Immediate Rat King creation

The Rat King appears immediately as a separate country with the Evolution IV package.

The scenario uses a Royal Basin that is separate from the initial independent Rat Nation basins. The Royal Basin is selected from the strongest remaining plague cluster, with preference for:

- high connected infected population
- at least one defensible capital state
- rail, port, or major urban value
- high Rat Infestation
- enough surrounding plague territory to support royal supply
- distance from at least some independent broods so the map begins with several visible rat actors

The Rat King receives:

- the separate Rat King tag
- the sentient sovereign and valid portrait package
- a government-route choice that remains open unless intensity-specific AI begins with a preference
- Dominion, Sentience, Brood Cohesion, and Hunger values
- its three-spirit lifecycle in the correct opening forms
- an intensity-scaled royal army and royal brood pulse
- the deep Rat King focus tree through the coronation and government opening
- claims or scripted authority over the other broods through the normal royal unification system

The scenario does not transfer every RTA brood to the King during bootstrap. That would erase the requested immediate coexistence of RTA broods and the Rat King. Independent broods remain on the map for an initial royal-consolidation grace period. After that period, normal dominance, allegiance, absorption, and conquest logic resumes.

The grace period blocks instant scripted annexation only. It does not make human countries safe from rats, stop plague spread, or prevent ordinary wars against rat actors.

## Evolution handling

The scenario activates Evolutions I through IV in order.

### Evolution I

The stronger strain is active in every seeded state. Countermeasure adaptation is required immediately. Mortality, relapse, and spread use the evolved model from the first ordinary pulse.

### Evolution II

Overseas route logic is active immediately. Ports, convoys, troop routes, and rat stowaways can continue spreading the disease after launch.

### Evolution III

RTA content is active immediately. The first scenario-created brood owns the Evolution III actor record. Later broods are additional emergences, not duplicate Evolution III rows.

### Evolution IV

The Rat King exists immediately. The scenario uses an explicit alternate coronation entry that creates the King without consuming all other broods. The Evolution IV record still uses the Rat King actor and unlocks the same Rat King mechanics, tree, decisions, and super-event presentation.

### Evolution V

Evolution V is not recorded or unlocked solely by scenario launch. The Rat King must still satisfy the accepted live thresholds for Chaos, state share, deaths, Dominion, Sentience, preparation, and focus progress. Maximum intensity can place the world near those thresholds, but cannot bypass the world-end path.

## Intensity scaling

The exact values belong in centralized scenario tuning data. The ranges below are design targets and should scale down safely on smaller or heavily altered maps.

| Intensity | Continents | Established Black Plague states | Internal RTA broods | Rat King starting states | Chaos floor | Opening character |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Low | 3 | 12 to 18 | 2 to 3 | 1 to 2 | 400 | several regional crises and a young royal basin |
| Medium | 4 | 24 to 36 | 4 to 6 | 2 to 4 | 600 | broad intercontinental emergency with established broods |
| High | 5 or every eligible continent when fewer exist | 45 to 65 | 7 to 10 | 4 to 6 | 800 | global military and medical crisis from the first day |
| Maximum | every eligible inhabited continent | 75 to 110 | 6 internal RTA broods | 7 to 10 | 999 | near-world-collapse setup with many severe states and a powerful Rat King |

The target number of infected states is a global target, not a per-continent target. The selector allocates states according to continent population, vulnerability, valid connected basins, and performance caps.

RTA army strength scales from:

- the selected intensity
- infected population in the assigned basin
- average Disease Load and Rat Infestation
- number of Severe Crisis and Collapsed states
- urban, port, frontline, and infrastructure factors
- available plague-state supply
- the number of broods actually created

A reduced brood count should create stronger remaining broods, not fewer weak countries that fail instantly.

## Chaos, Deaths, air cleanliness, and world threat

The scenario sets a minimum Chaos value rather than replacing a higher current value. Maximum stops at 999 during bootstrap so launch alone cannot satisfy the shared world-end Chaos gate.

The scenario then lets:

- opening population losses feed the Deaths tracker once
- ordinary disease deaths raise Chaos through the shared conversion
- infected state contributions affect air cleanliness through the normal outbreak system
- the active RTA carrier and the Rat King refresh the shared world-threat source
- deliberate later weapon use affect condemnation normally

The scenario should not create fake historical death totals merely to unlock Evolution V. Only the bounded opening loss and later real state-population deaths count.

## Disease decisions after launch

Human countries must immediately receive the correct shared disease category state.

- Countries with infected states see quarantine, treatment, emergency hospital, relief, and Black Plague-specific rat-control decisions.
- Countries bordering or linked to infected states see threatened-border, port, transport, and inspection decisions.
- Countries without nearby infection see prevention, surveillance, reserve, and international aid options.
- Human countries bordering rat actors see the anti-rat military and liberated-state cleanup families.
- Countries that retake rat territory still have to clean the plague and Rat Infestation.

The Black Plague-specific decisions remain separate decision entries inside the general disease category. The scenario does not create a dedicated Black Plague category.

## Mapmode after launch

The launch ends with one full rebuild of the existing disease mapmode.

In the shared contamination mapmode:

- every established Black Plague state uses a black base fill
- status is communicated through outlines, status icons, patterns, and tooltips
- Threatened states retain the shared warning colour until infection is established
- cured states leave the black fill after cleanup completes
- Rat-Controlled states remain black and add the rat-control accent
- weaponized provenance adds its own border or symbol without replacing the black fill

The mapmode must show the entire scenario result immediately after confirmation. It must not require the next weekly pulse to reveal seeded states.

## Reports and popup control

The scenario should communicate scale without creating dozens of simultaneous popups.

Use:

- one global launch report summarizing the multi-continent outbreak and immediate rat kingdoms
- the existing Rat King coronation super-event once after the King is valid
- one direct alert for each human player whose country lost or received states during bootstrap
- event-log and disease-board entries for the full state list
- ordinary later reports for new spread, containment, rat absorption, and world-end progression

AI countries should not receive one visible popup for every seeded state.

## AI initialization

The scenario initializes every actor in the correct strategic phase.

Human-country AI:

- evaluates domestic infected states before unrelated wars and low-value projects
- chooses one viable response package per priority state
- uses Black Plague-specific rat-clearing actions when Rat Infestation is high
- protects capitals, ports, supply hubs, and major population centers
- seeks international medical support when emergency burden exceeds capacity
- prepares anti-rat fronts where a brood or Rat King borders the country

RTA carrier AI:

- begins in survival and expansion mode
- secures its plague corridor and first burrow node
- avoids immediate dominance annexation during the grace period
- resumes normal archetype and dominance behavior afterward

Rat King AI:

- begins in coronation and consolidation mode
- selects a government route according to map state and intensity
- protects the Royal Basin before attempting broad conquest
- begins royal unification only after the grace period
- cannot jump directly to the world-end lane without live Evolution V eligibility

## Existing event and repeated launch behavior

### Natural event already active

The scenario reuses existing active state and country registries. It does not clear successful human containment, remove existing countermeasure progress, or reset disease history. It adds enough new states and actors to reach the selected scenario intensity, then activates missing evolved systems.

### RTA broods already exist

Existing RTA states and internal brood markers count toward the intensity target. The scenario creates only the missing number of broods. Existing rat states and units are not duplicated.

### Rat King already exists

The existing Rat King is preserved. The scenario strengthens its starting package only enough to meet the selected intensity floor, seeds the missing global outbreak, and creates missing internal RTA broods. Evolution IV is not recorded twice.

### Repeated launch

After a successful launch, the scenario row remains visible for history and detail purposes but the launch action is disabled. The tooltip explains that the instant setup has already been used.

## Failure handling and cleanup

The scenario launch is all-or-nothing for core identity.

If the launch cannot create a valid Rat King capital or cannot allocate the two-country rat package, it should fail before changing the map. It should not leave a half-built outbreak.

If optional target counts cannot be met after the minimum valid setup exists, the scenario scales down and reports the actual result through dynamic detail text or a launch summary.

The bootstrap must clean:

- temporary continent and state arrays
- temporary target countries
- unused tag reservations
- temporary state scores
- temporary transfer scopes
- scenario-only bypass flags
- suppressed-pulse state

Permanent state after launch includes only the event, scenario, disease, evolution, country, mapmode, and achievement-disqualifier data needed for ordinary play.

## Achievement handling

The permanent scenario-launched flag disqualifies the fourteen ordinary Event 20 achievements unless the live achievement framework explicitly classifies an achievement as scenario-eligible. This prevents instant Evolution III and IV setup from awarding achievements intended for natural campaign play.

No automatic achievement is granted for launching the scenario.

## Scenario-specific balance and validation

Each intensity must be tested as its own start condition.

### Low

- at least three continents when the map supports them
- at least twelve established plague states
- at least two internal RTA broods
- one valid Rat King country
- human containment remains possible with coordinated play

### Medium

- four-continent distribution
- several separate human crisis fronts
- independent broods remain visible after launch
- Rat King survives but does not immediately absorb all broods

### High

- world-threat cooperation becomes strategically relevant immediately
- disease category does not become an unreadable wall of decisions
- mapmode refresh completes without stale colours
- AI can prioritize several fronts without taking every expensive action

### Maximum

- every eligible continent receives established infection
- tag and division caps prevent runaway performance failure
- Chaos stops below the world-end gate at bootstrap
- Evolution V remains locked until live thresholds and focus progress are met
- Rat King and independent broods coexist at launch

### Cross-case validation

- launching while the natural outbreak is active produces no duplicate disease identity
- launching with existing RTA states creates only missing internal brood markers
- launching with an existing Rat King preserves it
- evolution history has at most one row for each of I through IV
- Event 20 history records once
- initial deaths record once
- affected Black Plague states show black immediately in the existing mapmode
- the general disease category shows Black Plague-specific decisions without creating a second category
- scenario bootstrap flags are cleared after launch
- a second launch is blocked
- save and reload preserves every state, country, decision, and mapmode status

## Acceptance criteria for the triggerable scenario

The scenario is complete only when:

- it is registered in the existing Triggerable Scenarios window
- it has a stable scenario ID, sort order, detail text, intensity text, and confirmation flow
- it launches directly without normal chaos, event, date, or evolution prerequisites
- it establishes many Black Plague states across several continents
- it immediately activates Evolutions I through IV
- it seeds several internal RTA broods without creating additional tags
- it creates the separate Rat King immediately
- RTA broods and the Rat King coexist after bootstrap
- Low, Medium, High, and Maximum produce materially different valid setups
- the Chaos floor creates immediate crisis but does not directly trigger world end
- the existing disease category receives generic and Black Plague-specific decisions
- the existing mapmode shows established Black Plague states with a black base colour
- event, evolution, death, country, and mapmode data are not duplicated
- ordinary Event 20 play continues after bootstrap
- Evolution V and terminal world end still require their accepted live conditions
- ordinary Event 20 achievements are protected from scenario shortcuts
- repeat launch is safely blocked
