# Repo Explorer Handoff

## Scope read

- Parent task: Map existing Event012 sources for current African territorial control and world-relative African military strength, supporting the accepted Gods of Africa Strength fidelity repair.
- Explicit constraints: Read-only exploration; write only this report; no gameplay or other documentation edits, Git operations, game launch, rewrite tools, new recurring/world hooks, Agent Nudger writes, or ownership of country, Charter, or model packages.
- Explicit exclusions: The parent is repairing the separate Chaos normalization; I did not audit or alter it.
- Files and identifiers requested: The cited Gods of Africa strength helper, shared Africa state/control logic, country and state arrays, candidate census, host transfer lifecycle, formable registries, and the accepted full spec at lines 163-204.
- Skills and references read: AGENTS.md; chaos-redux-events; chaos-redux-subagents; the focused offline wiki sections for continent, ownership/control, scopes, and arrays; installed-game trigger, effect, and collection documentation.

## Primary findings

Parent follow-up on 2026-10-08: installed vanilla `common/collections/collections.txt:303–311` defines `states_in_africa` from `game:all_states` with an `operators.limit` of `is_on_continent = africa`.
It supplies an authoritative native geographic collection without a manually enumerated mod roster.
Installed `common/collections/_documentation.md:7–44,69–90` documents collection references and `every_collection_element`.
The symbol-based MCP lookup for `states_in_africa` returned zero indexed definitions at revision `f3e1e769183dcb6442bd21211ecd25b7d97d8cce1e70d0f933609f80786054fd`, so that result is an index-coverage gap rather than evidence that the collection is absent.
The exact vanilla definition was read locally, but its runtime membership/count and the next territorial numerator remain unverified.
The original explorer findings below remain its bounded historical read, including the absence of a mod-owned complete roster.

- The current helper has no current African territory input and no world-relative military denominator: it reads host division count plus optional war readiness, then uses industry, relationship count, charter authority, recognition, reach, technology, internal condition, and Chaos factors.
- Event012 has a usable state-level ownership/control pattern only inside selected action state arrays; it requires the state to be African, owned by the relevant country, and controlled by that same country.
- No complete Chaos Redux Africa state roster or shared world military total was found in the bounded searches.
- The host-owned Gods candidate census is the closest existing country roster for a world-relative military calculation, but it is not a military statistic and has exclusions and a host-succession caveat.
- Event012 hosts are not one fixed tag with guaranteed continent-wide cores. Eligibility is based on a current African capital, and core recognition grants host cores on selected members' currently owned African states.
- Required map MCP evidence did not return. The local continent source establishes the continent keys, not the current state membership, so no Africa state count or complete territorial denominator is claimed.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| common/scripted_effects/012_africa_gods_effects.txt | Defines gods_of_africa_refresh_strength and its existing military, industry, continent, and other inputs. | Lines 620-806; source_lookup revision 7e61ba4a48567d15340971d22075c0bd3aff0e2441d7167a4408a080a9cf2a5d. |
| common/scripted_effects/012_africa_effects.txt | Builds africa_cooperative_relationship_count from relationship categories and contains the closest current-state owner/controller filter. | Lines 1115-1119 and 1222-1249. The peace-exemption pass filters africa_action_state_targets by continent, is_owned_by ROOT, and is_controlled_by ROOT, then deduplicates state entries into member and host ledgers. |
| common/scripted_triggers/012_africa_triggers.txt | Defines who may host, how current host identity is bound, and which countries qualify as African relationship targets. | africa_is_eligible_host at 374-379; africa_is_current_host at 431-440; africa_is_valid_relationship_target at 581-594. These are eligibility gates, not continental state counts. |
| common/scripted_triggers/012_africa_gods_epoch_binding_triggers.txt | Defines the existing host-core participant check. | gods_of_africa_participant_owns_host_core_state at 68-72 checks any owned African state that is a host core; it does not require current control or cover all Africa. |
| common/scripted_effects/012_africa_action_effects.txt | Creates action-scoped state arrays and contains Event012's core-recognition mutation. | africa_create_action_record at 4435-4556 copies selected states to africa_action_target.africa_action_state_targets; the list is cleared on action completion/cancel at 8529 and 8651. africa_action.grant_core_recognition at 7320-7328 cores the host on every African state owned by that member, with no controller check. |
| common/scripted_effects/012_africa_world_order_effects.txt | Initializes the host-owned Gods candidate census. | africa_initialize_scramble_and_world_packages at 781-963 clears and rebuilds gods_of_africa_candidate_registry, then sets gods_of_africa_candidate_census_complete. Lines 902-914 retain ordinary country scopes from global.countries. |
| common/scripted_triggers/012_africa_gods_triggers.txt | Bounds candidate membership and prevents duplicate rows at insertion time. | gods_of_africa_candidate_is_valid and gods_of_africa_candidate_can_be_remembered at 121-140 require a global.countries member, exclude nonhuman/special Chaos/current-host countries, and bound rows by global.countries cardinality. Source_lookup revision b9b8f372251ff5554387041db715996195260f5220226cbadb7526a99b71081a. |
| common/scripted_effects/012_africa_gods_effects.txt | Owns participant and candidate insertion/cleanup behavior. | gods_of_africa_remember_candidate and gods_of_africa_try_register_participant at 470-495 add candidates and live participants through the host event target; gods_of_africa_clean_system at 4679 onward clears live participants but not the candidate census. |
| common/on_actions/012_africa_gods_on_actions.txt | Adds countries named by selected engine transactions to the candidate/participant path. | Lines 14-16, 88-113 cover government change, puppet/release, and peace-conference callbacks; the file explicitly says it has no recurring world scan. |
| common/scripted_effects/012_africa_host_transfer_effects.txt | Stages and restores host-owned rosters and action arrays during succession. | Candidate array staging at 683-747 and restoration at 439-507; the new host flag is set before the old candidate roster is copied back. |
| common/collections/chaosx_country_collections.txt and common/collections/006_independence_wave_country_collections.txt | Expose Africa-related country-tag views. | chaosx_country_africa, overlap, and current-map-bound views at 104-121 and 006 overlap views at 92-104 are country collections, not state or territory rosters. |
| common/scripted_effects/006_independence_wave_formable_registry_effects.txt and common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt | Contain regional/formable registry patterns. | The registry names West African, East African, and Southern African federation families at lines 358, 406, and 430; targeted searches found no whole-continent Africa state roster. |

