# Outcomes, rewards, and aftermath

## Resolution principles

The expedition resolves through verifiable race state, not an arbitrary final roll.

The first participant that completes the final recovery mission with a valid route, functioning outpost, sufficient survey certainty, sufficient Logistics Readiness, and no unresolved blocking crisis secures the primary recovery core.

Every outcome must preserve four distinctions:

1. winning the main wreck
2. recovering major fragments
3. recovering minor fragments or copied data
4. leaving without usable material

A country may lose the main race and still earn a meaningful partial result. A country that never completed real expedition work receives no participation reward.

## Winner proof

A winner is valid only when all of the following are true:

- the country remains an active participant
- its expedition route remains valid
- its outpost is functioning or a valid emergency recovery route is active
- its survey certainty reached the final threshold
- its final recovery mission completed successfully
- the primary recovery core is not already claimed
- the country is not in an incompatible terminal state

The resolution helper must set the winner and the claimed state in one bounded effect chain. It must then cancel unresolved final recovery missions before another country can complete on the same day.

## Same-day completion

Same-day completions use a deterministic tie rule.

Priority order:

1. higher final survey certainty
2. higher Logistics Readiness
3. higher outpost integrity
4. lower Exposure Risk
5. earlier date on which final recovery readiness was reached
6. stable participant sequence as the final tie breaker

The stable participant sequence exists only to resolve an exact tie. It must not create a hidden advantage during ordinary play.

## Main technology reward

The winner receives one valid Event 016 custom operational technology through the neutral external-grant contract.

The grant must use the Event 016 public helper surface. Event 025 must not reproduce Event 016 technology effects, templates, equipment, provider registration, or lifecycle rebuild logic.

The primary path should call the random unresearched operational technology helper. A successful grant records Event 025 as the external origin in the shared alien-recovery ledger while leaving Event 016 history untouched.

Player-facing wording describes the result as knowledge decoded from the recovered craft. It never uses Kruger, Directorate, Event 016, or internal technology-family language.

## Valid reward pool

The actual pool is the Event 016 registry at implementation time.

Event 025 must not freeze a copied list of technology identifiers into its own scripts. It asks Event 016 for a valid unresearched base operational family.

The result may concern advanced propulsion, alien arms, computation, robotics, materials, teleportation, temporal systems, engineered biology, cloning, or another family exposed by the current Event 016 registry. The exact family remains random among valid choices.

Technology eligibility must respect dependencies, incompatibilities, existing ownership, and any provider-specific rules already enforced by Event 016.

## Duplicate-safe fallback

A winner may already own every base operational family. A safe no-op is not an acceptable major-event reward.

Implementation must therefore extend the shared Event 016 external-grant API with one general duplicate-safe route if the live repository does not already provide it.

Preferred helper contract:

`chaosx_grant_random_custom_technology_reward`

The helper should resolve in this order:

1. grant a random valid unresearched base operational family
2. otherwise grant a random valid unresearched upgrade whose dependency can be satisfied
3. otherwise grant the shared Alien Systems Integration capstone result

The helper should return:

- whether a reward was applied
- whether the result was a base family, upgrade, or capstone
- the selected family or upgrade identity for hidden ledgers and scripted localisation
- whether the reward was upgraded because of previous alien recovery

This helper belongs with Event 016 or the shared custom-technology system because Event 036 and future external sources can reuse it.

## Alien Systems Integration capstone

The capstone is used only when the recipient already owns every base family and every compatible upgrade in the Event 016 external pool.

It should represent the ability to integrate alien-derived systems across existing research and production.

The capstone must be strong enough to remain a major reward. It should provide a persistent but bounded combination of:

- special-project research speed
- aircraft, electronics, or propulsion research speed
- prototype production efficiency or reliability support
- reduced penalties from alien-system testing
- access to one integration decision family that improves an existing alien technology without creating a new free technology

The capstone must not create free units, free advanced equipment, a Kruger character, a Kruger State route, or Strategic Singularity access.

## Event 036 arbitration

Event 025 and Event 036 share one alien-recovery ledger.

The ledger must record at least:

- whether Event 025 was won by the current country
- which Event 025 technology family or upgrade was granted
- whether Event 036 has already granted an alien-aircraft package
- whether an overlap conversion has already been used
- the current highest alien-aircraft reward tier

