# Event 015 final icon and authored-frame asset handoff

Subagent role: `chaosx_icon_artist`  
Date: `2026-07-14`  
Status: owned asset package complete; one explicit parent gameplay-integration blocker remains

## Scope and boundaries

This pass audited and completed the Event 015 focus-use surface, decision/category/mission icon family, current idea pictures, exact current achievement triplets, and the three named live Ledger animations. It did not edit gameplay, localisation, report/news/super-event images, flags, portraits, or any other event package.

Skills used:

- `chaos-redux-subagents`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- system `imagegen`

Required offline wiki, vanilla documentation, and vanilla sprite precedents were read before asset registration. The source-researcher's `Non-Icon Event-Art Provenance Audit` and route-super blocker section in `manifest.md` were preserved unchanged in substance.

## Final results

### Focus audit

- `122` current `icon = GFX_goal_utopia_*` usages
- `72` unique current focus sprite ids
- `72/72` base definitions and `72/72` `_shine` definitions
- `72/72` current textures present at `94x86`
- `109` physical family DDS files retained; `37` are not current tree references
- No focus runtime art required regeneration in this pass

### Decision, mission, and category icons

- Exact machine-readable handoff: `docs/assets/015_utopia_manifesto/decision_icon_mapping.csv`
- Current live-source coverage: `139` rows
  - `9` categories
  - `98` decisions
  - `32` missions
- The initial audit saw `128` entries; during the task the live decision file added:
  - `decision_utopia_prove_every_calling_chosen`
  - `mission_utopia_sustain_every_calling_chosen`
- Both additions are included in the final mapping, using `GFX_decision_utopia_second_trade`.
- Generated and registered `30` new `32x32` sprites:
  - Categories: `GFX_decision_category_utopia_district`, `GFX_decision_category_utopia_island`, `GFX_decision_category_utopia_necessary_ground`, `GFX_decision_category_utopia_stewardship`, `GFX_decision_category_utopia_defense`, `GFX_decision_category_utopia_governance`, `GFX_decision_category_utopia_formation`
  - Decision families: `GFX_decision_utopia_publish_accounts`, `GFX_decision_utopia_seasonal_reserve`, `GFX_decision_utopia_second_trade`, `GFX_decision_utopia_land_register`, `GFX_decision_utopia_district_survey`, `GFX_decision_utopia_district_foundation`, `GFX_decision_utopia_island_project`, `GFX_decision_utopia_common_harbor`, `GFX_decision_utopia_inland_terminal`, `GFX_decision_utopia_need_case`, `GFX_decision_utopia_purchase`, `GFX_decision_utopia_lease`, `GFX_decision_utopia_joint_administration`, `GFX_decision_utopia_ultimatum`, `GFX_decision_utopia_emergency_provision`, `GFX_decision_utopia_long_integration`, `GFX_decision_utopia_technical_mission`, `GFX_decision_utopia_reserve_compact`, `GFX_decision_utopia_citizen_watch`, `GFX_decision_utopia_engineer_companies`, `GFX_decision_utopia_auxiliary_contract`, `GFX_decision_utopia_constitutional_correction`, `GFX_decision_utopia_formation_proclamation`
- Every CSV row resolves to a registered, present `32x32` DDS, including the retained final Event 015 decision family.

Parent action required: apply the CSV's exact `icon_value` to each category/decision/mission. At handoff time `common/decisions/015_utopia_manifesto_decisions.txt` still has zero `icon =` assignments. This subagent intentionally did not edit gameplay.

### Current idea pictures

The current `50` idea entries use `12` unique picture tokens. The ten missing exact sprites were generated, exported at `64x64`, and registered:

- `GFX_idea_utopia_unmeasured_country`
- `GFX_idea_utopia_inherited_order`
- `GFX_idea_utopia_charter_of_households`
- `GFX_idea_utopia_common_table`
- `GFX_idea_utopia_perfect_measure`
- `GFX_idea_utopia_closed_island`
- `GFX_idea_utopia_practical_commonwealth`
- `GFX_idea_utopia_garden_district_network`
- `GFX_idea_utopia_auxiliary_dependency`
- `GFX_idea_utopia_stewardship_burden`

The already-current `GFX_idea_utopia_found_manifesto` and `GFX_idea_utopia_common_store_network` remain in use. All `12/12` exact picture tokens now resolve.

### Exact current achievements

Created final `64x64` base, `_grey`, and mandated-overlay `_not_eligible` triplets for these exact `14` ids (`42` runtime DDS files):

- `utopia_manifesto_no_place_but_home`
- `utopia_manifesto_need_not_greed`
- `utopia_manifesto_every_calling_chosen`
- `utopia_manifesto_two_year_table`
- `utopia_manifesto_archipelago_of_small_places`
- `utopia_manifesto_inland_island`
- `utopia_manifesto_gold_for_common_use`
- `utopia_manifesto_the_joke_understood`
- `utopia_manifesto_consent_of_the_governed`
- `utopia_manifesto_the_perfect_measure`
- `utopia_manifesto_closed_circle`
- `utopia_manifesto_no_foreign_hands`
- `utopia_manifesto_the_stores_remain`
- `utopia_manifesto_no_one_in_chains`

All `42` explicit aliases are registered as `GFX_achievement_<id>{,_grey,_not_eligible}` in `interface/015_utopia_manifesto.gfx`. The `_not_eligible` files are verified pixel-for-pixel against the grayscale image composited with `.agents/skills/chaos-redux-event-assets/assets/achievements/overlay.png`.

The older `36` `gfx/achievements/015_utopia_*.dds` files were not removed: `docs/plans/015_utopia_manifesto_plans/repo_explorer_handoff.md` still references them, so the parent's deletion condition was not met. They are documented as historical, not current.

