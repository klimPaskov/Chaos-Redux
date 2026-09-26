# Publication status update — 2026-09-26

The prior 12-render batch returned `GUI_RENDERED` and verified all 85 fetched artifact hashes, but its source identities are mixed (`7770/e258` before the parent change and `6c3/4c93` after it), including one render whose GUI/script hashes changed during the call. I am preserving those outputs as provenance and do not count them as a consistent current-source matrix.

The canonical MCP checkout is now `d04d7eb51011461b3bb646946805a13bf5c73d2f`, version 3.5.0. The current-source runner is pinned to GUI SHA-256 `6c3a20368b6e2175aa0d2024098288a0bc2a97ec549c90a73058619e99946d33`, scripted-GUI SHA-256 `4c937887e349decd955e632c59bd119873cd1cced761f5995f5b698fee176dc2`, and English UI localisation SHA-256 `4aac46621cd516cdbfa6ed7b45754459a4dc80a8130868bad4e515be859cc445`.

Current call/process: `hoi4.gui_inspect` for `repression_ledger_window` with the 15 declared fixture states at 1920×1080/UI 1.25 is running in Node PID `10968`; its request is saved under `current_source_6c3a2036_4c937887/requests/`, and no inspection result has returned yet. Reference searches/reads, including installed scripted-GUI documentation and the source lookup, have completed in that run. Runtime state and artifact storage are in its task-owned OS temp directory.

Outstanding before handoff: finish that current-source inspection, capture the normal/hover/disabled/edge and click-region matrix at all three requested scales on the pinned files, review the related fixture images and bounds, and record the active picker hit region. The parent’s twelve primary-crop review is useful corroboration but does not replace these checks.

Known evidence limits: no numeric controller state is stated for the selected-location fixtures, so their site work/purpose controls remain disabled in the render and I will not invent a `controls` field; the GUI render route does not draw native `pdx_tooltip` popups, and no engine click-execution tool is exposed. These remain unproved capabilities, not successful acceptance cases. No gameplay or GUI source edits were made.
