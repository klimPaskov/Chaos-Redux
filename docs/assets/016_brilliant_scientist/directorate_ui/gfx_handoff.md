# Directorate UI GFX handoff

The Event 016 Directorate UI package supplies all 64 texture paths already referenced by `interface/016_brilliant_scientist_directorate.gfx`. Runtime DDS files live in `gfx/interface/016_brilliant_scientist/directorate/` and have the exact dimensions, alpha payloads, button-sheet packing, and animation-sheet frame counts in the binding contract.

Use `manifest.json` for the machine-readable sprite-to-runtime mapping and `validation/row_validation.tsv` for the 64-row decoded DDS proof. Use `contact_sheets/directorate_decoded_runtime_contact.png` and the three animation contact sheets for visual review. The full parent handoff, consumer notes, state semantics, and review checklist are in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_directorate_ui_asset_handoff.md`.

No `.gfx`, `.gui`, gameplay, localisation, or spreadsheet files were changed by this package. The parent agent should keep the existing `.gfx` and `.gui` registrations unchanged and review the generated visual states before final integration.
