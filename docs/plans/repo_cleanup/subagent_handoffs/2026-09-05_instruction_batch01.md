# Instruction cleanup batch 01 handoff

Date: 2026-09-05.
Status: bounded instruction repairs implemented for parent review.
Acceptance basis: the parent assigned these exact repairs and relayed the user's approval to apply the full-reading prerequisite separately to bounded cleanup batches.
This handoff does not claim approval for other repository changes or completion of the repository-wide cleanup.

## Files changed and behavior

| File | Before | After |
| --- | --- | --- |
| `AGENTS.md` | Specs location could be read as acceptance, Codex guidance used an unsupported context argument, and some ownership prose assigned in-game validation to agents. | Specs and Plans separates explicit user decisions, accepted design with its basis, implementation evidence, and proposals. It defines evidence-bearing dispositions. Codex guidance uses `collaboration.spawn_agent` with `fork_turns="none"`. Parent review and mandatory source/MCP evidence remain required, and the user owns live-game validation. |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | Routing repeated the context argument and used incomplete disposition shorthand. Tool exposure and standalone viewer availability were not distinguished. | Shared routing uses the supported Codex argument without inherited context, aligns dispositions with AGENTS.md and the plans index, and separates exposed technology routes, service health, and viewer availability. |
| `.codex/agents/chaosx_documentation_curator.toml` | A file in the specs area was presumed accepted unless called obsolete. | Acceptance needs a cited user decision or parent acceptance within authorized scope. Unsupported or conflicting acceptance remains unresolved. Current behavior can be documented without converting implementation evidence into design approval. |
| `.codex/agents/chaosx_repo_explorer.toml` | Agent Nudger write guidance conflicted with the read-only role. | Proposed writes and their review/recovery requirements go to the parent or assigned implementation owner. The explorer remains read-only apart from its requested report. |
| `.codex/agents/chaosx_localisation_auditor.toml` | The patch list included mirrored spreadsheet wording. | The worker passes final localisation keys and wording to the spreadsheet owner and does not edit the workbook or export-only CSVs. |

Changed prose in these paragraphs uses sentence breaks in place of semicolons.
No new skill was created.
The existing `chaos-redux-subagents` skill was updated, and other skills were left unchanged.

## Disposition contract

The reusable guidance preserves all seven dispositions and their required basis:

- Implemented requires current implementation evidence and validation limits.
- Promoted into an accepted spec requires acceptance basis and a destination specification.
- Accepted and queued requires acceptance basis and a queue reason.
- Rejected requires the recorded decision and reason.
- Superseded requires a named replacement.
- Blocked requires the exact missing input, route, or dependency.
- Unresolved identifies the missing decision or evidence.

A spec location, date, status label, or old handoff cannot establish approval.
Existing implementation proves what exists and does not by itself establish accepted design.

## Reads and evidence

Fully read before editing:

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.codex/agents/chaosx_documentation_curator.toml`
- `.codex/agents/chaosx_repo_explorer.toml`
- `.codex/agents/chaosx_localisation_auditor.toml`
- `C:\Users\klimp\.codex\skills\.system\skill-creator\SKILL.md`

Fully read before the final review correction or validation:

- `docs/plans/README.md`
- `C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py`

Consulted the required offline wiki pages through their opening material and relevant introductory sections, without claiming a full read of the large engine references:
`paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`.
All abbreviated wiki filenames in this sentence are under `paradox_wiki/`.
Inspected the installed vanilla documentation directory and consulted the opening Script Concepts and Bindable Localization material in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md`.
No engine syntax or mechanics were changed.

The current `collaboration.spawn_agent` schema exposes `fork_turns` and accepts `none`.
It does not expose `fork_context`.
No subagents were spawned for this batch.

`ALL_TOOLS` exposes the HOI4 tool namespace and all three read-only technology routes named in the shared skill's MCP evidence section.
The route names were checked against metadata, including the technology inspection tool declaration.
This proves exposure only.
No MCP service health test or game-surface inspection was performed for these instruction-only edits.
No Agent Nudger or standalone Technology Tree Viewer route was found in the exposed tool-name inventory.
That inventory does not establish installed package absence.
The previous instruction claim that the Technology Tree Viewer was absent remains unverified, so updated guidance requires separate verification and records a confirmed absence as a package gap.

## Validation and protected changes

Compared each owned file against the parent's supplied dirty-baseline copy, whose hash matched the pre-edit file.
Reviewed the bounded diff and validated the revised skill with the official `quick_validate.py` script.
Parsed all three edited TOMLs with `tomli` and verified that every field outside `developer_instructions` remains byte-identical to baseline.
This includes names, descriptions, models, reasoning efforts, sandbox modes, and nickname candidates.

Verified these additional ranges byte-for-byte:

- AGENTS.md sections 1 through 10, including gameplay, source-policy, asset, validation, and Git rules.
- AGENTS.md's complete Dual-Runtime Workflow section.
- The subagents skill's pre-existing binary-resource transport and chunk-retrieval paragraphs.
- The subagents skill's provider/source policy paragraphs and complete Asset routing section.

The 3D routing prompt list retained every provider, source, paid-operation, and asset requirement.
Its only edits were the supported context argument and a sentence break in its no-inherited-context wording.
The final 3D ownership paragraph distinguishes parent review from user-run live validation.

