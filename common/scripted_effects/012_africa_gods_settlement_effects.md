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

## Commit, classification, and reward

`gods_of_africa_commit_final_settlement = yes` runs on the current active host and fails before the authoritative endpoint.
It sets the host final-commit receipt before iterating, closing ordinary response/dispatch authority.
Each candidate calls `gods_of_africa_commit_participant_settlement = yes`.
This participant COUNTRY effect requires valid retained history, the host final-commit receipt, and no already committed outcome.
It saves regular `gods_of_africa_settlement_host` from the actual settling host and delegates grading, reward, live cleanup, and report presentation in that order.
There are no caller parameters, inferred recipients, or defaults.

The grading helper guards its own direct calls, retains the existing Enemy/Favored/Respected/Distrusted priority and thresholds, and snapshots five normal fields before public Strength is zeroed: settlement generation, origin, historical generation, Strength, and doctrine.
Permanent opt-out remains an Enemy condition independently of cleared live defiance.
The final standing and `gods_of_africa_final_outcome_committed` are durable.
Full-spec ratios, streaks, final-campaign contribution, and capability-scaled rewards require their separate accepted grading tranche; this lifecycle contract does not claim those factors already exist.

The reward helper requires retained history, a committed valid endpoint, a present standing, and no `gods_of_africa_settlement_reward_granted` receipt.
It sets that receipt once, uses the existing Favored/Respected quantities and native affordability/reserve gates, and preserves the existing fuel and common-defence ledger debits.
Native `send_equipment` sends actual infantry equipment variants from Africa to the explicitly captured participant; there is no recipient equipment synthesis.
Existing political-power branches and diplomatic memories remain unchanged by this coverage repair.
Their full-spec balance and material fallback disposition remain separate from lifecycle acceptance.
Neither report presentation nor acknowledgement grants a reward.

Finalization is itself guarded by retained history, a committed valid standing, and the owner endpoint.
It withdraws owned protection, removes live missions and permissions, remembers durable opt-out before removing live defiance, clears quote/payment/substitute work, and clears the participant authority flag.
It retains history, outcome, reward, and settlement snapshots.
Host cleanup clears the live registries and their counters once after the census pass.

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
The existing action and tooltip describe all surviving participants; no decision row, category, currency, or public meter is added.

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

## Evidence and further accepted work

Source and scenario evidence belong in `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_survivor_settlement_2026-10-03.md` and its independent audit.
The architecture source is `012_africa_gods_survivor_victor_design_2026-10-03.md`; the parent accepts its survivor method within the user's complete-Gods goal and queues explicit bilateral victor renewal as the next authority tranche.
Meaningful cases include live and archived survivors, zero-conduct enrollment, converted historical actors, vanished objects, never-enrolled candidates, the exact inherited generation, wrong origin or owner stamp, replayed acknowledgement, direct early helper calls, and native donor affordability/reserve checks.
No in-game execution, clean error.log, complete weighted validation, or full Gods completion is claimed by source proof.
The native collection and inherited-origin contracts retain their separate runtime acceptance limits.
