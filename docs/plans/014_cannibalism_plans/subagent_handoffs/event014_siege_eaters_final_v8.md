# Event 014 Siege Eaters 3D final v8 handoff

> Historical blocked handoff. Superseded by the accepted installed Siege Eaters runtime receipt; retain this file for provider failure evidence only.

Status: `blocked` after parent visual approval because the locked Meshy 7 request returned HTTP 402 at insufficient balance.

## Approved reference

The parent approved this exact single Meshy input on 2026-08-24:

- Final input: `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/refs/original/meshy_input.png`
- SHA-256: `1AC18B9B008CCCC70BC0AF30605CA72ADCC9030A1C233732559400C9A6744F75`
- Comparison: `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/refs/source/recovery_v8/source_to_refinement_comparison.png`
- Comparison SHA-256: `CDE376E9703D4A4E5DF993048F7BAD0F9CF339830BB8D5A7B5176C411600A25B`

Approval statement: `APPROVED exact SHA256 1AC18B9B008CCCC70BC0AF30605CA72ADCC9030A1C233732559400C9A6744F75.`

The locked Meshy 7 request used this exact file path but returned HTTP 402 before task creation. It generated no provider artifact and consumed no credits.

## Source and rights

- Source image: https://imgcdn.gamefound.com/richtextimage/richtext/320075a9-c6d1-4ff2-ac13-d99e6a875f59.jpg
- Official campaign page: https://gamefound.com/en/projects/chip-theory-games/the-elder-scrolls
- Publisher terms: https://chiptheorygames.com/policies/terms-of-service
- Publisher/project owner: Chip Theory Games; individual artist unresolved.
- Retrieval date: 2026-08-24.
- Archived source SHA-256: `59342677E01A84D57A097FE464D5CC4A101569894B4DA7BF9FF2267363E09D7F`.
- Rights mode: `reference_only_user_authorized`. No reuse license was stated. No explicit NoAI, no-derivatives, or equivalent prohibition was found on the reviewed official pages. Source bytes are non-shipping evidence and will not become runtime art.
- Uncertainty: the static campaign HTML snapshot did not expose the direct-image UUID; the association uses the parent's named official lead and the official Gamefound/Chip Theory context.
- Detailed evidence: `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/refs/source/recovery_v8/provenance.json` and `source_search.md`.

## Refinement and alpha result

Native ImageGen preserved the living warrior's anatomy, proportions, pose, horned skull headdress, bone-and-leather armor, footwear, spikes, exact massive two-handed mace, and overhead two-hand grip. It isolated and cleaned the figure and added culturally neutral charcoal-black and muted iron-red fictional siege paint plus restrained dried blood, dust, and grime. Plate-knight armor, undead anatomy, Indigenous or sacred motifs, modern tactical equipment, firearms, extra figures or limbs, changed grip, text, and gore were prohibited.

ImageGen produced an RGB checkerboard twice, including the targeted alpha-repair pass. U2Net and ISNet alternatives were rejected for matte damage, halos, or checker fringe. The selected documented fallback keys only border-connected near-neutral checker pixels and decontaminates the soft edge from neighboring subject colors. Final validation: 1055x1491 RGBA, alpha 0-255, four transparent corners, one visible component, foreground bbox `[194, 17, 952, 1408]`, complete mace/body/feet, and preserved internal negative spaces.

## Provider attempt and locked continuation

- Meshy route: official `@meshy-ai/meshy-mcp-server` 0.4.0; SDK 1.29.0; exact model identifier `meshy-7` under locked compatibility `meshy-7-v4`.
- Blender HOI4 adapter: `chaosx_blender_hoi4` 1.10.0.
- Blender: 5.1.2, build `ec6e62d40fa9`.
- io_pdx_mesh: 0.91.0, locked SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Environment verifier found no dependency findings. Its transient Meshy wrapper child was cleared by the shared pipeline process before live schema/balance evidence; no substitute route is permitted.
- Pre-attempt balance: 25 credits. The generation estimate is 30 credits. The exact compliant call returned `HTTP 402 Insufficient funds`; post-attempt balance remained 25, task ID and response ID were absent, and consumed credits were zero.
- A later shared-account balance recheck returned 20 credits. This occurred after the failed call and is not attributed to this package; current shortfall against the 56-credit minimum is 36.
- Minimum complete v8 provider tranche: 30 generation + 5 rig + 21 for seven custom actions = 56 credits. Observed shortfall: 31 credits. The rig-included walking source covers `move`; the other seven roles require distinct custom provider calls.
- Evidence: `provider/requests/v8_001_meshy_image_to_3d.json`, `provider/responses/v8_001_meshy_image_to_3d.json`, and `provider/credits/v8_001_meshy_image_to_3d.json`.
- Vanilla scale precedent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`, source height 7.351824797689915, entity scale 0.8, effective runtime height 5.881459838151932, forward `-Y`, up `+Z`.
- Required genuine provider-sourced actions: idle, move, attack, defend, support_attack, retreat, training, death. Local replacement or semantic alias motion is forbidden.
- Required sourced 44.1 kHz sound roles: selection, movement, idle vocal, maul swing, heavy impact, training, death.
- Required outputs after approval: provider downloads and checksums, protected Blender source, normalized/triangulated HOI4 mesh, PDX DDS material set, eight exported and reimported `.anim` files, action/contact/loop evidence, previews, manifests, sourced-audio evidence and sync map, and runtime/GFX/sound handoff. Runtime wiring remains parent-owned.

## Counter consumer handoff

The bespoke vanilla-green counter is reused only through the existing completed art handoff at `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_counter_art_handoff.md`:

- `GFX_unit_cannibal_siege_eaters_icon_medium`
- `GFX_unit_cannibal_siege_eaters_icon_medium_white`
- `GFX_unit_cannibal_siege_eaters_icon_small`

No counter pixels or runtime/GFX definitions are edited in this package.

## Sourced sound package

All seven requested sound roles now have sourced PCM s16le 44100 Hz mono candidates. Existing selection, movement, idle vocal, maul swing, heavy impact, and death candidates were retained with their archived source pages and hashes. The missing training role was mechanically derived from the public-domain Wikimedia/PDSounds `Male Pain Grunts` recording by stilgar: trim 21.12034-24.402948 seconds, high-pass 90 Hz, low-pass 9000 Hz, loudness normalization, fades, mono conversion, and 44100 Hz resampling.

- Training path: `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/audio/derived/cannibal_siege_eaters_training.wav`.
- Training SHA-256: `2FB04BFA3652E87056631845766FA3D5FC11808DF4834C8C48102A38B0655290`.
- Training duration/format: 3.282608 seconds, PCM s16le, 44100 Hz, mono.
- Full source/license/transformation ledger: `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/evidence/audio_sources/sound_design_v8.json`.
- Exact action-frame synchronization remains pending genuine v8 provider actions and is not guessed.

## Current blockers and remaining parent work

- Provider balance is insufficient: the latest recheck is 20 available versus 56 minimum for the compliant generation, rig, and seven custom-action tranche.
- Meshy generation, rigging, provider actions, Blender processing/export/reimport, and model texture conversion have not begun for the v8 lineage.
- Audio source selection and 44.1 kHz conversion are prepared, but exact frame synchronization remains blocked with the animations.
- The package is not runtime-wired and no in-game completion is claimed.
