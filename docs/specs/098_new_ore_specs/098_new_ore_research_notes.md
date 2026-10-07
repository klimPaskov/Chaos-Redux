# Event 098 New Ore: Sources, authority, and research limits

Research date: 7 October 2026. This document records what was read, what it supports, which conflicts were resolved as design, and what remains a native implementation question. It is separate from the event's player-facing specification.

## Full supplied-source reading

The supplied project material was fully read and processed before substantive design or repository research began. The team read all 88 distinct text contents, totaling 2,549,725 bytes. Those contents account for 131 physical text instances across the supplied standalone files and extracted archives. All five ZIP containers, including nested subagent archives, were enumerated and their text contents covered.

The parent handled 44 distinct contents, the scripted-system architect 35, the event-completion auditor four, and the improvement-loop planner five credited contents. The planner also read a newer planning copy later fully reread by the parent. Credited counts assign each distinct byte content once and do not double-count that overlapping effort.

Every duplicate was verified by complete byte-stream equality. Hashes and inventories support traceability but were not substitutes for reading a unique version. Early tool outputs that truncated during the source gate were recovered by bounded complete rereads. Gate PASS was recorded only after those gaps were closed. No required supplied source was intentionally shortened, omitted, or replaced by a summary to accelerate drafting.

The companion `098_new_ore_source_reading_ledger.json` lists every distinct source identity, version location, byte count, hash, reader, full-read status, and verified duplicate instance. Its role is to make this claim reviewable, not to substitute metadata for the completed reads.

The full supplied gate covers AGENTS, README, mechanics, the complete planning skill and its supplied older versions, every other supplied project skill, all three catalogs, dynamic-effect/trigger indexes, configuration text, every nested role definition, and the supplemental reading protocol. Relevant requirements were applied to the event. Skill availability did not itself create additional gameplay scope.

## Authority and accepted design

The user's current Event 098 brief is authoritative. The latest supplied project rules govern the planning workflow. Older supplied copies were fully read for continuity and conflict detection, but a superseded instruction was not silently preferred because it was easier.

The current brief explicitly supplies the initial armor floor, territorial control rule, evolution names and thresholds, selected weaker foreign access, four connections, and extreme power identity. The parent accepts the package's concrete values and bounded expansion choices within the user's request to expand the idea thoroughly. These include direct +50/+75/+200% with diminishing additional sources, foreign +20/+30/+80%, finite commercial/security/faction terms, scarcity cadence, ordinary demands and defense commitments, separate asteroid composition, difficult achievements, and one operational Super-Alloy presentation.

That is design acceptance for this planning package. It is not a claim that the user separately approved every numeric anchor or that any implementation already passed testing. Later changes to the core promise require an explicit disposition. Calibration can be revised through the named evidence while preserving that promise.

## Repository research

The architect's repository evidence is pinned to commit `a3ef485c5da7e2337122eca04ac65c175050f251` in [Chaos Redux](https://github.com/klimPaskov/Chaos-Redux/tree/a3ef485c5da7e2337122eca04ac65c175050f251). Additional current `master` fetches were made on the research date with returned blob identities recorded where available. The table distinguishes complete source reads from targeted additional research. These are later supporting reads and are not added to the 88-content supplied gate.

