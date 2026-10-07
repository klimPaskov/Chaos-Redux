# Engine feasibility and unresolved dependencies

Date: 2026-09-22. Scope: planning, not executable HOI4 implementation.

The requested design is fixed. The paths below are verification tasks for the implementation runtime, not permission to ship a weaker version. Native placement, native observation, and current-map discovery are different capabilities and must be proven separately.

## Evidence levels

**Observed source** means text or code was actually read. It does not prove current engine execution. **Design contract** means an authored requirement. **Model-tested** means a Python abstraction satisfied a property. **Engine-verified** requires the installed version, real supported script interfaces, and appropriate runtime or tool evidence. Nothing in this delivery is labeled engine-verified.

## Blocking capability register

| ID | Capability or dependency | Present evidence | Required closing evidence | What cannot be claimed yet |
| --- | --- | --- | --- | --- |
| B01 | Complete effective naval region set | User requirement, old random helper, bounded repo searches | Installed documentation plus effective-map inspection proving a supported complete enumeration or correctly fingerprinted campaign registry | Arbitrary compatible-map coverage |
| B02 | Country-owned additive mine effect and cap semantics | Current Event 088 source invokes `add_mines` within `every_country`. Offline Effects search excerpt describes current-country ownership | Current vanilla effect docs, relevant defines, scope test, empty/partial/full/over-cap comparisons | Native placement success, exact cap, or preservation under modified caps |
| B03 | Eligible owner rule in peace, exile, landlocked, subject, and dynamic cases | No complete native legality evidence | Verified country legality and effect support across the recipient cases | Coastline, mine technology, wartime status, or fleet size as a mandatory script gate |
| B04 | Material-increase observation for the +20 Chaos award and achievement provenance | Design requirement only | Reliable field before/after data or equivalent proven predicate that detects a real increase | Awarding Chaos only on real manifestation without an observation mechanism |
| B05 | Multi-owner hostility and combat aggregation | Separate-country placement intent and old source structure | Two-owner and multi-owner native observation with active wars, neutral owners, faction relationships, caps, and tooltips | Linear stacking of combat damage or immunity from owning a friendly field |
| B06 | Clearing and lifecycle behavior | User requires normal sweeping. No live or complete current native reference | Sweeping plus peace, decay, capitulation, disappearance, faction and save tests | Claimed mine persistence duration, clearance causality, or ownership transfer behavior |
| B07 | Successful application and shared dispatcher order | Supplied event skill identifies shared owners and prefire responsibilities. Current event applies in its option | Inspect live callers and generic fire helpers, prove preflight before consumption and one commit path before successful presentation | Exactly-once global behavior or safe partial-failure handling in the game |
| B08 | Achievement observation | Detailed design in Part 5 only | Reliable sweeping attribution, hostile-field totals, distinct-region history, native landing route/attacker/target observation, defeat attribution | Both achievement unlocks as implemented or even fully script-observable |
| B09 | Required HOI4 MCP routes | Supplied config and profiles name the service and tool families | Invokable live schemas and actual event, map, probability and relevant render receipts | MCP pass or source-only review equivalent to a tool audit |
| B10 | Custom subagent execution | All 20 supplied profiles were read. No usable spawn route exposed | Actual bounded custom-agent runs with receipts and parent dispositions | Independent audits or mandatory improvement-loop completion |
| B11 | Installed vanilla documentation and complete core wiki reading | Supplied references identify the paths. Only selected connected snippets and a truncated Scopes response were read | Read all applicable mandatory pages and installed docs, recording exact complete/partial status | All referenced must-read files having been fully processed |
| B12 | Visual references and achievement templates | Asset skill and profile text read completely | Inspect actual report examples, native achievement family, required templates, overlay, processing tools and decoded DDS results | Runtime asset production or verified visual compatibility |
| B13 | Live workbook and current registry alignment | Supplied CSV exports plus connected cluster-doc excerpt | Inspect XLSX and live member arrays, then mirror accepted runtime wording through the prescribed export path | Workbook correction, complete cluster reconciliation, or playable status |

B01, B02, B03, B05, B06, and B07 gate the requested mine incident. B04 gates the proposed material-only Chaos rule and event provenance. B08 gates achievements, not the logical definition of the mine addition. B09 through B13 gate the relevant project workflow claims. Independent progress is possible, but a blocked row cannot be marked passed because a different row passed.

## Current-map provider decision

First inspect current installed native documentation and the effective map. Prefer a documented native iterator or complete engine-maintained collection if one exists. Do not invent `every_strategic_region`, `every_sea_region`, `global.sea_regions`, or similarly plausible syntax.

If the only viable route is a generated registry, the generator must resolve the actual effective map after base game, Chaos Redux, compatible map content, load order and path replacement. It must use a proper parser for strategic regions and province classification, reject duplicate conflicting IDs, preserve valid unusual IDs, distinguish land from naval data, and emit a deterministic unique region set. Raw regex extraction of every integer in a file is not a map parser.

Bind the output to a reproducible fingerprint of the effective inputs and the supported configuration. A project-local registry does not know the player's arbitrary later mod selection. The implementation needs a real installation/build compatibility mechanism, a reliable runtime verification mechanism, or an explicitly constrained supported configuration. Until that is established, full arbitrary-map support remains blocked. A successful run on the unmodified map proves only that configuration.

## Placement interface

The current source's effect form is evidence worth investigating, not a validated recipe. Determine whether the region argument accepts a literal, variable, or verified meta-effect expansion, and whether the amount uses the documented numeric convention. Preserve current-country ownership across nested loops. `ROOT` is the event recipient and must not accidentally become the owner of every field.

A region-major loop and a country-major loop are both logically acceptable if they cover the same C × R snapshot exactly once and preserve ownership. Select the ordering supported by verified interfaces and measured cost. Do not use naval-range selection, ordinary mission legality, or random retry logic as shortcuts.

For each valid ordinary pair, the intended operation is additive. Native clamping may be relied on only after it is verified. Do not set fields to 1,000, delete then add, alter a global cap, merge owners, or write a modifier instead of mines. Over-cap preservation requires a specific compatibility result.

## Read capability is not write capability

The presence of `add_mines` does not establish a script trigger for reading owner-region mine counts. A save inspector may demonstrate a test result without providing a callable in-game predicate. Similarly, a global swept-mine statistic may not identify who swept which region. Keep these boundaries explicit when evaluating B04 and B08.

If exact runtime observation is unavailable, do not fabricate trigger names or a proxy based on naval bases, idle ships, convoy losses, coastal control, or time passed. Preserve the design and report the exact unobservable field. A revised achievement or Chaos rule would require an explicit design disposition rather than a hidden substitution.

## Version and expansion availability

The official Steam store page inspected on 2026-09-22 lists Man the Guns among the expansions included with the base purchase. This supports rejecting an unexamined assumption that current players must buy a separate expansion for the feature. It does not prove which script gates, entitlement checks, or engine behavior apply to every old installation.

Determine the supported build from the actual installed game and its documentation. Do not add a stale paid-DLC gate by memory and do not remove a verified current feature gate simply because store packaging changed. The observed repository snapshot and its offline wiki capture date are separate from the installed game version.

## No equivalence between planning checks and game checks

The included Python model checks the mathematical and lifecycle contracts. It does not read a save, invoke `add_mines`, discover a live map, run naval missions, render the game, inspect a workbook, or execute a custom agent. It cannot close B01 through B13 by itself.
