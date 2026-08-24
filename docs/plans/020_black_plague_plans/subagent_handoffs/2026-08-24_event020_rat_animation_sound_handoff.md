# Event 020 shared plague-rat animation and sound handoff

Date: 2026-08-24
Owner: `020_black_plague`
Asset slug: `rat_ground_unit_shared`
Job root: `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/`
Overall status: **animation incomplete / blocked; licensed audio installed**

## Free-only continuation update

The user subsequently prohibited every paid package, purchase, trial, demo, marketplace spend, Meshy spend, and transaction. The paid-source recommendation later in this historical handoff is therefore superseded and must not be acted on.

Quaternius Ultimate Animated Animal Pack `Fox.fbx` was acquired from the official zero-cost CC0 source and eight distinct source-skeleton actions were exported at 24 FPS, but every Fox-to-old-rig and Fox-rig direct binding was visually rejected. The retained source actions remain evidence only.

Danimal's CC BY-SA 4.0 rat was then audited as a rat-native rig bridge. Adapter 1.9.2 successfully rendered `Skeleton.001` with direct `Head.000` and `Body.000` consumers, but exact same-frame PNG hashes show the named action selections resolving to shared master-timeline phases rather than eight independently demonstrated clips. The required four-nearest Danimal-rig plus approved-Meshy-geometry request `96b5e03282b746aa931e9b3f72f58331` failed before mutation because the locked `prepare_candidate` operation rejects `.blend` sources. Native Walk could not reach the Meshy geometry gate, so a mixed Danimal-native plus Quaternius-missing-role route could not proceed.

The authoritative continuation evidence is `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/evidence/free_animation_sources/danimal_action_audit.md`, with the concise parent handoff at `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-24_event020_danimal_rat_free_route_blocker.md`. No runtime animation file was changed. The ten accepted audio derivatives were subsequently installed and wired.

## Outcome

The shared rat does **not** have a proper final animation package. The five installed `.anim` files are readable at 24 FPS, but their provider/professional lineage is unverifiable, their sampled deformation is extremely small, the death clip does not show a defensible articulated collapse in bounds evidence, and the entity fills three required roles with forbidden aliases: `defend` and `support_attack` reuse attack, while `training` reuses idle. None may be accepted or relabeled as final source motion.

The locked live Meshy route still cannot produce primary quadruped-rat motion. Its rig endpoint is the character/humanoid flow and `meshy_animate` accepts only `rig_task_id`, integer `action_id`, and optional post-processing. It exposes no animal/custom-skeleton rig, quadruped action family, semantic rat action request, or custom source-clip upload. All eight required dedicated actions therefore remain blocked until the user explicitly approves a compatible professional source.

A source-only sound package was produced independently. Four licensed originals and ten signed 16-bit PCM, 44.1 kHz mono mechanical derivatives are preserved with source pages, direct URLs, attribution, licenses, transforms, checksums, and ffprobe evidence. They are candidates only: no sound definition, entity state, GFX, or gameplay file was edited. The bamboo-rat calls are authentic but not the intended rat species; the gravel movement and cat-eating bite sources are generic substitutes and require explicit review. The two loop candidates have not passed a seamless-loop listening test.

## Gates, dependencies, route, and credits

The first process check verified that `MESHY_API_KEY` was nonblank before repository or job intake; its value was never printed or stored. The repository lock gate and `python .tools/3d_pipeline/verify_environment.py --probe-meshy` passed. An immutable copy of the final probe report is `evidence/dependencies/environment_report_probe_meshy.json`, SHA-256 `B52570A0BE524375B652DD9FB277A1374CD958BF399E46D99B8C2865BBFFBB8D`.

