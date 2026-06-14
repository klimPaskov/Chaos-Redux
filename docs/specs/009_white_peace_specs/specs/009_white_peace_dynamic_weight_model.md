# Event 009 — Dynamic Weight and Runtime Selection Model

## Design goal

White Peace is a peace-making event in a mod built around escalation, so its selection chance must be deliberately restrained. The event should be visible over a long campaign, but it should not compete with ordinary chaos events unless war clutter is genuinely high.

The model below is written as a design target. The implementation agent should translate it into the existing Chaos Redux event-weight helper pattern rather than building a parallel picker.

## Core formula

Use two caps:

1. **Environment cap** — recalculated from current wars and candidate count. This is never higher than `1500`.
2. **Effective cap** — environment cap multiplied by the normal repeatable decay multiplier from the fired-count system.

```text
environment_cap = clamp(base_cap + war_pressure + candidate_pressure + clutter_bonus + stale_war_bonus, min_cap, 1500)

effective_cap = floor(environment_cap * repeatable_decay_multiplier * evolution_multiplier)

live_weight = min(recovered_repeatable_weight, effective_cap)
```

If no safe candidate pair exists, the event has no live weight and should show as unavailable.

## Suggested tuning constants

Put these in an event-weight or Peace-cluster script constants file, following the existing constant organization.

| Constant | Suggested value | Purpose |
| --- | ---: | --- |
| `white_peace_base_cap` | `125` | Keeps one small valid war from producing a high weight. |
| `white_peace_min_valid_cap` | `120` | Minimum cap when a safe pair exists after all multipliers. |
| `white_peace_max_environment_cap` | `1500` | Hard cap requested for this event. |
| `white_peace_active_war_value` | `90` | Adds pressure per active war. |
| `white_peace_active_war_cap` | `540` | Prevents war count alone from maxing the event. |
| `white_peace_safe_minor_pair_value` | `85` | Adds pressure for safe minor pairs. |
| `white_peace_safe_minor_pair_cap` | `595` | Rewards many valid pairs without making every war a peace event. |
| `white_peace_minor_only_war_value` | `60` | Adds pressure for wars with no major participants. |
| `white_peace_minor_only_war_cap` | `240` | Makes true minor-war clutter matter. |
| `white_peace_clutter_bonus_5_wars` | `125` | First world-clutter step. |
| `white_peace_clutter_bonus_8_wars` | `175` | Second world-clutter step. |
| `white_peace_clutter_bonus_12_wars` | `225` | Late clutter step. |
| `white_peace_stale_war_bonus` | `75` | Optional if safe war age tracking exists. |
| `white_peace_recent_global_penalty` | `0.80` | Optional extra multiplier after very recent firing if repeatable decay is not enough. |

The tuning constants are intentionally moderate. With one safe minor war, the cap should usually land near the `250–400` range, far below `1000`. With many valid wars, it can rise toward or above `1000`, but only severe war clutter should approach `1500` before repeatable decay and evolution penalties.

## Evolution multipliers

Higher stages are stronger, so the event should be less likely to be selected.

| Stage | Multiplier | Reason |
| --- | ---: | --- |
| Base | `1.00` | One pair only. |
| I — Repeated Minor Settlements | `0.78` | One firing can settle several minor pairs. |
| II — Major-Country Settlement | `0.55` | Can involve a major country. |
| III — Broad Diplomatic Settlement | `0.38` | Can remove a larger war segment. |

This multiplier applies after the environment cap is calculated and before the repeatable recovered weight is clipped.

## Worked examples

These examples assume no previous Event 009 firing and no repeatable decay.

