# SCN015 duplicate native ID forensic handoff

Disposition: `unresolved` for root cause and object type, with completed bounded source research.
Authority: parent requested read-only forensic research and this single report write, with no gameplay edits or Git operations.
The parent owns implementation, verification, and commit.
The supplied live observation is fresh 1936 USA, Missile Age SCN015, Medium, Global Proliferation, launched from Triggerable Scenarios, with `[id.cpp:104] Failed to create id 1028 4713 Already exists in game might crash` within less than one day.
No game or desktop was launched, no debug-playtest was used, no logs were searched or requested, and no save was supplied or inspected.
Other agents' files and index were preserved.
The parent is separately repairing COUNTRY-only `exists` in STATE scopes and undefined global-target clears, so neither repair was duplicated here.
Event 032 remains incomplete, and this report does not supersede that status.
The parent supplied `72c748ac` as the ordinary-preparation repair and `a2761ef8` as a validation checkpoint, but the current live QA supersedes prior assumptions that STATE `exists` was valid.
No Git command was used to inspect or alter those commits.

## Findings and confidence

The exact setup path reaches native rocket-site construction and technology grants, but the inspected scripts do not provide a fixed native object ID or establish the object class of `1028`.
No explicit `create_unit`, `division_template`, `create_equipment_variant`, generated-character, dynamic-country, army/navy-leader creation, or OOB-loading command was found in the Event 032 scripted-effect files.
The immediate Global Proliferation setup closure contains no such creation command.
The shared scenario file does contain unrelated dynamic-country and OOB creation in zombie and clone helpers, but its mutually exclusive SCN015 dispatcher branch does not call those helpers.
The findings below establish source reachability rather than execution of a particular native allocator.

1. **Proven physical creation path:** `trigger_selected_chaosx_scenario` -> SCN015 dispatch -> `missiles_scenario_launch_unregistered` -> selected-recipient `chaosx.nr32.6` -> `missiles_scenario_apply_country_package` -> `missiles_initialize_or_advance_program` -> `missiles_initialize_scenario_package` -> `missiles_create_primary_site` -> `missiles_register_site` -> `add_building_construction = { type = rocket_site level = 1 instant_build = yes }`.
2. **Proven technology grant path:** the same scenario initializer applies `experimental_rockets` and `rocket_engines` when its stage is at least Guided.
It also applies the later engine technologies when the recipient already has a sufficiently high program stage, since setup only raises the stage and does not lower it.
3. **No proven duplicate native allocation:** the native building call has no `id` argument, and the technology grants have no supplied object ID.
`missiles_site_operation_id`, owner/controller IDs, program generations, and setup receipts are stored script variables, not native object-creation IDs.
4. **Existing same-transaction repeat guard:** `.6` checks selected-array membership and requires an absent or older country setup receipt.
The package writes the current receipt before its nested setup calls.
The selected roster suppresses duplicate entries, and the commit loop visits that frozen roster once.
An immediate duplicate `.6` delivery with the same receipt should therefore skip the package according to source conditions, subject to actual engine execution.
5. **Existing physical-site guard:** `missiles_create_primary_site` requires absence of `missiles_primary_site_established`.
Registration requires matching ownership/control, no scuttled flag, and no active flag.
If `rocket_site` is already above zero, registration adopts the building instead of constructing another level.
6. **Dynamic modifiers are not accumulated by this helper:** refresh removes all five site modifiers and then adds at most one branch result.
Installed documentation explicitly says adding an existing dynamic modifier updates its cooldown.
This does not prove which native object type backs modifiers, but it provides no evidence of a fixed-ID collision in repeated modifier application.
7. **No evidence-based numeric ID mapping:** MCP reference search for `1028` returned zero sections.
The pertinent installed documentation and bounded local source/mapping searches yielded no type registry connecting `1028` with a division, wing, equipment variant, character, building, or other class.
Installed console documentation exposes an object ID and optional object-type ID for `select`, but contains no mapping table here and says that command is unavailable in release builds.
The two reported numbers must remain uninterpreted.

## Exact call closure and branch exclusions

