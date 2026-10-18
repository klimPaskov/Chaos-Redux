# Event 039 Country Activation and Rollback Audit

Date: 2026-10-07.

Status: read-only audit with actionable source findings. No gameplay files were edited, no commit was created, HOI4 was not launched, no logs were searched, and no map write was performed.

Two shared source files changed during this audit. I refreshed the country transaction ranges after observing those changes. Their current diffs are confined to character-safety code outside this audit scope. The hashes below identify the bytes reviewed at handoff time.

## Bounded coverage

- Reviewed central Assassin State selection, preflight, transfer, capital assignment, postconditions, rollback, starting forces, stockpiles, and opening technology grants.
- Reviewed foreign derivative selection, state transfer, subject binding, force setup, transaction rollback, inheritance eligibility, parent rebinding, and country-loss cleanup.
- Reviewed country-tag registrations, country definitions, dormant derivative histories, Event 039 on-actions, and the matching scripted triggers.
- Read the named specification portions in Parts 5, 6, 10, and 18. Current source takes precedence over dated handoffs.
- Duplicate state transfer and native state/capital effect scopes were checked. No duplicate state append or same-state transfer defect was found in the current scripted call chains.
- Focus, event, map, and technology MCP inspect/render calls did not return artifacts within the bounded waits. Their source-level conclusions below are not engine or map validation.
- The mandatory probability pass was delegated to chaosx_ai_probability_auditor. It returned an incomplete audit with scenario and MCP limits recorded below.

## Findings

### P1. Dynamic carriers lack the engine reservation required before their first state transfer

The central candidate is created with create_dynamic_country in common/scripted_effects/039_murder_mystery_integration_effects.txt:1757-1840. Its child effects save the candidate target and initialize the country. The first state transfer happens later, through commit_assassin_state_creation at integration_effects:1842-1852 and transfer_split_states_to_assassin_state at common/scripted_effects/039_murder_mystery_runtime_effects.txt:1592-1594. The creation block contains neither a state transfer nor reserve_dynamic_country.

The derivative carriers have the same ordering. create_derivative_carrier in runtime_effects:1735-1760 runs initialize_derivative_carrier inside create_dynamic_country, then start_derivative_creation transfers the anchor and neighbour states later at integration_effects:2025-2043. The Event 039 source files contain no reserve_dynamic_country call. The project flag murder_mystery_assassin_carrier_reserved at integration_effects:471 is a scripted flag, not the engine reservation effect. murder_mystery_assassin_candidate_is_reserved at common/scripted_triggers/039_murder_mystery_character_triggers.txt:27-40 validates a target and allocation generation, with no engine reservation effect.

Installed effects documentation says a dynamic country with no owned states must be reserved after creation, and then unreserved when no longer needed, at Hearts of Iron IV/documentation/effects_documentation.md:6367-6375. The offline Effects wiki also warns that a country created without a state transfer in its create_dynamic_country effect can cease to exist, at paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:916. Vanilla precedent in common/scripted_effects/INS_scripted_effects.txt:781-787 keeps reserve_dynamic_country and transfer_state inside the create_dynamic_country block.

The source therefore does not establish that either new country survives from allocation to the later transfer. A recycled or missing target can prevent activation or make the following ownership and postcondition checks operate on a stale candidate. Runtime behavior was not observed because live-game launch is out of scope.

Correction recommendation: apply the native reservation inside each country’s create_dynamic_country child block, or transfer its first state inside that block. Release the reservation only after successful ownership is established or rollback has explicitly retired the candidate, and verify the candidate identity immediately before transfer.

### P1. Derivative rollback returns land but does not prove or perform carrier retirement

rollback_derivative_transaction in runtime_effects:1839-1853 calls the state-return helper, sets murder_mystery_derivative_requires_parent_retirement, clears transaction flags, then clears murder_mystery_derivative_country_candidate. It does not annex the candidate, call reserve_dynamic_country = no, or verify that the carrier no longer exists. The marker is only written, never read, in current repository source.

