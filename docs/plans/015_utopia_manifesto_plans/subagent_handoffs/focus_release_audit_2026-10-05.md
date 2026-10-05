# Event 015 Utopia Focus Release Audit

Date: 2026-10-05.

Disposition: implemented for the bounded focus-tree navigation and focus-localisation patch; release evidence remains unresolved until the current HOI4 MCP focus inspection, render, and probability baseline return.

Accepted design basis: the Event 015 planning package identifies itself as the accepted design and provenance package in docs/specs/015_utopia_manifesto_specs/README.md. Its route contract is docs/specs/015_utopia_manifesto_specs/matrices/focus_route_matrix.md and docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_3_focus_tree_architecture.md. The parent explicitly authorized the Common Provision terminology update and accepted the bounded shortcut addition on 2026-10-05. This patch adds no route family or country identity.

## High-priority findings

1. Current focus MCP evidence is blocked. The parallel hoi4.focus_inspect and hoi4.reference_context request remained pending for more than six minutes and its wrapper was stopped without a result. A separate hoi4.focus_render request for utopia_manifesto_tree remained pending for more than 90 seconds and its wrapper was stopped. The focus routes are exposed in the live tool inventory, but no current artifact, revision, diagnostics, or render was returned. The inventory has no separate hoi4.focus_lint endpoint; focus_inspect is the only exposed focus diagnostics route. Source checks below are not equivalent to current MCP evidence.

2. Focus AI probability evidence remains unresolved. The read-only chaosx_ai_probability_auditor owns the Event 015 focus baseline and was asked to use the complete available-focus pool for scenarios 015_minor_peacetime_1936, war_shortages, and constrained_route. Its current probability MCP inspections have timed out after the server's 600-second limit. No scenario results, candidate-pool completeness report, artifact, ranking, sweep, or probability comparison is available. This patch changes no ai_will_do block or weight, so no weight comparison was applicable.

3. The current source parser finds 34 reciprocal mutual-exclusion pairs, or 68 directed references, while the prior 2026-08-05 focus rules handoff reports 27 pairs and 54 directed references. Every current reference resolves to a focus ID, and all pairs are reciprocal. This appears to be an audit-count discrepancy, not a confirmed route defect; reconcile the historical handoff against a fresh focus_inspect result when the route returns.

4. Five focus titles exceed 30 characters and may need tile-fit review: utopia_manifesto_good_place_that_admits_its_limits, utopia_manifesto_six_hours_and_the_evening_lecture, utopia_manifesto_convene_the_interpretive_congress, utopia_manifesto_voluntary_commonwealth_league, and utopia_manifesto_council_property_transition. No current focus render exists to establish clipping, so I left the titles unchanged.

## Route coverage

All families promised by the accepted focus route matrix are present in the 124-focus source. This is source coverage; dynamic availability and current visual readability remain unconfirmed by MCP.

