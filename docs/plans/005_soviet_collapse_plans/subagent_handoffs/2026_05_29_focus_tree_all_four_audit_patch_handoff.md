# Soviet Collapse Focus Tree Audit And Bounded Patch Handoff

Date: 2026-05-29

Scope audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

References used: `AGENTS.md`, `hoi4-focus-trees`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, offline Paradox wiki core pages plus `National focus modding`, and vanilla focus/docs references.

## Changed Files

| File | Purpose |
| --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Added existing TSC/RMC depth helper calls and moved high-chaos endpoint focuses so mutual-exclusion lines no longer span most of the tree. |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | Moved KZR/SOG/KHW/ALN symbolic/expansion/charter/endgame coordinates to keep mutually exclusive route choices close and reduce centerline crossing. |

No localisation keys or icon ids were changed.

## Changed Focus IDs

| Focus id | Before | After |
| --- | --- | --- |
| `TSC_radio_towers_in_the_taiga` | Built radar and depot/supply control only. | Also advances existing `soviet_collapse_advance_tsc_observatory_network_depth`. |
| `TSC_portable_laboratory_trains` | Gave a small stockpile/depot/liaison package. | Also advances existing `soviet_collapse_advance_tsc_field_station_depth`. |
| `TSC_observatory_guard` | Generic military consolidation reward. | Also advances TSC observatory depth. |
| `TSC_claim_the_impact_zone` | High-chaos identity and local authority only. | Also advances TSC field-station depth. |
| `TSC_observatory_state`, `TSC_the_quiet_sky_settlement` | Settlement endpoint sat far left from the mutually exclusive high-chaos endpoint. | Moved to `x = 6`, directly opposite `TSC_starfall_mandate` at `x = 10`. |
| `RMC_count_the_returning_names`, `RMC_hagiographers_of_every_front` | Martyrology route did not call its existing depth helper. | Now call `soviet_collapse_advance_rmc_martyrology_depth`. |
| `RMC_reliquary_guard`, `RMC_dead_volunteer_columns` | Reliquary guard route did not call its existing depth helper. | Now call `soviet_collapse_advance_rmc_reliquary_guard_depth`. |
| `RMC_republic_of_witnesses`, `RMC_shrine_state` | Settlement endpoint sat far left from the mutually exclusive extreme endpoint. | Moved to `x = 6`; child moved to `y = 11`. |
| `DSC_republic_of_roll_calls`, `DSC_memorial_frontier_state` | Same endpoint/pathline issue. | Moved to `x = 6`; child moved to `y = 11`. |
| `NRF_port_republic_of_the_living`, `NRF_memorial_convoy_state` | Same endpoint/pathline issue. | Moved to `x = 6`; child moved to `y = 11`. |
| `ICD_citizens_after_death`, `ICD_state_of_last_addresses` | Same endpoint/pathline issue. | Moved to `x = 6`; child moved to `y = 11`. |
| `KZR_symbolic_crossing_state`, `KZR_khazar_charter`, `KZR_restoration_survives_modern_war`, `KZR_returned_names_endgame`, `KZR_road_beyond_the_caspian` | Symbolic/expansion mutual exclusion was spread across the centerline. | Route choice/charter/endgame coordinates now mirror the SOG/KHW/ALN pattern. |
| `SOG_symbolic_city_league`, `SOG_sogdian_city_charter`, `SOG_restoration_survives_modern_war`, `SOG_returned_names_endgame`, `SOG_cities_beyond_the_desert` | Same ancient-restoration line issue. | Moved to the compact `x = 7/8/6/10/10` route geometry. |
| `KHW_symbolic_oasis_authority`, `KHW_khwarazmian_water_charter`, `KHW_restoration_survives_modern_war`, `KHW_returned_names_endgame`, `KHW_delta_without_a_center` | Same ancient-restoration line issue. | Moved to the compact route geometry. |
| `ALN_symbolic_pass_principality`, `ALN_alan_pass_charter`, `ALN_restoration_survives_modern_war`, `ALN_returned_names_endgame`, `ALN_every_pass_a_border` | Same ancient-restoration line issue. | Moved to the compact route geometry. |

## Route Coverage Table

