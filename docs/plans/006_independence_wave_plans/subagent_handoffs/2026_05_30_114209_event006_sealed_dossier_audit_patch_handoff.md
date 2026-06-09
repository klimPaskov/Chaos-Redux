# Event 006 Sealed Dossier Decision Audit and Patch Handoff

## Scope

Bounded audit of `independence_wave_sealed_dossier_category`, its gates, four decisions, five scripted effects, constants, localisation, and Event 006 documentation. This pass did not edit flag assets, `gfx/flags`, `common/countries`, `history/countries`, Event 005 files, country packages, super-events, scripted GUI, or world-end hooks.

## Changed Files

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_114209_event006_sealed_dossier_audit_patch_handoff.md`

## Changed Identifiers

- `can_independence_wave_open_sealed_dossier`
- `independence_wave_open_sealed_archive_audit`
- `independence_wave_conduct_quiet_dead_census`
- `independence_wave_convene_unmarked_congress`
- `independence_wave_seal_impossible_registry`

## Findings Sorted by Severity

1. Medium: completed one-shot decisions could reappear as dead grey buttons after their timer because HOI4 decisions re-enable by default unless blocked by `fire_only_once` or visibility. This affected the audit and census decisions most clearly, and could leave clutter if later cleanup ever cleared route-closing flags.
2. Medium: the strange/occult gate accepted `independence_wave_package_strange_candidate` but not the matching `independence_wave_package_type = strange_package` variable. Other Event 006 AI logic already treats both as valid strange-package identity, so this gate was slightly too narrow for variable-only package state.
3. Low: the category intentionally opens for either a strange package or high occult pressure. This is broad enough to let a non-strange high-pressure release enter the first-pass dossier path, but that matches the documented first-pass "strange or occult-pressure" behavior. Full strange packages are still not claimed.
4. Low: all four decisions use political power as the primary cost. The effects are one-shot and not farmable after the patch, but future deeper strange packages should move some costs toward stability, command power, equipment, manpower, legitimacy, containment timers, or map objectives.

## Category Lifecycle Notes

`independence_wave_sealed_dossier_category` is visible only through `can_independence_wave_open_sealed_dossier`, which requires an independent Event 006 release and closes after either `independence_wave_sealed_registry_closed` or `independence_wave_unmarked_congress_convened`. The audit decision opens the archive and keeps the category alive through `independence_wave_sealed_archive_audited`; the reveal and containment decisions are mutually exclusive through both shared gate closure and direct decision visibility checks.

Patch behavior:

- Before: one-shot decisions relied only on state flags in `available`, so completed buttons could reappear unavailable after decision re-enable.
- After: the four decisions are `fire_only_once = yes`, and each decision visibility excludes its completed or mutually exclusive state.
- Before: variable-only strange package state did not open this category.
- After: `can_independence_wave_open_sealed_dossier` accepts either the strange package flag or `independence_wave_package_type = strange_package`; AI weighting for the strange/containment choices mirrors the same two-signal check.

## Mission Quality Notes

No timed mission is present in this tranche. The audited surface consists of four clickable decisions owned by Event 006 releases in `independence_wave_sealed_dossier_category`. Requirement progression is audit -> optional census -> reveal or containment. There is no duration-based success/failure mission, so duplicate-risk is limited to decision re-enable; this was patched with `fire_only_once` and completed-state visibility.

## Cost and Requirement Clarity Notes

Requirement localisation exists for the category and all four decisions. The custom trigger tooltips avoid exposing raw scripted triggers. The Unmarked Congress remains visible after the audit even when occult pressure is below the reveal gate, which is useful because the player sees the high-pressure requirement instead of losing the route clue. Costs are plain political power costs via script constants; acceptable for first-pass bureaucracy, but deeper strange follow-up should not stay PP-only.

## AI Validity and Route-Lock Notes

AI weights are bounded to release-country decisions and do not target dead countries or states. The patch aligned AI strange-package weighting with both accepted package signals. There are no targeted decisions, route arrays, closed borders, or world-route locks in this sealed dossier surface.

## Localisation and Tooltip Gaps

No missing localisation was found for:

- `independence_wave_sealed_dossier_category`
- `independence_wave_sealed_dossier_category_desc`
- all four decision names and descriptions
- all four custom requirement tooltip keys

Localisation file `localisation/english/006_independence_wave_l_english.yml` has UTF-8 BOM.

## Cleanup and Exploit-Risk Notes

The reveal and containment routes are mutually exclusive. The category closes after either final choice. The one-shot audit, census, reveal, and containment buttons now have both one-shot decision behavior and visibility cleanup. The quiet census still grants manpower once, but cannot be farmed through normal re-enable behavior after the patch.

## Remaining Issues and Recommended Fixes

- Future strange-package work should add a real containment mission with owner `Event 006 release`, category `independence_wave_sealed_dossier_category`, region `release-controlled core/anchor state`, requirement `hold occult pressure below the configured gate while remaining independent`, duration `45-120 days through constants`, success `containment recovery`, failure `reveal/escalation`, duplicate risk `one active containment review per country`.
- Future deeper package work should add non-PP costs and consequences for the census/reveal/containment branch.
- This tranche still does not implement strange country packages, strange focus modules, strange achievements, super-events, assets, country files, or world-threat hooks. That is correctly documented as a remaining first-pass limitation.

## Validation Run

- Bounded brace balance passed with balance `0` for:
  - `common/decisions/categories/006_independence_wave_categories.txt`
  - `common/decisions/006_independence_wave_decisions.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
- Unsupported operator scan found no `<=` or `>=` in the bounded Event 006 decision, trigger, effect, constant, localisation, or doc files.
- Localisation BOM check returned `efbbbf` for `localisation/english/006_independence_wave_l_english.yml`.
- Localisation coverage check found all sealed dossier category, decision, description, and requirement tooltip keys.
- Forbidden-path audit: this patch touched only the two Event 006 script files above and this handoff. The worktree already had pre-existing Event 005 modified paths, but this audit did not edit them.

## Skipped Validation

- No live in-game UI validation was run from this subagent environment.
- No broad Event 006 validation was run outside the bounded sealed dossier category, because the task scope was decision/category audit only.

## Plan Handoff Path

No broad expansion plan was written. This handoff is the required patch/audit handoff.
