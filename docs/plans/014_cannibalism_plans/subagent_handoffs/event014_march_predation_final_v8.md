# Event 014 March Predation Column 3D handoff — final v8

> Historical v8 adapter-boundary handoff. The current 1.10.14 export, grounded reimport, runtime wiring, and remaining provider-action caveat are recorded in `event014_cannibal_march_predation_column_runtime_wiring_2026-08-25.md` and the package manifest.

## Outcome

An eligible modern fictional source and bounded archer refinement are parent-approved and locked. Meshy 7 generation, provider rigging, and all eight distinct required provider actions succeeded and their immutable artifacts are archived. Blender export is blocked because adapter 1.10.2 reports calibrated scale during prepare but does not persist that scale coherently to the saved rigged mesh and armature.

The exact source is Alexander Chiveli Navarro's *Cannibal* Sketchfab render, explicitly based on Tooth Wu's *Cannibals - 1* concept. The source already supplies the requested human cannibal identity, red full-body paint, horned jaw mask, ragged fantasy armor, dual axes, and crazed full-body silhouette. The bounded ImageGen edit preserves that identity and replaces only the smaller second axe with a rough shortbow, adds a visible back quiver/arrows, and adds restrained culturally neutral bone trophies. The original large close axe remains.

The source image SHA-256 is `6A67762BA1868287F9E574AEEF713D6D0367FBE998627CC3B8F1420BC131213E`. The parent approved exact RGBA Meshy input SHA-256 `9523DBF13601E7AE8ACB3B58013700209D19BCA6C3866B8932FB6E8D18C91289` on 2026-08-24. Those exact bytes are promoted to the sole canonical `refs/original/meshy_input.png`; the pending duplicate was removed.

## Recovery v9 source and rights gate

- Primary source page: `https://sketchfab.com/3d-models/cannibal-7e26d839bd0e44619c724f32b75cab33`
- Primary source title/creator: *Cannibal* by Alexander Chiveli Navarro
- Underlying concept: Tooth Wu, *Cannibals - 1*, `https://www.artstation.com/artwork/baLZnn`
- Source mode: `reference_only_user_authorized`
- Exact Sketchfab API state: `license: {}`, `isDownloadable: false`; no model file was downloaded.
- Work-specific AI audit: the exact Sketchfab API tag list contains no `NoAI` tag, and the archived model HTML contains no `noai` or `noimageai` marker. Sketchfab Terms section 15 prohibits use as generative-AI input only for content actively marked NoAI.
- ArtStation audit: the indexed project record and targeted web searches expose no explicit NoAI marker for Tooth Wu's project. ArtStation Terms likewise attach the AI-input prohibition to content actively marked NoAI.
- Decision: no explicit NoAI, no-derivatives, or no-modification restriction was found for the exact works. The absence of a download license does not authorize model download; it remains all-rights-reserved source art used only under the parent's explicit reference-only authorization.
- Culture gate: pass. The design is a stylized invented horror-game humanoid; its jaw mask, red paint, armor, and weapons do not identify a living community, sacred motif, ceremonial object, or ethnographic context. Added bow/quiver/bone details contain no symbols.
- Source archive: `refs/source/recovery_v9/candidates/alexander_chiveli_cannibal_sketchfab_thumbnail.jpeg`
- Source manifest: `refs/source/recovery_v9/source_manifest.json`
- Archived page/API evidence: `refs/source/recovery_v9/pages/`
- Non-shipping status: all source pixels and page archives are evidence only.

## Recovery v9 approved refinement and alpha QA

- Exact approved input: `refs/original/meshy_input.png`
- Approved input SHA-256: `9523DBF13601E7AE8ACB3B58013700209D19BCA6C3866B8932FB6E8D18C91289`
- Exact prompts: `refs/briefs/imagegen_prompt_chiveli_v9.md`
- Opaque ImageGen result: `refs/derived/imagegen_cannibal_archer_opaque_checker_v9.png`, SHA-256 `17C5AC5AA2B254ADD2A5726BBF91853D74D79507713EA21BBDE0516D7CEDB199`
- Native alpha result: failed twice; both built-in ImageGen outputs were opaque 24-bit RGB with baked checkerboard and alpha 255 throughout.
- Fallback: checker-aware seeded foreground extraction in `evidence/process_checker_alpha_chiveli_v9.py`, with bounded pale-abdomen retention, fringe RGB decontamination, and narrow antialias.
- Source/final comparison: `refs/derived/chiveli_source_to_final_comparison_v9.png`
- Alpha metrics: 1672×941 RGBA; alpha 0–255; 1,339,159 transparent, 219,271 opaque, 14,922 partial pixels; visible bounds `[357, 28, 1276, 893]`.
- Black/white/checker proof: `refs/derived/meshy_input_alpha_black_v9.png`, `refs/derived/meshy_input_alpha_white_v9.png`, and `refs/derived/meshy_input_alpha_checker_v9.png`.
- Visual QA: full mask/horns, hair streamers, body, both arms/hands, both feet, large axe, complete bow and bowstring, back quiver/arrows, cloth, and bone trophies remain in frame. The body, paint, mask, ragged armor, close axe, and overall silhouette remain recognizably source-matched. No living-culture motifs, floor, base, shadow, extra person, text, or watermark remain.
- Approval state: `parent_approved_exact_sha_2026-08-24`.
- Parent finding: preserves the source design, reads as a distinct crazed cannibal archer, includes required bow/quiver/close axe/bone identity, and introduces no cultural motifs.