| Required family | Implemented anchors and payoff | Source status |
| --- | --- | --- |
| Recovery and survey | Recover the Manuscript, A Public Edition, Count Houses and Hands, The First Common Store, Agriculture for All, Convene the Interpretive Congress, An Interim Charter, The Country as a Question, Survey What We Lack, and Survey Domestic Alternatives | Covered |
| Consent of Households | Household Gives Consent, Free Callings, Municipal Charters, Cooperative Land Trusts, Constitution of Provision, Voluntary Commonwealth League, Commonwealth by Consent | Covered |
| Common Table | Nothing Private in Necessity, Councils of Callings, The Common Table, Social Workshops, Council Property Transition, Delegates Under Recall, Congress of Communes, Council Autonomy or Emergency Central Plan, Union of Tables | Covered |
| Guardians of Measure | Country Measured, Standard Houses, Tables of Need, Board of Measure, Shortage Forecasting, Cities in Series, Useful Freedom or Exact Obedience, Perfect Measure | Covered |
| Closed Island | One Island One Measure, Households of Service, The Closed Store, Penal Works, Auxiliary Contracts, Assigned Colonies, Cut the Channel, Perfect Island | Covered |
| Hidden revision route | Read Island as a Mirror, Institutions That Can Be Left, A Mixed Commonwealth, Sunset Clauses, Satire in Government, Public Audit, Reform Without Paradise, Good Place That Admits Its Limits | Covered; reveal conditions retained |
| Callings and education | Every Hand Knows the Soil through A Nation of Many Skills | Covered |
| Common stores | The First Common Store, The Capital Store, Regional Storehouses, Rotate Old Stores, Release Emergency Stores, Two Years Against Hunger, Surplus Beyond the Shore | Covered |
| Garden settlements | Homes Near Work, Rail Road and Common Ground, A Ring of Social Cities, district roles, and A Commonwealth of Places | Covered |
| Island project | Choose the Island, The Existing Island, The Archipelago Network, The Leased Island, The Coastal Refuge, The Inland Island, Build the Island, The Island Made Real | Covered; all five variants present |
| Defense | The Citizen Watch, Engineers Before Generals, A Small Army Well Housed, No Glory in the Field or Necessary Victory, auxiliary lifecycle, Commonwealth Defense Compact | Covered |
| Foreign commonwealth | Show the Stores, Offer the First Surplus, Houses Across Borders, A League of Small Places, Common Reserve Council, Mutual Defense Without Mastery, The Regional Commonwealth | Covered |
| Necessary Ground and stewardship | Survey What We Lack, peaceful offers, Ground Held in Trust, The Limit of Need or The Natural Right, The First Associate, stewardship, Charter Period, Status by Consent | Covered |
| Crisis correction | The Founding Crisis, Restore Consent, Empower the Councils, Give the Surveyors Authority, Seal the Island, Admit the Book Was a Question, A Settled Interim Charter | Covered; crisis corrections remain mutually exclusive |
| Formation and mature play | Proof of the Commonwealth, The Regional Proclamation, Integrate the Ring, The Second Generation, A Rule for Need, Beyond the Founder's Island, The Commonwealth at War, Plenty in an Age of Chaos | Covered |

No required route family or island variant was missing, replaced by a fallback, or simplified in the reviewed focus source.

## Missing or simplified content

No missing focus route, omitted island variant, or focus-tree fallback was confirmed against the accepted route matrix. This source-level result does not close the blocked MCP or probability evidence above.

## Focus patch and route behavior

The changed gameplay file is common/national_focus/015_utopia_manifesto_focus_tree.txt. It retains all 124 existing focus IDs, prerequisites, mutual exclusions, focus rewards, route flags, and AI weights. The source patch adds 11 top-level navigation shortcuts for Foundations, Political Routes, Callings and Schools, Stores and Neighbors, Garden Cities, Island Project, Defense, Necessary Ground, Crisis, Formation, and Revision.

Before the patch, the tree had no shortcut entries. The prior normal-scale render described bounds across roughly 60 columns and 17 rows, so players had to pan manually between spatially separated branch families. After the patch, each shortcut targets an existing branch anchor. The Crisis shortcut appears only while utopia_manifesto_constitutional_crisis is set. The Revision shortcut uses the same reveal trigger as Read Island as a Mirror: utopia_manifesto_can_reveal_joke_understood or utopia_manifesto_crisis_corrected_by_revision. No route gate, prerequisite, completion reward, or candidate AI score changed.

The 11 shortcut identifiers are utopia_manifesto_navigation_foundations, utopia_manifesto_navigation_political_routes, utopia_manifesto_navigation_callings, utopia_manifesto_navigation_stores_league, utopia_manifesto_navigation_garden_cities, utopia_manifesto_navigation_island_project, utopia_manifesto_navigation_defense, utopia_manifesto_navigation_necessary_ground, utopia_manifesto_navigation_crisis, utopia_manifesto_navigation_formation, and utopia_manifesto_navigation_joke_understood.

The shortcut targets use existing focus icon assignments; no icon IDs, GFX definitions, or textures changed. The offline wiki shortcut schema and the vanilla Germany and Persia shortcut blocks expose name, target, scroll_wheel_factor, and optional trigger, with no authored icon parameter. All target focus sprite definitions and texture paths resolve in source. Whether the native controls display the target icon as intended remains a render-only check.