Only the five assigned instruction files and this handoff were written by this worker.
No gameplay, localisation, asset, workbook, CSV, config, credentials, allowlists, or provider-policy files were edited.
No generators, runtime synchronization, commits, or game launches were run.

## Unresolved findings and parent integration

The AGENTS.md instruction to regenerate Qoder/Cursor definitions still conflicts with its instruction to leave those runtime trees untouched during a Codex session.
That conflict was deliberately left unresolved, and generated definitions were not synchronized.
The parent owns its final disposition and any later authorized synchronization.

Standalone viewer availability and live MCP service health remain unverified.
Tool metadata was not used as a substitute for either claim.
Paid-operation, source-policy, and model-policy conflicts outside this batch remain outside this worker's scope.

The parent owns root documentation indexes, final integration, final review, and any scoped commit.
No simplifications were made to the requested instruction repairs.
No repository-wide or gameplay completion claim is made.

## Baseline and final file hashes

Baseline root: `C:\Users\klimp\.codex\visualizations\2026\09\04\01a06e33-dc56-78e3-a787-850360234143\documentation_review\batch01_baseline\files`.

| File | Baseline SHA-256 | Final SHA-256 |
| --- | --- | --- |
| `AGENTS.md` | `fc9ec923378c547ae7841930f6a1e536c2aa0bc83944e03eeb933bc6f9726696` | `bfc79d363d9b59b084fc35cc883cbeb1ea74159203134cd2090104c925a9b4f5` |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | `a5d3717aa939bb73c10b8b81d91e224d7efb3a5408665506056597d4761327e4` | `1d3dd32607f643e9fede505bcde133fda56b8e0e270ae3b480ff1b1ce6ad34a2` |
| `.codex/agents/chaosx_documentation_curator.toml` | `c5d8ce5d7b1194762f41fa15384d35e39cba83ef95ab7bd06abad4b4461b5b98` | `ed5f3fedeeb3b175f384cb4869299cd9db7b88060779a588d94d83c2bbfdc7f5` |
| `.codex/agents/chaosx_repo_explorer.toml` | `1a6c78e901b5609955ee0c54ed2b9d905a260b813c8ef62c88ecf21444dc5304` | `276acf0305e8b2a1a9c2b6f60cc8153a9e5cd2d629dca85c592e834c9a65fd9a` |
| `.codex/agents/chaosx_localisation_auditor.toml` | `1a21ea25ec62710ce2272efd94771402ae454d891859a4cb1b713379572bbd36` | `8d588111bb27da851af9d16b8c426d6e9b59e517444464225e0a3e91385a161b` |

## Parent integration and runtime-configuration continuation

The bounded instruction repairs above were parent-reviewed and committed in `7cff54ad5522b2d9a4af6cde063a8028bbf4b8ac`.
The earlier review-status wording and final hashes describe that worker's handoff revision, not the current files after later authorized work.
The user subsequently supplied replacement AGENTS.md instructions naming `chaos-redux-scripted-gui` as the owner of GUI reference images and layout evidence.

The parent fully read the following four runtime files without editing them.
Both Cursor `MESHY_API_KEY` values are environment-variable placeholders, and no credential value was disclosed.

| Read-only file | Bytes | SHA-256 at review |
| --- | ---: | --- |
| `.codex/config.toml` | 11714 | `24bcac71960d42d2958fc98b49fd38a5244b0946bf80cf3ddb879a633c269427` |
| `.qoder/mcp.json` | 996 | `16890ca0e35251416c2c38627ef11d2a3561b1d94cd4c5b8d0598c77569d90ad` |
| `.cursor/mcp.json` | 1215 | `11fa02c71468690de1b0ffd5656132a47a16eaf18b5e6091ee10e61ecda22454` |
| `.cursor/rules/chaos-redux-cursor-runtime.mdc` | 1579 | `02b1ef33b03312945c6f457f37365ffb5b0e0452641aebe090cde49163dcfa15` |

All 20 Codex role registrations point to existing canonical TOMLs.
The configured production wrapper files exist, and `hoi4-agent-tools.cmd` resolves to the installed npm command path also named by Qoder and Cursor.
These checks establish registration and file resolution, not startup success, service health, provider access, or a standalone viewer.
The three runtimes register the same named production services, while the disabled development Blender route remains Codex-only.

Protected follow-up items:

- `.cursor/rules/chaos-redux-cursor-runtime.mdc` still names missing `.tools/sync_cursor_agents.py`. The existing generator is `.tools/sync/sync_cursor_agents.py`. The Cursor runtime-rule owner must apply that path correction under its runtime's write authority.
- `.codex/config.toml` describes `chaosx_event_ui_worker` using the older decision-layout ownership wording, while the replacement AGENTS.md assigns the GUI contract to `chaos-redux-scripted-gui`. The registration description needs a configuration-owner correction.
- The same Codex config describes extra failure-driven paid recovery as requiring confirmation and gives image-to-3D its own approval setting. AGENTS.md's preauthorization language differs. This cleanup preserves the configuration and records the authority decision needed, rather than changing paid-work or approval policy.
- Cross-runtime synchronization remains blocked by the conflicting destination-write instructions already recorded above. Neither generated tree was edited or regenerated.

No model, reasoning, sandbox, approval, credential, server allowlist, provider policy, runtime rule, or MCP configuration changed during this read-only continuation.
