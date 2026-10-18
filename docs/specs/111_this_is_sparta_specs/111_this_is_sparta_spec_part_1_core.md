# Event 111: This is SPARTA!!!

## Design identity

| Field | Specification |
| --- | --- |
| Current identity | Event 111, This is SPARTA!!! |
| Original catalog identity | 116 |
| Type | Minor Fire-Once |
| Required Chaos level | 1, as supplied in the accepted brief |
| Design status | To Be Reworked |
| Cluster | Unassigned |
| Country role | `SPARTA_TAG`, resolved through the full tag audit before implementation |
| Main experience | Establish a modern Spartan state, choose a durable political settlement, and sustain one of five major campaigns |
| Evolution | Age of Heroes, a separate high-Chaos development that introduces material Greek mythology |

All new names and semantic keys in this package are working labels for authors. Player-facing titles, descriptions, buttons, focus names, achievement text and political identity wording are writing directions. The accepted event title and five route names come from the user brief.

Sparta exists at the moment the successful entry event is shown. It already has independent territory in Laconia, a government, a capital, a returned host and a dedicated focus tree. The opening problem is making that state work. Founding is never a later reward for completing the first branch.

The player has two sources of strength. The finite returned host supplies experienced soldiers, confidence and a military institution. The modern population supplies the recruits, engineers, workers and administrators required for a lasting state. Ancient arms help define the opening and its visual identity. They do not remain an adequate answer to artillery, aircraft and armor.

## The campaign promise

Sparta should feel formidable in a narrow battle and vulnerable in a prolonged campaign. Its early formations have good cohesion and demanding supply requirements, while the country lacks reliable maintenance, technical education and a broad citizen body. The player can win an opening encounter and still lose the campaign by ignoring rifles, civilian cooperation or the road to the front.

The central choice is which institutions the returned warriors will share. A renewed dyarchy can bind military authority to ephor oversight. A broader citizenship settlement can make modern residents full participants. Military supremacy can mobilize quickly and preserve a privileged warrior core, while accumulating domestic friction and relying more heavily on coercive occupation abroad. Every direction has a viable main campaign. None supplies free manpower without population, factories without capacity, or automatic obedience from conquered people.

The five conquests pursue different kinds of power. Spartan Hegemony is a Greek settlement and a test of leadership among neighboring states. Legacy of Alexander is a long continental empire with multiple regional administrations. Thermopylae Avenged is a concentrated eastern war and a consequential Persian settlement. The Western Campaign is an overseas land war against industrial opposition. Hellenic Colonies Reborn is a naval network whose individual ports and treaties matter.

Age of Heroes changes the nature of power after the player has encountered a functioning historical revival. Mythic beings acquire real military and political roles. Their service depends on places, agreements and constraints the player can understand. Conventional modernization remains necessary because supernatural forces cannot replace a full field army, industrial economy or escort fleet.

## Entry territory and immediate founding

### Laconia as a real starting state

The implementation must create a Laconia state through a build-time split of the current Peloponnese geography. The committed state snapshot identifies the larger Peloponnese as state 186. It does not identify a separate Laconia state. Exact new state ID, provinces, capital province and coastal facilities are resolved from the installed map and collision audit described in [Part 8](111_this_is_sparta_spec_part_8_implementation_and_ai.md).

The new state must include the real Spartan location and a coherent part of Laconia. Its boundary must be playable and geographically defensible. Population, existing factories, slots, resources, infrastructure, airbase capacity, victory points, supply connections and bookmark ownership are divided from the parent state without duplication. A supply connection or modest coastal facility may be part of the authored map revision when the installed map requires it, with its capacity explicitly balanced in the country package. Transferring the whole Peloponnese is not the default substitute.

The rest of the Peloponnese remains available for the first territorial campaign. Existing Greek cores are not erased. Greece can recognize, contest or negotiate with the new country. The same rule applies if another country currently owns Laconia.

### Entry eligibility

The random event is eligible only when the following facts can be satisfied in the same founding transaction.

