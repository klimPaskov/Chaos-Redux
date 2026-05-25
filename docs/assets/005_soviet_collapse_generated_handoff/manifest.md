# Event 005 Soviet Collapse Generated Asset Handoff

Audit date: 2026-05-25

Scope: bounded generated-asset handoff for fictional/collective leader portraits and problematic fictional or ideology flags. This pass did not edit gameplay, script, localisation, `.gfx`, GUI, history, country, spreadsheet, or existing `gfx/flags` files.

## References inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags`
- `gfx/leaders/005_soviet_collapse`
- `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small`
- `docs/assets/005_soviet_union_collapse/manifest.md`
- `docs/assets/005_soviet_union_collapse/gfx_handoff.md`
- `docs/assets/005_soviet_union_collapse/portrait_sidecar_2026_05_24.md`
- `docs/assets/005_soviet_union_collapse/event005_asset_sidecar_2026_05_24.md`

The asset-skill reference tree contains flag examples at 82x52 PNG. There is no `leaders` or `portraits` reference folder under `.agents/skills/chaos-redux-event-assets/assets/`; existing Chaos Redux and Event 005 leader portraits were used as the portrait reference surface.

## Worktree guardrails

The worktree already contains broad unrelated Event 005 edits. This handoff preserves existing dirty assets and does not overwrite them.

Existing dirty flag families that must be preserved:

| Tag | Dirty variants | Dirty sizes/paths |
| --- | --- | --- |
| `ALN` | base, `communism`, `democratic`, `fascism`, `neutrality` | `gfx/flags/ALN*.tga`, `gfx/flags/medium/ALN*.tga`, `gfx/flags/small/ALN*.tga` |
| `CFR` | base, `communism`, `democratic`, `fascism`, `neutrality` | `gfx/flags/CFR*.tga`, `gfx/flags/medium/CFR*.tga`, `gfx/flags/small/CFR*.tga` |
| `KHW` | base, `communism`, `democratic`, `fascism`, `neutrality` | `gfx/flags/KHW*.tga`, `gfx/flags/medium/KHW*.tga`, `gfx/flags/small/KHW*.tga` |
| `KRS` | base, `communism`, `democratic`, `fascism`, `neutrality` | `gfx/flags/KRS*.tga`, `gfx/flags/medium/KRS*.tga`, `gfx/flags/small/KRS*.tga` |
| `KZR` | base, `communism`, `democratic`, `fascism`, `neutrality` | `gfx/flags/KZR*.tga`, `gfx/flags/medium/KZR*.tga`, `gfx/flags/small/KZR*.tga` |
| `RMC` | base, `communism`, `democratic`, `fascism`, `neutrality` | `gfx/flags/RMC*.tga`, `gfx/flags/medium/RMC*.tga`, `gfx/flags/small/RMC*.tga` |
| `SDZ` | base, `communism`, `democratic`, `fascism`, `neutrality` | `gfx/flags/SDZ*.tga`, `gfx/flags/medium/SDZ*.tga`, `gfx/flags/small/SDZ*.tga` |
| `SOG` | base, `communism`, `democratic`, `fascism`, `neutrality` | `gfx/flags/SOG*.tga`, `gfx/flags/medium/SOG*.tga`, `gfx/flags/small/SOG*.tga` |
| `TSC` | base, `communism`, `democratic`, `fascism`, `neutrality` | `gfx/flags/TSC*.tga`, `gfx/flags/medium/TSC*.tga`, `gfx/flags/small/TSC*.tga` |
| `UDC` | base, `communism`, `democratic`, `fascism`, `neutrality` | `gfx/flags/UDC*.tga`, `gfx/flags/medium/UDC*.tga`, `gfx/flags/small/UDC*.tga` |

Exact dirty flag file count in this scope: 150 files, from `10` tags times `5` variants times `3` sizes.

Existing dirty/deleted portrait files that must not be silently restored or overwritten:

- `gfx/leaders/005_soviet_collapse/BEC_leader.dds`
- `gfx/leaders/005_soviet_collapse/BLT_leader.dds`
- `gfx/leaders/005_soviet_collapse/COU_leader.dds`
- `gfx/leaders/005_soviet_collapse/ILU_leader.dds`
- `gfx/leaders/005_soviet_collapse/IRA_leader.dds`

## Active leader portrait handoff

No active fictional/collective Event 005 leader portrait needing final wiring was found in this bounded pass.

The currently wired active vanilla-supported council portraits are already registered in `interface/005_soviet_collapse_custom_icons.gfx` and referenced from `common/scripted_effects/005_soviet_collapse_effects.txt`:

| Active tag | Council portrait | Final DDS | Sprite | Status |
| --- | --- | --- | --- | --- |
| `MOL` | Sfat Crisis Directorate | `gfx/leaders/005_soviet_collapse/MOL_leader.dds` | `GFX_portrait_MOL_sfat_crisis_directorate` | already wired |
| `UZB` | Tashkent Emergency Majlis | `gfx/leaders/005_soviet_collapse/UZB_leader.dds` | `GFX_portrait_UZB_tashkent_emergency_majlis` | already wired |
| `TAJ` | Pamir Republican Council | `gfx/leaders/005_soviet_collapse/TAJ_leader.dds` | `GFX_portrait_TAJ_pamir_republican_council` | already wired |
| `TMS` | Ashgabat Desert Authority | `gfx/leaders/005_soviet_collapse/TMS_leader.dds` | `GFX_portrait_TMS_ashgabat_desert_authority` | already wired |
| `FER` | Far Eastern Republic Council | `gfx/leaders/005_soviet_collapse/FER_leader.dds` | `GFX_portrait_FER_far_eastern_republic_council` | already wired |

## Deferred portrait assets

These deleted portrait files appear stale/inactive rather than active missing references. Search found no current active Event 005 gameplay/interface/localisation references to the tags themselves beyond asset docs. Do not generate, restore, or wire them unless the parent confirms these inactive tags still ship.

| Tag | Deleted DDS | Existing source/preview evidence | Required action if revived | Current status |
| --- | --- | --- | --- | --- |
| `BEC` | `gfx/leaders/005_soviet_collapse/BEC_leader.dds` | `docs/assets/005_soviet_union_collapse/processed_png/BEC_leader.png` was reassigned to active `MOL` lineage | Generate a distinct fictional/collective council portrait, process to 156x210 DDS, then wire a new sprite only if the tag is revived. | blocked pending parent confirmation |
| `BLT` | `gfx/leaders/005_soviet_collapse/BLT_leader.dds` | `docs/assets/005_soviet_union_collapse/processed_png/BLT_leader.png` was reassigned to active `UZB` lineage | Generate a distinct fictional/collective council portrait, process to 156x210 DDS, then wire a new sprite only if the tag is revived. | blocked pending parent confirmation |
| `COU` | `gfx/leaders/005_soviet_collapse/COU_leader.dds` | `docs/assets/005_soviet_union_collapse/processed_png/COU_leader.png` was reassigned to active `TAJ` lineage | Generate a distinct fictional/collective council portrait, process to 156x210 DDS, then wire a new sprite only if the tag is revived. | blocked pending parent confirmation |
| `ILU` | `gfx/leaders/005_soviet_collapse/ILU_leader.dds` | `docs/assets/005_soviet_union_collapse/processed_png/ILU_leader.png` was reassigned to active `TMS` lineage | Generate a distinct fictional/collective council portrait, process to 156x210 DDS, then wire a new sprite only if the tag is revived. | blocked pending parent confirmation |
| `IRA` | `gfx/leaders/005_soviet_collapse/IRA_leader.dds` | `docs/assets/005_soviet_union_collapse/processed_png/IRA_leader.png` was reassigned to active `FER` lineage | Generate a distinct fictional/collective council portrait, process to 156x210 DDS, then wire a new sprite only if the tag is revived. | blocked pending parent confirmation |

Portrait source mode if revived: `$imagegen`, because these are fictional/collective council portraits rather than real leader portraits.

Target size if revived: 156x210 DDS.

Suggested `.gfx` file if revived: `interface/005_soviet_collapse_custom_icons.gfx` or the owning Event 005 custom/ancient portrait `.gfx` file chosen by the parent.

## Active flag handoff

No active country flag `.gfx` wiring is required. HOI4 resolves country flags directly from `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small`.

The existing dirty active flag families listed under Worktree guardrails should be preserved. This pass did not generate replacement TGAs, did not copy review files into `gfx/flags`, and did not alter existing dirty files.

## Deferred/problematic flag assets

The following inactive/stale flag families are documented as problematic because their base and ideology variants are byte-identical across normal, medium, and small sizes. They should not be treated as final unique ideology variants if those tags are revived.

