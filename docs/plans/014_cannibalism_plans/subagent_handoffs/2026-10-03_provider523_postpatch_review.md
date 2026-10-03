# Provider 523 postpatch review, 2026-10-03

Disposition: **PASS for this bounded source review**.
The parent repair resolves E014-COMP-01's invalid grid and mismatched ledger coordinates.
No remaining implementation defect was found in the requested grid, ledger, integer meta expansion, or aggregate obligations.
This is not engine-runtime acceptance or Event 014 completion.
The original `2026-10-03_event014_completion_resume_audit.md` remains an unchanged historical prepatch checkpoint.
After the independent checks, the parent handoff `2026-10-03_provider523_template_repair.md` and receipt `docs/plans/014_cannibalism_plans/evidence/2026-10-03_provider523_template_repair.json` were reviewed for consistency.
The receipt SHA-256 is `0e2c8c5943da8d50004f4f6a72b0067f625a92f3d67ec1f630bebd6b31afa2f4`.
Its current source hashes, nine placements, ledger sequence, group columns, native limits, and aggregate totals agree with this independent review, and its evidence limit remains source expansion rather than live acceptance.

## Scope and ownership

The user authorized a narrow read-only review of the parent-owned repair in `common/scripted_effects/014_cannibalism_effects.txt` and `common/script_constants/014_cannibalism_constants.txt`.
Only this new handoff was written by the reviewer.
No gameplay or asset file was edited, no commit was made, no model work was reopened, and no HOI4 launch or runtime-log request/search was performed.
The existing broader portrait, documentation, probability, GUI, and live-consumer gates are outside this postpatch review.

## Source evidence

- `common/script_constants/014_cannibalism_constants.txt:3656-3670`: one `fixed_point` schema and eight integral layout constants.
- `common/scripted_effects/014_cannibalism_effects.txt:19659-19666`: all eight constants are loaded into unscoped temporary variables before meta expansion.
- Effects lines 19667-19696: existing `meta_effect` binds each named placeholder through `[?temporary_variable|.0]`.
- Effects lines 19675-19683: the nine native regiment placements.
- Effects lines 19697-19720: nine component-ledger appends using those same temporary values.
- Effects lines 19727-19743: the unchanged aggregate sustainment callback.
- `common/script_constants/014_cannibalism_constants.txt:3632-3653`: unchanged provider/family ID 523, count 9, obligations, and AI weight.
- `common/units/014_cannibalism_irregular_infantry.txt`: current nine unit definitions and their group/manpower/equipment values.
- `common/scripted_effects/019_infantry_spawn_ledger_effects.txt:456-466`: the consumer stores the current column and row on every append.
- Shared ledger lines 743-758 and 793-802: obligation amount is component count times supplied amount, then the corresponding existing start factor is applied.

## Nine-family grid and exact ledger order

The table is the native template order and the actual append order.
The ledger uses combat slot kind and family profile 523 for all nine components.

| Order | Family | Column,row | Group | Template line | Ledger append line | Manpower | Infantry equipment | Motorized |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `cannibal_scavenger_warband` | 0,0 | infantry | 19675 | 19701 | 900 | 100 | 0 |
| 2 | `cannibal_feast_guard` | 0,1 | infantry | 19676 | 19703 | 850 | 100 | 0 |
| 3 | `cannibal_feast_cohort` | 0,2 | infantry | 19677 | 19705 | 1000 | 100 | 0 |
| 4 | `cannibal_bone_guard` | 0,3 | infantry | 19678 | 19707 | 700 | 100 | 0 |
| 5 | `cannibal_bone_riders` | 2,0 | mobile | 19679 | 19710 | 800 | 140 | 0 |
| 6 | `cannibal_island_reavers` | 0,4 | infantry | 19680 | 19713 | 900 | 150 | 0 |
| 7 | `cannibal_siege_eaters` | 1,0 | infantry | 19681 | 19716 | 900 | 100 | 0 |
| 8 | `cannibal_march_predation_column` | 1,1 | infantry | 19682 | 19718 | 800 | 100 | 35 |
| 9 | `cannibal_network_cadre` | 1,2 | infantry | 19683 | 19720 | 500 | 100 | 0 |
| Total | Nine bodies | Nine distinct cells | Two infantry columns, one mobile column | | | 7350 | 990 | 35 |

