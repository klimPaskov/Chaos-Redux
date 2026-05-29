# Soviet Collapse Focus Tree Bounded Audit And Patch Handoff

Date: 2026-05-29

Subagent scope: focus-tree audit and bounded small patches for the Soviet Collapse successor focus trees. This is not a completion claim for the whole Soviet Collapse focus-tree rework.

## Required References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki snapshot pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, AI focuses.
- Vanilla documentation read from `~/projects/Hearts of Iron IV/documentation/`: effects, triggers, modifiers, localisation objects, localisation formatters, script concepts, dynamic variables.
- Vanilla focus precedent inspected: `~/projects/Hearts of Iron IV/common/national_focus/generic.txt`.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- This handoff.

No localisation, icon `.gfx`, scripted effect, scripted trigger, decision, or idea files were changed in this pass.

## Changed Focus IDs

- Ukraine filters: `ukr_soviet_collapse_black_sea_defense_staff`, `ukr_soviet_collapse_ports_need_soldiers`.
- Belarus filters: `blr_soviet_collapse_railway_guard_regiments`, `blr_soviet_collapse_minsk_supplies_the_front`.
- Railway/custom filters: `PRA_armored_train_directorate`, `PRA_rails_over_capitals`.
- Red Mourning Commune filters: `RMC_claim_the_burial_roads`, `RMC_procession_columns`.
- Dead Soldiers Congress filters/reward: `DSC_stalingrad_roll_call`, `DSC_claim_the_soldiers_road`, `DSC_armies_that_do_not_demobilize`.
- Naval/revenant filters/reward: `NRF_claim_the_white_sea_lane`, `NRF_fleet_that_does_not_dock`.
- Iron Commissariat filters: `ICD_memorial_battalions`, `ICD_claim_the_unburied_front`, `ICD_grave_columns_march`.
- Factory successors filters: `OGB_notables_and_workshops`, `MFR_workers_own_the_arsenal`, `MFR_eternal_arsenal_marches`.

## Route Coverage Table

| Required route or tree | Implemented branch audited | Status | Notes |
| --- | --- | --- | --- |
| Ukraine | `soviet_collapse_ukraine_focus_tree`, 83 focuses | Partial | Broad tree exists with politics, League, foreign, military, industry, expansion, and high-chaos agriculture. Layout still needs a dedicated pass; only two filter mismatches were safe to patch. |
| Belarus | `soviet_collapse_belarus_focus_tree`, 53 focuses | Partial | Rail, forest, corridor, political, League, and high-chaos lanes exist. Tree still has close/crowded geometry in several lanes; only two filter mismatches were safe to patch. |
| League/custom splinters | `FTH`, `FEV`, `NLC`, plus compact custom trees | Partial | 47-focus custom splinters have more branch depth than the compact 18-focus high-chaos trees, but many support nodes still resolve through helper flags. Needs parent-level design for route depth. |
| Dead Soldiers Congress | `DSC_soviet_collapse_focus_tree`, 18 focuses | Improved locally | Aggressive line already had claims, war goals, AI conquest, and assault-column hooks. Added manpower/equipment/army XP/mobilization to `DSC_armies_that_do_not_demobilize`. |
| Railway successor | `PRA_soviet_collapse_focus_tree`, 22 focuses | Improved locally | Railway/supply mechanics already exist through rail authority, depot control, repair, junction, and moving-state decisions. Patched filters for armored train and rails-over-capitals mechanics. |
| Civilian factory successor | `CFR_soviet_collapse_focus_tree`, 47 focuses | Covered but still risky | Civilian construction identity is present through mandates, public works, contract networks, offsite civilian factories, and reconstruction decisions. No safe new gameplay patch needed in this pass. |
| Military factory successor | `MFR_soviet_collapse_focus_tree`, 58 focuses | Improved locally | Arsenal route exists with production, market, League, and conquest endpoints. Patched filters for worker-arsenal and endgame industry/annexation identity. |
| Naval successor | `NRF_soviet_collapse_focus_tree`, 18 focuses | Improved locally | Naval route has port muster, revenant fleet, convoy, dockyard, and marine hooks. Added dockyard/convoy/navy XP production to `NRF_fleet_that_does_not_dock` and fixed annexation filters. |
| OGB | `OGB_soviet_collapse_focus_tree`, 23 focuses | Improved locally | Volga restoration route exists. Patched `OGB_notables_and_workshops` filters to match its manpower/army reward. |
| TSC/RMC/ICD | `TSC`, `RMC`, `ICD` compact high-chaos trees | Partial | Compact high-chaos routes are coherent but shallow. Patched RMC/ICD annexation and industry filter mismatches. TSC still has several filter mismatches queued for a later pass. |

