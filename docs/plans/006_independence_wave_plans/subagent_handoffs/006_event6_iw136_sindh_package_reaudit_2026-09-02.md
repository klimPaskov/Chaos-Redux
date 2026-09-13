# Event 006 IW-136 Sindh package re-audit — 2026-09-02

## Status

`BLOCKED / FAIL-CLOSED — audit only; no gameplay, asset, central-admission, or map files changed.`

No source-safe, non-generic IW-136 tranche is implementable from the current evidence. The registered `SIN` carrier and the generic `iw_136` planner wrappers are not a country package, and adding readiness, adapter, attestation, or Join logic would bypass the unresolved identity, rights, provenance, package, probability, and host/map gates.

## Scope and authority

This audit is limited to IW-136 Sindh (`SIN`), accepted anchor state `443`, reservation group `RG-443`, package ID `iw_136`, South Asia and Himalaya region, and the accepted compact lower-Indus package contract.

The accepted row is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:137`.

The identity and provenance resolution is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:137`.

The state reservation contract is `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:37`.

The accepted force contract is `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:137`.

The current installed binding is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:137`.

The current authority remains the Event 006 HOLD/PARTIAL baseline: 32 content-attested packages, 29 reservation groups, 40 runtime adapters, and 161 unattested selectable rows. IW-136 remains unattested and must not be promoted by this audit.

Required offline Paradox wiki pages were consulted before source review, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus modding, Portrait modding, Graphical asset modding, State modding, Map modding, Supply areas, and Strategic region.

Relevant vanilla documentation was consulted before source review, including `script_concept_documentation.md`, `triggers_documentation.md`, `effects_documentation.md`, `loc_objects_documentation.md`, and `modifiers_documentation.md` under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

The country package, events, focus trees, decisions, assets, and probability skills were applied for this audit. Character portrait production remains owned by `chaosx_portrait_creator`; no portrait request was made because the identity gate is unresolved.

## Country package coverage checklist

| Surface | Result | Concrete evidence |
| --- | --- | --- |
| Tag registration and ownership | Partial baseline only | Vanilla `common/country_tags/00_countries.txt:334` registers `SIN = "countries/Sindh.txt"`; current mod `common/country_tags/006_independence_wave_countries.txt` has no `SIN`. |
| Country definition | Vanilla-only | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/countries/Sindh.txt` contains only graphical cultures and color; no mod SIN definition or Event 006 package shell exists. |
| Country history and capital | Vanilla-only | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/SIN - Sindh.txt` sets capital `443`, research slots, technologies, and politics; no mod SIN history or package setup exists. |
| State ownership and host | Planning baseline only | Vanilla `history/states/443-Sind.txt:10-12` gives RAJ ownership/core and SIN core; `:23` adds a PAK core. The binding preserves `443=RAJ`, with RAJ retaining at least one 1936 state. No Event 006 ownership/controller transfer is admitted. |
| Identity, rights, and origin | Blocked | The resolution requires period-correct port, municipal, customs, shipping, merchant, labor, and local-defense institutions, with traditional/dynastic authority only where period-correct; no accepted concrete officeholder/institution or rights contract is wired. |
| Leader and character roster | Missing | No mod SIN character file, `recruit_character`, leader, advisor, commander, high-command, or trait surface was found. Vanilla has no Sindh-specific character roster. |
| Portraits | Blocked | No accepted Sindh portrait consumer, source archive, rights evidence, or source-placeholder wiring exists. Generated or invented grounded leadership is forbidden. |
| Flags and symbols | Blocked | Vanilla provides only `SIN_communism`, `SIN_democratic`, `SIN_fascism`, and `SIN_neutrality` ladders; there is no base `SIN.tga`. No accepted period Sindh flag/emblem provenance or mod asset consumer exists. |
| Parties and politics | Vanilla-only | Vanilla history has neutrality-led politics, 1934 election, 60 neutrality/30 democratic/5 communist/5 fascist popularity; no Event 006 party names, government route, elections, rights, or settlement behavior exists. |
| Focus tree | Shared framework only | `common/national_focus/006_independence_wave_focus.txt` exposes the shared `independence_wave_focus_tree`; no SIN-specific callback, adapter, localization, icon, or route was found. |
| Decisions and missions | Missing | No IW-136 decision category, mission, timed objective, paid project, or package-local action was found. The broad SIN entries in `common/decisions/006_independence_wave_iw043_iw058_decisions.txt` are partner-target lists for other packages, not Sindh package logic. |
| Ideas and national spirits | Missing | No SIN-specific starting idea, lifecycle, icon, or gameplay-addressable starting problem exists. |
| Military and force setup | Spec-only | The accepted mapping calls for river infantry, port guards, and regular defectors (`regular_defectors`, force profile `67`) but no SIN OOB, templates, stockpiles, equipment, or setup effect exists. |
| Technology, industry, and supply | Vanilla baseline only | Vanilla history has two research slots and the listed early infantry/recon/support/motorized/artillery/air/armor technologies; no SIN package production, supply, port, rail, or technology consumer exists. |
| AI and playability | Missing and unquantified | No SIN strategy file or focus/decision AI exists. `independence_wave_weight_iw_136` is only a generic allocator weight, not country AI. |
| Formable and regional route | Not admitted | FORM-32 Indus Federation is a registry/spec contract in `006_formable_family_registry.csv:33`, not a current runtime consumer. No IW-136 formable implementation exists. |
| Cleanup, transfer, annexation, and host recovery | Missing | No SIN-specific release, transfer, annexation, puppet, cleanup, generation-safe teardown, or host-survival contract exists. |

## File surface checklist

| Surface | Current file or identifier | Finding |
| --- | --- | --- |
| Package metadata | `common/script_constants/006_independence_wave_constants_registry.txt:7632` | `iw_136=136` exists as a generic package ID. |
| Region loader | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2725-2736` | Generic loader binds `iw_136`, `RG-443`, South Asia/Himalaya, regional depth, river/corridor archetype, and anchor `443`; it saves the vanilla `SIN` carrier and current owner as event targets but adds no package gameplay. |
| Candidate trigger | `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:967` | Generic planner trigger calls `SIN = { is_independence_wave_candidate_tag_available = yes }`; this is gated and not an admission. |
| Shared candidate gate | `common/scripted_triggers/006_independence_wave_package_triggers.txt:74-81` | A candidate needs origin availability plus `independence_wave_package_content_ready`; comments explicitly state identity proofs do not grant readiness. |
| Weight preparation | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2985-2993` | Generic wrapper initializes zero, checks `can_plan_independence_wave_package_iw_136`, loads metadata, and delegates to the shared allocation calculator. |
| Reservation | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:3159-3168` | Generic wrapper reserves anchor `443` after loading metadata; it does not release or configure SIN. |
| Scenario ranking | `common/scripted_effects/006_independence_wave_scenario_effects.txt:185` | `iw_136` is present in a generic ranked package list only. |
| Weight initialization | `common/scripted_effects/006_independence_wave_effects.txt:3466` | `independence_wave_weight_iw_136` is initialized to zero. |
| Runtime adapter gate | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-62` | `iw_136` is absent from the admitted runtime adapter OR-list. |
| Content attestation gate | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202` | `iw_136` is absent from the content-attestation OR-list. |
| Preflight | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-210` | Preflight requires dormant scope, adapter, and content attestation; SIN cannot pass it. |
| Planner weight proof | `common/scripted_effects/006_independence_wave_package_planner_effects.txt:621-630` | The shared allocator only assigns the base weight after content attestation passes. |
| Focus source | `common/national_focus/006_independence_wave_focus.txt` | Shared tree only; no SIN package branch or callback. |
| Mod country/tag/history surfaces | `common/countries/`, `common/country_tags/`, `history/countries/` | Exact `SIN`, `iw_136`, and `IW-136` census found no Event 006 package shell or history. Current shell-consolidation changes do not include registered vanilla `SIN`. |
| Characters/recruitment | `common/characters/`, `history/general/` | Exact SIN/IW-136 census found no package roster or recruitment. |
| AI | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` | Exact SIN/IW-136 census found no country AI strategy. |
| Localisation/assets | `localisation/`, `gfx/`, `interface/` | Exact SIN/IW-136 census found no Event 006 country name/party/leader/idea/focus/decision/icon/portrait/flag consumer. |
| Formable | `common/decisions/formable_nation_decisions.txt:17330,17362` | These are existing vanilla Hindustan `original_tag = SIN` allow/visible references, unrelated to FORM-32 and not evidence of an IW-136 route. |

