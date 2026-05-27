## GFX Handoff

Target `.gfx` file: `interface/005_soviet_collapse_regional_icons.gfx`

Current duplicate sprite to unwind:

- `GFX_central_asia_soviet_collapse_steppe_federation`
- `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_steppe_federation.dds`

Proposed replacement sprites:

| Focus id | Sprite name | Final DDS path | Ready |
| --- | --- | --- | --- |
| `central_asia_soviet_collapse_turkestan_city_congress` | `GFX_central_asia_soviet_collapse_turkestan_city_congress` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_turkestan_city_congress.dds` | `needs_user_review` |
| `central_asia_soviet_collapse_turkestan_federation_road` | `GFX_central_asia_soviet_collapse_turkestan_federation_road` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_turkestan_federation_road.dds` | `needs_user_review` |
| `central_asia_soviet_collapse_federation_delegates` | `GFX_central_asia_soviet_collapse_federation_delegates` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_federation_delegates.dds` | `needs_user_review` |
| `central_asia_soviet_collapse_federation_state` | `GFX_central_asia_soviet_collapse_federation_state` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_federation_state.dds` | `needs_user_review` |

Suggested sprite snippets:

```txt
spriteType = {
	name = "GFX_central_asia_soviet_collapse_turkestan_city_congress"
	texturefile = "gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_turkestan_city_congress.dds"
}
spriteType = {
	name = "GFX_central_asia_soviet_collapse_turkestan_federation_road"
	texturefile = "gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_turkestan_federation_road.dds"
}
spriteType = {
	name = "GFX_central_asia_soviet_collapse_federation_delegates"
	texturefile = "gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_federation_delegates.dds"
}
spriteType = {
	name = "GFX_central_asia_soviet_collapse_federation_state"
	texturefile = "gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_federation_state.dds"
}
```

Uncertainty:

- the art is technically complete enough to preview and wire, but it should be reviewed once in-game because the alpha was recovered from imagegen checkerboard output rather than a native transparent source

