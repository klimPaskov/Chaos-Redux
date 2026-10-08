# Event016 runtime supply-endpoint binding review

Date: 2026-10-08.
Role: chaosx_scripted_system_architect, bounded read-only architecture task.
Disposition: geometry/control architecture specified; exact runtime supply-node reader, selected-node damage and whole-edge level/damage proof remain unresolved.
Only this report is created after absence checks on disk and HEAD.
No gameplay, catalogue, index, Git, model/unit-asset or HOI4-launch write/work is performed.
The KRG fabrication commit `bdda3448980b6dbf3efe8cafe0b9c55689163f24` is neither duplicated nor modified.

Authority: accepted `016_mengele_transit_deployment_acceptance_2026-10-08.md`, final completion contract lines 91-100, and the parent's bounded `016_transit_state_catalog_2026-10-08.md` component acceptance.
The full payoff stays +1 infrastructure at EACH selected endpoint and a level-two actor-controlled railway between verified supply endpoints.
No flag, stricter state aggregate, static 1936 node list or weaker rail predicate replaces it.
Parent owns catalogue data/engine validation, topology extraction and implementation.
AGENTS.md and the events, decisions/missions and subagents skill sections were read/applied; no skill was changed.

## Main finding: the current exact-node backend is not verified

Installed `any_province_building_level` supports STATE scope and a literal `province = { id = ... }` filter for a named building/level.
That proves a generic provincial-reader syntax, not that it recognizes special supply-network objects as ordinary province buildings.
The inspected documentation does not enumerate special-network support for this command.
The only supply_node line found in the bounded vanilla AI/trigger/decision/project search was COMMENTED OUT in ENG.txt:3075; its active query uses naval_base.
It is not a positive supply-node-query precedent.

The connected lookup's provinceBuildings dictionary omits nodes even though map/supply_nodes.txt records their locations separately.
This is a source-model representation distinction, not proof that the engine reader fails or succeeds.
Installed `00_buildings.txt:98-124` marks supply_node with `supply_node = yes` and handles rail_way separately.
Event028's ordinary provincial adapter explicitly excludes these two network types:
- `common/scripted_triggers/028_asteroid_incoming_province_triggers.txt:4-7,10-45` classifies ordinary types and warns against an ordinary setter.
- `common/scripted_effects/028_asteroid_incoming_province_effects.txt:4-9,16-25` confines the all-province setter adapter to ordinary buildings.
- `common/scripted_effects/028_asteroid_incoming_effects.txt:584-614` retains a separate native-evidence gap for rail/supply objects.

That exclusion concerns SETTERS; it does not itself establish that the generic READER is unsupported.
It does establish why treating every province_max token as an ordinary object is unjustified.
The exact conclusion here is **unverified supply-node special-object capability**, not a categorical claim that the query always fails.
`script_validate` recognizes the command/STATE scope but leaves its argument block unchecked.
Neither that result nor source-map data verifies a CURRENT exact-node predicate.

A bounded native-document inventory/search found aggregate supply_node/building counts, num_of_supply_nodes and total construction counters, but no documented current exact-province supply-node locator/health getter.
Do not substitute those aggregates or seed runtime eligibility from supply_nodes.txt.
The proposed full resolver's current-node backend must be verified before it can truthfully publish an exact current endpoint.
Geometry + control alone must return an explicitly unresolved binding status, not a successful supply entitlement.

## What is verified and reusable

| Capability | Verified fact | Limit |
| --- | --- | --- |
| Complete geometry input | Parent's accepted lazy catalogue covers 1,081 state IDs 1..1081, 10,272 assigned provinces, no repeated membership, maximum 70 members per state. | Parent-supplied extracted catalogue facts, not this worker's independent full extraction or runtime node proof. |
| Numeric array iteration | Native any_of/all_of supply named temporary value/index variables and do not create province scopes. | Do not use any_of_scopes on numeric province IDs; no province script scope is documented. |
| Current province control | Built-in province_controllers indexes controller COUNTRY by raw numeric province ID. | State-majority control alone does not prove a node province is controlled by the payer. |
| Numeric state identity | State GetID returns the history-file ID for meta use. | State dynamic id is an opaque internal pointer, often negative; never use it as the numeric catalogue key. |
| Static field injection | Native STATE meta_trigger can create a literal province.id query from an integer candidate. | Meta syntax does not grant the underlying query special-network semantics. |
| Actor identity | Explicit payer COUNTRY pointer can be compared with state owner/controller and the selected province controller. | Validate existence with a country-specific check; no reliance on outer ROOT or scope_exists(variable). |