The parent authorized replacing player-facing Commonwealth Ledger with Common Provision and generic ledger wording with contextual provision wording. The parent also asked for concise focus descriptions and requirement summaries. I shortened overlong island, formation, and resource-gate prose while retaining the route, site, manpower, equipment, political-authority, and formation requirements. The text auditor additionally identified receipt/record terminology; the focus localisation now has no visible ledger, receipt, or record terms. Internal script identifiers were not changed.

## Icon coverage

| Surface | Coverage |
| --- | --- |
| Focus blocks | 124 of 124 have an icon assignment |
| Unique focus sprite IDs | 74 |
| Missing sprite definitions or texture files | 0 |
| Highest repeated icon use | 4 focuses |
| Shortcut targets | 11 existing focus targets; no new art or GFX registration |

The most repeated focus icon families are GFX_goal_utopia_assemblies, GFX_goal_utopia_auditors, GFX_goal_utopia_settlement_charter, and GFX_goal_utopia_ring_councils, each used four times. This is a visual-variety risk rather than a missing-asset defect. The focus render must review whether those repeats remain legible in their current branch context.

## Localisation and reward mismatches

The source audit found title and description keys for all 124 focus IDs, no duplicate focus-localisation keys, and all 110 custom focus-tooltip references in the Event 015 English localisation. No title-to-reward or requirement-to-availability mismatch was confirmed in the source review. The bounded wording edits changed these 36 existing keys:

- utopia_manifesto_recover_the_manuscript_desc
- utopia_manifesto_transparent_store_accounts_desc
- utopia_manifesto_congress_of_communes_desc
- utopia_manifesto_penal_works_desc
- utopia_manifesto_rotate_old_stores_desc
- utopia_manifesto_release_emergency_stores_desc
- utopia_manifesto_choose_the_island_desc
- utopia_manifesto_the_archipelago_network_desc
- utopia_manifesto_the_leased_island_desc
- utopia_manifesto_build_the_island_desc
- utopia_manifesto_the_island_made_real_desc
- utopia_manifesto_show_the_stores_desc
- utopia_manifesto_proof_of_the_commonwealth_desc
- utopia_manifesto_the_second_generation_desc
- utopia_manifesto_cooperative_land_trusts_available_tt
- utopia_manifesto_commonwealth_by_consent_available_tt
- utopia_manifesto_perfect_measure_available_tt
- utopia_manifesto_households_of_service_available_tt
- utopia_manifesto_cut_the_channel_available_tt
- utopia_manifesto_perfect_island_available_tt
- utopia_manifesto_reform_without_paradise_available_tt
- utopia_manifesto_good_place_that_admits_its_limits_available_tt
- utopia_manifesto_six_hours_and_the_evening_lecture_available_tt
- utopia_manifesto_the_capital_store_available_tt
- utopia_manifesto_the_leased_island_available_tt
- utopia_manifesto_build_the_island_available_tt
- utopia_manifesto_the_island_made_real_available_tt
- utopia_manifesto_the_citizen_watch_available_tt
- utopia_manifesto_commonwealth_defense_compact_available_tt
- utopia_manifesto_mutual_defense_without_mastery_available_tt
- utopia_manifesto_ground_held_in_trust_available_tt
- utopia_manifesto_the_first_associate_available_tt
- utopia_manifesto_the_charter_period_available_tt
- utopia_manifesto_proof_of_the_commonwealth_available_tt
- utopia_manifesto_the_commonwealth_at_war_available_tt
- utopia_manifesto_plenty_in_an_age_of_chaos_available_tt

The 11 added shortcut localisation keys are utopia_manifesto_navigation_foundations, utopia_manifesto_navigation_political_routes, utopia_manifesto_navigation_callings, utopia_manifesto_navigation_stores_league, utopia_manifesto_navigation_garden_cities, utopia_manifesto_navigation_island_project, utopia_manifesto_navigation_defense, utopia_manifesto_navigation_necessary_ground, utopia_manifesto_navigation_crisis, utopia_manifesto_navigation_formation, and utopia_manifesto_navigation_joke_understood.

