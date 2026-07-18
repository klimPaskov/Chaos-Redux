# Event 19 standardization and demobilization transaction handoff

## Scope and ownership

This tranche owns the Event 19 management transaction changes for canonical
standardization, exact-obligation settlement finalization, and supervised
demobilization. It edits only the management effects, shared management
triggers, decisions, English localisation, and Event 19 documentation listed
below. No registry or scenario file was edited or created, and no Git commit was
made from the shared dirty worktree.

## Canonical standardization contract

- A country may own at most one `National Muster Standard`. It is a locked,
  nonrecruitable eight-battalion ordinary infantry template (five infantry in
  column one and three in column two).
- Its canonical template-ledger row uses sentinel lot UID 0 and is backed by
  exactly eight aligned component-ledger rows. An existing name without the
  canonical UID/ledger proof is an invariant failure; there is no alternate
  template fallback.
- `infantry_spawn_prove_source_template_unique_to_lot` proves exactly one lot
  row, exactly one template row, and no cross-lot unit-ledger reference for the
  source template UID. Both standardization and teardown require this proof.
- Start and completion preflights prove the lot UID, generation UID, unique
  source-template UID, exact unit-ledger UID set, and exact live-division UID
  set. Event 96's `division_template_lock_event_active` marker is checked at
  action availability, mission start, mission completion, preflight, and the
  final mutation boundary.
- The conversion charge is 15 percent of exact settled, unit-backed,
  salvageable-paid equipment and fuel. Manpower, unit-UID-zero incident rows,
  and forgiven/non-material amounts are excluded. The same exact profile totals
  drive player availability, AI selection, display, debit, and refund.
- Completion debits only after full affordability and identity proof, converts
  the exact cohort through `every_country_division` plus
  `change_division_template`, and proves unchanged country division count plus
  exact post-conversion identities. A failed postproof restores the old
  `Unbidden Muster <UID>` template and refunds the exact debit.
- Lot/unit ledger repointing to the canonical UID and retirement of the source
  template row occur only after successful postproof. The obsolete engine
  template remains an inert locked/nonrecruitable shell.

## Settlement debit boundary

`infantry_spawn_preflight_exact_settlement_commit` classifies every obligation
row belonging to the target lot before country resources are debited. A row is
either a unique positive payable row in `outstanding`/`servicing` state, or a
zero-balance terminal row in `settled`/`forfeited`/`transferred` state. The
payable UID set, row count, weighted debt, manpower total, target lot identity,
and any unaccounted-lot terminal disposition are all proven first. The
post-debit path is then deterministic and mutates only rows matching both the
frozen UID set and target lot UID; it contains no late failure branch.

## Batch demobilization contract

- Preflight rejects the shared canonical template and proves one unique locked
  source template, exact generation/template/unit UIDs, exact live cohort, zero
  player-action obligations, and exact salvage row ownership.
- The physical mutation is one documented `delete_units` call against the
  proven `Unbidden Muster <UID>` template with `disband = no`.
- The implementation proves the exact country-division count delta and complete
  absence of the target lot identity before changing unit/lot/template ledgers,
  granting salvage, recording history, or applying rewards.
- Event 96 overlap at completion, preflight, or immediately before deletion
  restores the mission lot to its selectable state without deleting units or
  granting salvage. Technical defeated-country cleanup retains its explicit
  absent-army path and never grants salvage.

## Player and AI surfaces

The standardization decisions and Evolution I common-tables action share the
same exact affordability trigger. AI scans candidate ordinary lots through the
same gate and selects the strongest affordable proven lot. Localisation now
describes the canonical conversion, exact 15-percent material/fuel loss,
rollback/refund behavior, single-template batch deletion, post-delete proof,
canonical exclusion, and Event 96 mission conflict.

No new visual asset was required. The existing standardization and
demobilization sprites remain the documented UI assets.

## Files changed

- `common/scripted_effects/019_infantry_spawn_management_effects.txt`
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`
- `common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt`
- `common/decisions/019_infantry_spawn_decisions.txt`
- `localisation/english/019_infrantry_spawn_l_english.yml`
- `docs/events/019_infantry_spawn.md`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_standardization_demobilization_transaction_handoff.md`

## Validation evidence

- The management scripts retain balanced block depth after the transaction
  replacements.
- The demobilization surface contains one `delete_units` call; the remaining
  `delete_unit` and `delete_unit_template_and_units` calls belong to the separate
  paid-request rollback contract.
- Source-template uniqueness, exact settlement row classification, canonical
  rejection, Event 96 gates, exact conversion postproof, rollback/refund, and
  success-only ledger publication were manually traced through their callers.
- English localisation retains its UTF-8 BOM.
- Scoped `git diff --check` reports no whitespace error (only the repository's
  existing line-ending conversion warnings).

## Simplifications, omissions, and blockers

None. The requested canonical template, exact charge, full affordability,
rollback/refund, success-only publication, batch deletion, post-delete proof,
shared-template protection, Event 96 race gates, exact-settlement debit
boundary, UI/localisation, AI parity, documentation, and handoff are present.
No blocker remains within this tranche.
