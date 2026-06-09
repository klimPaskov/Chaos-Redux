# Event 005 Soviet Collapse Focus Tree Current Audit and Kazakhstan Layout Patch

Timestamp: 2026-05-31 17:02:02 UTC

Subagent role: Chaos Redux focus tree subagent.

Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`, excluding all `CFR_*` focus tree/content
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Hard constraints respected:

- No flags, `gfx/flags`, visual assets, interface sprites, image assets, or asset files were touched.
- No CFR / Civilian Factory of Russia / construction-directorate content was edited.
- No commit was made.
- The worktree was already dirty; this pass does not claim unrelated parent/user/subagent changes.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`
- Vanilla focus precedent: `common/national_focus/estonia.txt`, `common/national_focus/finland.txt`, `common/national_focus/generic.txt`
- Event 005 focus specs and existing focus follow-up plan under `docs/specs/005_soviet_collapse_specs/` and `docs/plans/005_soviet_collapse_plans/`

## Files Changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Moved `kaz_soviet_collapse_alash_memory_restored` from `x = 35` to `x = 36`, keeping `y = 3`, to clear the last detected adjacent mutually exclusive selector pair in the current non-CFR scan. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_170202_event005_focus_tree_current_audit_kaz_layout_patch.md` | This handoff. |

Changed focus ids:

- `kaz_soviet_collapse_alash_memory_restored`

Localisation keys changed: none.

Icon ids changed: none.

No CFR ids changed.

## Route Behavior Before and After

Before:

- `kaz_soviet_collapse_alash_memory_restored` was at `(35, 3)`.
- `kaz_soviet_collapse_socialist_steppe_republic` was at `(34, 4)`.
- These mutually exclusive route selectors were diagonally adjacent, which makes the route split visually cramped and easy to read as a stacked selector rather than a clean fork.

After:

- `kaz_soviet_collapse_alash_memory_restored` is at `(36, 3)`.
- `kaz_soviet_collapse_socialist_steppe_republic` remains at `(34, 4)`.
- The mechanical layout scan reports zero adjacent mutual-exclusion pairs, zero duplicate coordinates, zero same-row prerequisites, zero upward prerequisites, and zero prerequisite pathline hits.

No rewards, prerequisites, mutual exclusions, availability, bypasses, AI weights, icons, localisation, decisions, ideas, flags, claims, cores, war goals, or formable hooks changed.

## Route Coverage Table

| Required route/content area | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine major republic identity | `soviet_collapse_ukraine_focus_tree`, `005_soviet_collapse_republics.txt:17`, 83 focuses | Partial | Broad route surface exists. Still helper-heavy: 78 focuses call helper effects and 51 have small stat/equipment-style rewards. |
| Generic breakaway republic | `soviet_collapse_breakaway_focus_tree`, `005_soviet_collapse_republics.txt:2342`, 36 focuses | Simplified | No direct focus-file decision/war/claim/core/unit/faction hooks detected; branch relies on helper bundles. |
| Internal republics | `soviet_collapse_internal_republic_focus_tree`, `005_soviet_collapse_republics.txt:3127`, 62 focuses | Simplified | Large enough by count, but all focuses use helper rewards and direct route mechanics are not visible in focus-file rewards. |
| Baltic republics | `soviet_collapse_baltic_focus_tree`, `005_soviet_collapse_republics.txt:4593`, 42 focuses | Simplified | Legal/restoration frame exists, but no direct focus-file hooks detected. Needs stronger port, forest, anti-puppet, and recognition gameplay. |
| Caucasus republics | `soviet_collapse_caucasus_focus_tree`, `005_soviet_collapse_republics.txt:5539`, 40 focuses | Partial | Some direct hooks exist, but mountain, oil, border, and Caucasus League routes still mostly resolve through helpers. |
| Central Asian republics | `soviet_collapse_central_asia_focus_tree`, `005_soviet_collapse_republics.txt:6445`, 45 focuses | Partial | Has some direct hooks and route identity, but still helper-heavy. |
| Moldova | `soviet_collapse_moldova_focus_tree`, `005_soviet_collapse_republics.txt:7566`, 48 focuses | Simplified | Dniester/Romanian/Ukrainian corridor concepts exist, but no direct focus-file hooks detected and 47 focuses call helper effects. |
| Belarus | `soviet_collapse_belarus_focus_tree`, `005_soviet_collapse_republics.txt:8709`, 53 focuses | Partial | Rail/forest/corridor identity exists. Still has 31 small reward focuses and needs more direct rail authority, League freight, and corridor decision surfaces. |
| Kazakhstan | `soviet_collapse_kazakhstan_focus_tree`, `005_soviet_collapse_republics.txt:10028`, 92 focuses | Broad but reward-heavy | Layout selector spacing patched. Resource, Alash, socialist, steppe, and League branches remain helper-heavy, with 86 helper focuses. |
| Full custom splinters | `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` in `005_soviet_collapse_custom_splinters.txt` | Present but template-like | Most have 47 focuses, but many have zero direct focus-file hooks and heavy generic helper/stat reward patterns. |
| Compact crisis splinters | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` in `005_soviet_collapse_custom_splinters.txt` | Shallow | 18-22 focuses. Some direct aggression exists in `PRA`, `DSC`, and `NRF`, but route depth is still below the high-chaos/OP actor expectation. |
| Factory successors excluding CFR | `OGB_soviet_collapse_focus_tree` at `005_soviet_collapse_factory_successors.txt:1170`; `MFR_soviet_collapse_focus_tree` at `:1778` | Mixed | MFR has 58 focuses and stronger arsenal identity. OGB remains a 23-focus shallow Volga successor. CFR was deliberately not audited for patching or edited. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` in `005_soviet_collapse_ancient_restorations.txt` | Shallow | Each has 16 focuses. They satisfy compact content but not a full political/industry/military/diplomacy/expansion route family standard. |

