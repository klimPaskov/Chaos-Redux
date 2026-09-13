# Event 029 Riches Found Generated Event Art Audit Handoff

Audit date: 2026-09-01.

This handoff covers only the nine report-event images and the one static decision-category picture assigned to the generated-event-art worker.

Eight retained source PNGs are valid native built-in ImageGen outputs for the fictional alternate-history documentary brief. The raid and Gold Disease sources were regenerated with native built-in ImageGen after parent review identified forbidden chest imagery, then reprocessed and reconverted through the canonical asset tools.

Per-asset disposition: all ten assigned assets are `art QA pass / parent review pending`; the repaired raid and Gold Disease masters supersede their earlier sources, and none is blocked or needs further user review for image quality.

The audit does not claim package completion, runtime wiring completion, or live in-game validation.

## Reference and consumer inspection

- Canonical report family: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`, its `contact_sheet.png`, root `README.md`, and root `CATALOG.md`.
- Canonical decision-category picture family: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/`, its `contact_sheet.png`, root `README.md`, and root `CATALOG.md`.
- Vanilla report consumer precedent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/eventpictures.gfx`, including `GFX_report_event_001`, `GFX_report_event_airplane_crash`, and `GFX_report_event_soldiers_parade`.
- Vanilla category-picture consumer precedent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/decisions.gfx`, including `GFX_decision_cat_picture_naval_treaties`, `GFX_decision_cat_picture_1936_election`, and `GFX_decision_cat_picture_faction_management_bulgaria`.
- Category presentation consumer: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/countrydecisionview.gui`, including the `decision_category_desc` picture region.
- Current project registration inspected but not edited: `interface/029_riches_found.gfx`.

The report family is treated as a 210x176 tilted documentary card with opaque content and transparent outer corners.

The category family is treated as a distinct opaque 114x101 presentation image without fake UI, readable text, or transparent corners.

## Processing and validation evidence

- Report processing provenance: `python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`.
- DDS conversion provenance: `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.
- Machine report: `docs/assets/029_riches_found/notes/validation_report.json`.
- Report contact sheet: `docs/assets/029_riches_found/contact_sheets/reports_contact_sheet.png`.
- Category contact sheet: `docs/assets/029_riches_found/contact_sheets/category_picture_contact_sheet.png`.
- Final processed-versus-decoded review: `docs/assets/029_riches_found/contact_sheets/final_roundtrip_review.png`.
- Every source PNG, processed PNG, and decoded DDS round trip was opened for visual inspection.
- All report outputs are 210x176, use the processor-created transparent outer corners, and have decoded DDS pixels exactly equal to the processed PNG pixels.
- The report DDS files use the repository-standard one-level BGRA layout with `147968` bytes, a 128-byte legacy header, and a 32-bit BGRA pixel payload.
- The category output is 114x101, opaque from edge to edge, uses `46184` bytes, and has a pixel-exact DDS round trip.

## Per-asset audit

### `GFX_report_event_riches_found_discovery`

Visual finding: The source shows a period excavation discovery with a bright ore seam, miners and prospectors, an improvised work camp, and officials controlling access.

The scene reads at native report size as a discovery report and avoids a treasure chest, giant crystal, modern open-pit machinery, readable text, watermarks, and portrait framing.

Repair: No art repair or regeneration.

Paths: Source `docs/assets/029_riches_found/source_png/riches_found_discovery_report_source.png`; processed preview `docs/assets/029_riches_found/processed_png/report_event_riches_found_discovery.png`; DDS evidence `docs/assets/029_riches_found/final_dds/report_event_riches_found_discovery.dds`; runtime DDS `gfx/event_pictures/029_riches_found/report_event_riches_found_discovery.dds`; decoded round trip `docs/assets/029_riches_found/notes/decoded_dds/report_event_riches_found_discovery.png`.

Provenance: Native built-in ImageGen generation record `exec-2f961dce-e75f-44e8-8902-c716b0b64db5`; prompt archive `docs/assets/029_riches_found/prompts/generated_event_art_prompts.md`.

Checksums: Source `01e0663fe6c8e37d1645860855ab88e7a7f8a89208773e432f807498712a7dd4`; processed `382d0648eb725b7817667903174b913fffae6196fd8b957068f78200f93b6644`; DDS and runtime `4b8a7de5ffa9290ed69aaa6b9617e090496fb74d9a458ebced981870971e77ad`.

