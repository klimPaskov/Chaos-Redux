# Famine takeover reference and source evidence

The complete takeover history was read in audit/implementation/review order, including the last round-3 audit.
The 18 static inbox defects and both dated live findings were traced separately from the older fix-results report.
`thread_final_status.json` has an empty famine `last` field and supplies no additional verdict.
The older `fix:famine` and `review:famine` entries describe working-tree fixes later published by rounds 1 and 2, and cannot replace current source review.

## Reference route limits

The root agent's callable tool inventory contains no `hoi4-agent-tools` routes.
The Luna specialist inventories do expose reference, decision, GUI, and probability routes.
Their actual bounded reference, GUI, and probability call outcomes are retained in the takeover status.
Local section reads below are reference evidence, not MCP execution or engine validation.
No online Paradox wiki was used.

## Direct sections read

Installed game root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`.
Offline wiki root: repository `paradox_wiki/`, snapshot captured 2026-09-19.

| Source | Lines read for this pass | SHA-256 |
| --- | --- | --- |
| Installed `documentation/triggers_documentation.md` | 1497-1505 (`any_neighbor_state`), 2110-2137 (`check_variable`), 4665-4673 (`has_resistance`), 5051-5059 (`has_war_with`), 5390-5398 (`is_core_of`) | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation/effects_documentation.md` | 2681-2704 (`clamp_temp_variable`), 7820-7841 (`set_temp_variable`) | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation/script_concept_documentation.md` | 216-247 (script constants) | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common/script_constants/documentation.md` | 1-73 (schema and examples) | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Installed `common/scripted_effects/SOV_scripted_effects.txt` | 618-644 (caller-created temporary state before nested work) | `cc9e16837afa1428d11e053dc982446b35587980daa011a1df12114c3ace2bf4` |
| Offline `Data structures - Hearts of Iron 4 Wiki.md` | 425-472 (variable precision, helper lifetime, regular versus temporary scope) | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `Scopes - Hearts of Iron 4 Wiki.md` | 811-848 (`PREV` nesting) | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Offline `Decision modding - Hearts of Iron 4 Wiki.md` | 268-278 (selection), 357-374 (AI willingness) | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| Offline `Localisation - Hearts of Iron 4 Wiki.md` | 44-80 (language header, keys, BOM) | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| Offline `Console commands - Hearts of Iron 4 Wiki.md` | 168-170 (`eval_trigger`, `eval_effect`) | `93206f1ccd110b9d0e0ce60a064309608318eac75aa81ddf3d536aeb03e6fca3` |

The installed `common/decisions/documentation.md` path is absent.
Decision source and installed effects/triggers documentation were read directly instead of claiming coverage of that missing file.
The repository's localisation key format takes precedence over the wiki's legacy numbered example.

## Save evidence

Commands: bundled save inspector `info` and scoped `find` on `countries/USA`.
File: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/save games/qa_001_fresh_head.hoi4`.
Header: `HOI4txt`, 102.3 MiB, player USA, democratic, normal difficulty, date `1936.1.1.12`, installed version `Operation Postern v1.19.2.0.a729 (2bce)`.
The scoped search for famine, migration cohort, and cannibalism scenario/manual state returns no USA matches.
This establishes a usable baseline for the named checks, not a current implementation acceptance run.
No save was modified or placed in Git.

## Director-authorized publication follow-up

The root agent's current inventory exposes `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` with their live schemas.
The earlier root-inventory gap above describes the preceding pass only.
No health/version or client-task-negotiation route is exposed, so no helper expansion or native MCP task was submitted.

The bounded `reference_search` query `PREV`, sources `game_doc` and `wiki`, limit 4, returned `OK` with offline Scopes revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`, section 811-872 and answering line 811.
It also returned the single-line Scopes entry at line 262 and Effects/Triggers entries at lines 267/262, with exact revision-bound IDs.
The limit omitted other search matches, so this search is not represented as full installed-document coverage.
The accompanying general `reference_context` (limit 6, exact state food dates/temp returns/nested PREV question) and `source_lookup` for `famine_open_outbreak_food_context` (one definition, 24 lines, no references) stayed pending and were caller-terminated.
The follow-up `reference_read` of Scopes 811-872 with that revision and a separate installed-doc search for `global.date` also stayed pending and were caller-terminated.
Those routes yielded no source artifact or detailed-read result.

Direct sections read in this follow-up: the same installed script-constants schema and concept sections at lines 1-73 and 216-247, installed `set_temp_variable` at 7820-7842, `any_neighbor_state` at 1497-1506, `has_war_with` at 5051-5061, and `is_core_of` at 5390-5400.
Offline Data structures lines 425-473 and Scopes lines 811-852 were read directly for temporary lifetime and nested PREV.
Their exact paths and SHA-256 revisions are retained in the table above.
Installed `common/scripted_effects/SOV_scripted_effects.txt` lines 1674-1687 use `PREV.skill_level` inside a country scope entered from a selected leader, demonstrating immediate-parent attribution independent of chain ROOT.
Its SHA-256 is the same source revision retained in the table.

All five director-assigned gameplay diffs were reviewed in full, including context tuning schema, selector/mapper call sites, local-war output storage, date retirement, transition clock cleanup, positive-loss mortality dispatch, and every changed achievement PREV comparison.
Independent review is retained in `subagent_handoffs/round3_publication_audit_20261006.md`.
The parent's two added source tests execute the six actual state-to-country recorders with an unrelated chain ROOT and stale-generation rejection, and the actual concealment dispatch with zero/positive measured loss and distinct controller matching.
The fixture supplies the installed engine's built-in `id` from the current scope.
An initial failed run exposed that missing fixture fact, which was repaired in the fixture without changing gameplay.
All nine bounded production-source tests then pass.
The audit handoff's seven-test result and missing-document statements are time-bound observations made before these parent additions.
Permanent context, cause-gate, and achievement documentation is published with the five gameplay drafts.
