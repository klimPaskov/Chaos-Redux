# Event005 Focus Tree Reward And Layout Patch Handoff

Date: 2026-05-31

Subagent scope: bounded audit and small patch for Event005 Soviet Collapse focus trees. Flag assets were not touched.

## Files Changed

| File | Change type |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Local x-coordinate shifts for four focuses whose vertical prerequisite lines were blocked by another focus. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Reward depth patch for one dead-army opener and two northern/arctic identity focuses. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | Reward depth patch for CFR rail-first and MFR factory-guard focuses. |

No localisation, flag, sprite, or GFX files were edited.

## Changed Focus IDs

| Focus id | Before | After |
| --- | --- | --- |
| `ukr_soviet_collapse_village_soviets_without_requisition` | Sat directly below `ukr_soviet_collapse_peasant_socialist_congress` with `ukr_soviet_collapse_rural_deputy_bloc` on the same vertical path. | Shifted left to clear the vertical prerequisite line. |
| `ukr_soviet_collapse_black_banner_takes_the_villages` | Vertical line from `ukr_soviet_collapse_black_soil_oath` ran through `ukr_soviet_collapse_dead_fields_living_columns`. | Shifted right to clear the high-chaos pathline. |
| `blr_soviet_collapse_the_forest_state_rumor` | Vertical dependency path from `blr_soviet_collapse_decentralized_detachments` ran through `blr_soviet_collapse_minsk_does_not_own_every_tree`. | Shifted right to clear the forest route pathline. |
| `blr_soviet_collapse_brest_is_not_a_gift` | Vertical dependency path from `blr_soviet_collapse_foreign_aid_through_brest` ran through `blr_soviet_collapse_railway_guard_regiments`. | Shifted right to clear the Brest pathline. |
| `CFR_rails_first` | One random core state received rail and supply. | Every core state receives rail plus infrastructure; one core state receives a supply node. |
| `MFR_factory_guard_columns` | Mostly manpower/equipment/helper plus decision tooltip. | Adds a guarded core arms factory buildout and AI arms-factory target strategy. |
| `DSC_call_the_dead_soldiers_congress` | High-chaos helper and legitimacy variable only. | Also unlocks `dsc_verify_the_roll_call`, mobilizes manpower/equipment, and fortifies a roll-call post. |
| `ARD_ice_watch_boards` | Stability and recognition only. | Adds air XP, radar/AA construction, and foreign-channel route integration. |
| `NLC_ice_road_customs` | Depot/supply helper only. | Adds trains, liaison/resilience variables, rail/infrastructure, and a supply node. |

## Route Coverage Table

| File | Implemented trees/focuses | Coverage status |
| --- | ---: | --- |
| `005_soviet_collapse_republics.txt` | 9 trees / 501 focuses | Major republic and shared republic coverage exists, with all audited focuses carrying icons, filters, rewards, and AI. Ukraine/Belarus/Kazakhstan remain too broad for final route-quality claims without parent review against the spec. |
| `005_soviet_collapse_custom_splinters.txt` | 25 trees / 1005 focuses | Most chaos countries have full 47-focus trees; crisis splinters have 18-22. DSC/NRF have stronger endgame helpers; many 47-focus splinters still need manual reward/icon uniqueness passes. |
| `005_soviet_collapse_factory_successors.txt` | 3 trees / 128 focuses | CFR and MFR have real branches and were strengthened here. OGB remains compact at 23 focuses and needs a parent decision on whether compact depth is acceptable. |
| `005_soviet_collapse_ancient_restorations.txt` | 4 trees / 64 focuses | Four 16-focus ancient restoration trees exist, but they remain shallow compared with the spec's identity-depth expectation. No patch in this pass. |

## Icon Coverage Table

| Surface | Result |
| --- | --- |
| Missing focus icons in audited files | None found by parser. |
| Missing `search_filters` / `ai_will_do` / `completion_reward` | None found by parser. |
| Repeated icons | Still present in several large trees. Highest-priority examples: `FEV_soviet_collapse_focus_tree` 13 repeated icon ids, `SZA_soviet_collapse_focus_tree` 12, `UWD_soviet_collapse_focus_tree` 15, `IUL_soviet_collapse_focus_tree` 15, `CFR_soviet_collapse_focus_tree` 11. These need an asset/icon pass, not a narrow focus-reward patch. |

