# Murder Mystery Specification Part 9: Assassin Unit Family, Technology, 3D, Audio, and Counters

## Unit-family purpose

The Assassin State needs a military identity that ordinary renamed infantry cannot provide. Its forces rely on small cadres, compartmented movement, reconnaissance, night operations, planned raids, urban and rough-terrain infiltration, and short periods of concentrated violence.

These strengths must create counterplay. Assassin formations have low staying power, weak armor interaction, poor performance under sustained artillery and air pressure, limited heavy equipment, and high training demands. The army still needs ordinary infantry, engineers, anti-air, artillery, transport, and later mechanized support.

## Owner and consumer disposition

Event 39 owns one standalone custom combat family provisionally called `Assassin Forces`. The family contains several combat profiles and one support attachment. It registers once with the shared Chaos unit-family registry.

- Assassin Cadre is the baseline combat provider profile
- Shadow Company is an elite offensive profile
- Silent Guard is a defensive profile
- Master Assassin is an Evolution V special-forces profile
- Mechanized Assassin is a late vehicle-backed profile
- Saboteur Cell is a support attachment and is not registered as a standalone Event 19 family

Foreign Assassin derivatives consume the same owner family with reduced availability. Event 19 can discover the family through the owner-side provider. No central Event 19 fixed list is extended.

## Custom equipment

The family should use one stable Event 39 equipment type provisionally called `assassin_operations_kit`. It represents specialist communications, climbing and breaching tools, concealment equipment, compact demolition supplies, secure documents, medical packs, and other scarce kit that ordinary infantry equipment does not model.

The equipment should:

- require a date and route-appropriate Event 39 technology
- use real military factory production
- have a low production volume relative to rifles
- be consumed by every custom combat profile at different rates
- be required by the Saboteur Cell support company
- have an exact Event 19 equipment token
- have icon, technology, production, stockpile, lend-lease, capture, and localisation coverage
- remain unavailable to ordinary countries unless an explicit capture, intelligence, or Event 19 derivative route grants it

The profiles also use ordinary infantry equipment, support equipment, trucks, mechanized equipment, fuel, and other standard supplies where their role requires them. Low ordinary rifle use does not mean zero equipment or free combat power.

## Unit profiles

### Assassin Cadre

Role: baseline line battalion for mobile infiltration and planned attacks.

Target behavior relative to a same-era ordinary infantry battalion:

| Attribute | Target band or direction |
| --- | --- |
| Manpower | 55 to 70 percent |
| Infantry equipment | 65 to 80 percent |
| Assassin operations kit | mandatory specialist cost |
| Organization | 120 to 135 percent |
| Movement | 110 to 120 percent where terrain allows |
| Reconnaissance | substantially higher |
| Soft attack | 105 to 115 percent before support |
| Defense | 70 to 85 percent |
| Hit points | 55 to 70 percent |
| Breakthrough | higher during prepared attack |
| Armor and piercing | negligible without attached support |
| Supply | lower basic food and rifle burden, higher specialist-kit sensitivity |
| Training time | longer than infantry |

Terrain direction:

- strong in urban, forest, hills, and mountains
- strong at night and during planned raids
- moderate in jungle, marsh, and river crossing only after specific training
- weak in open plains under conventional fire
- weak in desert without route-specific logistics
- vulnerable in prolonged static defense outside fortified urban positions

### Shadow Company

Role: cap-limited elite offensive formation for breakthroughs, raids, encirclement support, and rapid exploitation.

The Shadow Company improves attack, breakthrough, planning, movement, and night performance over the Assassin Cadre. It uses more operations kits, support equipment, training, intelligence capacity, and command attention. It has low hit points and cannot hold broad fronts.

Formation access should depend on focus route, technology, Cohesion, and a dynamic cap. Centralized command receives better control. Decentralized cells receive more local variants but lower central availability. Pragmatic state development can support larger conventional attachments.

### Silent Guard

Role: defensive elite for the capital, archives, supply hubs, urban strongpoints, movement leadership, and threatened subject capitals.

