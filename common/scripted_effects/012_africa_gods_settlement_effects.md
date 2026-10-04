# Gods survivor settlement contract

The Event 012 owner closes ordinary tribute once the authoritative Scramble phase is settled or `africa_continental_settlement_complete` exists.
It performs one bounded pass over `gods_of_africa_candidate_registry`, using retained enrollment history rather than current major status, current participation, or a non-capitulated-country requirement.
Existing historically enrolled objects remain eligible after capitulation, archival, or later special/nonhuman conversion.
The current host, nonexistent objects, and never-enrolled census entries are excluded.
This changes no enrollment rule for special/nonhuman countries.

Both registries contain unique entries from the engine's `global.countries` array, and their physical capacity is that native array's current cardinality, read as `global.countries^num` without another scan.
Candidate insertion compares actual candidate-array size to this bound; enrollment compares actual live-array size and requires durable candidate membership.
The public registration helper attempts candidate insertion before its guard, including for direct callers.
A native country absent from a unique subset necessarily has capacity; when the subset reaches the native cardinality it already contains every native country.
Registration cannot commit a genuine enrolled ledger outside the final census.
Scalar bookkeeping counts and a fixed count of tag definitions do not establish storage capacity.

## History and lineage proof

`gods_of_africa_participant_has_settlement_history = yes` is a COUNTRY trigger.
Inputs are an existing history-initialized flag or history-count marker, the participant generation, the explicit current host, and optional stamped history owner/origin.
No input or counter is manufactured by evaluation.
An existing owner stamp must equal `THIS.id`.
Current-generation records require the same current generation and a matching origin when that origin stamp exists.
The explicitly inherited branch requires a present participant origin matching both the current host origin and its inherited origin, and the participant generation exactly equal to the one staged old host generation.
It never treats every earlier generation as valid.

Genuine enrollment stamps history owner and origin only when absent, preserving them during re-entry and cleanup.
The one-use host-transfer transaction copies `global.africa_host_transfer_old_generation` and `global.africa_host_transfer_origin_host_id` into normal successor `gods_of_africa_inherited_history_generation` and `gods_of_africa_inherited_history_origin_host_id` while restoring the maintained census.
No additional lineage array, discovery scan, or clock is introduced.
Current-generation history predating the stamps retains its existing country-local initialization/generation proof; unproven inherited origin is rejected.
Country-object cloning, slot reuse, and historical migration without origin proof remain separate runtime/coverage questions.

## Commit, classification, and obligation

`gods_of_africa_commit_final_settlement = yes` runs on the current active host and fails before the authoritative endpoint.
It sets the host final-commit receipt, freezes `gods_of_africa_settlement_final_strength` and `gods_of_africa_settlement_final_doctrine` once, and then runs three bounded passes over the retained candidate census.

| Phase | Helper (scope) | What it does |
| --- | --- | --- |
| 1 | `gods_of_africa_settlement_classify_participant` (census entry) | Requires `gods_of_africa_settlement_can_commit`. Saves the regular `gods_of_africa_settlement_host` target, neutral-retires any open demand, refreshes the conduct record, calls `gods_of_africa_freeze_final_grade_inputs`, and classifies Enemy, then Favored, then Respected, then Distrusted with the `gods_of_africa_full_grade_*_is_valid` triggers. Stores the report cause in `gods_of_africa_settlement_cause`. A broken accounting invariant leaves `gods_of_africa_grading_unresolved` and `gods_of_africa_settlement_grade_unresolved` with the evidence intact and assigns no standing. |
| 2 | `gods_of_africa_initialize_settlement_obligation` (census entry) | Once per country: `gods_of_africa_calculate_settlement_entitlement`, then the frozen receipt (`gods_of_africa_reward_source_id`, `_source_generation`, `_source_origin_id`, `_receiver_id`) and the equipment and fuel entitlement, owed, and delivered amounts. Zero entitlement completes the obligation at once (`gods_of_africa_settlement_reward_granted`); otherwise `gods_of_africa_settlement_delivery_pending`. Calls `gods_of_africa_apply_settlement_diplomacy` once. A missing entitlement sets `gods_of_africa_settlement_obligation_unresolved` and never pretends zero. |
| 2 | `gods_of_africa_initialize_settlement_delivery` (host) | Sets `gods_of_africa_settlement_delivery_initialized` and computes the host owed totals in thousands. |
| 3 | `gods_of_africa_deliver_settlement_obligations` (host) | One bounded batch (below). |
| 3 | `gods_of_africa_settlement_finalize_participant` (census entry) | Finalizes live authority and sends `.608`. |

Entitlements follow the accepted formula: equipment `floor(min(ceiling, 1000 * C * B))`, fuel `floor(min(ceiling, 500 * C * B))`, with `C = min(16, M + 0.5 V + 0.5 L)` in packages, `B = (1 + 2S) * doctrine multiplier` for Favored (Reciprocal Covenant 1.25), `B = 0.25 + 0.75S` for Respected, and `B = 0` for Distrusted and Enemy.
Favored ceilings are 50000 equipment and 25000 fuel; Respected ceilings are 10000 and 5000.
For each component, `entitlement = delivered + owed` always holds.

