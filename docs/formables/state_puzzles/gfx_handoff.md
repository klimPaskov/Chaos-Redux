# Formable state-puzzle outline repair handoff

The five category families share the outline treatment used by the unchanged form_commonwealth runtime pair while retaining their existing state map silhouettes, texture dimensions, sprite ids, anchors, fill and hatch colours, and geometry artifacts.

The affected families are form_baltic_federation_category (28 pieces), form_baltic_sea_empire_category (82), form_north_sea_category (56), form_scandinavia_category (58), and form_sweden_hungary_category (36), for 260 unresolved/qualifying DDS pieces.

Each family manifest records the source PNG, processed PNG, final DDS, sprite name, geometry artifact, projected bbox, map revision, and hashes. The source PNG is a strict decode of the pre-repair runtime DDS because the earlier source folders were absent; the recorded geometry artifacts remain the authoritative map-derived province geometry and projection evidence.

The qualifying pass changes only the alpha of pixels whose RGB is (25, 56, 45) to the generic runtime outline alpha of 180. The unresolved pass changes only the RGB and alpha of the outer boundary pixels of connected components with at least 16 occupied pixels to (28, 31, 35, 220). Smaller disconnected islands keep their original outline pixels so their limited native geometry does not collapse into a dark dot.

The untouched fill and hatch palette remains qualifying fill (70, 148, 103) and pale keyline (155, 216, 165), plus unresolved fill (98, 101, 108) and hatch (66, 69, 75). Existing partial alpha values in those layers are preserved.

Per-family palette and alpha audit (exact post-conversion DDS values):

| Family | Qualifying fill | Qualifying outline | Qualifying keyline alpha | Unresolved fill / hatch | Unresolved outline | Existing grey edge alpha |
| --- | --- | --- | --- | --- | --- | --- |
| form_baltic_federation_category | (70, 148, 103), alpha 235/255 | (25, 56, 45), alpha 180 | (155, 216, 165), alpha 255 | fill (98, 101, 108) and hatch (66, 69, 75), alpha 190/235/255 | (28, 31, 35), alpha 220 | none |
| form_baltic_sea_empire_category | (70, 148, 103), alpha 235/255 | (25, 56, 45), alpha 180 | (155, 216, 165), alpha 255 | fill (98, 101, 108) and hatch (66, 69, 75), alpha 190/235/255 | (28, 31, 35), alpha 220 | none |
| form_north_sea_category | (70, 148, 103), alpha 235/255 | (25, 56, 45), alpha 180 | (155, 216, 165), alpha 179/180/199/216/233/255 | fill (98, 101, 108) and hatch (66, 69, 75), alpha 190/235/255 | (28, 31, 35), alpha 220 | (151, 154, 161), alpha 216/255 |
| form_scandinavia_category | (70, 148, 103), alpha 235/255 | (25, 56, 45), alpha 180 | (155, 216, 165), alpha 179/180/199/216/233/255 | fill (98, 101, 108) and hatch (66, 69, 75), alpha 190/235/255 | (28, 31, 35), alpha 220 | (151, 154, 161), alpha 216/255 |
| form_sweden_hungary_category | (70, 148, 103), alpha 235/255 | (25, 56, 45), alpha 180 | (155, 216, 165), alpha 255 | fill (98, 101, 108) and hatch (66, 69, 75), alpha 190/235/255 | (28, 31, 35), alpha 220 | none |

Interior fill and hatch RGB values remain unchanged.
The unresolved contour pass repaints 2,815 boundary pixels that previously used fill or hatch RGB as part of the bare coastline; those pixels become the shared near-black outline.
The qualifying keyline and existing grey edge alpha ranges above are inherited source values and were preserved.

The source and processed PNG directories are under each family directory’s source/ and processed/ children. Runtime DDS files remain under the existing gfx/interface/formables/state_puzzles/<family>/states/ paths. All sprite names and GUI anchors remain unchanged.

The ignored one-off processor is .tmp/formables_outline_repair.py. Commands used were python .tmp/formables_outline_repair.py process, python .tmp/formables_outline_repair.py convert form_baltic_federation_category form_baltic_sea_empire_category form_north_sea_category form_scandinavia_category form_sweden_hungary_category, python .tmp/formables_outline_repair.py verify, and the before/after sheet commands.

The external native-size and 4x nearest-neighbour sheets are C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/after/formables/before_contact_sheet.png, before_detail_sheet.png, after_contact_sheet.png, and after_detail_sheet.png. Each includes the unchanged form_commonwealth state 11 unresolved/qualifying pair for direct outline comparison.

Verification confirms exact source-to-processed pixel deltas limited to the described outline pixels, identical nonzero-alpha support, exact decoded DDS/processed PNG equality, matching native dimensions, and valid DDS headers for all 260 pieces. The form03 state 36 top fragments were checked against its exact province-derived row runs; they are genuine Frisian islets and remain unchanged per the review-plan fallback.

The shared .tools/formables/generate_formable_state_puzzle_runtime.mjs was left unchanged. Its pre-existing uncommitted two-line visibility-helper edits remain intact. No .gfx, GUI, or gameplay files changed.
