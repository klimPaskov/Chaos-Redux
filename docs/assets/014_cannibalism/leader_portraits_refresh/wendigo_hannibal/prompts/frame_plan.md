# Wendigo Hannibal canonical 16-frame plan

## Shared image-generation edit instruction

Treat the decoded `hannibal_wendigo.dds` as binding. Preserve the exact graphic black, bone-white, and red palette; central skull-mask identity; branching black crown silhouette; abstract white branch field; crop; camera; and flat painted texture. Redraw only the specified jaw, tongue, skull-fragment, eye, and branching motion. Keep the subject centred and readable as a 156x210 HOI4 portrait. Do not turn the portrait into a photograph, film still, prison scene, landscape, culturally specific ritual image, or generic monster bust.

| Frame | Motion state | Required generated state |
| --- | --- | --- |
| `000` | Canonical rest | Exact decoded canonical DDS; no generated alteration. |
| `001` | Eye ignition | Red eye accents brighten and the white jaw seam begins to separate. |
| `002` | Jaw unseals | Lower skull plate drops slightly; black mouth depth and a tongue tip are newly visible. |
| `003` | First gape | Jaw opens farther; the tongue curls toward lower camera-right and the branching silhouette flexes. |
| `004` | Reach | Tongue extends toward a small red-streaked white skull fragment entering at lower camera-right. |
| `005` | Coil | Tongue wraps once around the same fragment; jaw opens to half height. |
| `006` | Draw inward | Fragment moves toward the mouth under the tongue's pull; red accents flare along the jaw. |
| `007` | Maximum gape | Skull jaw opens beyond human range, fully exposing the abstract black maw while the fragment reaches the teeth. |
| `008` | Bite begins | Upper and lower white teeth close onto the fragment; the branching crown recoils. |
| `009` | Crush | Fragment visibly cracks into several painted white pieces with restrained red streaks. |
| `010` | First chew | Jaw rises and shifts; fragments move inside the black mouth and the tongue retracts halfway. |
| `011` | Second chew | Jaw closes farther; one last white fragment disappears behind the teeth. |
| `012` | Swallow | Mouth narrows, red throat accent descends, and the branching silhouette settles. |
| `013` | Jaw recovery | Lower skull plate returns toward its canonical position; tongue is no longer visible. |
| `014` | Locked stare | Jaw is nearly sealed; red eyes fix the viewer and remaining motion becomes minimal. |
| `015` | Loop bridge | Face, crown, jaw, and red accents settle very close to frame `000` for a clean blended return. |

## Output contract

- Canonical decoded source: `source_png/leader_ZZZ_hannibal_wendigo_static_source.png`.
- Source frames: `source_png/frames/leader_ZZZ_hannibal_wendigo_000_source.png` through `_015_source.png`.
- Processed frames: `processed_png/frames/leader_ZZZ_hannibal_wendigo_000.png` through `_015.png`.
- Static PNG: `processed_png/leader_ZZZ_hannibal_wendigo_static.png`.
- Sheet PNG: `processed_png/leader_ZZZ_hannibal_wendigo_sheet.png`.
- Static DDS: `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`.
- Sheet DDS: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds`.
- Preview: `previews/leader_ZZZ_hannibal_wendigo_preview.gif` at 12 fps.
- Contact sheets: source and processed under `contact_sheets/`.
