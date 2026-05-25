# Event 005 Generated Event Art Sidecar Manifest

Audit date: 2026-05-25

Scope: read-only asset sidecar for active Event 005 Soviet Collapse leader/council portraits and custom/cosmetic flags. This folder is review evidence only. It does not contain final replacement assets and does not overwrite active dirty flag files.

## Source And Reference Checks

- Repo guidance: `AGENTS.md`
- Skill guidance: `.agents/skills/chaos-redux-event-assets/SKILL.md`
- Image generation skill: `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- Flag references: `.agents/skills/chaos-redux-event-assets/assets/flags/`
- Active portrait sprite sources: `interface/005_soviet_collapse_custom_icons.gfx`, `interface/005_soviet_collapse_factory_ancient_icons.gfx`
- Active custom tags: `common/country_tags/chaosx_countries.txt`
- Prior Event 005 asset evidence: `docs/assets/005_soviet_union_collapse/manifest.md`, `docs/assets/005_soviet_union_collapse/visual_asset_sidecar_2026_05_24/`
- Vanilla comparison: `/home/klim/projects/Hearts of Iron IV/gfx/flags/small/SOV.tga`

The offline Paradox wiki core pages and vanilla documentation were consulted for repository compliance. The wiki snapshot does not contain an `Effects - Hearts of Iron 4 Wiki.md` page by that filename, so vanilla `effects_documentation.md` was used for effects reference. No script or gameplay change was made.

## Portrait Audit Entry

- Asset type: leader/council portraits
- Related event: Event 005 Soviet Collapse
- Source mode: existing generated/source assets already wired
- Active sprite count checked: 37
- Missing DDS files: 0
- Bad dimensions: 0
- Duplicate active portrait hashes: 0
- Expected size: 156x210
- Final folder checked: `gfx/leaders/005_soviet_collapse/`
- Status: `complete`

No missing unique leader or council portrait was found in the active wired portrait scope.

## Flag Audit Entry

- Asset type: country and route/cosmetic flags
- Related event: Event 005 Soviet Collapse
- Active flag scope: 32 custom Event 005 tags plus `UKR_BLACK_BANNER`
- Variants checked: base, `_communism`, `_democratic`, `_fascism`, `_neutrality`
- Sizes checked: normal 82x52, medium 41x26, small 10x7
- Missing files: 0
- Duplicate hashes: 0
- Normal TGA issues: 0
- Medium TGA issues: 0
- Small TGA issues: 50
- Status: `needs_user_review`

The small flag files for `CFR`, `KZR`, `SOG`, `KHW`, `ALN`, `KRS`, `RMC`, `UDC`, `SDZ`, and `TSC` are present and visually inspectable, but their current TGA encoding differs from the vanilla-compatible pattern used by clean active flags.

Current issue pattern:

- Problem files are `10x7`, but are 8-bit color-mapped TGAs with descriptor `0x00`.
- Vanilla `small/SOV.tga` and clean active small flags such as `UKR_BLACK_BANNER` and `FTH` are 32bpp RGBA TGAs with descriptor `0x08`.
- The corresponding normal and medium files for the same tags are 32bpp with descriptor `0x08`.

Problem file list: `audit/problem_small_flags.txt`

Contact sheet: `contact_sheets/problem_small_flags_current.png`

## Generation Decision

No `$imagegen` generation was run.

Reason: the audit did not find missing or non-unique source art. The remaining issue is a final TGA conversion/export problem on active dirty small flag files. Re-exporting those files in place would overwrite active dirty flag files, which the prompt explicitly forbids.

## Replacement Need

Generated replacement art is not currently required for portraits or flags. A non-overlapping follow-up can regenerate review-only small-flag candidates from the existing normal/medium/source art if the parent wants a ready replacement package, but the active dirty `gfx/flags/small/*.tga` files should not be overwritten by this sidecar.

## Blockers And Uncertainty

- Blocker for this subagent: active dirty small flag files cannot be overwritten.
- Uncertainty: I did not visually classify the 50 small flags as upside-down because their descriptor and bpp are already enough to mark them as export-problematic against the vanilla and clean-active pattern.
- Out of scope: gameplay, localisation, focus, decision, interface, country/history, and spreadsheet files were not edited.
