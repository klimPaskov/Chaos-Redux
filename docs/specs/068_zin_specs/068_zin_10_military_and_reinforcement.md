# 068 ZIN: armies, creatures and reinforcement

## Strength has several meanings

The country registry gives exact proposed starting formation counts. This roster gives the bodies, equipment, battlefield role and replacement contract behind each formation. Formation counts do not identify physical creature numbers. Five Sunhot formations contain far fewer beings than five ordinary human divisions and are much stronger in a suitable battle.

The numerical profile uses a reference human formation indexed at 100 for attack, defense, organization and supply demand. These are design benchmarks, not literal HOI4 modifier values. An attack index of 1000 means a target approximately ten times the reference offensive output in the controlled comparison before terrain and combined-arms effects. The implementation agent must translate the benchmark into verified subunit and equipment definitions and then test it. It must never paste an index of 1000 into an assumed native stat field.

The reference formation uses 5,000 human personnel, 500 infantry equipment and 50 support equipment. The equipment ratio follows an abstract formation package. It is not a statement that every physical soldier owns only one tenth of a weapon. For creature formations, bodies and supporting material are separate requirements. Manufacturing harnesses cannot create a giant.

Attack and defense indexes are starting tuning proposals. They are deliberately high for major creatures. A balanced playtest should first adjust access, deployment numbers, replacement, terrain and supply. It must not quietly reduce Sunhot elves, giants, dragons or named heroes to ordinary infantry.

## Recruitment and population ownership

A founding army is a real external arrival. Its personnel and equipment receive one arrival receipt separate from civilian settlement. A stockpile grant, manpower addition and creation of a formation cannot each claim to bring the same people three times. The country package must have enough actual and typed personnel for every starting unit before the transfer commits.

Human arrivals can contribute to ordinary human recruitment after resident policy permits it. Elves, giants, goblins, demons, undead and other beings require a typed reinforcement pool and an authorized template. Earth residents never become another species through a core, conscription law, template conversion or country annexation.

A typed pool is internal replacement accounting. It is not another public currency or a shop. Players see available formations, their requirements and replacement status. They pay only the established PP, CP, equipment or factory costs when a project requires those resources.

The implementation must prove that changing or disbanding a template cannot convert a scarce creature permit into ordinary manpower and then back into extra creatures. Restricted formations use the verified locked-template and event recruitment pattern. If the installed engine cannot enforce a proposed path, keep that path unavailable until the restriction is proven, rather than allowing unlimited training and labeling the army rare.

Disbanding a formation returns only surviving accounted personnel and recoverable equipment. Capturing a stockpile does not transfer the loyalty, knowledge or living bodies needed to form its creatures. Annexation can transfer surviving units through an explicit settlement, corruption or service agreement. It cannot multiply them.

## Common replacement rule

Each formation family has a proposed replacement project cadence in the table. A country normally sustains one project of a given family at a time. A completed project restores up to 25 percent of that family's original founding strength or creates the same finite equivalent when the project explicitly admits a new formation. The project consumes its full equipment share and the actual typed bodies. It does not refresh the whole starting army.

The cadence is not a free periodic spawn. Its requirements include a secure crossing or a demonstrated local recruitment institution, supplied deployment space, an eligible government and the necessary trained beings. Rare units can recover after losses without becoming an endless stream. Ordinary human forces eventually use normal production and recruitment, subject to their military route.

The 120-day founding bridge supports survival while the local economy is organized. Its expiry stops unsupported reinforcement and imposes the stated supply problem. It does not destroy surviving units or punish every enemy with a global debuff.

## Formation profiles

| Profile | Humans | Typed beings | Attack | Defense | Organization | Supply | Project cadence |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |

