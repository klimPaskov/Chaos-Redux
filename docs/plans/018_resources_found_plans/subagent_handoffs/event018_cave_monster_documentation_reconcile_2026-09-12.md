# Event 018 cave monster documentation reconciliation handoff

Date: 2026-09-12.

Scope: documentation-only reconciliation of the Cave Monster 3D package against the current runtime model folder, animation registry, mesh registry, entity consumers, five cave-brood sub-units, counter registry, sound definitions, and named historical handoffs.

## Outcome

The current runtime package is `implemented` with one mesh and four present and registered actions. The accepted current action contract intentionally maps `defend` and `support_attack` to `attack`, `retreat` to `move`, and `training` to `idle`. The stale `needs_user_review` status from the pre-visual 2026-08-10 static audit and the later eight-distinct-Meshy-action recovery requirement do not govern the current package.

The new authoritative current-state record is `docs/plans/018_resources_found_plans/cave_monster_current_package_manifest.md`. It does not claim live-game validation or strict 3D pipeline package completion.

## Source-of-truth map

| Claim type | Current authority | Disposition and boundary |
| --- | --- | --- |
| Current runtime bytes and hashes | `cave_monster_current_package_manifest.md` plus the engine-facing files | `implemented`; hashes were recomputed from the current checkout on 2026-09-12 |
| Current four-action and alias contract | `cave_monster_current_package_manifest.md`, `gfx/entities/018_resources_found_cave_monster.gfx`, and `gfx/entities/018_resources_found_cave_monster.asset` | accepted current design based on the parent task's explicit current exhaustive-audit finding; no live-game claim |
| Production lineage and historical export facts | `subagent_handoffs/cave_monster_3d_model_handoff.md` | implemented historical evidence; source/job paths are no longer present |
| Static visual proof | `subagent_handoffs/event018_cave_monster_visual_closure_2026-08-10.md` | implemented historical evidence; later than and superseding the pre-visual static audit |
| Runtime behavior contract | `docs/systems/3d_model_pipeline/resources_found_cave_monster_model.md` | current durable description linked to the current package manifest |
| Live HOI4 and audible behavior | no user-provided evidence in scope | unresolved validation limit; no in-game completion claim |
| Deterministic source/job package | no current job root, source image, checkpoint set, selected exports, reimport artifacts, or prior package manifest exists in the checkout | `blocked`; exact production and reproducibility gap |

## Plan and handoff dispositions

| Document | Previous state | Current disposition | Basis and reason |
| --- | --- | --- | --- |
| `018_cave_monster_3d_integration_addendum.md` | static integration `complete` | `implemented` | current entity aliases, sound hooks, and runtime hashes are present; strict package completion and live validation are not claimed |
| `subagent_handoffs/cave_monster_3d_model_handoff.md` | bounded static package `complete` | `implemented` historical production evidence | runtime hashes still match; the deterministic source/job package is absent |
| `subagent_handoffs/event018_cave_monster_static_closure_2026-08-10.md` | `needs_user_review` | `superseded` | `event018_cave_monster_visual_closure_2026-08-10.md` supplied the missing non-live visual evidence, and the current manifest records the current status |
| `subagent_handoffs/event018_cave_monster_visual_closure_2026-08-10.md` | bounded static package `complete` | `implemented` historical visual evidence | its evidence remains valid, while the current manifest separates runtime implementation from the absent job package and unperformed live validation |
| `subagent_handoffs/event018_cave_monster_meshy7_nonhumanoid_blocker_2026-08-22.md` | eight-role recovery `blocked` | `superseded` as current package status | the current parent acceptance identifies four actions and the listed aliases as intentional; the provider limitation remains conditional evidence only if an eight-distinct-provider-action requirement is explicitly accepted again |

## Contradictions reconciled

1. The pre-visual static audit retained `needs_user_review`, while the later visual closure recorded completed static evidence. A superseded notice now points the old audit to the later evidence and the current manifest.
2. The 2026-08-22 recovery handoff rejected all four local actions and every state alias, while the current accepted audit identifies the four actions and aliases as intentional. A superseded notice now preserves the provider-capability finding without letting the rejected eight-role requirement override current design.
3. Several durable documents said the temporary `docs/assets/018_resources_found/` workspace or reconstructed adapter roots were retained. Those paths are absent, and the current system, event-asset, integration, and model-handoff documents now record that fact.
4. The integration addendum described the five resolving entities as absent in its evidence baseline even though its own repair section and current source show them implemented. The sentence now identifies that as the historical pre-repair state.

