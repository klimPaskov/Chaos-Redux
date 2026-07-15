# Event 014 Removed-Origin Cleanup

Date: 2026-07-15

Status: implemented and closed by the 2026-07-15 cross-surface re-audits.

## Current authority

Event 014 has three warlord origins: Island Host, Siege Commune, and March Host. `CBA` through `CBH` are eight origin-agnostic reusable slots. No current gameplay, localisation, interface, portrait, flag, scenario, country package, focus, decision, idea, trait, AI profile, recruitment template, or Wendigo inheritance stage reserves a slot for any other origin.

Older dated audit and handoff files under `docs/plans/014_cannibalism_plans/subagent_handoffs/` are historical evidence of the superseded implementation and are not design authority. Current authority is the specification package, `docs/events/014_cannibalism.md`, this cleanup record, and the 2026-07-15 consolidation re-audits.

## Removed runtime surfaces

- Fourth-origin constant, state classifier, candidate weighting, origin flags, origin idea, commander traits, and AI strategy.
- Four-focus local-tree overlay and its four DDS icons, sprite registrations, reward helpers, AI weights, prerequisites, tooltips, and localisation.
- Origin-only prisoner-transfer decision, operation cost contract, target helper, effect, icon, and localisation.
- Lockhouse formation template, starting unit, specialist recruitment decision, recruitment counter, costs, inheritance flags, Wendigo template upgrade, icon, idea, cleanup, and localisation.
- Fixed CBG/CBH country-package pairing and detention-themed portrait/flag direction.
- Scenario selectors, reserved-state markers, capacity checks, and launch distributions tied to the removed origin.

## Replacement contracts

- Allocation selects the first reusable slot from all eight tags after geography determines one of the three remaining origins.
- Scenario capacity uses `count_triggers` across all eight slot-availability triggers, so any reusable combination can satisfy one through six requested countries.
- High and maximum Warlord States launches distribute four or six countries across the three origins. Convergence launches scale from one of each origin to two of each.
- All eight country and history files use the neutral `Cannibal Warlord Slot` identity. Runtime setup supplies origin, region, name, portrait, ideas, units, and AI.
- CBG and CBH flag families use origin-agnostic flat heraldry. Their seven regional portraits use HOI4-style leader busts with no prison or detention imagery.
- Unified recruitment and Wendigo inheritance retain Island Reavers, Siege Eaters, and March Predation Columns only.

## Closed audit proof

- `audits/event014_focus_tree_consolidation_reaudit_2026-07-15.md` confirms exactly 68 local warlord focuses, four focus-specific nodes for each of the three origins, 204 total focus icons across all three trees, and zero retired-origin identifiers.
- `audits/event014_decision_mission_consolidation_reaudit_2026-07-15.md` confirms exactly three live origin-specific warlord actions, three paid unified specialist-recruitment decisions, and atomic three-origin scenario planning.
- `audits/event014_country_package_consolidation_reaudit_2026-07-15.md` confirms eight origin-agnostic slots, exactly three origin packages, zero removed-origin runtime matches, and the full regional leader/flag wiring.
- The current asset authority confirms 204 focus-icon DDS files, 62 idea/modifier DDS files, 135 decision/category DDS files, and exactly three Event 014-referencing GFX files: the dedicated `interface/014_cannibalism.gfx` registry plus the shared `interface/chaosx_pictures.gfx` and `interface/chaosx_super_events.gfx` registries. Their 812 references resolve to 598 unique existing runtime paths with 598 unique hashes and no missing file.
- Current gameplay, localisation, interface, portrait, flag, scenario, country, focus, decision, idea, trait, AI, recruitment, and Wendigo inheritance surfaces contain no live fourth-origin package.

No fallback or partial replacement was used. Generic prison, camp, prisoner-protection, transfer-record, and humanitarian-recovery mechanics remain because they are origin-independent Event 014 content.
