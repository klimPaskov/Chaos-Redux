# Soviet Collapse Focus Current-State Audit

Scope: all current focus trees in:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No `gfx/flags`, `interface/flags`, flag sprite, or flag asset files were touched.

## References Consulted

- Repo instructions: `AGENTS.md`
- Skill: `.agents/skills/hoi4-focus-trees/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`, `common/decisions/_documentation.md`, `common/ai_strategy/_documentation.md`
- Vanilla focus precedent: `common/national_focus/generic.txt`, `common/national_focus/soviet.txt`

## Files Changed

- Added this handoff report only.

No focus, helper, localisation, decision, AI, interface, or asset files were patched. The worktree already contains broad parent/user changes in the scoped Soviet Collapse files, so I did not make isolated focus edits unless an issue was both unambiguous and safe. No such tiny focus edit met that bar in this pass.

## Exact Focus IDs Reviewed/Patch Status

Mechanical parser coverage:

- 41 focus trees parsed.
- 1,698 focus blocks parsed.
- 0 duplicate focus IDs.
- 0 missing `prerequisite = { focus = ... }` references.
- 0 missing `relative_position_id` references.
- 0 focus blocks missing `ai_will_do`.
- 0 focus blocks missing `completion_reward`.
- 176 mutual-exclusion edges parsed.

Focus files were reviewed tree-wide through parser coverage. Manual spot checks focused on the complaint hot spots and highest-risk findings:

- Ukraine: `ukr_soviet_collapse_purge_moscow_loyalists`, `ukr_soviet_collapse_re_register_the_party`, `ukr_soviet_collapse_the_ukrainian_commune_debate`, `ukr_soviet_collapse_the_double_republic`, `ukr_soviet_collapse_the_commune_war`, `ukr_soviet_collapse_direct_national_claims`, `ukr_soviet_collapse_ports_need_soldiers`, `ukr_soviet_collapse_great_steppe_and_sea_plan`, `ukr_soviet_collapse_the_western_question_cannot_wait`, `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map`.
- Belarus: `blr_soviet_collapse_railway_neutrality`, `blr_soviet_collapse_rail_war_state`, `blr_soviet_collapse_council_bargains_with_forests`, `blr_soviet_collapse_a_forest_that_can_govern`, `blr_soviet_collapse_foreign_aid_through_brest`, `blr_soviet_collapse_brest_is_not_a_gift`, `blr_soviet_collapse_the_league_depot_at_minsk`, `blr_soviet_collapse_minsk_supplies_the_front`, `blr_soviet_collapse_decentralized_detachments`, `blr_soviet_collapse_regular_forest_brigades`.
- Raw reward/pathline examples: `DSC_claim_the_soldiers_road`, `ALN_expansionist_mountain_claims`, `KZR_expansionist_steppe_levy`, `SOG_expansionist_merchant_claims`, `KHW_expansionist_water_claims`, `PRA_rails_over_capitals`, `central_asia_soviet_collapse_khwarazm_restoration_debate`.
- No focus IDs were patched.

## Tree Counts

Republic/shared republic trees:

| Tree | Focuses | Helper/mechanic reward focuses | Claim/war focuses | Mutex edges |
| --- | ---: | ---: | ---: | ---: |
| `soviet_collapse_ukraine_focus_tree` | 83 | 79 | 0 | 6 |
| `soviet_collapse_breakaway_focus_tree` | 36 | 33 | 0 | 6 |
| `soviet_collapse_internal_republic_focus_tree` | 62 | 62 | 0 | 6 |
| `soviet_collapse_baltic_focus_tree` | 42 | 41 | 0 | 12 |
| `soviet_collapse_caucasus_focus_tree` | 40 | 40 | 0 | 0 |
| `soviet_collapse_central_asia_focus_tree` | 45 | 44 | 1 | 16 |
| `soviet_collapse_moldova_focus_tree` | 48 | 48 | 0 | 12 |
| `soviet_collapse_belarus_focus_tree` | 53 | 52 | 0 | 4 |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 86 | 0 | 14 |

Other scoped trees:

- `MFR_soviet_collapse_focus_tree`: 58 focuses, 57 helper/mechanic rewards, 2 claim/war focuses, 0 mutex edges.
- `CFR_soviet_collapse_focus_tree`: 47 focuses, 47 helper/mechanic rewards, 0 claim/war focuses, 24 mutex edges.
- Nineteen 47-focus custom splinter templates: generally 34-46 helper/mechanic rewards each, usually 2 mutex edges each.
- Compact high-chaos/special trees (`PRA`, `DSC`, `RMC`, `TSC`, `NRF`, `ICD`, `OGB`): 18-23 focuses each, 1-2 claim/war focuses each, usually 4 mutex edges.
- Ancient restoration trees (`KZR`, `SOG`, `KHW`, `ALN`): 16 focuses each, 12-13 helper/mechanic rewards each, 3 claim/war focuses each, 2 mutex edges each.

