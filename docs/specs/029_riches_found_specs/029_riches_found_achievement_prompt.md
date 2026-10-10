# Event 029 achievement prompt

Use this prompt to verify and finish the seven Event 029 achievements.

The achievement definitions are owned by [Part 6, Achievement set](029_riches_found_spec_part_6_assets_localisation_achievements.md#achievement-set); do not restate or change them here.

## Current state

All seven IDs are registered in `common/achievements/chaos_redux_achievements.txt` with titles, descriptions, and tooltips, their completed, grey, and not-eligible triplets are wired through `interface/029_riches_found.gfx`, and tracking lives in `common/scripted_effects/029_riches_found_achievement_effects.txt` and `common/scripted_triggers/029_riches_found_achievement_triggers.txt`.

Unlock and disqualifier acceptance is the open item.

## What to verify

For each achievement:

1. Every route step and disqualifier in Part 6 has a producer at the real call site (decision, mission result, incident, transfer, or evolution entry) and a consumer in the unlock trigger.
2. History flags and counters survive save and reload, and mission cleanup or recapture never clears a permanent disqualifier.
3. Hold timers start only after their stated precondition and reset on control loss.
4. One mission, incident, or transfer can never count twice.
5. The tooltip names the public feat and the visible requirements without hidden variable names, and hidden achievements stay vague until their reveal.
6. Debug, force-trigger, and custom setups follow the shared achievement eligibility contract.

Report each achievement as verified by source review, blocked with the missing producer or consumer, or needing a user live test, in a handoff under `docs/plans/029_riches_found_plans/subagent_handoffs/`.
