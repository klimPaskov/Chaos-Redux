# GUI workflow instruction review

Date: 2026-09-05.
Disposition: implemented as a read-only instruction audit, reviewed by the parent.
Acceptance basis: the parent authorized bounded review of the GUI owner skill and event UI worker instruction body against the user's replacement AGENTS.md, with repairs limited to concrete non-policy defects.
The previously excluded full-read boundary is closed for both named sources and the required cross-skill inputs.
No source repair is justified, so both owned instruction files remain byte-identical to the continuation02 baselines.

## Findings and invariants

- chaos-redux-scripted-gui consistently owns reference-first composition, native mapping, layout budgets, visual review, and MCP evidence.
The decision skill retains presentation-layer choice, gameplay action integrity, payment, AI, cleanup, and balance.
- The worker remains restricted to a dedicated interface introduced and owned by a named event.
Shared interfaces remain parent-owned.
- Reference paths and acceptance basis must precede implementation.
Document existence does not establish acceptance.
Native controls and dynamic information cannot be replaced with flattened art.
- Direct reviewed source edits and optional rewrite remain compatible with mandatory before/after inspection, rendering, matched scenarios, and preserved artifacts.
The one-to-one production-render gate remains intact.
A passing tool result cannot waive visible defects.
- The linked visual-review file exists and covers painted/logical/glyph/click bounds, background mapping, state coherence, scenario coverage, and usability.
The cited vanilla meter files and scripted-GUI documentation support the described separation of presentation consumers.
- No skill, worker prompt, runtime setting, gameplay file, localisation, asset, workbook, generated agent, or configuration was edited.
Only this handoff was created.
No commit or synchronization was run.
The two owned sources and the visual-review reference already had Git modifications when inspected, and those pre-existing changes were preserved.

## Actual MCP evidence

The current tool catalog exposes exactly these GUI calls:

| Coding-agent name | Registered server name |
| --- | --- |
| mcp__hoi4_agent_tools__hoi4_gui_inspect | hoi4.gui_inspect |
| mcp__hoi4_agent_tools__hoi4_gui_render | hoi4.gui_render |
| mcp__hoi4_agent_tools__hoi4_gui_rewrite | hoi4.gui_rewrite |

No separate gui_compare route is exposed or registered in the inspected GUI registration module.
gui_render exposes comparisonScenario, scenario, relatedScenarios, generatedScenarios, states, and resolutions.
It does not imply access to older source snapshots.

The Codex registration names hoi4-agent-tools.cmd.
Get-Command resolves that shim to C:\Users\klimp\AppData\Roaming\npm\hoi4-agent-tools.cmd.
The shim points to C:\Users\klimp\AppData\Local\hoi4-agent-tools\3.0.8\node_modules\hoi4-agent-tools\dist\bin\stdio.js.
The installed package declares version 3.0.8.

Package evidence confirms the skill's detailed claims:

- dist\hoi4_agent_tools\mcp\tools\gui.js:114 requires windowName and scenario together for narrow inspection.
The same module registers the three routes and rejects expectedSourceHash outside patches mode.
- dist\hoi4_agent_tools\gui\scenario.js:96 defines the strict scenario contract, including elementStates and visible/hidden/containedBy/centeredOn expectations.
An invented fixtureChoices field is absent.
- dist\hoi4_agent_tools\gui\validators.js:181 uses visual text bounds for centering comparisons.
- docs\gui.md documents seeded generated scenarios, disabling generation for explicit fixtures, and UI scale as the game setting.
- dist\hoi4_agent_tools\gui\source-patch.js:58 permits safe scalar replacements and complete insertions at parsed block closes.
The skill's conservative scalar-replacement guidance is valid and does not need expansion during this review.

list_mcp_resources for hoi4_agent_tools returned an empty resource list.
list_mcp_resource_templates returned the artifact template with byte-range selectors and continuation metadata.
These responses establish resource discovery availability only.
No GUI inspect, render, or rewrite request was executed because this task changed no GUI surface.
GUI service execution health, native render quality, runtime fixture completeness, and live-game behavior remain untested.
No visual or engine completion claim is made.

