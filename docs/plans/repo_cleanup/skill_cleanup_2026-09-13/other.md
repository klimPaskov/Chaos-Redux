# Other skill cleanup handoff — 2026-09-13

Disposition: `implemented` for the bounded documentation cleanup, pending parent review.
Acceptance basis: the parent's explicit assignment carries the user's request for slightly more concise, logically organized, internally consistent skills with all requirements, conditions, exceptions, examples, explanations, dependencies, steps, strength, scope, and order preserved.
This handoff does not establish approval for production work described by a skill.
No child agents were spawned and no commit was made.

## Ownership and reading inventory

Only the seven assigned `.agents/skills/<name>/SKILL.md` files and this handoff were edited.
Originals were read from `C:/Users/klimp/.codex/tmp/chaos-redux-skill-cleanup-20260913/original/.agents/skills/`, which includes the user's existing changes.
Every original and current assigned file was read completely before further edits, using bounded reads and recovering truncated aggregate attempts through narrower rereads.
Original line counts were comfyui 16, debug-playtest 674, mtth 66, state-ledgers 97, xlsx 326, scripted-gui 122, and frame-animation 499.
The existing partly applied GUI/frame restructuring was reviewed and retained; it was not treated as the original source.
`AGENTS.md`, the complete `chaos-redux-subagents` skill, and the complete official `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md` were read.
The official skill informed the cleanup without overriding the user's preservation requirement or imposing a new template.

Offline references consulted: all eleven required core snapshot pages, plus Interface modding, Scripted GUI modding, Graphical asset modding, and Character modding.
Relevant body excerpts were inspected for scope, variables, MTTH, effect/trigger syntax, modifiers, localisation, on-actions, event/decision/idea structures, GUI layering, and portrait consumers.
Installed vanilla references consulted: `documentation/script_concept_documentation.md` (Script Constants and related concepts), `common/script_constants/documentation.md`, `documentation/effects_documentation.md` (state/country manpower and event-target saving), `documentation/triggers_documentation.md` (`check_variable`), `documentation/dynamic_variables_documentation.md` (`state_population_k`), `common/map_modes/documentation.md`, `common/scripted_guis/_documentation.md`, and localisation-object/modifier documentation excerpts.
Vanilla precedents inspected: `common/mtth/mtth_variables.txt`, `interface/alerts.gfx` (`frameAnimatedSpriteType`), and `interface/sov_paranoia_system_scripted_gui.gui`.
The event-assets portrait mode/state and generation-workflow passages were inspected to align the portrait correction with the disjoint asset worker.
These were reference consultations for instruction meaning; no engine-facing implementation was changed.
No Paradox web page, game launch, live QA, RunPod operation, asset production, paid operation, spreadsheet, runtime wiring, configuration, or helper implementation was performed.

## Per-file dispositions and changes

- `chaos-redux-comfyui`: `implemented`; split grounded step 3 into source-placeholder, optional styled-final, and RunPod/pending-token subitems while retaining steps 1–5 and their order.
- `chaos-redux-debug-playtest`: `implemented`; added phase groups for preconditions, launch/repair, setup/artifacts, smoke/catalog planning, feature protocols, defect routing/acceptance, and coverage/completion.
Original numbered sections 1–30 and all their prose, list entries, defaults, commands, and examples remain in their original order.
Dense triage paragraphs have distinct subordinate headings for script-constant schemas, variable comparisons, temporary-variable cleanup, runtime country templates, and patch attribution.
- `chaos-redux-mtth`: `implemented`; added Markdown separation before reference, notes, and typical-usage lists.
All definitions, examples, AI-weight pattern, and probability scenario contract are unchanged.
- `chaos-redux-state-ledgers`: `implemented`; moved the complete scope and temporary-variable section before the exact-transfer section, so scope prerequisites precede the transfer sequence.
Every transfer step remains in its original sequence and every later section is unchanged.
- `xlsx`: `implemented`; placed the existing main title and overview first, nested all output requirements under one section, renamed Important Requirements to Formula recalculation prerequisite, and made Excel File Workflows a populated parent.
Moved the complete formula-policy section with both unchanged examples before the pandas read/write example.
The common workflow, catalog export contract, new/edit examples, recalculation instructions and limitation, verification checklist, best practices, and code-style rules retain their order.
Added missing Markdown separators before lists/fences.
- `chaos-redux-scripted-gui`: `implemented`; retained the prior added MCP subsection boundaries and promoted visual/usability review to its own peer section, with its existing checklist subsections one level below it.
All prose, tables, five-step MCP sequence, optional-rewrite failure handling, scenario/assertion contract, visible-defect gates, and handoff requirements remain unchanged.
- `chaos-redux-frame-animation`: `implemented`; retained the added title and prior movement of use scope, related skills, and required references before production guidance.
Original sections 5/3/4/1/2 are revised sections 1/2/3/4/5; original 6–11 remain 6–11; original naming 13 is revised 12 and original output package 12 is revised 13; original 14–18 remain 14–18.
Every source-frame restriction, mockup exception, Sunburst-only rule with unavailable-selector qualification, transparency fallback, example, deliverable, overlay procedure, quality gate, and blocker remains unchanged.