All coordinates are integral and within the installed 5 by 5 native grid.
Columns 0 and 1 contain infantry-group bodies only.
Column 2 contains the mobile Bone Riders only.
There are no duplicates, missing family tokens, mixed-group columns, or row-5 placements.

The ledger tuple sequence is exactly:
`[(0,0), (0,1), (0,2), (0,3), (2,0), (0,4), (1,0), (1,1), (1,2)]`.
All nine template coordinates equal the corresponding ledger coordinates in order.
The reset to primary column 0 before Island Reavers at effects lines 19711-19712 is present, so the mobile column does not leak into the next component.

Only two coordinates differ from the prepatch baseline:
Bone Riders moves from 0,4 to 2,0, and Island Reavers moves from 0,5 to 0,4.
The other seven coordinates and all nine family ordering positions are preserved.

## Expanded integer meta syntax

Current layout constants are primary column 0, secondary column 1, mobile column 2, and row values 0, 1, 2, 3, 4.
All eight constants have integral current values under the `fixed_point` schema.
All eight bindings use `|.0`, so expansion supplies integer text rather than decimal coordinate tokens.
There is no `ROOT.` or `PREV.` prefix on the temporary variables.

The following expansion was derived read-only from the actual constant-to-temp and temp-to-placeholder bindings.
UID 523001 is an explicitly chosen audit example for the unchanged caller-supplied template UID.
It is not a runtime observation.

```text
division_template = {
	name = "Cannibal Irregular Muster 523001"
	is_locked = yes
	force_allow_recruiting = no
	priority = 0
	regiments = {
		cannibal_scavenger_warband = { x = 0 y = 0 }
		cannibal_feast_guard = { x = 0 y = 1 }
		cannibal_feast_cohort = { x = 0 y = 2 }
		cannibal_bone_guard = { x = 0 y = 3 }
		cannibal_bone_riders = { x = 2 y = 0 }
		cannibal_island_reavers = { x = 0 y = 4 }
		cannibal_siege_eaters = { x = 1 y = 0 }
		cannibal_march_predation_column = { x = 1 y = 1 }
		cannibal_network_cadre = { x = 1 y = 2 }
	}
}
```

The expanded native body has nine literal integer x/y pairs and no unbound uppercase placeholders.
The template lock, recruiting restriction, priority, name pattern, and consumer call structure remain unchanged.
The same temporary values feed the ledger without rounding, and they match the rendered integer tokens because all current constants are integral.
Future layout tuning must preserve that integrality.

## Aggregate obligations and patch scope

The nine unit definitions sum to 7,350 manpower, 990 infantry equipment, and 35 motorized equipment.
These equal the provider's `template_manpower`, `template_infantry_equipment`, and `template_motorized_equipment` at constants lines 3650-3652.
The combat count remains nine at line 3649.

The unchanged callback uses `component_count = 1` with the complete muster totals.
It queues three aggregate obligations, rather than multiplying each complete total by nine.
Manpower retains the manpower scaling kind and both equipment rows retain equipment scaling.
The shared consumer applies the existing start-manpower/start-equipment factors, so these are full-strength base obligations, not an assertion of issued runtime amounts under an undeclared scenario.

Read-only comparison with the parent Git baseline confirmed that the effects file differs only inside `chaos_unit_family_provider_523_event19_build_template`.
The sustainment callback and all other effects remain text-identical after newline normalization.
The constants change adds only the layout category and comment, preserving all original constant content after trailing-whitespace normalization.
No provider/family/equipment/manpower/AI weight, eligibility, payment, management, cleanup, or model binding changes were found in this repair.
The installed unit-definition source identity remains unchanged from the prepatch audit.

## Meaningful verification performed

A single read-only in-memory Python review:
- Resolved all eight layout constants and verified their integral values.
- Verified all eight temporary assignments and nine meta bindings, including the existing UID binding.
- Expanded the native template, then checked nine unique in-bounds cells against actual unit groups.
- Interpreted the component column/row assignments and verified all nine appends against the exact template order.
- Cross-checked the nine template tokens against all nine Event 014 unit definitions.
- Recomputed per-family manpower/equipment totals and compared them with the unchanged aggregate callback and provider constants.
- Compared the parent baseline to confirm only the two intended placements change and only the build-template body/layout category is edited.

No scratch script or generated gameplay source was written.
No engine execution or runtime parser success is inferred from these checks.

## Fresh MCP attempts and limits