Standing diplomacy (`gods_of_africa_apply_settlement_diplomacy`, once per country):

| Standing | Diplomacy |
| --- | --- |
| Favored | `gods_of_africa_settlement_honor` (+50) both ways, and Africa guarantees the country when they are at peace and no guarantee exists. |
| Respected | `gods_of_africa_settlement_favor` (+30) both ways, and a non-aggression pact when they are at peace and none exists. |
| Distrusted | Africa holds `gods_of_africa_settlement_suspicion` (-20) toward the country. |
| Enemy | `gods_of_africa_settlement_hostility` (-60) both ways. |

## Donor-backed delivery

`gods_of_africa_deliver_settlement_obligations` runs on the settling host for the first batch at the endpoint and again each time the host takes **Deliver settlement support** (`gods_of_africa_deliver_settlement_support`, host category, visible only while `gods_of_africa_settlement_source_has_pending_delivery` holds on the deciding country itself, enabled while `gods_of_africa_settlement_source_has_spare_stock` holds, 30-day re-enable).

1. Recompute the owed totals in thousands from valid receipts (`gods_of_africa_settlement_receipt_is_owed_by_source`): the receipt's source ID, generation, and origin must match the deciding host, and its receiver ID must match the receiver. A vanished receiver drops out; its receipt is never moved to another country.
2. Equipment budget: the greatest shipment `q`, at most the 20000 batch ceiling, the owed total, and the common-defence ledger above its 500 floor, for which `has_equipment` still leaves the army reserve (`max(500, ceil(0.1 * army infantry requirement))`). Found by a halving search of at most 16 steps.
3. Fuel budget: fuel above the 500 floor, at most 20000, read in thousands and bounded before conversion.
4. Each receiver's fuel basis is `min(fuel owed, free tank space)`; a full tank leaves the debt owed.
5. Proportional pass: each receiver gets `floor(A * share_k / T_k)`, multiplied before dividing; then one residual pass gives at most one more unit per receiver while budget remains. A receiver at war with Africa is skipped this batch and keeps its balance.
6. Every shipment is measured on both sides (`num_equipment@infantry_equipment`, `fuel_k`); only the common delivered amount leaves the owed balance, joins the delivered total, and (for equipment) leaves the common-defence ledger.
7. A receiver whose two balances reach zero gets `gods_of_africa_settlement_reward_granted`, and the totals are recomputed.

Finalization withdraws owned protection, removes live missions and permissions, remembers durable opt-out before removing live defiance, clears quote/payment/substitute work, and clears the participant authority flag.
It retains history, outcome, obligation, and settlement snapshots.
Host cleanup clears the live registries once after the census pass and keeps the candidate census for later deliveries.

## Independent receipt lifetime

`gods_of_africa_settlement_receipt_is_current = yes` requires the recipient to exist, a durable outcome, pending presentation, one valid standing enum, settlement generation/origin snapshots, and the regular frozen settlement host.
That frozen host must still exist, carry its final-commit receipt, and match both snapshots.
The check does not follow a later global `africa_host` replacement, require active Gods authority, require live roster membership, or reject a capitulated recipient.
Regular event targets travel into `.608` with the originating effect chain under the installed event-target contract.

`gods_of_africa_acknowledge_settlement = yes` consumes only pending presentation after this proof.
It never removes from a host array, decrements a host counter, clears the standing/outcome/reward receipt, or erases history.
A replay with no pending presentation is a no-op.
A vanished or changed frozen host rejects presentation while preserving committed accounting; exact native object/event lifetime remains unobserved.

The existing targeted `gods_of_africa_commit_settlement` helper delegates the complete terminal pass to the host once its continental flag is valid.
After the endpoint, the settling host's delivery row is the only settlement action; no currency or public meter is added.

## Usage and assets

Owner endpoint:

```text
gods_of_africa_commit_final_settlement = yes
```

Internal census country:

```text
gods_of_africa_commit_participant_settlement = yes
```

The participant helper requires the owner's endpoint to be committed first.
Direct early grading, reward, finalization, or receipt acknowledgement fails its own guard.
`.608` retains `GFX_report_event_012_africa_gods_settlement`, registered in `interface/012_africa_event_pictures.gfx`.
No image, DDS, new GUI, icon, portrait, or model is produced for this coverage repair.

## Evidence and limits

Design and scenarios: `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_full_grading_rewards_design_2026-10-03.md` (scenarios `G12_*`), implemented under the 2026-10-04 takeover.
The survivor census and lineage proof are documented in `012_africa_gods_survivor_settlement_2026-10-03.md` and its audit.
Native `send_equipment` variant selection, the exact fuel and equipment deltas, and the decision row's appearance are live-game checks; no in-game run is claimed here.
