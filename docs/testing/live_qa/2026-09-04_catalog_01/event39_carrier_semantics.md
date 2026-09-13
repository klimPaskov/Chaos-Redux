# Event 039 carrier semantics QA

Status: unresolved, read-only investigation.

Scope: determine whether the Event 039 `AXS` through `AXZ` registrations are intended to remain dormant ordinary tag templates with loader-only history files, or to become entries in the engine dynamic-tag pool.

No gameplay files were changed in this tranche. Events 006, 012, 016, and 023 were left untouched.

## Result

The seven launch records have a direct source cause: `AXS`, `AXT`, `AXU`, `AXV`, `AXW`, `AXY`, and `AXZ` are registered in `common/country_tags/039_murder_mystery_countries.txt`, but no matching `history/countries` file exists.

The current source still describes a fixed-tag carrier template model. The registry has no `dynamic_tags = yes` marker, the two active callers pass `original_tag = AXS` and `original_tag = AXT`, and the common country definitions contain only graphical culture and colours. The runtime then supplies the capital, politics, leader, ideas, technology, and equipment.

Adding an intentionally inert history file for each tag would preserve the current ordinary-tag registration model, assuming the engine accepts a zero-effect history file. It would not create a dynamic-tag pool. This parser and loader acceptance is not proven by the available documentation or by a live load in this task.

Adding `dynamic_tags = yes` before these entries would change their registration class and pool or recycling semantics. That is not equivalent to adding loader inputs, and the current source does not establish that the fixed `AXS` through `AXZ` names are intended pool slots. The vanilla trigger documentation also describes `is_dynamic_country` as checking `D01` through `D50`, while the installed vanilla registry currently defines `D01` through `D75`, so an arbitrary-name dynamic-tag inference would be unsafe.

The minimal registration fix is therefore not provable under the authorized safe-errors scope. The parent must first accept one carrier model and validate the engine identity behavior. No history fallback, dynamic marker, `copy_tag`, or invented country setup was added.

There is a second runtime blocker independent of the missing history files. Both Event 039 candidates are created before territory is transferred, and neither creation block calls `reserve_dynamic_country = yes`. Vanilla documentation says a dynamic country with no owned states must be reserved after creation. The host flag `murder_mystery_assassin_carrier_reserved` is a package flag and does not invoke that engine effect.

## Engine semantics and evidence

| Surface | Verified semantics | Evidence |
| --- | --- | --- |
| `dynamic_tags = yes` | Marks every country entry defined afterwards as dynamic. Vanilla uses it as the header for its temporary dynamic-country registry. | `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md:64`; `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/zz_dynamic_countries.txt:1-2` |
| `create_dynamic_country.original_tag` | Supplies the original tag or origin identity for the new dynamic country. The documented effect creates the dynamic country and runs its child effects. | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:3033-3044`; `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:301`; `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:321` |
| `create_dynamic_country.copy_tag` | If present, the new country copies data from this tag instead of from `original_tag`. It is a separate copy-source choice and must not be inferred from the origin tag. | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:3039-3043`; `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:301` |
| `reserve_dynamic_country = yes` | Reserves the created dynamic country so it is not recycled. The documentation specifically requires reservation when the new country has no owned states. | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:6367-6375`; `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:298,301` |
| Ordinary country history | A registered ordinary tag requires a `history/countries` file whose first three filename characters match the tag. The file supplies starting effects and is loaded in country-tag order. | `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md:36-42,104-107` |
| `is_dynamic_country` | The installed vanilla trigger documentation says true when the country tag is `D01` through `D50`. The installed vanilla registry has 75 dynamic entries, which is a documented-version caveat for arbitrary custom names. | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:5462-5469`; `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/zz_dynamic_countries.txt:1-76` |

The vanilla dynamic registry has 75 `common/countries/D##.txt` definitions and zero `history/countries/D##` files. For example, `common/countries/D01.txt` contains only a colour definition. This is evidence for a dynamic pool slot model, not evidence that arbitrary fixed tags should be moved into that pool.

The installed vanilla `create_dynamic_country` precedents use ordinary source tags as origins and then allocate a dynamic country. Examples include:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/BBA_Ethiopia.txt:6919-6948`, which creates from `original_tag = SOM` and transfers Somali-core states in the same child block.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/DOD_Romania.txt:4000-4026` and `4034-4055`, which create from `MOL` or `FROM` and then transfer states and puppet the result.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/GOE_Afghanistan.txt:2590-2618`, which uses `original_tag = PER`, explicitly reserves the new country, and then transfers states.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/LAR_occupation.txt:114-119`, which sets both `original_tag = FROM` and `copy_tag = FROM` when it wants the copy source to be explicit.

The protected Event 006 package gives the closest repository precedent for literal dormant carrier tags. Its registry remains outside a `dynamic_tags` block, and `common/scripted_effects/006_independence_wave_execution_effects.txt:511-525` uses `original_tag = AFX`, `copy_tag = THIS`, and `reserve_dynamic_country = yes` for the runtime-created country. Event 006 also has per-tag history files, such as `history/countries/ACX - Cornwall.txt`, that provide neutral politics and popularity before runtime formation. Those files are package-owned setup and cannot be copied into Event 039 as a generic fallback.

