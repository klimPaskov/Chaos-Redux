# Camp chemical caller-storage audit and patch hold

Disposition: parent gate released, exactly 66 caller-storage declarations implemented and frozen for independent tests, MCP comparison and integration.
The scope is only the existing `camp_rework_apply_chemical_escalation_in_action_state` caller in `common/scripted_effects/camp_repression_rework_effects.txt`.
The audit phase was read-only, and the later source edit contains only the parent-approved declaration block.
No test, index, stage, commit, game, log, or MCP graph action was taken by this agent.
The live missile owner retains all missile and receipt integrations.

## Source freeze

Baseline HEAD: `6e4e23a26fc6f81dd77e615108ff1cddf2734aeb`.
At capture, the camp file had clean Git status.
Its captured working SHA-256 is `7c68d93e8097fc6a33af11ff7cd3bae3216dc9335f36b65ac0cdcf94aff5644c`.
The captured HEAD/index and checkout bytes differed only by line endings and matched after CRLF-to-LF normalization.
The fresh pre-write guard matched those exact captured working bytes, and the frozen after identity is recorded below.

Evidence is under `docs/testing/2026-10-07_camp_chemical_lifetime/`.
`source_manifest.json` records raw working, HEAD and index identities, clean status, newline counts, cited dependency hashes, and authoritative reference revisions.
`before/common/scripted_effects/camp_repression_rework_effects.txt` is the exact raw working baseline.
The local `.gitattributes` sets `before/** -text` and `after/** -text`.
`after/common/scripted_effects/camp_repression_rework_effects.txt` contains the exact frozen patched bytes.
`proposed_insertion.json` records the accepted and applied field/default contract, containing owner, branch placement, byte offset and original line.
`insertion_manifest.json` records the exact inserted bytes, before/after spans, defaults, hashes, fresh write guard, index identities, and parent baseline evidence.

## Input and output contract

The caller executes the existing country-scoped method-tier resolver before its eligibility guard.
The guard requires a stored exact state, the existing country chemical-method permission/capacity path, no expansion-freeze flag, a positive method tier, and the exact state's existing eligibility predicate.
The actor remains the existing country ROOT and `camp_rework_action_state_id` remains the supplied state pointer.
No replacement actor, state, target, method tier, site, policy, or permission is proposed.

Inside that existing eligible branch, the first producing call is `camp_rework_prepare_chemical_method_outcome`.
None of the original map's 60 shared action fields or five method outputs has caller-owned storage before that call.
Later direct assignments of weapon class, route, severity and payload amount do not preserve the other returned/default fields.
The method-death-factor zero assignment after the entire eligible block is cleanup and cannot own the earlier returned method output.

The proposed insertion sits immediately before the method-outcome helper, preserving the original method helper, reset, target binding, classification, payload requirement, debit, protection, release, prepare, dispatch and post-dispatch sequence.
The original 60-field action contract is the committed map's 38 reset inputs, 20 reset outputs and two mask-only casualty baselines.
Its original defaults are preserved rather than supplying neutral condition or release receipts.
The five camp method outputs are:

| Field | Existing default | Actual downstream consumer |
| --- | --- | --- |
| `camp_rework_method_death_factor` | One | The existing restricted-site release-efficiency multiplier |
| `camp_method_evidence_gain` | Zero | Country and exact-state evidence updates after successful dispatch |
| `camp_method_accident_pressure` | Zero | Country resistance pressure and exact-state resistance accumulation |
| `camp_method_stockpile_cost` | Zero | The existing payload amount supplied before the exact debit helper |
| `cbrn_camp_action_duration_days` | `constant:camp_rework_chemical_contamination.chlorine_days` | The existing action duration override and resulting active-site timers |

The tier-specific helper overwrites those defaults using its existing researched method and mastery logic.
Storage initialization does not select another tier, alter any cylinder quantity or price, or change duration tuning.

## One additional output missing from the old map

The current caller invokes `cbrn_camp_record_shared_action_deaths` in the exact state after the shared dispatcher returns.
`cbrn_camp_effects.txt:77-79` reads `cbrn_action_civilian_deaths` and supplies that receipt to the existing camp death-record helper.
That scalar is not in the 60-field packet, which contains a civilian death fraction rather than the realized death count.
The dispatcher owns its private civilian-death output, but newly created dispatcher storage can disappear when returning to the camp caller.
The camp caller therefore also needs `cbrn_action_civilian_deaths = constant:cbrn_math.zero` before dispatch.

