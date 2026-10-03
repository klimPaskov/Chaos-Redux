# CSH Native Flag Package Review

Disposition: The requested native flag package is present and passes file, encoding, alias-coverage, orientation, and preview comparisons. Current in-game lookup behavior remains pending the user's post-repair live QA.

Review scope is limited to the CSH native flag repair and confirmation that the country and history sources remain outside the asset change. This is not a full country-package audit.

## Accepted scope and result

The user's 2026-10-03 13:20 live-QA report identified missing `CSH_democratic` and `CSH_neutrality` lookups in all three native flag folders during load and on 1 January 1936 after `cab3acb5b`. The accepted correction uses direct native filenames for the default flag and four ideology aliases, with one shared institutional design because CSH is the stateless internal Scientific Office.

All 15 expected files now exist: `CSH.tga`, `CSH_democratic.tga`, `CSH_neutrality.tga`, `CSH_fascism.tga`, and `CSH_communism.tga` in each of `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`. This closes the static filename and size coverage gap reported for the package.

| Runtime folder | Required size | Files verified |
| --- | --- | --- |
| `gfx/flags/` | 82x52 | `CSH.tga`, `CSH_democratic.tga`, `CSH_neutrality.tga`, `CSH_fascism.tga`, `CSH_communism.tga` |
| `gfx/flags/medium/` | 41x26 | `CSH.tga`, `CSH_democratic.tga`, `CSH_neutrality.tga`, `CSH_fascism.tga`, `CSH_communism.tga` |
| `gfx/flags/small/` | 10x7 | `CSH.tga`, `CSH_democratic.tga`, `CSH_neutrality.tga`, `CSH_fascism.tga`, `CSH_communism.tga` |

## Asset checks

I checked every header and payload. All 15 files are uncompressed TGA image type 2, have no color map, use 32-bit BGRA pixels, descriptor `0x08` with bottom-left origin, and have alpha 255 throughout. Their exact sizes are 17,074 bytes at 82x52, 4,282 bytes at 41x26, and 298 bytes at 10x7; each file length equals its 18-byte header plus the expected pixel payload.

For each file I manually normalized the bottom-left row order and BGRA channels, then compared the decoded pixels against its matching processed PNG. All 15 comparisons matched exactly. The five filenames in each size tier are byte-identical, as specified for this nonpolitical office identity. The contact sheet also shows the selected master and the normal, medium, and native-size small outputs; the flask and centered layout remain legible at the smallest size.

The manifest records the selected master at `docs/assets/cbrn_scientist_holder_flags/source_png/csh_scientific_office_master.png` (SHA-256 `403d2e09062825a33d36bdf09b77e0877ffc63e5e2fc2e3a66d5415391f83652`), the per-filename processed PNG previews, and runtime hashes. The shared runtime hashes are `8905a5cfaa1fe23c2cefba4ce3e8c2d6d206559b3ab8e6859c12ad2e952d776f` for normal, `5511bd6cdb8c7073fedec9b08ae1c596c01d7d3895c9fa917b94475341c7a734` for medium, and `19ef01e4eaae2569639c859db738c4a7beb6a8a27cd95df777b6a68615f8dfe8` for small.

The design evidence is in `docs/assets/cbrn_scientist_holder_flags/manifest.md`, `prompts/csh_scientific_office_flag.md`, and `contact_sheets/csh_flags_master_and_sizes.png`. The intentional shared ideology aliases are documented in the manifest.

## Country source and lookup contract

`common/country_tags/cbrn_scientist_holder.txt:2` registers `CSH` to `countries/CBRN Scientist Holder.txt`. `history/countries/CSH - Scientist Registry.txt:1` describes the internal holder as owning no state or core. The country tag, country definition, country history, scientist recruitment history, and startup history-effect owner were not changed in this flag repair. The country and history files were clean in the scoped worktree status check.

The current SHA-256 values for `common/scripted_effects/chaosx_startup_history_effects.txt` and `history/general/chaosx_startup_character_recruitment.txt` match the values in `docs/testing/2026-10-03_csh_flag_load_repair/scientist_source_check.json`. That record reports zero runtime recruitment commands in the startup owner and retains guarded CSH-origin transfers for Haldane, Fishman, and Velikanov. The recorded history recruitment locations are lines 93, 109, and 108 respectively.

A CSH-specific source-text search found no `.gfx`/`.gui` flag registration, cosmetic-tag route, or explicit flag-path override. The repair follows native tag-and-ideology filename lookup. The offline country-creation reference, `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md`, lines 461-480 (revision SHA-256 `0c0e57915a7d1eef9ddeebe91c7329e18f4f224af98ac33fac5edd35e3aaa35d`), documents filename-based selection, uncompressed 32-bit TGA, bottom-left origin, and the three dimensions. Installed `common/defines/00_graphics.lua`, lines 938-945 (SHA-256 `dfdab0a5fad7319d7b5ac524d98af49d3a0c1f95772e6b7a76abce54836f3d86`), gives the matching dimensions. Repository KRG examples use type 2, 32 bpp, descriptor 8 across the three sizes; installed `gfx/flags/small/USA.tga` is also type 2 and 32 bpp with bottom-left origin and 10x7 dimensions.

## Country-package checklist and remaining validation

- Tag and native aliases: covered for `CSH`, the default name, and all four ideology suffixes in all three runtime folders.
- Map and state setup: no map edit was made; the CSH history source and the accepted stateless-holder scope are unchanged.
- Politics, leaders, portraits, advisors, parties, focuses, decisions, ideas, military, technology, industry, supply, AI, and playability: outside this flag-only review; no full package audit is claimed.
- Missing or stale flag assets: none remain in the static 15-file package checked here.
- Simplifications in this asset scope: none. The same design across ideology aliases is an explicit accepted identity choice.
- Runtime validation: pending. File presence and format do not establish that HOI4 has completed the lookup without warnings after the repair. No fresh warning-absence claim is made; the user owns live-game validation.

This review wrote only `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-03_csh_flag_package_review.md`; it made no gameplay or asset edits, staged no files, and created no commit.
