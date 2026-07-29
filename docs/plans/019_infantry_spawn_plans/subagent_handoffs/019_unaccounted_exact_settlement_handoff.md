# Event 19 exact-obligation settlement handoff

## Scope

This tranche replaces aggregate debt disposal with row-exact settlement,
material-backed salvage, and a transactional ordinary paid-request path. It also
closes the emergency-integration manpower-liability exploit. The existing
`019_infantry_spawn_unit_registry_effects.txt` file was inspected as a contract
and was not edited; no additional Event 19 filename containing `registry` was
created.

## Accounting contract

- Obligation rows retain raw issued, paid, salvageable-paid, outstanding, and
  outstanding weighted-debt values.
- Fixed weighted debt per row is 45 for ordinary equipment, 20 for support, 40
  for fuel, 90 for prototype/extended equipment, and 100 for anomalous-provider
  obligations. Manpower contributes only its exact raw quantity to the separate
  manpower liability.
- Partial exact payment reduces weighted debt proportionally. Full payment
  clears the residual exactly.
- Incident relief calls the same payment kernel but is marked non-material, so
  it never creates salvage.
- Unaccounted lots are archived only after equipment debt and manpower liability
  both reach zero. Their unit status becomes `unaccounted_settled`, and this path
  does not add destruction or demobilization history.

## Player and AI surfaces

- `infantry_spawn_select_next_unaccounted_lot` cycles missing lots.
- `infantry_spawn_settle_selected_lot_obligations` displays and consumes the
  exact outstanding profile quantities as one preflighted transaction.
- AI uses the same affordability trigger and settlement effect, preferring an
  unaccounted affordable lot before other debt-bearing lots.
- Standardization, emergency integration, demobilization, and specialist
  preservation all require both exact lot balances to be zero.
- The Muster Board overview and selected-lot accounting expose both weighted
  equipment debt and exact manpower liability. Every outstanding 500 manpower
  also adds one battalion-equivalent to the existing Army Congestion ladder.

## Salvage and cleanup

- Verified supervised demobilization returns 30 percent of each materially paid
  unit-backed obligation profile.
- Specialist preservation returns 45 percent of materially paid support
  equipment and 45 percent of materially paid manpower apportioned by the lot's
  support-to-total component ratio. It grants
  `infantry_spawn_preserved_specialist_training` for one training cycle.
- Incident forgiveness and unit-UID-zero accounting rows are excluded.
- Technical teardown forfeits every remaining lot obligation and grants no
  salvage.

## Paid-request transaction

`infantry_spawn_request_random_formation` now performs:

1. system initialization and a complete transaction snapshot;
2. reusable/new generation preparation;
3. post-preparation quote, affordability preflight, and exact debit;
4. ordinary or Evolution III dispatch;
5. proof of the engine template, exact live-division identity, and aligned
   appended ledger rows;
6. success-only request count, ordinary-history telemetry, cooldown mission,
   Muster Control cost, board activation, and last-request flags.

Any failure deletes newly allocated `Unbidden Muster` templates and their
cohorts, truncates all appended aligned and auxiliary rows, restores the prior
generation tail/counters/flags, reverses finite prototype grants, and refunds
the exact quoted resources. Global monotonic UID allocators deliberately retain
gaps.

## Files changed

- `common/script_constants/019_infantry_spawn_constants.txt`
- `common/scripted_triggers/019_infantry_spawn_ledger_triggers.txt`
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`
- `common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt`
- `common/scripted_effects/019_infantry_spawn_ledger_effects.txt`
- `common/scripted_effects/019_infantry_spawn_generation_effects.txt`
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt`
- `common/scripted_effects/019_infantry_spawn_management_effects.txt`
- `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt`
- `common/decisions/019_infantry_spawn_decisions.txt`
- `common/ideas/019_infantry_spawn_ideas.txt`
- `localisation/english/019_infrantry_spawn_l_english.yml`
- `docs/events/019_infantry_spawn/overview.md`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_unaccounted_exact_settlement_handoff.md`

## Assets

No new visual asset is required. The settlement and lot-cycle decisions reuse
the registered Event 19 decision sprites, and the temporary training idea reuses
the existing specialist-training idea sprite contract.

## Remaining risks and queued work

- Standardization is safe but not feature-complete: the generated template stays
  locked instead of being converted into a separate ordinary template with
  explicit conversion loss and template-count reduction.
- Multi-unit demobilization uses complete preflight followed by sequential
  engine deletions. A late engine-side delete failure cannot recreate an earlier
  deleted division, so it is not a true engine rollback.
- The request rollback relies on the documented `delete_unit_template_and_units`
  contract and proves the country division count and template absence afterward;
  a failed engine deletion deliberately raises the ledger invariant instead of
  pretending rollback succeeded.

## Future extension suggestions

- Implement the spec-complete standardization conversion as its own reviewed
  transaction, including explicit composition mapping, material loss, template
  retirement, and template-count proof.
- If the engine gains a batch-delete transaction or reversible exact-division
  recreation contract, replace sequential demobilization deletion with that
  stronger primitive.
