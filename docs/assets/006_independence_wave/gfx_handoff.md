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

`chaosx_006_assyria_survives` is final, reviewed, and runtime-installed through
the IW-043/IW-058 static icon package. Use
`docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/manifest.md`
and its validation reports for the exact source, processed PNG, and runtime DDS
paths. The post-1968/1973 modern Assyrian flag remains excluded. The signature
achievement itself remains hidden/fail-closed until its proof writer and
adapter-attestation gates pass. No Event 006 advisor asset or sprite exists.

## Blocked/out-of-scope sprites

Do not wire placeholder textures for the following names:

- `GFX_independence_wave_formable_form_01` through
  `GFX_independence_wave_formable_form_48`;
- `GFX_independence_wave_league_emblem`;

The formable/league identities require final tags and approved motifs. The four
animated status families are no longer blocked: their authored sheets and static
fallbacks are consumed by the Statehood Ledger's explicit `Animate` toggle in
`interface/006_independence_wave.gui` and
`common/scripted_guis/006_independence_wave_scripted_gui.txt`.

## Northern and western Europe portrait handoff

Two approved source-backed, route-owned portrait DDS files for RHI and BAY are
documented in `northern_western_europe_gfx_handoff.md`. That handoff owns the
sprite names, exact texture paths, route locks, the blocked BRI identity record,
and the warning that historical symbol previews are provenance inputs rather
than runtime flag sprites.

The current full fictional portrait inventory and stable runtime contract are
in `portrait_refresh_male_hoi4_2026_07_18/manifest.md`, with production and
root visual-review handoff
`../../plans/006_independence_wave_plans/subagent_handoffs/006_event6_male_commander_portrait_refresh_2026_07_18.md`.
The registered AFX, AGX, AJX, BAY, BRI, RHI, SCO, and WLS textures retain their
existing registries and consumers. ACX and AEX remain unregistered
readiness-pool art only. The rejected mixed generated-art portrait handoff is
not a wiring authority, and custom Event 006 advisor icons remain withdrawn.

## 2026-07-18 FORM-48 Pacific supersession

The older blocked range above is superseded for `FORM-48` only. The final
texture is installed at
`gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds`.
The parent implementation should register it, preferably in a dedicated
`interface/006_independence_wave_form48.gfx`, without changing either stable
identifier:

```text
spriteTypes = {
	spriteType = {
		name = "GFX_independence_wave_formable_form_48"
		texturefile = "gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds"
	}
}
```

The complete `HBX` and `PFX` normal, medium, and small ideology ladders are
already installed and resolve through HOI4's country-tag filename lookup; they
need no sprite definitions. `HBX` now uses the historical 1911 Bear Flag
arrangement with the exact `CALIFORNIA REPUBLIC` legend; the prior textless
adaptation is no longer a runtime source. The parent must connect `PFX` to the FORM-48
cosmetic/formable path and point the stable UI consumer at the sprite above.
Detailed evidence and exact filenames are in
`form48_pacific_assets_2026_07_17/gfx_handoff.md`.
