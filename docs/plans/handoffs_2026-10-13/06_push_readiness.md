# Handoff 6: push readiness (prepare only, do not push)

Read `00_common_rules.md` in this folder first. Run this last, after handoffs 1 to 5 report.

## Why

The owner: "We cannot push current chaos redux state under any circumstances until things are restored and fixed properly." The local branch is about 2,500 commits ahead of `origin/master`. This handoff gets the repo into a state where the owner can push with one command once they have looked at the game themselves.

## Tasks

1. **Gate check.** Confirm from `live_verification_2026-10-13.md` and `plan_completion_audit_2026-10-13.md`: clean load with no mod-caused error and no localisation collision; main menu correct at 1920x1080 and 2560x1440; `e chaosx_test` spawns every family; every plan item `done`. List anything that fails; do not work around it.
2. **Git LFS.** Only assets the game actually loads belong in LFS. Find large files tracked in git or LFS that the game never loads (source PNGs, contact sheets, Blender files, provider downloads, `.tmp`, `docs/assets` working files) and make sure they are ignored or kept out of LFS going forward. Do not rewrite history. Report the size the push would upload and the LFS storage it would use.
3. **AI attribution.** Scan the unpushed commits (`origin/master..HEAD`) for `Co-Authored-By`, "Generated with" and similar lines. List them. Do not rewrite anything; the owner decides.
4. **Secrets scan** over the unpushed range (keys, tokens, personal paths in committed files). List findings.
5. **Working tree.** List uncommitted changes and untracked files, grouped by owner job where you can tell. Commit only finished, reviewed work that clearly belongs to a completed plan item; leave the rest and list it.
6. **README and docs.** The README keeps its cards (Discord, YouTube, Ko-fi, event catalog, guides, issues) and the video placeholder at the top. Release notes for the next version: write `docs/release_notes_next.md` from the restored and fixed items in plain language, with no mention of agents or internal process.
7. **Do not push.** End with the exact push command the owner would run and the list of anything still blocking it.

## Deliverable

`docs/plans/push_readiness_2026-10-13.md` with the gate table, sizes, findings and the blocking list.
