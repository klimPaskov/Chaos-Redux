# Event 005 Soviet Collapse Asset Handoff Manifest

Scope: bounded sidecar handoff for requested Event 005 leader/council/factory portraits and flag variants. No gameplay, localisation, `.gfx`, focus, history, country, spreadsheet, live flag, or live leader files were edited.

## References Inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- closest available portrait references: existing `gfx/leaders/005_soviet_collapse/` portraits, `docs/assets/005_soviet_collapse/generated_portraits_handoff/contact_sheets/reference_portrait_style_sheet.png`, and vanilla `gfx/leaders/`
- Event 005 final spec asset and country-package sections in `tmp/soviet_collapse_final_clean_merged_spec_package/specs/`
- required offline Paradox wiki core pages, including the available local `Effect - Hearts of Iron 4 Wiki.md`

The flag reference folder shows compact HOI4 flags with simple, centered, high-contrast marks at 82x52. The portrait references use 156x210 subdued painterly bust, council, or symbolic authority framing.

## Contact Sheets and Validation

Created read-only audit contact sheets from the current live target files:

- `contact_sheets/event005_requested_flags_normal_contact.png`
- `contact_sheets/event005_requested_flags_size_orientation_contact.png`
- `contact_sheets/event005_requested_leaders_contact.png`

Validation ledgers:

- `validation/current_live_asset_surface.tsv`
- `validation/normal_flag_hash_uniqueness.tsv`
- `validation/contact_sheet_identify.txt`

Current live files were inspected only. All requested normal and medium TGA flags render at the expected dimensions with descriptor byte `0x08`; all requested small TGA flags render at `10x7` with descriptor byte `0x00`. The origin bits are not set on either descriptor value, so the contact sheet is the visual orientation proof. The audit contact sheet shows the flags upright at normal, medium, and small sizes. Normal-size hash uniqueness is 5/5 for every requested tag, so the current base plus four ideology variants are not byte-identical copies.

## Asset Routing Rules

- Preserve existing no-suffix base flags for already-existing countries and any already-approved custom base flags unless the parent explicitly promotes a replacement.
- Generate only fictional, symbolic, factory-state, council, supernatural, or alternate-history route/ideology variants.
- Route historically grounded restoration flags or historically attested symbols to source research, not pure generation.
- Every promoted flag needs normal, medium, and small TGA outputs plus an orientation contact sheet.
- Every promoted generated portrait needs source PNG, processed PNG, final 156x210 DDS, prompt, manifest entry, and sprite handoff.

## Requested Flag Queue

Target paths for every promoted flag row:

- normal: `gfx/flags/<TAG>[_<ideology>].tga`
- medium: `gfx/flags/medium/<TAG>[_<ideology>].tga`
- small: `gfx/flags/small/<TAG>[_<ideology>].tga`

| Tag | Variant scope | Source mode | Design direction | Current handoff status |
| --- | --- | --- | --- | --- |
| `CFR` | preserve base; generate `_communism`, `_democratic`, `_fascism`, `_neutrality` if replacing variants | `$imagegen` | civilian factory state, reconstruction bureau, bridge/concrete works, civic production authority | planned; current live variants audited only |
| `KRS` | preserve base; generate ideology variants if replacing variants | `$imagegen` | Kronstadt sailor soviet, naval council, harbor guns, fleet/port authority | planned; current live variants audited only |
| `RMC` | preserve base; generate ideology variants if replacing variants | `$imagegen` | Red Martyrs' Resurrection Cult, memorial standard, death-state legitimacy, red-black ceremonial authority | planned; current live variants audited only |
| `SDZ` | preserve base; generate ideology variants if replacing variants | `$imagegen` | Security Directorate Zone, sealed archives, prison/records authority, cordon emblems | planned; current live variants audited only |
| `TSC` | preserve base; generate ideology variants if replacing variants | `$imagegen` | Tunguska Star Committee, Siberian star-science authority, cosmic committee mark | planned; current live variants audited only |
| `UDC` | preserve base; generate ideology variants if replacing variants | `$imagegen` | Union Defense Committee, emergency continuity, military district shield, restrained non-Soviet union symbolism | planned; current live variants audited only |
| `SOG` | preserve base and historical motif variants unless parent explicitly frames a route as fictional | source research for historical/restoration flags; `$imagegen` only for fictional route variants | Sogdian city-restoration, oasis/city-register motifs, historically grounded textile or seal language | source-research route recommended; current live variants audited only |
| `ALN` | preserve base and historical motif variants unless parent explicitly frames a route as fictional | source research for historical/restoration flags; `$imagegen` only for fictional route variants | Alan pass council, mountain pass authority, historically grounded regional heraldic motifs | source-research route recommended; current live variants audited only |
| `KHW` | preserve base and historical motif variants unless parent explicitly frames a route as fictional | source research for historical/restoration flags; `$imagegen` only for fictional route variants | Khwarazmian oasis authority, canal/water-board motifs, historically grounded Central Asian ornament | source-research route recommended; current live variants audited only |
| `KZR` | preserve base and historical motif variants unless parent explicitly frames a route as fictional | source research for historical/restoration flags; `$imagegen` only for fictional route variants | Khazar toll/Volga-Caspian authority, historically grounded steppe and trade-route symbolism | source-research route recommended; current live variants audited only |
| `MFR` | preserve base; generate ideology variants if replacing variants | `$imagegen` | military factory state, arsenal production board, armored-train depot, industrial command seal | planned; current live variants audited only |

