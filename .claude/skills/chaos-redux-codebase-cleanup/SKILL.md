---
name: chaos-redux-codebase-cleanup
description: Use when removing dead code, merging duplicated helpers, or verifying reference integrity across the whole Chaos Redux repository or one subsystem (scripted effects and triggers, scripted localisation, constants, ideas, modifiers, events, flags, localisation keys, GFX).
---

# Codebase Cleanup

Use this workflow for repository-wide or subsystem-wide dead-code, duplication, and reference-integrity cleanup. Follow `AGENTS.md` for completion, simplification reporting, and commit rules. Cleanup must not change gameplay unless the change is a reported, justified bug fix.

## 1. Entry point and audits

Run from the mod root, writing outputs to a task folder under ignored `.tmp/`:

```
python .tools/audit_script_references_static.py --json .tmp/<task>/script_reference_audit.json
```

It compares definitions against references for scripted effects, scripted triggers, scripted localisation, constant categories, ideas, dynamic and opinion modifiers, and events. It splits `dead` from `dynamic` candidates (names matching a `prefix_[`, `prefix_@`, or `prefix_$` builder, or an event-id `ns.[` stem), lists flags that are checked but never set and set but never checked, and groups exact and parametric clones. Read the tool docstring and `.tools/README.md` before relying on a column.

Companion audits: `.tools/audit_localisation_static.py` (missing or unbound keys, unlocalised requirement flags) and `.tools/audit_asset_wiring_static.py` (GFX wiring). A candidate list is a worklist, not a deletion list.
`python -B .tools/check.py full --json .tmp/<task>/check.json` runs every audit at once; its `review` findings are the candidate worklist, and its `error` findings must stay at zero after each removal. Rerun `check.py quick` on each subsystem's changed files before its commit.

## 2. False-positive patterns

Treat a candidate as live until these are ruled out.

- Meta-effect name builders: `[NAME]_<suffix>` where NAME comes from `[?token_var.GetTokenKey]`; registry provider hooks such as `<registry>_provider_[PROVIDER]_<hook>`; per-tag families such as `<system>_[TAG]_<action>`; batch dispatchers `..._batch_[BATCH_ID]`; extension dispatch `[EXTENSION_EFFECT]_apply`.
- Events fired by built ids (`<namespace>.[EVENT_ID]` inside a `meta_effect`), self-firing MTTH events, root and checkpoint events.
- Generated registries and catalogs (headers say generated or do not hand-edit), such as per-state registry triggers or province catalogs: keep and report; change the generator instead if needed.
- Trigger names that double as player-visible tooltip localisation keys: never merge or rename those clones.
- GFX: the asset audit does not model implicit engine naming (`GFX_idea_<id>`, focus icon plus `_shine`, decision and category icons, `£texticon` in localisation, sub-unit icons and counters, achievements, technologies). Never bulk-delete "dead" sprites.
- Localisation keys used by vanilla-override files are usually defined in vanilla localisation: check vanilla before calling them missing. `tech_effect|x` pipe syntax and commented examples are not keys.
- Keep: constant categories that are the single source for hand-mirrored `@` macros, documented APIs, CXT test-country setup hooks, save-compatibility stubs, debug helpers, and documented future hooks.

## 3. Verification before removal

1. Search the exact name across `common/`, `events/`, `interface/`, `localisation/`, `history/`, `map/`, `gfx/`, `docs/`, `.claude/skills/`, `.tools/`, and the spreadsheet CSV exports.
2. Trace every dynamic builder that could assemble the name, including its variable values and scripted localisation.
3. Check `git log -S<name>` to tell a lost-wiring regression from never-wired code.
4. Assign one disposition per candidate:
   - `remove`: strong evidence of no live reference.
   - `keep-unwired-intended`: the feature looks designed but is not wired. Report for a design decision; never wire it silently, since that changes behaviour.
   - `keep-dynamic`, `keep-generated`, `keep-dirty-file` (someone else's uncommitted changes), `keep-uncertain`.

## 4. Consolidation rules

- Replace byte-identical per-tag or per-package copies with one shared helper driven by scope or temp variables, and rewire every caller.
- Scripted effects take no parameter blocks; pass inputs through scope or temp variables.
- Keep a thin one-line wrapper only where a caller cannot be edited (dirty file) or the name is a dispatch contract.
- Do not merge clones whose names are tooltip keys. Leave two-member short clones when separate copies read more clearly.
- Document every shared helper in the owning subsystem's `.md` (for dynamic effects, `common/scripted_effects/chaosx_dynamic_effects.md`).

## 5. Flag triage (checked but never set)

- Bug: the setter was lost or the flag was renamed or mistyped. Fix and report as a behaviour change.
- Dead guard: an always-true `NOT` or always-false branch. Safe to remove.
- Vanilla-set flag: set by the engine or vanilla scripts. Keep.
- Fail-closed admission gate: intentionally blocks until something sets it. Keep.
- Unwired feature: report for a design decision.

## 6. Orchestration

- Split work by disjoint subsystem file sets. Give each subagent one shared written brief (rules, hard file boundaries, handoff format) plus its own candidate file.
- Run at most 3 heavy subagents concurrently. Many parallel agents each loading the full tree (about 1.9M lines) have exhausted memory and ended the parent session.
- Forbid whole-repository pickles or other multi-gigabyte caches, and forbid `taskkill /IM python.exe`, which kills other sessions' processes.
- Have each agent append progress to its handoff after every group so a restart loses nothing.
- Record a baseline `git status --porcelain` snapshot at the start. Files with someone else's uncommitted changes are reported, not edited.

## 7. Committing

Review each subsystem's handoff, re-grep removed names (expect zero live references), run the brace and BOM check, and run any touched `.tools/tests/test_*`. Then commit one subsystem per commit with `chaos-redux-shared-git-commit` (temporary index, fully owned paths only). Add no AI attribution lines.

## 8. Windows pitfalls

Bash heredocs collapse backslash escapes, so write Python scripts to files rather than inlining them. Preserve the BOM (localisation only) and each file's original line endings when rewriting.

## 9. Reporting checklist

Files changed; systems inspected; helpers created or updated; duplication removed; dead code removed; dead code kept with reason; behaviour changes; docs and localisation updates; validation performed; skills used, created, or updated; remaining risks; design decisions needed.
