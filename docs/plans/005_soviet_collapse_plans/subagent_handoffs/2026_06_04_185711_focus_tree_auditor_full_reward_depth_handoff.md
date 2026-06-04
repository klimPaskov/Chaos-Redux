# Event 005 Soviet Collapse Focus Tree Audit Handoff

Subagent: `chaosx_focus_tree_auditor`  
Mode: read-only audit. No focus files, localisation files, decisions, or `gfx/flags/*` assets were edited.  
Date: 2026-06-04 18:57 UTC

## Scope And References

Audited all files matching `common/national_focus/005_soviet_collapse_*.txt`.

Required guidance consulted:

- Skills: `hoi4-focus-trees`, `chaos-redux-events`, `hoi4-decisions-missions`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`
- Vanilla precedents: `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`, vanilla decisions under `~/projects/Hearts of Iron IV/common/decisions`

Vanilla precedent supports the main audit standard: route mutexes should be readable, decision unlocks should be obvious when focus rewards expose new actions, and idea add/remove/swap operations are player-facing reward noise unless hidden and lifecycle-safe.

## Focus Tree Counts

| File | Focus tree id | Focuses |
|---|---:|---:|
| `005_soviet_collapse_ancient_restorations.txt` | `KZR_soviet_collapse_ancient_focus_tree` | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `SOG_soviet_collapse_ancient_focus_tree` | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `KHW_soviet_collapse_ancient_focus_tree` | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `ALN_soviet_collapse_ancient_focus_tree` | 16 |
| `005_soviet_collapse_custom_splinters.txt` | `FTH_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `PRA_soviet_collapse_focus_tree` | 22 |
| `005_soviet_collapse_custom_splinters.txt` | `TSC_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `RMC_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `DSC_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `NRF_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `ICD_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `BSC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `TNC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `ALA_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `BBH_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `KRS_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `UDC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `SDZ_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `GAC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `DHC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `KHC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `FEV_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `SZA_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `UWD_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `MRC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `IUL_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `BAC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `ARD_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `NLC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_factory_successors.txt` | `CFR_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_factory_successors.txt` | `OGB_soviet_collapse_focus_tree` | 23 |
| `005_soviet_collapse_factory_successors.txt` | `MFR_soviet_collapse_focus_tree` | 58 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_ukraine_focus_tree` | 83 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_breakaway_focus_tree` | 36 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_internal_republic_focus_tree` | 62 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_baltic_focus_tree` | 42 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_caucasus_focus_tree` | 40 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_central_asia_focus_tree` | 45 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_moldova_focus_tree` | 48 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_belarus_focus_tree` | 53 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_kazakhstan_focus_tree` | 92 |

Total audited: 41 focus trees, 1,698 focuses.

## Top 20 Reward Spam Risks

Ranking is heuristic: direct idea ops and focus-called idea helpers score highest; repeated visible buildings/equipment dumps and flag-only flat rewards score next.

| Rank | File:line | Focus id | Risk |
|---:|---|---|---|
| 1 | `005_soviet_collapse_custom_splinters.txt:15586` | `KHC_laba_rear_area` | Calls `soviet_collapse_add_republic_focus_recovery_progress`, which can remove startup ideas; also adds 3 building rewards and two flags. |
| 2 | `005_soviet_collapse_custom_splinters.txt:18090` | `SZA_tomsk_omsk_switchyards` | Same recovery helper plus 3 random-state building rewards and mostly flat depot/institution variables. |
| 3 | `005_soviet_collapse_custom_splinters.txt:3488` | `NRF_living_harbor_committees` | Calls starting-tension cleanup helper, gives two stockpile dumps and two building rewards in one visible focus. |
| 4 | `005_soviet_collapse_custom_splinters.txt:25192` | `NLC_apatity_rear_area` | Recovery helper plus equipment, 2 buildings, foreign-channel helper, and flag-only gating. |
| 5 | `005_soviet_collapse_custom_splinters.txt:535` | `FTH_village_delegate_roads` | Recovery helper plus depot helper and two small building rewards; reads as generic route filler. |
| 6 | `005_soviet_collapse_custom_splinters.txt:1374` | `PRA_the_board_overrules_ministers` | Removes route tension ideas, adds two buildings, unlocks an already repeated PRA decision tooltip, and calls legal helper. |
| 7 | `005_soviet_collapse_custom_splinters.txt:25160` | `NLC_winter_road_columns` | Recovery helper plus equipment/buildings/flag, weak distinct mechanic. |
| 8 | `005_soviet_collapse_custom_splinters.txt:16743` | `FEV_harbor_fortress_line` | Five building construction effects plus equipment and one flag; high visible bloat for a single focus. |
| 9 | `005_soviet_collapse_custom_splinters.txt:14389` | `DHC_manych_rear_area` | Recovery helper plus two buildings and two flags. |
| 10 | `005_soviet_collapse_custom_splinters.txt:25502` | `NLC_extreme_gate` | Recovery helper on a gate focus; two buildings and flag-only payoff instead of a clear extreme mechanic. |
| 11 | `005_soviet_collapse_custom_splinters.txt:14559` | `DHC_winter_road_columns` | Mobile-column helper plus recovery helper; visible payoff is otherwise a small building/flag package. |
| 12 | `005_soviet_collapse_custom_splinters.txt:1228` | `PRA_the_timetable_declares_authority` | Calls `soviet_collapse_update_pra_authority_idea`; this is an idea lifecycle helper directly from the opener. |
| 13 | `005_soviet_collapse_custom_splinters.txt:1573` | `PRA_passport_of_the_moving_state` | Calls same PRA authority idea helper and high-chaos helper with only a flag/variable visible payload. |
| 14 | `005_soviet_collapse_custom_splinters.txt:25066` | `NLC_ration_and_signal_escorts` | Depot helper plus recovery helper; mostly a flag/variable payload. |
| 15 | `005_soviet_collapse_factory_successors.txt:1113` | `OGB_the_council_takes_the_seal` | Starting-tension cleanup helper plus legal helper; OGB is already short, so this feels like cleanup instead of route payoff. |
| 16 | `005_soviet_collapse_custom_splinters.txt:1639` | `PRA_league_transit_bargain` | Three helper calls including PRA idea update; high tooltip/helper density. |
| 17 | `005_soviet_collapse_custom_splinters.txt:16824` | `FEV_war_plan` | Four building rewards plus security helper; weak for a war-plan focus. |
| 18 | `005_soviet_collapse_custom_splinters.txt:25434` | `NLC_industry_plan` | Four building rewards and one flag; no obvious new mechanic. |
| 19 | `005_soviet_collapse_republics.txt:3992` | `internal_soviet_collapse_peninsula_fortress_plan` | Four building rewards plus security helper; generic fortress package. |
| 20 | `005_soviet_collapse_republics.txt:11732` | `kaz_soviet_collapse_industrial_settlement_compacts` | Four building rewards and one flag; weak payoff inside an otherwise large Kazakhstan tree. |

## Helper Effects Causing Idea/Spirit Churn

| Helper | Definition | Focus calls | Problem |
|---|---|---:|---|
| `soviet_collapse_add_republic_focus_recovery_progress` | `common/scripted_effects/005_soviet_collapse_effects.txt:4880` | 11 | Removes `soviet_collapse_republican_startup_disorder` or `_mitigated` when recovery completes. It is hidden, but focus rewards still call a lifecycle idea helper repeatedly from unrelated route focuses. |
| `soviet_collapse_clear_focus_starting_tension_ideas` | `common/scripted_effects/005_soviet_collapse_effects.txt:5825` | 6 | Removes seven different country-specific tension ideas. It is hidden, but focus reward identity becomes "clear setup tension" rather than a route-specific payoff. |
| `soviet_collapse_update_pra_authority_idea` | `common/scripted_effects/005_soviet_collapse_effects.txt:7897` | 3 | Clears and adds PRA authority ideas based on flags. Called by `PRA_the_timetable_declares_authority`, `PRA_passport_of_the_moving_state`, and `PRA_league_transit_bargain`; this is the clearest visible idea churn site. |

Highest-volume non-idea helpers from focuses: `soviet_collapse_apply_focus_depot_and_supply_control` 135 calls, `soviet_collapse_apply_focus_military_consolidation` 127, `soviet_collapse_apply_focus_legal_recognition` 104, `soviet_collapse_apply_focus_republican_compact_plan` 79, `soviet_collapse_apply_focus_foreign_channel` 64. These are not inherently bad, but the volume explains why many branches feel templated.

## Trees Lacking Clear Branch Families

High-risk by focus count and branch/mechanic scan:

- `KZR`, `SOG`, `KHW`, `ALN` ancient restoration trees: only 16 focuses each. They have symbolic/expansion choices and some claim decisions, but no full political, industry, military, diplomacy, expansion, and endgame branch set.
- `TSC`, `RMC`, `DSC`, `NRF`, `ICD`: 18-focus high-chaos/special trees. These are too short for their concepts. They read as opener, two mutex choices, a few support focuses, second mutex, endpoint.
- `PRA`: 22 focuses and the strongest unique mechanic surface in the short group, but expansion count is thin and the authority idea lifecycle is noisy.
- `OGB`: 23 focuses; it has restored-name flavor and Volga hooks, but industry and diplomacy are shallow.
- `soviet_collapse_breakaway_focus_tree`: 36 focuses with broad political wording, but only one expansion-keyed focus and no strong branch-specific map mechanics.
- Large 47-focus custom splinters are better by count, but many have weak mechanic counts: `FTH`, `BBH`, `KRS`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC` showed zero direct "mechanicish" rewards by the parser criteria. They rely on generic helpers and flat map/building rewards.

