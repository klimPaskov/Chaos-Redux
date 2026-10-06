ï»¿# Shared Chaos Redux achievement icon repair report

Disposition: implemented Event 031 state repair; its 12 grey and 12 not-eligible DDS states are parent-reviewed, while all completed icons retain their original artwork. Nineteen other finding rows remain open.

## Implemented state repair

The severity 1 `GFX_achievement_031_fracture_from_within_not_eligible` finding is implemented for all twelve Event 031 achievements by rebuilding each not-eligible state from its matching fully desaturated source and the exact unchanged canonical red-X overlay. The severity 3 `GFX_achievement_031_no_second_blast_grey` finding is implemented for the same twelve achievements by deriving every grey source deterministically from the unchanged completed source with alpha and position preserved.

The existing completed DDS files were preserved byte-for-byte. The original 36 DDS triplets were copied before edits to `docs/assets/gfx_fix_2026-10/shared_chaosx_achievements/baseline/031_state_repair/`. The current source layers are the matching existing Event 031 source PNGs under `docs/assets/031_random_terror/achievement_sources/`; each source-over-template composition reproduces its current completed DDS exactly.

All 12 triplets were built and audited with `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`. The audit reports strict 64x64 legacy BGRA output and exact source-layer composition for every state. Every completed DDS still matches its pre-edit SHA-256, and all 24 repaired `_grey.dds` and `_not_eligible.dds` files match their reviewed staged DDS hashes.

The canonical inputs remain unchanged: `achievement_template.png` SHA-256 `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`, `achievement_template_grey.png` SHA-256 `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`, and `overlay.png` SHA-256 `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD`.

The native before/after evidence is [031_state_repair_native_before_after.png](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/031_state_repair_native_before_after.png), and the enlarged state comparison is [031_state_repair_4x_nearest_before_after.png](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/contact_sheets/031_state_repair_4x_nearest_before_after.png). Per-file source, baseline, staging, and runtime hashes are in [031_state_repair_validation.json](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_state_repair_validation.json). The exact 24 changed runtime paths and hashes are in [031_state_repair_runtime_paths.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_state_repair_runtime_paths.txt), and all 12 strict runtime audits are retained in [031_process_achievement_icons_runtime_audit.txt](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/031_process_achievement_icons_runtime_audit.txt).

The parent reviewed the native and 4x state sheets and approved this state tranche. The base artwork style findings remain open, and this state-only pass does not claim to repair the completed art.

## Remaining findings

