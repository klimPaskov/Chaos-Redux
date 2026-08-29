# Mapmode, Corridor, and Relief Localisation Patch

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Scope and result

This bounded patch aligns the migration mapmode corridor selector and the named corridor and relief decisions with the persisted corridor and foreign-relief contracts. It does not change gameplay, constants, helpers, mapmode definitions, GUI, assets, the workbook, or the famine tooltip.

The package still owns exactly two dedicated mapmodes: `famine_state_map_mode` and `migration_state_map_mode`. `common/map_modes/chaosx_state_map_modes.txt` contains no third famine, migration, corridor, relief, reception, cohort, or return mapmode.

## Files changed

- `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt`
- `localisation/english/chaosx_map_modes_l_english.yml`
- `localisation/english/famine_migration_l_english.yml`
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/mapmode_corridor_relief_localisation_patch.md`

Concurrent edits were already present in all three source/localisation files. This patch preserved them and changed only the assigned corridor and relief passages.

## Changed keys and selectors

### Scripted localisation

`GetMigrationStateMapModeCorridorStatus` now distinguishes persisted lifecycle evidence in this priority order:

1. active protection mission
2. offer awaiting counterpart response
3. completed transfer awaiting mission activation
4. accepted offer awaiting the evacuation operation
5. attacked and disqualified terminal evidence
6. completed terminal evidence
7. rejected terminal evidence
8. expired terminal evidence
9. current relief access
10. no corridor evidence

Active contract flags and the current `famine_migration_corridor_status` must agree before an active label appears. Terminal labels read `famine_migration_corridor_last_terminal_status`, which the corridor cleanup deliberately preserves. Attack text therefore appears only after the exact attack receipt owner has produced disqualification evidence. It is never inferred from war, route loss, or control change.

### Mapmode localisation keys

- `migration_state_map_mode_corridor_offer_pending`
- `migration_state_map_mode_corridor_accepted`
- `migration_state_map_mode_corridor_operation_pending`
- `migration_state_map_mode_corridor_mission_active`
- `migration_state_map_mode_corridor_disqualified`
- `migration_state_map_mode_corridor_completed`
- `migration_state_map_mode_corridor_rejected`
- `migration_state_map_mode_corridor_expired`
- `migration_state_map_mode_corridor_relief_access` retained
- `migration_state_map_mode_corridor_none` retained
- `migration_state_map_mode_corridor_protected` removed because it collapsed several distinct states into one label

### Decision localisation keys

- `fm_accept_corridor_offer`
- `fm_accept_corridor_offer_desc`
- `fm_reject_corridor_offer`
- `fm_reject_corridor_offer_desc`
- `fm_negotiate_corridor_desc`
- `fm_invite_relief_desc`
- `fm_emergency_imports_desc`
- `fm_escorted_relief_convoy_desc`
- `fm_emergency_airlift_desc`

The existing decision titles for negotiation, invitation, imports, convoy delivery, and airlift delivery remain unchanged.

## Display behavior before and after

Before, the migration tooltip could show only an active protected-corridor label, recent relief access, or none. It could not distinguish a pending offer, acceptance, transaction-to-mission handoff, or a persisted terminal outcome. After, each label is backed by the exact current flags/status or preserved terminal status described above.

Before, `fm_invite_relief_desc` implied that invitation granted access and lowered food pressure. The source only selects an eligible donor and creates a contract. After, the description states that invitation creates a land, sea, or air contract and that no food or relief access appears until the matching delivery action succeeds.

Before, the import, convoy, and airlift descriptions implied generic relief effects. After, they identify the active route-specific contract, the exact foreign donor-state reserve transfer, and the route or capacity facts that must remain valid until delivery.

Before, corridor negotiation did not explain the ordinary counterpart response or separate evacuation phase, and the accept/reject decisions had no English keys. After, negotiation describes the unique enemy-front counterpart and delayed movement. Accept and reject text dynamically names the requester, origin, and front state. Acceptance explicitly moves no people or food, while rejection leaves the trapped cohort at its origin.

## Audit lists

### Missing keys

Found and fixed:

- `fm_accept_corridor_offer`
- `fm_accept_corridor_offer_desc`
- `fm_reject_corridor_offer`
- `fm_reject_corridor_offer_desc`

No scoped mapmode lifecycle key remains missing.

### Duplicate keys

No duplicate definition was found for any changed or newly added key across `localisation/english/**/*.yml`.

### Scripted localisation issues

Fixed the coarse corridor selector. Every new selector output has one English key, and the removed `migration_state_map_mode_corridor_protected` key has no remaining reference.

No broken dynamic token was found in the assigned passages. The requester, origin, and front names use the repository's existing scope-valued variable localisation form, for example `[?famine_migration_corridor_offer_origin_state_id.GetName]`.

### Dynamic text opportunities

Implemented exact requester, origin-state, and front-state names for the counterpart decisions.

No donor name was added to invitation text because the donor is selected only when that timed action resolves. Import, convoy, and airlift descriptions are visible even when a contract is unavailable, so printing a donor-state variable there could expose an empty or stale name. The text instead identifies the persisted contracted donor without claiming an identity before selection.

### Cross-surface mismatches

Fixed the mismatch between invitation text and the donor contract: invitation does not deliver food or grant access. Fixed the mismatch between corridor acceptance text and the transaction contract: acceptance does not move population. Fixed the mismatch between the mapmode's old generic active label and the corridor's current lifecycle/terminal evidence.

### Encoding concerns

Both changed English localisation files remain UTF-8 with BOM. The scripted-localisation `.txt` follows its existing encoding and is not a localisation YAML database.

### Prose-quality repair

- Vagueness: replaced generic foreign relief and safe-passage claims with the exact land, sea, air, counterpart, origin, and front contracts.
- Bloat: kept each decision description to the public action, phase boundary, and material failure conditions.
- Obvious explanation: removed the implication that invitation itself performs the visible delivery and made the follow-up action explicit.
- Repetition: separated contract creation, delivery, acceptance, evacuation, and mission protection so each passage owns one phase.
- Overcomplication: used direct sentences and concrete actors while preserving the necessary contract conditions.
- Style-rule repair: the changed text contains no em dash, semicolon, staccato chain, staged contrast formula, hidden weight, implementation history, or claim that displaced civilians are inherently diseased.

## Sourced quotations and tokens

No sourced or attributed quotation exists in the inspected assigned passages. No quotation was changed.

All existing dynamic tokens and formatting codes outside the changed passages were preserved. The new response text adds only scope-valued requester, origin, and front name tokens. No cost token was changed.

## Meaningful validation

- Scoped localisation census: every changed/new key appears exactly once across the English localisation tree.
- Selector coverage: each `GetMigrationStateMapModeCorridorStatus` output resolves to one existing English key, and the retired generic key has no remaining reference.
- Dedicated mapmode census: the only famine/migration definitions are `famine_state_map_mode` and `migration_state_map_mode`.
- BOM check: both changed `.yml` files begin with `EF BB BF`.
- Read-only map inspection: `MAP_INSPECTED` revision `f7a979d1f74467613b77975b15c311c6e48190a94cd51385cd9abd391807b44b`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c29984cb31885b25b11c450ff6b6b1e06a7b9f69d6a40d4474c0184f5c09e2cc/eac87c7336a0e35a169483c5504bd47cfe54116db6417fe5ccdb44de4a26ea80/map-inspect.f7a979d1f7446761.json`.
- Read-only state-layer render: `MAP_RENDERED`, PNG artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b38b495b28948e9d861ddb346019cf9b4663c886b78decf7acf42c4b7737d69/de22527c36fdb2a1168a5a16a11e163b14d784bc3e218678ce32e5619aec6005/map-state.png`.

## Skipped validation and blockers

The installed MCP map route renders offline state/map data but does not evaluate scripted mapmode state, scripted-localisation branches, tooltip overflow, or runtime decision localisation contexts. The query returned zero direct matches for the two scripted mapmode identifiers. The generic state-layer render therefore proves the map consumer is inspectable but does not prove these lifecycle strings visually. This exact limitation remains unresolved and source review is not treated as equivalent rendered evidence.

The map inspection also reported unrelated existing building-position and port-adjacent-sea diagnostics. They are outside this localisation task and were not changed.

The exact attack-receipt producer remains outside this patch and is currently documented as an owner blocker. The mapmode will show `Attacked and disqualified` only if a future authoritative producer persists `famine_migration_corridor_last_terminal_status = disqualified` through the existing helper.

No in-game validation was run because live consumer validation belongs to the user. No commit was created, as requested.

## Unresolved wording decisions and follow-up

No unresolved wording choice remains inside the assigned source scope. The parent should retain the MCP visual limitation and attack-owner blocker in the overall completion report.
