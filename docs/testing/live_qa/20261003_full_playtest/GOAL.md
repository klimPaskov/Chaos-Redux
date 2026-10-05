# Goal: clean, fully implemented, live-tested Chaos Redux (October 2026)

Owner: the orchestrating Claude session started on 2026-10-03. Set from the user's request of 2026-10-03.

## Definition of done

1. The game launches through the debug shortcut and reaches the main menu and a country map with no fresh Chaos Redux error.
2. Every event 1–40 whose rework has started is implemented in full (no simplifications) and live-tested; events whose rework has not started are recorded as not started.
3. Every Chaos Redux system (settings, event logs, chaos meter, clusters, triggerable scenarios, CBRN, camps, special projects, units, super-events, achievements) is live-tested; every triggerable scenario is launched, the fallout scenario last.
4. Every confirmed bug found in live play is fixed and retested, or recorded with its blocker in `bugs.md`.
5. Teaser screenshots of Chaos Redux features are in `docs/content_dump/` with clear descriptions; feature notes are there too (no bugs).
6. `CHAOS_REDUX_MECHANICS.md` uses real screenshots and recordings instead of placeholders and matches the current mod.
7. The rat units' and demonic zombies' animations are fixed.
8. Trailer v3: rewritten script and narration, no event-window screenshots, more moving map footage (diplomacy and political views), unit variety, a death counter past one billion, professional graphics, transitions and sound design, no visual defects.
9. A labelled in-game model showcase video (models, animations, sounds).
10. The repository has no errors and every finished change is committed and pushed.

## Work streams and owners

| Stream | Owner | Status |
|---|---|---|
| Events 006, 012, 016, 021, 023–029, 031–033, 035, 039; CBRN; camps | existing Codex threads (orchestrated) | in progress |
| Startup error gate, live playtest, bug fixing, screenshots | this session | pending |
| Triggerable scenarios showcase (fallout last) | this session | pending |
| Model animation fixes (rats, demonic zombies) | subagent via 3D pipeline skill | pending |
| Model showcase video | this session | pending |
| Trailer v3 | this session | pending |
| Mechanics document update | this session + documentation curator | pending |
| Final cleanup and push | this session | pending |

## Run artifacts

`docs/testing/live_qa/20261003_full_playtest/`: `run_manifest.md`, `test_report.md`, `bugs.md`, `repair_ledger.md`, `coverage.csv`, `setup_commands.md`, `logs/`, `screenshots/`.
Earlier partial runs (2026-09-04, 2026-09-13, 2026-09-28) were removed from the working tree; they remain in git history before this run's cleanup commit.
