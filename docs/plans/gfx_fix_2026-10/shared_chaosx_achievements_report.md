# Shared Chaos Redux achievement icon repair report

Disposition: nineteen findings are implemented and parent-reviewed, one Event024 finding is superseded, and the Event005 family-scale finding remains in final production.
The 60-DDS selected Event005-object/proxy,010,016 and019 tranche is committed in `aa6d070406788d4f49b3776febfd7500fe8b050e`.
The 21 Event020/027/028 achievements and their 63 DDS states are committed in `e53a03a9a1a571a975f7129f4a9d60d068eb1e1d`.

## Event 007 No Cores repair

The near-duplicate map-and-figure subject was replaced with a distinct hollow-core map emblem in the Event 007 aged-bronze plaque style. Parent approved v002, which keeps the missing core region as a large empty center and uses a few broad map boundaries. The exact original and edit prompts are in [v001](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/prompts/007_no_cores_subject_v001.md) and [v002](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/prompts/007_no_cores_subject_v002_edit.md); the selected native-alpha source and processing evidence are [v002 source](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/source/007_fury_no_cores_source_v002.png) and [alpha report](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/007_fury_no_cores_alpha_report_v002.json).

The selected 64x64 color subject was converted to the exact achievement source triplet by deterministic grayscale and the unchanged red-X overlay, then processed with `process_achievement_icons.py`. Parent-reviewed native-size and 4x candidate comparisons are [here](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/007_fury_no_cores_v002_candidate_native.png) and [here](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/007_fury_no_cores_v002_candidate_4x_nearest.png). All three promoted DDS states passed the strict 64x64 BGRA/source-layer audit in [007_no_cores_runtime_audit.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/007_no_cores_runtime_audit.txt). The current-runtime preflight and preserved originals are recorded in [007_art_promotion_preflight.json](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/007_art_promotion_preflight.json), with exact final paths and SHA-256 values in [007_no_cores_runtime_paths.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/007_no_cores_runtime_paths.txt).

## Event 005 object replacements and family-scale review

The parent reviewed and approved three original Event 005 medallion objects: an anchor with a port crane and council banner, a brass telegraph key with a stamped telegram, and a dossier with a map and wax seal. The transparent source masters, exact ImageGen requests, alpha reports, deterministic source-triplet manifests, native/4x review sheets, and strict DDS round-trip audit are retained under `docs/assets/gfx_fix_2026-10/shared_chaosx_achievements/`. The runtime triplets were promoted only after verifying their existing files against committed Git LFS object OIDs and saving the prior nine DDS files to `baseline/005_object_repairs_preflight/`. The exact final paths and SHA-256 values are in [005_object_repairs_runtime_paths.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/005_object_repairs_runtime_paths.txt); [the runtime audit](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/005_object_repairs_runtime_audit.txt) confirms strict 64x64 BGRA/source-layer equality.

The 005 family-scale finding remains unresolved while the other below-target subjects are repaired. The exact-native-size inventory contains 45 available color DDS files: [005_native_family_64.png](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/005_native_family_64.png), [4x nearest detail](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/005_native_family_4x_nearest.png), the ordered [hash/status index](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/005_native_family_contact_sheet_index.json), and [the 45-ID scale review](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/005_scale_visual_review.json). Current source contains 40 registered achievements and five unregistered legacy DDS files, while the issue note cites 46 subjects; no missing 46th asset was guessed or registered, and no orphan was changed. No preserved 005 subject-layer PNGs exist in `docs/assets` or repository history, so the authorized source route is a native-alpha ImageGen subject edit composited over the frozen opaque runtime composite.

The first parent-approved scale pilot is `005_soviet_collapse_proxy_without_master`, whose original red seal and attached green-gold tab were visibly below the 32px guide. The selected native-alpha source is [v005](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/source/005_proxy_scale_pilot/005_proxy_without_master_generated_v005.png), with its exact [ImageGen prompt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/prompts/005_proxy_without_master_scale_pilot_v005.md). The processed seal-plus-tab silhouette is 31x30px against the 42px inner field (74% of the target field), and the original plate/laurel pixels outside the new alpha mask remain unchanged. Parent reviewed the focused native and 4x comparisons: [native](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/005_proxy_scale_pilot_candidate_v005_captioned_native.png) and [4x nearest](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/005_proxy_scale_pilot_candidate_v005_captioned_4x_nearest.png).

