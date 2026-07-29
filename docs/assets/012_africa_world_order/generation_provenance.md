# Event 012 world-order icon generation provenance

## Tool and model provenance

- Generation route: official OpenAI `image_gen.imagegen` tool required by the `imagegen` skill and `chaos-redux-event-assets`.
- Model identifier: the tool response does not expose a model name; no model name is inferred or substituted here.
- Generation date: 2026-07-29 (the generated-image directory was `019fafdd-a156-7be3-b818-4ec076e2103a`).
- All 15 source atlases were generated at 1254x1254 RGB with a flat `#00ff00` chroma-key field and a 4x4 row-major layout. The atlas files are preserved in `source_atlases/` and the original generated-image UUID filenames are recorded below.
- The official `remove_chroma_key.py` helper was used for each cropped source tile (`#00ff00`, soft matte, despill); final PNGs were resized to the existing Event 012 contracts and converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

## Atlas provenance and exact prompts

Each entry below records the original generated-image output and the prompt passed to `image_gen.imagegen`. Subjects are row-major; unused filler cells were not shipped.

### Focus atlases

| output UUID file | preserved atlas | shipped tiles |
| --- | --- | --- |
| `exec-7b9a2392-2520-4b0c-84aa-a92c67a6da76.png` | `focus_middle_east_atlas_01.png` | Middle East focus tiles 0-15 |
| `exec-1bad589d-e794-494c-a885-375684c76f20.png` | `focus_middle_east_atlas_02.png` | Middle East focus tiles 0-3 |
| `exec-733e55c1-e7c8-4b13-bca7-375007b49a25.png` | `focus_europe_atlas_01.png` | Europe focus tiles 0-15 |
| `exec-9f3f4770-07d2-40d9-827d-327474b8a6f9.png` | `focus_europe_atlas_02.png` | Europe focus tiles 0-3 |
| `exec-6817e9ce-bec7-4526-b896-6ff0855eee7e.png` | `focus_asia_atlas_01.png` | Asia focus tiles 0-15 |
| `exec-6ca36a73-1a2c-4449-a7ce-0066e757dfd2.png` | `focus_asia_atlas_02.png` | Asia focus tiles 0-3 |
| `exec-094a2082-bfde-4112-acf8-10ebcdbfb811.png` | `focus_north_america_atlas_01.png` | North America focus tiles 0-15 |
| `exec-c3bd000c-8d82-4c64-b302-030dfc2aec0e.png` | `focus_north_america_atlas_02.png` | North America focus tiles 0-3 |
| `exec-a5658359-60c7-425d-aecb-c933336ace55.png` | `focus_south_america_atlas_01.png` | South America focus tiles 0-15 |
| `exec-ab603020-6add-4a72-b1c3-d8bdb8a1f0d2.png` | `focus_south_america_atlas_02.png` | South America focus tiles 0-4 |
| `exec-1cd22ed3-64d4-40c5-970a-cdfccac78399.png` | `focus_oceania_atlas_01.png` | Oceania focus tiles 0-15 |
| `exec-19152052-e2b5-4b74-9451-c46c5d9106e8.png` | `focus_oceania_atlas_02.png` | Oceania focus tiles 0-3 |

Common exact focus prompt prefix and suffix (used for every focus atlas):

> Create a single 4 by 4 atlas of sixteen unique Hearts of Iron IV national-focus icon illustrations for a fictional [continent] world-order route. Each cell must contain one centered ornate emblem, no text, no letters, no flags, no logos, no UI frame. Use transparent-ready flat chroma key background #00ff00 in the gutters and behind each emblem; keep each emblem separated by clear green gutters. HOI4 vanilla focus-icon visual language: painterly but crisp, strong dark ink outline, controlled highlights, readable at 94x86, no photorealism. [row-major subject list]. Ensure every tile is visually distinct and centered with generous margin.

