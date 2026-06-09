# Event005 Republic Focus Audit 2 Handoff

Scope: Event005 Soviet Collapse republic focus tree audit, primarily `common/national_focus/005_soviet_collapse_republics.txt`.

Flag constraint: no flag files, flag gfx, or flag interface definitions were edited.

Context note: the worktree and the scoped focus file already had broad uncommitted changes before this pass. This handoff lists only the bounded edits made in this audit.

## Changed Files

| File | Change type |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Bounded focus prerequisite, layout, and reward patch. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_event005_republic_focus_audit_2_handoff.md` | Required subagent handoff. |

## Exact Focus IDs Changed

| Focus id | What changed | Reason |
| --- | --- | --- |
| `ukr_soviet_collapse_officer_patronage_lists` | Removed `prerequisite = { focus = ukr_soviet_collapse_british_caution }`. Kept the Directory and grain-loan prerequisites. | Removed a long far-right diplomacy to left military pathline. The focus text/reward are about officer vetting and patronage risk, so the British observer gate was an overconstraint rather than a core requirement. |
| `ukr_soviet_collapse_the_directory_state` | Normalized local indentation, kept the existing custom tooltip, and added `soviet_collapse_spawn_focus_mobile_column = yes` inside the hidden reward package. | The finisher tooltip already promises a mobile command package. The existing helper makes the reward mechanically match the focus identity without adding a new mechanic or visible idea spam. |
| `blr_soviet_collapse_orders_printed_like_timetables` | Moved from `x = 18`, `y = 7` to `x = 19`, `y = 9`. | Its route parent `blr_soviet_collapse_military_transit_directorate` is at `y = 8`, so the old placement put a prerequisite parent below the child. The new placement keeps the tree compact and restores downward pathline flow. |

## Behavior Before And After

| Area | Before | After |
| --- | --- | --- |
| Ukraine officer vetting branch | A military Directory follow-up also required `ukr_soviet_collapse_british_caution`, creating a long cross-tree line from diplomacy into the left military lane. | The focus remains gated by the Directory route and the grain-loan support branch, but no longer depends on the British diplomacy node. |
| Ukraine Directory finisher | The tooltip described a mobile command package, while the hidden package provided command/war preparation but did not spawn the mobile column. | The finisher now calls the existing mobile-column helper in the hidden effect, matching the existing tooltip and strengthening the military endpoint. |
| Belarus military transit follow-up | `blr_soviet_collapse_orders_printed_like_timetables` sat above one of its required parents. | It now sits below the route parent, with no duplicate coordinate and no one-unit same-row collision. |

## Audit Findings

| Area | Result |
| --- | --- |
| Ukraine layout | No duplicate coordinates and no parent-below-child prerequisites after patch. The removed British prerequisite also removes the known long diplomacy-to-military pathline into `ukr_soviet_collapse_officer_patronage_lists`. |
| Belarus layout | No duplicate coordinates and no parent-below-child prerequisites after moving `blr_soviet_collapse_orders_printed_like_timetables`. |
| Branch depth and reward meaning | The Ukraine Directory endpoint now has a concrete unit payoff through an existing helper. Broader route redesign was not attempted. |
| Focus filters | Changed focuses already had suitable filters for their roles. No filter edits were needed. |
| Mutually exclusive nodes | No isolated or decorative mutually exclusive nodes were added. Existing Ukraine and Belarus route-lock exclusions were preserved. |
| Localisation | No localisation keys were added or renamed. The existing `ukr_soviet_collapse_the_directory_state_mechanics_tt` already describes the mobile command package now provided by the reward. |

## Validation

| Check | Result |
| --- | --- |
| Required wiki/docs/reference pass | Read `AGENTS.md`, `hoi4-focus-trees`, `chaos-redux-events`, `chaos-redux-subagents`, offline core wiki pages, offline National Focus wiki page, vanilla script concept/effects/triggers docs, and vanilla focus examples before editing. |
| Direct focus idea ops scan | `rg -n "add_ideas|remove_ideas|swap_ideas|modify_ideas" common/national_focus/005_soviet_collapse_republics.txt` returned no matches. |
| Unsupported comparison operator scan | The less-than-or-equal / greater-than-or-equal token scan returned no matches in the focus file. |
| Brace-depth check | `common/national_focus/005_soviet_collapse_republics.txt: brace_depth=0 min_depth=0 bad=[]`. |
| Duplicate same-tree coordinate scan | Ukraine and Belarus reported `duplicates {}`. |
| Parent-below-child prerequisite scan | Ukraine and Belarus reported `parents_not_above []`. |

## Skipped Checks

| Check | Reason |
| --- | --- |
| In-game load/screenshot validation | Not available in this subagent pass. |
| Full localisation audit | No focus ids or localisation keys changed. |
| `.gfx` sprite definition audit | No icon ids changed, and flags/gfx/interface definitions were explicitly out of scope. |
| Full republic tree redesign | Out of scope; this pass was limited to small/local focus-file fixes and required handoff. |

## Remaining Gaps

1. Ukraine and Belarus still have dense mid-tree route clusters. The patched items remove two concrete pathline problems, but a full screenshot-guided layout pass would be needed to prove every visible line is clean in the client.
2. Several major republic routes still depend on shared helper packages for payoff. The Directory endpoint was strengthened here, but broader leader/advisor/law/cosmetic route consequences remain parent-level design work.
3. The worktree contains many pre-existing uncommitted changes in Event005 and Event006 files. Parent review should isolate this handoff's two-file patch from earlier dirty-worktree state.
