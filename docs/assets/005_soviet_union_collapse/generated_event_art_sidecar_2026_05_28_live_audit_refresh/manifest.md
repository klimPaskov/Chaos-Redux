# Event 005 Generated Portrait And Fictional Flag Live Audit Refresh

Date: 2026-05-28

Event id: `005`

Event slug: `soviet_union_collapse`

Package: `generated_event_art_sidecar_2026_05_28_live_audit_refresh`

Scope: bounded asset-only audit of Event 005 fictional/symbolic leader portraits and fictional ideology or route flags. This refresh does not edit gameplay, localisation, `.gfx`, GUI, event, focus, decision, history, country, or spreadsheet files. No live DDS or TGA asset was regenerated or overwritten in this pass.

## Source mode

Audit-only refresh.

Why no new generation was appropriate:

- current live custom portrait DDS coverage is complete for the Event 005 custom-tag surface
- current live fictional custom-flag and route-flag families are present in all required sizes
- the current scoped live outputs do not expose a concrete missing file, duplicate-hash failure, wrong-size export, upside-down reviewed output, or obvious recolor-only ideology family that would justify regeneration
- the user explicitly asked that acceptable live assets be documented rather than replaced

## References inspected

- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `gfx/leaders/005_soviet_collapse/`
- `gfx/flags/`
- `gfx/flags/medium/`
- `gfx/flags/small/`
- `docs/assets/005_soviet_union_collapse/manifest.md`
- `docs/assets/005_soviet_union_collapse/gfx_handoff.md`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_28_goal_resume/`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_28_ogb_orientation_followup/`
- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_country_portrait_flag_source_audit_current.md`
- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_flag_portrait_sidecar_audit_noop.md`
- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_generated_portrait_flag_gap_check_noop.md`

## Live audit summary

- Custom Event 005 portrait DDS files checked: `32`
- Missing custom portrait DDS files: `0`
- Custom portrait DDS files with non-`156x210` size: `0`
- Duplicate custom portrait DDS hash groups in the scoped custom-tag set: `0`
- Custom and route flag files missing across normal, medium, and small families: `0`
- Flag files with wrong HOI4 dimensions: `0`
- Duplicate normal-size ideology or route hash groups inside the scoped families: `0`
- Exact default mod-side flag overrides for checked existing in-game countries: `0`
- Explicit route-flag files for `UKR_BLACK_BANNER`: `15`

Direct audit output is stored in:

- `notes/live_audit.txt`

## Visual review artifacts

Current review contact sheets created in this refresh:

- `contact_sheets/priority_portraits_labeled_contact.png`
- `contact_sheets/priority_custom_flags_normal_labeled_contact.png`
- `contact_sheets/ukr_black_banner_route_flags_normal_labeled_contact.png`

These are review artifacts only. They do not replace the live gameplay files.

## Priority portrait evidence

The current live portraits remain acceptable for the tags most likely to cause name-pool or institutional-name mistakes:

- `CFR`: institutional portrait, no personal random-name pool
- `KRS`: male-presenting one-person portrait
- `RMC`: male-presenting one-person portrait
- `SDZ`: male-presenting one-person portrait
- `TSC`: female-presenting one-person portrait
- `UDC`: female-presenting one-person portrait
- `SOG`: institutional or council portrait
- `ALN`: institutional or council portrait
- `KHW`: institutional or council portrait
- `KZR`: institutional or council portrait
- `OGB`: institutional or council portrait

Required implementation constraint preserved by this audit:

- female-presenting one-person portraits must only use female naming and female leader metadata where supported
- male-presenting one-person portraits must not use female naming or female metadata
- council, board, office, and institutional portraits must keep institutional names and must not use personal random-name pools

Existing source and final evidence for these portraits already exists at stable paths:

- source PNG examples: `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_28_goal_resume/source/*_leader_source.png`
- processed PNG examples: `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_28_goal_resume/processed/*_leader.png`
- final DDS paths: `gfx/leaders/005_soviet_collapse/*_leader.dds`

## Fictional custom and route flag evidence

The current live fictional ideology and route flag families remain acceptable in scope:

- custom ideology families reviewed visually in this refresh: `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`
- historical-restoration fictional families reviewed visually in this refresh: `ALN`, `KHW`, `KZR`, `OGB`, `SOG`
- route family reviewed visually in this refresh: `UKR_BLACK_BANNER`

Why they were kept:

- each reviewed family has a complete normal, medium, and small file set
- the reviewed normal-size variants read as distinct designs rather than straight recolors or flipped copies
- no current reviewed output presented an obvious orientation defect
- `UKR_BLACK_BANNER` remains a separate route or cosmetic family, not a base `UKR` override

Existing source and final evidence already exists at stable paths:

- generated custom ideology sources: `docs/assets/005_soviet_union_collapse/source_png/generated_custom_ideology_flags/`
- historical-restoration sources: `docs/assets/005_soviet_union_collapse/source_png/historical_flags/`
- `UKR_BLACK_BANNER` base source: `docs/assets/005_soviet_union_collapse/remaining_custom_flag_correction/source_png/UKR_BLACK_BANNER_base_source.png`
- live final TGA paths: `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`

## Result

No new generated asset package was needed. The live Event 005 fictional portrait and fictional ideology or route flag surface is acceptable for this bounded sidecar scope, so this refresh records evidence instead of replacing valid art.