## Requested Portrait Queue

Target size for all portraits: `156x210`. Proposed live folder if promoted: `gfx/leaders/005_soviet_collapse/`.

| Tag | Asset type | Source mode | Target final DDS | Proposed sprite | Suggested `.gfx` file | Current handoff status |
| --- | --- | --- | --- | --- | --- | --- |
| `CFR` | factory/council leader portrait | `$imagegen` | `gfx/leaders/005_soviet_collapse/CFR_leader.dds` | `GFX_portrait_CFR_civilian_works_directorate` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |
| `MFR` | factory/council leader portrait | `$imagegen` | `gfx/leaders/005_soviet_collapse/MFR_leader.dds` | `GFX_portrait_MFR_arsenal_directorate` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |
| `KRS` | fictional naval council portrait | `$imagegen` | `gfx/leaders/005_soviet_collapse/KRS_leader.dds` | `GFX_portrait_KRS_kronstadt_council` | `interface/005_soviet_collapse_custom_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |
| `RMC` | fictional/symbolic cult portrait | `$imagegen` | `gfx/leaders/005_soviet_collapse/RMC_leader.dds` | `GFX_portrait_RMC_resurrection_cult` | `interface/005_soviet_collapse_custom_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |
| `SDZ` | fictional security authority portrait | `$imagegen` | `gfx/leaders/005_soviet_collapse/SDZ_leader.dds` | `GFX_portrait_SDZ_security_directorate` | `interface/005_soviet_collapse_custom_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |
| `TSC` | fictional cosmic committee portrait | `$imagegen` | `gfx/leaders/005_soviet_collapse/TSC_leader.dds` | `GFX_portrait_TSC_tunguska_star_committee` | `interface/005_soviet_collapse_custom_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |
| `UDC` | fictional loyalist committee portrait | `$imagegen` | `gfx/leaders/005_soviet_collapse/UDC_leader.dds` | `GFX_portrait_UDC_union_defense_committee` | `interface/005_soviet_collapse_custom_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |
| `SOG` | fictional/restoration council portrait unless parent specifies a real person | `$imagegen` for council portrait; source research only for real-person portrait | `gfx/leaders/005_soviet_collapse/SOG_leader.dds` | `GFX_portrait_SOG_sogdian_council` | `interface/005_soviet_collapse_ancient_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |
| `ALN` | fictional/restoration council portrait unless parent specifies a real person | `$imagegen` for council portrait; source research only for real-person portrait | `gfx/leaders/005_soviet_collapse/ALN_leader.dds` | `GFX_portrait_ALN_alan_pass_council` | `interface/005_soviet_collapse_ancient_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |
| `KHW` | fictional/restoration council portrait unless parent specifies a real person | `$imagegen` for council portrait; source research only for real-person portrait | `gfx/leaders/005_soviet_collapse/KHW_leader.dds` | `GFX_portrait_KHW_oasis_authority_council` | `interface/005_soviet_collapse_ancient_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |
| `KZR` | fictional/restoration council portrait unless parent specifies a real person | `$imagegen` for council portrait; source research only for real-person portrait | `gfx/leaders/005_soviet_collapse/KZR_leader.dds` | `GFX_portrait_KZR_khazar_toll_council` | `interface/005_soviet_collapse_ancient_icons.gfx` | current live portrait audited; regenerate only if parent rejects it |

## Not Produced in This Sidecar

No new generated source PNGs, processed PNGs, final DDS files, or final TGA files were produced. This pass is a manifest/contact-sheet handoff and validation surface only, so it does not replace or promote any live asset.