The Silent Guard receives strong urban defense, entrenchment, organization recovery, and resistance to surprise. It has lower movement and offensive reach than the Shadow Company. It should use heavier support equipment and local fortification support.

The unit should not receive universal defense bonuses in every terrain. Its best performance is tied to urban, fortified, capital, or key-infrastructure contexts.

### Master Assassin

Role: Evolution V special-forces formation for narrow high-value operations and temporary command disruption.

The Master Assassin profile has the strictest cap, longest training, highest operations-kit cost, highest reconnaissance, and strongest short attack window. It has very low hit points and poor ability to hold territory. It should depend on advanced intelligence preparation and Cohesion.

The profile must not represent one person as a division. It represents a small formation of veteran cadres, infiltrators, guides, communications specialists, and support teams.

### Mechanized Assassin

Role: late-game rapid exploitation and mobile infiltration with protected transport.

The formation uses mechanized equipment, trucks, fuel, support equipment, and operations kits. It gains speed, hardness, breakthrough, and operational reach. It remains expensive, supply-sensitive, vulnerable to anti-armor weapons, and unsuitable for low-industry states.

Mechanized Assassin access should normally require Evolution V, an advanced military or industrial route, a production threshold, and enough fuel. The Necessary Mask route reaches it most directly. Other routes can unlock it through a higher Cohesion or captured-industry cost.

### Saboteur Cell support company

Role: support attachment for reconnaissance, demolition, route disruption, urban attack, and limited anti-supply effects.

The support company uses operations kits, support equipment, and a small manpower commitment. It belongs to the Event 39 provider package but remains support-only. It is not a standalone Event 19 family because it cannot form a valid division by itself.

The company should improve planned raids and rough-terrain operations. It should not grant a broad permanent enemy-supply destruction effect without a bounded operation or combat condition.

## Division templates

### Opening templates

The Assassin State begins with:

- a small Assassin Cadre template with engineers or reconnaissance where affordable
- one ordinary local holding infantry template
- one elite template only when scenario intensity or maturity supports it

The starting custom template should be usable with the actual stockpile. It should not spawn understrength by design unless the opening story explicitly gives the player a recovery mission.

### Progression

The military branch unlocks larger cadres, Saboteur Cell support, Shadow Companies, Silent Guard, conventional support, and Mechanized Assassins. Master Assassins remain a late cap-limited formation.

Foreign derivatives receive a smaller template set and cannot train every profile until central support or local focuses unlock them.

## Formation caps

Caps should depend on:

- controlled population
- Event 39 operations-kit production
- completed military focuses
- Brotherhood Cohesion
- agency or intelligence capacity
- number of foreign cells and subjects being supported
- scenario intensity
- elite special-forces capacity where the engine supports it

The player should see current cap, used capacity, next source of capacity, and reason a formation cannot be trained.

Master Assassins and Shadow Companies require hard caps. Assassin Cadres can become a significant part of the army but should still be limited by operations kits, manpower, training, and conventional holding needs.

## Reinforcement and sustainment

Custom formations reinforce from real manpower and equipment. Operations kits are not abstract charges. Low Cohesion, broken supply, lost workshops, foreign deployment, and insufficient intelligence capacity can reduce reinforcement or readiness.

A sustainment system may apply temporary readiness penalties when the country fields more custom units than its support capacity. It must be visible and reversible through production, focus, or demobilization.

## Battlefield counterplay

Ordinary opponents should counter Assassin formations through:

- armor and hardness
- artillery and sustained soft attack
- close air support and air superiority
- reconnaissance and counterintelligence
- fortified open fronts
- attrition and supply denial
- prolonged combat that exploits low hit points
- anti-partisan and garrison preparation
- control of rail, ports, and fuel

The units should create tactical problems without invalidating normal army composition.

## AI template policy

AI Assassin countries must maintain a combined force. Suggested composition goals vary by route and economy:

- Assassin Cadre and ordinary infantry form the main army
- Shadow Companies remain a small offensive share
- Silent Guard protects capitals and critical supply nodes
- Master Assassins remain rare and objective-driven
- Mechanized Assassins appear only when production and fuel can support them
- Saboteur Cells attach to selected elite or operational divisions