QA: Source 1549x1015 and opaque; processed and decoded 210x176 with alpha range 0-255 and transparent corners; DDS is 147968 bytes; round trip exact.

### `GFX_report_event_riches_found_rush`

Visual finding: The source shows a dense period rush camp with wooden housing, canvas, workers, a merchant table, a period truck, a horse cart, and a mine road or shaft.

The opportunity and congestion read at native report size without modern vehicles, readable text, a generic crowd-only composition, or portrait framing.

Repair: No art repair or regeneration.

Paths: Source `docs/assets/029_riches_found/source_png/riches_found_rush_report_source.png`; processed preview `docs/assets/029_riches_found/processed_png/report_event_riches_found_rush.png`; DDS evidence `docs/assets/029_riches_found/final_dds/report_event_riches_found_rush.dds`; runtime DDS `gfx/event_pictures/029_riches_found/report_event_riches_found_rush.dds`; decoded round trip `docs/assets/029_riches_found/notes/decoded_dds/report_event_riches_found_rush.png`.

Provenance: Native built-in ImageGen generation record `exec-6a429cf4-ab77-4d5c-9df1-5b81005f42e3`; prompt archive `docs/assets/029_riches_found/prompts/generated_event_art_prompts.md`.

Checksums: Source `6b2d6be7fda9ccd7d5f24808b639184e23c17483001645c45c9586b9acbccfe1`; processed `464c258a2b15ceeef37b0c49d3149b83ed4435391880de5f6868e2220d79d2f2`; DDS and runtime `f686f95d5a1f3790485c37903a91bd48f8f6583cf35cc5340b012f0d793a3c94`.

QA: Source 1536x1024 and opaque; processed and decoded 210x176 with alpha range 0-255 and transparent corners; DDS is 147968 bytes; round trip exact.

### `GFX_report_event_riches_found_concession`

Visual finding: The source shows an industrial processing works with conveyor machinery, workers behind a gate, officials or engineers, guards, rifles, and period uniforms.

The controlled-access concession reads at native report size without relying on a handshake, a meeting table, modern equipment, readable text, or portrait framing.

Repair: No art repair or regeneration.

Paths: Source `docs/assets/029_riches_found/source_png/riches_found_concession_report_source.png`; processed preview `docs/assets/029_riches_found/processed_png/report_event_riches_found_concession.png`; DDS evidence `docs/assets/029_riches_found/final_dds/report_event_riches_found_concession.dds`; runtime DDS `gfx/event_pictures/029_riches_found/report_event_riches_found_concession.dds`; decoded round trip `docs/assets/029_riches_found/notes/decoded_dds/report_event_riches_found_concession.png`.

Provenance: Native built-in ImageGen generation record `exec-188c923a-d55a-45fa-99d0-f588615b9de4`; prompt archive `docs/assets/029_riches_found/prompts/generated_event_art_prompts.md`.

Checksums: Source `2c83b5dc25145dd13c23ad2138418fd5a8dbc2cbb4801804000b37304680ea0f`; processed `13acbd1e833c6a1aa79f1cfe20f9ecf0286300dd031dc4fe7c0385dee7e1d82b`; DDS and runtime `d5b3b728f4698f39ad6a7b35b53e44ee762164419d248ef8108822d52c9d9e2f`.

QA: Source 1536x1024 and opaque; processed and decoded 210x176 with alpha range 0-255 and transparent corners; DDS is 147968 bytes; round trip exact.

### `GFX_report_event_riches_found_raid`

Visual finding: The repaired source shows a canvas-wrapped assay crate with sample trays and a document satchel, armed claimants and guards, and access around a mine or office.

The raid reads as a focused seizure at native report size without gore, a generic battlefield, modern weapons, readable text, or portrait framing.

Repair: Replaced the forbidden treasure-chest/strongbox motif with a canvas-wrapped assay crate, sample trays, and document satchel using native built-in ImageGen. The prior source is retained under `docs/assets/029_riches_found/notes/superseded_sources/riches_found_raid_report_source_before_chest_repair.png`.

