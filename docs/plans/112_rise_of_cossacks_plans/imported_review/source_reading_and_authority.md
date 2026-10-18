# Source reading and authority

## Status and purpose

The supplied-source reading gate is complete.
The parent and three collaborating role agents processed all 90 unique text variants represented by 132 supplied text paths, totaling 2,594,283 unique raw bytes across five archive objects.
The consolidated coverage check reports `PASSED` and an empty error list.
These counts describe the supplied text collection and its exact-byte equivalence groups, not a claim that the entire repository, installed game, external historical literature, images, binaries, or runtime has been reviewed.
The controlling reading evidence is `source_audit/consolidated_reading_coverage.json`, with raw-byte SHA256 `2e9a9f0dd5165e4b97416a99559e7e01ba55f95efd74b9c97fac73684ad4ea9d`.
The authority rules come from the Project Source Protocol, current AGENTS, current planning skill, and current role routing skill, identified as S19, S58, S60, and S69 in the source index below.

This document records source authority for the Event 112 Rise of Cossacks planning package.
Its companion `implementation_usage_maps.md` describes future ownership, tool use, evidence and release blockers.
Neither document implements gameplay, produces art, changes the workbook or CSVs, or establishes runtime acceptance.

## Reading method and completeness

The protocol was read before substantive project work.
The team unpacked both project-source archives and their nested role archives and inventoried the standalone role archive.
Each supplied text path was assigned to a group only after exact raw-byte SHA256 verification.
One full representative could satisfy a group of byte-identical aliases.
Every differing old and current variant received its own complete semantic read.
Similar titles, matching lengths, normalized text, previews, archive listings, search results and summaries were never used as proof of equivalent complete content.

Readers emitted complete decoded text in bounded chunks, generally around 20,000 to 26,000 characters, with smaller chunks where needed.
Readers semantically processed the returned text and recorded continuous zero-based, half-open character ranges.
A truncated tool response did not count as complete coverage until the affected range was fully replayed.
The raw-byte hashes remain independent of the decoded-character coverage coordinates.
Some readers used universal-newline decoding and others preserved original CRLF characters, so the recorded endpoint must be interpreted using that reader's coordinate declaration.
A character offset is not a byte offset.
The automated consolidation checked range continuity and alias hashes after the semantic reads.
The consolidation script and byte scans did not replace those reads.

The current full 3D owner skill provides an explicit example of shared coverage.
The documentation curator read original UTF-8 decoded characters `[0,48000)`.
That partial read was transferred to the scripted system architect, who completed `[48000,116222)` and replayed the last clipped chunk before accepting completion.
The curator's personal ledger correctly retains a partial and transferred status for that skill.
The consolidated ledger records complete team coverage and the split attribution for S52.
The parent separately took the full old planning skill and both super-event owner skills when work was redistributed.

### Actual collaborators

The role names below describe the three agents actually collaborating through this conversation's orchestration tools.
They were given bounded role prompts based on the supplied canonical definitions.
This is not evidence that a project-local custom-agent launcher, installed TOML model selection, HOI4 MCP service, Meshy route or Blender bridge was invoked.
The parent retains integration and completion responsibility under S58 and S69.

| Actual participant | Actual contribution | Coverage accounting |
| --- | --- | --- |
| Parent | Protocol and shared authority review, both planning variants, both super-event variants, source consolidation and later pinned repository review | Seven full variant entries in the consolidated ledger, including three prerequisites also read by the curator |
| `chaosx_improvement_loop_planner` | Complete assigned mechanics, events, focuses, decisions, improvement-loop and associated role reading, then planning support | 18 full variant entries |
| `chaosx_scripted_system_architect` | Complete assigned catalogs, configuration, script and GUI infrastructure, role sources, and the redistributed 3D owner sources, then architecture support | 40 full variant entries, including shared coverage of S52 |
| `chaosx_documentation_curator` | Complete assigned asset and animation variants and ten pairs of role definitions, three shared prerequisites, version-conflict notes and these documentation maps | 25 fully read revised assigned variants plus three prerequisite entries, with S52 partial coverage attributed separately |

The row counts overlap and must not be added to infer the number of unique supplied sources.
The unique total remains 90.
The canonical future roles are mapped separately in the companion document.

### Archive inventory

| Archive object | Read treatment |
| --- | --- |
| `project_sources/01-subagents.zip` | All 20 role definitions extracted and hash-grouped against the nested baseline copies |
| `project_sources/24-all-project-sources.zip` | All supplied baseline Markdown, TOML and CSV text read, with its nested role archive expanded |
| `source_audit/baseline_archive/subagents.zip` | All 20 contained role definitions included in exact-byte alias verification |
| `upload/all-project-sources(20261010-065955).zip` | All supplied current Markdown, TOML and CSV text read, with its nested role archive expanded |
| `source_audit/current_archive/subagents.zip` | All 20 current role definitions read as distinct current variants where their hashes differ |

The exact archive-member and alias inventory is `source_audit/manifest.json`.
The complete per-reader range records are preserved in `source_audit/parent_coverage.json`, `source_audit/reader_planner/coverage.json`, `source_audit/reader_architect/coverage.json`, and `source_audit/reader_docs/coverage_ledger.json`.
The consolidated ledger is the final joined coverage record.

## Authority order for this package

The explicit current user brief controls the event's identity, classification and requested design direction.
The current attached technical owner skill controls its domain where its detailed contract resolves an older instruction or a stale role summary.
Current AGENTS supplies shared workflow, ownership and validation rules.
The source protocol governs the all-source reading gate and honest planning-only handling of unavailable implementation capabilities.
Older source variants remain historical evidence and must not silently restore superseded requirements.
The pinned repository is implementation evidence at one revision and does not supersede the newer attached owner instructions.
Installed vanilla documentation and exact installed precedents remain primary authority for engine syntax and behavior, with relevant offline wiki sections also required before engine-facing edits.
No runtime behavior follows solely from a planning example, a helper name, a catalog row, or an old tool artifact quoted in documentation.
These rules are grounded in S19, S58, S60 and S69.

An accepted design records its acceptance basis separately from implementation evidence.
A file's placement under `docs/specs/` does not by itself prove user acceptance, implementation or validation.
The normal destination for the accepted specification is `docs/specs/112_rise_of_cossacks_specs/`.
Working implementation plans belong under `docs/plans/112_rise_of_cossacks_plans/`, with role handoffs under that plan's `subagent_handoffs/` directory.
This documentation task prepares reviewable planning material and does not promote files into the repository.
S58 and S69 require the final parent review to preserve that distinction.