No complete built-in per-state province list was found in the installed dynamic-variable/global/state inventories and bounded documentation search.
The documented global states array is all state scopes; province_controllers is not a state-membership array.
The inspected State localisation properties expose GetID/GetName, not a province collection.
Do not invent THIS.provinces, state_provinces or province_states.
The accepted geometry catalogue is the verified component choice, and this worker creates no competing dataset/loader.

## Recommended exact API/data contract

Recommend one Event016-owned pure STATE producer `brilliant_scientist_transit_resolve_supply_endpoint`, plus one frozen-binding validator.
Names below describe the parent implementation contract, not installed helpers or new gameplay design acceptance.

Use the parent's existing accepted geometry API exactly:
`brilliant_scientist_transit_load_state_province_catalog`, outputs `transit_catalog_state_id`, caller-owned temporary integer array `transit_state_province_ids`, and `transit_catalog_loaded`.
It uses documented GetID/meta_trigger and a balanced static numeric dispatcher.
Do not dynamically paste an unknown helper name or scan all states.
Unknown/negative/fractional IDs return empty/false through that accepted dispatcher.
The parent generates/validates this component; no implementation is duplicated here.

| Resolver field | Type / ownership / default | Contract |
| --- | --- | --- |
| `transit_endpoint_actor` | Caller-owned temporary COUNTRY pointer, required | Explicit payer set in country context before entering the selected STATE; no outer ROOT inference. |
| `transit_catalog_state_id` | Caller-owned temporary raw integer, zero | Numeric GetID-derived state key from the parent loader; not the state scope pointer. |
| `transit_state_province_ids` | Caller-owned temporary integer array, empty | ALL geometry members of THIS state, sorted/unique, no static node/status filtering. |
| `transit_catalog_loaded` | Caller-owned temporary status, zero | Complete matching geometry entry loaded. |
| `transit_endpoint_province_id` | Caller-owned temporary positive integer, zero | Deterministic current exact node ID only after verified node backend and current control/membership checks. |
| `transit_endpoint_found` | Caller-owned temporary status, zero | Binding success, not general rail/health certification. |
| `transit_endpoint_node_reader_known` | Caller-owned temporary status, zero | Proven special-node backend available; zero distinguishes unknown capability from a genuinely absent node. |
| `transit_endpoint_health_known` | Caller-owned temporary status, zero | Exact selected-node health proof available; not inferred from binding/presence. |

All consumed scalar/array outputs must exist in the caller before nested helper entry.
Reset result fields on every query and preserve the actor input.
The helper changes temporary scratch only: no flag, regular record, global registry, payment, history, target or construction.
A stable producer boolean may accompany explicit statuses; a malformed/unsupported backend must not look like “no node here” or successful binding.
The current verified capability does not permit setting node_reader_known/found to one solely from the generic argument shape.

### Resolver algorithm after an exact-node backend is established

1. Validate THIS as the selected STATE and the explicit payer as an existing COUNTRY.
Read current state ownership/controller against that payer; regular country scope pointers and raw numeric state IDs remain distinct.
2. Invoke only the accepted geometry loader; require its matching complete entry.
Do not copy current node/controller/damage/capital eligibility into immutable geometry.
3. Iterate these numeric members only, guarding positive/integral IDs and controller-array index bounds.
Use `province_controllers^transit_endpoint_candidate` CURRENTLY and compare its COUNTRY pointer with the explicit actor.
No controller snapshot from the map source or majority-state rule authorizes a node.
4. Query the verified CURRENT special supply-node predicate at that member in the SAME STATE context.
The backend must detect newly built/moved nodes outside supply_nodes.txt and reject removed/captured nodes at the exact ID.
5. Reduce the lowest valid numeric province ID, then publish found one and that ID.
This is deterministic first-in-ascending-membership semantics.

Prefer a full numeric all_of pass whose body always returns true and updates the minimum only inside an if.limit.
This is O(P), independent of undocumented iteration ordering, and examines all P members.
An any_of early-stop implementation is structurally supported but needs proven ordering and correct short-circuit handling; a temporary-write/no-match branch must not accidentally return true.
None of these operations scopes into a province.

The generic node query below is a **candidate backend probe**, not verified production functionality:

~~~text
# STATE scope; province is a filter block, not a province scope.
meta_trigger = {
	text = {
		any_province_building_level = {
			province = { id = [PID] }
			building = supply_node
			level > 0
		}
	}
	PID = "[?transit_endpoint_candidate|.0]"
}
~~~