| Requirement | Reason and behavior |
| --- | --- |
| Event identity is unused in the current campaign | Current 111 and migrated legacy 116 receipts count as the same Spartan incident |
| The audited Laconia state exists | A missing map dependency makes the event unavailable |
| Laconia has a valid owner and a resolved controller | A contested state cannot be treated as a peaceful transfer by assumption |
| A valid capital and deployable location are available | Country setup and unit creation cannot run in a dormant tag without land |
| The former owner can continue to exist with a legal capital | A one-state human country is not silently deleted to create Sparta |
| Existing troops have a legal disposition | The event cannot steal, duplicate or delete another country's formations |
| The Spartan tag and required packages are available | A collision or missing custom unit provider blocks selection instead of creating a generic substitute |

Current ownership and control are sampled again at commit. A changed owner, capital loss or competing release invalidates the pending transaction. The shared manual-failure surface explains the failed prerequisite when a manual fire was requested. Normal random selection treats the event as unavailable and selects other eligible content.

The default founding transfers a settled state whose owner also controls it. An occupied Laconia requires a separately validated handover path in the installed engine before that variant may be enabled. This bounds the release logic while leaving the event able to appear under a Greek, foreign or alternate-history owner.

### The founding transaction

The shared entry prepares the future Spartan actor before the event history row is recorded. Within the same successful flow it transfers the audited state, sets the capital, installs the country package, loads the dedicated tree only for the genuinely created Spartan country, registers custom military content, grants the measured opening package and records the finite arrival cohort. The arrival receipt is committed once.

The former owner keeps its remaining territory, government, characters, focus tree, equipment and armies. Its capital moves only if necessary and only to a validated remaining location. Existing wars are handled through explicit native country-release rules. Sparta does not inherit an arbitrary set of wars merely because Laconia had a previous owner, and the event does not end those countries' unrelated wars.

The receiving player sees a concise explanation of the new state and its immediate weaknesses. A human former owner retains control of their current country by default. A separate explicit option can offer switching to the new Sparta after the country exists. A timed confirmation defaults to staying with the current country. Multiplayer never transfers another human's country control.

### Immediate neighboring reaction

The former owner receives a scoped response about territory and recognition. Its choices concern a temporary settlement, negotiations over the border, or preparation to contest independence. No response makes Sparta retroactively unfounded. Acceptance can create a limited ceasefire or nonaggression arrangement when the corresponding native mechanism is verified. Refusal creates diplomatic hostility and access to a bounded territorial demand, not an instant all-world war.

A Greek government receives a more specific dispute over common identity and Laconian sovereignty. A foreign occupier or annexing power sees a challenge to its existing administration. A living Macedonia or restored Persia receives later route-specific interactions. They do not need to be present at birth.

The opening has no invulnerability period. Its protection comes from a coherent starting area, an appropriate army, attainable early actions and AI restraint about wars it cannot support. A hostile human neighbor can still attack through normal legal mechanics.

## Opening scale and first decisions

The opening bands are tuning anchors within a bounded dynamic calculation. They are selected from actual regional opponents, the campaign's technology environment, supply and the state being created. The late band requires both a later date and materially modern nearby opposition. Calendar year alone does not produce a large army.

| Opening band | Returned host anchor | Modern local formation anchor | Civic Settlement | Military Adaptation | Main pressure |
| --- | ---: | ---: | ---: | ---: | --- |
| Weak | 2 brigades of 2,000 | 1 brigade of 3,000 | 25 | 10 | Few trained locals and a narrow economy |
| Normal | 3 brigades of 2,000 | 2 brigades of 3,000 | 25 | 15 | Recognition, rifles and basic transport |
| Severe | 5 brigades of 2,000 | 3 brigades of 3,000 | 20 | 20 | Strong regional enemies and expensive sustainment |
| Late | 6 brigades of 2,000 | 4 brigades of 3,000 | 20 | 25 | An obsolete core in a mechanized and aerial battlefield |

These are manpower ceilings, subject to native template verification. Modern local personnel come from available recruitable population. Missing population or equipment creates an understrength formation or a smaller viable package. It does not create fictional local residents. The finite ancient cohort is an explicit event arrival, separately recorded from local population.

Interpolation can vary formation count within the accepted range and change readiness, supply stock, transport assistance and equipment completeness. It cannot exceed the upper band by counting every division in a distant enemy faction. Relevant opposition is the reachable regional force that can threaten Laconia. The calculation never scales directly with the player's later successes and never refills the original host.

