# Event005 Soviet Collapse Focus Tree Audit Handoff

Date/time: 2026-06-04 12:13:29 UTC

Role: bounded focus-tree audit subagent. Scope was audit plus small safe patches only.

## Files inspected

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt` for helper payload/idea checks
- `common/ideas/005_soviet_collapse_ideas.txt` and Event005 constants/decision files by search context

Required references consulted before file inspection:

- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla precedent: `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`.
- Repo skills: `hoi4-focus-trees`, `chaos-redux-events`.

## Commands and checks run

- `rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|National focus|Focus'`
- `sed -n ...` on the required wiki pages and vanilla documentation listed above.
- `wc -l` on the four audited focus files.
- Brace-aware Python audit over the four focus files for focus counts, duplicate focus ids, direct `add_ideas`, multiple direct `add_ideas`, repeated helper calls, same-row prerequisite risks, close mutually exclusive pairs, and brace deltas.
- `rg -n "add_ideas|swap_ideas"` on all four audited focus files. It returned no matches.
- Brace-aware Python audit over `common/scripted_effects/005_soviet_collapse_effects.txt` for helper blocks with `add_ideas`, `swap_ideas`, and `remove_ideas`.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt` after the patch. It returned no matches.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt` after the patch. It passed.
- Brace-balance check after the patch: all four audited focus files had brace delta `0`.

## Summary counts

- Parsed focus blocks: 1,698 total.
- Parsed focus trees: 41.
- By file:
  - `005_soviet_collapse_republics.txt`: 501 focuses
  - `005_soviet_collapse_custom_splinters.txt`: 1,005 focuses
  - `005_soviet_collapse_factory_successors.txt`: 128 focuses
  - `005_soviet_collapse_ancient_restorations.txt`: 64 focuses
- Duplicate focus IDs across the four audited files: none detected.
- Direct `add_ideas` in audited focus files: none detected.
- Direct multiple-idea rewards in audited focus files: none detected.
- Scripted-effect blocks with `add_ideas`: 36, mostly startup/setup or authority update effects, not direct focus rewards.

## Files changed

Patched one narrow layout issue in:

- `common/national_focus/005_soviet_collapse_republics.txt`

Changed only the `y` positions of these Belarus focuses:

- `blr_soviet_collapse_minsk_supplies_the_front`: `y = 12` to `y = 13`
- `blr_soviet_collapse_the_league_depot_at_minsk`: `y = 12` to `y = 14`
- `blr_soviet_collapse_the_forest_state_rumor`: `y = 14` to `y = 15`

Reason: these were same-row prerequisite chains. The local National focus modding wiki says prerequisites should be placed above dependent focuses or path sprites can generate incorrectly.

No gfx, flags, or interface flag files were touched.

## Findings

### 1. No direct duplicate idea add found in the audited focus files

Evidence:

- `rg -n "add_ideas|swap_ideas" common/national_focus/005_soviet_collapse_*.txt` returned no matches for the four audited files.
- Direct duplicate `add_ideas` in one focus reward: none detected.
- Direct multiple `add_ideas` in one focus reward: none detected.

This does not clear the "idea spam" complaint entirely. The issue is now mostly indirect: many focuses repeatedly call generic identity/progression helpers that advance consolidated variables and route payloads. The parent should treat this as reward-spam/identity-spam, not direct duplicate `add_ideas` spam.

Concrete repeated helper evidence:

- `soviet_collapse_apply_focus_depot_and_supply_control`: 138 focus calls.
- `soviet_collapse_apply_focus_military_consolidation`: 132 focus calls.
- `soviet_collapse_apply_focus_legal_recognition`: 108 focus calls.
- `soviet_collapse_apply_focus_republican_compact_plan`: 80 focus calls.
- `soviet_collapse_apply_focus_high_chaos_identity`: 60 focus calls.

Representative direct route example:

- `ukr_soviet_collapse_socialist_republic_without_moscow`
- `ukr_soviet_collapse_peasant_socialist_congress`
- `ukr_soviet_collapse_workers_congress_in_kharkiv`
- `ukr_soviet_collapse_village_soviets_without_requisition`
- `ukr_soviet_collapse_purge_moscow_loyalists`
- `ukr_soviet_collapse_re_register_the_party`

These repeatedly use `soviet_collapse_apply_focus_socialist_sovereignty`, usually with only a small stability, command power, or political power adjunct. The helper itself advances depth, stability, recognition, institution strength, recovery, and payloads. This is technically centralized, but it makes route rewards feel flat when used as the main payoff several times in a row.

### 2. Reward ladders are often flat helper ladders

`FTH_soviet_collapse_focus_tree` is the clearest example. Early/mid focuses mostly set a country flag plus a generic tooltip/helper:

- `FTH_first_guard`: command power plus `soviet_collapse_apply_custom_splinter_first_guard_identity`
- `FTH_stores`: `soviet_collapse_apply_custom_splinter_stores_identity`
- `FTH_legitimacy`: `soviet_collapse_apply_custom_splinter_legitimacy_identity`
- `FTH_rival`: `soviet_collapse_apply_custom_splinter_rival_identity`
- `FTH_doctrine`: `soviet_collapse_apply_custom_splinter_doctrine_identity`
- `FTH_economy`: `soviet_collapse_apply_custom_splinter_economy_identity`
- `FTH_league`: `soviet_collapse_apply_custom_splinter_league_identity`
- `FTH_foreign`: `soviet_collapse_apply_custom_splinter_foreign_identity`

The same generic skeleton appears across many 47-focus custom splinters. Summary evidence:

- `FTH_soviet_collapse_focus_tree`: 47 focuses, 0 decision unlocks detected, 0 claims/cores/wargoals detected.
- `BBH_soviet_collapse_focus_tree`: 47 focuses, 0 decision unlocks detected, 0 claims/cores/wargoals detected.
- `KRS_soviet_collapse_focus_tree`: 47 focuses, 0 decision unlocks detected, 0 claims/cores/wargoals detected.
- `UDC_soviet_collapse_focus_tree`: 47 focuses, 0 decision unlocks detected, 0 claims/cores/wargoals detected.
- `SDZ_soviet_collapse_focus_tree`: 47 focuses, 0 decision unlocks detected, 0 claims/cores/wargoals detected.
- `GAC_soviet_collapse_focus_tree`: 47 focuses, 0 decision unlocks detected, 0 claims/cores/wargoals detected.

These trees have breadth, but many branches do not yet have the kind of political, industrial, expansion, military, decision, or diplomacy payoff required by the focus-tree skill.

### 3. Remaining pathline/layout risks after the small patch

After patching the Belarus same-row chain, the parser still finds five prerequisite placement risks:

- `soviet_collapse_local_courts_and_militia_rolls` at `y = 3` depends on `soviet_collapse_capital_committee_records` at `y = 5`.
- `soviet_collapse_foreign_cadre_school` at `y = 3` depends on `soviet_collapse_foreign_liaison_government` at `y = 4`.
- `soviet_collapse_sponsor_aid_audit` at `y = 3` depends on `soviet_collapse_foreign_liaison_government` at `y = 4`.
- `CFR_a_civilian_factory_in_every_capital` at `y = 12` depends on `CFR_the_debt_map` at `y = 12`.
- `CFR_the_city_without_citizens` at `y = 6` depends on `CFR_the_concrete_committee` at `y = 6`.

One tight mutually exclusive pair remains:

- `ukr_soviet_collapse_purge_moscow_loyalists` at `(19, 11)` vs `ukr_soviet_collapse_re_register_the_party` at `(20, 11)`.

This is a same-row adjacent mutex pair with modest rewards. It is both a visual overlap risk and a gameplay-depth risk unless the parent expands the choice consequences.

### 4. Some mutually exclusive choices are mechanically thin

The Ukraine socialist mutex:

- `ukr_soviet_collapse_purge_moscow_loyalists`
- `ukr_soviet_collapse_re_register_the_party`

