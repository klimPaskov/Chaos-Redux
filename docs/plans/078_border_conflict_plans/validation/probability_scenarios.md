# Probability and timing audit scenarios

## Required auditor and tools

Route this work through `chaosx_ai_probability_auditor`.
Start with `hoi4.probability_inspect` to identify real implemented random pools, seed gates, evolution MTTH, shared selection weights, helper inputs, and dynamic settings.
Then use named-scenario evaluation and threshold sweeps.
Use seeded simulations only when uncertainty and its distributions are declared.
Use comparisons after each relevant implementation change.
Render evidence when it makes bias, timing, or sensitivity easier to review.

No probability tool was executed during this planning pass.
The percentages below are intended design inputs.
They are not empirical native results or a substitute for the mandatory adapter-backed audit.
Native battles are not assigned win probabilities by this package.

## Scenarios

| ID | Scenario inputs | Audit question |
| --- | --- | --- |
| Q01 | Two valid target states, one has five legal staging states and one has one | Does target selection remain 50 percent each before the staging draw? |
| Q02 | Three valid targets owned by A and one owned by B | Does uniform target sampling produce the intended 75/25 target-owner exposure without hidden country weighting? |
| Q03 | Same pair discovered from both country directions | Is a canonical pair sampled only once? |
| Q04 | Two pair orders and one contested endpoint | Is order randomized reproducibly and is the resulting conditional availability reported honestly? |
| Q05 | Long-border slot sets with different graph shapes but equal F | Are root counts equal while target distributions remain conditioned on feasible selection? |
| Q06 | F across 0, 1, 4, 5, 9, 10, and 15 | Are allowance thresholds exact with no off-by-one additions? |
| Q07 | Eligible attacking root victory at Chaos 400 with no third evolution | Does one valid opportunity use 25 percent, with no duplicate roll from the losing side's callback? |
| Q08 | Same root with Border Momentum and Borders in Motion applied | Does the valid seed opportunity use 75 percent? |
| Q09 | Root wins but no newly adjacent legal target exists | Is there no meaningful seed draw, retry, or hidden delayed success chance? |
| Q10 | Seeded chain wins several times | Is continuation automatic when valid, rather than repeatedly multiplied by the original seed chance? |
| Q11 | Every evolution-toggle combination at Chaos 600 | Are disabled mechanics impossible through a higher-tier branch? |
| Q12 | Active wave crosses 200, 400, and 600 at scheduled dates | What does the verified MTTH adapter predict under these changing eligibility conditions? |
| Q13 | Active wave closes before a pending mutation | Is remaining mutation probability zero after closure? |
| Q14 | Repeat wave arrives with an older active pair | Are occupied roots removed before the new conditional pool is evaluated? |
| Q15 | Shared Wars selection and repeat recovery before and after rework | Are the framework's weights preserved, with no extra draws per battle or continuation? |
| Q16 | Country AI acknowledgements and informational entries | Is there no invented outcome chance or willingness score for a non-choice? |

## Reporting distinctions

Uniformity applies to the distinct valid target states available at the moment of that draw.
It does not mean equal attacking and defending probability for two countries that own different numbers of candidate states.
It also does not mean an unconditional uniform distribution over final active states after reservation conflicts and extra-front selection.
Report those conditional boundaries explicitly.

A 25 percent root seed chance is not a 25 percent chance to capture the next state.
The root must first achieve a real native victory and have a valid newly opened target.
The next battle still needs an actual military result.
A 75 percent seed chance is not a predicted conquest rate.

MTTH timing must come from the verified game-version adapter.
Do not assume a 90-day timing parameter is a fixed 90-day delay, a guaranteed 90-day mean, or a daily probability of one ninetieth.
Provide exact, bounded, sampled, and unresolved findings as distinct categories.

AI decision willingness is not a click probability.
The current design has mandatory allocation and no strategic purchase decisions.
If implementation introduces a new AI strategy or decision weight, add its exact availability, costs, target state, and competing actions to a new named scenario before auditing it.

## Evidence bundle

Return inspection coverage, named scenario inputs, adapter version, exact tool actions, result files, unresolved inputs, and a comparison against the prior implementation when applicable.
Report native military uncertainty separately from script selection probabilities.
Do not choose the desired design values on behalf of the parent.
The parent resolves balance changes and updates every affected specification and tooltip source.
