# 84 · Implementation acceptance scenarios

## Status

These are required future acceptance scenarios. They have not been run in HOI4. The planning turn performs only a parent-authored document consistency and packaging check, recorded separately in the package manifest. It is not an independent subagent review, a probability audit, a technology audit, or a live playtest.

Each executed scenario must record game/repository revision, setup, observed behavior, expected behavior, relevant files, and evidence. Group related checks into scenario saves so they are practical to run. Do not mark a test passed because a comment says the feature exists.

## Opening, progression, and accounting

| ID | Scenario | Pass condition |
|---|---|---|
| QA01 | Ordinary major origin | Exactly one eligible country starts at I15/R10, one local cell, no special army |
| QA02 | Player minor origin | A nonmajor human country is eligible without being counted twice if later major |
| QA03 | No valid origin | No partial setup, root reward, or erroneous global pacing transaction |
| QA04 | Origin selection through either cluster | Same root consumed once, both memberships correct, cluster pacing not duplicated |
| QA05 | Legacy Event 84 dispatch | No old global +100 PP payload remains reachable through the new root |
| QA06 | Repeated root invocation | Existing episode remains singular, no reset of Influence, cases, or stockpiles |
| QA07 | Influence band boundaries | Continuous coverage at 19/20,39/40,59/60,79/80 and fractional internal values |
| QA08 | Reaction band boundaries | Continuous coverage at 24/25,49/50,69/70,84/85 |
| QA09 | Monthly review and urgent check | Proration prevents a 10-day callback from paying a full30-day contribution |
| QA10 | Many war, cultural, and sponsor causes | Bucket and final caps work, current causes remain explainable |
| QA11 | Multiple foreign sponsors | Only one recipient foreign-network contribution per review |
| QA12 | Dormancy and reactivation | Dormant work stops, real new cause restarts it once, permanent laws remain |
| QA13 | Government transfer during queued callbacks | One successor owns the state, no doubled timers or delayed dead-tag rewards |
| QA14 | Two independent meters | I80/R90 possible, no forced inverse relationship |
| QA15 | Spirit budget and total modifiers | At most three Event 84 spirits, no old-tier stacking or overlapping route totals |
| QA16 | Pure equality reform | No inherent recruitment, fertility, research, or skill penalty from orientation or equality |
| QA17 | Explicit growth policy | Only future positive growth changes, living population and death count not reduced |
| QA18 | Shared civilian-loss event | Actual victims counted once and shared death-derived Chaos not duplicated |
| QA19 | Manual setup accounting | One declared Chaos addition, no retrospective root, congress, or spread bonuses |
| QA20 | Peace settlement reward | Maintained substantive settlement pays once, posture cycling cannot farm Chaos reduction |

## Decisions, characters, and political authority

| ID | Scenario | Pass condition |
|---|---|---|
| QA21 | Every decision page at peak availability | At most six primary actions and three active Event 84 missions across all categories |
| QA22 | Foreign target pagination | At most four targets plus navigation, browsing spends nothing and creates no mission |
| QA23 | Poor-country project | No negative equipment or factories, reduced scope declared before acceptance |
| QA24 | Cost band changes during project | Contracted costs remain fixed and spending is not duplicated |
| QA25 | Full, partial, failed, and canceled negotiation | Correct distinct outcomes and durations, no parent/child double mission; an external Event 82 remobilization uses the existing single 60-day repair extension without an automatic betrayal award, while deliberate repudiation or unrepaired expiry can fail |
| QA26 | Honest co-optation versus sham | Material authority and delivery determine result, no free repeated Stability |
| QA27 | Suppression with no surviving network | No indestructible underground bonuses remain |
| QA28 | Eradication success or failure | Specified costs and consequences, no population deletion from organizational closure |
| QA29 | Case evidence persistence | Save/reload does not reroll allegation truth or character identity |
| QA30 | Adult private-life case | No explicit imagery, unsupported real-person orientation, or inherently harmful orientation trait |
| QA31 | Protection, voluntary disclosure, fabrication exposure | Consent and evidence are distinguished, completed case cannot repay rewards |
| QA32 | Character changes role or dies | Active effects follow actual office and survival, no duplicated general/field-marshal benefit |
| QA33 | Leader political conversion | Cabinet and command authority matter, no universal instant flip from one trait |
| QA34 | Baseline peaceful takeover below200 Chaos | Ordinary political route functions without an evolution gate |
| QA35 | Every constitutional route | Distinct institutions and tradeoffs, complete early/middle/late path and aftermath |
| QA36 | Existing-country focus integration | Meaningful national tree preserved, no blanket replacement |
| QA37 | Event-created authority | Complete country package, all names/flags/roles/forces/tech/diplomacy covered |
| QA38 | Subject movement government | No sovereign treaty, faction, or resource power without actual autonomy authority; an Event 79 winner preserves the current constitutional government and cells, while Event 81 cancels ineligible sovereign tax work after actual puppeting |
| QA39 | Political reversal | Current valid identities and surviving assets preserved, no resurrected ruler or duplicate rewards |
| QA40 | Religious and secular flavour | Institutions fit the actual country, no universal religion-to-Reaction shortcut |

