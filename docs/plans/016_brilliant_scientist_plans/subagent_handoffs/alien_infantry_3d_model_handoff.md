# Alien infantry 3D model production handoff

Status: incomplete, `needs_user_review`. The first Meshy 7 candidate is rejected; failure-driven paid recovery is awaiting user authorization.

## Work completed

The deterministic Event016 job was initialized at `docs/assets/016_brilliant_scientist/models_3d/alien_infantry`, with exact reusable consumer `alien_infantry_entity`. The official Meshy route, exact `meshy-7` identifier, repository Blender adapter, Blender build, and checksum-locked exporter were verified before spend. The adapter override already resolves `alien_infantry` to this job root; no adapter or checksum-lock change was required.

The original opaque ImageGen soldier and both failed opaque native-alpha edits were preserved. The repository-permitted background-removal fallback created exactly one provider input without changing the soldier's RGB content. Its SHA-256 is `E71F874C68B5E995206B6BD083498642E434C6A89BA64899A3DF13789ADE6CD2`. The alpha maximum of 253 is a probabilistic soft-matte characteristic. A faint head/rifle fringe was recorded, and seven-view Blender inspection found no obvious halo-derived shell.

Meshy 7 task `01a02497-1fb9-7a1b-bec6-ec388d54a016` succeeded technically and consumed 30 credits. The GLB SHA-256 is `E22474E3697FEF917E98AF9A3FD6B544A66E10B5C4A45A5FF4967546638A527A`; the FBX SHA-256 is `B16734164A6A208B0B89349BED24339B0D97DC7092E53B81B19BC676B82171D6`. No paid task existed in the job before this call. Provider downloads and PBR maps were archived immediately with request, response, task, credit, and checksum evidence.

## Rejection and Blender evidence

The generated T-pose is unarmed: the required readable retro-futurist laser rifle is completely absent. This is a hard identity/component failure, so the candidate was rejected before rig, animation, runtime texture conversion, or PDX export.

The protected provider source contained 1,995,264 triangles; the working QA duplicate has 29,999 triangles, 20,163 loose boundary edges, 356 boundary components, 48 branched boundary components, zero non-manifold edges, and zero degenerate faces. Blender adapter request `24b292a4a93948deb8ac38c74d85e108` produced the report, protected source, checkpoints, and seven views. Automatic checkpoint filenames containing `approved` are adapter stage names and are not acceptance evidence.

Vanilla calibration used installed `gfx/models/units/western_european_infantry.mesh` and `gfx/entities/units_infantry.asset#infantry_rifle_entity`, forward `-Y`, up `+Z`, entity scale `0.8`. Measured vanilla source height was `7.351824797689915`; candidate source height was `7.3537750244140625`; effective candidate runtime height was `5.8830200195312505`, a `0.0015605927312503098` delta. Scale passed, but the rifle failure remains decisive.

No rig, weight audit, packed PDX material, `.mesh`, `.anim`, export, or reimport result exists. Required `idle`, `move`, `laser_attack`, `defend`, `support_attack`, `retreat`, and `death` actions are all explicitly blocked. No static or semantic substitution was made.

## Versions and lock evidence