Candidate ID comes from validated integer geometry, not a scope pointer/display name.
Meta injection avoids assuming that static province.id accepts a variable token.
Native docs make all_provinces=yes mutually exclusive with id.
The exact generic query should be verified on a genuine current network node and a non-node member, then a newly constructed/moved/removed node, before becoming the resolver backend.
A successful parser/scope check alone cannot close this requirement.
If it does not read special nodes, a separate exact native locator is required; no native first-class province scope is available as an invented workaround.

## Selection, frozen receipt and currentness

The accepted free origin/destination controls select STATEs in the existing category.
Country target_root_trigger supplies provider/prerequisite/phase gates; state_target=any_owned_state narrows candidates.
Within FROM STATE, pass the explicit payer from the country caller.
The geometry/resolver producer may be used in target_trigger/available without writing regular receipts.
Repeat live ownership/control/node checks at commit; a daily target cache is not authority.

Before payment, discovery/preview may update to the current deterministic node of either selected state.
At payment, recompute both exact bindings and confirm distinct neighboring owned-and-controlled industrial/supply states, both +1 infrastructure slots, and the accepted level-two actor-controlled route preflight.
Freeze payer pointer, both STATE pointers, their GetID numeric keys, exact numeric province IDs, geometry revision/provenance, intended infrastructure levels and rail specification in the payer's existing private transaction.
Temporary discovery results are not persistence.

Proposed `brilliant_scientist_transit_bound_supply_endpoint_is_valid` is STATE scoped and accepts explicit actor plus frozen province ID.
It checks the exact member, current STATE owner/controller, CURRENT province controller, CURRENT verified special-node backend and any established exact node-health condition.
It never reruns discovery or selects another node.
Use it at finish/recovery and supplemental consumer validity.
An alternate new node in the same state cannot replace the paid endpoint.
Reacquisition/repair may restore the same genuine bound location; it does not replay construction, transfer entitlement to a captor or revoke learned neutral technology.
The accepted private receipt remains separate from KRG history.

Country capital supply-source semantics are distinct from supply_node building semantics.
State GetCapitalVictoryPointName is the largest-VP name, not a country-capital province locator or node proof.
Native state-to-state rail pathing prefers capital, then nodes/naval; hence use explicit frozen province endpoints once node binding is proved.
Do not silently accept a capital without the required real supply endpoint.
A capital-source exception requires its own accepted and verified exact native semantics.

## Exact node health and whole-edge proof

| Need | Current documented capability | Gap that must remain open |
| --- | --- | --- |
| Node membership/control | Complete geometry and current province controller lookup | Cannot prove special-node presence by themselves. |
| Exact current node presence | Generic STATE/literal province building reader is a candidate | No verified special supply_node support from inspected documentation/active precedent/current lookup. |
| Exact selected-node damage | STATE non_damaged_building_level / damaged_building_level aggregates exist | No documented exact province parameter or damaged-level exclusion for the candidate reader; a different healthy node can satisfy aggregates. |
| Infrastructure delivery | State infrastructure/non-damaged readers, slots and construction | Keep actual +1 in EACH endpoint with distinct component receipts. |
| Connectivity/buildability | Explicit native path/start/target province specification, allied restriction and controller-priority exclusion, fallback choice | Does not prove every selected edge is level two or healthy. |
| Rail minimum level | has_railway_level finds some qualifying railway within a STATE | Unrelated higher track can satisfy it; not exact corridor minimum proof. |
| Rail damage | State/country damaged-building aggregates | No documented exact route/edge damage getter or predicate. |
| Computed path identity | Native builder/query can select paths; explicit literal paths can constrain a known path | No documented query exporting the current chosen shortest-path sequence for arbitrary runtime endpoints. |

has_railway_connection says “same params as can_build_railway” but its documented example supplies no level/damage threshold.
That is a potential parser research seam, not established proof that level=2 enforces every edge or excludes damage.
The bounded search found no exact minimum-level/damage contract.
Checking every province for a generic rail_way building level is also unverified for special rail-network storage and cannot identify each selected edge pair; another incident edge could be unrelated.
has_damaged_buildings is COUNTRY scoped, and country supply-node count cannot settle exact endpoint/location proof.

Parent's connected source-map artifact can provide complete SOURCE topology and initial levels for selected probes.
It does not observe campaign construction, repair or damage.
Do not substitute static1936 nodes, stronger whole-state damage gates or country aggregates as equivalent exact evidence.
Such substitutes can also exclude otherwise valid selected states and would require explicit acceptance.
Both +1 infrastructure components and the level-two native railway payoff/receipts remain intact while these capabilities are resolved.
The full resolver and commissioning cannot be called ready from geometry/control alone.

## Performance and presentation contract

