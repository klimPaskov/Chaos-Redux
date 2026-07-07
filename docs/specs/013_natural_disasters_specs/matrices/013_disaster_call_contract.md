# Event 013 disaster call contract matrix

This matrix describes the reusable call surface that other systems should use. It is design guidance, not code.

| Call field | Required | Accepted direction | Default behavior |
| --- | --- | --- | --- |
| caller_type | Yes | random, cluster, scenario, external_event, deity, hostile_actor, debug | random |
| caller_event_id | No | event id or source key | Event 013 |
| disaster_family | No | specific family or family group | weighted random baseline pool |
| target_mode | No | state, country, region, coast, enemy, random valid, scripted target | random valid target |
| target_state | Conditional | chosen state | built from target mode |
| target_country | Conditional | chosen country | built from target state or anchor |
| severity | No | local, severe, regional, catastrophic, abnormal | local or sequence-scaled |
| sequence_count | No | single, local season, regional system, global pulse, moving corridor, barrage | stage default |
| news_policy | No | always, meaningful, first family, major only, none | meaningful with throttle |
| report_policy | No | affected country, caller, global, silent | affected country delayed report |
| aftermath_policy | No | none, light, normal, full, emergency | normal for serious impact |
| chain_policy | No | none, family, famine, disease, refugee, aftershock, tsunami, abnormal | family if severity allows |
| death_scale | No | multiplier or caller pressure | severity and vulnerability default |
| building_scale | No | multiplier or caller pressure | family and severity default |
| warning_scale | No | modifier to warning odds | local capacity default |
| caller_cost_checked | Yes for weaponized callers | flag or proof that caller paid cost | not needed for random or scenario |
| log_mode | No | normal Event 013 row, silent subcall, scenario row | Event 013 row for season start only |

## Caller safety

External callers can be dramatic, but they need their own cost, cooldown, and target legitimacy. The Event 013 engine should not provide free unlimited enemy disasters. The engine should enforce target validity, same-day duplicate blocking, heat stacking exclusion, and global abnormal repeat protection.
