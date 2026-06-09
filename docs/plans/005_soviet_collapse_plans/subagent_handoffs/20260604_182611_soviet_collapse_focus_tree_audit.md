# Soviet Collapse Focus Tree Audit Handoff

Timestamp: 2026-06-04 18:26 UTC

Scope: read-only audit of Soviet Collapse focus trees and related decision/scripted surfaces. No gameplay files were edited.

## References Checked

- Repo guidance: `AGENTS.md`
- Skills used: `hoi4-focus-trees`, `chaos-redux-subagents`
- Offline wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus modding
- Vanilla docs/precepts: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `common/decisions/_documentation.md`, `common/ai_strategy/_documentation.md`, `common/on_actions/_documentation.md`, `common/script_constants/documentation.md`
- Vanilla precedent: `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`

## Audit Coverage

Checked files requested by parent:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `localisation/english/005_soviet_collapse*_l_english.yml`

Parsed 41 focus trees and 1,698 focuses with lightweight read-only scripts/searches.

## Executive Findings

1. The trees are not shallow because of low focus count. They are shallow because many focuses collapse into the same handful of generic helper payloads.
2. Direct duplicate `add_ideas` in focus files was not found. The “idea spam” risk is indirect: broad scripted effects add/remove many stage and country identity spirits, while focus rewards repeatedly push the same variable/helper ladders.
3. The most repeated focus reward pattern is `add_stability` plus `soviet_collapse_apply_focus_legal_recognition`, reused 35 times. The helper at `common/scripted_effects/005_soviet_collapse_effects.txt:8747` only advances legal depth, recognition, institution strength, recovery progress, route payload, high-chaos payload, and SOV pressure. It does not itself unlock a distinct country decision, war, core, unit, advisor, leader, or country identity change.
4. The high-use generic helpers are heavily variable/stat oriented:
   - `soviet_collapse_apply_focus_depot_and_supply_control` at `common/scripted_effects/005_soviet_collapse_effects.txt:8859`, used 138 times.
   - `soviet_collapse_apply_focus_military_consolidation` at `common/scripted_effects/005_soviet_collapse_effects.txt:8838`, used 131 times.
   - `soviet_collapse_apply_focus_legal_recognition` at `common/scripted_effects/005_soviet_collapse_effects.txt:8747`, used 108 times.
   - `soviet_collapse_apply_focus_republican_compact_plan` at `common/scripted_effects/005_soviet_collapse_effects.txt:9457`, used 94 times.
5. Custom splinter trees reuse very similar branch skeletons. The generic identity wrappers at `common/scripted_effects/005_soviet_collapse_effects.txt:13873-13945` mostly call payload helpers through `hidden_effect` and are repeated across 13-15 countries.
6. Ukraine has the worst layout problems: one exact duplicate coordinate, five too-close same-row pairs, and most of the 301 parsed pathline crossings.
7. Continuous focus positions are unusually high compared with vanilla defaults, but my grid heuristic did not prove a hard overlap with parsed focus coordinates. Treat this as a visual risk to verify in-game or with screenshots, not a confirmed script overlap.
8. Focus-decision links are inconsistent. Many focuses only show `unlock_decision_tooltip`, while the actual decisions are mostly gated by flags in `common/decisions/005_soviet_collapse_decisions.txt`; most focus IDs/flags are not consumed by the decision file.
9. I did not find a focus/country setup script cause for upside-down flags. No focus-side `set_cosmetic_tag` or orientation/flip parameter appeared in the audited focus files. Likely script-side suspects, if any, would be wrong cosmetic tag assignment or wrong country tag/flag naming, but the visible focus/country setup did not expose such a cause.

## Top 20 Worst Focus IDs For Spam/Repetition

These are the worst representatives of the repeated `add_stability` + `soviet_collapse_apply_focus_legal_recognition` pattern. They should be first candidates for branch-specific replacement rewards, not necessarily all individually broken.