## Prior rejected Bestiarum lineage

The visually approved Bestiarum Games *Fleshmad Hunters | Man Eaters — Hunter 1* source is legally ineligible for ImageGen cleanup. The Network Cadre audit found that the archived Bestiarum Terms and Conditions, updated 2025-03-26, section 6 explicitly prohibit unauthorized reproduction, distribution, modification, or commercial use of content including promotional materials. Reference-only user authorization cannot override that explicit restriction.

The source at SHA-256 `9E0028B6458CFD4876D347A44EEBD0FB4B533DDF71F10ABA6B73E42D3F0F668F` and cleanup at SHA-256 `74253F5B89DB675D39F94AF7007358116FB21F30BAA0CF85572580FAC5308D10` are rejected non-shipping evidence. The rejected cleanup is preserved at `refs/derived/bestiarum_rejected_meshy_input_v8.png`; it must not be sent to Meshy.

## Prior Bestiarum terms reconciliation

- Archived terms: `refs/source/recovery_v8/pages/bestiarum_terms.html`
- Archived terms SHA-256: `DBD0D6E0EF582E82807A152C28F94633742026FF3ABBCCAA7EF57503C0134885`
- Relevant heading: `6. Intellectual Property`
- Relevant archived statement: unauthorized modification of Bestiarum content, expressly including promotional materials, is strictly prohibited.
- Decision: explicit incompatible restriction; reject despite prior visual approval and user reference-only authorization.
- Provenance record: `refs/source/provenance_bestiarum_v8.json`
- Rejected input record: `refs/original/input_manifest.json`

## Rejected refinement evidence

- Source page: `https://bestiarumgames.com/products/flesh-hunters-man-eaters-bestiarum-miniatures-d-d-wargaming-dnd`
- Title: *Fleshmad Hunters | Man Eaters — Hunter 1*
- Creator/publisher: Bestiarum Games / Bestiarum Studio LLC
- Source path: `refs/source/recovery_v8/candidates/bestiarum_fleshmad_hunter_1.jpg`
- Source SHA-256: `9E0028B6458CFD4876D347A44EEBD0FB4B533DDF71F10ABA6B73E42D3F0F668F`
- Rejected refinement path: `refs/derived/bestiarum_rejected_meshy_input_v8.png`
- Rejected refinement SHA-256: `74253F5B89DB675D39F94AF7007358116FB21F30BAA0CF85572580FAC5308D10`
- Source/final comparison: `refs/derived/bestiarum_source_to_final_comparison_v8.png`
- Alpha QA: `refs/derived/meshy_input_alpha_black_v8.png`, `refs/derived/meshy_input_alpha_white_v8.png`, and `refs/derived/meshy_input_alpha_checker_v8.png`
- Technical alpha result: 1254×1254 RGBA; alpha range 0–255; 1,271,898 transparent, 290,736 opaque, and 9,882 partial pixels; visible bounds `[144, 14, 965, 1152]`.
- Visual result before the terms rejection: faithful human Man Eater identity, greatbow/arrow/quiver, skull breast trophy, bone crown, irregular paint, culturally neutral materials, full limbs, and clean alpha.

Native ImageGen transparency failed twice: the first output baked a checkerboard and the targeted retry returned an opaque studio backdrop. The retained rejected evidence used rembg 2.0.61 with post-processing, boundary-only neutral-checker cleanup, and a narrow antialias. No source pixels or derivative pixels ship.

## Continued source recovery

No replacement clears both the visual and rights gates.

