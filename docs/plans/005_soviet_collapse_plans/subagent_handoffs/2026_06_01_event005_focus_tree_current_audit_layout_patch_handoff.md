# Event005 Soviet Collapse focus tree audit and bounded layout patch

Date: 2026-06-01

Scope audited:
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- Directly related reward evidence in `common/scripted_effects/005_soviet_collapse_effects.txt`
- Directly related custom-tooltip localisation in `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

No-touch constraint honored: no `gfx/flags`, `interface/flags`, flag sprite, interface sprite, or gfx definition files were edited or inspected beyond focus icon identifiers present in focus files.

Required references and skills used:
- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages opened: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla documentation opened: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla precedent checked: `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`, with additional focus mutual-exclusion pattern checks in `baltic_shared.txt`.

Worktree note: the four Event005 focus files and many handoff docs were already dirty or untracked before this audit. The only gameplay patch made by this pass is the five y-coordinate changes listed below.

## Audit summary

| Metric | Result |
| --- | ---: |
| Focus files audited | 4 |
| National focus trees | 41 |
| Focus blocks | 1698 |
| Duplicate focus ids | 0 |
| Focuses missing `ai_will_do` | 0 |
| Focuses missing `search_filters` | 0 |
| Focuses missing icon assignment | 0 |
| Missing focus name localisation | 0 |
| Missing focus description localisation | 0 |
| Direct focus `add_ideas` rewards | 0 |
| Direct focus `remove_ideas` rewards | 0 |
| Direct focus `swap_ideas` rewards | 0 |
| Direct focus `add_timed_idea` rewards | 0 |
| Stockpile reward focuses | 163 |
| Wargoal focuses | 15 |
| Claim focuses | 14 |
| AI-strategy-effect focuses | 24 |
| Decision unlock/activation focuses | 72 |

The direct visible idea spam reported by earlier passes has mostly been removed from focus completion blocks. The current worst reward problem is now generic helper and generic-tooltip spam: many focuses expose the same custom effect tooltip or run the same helper-looking route bundles, which makes branches feel like renamed wrappers over a common reward template rather than political, industrial, military/logistics, and expansion routes with identity.

## Route coverage table

| File / tree | Focuses | Current route coverage | Main gap |
| --- | ---: | --- | --- |
| `KZR_soviet_collapse_ancient_focus_tree` | 16 | Ancient legitimacy, border names, workshop/logistics, league/expansion | Too shallow for an overpowered chaos successor; `KZR_expansionist_steppe_levy` at `common/national_focus/005_soviet_collapse_ancient_restorations.txt:222` and `KZR_returned_names_endgame` at `:325` are helper-led end states. |
| `SOG_soviet_collapse_ancient_focus_tree` | 16 | Ancient trade/merchant legitimacy, route guard, expansion | Same 16-focus stub issue; `SOG_expansionist_merchant_claims` at `:612` and `SOG_returned_names_endgame` at `:711` need real route mechanics. |
| `KHW_soviet_collapse_ancient_focus_tree` | 16 | Delta legitimacy, water/control themes, expansion | `KHW_expansionist_water_claims` at `:992`, `KHW_returned_names_endgame` at `:1100`, and `KHW_delta_without_a_center` at `:1128` overuse helper payoffs. |
| `ALN_soviet_collapse_ancient_focus_tree` | 16 | Ancient northern identity, guard routes, league/expansion | `ALN_returned_names_endgame` at `:1483` is a route name without enough direct mechanic payoff. |
| `FTH` custom splinter | 47 | Political commune, settlement, military/logistics, expansion-lite | Stronger shape than compact stubs but still uses broad generic route identity tooltips and helper bundles. |
| `PRA` custom splinter | 22 | Rail authority and moving-state identity | Severe compact-tree gap; `PRA_the_timetable_declares_authority` at `custom_splinters.txt:1198`, `PRA_timetable_law` at `:1298`, `PRA_the_board_overrules_ministers` at `:1344`, `PRA_armored_train_directorate` at `:1369`, `PRA_passport_of_the_moving_state` at `:1529`, `PRA_neutral_corridor_letters` at `:1552`, `PRA_charge_for_safe_passage` at `:1573`, and `PRA_the_pale_line_endures` at `:1744` need rail-state decisions/route consequences. |
| `TSC` custom splinter | 18 | Tunguska/star identity, observatory guard, impact zone | Severe compact-tree gap; `TSC_radio_towers_in_the_taiga` at `:1874`, `TSC_observatory_guard` at `:1979`, `TSC_claim_the_impact_zone` at `:2112`, `TSC_sky_over_siberia` at `:2134`, and `TSC_the_quiet_sky_settlement` at `:2222` need a project/anomaly/science payoff loop. |
| `RMC` custom splinter | 18 | Martyr/reliquary legitimacy, columns, shrine state | Severe compact-tree gap; `RMC_count_the_returning_names` at `:2319`, `RMC_reliquary_guard` at `:2430`, `RMC_procession_columns` at `:2601`, and `RMC_shrine_state` at `:2696` need cult/procession/recruitment mechanics. |
| `DSC` custom splinter | 18 | Dead soldiers, revenant staff, grave ordnance | `DSC_revenant_staff_line` at `:2866`, `DSC_grave_ordnance_claims` at `:2901`, `DSC_rearguard_supply_bureau` at `:2971`, and `DSC_memorial_frontier_state` at `:3250` are high-priority shallow identity payoffs. |
| `NRF` custom splinter | 18 | Northern fleet/revenant convoy | `NRF_fleet_that_does_not_dock` at `:3665` and `NRF_memorial_convoy_state` at `:3765` should produce naval/port/convoy and coast-control systems, not just helper pressure. |
| `ICD` custom splinter | 18 | Iron commissariat/dead-command identity | `ICD_grave_columns_march` at `:4138` and `ICD_state_of_last_addresses` at `:4230` need coercion/front/discipline mechanics. |
| 47-focus custom templates: `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` | 47 each | Political, legal/settlement, logistics/military, diplomacy, expansion/endgame lanes generally present | The lane count is acceptable, but too many rewards still call shared route bundles. Several templates repeat icon IDs and have endpoint rewards that read as generic recognition/depot/security packages. |
| `CFR` factory successor | 47 | Construction state, municipal legality, guards, industry, foreign engineers | Stronger than most compact trees, but repeated idea updater/setup rewards still blur construction-mandate identity. |
| `OGB` factory successor | 23 | Restored name, Volga position, expansion-lite | Too shallow for a chaos-country identity; needs trade, old-name politics, border diplomacy, and military/logistics growth. |
| `MFR` factory successor | 58 | Arsenal quotas, military-industrial command, force buildup | Best-developed factory route by size; still helper-heavy and needs clearer route-exclusive consequences. |
| Ukraine republic tree | 83 | Multiple political routes, industry, military/logistics, diplomacy | Large enough, but payoff/route locks need deeper Soviet Collapse system integration and pathline review. |
| Generic breakaway tree | 36 | Breakaway survival, local institutions, logistics | Basic structure only; lacks overpowered chaos identity and route-specific mechanics. |
| Internal republic tree | 62 | Soviet-remnant/legal/internal-republic paths | Better breadth, but rewards lean toward compact helper packages rather than route-specific state mechanics. |
| Baltic tree | 42 | Legal continuity, military border government, Baltic league, foreign protection | Four mutual-exclusive route choices remain on the same row, making pathlines cross route nodes and reducing fork clarity. |
| Caucasus tree | 40 | Local authority, mountain/security/logistics themes | Needs more explicit expansion and high-chaos power identity. |
| Central Asia tree | 45 | Steppe/rail/irrigation/federation themes | Needs stronger logistics-industrial and expansion route consequences. |
| Moldova tree | 48 | Union-question routes, border/smuggler/soil recovery themes | Three mutual-exclusive route choices remain on the same row, with intervening focuses creating pathline risk. |
| Belarus tree | 53 | Minsk council, socialist autonomy, military transit, foreign corridor | Four mutual-exclusive route choices remain on the same row, with transit/corridor identity needing stronger decision hooks. |
| Kazakhstan tree | 92 | Alash/socialist/military/resource/league/foreign/high-chaos coverage | Size is good, but helpers and repeated stockpile/building rewards still dilute route identity. |

## Concrete worst offenders

High-priority shallow or generic-reward focuses:
- `KZR_expansionist_steppe_levy` at `common/national_focus/005_soviet_collapse_ancient_restorations.txt:222`: stockpile plus assault/claims/high-chaos helper bundle in a 16-focus tree.
- `SOG_expansionist_merchant_claims` at `common/national_focus/005_soviet_collapse_ancient_restorations.txt:612`: same shallow expansion pattern.
- `KHW_expansionist_water_claims` at `common/national_focus/005_soviet_collapse_ancient_restorations.txt:992`: same shallow expansion pattern.
- `KHW_delta_without_a_center` at `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1128`: end-state naming but helper/claim-led reward.
- `DSC_revenant_staff_line` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2866`: high-chaos/depot/objective helper pattern where a dead-army command system should appear.
- `PRA_*` compact route endpoints from `common/national_focus/005_soviet_collapse_custom_splinters.txt:1198-1744`: moving rail-state lore but mostly authority/updater/helper effects.
- `TSC_*` compact route endpoints from `common/national_focus/005_soviet_collapse_custom_splinters.txt:1874-2222`: anomalous/star-science lore but no distinct project loop.
- `RMC_*` compact route endpoints from `common/national_focus/005_soviet_collapse_custom_splinters.txt:2319-2696`: reliquary/martyr lore but no distinct procession/recruitment/legitimacy loop.
- `NRF_*` compact route endpoints from `common/national_focus/005_soviet_collapse_custom_splinters.txt:3665-3765`: revenant fleet lore but weak naval/port/convoy consequences.
- `ICD_*` compact route endpoints from `common/national_focus/005_soviet_collapse_custom_splinters.txt:4138-4230`: death-commissariat lore but no coercive military/governance loop.

