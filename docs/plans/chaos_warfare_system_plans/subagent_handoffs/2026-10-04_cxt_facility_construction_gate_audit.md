# CXT Facility Construction Gate Audit — 2026-10-04

Disposition: `unresolved` for the runtime cause. The source already grants technology before facility provisioning and checks candidate construction after transferring the state to CXT, but source inspection cannot establish why the live native trigger returned false for the reported candidates.

## Scope and liveQA evidence

This is a read-only diagnostic of CXT setup for `land_facility` and `biowarfare_facility`. No gameplay source was changed, no game was launched, and no logs or saves were requested or inspected.

The parent supplied this liveQA observation: CXT searched 25 foreign states for each facility type, `can_construct_building` returned false for every tested candidate, and CXT finished without either building. This is runtime evidence reported by the parent; I did not independently observe it.

## Source findings

`events\chaosx_test_country.txt:11-18,57-67` registers a triggered receiver whose trigger requires `tag = CXT`, then calls `chaosx_test_country_initial_setup` from that country scope after its capital gate. The event and setup source therefore establish `ROOT = CXT` for the intended setup path.

`common\scripted_effects\chaosx_test_country_effects.txt:401-418` grants all technologies, completes registered special projects, grants technologies again, and only then calls `chaosx_test_country_build_special_facilities`. The facility order at lines 213-227 is naval, nuclear, air, land, biological, then chemical.

`common\scripted_effects\chaosx_test_country_effects.txt:70-95` first checks whether any currently owned CXT state meets the shared facility requirements and passes native `can_construct_building`. If not, lines 96-121 select an eligible foreign state and save its original owner and controller. Lines 126-137 transfer the state to `ROOT`, set its controller to `ROOT`, then test the shared requirements and native construction trigger. There is no native construction check against the foreign owner before transfer. Lines 141-156 restore both owner and controller when the post-transfer test fails. On success, lines 174-188 select an owned, controlled, eligible state, repeat the native trigger, and invoke `construct_building_in_random_province` for one level.

`common\scripted_triggers\chaosx_test_country_triggers.txt:10-37` requires the state to be owned by `ROOT`, coastal only for `naval_facility`, and free of the six recognized CXT facility types. The search additionally excludes capitals, impassable states, demilitarized zones, and candidates without valid owner/controller scopes.

The reported 25 attempts match the configured bound. `common\script_constants\chaosx_test_country_constants.txt:25-36` sets `facility_search_max_candidates = 24`; the helper initializes attempts to zero and increments after each candidate, stopping only when attempts are greater than 24 (`common\scripted_effects\chaosx_test_country_effects.txt:80-81,163-168`). This bounds attempts and does not explain the native false result.

## Native gates reviewed