No cross-file repetition was removed.
No requirement was replaced with a reference whose loading is uncertain, and no genuine prose duplicate was merged away in this group.
Structural heading additions do not add workflow requirements.
The numbered debug sections retain their numbers; frame-animation's moved numbered sections are renumbered consistently.

## Evidenced correction

Comfyui original step 3 said `No HOI4 repaint is required.` without distinguishing source preparation from final completion.
Revised step 3 confines that statement to source-placeholder preparation and says the wired sourced portrait remains explicitly pending until the user supplies its HOI4-style replacement.
Authority: `AGENTS.md` §4.17 explicitly states that a wired sourced portrait remains an explicitly pending source placeholder until that replacement is supplied.
The corrected wording preserves unchanged source/crop/resize/wiring identity, optional `styled_final` invocation only after an explicit user request, user-operated RunPod, worker validation/installation, workflow/provider/job/hash/review evidence, the queued-job/preview exclusion, and the RunPod prohibition.
`replacement_pending` remains limited to an outstanding explicit styled-final request; general source-placeholder pending status is distinct from that request-dependent token.
This agrees with the asset worker's selected-mode/state correction and does not authorize starting the optional branch.

## Unresolved dependencies and scope distinctions

`chaos-redux-debug-playtest` §4 requires `.agents/skills/hoi4-autonomous-debug-playtest/SKILL.md`, or its packaged generic copy.
Neither the named repository path nor a matching packaged `SKILL.md` was found by file inventory under repository `.agents/skills`, `C:/Users/klimp/.codex/skills`, `C:/Users/klimp/.agents/skills`, and `C:/Users/klimp/.codex/plugins/cache`.
Disposition: `unresolved`; retain the required reference.
Decision/input needed: the actual generic package location or an explicit decision about that dependency; no substitute path or replacement instructions were invented.
The special debug skill's explicit opt-in desktop/log/relaunch workflow is preserved as a distinct authorized invocation scope, without integrating it into ordinary coding/completion routes or treating differing opt-in gates as a contradiction.

Generated `.qoder/repowiki` documents contain line-range links into debug/frame skills.
These are generated line citations outside ownership, not maintained heading anchors inside the skill contract; relocation can make their ranges stale.
They were not edited or represented as current section evidence.
Maintained conventional skill links and relevant incoming GUI heading anchors were checked; the GUI content-budget, reference, MCP review, usability, background, click-region, and handoff anchor titles remain intact.
The event-assets `generate-and-refine-source-art` destination remains present.
Paths, commands, ids, values, frontmatter, and inline technical literals were retained; the generic dependency remains the reported gap.

## Preservation and validation evidence

A detail-by-detail comparison checked every original nonblank nonheading line as an occurrence against the revision, including repeated occurrences.
Six files retain every such line exactly, independent of relocation or added blank lines/headings.
Comfyui has exactly one changed original line: its grounded step 3, whose complete requirement mapping and narrow correction are documented above.
All original inline technical literals remain present in every file.
Original frontmatter bytes and every fenced example's exact bytes are preserved, treating moved fence blocks as a multiset rather than requiring their original location.
This caught unintended newline normalization in debug and GUI metadata and was corrected before handoff.
The GUI original has mixed prose line endings; its metadata remains byte-exact and prose newline differences do not change the instruction text.
No code block, command, numeric example, template snippet, or required technical literal was rewritten.
The official quick validator passed all seven skills.
Its first default-Windows-encoding run failed to decode the state-ledger and XLSX Unicode text; both passed when rerun with Python UTF-8 mode, without modifying the validator or dropping characters.
No behavior/production forward test or MCP engine-surface test was run because this assignment changes instruction organization only and explicitly excludes production/runtime work.
Parent review remains responsible for semantic acceptance, cross-group reconciliation, and the final commit.

## Original-passage location map

The table maps every original section start to its revised section start; the preservation comparison above covers each individual nonheading line inside those passages, rather than substituting a section-level summary for detail preservation.
Subheading boundaries added inside debug triage do not truncate the original triage paragraphs.
All line numbers refer to the original snapshot and the current handoff-time files.

