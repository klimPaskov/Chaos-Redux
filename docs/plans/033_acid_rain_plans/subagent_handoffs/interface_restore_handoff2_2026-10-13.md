# Event 033 interface restoration handoff

Disposition: implemented in the assigned Event 033 window and presentation read model; parent review and final MCP renders remain outstanding.

## Ownership and acceptance

The owned surface is Event 033, Acid Rain, with the dedicated `acid_rain_world_window` and decision-category `acid_rain_category_inlay` in `interface/033_acid_rain.gui`.

`acid_rain_decisions_scripted_gui` attaches the inlay to the decision category, and `acid_rain_world_scripted_gui` attaches the world window in player context.

The category opener and the Event Details navigation control are the two window entry points; the window remains a read-only presentation surface whose response actions are handled through decisions.

Acceptance is the owner direction in the 13 October restoration task: resolve the Event 033 visual uncertainty in favor of the exact prior composition from `eac05dd94d7530cb1fc056b173fb51da997b5c69`, and preserve the specifically named later features.

The parent clarified during implementation that historical national and phase-clock values must use their original presentation snapshots and helper bridge, not substitute current unrelated values.

This is a restoration from an existing accepted source reference, not a new visual design; the historical `.gui`, scripted GUI effects, and localisation at `eac05dd94d7530cb1fc056b173fb51da997b5c69` are the reference.

The audit disposition appears in `docs/plans/interface_restore_audit_2026-10-13.md`, Event 033 row for `92d525f479d1`.

## Changed files and identifiers

- `interface/033_acid_rain.gui`: restores the inline global ledger, separate transition and dissipation rows, and the national contamination row at their historical coordinates.
- `common/scripted_effects/033_acid_rain_gui_effects.txt`: restores only the historical display snapshots for current global air contamination percent, remaining air allowance percent, transition elapsed days, next dissipation-check days, and country-local contamination percent.
- `localisation/english/033_acid_rain_l_english.yml`: restores the four historical value strings and removes the no-longer-used `acid_rain_world_global_ledger_heading` key; the later breakup string remains wired as a tooltip.
- `common/scripted_guis/033_acid_rain_scripted_guis.txt`: unchanged; its current entry points, guards, regional overlays, exact-ratio fill property, and navigation/effects remain intact.

No gameplay values, contamination effects, decisions, costs, AI, event outcomes, or asset registrations were changed.

## Historical reference and native mapping

The accepted historical root is a fixed `900x600` native window centered with `position = { x = -450 y = -300 }`, `orientation = center`, and `origo = upper_left`.

| Historical/background region | Native IDs and source bounds | Content and interaction | Assets and states |
| --- | --- | --- | --- |
| Header ledger | `acid_rain_world_global_ledger`, `(24,39)`, `790x18` | Four inline global air/added/remaining/deaths facts with the historical contamination tooltip. | Native text over the existing `GFX_tiled_window` board background. |
| World footprint and weather | `acid_rain_map_panel`, `(24,74)`, `560x300`; `acid_rain_front_stack`, `(604,74)`, `272x300`. | Seven region overlays expose hover facts; front cards or the empty-front card occupy the right stack. | Existing map, overlay, veil, front marker, static marker, and card sprites. The later ratio projection and global-layer suppression remain. |
| Global phase card | `acid_rain_global_card`, `(0,25)` inside the right stack, `272x267`; rows at y=39 and y=61. | The historical transition and next-dissipation clocks remain separate. The later breakup date/state remains available on hover over the second row. | Existing `GFX_acid_rain_card_background`; native text and tooltip. |
| Coverage viewport | `acid_rain_coverage_panel`, `(24,390)`, `560x118`. | Exact-ratio track, projected x fill, seven regional rows, and completion marks. | Existing fixed frame/fill assets; no art was added. |
| National strip | `acid_rain_national_strip`, `(24,508)`, `852x44`; restored contamination text at `(45,24)`, `790x14`. | Preparedness, warning/exposure/forecast/aftermath/deaths/saved summaries and current contamination. | Existing transparent tiled strip, preparedness badge, and component pips. The historical row sits 6px above the strip's lower edge. |
| Footer and category opener | World footer controls at y=560; category opener at `(364,54)` in its `500x92` inlay. | Refresh, motion preference, back, Event Details, close/Escape, and open controls remain native and scripted. | Existing `GFX_button_123x34` and `GFX_closebutton`. |

The restored global header line ends at local x=814, leaving 86px before the 900px root edge.

The national contamination row ends at local x=835 inside the strip's x=876 right edge, leaving 41px of horizontal clearance.

The historical two clock rows occupy y=39–57 and y=61–79 in the 267px global card, leaving the storm summary at y=85 unobstructed.

The national contamination snapshot is country-local GUI state exactly as in the historical implementation; its source remains the historical `global.air_contamination_bp` value.

The phase writers read `global.acid_rain_global_transition_day`, `global.acid_rain_global_minimum_dissipation_day`, and `global.acid_rain_next_dissipation_check_day` through the existing `chaosx_convert_date_offset_to_days` helper.

The unchanged runtime source `common/scripted_effects/033_acid_rain_effects.txt` still writes the transition date and next dissipation-check date and reads the same air-contamination basis-point variable; the restored GUI snapshots therefore consume existing state rather than inventing or advancing it.

The current dated-breakup branch remains under `acid_rain_global_card_breakup` on the restored `acid_rain_global_card_window` hover target, preserving the later consequence presentation without replacing either historical clock.

