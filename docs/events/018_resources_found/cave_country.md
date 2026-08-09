# Event 018 Cave Country Package

The Oth-Kesh Host is Event 018's single persistent nonhuman country. It remains dormant until a protected Evolution IV breach succeeds in an active resource field. The country uses tag `DHO`, the original nonhuman sub-ideology `resonant_brood_hierarchy`, the ruling institution `The Resonant Maw`, and the literal cave-monster sovereign Vhorruk. Its base identity is the Oth-Kesh Host. The terminal cosmetic identity is the World Below.

## Emergence contract

Evolution IV cannot create the country on the discovery day. A field must first pass the public-crisis minimum, accumulate the visible breach and exploitation requirements, remain unsealed, and finish the protected final-response window. Full sealing permanently disqualifies only that field and does not schedule hidden retaliation.

The first valid breach performs these operations in order:

1. preserve the exact origin state, discoverer, owner, controller, six Event 018 resource ledgers, field sequence, exploitation history, deaths, safety work, evacuation, hunts, suspension, and failed-seal history;
2. calculate the opening army before physical field cleanup;
3. present the former owner with resistance, international-aid, and playable Oth-Kesh continuation choices;
4. initialize DHO, transfer and core the origin state, set the capital, establish a supply node when the state has none, remove the ordinary field lifecycle, and retain the origin history in the cave-country ledger;
5. spawn the calculated opening broods in valid controlled origin provinces;
6. register the shared cave world-threat source, emit the unique emergence super-event, and declare war on every land actor along the controlled frontier.

Later valid breaches join the same DHO country. They create another cave anchor rather than a second tag.

## Opening strength

Opening strength is calculated by `resources_found_calculate_cave_starting_strength` in state scope. The score uses the field's Event 018 resource total, distinct-resource count, discovery count, Developed Yield, Excavation Depth, maximum-extraction history, Event 018 deaths, failed seals, militarized exploitation, and unsealed-nest history. Workforce Safety, successful evacuation, sealed-network work, long suspension, and successful hunts reduce the score.

The final division count is:

- at least 6 divisions;
- one division per 5 retained score after the configured modifiers;
- never more than 30 divisions.

The value is recorded on both the origin state and DHO for Event Details and defeat accounting. Before the breach transfer, the exact frozen value and each candidate's capital are also recorded for both the legal owner and physical controller, so either role can satisfy Thirty From Below without inferring a past occupation from later ownership.

## Body economy and templates

Oth-Kesh units consume neither ordinary manpower nor equipment. Their five sub-units in `common/units/018_resources_found_cave_broods.txt` have zero manpower, no equipment definition, and deliberately extreme training time. The corresponding templates in `history/units/DHO_1936.txt` are locked and set `force_allow_recruiting = no`. The dormant history does not preload this OOB; Evolution IV loads the template package once immediately before the opening army is created. Event and anchor effects are the only normal source of divisions.

The available templates are:

- Oth-Kesh War-Brood, the slow armored base formation;
- Oth-Kesh Stone Phalanx, the slowest and most heavily armored doctrine formation;
- Oth-Kesh Burrow Column, a lower-armor formation with urban and mountain approach bonuses;
- Oth-Kesh Scree Pack, the fastest and least armored doctrine formation;
- Oth-Kesh Feeding Guard, a nearly immobile anchor-defense formation.

The unit `maximum_speed` field is a multiplier on the equipment-speed baseline rather than an absolute speed. Against the standard 4 km/h foot baseline and the shared `Slow Blood` penalty of 35 percent, the pre-route roster is:

| Template | Battalion speed modifier | Effective speed |
| --- | ---: | ---: |
| Oth-Kesh War-Brood | -45% | 1.43 km/h |
| Oth-Kesh Stone Phalanx | -65% | 0.91 km/h |
| Oth-Kesh Burrow Column | -30% | 1.82 km/h |
| Oth-Kesh Scree Pack | -45% | 1.43 km/h |
| Oth-Kesh Feeding Guard | -75% | 0.65 km/h |

Mineral armor and high hardness make ordinary soft attack inefficient. Concentrated hard attack and sufficient piercing are the intended direct counters. Low speed, surface supply dependence, anchor recapture, denial of resource states, and the origin command crisis provide operational counters. The adaptation lane changes strengths without removing the piercing and hard-attack answer.

Ordinary recruitment, normal equipment production, equipment-market access, ordinary trade, alliance seeking, routine volunteer diplomacy, and an early navy or air force are disabled by templates, ideas, country rules, diplomatic AI, and decision visibility. Captured industry instead accelerates anchors, adaptations, and brood queues.

## Captured-resource capacity

Every controlled non-origin state is evaluated from its current total oil, aluminium, rubber, tungsten, steel, and chromium. Its capacity is:

`min(10, floor(total strategic resources / 10))`