Paths in this section are relative to `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

| Surface | Exact source | Scope, input, output, and side effects |
| --- | --- | --- |
| Shared launch | `common\scripted_effects\chaosx_triggerable_scenarios_effects.txt:1105-1112,1265-1274,1305-1311` | COUNTRY launch scope initializes settings, copies selected scenario into temporary launch ID, preserves/restores the event timer, and dispatches only the Missile Age branch for ID 15. |
| Roster and commit | `common\scripted_effects\032_missiles_scenario_effects.txt:289-407,698-783` | COUNTRY origin loads profile/intensity globals, freezes eligible countries once, selects unique recipients, preflights, increments setup receipt, sends immediate `.6` to each selected country, then clears transaction storage. |
| Receiver | `events\032_missile_crisis.txt:30-49` | COUNTRY recipient provides ROOT to site helpers, checks transaction flags, country existence, membership, and receipt before calling the package. |
| Country adapter | `common\scripted_effects\032_missiles_scenario_effects.txt:593-652` | COUNTRY recipient writes bypass/origin flags, receipt and nine persistent transaction inputs, calls normal program entry and normalization, validates active-site result, then clears inputs and bypass. |
| Shared program entry | `common\scripted_effects\032_missiles_effects.txt:320-388` | COUNTRY recipient initializes variables and achievements, selects scenario initializer while bypass is set, clamps values, assigns AI profile, optionally applies mature package, refreshes one status idea, and stores firing receipt. |
| Scenario initializer | `common\scripted_effects\032_missiles_operations_effects.txt:623-723` | COUNTRY ROOT receives stage/reserve/readiness/control inputs, grants native technologies, creates/adopts primary site, adjusts script site level/capacity, refreshes site modifier, recalculates network/custody, and records failure if no active site. |
| Technology normalization | `common\scripted_effects\032_missiles_effects.txt:394-408` | COUNTRY recipient reads `has_tech`, computes normalized stage, and only raises the program stage. It creates no native object explicitly. |
| Site creation/adoption | `common\scripted_effects\032_missiles_effects.txt:728-813` | STATE site with recipient ROOT writes flags, variables and owner IDs, adopts an existing native rocket site or constructs one instant level, adds the state to recipient array, and marks primary established. |
| Site presentation | `common\scripted_effects\032_missiles_effects.txt:863-935` | STATE refresh removes the modifier family and chooses rogue, damaged, compromised, hardened, or active state. |
| Baseline reserve | `common\scripted_effects\032_missiles_effects.txt:473-544` | COUNTRY reserve helpers calculate script numbers and change reserve variables, with no stockpile equipment creation. The ordinary first-package caller at lines 335-350 is excluded by scenario bypass. |
| Event 16 reaction | `common\scripted_effects\016_brilliant_scientist_context_effects.txt:424-448` | COUNTRY host reaction uses country and existing Kruger character receipt flags, adjusts six variables, and refreshes idea lifecycle through `016_brilliant_scientist_effects.txt:530-564,569-614,619-697`. It contains no generated character or unit creation. |

The ordinary initial package at `032_missiles_effects.txt:335-350` is the `else` of the scenario-bypass branch.
Its technology-step, first-reserve, primary-site and Event 16 reaction calls do not run alongside the scenario initializer during a normal SCN015 recipient commit.
The human `.2` report is likewise suppressed by the bypass condition at lines 380-385, so its Event 16 option reaction is not an immediate SCN015 consequence.
The package's Global Proliferation profile does not satisfy the Saturation, Command Breakdown, Special Payload Crisis, or Retaliation Network branches.
Consequently evolution unlock recording, command incident seeding, payload integration, and retaliation-warning seeding in those profile branches do not run for the specified launch.
At Medium, the target stage is 2, the recipient share is 0.35, and the script site level target is 2 (`common\script_constants\032_missiles_scenario_constants.txt:53,58,72`).
Stage Guided is 2 (`common\script_constants\032_missiles_constants.txt:70`).
For a recipient with no higher pre-existing stage, only the first two native technology grants execute and the mature package is excluded.
Scenario site-level adjustment changes Event 032 variables, not the physical building through another construction call.
Global Proliferation does not directly schedule a missile operation or launch in this setup closure.
Ordinary later campaign behavior and unrelated callbacks are not proven absent by this bounded trace.

## Native unlock and creation evidence

Effective `experimental_rockets` at `common\technologies\electronic_mechanical_engineering.txt:1280-1341` unlocks the native rocket-site building to level 3.
Its `on_research_complete` body at lines 1308-1331 contains custom tooltips, with no explicit object-creation effect.
Effective `rocket_engines` at lines 1343-1400 unlocks `rocket_engine_1` and conditionally enables `rocket_interceptor_equipment_1` without By Blood Alone.
The guided-missile equipment entry is commented out.
Later `improved_rocket_engines` and `advanced_rocket_engines` at lines 1530-1625 follow their engine-module and conditional interceptor-equipment patterns.
MCP source lookup confirms the same-relative-path installed vanilla technology file is shadowed by the mod file, rather than proving two simultaneously effective `rocket_engines` definitions.
No additional duplicate-technology cause was established.

The parent's follow-up specifically requested grant-time variant evidence, so the four mod and installed vanilla technology bodies were compared by their actual unlock and callback content.

| Technology | Mod lines | Installed vanilla lines | Native unlocks and callbacks |
| --- | --- | --- | --- |
| `experimental_rockets` | 1280-1341 | 1261-1322 | `rocket_site` level 3, with only custom tooltips in completion callback. No explicit variant ID or creation. |
| `rocket_engines` | 1343-1400 | 1324-1381 | `rocket_engine_1`, conditional `rocket_interceptor_equipment_1` without By Blood Alone, guided-missile equipment commented out, no completion callback. |
| `improved_rocket_engines` | 1530-1583 | 1511-1564 | `rocket_engine_2`, conditional `rocket_interceptor_equipment_2` without By Blood Alone, guided-missile equipment commented out, artillery modifiers, no completion callback. |
| `advanced_rocket_engines` | 1585-1632 | 1566-1613 | `rocket_engine_3` and `guided_anti_ship_missile`, conditional `rocket_interceptor_equipment_3` without By Blood Alone, guided-missile equipment commented out, artillery modifiers, no completion callback. |

Installed `documentation\effects_documentation.md:3069-3099`, read through MCP, documents a concrete indirect variant mechanism.
For `create_equipment_variant`, `allow_without_tech` defaults to no and the variant is created once the equipment type's research completes.
It also says a missing parent version uses or creates the default variant.
Installed `common\units\equipment\_documentation.md:105-111` documents `default_modules` as the modules of the default equipment variant, but does not describe its runtime allocator or ID type.
These are evidence that grant-time variant creation can exist in the engine, rather than proof that the four missile grants collide.
A bounded exact search for `type = rocket_interceptor_equipment_1/2/3` in mod history/scripted effects and installed vanilla country history/scripted effects returned no creation blocks.
The installed USA country-history file contained no rocket-interceptor or missile technology match.
Installed interceptor equipment definitions in `common\units\equipment\x_plane_airframes.txt:1042-1120` contain archetype, parent, stats and upgrades, with no fixed native numeric IDs in those inspected definitions.
The first two definitions are at 1042 and 1079, and the third begins at 1106.
The active DLC set was not supplied, so the conditional interceptor-equipment unlock must not be assumed active.
No concrete deferred rocket-interceptor variant or script callback was established as a collision source.
Default/native variant allocation remains an engine-side candidate alongside instant building activation.

Installed `common\buildings\00_buildings.txt:338-354` declares `rocket_site` with `rocket_production = 0`, `rocket_launch_capacity = 1`, `spawn_point = rocket_site_spawn`, and state max 3.
No mod rocket-site building declaration was found in the inspected mod building files.
This definition proves a native launch-capacity building consumer, but does not document an automatic wing creation, native runtime type ID, or allocator behavior.
An implicit wing/equipment allocation through building or technology activation remains a hypothesis, not a finding.

## Minimal parent recommendation

Preserve all accepted scenario content and both native technology and site outputs.
There is no proven allocator-level fix from the supplied evidence.
The narrow content-preserving hardening candidate is to add `NOT = { has_tech = <technology> }` to each of the four existing stage-gated grants in `missiles_initialize_scenario_package` and use `popup = no` consistently.
This avoids unnecessary reapplication to recipients who already own a technology while retaining grants to recipients who need it.
The repository's existing `union_compatible_researched_technologies_from_donor` already uses this missing-tech guard (`common\scripted_effects\chaosx_dynamic_effects.txt:483-527`, documented in its matching Markdown at lines 196-208).
No new generic helper is needed for four local guarded calls.
This recommendation is not a confirmed resolution of the fresh first-launch collision, since a recipient with no technology would still legitimately receive the same grant.
`popup = no` affects presentation and is not an ID fix.
Keep the existing receipt and native-building-presence guards, and do not add a guessed fixed-ID rewrite, remove rocket-site construction, or replace accepted native unlocks with script-only substitutes.
Object-class identification and attribution to technology activation versus instant rocket-site construction remain the concrete missing evidence for a root-cause fix.

No new helper, constants/tuning table, event target, cleanup hook, migration, gameplay restriction, or content deletion is proposed here.
The helper map above documents the existing local architecture.
Parent-owned STATE predicate and global-target-clear repairs remain separate.

## MCP evidence and limitations

Connected workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Reference/source routes were exposed and live calls succeeded.
An initial nonexistent lookup for `missiles_scenario_launch` returned zero definitions, then corrected exact-symbol lookups succeeded.
Two event selector validation errors were corrected using the observed schema `selector = { kind: "event", eventId: "chaosx.nr32.6" }`.
No helper-expansion or native-task route was used because connected server health/version and client negotiation were not established.
No timeout of 600 seconds occurred.

- Exact `.6` source lookup returned one non-shadowed mod event at lines 30-49, revision `80d2735f5c6a7eabf23a4bb44ff22e8965ab6728e51b15584a0341535f584797`.
- Exact scenario initializer and registration lookups returned the expected helper definitions under that same revision, with bounded text continuations.
The underlying files were read directly for the rest of their blocks.
- Event trace returned `EVENT_INSPECTED_PARTIAL`, `analysisMode = focused`, helpers 0, and revision `f2b8bdff77c9db689497266f8e35cb0795c11751b02e0188f6533efbece85fd5`.
The refreshed narrow trace retained the same revision and focused lifecycle boundary.
Its refreshed artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6b7ce6ddf77fe969d3a8a803b07fc055b035803af872235437cc17cc5246d74/ceb30e1fd20acf10ca4feafd0e6d4480e7dcf4491172b87031e95fffd7f9456a/event-trace-f2b8bdff77c9.json`.
- Event scope render returned `EVENT_RENDERED_PARTIAL` with selected nodes 0, helpers 0, omitted nodes 43002, and the same event revision despite exact source lookup finding `.6`.
This is a graph-selection coverage gap, and the render is not proof of this setup closure.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17ece2baa0d9eb95e83aa6773d679c4ca7d6c82fe9ba28ef1262e3019918187d/ab2ec96fb854f56f5f22c8b8f5bb590f0344fc5fd10cc0c9952064dc2735289a/event-scope-f2b8bdff77c9.json`.
Reading it failed with exact blocker `Mcp error: -32603: Artifact provenance manifest is unavailable`.
- Technology unlock inspection for `rocket_engines` returned `TECH_INSPECTED_PARTIAL`, revision `a9c612207a9d9347ba875f4c7559b2703a84d982ef6a15c2465fd9f08aa132b2`, unresolved count 3, with validation false because helper projections were deferred.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6f5921a50b3830e567115a835fe96984fddbfe430b8aa7c5b2cbf8f4253967c/acb80bf2b606d7da4ffe7d883cf81505fd1585e9b6d965b907f50177aecaa2b9/technology-unlocks-a9c612207a9d.json`.
Reading this artifact failed with the same unavailable-provenance-manifest blocker.
Its summary is not complete unlock or native-creation evidence.
- `chaosx_ai_probability_auditor` was spawned isolated and read-only for the deterministic setup selectors.
Both `hoi4.probability_inspect` calls returned `PROBABILITY_SOURCE_DISCOVERED`, zero available adapters, zero candidates, and `discoveryReason = no_weighted_surfaces`.
They supply no probability evidence for deterministic selection or duplicate native IDs.
Revision: `9e4f93a57369d37acfcc82eebba4c7de8dd3f2530ce149aca6b5bc856ca00d13`.
Artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca88c0fe559f1015dd4e70efc7b0f3f8f3dbceabeb6f5c9e551bd94ac309f1a6/9e5e618a38539fc9c6209990afe7189529016a5d84a51024b6c93fc490c135c5/probability-inspect-ad97026ac551.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0db583cc7388b5ef0b19a6be7b45b963ebd30f3f784a58a117cb787509dee680/05d5396917eaeb654edbdcfcb70b880da5d56cd52257ac8269f73fd1b156073e/probability-inspect-d1c05749725c.json`.
The auditor reported tool source hashes `ad97026ac551ae8e321218c18ce3119ee32a9cc3bb4e834ce1b49e8552e281d0` and `d1c05749725c240435cbc45e372ac72b20ea6bd46935b1a1e008fb2f0437c1d0`, which differ from local raw-byte hashes below.
That identity difference is retained unresolved and is not assumed to be engine or current-file equivalence.

The context call omitted Triggers, Scopes, On actions, and Localisation because of its limit.
Only task-relevant detailed references are claimed below, including targeted installed trigger reads and direct scope/event-target reads.
No claim of complete context-bundle coverage is made.
No GUI layout, focus, or map rewrite/design was performed.
Technology rendering/comparison and event comparison were not used for a proposed source change because this task changes no engine-facing source.
Runtime allocation behavior, live callback timing, and `.6` graph helper coverage remain unvalidated.

## References actually read

The installed root is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
The offline wiki root is `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki`.
SHA-256 values refer to whole raw files, and line spans refer to the read section.

| Reference | Lines | SHA-256 | Relevant evidence |
| --- | --- | --- | --- |
| Installed `documentation\effects_documentation.md` | 839-847,1153-1173,2943-2962,6496-6512,7805-7819 | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` | STATE building construction, dynamic-modifier cooldown update, COUNTRY event delivery and technology grant, pointer storage. Detailed building/modifier/technology/target reads used MCP. |
| Installed `documentation\triggers_documentation.md` | 4882-4890 | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` | `has_tech` is a COUNTRY predicate. MCP search/read and direct section read. |
| Installed `documentation\console_commands_documentation.md` | 1497-1502 | `B65548C92B318F84F2185BE790A3E0F2BCE331EA646E233BF2EA85114BF8215D` | Object and object-type parameters exist, but no `1028` mapping and command unavailable in release build. |
| Offline `Effects - Hearts of Iron 4 Wiki.md` | 1928-1970 | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` | Technology effect semantics, read through revision-bound MCP. |
| Offline `Technology modding - Hearts of Iron 4 Wiki.md` | 125-171 | `C5428838DB20C4C812C66AFF82CBAFC58DB3B73453C30436BCE0D97436170BEE` | Completion effects execute for effect-granted technologies, equipment/module/building unlock meaning, building level semantics. Enabling section read through MCP and completion section directly. |
| Offline `Data structures - Hearts of Iron 4 Wiki.md` | 263-307 | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` | Event targets store scope pointers and regular targets carry into fired events. Direct relevant section read. |
| Offline `Scopes - Hearts of Iron 4 Wiki.md` | 250-267 | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` | Event recipient ROOT, containing PREV, STATE and COUNTRY dual scopes. Direct relevant section read. |
| Installed `common\technologies\electronic_mechanical_engineering.txt` | 1324-1381 | `7F2A02CC871AC944657AD2B127C70F3E30ECBE639606700FFC9D4385F76739FF` | Exact vanilla rocket-engine precedent read through source lookup, reported shadowed by mod. |
| Installed `common\buildings\00_buildings.txt` | 338-354 | `9FA27D266F726DE04C71311551698C6466257636DCC34D2573A3568D397BD539` | Exact native rocket-site building definition. |
| Installed `events\Germany.txt` | 1841-1870 | `33FE28FC94AA16DB13FF51AE7B2AA897B13790FBF267D2DB7EF567010A5799D0` | Native STATE-scoped construction precedent in `germany.27`, not a rocket-site allocator or duplicate-ID precedent. |
| Installed `common\units\equipment\_documentation.md` | 105-113 | `FE7A672ABE4BE6EF0191C566B81C41D01EFFE7A45AB8D786A914FDB89C5400C9` | Default equipment-variant module schema, without allocator timing or numeric object-type mapping. |
| Installed `common\units\equipment\x_plane_airframes.txt` | 1042-1120 | `0747E1A834D4C44EEEE593BC0D5CBD7F636BE6F34BE89BE53B19F83AFCD08F8A` | Native interceptor equipment archetype/parent/stat definitions, no fixed numeric IDs in inspected blocks. |

