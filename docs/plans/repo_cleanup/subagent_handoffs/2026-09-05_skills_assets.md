# Asset skill review handoff

Status: implemented documentation corrections, pending parent review.
The parent authorized this bounded cleanup and owns review, selective staging, and the commit.
No gameplay, asset, workbook, configuration, generated role, helper, provider, or engine files were changed.
No engine or provider route was called, and no game, Blender, or RunPod process was launched.
No commits, synchronization, or deletions were performed.

## Full-read ledger

These files were read in full before edits.
Coverage describes the pre-edit content, excluding later concurrent additions.

| File | Coverage |
| --- | --- |
| `AGENTS.md` | Full file, with the initially truncated middle recovered in a bounded read |
| `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` | All 413 pre-edit lines |
| `.agents/skills/chaos-redux-event-assets/SKILL.md` | All 1533 pre-edit lines |
| `.agents/skills/chaos-redux-comfyui/SKILL.md` | All 16 pre-edit lines |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | All 363 lines at review |
| `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md` | All 229 lines |
| `.codex/agents/chaosx_3d_model_pipeline.toml` | All 187 lines at review |
| `.codex/agents/chaosx_portrait_creator.toml` | All 20 lines |
| `.codex/agents/chaosx_generated_event_art.toml` | All 72 lines |
| `.codex/agents/chaosx_icon_artist.toml` | All 117 lines |
| `.codex/agents/chaosx_asset_source_researcher.toml` | All 58 lines |

Initial owned skill bytes matched the parent snapshot under `C:/Users/klimp/.codex/visualizations/2026/09/04/01a06e33-dc56-78e3-a787-850360234143/documentation_review/skills_batch02_baseline/files/` exactly.
Initial SHA-256 values were:

- 3D model pipeline: `e309dc7eacbfe2f31f61b69f5fad2def054e605dd8b643bc2b376e89957fa1ef`
- Event assets: `d01e0490b8fd54f8d1e300b10f86aed4f2f69dd63fbf6fb6ea9a6ea9f987d35d`
- Portrait production: `5e96c2b0e1b8967d33606daf70c411560bd4c6bc8295d58a8fc3760afac79a66`

Supporting references were consulted only to the extent needed for documentation review.
The first 24 lines of each required offline core page were opened: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
The Graphical asset modding introduction and Entity modding lines 1-45 were also opened.
The installed vanilla documentation directory was listed and `documentation/script_concept_documentation.md` lines 1-45 were consulted.
These limited readings do not establish engine-behavior validation.

## Exact surviving task changes

| Document | Disposition | Changes and basis |
| --- | --- | --- |
| `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` | `implemented` | Eight targeted replacements align live testing, screenshots, and in-game evidence with AGENTS.md sections 0 and 4.16, and replace the obsolete spawn argument. The parent retains source wiring, review, evidence reconciliation, and completion claims. The user performs live testing. `fork_context=false` becomes `fork_turns="none"` through Codex `collaboration.spawn_agent`, matching its current declaration and the shared subagents skill. |
| `.agents/skills/chaos-redux-event-assets/SKILL.md` | `implemented` | The technology icon paragraph names the exposed read-only `mcp__hoi4_agent_tools__hoi4_tech_inspect` and `mcp__hoi4_agent_tools__hoi4_tech_render` tools. Existing modes and views remain unchanged. It states the existing mandatory MCP requirement and distinguishes tool exposure, service health, and standalone viewer installation. Two 3D handoff/checklist passages assign live testing and screenshots to the user and evidence review to the parent. |
| `.agents/skills/chaos-redux-comfyui/SKILL.md` | `implemented` | Punctuation only. Portrait modes, provider ownership, source discipline, review requirements, and restrictions remain unchanged. |
| This handoff | `implemented` | Records read coverage, task changes, excluded concurrent content, validation limits, and unresolved protected conflicts. |

Mechanical prose cleanup replaced 91 prose semicolons in the 3D skill, 40 in event-assets, and 3 in portrait production with sentence punctuation.
The 3D count excludes semicolons already replaced in the targeted edits.
Five hard-wrapped reference-library paragraphs in event-assets were joined without changing their words.
Fenced code and quoted strings were preserved.
Source constraints, model choices, provider routes, spending policy, permission gates, safety gates, trigger boundaries, and fallback requirements retain their meaning.
No skill was created, and no other skill was edited by this worker.

No helper-path correction was needed.
The named DDS converter, report processor, achievement processor, portrait crop tool, advisor processor, Meshy wrappers, and 3D configuration paths were present at their documented locations.
Their existence does not prove successful helper or provider execution.

## Concurrent content excluded from this batch

Another user task inserted three lines under `Decision category and scripted GUI visual packs` in event-assets after the full pre-edit read.
They begin with `For new or redesigned scripted GUIs, follow` and reference `chaos-redux-scripted-gui`, then describe a compositional reference and painted bounds.
The parent confirmed that ownership and instructed this worker to preserve those lines untouched.
They were read only to verify preservation, were not audited for design or policy, and are excluded from this batch's full-read proof and changes.
The semicolon in that concurrent paragraph remains untouched.
The parent must stage only this batch's verified deltas, not the entire current event-assets file.

## Validation and limits

The official `skill-creator/scripts/quick_validate.py` reported `Skill is valid!` for all three owned skills.
A word-level diff was reviewed to distinguish the eleven targeted replacements from punctuation and wrapping changes.
Fenced blocks matched the initial snapshot exactly in all three skills.
The obsolete spawn argument is removed from the owned 3D skill.

