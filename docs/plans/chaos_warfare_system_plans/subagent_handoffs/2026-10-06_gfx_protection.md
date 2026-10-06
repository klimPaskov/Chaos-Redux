# CBRN protection modifier glyphs

Disposition: implemented, parent accepted within the explicit graphics-repair task.
Five existing dynamic-modifier textures use distinct flat orange/grey symbols at 32x32 instead of oversized 64x64 painted scenes.
Subjects are a tripod alarm bell, civilian shelter arch, medical shield and cross, operating factory and respirator, and emergency supply crates.
All sprite names and existing consumer paths are retained.
The parent reviewed the native and four-times contact sheet and approved promotion after the diffuse background was removed from the generated subjects.
Final DDS decoding matches the approved processed PNGs exactly.

Sources, prompts and before/after previews are retained under `docs/assets/chaos_warfare_system/2026-10-06_gfx_primary/` while the larger package remains active.
Review sheet: `contact_sheets/cbrn_protection_modifiers_native_4x.png`.
Conversion evidence: `notes/protection_runtime_alpha.json`.
The exact final texture hashes are in the adjacent JSON inventory.

The orchestrator should open a state with each protective response active and check that its modifier icon fits the ordinary state-view list, has no glow or clipped background, and matches the named response.
This five-texture tranche does not close the remaining graphics or native cost-row acceptance.