Both are route locks, but the immediate rewards are only a flag, a small command power or stability reward, and the same socialist helper. There is no immediate leader/advisor/law/decision split in these focus rewards. Parent should turn this into a real split: purge path should affect security apparatus, officers, arrests, or anti-Moscow decisions; re-register path should affect party legality, cadres, diplomacy with socialist breakaways, and AI strategy.

### 5. Chaos-country concepts remain underpowered relative to their premise

Examples:

- `TSC_soviet_collapse_focus_tree`: 18 focuses, only 1 decision unlock detected.
- `RMC_soviet_collapse_focus_tree`: 18 focuses, only 1 decision unlock detected.
- `ICD_soviet_collapse_focus_tree`: 18 focuses, only 1 decision unlock detected.
- `DSC_soviet_collapse_focus_tree`: 18 focuses, stronger than the others but still very compact for a dead-soldier concept.
- `NRF_soviet_collapse_focus_tree`: 18 focuses, better support/decision count but still compact.

The concepts imply special mechanics, unique recruitment, expansion consequences, containment pressure, or world reaction. Most of the current surface is still focus rewards, variables, small buildings/stockpiles, and generic high-chaos identity helpers.

Ancient restoration trees also remain shallow for their concepts:

- `KZR_soviet_collapse_ancient_focus_tree`
- `SOG_soviet_collapse_ancient_focus_tree`
- `KHW_soviet_collapse_ancient_focus_tree`
- `ALN_soviet_collapse_ancient_focus_tree`

They are each 16 focuses and strongly mirror one another structurally. They do have claims and a few decision unlocks, but they need sharper political identity, diplomacy, postwar settlement, and country-specific economic/military branches.

## Prioritized parent implementation plan

1. Finish layout cleanup before adding more content.
   - Fix the five remaining prerequisite-above risks listed above.
   - Spread or vertically stagger the `ukr_soviet_collapse_purge_moscow_loyalists` / `ukr_soviet_collapse_re_register_the_party` mutex pair.
   - Re-run the brace-aware parser and screenshot/check the affected trees in-game.

2. Convert repeated helper ladders into route payoffs.
   - Keep the shared helpers, but stop using them as the entire reward identity.
   - For every route fork, add at least one concrete surface: decision unlock, law/advisor/leader change, faction/AI strategy, state construction package, claims/cores/wargoal, unit template, or event hook.

3. Rework one custom splinter archetype at a time, then propagate the pattern manually.
   - Start with `FTH` because it cleanly shows the problem: many 47-focus branches but no decision unlocks or expansion consequences.
   - Add decisions and route-specific consequences first, then adapt BBH/KRS/UDC/SDZ/GAC only where their concept supports it.

4. Deepen chaos-country special mechanics.
   - TSC/RMC/DSC/NRF/ICD should each get at least one unique mechanic or decision family, not just a compact focus package.
   - Suggested surfaces: special recruitment, containment/recognition pressure, unique expansion rules, enemy reactions, and crisis escalation missions.

5. Upgrade the ancient restorations from mirrored compact trees to distinct country packages.
   - Keep shared structure where useful, but add tag-specific branch payoffs: KZR toll/transit authority, SOG city-road diplomacy, KHW irrigation/oasis legitimacy, ALN pass/mountain defense.
   - Add postwar handling for claims: integration, puppet/protectorate options, resistance risk, and League/neighbor reactions.

6. Run audit gates after each tranche.
   - Duplicate focus IDs.
   - Direct `add_ideas`/`swap_ideas`.
   - Helper call density by route.
   - Prerequisite-above and close-mutex layout checks.
   - Missing `ai_will_do`, missing reward, missing search filters.
   - Decision/localisation/icon docs alignment.

## Validation result

Passed after the small patch:

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt` returned no matches.
- Brace delta was `0` for all four audited focus files.
- Duplicate focus IDs: none detected.

Known remaining risks are listed above. The audit was intentionally bounded and did not attempt a full tree rewrite.
