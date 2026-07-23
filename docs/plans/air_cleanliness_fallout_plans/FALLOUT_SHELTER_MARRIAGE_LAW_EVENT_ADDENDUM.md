# Shelter Marriage Law event addendum

This addendum implements the next country-level global-survival chain after
Empty Ward. The chain remains dormant until the accepted scheduler activation
receipts exist.

## Frozen inputs

| Input | Source | Use |
| --- | --- | --- |
| Cohesion | `fallout_survival_cohesion_current` | Viability and communal threshold |
| Food | `fallout_survival_current_entries^1` | Eligibility, viability, and costs |
| Shelter | `fallout_survival_current_entries^8` | Eligibility and private-law threshold |
| Recognition | `fallout_survival_current_entries^9` | Eligibility and civil or religious thresholds |
| Generation count | `fallout_generation_change_count` | Eligibility and viability context |
| Legitimacy | `fallout_marriage_303_legitimacy` | Durable law trust |
| Integration | `fallout_marriage_303_integration` | Cross-shelter household integration |
| Fertility | `fallout_marriage_303_fertility` | Durable family recovery signal |
| Exposure | `fallout_marriage_303_exposure` | Durable exposure pressure carried through the chain |

## Review contract

Candidate `303` uses transaction `710017` and route `7117`. Events `303` through
`309` contain one human opening, one hidden-AI opening, one human delayed
result, one hidden-AI result, one human callback, one hidden-AI callback, and
cleanup. The result is delayed exactly 42 days and the callback exactly 300
days. Four policies have separate costs, deterministic grading, visible
tooltips, hidden-AI choice, outcome memories, timed modifiers, and 15 Event Log
payloads. Failure uses shared Deaths at 0.08 percent for the result and 0.04
percent for the callback.

## Boundaries

No scheduler activation setter is added. No ordinary Zombie id, file, asset,
audio, sprite, or path is reused. No state or actor target is invented for a
country-level family-law decision.
