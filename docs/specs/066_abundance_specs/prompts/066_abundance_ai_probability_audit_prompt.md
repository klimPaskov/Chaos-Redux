# Event 066 AI and Probability Audit Prompt

Use `chaosx_ai_probability_auditor` with `fork_context=false`.
This is a read-only audit.
Do not patch source or choose the intended balance target.

## Sources

Read:

- `docs/specs/066_abundance_specs/specs/066_abundance_spec_part_3_choice_generation.md`
- `docs/specs/066_abundance_specs/specs/066_abundance_spec_part_5_evolutions_and_cluster.md`
- `docs/specs/066_abundance_specs/specs/066_abundance_spec_part_6_global_flow_ai_multiplayer.md`
- `docs/specs/066_abundance_specs/research/066_abundance_probability_scenario_matrix.md`
- the implementation files and provider manifest supplied by the parent
- `AGENTS.md`, `chaos-redux-events`, and `chaos-redux-subagents`

## Mandatory workflow

Start with `hoi4.probability_inspect` for every weighted surface.
Name the source revision, candidate pool, external factors, scenario ID, and whether the pool is complete.
Then use the minimum evidence tool that answers the question:

- `hoi4.probability_evaluate` for exact option or card pools
- `hoi4.probability_sweep` for Chaos, evolution, profile, shortage, danger, and desperation changes
- `hoi4.probability_simulate` for large dynamic pools and repeat diversity
- `hoi4.probability_compare` for every post-tuning comparison against the same baseline scenarios
- `hoi4.probability_render` for cardinality, family share, AI ordering, cluster incidence, and sensitivity views
- `hoi4.probability_sequence` only when cadence, recovery, caps, cooldowns, removals, resets, and terminal states are fully declared

Label every result exact, bounded, sampled, score-only, or unresolved.
Do not calculate an exact probability from an incomplete provider pool.

## Surfaces to audit

- candidate provider and family weighting
- Evolution I rarity, strange, active-crisis, and harmful shifts
- single, pair, and triple cardinality weighting
- Low, Standard, Medium, and High profiles
- duplicate and hard-conflict rerolls
- recent-candidate and family dampening
- option position randomization
- AI card scores and final `ai_chance`
- AI danger, desperation, saturation, and route modifiers
- cluster Event 66 slot incidence before and after coalescing
- any fallback or recovery random blocks

## Scenario contract

Run every applicable ID from `research/066_abundance_probability_scenario_matrix.md`.
When an implementation cannot construct a scenario, mark it unresolved and name the missing data.
Do not silently replace the pool or external state.

The audit must prove these orderings:

- baseline has no benefit filter
- Evolution I increases strange and harmful odds over the same controlled pool
- ordinary values remain material after Evolution I
- pair frequency rises from Low toward High at Evolution II
- triples are unavailable before Evolution III
- Evolution III Standard and Medium are triple-led, while Low keeps strong pair presence
- option order has no effect on generation or AI selection
- recent values remain possible
- low-weight positive providers are not permanently starved
- stable ordinary AI favors strong safe cards over severe harmful cards
- desperate and owner-specialized AI can accept risk
- all-harmful option sets still resolve without a generic fallback
- three cluster slots do not produce three Event 66 waves

## Baseline and comparison cycle

The first pass records baseline evidence before any balance patch.
Return exact scenario hashes and artifact references to the parent.
After the owner applies tuning, repeat the same scenarios and use `hoi4.probability_compare`.
Do not accept different pools, changed seeds, or renamed scenarios as a valid comparison without explaining the effect.

## Report

Return:

- inspected surfaces and source locations
- scenario IDs and complete inputs
- tool calls selected and why
- exact, bounded, sampled, score-only, and unresolved findings
- target-band and ordering violations
- dominance and starvation findings
- option-index bias findings
- AI preference findings
- cluster coalescing incidence findings
- baseline versus patched comparison
- rendered evidence references
- remaining uncertainty

The audit remains read-only.
Balance decisions belong to the parent and owning implementation agent.