Paths: Source `docs/assets/029_riches_found/source_png/riches_found_raid_report_source.png`; processed preview `docs/assets/029_riches_found/processed_png/report_event_riches_found_raid.png`; DDS evidence `docs/assets/029_riches_found/final_dds/report_event_riches_found_raid.dds`; runtime DDS `gfx/event_pictures/029_riches_found/report_event_riches_found_raid.dds`; decoded round trip `docs/assets/029_riches_found/notes/decoded_dds/report_event_riches_found_raid.png`.

Provenance: Native built-in ImageGen generation record `exec-2ecf30d8-9893-45c9-81bb-103044563591`; repair prompt is retained in `docs/assets/029_riches_found/prompts/generated_event_art_repairs.md`.

Checksums: Source `a2f62557bcaff49694986e0ada4f7e2c83b7f743e7533ad80fb5ea292a0d7ac6`; processed `b7b0091bdbd4b7d3a904fda6a0694ccae9ac81cdd8f7d744d1c38c14f637530c`; DDS and runtime `6d7fb9ccb586528c345f937e8258b12cdb5d837609ee9196a12e497d52fc348e`.

QA: Source 1536x1024 and opaque; processed and decoded 210x176 with alpha range 0-255 and transparent corners; DDS is 147968 bytes; round trip exact.

### `GFX_report_event_riches_found_collapse`

Visual finding: The source shows rescuers digging through damaged timber supports with dust, broken rail, and winch infrastructure.

The collapse reads as a period mine accident at native report size without bodies, gore, supernatural elements, modern rescue equipment, readable text, or portrait framing.

Repair: No art repair or regeneration.

Paths: Source `docs/assets/029_riches_found/source_png/riches_found_collapse_report_source.png`; processed preview `docs/assets/029_riches_found/processed_png/report_event_riches_found_collapse.png`; DDS evidence `docs/assets/029_riches_found/final_dds/report_event_riches_found_collapse.dds`; runtime DDS `gfx/event_pictures/029_riches_found/report_event_riches_found_collapse.dds`; decoded round trip `docs/assets/029_riches_found/notes/decoded_dds/report_event_riches_found_collapse.png`.

Provenance: Native built-in ImageGen generation record `exec-42d9ac7a-c346-45c1-a54c-a538fb6659cc`; prompt archive `docs/assets/029_riches_found/prompts/generated_event_art_prompts.md`.

Checksums: Source `145c7a750f4b8a86fb0078572e8f0d5d01e7cb72acf4cb7f3dc89df8d711e406`; processed `78fb75cf9c82d9f859c655aa8d28cb4a17a0109b0ddbd969fb40cbcb091d3984`; DDS and runtime `bbf428c4687b2c02d367cffbaa840aee26c91134c7c41ab0d0d2af50de4e5841`.

QA: Source 1536x1024 and opaque; processed and decoded 210x176 with alpha range 0-255 and transparent corners; DDS is 147968 bytes; round trip exact.

### `GFX_report_event_riches_found_gold_disease`

Visual finding: The repaired source shows workers counting or hiding small pieces at an assay bench, a balance scale, ledger papers, a canvas pouch, and suspicious guards.

The metaphor for social gold disease reads at native report size without plague imagery, medical props, zombies, glowing infection, readable text, or portrait framing.

Repair: Replaced the forbidden locked-chest motif with an assay bench, balance scale, ore samples, ledger sheets, and a canvas pouch using native built-in ImageGen. The prior source is retained under `docs/assets/029_riches_found/notes/superseded_sources/riches_found_gold_disease_report_source_before_chest_repair.png`.

Paths: Source `docs/assets/029_riches_found/source_png/riches_found_gold_disease_report_source.png`; processed preview `docs/assets/029_riches_found/processed_png/report_event_riches_found_gold_disease.png`; DDS evidence `docs/assets/029_riches_found/final_dds/report_event_riches_found_gold_disease.dds`; runtime DDS `gfx/event_pictures/029_riches_found/report_event_riches_found_gold_disease.dds`; decoded round trip `docs/assets/029_riches_found/notes/decoded_dds/report_event_riches_found_gold_disease.png`.

Provenance: Native built-in ImageGen generation record `exec-09ab7ba5-a795-4c11-81b7-0c65ba9ce090`; repair prompt is retained in `docs/assets/029_riches_found/prompts/generated_event_art_repairs.md`.

