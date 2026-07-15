# Event 006 northern and western Europe generated-art prompts

## Production rules shared by every prompt

The four live country flags were generated in four separate official ImageGen
calls. Each call received one rights-cleared historical flat-design reference
and one canonical vanilla HOI4 normal/medium/small flag ladder as visual inputs.
The historical reference controls the design; the vanilla ladder controls only
flat presentation and small-size readability. The prompts forbid fabric,
lighting, perspective, decoration, text, watermarks, and alternate redesigns.

The portrait prompts below remain independent portrait-generation records. No
historical portrait, living person, named historical figure, or generated image
from another tag was supplied as a portrait reference.

## Live historical flag prompts and provenance

Every call requested a 3:2, front-facing, edge-to-edge orthographic flag. Raw
ImageGen outputs are retained unchanged in `../source_png/generated_nwe/flags/`.
The build tool maps those raw pixels to the documented exact palette without
dithering, never imports a reference mask, and never traces or redraws a symbol.
For ACX only, it deterministically promotes one almost-solid noisy cross-edge
scanline to the adjacent white field. The normal flag is resized from that flat
master; medium and small are resized from normal with no bespoke redesign.

### ACX Cornwall — St Piran's Cross

Historical input: `../source_png/country_symbols/acx_st_pirans_cross_source.png`
([Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Flag_of_Cornwall.svg),
public domain); identity and proportion check:
[Flag Institute UK Flag Registry](https://www.flaginstitute.org/wp/flags/cornwall-flag/).
Canonical presentation input: `arm.png` at all three vanilla-reference sizes.

> Reproduce the attached historical St Piran's Cross design exactly as a clean
> flat flag: one plain white upright cross on a solid black field, with the same
> centered geometry and no added charge. Output one edge-to-edge 3:2
> orthographic flag master. No pole, border, folds, fabric texture, lighting,
> shadow, depth, gradient, weathering, caption, lettering, watermark, mockup,
> modern logo, or alternate redesign. Use the attached canonical vanilla HOI4
> flag ladder only as a reference for flat graphic clarity at small size.

Raw ImageGen output:
`C:/Users/klimp/.codex/generated_images/019f64f5-0142-7ea2-9be6-3b919c017427/exec-7f7bae87-7c21-433f-bf73-adbbdaca7976.png`.
Repo copy: `../source_png/generated_nwe/flags/ACX_st_pirans_cross_imagegen_raw.png`.
Flat master: `../source_png/generated_nwe/flags/ACX_st_pirans_cross_imagegen_flat_master.png`.
Exact output palette: `#000000`, `#FFFFFF`.

### AEX retirement boundary

AEX is a vanilla `BEL_flanders` cosmetic overlay, not a standalone Event 006
country. No AEX flag prompt is active. The obsolete generated AEX civic master,
processed previews, and runtime TGA triplet are retired and the build validator
requires them to remain absent. The historical Lion of Flanders arms source is
retained only as evidence for the existing vanilla cosmetic overlay.

### AFX Wallonia — 1913 coq hardi

Historical input: `../source_png/country_symbols/afx_walloon_rooster_source.png`
([Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Flag_of_Wallonia.svg),
CC0); historical identity check:
[Wallonia Public Service](https://connaitrelawallonie.wallonie.be/histoire-et-symboles/symboles/un-embleme-le-coq-hardi).
Canonical presentation input: `isr.png` at all three vanilla-reference sizes.

> Reproduce the attached Walloon coq hardi flag design exactly as a clean flat
> flag: one red coq hardi, beak closed and dexter leg raised, centered on one
> solid yellow field. Preserve its single-charge arrangement and orientation.
> Output one edge-to-edge 3:2 orthographic flag master. No pole, border, folds,
> fabric texture, lighting, shadow, depth, gradient, weathering, caption,
> lettering, watermark, mockup, modern logo, or alternate redesign. Use the
> attached canonical vanilla HOI4 flag ladder only as a reference for flat
> graphic clarity at small size.

Raw ImageGen output:
`C:/Users/klimp/.codex/generated_images/019f64f5-0142-7ea2-9be6-3b919c017427/exec-96127640-0f4b-4a81-b6db-f17f28e66008.png`.
Repo copy: `../source_png/generated_nwe/flags/AFX_walloon_coq_hardi_1913_imagegen_raw.png`.
Flat master: `../source_png/generated_nwe/flags/AFX_walloon_coq_hardi_1913_imagegen_flat_master.png`.
Exact output palette: `#FFD100`, `#E4002B`.

### AGX Friesland — provincial flag

Historical input: `../source_png/country_symbols/agx_west_frisian_flag_source.png`
([Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Frisian_flag.svg),
public domain); official design check:
[Province of Fryslân](https://www.fryslan.frl/friese-vlag).
Canonical presentation input: `ice.png` at all three vanilla-reference sizes.

> Reproduce the attached Friesland provincial flag design exactly as a clean
> flat flag: seven alternating diagonal bands, four blue and three white, with
> exactly seven red pompeblêden in the documented arrangement. Preserve the
> diagonal direction, symbol count, and orientation. Output one edge-to-edge
> 3:2 orthographic flag master. No pole, border, folds, fabric texture,
> lighting, shadow, depth, gradient, weathering, caption, lettering, watermark,
> mockup, modern logo, extra symbols, or alternate redesign. Use the attached
> canonical vanilla HOI4 flag ladder only as a reference for flat graphic
> clarity at small size.

Raw ImageGen output:
`C:/Users/klimp/.codex/generated_images/019f64f5-0142-7ea2-9be6-3b919c017427/exec-8553e19e-c7ad-4591-95f2-845eeaddcc52.png`.
Repo copy: `../source_png/generated_nwe/flags/AGX_friesland_provincial_imagegen_raw.png`.
Flat master: `../source_png/generated_nwe/flags/AGX_friesland_provincial_imagegen_flat_master.png`.
Exact output palette: `#244994`, `#FFFFFF`, `#E72326`.

### AJX Saar — Territory flag, 1920–1935

Historical input:
`../source_png/country_symbols/ajx_saar_territory_1920_1935_source.png`
([Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Flag_of_Saar_1920-1935.svg),
public domain); institutional check:
[Saarland State Chancellery](https://artsandculture.google.com/story/saarhundert-das-saargebiet-ein-kind-der-internationalen-v%C3%B6lkergemeinschaft-staatskanzlei-saarland/kQWBBjUfmhpHJA?hl=en).
Canonical presentation input: `arm.png` at all three vanilla-reference sizes.

> Reproduce the attached Saar Territory 1920–1935 flag design exactly as a
> clean flat flag: three equal horizontal bands in blue, white, and black from
> top to bottom. Preserve the stripe order, equal geometry, and orientation.
> Output one edge-to-edge 3:2 orthographic flag master. No pole, border, folds,
> fabric texture, lighting, shadow, depth, gradient, weathering, caption,
> lettering, watermark, mockup, modern logo, emblem, or alternate redesign. Use
> the attached canonical vanilla HOI4 flag ladder only as a reference for flat
> graphic clarity at small size.

Raw ImageGen output:
`C:/Users/klimp/.codex/generated_images/019f64f5-0142-7ea2-9be6-3b919c017427/exec-801f7d89-ac0f-4f24-845a-19118f40caa2.png`.
Repo copy: `../source_png/generated_nwe/flags/AJX_saar_territory_1920_1935_imagegen_raw.png`.
Flat master: `../source_png/generated_nwe/flags/AJX_saar_territory_1920_1935_imagegen_flat_master.png`.
Exact output palette: `#00209F`, `#FFFFFF`, `#000000`.

## Institutional council portrait prompts

Each prompt requested one vertical 1930s institutional portrait: a fictional
ensemble rather than a fake historical individual, painterly realism consistent
with HOI4 leader art, no text, and enough head-and-torso clearance for a
156×210 crop.

### ACX — Cornish Port and Mines Security Committee

> Paint a fictional late-1930s Cornish port-and-mines emergency committee as a
> formal institutional portrait. Four distinct delegates—harbor worker, mine
> representative, municipal clerk, and local civil-defense official—confer
> around a map table. Show a rough Atlantic harbor, crane, miner's lamp, and a
> black-and-white cross textile as environmental clues. Serious cooperative
> mood, modest civilian clothing, no named or recognizable person.

### AEX — Flemish Civil-Industrial Security Board

> Paint a fictional late-1930s Flemish civil-industrial security board as a
> formal institutional portrait. Four delegates representing rail, factory,
> municipal administration, and civil security meet around plans in an office
> overlooking brick industry and rail sidings. A small black-lion relief may
> appear on the wall. Restrained dark workwear and suits, no modern insignia,
> no named or recognizable person.

### AFX — Walloon Provisional Assembly

> Paint a fictional late-1930s Walloon provisional assembly as an institutional
> portrait. Four delegates—a mineworker, steel engineer, municipal magistrate,
> and reserve inspector—meet around papers and a valley map, with coal, steel,
> and smokestacks visible behind them. Include a discreet red-rooster civic
> relief, not a copied flag. Industrial dignity, mixed civilian roles, no named
> or recognizable person.

### AGX — Friesland Coastal Council

> Paint a fictional late-1930s Friesland coastal council as an institutional
> portrait. Four delegates from municipal government, harbor labor, dike
> engineering, and coastal constabulary study a flood-defense chart in a room
> overlooking a dike and small harbor. A discreet red pompeblêd tile may appear
> among blue-and-white details. Bounded Friesland identity, no pan-Frisian
> claim, no named or recognizable person.

### AJX — Saar Municipal Neutral Commission

> Paint a fictional late-1930s Saar municipal neutral commission as an
> institutional portrait. Four delegates—municipal jurist, mine representative,
> rail administrator, and industrial-security official—sit around a ledger and
> sealed correspondence with mineworks outside. Include a restrained
> blue-white-black ribbon as commission memory, without copying a flag. Neutral
> administrative mood, no named or recognizable person.

## Regional officer portrait prompts

Each officer was generated independently in a separate ImageGen call. All five
are fictional male-presenting people; none is intended to depict a real person.
The large 156×210 and small 50×67 runtime files are deterministic crops of the
same tag-specific generated master.

### ACX — Thomas Trevorrow

> Paint one fictional male Cornish coastal-defense officer in a late-1930s
> civilian harbor-security uniform, head-and-torso vertical portrait. Place him
> in a harbor office with an Atlantic breakwater, crane, and miner's safety lamp
> behind him. Navy work coat and plain peaked cap, resolute but not militarist,
> no rank copied from a real service, no recognizable person.

### AEX — Hendrik Vermeulen

> Paint one fictional male Flemish industrial-security commander in a
> late-1930s dark civil-guard uniform, head-and-torso vertical portrait. A brick
> factory district, freight railway, rolled plans, and measuring instruments
> establish his role. Plain geometric collar tabs without national or ideology
> insignia, composed professional expression, no recognizable person.

### AFX — Marcel Delcourt

> Paint one fictional male Walloon reserve commander in late-1930s industrial
> emergency clothing, head-and-torso vertical portrait. Give him a weathered
> field coat and dark burgundy scarf with a coal tipple, steelworks, smoke, and
> miner's lamp behind him. He should look like a reserve organizer drawn from
> the industrial valleys, not a regular-army celebrity; no recognizable person.

### AGX — Sjoerd Hoekstra

> Paint one fictional male Frisian coastal-constabulary commander in a
> late-1930s navy weather coat and plain peaked cap, head-and-torso vertical
> portrait. Set him on a windswept dike or harbor station with signal lamp,
> mast, small sailing craft, and binoculars. Practical coastal-service bearing,
> no national or ideology insignia, no recognizable person.

### AJX — Karl Becker

> Paint one fictional male Saar industrial-security commissioner in a
> late-1930s charcoal municipal guard uniform, head-and-torso vertical portrait.
> Place him in an administrative office overlooking a mine headframe, with a
> ledger, sealed document, and safety lamp. Plain cap and leather dispatch case,
> neutral commission bearing, no political insignia, no recognizable person.
