# Event 028 near-miss selection eligibility

Disposition: implemented in source, with native achievement and settings acceptance unresolved.
Acceptance basis: Part 10 explicitly requires both evolutions enabled and eligible, and disqualifies an evolution disabled before selection.

`asteroid_incoming_resolve_miss` preserves the opening eligibility requirements and checks the shared `is_current_evolution_enabled` predicate for both Global Fragmentation and Extraordinary Minerals at selection time.
The two checks use the existing Event 028 identity, type, stage, and tier constants through the same temporary-variable contract as the opening snapshot.
An opening preview does not override a later disabled evolution.
Disabling either evolution blocks only the achievement award and does not punish the miss.
The existing manual, debug, force-trigger, AI, country-classification, prior-impact, dust, and crater disqualifiers remain in place.
The source-model comparison confirms that every non-award miss operation is unchanged from commit `829f4db894d90a08570e5483377189ca51638771`.
No option weight, target selection, physical profile, visible wording, asset, audio, ledger, history-row append, or workbook field changed in this repair.

Run `python .tools/validation/validate_028_near_miss.py`.
The actual-source model reads both before and after award branches, the shared settings predicates, achievement predicates, and tier constants.
It evaluates the exact meta-trigger flag naming from the shared source and fails on unknown evaluated commands.
The external shared country classifier is a declared scenario input, not native classification evidence.

Sixteen scenarios pass.
The three regressions are disabling Fragmentation, disabling Minerals, and disabling both after opening, which the before branch incorrectly awarded.
Both-enabled 800 and 900 Chaos cases still award.
Missing either opening preview, Chaos 799, prior impact, active dust, an existing crater, debug, manual, force-trigger, a special-country classification, and AI all remain disqualified.
The non-award miss-body comparison preserves its exact before-source operations.
The model is neither a native HOI4 run nor probability evidence.

## References and evidence limits

The parent re-verified coding-route exposure after continuation.
`hoi4.reference_context` for the event surface timed out after 600 seconds, and a narrower offline `fire_only_once` lookup was submitted.
The corrected one-event `hoi4.event_inspect` trace and one-state `hoi4.map_inspect` lookup also timed out after 600 seconds, with narrower retries submitted.
No new source revision, engine scenario, or graph artifact was returned by those failed calls.
The exposed `source_lookup` schema has no `view` or `keyPath`, and `script_validate` is not exposed.
These route limits do not establish native acceptance.

The pertinent offline Data structures variable and temporary-variable section at lines 425 through 478 was read directly, SHA256 `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
Installed `documentation/effects_documentation.md` at lines 7820 through 7840 documents `set_temp_variable`, SHA256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
The verified project precedent is the opening snapshot in `events/028_asteroid_impact.txt`, which passes the same four fields to the shared settings predicate.
Current shared settings source SHA256 is `99BA6329FA9DD0EFCC06FB2A1A6452BD0C82CA252A379BE78D0CFAACFE2F8F20`.
Current Event 028 achievement predicate SHA256 is `83AFE2130F7A7959F51609084E9C64BA5F61118779A5E35768628286FB3A59F9`.
The completion report must retain the live settings-toggle, achievement persistence, and no-aftermath scenarios as unresolved until actual evidence exists.

Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.
No skill, asset, localisation key, or workbook row was created or changed for this repair.