1. Eldritch Foundry's *Cannibal Tribe Archer*, sold by Hot Goblin and described in its Japanese catalog as a bone-mask tracker, is visually promising and explicitly cannibal. It is rejected because Hot Goblin Terms section 5 prohibits unauthorized reproduction, alteration, and other secondary use of product photographs and content.
2. The *Bone Tomahawk* troglodyte archer film still is a modern fictional human cannibal with a bow and body paint. It is rejected because it lacks a visible quiver and the required skull/bone headgear and trophy silhouette.
3. Sketchfab's *Cult Fanatic (Enemy Archer)* has a skull mask, bone-crafted bow, muscular human anatomy, and a quiver. It is rejected because the source does not identify the figure as a cannibal; ImageGen may not invent that identity.
4. Bestiarum Hunter 4 is rejected under the same section 6 terms restriction as Hunter 1.
5. The prior Conan and goblin candidates remain rejected for cultural anchoring and wrong species/identity respectively.

The parent-directed Far Cry Primal lead was audited next. The Udam are an explicit fictional cannibal faction, Prima's guide names an `Udam Elite Archer`, and elite Udam use protective masks or helmets and bone armor. March was assigned the heavier elite roaming design, while Network Cadre retains the ordinary lean archer design. Ubisoft's current Terms of Use at `https://www.ubisoft.com/legal/documents/termsofuse/en-US` explicitly prohibit using Ubisoft Services or Content as input in prompts for artificial-intelligence tools or for model training/fine-tuning. This is a direct NoAI-equivalent restriction, so no official, press, wiki, or gameplay screenshot was downloaded or promoted. The design split is recorded only to prevent future duplication if an independently licensed depiction becomes available.

The source shortlist and decisions are recorded in `refs/source/recovery_v8/source_shortlist.json` and `refs/source/recovery_v8/source_shortlist.md`.

## Dependency verification

The repository-owned preflight previously passed:

- Official Meshy MCP package: `@meshy-ai/meshy-mcp-server` 0.4.0
- Meshy SDK: 1.29.0
- Required generation identifier: exact `meshy-7`
- Repository Blender HOI4 adapter: `chaosx_blender_hoi4` 1.10.2
- Blender: 5.1.2, build `ec6e62d40fa9`
- `io_pdx_mesh`: 0.91.0, checksum beginning `A683DF`
- Blender adapter socket: `127.0.0.1:9876`
- `.tools/3d_pipeline/verify_environment.py --probe-meshy`: passed with no findings

No route substitution or downgrade was used.

## Paid operations and costs

- Meshy 7 image-to-3D task `01a03455-079f-704d-b216-79204a845990`: succeeded, 30 credits.
- Provider rig task `01a0345d-a0a0-7232-a8c4-46a35f9204f9`: succeeded, 5 credits.
- Eight distinct `meshy_animate` tasks: all succeeded at 3 credits each, 24 credits total.
- Total v9 Meshy credits consumed: 59.
- A `meshy_convert` compatibility probe against the idle animation was rejected before task creation because animation tasks expose no model file; consumed credits: 0.
- Balance samples were 1,017 before generation, 899 before rigging, 848 before the animation tranche, and 800 after that tranche. Other concurrent workers used the shared account, so costs are taken from exact task receipts rather than inferred balance deltas.
- Exact task IDs, action IDs, arguments, hashes, balances, and receipts: `provider/v9_task_lineage.json`.
- Exact official signed URL inventories: `provider/v9_official_signed_url_inventories.json`.
- Rig and action artifacts were saved with the repository allowlisted `mcp_provider_signed_asset_fetch` transport, restricted to `assets.meshy.ai`; no raw HTTP fallback was used.
- Far Cry Primal source downloads: 0; ImageGen calls: 0.
- Recovery v9 native ImageGen calls: 2 (one bounded object edit and one transparency-only retry); these were native ImageGen operations, not Meshy credits.

## Provider and geometry results

- Generation GLB: `provider/downloads/chiveli_v9_generation_model.glb`, SHA-256 `1B30B6AD38D2CE131C75701F1D8B45452E7EC27846F73588188C4016F0C9F3F6`.
- Visual review passes the identity gate: shortbow, back quiver/arrows, close axe, horned jaw mask, bone trophies, irregular red paint, and asymmetric horror silhouette are all present.
- Bounded geometry QA reached 30,000 triangles, 14,886 vertices, zero non-manifold edges, zero degenerate faces, and 138 loose accessory-seam boundary edges.
- Provider rig FBX SHA-256: `FFF8DA36D9453E7A5B850544AE163CD85CD3F919AFEF5485E5B5E6703BCEB6BF`.
- All eight 24 FPS provider FBX actions and checksums are recorded in `provider/v9_task_lineage.json`; no locally authored, aliased, transform-only, or static replacement action was used.

## Adapter 1.10.2 scale blocker and quarantine