## Duplicate visible idea/helper reward evidence

Direct focus idea reward status:
- Direct `add_ideas`, `remove_ideas`, `swap_ideas`, and `add_timed_idea` in the audited focus completion blocks: 0.
- This means the old visible focus-panel idea spam is not currently caused by direct focus idea effects in these four files.

Current visible/generic reward spam:
- `custom_effect_tooltip = soviet_collapse_custom_splinter_route_identity_reward_tt` appears in 355 focus rewards. The localisation at `localisation/english/005_soviet_collapse_custom_countries_l_english.yml:1791` is intentionally generic: "route-specific institution package" covering legitimacy, depots, recognition, military prep, construction, assault formations, or claims.
- `custom_effect_tooltip = soviet_collapse_custom_splinter_doctrine_identity_reward_tt` appears in 19 focus rewards. The localisation is at `localisation/english/005_soviet_collapse_custom_countries_l_english.yml:1804`.
- `custom_effect_tooltip = soviet_collapse_custom_splinter_hidden_doctrine_reward_tt` appears in 19 focus rewards. The localisation is at `localisation/english/005_soviet_collapse_custom_countries_l_english.yml:1805`.

Most repeated helper calls found in focus rewards:
- `soviet_collapse_apply_focus_depot_and_supply_control`: 138 calls.
- `soviet_collapse_apply_focus_military_consolidation`: 132 calls.
- `soviet_collapse_apply_focus_legal_recognition`: 117 calls.
- `soviet_collapse_apply_focus_republican_compact_plan`: 80 calls.
- `soviet_collapse_apply_objective_source_pressure_delta`: 63 calls.
- `soviet_collapse_apply_focus_foreign_channel`: 63 calls.
- `soviet_collapse_apply_focus_high_chaos_identity`: 60 calls.
- `soviet_collapse_apply_focus_security_supply_plan`: 57 calls.
- `soviet_collapse_apply_focus_league_preparation`: 52 calls.
- `soviet_collapse_apply_custom_splinter_league_identity`: 38 calls.
- `soviet_collapse_apply_custom_splinter_enemy_front_identity`: 36 calls.
- `soviet_collapse_apply_custom_splinter_expansion_claims`: 28 calls.
- `soviet_collapse_apply_focus_chaos_assault_plan`: 28 calls.