| Sprite | Severity | Disposition | Evidence or next action |
| --- | ---: | --- | --- |
| `GFX_achievement_031_no_second_blast` | 2 | unresolved | Parent approved the v003 medal subject as the style benchmark; the other eleven distinct Event 031 subjects and a coherent family sheet remain to be produced before any completed-state promotion. |
| `GFX_achievement_031_maximum_survivor` | 2 | unresolved | The current completed art still has red X marks, which must be removed from the completed state. |
| `GFX_achievement_007_fury_no_cores` | 2 | unresolved | The current image remains near-duplicate to `007_fury_last_neighbor`; create a distinct coreless-map or empty-shield subject. |
| `GFX_achievement_005_soviet_collapse_every_port_a_council` | 2 | unresolved | The current icon remains a second sailor portrait; replace it with a port or council object subject. |
| `GFX_achievement_005_soviet_collapse_the_world_read_the_telegram` | 2 | unresolved | The current black-and-white photo remains; create the painted telegraph-key and telegram subject. |
| `GFX_achievement_005_soviet_collapse_file_that_became_country` | 2 | unresolved | The current photo texture remains; create a painted dossier, map, and seal subject. |
| `GFX_achievement_020_black_plague_first_cordon` | 2 | unresolved | The 020 unlocked states still lack visible colour separation; the complete plague family needs accent and medallion review. |
| `GFX_achievement_023_sov_nuclear_bombs_a_hundred_suns` | 2 | unresolved | Existing v1/v2 candidate triplets remain `needs_user_review` in `docs/assets/023_sov_nuclear_bombs/manifest.md`; parent review should decide whether either candidate can satisfy the new accent and frame finding. |
| `GFX_achievement_016_brilliant_scientist_the_former_host` | 2 | unresolved | The installed 016 source family exists, but the eight named achievements still need stronger colour accents and grey regeneration. |
| `GFX_achievement_010_death_last_ferry` | 2 | unresolved | The seven near-black 010 achievements need readable focal values and unlocked colour separation. |
| `GFX_achievement_asteroid_incoming_world_reconnected` | 2 | unresolved | The currently promoted 028 triplet matches the accepted v002 candidate hashes, but the globe still uses the flat-card treatment called out by this finding. |
| `GFX_achievement_020_black_plague_forty_days` | 3 | unresolved | The 13 020 achievement subjects still need the requested coherent medallion treatment. |
| `GFX_achievement_023_sov_nuclear_bombs_the_last_telephone` | 3 | unresolved | Existing 023 candidates remain `needs_user_review`; the current frame and unlocked-colour finding is still open. |
| `GFX_achievement_024_video_game_in_sweden_reality_check` | 3 | unresolved | Current runtime retains the flat-card icon. Dated candidate subjects exist at `docs/assets/024_video_game_in_sweden/source_png/repairs_20261006/`, with state previews under `processed_png/repairs_20261006/achievement_state_previews/`; they have not been promoted by this worker. |
| `GFX_achievement_027_doctrine_research_first_lesson` | 3 | unresolved | The installed Event 027 triplets are documented in `docs/assets/027_doctrine_research/`, but the current first-lesson family sheet still needs the shared medal treatment and simplified sibling subjects. |
| `GFX_achievement_019_infantry_spawn_three_false_apocalypses` | 3 | unresolved | The current completed icon remains a three-panel composition; a single medal subject is required. |
| `GFX_achievement_asteroid_incoming_government_beyond_the_crater` | 3 | unresolved | The promoted 028 candidate matches its recorded staging hashes, but its current square-card subject does not satisfy the new laurel style requirement. |
| `GFX_achievement_005_soviet_collapse_soviet_unbroken_signal` | 3 | unresolved | The 005 family still has undersized subjects; all 46 sources need the requested larger interior footprint while retaining their established family frame. |
| `GFX_achievement_asteroid_incoming_collector_of_fallen_stars` | 3 | unresolved | The promoted 028 subject still lacks a sufficiently visible unlocked colour accent. |

No art from the unresolved rows was overwritten. Existing 023 and 024 candidates remain available for parent review, and their original files stay in their event-owned workspaces.

## Contact-sheet incident

While inspecting the external sheet builder, I invoked `python 'C:/Users/klimp/Videos/chaos_redux_trailer/tools/gfx_sheets.py' --help`. The script has no argument parser, so it started its full default generator and wrote into the shared external `records/gfx_review/` directory. The exact command, confirmed process IDs, observed timestamp range, every output filename, and each post-overwrite hash are recorded in [old_sheet_overwrite_incident.md](../../assets/gfx_fix_2026-10/shared_chaosx_achievements/evidence/old_sheet_overwrite_incident.md). The original shared JPGs had already been inspected before this call, but their pre-overwrite file hashes were not captured; the replacement sheets are not treated as original-review proof. All subsequent current sheets were written only under this package's isolated `docs/assets/gfx_fix_2026-10/current_contact_sheets/` directory.

## Wiring and live review

No `.gfx`, GUI, gameplay, localisation, or registry files were edited. The existing achievement sprite names and root `gfx/achievements/` DDS paths remain unchanged. The parent owns the commit of the exact 24 state paths. The user owns live-game validation; no game or desktop window was launched by this worker.

## Committed runtime state crosswalk

The following exact paths carry this bounded state repair.