### Required authored-frame animations

| Animated sprite | Static sprite | Frames | Frame / sheet | Playback | Static fallback |
| --- | --- | ---: | --- | --- | --- |
| `GFX_utopia_need_warning_animated` | `GFX_utopia_need_warning_static` | `8` | `64x64` / `512x64` | `5 fps`, loop, play on show | frame `004` |
| `GFX_utopia_reserve_fill_animated` | `GFX_utopia_reserve_fill_static` | `8` | `300x24` / `2400x24` | `4 fps`, loop, play on show | frame `004` |
| `GFX_utopia_formation_ready_seal_animated` | `GFX_utopia_formation_ready_seal_static` | `10` | `96x96` / `960x96` | `5 fps`, loop, play on show | frame `005` |

Every animation has:

- a written brief and frame plan
- a frozen imagegen source storyboard
- separately cropped source frames
- separately processed frames
- an exact horizontal frame sheet
- a static fallback
- a contact sheet
- a looping GIF preview
- final uncompressed BGRA DDS files
- `.gfx` registration matching the live `.gui` sprite id

The source and processed frame hashes are all unique within each sequence. These are genuine state changes—crack/grain/cord changes, physical reserve inventory changes, and separately authored household-relief/seal-light states—not one still moved, scaled, rotated, blurred, filtered, or recolored. The formation flare uses the shared sequence crop/scale so the seal does not shrink at the peak frame.

## Source and review artifacts

- Prompt/provenance record: `docs/assets/015_utopia_manifesto/prompts/final_icon_frame_generation.md`
- Frozen icon atlases: `docs/assets/015_utopia_manifesto/source_png/final_icons/`
- Final processed icons and contacts: `docs/assets/015_utopia_manifesto/processed_png/final_icons/`
- Final icon DDS staging: `docs/assets/015_utopia_manifesto/dds/final_icons/`
- Animation packages: `docs/assets/015_utopia_manifesto/animations/utopia_need_warning/`, `utopia_reserve_fill/`, and `utopia_formation_ready_seal/`
- Decision/category/mission mapping: `docs/assets/015_utopia_manifesto/decision_icon_mapping.csv`
- Machine audit record: `docs/assets/015_utopia_manifesto/final_icon_frame_audit.json`
- Updated owned documentation:
  - `docs/assets/015_utopia_manifesto/manifest.md`
  - `docs/assets/015_utopia_manifesto/gfx_handoff.md`
  - `docs/assets/015_utopia_manifesto/icon_animation_handoff.md`

Review contacts inspected after final processing:

- `processed_png/final_icons/utopia_final_decision_category_contact.png`
- `processed_png/final_icons/utopia_final_idea_contact.png`
- `processed_png/final_icons/utopia_final_achievement_contact.png`
- `processed_png/final_icons/utopia_final_achievement_triplets_contact.png`
- `animations/utopia_need_warning/previews/utopia_need_warning_contact.png`
- `animations/utopia_reserve_fill/previews/utopia_reserve_fill_contact.png`
- `animations/utopia_formation_ready_seal/previews/utopia_formation_ready_seal_contact.png`

## Runtime files and registry changes

- New decision/category DDS files: `gfx/interface/decisions/015_utopia_manifesto/<30 exact stems>.dds`
- New current idea DDS files: `gfx/interface/ideas/015_utopia_manifesto/<10 exact stems>.dds`
- New live animation DDS files: `gfx/interface/015_utopia_manifesto/utopia_{need_warning,reserve_fill,formation_ready_seal}_{static,sheet}.dds`
- New exact achievement triplets: `gfx/achievements/utopia_manifesto_*.dds`
- Registry: `interface/015_utopia_manifesto.gfx`
  - added `10` current idea definitions
  - added `30` decision/category definitions
  - added `42` exact achievement aliases
  - added `3` static and `3` animated live-GUI definitions
  - corrected all stale `gfx/interface/utopia_manifesto/` texture paths to `gfx/interface/015_utopia_manifesto/`
  - added `play_on_show`, zero loop pause, and transparent hit behavior to the live Ledger seal and three required animations

No report/news/super-event picture, flag, portrait, gameplay, localisation, or other-event file was changed by this asset pass.

## Validation evidence

Commands:

```text
python docs/assets/015_utopia_manifesto/_tooling/generate_decision_icon_mapping.py
python docs/assets/015_utopia_manifesto/_tooling/audit_final_icon_frame_package.py
```

Final audit result: `pass`.

Task-specific checks covered:

- current focus usage/base/shine/file/dimension closure
- current idea token/definition/file/dimension closure
- exact live decision/category/mission mapping drift and file closure
- exact current achievement ids, all triplets, aliases, DDS format, staging parity, and mandated overlay
- distinct source/processed animation frames, sheet-frame byte parity, static-fallback frame parity, GIF count, DDS dimensions/format, and `.gfx` metadata
- all six live Ledger GUI references resolving to present textures
- no duplicate Event 015 sprite names and no stale old GUI texture root in `interface/015_utopia_manifesto.gfx`

## Simplifications, omissions, and blockers

- No simplification or fallback was used inside the owned icon/frame package.
- Blocker: gameplay has zero decision/category/mission `icon =` assignments. The parent must apply `decision_icon_mapping.csv`; until then the final sprite package exists but is not selected by those gameplay entries.
- Retained historical files: `36` legacy achievement DDS files and `37` surplus focus-family DDS files were left intact to preserve referenced/user work. They are explicitly excluded from current-coverage claims.
- Non-owned blocker preserved from the source-research audit: five route-specific super-event image sources/DDS files remain missing. This pass neither created nor altered them.