Standalone Technology Tree Viewer availability was checked separately at the inspected package boundary.
The package exposes only stdio.js, http.js, and setup.js bin entries.
Its technology documentation describes read-only analysis and optional static HTML render reports.
No dedicated standalone Technology Tree Viewer launcher was found in this package, which remains a package gap.
This does not establish machine-wide absence or technology service health.
The exposed mcp__hoi4_agent_tools__hoi4_tech_inspect, mcp__hoi4_agent_tools__hoi4_tech_render, and mcp__hoi4_agent_tools__hoi4_tech_compare tools do not close that gap.

## Read ledger

Paths beginning R\ are relative to the repository root below.
P\ identifies the installed package root, V\ the vanilla game root, and B\ the continuation02 baseline root.
Hashes are SHA-256 of exact observed file bytes.
Full-read entries were read completely, with explicit follow-up chunks where tool output had been truncated.
Partial references identify their actual consulted range or search scope.
The two baseline files were confirmed byte-identical to their completely read current counterparts.

- R: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux
- P: C:\Users\klimp\AppData\Local\hoi4-agent-tools\3.0.8\node_modules\hoi4-agent-tools
- V: C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV
- B: C:\Users\klimp\.codex\visualizations\2026\09\04\01a06e33-dc56-78e3-a787-850360234143\documentation_review\continuation02\baseline

