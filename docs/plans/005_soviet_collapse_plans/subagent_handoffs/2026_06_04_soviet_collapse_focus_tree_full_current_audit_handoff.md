# 2026-06-04 Event005 Soviet Collapse Focus Tree Full Current-State Audit

Role: `chaosx_focus_tree_auditor`

Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Related localisation was not edited because no focus text/tooltips were patched.

Hard constraint status:

- No `gfx/flags/*.tga` files were opened for edit or modified.
- `git status --short gfx/flags` returned no entries after the audit.
- No gameplay, localisation, gfx, or flag patches were made.

## References Consulted

Offline Paradox wiki pages consulted before opening Chaos Redux gameplay files:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`

Vanilla documentation and precedents consulted:

- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `~/projects/Hearts of Iron IV/common/script_constants/documentation.md`
- `~/projects/Hearts of Iron IV/common/focus_inlay_windows/documentation.md`
- `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`
- `~/projects/Hearts of Iron IV/common/national_focus/poland.txt`
- `~/projects/Hearts of Iron IV/common/national_focus/generic.txt`

Repo skills used:

- `hoi4-focus-trees`
- `chaos-redux-subagents`
- `chaos-redux-events`
- `hoi4-decisions-missions`

## Current Tree Inventory

The four audited files currently contain 41 focus trees and 1,698 `focus = { ... }` blocks.

| File | Trees | Focus count |
| --- | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 9 | 501 |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1,068 |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 |
| `005_soviet_collapse_ancient_restorations.txt` | 4 | 64 |

Parser findings:

- No duplicate focus IDs were found across the four audited files.
- No exact duplicate focus coordinates were found inside the same tree.
- No non-reciprocal `mutually_exclusive` pairs were found by token scan.
- No `<=` or `>=` operators were found in the four audited focus files.

The absence of duplicate IDs/coordinates does not mean layout is good. Several trees are visually over-wide, route locks are often hidden behind `available` blocks instead of visible mutual-exclusion lines, and many branches remain reward-helper ladders rather than distinct gameplay routes.

## Top 20 Ranked Actionable Issues

### 1. Systemic reward-helper spam is still the dominant reward pattern

Evidence:

- `soviet_collapse_apply_focus_depot_and_supply_control` appears in 141 focuses, including `ukr_soviet_collapse_seal_the_grain_ledgers` at `005_soviet_collapse_republics.txt:81`, `soviet_collapse_secure_ministry_ledgers` at `:2359`, and many more.
- `soviet_collapse_apply_focus_military_consolidation` appears in 132 focuses, including `ukr_soviet_collapse_war_without_a_declaration` at `005_soviet_collapse_republics.txt:164` and `ukr_soviet_collapse_officers_above_parties` at `:531`.
- `soviet_collapse_apply_focus_legal_recognition` appears in 108 focuses, including `ukr_soviet_collapse_guard_the_telegraph_house` at `005_soviet_collapse_republics.txt:54` and `blr_soviet_collapse_minsk_emergency_office` at `:8715`.

Impact: The trees still feel like repeated stat/institution increments. Even when helpers are better than raw `add_ideas`, the player repeatedly receives the same hidden reward family under different labels.

Recommended patch owner: `chaosx_scripted_system_architect` for reward-family redesign, then parent focus implementation agent for route-specific replacement rewards.

### 2. Most custom splinter trees still share the same 47-focus skeleton

Evidence:

- `BSC_soviet_collapse_focus_tree` starts at `005_soviet_collapse_custom_splinters.txt:4300` with generic `BSC_birth`, `BSC_first_guard`, and `BSC_stores` at `:4316`, `:4336`, and `:4365`.
- `TNC_soviet_collapse_focus_tree` repeats the same `birth`, `first_guard`, `stores` opening at `005_soviet_collapse_custom_splinters.txt:5419`, `:5435`, `:5455`, and `:5484`.
- `ALA_soviet_collapse_focus_tree` repeats the same pattern at `005_soviet_collapse_custom_splinters.txt:6548`, `:6564`, `:6584`, and `:6613`.

Impact: The 47-focus count masks sameness. Names and some helper calls vary, but the route architecture and reward rhythm remain template-like across many countries.

Recommended patch owner: Parent focus implementation agent with `chaosx_improvement_loop_planner` for per-country identity addenda.

### 3. Most chaos/splinter countries are not aggressive enough

Evidence:

- Across `005_soviet_collapse_custom_splinters.txt`, most 47-focus custom splinter trees have no direct `create_wargoal`, no direct claims, and no `add_ai_strategy`.
- Direct war/AI aggression is concentrated in a small subset: `PRA_rails_over_capitals` at `:1701`, `TSC_starfall_mandate` at `:2189`, `RMC_resurrection_without_state` at `:2688`, `DSC_congress_of_the_dead_army` at `:3247`, `NRF_northern_revenant_fleet` at `:3770`, and `ICD_commissariat_without_end` at `:4239`.
- `BSC_soviet_collapse_focus_tree` at `:4300`, `TNC_soviet_collapse_focus_tree` at `:5419`, and `ALA_soviet_collapse_focus_tree` at `:6548` have no direct war/claim/AI-strategy payloads in the parsed focus blocks.

Impact: High-chaos countries often play like normal weak successors with darker names. They need stronger war goals, claims, unit packages, pressure decisions, and AI conquest strategy.

Recommended patch owner: Parent focus implementation agent; `chaosx_decision_mission_auditor` for aggression decisions after focus rewards are wired.

### 4. Republic and regional trees are still too passive on expansion

Evidence:

- `soviet_collapse_ukraine_focus_tree` at `005_soviet_collapse_republics.txt:17` has 83 focuses, but parsed direct war goals and direct claims are both 0.
- `soviet_collapse_belarus_focus_tree` at `:8699` has 53 focuses, but parsed direct war goals and direct claims are both 0.
- `soviet_collapse_baltic_focus_tree` at `:4571` has 42 focuses, but parsed direct war goals and direct claims are both 0.
- `soviet_collapse_central_asia_focus_tree` at `:6435` has one claim-focused item, `central_asia_soviet_collapse_khwarazm_restoration_debate` at `:7380`.

Impact: These trees have politics, logistics, League preparation, and recognition, but they do not create enough direct map pressure for a Soviet collapse scenario.

Recommended patch owner: Parent focus implementation agent.

### 5. Ukraine is deep but still reward-heavy and indirect on expansion

Evidence:

- `ukr_soviet_collapse_direct_national_claims` at `005_soviet_collapse_republics.txt:1723` calls `soviet_collapse_apply_ukr_direct_national_claims`, `soviet_collapse_apply_focus_military_consolidation`, and a tooltip, but has no direct `create_wargoal` or `add_ai_strategy`.
- `ukr_soviet_collapse_black_sea_hegemony` at `:1753` unlocks `ukr_soviet_collapse_black_sea_security_mission`, then hides a package helper.
- `ukr_soviet_collapse_great_steppe_and_sea_plan` at `:1853` again relies on helper packages and flags, not direct aggression.

Impact: Ukraine has more route depth than most trees, but its expansion lanes feel like unlock/tooltip chains. The major regional actor should more visibly change the map, create war pressure, and drive AI behavior.

Recommended patch owner: Parent focus implementation agent, then `chaosx_decision_mission_auditor` for the external border/Black Sea decision payloads.

### 6. Belarus has strong theme but no hard strategic payoff

Evidence:

- `blr_soviet_collapse_which_road_is_belarus` at `005_soviet_collapse_republics.txt:8783` opens the route question.
- `blr_soviet_collapse_military_transit_directorate` at `:8873`, `blr_soviet_collapse_rail_war_state` at `:9350`, and `blr_soviet_collapse_the_forest_general_staff` at `:9534` build a rail/forest military identity.
- No direct war goals, direct claims, or `add_ai_strategy` were parsed in the Belarus tree.

Impact: The rail/forest identity is readable, but the payoff is defensive/logistical rather than strategically assertive. Belarus needs a real corridor doctrine, coercion/ultimatum tools, League logistics rules, or regional intervention authority.

Recommended patch owner: Parent focus implementation agent.

### 7. League-country trees are shared too broadly and not adapted enough

Evidence:

- `soviet_collapse_baltic_focus_tree` at `005_soviet_collapse_republics.txt:4571` is assigned to `LIT`, `LAT`, and `EST` through one country selector.
- `baltic_soviet_collapse_legal_continuity_government` at `:4694`, `baltic_soviet_collapse_baltic_league_first` at `:4738`, and `baltic_soviet_collapse_foreign_protection_council` at `:4768` are generic route labels for all three tags.

Impact: Shared trees are acceptable only when adapted. This tree does not provide enough Estonia/Latvia/Lithuania-specific politics, claims, security problems, sponsor logic, or postwar settlement.

Recommended patch owner: Parent focus implementation agent with country-package audit support.

### 8. Factory successor layout and branch shape remain uneven

Evidence:

- `CFR_soviet_collapse_focus_tree` starts at `005_soviet_collapse_factory_successors.txt:15`; the opening chain `CFR_count_the_cranes`, `CFR_the_trust_office_takes_the_seal`, `CFR_ration_cards_for_workers`, `CFR_emergency_cement_accounts`, and `CFR_the_unfinished_city_speaks` at `:31`, `:56`, `:83`, `:107`, and `:131` all sit at `x = 17` from `y = 0` through `y = 4`.
- `MFR_soviet_collapse_focus_tree` starts at `:1764` and opens with a similar vertical state-building chain from `MFR_orders_outlive_ministries` at `:1780` through `MFR_factory_guard_oaths` at `:1856`.

Impact: Factory successors have more mechanics than most splinters, but some openings still read like vertical checklists. The visual tree should separate political board, industrial production, security, expansion, and failure/high-chaos lanes sooner.

Recommended patch owner: Parent focus layout pass.

### 9. OGB is too small for its premise

Evidence:

- `OGB_soviet_collapse_focus_tree` at `005_soviet_collapse_factory_successors.txt:1156` has 23 focuses.
- It has direct aggression at `OGB_the_volga_cannot_have_two_seals` at `:1514` and `OGB_the_old_name_survives_modern_war` at `:1722`, plus claims at `OGB_claim_the_old_trade_cities` at `:1600`, but the overall tree is shorter than the 47-focus splinter shell.

Impact: Old Bolghar has formable/restoration potential but less branch depth than many generic splinters. It needs more internal legitimacy, Volga diplomacy, Muslim/Tatar/Bolghar identity conflict, industry, military, and post-formation integration.

Recommended patch owner: `chaosx_improvement_loop_planner`, then parent focus implementation agent.

### 10. Ancient restoration trees are too compact and mirrored

Evidence:

- `KZR_soviet_collapse_ancient_focus_tree` at `005_soviet_collapse_ancient_restorations.txt:12` has 16 focuses.
- `SOG_soviet_collapse_ancient_focus_tree` at `:407`, `KHW_soviet_collapse_ancient_focus_tree` at `:796`, and `ALN_soviet_collapse_ancient_focus_tree` at `:1189` each also have 16 focuses with matching `old_*_border_files`, symbolic-authority, charter, survival, and final border/road focuses.
- Each ancient tree has one direct war focus and three claim-bearing focuses, but little political route branching or distinct economic/military depth.

Impact: They are better at direct claims than republics, but their design is still too close to a mirrored mini-template.

Recommended patch owner: `chaosx_improvement_loop_planner` for distinct ancient-route expansions.

### 11. Focus-to-decision integration is concentrated, not systemic

Evidence:

- Only 79 of 1,698 parsed focuses contain `unlock_decision*` or `activate_decision*`.
- Many 47-focus custom splinter trees have 0 parsed decision unlocks, including `BSC_soviet_collapse_focus_tree` at `005_soviet_collapse_custom_splinters.txt:4300`, `TNC_soviet_collapse_focus_tree` at `:5419`, and `ALA_soviet_collapse_focus_tree` at `:6548`.
- PRA is an exception with 14 decision-touching focuses in 22 focuses, starting at `PRA_soviet_collapse_focus_tree` at `:1199`.

Impact: Most countries still receive focus rewards instead of evolving decision categories. This weakens replayability and makes route choices feel less interactive.

Recommended patch owner: Parent focus implementation agent plus `chaosx_decision_mission_auditor`.

### 12. Route-specific AI is too thin

Evidence:

- Only 24 focuses across all four files directly contain `add_ai_strategy`.
- None of the republic shared trees parsed direct `add_ai_strategy` payloads.
- Most route differentiation is `ai_will_do`, such as `ukr_soviet_collapse_black_banner_compact` at `005_soviet_collapse_republics.txt:268` with `base = 2`, or `blr_soviet_collapse_foreign_corridor_administration` at `:8898` with foreign-appetite weighting.

Impact: `ai_will_do` can select focuses, but it does not make countries aggressive, defensive, pro-faction, anti-SOV, or expansionist after focus completion. Chaos countries especially need persistent AI strategies.

Recommended patch owner: Parent focus implementation agent; consider `hoi4-mtth` only if focus AI becomes cluttered.

### 13. Focus filters often do not match visible rewards

Evidence:

- `ukr_soviet_collapse_first_republican_line` at `005_soviet_collapse_republics.txt:122` builds a capital fort but has only `FOCUS_FILTER_ARMY_XP FOCUS_FILTER_MANPOWER`.
- `blr_soviet_collapse_orders_printed_like_timetables` at `:9029` builds a railway in `random_owned_controlled_state`, but has no `FOCUS_FILTER_INDUSTRY`.
- `baltic_soviet_collapse_legal_continuity_government` at `:4694` adds infrastructure in a random owned state but has only political/stability filters.

Impact: Search/filter UX is misleading. Players looking for construction, industry, expansion, or manpower focuses will miss relevant nodes.

Recommended patch owner: Focus-tree subagent patch pass.

### 14. Route locks are often hidden instead of visible mutual exclusions

Evidence:

- Ukraine route locks use hidden `available` exclusions rather than visible `mutually_exclusive` arrows: `ukr_soviet_collapse_socialist_republic_without_moscow` at `005_soviet_collapse_republics.txt:293`, `ukr_soviet_collapse_black_banner_compact` at `:268`, `ukr_soviet_collapse_elections_under_shellfire` at `:308`, `ukr_soviet_collapse_officers_above_parties` at `:531`, and `ukr_soviet_collapse_protectorate_debate` at `:1678`.
- The parser found no missing reciprocal mutual exclusions, but this is partly because several major identity choices are not represented as mutual exclusions at all.

Impact: The choices may work mechanically, but the player does not get clean visual route-identity lines. This matches the user complaint that pathlines/mutual exclusions remain ugly.

Recommended patch owner: Focus layout/route-lock pass.

### 15. Some prerequisite lines show OR while availability enforces a different gate

Evidence:

- `blr_soviet_collapse_which_road_is_belarus` at `005_soviet_collapse_republics.txt:8783` has a single `prerequisite` block containing three focuses, which is an OR line display, then `available` requires two of the three through explicit AND pairs.
- `blr_soviet_collapse_join_the_league_when_war_comes` at `:9684` uses a single prerequisite block containing four route focuses, which displays as route OR, then availability adds a war/threat gate.

Impact: This may be intentional, but the focus tree view will not communicate the actual gating. Use clearer prerequisite architecture, route-specific branch placement, or tooltip-localized custom gates where layout lines would mislead.

Recommended patch owner: Focus layout/route-lock pass.

### 16. Political identity changes are too often flags/helpers rather than visible country changes

Evidence:

- Only 9 parsed focuses across all four files contain direct politics/cosmetic/leader keywords.
- `ukr_soviet_collapse_black_banner_compact` at `005_soviet_collapse_republics.txt:268` is a good visible exception with `set_cosmetic_tag = UKR_BLACK_BANNER`.
- Many route focuses, such as `blr_soviet_collapse_national_council_of_minsk` at `:8829`, `blr_soviet_collapse_socialist_autonomy_without_moscow` at `:8855`, and `blr_soviet_collapse_military_transit_directorate` at `:8873`, set route flags and helpers but do not directly change ruling party, leader, cosmetic name, or country package.

Impact: Political routes often do not visibly transform the country enough. Focuses should change leadership, ideology, party names, laws, advisors, cosmetics, or country identity where appropriate.

Recommended patch owner: Parent focus implementation agent plus `chaosx_country_package_auditor`.

### 17. Direct unit/template rewards are thin

Evidence:

- The audit found no direct `division_template`, `load_oob`, or direct unit-template blocks in focus rewards by simple scan.
- Unit effects are mostly hidden helper calls, such as `soviet_collapse_spawn_focus_mobile_column` in `ukr_soviet_collapse_the_directory_state` at `005_soviet_collapse_republics.txt:678`, and repeated assault-column helpers such as `soviet_collapse_spawn_custom_splinter_assault_columns` in `TSC_starfall_mandate` at `005_soviet_collapse_custom_splinters.txt:2189`.

Impact: Hidden helper unit packages can work, but focus rewards do not visibly explain or diversify military growth enough. Aggressive chaos tags should receive more obvious elite units, templates, militia packages, and AI production behavior.

Recommended patch owner: Parent focus implementation agent with country package review.

### 18. High-chaos branches are often too low-weighted and late-gated

Evidence:

- `ukr_soviet_collapse_black_banner_compact` at `005_soviet_collapse_republics.txt:268` has `ai_will_do base = 2`.
- `ukr_soviet_collapse_the_bread_line_becomes_a_border` at `:2000`, `ukr_soviet_collapse_black_soil_oath` at `:2087`, and `ukr_soviet_collapse_grain_census_of_everyone` at `:2144` also use low base weights and mostly helper effects.
- Custom splinter high-chaos helper `soviet_collapse_apply_focus_high_chaos_identity` appears 60 times, but only a minority pair it with direct conquest pressure.

Impact: High chaos should produce overpowered, dangerous, aggressive paths. Current weighting and payloads often make it a flavor branch rather than a campaign threat.

Recommended patch owner: Parent focus implementation and balance pass.

### 19. Layout still has over-wide trees and checklist trunks

Evidence:

- Ukraine spans `x = 4..34`, `y = 0..18` from `soviet_collapse_ukraine_focus_tree` at `005_soviet_collapse_republics.txt:17`.
- Belarus spans `x = 3..29`, `y = 0..16` from `soviet_collapse_belarus_focus_tree` at `:8699`.
- Kazakhstan spans `x = 2..36`, `y = 0..12` from `soviet_collapse_kazakhstan_focus_tree` at `:10001`.
- CFR's opening trunk uses `x = 17` repeatedly at lines `005_soviet_collapse_factory_successors.txt:31`, `:56`, `:83`, `:107`, and `:131`.

Impact: Exact coordinate collisions are gone, but the visual result can still be ugly: too wide, too many long diagonal/orthogonal routes, and some vertical checklist trunks.

Recommended patch owner: Focus layout pass.

### 20. Formatting and placeholder-comment residue makes review harder

Evidence:

- Ukraine has multiple empty role comments where no focus follows immediately, for example around `005_soviet_collapse_republics.txt:186`, `:198`, `:285`, and later route sections.
- Several focuses have irregular indentation that is not a gameplay break but makes visual review harder, such as `ukr_soviet_collapse_re_register_the_party` around `:409`, `ukr_soviet_collapse_protectorate_debate` around `:1678`, and Baltic focuses around `:4738` and `:4768`.

Impact: This increases audit cost and makes layout/pathline work harder. It also suggests prior generated or mechanical edits were not fully polished.

Recommended patch owner: Focus cleanup pass after gameplay route fixes.

## Tree-Specific Notes

### Ukraine

Status: The deepest current republic tree. It has real route families, multiple route locks, foreign/League content, and high-chaos branches. Remaining problems are not lack of count; they are payoff quality, visible route exclusivity, and direct strategic pressure.

Priority fixes:

- Add direct war/claim/AI strategy to expansion capstones where appropriate.
- Convert hidden route-lock gates into visible mutual exclusions where pathlines can be made clean.
- Reduce repeated legal/socialist/military helper calls in favor of route-specific decisions, units, advisors, and visible identity changes.

### Belarus

Status: The rail/forest identity is readable. The tree has a stronger structure than many custom splinters, but it lacks hard strategic payoff.

Priority fixes:

- Give the military transit/rail war route direct coercion, border control, or war-plan mechanics.
- Make League logistics into a concrete shared mechanic, not only helper/decision unlocks.
- Add more route-specific AI behavior after rail war, neutrality, or foreign corridor commitments.

### League and Regional Shared Trees

Status: Baltic, Caucasus, Central Asia, Moldova, internal republic, and breakaway shared trees are better than generic fallback, but still feel shared. The Baltic tree especially needs tag-specific identity.

Priority fixes:

- Add country-specific branches or scripted-localised route variants for tags sharing a tree.
- Add more regional claims, guarantees, protectorate/settlement outcomes, and AI strategy.
- Ensure League member/founder routes have membership rules, refusal logic, shared war goals, and postwar handling.

### Factory Successors

Status: CFR and MFR have more distinct mechanics. OGB is too small. Layout and reward variety are still uneven.

Priority fixes:

- Expand OGB into a full restoration/federal/Volga route package.
- Break CFR/MFR vertical openings into distinct board, factory, security, expansion, and crisis lanes.
- Make industrial branches produce visible map, production, and resource outcomes with decisions and AI behavior.

### Chaos and Custom Splinters

Status: Early high-chaos tags have some direct aggression, but most custom splinters are not dangerous enough. The repeated 47-focus shell remains the largest design issue in this audit.

Priority fixes:

- For every high-chaos splinter, add at least one direct conquest/pressure branch with war goals, claims, units, and persistent AI strategy.
- Replace generic `first_guard`, `stores`, `legitimacy`, `doctrine`, `foreign`, `settlement`, `industry_plan`, `hidden_doctrine`, `endgame` rhythm with per-country mechanics.
- Ensure each chaos state has an OP but costly style: death-state manpower, machine-state production, rail-state mobility, fleet-state naval raiding, commune-state militia spam, etc.

### Ancient Restorations

Status: Better direct claims than republics, but too compact and mirrored. These should be weird, politically sharp, and regionally disruptive.

Priority fixes:

- Expand each ancient tree beyond 16 focuses.
- Add distinct politics, archaeology/legitimacy mechanics, religious/cultural authority, and post-conquest integration.
- Add route-specific AI aggression and hidden formable/identity payoffs where justified.

## Narrow Patches Made

None.

Reason: I did not find a small, isolated focus bug that was safer to patch than to report. The current gaps are broad route-depth, reward-design, AI-aggression, and layout-quality issues. The working tree is also already heavily modified by parent/user work, so I avoided touching gameplay files.

## Validation Commands Run

- `rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|National focus'`
- `rg -n` reference scans against the offline wiki pages listed above.
- `find "$HOME/projects/Hearts of Iron IV" -path '*/documentation*' -type f`
- `rg -n` scans in vanilla `soviet.txt`, `poland.txt`, and `generic.txt` for focus syntax, filters, mutual exclusions, claims, war goals, and AI.
- `git status --short`
- Structured Python parse of the four audited focus files for tree count, focus count, duplicate IDs, duplicate coordinates, reciprocal mutual exclusions, helper counts, reward categories, decision hooks, aggression hooks, and filter mismatch samples.
- `git status --short gfx/flags`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`

## Remaining Risks

- This was a static script audit, not an in-game visual inspection. I can identify layout risk from coordinates and route structure, but not exactly how every line renders in the focus UI.
- Hidden helper payloads may contain stronger mechanics than the focus files reveal. The focus player experience still depends on what the focus block visibly communicates and unlocks.
- Some direct claims/war behavior may be inside helper effects rather than focus blocks. That still weakens focus auditability and tooltip clarity unless the helper produces clean custom tooltip text and route-specific AI.
- No localisation was patched or audited in detail because no focus text/tooltips were changed.

## Flag Statement

No flag files were touched. No `gfx/flags/*.tga` edits were made or proposed. The audit only reviewed focus references and script behavior.
