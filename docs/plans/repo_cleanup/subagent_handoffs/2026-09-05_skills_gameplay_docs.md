# Gameplay skill documentation review

Disposition: implemented for the bounded documentation edits listed here, pending parent review and selective staging.
The parent authorized correction of verified documentation defects in the events, decisions/missions, and focus-tree skill entrypoints, then explicitly added routing-wording corrections in the focus and decision canonical auditor TOMLs.
This handoff does not establish acceptance of any gameplay design, engine interpretation, provider operation, or concurrent GUI migration.
No simplifications were made to the assigned documentation corrections.
Protected conflicts remain unresolved below.

## Full reads and review boundary

Fully read the three assigned entrypoints before editing, including recovery reads for output truncated by the tool transport:

- `.agents/skills/chaos-redux-events/SKILL.md`, 810 lines at initial read.
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, 1170 lines at initial read.
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`, 1505 lines at initial read.

Fully read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md` as instruction references.
Fully read the canonical `chaosx_event_completion_auditor`, `chaosx_decision_mission_auditor`, `chaosx_focus_tree_auditor`, `chaosx_event_ui_worker`, `chaosx_ai_probability_auditor`, and `chaosx_skill_maintainer` TOMLs under `.codex/agents/`.
The focus and decision auditor TOMLs were fully reread before their later authorized routing edits.
The other reference files were not edited by this worker.
Opened the required eleven core offline wiki pages and consulted their contents listings and introductions.
No gameplay or engine rule was reconciled, and no vanilla implementation review or engine validation is claimed.

Verified the state-registry guide's actual location with filesystem existence checks, then read the relocated guide and its companion README as supplemental documentation.
The guide exists at `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/universal_state_registry_workflow.md`.
The formerly implied skill-root `universal_state_registry_workflow.md` does not exist.

Baseline: `C:/Users/klimp/.codex/visualizations/2026/09/04/01a06e33-dc56-78e3-a787-850360234143/documentation_review/skills_batch02_baseline/files`.
No commit or synchronization was run.

## Exact surviving edits

### Events skill

In `Spec and plan locations`, replaced:

> Source event specs live under `docs/specs/<event_id>_<event_slug>_specs/`. Implementation should read those files as the main design source when they exist.

With:

> Source event specs live under `docs/specs/<event_id>_<event_slug>_specs/`. Read them as the main design source when they exist, and record the explicit user decision or parent acceptance within the user-authorized scope that supports each accepted claim.
> A spec location, date, status label, or old handoff does not prove approval, and implementation evidence proves what exists rather than what was accepted.
> Keep missing or conflicting acceptance evidence unresolved under the AGENTS.md Specs and Plans dispositions.

In `Spec fidelity and implementation quality`, replaced exactly:

> When implementing from `docs/specs/`, treat mapped content as acceptance criteria.

With:

> When implementing from `docs/specs/`, treat mapped content with recorded acceptance as acceptance criteria.

The remaining fallback and simplification wording in that paragraph was preserved.

In `3D model and entity integration`, replaced:

> The main event agent owns the gameplay and runtime source wiring, final runtime copy synchronization, province/state placement, live consumer, and in-game evidence. The 3D worker owns the bounded model package and must not claim event or in-game completion.

With:

> The main event agent owns the gameplay and runtime source wiring, final runtime copy synchronization, province/state placement, and review of live-consumer and in-game evidence supplied by the user.
> The user performs live-consumer and in-game validation.
> The 3D worker owns the bounded model package and must not claim event or in-game completion.

Unwrapped the country-carrier paragraph without changing its words.
The old paragraph ran from `When an event needs a reusable country carrier, consult` through `are provenance only and are not current acceptance tools.` across eleven lines.
The new paragraph has five complete physical lines, beginning `When an event needs`, `Use the`, `Do not create`, `After changing`, and `The legacy`.
No carrier, collision, source, or archive rule changed.

The following ten exact punctuation replacements survived.
Each row records the complete changed substring, and the surrounding sentence content is unchanged.

| Old | New |
| --- | --- |
| `path; do not` | `path. Do not` |
| `evidence; the analyzer` | `evidence. The analyzer` |
| `` `scenarioSet`; do not `` | `` `scenarioSet`. Do not `` |
| `` `common/scripted_effects/chaosx_logic_effects.txt`; those effects `` | `` `common/scripted_effects/chaosx_logic_effects.txt`. Those effects `` |
| `block runs; if the actor` | `block runs. If the actor` |
| `` `record_events_log_evolution_entry = yes`; no-actor `` | `` `record_events_log_evolution_entry = yes`. No-actor `` |
| `incomplete content; it is` | `incomplete content. It is` |
| `placeholder roots; do not` | `placeholder roots. Do not` |
| `additive setup; put that setup` | `additive setup. Put that setup` |
| `Chaos Redux scientists; it is` | `Chaos Redux scientists. It is` |