## State, interaction, and budget review

The category inlay and world window are player-only and generation-guarded; the window is visible through formation, regional, global-warning, global, and closed phases while the episode remains valid.

Regional overlays retain their status/touched predicates and are suppressed while the global layer is active; the global layer retains its separate static/animated full-map consumers.

Front slots retain their active visibility and their empty-list alternative; the global storm list retains its three visible records and overflow hint.

The motion preference continues to select animated or static marker/veil consumers, and completed-region marks retain frame 2.

The six native button elements are `acid_rain_category_open`, `acid_rain_world_close`, `acid_rain_world_refresh`, `acid_rain_world_motion`, `acid_rain_world_back`, and `acid_rain_world_details`.

Their scripted effects and enable/visibility triggers remain in the unchanged `common/scripted_guis/033_acid_rain_scripted_guis.txt`; the region overlays are tooltip-bearing icons, not invented click controls.

There are no gameplay actions or spendable costs on this window, so no cost texticons or decision-owner cost/effect review applies to these controls.

The restored historical national strip exposes eight summary readings, plus four preparedness-component pips, and the regional coverage viewport retains its seven records.

That inherited density exceeds the general four-value guidance; the owner explicitly accepted this historical composition for this restoration, so no values or rows were removed to redesign it.

The global ledger itself has four values, and the phase card retains the prior two clock values plus the later breakup tooltip.

## Source checks and visual limitations

The offline wiki section `Scripted GUI modding > Properties`, lines 391–441, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`, documents scripted x/y properties used by the preserved exact-ratio fill.

The offline wiki section `Interface modding > Containers`, lines 73–80, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`, documents independent containers and scripted GUI attachment.

Installed `common/scripted_guis/_documentation.md`, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, was read at lines 1–146 for player-context windows, native effects/triggers, and element properties.

The installed vanilla precedent `game:interface/sov_paranoia_system_scripted_gui.gui`, source revision `68c05772c19b6eab9d2dc0751eae662e5f42f1664796a82f3076071cfc473de9`, lines 1–80, demonstrates an independent container with native child icons, text, and tooltips.

Source geometry places the centered root at `(510,240)` on `1920x1080` scale 1 and `(233,84)` on `1366x768` scale 1; the same fixed 900x600 child bounds fit both canvases with symmetric margins.

Footer button textures are `123x34` at local x=24, 165, 306, and 753; the final button ends at x=876, within the root's 900px width.

The parent explicitly reserved `hoi4.gui_inspect` and `hoi4.gui_render` for its MCP health and final-render pass, so this subagent made no GUI inspect/render calls.

No baseline, intermediate, comparison, hierarchy, click-region, or final-render artifacts are claimed; only the exact historical source and source-derived bounds were reviewed here.

The initial task HEAD was `d9ee328c87fa46af6af6693086e2b6094ebfa31`; it advanced to `e5b1f144c2c69a177249307bb4460c28b551da10` during shared work, with no committed changes to the four Event 033 source paths between those revisions.

The raw pre-edit `.gui` and `.txt` working-tree bytes are preserved as `.tmp/interface_restore_handoff2/event033/033_acid_rain.gui.pre` and `.tmp/interface_restore_handoff2/event033/033_acid_rain_scripted_guis.txt.pre`.

Raw Git-blob pre-edit snapshots of the presentation effects and localisation are preserved as the corresponding `*.pre-head` files under the same ignored task directory.

Current working-tree SHA-256 values are `interface/033_acid_rain.gui` `b5d826cd01d636e6eb348d843c8098e190593c881df7bcf6148c4170ea47fe50`, `common/scripted_guis/033_acid_rain_scripted_guis.txt` `5c0e9bb589ecfb79efc0347b7010d8f762b460c3fd7089cf1a87708f17255125`, `common/scripted_effects/033_acid_rain_gui_effects.txt` `a49997ceeccf7e9ef2f9157928571b41daeb89dfef05ced9b22b97135ff32945`, and `localisation/english/033_acid_rain_l_english.yml` `4703671ba11cdd27d8464518de47107cc3689415822416211807a4cabed09669`.

No game process was launched, and no in-game validation is claimed.

The task-local pre-edit snapshots and temporary source comparisons are under `.tmp/interface_restore_handoff2/event033/` and are excluded from maintained files.

## Remaining parent integration

The parent should run the matched overview, regional hover, list-empty/list-full, global-phase, and footer interaction renders at `1920x1080` and `1366x768`, both at UI scale 1, against the stated historical source baseline and current source hashes.

The parent owns final review and any unresolved renderer diagnostics; the remaining limitation is visual evidence only, not a missing asset or gameplay integration.

No simplifications were made to the assigned restoration; the only adaptation is retaining the later dynamic breakup line as a tooltip on the restored historical clock row.

Skills used: `chaos-redux-scripted-gui` and `chaos-redux-subagents`.

## Parent integration follow-up

The parent restored `acid_rain_gui_contamination_tt` from the exact `eac05dd94` source, preserving its wording while consuming two GUI-only percentage snapshots of `acid_rain_air.lifetime_allowance_bp` and `acid_rain_air.global_ceiling_bp`.
These four arithmetic lines publish existing tuning values and change no contamination limit or outcome.
The restored global deaths line uses the owner’s existing `*1` compact format rather than plain large numbers.
The shared render route timed out after 600 seconds; no pixel or game proof is claimed, and the source windows are assigned to Handoff 1.
