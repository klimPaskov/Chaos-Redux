# Grounded portrait source-placeholder policy reconciliation

Date: 2026-08-03

Status: reusable portrait mode rule updated; no runtime portrait files were changed.

## Scope

Updated only `.agents/skills/chaos-redux-comfyui/SKILL.md` and this handoff.

No gameplay, character, GFX, interface, localisation, asset, spreadsheet, or other skill file was edited.

## Reusable rule added

When the user explicitly requests source-placeholder mode for a grounded historical or otherwise real-person portrait, preserve the unchanged attributed source, create an explicit head-and-shoulders crop with JSON equality evidence, fit it deterministically to `156x210`, convert it to DDS, and wire the runtime as `source_placeholder` with `replacement_pending`.

This mode must not create or validate a provider job, configure or select a provider workflow, upload the source, execute ComfyUI, repaint, style-transfer, recolour, retouch, filter, or substitute a generated face.

Provider-backed styled output remains required only when the user explicitly requests it or the task calls for a styled final, and the existing locked workflow, job schema, provider routing, output review, and `styled_final` gates remain in force for that mode.

Fictional high-chaos portraits use the native ImageGen route under the parent brief and never use the ComfyUI portrait workflow.

## Changed skill sections

- Frontmatter description now covers grounded source-placeholder mode and provider-backed final mode.
- Opening policy and provider persistence now separate source-placeholder mode from provider setup and execution.
- Portrait job contract now skips provider-job validation for explicit source-placeholder requests while preserving provider-backed workflow selection.
- Ownership and review now keep source research and provider execution conditional on the selected mode.
- Grounded source-placeholder mode now contains the complete source-to-crop-to-fit-to-DDS runtime sequence.
- Durable source/fallback guidance now distinguishes source-placeholder mode from a pending provider-backed styled request.
- Required handoff fields are conditional for source-placeholder versus provider-backed output.

## Preserved behavior

The locked upstream workflow ids, provider persistence fields, combined provider route sections, prompt rules, output dimensions, independent review gates, durable source archive, and parent-owned runtime wiring remain in the skill.

## Validation

- Read the repository instructions, offline Paradox Wiki core pages, relevant vanilla documentation, the portrait skill, the skill-creator guidance, the event-assets portrait guidance, and the current source-placeholder policy before editing.
- Ran `python -B C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-comfyui`.
- Re-read the edited skill and inspected its focused diff for mode wording, provider bypass, preserved workflow details, and accidental scope expansion.

No simplifications or unresolved blockers remain for this skill-only change.

The parent agent owns review and commit of the shared worktree.