- Official Meshy MCP: `@meshy-ai/meshy-mcp-server` `0.4.0`, git `d8c77d1cb897e345eb41d38b510b8391b1664346`, revision `meshy-7-v4`.
- Blender: `5.1.2`, build `ec6e62d40fa9`.
- Blender HOI4 adapter: `chaosx_blender_hoi4` `1.5.0`; all four source hashes matched `.tools/3d_pipeline/config/dependencies.lock.json`.
- `io_pdx_mesh`: `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Adapter health request: `103f7c71c86645bc84e1d2efc279ca53`.
- Environment verifier: zero findings.

## Sourced sound package

All four candidates are CC0 1.0 and preserve immutable originals plus mechanically derived mono 44.1 kHz signed 16-bit PCM files.

- Laser fire: bart, [Space Laser](https://opengameart.org/content/space-laser), original SHA `3A26ECAB8F36DCA14A91519657E60351566A268D28A2EC4F933B0F9718A7258D`, derived `alien_infantry_laser_fire.wav` SHA `4E9552C0D023A34BBE816DAD3443E7C4C0C889720C5F5735871F2D7D7682C770`; trimmed to 1.2 seconds with a 0.95-1.20 second fade. Bind to `laser_attack` and `support_attack` muzzle discharge after accepted actions exist.
- Movement: GboxMikeFozzy, [Footsteps](https://opengameart.org/content/footsteps-0), original SHA `33C9BEF5E8AEB1069455699A34A0C5E1EF1787FD3F61594B0859D7E6BB9F9DEC`, derived `alien_infantry_move.wav` SHA `E0B36F9B38769ADD16F2569189B7B013749D6F014C37CDB146CD61B060A6A99E`; bind at grounded contacts in `move` and `retreat`.
- Idle: Ogrebane, [Sci-Fi Vehicle Sound](https://opengameart.org/content/sci-fi-vehicle-sound), original SHA `46AB090FAE668CD83D613019EBC42F8F24B4C511572F4EAC024AD5006680E350`, derived `alien_infantry_idle.wav` SHA `B0234598B2DC11635A8713C076A0F6C7E697F29FCA21813EA68922AD38D91C7A`; use as an idle-entry one-shot unless a future seam audit approves looping.
- Death: Julie Damsgaard / Spring Spring / Spring Enterprises, [Various Sound Effects](https://opengameart.org/content/various-sound-effects-0), original SHA `9216E8A1E252765392CB30637489F8E58831280B1139FA5E2E916B79E375C916`, derived `alien_infantry_death.wav` SHA `AFFCE4695B4B493BD2611E591EFA39931BBFAE19E0079D9C77DA5B71D201263B`; bind at death onset.

Exact synchronization frames remain blocked until accepted actions exist. Selection and acknowledgement voices remain intentionally unwired because installed `TAG_infantry_*` consumers are country/original-tag-wide; replacing them would also replace global ordinary-infantry voices.

## Counter handoff

The owning subunit uses `sprite = alien_infantry`, hence exact entity `alien_infantry_entity`. Required original counter consumers are `GFX_unit_alien_infantry_icon_medium` -> `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds` and `GFX_unit_alien_infantry_icon_medium_white` -> `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds`.

Installed precedents are `interface/subuniticons.gfx:46` and `:199`, backed by `unit_infantry_icon.dds` at 152x42 with two 76x42 frames and `onmap_unit_infantry_icon.dds` at 60x12 with two 30x12 frames. Both have real alpha and two left-to-right normal/state frames. The large green family includes RGB `73,106,73` and `74,107,74`. Matching skill-local families are `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `map_counters/`.

The icon tranche completed both original alien-head/laser-rifle counters and installed their two-frame DDS files at the required paths. `interface/alien_infantry_system.gfx` registers the large and on-map consumers. The completed processing, round-trip, palette, alpha, and contact-sheet evidence is recorded in `docs/assets/016_brilliant_scientist/dhrondan_icon_package/manifest.md` and `016_dhrondan_icon_asset_completion_handoff_2026-08-21.md`. No placeholder or reused vanilla counter was installed; live display acceptance remains user-owned.

## Files and evidence

- Job manifest: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/manifest.md`.
- Rejection evidence: `validation/generation_rejection.json`.
- Blender report: `blender/reports/alien_infantry_candidate_prepare.json`.
- Contact sheet: `blender/previews/alien_infantry_candidate_contact_sheet.jpg`, SHA `C7B1DCC89C298DFAAE21A9880268853320C3C706454C83047FA436A5CB30DD05`.
- Source manifest: `refs/original/input_manifest.json`.
- Provider history: `history.jsonl`; request/response/credit/task receipts under `provider/`.
- Runtime crosswalk: `runtime/crosswalk.md`.
- Runtime handoff: `runtime/handoff.md`.
- Sound provenance and handoff: `evidence/audio/provenance/audio_sources.json`, `runtime/sound_handoff.md`.
- Historical counter brief: `runtime/counter_handoff.md`; superseded completion evidence is in `docs/assets/016_brilliant_scientist/dhrondan_icon_package/manifest.md`.

## Blocker and next authorization

One additional Meshy 7 image-to-3D generation from a rifle-silhouette-preserving cleanup is the proposed recovery, estimated at 30 extra credits. It is failure-driven and has not been launched. User confirmation is required before that spend. Until an accepted rifle-bearing candidate completes rigging, all seven actions, PDX export/reimport, sound synchronization, and parent runtime wiring, this package must remain incomplete.

On 2026-08-22, a read-only provider recheck confirmed task `01a02497-1fb9-7a1b-bec6-ec388d54a016` remains `SUCCEEDED` and consumed 30 credits. The live account balance was 626 credits. A technically successful but rejected task is not refunded, and the verified provider exposes no free retry or correction operation that can restore the missing rifle. No paid operation was started during this recheck.

No gameplay unit stats, API/contact logic, DHR country files, focus files, global infantry voices, or live consumers were edited by the model worker. The parent later committed the reviewed blocked evidence package with the rest of the asset and audit documentation.
