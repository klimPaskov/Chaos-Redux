# Common rules for every handoff (read first)

Work autonomously in the Chaos Redux repo: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`. Follow its `AGENTS.md`. Never ask questions; decide, act, report.

## Sources of truth

- The owner's plan: `docs/plans/chaos_redux_restore_plan_2026-10-12.md`. Each item carries the commits that addressed it.
- Reports from the first two rounds, all in `docs/plans/`: `chaos_redux_text_restore_2026-10-12.md`, `chaos_redux_restore_assets_audio_2026-10-12.md`, `shared_interface_plans/restore_a8_a10_b3_b10_b12_2026-10-12.md`, `biowarfare_restore_comparison_2026-10-12.md`, `chaos_redux_load_camps_repair_2026-10-13.md`, `chaos_redux_restore_c2_c3_2026-10-13.md`, `performance_audit_2026-10-13.md`, `chaos_redux_c6_nonhuman_2026-10-13.md`, `chaos_redux_c9_event_audit_2026-10-13.md`, `chaos_redux_c10_first_incident_2026-10-13.md`, `migration_famine_history_2026-10-13.md`, `cbrn_start_audit_2026-10-13.md`, `interface_restore_audit_2026-10-13.md`, `systems_restore_audit_2026-10-13.md`, `icons_needing_new_art_2026-10-13.md`.

## Rules that override everything

- "Restore" means the EXACT earlier content from git history (`git log -S/-G`, `git show <commit>^:<path>`), byte-exact for binaries (LFS: `git show <commit>:<path> | git lfs smudge > <path>`). Never a rewrite or reinterpretation. Keep only content for genuinely new mechanics and values that were made dynamic.
- The owner's standing direction: "I want everything now restored, fixed and everything that was included in the plan." Earlier rounds left judgement calls untouched; this round resolves them in favour of the earlier state unless that contradicts an explicit owner request in the plan.
- Do not improve, tidy, shorten or re-style anything you restore. Do not redesign anything. Never replace or repoint existing art except to put the original back.
- Localisation stays UTF-8 with BOM. Report events never have more than 4 options. Large numbers in UI text are shortened with k (48.2k). No political power costs on migration or famine decisions.
- No world-wide periodic on_actions without the owner's permission.
- Never add AI attribution to commits. NEVER push. Chaos Redux must not be pushed until the owner says so.
- Other agents may work in this tree at the same time. Commit only your own paths with `.claude/skills/chaos-redux-shared-git-commit` (temporary index, compare-and-swap `update-ref`). Never `git add -A`, reset, stash, or checkout other paths.
- Never touch the Windows game, its settings, or a HOI4 instance you did not launch. Live checks use only the isolated Linux game in WSL (Ubuntu-24.04, `/home/klim/games/hoi4`, launcher `C:/Users/klimp/Videos/chaos_redux_trailer/records/cx/wsl_hoi4_launcher.sh`, shared lock `/tmp/hoi4_wsl.lock`, guide `docs/testing/clausewitz_mcp_linux.md`). Hold the lock only while using the game and restore its settings byte-exactly.
- Write nothing outside the repo except a short entry in `C:/Users/klimp/Videos/chaos_redux_trailer/records/cx/LEDGER.md`.
- When an item is done, append your commit hash to its line in the plan file (edit only your own item lines; re-read before each edit).

## Final report

Short, per item: what was wrong, what was restored from which commit or fixed, your commits, what could not be done and why, what was verified in game and what was not.
