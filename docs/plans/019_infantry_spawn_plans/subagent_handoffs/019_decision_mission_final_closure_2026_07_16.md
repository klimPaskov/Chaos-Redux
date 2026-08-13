# Event 019 final decision/mission closure audit

## Closure date and authority

Date: 2026-07-16

This is the fresh, read-only final closure audit for the Event 019 decision and
mission surface. The authoritative inventory is
`docs/specs/019_infantry_spawn_specs/matrices/019_decision_mission_map.md`, with
AI expectations cross-checked against
`docs/specs/019_infantry_spawn_specs/matrices/019_ai_strategy_matrix.md` and the
decision/UI/AI contract in
`docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_7_decisions_ui_ai_balance.md`.

The audit used the `chaos-redux-subagents` and `chaos-redux-decisions-missions`
workflows. The required offline wiki pages and the vanilla decision, scripted
GUI, trigger, effect, variable, and script-constant documentation were reviewed
before source inspection. No gameplay, localisation, asset, GUI, category,
registry, or spreadsheet file was edited.

## Severity verdict

| Severity | Open findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |

The bounded 77-object decision/mission matrix is clean. B-019-001 and
B-019-002 remain separate approval blockers and are not included in these
severity totals.

## Inventory closure

A brace-aware source inventory found exactly 77 child objects under the three
Event 019 categories:

| Source | Decisions | Missions | Total | Object span |
| --- | ---: | ---: | ---: | --- |
| `common/decisions/019_infantry_spawn_decisions.txt` | 35 | 10 | 45 | lines 10-873 |
| `common/decisions/019_infantry_spawn_claimant_decisions.txt` | 6 | 0 | 6 | lines 9-160 |
| `common/decisions/019_infantry_spawn_derivative_decisions.txt` | 23 | 3 | 26 | lines 26-626 |
| **Total** | **64** | **13** | **77** | |

The three category registrations are present exactly once and carry live
runtime visibility gates rather than relying on load-time `allowed`:

- ordinary management:
  `common/decisions/categories/019_infantry_spawn_decision_categories.txt:11-37`;
- claimant command:
  `common/decisions/categories/019_infantry_spawn_claimant_categories.txt:10-20`;
- derivative operations:
  `common/decisions/categories/019_infantry_spawn_derivative_decision_categories.txt:10-25`.

The ordinary category excludes derivatives and stays visible only for a live
Event 019 management state, running mission/cooldown, unresolved lot, Evolution
III board access, or an open board. The claimant category requires active Event
019, Evolution III, and the claimant system. The derivative category requires a
derivative country and one of its live operations/crisis flags. All three also
require the scenario transaction to be idle.

## Object schema, gating, costs, and tooltips

The parser checked fields at object depth rather than counting nested text:

- all 64 decisions have `icon`, `visible`, `available`, `complete_effect`, and
  `ai_will_do`;
- all 13 missions have `icon`, `activation`, `available`,
  `days_mission_timeout`, and `timeout_effect`;
- every decision completion body exposes a `custom_effect_tooltip` (35 ordinary,
  6 claimant, and 23 derivative);
- all 50 custom-cost decisions have a one-for-one `custom_cost_trigger` and
  `custom_cost_text` pair;
- 5 decisions use ordinary political-power `cost`; and
- the remaining 9 decisions are deliberately free view, selection, lifecycle,
  or destructive-choice actions, while all 13 missions correctly have no
  purchase cost.

The nine no-purchase decisions are the board opener, the two lot selectors,
supervised demobilization, emergency field integration, emergency-reserve
recognition, the lot survey, prototype cannibalization, and claimant-demand
refusal. Their availability gates and completion tooltips expose the actual
state change or sacrifice; none is an unguarded paid action.

The ordinary definitions at
`common/decisions/019_infantry_spawn_decisions.txt:53-748`, claimant definitions
at `common/decisions/019_infantry_spawn_claimant_decisions.txt:9-160`, and
derivative definitions at
`common/decisions/019_infantry_spawn_derivative_decisions.txt:26-604` all use
the same reusable trigger/effect entry points that revalidate state at
execution. Costs are debited inside those effects only after the corresponding
availability/preflight succeeds; custom decision costs are not assumed to be
automatically deducted by the engine.

## Mission lifecycle and cooldown closure

The ten ordinary missions are defined at
`common/decisions/019_infantry_spawn_decisions.txt:755-873`. Their activation
triggers are intentionally false for manual creation and each mission is
started with `activate_mission` only by its owning effect. Running flags provide
visibility, timeout handlers defer or complete the same owning workflow, and
the Event 019 cleanup effect removes all ten missions at
`common/scripted_effects/019_infantry_spawn_management_effects.txt:7408-7417`.

The three derivative missions are defined at
`common/decisions/019_infantry_spawn_derivative_decisions.txt:465-485`,
`:567-585`, and `:605-626`. Their package effects explicitly activate them, and
derivative cleanup removes all three. Cancel and timeout effects clear or route
the same integration, submission, and opening-crisis state, so no invisible
or orphaned mission path was found.

