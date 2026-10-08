# Event 012 Strength: Chaos scale

Acceptance basis: the full Gods goal requires Strength to derive from current Chaos, with Chaos supplying a limited share rather than replacing African capability.
Disposition: implemented source correction, with native numeric consumption and complete Strength acceptance remaining unverified.

## Finding and implementation

The shared Chaos meter uses tiers of 200 points, with its final tier beginning at `chaos_meter_tier_range.tier_final.min` (1000).
That final tier has no upper bound, and 1001 is its settings-display sentinel.
The previous Strength helper divided the raw meter by 1 before limiting the component to 100.
Its entire ten-point contribution therefore arrived at Chaos 100, halfway through the first tier.
The Evolution II and III bonuses also stopped affecting this component above that point.

`gods_of_africa_refresh_strength` divides the current meter by the shared final-tier endpoint and multiplies by the component maximum.
The existing Evolution II bonus of 15, Evolution III bonus of 25, component bounds and ten-percent weight follow that normalization.
The unused `gods_of_africa_strength.chaos_divisor` entry is removed.
The calculation uses shared tuning directly and introduces no public value or new periodic hook.

| Chaos, without evolution bonuses | Prior contribution to Strength | Normalized contribution |
| ---: | ---: | ---: |
| 100 | 10 | 1 |
| 200 | 10 | 2 |
| 400 | 10 | 4 |
| 600 | 10 | 6 |
| 800 | 10 | 8 |
| 1000 | 10 | 10 |

At Chaos 200, Evolution II produces a 35-point component and 3.5 points of Strength.
With both evolution bonuses, that component reaches 60 and supplies six Strength points.
Final-tier and above-final-tier inputs respect the same ten-point contribution budget.
These are component arithmetic results, with the other Strength components and smoothing outside the isolated model.
No punishment gate, demand price, doctrine modifier or willingness expression changes in this correction.

## Evidence

The immutable before and after manifests and source copies are in `012_gods_strength_chaos_2026-10-08_evidence/`.
The parent ran the updated existing response source model, with all 22 groups passing.
Its additional group executes the production component, evolution branches, bounds and weighted accumulation across 56 cases.
It covers every shared tier edge, the final-tier sentinel, an above-final-tier value and four evolution-flag combinations.
It also detects any unrelated owner-body or tuning change outside the accepted normalizer replacement and removed obsolete entry.
The result is `source_model_after.json` in that evidence directory.

The country-scope MCP snippet check returned `SCRIPT_CHECK_PARTIAL`, with ten supported commands and six unchecked native argument blocks.
`valid=null` and `parametersChecked=false` prevent treating that result as native arithmetic execution.
The documentation aggregate revision is `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The probability specialist owns the corresponding deterministic-sum adapter boundary and narrow before/after attempts in `012_gods_strength_chaos_probability_2026-10-08.md`.
No numeric AI probability or gameplay observation is inferred from the component model.

## References and scope

Installed `documentation/effects_documentation.md:3587–3594`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, was read through MCP for temporary-variable division.
The same installed file's multiplication and temporary-clamp sections at 5012–5024 and 2681–2694 were read locally.
Its clamp-variable section at 2695–2712 was read through MCP for the operation order and variable-valued bounds.
Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:715`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, was read through MCP for those bounds.
Vanilla `common/scripted_effects/USA_scripted_effects.txt:476–486` normalizes senator support by its total and scales the result for presentation, using the same temporary divide/multiply sequence.
The shared Chaos constants and existing repository consumers of the nested final-tier endpoint provide the meter-scale authority.

The changed source files are `common/scripted_effects/012_africa_gods_effects.txt`, `common/script_constants/012_africa_gods_constants.txt` and the existing `.tools/validation/test_012_gods_response_phases.js`.
The canonical Gods guide records the component scale.
No localisation, catalog, icon, image, focus, AI profile or event registration is changed.
No simplification is adopted.
Direct territorial-control and relative-world-power coverage remain separate parent audit questions, so this correction does not prove the full Strength contract or full Gods completion.
