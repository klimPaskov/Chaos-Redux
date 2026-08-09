# Archival decision-category picture handoff

This handoff covers only the three static decision-category pictures requested by the parent task. The selected consumers are the larger decision-category `picture` surface, not small category icons or scripted-GUI backgrounds, and every final texture uses the active 114x101 canvas.

## Requirement-to-runtime crosswalk

| Category consumer | Exact sprite name | Processed review PNG | Final runtime DDS | Status |
| --- | --- | --- | --- | --- |
| `chaosx_communism_fight_category` in `common/decisions/categories/001_communism_spread_categories.txt` | `GFX_decision_cat_picture_communist_insurgency` | `docs/assets/decision_category_formable_state_puzzle/processed/decision_cat_picture_communist_insurgency.png` | `gfx/interface/decisions/001_communism_spread/decision_cat_picture_communist_insurgency.dds` | complete, pending parent `.gfx` wiring |
| `chaosx_space_race_decision_category` in `common/decisions/categories/044_space_race_categories.txt` | `GFX_decision_cat_picture_space_race` | `docs/assets/decision_category_formable_state_puzzle/processed/decision_cat_picture_space_race.png` | `gfx/interface/decisions/044_space_race/decision_cat_picture_space_race.dds` | complete, pending parent `.gfx` wiring |
| `chaosx_greenland_sale_category` in `common/decisions/categories/092_greenland_sale_categories.txt` | `GFX_decision_cat_picture_greenland_sale` | `docs/assets/decision_category_formable_state_puzzle/processed/decision_cat_picture_greenland_sale.png` | `gfx/interface/decisions/092_greenland_sale/decision_cat_picture_greenland_sale.dds` | complete, pending parent `.gfx` wiring |

The source archive, processing previews, review contact sheet, and provenance evidence remain under `docs/assets/decision_category_formable_state_puzzle/` while the parent completes integration. The review contact sheet is `docs/assets/decision_category_formable_state_puzzle/contact_sheet.png` and is not a runtime asset.
## Manifest rows