Request cooldown is a real mission and flag pair: ordinary success activates it
at `common/scripted_effects/019_infantry_spawn_management_effects.txt:5040-5055`,
selected-family success activates the same mission at
`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1188-1204`,
and its timeout clears the cooldown through the shared completion helper.
Claimant counter-command and discredit use their explicit constant-backed
`days_re_enable` values at
`common/decisions/019_infantry_spawn_claimant_decisions.txt:94-136`.
Derivative reinforcement, fragmentation, and submission decisions use their
own package flags and bounded cooldown effects.

## Scripted GUI parity

The Muster Board is human-only and is gated by the same live board-availability
trigger at
`common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:9-20`.
Every gameplay button in its effect table (lines 22-103) calls the shared action
effect also used by the corresponding decision or AI route. Every enabled check
in lines 105-204 calls the matching shared `can_*` or payment trigger.

This pair audit covers lot audit, territorial assignment, training,
standardization, specialist preservation, demobilization, emergency
integration, both prototype outcomes, all five request modes, all six claimant
responses, selected-family reinforcement/training, cantonment, liaison,
restricted deployment, sustainment, containment, and dispersal. Tabs, list-row
selection, refresh, animation state, and claimant cycling alter view state only.
The GUI declares `ai_enabled = { always = no }` at line 234, so AI behavior does
not depend on clicking the human interface.

## AI equivalence and liaison dispatch

All 64 decisions have explicit `ai_will_do`. The only deliberately disabled
decision weights are:

- four view/selection helpers: open board, select next ordinary lot, select next
  unaccounted lot, and survey lots; and
- the seven ordinary anomalous-family buttons whose AI route is centralized in
  `infantry_spawn_run_anomalous_family_ai`.

All other ordinary actions, all six claimant responses, and all 23 derivative
decisions have live weighted paths with their availability gates intact. The
per-country Event 019 pulse selects safe lot targets for ordinary AI, processes
affordable obligations, routes claimant-demand responses, and calls the
central anomalous-family dispatcher; it does not require the scripted GUI.

The family AI is bounded to the highest-pressure visible family and uses the
same view and transaction effects as the player
(`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1488-1595`).
Critical pressure weights containment and dispersal. Ordinary pressure weights
sustainment, cantonment, restricted deployment, and liaison together. Liaison
is specifically:

- gated by `infantry_spawn_can_appoint_selected_family_liaison` at line 1560;
- assigned `ordinary_liaison` plus the field-prophet bonus at lines 1561-1565;
- included in the common total at line 1570; and
- dispatched through the same
  `infantry_spawn_appoint_selected_family_liaison` effect at line 1577.

If no ordinary family-management action is available, the same dispatcher can
take the guarded family reinforcement/training transaction at lines 1580-1592.
This closes claimant/family liaison participation in ordinary weighting and
dispatch rather than treating liaison as a player-only exception.

## Paid-request transaction closure

The previous selected-family transaction handoff was rechecked against the
current source rather than accepted by reference.

### Immutable payment baseline and rollback ordering

`infantry_spawn_snapshot_management_request_payment_resources` captures exact
pre-debit army experience, political power, command power, manpower, fuel,
ordinary equipment, and coal-golem equipment at
`common/scripted_effects/019_infantry_spawn_management_effects.txt:4431-4442`.
`infantry_spawn_verify_management_request_payment_resources_restored` compares
every balance for exact equality and quarantines any mismatch at lines
`4447-4468`.

The ordinary request snapshots payment and structure before preparation or
debit at lines `5012-5025`. Its failure branch runs structural rollback first,
admits a single refund only when rollback proof is valid, and then checks exact
resource restoration at lines `5060-5069`.

The selected-family path snapshots payment before the provider debit at
`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1146-1162`
and snapshots structure only after provider and overhead payment have both
succeeded at lines `1163-1178`. Materialization failure runs structural
rollback first and admits the overhead and provider refunds only when rollback
is valid at lines `1211-1221`. Provider-only payment failure paths restore or
prove the same immutable baseline at lines `1224-1239` before any structure has
been published.

`infantry_spawn_rollback_management_request_transaction` contains no payment
refund. It removes the created engine objects and every published tail, restores
the reusable generation tail, flags, prototype stockpiles, and aggregate
variables, and then proves exact structural restoration at
`common/scripted_effects/019_infantry_spawn_management_effects.txt:4608-4866`.
When that proof fails, no refund, success credit, request count, cooldown,
control debit, or final training authorization is reachable.

### Six allocator endpoints

The structural snapshot captures the generation, lot, template, unit,
obligation, and deletion-cohort allocator endpoints at
`common/scripted_effects/019_infantry_spawn_management_effects.txt:4505-4510`.
Expected values are derived from exact published-row deltas at lines
`4932-4959`; the common verifier proves all six endpoints at lines `4985-4990`.