The origin state's future capacity is always zero, regardless of its resources. A non-origin state must remain continuously under DHO control for 30 days before its anchor activates. Losing control interrupts activation. A mature anchor spawns at most one queued division at each configured interval, so several captures cannot produce an instant army stack.

When DHO loses an active anchor, that capacity enters a 21-day grace period. Recapture can restore support. If the grace period expires, excess divisions are retained but receive `cave_unfed_broods` instead of disappearing. Destroyed divisions free capacity naturally. Surface recapture opens a state cleanup path that removes the core, anchor flags, capacity variables, cave modifiers, and underground resource suppression before applying the explicit cleanup scar.

## Focus architecture

`common/national_focus/018_resources_found_cave_focus_tree.txt` defines 67 focuses. Every reward changes an idea, decision unlock, anchor rule, AI target, map objective, spawn preference, capacity rule, or terminal preparation surface. Focus-only completion markers are not used as substitute rewards.

The opening lane secures the origin, creates commanders, initializes the brood network, and teaches the AI to identify resource-bearing surface routes.

Three mutually exclusive hierarchy routes follow:

- One Maw centralizes command around Vhorruk and the origin, concentrates fronts, and deterministically marks the land-reachable enemy state with the greatest total standard-resource value;
- Many Chambers distributes command among mature anchors, extends loss grace, and permits a second deep capital;
- Hoard the Veins makes the richest feeding chambers the governing structure, unlocks Feeding Guards, shortens the brood interval through Mineral Tithe, and adds one non-stacking vault fort level to every current and future mature anchor.

The resource-anchor lane activates capacity, enables automatic brood queues, fortifies feeding states, converts captured industry, marks bounded tunnel-endpoint pairs, and creates a continental network that makes future automatic broods prefer controlled linked endpoints.

Three mutually exclusive warfare doctrines follow:

- Stone Phalanx unlocks deliberate armored pressure and fortified-line targets. Its one doctrine spirit swaps from the base package to cumulative Interlocking Carapaces and then cumulative Great-Gun Resistance only after DHO has faced meaningful piercing. The final stage marks a reachable strongpoint rather than nullifying hard attack;
- Burrow War unlocks underground approaches to rail, road, urban, and command targets. Its base spirit swaps to one cumulative Urban Cellar Networks spirit. A paid approach selects only a defended capital, supply hub, or level-3 fortified state adjacent to an active nondisrupted anchor, then exposes that exact state through a 90-day capture mission;
- Scree Tide unlocks dispersed rapid broods, pursuit, and crossing objectives. Its one doctrine spirit swaps from the base package to cumulative Split Great Broods and then cumulative Lighter Plates. Split Great Broods reduces the automatic-spawn interval once while trading defense, cohesion, and supply efficiency for movement. Its 180-day achievement surge opens only with three deployed Scree Packs inside live brood capacity and rechecks both facts at completion. The surge credits each captured state and defeated country once per attempt.

The adaptation lane records enemy piercing and lets DHO select denser plates or open joints. That selected route remains one spirit while it swaps into a route-specific cumulative Surface Senses stage and then a route-specific cumulative Sky-Hardened stage. The final adaptation helper preserves only the highest route stage and selects Stone automatic broods for dense plates or Scree automatic broods for open joints. A completed focus route therefore has at most one hierarchy spirit, one doctrine spirit, and one adaptation spirit. The continental lane deterministically marks the richest reachable resource state, then marks industrial belts, capitals, coasts, coalitions, and the last eligible resistance. The hidden world-end lane appears only after the continental objective is genuinely relevant and prepares verified distant footholds without opening them early.

`Link the Chambers` deliberately uses one prerequisite group for the three hierarchy capstones and a second group for the three doctrine capstones, so it requires one completed focus from each family. `Surface Senses` deliberately accepts either mutually exclusive body-plan focus. Sky hardening is proactive once Surface Senses is complete; its availability cannot depend on an ordinary country selecting a particular response event, because it gates the shared continental route.

## Decisions and AI

The Oth-Kesh Brood Network category exposes a bounded set of phase-appropriate actions. It marks rich states, starts or accelerates anchors, guards feeding chambers, selects doctrine-specific automatic spawns, replaces origin broods, consolidates unfed formations, deepens tunnel links, prepares doctrine attacks, converts industry, refreshes queues, fortifies the origin, refreshes continental objectives, begins world-end verification, and prepares resource-weighted footholds.

`common/ai_strategy/018_resources_found_ai_strategy.txt` switches DHO among four strategic conditions:

- anchor defense and reduced front width while below supported capacity;
- resource-corridor offensives when support is stable;
- origin recovery when the first chamber is lost;
- terminal fronts around anchors and footholds after world end.

The focus AI chooses hierarchy from state spread and origin risk, doctrine from enemy armor, fortification, terrain, and campaign shape, and adaptation from observed piercing. Invalid route focuses and decisions receive zero weight through their availability gates.

The non-round focus AI tiers are intentional ordering values. Adjacent priorities remain distinct so campaign milestones, network work, adaptations, and terminal preparation do not collapse into equal-weight ties.

