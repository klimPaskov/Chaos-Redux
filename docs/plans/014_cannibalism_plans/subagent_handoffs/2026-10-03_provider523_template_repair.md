# Event 014 provider 523 template repair

Disposition: implemented and independently reviewed at the source boundary.
Acceptance basis: the user-authorized Event 014 continuation and the completion auditor's confirmed invalid native formation coordinates.

The independent review in `2026-10-03_provider523_postpatch_review.md` passes the bounded template, group, ledger, meta-expansion and obligation checks with no remaining defect on that surface.
Its MCP and live-evidence limitations remain explicit and do not establish full Event 014 completion.

Provider 523's Cannibal Irregular Muster contains all nine family battalions.
The eight infantry-group families occupy columns 0 and 1, and Bone Riders occupies mobile column 2.
Island Reavers uses row 4 of the first infantry column.
All coordinates fit the installed five-column, five-row combat grid, and each column contains one native unit group.

The `cannibalism_muster_layout` script constants supply the template and component ledger together.
The existing meta effect receives integer-formatted temporary values, so its `division_template` payload contains literal coordinates rather than unsupported dynamic tokens in native position fields.
The same temporary values build the nine ledger rows in template order.
No family or battalion is dropped to accommodate the grid.

## Changed files

- `common/script_constants/014_cannibalism_constants.txt`: define the shared muster columns and rows.
- `common/scripted_effects/014_cannibalism_effects.txt`: move Bone Riders and Island Reavers, inject the shared layout into the existing template meta effect and match its component ledger.
- `docs/plans/014_cannibalism_plans/evidence/2026-10-03_provider523_template_repair.json`: preserve the committed before source revision, resolved after coordinates, native limits, group identities and resource reconciliation.
- This handoff and the independent postpatch review record the implementation and validation limits.

## Meaningful validation and balance

The expanded formation has nine distinct sub-unit IDs, nine distinct positions and exactly nine component ledger rows.
The row-by-row ledger coordinates match the template order.
Each column's unit groups are checked against the actual Event 014 sub-unit definitions.
Grid bounds are read from the installed `MAX_DIVISION_BRIGADE_WIDTH` and `MAX_DIVISION_BRIGADE_HEIGHT` defines, rather than assumed.
The intended total obligations still equal the summed unit definitions: 7,350 manpower, 990 infantry equipment and 35 motorized equipment.
The provider's existing obligation manifest retains those totals.
No eligibility, AI weights, stochastic score, unit statistics or resource tuning changed.

These are source expansion and installed-database checks.
They do not establish live template construction, source-loader acceptance or successful full MCP helper coverage.
`hoi4.script_validate` is absent from the connected tool list.
The completion auditor's current event render is partial, with four nodes and no indexed helpers; its narrower inspect/compare attempts returned no complete helper evidence.
The parent's documentation/source queries and narrower retries both timed out after 600 seconds.
No source-only check is promoted into engine evidence.

## References read directly after the MCP route gap

| Source | Lines | SHA-256 | Relevant rule |
| --- | --- | --- | --- |
| `paradox_wiki/Division modding - Hearts of Iron 4 Wiki.md` | 48–86 | `19b8349a2e1a7da45d138c0807119d1ab5e24c391a8182099ff59ff18d8be147` | Zero-based template coordinates, five rows/columns and one group per column. |
| Installed `documentation/effects_documentation.md` | 3625–3632; 4833–4852 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | Country-scoped `division_template`; meta-effect substitution. |
| Installed `common/defines/00_defines.lua` | 859–863 | `405a24ce579815443cafe052cff1361e20c712ca8182e3f10ccbf45330dd4be4` | Combat and support grid bounds. |
| Installed `documentation/script_concept_documentation.md` | 216–245 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` | Fixed-point constants and scoped-variable access. |
| Installed `common/script_constants/documentation.md` | 1–35 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` | Constant schema and explicit `constant:` access. |
| Installed `history/units/USA_1936.txt` | 2–22 | `b35e018b27803aab8fb03e2e850b3bd6ff532f88ca269a9f62b2c19a164165d8` | Native zero-based regiment and support layout precedent. |

All installed paths above are relative to `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
The existing ledger appender at `common/scripted_effects/019_infantry_spawn_ledger_effects.txt:456` consumes the supplied component columns and rows without changing the new `cannibalism_muster_*` temporary values.

## Simplifications, omissions, and blockers

No simplification or fallback was introduced.
All nine family IDs, resource totals, locked-template behavior and existing provider callbacks are preserved.
No localisation, bitmap asset or catalog wording changes are required by this coordinate repair.
Full Event 014 completion remains blocked by the separately recorded probability, GUI, portrait/source-receipt and orchestrator-owned live evidence gaps.
This repair does not claim a clean live `error.log`.

Skills used: `chaos-redux-events`, `chaos-redux-subagents` and `chaos-redux-shared-git-commit`.
