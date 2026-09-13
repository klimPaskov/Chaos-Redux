# Events 011, 013, and 014 documentation review

Date: 2026-09-05.
Disposition: implemented for the three overview repairs, with unresolved archive, acceptance, and validation issues retained.
The [central cleanup record](../documentation_state.md) owns broader continuation.

## Reading and ownership

Curator `shared_events_docs_c02` fully read all three originals and their authority dependencies, then returned a read-only closeout with no edits or pending writes.
The parent independently fully read all three and applied the bounded repairs.
The curator fully read the current request, AGENTS.md, subagent and event skills, eleven core offline wiki pages, and vanilla script-concept, effect, trigger, and modifier documentation.
Its authority reads cover Event 011 specification README, manifest, source inventory, specification and plan completion audits, and documentation-curator handoff.
For Event 013 it read the specification README, manifest, source map, closure resume, physical-geography handoff, GUI geometry handoff, localisation/evolution handoff, and decision/mission handoff.
For Event 014 it read the specification README, package manifest, asset inventory, documentation completion, probability refresh, and vanilla-visual reuse decision.
These reported dependency reads are not a reconciliation of every interior source.

| Fully read original | Bytes | SHA-256 | Disposition |
| --- | ---: | --- | --- |
| `docs/events/011_secret_alliance/overview.md` | 36950 | `811055873b63fdaceb90b0c28bf0340a1955f2a45fc3c1ceff6aaf64c3087edd` | Implemented overview repair |
| `docs/events/013_natural_disasters/overview.md` | 35595 | `31c89d461caef4e2e7684dbea624f6555574e082183cc76b3dd1c282863fda75` | Implemented overview repair |
| `docs/events/014_cannibalism/overview.md` | 38972 | `0585a0fde809ec0686b04d69d0999f7e08e045de72eb5afc860fd6abb491885e` | Implemented overview repair |

## Repairs and unresolved claims

| Overview | Repair | Retained issue |
| --- | --- | --- |
| Secret Alliance | Attributed CLEAN, FINAL CLEAN, Implemented, audit hashes, and freeze claims to their historical records. Labelled the old GUI manual-recovery account as history, corrected prose, and recorded the missing asset register. | The historical `REWRITE_STRUCTURE_LIMIT` failure alone is not a current implementation gate under the user-supplied 2026-09-06 AGENTS.md. Mandatory visual evidence remains required. Workbook hashes and cell statuses are not a current catalog audit. |
| Natural Disasters | Replaced the claim that the source-art package is presently retained with the actual archive gap and recorded deletion. Preserved the complete API, 25 families, capacities, geography counts, and existing cluster content. | The restoration record conflicts with the absent directory. No source package recovery or design promotion occurred. |
| Cannibalism | Corrected the March Predation modifier description from 2.2 to source-backed 1.2, retaining the old number as a documentation mismatch. Attributed 2026-08-26 completion language to its retained report. | Portrait acceptance remains blocked, partial MCP and live-consumer gaps remain, and existing approved vanilla-visual reuse was not reopened or generalized. |

All three preserve distinct numbers, source identifiers, route constraints, audit history, and future ideas.
Future ideas are labelled unresolved and do not authorize implementation through this task.

## Path and source evidence

`docs/assets/011_secret_alliance/asset_register.md` is absent, with deletion recorded by `487670dee3722238dadc218a30d84c59aa27594a`.
`docs/assets/013_natural_disasters/` and its `manifest.md` are absent, with deletion recorded by `c008ec53f051add01f4c81ff8ce86b9fea668b1e`.
Neither finding establishes runtime DDS absence.

Narrow source reads in `common/units/014_cannibalism_irregular_infantry.txt` found `@MARCH_PREDATION_SPEED = 1.20` and the March consumer `maximum_speed = @MARCH_PREDATION_SPEED` with `transport = motorized_equipment`.
The overview already used `12 × (1 + 1.2) = 26.4` and a 26.4 speed table entry.
The repair aligns the descriptive modifier with that unchanged source and formula, not a new balance target or runtime speed test.
The same narrow lookup found `@BONE_RIDERS_SPEED = 1.60` and its existing consumer, which remain unchanged.

The `decision_<decision_id>.dds` string is an explicit filename template, not a missing literal asset.
The literal `gfx/FX/buttonstate_blendframes.lua` file is absent from both the mod and installed vanilla path checked.
Vanilla `interface/alerts.gfx` and `interface/core.gfx` nevertheless use that exact effectFile token, and `gfx/FX/buttonstate_blendframes.shader` exists in the installed game.
This is matching vanilla reference evidence against inferring a missing runtime effect from a literal Lua-file check.
Only those declarations and file existence were checked, not a complete shader review or rendered animation acceptance.

## Historical GUI statements retained

The original Event 011 overview stated:

> The generated SVG is an offline approximation and does not substitute for live consumer evidence.

It also recorded:

> The MCP source rewriter rejected the resize in whole-source, constants-only, and exact-property modes with `REWRITE_STRUCTURE_LIMIT`. The source change was therefore applied through the repository edit workflow and then re-inspected and rendered through the MCP.

Those statements remain historical evidence.
The user-supplied AGENTS.md on 2026-09-06 makes `gui_rewrite` optional and permits direct application of an authorized reviewed GUI edit without another fallback approval solely because a rewrite failed or rolled back.
Mandatory inspect, render, and matching before-and-after evidence remain required, and visible defects cannot be dismissed as renderer discrepancies.
The owning scripted-GUI skill provides the workflow details under that explicit user direction.

## MCP evidence and limits

The curator's Event 011, 013, and 014 inspections all returned `EVENT_INSPECTED_PARTIAL` at revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`.
Workspace-wide helper and lifecycle projections were deferred, and the reports contained one validation blocking diagnostic.
Exact artifacts:

- Event 011: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4cb8e4618d5a8294f321f85618c63f432bc72ccc83ad976c69738d2034a38e7b/f275a6497b9fb05327ea9e037703709c16d53ad22bd5f41585576ea4059b661c/event-scan-1102e50fad94.json`.
- Event 013: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27c5fe54d76638c5d61fe2b6ecf8e8fee420dd75acbbd1135a54768861cfc15b/b366abf5c6a9a2664e94d54caabe213e448b69a83101b3b332974f14d78983fe/event-scan-1102e50fad94.json`.
- Event 014: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7331e465ca99e924f5eb38224e7581a197311d1071b05673c05223bf3d0ee879/012155433ff56b4fff79c5bf929b3848ee0188ef04891c559dcae1974f950cdb/event-scan-1102e50fad94.json`.

The parent reviewed the curator closeout, not the full linked artifact payloads.
No new GUI or probability audit was performed for these three events.
Existing scenario-specific probability records retain their own evidence and limits, and this cleanup does not replace them with generic source certainty.
No gameplay, localisation, workbook, asset, provider, configuration-policy, or live-game action occurred.
No design simplification or fallback was introduced.
Skills used: `chaos-redux-subagents` and `chaos-redux-events`.

## Commit isolation

The Event 013 working copy already contained an uncommitted replacement cluster paragraph adding Event 033 and Event 051 membership.
The task commit excludes that inherited semantic change and leaves the working copy intact.
The reviewed archive, prose, evidence-boundary, and source-backed typo repairs are included independently.
No older tracked membership claim is promoted as current accepted design by this isolation.

The reviewed changes are preserved on `codex/documentation-cleanup-review-20260906`.
Integration into the shared working branch remains pending because its Git index lock is owned outside this task.
See the central cleanup record for the selective manifests and integration boundary.
