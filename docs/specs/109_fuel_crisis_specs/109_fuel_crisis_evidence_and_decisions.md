# Fuel Crisis planning evidence and design decisions

## What this package establishes

This is a full planning package for Event 109 Fuel Crisis. It contains design specifications and future implementation instructions. It does not contain a gameplay patch, finished localisation, produced artwork, a workbook edit, or a claim of runtime validation.

The user supplied the mechanic and catalog identity. The planning work develops its operational consequences, presentation, Chaos contribution, Tasks contracts, achievement, implementation boundaries, and validation scenarios. Additional numerical tuning and the achievement are parent-authored design choices under the request to expand the specification. They are not attributed to an explicit user approval or to existing implemented behavior.

## Complete supplied-source processing

The source gate finished before substantive event design or repository implementation research began.

| Coverage item | Result |
| --- | --- |
| Supplied and extracted text occurrences | 132 |
| Distinct text versions | 90 |
| Distinct text content size | 2,594,283 bytes |
| Distinct Markdown versions | 42 |
| Distinct TOML versions | 42 |
| Distinct CSV versions | 6 |
| Supplied archive containers | Three |
| Nested archive containers | Two |
| Unread supplied source texts after the gate | Zero |
| Truncated outputs counted as completed reading | Zero |

The three supplied archives were the standalone subagents archive, the earlier all-project-sources archive, and all-project-sources(20261010-122247).zip. Both all-project-sources archives contained a nested subagents archive. All five containers were fully inventoried and passed ZIP CRC checks. Every extracted text member was matched to the source manifest.

This was collective reading by the parent and the three supplied project roles. It is not a claim that one agent personally reread every version. The parent read the complete planning, AGENTS, subagent routing, and protocol material and integrated the complete specialist source notes. The specialist assignments covered every remaining source, including all catalog rows, visual and technical skills, configuration, and all twenty current and twenty older subagent definitions.

| Reading owner | Distinct assigned source versions fully covered |
| --- | ---: |
| Parent | 7 |
| Scripted-system architect, original assignment | 16 |
| Decision and mission auditor | 16 |
| Documentation curator | 31 |
| Scripted-system architect, transferred older profiles | 20 |
| Total | 90 |

The assignments overlap in prerequisite reading, which is additional reading rather than additional distinct-source coverage. The curator's original ledger honestly retains twenty older profiles as delegated. The architect's supplemental ledger completes those profiles and the combined gate resolves that delegation.

### How complete reading was recorded

Current and otherwise distinct text was read in bounded complete chunks. Byte-identical copies were verified by SHA-256 and direct byte comparison instead of repeatedly presenting identical text.

Older revisions were covered through lossless version reconstruction. A reader first read the entire current counterpart. Every unchanged older span was matched exactly to that already read text. Every differing older passage was printed verbatim and read. Original byte-order marks and line terminators were retained. Reconstructing the older file reproduced its original bytes and hash exactly.

This method avoids repeating identical passages. It does not replace changed passages with summaries. It also does not claim that files differing only in line endings were byte-identical.

Some initial output requests exceeded tool limits. They were not counted as coverage. The affected source ranges were reread in smaller complete outputs before the gate passed. The parent independently rechecked all manifest hashes and duplicate equivalence. After the source attachments were surfaced again with the user's continuation, all 134 manifest entries, including the two nested containers, still matched their recorded hashes.

The accompanying source inventory gives one row per distinct text version, every occurrence, its byte size, hash, reading owner, and method. The reading receipts preserve the original per-reader records and the combined gate.

## Additional Tasks source

After the supplied-source gate, a targeted continuity search located the prior user brief titled 101 - Tasks(1).md. It was read completely, from line 1 through line 241, with no further text remaining.

That brief establishes:

- Tasks is player-only.
- Multiplayer selection chooses one valid player-controlled country.
- Objectives and deadlines derive from the current campaign.
- Fuel Crisis may provide a reserve-recovery or existing supply-route objective.
- Rewards, consequences, and the repeatable task lifecycle belong to Event 101.
- Tasks does not use a permanent task currency.

The source was created and modified on 9 October 2026. Its file identity is recorded in the reading receipts. It is a prior design brief, not proof of runtime implementation.

