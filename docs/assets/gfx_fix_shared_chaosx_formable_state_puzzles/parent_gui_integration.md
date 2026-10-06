# Parent puzzle marker integration

Acceptance basis: the assigned shared graphics review requires a readable minimum footprint for eight tiny states while preserving their geographic silhouettes.
The parent selected the corrected v3 textures after reviewing nine whole-puzzle mosaics, fifteen paired-state pages and all eight marker details.
These mosaics are the scoped before/after layout references; they establish local geometry, not full engine-window acceptance.

The parent changed eight `iconType.position` leaves in six existing shared GUI files.
Each shift compensates for transparent padding around the source core, keeping that core at its original map coordinates.
The existing dynamic image properties still choose unresolved/qualifying sprites, and the delayed state-tooltip keys remain attached to the same icon names.

| Window suffix | State | Original x,y | Padded x,y |
|---|---:|---|---|
| `form_north_sea_empire` | 932 | 126,140 | 121,135 |
| `form_scandinavia` | 910 | 239,164 | 234,159 |
| `goe_form_hindustan` | 320 | 220,149 | 215,144 |
| `goe_form_hindustan` | 321 | 190,130 | 185,125 |
| `goe_form_hindustan` | 985 | 267,60 | 262,56 |
| `unite_maghreb` | 783 | 122,66 | 117,61 |
| `proclaim_greater_italy` | 116 | 185,157 | 181,152 |
| `unite_latin_africa` | 796 | 181,105 | 176,101 |

## Source evidence

The offline `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, lines 178–195, defines icon positioning, sprite references and tooltip attributes; SHA-256 is `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`.
The offline `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`, lines 391–434, documents image properties and scripted-localisation texture selection; SHA-256 is `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`.
The installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md`, lines 60–82, documents dynamic image and position properties; SHA-256 is `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`.
The installed `interface/sov_paranoia_system_scripted_gui.gui`, lines 26–38, is the vanilla static-icon positioning precedent; SHA-256 is `b8925bf8daf88ba82e6ce66f7b5131cae7083e6eda5367e2cf2b6eaef6310a85`.
The unchanged `common/scripted_guis/chaosx_formable_state_puzzles.txt` supplies image properties for these exact icon names without overriding their x/y positions.

## Engine evidence gap

The exact six windows were attempted through `hoi4.gui_inspect` and `hoi4.gui_render` before and after the coordinate edits at 1920×1080, UI scale 1.
Every request failed with `Transport closed`; `parent_mcp_gui_before.json` and `parent_mcp_gui_after.json` retain the actual requests and responses.
No production PNG, `validation.json`, matching engine comparison, or click/hover acceptance was returned.
The final engine visual gate remains open; local mosaics and source checks are not equivalent proof.

## Orchestrator check

Use formable fixtures for the six named windows with the affected states first unresolved and then qualifying.
Inspect each marker and hover its centre at UI scale 1: the same state tooltip must appear, its original geographic core must remain fixed, and the ring must stay inside the 440×180 puzzle area.
Changing ownership/control to satisfy that state's existing condition must switch its grey hatch/ring to the muted green variant without moving it.
The nine canonical manifests retain the padded bitmap origins so future runtime generation preserves these positions.