revert_derivative_creation in common/scripted_effects/039_murder_mystery_lifecycle_effects.txt:981-998 calls rollback_derivative_transaction first. It clears derivative flags only if the candidate event target remains. The rollback helper has already cleared that target, so this cleanup branch cannot reach the candidate after an active transaction rollback. cleanup_transient_runtime invokes rollback_derivative_transaction directly at runtime_effects:2528-2532, which also clears the candidate target before its later target cleanup. A candidate that failed before registry commit is not present in the derivative arrays for reconcile_derivative_registry to retire.

The carrier selector only reuses a tag when no living country has the corresponding original_tag, at runtime_effects:1696-1729. The actual fate of a landless dynamic country after its last state is transferred away was not runtime-tested, so a persistent tag leak is conditional. The definite source defect is that rollback publishes setup_rolled_back without a country-retirement or tag-availability postcondition. The comment on start_derivative_creation promises that failure leaves no landless derivative, but the rollback call chain does not prove that outcome.

Correction recommendation: keep the candidate target through rollback, restore all moved states, retire or annex the candidate through a verified engine-supported path, clear its transaction and derivative identity state, and verify the original_tag is free before publishing rollback completion. Apply the same cleanup when transaction preparation rejects before the active flag is set.

### P1. Split and revolt preflights validate state counts and connectivity, not country viability

For the central split, select_assassin_state_cluster chooses a random owned and controlled neighbour of the host capital and grows a connected cluster using ownership, control, impassable, and non-capital checks at integration_effects:1689-1742. register_split_state prevents duplicate state IDs at runtime_effects:1513-1525. validate_split_state_registry checks cluster size, a state-count remnant, share by count of controlled states, and anchor membership at runtime_effects:1531-1560. The post-transfer check compares state counts and verifies a capital in the transferred array plus one live state for the host at integration_effects:1861-1892. host_has_live_state only requires a controlled owned state at runtime_triggers:89-95.

The candidate filter does not score or require population, factories, resources, a supply node, railway access, port access, or a viable defensive route. minimum_anchor_quality is declared at common/script_constants/039_murder_mystery_constants.txt:548 but no use was found. The split preflight counts state share rather than viable core territory. refresh_split_preflight sets the requested share to the 15 percent minimum at lifecycle_effects:752-765.

Foreign revolts have the same gap. country_can_lose_revolt_cluster only requires more than two controlled source states and basic country eligibility at common/scripted_triggers/039_murder_mystery_lifecycle_triggers.txt:41-52. start_derivative_creation transfers one random non-capital anchor plus one neighbour, as cluster_extra_states is 1, at integration_effects:1970-2045. The postcondition only calls host_has_live_state for both countries at integration_effects:2047-2059. A three-state source can be left with only one state, while the new derivative can receive two low-capacity states.

The force package adds minimum divisions and fixed opening stockpiles from state counts, not population, factories, host force size, or supply quality, at common/scripted_effects/039_murder_mystery_forces_effects.txt:54-95 and 114-156. Part 6 requires population, industry, supply, and a realistic route to fight for both sides at spec_part_6_assassin_state.md:40-71. Part 5 requires the foreign revolt to have a viable capital, sufficient population, industry or a bounded grant, supply access, and a viable remnant at spec_part_5_international_network.md:152-165.

Correction recommendation: preflight candidate and remnant states using actual population, industry, supply, and route features. Recheck both country packages after transfer and before capital/core/force setup commits. Reject, shrink, or reselect the cluster when either side fails. Tie force counts and emergency stocks to those validated inputs.

### P1. Territorial heir eligibility admits a one-state, low-capacity derivative

murder_mystery_country_is_valid_heir in common/scripted_triggers/039_murder_mystery_lifecycle_triggers.txt:73-83 requires an existing derivative, no loss/detachment flags, no capitulation, at least one owned state, and Cohesion of at least 20. Those thresholds are constants at common/script_constants/039_murder_mystery_lifecycle_constants.txt:191-202. select_territorial_heir then ranks eligible candidates by state count, capped factory count, and Cohesion at lifecycle_effects:1846-1882. Industry contributes to ranking, but the trigger has no minimum industry, population, supply, controlled capital, mature-network, or incompatible-subject check.