AI must not convert all infantry into custom units, queue equipment it cannot produce, or spend every operations kit on foreign decisions.

## Technology architecture

The family should use a compact Event 39 technology line or special-project-backed unlocks after inspection of the live tech graph.

Working technology roles:

- clandestine combat training, which unlocks Assassin Cadres and operations kits
- compartmented logistics, which improves reinforcement, supply handling, and foreign deployment
- urban and rough-terrain infiltration, which unlocks Saboteur Cells and terrain specialization
- shadow operations doctrine, which unlocks Shadow Companies
- protected command doctrine, which unlocks Silent Guard
- master cadre system, which unlocks Master Assassins at Evolution V
- mechanized infiltration, which unlocks Mechanized Assassins

The implementation must use `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` for the final branch. It should not create isolated hidden technologies with missing prerequisites or assets.

## Event 19 owner integration

Event 39 provides one idempotent registration surface from its own integration file and bounded startup or runtime rebuild path. Registration calls the shared family registration API and does not create a recurring whole-world scan.

The registered provider must expose all thirteen callbacks:

- `chaos_unit_family_provider_N_event19_evaluate_eligibility`
- `chaos_unit_family_provider_N_event19_build_template`
- `chaos_unit_family_provider_N_event19_spawn_unit`
- `chaos_unit_family_provider_N_event19_reconcile_sustainment`
- `chaos_unit_family_provider_N_event19_get_equipment_token`
- `chaos_unit_family_provider_N_event19_publish_custom_equipment_tokens`
- `chaos_unit_family_provider_N_event19_get_presentation`
- `chaos_unit_family_provider_N_event19_evaluate_management`
- `chaos_unit_family_provider_N_event19_pay_management_action`
- `chaos_unit_family_provider_N_event19_refund_management_action`
- `chaos_unit_family_provider_N_event19_setup_derivative`
- `chaos_unit_family_provider_N_event19_remove_public_additions`
- `chaos_unit_family_provider_N_event19_cleanup_derivative`

The provider uses stable numeric family and equipment-profile identities. It publishes the operations-kit token. It preserves exact payment and refund symmetry. It does not activate Event 39, create the Assassin State, raise Network Reach, start wars, add murders, fire super-events, or unlock World of Anarchy when Event 19 generates a derivative.

Event 19 derivatives receive a neutral army presentation unless Event 39 supplies a separately supported derivative visual profile. Support-only Saboteur Cells remain inside valid provider templates.

The implementation must update the shared unit-family registry documentation and Event 19 coverage documentation. Missing callbacks, unresolved equipment tokens, generic infantry substitution, or parent-event leakage are blockers.

## CXT coverage

Every new land sub-unit and concrete equipment type requires owner-side CXT coverage through the project test-country contract. The owner registers idempotently, provides its apply helper, and supports bounded repair and maintenance where the shared CXT hooks do not already cover recurring work.

The final inventory must cross-check every Event 39 battalion, support company, equipment token, presentation token, provider disposition, CXT registration, and synchronizer.

## 3D package scope

### Mandatory model family A: Assassin infantry

One humanoid source model should cover Assassin Cadre and provide supported entity or texture variants for Shadow Company and Master Assassin. A Silent Guard variant can share the rig and animation family but should have a clearly different silhouette through approved clothing, protective gear, or equipment.

Visual direction:

- 1930s to 1940s clandestine field equipment
- practical dark or muted clothing with period materials
- compact webbing, radios, satchels, climbing or breaching tools
- face visible or partly obscured in a practical way
- no fantasy armor, glowing weapons, modern tactical gear, anime proportions, katana, or generic ninja costume
- no real religious or extremist symbol

### Mandatory model family B: Mechanized Assassin vehicle

A distinct light mechanized or armored transport model should support rapid covert movement and exploitation. It should look like a plausible period conversion or purpose-built clandestine vehicle, not a modern stealth vehicle.

Visual direction:

- compact 1930s to 1940s armored transport or reconnaissance chassis
- protected passenger compartment and communications gear
- low visual profile without impossible futuristic shapes
- practical wheels or tracks selected after vanilla reference inspection
- no fantasy blades, oversized skulls, or fake text

