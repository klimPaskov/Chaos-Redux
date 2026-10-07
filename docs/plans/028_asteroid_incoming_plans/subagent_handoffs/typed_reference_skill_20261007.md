# Typed references and map-entity allocation skill handoff

Disposition: implemented skill correction, pending parent review and parent-owned commit.
Acceptance basis: the user's explicit request to capture one reusable proven-workflow correction in an existing repo skill, with this exact handoff path.

## Changed files and rule

- `.agents/skills/chaos-redux-events/SKILL.md`: one paragraph under `3D model and entity integration`, immediately after the building/map-entity placement guidance.
- `docs/plans/028_asteroid_incoming_plans/subagent_handoffs/typed_reference_skill_20261007.md`: this new task-specific handoff, confirmed absent before creation.

Exact added rule:

> For map-entity allocation, distinguish typed country/state scope references from documented plain numeric IDs, and do not assume `THIS.id` is a displayed state number or country ordinal.
> Host fixtures must preserve that distinction and reject undocumented pointer arithmetic instead of seeding scope references with ordinary integers.
> Allocate entity IDs from a proven numeric getter or an existing verified literal map ledger, then audit uniqueness and collisions against every existing and proof allocation because `create_entity` replaces an entity with the same ID.
> Preserve scope pointers separately for identity and durable target links.
> Source/model and collision checks do not prove native playback or save/restore entity identity, and do not establish that every native arithmetic conversion is impossible.

The previous guidance covered map placement, entity linkage, source/runtime ownership, pointer identity and fixture limitations, but did not connect typed references to graphical ID allocation and collision checks.
No new skill was created.
`chaos-redux-event-assets`, `chaos-redux-subagents` and `chaos-redux-save-inspection` were left unchanged.
There is no dedicated numeric entity-ID/map-VFX section in the inspected asset skill, so the existing event entity-integration section owns the correction without duplicating it elsewhere.
No AGENTS.md or subagent routing update is needed.

## Evidence and references

The parent supplied the completed correction at commit `3e21f5eaef60d9b912cedfebfe1214b376c5c6b7` and its evidence paths.
The named `qa_evt028.hoi4` observation records USA at `1936.3.7.4`, Operation Postern `v1.19.2`, with the original state-506 reference stored as `-10737.41318` and the country reference as `10787.41059`.
These are the parent's documented observations, not a fresh save inspection by this worker.
The owner replaced the assumed numeric `THIS.id` plus 15000 with the shared verified map cache's literal numeric anchor province, yielding 1,081 unique IDs in 15036–28408 with zero overlap against 5,406 audited existing/proof IDs.
These counts are retained from parent evidence rather than represented as an independently rerun collision audit.

Read evidence documents in full: `docs/events/028_asteroid_incoming/map_presentation.md` and `docs/plans/028_asteroid_incoming_plans/native_save_observations_20261007.md`.
Read the emitter/retirement source in `common/scripted_effects/028_asteroid_incoming_map_visual_effects.txt` through line 135 and the relevant host-model excerpt in `.tools/validation/validate_028_presentation.py`, including its rejection of numeric `THIS.id`.
No gameplay validator was executed for this documentation-only change.

Read offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` lines 425–434 (Variables) and 955–972 (Token-valued variables), SHA-256 revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
The token section explicitly allows some token arithmetic, which prevents interpreting this correction as a universal ban on native arithmetic conversions.
Read installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` lines 3046–3068 through live `hoi4.reference_read`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Its `create_entity` contract states that a supplied existing ID replaces that entity, grounding the collision requirement.
Reference routes were exposed and the context, search and installed-section read succeeded.
The map context had omitted sources and was used only for discovery, without claiming complete map-reference coverage.

## Preservation, validation and limits

Before editing, read AGENTS.md and the complete `skill-creator`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-event-assets` and `chaos-redux-save-inspection` skills.
Reuse the events skill's existing scope/lifecycle and actual-source fixture guidance, the asset skill's source-versus-rendered-evidence boundary, and the subagents skill's bounded ownership and handoff contract.
Existing events-skill changes at the parchment formatting, transaction receipt and event-option audit sections belong to other work and were preserved.
Removing only this paragraph from the final text reproduces the pre-edit newline-normalized SHA-256 `0e8c75827998db320b93189cc3ca4eceb1e0a2994138134cf504bc4a81af3e6c`.
The added skill text contains no event number, tag, state number, commit hash, save name or task-specific allocation band.
The official `skill-creator` `quick_validate.py` accepted the updated events skill with `Skill is valid!`.

The first absolute-path patch attempt failed without changing the file hash, and the repository-relative patch succeeded.
No gameplay, assets, source scripts, external tool source, native game or Git state was changed by this worker.
The save was not opened, copied or modified.
Native graphical playback and save/restore entity identity remain unverified, and the evidence does not establish that every native arithmetic conversion is impossible.
There are no skill-maintenance blockers, simplifications or fallback claims.
The parent owns final review and the actual skill commit through the shared-working-tree workflow, including separation from other pending skill changes.
This worker freezes after returning the complete findings inline.
