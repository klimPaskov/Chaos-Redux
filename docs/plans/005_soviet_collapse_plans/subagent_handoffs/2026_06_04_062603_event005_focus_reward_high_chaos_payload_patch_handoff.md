# Event005 Soviet Collapse Focus Reward Audit Handoff

Date: 2026-06-04 06:26 UTC

## Scope

Focused current-state audit and bounded patch pass for Soviet Collapse focus-tree reward spam, duplicate idea/reward chains, shallow focus rewards disconnected from existing mechanics, and pathline-prone layouts.

No flag files, visual flag assets, `.tga` files, flag `.gfx` files, or flag sprites were touched.

## Required References Used

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- Core offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding
- Vanilla docs inspected for script behavior: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`, `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_062603_event005_focus_reward_high_chaos_payload_patch_handoff.md`

## Files Audited Without Direct Edits

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No decisions or localisation were changed, so the decisions skill was not needed for this patch.

## Patch Summary

The clearest remaining high-signal issue was helper-level reward duplication in high-chaos successor focus rewards.

Before this patch, `soviet_collapse_apply_high_chaos_focus_escalation_payload` and `soviet_collapse_apply_focus_high_chaos_identity` used `soviet_collapse_high_chaos_focus_payload_applied` as a temp-variable guard. Temp variables do not persist between separate focus completion reward executions, so separate high-chaos focuses could repeatedly re-run the same visible reward chain. Several inline chaos helpers also called `soviet_collapse_apply_high_chaos_focus_identity_payload` directly, which left the identity subpayload open to repeated grants.

Changed helpers:

- `soviet_collapse_apply_high_chaos_focus_escalation_payload`
  - Now delegates directly to `soviet_collapse_apply_high_chaos_focus_payload`.
- `soviet_collapse_apply_high_chaos_focus_payload`
  - Now gates the shared high-chaos focus reward package behind persistent country flag `soviet_collapse_high_chaos_focus_payload_granted`.
  - Still requires `soviet_collapse_high_chaos_successor`.
  - Preserves existing assault-column, expansion-claim, conflict-plan, identity-payload, and AI-strategy rewards, but makes the shared package one-time per country.
- `soviet_collapse_apply_high_chaos_focus_identity_payload`
  - Now gates the identity subpayload behind persistent country flag `soviet_collapse_high_chaos_focus_identity_payload_granted`.
  - This also protects direct callers that do not go through the shared escalation payload.
- `soviet_collapse_apply_focus_high_chaos_identity`
  - Removed the ineffective temp-variable gate and delegates to the shared persistent-guarded payload.

## Validation

Commands run:

- Brace balance on `common/scripted_effects/005_soviet_collapse_effects.txt`
  - Result: `final_depth=0 min_depth=0`
- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt`
  - Result: clean
- `git diff --check --no-index /dev/null docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_062603_event005_focus_reward_high_chaos_payload_patch_handoff.md`
  - Result: no whitespace errors in the new handoff file
- Unsupported comparison-operator scan on the touched script and handoff files
  - Result: no matches
- `git diff --name-only | rg '(^|/)gfx/flags/|\.tga$|flag.*\.(gfx|dds|tga)$|(^|/)flags/' || true`
  - Result: no output; no flag files in the diff

## Remaining Gaps

- No direct focus layout edits were made in this pass. The strongest evidence found was reward-chain duplication in shared helpers, so the patch stayed there.
- Some high-chaos inline helper blocks still have duplicated local wrapper structure and rough indentation. Their direct identity payload calls are now protected by the new persistent identity guard, but a broader cleanup could route more of them through the shared payload in a later focused refactor.
- No new focus rewards, decisions, localisation, or icons were added.

## Simplifications, Omissions, and Blockers

No fallbacks were used and no flag work was performed.

This handoff intentionally records a bounded helper-only fix. The worktree already contained broad pre-existing modifications across Event005 and Event006 files, including the touched scripted effects file, so no commit was created from this subagent pass.