No icon ID or focus title key changed. The current focus localisation is UTF-8 with BOM.

## Layout and lint findings

The source inventory found no focus coordinate collision, unresolved prerequisite, or prerequisite-only unreachable node. The prior 2026-08-05 MCP report measured zero connector crossings, node intersections, long connectors, duplicate coordinates, and same-row spacing violations. Focus-node coordinates did not change in this patch, but those prior results do not validate the new navigation controls. The current focus_inspect diagnostics route did not return, and no separate focus_lint endpoint is exposed.

## AI behavior gaps

Every focus retains an ai_will_do block, a completion_reward block, and search_filters. The five political route openers use route-preference and route-avoidance scripted triggers. The prior focus rules audit counted 12 route/state AI plans in common/ai_strategy/015_utopia_manifesto_ai_strategy.txt. These are structural facts, not evaluated probabilities; the required baseline scenarios remain pending with the probability auditor.

## Idea lifecycle

The three opening idea additions use family-stage guards. Route and property ideas are delegated to the shared country lifecycle helpers rather than directly removed or stacked by the focus nodes. Source hooks were found; no save-state or live campaign behavior is claimed.

## Country identity and formation hooks

The focus route openers set their route and call utopia_manifesto_commit_current_route_identity; that helper applies the route property settlement and matching institution identity. The formation proof focus checks utopia_manifesto_can_form_current_route and unlocks the formation decisions. Final cosmetic identity and leader changes remain with the identity helper and decision-owned formation flow. No missing focus-to-formation hook was identified; decision execution and country package outcomes remain with their owning audits.

## Source-level validation and skipped evidence

A one-off static source inventory after the edits found 124 unique focus nodes, 126 resolved prerequisite references, no prerequisite-only unreachable nodes, 34 reciprocal mutual-exclusion pairs, no coordinate collisions, and 124 AI, reward, and search-filter blocks. It also found 74 focus sprite IDs with no missing definitions or textures, 124 title/description pairs, 110 resolved custom-tooltip references, and 11 shortcut targets with matching localisation keys and scroll factors between 0 and 1. The focus localisation contains no visible ledger, receipt, or record terms.

These checks are source parsing and file-reference checks. They do not establish native tooltip fit, icon presentation, current shortcut pan/zoom, focus availability under live state, or AI selection probability.

The current MCP focus inspection and render were skipped after the calls remained pending for the durations stated above. The separate focus_lint route is absent from the tool inventory. The focus_rewrite route was not used because this patch did not rewrite node positions, prerequisites, or route architecture; the shortcut declarations were added directly from the documented native schema and vanilla examples. The AI probability baseline is pending with its owning read-only auditor.

## Prior MCP artifacts and current limits

The prior 2026-08-05 handoff, docs/plans/015_utopia_manifesto_plans/subagent_handoffs/focus_rules_audit_2026-08-05.md, reported a clean node layout with 124 focuses, 126 connectors, and zero crossings, node intersections, long connectors, duplicate coordinates, or same-row spacing violations. Its inspect revision was c116a01172f19a36d786b4e3c3d43e02284132a10071a828ee8a5e3ca823392b and layout hash 702d82bb13bd4d319eb0836bdbb093280b9bb8b53e6f77d40096f68affc8cbb5.

Prior inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d6de65be7b35785951ea80903be350ee66409d05f9fb033fbbaed0f3f534df1/c2148d7174e0dbf0eeb59c959e0f6be0a5d982ad2f1ee72191ad0079c542864c/focus-inspect.c116a01172f19a36.json.

Prior render HTML: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6d6fc0e405fe98436f810743b9e795a7f891faba6c7e2725c4c17f421adb783/6a4c3610b23c5dbedde6299bcabc7f2db4bd00f29c610941b5ab9cf8db230dfb/utopia_manifesto_tree.focus.html.