### Decisions and missions skill

In the required-reading bullet, replaced exactly:

> - `templates/formable_state_puzzle/README.md` and `universal_state_registry_workflow.md` when a formable's proof uses exact state control

With:

> - `templates/formable_state_puzzle/README.md` and `templates/formable_state_puzzle/universal_state_registry_workflow.md` when a formable's proof uses exact state control

Two punctuation replacements survive outside the concurrent GUI replacement:

| Old | New |
| --- | --- |
| `` `custom_cost_trigger`; manually debit `` | `` `custom_cost_trigger`. Manually debit `` |
| `text and art; internal Markdown` | `text and art. Internal Markdown` |

An initial third punctuation replacement changed `abandoned; any defect` to `abandoned. Any defect` in the original background-first GUI paragraph.
The concurrent GUI replacement removed that paragraph.
This third replacement is not a surviving task hunk and must not be restored or staged as this worker's change.

### Focus-tree skill

The initial pass made two punctuation replacements, both in the reward-only layout-preservation paragraph:

| Old | New |
| --- | --- |
| `comparison evidence; they do not` | `comparison evidence. They do not` |
| `accepted scope; if the required` | `accepted scope. If the required` |

The inspection, comparison, rewrite, rollback, layout, and stopping rules are unchanged.
No skill was created.

### Routing corrections backed by explicit authority

The parent explicitly authorized these follow-up corrections and confirmed that equivalent remaining qualifiers in the owned skills should also be aligned.
The authority is `AGENTS.md`, Subagents, which requires `chaosx_ai_probability_auditor` for every weighted AI or probability surface, keeps that auditor read-only, and requires baseline audit, owner-applied patch, and matching-scenario comparison for weighted changes.
The same section limits explorer routing to unclear file locations, patterns, references, touchpoints, missing-file recovery, or implementation order.
These edits align lower-level wording with those existing requirements without choosing a new probability or activation policy.

All following old/new sentence pairs are exact surviving replacements.
The rest of each paragraph, including scenario and compare requirements, remains unchanged.

| File and location | Old | New |
| --- | --- | --- |
| Events skill, subagent list | Spawn `chaosx_repo_explorer` before editing when the event touches many systems or when file locations are uncertain. | Use `chaosx_repo_explorer` before editing only when file locations, existing patterns, vanilla references, likely touchpoints, missing-file recovery, or implementation order are unclear. |
| Events skill, subagent list | Spawn `chaosx_ai_probability_auditor` for every complex or balance-sensitive AI weight, MTTH, random-selection, or weighted-pool surface before completion. | Spawn `chaosx_ai_probability_auditor` for every in-scope AI weight, MTTH, random-selection, or weighted-pool surface before completion. |
| Decisions skill, introduction | Route every complex or balance-sensitive decision or mission weight to `chaosx_ai_probability_auditor` for the mandatory MCP probability pass. It may directly patch small decision, mission, tooltip, dynamic localisation, AI, cleanup, cooldown, visibility, and existing formable requirement issues when the fix is local and clearly safer. | Route every in-scope decision or mission weight to `chaosx_ai_probability_auditor` for the mandatory MCP probability pass. The probability auditor remains read-only. The `chaosx_decision_mission_auditor` may directly patch small decision, mission, tooltip, dynamic localisation, AI, cleanup, cooldown, visibility, and existing formable requirement issues when the fix is local and clearly safer. |
| Decisions skill, AI behavior | For complex decision or mission weights, route the analysis through `chaosx_ai_probability_auditor`. | For every in-scope decision or mission weight, route the analysis through `chaosx_ai_probability_auditor`. |
| Focus skill, introduction | Route every complex or balance-sensitive focus-weight audit through `chaosx_ai_probability_auditor`. | Route every in-scope focus weight through `chaosx_ai_probability_auditor`. |
| Focus skill, AI behavior | When focus selection probabilities, route dominance, or starvation matter, route the audit through `chaosx_ai_probability_auditor`. | For every in-scope focus-selection or focus-weight surface, route the audit through `chaosx_ai_probability_auditor`. |
| `.codex/agents/chaosx_focus_tree_auditor.toml`, opening MCP paragraph | For every complex or balance-sensitive focus weight, route the mandatory probability analysis through `chaosx_ai_probability_auditor`. | For every in-scope focus weight, route the mandatory probability analysis through `chaosx_ai_probability_auditor`. |
| `.codex/agents/chaosx_decision_mission_auditor.toml`, opening MCP paragraph | For every complex or balance-sensitive decision or mission weight, route the mandatory probability analysis through `chaosx_ai_probability_auditor`. | For every in-scope decision or mission weight, route the mandatory probability analysis through `chaosx_ai_probability_auditor`. |