1. `ukr_soviet_collapse_elections_under_shellfire` at `common/national_focus/005_soviet_collapse_republics.txt:321`
2. `FTH_anti_puppet_commune_clause` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:655`
3. `ukr_soviet_collapse_republic_of_laws` at `common/national_focus/005_soviet_collapse_republics.txt:948`
4. `PRA_timetable_law` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1330`
5. `OGB_guard_the_old_capital` at `common/national_focus/005_soviet_collapse_factory_successors.txt:1502`
6. `soviet_collapse_neutrality_under_pressure` at `common/national_focus/005_soviet_collapse_republics.txt:2777`
7. `internal_soviet_collapse_write_the_autonomy_statute` at `common/national_focus/005_soviet_collapse_republics.txt:3231`
8. `BSC_anti_puppet_caravan_clause` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:5165`
9. `caucasus_soviet_collapse_the_border_faiths_and_nations` at `common/national_focus/005_soviet_collapse_republics.txt:5658`
10. `caucasus_soviet_collapse_mountain_federal_compact` at `common/national_focus/005_soviet_collapse_republics.txt:5729`
11. `caucasus_soviet_collapse_capital_claims_the_valleys` at `common/national_focus/005_soviet_collapse_republics.txt:5898`
12. `TNC_samarkand_bukhara_legitimacy` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:5991`
13. `caucasus_soviet_collapse_the_passes_vote` at `common/national_focus/005_soviet_collapse_republics.txt:6263`
14. `central_asia_soviet_collapse_samarkand_letters` at `common/national_focus/005_soviet_collapse_republics.txt:6673`
15. `ALA_local_district_registers` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:7114`
16. `moldova_soviet_collapse_bessarabian_legal_files` at `common/national_focus/005_soviet_collapse_republics.txt:7697`
17. `moldova_soviet_collapse_ministry_seals` at `common/national_focus/005_soviet_collapse_republics.txt:8126`
18. `moldova_soviet_collapse_constitutional_sfat` at `common/national_focus/005_soviet_collapse_republics.txt:8203`
19. `blr_soviet_collapse_minsk_emergency_office` at `common/national_focus/005_soviet_collapse_republics.txt:8815`
20. `blr_soviet_collapse_council_bargains_with_forests` at `common/national_focus/005_soviet_collapse_republics.txt:9100`

## Layout And Pathline Risks

Highest priority layout fixes:

- Exact duplicate coordinate in Ukraine: `ukr_soviet_collapse_the_commander_or_the_cabinet` at `common/national_focus/005_soviet_collapse_republics.txt:625` and `ukr_soviet_collapse_army_of_the_republic` at `common/national_focus/005_soviet_collapse_republics.txt:1120` both resolve to `(21, 6)`.
- Ukraine pathline crossings are severe. Examples:
  - `ukr_soviet_collapse_count_the_depot_keys -> ukr_soviet_collapse_first_republican_line` crosses `ukr_soviet_collapse_moscows_officers_in_our_barracks -> ukr_soviet_collapse_black_sea_defense_staff`.
  - `ukr_soviet_collapse_open_the_liaison_offices -> ukr_soviet_collapse_foreign_advisers_in_plain_coats` crosses multiple military/foreign/expansion links.
  - `ukr_soviet_collapse_advisers_without_flags -> ukr_soviet_collapse_equipment_corridor_authority` crosses several late Ukraine route links.
- Parsed pathlines through focus coordinates:
  - `ukr_soviet_collapse_officers_above_parties -> ukr_soviet_collapse_officer_patronage_lists` passes through the duplicate `(21, 6)` area.
  - `ukr_soviet_collapse_general_staff_war_college -> ukr_soviet_collapse_the_directory_state` passes through `ukr_soviet_collapse_ports_need_soldiers`.
  - `kaz_soviet_collapse_oil_field_protection_orders -> kaz_soviet_collapse_emergency_oil_boards` passes through several Kazakhstan nodes.
- Too-close same-row pairs to widen:
  - Ukraine: `ukr_soviet_collapse_first_republican_line` / `ukr_soviet_collapse_depot_motor_columns`.
  - Ukraine: `ukr_soviet_collapse_workers_congress_in_kharkiv` / `ukr_soviet_collapse_army_supremacy`.
  - Central Asia: `central_asia_soviet_collapse_desert_scout_columns` / `central_asia_soviet_collapse_the_basmachi_amnesty_ledger`.
  - Moldova: `moldova_soviet_collapse_river_guard_brigades` / `moldova_soviet_collapse_ukrainian_grain_road`.
  - Belarus: `blr_soviet_collapse_socialist_autonomy_without_moscow` / `blr_soviet_collapse_last_train_east`.

Continuous panel note:

- Current `continuous_focus_position` values are often `y = 140`, `180`, or `240`, while vanilla Soviet uses `continuous_focus_position = { x = 55 y = 1600 }`.
- No hard overlap was proven by parsed grid coordinates, but the high placement is risky for very wide/late branches. Move panels down after layout cleanup if screenshots show overlap.

## Branch Depth And Country Identity Gaps

Most severe identity gaps:

- Generic custom splinters (`TNC`, `ALA`, `BBH`, `KRS`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`) share many identical helper names: `first_guard`, `stores`, `legitimacy`, `rival`, `doctrine`, `economy`, `league`, `foreign`, `special_arm`, `enemy_front`, `civil_rule`, `propaganda`, `settlement`, `hidden_doctrine`, `extreme_gate`.
- Many custom splinter identity helpers at `common/scripted_effects/005_soviet_collapse_effects.txt:13873-13945` are wrappers with no immediate visible country package change. The payloads may update variables/ideas, but focuses do not reliably change leaders, cosmetic tags, advisors, laws, decision categories, or diplomatic behavior.
- Branches often read as reward ladders: legal/recognition ladder, depot ladder, military ladder, foreign ladder, league ladder. They need country-specific unlocks at branch milestones.
- Political branches rarely route into expansion/industry/decision surfaces strongly enough. A focus that chooses a legal, military, league, foreign, or high-chaos identity should alter later expansion, cores, war decisions, unit templates, and AI strategies.
- Several trees have "mutually exclusive" or route-choice focuses that are mechanically too similar. Confirmed identical pair:
  - `OGB_scholars_guard_the_charter` and `OGB_clerics_guard_the_charter`, `common/national_focus/005_soviet_collapse_factory_successors.txt:1143`, both reduce to `add_stability` in the direct reward signature.