## Map and state setup

The accepted anchor is state `443`, localized as Sind, with current binding `443=RAJ`, `RAJ=439`, and an explicit requirement that the host retains at least one 1936 state after compact reservation.

Vanilla `history/states/443-Sind.txt` records state ID `443`, owner/core RAJ, SIN core, PAK core, victory point province `3456` at 25, infrastructure 2, one industrial complex, naval base 4, ten listed provinces, and local supply `7.0`. This is a useful historical baseline, not a release authorization.

Read-only `hoi4_map_inspect` for state `443` completed at workspace revision `9ecfc1f41da23dc6ddfe554f06e7f835c747b22b25427fe91d6976853e9cc823` with one inspected state and the connected map validation families for files/definitions, bitmap geometry, state-region membership, and networks/adjacencies. The MCP returned workspace-linked map JSON/PNG/HTML artifacts, but their provenance manifest could not be read, so no incomplete URI is recorded as validated evidence.

The same map inspection reported workspace-global locator validation failure and truncated diagnostics, including 1,323 `MAP_BUILDING_POSITION_INVALID` and 1,331 `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics. These were not attributable to state 443 from the returned projection and must not be treated as a Sindh defect.

An allocation preview including state `443` failed with the exact MCP code `MAP_STATE_ID_COLLISION`. No map rewrite was attempted.

The state-443 artifact provenance read failed with `resources/read failed ... Artifact provenance manifest is unavailable`, and a subsequent `hoi4_map_render` failed with `tool call ... hoi4.map_render ... Transport closed`. Therefore there is no current rendered map evidence for a Sindh package, and the installed binding remains a planning contract only.

## Politics, leader, portrait, flag, advisor, and party issues

The accepted resolution requires a defensible 1936 Sindh officeholder or authentic institutional authority. It specifically permits port, municipal, customs, shipping, merchant, labor, and local-defense institutions, with traditional or dynastic authority only where period-correct. No such identity has been accepted or wired.

Vanilla localization in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/countries_l_english.yml:4968-4982` supplies baseline `SIN`, `SIN_DEF`, `SIN_ADJ`, and ideology names, but it does not satisfy the Event 006 rights, identity, or route-localization contract.

