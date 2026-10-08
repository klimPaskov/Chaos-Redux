# Missile CBRN caller follow-up

Date: 2026-10-07.
Disposition: read-only follow-up with one remaining caller-storage defect.
Acceptance basis: parent requested review of peer commit `5793df4345a413dcf7cadf5aeae99597a859020a` and its current Event 032 chemical consumer.
Owned changes: this handoff and `2026-10-07_missile_cbrn_caller_followup.json` only.
No source, index, shared tests, framework, or commit was changed.

## Result

The current `missiles_dispatch_chemical_payload` has justified partial caller ownership and does not need a blind full-60 allocation.
It owns 38 output slots before reset, including the additional `cbrn_action_civilian_deaths` consumed by Event 032 afterward.
Eight additional public action inputs are set unconditionally in its own frame before the returning getters or prepare helper consume them.
One necessary returned field is missing: `cbrn_action_retaliation_status`.
The minimal candidate fix is one existing-name caller declaration with `constant:cbrn_retaliation_status.none` before reset/prepare.
This report proposes that fix but does not apply it.

`missiles_check_chemical_payload_stock` no longer exists in the current source.
Its old insertion-map entry should not be applied to this source version.

## Actual boundaries and field map

| Boundary | Actual storage and use | Assessment |
| --- | --- | --- |
| Reset at line 4421 | The owner first allocates 38 fields at 4383-4420, then calls `cbrn_reset_action_context`. | Returning reset modifications retain the existing output slots. Optional reset fields omitted by this specialized owner are considered separately below. |
| Direct inputs at 4427-4433 and 4458 | Target proof, weapon class, exact agent, strategic route, strategic severity, late-route authorization, release efficiency, and explicit missing-condition receipt are created in the missile owner. | These values already have caller storage. Repeating them in a pre-reset full packet would not solve an additional return problem. |
| Agent getter at 4459 | `cbrn_chemical_air_raid_set_agent_class_internal` updates the already-owned class slot. | Covered. |
| Frozen payload receipt at 4461-4463 | Required and consumed payload are copied directly from the saved preparation-time `missiles_operation_payload_consumed`, and proof is directly assigned before the existing verified-debit gate. | Covered for temporary lifetime. This source review does not certify the real custody receipt or payment transaction. |
| Protection and doctrine at 4470-4471 | Military/civilian protection outputs, both mask-only casualty outputs, protection proof and doctrine multiplier have owner storage. | Covered. Shared private profile and weight storage is committed, as described below. |
| Prepare at 4472 | Result, rejection reason, victim proof, all exposure outputs, source label and conditional vehicle/armored receipts are owned. | Covered except the returned retaliation status. |
| Generic retaliation classifier inside prepare, exposure line 958 | `cbrn_prepare_chemical_action_record` calls the generic classifier, which can return authorized status. Neither the current missile caller nor prepare owns that output before its producer. | Concrete missing ownership at the generic-to-prepare and prepare-to-missile returns. One ancestor declaration in the missile frame covers both. |
| Dispatch at 4477 | `cbrn_action_dispatch_proof` is owned by the missile caller and is not reset by the dispatcher. Existing dispatcher guard and private consequence declarations are preserved. | Covered for the inspected return contract. No complete sink transaction was executed here. |
| Event 032 record at 4478-4479 | Delivery result and civilian deaths are saved after dispatch. The civilian-death temporary is explicitly owner-initialized at 4420. | Death-result forwarding is covered, rather than relying solely on the dispatcher's private local slot. |

The retaliation status is consumed by state consequence history, condemnation, confirmed-use recording, unified action records, and actor last-use history in `cbrn_consequence_effects.txt`.
The generic classifier can persist `cbrn_last_retaliation_action_status` while its returned temporary disappears.
This permits the saved retaliation receipt and chemical consequence record to disagree under the conservative helper-frame model.

The preparation helper creates `cbrn_retaliation_action_proportionate_proof` before calling the classifier, and the classifier consumes it within that same preparation frame.
It is not a forwarded result consumed by this missile owner.
The current strategic route cannot enter the tactical proportionate branch, so this field does not create another missile ownership requirement.

## Why the complete 60-field reset is not required here

The three repaired native raid owners were general complete-record consumers with broad returned defaults and outputs.
This missile adapter specializes a fixed strategic chemical route and sets its known inputs directly.
Of the original 60 packet fields, 45 have current direct owner assignments or initial owner output storage, and one additional owner slot stores civilian deaths outside that packet.
Fifteen packet fields are omitted, but only retaliation status is a missing returned output in the current route.

The nine optional condition inputs are weather, terrain, target density, command, evidence control, context condemnation, forecast confidence, command integration, and base friendly risk.
The caller explicitly sets `cbrn_action_conditions_resolved_proof` to missing.
The exposure calculator uses its local zero condition defaults and reads those optional inputs only through the existing resolved-condition gate.
There is no returned condition getter in this missile path that would require owning those nine omitted fields.
Changing that receipt or supplying fabricated condition values would alter the mechanism rather than repair its lifetime.

