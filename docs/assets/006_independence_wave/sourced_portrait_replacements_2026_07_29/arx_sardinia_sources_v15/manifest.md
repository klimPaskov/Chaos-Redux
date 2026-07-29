# Event 006 ARX sourced male portrait research v15

Date: 2026-07-29.

Scope: source masters and exact pixel crops only for the three live ARX large-portrait consumers, with collision and rights research for nearby Sardinian candidates.

This package contains no generated repaint, resized 156x210 finish, DDS, GFX edit, localisation edit, advisor icon, dossier art, or gameplay change.

## Disposition summary

| Consumer | Identity | Source disposition | Roster disposition | Decision boundary |
|---|---|---|---|---|
| `ARX_sardinian_provisional_assembly` | Emilio Lussu | `source_ready_for_parent_review` | `needs_user_review` | The Senate portrait is clearer than the failed 1916 trial and is CC BY 3.0 IT, but Commons only dates it `before 1958`; downstream likeness/style audit is still required and the existing failed repaint remains blocked. |
| `ARX_sardinian_crown_consultative_council` | Luigi Arborio Mella di Sant'Elia | `source_ready_for_parent_review` | `needs_user_review` | Sardinian-born court official and royal confidant with a Senate CC BY 3.0 IT source and no owner collision; the Commons date is only bounded before 1955 and the 153x193 source is small, so parent visual/era review is required. |
| `ARX_gavino_piras` | Vittorio Vernè | `source_ready_for_parent_review` | `needs_user_review` if a Sardinia-linked commander is accepted; `blocked_strict_birth_requirement` otherwise | Commons records anonymous 1930s PD-Italy plus PD-1996 and the prior role audit documents 1936 general command and a Sardinia-linked formation, but Vernè was born in Rome rather than Sardinia. |

## Source inventory