## Local source identities

These hashes were checked twice and the four principal call-closure files retained identical raw bytes during this research.
They do not imply the shared worktree was otherwise unchanged or that cached MCP domain graphs used these bytes.

| Mod-relative file | Raw SHA-256 |
| --- | --- |
| `common\scripted_effects\032_missiles_scenario_effects.txt` | `AD525A7412A6C8A026ABEB99CF03B3FAA68CA64DF7B911CDE9ACA039B0649270` |
| `common\scripted_effects\032_missiles_effects.txt` | `FA3D682945BF0D038D2890C62E334F3785E01AB7D2295F545274D74E350F3D19` |
| `common\scripted_effects\032_missiles_operations_effects.txt` | `D41B59EDCFD29B015F566914FDDCF88D2BD7469224BE635D22B5E2B967C8A8F1` |
| `events\032_missile_crisis.txt` | `B088E3245E1CE7858037F3A697045286F83A2E41DBDDF69102DD18152A6F23AB` |
| `common\scripted_effects\chaosx_triggerable_scenarios_effects.txt` | `3F183E17A7F4EAB2A98DB5D55CACA7519A133B4158E0CCF46562F5E188343C2C` |
| `common\scripted_effects\016_brilliant_scientist_context_effects.txt` | `C76E351AA366BE60E69472E007B56312C2C18642AAB4B96F8F9AC63819C2B80A` |
| `common\technologies\electronic_mechanical_engineering.txt` | `D279418B92D31511AB24E190CA3BD1FEA8E8387101FB4019F0DC1691314EA7E9` |
| `common\dynamic_modifiers\032_missiles_state_modifiers.txt` | `D33DCC774EDD34359AC7680BE27823C25B12C501C214D6B60FF5E02E6F28B312` |
| `common\script_constants\032_missiles_scenario_constants.txt` | `0B455DDC643547FBAC0DFB634CE24B8B58F97CAF349C2A618619F9718C9835A2` |
| `common\script_constants\032_missiles_constants.txt` | `77BEB588E0B8CEDF8E45459F4790A58234B6EA67C5286C5037C0C7396A80DDEE` |

## Completed work, skipped validation, and handoff boundary

Completed: bounded source closure, creation-command inventory, explicit native-ID argument search, branch exclusion of unrelated scenario constructors, Event 16 reaction review, effective native technology precedent, building definition, modifier refresh behavior, reference/source MCP calls, focused event inspect/render attempts, narrow technology inspect, and probability specialist evidence pass.
Files changed: only this report.
Helper documentation changed: none.
Call sites, constants, cleanup logic, localisation, assets, and gameplay behavior changed: none.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or updated within this restricted write scope.
No gameplay simplification or accepted-content removal was made.

Skipped meaningful validation: no runtime reproduction or allocator inspection because this read-only sidecar has no game-launch authority and no supplied save or native ID registry.
No engine-body validation was run on a patch because no script patch exists.
No probability scenario, sweep, or comparison was run because the auditor found no supported candidate surface for this question.
Source-only evidence was not substituted for missing lifecycle, render artifact, or native allocation evidence.
The immediate next parent decision is whether to apply the guarded technology hardening while keeping duplicate-ID attribution explicitly unresolved.
The duplicate-ID error itself remains unresolved, and full Event 032 completion is not claimed.
