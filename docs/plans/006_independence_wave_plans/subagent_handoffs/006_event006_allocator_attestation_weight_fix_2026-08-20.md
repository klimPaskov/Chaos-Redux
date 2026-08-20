# Event 006 allocator attestation-weight fix

Date: 2026-08-20

## Disposition

Implemented a narrow source fix for the standalone Event 006 entry path. Unimplemented package rows now remain at zero allocation weight instead of receiving the allocator minimum, so they cannot be selected repeatedly ahead of an admitted package.

## Root cause

`independence_wave_calculate_candidate_allocation_weight` initialized every candidate at zero, correctly raised the weight only inside the content-attestation branch, and then applied the positive minimum clamp outside that branch. Rows without content attestation therefore became selectable even though `independence_wave_begin_package_reservation` rejected them before incrementing the attempt counter. The allocator could spend the whole transaction selecting rejected, unimplemented rows and never reach a releasable country.

## Source change

Changed `common/scripted_effects/006_independence_wave_package_planner_effects.txt` so the minimum-weight clamp also requires `has_independence_wave_runtime_package_content_attestation_for_execution_id = yes`. The patch does not widen the attestation list, adapter list, preflight, Join order, or package content contract.

## Capital-scope audit

The current repository versions of `common/scripted_triggers/006_independence_wave_epirus_package_triggers.txt`, `common/scripted_triggers/006_independence_wave_thrace_package_triggers.txt`, and `common/scripted_triggers/006_independence_wave_banat_package_triggers.txt` contain fixed numeric anchor-state scopes (`185`, `184`, and `82`) and no `capital_scope` call. Their dormant carrier histories intentionally have no capital before release. The pasted line-17 errors therefore do not match the current source snapshot.

## Evidence and limits

The static allocator audit still reports 149 publishers, 40 adapters, 32 content attestations, and 29 compatible reservation groups, with the pre-event crisis surface retired. The mandatory probability inspection of the planner source returned `PROBABILITY_SOURCE_DISCOVERED` with no exposed weighted surface because the weighting is assembled through scripted/meta effects. The current Event 006 inspect remains `EVENT_INSPECTED_PARTIAL` with zero selected blockers because the large-workspace helper and lifecycle projection is deferred. No live-game launch was performed.

The probability artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30259cfaa9ba5a1dce398ee2588728c9462910d7bff872d84efebce9c6b30c24/ba4c52c7ee95d0228fdcc8424b77946805d8e05e502b010ed55efb51b8d51f1f/probability-inspect-116469afe2f3.json`. A fresh `hoi4.event_inspect` lint of `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d43ba69c4d0fc1ae60a12140441afb9eda815014074ea93f9a864390d6cd96b/c1093035ac42d54e1fc954802b90f59c502c23ea34c4090f01236af1316efcc2/event-lint-98ac244e0b19.json`. Both MCP routes defer large-workspace helper and lifecycle projection.

## Remaining user-side check

Trigger `chaosx.nr6.1` after loading this source and confirm that the committed report appears only after at least one admitted package is released. No pre-event decision, pressure category, crisis indication, or other player-facing entry surface was added.
