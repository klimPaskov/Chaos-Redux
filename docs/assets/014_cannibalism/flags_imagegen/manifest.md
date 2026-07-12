# Event 014 Cannibalism Flag Asset Manifest

## Scope

This package implements the frozen flag ledger at `docs/plans/014_cannibalism_plans/014_flag_asset_frozen_ledger.md`.

- Families: 13
- Generated compositions: 65
- Live TGA files: 195
- Variants per family: base, communism, democratic, fascism, neutrality
- Sizes: 82x52, 41x26, 10x7
- Source mode: fictional artwork generated with the built-in `image_gen` tool
- Final format: uncompressed 32-bit TGA, bottom-left origin, opaque alpha
- Status: complete

The row-by-row machine-readable manifest is `asset_manifest.tsv`. It lists every one of the 65 compositions and its source sheet, source crop, three processed PNGs, three live TGAs, and prompt ledger.

## Package paths

- Exact prompt and generation provenance: `prompts/imagegen_prompt_ledger.md`
- Generated source sheets: `source_sheets/`
- Selected high-resolution source crops: `source_crops/`
- Processed PNGs: `processed_png/82x52/`, `processed_png/41x26/`, `processed_png/10x7/`
- TGA-decoded contact sheets: `contact_sheets/`
- Mechanical validation and hashes: `validation/`
- Reproducible crop/export/validation helper: `process_event014_flags.py`

## Live placement

- Standard: `gfx/flags/<asset_stem>.tga`
- Medium: `gfx/flags/medium/<asset_stem>.tga`
- Small: `gfx/flags/small/<asset_stem>.tga`

Each family uses these five filename stems:

| Variant | Stem form | Composition language |
|---|---|---|
| Base | `<family>` | ideology-neutral form |
| Communism | `<family>_communism` | multiple objects converge into collective command |
| Democratic | `<family>_democratic` | open, defensive, or outward-facing civic resistance |
| Fascism | `<family>_fascism` | rigid vertical alignment and militarized control |
| Neutrality | `<family>_neutrality` | lone, oversized, off-balance warlord dominance |

## Family coverage

| Family | Required motif | Five distinct live stems |
|---|---|---|
| `CBA` | island reef, hooked blade, torn convoy rope, red surf | `CBA`, `CBA_communism`, `CBA_democratic`, `CBA_fascism`, `CBA_neutrality` |
| `CBB` | black lighthouse, jaw harbor, signal lamp, broken chain | `CBB`, `CBB_communism`, `CBB_democratic`, `CBB_fascism`, `CBB_neutrality` |
| `CBC` | breached wall, ration bowl, siege stakes, blood-marked masonry | `CBC`, `CBC_communism`, `CBC_democratic`, `CBC_fascism`, `CBC_neutrality` |
| `CBD` | tunnel lamp, chained gate, buried knives, collapsed arch | `CBD`, `CBD_communism`, `CBD_democratic`, `CBD_fascism`, `CBD_neutrality` |
| `CBE` | wagon wheel, marching blade, blank field-map scraps, muddy track | `CBE`, `CBE_communism`, `CBE_democratic`, `CBE_fascism`, `CBE_neutrality` |
| `CBF` | rail spike, horse jaw, depot flame, broken transport rail | `CBF`, `CBF_communism`, `CBF_democratic`, `CBF_fascism`, `CBF_neutrality` |
| `CBG` | barred iron mouth, key, prison tower, torn blank ledger | `CBG`, `CBG_communism`, `CBG_democratic`, `CBG_fascism`, `CBG_neutrality` |
| `CBH` | armored gauntlet, shackles, transport gate, blank file blot, broken baton | `CBH`, `CBH_communism`, `CBH_democratic`, `CBH_fascism`, `CBH_neutrality` |
| `CBL` | empty command table and blood-red routes, with no leader portrait | `CBL`, `CBL_communism`, `CBL_democratic`, `CBL_fascism`, `CBL_neutrality` |
| `CBL_CENTRAL_COMMAND` | blade and chain binding routes into rigid command | `CBL_CENTRAL_COMMAND`, `CBL_CENTRAL_COMMAND_communism`, `CBL_CENTRAL_COMMAND_democratic`, `CBL_CENTRAL_COMMAND_fascism`, `CBL_CENTRAL_COMMAND_neutrality` |
| `CBL_HOST_CONFEDERATION` | four unequal Host weapons joined around an empty table | `CBL_HOST_CONFEDERATION`, `CBL_HOST_CONFEDERATION_communism`, `CBL_HOST_CONFEDERATION_democratic`, `CBL_HOST_CONFEDERATION_fascism`, `CBL_HOST_CONFEDERATION_neutrality` |
| `CBL_RITUAL_STATE` | blank state ledger, punishment table, plain sealed bowl, ordered chains | `CBL_RITUAL_STATE`, `CBL_RITUAL_STATE_communism`, `CBL_RITUAL_STATE_democratic`, `CBL_RITUAL_STATE_fascism`, `CBL_RITUAL_STATE_neutrality` |
| `ZZZ_CANNIBALISM_HANNIBAL` | frost-cracked animal jaw, winter chain, ruined road, dark-red ice | `ZZZ_CANNIBALISM_HANNIBAL`, `ZZZ_CANNIBALISM_HANNIBAL_communism`, `ZZZ_CANNIBALISM_HANNIBAL_democratic`, `ZZZ_CANNIBALISM_HANNIBAL_fascism`, `ZZZ_CANNIBALISM_HANNIBAL_neutrality` |

## Content restrictions

All selected source sheets were reviewed before export. They contain no real people or victims, readable text, real political emblems, extremist insignia, national coats of arms, Indigenous regalia, sacred imagery, tribal symbols, or recognizable national symbols. `ZZZ_CANNIBALISM_HANNIBAL` uses only an animal jaw, ice, chain, and road; it does not depict a creature, person, antlers, headdress, mask, totem, feather, rune, or borrowed cultural motif.

The existing Wendigo base family was not opened for writing. Its preservation hashes are recorded in the validation report and subagent handoff.

## Superseded identity

`CBL_LAST_TABLE` is not part of this package. Its 13 live remnants were removed only after all 195 current TGAs passed the format, orientation, alpha, decoded-pixel, count, and uniqueness gates. Historical source art and processed documentation files outside the live `gfx/flags` folders were left intact.
