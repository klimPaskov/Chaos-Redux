# Event 012 Tier A identity icon GFX handoff

This bounded follow-up supplies six focus/goal DDS files and six decision DDS files. No package seal DDS was produced because the code audit found no current 64x64 package-seal consumer for these dormant fictional country packages; their current visual consumers are portrait sprites only.

The parent has already committed `interface/012_africa_strange_force_icons.gfx` with the primary strange-force registry. Do not append duplicate registrations there for these follow-up assets unless a real focus or decision consumer is wired. This handoff only records proposed stable sprite IDs and runtime paths.

| Package | Focus/goal DDS | Focus sprite ID | Decision DDS | Decision sprite ID |
| --- | --- | --- | --- | --- |
| Pan | `gfx/interface/goals/012_africa/tier_a/goal_012_africa_pan_high_chaos.dds` | `GFX_goal_012_africa_pan_high_chaos` | `gfx/interface/decisions/012_africa/tier_a/decision_012_africa_pan_high_chaos.dds` | `GFX_decision_012_africa_pan_high_chaos` |
| Gorilla Kingdom | `gfx/interface/goals/012_africa/tier_a/goal_012_africa_gorilla_kingdom.dds` | `GFX_goal_012_africa_gorilla_kingdom` | `gfx/interface/decisions/012_africa/tier_a/decision_012_africa_gorilla_kingdom.dds` | `GFX_decision_012_africa_gorilla_kingdom` |
| The Green | `gfx/interface/goals/012_africa/tier_a/goal_012_africa_the_green.dds` | `GFX_goal_012_africa_the_green` | `gfx/interface/decisions/012_africa/tier_a/decision_012_africa_the_green.dds` | `GFX_decision_012_africa_the_green` |
| Living Rivers | `gfx/interface/goals/012_africa/tier_a/goal_012_africa_living_rivers.dds` | `GFX_goal_012_africa_living_rivers` | `gfx/interface/decisions/012_africa/tier_a/decision_012_africa_living_rivers.dds` | `GFX_decision_012_africa_living_rivers` |
| Stoneborn | `gfx/interface/goals/012_africa/tier_a/goal_012_africa_stoneborn.dds` | `GFX_goal_012_africa_stoneborn` | `gfx/interface/decisions/012_africa/tier_a/decision_012_africa_stoneborn.dds` | `GFX_decision_012_africa_stoneborn` |
| Ancient Hosts | `gfx/interface/goals/012_africa/tier_a/goal_012_africa_ancient_hosts.dds` | `GFX_goal_012_africa_ancient_hosts` | `gfx/interface/decisions/012_africa/tier_a/decision_012_africa_ancient_hosts.dds` | `GFX_decision_012_africa_ancient_hosts` |

All focus DDS are 94x86 and all decision DDS are 32x32. Their headers are uncompressed legacy BGRA 32-bit with exact `128 + width*height*4` lengths, and every decoded DDS is pixel-equal to its target processed PNG.

Current code consumers audited in `common/characters/012_africa_fictional_characters.txt` are portrait IDs only: `GFX_portrait_012_africa_fictional_pan`, `GFX_portrait_012_africa_fictional_gorilla_kingdom`, `GFX_portrait_012_africa_fictional_the_green`, `GFX_portrait_012_africa_fictional_living_rivers`, `GFX_portrait_012_africa_fictional_stoneborn`, and `GFX_portrait_012_africa_fictional_ancient_hosts`. No current focus/decision/seal ID was found for these six package identities.
