
# Event 013 effects and tuning matrix

This file is a design tuning map. It names values and relationships that should be centralized in script constants or documented helper tuning. It does not require exact literals.

## Severity bands

| Band | Use | Damage direction | Dynamic death-rate direction | Recovery |
| --- | --- | --- | --- | --- |
| Light | Hail, small storm, minor flood, weak sandstorm. | One or a few state assets, mostly temporary. | Very low state-population percentage. Absolute deaths scale with the affected state's population. | One recovery action can usually clear it. |
| Moderate | Baseline flood, wildfire, blizzard, earthquake in less dense state. | Several infrastructure or building hits. | Low to medium state-population percentage. Dense states can still suffer meaningful absolute deaths. | Decision plus mission if neglected. |
| Severe | Major cyclone, urban earthquake, tsunami, regional flood. | Many buildings or key strategic assets. | Medium to high state-population percentage. Dense urban or coastal states can lose hundreds of thousands or more. | Multiple recovery tasks and possible follow-up. |
| Extreme | Evolution III meteor, massive quake-wave, massive volcano, moving storm corridor. | Multi-state damage and strong state modifiers. | High to severe state-population percentage. Multi-million deaths must be possible in dense states or dense regional chains. | Regional recovery, follow-up risk, newsworthy. |

## Dynamic scalar factors

| Factor | Should increase severity | Should reduce severity |
| --- | --- | --- |
| Chaos tier | Higher tier raises incident count and severity ceiling. | Calm tier keeps sequence small. |
| Preparedness | Lack of warning or ignored warnings worsens loss. | Warning decisions and recovery investment reduce loss. |
| State population | Multiplies the final loss rate into higher absolute deaths. | Low population naturally lowers absolute deaths through the same percentage formula. |
| Building density | Raises building damage potential. | Low building count lowers industrial damage. |
| War state | Worsens evacuation and supply aftermath. | Peace improves recovery capacity. |
| Infrastructure | Dense infrastructure can take damage, but helps evacuation if intact. | Poor infrastructure lowers asset damage ceiling but worsens delayed deaths. |
| Prior aftermath | Same family aftermath makes chain more likely. | Cleared recovery lowers chain weights. |
| Manual scenario intensity | Higher intensity raises incident count and abnormal access. | Low intensity uses local incidents only. |


## Dynamic percentage death formula

The implementation should centralize death math in a helper that works from rates. Suggested helper shape:

```text
base_family_loss_rate
* severity_multiplier
* evolution_multiplier
* density_multiplier
* war_and_stability_multiplier
* aftermath_multiplier
* preparedness_reduction
= final_dynamic_loss_rate

current_state_population * final_dynamic_loss_rate = civilian_deaths
```

Implementation notes:

- Do not use fixed casualty amounts such as `5,000 deaths from flood` or `100,000 deaths from earthquake`.
- Do not give each state a fixed death value.
- Do not use an absolute death cap as the main safety control. Cap the loss rate instead.
- Apply the formula separately to every affected state, then sum the sequence total for the death log and event details.
- Ongoing famine, exposure, ashfall, water, refugee, and disease-adjacent natural aftermath deaths should use the same rate model against current state population.
- Severe Evolution III disasters must be able to reach multi-million totals when dense states or several dense neighboring states are hit.

## Suggested helper families

| Helper purpose | Scope | Inputs | Outputs | Side effects |
| --- | --- | --- | --- | --- |
| Build disaster sequence | Root or global setup. | scenario flag, evolution tier, cluster member slot, chaos tier. | Sequence id, incident count, delay schedule. | Saves sequence variables and target memory. |
| Pick disaster family | Root or country. | allowed family set, state groups, prior family memory. | Family id. | Stores family id and reason. |
| Pick target state | Country or state loop helper. | family id, target scoring, excluded states. | Target state event target or state id variable. | Stores target and named region data. |
| Apply impact | State with country owner. | family id, severity, preparedness, evolution tier, current state population. | Damage variables, final loss rate, and death counts. | Damages buildings, reduces population by `current_state_population * final_dynamic_loss_rate`, logs deaths, applies modifiers. |
| Start aftermath | State and country. | family id, severity, unresolved ledgers. | Aftermath flags and variables. | Activates decisions and missions. |
| Advance recovery | Country or state. | action id, costs paid, target ledger. | Recovery progress. | Reduces ledger values and chain weights. |
| Schedule follow-up | Country or global sequence. | family id, unresolved ledgers, delay band. | Follow-up event id and delay. | Queues subevent without random log spam. |
| Close ledger | Country and state. | progress, timers, annexation, invalid target. | Cleanup. | Removes modifiers, clears flags, hides decisions. |

## Cooldown and repetition safeguards

- Per-state recent disaster memory should reduce chance of unrelated repeat hits.
- Same-family repeat hits can happen only when the aftermath chain calls for them.
- Cluster member slots should avoid selecting the same target state unless the family intentionally chains.
- Manual maximum intensity can relax repetition limits, but still should avoid every impact hitting one state.
- Recovery actions should have cooldowns or consume ledger-specific flags so the player cannot click the same cheap action endlessly.

## Death and chaos synchronization

Natural disasters feed civilian deaths. Every death entry should come from a per-state percentage calculation. Chaos gain should primarily come through the shared death system and a small direct incident pressure for severe evolved disasters. Do not add condemnation. Do not add chemical or nuclear contamination.

Direct chaos gain can be small for ordinary disaster sequences and larger for first abnormal season, but it should not push the event into its own world-end branch.
