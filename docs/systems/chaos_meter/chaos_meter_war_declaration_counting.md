# Chaos Meter War Declaration Counting

## Purpose

The chaos meter counts new war relations from `on_war_relation_added`, where `ROOT` is the attacker and `FROM` is the defender. The handler is `chaos_meter_on_war_relation_added` in `common/scripted_effects/chaos_meter_effects.txt`, wired from `common/on_actions/chaosx_on_actions_chaos_meter.txt`.

## Counting Rules

Major-on-major war relations contribute `constant:chaos_meter_delta.war.major`.
Other qualifying relations contribute `constant:chaos_meter_delta.war.minor` when the attacker is independent or outside a faction and the defender is independent.
Zombie outbreak attackers retain their exclusion.
Faction follow-up relations are ignored when another member of the attacker's faction already fights the defender.
The handler checks that context before counting either a major or minor relation.
Minor contributions retain their full configured value until the attacker's daily total reaches `constant:chaos_meter_war_cap.minor_same_day` (5).
Only any remaining daily allowance contributes on the last eligible relation; the next day starts a fresh allowance.
Major-on-major relations retain their configured 5 contribution and do not consume the minor allowance.
The existing `chaos_meter_minor_war_declaration_day` and `chaos_meter_minor_war_chaos_today` country variables own that allowance; no periodic reset hook is needed.
Faction context is a game-state proxy for a follow-up relation, not a durable declaration receipt, and its outcome depends on the relation state visible when the callback fires.

## Icons

This mechanic has no dedicated icons. It reuses the existing chaos meter history reason and popup assets:

- history reason constants in `common/script_constants/chaos_meter_constants.txt`
- history display through `common/scripted_effects/chaos_meter_effects.txt`
- popup wiring through the existing chaos meter scripted GUI

## Future Plans

If major-war spam becomes a balance problem, add a separate major-war daily cap rather than reusing the minor cap. If later event chains need exact multi-target batch reporting, pass an explicit target-count variable into `add_chaos_meter_value` before recording the history row.
