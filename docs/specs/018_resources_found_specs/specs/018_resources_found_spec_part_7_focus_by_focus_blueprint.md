# Event 018 Resources Found, Part 7 Event 018 Deepening Pass, Focus-by-Focus Blueprint and Route Diagrams

All focus names, node ids, route names, and lane names in this file are working labels only. They are not final localisation. The implementation agent owns final focus ids, final focus names, final descriptions, final coordinates, and final icon assignments. The blueprint exists to prevent a shallow Cave Host tree and to give the implementation agent enough structure to build the tree without inventing route logic.

This pass expands the Cave Host tree from path-level design into a focus-by-focus role blueprint. It preserves the fixed-purpose nonhuman identity from the earlier files. The Host remains slow, heavily armored, resource driven, and unable to use normal manpower or equipment. Its army is created by the resource capacity rule, with the origin army capped around 30 and later non-origin state capacity equal to one division per 10 total resources, capped at 10 per state.

## Coordinate model

The coordinate model uses approximate focus-tree positions. These positions are design guidance, not mandatory final layout. The final tree should keep the same branch relationships and avoid tangled lines.

| Lane | Approximate x band | Row range | Visual role |
| --- | --- | --- | --- |
| Opening trunk | 14 to 20 | 0 to 4 | first breach, Host rules, branch unlocks |
| Hunger lane | 4 to 9 | 4 to 10 | resource targeting and capacity reliability |
| Stone hide lane | 10 to 14 | 4 to 9 | armor, hardness, recovery, slow siege identity |
| Tunnel lane | 15 to 20 | 4 to 9 | rough terrain, tunnel links, resource-state movement |
| Brood hierarchy lane | 21 to 27 | 4 to 11 | method choice between swarm and elder broods |
| Surface terror lane | 29 to 34 | 5 to 10 | panic, depopulation pressure, enemy disruption |
| Continental maw lane | 13 to 19 | 11 to 17 | late continent pressure and world-end support |

The opening should split by row 3 or row 4. The Host should not spend 10 focuses reaching its first choice. Hunger, stone hide, tunnel, and brood hierarchy should be visible early. Surface terror can appear after public victory or visible surface attacks. Continental maw should stay late and require real map success.

## Opening trunk focus roles

| Working id | Row | X | Working label | Prerequisite guide | Role | Unlock or reward direction | AI priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_origin_nest_anchor | 0 | 16 | Origin nest anchor | none | Creates the first stable nest identity and stores the origin state as a permanent special state. | Origin defence bonus, origin score display, nonhuman country rules visible. | Always first |
| ch_bodies_from_the_seam | 1 | 16 | Bodies from the seam | origin nest anchor | Explains why resources become bodies instead of normal industry. | Resource capacity display, capacity refresh hook, cave monster template family. | Always high |
| ch_first_surface_war | 2 | 14 | First surface war | bodies from the seam | Pushes the Host toward neighbouring states and public war. | Neighbour target selection, first war pressure, front AI. | High if not surrounded by majors |
| ch_hunger_remembers | 2 | 18 | Hunger remembers | bodies from the seam | Opens the idea that the Host can sense resource value. | Hunger lane, resource target markers. | High in resource-rich region |
| ch_the_slow_host | 3 | 12 | The slow host | first surface war | Defines slow armored movement as identity, not a temporary penalty. | Stone hide lane, base armor and speed identity. | High when facing infantry-heavy enemies |
| ch_the_lower_roads | 3 | 16 | The lower roads | first surface war or hunger remembers | Opens rough terrain and resource-state movement logic. | Tunnel lane, terrain direction. | High if origin is mountainous or resource clusters exist |
| ch_brood_forms | 3 | 21 | Brood forms | hunger remembers | Opens the choice between brood methods. | Brood hierarchy lane, spawn method preview. | High after first captured resource state |
| ch_surface_smell | 4 | 29 | Surface smell | first surface war and one public combat condition | Opens terror lane after the Host is visibly killing and driving people away. | Surface terror lane. | Medium until Host captures a victory point |

Implementation notes for the trunk:

- The first two focuses are mandatory. They set the rules of play.
- The third row should branch into at least three lanes.
- The trunk should not give ordinary factories, political power, stability, or war support.
- The trunk should use tooltip direction that explains visible rules without exposing hidden world-end checks.

## Hunger lane focus roles

| Working id | Row | X | Working label | Prerequisite guide | Role | Unlock or reward direction | Tradeoff or risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_scent_of_ore | 4 | 6 | Scent of ore | hunger remembers | Begins resource-state target selection. | Adjacent resource-rich states become preferred targets. | Human countries see clearer signs of targeted pressure. |
| ch_taste_of_the_old_field | 5 | 6 | Taste of the old field | scent of ore | Gives the Host special awareness of the origin resource type. | States with matching resource type get stronger target score. | Narrow target bias can delay strategic movement. |
| ch_rich_ground_calling | 6 | 4 | Rich ground calling | taste of the old field | Improves capacity reliability from medium and rich resource states. | Faster spawn queue refresh after captures. | Foreign resource-deficit countries become more alarmed. |
| ch_empty_ground_disdain | 6 | 8 | Empty ground disdain | taste of the old field | Makes Host less interested in poor ground. | AI avoids low-resource states unless they form needed corridors. | Host may leave open terrain to enemies. |
| ch_old_resource_memory | 7 | 5 | Old resource memory | rich ground calling | Ties the original discovery to later Host hunger. | Matching resource states give temporary brood readiness or attack planning. | Humans can infer the pattern through target behaviour. |
| ch_rival_seams | 7 | 9 | Rival seams | empty ground disdain | Allows a second priority resource type when the continent has poor matching deposits. | Secondary target score based on total resources. | Slightly higher world threat from spreading target list. |
| ch_hungry_calculation | 8 | 7 | Hungry calculation | old resource memory and rival seams | Merges direct hunger with strategic target logic. | Better AI target selection, cleaner war-goal choice. | Enemy anti-Host coalition interest rises. |
| ch_tenfold_rule | 9 | 7 | Tenfold rule | hungry calculation | Makes the capacity rule more readable and consistent. | Capacity tooltip and non-origin capacity refresh become more reliable. | Does not raise the user cap. |
| ch_mouth_of_the_vein | 10 | 7 | Mouth of the vein | tenfold rule | Hunger lane capstone. | Captured resource states fill capacity more predictably and with less delay. | Raises global world-threat pressure. |

The hunger lane should strengthen clarity and reliability. It must not bypass the non-origin cap. A state with more than 100 resources still caps at 10 non-origin divisions unless a later implemented rule consumes more than one capacity per stronger division.

## Stone hide lane focus roles

| Working id | Row | X | Working label | Prerequisite guide | Role | Unlock or reward direction | Tradeoff or counterplay |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_hardened_bodies | 4 | 12 | Hardened bodies | the slow host | Starts stone armor progression. | Base armor and hardness increase. | Speed drops or remains poor. |
| ch_bullets_on_stone | 5 | 12 | Bullets on stone | hardened bodies | Makes infantry weapons less effective. | Defence against soft attack and low-piercing enemies. | Hard attack becomes clearer counterplay. |
| ch_deep_plates | 6 | 10 | Deep plates | bullets on stone | Opens heavier armor method. | Higher armor for elite or front units. | Reinforcement rate drops. |
| ch_mineral_wounds_close | 6 | 14 | Mineral wounds close | bullets on stone | Links recovery to mineral ground. | Better recovery or reinforce chance in resource states. | Weaker outside resource states. |
| ch_pressure_carapace | 7 | 10 | Pressure carapace | deep plates | Improves hard defensive identity. | More breakthrough and defence when attacking fortified resource states. | Human anti-tank and CAS decisions should unlock faster. |
| ch_shells_find_cracks | 7 | 14 | Shells find cracks | mineral wounds close | Creates explicit weakness instead of pure invulnerability. | Enemy hard attack, heavy artillery, and CAS get meaningful counterplay hooks. | Host gets no benefit against prepared heavy weapons. |
| ch_slow_siege_body | 8 | 12 | Slow siege body | pressure carapace and shells find cracks | Turns the lane into a siege identity. | Fort or entrenched-state pressure, heavy attack style. | Movement remains bad. |
| ch_stone_hide_capstone | 9 | 12 | Stone hide capstone | slow siege body | Final stone route payoff. | Very high armor and defence against unprepared armies. | Human anti-monster counter decisions become more urgent and visible. |