## Catalog conflicts and their disposition

The current brief specifies Event 112 Rise of Cossacks, original 122, Minor Fire-Once, To Be Reworked, chaos level 1 and Formables Medium.
It also specifies immediate emergence in a random valid East Slavic state and The Hosts Answer as a substantive later evolution.
Those instructions control this package.

| Surface | Supplied catalog evidence | Planning disposition | Future alignment gate |
| --- | --- | --- | --- |
| Event number and title | Both exports label ID 112 as Lootboxes, while its description concerns a national wrestling tournament | Use the user's Event 112 title in the specification and preserve the catalog conflict explicitly | Audit actual runtime identifiers, registrations, log indexes and existing owners before claiming `chaosx.nr112.1` is safe to wire |
| Original Cossack row | Both exports place Rise of Cossacks at ID 122 and provide only a brief rise-and-expansion premise | Preserve original 122 as the migration reference | Map old row, current event identity and every runtime consumer through one reviewed crosswalk |
| Classification and status | Both relevant old rows are Unavailable and do not contain the user's Cossack classification or evolution | Minor Fire-Once, To Be Reworked, chaos 1 and The Hosts Answer follow the current user brief | Update the authoritative workbook only after an authorized alignment pass, then regenerate CSV exports |
| Formables membership | Both cluster exports identify Formables as cluster 6, Minor Repeatable, chaos 3, with members 3, 12, 38 and 48 at High, Severe, High and Medium | The user's Formables Medium membership is the proposed Cossack member metadata | Preserve the cluster's own metadata unless separately changed, and align event-side and cluster-side membership together |
| Scenario registration | Neither scenario export contains a Cossack scenario | Do not infer an existing scenario registration or ID | Allocate and wire an accepted scenario only after repository and workbook ownership checks |
| Wider catalog consistency | Current Event 31 has a blank event-side cluster field while current cluster 16 still lists it | Record as an unrelated catalog consistency finding | Do not repair unrelated rows in this package |

Catalog evidence is S14 and S61 for events, S11 and S68 for clusters, and S22 and S55 for scenarios.
The architect's complete source comparison is `source_audit/reader_architect/catalog_variant_deltas.json`.
Both event exports contain 165 rows.
The current cluster export still contains 19 rows but moves Intelligence from ID 8 to ID 20.
The current scenario export contains 16 entries against 15 in the older export, moves Assassin Network from SCN-014 to SCN-019, and adds SCN-016 Global Jihad.
These changes establish that the supplied variants differ materially and were not interchangeable reading copies.
They do not authorize unrelated gameplay or catalog work.

## Newest-owner resolutions

| Conflict or drift | Resolution used in this package | Source basis |
| --- | --- | --- |
| Older broad wiki-first wording versus the supplied-source hard gate | Complete the supplied collection first, then read relevant offline and installed engine sections before engine-facing work | S19 and S58 |
| Older optional CXT weekly maintenance versus current player-triggered grants | Registration and pending markers may use documented bounded seams, while grants and replenishment stay with player debug decisions | S13 versus S58, with `docs/testing/chaosx_test_country.md` still required for implementation |
| GUI rewrite listed as mandatory in some summaries versus detailed current GUI rules | Inspect and render before and after remain required, while `hoi4.gui_rewrite` is an optional application route | S44, S58 and S71 control over stale summary wording |
| Current process configuration versus older command-name prose | Verify the actual connected process, package version, health and live schemas instead of inferring capabilities from either launcher string | S08, S63 and S58 |
| Older asset reference root `assets/vanilla_reference/` versus current `assets/gfx_references/` | Current attached asset paths govern future production, and the pinned older shelves are historical reference metadata only | S06 versus S64 |
| Separate older ComfyUI skill versus integrated current portrait workflow | Use current asset and portrait ownership, preserve grounded identity, and leave provider operation for styled grounded finals to the user | S02, S64 and S82, supported by R01 below |
| Fictional random leaders in existing host carriers versus current grounded-source policy | Reuse existing carrier identity only through coordinated ownership review and remedy unsupported identities without inventing replacement people | S64, S78 and S82, with parent-attributed pinned carrier evidence below |
| Old direct-to-Blender firearm routing and stale current 3D role description versus detailed current body-first route | Separate item-free Meshy 7 body and item tasks, provider rig and actions for eligible bipeds, then live Blender assembly and repair | S52 and detailed S80 control over S12 and stale summary wording |
| Old adapter skeleton or key synthesis versus current live authoring rule | Missing geometry, bones, skinning and skeletal keys are authored in the verified live Blender route, while adapters process and ingest actual authored results | S52 controls the production route |
| Old paid recovery while credits permit versus current attempt limits | Use the accepted job's locked generation and retry allowances, with the documented single rig or action attempt before ordinary live repair | S52 and S80 |
| Old general 2D DDS conversion applied to model textures versus current model material rules | 2D sprites retain their exact uncompressed BGRA contract, while model diffuse uses BC1 and normal/specular use BC3 with complete mips | S64 and S52 |
| Old flat animation strip assumptions versus current maximum texture side | Plan real source frames and split synchronized strips when necessary to respect 16,384 pixels without losing required semantics | S15 versus S53 |
| Old exposed Harder Crises for Players switch versus current shared mechanics | Treat the current always-active player weighting and shorter cooldown behavior as the shared baseline | S05 versus S49 |
| Old repeated-key, helper-output and population-loss shorthand versus current exact contracts | Retain exact source occurrences, caller-owned temporary outputs, measured transaction results and no double debit | S47, S54 and S58 |
| Pinned state-puzzle workflow says required entries remain visible while current GUI guidance honors explicit visibility hooks | Follow the current owner contract and record the intended requiredness and visibility policy independently before generation | S44 and S51, with R06 treated as an older supporting workflow |

The version changes in model declarations describe supplied configuration metadata.
They do not establish which model or runtime route executed this conversation.
The detailed source notes are `source_audit/reader_docs/requirements_notes.md`, `source_audit/reader_architect/requirements_notes.md`, and `source_audit/reader_planner/requirements_notes.md`.

## Pinned repository evidence after the reading gate

The parent established read-only access to `klimPaskov/Chaos-Redux` at commit `a3ef485c5da7e2337122eca04ac65c175050f251`, dated October 6 in the parent's repository evidence.
The attached current owner collection is dated October 10 and remains the newer policy source.
The following carrier facts are attributed to the parent's complete reads at that pinned revision.
The curator did not independently read those six carrier files.

