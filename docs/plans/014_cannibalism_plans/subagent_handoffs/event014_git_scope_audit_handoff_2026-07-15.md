# Event 014 Git Scope Audit Handoff — 2026-07-15

## Result

The Event 014 tranche is safe to stage entirely by whole-file pathspec. Against master at HEAD 4f634045877c970b8472b123210ec0486ff8ad0c:

- pre-report scope: 977 paths;
- modified: 846;
- deleted: 76;
- untracked: 55;
- mixed shared files: 0;
- Event 014 hunks in shared files: 0;
- staged paths during this audit: 0.

This handoff and the companion audit add two untracked Event 014 documentation files, so the expected final staging count is 979 paths with 57 untracked paths.

The detailed evidence and shared-file classifications are in:

- docs/plans/014_cannibalism_plans/audits/event014_git_scope_audit_2026-07-15.md

## Exact validated staging command

~~~powershell
git add -A -- ':(glob)**/014_cannibalism*' ':(glob)**/014_cannibalism*/**' ':(glob)**/zz_014_cannibalism*' ':(glob)gfx/flags/**/CB[A-H]*.tga' ':(glob)gfx/flags/**/CBL*.tga' ':(glob)gfx/flags/**/ZZZ_CANNIBALISM_HANNIBAL*.tga'
~~~

The pathspec selected 977 of 977 independently classified pre-report paths, with zero missing and zero extra. The two report paths are covered by the 014_cannibalism_plans directory pathspec.

## Whole-file scope

Stage:

- every current path whose segment or basename begins 014_cannibalism;
- every current basename beginning zz_014_cannibalism;
- the 195 modified Event 014 flags defined by 65 exact flag stems across root, medium, and small tiers.

The exact flag roots are CBA-CBH, CBL, CBL_CENTRAL_COMMAND, CBL_HOST_CONFEDERATION, CBL_RITUAL_STATE, and ZZZ_CANNIBALISM_HANNIBAL, each with the empty, communism, democratic, fascism, and neutrality suffixes.

The 76 deleted paths are intentional scope: 74 superseded Event 014 runtime loaders plus two superseded static portrait DDS files.

## Hunk instructions

There are no Event 014 mixed-file hunks. Do not stage any shared file or any portion of one for this tranche.

In particular, exclude the modified shared achievement registry/localisation, Event Log/evolution/Event Details effects and localisation, scenario registry and docs, chaos meter files, dynamic effects and docs, generic GUI localisation, the catalog workbook, and all shared audio/GFX registries.

The workbook was compared at cell level. Its current changes belong only to Event 015, Event 019, and SCN-013; no Event 014 cell or table-range change is present.

## Important false positives to exclude

- UTOPIA_MANIFESTO and utopia flags;
- ZZZ_weaponized_wendigo flags;
- Event 019 prototype_cannibalization source, processed, keyed, and DDS assets;
- all Event 006, Event 015, Event 019, Fallout, and CBRN changes outside dedicated Event 014 paths.

## Parent verification

Immediately before staging:

1. Confirm HEAD is still 4f634045877c970b8472b123210ec0486ff8ad0c.
2. Run the exact pathspec command.
3. Confirm git diff --cached --name-only reports 979 paths.
4. Inspect git diff --cached --name-status and verify that every path matches the dedicated Event 014 or exact flag rules above.
5. Keep every shared file out of the staged set.

If HEAD or the worktree changed after this handoff, rerun the scope comparison before relying on the 979-path count.

## Files created by this subagent

- docs/plans/014_cannibalism_plans/audits/event014_git_scope_audit_2026-07-15.md
- docs/plans/014_cannibalism_plans/subagent_handoffs/event014_git_scope_audit_handoff_2026-07-15.md

No gameplay, asset, localisation, workbook, Git index, or commit state was changed.

## Simplifications, omissions, and blockers

None for the audit. This is a staging-scope handoff only; it does not replace the feature's gameplay, visual, localisation, or completion audits.

## Skills used

- chaos-redux-subagents;
- xlsx.

No skill was created or updated.