install_territorial_heir converts the selected country into the central actor at lifecycle_effects:1887-1932. It ends a puppet relationship only when the heir is still a subject of murder_mystery_defeated_central at lines 1891-1896. A derivative with one owned state and Cohesion 20 can therefore pass without the Part 5 minimum industry, population, and supply proof, and the eligibility gate does not exclude an incompatible subject relationship.

Correction recommendation: add fail-closed population, industry, supply, controlled-territory/capital, current movement-parent, and subject/terminal-ownership conditions before ranking. Revalidate those same conditions immediately before installing the heir.

## Verified transaction details

Central split states are deduplicated before append with is_in_array at runtime_effects:1513-1525. The derivative attempt clears its transfer array, adds one anchor, and visits the anchor’s neighbours once at integration_effects:1967-1977 and 2025-2045. Rollback returns the recorded array and clears it in return_derivative_transfer_states at lifecycle_effects:965-977, so the second call from revert_derivative_creation sees an empty array. No duplicate transfer defect was found in the source call chain.

Both split selectors exclude the current capital. The central candidate takes the selected anchor as its capital after transfer at integration_effects:1854-1857. No current call path transfers the host capital in the reviewed split. Population is carried with whole-state ownership changes. No separate population debit or credit effect appears in these transactions.

Actual winner scope handling is consistent with the documented callbacks. on_capitulation uses ROOT for the capitulated country and FROM for the winner, while on_annex uses ROOT for the winner and FROM for the annexed country. The Event 039 handlers save that actual winner at common/on_actions/039_murder_mystery_on_actions.txt:36-80. record_case_owner prefers that winner when it is not a movement country at lifecycle_effects:1153-1170. The local derivative_parent_government field intentionally records the government a derivative rose against. The separate derivative_parent_entries array records its movement patron and is rebound to the new center at lifecycle_effects:1936-1967. I found no wrong-ROOT inheritance defect in this path.

Country-loss cleanup calls decision_cancel_bound_objectives through cleanup_country_runtime at runtime_effects:2493-2508. The shared helper clears objective context and removes the active Event 039 missions at common/scripted_effects/039_murder_mystery_decision_effects.txt:298-330. The failed derivative candidate cleanup gap remains because that candidate has not entered the derivative registry.

AXS is registered and has both a country definition and an inert 1936 history template. AXT, AXU, AXV, AXW, AXY, and AXZ also have inert dormant history files. Their runtime setup is supplied through create_dynamic_country effects.

## MCP evidence and limits

The live server status resource reported HOI4 Agent Tools version 3.10.0, stdio transport, and workspace mod_chaos_redux_ea3b2d67c2c0. Reference context, search, read, and source_lookup schemas were exposed. The event, focus, map, technology, and probability routes were also exposed. I did not invoke helper_expansion, job tools, or native tasks, so client task negotiation was not applicable.

Reference context succeeded for event, map, and general surfaces. Reference search/read retrieved installed and wiki evidence for transfer_state_to, transfer_state, set_capital, annex_country, is_owned_and_controlled_by, state_population_k, on_capitulation, and on_annex. Search for create_dynamic_country/reserve_dynamic_country returned the offline Effects wiki sections at lines 913 and 916, revision 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c. The matching reference_read calls did not return within the bounded wait, so I read those local lines directly. The installed effects documentation locally states the reservation rule at lines 6367-6375. The technology reference_context call did not return, so the local Technology modding wiki sections were read directly. The installed documentation folder has no standalone technology-mod documentation file.

source_lookup succeeded for runtime_effects line 1831 and identified the active, unshadowed rollback effect at MCP source revision 1a44f0a4fe6809f81cda0fd58888a6d525de9412b3767d3850f8136e932262c2. Its location query returned no full definition body. The later symbol-based lookup did not return.

