# Handoff 12: text restore, deep pass (older than five weeks)

Read `00_common_rules.md` in this folder first. This handoff can run at the same time as all the others.

## Why

The first text restore covered rewrite commits from about September and October 2026 (9,218 values, report in `docs/plans/chaos_redux_text_restore_2026-10-12.md`). The owner said the mod regressed over "more than a year" and asked for texts restored "if they all came recently, in the past several weeks". Older bulk rewrites may exist. This pass finds them and restores only where the older text is clearly the owner's own wording that a bulk sweep later flattened.

## Tasks

1. List every commit from August 2025 to August 2026 that changed the wording of more than 30 existing localisation keys at once without adding the mechanic those keys belong to. Use the commit message, the ratio of changed to added keys, and whether script files changed in the same commit.
2. For each such sweep, compare old and new values. Restore the old value where the sweep made text vaguer, more generic or shorter without a mechanic change. Do NOT restore where the old text described a mechanic that no longer works that way, and do not touch keys already restored in the first pass (its key list is in `docs/plans/chaos_redux_text_restore_2026-10-12_keys.json.gz`).
3. Scripted localisation (`common/scripted_localisation/`) and dynamic text: restore earlier branches that were dropped.
4. Player-facing rules the owner set: no update-history wording ("now", "reworked", "newly added"), no internal terms, numbers shortened with k.
5. Keep the event catalog workbook in step with any restored event, evolution or cluster wording (`chaos-redux-xlsx` skill; run `python .tools/export_event_catalog_csv.py` afterwards).

## Deliverable

Append a "Deep pass" section to `chaos_redux_text_restore_2026-10-12.md`: sweeps found, keys restored per sweep, keys deliberately kept and why, commits.
