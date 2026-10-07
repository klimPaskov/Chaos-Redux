# Combined CBRN reconnaissance allocation

Acceptance basis: the user-approved overhaul requires a combined +35% dedicated-unit static budget, and the current parent retains the earlier documented interpretation that reconnaissance utility belongs within that allowance.
The user did not separately prescribe a reconnaissance formula or numeric ceiling by name.
The parent accepts this bounded allocation within the combined-budget scope while preserving the 25% Integrated Command adoption reward accepted in the [doctrine correction](2026-10-07_doctrine_reward_mastery.md).
The [source review](../../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-07_reconnaissance_budget_review.md) records the acceptance boundary and legal same-command composition.

The previous technology-only calculation omitted the doctrine and both HQ factors.
With one Operations and one Medical section, the country/HQ factors alone exceeded the interpreted budget before weather technologies were counted.
The accepted allocation is:

| Source | Allocation |
| --- | ---: |
| Integrated Command adoption | 25% reconnaissance |
| Operations HQ | 4% reconnaissance; its 5% planning bonus is retained |
| Medical HQ | 2% reconnaissance; both 30% wound/sickness reductions are retained |
| Three hidden weather technologies | `recon` values 0.01, 0.02 and 0.03 |

This reduces the secondary Operations HQ factor from 15% to 4% and Medical HQ from 10% to 2%.
The weather total falls from 1.20 to 0.06 under the existing flat-point interpretation, a 95% reduction of that stat grant.
The doctrine's visible adoption payoff remains 25%.
HQ abilities, identities, costs, manpower, equipment, training, supply, unlock chronology and all other fields retain their authored behavior.
The visible instrument progression and its equipment unlocks still grant the same three hidden technologies.
No policy, AI weight, mastery contributor, raid, event or recurring hook changes.

On the Recon Detachment's base four, the complete flat-point source model gives `1.015 * 1.25 * 1.04 * 1.02 = 1.34589`.
Normalizing each weather point grant independently gives `1.0025 * 1.005 * 1.0075 * 1.25 * 1.04 * 1.02 = 1.3459812868125`.
Field Medical receives no weather-category grant; the independent country/HQ factor is 1.326.
These calculations reserve one equipped instance of each relevant section and retain ordinary vanilla and unrelated event progression equally on both sides.

Disposition: implemented in source, with native field semantics and accumulation unresolved.
The point interpretation follows the existing owner model and installed recon-technology precedents, while the generic offline technology prose does not enumerate a recon exception to multiplicative subunit bonuses.
If the native field is fractional instead, the candidate's alternate source calculation exceeds 35%; no native cap pass is claimed.
The [source checks](../../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-07_reconnaissance_budget_source_checks.md) retain that countermodel, preserved-field proof and exact baseline comparisons.