## Existing patterns

africa_action_state_targets is an action ledger, not a geographic census. The host-side action record copies selected state scopes to the action target country, and the target list is used by action completion and the peace-exemption path. The peace-exemption path is the strongest existing source pattern for current held territory because it checks both owner and controller and deduplicates the resulting state scopes.

gods_of_africa_candidate_registry is a host-owned country-scope roster. Its one-time census walks global.countries and retains ordinary country objects, including minors, capitulated countries, and landless tags; it excludes the current host, nonhuman countries, and special Chaos countries. The candidate validity trigger does not require major or player status, while the separate live participant registry does.

The census builder is bounded by global.countries cardinality, not by a small fixed set. It is a retained roster rather than a cached military total, so using it for a current division denominator would still require reading current country strength over its entries or consuming a separate aggregate that was not found.

Host succession is a concrete denominator hazard. The successor receives africa_unifier_host before the old candidate registry is restored, and the restore loop copies the staged registry without filtering the successor. The targeted search found no remove_from_array path for gods_of_africa_candidate_registry; a post-transfer world sum that also adds the host separately could count the successor twice unless membership is revalidated.

Candidate membership is refreshed by the one-time host initialization and by transaction-bound calls to gods_of_africa_remember_candidate. The callbacks cover government changes, puppet/release events, and peace-conference completion; the code does not establish that every unrelated dynamically created country is registered.

gods_of_africa_participants is narrower still: it is the live participant array used for demands and recognized-major counting. The current strength helper counts recognition among those participants when they are marked major; that count is not African army power or total world power.

num_of_controlled_states appears in host-size and target-strength checks, but those uses are not filtered to Africa. The static chaosx_country_africa collections are tag inventories, not current state ownership/control collections. No common/geographical_regions or common/strategic_regions state roster was found.

The host core set is variable by country and history. Event012 accepts any country with an African capital as a host, and the core-recognition action grants host cores to African states owned by the selected member whether or not those states are currently controlled by that member. Therefore, host cores are not a safe proxy for current control or a complete Africa denominator.

## Vanilla or reference precedents

Vanilla common/scripted_triggers/ITA_scripted_triggers.txt at lines 293-329 groups East, West, Central, and Southern Africa by combining is_on_continent = africa with strategic-region IDs. This is a subregional precedent, not a complete continent roster; region 181 appears in both the East and South groups, so region-group sums require unique-state handling.

Vanilla map/continent.txt in the installed game contains the continent keys, and the mod has no map/continent.txt override. The file does not list Africa's member states, so it does not settle the map denominator.

Installed documentation read through the live reference routes: triggers_documentation.md lines 1318-1326 for any_controlled_state, 1612-1620 for any_owned_state, 6006-6014 for is_on_continent, and 6079-6087 for is_owned_and_controlled_by, all at revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae4953217a403386b2f6c85196aa0; effects_documentation.md lines 4296-4311 for for_each_scope_loop at revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af; and script_concept_documentation.md lines 60-81 for collections at revision 884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7.

Offline wiki sections read: Triggers - Hearts of Iron 4 Wiki.md lines 1847 and 1854 for is_owned_and_controlled_by and is_on_continent at revision abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06; Scopes - Hearts of Iron 4 Wiki.md lines 388-392 for owned versus controlled state scopes at revision 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49; Data structures - Hearts of Iron 4 Wiki.md lines 1069-1077 and 1217 for array ownership and scope iteration at revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4; and Effects - Hearts of Iron 4 Wiki.md line 120 for every_owned_state at revision 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c.

## Likely edit order for the parent

