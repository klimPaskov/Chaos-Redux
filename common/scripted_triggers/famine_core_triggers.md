# Famine state cause and reserve gates

This API note supplements `famine_core_triggers.txt` and the core calculation contract in `../scripted_effects/famine_core_effects.md`.
The three historical cause gates run in the exact STATE selected by the caller.
They read facts only and never register a state, add pressure, grant food, commit a stage, or change population.
Selection and mapping both apply the same gate, while their callers retain the existing anchor checks.

| Trigger | Required facts | Defaults and output |
| --- | --- | --- |
| `famine_china_policy_profile_cause_proven` | CHI or PRC owns or controls the state, current `famine_food_pressure` is positive, and extraction, concealment, owner forced-labor quota, restricted owner departure policy, or at least standard occupation conduct holds. | Boolean. Caller must resolve temporary `famine_occupation_profile` first. Missing policy variables prove no policy cause. The Henan anchor and post-start date checks belong to selector and mapper. |
| `famine_ceara_profile_cause_proven` | BRA owns or controls the state, current food pressure is positive, and its latest source is natural disaster/resource shortage, an unexpired disaster context exists, owner departure is restricted, or an active camp exists. | Boolean. No occupation prerequisite. A different food shock without a drought or confinement cause fails. The Ceara anchor belongs to selector and mapper. |
| `famine_congo_profile_cause_proven` | BEL or FRA owns or controls the state, current food pressure is positive, and at least standard occupation, non-core colonial ownership, local-war evidence, owner forced-labor quota, or an active camp holds. | Boolean. Caller must resolve temporary occupation and local-war outputs first. Congo/Middle Congo anchors belong to selector and mapper. |

For any caller that consumes the helpers' temporary outputs, create `famine_occupation_profile = constant:famine_occupation_profile.none` and `famine_local_war_evidence = constant:humanitarian_runtime.zero` before calling their resolvers.
Temporary values are unscoped.
The resolvers update that storage and the cause gates read it without further mutation.

Example within the existing Henan selector, after resolving occupation conduct:

```text
if = {
	limit = { famine_china_policy_profile_cause_proven = yes }
	set_variable = { famine_historical_profile_id = constant:famine_profile_id.hist_china_policy_famine }
}
```

The production selector additionally checks the exact Henan state and date.
The cause gate itself is not permission to apply that profile to another state.
The current famine reserve-release and retirement gates retain their contracts in the core and decision-owner API notes.
