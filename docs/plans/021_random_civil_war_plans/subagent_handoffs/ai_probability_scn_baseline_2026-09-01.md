# Event 021 SCN-01 and SCN-03 Baseline Probability Audit

## Immediate MCP blocker record

The mandatory first probability inspection was attempted with adapter `custom_weighted_pool` against `common/scripted_effects/021_random_civil_war_parent_effects.txt`, selector `random_civil_war_trigger_manual_scenario`, and `refresh = true`.

Exact MCP response: `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: Unrecognized keys: "relativePath", "selector" at source`.

This error was recorded immediately. The audit remains unresolved until the required probability route accepts a valid source or declared custom-pool input.

A narrow schema correction was then attempted with `adapter = custom_weighted_pool` and `refresh = true` without a source.

Exact MCP response: `MCP error -32602: Input validation error: An adapter requires a source; provide a source alone to discover compatible adapters`.

A source-only retry using the Windows-relative source path string `common/scripted_effects/021_random_civil_war_parent_effects.txt` returned:

Exact MCP response: `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: Invalid input: expected object, received string at source`.