## Missing or Simplified Content

- `PRA_soviet_collapse_focus_tree`, `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, and `ICD_soviet_collapse_focus_tree` remain shallow crisis trees at 18-22 focuses.
- Most 47-focus custom splinters have route labels but no direct focus-file hooks for decisions, war goals, claims, cores, units, factions, cosmetic changes, or AI strategy. This is broad route design, not a safe small patch.
- `OGB_soviet_collapse_focus_tree` remains a 23-focus successor and is still shallow compared with the OP/high-impact successor expectation.
- `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, and `ALN_soviet_collapse_ancient_focus_tree` remain 16-focus compact restorations.
- Republic shared trees still depend heavily on helper effects instead of direct, readable decision/mission/map/unit payoffs.

## Icon Coverage Table

| File | Non-CFR focuses checked | Unique icon ids | Repeated icon groups | Repeated icon uses | Missing icon assignments |
| --- | ---: | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 501 | 458 | 22 | 65 | 0 |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 885 | 99 | 219 | 0 |
| `005_soviet_collapse_factory_successors.txt` excluding CFR | 81 | 81 | 0 | 0 | 0 |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 42 | 8 | 30 | 0 |

Repeated icon clusters to prioritize later:

- Republics: `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`, `GFX_moldova_soviet_collapse_ukrainian_corridor`.
- Custom splinters: `GFX_focus_FEV_diplomatic_plan`, `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_civil_rule`, `GFX_focus_MRC_foreign`, `GFX_focus_IUL_supply`, `GFX_focus_IUL_war_plan`.
- Ancient restorations: `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_guard_old_routes`, `GFX_focus_soviet_collapse_ancient_league_bargain`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_symbolic_state`.

No icon files, sprite files, interface files, or asset files were changed.

## Localisation and Reward Mismatch List

Mechanical localisation coverage:

- Non-CFR focus ids checked against `localisation/english/*005_soviet_collapse*_l_english.yml`: 1,651.
- Missing focus name keys: 0.
- Missing focus `_desc` keys: 0.

Reward/localisation mismatch risks:

- `soviet_collapse_breakaway_focus_tree`, `soviet_collapse_internal_republic_focus_tree`, `soviet_collapse_baltic_focus_tree`, and `soviet_collapse_moldova_focus_tree` promise political survival, restoration, and regional settlement but have no direct focus-file decision/war/claim/core/unit/faction hooks by static scan.
- Full custom splinter trees such as `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, and `NLC` are still likely to feel template-like because direct route mechanics are hidden behind repeated helper families.
- Ancient restoration localisation reads distinct, but route depth remains compact and repeated icon families reinforce the shared-template feel.
- MFR is stronger than most non-CFR factory-successor content, but it still has 57 helper focuses and needs more direct arsenal export/client-state mechanics before final completion.

## AI Behavior Gaps

- Every parsed focus has an `ai_will_do` block.
- Many `ai_will_do` blocks remain flat base weights or one-condition modifiers rather than route-aware behavior.
- High-chaos/custom splinter AI needs stronger pressure toward aggression, claims, war goals, late-game routes, and special mechanics when valid.
- Republic AI still needs more deliberate route selection for League alignment, foreign dependency, expansion, high-chaos escalation, and regional defense.
- OGB and ancient-restoration AI should be revisited after route depth is expanded; detailed weights on shallow trees would preserve current simplification.

## High-Priority Fixes First

1. Expand or explicitly scope down `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` compact crisis trees.
2. Add direct route payoffs to the 47-focus custom splinters: claims, war goals, targeted decisions, special units, AI strategy, and postwar hooks.
3. Expand `OGB_soviet_collapse_focus_tree` beyond its 23-focus current shape or document it as intentionally compact.
4. Expand `KZR`, `SOG`, `KHW`, and `ALN` beyond 16-focus compact restorations if they are expected to be long-lived country identities.
5. Reduce helper/list reward feel by replacing repeated helper-only payoffs with existing decisions, missions, state-building effects, units, claims, war goals, and custom tooltips.
6. Run a repeated-icon identity pass after route structure settles. Do not touch flags/assets unless explicitly scoped by the parent.

## Validation Run

- Brace-balance check on the four audited focus script files: all final depths 0; no early close lines.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt`: passed.
- Mechanical layout scan after patch: 1,698 focuses, 41 trees, missing AI 0, missing icon assignments 0, missing search filters 0, duplicate coordinates 0, prerequisite pathline hits 0, upward prerequisites 0, same-row prerequisites 0, adjacent mutual-exclusion references 0, missing focus references 0.
- Localisation coverage scan: 1,651 non-CFR focus ids checked, missing names 0, missing descriptions 0.
- `git diff --name-only -- gfx/flags`: empty.

## Skipped Validation

- No in-game launch or screenshot validation was run.
- No sprite-definition or asset-manifest patch was made because asset files and interface sprites were explicitly out of scope.
- No CFR validation beyond exclusion was performed because the parent is editing CFR locally in this tranche.

## Remaining Route Risks

- The current implementation is mechanically cleaner than earlier handoffs, but broad route quality remains incomplete for compact crisis splinters, OGB, ancient restorations, and many custom splinters.
- Helper-heavy focus rewards can still feel like idea/list spam even though direct focus-file `add_ideas` spam is not present.
- Repeated focus icons remain a visual-quality issue, especially in custom splinters and ancient restorations.
- Existing broader plan still applies: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.

Plan handoff path written:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_170202_event005_focus_tree_current_audit_kaz_layout_patch.md`