The full event state_flow request for selector chaosx.nr39.1, the narrower event trace, and event state render did not return graph artifacts after bounded waits of approximately 1.5 to 4 minutes. Focus inspection of murder_mystery_assassin_focus_tree and its exact source path, plus a cropped opening-focus render, also did not return artifacts after approximately 3 minutes. Map inspection with overview and a state query did not return after approximately 3 minutes. The map render at scale 0.12 was rejected because the connected schema requires an integer scale. The corrected state render at scale 1 with state-buildings, supply-nodes, railways, and adjacencies did not return an artifact after approximately 3 minutes. Technology trace for murder_mystery_clandestine_combat_training and its dependency render did not return artifacts after approximately 3 minutes. These are unresolved engine/map coverage limits, not negative validation results.

The standalone Technology Tree Viewer was checked separately from route exposure and service health. No matching viewer was found in registered Start apps, running processes, or repository tools/docs. Record standalone viewer availability as a package gap. The exposed MCP technology routes do not establish a standalone viewer.

chaosx_ai_probability_auditor returned an incomplete read-only pass. The submitted strategy scenarios were EVT039_CENTRAL_VS_ORIGINAL_HOST and EVT039_DERIVATIVE_VS_SELECTED_SOURCE. The strategy inspection found no probability pool and classified the two add_ai_strategy entries as scores. Its reported source hash was 2ed8dec83a731a06176bb77bccd8907fd906f42b1bbcdeb834ee5caa19a95c18, which does not match the local forces_effects SHA-256 below. The auditor could not correlate that source identity to local bytes, so the strategy inspection does not establish current-file behavioral evidence. The strategy evaluation remained pending when the auditor stopped.

For chaosx.nr39.40, the complete local option pool is .40.a at base 100 and .40.b at base 0. Option B is available only to the human original host when the target and switch flags are valid. The scenarios were EVT039_40_AI_ACTIVATION and EVT039_40_HUMAN_SWITCH. For .23, .24, and .25, each event has one local option at base 100. The .23 scenario was EVT039_INHERITANCE_PENDING. The .40 and .23 inspections/evaluations timed out after 600 seconds. .24 and .25 were not individually evaluated. Event scenarios had empty state maps, so their global flags and typed scope bindings remained unmodelled. These source weights do not provide an MCP-certified probability.

The seven Event 039 technology candidates each use base 3 and a factor of 2 when at war. The named scenarios were EVT039_CENTRAL_PEACE, EVT039_CENTRAL_WAR, EVT039_DERIVATIVE_PEACE, and EVT039_DERIVATIVE_WAR. The technology probability inspection found seven candidates and poolComplete = false. The full national research pool and external research factors were not included. State maps, researched-tech prerequisites, and route flags were unbound. The candidate source hash 8ebf556510025398616206214766ef1afdb3c0f7272f25f2e63a7d67586e5639 matches the local technology file SHA-256 below. The corrected peace/war evaluations timed out after 600 seconds. The central setup grants the first three technologies. The derivative setup grants only murder_mystery_clandestine_combat_training.

No normalized event-option or research probability, rank, dominance, starvation, or rank reversal is certified. The strategy inspect did not model resulting AI behavior. No probability comparison was applicable because this audit made no source change. Useful inspect artifacts:

- Strategy inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cfe31037bcae1df48a762b8e1b22b643ea55df3bbc4ec583dea420fbb70b1130/ee8db71de0a1ab5dfa5272092d516d77abcc0754c695fb7cc98ba98a22be6224/probability-inspect-2ed8dec83a73.json
- Technology inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8f5b44dc29f42d502d28d953c32c46759083b35c33514f97bd8ca345fc406ab4/639848fbd9021d0559a3b9b4e9532e4f5f76439b1389575e671bcd16bab0180f/probability-inspect-57cf5f7d35a2.json

## Current source versus 2026-10-03 evidence

The handoff capture_inheritance_repair_architecture_2026-10-03.md at line 72 describes the earlier inheritance path as same-country leader replacement and says it did not scan derivative rows. Current source has select_territorial_heir, install_territorial_heir, and derivative rebind helpers at lifecycle_effects:1846-1967. The older line finding is superseded and was not treated as current behavior. Its MCP timeout notes also do not describe the current server, which returned live reference and source-location results. The current event/focus/map/technology graph calls in this audit remain unresolved as stated above.