Parent reports the complete accepted catalogue has maximum 70 members per state; no 1,000-item state truncation is needed for this geometry.
Balanced dispatch is O(log S) for S=1081 and the current-node pass O(P) for P<=70, plus O(P) membership loading.
Record those as parent data facts, not an independent full catalogue extraction by this worker.
Province controller reads are indexed, not a global/world scan.
There is no startup population, world iteration, scheduler, registry grant or periodic eligibility repair.

Native MAX_EFFECT_ITERATION=1000 applies to loop effects; native any_of/all_of docs do not specify that same cap or establish arbitrary unlimited traversal.
For this 70-member input, parent still tests complete traversal and last-member success through actual source/engine boundaries.
Never use an undocumented iteration limit to silently omit data.

Use narrowed daily target gates and current live available/commit checks, not a per-frame scan over every state/province.
Post-payment checks concern only the frozen two bindings and qualifying route.
Label selected states with FROM/saved STATE GetName; use raw GetID for debug/meta keys.
Display exact node integer IDs when a proven province-name localisation context is absent.
Do not use a numeric state scope like [6521.GetName] as if it were a province.
Province localisation objects do not create province script scopes.
Reuse the existing selection/category presentation; no family/category/window/project/technology/unit or asset/model package is added.

Required evidence cases before backend acceptance: standing node versus non-node member; dynamic node outside baseline file; moved node before/after payment; removed/captured node with alternate remaining; partial-state control; foreign outer ROOT; opaque state id versus GetID; all 70 members/last valid member; unknown catalogue key; capital without node; selected-node damage with another healthy node; unrelated high-level/damaged rails; partial infrastructure/rail settlement and idempotent recovery.
These are parent evidence contracts, not an instruction to launch HOI4 in this task.

## Map evidence and revision distinction

Parent supplied MAP_INSPECTED revision `34b40fa7ff00cf49602d57615f525b0ec820972e86e8c1676f6779eef2a99f6f`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/12c4c50f92e48351b8502af80dc630f64d80ffbe62f17468be9a3333c89ff236/f0d74c19d48aa33ca03a45abf5ac0092c1b2f8473fe4cba77149802be17d9aeb/map-inspect.34b40fa7ff00cf49.json`, 74,681,698 bytes.
Parent owns its extraction/verification and reports membership/network/bitmap/definition checks passed, with overall false because of three Event032 localisation errors and floating-harbor review warnings.
No full clean-map claim follows.
Those are source probes, not approved fixed endpoints or live campaign state.

Worker performed only a bounded lookupOnly state64/province6521 probe, no overview/full duplicate call.
It returned MAP_LOOKUP_COMPLETED, no inline blocker, revision `0bfec365ebd618829c30c16d5ecb9b6ce026d0927a64e11dd437759265adbe9f`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07dd341066c71d8aec48c8fb89c7833d4b6e33dd2d5318e7c6f8f3492fcc0be7/c490f286b534d07485a10907b80f3cb9386084f1db1997095e153964deb6fb6e/map-lookup.0bfec365ebd61882.7f4bb8ad66327b5e.json`.
Own lookup bytes were read-only verified at `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\07\07dd341066c71d8aec48c8fb89c7833d4b6e33dd2d5318e7c6f8f3492fcc0be7\map-lookup.0bfec365ebd61882.7f4bb8ad66327b5e.json`: 247,840 bytes and exact SHA `07dd341066c71d8aec48c8fb89c7833d4b6e33dd2d5318e7c6f8f3492fcc0be7`.
Do not merge this revision with the supplied parent full result.

Selected state64 record has sixteen members, infrastructure4, civilian industry4, military industry5, capital-VP6521; province6521 maps to64.
Its provinceBuildings[6521] is empty and controller null in the parsed source record.
Neither absence means the runtime network lacks a node/controller; nodes have separate baseline map data and control is runtime state.
This is why static catalogue/model building dictionaries are not eligibility evidence.

Matching source hashes: supply_nodes.txt `cf80e9f359676b92f7bb60f00725b5fe3384339269567b461b728f97fd997abb`; railways.txt `86cc3fba40f39442bb4bf883a51740951c09073c5234e6b7b744d966fa2ee455`; state64 source `3bd06f88ba34dd9e81927820768fd3e90ec4532e3928552a34ff8b80b4666b6f`.
No state65/full topology extraction was duplicated.
The previous transport timeouts are historical; current source-map availability does not close runtime special-object/health proof.

## References, validation and completed boundary

