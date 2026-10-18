# Demilitarization: research and source notes

This appendix records the evidence used to shape the design. The gameplay files remain the source of the proposed event behaviour. A source snapshot, a historical analogy, and an observed implementation are different kinds of evidence.

## Design authority and accepted expansion

The user's current brief is the attached file 114 - Demilitarization(2).md. It establishes Event 114, original catalog ID 124, Minor Repeatable, To Be Reworked, Chaos level 1, Peace membership, High member severity, the border-state baseline, war suspension, peace restoration, and the three named evolutions.

The current brief takes precedence over the supplied catalog's older all-but-capital baseline. It also establishes the independent Event 096 condition boundary.

The parent accepted the following additions within the user's explicit request to expand the idea thoroughly:

- Current-controller territorial applicability and separate legal ownership provenance.
- One immutable border snapshot for the Deeper ring.
- A capital refuge under Total only when the capital is outside the earlier required belts.
- A cumulative evolution sequence with authored thresholds 200, 400, and 800.
- One cohesion value, 14 peacetime-day reviews, bounded real-unit losses, and delayed living-personnel returns.
- Four military response families, two mission/objective roles, and five demanding achievements.
- Source-aware shared DMZ ownership and member-scoped Peace context preparation as necessary integration boundaries.

These are planning decisions. They do not claim a user approved particular numeric tuning in a previous session or that the repository already implements them.

## Supplied-source reading coverage

The hard source-reading gate passed before substantive specification drafting and repository research.

| Coverage item | Completed count |
| --- | ---: |
| Supplied top-level files | 27 |
| Archive containers, including nested containers | 5 |
| Archive members | 111 |
| Text copies, including duplicate copies | 133 |
| Distinct complete text buffers | 91 |
| Distinct source text bytes | 2,596,371 |
| Distinct source lines | 29,837 |
| Outstanding required-source reading gaps | 0 |

The four actual readers were /root, /root/source_inventory, /root/assets_sources, and /root/systems_sources. The reading covered the standalone Project Sources, the older supplied archive and subagent archive, the dated all-project-sources(20261010-191414).zip archive, nested subagent definitions, catalogs, mechanics, workflow guides, and the current brief.

Each distinct full text was exposed and processed in full by an assigned reader. Exact duplicate aliases were grouped only after complete byte-buffer equality. Hashes and inventories did not count as reading. Every extracted archive member was reconciled with its original archive bytes.

The root did not personally reread all duplicate copies or independently read every source group. This was distributed full reading, followed by integration and specialist review. Oversized intermediate outputs that clipped required reading were replaced by complete bounded reads before the gate passed.

The machine-readable receipt is 114_demilitarization_source_coverage.json. It records sources, group ownership, byte coverage, archive membership, and the completion basis. It verifies reading, not repository integrity, engine support, or game execution.

## Source versions and catalog migration

The dated supplied AGENTS.md and owner guides are used for the current workflow where they differ from older copies. Their dates alone do not establish that every embedded catalog row is current. Conflicting versions were read and compared rather than silently discarded.

The supplied CSV snapshots still place Demilitarization at legacy ID 124 with an all-but-capital premise and Unavailable status. Their ID 114 row refers to Fuel crisis. The current brief explicitly remaps this design to 114.

The canonical repository workbook is docs/spreadsheets/chaos_redux_events_catalog.xlsx. It was not opened or edited in this planning session. The catalog evidence here is explicitly the supplied CSV export snapshots, corroborated where possible by targeted repository source inspection.

Implementation must reconcile the workbook and live registries through the spreadsheet owner workflow. Do not overwrite the unrelated legacy ID 114 row mechanically, create both 114 and 124 as active copies of this event, or mark the event Playable on the strength of a spec package.

The supplied Peace CSV lists 9, 9, 9, 9, 61. The inspected repository instead has two White Peace logical member rows. Event 61 in the supplied catalog is Half mils into civs. It must not be relabelled as a different peace movement.