## Military, diplomacy, and terminal play

| ID | Scenario | Pass condition |
|---|---|---|
| QA41 | Chaos600 without repression | Armed Peace does not unlock automatically |
| QA42 | Two duplicate reports of one raid | They do not satisfy the two-distinct-incidents gate |
| QA43 | All four units train and reinforce | Native costs consumed once, correct manpower, equipment, caps, and actual deployment |
| QA44 | Training cancellation and formation conversion | Material conserved, spent resources not magically refunded, no cloned unit |
| QA45 | Home-territory tactical bonus | Correct supported scope, no global tank or foreign-unit bonus |
| QA46 | Supply failure and combat casualties | Units remain mortal and supply-dependent, no hidden immunity |
| QA47 | Air and naval programs | Actual aircraft/ships/ports/tech required, no landlocked fleet or extra research slots |
| QA48 | Civil-war eligibility | High I/R alone insufficient, real rupture and viable authority required |
| QA49 | One-state crisis | Playable capital/authority outcome, no unsupported state partition |
| QA50 | Civil-war material split | Pre/post ledger reconciles armies, ships, wings, equipment, manpower, population, and characters |
| QA51 | Existing external war during civil war | War and faction relationships remain valid and explicit; an Event 80 crash declaration is not vetoed by movement government, and ordinary mediation does not silently end it |
| QA52 | Peaceful reunification | Surviving assets merge once, treaties and actual leaders resolve correctly |
| QA53 | Postwar demobilization | Actual survivors and recoverable equipment only, no double return |
| QA54 | Bloc founding | Three qualified consenting sovereign members and valid faction membership resolution |
| QA55 | Congress obligations and human members | No spending another player's equipment or changing their laws without authority |
| QA56 | Refuge and migration | Actual surviving arrivals counted once, reception capacity and route matter |
| QA57 | Chaos1000 and majorityabove50% | Terminal does not fire |
| QA58 | Chaos1001 and exactly50% majority | Terminal does not fire |
| QA59 | Owner/controller/subject/travel overlap | Every resident state counted once under actual controller; live Airship custody remains in the world denominator once without a state-control numerator until actual settlement, including a strict-majority near miss |
| QA60 | Zero denominator or nonhuman population edge | Correct authoritative living-population definition and no division error |
| QA61 | No meaningful traditionalist territory | No enemy created to force the world-end scene |
| QA62 | Disabled terminal branch | Ordinary episode continues but automatic world end remains disabled |
| QA63 | Another terminal scenario owns progression | No incompatible second terminal commit |
| QA64 | Two simultaneous qualifying terminal checks | One activation, one history entry, one cinematic owner |
| QA65 | World-end activation | Ordinary automatic picker stops, event's own campaign and humanitarian systems continue |
| QA66 | Cosmetic rival renaming | Active restoration command cannot evade the substantive defeat condition |
| QA67 | Final power-center and industry conditions | Actual control or ratified security authority, not mere opinion, and correct75% industry threshold |
| QA68 | Final180-day maintenance | Victory only after terms maintained, partial and suspension outcomes distinct |
| QA69 | Temporary majority loss | Defined90-day recovery crisis, no immediate silent deletion |
| QA70 | Traditionalist or negotiated terminal result | Rights, war end, institutions, and surviving legal opposition resolved according to actual path |

