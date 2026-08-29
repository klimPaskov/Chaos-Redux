# AI probability audit prompt for Event 028: Asteroid Incoming

Act as the read-only `chaosx_ai_probability_auditor`. Read the Event 028 specification pack, the implemented event option pool, target relation helpers, target scores, decision AI weights, and the relevant project probability skill. Use the HOI4 MCP probability workflow for every in-scope surface.

Start with `hoi4.probability_inspect`. Identify the exact four-option pool, every external factor, normalization rule, and any unresolved scripted input. Do not infer a final probability from an incomplete pool.

## Opening option scenarios

Evaluate these scenarios with the full three-target-plus-miss pool.

- `AST_AI_01`: Stable democratic major at peace, three neutral or friendly targets. Miss must dominate.
- `AST_AI_02`: Democratic major losing an existential war, one hostile major and two neutrals. Miss remains strong. Only the hostile major can become plausible.
- `AST_AI_03`: Fascist major in total war, enemy faction leader, weak enemy, and neutral. The faction leader should rank first or close to miss. Neutral remains near zero.
- `AST_AI_04`: Nonaligned minor at peace facing three unrelated majors. Miss strongly dominates.
- `AST_AI_05`: Existing destructive special actor facing three enemies. Best strategic enemy can dominate miss only when route identity supports it.
- `AST_AI_06`: Subject, faction ally, and enemy. Subject and ally must score zero or a proven protected minimum. Enemy competes with miss.
- `AST_AI_07`: Fragile chooser at 700 Chaos with fragmentation. Fragment risk raises miss preference relative to the otherwise identical 500-Chaos case.
- `AST_AI_08`: Near-capitulation chooser at 700 Chaos with one existential enemy. The enemy strike becomes materially more likely than in a stable case.
- `AST_AI_09`: Chooser controls several mineral sites and faces one distant enemy. Miss gains weight because new fragments can threaten its advantage.
- `AST_AI_10`: Ally, guarantee, and subject as all three targets. Miss is effectively certain.

For every scenario, report raw scores, normalized probabilities when exact, ordering, dominance, protected-target behavior, and sensitivity to ideology, war state, capitulation progress, relation type, target strategic value, and fragmentation.

## Sensitivity sweeps

Run sweeps for:

- Chaos from 0 to 999
- Capitulation progress from safe to near defeat
- Target relation from ally through neutral to active enemy
- Target value from weak minor to hostile faction leader
- Fragmentation off and on
- Chooser stability and war support
- Chooser route identity where the implementation exposes one

Render a matrix or sensitivity view when it improves review.

## Recovery decision scenarios

Inspect and evaluate the complete visible decision pool for these situations.

- High preventable deaths with adequate equipment should prioritize mobile hospitals.
- Capital supply disconnection should prioritize the emergency rail corridor.
- Low train reserve during a collapsing front should suppress expensive rail and reconstruction actions.
- Severe dust with strong industry should prioritize factory hardening.
- A threatened controlled main crater should prioritize perimeter security.
- A distant enemy fragment site should not override homeland defense.
- A country with urgent national damage should delay global observation contribution until reserve floors are met.

Distinguish availability, AI score, and normalized selection where several decisions compete.

## Patch comparison

The auditor is read only. Return baseline evidence before the owner changes weights. After the owner patches, run `hoi4.probability_compare` with the same named scenarios and inputs. Report changed ordering, probability shifts, protected-target regressions, new starvation, and unresolved cases.

Do not choose a balance target that conflicts with the specification. Do not patch source. Mark results exact, bounded, sampled, score-only, or unresolved according to the actual evidence.
