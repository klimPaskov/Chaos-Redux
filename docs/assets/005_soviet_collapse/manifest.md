# Event 005 Soviet Collapse Sidecar Asset Manifest

This package is a bounded generated-art and review sidecar for the Event 005 Soviet Collapse ancient/restoration/high-chaos asset complaint set: `ALN`, `KHW`, `KZR`, `SOG`, `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, and `OGB`.

No gameplay, localisation, `.gfx`, history, country, focus, decision, scripted logic, spreadsheet, live `gfx/leaders/**`, or live `gfx/flags/**` files were edited.

## Generated Portraits

| Asset | Tag | Type | Source mode | Source PNG | Processed PNG | Sidecar DDS | Proposed live DDS | Sprite name | Suggested `.gfx` file | Target size | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alan Pass Council | `ALN` | portrait | `$imagegen`, fictional collective council | `docs/assets/005_soviet_collapse/source_png/leader_aln_pass_council_source.png` | `docs/assets/005_soviet_collapse/processed_png/leader_aln_pass_council.png` | `docs/assets/005_soviet_collapse/final_dds/ALN_leader.dds` | `gfx/leaders/005_soviet_collapse/ALN_leader.dds` | `GFX_portrait_ALN_alan_pass_council` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | 156x210 | handed_off |
| Oasis Register Authority | `KHW` | portrait | `$imagegen`, fictional collective council | `docs/assets/005_soviet_collapse/source_png/leader_khw_oasis_authority_source.png` | `docs/assets/005_soviet_collapse/processed_png/leader_khw_oasis_authority.png` | `docs/assets/005_soviet_collapse/final_dds/KHW_leader.dds` | `gfx/leaders/005_soviet_collapse/KHW_leader.dds` | `GFX_portrait_KHW_oasis_register_authority` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | 156x210 | handed_off |
| Itil Toll Council | `KZR` | portrait | `$imagegen`, fictional collective council | `docs/assets/005_soviet_collapse/source_png/leader_kzr_toll_khaganate_source.png` | `docs/assets/005_soviet_collapse/processed_png/leader_kzr_toll_khaganate.png` | `docs/assets/005_soviet_collapse/final_dds/KZR_leader.dds` | `gfx/leaders/005_soviet_collapse/KZR_leader.dds` | `GFX_portrait_KZR_itil_toll_council` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | 156x210 | handed_off |
| Council of the City Registers | `SOG` | portrait | `$imagegen`, fictional collective council | `docs/assets/005_soviet_collapse/source_png/leader_sog_city_league_source.png` | `docs/assets/005_soviet_collapse/processed_png/leader_sog_city_league.png` | `docs/assets/005_soviet_collapse/final_dds/SOG_leader.dds` | `gfx/leaders/005_soviet_collapse/SOG_leader.dds` | `GFX_portrait_SOG_city_registers_council` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | 156x210 | handed_off |

Prompt record: `docs/assets/005_soviet_collapse/prompts/generated_prompts.md`.

Contact sheet: `docs/assets/005_soviet_collapse/contact_sheets/ancient_restoration_council_portraits.png`.

DDS conversion note: the repository converter found a configured Windows `texconv.exe` path that was not executable from this Linux session, and its ffmpeg BGRA fallback raised a header packing error. The sidecar DDS files were therefore written with ImageMagick `convert`. Treat the PNG previews as the canonical reviewed sidecar previews if the main agent requires a strict DirectXTex reconversion pass before promotion.

## Flag Review

The requested live flag files were reviewed in place only. They were not edited or replaced because the worktree already contains dirty flag changes for the requested tags.

Exhaustive reviewed paths and orientation metadata are in:

- `docs/assets/005_soviet_collapse/contact_sheets/current_flag_orientation_review.tsv`
- `docs/assets/005_soviet_collapse/contact_sheets/current_flag_exact_duplicate_groups.tsv`
- `docs/assets/005_soviet_collapse/contact_sheets/current_flag_intra_tag_rmse.tsv`

Contact sheets:

- `docs/assets/005_soviet_collapse/contact_sheets/current_requested_flags_normal.png`
- `docs/assets/005_soviet_collapse/contact_sheets/current_requested_flags_medium.png`
- `docs/assets/005_soviet_collapse/contact_sheets/current_requested_flags_small_scaled.png`

Orientation and size result:

- All reviewed normal flags exist at 82x52.
- All reviewed medium flags exist at 41x26.
- All reviewed small flags exist at 10x7.
- TGA descriptor bytes observed: `0x8` for alpha-bearing normal/medium assets and `0x0` for many non-alpha small assets.
- The normal, medium, and scaled-small contact sheets show the designs in landscape orientation.

Uniqueness result:

- No exact pixel-duplicate normal-size flags were found among the reviewed set.
- The only low-distance same-tag pair detected by RMSE was `RMC.tga` versus `RMC_communism.tga` at `0.1130`; this is not an exact duplicate but should receive visual review if the user wants stronger ideology separation.
- The live designs are mostly distinct in composition, not just simple flips, recolors, or one-shape additions.

Historical-source routing:

- `OGB` is tied to Old Great Bulgaria, a historically attested restoration frame. If the intended flag uses historical Bulgarian/Volga Bulgar symbols, route to `chaosx_asset_source_researcher` rather than fabricating a symbol.
- `ALN`, `KHW`, `KZR`, and `SOG` are fictional high-chaos restoration states in this mod context, but any attempt to use historically attested Alan, Khwarazmian, Khazar, or Sogdian banners, tamgas, seals, scripts, or religious symbols should be source-researched first.
- `KRS`, `CFR`, `RMC`, `SDZ`, `TSC`, and `UDC` are fictional/high-chaos or invented political entities in this Event 005 context; generated ideology variants are appropriate if the main agent chooses to replace current dirty live flags.

## Proposed Follow-Up Flag Priorities

No flag files were generated in this package. If the main agent promotes a second bounded batch, prioritize:

| Priority | Tag | Variant | Source mode | Reason |
| --- | --- | --- | --- | --- |
| 1 | `RMC` | `communism` | `$imagegen`, fictional symbolic | Closest same-tag similarity found against base; should diverge more clearly from the martyr-cult base flag. |
| 2 | `OGB` | all ideology variants | source research first if using historical symbols; otherwise `$imagegen` fictional alternate-history | Historical/restoration symbolism risk needs explicit source-mode choice before generation. |
| 3 | `ALN`, `KHW`, `KZR`, `SOG` | ideology variants | `$imagegen` only for fictional designs; source research if using attested symbols | Ancient-restoration designs can accidentally imply real historical symbols. |
