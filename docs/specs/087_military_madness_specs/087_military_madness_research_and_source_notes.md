# Military Madness: Research and Source Notes

## Source hierarchy

The user's Military Madness brief is authoritative for the event identity, repeatability, country coverage, duration, roll counts, broad-pool guarantees, thresholds, duplicate behavior, pool breadth and cluster assignment.
Project rules and skills govern planning quality, ownership and validation.
Existing source shows what must be replaced or preserved and does not override the brief.

The magnitude bands, equal-entry sampling, pre-fire stage selection, technical saturation, presentation, Chaos impulse, AI use of results and achievement objectives are design elaborations under the user's request to expand the specification, not additional user instructions.
The README records which of them were accepted in later passes.

## Legacy event

The legacy event (`events/087_ww1.txt`, `common/ideas/087_ww1_ideas.txt`) fires `chaosx.nr87.1`, sends the recipient report `chaosx.nr87.2`, and grants a fixed `entrenchment_bonus` idea from its option for nine months.
That idea combines entrenchment and reconnaissance bonuses with an attrition increase and allows civil-war copying.
None of this matches the requested random one-year system, so the rework replaces the reward path and keeps the `chaosx.nr87.1` entry.

The catalog still names Event 087 "It’s WW1", Minor Repeatable at Chaos level 1.
Military Preparation is cluster 18, and its member list does not yet contain Event 087; the workbook update happens through the spreadsheet worker and exporter during implementation.

## Technical findings

- Dynamic modifiers accept variable-backed values, but the game cannot enumerate modifier keys at runtime, so the design uses an audited registry built once from the documentation and sampled at runtime (Part 2).
- `equipment_bonus` and `research_bonus` are idea attributes, not ordinary modifiers, and cannot go into a dynamic-modifier block; soft attack, armor, unit-specific and terrain rows need a real country-scoped binding or a reversible national adapter.
- Dynamic modifiers are re-evaluated on the game's update cycle, so a total-minus-own-contribution safety calculation can drift; the saturation rule in Parts 3 and 4 must be proved against the actual update order.
- No modifier token or numeric safety bound in this package is certified; the magnitude table is a design target.

## Sources still to read during implementation

| Source | Why |
|---|---|
| Offline wiki core set (Data structures, Triggers, Effects, Modifiers, Scopes, On actions, Event, Decision, Idea and AI modding) | Bindings, scopes, dynamic modifiers, timed decisions and AI strategies |
| Installed `documentation/` modifier, effect and trigger references | Exact tokens, value types and scopes for the registry |
| Enabled DLC content and Chaos Redux military systems | Breadth of the registry |
| Current event selection, cluster, Chaos and achievement implementation | Integration |
| Event-assets reference library and achievement templates | Asset production |

## Scope decisions

The design expands the lottery, timed overlap, readable results, provider coverage, AI use of results and achievement opportunities.
It adds no selectable archetypes, paid rerolls, invented forces, focus tree, country, super-event, world-end or scripted GUI; those omissions preserve the requested passive random event.
