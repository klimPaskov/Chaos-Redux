# Weapon-free reference skill consistency handoff

Disposition: implemented; parent review and commit pending.
Acceptance basis: the parent explicitly assigned this bounded correction and relayed the user's 2026-09-08 approval of fresh weapon-free firearm-body regeneration, superseding the former closure firearm exception while preserving non-firearm geometry.

## Changed documents

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`: replaced only the contradictory paragraph immediately after the opening paragraph of `Exactly one Meshy reference image`.
- This handoff records the patch, acceptance basis, review evidence, and boundaries.

The input gate requires readable complete anatomy, source identity, approved color/material cues, non-anime style, and zero firearms or wielded props on the firearm route.
The trigger-hand, support-hand, stock/shoulder, muzzle, and fireable-contact checks belong to the assembled Blender model and every firing action.
The `non_firing` exclusion remains explicit.

## Review evidence and boundaries

Compared the replacement with the same section's opening and preflight paragraphs, `Route selection and component completion`, and `Geometry, materials, rigging, and actions`.
The reference-input requirement no longer asks the weapon-free image to depict firearm contacts.
Exactly-one-input, Meshy 7 body-only production, direct Blender rig/actions and separate equipment, non-firearm preservation, provenance, immutable sources, and prepared-input parent approval remain unchanged.
No event-specific content was added to the skill, and no new skill, routing rule, tool name, MCP capability claim, or configuration was introduced.
This is documentation consistency evidence only, not model, provider-service, export, or runtime validation.
No gameplay files or other skills were edited, and nothing was staged or committed by this worker.

## Simplifications, omissions, and blockers

None for the assigned paragraph correction.
Parent review and commit remain parent-owned.