No comment-only or zero-effect country history precedent was found in the installed vanilla history folder or the current Chaos Redux history folder. The available evidence supports the classification distinction, but not the exact parser behavior of a truly empty file.

## Current Event 039 surface

### Country package coverage checklist

| Package surface | Status | Exact evidence or blocker |
| --- | --- | --- |
| Tag registration | Present but semantically unresolved | `common/country_tags/039_murder_mystery_countries.txt:4-15` registers `AXS`, `AXT`, `AXU`, `AXV`, `AXW`, and `AXZ` as ordinary entries with no `dynamic_tags = yes`. |
| Common country definitions | Present | `common/countries/039_murder_mystery_assassin_state.txt:4-12` and `common/countries/039_murder_mystery_derivative_state.txt:4-12` provide graphical culture and colours only. |
| Ordinary history inputs | Missing | No `history/countries` file begins with any of the seven prefixes. This is the direct cause of the launch 08 `history.cpp:279` records documented in `docs/testing/live_qa/2026-09-04_catalog_01/missing_country_history_sources.md:14-18,22-34`. |
| Dynamic pool registration | Absent and not safe to infer | No Chaos Redux `dynamic_tags` declaration exists. The fixed carrier model is not validated as a dynamic pool model. |
| Active carrier callers | Partial | `common/scripted_effects/039_murder_mystery_integration_effects.txt:1517-1601` calls `original_tag = AXS`; `:1713-1729` calls `original_tag = AXT`. |
| Reserved derivative slots | Unused in bounded source scan | `AXU`, `AXV`, `AXW`, `AXY`, and `AXZ` are registry reservations only. No direct `original_tag` caller was found for them. |
| Runtime reservation | Missing | No `reserve_dynamic_country` call exists in the Event 039 integration or runtime effects. The package flag at `:344` is not the engine reservation effect. |
| Tag identity acceptance | Blocked | `docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_6_assassin_state.md:15-21` explicitly says no tag was selected and requires a carrier audit before implementation. |

### File surface checklist

| File surface | Finding |
| --- | --- |
| `common/country_tags/039_murder_mystery_countries.txt` | Registry comments call the entries dormant dynamic carriers, but the file declares ordinary tag entries and no dynamic pool marker. |
| `common/countries/039_murder_mystery_assassin_state.txt` | Static template data exists for AXS. No history, capital, politics, leader, state, or OOB data is present here. |
| `common/countries/039_murder_mystery_derivative_state.txt` | Shared static template data exists for AXT through AXZ. Its comment explicitly says no ordinary civil-war history is attached. |
| `common/scripted_effects/039_murder_mystery_integration_effects.txt` | AXS and AXT are created dynamically with `original_tag` only. Runtime country setup is supplied in child effects, and territory is transferred later. |
| `common/scripted_effects/039_murder_mystery_runtime_effects.txt` | Split and derivative transaction effects validate and transfer states, but no engine dynamic-country reservation is applied. |
| `events/039_murder_mystery.txt` | Event roots dispatch the setup and transaction helpers. No country history or pool declaration is provided here. |
| `history/countries/AXS*` through `AXZ*` | All absent. No approved source exists for safe recovery. |

### Missing or stale package surfaces

- The seven history inputs are absent.
- The registry comments and the accepted spec disagree on carrier status. The comments assume dormant dynamic carriers, while the spec says no tag was selected and requires an audit first.
- The source has no explicit dynamic-tag pool declaration.
- The source has no `copy_tag` argument. That means the documented default copy source remains the `original_tag` template, which is materially different from the Event 006 `copy_tag = THIS` pattern.
- The source has no `reserve_dynamic_country = yes` call even though candidate creation precedes state transfer.
- `AXU`, `AXV`, `AXW`, `AXY`, and `AXZ` are registered but have no bounded callers in the current scan. Their capacity role is therefore only described by comments and registry rows.

### Map and state setup issues

No map rewrite was authorized or performed, and no fixed state or capital was invented. The active candidate paths use runtime anchors:

- Assassin State capital is set from `event_target:murder_mystery_split_anchor_state` at `common/scripted_effects/039_murder_mystery_integration_effects.txt:1593`, while the split-state transfer happens later in `common/scripted_effects/039_murder_mystery_runtime_effects.txt:1424-1431`.
- A derivative first transfers `event_target:murder_mystery_derivative_anchor_state` at `common/scripted_effects/039_murder_mystery_integration_effects.txt:1766-1768`, then sets that state as capital at `:1771-1773`.

The map and state identity is consequently a runtime transaction concern. It cannot resolve the registration error without a carrier identity decision. No map MCP inspection was run because this bounded task has no fixed state or map edit to inspect.

### Politics, leader, portrait, flag, advisor, and party issues

Static history supplies none of these surfaces. Runtime setup does create the Assassin State leader `MURDER_MYSTERY_FIRST_KNIFE_NAME` with `GFX_portrait_039_first_knife` at `common/scripted_effects/039_murder_mystery_integration_effects.txt:1544-1550` and route-specific derivative leaders at `:1730-1764`. Those runtime identities were not redesigned or re-audited in this registration-only investigation.