| Runtime DDS | SHA-256 |
|---|---|
| `gfx/achievements/031_no_second_blast_grey.dds` | `d7326c6451f23d94598820ad765fbd5dff69ffc1da02a3f584af53adcb2692b5` |
| `gfx/achievements/031_no_second_blast_not_eligible.dds` | `79c7bbc47366f935bec1bbfdf18bc2225863e3e0d22d159ff558bca64815a025` |
| `gfx/achievements/031_the_long_watch_grey.dds` | `2465ffdf8597420bff15c44fb4ad740e0e598a9a9407f287e03711891bfc4170` |
| `gfx/achievements/031_the_long_watch_not_eligible.dds` | `97546c6f6e53c74a477e75b70fa87a0c5758bcc5437545f552d5cf8c37067cd8` |
| `gfx/achievements/031_the_city_still_stands_grey.dds` | `9d415afa778543adb4c7d32f6fe4873892654ac00582956fb529861faf0e07b6` |
| `gfx/achievements/031_the_city_still_stands_not_eligible.dds` | `47fa6cbe18b3a5b616bc8036a8fdcaec4482698357b5baf9a6dfcb259b3450dd` |
| `gfx/achievements/031_cut_every_route_grey.dds` | `275a7888b1574fd1e4a900531d323517ce5cf20d7cc1b01fe24efaca27dcc165` |
| `gfx/achievements/031_cut_every_route_not_eligible.dds` | `ef06704608619ba145039a689d6ff8c885f849bf4bb6f440da7da55c8faf8c0c` |
| `gfx/achievements/031_the_false_claim_rejected_grey.dds` | `5e1fca07b1c44d5532a11dab8ce8cc7767dbd335be9f289b6fa7cb6407c29aff` |
| `gfx/achievements/031_the_false_claim_rejected_not_eligible.dds` | `3917726fa9e097706004f025a843efad28d820b0d0a226fd4d9ec3607f290ff4` |
| `gfx/achievements/031_no_collective_punishment_grey.dds` | `b9fb0716e04bcbd4057941cba16f30bfa57c892d3afe33255fc3de42156d4ee0` |
| `gfx/achievements/031_no_collective_punishment_not_eligible.dds` | `d2001f9fa3f400743c487c5ad9ac5d846e62f24360e8fd502e15a7ab346cffcb` |
| `gfx/achievements/031_enemy_of_my_enemy_grey.dds` | `ebdaa9c99b5cfeb4d8cbb0d9b87ec7f8adfef9aa21de3ac84dbae3e90bd87efa` |
| `gfx/achievements/031_enemy_of_my_enemy_not_eligible.dds` | `e48db7a9bf6d36bad4d65d928422db5425a86b1965ad6d156cde365a32815501` |
| `gfx/achievements/031_fracture_from_within_grey.dds` | `ecc6409ac94235a554a8b1076654ff569d8cfa93665852811fb924cd3cbb5467` |
| `gfx/achievements/031_fracture_from_within_not_eligible.dds` | `d6680e7ee83bdc586525cfb64ec18e9191ec9d1d813592b50017661203fa303e` |
| `gfx/achievements/031_maximum_survivor_grey.dds` | `367b6a1a6d354d50ce15669e21f338fd15b773a0cf972cac5d22579a6c13872a` |
| `gfx/achievements/031_maximum_survivor_not_eligible.dds` | `55ede06bbf078346df5b8c2fa5e13ccb983dc61555374b03f39f78074ea61c71` |
| `gfx/achievements/031_false_revelation_denied_grey.dds` | `058074cfef430de317504bea8de49f0ba9111e567dd82cac0b0b40d0d4a639bf` |
| `gfx/achievements/031_false_revelation_denied_not_eligible.dds` | `d4dbdefe270694fc8a1c582894b544a7b0e59c164d09ea12c4b58bef363e5959` |
| `gfx/achievements/031_victims_before_victory_grey.dds` | `56dba65ea7cb45afff5c0edd450623dcfcc520a19509acce734d3a21ef0b6c5d` |
| `gfx/achievements/031_victims_before_victory_not_eligible.dds` | `c70957222935ac7150de1a05d7691232291b3c38d689c67089119a4a879849b1` |
| `gfx/achievements/031_war_without_a_capital_grey.dds` | `c95ac4fe181831c13e36048ab429849014156a90fe6196f2dcb7e1b42d53923d` |
| `gfx/achievements/031_war_without_a_capital_not_eligible.dds` | `9136544384c19c10ce191bb29f40012f328c22a3f610e76f6c02ff17d4dd3859` |
