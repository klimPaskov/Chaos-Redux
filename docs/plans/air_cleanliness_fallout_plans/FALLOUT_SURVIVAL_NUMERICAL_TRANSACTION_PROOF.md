# Fallout survival numerical transaction proof

## Verdict

The accepted nine-resource opening ledger has an implemented numerical producer and an exact replay transaction. It remains transition owned and dormant behind the existing successor-allocation barrier. The scheduler activation flags remain unset and no living-world event block is added by this tranche.

The same tranche makes immediate Fallout population loss deterministic by grade at 90, 91, 92, 93, 94, and 95 percent. The mutation preserves one person in every nonempty state, observes the exact population delta, and sends only that observed delta to the shared Deaths accounting path.

## Source files

- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/script_constants/fallout_world_end_constants.txt`
- `common/scripted_effects/fallout_survival_ledger_effects.txt`
- `common/scripted_triggers/fallout_survival_ledger_triggers.txt`
- `common/scripted_effects/fallout_world_end_effects.txt`
- `common/scripted_triggers/fallout_world_end_triggers.txt`

## Frozen numerical inputs

World transition schema 12 freezes the accepted specialty inputs in the same snapshot generation as the other state evidence. These include naval bases, radar, synthetic refineries, fuel silos, three dam families, three reactor families, and coal. The permanent building-loss receipt also records post-rewrite non-damaged infrastructure, civilian factories, military factories, air bases, and dockyards.

The state producer reads only frozen or durable transition receipts. It does not read later ownership, construction, repairs, deposits, Air Winter changes, or live state category. The frozen state-owner pointer selects all and only the states assigned to each successor.

## Numerical transaction

`fallout_commit_survival_ledger_numerical_transaction` is the sole producer and sole setter of `fallout_survival_ledger_ready`.

1. Require survivor allocation, current player planning, current successor allocation, current survival identity, no transition error, no player commit, and no ready ledger.
2. Set `fallout_survival_ledger_building`.
3. Clear only the uncommitted numerical payload.
4. Build every state row in stable ledger order.
5. Recompute every state row into separate replay arrays.
6. Build every country row from frozen ownership and unrounded state numerators.
7. Recompute every country row into separate replay arrays.
8. Record the numerical date and arithmetic day.
9. Require the global precommit proof across every frozen state and country.
10. Clear the building flag.
11. Set `fallout_survival_ledger_ready` as the final success write.

Failure clears every provisional numerical row, preserves the accepted identity payload, records one `survival_ledger_incomplete` error, and leaves ready absent. The numerical recovery helper owns only that exact one-error signature and retries through the ordinary coordinator.

## Row proof

State arrays contain ten entries in the fixed resource order. Index 0 is zero. Indexes 1 through 9 require denominator 100, numerator 0 through 10,000, and final share 0 through 100. Produced Air Winter rows replay the complete formula. Not-applicable Air Winter rows replay typed zero numerators and shares and remain excluded from country aggregation.

Country arrays contain the same ten resource identities. The durable row proves exact replay mirrors for raw numerator, raw denominator, immutable initial, population weight sum, weighted score sum, and hub score. It proves the accepted static bounds. The precommit proof additionally requires every mutable current value to equal its immutable initial value. After global commit, current may change within 0 through 100 while raw and initial values remain fixed.

The installed map count remains 1,081 states. With the accepted weight cap of 8, the static accumulator limits are 8,648 weight points and 864,800 weighted score points. State and country raw numerators remain bounded at 10,000.

## Population transaction proof

`fallout_apply_state_population_loss` freezes `fallout_population_before_loss_k` from the live pre-mutation state and derives the people count from that receipt. The durable trigger binds the receipt back to the pretransition population. It also proves:

- requested loss uses the grade constant from 90 through 95 percent
- committed loss does not exceed the request or the live amount above the one-person floor
- replayed pre-loss people equal the original people receipt
- post-loss people plus observed loss equal pre-loss people
- every nonempty state retains at least one person
- an empty state remains empty and records zero loss
- Deaths receives exactly the observed delta with population mutation disabled

The percentage calculation applies the `0.01` scale before multiplying by the stored integer grade percentage. The largest installed state population is 45,365,364. Scaling first produces an intermediate value of 453,653.64 and a 95 percent request of 43,097,095.8 before final rounding. Reversing those operations would create a 4,309,709,580 intermediate value, which exceeds the signed 32-bit whole-number range used by engine fixed-point arithmetic. The implemented order keeps the installed-map population path within that range while preserving the 90 through 95 percentage receipt.

The issue flag is written before the single population mutation. Recovery can observe and reconcile that transaction but cannot apply it again.

## Static scenario inputs

The reviewed scenarios below use normalized inputs after the accepted common-signal formulas. Abbreviations are Food Reserve `FR`, rural identity `RI`, port `PT`, Reclamation `RQ`, Access `AC`, Water Security `WS`, Shelter Capacity `SH`, logistics `LG`, Adaptation `AD`, urban identity `UI`, industry `IN`, Recovery `RV`, salvage `SV`, material `MT`, fuel source `FS`, power source `PS`, communications `CM`, and administration `AM`.

| Profile | FR | RI | PT | RQ | AC | WS | SH | LG | AD |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| R rural refuge | 85 | 90 | 0 | 60 | 80 | 75 | 70 | 60 | 45 |
| D dead industrial city | 20 | 20 | 0 | 15 | 30 | 25 | 25 | 20 | 35 |
| T ordinary town | 55 | 65 | 0 | 40 | 55 | 55 | 50 | 40 | 40 |
| F isolated fuel hub | 20 | 30 | 0 | 20 | 45 | 35 | 30 | 20 | 35 |
| P power keep | 35 | 45 | 0 | 30 | 60 | 65 | 60 | 40 | 50 |
| M maritime remnant | 60 | 65 | 85 | 45 | 70 | 60 | 55 | 50 | 50 |
| A altered enclave | 25 | 30 | 0 | 70 | 20 | 30 | 45 | 20 | 85 |
| N no specialty assets | 45 | 65 | 0 | 35 | 55 | 50 | 45 | 40 | 35 |

| Profile | UI | IN | RV | SV | MT | FS | PS | CM | AM | Population weight |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| R rural refuge | 20 | 20 | 35 | 15 | 40 | 20 | 30 | 20 | 10 | 0.250 |
| D dead industrial city | 85 | 70 | 25 | 90 | 80 | 15 | 25 | 45 | 42.5 | 0.800 |
| T ordinary town | 40 | 30 | 35 | 35 | 35 | 10 | 20 | 30 | 20 | 0.350 |
| F isolated fuel hub | 70 | 40 | 25 | 60 | 45 | 100 | 35 | 25 | 35 | 0.080 |
| P power keep | 55 | 50 | 45 | 35 | 45 | 15 | 100 | 55 | 27.5 | 0.120 |
| M maritime remnant | 45 | 35 | 40 | 30 | 35 | 35 | 25 | 65 | 22.5 | 0.220 |
| A altered enclave | 70 | 25 | 30 | 75 | 50 | 10 | 20 | 15 | 35 | 0.090 |
| N no specialty assets | 40 | 30 | 30 | 25 | 20 | 0 | 9 | 20 | 20 | 0.180 |

## Static state results

Each cell is `raw numerator / rounded state score`.

| Profile | Food | Water | Medicine | Scrap | Fuel | Power | Filters | Shelter | Recognition |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| R | 7425 / 74 | 6950 / 70 | 3575 / 36 | 3725 / 37 | 3700 / 37 | 4000 / 40 | 4675 / 47 | 6200 / 62 | 2575 / 26 |
| D | 1900 / 19 | 2575 / 26 | 5350 / 54 | 6900 / 69 | 2650 / 27 | 3400 / 34 | 4425 / 44 | 3175 / 32 | 4587.5 / 46 |
| T | 5000 / 50 | 5050 / 51 | 3875 / 39 | 3900 / 39 | 2575 / 26 | 3025 / 30 | 4025 / 40 | 4700 / 47 | 3225 / 32 |
| F | 2375 / 24 | 3300 / 33 | 4450 / 45 | 4925 / 49 | 6675 / 67 | 3525 / 35 | 3600 / 36 | 3450 / 35 | 3625 / 36 |
| P | 3675 / 37 | 5850 / 59 | 5175 / 52 | 4625 / 46 | 3200 / 32 | 7500 / 75 | 5150 / 52 | 5550 / 56 | 4712.5 / 47 |
| M | 6350 / 64 | 5775 / 58 | 4600 / 46 | 4200 / 42 | 4325 / 43 | 3750 / 38 | 4750 / 48 | 5425 / 54 | 4812.5 / 48 |
| A | 2725 / 27 | 3525 / 35 | 4550 / 46 | 4625 / 46 | 1575 / 16 | 2100 / 21 | 4175 / 42 | 4525 / 45 | 3100 / 31 |
| N | 4500 / 45 | 4675 / 47 | 3700 / 37 | 3250 / 33 | 2075 / 21 | 2475 / 25 | 3800 / 38 | 4375 / 44 | 2800 / 28 |

## Static country scenarios

The seven required cases use these frozen memberships.

| Scenario | Frozen state profiles | State count | Archetype adjustment |
| --- | --- | ---: | ---: |
| Small one-state successor | R x1 | 1 | Food Compact +5 Recognition |
| Large successor | R x5, D x3, T x2, F x1, P x1 | 12 | Continuity Government +15 Recognition |
| Maritime successor | M x3 | 3 | Maritime Remnant +10 Recognition |
| Altered successor | A x2 | 2 | Mutant Polity -20 Recognition |
| Isolated fuel hub | F x1, R x5 | 6 | Warlord Command -15 Recognition |
| No specialty assets | N x4 | 4 | Quarantine State 0 Recognition |
| Tied power hubs | P x2, R x2 | 4 | Technate +5 Recognition |

Country columns are population `weight sum`, unrounded `weighted score sum`, `coverage`, strongest unrounded `hub`, blended raw `numerator`, `denominator`, rounded physical `base`, Recognition `adjustment`, immutable `initial`, and opening mutable `current`.

### Small one-state successor

| Resource | Weight sum | Weighted sum | Coverage | Hub | Numerator | Denominator | Base | Adjustment | Initial | Current |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Food | 0.250 | 18.563 | 74.250 | 74.250 | 7425.000 | 100 | 74 | 0 | 74 | 74 |
| Clean water | 0.250 | 17.375 | 69.500 | 69.500 | 6950.000 | 100 | 70 | 0 | 70 | 70 |
| Medicine | 0.250 | 8.938 | 35.750 | 35.750 | 3575.000 | 100 | 36 | 0 | 36 | 36 |
| Scrap | 0.250 | 9.313 | 37.250 | 37.250 | 3725.000 | 100 | 37 | 0 | 37 | 37 |
| Fuel | 0.250 | 9.250 | 37.000 | 37.000 | 3700.000 | 100 | 37 | 0 | 37 | 37 |
| Power | 0.250 | 10.000 | 40.000 | 40.000 | 4000.000 | 100 | 40 | 0 | 40 | 40 |
| Filters | 0.250 | 11.688 | 46.750 | 46.750 | 4675.000 | 100 | 47 | 0 | 47 | 47 |
| Shelter | 0.250 | 15.500 | 62.000 | 62.000 | 6200.000 | 100 | 62 | 0 | 62 | 62 |
| Recognition | 0.250 | 6.438 | 25.750 | 25.750 | 2575.000 | 100 | 26 | 5 | 31 | 31 |

### Large twelve-state successor

| Resource | Weight sum | Weighted sum | Coverage | Hub | Numerator | Denominator | Base | Adjustment | Initial | Current |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Food | 4.550 | 179.722 | 39.499 | 74.250 | 4297.451 | 100 | 43 | 0 | 43 | 43 |
| Clean water | 4.550 | 193.685 | 42.568 | 69.500 | 4526.132 | 100 | 45 | 0 | 45 | 45 |
| Medicine | 4.550 | 209.983 | 46.150 | 53.500 | 4688.500 | 100 | 47 | 0 | 47 | 47 |
| Scrap | 4.550 | 248.953 | 54.715 | 69.000 | 5828.613 | 100 | 58 | 0 | 58 | 58 |
| Fuel | 4.550 | 137.055 | 30.122 | 66.750 | 3927.898 | 100 | 39 | 0 | 39 | 39 |
| Power | 4.550 | 164.595 | 36.175 | 75.000 | 4588.104 | 100 | 46 | 0 | 46 | 46 |
| Filters | 4.550 | 201.873 | 44.368 | 51.500 | 4508.082 | 100 | 45 | 0 | 45 | 45 |
| Shelter | 4.550 | 196.020 | 43.081 | 62.000 | 4497.319 | 100 | 45 | 0 | 45 | 45 |
| Recognition | 4.550 | 173.418 | 38.114 | 47.125 | 4081.712 | 100 | 41 | 15 | 56 | 56 |

### Maritime successor

| Resource | Weight sum | Weighted sum | Coverage | Hub | Numerator | Denominator | Base | Adjustment | Initial | Current |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Food | 0.660 | 41.910 | 63.500 | 63.500 | 6350.000 | 100 | 64 | 0 | 64 | 64 |
| Clean water | 0.660 | 38.115 | 57.750 | 57.750 | 5775.000 | 100 | 58 | 0 | 58 | 58 |
| Medicine | 0.660 | 30.360 | 46.000 | 46.000 | 4600.000 | 100 | 46 | 0 | 46 | 46 |
| Scrap | 0.660 | 27.720 | 42.000 | 42.000 | 4200.000 | 100 | 42 | 0 | 42 | 42 |
| Fuel | 0.660 | 28.545 | 43.250 | 43.250 | 4325.000 | 100 | 43 | 0 | 43 | 43 |
| Power | 0.660 | 24.750 | 37.500 | 37.500 | 3750.000 | 100 | 38 | 0 | 38 | 38 |
| Filters | 0.660 | 31.350 | 47.500 | 47.500 | 4750.000 | 100 | 48 | 0 | 48 | 48 |
| Shelter | 0.660 | 35.805 | 54.250 | 54.250 | 5425.000 | 100 | 54 | 0 | 54 | 54 |
| Recognition | 0.660 | 31.763 | 48.125 | 48.125 | 4812.500 | 100 | 48 | 10 | 58 | 58 |

### Altered successor

| Resource | Weight sum | Weighted sum | Coverage | Hub | Numerator | Denominator | Base | Adjustment | Initial | Current |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Food | 0.180 | 4.905 | 27.250 | 27.250 | 2725.000 | 100 | 27 | 0 | 27 | 27 |
| Clean water | 0.180 | 6.345 | 35.250 | 35.250 | 3525.000 | 100 | 35 | 0 | 35 | 35 |
| Medicine | 0.180 | 8.190 | 45.500 | 45.500 | 4550.000 | 100 | 46 | 0 | 46 | 46 |
| Scrap | 0.180 | 8.325 | 46.250 | 46.250 | 4625.000 | 100 | 46 | 0 | 46 | 46 |
| Fuel | 0.180 | 2.835 | 15.750 | 15.750 | 1575.000 | 100 | 16 | 0 | 16 | 16 |
| Power | 0.180 | 3.780 | 21.000 | 21.000 | 2100.000 | 100 | 21 | 0 | 21 | 21 |
| Filters | 0.180 | 7.515 | 41.750 | 41.750 | 4175.000 | 100 | 42 | 0 | 42 | 42 |
| Shelter | 0.180 | 8.145 | 45.250 | 45.250 | 4525.000 | 100 | 45 | 0 | 45 | 45 |
| Recognition | 0.180 | 5.580 | 31.000 | 31.000 | 3100.000 | 100 | 31 | -20 | 11 | 11 |

### Isolated fuel hub

| Resource | Weight sum | Weighted sum | Coverage | Hub | Numerator | Denominator | Base | Adjustment | Initial | Current |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Food | 1.330 | 94.713 | 71.212 | 74.250 | 7151.617 | 100 | 72 | 0 | 72 | 72 |
| Clean water | 1.330 | 89.515 | 67.305 | 69.500 | 6752.406 | 100 | 68 | 0 | 68 | 68 |
| Medicine | 1.330 | 48.248 | 36.276 | 44.500 | 3709.868 | 100 | 37 | 0 | 37 | 37 |
| Scrap | 1.330 | 50.502 | 37.972 | 49.250 | 4079.135 | 100 | 41 | 0 | 41 | 41 |
| Fuel | 1.330 | 51.590 | 38.789 | 66.750 | 4577.961 | 100 | 46 | 0 | 46 | 46 |
| Power | 1.330 | 52.820 | 39.714 | 40.000 | 3978.571 | 100 | 40 | 0 | 40 | 40 |
| Filters | 1.330 | 61.318 | 46.103 | 46.750 | 4616.805 | 100 | 46 | 0 | 46 | 46 |
| Shelter | 1.330 | 80.260 | 60.346 | 62.000 | 6051.128 | 100 | 61 | 0 | 61 | 61 |
| Recognition | 1.330 | 35.087 | 26.382 | 36.250 | 2934.211 | 100 | 29 | -15 | 14 | 14 |

### No specialty assets

| Resource | Weight sum | Weighted sum | Coverage | Hub | Numerator | Denominator | Base | Adjustment | Initial | Current |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Food | 0.720 | 32.400 | 45.000 | 45.000 | 4500.000 | 100 | 45 | 0 | 45 | 45 |
| Clean water | 0.720 | 33.660 | 46.750 | 46.750 | 4675.000 | 100 | 47 | 0 | 47 | 47 |
| Medicine | 0.720 | 26.640 | 37.000 | 37.000 | 3700.000 | 100 | 37 | 0 | 37 | 37 |
| Scrap | 0.720 | 23.400 | 32.500 | 32.500 | 3250.000 | 100 | 33 | 0 | 33 | 33 |
| Fuel | 0.720 | 14.940 | 20.750 | 20.750 | 2075.000 | 100 | 21 | 0 | 21 | 21 |
| Power | 0.720 | 17.820 | 24.750 | 24.750 | 2475.000 | 100 | 25 | 0 | 25 | 25 |
| Filters | 0.720 | 27.360 | 38.000 | 38.000 | 3800.000 | 100 | 38 | 0 | 38 | 38 |
| Shelter | 0.720 | 31.500 | 43.750 | 43.750 | 4375.000 | 100 | 44 | 0 | 44 | 44 |
| Recognition | 0.720 | 20.160 | 28.000 | 28.000 | 2800.000 | 100 | 28 | 0 | 28 | 28 |

### Tied power hubs

| Resource | Weight sum | Weighted sum | Coverage | Hub | Numerator | Denominator | Base | Adjustment | Initial | Current |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Food | 0.740 | 45.945 | 62.088 | 74.250 | 6330.405 | 100 | 63 | 0 | 63 | 63 |
| Clean water | 0.740 | 48.790 | 65.932 | 69.500 | 6628.919 | 100 | 66 | 0 | 66 | 66 |
| Medicine | 0.740 | 30.295 | 40.939 | 51.750 | 4202.027 | 100 | 42 | 0 | 42 | 42 |
| Scrap | 0.740 | 29.725 | 40.169 | 46.250 | 4168.919 | 100 | 42 | 0 | 42 | 42 |
| Fuel | 0.740 | 26.180 | 35.378 | 37.000 | 3578.378 | 100 | 36 | 0 | 36 | 36 |
| Power | 0.740 | 38.000 | 51.351 | 75.000 | 5726.351 | 100 | 57 | 0 | 57 | 57 |
| Filters | 0.740 | 35.735 | 48.291 | 51.500 | 4861.149 | 100 | 49 | 0 | 49 | 49 |
| Shelter | 0.740 | 44.320 | 59.892 | 62.000 | 6010.270 | 100 | 60 | 0 | 60 | 60 |
| Recognition | 0.740 | 24.185 | 32.682 | 47.125 | 3701.520 | 100 | 37 | 5 | 42 | 42 |

The tied-hub case has two power states at the same unrounded score of 75. The numeric maximum is identical regardless of iteration order. No hub identity is stored, so no false winner can affect gameplay.

## Engine-sensitive evidence

Primary installed documentation:

- `documentation/effects_documentation.md` for state and country variable arithmetic, clamp, round, arrays, `for_loop_effect`, and `for_each_scope_loop`
- `documentation/triggers_documentation.md` for exact variable comparisons, `all_of`, `all_of_scopes`, array value and index capture, and dynamic scope validation
- `documentation/dynamic_variables_documentation.md` for resources, total building levels, damaged building levels, and non-damaged building levels in state scope
- `documentation/script_concept_documentation.md` and `common/script_constants/documentation.md` for typed fixed-point constants and scope variables
- offline Data structures, Effects, Triggers, and Scopes wiki pages for arrays, temporary variables, and stored scope values

Vanilla precedents inspected were `events/AAT_Finland.txt` for stored-scope iteration, `events/BBA_ItaloEthiopianWar.txt` for variable rounding, and `events/GOE_Raj.txt` for ordered calculation, rounding, and clamping.

No Hearts of Iron IV run was performed. Immediate read visibility, fixed-point overflow behavior, save interruption recovery, and multiplayer observation remain runtime-sensitive and unobserved. The manual scenario remains inactive because exact runtime acceptance of the every-valid-province thermonuclear sweep is not proven.