## Localisation And Reward Mismatch Notes

No player-facing IDs were added or renamed, so localisation files were not changed. The patched rewards now better match their existing focus names:

| Focus id | Match improvement |
| --- | --- |
| `CFR_rails_first` | Reward now visibly prioritizes rails across the core network. |
| `MFR_factory_guard_columns` | Factory guard columns now secure an actual arms-factory buildout. |
| `DSC_call_the_dead_soldiers_congress` | The dead congress now immediately unlocks roll-call work and raises a fortified roll-call base. |
| `ARD_ice_watch_boards` | Ice watch now has radar/AA and air coordination, not only abstract stability. |
| `NLC_ice_road_customs` | Ice road customs now create rail/logistics infrastructure and trains. |

## Idea Spam / Duplicate Idea Audit

Direct focus-block audit found no current focuses in the four files that add multiple ideas or repeat the same `add_ideas` line inside one `completion_reward`. Remaining perceived idea spam is mostly helper-driven identity application and repeated route tooltip language. Parent follow-up should focus on reducing repeated helper-visible tooltips and replacing generic identity-helper-only rewards with concrete decision/building/unit/map effects.

## AI Behavior Gaps

All focuses in the audited files have `ai_will_do`, but many remain flat base weights with only one or two state checks. Parent should prioritize route-aware AI for:

| Tree/family | Gap |
| --- | --- |
| Generic 47-focus custom splinters | Many route choices use the same base weights and only shallow war/stability checks. |
| Ancient restorations | Compact trees need route-specific AI for symbolic/expansionist settlement choices. |
| CFR/MFR/OGB | Factory-state AI should strongly prefer routes based on construction capacity, war state, factory count, and Soviet depot pressure. |
| Ukraine/Belarus high-chaos routes | AI should avoid high-chaos escalation unless chaos tier, war pressure, and old-movement pressure justify it. |

## High-Priority Remaining Gaps

1. Full route rework is still too broad for this subagent. The spec requires meaningful political, industrial, expansion, diplomacy, military, and late-game branches. Existing broad plan remains: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.
2. Repeated icons violate the spec's unique-icon requirement. Do not solve this by touching flags; route focus icons need a dedicated icon asset pass.
3. Many 47-focus custom splinters still have identity-helper-only or small one-off reward focuses. Patch candidates for the parent: `FEV_siberian_factory_letters`, `SZA_ural_factory_letters`, `UWD_industrial_neutrality_statute`, `ARD_murmansk_port_records`, `NLC_polar_neutrality_statute`, and the old-movement mobile/cavalry support nodes.
4. Ancient restoration trees (`KZR`, `SOG`, `KHW`, `ALN`) are only 16 focuses each. They need route depth and AI behavior before completion claims.
5. `OGB_soviet_collapse_focus_tree` has only 23 focuses. Parent should either deepen it as a real overpowered successor or explicitly classify it as compact.

## Validation Run

Passed:

```text
python3 brace-depth check:
common/national_focus/005_soviet_collapse_republics.txt: brace_depth=0 bad=[]
common/national_focus/005_soviet_collapse_custom_splinters.txt: brace_depth=0 bad=[]
common/national_focus/005_soviet_collapse_factory_successors.txt: brace_depth=0 bad=[]

git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt
no output

focus parser:
no missing/nonreciprocal mutual exclusions found
no remaining vertical blockers found within the audited trees
no missing icons, search filters, ai_will_do, or completion_reward found
```

Skipped:

- No live HOI4 load test; subagent environment only.
- No flag validation by request. No files under `gfx/flags` were read or edited.
- No localisation encoding edit because no localisation file was touched.

## Remaining Risk

The repository worktree was already dirty, including these same Event005 files. This handoff lists only the bounded focus changes made in this pass; parent should review the combined diff before committing.
