# Shared Chaos Redux achievement icon repair report

Disposition: four Event 031 achievement findings are implemented and parent-reviewed. A fifth finding is superseded by an already parent-integrated Event 024 medal triplet. Sixteen other finding rows remain unresolved.

## Event 031 achievement family

The approved Event 031 family now uses one original bronze laurel-medal subject per achievement, with each central emblem sized to remain clear at 64x64. Parent reviewed the exact native-size and 4x nearest contact sheets and approved the full triplet batch for promotion. The art interpretation is the canonical square achievement template beneath one transparent medal subject; it preserves the supplied template and adds no separate fabricated frame.

The eleven newly generated subjects each have a distinct center emblem and were generated individually with native transparency. The exact prompts and the accepted `031_no_second_blast` v003 style-reference scope are recorded in [031_remaining_subjects_prompts.md](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/prompts/031_remaining_subjects_prompts.md). The source PNGs are preserved under `docs/assets/gfx_fix_2026-10/shared_chaosx_achievements/source/`. Each source is 1254x1254 RGBA with real 0..255 alpha; no opaque-background removal was used. The subject normalizer crops only around alpha-visible content, scales within 56x56, centers on a 64x64 canvas, and resamples in premultiplied RGBA. Per-source dimensions, crop bounds, alpha ranges, and SHA-256 values are in the corresponding `evidence/031_*_alpha_report_v001.json` files.

Each 64x64 color subject was retained unchanged for the completed state. The grey source was derived with deterministic full desaturation while preserving its canvas, placement, and alpha. The not-eligible source is the grey layer composited with the unchanged canonical red-X overlay at exact 64x64 alignment. The exact canonical completed template, grey template, and overlay hashes are `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`, `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`, and `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD`. The source-triplet hash manifest is [031_generated_triplets_manifest.json](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_generated_triplets_manifest.json).

Final DDS triplets were produced with `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`, which verifies strict one-level 64x64 BGRA files and exact source-layer composition. All 12 promoted runtime triplets passed its audit; the saved results are in [031_generated_batch_runtime_audit.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_generated_batch_runtime_audit.txt). The contact sheets compare the previous runtime art against the staged candidate color, grey, and not-eligible states: [native 64x64](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/031_generated_batch_native.png) and [4x nearest](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/031_generated_batch_4x_nearest.png).

Before promotion, the worker verified that all 36 current runtime DDS files still matched the original completed and committed state-repair outputs, then saved a fresh pre-promotion snapshot under `docs/assets/gfx_fix_2026-10/shared_chaosx_achievements/baseline/031_art_promotion_preflight/`. The hash-guard record is [031_art_promotion_preflight.json](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_art_promotion_preflight.json). All 36 approved DDS files are promoted at their existing `gfx/achievements/<achievement_id>.dds` paths; the exact paths and final SHA-256 values are listed in [031_generated_batch_runtime_paths.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_generated_batch_runtime_paths.txt).

The earlier state-only tranche was parent-committed as `544ef6ab9`; this report supersedes its state-only status. Current completed art contains no eligibility X, all twelve grey states are fully grayscale, and all twelve not-eligible states use the unchanged red-X overlay. No `.gfx`, GUI, gameplay, localisation, or achievement registry files were edited, and all sprite names remain stable.

## Finding dispositions

