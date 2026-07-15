# HOI4 leader portrait references

These PNGs are extracted review copies of vanilla Hearts of Iron IV leader
portraits. They establish the required Chaos Redux target: a `156x210`
painted portrait with a recognisable face, head-and-shoulders or restrained
bust framing, period-appropriate clothing, controlled contrast, a quiet
background, and no raw-photograph finish.

They are reference-only. Never wire them through a Chaos Redux `.gfx` file,
ship one as a mod portrait, or copy a depicted person into a different
identity.

| Review file | Vanilla source |
| --- | --- |
| `vanilla_den_thorvald_stauning.png` | `gfx/leaders/DEN/Portrait_Denmark_Thorvald_Stauning.dds` |
| `vanilla_ire_eamon_de_valera.png` | `gfx/leaders/IRE/Portrait_Ireland_Eamon_de_Valera.dds` |
| `vanilla_fin_carl_mannerheim.png` | `gfx/leaders/FIN/portrait_fin_carl_mannerheim.dds` |
| `vanilla_lux_charlotte.png` | `gfx/leaders/LUX/portrait_LUX_charlotte_wilhelmine.dds` |
| `vanilla_ice_sveinn_bjornsson.png` | `gfx/leaders/ICE/portrait_ice_sveinn_bjornsson.dds` |
| `vanilla_eth_haile_selassie.png` | `gfx/leaders/ETH/Portrait_Ethiopia_Haile_Selassie.dds` |

All vanilla paths are relative to:
`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

Use `.tools/extract_hoi4_portrait_references.py` to recreate the reference
set and contact sheet from an installed game. Use
`.tools/process_hoi4_portrait.py` only as the deterministic crop, finish, and
review step. Its output remains a candidate until a human visual comparison
confirms the face, framing, painted finish, clothing, and background against
this reference set.

For a real person, retain the attributed archival master and its source note,
select an explicit head-and-shoulders crop, and preserve their identity. Do
not reconstruct a missing face, exchange features, or turn an uncertain
source into a confident identification.
