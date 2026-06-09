# Event005 Soviet Collapse Focus Delta Audit

Timestamp: 2026-06-04 17:34 UTC
Subagent role: `chaosx_focus_tree_auditor`
Mode: read-only gameplay/localisation/assets audit. This markdown report is the only file written.

## Scope

Fresh delta audit of current Event005 Soviet Collapse focus trees against the latest objective:

- reduce idea/reward-helper spam
- make political, industrial, and expansion branches legible
- clean random/messy mutexes and pathline risks
- make chaos countries feel overpowered and aggressive through focuses
- close focus-linked expansion, decision, coring, unit, and mechanic gaps

Files inspected:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- existing reports in `docs/plans/005_soviet_collapse_plans/subagent_handoffs/`

No `gfx/flags`, flag sprites, `.tga` files, gameplay scripts, localisation, interface, or asset files were edited.

## Delta Baseline

Already addressed by existing parent/subagent reports:

- Direct focus-level idea spam is gone. Current parser found `0` direct `add_ideas`, `remove_ideas`, `swap_ideas`, or `add_timed_idea` operations in focus completion rewards.
- Same-focus duplicate direct helper calls were not found.
- Duplicate focus coordinates were not found in the current four focus files.
- MFR ownership-route mutexes are now visible.
- Some Ukraine, Belarus, CFR, DSC, ancient restoration, BSC/TNC/ALA, UDC, ARD, NLC, and high-chaos helper payloads were strengthened.

Still current:

- 1,698 focus blocks across 41 focus trees.
- Generic helper rhythm remains high: `soviet_collapse_apply_focus_depot_and_supply_control` 135 calls, `soviet_collapse_apply_focus_military_consolidation` 127, `soviet_collapse_apply_focus_legal_recognition` 103, `soviet_collapse_apply_focus_republican_compact_plan` 80, `soviet_collapse_apply_focus_foreign_channel` 65, `soviet_collapse_apply_focus_high_chaos_identity` 48.
- Many trees still lack focus-staged decisions or direct expansion/coring/wargoal evidence in the focus file, even where helper payloads may add some behavior.

## Top 20 Current Problems

1. Generic helper-reward rhythm is still the dominant focus experience.
   Evidence: helper counts above; representative same-shape early FTH chain at `common/national_focus/005_soviet_collapse_custom_splinters.txt:52`, `:77`, `:101`, `:125`, `:149`, `:173`, `:197`, `:221`. The helpers are stronger than before, but many countries still read as the same scaffold with different tag prefixes.

2. Many trees still have zero focus-staged decision links.
   Evidence: zero decision-link focus trees include the generic breakaway tree (`common/national_focus/005_soviet_collapse_republics.txt:2355`), internal republic tree (`:3167`), Baltic tree (`:4657`), Moldova tree (`:8688`), and many 47-focus custom splinters such as FTH (`common/national_focus/005_soviet_collapse_custom_splinters.txt:52`) and BBH/KRS/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC.

3. Several large republic/shared trees still show no direct focus-file expansion payload.
   Evidence: Baltic, Belarus, Kazakhstan, Moldova, internal republic, and generic breakaway parsed with `0` direct focus-file `add_state_claim`, `add_state_core`, `create_wargoal`, or `declare_war_on` calls. Examples: Baltic opening and route fork at `common/national_focus/005_soviet_collapse_republics.txt:4657` and `:4745`; Belarus rail/League branch at `:9777` through `:10090`; Kazakhstan federation branch at `:10813` and `:11339`; Moldova endpoints at `:8688` and `:8730`.

4. Moldova still has the clearest remaining hard pathline defect.
   Evidence: `moldova_soviet_collapse_the_river_state` at `common/national_focus/005_soviet_collapse_republics.txt:8730` has a same-column prerequisite path from `moldova_soviet_collapse_river_guard_brigades` to `(14,13)` running through `moldova_soviet_collapse_tiraspol_depot_belt` at `(14,7)`. It also has very long prerequisites from the route fork and west/east branches (`:8694-8703`, `:8736-8745`).

5. Moldova's political/river/Prut branches still converge as a messy endpoint instead of real branch families.
   Evidence: `moldova_soviet_collapse_republic_of_crossings` at `common/national_focus/005_soviet_collapse_republics.txt:8688` OR-joins seven route branches and rewards a generic republican compact helper plus recognition. `moldova_soviet_collapse_the_river_state` at `:8730` then depends on even more branches, with no focus-staged Moldova decision or direct map payload visible in this file.

