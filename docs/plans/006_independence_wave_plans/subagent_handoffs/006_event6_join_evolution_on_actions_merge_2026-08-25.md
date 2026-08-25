# Event 006 Join/Evolution on-action registry merge

Date: 2026-08-25

## Scope

This source-layout tranche folds the two small Event 006 callback files into the existing on-action registry:

- `common/on_actions/006_independence_wave_join_on_actions.txt`
- `common/on_actions/006_independence_wave_evolution_on_actions.txt`

Their blocks now live in `common/on_actions/006_independence_wave_on_actions_registry.txt` under explicit `SOURCE` markers. The two standalone files are removed.

## Preservation

- All six Join callback keys and their effects are preserved byte-for-byte in executable content.
- All three evolution callback keys and their effects are preserved byte-for-byte in executable content.
- The registry remains a single `on_actions = { ... }` namespace.
- The achievement on-action file remains separate because it defines overlapping engine callback keys and therefore retains its existing composition boundary.
- No scripted effect, trigger, event, decision, cost, admission, AI, localisation, or asset identifier changed.

## Validation

The source diff was reviewed for balanced nesting and exact callback/effect preservation. Existing Event 006 static validators are the required follow-up. No live HOI4 parser or MCP callback claim is made.