Only the quoted sentences inside `developer_instructions` changed in the two TOMLs.
Their names, descriptions, models, reasoning efforts, sandbox modes, nickname candidates, and all text outside the instruction field were preserved byte-for-byte.
The decision auditor's concurrent scripted-GUI reading bullet was preserved.
No generated role was changed and no sync was run.
The parent owns any required propagation of the canonical role instructions under the repository's runtime workflow.

## Concurrent changes excluded from this handoff

The parent confirmed that another user task is creating `chaos-redux-scripted-gui`.
Its changes were preserved and are excluded from this worker's ownership and validation claim.

- The decisions skill's `Scripted GUI decision categories and mechanic windows` section was replaced after the full read, with new routing to `chaos-redux-scripted-gui` and consolidated GUI action guidance.
- Its introductory companion-skill paragraph also gained a `chaos-redux-scripted-gui` reference.
- The events skill's `Scripted GUI and animated event presentation` section gained `chaos-redux-scripted-gui` reference-selection and native-element mapping guidance, and its worker contract reference changed to that skill.
- The decision auditor TOML gained a required-reading bullet for `.agents/skills/chaos-redux-scripted-gui/SKILL.md`.
- Reconstructing the intended event edits from the parent baseline exposed only that additional GUI-routing delta at the final comparison.
- Reconstructing the intended focus edits from the parent baseline matched the current focus skill exactly at the final comparison.

The parent should stage only the exact surviving edits above against current HEAD.
Do not stage complete current files as if all their differences belong to this batch.
The new GUI skill and migrated GUI guidance were not fully audited by this worker.
Any punctuation introduced inside the concurrent replacement remains with its owner.

## External candidates for selective staging

At the parent's request, wrote baseline-plus-reviewed-change candidates under `C:/Users/klimp/.codex/visualizations/2026/09/04/01a06e33-dc56-78e3-a787-850360234143/documentation_review/reviewed_candidates/`, using the original repository-relative paths.
The three skills use `skills_batch02_baseline/files` as their source, and the two canonical roles use `batch01_baseline/files`.
Candidates exclude the concurrent GUI migration and exclude the removed GUI paragraph's punctuation edit.
They are staging inputs and must not overwrite the shared working files.
Candidate/current comparisons normalize only CRLF versus LF for content review.

| Candidate path below the external root | SHA-256 | Difference from current content |
| --- | --- | --- |
| `.agents/skills/chaos-redux-events/SKILL.md` | `451db33d4b873db977d41eb988ce8814fc272842564eb69234408c1b1978b887` | Only the known concurrent GUI-routing paragraph |
| `.agents/skills/chaos-redux-decisions-missions/SKILL.md` | `11147bfb355d0dac77d39b2b951073bd8904cf9700ccbde987e0ccf31ec0d329` | Only the known companion-skill reference and concurrent GUI-section replacement |
| `.agents/skills/chaos-redux-focus-trees/SKILL.md` | `01f0a02087db793af889e30d833733e6aa9a4552f793f562e8499975e068d324` | Exact content match |
| `.codex/agents/chaosx_focus_tree_auditor.toml` | `d13068aaf5d1ffea1bd4c62a676c67e8d80da0bda0f4c4478d206e784f62335f` | Exact content match |
| `.codex/agents/chaosx_decision_mission_auditor.toml` | `63031f8b2a8fa5b87d3bb1e83ae28f583b94c1ebd7fadf0b42142061d24bb233` | Only the known concurrent scripted-GUI reading bullet |

No unknown candidate/current delta remained at comparison time.

## Verification and preserved gates

All three entrypoints passed the official `skill-creator/scripts/quick_validate.py` validator.
All three external skill candidates also passed that validator after the routing corrections.
Parsed both current and candidate auditor TOMLs with `tomli` and confirmed all six fields outside `developer_instructions` equal the parent baseline.
The first decisions validation attempt failed because Windows Python used cp1252 to read UTF-8 prose.
Rerunning with `python -X utf8` passed without changing file content to accommodate that environment issue.
The repaired required-reading path resolves to the guide that documents the universal state-registry workflow.
Compared current files with an expected reconstruction of this worker's baseline edits to identify and preserve the concurrent deltas described above.

The current `collaboration.spawn_agent` schema uses `fork_turns`, and `fork_turns="none"` is already documented in the shared subagents skill and AGENTS.md.
None of the three owned entrypoints contained `fork_context`, so no tool argument was changed there.
Discovered the exposed `mcp__hoi4_agent_tools__hoi4_event_*`, `hoi4_focus_*`, `hoi4_gui_*`, `hoi4_probability_*`, and `hoi4_tech_*` tool names from session metadata without calling the engine or provider.
Existing named routes used by the punctuation-edited MCP paragraphs were present in that metadata.
Exposure establishes neither service health nor standalone Technology Tree Viewer availability.
No service-health or viewer-availability claim was added, and the shared package-gap requirement remains unchanged.