## Focus-By-Focus Audit Notes

The following high-risk trees were parsed focus-by-focus for id, icon assignment, AI block, reward presence, coordinate collision, and reciprocal mutual exclusion. A `*` marks a focus changed in this pass.

### Ukraine

Audited 83 focuses. No duplicate coordinates, missing icons, missing AI blocks, empty rewards, duplicate focus ids, or non-reciprocal mutual exclusions detected. Patched `*ukr_soviet_collapse_black_sea_defense_staff` and `*ukr_soviet_collapse_ports_need_soldiers` filter coverage. Remaining risk: the tree is still visually broad and uneven; fixing that safely requires a layout redesign pass, not a narrow coordinate tweak.

### Belarus

Audited 53 focuses. No duplicate coordinates, missing icons, missing AI blocks, empty rewards, duplicate focus ids, or non-reciprocal mutual exclusions detected. Patched `*blr_soviet_collapse_railway_guard_regiments` and `*blr_soviet_collapse_minsk_supplies_the_front` filter coverage. Remaining risk: Minsk/rail/forest lanes remain crowded and some branch gates are visually hard to read.

### League And Custom Splinters

Audited `FTH` 47 focuses, `FEV` 47 focuses, and `NLC` 47 focuses. No structural validation failures found. These trees are no longer pure one-line reward ladders, but still include many helper/flag-based support nodes. No safe local route redesign was attempted.

### Compact High-Chaos Trees

Audited `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD`.

- `PRA`: 22 focuses; patched `*PRA_armored_train_directorate` and `*PRA_rails_over_capitals`.
- `TSC`: 18 focuses; no patch in this pass, but filter mismatches remain on observatory/perimeter/starfall military-air content.
- `RMC`: 18 focuses; patched `*RMC_claim_the_burial_roads` and `*RMC_procession_columns`.
- `DSC`: 18 focuses; patched `*DSC_stalingrad_roll_call`, `*DSC_claim_the_soldiers_road`, and `*DSC_armies_that_do_not_demobilize`.
- `NRF`: 18 focuses; patched `*NRF_claim_the_white_sea_lane` and `*NRF_fleet_that_does_not_dock`.
- `ICD`: 18 focuses; patched `*ICD_memorial_battalions`, `*ICD_claim_the_unburied_front`, and `*ICD_grave_columns_march`.

### Factory Successors

Audited `CFR` 47 focuses, `OGB` 23 focuses, and `MFR` 58 focuses. No duplicate coordinates, missing icons, missing AI blocks, empty rewards, duplicate focus ids, or non-reciprocal mutual exclusions detected. Patched `*OGB_notables_and_workshops`, `*MFR_workers_own_the_arsenal`, and `*MFR_eternal_arsenal_marches`.

## Before And After Behavior

Before:

- Several focuses with naval XP, dockyard, claim, core, war-goal, manpower, or industrial rewards were missing the matching search filters.
- `DSC_armies_that_do_not_demobilize` was aggressive through claims/wargoals/AI but did not directly reinforce the Dead Soldiers manpower/mobilization fantasy.
- `NRF_fleet_that_does_not_dock` claimed a naval route and applied high-chaos identity, but did not provide a direct naval-production payoff before the later end focus.

After:

- Patched filters now surface relevant naval, industry, manpower, army XP, and annexation categories for the changed focuses.
- `DSC_armies_that_do_not_demobilize` now adds front manpower, infantry equipment, artillery, army XP, and `dsc_revenant_mobilization`.
- `NRF_fleet_that_does_not_dock` now adds navy XP, convoys, and a coastal dockyard slot/building where a coastal state is available.

## Localisation Keys And Icon IDs Changed

- Localisation keys changed: none.
- Focus icon ids changed: none.
- New icon assets required: none.

## Missing Or Simplified Content

- Ukraine remains a broad, visually uneven tree. The safe patch pass did not attempt a geometric redesign.
- Belarus remains crowded in the Minsk rail/forest/political lanes. No safe coordinate-only patch would solve the underlying branch spacing.
- `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` are still compact 18-focus high-chaos trees; this pass did not add route families.
- `FTH`, `FEV`, and `NLC` are deeper but still rely on many helper/flag rewards. A parent design pass should decide which helper nodes become decisions, missions, or route-visible mechanics.
- Some filter mismatches remain outside the patched ids, especially in `TSC`, `FEV`, `NLC`, and other non-targeted branches. I left them queued because the task requested bounded patches, not a broad sweep.

