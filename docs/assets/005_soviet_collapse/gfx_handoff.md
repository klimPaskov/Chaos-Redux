# Event 005 Soviet Collapse Generated Portrait and Flag Review Handoff

This is a bounded sidecar package. It does not edit gameplay, localisation, `.gfx`, history, country, focus, decision, scripted logic, spreadsheet, live portrait DDS, or live flag files.

## Portrait Handoff

| Asset | Type | Source mode | Source PNG | Processed preview | Sidecar DDS | Proposed live DDS | Proposed sprite name | Suggested `.gfx` file | Use notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ALN` Alan Pass Council | portrait | `$imagegen`, fictional collective council | `docs/assets/005_soviet_collapse/source_png/leader_aln_pass_council_source.png` | `docs/assets/005_soviet_collapse/processed_png/leader_aln_pass_council.png` | `docs/assets/005_soviet_collapse/final_dds/ALN_leader.dds` | `gfx/leaders/005_soviet_collapse/ALN_leader.dds` | `GFX_portrait_ALN_alan_pass_council` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | Sidecar candidate only; compare against dirty live portrait before promotion. |
| `KHW` Oasis Register Authority | portrait | `$imagegen`, fictional collective council | `docs/assets/005_soviet_collapse/source_png/leader_khw_oasis_authority_source.png` | `docs/assets/005_soviet_collapse/processed_png/leader_khw_oasis_authority.png` | `docs/assets/005_soviet_collapse/final_dds/KHW_leader.dds` | `gfx/leaders/005_soviet_collapse/KHW_leader.dds` | `GFX_portrait_KHW_oasis_register_authority` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | Sidecar candidate only; compare against dirty live portrait before promotion. |
| `KZR` Itil Toll Council | portrait | `$imagegen`, fictional collective council | `docs/assets/005_soviet_collapse/source_png/leader_kzr_toll_khaganate_source.png` | `docs/assets/005_soviet_collapse/processed_png/leader_kzr_toll_khaganate.png` | `docs/assets/005_soviet_collapse/final_dds/KZR_leader.dds` | `gfx/leaders/005_soviet_collapse/KZR_leader.dds` | `GFX_portrait_KZR_itil_toll_council` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | Sidecar candidate only; compare against dirty live portrait before promotion. |
| `SOG` Council of the City Registers | portrait | `$imagegen`, fictional collective council | `docs/assets/005_soviet_collapse/source_png/leader_sog_city_league_source.png` | `docs/assets/005_soviet_collapse/processed_png/leader_sog_city_league.png` | `docs/assets/005_soviet_collapse/final_dds/SOG_leader.dds` | `gfx/leaders/005_soviet_collapse/SOG_leader.dds` | `GFX_portrait_SOG_city_registers_council` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | Sidecar candidate only; compare against dirty live portrait before promotion. |

Portrait contact sheet: `docs/assets/005_soviet_collapse/contact_sheets/ancient_restoration_council_portraits.png`.

## Flag Orientation and Uniqueness Review

Reviewed tags: `ALN`, `KHW`, `KZR`, `SOG`, `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `OGB`.

Reviewed variants for each tag: base, `communism`, `democratic`, `fascism`, `neutrality`.

Reviewed sizes for each asset:

- Normal: `gfx/flags/<TAG>[_ideology].tga`, expected 82x52.
- Medium: `gfx/flags/medium/<TAG>[_ideology].tga`, expected 41x26.
- Small: `gfx/flags/small/<TAG>[_ideology].tga`, expected 10x7.

Exhaustive asset-path ledger: `docs/assets/005_soviet_collapse/contact_sheets/current_flag_orientation_review.tsv`.

Contact sheets:

- `docs/assets/005_soviet_collapse/contact_sheets/current_requested_flags_normal.png`
- `docs/assets/005_soviet_collapse/contact_sheets/current_requested_flags_medium.png`
- `docs/assets/005_soviet_collapse/contact_sheets/current_requested_flags_small_scaled.png`

Orientation confirmation:

- Every reviewed normal flag is present and 82x52.
- Every reviewed medium flag is present and 41x26.
- Every reviewed small flag is present and 10x7.
- Contact sheets show all reviewed flags in landscape orientation.
- TGA descriptor bytes are recorded per file in the TSV. Existing reviewed assets use `0x8` or `0x0`; no file was rewritten for descriptor normalization in this sidecar.

Uniqueness confirmation:

- No exact normal-size pixel duplicates were found. See `docs/assets/005_soviet_collapse/contact_sheets/current_flag_exact_duplicate_groups.tsv`.
- Same-tag similarity scan only flagged `gfx/flags/RMC.tga` against `gfx/flags/RMC_communism.tga` as visually close (`0.1130` normalized RMSE). See `docs/assets/005_soviet_collapse/contact_sheets/current_flag_intra_tag_rmse.tsv`.
- Visual review of the normal contact sheet shows the listed ideology flags are generally distinct designs rather than simple flips, filters, or one-shape additions.

## Historical-Source Needs

| Tag | Asset scope | Source mode recommendation | Notes |
| --- | --- | --- | --- |
| `OGB` | base and ideology flags | `chaosx_asset_source_researcher` if historical/attested symbolism is intended; `$imagegen` only for clearly fictional alternate-history variants | Old Great Bulgaria is historically attested enough that authentic symbols should not be fabricated. |
| `ALN` | base and ideology flags | `$imagegen` for fictional variants; source research for real Alan symbols, banners, scripts, or seals | Generated ancient-restoration flags are acceptable only when treated as fictional Event 005 designs. |
| `KHW` | base and ideology flags | `$imagegen` for fictional variants; source research for real Khwarazmian symbols, scripts, or seals | Avoid fabricating attested oasis/Khwarazmian symbols. |
| `KZR` | base and ideology flags | `$imagegen` for fictional variants; source research for real Khazar symbols, tamgas, scripts, or seals | Avoid fabricating attested Khazar symbolism. |
| `SOG` | base and ideology flags | `$imagegen` for fictional variants; source research for real Sogdian symbols, scripts, or seals | Avoid fabricating attested Sogdian symbolism. |
| `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC` | ideology flags | `$imagegen`, fictional high-chaos designs | Safe generated-fictional scope unless the main agent intentionally anchors a design to real symbols. |

## Blockers and Uncertainty

- Live flags and live leader DDS files are already dirty in this worktree, so this sidecar did not overwrite or restore them.
- The repository DDS converter could not use the configured Windows `texconv.exe` from Linux, and its ffmpeg fallback failed with a header packing error. Sidecar DDS files were produced with ImageMagick; reconvert from the processed PNGs with DirectXTex before promotion if strict repository DDS provenance is required.
- Photoshop was not used; this task did not include report-event house-style processing.

## Parent-Agent Next Steps

1. Compare the four sidecar portrait DDS files against current live `gfx/leaders/005_soviet_collapse/*_leader.dds` before promotion.
2. If promoting a portrait, copy the sidecar DDS to the proposed live path and keep the existing sprite names listed above.
3. If doing a second flag batch, start with `RMC_communism` and any `OGB` ideology variants after resolving whether OGB should use source-researched historical symbolism or clearly fictional alternate-history design.
