# The Empty Ward event addendum

## Review decision

Implement candidate 296 as a dormant Year 2 global-survival institution
tranche. It follows Fever Dormitory and School in the Vent Room without
duplicating their policy lanes. The ward is a physical memory of the epidemic,
so each choice changes what the country can use, remember, or reserve.

## Frozen inputs

| Input | Source | Use |
| --- | --- | --- |
| Medicine | `fallout_survival_current_entries^3` | Viability, eligibility, and costs |
| Shelter | `fallout_survival_current_entries^8` | Viability, eligibility, and reserve policy |
| Cohesion | `fallout_survival_cohesion_current` | Viability and veteran policy threshold |
| Recognition | `fallout_survival_current_entries^9` | Research and memorial thresholds |
| Generation count | `fallout_generation_change_count` | Eligibility, severity context, and viability |
| Ward capacity | `fallout_ward_296_capacity` | Durable institution reserve |
| Research | `fallout_ward_296_research` | Research clinic threshold and growth |
| Trust | `fallout_ward_296_trust` | Veteran policy threshold and durable institutional trust |
| Exposure | `fallout_ward_296_exposure` | Durable exposure pressure carried through result and callback |

## Authored policies

The veteran home gives injured crews a public recovery room. The research
clinic keeps fever records beside clean instruments. The memorial hall gives
families one room for names and grief. The reserved empty ward keeps beds ready
without claiming that unused capacity is already a social institution. Each
policy has distinct costs, result thresholds, resource deltas, memory flags,
and timed modifiers.

## Delayed transaction

The opening reserves one result after 35 days and one callback after 240 days.
Human visible cost is three for the opening and one for each delayed receipt.
Hidden AI pays zero visible cost while using the same branch, grading, result,
callback, history, and cleanup effects. Result failure uses Deaths at 0.1
percent. Callback failure uses Deaths at 0.05 percent. Cleanup cannot clear the
School memory and does not create scheduler activation.

## Review boundary

The chain remains dormant and uncounted until the accepted numerical contract
opens activation. Host authority, save recovery, multiplayer behavior, and
live Event Log delivery remain unobserved.
