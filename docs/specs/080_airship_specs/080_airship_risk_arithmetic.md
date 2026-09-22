# Event 080: Illustrative risk arithmetic

This appendix checks only arithmetic in the proposed fixed-Condition model. It does not model repairs, wear, delays, changing hazards, incidents that reduce Condition to zero, emergency choices, or actual game code. It is not an MCP probability audit or an achieved balance result.

For a single unchanged exposure, the direct fatal-branch probability is the operational incident probability multiplied by the conditional fatal severity probability. For 121 independent identical exposures, the chance of at least one such direct fatal branch is `1 - (1 - p)^121`.

| Fixed band | Incident probability | Fatal given incident | Direct fatal per exposure | At least one direct fatal branch in 121 identical exposures |
|---|---:|---:|---:|---:|
| Sound | 5% | 0.5% | 0.025% | 2.9801% |
| Worn | 10% | 2.5% | 0.250% | 26.1311% |
| Damaged | 20% | 10% | 2.000% | 91.3233% |
| Critical | 35% | 30% | 10.500% | 99.9999% |

The fixed worn, damaged, and critical rows show why deterioration must create a credible reason to repair. A healthy row alone cannot predict completion for a whole voyage. Damage-driven crashes through Condition reaching zero are an additional path in the full model, while actual repairs can improve later exposure. The complete scenario plan is in `080_airship_validation_matrix.md`.

The conditional severity rows each sum to 1,000. The route timing target is 121 times two days, giving 242 days before additional delay or diversion travel.
