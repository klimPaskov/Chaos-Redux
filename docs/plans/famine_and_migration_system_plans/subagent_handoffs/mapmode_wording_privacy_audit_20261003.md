# Mapmode wording and privacy audit, 2026-10-03

Disposition: source audit implemented, connected inspection and tooltip visual validation blocked.
The parent assigned a bounded read-only audit of the architect's current mapmode changes, including outstanding flight obligations, positive reception roles, evacuation-only corridor context, and public versus owner/controller tooltip access.
The auditor changed this report only and made no gameplay, localisation, spreadsheet, asset, or Git changes.
The shared worktree contains concurrent changes, so line references describe the inspected working copy and require parent review against the final diff.

## Source findings

- `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt:604` selects famine numeric detail only when `famine_food_stage` exists and the state is owned or controlled by `ROOT`.
- `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt:1112` selects migration numeric detail only when the state is owned or controlled by `ROOT` and a local migration or explicitly evacuation corridor context exists.
- Both selectors fall back to public keys that contain only a qualitative food stage or migration role.
The public fallbacks do not call the private movement-cause, cohort, corridor, generation, share, capacity, or national-total getters and contain no numeric variable substitutions.
- `migration_initialize_state` at `common/scripted_effects/migration_core_effects.txt:1660` initializes reception, flight, returned, resettled, and trapped ledgers to zero without creating the context flags.
The migration detail selector no longer opens solely because a zero reception ledger exists.
An initialized zero flight ledger also does not create detail context.
Positive national totals alone do not open the private state tooltip.
- The owner-country block in `migration_state_map_mode_detail_authorized` explicitly reads `FROM.owner`, names that country, and labels integration and resettlement as national.
State reception, waiting, returned, and resettled values explicitly read `FROM`.
The permitted controller route can also see the owner's country totals through this existing block.
That follows the assigned owner/controller permission, but it should not be described as a separate country-level secrecy guarantee.
- `GetMigrationStateMapModeOriginRole` at lines 750–775 now accepts an active displacement origin with either positive flight pressure or positive live flight population.
`GetMigrationStateMapModeDestinationRole` at lines 791–820 now accepts active positive reception in addition to actual resettlement or return context.
No new state identity or physical transfer is fabricated by these role getters.
- `migration_apply_flight_request` at `common/scripted_effects/migration_core_effects.txt:749` adds the same accepted request to flight pressure and state flight population.
`civilian_transfer_reconcile_obligations` at `common/scripted_effects/civilian_transfer_effects.txt:560` settles the paired ledgers from a proven actual origin debit, bounded by both live balances, and subtracts the same amount from both at lines 570–571.
Therefore `Departed` was incorrect for the live state flight ledger.
`Awaiting departure` accurately describes an outstanding obligation, distinct from the recorded latest physical departure share.
- `migration_apply_reception_delta` at `common/scripted_effects/migration_core_effects.txt:1070` applies paired state reception and destination-owner reception deltas.
`migration_refresh_reception_context` at line 1009 requires positive local reception load for reception context.
The destination label now matches that actual local receipt.
- Active preparation, route proof, corridor phase, and generation selectors require `humanitarian_corridor_operation = evacuation`.
Terminal selectors require the saved terminal operation to be evacuation.
`common/scripted_effects/humanitarian_corridor_effects.txt:926` snapshots terminal status and known evacuation/relief operation before clearing live context.
Repeated cleanup without a new status preserves the previous pair.
The migration map's terminal-colour checks at `common/map_modes/chaosx_state_map_modes.txt:626` use the same evacuation provenance requirement.
Food relief therefore does not become migration corridor context through those changed paths.

## Wording review and parent-accepted fixes

The parent accepted two narrow wording fixes and assigned application to the architect who owns the YML file.

1. `localisation/english/chaosx_map_modes_l_english.yml:155`, `migration_state_map_mode_detail_authorized`: retain `Awaiting departure` for `migration_state_flight_population`, and replace `Waiting to leave` with `Flight pressure` for `migration_flight_pressure`.
The old pair repeated one concept and suggested separate populations even though the normal producers and settlement keep the ledgers paired.
2. `localisation/english/chaosx_map_modes_l_english.yml:229`, `migration_state_map_mode_corridor_generation_recorded`: replace `Corridor operation [?FROM.humanitarian_corridor_route_generation|*0] active` with `Current evacuation corridor`.
The number is an internal generation receipt, not an in-world operation identity.
`Current` avoids claiming that a prepared route is already open, and the adjacent phase getter explains its actual status.
This removes only an implementation identifier, intentionally, without changing any population, requirement, consequence, or route phase token.