### Model source rule

Each model uses Meshy 7 and exactly one approved final input image. The final input should be a clean modern designed artwork created after source research, with one subject, clear silhouette, full visible geometry, simple background, and stable perspective. A multi-view board, turnaround, collage, or side-profile sheet is forbidden as Meshy input.

Generated source art must be reviewed before paid provider work. The model job preserves the original input, provider task lineage, downloaded source, checksum, Blender checkpoints, textures, rigs, actions, exports, reimports, and runtime handoff.

### Vanilla reference gate

Before production, inspect the exact installed vanilla mesh and entity used for humanoid scale, axes, facing, origin, source height, entity scale, and effective runtime height. Inspect a suitable vanilla mechanized or reconnaissance model for the vehicle. Do not invent file names in advance.

### Required humanoid actions

- idle loop
- movement loop
- attack or fire sequence with aim, discharge, recoil, and recovery
- death sequence with articulated collapse, impact, and settling
- any role-specific action only when the runtime consumer exists

Every final skeletal action must retain primary motion from verified Meshy animation or another explicitly user-approved professional source. Transform-only, static aliases, whole-rig rotations, and locally improvised final animation are forbidden.

### Required vehicle actions

- idle or engine loop if the engine asset pattern supports it
- movement with wheel or track behavior
- attack action only if the entity has a visible weapon consumer
- destruction or death action where the vanilla entity pattern requires it

### Runtime evidence

The model handoff must include parser or reimport evidence for `.mesh` and `.anim`, runtime hashes, entity scale crosswalk, material mapping, action bindings, live consumer identifiers, and any blocked role. A provider preview or `.blend` file is not completion.

## Unit audio

Custom-unit audio must come from identified vanilla files or externally sourced files with provenance and licensing evidence. Recording, generation, synthesis, primitive waveforms, placeholder audio, and unlicensed downloads are forbidden.

Required roles where the runtime consumer supports them:

- select
- acknowledge
- move
- attack
- retreat
- idle variation
- damage or suppression
- death or destruction
- vehicle engine and movement for Mechanized Assassins
- weapon, equipment, impact, and movement synchronization points

Voice direction should be route and host aware when practical. The central movement can use restrained multilingual or host-language command sets. It should not use stereotyped whispers or a fabricated religious accent. A silent role is allowed only with a concrete design and runtime reason.

The 3D worker must research Internet audio sources, preserve originals, document title, creator, source, license, checksum, editing, final path, and synchronization. If no defensible source exists, the role remains blocked.

## Bespoke counters

Every custom combat profile needs the counter surfaces it actually uses. Before art begins, inspect the exact installed vanilla counter definition and DDS, plus the matching skill-local counter family. Sample the real vanilla green palette from the reference.

Required directions:

- Assassin Cadre counter with invented Event 39 emblem and clear infantry role
- Shadow Company counter with a distinct elite mark
- Silent Guard counter with a defensive or guard mark
- Master Assassin counter with a distinct cap-limited elite mark
- Mechanized Assassin counter with the correct mechanized family structure
- Saboteur Cell support icon or counter consumer where the engine displays it

Counters need normal, selected, disabled, and other actual consumer states when required. Reused vanilla counters, arbitrary green, unreferenced imitation, and opaque matte errors are not final.

## Icon and equipment assets

The unit package also requires:

- sub-unit icons
- support company icon
- operations-kit equipment icon
- technology icons
- division designer icons
- production icon
- idea or doctrine icons where used
- model and counter handoff entries
- static fallbacks for any animated small asset

All alpha-backed outputs should request native transparency and preserve alpha through DDS conversion.

## Acceptance standard

The custom unit family is complete only when the units have distinct mechanics, real equipment, production and reinforcement, caps, AI ratios, technology, doctrine, Event 19 provider coverage, CXT coverage, icons, counters, 3D models, skeletal actions, sourced audio, runtime wiring, documentation, and validation. Renamed vanilla infantry, generic counters, missing audio, one overpowered universal battalion, or unverified provider callbacks are not accepted fallbacks.
