ï»¿# Shared Chaos Redux decision category picture repair report

Status: the single assigned finding is handed off with parent visual approval; the final in-game category consumer check remains pending.

Scope is limited to the `shared_chaosx_decision_category_pictures` findings in `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` and `gfx_issues.json`.

## `GFX_decision_cat_picture_space_race`

The source was replaced with a native ImageGen scene of a late-1930s A4/V-2 test rocket, matching the sepia period picture-card style of the 032 missiles picture and canonical decision category picture references. The parent reviewed the processed 114x101 image on 2026-10-06 and approved its rocket readability, worn thin frame, period treatment, and lack of labels.

| Field | Value |
|---|---|
| Status | Handed off; parent visual approval accepted, in-game category check pending |
| Sprite | `GFX_decision_cat_picture_space_race` |
| Target `.gfx` | `interface/chaosx_decision_category_pictures.gfx` |
| Runtime DDS | `gfx/interface/decisions/044_space_race/decision_cat_picture_space_race.dds` |
| Canvas and background | 114x101, opaque full-canvas category picture |
| Active consumer | `chaosx_space_race_decision_category` in `common/decisions/categories/044_space_race_categories.txt`; it is visible while the global flag `space_race` is set |

### Candidate lineage and prompts

The first generated candidate is retained at `docs/assets/gfx_fix_shared_chaosx_decision_category_pictures/source_generated/decision_cat_picture_space_race_candidate_v1.png` (SHA-256 `115c61b12275d49e6a091f54e7ae1b4078d692f66efc8be1aee0d2a10c3c7021`). It established the rocket, smoke, sepia tone, and picture frame but came out with a wider composition than the reference family.

Candidate 1 ImageGen prompt: "Use case: historical-scene. Asset type: Hearts of Iron IV decision category picture, opaque 114x101 full-canvas scene. Input image 1 (`032_missiles_program_category.png`) is a style and treatment reference only: period sepia documentary realism, print grain, restrained contrast, and a thin worn-paper border. Input image 2 (`decision_cat_picture_1936_election.png`) is a style reference only for the aged paper picture treatment; do not copy its people, wall, or scene. Primary request: a believable late-1930s A4/V-2 class test rocket standing on a fixed launch gantry at a remote test range, with a low launch structure, smoke beginning to billow around the base, and no identifiable people. Composition/framing: small clear rocket silhouette near center, launch gantry and smoke readable at native 114x101, thin paper edge around the whole picture, no important details clipped. Style/medium: sepia monochrome period press photograph with natural grain and the exact restrained picture-card feel of the references. Lighting/mood: overcast, serious engineering milestone. Constraints: full opaque canvas, no transparency; no Saturn V, no NASA or Apollo imagery, no Earth horizon, no modern rocket hardware, no flags, no insignia, no labels, no readable text, no logos, no watermarks, no fake interface."

Candidate 2 is the selected final source at `docs/assets/gfx_fix_shared_chaosx_decision_category_pictures/source_generated/decision_cat_picture_space_race_source.png` (SHA-256 `0e72b8f62eb0c964417b3f148f422af6e64371c25eaead92d2e126ceeaf16856`). It is a focused edit of candidate 1 to bring the subject and all four paper edges into a compact near-square card while preserving the same scene.

Candidate 2 edit prompt: "Use case: precise-object-edit. Asset type: opaque Hearts of Iron IV decision category picture for a 114x101 consumer. Input image 1 is the edit target: preserve the same A4/V-2 test rocket, gantry, smoke, forest line, sepia monochrome photography, grain, and aged paper picture-card treatment. Input image 2 is a style reference only for the target's compact 114x101 paper-card framing. Primary request: recompose the same documentary scene into a near-square 1.13:1 canvas so the entire thin worn-paper frame remains visible on all four sides; keep the rocket central and legible, retain the gantry and smoke, and bring the paper edge inward evenly to suit the compact composition. Constraints: change only the framing and crop; preserve the same subject and era; no added people, signs, logos, lettering, labels, UI, modern rocket parts, color, watermarks, or extra border; full opaque sepia image, no transparent corners."

### Processing and runtime evidence

Before-state DDS snapshot: `docs/assets/gfx_fix_shared_chaosx_decision_category_pictures/source_runtime/decision_cat_picture_space_race_before.dds` (SHA-256 `8fa6eb91e1b2570a7f8f2e45365204ab7c843de8db3ec61efcc4c056e1fc71d9`). Its decoded PNG is preserved at `docs/assets/gfx_fix_shared_chaosx_decision_category_pictures/source_runtime/decision_cat_picture_space_race_before.png` and shows the full-colour Saturn V launch image.

Processed PNG preview: `docs/assets/gfx_fix_shared_chaosx_decision_category_pictures/processed/decision_cat_picture_space_race.png` (114x101 RGBA, SHA-256 `12ac23811becb9548a6410ac2125e835cf0597eda5d3c574dc34d86eee90b3ec`). The selected 1330x1183 source was resized to the reference-family canvas without cropping its outer frame; the final remains fully opaque.

Final DDS: `gfx/interface/decisions/044_space_race/decision_cat_picture_space_race.dds` (114x101, SHA-256 `4d5246ff9a9e8ec6a1c346aa17d7a652fb6f5b902d899da6d4fe0c699fc3e969`). It decodes pixel-exactly to the processed PNG with alpha range 255-255.

The narrowed contact sheet was generated through the trailer `gfx_sheets.py` utility using only `interface/chaosx_decision_category_pictures.gfx` and this sprite. It is retained at `docs/assets/gfx_fix_shared_chaosx_decision_category_pictures/contact_sheets/space_race_contact_sheet/shared_chaosx_decision_category_pictures_1.jpg`.

### Asset manifest and handoff

| Sprite | Source PNG | Processed PNG | Final DDS | Source/background mode | Target `.gfx` | Use note |
|---|---|---|---|---|---|---|
| `GFX_decision_cat_picture_space_race` | `docs/assets/gfx_fix_shared_chaosx_decision_category_pictures/source_generated/decision_cat_picture_space_race_source.png` | `docs/assets/gfx_fix_shared_chaosx_decision_category_pictures/processed/decision_cat_picture_space_race.png` | `gfx/interface/decisions/044_space_race/decision_cat_picture_space_race.dds` | Native ImageGen; opaque full-canvas image | `interface/chaosx_decision_category_pictures.gfx` | Sepia A4/V-2 test-range scene with the paper-card frame; preserve the existing sprite name and texture path. |

No `.gfx`, gameplay, localization, GUI, or decision file was changed. The existing sprite definition already points at the final DDS path.

## Remaining live check

When `chaosx_space_race_decision_category` is visible with global flag `space_race` set, confirm that the image appears at its native category-picture crop with the rocket and complete paper border intact.
For an isolated art check, use a paused 1936 USA setup, run `event chaosx.nr44.2 USA`, accept its sole option, and open Decisions.
That option sets the required global flag; inspect the Space Race category picture for the complete sepia rocket scene and paper edge.
This fixture checks the picture consumer only and does not establish contender registration or gameplay progression.

