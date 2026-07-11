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
| recovery_scale | No | recovery-burden multiplier | family and aftermath-policy default |
| supply_scale | No | state-disruption multiplier | family and severity default |
| caller_cost_checked | Yes for weaponized callers | flag or proof that caller paid cost | not needed for random or scenario |
| caller_cooldown_checked | Yes for weaponized callers | flag or proof that caller passed its own cooldown | not needed for random or scenario |
| target_legitimacy_checked | Yes for weaponized callers | flag or proof that hostile target selection is legitimate | not needed for random or scenario |
| log_mode | No | normal Event 013 row, silent subcall, scenario row | Event 013 row for season start only |

## Caller safety

External callers can be dramatic, but they need their own cost, cooldown, and target legitimacy. The Event 013 engine should not provide free unlimited enemy disasters. The engine should enforce target validity, same-day duplicate blocking, heat stacking exclusion, and global abnormal repeat protection.

Target modes are fixed domains. A retry may reroll a family only when the caller requested a random family or family group; it never widens a selected state, country, strategic region, coast, enemy set, or caller-provided target. A specific family is never substituted. Every candidate must pass immutable family geography before logistical exposure is scored: a volcanic vent, climate band, storm basin, coast type, fuel zone, or slope domain is physical eligibility, while infrastructure, population, resources, buildings, and prior disaster history are priority inputs only.

## Public result

Every call returns `natural_disaster_call_result`, `natural_disaster_call_reject_reason`, `natural_disaster_call_sequence_id`, `natural_disaster_call_primary_job_count`, and `natural_disaster_call_skipped_primary_count`. The first successfully scheduled primary pair is exposed through `natural_disaster_call_resolved_primary_family`, regular event targets `natural_disaster_call_resolved_primary_state` and `natural_disaster_call_resolved_primary_country`, and numeric proof outputs `natural_disaster_call_has_resolved_primary_state` and `natural_disaster_call_has_resolved_primary_country`. `natural_disaster_call_resolved_target_region` echoes a successful selected-region request. A caller must test the numeric proof outputs because regular event targets can remain present after an earlier call in the same chain.