The four vanilla ideology flag ladders are not a sourced base or route variant. The symbol handoff remains blocked and explicitly forbids backdating modern/post-1936 symbols or promoting an ideology variant without historical/route provenance.

No leader, council, committee, junta, advisor, commander, institutional portrait, portrait archive, portrait placeholder, or portrait-specific `.gfx` wiring exists for SIN. A fictional or generated grounded leader would violate the accepted source gate; institutional names must not be fabricated as personal random-name pools.

No Event 006 party names, popularity changes, government transitions, election behavior, rights/autonomy routes, or mixed-population safeguards exist. A local patch cannot safely supply these without identity research and package design.

## Focus, decision, idea, event, and asset issues

`hoi4_focus_inspect` on `independence_wave_focus_tree` completed with `FOCUS_INSPECTED`, 184 focuses, zero branch-count diagnostics, zero connector crossings/intersections, and one long-connector warning. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca7e814ee85cbe6743dcbb8c74fcecadc5885b55587c315267300f13999c9f3c/8ffccbc46427863b23b931c6074986fd7f3bc9b7e4cdb3bbc3d2d78560b85317/focus-inspect.8665217aa8ee7699.json`.

`hoi4_focus_render` completed for the shared tree at source revision `8665217aa8ee7699459939565d85668c8a929fc39655a7949ae64c7dfade569d` and layout hash `a4d2d61f...`, producing the HTML/SVG/JSON/source-map/plan artifacts under the MCP workspace. This proves shared-tree syntax/layout only; it does not prove a SIN route, localization, icon coverage, or focus AI.

The first focus-render attempt used unsupported `includeHtml` and failed with `MCP error -32602: Unrecognized key: "includeHtml"`; the corrected call succeeded. This is recorded to prevent treating the failed call as a source defect.

`hoi4_event_inspect` trace for `chaosx.nr6.1` completed as `EVENT_INSPECTED_PARTIAL` with revision `18bf807c8be35655138be368b38a6ff43f90d4c9ac0a1470ca1d9d44f43afd8f`, graph hash `e12130ac480e90a1098f39e8c272668599c42b61125c7a027bb8e84ebe6659d2`, 9,725 events, 15,153 options, 38,332 edges, and no blocking diagnostics in the selected projection. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/afd1ec9a251d6f5f4848724200ed3e1e86d2bedbe14047dce48b6bc90274ede7/cb40e96327f764168e16f251f8fba54d17aac57ad05c23cb8c66c153e2c43a09/event-trace-18bf807c8be3.json`.