| Skill | Original section and line | Revised line |
| --- | --- | --- |
| chaos-redux-comfyui | 6 — Chaos Redux portrait production | 6 |
| chaos-redux-debug-playtest | 6 — Chaos Redux Autonomous Debug Playtest | 6 |
| chaos-redux-debug-playtest | 12 — Capability gate | 14 |
| chaos-redux-debug-playtest | 27 — Default Chaos Redux configuration | 29 |
| chaos-redux-debug-playtest | 46 — Invocation scope | 48 |
| chaos-redux-debug-playtest | 66 — Mandatory project reading before a run | 68 |
| chaos-redux-debug-playtest | 91 — Repository boundary | 93 |
| chaos-redux-debug-playtest | 112 — Launch and clean-start gate | 116 |
| chaos-redux-debug-playtest | 135 — Chaos Redux error triage | 139 |
| chaos-redux-debug-playtest | 171 — Repair loop | 185 |
| chaos-redux-debug-playtest | 192 — Test-country rule | 208 |
| chaos-redux-debug-playtest | 210 — Deterministic setup policy | 226 |
| chaos-redux-debug-playtest | 226 — Dedicated test artifacts | 242 |
| chaos-redux-debug-playtest | 254 — Chaos Redux smoke test | 272 |
| chaos-redux-debug-playtest | 275 — Event-catalog coverage | 293 |
| chaos-redux-debug-playtest | 304 — Status handling | 322 |
| chaos-redux-debug-playtest | 316 — Event test protocol | 336 |
| chaos-redux-debug-playtest | 337 — Evolution test protocol | 357 |
| chaos-redux-debug-playtest | 355 — Cluster test protocol | 375 |
| chaos-redux-debug-playtest | 375 — Triggerable scenario test protocol | 395 |
| chaos-redux-debug-playtest | 398 — Event Logs and Event Details visual audit | 418 |
| chaos-redux-debug-playtest | 423 — Chaos Meter visual and gameplay audit | 443 |
| chaos-redux-debug-playtest | 447 — Decisions, missions, and scripted GUI | 467 |
| chaos-redux-debug-playtest | 465 — Focus-tree live audit | 485 |
| chaos-redux-debug-playtest | 481 — Country-package live audit | 501 |
| chaos-redux-debug-playtest | 499 — Super-event live audit | 519 |
| chaos-redux-debug-playtest | 516 — Asset and animation live audit | 536 |
| chaos-redux-debug-playtest | 543 — AI and time-progression pass | 563 |
| chaos-redux-debug-playtest | 563 — Defect ownership and routing | 585 |
| chaos-redux-debug-playtest | 584 — Fix acceptance | 606 |
| chaos-redux-debug-playtest | 601 — Full-catalog coverage ledger | 625 |
| chaos-redux-debug-playtest | 622 — Completion standard | 646 |
| chaos-redux-debug-playtest | 642 — Final report | 666 |
| chaos-redux-mtth | 6 — Chaos Redux MTTH Variables | 6 |
| chaos-redux-mtth | 8 — Scope and References | 8 |
| chaos-redux-mtth | 15 — Defining an MTTH entry | 16 |
| chaos-redux-mtth | 38 — Using an MTTH entry | 40 |
| chaos-redux-mtth | 50 — AI weights with MTTH | 53 |
| chaos-redux-mtth | 64 — Scenario analysis | 67 |
| chaos-redux-state-ledgers | 6 — Chaos Redux State Ledgers | 6 |
| chaos-redux-state-ledgers | 10 — Source contract | 10 |
| chaos-redux-state-ledgers | 16 — Exact transfer contract | 24 |
| chaos-redux-state-ledgers | 31 — Scope and temporary-variable rules | 16 |
| chaos-redux-state-ledgers | 39 — Sparse aligned cohort registry | 39 |
| chaos-redux-state-ledgers | 54 — Reception and outcome accounting | 54 |
| chaos-redux-state-ledgers | 62 — Transaction-time map projections | 62 |
| chaos-redux-state-ledgers | 72 — No-double-counting proof | 72 |
| chaos-redux-state-ledgers | 84 — Validation and handoff | 84 |
| xlsx | 6 — Requirements for Outputs | 12 |
| xlsx | 8 — All Excel files | 14 |
| xlsx | 10 — Zero Formula Errors | 16 |
| xlsx | 14 — Preserve Existing Templates (when updating templates) | 20 |
| xlsx | 20 — Financial models | 26 |
| xlsx | 22 — Color Coding Standards | 28 |
| xlsx | 26 — Industry-Standard Color Conventions | 32 |
| xlsx | 34 — Number Formatting Standards | 40 |
| xlsx | 36 — Required Format Rules | 42 |
| xlsx | 45 — Formula Construction Rules | 51 |
| xlsx | 47 — Assumptions Placement | 53 |
| xlsx | 53 — Formula Error Prevention | 59 |
| xlsx | 61 — Documentation Requirements for Hardcodes | 67 |
| xlsx | 70 — XLSX creation, editing, and analysis | 6 |
| xlsx | 72 — Overview | 8 |
| xlsx | 76 — Important Requirements | 76 |
| xlsx | 80 — Reading and analyzing data | 117 |
| xlsx | 82 — Data analysis with pandas | 119 |
| xlsx | 102 — Excel File Workflows | 80 |
| xlsx | 104 — CRITICAL: Use Formulas, Not Hardcoded Values | 82 |
| xlsx | 108 — ❌ WRONG - Hardcoding Calculated Values | 86 |
| xlsx | 124 — ✅ CORRECT - Using Excel Formulas | 102 |
| xlsx | 139 — Common Workflow | 139 |
| xlsx | 159 — Chaos Redux event catalog export contract | 159 |
| xlsx | 175 — Creating new Excel files | 175 |
| xlsx | 204 — Editing existing Excel files | 204 |
| xlsx | 231 — Recalculating formulas | 231 |
| xlsx | 253 — Formula Verification Checklist | 255 |
| xlsx | 257 — Essential Verification | 259 |
| xlsx | 263 — Common Pitfalls | 265 |
| xlsx | 272 — Formula Testing Strategy | 274 |
| xlsx | 278 — Interpreting recalc.py Output | 280 |
| xlsx | 295 — Best Practices | 298 |
| xlsx | 297 — Library Selection | 300 |
| xlsx | 302 — Working with openpyxl | 305 |
| xlsx | 310 — Working with pandas | 313 |
| xlsx | 316 — Code Style Guidelines | 319 |
| chaos-redux-scripted-gui | 6 — Chaos Redux Scripted GUI | 6 |
| chaos-redux-scripted-gui | 12 — Scope and source reading | 12 |
| chaos-redux-scripted-gui | 18 — Reference image before implementation | 18 |
| chaos-redux-scripted-gui | 34 — Content and interaction budget | 34 |
| chaos-redux-scripted-gui | 42 — Required MCP visual review and optional rewrite | 42 |
| chaos-redux-scripted-gui | 62 — Scripted GUI visual and usability review | 70 |
| chaos-redux-scripted-gui | 66 — Geometry, typography, and control bounds | 74 |
| chaos-redux-scripted-gui | 83 — Background and reference coverage | 91 |
| chaos-redux-scripted-gui | 94 — Click regions, overlap, and state behavior | 102 |
| chaos-redux-scripted-gui | 106 — Scenario coverage and evidence | 114 |
| chaos-redux-scripted-gui | 114 — Usability and integration | 122 |
| chaos-redux-scripted-gui | 120 — Handoff and completion | 128 |
| chaos-redux-frame-animation | 6 — Core rule | 58 |
| chaos-redux-frame-animation | 30 — HOI4 animation model | 82 |
| chaos-redux-frame-animation | 49 — Relationship with other skills | 21 |
| chaos-redux-frame-animation | 67 — Required HOI4 references before wiring | 39 |
| chaos-redux-frame-animation | 86 — When to use this skill | 8 |
| chaos-redux-frame-animation | 99 — What counts as a real source frame | 101 |
| chaos-redux-frame-animation | 121 — Required animation brief | 123 |
| chaos-redux-frame-animation | 147 — Frame plan | 149 |
| chaos-redux-frame-animation | 166 — Generation rules | 168 |
| chaos-redux-frame-animation | 185 — Deterministic processing rules | 187 |
| chaos-redux-frame-animation | 207 — HOI4 sheet construction | 209 |
| chaos-redux-frame-animation | 232 — Required output package | 274 |
| chaos-redux-frame-animation | 267 — Naming rules | 234 |
| chaos-redux-frame-animation | 307 — `.gfx` handoff pattern | 309 |
| chaos-redux-frame-animation | 339 — HOI4 wiring handoff | 341 |
| chaos-redux-frame-animation | 366 — Leader portrait overlay animations | 368 |
| chaos-redux-frame-animation | 456 — Quality gates | 458 |
| chaos-redux-frame-animation | 485 — Blockers | 487 |