Idea/setup evidence outside direct focus rewards:
- `common/scripted_effects/005_soviet_collapse_effects.txt:16346-16938` defines setup helpers that add starting identity ideas for custom successors, for example `cfr_construction_mandates` at `:16359`, `mfr_arsenal_quotas` at `:16379`, `krs_sailors_assembly` at `:16399`, `fth_free_territory_communes` at `:16417`, `dsc_dead_soldiers_congress` at `:16494`, `ogb_disputed_restored_name` at `:16744`, `tsc_tunguska_star_committee` at `:16879`, `icd_iron_commissariat_of_the_dead` at `:16899`, `ard_northern_port_directorate` at `:16918`, and `nrf_northern_revenant_fleet` at `:16938`.
- Additional non-focus helper sections add or update `cfr_construction_mandates` at `common/scripted_effects/005_soviet_collapse_effects.txt:10598`, `:10666`, and `:10704`, and `mfr_arsenal_quotas` at `:11222`. These are not direct focus-panel spam, but they explain why idea/helper churn remains visible in the broader Event005 system.

## Pathline and layout risks

Pre-patch layout audit:
- Same-coordinate focus conflicts: 0.
- Prerequisite lines that move upward or sideways: 0.
- Same-row prerequisite spans through intermediate nodes: 0.
- Same-row mutual-exclusion spans through intermediate nodes: 15.

