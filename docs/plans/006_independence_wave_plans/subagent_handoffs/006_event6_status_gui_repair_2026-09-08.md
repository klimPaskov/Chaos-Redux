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
`hoi4.gui_render` received the same request plus `states: ["normal"]` and completed as `GUI_RENDERED` with 27 artifacts and no server blockers.
Its exact sourceRevision is `1178ad59092abf8b6378f57b77b83f6c5801bc86f93bd0ebf6f826bf9d170a90`, scenarioId `event006_status_repair_baseline`.
The response reports `validation.passed = true` but also 64 `GUI_VISIBLE_OVERLAP` findings and fidelity counts of 556 modelled, 5 approximated, 15 ignored, 0 missing, 4 unsupported, and 12 unresolved.
It reports one state, one scenario, and four resolution entries; only the explicitly requested 1920×1080 full image was reviewed, so no wider resolution coverage is claimed.
The same-scenario cached `gui_inspect` retry also failed with `timed out awaiting tools/call after 180s`.
There are two failed corrected inspect attempts and one successful baseline render; inspection evidence remains unavailable, so the bounded repair stops here.

Current render artifacts:

- Full PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b69c93a2569d4392d07bd27e1e37652f29cc4edbbecb1d183e58f5d02b41c284/282f1b14a019b038bc4cac04cb658114990d9afe356820f630ddf6439d11a2d5/independence_wave_status_window-full.png`
- Hierarchy: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6ab51bd1a02d1bcc37371410041db872f48ec537d4ffcbc31799ba71b7e9c69/401da573a53b83b56dc62856ce2bfdb5b5478335ba8f0093319448b1635cbfc5/independence_wave_status_window-hierarchy.svg`
- Click regions: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6eb93da154f832d2b6df86dfb764b56b893af485e1ce1e537e5135601b85f24/0ee20007e5c5fe552dcad978d51d3fea39a1f9db4a1774847ca758fc2c3e7143/independence_wave_status_window-click-regions.png`
- Fidelity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85d50111a5225411f583b688d9e33a1bb67053e92d3e9bf4e1405e0cd6c1636d/ab957634c94fa6da1a9bb9097541925ac9bb51fe309bf10f18b790433e679478/independence_wave_status_window-fidelity.json`
- Validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf5a982f9a7afaa664cabb8d5b04ef50c5b5a731e2eeda09bcbce6419d9e5d89/362e30c4450fa3d894241ce44b9e90d365043600cb1943754b4e86507ed83acd/independence_wave_status_window-validation.json`

The complete PNG was retrieved through the artifact resource's documented byte-range selectors in 24,000-byte chunks after a single large resource response could not be decoded.
The actual full image was reviewed: the bottom-right native tab text panels visibly overprint one another, dynamic values display `[X]`/`[dynamic_loc]`, and the instability warning touches the unresolved instability text.
These are visibly unacceptable findings in the current baseline, not waived by its passing validation boolean.
The scenario declares no runtime flags, numeric values, or dynamic localisation substitutions; a coherent per-tab fixture is still necessary to distinguish exact state evaluation from source defects.
No post-change render or matched source comparison exists because no runtime source was changed.
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

- Mandatory current baseline inspection and before/after comparison are absent; one normal baseline render exists and has visible defects.
- No correction reference image or completed native-region mapping was produced because the baseline gate failed.
- Full-window review found overprinted tab text and unresolved values; cropped, annotated, hierarchy, click-region, label-centering, text-density, painted-bounds, and reference-fidelity review remain incomplete.
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