Checksums: Source `a3236af9a2638c0b1c678ac3bf553319b49168aee1059ea4fcf50bee53948f29`; processed `136d99033321a94643a83de8b6b4aef20b7b717a354d93d36c64277072dd472b`; DDS and runtime `43c3df7e59f7b257485d178a106b0fca2db9bc89aa1cd26376a69ed6c770af4d`.

QA: Source 1537x1023 and opaque; processed and decoded 210x176 with alpha range 0-255 and transparent corners; DDS is 147968 bytes; round trip exact.

### `GFX_report_event_riches_found_opened_depths`

Visual finding: The source shows miners in a timbered deep chamber and a narrow luminous geometric passage as the single supernatural feature.

The real rock, timber, and period lamps anchor the opened-depths concept at native report size without demons, lava, an altar, modern horror props, readable text, or portrait framing.

Repair: No art repair or regeneration.

Paths: Source `docs/assets/029_riches_found/source_png/riches_found_opened_depths_report_source.png`; processed preview `docs/assets/029_riches_found/processed_png/report_event_riches_found_opened_depths.png`; DDS evidence `docs/assets/029_riches_found/final_dds/report_event_riches_found_opened_depths.dds`; runtime DDS `gfx/event_pictures/029_riches_found/report_event_riches_found_opened_depths.dds`; decoded round trip `docs/assets/029_riches_found/notes/decoded_dds/report_event_riches_found_opened_depths.png`.

Provenance: Native built-in ImageGen generation record `exec-52f52846-3ae1-4205-9165-f3645a853d6c`; prompt archive `docs/assets/029_riches_found/prompts/generated_event_art_prompts.md`.

Checksums: Source `cbbcafaba7512a41d1cada5355f3d11c88dc6e1158f8a499a308b2d0320601e4`; processed `5b3fe2e2d2a7c78518de4aa39db6f80ac84fd35f48a523b099027f9a2d147a5e`; DDS and runtime `0fc3e29319981856c45b6120d29f0fbe3f1a4db6107b4cc2ba326fac37d88626`.

QA: Source 1536x1024 and opaque; processed and decoded 210x176 with alpha range 0-255 and transparent corners; DDS is 147968 bytes; round trip exact.

### `GFX_report_event_riches_found_gilded_sovereignty`

Visual finding: The source shows a guarded mine enclave with gatehouse, housing, payroll or security access, rail wagons, and a central outsider.

The order, wealth, and separation read at native report size without a new flag, a throne, modern infrastructure, readable text, or portrait framing.

Repair: No art repair or regeneration.

Paths: Source `docs/assets/029_riches_found/source_png/riches_found_gilded_sovereignty_report_source.png`; processed preview `docs/assets/029_riches_found/processed_png/report_event_riches_found_gilded_sovereignty.png`; DDS evidence `docs/assets/029_riches_found/final_dds/report_event_riches_found_gilded_sovereignty.dds`; runtime DDS `gfx/event_pictures/029_riches_found/report_event_riches_found_gilded_sovereignty.dds`; decoded round trip `docs/assets/029_riches_found/notes/decoded_dds/report_event_riches_found_gilded_sovereignty.png`.

Provenance: Native built-in ImageGen generation record `exec-93da2a92-79d1-4000-aa3a-d2c988f0f0a3`; prompt archive `docs/assets/029_riches_found/prompts/generated_event_art_prompts.md`.

Checksums: Source `faabe4d8e4239cf935cfb2aaf4ef0217c3345460d54113afc2125a073d0eb5f0`; processed `e87f214528daa61abad8c9a13f07df5562d7688845ae5b0c489b16e093b5195d`; DDS and runtime `1ca6db8409969b38c43a1a18b1dc4d7fd230053a63174dcac8aa3884301f8743`.

QA: Source 1536x1024 and opaque; processed and decoded 210x176 with alpha range 0-255 and transparent corners; DDS is 147968 bytes; round trip exact.

### `GFX_report_event_riches_found_bottomless_account`

Visual finding: The source shows an underground assay room with scale, ore, ledger, observers, and an open pit-like aperture that physically implies an impossible transaction.

The account concept reads at native report size without depending on legible ledger text, modern financial props, fake UI, readable text, or portrait framing.

Repair: No art repair or regeneration.

