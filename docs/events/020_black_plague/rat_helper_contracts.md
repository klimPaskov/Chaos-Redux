# Event 020 Rat Helper Contracts

Event 020 rat-carrier helpers live in `common/scripted_effects/020_black_plague_rat_effects.txt`. They are private to the Black Plague system and do not belong in the cross-system dynamic-effect registry.

## black_plague_rat_refresh_swarm_meters

Purpose: refresh the visible Brood Mass carrier meters during the existing capped `RTA` growth pulse.

Scope: active `RTA` country. The helper excludes `RTX`, whose Dominion, Sentience, Cohesion, and Hunger meters use the separate royal pulse.

Inputs: Event 020 hierarchy flags, controlled Rat-Controlled state count, immune-blood hardening, brood state, and the existing pulse variables.

Outputs:

- `black_plague_rat_hunger`
- `black_plague_rat_coherence`
- `black_plague_rat_disease_dominion`
- `black_plague_rat_dominion_states`

Defaults: every visible meter is clamped to the shared `0` to `100` range.

Side effects: the helper can fire `chaosx.nr20.46` once when unresolved Hunger crosses the crisis threshold. Its choices spend mass or feed on a controlled state without removing the underlying plague.

Example:

```txt
RTA = {
	black_plague_rat_refresh_swarm_meters = yes
}
```

## Assets

The helper uses the existing Rat category meters and Event 020 report presentation. It requires no additional sprite registration.

## Future plans

Future rat-carrier meters should remain Event 020-owned unless an unrelated event adopts the same complete contract and state model.