The approved proxy source triplet was processed by `process_achievement_icons.py`, promoted to its three existing runtime paths after an LFS-aware per-file hash guard, and strictly decoded at 64x64. The [triplet audit](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/005_proxy_triplet_staging_audit.json), [promotion preflight and preserved originals](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/005_proxy_art_promotion_preflight.json), and [final runtime hashes](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/005_proxy_promoted_runtime_paths.txt) record template/overlay identities, old/new hashes, source-to-DDS equality, and unchanged sprite names. The pilot is complete; no GFX edits were made.

The 45-ID guide identifies these additional registered subjects below target: `all_roads_leave_moscow`, `black_soil_black_banner`, `diplomats_knife`, `double_game`, `eastern_buffer_without_moscow`, `no_empty_borders`, `southern_cascade`, `three_capitals_one_chain`, and `world_as_one_factory`. The named `soviet_unbroken_signal` star already exceeds the requested center footprint and was left unchanged.

## Event 031 achievement family

The approved Event 031 family now uses one original bronze laurel-medal subject per achievement, with each central emblem sized to remain clear at 64x64. Parent reviewed the exact native-size and 4x nearest contact sheets and approved the full triplet batch for promotion. The art interpretation is the canonical square achievement template beneath one transparent medal subject; it preserves the supplied template and adds no separate fabricated frame.

The eleven newly generated subjects each have a distinct center emblem and were generated individually with native transparency. The exact prompts and the accepted `031_no_second_blast` v003 style-reference scope are recorded in [031_remaining_subjects_prompts.md](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/prompts/031_remaining_subjects_prompts.md). The source PNGs are preserved under `docs/assets/gfx_fix_2026-10/shared_chaosx_achievements/source/`. Each source is 1254x1254 RGBA with real 0..255 alpha; no opaque-background removal was used. The subject normalizer crops only around alpha-visible content, scales within 56x56, centers on a 64x64 canvas, and resamples in premultiplied RGBA. Per-source dimensions, crop bounds, alpha ranges, and SHA-256 values are in the corresponding `evidence/031_*_alpha_report_v001.json` files.

Each 64x64 color subject was retained unchanged for the completed state. The grey source was derived with deterministic full desaturation while preserving its canvas, placement, and alpha. The not-eligible source is the grey layer composited with the unchanged canonical red-X overlay at exact 64x64 alignment. The exact canonical completed template, grey template, and overlay hashes are `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`, `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`, and `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD`. The source-triplet hash manifest is [031_generated_triplets_manifest.json](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_generated_triplets_manifest.json).

Final DDS triplets were produced with `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`, which verifies strict one-level 64x64 BGRA files and exact source-layer composition. All 12 promoted runtime triplets passed its audit; the saved results are in [031_generated_batch_runtime_audit.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_generated_batch_runtime_audit.txt). The contact sheets compare the previous runtime art against the staged candidate color, grey, and not-eligible states: [native 64x64](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/031_generated_batch_native.png) and [4x nearest](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/031_generated_batch_4x_nearest.png).

Before promotion, the worker verified that all 36 current runtime DDS files still matched the original completed and committed state-repair outputs, then saved a fresh pre-promotion snapshot under `docs/assets/gfx_fix_2026-10/shared_chaosx_achievements/baseline/031_art_promotion_preflight/`. The hash-guard record is [031_art_promotion_preflight.json](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_art_promotion_preflight.json). All 36 approved DDS files are promoted at their existing `gfx/achievements/<achievement_id>.dds` paths; the exact paths and final SHA-256 values are listed in [031_generated_batch_runtime_paths.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_generated_batch_runtime_paths.txt).

The earlier state-only tranche was parent-committed as `544ef6ab9`; this report supersedes its state-only status. Current completed art contains no eligibility X, all twelve grey states are fully grayscale, and all twelve not-eligible states use the unchanged red-X overlay. No `.gfx`, GUI, gameplay, localisation, or achievement registry files were edited, and all sprite names remain stable.

## Event 023 nuclear achievement family