6. Central Asia's `the_southern_shield` remains a long OR join after multiple divergent lanes.
   Evidence: `central_asia_soviet_collapse_the_southern_shield` at `common/national_focus/005_soviet_collapse_republics.txt:7272` OR-prereqs five focuses from distant lanes (`:7279-7285`). It unlocks regional defense decisions, but the focus still acts as a broad join rather than a clean expansion/security branch endpoint.

7. Kazakhstan is large but still under-exposes expansion and decision mechanics.
   Evidence: 92 focuses, only 4 focus-level decision links and `0` direct focus-file expansion payloads in the parser. Long pathline examples: `kaz_soviet_collapse_steppe_federation_charter` at `common/national_focus/005_soviet_collapse_republics.txt:10813` from `(2,3)` to `(19,5)`, `kaz_soviet_collapse_the_steppe_arbitration_court` at `:11339` back from `(19,5)` to `(2,6)`, resource branch jump at `:11656`.

8. Belarus rail depth improved, but rail/League payoff still over-converges and expansion remains absent.
   Evidence: `blr_soviet_collapse_prepare_league_freight_tables` at `common/national_focus/005_soviet_collapse_republics.txt:9777`, `join_the_league_when_war_comes` at `:9806`, `minsk_supplies_the_front` at `:9852`, and `the_league_depot_at_minsk` at `:10090` form a long multi-prereq rail/League lane. Parser found `0` direct Belarus expansion effects.

9. Ukraine layout is improved but still has a long political branch line and a crowded democratic/military route join.
   Evidence: `ukr_soviet_collapse_provincial_governors_or_elected_radas` at `common/national_focus/005_soviet_collapse_republics.txt:902` requires `rural_deputy_bloc` from `(10,8)` and `minority_autonomy_statutes` from `(24,11)`, landing at `(23,12)`. This remains one of the longest Ukraine edges after the parent layout tranche.

10. Baltic route locks remain hidden through `available` checks rather than fully visible route structure.
    Evidence: `baltic_soviet_collapse_the_legal_state_or_the_front_state` at `common/national_focus/005_soviet_collapse_republics.txt:4745` feeds route choices such as `legal_continuity_government` at `:4761` and `military_border_government` at `:4793`; current route exclusivity is mostly hidden in `available` blocks rather than visible mutexes. The tree also has no focus-staged decisions or direct expansion effects.

11. Caucasus is still mostly shared-helper state-building with limited focus-staged mechanics.
    Evidence: opening focuses at `common/national_focus/005_soviet_collapse_republics.txt:5621`, `:5634`, `:5650`, and `:5666` are helper/stat rewards. The tree has only 2 focus-level decision hooks and `0` direct expansion effects in the parser despite oil/pass/league themes.

12. The 16-focus ancient restorations remain compact side trees after the symbolic-core patch.
    Evidence: KZR/SOG/KHW/ALN each have 16 focuses. Charter joins at `common/national_focus/005_soviet_collapse_ancient_restorations.txt:288`, `:697`, `:1096`, and `:1508` OR-join the symbolic and expansion forks into one focus. This is legal, but it compresses politics, industry, diplomacy, expansion, and settlement into one short spine.

13. Ancient expansion is now strong, but still generic across the four restorations.
    Evidence: expansionist focuses call the same assault/claim/high-chaos neighbor package around `KZR_expansionist_steppe_levy` (`common/national_focus/005_soviet_collapse_ancient_restorations.txt:240`), `SOG_expansionist_merchant_claims` (`:648`), `KHW_expansionist_water_claims` (`:1047`), and `ALN_expansionist_mountain_claims` (`:1457`). They need route-specific postwar decisions, not only shared OP payloads.

14. TSC has better decisions than before, but still lacks a full anomaly mechanic branch.
    Evidence: `TSC_claim_the_impact_zone` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2207` now unlocks a decision and calls expansion helpers, but the tree is still only 18 focuses. The quiet endpoint `TSC_observatory_state` at `:2301` remains a compact republican-compact/stability payoff rather than a separate non-chaos anomaly governance path.

15. RMC and ICD death-state expansion is still too thin before the capstone.
    Evidence: `RMC_claim_the_burial_roads` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2682` adds one scoped claim and high-chaos identity; `ICD_claim_the_unburied_front` at `:4228` does the same pattern, followed by `ICD_grave_columns_march` at `:4249`. These need route-specific forced-march, coring, and dead-roll decision families before the endpoint.