The stone hide lane must not remove counterplay. It should tell the implementation agent to make hard attack, anti-tank, heavy artillery, CAS, and resource denial matter.

## Tunnel lane focus roles

| Working id | Row | X | Working label | Prerequisite guide | Role | Unlock or reward direction | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_lower_road_sense | 4 | 17 | Lower road sense | the lower roads | Starts rough terrain identity. | Better movement or combat in hills, mountains, forests, and mining terrain. | No open plain speed gain. |
| ch_mine_rail_ghosts | 5 | 17 | Mine rail ghosts | lower road sense | Uses surface extraction routes as underground cues. | Planning or movement near rail and resource states. | Requires controlled resource or rail path. |
| ch_under_the_forts | 6 | 15 | Under the forts | mine rail ghosts | Gives slow siege utility against static lines. | Fort pressure or siege preparation. | Does not create instant breakthroughs. |
| ch_burrowed_reserves | 6 | 19 | Burrowed reserves | mine rail ghosts | Lets broods shift between controlled resource states. | Redeployment decision or event between eligible states. | Cooldown and resource-state requirement. |
| ch_seam_listening | 7 | 15 | Seam listening | under the forts | Improves detection of weak seams near enemy lines. | Targeting bonus against adjacent resource clusters. | Limited by existing front. |
| ch_resource_gateways | 7 | 19 | Resource gateways | burrowed reserves | Defines linked controlled resource states as a network. | Defensive support or local reinforcement between linked states. | Network breaks when resources are lost. |
| ch_closed_earth_logistics | 8 | 17 | Closed earth logistics | seam listening and resource gateways | Makes the tunnel system readable. | Capacity refresh and local movement benefit from connected resource states. | Poor ground still matters. |
| ch_deep_road_capstone | 9 | 17 | Deep road capstone | closed earth logistics | Tunnel lane capstone. | Host becomes difficult to isolate inside resource clusters. | Resource denial and cutting clusters remain key counters. |

The tunnel lane should create a slow and stubborn enemy, not a fast raider. It can help the Host reposition between controlled resource zones, but it should not become a tank blitz system.

## Brood hierarchy focus roles

| Working id | Row | X | Working label | Prerequisite guide | Role | Unlock or reward direction | AI priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_brood_ordering | 4 | 23 | Brood ordering | brood forms | Explains that the Host can organize its bodies in different ways. | Shows current spawn method and capacity. | High after first resource capture |
| ch_resource_wombs | 5 | 23 | Resource wombs | brood ordering | Improves origin and captured-state spawning infrastructure. | Spawn queue quality, cooldown tuning. | High |
| ch_claim_the_deep_hierarchy | 6 | 23 | Claim the deep hierarchy | resource wombs | Locks the player toward a method choice. | Opens mutually exclusive swarm and elder paths. | High |

### Swarm brood branch

| Working id | Row | X | Working label | Prerequisite guide | Role | Reward direction | Weakness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_many_small_shapes | 7 | 21 | Many small shapes | claim the deep hierarchy | Swarm branch entry. | Smaller, more frequent broods. | Individual divisions are weaker. |
| ch_fast_awakening | 8 | 20 | Fast awakening | many small shapes | Speeds capacity filling. | Captured resource states produce bodies sooner. | More vulnerable to encirclement. |
| ch_front_swarm | 9 | 22 | Front swarm | fast awakening | Improves broad front coverage. | Better line holding across multiple fronts. | Poor against prepared hard attack. |
| ch_broken_armor_bargain | 10 | 20 | Broken armor bargain | front swarm | Makes the tradeoff explicit. | More units or better recovery at lower armor. | Anti-tank and CAS can punish masses. |
| ch_swarm_capstone | 11 | 21 | Swarm capstone | broken armor bargain | Final swarm payoff. | Capacity fills quickly across many resource states. | No change to per-state capacity cap. |

### Elder brood branch

