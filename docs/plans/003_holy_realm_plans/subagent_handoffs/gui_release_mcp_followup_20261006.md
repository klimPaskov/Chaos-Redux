# Event003 Mandala GUI MCP Evidence Follow-up

Disposition: unresolved. The parent requested exactly one current-source inspect and one matched render of the existing Event003 Mandala category container after promoting the real-frame asset package and applying the accepted tab-filtering source. Both requested calls returned `Transport closed`, so neither an after-inspect revision nor a render artifact exists. I made no retry and no source edits.

## Scope and Current Source

The inspected identifier was `holy_realm_mandala_category_container`, bound by `holy_realm_mandala_category_scripted_gui` in `common/scripted_guis/003_holy_realm_scripted_guis.txt` and attached to Event003's `holy_realm_mandala_category`. The existing five buttons and the approved 470x560 panel are unchanged from the previously reviewed owned block. A bounded block comparison against `gui_release_20261005_evidence/gui_mandala_container.after.gui` confirmed the current owned GUI block still matches; the full `interface/chaosx_decisions.gui` hash differs because the shared file contains other agents' work outside this block. No shared or unrelated UI block was inspected or edited.

The parent reports that 14 real Mandala DDS files were promoted under package identifier `4dfdc7c7`, the Refuge default button cue was fixed, and accepted G4 source cleanup was committed as `ce0`. The parent also reports the separate tab-filtering source handoff at `docs/plans/003_holy_realm_plans/subagent_handoffs/mandala_tab_filtering_20261006.md`; its post-filter integration remains parent-owned. This follow-up only records the requested GUI route calls and preserves those changes.

Current source hashes captured immediately before the two calls are:

| Path | SHA-256 |
| --- | --- |
| `interface/chaosx_decisions.gui` | `1EE91999E3552D929B0C823041000E478DC1432B9AA9B27D5F4C7E147405CA0F` |
| `common/scripted_localisation/003_holy_realm_scripted_localisation.txt` | `EF690E66ACA2F30088BA1C4F80CF95A6E0C078CA608ECEC5314EB3D18B9C5A1C` |
| `localisation/english/003_the_holy_realm_l_english.yml` | `A2AEBC312C760A4E06336ACFC4D51A60B23C8CDEA3D0E678992FEB6E8E732B23` |
| `interface/003_holy_realm.gfx` | `DBA73B7BBFDECD3866756FC8320B51CB238CC163E88CEF667ED13B1033C5E8FD` |
| `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_dormant_animated.dds` | `932B23CCF9707B0CFA462396C46FD9775585A5B85741272AE8A85C21A9A00B0C` |

The scripted GUI still selects the active animation through `GetHolyRealmMandalaSprite`; the `.gui` base sprite remains the static dormant fallback. The current rendered-state fixture's scripted sprite accessor was set to `GFX_holy_realm_mandala_dormant_animated`, which is the source-selected state when no later-stage, meditation, teaching, awakened, wrathful, Final Silence, or Empty Seat flags are present. The renderer call did not return, so actual image consumption is not claimed.

## Matched Refuge Fixture

Both tool requests used scenario id `evt003_tib_refuge_default_no_other_tabs_20261006`, TIB on 1936.1.1, `l_english`, 1920x1080, UI scale 1, and `generatedScenarios.enabled = false`. Its only country flag is `holy_realm_active`; no Mandala tab flags are set, exercising the default Refuge state. Per-control states set only `holy_realm_panel_tab_refuge_button` to selected and the other four buttons to normal.

The fixture values are source-derived from the existing TIB Refuge setup: Spiritual Legitimacy 55, Compassion Drift 0, Mandala Reach 35, Final Silence Pressure 0, doctrine rigidity 10, Bodhi 0, Dhyana 0, teaching successes 0, Meditation Charge 20, Defilements 45, Sangha Cohesion 55, and global Chaos 0. Display-bound preview variables use the initialized source constants: Bodhi maximum 108, Dhyana maximum 4, and required teaching successes 12.

The explicit scripted-localisation accessors match the current source and full English localization output: the active Mandala sprite is `GFX_holy_realm_mandala_dormant_animated`; the primary line is `§GSpiritual Legitimacy§!: §Y55§!`; the secondary line is `§CCompassion Drift§!: §Y0§!  §CSangha Cohesion§!: §Y55§!`; the risk line is one space; the selected Refuge label is `> Refuge`; other button labels are `Arhats`, `Diplomacy`, `Doctrine`, and `Alert`; the stage is `Mountain Refuge`; the doctrine is `Doctrine: Unsettled`; and the Refuge body is `Families cross the passes seeking safety. The Realm can shelter them, count them, or close the roads and preserve its stores.` These are exact source strings with the fixture's bound values substituted.

## One Inspect Attempt

The sole current-source `hoi4.gui_inspect` call used the exact window identifier, workspace `mod_chaos_redux_ea3b2d67c2c0`, and the matched Refuge fixture above. It returned:

```text
tool call error: tool call failed for `hoi4_agent_tools/hoi4.gui_inspect`

Caused by:
    Transport closed
```

No structured inspect result, diagnostic list, artifact, or source revision was returned. The complete request and error are recorded in `gui_release_20261005_evidence/gui_inspect_after_refuge_no_other_tabs_20261006.json`.

## One Render Attempt

The sole current-source `hoi4.gui_render` call used the identical fixture and window, with `states = ["normal"]` and one resolution entry at 1920x1080, UI scale 1. The per-control element-state map still selected only Refuge. It returned:

```text
tool call error: tool call failed for `hoi4_agent_tools/hoi4.gui_render`

Caused by:
    Transport closed
```

No full, cropped, annotated, hierarchy, click-region, validation, or comparison artifact was returned, so there was no image to review or post-render defect check to complete. The complete request and error are recorded in `gui_release_20261005_evidence/gui_render_after_refuge_no_other_tabs_20261006.json`.

## Handoff Limits

This follow-up does not claim post-filter visual acceptance, current engine diagnostics, asset-image correctness, or in-game completion. No source, GUI layout, scripted-GUI binding, localization, gameplay, or asset file was changed. The parent retains integration and review of the source tab filtering and asset package. The GUI evidence blocker is the MCP transport failure on both single attempts; no retry was made, as requested.
