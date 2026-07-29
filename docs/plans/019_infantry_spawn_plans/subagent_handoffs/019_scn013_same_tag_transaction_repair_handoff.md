# Event 019 SCN-013 Same-Tag Transaction Repair Handoff

## Result

SCN-013 package setup is atomic for one-state and all-island same-tag actors. The runtime freezes the existing Event 19 ledger boundaries and country-local accounting before package materialization. Claimant promotion or government replacement, reserve manpower, scenario AI, scenario pressure, faction departure, and actor registration wait for exact package and diplomacy proof. A failed package deletes and proves absence of only the newly appended scenario unit IDs and unique templates before truncating the new ledger tails and restoring the prior country state. A country whose pre-existing main or claimant ledgers are not aligned is rejected before materialization and exits without resizing any ledger.

The ordinary-history gate was traced to its append sites. `infantry_spawn_contributes_to_ordinary_evolution_history` rejects scenario actors, dynamic scenario breakaways, takeover actors, setup-bypass actors, and derivative countries. SCN-013 keeps one of those identities through package evaluation, and package success now explicitly asserts the exclusion. Consequently the transaction's exact contribution to shared lot, formation, claimant, request, incident, and management history is zero. Same-tag rollback, dynamic rollback, and their delayed retries never restore a frozen shared counter and cannot discard intervening changes from another country.

General Mutiny uses exactly one dedicated scenario generation and one new unit per requested lot, assigns only the newly appended random lots to the newly created claimant, and retains the claimant's government. If that exact same-tag claimant cannot complete the takeover, the existing failed-coup consequence runs before technical cleanup. A dynamic General claimant breakaway adopts the already aligned scenario ledger as its derivative private ledger; derivative initialization no longer clears the claimant's live unit, lot, or obligation identity. Dynamic Anomalous Rising retains its provider-installed derivative government.

No registry file, registry filename, registry row, scenario registration, constant, decision, localisation file, management file, or settlement file was edited. No substitute route or fallback was introduced.

## Changed files

- `common/scripted_effects/019_infantry_spawn_scenario_effects.txt`
  - defers generic government, manpower, AI profile, and pressure until exact package proof;
  - defers same-tag claimant promotion, faction departure, and actor registration until the package and diplomacy gates have passed;
  - requires exact generation targets for Conventional Flood and Arsenal Lottery, exact random-lot and claimant proof for General Mutiny, and exact generation/lot/unit formation targets for Anomalous Rising;
  - creates a dedicated General Mutiny request generation so a pre-existing open generation row is never reused;
  - corrects claimant assignment to restore the helper's automatic first assignment and then assign only the new lot tail;
  - snapshots same-tag ledger boundaries, accounting variables, relevant flags, and auxiliary technology/achievement arrays;
  - rejects a pre-existing unaligned main or claimant ledger before package materialization and never resizes that pre-existing state;
  - deletes only new immutable unit cohort IDs and unique `Unbidden Muster <template UID>` templates without refunds;
  - proves every new unit UID and template absent before resizing aligned tails;
  - retries an unproved deletion without discarding the identity rows needed by the retry;
  - proves ordinary-history exclusion at each successful package branch and removes stale shared lot/formation snapshots and rewinds from both immediate and delayed rollback.
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`
  - adds `infantry_spawn_derivative_adopt_scenario_claimant_ledger`;
  - requires aligned nonempty scenario claimant ledgers before claimant-breakaway derivative initialization;
  - adopts those exact ledgers instead of clearing them;
  - leaves the scenario-created derivative pulse to the post-package pressure step;
  - removes redundant frozen lot/formation rewinds because derivative identity already excludes every ordinary-history append.
- `events/019_infantry_spawn_scenario.txt`
  - adds hidden retry event `chaosx.nr19.955`.
- `docs/events/019_infantry_spawn/systems/triggerable_scenario.md`
  - documents exact package proof, deferred finalization, same-tag rollback/retry, General claimant-ledger adoption, and the permitted failed-coup consequence.
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_scn013_same_tag_transaction_repair_handoff.md`
  - records this bounded implementation handoff.

## Important identifiers

- `infantry_spawn_scenario_begin_same_tag_transaction`
- `infantry_spawn_scenario_attempt_same_tag_rollback`
- `infantry_spawn_scenario_retry_same_tag_rollback`
- `infantry_spawn_scenario_resize_same_tag_ledger_tails`
- `infantry_spawn_scenario_evaluate_actor_package`
- `infantry_spawn_scenario_begin_random_lot_generation`
- `infantry_spawn_scenario_finalize_actor_government`
- `infantry_spawn_derivative_adopt_scenario_claimant_ledger`
- `chaosx.nr19.955`

## Engine and precedent basis

The implementation follows the offline wiki's array, variable, unit, event-target, country, scope, trigger, effect, event, decision, idea, AI, division, and unit guidance plus the official vanilla effect, trigger, dynamic-variable, script-concept, and script-constant documentation. The exact unit rollback mirrors La Résistance's fake-army pattern: retain the ID supplied to `create_unit`, call `delete_unit` with that exact ID, and keep identity data until deletion is proved. `delete_unit_template_and_units` is restricted to the package's globally unique Event 19 template UID names and uses `disband = no`.

## Validation evidence

- The re-audit maps all 74 main-ledger arrays and all 12 claimant-ledger arrays into 95 same-tag resize targets; the remaining nine targets are the intended auxiliary technology, template-lock, transfer, and achievement arrays. All 17 resize boundary variables have a pre-materialization snapshot.
- General Mutiny proves exactly one new generation, the requested lot count, the same exact unit count, one claimant row, aligned main/claimant ledgers, and a complete derivative identity where applicable.
- The only lot and formation global increment sites are guarded by `infantry_spawn_contributes_to_ordinary_evolution_history`; claimant, request, incident, and management history increments use the same gate. Every successful scenario branch explicitly proves that gate false before finalization.
- No scenario or derivative-package rollback path snapshots or assigns a frozen ordinary-history global. Monotonic global UID allocators remain intentionally forward-only and are never rewound.
- The wider Event 19 audit found synchronous rollback snapshots in ordinary generation/request code, but no other delayed scenario cleanup writes a frozen shared counter; those non-scenario transactions are outside this bounded repair.
- Auxiliary locked-template, spawn-only-template, technology-lock, transfer-eligibility, pretechnology, and achievement-pretechnology arrays have their own frozen boundaries.
- The three touched script/event files have balanced braces and no duplicate top-level scripted-effect identifier; repeated `country_event` blocks are expected.
- `chaosx.nr19.955` has one definition and one scheduled call.
- No literal unsupported `<=` or `>=` operator was introduced.

## Simplifications, omissions, and blockers

None. The repair does not use a substitute actor, government, route, package, or cleanup fallback. If exact object deletion cannot be proved, the original tag remains under the cleanup marker and retries with the intact ledger tail.
