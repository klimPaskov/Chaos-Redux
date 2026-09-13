# Skill cleanup completion report, 2026-09-13

Disposition: `implemented` for the requested safe editorial cleanup and preservation review.
Unresolved conflicts and missing references remain explicitly pending below.

The [category-picture policy and hash cleanup follow-up](category_pictures_and_hashes.md) records the subsequent explicit user corrections.
The passage maps and citation inventories below describe the preceding cleanup snapshot; consult the follow-up for current picture eligibility and hash-bookkeeping changes.

## Scope and preservation

Reviewed all 16 project `SKILL.md` files and their 12 supporting instruction/example documents against a pre-edit snapshot that includes existing user changes.
Applied editorial changes to all 16 skills and four supporting Markdown documents; eight supporting documents remain unchanged.
Each bounded owner fully read its assigned originals and the references needed to interpret them before editing, repaired truncated reads, and recorded a passage-level preservation map.
The parent reviewed the changes, correction evidence, remaining conflicts, and preservation results.

Related prerequisites and ownership rules precede dependent steps; family-specific guidance, exceptions, and execution gates remain attached to their scope.
Changes include heading hierarchy, phase grouping, misplaced-section moves, checklist numbering, paragraph reflow, and slight wording reductions.
The adjacent repeated `evolutions` bullet and genuine super-event purpose, quote, and source-preservation repetition were merged.
No cross-file instruction was removed to rely on another skill being loaded.
No shared template was imposed.

The preservation review accounts for every original passage or documented authority correction.
All 16 skill frontmatter blocks retain their original raw bytes; fenced examples and technical literals remain intact.
Original conditions, instruction strength, exceptions, workflow order, dependencies, values, and identifiers were retained.
No simplifications or intentional omissions were introduced.
Official skill validation passed for all 16 folders; maintained Markdown references were reviewed against the final headings and retained resources.

## Justified corrections