| Working id | Row | X | Working label | Prerequisite guide | Role | Reward direction | Weakness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_older_bodies | 7 | 25 | Older bodies | claim the deep hierarchy | Elder branch entry. | Fewer, stronger bodies. | Slower capacity fill. |
| ch_long_waking | 8 | 26 | Long waking | older bodies | Delays spawn for stronger units. | Better template quality from high-resource states. | Empty fronts become riskier. |
| ch_cracking_fortified_ground | 9 | 24 | Cracking fortified ground | long waking | Gives elder bodies siege purpose. | Better breakthrough against defended resource states. | Not useful against wide empty fronts. |
| ch_fewer_deeper_names | 10 | 26 | Fewer deeper names | cracking fortified ground | Keeps the route from becoming a swarm with better stats. | Higher armor and organization, fewer total bodies if conversion is used. | Capacity use can be heavier if implementation supports it. |
| ch_elder_capstone | 11 | 25 | Elder capstone | fewer deeper names | Final elder payoff. | Elite siege broods from high-resource states. | Still respects non-origin cap through capacity accounting. |

Swarm and elder paths are mutually exclusive. Other lanes should stay compatible with either method.

## Surface terror lane focus roles

| Working id | Row | X | Working label | Prerequisite guide | Role | Unlock or reward direction | Backlash |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_first_city_fear | 5 | 31 | First city fear | surface smell and public victory condition | Starts panic warfare around visible attacks. | Enemy local panic near victory points and front states. | Human response grows. |
| ch_emptying_streets | 6 | 31 | Emptying streets | first city fear | Drives population flight and disruption. | Enemy state output loss or evacuation pressure. | Evacuation and hunt decisions strengthen. |
| ch_night_roads | 7 | 29 | Night roads | emptying streets | Makes nearby movement and logistics uncertain. | Enemy planning or movement disruption near Host fronts. | Limited by active front and state control. |
| ch_names_in_shelters | 7 | 33 | Names in shelters | emptying streets | Tracks public civilian fear without writing final text. | World threat pressure when civilian deaths or panic are high. | Anti-Host cooperation increases. |
| ch_failed_hunts | 8 | 29 | Failed hunts | night roads | Reacts to human hunt decisions and monster visibility. | Host gains temporary pressure when hunts fail. | Humans can learn and improve counters. |
| ch_fear_crosses_borders | 8 | 33 | Fear crosses borders | names in shelters | Spreads panic to neighbours. | Border states near Host get weaker output or readiness. | Diplomatic coalition is more likely. |
| ch_city_maw | 9 | 31 | City maw | failed hunts and fear crosses borders | Focuses terror around cities. | Stronger panic around high-population states and VPs. | Civilian-protection responses become urgent. |
| ch_surface_terror_capstone | 10 | 31 | Surface terror capstone | city maw | Final terror payoff. | Strong enemy disruption and world-threat visibility. | Stronger global response, stronger counter decisions. |

The surface terror lane should be harsh and visible. It must not be written as comedy in player-facing implementation. It should use fear, movement, missing people, evacuation, and city disruption as direction.

## Continental maw focus roles

| Working id | Row | X | Working label | Prerequisite guide | Role | Unlock or reward direction | Gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_roots_of_continent | 11 | 16 | Roots of the continent | hunger capstone or deep road capstone and large foothold condition | Chooses or identifies the continent where Host is strongest. | Continent progress tracker, target continent memory. | Requires real continental foothold. |
| ch_resource_knots | 12 | 14 | Resource knots | roots of continent | Targets the richest states on the same continent. | Resource cluster targeting. | Requires known target continent. |
| ch_beneath_every_border | 12 | 18 | Beneath every border | roots of continent | Weakens ordinary border meaning inside the target continent. | Planning or movement among nearby resource clusters. | Does not cross oceans. |
| ch_against_denial_lines | 13 | 13 | Against denial lines | resource knots | Counters human resource denial. | Host can pressure fortified resource states. | Human scorched-resource actions still matter. |
| ch_the_continent_opens | 13 | 19 | The continent opens | beneath every border | Moves from state hunger to continental system. | World-end readiness increases if chaos and control conditions align. | No world-end by focus alone. |
| ch_stored_origin_hunger | 14 | 16 | Stored origin hunger | against denial lines or the continent opens | Keeps origin score relevant without letting it inflate later capacity. | Origin army memory and origin nest bonus. | Does not count origin resources again for future state capacity. |
| ch_across_mountain_chains | 15 | 14 | Across mountain chains | stored origin hunger | Improves continental rough-terrain pressure. | Better movement or defence in mountains and hills. | Still slow in open ground. |
| ch_world_below_ready | 15 | 18 | World below ready | stored origin hunger | Prepares terminal scenario checks. | World-end readiness flag or stage if actual state control qualifies. | Requires chaos over 1000 and state conditions for terminal branch. |
| ch_maw_warning_state | 16 | 16 | Maw warning state | across mountain chains and world below ready | Makes the late threat visible through systems, not spoilers. | Super-event readiness and global threat response. | Human coalition may escalate. |
| ch_continental_maw_capstone | 17 | 16 | Continental maw capstone | maw warning state | Final support focus for terminal branch. | Supports world-end scenario if Host owns enough of a continent. | Does not bypass world-end gate. |