The installed trigger documentation defines `can_construct_building` as a STATE-scope trigger that checks whether the country in `ROOT` and the state in scope can build the specified building. The offline Triggers page gives the same scope rule. References: installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:1920-1934`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`; offline `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md:1870-1885`, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`.

The installed vanilla definition `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\buildings\00_buildings.txt:556-577` defines `land_facility` with `disabled_in_dmz = yes`, one level per province and state, and `group_by = special_project_facility`; it does not declare `dlc_allowed` or `is_buildable = no`. The mod definition `common\buildings\chaosx_buildings.txt:38-72` gives `biowarfare_facility` the same DMZ and one-level shared-group limits and likewise has no explicit DLC gate or `is_buildable = no`.

The offline Building modding section documents `dlc_allowed` as the building-level DLC restriction and says `is_buildable` defaults to yes; it defines `group_by` as a shared maximum across buildings in that group. References: `paradox_wiki\Building modding - Hearts of Iron 4 Wiki.md:111-134` and `:53-83`, revision `1e5fb5410a26af12b5b791b193f8f602c4ef8a3614ed897ae4c67084477f7bfc`.

The offline Technology modding section says a building with no technology assigned to unlock it remains selectable, while `enable_building` gates construction up to a declared level. A targeted search of the mod and installed vanilla `common\technologies` directories found no `land_facility` or `biowarfare_facility` reference, and the technology unlock inspection selected zero nodes for each target. References: `paradox_wiki\Technology modding - Hearts of Iron 4 Wiki.md:146-171`, revision `c5428838db20c4c812c66aff82cbafc58db3b73453c30436bce0d97436170bee`; MCP source inventory revision `4f4d31903525889ae8d14506edef73ec68c064455efc0deae11b45de486dfe1` for the mod and game definitions.

These findings rule out an explicit `dlc_allowed` or `enable_building` gate in the inspected definitions and technology files. They do not establish which DLC the live session has enabled, nor do they prove the runtime trigger result. No DLC absence is asserted as the cause.

Both facilities share the `special_project_facility` group cap. One additional group member is `anomaly_signal_beacon_pilot`, defined as non-buildable but with the same group in `common\buildings\chaosx_3d_model_pilots.txt:6-34`; the showcase places it in Brandenburg state 64, province 9560 (`common\scripted_effects\chaosx_3d_model_pilot_showcase_effects.txt:6-19`). The CXT helper does not include this pilot id in its six-facility prefilter. If Brandenburg is selected, the native level/group limit can reject that candidate. The rejected-state array prevents selecting that same state repeatedly, so this single building cannot explain 25 failed states.

## Technology loop size

`common\scripted_effects\chaosx_test_country_technology_effects.txt:5-35` captures `global.technology^num`, starts at `@CXT_FIRST_TECHNOLOGY_INDEX = 1`, and ends before the captured count. The source comments that index zero is a reserved invalid object. The installed-game plus mod technology inventory reported 688 technology definitions at graph revision `ef58ca3ed9b1e1c784cba694a20dc8c0695ec783ac1701da93820bf148a15379`, graph hash `ac386cdc78f0e6011c5215dbc9721d7c07199716876b74a61535482361f034a3`. This implies 688 real entries after the reserved slot, below the wiki's 1,000 loop-effect iteration cap. The count is from the indexed source graph, not a live read of the runtime array or proof that each `set_technology` effect executed.

The offline Data structures/Defines search returned `MAX_EFFECT_ITERATION = 1000` for loop effects; source: `paradox_wiki\Defines - Hearts of Iron 4 Wiki.md:65-92`, revision `61ae03fd36bcbe2ab6ca1304b013d3f432b88e6592856fffdd2685f792e87fcc`.

## MCP and viewer evidence

The connected `hoi4_agent_tools` exposes `hoi4_reference_context`, `hoi4_reference_search`, `hoi4_reference_read`, `hoi4_source_lookup`, `hoi4_tech_inspect`, `hoi4_tech_render`, and `hoi4_tech_compare`. The technology inspect and render calls returned live `status = ok` responses for workspace `mod_chaos_redux_ea3b2d67c2c0`. Inspect reported `TECH_INSPECTED_PARTIAL` because whole-workspace helper projections were deferred; render reported `TECH_RENDERED_PARTIAL`, zero selected nodes, and `sourceAccurate = false` for the requested unlock view. The report artifact reads failed with the exact route error `Artifact provenance manifest is unavailable`, so those reports remain unresolved and are not treated as definitive proof of absent unlocks. Inspect report URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d4ee2707d1b66bb546db1579cfc33a8385c9106bb3fcf4c5d04fe52d59a321b/c606ce0cef8263b9a19c0774d46af20b44b862e34083cccbf04e233a60e7b472/technology-unlocks-ef58ca3ed9b1.json`.

The installed package at `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools` is version `3.6.0`. Its `docs\technology.md` describes the Technology Tree Viewer as the MCP graph and static-report workflow; its HTTP transport exposes `/mcp` and OAuth metadata routes, with no separate viewer UI route. A process, Start menu, and uninstall-registration search found no independent Technology Tree Viewer application. A separate standalone UI was therefore not found in the checked package or Windows app inventory; the exposed MCP routes remain available. The connected process does not expose a distinct version/health route; live domain calls returned `status = ok`.

