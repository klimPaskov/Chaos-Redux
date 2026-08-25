# Event 012 Africa — Oracle Recon reference replacement handoff

Status: `parent_approved_exact_hash`. Source-replacement tranche complete; stopped before Meshy.

## Outcome

The active reference is replaced with a materially better, grounded adult African male oracle/diviner. The exact alpha-decontaminated cleanup is `docs/assets/012_africa/models_3d/oracle_recon/refs/original/meshy_input.png`, 3143x4350 RGBA, SHA-256 `160602EDE80FF5428089D2C5B5012C52EC3019023D26DF22D96B12DDDEF6A76B`. Parent visual approval on 2026-08-25 is hash-bound to that file. No Meshy, balance, Blender, adapter or other provider route was called; this tranche consumed zero credits.

Parent review sheet: `docs/assets/012_africa/models_3d/oracle_recon/refs/derived/luan_silva_source_to_cleanup_contact_sheet.jpg`, SHA-256 `29899DF66392B0CD22E904AFA421A0B80F1B0C8719BC50A1843B296FEFD9781E`.

## Selected source and terms

- Artwork: “African Shaman.”
- Creator: Luan Silva (`Luan_Vieira`).
- Publisher/page: ZBrushCentral, https://www.zbrushcentral.com/t/african-shaman/444985.
- Linked creator portfolio: https://www.artstation.com/artwork/vDbbd6.
- Direct source render: https://www.zbrushcentral.com/uploads/default/original/4X/2/9/a/29a57cd39c64b0d870df6fe5d7115f34800ae503.jpeg.
- Published: 2023-04-05; retrieved: 2026-08-25.
- Source fingerprint: 3143x4350 RGB JPEG, SHA-256 `75AD9DA9680152B74575237007DA6340BA865B75E36E0261D5A1D919A31CF70D`.
- Terms: copyrighted authorial portfolio artwork; no reusable license stated. Accepted only as non-shipping `reference_only_user_authorized` visual reference under the user's standing authorization. The inspected ZBrushCentral and linked ArtStation pages exposed no explicit NoAI, no-derivatives or equivalent incompatible term.
- Untouched source bytes were removed after inspection/hashing/cleanup because separate archival permission was not established. The required comparison sheet remains non-shipping review evidence.

## New candidate gates

- Identity: pass — clearly adult African male, realistic readable face/body, practical travelling oracle/diviner rather than glamorized fantasy assassin.
- Completeness: pass — full head, torso, arms/hands, legs/feet and complete held staff are visible; riggable humanoid anatomy.
- Style: pass — professional realistic real-time character render; no anime, manga, manhwa, chibi, cel shading or exaggerated anime proportions.
- Color: pass — genuinely colored skin, cloth, leather, fur, wood and bone; not monochrome.
- Period/technology: pass — ritual/medieval/fantasy equipment is compatible with the 1936–45 alternate-history world; no electronics, advanced optics, modern tactical gear, plastic or science-fiction machinery.
- Recon readability: pass with review note — staff, pouches, lightweight field garments and mobile silhouette read as travelling scout/diviner, though oracle is stronger than military reconnaissance. No spyglass or new scout gear was invented.
- Alpha: pass — RGBA, alpha 0–255, four corners zero, 9,174,983 zero-alpha pixels, 4,497,067 nonzero-alpha pixels, visible bbox `(483, 111, 2531, 4315)`.
- Fidelity: pass — final preserves the source's pose, anatomy, clothing, equipment, proportions, materials, palette and details. Light/dark/checker review shows no clipped staff/anatomy, visible signature, cast backdrop or unintended internal holes.

## Cleanup lineage

The native ImageGen faithful-cleanup call preserved identity but returned a 1067x1475 RGB image with baked checkerboard, SHA-256 `BAFE1A2B1473CC2C8B8FFE0658B987C4C868C10F21CF45C1C32543E32C161133`; rejected. A targeted alpha-only native revision returned another RGB checkerboard, 1067x1474, SHA-256 `F2277A31CE4B0EB96A57912D8A8CEE168C3FFF0BF21C3D6B4D0842ED9AE90051`; rejected.

The documented fallback used `rembg 2.0.61`/`u2net` on the immutable high-resolution source, followed by deterministic alpha remap (`<=128 -> 0`; `129..255 -> 2..255`). It removed the background and signature without asking ImageGen to redraw or invent anything. Alpha review: `refs/derived/luan_silva_source_rembg_review_light_dark_checker.jpg`, SHA-256 `CD7BA13889F4334F0A4CF7EAAC491F51C8A7A8C2A7454AE801101ABEC28472FF`.

## Rejected old identity and all derivatives

The user rejected Jordy Knoop's “05 - Spy” as a weird stylized/anime-female fantasy spy rather than the intended African male oracle-scout. Its exact former active input, SHA-256 `860D7814D7E730F6CEE2F1EDB44AEAEB9A93E394CC5851BC06B3992F8F4C7579`, is preserved at `refs/rejected/jordy_knoop_lineage_superseded_2026-08-25/meshy_input_jordy_knoop_rejected.png`.

The rejection propagates to the entire old identity lineage, all marked `rejected_superseded_identity_do_not_wire`:

- generation `01a0345a-a2aa-7203-8656-18c4c8bd6a99`;
- remesh `01a03464-33a4-7504-9d6e-f6f93cf13ec4`;
- rig `01a0346a-7566-7ca3-a2ae-5aec375ddc41`;
- idle `01a03493-4028-7bd8-9e25-38e8908aff0b`;
- move `01a03493-5bf1-78b1-af72-8ef7d02530b6`;
- recon `01a03493-73a5-78b5-9482-7ec0d4f7daaa`;
- observation `01a03493-90bb-7ce8-ad96-16df660a861e`;
- death `01a03493-ad58-72a6-9009-f2962b4be834`;
- all old GLB/FBX downloads, Blender checkpoints/previews, rig weights, PDX textures, `.mesh`, five `.anim`, export/reimport proofs, action semantics, audio synchronization, bespoke counters and runtime handoffs.

Those files remain immutable evidence and were not deleted or overwritten. Historical spend remains nine paid operations / 85 credits and is not attributed to this zero-credit tranche.

## Required next gate

Parent has visually approved exact SHA-256 `160602EDE80FF5428089D2C5B5012C52EC3019023D26DF22D96B12DDDEF6A76B`. The replacement identity now requires a separate fresh full Meshy/model/action tranche plus audio synchronization and bespoke counter regeneration/revalidation; runtime wiring remains parent-owned. Do not reuse or wire any old model, action, audio synchronization or counter output.

## Files changed within owned scope

- `docs/assets/012_africa/models_3d/oracle_recon/**`: active input, preserved rejected input/evidence, source/provenance/search/prompt/validation/contact sheets, job/manifest/history, and rejection banners on old runtime/audio/counter handoffs.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_oracle_recon_reference_replacement.md`.

No gameplay, GFX, entity, sound-definition, localisation, spreadsheet, other event or runtime implementation file was edited. No commit was created.