| Inspected source | Coverage | Finding used in this plan |
| --- | --- | --- |
| [events/098_new_ore.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/events/098_new_ore.txt) | Complete | Existing event identity, random-state structure, state marker/singleton, initial owner grant |
| [common/ideas/098_new_ore_ideas.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/ideas/098_new_ore_ideas.txt) | Complete | Legacy actual equipment-armor bonus, instant candidate, extra attack/defense/speed, cancellation and transfer structure |
| [098 dynamic modifier](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/dynamic_modifiers/098_new_ore_dynamic_modifiers.txt) | Complete | State marker uses a generic mine idea sprite, which does not establish its native canvas |
| [029 on-actions](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/on_actions/029_riches_found_on_actions.txt) | Complete | Current-control callback and bounded registered-mine handling for country transformations |
| [028 mineral ideas](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/ideas/028_asteroid_incoming_ideas.txt) | Complete | Existing country `armor_factor` candidate and legacy main/fragment structure |
| [028 runtime effects](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_effects/028_asteroid_incoming_runtime_effects.txt) | Targeted mineral/achievement/control sections at 1712–1815 and 1910–1933 | Older embedded six-fragment logic and broad removal, not the indexed newer owner API |
| [086 event entry](https://github.com/klimPaskov/Chaos-Redux/blob/master/events/086_world_claims.txt) | Complete | Actual inspected entry selects Germany, while supplied catalog describes Germany or the Soviet Union |
| [092 event entry](https://github.com/klimPaskov/Chaos-Redux/blob/master/events/092_greenland_sale.txt) | Complete | Sale offer and buyer-facing flow exists. This alone does not establish the complete auction settlement or price provider |
| [Elephant equipment](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/units/equipment/012_africa_elephant_equipment.txt) | Complete | Positive armor in an equipment archetype classified as infantry |
| [Elephant forces](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/units/012_africa_elephant_forces.txt) | Complete | Separate intrinsic subunit armor, requiring coverage beyond equipment categories |
| [Coal golems](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/units/coal_golems.txt) | Complete | Another intrinsic positive-armor contribution |
| [018 AI strategy](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/ai_strategy/018_resources_found_ai_strategy.txt) | Complete | Real event-owned state target and front strategy consumers, with validity and cleanup precedent |
| [Universal cost system](https://github.com/klimPaskov/Chaos-Redux/blob/master/docs/systems/universal_cost_modifier.md) | Complete | Intended normalized quote, scale, inclusive affordability, actual payment and refund ownership |
| [Universal cost helper documentation](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_effects/chaosx_universal_cost_effects.md) | Complete | Documented ceiling and exact-comparison promises |
| [Universal cost helper code](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_effects/chaosx_universal_cost_effects.txt) | Complete | Implementation differs from documented ceiling/comparison method, requiring exact boundary proof before use |
| [019 MTTH source](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/mtth/019_infantry_spawn_mtth.txt) | Complete | Inspected current interval definition and bounded due-date lifecycle precedent in associated research context |
| [Shared dynamic effects code and docs](https://github.com/klimPaskov/Chaos-Redux/tree/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects) | Complete retrieved dynamic-effects files, targeted use of public API sections | Current public helper contracts and owner/private separation |
| Repository `paradox_wiki` copies of Idea, Equipment, Modifiers, List of modifiers, Scopes, On actions, and AI modding | Targeted relevant sections of additional reference documents | Candidate armor, callback, scope and AI semantics. Not claimed as full native documentation or runtime proof |
| Repository `paradox_wiki` Decision modding | Complete retrieved text | Decision/target refresh, custom-cost, mission and native target behavior as an offline reference, pending current installed verification |

Repository searches and directory inventories establish paths and discovery context. They do not imply all files in a returned directory were read. Downloading a large offline reference did not itself count as reading it. The source gate's complete supplied reading and the later targeted research are deliberately separate claims.

## Material source conflicts and dispositions

| Conflict | Disposition in this package |
| --- | --- |
| 098 catalog has blank evolutions/cluster and older production-oriented wording | Current brief supplies four evolutions, Positive Economy High, and broad immediate actual armor. The planning task does not edit export-only catalogs or declare Playable |
| Old 098 gives initial owner benefit and uses cancellation/country scan transfer | Accepted behavior is immediate actual-controller entitlement, unique state registry, and bounded lifecycle |
| Legacy `armor` equipment family misses inspected custom positive armor | Broad consumer inventory and effective paired-stat proof are mandatory. Intrinsic subunit armor and actual naval armor are explicit |
| Indexed newer 028 mineral API paths are absent in current fetched repository | Preserve its intended separate, current-controller contract. Resolve the owner-side source discrepancy during implementation. Do not silently use the old six-slot cap |
| Universal cost documentation and code disagree about rounding/comparison | Inspect and prove the owning helper before use, with exact below/equal/above tests and actual receipt conservation |
| World Claims catalog and entry name different possible actors | Read the actual activated claimant through Event 086's verified runtime contract. Event 098 does not manufacture the missing alternate entry |
| Asset reference terminology differs across supplied generations | Latest specialized asset skill's `gfx_references` is canonical. Exact installed shelf still must be inspected |
| Old Chaos tier descriptions differ from latest mechanics | Use current 0–199, 200–399, 400–599, 600–799, 800–999, and 1000+ ranges, with requested numeric evolution thresholds |

## Historical and material inspiration

The mineral is fictional. Every ore strength value, diplomatic cost, source limit, timer, and achievement threshold is authored game design. Historical research helps the material and bargaining feel grounded, without claiming that a real ore produced the fictional gameplay effect.

The USGS fact sheet [Molybdenum: A Key Component of Metal Alloys](https://www.usgs.gov/publications/molybdenum-a-key-component-metal-alloys), S. J. Kropschot, 2010, Fact Sheet 2009–3106, DOI [10.3133/fs20093106](https://doi.org/10.3133/fs20093106), describes how alloying uses can improve steel properties and includes armor plate among applications. The design inference is a plausible material-testing and protective-alloy visual language. It does not identify New Ore as molybdenum or substantiate the event's numerical strength.

The U.S. Department of State's [17 January 1944 instruction from Hull to Norweb](https://history.state.gov/historicaldocuments/frus1944v04/d90), in Foreign Relations of the United States 1944, volume IV, document 90, discusses Portuguese wolfram supply, quotas or embargo, economic concessions, and alliance/neutrality pressures. The design inference is that valuable military materials can support barter, security commitments, competing terms, and political pressure through ordinary diplomacy. The document does not imply that such negotiations must automatically lead to war.

Both primary sources were opened by the parent. They provide limited inspiration rather than final localisation. The Super-Alloy's exact quotation and music remain a later research task with their own attribution and rights evidence.

## What could not be fully read or verified

Every supplied project-source text was fully covered. However, not every file referenced by those sources was supplied or accessible, and this package does not claim otherwise.

The installed game documentation, full installed vanilla/mod/DLC consumer inventory, native state and category textures/GUI definitions, canonical asset contact sheets and template pixels, authoritative XLSX workbook, live game behavior, and actual campaign save files were not available for a complete native inspection in this session. Additional offline wiki research used targeted sections as stated above. The full Asteroid runtime file outside its named relevant sections was not read.

Exact fetches of the indexed `028_asteroid_incoming_mineral_effects.md` and `.txt`, `chaosx_universal_cost_exact_triggers.md`, `docs/events/098_new_ore.md`, and the queried canonical art-reference paths returned unavailable/404 results. A 404 from this repository route does not prove that a corresponding installed local file is absent.

No HOI4 MCP, engine run, gameplay implementation, real equipment transfer test, native asset rendering, actual save comparison, or statistical AI probability audit was performed. The mathematical examples, file/package validation, and design consistency review are planning evidence. Their scope is stated exactly in the implementation map and final review record.

No user requirement was intentionally simplified or truncated to produce a quicker specification. The bounded agreement system, one ordinary category, source scarcity, and diminishing additional deposits are explicit design decisions supporting the user's event identity and request for ordinary diplomacy. Remaining engine and asset questions are preserved as concrete proof gates, not treated as solved by the written plan.