The state starts with two research slots. Technical education, a working research network and late imperial research institutions unlock the third, fourth and fifth slots. Starting technology is a narrow validated basket of basic administration, civilian industry and contemporary small arms. A bounded late-start catch-up fills essential prerequisites, while armor, modern air power and a capable navy remain meaningful investments.

### Early play rhythm

| Period | Player priorities | Visible choices and consequences |
| --- | --- | --- |
| First week | Understand the state and stabilize supply | Inspect the three starting institutional problems, protect the capital connection and choose the first emergency program |
| First month | Decide how to equip and administer the revival | Negotiate rifles, convert a limited set of survivors, restore local administration or concentrate on training |
| First season | Make the Agoge sustainable | Admit modern recruits, decide how citizenship affects service and support one viable industrial program |
| First year | Establish a political settlement and strategic direction | Build an army that can replace losses, choose partners or rivals and commit to one conquest route |
| Expansion phase | Turn battlefield gains into usable territory | Complete regional settlements, repair ports and rail, manage clients and recover from failed operations |
| Late campaign | Defend the chosen order | Sustain the final empire or league, address succession and war exhaustion, and decide how to govern material mythology if it appears |

The first useful decision is affordable from the opening package. The player must have at least two meaningful first focuses available, normally administration and military adaptation, with industrial recovery also visible. A requirement for a building or equipment type the country cannot yet obtain must have a disclosed alternative. Basic survival cannot depend on paid DLC or another random event firing.

## Shared public values

### Civic Settlement

Civic Settlement represents how far the returned government has established a workable relationship with modern residents and incorporated institutions. It is not a claim that every resident agrees with the regime. It ranges from 0 to 100 and is displayed as an integer with the next important threshold.

| Band | Meaning | Gameplay effect direction |
| --- | --- | --- |
| 0–19 | Founding settlement is failing | Crisis recovery becomes prominent, expansion commitments are restricted and coercive shortcuts carry additional costs |
| 20–39 | Provisional order | Basic programs work, while wider recruitment and difficult diplomacy remain constrained |
| 40–59 | Recognized institutions | Normal civic recruitment, negotiated integration and durable partner agreements become available |
| 60–79 | Broad working settlement | Larger occupations and league responsibilities can be managed, with better access to consensual integration |
| 80–100 | Established civic order | The most demanding reform and stable imperial settlements become achievable |

Civic gains come from completed administration, citizenship agreements, supplied relief, successful regional settlements and honored diplomatic terms. Losses come from broken agreements, rushed coercive integration, domestic crises and actual failures of military provisioning. Routine combat casualties are handled by existing systems and are not converted into an unbounded daily Civic penalty.

Repeatable recovery has diminishing returns above the recovery band. An emergency measure can restore a country from crisis, but cannot be clicked repeatedly to reach 100. Lasting high values require completed institutions and successful obligations. Each value-changing operation records its source, clamp, cooldown and actual applied amount.

### Military Adaptation

Military Adaptation measures the integration of modern weapons, logistics, training and command across Spartan institutions. It ranges from 0 to 100. It does not replace technology, doctrine, division experience or equipment stockpiles.

| Band | Meaning | Gameplay effect direction |
| --- | --- | --- |
| 0–24 | Returned military practice dominates | The ancient host retains its opening limitations, modern cadre conversion is restricted and transport shortages matter |
| 25–49 | Functional transition | Basic modern cadres, support services and the first combined-arms programs become available |
| 50–74 | Modern army | Larger cadre intake, dependable staff work and route-specific operational programs become viable |
| 75–100 | Mature military institution | Advanced route doctrines and demanding imperial logistics are supported |

Adaptation rises through actual conversion programs, equipped exercises, technical education, support-service construction and validated modern research. It does not rise from changing a division template back and forth. The same cohort, technology or exercise stage cannot be counted twice. A shortage can reduce the effectiveness of units without automatically erasing decades of learned knowledge. Severe institutional disruption uses a clearly signaled stage setback rather than a constant oscillating meter.

### Mythic Strain

