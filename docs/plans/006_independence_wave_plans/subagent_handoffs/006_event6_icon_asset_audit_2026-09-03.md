# Event 006 icon asset audit — 2026-09-03

## Scope and outcome

This audit covers matrix rows ASSET-007 through ASSET-038, ASSET-047, and ASSET-049, plus the accepted IW-043, IW-058, IW-093, IW-098, FORM-05, and related Event-006 icon packages.

The runtime families decode at their native consumer sizes, registered texture paths resolve, and no clipping or visible matte remains in the inspected final DDS files.

Two concrete one-pixel magenta/alpha spill defects were repaired in existing processed assets and reconverted with the official DDS converter.

No gameplay, GUI, category definition, or GFX registration file was changed, and no art was generated or substituted.

## Inventory counts

| Family | Matrix / accepted target | Final runtime inventory | Native result |
| --- | ---: | ---: | --- |
| National focus | 13 matrix rows, ASSET-007–019 | 121 DDS | All strict 94x86 BGRA; every focus base has a paired shine registration and no orphan/missing texture |
| Ideas / national spirits | 7 matrix rows, ASSET-020–026, plus ASSET-049 | 43 DDS | All strict 64x64 BGRA; no orphan/missing texture among registered files |
| Decisions | 12 matrix rows, ASSET-027–038 | 69 DDS in the Event-006 decision tree | 65 strict 32x32 decision icons plus four intentional 52x40 compact category icons |
| Shared compact categories | Five Event-006 consumers in `visual_consistency_repair/categories` | 5 of the six files in that folder | Strict 52x40 BGRA; the sixth, `death_survey`, is an Event-010 consumer and was left untouched |
| Category pictures | Four Event-006 package consumers in `visual_consistency_repair/pictures` | 4 DDS | Strict 114x101 opaque BGRA, matching the separate category-picture family |
| Achievements | ASSET-047, 16 achievement IDs with three states | 48 DDS | All strict 64x64 BGRA; all 16 completed/grey/not-eligible triplets are present |
| Missions | ASSET-038 | No separate mission family | `decision_independence_wave_integration_missions` is correctly a 32x32 decision sprite; no distinct mission art was invented |

The matrix focus names are `founding_administration`, `constitutional_state`, `popular_councils`, `traditional_restoration`, `military_emergency`, `patron_client`, `recognition_diplomacy`, `army_integration`, `infrastructure_authority`, `former_host_settlement`, `league_congress`, `regional_formable`, and `high_chaos_sovereignty`.

The matrix idea names are `improvised_government`, `unrecognized_state`, `fragmented_command`, `unsettled_borders`, `patron_pressure`, `league_membership`, and `founding_identity`; ASSET-049 is `post_release_instability`.

The matrix decision names are `recognition_actions`, `government_actions`, `army_integration_actions`, `depot_border_actions`, `former_host_negotiations`, `patron_aid`, `patron_balancing`, `network_aid`, `league_votes`, `border_arbitration`, `formable_proclamation`, and `integration_missions`.

## Consumer to sprite to definition to DDS

