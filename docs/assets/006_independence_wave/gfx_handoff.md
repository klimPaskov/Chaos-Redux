# Event 006 static icon GFX handoff

## Parent-owned wiring boundary

This handoff does not edit `.gfx`, `.gui`, gameplay, localisation, or achievement
registry files. The parent implementation owns those edits. The final textures
already exist at the paths below and may be wired without renaming.

Recommended sprite registry: `interface/006_independence_wave.gfx`. If the parent
already created a dedicated Event 006 registry, use that file instead and keep the
sprite names below unchanged.

## Focus sprites

| Sprite | Texture |
|---|---|
| `GFX_goal_independence_wave_founding_administration` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_founding_administration.dds` |
| `GFX_goal_independence_wave_constitutional_state` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_constitutional_state.dds` |
| `GFX_goal_independence_wave_popular_councils` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_popular_councils.dds` |
| `GFX_goal_independence_wave_traditional_restoration` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_traditional_restoration.dds` |
| `GFX_goal_independence_wave_military_emergency` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_military_emergency.dds` |
| `GFX_goal_independence_wave_patron_client` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_patron_client.dds` |
| `GFX_goal_independence_wave_recognition_diplomacy` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_recognition_diplomacy.dds` |
| `GFX_goal_independence_wave_army_integration` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_army_integration.dds` |
| `GFX_goal_independence_wave_infrastructure_authority` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_infrastructure_authority.dds` |
| `GFX_goal_independence_wave_former_host_settlement` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_former_host_settlement.dds` |
| `GFX_goal_independence_wave_league_congress` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_league_congress.dds` |
| `GFX_goal_independence_wave_regional_formable` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_regional_formable.dds` |
| `GFX_goal_independence_wave_high_chaos_sovereignty` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_high_chaos_sovereignty.dds` |

Primary sprite entry pattern:

```text
spriteType = {
	name = "GFX_goal_independence_wave_founding_administration"
	texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_founding_administration.dds"
}
```

Every focus sprite also needs the usual paired shine sprite named by appending
`_shine`, for example
`GFX_goal_independence_wave_founding_administration_shine`. Mirror the installed
vanilla `interface/goals_shine.gfx` structure: use the same Event 006 texture as
the animation mask and retain vanilla's focus-shine overlay/effect settings. Do
not point the shine entry at a different family icon.

## Idea sprites

| Sprite | Texture |
|---|---|
| `GFX_idea_independence_wave_improvised_government` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_improvised_government.dds` |
| `GFX_idea_independence_wave_unrecognized_state` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_unrecognized_state.dds` |
| `GFX_idea_independence_wave_fragmented_command` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_fragmented_command.dds` |
| `GFX_idea_independence_wave_unsettled_borders` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_unsettled_borders.dds` |
| `GFX_idea_independence_wave_patron_pressure` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_patron_pressure.dds` |
| `GFX_idea_independence_wave_league_membership` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_league_membership.dds` |
| `GFX_idea_independence_wave_founding_identity` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_founding_identity.dds` |
| `GFX_idea_independence_wave_post_release_instability` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_post_release_instability.dds` |

Entry pattern:

```text
spriteType = {
	name = "GFX_idea_independence_wave_post_release_instability"
	texturefile = "gfx/interface/ideas/006_independence_wave/idea_independence_wave_post_release_instability.dds"
}
```

The Post-Release Instability sprite is stable but currently lacks an ASSET ID in
the accepted family registry. Add a registry row rather than renaming this file.

## Decision and mission sprites

| Sprite | Texture |
|---|---|
| `GFX_decision_independence_wave_recognition_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_recognition_actions.dds` |
| `GFX_decision_independence_wave_government_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_government_actions.dds` |
| `GFX_decision_independence_wave_army_integration_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_army_integration_actions.dds` |
| `GFX_decision_independence_wave_depot_border_actions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_depot_border_actions.dds` |
| `GFX_decision_independence_wave_former_host_negotiations` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_former_host_negotiations.dds` |
| `GFX_decision_independence_wave_patron_aid` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_patron_aid.dds` |
| `GFX_decision_independence_wave_patron_balancing` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_patron_balancing.dds` |
| `GFX_decision_independence_wave_network_aid` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_network_aid.dds` |
| `GFX_decision_independence_wave_league_votes` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_league_votes.dds` |
| `GFX_decision_independence_wave_border_arbitration` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_border_arbitration.dds` |
| `GFX_decision_independence_wave_formable_proclamation` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_formable_proclamation.dds` |
| `GFX_decision_independence_wave_integration_missions` | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_integration_missions.dds` |

Entry pattern:

```text
spriteType = {
	name = "GFX_decision_independence_wave_border_arbitration"
	texturefile = "gfx/interface/decisions/006_independence_wave/decision_independence_wave_border_arbitration.dds"
}
```

Use these sprite names in the decision/mission definitions according to the
authoritative decision map. One icon is intentionally shared inside each accepted
family; do not rename or duplicate the texture for every decision.

## Achievements

Do not add achievement `spriteType` definitions. HOI4 resolves achievement art by
exact filename under `gfx/achievements/`.

For each delivered ID, the completed, grey, and not-eligible files are:

```text
gfx/achievements/<achievement_id>.dds
gfx/achievements/<achievement_id>_grey.dds
gfx/achievements/<achievement_id>_not_eligible.dds
```

Delivered IDs:

- `chaosx_006_one_state_to_statehood`
- `chaosx_006_no_master`
- `chaosx_006_peace_with_host`
- `chaosx_006_break_reconquest`
- `chaosx_006_found_league`
- `chaosx_006_cross_regional_league`
- `chaosx_006_rescue_member`
- `chaosx_006_regional_formable`
- `chaosx_006_volga_bulgaria`
- `chaosx_006_small_to_major`
- `chaosx_006_radical_bloc`
- `chaosx_006_every_flag_survival`
- `chaosx_006_balanced_patrons`
- `chaosx_006_league_arbitrator`
- `chaosx_006_host_remnant`

`chaosx_006_assyria_survives` is reserved but unproduced. Exact reserved paths and
the required community-attributed source input are in `manifest.md`.

## Blocked/out-of-scope sprites

Do not wire placeholder textures for the following names:

- `GFX_independence_wave_formable_form_01` through
  `GFX_independence_wave_formable_form_48`;
- `GFX_independence_wave_league_emblem`;
- `GFX_independence_wave_recognition_seal_static` and
  `GFX_independence_wave_recognition_seal_animated`;
- `GFX_independence_wave_dependency_warning_static` and
  `GFX_independence_wave_dependency_warning_animated`;
- `GFX_independence_wave_league_charter_activation_static` and
  `GFX_independence_wave_league_charter_activation_animated`;
- `GFX_independence_wave_formable_eligibility_seal_static` and
  `GFX_independence_wave_formable_eligibility_seal_animated`.

The formable/league identities require final tags and approved motifs. The four
animated pairs require GUI dimensions and real authored frame sequences with
static fallbacks. `manifest.md` records the exact missing inputs and naming
contract.