The probability auditor observed integration_effects hash C9A895347AEE8DF9532AA061D39D58A085A961F71B8469B5385F338BD51157FB at its read time and reported two different HEAD reads for that path. The hash table below records my final local worktree bytes after refreshing the transaction ranges. The auditor's technology candidate hash matches the local technology file. Its strategy-inspect hash does not match the local forces file, so that surface remains unresolved.

## Current byte hashes

These local SHA-256 hashes identify the source and spec bytes reviewed at handoff time. The two modified effect files include concurrent character-safety changes outside this audit scope.

| File | SHA-256 |
| --- | --- |
| common/scripted_effects/039_murder_mystery_runtime_effects.txt | 39AC5EBAB51C69A5B830FBD046BF5EB4A2D94B3C11CE208E5C69E59240BD3FCD |
| common/scripted_effects/039_murder_mystery_integration_effects.txt | 8637B23CB3B6BA35757FCAAEF1E63DDF5E110F204CC5C43FE1F1ABD0990C4D87 |
| common/scripted_effects/039_murder_mystery_lifecycle_effects.txt | 80B75B7C234F2F9C6DFE86511BC9128E101E584F9D3CB9FC94080E04EDA9748A |
| common/scripted_effects/039_murder_mystery_forces_effects.txt | 25E116FE0ADCD162A1EB0A327954D59B6E6340082AC7DF6EE32BB20C7A816573 |
| common/scripted_effects/039_murder_mystery_decision_effects.txt | 04349424CB60F9F989C4B72BD253FCE36631B214D8E4D6B0EBDF900523176DF2 |
| common/scripted_triggers/039_murder_mystery_runtime_triggers.txt | 8DF841A6BC23A8C2A63611AA9A487554CADBAD716528F79483C281DD9EE85DCD |
| common/scripted_triggers/039_murder_mystery_integration_triggers.txt | 9CFEAFDBFDA9FD76301C3B72031A8BFD3F1BAC9EE66471DDE52927BFAC376274 |
| common/scripted_triggers/039_murder_mystery_lifecycle_triggers.txt | 9BF8CD5361D51E50E744823CB23508E3FFDEBE4314E27930DA075F3920F62E8C |
| common/scripted_triggers/039_murder_mystery_character_triggers.txt | E4ADD526F07512119F21851C5A876A2E67725806B815CF516557816F9834A7C6 |
| common/on_actions/039_murder_mystery_on_actions.txt | 70B3F30B70546F10A96197B7A15FEEC9575EC7DFF412770DF70FB8760C7E1088 |
| events/039_murder_mystery.txt | 749105E395578F57F0AF0C9937D593DC252495D920D05DD568A8611AA3661892 |
| common/technologies/039_murder_mystery_assassin_technologies.txt | 8EBF556510025398616206214766EF1AFDB3C0F7272F25F2E63A7D67586E5639 |
| common/national_focus/039_murder_mystery_assassin_focus.txt | C8745925AD30762DABC7C50BC892D13A099E51A73B09266425402054B46E0D26 |
| common/country_tags/039_murder_mystery_countries.txt | DDDF7C2F5CC86D68791DA7FEDC131A7569FD25A2AFAD57412C384F7502051FBD |
| common/countries/039_murder_mystery_assassin_state.txt | 607728442A3352DA7299C8BAAA0F69C0C68EA9E37C6A21090E26F96638754B0D |
| common/countries/039_murder_mystery_derivative_state.txt | FF180B2B1B756D84F28A0929CB1EBD1AC2E719F62EE6EC3D77C0FE82776EEDE6 |
| history/countries/AXS - Murder Mystery Dormant Template.txt | 83BE80E68B2F3AD5C8AF5960BFB49DB587C1BACF2814361284661B012861B75F |
| common/script_constants/039_murder_mystery_constants.txt | 20985F34CD430782AAD1FE917145949DCF5E5658453B5494182599F56ABA02B6 |
| common/script_constants/039_murder_mystery_lifecycle_constants.txt | B342957B6451900482E79091B54B7B7A079CF83AFDCC13100E3323CB4B0963DA |
| common/script_constants/039_murder_mystery_forces_constants.txt | 9F24BA5096644BF6AD43D22E943708C63665424850C7E5E6E72D410CA18E89FA |
| history/countries/AXT - Murder Mystery Dormant Template.txt | DF1EDB93F6D8FFA315CA8F51DD0CBD62CF2C62E0D5B9EAFA022CE3DA58860B38 |
| history/countries/AXU - Murder Mystery Dormant Template.txt | 735FC89A267581206827E4407C68A80DD6CE35DDF16F8B7BDB98CDD41D655758 |
| history/countries/AXV - Murder Mystery Dormant Template.txt | BA7386F0FB8359621868737038D3789DDD7268843BD895407FD20F164EECAA35 |
| history/countries/AXW - Murder Mystery Dormant Template.txt | 54F689E811B4354CE1C07B35A2A440B8993106B4E8C327D4872AC196D544D5A6 |
| history/countries/AXY - Murder Mystery Dormant Template.txt | 266A96FD04B527C8B9A82817FC20BEF3528246C2661B03958E65FEEC20187D54 |
| history/countries/AXZ - Murder Mystery Dormant Template.txt | 6359B8AE89326FEDEB25551194E51A8AD6A81F5AD27E6E80FED5CA247AF588A4 |
| docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_5_international_network.md | AAFE40079A6B287FD086FC1872DA45FAC55B50854DC17DE30DEAFE46FF404E52 |
| docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_6_assassin_state.md | 4A8386D66AFF165D09AE9A047BEF4F4B295C378FF72D78BF03B1EF403A0AC60A |
| docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_10_world_end.md | 9AB5207F06C5D40609164D724A949C507CBC9E63145308E9B363E6921DCDD5F8 |
| docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_18_acceptance.md | 916C0B169F69EF10A081E3FDE0704A8AC7DC1E7D319310298A79533A556E3428 |

