# Event 021 REC Parent Pre/Post Probability Evidence

Date: 2026-09-01

Scope: REC-01 through REC-06 plus one supplementary unresolved-sponsor fixture.

Classification: parent-run MCP diagnostic and owner patch evidence. This is not the required independent `chaosx_ai_probability_auditor` certificate.

## Source defect

The accepted recurrence matrix requires broken settlement guarantees to increase recurrence strongly and unresolved foreign sponsorship to increase recurrence. The pre-change `event021_prepare_recurrence` score included fracture pressure, recurrence memory, failed settlement, authority collapse, and good-settlement relief, but ignored `random_civil_war_settlement_violation`, `random_civil_war_settlement_obligation_breached`, `random_civil_war_sponsor_evidence_active`, and `random_civil_war_sponsor_commitment_active`.

The exact pre-change REC-05 fixture therefore produced recurrence score zero and remained ineligible despite a broken guarantee.

## Owner patch

`common/script_constants/021_random_civil_war_constants.txt` now defines `settlement_violation_pressure = 25` and `foreign_sponsor_pressure = 10` under `random_civil_war_settlement_tuning`.

`common/scripted_effects/021_random_civil_war_effects.txt::event021_prepare_recurrence` now adds the settlement-violation contribution once when either violation flag is present and adds the sponsor contribution once when either sponsor-dependence flag is present. Paired flags are OR-gated so the same state cannot be counted twice.

`docs/events/021_random_civil_war/overview.md` now records broken obligations and unresolved sponsor dependence among the recurrence inputs.

## Pre-change evaluation

The pre-change analysis is `probability-8a7fc81c4c46099c41d31e98` with scenario hash `0988869164a35d81c5550a22cdf5bedf24db78594e8c50dd0926abd2c30d37c7` and zero unresolved inputs.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ac464e59babe597ec77c48d3f502887722391f8d67be46bdbc39dfac724b697/4d9692c1f3e5046cb4cd6f6275d67c6c4bc96893302439df99103f99d4ab1869/probability-8a7fc81c4c46099c41d31e98.json`

The matching inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d61b77c4c372208d66b34796e8d35bbc7918c80fb076d73439cfedaabdc8519/0a33d2dbbd5f19af81d867c242e1664de1b161b634f62d4e4a671638348c7fd2/probability-inspect-f0b9ebc1a538.json`.

| Fixture | Pre-change score | Eligibility |
| --- | ---: | --- |
| REC-01 durable negotiated peace | 0 | Ineligible |
| REC-02 harsh settlement with low authority | 100 | Eligible |
| REC-03 successor grace active | 0 | Ineligible |
| REC-04 partition or armistice | 55 | Eligible |
| REC-05 broken guarantee | 0 | Ineligible; demonstrated defect |
| REC-06 actual nonhuman | 0 | Ineligible |

## Post-change evaluation

The post-change analysis is `probability-1c92baf1311590250c04dfce` with scenario hash `0a09d20451f59208dfa5d00e9bfbe1ea5b31bd370ccd4cf841f6191da750385b` and zero unresolved inputs.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c57cd24c2e0bb5913d8007c005bdac0738f6a90c3dcc49b5dc4410bc27becf7/903c2dcfe4453b749b702ac533fbbf0a2ea76b14e9c73c9cec80e1b531a09e94/probability-1c92baf1311590250c04dfce.json`

The matching inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/880299365c7da536f21ca5da6bd4c6187fa2f199cf6d13a1600600e734dde088/0988157069ca50ad39570642246bf696662829928d7584d7ed9e8c9ba2bc223e/probability-inspect-91e9f207787d.json`.

| Fixture | Post-change score | Eligibility |
| --- | ---: | --- |
| REC-01 durable negotiated peace | 0 | Ineligible |
| REC-02 harsh settlement with low authority | 100 | Eligible |
| REC-03 successor grace active | 0 | Ineligible |
| REC-04 partition or armistice | 55 | Eligible |
| REC-05 broken guarantee | 60 | Eligible |
| REC-06 actual nonhuman | 0 | Ineligible |
| REC-SPONSOR-DEPENDENCE | 45 | Eligible |

## Same-scenario comparison

The raw-score before/after comparison uses identical seven-fixture scenario state and isolates the two added contributions. Threshold eligibility is proven by the post-change evaluation because eligibility itself is derived from the resulting score and cannot be held identical across the changed REC-05 fixture.

The comparison analysis is `probability-2e2594e85891304baa026a5d` with scenario hash `c1241a9c570160287f8f3f6f5b62881069470849ff15be465779a41b19c102c0`, zero unresolved inputs, two attributed changes, and no regressions.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f45b71ea36b4df7367e1bb10d13fe6472bc0df2a6d0b073049c109f32727e63/a667c4d366333c474db9505d1be778daec7e5630fdf23022c193feeb9e72a076/probability-2e2594e85891304baa026a5d.json`

The only score changes are REC-05 from 35 to 60, a delta of 25, and REC-SPONSOR-DEPENDENCE from 35 to 45, a delta of 10. All other fixtures are unchanged. Probability and rank deltas remain zero because each diagnostic scenario contains one abstract recurrence candidate and measures its raw score and gate rather than a normalized multi-country draw.

The MCP dominance warnings are expected for these one-candidate fixtures and do not indicate a competing route imbalance.

## Remaining gate

An independent `chaosx_ai_probability_auditor` must reproduce or review the post-change evaluation and same-scenario comparison before the repository requirement for specialist probability certification is satisfied. The complete Event 021 named probability matrix also remains open.
