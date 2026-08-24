# Firearm animation, discharge effects, and sourced audio skill update

Status: complete after parent reconciliation.

## Changed files

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`: inlined the source-first modern-designed-artwork gate at the existing source/reference section. The gate now requires an eligible Internet-sourced designed-artwork origin, preserved URL/creator-or-publisher/rights-or-reuse/AI-use provenance, immutable original bytes and checksum, explicit `reference_only_user_authorized` direction for copyrighted reference use, faithful source-grounded ImageGen editing, exactly one Meshy input image, and a blocked or review stop when no eligible source survives. It rejects from-scratch model concepts, generic category replacements, and generative redesigns after failed search. Job intake now records source lineage and automatic recovery stop conditions, and the provider failure paragraph records automatic Meshy recovery with no recovery-spend confirmation.
- `.agents/skills/chaos-redux-3d-model-pipeline/references/source-reference-policy.md`: deleted after its still-valid instructions were inlined into `SKILL.md`.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`: extended the 3D handoff with the Meshy-only weapon-bearing source requirement, the prohibition on Blender weapon isolation/attachment/parenting/weighting/weapon-bone/manual replacement motion, automatic provider recovery or block, no ritual T-pose, firing-state discharge crosswalk, parent-owned runtime wiring, and the distinction that non-firing armed actions need no particles or gunshot audio. Added the corresponding final-checklist rows.
- Parent reconciliation removed the remaining recovery-confirmation language, removed the default A/T-pose and manual weapon-isolation/bone workflow, documented the verified Meshy `rig_task_id + action_id` animation contract, required visible firearm discharge motion and stable grip contacts, and added the complete firing-state particle/light/audio crosswalk directly to the 3D skill.

## Validation and evidence

- `Test-Path .agents/skills/chaos-redux-3d-model-pipeline/references/source-reference-policy.md` returns `False`.
- `rg source-reference-policy .agents/skills` returns no live reference.
- The source gate in `SKILL.md` was inspected at lines 144–162 after the edit and contains the inlined policy; no standalone source-policy link remains.
- The installed Meshy route was inspected: `mcp__meshy__meshy_animate` requires `rig_task_id` and integer `action_id`; the repository lock and client agree. The live read-only `meshy_check_balance` call returned 724 credits during this pass. The official animation-library reference documents `action_id` as the predefined library-action selector: [Meshy Animation Library](https://docs.meshy.ai/en/api/animation-library).
- The offline `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md` and installed vanilla MG entity precedent were consulted as required. No gameplay, GFX, entity, sound, model, or asset file was edited.
- Both updated skills pass the repository skill validator after parent reconciliation, and searches find no dangling policy-file reference or stale manual-weapon/recovery-confirmation route.

## Remaining blocker

None for this skill-maintenance tranche. Model production and runtime particle/audio wiring remain separate Event 016 implementation work.
