# Event 012 Gods of Africa spreadsheet handoff

Disposition: `implemented` for Event 012 catalog alignment and `superseded` for the original worker-stage export instruction. This is a dated reconciliation of the worker handoff, not a new workbook edit.

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

## Current reconciliation, 2026-09-25

Acceptance basis: the explicit Event 012 ownership and protection choices are recorded in `docs/specs/012_africa_specs/specs/012_africa_spec_part_3_focus_tree_architecture.md:979-989`. The workbook is player-facing catalog implementation evidence and does not grant design approval.

The parent read the workbook without editing it and confirmed that `Events!C13`, `D13`, `E13`, and `F13` match the current Event Details and Evolution I-III localisation. `Events!A71 = 70`, `B71` is blank, and `M71` is blank, so Event 070 remains available for another idea under the explicit Event 012 ownership goal.

The current `Events!F13` is the in-world `africa.evolution.3.body` text: “Africa's settlement has become a question every great power must answer. Foreign bases, sanctions, continent-wide mobilization, strange new actors, and rival projects are now part of the same struggle.” It is not technical validation prose or the earlier worker-stage bounded-offer sentence.

The parent ran `python .tools/export_event_catalog_csv.py` from the repository root and reported success with the export files unchanged. A read-only SHA-256 check of the present CSVs matched the reported results: Events `fe6e2437151c9971cae0b48573ddf2fb1657247dc45cb6c068e7644b65cfb165`, Clusters `276964d65cad082f678c7bbfff4d8e89d99930b1f3707b1d8dd07ba1e3755d8a`, and Scenarios `8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7`. The current Events CSV row for Event 070 has only ID `70` populated, and Event 012's detail and evolution columns mirror the cited localisation.

This curator did not open or edit the workbook, rerun the exporter, or change any CSV. Workbook cell equality is parent-provided read-only evidence, while current CSV hashes and the exported row were checked here. These catalog facts do not validate Event 012 gameplay or resolve focus-route, art-reuse, probability, MCP, or live-game limits.

## Original worker stage, retained as historical evidence

The original worker reported these two edited cells on Excel row 13 for Event ID 12, `Africa Is One`:

- `C13` (`Details`): replaced the entire cell with the exact event-details localization value below.
- `F13` (`Evo III`): replaced a stale protection-family sentence at that stage. The later parent correction replaced the worker-stage bounded-offer wording with the exact in-world Evolution III text recorded above.

The entire `C13` value now matches `chaosx.events_log.window.event_details.africa` in `localisation/english/012_african_union_l_english.yml`, replacing the longer mechanic and validation dossier and removing any earlier replacement character.

Final exact player-facing event detail quoted in `Events!C13`:

> An African government has started pulling the continent together with aid, guarantees, liberation deals, and a common Charter. Other countries can join, bargain, walk away, or build a rival camp. If the project keeps its promises, regional congresses and constitutional settlements can turn the idea into roads, armies, laws, and a fierce argument over who carries the cost.

The later parent catalog correction made `Events!D13`, `Events!E13`, and `Events!F13` match `africa.evolution.1.body`, `africa.evolution.2.body`, and `africa.evolution.3.body` in `localisation/english/012_africa_evolutions_l_english.yml`. The Events row's `C13` matches the in-game Event Details key. The accepted cost split and protection services remain in design and implementation documentation, not in the player-facing Evolution III field.

The earlier parent export succeeded with Events CSV SHA-256 `1537629a51c45a223c7eec197d01707546c403132937a6dc6c51a8936b8afbaf`, Clusters CSV SHA-256 `689fe07883da14abe2ceb7c29c151db50808cf97a366e60808281b16e37c76a2`, and Scenarios CSV SHA-256 `8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7`. These are dated export fingerprints and are superseded as current hashes by the values above.

Source: `localisation/english/012_african_union_l_english.yml`, key `chaosx.events_log.window.event_details.africa`. The `F13` replacement sentence was supplied in the parent instruction.

At the original worker stage, a pre-edit snapshot comparison found only `Events!C13` and `Events!F13` changed. The worker reported that every other cell value, style, number format, sheet, table, filter, validation, merge, row and column dimension, freeze pane, and formula value matched. Event 070 was still ID 70 with no event name. The worker did not run the exporter or make a commit at that stage.

The original worker's exporter request is closed by the later successful parent export. Catalog alignment does not close the wider Event 012 completion questions.
