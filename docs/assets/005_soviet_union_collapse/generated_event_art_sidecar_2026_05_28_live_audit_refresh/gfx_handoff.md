# Event 005 Generated Portrait And Fictional Flag Live Audit Refresh Handoff

Scope: no-regeneration audit refresh for Event 005 fictional portraits and fictional ideology or route flags.

## Final live paths retained

Portraits:

- `gfx/leaders/005_soviet_collapse/*_leader.dds`

Flags:

- `gfx/flags/<TAG>[_<ideology>].tga`
- `gfx/flags/medium/<TAG>[_<ideology>].tga`
- `gfx/flags/small/<TAG>[_<ideology>].tga`

No new `.gfx` sprite definitions are needed from this refresh.

## Keep-as-is determination

Retain the current live files for the bounded Event 005 portrait and fictional flag surface.

Reasons:

- no missing custom portrait DDS file was found in the 32-tag custom Event 005 set
- no custom portrait size defect was found
- no duplicate custom portrait hash group was found
- no missing custom or route flag family member was found
- no flag dimension defect was found
- no exact default override was found for checked existing in-game country tags
- `UKR_BLACK_BANNER` remains a route or cosmetic family only

## Name-pool and identity notes

- `TSC` and `UDC` read as female-presenting one-person portraits and must stay on female personal naming only
- `KRS`, `RMC`, and `SDZ` read as male-presenting one-person portraits and must not use female names or female metadata
- `CFR`, `SOG`, `ALN`, `KHW`, `KZR`, and `OGB` remain institutional or council portraits and must keep institutional naming only

## Review artifacts

- `contact_sheets/priority_portraits_labeled_contact.png`
- `contact_sheets/priority_custom_flags_normal_labeled_contact.png`
- `contact_sheets/ukr_black_banner_route_flags_normal_labeled_contact.png`
- `notes/live_audit.txt`

## Parent-agent note

Do not regenerate or overwrite the current live Event 005 fictional portrait or route-flag files unless a later pass finds a concrete art defect rather than a metadata or documentation issue.