## Runtime diagnosis and handoff

No narrow source fix is proven. The current source already grants technologies before facility provisioning and evaluates `can_construct_building` after transfer to CXT. Do not bypass the native building gate or assume missing DLC is responsible.

The parent added a temporary diagnostic immediately after transfer, guarded by the existing `chaosx_test_country_setup_trace_active` flag, to record the ROOT actor, current owner/controller, Gotterdammerung check, shared-precondition result, and native `can_construct_building` result for the active facility token. The parent owns that source edit and must remove the temporary diagnostic after the runtime cause is resolved. This read-only handoff does not create or alter it; the installed source is common/scripted_effects/chaosx_test_country_facility_diagnostics.txt with one guarded post-transfer caller.

The helper is published so that the caller already committed in `eb08e1dde` resolves in every checkout; without it a checkout logs an unknown effect and the trace silently does nothing. It stays read-only, runs only under the explicit setup-trace flag, and changes no construction, transfer, retry bound, ownership, technology or cost. Remove the helper file and its single caller together in one change once the native rejection is identified.

The decisive unresolved values are whether the transferred state is actually owned and controlled by CXT at the check, whether the live DLC check is true, and whether the shared group/level or another native condition makes the building unavailable. The currently available userQA summary does not distinguish these branches. No logs or saves are requested by this report.

## Supply requirement and the placement change (parent, 2026-10-04)

`need_supply = yes` is declared by every special-project facility: vanilla `land_facility` at installed `common/buildings/00_buildings.txt:556-577`, and the mod's `biowarfare_facility` at `common/buildings/chaosx_buildings.txt:38-72`, together with `naval_facility`, `nuclear_facility`, `air_facility` and `cw_facility`.
The installed special-project facility documentation requires a supply-connected province before construction can start, and the state-scope `can_construct_building` trigger evaluates the country in `ROOT` against the state in scope, so an unsupplied state fails that gate.
A randomly selected foreign state that touches no CXT-controlled territory can never join CXT's supply network after the temporary transfer, which is consistent with every tested candidate returning false.

The parent therefore made two bounded source changes.
The foreign candidate filter now also requires `any_neighbor_state = { is_controlled_by = ROOT }`, so a borrowed state can actually join the network.
The construction pass now tries a supply-connected owned state first, through the new `chaosx_test_country_state_is_supply_connected` state trigger (capital, supply node or railway), and only then falls back to any owned state that passes the native gate; `construct_building_in_random_province` picks an arbitrary province in the state, so the preference matters.
No gate is bypassed, the native trigger remains the decider, the retry bound is unchanged, and rejected temporary transfers still restore both owner and controller.
The temporary trace now also records `supply_connected` and `adjacent_to_actor` for each tested candidate, so the orchestrator's run shows which branch the rejection belongs to.

One limitation stays open and can only be settled in a live session: the facility phase runs inside the same effect chain as the annexation, so the engine's supply network may not yet include the newly acquired states at the moment the gate is evaluated.
If the trace reports owned, adjacent and supply-connected candidates that still return `native_can_construct=no`, the next change is to move the facility phase to a later tick rather than to weaken the gate.
`docs/testing/chaosx_test_country.md` currently carries another owner's uncommitted Event 029 paragraph plus a whole-file line-ending rewrite, so the harness documentation update is recorded here instead of editing that file.

## Work and validation record

Only this audit handoff is written. No tags, states, leaders, parties, focus ids, localisation keys, formables, or gameplay files changed. No map operation or in-game validation was performed. The source lookups, targeted technology search, building definition review, reference searches/reads, and live read-only technology inspect/render calls are the meaningful checks for this bounded diagnostic.