Parent reviewed the exact native-size and 4x nearest Event 023 family sheet, then approved all seven medal triplets for promotion after a focused Firebreak revision. The new subjects replace grey-card hardware renders with distinct bronze-laurel medals, high-contrast center subjects, and restrained warm accents. Firebreak v002 replaces its numeral-like switch with a plain round brass dial; the focused Firebreak 64px and 4x sheets are retained with the full-family views.

The selected sources, exact prompt records, alpha reports, processed PNGs, source triplets, staged DDS files, and the original runtime hashes are listed in [023_source_prompt_evidence_paths.md](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/023_source_prompt_evidence_paths.md) and [023_promoted_runtime_manifest.json](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/023_promoted_runtime_manifest.json). The v001 candidates that carried the unrelated 031 city motif remain preserved; the five affected subjects use separate text-only v002 requests, and Firebreak uses a focused v002 edit. The v2 native and 4x family sheets are [here](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/023_nuclear_family_v002_native.png) and [here](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/023_nuclear_family_v002_4x_nearest.png).

All 21 current 023 DDS files passed the strict 64x64 BGRA/source-layer audit after promotion; saved results are in [023_runtime_triplet_audit.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/023_runtime_triplet_audit.txt). The LFS-aware preflight matched all 21 prior runtime files against their committed object OIDs and saved untouched originals in `baseline/023_art_promotion_preflight/`. Exact final runtime paths and SHA-256 values are listed in [023_final_runtime_paths.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/023_final_runtime_paths.txt). The stable achievement sprites and root DDS destinations were preserved; no `.gfx` edits were made.

## Finding dispositions