Selected-family training additionally constrains generation advance to zero or
one, lot/template to one, and unit/obligation/deletion-cohort to zero at
`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:972-983`.
Selected-family spawn constrains generation to zero or one,
lot/template/unit/deletion-cohort to one, and obligations to two at lines
`1082-1087`. Rollback permits harmless monotonic identity gaps but rejects any
allocator regression at management-effect lines `4835-4841`.

### Exact family rows, obligations, and aggregates

Training proves the exact new lot, template, component, selected-state,
locked-template, and trainable-family tails; unchanged unit and obligation
counts; unchanged division, debt, and manpower aggregates; exact global totals;
and all allocator expectations at
`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:919-1007`.

Spawn proves one exact new lot, template, selected-state row, unit,
locked-template row, spawn-only row, and transfer-eligible row, plus exactly two
obligations at lines `1010-1136`. The obligation proof checks consecutive UIDs,
generation/lot/unit links, manpower then provider resource profile, issued,
paid, salvageable, outstanding, debt-value, and status fields, exact lot debt
and manpower, and exact country/global aggregates. Provider obligation creation
resets the debt override and publishes those two rows at
`common/scripted_effects/019_infantry_spawn_ledger_effects.txt:725-743`.

### Final non-refundable engine setter

HOI4 exposes no documented trigger that can read back
`force_allow_recruiting`. The implementation therefore proves the fresh
training template, all rows, aggregates, endpoints, and payment commit first.
Only inside the successful, non-refundable branch does
`infantry_spawn_commit_selected_family_training_authorization` apply
`set_division_force_allow_recruiting` and the template lock
(`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:875-888`,
called at lines `1206-1209`). No refund path is reachable after that setter.

## Registry and on-action constraints

A filename and provider-hook scan found exactly one Event 019 registry
implementation:

`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`

The three provider payment/refund pairs also live only in that file at lines
`4123-4176`, `4279-4328`, and `4437-4490`, and each clears its paid token after
refund. No second Event 019 registry file or duplicate provider payment hook was
found.

A scan of every Event 019 reference under `common/on_actions/` found no
`on_daily`, `on_weekly`, or `on_monthly` Event 019 hook. The only Event 019
on-action files use lifecycle events such as capitulation/annexation; recurring
management remains a bounded, self-rescheduling country pulse.

## Separate approval blockers

These are not decision/mission severity findings and were not simplified or
worked around:

- **B-019-001 — exact live recorded-formation subset ownership transfer.** The
  available native capability is still false. Recreate/prove/delete would lose
  live division state such as organisation, veterancy, medals, officer/order
  assignment, and related identity, so that fallback remains unapproved.
- **B-019-002 — exact same-battle achievement attribution.** The engine-facing
  implementation still cannot atomically prove the exact recorded division,
  battle victory, duration/ratio threshold, and casualties for all four
  achievements. The controlled combat-trial substitute remains unapproved;
  the helper stays unwired and the achievements remain hidden/unawarded.

## Source freeze and audit artifacts

The audited source did not change between the opening inventory and the final
transaction pass. Final SHA-256 fingerprints were:

| File | SHA-256 |
| --- | --- |
| `common/decisions/019_infantry_spawn_decisions.txt` | `B4468D40043D70FFDF31D658EA600FA2FA284C5DBAC86422C04D11B46DE020E0` |
| `common/decisions/019_infantry_spawn_claimant_decisions.txt` | `85D9E1CB78C37A1B554F32065FA923E5E4E15B092087F303750DB5F4EF54233B` |
| `common/decisions/019_infantry_spawn_derivative_decisions.txt` | `644566ADF9DAADB672C61518495F8BD85749611BF3AC38E2BF7875E1FAC92058` |
| ordinary/claimant/derivative category files | `43B7DAFB...70AF159` / `B196651F...E7DA7A8BB` / `B308B19F...4E5C6D43` |
| `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt` | `0CEE0046D48F19766976764D1DA5407F6FE7DB08F0DA2A8A0B669D4315F03A9A` |
| `common/scripted_effects/019_infantry_spawn_management_effects.txt` | `260F1C42EFC6BDBE34F1A63F5540538FB543520CFE087B3ADC6DFF1FDE691A31` |
| `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt` | `FD6BF31E41DAA05907302214CD46C6A63C6C0546BF77D498038A37B01454AFFA` |
| `common/scripted_effects/019_infantry_spawn_ledger_effects.txt` | `C0B5255D4EC2A6C38312E32634A7ED1BC79C94D56334D2DA409B69CDB77E92EC` |
| `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt` | `F5582496605395431EF38AF798D6C56D05DD2CF91B7CF8C89D57A42F87C3D90A` |

This handoff is the only file produced by the audit. It is a static source
closure, not an engine runtime claim. No fallback, placeholder, weakened
substitute, or other simplification was introduced.