Mythic Strain appears only after Age of Heroes activates. It records the pressure created by maintaining and exploiting impossible powers. Its full rules, bands, recovery and consequences are in [Part 5](111_this_is_sparta_spec_part_5_age_of_heroes.md). Before activation the category has no empty third row or unexplained supernatural gauge.

### Other information

Route commitments, partner status, port access, investigation status, original-cohort receipts and regional settlement results use flags, qualitative labels or transaction records. The design adds no other permanent public currency. Native political power, command power, stability, war support, manpower and equipment remain useful and visible.

## Institutional effects and military limits

The country has at most three simultaneous focus-tree-owned national spirits. The three slots represent the political settlement, the military institution and state capacity. Opening penalties and later benefits replace stages within those slots. Every branch reward names the slot it changes or names a different genuine consumer such as a state program, unit trait, technology bonus or timed mission effect.

Age of Heroes follows the same budget. Divine government changes the political slot. Mythic logistics changes the relevant state-capacity stage. Hero traits belong to actual characters and powers belong to their genuine units or scoped operations. The implementation must not hide a fourth tree spirit under a new label.

Ordinary infantry, artillery, trucks, armor, aircraft and ships use normal equipment families after compatibility inspection. The returned host and modern Spartan cadre are custom human families. The ancient host cannot be recruited indefinitely. Its surviving personnel can enter modern cadre formations through a conserved conversion. Modern cadres can then be trained from eligible contemporary recruits, with the normal manpower and equipment costs.

The population remains human at birth and throughout normal conquest. A country can be a special Chaos actor while using normal civilian systems. Mythic soldiers do not automatically transform all residents into nonhuman beings. The late sacred dyarchy receives a separate classifier review because genuinely divine rulers change institutions, while its civilian population remains modern and human.

## Commitment, progress and failure

The route selection is initially exploratory. The player can view every route's premise, first regional goals, diplomatic demands and military needs. A route commits at its first irreversible territorial charter or expansion mandate. That action has a clear confirmation that lists the four routes being closed and the support branches that remain useful.

Once committed, a route does not change because a target becomes difficult. Its internal alternatives provide recovery. The eastern route can choose a northern corridor when its central passage is blocked. The western route can choose an Adriatic bridgehead. A colony network can rely on sovereign holdings or real treaty partners. Alexander's empire can use regional client kingdoms. These alternatives preserve the chosen campaign's identity.

Completion requires more than owning a list of states for one hour. The player must satisfy the selected territorial predicate, settle required regions, maintain a workable government and complete the final charter. A completed charter unlocks an enduring identity and an appropriate presentation beat. Losing a region later suspends bonuses that depend on control, while preserving the historical fact of having achieved the charter. It does not repeatedly award the same formable, achievement progress or Chaos.

### Recovery ladder

| Setback | Immediate effect | Available recovery | Lasting consequence |
| --- | --- | --- | --- |
| Rifles or transport run short | Readiness and project progress suffer | Reduce the next intake, buy or produce equipment, negotiate limited aid | Aid obligations and missed opportunities remain recorded |
| Civic crisis | Expansion is restricted and recovery actions rise in priority | Honor a citizenship settlement, suspend a coercive policy or fund relief | A political stage may change and a broken promise cannot be erased |
| Failed offensive | The route pauses at its current anchor | Refit, choose the route's alternate corridor, seek a limited peace | War losses and diplomatic distrust remain |
| Lost client or port | Dependent bonuses and map cells become inactive | Restore the treaty, secure another explicitly allowed site or recover the original | A vanished partner is not replaced by a duplicate tag |
| Loss of Laconia while Sparta survives | Founding and mythic services are disrupted | Retain the legitimate surviving government and pursue a restoration objective | No second returned host or second founding grant |
| Capitulation or annexation | Event-owned growth stops and pending transactions cancel | A later legal restoration can recover surviving institutional progress | Unique deaths, consumed artifacts and original-cohort losses persist |
| Mythic rupture | The affected power becomes unavailable and a regional containment task opens | Contain, release or bind the manifestation under stricter terms | Its rupture receipt and any permanent loss persist |