| Sprite | Severity | Disposition | Evidence or remaining action |
| --- | ---: | --- | --- |
| `GFX_achievement_031_fracture_from_within_not_eligible` | 1 | implemented | The red-X state is now regenerated from the fully grayscale subject and canonical overlay for all twelve Event 031 achievements. |
| `GFX_achievement_031_no_second_blast` | 2 | implemented | The previously flat-square family was replaced with the parent-approved original laurel-medal family for all twelve Event 031 achievements. |
| `GFX_achievement_031_maximum_survivor` | 2 | implemented | The completed state now has a clear survivor-and-shield medal and no red X; its grey and not-eligible siblings are derived consistently. |
| `GFX_achievement_007_fury_no_cores` | 2 | implemented | Parent-approved v002 replaces the duplicate map-and-figure with a large hollow-core map emblem in the Event 007 bronze-plaque style. The three current DDS files and SHA-256 values are in [the 007 runtime crosswalk](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/007_no_cores_runtime_paths.txt). |
| `GFX_achievement_005_soviet_collapse_every_port_a_council` | 2 | implemented | Parent-approved anchor, crane, and council-banner medal replaces the duplicate sailor portrait; the final triplet paths and hashes are in [the 005 runtime crosswalk](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/005_object_repairs_runtime_paths.txt). |
| `GFX_achievement_005_soviet_collapse_the_world_read_the_telegram` | 2 | implemented | Parent-approved painted telegraph key and stamped telegram replaces the black-and-white photograph, with grey and not-eligible states derived consistently. |
| `GFX_achievement_005_soviet_collapse_file_that_became_country` | 2 | implemented | Parent-approved dossier/map/wax-seal medal replaces the grainy photo texture; the final triplet passed strict DDS/source-layer checks. |
| `GFX_achievement_020_black_plague_first_cordon` | 2 | implemented | All 13 plague color subjects use readable physical accents; their grey/X states are derived consistently. Parent-approved63-state package is committed in `e53a03a9a`. |
| `GFX_achievement_023_sov_nuclear_bombs_a_hundred_suns` | 2 | implemented | The parent-approved medal family gives the vault-and-device emblem a strong brass accent; the grey and not-eligible states were derived from the color source. See the [023 runtime crosswalk](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/023_final_runtime_paths.txt). |
| `GFX_achievement_016_brilliant_scientist_the_former_host` | 2 | implemented | All eight named scientist subjects received physical color accents; the former-host and combined-arms v002 revisions were explicitly parent-approved. The 24 matching color/grey/X DDS are committed in `aa6d07040`. |
| `GFX_achievement_010_death_last_ferry` | 2 | implemented | All seven dark-atlas subjects received readable focal lighting and color accents; the No Witnesses v003 globe has the approved strong red land relief. The 21 DDS are committed in `aa6d07040`. |
| `GFX_achievement_asteroid_incoming_world_reconnected` | 2 | implemented | The globe is a dark-metal relief within coherent bronze laurels, with readable gold route lines and a matching grayscale state. |
| `GFX_achievement_020_black_plague_forty_days` | 3 | implemented | All 13 plague subjects use coherent bronze-laurel medallions and unclipped native-size framing; current sources, runtime hashes and before/after sheets are in the secondary achievement handoff. |
| `GFX_achievement_023_sov_nuclear_bombs_the_last_telephone` | 3 | implemented | The parent-approved dark-bronze laurel medal shows the hotline receiver and safe launch lever with unlocked color accents; the full 023 triplet family is verified at the exact runtime paths. See the [023 runtime crosswalk](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/023_final_runtime_paths.txt). |
| `GFX_achievement_024_video_game_in_sweden_reality_check` | 3 | superseded | Commit `18bf22a36` installed the parent-reviewed reality-check medallion triplet with a shared laurel layer. The completed DDS is `gfx/achievements/024_video_game_in_sweden_reality_check.dds`, SHA-256 `3113f513fc7b0ab378cb701ca3cba4885af688b04f1eb7b67e669e2e78a011d8`; all three states passed the package's strict 64x64 triplet audit. See [the current 024 repair round-trip sheet](../../assets/024_video_game_in_sweden/contact_sheets/20261006_024_graphics_repair_roundtrip_final_v2.png) and [per-asset QA](../024_video_game_in_sweden_plans/asset_repairs_20261006_qa.json). |
| `GFX_achievement_027_doctrine_research_first_lesson` | 3 | implemented | The three doctrine subjects are distinct compact medals: book/sword, one shield, and combined shield/compass. The crowded corner emblems were replaced with large focal objects. |
| `GFX_achievement_019_infantry_spawn_three_false_apocalypses` | 3 | implemented | One original three-bell bronze-laurel medal replaces the triptych; the matching grey/X states preserve the canonical overlay. The triplet is committed in `aa6d07040`. |
| `GFX_achievement_asteroid_incoming_government_beyond_the_crater` | 3 | implemented | All five asteroid subjects share the accepted bronze-laurel style; the crater/causeway replaces the unframed square-card treatment. |
| `GFX_achievement_005_soviet_collapse_soviet_unbroken_signal` | 3 | unresolved | Current family inventory is 40 registered IDs plus five unregistered legacy DDS files (45 total); the issue cites 46 and no guessed asset was added. The named red-star subject already exceeds the 32px guide and remains unchanged. Parent-approved pilot `proxy_without_master` now has a 31x30 subject-only replacement triplet promoted at unchanged sprite paths; nine other below-target registered subjects remain. See the 45-ID evidence, captioned guide sheets, and pilot runtime hash crosswalk above. |
| `GFX_achievement_asteroid_incoming_collector_of_fallen_stars` | 3 | implemented | The selected meteor specimen has a physical amber/gold accent, remaining clearly distinct from its fully grayscale counterpart. |
| `GFX_achievement_031_no_second_blast_grey` | 3 | implemented | All twelve Event 031 grey states are fully grayscale with canvas, subject position, and alpha preserved. |

## Contact-sheet incident

While inspecting the external sheet builder, I invoked `python 'C:/Users/klimp/Videos/chaos_redux_trailer/tools/gfx_sheets.py' --help`. The script has no argument parser, so it started its full default generator and wrote into the shared external `records/gfx_review/` directory. The exact command, confirmed process IDs, observed timestamp range, every output filename, and each post-overwrite hash are recorded in [old_sheet_overwrite_incident.md](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/old_sheet_overwrite_incident.md). The original shared JPGs had already been inspected before this call, but their pre-overwrite file hashes were not captured; the replacement sheets are not treated as original-review proof. All later review sheets were written only under the isolated task directories in `docs/assets/gfx_fix_2026-10/`.

## Runtime paths and SHA-256

