# Event 012 elephant model handoff

Status: `superseded_by_vanilla_elephantry_reuse`.

The user explicitly directed the parent to reuse the installed vanilla elephantry model for the Event 012 elephant formation. No custom Meshy 7 generation, rigging, animation, export, sound, or counter promotion is required for this unit.

Asset: `chaosx_elephants` / `elephant_shared_base` (historical evidence only).

Active runtime consumer: `chaosx_elephant` with `sprite = elephantry`; no custom entity override.

Evidence root: `docs/assets/012_africa/models_3d/elephant_shared_base`.

## Outcome

No replacement model was generated. A complete named one-rider war-elephant source was selected, and the explicitly authorized local transparency fallback produced one reviewed RGBA candidate pending parent comparison approval, while the action-source gate remains independently blocked.

The restarted search selected The Printing Goes Ever On's *Harad - Desert Warriors, Eastern Men War Elephant* commercial miniature render under explicit `reference_only_user_authorized` permission. Its third gallery view has one rider, complete four-legged anatomy, visible tail/trunk/tusks, and a reinforced woven-wood mounted platform/harness. Source bytes were transient only; SHA-256 fingerprint `75A21D4EC74DAEC8CF6E8A1857ACC79A9B5E26A12A1383BE29F8F667018A3704`. Faithful ImageGen cleanup preserved the visible subject and removed the base, but baked an opaque checkerboard (`ABA2C992...1EAA7D`, `rgb24`). The authorized transparency-only repair baked opaque white (`3344302C...D893E`, `rgb24`). The parent then authorized `rembg 2.0.61` plus deterministic alpha remapping. The stronger white-background cleanup supplied unchanged RGB while U2Net supplied only the mask; the resulting grayscale RGBA `6D71BE515210AA1A78949D822ECF38BA4814755FE8CD83C4302BC5810B28447E` passed alpha and component review, then moved to `refs/derived/` when the later color gate superseded it. No image has been submitted to Meshy.

The source and cleanup pass the new period-appropriateness gate for this deliberately archaic 1936–45-world unit. They show elephant hide, textiles, rope/fibre bindings, woven/bundled wooden construction, tusk apparatus, and non-modern rider equipment, with no electronics, advanced optics, plastics, contemporary tactical gear, powered machinery, or science-fiction parts. ImageGen did not periodize the source, and the final fallback changed alpha only.

The later color gate rejected monochrome as a Meshy input. The grayscale RGBA was preserved at `refs/derived/meshy_input_grayscale_pre_color_gate.png`, and one native ImageGen edit faithfully applied natural gray-brown hide, ivory, weathered wood, fibre, leather, muted period textiles, and period rider colors. The direct ImageGen RGB `1C00B8B0AF180217775DF1C412FF30A13B891A044EBF974527BADCB261AA0BE2` baked a checkerboard, so the authorized `rembg 2.0.61`/U2Net mask and deterministic alpha remap were applied without changing its RGB. The final `refs/original/meshy_input.png` is 1380x1140 RGBA, SHA-256 `78A04549F24C4C1E5E510BEEAD8932D89F402CC8E0B64A17DCCD7E8CBF9AA702`. Side-by-side, normalized-bound, subject-coverage, color-variation, material-separation, dark/light/checker, component, and period reviews pass.

Parent visual review approved that exact SHA-256 on 2026-08-24. Approval covers the dedicated colorization edit, coherent natural and medieval/fantasy palette, 1936–45 alternate-history period gate, exact elephant/rider/howdah fidelity, all named components, material separation, and repaired alpha. The approved bytes are locked as the sole Meshy input. No Meshy call was made because submission remains explicitly paused and the action-source route is independently blocked.