| Dependency | Verified value |
|---|---|
| Official Meshy MCP | `@meshy-ai/meshy-mcp-server` `0.4.0`, git `d8c77d...` |
| Meshy SDK | `1.29.0`, git `e12c...` |
| Image-to-3D model | exact `meshy-7`; no alias or downgrade |
| Blender | `5.1.2`, build `ec6e62d40fa9` |
| Blender adapter | `chaosx_blender_hoi4` `1.8.2` |
| io_pdx_mesh | `0.91.0`; locked archive checksum begins `A683` and ends `F7C2` |
| Dependency lock SHA-256 | `C420C7EB701EA1C29F6195B6CE515B52B36EEA6B9AA5910D21254B8702A11495` |
| Meshy schema lock SHA-256 | `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233` |
| Adapter config SHA-256 | `71B138604D875AF041E13715F82336CA4D9148AB41799B2AABE7669BEDBE0FA2` |

The Blender socket at `127.0.0.1:9876` was separately listening. Adapter health request `962370eb83094f4ea9c15dbc693f3530` passed and loaded the locked Blender and extension.

The first observed live balance during this pass was 719 credits. A later independently preserved probe observed 684 credits after concurrent repository work; no paid call in this job explains that difference. This job made zero paid calls, created no provider task/response IDs, estimated zero credits, and consumed zero credits. No new geometry call was attempted because geometry generation cannot fix the missing primary-motion route.

## Geometry, material, scale, rig, and weights

The installed mesh was copied byte-for-byte to `evidence/runtime_snapshot/black_plague_rat.mesh`, SHA-256 `52C4C6B5E4EB41D6726DDD5EA7271E8FD486C1136B5F4CF7E496E3FED639EBA4`, and kept immutable. Locked reimport request `2a0047972045416f87685cff49ed50c0` created `blender/checkpoints/reimport_runtime_snapshot_reimport.blend` plus seven preview views. Scene inspection request `d3acf30f35a8479db431759cc8ec5e42` recorded identity transforms, one armature modifier, 17 vertex groups, and normalized one-bone weights for all 32,909 vertices with no zero-weight vertex.

Measured source bounds are `12.5761909485 × 14.3501110077 × 7.3518247604`, minimum `[-6.2977471352, -7.1680397987, 0]`, maximum `[6.2784438133, 7.1820716858, 7.3518247604]`. The entity applies scale `1.35` exactly once, yielding effective runtime dimensions `16.9778577805 × 19.3726498604 × 9.9249634266`. Against the named vanilla source `western_european_infantry.mesh` height `7.3518242835` and `infantry_rifle_entity` scale `0.8`, effective height `5.8814594268`, the rat is `1.6875001095×` vanilla infantry height. Axes are `-Y` forward and `+Z` up; source ground contact is `Z=0`; root and actions are intended in place.

The mesh has 29,999 triangles, 32,909 seam vertices, 15,012 position-welded vertices, zero degenerate faces, zero non-manifold edges, and 101 position-welded boundary edges. PDX packed diffuse/specular/normal material connections exist. Texture lookup warnings in the audit proof are expected because the byte-identical runtime texture files were not duplicated beside the audit-only mesh; the installed runtime files were not mutated.

The 17-bone custom quadruped map is documented in `blender/rig_map.md`: `root`, `body`, `neck`, `head`, `trunk_01`, `trunk_02`, `tail`, four upper/lower limb pairs, plus inherited auxiliary bones `howdah` and `rider`. Those two names are semantic anomalies; no howdah, rider, armor, second creature, or corresponding geometry is authorized. They must remain inert compatibility bones unless an approved source proves a necessary mapping. Any skeleton change invalidates all action/export approvals.

Three non-paid adapter preparation attempts failed and are retained as evidence rather than hidden: `8f13a7694b594f3f82677315e3289282` rejected a source outside the job-relative contract, `e202aae5d49b4494bf4430389106b983` rejected an absolute vanilla-reference path, and `d44b8afa631f4697ba565cc49c877656` confirmed that a runtime `.mesh` is not a provider candidate input. The read-only reimport route was then used successfully.

## Installed action results