| Sprite | Severity | Disposition | Evidence or remaining action |
| --- | ---: | --- | --- |
| `GFX_achievement_031_fracture_from_within_not_eligible` | 1 | implemented | The red-X state is now regenerated from the fully grayscale subject and canonical overlay for all twelve Event 031 achievements. |
| `GFX_achievement_031_no_second_blast` | 2 | implemented | The previously flat-square family was replaced with the parent-approved original laurel-medal family for all twelve Event 031 achievements. |
| `GFX_achievement_031_maximum_survivor` | 2 | implemented | The completed state now has a clear survivor-and-shield medal and no red X; its grey and not-eligible siblings are derived consistently. |
| `GFX_achievement_007_fury_no_cores` | 2 | unresolved | The current image remains near-duplicate to `007_fury_last_neighbor`; create a distinct coreless-map or empty-shield subject. |
| `GFX_achievement_005_soviet_collapse_every_port_a_council` | 2 | unresolved | The current icon remains a second sailor portrait; replace it with a port or council object subject. |
| `GFX_achievement_005_soviet_collapse_the_world_read_the_telegram` | 2 | unresolved | The current black-and-white photo remains; create the painted telegraph-key and telegram subject. |
| `GFX_achievement_005_soviet_collapse_file_that_became_country` | 2 | unresolved | The current photo texture remains; create a painted dossier, map, and seal subject. |
| `GFX_achievement_020_black_plague_first_cordon` | 2 | unresolved | The 020 unlocked states still lack visible colour separation; the complete plague family needs accent and medallion review. |
| `GFX_achievement_023_sov_nuclear_bombs_a_hundred_suns` | 2 | unresolved | Existing v1/v2 candidate triplets remain `needs_user_review` in `docs/assets/023_sov_nuclear_bombs/manifest.md`; parent review should decide whether either candidate can satisfy the accent and frame finding. |
| `GFX_achievement_016_brilliant_scientist_the_former_host` | 2 | unresolved | The installed 016 source family exists, but the eight named achievements still need stronger colour accents and grey regeneration. |
| `GFX_achievement_010_death_last_ferry` | 2 | unresolved | The seven near-black 010 achievements need readable focal values and unlocked colour separation. |
| `GFX_achievement_asteroid_incoming_world_reconnected` | 2 | unresolved | The promoted 028 triplet matches the accepted v002 candidate hashes, but the globe still uses the flat-card treatment called out by this finding. |
| `GFX_achievement_020_black_plague_forty_days` | 3 | unresolved | The 13 020 achievement subjects still need the requested coherent medallion treatment. |
| `GFX_achievement_023_sov_nuclear_bombs_the_last_telephone` | 3 | unresolved | Existing 023 candidates remain `needs_user_review`; the current frame and unlocked-colour finding is still open. |
| `GFX_achievement_024_video_game_in_sweden_reality_check` | 3 | superseded | Commit `18bf22a36` installed the parent-reviewed reality-check medallion triplet with a shared laurel layer. The completed DDS is `gfx/achievements/024_video_game_in_sweden_reality_check.dds`, SHA-256 `3113f513fc7b0ab378cb701ca3cba4885af688b04f1eb7b67e669e2e78a011d8`; all three states passed the package's strict 64x64 triplet audit. See [the current 024 repair round-trip sheet](../../assets/024_video_game_in_sweden/contact_sheets/20261006_024_graphics_repair_roundtrip_final_v2.png) and [per-asset QA](../024_video_game_in_sweden_plans/asset_repairs_20261006_qa.json). |
| `GFX_achievement_027_doctrine_research_first_lesson` | 3 | unresolved | The installed Event 027 triplets are documented in `docs/assets/027_doctrine_research/`, but the current first-lesson family sheet still needs the shared medal treatment and simplified sibling subjects. |
| `GFX_achievement_019_infantry_spawn_three_false_apocalypses` | 3 | unresolved | The current completed icon remains a three-panel composition; a single medal subject is required. |
| `GFX_achievement_asteroid_incoming_government_beyond_the_crater` | 3 | unresolved | The promoted 028 candidate matches its recorded staging hashes, but its current square-card subject does not satisfy the new laurel style requirement. |
| `GFX_achievement_005_soviet_collapse_soviet_unbroken_signal` | 3 | unresolved | The 005 family still has undersized subjects; all 46 sources need the requested larger interior footprint while retaining their established family frame. |
| `GFX_achievement_asteroid_incoming_collector_of_fallen_stars` | 3 | unresolved | The promoted 028 subject still lacks a sufficiently visible unlocked colour accent. |
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


## Handoff boundary

The existing achievement sprite names and `gfx/achievements/` paths remain unchanged, so no `.gfx` repoint is required for this family. The parent owns the reviewed commit. The user owns live-game validation; this worker did not launch the game or open a desktop window.
