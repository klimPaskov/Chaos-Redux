# AI probability audit handoff: three retired Mengele import decisions

**Disposition:** Unresolved pending execution of the queued baseline inspect and matched post-change comparison. The owner applied the eligibility-only cutover after receiving the explicit narrower-retry blocker.

Detailed evidence is in [baseline_blocker.md](ai_evidence/mengele_import_retirement_2026-10-03/baseline_blocker.md). Native client and job evidence are retained in `ai_evidence/mengele_import_retirement_2026-10-03/native_task_evidence.json`, `native_task_inspect.log`, and `native_task_inspect_current.log`.

Audited IDs: `import_subjects_from_japanese_china`, `import_subjects_from_india`, and `import_subjects_from_africa` in `common/decisions/germany_mengele_decisions.txt`. Shared helper reviewed: `germany_mengele_import_subjects_from_from_state` in `common/scripted_effects/germany_mengele_effects.txt`; source-state gate: `camp_rework_state_can_accept_responsibility_from_root` at `common/scripted_triggers/camp_repression_rework_triggers.txt:41-46`.

The configured global server is `hoi4-agent-tools` 3.6.0. Direct stdio client initialization and task negotiation through the provided SDK 1.30.0 succeeded; probability inspect advertises optional task support. The corrected frozen-source inspect task is `mod_chaos_redux_ea3b2d67c2c0:job_7feeb5acb54a43fde08ab09950abd625fc7bd5a71590a8af5928c56c2eef60ad`. Its durable job remains `queued`, revision 1, `resultReady=false`, with `updatedAt` unchanged since `2026-10-03T14:32:08.867Z`; a native `tasks/get` query after the 30-minute TTL still returned `working`. The latest `job_inspect` at `2026-10-03 15:03:34 UTC` still found the job queued.

Earlier broad and three-ID narrowed standard inspect calls timed out after 600 seconds. I have not issued evaluate, sweep, compare, or render calls while the required baseline inspect remains queued.

Source review confirms the three before/after `ai_will_do` blocks are byte-identical and use the shared `germany_mengele_decision_ai.silence_dissenting_file` constant, currently `12`. This is static score-only evidence, not an AI selection probability. A valid program scenario additionally needs a post-1943.5.29 date and an operational, GER-controlled state 88 with the state-scoped initialized flag; the retirement cutover uses the separate country-scoped initialized flag. The map-target pools and external state/faction/controller factors remain incomplete; no exact selection chance, dominance, starvation, rank reversal, repetition, or exploit conclusion is supported.

The after decision snapshot SHA-256 is `4425e12b2afe38eb62426095ee30eb765a3e5f02c041f2c1ac40127e4436d33d`. It gates the three decisions on `NOT camp_admin_initialized` in visibility, target-root eligibility, and hidden availability while preserving AI scores and refunding only the native PP cost for stale completions. Both shared import helpers now only zero scratch input, so source review shows no transfer or benefit payload if a stale choice remains available during a state/country flag transition; the source fixtures report net PP change 0. This audit has not established engine-side AI candidate exclusion after initialization.