| Tag | Problem | Exact affected final paths | Required action if revived | Current status |
| --- | --- | --- | --- | --- |
| `BEC` | Base and all ideology variants are identical; also shares identity with `COU` according to prior sidecar notes. | `gfx/flags/BEC*.tga`, `gfx/flags/medium/BEC*.tga`, `gfx/flags/small/BEC*.tga` | Generate distinct fictional ideology flag family, export normal/medium/small TGA, then apply to active flag paths only after parent confirms tag revival. | blocked pending parent confirmation |
| `BLT` | Base and all ideology variants are identical. | `gfx/flags/BLT*.tga`, `gfx/flags/medium/BLT*.tga`, `gfx/flags/small/BLT*.tga` | Generate distinct fictional ideology flag family, export normal/medium/small TGA, then apply to active flag paths only after parent confirms tag revival. | blocked pending parent confirmation |
| `COU` | Base and all ideology variants are identical; also shares identity with `BEC` according to prior sidecar notes. | `gfx/flags/COU*.tga`, `gfx/flags/medium/COU*.tga`, `gfx/flags/small/COU*.tga` | Generate distinct fictional ideology flag family, export normal/medium/small TGA, then apply to active flag paths only after parent confirms tag revival. | blocked pending parent confirmation |
| `ILU` | Base and all ideology variants are identical; also identical to `DSC` according to prior sidecar notes. | `gfx/flags/ILU*.tga`, `gfx/flags/medium/ILU*.tga`, `gfx/flags/small/ILU*.tga` | Generate distinct fictional ideology flag family, export normal/medium/small TGA, then apply to active flag paths only after parent confirms tag revival. | blocked pending parent confirmation |
| `IRA` | Base and all ideology variants are identical; also identical to `DSC` according to prior sidecar notes. | `gfx/flags/IRA*.tga`, `gfx/flags/medium/IRA*.tga`, `gfx/flags/small/IRA*.tga` | Generate distinct fictional ideology flag family, export normal/medium/small TGA, then apply to active flag paths only after parent confirms tag revival. | blocked pending parent confirmation |

Exact suffix set for each deferred tag: base, `_communism`, `_democratic`, `_fascism`, and `_neutrality`.

Exact size set for each deferred tag and suffix:

- normal: `gfx/flags/<TAG><suffix>.tga`, 82x52
- medium: `gfx/flags/medium/<TAG><suffix>.tga`, 41x26
- small: `gfx/flags/small/<TAG><suffix>.tga`, 10x7

Flag source mode if revived: `$imagegen`, because these are fictional/alternate-history ideology flag variants.

Country flag `.gfx` note: no `.gfx` sprite is needed for country flags.

## Existing review-only generated flag package

Review-only generated `SOG` replacement candidates already exist under:

- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/manifest.md`
- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/gfx_handoff.md`
- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/tga/`

Those files are not active gameplay assets and were not copied into `gfx/flags` by this handoff. Because `SOG` currently has dirty active flag files, preserve the active `gfx/flags/SOG*.tga`, `gfx/flags/medium/SOG*.tga`, and `gfx/flags/small/SOG*.tga` files unless the parent explicitly approves replacement.

## Generation prompt templates for deferred work

Use Codex built-in `image_gen` only after parent confirmation that a deferred inactive tag should be revived.

### Fictional/collective leader portrait

```text
Use case: historical-scene
Asset type: HOI4 fictional leader/council portrait, final crop 156x210
Primary request: Create a fictional collective emergency council portrait for Event 005 Soviet Collapse tag <TAG>, not based on any real person.
Subject: A small governing body represented by one clear central seated official with two subdued advisers behind them, period-appropriate 1936-1945 Soviet-border civilian or military-administrative clothing, regional visual cues for <REGION>, no recognizable real individual.
Style: HOI4-style leader portrait, upper torso/bust framing, subdued painterly realism, muted period palette, clear face and authority silhouette, dark neutral office background.
Composition: centered, readable at 156x210, strong head-and-shoulders focus, no crowd clutter.
Avoid: readable text, labels, watermarks, modern props, modern uniforms, modern streets, meme styling, exact likeness of any real leader, flags copied from existing countries.
```

### Fictional ideology flag family

```text
Use case: logo-brand
Asset type: fictional alternate-history HOI4 country flag source art, to be processed to 82x52, 41x26, and 10x7
Primary request: Create a clean fictional flag for Event 005 Soviet Collapse tag <TAG> and ideology <IDEOLOGY>, distinct from its base and other ideology variants.
Subject: Intentional flag design using regional motifs for <REGION>, one bold central emblem or field structure, readable at 10x7, no historical attested symbol unless separately sourced.
Style: flat flag artwork with restrained cloth texture, strong contrast, no text, no seals with tiny unreadable details.
Composition: horizontal flag aspect, simple enough for HOI4 small flag size, orientation unambiguous.
Avoid: simple recolor of an existing variant, flipped copies, one added basic shape as the only difference, copied Soviet or vanilla country flag, readable letters, watermarks, modern logo styling.
```

## Completion state

- Created this handoff manifest only.
- Created no source PNGs, processed PNGs, DDS files, TGA files, contact sheets, `.gfx` edits, gameplay edits, localisation edits, or existing asset overwrites.
- Active missing leader portraits needing final wiring: none found.
- Active missing flags needing final wiring: none found; country flags do not use `.gfx` wiring.
- Deferred inactive portrait and flag families needing parent confirmation before generation: `BEC`, `BLT`, `COU`, `ILU`, and `IRA`.