Every newly adjacent land actor is attacked once. The frontier resolver evaluates both owner and controller across every non-impassable neighboring state of DHO-controlled territory. It therefore catches occupation frontiers before a peace conference changes ownership.

## Ordinary-country counterplay

The Anti-Cave Response category provides:

- emergency aid using anti-tank equipment, infantry equipment, support equipment, trucks, and trains;
- national anti-armor preparation with hard-attack and piercing bonuses;
- resource denial in threatened non-origin states, visibly damaging local output and adding 30 days to the first anchor attempt; a completed activation consumes the preparation once, subtracts three capacity with a zero clamp, and preserves the denial scar until liberation cleanup or post-defeat cleanup;
- a visible recapture window during anchor activation;
- mature-anchor disruption and cleanup;
- origin-defense and origin-recapture objectives;
- threat-cooperation doctrine and postwar reconstruction.

The cave country retains very high armor after these measures. Counterplay improves the correct weapon family and map response rather than applying a generic damage override.

## World end

World-end verification begins only when DHO owns and controls every eligible state on the stored origin continent. Eligible states exclude impassable and invalid remote microstate cases. The complete gate also requires:

- the world-end setting enabled;
- no active world end;
- global chaos strictly above 1000;
- a continuous 60-day verification period;
- at least one valid resource-weighted foothold candidate outside the origin continent.

Mature verification only unlocks the final `DHO_the_world_opens_below` focus and its notice; it never writes a terminal flag or opens a foothold. Completing that capstone repeats every exact gate, then sets the shared terminal state, stops incompatible automatic event progression, blocks ordinary Event 018 discoveries, transforms DHO into `DHO_WORLD_BELOW`, strengthens the route-aware chamber network, and opens stronger footholds on every valid non-origin continent. Candidate weighting favors strategic resources, resource diversity, industry, transport, and existing Event 018 field value. A candidate must be controlled by its ordinary owner, and that owner must retain at least one other state. Each foothold therefore creates a local playable front and neighbor wars instead of deleting the surrounding country.

## Defeat and cleanup

Regional defeat is valid when DHO controls no state. It clears the cave threat source, cave AI state, global active markers, neighbor notices, active anchor infrastructure, residual cave modifiers, and future Evolution IV eligibility. Every liberated anchor retains an explicit cleanup decision until its physical state is resolved.

The global defeat super-event and reconstruction compact are gated separately. They require world-end or distant-foothold history, or complete origin-continent consumption sustained for the configured campaign period. The three-quarter milestone alone remains regional. A regional outbreak that never reached the final gate ends with the regional containment presentation only.

## Files and assets

Country and army runtime:

- `common/country_tags/018_resources_found_cave_country.txt`
- `common/countries/The Oth-Kesh Host.txt`
- `history/countries/DHO - Oth-Kesh Host.txt`
- `common/characters/018_resources_found_cave_characters.txt`
- `common/country_leader/018_resources_found_cave_traits.txt`
- `common/units/018_resources_found_cave_broods.txt`
- `history/units/DHO_1936.txt`
- `common/ideas/018_resources_found_cave_ideas.txt`
- `common/national_focus/018_resources_found_cave_focus_tree.txt`
- `common/ai_strategy/018_resources_found_ai_strategy.txt`
- `common/scripted_effects/018_resources_found_cave_effects.txt`
- `common/scripted_triggers/018_resources_found_cave_triggers.txt`
- `common/on_actions/018_resources_found_on_actions.txt`

Visual identity:

- base and ideology flags: `gfx/flags/DHO*.tga`, including medium and small sizes;
- terminal flags: `gfx/flags/DHO_WORLD_BELOW.tga`, including medium and small sizes;
- leader and commander portraits: `gfx/leaders/018_resources_found/`; Vhorruk's character uses the dedicated static political portrait;
- Vhorruk real-frame portrait animation: eight-frame horizontal sheet DDS, source frames, GIF review preview, and contact sheet under the Event 018 asset package, wired to the Evolution IV Event Details actor surface while the character UI uses the dedicated static portrait;
- focus icons: `gfx/interface/goals/018_resources_found/`, registered in `interface/018_resources_found.gfx`;
- cave ideas and countermeasure ideas: `gfx/interface/ideas/018_resources_found/`, registered in the same GFX file;
- cave and anti-cave decision/category art: `gfx/interface/decisions/018_resources_found/`, registered in the same GFX file.

The permanent runtime inventory, provenance conclusions, dimensions, frame counts, DDS/TGA paths, sprite identifiers, and specialist evidence links are maintained in `docs/events/018_resources_found/assets.md`.

## Future extension rules

Future cave routes should extend anchor choice, map objectives, unit templates, or coalition counterplay. They should not replace these systems with small passive modifiers. New animated identities require separately authored source frames and a static fallback. Additional nonhuman leaders must use authored Oth-Kesh names and generated portraits, never human random-name pools.