## Aggression And Power Level

The user concern that chaos countries are not aggressive or overpowered enough is supported for many trees:

- Many trees have no direct `create_wargoal`, `declare_war_on`, `add_state_claim`, or `add_ai_strategy` in focus rewards.
- Generic republic trees mostly push SOV pressure and variables rather than giving direct offensive tools.
- High-chaos helpers are stronger:
  - `soviet_collapse_apply_high_chaos_focus_payload` at `common/scripted_effects/005_soviet_collapse_effects.txt:8765` can add conquest/antagonize strategy and create/declare war against SOV in high-chaos cases.
  - `soviet_collapse_apply_high_chaos_neighbor_expansion_plan` at `common/scripted_effects/005_soviet_collapse_effects.txt:9646` is one of the few helpers that directly creates neighbor expansion pressure.
- The issue is uneven distribution: some high-chaos/factory/ancient trees have aggressive hooks; many republic and generic splinter branches remain variable/stat ladders.

## Focus-Decision Link Gaps

Existing links:

- League unit deployment is unlocked through `soviet_collapse_unlock_league_unit_deployment_decisions` at `common/scripted_effects/005_soviet_collapse_effects.txt:2166`, and decisions check `soviet_collapse_league_unit_deployment_unlocked` at `common/decisions/005_soviet_collapse_decisions.txt:4360` and `4386`.
- Regional recognition decision exists at `common/decisions/005_soviet_collapse_decisions.txt:4199`.
- Returned-names claim decisions exist at `common/decisions/005_soviet_collapse_decisions.txt:5114`, `5147`, `5179`, `5211`.
- Custom splinter consolidate-claim decisions exist for many tags, e.g. `krs_consolidate_claim` at `common/decisions/005_soviet_collapse_decisions.txt:5273`, `fth_consolidate_claim` at `5385`, `bbh_consolidate_claim` at `5488`, etc.

