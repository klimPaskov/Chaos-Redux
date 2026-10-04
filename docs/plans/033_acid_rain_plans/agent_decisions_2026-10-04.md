# Event 033 agent decisions, 2026-10-04

Disposition: accepted and queued.
Acceptance basis: the user granted the Event 033 lead full design authority on 2026-10-04 and directed it to take the recommended, spec-consistent option for every open choice and record it here.
Each decision below resolves an item that earlier handoffs left unresolved; implementation evidence is recorded separately when the work lands.

## D1. Adopt the stopped thread's uncommitted Event 033 work

The uncommitted Event 033 rewrite (consequence transaction, episode caps, damage receipts, quote/target bridge repairs, GUI wiring, achievements, aftermath file, delivered animation and veil DDS files) is adopted after a load-safety review and committed with the shared-tree workflow.
Basis: the accepted consequence repair spec is implemented in that work, `.tools/validation/validate_033_acid_rain.py` passes, the population-helper source replay passes all 40 cases, and the routed static-lint fixes 3, 4 and 13 plus the working-tree halves of 1 and 2 exist only there.
The shared population-first helper in `common/scripted_effects/chaosx_dynamic_effects.txt` and its twelve caller output declarations are committed as their own hunk-only commit so other owners' uncommitted hunks in those files stay untouched.

## D2. Severe and superstorm forecast lead becomes nine days

`acid_rain_evolution.severe_forecast_lead_days` and `acid_rain_evolution.superstorm_lead_days` change from 3 to 9.
The seven-day evacuation matrix, the 0.05 percent per-state ceiling, and the accepted Three Evacuations rule (completion strictly before the first severe pulse) stay unchanged.
Basis: Part 5 requires the evacuation receipt to apply before impact, the decision prompt requires completion before the first severe pulse for full protection, and the achievement acceptance requires the same; with a three-day lead none of these can happen.
Severe targets are already held out of front-footprint retirement while targeted, so the longer lead does not lose targets when the front drifts.
The improvement-loop planner recommended exactly this value, which leaves two days of reaction slack over the seven-day job.
Part 7, the evolution and Event Details text, and the catalog notes are updated to nine days in the same change.

## D3. Evacuation partial effect and local disruption

A paid evacuation that has run one full day grants a reduced share of the evacuation mortality reduction to severe and superstorm pulses; completion grants the full reduction.
Evacuation protection applies only to severe and superstorm pulses, as Part 5 states.
A new state dynamic modifier applies the promised temporary production, construction and supply penalty for the evacuation's duration and is removed when the severe episode closes.

## D4. Two Regions Ready uses late warning binding

A paid urgent national action that is still running when a new warning is published for a responsible state, and that has no warning association yet, binds to that warning visit.
Completion strictly before that visit's arrival then counts; an action that starts after arrival still disqualifies, and one action still credits only one visit.
Basis: every urgent action lasts 14 to 21 days against a seven-day warning, so only an action started before the warning can finish inside it, and the existing bridge captured the association only at start time.

## D5. Humanitarian integration uses a source-specific famine adapter

Acid Rain registers its proven consequences through an Event 033 famine adapter that mirrors `famine_adapt_natural_disaster_state`: exact applied mortality pulses, tier-2 and tier-3 aftermath, and completed large evacuations, each with Acid Rain source identities distinct from Event 013 and Air Winter.
Evacuation displacement is registered as humanitarian disaster pressure, not as a migration cohort, because Part 5 forbids permanent population transfer without a verified migration API and the migration adapter documents Event 33 as lacking cohort facts.
The adapter addition is coordinated with the famine and migration owner as a minimal append.

## D6. Concurrency follows Parts 5 and 8

Each national urgent family keeps its own receipt, so different families can run at the same time while each family runs at most once.
Evacuations and state recovery operations keep per-state receipts, and the country counters count in-progress operations against the 2/4/8 evacuation caps and the 1/1/2/3 recovery-operation caps.
Payment, reservation and one-time return stay per operation.