The remaining five harmless omissions are the nested proportionate proof discussed above, legacy cylinder-source proof not used by this frozen strategic receipt, optional evidence-floor override, optional duration override, and the no-release air-attempt dispatch proof not used by this missile release path.
The optional override readers retain their original zero/absent behavior and guards.
The reset helper still resets any already-existing ancestor temporaries for these fields.
This assessment applies to the current inspected route and should be revisited if a later change adds a returned getter, consumes those fields after return, changes their defaults, or introduces a new missile action route.

No full-60 initializer, new output family, parameter wrapper, or payment path is proposed.

## Bounded conservative-frame reproduction

Reused the existing Event 026 parser and strict returning-helper VM unchanged in an in-memory probe.
The probe executes the actual missile allocation/reset prefix, then the actual preparation accepted branch and actual generic retaliation classifier.
It supplies existing actor/victim/state scopes, a war, and active retaliation rights as explicit fixtures.
Victim binding, doctrine calculation and exposure calculation are excluded fixture boundaries.
It does not execute all prepare validation, missile custody, outcome selection, damage, dispatch, or record sinks.

| Probe | Saved generic last status | Returned action status | Prepared result |
| --- | --- | --- | --- |
| Current caller | Authorized 1 | Dropped | Accepted 1 |
| In-memory candidate with one caller declaration | Authorized 1 | Authorized 1 | Accepted 1 |

This proves the bounded temporary-output defect and effect of the minimal declaration in the source model.
It does not establish native execution or whole-transaction correctness.
Probe results and exact hashes are retained in the JSON companion.
One attempted probe had a test-only syntax error, and a later attempt asserted the wrong fixture argument shape for `has_war_with`.
Both failed before producing accepted evidence and did not modify source.

## Committed dependency coverage

Peer commit 5793 contains the eighteen exposure route/class/exact-agent profile allocations in `cbrn_calculate_chemical_action_outputs`.
It also contains the six generic outputs before the first returning protection calculation in `cbrn_resolve_action_target_protection`, with that storage covering its two passes.
The exact `cbrn_calculate_action_protection` AST matches the version committed by our `611cbb63` patch, including its six private weight declarations.
The peer commit therefore preserves those six weight fixes.

The previously untracked `cbrn_payload_reservation_effects.txt` is present in commit 5793 and has exact committed and working SHA-256 `fd8535a93429919eff2a0b22e0d9b5906872ee78c34d6fa96f4dbd9fe07c02f2`.
Its `cbrn_payload_validate_request_authorization` definition is present in committed source.
The previous local-only reservation dependency caveat is resolved for that published file.
This does not audit all 640 lines of its custody transactions or their native primitive dependencies.

## Source drift and hashes

At the first read, HEAD was 5793.
During the audit it advanced to `0dc5df3f11da5639e79752591cf78781b7da4d43` while the peer reconciled unrelated civil-war split accounting.
The working missile file differs from the 5793 blob outside the chemical helper, and its chemical helper AST is exactly identical to the committed 5793 helper.
The other inspected shared files differ only by newline normalization from their 5793 committed contents.
No ownership finding is based on the unrelated civil-war edits.
The JSON companion records initial working and committed hashes and final drift checks.

| File under `common/scripted_effects/` | Working SHA-256 at audit snapshot |
| --- | --- |
| `032_missiles_operations_effects.txt` | `3ae3a6ec33c61c7bb7846c47628d9a2b978bc886b4841be09004d4722358f23f` |
| `cbrn_exposure_effects.txt` | `bb23620b4f16f62b4f808b3524b6a59e6bcf57a12f62802c816b1ceb824aae72` |
| `cbrn_protection_effects.txt` | `278bbd01add94610a81b453ce3e2fbcd12003e737ed4a06eeb6af4184377d8f4` |
| `cbrn_payload_reservation_effects.txt` | `fd8535a93429919eff2a0b22e0d9b5906872ee78c34d6fa96f4dbd9fe07c02f2` |
| `cbrn_consequence_effects.txt` | `e1c08016ed44c2e1cd226cdc7aeb3ff105648cf585055cb62c2d0f842f815c72` |
| `cbrn_diplomacy_effects.txt` | `60b8c4c70a018328e64f19c8e2c5caf7cbbbfcbb99928f5c0b538b1d53278042` |

Camp remains parent-owned and is outside this follow-up.
No MCP graph, engine, game, log, staging, or commit action was performed.
The existing events/native-raids/subagents lifetime and ownership guidance was used, with no skill changes.
No gameplay fallback or simplification was introduced.
The parent receives one concrete remaining storage fix, evidence of the otherwise justified partial ownership, and confirmation that the shared dependency allocations are committed.
