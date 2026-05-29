# Soviet Collapse Focus Route Layout and OGB Endpoint Patch Handoff

Date: 2026-05-29
Subagent: Chaos Redux focus tree subagent

## High-Priority Fixes First

| Priority | Issue | File/id references | Patch |
| --- | --- | --- | --- |
| High | Ukraine democratic and military follow-up focuses were direct children of the statehood selector, so their path lines sat among mutually exclusive route-lock nodes and made route semantics less clear. | `common/national_focus/005_soviet_collapse_republics.txt:633`, `:958` | `ukr_soviet_collapse_the_commander_or_the_cabinet` now requires `ukr_soviet_collapse_officers_above_parties`; `ukr_soviet_collapse_republic_of_laws` now requires `ukr_soviet_collapse_elections_under_shellfire`. |
| High | `ukr_soviet_collapse_british_caution` sat between mutually exclusive statehood route nodes as a direct child of `ukr_soviet_collapse_question_of_statehood`. | `common/national_focus/005_soviet_collapse_republics.txt:1394` | It now requires `ukr_soviet_collapse_foreign_courts_notice_kyiv`, matching its diplomacy text and removing the same-row route-lock obstruction. |
| High | Old Great Bulgaria's endgame helper was still only an idea application, weak for a high-chaos restoration endpoint. | `common/scripted_effects/005_soviet_collapse_effects.txt:14576` | `soviet_collapse_complete_old_great_bulgaria_endgame` now adds manpower, infantry equipment, artillery, controlled-state cores for its old trade city claims, guarded Soviet annexation war goal and AI, and rival-Idel-Ural war AI when the rival-seal route was chosen. |
| Medium | FTH had two exact focus coordinate collisions. | `common/national_focus/005_soviet_collapse_custom_splinters.txt:984`, `:1010` | Moved `FTH_commune_court_registers` and `FTH_tachanka_column_oaths` from `x = 6` to `x = 5`, preserving their branches while removing duplicate coordinates. |

## Changed Files

| File | Changes |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Ukraine prerequisite and small coordinate adjustments for three route-adjacent focuses. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | FTH coordinate-only layout cleanup for two focuses. |
| `common/scripted_effects/005_soviet_collapse_effects.txt` | Existing Old Great Bulgaria endgame helper strengthened. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_route_layout_ogb_patch_handoff.md` | This handoff. |

## Changed Identifiers

Changed focus ids:

- `ukr_soviet_collapse_the_commander_or_the_cabinet`
- `ukr_soviet_collapse_republic_of_laws`
- `ukr_soviet_collapse_british_caution`
- `FTH_commune_court_registers`
- `FTH_tachanka_column_oaths`

Changed helper id:

- `soviet_collapse_complete_old_great_bulgaria_endgame`

Localisation keys changed: none.

Icon ids changed: none.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine distinct political routes | Military directory, democratic Rada, socialist sovereignty, Black Banner, and foreign/protectorate branches. | Partial, improved | This pass fixed three route-line semantics issues. Full route reward identity still needs parent review. |
| Factory and construction authorities become very strong | CFR and MFR already have construction/arsenal trees; OGB is in the same factory-successor file as a restoration successor. | Partial | No CFR/MFR edits in this pass. OGB endpoint now has real military and territorial payoff. |
| Dead Soldiers Congress aggressive expansion | DSC has existing war-goal/core/assault-column endpoint content. | Present but still shallow | No direct DSC patch this pass because current DSC already has aggressive endpoint hooks; broader depth remains a redesign item. |
| Railway authority rails and supply | PRA has rail, supply-node, armored-train, corridor, junction, and endgame focuses. | Present | No direct PRA patch; current rail/supply identity matches the requested direction better than the remaining shallow trees. |
| Ancient restorations with real depth | KZR, SOG, KHW, ALN have 16 focuses each. | Missing depth | Too broad for a small patch. Needs implementation-ready redesign from existing follow-up plan. |
| Custom splinter route depth | Most full custom splinters have 47 focuses; crisis trees are 18-22 focuses. | Partial | FTH coordinate collision fixed. Several crisis trees remain too shallow for completion claims. |

## Missing or Simplified Content

| Area | Finding | References |
| --- | --- | --- |
| Direct duplicate `add_ideas` in focus files | None in the current four focus files. The active worktree appears to have moved focus idea application into helpers or removed direct focus idea adds. | Four focus files scanned; direct focus `add_ideas`, `add_timed_idea`, and `swap_ideas` count is 0. |
| Shallow crisis trees | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` remain much smaller than full 47-focus custom splinter trees. | `common/national_focus/005_soviet_collapse_custom_splinters.txt:1226`, `:1798`, `:2275`, `:2759`, `:3321`, `:3824` |
| Ancient restoration stubs | Four ancient-restoration trees have only 16 focuses each. | `common/national_focus/005_soviet_collapse_ancient_restorations.txt:30`, `:402`, `:775`, `:1151` |
| OGB route depth | OGB has 23 focuses, far below major high-chaos successor depth. | `common/national_focus/005_soviet_collapse_factory_successors.txt:1144` |
| Generic helper cadence | Many focus rewards still rely on shared recognition, depot, high-chaos, military, or legal helpers. | Current files broadly; see existing follow-up plan `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`. |

