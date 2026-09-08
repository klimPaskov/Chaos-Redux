# Event 006 status GUI repair — blocked evidence pass

Disposition: **blocked; no runtime source edits**.
Event: `006_independence_wave`.
The parent authorized only the dedicated `independence_wave_status_window` status panel, preserving its five-value design and absolute no-pre-event contract.

## Ownership and accepted scope

The parent selected `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`, its mechanic-presentation section, and `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv` row `ASSET-039` as the accepted repair authority on 2026-09-08.
The spec describes an Event 006 decision-category attachment, five values, relationship cards, secondary tabs, and state-driven cues.
The source identifies `independence_wave_status_scripted_gui`, `context_type = decision_category`, `window_name = independence_wave_status_window`, and `visible = { is_independence_wave_active_country = yes }`.
This proves a dedicated Event 006 surface, not ownership of any shared event log or settings framework.
The concrete owning decision-category identifier and the active-country helper implementation were not traced in this blocked pass.

Allowed runtime files, all left unchanged by this worker:

- `interface/006_independence_wave.gui`
- `interface/006_independence_wave.gfx`
- `common/scripted_guis/006_independence_wave_scripted_gui.txt`
- Existing directly linked Event 006 status localisation, if needed; none was edited.

The parent authorized selecting existing correction references and existing static fallbacks, but no new artwork or gameplay changes.
The prior handoff is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_gui_scale_mcp_retry_2026-09-05.md`.
The parent-provided reference artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b69c93a2569d4392b07bd27e1e37652f29cc4edbbecb1d183e58f5d02b41c284/dccb68f86dfcdf26996e487c0f14214924ede990a5880ad1e02733f6ca4ba415/independence_wave_status_window-full.png`.
That old artifact was not reviewed as an image in this pass and is not a current baseline or completion proof.

## Required MCP route evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Exact window selector: `independence_wave_status_window`.
The first schema probe incorrectly nested `uiScale` in `scenario.resolution` and returned `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.gui_inspect: Unrecognized key: "uiScale" at scenario.resolution`.
The corrected baseline request was:

```json
{
  "workspaceId": "mod_chaos_redux_ea3b2d67c2c0",
  "windowName": "independence_wave_status_window",
  "scenario": {
    "id": "event006_status_repair_baseline",
    "resolution": { "width": 1920, "height": 1080 },
    "uiScale": 1
  },
  "generatedScenarios": { "enabled": false }
}
```

`hoi4.gui_inspect` failed with `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_inspect`, caused by `timed out awaiting tools/call after 180s`.
`hoi4.gui_render` received the same request plus `states: ["normal"]`; its result is pending at this handoff draft.
No new MCP artifact, sourceRevision, hierarchy, click-region, fidelity report, or production image has been returned for review.
Per `chaos-redux-scripted-gui`, missing mandatory inspect/render evidence blocks edits and visual completion; source-only review is not substituted.

## Source-level observations, not visual acceptance

The window is a 700×500 native container with a background, five left-column status values, right-column relationship/phase/mission text, five navigation tabs, and a shared lower text-panel region.
The five tab click effects set their own flag and clear all four sibling flags.
The Government text panel is visible when its flag is set or when none of the four alternative flags is set.
Each other text panel checks its own flag.
Consequently, ordinary tab clicks are mutually exclusive, while externally inconsistent multiple flags could still expose multiple text panels; that is a candidate defensive repair, not a validated cause of the reported production conflict.
The instability icon has its own severe-instability predicate and is not a tab.
It must not be hidden merely to satisfy an incoherent global selected/active fixture.

The source contains four distinct static fallback registrations and corresponding animated siblings:

| Family | Static GFX identifier | Animated GFX identifier |
| --- | --- | --- |
| Recognition | `GFX_independence_wave_recognition_seal_static` | `GFX_independence_wave_recognition_seal_animated` |
| Dependency | `GFX_independence_wave_dependency_warning_static` | `GFX_independence_wave_dependency_warning_animated` |
| League | `GFX_independence_wave_league_charter_activation_static` | `GFX_independence_wave_league_charter_activation_animated` |
| Formable | `GFX_independence_wave_formable_eligibility_seal_static` | `GFX_independence_wave_formable_eligibility_seal_animated` |

The persistent unanimated readout uses each family's `_states` sprite and a live frame property.
The `independence_wave_status_gui_show_animation` flag makes static state-strip controls and animated controls mutually exclusive.
The exact vanilla `interface/alerts.gfx` frameAnimatedSpriteType precedent uses frame count, FPS, looping, play-on-show, transparency, and `gfx/FX/buttonstate_blendframes.lua`; the inspected blocks contain no static-fallback field.
No invented engine field was added and no animated consumer was silently replaced by static artwork.
Fallback registration alone does not prove DDS validity, render resolution, or animation playback; those remain unverified here.

## Source identity and concurrent-work safety

Two SHA-256 samples during this pass matched:

| File | SHA-256 |
| --- | --- |
| `interface/006_independence_wave.gui` | `F0F012733724B03DC535F4975025AF60027CAF1C23591DCAF125BBED44469C94` |
| `interface/006_independence_wave.gfx` | `ED545B4BBF5DCDC08524956D72595B1F74F6322FC0B693CB68F9727E6E4B2119` |
| `common/scripted_guis/006_independence_wave_scripted_gui.txt` | `BA8F9E9DCCFA5B9DBED9B369D9BCC0C427AFBD1646E63BC4D6582F6CEAB4709C` |

Git status reported the scripted-GUI file modified while an immediately following diff returned no hunks.
The parent confirmed no other named worker owned it and instructed conservative handling of concurrent index activity.
This worker neither reset nor rewrote it and did not commit any runtime or unrelated files.

## Remaining acceptance work and omissions

- Mandatory current baseline inspection/render and before/after comparison are absent.
- No correction reference image or completed native-region mapping was produced because the baseline gate failed.
- Full-window, cropped, annotated, hierarchy, click-region, label-centering, text-density, painted-bounds, and reference-fidelity review remain incomplete.
- Explicit coherent Government, Recognition, Security, League, and Ambitions fixtures, warning thresholds, animated/static variants, closed/pre-event state, 1920×1080, and 1280×720 evidence remain pending.
- The prior handoff describes broad/global-state fixtures; it does not provide a reproducible per-tab runtime-input matrix.
- Costs, refresh effects, AI equivalence, source helper lifecycle, no-pre-event runtime behavior, and final decision-category integration remain parent/decision-owner responsibilities and were not changed.
- The accepted panel has five simultaneous mechanic values, conflicting with this worker's current four-value hard ceiling; the panel is preserved, and full contract completion cannot be claimed under that conflict.
- No gameplay-changing action, label, cost, asset, or tab was removed; no fallback, redesign, or simplification was implemented.
- Live-consumer evidence remains outside this worker's pass.

The only file authored by this worker is this blocked handoff.
The scripted-GUI skill and visual-review contract determined the stop; decisions/missions guidance informed the preserved gameplay boundary.
Frame-animation guidance confirmed that animated assets cannot be silently replaced by static art.
Required asset/event guidance and broader reference reading were not completed to implementation readiness after the MCP gate failed; no implementation-readiness claim follows.