The continental maw lane must never use a focus click alone to force the terminal branch. The terminal branch still needs the world state, continent threshold, chaos over 1000, and no existing world-end state.

## Cross-lane prerequisites and convergence

| Source lane | Target lane | Connection purpose | Suggested connection |
| --- | --- | --- | --- |
| Hunger | Continental maw | Rich-state targeting should feed continent pressure. | mouth of the vein can unlock roots of the continent with territory gate. |
| Tunnel | Continental maw | Resource networks should support continent progression. | deep road capstone can unlock roots of the continent with territory gate. |
| Stone hide | Surface terror | Armored city attackers should intensify panic. | stone hide capstone can add optional prerequisite to city maw or give bonus if both exist. |
| Brood swarm | Hunger | Many bodies need more reliable target logic. | swarm capstone can boost hunger capstone effects. |
| Brood elder | Stone hide | Elder bodies pair with armor and siege logic. | elder capstone can boost slow siege body or stone hide capstone. |
| Surface terror | Continental maw | Public terror should accelerate world response and super-event readiness. | surface terror capstone can improve maw warning state effects. |

## Route coverage table

| Required route from earlier spec | Blueprint coverage | Status | Notes |
| --- | --- | --- | --- |
| Opening trunk | 8 working nodes | Covered | Establishes origin, capacity, wars, and lanes. |
| Hunger lane | 9 working nodes | Covered | Improves targeting and capacity reliability without raising the cap. |
| Stone hide lane | 8 working nodes | Covered | Gives armor identity and counterplay. |
| Tunnel lane | 8 working nodes | Covered | Adds rough-terrain and controlled-resource movement. |
| Brood hierarchy | 3 shared nodes and 10 route nodes | Covered | Swarm and elder are the only main mutual exclusion. |
| Surface terror | 8 working nodes | Covered | Adds panic and hostile response escalation. |
| Continental maw | 10 working nodes | Covered | Supports world-end without bypassing required state gates. |
| AI branch behavior | Situation table and focus priority notes | Covered | Implementation still needs final `ai_will_do` and strategy plans. |
| Focus icon direction | Lane motif requirements | Covered by prior asset file and this blueprint | Final icons remain asset work. |
| Route tradeoffs | Per lane weakness and backlash notes | Covered | No lane is pure benefit without counterplay. |

## Implementation acceptance for this blueprint

A final tree can rename, split, merge, or reposition working nodes. It still satisfies this blueprint only if it preserves these design requirements:

- At least one early mandatory trunk and at least four visible lanes by the first major branch split.
- Hunger, stone hide, tunnel, brood hierarchy, surface terror, and continental maw all exist as felt gameplay paths.
- Brood method is a true mutually exclusive choice.
- Hunger does not violate the non-origin capacity cap.
- Stone hide has clear hard-attack counterplay.
- Tunnel improves stubborn resource-state movement without making the Host fast.
- Surface terror increases enemy disruption and world response.
- Continental maw supports the terminal branch but does not fire it alone.
- The tree uses route-specific AI and varied rewards.
- Every final focus has icon direction and final localisation written during implementation.