Gaps:

- Many focus rewards use `unlock_decision_tooltip` but do not directly `activate_decision` or set a specific per-decision unlock flag beyond broad route flags.
- Most parsed focus IDs are not directly referenced outside focus files. This is not always a bug, but it means many branch milestones cannot be consumed by decisions, missions, AI, or postwar systems.
- Expansion focuses often grant claims/wargoals without a linked postwar integration decision, resistance/coring mission, puppet/protectorate option, or AI follow-up.
- Industry focuses often add buildings without country-specific construction decisions, regional projects, repair missions, or production-line decisions.
- Unit-focused branches often create unit templates or spawn units through generic helpers, but do not consistently unlock repeatable recruitment/deployment decisions per route.

## Flag Orientation Audit

No sprite files were edited or inspected for flipping.

Script/interface-visible findings:

- I did not find focus-side `set_cosmetic_tag` or any orientation/flip setting in the audited focus files.
- Country setup search did not expose a script construct that would flip flags upside down.
- If flags are upside down in-game, likely causes are outside this focus audit surface: source DDS orientation, wrong generated sprite file, wrong flag filename/tag association, or a cosmetic tag assignment elsewhere. Do not flip sprites from this audit; parent should route a separate country-package/asset audit if needed.

## First Tranche Recommendations

Do not broad-generate replacement trees. Start with bounded, high-impact repairs.

1. Fix Ukraine layout first.
   - Move `ukr_soviet_collapse_army_of_the_republic` away from `(21, 6)`.
   - Split Ukraine into clean lanes: legal/socialist/black-banner left, military center, foreign/expansion right, bread-state/high-chaos lower-right.
   - Re-run a pathline crossing script before gameplay edits continue.

2. Replace the top 20 repeated legal-recognition rewards with branch-specific payoffs.
   - Keep `soviet_collapse_apply_focus_legal_recognition` as a baseline only.
   - Add one distinct unlock per focus group: decision, mission, core/claim route, unit template, leader/advisor, law/cosmetic change, AI strategy, or targeted postwar integration.

3. Add focus-decision links for one country family at a time.
   - Suggested first families: Ukraine, Kazakhstan, Belarus, then the custom splinter template family.
   - For each route branch, add or wire 2-3 decisions that are visibly changed by completed focuses.

4. Make custom splinter helper wrappers less empty.
   - For each repeated identity wrapper at `common/scripted_effects/005_soviet_collapse_effects.txt:13873-13945`, add narrow route-specific side effects through existing payloads: AI strategy, decision unlock flag, route-specific unit/recruitment hook, or claim/consolidation hook.
   - Do not expand all 15 tags at once. Pick 3 representative tags and establish a pattern.

5. Make chaos successor aggression consistent.
   - For non-high-chaos branches, add safer staged aggression: claims first, border-war/pressure decision second, war goal or SOV antagonize strategy at capstone.
   - For high-chaos branches, ensure focus AI weights prefer war/expansion and that claims/cores have a postwar consolidation decision.

6. Separate political/industrial/expansion payoffs.
   - Political: leader/party/cosmetic/advisor/law or decision category change.
   - Industry: state-targeted repair/build decisions, supply hubs/rail, production line decisions.
   - Expansion: claims/war goals plus postwar integration, coring, protectorate, or resistance decisions.

## Validation Performed

- Read-only parser counted focus trees, focus IDs, coordinates, prerequisites, mutual exclusions, reward signatures, and helper calls.
- Searched for direct idea adds/removals, decision activation/gating, war/core/claim hooks, and flag/cosmetic setup references.
- No gameplay files changed.

## Simplifications, Omissions, And Blockers

- This is an audit report only. It does not implement the rework.
- Pathline crossing detection is coordinate-based and approximate. It should be verified visually after layout edits.
- Continuous panel overlap was not confirmed by the parser; screenshot-based verification remains needed.
- I did not inspect or edit flag DDS files by instruction.
- I did not audit every localisation string for tone; localisation files were included in coverage only for surface alignment and key presence awareness.
