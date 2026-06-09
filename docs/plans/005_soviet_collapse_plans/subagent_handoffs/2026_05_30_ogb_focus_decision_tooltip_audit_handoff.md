# 2026-05-30 Event 005 Focus Audit and OGB Decision Tooltip Patch

## Scope

Audited and patched only the requested Event 005 focus surfaces:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

Read-only context used:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- Event 005 localisation and docs
- Existing Event 005 focus handoffs under this folder

Required references read before inspection/editing: `AGENTS.md`, `hoi4-focus-trees`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, the required offline wiki pages including National focus/Decision/Event/Idea/AI/Localisation/Effect/Triggers/Scopes/Data structures/Modifiers/On actions, vanilla documentation under `~/projects/Hearts of Iron IV/documentation/`, vanilla decision documentation, and vanilla `common/national_focus/soviet.txt`.

No web access was used. No gfx, flags, Event 006 files, decisions, scripted effects, triggers, or localisation were edited.

## Changed Files

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | Added one missing `unlock_decision_tooltip` for an existing OGB decision already gated by the same focus flag. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_ogb_focus_decision_tooltip_audit_handoff.md` | This handoff. |

The worktree was already dirty in the three scoped focus files and many unrelated Event 005/Event 006 files. This handoff claims only the OGB tooltip line and this markdown file.

## Changed Focus IDs

| Focus id | Before | After | Why safe |
| --- | --- | --- | --- |
| `OGB_raise_the_heritage_guard` | Set `ogb_focus_raise_the_heritage_guard` and called `soviet_collapse_apply_ogb_focus_heritage_guard_muster`, but did not surface the existing focus-gated decision. | Also shows `unlock_decision_tooltip = ogb_guard_kazan_ferry_line`. | `ogb_guard_kazan_ferry_line` already has `visible = { tag = OGB has_soviet_collapse_successor_decision_surface = yes has_country_flag = ogb_focus_raise_the_heritage_guard }` in `common/decisions/005_soviet_collapse_decisions.txt:6852`. The patch changes focus tooltip visibility only; it does not alter decision availability, costs, AI, icons, localisation, flags, or rewards. |

## Route Behavior Before and After

| Route | Before | After |
| --- | --- | --- |
| OGB heritage guard / river defense | Completing `OGB_raise_the_heritage_guard` silently made `ogb_guard_kazan_ferry_line` visible through its country flag. | The focus now advertises the existing ferry-line guard decision at completion, reducing hidden mechanic clutter. |

No localisation keys changed. No icon ids changed.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine political, military, industry, diplomacy, expansion, League, Black Sea/grain routes | `soviet_collapse_ukraine_focus_tree` | Partial/deep but cluttered | 83 focuses and several decision hooks exist, but route-selector geometry and helper-heavy rewards remain high priority. |
| Generic and internal republics | `soviet_collapse_breakaway_focus_tree`, `soviet_collapse_internal_republic_focus_tree` | Simplified | Large portions still use flat rewards and consolidated helper calls without direct decisions, claims, cores, or postwar mechanics. |
| Baltic, Caucasus, Central Asia, Moldova, Belarus, Kazakhstan republic routes | Regional republic trees in `005_soviet_collapse_republics.txt` | Partial | Belarus/Kazakhstan/Central Asia have some hooks; Baltic/Moldova/internal republics remain weak on direct route mechanics and expansion payoff. |
| Full custom splinters | 47-focus trees in `005_soviet_collapse_custom_splinters.txt` | Broad but mechanic-light | Most have route labels and local AI weights, but many still lack direct decision/mission/claim/core/wargoal hooks in focus rewards. |
| Compact chaos/special actors | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` | Shallow to partial | PRA/DSC/NRF have better decision integration; TSC/RMC/ICD still need full special-mechanic depth. |
| Factory successors | `CFR`, `OGB`, `MFR` | Partial | CFR/MFR are stronger but still reward-heavy. OGB remains the shallowest factory successor; this patch only surfaces one existing OGB decision. |

## Idea Spam and Helper Audit

Direct focus idea operations in the three scoped focus files:

| File | `add_ideas` | `swap_ideas` | `add_timed_idea` | `remove_ideas` | `soviet_collapse_update_consolidated_republic_ideas` calls |
| --- | ---: | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 0 | 0 | 0 | 0 | 30 |
| `005_soviet_collapse_custom_splinters.txt` | 0 | 0 | 0 | 7 | 64 |
| `005_soviet_collapse_factory_successors.txt` | 0 | 0 | 0 | 1 | 6 |

Findings:

- Direct visible idea-add spam is not present in the scoped focus files.
- The remaining perceived idea churn comes from repeated hidden calls to `soviet_collapse_update_consolidated_republic_ideas` and endpoint/helper logic, not direct focus `add_ideas`.
- The eight direct `remove_ideas` cases are cleanup/removal operations, not new idea spam.
- Broad helper-side lifecycle cleanup is outside this bounded focus-only patch.

