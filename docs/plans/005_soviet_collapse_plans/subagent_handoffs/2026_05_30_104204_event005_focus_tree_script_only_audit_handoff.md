# Event 005 Soviet Collapse Focus Tree Script-Only Audit Handoff

Timestamp: 2026-05-30 10:42 UTC

Auditor: Chaos Redux focus tree subagent

Constraint: flags, sprites, and visual asset folders were not read, written, or modified. This audit is script/localisation/docs only.

## Scope

Audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Related script-only support where needed for focus helper/reward tracing:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/ideas/005_soviet_collapse_ideas.txt`
  - `common/ai_strategy/005_soviet_collapse.txt`
  - `localisation/english/*005_soviet_collapse*_l_english.yml`

I did not inspect interface `.gfx`, sprite definitions, `gfx/`, `flags/`, or any flag asset.

## Files Changed

| File | Change |
|---|---|
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_104204_event005_focus_tree_script_only_audit_handoff.md` | Added this audit handoff. |

No focus tree gameplay file was patched in this pass.

Changed focus ids: none.

Localisation keys changed: none.

Icon ids changed: none.

## Route Coverage Table

| Route family | Implemented files/trees | Current status | Remaining gap |
|---|---|---|---|
| Ukraine major republic | `soviet_collapse_ukraine_focus_tree`, 83 focuses | Present and mechanically broad; no current duplicate coord/pathline risk found. | Still helper-heavy and should get deeper route-specific decision, expansion, grain, Black Sea, League, Bread State, and Black Banner consequences. |
| Generic breakaway fallback | `soviet_collapse_breakaway_focus_tree`, 36 focuses | Present fallback emergency tree. | Acceptable as fallback only; not a bespoke long-lived identity tree. |
| Internal republics | `soviet_collapse_internal_republic_focus_tree`, 62 focuses | Present with internal-regional hooks. | Needs less shared-helper feel and more regional route payoff if used for important tags. |
| Baltic/Caucasus/Central Asia/Moldova/Belarus/Kazakhstan republics | Republic file, 40-92 focuses per tree | Present and localized. Ukraine, Belarus, Kazakhstan are the strongest. | Belarus/corridor and Moldova/Central Asia routes still need more concrete decision and postwar mechanics. |
| Full custom splinters | FTH, BSC, TNC, ALA, BBH, KRS, UDC, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, BAC, ARD, NLC; 47 focuses each | Present. | Still templated across many countries. Needs identity-specific mechanics, aggression, claims/cores, postwar handling, and route AI beyond shared helpers. |
| Crisis/special splinters | PRA 22 focuses; TSC/RMC/DSC/NRF/ICD 18 focuses | Present but compact. | Too shallow for the user's requested overpowered chaos countries unless explicitly reclassified as short crisis trees. |
| Factory successors | CFR 47, OGB 23, MFR 58 focuses | CFR/MFR have real forks and stronger identity; OGB remains compact. | OGB is too shallow; CFR/MFR still need more operating-model mechanics, not only factory/war-goal payoffs. |
| Ancient restorations | KZR/SOG/KHW/ALN, 16 focuses each | Present as compact restoration packages. | Shallow by focus-tree skill standard; needs broader route plan before claiming full depth. |

## Mechanical Audit Results

| Check | Result |
|---|---|
| Focus count | 1,698 focuses across 41 focus trees. |
| Duplicate focus ids | 0. |
| Duplicate coordinates | 0 duplicate coordinate groups after resolving same-line `x =`/`y =` assignments. |
| Same-row prerequisite line risks | 0. |
| Vertical pathline-through-focus risks | 0 detected by same-column parent/child scan. |
| Mutual-exclusion midpoint/through-focus risks | 0 detected by same-row mutual-exclusion scan. |
| Direct `add_ideas`/`add_timed_idea` in focuses | 0 in all four focus files. |
| Focus calls to directly idea-granting scripted helpers | 0 direct focus calls to helpers whose own block contains `add_ideas`/`add_timed_idea`. |
| Helper idea grant definitions in event scripted effects | 45 scripted effect blocks in `common/scripted_effects/005_soviet_collapse_effects.txt` contain direct `add_ideas` or `add_timed_idea`; most are setup, staged republic idea, or endpoint helpers. |
| Common focus helper density | `soviet_collapse_apply_focus_legal_recognition` 305 calls; `soviet_collapse_apply_focus_depot_and_supply_control` 258; `soviet_collapse_apply_focus_military_consolidation` 254; `soviet_collapse_apply_focus_league_preparation` 220; `soviet_collapse_apply_focus_foreign_channel` 176; `soviet_collapse_apply_focus_high_chaos_identity` 98. |
| Missing focus icon assignments | 0. Sprite-definition existence was not validated because the user forbade sprite/GFX inspection. |
| Missing `ai_will_do` | 0. |
| Missing search filters | 0. |
| Missing focus localisation names/descriptions | 0 missing names, 0 missing descriptions across `localisation/english/*005_soviet_collapse*_l_english.yml`. |
| Unsupported `<=`/`>=` in audited script files | 0. |
| Bracket depth | Final depth 0/min depth 0 for all four focus files plus checked support files. |

Ukraine/Belarus spacing verification:

- `soviet_collapse_ukraine_focus_tree`: 83 focuses, x range 4-34, y range 0-18, no duplicate coords, no same-row prerequisites, no vertical path-through-focus risk, no mutual-exclusion through-focus risk.
- `soviet_collapse_belarus_focus_tree`: 53 focuses, x range 3-28, y range 0-16, no duplicate coords, no same-row prerequisites, no vertical path-through-focus risk, no mutual-exclusion through-focus risk.

## Idea Spam Finding

The specific current complaint "one focus gives the same idea multiple times" was not reproduced in the four focus files by direct scan:

- No focus contains direct `add_ideas` or `add_timed_idea`.
- No focus directly calls a helper whose own block directly contains `add_ideas` or `add_timed_idea`.
- The repeated direct-updater class appears to have been cleaned by prior passes.

The broader complaint remains valid as a design/reward issue:

- The focus trees rely very heavily on shared helper rewards. Even when those helpers avoid direct idea spam, they make focus rewards feel similar.
- `soviet_collapse_update_consolidated_republic_ideas` still owns staged republic spirit swaps in `common/scripted_effects/005_soviet_collapse_effects.txt:5348` and contains many guarded `add_ideas` branches. That looks intentional and hidden, but it concentrates visible national-spirit payoff in one helper-led system.
- Setup/endgame helpers still add route ideas, for example custom splinter setup helpers around `common/scripted_effects/005_soviet_collapse_effects.txt:15000-15544` and returned-name/endgame helpers around `:14545-14829`. These are not duplicated by focus surface scan, but they reinforce helper-led reward identity.

## Worst Remaining Trees/Routes Needing Full Rework

| Priority | Tree/route | Example current issue | What it should unlock |
|---|---|---|---|
| 1 | `PRA_soviet_collapse_focus_tree`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:1217` | 22 focuses; rail identity exists, but many rewards are rail construction, trains, support equipment, and endpoint war goal. | A railway-state mechanic: junction-control decisions, supply corridor missions, armored train deployments, toll/neutral-passage diplomacy, rail denial operations, and postwar rail integration. |
| 2 | `DSC_soviet_collapse_focus_tree`, `005_soviet_collapse_custom_splinters.txt:2772` | 18 focuses; dead-soldiers concept is too short for a major chaos actor. | Manpower revival/escalation loop, aggressive war goals, occupied-state cores or memorial integration, relentless-war AI, casualty-fed bonuses, and postwar "roll call" settlement mechanics. |
| 3 | `NRF_soviet_collapse_focus_tree`, `005_soviet_collapse_custom_splinters.txt:3369` | 18 focuses; naval/dead-fleet concept is still mostly compact endpoint content. | Naval warfare package: dockyards, convoy raiding, coastal claims, fleet/dead-convoy missions, Arctic port seizures, naval invasion prep, and maritime postwar integration. |
| 4 | `OGB_soviet_collapse_focus_tree`, `common/national_focus/005_soviet_collapse_factory_successors.txt:1172` | 23 focuses; some claims/wargoals exist, but it remains shallow for an OP restored Volga successor. | Volga restoration route family with legitimacy, river tolls, Kazan/Ufa settlement, IUL rivalry outcomes, staged claims/cores, religious/scholarly governance split, and regional AI expansion. |
| 5 | `TSC_soviet_collapse_focus_tree`, `005_soviet_collapse_custom_splinters.txt:1814` | 18 focuses; high-chaos Tunguska identity needs more than endpoint spectacle. | Starfall pressure mechanic, scientific cult vs containment route, regional anomaly decisions, targeted war goals, special units, and AI high-risk escalation gates. |
| 6 | `ICD_soviet_collapse_focus_tree`, `005_soviet_collapse_custom_splinters.txt:3873` | 18 focuses; iron/dead commissariat is compact and not yet a full overpowered state. | Factory-death command economy, forced production decisions, undead/commissariat manpower loop, war goals, cores, and occupation conversion mechanics. |
| 7 | `CFR_soviet_collapse_focus_tree`, `common/national_focus/005_soviet_collapse_factory_successors.txt:17` | Stronger than most, but still relies on public-works helpers and a limited construction-decision layer. | Civilian construction directorate system: escalating build queues, client-city protectorates, building-debt decisions, factory-in-every-capital route, and map-targeted reconstruction/conquest choices. |
| 8 | `MFR_soviet_collapse_focus_tree`, `005_soviet_collapse_factory_successors.txt:1777` | 58 focuses and many arsenal rewards, but the state concept should be more oppressive and mechanically distinct. | Arms-order economy: production-line decisions, arms-for-recognition diplomacy, client arming, forced procurement, armored train/arsenal units, and war-market escalation AI. |
| 9 | `ARD_soviet_collapse_focus_tree` / `NLC_soviet_collapse_focus_tree`, custom splinter file | 47-focus shapes exist, but naval/polar identities still share generic helper rhythms. | Naval directorate/polar warfare mechanics: dockyard expansion, convoy control, Arctic port missions, naval invasion routes, coastal fortification, and postwar port settlement. |
| 10 | Ancient restorations KZR/SOG/KHW/ALN | 16-focus packages, repeated ancient icon families and compact rewards. | Distinct restoration identity per tag: old-border proof, symbolic legitimacy, route-specific claims, patron bargains, integration missions, and non-generic ancient-state AI. |

## Icon Coverage Table

| File | Focuses | Missing icon assignment | Repeated icon concern |
|---|---:|---:|---|
| `005_soviet_collapse_republics.txt` | 501 | 0 | Repeated families remain, e.g. `GFX_ukr_soviet_collapse_democratic`, `GFX_moldova_soviet_collapse_ukrainian_corridor`, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | Repeated icon families remain across templated splinters, e.g. FEV/SZA diplomatic families and ancient-style shared motifs. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | CFR has repeated construction/civilian motifs by concept; still needs unique variants when sprite work is allowed. |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | Many icons repeat once per ancient tree by design; this reinforces the shallow shared-template feel. |

Sprite-definition coverage was intentionally skipped because of the no-sprites/no-GFX constraint.

## Localisation And Reward Mismatch List

Localisation coverage:

- 0 missing focus names.
- 0 missing focus descriptions.
- No localisation was patched.

Reward/design mismatches that remain:

- `PRA_claim_the_branch_lines`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:1656`: title implies territorial/rail-line claims; current payoff is decision/rail construction and should make rail-junction claims or route objectives more explicit.
- `OGB_kazan_ferry_offices`, `common/national_focus/005_soviet_collapse_factory_successors.txt:1321`: named Kazan/Volga ferry-office focus uses generic random core construction. It should target Volga/Kazan trade states or unlock a ferry/toll decision.
- `CFR_build_the_border_bend_the_border`, `common/national_focus/005_soviet_collapse_factory_successors.txt:974`: title and annexation filter imply direct border change; reward appears more like construction/border pressure. Needs either a concrete claim/war-state payoff or a filter/name adjustment.
- Shallow crisis endpoints such as `DSC_congress_of_the_dead_army`, `NRF_northern_revenant_fleet`, and `ICD_*` endpoints are conceptually large but still sit in short trees; they need route families behind them, not only endpoint helper ideas.

## AI Behavior Gaps

- Every focus has `ai_will_do`, but route-aware AI is uneven.
- Ukraine, Belarus, and Kazakhstan have better route-aware AI strategy support in `common/ai_strategy/005_soviet_collapse.txt`.
- Crisis splinters and many 47-focus custom splinters still need AI that matches identity: railway countries should chase rail/supply nodes; dead-soldier countries should prefer aggression/manpower/cores; naval directorates should prioritize ports, dockyards, convoys, and coastal wars; factory countries should prioritize arms/civilian construction and client wars.
- Adding more weights without deeper route mechanics would preserve shallow structure, so this should be paired with the route rework.

## High-Priority Fixes First

1. Expand or explicitly classify the shallow crisis trees: `PRA`, `DSC`, `NRF`, `TSC`, `ICD`, `RMC`.
2. Expand `OGB_soviet_collapse_focus_tree` beyond the current compact 23-focus package or document it as intentionally limited.
3. Convert repeated helper-heavy custom splinter rewards into identity mechanics: rail/supply for PRA, manpower/cores/aggression for DSC, naval warfare for NRF/ARD/NLC, construction decisions for CFR, production/arms-market mechanics for MFR.
4. Add postwar settlement hooks to expansion routes: cores, claims, occupation decisions, protectorates, integration missions, or border settlement events.
5. Add route-aware AI after mechanics exist, not before.
6. When sprite work is allowed later, assign more unique focus icon variants; do not do that in this no-sprites pass.

## Route Behavior Before And After

Before: current script already has broad focus coverage and clean mechanical layout, but many routes still play through shared helper rewards and compact endpoint ladders.

After this audit: no route behavior changed. The handoff identifies remaining full-route work and confirms that the obvious small script issues requested for this pass were not currently present.

## Validation Run

Commands run:

```bash
python3 - <<'PY'
from pathlib import Path
files=list(Path('common/national_focus').glob('005_soviet_collapse_*.txt'))+[Path('common/scripted_effects/005_soviet_collapse_effects.txt'),Path('common/ideas/005_soviet_collapse_ideas.txt'),Path('common/ai_strategy/005_soviet_collapse.txt')]
for p in files:
    text=p.read_text(encoding='utf-8-sig')
    depth=0
    min_depth=0
    for ch in text:
        if ch=='{': depth+=1
        elif ch=='}':
            depth-=1
            min_depth=min(min_depth,depth)
    print(f'{p}: final_depth={depth} min_depth={min_depth}')
PY
```

Result: final depth 0/min depth 0 for every checked file.

```bash
rg -n "<=|>=" common/national_focus/005_soviet_collapse_*.txt common/scripted_effects/005_soviet_collapse_effects.txt common/ideas/005_soviet_collapse_ideas.txt common/ai_strategy/005_soviet_collapse.txt || true
```

Result: no matches.

```bash
rg -n "add_ideas|add_timed_idea" common/national_focus/005_soviet_collapse_*.txt || true
```

Result: no matches.

Additional Python parser audits were run for focus counts, duplicate focus ids, duplicate coords, same-row prerequisite risks, pathline-through-focus risks, mutual-exclusion midpoint risks, missing icons, missing `ai_will_do`, missing search filters, localisation names/descriptions, and direct focus-called idea helpers. Results are summarized above.

## Skipped Validation And Why

- Sprite/GFX/icon-definition validation skipped because the parent/user explicitly forbade touching or inspecting flags/sprites/GFX assets.
- In-game screenshot/layout validation skipped because it would require visual asset/UI rendering outside this script-only audit.
- No gameplay patch validation was run because no gameplay file was changed.

## Remaining Route Risks

- The broad user complaint about shallow/random branches remains open.
- The exact repeated-same-idea-from-one-focus issue appears resolved at the direct focus/helper surface, but helper-led staged ideas remain dense and should be kept under review during future reward work.
- Ukraine and Belarus spacing is mechanically clean by coordinate/pathline scan, but visual screenshot confirmation is still pending if the parent wants UI proof later.
- Existing broader plan remains relevant: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets` for asset-boundary rules only; no assets were inspected or modified.
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
