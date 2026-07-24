# Prompt and provenance record

Generation mode: official built-in ImageGen, one independent call per icon source. Each call used a structured stylized-concept prompt with `Asset type: Hearts of Iron IV national-spirit idea icon`, a single centered object group, painterly HOI4 idea-icon grammar, 1930s–1940s material mood, compact 60x68 readability, and a flat `#00ff00` chroma-key background for local alpha extraction.

Shared negative constraints for every call were: no text, letters, watermark, map, flag, UI frame, circular badge, modern objects, fake checkerboard, cast shadow, or opaque square. The source references were visual style guidance only; no reference pixels were copied, traced, recolored, or filtered into final art.

## Per-asset prompt subjects

| Source | Prompt subject and mechanic grounding |
| --- | --- |
| `idea_africa_priority_council_settlement_source.png` | Balanced council table, three carved stools, brass seal and linked papers for negotiated settlement. |
| `idea_africa_priority_civic_settlement_source.png` | Civic courthouse arch, open charter scroll and clasped hands for constitutional settlement. |
| `idea_africa_priority_producer_settlement_source.png` | Hammer, grain sheaf and workshop gate for producer/industrial settlement. |
| `idea_africa_priority_asante_problem_source.png` | Two intact civic ledgers split apart, mundane administrative ink seal in two pieces, failed railway/trade lines and closed intact civic canopy; explicitly no stool, throne, seat, regalia or sacred object. This replacement was generated after review rejected an earlier broken-stool concept. |
| `idea_africa_priority_asante_mature_source.png` | Three linked gold ingots, clasped ledgers, intact brass administrative seal, converging railway/trade lines and open civic canopy; explicitly no stool, throne, seat, regalia or sacred object. |
| `idea_africa_priority_oyo_problem_source.png` / `idea_africa_priority_oyo_mature_source.png` | Broken versus disciplined cavalry saddle, reins, lance and tribute chest for Oyo cavalry and tributary politics. |
| `idea_africa_priority_sokoto_problem_source.png` / `idea_africa_priority_sokoto_mature_source.png` | Split versus illuminated law tablet, scholar lamp and emirate seals for Sokoto scholarship and law. |
| `idea_africa_priority_kanem_bornu_problem_source.png` / `idea_africa_priority_kanem_bornu_mature_source.png` | Broken versus restored Lake Chad canoe, cavalry harness and manuscript bundle for lake trade and scholarship. |
| `idea_africa_priority_manden_problem_source.png` / `idea_africa_priority_manden_mature_source.png` | Snapped versus linked river-ferry chain, gold pan and caravan markers for Manden federation, gold and river routes. |
| `idea_africa_priority_kongo_problem_source.png` / `idea_africa_priority_kongo_mature_source.png` | Divided versus connected provincial seal, trade chain and generic cross-shaped charter token for Kongo provincial federation and diplomacy. |
| `idea_africa_priority_buganda_problem_source.png` / `idea_africa_priority_buganda_mature_source.png` | Torn versus aligned lakeside charts, royal drum and civic charter for Buganda court stability and administration. |
| `idea_africa_priority_aksum_problem_source.png` / `idea_africa_priority_aksum_mature_source.png` | Cracked versus restored highland road marker, lamp and supply crates for Aksum logistics and highland administration. |
| `idea_africa_priority_harar_problem_source.png` / `idea_africa_priority_harar_mature_source.png` | Congested versus balanced market gate, spice sacks, merchant ledgers and brass scale for Harar trade. |
| `idea_africa_priority_kilwa_problem_source.png` / `idea_africa_priority_kilwa_mature_source.png` | Splintered versus sturdy dhow mast/sail, harbor rope and dock pulley for Kilwa maritime trade and shipyards. |
| `idea_africa_priority_nubia_problem_source.png` / `idea_africa_priority_nubia_mature_source.png` | Collapsed versus reinforced river embankment, building plan and Nile ferry planks for Nubian federation and construction. |
| `idea_africa_priority_luba_problem_source.png` / `idea_africa_priority_luba_mature_source.png` | Separated versus linked generic council craft panel, iron bloom and memory beads for Luba councils, memory societies and iron. No sacred object is asserted. |
| `idea_africa_priority_lunda_problem_source.png` / `idea_africa_priority_lunda_mature_source.png` | Broken versus intact tribute chain, client-ruler staffs and trade caravan for Lunda federation incorporation and tribute. |
| `idea_africa_priority_great_zimbabwe_problem_source.png` / `idea_africa_priority_great_zimbabwe_mature_source.png` | Weathered/blocked versus sunlit intact stone wall, gold vein and resource markers for mining and local resources. |
| `idea_africa_priority_merina_problem_source.png` / `idea_africa_priority_merina_mature_source.png` | Blocked versus sturdy highland bridge, trade bundle and supply crates for Merina island logistics and trade. |
| `idea_africa_priority_zulu_problem_source.png` / `idea_africa_priority_zulu_mature_source.png` | Disordered versus aligned generic shield rack, assegai shafts and training cord for Zulu army organization and training. |

Processing provenance: `remove_chroma_key.py --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill` produced keyed intermediates in `validation/keyed/`; Pillow then fitted each alpha image inside a transparent 60x68 canvas. DDS conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 60 --height 68`. The converter output was decoded by `validation/validate_and_decode.py` and compared byte-for-byte at RGBA pixel level with the processed PNG.