`hoi4_event_render` for `events/006_independence_wave.txt` completed as `EVENT_RENDERED_PARTIAL` with the same revision/graph hash, layout hash `5a87c354...`, and no blocking diagnostics, but deferred workspace-wide helper and lifecycle projections. The file-level render has no SIN-specific event entry, option, event log actor, event-details consumer, or cleanup surface.

There is no IW-136 decision category, mission, idea, icon, portrait, flag, focus icon, or package-local asset manifest. No event-owned GUI is introduced, so no GUI rewrite is justified.

## Starting military, technology, industry, supply, and production issues

The accepted force mapping is a design contract only: river infantry, port guards, regular defectors, force profile `67`, engineers/artillery/recon/river logistics, coastal signals, and civilian oversight. No OOB, division template, equipment, manpower, production line, convoy/train, fuel, port, railway, supply, or reinforcement setup is present for SIN.

Vanilla SIN history provides two research slots and the early technology baseline listed in the vanilla history file, but has no Event 006 starting forces, ideas, production, or package-specific technology unlock.

The read-only `hoi4_tech_inspect` workspace scan completed at revision `a1417861a875af477b7a3610a988ee2b9df2256e200e0f90b7f335749ff319aa` with 679 technologies, 18 folders, 475 placements, 457 edges, 860 unlocks, 520,292 references, three unresolved items, and 1,295 issues. `hoi4_tech_render` produced a workspace-global summary but validation remained false with 1,427 blocking technology diagnostics. It does not isolate SIN.

The installed package currently exposes no country-specific/runtime Technology Tree Viewer consumer for SIN. The generic tech scan/render is workspace-global and diagnostically blocked, so technology evidence remains unresolved rather than a positive package finding.

## AI and probability issues

No SIN strategy file, focus factors, research factors, template behavior, decision AI, diplomacy behavior, or survival/role strategy exists. The generic `independence_wave_prepare_weight_iw_136` wrapper feeds the shared weighted allocator, and the planner only assigns a base weight after content attestation at `common/scripted_effects/006_independence_wave_package_planner_effects.txt:621-630`.

The mandatory probability pass was attempted against the `custom_weighted_pool` surface for `independence_wave_weight_iw_073`, `iw_086`, `iw_095`, `iw_108`, `iw_130`, and `iw_136` using `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` as source. The exact MCP failure was `tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: Transport closed`; no artifact or quantitative comparison was returned.

