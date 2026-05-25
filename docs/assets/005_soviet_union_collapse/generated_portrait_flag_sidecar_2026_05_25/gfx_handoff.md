# GFX Handoff

This is an isolated sidecar package. No `.gfx` files were edited.

## Generated Pilot Portrait

| Asset | Sidecar final file | Proposed live DDS path | Proposed sprite name | Suggested `.gfx` file | Use notes |
| --- | --- | --- | --- | --- | --- |
| CFR leader/council portrait | `docs/assets/005_soviet_union_collapse/generated_portrait_flag_sidecar_2026_05_25/final_dds/CFR_leader.dds` | `gfx/leaders/005_soviet_collapse/CFR_leader.dds` | keep existing CFR portrait sprite if already wired; otherwise `GFX_portrait_CFR_civilian_works_directorate` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | Fictional generated council portrait. Parent should compare against the current dirty/working CFR portrait before promotion. |

Ready-to-copy sprite shape if a new sprite is needed:

```txt
spriteType = {
	name = "GFX_portrait_CFR_civilian_works_directorate"
	texturefile = "gfx/leaders/005_soviet_collapse/CFR_leader.dds"
}
```

## Generated Pilot Flag

HOI4 country flags are TGA assets, not `.gfx` sprite DDS entries. This sidecar produced all three flag sizes inside the sidecar only:

| Asset | Sidecar normal | Sidecar medium | Sidecar small | Proposed live paths | Orientation confirmation |
| --- | --- | --- | --- | --- | --- |
| CFR communism ideology flag | `final_tga/normal/CFR_communism.tga` | `final_tga/medium/CFR_communism.tga` | `final_tga/small/CFR_communism.tga` | `gfx/flags/CFR_communism.tga`, `gfx/flags/medium/CFR_communism.tga`, `gfx/flags/small/CFR_communism.tga` | Normal `82x52`, medium `41x26`, small `10x7`; TGA descriptor byte is `0x08`; contact sheet reviewed in `contact_sheets/CFR_communism_flag_sizes.png`. |

Parent should only promote this pilot flag after confirming it is preferred over the current dirty `CFR_communism` files.

## Blocked/Queued Handoff

The remaining portrait and flag rows are listed in `queued_asset_ledger.md`. They are not generated in this sidecar. The blocker is not tool availability; it is promotion scope: bulk replacement would need parent selection against the existing dirty Event 005 flag and portrait worktree.