| line | 5,000 | 0 | 100 | 100 | 100 | 100 | 90 days |
| light | 5,000 | 0 | 95 | 100 | 100 | 80 | 90 days |
| heavy | 5,000 | 0 | 150 | 125 | 100 | 125 | 120 days |
| mounted | 5,000 | 0 | 125 | 90 | 100 | 110 | 120 days |
| engineer | 2,500 | 0 | 60 | 110 | 100 | 90 | 120 days |
| marine | 5,000 | 0 | 100 | 100 | 100 | 100 | 120 days |
| elf | 0 | 1,000 | 250 | 250 | 150 | 75 | 180 days |
| orc | 0 | 5,000 | 175 | 125 | 90 | 125 | 120 days |
| goblin | 0 | 2,500 | 90 | 100 | 100 | 75 | 120 days |
| ogre | 0 | 500 | 500 | 350 | 100 | 200 | 180 days |
| giant | 0 | 100 | 1000 | 750 | 125 | 250 | 270 days |
| troll | 0 | 250 | 600 | 600 | 100 | 175 | 180 days |
| yeti | 0 | 500 | 400 | 500 | 125 | 150 | 180 days |
| ent | 0 | 100 | 850 | 1200 | 150 | 200 | 270 days |
| demon | 0 | 500 | 500 | 350 | 125 | 150 | 180 days |
| shachihata | 0 | 100 | 1200 | 900 | 150 | 300 | 270 days |
| sunhot | 0 | 250 | 1500 | 1500 | 175 | 200 | 270 days |
| mycid | 0 | 1,000 | 175 | 300 | 150 | 125 | 180 days |
| grave | 0 | 5,000 | 250 | 250 | 100 | 150 | 180 days |
| beast | 250 | 250 | 500 | 300 | 100 | 200 | 180 days |
| dragon | 250 | 5 | 2000 | 1000 | 150 | 300 | 360 days |
| hero | 250 | 0 | 2500 | 2000 | 200 | 100 | 180 days |

The hero row counts the personal guard. Einendil is the one named individual attached to that formation and commander package. His identity cannot be duplicated by a normal replacement project. His recovery follows the specific 180-day route in the succession document.

## Exact unit inventory

Every key below has its own registry record. A shared profile provides a baseline, not permission to use identical politics, counter art, equipment identity, replacement sources and visual design for all regional units.

| Unit key | Profile | Starting country users | Specific requirement |
| --- | --- | --- | --- |