Paths: Source `docs/assets/029_riches_found/source_png/riches_found_bottomless_account_report_source.png`; processed preview `docs/assets/029_riches_found/processed_png/report_event_riches_found_bottomless_account.png`; DDS evidence `docs/assets/029_riches_found/final_dds/report_event_riches_found_bottomless_account.dds`; runtime DDS `gfx/event_pictures/029_riches_found/report_event_riches_found_bottomless_account.dds`; decoded round trip `docs/assets/029_riches_found/notes/decoded_dds/report_event_riches_found_bottomless_account.png`.

Provenance: Native built-in ImageGen generation record `exec-b16b5da3-84d7-47ee-8a9f-14a4e7ce76b5`; prompt archive `docs/assets/029_riches_found/prompts/generated_event_art_prompts.md`.

Checksums: Source `87ab70761c8152b4c30d3d4cb657f22a2f9b2a29bc7d9ff65fae3927f2288ef0`; processed `8154b4791f647e5374f252d126cb48cacafca67850a3c9d9ffe0aba25a59ec34`; DDS and runtime `e043f685634d2360c50b42a5edb68f97f920515be7b7d8aa471e88963605d57a`.

QA: Source 1536x1024 and opaque; processed and decoded 210x176 with alpha range 0-255 and transparent corners; DDS is 147968 bytes; round trip exact.

### `GFX_decision_cat_picture_riches_found`

Visual finding: The source is a broad opaque sepia mine entrance with rail and ore wagons, a pay-transport horse wagon, workers, guards, rough offices, and housing.

The image works as a distinct category baseline at native 114x101 presentation size and contains no fake UI, readable text, transparent corners, Gold Disease-specific imagery, or supernatural demon imagery.

Repair: No art repair or regeneration.

Paths: Source `docs/assets/029_riches_found/source_png/riches_found_category_picture_source.png`; processed preview `docs/assets/029_riches_found/processed_png/decision_cat_picture_riches_found.png`; DDS evidence `docs/assets/029_riches_found/final_dds/decision_cat_picture_riches_found.dds`; runtime DDS `gfx/interface/decisions/029_riches_found/decision_cat_picture_riches_found.dds`; decoded round trip `docs/assets/029_riches_found/notes/decoded_dds/decision_cat_picture_riches_found.png`.

Provenance: Native built-in ImageGen generation record `exec-9c8f480c-5965-42c7-852e-684a91dce470`; prompt archive `docs/assets/029_riches_found/prompts/generated_event_art_prompts.md`.

Checksums: Source `baaf6bea083d4005709ce37a872bd7fcb68b8d5f80d149f4d5ce2cd524252636`; processed `76eca15441765b8a781f8964e9f1807c069d72f179588f981c590f4b3d6380ff`; DDS and runtime `4ef47fbf0362974de50e2fd907e378ff39d57b81ff54a7b2e77edecd8c752042`.

QA: Source 1254x1254 and opaque; processed and decoded 114x101 with alpha range 255-255 and opaque edges; DDS is 46184 bytes; round trip exact.

## Evidence repairs and ownership boundary

- Updated `docs/assets/029_riches_found/manifest.md` so the missing transient ImageGen filesystem paths are explicitly recorded as unavailable while the retained source masters, prompt archive, generation record IDs, and hashes remain authoritative.
- Updated `docs/assets/029_riches_found/gfx_handoff.md` so the current project target is `interface/029_riches_found.gfx`; vanilla `eventpictures.gfx` and `decisions.gfx` remain documented as consumer precedents.
- The raid and Gold Disease source masters, processed PNGs, DDS files, runtime copies, and contact-sheet panels were regenerated after the chest-image defect was found; superseded masters remain in the notes archive.
- No `.gfx`, gameplay, event, decision, localisation, GUI, flag, portrait, icon, animation, audio, or 3D file was edited.

## Skipped validation and blockers

- Live Hearts of Iron IV launch, in-game event display, decision-category display, and final runtime screenshot validation were skipped because they belong to the parent integration workflow.
- The installed vanilla consumers and current project sprite registration were inspected, but this worker did not edit or validate parent-owned runtime wiring in-game.
- The original transient `$CODEX_HOME/generated_images/` paths are absent, so those paths cannot be reopened; the retained local source PNGs, generation record IDs, prompt archive, hashes, and processing evidence preserve provenance.
- No art-production blocker remains for these ten assigned assets.