| Read path | Coverage | SHA-256 |
| --- | --- | --- |
| R\AGENTS.md | full | 63FB71F94192F90B7D3BFFFC9F9B2EA6F51B5F69D1A9969F257D3098B391EB52 |
| R\.agents\skills\chaos-redux-scripted-gui\SKILL.md | full | BC8D879FB806DBE0CE10294AF516CF646855423789C911730353BD48BAB70C5A |
| R\.codex\agents\chaosx_event_ui_worker.toml | full | 988CC8AFB24F565BD341996EC9D92A981690A77D81B6932C2C55D27B2A35986F |
| R\.agents\skills\chaos-redux-subagents\SKILL.md | full | 7A9CA4CFA5EC0E1AFC633073257D02D2A13CD6E521718118E9AC0BB4DF416B01 |
| R\.agents\skills\chaos-redux-decisions-missions\SKILL.md | full | 3B01B9F2DF26C861F725CB3E61E118F99F5BD164D2F00CA2AC530F43D9A4A2BA |
| R\.agents\skills\chaos-redux-events\SKILL.md | full | D8087AE19188354786804CE69F3B78010F81711264BA038D4CBDAA13016E2748 |
| R\.agents\skills\chaos-redux-scripted-gui\references\visual-review.md | full, read-only dependency | E0AEB1066A5AED568818B20A7DEEE0644F6FD1EC52BF4F597C35EA084782D070 |
| C:\Users\klimp\.codex\skills\.system\skill-creator\SKILL.md | full | CCCD291077EC57C6F50CA6529F0F3FB93212DA09473EFFB2FCEC808E81B21288 |
| B\.agents\skills\chaos-redux-scripted-gui\SKILL.md | byte-identical baseline | BC8D879FB806DBE0CE10294AF516CF646855423789C911730353BD48BAB70C5A |
| B\.codex\agents\chaosx_event_ui_worker.toml | byte-identical baseline | 988CC8AFB24F565BD341996EC9D92A981690A77D81B6932C2C55D27B2A35986F |
| R\.codex\config.toml | registration lines 11-15 and route-name search only | 24BCAC71960D42D2958FC98B49FD38A5244B0946BF80CF3DDB879A633C269427 |
| C:\Users\klimp\AppData\Roaming\npm\hoi4-agent-tools.cmd | full | E01529F70E9B04B5AEED13F6192086979C9EB8FEF3072F0C79833030B30D1563 |
| P\package.json | full | 025F08DEE731D69996DE45AD3BAC56ECA1869269782CAF40DDD85093773C83EE |
| P\docs\gui.md | full | 8345805D134D9BA906AE5162E0E4D5457AF196551F141FE2BAEDFF9E6303C129 |
| P\dist\hoi4_agent_tools\mcp\tools\gui.js | 104-198 and 411-487, route/schema searches | 67160712D5F3062D7E931440B419065A69640F27BDD29A416190FD19148A079F |
| P\dist\hoi4_agent_tools\gui\scenario.js | 91-170 | 4443685E7D1D83DCC1D9BB26BF70BE800625678D94E2FE1B7921BB9316EED204 |
| P\dist\hoi4_agent_tools\gui\validators.js | 176-223 | 101600834891516F185158FB3286A25350566213A6F012492BE0771D2457DF73 |
| P\dist\hoi4_agent_tools\gui\studio.js | 1076-1140 and schema searches | A7F1920656183BED7A3DDFD2E3659C52F371D4643EED5D06AA3CD66EA0841826 |
| P\dist\hoi4_agent_tools\gui\source-patch.js | 58-end | F7B398E2AF62E8AE320F41212447C1F70A26F37170EF631426716ED84EB0AC23 |
| P\docs\technology.md | 48-68 and viewer/render searches | C6F29B908C488798F40CDE9376C011C3023511B5B9C29C99C7D0845320F4996F |
| V\common\scripted_guis\_documentation.md | full | 43CE647FC5FDE27488855B060B5463C790E5E356149FCEB010D36B960B40F838 |
| V\documentation\script_concept_documentation.md | 1-50 and GUI/localisation search | 884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7 |
| V\documentation\loc_formatter_documentation.md | 1-50 | 1FBD9A031FD09100D79BAC08DEC3C16E19468F23516C5E67C67578156282AF08 |
| V\documentation\loc_objects_documentation.md | 1-35 | A5D06DA0B42E615FA0C40D0103D9125ED68A7691778E20C0315ACA7C82822C81 |
| V\interface\sov_paranoia_system_scripted_gui.gui | 1-60 | B8925BF8DAF88BA82E6CE66F7B5131CAE7083E6EDA5367E2CF2B6EAEF6310A85 |
| V\common\scripted_guis\SOV_paranoia_system_scripted_gui.txt | 1-75 | 00DB231BF1D3183520E8E980B3433D5E5678A101849F96C17625D6B9384D85C5 |
| R\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | 7E5E5369DAD08240B61EAC1126823087335AACD7230C6294F5A7F8AD3C4D4F38 |
| R\paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | 035E5FD34130E6E3AE74821C59E9134E156E4B548A3525B973978AD0BD75578F |
| R\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | 166DB8E2BE659269D8FA236D28C85F3A9EBB9AFAB0587C655CCF50AD71BF5F7A |
| R\paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | 78DCC5C2BF72A17B846EF47D4B80D8DB207091F89409ED7A21725E27AC2D701D |
| R\paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | 9B38E45FA70BAB7B166F78EDCF048877230F5D3AA7ED5FC25A71CE8FCD7E9003 |
| R\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | 64633D8033D36DF8E2B9B3AEC8D430D07C4D89175EA711148E8189E6E093F844 |
| R\paradox_wiki\On actions - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | 79A94B07D9E69844EAED6F05DAB3C2F351ECE6451C500408302DD847D62C5078 |
| R\paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | E41428E9CD928DF07E67D2D08FF37A07AC7B75DC9B57918FF7D26BE6C7BFD2AA |
| R\paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | CF5B2C91791AAEAA69B7A1869D876D781B238B4111425B05682D9DCF63B0AB5B |
| R\paradox_wiki\Idea modding - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | EA445094EF98807EC29286FC095081B40F2D76AA576A6E9F27C863433FBB9DDD |
| R\paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md | 1-25, required reference opening | 1EDC5FF8E5C10916B18EE780B495A199FEA113C5689D3C71D2F19F9F2CF560BB |
| R\paradox_wiki\Interface modding - Hearts of Iron 4 Wiki.md | 1-110 | 237A1678A4B84125FDCFB47CEA49BEE39123A8609499ED71A3FCA0F276A3768E |
| R\paradox_wiki\Scripted GUI modding - Hearts of Iron 4 Wiki.md | 1-90 | C76F6DDACA15575297991D92E53DD9F36138B98C358064F21E82052383D8D702 |

## Dispositions, limits, and next paths

| Document | Disposition | Evidence or next action |
| --- | --- | --- |
| .agents/skills/chaos-redux-scripted-gui/SKILL.md | implemented review, unchanged | Complete read and installed contract checks above. |
| .codex/agents/chaosx_event_ui_worker.toml | implemented review, unchanged | Complete read, event boundary and owner-skill agreement. |
| This handoff | implemented audit, parent-reviewed | Close the named excluded-read boundary in docs/plans/repo_cleanup/documentation_state.md after parent review. |