Small bounded patch made:
- Moved five custom-splinter settlement/loyalist payoff focuses down so their mutual-exclusive fork pathlines no longer run through same-row fork content.

Changed focus ids:
- `UDC_loyalist_statute_guarantees` in `common/national_focus/005_soviet_collapse_custom_splinters.txt:10740`: `y = 7` -> `y = 10`.
- `SDZ_chain_of_custody_statutes` in `common/national_focus/005_soviet_collapse_custom_splinters.txt:11956`: `y = 7` -> `y = 10`.
- `GAC_harvest_truce_guarantees` in `common/national_focus/005_soviet_collapse_custom_splinters.txt:13391`: `y = 7` -> `y = 11`.
- `DHC_convoy_autonomy_guarantees` in `common/national_focus/005_soviet_collapse_custom_splinters.txt:14430`: `y = 7` -> `y = 11`.
- `KHC_grain_passage_guarantees` in `common/national_focus/005_soviet_collapse_custom_splinters.txt:15623`: `y = 7` -> `y = 11`.

Route behavior before and after:
- Before: these payoff focuses sat on the same row as mutually exclusive fork choices, so pathlines could visually run through fork nodes and make the branch structure look like a decorative row rather than a meaningful fork.
- After: the payoff focuses sit below the forks, preserving prerequisite/downward flow and making the fork outcome clearer without changing rewards, prerequisites, icons, localisation, AI weights, or country behavior.

Remaining post-patch layout risks:
- Same-row mutual-exclusion spans reduced from 15 to 10.
- Remaining spans are in `common/national_focus/005_soviet_collapse_republics.txt` and should be fixed in a dedicated republic layout pass:
  - Baltic route row: mutual-exclusion lines among `baltic_soviet_collapse_legal_continuity_government`, `baltic_soviet_collapse_military_border_government`, `baltic_soviet_collapse_baltic_league_first`, and `baltic_soviet_collapse_foreign_protection_council` pass across `baltic_soviet_collapse_singing_barricades_early` and nearby route focuses.
  - Moldova route row: mutual-exclusion lines among `moldova_soviet_collapse_alliance_not_union`, `moldova_soviet_collapse_conditional_union`, and `moldova_soviet_collapse_reject_the_union_question` pass across `moldova_soviet_collapse_smugglers_and_border_committees` and `moldova_soviet_collapse_black_soil_recovery_boards`.
  - Belarus route row: mutual-exclusion lines among `blr_soviet_collapse_national_council_of_minsk`, `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate`, and `blr_soviet_collapse_foreign_corridor_administration` still share a crowded route-choice row.

## Icon coverage table

| File | Focuses | Missing icon assignments | Unique icon ids | Repeated icon ids | Worst repeats |
| --- | ---: | ---: | ---: | ---: | --- |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | 42 | 8 | `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_symbolic_state`, `GFX_focus_soviet_collapse_ancient_returned_names_endgame`, `GFX_focus_soviet_collapse_ancient_restoration_survives`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_league_bargain`, `GFX_focus_soviet_collapse_ancient_guard_old_routes` each repeat across ancient variants. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | 885 | 99 | `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_foreign`, `GFX_focus_MRC_civil_rule`, `GFX_focus_IUL_war_plan`, `GFX_focus_IUL_supply`, `GFX_focus_FEV_diplomatic_plan` each repeat 4 times; `DHC_convoy_autonomy_guarantees` uses `GFX_focus_DHC_legitimacy` at `custom_splinters.txt:14431`, and `KHC_grain_passage_guarantees` uses `GFX_focus_KHC_legitimacy` at `:15624`. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | 113 | 11 | `GFX_focus_CFR_the_builder_state`, `GFX_focus_CFR_municipal_board_elections`, `GFX_focus_CFR_concrete_republic`, and `GFX_focus_CFR_civilian_hegemony_project` repeat 3 times. |
| `005_soviet_collapse_republics.txt` | 501 | 0 | 458 | 22 | `GFX_ukr_soviet_collapse_democratic`, `GFX_moldova_soviet_collapse_ukrainian_corridor`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_central_asia_soviet_collapse_steppe_federation`, and `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards` repeat heavily. |