Prior render SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd206326692d85d8ba7533d4070a6c6f67cd89e8bdddafd3dd510059d832767e/3acc9cbe0b05ac5574a67ada39613d0c42b5980d028af97fca3449c754d1b431/utopia_manifesto_tree.focus.svg.

Those artifacts predate the 11 shortcuts and current localisation. Focus coordinates and node titles were not changed, so they remain context for the authored graph, but they do not verify the new controls or current text.

## References consulted

- Offline wiki: paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md, shortcut schema lines 148-167, prerequisite and mutual-exclusion semantics lines 277-286, allow_branch refresh behavior lines 420-422, focus search filters line 457, and ai_will_do behavior lines 606-622. Local file SHA-256: BD989A13237C464F140A0AA671CC42C30A48E84A27DAE791B8914654FB9C6203.
- Installed documentation: C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md, load_focus_tree lines 4771-4789 and mark_focus_tree_layout_dirty lines 4811-4818; SHA-256 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF.
- Installed vanilla precedent: C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/germany.txt lines 42-95 for named target/zoom shortcuts and conditional entries; SHA-256 4CFD72972E19BCC560684DFC2F170E62CE786153EE01CF06EE7ACC9609996095.
- Installed vanilla precedent: C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/persia.txt lines 68-96 for DLC-gated shortcut triggers; SHA-256 C5D2209AAFBA583FED5ECEAFEACA6D721471D6C50EC2DFF40BD02113025C2411.
- No dedicated national-focus documentation file was present in the installed documentation directory. The current event focus loading and visibility helpers were read directly in common/scripted_effects/015_utopia_manifesto_effects.txt, common/scripted_effects/015_utopia_manifesto_identity_effects.txt, common/scripted_effects/015_utopia_manifesto_country_effects.txt, common/scripted_triggers/015_utopia_manifesto_triggers.txt, and common/ideas/015_utopia_manifesto_ideas.txt.

The MCP reference-context, focus-inspect, and focus-render calls returned no result, so no reference_search, reference_read, or source_lookup result is claimed. No Paradox wiki web access or game launch was used.

## Remaining route risks

The 11 shortcut zoom values are bounded to 0.50-0.75 and follow vanilla shortcut ranges, but their pan and zoom have not been visually checked in the current tree. The crisis and revision shortcut conditions mirror the corresponding focus branch conditions; dynamic button visibility after layout refresh is not confirmed in a live render. Five localized focus titles above 30 characters may wrap in native tiles. Current route availability, idea-stage ordering, and AI ranks have no new runtime or probability evidence.

## Changed files and remaining follow-up

- common/national_focus/015_utopia_manifesto_focus_tree.txt: added 11 navigation shortcuts; no focus IDs or weights changed.
- localisation/english/015_utopia_manifesto_focus_l_english.yml: shortened 36 existing strings, removed visible bookkeeping terminology and replaced Commonwealth Ledger with Common Provision, and added 11 navigation labels.
- docs/plans/015_utopia_manifesto_plans/subagent_handoffs/focus_release_audit_2026-10-05.md: this audit handoff.

Current raw SHA-256: common/national_focus/015_utopia_manifesto_focus_tree.txt is 9DCE3A0805F6087F30E37885A7EECA1912E39932B01504D0B19E1E3A1B0BFAFF, and localisation/english/015_utopia_manifesto_focus_l_english.yml is 66F45BC215304E3A00FD47EE579FB15058DB9F084CE004A07B0B4B3630D95F5C.

No icon IDs or GFX files changed. No route family was added, removed, or replaced. No separate expansion plan was written because the accepted tree is already deep and its route families are present.

Before treating the focus surface as release-verified, rerun hoi4.focus_inspect and hoi4.focus_render against the current source; review each shortcut target, pan, zoom, hidden-region trigger, title fit, repeated icon use, connector geometry, and current-source diagnostics. The probability auditor must finish the three named focus scenarios with the complete candidate pool before any numeric AI conclusion is made. The parent retains final review and cross-system completion.

Skills applied: chaos-redux-focus-trees, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-event-assets, and chaos-redux-subagents. No skills were created or updated. No game session was launched.