## Manual scenario, assets, and integration

| ID | Scenario | Pass condition |
|---|---|---|
| QA71 | Four intensity previews | Clear countries, role, Chaos addition, forces, share, and crisis/war setup |
| QA72 | Preview cancellation | No government, resource, or population mutation |
| QA73 | Scarce valid countries | Reduced configuration disclosed, no invalid fake full bloc |
| QA74 | Material shortage during manual allocation | Real reallocations or understrength cohorts, no hidden manpower or equipment gift |
| QA75 | Maximum launch from zeroChaos | Exactly1000 before other actual developments, no false strict-threshold activation |
| QA76 | Scenario launch in high-Chaos campaign | Additive value and real population share shown, independent terminal conditions retained |
| QA77 | Multiplayer setup | Each affected human's role and commitments honored, no involuntary hidden faction swap |
| QA78 | Four custom unit models | Separate body/gun Meshy 7 provenance, current 3D owner-skill rig/action and Blender evidence, correct scale and export/reimport |
| QA79 | Six actions per model | Actual skeletal idle/move/attack/defend/support-attack/death, correct grip and sounds |
| QA80 | Unit counters | Correct152×42 two-frame sheet, native template/small assets, actual map consumer proof |
| QA81 | Voices and sound | Licensed sources, real tag/original-tag routing, no unsupported per-subunit voice promise |
| QA82 | Historical and fictional portraits | Correct identity, age and survival, separate native role sizes, no unauthorized RunPod execution |
| QA83 | All cosmetic identities | Every reachable country/identity/ideology/size consumer covered, no generic placeholder passed as final |
| QA84 | Report/news/super-event scenes | Native sizes, correct official frame and alpha, contextually true scene |
| QA85 | Super-event research and audio | Verified text and attribution, unique cleared tracks≤120 seconds, actual settings-aware playback |
| QA86 | Cinematic sequencing | No stale back-to-back founding scenes after terminal activation, effects not delayed for art |
| QA87 | Focus tree renders | All paths, exclusions, lines, icons, and new-country foundations readable and reachable |
| QA88 | Probability audit | Inspect/evaluate/sweep/compare evidence, correct adapter distinctions, no toy simulation claim |
| QA89 | Technology audit | Inspect/render/compare covers unit unlocks, equipment, research, inherited country setup |
| QA90 | Sixteen achievements | True and near-miss states, manual/debug restrictions, tag lineage, all 48 icon states |
| QA91 | Callback performance | No unauthorized global periodic loop and no duplicate callback registration |
| QA92 | Catalog and shared displays | Workbook-led identity, two clusters, reserved SCN-031 / raw 31 scenario, evolutions, world-end toggle, history, details coherent |
| QA93 | CXT and startup coverage | All four new subunits registered through the actual idempotent test-country pattern, no copied vanilla history for additive grants |
| QA94 | Full save/reload cycle | Missions, cases, governments, formations, treaties, counters, and terminal ownership persist |
| QA95 | Near-completion improvement loop | Actual configured planner and scoped follow-up review performed, accepted changes integrated throughout |
| QA96 | Final completion audit | Independent completion evidence, no assets or runtime claims unsupported by produced files and tests |

## Runtime audit order

Inspect source ownership and supported consumers first. Validate the mathematical and scope contracts next. Run the decision, country, focus, AI/probability, and technology audits against implemented files before live acceptance. Produce assets and integrate them with their native consumers, then run the high-value peaceful, polarized, civil-war, manual, and terminal scenarios. Invoke the debug-playtest workflow only under its actual user-invocation and runtime rules.

The near-completion improvement-loop planner must receive the complete current package and a self-contained question about unresolved creative and gameplay weaknesses. Its approved improvements must be incorporated into the main parts, matrices, asset register, and prompts. A missing planner invocation remains an explicit limitation. A parent writing its own checklist does not satisfy independent review.