## Targeted repository evidence

Repository observations are pinned to [commit a3ef485c5da7e2337122eca04ac65c175050f251](https://github.com/klimPaskov/Chaos-Redux/commit/a3ef485c5da7e2337122eca04ac65c175050f251), dated 6 October 2026 at 15:21:52 UTC.

This repository pass was targeted. Complete files were fetched where needed, but only relevant repository sections were read. It was not a second full-repository source gate. No historical-commit audit or complete recursive source inspection was performed.

| Observed source | Finding and design consequence |
| --- | --- |
| [Event 53 source](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/events/053_mysterious_man.txt) | Line 54 uses the direct zero form of the fuel setter. This is repository precedent, not a live engine test. |
| [Offline Effects reference](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Effects%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Lines 1718 to 1720 document fuel addition, direct fuel setting, and ratio setting. The direct setter is the selected implementation candidate. |
| [Offline Scopes reference](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Scopes%20-%20Hearts%20of%20Iron%204%20Wiki.md) | The current-country iterator and ROOT distinction support one synchronous pass over existing countries. |
| [Dynamic effect implementation](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_dynamic_effects.txt) | Lines 752 to 755 negate the removal input and call additive fuel adjustment. That helper does not provide a measured exact-zero contract. |
| [Settings dispatch implementation](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_settings_effects.txt) | The dispatcher sends the country event before shared type accounting. Explicit force paths bypass ordinary fired restrictions. |
| [Event logic implementation](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_logic_effects.txt) | Fired membership excludes ordinary repeat selection. The Fire-Once handler still performs history and pacing after its guarded array append. Its weight comment disagrees with its value assignment. |
| [Offline Data structures reference](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Data%20structures%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Current and maximum fuel variables are documented in thousands. Their units must not be confused with raw oil or unscaled fuel. |
| [Offline Triggers reference](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Triggers%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Positive fuel, major status, and war status have documented predicates useful for the one-time Chaos counters. |
| [Offline Event modding reference](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Event%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Immediate and no-delay event behavior support a synchronous receipt handoff candidate. Installed execution order still needs verification. |
| [Shared cluster implementation](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_event_cluster_effects.txt) | Random Stuff samples the authoritative event pool. This historical observation described the inspected source at that revision. The accepted design now assigns Fuel Crisis to Various Anomalies cluster 11, Severe, with existing eligibility unchanged. |
| [Achievement registry](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/achievements/chaos_redux_achievements.txt) | One registry unique ID, event-grouped string keys, country completion predicates, and root achievement icon lookup are established patterns. |

The checked directories contained 162 event files, 91 specification entries, 122 decision entries, 415 scripted-effect entries, and 252 scripted-trigger entries. Their names did not identify a 101 Tasks, 109 Fuel Crisis, or 114 Fuel Crisis implementation. Exact searches for the inspected event identifiers also returned no matching implementation.

This is a bounded absence finding. It does not prove that every branch, history entry, oddly named file, or external working tree lacks related work. The recursive tree request failed with a transport error. The implementation agent must repeat narrow identity and owner checks in its actual checkout.

## Source conflicts and their disposition

| Conflict | Treatment in this package |
| --- | --- |
| Catalog 109 is Custom laws and 114 is Fuel Crisis | This is a pre-migration snapshot recording the identity collision. The user accepted design ID 109 and authorized migration; former Fuel Crisis identity 114 is historical only, and the authorized workbook and registry migration is complete. See the shared identifier registry and 24 October migration record. |
| Historical catalog availability labels | These labels describe the inspected snapshot only and do not establish current catalog status or runtime availability. |
| Historical Tasks availability labels conflict across snapshots | Preserve each label as a historical observation; neither establishes the current catalog or runtime status. The Tasks API remains an implementation dependency. |
| Older asset paths use vanilla_reference | Future production uses the current owner path, gfx_references. |
| Older portrait, 3D, and audio routes differ from current owner instructions | The full differences were read and recorded. They do not add feature surfaces to this event. Current dedicated owner instructions govern future relevant work. |
| Current completion profile mentions mandatory GUI rewrite while current owner guidance makes it optional | Require applicable inspect, render, matched comparison, and image review evidence. Do not require an optional write route. |
| Source statements disagree about variable-duration timed flags | Do not assume unsupported flag syntax. Use the verified Tasks deadline and native timer route. |
| Shared Fire-Once comment says zero weight but code assigns one | Use the observed fired-state exclusion and explicit owner admission contract. Do not treat the comment as replay protection. |

The newer source set is the planning baseline where it adds or changes requirements. An older source is retained as evidence of history, not silently substituted for the current technical owner.

## Design decisions and acceptance basis

| Item | Disposition | Basis |
| --- | --- | --- |
| Exact worldwide stockpile zero, intact upstream economy, natural recovery, no evolutions | Preserved user requirement | Current Fuel Crisis brief |
| Player-only Tasks assignment | Preserved prior user requirement | Fully read Tasks brief |
| Direct setter candidate | Promoted into this specification | Repository precedent and offline documentation, with installed verification pending |
| Small occurrence receipt and duplicate guard | Promoted into this specification | Observed shared dispatch and accounting order |
| Deliberate force replay distinct from duplicate delivery | Promoted into this specification | Existing shared force feature and owner admission analysis |
| First committed force or raw-debug occurrence consumes natural eligibility | Parent design choice clarified in improvement review | Keep the owner consumed state aligned with the shared fired record |
| Forced and raw direct-debug origins cannot earn this achievement | Parent design choice clarified in improvement review | Use frozen occurrence provenance to preserve an ordinary earned challenge, with existing registry validity as an additional gate |
| One-time Chaos bands from +10 through +25 | Parent design choice for testing | Global reserve shock calibrated as one source, with transient exposure counts |
| Two alternative Tasks templates | Promoted into this specification | User's reserve-or-oil connection and active-objective guidance |
| Dynamic 90 to 180 day Tasks durations | Parent design choice for testing | Mission guidance, forecast feasibility, and bounded crisis relevance |
| Earlier universal 180-day task proposal | Superseded | Replaced by the dynamic formulas in Part 3 |
| Later 365-day maximum proposal | Superseded | Part 3 caps this crisis-specific connection at 180 and rejects longer forecasts |
| Mandatory conservation-only reserve route | Superseded | Part 3 allows a verified conservation or recurring supply-improvement route |
| Reserve deadline margin on refill time alone | Superseded in final review | Apply 30% to action lead plus refill time. A forecast that then exceeds 180 days is rejected |
| Conservation assessed only against onset demand | Clarified in final review | Freeze assignment commitment demand as well and require a meaningful 20% reduction from both references, independent of starvation-limited consumption |
| One difficult achievement tied to an active Tasks outcome | Parent design choice, specified with a runtime dependency | Achievement guidance and curator proposal, without adding a separate recovery system |
| Proposal to omit a Fuel Crisis achievement | Not adopted | A measurable demanding Tasks recovery route can support one without changing the core economy |
| Static news and shared-log scene consumers | Promoted as planned requirements | Native announcement plus established shared presentation, with exact hooks to verify |

Later review findings and their final dispositions are recorded in the package review record. Temporary specialist drafts are not competing specifications.

## What remains unverified

No HOI4 MCP tools were exposed in this session. The supplied configuration is evidence of intended tooling, not proof that the configured services are running here. Installed native game documentation, the user's active DLC and mod set, engine scheduling, fuel precision, local unit buffers, real task accessors, native mission timing, and gameplay behavior were not verified.

The referenced asset contact sheets, immutable achievement templates, final sprite bindings, and current live consumer dimensions must be inspected during production. Artwork and localisation have been planned, not produced.

The live XLSX workbook was not edited or inspected as the authoritative current registry. The supplied CSV snapshots were fully read. Identity reconciliation in the actual workbook and checkout remains an implementation prerequisite.

Public web searches were attempted for official fuel developer material. The official forum content could not be fetched reliably and the Steam announcement exposed insufficient text. Those attempts are not used as proof of engine behavior or historical claims. The package relies on the user briefs, supplied project sources, targeted repository evidence, and explicitly labeled design reasoning.

No Hearts of Iron IV process was launched. No source-only review is represented as a native or in-game test. The implementation and MCP usage maps define the remaining work precisely.
