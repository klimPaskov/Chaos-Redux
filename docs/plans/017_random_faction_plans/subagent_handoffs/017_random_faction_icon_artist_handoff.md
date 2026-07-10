# Event 017 Random Faction Icon Artist Handoff

- Date: 2026-07-10
- Subagent: `chaosx_icon_artist`
- Mode: audit plus narrow patch
- Scope: decision/category icons, idea icons, achievement icon triplets, bloc-pressure seal animation, border-warning animation, asset documentation, and GFX handoff only

## Outcome

The existing Event 17 source art is genuine generated artwork and was preserved. The static package already contained the required category icon, all implementation-facing decision icons, all five idea icons, all six achievement triplets, and two eight-state animation source atlases. No duplicate replacement art was generated.

Two invalid animation derivatives were repaired:

1. Residual chroma alpha had prevented the old processor from trimming the 271x724 source cells, shrinking the visible 64x64 seal to roughly 20x23 pixels and the warning art to roughly 21x54 pixels.
2. The old sheet assembler pasted each RGBA frame with its own alpha as a second mask, so sheet-edge alpha did not match the processed frames.

Both sequences were re-keyed from the untouched real source frames with the official imagegen chroma helper, normalized with one shared scale and centered anchor per sequence, and reassembled with exact RGBA copies. Runtime and package DDS derivatives were regenerated from those corrected sheets and static fallbacks.

## References Consulted

- `C:/Users/klimp/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md`
- `docs/specs/017_random_faction_specs/prompts/017_random_faction_asset_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/017_random_faction_achievement_prompt.md`
- Required offline core wiki pages named in `AGENTS.md`
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/alerts.gfx`
- Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/menubar.gfx`
- Archived style review: `docs/assets/017_random_faction/contact_sheets/reference_contact_sheet.png`

The current tree no longer contains the skill reference directories named by the asset skill. They were deleted after the Event 17 package was produced. The preserved Event 17 reference contact sheet records the decision, idea, report, and achievement examples that were inspected while those folders existed.

## Asset Coverage

| Family | Count | Final dimensions | Sprite or filename coverage | Status |
|---|---:|---:|---|---|
| Decision category icon | 1 | 32x32 | `GFX_decision_category_random_faction_bloc_pressure` | wired |
| Decision icons | 11 | 32x32 each | all `GFX_decision_random_faction_*` ids in `interface/017_random_faction.gfx`, including stabilization, liaison, opposition, neutrality, border, observer, press, staff, radio, corridor, and commitment families | wired |
| Idea icons | 5 | 64x64 each | all five `GFX_idea_random_faction_*` sprites | wired |
| Achievement icons | 6 triplets / 18 DDS | 64x64 each | completed, `_grey`, and `_not_eligible` for all six Event 17 achievement ids | wired |
| Bloc-pressure seal | 8 frames plus static | 64x64 frames; 512x64 sheet | `GFX_random_faction_bloc_pressure_seal_static`, `GFX_random_faction_bloc_pressure_seal_animated` | wired |
| Border warning | 8 frames plus static | 64x64 frames; 512x64 sheet | `GFX_random_faction_border_warning_static`, `GFX_random_faction_border_warning_animated` | wired |

The full sprite-to-path mapping is in `docs/assets/017_random_faction/gfx_handoff.md`.

## Source Evidence

| Evidence | SHA-256 | Notes |
|---|---|---|
| `docs/assets/017_random_faction/contact_sheets/decision_source_contact_sheet.png` | `eecfd0f9c4765c88a3d755a551e11e6525a7691fabbd5c98058690d61098de93` | Shows the separate generated decision/category source PNGs on chroma key. |
| `docs/assets/017_random_faction/source/idea_random_faction_source_atlas.png` | `3dd89088848bb504730f8e6407a3c5d496c1b1e0439375a21e9742ac19fcc146` | Contains five distinct idea-specific source compositions. |
| `docs/assets/017_random_faction/source/achievement_017_random_faction_source_atlas.png` | `7f9ec3e9db2babfccef3b7fd3863325c9f98c4f28d8c59bdad0e3d6a6ea4ff5a` | Contains six distinct framed achievement compositions. |
| `docs/assets/017_random_faction/source/random_faction_bloc_pressure_seal_source_atlas.png` | `adccd23d1ece4a457484ffb98b439fa009c7dc832abcf344272658b75bf660d1` | Eight separately drawn cloth, cable, paper, wax-seal, light, and spark states. |
| `docs/assets/017_random_faction/source/random_faction_border_warning_source_atlas.png` | `66bd60128e963d09b8fcd89ab54e8ef363397e19af5afdd7b7c5dc8247a24713` | Eight separately drawn border-post, lantern, flag, wire, amber, and red-alert states. |
| `docs/assets/017_random_faction/contact_sheets/reference_contact_sheet.png` | `150f699045c790608caff543cc2ed74170bd6f245356b65bd53596ba33c2a6ac` | Preserved record of the required asset-type reference inspection. |

