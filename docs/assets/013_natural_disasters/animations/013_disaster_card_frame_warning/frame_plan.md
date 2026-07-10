# 013 disaster card frame warning frame plan

| Frame | Motion state | Visual change | Prompt/source provenance | Anchor | Loop note |
| --- | --- | --- | --- | --- | --- |
| `000` | quiet warning | Faint amber trace at lower corners. | Atlas A, row 1; built-in `image_gen`. | center | Opening state. |
| `001` | rise | Signal climbs both sides. | Atlas A, row 2; built-in `image_gen`. | center | Easing in. |
| `002` | rise | Light reaches upper corners with small sparks. | Atlas A, row 3; built-in `image_gen`. | center | Easing in. |
| `003` | pre-peak | Most of the border is alive. | Atlas A, row 4; built-in `image_gen`. | center | Static fallback. |
| `004` | peak | Full uneven amber rim and corner sparks. | Atlas B, row 1; built-in `image_gen`. | center | Loop apex. |
| `005` | fall | Top center darkens and filaments segment. | Atlas B, row 2; built-in `image_gen`. | center | Easing out. |
| `006` | low warning | Light remains on sides and lower corners. | Atlas B, row 3; built-in `image_gen`. | center | Returning. |
| `007` | reset bridge | One faint lower-corner trace remains. | Atlas B, row 4; built-in `image_gen`. | center | Visually approaches `000`. |

Every row is separately drawn source art. Local processing only split the two atlases, removed the chroma key, resized to the shared frame canvas, and assembled review/game outputs.