## Reward-Spam Findings

Direct focus-level idea spam is currently not present in the four focus files:

- 0 direct `add_ideas`.
- 0 direct `swap_ideas`.
- 0 direct `add_timed_idea`.
- 0 direct `remove_ideas`.

The player complaint is still partly valid, but the current source is helper-side and repetition-style reward design rather than direct focus-file idea spam:

- `common/scripted_effects/005_soviet_collapse_effects.txt` still contains many idea lifecycle operations, including republic cleanup/removal blocks around lines 5557-5604, route payoff idea grants such as `pra_*`, `cfr_*`, `mfr_*`, `dsc_*`, and many custom-splinter identity ideas around lines 17183-17772.
- Many focuses call the same broad reward families repeatedly, especially `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_socialist_sovereignty`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_rail_authority_reward`, and `soviet_collapse_apply_focus_mobile_columns_reward`.
- This makes several branches feel generic even when the focus file no longer literally grants new ideas every focus.

Largest raw/direct reward blocks still worth helper consolidation:

- `DSC_claim_the_soldiers_road`: 35 reward lines.
- `ALN_expansionist_mountain_claims`: 34 reward lines.
- `KZR_expansionist_steppe_levy`: 32 reward lines.
- `SOG_expansionist_merchant_claims`: 32 reward lines.
- `KHW_expansionist_water_claims`: 32 reward lines.
- `OGB_the_old_name_survives_modern_war`: 27 reward lines.
- `KHW_khwarazmian_water_charter`: 27 reward lines.
- `PRA_rails_over_capitals`: 25 reward lines.

## Pathline And Mutex Findings

Syntax/reference state is clean: no duplicate IDs, missing prerequisite targets, missing relative-position targets, one-way mutexes, or missing AI weights were found.

However, geometric pathline risk remains. The parser found 1,677 prerequisite corridors passing through or near another focus coordinate, and 22 of those involve a focus mutually exclusive with one endpoint. This is a broad geometric detector, so it over-reports long diagonals; the following are the high-priority current examples:

- `soviet_collapse_ukraine_focus_tree`: `ukr_soviet_collapse_re_register_the_party` -> `ukr_soviet_collapse_the_ukrainian_commune_debate` passes through the mutually exclusive `ukr_soviet_collapse_purge_moscow_loyalists`.
- `soviet_collapse_internal_republic_focus_tree`: `internal_soviet_collapse_write_the_autonomy_statute` -> `internal_soviet_collapse_legal_autonomy_congress` passes through mutually exclusive `internal_soviet_collapse_security_council`.
- `soviet_collapse_central_asia_focus_tree`: `central_asia_soviet_collapse_loose_southern_pact` -> `central_asia_soviet_collapse_the_south_survives_together` passes through mutually exclusive `central_asia_soviet_collapse_federation_state`.
- `soviet_collapse_central_asia_focus_tree`: `central_asia_soviet_collapse_negotiate_with_the_mountain_bands` -> `central_asia_soviet_collapse_the_basmachi_amnesty_ledger` passes through mutually exclusive `central_asia_soviet_collapse_clear_the_mountain_bands`.
- `soviet_collapse_moldova_focus_tree`: `moldova_soviet_collapse_union_with_romania_question` -> `moldova_soviet_collapse_conditional_union` passes through mutually exclusive `moldova_soviet_collapse_alliance_not_union`.
- `soviet_collapse_kazakhstan_focus_tree`: several `kaz_soviet_collapse_alash_memory_restored` edges cross through `kaz_soviet_collapse_socialist_steppe_republic` or `kaz_soviet_collapse_resource_defense_directorate`.

Potentially pointless or over-broad mutex groups requiring design review:

- `soviet_collapse_baltic_focus_tree`: `baltic_soviet_collapse_legal_continuity_government`, `baltic_soviet_collapse_baltic_league_first`, and `baltic_soviet_collapse_foreign_protection_council` are a three-way route identity lock. This may be valid, but each needs distinct route consequences to justify excluding the others.
- `soviet_collapse_central_asia_focus_tree`: `central_asia_soviet_collapse_local_republic_council`, `central_asia_soviet_collapse_foreign_border_patronage`, and `central_asia_soviet_collapse_turkestan_federation_road` look like a real route fork, while `central_asia_soviet_collapse_negotiate_with_the_mountain_bands` versus `central_asia_soviet_collapse_clear_the_mountain_bands` is clearer and should remain a mutex.
- `soviet_collapse_moldova_focus_tree`: `moldova_soviet_collapse_alliance_not_union`, `moldova_soviet_collapse_conditional_union`, and `moldova_soviet_collapse_reject_the_union_question` are probably valid identity locks but still need layout cleanup.
- `CFR_soviet_collapse_focus_tree`: governance and strategy locks are numerous. Some are probably real governing-authority choices; `CFR_factories_first` versus `CFR_contracts_first` should be checked for whether both could coexist as support branches.
- `soviet_collapse_belarus_focus_tree`: `blr_soviet_collapse_decentralized_detachments` versus `blr_soviet_collapse_regular_forest_brigades` is a valid military-structure choice, not a pointless mutex.

## Ukraine And Belarus Status

Ukraine is much better than an empty or tiny tree: it has 83 focuses and recognizable political, military, industry, foreign, League, Black Sea, bread-state, and high-chaos content. It still looks bad because the right side is visually tangled and many payoffs reuse shared helper families rather than route-specific visible consequences. It should not be patched with one-off x/y nudges; it needs a deliberate layout pass around the statehood, socialist, foreign, Black Sea, and bread/high-chaos lanes.

Belarus has 53 focuses and a clearer identity than earlier reports: rail, forest, corridor, League logistics, and legal/foreign surfaces are present, with extensive localisation in `005_soviet_collapse_blr_focus_l_english.yml`. It still needs a rail/forest/corridor layout pass because convergence focuses pull from far-apart lanes. It also needs more decision surface depth; focus-level Belarus decision hooks are still thinner than Ukraine's League/border decision surface.

## Branch-Depth Gaps

- Direct focus rewards now connect to mechanics in most trees, but too many trees depend on common helper families, making political/industrial/military routes feel similar in play.
- Custom 47-focus splinters are structurally broad, but many share the same branch shape: birth, legitimacy, economy, doctrine, supply, enemy front, diplomacy, radical/settlement/endgame. The stronger ones need tag-specific route mechanics and expansion targets, not only stronger constants.
- Ancient restorations are compact and readable but shallow. Each has clear symbolic versus expansionist paths, but three claim/war payoff focuses per 16-focus tree concentrate most map gameplay into a small area.
- Chaos countries are more aggressive than a normal minor because many war/claim focuses and AI strategy overlays exist, but tag-specific aggression is still uneven. The AI strategy file has generic custom-splinter and route overlays, plus Ukraine/Belarus/Kazakhstan constants, but not every chaos country has a bespoke target plan.
- Decision integration is strongest for Ukraine and PRA-style rail mechanics. Belarus, Moldova, generic breakaway/internal republic, and many custom splinters still need more route-specific decisions/missions.

## Prioritized Recommendations

1. Reflow Ukraine as a single layout tranche. Start with `ukr_soviet_collapse_re_register_the_party`, `ukr_soviet_collapse_purge_moscow_loyalists`, and `ukr_soviet_collapse_the_ukrainian_commune_debate`, then continue through the Black Sea/bread/high-chaos lanes.
2. Reflow Belarus rail/forest convergence. Keep `blr_soviet_collapse_railway_neutrality` and `blr_soviet_collapse_rail_war_state` adjacent, then isolate League freight and forest convergence lines.
3. Review helper-side idea lifecycles in `common/scripted_effects/005_soviet_collapse_effects.txt`. Do not add focus-file hacks; decide which helper ideas are intended lasting institutions and which should become variables, dynamic modifiers, decision unlocks, or staged swaps.
4. Replace repeated generic helper-only payoffs with route-specific helpers for Ukraine, Belarus, Kazakhstan, MFR/CFR, and the highest-impact custom splinter trees.
5. Add Belarus, Moldova, and Kazakhstan decision/missions comparable to Ukraine's League and external-border decision surface.
6. Convert ancient restoration raw claim/war blocks into documented scripted effects so future balance can tune claims, AI aggression, and postwar consequences in one place.
7. Add tag-specific AI strategy overlays for the chaos countries that are supposed to be especially overpowered and aggressive.

## Validation

Validation run in this pass:

- `git diff --check -- docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_125957_soviet_collapse_focus_current_state_audit.md`: clean.
- `rg -n "<=|>="` on the four scoped focus files: no unsupported operators found.
- Mechanical parser over all four scoped focus files.
- Structural checks: duplicate focus IDs, missing prerequisites, missing `relative_position_id`, missing `ai_will_do`, missing completion rewards, one-way mutexes.
- Reward scan for direct `add_ideas`, `swap_ideas`, `add_timed_idea`, `remove_ideas`, raw claim/war effects, and large completion rewards.
- Related helper scan for idea operations and repeated shared focus helpers.
- Focus parser result: `focus_trees=41 focus_blocks=1698 duplicate_ids=0 missing_prereqs=0 missing_relative_position=0 ai_missing=0 completion_reward_missing=0 brace_errors=0`.
- `git status --short` reviewed before edits; worktree has many existing parent/user modifications.

Follow-up validation still needed after any future focus edit:

- `git diff --check -- <changed files>`
- brace/focus parser on edited files
- visual or screenshot review for Ukraine/Belarus layout after any real coordinate tranche

## Skills Used

- `hoi4-focus-trees`

No skills were created or updated.