| Parent-read path | Relevance |
| --- | --- |
| `common/country_tags/006_independence_wave_countries.txt` | Existing tag allocation and shared carrier ownership |
| `common/country_tags/chaosx_countries.txt` | Existing project country identities and tag crosswalk |
| `common/collections/006_independence_wave_country_collections.txt` | Independence Wave carrier collections |
| `common/collections/chaosx_country_collections.txt` | Shared country classification and collection seams |
| `history/countries/DHC - Don Host Emergency Circle.txt` | Existing Don Host carrier history and identity |
| `history/countries/KHC - Kuban Host Provisional Council.txt` | Existing Kuban Host carrier history and identity |

The parent reports DHC and KHC as existing Event 005 carriers, despite the 006 names on some shared files.
The histories include invented randomized leader names that conflict with the current grounded-source policy.
Their existence means that a future Cossack package must coordinate carrier reuse with the existing owner, preserve living countries and their meaningful trees, and remediate identity sources through an explicit shared handoff.
A new tag cannot be invented as a convenience bypass.
A living DHC or KHC cannot be silently replaced, reinitialized or stripped of content merely because Event 112 needs a host.
The exact reuse, non-reuse and cleanup branches remain implementation acceptance questions for the parent and country owner.

### Curator-read supporting documents

The curator fetched and fully read the eight text documents below at the same pinned commit after the common gate opened.
The read record is `source_audit/reader_docs/repo_support_manifest.json`.
Every saved file reproduces the fetched Git blob SHA1, and the manifest separately records its raw-byte SHA256, byte size, complete decoded-character ranges and local source copy.
These eight post-gate supporting documents are additional evidence and are not silently added to the 90 supplied-source count.
Their quoted historical artifact hashes and source claims are evidence about those documents, not this task's execution.

| ID | Fully read supporting text | Raw-byte SHA256 |
| --- | --- | --- |
| R01 | [Portrait production](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/.agents/skills/chaos-redux-event-assets/references/portrait-production.md) | `2ccfc59073bbea4a4fab1dafd374b334eebd64060706b28f9e45ed36d20136ea` |
| R02 | [State puzzle package instructions](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/README.md) | `42a8be6c3b0ca5f2c20bdac788c1e50b03f690a63c8eb9c2ece61f8004fce3e7` |
| R03 | [Historical reference library README](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md) | `28c20975491c65c1e256479a85b6ce207d6cd2d0385fa001b82541f0c63dce6b` |
| R04 | [Historical reference catalog](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md) | `d88b626038ae129be6853addd7c432a4c517b48e63f9ffcb1c7d127d8d9c0087` |
| R05 | [Historical reference provenance manifest](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/REFERENCE_MANIFEST.md) | `347719dea2166dd96e1deb9b5d45ede38ee34a4edef611af1c8a93cb41199eb0` |
| R06 | [Universal state registry workflow](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/universal_state_registry_workflow.md) | `00fe0396ffe982a0691b12034ed1ae927faa62a2b8a50aabaaffea3e8ac75b9f` |
| R07 | [Category attachment audit](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/category_attachment_audit.md) | `d4a7a9f16cbca0fbe256370d8e6a801d099a813d7ebe74acda9ec0e8459c1f92` |
| R08 | [State puzzle validation checklist](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/validation_checklist.md) | `f04cb3d23831708cb5516e236004c55c49915516a33de21dab38c9ee4cb48b34` |

The current canonical `assets/gfx_references/README.md` and `assets/gfx_references/CATALOG.md` paths returned 404 at the pinned revision.
The historical counterparts under `assets/vanilla_reference/` were discovered through read-only repository search and then fetched in full at the pinned SHA.
The older metadata describes review copies, extracted source dimensions, ownership paths and earlier MCP renders.
The curator did not fetch or visually inspect the associated PNGs, contact sheets, DDS files, installed vanilla consumers or historical MCP resources.
The metadata's counts, frame declarations, extraction build and artifact hashes have not been independently revalidated against those binaries in this task.
Its source dimensions are reference evidence and never override the actual consumer selected for Event 112.
R03, R04 and R05 establish those limits explicitly.

R01 confirms the grounded portrait state contract.
A defensible attributed source can be preserved unchanged, cropped explicitly, resized deterministically and wired as `source_placeholder`.
That status remains pending the user's HOI4-style replacement and is not `styled_final`.
`replacement_pending` applies only while an explicit styled-final request is outstanding.
`styled_final` requires the user-supplied output plus workflow revision, provider or job evidence and independent identity, framing and provenance review.
No face may be invented when a grounded source is unavailable.

R02, R06, R07 and R08 require an exact installed-map state puzzle for territorial proof involving several independently qualifying states, alternate groups or live territorial counts.
The universal geometry registry and finite candidate manifests are build inputs, and runtime play cannot invent a new state texture or positioned GUI node.
The state registry builder and consumer compiler are archived provenance tools at the pinned revision.
A new consumer or changed map needs a deliberate reviewed restoration or replacement of that producer chain before generated artifacts change.
The active runtime generator is `.tools/generate_formable_state_puzzle_runtime.mjs` and discovers complete manifests directly under `docs/formables/state_puzzles/*/`.
A successful individual window render cannot prove that every relevant category attaches the generated `decision_category` scripted GUI.
Map provenance, per-state shared qualification, dynamic owner/controller hovers, non-colour status cues, each category attachment and exact DDS round trips remain separate acceptance gates.

### Additional parent evidence received during drafting

The parent repository manifest is `source_audit/root_repository_evidence_manifest.json`.
It records 11 fully read and Git-blob-verified files plus a 404 result for `docs/specs/shared_identifier_registry.md`.
In addition to the six carrier files above, the parent read `events/000_chaosx_events.txt`, `common/script_constants/event_system_constants.txt`, `common/script_constants/event_cluster_constants.txt`, `events/048_old_great_bulgaria.txt`, and `events/073_mongols_rise.txt`.
The manifest records a 162-entry events inventory with no Cossack, 112 or 122 filename and nontruncated common and history inventories.
An inventory result is discovery evidence and does not establish namespace freedom or a complete content audit.

The parent reports Formables cluster ID 6 with unlock tier 3 and a Medium severity floor of 1 in the pinned constants.
The user's independent Event 112 chaos level 1 remains authoritative, while an invocation through the existing cluster may still respect the cluster's own tier 3 gate.
This separation must appear in the later registration crosswalk.
The parent also reports broad instant cores and fixed ten-unit creation in Event 048, and fixed cavalry plus continent-wide claims in Event 073.
Those are inspected existing behaviors, not approved templates for Event 112's dynamic strength or territorial integration.
The source copies and individual hashes remain in the parent manifest.