Schemas for reference_context/search/read, source_lookup, map_inspect and script_validate were verified and called narrowly.
An overlong (>160-character) context question was corrected; it was an argument rejection, not service failure.
No successful route timed out in this task, so timeout/narrower retry was not triggered.
No broad event/helper graph, full map duplicate, native job or rewrite was used.
Context omitted Strategic region modding, Bookmark modding and Localisation; no corresponding editing occurs, GetID/GetName were targeted directly, and no full omitted-page coverage is claimed.

Exact native reference path: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, revision/SHA `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
Live reference_read sections: all_of1036-1051; any_of1515-1530; any_province_building_level1621-1642; meta_trigger6404-6423; non_damaged_building_level6554-6569; has_railway_connection4603-4627.
Direct ancillary sections: can_build_railway1884-1919, has_railway_level4628-4640, country has_damaged_buildings3684-3691, aggregate building_count1830-1840.
They do not state exact special-node/edge damage semantics.

Native `...\documentation\dynamic_variables_documentation.md`, revision/SHA `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`: province_controllers1042-1044 read through MCP; global/state inventory1042-1046,1096-1175 read locally, with no state-province built-in found.
Native `...\documentation\loc_objects_documentation.md:644-660`, revision `a5d06da0b42e615fa0c40d0103d9125ed68a7691778e20c0315aca7c82822c81`, proves State GetID/GetName.
Native `...\common\defines\00_defines.lua:25` documents MAX_EFFECT_ITERATION1000 for loop effects.
Native `...\common\buildings\00_buildings.txt:98-124`, raw SHA `9fa27d266f726de04c71311551698c6466257636dcc34d2573a3568d397bd539`, and separate map/supply/rail representation establish why special-object support cannot be inferred from a provincial cap alone.

Offline `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`: any_of1148, opaque state id1671, controller array1790 were read through reference IDs; all_of1150 was read in the relevant local section.
Offline `...\paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md:626`, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, proves raw GetID.
Offline `...\paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md:1836,1867`, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, supplies generic provincial/connection parallels, not special-node runtime proof.

Exact vanilla lookup: ENG_supply_for_tobruk_push, `game:common/ai_strategy/ENG.txt:3069-3079`, keyPath enable/452, revision `51dfe78c66fc13df21be2d4991dbe9eced8c7a1ad081df1b087c39ae91a9d10d`.
Active query is naval_base; supply_node is commented.
Raw ENG file SHA `f6fed5347c68ab2a3b79e4864dc5d72490c9cabe46a16e865932d2e5a37716d9`.
Direct ITA decision precedent `...\common\decisions\ITA.txt:6942-6955` proves multiple literal province IDs for ordinary bunker query, SHA `e3c582f0730af4b74196c00e825dff5fccc46db8eb2d8c9dbfb2fa8bcd21f76e`.
No AI weights were evaluated/changed.

Event028 ordinary classifier SHA `09b4da47a33e7373891a42d17c9c3da64784611c8ae598e3491ce9c125da7d37`.
Event028 provincial setter SHA `f75b6cda8d1f9cd3c003c63cb49805d1c303fa594884d1f2aef1c7c8f2aeb2d5`.
Its exact definition was read through bounded source_lookup, index revision `ef202621deca5bd7b6770ca33578744f8d5d9c4073298675cf301450255f840f`, with the complete local classifier/header checked through line 56.
These are local adapter boundaries, not confirmed negative engine-reader tests.

Bounded STATE script_validate on literal node query and numeric any_of/controller-index query returned SCRIPT_CHECK_PARTIAL / valid null / parametersChecked false.
Command kind and STATE context were recognized, but each native argument block remained unchecked.
Documentation DB revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
It cannot verify supply_node special-object support, dynamic meta body, generated geometry, health, path edges or native runtime behavior.
No helper/source fixture is written or declared implemented by this report.

Authority hashes: accepted full route `dc18ddb64f45b9634932e732cbcaa8bd3a4a9d10c997ef8f4e6703cff4a42b15`; final contract `85083446610d0cae9c8c52ce2afa829ab799a170c38dc9249557e9f171a3ef48`; accepted catalogue plan `78b022c51ca6305f0a00037c169e8376cb6ac5c8fd9548df11c84bb09cb02209`.
HEAD reading point `77ee68fabe686cfda74c225313a601971853aedf`, not an immutable whole-workspace baseline.

Completed: bounded source/reference/map feasibility and exact API/data/lifecycle contract for parent review.
Open: verified current special-node primitive, exact selected-node health, current whole-edge level/damage and computed-path introspection, parent catalogue/source/runtime acceptance and multi-component transaction proof.
No approved payoff is simplified; no stricter aggregate or static-node fallback is used.
Full runtime endpoint resolution and private commissioning remain incomplete at those exact capabilities.