## Mutex And Pathline Risks

- CFR has a four-way route selector implemented as twelve pairwise mutex lines at `005_soviet_collapse_factory_successors.txt:136-237`. This is visually dense and likely hard to read. Use a clean selector row with one focus per route and avoid additional crossing prerequisites below it.
- MFR has a four-way selector at `005_soviet_collapse_factory_successors.txt:1750-1844`, with each focus mutexing the other three in one block. It is valid, but it creates a large blocked cluster before the tree payoff is visible.
- Moldova has a three-way selector at `005_soviet_collapse_republics.txt:7804-7868`; this is meaningful politically, but it should be reviewed for line crossings because the branch is compact and near other route lanes.
- The 18-focus special trees repeat two binary mutex pairs each: TSC `1999/2032` and `2260/2299`, RMC `2447/2478` and `2730/2759`, DSC `2938/2970` and `3280/3309`, NRF `3489/3521` and `3806/3831`, ICD `3995/4027` and `4275/4300`. These choices are not pointless narratively, but the repeated shape makes them feel copied and visually formulaic.
- Most 47-focus custom splinters repeat `settlement` versus `radical_turn`. This is a useful route split, but the repeated layout and reward rhythm makes the trees blur together.
- Parser did not detect duplicate absolute coordinates in the audited focus blocks. The remaining visual risk is pathline density/crossing, not same-coordinate overlap.

