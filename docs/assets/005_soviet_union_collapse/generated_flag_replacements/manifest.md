# Event 005 Generated Flag Replacements Manifest

Event id: `005`

Event slug: `soviet_union_collapse`

Asset package: `generated_flag_replacements`

Scope: review-only generated replacement package for user-named ugly/simple-shape Event 005 flags. This pass did not edit active `gfx/flags`, gameplay, localisation, `.gfx`, GUI, focus, decision, event, history, country, or spreadsheet files.

Reference folders inspected:

- `.agents/skills/chaos-redux-event-assets/assets/flags`
- `gfx/flags/`
- `docs/assets/005_soviet_union_collapse/generated_flag_fixes`
- `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction`
- `docs/assets/005_soviet_union_collapse/remaining_custom_flag_correction`

Source mode: generated with Codex built-in `image_gen`.

Why generation is appropriate: `SOG` and its ideology variants are fictional/alternate-history Event 005 flags. They do not represent historical flags or historically attested symbols requiring source research.

## Audit Summary

- Active files exist for every user-named `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, and `KZR` base/ideology flag that is in scope.
- Active normal/medium/small flag dimensions for the named set are present in the standard folders.
- Current active named flags decode upright in the audit contact sheet.
- Existing generated-source coverage was found for `CFR`, `KRS`, `RMC`, `SDZ`, and most of `TSC` under `generated_flag_fixes/source_png`.
- No generated-source package was found for `UDC`, `SOG`, `ALN`, `KHW`, or `KZR` before this pass.

Audit contact sheet:

- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/contact_sheets/audit_active_named_flags.png`

## Completed Review Subset

Each completed asset has source PNG, processed PNG previews, review DDS outputs, and review TGA outputs. Asset status is `needs_user_review` because active game files were intentionally not overwritten.

| Asset | Type | Source PNG | Processed PNGs | Review DDS outputs | Review TGA outputs | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `SOG` | base country flag | `source_png/SOG_source.png` | `processed_png/SOG_<normal\|medium\|small>.png` | `dds/SOG_<normal\|medium\|small>.dds` | `tga/SOG_<normal\|medium\|small>.tga` | `needs_user_review` |
| `SOG_communism` | ideology flag | `source_png/SOG_communism_source.png` | `processed_png/SOG_communism_<normal\|medium\|small>.png` | `dds/SOG_communism_<normal\|medium\|small>.dds` | `tga/SOG_communism_<normal\|medium\|small>.tga` | `needs_user_review` |
| `SOG_democratic` | ideology flag | `source_png/SOG_democratic_source.png` | `processed_png/SOG_democratic_<normal\|medium\|small>.png` | `dds/SOG_democratic_<normal\|medium\|small>.dds` | `tga/SOG_democratic_<normal\|medium\|small>.tga` | `needs_user_review` |
| `SOG_fascism` | ideology flag | `source_png/SOG_fascism_source.png` | `processed_png/SOG_fascism_<normal\|medium\|small>.png` | `dds/SOG_fascism_<normal\|medium\|small>.dds` | `tga/SOG_fascism_<normal\|medium\|small>.tga` | `needs_user_review` |
| `SOG_neutrality` | ideology flag | `source_png/SOG_neutrality_source.png` | `processed_png/SOG_neutrality_<normal\|medium\|small>.png` | `dds/SOG_neutrality_<normal\|medium\|small>.dds` | `tga/SOG_neutrality_<normal\|medium\|small>.tga` | `needs_user_review` |

Prompt log:

- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/prompts/SOG_prompts.md`

Contact sheets:

- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/contact_sheets/SOG_replacement_family_normal_contact_sheet.png`
- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/contact_sheets/SOG_replacement_family_small_contact_sheet.png`

## Orientation And Size Confirmation

- Normal previews and DDS: `82x52`.
- Medium previews and DDS: `41x26`.
- Small previews and DDS: `10x7`.
- Review TGA outputs match the same dimensions.
- The normal-size and small-size contact sheets decode upright. No upside-down or mirrored source was observed in the completed `SOG` subset.

## Blocked Or Deferred Assets

The full user-named replacement scope is larger than one bounded generated-art pass: roughly forty-four individual flag assets when base flags and all ideology variants are counted. This pass therefore completed the `SOG` family only and leaves the following as `planned`/deferred for parent review or a follow-up bounded pass:

- `CFR_communism`, `CFR_democratic`, `CFR_fascism`, `CFR_neutrality`
- `KRS_communism`, `KRS_democratic`, `KRS_fascism`, `KRS_neutrality`
- `RMC_communism`, `RMC_democratic`, `RMC_fascism`, `RMC_neutrality`
- `SDZ_communism`, `SDZ_democratic`, `SDZ_fascism`, `SDZ_neutrality`
- `TSC_communism`, `TSC_democratic`, `TSC_fascism`, `TSC_neutrality`
- `UDC_communism`, `UDC_democratic`, `UDC_fascism`, `UDC_neutrality`
- `ALN`, `ALN_communism`, `ALN_democratic`, `ALN_fascism`, `ALN_neutrality`
- `KHW`, `KHW_communism`, `KHW_democratic`, `KHW_fascism`, `KHW_neutrality`
- `KZR`, `KZR_communism`, `KZR_democratic`, `KZR_fascism`, `KZR_neutrality`

Note: active `CFR`, `KRS`, `RMC`, `SDZ`, and most `TSC` ideology variants already have generated source PNGs in the older `generated_flag_fixes` package. The priority gap after this pass is `UDC`, `ALN`, `KHW`, and `KZR`, plus any explicit redesign request for already sourced variants.
