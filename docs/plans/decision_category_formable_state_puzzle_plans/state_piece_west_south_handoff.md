# West/South formable state-puzzle asset handoff

Status: complete asset package, pending parent runtime-generator review. This handoff covers only `form_gran_colombia`, `form_commonwealth`, `form_united_netherlands`, `form_mutapa`, `unite_maghreb`, `proclaim_greater_italy`, and `unite_latin_africa`. Nordic League assets are intentionally absent.

## Source-of-truth and MCP evidence

The required state sets were extracted from `common/decisions/formable_nation_decisions.txt` and the live wrappers in `common/scripted_triggers/chaosx_formable_state_puzzle_triggers.txt`. The installed-map MCP initialization succeeded against revision `45748dacfcc82afdb1ae1ab00387f278c960a9c27a2d3fb28ce322aa773b9d38` with map dimensions `5632x2048`, `1081` states, and valid province bitmap/state membership/network checks. The MCP map artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73b9ae4c5c1553dc31fedb4d56e3b1254d257f40841cd5ea0b80e37c0bc3b614/a21790a3b304d0f89c214db7e1f1c1bd55b86b391b5c922c2c2f905d23a1806a/map-inspect.45748dacfcc82afd.json`. The linked province row-run artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6e51082a5b2bc5dd358b40e15a64f358b6b40bf2b06426454bd1ca90c03b7cb/478a0fe36c8c7866749bb194fb0f530f1d6ba9d8c79924745b00607e7ee32ecc/map-province-geometry.45748dacfcc82afd.a615eeaee21de517.json`.

The state-scoped follow-up MCP calls exceeded the server's 180-second call limit. The full-map inspection reported unrelated pre-existing building-position and floating-harbor diagnostics, so its overall `validation.passed` was false even though the province bitmap, state membership, map networks, and canonical row-run geometry checks passed. No fallback map source was substituted: the package uses the same installed `provinces.bmp`, `definition.csv`, and state-history membership validated by that inspection, and records the revision plus local SHA-256 hashes in every manifest and geometry artifact.

## Required state sets and helper policy

| formable / category | required state ids | groups and counting rule |
| --- | --- | --- |
| `form_gran_colombia` / `form_gran_colombia_category` | `490,491,304,305,649,486,306,493,489,307,488` | shared `490,491,304`; Ecuador `305,649`; Colombia `486,306,493`; Venezuela `489,307,488`; all wrappers use `chaosx_formable_state_qualifies` (`is_controlled_by = ROOT`). |
| `form_commonwealth` / `form_commonwealth_category` | `11,189,86,87,88,90,98,10,97,92,91,89,93,94,95,96,784` | Lithuania `11,189`; Poland `86,87,88,90,98,10,97,92,91,89,93,94,95,96,784`; all wrappers use `is_controlled_by = ROOT`. |
| `form_united_netherlands` / `form_united_netherlands_category` | `8,7,35,36,6,34,977,980` | shared `8`; Netherlands `7,35,36`; Belgium `6,34,977,980`; all wrappers use `is_controlled_by = ROOT`. |
| `form_mutapa` / `form_mutapa_category` | `541,893,894,895,681,719,275,542,545,544,896,897,771,981` | one core territory group; all wrappers use `is_controlled_by = ROOT`. |
| `unite_maghreb` / `maghreb_formable_category` | `290,461,462,783,699,557,513,459,460,458,665,448,661,449,662,450,663,451` | one core territory group; all wrappers use `is_controlled_by = ROOT`. |
| `proclaim_greater_italy` / `greater_italy_category` | fixed `852,736,160,39,850,159,158,161,162,157,2,849,117,156,115,114` plus fixed alternate-policy states `1,846,735,163,103,853,116,182,164` | first 16 wrappers use `is_controlled_by = ROOT`; the nine `required_other_states` wrappers preserve the live subject policy: direct ITA control OR control by any subject of ITA. Assets contain only these 25 fixed state pieces; they do not invent or expand the alternate set. |
| `unite_latin_africa` / `latin_africa_category` | `295,888,889,890,718,538,768,769,796,540,891,892,772,539,297,773,660,774` | one core territory group; wrappers use `is_controlled_by = ROOT`. |

## Files and naming

Each formable has a manifest at `docs/formables/state_puzzles/<formable_id>/manifest.json`, a local geometry artifact at `docs/formables/state_puzzles/<formable_id>/<formable_id>_geometry_artifact.json`, source masks under `source/state_<state_id>_mask.png`, review masks under `masks/state_<state_id>_mask.png`, processed pairs under `processed/state_<state_id>_{unresolved,qualifying}.png`, projection previews (`projection_unresolved.png`, `projection_qualifying.png`, `<formable_id>_projection_440x180.png`, and `<formable_id>_projection_440x180_qualifying.png`), and a native-size `contact_sheet.png`.

Runtime DDS pairs are under `gfx/interface/formables/state_puzzles/<formable_id>/states/state_<state_id>_{unresolved,qualifying}.dds`. Every manifest entry carries `state_id`, `position`, legacy generator-compatible `canvas_position`, `sprites` plus `sprite_names`, and `runtime_dds` fields. Runtime art uses the generated sprite names `formable_state_puzzle_<formable_id>_state_<state_id>_{unresolved,qualifying}`; no `.gfx`, GUI, gameplay, localisation, or decision file was edited.

## Geometry and projection evidence

Geometry is derived deterministically from the installed 24-bit `provinces.bmp` and `definition.csv`: state-history province IDs are mapped to province pixels, the union of the required states is cropped, then one shared Lanczos projection is applied to the 440x180 canvas with six-pixel outer padding. Each state is tight-bounded from the projected mask, preserving neighbouring seams. The unresolved variant is grey with diagonal hatch and keyline; the qualifying variant is green with pale inner keyline and dark silhouette outline, so qualification is not colour-only. Each manifest stores source bbox, source size, scale, origin, scaled size, per-state tight bbox, projected mask size, mask pixel count, province IDs, history file, and source hashes.

## Validation

The package contains 111 state pieces and 222 final DDS files: Gran Colombia 11/22, Commonwealth 17/34, United Netherlands 8/16, Mutapa 14/28, Maghreb 18/36, Greater Italy 25/50, and Latin Africa 18/36. All manifest runtime paths exist. A local generator-compatibility check passed for every manifest against `.tools/generate_formable_state_puzzle_runtime.mjs` requirements (`schema`, `projection.canvas = [440,180]`, `state_policy.required_state_ids`, `canvas_position`, `sprite_names`, and both runtime DDS paths). DDS header/length/dimension audit passed for all 222 files with zero errors. Contact sheets were visually inspected for all seven packages; the projections assemble in geographic positions and the state silhouettes remain readable at native review scale.

No gameplay, GFX registry, GUI, localisation, decision, scripted trigger, or state-history files were changed. The helper `chaosx_formable_proclaim_greater_italy_state_*` subject-control semantics remain untouched and are recorded in the Greater Italy manifest. The temporary generation utility is `.tools/generate_state_puzzle_west_south.py`; the parent may retain or remove it after reviewing the reproducibility evidence.
