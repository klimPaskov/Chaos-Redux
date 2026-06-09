# Event005 Parent Tranche: Internal Republic Release Core Refresh

Timestamp: 2026-06-04 UTC

Scope:
- `common/scripted_effects/005_soviet_collapse_effects.txt`

Parent constraints honored:
- No `gfx/flags`, `.tga`, flag sprites, or flag interface files were touched.
- No unrelated Event006 files were edited.
- No commit was made because the full active Soviet Collapse goal remains incomplete.

## Change

The internal republic release-core restoration helper now runs during active release checks as well as crisis initialization and terminal collapse.

Changed call sites:
- `soviet_collapse_maybe_release_threat_breakaway`
- `soviet_collapse_release_dynamic_follow_on_republics`

This means active Soviet Collapse games refresh the release cores for internal republic candidates before counting or selecting progressive follow-on releases. The release pipeline can therefore see niche republics such as Karelia, Komi, Tatarstan, Bashkortostan, Yamalia, Taymyria, Nenets, and other internal republic tags during ongoing collapse progression, not only when a new crisis starts or when Union Unmade is already terminal.

## Behavior

Before:
- Existing active collapse chains could miss internal republic candidates if their release cores were not present before the terminal/scenario path.
- Dynamic follow-on releases could still report no eligible niche republics even after Gathering Storm style chaos pressure.

After:
- Candidate counting and dynamic follow-on release loops refresh the internal republic release map first.
- Terminal/scenario release behavior remains unchanged except that it shares the same restored-core candidate pool.

## Validation

Commands run:
- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_092422_event005_focus_tree_full_current_audit_no_patch.md`
- `rg -n "<=|>=" common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Brace balance check on `common/scripted_effects/005_soviet_collapse_effects.txt`

Results:
- `git diff --check` passed.
- Unsupported operator scan returned no matches.
- Scripted effects brace balance: `0`.

## Remaining Gaps

This tranche does not complete the full focus-tree rework. The focus-tree audit at `2026_06_04_092422_event005_focus_tree_full_current_audit_no_patch.md` still identifies broad route-depth, reward-spine, and layout/pathline redesign work across all Event005 focus files.