## Missing or Simplified Content

- `OGB_soviet_collapse_focus_tree` still needs real Volga restoration depth: more decision staging, old-border arbitration, heritage guard follow-through, Idel-Ural compact/rivalry consequences, and a clearer symbolic-vs-expansion route payoff.
- `TSC`, `ICD`, `RMC`, and several 47-focus custom splinters remain route skeletons with repeated helper rhythm rather than strong mechanics.
- Baltic, Moldova, internal republics, and many full custom splinters still lack direct decision/mission/expansion hooks.
- Flat reward density remains a broad problem: many focuses still grant stability, political power, state buildings, equipment, XP, or helper variables without a route-defining payoff.
- Several trees still need postwar handling: claims/cores, integration decisions, settlement missions, puppeting/protectorate logic, or regional reaction.

## Layout Issues

High-priority layout risks remain:

- Ukraine route selectors around `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_officers_above_parties`, and `ukr_soviet_collapse_protectorate_debate` still need a deliberate route layout pass.
- Kazakhstan remains dense, especially early/mid route rows with many adjacent focuses and base-only AI.
- CFR and MFR have broad mutually exclusive geometry and prior dirty coordinate changes visible in `git diff`; I did not edit those inherited changes.
- No new coordinate patch was made in this pass.

## Icon Coverage

| File | Focuses | Icon assignments | Missing icon assignments | Notes |
| --- | ---: | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 501 | 0 | Repeated icon ids remain a design-quality issue, but no missing assignment was found. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 1005 | 0 | Repeated icon families remain high among templated 47-focus splinters. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 128 | 0 | OGB/MFR are cleaner than CFR; no icon touched. |

## Localisation and Reward Mismatch

- No localisation keys changed.
- The added decision tooltip uses the existing decision id `ogb_guard_kazan_ferry_line`; no new localisation key is required.
- Existing focus localisation remains present by prior/current audits, but broad reward-tone mismatch remains where focus names promise war plans, diplomacy, rail states, dead armies, restored names, or factory polities and rewards still resolve mostly to shared helper variables or flat stockpiles.

## AI Behavior Gaps

| File | Focuses | `ai_will_do` blocks | Missing AI blocks | Notes |
| --- | ---: | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 501 | 0 | Many republic focuses remain base-weight or lightly state-aware. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 1005 | 0 | Local route modifiers exist, but persistent route strategies and target selection remain uneven. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 128 | 0 | CFR/MFR/OGB have focus AI, but OGB needs more route strategy tied to restoration decisions and Idel-Ural/SOV targets. |

## High-Priority Fixes First

1. Deepen OGB beyond the current 23-focus compact route: add staged decision logic, Volga legitimacy thresholds, old-city settlement, heritage guard follow-up, and Idel-Ural compact/rivalry consequences.
2. Clean Ukraine route layout as a dedicated pass, not a one-node shuffle.
3. Add direct mechanics to Baltic, Moldova, internal republics, and zero-hook custom splinter trees.
4. Replace repeated flat stockpile/building/XP rewards with existing or new route-specific decision unlocks and postwar settlement hooks.
5. Add persistent route-aware AI strategies for aggressive chaos routes and factory successor ambitions.
6. Do an icon design pass after route structure stabilizes; do not touch flags/gfx during focus-only cleanup.

## Validation Run

Passed:

```sh
git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt
```

Brace-depth check:

```text
common/national_focus/005_soviet_collapse_republics.txt: final_depth=0 min_depth=0
common/national_focus/005_soviet_collapse_custom_splinters.txt: final_depth=0 min_depth=0
common/national_focus/005_soviet_collapse_factory_successors.txt: final_depth=0 min_depth=0
```

Unsupported operators:

```sh
rg -n '<=|>=' common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt
```

Result: no matches.

Other checks:

- Focus/icon/AI/search filter counts: `501/501/501/501`, `1005/1005/1005/1005`, `128/128/128/128`.
- Direct focus `add_ideas`, `swap_ideas`, `add_timed_idea`: 0 in all three scoped files.
- `ogb_guard_kazan_ferry_line` visibility gate confirmed in `common/decisions/005_soviet_collapse_decisions.txt:6852`.

Skipped validation:

- No in-game load, screenshot, or external HOI4 parser run.
- No localisation encoding rewrite; no localisation file changed.
- No commit made because the parent worktree is already dirty across Event 005 and Event 006 files, including preexisting changes in the scoped focus files.

## Remaining Route Risks

This patch is intentionally small. It improves one hidden existing OGB decision link, but the user complaint remains broadly valid: Event 005 focus trees are still too helper-heavy, layout-dense, and unevenly connected to decisions, expansion, postwar handling, and route AI. The next useful work should be a focused OGB/TSC/ICD/PRA/DSC/NRF mechanics tranche or a Ukraine/Kazakhstan layout and reward-depth pass, not more broad audit-only churn.