## Icon Coverage Table

| Check | Result |
| --- | --- |
| Missing `icon =` in parsed focus blocks | 0 in the four audited focus files. |
| Icon ids changed | 0. |
| Repeated icons | Still present by design in several shared/regional packages; not patched here because no intended replacement icon was clearly safer. |
| Asset work needed | None for this patch. Larger route redesign should request new icons for ancient restorations and shallow crisis tree route families. |

## Localisation and Reward Mismatch List

| Focus/helper | Status |
| --- | --- |
| `ukr_soviet_collapse_the_commander_or_the_cabinet` | Localisation already describes the Directory deciding command vs cabinet, matching the new military-route prerequisite. |
| `ukr_soviet_collapse_republic_of_laws` | Localisation already describes courts/radas/front votes, matching the new democratic-election prerequisite. |
| `ukr_soviet_collapse_british_caution` | Localisation describes British observers; prerequisite now follows the foreign-courts diplomacy branch. |
| `FTH_commune_court_registers`, `FTH_tachanka_column_oaths` | Coordinate-only changes, no text mismatch introduced. |
| `soviet_collapse_complete_old_great_bulgaria_endgame` | Helper now better matches Old Great Bulgaria restoration/endgame text by adding cores, army stores, and aggressive war behavior instead of only `ogb_restored_volga_empire`. |

## AI Behavior Gaps

Fixed:

- `soviet_collapse_complete_old_great_bulgaria_endgame` now adds `conquer` and `antagonize` AI against `SOV` when it creates the Soviet war goal.
- Rival-seal OGB now gets `conquer` and `antagonize` AI against `IUL` when the guarded rival route war goal is created.

Remaining:

- Many custom splinters still rely on focus-local `ai_will_do` instead of persistent route strategy plans.
- High-chaos tags should get more route-specific target selection and postwar behavior.
- Ancient restorations lack route-aware AI because the trees are still shallow.

## Validation Run

Commands run:

```bash
python3 - <<'PY'
from pathlib import Path
files=[
'common/national_focus/005_soviet_collapse_republics.txt',
'common/national_focus/005_soviet_collapse_custom_splinters.txt',
'common/national_focus/005_soviet_collapse_factory_successors.txt',
'common/national_focus/005_soviet_collapse_ancient_restorations.txt',
'common/scripted_effects/005_soviet_collapse_effects.txt']
for fn in files:
    depth=0
    for line in Path(fn).read_text(encoding='utf-8-sig', errors='ignore').splitlines():
        depth += line.count('{') - line.count('}')
    print(fn, depth)
PY
rg -n '<=|>=' common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt common/scripted_effects/005_soviet_collapse_effects.txt
git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/scripted_effects/005_soviet_collapse_effects.txt
```

Results:

| Check | Result |
| --- | --- |
| Brace depth | Final depth 0, no negative depth in all four focus files and `common/scripted_effects/005_soviet_collapse_effects.txt`. |
| Unsupported operators | No `<=` or `>=` matches. |
| Diff whitespace | `git diff --check` passed for the three changed script files. |
| Direct focus idea rewards | 0 direct `add_ideas`, `add_timed_idea`, or `swap_ideas` lines inside focus blocks in the four audited focus files. |
| Duplicate coordinates | 0 after patch in the four audited focus files. |
| Same-row mutual-exclusion middle-node scan | 0 after patch in the four audited focus files. |

## Skipped Validation

- No HOI4 launch or in-game screenshot pathline validation was run.
- No localisation BOM check was needed because localisation was not edited.
- No commit was created because the parent worktree is already heavily dirty with many Soviet Collapse changes in the same files, and this subagent should not claim unrelated pending work.

## Remaining Route Risks

1. The focus tree redesign requirement is broader than a safe small patch. The existing plan at `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` remains the implementation-ready handoff for full depth work.
2. OGB is stronger after the endpoint patch, but it still needs a full restoration route expansion if it is meant to stand beside CFR/MFR as a major high-chaos successor.
3. Ancient restorations are still shallow 16-focus packages.
4. Several 47-focus custom splinters still use similar reward cadence and need tag-specific mechanics, decisions, target states, and AI strategies.
5. Static coordinate scans cannot prove in-game Bezier pathline aesthetics; parent should do visual focus-tree review after broader layout work.