The seven flag ladders are documented as present in `docs/assets/039_murder_mystery/visual_asset_audit.md:296-316`, but flags cannot satisfy the missing history input. Portrait production and provenance are outside this carrier-semantics scope.

### Focus, decision, idea, and asset issues

The runtime candidate receives Event 039 ideas at `common/scripted_effects/039_murder_mystery_integration_effects.txt:1536-1540` and `:1726-1728`. Focus trees, decisions, and idea lifecycle are not changed by a registration-only fix and were not treated as evidence for choosing a tag model. No asset or GUI change was made.

### Starting military, technology, industry, supply, and production issues

The Assassin State runtime applies research slots, stability, war support, technology, manpower, and operation kits at `common/scripted_effects/039_murder_mystery_integration_effects.txt:1541-1544` and `:1594-1600`. The derivative path applies manpower and operation kits at `:1726-1728`. These values are not available from the common country definitions and therefore do not make a missing ordinary history file safe by themselves.

No fixed OOB, production line, supply, railway, port, resource, or building setup is present in the carrier definitions. No such setup was invented.

### AI and playability issues

The candidates are intended to become playable only after the split or derivative transaction passes its postconditions. The Assassin State transaction validates candidate existence, state count, capital, and leader registration in `common/scripted_effects/039_murder_mystery_integration_effects.txt:1605-1677` and `common/scripted_effects/039_murder_mystery_runtime_effects.txt:1403-1452`. The derivative path validates state transfer and host survival at `:1769-1787`.

Those checks cannot prove the engine will retain a newly created dynamic country between the creation block and the later transfer block. The missing reservation effect remains a playability blocker. No AI weighting or probability surface was changed, so no probability-auditor pass was applicable.

## MCP evidence

The required event route was attempted read-only.

- `mcp__hoi4_agent_tools__hoi4_event_inspect` with selector `event:chaosx.nr39.1`, mode `state_flow`, returned `status = error`, `code = INTERNAL_ERROR`, `filesScanned = []`, and blocker message `Unexpected internal error`.
- A file scan of `events/039_murder_mystery.txt` returned `EVENT_INSPECTED_PARTIAL` with graph revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`. The linked artifact is [event-scan-1102e50fad94.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72cc4daceb1c2b0f0740e99c445075bf1e0af828bf65f8814ade65069344dc3e/68cd01e859907f11da23d970e36c03f7747096eb458330f3e0580e4ba9a537f0/event-scan-1102e50fad94.json). The result is partial because the large workspace scan retained a truncated inline projection and reported one unrelated `SOURCE_UNCLOSED_BLOCK` diagnostic in `mod:common/on_actions/023_sov_nuclear_bombs_on_actions.txt`.
- A read-only event render returned `EVENT_RENDERED_PARTIAL`. The linked authoritative overview is [event-overview-1102e50fad94.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/548ab2f476c090f00f05de4844638282e91c6933c086b2622248c3d89129fb92/50eea170f8ee467eaaf522ddcdea9d387220afd6b9cd207ee50fc341b488f8a0/event-overview-1102e50fad94.json). It confirms the Event 039 root `chaosx.nr39.1` and records unresolved focused helper projections, including `murder_mystery_prepare_opening_package` and `murder_mystery_apply_scenario_setup`; it does not establish country-tag or dynamic-pool semantics.

No focus, technology, GUI, probability, or map surface was modified or claimed as validated in this bounded investigation. Standalone Technology Tree Viewer availability was not tested because no technology dependency is in scope.

## Parent action

Before any source fix, accept one of these package models:

1. Fixed dormant ordinary carrier templates. Supply seven tag-specific history inputs whose content is explicitly accepted for Event 039, verify that a zero-effect or inert history file loads, and keep `AXS` through `AXZ` outside a dynamic pool. Add the documented dynamic-country reservation at the runtime creation boundary if candidates can exist without owned states.
2. A validated dynamic-tag pool. Rework the registry and callers together around a documented or engine-verified pool allocation model, with an explicit capacity and origin or copy-source contract. Do not treat `dynamic_tags = yes` as a one-line loader repair.

The current evidence does not select between these models. The safe disposition is to leave the seven registrations unresolved and keep the launch 08 history records open until the parent accepts a carrier identity and obtains engine validation.

## Simplifications, omissions, and blockers

- No gameplay source files were changed.
- No empty history files were added because the engine acceptance of a zero-effect history file is unverified and the parent has not accepted the static carrier model.
- No `dynamic_tags = yes` marker was added because it would change registration and pool semantics.
- No `copy_tag` argument was added because it would change the documented data-copy source.
- No capitals, leaders, parties, technology, states, OOBs, AI weights, generic fallback histories, assets, or map data were invented.
- Confirmed blockers are the unresolved carrier identity, seven absent history inputs, the lack of a proven dynamic pool contract, the absent runtime dynamic-country reservation, and the focused `hoi4_event_inspect` internal error.