| Role | Runtime SHA-256 | Frames / adapter request | Result |
|---|---|---|---|
| idle | `894A84BD75294AE56F245885E76AD034C3687F8100DBA564F0821D6B98821B9C` | 1–49 / `eea9d08459b64e7993fea174f1bba962` | Readable loop, minute bounds change, no accepted source lineage. |
| move | `F53FA3DE5D12000988DD61EE2DC2DC5491B4D6B56CF1E2237B386976E54BA5CF` | 1–25 / `5423dcb5f26448309f808b474081d0e2` | Readable loop, sampled Y change only about 0.0016 source units, no accepted source lineage. |
| attack | `BFF4D999BF778B6B5CE802C15754D600815F864A61A312548BD87B900F90AE82` | 1–33 / `da7443e10e15434986828c2d93b395d9` | Returns to neutral; no defensible wind-up/lunge/contact/recovery lineage. |
| retreat | `CB4DC54FC89D7CB20E1481FFD3337950AC4D42F66AF8D49A8AD7B780A6C22529` | 1–25 / `e603feb79299453f810f93c08c0a6e68` | Phase-reversed minute movement; no accepted source lineage. |
| death | `95195F3BFADB2E796F354EADDAADBD585C53258D6D6F94D8387EEF98FF3C4601` | 1–37 / `c551f68d73094c57b7b909f351c9a6b3` | Ground drifts to `-0.0081567` while height is effectively unchanged; no articulated collapse proof. |
| defend | none | entity alias to attack | Forbidden; blocked. |
| support_attack | none | entity alias to attack | Forbidden; blocked. |
| training | none | entity alias to idle | Forbidden; blocked. |

The five proof blends and 75 action previews are under `blender/checkpoints/` and `blender/previews/`. They prove static import and temporal sampling only. No `.anim` replacement was exported and every runtime byte remains unchanged.

## Professional source approval shortlist

No source was acquired or used. Full URLs, licensing, coverage, access, cost, and retargeting risks are in `evidence/professional_animation_candidates.md`.

1. `Rat` by RifatBilalov on Fab advertises 74 in-place/root-motion rat clips and FBX, including multiple attacks, death, idles, directional movement, hits, turns, hide, sleep, and more. Fab Standard License permits modification and embedded commercial use with a source-format tier; the public price was not exposed. This is the strongest candidate, but dedicated defend/support/training/retreat semantic mapping and skeleton compatibility require post-acquisition proof.
2. `PSX Animals: Rats` by MCSTEEG is USD 2, commercially licensed with a no-redistribution restriction, and includes a Blender file with two idle, run, attack, and death. It cannot cover all eight roles without forbidden reuse.
3. `Animal Pack Deluxe` by janpec is listed at USD 5 under the Unity Asset Store model; it advertises rat idle/eat/walk/run/attack/die families. It also lacks enough distinct roles until source files and skeleton are inspected.

The recommended user-approval request is the Fab Rat source, conditioned on confirmation of a source-format license tier and displayed regional price. Approval would authorize inspection/retargeting, not automatic acceptance.

## Audio sources, derivatives, and proposed runtime map

All originals were downloaded on 2026-08-24 and preserved under `evidence/audio/originals/`:

| Source | Attribution/license | Original SHA-256 | Derived roles |
|---|---|---|---|
| [Bamboo Rat calls — Commons](https://commons.wikimedia.org/wiki/File:Bamboo_Rat_(Dactylomys_dactylinus)_(W_DACTYLOMYS_DACTYLINUS_R1_C1).ogg), [direct](https://upload.wikimedia.org/wikipedia/commons/8/8a/Bamboo_Rat_%28Dactylomys_dactylinus%29_%28W_DACTYLOMYS_DACTYLINUS_R1_C1%29.ogg) | British Library Board; Richard Ranft; CC BY 4.0; shelfmark W1CDR0001419 BD20 | `F3FE77A46115BECBC5761315D4A993DFBF5303D6285A8CACF998948A9C00D946` | selection, acknowledgement, idle ambience, attack, retreat, training, death vocals |
| [Dull thud — Commons](https://commons.wikimedia.org/wiki/File:Dull_thud.ogg), [direct](https://upload.wikimedia.org/wikipedia/commons/5/5b/Dull_thud.ogg) | gregoryweir; public-domain dedication | `5B91906D41BD57F1F6551E446D30FBFF06EC59A39D22725140293EF4AEC6CDB3` | impact/contact |
| [Walking on gravel — Commons](https://commons.wikimedia.org/wiki/File:Walking-on-gravel-38827.ogg), [direct](https://upload.wikimedia.org/wikipedia/commons/9/93/Walking-on-gravel-38827.ogg) | uploaded by Fdsfds2.0 from Pixabay; author absent; CC0 1.0 | `14990DE1FD15418B55A2C939B0A99348446E613C1C4A5A307E49A87D228DE5EF` | movement/scurry candidate; generic-source review required |
| [Cat eating noisily — Commons](https://commons.wikimedia.org/wiki/File:Cat_eating_noisily.ogg), [direct](https://upload.wikimedia.org/wikipedia/commons/6/62/Cat_eating_noisily.ogg) | admin_phpbb; public domain | `B96EE393ADAB3A45832B0BE54C3CB0726F7317EC52F203ED18AE2B1B30D4B955` | wet bite candidate; wrong-animal review required |

Every derivative re-probes as `pcm_s16le`, `s16`, 44,100 Hz, mono. Exact trims, fades, normalization, durations, hashes, and original ffprobe receipts are in `evidence/audio/derivation_and_ffprobe.md`. The ten derivative hashes are recorded in that file and the job manifest.

The ten derivatives are installed under `sound/020_black_plague/rat_units/`. `sound/020_black_plague_rat_units_sound.asset` defines the RTA/RTX voice surfaces and the eight spatial action cues consumed by `gfx/entities/020_black_plague_rat.asset`.

Nominal 24 FPS synchronization is fully tabulated in `evidence/audio/runtime_sync_map.md`: attack bite/contact frame 17 (`0.667 s`), death impact frame 28 (`1.125 s`), opening vocals at frame 1, and loops across the full action ranges. These times remain blocked from final acceptance because the corresponding installed actions are rejected.

Installed voice precedents establish five tag-wide infantry names: `<TAG>_infantry_idle`, `<TAG>_infantry_move_out`, `<TAG>_infantry_neutral_combat`, `<TAG>_infantry_positive_combat`, and `<TAG>_infantry_retreat`. Parent wiring must define the applicable RTA and RTX pairs, including exactly `RTA_infantry_idle` and `RTX_infantry_idle`. This is tag-wide selection/order routing, not per-subunit routing. All five rat templates and six rat subunits are intended consumers, but future ordinary infantry under RTA/RTX would also receive these voices.

## Counter audit

`interface/chaosx_subuniticons.gfx` correctly registers `GFX_unit_black_plague_rat_shared_base_icon_medium`, `_medium_white`, and the two gameplay aliases with two frames. The large DDS is 152×42 / two 76×42 frames, SHA-256 `2D1DAC7276B58964D1D4656F1474B326C6DAA65BAB0194A4546F8225F5AB8E71`; the on-map DDS is 60×12 / two 30×12 frames, SHA-256 `FD14144EF07115B26BAE3434BAB03817228B586383D506BA154F5FD0152329E3`.

The exact installed references are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, `GFX_unit_infantry_icon_medium`, `GFX_unit_infantry_icon_medium_white`, `unit_infantry_icon.dds` SHA-256 `B33A8E3B69CC789EB0E31BA99F4E5BA4E5B0A8B51EC1A7A7F709C3516F720C23`, and `onmap_unit_infantry_icon.dds` SHA-256 `58AB78662C2A64A519B8D5D144582E7B2785915BD0A0A822696D87A9DE6F766C`. Matching skill-local reference families are `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `units/land/map_counters/`. Sampled large green anchors include `#496A49`, `#4A6B4A`, `#537253`, and `#648064`; frame 0 is normal green and frame 1 is the pale alternate.

The real blocker is unchanged: original source PNGs, processed frame PNGs, a package manifest, contact sheet, and DDS round-trip/comparison evidence are absent. The installed strips therefore remain review-gated even though their static dimensions and consumers are correct. A bounded `chaosx_icon_artist` recovery task was routed to `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-24_event020_rat_counter_handoff.md`; it is pending at the time of this core handoff. Runtime DDS and GFX were not changed.

## Files created

Core documentation:

- `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/rat_ground_unit_shared_model_job.yaml`
- `history.md`
- `manifest.md`
- `runtime/crosswalk.md`
- `blender/rig_map.md`
- `evidence/meshy_capability.md`
- `evidence/installed_action_audit.md`
- `evidence/professional_animation_candidates.md`
- `evidence/audio/source_search.md`
- `evidence/audio/provenance.md`
- `evidence/audio/derivation_and_ffprobe.md`
- `evidence/audio/runtime_sync_map.md`
- this handoff

Evidence/artifacts:

- immutable runtime mesh and five action copies under `evidence/runtime_snapshot/`
- four immutable audio originals and ten mechanical WAV candidates under `evidence/audio/`
- immutable vanilla mesh/entity copies under `blender/reference/`
- six locked reimport proof blends and all adapter request/result logs under `blender/checkpoints/` and `logs/adapter/`
- runtime and action preview PNGs under `blender/previews/`
- immutable probed dependency report under `evidence/dependencies/`

The worker phase did not edit gameplay or runtime files. The parent integration phase installed the ten WAV derivatives, added `sound/020_black_plague_rat_units_sound.asset`, registered the spatial effects in `sound/chaosx_sound.asset`, and synchronized the entity states in `gfx/entities/020_black_plague_rat.asset`. Runtime model, action, and counter files remain unchanged.

## Meaningful validation and remaining work

Performed: dependency/checksum/schema verification, free balance probes, independent Blender socket probe, adapter health, exact vanilla model/entity and voice precedent inspection, full XYZ scale crosswalk, mesh/rig/weight/material inspection, mesh and all five action reimports, temporal multi-view previews, licensed source-page/direct-URL review, original checksums, mechanical WAV derivation and ffprobe, exact RTA/RTX voice-template enumeration, and counter definition/dimension/hash/reference-family audit.

Skipped or incomplete:

- No paid Meshy operation: live schema lacks a compliant quadruped route.
- No professional animation import: the user has not approved a source.
- No final eight-action export/reimport: primary motion is blocked.
- The installed audio package passes file, format, definition, and entity-reference validation. Final perceptual playback remains user-owned live validation.
- No live HOI4 consumer, playback, or in-game scale validation: parent/user-owned and not claimed.
- Counter source/contact-sheet recovery was routed but is pending.

## Parent decisions and actions required

1. Continue only with genuinely free, source-format, mod-license-compatible animation packages. Do not purchase, trial, preview-rip, or spend provider credits.
2. Require a clean common-rig Walk bind with visible phase differences, intact anatomy, grounded contact, and the engine-compatible influence cap before processing all eight distinct roles.
3. Validate exact audio playback and synchronization during user-owned live testing after valid final actions exist.
4. Review the pending counter recovery output and only promote it if original-art, exact vanilla palette/state, round-trip, and comparison evidence pass.

There were no hidden fallbacks or silent simplifications. The package is explicitly incomplete because proper dedicated animation remains blocked and counter source evidence is pending. Licensed sound definitions and runtime entity cues are installed; their final timing remains provisional until accepted actions exist.