| Consumer definitions | Sprite token | Registration / runtime path |
| --- | --- | --- |
| `common/national_focus/006_independence_wave_focus.txt` and accepted package focus files | `GFX_goal_independence_wave_<stem>` | `interface/006_independence_wave.gfx`, `interface/006_independence_wave_iw093_iw098_focus.gfx`, or `interface/006_independence_wave_small_assets.gfx` -> `gfx/interface/goals/006_independence_wave/**/<stem>.dds`; 121 base paths and 121 shine paths resolve |
| `common/ideas/006_independence_wave_ideas_registry.txt` and accepted package idea files | `GFX_idea_independence_wave_<stem>` | `interface/006_independence_wave.gfx` or `interface/006_independence_wave_small_assets.gfx` -> `gfx/interface/ideas/006_independence_wave/**/<stem>.dds`; 43 registered paths resolve |
| `common/decisions/006_independence_wave_*.txt` and accepted package decision files | `GFX_decision_independence_wave_<stem>` | `interface/006_independence_wave.gfx` or `interface/006_independence_wave_small_assets.gfx` -> `gfx/interface/decisions/006_independence_wave/**/<stem>.dds`; 69 registered paths resolve |
| `common/decisions/categories/006_independence_wave_categories.txt` | `GFX_decision_category_independence_wave_{integration,government,diplomacy,network,borders}` | `interface/visual_consistency_repair.gfx` -> `gfx/interface/decisions/visual_consistency_repair/categories/*.dds`; five Event-006 consumers resolve |
| IW-043, IW-058, IW-093, and IW-098 category definitions in `common/decisions/categories/006_independence_wave_categories.txt` | `GFX_decision_category_independence_wave_iw043_middle_volga_congress`, `...iw058_council_of_communities`, `...iw093_asante_compact_category`, `...iw098_sokoto_compact_category` | `interface/006_independence_wave_small_assets.gfx` -> `gfx/interface/decisions/006_independence_wave/{volga_assyria,iw093_iw098}/*.dds`; all four 52x40 paths resolve |
| The same four package category definitions | `GFX_decision_cat_picture_independence_wave_{iw043_middle_volga_congress,iw058_council_of_communities,iw093_asante_compact,iw098_sokoto_compact}` | `interface/visual_consistency_repair.gfx` -> `gfx/interface/decisions/visual_consistency_repair/pictures/*.dds`; all four 114x101 paths resolve |
| `common/achievements/chaos_redux_achievements.txt` | Exact achievement ID filename, with `_grey` and `_not_eligible` states | No GFX sprite registration; direct `gfx/achievements/<achievement_id>{,_grey,_not_eligible}.dds`; all 16 triplets resolve |

The path scan found 242 focus registrations for 121 unique DDS files, 43 idea registrations, 69 Event-006 decision-folder registrations, 42 category registrations in the shared category folder, and 11 shared category-picture registrations, with zero missing texture paths.

## Category path recommendation

Keep the six compact category DDS files under `gfx/interface/decisions/visual_consistency_repair/categories/` and the four category-picture DDS files under `gfx/interface/decisions/visual_consistency_repair/pictures/`.

The exact registrations are lines 12–17 and 62–65 of `interface/visual_consistency_repair.gfx`, and the Event-006 category consumers use those exact sprite IDs from `common/decisions/categories/006_independence_wave_categories.txt`.

Moving only the files would immediately invalidate the registered texture paths; moving files and rewriting the shared registry would add unnecessary path churn without correcting a runtime defect.

The compact files are 52x40 and the pictures are 114x101, which are separate inspected vanilla category families and must not be moved into or resized as the 32x32 decision family.

Five of the six compact files are Event-006 consumers; `decision_category_independence_wave_death_survey.dds` is consumed by `common/decisions/categories/010_death_categories.txt` and is an out-of-scope compatibility sibling.

The four package-specific compact category files already in `gfx/interface/decisions/006_independence_wave/{iw093_iw098,volga_assyria}/` are correctly kept with their owning Event-006 package registrations.

## Source and canonical reference evidence

The matrix and accepted central manifest are `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv` and `docs/assets/006_independence_wave/{manifest.md,gfx_handoff.md}`.

The accepted source masters and processed previews are under `docs/assets/006_independence_wave/source_png/` and `docs/assets/006_independence_wave/processed_png/`, with accepted package archives for IW-043/IW-058, IW-093/IW-098, and FORM-05.

The matching canonical vanilla contact sheets and representative native references were inspected from the single approved root `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference` under `icons/national_focus`, `icons/ideas`, `icons/decisions`, `icons/missions`, `icons/decision_categories`, and `icons/achievements`.

The canonical focus family is transparent, centred, and ornate; the idea family is compact and transparent; decisions are simple 32x32 silhouettes; mission references are small state-dot treatments; compact categories are approximately 52x40; category pictures are approximately 114x101; achievement references are 64x64 framed triplets.

The Event-006 contact sheets under `docs/assets/006_independence_wave/contact_sheets/` and the decoded final DDS contact sheet were inspected as review aids, followed by native-size representative inspection.

The accepted achievement template hashes remain unchanged: completed `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`, grey `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`, and overlay `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD`.

## Concrete repair