| World state | Approximate environment cap before evolution | Stage | Effective cap | Design reading |
| --- | ---: | --- | ---: | --- |
| One safe minor war, two active wars total | `~380` | Base | `~380` | Available but much less likely than a default event. |
| Three active wars, two safe minor pairs | `~565` | Base | `~565` | Noticeable but still restrained. |
| Six active wars, four safe minor pairs | `~1165` | Base | `~1165` | War clutter is high enough to compete. |
| Six active wars, four safe minor pairs | `~1165` | Stage I | `~909` | Stronger effect, lower selection chance. |
| Ten active wars, six safe minor pairs, one major war | `~1500` | Stage II | `~825` | Can touch majors but remains rarer than base clutter cleanup. |
| Twelve active wars, eight safe pairs | `1500` | Stage III | `570` | Broad settlement exists as a rare pressure valve. |
| Same as above after one Event 009 firing | `1500` | Stage III | `285` | Repeatable decay keeps repeated broad peace rare. |

## Candidate-count calculation

The event should not use raw active-war count alone. It must measure safe candidates. If active wars exist but all are protected or invalid, the event should not fire.

Recommended runtime variables:

| Variable | Meaning |
| --- | --- |
| `global.white_peace_active_war_count` | Count of active wars discovered during the check. |
| `global.white_peace_safe_minor_pair_count` | Count of valid minor-versus-minor pairs. |
| `global.white_peace_minor_only_war_count` | Count of wars with no major participants, if unique-war tracking is practical. |
| `global.white_peace_major_candidate_count` | Count of stage II/III safe major relationships. |
| `global.white_peace_broad_candidate_score` | Score for stage III branch selection. |

If unique-war counting is too expensive or not supported cleanly, use candidate-pair count plus country-at-war count as the main dynamic proxy. Do not add a daily all-country counter only for this event.

## On-demand calculation rule

Weight and candidate context should be prepared on demand:

- when the random event picker evaluates Event 009;
- when the event list needs to show live weight/detail state;
- when the Peace cluster detail view evaluates availability;
- when a test firing requests Event 009 through existing settings tools.

Do not add a new daily or weekly global loop solely for this event. If the existing monthly recovery pulse already recalculates event weights, it can call a global-only helper, but country-pair candidate scanning should stay inside selection/detail preparation.

## Effective weight lifecycle

Recommended lifecycle:

1. Existing repeatable recovery raises `recovered_repeatable_weight` by the normal monthly amount.
2. Event 009 helper recalculates `environment_cap` from current war pressure.
3. Helper multiplies by `evolution_multiplier` and normal repeatable decay multiplier.
4. Live picker uses `min(recovered_repeatable_weight, effective_cap)`.
5. If conditions worsen, the displayed and used weight falls immediately because the cap fell.
6. If conditions improve, the cap rises immediately, but the recovered weight still needs normal recovery unless it is already above the cap.
7. When the event fires, existing repeatable fired-count and cap-decay behavior applies.

Do not permanently lower recovered weight just because the environment cap temporarily fell. The cap should clip the live value; it should not erase stored recovery.

## Branch selection after event is picked

After Event 009 is selected, branch mode should be chosen separately from event-pool weight.

| Stage | Single minor | Multi minor | Major-country | Broad settlement |
| --- | ---: | ---: | ---: | ---: |
| Base | `100` | `0` | `0` | `0` |
| I | `70` | `30` | `0` | `0` |
| II | `60` | `25` | `15` | `0` |
| III | `50` | `25` | `15` | `10` |

Branch weights should be modified by candidate availability:

- if no multi-minor candidate exists, transfer its weight to single minor;
- if no major candidate exists, transfer its weight to minor branches;
- if broad settlement has no valid candidate, transfer its weight to multi-minor or single minor;
- if only major candidates exist at stage II/III, allow major branch but apply a final safety reroll;
- if no branch can build a valid target, skip cleanly.

## Safety scoring

After forbidden candidates are removed, use weighted random selection rather than pure random. Suggested scoring:

| Factor | Score change | Purpose |
| --- | ---: | --- |
| Both countries are minors | `+40` | Base event identity. |
| War has no major participants | `+30` | Avoids changing big wars. |
| War has lasted long enough to feel stale | `+20` | Removes clutter rather than fresh wars. |
| Neither capital is occupied by the other | `+20` | Avoids robbing clear victories. |
| Both countries are independent | `+15` | Avoids subject/overlord edge cases. |
| Both are outside factions | `+15` | Avoids alliance-war side effects. |
| Previous pair settlement memory exists | `-100` and veto if active | Prevents repeat loops. |
| Either side is near capitulation | veto | Avoids invalid rescue. |
| Either side has protected-war flag | veto | Avoids scripted content. |
| Civil conflict pair | veto | Avoids civil war breakage. |
| Nonhuman/special threat actor | veto | Keeps crisis systems intact. |

Stage II/III major candidates start with a lower base score and require additional safety proof.

## Safe candidate tiers

Use three tiers internally.

### Tier A — safe

- two minors;
- no faction leaders;
- no major participants;
- no subject/overlord complications;
- no protected flags;
- no capital occupied;
- no near-capitulation state.

Base and stage I should use only Tier A.

### Tier B — cautious

- minor pair inside a larger war but pair-level settlement is safe;
- subject country whose overlord state will remain valid;
- minor-major relationship at stage II/III with no protected flags;
- war has major participants but selected pair is not deciding the entire war.

Stage II and III can use Tier B after a final validation pass.

### Tier C — forbidden

Any pair that hits a hard veto. No stage should use Tier C.

## Repeat-prevention memory

Recommended memory durations:

| Memory | Duration direction | Purpose |
| --- | --- | --- |
| `recent_white_peace_country` | about 180 days | Avoid same country being repeatedly cleaned up. |
| `recent_white_peace_pair` | about 360 days | Avoid the same two countries immediately cycling through war and peace. |
| `recent_major_white_peace_country` | about 540 days | Avoid repeated major settlements. |
| `recent_broad_white_peace` | about 720 days | Keep broad settlements rare beyond repeatable decay. |

Use script constants for the durations. If timed flag fields reject script constants, use file-scoped literal constants mirrored to the script constants file and document the mirror.

## Chaos adjustment model

The direct Chaos reduction should be meaningful but capped.

| Branch | Suggested direct Chaos change | Cap note |
| --- | ---: | --- |
| Single minor pair | `-1` | Always small. |
| Multi minor | `-1` per pair, capped at `-3` | Keeps stage I from being too restorative. |
| Major-country settlement | `-2`, or `-3` if a major exits a long war | Stronger because major involvement matters. |
| Broad settlement | `-1` per pair/war segment, capped at `-3`, rare `-4` for several separate wars | Still cannot undo global chaos alone. |

These values align with the broader Chaos Meter idea that peace reduces chaos but does not erase the consequences of war.

## Availability states for UI

Use clear skip reasons in the event list and cluster detail view.

| State | Display direction |
| --- | --- |
| No active war exists | Event unavailable. |
| Active wars exist but no safe pair exists | Event unavailable: no safe settlement candidate. |
| Safe minor pair exists | Event available with dynamic weight. |
| Only major candidate exists before stage II | Event unavailable or limited to N/A because major settlement is not unlocked. |
| Protected wars dominate | Event unavailable: protected conflicts. |
| Recently settled pairs only | Event unavailable or low weight due recent settlement memory. |

Do not show raw candidate trigger blocks to players.

## Validation scenarios

Implementation validation should include these scenarios:

1. **No active wars** — Event 009 has no live weight and event detail shows unavailable.
2. **One safe minor war** — event has low dynamic cap below default event weight and can settle one pair.
3. **Several safe minor wars** — cap rises; stage I branch can settle more than one pair within caps.
4. **Only protected wars** — active wars exist but Event 009 does not fire.
5. **Only major wars before stage II** — base event does not settle majors.
6. **Stage II with safe major candidate** — major branch can fire but remains less likely than minor branch.
7. **Stage III overload** — broad settlement caps pair count and Chaos reduction.
8. **Repeat firing** — normal repeatable recovery and decay reduce live cap after firing.
9. **Recent pair memory** — the same pair is excluded until memory expires.
10. **Capital occupation edge case** — near-winner wars are not white-peaced by accident.