The subject lists are recorded in the atlas tile labels and in every manifest record's `source_tile`; the exact lists were: Middle East (crossroads balance; end foreign mandates; water/food; pipeline sovereignty; holy cities; Arab federal pact; plural crossroads federation; royal concert; socialist republics; desert covenant; federal chamber; protected communities; council of courts; republics coordination; nonhuman covenant terms; desert/mountain command; atlas 02: Red Sea/Nile treaty; withdrawal/guarantees law; crossroads settlement congress; sovereign settlement); Europe (continental settlement; border guarantees; industrial rail reconstruction; colonial reckoning; democratic federation; socialist union; royal concert; continental command; neutral confederation; mythic compact; federal chamber; congress of republics; council of crowns; emergency command statute; sovereignties council; nonhuman compact law; atlas 02: common army/air defence; withdrawal/crisis law; post-colonial treaty; ratify settlement); Asia (regional congresses; eastern/coastal centre; southern river centre; inland/steppe centre; archipelago centre; plural federation; revolutionary union; imperial congress; anti-colonial front; celestial covenant; federal centres chamber; congress of revolutionary republics; regional imperial chambers; liberation council; publish celestial covenant law; food/river/monsoon board; atlas 02: rail/maritime corridors; common defence/autonomy law; Indian Ocean partnership; ratify centres settlement); North America (continental bargain; industrial grid/transport; Caribbean/Central membership; Indigenous/regional settlement with respectful woven council; citizenship/mobility compact; republic of republics; continental commonwealth; hemisphere command; socialist continental union; storm frontier compact; bicameral congress; council of governments; civilian command statute; workers/republics congress; storm containment law; resources/withdrawal law; atlas 02: Atlantic/Pacific defence; Caribbean/Atlantic islands settlement; Africa diaspora citizenship treaty; ratify continental bargain); South America (three-regions balance; Andean transport; Amazon river/forest; Plata ports/two-ocean; resource concessions/debt audit; congress of republics; plural federation; socialist union; continental command; restored concert; sun covenant; republican chamber; council of three regions; workers/communes congress; civilian command statute; council of realms; atlas 02: publish sun covenant law; resource/debt sovereignty law; continental defence/corridors; South Atlantic partnership; ratify three-regions settlement); Oceania (ocean network; island congress/sovereignty; convoy/shipping; air routes/dispersed industry; island development/evacuation; anti-colonial liberation/land settlement; maritime federation; treaty dominion; indigenous-led ocean union with respectful oceanic meeting house and canoe motifs; socialist maritime commonwealth; deep-sea covenant; federal island chamber; dominion island council; people's ocean congress; workers/ports congress; deep-sea containment law; atlas 02: ocean constitution/withdrawal law; Pacific defence/disaster reserve; Indian Ocean/Southern Sea treaty; ratify ocean network).

### Idea atlases

| output UUID file | preserved atlas | shipped tiles |
| --- | --- | --- |
| `exec-506ad895-0380-4b8b-8254-d87ad3f77cbe.png` | `ideas_middle_east_europe_atlas.png` | Middle East tiles 0-5; Europe tiles 6-12 |
| `exec-17d4f0a4-a6a8-4b51-9d20-a4a1269e1104.png` | `ideas_asia_north_america_atlas.png` | Asia tiles 0-5; North America tiles 6-11 |
| `exec-e3ff3d77-200d-4b5e-a596-31b4ff77d61c.png` | `ideas_south_america_oceania_atlas.png` | South America tiles 0-6; Oceania tiles 7-12 |

Exact idea prompt used for all three atlases:

> Create one compact 4 by 4 atlas of sixteen unique Hearts of Iron IV national-idea icon illustrations. Every cell is one centered symbolic emblem designed for 64x64, ornate dark outline, painterly but crisp, no text, no letters, no flags, no logos, no UI frame. Use flat chroma-key green #00ff00 in gutters and behind each emblem for later transparency processing. Row-major [group-specific subject list]. Fill the remaining cells with additional distinct neutral diplomatic/continental/oceanic emblems. Keep the requested subjects visually distinct and readable at small size.

The group-specific subject lists are exactly the first shipped tiles in each manifest record: Middle East + Europe (13), Asia + North America (12), and South America + Oceania (13). No filler tile was shipped and no generated tile was rejected during contact-sheet review.

