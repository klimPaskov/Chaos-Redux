# 5. Baseline and Evolution I Consequences

## Severity principle

Every baseline package must be large enough that refusal remains dangerous. A package can scale down for a small country, but it cannot become a token loss.

Severity should consider the selected target's size, current reserves, industry, military strength, controlled territory, war state, population, occupied territory, prior refusals, active evolution behavior, and the owning system's protections.

The package entries below are working design identities. They are not final event titles or localisation.

## Baseline registry

### `mm_b00_government_paralysis`

**Owner:** Event 53.

A severe temporary collapse of national administration and command capacity. It combines meaningful Political Power and Command Power loss with temporary government, planning, mobilisation, and industrial pressure. Stability and War Support can also fall within protected bounds.

This package is always valid for a normal Event 53 target and serves as the final transaction safety package after repeated adapter failure.

It must not be designed as several tiny modifiers. The combined effect should alter immediate priorities for several months.

### `mm_b01_stability_collapse`

**Owner:** Event 53 or the shared political-crisis owner.

The target suffers a large immediate Stability loss and a temporary recovery penalty. The effect scales from current Stability and country size. It must remain substantial when current Stability is already low by adding a temporary governance burden instead of wasting most of the package at the floor.

### `mm_b02_war_support_collapse`

**Owner:** Event 53 or the shared political-crisis owner.

The target suffers a large War Support loss and a temporary mobilisation or surrender-pressure consequence. At peace, the package should still matter through military readiness, recruitment, or public commitment. At war, it should create a clear strategic problem.

### `mm_b03_strike_wave`

**Owner:** a shared domestic-crisis adapter or Event 53 until a shared owner exists.

A country-wide strike wave disrupts civilian production, military production, construction, rail use, and political capacity for a dynamic period. Industrial regions can receive stronger local disruption. The package must include a cleanup path and cannot create a permanent strike state without follow-up gameplay.

### `mm_b04_coup_attempt`

**Owner:** a reusable coup or political-crisis system.

A serious coup attempt begins inside the target government. The owner resolves valid ideology, military, security, or elite actors. The package can produce a failed coup with lasting damage, a government replacement, or a limited internal conflict according to the owning system.

This package is invalid when no safe coup form can be resolved.

### `mm_b05_hostile_political_movement`

**Owner:** a reusable political-movement system.

A hostile movement gains organization, popularity, local control, and a timed escalation route. It should create pressure beyond a flat popularity change. The movement can feed strikes, sabotage, unrest, or later revolt if ignored.

The owner chooses a valid movement identity after the package is selected. Different ideologies or regional movements do not receive extra Event 53 ballots.

### `mm_b06_army_mutiny`

**Owner:** a reusable military-fracture system.

Part of the armed forces refuses orders, abandons equipment, seizes local facilities, or creates a short armed standoff. The package scales from army size and command cohesion. It can remove units, damage organization, destroy stockpiles, or create a bounded revolt.

A later mass-mutiny package is a separate Evolution II consequence.

### `mm_b07_separatist_uprising`

**Owner:** a reusable uprising system.

One valid separatist or regional movement begins an armed uprising without necessarily becoming a fully packaged independent country. The owner chooses territory, strength, demands, and war form.

This package is distinct from Independence Wave. It represents an uprising or territorial revolt. The Evolution I independence package creates a viable released country through the full Independence Wave contract.

### `mm_b08_border_conflict`

**Owner:** a reusable border-conflict system.

A valid neighboring dispute becomes an armed border crisis centered on the selected player. The package must select a plausible border actor, reserve a valid border area, and avoid creating an impossible conflict through faction, truce, subject, or active-war contradictions.

The result can remain limited or escalate through the owning system.

### `mm_b09_random_external_war`

**Owner:** a reusable war-crisis system.

One valid foreign country becomes hostile and enters a bounded war centered on the selected player. The attacker must have a viable route to fight and cannot be a fabricated disposable tag.

The package cannot select an ally, subject, inaccessible landlocked actor, invalid special Chaos actor, or country protected by a hard conflict rule that the adapter cannot reconcile.

### `mm_b10_equipment_destruction`

**Owner:** Event 53 using supported stockpile debit helpers.

Large portions of one meaningful supported military stockpile disappear or are destroyed. The internal equipment type is selected after the package receives its ballot. Infantry equipment, support equipment, artillery, trucks, and other safely supported categories can qualify.