| Runtime DDS | SHA-256 |
| --- | --- |
| `gfx/achievements/031_no_second_blast.dds` | `02978D4892F5C44A8F55A4DA8BF89B14DE2742BFEC90B7885951B190A1787800` |
| `gfx/achievements/031_no_second_blast_grey.dds` | `20A6339B84B0151D8D7366AA588FB7A4C2CDE333A346F6F381A44F5F8AB71E62` |
| `gfx/achievements/031_no_second_blast_not_eligible.dds` | `A83986E27A8CE0B8AADEDED4E9EE278CD3D11B7B06AE14B49B7B91EED0F0B6A7` |
| `gfx/achievements/031_the_long_watch.dds` | `134BA4DF920E6681EF4640F08C5593B90EE3D7C0DFD47E200AFB0263F26B502D` |
| `gfx/achievements/031_the_long_watch_grey.dds` | `228F158899C7ED4BE783B34486BBE4AB12AB50704FACE6A464879FD5E70E8522` |
| `gfx/achievements/031_the_long_watch_not_eligible.dds` | `9EC935AB8D0F7E2C12B9EACC594DA9FB32205567B6781351435CF455E67F2A73` |
| `gfx/achievements/031_the_city_still_stands.dds` | `ED8C31DBA13DE6D5BAE420E1C227AAAABB1BD67766125501CD18E25B2D60C32B` |
| `gfx/achievements/031_the_city_still_stands_grey.dds` | `C874B77FD80BC325812199AE0861B42D7B1D3C8C2A59AB90EE8ACCFC132D465D` |
| `gfx/achievements/031_the_city_still_stands_not_eligible.dds` | `448741573DB2684AF45DD0F65609A0945F389E3B5D48C6059C98276B958A1D15` |
| `gfx/achievements/031_cut_every_route.dds` | `D8E68BD4DE1A1C4A6350744491587BEDCAB2E16B442E21354694978857D679D5` |
| `gfx/achievements/031_cut_every_route_grey.dds` | `FE279A4FE615DF3D58F41ABEAB9900B1E219C6F53FD5256A0F71FF104D67020D` |
| `gfx/achievements/031_cut_every_route_not_eligible.dds` | `A73EFD28D516733E56065F182F7A98B08EC4357D4E574E5599448F4F398F758F` |
| `gfx/achievements/031_the_false_claim_rejected.dds` | `F83B7D6F0F35CDE0A7B22A005E004E7A55FA767858CC21A894496AB528BD3E7A` |
| `gfx/achievements/031_the_false_claim_rejected_grey.dds` | `FCC13D2678E6004823194A5F95D97CBFF62DE5F98B08127C93F8CDF4685B83D3` |
| `gfx/achievements/031_the_false_claim_rejected_not_eligible.dds` | `150891DD3C8730972A7407FDB114876E0ACBC108950551950D7B23287281746C` |
| `gfx/achievements/031_no_collective_punishment.dds` | `959548280A42A6BCA1FE54CA856105A4C46A3E576CF9109DDD1D1DB38A77D1F6` |
| `gfx/achievements/031_no_collective_punishment_grey.dds` | `D10BA85EB5287F5AA77A92254ECECD6832C11E258ACBD14A546AAA02C9054090` |
| `gfx/achievements/031_no_collective_punishment_not_eligible.dds` | `FB140D8FAD89644A0FA72DACF631D950361B770989EF4F0BD4811F0778ADC141` |
| `gfx/achievements/031_enemy_of_my_enemy.dds` | `E48F2A928A6A22A7C810A44BD0FEB0E928DF4A963D71AE174470819C25C5228C` |
| `gfx/achievements/031_enemy_of_my_enemy_grey.dds` | `23C96B2ADF73C98AC8FAB2A4CB5DCF730B683832A31A08189DF3CBBCB40CA38E` |
| `gfx/achievements/031_enemy_of_my_enemy_not_eligible.dds` | `9782A388F367EE213E56E479BCBB61A81BCD1C892979E1A98DE9FFAE25428FC8` |
| `gfx/achievements/031_fracture_from_within.dds` | `7702D88F9DD05446E86FEEB0609B35003217C131445F6B003901AF8E247D098D` |
| `gfx/achievements/031_fracture_from_within_grey.dds` | `EA01D3EC3312341028EB7A73B8F815C0A5D3DC422972A905D44B3781476EC175` |
| `gfx/achievements/031_fracture_from_within_not_eligible.dds` | `0893D3F5EBC26601D6F5F85EA2AC500395ADDD66CD3D493F4D206261DAD201AE` |
| `gfx/achievements/031_maximum_survivor.dds` | `C99577F03DB5998C9F6ED05053EE25BF6954F045C823BA0EA1F105EC99E5EFCB` |
| `gfx/achievements/031_maximum_survivor_grey.dds` | `E0AD25E7D3250392EBE77CDC3798B702F8E37A016ECFCC82E8AE44142D656544` |
| `gfx/achievements/031_maximum_survivor_not_eligible.dds` | `226D4466F66C5BE2B6B46B0EADF2255E3F8FA19C28FFFB83AF4CCB263E69C720` |
| `gfx/achievements/031_false_revelation_denied.dds` | `30998BC863A3641102ABF5960CA7C7A8F8D449A08510013B918CBA8977141D76` |
| `gfx/achievements/031_false_revelation_denied_grey.dds` | `04AD1A07B2B83A3BCCFA7033DB9EEB86804A1CAD7EA26BC84DCF3B2A20CAFC5D` |
| `gfx/achievements/031_false_revelation_denied_not_eligible.dds` | `3D6CB98CF74ADB402C5ADC9C7627E24005192E4E9335DAC26E1E2EE58D447D11` |
| `gfx/achievements/031_victims_before_victory.dds` | `EE5ACCA686911D768CF378343E2C3AD1BD542B465BCCD571080505F721DF2E94` |
| `gfx/achievements/031_victims_before_victory_grey.dds` | `184330943122A61385E7002113118403C5E641192F1B82E0A0DB3F0452D32030` |
| `gfx/achievements/031_victims_before_victory_not_eligible.dds` | `6BAFE1E6C8A89B9E404C696FDD8CCDE02C0FD8DFB91CA9C790EBAECFD69D3B34` |
| `gfx/achievements/031_war_without_a_capital.dds` | `B5E12846D86B0D1B847CC32636B93C7ABD4577634CB5BBE1F9B2526CE29CE07D` |
| `gfx/achievements/031_war_without_a_capital_grey.dds` | `477070FE5E1F380FD03CA00952CA8D971124342888A07523517B233569924897` |
| `gfx/achievements/031_war_without_a_capital_not_eligible.dds` | `B7F5E671CD20040417116793D99DC8AA6181D9A59DAD6CF4AFAFAE89DAAB2461` |


