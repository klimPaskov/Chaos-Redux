# 117 Autonomy: sources and evidence

The supplied-source reading gate is complete.
The team fully read and processed all **151 unique supplied text sources**, totaling **3,209,743 bytes**, before substantive design and repository investigation.
The parent processed the reader reports and integrated the relevant specialist reviews.
No supplied text file remains unread, and no source or specification content was shortened for speed.

This appendix records the evidence behind the eight numbered specification parts.
It distinguishes supplied requirements, current implementation evidence, neighboring proposals, historical context, and future verification dependencies.
It does not change the design or promote an unaccepted review recommendation into the specification.
The parent integration handoff records acceptance and review dispositions.

The complete machine-readable catalog is [117_autonomy_source_read_manifest.json](../../plans/117_autonomy_plans/imported_review/117_autonomy_source_read_manifest.json).
It contains one record for every supplied source, its original origin, duplicate aliases, exact SHA-256, byte and line counts, responsible reader, and full-read coverage.
It also records the repository sources, historical references, catalog analysis, citation mapping, and evidence limits.
Original origins and stable source IDs are preserved without temporary absolute workspace paths.

## How the source gate was satisfied

The gate passed at **2026-10-23 12:39:43 UTC**, as recorded in `source_review/source_gate.json`.
Reading was distributed across four allocations.
This is a team-based claim, and does not mean that the parent or this documentation curator personally read every source.

| Reader | Unique supplied texts | Source bytes | Complete reading chunks | Responsibility |
| --- | ---: | ---: | ---: | --- |
| Parent, recorded as `root` | 29 | 597,387 | 14 | Source protocol, current planning package, current root guidance and catalogs, and selected current role definitions |
| `source_assets` | 44 | 1,009,228 | 24 | Asset, presentation, focus, animation, model, and corresponding specialist guidance |
| `source_governance` | 40 | 775,019 | 18 | Governance, historical planning and catalogs, spreadsheet rules, and selected system and role guidance |
| `source_systems` | 38 | 828,109 | 19 | Event, decision, diplomacy, autonomy, AI, helper, modifier, lifecycle, and corresponding role guidance |
| **Total** | **151** | **3,209,743** | **75** | **All allocated source text fully read and processed** |

The three source readers also read the common source protocol.
That shared read is not counted three additional times in the 151 unique-source total.
Their complete reports and ledgers were processed by the parent.
The register preserves the hashes of those reports and ledgers so the evidence remains distinguishable from a later summary.

The inventory contains **174 physical records**.
Of these, 173 are text records representing 151 unique sources and 22 byte-identical duplicate text copies.
The remaining record is a duplicate nested `subagents.zip` container, not an additional unread text source.
All 174 physical-record hashes and the recorded byte-equivalence checks were verified.
The catalog's original origins and aliases account for all 173 physical text records.

Several initial output attempts hit an output or context limit.
The affected chunks were completely reread, or read as exact adjoining halves, before the gate passed.
No truncated attempt was counted as complete coverage.
All repaired reads and their responsible allocations are recorded in the manifest.
The original inventory's pre-read `pending` fields are superseded by the passed gate and completed reader ledgers.

## Supplied-source families

| Source tokens | Family | Unique texts | Bytes | Treatment |
| --- | --- | ---: | ---: | --- |
| `PS-S001` to `PS-S023` | Loose project documents, historical catalogs, and the source-reading protocol | 23 | 1,064,163 | Fully read, including older versions that required comparison |
| `PS-S024` to `PS-S043` | Earlier TOML specialist definitions | 20 | 151,247 | Fully read as earlier role representations |
| `PS-S044` to `PS-S119` | Current skills, complete linked references, and supplied templates | 76 | 1,572,718 | Fully read, including families whose implementation surfaces were not selected |
| `PS-S120` to `PS-S128` | Current root guidance, mechanics, registries, catalogs, and configuration | 9 | 293,376 | Fully read and reconciled with the older supplied versions |
| `PS-S129` to `PS-S151` | Current Markdown specialist definitions | 23 | 128,239 | All 23 fully read, with only relevant roles exercised |