Reference citations and revisions:

- Installed effects documentation, transfer_state_to lines 8332-8347, set_capital lines 6655-6668, annex_country lines 2495-2498, and set_technology lines 7805-7818. Revision 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF.
- Installed effects documentation, reserve_dynamic_country lines 6367-6375. The same installed documentation file revision is 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF.
- Installed triggers documentation, is_owned_and_controlled_by lines 6079-6087. Revision 7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29.
- Installed dynamic variables documentation, state_population_k lines 1168-1171. Revision 538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA.
- Offline Effects wiki, create_dynamic_country lines 916 and 1020-1029, and reserve_dynamic_country line 913. Revision 997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C.
- Offline On actions wiki, on_capitulation line 254 and on_annex line 257. Revision 6822ADC85A374A1C1364F2DEF6F32C6D66DA9FB0280319DDD6AF4B84B33D882A.
- Installed on-actions documentation, Diplomacy/War lines 30-49. Revision 876BE96CAB02A3EAA9A133891BEA5F963F8980AA4A794F759C1B30F87D2663C4.
- Offline Technology modding wiki, technology grant lines 78-79, unlocks lines 146-170, and AI weighting lines 331-354. Revision C5428838DB20C4C812C66AFF82CBAFC58DB3B73453C30436BCE0D97436170BEE.
- Vanilla common/scripted_effects/INS_scripted_effects.txt lines 781-787 reserves the dynamic country and transfers a state inside the create_dynamic_country block. SHA-256 7152B2E9DD2FBC68B36AAEB7975FE1DA3E7DE2E766B61EFD0DB1EAA16E4C1CE7.

Skills used: chaos-redux-subagents, chaos-redux-events, chaos-redux-focus-trees, chaos-redux-state-ledgers, and chaos-redux-decisions-missions. The delegated probability auditor also read chaos-redux-mtth while checking for weighted timing surfaces. No skills were created or changed.
