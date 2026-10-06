# Event 023 reference and source evidence

Only offline wiki and installed vanilla documentation were used for engine syntax.
The connected `hoi4.reference_context`, `reference_search`, `reference_read`, `source_lookup`, event, decision, probability and `script_validate` schemas were exposed.
Exposure alone does not prove service health or executed engine behavior.
No independent connected server version or desktop viewer availability was confirmed.
No `refresh = true`, whole-repository state-flow or helper-expansion query was used.

| Read reference | Lines | Source revision returned by MCP |
| --- | --- | --- |
| Installed `documentation/effects_documentation.md`, random_list | 5413?5432 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, random effects | 4518?4557 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, missions | 465?479 | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| Installed `documentation/script_concept_documentation.md`, Script Constants | 216?222 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common/script_constants/documentation.md`, mandatory first schema | 1?34 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |

The initial event context omitted Triggers and On actions under its limit.
Those were read at exact reactor/control/callback sections by the reactor worker, with citations and delivery gaps in `subagent_handoffs/reactors_20261006.md`.
Targeted event-modification reading used the local Event modding snapshot lines 24?35 for recipient ROOT, carried event targets and sender FROM semantics.
Local Decision modding lines 303?326 establish the custom-cost trigger/text/tooltip contract.
Installed `common/decisions/CHI_decisions.txt:6454` is the native `days_mission_timeout = var:CHI_improving_neglected_countryside_mission_time` precedent, with its surrounding timeout block read directly.
`hoi4.source_lookup` returned the CHI flying-tigers decision definition at game path `common/decisions/CHI_decisions.txt:3654?3673`, source index revision `a874904e876d8d45494aae78a9f10a31e7bb854436fc3e59e8c2d786f5978ef1`.

The installed `set_country_flag` section at `documentation/effects_documentation.md:6730?6738` confirms country scope but does not settle variable-duration parsing.
This pass therefore follows the existing documented Event 23 meta-effect literal-day pattern for service flags instead of assuming a variable token is accepted.
The full file hashes below identify these local fallback reads.

- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`: SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`: SHA-256 `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`: SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/CHI_decisions.txt`: SHA-256 `efcec834a71901a5da66eef97f8b817d1b7299c36f16e48893ff9f3918039068`.

## MCP coverage limits

Parent entry trace returned `EVENT_INSPECTED_PARTIAL`, `analysisMode = focused`, revision `3eacffa45860dba3e66b6bce34d52e3370164de7ff6c0cb291f3206b359173cc`, graph hash `184339ba0021043259f0493c01b90a2ccdf0fea902c3efdae20ff1a23e6cdde6`, with no expanded helpers and one blocking global diagnostic.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fef438248834f8526a20cb81998ae80d80886da82a32b3d4ea88e4cde4712a01/ef7e016dc9094979b1724a2d3fe84f074efdda8c16d08dfea08bfd8148af30a5/event-trace-3eacffa45860.json`.
Focused entry evidence does not validate the full helper lifecycle.
Localisation and completion handoffs retain their narrow render/compare artifacts or unreturned-route limits.
Probability evidence and frozen source identities belong to `subagent_handoffs/probability_20261006.md`.
`script_validate`?s live metadata did not show its limit maximum, and an initial limit 40 request was rejected with maximum 32.
The parent corrected it and requested every changed event, decision, effect, trigger and on-action file at limit 32.
Final returned checks, unresolved findings and any unreturned requests are retained in the validation evidence and takeover status, without claiming engine execution.

Skills applied: events, decisions/missions, event-assets, subagents and shared-git-commit.
The source specification explicitly excludes a new focus tree, country, portrait, model or scripted GUI, and no such surface was added or changed.
No skill file or workbook/export was edited by this pass.

The parent found a localisation pointer defect in the first localisation handoff: custom normal-variable scopes require the question-mark prefix, unlike regular event targets.
Offline `Data structures - Hearts of Iron 4 Wiki.md:492?496` explicitly requires `[?country_variable.GetName]`.
Installed `localisation/english/aat_decisions_l_english.yml:399?415` uses `[?DEN.DEN_overlord_nation.GetNameDef]` and `[?DEN.hosts_danish_brigades.GetNameDefCap]` as exact current-engine precedents.
News 231/232 use `[?SOV.sov_nuclear_bombs_news_threat_country.GetNameDef]` and equivalent state/strike variables.
Successor news retains regular carried event targets without a question mark.

## Final validation interpretation

The whole-file validator returned `SCRIPT_CHECKED` for both Event 023 event files and `SCRIPT_CHECK_PARTIAL` for the effect/trigger/decision/on-action families.
Its final cost-aligned decision read checked 1,561 commands, returned no findings, and explicitly left 102 native argument blocks and 15 unknown-scope roots outside complete proof.
The event-effects whole-file warning names the pre-existing static character scope `KRG_warren_kruger` in the Event 16 milestone bridge.
The character is defined in `common/characters/016_brilliant_scientist_characters.txt:11`.
A separate exact snippet with that declared character binding returned `SCRIPT_CHECKED`, `valid = true`, zero unresolved findings and no unchecked argument blocks, citing installed `has_character_flag` at lines 3422?3437.
This resolves the command-kind/scope question for that bridge without claiming a live character roster result.
Other file checks have no concrete findings, but `valid = null`, unknown root scopes and unchecked argument blocks remain material coverage limits.
`script_validation_20261006.json` and `script_validation_final_20261006.json` retain the returned checks.
Malformed limit/binding requests were corrected, and their validation errors are not treated as engine evidence.
The final source hash inventory identifies the exact owned files committed after the adversarial corrections.
The report-color audit returns zero literal color keys, and the parent also removed automatic colored delta formatting from technical report descriptions.
