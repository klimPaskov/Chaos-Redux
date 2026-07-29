# Repo Explorer Handoff

## Scope read
- Parent task: perform the final Event 012 registration scan after Charter UI DDS, independence-wave flags, sovereign portraits, and Event 013 nature-call changes settled.
- Explicit constraints: read-only repository exploration with this handoff as the only write; classify active hard blockers separately from dormant or deferred references.
- Requested surfaces: `set_cosmetic_tag`, characters, country/news events, focus trees, ideas, GFX textures, localisation, audio, flags, and Event 013-call references.
- Skills and references read: `chaos-redux-events`, `chaos-redux-super-events`, the required offline Paradox wiki pages, and the relevant vanilla event, GUI, localisation, effects, and script-constant documentation.

## Primary findings
- No active Event 012 parser or registration hard blocker was found in the settled worktree.
- Event 012 has 43 definitions: 39 country events and 4 news events. A repository-wide direct-reference pass found 97 Event 012 reference occurrences, 43 unique IDs, and no undefined IDs.
- All requested dynamic references resolve: 48 unique `set_cosmetic_tag` values, 9 `recruit_character` values, 9 focus-tree loads covering 8 unique trees, and 93 idea-reference occurrences covering 80 unique ideas.
- The six `interface/012_africa*.gfx` packages expose 205 texture rows in total, and all 205 runtime texture paths exist, including all 16 Charter textures and all 16 sovereign portraits.
- Event 012 actions 69 and 70 use the existing Event 013 public `call_natural_disaster = yes` contract with exact target, caller proof, receipts, cooldown, severity, and backfire bookkeeping; no unresolved direct `chaosx.nr13.*` call was found.
- Event 012 audio files exist on disk, but IDs 59 and 60 remain unregistered and unconsumed by the super-event sound registry. This is a deferred package surface, not an active Event 012 load blocker because the world super-event readiness gate remains unset.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `events/012_african_union.txt` | Canonical Event 012 entry and union/war/reaction events. | `chaosx.nr12.1` at line 14; `chaosx.nr12.300`–`.309` at lines 210–627; `chaosx.nr12.308` is the Event 012 news definition at line 609. |
| `events/012_africa_evolutions.txt` | Event 012 evolution events. | `chaosx.nr12.400`–`.403` at lines 5–38. |
| `events/012_africa_priority_member_events.txt` | Priority-member events and nine sovereign recruit calls. | `africa_priority_member.1240` at line 20; `recruit_character` calls at lines 32–64. |
| `events/012_africa_rsa.txt` | RSA route events. | `chaosx.nr12.1200`–`.1209` (except `.1203`) at lines 12–184. |
| `events/012_africa_world_order.txt` | World-order country/news events. | Country IDs `.1`–`.7` and `.60`; news IDs `.100`–`.102` at lines 14–305. |
| `common/scripted_effects/chaosx_logic_effects.txt` | Global fire-once registration. | Event 012 is added to `global.fire_once_events` at line 178. |
| `common/scripted_effects/chaosx_settings_effects.txt` | Prefire and Event 012 dispatcher path. | Africa prefire/dispatcher blocks are in the Event 012 registration section around lines 4711 and 4815. |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | Cluster registration and severity/member mapping. | Event 012 maps to the formables cluster and required member path around lines 379 and 525. |
| `common/scripted_effects/chaosx_events_log_effects.txt` | Event-log actor and evolution registration. | Africa actor mapping is around lines 283–288; evolution preview handling begins around line 2131. |
| `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` | Event name mapping. | `africa_event.id` maps to `chaosx.event_name.12` at lines 69–70. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Event-log name and detail-window mapping. | Event name mapping is at lines 1055–1059; Africa event-detail localisation is at lines 5966–5967. |
| `common/countries/012_africa_cosmetic.txt` and `common/countries/012_africa_world_order_cosmetic.txt` | Cosmetic-tag definitions. | The 48 Event 012 cosmetic references resolve to the route tags in these two files. |
| `common/characters/012_africa_priority_member_characters.txt` | Priority-member character definitions. | All nine recruit references resolve; the file contains 16 sovereign character definitions. |
| `common/scripted_effects/012_africa_world_order_effects.txt` | World-order focus loaders, ideas, cosmetic tags, and package lifecycle. | Installer readiness guard at lines 465–469; six focus loaders at lines 516–541; route idea/tag application at lines 1234–1286. |
| `common/national_focus/012_africa_*` and `common/ideas/012_africa_*` | Focus and idea definitions. | All Event 012 loader and idea references resolve across the continental, priority-member, unity, and six world-order files. |
| `interface/012_africa*.gfx` and `gfx/interface/012_africa/` | Event pictures, focus/decision art, portraits, Charter UI sprites, and texture consumers. | Final scan: 205 texture rows, 205 paths present; `interface/012_africa_charter.gfx` contains 16 Charter rows. |
| `interface/012_africa_charter.gui` and `common/scripted_guis/012_africa_charter_scripted_gui.txt` | Charter GUI surface and click-method wiring. | 63 unique GUI text/button/tooltip localisation tokens resolve; 36 button elements have matching click and enabled/visibility methods. Vanilla-only sprites are `GFX_flag_small2` and `GFX_tiled_window_transparent`. |
| `common/scripted_effects/012_africa_action_effects.txt` | Event 013 nature-call caller and receipt ledger. | Public caller helper begins at line 6319, invokes `call_natural_disaster = yes` at line 6372, and is dispatched from action resolution at line 6463. |
| `common/script_constants/012_africa_action_constants.txt` | Action IDs and caller tuning. | `petition_the_rain = 69` and `defy_the_drought = 70` at lines 84–85; caller tuning block begins at line 349. |
| `common/scripted_triggers/012_africa_triggers.txt` | Nature-call actor, cost, cooldown, and target gates. | Nature-call eligibility and cost triggers begin at lines 1085 and 1107. |
| `events/013_natural_disasters.txt` and `common/scripted_effects/013_natural_disasters_effects.txt` | Event 013 public contract and downstream controller. | Canonical hidden entry `chaosx.nr13.1` is at line 12; it consumes the caller variables and invokes the shared `call_natural_disaster` contract at line 60. |
| `sound/012_africa/` and `sound/012_africa/` | Physical Event 012 super-event audio candidates. | `super_event_59_scramble_response` and `super_event_60_continental_wars` exist as WAV files, but are not registered in `sound/chaosx_sound.asset`, or `sound/chaosx_sound.asset`. |