An origin containing `!` identifies an archive member.
For example, `upload/all-project-sources(20261023-123006).zip!subagents.zip!chaosx-documentation-curator.md` identifies the exact nested role source, not an inferred installed agent.
Byte-identical aliases share the same completed reading coverage.
Nonidentical historical and current versions remain separate source records.

Current explicit user decisions govern the requested Event 117 Autonomy identity and original ID 128 relationship.
The current supplied guidance governs the planning workflow where it supersedes older versions.
Current repository evidence establishes what exists at the inspected revision, while an existing spec or handoff alone does not establish that its proposals were accepted or implemented.
The source register preserves these distinctions rather than combining incompatible versions into one implementation recipe.

### Principal supplied references used by the numbered parts

| Token or range | Current supplied subject | What the citation supports |
| --- | --- | --- |
| `PS-S050` to `PS-S052` | AI strategies and related AI references | Different score and probability semantics, complete candidate pools, contextual weighting, and honest analytical limits |
| `PS-S058` to `PS-S067` | Decisions, missions, payment, presentation, and validation references | Exact affordability, payment ownership, meaningful mission work, expiry and cancellation, and coherent presentation |
| `PS-S068`, `PS-S069` | Diplomacy and war skill plus syntax reference | General subject eligibility, point grants versus status mutations, subject lifecycle, native scope questions, and shared owners |
| `PS-S073` to `PS-S078` | Event assets and relevant family, provenance, portrait, and reference-library guidance | Distinct asset families, actual consumer verification, source modes, lineage, and production boundaries |
| `PS-S080` to `PS-S087` | Current event-planning skill and all supplied planning references | Thorough event design, selected surfaces, direction-only localisation, presentation, and delivery structure |
| `PS-S088` to `PS-S092` | Current event skill and integration references | Immediate effects, event details, log and evolution ownership, country continuity, and selected terminal-surface boundaries |
| `PS-S098` | Current improvement-loop skill | Near-completion review and explicit disposition of proposed improvements |
| `PS-S102` | MTTH skill | Appropriate timing and score analysis without misreporting engine probabilities |
| `PS-S107` | Current subagent skill | Bounded specialist responsibilities and parent integration ownership |
| `PS-S116` to `PS-S119` | XLSX skill and complete references | Authoritative workbook handling, preservation, current schema inspection, and export obligations after an accepted save |
| `PS-S120` | Current `AGENTS.md` | Source authority, specs and plans, documentation rules, verification limits, and completion standards |
| `PS-S121` | Current `CHAOS_REDUX_MECHANICS.md` | Shared mechanics and Chaos ownership context |
| `PS-S126`, `PS-S127` | Current dynamic effects and trigger registries | Helper contracts, lifecycle and identity boundaries, scope handling, and shared system reuse |
| `PS-S129` to `PS-S151` | Current specialist definitions | The supplied role contracts and their actual applicability |

Every `PS-Snnn` citation resolves to its exact original origin and hash in the JSON catalog.
An inclusive range such as `PS-S050` to `S052`, including the equivalent en dash notation used in the numbered parts, resolves to each individual source in that range.
The shorter table above is a reading guide, not a replacement for the complete 151-row catalog.

## Repository investigation and exact read scope

The separate repository audit examined `klimPaskov/Chaos-Redux` at commit **`41bc4e5045a7b5c131be69dda2f08079d478634c`**.
It began after the supplied-source gate.
It retrieved **24 complete text payloads**, read **15 texts in full**, and read **9 through targeted sections**.
Every complete payload independently recomputed to the Git blob SHA reported by GitHub.
A verified complete payload does not turn a targeted read into a full-file read.
The JSON records the individual read scopes and line spans without changing their meaning.

The parent additionally read four complete contracts: the liberation release coordinator, universal cost framework, exact quotation triggers, and war-declaration counting documentation.
The first two were initially fetched from `master`.
Later pinned payloads were obtained for all four, and their bytes were compared with the earlier full-read material.
All four contain exactly the same source text.
Each convenience text copy has one additional trailing line feed, which is recorded separately rather than treated as repository content.
The first two original connector payloads also match the pinned payloads byte for byte and have the same Git blob SHA.
The additional reads can therefore be cited at the pinned commit without assuming that a branch name establishes a pin.