Equipment subtypes do not receive separate Event 53 ballots unless they have a distinct package identity approved by registry maintenance.

### `mm_b11_fuel_reserve_loss`

**Owner:** Event 53 using the supported fuel debit helper.

A major share of the target's fuel reserve is lost. The amount should consider reserve size, ordinary consumption, current war state, and a structural country floor. A large fuel-using power should feel a strategic interruption. A country with no meaningful fuel system makes the package invalid.

### `mm_b12_train_loss`

**Owner:** Event 53 using the supported train stockpile helper.

A meaningful number of trains is destroyed or disappears. The loss scales from rail dependence, network size, current train stockpile, and war conditions. It must be large enough to create supply pressure without always deleting the entire network reserve.

### `mm_b13_convoy_loss`

**Owner:** Event 53 using the supported convoy stockpile helper.

A major convoy reserve loss strikes a country that depends on maritime trade, supply, troop movement, or overseas territory. A purely landlocked country with no meaningful convoy system excludes this package.

### `mm_b14_factory_destruction`

**Owner:** Event 53 using a bounded building-damage helper or a dedicated industrial-damage adapter.

A dynamic share of civilian factories, military factories, dockyards, and supporting industrial buildings is damaged or destroyed across valid industrial states. The target selection should avoid concentrating every hit in one low-value state unless the package chooses a single industrial center deliberately.

At higher evolution behavior, severity rises within the same ballot.

### `mm_b15_infrastructure_destruction`

**Owner:** Event 53 or a shared infrastructure-crisis owner.

Railways, infrastructure, supply hubs, ports, airbases, and related logistics buildings suffer a coordinated breakdown in several valid states. The package should create a clear supply and movement problem. It should not duplicate the factory-destruction package by focusing mainly on industry.

### `mm_b16_natural_disaster`

**Owner:** Event 013 Natural Disasters through `call_natural_disaster`.

The selected player becomes the country-scope origin for one valid disaster sequence. Event 013 resolves family, targets, damage, deaths, aftermath, reports, and cleanup.

Every valid disaster family remains internal to the Natural Disasters adapter. Earthquake, flood, wildfire, volcanic activity, storm, and other supported variants do not receive separate Event 53 ballots unless the Natural Disasters owner later establishes that one has a separate strategic identity requiring its own registered package.

### `mm_b17_intelligence_compromise`

**Owner:** Event 52 Intel Leaked through a consequence adapter.

The target suffers a substantial intelligence-exposure package. Foreign governments gain the valid intelligence advantages, network access, or information benefits owned by Event 52. The leak is attributed to Event 53 refusal and does not count as Event 52 firing.

This entry remains blocked until Event 52 exposes a safe bounded adapter that can bypass source-event bookkeeping.

### `mm_b18_economic_isolation`

**Owner:** Event 50 Great Embargo through a consequence adapter.

A large international coalition isolates the target through the real embargo package. Event 50 owns coalition selection, economic pressure, diplomatic participation, DLC-aware behavior, duration, and cleanup.

This entry remains blocked until Event 50 exposes a safe bounded adapter.

### `mm_b19_famine_pressure`

**Owner:** the famine adapter.

One or several valid states enter a severe food-security incident based on real supply, access, vulnerability, and current conditions. The package cannot create famine in a state that the famine owner cannot validate.

Famine owns stages, reserves, relief access, mortality, decisions, missions, migration requests, and cleanup. Event 53 supplies origin and requested severity only.

### `mm_b20_displacement_crisis`

**Owner:** the migration adapter.

A proven movement or reception crisis displaces a substantial civilian cohort from one or several valid origin states. The package must use the migration transaction contract and cannot invent population, duplicate deaths, or erase trapped people.

Migration owns cohorts, routes, reception, settlement, returns, mortality inside transfers, and cleanup.

### `mm_b21_character_assassination`

**Owner:** a reusable character-crisis adapter.

One important eligible political or military character is assassinated. Valid targets can include national leaders, senior commanders, high command, important advisors, or other characters whose removal is safe and meaningful.

The package must protect irreplaceable engine roles, invalid historical transitions, and characters already removed. Different eligible characters are target variants inside one ballot.

### `mm_b22_occupation_revolt`

**Owner:** a reusable resistance or occupation-crisis system.

A large revolt begins in meaningful occupied or non-core territory controlled by the selected player. The owner resolves local states, resistance actors, unit strength, supply, claims, and war form.