| Asset | Source file and source page | License or rights | Date and era fit | Uncertainty | Runtime path and sprite |
| --- | --- | --- | --- | --- | --- |
| Communist insurgency | `docs/assets/decision_category_formable_state_puzzle/source/communist_insurgency_source.jpg`; [LOC item](https://www.loc.gov/resource/ds.17451/) | LOC: no known restrictions on publication; Commons: public domain in the United States because copyright was not renewed | circa 1930–1940; period archival labor/Communist demonstration | Commons warns that non-US jurisdictions may differ; retain attribution to Underwood & Underwood and Library of Congress | `gfx/interface/decisions/001_communism_spread/decision_cat_picture_communist_insurgency.dds`; `GFX_decision_cat_picture_communist_insurgency` |
| Space race | `docs/assets/decision_category_formable_state_puzzle/source/space_race_saturn_v_engines_ignite_source.jpg`; [NASA image page](https://www.nasa.gov/image-detail/saturn-v-engines-ignite/) | NASA-produced image, public domain in the United States unless otherwise noted | 16 July 1969; direct Apollo-era space-race launch photograph | NASA logo/endorsement restrictions apply in other uses, but no logo or endorsement text is present in this crop | `gfx/interface/decisions/044_space_race/decision_cat_picture_space_race.dds`; `GFX_decision_cat_picture_space_race` |
| Greenland sale | `docs/assets/decision_category_formable_state_puzzle/source/greenland_wdl11258_source.png`; [Commons WDL11258 record](https://commons.wikimedia.org/wiki/File:Map_of_Greenland_WDL11258.png) | Public Domain Mark 1.0 for the faithful reproduction of a public-domain map; underlying work by Hans Poulsen Egede | 4 January 1737; archival Danish map of Greenland and its west coast | Source covers the west coast rather than the full island; faithful-reproduction reuse caveat is preserved; Wikimedia CDN required transparent proxy retrieval | `gfx/interface/decisions/092_greenland_sale/decision_cat_picture_greenland_sale.dds`; `GFX_decision_cat_picture_greenland_sale` |


## Sourced assets and provenance

### Communist insurgency

The source is `docs/assets/decision_category_formable_state_puzzle/source/communist_insurgency_source.jpg` with SHA-256 `86599fc519f42175ae55aab064e2f70eea8f4b19f85fcecc3bf68518db0c6cd4` and native dimensions 879x1024 RGB JPEG.

The archival record is the Library of Congress item [Communists' party demonstration in Union Sq. May Day 193?](https://www.loc.gov/resource/ds.17451/) and its [JSON metadata record](https://www.loc.gov/resource/ds.17451/?fo=json); the downloaded source endpoint is `https://tile.loc.gov/storage-services/service/pnp/ds/17400/17451v.jpg`.

The image is credited to Underwood & Underwood and dated by the Library of Congress to between circa 1930 and circa 1940. The Library of Congress rights advisory says "No known restrictions on publication." The matching [Wikimedia Commons record](https://commons.wikimedia.org/wiki/File:Communists%27_party_demonstration_in_Union_Sq._May_Day_193%3F.jpg) identifies the work as public domain in the United States because it was published between 1931 and 1963 and the copyright was not renewed, while warning that terms can differ in jurisdictions that do not apply the rule of the shorter term.

The crop removes the scanned mounting board and handwritten edge marks and keeps the original street scene with Communist banners, newspaper signage, and the marching crowd. The source crop box is `(left=124, top=170, right=840, bottom=805)`; the aspect fit produces a 716x634 crop before the final 114x101 LANCZOS resize.

### Space race

The source is `docs/assets/decision_category_formable_state_puzzle/source/space_race_saturn_v_engines_ignite_source.jpg` with SHA-256 `8be56cecf5ff8898ca9ea9213a67d7dbd3bbf49d0189d70ac909f219d8ab1ed7` and native dimensions 1041x1358 RGB JPEG.

The source is the official NASA [Saturn V Engines Ignite](https://www.nasa.gov/image-detail/saturn-v-engines-ignite/) image page and direct download `https://www.nasa.gov/wp-content/uploads/2023/03/624181main_1969-07-16-4_full.jpg`. NASA identifies the photograph as the Apollo 11 Saturn V liftoff from Kennedy Space Center on 16 July 1969, credits NASA, and labels the page image 1041x1358 pixels.

NASA-produced material is public domain in the United States unless otherwise noted. The image contains no NASA logo or endorsement text, and the handoff preserves the requested NASA credit. NASA branding and endorsement restrictions still apply to any future use outside this texture handoff.

The crop retains the rocket nose, smoke plume, launch tower, and coastal launch complex in a single period photograph. The source crop box is `(left=0, top=0, right=1041, bottom=922)`; the final 1041x922 crop is resized to 114x101 with LANCZOS.

### Greenland sale

The selected source is `docs/assets/decision_category_formable_state_puzzle/source/greenland_wdl11258_source.png` with SHA-256 `f6b3c2d9eb2e6e54a97e72f8d099727dd75353f7b8363d0e26c8b20b6b96f5ca` and native dimensions 1283x1024 RGB PNG.

The archival record is [Map of Greenland WDL11258](https://commons.wikimedia.org/wiki/File:Map_of_Greenland_WDL11258.png), sourced by the record to the [World Digital Library item 11258](http://www.wdl.org/en/item/11258/) and the original download URL `http://dl.wdl.org/11258.png`. The map is attributed to Hans Poulsen Egede (1686–1758), dated 4 January 1737, held by the Royal Library of Denmark, and describes the west coast of Greenland with Danish annotations, a compass, and a lower-right cartouche scene. The Commons record marks the faithful reproduction Public Domain Mark 1.0 and notes the underlying work is public domain; it also records the usual jurisdiction caveat for faithful reproductions of public-domain art.

The local copy was retrieved through the transparent image proxy `https://images.weserv.nl/?url=upload.wikimedia.org%2Fwikipedia%2Fcommons%2Fc%2Fc5%2FMap_of_Greenland_WDL11258.png` because Wikimedia's CDN returned a bot-rate response during acquisition. The canonical Commons and World Digital Library URLs above remain the provenance authorities, and the downloaded file is retained unchanged in the source archive after retrieval.

The crop keeps the antique west-coast map, central compass, and the lower-right Danish cartouche scene that makes the territory and historical sovereignty legible at tiny size. The source crop box is `(left=100, top=70, right=1175, bottom=1010)`; the aspect fit produces a 1061x940 crop before the final 114x101 LANCZOS resize.

A second public-domain candidate, `docs/assets/decision_category_formable_state_puzzle/source/greenland_major1874_source.jpg`, was retained for review only. Its [Commons record](https://commons.wikimedia.org/wiki/File:MAJOR%281874%29_p67_Map_of_Greenland.jpg) identifies a circa 1875 British Library Mechanical Curator scan and Public Domain Mark, but the map covers only south-west Greenland and reads as sparse cartography at 114x101, so it was rejected in favor of the Egede map. It is shown as the rejected alternative on the contact sheet and is not a runtime consumer.

## Final DDS evidence

All three runtime outputs were produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` from the processed PNGs using `--width 114 --height 101`. Each file is a 46,184-byte legacy one-level uncompressed BGRA DDS with a 128-byte header, `DDS_HEADER` size 124, `DDS_PIXELFORMAT` size 32, flags 65, fourCC 0, 32-bit BGRA masks, `DDSCAPS_TEXTURE` 0x1000, and no mipmaps. The decoded pixel round trip matches the processed PNG byte-for-byte after BGRA-to-RGBA channel conversion, and every alpha byte is 255 because these are opaque category pictures.

| Runtime DDS | Processed PNG SHA-256 | DDS SHA-256 | Dimensions | Alpha min/max | Crop status |
| --- | --- | --- | --- | --- | --- |
| `gfx/interface/decisions/001_communism_spread/decision_cat_picture_communist_insurgency.dds` | `4ae3dd801d7a822ad7e0e7af5cf67807ccfd00727c811ddb38f96f1d12172bfa` | `1b6e63bce1e36406f1419af5d0180abe6e0003a2458c826f3a1fd781b1996b73` | 114x101 | 255/255 | scanned mount removed; banners and crowd retained |
| `gfx/interface/decisions/044_space_race/decision_cat_picture_space_race.dds` | `de0b64dc76731621ddae4ab997ccd664ece204378b80b04aadf84cb41107bd67` | `8fa6eb91e1b2570a7f8f2e45365204ab7c843de8db3ec61efcc4c056e1fc71d9` | 114x101 | 255/255 | rocket nose, plume, tower, and coast retained |
| `gfx/interface/decisions/092_greenland_sale/decision_cat_picture_greenland_sale.dds` | `e43f67775197c23c991304f14ae9f9edeed89705f0da2e1b81328a68efc628bf` | `3d60d479a1f34c5d6ad1c1da7acaf00b67f8522ad999a1884553cda13aa572b7` | 114x101 | 255/255 | antique map, compass, and cartouche retained |

## Parent wiring handoff

The parent should add the three sprite definitions to the appropriate existing `.gfx` file without changing the sprite names or runtime DDS paths:

```text
spriteType = {
	name = "GFX_decision_cat_picture_communist_insurgency"
	texturefile = "gfx/interface/decisions/001_communism_spread/decision_cat_picture_communist_insurgency.dds"
}
spriteType = {
	name = "GFX_decision_cat_picture_space_race"
	texturefile = "gfx/interface/decisions/044_space_race/decision_cat_picture_space_race.dds"
}
spriteType = {
	name = "GFX_decision_cat_picture_greenland_sale"
	texturefile = "gfx/interface/decisions/092_greenland_sale/decision_cat_picture_greenland_sale.dds"
}
```

The parent remains responsible for the category `picture =` fields, `.gfx` registration, localisation, gameplay references, and final in-game validation. This subtask did not edit category gameplay, localisation, or any interface `.gfx` file.

## Reference and validation notes

The canonical decision-category picture family was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/`, including its 114x101 PNG examples, `contact_sheet.png`, `README.md`, `CATALOG.md`, and `REFERENCE_MANIFEST.md`. The offline [Decision modding wiki page](../../../../paradox_wiki/Decision%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) confirms that category pictures are sprite-backed `picture` fields that appear beside the category description, and the installed Vanilla precedent in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/decisions.gfx` uses `GFX_decision_cat_picture_*` sprites pointing to `gfx/interface/decisions/*.dds`.

No generated substitutes or unapproved fallbacks were used. The communist image carries a jurisdiction caveat in the source record, and the Greenland map is a historical west-coast map rather than a modern full-island political map; both facts are preserved here for parent review rather than silently hidden.
