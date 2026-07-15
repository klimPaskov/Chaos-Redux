# HOI4 advisor and high-command icon references

These PNGs are extracted review copies of vanilla Hearts of Iron IV advisor
icons. They establish a separate `65x67` presentation target: a readable
HOI4-styled head-and-shoulders portrait inside a dark bevelled dossier card,
with the small paper overlay and transparent outer corners used by the
advisor/officer interface.

An advisor icon is not a shrunken `156x210` leader portrait. Build it from the
approved portrait master with its own crop and use
`.tools/process_hoi4_portrait.py advisor` to create the dossier presentation.
The script creates an original frame and paper overlay; it never copies a
vanilla advisor frame. Compare every candidate with this folder before DDS
conversion and wiring.

| Review file | Vanilla source |
| --- | --- |
| `vanilla_advisor_europe_1.png` | `gfx/interface/ideas/idea_generic_political_advisor_europe_1.dds` |
| `vanilla_advisor_europe_6.png` | `gfx/interface/ideas/idea_generic_political_advisor_europe_6.dds` |
| `vanilla_advisor_female_europe.png` | `gfx/interface/ideas/idea_generic_political_advisor_female_europe.dds` |
| `vanilla_advisor_africa_1.png` | `gfx/interface/ideas/idea_generic_political_advisor_africa_1.dds` |
| `vanilla_advisor_asia_1.png` | `gfx/interface/ideas/idea_generic_political_advisor_asia_1.dds` |
| `vanilla_high_command_fevzi_cakmak.png` | `gfx/interface/ideas/idea_tur_fevzi_cakmak_high_command.dds` |

All vanilla paths are relative to:
`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

Use `.tools/extract_hoi4_portrait_references.py` to recreate these reference
PNGs and the contact sheet from an installed game. The extracted images are
reference-only and must never be wired or shipped as Chaos Redux runtime art.
