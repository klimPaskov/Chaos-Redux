# Event 028 state-icon placement repair

Disposition: implemented path and documentation repair, with native consumer acceptance unresolved.
Acceptance basis: the user's complete event visual-asset repair request and the event-assets skill require explicit-path event artwork to be grouped under its owning event folder.

Seven existing state-modifier DDS files moved from the family root into `gfx/interface/state_modifiers/028_asteroid_incoming/`.
Their bytes, native 32x32 canvases, alpha, and source art are unchanged.
All eight texture references in `interface/028_asteroid_incoming.gfx`, including the fragment-center recovery alias, point to the new folder.
Every sprite ID remains stable, so dynamic-modifier consumers keep the same IDs.
No image was redrawn, resized, recoloured, replaced, or converted for this repair.
The temporary asset audit also corrects the main-material idea's consumer to `GFX_idea_asteroid_incoming_main_crater_material`, keeping it distinct from the 32x32 main-crater state sprite.

## Review and byte evidence

The parent reopened all seven final native DDS round-trip PNGs individually and compared them with the canonical state-modifier family.
No new crop, clipping, alpha, or readability defect was observed in those unchanged native images.
Each moved DDS was decoded and its RGBA pixels compared exactly with its reviewed round trip.
Each SHA256 below matches before and after movement.
The sprite registry contains no duplicate names, and no live reference to any of the seven old paths remains.

| File basename | Unchanged DDS SHA256 |
| --- | --- |
| `main_asteroid_crater` | `A6F6B41C365F64178EC298ED83AB355E98779C63CDC4BBC2AB584AB89873E738` |
| `catastrophic_impact_zone` | `7FB3A3DFEC7C04CF20DE1AD3E18A6D440E04974875D033B8118BB8E6B117C3B0` |
| `major_impact_zone` | `6D20B214AD2127979A21ED64857E6ECC43BC6AE7DA5CDBAB2905194A1501548E` |
| `outer_shock_zone` | `4DBF506BB27815E80E8CFB5143CA6E8DE48EF9CFF0DE1D62B328141DE8AF78B9` |
| `fragment_crater` | `9CAFD9B0C442DFA83BA28048BDDF2DEAB714D1C5E7F209AA0574932C884F1C87` |
| `heavy_fragment_damage` | `F2612AE7668DCFE399490C4E589E3C1D680A5CFF602086C02A915BAC370B2C1A` |
| `light_fragment_damage` | `8208509B1772E0E7DB90A43D0C6BD79254530893CCB1B1846C535A48FD9C1B22` |

The canonical library README and state rows in `CATALOG.md` at lines 340 through 344 were inspected, along with the family contact sheet and the individual native conscription-exemption reference.
Installed vanilla `gfx/interface/state_modifiers/modifiers_conscription_exemptions_granted.dds` decodes to the exact pixels of that inspected 32x32 canonical PNG.
Its owning vanilla `interface/countrystateview.gfx` sprite at lines 793 through 796 and the Sudetenland sprite at lines 1264 through 1267 were read directly.
That registry's SHA256 is `B12B196875611B51FB7DDE7F5F0893AFF0327D5AE848AFDA63D0AC77F18BBA8C`.
Offline `Graphical asset modding - Hearts of Iron 4 Wiki.md` at lines 30 through 80 documents sprite identity and relative texture paths, SHA256 `F8E3D4AD382F4E5F8E170492A484D090BAD62E3711CABFB5D3BF84E58AB32DD9`.

Required event inspection timed out after 600 seconds for both the corrected opening trace and its narrower single-node return-board retry.
The one-event options render was submitted separately and has not established current native acceptance.
The source and pixel evidence above does not replace an MCP render or live consumer evidence.
No dedicated Event 028 GUI, new icon family, or new placeholder is introduced.
Existing inherited-news master/provenance and overwritten rejected-candidate evidence limitations remain recorded in the final audit.

Skills used: `chaos-redux-event-assets`, `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.
