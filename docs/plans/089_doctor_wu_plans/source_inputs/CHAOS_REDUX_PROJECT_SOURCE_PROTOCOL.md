# Chaos Redux Project Source Reading Protocol

## Purpose

This file defines the mandatory source-reading procedure for ChatGPT work inside the Chaos Redux project.

The short Project Instructions should point to this file. This file then provides the detailed rules so the Project Instructions can remain within the character limit.

## 1. Hard source-reading gate

Before doing any substantive project work, ChatGPT must fully read and process **every file currently supplied as a ChatGPT Project Source**.

This gate applies before:

- event or mechanic planning
- specification writing
- package creation
- repository research about the requested feature
- implementation recommendations
- asset planning
- design review
- audit conclusions

No substantive work begins until the gate passes.

## 2. What counts as a Project Source

The gate covers every source currently supplied to the ChatGPT project, including:

- Markdown and text files
- `AGENTS.md`
- skill files
- configuration files
- subagent definitions
- event, cluster, and scenario catalogs
- CSV files
- documentation
- user-supplied planning files
- ZIP and other supported archives
- relevant files contained inside supplied archives
- any other file exposed as a Project Source

Do not decide that a source is unimportant and skip it.

## 3. What “fully read” means

A file is fully read only when its complete contents have actually been accessed and processed.

The following do **not** count as full reading:

- search snippets
- previews
- partial excerpts
- summaries
- only the beginning or ending of a file
- only “relevant-looking” sections
- truncated tool output
- relying on a previous conversation
- relying on memory
- relying on a repository copy instead of the supplied source
- assuming two files are equivalent without checking the supplied source

If a tool says content is truncated, partial, clipped, or incomplete, continue reading through more chunks, searches, file views, or extraction until the entire file has been processed.

A tool response saying that the complete file is available does not itself count as reading the rest of the file.

## 4. Large-file reading procedure

For long files, read them in bounded chunks until the entire file has been covered.

Internally track enough information to avoid gaps, for example:

- filename
- file size when available
- chunk or line ranges read
- whether any output was truncated
- final completion status

Do not stop after a few highly relevant sections.

When possible, use a deterministic chunking scheme so that every byte or line range is covered exactly once or with harmless overlap.

## 5. Archive reading procedure

### `all-project-sources.zip` availability

`all-project-sources.zip` is intentionally supplied as an extractable Project Source. In the ChatGPT environment, it is available through the sandbox/container filesystem for direct archive extraction. If a Project Source browser, file-search surface, or preview tool cannot open the ZIP directly, that does not make the archive unavailable. ChatGPT must attempt extraction through the sandbox/container runtime before declaring `all-project-sources.zip` inaccessible.

For archives:

1. Inspect the archive inventory.
2. Extract it safely.
3. Enumerate the contained files.
4. Fully read every relevant contained text/configuration/subagent/skill/documentation/catalog file.
5. Record the archive as complete only after the contained required files are complete.

An archive listing alone does not satisfy the gate.

Do not treat subagent definition files inside an archive as optional merely because their names are already mentioned elsewhere.

## 6. Source coverage ledger

Before substantive work begins, every current Project Source must internally resolve to one of these successful states:

- `fully read`
- `fully extracted and read`

The following states fail the gate:

- `searched`
- `previewed`
- `partially read`
- `truncated`
- `assumed equivalent`
- `unavailable`
- `not relevant`
- `read in a previous conversation`

A useful internal source ledger may contain:

| Source | Type | Complete contents read | Archive contents read | Notes |
| --- | --- | --- | --- | --- |
| example.md | Markdown | yes | n/a | complete |
| agents.zip | archive | yes | yes | all definitions processed |

The ledger does not need to be shown to the user unless useful, but it should be used to prevent accidental omissions.

## 7. Failure behavior

If even one Project Source cannot be fully accessed or read:

1. Stop before producing the requested substantive work.
2. Name the exact incomplete or inaccessible source.
3. Explain the access problem.
4. Do not silently continue with a partial, simplified, or best-effort package.
5. Continue only if the user explicitly authorizes proceeding despite the missing source.

Do not claim that all Project Sources were read when this gate has failed.

## 8. Project Sources are the initial authority

Project Sources are the primary copies for the initial reading pass.

Do not use GitHub, the live repository, or another external copy to reread a file when the same or substantially equivalent version is already supplied as a Project Source.

Task-specific skill reading lists are **additional requirements**, not substitutes for the complete Project Source pass.

A skill that says “read these relevant files” never means “skip the rest of the Project Sources.”

Explicit user decisions and corrections take priority over older planning material.

## 9. GitHub and repository inspection after the gate

Once every Project Source has been fully read, GitHub or live-repository inspection is allowed and encouraged where useful.

Repository inspection is appropriate when:

- the required file is not included in Project Sources
- a Project Source explicitly links to another repository file
- current implementation state must be checked
- exact paths, identifiers, assets, helpers, or precedents must be verified
- existing code or integration points matter
- a supplied source may be stale and the difference matters
- a planning package needs current implementation evidence

It is completely acceptable to inspect repository files that are **not** present in Project Sources.

Do not reread full repository copies of already supplied Project Sources unless version differences matter to the task.

For planning work, use this priority:

1. all current Project Sources
2. the user's current brief and corrections
3. targeted repository inspection for missing or implementation-specific evidence

Avoid broad repository rereads when targeted inspection is enough.

## 10. Referenced repository documentation

After the source gate passes, inspect repository files explicitly required by supplied skills when they matter to the task, such as:

- offline Paradox wiki pages
- templates
- shared helper documentation
- current event implementations
- current focus trees
- decisions and missions
- GUI/GFX files
- country packages
- asset manifests
- docs referenced by `AGENTS.md`
- current catalogs or workbook-related evidence

If one of these external supporting files is inaccessible, record the limitation where it matters.

Do not pretend it was read.

## 11. ChatGPT environment limitations

ChatGPT is **not required** to execute Chaos Redux MCP workflows or spawn project custom subagents when those capabilities are unavailable in the ChatGPT environment.

Their absence does not block a planning package.

ChatGPT must never claim that it ran an MCP tool or spawned a subagent when it did not.

Instead, planning packages should prepare clear implementation maps for the later coding environment.

## 12. Subagent usage map requirement

When the supplied skills would normally route work to project subagents, the planning package should include a **Subagent Usage Map**.

For every relevant subagent, specify:

- canonical subagent name
- why it is needed
- when it should run
- exact surfaces it owns
- required inputs and context
- expected output or handoff
- files or systems it must not change
- dependencies on earlier implementation steps
- what the parent coding agent must review afterward

Only include subagents relevant to the planned feature.

Typical examples include:

- `chaosx_improvement_loop_planner`
- `chaosx_event_ui_worker`
- `chaosx_focus_tree_auditor`
- `chaosx_decision_mission_auditor`
- `chaosx_country_package_auditor`
- `chaosx_localisation_auditor`
- `chaosx_ai_probability_auditor`
- `chaosx_event_completion_auditor`
- `chaosx_scripted_system_architect`
- `chaosx_generated_event_art`
- `chaosx_icon_artist`
- `chaosx_portrait_creator`
- `chaosx_3d_model_pipeline`
- super-event text/audio research agents
- documentation and spreadsheet workers

The map should be detailed enough that Codex or another supported implementation environment can execute the workflow without redesigning the delegation structure.

## 13. MCP usage map requirement

When supplied skills require HOI4 MCP inspection, rendering, comparison, probability analysis, or other MCP evidence, the planning package should include an **MCP Usage Map** instead of requiring ChatGPT itself to execute unavailable tools.

For every relevant MCP surface, specify:

- tool or tool family
- exact gameplay surface
- when it should run
- required scenarios or states
- expected evidence
- before/after comparison requirements
- what findings block completion
- which parent or subagent owns the follow-up

Examples:

- scripted GUI: GUI inspect/render with matched before/after scenarios
- focus trees: focus inspect/render and route-layout review
- weighted AI, MTTH, and random selection: probability inspect/evaluate/compare workflow
- event chains: event inspect/render/compare when relevant
- technology/doctrine: tech inspect/render/compare
- map work: map inspection before any rewrite

These are implementation handoffs, not claims that ChatGPT already produced the evidence.

## 14. Planning package standard

Use the fully read Project Sources as the design baseline.

Use targeted repository inspection where useful.

Preserve the user's core design and expand it according to relevant skills.

Cover every surface the feature genuinely needs, such as:

- event progression
- mechanics
- evolutions
- decisions and missions
- focus trees
- country packages
- AI behavior
- assets
- scripted GUI
- animation
- 3D models
- super-events
- manual scenarios
- world-end branches
- achievements
- shared-system integration
- documentation
- catalog alignment
- subagent routing
- MCP validation handoffs

Do not add sections for systems the feature does not use.

Do not add administrative filler merely to increase package size.

## 15. Conflict handling

When Project Sources disagree:

1. identify the conflict
2. prefer explicit current user decisions
3. determine whether one source has clearer technical authority
4. distinguish accepted design from current implementation
5. leave genuinely unresolved contradictions explicit

Do not silently combine incompatible rules.

If current repository implementation differs from a Project Source, determine whether the difference is:

- newer implementation
- stale documentation
- planned future design
- an actual inconsistency

Do not silently replace the user's requested design with current repository behavior.

## 16. No silent simplification

Do not silently remove, merge, downgrade, replace, or omit requested mechanics because they are difficult.

If a requested feature appears technically questionable:

1. investigate it
2. inspect relevant source or repository evidence
3. design around the constraint when possible
4. mark unresolved feasibility issues clearly

Do not substitute a smaller fallback without explicit user approval.

## 17. Re-run rule

Run the complete Project Source reading gate at the start of **every new substantive task** in this project.

Do this even when:

- another task recently read the sources
- the same conversation previously used them
- memory contains summaries
- the source set appears unchanged

The current Project Sources are authoritative for the current task.

## 18. Final honesty rule

Never claim that:

- every Project Source was read when one was not
- repository evidence was inspected when it was not
- MCP evidence was collected when MCP was unavailable
- a subagent was used when it was not
- a planning package is implementation-validated when it is only design work

Clearly distinguish:

- fully read Project Sources
- repository files actually inspected
- user-provided accepted design
- planning assumptions
- future MCP work
- future subagent work
- implementation-only validation
- blockers and unresolved questions