The architect applied both parent-accepted wording edits, and the auditor verified the final keys directly.
Final YML SHA-256: `1943DACAE6526EB7B707CF31624CBD06D19B42920F219B1D48FACADA60379AE6`.
Final inspected selector-file SHA-256: `F50E68EF4D157709B333207A8290AF0A440BA94353B7FA63C4CE406C1F539329`.
The numeric population tokens and all adjacent phase, role, cohort, actor, share, and country-total getters were preserved.
The only intentionally removed token was the internal corridor generation display.

Vagueness: no additional proven issue in the changed bounded text.
Bloat: no additional sentence needs removal in the changed bounded text.
Obvious explanation: no redundant explanatory paragraph was introduced.
Repetition: paired waiting labels are the proven issue above.
Overcomplication: no additional proven issue in the changed bounded text.
Style-rule repair: generation identity exposure is the proven implementation-text issue above.
The inspected text remains concise and serious.
No quotation-bearing surface was assigned or inspected, and no sourced or attributed quotation was changed.

## Key, dynamic text, and cross-surface checks

Missing keys: none among famine/migration `localization_key` references in the bounded mapmode selector file against `chaosx_map_modes_l_english.yml`.
Duplicate keys: none in the inspected mapmode YML.
Broken scripted-localisation references: none proven in the changed selector paths.
Dynamic opportunities: existing state names, owner names, local totals, national totals, route phases, physical departure share, and arrival share remain dynamic.
No new meter or independent arithmetic owner was added by the inspected changes.
The generation receipt should stay internal as described above.
Encoding concerns: none identified in the bounded YML source check.
Catalog mismatches: no event catalog row is assigned because this package is a shared system without an event ID.
The workbook and export-only CSVs were not edited or treated as sources of truth.
The final two key changes above are the wording handoff if another consumer mirrors them.
Spec presentation remains three category values each: Food Security, Food Reserves, Relief Access for famine, and Displacement Load, Reception Capacity, Border Policy for migration.
This audit did not broaden into category layout or prose changes.

## Reference evidence and validation limits

Skills used: `.agents/skills/chaos-redux-subagents/SKILL.md` and `.agents/skills/chaos-redux-events/SKILL.md`, including the player-facing prose and handoff rules.
The package README and presentation specification were read for the accepted independent-mechanic and three-value constraints.

The connected metadata exposes `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, and `hoi4.map_inspect`.
The call `hoi4.reference_context({surface: "localisation", limit: 4})` and the bounded `hoi4.map_inspect({lookupOnly: true, query: "famine migration mapmode", queryLimit: 3, includeOverview: false})` did not return during the source audit.
No service-health, sourcepass, map-inspection, engine, or artifact coverage claim is made from exposed tool names or these pending calls.
No artifact URI was returned to retain.

The exposed `hoi4.map_render` schema supports only fixed geography layers, area/tile selection, and listed geographic overlays.
It has no scripted-mapmode identifier, viewer scenario, tooltip, or localisation-layout parameter.
Consequently, it cannot establish famine/migration scripted tooltip wrapping, overflow, or owner/controller scenario coverage through this exposed schema.
That is a specific route gap, and source review is not equivalent visual or engine evidence.

Local fallback references read:

- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:520`–537, scope namespaces, and lines 656–689, scripted text selection and first passing alternative.
SHA-256: `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/map_modes/documentation.md`, full 100-line native example, including player scope and FROM state scope.
SHA-256: `FE0A32E55F8F409DF104C9F386F607767D795193046E1DE509FAC75A46EC6392`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_localisation/00_scripted_localisation.txt:1`–36, native scope guidance and ordered trigger/fallback precedent.

Standalone Technology Tree Viewer availability was checked separately in the exposed tool inventory.
No standalone viewer tool was found, while technology domain render routes are exposed.
Record this as an exposed-package gap, not a claim that no external viewer installation exists.
Technology is outside this audit's task surface.

Meaningful validation performed: transfer-producer/settlement trace, local-versus-country scope trace, public getter reachability trace, terminal operation/phase pairing, bounded key coverage, and manual reading of each changed tooltip fragment.
Meaningful validation skipped: connected map inspection, tooltip production rendering and matching viewer scenarios, because the pending service calls and renderer schema do not supply that evidence.
No game was launched and no logs were read.
No gameplay simplification was made by this auditor.
The two wording changes are verified in the final source.
There are no unresolved wording decisions within this bounded audit.