| Identity and role | Unchanged source master | Dimensions / SHA-256 | Exact crop | Crop dimensions / SHA-256 | Provenance and rights |
|---|---|---|---|---|---|
| Emilio Lussu, civic leader | [`source_masters/emilio_lussu_senate_pre1958.jpg`](source_masters/emilio_lussu_senate_pre1958.jpg) | 180x253 / `23b0f650f56cb7aeeb017bcad7cde5186d190cb05f6bab99f8656efd895489a0` | [`source_crops/emilio_lussu_senate_pre1958_crop.png`](source_crops/emilio_lussu_senate_pre1958_crop.png), `(0,0,180,253)` | 180x253 / `0440330b7d53bd8fa44b8af38e8452304b624208a5e0fbb89d416293a448c78b` | [Commons File:Emilio Lussu.jpg](https://commons.wikimedia.org/wiki/File:Emilio_Lussu.jpg), Senate of the Republic source record, unknown photographer, `before 1958`, `CC BY 3.0 IT` via `{{Senato.it}}`. |
| Luigi Arborio Mella di Sant'Elia, crown/council | [`source_masters/luigi_mella_santelia_senate.gif`](source_masters/luigi_mella_santelia_senate.gif) | 153x193 / `7ada408f2c89d94cd54e19ff9d6914311881df964b434b2aaf8a89a84148802e` | [`source_crops/luigi_mella_santelia_crop.png`](source_crops/luigi_mella_santelia_crop.png), `(0,0,153,193)` | 153x193 / `530ed290cb842e435f61e6f796302bbedfe045627f7d36c465d2802fac8d0515` | [Commons File:Mella di Sant'Elia.gif](https://commons.wikimedia.org/wiki/File:Mella_di_Sant%27Elia.gif), Senate of the Republic source record, unknown photographer, `before 1955-06-26`, `CC BY 3.0 IT` via `{{Senato.it}}`. |
| Vittorio Vernè, Sardinia-linked commander | [`source_masters/vittorio_verne_commander_commons.jpg`](source_masters/vittorio_verne_commander_commons.jpg) | 200x250 / `de94df14318398914a51aa0fb6601f9c31f916cc98d3803b313fe33be15f1417` | [`source_crops/vittorio_verne_commander_crop.png`](source_crops/vittorio_verne_commander_crop.png), `(7,0,193,250)` | 186x250 / `752046992ffb8c244b1b480b728f1d79988d3683e1d61532903e374027f42b09` | [Commons File:Vittorio Vernè.jpg](https://commons.wikimedia.org/wiki/File:Vittorio_Vern%C3%A8.jpg), anonymous photograph sourced to Generals.dk, `anni 30`, `PD-Italy` plus `PD-1996`. Copied byte-for-byte from the prior bounded ARX package. |

## Nearby researched candidates and dispositions

| Candidate | Evidence | Disposition |
|---|---|---|
| Giuseppe Valle | [`source_masters/giuseppe_valle_1936_encyclopedia.png`](source_masters/giuseppe_valle_1936_encyclopedia.png), 417x488, SHA-256 `f9499f2a5c2421a2195c58f371abd8712b2d00b5b639bfabd0f154ee6c890802`; [Commons File:Giuseppe Valle.png](https://commons.wikimedia.org/wiki/File:Giuseppe_Valle.png), *Grande enciclopedia aeronautica 1936*, `before 1936`, `PD-Italy` plus `PD-1996`; born Sassari and Air Staff chief 1934-1939. | `blocked_owner_collision`: Kaiserreich owns `SRD_giuseppe_valle` in `common/characters/SRD characters.txt:129-148`, recruits it in `history/countries/SRD - Sardinia.txt:173`, and registers large/small portraits in `interface/kaiserreich/portraits/SRD_portraits.gfx:27-32`; no guarded transfer is in scope. The exact crop is retained at [`source_crops/giuseppe_valle_1936_crop.png`](source_crops/giuseppe_valle_1936_crop.png), `(0,0,417,488)`, SHA-256 `994fd73efdfc2dd92fee0c526e86758ff5df9b259221d850e41726b1fc9c64be`. |
| Giuseppe Pizzorno | [`source_masters/giuseppe_pizzorno_commons_lowres.jpg`](source_masters/giuseppe_pizzorno_commons_lowres.jpg), 145x160, SHA-256 `66f9a1628394675b0bd182a56b51bd7345679bfbd8386c0a199003cab06b7318`; [Commons File:Giuseppe Pizzorno.jpg](https://commons.wikimedia.org/wiki/File:Giuseppe_Pizzorno.jpg), L'Unione Sarda, unknown photographer, photo antecedent to 1955, `PD-Italy` plus `PD-1996`; born Cagliari, general, Brigata Sassari commander, East Africa staff/command service, and 1935-1936 operations are documented in the Italian biography. | `blocked_source_quality`: no owner collision was found, but the only attributed headshot is a 145x160 side-profile thumbnail with an unknown capture date and insufficient detail for a defensible identity-preserving repaint. The exact full-frame crop is retained at [`source_crops/giuseppe_pizzorno_lowres_crop.png`](source_crops/giuseppe_pizzorno_lowres_crop.png), `(0,0,145,160)`, SHA-256 `6e08a86e5c14bc7727faa7745dbf528522410e43c973f40795c65e6ae978fe0f`. |

## Rejected Lussu alternate

The 1945 De Gasperi group photograph is retained only as provenance evidence at [`source_masters/emilio_lussu_degasperi_1945.jpg`](source_masters/emilio_lussu_degasperi_1945.jpg), 1228x698, SHA-256 `f03a45e17e3efed1173c718d1c9db1d13606857f16d620f90e763cebc1001f10`.

Its [Commons record](https://commons.wikimedia.org/wiki/File:PRIMO_GOVERNO_DE_GASPERI%2C_CON_NENNI%2C_TOGLIATTI%2C_LUSSU_E_CATTANI.jpg) gives date 1945, unknown author, JOYCE LUSSU / Portrait / Transeuropa source credit, and `PD-Italy` plus `PD-1996`.

Lussu is at the far left in side profile with a small face in a crowded group, so no exact portrait crop was made and the image is `rejected_unsuitable_portrait_source`.

## Exact-crop verification

Each PNG crop was created with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` and its paired JSON records `exact_source_crop_verified`, decoded RGBA pixel equality, source dimensions, source hash, crop rectangle, and the normalized command.

No crop was resized, recoloured, retouched, sharpened, or otherwise interpreted.