The untouched source masters remain preserved; the repairs removed one clearly isolated `(255,0,255,1)` pixel from each existing processed RGBA preview and set it to `(0,0,0,0)`, then reconverted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` at the existing native dimensions.

Changed processed preview: `docs/assets/006_independence_wave/iw093_iw098_icons_2026_07_18/processed/focus/independence_wave_iw098_sultanic_settlement.png`.

Changed runtime DDS: `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_sultanic_settlement.dds`.

Changed processed preview: `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/processed_png/decisions/decision_independence_wave_form05_capital.png`.

Changed runtime DDS: `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_capital.dds`.

Updated package evidence for the repaired outputs: `docs/assets/006_independence_wave/iw093_iw098_icons_2026_07_18/metadata/hashes.sha256`, `docs/assets/006_independence_wave/iw093_iw098_icons_2026_07_18/metadata/validation.json`, `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/hashes.sha256`, and `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/notes/validation.json`.

Post-repair runtime hashes are `C6C0021015C718D5F26651E51D219357CD99834A7FF9AC05D95BE20B62FE64D2` for the IW-098 focus DDS and `FEC0EDCF98EB74571DE2D527429F2C8FFECBBF796721B929ED85A4864F01D8A0` for the FORM-05 decision DDS.

## Visual and technical status

Every inspected final DDS uses the expected strict one-level BGRA layout, with exact dimensions and no hidden RGB in fully transparent pixels.

The post-repair scans found no visible exact magenta pixels and no hidden RGB under alpha zero in the Event-006 focus, idea, decision, shared category, or category-picture folders.

Native-size inspection found no clipping, edge bleed, opaque square on alpha-backed families, or unreadable crop in the inspected Event-006 contact sheets and representative finals.

The category-picture family is intentionally opaque, matching its inspected consumer and vanilla family; the achievement root triplets are intentionally template-composited and opaque or near-opaque rather than alpha-backed icon subjects.

The official `process_achievement_icons.py --audit` passed all 15 central triplets and the accepted cross-package `chaosx_006_assyria_survives` triplet, including exact template/overlay preservation and source/output checks.

## Blockers, orphans, and needs-user-review

Two implicit idea consumers have no registered sprite or DDS: `picture = independence_wave_recognition_diplomacy` at lines 811, 932, 1212, 3257, 4141, and 4302, and `picture = independence_wave_recognition_campaign` at lines 1403, 1413, 1423, 1531, and 1553 of `common/ideas/006_independence_wave_ideas_registry.txt`.

These imply `GFX_idea_independence_wave_recognition_diplomacy` and `GFX_idea_independence_wave_recognition_campaign`, but neither is in the accepted matrix or manifests; no existing focus or idea sprite is a source-correct substitute, so they remain fail-closed and need an owner-approved asset/registration decision.

Two Siberian decisions use the unregistered `GFX_decision_independence_wave_network_actions` at lines 2498 and 2758 of `common/decisions/006_independence_wave_siberian_decisions.txt`.

The accepted `GFX_decision_independence_wave_network_aid` asset is a different token and cannot be silently substituted; the missing network-actions asset remains fail-closed pending owner-approved source art and registration.

No orphan DDS was found in the inspected Event-006 icon folders, and no registered Event-006 texture path was missing.

The central `_tooling/icon_build_report.json` has 45 stale achievement runtime hashes against the current template-composited root DDS outputs; the official achievement audits and runtime decodes pass, but the report needs an owner-approved refresh if it is release evidence.

The accepted historical source workflow used a magenta chroma fallback before alpha processing; untouched source masters retain that provenance, while all inspected processed/runtime alpha-backed outputs pass the current visible-matte checks.

Unrelated pre-existing evidence drift in package metadata was not broadened or rewritten.

## Validation record

Validation included strict DDS header, dimensions, pitch, BGRA masks, length, alpha-range, visible-matte, and hidden-RGB scans across all counted runtime folders.

Validation included registration-to-texture resolution, consumer-to-sprite inventory, paired focus-shine coverage, and orphan scans across the Event-006 definitions and interface registries.

Validation included native-size visual inspection of every canonical family contact sheet, Event-006 contact sheets, representative final DDS files, and all achievement triplet states.

Validation included the official achievement processor audits, exact template and overlay hashes, and decode checks of both repaired DDS files at `(62,57)` and `(2,18)`.

No live Hearts of Iron IV launch was performed, as required for this audit boundary.

No staging or commit was performed; unrelated worktree changes were preserved.