Current official Meshy API documentation still states that programmatic rigging is unsuitable for nonhumanoid assets. The current repository schema lock requires `rig_task_id` plus `action_id` for `meshy_animate`, while `meshy_rig` accepts only `input_task_id` or `model_url` and exposes no local custom-rig upload. The exact 17-bone elephant map remains recorded in `job.yaml`, but the local rig can only prepare a skeleton and cannot mint the provider rig task required for substantive Meshy animation. No professional quadruped source has user approval. All eleven roles—`idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, `death`, `deploy`, `supply_load`, and `impact`—remain blocked; no alias, humanoid rig, local motion, or static substitute was used.

Fresh Blender scale remeasurement was not performed because the global provider/Blender route was explicitly paused. The surviving numeric crosswalk remains documented but pending fresh measurement: rider source height `7.3518242835`, entity scale `0.8`, rider effective height `5.8814594268`, provider target height `33.5147094727`, and elephant effective height `26.81176757816`. The recorded dedicated preparation rig has 17 bones: `root`, `body`, `neck`, `head`, `trunk_01`, `trunk_02`, `tail`, four upper/lower leg pairs, `howdah`, and `rider`.

## Files changed or created

- `docs/assets/012_africa/models_3d/elephant_shared_base/job.yaml`
- `docs/assets/012_africa/models_3d/elephant_shared_base/manifest.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/history.jsonl`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/source/source_search.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/source/provenance.json`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/source/faithful_cleanup_prompt.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/source/source_to_cleanup_comparison.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/source/local_transparency_processing.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/source/faithful_colorization_prompt.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/source/source_to_colorization_comparison.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/derived/faithful_cleanup_opaque_white.png`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/derived/meshy_input_grayscale_pre_color_gate.png`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/derived/faithful_colorization_opaque_checker.png`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/derived/faithful_colorization_rgba_candidate.png`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/original/meshy_input.png`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/original/input_manifest.json`
- `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/reference_cleanup/` — raw U2Net mask, alpha validation receipt, and dark/light/checker review images
- `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/reference_colorization/` — prompt-linked color/alpha validation, raw mask, comparison sheet, and dark/light/checker reviews
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/source/candidates/` — archived CC0 package, exact TIF, and review decodes
- `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/action_source_feasibility.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/dependency_and_route_preflight.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/audio_revalidation_2026-08-24.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/audio/original/` — three immutable sourced originals
- `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/counter_revalidation_2026-08-24.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/counters/` — read-only runtime/vanilla/skill decodes
- `docs/assets/012_africa/models_3d/elephant_shared_base/runtime/handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_meshy7_redo.md`

No runtime, gameplay, GFX, entity, sound-definition, localisation, spreadsheet, or other asset file was edited.

## Provider and dependency evidence

- Paid Meshy calls: `0`; submitted estimated credits: `0`; observed consumed credits: `0`; no task ID or response ID exists.
- No Meshy wrapper, tools-list, balance, provider, Blender, or adapter call was made in this tranche.
- Dependency lock SHA-256: `C420C7EB701EA1C29F6195B6CE515B52B36EEA6B9AA5910D21254B8702A11495`.
- Schema lock SHA-256: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`, revision `meshy-7-compat-live-declaration-2026-08-21`.
- Locked official Meshy MCP: `@meshy-ai/meshy-mcp-server` `0.4.0`, git `d8c77d1cb897e345eb41d38b510b8391b1664346`, compatibility revision `meshy-7-v4`, verified model `meshy-7`.
- Blender HOI4 adapter lock version: `1.8.2`.
- Blender lock line: `5.1.2`, build `ec6e62d40fa9`.
- `io_pdx_mesh`: `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.

These are repository-lock observations, not a new live route verification.

## Audio result

All three immutable originals were reconstructed from defensible source pages and exactly reproduce the historical hashes:

- public-domain `Dull Thud` by gregoryweir: `5B91906D41BD57F1F6551E446D30FBFF06EC59A39D22725140293EF4AEC6CDB3`.
- CC0 `Elephant voice - trumpeting` by தகவலுழவன்: `E5F3120E5EACA87CC080BBF57BD185C96D52FD0F63CC1DFE33228C8BFA29F3BC`.
- public-domain `Squeaky door` by leonmire: `B60B97C3F73C9754FC36B58CEA4862D50FF800F12632C9B55BC6F8132E93D9C5`.

The six existing runtime WAVs were preserved and re-probed as PCM s16le, 48 kHz mono. Their exact hashes, source URLs, attribution, licenses, content checks, and current synchronization points are in `evidence/audio_revalidation_2026-08-24.md`. The missing historical trim/fade/gain recipes prevent a complete transformation reconstruction for every derivative. The CC0 trumpet/idle derivative is a defensible selection one-shot candidate, but the mandatory selection role remains blocked at binding: installed land-unit selection is country/original-tag voice routing, no verified per-subunit selection hook was found, and this shared body is consumed across host/member formations. Entity idle is not selection.

## Counter result

The exact installed definition `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, vanilla large/small infantry DDS files, and skill-local large/small reference family were re-inspected. Existing runtime candidates remain:

- `unit_elephant_shared_base_icon`, 152x42/two frames, SHA-256 `5D455DC3268BE89451D967E187FD5AAA8D6966C9A82FF8AE933208DF2201A21E`.
- `onmap_unit_elephant_shared_base_icon`, 60x12/two frames, SHA-256 `6E2AC8B322F4FE1D6D126E1B02727BE721B83FD4EEC5788D6B9D0AB083188BDD`.

Decoded comparison confirms a bespoke elephant silhouette, real alpha, olive-green large treatment, grayscale small treatment, and correct frame/canvas behavior. However, the deleted source PNG, processed PNG, prompt/source-mode record, icon-artist handoff, and original comparison sheet were not recoverable from Git. The counters are revalidated runtime candidates, not a complete production-lineage package. No 2D authoring was performed.

## Geometry, material, rig, action, export, and synchronization status

- Geometry: not generated; historical runtime mesh remains unverifiable.
- Materials/textures: not processed; historical runtime DDS files remain unverifiable.
- Rig/weights: not created or audited; 17-bone map is preparation-only.
- Actions: all eleven blocked; six historical files remain unverifiable, five required distinct roles are absent, and current runtime aliases are forbidden.
- `.mesh`/`.anim` export and reimport: not run.
- Selected input-to-runtime hashes: final colored input `78A04549F24C4C1E5E510BEEAD8932D89F402CC8E0B64A17DCCD7E8CBF9AA702`; no runtime synchronization or provider lineage exists.
- Runtime synchronization: not run; runtime root remained read-only.
- In-game validation: not claimed and remains parent-owned.

## Meaningful validation and skipped validation

Performed: official API/schema contract comparison, reusable-source license/identity review, faithful-cleanup component comparison, dedicated colorization comparison, normalized-bound and subject-coverage comparison, quantitative color-variation check, material-boundary and period review, exact post-alpha RGB-preservation check, RGBA/alpha/corner/bbox validation, dark/light/checker alpha review, immutable audio-source hash reproduction, runtime WAV format probes and bounded source-content comparisons, exact installed vanilla counter definition/DDS inspection, skill-reference inspection, DDS dimension/frame/hash checks, alpha/palette analysis, and visual decoded counter review.

Skipped because blocked or explicitly paused: parent comparison approval, live Meshy 7 schema/balance/provider work, fresh Blender scale measurement, geometry QA, material conversion, rig/weight review, action processing, phase/contact validation, PDX export/reimport, source-to-runtime copying, and in-game consumer validation.

## Remaining parent decisions

1. Preserve the parent-approved exact `refs/original/meshy_input.png` bytes; any revision invalidates approval and requires a new comparison gate.
2. Wait for an approved Meshy/API quadruped rig route that returns a usable `rig_task_id`, or explicitly approve a named licensed professional elephant/quadruped animation source covering all eleven roles.
3. Resolve the mandatory selection consumer without affecting ordinary infantry unintentionally.
4. Decide whether the existing counter candidates require a fresh `chaosx_icon_artist` production pass to restore complete lineage.

Simplifications: none. The package is incomplete and explicitly blocked rather than completed with aliases, humanoid motion, local authoring, source redesign, or unverifiable historical outputs.
