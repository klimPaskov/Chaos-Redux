# Portrait skill source-placeholder and styled-final mode reconciliation

Date: 2026-08-06

Status: reusable portrait guidance reconciled; no gameplay, character, runtime asset, `.gfx`, localisation, GUI, or spreadsheet file was changed by this handoff.

## Scope

Updated only `.agents/skills/chaos-redux-event-assets/SKILL.md` and `.agents/skills/chaos-redux-comfyui/SKILL.md` in the skill-policy tranche, while preserving unrelated in-progress edits already present in the shared worktree.

## Reusable policy

Grounded or historical portraits select an explicit mode in the brief or manifest.

- `source_placeholder` preserves the unchanged attributed source, exact decoded-pixel head-and-shoulders crop, deterministic `156x210` fit, identity, and DDS/runtime wiring, and does not wait for an HOI4 repaint.
- Provider-backed `styled_final` is a separate optional branch that starts only after the user explicitly requests a styled final; the user runs the locked provider workflow and supplies the output, and `chaosx_portrait_creator` validates and installs it at the same runtime path.
- `replacement_pending` is used only when that explicit styled-final request remains outstanding, never as an automatic state for every grounded source placeholder.
- Fictional high-chaos or impossible portraits continue to use native ImageGen and never use the grounded source branch.
- Advisor, theorist, high-command, officer-corps, dossier-card, and other small-portrait families remain authorization-bounded and are not inferred from character or portrait consumers.

## Changed skill sections and line anchors

- `chaos-redux-event-assets/SKILL.md:149` defines the explicit grounded `source_placeholder` mode and the optional provider-backed `styled_final` branch.
- `chaos-redux-event-assets/SKILL.md:270` makes the durable prompt package conditional on the optional styled-final branch instead of requiring it for every grounded source.
- `chaos-redux-event-assets/SKILL.md:282` prevents automatic `replacement_pending` status and keeps source-only identity review distinct from styled-final review.
- `chaos-redux-event-assets/SKILL.md:597-601` makes manifest fields and portrait states conditional and defines `source_placeholder`, `replacement_pending`, and `styled_final` semantics.
- `chaos-redux-event-assets/SKILL.md:1112-1129` documents source-placeholder crop/resize/DDS wiring and the user-triggered provider replacement path.
- `chaos-redux-event-assets/SKILL.md:1140-1161` separates source-placeholder evidence from optional provider output and preserves the no-advisor-icons boundary.
- `chaos-redux-event-assets/SKILL.md:1512` updates the completion checklist so a selected source placeholder does not require a user-run provider result.
- `chaos-redux-comfyui/SKILL.md:3,12` names explicit source-placeholder mode, optional provider-backed styled final, native ImageGen for fictional high-chaos subjects, and the conditional `replacement_pending` state.

## Validation

- Read `AGENTS.md`, the offline Paradox Wiki core pages, installed vanilla documentation, the skill-creator guidance, and both target skills before editing.
- Ran `python -B C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-event-assets`.
- Ran `python -B C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-comfyui`.
- Ran `git diff --check -- .agents/skills/chaos-redux-event-assets/SKILL.md .agents/skills/chaos-redux-comfyui/SKILL.md docs/plans/006_independence_wave_plans/subagent_handoffs/006_portrait_skill_mode_reconciliation_2026_08_06.md`.
- Ran focused searches for `source_placeholder`, `replacement_pending`, `styled_final`, `HOI4-style`, `RunPod`, and `advisor` to verify the two modes remain distinct and the authorization gate remains present.

No simplification was made inside the requested scope. Other skill files may still contain older portrait wording and were intentionally left untouched because the parent limited this tranche to the two target skills.

The parent agent owns final review and commit of the shared worktree.
