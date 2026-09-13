# Event 42 probability and weighted-logic scenarios

## Audit ownership

Every weighted surface must be inspected by `chaosx_ai_probability_auditor` before implementation is declared complete. The auditor starts with `hoi4.probability_inspect`, states whether each candidate pool and external factor is complete, and distinguishes exact, bounded, sampled, score-only, and unresolved evidence.

After any weight patch, run `hoi4.probability_compare` with the same scenario IDs and inputs.

## Surface inventory

Weighted surfaces expected in Event 42 include:

- recipient selection
- delivery magnitude
- anchor-family selection
- supporting-family selection
- mismatch-family selection
- equipment technology level
- provenance signature
- landing-report count and report-state selection
- nuclear cache chance
- nuclear quantity band
- Evolution III special-slot count
- special-family selection
- rare recovery accident selection
- cluster participation where the cluster owns a member chance
- any AI decision or template score introduced by compatibility receipts

## Named scenarios

### `E42_RECIPIENT_01_UNIFORM_FIVE_COUNTRIES`

Candidate pool:

- one one-state AI minor
- one one-state player minor
- one ordinary subject
- one ordinary major
- one large AI power

All five meet the same validity rules. Expected result: each has exactly 20 percent raw selection probability. Country size, player status, subject status, major status, factory count, manpower, war status, and stockpile do not change the result.

Evidence: exact normalized pool evaluation.

### `E42_RECIPIENT_02_INVALID_SPECIAL_COUNTRY_REMOVAL`

Start from the five-country pool and add one special Chaos country, one actual nonhuman country, and one government without an owned and controlled state.

Expected result: the three invalid candidates have zero eligibility. The original five remain equal at 20 percent each after normalization.

Evidence: exact eligibility and normalized pool evaluation.

### `E42_RECIPIENT_03_REPEAT_RECIPIENT_ALLOWED`

Give one candidate a completed prior Event 42 history entry. Give another candidate an active unresolved Event 42 report chain.

Expected result: prior completed history does not alter weight. The active-chain country is temporarily ineligible. All other valid countries remain equal.

Evidence: exact evaluation before and after report-chain cleanup.

### `E42_MAGNITUDE_01_BASELINE`

Active stage: baseline. No external scale modifier.

Expected starting distribution:

- Enormous 60 percent
- Colossal 30 percent
- Impossible 10 percent

Evidence: exact random-list evaluation and seeded simulation for sanity.

### `E42_MAGNITUDE_02_EVOLUTION_ORDERING`

Evaluate baseline and all three evolutions with identical external state.

Expected result: the probability of Impossible rises monotonically at each stage. The probability of Enormous falls monotonically. Colossal does not collapse into a negligible outcome.

Starting targets:

- baseline 60, 30, 10
- Evolution I 50, 35, 15
- Evolution II 40, 40, 20
- Evolution III 35, 40, 25

Evidence: exact comparison and sensitivity render.

### `E42_FAMILY_01_NO_RECIPIENT_OPTIMIZATION`

Use the same random seed and stage for a landlocked minor, an island minor, a fuel-starved country, and a major with broad infrastructure.

Expected result: recipient conditions do not change the anchor-family weight table. Technical DLC or token validity may change a token inside a family, but geography and strategic usefulness do not change family probability.

Evidence: exact score comparison across four scenarios.

### `E42_FAMILY_02_MISMATCH_PRESENCE`

Evaluate every stage across a complete safe conventional pool.

Expected result: every valid package contains at least one mismatch family when at least one technically valid mismatch exists. No one mismatch family dominates through broad applicability.

Evidence: bounded evaluation plus seeded simulation of at least 10,000 manifests.

### `E42_FAMILY_03_POOL_STARVATION`

Temporarily remove one or more DLC-dependent designer families and mark one family invalid.

Expected result: failed technical slots reroll inside a comparable-value family pool. Package family count and strategic value remain inside stage targets. Common infantry equipment does not absorb nearly every failed slot.

Evidence: probability sweep over available-family masks and starvation render.

### `E42_TECH_01_BASELINE_LEVELS`

Evaluate a recipient with early equipment research, one with mid-game research, and one with late-game research.

Expected baseline mix:

- 55 percent current or recognizable
- 30 percent one meaningful generation ahead
- 10 percent foreign peer or alternate design
- 5 percent highest safe conventional tier

Expected result: recipient research changes relative tier labeling, not package quantity. No recipient loses a family because its research is weak.

Evidence: exact evaluation with complete tier pools.

### `E42_TECH_02_EVOLUTION_I_ADVANCEMENT`

Evaluate the same recipients under Evolution I.

Starting mix:

- 20 percent peer
- 45 percent one or two generations ahead
- 25 percent highest safe conventional tier
- 10 percent unusual foreign or specialized variant

Expected result: advanced outcomes dominate peer outcomes, while peer equipment remains possible.

Evidence: exact comparison with baseline.

### `E42_NUCLEAR_01_CHAOS_SWEEP`

Active stage: Evolution II or III. Sweep Chaos from 400 through 1200.

Expected starting chance:

- 25 percent at 400 to 599
- 35 percent at 600 to 799
- 45 percent at 800 to 999
- 55 percent at 1000+

Expected result: chance rises monotonically and caps at the defined maximum. Recipient nuclear status does not alter the chance, although it changes the guarded Chaos milestone after receipt.

Evidence: exact sweep and chart.

### `E42_NUCLEAR_02_QUANTITY_BY_MAGNITUDE`

Condition on a successful nuclear slot and evaluate all magnitude bands.

Expected quantity ordering:

- standard cache 25 to 75
- Colossal cache 75 to 150
- Impossible cache 150 to 250

Expected result: every value is substantial and rounded. Recipient size has no effect.

Evidence: range evaluation and seeded simulation.

### `E42_SPECIAL_01_SLOT_COUNT`

Active stage: Evolution III with at least three safe special families.

Starting distribution:

- zero families 40 percent
- one family 40 percent
- two families 15 percent
- three families 5 percent

Expected result: a special family appears in 60 percent of Evolution III packages. No roll selects more unique families than the current safe pool contains.

Evidence: exact evaluation and seeded simulation.

### `E42_SPECIAL_02_FAMILY_EQUALITY`

Use a safe pool of four families with no family-specific rarity modifier.

Expected result: each family has equal chance to occupy the first special slot. Subsequent slots sample without replacement. Quantity semantics do not change selection chance.

Evidence: exact combination evaluation.

### `E42_SPECIAL_03_EXCLUSION_AND_REROLL`

Mark one family conditional and one family excluded.

Expected result: neither appears. The remaining safe families renormalize without creating a blank special token. The conventional package is unchanged.

Evidence: exact pool evaluation.

### `E42_REPORT_01_COUNT_BY_MAGNITUDE`

Evaluate report count at each magnitude and evolution.

Expected result: report count remains between three and seven. Larger packages trend upward, but all values remain possible where intended. The count is independent of recipient state count.

Evidence: exact score evaluation.

### `E42_REPORT_02_ONE_STATE_RECIPIENT`

Recipient has one valid state and report count is seven.

Expected result: all reports target the valid state with different site or theme roles. State selection does not fail, reduce the package, or create repeated equipment grants.

Evidence: deterministic sequence inspection, not a probability-only claim.

### `E42_CLUSTER_01_ROOT_AND_MEMBER`

Evaluate Event 42 as a selected cluster root and as an optional member under the final Various Anomalies registry.

Expected result: participation follows the cluster's declared Low-member rules. One cluster transaction can create at most one Event 42 delivery. Event 42's own recipient selection remains uniform.

Evidence: exact cluster pool evaluation plus event-chain inspection.

### `E42_AI_01_SPECIAL_TEMPLATE_SCORE`

For each allowlisted fielding receipt, evaluate AI template or creation score under:

- adequate stockpile and supply
- adequate stockpile but no fuel
- low manpower
- already excessive special-unit share
- source event later grants normal production

Expected result: AI fields finite special units only when support conditions pass, does not starve ordinary forces, and stops when the stockpile or cap is exhausted.

Evidence: score evaluation, sweeps, and probability comparison after tuning.

### `E42_AI_02_CAPTURED_PAYLOAD_USE`

For each allowlisted payload, evaluate AI use under valid and invalid war, target, policy, range, fuel, command, cooldown, and consequence conditions.

Expected result: invalid cases score zero. Valid use remains rare enough to preserve strategic judgment and uses the owner system's target ordering.

Evidence: exact validity evaluation and score sweep.

## Sequence evidence

Use `hoi4.probability_sequence` only when the Event 42 repeatable-event manifest explicitly provides the complete cadence inputs required by the tool, including repeatable cap reduction, weight recovery, cluster intervention, event timer behavior, evolution pacing, enable state, and terminal conditions.

Do not use an incomplete sequence model to claim a campaign-wide firing probability.

## Comparison requirement

Every final weighted change needs:

1. baseline inspection using these scenario IDs
2. parent or owner patch
3. `hoi4.probability_compare` with the same candidate pools and external state
4. a short finding that states whether the intended ordering, caps, equality, and starvation limits were preserved

Unresolved or incomplete pools remain explicit blockers.