Event 114 is the event identity. Peace ID 4 is an existing cluster identity. Any new member-row identity or achievement identity requires its own collision check. Negative searches for chaosx.nr114.1 and chaosx.nr124.1 did not prove that their namespaces are free.

## Repository inspection

Repository: klimPaskov/Chaos-Redux. Inspected revision: a3ef485c5da7e2337122eca04ac65c175050f251. The connector reported master as the default branch.

Inspection was targeted to relevant source bodies and offline reference sections. Full files were sometimes fetched for navigation, but this appendix does not claim every line of the repository was read.

| Evidence | Finding and design consequence |
| --- | --- |
| [Event 001 effects](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/001_communism_spread_effects.txt), especially 327–378 | The added-DMZ marker protects an earlier boolean state but cannot represent a later overlapping source. Event 114 needs source-owned reconciliation. |
| [Event 018 decisions](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/decisions/018_resources_found_decisions.txt), 539–574 | A negotiated field sets a DMZ directly, and another path clears it. Those writes need owner adapters. |
| [Event 018 decision effects](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/018_resources_found_decision_effects.txt), 803–820 and 1291–1301 | Commission activation, restoration, and closure do not provide a complete shared ownership mechanism. |
| [Event 018 main effects](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/018_resources_found_effects.txt), 800–841, and [its event file](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/events/018_random_resource.txt), 1724–1767 | The negotiated field marker appears in option 18.44.a after the decision has already set the DMZ. Other options use different markers. Preserve the actual ordering when integrating. |
| [Event 096](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/events/096_divisions_lock.txt), 22–78 | The inspected implementation locks templates and schedules a 90-day release. It does not establish the fuller allowance design in the current brief. Event 114 preserves the brief's independent-condition boundary. |
| [Peace cluster effects](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_event_cluster_effects.txt), 1491–1515 and 4132–4147 | Current Peace rows are White Peace rows, and runtime setup unconditionally requires a White Peace context. A valid 114 peacetime trigger requires member-scoped context setup. |
| [Cluster constants](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/script_constants/event_cluster_constants.txt), 152–163 | High severity has effective floor tier 2. Preserve the distinction from Event 114's own catalog Chaos level. |
| [Chaos meter effects](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaos_meter_effects.txt), 4514–4618 | add_chaos_meter_value applies the shared meter policy and records history. Use the real custom-reason context and do not bypass the shared disabled or upper-state behaviour. |
| [Event 019 on-actions](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/on_actions/019_infantry_spawn_derivative_on_actions.txt), 1–132 | Country-local lifecycle reconciliation is an existing source pattern. |
| [Event 016 raid effects](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/raids/016_brilliant_scientist_portal_raids.txt), 236–270 and 484–519 | An exact selected-division destruction call exists after a reconstruction receipt. This does not prove peaceful refunds or partial desertion. |
| [White Peace handoff](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/specs/009_white_peace_specs/specs/009_white_peace_event_text_log_cluster.md) | Useful context for global evolution history and Peace membership. Its finished localisation examples are not copied into this direction-only package. |

A source-documentation discrepancy was also found in the civilian population helper. The supplied current helper guide describes measured population-first accounting, while the fetched [dynamic-effects source](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_dynamic_effects.txt) has an older-looking requested/clamped result path. This was not diagnosed as live behaviour or repaired. Military desertion does not use that civilian helper under either contract.

## Offline engine reference evidence

The repository's offline wiki snapshot was used. The live Paradox wiki was not used.