| `rush_line` | line | rush | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `noris_line` | line | noris | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `dondor_guard` | line | dondor | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `rush_island_guard` | line | rush_islands | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `enhesis_river_guard` | line | enhesis | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `goodin_guard` | line | goodin | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `zhen_guard` | line | zhen | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `ihuj_guard` | line | ihuj | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `white_host_line` | line | lerenwaith | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `yeldenne_guard` | line | yeldenne | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `rush_frontier` | light | rush | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `gunwaith_highlander` | light | gunwaith | Mountain defense +50 percent. Research improves ordinary equipment without deleting the clan military identity. |
| `girdon_warden` | light | girdon | River defense +50 percent. Its contracted goblin engineers remain a separate northern company, not a human template conversion. |
| `keredr_militia` | light | keredr | Local defense +25 percent in settled states. No special offensive superiority. |
| `goodin_light` | light | goodin | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `selen_ranger` | light | Focus, charter or succession only | Human elite Rangers. Forest attack and defense +50 percent. Independent charter is mandatory. Afrit cannot recruit them through an ordinary goblin or monster pool. |
| `dondor_shock` | heavy | dondor | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `buldor_heavy` | heavy | buldor | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `white_host_guard` | heavy | lerenwaith | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `yeldenne_warden` | heavy | yeldenne | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `ash_warrior` | heavy | goldoroth_ash | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `afrit_servant` | heavy | afrit | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `huhun_rider` | mounted | rush | Human mounted Rush tradition. Plains movement +25 percent. Remount services are real support equipment and trained mounts, not a new public currency. |
| `noris_camel` | mounted | noris | Desert movement and defense +50 percent. Cold movement penalty 25 percent. Requires the Noris package or a delivered contract. |
| `adel_rider` | mounted | adel | Rapid coastal and plains intervention. Movement +25 percent. No scripted teleport to an unconnected frontline. |
| `buldor_engineer` | engineer | buldor | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `white_host_engineer` | engineer | lerenwaith | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `flame_support` | engineer | goldoroth_ash | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `zhen_arcanist` | engineer | zhen | Human or near-human magical support direction remains proposed. Benchmark attack 200. Projects use state-targeted actions, not invented engine spell APIs. |
| `enhesis_marine` | marine | enhesis | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `rush_island_marine` | marine | rush_islands | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `pulundur_marine` | marine | pulundur | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `rafby_marine` | marine | rafby | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `deepwatch_marine` | marine | sodoloro | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `ihuj_marine` | marine | ihuj | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `kradlon_marine` | marine | kradlon | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `elven_line` | elf | magical_elves | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `elven_ranger` | elf | magical_elves | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `god_forest_guard` | elf | god_forest | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `corrupted_elf` | elf | Focus, charter or succession only | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `bloody_orc` | orc | bloody_orcs | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `sea_orc` | orc | pulundur, kradlon | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `stabillo_orc` | orc | stabillo | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `black_orc` | orc | blackton | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `blackton_guard` | orc | blackton | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `gate_orc` | orc | dark_gate | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `hell_orc` | orc | volgan | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `goblin_engineer` | goblin | girdon, stone_goblins | Typed goblin engineer company. Fort and crossing support. Girdon access is a specific proposed contract, never an ordinary Rush entitlement. |
| `stone_goblin` | goblin | stone_goblins | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `nothings_goblin` | goblin | nothings | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `goblin_infiltrator` | goblin | nothings | Infiltration uses a paid targeted action and evidence receipt. Mere deployment never deletes enemy equipment. |
| `snow_goblin` | goblin | worldond | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `eye_ogre` | ogre | eye_ogres | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `ogre_porter` | ogre | eye_ogres | Support-focused ogre formation. Attack benchmark 250 and supply support role. Cannot grant an unlimited global supply bonus. |
| `ogre_marine` | ogre | rafby | Transport-trained ogres. Landing penalty reduction is narrower than ordinary full marine specialization. |
| `goldoroth_ogre` | ogre | goldoroth_ogres | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `ogre_siege` | ogre | goldoroth_ogres | Fort attack +75 percent, movement penalty 25 percent. Siege effects need a real battlefield or selected-state operation. |
| `ice_ogre` | ogre | horidor | Winter shock host. Cold attack +50 percent. Mammoths remain a separately reinforced formation. |
| `demonic_ogre` | ogre | volgan | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `titanos_giant` | giant | titanos | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `forgotten_giant` | giant | forgotten_giants | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `hiloron_giant` | giant | Focus, charter or succession only | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `corrupted_giant` | giant | Focus, charter or succession only | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `fog_troll` | troll | fog_trolls | Hill and mountain defense +50 percent. Fog is cultural identity until a verified weather consumer supports a live fog bonus. |
| `flame_troll` | troll | stabillo | Fire tradition does not grant universal chemical, nuclear or supply immunity. |
| `endless_troll` | troll | endless | Siege and cave identity. Fort attack +50 percent through a verified combat modifier. |
| `reef_troll` | troll | sodoloro | Coastal defense +50 percent. Does not walk between sea provinces as a land army. |
| `frost_troll` | troll | frost_trolls | Winter defense +75 percent, hot-climate movement penalty 25 percent. |
| `coldor_yeti` | yeti | coldor | Winter and mountain advantage +50 percent, warm-climate attrition exposure +25 percent unless provisioned. |
| `worldond_yeti` | yeti | worldond | Organized winter army. Winter defense +50 percent. Supply preparation can remove warm expedition penalties but cannot turn it into a desert specialist. |
| `kilinti_ent` | ent | Focus, charter or succession only | Forest defense +100 percent. Movement -50 percent. Logging disputes follow its charter. No free forest biome transformation. |
| `forest_guardian` | ent | god_forest | Sunhot guardian tradition. Forest defense +75 percent. Not automatically the same species or political identity as Kilinti ents. |
| `bound_ent` | ent | Focus, charter or succession only | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `afrit_demon` | demon | afrit | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `volgan_herald` | demon | volgan_children | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `netherborn` | demon | volgan_children, volgan | Already Volgan-owned when supplied by the Dead Lands. No default neutral allegiance lottery. |
| `volgan_guard` | demon | volgan | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `shachihata_demon` | shachihata | shachihata | Very large, rare demons. Needs a separate measured model scale and ample local supply. |
| `sunhot_elf` | sunhot | sunhot_elves | Over three meters tall in the lore. Exceptional formation strength is controlled by finite bodies and slow replacement, not ordinary infantry statistics. |
| `mycid_guard` | mycid | mycids | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `mycid_spore` | mycid | mycids | Regional identity, equipment and replacement follow the owning country package. Access to this unit does not change political allegiance. |
| `grave_host` | grave | volgan_children, volgan | Finite realm reinforcement or verified new-death trigger. Destroyed undead do not supply a new civilian-death tranche. |
| `warg_rider` | beast | bloody_orcs | Independent orc rider and mount package. No ordinary Rush recruitment. Rider and mount losses consume their correct pools. |
| `mammoth_host` | beast | horidor | Mammoths with support personnel. Slow cold-terrain force with separate creature scale and rig. |
| `mazerin_beast` | beast | volgan | Direct Volgan regional beast host. Separate nonhumanoid rig and sound brief. |
| `dragon_mountain_host` | dragon | Focus, charter or succession only | Dragon Mountain military tradition. Elven route only. Five dragons plus handlers form one rare host. No sovereign dragon identity. |
| `sunhot_drake` | dragon | Focus, charter or succession only | Eligible Sunhot route. Distinct fire-drake appearance and support. No separate Great Volcano dragon country. |
| `afrit_dragon` | dragon | Focus, charter or succession only | Corrupted or bound dragon host, acquired through an explicit operation. Corruption transfers existing living creatures without duplicating them. |
| `einendil_guard` | hero | Focus, charter or succession only | One named hero and personal guard. Strongest individual fighter does not mean the strongest whole army. One active physical formation and one commander identity. |

