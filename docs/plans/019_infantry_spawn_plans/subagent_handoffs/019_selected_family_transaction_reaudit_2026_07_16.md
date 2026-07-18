# Event 019 paid-request transaction re-audit

## Closure - 2026-07-16

This is the read-only gameplay re-audit of the ordinary paid-request and
ordinary-country selected-family paid-request transactions after remediation of
the earlier refund, allocator, obligation, and training-authorization findings.
The gameplay audit used the `chaos-redux-events`, `chaos-redux-subagents`, and
`hoi4-decisions-missions` workflows. No gameplay or registry file was edited by
this audit.

### Severity verdict

| Severity | Open findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |

The previous P1-1 through P1-4 findings and P2-1 finding are closed in the
current worktree.

### Payment snapshots and refund proof

- `infantry_spawn_snapshot_management_request_payment_resources` captures the
  immutable pre-debit balances for army experience, political power, command
  power, manpower, fuel, ordinary request equipment, and coal-golem equipment
  in
  `common/scripted_effects/019_infantry_spawn_management_effects.txt:4428-4442`.
- `infantry_spawn_verify_management_request_payment_resources_restored` checks
  every captured balance for exact equality after the applicable refund hooks
  and quarantines the country on any mismatch at the same file's lines
  `4444-4468`.
- The ordinary request takes both its payment and structural snapshots before
  preparation or payment at lines `5012-5025`. Its failure branch runs the
  structural rollback, requires `infantry_spawn_request_rollback_valid`, refunds
  at most once, and then runs the exact resource proof at lines `5060-5069`.
- The selected-family request takes its pre-payment resource snapshot before the
  provider debit at
  `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1146-1162`.
  After both provider and overhead payment succeed, it takes the separate
  structural snapshot at lines `1163-1178`. A failed materialization performs
  structural rollback first, admits both refund hooks only when rollback is
  valid, and then proves the pre-payment balances exactly at lines `1211-1221`.
- If overhead payment fails, no lot, template, unit, ledger, or allocator has
  been published. The provider-only debit is reversed once and immediately
  checked against the pre-payment snapshot at lines `1224-1232`. If provider
  payment itself fails, no refund hook runs and the same equality proof detects
  any partial debit at lines `1234-1238`.

`infantry_spawn_rollback_management_request_transaction` contains no payment
refund. It performs only engine-object, ledger-tail, flag, prototype-stockpile,
and aggregate restoration and proof at
`common/scripted_effects/019_infantry_spawn_management_effects.txt:4604-4866`.
The ordinary refund helper also clears its payment-success token at lines
`4593-4602`; the family overhead and provider refund helpers clear their own
paid tokens. The reviewed callers contain no reachable double-refund path.

### Monotonic allocator proof

The structural snapshot captures the generation, lot, template, unit,
obligation, and deletion-cohort allocator endpoints at
`common/scripted_effects/019_infantry_spawn_management_effects.txt:4505-4510`.
`infantry_spawn_prepare_management_request_allocator_expectations` derives each
expected endpoint from its exact published row delta at lines `4932-4959`, and
the common materialization verifier proves all six endpoints at lines
`4985-4990`.

For selected-family training, the runtime proof constrains generation advance to
zero or one, lot and template advance to one, and unit, obligation, and
deletion-cohort advance to zero at
`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:972-983`.
For selected-family spawn, the proof constrains generation advance to zero or
one, lot/template/unit/deletion-cohort advance to one, and obligation advance to
two at lines `1082-1087`, on top of the common exact endpoint checks.

The ordinary path reaches `infantry_spawn_prepare_request_generation_context`
once. That helper either reuses the sole latest open/audited generation or
allocates and appends exactly one generation row
(`common/scripted_effects/019_infantry_spawn_core_effects.txt:321-380`), so its
generation allocator delta is likewise exactly zero or one. Allocators are
never rewound during rollback; the rollback proof rejects regression while
preserving harmless failed-transaction identity gaps at management-effect lines
`4835-4841`.

### Exact family publication proof

Training proves the exact fresh lot, template, component, selected-state,
locked-template, and trainable-family tails; unchanged unit/obligation counts;
unchanged division/debt/manpower totals; exact global totals; and exact
allocator endpoints at
`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:919-1007`.

Spawn proves exactly one fresh lot, template, selected-state row, unit,
locked-template tail, spawn-only-template tail, and transfer-eligible-unit tail,
plus exactly two obligations at lines `1010-1136`. The two obligation rows are
proved as:

- consecutive monotonic UIDs;
- exact generation, lot, and unit links;
- manpower followed by the provider resource profile;
- exact issued, paid, salvageable, outstanding, debt-value, and status fields;
- exact lot outstanding manpower/debt; and
- exact country manpower-liability/equipment-debt aggregates.

The relevant row and aggregate checks are at lines `1034-1058` and
`1071-1129`; auxiliary tail identity checks are at lines `1105-1107`.

`infantry_spawn_record_provider_unit_obligations` explicitly resets
`infantry_spawn_current_obligation_debt_value_override` before either provider
row at
`common/scripted_effects/019_infantry_spawn_ledger_effects.txt:725-743`, so an
ordinary obligation override cannot leak into an anomalous family obligation.

### Training engine commit ordering

HOI4 exposes setters but no documented read trigger for
`force_allow_recruiting`. The script therefore proves the complete fresh
template, ledger, allocator, and paid transaction first. Only after the success
branch has become non-refundable does
`infantry_spawn_commit_selected_family_training_authorization` apply
`set_division_force_allow_recruiting` and the template lock
(`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:875-888`,
called at lines `1206-1209`). No refund branch is reachable afterward.

### Syntax, scope, and registry constraints

The political-power and command-power snapshots use documented country game
variables on the right-hand side of `set_temp_variable`; their equality checks
remain in the same country-scoped effect chain. Payment flags, expected
allocator values, provider obligation inputs, and current stable UIDs remain
temporary values in that same chain. The three reviewed effect files have
balanced script blocks, and the remediated ordering introduces no unsupported
scope transition.

No Event 019 registry file was created or edited. The sole dedicated registry
implementation remains
`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`.

### Remaining blockers or simplifications

None for this bounded transaction surface.