### Event 025 first

When Event 025 fires first:

- the ordinary random reward may include an alien-arms or propulsion family
- Event 036 later checks the ledger
- Event 036 must not repeat the same base reward
- an overlapping Event 036 result becomes an upgraded aircraft package, higher technology tier, module unlock, production route, or another valid aircraft-specific improvement

### Event 036 first

When Event 036 fires first:

- Event 025 excludes the exact base reward already represented by Event 036 when another valid base family exists
- if only overlapping choices remain, Event 025 grants a compatible upgrade
- if the recipient has exhausted the full pool, Event 025 grants Alien Systems Integration

### Different countries

Different countries may receive separate alien results. Duplicate arbitration is primarily country-specific.

The global ledger should still record that the world has seen more than one alien-recovery incident. That fact can alter news wording, foreign suspicion, and Event 044 Space Race hooks without denying another country its reward.

## Public reward reveal

The winner announcement should reveal the broad field, not the internal technology key.

Examples of broad fields include:

- propulsion and flight control
- directed energy and weapons
- computation and autonomous machinery
- exotic materials
- spatial manipulation
- biological synthesis
- temporal instrumentation

The report should state that the winner has secured usable knowledge. It should not list every unlocked runtime consumer or future synergy.

## Winner aftermath

The winner enters a research aftermath lasting long enough for later decisions and Evolution V to matter.

Baseline aftermath components:

- a staged Alien Recovery Program idea
- access to analysis, containment, secrecy, and limited sharing actions
- a visible winner marker in Event Details
- a foreign attention value used for espionage and diplomatic reactions
- cleanup of the active race while retaining the artifact ledger

The idea begins as a mixed state. It represents technical access, secrecy costs, testing accidents, and administrative strain.

Suggested lifecycle:

| Form | Role | Transition |
| --- | --- | --- |
| Secured Antarctic Material | Immediate recovery, strong research access, high burden | Analysis policy selected |
| Controlled Alien Research | Lower risk, slower exploitation | Containment route |
| Integrated Alien Systems | Stronger use, higher Exposure or Dependence | Aggressive integration route |
| Shared Recovery Commission | Reduced exclusive benefit, diplomacy and research-sharing advantages | Cooperative transfer route |
| Sealed Antarctic Archive | Technology retained, artifact inaccessible, lowest active risk | Destruction or deep storage route |
| Compromised Alien Program | Accident, leak, survivor, or Evolution V failure | Emergency recovery chain |

The implementation agent may use dynamic modifiers or staged ideas. It should avoid stacking several permanent alien ideas on one country.

## Losing expedition rewards

Losing rewards scale with verified contribution.

### Tier 0: Observer or failed departure

Requirements:

- no functioning outpost
- no verified fragment
- little or no survey work

Reward:

- no mechanical research reward
- public winner report only

### Tier 1: Survey data

Requirements:

- functioning route or partial outpost
- meaningful survey contribution
- no physical fragment

Reward direction:

- bounded research bonus toward electronics, radar, aviation, or special projects
- one intelligence insight about the winner or another participant when justified

### Tier 2: Minor fragments

Requirements:

- at least one verified fragment or equivalent copied technical data
- meaningful progress

Reward direction:

- stronger research bonus
- temporary materials or electronics production support
- access to one fragment-analysis mission

### Tier 3: Major fragment cache

Requirements:

- high progress or successful Evolution IV fragment recovery
- physical recovery proof
- did not secure the main core

Reward direction:

- one Event 016 custom technology upgrade only when the country already owns the matching dependency and the fragment supports it
- otherwise a large research bonus and an alien-fragment idea with a short lifecycle

A losing country cannot receive a random full base operational technology unless an evolution or rare branch explicitly gives it control of a major independent system. The main winner must remain distinct.

## Fragment accounting

Every fragment has a stable category and one owner at a time.

Suggested categories:

- propulsion lattice
- energy conduit
- computation core
- structural material
- sensor array
- biological or environmental sample

The active wreck may expose fewer categories depending on evolutions. Evolution IV can expose all categories across separate sites.

Fragments are never duplicated by transfer. Transfer clears the previous owner and updates the ledger.

## Evolution I reward effect

