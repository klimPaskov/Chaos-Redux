# Event 012 Gods of Africa response-context trigger handoff

Date: 2026-10-07.
Disposition: implemented within the authorized helper-file scope and awaiting parent integration review.

## Scope and authority

This patch adds seven pure scripted triggers for the parent-owned host response views.
The bounded source of decision behavior is the immutable snapshot at `docs/plans/012_africa_plans/subagent_handoffs/012_gods_decision_phases_2026-10-07_evidence/before/common__decisions__012_africa_gods_decisions.txt`.
The snapshot SHA-256 is `B39073B4370A8F7508DDC7902A6D9F4E5907942375313257FD063268A60FC6E8`.
The user authorized full Gods implementation without simplification and assigned the parent ownership of view selectors, decision rows, costs, effects, AI, cleanup and localisation.
This handoff records implementation evidence for the helpers and does not claim that the phase plan or whole feature is complete.

## Changed files and identifiers

- `common/scripted_triggers/012_africa_gods_response_context_triggers.txt` adds the seven triggers listed below.
- `docs/plans/012_africa_plans/subagent_handoffs/012_gods_response_context_handoff_2026-10-07.md` records source coverage, behavior and validation limits.
- `gods_of_africa_substitute_answer_is_current` mirrors the participant answer target: existing country, participant flag and current pending substitute offer.
- `gods_of_africa_reject_answer_is_current` mirrors the candidate answer target: existing country and either a current victor renewal or a participant with a current pending substitute offer.
- `gods_of_africa_reconciliation_answer_is_current` mirrors the candidate answer target: existing country and either a current victor renewal or a participant with reparations paid, an offer pending and current reconciliation eligibility.
- `gods_of_africa_host_has_pending_answers` searches the existing participant and candidate arrays through those exact answer predicates.
- `gods_of_africa_host_has_priority_context` covers the five independent shortages and the mutually exclusive emergency, arsenal-support and logistics-aircraft priority lane.
- `gods_of_africa_host_has_partner_context` covers leniency, public pardon, protection and expedition target context.
- `gods_of_africa_host_has_judgment_context` covers offender marking, offense escalation, coalition arming and occupier coercion target context.

## Source coverage

The target IDs and eligibility were read from the immutable decision snapshot, not from the parent's concurrently edited phase source.
The five independent priority rows are `gods_of_africa_prioritize_land`, `gods_of_africa_prioritize_fuel`, `gods_of_africa_prioritize_manpower`, `gods_of_africa_prioritize_industry` and `gods_of_africa_prioritize_transport` at snapshot lines 1162–1288.
The advanced row is `gods_of_africa_prioritize_emergency` before arsenal and logistics support, `gods_of_africa_prioritize_support` after arsenal support and before logistics support, or `gods_of_africa_prioritize_air_defense` after logistics support at snapshot lines 1290–1333.
Each priority branch retains its source shortage threshold and focus flags.
No priority-affordability or cooldown check was added because those checks belong to availability rather than visible context.

The partner rows are `gods_of_africa_grant_leniency` and `gods_of_africa_public_pardon` at snapshot lines 1335–1471, `gods_of_africa_protect_partner` at lines 1472–1541, and `gods_of_africa_send_expedition` at lines 2000–2057.
Their original host focus gates and target checks are preserved.
Protection context uses `gods_of_africa_participant_can_receive_protection`, which excludes host stock and political-power affordability.
The separate protection affordability checks remain in the original availability and custom-cost path.

The judgment rows are `gods_of_africa_mark_offender` at snapshot lines 1782–1867, `gods_of_africa_escalate_offense` at lines 1868–1940, `gods_of_africa_arm_offender_enemies` at lines 1941–1999, and `gods_of_africa_coerce_occupier` at lines 2058–2113.
Their focus gates, participant and generation checks, proven-offense checks, target validity helpers and offender-capacity check are retained.
The offender-capacity check is evaluated explicitly through `ROOT` so it remains on the host while `THIS` is the array member.