A political failure should leave meaningful choices before it becomes a final defeat. Emergency military rule can stabilize a crisis at an institutional cost. A civic compromise can rescue recruitment while abandoning a privileged arrangement. A foreign treaty can preserve the state while constraining expansion. None silently selects another route on the player's behalf.

## Chaos impact map

These values are first-pass tuning anchors for distinct abnormal consequences. The shared Chaos system retains responsibility for ordinary wars, annexations, puppeting, factions, deaths and related changes. Evolution eligibility, activation, branch unlocks and log entries award zero Chaos by themselves.

| Milestone or outcome | Why Chaos changes | Anchor and dynamic rule | Repeat guard | Shared-source overlap | Containment counterpart |
| --- | --- | --- | --- | --- | --- |
| `C111_FOUNDING` | A materially returned ancient host establishes an independent modern state | +5. Use +3 for a very small peaceful founding footprint, +5 otherwise | Once for current 111 and migrated 116 identity together | State transfer, liberation and ordinary political changes keep their own shared accounting. This premium measures the anomalous polity | `C111_DISSOLUTION` |
| `C111_GREEK_REACH` | The revived state becomes a durable Greek regional power | +5 when the first required Greek regional settlement is held for 90 days | Once, shared by all five routes | No reward for every province, factory or annexation | Included in durable dissolution, not repaid per state |
| `C111_PARTNER_ORDER` | Other real governments accept a lasting Spartan-led political order | +3 after the first qualifying partner agreement survives 90 days with its material obligations satisfied | Once for the event, not once per client | A normal faction or puppet action is counted by the shared source. The premium concerns recognition of the returned institution | Collapse of the abnormal order is part of dissolution |
| `C111_TRANSREGIONAL` | The Spartan state establishes sustained power beyond its original Greek region | +10 after a required non-Greek regional settlement and its supply or treaty obligation are maintained for 90 days | Once across all routes | The abnormal actor's reach is distinct from each ordinary war or annexation | Included in a later major containment result |
| `C111_ROUTE_ORDER` | A complete route establishes a durable imperial or maritime order | +10 for Hegemony, +15 for Thermopylae, Western or Colonies, +20 for Alexander. The final charter and all required administration are necessary | One selected-route completion receipt | No separate premium merely for the cosmetic rename or super-event playback | `C111_MAJOR_CONTAINMENT` when the qualifying power is later permanently dismantled |
| `C111_HERO_PROOF` | A named mythic being becomes materially present and accepts a real service role | +10 for the first verified heroic presence | Once, even if evolution starts at high Chaos | This is the concrete being, not the evolution activation | `C111_PERMANENT_SEAL` |
| `C111_IMPOSSIBLE_FORCE` | The first nonhuman military family becomes operational | +10 for the first fielded Spartoi, Talos or Stymphalian package. Later families do not each repeat this grant | One shared first-capability receipt | Ordinary military buildup remains shared | Permanent sealing of all operational mythic families |
| `C111_RUPTURE` | An exploited manifestation causes a real regional loss of control | +3 for the first bounded rupture, +5 instead if it disrupts two distinct registered sites. The larger severity replaces the smaller award through a difference receipt | One award with one possible severity upgrade, never a repeatable farm | Any actual deaths or destruction are accounted separately and not priced again here | Successful durable containment can contribute to the sealing reduction |
| `C111_DIVINE_SOVEREIGNTY` | Manifested twins assume the sovereign offices of an established state | +20 after the sacred dyarchy is materially installed and its prerequisites hold | Once | Abstract focus completion, ideology change and ceremonial presentation add nothing extra | Permanent removal of divine sovereignty under a valid containment settlement |
| `C111_COERCIVE_MANDATE` | A mature state uses operational mythic force to impose a new regional political settlement | +15 on the first completed coercive mandate settlement, never on choosing its branch | Once | Ordinary conquest and deaths retain shared sources | Included in major containment |
| `C111_PERMANENT_SEAL` | All event-owned operational mythic powers are durably released or contained | −10, only after heroic proof or impossible-force receipts exist and the settlement survives 180 days | Once. Reopening powers does not reset eligibility | Normal peace has its own accounting | The negative reward cannot be earned from a canceled investigation or temporary stand-down |
| `C111_DISSOLUTION` | The anomalous polity ceases to govern territory and its restoration machinery is durably dismantled | −3 for a local actor, −5 if Greek reach was earned, after 180 days | Once, mutually exclusive with the larger containment award | Ordinary annexation or liberation is separate | Surviving refugees and historical losses remain |
| `C111_MAJOR_CONTAINMENT` | The material mythic sovereignty or coercive institutions of an established Spartan power are permanently removed under an authenticated containment settlement | Requires a prior `C111_TRANSREGIONAL` or `C111_ROUTE_ORDER` receipt and a prior actual `C111_COERCIVE_MANDATE` or `C111_DIVINE_SOVEREIGNTY` receipt. After 180 days of durable removal, use −15 if the route receipt exists and −10 otherwise | Once. If a local dissolution reduction already applied, award only the difference. `EX03`, ACH20 and the conditional international-defeat presentation share this qualifying-opponent predicate | No refund of total historical wars, deaths or annexations. A sacred government need not have been coercive to possess material mythic sovereignty | This is the final event-specific reduction band |