1. Resolve whether the intended territory contribution counts only states currently owned and controlled by the host, or also territory held by sovereign, autonomous, or subject members, and keep ownership separate from occupation/control.
2. Resolve the world-military denominator universe before reusing the candidate census, including the current-host row after succession and the intentional exclusion of nonhuman and special Chaos countries.
3. Obtain map_inspect and map_render evidence for the loaded Africa state/region boundary; the current offline file and source predicates do not establish the full loaded state roster.
4. After those inputs are settled, update the existing strength path in common/scripted_effects/012_africa_gods_effects.txt and validate its callers and refresh lifecycle. No new helper, array, recurring hook, or owner package is proposed by this handoff.

## Validation checks

- Re-run targeted searches for gods_of_africa_refresh_strength, africa_cooperative_relationship_count, africa_action_state_targets, and gods_of_africa_candidate_registry after the parent change.
- Verify any territory numerator checks Africa membership and the intended owner/controller relation, and ensure state entries are unique when combining host, member, project, or region rosters.
- Verify the candidate roster after host transfer and the intended treatment of nonhuman/special Chaos countries before using it as a world denominator.
- Retry narrow hoi4.event_inspect and hoi4.event_render evidence against the changed source revision, and retain helper coverage and unresolved findings separately.
- Retry hoi4.map_inspect and hoi4.map_render for continent/state membership before claiming map coverage.
- No tests or live-game checks were run by this read-only explorer; the user retains live-game validation.

## Risks and blockers

Confirmed source-derived risks:

- Core membership is not current control. The grant-core-recognition action can add host cores to member-owned African states without checking controller, while the Gods trigger uses host-core membership as an ownership gate.
- Sovereign member territory is not host-owned territory. Relationship counts and member-country counts cannot establish that Africa owns or controls a state's land.
- An occupied state can be owned by one country and controlled by another; the peace-exemption code's paired owner/controller check is the only reviewed current-control pattern in the requested Event012 files.
- Host transfer restores the candidate census without excluding the new host, so the roster is unsafe as a host-plus-world denominator until current-host membership is filtered or rebuilt.
- The candidate census omits nonhuman and special Chaos country objects, and registration of later country objects is tied to specific transaction callbacks.

HOI4 MCP evidence and route limits:

- hoi4.source_lookup returned source locations for the strength helper, census builder, candidate guard, action state list, core grant, and host trigger. The relevant source revisions are 7e61ba4a48567d15340971d22075c0bd3aff0e2441d7167a4408a080a9cf2a5d for effects and b9b8f372251ff5554387041db715996195260f5220226cbadb7526a99b71081a for triggers.
- hoi4.event_render returned EVENT_RENDERED_PARTIAL for chaosx.nr12.600 at graph revision 5b61a45d5836c19fd276ef8a5e51b000c91b28ce24b8158b45c373319843902d. The JSON artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87e1839b2ec267c6004ab6769351a20dbab4d622e78238da15a3108fd866ce77/3ff10825f862212d6cb0f4ae976c7b6c12df75ba14322a0991167c5cf034aae6/event-overview-5b61a45d5836.json and the manifest is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00328f95e741d6459ce44f029bc477738d8d83bdf41da1d757ff5281162cb5c4/7e757503a4d600963d6bce45c22ff4e7f2e5510ad6233ca60aa5aee13810f527/event-overview-5b61a45d5836-manifest.json.
- The selected event render contains chaosx.nr12.600 and unresolved helper africa_gods_of_africa_commit_activation, with expandHelpers = false and manifest complete = false. The helper is present in common/scripted_effects/012_africa_gods_effects.txt at line 4758, so the render's missing_helper finding is an active-catalog/focused-coverage limit, not proof that the source helper is absent. The result reports 46,253 omitted nodes, while the manifest's omittedNodeCount is 0; omission accounting is inconsistent.
- hoi4.event_inspect state_flow, trace, and lint calls did not return within bounded waits of 30, 20, and 20 seconds respectively. No inspect artifact or helper/lifecycle certification was returned.
- hoi4.map_inspect returned no result within 20 seconds for lookupOnly query continent africa and a second Africa query; hoi4.map_render for the continent layer returned no result within 25 seconds. No map artifact was returned, so source findings do not substitute for map evidence.
- hoi4.probability_inspect on the deterministic strength helper with adapter custom_weighted_pool did not return within 20 seconds. The helper is deterministic arithmetic, not an event chance, MTTH, random list, AI selector, or declared random pool; no probability audit is claimed, and the separate Chaos normalization was excluded.
- The connected tool inventory exposes hoi4.tech_inspect, hoi4.tech_render, and hoi4.tech_compare, but no separate Technology Tree Viewer tool. Technology is out of scope here, and standalone package availability is not established by the exposed routes.
- No separate HOI4 server-version/health endpoint appeared in the connected tool inventory. Source and reference calls returned status OK, and the event renderer returned a partial result; general service health is not claimed.

## Recommended next action

Before editing, the parent should settle the state-ownership/controller rule and the intended world-military universe, then obtain read-only map MCP evidence for the African state boundary. The candidate registry and action state arrays are useful bounded inputs, but neither is a complete, current continental territory or military total.

## Writes performed

Only this requested report was written. No gameplay, localization, GUI, asset, or other documentation file was changed; no dry-run, apply, post-validation, rollback, or recovery operation was performed.
