# Event 021 scenario target-ticket probability audit

Audit date: 2026-09-19.

## Scope

The requested independent `chaosx_ai_probability_auditor` pass covered the Event 021 manual scenario target-ticket repair in `event021_parent_add_scenario_target_to_weighted_pool` and the centralized `random_civil_war_scenario_target_weight` constants.

The intended named fixtures were `SCN-01-LOW-MINOR-PREFERENCE`, `SCN-02-MEDIUM-NEUTRAL`, and `SCN-03-HIGH-MAJOR-PREFERENCE`, using identical two-candidate minor/major pools before and after the patch.

## Result

The auditor was spawned with `fork_context=false` and the required self-contained read-only prompt. It remained non-terminal through bounded waits and was interrupted before its first MCP probability call. It returned that no durable handoff was written, no MCP probability failure or timeout was observed in that pass, and no gameplay files were edited.

There is therefore no independent inspect, evaluate, or compare artifact for this repair.

## Parent-owned source evidence

The owner patch is committed in `6a4e3cfb8`.

Low uses minor `4` and major `1`, Medium uses minor `2` and major `2`, and High uses minor `1` and major `3` before the shared individual-crisis load adjustment. Maximum bypasses this helper and copies the confirmation-time eligible set.

The current source hashes and focused Event MCP lint receipt are recorded in `probability_parent_current_matrix_refresh_2026-09-19.md` and `docs/events/021_random_civil_war/acceptance_evidence.md`.

## Disposition

`accepted and queued` for independent probability certification and live scenario testing.

This handoff does not establish exact Low/Medium/High selection distributions, whole-world target probabilities, a same-scenario before/after comparison, or Maximum successful-commit coverage. The Event 021 package remains in the `Needs Testing` phase and is not finally accepted.
