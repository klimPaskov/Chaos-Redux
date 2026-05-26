# Event 005 Generated Flag and Portrait Current Audit Handoff - 2026-05-26

Scope: `chaosx_generated_event_art` bounded audit for Event 005 Soviet Collapse leader/council/factory portraits and the user-named flag families `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, `KZR`, plus `OGB` orientation state.

## Completed Work

- Audited the live Event 005 leader portrait references from `interface/005_soviet_collapse*.gfx`.
- Audited live normal, medium, and small TGA outputs for the scoped flag families.
- Created a sidecar manifest, validation ledgers, and contact sheets.
- Confirmed that no new generated-art replacement batch is needed for the scoped surface.

Sidecar manifest:

- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_flag_portrait_current_audit/manifest.md`

Validation ledgers:

- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_flag_portrait_current_audit/notes/named_flag_tga_header_audit.tsv`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_flag_portrait_current_audit/notes/named_flag_family_uniqueness.tsv`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_flag_portrait_current_audit/notes/referenced_leader_portrait_audit.tsv`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_flag_portrait_current_audit/notes/existing_country_default_flag_override_check.tsv`

Contact sheets:

- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_flag_portrait_current_audit/contact_sheets/named_flags_normal_contact.png`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_flag_portrait_current_audit/contact_sheets/named_flags_medium_scaled_contact.png`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_flag_portrait_current_audit/contact_sheets/named_flags_small_scaled_contact.png`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_flag_portrait_current_audit/contact_sheets/referenced_leader_portraits_contact.png`

## Asset Changes

No TGA, DDS, source PNG, processed PNG, gameplay, localisation, `.gfx`, GUI, event, focus, country/history, script, or spreadsheet files were edited.

No `$imagegen` call was made because the current scoped portrait and flag surface already passes the audit. Creating new art would have overwritten accepted assets without a remaining missing/broken target.

## Validation Results

Flags:

- scoped families: `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, `KZR`, `OGB`
- checked variants per family: base, `_communism`, `_democratic`, `_fascism`, `_neutrality`
- all normal flags are `82x52`, type `2`, 32 bpp, descriptor `0x08`
- all medium flags are `41x26`, type `2`, 32 bpp, descriptor `0x08`
- all small flags are `10x7`, type `2`, 32 bpp, descriptor `0x08`
- every scoped same-tag family has `5/5` unique hashes at normal, medium, and small size
- contact sheets render the scoped flags upright; no upside-down or mirrored family was observed

Portraits:

- referenced Event 005 leader portrait DDS files checked: `37`
- missing referenced portraits: `0`
- checked portrait dimensions: all `156x210`
- duplicate checked portrait hashes: `0`
- vanilla leader DDS hash matches: `0`

Existing-country base flag rule:

- no mod-side default flag overrides were found for the vanilla-supported ordinary/internal country tags checked in the sidecar manifest
- no existing-country base flag was created or changed

## Blockers and Uncertainty

No generated-fictional/council/factory portrait or fictional flag variant remains safely actionable in this scoped pass.

Historical or real assets were not generated. If the parent rejects a historical/restoration flag or asks for a real leader portrait, that should be routed to `chaosx_asset_source_researcher` rather than substituted by generated art.