## Additional architect repository evidence

The architect reports full semantic reads of nine further supporting files at the same pinned repository revision.
The exact file identities and returned decoded-character ranges are recorded in `repository_evidence.json`.
The normalized local reference copies are not byte baselines for later repository changes.
The Git blob identities below are those returned by the repository connector and recorded by the architect.
The curator fully read that manifest and `repository_contract_review.md`, not the nine underlying bodies personally.

| File read by architect | Returned Git blob identity | Complete decoded-character coverage |
| --- | --- | --- |
| `docs/testing/chaosx_test_country.md` | `e1b10f9f5630d83d76f36319d75183fb263da6c3` | [0, 19000), [19000, 27195) |
| `docs/systems/universal_cost_modifier.md` | `f053e8d76ef5d7232fd622a18b7ae7d9faa77e83` | [0, 15291) |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | `06e1b00524b565f1a6421bc6c9db720193ab69db` | [0, 13000), [13000, 29817) |
| `common/scripted_effects/chaosx_universal_cost_effects.md` | `63742514d7ae78b3ccadb4efd6b52d8d6d101ddf` | [0, 21584) |
| `common/scripted_effects/chaosx_universal_cost_effects.txt` | `cb073610d5f466c403fc88e4e98e1e596fd50c7a` | [0, 22000), [22000, 44000), [44000, 65182) |
| `common/script_constants/chaosx_universal_cost_constants.txt` | `c9dae6d241d7a88e08914210046dcaa868676bf0` | [0, 4094) |
| `common/scripted_triggers/chaosx_universal_cost_triggers.txt` | `f8b0362b89a89ef67160efc231789ebd563521e9` | [0, 9281) |
| `common/raids/_documentation.md` | `dd76bf73e0dc701ccc163cd9abfafdd00da3835c` | [0, 16283) |
| `common/raids/016_brilliant_scientist_portal_raids.txt` | `ad52acacb7d9be15cce352d1d311758a50dfb833` | [0, 18138) |

The review records source-level conflicts in the older universal-cost and civilian-loss helpers, including conditional arithmetic implications and missing current exact-trigger paths.
Those findings do not prove an installed-game defect or authorize an event-private shared-helper rewrite.
The parent must resolve the current owner contracts and implementation before exact payment or civilian movement can ship.
The native raid documentation and Event 016 precedent are source evidence, not proof that the selected cavalry raid works in the current engine or DLC configuration.
The CXT document is fully read by the architect, and no destructive debug invocation or runtime fixture was executed.
The parent, curator and architect manifests together report twenty-eight additional distinct repository text files outside the ninety supplied variants.

## Supporting references still required for implementation

The supplied-source gate covered every supplied source, including all differing variants.
It did not supply the installed game, active mod stack, workbook, current reference image shelves, provider tooling or most implementation bodies named by the owner skills.
Some supporting repository text has now been read as recorded above and in other team manifests.
The obligations below name the exact supporting sources or bounded source families that the relevant future owner must inspect before relying on them.
A path listed as pending means this documentation package has not established that requirement, not that the file is necessarily absent everywhere.

