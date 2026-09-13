# Event 052 Intel Leaked Specification Package

This package is the source-design handoff for Chaos Redux Event 052, **Intel Leaked**.

The event is a Minor Repeatable intelligence crisis available from Chaos level 1. Each ordinary firing compromises one valid player-controlled country or one valid major power. Foreign governments receive a temporary intelligence windfall, while the target races to change codes, withdraw endangered personnel, rewrite plans, rebuild networks, and decide whether to turn the breach into a deception channel.

The design keeps one persistent player-facing value, **Exposure**. Exposure measures how useful the leaked archive remains. Archive contents, recipient confidence, operative risk, foreign reliance, domain scores, and investigation findings remain internal unless a decision or report makes part of them relevant to the player.

Event 052 belongs to the Intelligence cluster as its low-severity repeatable member. Event 039 remains the cluster's medium-severity fire-once leadership and murder crisis. The two events can interact through bounded evidence and target-state hooks without sharing identities, escalation routes, or terminal content.

## Intended extraction location

Extract the top-level `052_intel_leaked_specs/` folder into:

```text
docs/specs/
```

The resulting source folder should be:

```text
docs/specs/052_intel_leaked_specs/
```

## Recommended reading order

1. `specs/052_intel_leaked_spec_part_1_core_incident.md`
2. `specs/052_intel_leaked_spec_part_2_exposure_and_exploitation.md`
3. `specs/052_intel_leaked_spec_part_3_damage_control_and_recovery.md`
4. `specs/052_intel_leaked_spec_part_4_deception_investigation_and_variants.md`
5. `specs/052_intel_leaked_spec_part_5_evolutions_repeatability_and_connections.md`
6. `specs/052_intel_leaked_spec_part_6_ai_presentation_achievements_and_balance.md`
7. The matrices under `matrices/`
8. The specialist prompts under `prompts/`
9. The implementation and catalogue handoffs under `handoffs/`
10. The review records under `quality/`

## Package boundaries

The design uses an ordinary decision category with a static category picture, phased actions, dynamic reports, and Event Log integration. This surface is sufficient because the player manages one visible value and a small number of current responses. Foreign exploitation, archive composition, reliance, and network risk remain deeper simulation layers behind the readable player surface.

The source specification gives direction for final player-facing text. Working labels identify mechanics, actions, missions, variants, and achievements. They are not finished localisation and should be rewritten during implementation in the established Chaos Redux voice.

The existing `chaosx.nr52` namespace and Event 052 identity remain stable. The current repository source contains a legacy two-event implementation that gives every country permanent maximum base intelligence against the target. The replacement design requires temporary, scaled, reversible exposure with recovery, cleanup, decisions, deception, and evolution behavior.

## Source and process status

Every supplied project file was read fully, including all Markdown files, the TOML configuration, all three CSV catalog exports, the ZIP archive, and all twenty extracted subagent TOML definitions. `source_inventory.md` records byte counts, line counts, SHA-256 hashes, and reading status.

The connected tool registry did not provide a working subagent execution route. The registry probe failed with an HTTP 404. The package therefore does not claim that external subagent processes ran. The applicable subagent contracts were applied as separate manual specialist passes, and the result is recorded in `quality/052_intel_leaked_manual_specialist_passes.md`.

Historical research informed the deception and counterintelligence design. The research pass used official English Heritage, U.S. Army University Press, CIA Center for the Study of Intelligence, and NSA material. The sources support controlled leaks, false traffic, double-agent risk, feedback from intercepted responses, compartmentation, and the slow value of cryptanalytic reconstruction. The event remains fictional and never assigns its breach to a real historical operation.

## Package verification

- `source_inventory.md` records the complete supplied-source reading pass.
- `manifest.md` records every package file, byte count, line count, and SHA-256 hash.
- `quality/052_intel_leaked_acceptance_criteria.md` defines the implementation pass conditions.
- `quality/052_intel_leaked_improvement_loop_closure.md` records the depth and anti-bloat conclusion.
- `quality/052_intel_leaked_completion_audit.md` checks the completed planning package against the user brief and project rules.
- `matrices/052_intel_leaked_chaos_impact_map.md` separates Event 052 Chaos changes from generic war, death, annexation, and other shared sources.
- `matrices/052_intel_leaked_ai_probability_scenarios.md` defines the mandatory weighted-behavior audit scenarios for implementation.

## Core non-negotiables

- Baseline firing compromises exactly one target.
- The target is the current valid player-controlled country or a random valid major power.
- Every foreign ordinary government receives a meaningful temporary intelligence advantage.
- Exposure always declines through time and can decline faster through real damage-control action.
- Agency and operative content deepens the event when available but never carries the base event alone.
- The target can exploit foreign reliance through Poison the Leak and domain-specific deception.
- Deep Files activates from 400 Chaos.
- Total Compromise activates from 800 Chaos and can affect several countries at once or produce one exceptionally severe target profile.
- Each repeat firing creates a fresh incident with fresh targets, archive composition, duration, exploiters, risks, and recovery state.
- The event never gives untracked permanent intelligence.
- The source of the breach remains unresolved.