## Event 023 runtime paths and SHA-256

| Runtime DDS | SHA-256 |
| --- | --- |
| `gfx/achievements/023_sov_nuclear_bombs_a_hundred_suns.dds` | `E1525691899D21636589B2DC1B311774CD32331D71616D592A017AECC8320D38` |
| `gfx/achievements/023_sov_nuclear_bombs_a_hundred_suns_grey.dds` | `E351ACCD1086CD48F39DDFBADD4A7C13104310BB71EEF8AAE7D2964A68A82325` |
| `gfx/achievements/023_sov_nuclear_bombs_a_hundred_suns_not_eligible.dds` | `86FF4D9F105146E951B35C7BAF5D6F655E9128DE83A00D41DAF7633FA1CCCF25` |
| `gfx/achievements/023_sov_nuclear_bombs_the_bomb_never_fell.dds` | `1F00FDD53CCA4016881F8E7266966CCF164290B41163604035DF3D1F09008D61` |
| `gfx/achievements/023_sov_nuclear_bombs_the_bomb_never_fell_grey.dds` | `913697F55C2C327583BFC43DA2564F4ECD4FFC5F1875E87AE2B721BB0EB73A3B` |
| `gfx/achievements/023_sov_nuclear_bombs_the_bomb_never_fell_not_eligible.dds` | `B8FAFFD1C957CA24BB1FB8EB9EB79F5E6573843CE2C52D285E6F086E8BA7D0D8` |
| `gfx/achievements/023_sov_nuclear_bombs_ultimatum_without_ash.dds` | `98F218C075895F65F4A690194B36F8C69E918A8A1180C06A17E56F813AF38AD9` |
| `gfx/achievements/023_sov_nuclear_bombs_ultimatum_without_ash_grey.dds` | `DE6535E0EC82166C283F34777041DE9DB76AD7A28EF2BEAC5D623DCD4057A95E` |
| `gfx/achievements/023_sov_nuclear_bombs_ultimatum_without_ash_not_eligible.dds` | `F4620F8FE04B70C26C59860BCC100EC9AAF7E5EACA8CB98CCA2012FF0D1513D0` |
| `gfx/achievements/023_sov_nuclear_bombs_scattered_arsenal.dds` | `CEC7EAEA2D0FE64CCC64FD2C4E738D14D8813D44CE79F86AB8DACA35EBCB06B9` |
| `gfx/achievements/023_sov_nuclear_bombs_scattered_arsenal_grey.dds` | `E551662E4F0C9004B84D5B87A992C42E1287A6234E476CF185D35A438CBB5118` |
| `gfx/achievements/023_sov_nuclear_bombs_scattered_arsenal_not_eligible.dds` | `63B73BC638D6A643EF13C3B3BD0BE41BD8E0B540CAA833A76FB755047F268E67` |
| `gfx/achievements/023_sov_nuclear_bombs_firebreak.dds` | `5316BAF0CA9C5CD0862393554E5AF89C71E36CD035E436B6498BB9279771990D` |
| `gfx/achievements/023_sov_nuclear_bombs_firebreak_grey.dds` | `67A6880023FBEAC05DFFDE079202B042F7BD94671516732FD4CE9C1AB149E738` |
| `gfx/achievements/023_sov_nuclear_bombs_firebreak_not_eligible.dds` | `BD399CA9CB92154CB7320C2C8C7C63927FFFCFDC3DA58DC1BEF7A0DF25FC5D79` |
| `gfx/achievements/023_sov_nuclear_bombs_first_and_last.dds` | `08E0FF92950BA2DB6DB79863E0EFC691685CA5710883960C92D9111ACBEF3F72` |
| `gfx/achievements/023_sov_nuclear_bombs_first_and_last_grey.dds` | `ABDF1C8F323976D37F67291AFF23D8124C47FE323AC634F133833F19ABC7904E` |
| `gfx/achievements/023_sov_nuclear_bombs_first_and_last_not_eligible.dds` | `BC160FC0C9621E14697113BD97076EF60C122A909744D84A8F99BB4519B65853` |
| `gfx/achievements/023_sov_nuclear_bombs_the_last_telephone.dds` | `9211F60800CE83A833F3D1B015E8B52AD5C34AD06B2F50B304719A838A89D20B` |
| `gfx/achievements/023_sov_nuclear_bombs_the_last_telephone_grey.dds` | `AB3EB0E4B42F8AA77463D5898A63DBCFA88E2AD2DEB077BBE6C9A54A2438C039` |
| `gfx/achievements/023_sov_nuclear_bombs_the_last_telephone_not_eligible.dds` | `D26081EF36230E537DE6D9EA482DD8067BD9309EFC2FF77D08C11A3097F8F56B` |