Preserved mandatory MCP use, read-only inspector and viewer rules, probability audit/patch/compare ownership, balance limits, source and provider requirements, spend and approval requirements, portrait handling, trigger gates, and user-only live testing.
No gameplay, asset, localisation, workbook, generated-role, provider, engine, or runtime configuration was edited.
The two canonical auditor prompt TOMLs changed only inside `developer_instructions` as explicitly authorized above.
No archived helper was invoked and no fallback was selected.

## Reviewed conflicts and dispositions

These passages are quoted as evidence only.
This review makes no permissive choice and does not reconcile engine, probability behavior, balance, source, or permission rules.
The probability-routing and explorer wording findings are resolved under explicit higher-priority authority as recorded above.

### Duration fields

AGENTS.md says:

> For duration fields that reject constants, such as `days =` inside timed flags, assign the constant to a normal or temporary variable first and pass that variable to `days =`.

The events skill's `Duration fields and constants` section says:

> For those fields, use a file-scoped `@NAME = literal` constant in the same script file and pass `days = @NAME`. Keep the value mirrored with the matching `common/script_constants/` tuning entry, and update both in the same change.

And:

> Do not work around this by setting a temp variable and passing `days = temp_name`. those fields can reject variable tokens too. In which case, a `meta_effect` must be used if possible.

Disposition: unresolved engine interpretation, left unchanged.

### Probability audit scope and patch antecedent

Before the authorized follow-up, the decisions skill introduction said:

> Route every complex or balance-sensitive decision or mission weight to `chaosx_ai_probability_auditor` for the mandatory MCP probability pass. It may directly patch small decision, mission, tooltip, dynamic localisation, AI, cleanup, cooldown, visibility, and existing formable requirement issues when the fix is local and clearly safer.

The probability auditor's canonical role says:

> - Do not use rewrite tools or patch weights, prerequisites, route logic, or tuning values.

The events and focus skills and the canonical focus and decision auditor prompts also used limited routing qualifiers.
Disposition: resolved by the exact routing replacements above under AGENTS.md's existing every-surface rule and the parent's explicit follow-up authorization.
The patch-capable subject is now explicitly `chaosx_decision_mission_auditor`, and `chaosx_ai_probability_auditor` remains read-only.

### Focus reward exceptions

The focus skill says:

> If a focus mainly gives a small flat modifier, the implementation must justify why that modifier matters. It can be acceptable as one part of a larger reward package, a frequent stack, a temporary crisis push, or a final adjustment to an existing mechanic.

Its hard fairy-dust rule says:

> Values such as `+2%`, `+3%`, `+7%`, `12`, `18`, tiny political power grants, tiny stability or war support changes, token equipment, and slight generic production bonuses are completion-blocking defects unless an engine-defined formula or hard technical constraint requires that exact value.

Disposition: unresolved balance-exception tension, left unchanged.

### Explorer activation

Before the authorized follow-up, the events skill said:

> - Spawn `chaosx_repo_explorer` before editing when the event touches many systems or when file locations are uncertain.

AGENTS.md says:

> Use `chaosx_repo_explorer` only when file locations, existing patterns, vanilla references, likely touchpoints, missing-file recovery, or implementation order are unclear.

Disposition: resolved by mirroring the existing AGENTS.md uncertainty-based gate, with explicit parent authorization.

### Supplemental template references outside write scope

`templates/formable_state_puzzle/README.md` says:

> The parent still owns runtime wiring, final source review, and live-consumer validation.

It also assigns `final in-game acceptance` to the event/system owner in its ownership paragraph.
AGENTS.md assigns live-consumer and in-game validation to the user.
Disposition: unresolved out-of-scope documentation correction for the parent to route.

The same README says:

> Avoid relying on event targets in scripted GUI: the offline Scripted GUI wiki explicitly warns that event targets break there.

The events skill says:

> Event targets are valid scope pointers inside scripted GUI triggers, effects, and scripted localisation.

Disposition: unresolved engine interpretation, with both passages preserved.

## Unreviewed references and remaining limits

No transitive review of gameplay, vanilla sources, runtime assets, map registries, catalog data, event specs, or event plans was performed.
Beyond the entrypoints and canonical roles explicitly listed above, referenced skill bodies such as event-assets, comfyui, 3D-model-pipeline, frame-animation, event-planning, improvement-loop, super-events, MTTH, and xlsx remain outside this batch's full-read claim.
The formable template schemas, scripts, examples, `category_attachment_audit.md`, `validation_checklist.md`, and `static_category_picture_option.md` were not audited.
Paths and helper identifiers unrelated to the one repaired guide reference were not reconciled with gameplay source.
The concurrent scripted-GUI skill and migration require their own owner review.
The parent owns final review, selective staging, and any commit.
