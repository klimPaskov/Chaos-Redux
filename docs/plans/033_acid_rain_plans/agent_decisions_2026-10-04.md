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

## Implementing-engineer decisions, round 1

These decisions were taken by the Event 033 implementing engineer under the same full design authority, choosing the spec-consistent option in each case.

### D7. Decision cost text reads published display rows

Disposition: implemented (commit "Show real costs on every Acid Rain decision").
The quote refresh effects publish one persistent row per decision for player countries (`acid_rain_cost_<row>_<family>`), passed through the same final quote step (`acid_rain_finalize_loaded_quote`) that the affordability trigger and the debit use, so the shown numbers are the paid ones.
AI countries skip the display rows because they never read them.
The host worker refreshes player rows every worker tick along with AI rows, so discounts and band changes reach the text within three days.
Evacuation and decontamination show "trains or convoys" because the chosen state, not the country, decides the route, and localisation cannot rely on the targeted state scope.
The `_blocked` variant is selected by the engine from `custom_cost_trigger`, which is the same trigger the start transaction rechecks.

### D8. Evacuation effect values

Disposition: implemented (commit "Give severe evacuations time to work").
The partial share is 50 percent of the full evacuation reduction (`acid_rain_mortality.evacuation_partial_share`), granted from one full day after the start (`acid_rain_preparedness.evacuation_partial_delay_days`) to severe and superstorm pulses only.
The finished-evacuation damage-pressure reduction is limited to severe and superstorm pulses for the same reason.
The disruption modifier `acid_rain_evacuation_disruption` costs 15 percent local factory output, 25 percent local construction speed and 15 percent local supply; it is added at the start, removed at once if the evacuation fails, and removed when the severe episode closes after a finished evacuation, with a 40-day safety duration.
The evacuation decision requires a free national action slot, because the start transaction already required one and a decision that could be taken without effect is a defect; concurrency (D6) replaces this gate with per-state receipts.

### D9. Registry arrays are created before indexed writes

Disposition: implemented (commit "Create Acid Rain registry arrays before writing their elements").
An indexed `set_variable` only changes an existing element (Data structures, arrays section of the offline wiki), and every other system in the mod creates its arrays first; 74 Event 033 arrays were only cleared and then written by index.
Each registry is cleared and resized to its bound when it is initialised; severe-cell and superstorm slots start retired so allocation sees them as free.

### D10. Operation model for D6

Disposition: implemented (commit "Run Acid Rain response operations side by side").
National families (Shelter Protocols, Water Distribution, Medical Surge, Reroute Transport, demobilization) each hold one row in `acid_rain_op_*_entries` and their own completion event (`chaosx.nr33.42` to `.46`).
Evacuations and recovery work are state operations held on the state with the paying country as a scope variable, listed in the owner's `acid_rain_op_states`, and completed by the state event `chaosx.nr33.47`; `acid_rain_evacuations_active` and `acid_rain_recovery_ops_active` count operations in progress against the band caps 2/2/4/8 and 1/1/2/3.
Civilian factory commitments of running operations sum into one variable-valued modifier, `acid_rain_action_commitment`.
A completed evacuation keeps its protection and disruption until its severe episode closes but no longer occupies an evacuation slot.
Natural acute closure keeps paid recovery work and demobilization running and releases the rest; administrative closure releases everything.

### D11. Decision visibility and gates (Part 5 category table)

Disposition: implemented (same commit as D10).
Projects stay visible and payable during warnings and exposure.
Recovery decisions appear only when no warning, exposure or forecast covers the country, and each targets a state with aftermath and no acute weather of its own.
Shelter Protocols, Water Distribution and Reroute Transport cannot be bought while their protection is still in force, and Medical Surge waits for medical fatigue to end.
Demobilization opens whenever no warning, exposure or forecast covers the country and there is apparatus to wind down; it cancels unfinished projects through the normal path, keeps the recovery tail, and grants `acid_rain_demobilized_recovery` (10 percent repair speed, 5 percent construction speed) for 60 days, which also blocks a repeat.
The AI does not demobilize while the crisis is active and projects are running, so paid projects are not thrown away.

### D12. Two Regions Ready late binding (D4)

Disposition: implemented (same commit as D10).
When a warning visit is recorded for a state, its controller binds every running urgent operation and evacuation that has no visit yet to that visit; the existing arrival recorder then credits only completion strictly before arrival and rejects starts after arrival.

### D13. Recovery actions follow the recorded burden

Disposition: implemented (commit "Tie Acid Rain recovery to the damage the rain recorded").
Restore Transport targets only states with rain-recorded infrastructure or railway damage points and clears those points when it finishes; Repair Industry does the same for civilian and military factory points, so neither can repair more than the rain damaged.
Decontamination targets states whose rain impact left an environmental burden (`acid_rain_environmental_burden`, set by every recorded window impact and cleared when the aftermath tier reaches zero); it consumes nothing else, so a state can always be cleared once its structural damage is repaired.
AI scoring favours transport when transport points are the larger structural burden, industry when factory points are larger, and decontamination when no structural damage remains.
Probability evidence: `hoi4.probability_inspect` with adapter `decision_ai_will_do` on `common/decisions/033_acid_rain_decisions.txt` returned `INTERNAL_ERROR` on 2026-10-04, as it did for the lead, so no baseline or comparison could be produced; the factors are the existing `@acid_rain_ai_*` aftermath factors plus one new 1.5 factor.

### D14. Humanitarian amounts (D5)

Disposition: implemented (commit "Register Acid Rain humanitarian pressure with the famine system").
`famine_adapt_acid_rain_state` is a minimal append to the famine-owned adapter file and its documentation table; it mirrors the Event 013 adapter and requests natural-disaster pressure.
Event 033 builds the proof bundle in `acid_rain_register_humanitarian_pressure` with source id 33, the Acid Rain death reason, the current generation and a per-transaction revision (positive pulse receipt count, aftermath tier, or evacuation operation key).
Registered amounts: each exact positive pulse loss; 0.5 percent of the state population when its aftermath first reaches tier 2 and 1 percent at tier 3; 2 percent when an evacuation of a state with at least 500k people finishes.
At the famine owner's 20 percent maximum share these are small pressure steps, so the rain adds strain without overriding famine's own drivers.
The famine and migration owner could not be reached from this run; the append touches no existing famine code and is recorded here for that owner's review.
