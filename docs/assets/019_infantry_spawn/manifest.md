# Event 019 Infantry Spawn Asset Manifest

Status: package complete for the accepted scope. The non-regional visual rows are retained and wired. The 91-row regional flag candidate is independently approved by `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md` (PASS, remediation gate cleared), and the final whole-event audit `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_completion_audit_2026_07_18.md` is PASS with P0/P1/P2 = 0. The machine validation JSON intentionally retains its literal processor candidate status, `candidate_requires_independent_visual_review`; that field is superseded for approval by the separate PASS handoff and was not edited. Parent workbook/catalog reconciliation and export are complete, Event 19 and SCN-013 now read `Fully Functional`, and `package_contents.md` verifies 33/33 current files. No closure gate remains. Exact identifiers and decision-to-icon reuse are recorded in `gfx_handoff.md`.

## References inspected

- Offline wiki: Graphical Asset Modding, Interface Modding, Scripted GUI Modding, Localisation, Portrait Modding, Achievement Modding, Country Creation, and the required core scripting pages.
- Vanilla interface precedents: `interface/alerts.gfx`, `interface/countryconstructionsview.gfx`, `interface/countryconstructionsview.gui`, and `interface/theatreselector.gfx`.
- Project reference folders: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/{decisions,ideas,national_focus,achievements}/`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/{normal,medium,small}/`, their contact sheets, and the Event 007, Event 010, and Event 018 interface-animation packages.
- Canonical flat-flag references: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/{normal,medium,small}/`, `assets/vanilla_reference/CATALOG.md`, and `assets/vanilla_reference/flags/contact_sheet.png`; the offline Country Creation flag section and installed vanilla cosmetic-tag effect/trigger documentation were also inspected.

## Achievement icons

All completed icons are separate `$imagegen` originals. Grey variants are true grayscale conversions. Not-eligible variants are the grey images composited with `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png`. Final files are 64 by 64 uncompressed 32-bit BGRA DDS and live directly under `gfx/achievements/`. The achievement loader resolves those filenames directly, and all 33 completed/grey/not-eligible textures also have explicit reusable sprite aliases in `interface/chaosx_achievements.gfx`.

| Achievement id | Prompt direction | Source PNG | Processed PNG triplet | Final DDS triplet | Status |
| --- | --- | --- | --- | --- | --- |
| `019_infantry_spawn_every_rifle_accounted_for` | sealed ledger, complete roster, stacked bolt-action rifles | `source_png/achievements/019_infantry_spawn_every_rifle_accounted_for_source.png` | `processed_png/achievements/019_infantry_spawn_every_rifle_accounted_for{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_every_rifle_accounted_for{,_grey,_not_eligible}.dds` | complete |
| `019_infantry_spawn_one_battalion_wonder` | lone battalion holding against an immense front | `source_png/achievements/019_infantry_spawn_one_battalion_wonder_source.png` | `processed_png/achievements/019_infantry_spawn_one_battalion_wonder{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_one_battalion_wonder{,_grey,_not_eligible}.dds` | complete |
| `019_infantry_spawn_the_army_has_voted` | ballot box crossed by command baton and military cap | `source_png/achievements/019_infantry_spawn_the_army_has_voted_source.png` | `processed_png/achievements/019_infantry_spawn_the_army_has_voted{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_the_army_has_voted{,_grey,_not_eligible}.dds` | complete |
| `019_infantry_spawn_order_from_noise` | scattered military symbols resolving into ordered columns | `source_png/achievements/019_infantry_spawn_order_from_noise_source.png` | `processed_png/achievements/019_infantry_spawn_order_from_noise{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_order_from_noise{,_grey,_not_eligible}.dds` | complete |
| `019_infantry_spawn_combined_arms_accident` | interlocked horse, track, bicycle wheel, gun, and helmet | `source_png/achievements/019_infantry_spawn_combined_arms_accident_source.png` | `processed_png/achievements/019_infantry_spawn_combined_arms_accident{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_combined_arms_accident{,_grey,_not_eligible}.dds` | complete |
| `019_infantry_spawn_no_room_on_the_train` | intact steam locomotive crowded by formation markers | `source_png/achievements/019_infantry_spawn_no_room_on_the_train_source.png` | `processed_png/achievements/019_infantry_spawn_no_room_on_the_train{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_no_room_on_the_train{,_grey,_not_eligible}.dds` | complete |
| `019_infantry_spawn_borrowed_future` | speculative advanced vehicle emerging from an old depot | `source_png/achievements/019_infantry_spawn_borrowed_future_source.png` | `processed_png/achievements/019_infantry_spawn_borrowed_future{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_borrowed_future{,_grey,_not_eligible}.dds` | complete |
| `019_infantry_spawn_three_false_apocalypses` | separately sealed zombie, ghost, and coal-golem silhouettes | `source_png/achievements/019_infantry_spawn_three_false_apocalypses_source.png` | `processed_png/achievements/019_infantry_spawn_three_false_apocalypses{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_three_false_apocalypses{,_grey,_not_eligible}.dds` | complete |
| `019_infantry_spawn_barracks_of_babel` | camel, bicycle, amphibious tank, and flamethrower column | `source_png/achievements/019_infantry_spawn_barracks_of_babel_source.png` | `processed_png/achievements/019_infantry_spawn_barracks_of_babel{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_barracks_of_babel{,_grey,_not_eligible}.dds` | complete |
| `019_infantry_spawn_quiet_demobilisation` | departing columns, stacked rifles, intact sealed ledger | `source_png/achievements/019_infantry_spawn_quiet_demobilisation_source.png` | `processed_png/achievements/019_infantry_spawn_quiet_demobilisation{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_quiet_demobilisation{,_grey,_not_eligible}.dds` | complete |
| `019_infantry_spawn_every_barracks_a_front` | fictional country outline filled by hostile front markers | `source_png/achievements/019_infantry_spawn_every_barracks_a_front_source.png` | `processed_png/achievements/019_infantry_spawn_every_barracks_a_front{,_grey,_not_eligible}.png` | `gfx/achievements/019_infantry_spawn_every_barracks_a_front{,_grey,_not_eligible}.dds` | complete |

Review sheets: `contact_sheets/event_019_achievement_completed_contact_sheet.png` and `contact_sheets/event_019_achievement_not_eligible_contact_sheet.png`.

## Completed visual package

- Eleven distinct fictional documentary report sources are processed to 210 by 176 PNG/DDS cards under `processed_png/report/` and `gfx/event_pictures/019_infantry_spawn/`.
- Twenty distinct regional claimant army/muster scenes, six derivative zombie, ghost, or golem host scenes, and one identity-neutral unassigned muster are retained as 27 separate built-in ImageGen originals, then processed to 156 by 210 PNG/DDS under the fixed technical `processed_png/portraits/` and `gfx/leaders/019_infantry_spawn/` paths. No retained scene contains an individual focal human/person; none is a fallback, reused source, or transformed substitute.
- The no-focal-person rule applies to these 27 fixed identity slots and every Event 19 UI, scenario, or authority display that reuses them. Report cards, focus icons, decision icons, and achievement illustrations are separate asset types governed by their own briefs; they do not stand in for a claimant, commander, council, or derivative identity.
- Three separate real-source-frame animation packages are processed with static fallbacks, horizontal PNG/DDS sheets, GIF review previews, and contact sheets under `animations/` and `gfx/interface/019_infantry_spawn/`.
- Forty-five distinct derivative-focus icons are processed to current vanilla-sized 100 by 88 transparent PNG/DDS under `processed_png/focuses/` and `gfx/interface/goals/019_infantry_spawn/`; every base sprite has a matching conventional `_shine` SpriteType using the same authored texture and `gfx/FX/buttonstate.lua`.
- Forty-seven distinct decision concepts are processed to 33 by 32 transparent PNG/DDS under `processed_png/decisions/` and `gfx/interface/decisions/019_infantry_spawn/`; missions reuse the matching action icon, while the request cooldown uses the dedicated clock marker. The prototype-preservation and prototype-cannibalization icons retain individual imagegen source masters in `source_png/decisions/`.
- Nine idea icons, three decision-category icons, and six muster-board markers are processed under `processed_png/ideas/`, `processed_png/ui/`, `gfx/interface/ideas/019_infantry_spawn/`, and `gfx/interface/019_infantry_spawn/`.
- One 1120 by 760 muster-board background is processed under `processed_png/gui/` and `gfx/interface/019_infantry_spawn/`; the current authored composition and runtime proof are retained in `gui_background_rebuild_2026_07/` with its source PNG, processed PNG, review sheet, manifest, and GFX handoff.
- Thirteen distinct original cosmetic flags remain as identity precedents. The current 13 by 7 regional candidate contains 91 independently generated full-flag raw sources, 91 deterministic 820 by 520 spot masters, and 91 native normal, medium, and small PNG/TGA ladders at 82 by 52, 41 by 26, and 10 by 7. Visual and runtime row review passes, and the independent remediation re-audit cleared the regional asset gate and authorized promotion to the parent-owned package workflow. See `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`. The machine JSON remains a literal `candidate_requires_independent_visual_review` processor-state record, not an approval verdict.

## Report-event mapping

| Sprite | Report art |
| --- | --- |
| `GFX_report_event_infantry_spawn` | manifestation |
| `GFX_report_event_infantry_spawn_evolution_i` | organised host |
| `GFX_report_event_infantry_spawn_evolution_ii` | seized arsenal |
| `GFX_report_event_infantry_spawn_evolution_iii` | claimant command |
| `GFX_report_event_infantry_spawn_evolution_iv` | anomalous registry |
| `GFX_report_event_infantry_spawn_{zombie,ghost,golem}_{release,defeat}` | derivative release and defeat cards |

## Fixed portrait-slot army/host package

- Claimants: `GFX_portrait_infantry_spawn_claimant_01` through `GFX_portrait_infantry_spawn_claimant_20`; each shows a different region-compatible army or muster rather than the claimant character.
- Commander-labelled derivative slots: `GFX_portrait_infantry_spawn_{zombie,ghost}_host_commander` and `GFX_portrait_infantry_spawn_golem_master_builder`; each shows one massed host with no focal individual.
- Council-labelled derivative slots: `GFX_portrait_infantry_spawn_{zombie,ghost}_host_council` and `GFX_portrait_infantry_spawn_golem_pattern_council`; each shows exactly three massed formations or cohorts rather than councillor figures.
- Identity-neutral muster: `GFX_portrait_infantry_spawn_unassigned_muster` shows an anonymous country-neutral massed army. It is used before a valid claimant/family/scenario identity resolves and as the deliberate army-only identity for all four Event Log evolution-detail rows. It never selects, substitutes, or fabricates a claimant or family identity.
- Gameplay identity metadata preserves the twenty male claimant profiles and exact runtime region gates. Profiles 04 and 12 remain Asia/Australasia diaspora-compatible; profile 20 remains Australia-only. There is no global or mismatched-region claimant fallback.
- The derivative families remain categorical at runtime size: massed undead ranks for zombies, vaporous spectral formations for ghosts, and collective coal/basalt/mineral hosts for golems. The Ghost Host Council remains a genderless institutional identity expressed as an empty-centered spectral ring plus exactly two recessed crescent formations.
- Exact 27-row source/processed/DDS/sprite/identity/hash crosswalk: `notes/claimant_portrait_asset_crosswalk_2026_07_16.md`.
- Linked 27-row retained reproduction specifications and built-in ImageGen provenance: `prompts/claimant_portrait_reproduction_specs_2026_07_16.md`.

## Real-frame animation packages

| Package | Frozen animation-source atlas | Retained cells | Final frame size | Sheet | Runtime playback |
| --- | --- | ---: | ---: | ---: | ---: |
| `muster_seal_pulse` | `animations/muster_seal_pulse/source_atlas/muster_seal_pulse_animation_source_atlas.png` | 8 (`4x2`) | 64 by 64 | 512 by 64 | 8 fps |
| `critical_command_border` | `animations/critical_command_border/source_atlas/critical_command_border_animation_source_atlas.png` | 8 (`4x2`) | 156 by 210 | 1248 by 210 | 6 fps |
| `anomalous_registry_emblem` | `animations/anomalous_registry_emblem/source_atlas/anomalous_registry_emblem_animation_source_atlas.png` | 10 (`5x2`) | 64 by 64 | 640 by 64 | 5 fps |

The three atlases were produced with built-in ImageGen as explicit animation-source atlases, using each package's former frame `000` as a strict object-identity reference. Every row-major atlas cell is retained as source art. Local processing only slices the frozen atlas, removes the flat green background and disconnected atlas-edge debris, applies one shared sequence scale and center anchor, exports exact-size frames, and assembles the sheet, static fallback, GIF, contact sheet, and BGRA DDS. It does not synthesize the internal motion. The complete per-frame source hashes and authored state descriptions are recorded in each package's `frame_plan.md`.

| Package | Atlas size | Atlas SHA-256 | Anchor deviation | Minimum silhouette IoU | Chroma residue |
| --- | ---: | --- | ---: | ---: | ---: |
| `muster_seal_pulse` | 1774 by 887 | `58456dfdbf1bf3e7a877bee6e178547f3bda5dffb3f7e856a188c5b165bccad1` | 0.455 px | 0.8838 | 0 pixels |
| `critical_command_border` | 1470 by 1070 | `4bbf16da40a7dddae4e16c8b9059609a8e415b6726b25946626c7f3d68d45246` | 0.438 px | 0.9441 | 0 pixels |
| `anomalous_registry_emblem` | 1983 by 793 | `f634899a432dd8317412de13f8ae31cbf2e47c5d97f2c8e563ced6e1a8f4cd85` | 0.495 px | 0.9278 | 0 pixels |

Original-detail atlas and processed-contact inspection confirms a single stable object identity per loop: the seal's mount/rivets/wax disk, the command border's rails/corners/open aperture, and the registry plaque's perimeter/clasps/stone doors remain invariant while their internal cracks, relief, etched paths, and containment hardware change. All 26 source frames and all 26 processed frames have package-local unique hashes. Frame `000` is the static fallback and the first frame of each horizontal sheet.

| Package | Sheet PNG SHA-256 | Static PNG SHA-256 | Sheet DDS SHA-256 | Static DDS SHA-256 |
| --- | --- | --- | --- | --- |
| `muster_seal_pulse` | `d10068c5a398bbdbafb255b82cff1de974bb5fc1b8217cc7a1464c9a731b123f` | `11c38b63d2b4bec6d008f0f5ca7454044ba0035b3592a0e16cae246e6aa70b70` | `33a855e5298504610de70ba88ebdb06837ff5c7093b1c9f763b7bb710f4191bc` | `5966eed860427667d9c868b63662cb153cfe1ef2ce632f85dcc116a261d66804` |
| `critical_command_border` | `0cbdd32049550f69cf06cb6c1c7525da3130df86234f46a48bbe07c2bb2bb5b4` | `a7b776bc7e19483560423360ef80d35cb9d3566069e203c1659267d8d114934d` | `431928916098dd0660af561f3d7071f21cdd77741d2716dc4e2c4101a8d912f9` | `cce2ca528ed6b12c21677c54757745b1009fd26bc37f32b007cbcada86644aba` |
| `anomalous_registry_emblem` | `c2d0357bffa98afc538159477014a42e5f7216a047416d0235f2f34781cc96f1` | `f025e94c6944e51805d318fb6132c880e4110e75694721d21a8d3fa57597318b` | `a5bddd5a0ab7ce706e44ebc231769d8c6ccff3cd9ea16a57bf98f1f2e9006343` | `fe0438972ecb9477f9fb4f579536c2c54027990c0826c74b35788ac22a1c88c4` |

The source-frame and final PNG hashes record the retained Python 3.13 and Pillow 12.2 processor output. A cross-encoder audit reproduced the predecessor byte hashes under Pillow 11.1 and the current hashes under Pillow 12.2 from identical decoded pixels. The nine changed PNG byte hashes therefore reflect encoding only: dimensions, alpha, authored frame content, frame distinctness, and runtime DDS pixels and hashes are unchanged.

All six DDS files match their PNG pixels exactly and use the required uncompressed 32-bit BGRA masks. GIF review timing is quantized to 120 ms at 8 fps and 160 ms at 6 fps; the authoritative runtime speeds remain the exact `8`, `6`, and `5` fps values in `interface/019_infantry_spawn.gfx`.

## Cosmetic flag identities

| Family | Cosmetic tags | Design distinction |
| --- | --- | --- |
| Claimant breakaway | `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY` | disputed muster ledger, unequal command batons, mobilised canton |
| Zombie | `INFANTRY_SPAWN_ZOMBIE_BASE`, `_CLAIMANT`, `_COLLECTIVE`, `_SPECIES` | tally host, crowned host, linked dead columns, devouring species spiral |
| Ghost | `INFANTRY_SPAWN_GHOST_BASE`, `_CLAIMANT`, `_COLLECTIVE`, `_SPECIES` | anchored procession, pale crown, chorus of masks, moon-door dominion |
| Golem | `INFANTRY_SPAWN_GOLEM_BASE`, `_CLAIMANT`, `_COLLECTIVE`, `_SPECIES` | bound rune, master-builder march, distributed pattern, living-stone realm |

The thirteen source identities use different compositions and silhouettes rather than recolours. Name, definite-name, adjective, and ideology-alias keys are consolidated in the existing UTF-8-BOM Event 19 localisation file, `localisation/english/019_infrantry_spawn_l_english.yml`; the asset pass does not duplicate them. HOI4 resolves cosmetic flag filenames and localisation directly from the `set_cosmetic_tag` token; no separate cosmetic-tag code registry is required.

### Regional flag matrix

Every matrix filename follows `INFANTRY_SPAWN_<IDENTITY>_<REGION>`. The thirteen identity stems are the claimant breakaway plus the four zombie, four ghost, and four golem rows listed above. The seven region tokens below retain the 7/16 motif names as archival descriptive labels only. They are not current source-generation instructions or claims that the old motif/composite pipeline remains active:

| Region token | ImageGen-authored secondary motif |
| --- | --- |
| `EUROPE` | split heraldic chevron |
| `MIDDLE_EAST` | eight-point geometric knot |
| `AFRICA` | stepped sun and spearhead |
| `ASIA` | mountain-cloud gate |
| `AUSTRALIA` | navigation star and wave |
| `NORTH_AMERICA` | broken star and rail chevron |
| `SOUTH_AMERICA` | condor-step and maize diamond |

The current source/runtime chain is the only active regional chain:

1. 91 unmodified built-in ImageGen full-flag raws under `source_png/flags/regional_full_flag_raw/`.
2. 91 deterministic 820 by 520 RGB spot masters under `processed_png/flags/regional_spot_colour_masters/`.
3. 273 native PNGs under `processed_png/flags/`, at 82 by 52, 41 by 26, and 10 by 7.
4. 273 bottom-left-origin runtime TGAs under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

The exact processor and arguments are recorded in `_tooling/process_event_019_regional_flags.py` and `regional_flag_validation_2026_07_18.json`. The seven retained GHOST_BASE prompt records were recovered exactly from the original archive and independently matched by the parent. They remain in the existing ghost-owned prompt and provenance records.

`source_png/flags/regional_variants/`, the seven-motif composite notes, the 2026-07-16 validation/checksum pair, and the 7/16 motif/composite contact sheets remain archival superseded evidence. They are not current processor inputs, runtime sources, or approval records.

## GUI and sprite definitions

- `interface/019_infantry_spawn.gfx` is the sole Event 019 gameplay, report, identity-scene, and Muster Board sprite-definition file. It does not define gameplay or unit registries. The shared `interface/chaosx_achievements.gfx` separately registers the eleven achievement texture triplets.
- `interface/019_infantry_spawn_muster_board.gui` consumes the 1120 by 760 background, all three animated sprites, all three static fallbacks, and the selected claimant army/muster scene through its unchanged portrait-slot widget.
- `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt` already owns animated/static visibility and dynamic portrait-slot selection; this asset tranche does not alter that behavior.
- `common/scripted_localisation/019_infantry_spawn_scenario_scripted_localisation.txt` and `common/scripted_effects/019_infantry_spawn_scenario_effects.txt` reuse the registered army/muster and massed-host slots for SCN-013 government identities. No direct-scenario authority image contains a focal person.
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt` binds the evolution-detail image to `GetEventsLogSelectedEvolutionPortrait`; the Event 019 branches in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` select the identity-neutral army muster for stages I through IV instead of the shared unknown-person image.
- Category and state-marker sprite identifiers are documented in `gfx_handoff.md`.

## Processing and review evidence

- Reproducible processor and validator: `_tooling/process_event_019_generated_art.py`.
- Regional flag processor and validator: `_tooling/process_event_019_regional_flags.py`.
- Generated icon and flag prompt record: `prompts/generated_icon_and_flag_prompts.md`; animation prompts and state plans remain inside each animation package.
- Complete claimant, derivative, and technical-default army/host scene prompt/provenance record: `prompts/claimant_portrait_reproduction_specs_2026_07_16.md`; exact 27-row source-to-runtime crosswalk: `notes/claimant_portrait_asset_crosswalk_2026_07_16.md`.
- Archival superseded regional motif prompt record: `prompts/regional_flag_motif_prompts_2026_07_16.md`.
- Focus review: `contact_sheets/event_019_focus_icon_contact_sheet.png`; runtime wiring contains 45 base focus sprites and 45 matching shine sprites.
- Decision review: `contact_sheets/event_019_decision_icon_contact_sheet.png`.
- Idea/UI review: `contact_sheets/event_019_idea_icon_contact_sheet.png` and `contact_sheets/event_019_ui_icon_contact_sheet.png`.
- Flag review: `contact_sheets/event_019_flag_contact_sheet.png`.
- Archival superseded regional motif-source review: `contact_sheets/event_019_regional_motif_source_contact_sheet.png`.
- Current 7/18 regional three-size matrix review: `contact_sheets/event_019_regional_flag_contact_sheet.png`; current 7/18 dedicated 10 by 7 review: `contact_sheets/event_019_regional_flag_small_readability_contact_sheet.png`.
- GUI review: `contact_sheets/event_019_gui_background_contact_sheet.png` and `gui_background_rebuild_2026_07/review/muster_board_background_contact_sheet.png`.
- Army/host scene review: `contact_sheets/event_019_claimant_source_contact_sheet.png`, `contact_sheets/event_019_claimant_processed_contact_sheet.png`, `contact_sheets/event_019_derivative_portrait_source_contact_sheet.png`, `contact_sheets/event_019_derivative_portrait_processed_contact_sheet.png`, `contact_sheets/event_019_unassigned_muster_source_contact_sheet.png`, and `contact_sheets/event_019_unassigned_muster_processed_contact_sheet.png`. These sheets compare the retained formation, army, and host art at source and runtime sizes without presenting human leader references. The legacy processed derivative review filename `contact_sheets/event_019_derivative_portrait_contact_sheet.png` remains synchronized for existing documentation links.

The fixed portrait-slot subset validation covers 27 source files, 27 processed PNGs, and 27 runtime DDS files: stage-local hashes are unique, every processed/runtime scene is 156 by 210, every DDS is an uncompressed 32-bit BGRA file of 131168 bytes, and every processed PNG is decoded-pixel-equal to its DDS. Source and runtime-size visual review confirms that all twenty claimant slots read as distinct army/muster scenes, all six derivatives read as massed hosts or councils-as-massed-formations, the technical default reads as an anonymous muster, and none contains an individual focal human/person. The core validator also checks exact PNG/DDS dimensions, uncompressed 32-bit DDS masks and pixel fidelity, useful alpha, distinct icon hashes, real animation-frame distinctness, GIF frame counts, achievement overlays, TGA dimensions/depth/origin/compression, TGA pixel fidelity, and chroma-green flag borders. The current regional validator checks all 91 raw-to-spot-master rows, all 273 processed PNG/TGA pairs, exact bottom-left TGA headers and byte lengths, `file(1)` output, decoded pixel equality, opaque alpha, recorded spot palettes, and 91-way uniqueness independently at normal, medium, and small sizes. Machine-readable results are in `regional_flag_validation_2026_07_18.json` and `regional_flag_checksums_2026_07_18.sha256`.

## Simplifications, omissions, and blockers

The 91 current visual/runtime rows pass the independent row review. The independent remediation re-audit handoff `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md` is PASS and clears the regional asset gate. The final whole-event audit `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_completion_audit_2026_07_18.md` is PASS with P0/P1/P2 = 0. The recorded validator status remains the immutable literal `candidate_requires_independent_visual_review` processor-state field, not a contrary approval claim. Parent workbook/catalog reconciliation and export are complete, Event 19 and SCN-013 now read `Fully Functional`, and package inventory is complete at 33/33. No fallback or replacement asset is authorized. The Event 019 implementation owns the gameplay moments that select cosmetic tags and dispatches each zombie, ghost, and golem release or defeat report exactly once; all frozen asset identifiers required by that wiring are present.
