# Event 005 Generated High-Chaos Flags Manifest

Event id: `005`

Event slug: `soviet_union_collapse`

Package: `generated_high_chaos_flags_2026_05_26`

Scope: bounded first batch of generated fictional base-flag replacements for poor/simple Event 005 high-chaos flag art. This package does not edit `.gfx`, gameplay, localisation, GUI, focus, decision, scripted, country history, or live flag files. It provides TGA-ready handoff files for parent review or promotion.

## References Inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- existing Event 005 flag files in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`
- existing Event 005 leader/council portrait contact sheet at `docs/assets/005_soviet_collapse/event005_asset_handoff/contact_sheets/event005_requested_leaders_contact.png`
- offline Paradox wiki core pages required by `AGENTS.md`
- vanilla documentation under `/home/klim/projects/Hearts of Iron IV/documentation/`

## Preservation Rules Applied

- No existing live base flag was overwritten.
- No vanilla-supported or pre-existing country base flag was replaced.
- This package contains only isolated candidate files under `docs/assets/`.
- The five first-batch targets are treated as fictional Event 005 custom high-chaos tags.
- Ideology variants were not produced from palette swaps or simple emblem overlays. They remain pending until they can receive distinct generated/source art.
- `SOG`, `ALN`, `KHW`, and `KZR` are not included in this generated flag batch because their restoration flags need historically grounded/source-research treatment unless a specific route is explicitly fictional.

## Contact Sheets

- Normal-size review: `contact_sheets/high_chaos_flags_normal_contact.png`
- Size and orientation review: `contact_sheets/high_chaos_flags_size_orientation_contact.png`

Orientation note: the generated source art and all processed previews were exported upright without vertical flipping. The contact sheets are the visual orientation proof for normal, medium, and small sizes.

## Validation

- Format/hash audit: `validation/tga_format_hash_audit.tsv`
- Normal flags: `82x52` TGA, descriptor byte `0x08`
- Medium flags: `41x26` TGA, descriptor byte `0x08`
- Small flags: `10x7` TGA, descriptor byte `0x08`

## Assets

| Tag | Asset type | Source mode | Source PNG | Processed previews | Final TGA paths | Target sizes | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `KRS` | fictional base flag | `$imagegen` | `source_png/KRS_source.png` | `processed_png/KRS_normal.png`, `processed_png/KRS_medium.png`, `processed_png/KRS_small.png` | `final_tga/normal/KRS.tga`, `final_tga/medium/KRS.tga`, `final_tga/small/KRS.tga` | `82x52`, `41x26`, `10x7` | `handed_off` | Kronstadt naval council design with anchor and broken chain. |
| `RMC` | fictional base flag | `$imagegen` | `source_png/RMC_source.png` | `processed_png/RMC_normal.png`, `processed_png/RMC_medium.png`, `processed_png/RMC_small.png` | `final_tga/normal/RMC.tga`, `final_tga/medium/RMC.tga`, `final_tga/small/RMC.tga` | `82x52`, `41x26`, `10x7` | `handed_off` | Red Martyrs memorial/resurrection standard. |
| `SDZ` | fictional base flag | `$imagegen` | `source_png/SDZ_source.png` | `processed_png/SDZ_normal.png`, `processed_png/SDZ_medium.png`, `processed_png/SDZ_small.png` | `final_tga/normal/SDZ.tga`, `final_tga/medium/SDZ.tga`, `final_tga/small/SDZ.tga` | `82x52`, `41x26`, `10x7` | `handed_off` | Security Directorate sealed archive and cordon emblem. |
| `TSC` | fictional base flag | `$imagegen` | `source_png/TSC_source.png` | `processed_png/TSC_normal.png`, `processed_png/TSC_medium.png`, `processed_png/TSC_small.png` | `final_tga/normal/TSC.tga`, `final_tga/medium/TSC.tga`, `final_tga/small/TSC.tga` | `82x52`, `41x26`, `10x7` | `handed_off` | Tunguska star-science committee design with meteor/compass mark. |
| `UDC` | fictional base flag | `$imagegen` | `source_png/UDC_source.png` | `processed_png/UDC_normal.png`, `processed_png/UDC_medium.png`, `processed_png/UDC_small.png` | `final_tga/normal/UDC.tga`, `final_tga/medium/UDC.tga`, `final_tga/small/UDC.tga` | `82x52`, `41x26`, `10x7` | `handed_off` | Union Defense Committee military district shield. |

## Portrait Status

No new portrait DDS files were generated in this first batch. The priority tags already have live `156x210` DDS portraits in `gfx/leaders/005_soviet_collapse/`, and the existing contact sheet shows they are council/factory-style or leader-style images rather than blank placeholders. Regenerate only a specifically rejected portrait in a later targeted batch to avoid overwriting unrelated dirty leader files.

Existing priority portrait files observed:

- `gfx/leaders/005_soviet_collapse/KRS_leader.dds`
- `gfx/leaders/005_soviet_collapse/RMC_leader.dds`
- `gfx/leaders/005_soviet_collapse/SDZ_leader.dds`
- `gfx/leaders/005_soviet_collapse/TSC_leader.dds`
- `gfx/leaders/005_soviet_collapse/UDC_leader.dds`
- `gfx/leaders/005_soviet_collapse/SOG_leader.dds`
- `gfx/leaders/005_soviet_collapse/ALN_leader.dds`
- `gfx/leaders/005_soviet_collapse/KHW_leader.dds`
- `gfx/leaders/005_soviet_collapse/KZR_leader.dds`

## Remaining Work

- Generate distinct ideology/route variants for `KRS`, `RMC`, `SDZ`, `TSC`, and `UDC` from separate generated/source art if the event needs them; do not derive them as simple recolors of these base flags.
- Route `SOG`, `ALN`, `KHW`, and `KZR` flag replacements through historical/source-research or historically grounded design unless the parent explicitly labels a specific variant as fictional.
- Regenerate only the specific leader/council portraits the parent rejects; all nine priority tags already have live portrait DDS files at the correct size.

## Blockers And Simplifications

- Simplification: this is a first batch of five base flags, not the full Event 005 flag surface.
- Simplification: ideology variants were intentionally not produced because doing them quickly from these base flags would recreate the user's complaint about simple recolors.
- Blocker: no live asset promotion was performed because related docs and some leader files were already dirty before this pass.