## Chaos Countries Not OP/Aggressive Enough

The following need stronger lore-driven mechanics, not just more stats:

- `TSC`: needs sky/impact-zone mechanics, anomaly research decisions, targetable observation sites, and aggressive claims/wargoals around Siberian route control.
- `RMC`: needs cult martyrdom pressure, resurrection-cell recruitment, sacrifice/reliquary missions, and territorial martyr-road claims.
- `DSC`: has some stronger hooks than peers, but still needs death-army escalation, recurring revenant units, grave-front claims, and post-victory occupation/terror mechanics.
- `NRF`: needs fleet/port mechanics, ghost convoy raids, Arctic naval buildup, White Sea claims, and port integration decisions.
- `ICD`: needs dead commissariat authority, political terror, roll-call conscription, internal purge decisions, and direct offensive pressure.
- Ancient restorations: `KZR`, `SOG`, `KHW`, `ALN` need cores/claims/wargoals tied to their historical restoration thesis, stronger regional integration decisions, elite units, and final formable/end-state payoffs.
- `OGB`: needs Volga-Idel regional mechanics, stronger conflict/settlement with Idel-Ural, and a real expansion or confederation branch.
- `PRA`: should turn railway authority into a reusable moving-state mechanic with route permits, armored train deployment, corridor taxation, and coercive rail war goals.

## Focus-To-Decision/Mechanic Gaps

Findings:

- Focus files set 1,696 distinct country flags. A script-token scan outside the audited focus files found 1,379 with no occurrence elsewhere. This is not automatically a bug because focus flags can be used only for focus prerequisites/AI, but it is a strong sign that many focuses do not unlock mechanics beyond the tree itself.
- Ancient restoration flags are especially suspect: most `KZR_*`, `SOG_*`, `KHW_*`, and `ALN_*` focus flags are not read outside the audited focus file. Examples: `KZR_khazar_charter`, `SOG_sogdian_city_charter`, `KHW_khwarazmian_water_charter`, `ALN_alan_pass_charter`.
- Per-tag custom splinter flags like `ala_focus_*`, `ard_focus_*`, and similar are mostly focus-internal. This makes the 47-focus trees look large while many route milestones have no external decision/mechanic consequences.
- Decision scan found only 71 focus reward lines using `unlock_decision_tooltip` or `activate_decision` across 1,698 focuses. Many decisions are gated by flags instead of explicit unlock tooltips, which works mechanically but hides the connection from the player.
- `common/decisions/005_soviet_collapse_kazakhstan_route_decisions.txt` route decisions are gated by focus-set route flags but are not directly exposed by focus unlock tooltips. The `*_recent` flags are decision cooldown flags, not focus gaps.
- `common/decisions/005_soviet_collapse_moldova_route_decisions.txt` has the same pattern: route flags exist, but decision availability is not consistently announced by focus completion.
- Returned-names decisions are partially exposed by ancient focus tooltips, but the one-shot flags like `soviet_collapse_returned_names_museum_opened`, `...archivists_recruited`, and `...old_banner_commissioned` are decision-internal. Parent should avoid misclassifying these as missing focus flags.

## Implementation Order For Parent

1. **Idea helper cleanup tranche:** Replace focus reward calls to `soviet_collapse_update_pra_authority_idea`, `soviet_collapse_clear_focus_starting_tension_ideas`, and `soviet_collapse_add_republic_focus_recovery_progress` with clearer route-specific helpers or custom tooltips where needed. Keep hidden lifecycle cleanup, but prevent repeated visible reward churn.
2. **Top 20 reward spam tranche:** Patch the ranked reward sites by moving repeated building/equipment payloads behind custom tooltips, adding route-specific decision unlocks, units, claims, or dynamic mechanics, and removing duplicate random-state construction where it has no clear geography.
3. **Short chaos tree depth tranche:** Expand `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, `PRA`, and `OGB` into real political/industry/military/diplomacy/expansion/endgame branches. Do not bulk-copy a 47-focus template.
4. **Ancient restoration mechanics tranche:** Give `KZR`, `SOG`, `KHW`, and `ALN` concrete restoration systems: claims/cores, integration decisions, historic legitimacy pressure, elite units, and end-state choices.
5. **Decision visibility tranche:** For Kazakhstan, Moldova, returned names, PRA, MFR, CFR, and custom splinter route decisions, add focus unlock tooltips where a focus is intended to open a decision category/action. Do not add fallback decisions without parent design approval.
6. **Layout/mutex cleanup tranche:** Review CFR, MFR, Moldova, and the 18-focus special trees in the focus UI. Keep meaningful choices, but reduce repeated mutex clusters and pathline clutter.

## Validation And Limitations

Commands/scripts run:

- `rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|National focus'`
- `sed -n ...` on required offline wiki pages and vanilla documentation
- `rg --files common/national_focus | rg '005_soviet_collapse_.*\\.txt$'`
- Python brace parser over all four Event005 focus files to count focus trees, focus blocks, reward operations, helper calls, branch keyword counts, mutex structures, and focus-set flags
- `rg -n` on helper definitions and high-risk focus snippets
- Decision scan over `common/decisions/005_soviet_collapse*.txt`
- Vanilla precedent scans in `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt` and `~/projects/Hearts of Iron IV/common/decisions`

Limitations:

- I did not run the game or inspect live focus UI pathlines.
- Flag gap scan is token-based. It can miss meta-generated references and can overcount intentionally focus-internal flags.
- Branch family classification is keyword/mechanic heuristic; it identifies review targets, not final design truth.
- No files were patched beyond this handoff report.

Skills used: `hoi4-focus-trees`, `chaos-redux-events`, `hoi4-decisions-missions`.