The repository review and its payload ledger are separate from both the 151 supplied-source records and the catalog investigation.
Their working-record filenames and hashes are preserved in the JSON.
The links below identify the actual pinned source files.

### Repository citation register

| Token | Source and read scope | Supported finding and practical limit |
| --- | --- | --- |
| `R-AUTONOMY` | [Offline autonomy-state reference](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/paradox_wiki/Autonomy%20state%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md), full read. [Offline effect section](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/paradox_wiki/Effects%20-%20Hearts%20of%20Iron%204%20Wiki.md#L1432-L1484), targeted. [Famine native-score writer](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/famine_opposition_effects.txt#L189-L270), targeted, with its [trigger source](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_triggers/famine_opposition_triggers.txt) read in full | Ladder fields and a genuine source precedent for a dynamic native points write. They do not establish installed scale, useful headroom, retained score, legal promotion, or universal DLC compatibility |
| `R-AFRICA-STATE` | [Africa Charter autonomy definitions](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/autonomous_states/012_africa_autonomy.txt), full read | The two mod states require consent and current host identity, forbid ordinary level-taking and level-losing, and suppress ordinary autonomy AI desires. Their score retention and practical use are separate questions |
| `R-AFRICA-OWNER` | [Charter owner documentation](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/012_africa/charter_autonomy_and_focus_ai.md), full read. [Owner effects](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/012_africa_effects.txt#L1008-L1130) and [host-generation trigger](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_triggers/012_africa_triggers.txt#L433-L451), targeted | Event 012 owns its constitutional relationship writes, consent, and host succession. No demonstrated generic score adapter makes those stages advance |
| `R-063` | [Current Subject Independence event](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/events/063_subject_independence.txt), full read | A legacy random-subject release and former-master response exist. This is not an established exact-target local settlement API |
| `R-063-PLAN` | [Rework README](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/063_subjects_break_free_specs/README.md) and [connections chapter](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_4_evolutions_clusters_and_connections.md), both full reads | Proposed autonomy-sensitive connections and a broader rework, with unresolved acceptance stated in its README. Those proposals do not prove current executable behavior |
| `R-COST` | [Universal cost framework](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/systems/universal_cost_modifier.md), full parent read with pinned-byte equivalence verified | Exact quotation, payment, settlement, and refund ownership if an accepted implementation introduces a spendable payment |
| `R-QUOTE` | [Exact quotation and affordability contract](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_triggers/chaosx_universal_cost_exact_triggers.md), full parent read with pinned-byte equivalence verified | Pure inclusive affordability, exact quote handling, and agreement between display and payment. Source review is not native execution |
| `R-WAR` | [War-declaration counting](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/systems/chaos_meter/chaos_meter_war_declaration_counting.md), full parent read with pinned-byte equivalence verified | The shared war-relation handler owns qualifying war Chaos. The documentation does not establish observed callback behavior in this session |
| `R-006-API` | [Country API](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/006_independence_wave/country_api.md) and [evolutions documentation](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/006_independence_wave/evolutions.md), full reads. [Overview](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/006_independence_wave/overview.md) and [root event](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/events/006_independence_wave.txt#L1-L215), targeted | Current origin, generation, existing-content, and release-root ownership. Collection membership alone is not authority to assign another country's creation package |
| `R-006-HOST` | [Former-host response](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/006_independence_wave/host_response.md), full read | Bounded response and queue precedent. Its political operations remain specific to Event 006 |
| `R-006-FRONT` | [Reclamation front lifecycle](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/006_independence_wave/reclamation_front_lifecycle.md), full read | Exact participants, finite objectives, receipts, rollback, and cleanup precedent. It is not a generic Event 117 confrontation API |
| `R-IMRO` | [IMRO README](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/110_imro_specs/README.md) and [Freedom or Death chapter](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/110_imro_specs/110_imro_spec_part_6_freedom_or_death.md), full reads. [Integration handoff](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/110_imro_specs/110_imro_integration_handoff.md), targeted | Current planned ownership of historical 144, complete current-subject participation, and sovereignty-preserving transaction principles. Named integration helpers remain proposed contracts |
| `R-PARTITION` | [Partition integration chapter](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/113_the_partition_specs/113_the_partition_spec_part_9_tasks_and_integrations.md), full read | Current planned identity and integration boundaries for actual sovereignty and existing country content. The chapter does not establish a live Tasks API |
| `R-IDENTITY` | [Current event index](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/README.md), full read. [Stale Event 021 references](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/021_random_civil_war_specs/021_random_civil_war_spec_part_7_event_006_country_packages_and_focus_handling.md#L505-L521), targeted. Related owner sources, workbook, directory inventories, and targeted queries are enumerated in the JSON | Current identity conflicts and a bounded search that did not locate an actual Autonomy 117 or 128 root or a current Warlords 116 owner package. No universal absence claim is made |
| `R-CATALOG` | [Authoritative XLSX](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/spreadsheets/chaos_redux_events_catalog.xlsx), structural read-only analysis. [Spreadsheet README](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/spreadsheets/README.md) and [exporter](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/.tools/export_event_catalog_csv.py), full text reads | Actual workbook identity, schema, legend, repeated membership slots, and source/export rules. No save, export, recalculation, or rendering occurred |
| `R-RELEASE` | [Liberation release coordinator](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/systems/liberation_release_coordinator.md), full parent read with pinned-byte equivalence verified | Supplemental shared release ownership and transaction context. It does not authorize assigning an existing country a new creator origin |

All 24 audit payloads remain in the JSON ledger, including the South Africa trigger inventory that supplies a checklist of referenced subject IDs.
Referenced IDs were not mistaken for inspected native definitions.
The nine targeted reads retain their actual spans, even when a complete file was downloaded and searched.
Repository directory and search records are recorded as metadata evidence, rather than additional full text reads.

### Catalog facts and preservation evidence

The actual workbook was analyzed read-only across its five sheets: Events, Clusters, Cluster Memberships, Scenarios, and Legend.
The inspection covered structure, headers, tables, relevant rows and coordinates, validation, conditional-format metadata, legend values, and membership reconciliation.
Its **98,437 bytes** retained SHA-256 **`882cabb80387a4999ea67d40b28952c4479e4382a0e38fa18b27ec0e08a8c346`** before and after analysis.
The recomputed Git blob matched **`8898385d0cb4d8993b4818557acd9b64d2caec2a`**.

At the pinned commit, ID 117 is **5-Way Civil War**, ID 128 is **Autonomy**, and both are **Unavailable**.
Neither row belongs to a cluster in the inspected workbook.
Liberations is cluster 2 and preserves the ordered member IDs `5, 6, 6, 6, 63`, with severities `Severe, Low, Medium, High, Medium`.
These are current catalog facts, not a completed migration to the requested Event 117 Autonomy identity.
The existing ID 117 row is not vacant.

No workbook writer saved the downloaded evidence copy.
The exporter was fully read but not executed.
There was no workbook edit, CSV export, recalculation, visual rendering, external publication, or catalog status promotion.
The README and exporter convenience copies each contain one additional trailing line feed.
Removing only that line feed reproduces their reported source Git blobs exactly, and the register retains source and convenience-copy hashes separately.

## Historical references

### H-01: Statute of Westminster 1931

Source: [the enacted seven-page statute](https://www.legislation.gov.uk/ukpga/1931/4/pdfs/ukpga_19310004_en.pdf), read completely by the parent.
Sections 4 and 10 were considered in the context of the full statute.
The reference supports the writing direction's distinction between greater legislative autonomy, continued association, consent, and differing adoption provisions.
It does not establish a single constitutional ladder for every subject country or justify copying that arrangement into the game's mechanics.
No quotation from it is required by the plan.

### H-02: Philippine independence memorandum, September 8, 1943

Source: [Foreign Relations of the United States, 1943, Volume III, document 978](https://history.state.gov/historicaldocuments/frus1943v03/d978), with the relevant September 8 memorandum read by the parent.
Its discussion of economic reconstruction, constitutional continuity, and continuing defense arrangements supplies period context for the practical questions surrounding independence.
The connection to administrative preparation and security is an explicit design inference.
The memorandum expresses its issuing government's position and is not a neutral verdict on the Philippines' proper political choice.
It provides no numerical risk rule for the game.

The original URLs and parent read scopes are recorded in the JSON.
No preserved byte hash for either historical web source was supplied to this curator, and no such hash is invented.
Neither reference is final localisation or a required historical-person roster.

## V-AUTONOMY: a verification dependency, not a read source

`V-AUTONOMY` identifies work that must establish native compatibility before universal implementation acceptance.
It must not be counted as a source read or as a successful engine test.
The supplied-source gate is complete even though the separate native evidence remains unavailable.

The required evidence is:

1. The installed effect, trigger, dynamic-variable, and modifier documentation relevant to native autonomy, subject identity, and the selected integration surfaces.
2. Loaded autonomous-state definitions, current defines, DLC conditions, mod overrides, and actual override order.
3. A complete supported-family matrix, including ordinary subjects, dominions, collaboration governments, locked arrangements, custom Charter subjects, capped intervals, nested subjects, special countries, and no-DLC configurations.
4. Each family's actual point interval, precision, retained delta, cap or overflow behavior, lawful progression route, remaining political gates, and owner consent requirements.
5. Accepted owner handling and evidence for any family where native score presently has no demonstrated useful progression route.

The repository provides real point-writing and lifecycle precedents.
It also provides a concrete locked-owner conflict in the Africa Charter definitions.
Neither fact establishes universal useful support.
The package preserves that implementation acceptance dependency without treating a metadata receipt, an attempted points call, an invented economic substitute, or a changed relationship as proof that the requested autonomy benefit works.

## Specialist use and actual execution route

All **23 current supplied role definitions** were read during the team gate, together with the 20 earlier TOML representations for comparison.
Reading a role does not mean it was executed.
Relevant roles were applied through **standard collaboration agents with explicit supplied role guidance**.
No native custom Claude agent runtime, configured Claude model label, or unavailable execution backend is claimed.
The source-reading team was separate from the later specialist reviews.

The applied planning roles cover repository exploration, read-only catalog inspection, scripted-system architecture, decision and mission design, AI and probability, the improvement loop, localisation direction, documentation curation, and final completion auditing.
The parent handoff records the final completion review and every acceptance disposition.
Asset production, portrait production, focus implementation, 3D production, and other unused role surfaces were not invoked merely because their definitions were supplied.
Future production roles are identified by the integration handoff only when their actual surface is required.

The documentation curator compiled this register from the passed gate, the original inventory and duplicate verification, all reader ledgers and reports, the repository review and payload ledger, the catalog review and evidence, and the verified supplemental parent-read payloads.
The curator fully read the supplied documentation-curator role and the relevant current documentation instructions.
This work did not repeat the broad gate or replace the original readers' attestations with a personal full-reading claim.

## Verification limits retained in the package

No callable HOI4 tool route was exposed in the recorded tool inventory.
The installed Windows and WSL-mounted game roots checked during the repository audit were unavailable.
No installed native autonomy definitions, native game documentation, runtime save, game execution, or live playtest was inspected.
The repository's offline autonomy reference and relevant offline Effects section were available and read at the recorded scopes.
No public Paradox wiki browsing is claimed.

No actual visual-reference library, installed texture, native GUI, rendered game screen, or finished event art was inspected by this planning package.
Asset dimensions and family guidance in the specification remain source-derived planning contracts until their real consumers and references are inspected.
The workbook analysis likewise makes no visual-rendering claim.

Source-derived arithmetic and AI reasoning are planning evidence, not measured native probabilities or observed AI behavior.
Current source contracts and neighboring proposals retain their actual implementation and acceptance limits.
The completed source gate does not remove the explicit native compatibility, identity migration, or owner-contract proof requirements recorded in the parent integration handoff.

## Register verification

Compilation reverified all 151 unique-source hashes against their gate records and completed reader ledgers.
It reverified all 174 physical-record hashes and confirmed that the 173 text origins resolve through the source catalog and aliases.
It independently recomputed all 24 repository audit Git blobs, all four supplemental parent-read Git blobs, and all three catalog-source Git blobs.
The supplemental pinned payloads were compared with the actual earlier full-read material before inherited reading coverage was recorded.
Each source token used by the eight numbered parts resolves in the accompanying JSON, while `V-AUTONOMY` remains explicitly typed as a future verification dependency.