The package is invalid when the target lacks enough qualifying territory.

### `mm_b23_random_civil_war`

**Owner:** Event 021 Random Civil War through a reusable civil-war framework.

A serious domestic fracture begins using the owner's valid ideological, regional, legal-government, or command-split package. The civil war must divide forces and territory in a playable form.

Event 53 remains attached to the original target government unless the owner later submits valid legal-successor proof.

This entry remains blocked until Event 021 exposes a safe consequence adapter.

### `mm_b24_diplomatic_crisis`

**Owner:** Event 53 or a shared diplomatic-crisis system.

A major diplomatic breakdown damages relations, guarantees, access, foreign support, or faction cohesion around the selected player. The package must do more than apply a small opinion penalty. It should close concrete cooperation routes, create a serious dispute, or trigger a bounded diplomatic confrontation.

## Evolution I activation

Evolution I becomes eligible at `400+` Chaos. If the threshold and enable state are already satisfied before Event 53 first fires, the first visit can use Evolution I demand behavior and registry entries immediately.

When the chain is already active, the evolution milestone should use target-local paced activation. It records one shared evolution-log entry with the selected country as actor and gives zero Chaos by itself.

Evolution I broadens demand types and adds the following packages.

## Evolution I registry additions

### `mm_i01_independence_wave_release`

**Owner:** Event 006 Independence Wave through a bounded release adapter.

One viable independence movement becomes independent from the selected player's territory. The released country receives its normal country package, territory, armed forces, equipment, manpower, leaders, flags, focus content, claims, diplomacy, and immediate war against the former host when the owner determines that war is appropriate.

The source event remains available to fire later. This package is invalid without at least one viable release candidate.

### `mm_i02_disease_outbreak`

**Owner:** the shared disease or outbreak system.

A real harmful outbreak begins in one or several valid states. The owner selects one valid baseline disease agent after the package is chosen. Agent variants do not receive extra ballots at this tier.

The disease system owns spread, mortality, containment, Air Cleanliness contribution, aftermath, cure interaction, and cleanup.

### `mm_i03_command_fracture`

**Owner:** a reusable military-fracture system.

Several commands refuse coordination, units lose organization and planning, senior officers defect or disappear, and one region can form an armed military authority. This is broader than the baseline army mutiny but below the Evolution II mass-mutiny package.

### `mm_i04_industrial_blackout`

**Owner:** Event 53 or a shared industrial-crisis owner.

A large part of national industry becomes unavailable for a dynamic period through power failure, missing workers, inaccessible plants, and unexplained machinery loss. The package uses a timed capacity burden and targeted building damage.

It is distinct from factory destruction because much of the industrial base can return after the crisis ends.

### `mm_i05_multi_region_sabotage`

**Owner:** Event 53 or a shared sabotage system.

Several separated industrial, rail, port, air, or supply targets are hit in one coordinated episode. The owner reserves distinct states and avoids placing every strike in one region. The package should create several simultaneous repair priorities.

### `mm_i06_multi_actor_border_crisis`

**Owner:** a reusable war-crisis system.

Two or more valid neighboring countries coordinate pressure, border incidents, or a limited intervention against the selected player. The package can create linked border conflicts or one bounded coalition war.

It is invalid unless the full foreign actor set and conflict structure can be resolved safely.

### `mm_i07_supply_network_collapse`

**Owner:** Event 53 or a shared logistics-crisis system.

A country-wide logistics breakdown combines train loss, railway damage, hub disruption, and temporary supply penalties. It is one coherent network crisis, not several independently rolled stockpile packages.

### `mm_i08_security_service_breakdown`

**Owner:** a reusable intelligence and internal-security system.

The target's counterintelligence, agency operations, resistance control, and internal security are disrupted for a dynamic period. Agents can be exposed, operations delayed, and hostile networks strengthened according to valid owner capabilities.

This package is distinct from Intel Leaked. It attacks the target's active security apparatus, while the Intel Leaked package distributes a catastrophic volume of classified material abroad.

## Evolution I severity changes to baseline packages

When Evolution I behavior is active:

- political collapses use higher minimums and longer recovery burdens
- stockpile losses use larger reserve shares
- infrastructure and factory packages can affect more states
- mutiny, uprising, border, and war packages begin with stronger preparation
- famine, displacement, disaster, and outbreak owner requests use the next safe severity band
- assassination can include a wider eligible senior-character pool

Each baseline package still appears once.