| Reference obligation | Exact path or bounded family | Current evidence and next owner |
| --- | --- | --- |
| Offline engine rules | `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, and the relevant Event, Decision, Focus, Country, Character, Idea, AI, Interface, Scripted GUI, Localisation, Map and State modding pages | Parent confirmed offline directory availability only in the repository inventory, and each touched engine contract still needs its relevant cited sections and exact revision |
| Installed core syntax | Installed `documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `loc_objects_documentation.md`, `loc_formatter_documentation.md`, and `common/script_constants/documentation.md` | Installed game is absent from the supplied workspace, so the implementation owner must inspect the actual build |
| Native raid scope and costs | Installed `common/raids/_documentation.md`, selected `common/raids/` definitions and their exact effects and triggers | Architect fully read the pinned repository documentation copy and Event 016 precedent, while the actual installed actor, target, RAID_INSTANCE and prepared-visibility behavior remains unverified |
| Scripted GUI context | Installed `common/scripted_guis/_documentation.md`, the selected `.gui` and `.gfx` consumers, and the GUI skill's separately referenced `references/visual-review.md` if present | GUI owner must read and cite the actual consumer before layout construction |
| Formable vanilla precedent | `common/decisions/categories/AUS_decision_categories.txt`, `common/scripted_guis/AUS_antischluss_measures_scripted_gui.txt`, `interface/aus_antischluss_measures_scripted_gui.gui` | R02 names the precedent but this curator did not read those installed source bodies |
| Shared helper bodies | `common/scripted_effects/chaosx_dynamic_effects.txt`, `common/scripted_triggers/chaosx_dynamic_triggers.txt`, `common/mtth/chaosx_mtth_variables.txt`, `common/script_constants/chaosx_date_units_constants.txt` and the exact owner files named by a selected public API | Architect fully read the pinned dynamic effects body and recorded conflicts with the newer owner, while the current trigger, MTTH, date-unit and other called bodies still need exact closure |
| Exact payment framework | `docs/systems/universal_cost_modifier.md`, `common/scripted_triggers/chaosx_universal_cost_exact_triggers.md` and implementing quotation, affordability and debit sources | Architect fully read the pinned cost system, API, effects, constants and legacy triggers, while the two newer exact-trigger paths returned 404 and the documented arithmetic and native debit differences remain integration gates |
| Country identity and ownership | All active vanilla and project tag, cosmetic, character, portrait, country-history and collection definitions, plus installed Workshop and other local mods | Six pinned carrier files are read by the parent, but the full collision and grounded-person ownership audit remains open |
| Current asset metadata | `.agents/skills/chaos-redux-event-assets/assets/gfx_references/README.md`, `CATALOG.md`, `REFERENCE_MANIFEST.md`, the relevant family contact sheets and `scripted_guis/README.md` | Current README and CATALOG return 404 at the pinned older revision, and the visual shelves remain uninspected |
| Visual component roles | `.agents/skills/chaos-redux-event-assets/assets/visual_components/CATALOG.md` and each selected family contact sheet | Pending, and catalog roles must govern reference-only versus permitted persistent background use |
| Portrait and icon processing | Exact current portrait and report processors, achievement backgrounds and overlay, and `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, with the advisor template inactive because no advisor card is accepted | R01 is fully read, while processor and image-byte behavior remain pending |
| State geometry and schema | `docs/formables/state_registry/generated/state_geometry_registry.json`, `docs/formables/state_registry/consumer_spec.schema.json`, `consumer_spec.template.json`, active ordered map roots and state histories | Workflow text is read, but geometry bytes, schema, current map roots and hash coherence are unverified |
| State puzzle producer chain | `.tools/archive/build_formable_state_registry.py`, `.tools/archive/build_formable_state_puzzle_consumer.py`, `.tools/generate_formable_state_puzzle_runtime.mjs`, and selected existing `docs/formables/state_puzzles/*/manifest.json` artifacts | The archive restriction is established by R06, while an authorized restoration or replacement and generator source review remain pending |
| CXT registration | `docs/testing/chaosx_test_country.md` and actual extension registration sources | Architect fully read the pinned CXT document, while selected model and template registration disposition and actual implementation remain pending without automatic periodic grants |
| Selected 3D toolchain | `.tools/3d_pipeline/README.md`, `config/dependencies.lock.json`, `config/meshy_tool_schema.lock.json`, `config/blender_hoi4_adapter.json`, profile and calibration files, wrapper bodies and `references/unit_rebuild_workflow.md` | Owner skill is fully read by the team, while actual lock, source closure, schemas and live tool compatibility remain unverified |
| Selected 3D processing and evidence | `.tools/3d_pipeline/review/review_cli.py`, `review/provider_intake.py`, `review/lab_actions.py`, `review/pdx_textures.py`, `review/export_package.py`, `textures/cli.py`, `audio/master.py`, and `runtime/reimport_runtime.py` relative to `.tools/3d_pipeline/` | These documented paths identify required implementation review and do not establish executed operations or current source integrity |
| Exact selected 3D consumers | Installed `.mesh`, `.anim`, `.asset`, entity, shader, material, sound, counter and any building consumer for the accepted model family | Pending actual source-scale, runtime-scale, action, sound and counter inspection |
| Workbook preservation | `docs/spreadsheets/README.md`, the real catalog XLSX, `.agents/skills/chaos-redux-xlsx/references/catalog.md`, `references/preservation.md`, and `.tools/export_event_catalog_csv.py` | CSVs are read-only source evidence, and no workbook or export mutation is authorized here |
| Runtime mapping and later save evidence | `docs/runtimes.md`, the save inspector implementation and any user-supplied HOI4txt save | Pending if a concrete later runtime question requires them, with saves preserved and their exact version and date recorded |
| Historical text, portraits, symbols and audio | Exact sources selected by the research and asset owners, including author, date, uncertainty, rights and provenance | Parent research may supply historical evidence, and no sourced image, quotation or recording is inferred from a thematic brief |


### Selected presentation and asset boundary

During documentation drafting, the parent selected standard decision categories with exactly two meters and a selected-set formable state puzzle.
The selected package has no dedicated full management window, no frame animation, no new horse currency and no standalone unit-counter asset row.
The mounted rider, horse, separate held item and foot plastun custom 3D visuals are explicit selected requirements over native cavalry and infantry archetypes, with plastun templates and visuals.
All portraits remain source-first, and no ComfyUI or RunPod execution is included.
The companion map therefore leaves the dedicated event UI worker inactive, keeps shared category and puzzle implementation with the parent, activates the 3D workflow and preserves inspection of retained native counter bindings.
These are parent-selected planning surfaces and do not establish that any visual asset or gameplay source has been produced.
Part 12 now fixes the finite production rows, including eighteen reports, six news scenes, three super-event scenes and audio requirements, twenty base focus subjects plus three variants, eighteen decision subjects, nine spirit tiers, eight achievement subjects, four named portraits and one institutional representation, four template emblems, twenty flag families plus three neutral alternatives, and two model entities.
All sixty-seven report situations map to the eighteen report illustrations under explicit truthful-use conditions.
The eighty-three flag bindings are logical obligations and do not imply eighty-three new production jobs.
Civilian relocation is explicitly selected by P04, P11, P12, P14 and GP08, so the exact state-ledger workflow is active for those accepted physical movements.
The three super-event packages and eight achievement rows are active future production requirements.
Named advisor cards remain outside scope.

## Limits of the present evidence

A filtered inventory of the curator's currently exposed tool names returned no HOI4, Meshy or Blender routes.
The parent independently reported the same absence.
No HOI4 server health check, live schema negotiation, domain inspect, render, probability evaluation, compare, map operation, provider generation or Blender authoring ran in this documentation work.
GitHub `fetch_file` and search were read-only source retrieval, and local hashing checked source-copy integrity.
No asset binaries were produced or accepted.
No installed vanilla, Workshop or other local mod collision audit is claimed.
No game was launched, and no live-game behavior was established.
The user retains live-consumer validation under the current project rules without a request for logs or a demand to perform new tests in this planning handoff.

The source-reading gate therefore closes the supplied-source obligation and enables informed planning.
It does not close the future evidence gates mapped in `implementation_usage_maps.md`.

## Complete supplied-source index

Every row below has complete team semantic coverage and exact raw-byte alias verification in the consolidated ledger.
The representative path identifies the readable content variant.
The alias count includes that representative and resolves to the complete `paths` list in the ledger.
`P`, `L`, `A` and `D` denote parent, improvement-loop planner, scripted-system architect and documentation curator respectively.
S52 includes the explicit D-to-A transfer described above.

| ID | Representative source path | Bytes | Aliases | Reader | SHA256 |
| --- | --- | ---: | ---: | --- | --- |
| S00 | `project_sources/21-README.md` | 2,857 | 2 | A | `9f713e2dcaf1e0fad5b070b8a921b23a648a1a01583e4f698cdd50e8e66bce74` |
| S01 | `project_sources/10-chaos-redux-events.md` | 80,791 | 2 | L | `42b1c53c5996f8bb495426b9ebdc6854cdd4309744feddb26df781a0692dd036` |
| S02 | `project_sources/03-chaos-redux-comfyui.md` | 2,456 | 2 | D | `125daa4e66957fcf02f5cd91e3a0a17f4a99395ad0f40c7ae376b4b59393b303` |
| S03 | `project_sources/11-chaosx_dynamic_effects.md` | 19,635 | 2 | A | `73b2740ebfb891c6772de72d456dd1805f5bd3921f61ff60c0df38c6f2c45030` |
| S04 | `project_sources/15-chaos-redux-debug-playtest.md` | 34,086 | 2 | A | `9c6e27b8a86fd27422d8b2ec5302ac6fa7c64d89a564dbbda71db238190e3549` |
| S05 | `project_sources/23-CHAOS_REDUX_MECHANICS.md` | 41,848 | 2 | L | `e3f21aca358f84d085222272bccd1d2896b4c0ef4bb418de079f882975e35da1` |
| S06 | `project_sources/09-chaos-redux-event-assets.md` | 109,712 | 2 | D | `6766e846130e22a1ac0cea89e32bb0fca9495828216a130c1a882e1544212bfd` |
| S07 | `project_sources/08-chaos-redux-event-planning.md` | 197,109 | 2 | P | `4a1a0a46ffe4145d61fe0992ad7eb82650c386af028b21a1dbd10a6e227881cb` |
| S08 | `project_sources/20-config.toml` | 11,714 | 2 | A | `24bcac71960d42d2958fc98b49fd38a5244b0946bf80cf3ddb879a633c269427` |
| S09 | `project_sources/16-chaos-redux-super-events.md` | 33,489 | 2 | P | `001a899b4b19ccf6bdf15a82bd446eae0e290c5f64caec5762883af25976924e` |
| S10 | `project_sources/04-chaos-redux-decisions-missions.md` | 64,394 | 2 | L | `bd92b691ec78d81db2fe9c19f5574e21969dfa951ef08dbb9dc80085cc2034d9` |
| S11 | `project_sources/17-chaos_redux_clusters_catalog-5-.csv` | 5,362 | 2 | A | `689fe07883da14abe2ceb7c29c151db50808cf97a366e60808281b16e37c76a2` |
| S12 | `project_sources/07-chaos-redux-3d-model-pipeline.md` | 96,728 | 2 | A | `45ffc273c4df5ec479c83f193815d2c9ffd6092e18cec54242544c08684442f7` |
| S13 | `project_sources/05-AGENTS.md` | 44,442 | 2 | A | `ba5f6799c692f461e3922e0a2e6687516bba210206c3758b07c37fce5cfb56d4` |
| S14 | `project_sources/19-chaos_redux_events_catalog-5-.csv` | 65,053 | 2 | A | `e2e457ba96ae89b316aa01248eebe41d9aacbafc590f4940b56a55133fcd35c6` |
| S15 | `project_sources/13-chaos-redux-frame-animation.md` | 28,266 | 2 | D | `86469ff50f33ead0690d3709b0523de1992f01a29713b801a6dd08c27b1be870` |
| S16 | `project_sources/12-chaos-redux-scripted-gui.md` | 23,695 | 2 | A | `f85f0a0888b25d14ca6d6b6535ea8b578542e19dac1f5fbd3d9113e51a525b93` |
| S17 | `project_sources/14-chaos-redux-focus-trees.md` | 98,951 | 2 | L | `74805c1f8522ee8630912fd8946c6d547fd43d61e4a907fc71ba08a803253d3f` |
| S18 | `project_sources/02-chaos-redux-improvement-loop.md` | 28,515 | 2 | L | `ca2b6a001f691f2b247823b5b9914a3d04076dff429aa85bc035aa34f6124d73` |
| S19 | `project_sources/25-CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` | 12,728 | 1 | P,D | `e7d9ac3d70b8a883371b5b89aa4bcbe6657b4a87d0b3da31019e1e48bc7101c9` |
| S20 | `project_sources/06-chaos-redux-subagents.md` | 41,493 | 2 | A | `68e6b1d4878e4c87981c9e58cebb1182052555d9313d60748fd573f01ad8223e` |
| S21 | `project_sources/22-chaosx_dynamic_triggers.md` | 3,991 | 2 | A | `6792ee030cb6b658698e92f188f4980e05553f80ba3de8b9260d3cf47fab4843` |
| S22 | `project_sources/18-chaos_redux_scenarios_catalog-5-.csv` | 16,848 | 2 | A | `8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7` |
| S23 | `source_audit/standalone_subagents/chaosx_localisation_auditor.toml` | 9,782 | 2 | A | `8d588111bb27da851af9d16b8c426d6e9b59e517444464225e0a3e91385a161b` |
| S24 | `source_audit/standalone_subagents/chaosx_event_ui_worker.toml` | 10,136 | 2 | A | `56a254896faf78e4c6ca5aa6398fa5ac6b7106ec6bdc6f0efe767acfa879032c` |
| S25 | `source_audit/standalone_subagents/chaosx_event_completion_auditor.toml` | 4,141 | 2 | A | `38180484672c2cb363b40cbdd712ef9dbdd1df9cda9acbc534223ab42fb22990` |
| S26 | `source_audit/standalone_subagents/chaosx_documentation_curator.toml` | 11,319 | 2 | D | `e881bcc4303dac392904464c7bdce47a11d2210f6f794842f56245579c048008` |
| S27 | `source_audit/standalone_subagents/chaosx_super_event_text_researcher.toml` | 3,921 | 2 | D | `c918dae02f2b1127f71134065558f313faec82fba49f3e43022bfeaf3bfb66cb` |
| S28 | `source_audit/standalone_subagents/chaosx_decision_mission_auditor.toml` | 8,994 | 2 | L | `1b1f9e50909d54daf2a11d255873b7382f970871543d751d924d94b015265a32` |
| S29 | `source_audit/standalone_subagents/chaosx_asset_source_researcher.toml` | 3,024 | 2 | D | `f652dfac61f3e41decbdcbb48765b281f7ac7bc0eb7803aa2a89d94c6ccdea7b` |
| S30 | `source_audit/standalone_subagents/chaosx_generated_event_art.toml` | 3,930 | 2 | D | `d056a89535a8740cd6dac3d61cea5f5a73fe9ef6e4d9a87406a86aedc851a38d` |
| S31 | `source_audit/standalone_subagents/chaosx_country_package_auditor.toml` | 8,099 | 2 | L | `d1c6e194082366b514310f76d4c8e7e81679fc81d2be6d23bb59fc16a0ce4bd0` |
| S32 | `source_audit/standalone_subagents/chaosx_scripted_system_architect.toml` | 5,388 | 2 | A | `7c845c07d54d3c19533ed24f6a68a9b77d9e90e056824bd87023916d9a8a89f2` |
| S33 | `source_audit/standalone_subagents/chaosx_3d_model_pipeline.toml` | 27,552 | 2 | D | `f0036ce6d12b60c01c3b1042ddee59bbefad13f8267625efcfd9569ac42d226d` |
| S34 | `source_audit/standalone_subagents/chaosx_skill_maintainer.toml` | 3,258 | 2 | D | `232a9a008c076c9baf38e10b412c8d1bbedfd108e209f33b514053f29b41d148` |
| S35 | `source_audit/standalone_subagents/chaosx_portrait_creator.toml` | 2,049 | 2 | D | `ea2ae603081f64afa82f588bfc143b35f97ee8165f16cf0271784869c55086f8` |
| S36 | `source_audit/standalone_subagents/chaosx_spreadsheet_doc_worker.toml` | 4,605 | 2 | D | `896cb63222484317280d31c340edfc282847774f8edab31a68d7fc2b8b0be33b` |
| S37 | `source_audit/standalone_subagents/chaosx_ai_probability_auditor.toml` | 6,414 | 2 | A | `1c3c202e7f15d310cbe2879f3d6f088e2c2fe71806bb33f13bd276c173d184b2` |
| S38 | `source_audit/standalone_subagents/chaosx_icon_artist.toml` | 10,096 | 2 | D | `df0345a30665c2197b77e5a9df72fd12d545086de3010358077fbe4bf9799f2b` |
| S39 | `source_audit/standalone_subagents/chaosx_improvement_loop_planner.toml` | 7,229 | 2 | L | `c8bcb04ac81e33dac5975c7f3294383f730645b3a3fc3ef26b0c2eb1d79a86b8` |
| S40 | `source_audit/standalone_subagents/chaosx_repo_explorer.toml` | 13,488 | 2 | A | `276acf0305e8b2a1a9c2b6f60cc8153a9e5cd2d629dca85c592e834c9a65fd9a` |
| S41 | `source_audit/standalone_subagents/chaosx_super_event_audio_researcher.toml` | 3,342 | 2 | D | `c0e7e0c422f158e566e2b8fa72de3da225ff626ef3fab06927281b9e33a458c3` |
| S42 | `source_audit/standalone_subagents/chaosx_focus_tree_auditor.toml` | 4,480 | 2 | L | `88149cedcf2de42a2b824635133d083dac4ab9e911de4d91174b727919bb7aac` |
| S43 | `source_audit/current_archive/chaos-redux-improvement-loop.md` | 28,767 | 1 | L | `a875e05d1f4fa31d90ccc126ea61d9e391ee23af333521a818eafddf2eef50b7` |
| S44 | `source_audit/current_archive/chaos-redux-scripted-gui.md` | 28,241 | 1 | A | `e5c724c2e2ccaaeb35a00c77594b1629280bc7727ffb2f391fd65a65fc730d52` |
| S45 | `source_audit/current_archive/chaos-redux-focus-trees.md` | 99,463 | 1 | L | `201b6a026201bfc2e02e5d122a02d2bf3423ed463ec5041becb9d496cf7e4018` |
| S46 | `source_audit/current_archive/chaos-redux-save-inspection.md` | 8,139 | 1 | A | `038224e26040889915458b6aa03039f2f34bd8e4c1e182dbe4ec8a3cded8f01e` |
| S47 | `source_audit/current_archive/chaosx_dynamic_effects.md` | 49,370 | 1 | A | `932a8102cacf420061e8d48fb69ddf9765a536636cfab42abb2c60190c2f3f6d` |
| S48 | `source_audit/current_archive/chaos-redux-native-raids.md` | 4,821 | 1 | A | `601c90faca20b8166496a38153776facf37d5efb0224ad48fd8879de66b7534c` |
| S49 | `source_audit/current_archive/CHAOS_REDUX_MECHANICS.md` | 55,586 | 1 | L | `21f21df8bf621e4362f1e010d342f71df2a939c499bbfce89bc7772790411b56` |
| S50 | `source_audit/current_archive/chaos-redux-debug-playtest.md` | 35,963 | 1 | A | `ea26d70c3239138dce16d3a653e166701a6b7a99fcd0ed06332ad2c5785e626a` |
| S51 | `source_audit/current_archive/chaos-redux-decisions-missions.md` | 77,650 | 1 | L | `60fe85f29ad547b84153f0d7288d8fbef9ce9ca2241a5fc80e0fa0bed3f04ef9` |
| S52 | `source_audit/current_archive/chaos-redux-3d-model-pipeline.md` | 116,242 | 1 | D + A | `e43e2bc6577f0a930480daa7b0a540fc44e1fb45bbd0a3cf12a09bb7898ec098` |
| S53 | `source_audit/current_archive/chaos-redux-frame-animation.md` | 29,504 | 1 | D | `57ab0788652c45c6b21b56d46d96bd5b0e1aa3456d826a6cc42ae89a12e712ab` |
| S54 | `source_audit/current_archive/chaos-redux-state-ledgers.md` | 14,609 | 1 | A | `208c7451f42c7f60fda71f8ed79a604f1469b819f2f17a4769d87016519e1646` |
| S55 | `source_audit/current_archive/chaos_redux_scenarios_catalog.csv` | 18,229 | 1 | A | `95d667fa6c1d5e874b0c51c61efb465b814ae484f6dc48616680238ec85dc5e9` |
| S56 | `source_audit/current_archive/chaos-redux-xlsx.md` | 5,309 | 1 | A | `85db19503086162a59793b3abfff3eb5be4c2d5d66f943c8378c48a3de1f6545` |
| S57 | `source_audit/current_archive/chaosx_dynamic_triggers.md` | 4,746 | 1 | A | `9e6db6f77e0b5fca50ed2b6840664fc5642bacdc754d68c42f0d3c4a5f5fe681` |
| S58 | `source_audit/current_archive/AGENTS.md` | 48,552 | 1 | P,D | `e6375b0aa386e510abd4a35677dccf2871e47f75c9f169e593d52f8c77feff28` |
| S59 | `source_audit/current_archive/chaos-redux-events.md` | 100,605 | 1 | L | `ff298ddaaccd5e1127a3b99c28fab7f138168b0ffa30ec05ef95234ed5251e4e` |
| S60 | `source_audit/current_archive/chaos-redux-event-planning.md` | 200,868 | 1 | P | `f5b30ab6d6ea44d3cadf8eb0220da22ef375e729d275c677ed9832592893866d` |
| S61 | `source_audit/current_archive/chaos_redux_events_catalog.csv` | 63,141 | 1 | A | `f5936e217d2ac67da30b026b9426d0992261e9caf599ef74713ddb1328ef89e1` |
| S62 | `source_audit/current_archive/chaos-redux-mtth.md` | 2,383 | 1 | A | `8a58ec3b838fbc006af98a39f69f77d104e405588490384b81f53ea75bae2160` |
| S63 | `source_audit/current_archive/config.toml` | 12,647 | 1 | A | `8b410f652acd6c6bdfbc985139839ca8b2166f70dc70debc521d6ffe27777012` |
| S64 | `source_audit/current_archive/chaos-redux-event-assets.md` | 117,335 | 1 | D | `1a5c8177c3bfa6eb400d21b03e2d8420c4898ccb5ab34a2b15bcd04c2155a0ef` |
| S65 | `source_audit/current_archive/chaos-redux-super-events.md` | 33,013 | 1 | P | `cb6fd9f8641c9115cc2ab6b357f53d7ef0b21a9348a227e0f1aab1586e5548bd` |
| S66 | `source_audit/current_archive/README.md` | 2,650 | 1 | A | `7fdd0f12bd802cbe6332e5ed218c8573dc215f92560cbb334ae05c204e845435` |
| S67 | `source_audit/current_archive/chaos-redux-shared-git-commit.md` | 6,515 | 1 | A | `100a9ac8745066d2d96cf58aae8758f035a9f91a5ed23bf12c2c701d5e1884ec` |
| S68 | `source_audit/current_archive/chaos_redux_clusters_catalog.csv` | 5,232 | 1 | A | `5c6ff98f080e5e93d96a57dd171dd665574f9372dc53002455e8ad145877f260` |
| S69 | `source_audit/current_archive/chaos-redux-subagents.md` | 55,946 | 1 | P,D | `cc0c5514559ebfd61f7c7855066a00055622e34e2e286c952cd053170b2eac68` |
| S70 | `source_audit/current_archive/subagents/chaosx_localisation_auditor.toml` | 9,782 | 1 | A | `cd66a77792965ec5c435e7b8892847000ff4da0c70816966b047f2f3514c2b9f` |
| S71 | `source_audit/current_archive/subagents/chaosx_event_ui_worker.toml` | 10,134 | 1 | A | `a9f67e17c7ad6aeb31f4a1d7078ad50a2c7dffe52ba5fdc6d704f752aa932ef9` |
| S72 | `source_audit/current_archive/subagents/chaosx_event_completion_auditor.toml` | 4,141 | 1 | A | `277fa8ce183ecb1b586620be058e075860940863121e190b619be18e3eabde66` |
| S73 | `source_audit/current_archive/subagents/chaosx_documentation_curator.toml` | 11,319 | 1 | D | `68aab4a71c00065ae88cff1417e2e2790da79d0c9a1390d132dec93942ffc49d` |
| S74 | `source_audit/current_archive/subagents/chaosx_super_event_text_researcher.toml` | 3,919 | 1 | D | `f75fd8cd6aba92afe806f0687027d7f8a92f1574a07064698548b82c5ed1441a` |
| S75 | `source_audit/current_archive/subagents/chaosx_decision_mission_auditor.toml` | 8,992 | 1 | L | `e70f478705aa61c145e4ed1776d5cedc78acf1b26182809ee3e1e1c557d5cc59` |
| S76 | `source_audit/current_archive/subagents/chaosx_asset_source_researcher.toml` | 3,019 | 1 | D | `02e9522da2f968bb1d1aedf6d5b3ceee13773c19c43a9b72ef1fc96f94ba922b` |
| S77 | `source_audit/current_archive/subagents/chaosx_generated_event_art.toml` | 3,925 | 1 | D | `adaac5d900e1e0b2d3a69c8746b85f0e5585faea7b011acd33bc51eb4ce4e66a` |
| S78 | `source_audit/current_archive/subagents/chaosx_country_package_auditor.toml` | 8,021 | 1 | L | `a6a6a9e003c58af795a217ae8e5cf0096d1ec116b0ec5b3a25871e2526211b44` |
| S79 | `source_audit/current_archive/subagents/chaosx_scripted_system_architect.toml` | 5,388 | 1 | A | `d1f3face145ee254ce6b02d602778311c6183c53a9343df0ff18acc56d294289` |
| S80 | `source_audit/current_archive/subagents/chaosx_3d_model_pipeline.toml` | 28,417 | 1 | D | `89f68c42cc1385f7cfc40c14229462854754fa4d933a7de582002cd901e93b23` |
| S81 | `source_audit/current_archive/subagents/chaosx_skill_maintainer.toml` | 3,258 | 1 | D | `ee8785031aa9924bd0370043297af80c627d853f86bb05caf43527111913aa88` |
| S82 | `source_audit/current_archive/subagents/chaosx_portrait_creator.toml` | 2,509 | 1 | D | `1d8e334d8535bc1f5a4722f0fa7877b641dff51a20e8269e891ae7694daf9145` |
| S83 | `source_audit/current_archive/subagents/chaosx_spreadsheet_doc_worker.toml` | 4,714 | 1 | D | `bbc50a69e8e02cf23117cb9d2e4d2f82f63b525863c8afaa18188449ae415dda` |
| S84 | `source_audit/current_archive/subagents/chaosx_ai_probability_auditor.toml` | 6,412 | 1 | A | `f30e9b61560f9e863013740946ebd53bbb1d4cb2fbb21d5d4903c86ce813acf6` |
| S85 | `source_audit/current_archive/subagents/chaosx_icon_artist.toml` | 10,864 | 1 | D | `2ae3cce3c2fe249a24cc91efcaccdbede8be8cac56bf7f9dd23a3a83657d9574` |
| S86 | `source_audit/current_archive/subagents/chaosx_improvement_loop_planner.toml` | 7,229 | 1 | L | `04b7bdbe8f0e4dc33f8b97d45fc4823a1b4684fe59896c0721297fa21a385fa5` |
| S87 | `source_audit/current_archive/subagents/chaosx_repo_explorer.toml` | 13,486 | 1 | A | `dfaaf09b1ae5d8b98684a6dfcac20bed03d03ae27f5e210abfe7b8659fbedb01` |
| S88 | `source_audit/current_archive/subagents/chaosx_super_event_audio_researcher.toml` | 3,340 | 1 | D | `bf623c4ad7210badfe0f53d175e5c7ef8f73e27639501c4811e07bc12d0c0098` |
| S89 | `source_audit/current_archive/subagents/chaosx_focus_tree_auditor.toml` | 4,478 | 1 | L | `8905303df1fdc2c7ff002c8cfb53abf59e87259cef574c6935d4d85b36682847` |