No callable project-subagent collaboration route for `chaosx_ai_probability_auditor` was exposed in this subagent session. The direct MCP attempt therefore cannot substitute for the mandatory auditor ownership pass. No AI weight or probability patch was made, and no quantitative balance claim is made.

## Central gates and why no patch is safe

`iw_136` is absent from the runtime adapter OR-list at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-62` and the content-attestation OR-list at `:159-202`.

The preflight at `:207-210` requires dormant scope, adapter, and content attestation, so adding `iw_136` there would falsely admit an incomplete package.

No `independence_wave_package_content_ready` grant, central preflight, release/Join path, or FORM-32 runtime consumer exists for SIN.

The generic region wrappers are already fail-closed and are the correct current behavior. Patching them, the central dispatch lists, or the readiness flag would bypass the accepted gates and exceed this bounded country-package task.

## Completed work, omissions, and blockers

Completed: scoped source census; accepted-spec and installed-binding cross-check; vanilla country/history/state/politics/flag/localization review; exact mod tag/package/character/AI/decision/idea/asset census; offline wiki and vanilla documentation review; read-only MCP map, event, focus, and technology inspections/renders; mandatory probability route attempt; dated handoff creation.

No gameplay or asset patch was made. No central adapter, attestation, preflight, readiness flag, Join, FORM-32 route, fallback leader, fallback portrait, fallback flag, generic party, generic decision, generic idea, generic AI, OOB, or map write was added.

Remaining blockers are the exact 1936 Sindh officeholder or authentic institutional identity, rights-cleared portrait/source-placeholder evidence, period-fit flag/symbol provenance, package-local parties/politics/rights and mixed-population settlement, force/setup/economy/supply/cleanup implementation, package AI, FORM-32 design/admission, current map allocation/render evidence, and the required probability-auditor comparison.

Map render failed with `Transport closed`; allocation preview failed with `MAP_STATE_ID_COLLISION`; map artifact provenance read failed because the provenance manifest was unavailable; event file-scope inspection initially timed out after 180 seconds but focused trace/render returned partial evidence; technology evidence is workspace-global and blocking; probability inspection failed with `Transport closed`. These limitations are not treated as positive validation.

Live/in-game testing was not run because it belongs to the user and is outside the agent workflow.

## Exact next owner and sequencing

1. The Event 006 parent/identity owner should route IW-136 research to `chaosx_asset_source_researcher` and `chaosx_portrait_creator` for one defensible male period leader or authentic institutional consumer, with rights and source-placeholder evidence.

2. The symbol/asset owner should resolve a period-fit base or explicitly accepted alternate/civic route and complete the event-assets provenance, processing, `.gfx`, and manifest contract without reusing an unproven ideology ladder.

3. A package implementer should then build the non-generic IW-136 contract inside IW-136-owned files: identity and party setup, rights/autonomy behavior, force/setup/economy, decisions/projects/ideas, shared-focus callbacks, AI, host settlement, cleanup, and any separately accepted FORM-32 route. This requires a new implementation plan if the parent accepts the broad package scope; it is not a safe small patch from this audit.

4. After package-local completion, route the same scenarios through `chaosx_ai_probability_auditor` with `hoi4.probability_inspect` and `hoi4.probability_compare`, and repeat the current map/event/focus/technology inspections with artifact provenance available.

5. Only the Event 006 parent may later add central adapter, content attestation, preflight, release/Join, and FORM-32 admission after all package, identity, asset, probability, host, and map gates pass.

## Changed files and identifiers

Only this handoff was added: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw136_sindh_package_reaudit_2026-09-02.md`.

No gameplay, map, asset, localization, central registry, tag, focus, decision, idea, AI, history, character, or formable files were changed. No tags, state IDs, leaders, parties, focus tree IDs, localization keys, or formable IDs were added or changed.

No plan handoff was written because the present task is an audit handoff; if the parent accepts the broad identity/package work above, it should create or route a separate implementation plan before any package construction.
