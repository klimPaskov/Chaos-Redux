# Event 015 Commonwealth Ledger scripted-GUI cleanup

## Scope

The Ledger scripted GUI now uses one country variable, `utopia_manifesto_ledger_tab`, with centralized values in `common/script_constants/015_utopia_manifesto_constants.txt`. Overview, Callings, Stores, and Necessary Ground buttons set that state directly; panel visibility compares the same state, and a missing state falls back to Overview.

The old four-flag tab state was removed from the GUI and from `utopia_manifesto_clear_ledger_runtime`. Tab buttons are enabled only while the Ledger is visible, preventing stale click targets after cleanup.

## Validation evidence

`hoi4_gui_inspect` and `hoi4_gui_render` were run for the Ledger container at 1280x720 and 1920x1080 with normal, hover, selected, warning, long-text, and missing-localisation states. The Event 015 window resolves with 71 inspected elements and complete offline representations. The shared source graph still reports unrelated repository-wide context-type errors and overlap diagnostics from other scripted GUIs; those are outside the Event 015 window and were not modified.

The render comparison remained stable across the requested resolutions. Event 015 source references resolve without a missing tab flag or missing state variable.

## Changed files

- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `interface/015_utopia_manifesto_ledger.gui` (reviewed; no geometry change required)