Pending-answer coverage uses `gods_of_africa_accept_substitute` at snapshot lines 1542–1604, `gods_of_africa_reject_substitute` at lines 1605–1663 and `gods_of_africa_accept_reconciliation` at lines 1728–1781.
Substitute answer visibility does not require affordability, transfer clearance or an open payment retry.
The candidate-array scan retains the non-member victor-renewal exception in both candidate predicates.
Paid reconciliation still requires its original paid flag, pending-offer flag and `gods_of_africa_participant_can_reconcile` guard.

## Private helper API and scope

All seven helpers take no parameters, return a boolean trigger result and have no side effects.
The three `*_answer_is_current` predicates are COUNTRY scoped on an array candidate.
The four `gods_of_africa_host_has_*_context` predicates are COUNTRY scoped on the current Gods host.
Host helpers require `gods_of_africa_active_host_is_valid` before reporting a context.
Inside `any_of_scopes`, `THIS` is the participant or candidate and `ROOT` remains the host.
No helper uses `FROM` or `PREV`.
Only the offender-capacity test explicitly scopes back to `ROOT` because the original target trigger evaluated that check on the host.
The arrays are the host-owned `gods_of_africa_participants` and `gods_of_africa_candidate_registry` arrays, with no world scan, first-target cap or cache flag.

The target helpers check the cheap participant, offer, paid and renewal flags before the existing current-generation, current-contract, deadline or victor guard where those flags are logical prerequisites.
The current helper bodies remain authoritative for epoch, generation, deadline, route and target validity.
The historical comment above `gods_of_africa_proven_offender` describes host scope, while the frozen decision target invokes it under `FROM` and its body reads target-local flags and counters.
This patch follows the actual frozen call-site scope and leaves the unrelated source comment for parent review.

## Behavior before and after

Before this patch, the parent had no bounded host predicates to select a response family from live campaign context.
The source decision `target_trigger` checks were daily, while targeted `visible` checks run each frame.
The parent can prewarm the three answer rows with only `FROM exists = yes` inside their existing target arrays, then use the three `*_answer_is_current` helpers in the live `visible` path while retaining the old `available` logic.
The host pending-answer selector can use `gods_of_africa_host_has_pending_answers` to detect current replies directly from the same arrays.
Priority, partner and judgment navigation can use their corresponding host predicates to avoid empty families while retaining otherwise-valid unaffordable children.
Decision rewrites, prewarming and view gating remain parent-owned and were not changed here.

## References and evidence

The installed trigger documentation section `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:1531-1545`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, defines `any_of_scopes` as iterating an array and evaluating its trigger block for each scope.
The offline wiki section `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:1149`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, confirms that the check scopes into each array element and documents `PREV` as the parent scope after that change.
The offline decision section `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:531-537`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, says `target_trigger` evaluates `FROM` as target and `ROOT` as the acting country daily, while `visible` checks both every tick.
The installed decision documentation `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, independently confirms daily `target_trigger` and per-frame `visible` checks.
The vanilla `invite_to_org` decision in `game:common/decisions/African_Union_decisions.txt:3-56` was located and read with `hoi4.source_lookup`, workspace-index revision `8ae6541434c0a2a85e07c56e4e42dc12f312745c69364d26e582ba8a3d11fa77`.
That targeted decision shows the installed ROOT and FROM distinction in an Africa-focused decision and uses PREV only for its nested owner/core scope.

## Validation and limits

The file-mode `hoi4.script_validate` check returned `SCRIPT_CHECK_PARTIAL` with `valid = null`, zero diagnostics and zero unresolved commands across 90 checked commands.
It performed syntax, command-kind, declared-scope and event-popup checks, but left 18 argument blocks unchecked and could not infer the scope of the seven scripted-trigger roots.
The result is useful syntax evidence and does not establish complete command-argument or engine-runtime validity.
No AI weight, score or probability source was changed, so probability inspection and comparison are not applicable to this helper-only patch.
No GUI layout or decision-row file was changed, so GUI inspect, render and comparison evidence remain with the parent integration.
No live game was launched.

The parent still owns the new view enum, navigation decisions, human-only selector, visible-row prewarming and gating, effects, cleanup, localisation, balance integration and final cross-surface review.
The parent should confirm the answer rows appear immediately after the existing target cache is prewarmed and that the `available` conditions remain unchanged.
This patch does not establish native row geometry, live-game behavior, whole-feature completion or acceptance of unresolved plan proposals.

Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events` and `chaos-redux-subagents`.
