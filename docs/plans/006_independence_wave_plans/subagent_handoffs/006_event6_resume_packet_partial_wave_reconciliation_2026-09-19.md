# Event 006 resume-packet partial-wave reconciliation — 2026-09-19

Disposition: documentation-only current-authority correction. Event 006 remains **HOLD / PARTIAL** at 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows. No gameplay, localisation, asset, spreadsheet, source-spec design, or probability weight was changed, and no commit was created.

## Authority and exact change

The parent-accepted 2026-09-12 [root-to-release transaction audit](006_event6_root_release_transaction_audit_2026-09-12.md) documents removal of the exhausted-pool selected-count rewrite from `independence_wave_allocate_automatic_packages`. Current source at `common/scripted_effects/006_independence_wave_effects.txt:3621-3672` keeps the frozen target and shared expected count, sets `independence_wave_plan_exact_count_failed`, records `liberation_plan_reject_reason.insufficient_pool`, and does not publish contribution readiness when an automatic pool is short. The exact automatic ladder remains `3/4/5/7/10`, including World Collapse at `10`. The parent acceptance basis is stated in the 2026-09-12 audit; the 2026-08-20 joint expected-count, 2026-08-22 exact-ladder, and 2026-08-24 manual standalone partial-wave handoffs remain dated implementation receipts rather than present behavior authority.

Only `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` was edited:

| Resume paragraph | Before | After |
| --- | --- | --- |
| Former line 452, joint expected-count receipt | The 2026-08-20 repair could read as a current partial-wave selected-count rule. | Labels it dated joint repair evidence and states the current frozen nominal count and `insufficient_pool` failure, with the 2026-09-12 audit as current authority. |
| Former line 454, standalone exception | It already called the 2026-08-24 exception superseded but named the 2026-08-22 handoff as the current authority. | Names the parent-accepted 2026-09-12 allocator repair as current and keeps both 2026-08 handoffs as historical evidence. |
| Former line 484, resume authority pointer | Routed to a 2026-09-05 override. | Routes to the existing 2026-09-19 current-authority override at the top of the packet. |
| Former line 490, exact-count summary | Named the 2026-08-22 handoff as current. | Names current `independence_wave_allocate_automatic_packages` source and the 2026-09-12 repair, explicitly preserving the older handoffs as support/history. |

No historical handoff was rewritten or deleted. The 2026-08-24 manual partial-wave exception is superseded for current automatic allocation, not silently presented as an accepted fallback. No unconditional country admission, replacement pool, lower target, pre-event surface, or balance conclusion was introduced. The adjacent 2026-08-24 probability-auditor prose and older immediate-continuation list remain dated or separately owned and were not broadly reconciled in this bounded patch.

## Focused validation and limits

`python -B .tools/audit_event6_allocator.py --strict` passed on the current source and reported the exact `3/4/5/7/10` automatic counts, World Collapse `10`, 32 attestations, 29 compatible groups, 40 adapters, and no pre-event crisis surface. A targeted source read of the allocator found no short-pool assignment of either target or expected count to selected count and confirmed its `insufficient_pool` failure branch. A focused search of the edited resume packet found no remaining assertion that a non-empty undersized standalone automatic selection is a current success path; surviving partial-wave references explicitly identify dated history or the fail-closed rule.

Read-only `hoi4.event_inspect` lint on `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c720b042e81eb386b32de671286f1d3ec5deaf2d2f213896a474200665902e6/92eb2df6e83efa69cd91bc1236cc6816d1a5c31da9bb51cc888224480176e4bd/event-lint-95a1779f47fa.json`. This is structural evidence only; helper/lifecycle projection, execution, release, terminal receipt, and live-game outcome remain unproven. The [2026-09-19 probability audit](006_event6_probability_audit_2026-09-19.md) remains the independent scenario-specific weighted-logic authority; its exact declared outer fixtures do not establish nested package odds or campaign balance. No probability source changed, so no before/after `probability_compare` was warranted for this documentation patch.

The changed prose keeps each sentence on one physical line and preserves paragraph boundaries. Parent review should confirm the four narrow resume-paragraph changes and retain the historical handoffs for transaction provenance.