All 16 animation source-frame PNGs have unique SHA-256 hashes. Visual inspection of the source atlases and contact sheets confirms real painted content and frame-authored internal state changes rather than primitive drawings or transform-only animation.

## Files Changed by This Patch

### Repaired animation derivatives

- `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/processed_frames/`: eight corrected frames plus static fallback.
- `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/sheets/random_faction_bloc_pressure_seal_sheet.png`.
- `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/previews/`: corrected contact sheet and review GIF.
- `docs/assets/017_random_faction/animations/random_faction_border_warning/processed_frames/`: eight corrected frames plus static fallback.
- `docs/assets/017_random_faction/animations/random_faction_border_warning/sheets/random_faction_border_warning_sheet.png`.
- `docs/assets/017_random_faction/animations/random_faction_border_warning/previews/`: corrected contact sheet and review GIF.
- `docs/assets/017_random_faction/dds/`: both corrected static DDS copies and both corrected sheet DDS copies.
- `gfx/interface/animated/017_random_faction/`: both corrected static runtime DDS files and both corrected runtime sheet DDS files.

### Documentation

- `docs/assets/017_random_faction/manifest.md`.
- `docs/assets/017_random_faction/gfx_handoff.md`.
- Both animation `brief.md` files.
- Both animation `frame_plan.md` files.
- `docs/assets/017_random_faction/prompts/icon_and_animation_prompts.md`.
- This handoff.

No `.gfx`, `.gui`, gameplay, localisation, spreadsheet, or report-picture file was edited by this subagent.

## Task-Specific QA

- Decision/category processed icons: 12 files, all 32x32, all unique, all with real transparent unused pixels.
- Idea processed icons: 5 files, all 64x64, all unique, all with real transparent unused pixels.
- Achievement completed icons: 6 unique source artworks. Grey variants are grayscale. Not-eligible variants differ from grey through the standard red cross overlay and contain 694 red-dominant overlay pixels each.
- Bloc-pressure seal: 8 unique source frames; 8 processed 64x64 frames; visible alpha bounds roughly 49-50x55-56; 512x64 sheet; exact sheet-to-frame RGBA equality; static equals frame 000; no visible chroma fringe.
- Border warning: 8 unique source frames; 8 processed 64x64 frames; visible alpha bounds roughly 42-45x55-56; 512x64 sheet; exact sheet-to-frame RGBA equality; static equals frame 000; no visible chroma fringe.
- Each review GIF contains the eight real states plus one review-only repeated rest frame. GIFs are not runtime assets.
- Runtime and package DDS files are 32-bit uncompressed A8R8G8B8 with masks `00ff0000`, `0000ff00`, `000000ff`, and `ff000000` and retain real alpha.
- `interface/017_random_faction.gfx` registers both static fallbacks and both eight-frame animated sprites with `animation_rate_fps = 8`, `looping = yes`, and `play_on_show = yes`.
- `interface/chaosx_achievements.gfx` contains all 18 Event 17 achievement sprite definitions.

## Risks and Reproducibility Notes

- The exact historical imagegen tool-call text was not saved with the original source commit. `docs/assets/017_random_faction/prompts/icon_and_animation_prompts.md` provides a canonical reconstruction and explicitly does not present itself as a verbatim transcript.
- The skill reference folders and standard achievement overlay source were removed from the current tree after the final variants were produced. The completed runtime assets are unaffected, but the overlay/reference inputs must be restored before a full clean regeneration.
- `docs/assets/017_random_faction/_tooling/process_random_faction_assets.py` still assumes the deleted overlay path and uses the superseded animation matte logic. It must not be used to regenerate these derivatives without first being brought into line with the official chroma helper and restored reference inputs.

## Simplifications, Omissions, and Blockers

- Simplifications: none.
- Substitute or fallback art: none.
- Missing requested icon assets: none.
- Blockers to using the completed runtime assets: none.
