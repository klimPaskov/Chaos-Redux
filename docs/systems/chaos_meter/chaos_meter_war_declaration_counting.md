# Chaos Meter War Declaration Counting

## Purpose

The chaos meter counts new war relations from `on_war_relation_added`, where `ROOT` is the attacker and `FROM` is the defender. The handler is `chaos_meter_on_war_relation_added` in `common/scripted_effects/chaos_meter_effects.txt`, wired from `common/on_actions/chaosx_on_actions_chaos_meter.txt`.

## Counting Rules

Major-on-major war relations contribute `constant:chaos_meter_delta.war.major`.
Other qualifying relations contribute `constant:chaos_meter_delta.war.minor` when the attacker is independent or outside a faction and the defender is independent.
Zombie outbreak attackers retain their exclusion.
Faction follow-up relations use the same historical qualification rather than a separate duplicate suppression rule.
Each qualifying relation contributes its full value without an actor-wide daily minor-war cap.

## Icons

This mechanic has no dedicated icons. It reuses the existing chaos meter history reason and popup assets:

- history reason constants in `common/script_constants/chaos_meter_constants.txt`
- history display through `common/scripted_effects/chaos_meter_effects.txt`
- popup wiring through the existing chaos meter scripted GUI

## Future Plans

If major-war spam becomes a balance problem, add a separate major-war daily cap rather than reusing the minor cap. If later event chains need exact multi-target batch reporting, pass an explicit target-count variable into `add_chaos_meter_value` before recording the history row.