Connected live schemas were checked for source lookup, reference search, event inspect, event render, and event compare.
`hoi4.script_validate` is not exposed in the connected tool inventory.
No helper-expansion/job route was used without confirmed health/version/task-negotiation evidence.

Each request below exceeded an explicit 55,000 ms client audit deadline and returned no completed tool result, artifact, revision, or coverage report:
- Exact provider `source_lookup`: one definition, no references, 24 lines, retried at 12 lines.
- `reference_search` for `meta_effect`: installed/wiki sources, limit 2, retried wiki-only at limit 1.
- Root `event_inspect`: trace with one node, one edge, depth 1, helpers off, retried as downstream lint at the same minimum boundary.
- Root `event_render`: neighborhood with one node, depth 1, helpers off, retried downstream.
- `event_compare`: cached prepatch revision `e9e470262f1ea057b06851d06c768e7e69517688395c2427a2d534af5005edff` against current, root selector, one chain node, one render node, render false.

The comparison was already at the minimum one-node boundary.
These are client nonresponse limits, not invented server error codes.
Even a focused root event graph would not itself certify the provider's meta-expanded helper or Event 019 runtime transaction.
No fresh MCP success or source-only equivalent engine proof is claimed.
No weighted logic was changed or rebalanced by this patch, and this narrow review makes no new probability sign-off.

## Local reference evidence

Relevant sections were read directly after the MCP reference nonresponse.
No Paradox wiki web access was used.

| Reference | Lines | SHA-256 | Rule |
| --- | --- | --- | --- |
| `paradox_wiki/Division modding - Hearts of Iron 4 Wiki.md` | 69-72 | `19b8349a2e1a7da45d138c0807119d1ab5e24c391a8182099ff59ff18d8be147` | Group consistency within columns, zero-based grid limits. |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 4637-4668 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` | Meta substitution using `[?variable|.0]` produces integer text. |
| Installed `documentation/effects_documentation.md` | 4833-4851 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | Meta text and named replacements, valid scopes. |
| Installed `documentation/script_concept_documentation.md` | 216-245 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` | Fixed-point constants and `constant:` access through variables. |
| Installed `common/script_constants/documentation.md` | 1-32 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` | Constant schema and supported access. |
| Installed `common/defines/00_defines.lua` | 859-863 | `405a24ce579815443cafe052cff1361e20c712ca8182e3f10ccbf45330dd4be4` | Native five-column/five-row template dimensions. |
| Installed `history/units/GER_1936.txt` | 4-40 | `bdf33f60d8e1d972f8fd56c92e550c53d2af9140776e708d28f4952f2e806b17` | Vanilla native template placement precedent. |

Installed paths are under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`.
The installed source precedent and integer meta/constant documentation support the source conclusion.
They do not establish a live spawn or ledger transaction.

## Current source identities

| Source | Raw working-file SHA-256 |
| --- | --- |
| `common/scripted_effects/014_cannibalism_effects.txt` | `1751eee6c2a9de6770b6aadae2d6f18010ef84ea85bf17e6003fc4773a2fe302` |
| `common/script_constants/014_cannibalism_constants.txt` | `7125925b89b7a2f29ba41b9cba65fca5541a5261c234e7ba2342ddc4ec5bc713` |
| `common/units/014_cannibalism_irregular_infantry.txt` | `db9abb73d642c3fe218543d8444d609a5141e843fc7478cbba875701d5253623` |
| `common/scripted_effects/019_infantry_spawn_ledger_effects.txt` | `2c684af383aedc9ef2db10613054083f19569262f9617c3c260f242eb6d6dc8c` |

The final captured parent Git baseline reference was `46ea619977e21c1e210ea6ebd487a534ec45af23`.
Its raw effects blob hash is `ed6a485ca3fc49f92e45088fbe58acf8e63e15a73c2412438dcb1895b2143f97`, and its raw constants blob hash is `dcbd72e4f530769ef3a7d67a44c03cfdb2ac952716be0236b2caa12e2264bb12`.
Git blob and historical working-file hashes may differ with line endings, so the patch-scope comparisons above explicitly normalize newlines.

## Final disposition

E014-COMP-01 is **repaired and verified in current source**.
The narrow review found no remaining requested-surface defect and no new simplification.
Fresh MCP and live spawn/ledger acceptance remain unverified.
No Event 014 full-completion claim is made.
No further gameplay patch is recommended from this postpatch review.
Skills applied: `chaos-redux-events`, with the previously read planning, improvement-loop, and subagent ownership/disposition guidance retained.