Icon action needed:
- No missing focus icon assignments were found.
- Repeated icon ids are still common enough to reinforce the "same tree with renamed nodes" feeling, especially in ancient variants and republic regional templates.
- I did not edit icon references except preserving them while moving coordinates.

## Localisation and reward mismatch list

No missing focus name or description localisation was found by key scan.

Mismatch risks:
- `PRA_*` moving railway-state titles promise a unique mobile sovereignty mechanic, but many rewards still look like ordinary authority/recognition/depot helper bundles.
- `TSC_*` Tunguska/star/observatory titles promise anomalous science or signal mechanics, but route payoffs are largely generic helpers, stockpiles, buildings, and claims.
- `RMC_*` reliquary/martyr/procession titles promise cultic manpower and legitimacy loops, but most rewards do not visibly create a procession or reliquary system.
- `DSC_*`, `NRF_*`, and `ICD_*` death-state/revenant titles promise overpowering supernatural or militarized identity routes; current compact trees do not yet provide enough direct units, naval/port assets, coercive command, decision hooks, or AI strategy changes.
- Ancient `*_returned_names_endgame` titles imply restored-state endpoint payoffs, but the trees remain 16-focus stubs with repeated ancient helper/icon patterns.
- The generic custom-splinter tooltip at `localisation/english/005_soviet_collapse_custom_countries_l_english.yml:1791` is accurate to the implementation but too broad to make focus outcomes feel distinct.

## AI behavior gaps

Mechanical status:
- Every audited focus has an `ai_will_do` block.
- Every audited focus has `search_filters`.

Behavioral gap:
- Most `ai_will_do` coverage appears to be basic per-focus weighting rather than route-aware strategic behavior. Only 24 focuses call AI strategy effects directly across 1698 focuses.
- Custom 47-focus templates often have no AI strategy-effect focuses despite having several identity routes. The AI can finish branches, but it does not consistently receive route-specific aggression, diplomacy, industry, logistics, or consolidation priorities.
- Chaos successors meant to be very overpowered need AI behavior tied to route identity: expansion routes should use front/target strategy, military/logistics routes should prioritize supply and force buildup, diplomacy/league routes should avoid wasting time on incompatible conquest, and industrial routes should bias construction/rebuild decisions.

## High-priority fixes first

1. Replace generic route-identity tooltip spam:
   - Target the 355 uses of `soviet_collapse_custom_splinter_route_identity_reward_tt`.
   - Split into route-family-specific tooltips: political consolidation, industrial mandate, logistics depot, military command, diplomatic recognition, league construction, expansion claim, and high-chaos assault.
   - This can be done without adding new mechanics, and it directly addresses visible reward spam.

2. Deepen compact high-chaos splinters:
   - `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` are currently the clearest mismatch between lore and gameplay depth.
   - Each needs an exact small system: rail-state decisions for `PRA`, anomaly/signal projects for `TSC`, procession/reliquary recruitment for `RMC`, dead-army command for `DSC`, convoy/port fleet for `NRF`, and coercive commissariat order for `ICD`.

3. Expand ancient restorations:
   - `KZR`, `SOG`, `KHW`, and `ALN` need political, industrial, expansion, military/logistics, and diplomatic routes instead of 16-focus mirrored stubs.
   - This is broad rework and should not be attempted as a subagent micro-patch.

4. Fix remaining republic route-choice layout:
   - Baltic, Moldova, and Belarus same-row mutual-exclusion spans remain after this patch.
   - This should be a dedicated layout pass to avoid accidentally crossing prerequisite rows in large republic trees.

5. Add route-aware AI strategy effects:
   - Focus trees already have `ai_will_do`, but route identity is not strongly reflected in AI strategy.
   - Add route-completion strategy effects to expansion, industrial, military/logistics, and diplomacy endpoints.