## Rush and the specialist peoples

The initial Huhun contingent represents a limited pre-existing royal obligation. It does not grant Rush an unlimited rider pool before the Huhun charter. Selen, Hiloron and Kilinti recruitment requires their own agreement. A dominion's territory, troops and replacement obligation remain connected throughout the succession.

A submitted dominion can provide surviving normal formations to Afrit's Rush government. Corrupted variants require a later specific action and retain the same physical personnel identity. A defeated or refusing dominion cannot provide its entire starting army again merely because a focus says that it has been subdued.

Independent orcs, goblins, trolls and ogres use their own diplomatic and military packages. An exceptional friendly clan needs an identifiable prior agreement and receives finite units. Such an exception never enables a general Rush monster recruitment branch.

## Dragons

The proposed gameplay representation is a rare land formation containing dragons and handlers. It has a winged creature model and appropriate movement and attack animation, but it remains bound to the army's supply, front and transport rules. A flight animation is not an air-wing mechanic. Dragons cannot become ships, teleport across oceans, conduct a strategic bombing mission or bypass every terrain restriction simply because their model has wings.

The first eligible dragon project takes 180 days and costs 100 PP and 500 support equipment, with the required elven or Afrit route, an accessible tradition and five admitted living dragons. The future military profile supplies the remaining family-specific material. Subsequent replacement is much slower, with the 360-day cadence in the registry. Sunhot drakes and Afrit-bound dragons have distinct visual and political identities.

A genuine aircraft-domain dragon system would need a separate accepted design, equipment rules, air missions, replacement, airbase behavior, counters and model consumers. That extension is not silently assumed in this package.

## Ships and maritime survival

A maritime country requires an operational port at founding. Its naval package arrives through the crossing and has an explicit ship roster, convoy grant, fuel or propulsion requirement and repair pathway. Ships are not spawned inland and a navy cannot be represented only by marine divisions.