No new positive award scales by multiplying it against the current Chaos value. A late campaign can reach more milestones because it permits greater events, while each incident retains a readable magnitude. The normal path's direct positive anchors are bounded by its actual completed stages. Mythic abuse cannot manufacture an endless loop of rupture and containment points.

The ownership-change and settlement callbacks evaluate only registered Spartan roles and route states. The package does not add a recurring worldwide search for stronger countries. Every Chaos row contains the actual actor, event identity, reason, applied amount and milestone receipt through the shared history path.

## Player information and presentation

The opening event communicates the independent country's appearance, its finite veteran core and the gap between warrior skill and modern state capacity. It should convey immediate physical presence through soldiers, terrain and equipment. It should not rely on bureaucratic mystery, documents or an extended explanation of implementation details.

The country decisions show Civic Settlement, Military Adaptation and, after activation, Mythic Strain. The normal decision surface handles costs, missions and available actions. The active route receives one compact exact-shape state puzzle whose cells distinguish ownership, control, valid partner status, active settlement and disputed requirements. The same predicate controls the final action and the cell state.

The player should be able to identify the next missing requirement without opening every focus. Route tooltips name required geographic groups and permitted alternatives. A vanished Macedonia changes a diplomatic option's availability and explanation. It does not leave a permanently impossible focus with no route continuation. A disputed Persian capital resolves to the actual Persian actor and territory.

Reports are local and actionable. News is reserved for changes other countries need to understand. Super-events are reserved for earned route completion and the major mythic moments defined in [Part 7](111_this_is_sparta_spec_part_7_presentation_and_assets.md). The opening Minor event does not receive a global super-event simply for being selected.

## Specification map

| Part | Purpose |
| --- | --- |
| [Part 2](111_this_is_sparta_spec_part_2_country_and_military.md) | Country package, political institutions, technology, economy, armed forces and replacement paths |
| [Part 3](111_this_is_sparta_spec_part_3_focus_routes.md) | Shared focus architecture, five route branches, geographic sets, locks and postwar payoffs |
| [Part 4](111_this_is_sparta_spec_part_4_decisions_and_settlements.md) | Action records, missions, citizenship, territorial settlements and treaty handling |
| [Part 5](111_this_is_sparta_spec_part_5_age_of_heroes.md) | Evolution, mythic characters and forces, Strain, divine politics and counterplay |
| [Part 6](111_this_is_sparta_spec_part_6_connections_and_achievements.md) | Cross-event interactions, difficult achievements and their tracking contracts |
| [Part 7](111_this_is_sparta_spec_part_7_presentation_and_assets.md) | Art, flags, portraits, UI, models, sound, animation and major presentation beats |
| [Part 8](111_this_is_sparta_spec_part_8_implementation_and_ai.md) | Engine boundaries, geographic integration, identity migration, AI and validation scenarios |

Historical and repository evidence is recorded separately in the package's research and evidence files. The design uses Xenophon's account of Spartan institutions, Plutarch's account of civic reform and ancient literary mythology as inspiration. All numerical balance, modern political outcomes and supernatural military mechanics are authored game design.