## Icon Coverage Table

| Tree | Focus icon assignment | Repeated or missing icon risk |
| --- | --- | --- |
| Ukraine | All audited focuses have an icon assignment | Some icons are generic/reused by route family; no missing icon ids detected by text audit. |
| Belarus | All audited focuses have an icon assignment | No missing icon ids detected by text audit. |
| FTH/FEV/NLC | All audited focuses have an icon assignment | Several shared-route icon patterns remain; not changed. |
| PRA/TSC/RMC/DSC/NRF/ICD | All audited focuses have an icon assignment | Compact trees use bespoke high-chaos icon ids; no missing icon assignment detected. |
| CFR/OGB/MFR | All audited focuses have an icon assignment | No missing icon assignment detected. |

## Localisation And Reward Mismatch List

- No missing focus name/description keys were patched in this pass.
- Reward/filter mismatches patched are listed under Changed Focus IDs.
- Potential remaining mismatch: player-facing descriptions may still undersell helper-based rewards in older flag-heavy nodes. A localisation audit should compare text against helper effects after the parent accepts route-depth changes.

## AI Behavior Gaps

- All audited high-risk focuses have `ai_will_do`.
- Most route-aware AI is still local `ai_will_do` weighting rather than a full country-level strategy plan.
- Compact high-chaos trees weight chaos-tier and war-state decisions, but their AI does not yet deeply react to all decision-category state, e.g. rolling stock, revenant fleet authority, or custom splinter route completion.

## High-Priority Fixes Remaining

1. Ukraine layout and route readability: split the political, League, foreign, expansion, and high-chaos agriculture lanes into a planned geometry pass.
2. Belarus layout: re-space the early Minsk trunk and route fork so rail, forest, corridor, and League lines are readable without crowding.
3. TSC filter and reward identity: align observatory/perimeter/starfall filters with air, industry, manpower, and annexation effects.
4. FEV/NLC filter pass: finish filter consistency for rail, harbor, station, weather, winter, and volunteer-school focuses.
5. Custom splinter depth: convert more helper-only focuses into visible decisions, missions, target state work, or route mechanics.

## Validation Run

Commands run:

```bash
python3 - <<'PY'
from pathlib import Path
files=[Path(p) for p in ['common/national_focus/005_soviet_collapse_republics.txt','common/national_focus/005_soviet_collapse_custom_splinters.txt','common/national_focus/005_soviet_collapse_factory_successors.txt','common/national_focus/005_soviet_collapse_ancient_restorations.txt']]
for p in files:
    txt=p.read_text(encoding='utf-8-sig')
    depth=0
    min_depth=0
    for ch in txt:
        if ch=='{': depth+=1
        elif ch=='}':
            depth-=1
            min_depth=min(min_depth,depth)
    print(f'{p}: final_depth={depth} min_depth={min_depth}')
PY
rg -n '<=|>=' common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt || true
```

Result:

- Brace depth: all four audited focus files ended at `final_depth=0`, `min_depth=0`.
- Unsupported `<=` or `>=`: no matches.
- Duplicate focus ids: none found across the four audited files.
- Non-reciprocal mutual exclusions: none found across the four audited files.
- Coordinate collisions: none found across the four audited files.
- Patched focus filter recheck: all 19 changed focuses contain the intended filters.

## Skipped Validation And Why

- No live HOI4 load test was run from this subagent.
- No full localisation auditor was spawned; this patch did not edit player-facing text.
- No commit was made because the worktree already contained concurrent uncommitted edits in the same Soviet Collapse files. Committing only this subagent's hunks would require staging within files that also contain unrelated edits.

## Remaining Route Risks

- The broader user complaint is still valid at design level: some Soviet Collapse trees are mechanically improved but still feel dense, helper-heavy, or visually messy.
- This patch reduces filter mismatch and strengthens two high-chaos endpoint rewards. It does not redesign Ukraine, Belarus, League, factory, or high-chaos route families.
- Existing plan/handoff files in `docs/plans/005_soviet_collapse_plans/` should be reviewed by the parent before scheduling the next route-design pass.

## Plan Handoff Path

No new broad improvement plan was written. This patch handoff is:

`docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_tree_bounded_audit_identity_filter_patch_handoff.md`
