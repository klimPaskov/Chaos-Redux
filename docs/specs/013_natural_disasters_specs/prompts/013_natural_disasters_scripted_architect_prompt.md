
# Scripted system architect prompt for Event 013 Natural Disasters

Use `chaosx_scripted_system_architect` before implementing repeated Event 13 helper logic. This is for architecture or narrow helper implementation inside the current task scope.

## Design target

Event 13 needs reusable helper families for disaster sequence setup, target selection, damage application, death logging, aftermath ledgers, recovery progress, follow-up scheduling, cluster member slots, scenario bypass setup, and cleanup.

## Required helper map

Propose or implement narrow helpers for:

- building an Event 13 sequence context,
- choosing evolution stage and family set,
- selecting valid states by family,
- scoring targets by population, buildings, terrain, coast, port, river, mountain, desert, forest, war state, and recent hit memory,
- applying family-specific building damage,
- applying real state population loss and civilian death entries through per-state dynamic percentage formulas,
- applying state modifiers and supply penalties,
- starting country and state aftermath ledgers,
- activating recovery decisions and missions,
- advancing recovery progress,
- scheduling delayed follow-ups without extra random-event history rows,
- marking and clearing sequence state,
- handling Natural Disasters cluster member slots,
- handling Disaster Barrage scenario type and intensity bypass,
- placeholder routing for Sandstorm and Event 46.

## Constants and tuning

Plan script constants for:

- incident count by baseline, evolution, cluster slot, and scenario intensity,
- delay bands,
- severity bands,
- warning chance factors,
- death-rate scaling factors, percentage ceilings, density multipliers, preparedness reductions, and safeguards against fixed casualty amounts,
- building damage weights by family,
- recovery costs,
- AI weights,
- follow-up chain weights,
- news threshold gates.

## Output

Return a helper map with names, scopes, inputs, outputs, side effects, cleanup, call sites, constants, risks, unsupported dynamic fields, and validation notes. If helpers are implemented, write a patch handoff under:

`docs/plans/013_natural_disasters_plans/subagent_handoffs/`