## Duplicate or superseded documents

- `event018_cave_monster_static_closure_2026-08-10.md` is retained as historical pre-visual audit evidence and marked superseded.
- `event018_cave_monster_visual_closure_2026-08-10.md` remains the visual-proof record and defers current package status to the new manifest.
- `event018_cave_monster_meshy7_nonhumanoid_blocker_2026-08-22.md` is retained as a conditional provider-capability record and marked superseded for current package disposition.
- `cave_monster_3d_model_handoff.md` and `resources_found_cave_monster_model.md` retain different purposes: historical production evidence and current runtime behavior respectively, so they were not merged.

## Stale prompts and instructions

No cave-monster prompt file or deterministic job file exists in the current checkout. The stale actionable instruction was the 2026-08-22 demand for eight distinct Meshy-provenance actions; it is now explicitly superseded for the current package.

Historical paths under `docs/assets/018_resources_found/models_3d/` remain useful lineage references but must not be read as existing files or a resumable current job.

## Markdown hard-wrap audit

No accidental mid-sentence or mid-clause hard wraps were found in the changed Markdown scope. Deliberate headings, paragraphs, list items, tables, and block quotes were preserved.

## Files changed

- Created `docs/plans/018_resources_found_plans/cave_monster_current_package_manifest.md`.
- Created `docs/plans/018_resources_found_plans/subagent_handoffs/event018_cave_monster_documentation_reconcile_2026-09-12.md`.
- Updated `docs/plans/018_resources_found_plans/subagent_handoffs/event018_cave_monster_static_closure_2026-08-10.md` with a superseded-status notice.
- Updated `docs/plans/018_resources_found_plans/subagent_handoffs/event018_cave_monster_visual_closure_2026-08-10.md` with a current-status notice.
- Updated `docs/plans/018_resources_found_plans/subagent_handoffs/event018_cave_monster_meshy7_nonhumanoid_blocker_2026-08-22.md` with a superseded-recovery notice.
- Updated `docs/plans/018_resources_found_plans/subagent_handoffs/cave_monster_3d_model_handoff.md` to defer current status to the manifest and record the absent historical job roots.
- Updated `docs/plans/018_resources_found_plans/018_cave_monster_3d_integration_addendum.md` to use the `implemented` disposition, identify the historical pre-repair evidence correctly, and record absent temporary roots.
- Updated `docs/systems/3d_model_pipeline/resources_found_cave_monster_model.md` to identify the authoritative manifest and absent source/job package.
- Updated `docs/events/018_resources_found/assets.md` to stop claiming that the absent temporary workspace is retained and to link the authoritative package manifest.

## Validation

Current SHA-256 hashes were recomputed for all nine files in the runtime model folder, both entity registration files, the five-consumer sub-unit file, the shared counter registry, and the sound-definition file. Direct source inspection confirmed four animation registrations, the canonical entity's eight state bindings, the five clone aliases, and all five sub-unit sprite tokens.

Targeted searches confirmed that the three historical `docs/assets/018_resources_found/` paths are absent and that no cave-monster job or package manifest existed elsewhere under `docs/` before this patch. Targeted status and path searches were repeated after patching.

No Blender, Meshy, provider, adapter, HOI4, audio-playback, or live-game operation was run because this was a documentation-only reconciliation against current files and preserved evidence.

## Remaining risks and parent decisions

The parent should retain `implemented` as the current static runtime disposition unless user-provided live evidence supports a separate in-game conclusion. The parent should not restore `needs_user_review` merely because live-game validation remains unperformed; the current manifest already records that validation limit without conflating it with the static implementation state.

The absent source/job package remains the only confirmed production and reproducibility blocker. A future repair or regeneration tranche needs a newly complete deterministic job under the then-current 3D pipeline contract; documentation cannot reconstruct missing source images, Blender checkpoints, selected exports, or reimport artifacts.

No gameplay, localisation, scripted localisation, GUI, GFX, model, animation, sound, spreadsheet, skill, `.codex`, `.qoder`, or `.cursor` file was edited. No simplification or fallback was introduced.

