# Event 24 AI and probability audit handoff

Current-state disposition, 6 October: superseded for current completion claims by `../takeover_status_2026-10-06.md`.
The inherited reconciliation below is retained as historical evidence for its dated sources and artifacts.
Its old counts, pending-audit notices, and current-revision claims do not certify the finishing-pass source.

## Scope

The probability role reviewed opening `ai_chance`, route selection, ordinary actions, evolution openings, emergency behavior, and the named scenario matrix.

## Named scenarios

The final matrix is `P24_FINAL_OPENING_MATRIX` with `P24-O1` stable peace, `P24-O2` low-experience domestic pressure, `P24-O3` wartime high Chaos, and `P24-O4` severe instability with supply and core-loss crisis flags.

## Findings and parent integration

Route-specific weights remain explicit for the three openings and action routes. The maximum-risk route is suppressed by near capitulation, broken supply, severe instability, and severe campaign crisis checks.

The emergency matrix showed the controlled route dominant in `P24-O4`, and the commercial route factor was reduced to zero for the emergency crisis branch so it cannot outrank the bounded response.

## Validation

The fresh `hoi4.probability_inspect` call used the `event_option_ai_chance` adapter on `chaosx.nr24.2` and returned a complete three-candidate pool with four required inputs and zero unresolved inspect items. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76d77d048417a1b186b55db0e5a9240b0b068fe76b4280e386dda729f573f8e2/fd8692e72d53bac84a8ff7a0d79a4c8dd0b50b122c09849a4eb05971f01163c7/probability-inspect-dbb4a64f206f.json`.

The fresh named evaluation completed all four `P24_FINAL_OPENING_MATRIX` scenarios. It returned 12 candidate rows, 12 bounded unresolved adapter inputs, and one diagnostic stating that the commercial opening's supply modifier was inactive in the supplied matrix. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f67017802db38f3033f13c7da9155822c60531c6a14b23fded978d1f2370fda7/2c77c3ee1582b4997563595f327f82e7b135bd12bbad5dfe8fcacd85f7952c09/probability-cb60cb3ec67ba407e5c9dec4.json`.

A bounded safety sweep across Chaos, stability, surrender progress, and army experience completed six sweep points. It preserved explicit uncertainty and the same single inactive-supply diagnostic. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de36369c6bc9b9692009da00d1da9ff7b81ce9c37e16ce3d33a4cc1ed0dc0ab4/ff3713a0207fb53c8f9ff80b835681b7bf8f7c29fb1cd34ad72ba9e411943c86/probability-152115d6d981a0053acb5a28.json`.

The current-source control comparison used the same source descriptor on both sides and the same four named scenarios. It completed with zero comparison changes, while retaining the 12 bounded unresolved inputs and one diagnostic. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd641ce6fdfc359ab69849902e57b21639860a19b7838aaad5644cf080b50bd5/967b0b385acb585dbebb96434cf75b770e95c1eaf68a8ba734b84368f2bda994/probability-85b8428ca2542bb68c3ae99c.json`.

The normal decision-category inspect was also rerun. The adapter found the category-shaped source but could project only one decision candidate and left 17 inputs unresolved. The source decision map remains audited independently because the adapter does not expand this normal category into its complete action pool.

## Remaining risks

The probability artifacts are bounded adapter projections rather than a native engine run. The named evaluation, safety sweep, and current-source control comparison are complete, but the decision adapter projection remains incomplete and cannot certify the full category-shaped action pool. A historical before-and-after comparison against the earlier weighted source is not claimed because the adapter has no valid historical workspace revision descriptor.