| Required route family | Implemented coverage | Status | Notes |
| --- | --- | --- | --- |
| Political/state-building | Present in all four files. | Partial | Deep in Ukraine/Kazakhstan/MFR; compact in OGB/PRA; shallow in TSC/RMC/DSC/NRF/ICD and KZR/SOG/KHW/ALN. |
| Industry/logistics | Present in most trees. | Partial | Too many compact trees still lean on small stockpile/building packets rather than persistent mechanics or state-targeted industry loops. |
| Military | Present in all playable groups. | Partial | High-chaos endpoints are stronger, but many 47-focus splinters still share generic militia/front/supply structures. |
| Diplomacy/league/patronage | Present in republic, custom, factory, and ancient files. | Partial | AI and rewards often do not distinguish acceptance, neutrality, faction formation, or patron risk enough. |
| Expansion/claims/war goals | Stronger in OGB/PRA/TSC/RMC/DSC/NRF/ICD and ancient restorations. | Partial | Many medium republic/custom trees still have no direct claims/cores/war goals in focus rewards. |
| Special mechanics/dynamic variables | Present but uneven. | Partial | TSC/RMC now use existing depth helpers. Other compact chaos tags still need helper-side depth systems. |
| Mutually exclusive routes with purpose | Present. | Improved | Symmetry validates cleanly. Remaining issue is route depth, not broken exclusion references. |
| Route-aware AI | Present at focus level. | Weak | Mostly `ai_will_do` modifiers; little cross-branch strategic behavior or route-plan persistence. |

## Missing Or Simplified Content

| Area | File and identifiers | Remaining work |
| --- | --- | --- |
| Compact high-chaos trees | `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree` in `005_soviet_collapse_custom_splinters.txt` | 18 focuses each. They have identity and endpoints but not full political/industry/military/diplomacy/expansion/special-mechanic branch families. |
| Compact railway/restoration trees | `PRA_soviet_collapse_focus_tree` in `005_soviet_collapse_custom_splinters.txt`; `OGB_soviet_collapse_focus_tree` in `005_soviet_collapse_factory_successors.txt` | 22/23 focuses. Stronger than shallow tags but still below major-country depth. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` trees in `005_soviet_collapse_ancient_restorations.txt` | 16 focuses each. Good claims/route identity, but not enough internal politics, diplomacy, army, industry, and post-conquest integration. |
| Medium 47-focus custom splinters | `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` | Broad skeletons exist, but several still read as templated branches with repeated reward patterns and shared route shapes. |
| Republic successors | `soviet_collapse_republics.txt` trees | Large enough, but rewards are helper-heavy and expansion payoffs are uneven. Ukraine/Kazakhstan are deep; generic and regional republic trees need more route-specific payoff auditing. |
| Helper-side idea lifecycle | `common/scripted_effects/005_soviet_collapse_effects.txt:14568`, `14581`, `14592`, `14607`, `14621`, `14635`, `14678` | Endgame helpers still add major ideas. I did not edit parent-owned helper files; parent should decide whether this is intended payoff or lingering idea spam. |

## Icon Coverage Table

| Group | Missing icon assignments | Repeated icon concern |
| --- | --- | --- |
| All four focus files | None found. | No focus lacks an `icon = ...` assignment. |
| Large republic trees | None. | Repeated icons above 2 uses in Ukraine, internal republic, Baltic, Caucasus, Central Asia, Moldova. |
| Medium custom splinters | None. | Notable repeated icons in `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `CFR`; most others are acceptable. |
| Compact chaos trees | None. | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, `OGB` all have unique icons per focus. |
| Ancient restorations | None. | `KZR`, `SOG`, `KHW`, `ALN` all have unique icons per focus after current file state. |

## Localisation And Reward Mismatch List

Validation found no missing focus name or description localisation for the current focus ids.

Remaining mismatch risks are design-level rather than missing-key errors:

- `TSC_observatory_state` and `TSC_the_quiet_sky_settlement` now have better layout, but their rewards still rely on generic legal/league/stability effects rather than a full observatory-state mechanic.
- `RMC_republic_of_witnesses` and `RMC_shrine_state` now have better layout and linked depth helpers upstream, but the settlement endpoint still shares the same endgame helper as the extreme route.
- `DSC_memorial_frontier_state`, `NRF_memorial_convoy_state`, and `ICD_state_of_last_addresses` are lore-specific in text but still use compact generic stability/legal/league reward patterns.
- Ancient restoration endgames promise restored-state identity but currently stop at claims, variables, and a few map/building effects.

## AI Behavior Gaps