| Package | Proposed first fleet | Convoys | Campaign role |
| --- | --- | ---: | --- |
| Rush Island Confederacy | 5 escort vessels and 5 light combat vessels | 50 | Defensive island fleet, royal transport and convoy protection. |
| Enhesis | 5 shallow-draft escort vessels | 50 | Trade routes, transport and local defense. River craft are narrative and support assets until a verified river consumer exists. |
| Rafby | 5 raider vessels and 5 escort vessels | 25 | Paid raiding, interdiction and captured-ship diplomacy. |
| Pulundur | 5 raider vessels | 25 | Narrow-sea operations and dark patron transport. |
| Sodoloro | 5 heavy coastal-defense vessels and 5 escorts | 25 | Strong home-water defense with limited distant projection. |
| IHUJ | 5 escort vessels | 25 | Island defense and safe transit between its settled ports. |
| Kradlon | 5 raider vessels and 5 escorts | 25 | Northern maritime raids and amphibious support. |

These vessel labels are design families. Their exact native hull, module, technology and visual representation must be chosen against installed game definitions. A supernatural-looking ship does not automatically gain a battleship's statistics. No aircraft carrier, submarine fleet or modern missile ship is implied.

Every fleet needs 180 days of initial operating supplies and a repair route. A trade colony can contract Earth maintenance. A raider can use a real captured port. A colony lacking fuel cannot operate indefinitely on a hidden exemption. A captured ship is transferred from a real opposing roster only when a supported transaction exists. Otherwise the relevant reward is equipment or compensation, clearly described as such.

## Terrain and counterplay

Major creatures have strong roles and real weaknesses. Ents defend forests and struggle to reposition. Giants excel at assault and siege but consume supply and cannot cover a wide front alone. Trolls are strong in difficult terrain with slow replacement. Sunhot forces can defeat much larger conventional formations, yet cannot be everywhere at once. Dragons give an eligible power a rare mobile shock host, not universal strategic reach.

Earth forces can build reconnaissance, fortification, supply denial, air support and concentrated anti-armor or artillery solutions through verified native mechanics. Biological or chemical susceptibility is not assumed from a fantasy species name. A species-specific environmental interaction requires the relevant shared-system adapter and evidence. The design does not grant all creatures blanket immunity to every weapon.

Defensive agreements and isolation are meaningful counters. Attacking a new colony without preparation should be dangerous. Waiting, trading and studying its actual demands should often be safer, without making peaceful choices mandatory.

## Three-power force tests

Before the Rush crown is captured, Volgan must exceed Afrit in effective military power by a large margin under the same supply and deployment conditions. His sixty starting formations include mixed powerful hosts, while Afrit begins with ten and depends on later political acquisitions.

The canonical Rush Kingdom must be the strongest common colony as a complete country package. Compare its ordinary army, specialist obligations, replacement, supply and industry against Dondor and the other baseline societies. A specialist enemy can win a favorable local battle without becoming the stronger overall common power.

After a successful Afrit usurpation and submission of the recognized dominions, The Ashen Throne should have a clear effective advantage over Volgan. Test the combined surviving army, production and reinforcement capacity. If normal succession losses make that advantage impossible, improve the usurpation's real consolidation and replacement routes. Do not create a fresh duplicate Rush army as a victory reward.

Einendil is the strongest individual warrior, but his personal guard cannot win a global war without allied formations, transport and supply. Sunhot power remains exceptional even when the good alliance loses a campaign through poor distribution or inadequate support.

## Models, counters and sound

Every major visually distinct family needs its own planned model package, counter identity and sound direction. Human regional variants can share a verified animation source when it fits their anatomy and weapons, but cannot use a renamed generic counter as their final art. Giants, ents, yetis, mycids, demons, Sunhot elves, dragons, grave hosts and mixed beasts require their distinct anatomy and scale treatment.

The 3D worker must inspect a named installed-vanilla reference, measure the source mesh and entity scale, apply scale once, verify the custom rig and every required action, export and reimport the actual mesh and animation, then provide the source-to-runtime handoff. The main agent owns the live entity and unit consumer. A render or provider completion is not in-game proof.

Selection voice routing may be country-wide in the installed consumer. Rush has several different creature families, so a per-subunit selection voice must not be promised without a supported engine path. Use a suitable approved country-level command identity where it genuinely serves the whole roster, and mark a requested incompatible per-species selection layer unresolved. Attack and movement sounds still require the correct entity consumer and sourced licensed audio.

No model, counter, sound file or engine-tested combat value is produced by this planning package. The asset and acceptance documents define their production and review gates.
