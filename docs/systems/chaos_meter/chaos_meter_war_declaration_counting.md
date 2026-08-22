# Chaos Meter War Declaration Counting

## Purpose

The chaos meter counts new war relations from `on_war_relation_added`, where `ROOT` is the attacker and `FROM` is the defender. The handler is `chaos_meter_on_war_relation_added` in `common/scripted_effects/chaos_meter_effects.txt`, wired from `common/on_actions/chaosx_on_actions_chaos_meter.txt`.

## Counting Rules

Faction follow-up war relations are ignored when another member of the attacker's faction is already at war with the same defender. This keeps a faction-wide declaration against many targets from multiplying chaos by every faction member that joins or repeats the same target war.

Minor war declarations use `constant:chaos_meter_delta.war.minor`, but each attacking country can only add up to `constant:chaos_meter_war_cap.minor_same_day` chaos from minor war relations on the same day. The actor stores:

- `chaos_meter_minor_war_declaration_day`
- `chaos_meter_minor_war_chaos_today`

When the day changes, the stored total resets on the next minor war relation handled for that country.

## Icons

This mechanic has no dedicated icons. It reuses the existing chaos meter history reason and popup assets:

- history reason constants in `common/script_constants/chaos_meter_constants.txt`
- history display through `common/scripted_effects/chaos_meter_effects.txt`
- popup wiring through the existing chaos meter scripted GUI

## Future Plans

If major-war spam becomes a balance problem, add a separate major-war daily cap rather than reusing the minor cap. If later event chains need exact multi-target batch reporting, pass an explicit target-count variable into `add_chaos_meter_value` before recording the history row.
