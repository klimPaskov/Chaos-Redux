# Event 021 SPN Parent Probability Diagnostic

Date: 2026-09-01

Scope: SPN-01 through SPN-05 against the three current Evolution II external-action decisions.

Classification: parent-run current-source MCP diagnostic. This is not the required independent `chaosx_ai_probability_auditor` certificate and does not claim a normalized action-selection probability because the installed decision adapter is score-only.

## Source surface

The inspected candidate pool is `event021_support_government`, `event021_support_opposition`, and `event021_offer_mediation` from `common/decisions/021_random_civil_war_decisions.txt`.

All three start at `constant:event021_ai.base_action = 1`. The two armed-support actions multiply by `priority_major = 1.5` for the opportunistic-sponsor profile and by `discourage_repression = 0.75` for the mediator profile. Mediation multiplies by `priority_major = 1.5` for the mediator profile and by `discourage_concession = 0.75` for the opportunistic-sponsor profile.

The score adapter does not normalize decision scores into action probabilities. Validity comes from the source visibility, availability, resource, one-action, and target-survival gates. The named MCP fixtures declare those source gates explicitly: a valid action uses the declared hidden-trigger scope; an invalid action receives an exact false candidate override. False overrides were used only for invalid candidates, so they do not override the profile modifiers on eligible candidates.

The source inspection completed with three candidates, zero unresolved inputs, source revision `21666e64d1d772ede92e2b9b8595ce770ca7b5049cb21468d3aa2ae2ee5bd2c7`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81dcd0673b248387b62e374c41210c5db3354d5cd2eb9a263c7441a3bbe4b433/37f7746cff00e9a270ab5161b30584a39b271c43f63bac31d9d7feff1f3a2076/probability-inspect-b012bf7ee578.json`.

## Named evaluation

The five-scenario evaluation completed with analysis `probability-b5163d0f1c04bd490bff6dcc`, scenario hash `315c23693b64d7443f02aab3ce3b439c1742d941ff59b2dd30f5ff4148108435`, 15 candidate rows, zero unresolved inputs, and zero diagnostics.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa33ec717bf707f57688d565e00fa118951e6d82cbded06efa8afa8b1614b102/3b70efca158195ff62b13d0d9f11ca20f119c3154702d7e758e0c8f5260f9752/probability-b5163d0f1c04bd490bff6dcc.json`

| Fixture | Government support | Opposition support | Mediation | Result |
| --- | --- | --- | --- | --- |
| SPN-01 rich neutral major, one aligned viable side | 1.5, eligible, rank 1 | 0, ineligible | 0.75, eligible, rank 2 | Moderate aligned support leads; the invalid rival side is exact zero. |
| SPN-02 desperate war and inadequate equipment | 0, ineligible | 0, ineligible | 0, ineligible | Resource and action gates suppress every commitment. |
| SPN-03 rival sponsors and two viable sides | 1.5, eligible, rank 1 | 1.5, eligible, rank 2 | 0.75, eligible, rank 3 | Both viable sides retain equal competitive support scores. The source one-action receipt bounds each exposed sponsor's commitment. |
| SPN-04 no viable administration or survival path | 0, ineligible | 0, ineligible | 1, eligible, rank 1 | Armed support is exact zero while non-military mediation remains possible. |
| SPN-05 neutral mediator | 0.75, eligible, rank 2 | 0.75, eligible, rank 3 | 1.5, eligible, rank 1 | Military support is reduced and mediation leads by two to one. |

The numeric ranks in tied cases follow deterministic report ordering and do not mean one equal-score armed side is preferred over the other.

## Source gate boundary

`event021_country_can_manage_exposure` requires a normal human exposed neighbor, a live source crisis, and no terminal or settled phase. The two support decisions additionally require their corresponding government or opposition target-valid trigger, sufficient resources, and no `event021_neighbor_action_used` flag. Each completed support or mediation action sets `event021_neighbor_action_used`, while support writes a bounded 120-day sponsor commitment and matching recipient evidence. These lifecycle conditions are source evidence, not normalized probabilities.

The current adapter result supports the named willingness relationships but does not prove that HOI4 chooses among all visible decisions as one categorical pool. It also does not substitute for a live commitment lifecycle sequence.

## Remaining gate

An independent `chaosx_ai_probability_auditor` certificate remains required. No gameplay source was changed during this SPN diagnostic, so no new owner patch or before/after compare was created for this family. The historical pre-change audit remains the baseline record that sponsor roles and support scores were absent before implementation.