| Area | File/ids | Gap |
| --- | --- | --- |
| High-chaos compact tags | `TSC`, `RMC`, `DSC`, `NRF`, `ICD` endpoint routes | AI weights react to chaos tier, war, and some route flags, but lack broader route plans for expansion versus settlement, faction use, and when to avoid overextension. |
| OGB/PRA | `OGB_*`, `PRA_*` trees | AI is better than the shallow chaos tags but still mostly local focus weights; no visible full strategic plan for compact vs conquest identities. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` | AI can choose branches, but there is no robust post-claim behavior for integrating or prioritizing claims. |
| Medium custom splinters | 47-focus splinter trees | Many use route flags and chaos-tier weights, but repeated branch shapes make AI behavior feel similar across identities. |

## Ranking By Depth And Remaining Work

| Tree | Focuses | Rank | Remaining work |
| --- | ---: | --- | --- |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | Deep | Audit route payoff and AI specificity. |
| `soviet_collapse_ukraine_focus_tree` | 83 | Deep | Audit helper-heavy rewards and expansion payoff. |
| `soviet_collapse_internal_republic_focus_tree` | 62 | Deep | Reduce helper/reward repetition and add clearer regional end states. |
| `MFR_soviet_collapse_focus_tree` | 58 | Deep | Good identity; verify factory mechanics and route AI. |
| `soviet_collapse_belarus_focus_tree` | 53 | Medium-high | Needs stronger expansion/diplomacy payoff. |
| `soviet_collapse_moldova_focus_tree` | 48 | Medium | Needs less stockpile/building repetition. |
| 47-focus custom splinters (`FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`, `CFR`) | 47 each | Medium | Branch families exist; remaining work is identity-specific rewards, AI, icons where repeated, and expansion consequences. |
| `soviet_collapse_central_asia_focus_tree` | 45 | Medium | Claims exist; needs stronger post-claim integration and diplomacy. |
| `soviet_collapse_baltic_focus_tree` | 42 | Medium | Good diplomacy shell; needs stronger military/port payoff. |
| `soviet_collapse_caucasus_focus_tree` | 40 | Medium | Needs oil/pass mechanics and more consequenceful diplomacy. |
| `soviet_collapse_breakaway_focus_tree` | 36 | Compact | Needs deeper political/industry/military route families. |
| `OGB_soviet_collapse_focus_tree` | 23 | Compact | Strong identity, still too short for a major chaos country. |
| `PRA_soviet_collapse_focus_tree` | 22 | Compact | Strong railway identity, needs a real rail-control mechanic and broader expansion branch. |
| `TSC`, `RMC`, `DSC`, `NRF`, `ICD` trees | 18 each | Shallow compact | Need full expansion addenda, not more small focus-file patches. |
| `KZR`, `SOG`, `KHW`, `ALN` ancient trees | 16 each | Shallow compact | Need political, military, industry, diplomacy, and postwar integration expansion. |

## High-Priority Fixes Applied First

1. Used existing TSC/RMC depth helpers where focus names already promised observatory, field-station, martyrology, and reliquary development.
2. Shortened bad high-chaos endpoint mutual-exclusion pathlines in TSC/RMC/DSC/NRF/ICD.
3. Shortened ancient restoration symbolic-versus-expansion mutual-exclusion pathlines in KZR/SOG/KHW/ALN.

## Validation Run

- Brace depth on all four focus files: `0` final depth for all four files.
- Duplicate focus id scan: none.
- Duplicate top-level focus-tree id key scan: none.
- Missing prerequisite/mutual-exclusion/relative-position refs: none.
- Mutual-exclusion symmetry: none missing.
- Direct duplicate `add_ideas` in focus rewards: none.
- Direct duplicate helper-like calls in a single focus reward: none.
- Unsupported `<=`/`>=` scan: no matches.
- Missing focus localisation name/description scan: none.
- Missing icon assignment scan: none.
- `git diff --check` on touched focus files: passed.

## Skipped Validation

- No live HOI4 load test was run in this subagent pass.
- Parent-owned helper, decision, trigger, and script constant files were not edited by design.

## Remaining Route Risks

- The four audited files are structurally clean, but the objective is not fully satisfied by bounded focus-file patches. Several chaos countries remain compact and need new or expanded helper-side mechanics, decision hooks, and postwar integration.
- Direct focus-level `add_ideas` spam is currently absent; if the user still sees idea spam, the likely source is helper-side endgame/evolution effects, especially the helper ids listed above.
- The strongest remaining design need is not another small coordinate pass; it is an accepted expansion plan for TSC/RMC/DSC/NRF/ICD, OGB/PRA, and the ancient restoration set.

## Improvement Plan Handoff

Use this handoff as the improvement plan for the next parent pass:

1. Add or extend helper-side depth systems for `DSC`, `NRF`, `ICD`, `PRA`, `OGB`, `KZR`, `SOG`, `KHW`, and `ALN`, matching the existing TSC/RMC helper pattern.
2. Give each compact high-chaos country one route-specific decision loop: railway control for `PRA`, star research/perimeter control for `TSC`, memorial musters for `RMC/DSC/ICD`, cold-port convoy authority for `NRF`, Volga legitimacy for `OGB`, and restored-name integration for ancient tags.
3. Add postwar integration for claims: cores or staged integration missions should follow conquest; war goals alone are insufficient.
4. Add route-level AI behavior beyond `ai_will_do`, especially for settlement versus extreme paths and for when the AI should form/join factions.
5. Keep focus rewards tied to Soviet Collapse variables, decision unlocks, claims, war goals, buildings, units, and helper depth. Avoid adding more flat ideas unless they are end-state payoffs with clear lifecycle.