## Handoff boundary

The existing achievement sprite names and `gfx/achievements/` paths remain unchanged, so no `.gfx` repoint is required for this family. The parent owns the reviewed commit. The user owns live-game validation; this worker did not launch the game or open a desktop window.

## Parent Event020,027 and028 acceptance

The parent viewed all three family before/after sheets at native 64px and 4x nearest, approved all 21 subjects, and independently checked all 63 installed DDS against the exact canonical-template/source composition.
The final selected native masters, all 23 exact ImageGen call receipts, both rejected cordon attempts, frozen baseline hashes, guarded promotion, current runtime path/hash table and per-family sheets are preserved in `docs/assets/gfx_fix_2026-10/shared_secondary_achievements/`.
The independent result is `evidence/parent_independent_63_compositions.json`; the selected source crosswalk is `evidence/selected_lineage_final_packet.json`; commit is `e53a03a9a1a571a975f7129f4a9d60d068eb1e1d`.
The earlier Event007/031 runtime commits retain their original outcomes; their 426-path source/review archive is committed in `14728948cd21408d1a78a38dac09dad59aacec91`.

## Parent selected60 acceptance

The parent independently strict-decoded all 60 installed DDS, compared every RGBA byte with the approved 64px processed review PNG, and verified every selected native-source and exact-prompt hash.
The crosswalk is `evidence/selected_achievement_bundle_60_20261006.json`; independent evidence is `evidence/selected_achievement_parent_independent_60.json`; commit is `aa6d070406788d4f49b3776febfd7500fe8b050e`.
