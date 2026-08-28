# Event 006 IW-095 roster-checkpoint gate repair — 2026-08-28

## Scope

This bounded source repair hardens the package-local IW-095 Dahomey initialization gate. It does not admit DAH, select a leader, create or wire assets, alter the central allocator, or change any Event 006 count.

## Defect

`independence_wave_dahomey_checkpoint_roster` was called automatically from `independence_wave_setup_iw_095_dahomey`, while `has_independence_wave_dahomey_command_roster` only checked the parent identity/rights flag. That allowed identity clearance to synthesize a command-roster receipt even though the approved portrait and roster evidence remained unresolved.

## Repair

- `common/scripted_triggers/006_independence_wave_first_footprint_package_triggers.txt` now requires the parent-published `independence_wave_dah_roster_checkpoint` in `has_independence_wave_dahomey_command_roster`.
- The same trigger now gates `can_initialize_independence_wave_iw_095_package`, so setup cannot partially initialize DAH without the explicit roster receipt.
- `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt` no longer clears the parent-owned roster checkpoint at setup entry and no longer auto-calls the checkpoint effect. Cleanup still clears the generation-owned receipt.
- The setup comment records that identity clearance alone is not a command-roster proof.

The existing `independence_wave_dahomey_checkpoint_roster` effect remains the explicit parent-owned publisher after the approved roster and portrait/identity review are complete. Until that receipt is published, the package remains fail-closed and no package-local decisions or missions can activate.

## Validation

- `python -B .tools/audit_event6_flags.py --strict` passed with 102 registered tags and 0 incomplete flag families.
- `python -B .tools/audit_event6_allocator.py --strict` passed with 32 attestations, 29 compatible reservation groups, 40 runtime adapters, and the unchanged `3/4/5/7/10` ladder.
- `python -B .tools/audit_event6_country_api.py` passed with 242 broad tags, 191 resolved carriers, and no missing or duplicate carriers.
- `python -B .tools/audit_event6_form16.py` passed.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.

The mandatory Event 006 and probability MCP routes remain blocked by the recorded `ARTIFACT_MANIFEST_INTEGRITY_FAILED` response with no artifacts. No engine or live-game claim follows.

## Boundary

This repair tightens a fail-closed package-local gate only. IW-095 still lacks the attested identity/rights receipt, approved neutral symbol and portrait roster, central adapter and Join wiring, typed probability evidence, and working MCP artifact manifest required for admission.