| Reference | What it supports and what remains uncertain |
| --- | --- |
| [Effects](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Effects%20-%20Hearts%20of%20Iron%204%20Wiki.md) | State DMZ setting, division destruction, group deletion with disband refunds, and state-based army teleportation are documented. Partial manpower-only mutation and exact selected peaceful refunds remain unproven. |
| [Scopes](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Scopes%20-%20Hearts%20of%20Iron%204%20Wiki.md) | State and actual division iteration exist. Neighbour iteration alone does not prove true-land-only adjacency. |
| [On actions](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/On%20actions%20-%20Hearts%20of%20Iron%204%20Wiki.md) | First-war, last-war peace, and state-controller callbacks support the lifecycle. Owner-only and automatic capital coverage still need installed proof. |
| [Data structures](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Data%20structures%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Scope lifetime and manpower/equipment readers need careful interpretation. A total-manpower reader must not be assumed to mean spendable reserve. |
| [Triggers](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Triggers%20-%20Hearts%20of%20Iron%204%20Wiki.md) | War, capital, DMZ, and unit-strength tests are documented. A strength test is not a precise manpower mutation. |

Installed-game reference, actual native behaviour, and source version can differ. The implementation proof gates preserve those distinctions.

## Historical research and design inference

These sources provide context for the existing design. Event 114's worldwide mechanism, automatic war suspension, numerical cohesion, and evolutions remain fictional rules.

### Territorial limits in a treaty

The Versailles Treaty Articles 42 and 43 define a geographic military restriction around the Rhine, including armed-force presence and manoeuvres. Article 42 also addresses fortifications. This provides a historical example of a bounded military exclusion area. It does not authorise copying the fortification rule into Event 114 or treating its global condition as the treaty.

Source: [Yale Avalon Project, Treaty of Versailles, Part III](https://avalon.law.yale.edu/imt/partiii.asp), Articles 42–43. No quotation is used.

Design inference: use tangible frontier geography and military absence in the early reports. Keep Event 114's existing infrastructure intact.

### Unequal release expectations and overcrowded service

The National Army Museum describes disputed British demobilisation priorities after the First World War and problems caused by transport delays and crowded camps. It also describes the overall demobilisation as successful.

Source: [National Army Museum, Peace and commemoration](https://www.nam.ac.uk/explore/peace-and-commemoration), Demobilisation, Mutiny, Crisis averted, and Empire troops sections.

Design inference: service conditions, release expectations, and maintaining experienced cadres provide distinct response motives. The history does not make desertion or radicalisation inevitable.

### Administrative release priorities

The Commons record of 4 October 1944 describes planned release by age and service and discusses the difficulty of an equitable overseas-service priority. It also addresses continued service obligations for Auxiliary Air Force personnel.

Source: [UK Parliament, Hansard, Demobilisation](https://hansard.parliament.uk/commons/1944-10-04/debates/6dee3264-851f-4d7e-b98a-263ceead4cb8/Demobilisation).

Design inference: response writing can distinguish clear service obligations from poor daily conditions. This source does not establish the effectiveness of the proposed game costs or modifiers.

### Åland's own territorial history

Finland's foreign ministry dates Åland's demilitarisation to 1856 and identifies the separate 1921 convention on demilitarisation and neutralisation.

Source: [Ministry for Foreign Affairs of Finland, Centenary celebrations of the autonomy of the Åland Islands set to begin](https://um.fi/current-affairs/-/asset_publisher/gc654PySnjTX/content/ahvenanmaan-itsehallinnon-satavuotismerkkivuosi-alkaa/35732), published 9 June 2021, historical sections.

Design inference: Finnish context can acknowledge an existing territorial precedent. It must not imply that the historical regime followed Event 114's automatic wartime suspension. Use only date-appropriate references in a campaign.

## Actual specialist work and evidence limits

The source readers supplied full-reading receipts, integration notes, and asset and historical consultations. The actual chaosx_scripted_system_architect completed a plan-only lifecycle, source-ownership, native-capability, and accounting handoff.

The actual chaosx_improvement_loop_planner was spawned near planning completion with fork_turns set to none. Its findings and the parent's dispositions are recorded in 114_demilitarization_review_dispositions.md.

No HOI4 MCP tool was exposed in tool discovery. No game was launched. No engine test, probability evaluation, render of the game UI, or asset production was claimed. The current work creates specifications and handoffs, with empirical implementation gates kept visible.