| Correction | Basis and detailed record |
| --- | --- |
| Route every character portrait, including fictional advisor masters, to `chaosx_portrait_creator`. | Explicit AGENTS.md portrait ownership in sections 0 and 8; [asset record](assets.md#moves-merges-and-authority-corrections). |
| Keep sourced `source_placeholder` portraits pending until the user supplies the HOI4-style replacement; preserve the explicit request-only modes and identifiers. | AGENTS.md section 4, item 17, and portrait ownership; [asset record](assets.md#moves-merges-and-authority-corrections) and [portrait record](other.md#evidenced-correction). |
| Clarify sourced historical flag design followed by required final ImageGen reconstruction. | The existing asset and planning every-new-flag rules; [planning record](planning_routing.md#corrections-and-evidence). |
| Assign the decision template's live-game acceptance and validation to the user. | AGENTS.md section 0 and section 4, item 16; [decision record](decisions_focuses.md#evidenced-authority-corrections). |
| Replace the stale 3D `event-assets section 9.1` pointer with the actual named counter-contract anchor. | The retained asset heading and locally resolved target; [model record](models_events.md#genuine-merges-and-corrections). |

## Model defaults and user correction

The Astra cleanup subagents were interrupted immediately and were not resumed.
Subsequent cleanup used Sol high workers with explicit isolated prompts.
Only the `model` and `model_reasoning_effort` fields in the three affected TOML definitions were changed to `gpt-5.6-sol` and `high`: `chaosx_3d_model_pipeline`, `chaosx_event_ui_worker`, and `chaosx_skill_maintainer`.
Every other byte of those definitions was preserved against their pre-change snapshot.
The user's final correction explicitly retains Astra for 3D model authoring; those workflow instructions remain intact.
Generated agent definitions were not synchronized or rewritten.
The model-field-only commit is `098de50cf0` (`Set Astra subagent TOML defaults to Sol high`).

## Unresolved conflicts and decisions

No precedence or compromise was invented for these cases.
The original competing instructions remain intact, with exact locations, scope analysis, and decisions needed in the linked records.

| Area | Pending decision and location record |
| --- | --- |
| Planning | Whether sourced finished super-event wording may appear in a spec, and whether the prohibition on implementation tables excludes the separately mandated detailed 3D matrices/prompts; [planning boundaries](planning_routing.md#unresolved-boundaries-and-scoped-distinctions). |
| Assets | Manual versus bundled advisor dossier composition; people-free councils versus expressly authorized staged invented groups; separate Meshy firearm geometry versus Blender construction; [asset conflicts](assets.md#unresolved-conflicts-and-exact-decision-needs). |
| Models and events | Timed-flag variable forwarding versus rejecting variables and using local constants/meta construction; workbook-only spreadsheet ownership versus the broader events dispatch wording; firearm construction also appears here; [model/event rules](models_events.md#unresolved-rules-and-scoped-differences). |
| Decisions and focuses | Registry migration versus alternate counting paths; eligibility-dependent control results; example YAML prose/key formatting; duplicated geometry evidence; fresh builder evidence versus reused reviewed artifacts; palette differences; event-created versus expressly designed replacement focus loading; static-picture exception scope; [eight exact cases](decisions_focuses.md#unresolved-contradictions-and-decisions-needed). |

Sol TOML defaults versus Astra 3D authoring, opt-in debug playtesting versus ordinary no-launch work, stronger parent audio limits, and differently scoped prose guidance were treated as explicit or compatible scoped distinctions.
They were not silently normalized into universal rules.

## References and verification limits

The team consulted the required offline core wiki pages, adjacent system pages, relevant installed vanilla documentation/examples, the official `skill-creator` skill, and project subagent/maintainer guidance.
The handoffs distinguish complete instruction-document reads from relevant engine-reference excerpts and list all consulted sources.

Seven inherited links in the asset interface reference README point to absent resources, including its contact sheet and six named family shelves.
Their literal paths were preserved because no equivalent destination was established; the missing images cannot be read or verified.
The debug skill's required generic `hoi4-autonomous-debug-playtest` package was also absent from the searched repository, user skill roots, and plugin cache.
Its dependency remains intact pending its actual location or an explicit dependency decision; [missing dependency record](other.md#unresolved-dependencies-and-scope-distinctions).

All 22 generated `.qoder/repowiki` documents citing skill line spans were fully read.
98 exact citation target/label updates were applied in five documents; 100 citations remained at their verified original positions, and 408 uncertain or already stale citations remain unchanged with individual reasons in the [citation record](cross_references.md).
Prose and fenced examples in these generated documents were preserved.
These documents are ignored and untracked, so their workspace repairs were not force-added to Git.

This is an instruction-document audit, not an independent verification of current provider pricing, tool health, licensing, Blender integration, or engine/runtime behavior.
No paid workflow, external production action, or live-game testing was performed.

## Commit boundary and review records

The cleanup commit contains 18 independently reviewable revised instruction documents and these review records.
The asset and event skill entrypoints remain edited in the working tree but outside that commit because their cleanup overlaps earlier or concurrent changes.
Unattributed event database/default-object and synchronization-scheduling additions were preserved and were not adopted as requirements authored by this cleanup.
Unrelated gameplay changes and the other task's staged work were excluded from this commit.

| Review record | Coverage |
| --- | --- |
| [Planning and routing](planning_routing.md) | Event planning, improvement loop, subagent routing. |
| [Assets](assets.md) | Asset skill and six supporting Markdown documents. |
| [Models and events](models_events.md) | 3D pipeline, events, super-events. |
| [Decisions and focuses](decisions_focuses.md) | Focus/decision skills and five template Markdown documents, plus read-only example/schema interpretation. |
| [Other skills](other.md) | Portraits, debug playtesting, MTTH, state ledgers, spreadsheet guidance, GUI, frame animation. |
| [Generated citations](cross_references.md) | Fully read generated callers, exact safe reference repairs, and unresolved attribution. |

The complete original/final snapshots, SHA-256 inventory, mechanical preservation review, validator results, and selective commit candidates are retained locally under `C:/Users/klimp/.codex/tmp/chaos-redux-skill-cleanup-20260913/`.
These supplement the passage maps and manual review; they do not substitute for reading the instructions.