Tool declarations were inspected through the current catalog without invoking the routes.
It exposes `mcp__hoi4_agent_tools__hoi4_tech_inspect`, `mcp__hoi4_agent_tools__hoi4_tech_render`, and `mcp__hoi4_agent_tools__hoi4_tech_compare` as read-only tools.
The documented inspect modes `explain` and `lint`, and render views `assets` and `folder`, appear in those declarations.
The catalog also exposes the named Meshy operations and repository Blender adapter operations.
This establishes tool names, not service health, installed package integrity, bridge reachability, provider balance, or viewer installation.
Those checks were outside this batch and were not run.
Standalone Technology Tree Viewer installation remains unverified here.
An absent viewer must be recorded as a package gap when verified, not inferred from route exposure.

## Protected conflicts left unresolved

Each item below is `unresolved` because reconciliation would alter protected policy or require engine/provider evidence outside this batch.
No permissive interpretation was selected.
Line numbers refer to observations during review and may shift with concurrent edits.

1. Grounded portrait completion conflicts with AGENTS.md.
   `.agents/skills/chaos-redux-comfyui/SKILL.md:12` says “No HOI4 repaint is required.”
   `.agents/skills/chaos-redux-event-assets/SKILL.md:273` says “`source_placeholder` is complete when selected.”
   `AGENTS.md:334` says “A wired sourced portrait remains an explicitly pending source placeholder until the user supplies its HOI4-style replacement.”
   Related `replacement_pending` restrictions in event-assets sections 8, 21, and 29 remain unchanged.
2. The 3D source transformation contract conflicts across owners.
   `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:405` prohibits creating “a substantially original substitute.”
   `.codex/agents/chaosx_3d_model_pipeline.toml:94` requires “a substantially original, model-ready refinement” and says “it need not be pixel-faithful.”
   The faithful-preparation gate and broader refinement permission were preserved.
3. The hard start gate and reading order conflict.
   `.codex/agents/chaosx_3d_model_pipeline.toml:10` requires the key check “Before reading AGENTS.md”.
   `AGENTS.md:11` requires offline wiki consultation before opening or editing any Chaos Redux file.
   The 3D skill's hard gate remains unchanged.
   This batch reviewed instructions and did not initiate a 3D production job.
4. Dependency installation instructions need clarification.
   `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:40` says the bootstrap “must also install and enable the matching Blender MCP add-on”.
   The mismatch branch at line 42 says “Do not install packages”.
   No installation scope or trigger was changed.
5. Animation source approval differs.
   `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:219` allows an external source “approved by the parent or user before acquisition”.
   `.codex/agents/chaosx_3d_model_pipeline.toml`, Animation rules, requires “an explicitly user-approved professional animation source”.
   AGENTS.md section 4.17 also requires user discussion for unapproved fallbacks.
   Existing approval requirements were preserved.
6. Nonhumanoid rig guidance differs.
   `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:215` requires the Meshy rig route first for creature, quadrupedal, multi-limbed, and mechanical profiles.
   `.codex/agents/chaosx_3d_model_pipeline.toml:107` limits Meshy rigging to a suitable standard humanoid biped and directs other profiles to Blender rigs.
   No provider capability or fallback claim was changed.
7. Exposed Meshy tool descriptions say “Before calling ANY tool that costs credits, present the cost and wait for user confirmation.”
   `AGENTS.md:71` and the 3D skill's paid-work rules pre-authorize planned spending and failure-driven recovery while balance and capability permit.
   No spending or confirmation rule was changed or acted on.
8. Portrait routing has a residual overlap.
   `.agents/skills/chaos-redux-event-assets/SKILL.md:81` includes “explicitly authorized fictional advisor masters” in `chaosx_generated_event_art` scope.
   `AGENTS.md:403` routes every character portrait to `chaosx_portrait_creator`, and event-assets section 21.1 assigns fictional advisor masters to that worker.
   This ownership/authorization boundary was reported rather than changed.
9. Advisor review uses a potentially stronger approval term.
   `.agents/skills/chaos-redux-event-assets/SKILL.md:1174` calls visual approval “a separate human gate”.
   The shared subagents skill's Parent review section requires a reviewer who is not the producer without specifying a human.
   The human approval wording remains unchanged.
10. Historical flag production routing remains unclear.
    Event-assets section 20 requires ImageGen final art for historical flags, while `.codex/agents/chaosx_generated_event_art.toml:29` excludes historical flags from that role.
    Source selection and ownership were not broadened.
11. Event-specific leakage remains in adjacent guidance.
    `.agents/skills/chaos-redux-event-assets/SKILL.md:312` names “Event 006 advisor assets”.
    The 3D skill's `--specialized-zombie-batch` option is an existing helper interface, not a generic renamed interface.
    This batch did not change those source/authorization examples or invent replacement flags.
12. `BGRB 8.8.8.8` remains a technical typo candidate in event-assets sections 6 and 29.
    The converter declares `DDS_FORMAT = "BGRA"` and provides `write_bgra_dds`, while section 24 already documents BGRA.
    The parent required installed vanilla and offline reference evidence before any engine/material correction.
    That evidence was not established here, so both phrases remain for separate technical review.

## Unreviewed references and parent work

The full-read ledger does not include the linked asset-library README, CATALOG, contact sheets, images, model jobs, dependency-lock contents, templates, helper READMEs, or all helper implementations.
The converter's declared format and writer were consulted as limited evidence only.
Offline and vanilla documents were consulted in excerpts, not audited in full.
No external source rights, provider pricing, live schemas, geometry, materials, animation, sound, counter art, or engine behavior was validated.

The parent should review these changes and conflicts, preserve the concurrent GUI addition, and commit only the accepted batch delta.
No simplification of asset-production requirements was introduced.
Protected conflicts and the technical typo candidate remain unresolved rather than being presented as repaired.
