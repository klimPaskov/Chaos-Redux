# Event 005 Generated Asset Sidecar

Audit date: 2026-05-24

Scope: Event 005 Soviet Collapse generated leader/council portraits and fictional/generated flags. This sidecar did not edit gameplay, localisation, script, `.gfx`, history, country, or spreadsheet files.

## Reference Folders Inspected

- `.agents/skills/chaos-redux-event-assets/assets/flags`
- `gfx/leaders/005_soviet_collapse`
- `gfx/leaders`
- `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small`
- `docs/assets/005_soviet_union_collapse`

## Current Portrait State

No active referenced Event 005 leader/council portrait DDS was missing in this pass. The active council portraits below exist at `156x210` and have source plus processed PNG sidecars:

| Active tag | Final DDS | Source PNG | Processed PNG |
| --- | --- | --- | --- |
| `MOL` | `gfx/leaders/005_soviet_collapse/MOL_leader.dds` | `docs/assets/005_soviet_union_collapse/source_png/MOL_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/MOL_leader.png` |
| `UZB` | `gfx/leaders/005_soviet_collapse/UZB_leader.dds` | `docs/assets/005_soviet_union_collapse/source_png/UZB_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/UZB_leader.png` |
| `TAJ` | `gfx/leaders/005_soviet_collapse/TAJ_leader.dds` | `docs/assets/005_soviet_union_collapse/source_png/TAJ_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/TAJ_leader.png` |
| `TMS` | `gfx/leaders/005_soviet_collapse/TMS_leader.dds` | `docs/assets/005_soviet_union_collapse/source_png/TMS_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/TMS_leader.png` |
| `FER` | `gfx/leaders/005_soviet_collapse/FER_leader.dds` | `docs/assets/005_soviet_union_collapse/source_png/FER_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/FER_leader.png` |

These active DDS paths are referenced by `interface/005_soviet_collapse_custom_icons.gfx`; this sidecar only read that file to verify references.

## Deleted Portrait DDS Paths

The following tracked portrait DDS files are currently deleted from the working tree:

- `gfx/leaders/005_soviet_collapse/BEC_leader.dds`
- `gfx/leaders/005_soviet_collapse/BLT_leader.dds`
- `gfx/leaders/005_soviet_collapse/COU_leader.dds`
- `gfx/leaders/005_soviet_collapse/ILU_leader.dds`
- `gfx/leaders/005_soviet_collapse/IRA_leader.dds`

I found no current references to `BEC`, `BLT`, `COU`, `ILU`, or `IRA` in the active Event 005 gameplay/interface/localisation/docs search pass. Their processed PNGs still exist, and each is hash-identical to one of the active council portraits:

| Deleted tag | Reassigned active tag | Existing processed PNG |
| --- | --- | --- |
| `BEC` | `MOL` | `docs/assets/005_soviet_union_collapse/processed_png/BEC_leader.png` |
| `BLT` | `UZB` | `docs/assets/005_soviet_union_collapse/processed_png/BLT_leader.png` |
| `COU` | `TAJ` | `docs/assets/005_soviet_union_collapse/processed_png/COU_leader.png` |
| `ILU` | `TMS` | `docs/assets/005_soviet_union_collapse/processed_png/ILU_leader.png` |
| `IRA` | `FER` | `docs/assets/005_soviet_union_collapse/processed_png/IRA_leader.png` |

Handoff: do not regenerate these five portraits unless the parent confirms the inactive tags are still needed. If they are needed, generate fictional collective/council portraits only; do not generate real leader portraits.

## Flag State

For the inspected Event 005 generated/fictional flag set, all normal/medium/small TGA files currently present in scope decode to the expected dimensions:

- normal: `82x52`
- medium: `41x26`
- small: `10x7`

No active base flag for vanilla-supported `SOV`, `RUS`, `UKR`, `BLR`, or `KAZ` was changed by this pass.

The following inactive/stale flag families are byte-identical across their base and ideology variants and should not be treated as final unique ideology variants if these tags become active again:

- `BEC` and `COU`: identical base plus all ideology variants in normal, medium, and small folders.
- `BLT`: identical base plus all ideology variants in normal, medium, and small folders.
- `ILU` and `IRA`: identical base plus all ideology variants in normal, medium, and small folders, also identical to `DSC`.

Exact affected paths follow this pattern for each listed tag and suffix:

- `gfx/flags/<TAG><suffix>.tga`
- `gfx/flags/medium/<TAG><suffix>.tga`
- `gfx/flags/small/<TAG><suffix>.tga`

Where `<TAG>` is `BEC`, `BLT`, `COU`, `ILU`, or `IRA`, and `<suffix>` is blank, `_communism`, `_democratic`, `_fascism`, or `_neutrality`.

## Existing Generated Flag Handoff

The review-only `SOG` replacement family already exists under:

- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/manifest.md`
- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/gfx_handoff.md`
- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/tga/`

It is marked `needs_user_review` and was not copied into active `gfx/flags` by this pass.

## Deferred Generation Prompts

Use Codex built-in `image_gen` for these only if the parent confirms the inactive tags should be revived or their flags should remain in the shipped asset set.

### Fictional Council Portrait Prompt Template

```text
Use case: historical-scene
Asset type: HOI4 fictional leader/council portrait, final crop 156x210
Primary request: Create a fictional collective emergency council portrait for Event 005 Soviet Collapse tag <TAG>, not based on any real person.
Subject: A small governing body represented by one clear central seated official with two subdued advisers behind them, period-appropriate 1936-1945 Soviet-border civilian or military-administrative clothing, regional visual cues for <REGION>, no recognizable real individual.
Style: HOI4-style leader portrait, upper torso/bust framing, subdued painterly realism, muted period palette, clear face and authority silhouette, dark neutral office background.
Composition: centered, readable at 156x210, strong head-and-shoulders focus, no crowd clutter.
Avoid: readable text, labels, watermarks, modern props, modern uniforms, modern streets, meme styling, exact likeness of any real leader, flags copied from existing countries.
```

### Fictional Flag Prompt Template

```text
Use case: logo-brand
Asset type: fictional alternate-history HOI4 country flag source art, to be processed to 82x52, 41x26, and 10x7
Primary request: Create a clean fictional flag for Event 005 Soviet Collapse tag <TAG> and ideology <IDEOLOGY>, distinct from its base and other ideology variants.
Subject: Intentional flag design using regional motifs for <REGION>, one bold central emblem or field structure, readable at 10x7, no historical attested symbol unless separately sourced.
Style: flat flag artwork with restrained cloth texture, strong contrast, no text, no seals with tiny unreadable details.
Composition: horizontal flag aspect, simple enough for HOI4 small flag size, orientation unambiguous.
Avoid: simple recolor of an existing variant, flipped copies, one added basic shape as the only difference, copied Soviet or vanilla country flag, readable letters, watermarks, modern logo styling.
```

## Blockers and Uncertainty

- I did not generate or restore the deleted `BEC`, `BLT`, `COU`, `ILU`, or `IRA` DDS files because the current repo search found them as inactive/stale tags rather than active missing references.
- I did not replace the duplicate inactive flag families because doing so would create final active-looking assets for tags that currently appear inactive; that should be confirmed by the parent before generating or copying outputs.
- Broad unrelated working-tree changes already existed before this sidecar pass and were left untouched.