Adapter prepare request `e3f34e3528f84a399989a4a91044dcad` reported a normalization factor of `4.458702482665469`, final mesh height `7.3518242836`, and effective runtime height `5.8814594269` at entity scale `0.8`. Reopening the saved `05_pre_export.blend` through inspect request `7bc02969fd734140ab33e06752c21c89` measured working mesh `char1.001` at only `[1.7731509, 0.8888814, 1.6488708]`, while working armature `Armature.001` retained object scale `0.01`. The prepare response therefore did not match persisted rigged-scene state.

The original rigged preview was extremely small because the saved provider-scale actor was framed against the vanilla-scale reference. Tight inspect previews make the design readable but are camera-only evidence and do not prove runtime scale. No mesh or animation export was accepted.

All 1.10.2 v9 Blender descendants were moved under `blender/rejected/adapter_1_10_2_scale_persistence/`. Exact blocker evidence is `blender/reports/v9_scale_persistence_blocker.json`. Immutable provider sources, actions, audio, and counter evidence remain outside quarantine.

## Adapter 1.10.3 rebuild and mixed-version pause

- Fresh adapter health request `3ea703d385d54b5f951f772eefb7db68` resolved Blender 5.1.2, `io_pdx_mesh`, and adapter 1.10.3.
- Clean prepare request `63f556d5b596498c972775448db4dcc2` started from immutable `provider/downloads/chiveli_v9_rigged_model.fbx`.
- Save/reopen persistence passed: target `7.3518242835` m, persisted `7.3518242835998535` m, delta `9.985345883478658e-11` m, tolerance `7.3518242835e-05` m.
- Accepted prepared geometry is 30,000 triangles and 14,885 vertices, with zero non-manifold edges, zero degenerate faces, no negative-scale objects, and ground contact within `6.93e-7` m.
- Tight front, left, rear, right, and three-quarter previews in `blender/previews/cannibal_march_predation_column_v9_1_10_3_*.png` prove the bow, quiver/arrows, long close blade, bone/skull kit, paint, cloak, mask, and full limbs at comparable framing.
- All eight distinct provider FBXs passed exact checksum and flat provenance verification, were hierarchy-aware retargeted onto `Armature.001`, and were duration-preserving retimed from 24 FPS to 30 FPS. The action report is `blender/reports/v9_adapter_1_10_3_action_processing.json`.
- The declared in-place mapping suppresses only provider-space Hips translation while retaining verified shoulder, arm, spine, leg, hand, foot, neck, and head motion. No body motion was locally authored or replaced.
- Pre-ground five-sample, three-view QA for attack, support attack, and death is recorded in `blender/reports/v9_1_10_3_critical_action_visual_qa.json`. The bow, hand-adjacent mesh, long blade, cloak, and quiver remain bounded and coherent; death contains articulated fall and settling motion. Ground contact still required the adapter's source-preserving Hips-Z correction.
- Ground correction passed for all eight actions with final contact within approximately `±2.62e-5` m, and weight-only sanitization preserved the static 7.3518242836 m geometry while reducing the working mesh to no more than four influences and retaining zero zero-weight vertices.
- A concurrent repository update changed the dependency lock from adapter 1.10.3 to unapproved 1.10.4 during this grounding tranche. Idle, move, attack, and defend grounding ran under 1.10.3; support attack, retreat, training, death, and weight-only sanitization ran under 1.10.4. Exact request IDs and versions are preserved in `blender/reports/v9_1_10_3_grounding_and_sanitization.json`.
- The parent explicitly paused all further adapter calls and exports pending a clean authoritative adapter decision. No `.mesh` or `.anim` from this mixed-version descendant is accepted.

## Remaining work and blockers

- Blender mutation and export are paused until the parent supplies a clean committed adapter continuation after the 1.10.3-to-1.10.4 lock transition.
- Post-ground attack/support/death visual confirmation, remaining-role motion previews, loop-seam review, and final sound-frame synchronization remain required.
- Final PDX texture relink, `.mesh`/eight `.anim` export, and exported/reimported bounds and deformation proof remain required.
- PDX texture processing and final `.mesh` export/reimport remain pending.
- Existing sourced 44,100 Hz audio and bespoke counter evidence were preserved; final frame synchronization and parent-owned runtime/GFX/sound wiring remain pending.
- Parent-owned live in-game validation remains untouched.

## Simplifications, omissions, and blockers

No Meshy identity or animation fallback was used. Native transparency failed twice, so the allowed local background-extraction fallback was used and fully recorded. Adapter 1.10.3 fixed the original persistence defect, but the package remains incomplete because the dependency lock advanced to unapproved 1.10.4 mid-grounding; mixed-version descendants are preserved as evidence and no export is accepted.