The complete proposed narrow insertion contains 66 scalar declarations, comprising the original 60, five method outputs, and this observed returned death-count consumer.
The sidecar names the additional output and its source basis explicitly.
The parent explicitly accepted this additional output and the complete 66-field contract before releasing the patch gate.
No new death calculation or duplicate death payment/record is proposed.
The existing camp bridge continues to consume the dispatcher's same exact receipt.

## Boundaries preserved on release

`cbrn_try_debit_action_payload` retains its existing metadata, unlocked-agent, profile, stock and exact-model checks and remains the sole existing camp action debit path.
No native raid outcome payment path is added to this restricted-site mechanic.
The caller still requires consumed-payload proof and positive quantity before protection, release and record preparation.
It still requires accepted preparation before dispatch and supplied dispatch proof before country/site consequences and the camp receipt bridge.
`cbrn_action_dispatch_proof` may be initialized only in this fresh action-owner packet and must not be reset in the shared dispatcher.

Restricted-site release still derives efficiency from current readiness and method factor and duration from the existing tier.
The adapter supplies no new weather, terrain, density, forecast, command, or friendly-risk receipt.
The successful-dispatch site flags, responsibility pointer, evidence/resistance updates, active-site registration, country recalculation, and final method-factor cleanup remain in their original order.

## References, ownership, and remaining work

The event skill's caller-owned output rule and repository ownership requirements were read for this audit.
The authoritative lifetime sections remain offline `Data structures:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, and installed `effects_documentation.md:7820-7827`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The committed `2026-10-07_chemical_action_lifetime_insertion_map.json` provides the exact public packet and method defaults.
The snapshot manifest cites current camp adapters, shared exposure/protection/consequence/payload source, camp and shared triggers, and tuning identities.
Dependency hashes are evidence identities rather than a lock on the live missile owner's files.
No dependency source was edited.

This audit identifies output ownership and source integrity, not native execution of a camp transaction.
No transaction tests or MCP graphs were run by this agent.
The parent obtained the requested supported baseline and explicitly released the patch gate.
The bounded source audit and declaration patch are complete within this assigned scope.

## Released patch and source-integrity review

The parent's initial full-refresh graph scan returned `INTERNAL_ERROR`.
The supported bounded `event_inspect(mode=scan)` for `camp_administration_country.1`, with node/edge/depth limits of one, no helper expansion and no refresh, subsequently returned `EVENT_INSPECTED_PARTIAL`.
Its graph revision is `db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5`, and the graph URI remains parent-side.
It has zero expanded helpers and deferred lifecycle projections, so this gate release is not native transaction or helper-lifetime proof.

The fresh exact-byte guard confirmed the captured `7c68d93e...` working source immediately before the write.
Release-time HEAD was `0dc5df3f11da5639e79752591cf78781b7da4d43`.
Exactly 66 literal `set_temp_variable` declarations and one explanatory comment were inserted at the captured original line 5024, immediately before `camp_rework_prepare_chemical_method_outcome` inside the unchanged eligibility branch.
The atomic replacement was preceded by another exact-byte race check, and no source conflict occurred.
The original physical line ending and indentation at that anchor were retained.

Frozen after SHA-256: `cf83c6498e7cd94ebd8125f26e572113d0a83cb121829c87636cf86487a20ada`.
Removing the recorded inserted byte span exactly reproduces every original working byte.
The parsed original statements and order match the captured baseline after that removal, and the inserted fields/defaults match the accepted 66-entry contract in the same containing sequence.
The Git index entry remained unchanged.
No cost, debit, refund, helper call, eligibility/policy gate, severity, target, timer, Condemnation value, site update, death bridge, cleanup or callback was modified.
No new proof or default acceptance was supplied.

The patch is frozen with exact before/after archives and an insertion manifest for isolated review.
The parent retains independent transaction tests, MCP comparison, shared-owner integration and commit ownership.
No gameplay completion, fallback or native-execution result is claimed by this source-integrity review.
