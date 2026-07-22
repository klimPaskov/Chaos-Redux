# GFX handoff: captured facility recovery raid icons

Parent wiring scope: native HOI4 raid `custom_map_icon` / raid-type map icon.

Suggested existing target file: `interface/chaosx_raids.gfx`.

The parent agent owns the `.gfx` edit. Copy these exact entries into the existing `spriteTypes = { ... }` block:

```text
spriteType = {
	name = "GFX_raid_type_icon_bio_facility_secure_preserve"
	texturefile = "gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_secure_preserve.dds"
}
spriteType = {
	name = "GFX_raid_type_icon_bio_facility_destroy_safely"
	texturefile = "gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_destroy_safely.dds"
}
```

Runtime ids and final textures:

| Raid id | Sprite id | DDS texture path | Native size | DDS |
|---|---|---|---:|---|
| `bio_facility_secure_preserve_raid` | `GFX_raid_type_icon_bio_facility_secure_preserve` | `gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_secure_preserve.dds` | 32x32 | uncompressed BGRA / B8G8R8A8, one level |
| `bio_facility_destroy_safely_raid` | `GFX_raid_type_icon_bio_facility_destroy_safely` | `gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_destroy_safely.dds` | 32x32 | uncompressed BGRA / B8G8R8A8, one level |

No `.gfx`, `.gui`, gameplay, raid, localisation, or existing icon files were edited by this asset package. The filenames and sprite ids above were provided by the parent prompt and must remain unchanged.

Visual notes:

- Preserve icon: sealed brass-edged facility doorway, lock, containment shield, and secured ledger/evidence case.
- Destroy-safely icon: circular sealed chamber, crossed inert canister silhouettes, and a controlled timer/demolition marker.
- Both have real transparent unused pixels and no active-agent cloud, gore, procedural biological content, or generated text.