## Existing patterns

Event 012 follows the repository’s canonical registration pattern: numbered entry event, global fire-once membership, prefire/dispatcher routing, event-log actor and detail mapping, and cluster registration. The canonical gameplay entry remains `chaosx.nr12.1`.

The world-order package is intentionally dormant. Its six package loaders and installer require `africa_world_package_implementation_ready`; the current worktree has only reads of that flag and no setter. The world-order focus trees are iconless shells and the prior 159 world-order focus/idea art consumers are no longer active references. This is a safe deferred art/package state, not a parser error.

The nature-call route reuses the Event 013 controller contract instead of introducing a second event family. The caller reserves cost, persists the selected-country target, writes proof inputs, records accepted/rejected/backfire receipts, and clears the reservation in the existing action ledger.

Generic event pictures are deliberate vanilla reuse. `GFX_report_event_generic_conference` and `GFX_report_event_generic_african_unity` resolve from the vanilla `interface/eventpictures.gfx`; all dedicated Event 012 event-picture names resolve from the mod’s current GFX files.

## Vanilla or reference precedents

- Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/eventpictures.gfx:1684` defines `GFX_report_event_generic_conference`.
- Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/eventpictures.gfx:3061` defines `GFX_report_event_generic_african_unity`.
- Vanilla `interface/general_stuff.gfx:282` and `interface/core.gfx:149` provide the Charter GUI’s `GFX_flag_small2` and `GFX_tiled_window_transparent` sprites.
- The required vanilla documentation and offline Paradox wiki pages were used for event, effect, trigger, localisation, GUI, on-action, and script-constant syntax. No additional reference-mod precedent was needed for this inventory.

## Likely edit order for the parent

1. Treat the active Event 012 registrations as settled; no gameplay registration patch is required from this scan.
2. Keep the Event 013 caller contract and action 69/70 gates synchronized with the existing Event 013 controller; do not add direct `chaosx.nr13.*` event calls unless the public contract changes.
3. If the world-order package is reactivated, restore its complete art, focus/idea icon, super-event text/image/audio/scenario package, and readiness-flag setter in one coordinated pass.
4. If Event 012 audio is activated, register IDs 59/60 as sound, wire the corresponding current-audio effect, and update the super-event readiness package together.
5. Keep the Charter GFX comment and asset manifests aligned with the installed 16-texture package; the stale “not fabricated” comment was corrected during the final pass.

## Validation checks

- Re-run a direct event-reference parser over `common/` and `events/`: expect 43 Event 012 IDs, 97 direct references, 43 unique references, and no undefined IDs.
- Re-run helper reference checks: `set_cosmetic_tag` 48/48 resolved, `recruit_character` 9/9 resolved, focus loads 9 occurrences/8 unique resolved, and idea refs 93 occurrences/80 unique resolved.
- Re-run the GFX texture parser over `interface/012_africa*.gfx`: expect 205 texture rows and zero missing runtime paths.
- Re-run the Charter GUI token and sprite check: expect 63 localisation tokens with no missing keys and only the two documented vanilla-only sprite names.
- Re-run the Event 013 call search: expect the Event 012 caller’s single `call_natural_disaster = yes`, action IDs 69/70, and no unresolved direct `chaosx.nr13.*` references in Event 012 files.
- Re-run readiness and audio searches before enabling deferred packages: `africa_world_package_implementation_ready` and `africa_the_world_super_event_package_ready` should not be treated as active until their complete package contracts exist.

## Risks and blockers

### Confirmed active hard blockers

- None found for the active Event 012 event, character, focus, idea, GFX, Charter GUI, cosmetic-tag, flag, or Event 013 caller registrations.

### Safely dormant or deferred references

- The six world-order focus packages and 38 world-order idea packages remain dormant behind `africa_world_package_implementation_ready`; their historical icon rows are not active consumers.
- Super-event audio candidates for IDs 59/60 exist physically but have no registry entries or active Event 012 audio consumer. The terminal world package is explicitly gated by `africa_the_world_super_event_package_ready` and has no default audio fallback.
- The dedicated Event 012 entry proclamation art exists, but the canonical entry currently uses the vanilla African-unity picture. This is a presentation choice, not a load blocker.

## Recommended next action

Use this handoff as the Event 012 registration baseline, then keep the world-order art/audio readiness packages deferred until their complete package contracts are intentionally enabled.
