# Event 006 localisation runtime repair

Date: 2026-07-25

Scope: parent-owned follow-up to the read-only localisation audit.

## Repairs

- `localisation/english/006_independence_wave_scenario_l_english.yml` now reports the canonical SCN-008 split of 138 selectable packages with unique current-map bindings, 55 selectable packages without a unique binding, and 13 non-selectable route overlays.
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt` now defines `GetIndependenceWaveLeaguePhase` for all thirteen researched league phases plus an unresolved fallback.
- `localisation/english/006_independence_wave_gui_l_english.yml` now renders the named phase getter instead of exposing the raw global phase integer and contains the matching phase labels.
- The authoritative source map, resume packet, and Event 006 document now describe ASSET-040 through ASSET-043 as produced semantic frame packages and describe the current IW-006 admission correctly.

## Validation

- All three edited localisation YAML files remain UTF-8 with BOM.
- Targeted GUI inspection returned `GUI_INSPECTED` and targeted rendering returned `GUI_RENDERED` for `independence_wave_status_window` at 1280x720 and 1920x1080 across normal, warning, active, and long-text states.
- The GUI tool still reports the repository-wide diagnostic ceiling and unrelated global context errors, so this is targeted evidence rather than a global GUI pass.
- No game process was launched and no live scenario execution was claimed.
