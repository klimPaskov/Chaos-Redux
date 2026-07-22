# Leader portrait reference index

This directory is the user-requested, directly browsable HOI4 portrait-style
reference pack for agents. It contains a small male-only set of byte-identical
Vanilla HOI4 review PNGs under `leaders/` and `commanders/`, plus role-specific
contact sheets. The complete canonical library remains under
`../vanilla_reference/`; these copies are review material, never runtime assets.
Exact source mapping and SHA-256 values are in
[`REFERENCE_MANIFEST.md`](REFERENCE_MANIFEST.md).

## Route by HOI4 role

| HOI4 role | Canonical reference path | Native canvas | Quick-reference sheet |
| --- | --- | ---: | --- |
| Country leader | `../vanilla_reference/portraits/leaders/` | `156x210` | `leaders/contact_sheet.png` |
| Army or navy commander | `../vanilla_reference/portraits/commanders/` | `156x210` | `commanders/contact_sheet.png` |
| Operative | `../vanilla_reference/portraits/operatives/` | `156x210` | canonical family sheet only |

The curated pack contains four country leaders and four land/naval commanders,
all male-presenting and all `156x210`. It deliberately contains no Event 6
runtime art, generated people, female portraits, advisor icons, dossier cards,
or `_small` derivatives.

Before producing a portrait:

1. Read the canonical [library rules](../vanilla_reference/README.md) and
   [catalog](../vanilla_reference/CATALOG.md).
2. Inspect the matching canonical contact sheet and this pack's role-specific
   sheet.
3. Keep country-leader and commander textures as full `156x210` portraits.
4. For a grounded real person, retain an unchanged attributed source, make an
   explicit head-and-shoulders crop, and use ImageGen only as an
   identity-preserving HOI4-style edit of that exact crop.
5. Reject raw-photo finishes, generic oil filters, reconstructed faces, weak
   likenesses, beautification, and style treatments that materially change the
   person.

Reference PNGs may be viewed and supplied as style-only inputs. Do not recolour,
trace, wire, copy into runtime folders, or ship them as final Chaos Redux art.