## Exact implementation tranches for broad rework

Tranche 1: compact high-chaos successor mechanics
- Countries: `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`.
- Add 4-8 focuses per country only after design approval, or patch existing endpoints if the parent wants minimal churn.
- Tie each to a small decision/effect loop already in Event005 where possible.
- Deliverables: route-specific tooltip keys, one or two route-specific scripted helper calls, AI strategy effects, and endpoint rewards that grant claims/units/industry/decision unlocks directly relevant to the identity.

Tranche 2: ancient restoration tree expansion plan
- Countries: `KZR`, `SOG`, `KHW`, `ALN`.
- Required routes: political restoration, industrial/old workshop network, military/logistics guard, expansion/old borders, diplomatic league or survival.
- Deliverable should be a full plan first because this requires more than small coordinate/reward patches.

Tranche 3: republic route-layout and fork-meaning pass
- Files: primarily `005_soviet_collapse_republics.txt`.
- Fix Baltic, Moldova, and Belarus same-row mutual-exclusion spans.
- Check that mutually exclusive routes change downstream availability and not only grant alternative names.
- Add route-specific AI and reward tooltips where low-risk.

Tranche 4: custom template reward differentiation
- Countries: `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`.
- Replace repeated helper packages with route-specific payloads while preserving current tree size.
- Priority candidates are templates with many stockpile rewards and repeated icon ids: `ARD`, `KHC`, `UWD`, `DHC`, `FEV`, `BSC`, `BAC`, `IUL`, `NLC`, `KRS`.

Tranche 5: icon identity pass
- Do not touch flag/interface sprite files in this audit scope.
- Later, define or assign more distinct focus icons for repeated ancient/republic/template icons and document any needed placeholder sprite replacements under the Event005 asset docs.

## Patch details

Changed file:
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`

Changed focus ids:
- `UDC_loyalist_statute_guarantees`
- `SDZ_chain_of_custody_statutes`
- `GAC_harvest_truce_guarantees`
- `DHC_convoy_autonomy_guarantees`
- `KHC_grain_passage_guarantees`

Localisation keys changed: none.

Icon ids changed: none.

Gameplay behavior changed: no rewards, prerequisites, bypasses, mutual exclusions, AI weights, focus filters, decisions, ideas, events, or scripted effects were changed.

Layout behavior changed:
- The five listed settlement/loyalist payoff focuses are now below their fork rows, reducing custom-splinter pathline overlap risk.

## Validation run

Commands/checks run:
- Brace-balance parser over all four `005_soviet_collapse*.txt` focus files: all files balanced, minimum depth never below zero.
- Focus id parser over all four focus files: 1698 focus blocks, 1698 unique ids, duplicate ids 0.
- Focus scan: missing `ai_will_do` 0, missing `search_filters` 0, missing icons 0, missing focus name localisation 0, missing focus description localisation 0.
- Layout scan after patch: same-coordinate focus conflicts 0, upward/sideways prerequisites 0, same-row prerequisite spans 0, same-row mutual-exclusion spans reduced from 15 to 10.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`: passed with no output.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_*.txt common/scripted_effects/005_soviet_collapse_effects.txt localisation/english/005_soviet_collapse*.yml`: no unsupported `<=` or `>=` operators found in checked files.

Skipped validation and why:
- No live in-game validation or focus-tree screenshot validation was run from this subagent pass.
- No gfx/interface sprite validation was run because the user explicitly forbade touching flag/interface/sprite files and this pass only audited focus icon identifiers inside focus files.
- No commit was created because the same files were already dirty with parent/user changes before this pass; staging a commit would risk mixing unrelated work into the audit patch.

## Remaining route risks

- Broad tree-depth complaints are valid. Many branches are structurally present but still mechanically shallow or helper-led.
- Chaos successor overpowered identity is inconsistent: large countries like Kazakhstan have breadth, while compact custom/ancient trees do not yet feel like world-shaping chaos countries.
- Mutually exclusive forks often exist syntactically, but several need downstream consequences, route-specific AI, and visible mechanics so the fork matters beyond choosing a label and reward bundle.
- Remaining republic pathline risks should be fixed before a completion claim.
- Reward tooltip spam remains the most visible non-layout issue after this pass.

