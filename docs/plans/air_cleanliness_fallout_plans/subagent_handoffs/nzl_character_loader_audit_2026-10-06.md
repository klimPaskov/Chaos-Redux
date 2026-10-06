# NZL Character Loader Audit (2026-10-06)

## Status and scope

This is a bounded read-only review of the parent-owned loader change in `common/characters/fallout_consolidated_characters.txt` and `common/scripted_effects/fallout_consolidated_effects.txt`. I made no gameplay, focus, localisation, or asset edits. The only file written for this task is this handoff.

The parent supplied HEAD `9ec627597` and the intended two-file diff boundary, and prohibited Git commands. I therefore verified the resulting source state and connected call paths but could not independently reconstruct the old generated role blocks for a byte-for-byte before/after comparison. The role-preservation conclusion below combines the current definitions with the parent-provided statement that only generation-token handling and indentation changed.

## Country package coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| NZL tag and package identity | Passed within loader scope | The activation gate requires the current NZL assignment identity, exact state package, and current conflict dispositions before activation. |
| Static leader and advisor definitions | Passed in the resulting source | All six expected IDs are declared in the static character file with their roles, traits, portraits, and advisor conditions. |
| Recruitment call scope | Passed | Both the existing-tag caller and the dynamic-output caller enter the activation effect in the intended country scope. |
| Focus promotions and tree assignment | Passed for character resolution | Parliament, Relief Speaker, and Harbor Constable promotions point to static leader IDs; activation loads `fallout_nzl_lifeboat_focus_tree`. |
| Portrait GFX and DDS files | Passed for file existence | All six referenced GFX sprites and their DDS textures exist. Parent context says the source placeholders still await the user's HOI4-style finals. |
| Advisor AI weights | Pending separate routed audit | The three existing advisor `ai_will_do` blocks are unchanged in the inspected role definitions. The parent has routed their mandatory probability pass to `fallout_probability_final`; that result was not available in this handoff. |
| Other country surfaces | Not audited by this assignment | Party setup, flags, state/map data, starting forces, technologies, production, supply, and broader playability remain outside the two-file loader review. |

## Static role inventory

The file-scoped values at lines 9-11 retain AI normal weight 10 and advisor costs 25/45 political power. The three leader definitions preserve their role identifiers, ideologies, traits, and large portrait tokens.

| Character ID | Current role and retained fields |
| --- | --- |
| `NZL_fallout_lifeboat_parliament` | Country leader, centrism, `fallout_nzl_lifeboat_parliament_trait`, large portrait. |
| `NZL_fallout_relief_speaker` | Country leader, centrism, `fallout_nzl_relief_speaker_trait`, large portrait. |
| `NZL_fallout_harbor_constable` | Country leader, despotism, `fallout_nzl_harbor_constable_trait`, large portrait. |
| `NZL_fallout_dairy_relief_commissioner` | Political advisor, matching `idea_token`, NZL-only eligibility, current-package and focus visibility, food-security availability, dairy trait, medium cost 45, AI normal factor 10 plus the existing food-critical modifier. |
| `NZL_fallout_storm_port_engineer` | Political advisor, matching `idea_token`, NZL-only eligibility, current-package and focus visibility, state 284 ownership/control availability, storm-port trait, medium cost 45, AI normal factor 10 plus the existing harbor-critical modifier. |
| `NZL_fallout_radio_service_coordinator` | Political advisor, matching `idea_token`, NZL-only eligibility, current-package and focus visibility, sea-lane-security availability, radio trait, low cost 25, AI normal factor 10. |

The advisor traits resolve in `common/country_leader/fallout_consolidated_leader_traits.txt` at lines 60-79. The three `idea_token` values match their corresponding character IDs in the advisor declarations.

## Recruitment behavior and caller scope

The current helper at `common/scripted_effects/fallout_consolidated_effects.txt:19005-19030` checks `NOT = { has_character = <ID> }` before each of the six `recruit_character` calls. The activation effect invokes that helper at line 19394 before the leader promotion, party setup, and focus-tree load.

The existing-tag path scopes activation inside `NZL = { }` at lines 21045-21070. The dynamic materialization path scopes activation inside `event_target:fallout_b7_nzl_dynamic_output = { }` at lines 20816-20818. The activation predicate requires `fallout_nzl_assignment_identity_is_current`, `fallout_nzl_has_exact_state_package`, current conflict dispositions, and that the package is not already current. The identity predicate checks the NZL or designated dynamic-country identity, current assignment row, New Zealand Lifeboat State memory ID, and Oceania remote-islands region. I verified the country scopes and identity gate; the parent-provided sole-receipt invariant remains owned by the broader B7 allocation work.

The effect promotes the static IDs `NZL_fallout_lifeboat_parliament` at line 19396, `NZL_fallout_relief_speaker` at line 19481, and `NZL_fallout_harbor_constable` at line 19500. The other three definitions are advisors and are not promoted as country leaders.

The parent-provided before-state used runtime `generate_character` blocks. The resulting state uses static role declarations followed by guarded country-scope recruitment. Installed documentation says `generate_character` requires a `token_base`, while the offline wiki explains that midgame generation needs a full history-file template and fails when that template does not exist. The reviewed recruit helper follows installed documentation that `recruit_character` attaches the named character to a country and must run in country scope.

## Portrait coverage

All six sprite declarations resolve to DDS files:

- `GFX_portrait_NZL_fallout_lifeboat_parliament` → `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_lifeboat_parliament.dds`.
- `GFX_portrait_NZL_fallout_relief_speaker` → `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_relief_speaker.dds`.
- `GFX_portrait_NZL_fallout_harbor_constable` → `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_harbor_constable.dds`.
- `GFX_portrait_NZL_fallout_dairy_relief_commissioner_small` → `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/NZL_fallout_dairy_relief_commissioner.dds`.
- `GFX_portrait_NZL_fallout_storm_port_engineer_small` → `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/NZL_fallout_storm_port_engineer.dds`.
- `GFX_portrait_NZL_fallout_radio_service_coordinator_small` → `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/NZL_fallout_radio_service_coordinator.dds`.

The asset check establishes that the declared sprites have files. It does not establish final portrait provenance or replace the separately pending user-supplied HOI4-style portrait finals.

## HOI4 source and MCP evidence

The installed game documentation search and read succeeded against revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`:

- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:4435-4457` documents `generate_character`, its country scope, and mandatory `token_base`.
- The same documentation at lines 5696-5708 documents `recruit_character` and its required country scope.

The offline wiki search identified `paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md:537-588` at revision `8ef3f5d9923026dd81f239944710b7331a8d06ad42e4345b32fce4e86dd95d98`. A revision-bound `hoi4.reference_read` attempt returned `REFERENCE_REVISION_STALE` while reporting that same current revision, so I read the cited local offline section directly. It states that midgame `generate_character` uses an existing full history-file template and fails when that template is absent.

The installed vanilla precedent was read locally from `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\characters\NZL.txt`, which declares static NZL characters, and `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\NZL - New Zealand.txt:74-78`, which recruits them into NZL.

The source index resolved `NZL_fallout_lifeboat_parliament`, `NZL_fallout_relief_speaker`, and `NZL_fallout_harbor_constable` as `kind = leader` definitions in `mod:common/characters/fallout_consolidated_characters.txt`, with no override or source-shadow flags. These lookups completed under index revision `25d9f9ad589104d481c81c257de87dd49be0409e5520c0f962f86e3c4e64ea7d`. The initial six-symbol parallel lookup batch did not return within roughly five minutes and was stopped; the three targeted leader lookups then completed successfully.

## Focus inspection and render

The read-only `hoi4.focus_inspect`, `hoi4.focus_render`, and `hoi4.focus_raster` routes completed for `fallout_nzl_lifeboat_focus_tree` in `common/national_focus/fallout_consolidated_focus.txt`, with no blockers or missing-character diagnostics. The narrow source lookups independently resolved the three promoted leaders.

The MCP diagnostics contained 10 layout warnings: five `FOCUS_LAYOUT_LINEAR_DETOUR`, three `FOCUS_LAYOUT_LONG_CONNECTOR`, and two `FOCUS_LAYOUT_ZIGZAG_CHAIN`. They identify the relief-rights, Devonport, storm-port, radio-weather, Pacific-rescue, and relief-ports chains, plus long links from `fallout_nzl_bind_the_two_islands` to `fallout_nzl_dairy_relief_fleet`, `fallout_nzl_rebuild_devonport`, and `fallout_nzl_home_guard_rolls`. One additional unrelated warning is `FOCUS_LOCALISATION_REFERENCE_MISSING` for the generic `continuous_restrict_freedom_desc` key.

The diagnostic set contains no overlap, crossing, or clipping code. I could not independently confirm the rendered pixels: the remote PNG resource read truncated the base64 data, so no local PNG was produced. The parent can review the actual full-resolution PNG artifact here: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0cc5bdbd3591ce90834c6ac2c8eec6601abadef5497b087bae7ba156fc9efad8/97b87fe6f0149bf4fd30855b963f6058ce5c10d70e99377060c8f43ab0090c28/fallout_nzl_lifeboat_focus_tree.focus.png` (SHA-256 `0cc5bdbd3591ce90834c6ac2c8eec6601abadef5497b087bae7ba156fc9efad8`, 453,909 bytes). A full-tree 0.25-scale PNG is also available at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0357ee212bb34de0755dc04ae74205606a2d3f36645e0f5e7c435e72a348e16f/d0fa34d6a3820474d08037e58dbd88434164b4cc249aa9252205d4b20ea27114/fallout_nzl_lifeboat_focus_tree.focus.png` (SHA-256 `0357ee212bb34de0755dc04ae74205606a2d3f36645e0f5e7c435e72a348e16f`, 51,045 bytes).

The focus-tree header at `common/national_focus/fallout_consolidated_focus.txt:37-39` says the tree has no active loader, while the NZL activation effect at `common/scripted_effects/fallout_consolidated_effects.txt:19428-19432` loads it and sets `fallout_nzl_focus_tree_loaded`. This stale prose is outside the reviewed character-loader diff and was not edited.

## Findings, uncertainty, and follow-up

No confirmed defect was found in the resulting six-character loader path: all IDs are static, all six guarded recruit calls are present, the callers use the expected country scopes, leader promotions resolve, and the six referenced portrait DDS files exist.

The exact before/after equality of role blocks was not independently compared because Git commands were prohibited for this assignment. The three advisor AI weights still need the parent-routed probability audit before anyone claims weighted-surface coverage. Pixel-level overlap, connector crossing, and clipping review remains open for the parent because the PNG resource could not be materialized locally. The existing focus layout diagnostics and stale focus-tree comment are recorded for parent review; no focus edits were authorized here.

No map inspection, country-wide balance review, game launch, or in-game validation was performed. The map, starting setup, and broader country package surfaces were outside the assigned loader audit.

## Files changed by this audit

Only `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/nzl_character_loader_audit_2026-10-06.md` was written by this subagent. No gameplay source was changed, and no commit was made.

## Guidance read

I read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-focus-trees/SKILL.md` for this bounded review.