The active signal improves search speed and can reveal a compatible technology family.

Following the signal increases the chance that the final reward belongs to the revealed broad field. It does not guarantee an internal technology key if that result is invalid or already owned.

Remote signal study may grant a smaller pre-winner research benefit. It cannot grant the full main reward before recovery.

## Evolution II reward effect

A captured or cooperative survivor may provide:

- one additional fragment category
- a higher chance of a valid technology upgrade
- a safer containment route
- information that reduces Event 036 overlap

A killed, escaped, or hostile survivor can damage the reward, raise Exposure Risk, or create a follow-up incident.

The survivor must not become a generated real-world character. It is an impossible entity or machine and may use generated non-portrait art if shown.

## Evolution III reward effect

Militarised expeditions may seize rival fragments or outposts.

Seizure never grants the main core without completing the final recovery proof. A country cannot win by repeatedly raiding weak participants while ignoring survey and logistics.

Captured scientists or crews are temporary expedition resources. They do not become permanent advisors unless a later accepted design explicitly creates such a route.

## Evolution IV reward effect

The winner may choose between the main core and broad fragment recovery.

Possible outcomes:

- secure the core quickly and leave several fragments available to rivals
- stabilize the wreck and attempt broader recovery at greater risk
- collect a specialized fragment set while another country wins the core

The main core remains the ordinary winner condition. Fragment breadth supports achievements and upgrade selection.

## Evolution V aftermath

Evolution V changes post-recovery Exposure Risk into Alien Dependence for technology holders.

Dependence represents the degree to which doctrine, production, research, and command decisions rely on systems that are poorly understood.

The holder chooses among five policy families.

### Contain

- slows exploitation
- reduces Dependence
- lowers accident chance
- preserves the technology
- opens inspection and safety missions

### Destroy

- removes or seals physical material
- keeps already learned technology
- blocks stronger alien upgrades from this artifact
- sharply lowers Dependence
- may damage relations with countries that expected access

### Transfer

- sends physical custody to a willing valid country
- transfers future artifact actions and Dependence pressure
- does not transfer already researched technology automatically
- creates diplomacy and intelligence consequences

### Conceal

- preserves exclusive access
- lowers immediate public pressure
- raises leak and internal-capture risk
- worsens consequences when exposed

### Integrate

- grants the strongest technology benefits
- raises Dependence
- changes doctrine and production behavior
- unlocks stronger accidents and containment crises
- supports the difficult integration achievement route

None of these routes is terminal. A country can recover from high Dependence through long, expensive containment work.

## Casualties and the Deaths ledger

Actual expedition deaths must use the shared Deaths system when enabled.

Valid death sources include:

- ship loss
- outpost fire or collapse
- exposure and starvation after route failure
- signal pulse accident
- survivor attack
- armed clash
- wreck instability
- containment accident

Deaths should be modest compared with mass-casualty events. They represent expedition teams, sailors, aircrews, scientists, and soldiers.

The event must not apply state population loss for personnel who were already committed as expedition manpower unless the design explicitly models them as civilians drawn from the home population. Military losses should use the military side of the shared ledger where supported.

## Withdrawal outcome

A country may withdraw before the final recovery.

Withdrawal returns part of the temporary industrial commitment, cancels missions, and preserves verified data or fragments already held.

A safe withdrawal costs time and resources. An emergency evacuation is faster but can abandon fragments, damage the outpost, and cause casualties.

A withdrawn country cannot re-enter the same race.

## No-participant resolution

If every invited country declines or becomes invalid before departure, the event closes through a public report that the site remains beyond reach.

The main reward is not assigned. Event 036 remains fully available.

If all active expeditions collapse after outposts exist, the highest verified fragment holder may receive a minor fragment outcome, but no country receives the main technology.

## Save and cleanup contract

After winner resolution the implementation must:

- save the winner as a persistent global event target or stable country identity only for as long as needed
- record the winner in Event Details and history-related data
- cancel active race missions
- clear participant selected targets
- release temporary factory commitments
- clear temporary route scopes
- retain alien-recovery ledgers, fragment ownership, aftermath state, and achievements
- retain Evolution V country tracks when active
- prevent another winner declaration

The cleanup should be idempotent so save reload and duplicate calls do not remove legitimate rewards or reapply them.
