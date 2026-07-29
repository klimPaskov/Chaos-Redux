# Event 012 W1 Constituent Agency and Package Ratification Protocol

## Scope and implementation status

This handoff covers the W1 constituent protocol tranche. It changes only the shared Event 012 package constants, package effects/triggers, polity decisions, the new constituent event surface, localisation, and this handoff. It does not create tags, subjects, territory transfers, models, recurring world scans, or terminal package readiness.

## Files changed

- `common/script_constants/012_africa_world_order_constants.txt`
- `common/scripted_effects/012_africa_world_order_effects.txt`
- `common/scripted_triggers/012_africa_world_order_triggers.txt`
- `common/decisions/012_africa_decisions.txt`
- `events/012_africa_world_package.txt`
- `localisation/english/012_africa_world_order_l_english.yml`

## Shared helper map

| Helper | Scope | Inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- | --- |
| `africa_world_open_constituent_invitation` | Constituent | Frozen package roster target and protocol event target | Sets `africa_world_constituent_invitation_pending`, opens the response timeout, and moves the package phase to `constituent_bargaining` | `africa_world_invite_constituent_to_compact` |
| `africa_world_open_constituent_counterterms` | Constituent | Open invitation | Sets `africa_world_constituent_counterterms_pending`; pending accounting remains open | Event `.1` negotiate option |
| `africa_world_record_constituent_consent` | Constituent | Invitation or counterterm response | Clears invitation/pending state, records voluntary membership, increments voluntary external count and authority, and removes stale refusal/withdrawal ledger entries | Package event `.2`, counterterm accept |
| `africa_world_record_constituent_refusal` | Constituent | Invitation/counterterm refusal | Clears response state, records public refusal and grievance, increments refusal ledger, and applies central authority/legitimacy losses | Package event `.4`, invitation timeout |
| `africa_world_record_constituent_coercion` | Constituent | Real refusal, rejected counterterms, or contested withdrawal; no package war | Records public coerced membership, increments coerced external count, preserves grievance, and applies central authority/legitimacy losses | Existing `africa_world_coerce_constituent_compact` decision |
| `africa_world_open_constituent_withdrawal_notice` | Constituent | Voluntary/coerced member and reverse package-actor array | Sets a 60-day notice, increments package pending responses, and schedules timeout `.12` | `africa_world_submit_constituent_withdrawal_notice` |
| `africa_world_accept_withdrawal_safeguards` | Constituent | Open notice | Clears notice/contest state, records local-command safeguard, retains membership, and restores a small authority amount | Events `.8`/`.9` -> `.10` |
| `africa_world_reject_withdrawal_safeguards` | Constituent | Open notice | Clears notice, records contested/rejected grievance, and makes coercion separately visible | Events `.8`/`.9` -> `.11` |
| `africa_world_record_constituent_withdrawal` | Constituent | Orderly notice accepted or peaceful timeout | Clears membership, decrements voluntary/coerced counts, records withdrawal, and applies central authority/legitimacy losses | Package finalizer `.13`, timeout `.12` |
| `africa_world_package_ratification_is_proven` | Package actor trigger | Heartland, route, crisis, lanes, withdrawal law, ledger, quorum, capacity, authority, legitimacy | Returns true only for a complete voluntary/explicitly resolved package protocol; `africa_world_complete_sovereign_package` now requires it | Package capstone and terminal settlement trigger |
| `africa_world_cleanup_package_constituent_protocol` | Package actor | Existing frozen constituent array | Clears invitation/counterterm/withdrawal flags on all recorded constituents, removes reverse package links, clears ledger arrays and pending count | Package actor loss/successor review |

All event-targeted record helpers select `africa_world_protocol_package` and `africa_world_protocol_constituent` explicitly. Decision-targeted calls retain the existing ROOT/PREV path, so package authors cannot author a constituent answer.

## Constants and tuning table

- `africa_world_package_protocol`: invitation/counterterm/withdrawal Political Power costs, 45-day invitation responses, 60-day withdrawal notices, quorum cutoff/minimum, authority/legitimacy/capacity thresholds, public loss values, and AI weights.
- `africa_world_package_phase`: `opening_congress`, `constituent_bargaining`, `route_committed`, `shared_lanes`, `ratification`, `sovereign`, `union_convention`, `union_active`, `war_active`, `successor_review`, `breakup_review`, and `terminally_resolved`.
- `africa_world_package_crisis_result`: `none`, `success`, `compromise`, and `failure`; W2 route loops write the result and the shared proof accepts only success/compromise.
- `africa_world_constituent_safeguard`: `none`, `local_command`, `resource_veto`, `language_guarantee`, and `basing_restriction`; W1 records the local-command variant while leaving the enum open for route-specific counterterms.

## Event target and cleanup plan

The package actor saves `africa_world_protocol_package` before a targeted invitation or withdrawal decision saves `africa_world_protocol_constituent`. Regular event targets are sufficient for this short chain and are carried into events fired from the effect chain. Invitation timeout `.16` and withdrawal timeout `.12` are guarded by the corresponding pending flags, so resolved chains become no-ops. Package actor loss calls `africa_world_cleanup_package_constituent_protocol` before successor/exile/breakup review and clears reverse links without a world iteration.

## Migration from duplicated logic

The old package-owned consent, refusal, and withdrawal decisions were removed from `africa_world_polity_actions_category`. The package actor now has only the invitation decision and the existing coercion decision. Constituent governments use the reverse package-actor array for `africa_world_submit_constituent_withdrawal_notice`. Existing W0 constituent arrays and status flags remain the ledger source; new protocol flags are additive and are cleared by record/cleanup helpers.

## Risks and unsupported analysis

- Route-specific W2 loops must write the exact shared-lane proof flags listed in the W1 addendum (`africa_crossroads_*_ratified`, `africa_europe_*_ratified`, `africa_asia_*_ratified`, `africa_north_america_*_ratified`, `africa_south_america_*_ratified`, and `africa_oceania_*_ratified`). The shared proof intentionally does not grant readiness from the six deferred high-chaos route flags.
- `script_constants` are global, but unsupported engine fields can still reject dynamic constants. Decision costs use the documented `cost = constant:` form; event Political Power spends derive a temporary negative value through `africa_world_spend_protocol_political_power`.
- Event-target retention, AI option selection, timed-event persistence, and in-game decision visibility require the parent-owned runtime pass. Hearts of Iron IV was not launched by this subagent.

## Validation performed

- Read the required offline wiki pages and vanilla scripting documentation before editing.
- Audited the new event namespace for duplicate `africa_world_package.*` IDs across all Event 012 files; no duplicates were found.
- Audited every new event/decision localisation reference against `012_africa_world_order_l_english.yml`; no missing keys were found.
- Ran a brace/quote parser over all five touched script surfaces after the final patch; all returned balanced braces and closed quotes.
- Confirmed the localisation file retains a UTF-8 BOM and the new scripts contain no unsupported `<=` or `>=` operators.
- Ran read-only `hoi4.event_inspect` lint for `africa_world_package.1`; the MCP returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics, while deferring workspace-wide helper/lifecycle projections because the workspace graph is large.

## Follow-up for parent/W2

W2 route loops should set `africa_world_package_crisis_result` to `success` or `compromise`, advance `africa_world_package_phase` through route/shared-lane/ratification states, and publish the exact route proof flags before invoking the shared package capstone. No W1 helper sets the crisis result or terminal readiness.