The runtime synchronization policy remains unresolved.
AGENTS.md calls for generating Qoder/Cursor definitions from TOML while also prohibiting Codex writes to those destinations.
No synchronization was attempted.
Any future prompt propagation must resolve that destination-write conflict explicitly before running .tools\sync\sync_qoder_agents.py or .tools\sync\sync_cursor_agents.py.

The parent separately reported stale GUI wording in .codex\config.toml and a stale sync command in the Cursor runtime rule.
These protected configuration findings were not repaired or independently audited here beyond the narrow Codex route registration check.
Return them to the parent's runtime-configuration review.
No policy, approval, provider, model, reasoning, permission, or source rules were changed.

Patch readiness: no owned-source patch is required or staged by this worker.
The parent reviewed this handoff and accepted the bounded instruction-audit result without any GUI or engine completion claim.
Skills used: skill-creator and the four named repository skills, with the GUI visual-review reference consulted.
Skills created or updated: none.
No requested instruction behavior was simplified or omitted.
Service execution and visual/live-game evidence remain unverified within this instruction-only audit.

## Prose-only follow-up, parent-reviewed

Date: 2026-09-05.
Disposition: implemented prose cleanup, reviewed by the parent.
Acceptance basis: the parent explicitly authorized applying the user's no-authored-semicolons-or-em-dashes rule to the original GUI skill and the worker's developer_instructions text.
The parent-reviewed technical audit above remains accepted.
Its unchanged-file statements and original hash ledger describe the initial audit checkpoint.
This follow-up supersedes those statements only for the two prose-edited files.

| Changed surface | Exact prose-only change against continuation02 baseline | Final SHA-256 |
| --- | --- | --- |
| .agents/skills/chaos-redux-scripted-gui/SKILL.md | Replaced 25 prose semicolons with sentence boundaries and removed four trailing list semicolons. Capitalized new sentence starts and preserved list continuation indentation. Original affected lines: 9, 17, 18, 28, 29, 34, 39-42, 47, 52, 54, 64, 65, 72, 75, 77, 78, 80, 81, 85, 91, 98, 102, 103, 106, 116, 118. | 6BDA7E4671F3DD065F476E9112A09A0EC97AC0A24C5763EB92870E6006661731 |
| .codex/agents/chaosx_event_ui_worker.toml, developer_instructions only | Replaced ten prose semicolons with sentence boundaries, capitalized new sentence starts, and preserved numbered/bulleted continuation structure. Original affected lines: 32, 33, 38-40, 45-48, 62. | 56A254896FAF78E4C6CA5AA6398FA5AC6B7106EC6BDC6F0EFE767ACFA879032C |
| This handoff | Appended this follow-up with separate review status. | Not self-hashed. |

No em dash occurred in either edited surface.
The complete ordered word sequences match the baselines after case normalization.
All inline code spans match exactly.
The TOML prefix and suffix outside developer_instructions remain byte-identical.
The visual-review dependency retains SHA-256 E0AEB1066A5AED568818B20A7DEEE0644F6FD1EC52BF4F597C35EA084782D070.
Reference-first acceptance, scope boundaries, provider and source policies, optional rewrite behavior, mandatory inspect/render evidence, one-to-one visual gates, gameplay ownership, limits, identifiers, paths, examples, and quoted literals retain their meanings and values.

Reviewed the complete diffs against both continuation02 baselines.
The official skill-creator quick_validate.py command returned "Skill is valid!" for the changed GUI skill.
A validation helper initially stopped before writes because the default Python lacks tomllib.
The completed check instead compared the unchanged TOML prefix and suffix directly, which verifies the granted edit boundary without depending on a parser.
No new package, service, render, or live-game checks were performed.

The top-level TOML description still contains a semicolon because the parent explicitly restricted this pass to developer_instructions and required preserving external fields.
The visual-review dependency remains read-only, including its existing prose punctuation.
These exclusions require parent-owned scope decisions for any further style pass.

Skills updated: chaos-redux-scripted-gui.
No skill was created.
Worker prompt updated: developer_instructions of chaosx_event_ui_worker only.
No instruction simplification, policy change, runtime synchronization, or commit was made.
The parent reviewed both complete diffs and independently verified the ordered words, inline code, and parsed TOML fields outside developer_instructions against the captured baselines.
The prose-only follow-up is accepted within the user-authorized cleanup scope.
