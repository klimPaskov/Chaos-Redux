# Event 005 Flag and Portrait Current Audit

Date: 2026-05-26

Scope: bounded generated-event-art sidecar audit for Event 005 Soviet Collapse leader/council/factory portraits and the user-named flag families `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, `KZR`, plus `OGB` orientation state.

No gameplay, localisation, `.gfx`, GUI, event, focus, country/history, script, or spreadsheet files were edited. No flag, portrait, DDS, or TGA asset file was changed in this pass.

## References Inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `interface/005_soviet_collapse_custom_icons.gfx`
- `interface/005_soviet_collapse_factory_ancient_icons.gfx`
- live files under `gfx/leaders/005_soviet_collapse/`
- live files under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`
- prior Event 005 generated asset and small-flag export handoffs under `docs/assets/005_soviet_union_collapse/`

The required offline wiki core pages and vanilla documentation entry points were consulted before writing this handoff. They did not change the asset-only outcome.

## Source Mode

No new source image was created. The current live surface already contains completed generated-fictional and sourced/historical-restoration assets, so no `$imagegen` call was made.

Generation remains appropriate only for fictional/council/factory portraits and fictional custom/route flag variants. Historical or real flags and real leader portraits remain blocked for this generated-art route and should go to source research if the current approved source assets are rejected.

## Flag Audit

Checked families:

- `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`
- `SOG`, `ALN`, `KHW`, `KZR`
- `OGB`

For each family, the base flag plus `_communism`, `_democratic`, `_fascism`, and `_neutrality` variants were checked at normal, medium, and small sizes.

Results:

- all scoped normal flags exist at `82x52`
- all scoped medium flags exist at `41x26`
- all scoped small flags exist at `10x7`
- all scoped TGAs are type `2`, 32 bpp, descriptor `0x08`
- every scoped same-tag family has `5/5` unique hashes at normal, medium, and small size
- `OGB` normal/medium/small outputs are present, unique by variant, and use the same valid header/origin pattern as the rest of the scoped set
- no upside-down or mirrored scoped flag was observed on the generated contact sheets

Validation files:

- `notes/named_flag_tga_header_audit.tsv`
- `notes/named_flag_family_uniqueness.tsv`
- `notes/existing_country_default_flag_override_check.tsv`

Contact sheets:

- `contact_sheets/named_flags_normal_contact.png`
- `contact_sheets/named_flags_medium_scaled_contact.png`
- `contact_sheets/named_flags_small_scaled_contact.png`

## Portrait Audit

Checked active Event 005 leader portrait references from `interface/005_soviet_collapse*.gfx`.

Results:

- referenced Event 005 leader portrait files checked: `37`
- missing referenced portrait files: `0`
- all checked portrait DDS files are `156x210`
- duplicate checked portrait hashes: `0`
- vanilla leader DDS hash matches: `0`

Validation file:

- `notes/referenced_leader_portrait_audit.tsv`

Contact sheet:

- `contact_sheets/referenced_leader_portraits_contact.png`

## Existing-Country Base Flag Rule

The exact default override check for vanilla-supported ordinary/internal tags found no mod-side default flag override files for:

`UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`.

No base flag for an existing-game country was created or changed.

## Produced Assets

No new generated source PNG, processed PNG, DDS, or TGA gameplay asset was produced in this pass. The sidecar produced only audit artifacts and contact sheets.

## Blockers and Uncertainty

No safe generated-art asset remains missing or broken in the scoped surface.

If a future request asks for new real leader portraits, historical flags, or historically attested symbols, this generated-art route should mark those as blocked and route them to source research instead of generating substitutes.