16. NRF is more naval now, but the naval death-state still has only a narrow branch.
    Evidence: `NRF_living_harbor_committees` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:3491`, `NRF_revenant_admiralty` at `:3523`, and `NRF_northern_revenant_fleet` at `:3833` add convoys/naval XP/AI pressure, but the 18-focus tree lacks a full port seizure, convoy raiding, coastal settlement, and naval-invasion branch.

17. OGB remains short and politically flat in its restored-name opening.
    Evidence: `OGB_scholars_guard_the_charter` and `OGB_clerics_guard_the_charter` at `common/national_focus/005_soviet_collapse_factory_successors.txt:1137` and `:1157` are popularity/stability/legitimacy branches; `OGB_society_of_the_restored_name` at `:1299` is still stability plus variable. `OGB_treat_with_idel_ural` at `:1382` gives opinion/AI strategy but no compact decision or joint mechanic.

18. CFR's four-way forks are visible but still mechanically crowded.
    Evidence: governance mutex row at `common/national_focus/005_soviet_collapse_factory_successors.txt:135`, `:165`, `:197`, `:228`; strategy row at `:363`, `:383`, `:417`, `:442`. Some branches now have decisions and construction payloads, but the tree still has many route locks feeding similar construction-mandate outcomes.

19. UDC and SDZ still have long diplomacy-to-statute joins.
    Evidence: `UDC_loyalist_statute_guarantees` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:10893` joins `UDC_command_mediation` and `UDC_diplomatic_plan` across a 20-step edge; `SDZ_chain_of_custody_statutes` at `:12136` has the same pattern across a 19-step edge. Both remain pathline and route-readability risks.

20. BAC and several other 47-focus splinters still have no decision evolution despite local reward depth.
    Evidence: BAC has long war/industry pathlines at `common/national_focus/005_soviet_collapse_custom_splinters.txt:22749` and `:22848`, but the parser found `0` focus-staged decision links. Similar zero-link 47-focus trees include BBH, KRS, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, and BAC.

## Prioritized Patch Order

1. Moldova layout and mechanics first: split `republic_of_crossings` and `the_river_state` into clean river/Prut/eastern-buffer lanes, remove the axis blocker, and add Moldova-specific crossing, Dniester, Romanian, Ukrainian corridor, and postwar settlement decisions.
2. Add decision/mechanic staging to zero-link shared trees: generic breakaway, internal republic, Baltic, Moldova, and the 47-focus custom splinters that still have no focus-staged decisions.
3. Patch Central Asia and Kazakhstan pathlines plus expansion payoffs: break up giant OR joins, add federation/protectorate/settlement decisions, and expose claims/cores/wargoals or regional war missions in focus rewards/tooltips.
4. Expand or explicitly accept the compact special trees. If not accepted as short side trees, TSC/RMC/ICD/NRF and the ancient restorations need 35-45 focus equivalents or dense decision modules covering politics, industry, diplomacy, expansion, and special mechanics.
5. Replace repeated generic helper rewards with per-tag signature helpers. Start with FTH/BBH/KRS/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC so each has a visible special mechanic and one focus-staged decision phase.
6. Rework OGB and CFR branch payoffs: OGB needs restored-name governance and Volga compact decisions; CFR needs clearer route-specific construction mandate spending, protectorate contracts, and fewer same-outcome forks.
7. Run a visual pathline screenshot pass after coordinate changes. Current mechanical checks removed duplicate coords and axis blockers except Moldova, but long diagonal paths remain likely to render poorly.

## Validation Notes

Read-only checks performed:

- Required offline wiki pages and focus-specific wiki page consulted.
- Vanilla focus precedents sampled from `soviet.txt`, `baltic_shared.txt`, and `estonia.txt`.
- Existing Event005 handoffs reviewed, especially reports and parent tranches from 2026-06-04.
- Parser pass over all four Event005 focus files:
  - 41 focus trees
  - 1,698 focuses
  - 0 direct focus idea operations
  - 0 duplicate focus coordinates
  - 1 remaining simple axis-blocking pathline, in Moldova
- `git status --short` inspected to confirm the worktree was already broadly dirty; unrelated changes were ignored.

No gameplay, localisation, asset, flag, sprite, or `gfx/flags` file was edited by this audit.
