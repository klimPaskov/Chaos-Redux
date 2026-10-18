# Event 029 ordinary decision-icon repair — continuation handoff

**Status:** candidate production and evidence are complete for the current batches; every item except the two parent-promoted runtime assets remains candidate-only and requires parent review.

**Scope:** only the 47 ordinary decision-icon aliases registered in `interface/029_riches_found.gfx` and consumed by `common/decisions/029_riches_found_decisions.txt`; all new outputs target the native 32×32 alpha-backed decision family.

**Authority and ownership:** the parent owns runtime promotion and final DDS approval; this handoff records evidence and candidates only.

All prior candidate sources, exact prompts, version history, and baseline hashes remain preserved in the [October 7 handoff](decision_icon_repair_2026_10_07.md), [candidate lineage](../../../assets/029_riches_found/repair_2026_10_07_decisions/candidate_lineage.md), and [baseline hash record](../../../assets/029_riches_found/repair_2026_10_07_decisions/baseline_hashes.md).

The parent confirmed that sanitation v2 and dividend v2 were promoted and committed as `f7a08ab4fbb91e07f52ca8f73ee92885284d9f76`.

Any October 7 wording that described those two items as uncommitted or not committed is superseded for current status only; the original October 7 text and its baseline hashes remain preserved as historical evidence.

No GFX, decision, gameplay, localisation, or runtime DDS file was edited in this continuation; no Git/index/commit operation or game launch was performed.

## Consumer and visual family evidence

The canonical decision reference family was inspected from `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/decisions`, beginning with its contact sheet and then the relevant individual references; no project-local reference copy was used.

The installed vanilla ordinary decision-row consumer was inspected in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/countrydecisionview.gui` and `countrydecisionview.gfx`.

The vanilla dark row texture is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/decisionview/decision_item_bg.dds`, 1536×40, SHA-256 `a8b995d02cb82c501227bdb3c7a375baaec6f2a8b7519378b87269eb1409b52a`.

The first 512×40 row frame places the 32×32 icon slot at `(14,3)-(46,35)`; its extracted slot review image is `review/parent_dds_review_2026_10_08/native_ui/vanilla_decision_item_bg_icon_slot_32.png`, SHA-256 `62d9999d89635fe47f623ccb58fa36733bd6baa54c0013ebfa87a7591c2d13a6`.

## First review batch — parent-accepted compact compositions, final DDS gate pending

The parent opened the source, processed PNG, native decoded-DDS PNG, and enlarged decoded-DDS view individually for all four entries and accepted the compositions: army cordon/posts/rope/helmet, concession auction/gavel, deeper drilling/rock, and mine police/shield.

The acceptance is for composition only; parent final DDS approval and any runtime promotion remain pending.

All four are 1254×1254 transparent ImageGen masters with retained prompts; each processed image is 32×32 and each candidate DDS is a strict single-level 32×32 BGRA decode with alpha 0–255 and exact decoded-pixel equality to its processed PNG.

| Alias | Exact ImageGen source output | Prompt record | Retained source PNG and SHA-256 | Processed PNG and SHA-256 | Candidate DDS and SHA-256 | Native decoded DDS PNG and SHA-256 | Nearest 4× decoded view and SHA-256 | Nearest 8× decoded view and SHA-256 |
|---|---|---|---|---|---|---|---|---|
| `army_cordon` | `C:/Users/klimp/.codex/generated_images/01a116d0-794f-77c2-8780-8cca0aa1b404/exec-0abb4631-db3d-4659-893d-97920a7e3da9.png` | `prompts/decision_riches_found_army_cordon_edit_v2_compact_2026_10_07.md` | `candidate/source_png_v2_compact_2026_10_07/decision_riches_found_army_cordon.png`; `7a4cc14bf7a10934ff8d04382559f221515483e721eda617cd83b8f0252d4a48` | `candidate/processed_png_v2_compact_fit28_2026_10_07/decision_riches_found_army_cordon.png`; `eb49eab049c977a59d7653f85dd88a1f8e1aab151e394bf7dcce97dbded9f14a` | `candidate/final_dds_v2_compact_fit28_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_army_cordon.dds`; `2e49e0567bdee1270f9afde744d2082575a999cb67f3c9d3f440725a3778bf50` | `review/parent_dds_review_2026_10_08/native/decision_riches_found_army_cordon.png`; `eb49eab049c977a59d7653f85dd88a1f8e1aab151e394bf7dcce97dbded9f14a` | `review/parent_dds_review_2026_10_08/nearest_4x/decision_riches_found_army_cordon.png`; `53b6372770b14012ed39a3d595b263882955ac37c41015a60bc1b0cdee3949d9` | `review/parent_dds_review_2026_10_08/nearest_8x/decision_riches_found_army_cordon.png`; `5e6a2232bf77f41178abcbbda9faed40f200c0b4c8f9570092d97f4c541aad7a` |
| `concession_auction` | `C:/Users/klimp/.codex/generated_images/01a116d0-794f-77c2-8780-8cca0aa1b404/exec-2f525635-2419-4972-a78b-11c4517c7e2d.png` | `prompts/decision_riches_found_concession_auction_edit_v2_compact_2026_10_07.md` | `candidate/source_png_v2_compact_2026_10_07/decision_riches_found_concession_auction.png`; `7b6e7c924b76e5d38a720a2387d9d35bb2a312c3841b559385ff81298b915926` | `candidate/processed_png_v2_compact_fit28_2026_10_07/decision_riches_found_concession_auction.png`; `fb44b6876e49ba3b6105f74e41f0021972ae6f38776a6fe95781d5b4bd3129f5` | `candidate/final_dds_v2_compact_fit28_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_concession_auction.dds`; `8ffb58c86a31a10af7555c10e08b4c6c22305a1bea38a23ef8f37aab6af587c3` | `review/parent_dds_review_2026_10_08/native/decision_riches_found_concession_auction.png`; `fb44b6876e49ba3b6105f74e41f0021972ae6f38776a6fe95781d5b4bd3129f5` | `review/parent_dds_review_2026_10_08/nearest_4x/decision_riches_found_concession_auction.png`; `11ea5e8305978a72f90653ca2e758403728a1fcef31f3c1ca25d8d227377cbf4` | `review/parent_dds_review_2026_10_08/nearest_8x/decision_riches_found_concession_auction.png`; `1e4b022016471028c81b0954541516e40d97fd655b2f460635bdd26667629bad` |
| `drive_deeper` | `C:/Users/klimp/.codex/generated_images/01a116d0-794f-77c2-8780-8cca0aa1b404/exec-7ce5c80b-0268-45f9-b311-c7ab9aa3b075.png` | `prompts/decision_riches_found_drive_deeper_edit_v2_compact_2026_10_07.md` | `candidate/source_png_v2_compact_2026_10_07/decision_riches_found_drive_deeper.png`; `3c9693edde9a90e0d4b8c858521a4faf8417afd60b05f6ab9b38b456caeb76c2` | `candidate/processed_png_v2_compact_fit28_2026_10_07/decision_riches_found_drive_deeper.png`; `ab7ceef17577ffa066948e398d6068e7d5d5757f4234d9008e1cef9b031bb96c` | `candidate/final_dds_v2_compact_fit28_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_drive_deeper.dds`; `69401ed02bc426918566c49b00a03f4e19ae2ba6ebf33bedadc90542f53db99e` | `review/parent_dds_review_2026_10_08/native/decision_riches_found_drive_deeper.png`; `ab7ceef17577ffa066948e398d6068e7d5d5757f4234d9008e1cef9b031bb96c` | `review/parent_dds_review_2026_10_08/nearest_4x/decision_riches_found_drive_deeper.png`; `59eabf2e6b39b9407324dcc2416cef2aa3ef54743965ec743d823b8458bcf0c4` | `review/parent_dds_review_2026_10_08/nearest_8x/decision_riches_found_drive_deeper.png`; `c9c32b4125de53484050ce146e0f1cd6a391ce39cffc44b5543e8f29e5372e18` |
| `mine_police` | `C:/Users/klimp/.codex/generated_images/01a116d0-794f-77c2-8780-8cca0aa1b404/exec-e9742802-aa1f-408b-876e-a0ff21e064fb.png` | `prompts/decision_riches_found_mine_police_edit_v2_compact_2026_10_07.md` | `candidate/source_png_v2_compact_2026_10_07/decision_riches_found_mine_police.png`; `8d5c11143244bd0d301dd137e9b952ee170bc9011036bc7ddbc2de29c4ddeb36` | `candidate/processed_png_v2_compact_fit28_2026_10_07/decision_riches_found_mine_police.png`; `bb52418b6c29c0df6502cc309a4b2ecf968b64b468644cc83826aa82ce0fea8c` | `candidate/final_dds_v2_compact_fit28_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_mine_police.dds`; `732859b8aa2786af5a2bdc6c4699a9435d48ac81a1b9249a4e0ca0c73e15c145` | `review/parent_dds_review_2026_10_08/native/decision_riches_found_mine_police.png`; `bb52418b6c29c0df6502cc309a4b2ecf968b64b468644cc83826aa82ce0fea8c` | `review/parent_dds_review_2026_10_08/nearest_4x/decision_riches_found_mine_police.png`; `39c74358a0e7ee23bde521f60bfe85c996c46b59a001cf5d88b0f14bb7740de2` | `review/parent_dds_review_2026_10_08/nearest_8x/decision_riches_found_mine_police.png`; `5df6e4ca6f517532597e95e67f88ba2ec84f623b6ae743289b670066ab2cdfc3` |

### Edge-fleck review for the first batch

The parent noticed isolated-looking light pixels around the cordon, gavel, and drill in enlarged decoded-DDS views; those were checked against the untouched source alpha and the actual vanilla dark decision-row icon slot.

Each source has one principal component at alpha ≥16, no alpha ≥8 source pixels touch the canvas edge, and any secondary alpha ≥8 pieces lie within 1.91 source pixels of the principal silhouette.

The apparent detached marks in processed output are alpha 1–4 only; over the exact native dark-row slot their maximum per-channel contribution is 2 values for each of the four icons.

The dark-row composites are `review/parent_dds_review_2026_10_08/native_ui/decision_riches_found_army_cordon_on_vanilla_decision_row_32.png` (SHA-256 `407499b87c73676ab72c8b7e8f866dacd9c45cedf4083c92b833ca16586128d3`), `review/parent_dds_review_2026_10_08/native_ui/decision_riches_found_concession_auction_on_vanilla_decision_row_32.png` (SHA-256 `5fd64c82215ca660ed043034156631e0c565457693dc0b888bd2754c318b7545`), `review/parent_dds_review_2026_10_08/native_ui/decision_riches_found_drive_deeper_on_vanilla_decision_row_32.png` (SHA-256 `6e553c553e9754919ae8ec811af0c622e637bbd5c90cf212fbacd9c25a7df0dc`), and `review/parent_dds_review_2026_10_08/native_ui/decision_riches_found_mine_police_on_vanilla_decision_row_32.png` (SHA-256 `e5cc09aee5bfb9b85a2da4533159eee43ddc9539778f6819c496535026ef1f35`).

The native composites show no visible detached dust; no cleanup child, rescale, or semantic source edit was warranted, and all original source/processed/DDS versions remain intact.

## Batch 02 — current review queue

The parent individually reviewed source, processed PNG, native decoded DDS, and 4× decoded DDS for all six Batch 02 originals.

The compositions of housing, port route, pay train, and truce were accepted; their final DDS approval remains pending the same edge and round-trip review gate.

| Alias | Source PNG and SHA-256 | Prompt | Processed PNG and SHA-256 | Candidate DDS and SHA-256 | Native / nearest 4× / nearest 8× decoded views |
|---|---|---|---|---|---|
| `housing` | `candidate/source_png_v1_compact_batch02_2026_10_07/decision_riches_found_housing.png`; `61fe98290d5be0110b4ed76cf0cb20bffece8493fee8b706c056aae5a7324457` | `prompts/decision_riches_found_housing_edit_v1_compact_batch02_2026_10_07.md` | `candidate/processed_png_v1_compact_fit28_batch02_2026_10_07/decision_riches_found_housing.png`; `2dbae444929e625809351efe49f4c801a443eb9026289bf96baada9350aaad51` | `candidate/final_dds_v1_compact_fit28_batch02_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_housing.dds`; `5785adf74933f60e3585fb49c5080e138a27dc65a5869a14009204af79270be8` | `review/parent_dds_review_2026_10_08/native/decision_riches_found_housing.png` (`2dbae444929e625809351efe49f4c801a443eb9026289bf96baada9350aaad51`); `review/parent_dds_review_2026_10_08/nearest_4x/decision_riches_found_housing.png` (`be71ac1ada252886ee96fdf46ca386e3e324009e27d631b69250ab0ca7131eed`); `review/parent_dds_review_2026_10_08/nearest_8x/decision_riches_found_housing.png` (`df33cd56c87cea62b0aae2fe44ae0f3cfce5a1e68784c1ad59ef6a81915d47c7`) |
| `port_route` | `candidate/source_png_v1_compact_batch02_2026_10_07/decision_riches_found_port_route.png`; `619760d1e83eeb66be8026ec5f21e4c90722934e0b769f24cdc446011711f2ef` | `prompts/decision_riches_found_port_route_edit_v1_compact_batch02_2026_10_07.md` | `candidate/processed_png_v1_compact_fit28_batch02_2026_10_07/decision_riches_found_port_route.png`; `ebdbca89297cd97489da1335f7904815c8cb8de37ee5bcdd772630dcb745d6bf` | `candidate/final_dds_v1_compact_fit28_batch02_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_port_route.dds`; `0117ed2badd5ad2f7b70982a10689c8c34e786e560f854c9e26f3527669e8347` | `review/parent_dds_review_2026_10_08/native/decision_riches_found_port_route.png` (`ebdbca89297cd97489da1335f7904815c8cb8de37ee5bcdd772630dcb745d6bf`); `review/parent_dds_review_2026_10_08/nearest_4x/decision_riches_found_port_route.png` (`026ce5150a8c198bba96f667df1c42aec12ce879d76c5659b536f709c4a87498`); `review/parent_dds_review_2026_10_08/nearest_8x/decision_riches_found_port_route.png` (`e01a64152c78e025e9057e336564fb6abd49d3f37add295a64ce4d24c7d5dce6`) |
| `pay_train` | `candidate/source_png_v1_compact_batch02_2026_10_07/decision_riches_found_pay_train.png`; `8ce317d3b4822b5c978d130da36a132e22dab2be8c83e4a4440610eea717dd21` | `prompts/decision_riches_found_pay_train_edit_v1_compact_batch02_2026_10_07.md` | `candidate/processed_png_v1_compact_fit28_batch02_2026_10_07/decision_riches_found_pay_train.png`; `8f40a517c999ac4025c415aaf47016368c6e43405c226edf7c5417471546a3b8` | `candidate/final_dds_v1_compact_fit28_batch02_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_pay_train.dds`; `075d86d567b8f101fbf83f523886abe3ea98f0d7efed4fc7aeea4473c3be8222` | `review/parent_dds_review_2026_10_08/native/decision_riches_found_pay_train.png` (`8f40a517c999ac4025c415aaf47016368c6e43405c226edf7c5417471546a3b8`); `review/parent_dds_review_2026_10_08/nearest_4x/decision_riches_found_pay_train.png` (`80ae352ad7d885d1bdf51b8c36b20fcaa13a6f13f3a9b5b04f6ff5a2a4221b58`); `review/parent_dds_review_2026_10_08/nearest_8x/decision_riches_found_pay_train.png` (`8bdb6eb5c16f9498aca65b300365f7efbe64621561f846fcf79a72e3254d230f`) |
| `truce` | `candidate/source_png_v1_compact_batch02_2026_10_07/decision_riches_found_truce.png`; `860487e7e0feba7842c0531813f9c8148c98c6f17828975509b67711f0e96997` | `prompts/decision_riches_found_truce_edit_v1_compact_batch02_2026_10_07.md` | `candidate/processed_png_v1_compact_fit28_batch02_2026_10_07/decision_riches_found_truce.png`; `f0be81692141c8a08fa3250b53272683cfa3b7788a1942eb5b16af7c9631635f` | `candidate/final_dds_v1_compact_fit28_batch02_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_truce.dds`; `523ff542a62e768b32dcf7a58fac200fb43a0cf46e34b449821bf39a7d1db5f0` | `review/parent_dds_review_2026_10_08/native/decision_riches_found_truce.png` (`f0be81692141c8a08fa3250b53272683cfa3b7788a1942eb5b16af7c9631635f`); `review/parent_dds_review_2026_10_08/nearest_4x/decision_riches_found_truce.png` (`2f3789c476ee95744c8e462e88c886cefa9e7102922c3a92b6c82396e66a0f1f`); `review/parent_dds_review_2026_10_08/nearest_8x/decision_riches_found_truce.png` (`a42612513f31697bce710a42bb6fc7fec6c03d88ad2036446c64688163a42e99`) |

For the four accepted compositions, alpha ≥8 source components do not touch the source canvas edge; their secondary components sit within 1.91 source pixels of the main silhouette.

The processed versions contain only low-alpha edge pixels at alpha 1–4, with counts 80 (housing), 84 (port route), 74 (pay train), and 59 (truce); over the vanilla dark-row icon slot these contribute at most 2, 3, 2, and 2 channel values respectively.

All four candidate DDS files decode pixel-identically to their processed PNGs; no edge cleanup or rescale was made.

The original evacuation composition is rejected because the worker merged into a dark shaft, the frame dominated, and removal/person movement was not legible at native size.

The original temporary-closure composition remains borderline because numerous fine bars/grid filled the canvas and the chain/padlock collapsed into the center.

The old versions and exact prompts remain preserved; no historical prompt was reconstructed.

| Alias | Current visual repair | Exact ImageGen output | Prompt record | Source PNG and SHA-256 | Processed PNG and SHA-256 | Candidate DDS and SHA-256 | Native / nearest 4× / nearest 8× decoded views |
|---|---|---|---|---|---|---|---|
| `evacuation` | v5 focused ImageGen edit; current candidate emphasizes a brighter, distinct exiting worker as the primary silhouette and a minimal recessed frame | `C:/Users/klimp/.codex/generated_images/01a11a44-68b1-7230-98e5-94c5e1c5d2e3/exec-ff1eeb73-ac5a-425e-9b3c-3ea26e8efab4.png` | `prompts/decision_riches_found_evacuation_edit_v5_compact_batch02_2026_10_08.md` | `candidate/source_png_v5_compact_batch02_2026_10_08/decision_riches_found_evacuation.png`; `f8c05ed2a2ae465139f5ba98e2b0a9d52c658cee19a8c560520b8f3c4d395ff3` | `candidate/processed_png_v5_compact_fit28_batch02_2026_10_08/decision_riches_found_evacuation.png`; `dcb6f38873a009593b1116de1f28f1666dd44b3ae1a0a6cfaffa233bb8b03706` | `candidate/final_dds_v5_compact_fit28_batch02_2026_10_08/gfx/interface/decisions/029_riches_found/decision_riches_found_evacuation.dds`; `93e74b6d803fa00b062228eef7ad40c623b5fd7457625ab0aca43ea71046f7e2` | `review/parent_dds_review_2026_10_08/batch02_v5/native/decision_riches_found_evacuation.png` (`dcb6f38873a009593b1116de1f28f1666dd44b3ae1a0a6cfaffa233bb8b03706`); `review/parent_dds_review_2026_10_08/batch02_v5/nearest_4x/decision_riches_found_evacuation.png` (`f1c11f8729e7cccbf5a4ee02fceccefea492e407bf84434e60945dc6e434d68b`); `review/parent_dds_review_2026_10_08/batch02_v5/nearest_8x/decision_riches_found_evacuation.png` (`2e6f08c1b5756a0dcd6508849e28360fbbbb94db57e3c82bfd38ebae5569e65a`) |
| `temporary_closure` | v4 fresh original ImageGen candidate; current composition uses fewer heavy bars, a larger readable padlock/chain, and a visibly reopenable gate | `C:/Users/klimp/.codex/generated_images/01a11a44-68b1-7230-98e5-94c5e1c5d2e3/exec-c4d50015-b81a-4910-acf3-bb59846ba2e0.png` | `prompts/decision_riches_found_temporary_closure_gen_v4_compact_batch02_2026_10_08.md` | `candidate/source_png_v4_compact_batch02_2026_10_08/decision_riches_found_temporary_closure.png`; `dad8a95428485ac02e7f24d704cb69cd3351cd89a8a6e4ceea4501ec83236905` | `candidate/processed_png_v4_compact_fit28_batch02_2026_10_08/decision_riches_found_temporary_closure.png`; `2f3c5346f0bf4d18dcfa81a35b8377da1590b90586649122d34cda3511dfc719` | `candidate/final_dds_v4_compact_fit28_batch02_2026_10_08/gfx/interface/decisions/029_riches_found/decision_riches_found_temporary_closure.dds`; `532fe8e186f4430855db6e5e195a277f9ef711ea7a1f0e60549fc65c7c90797f` | `review/parent_dds_review_2026_10_08/batch02_v4/native/decision_riches_found_temporary_closure.png` (`2f3c5346f0bf4d18dcfa81a35b8377da1590b90586649122d34cda3511dfc719`); `review/parent_dds_review_2026_10_08/batch02_v4/nearest_4x/decision_riches_found_temporary_closure.png` (`c00069f3351591348e9cb115e033b163415d42b5dcef43bf9fbf250596dcf2e3`); `review/parent_dds_review_2026_10_08/batch02_v4/nearest_8x/decision_riches_found_temporary_closure.png` (`2c66b806f74fc44c4a9ac3c28f86b5d61b666c37b0d436624e2b808781c7037e`) |

For temporary-closure v4, the retained source remains unchanged; the processing derivation cleared only source pixel `(0,0)` from alpha 1 to transparent black before resizing because it was an isolated exterior alpha speck.

That was a bounded one-pixel alpha cleanup, not background removal; no opaque/chroma background, local primitive redraw, or scale-only repair was used.

Evacuation v5 and temporary-closure v4 are new review candidates, not parent-approved compositions or runtime assets.

## Batches 05–08 — remaining candidate coverage

The original native-alpha generation route was continued through Batches 05, 06, 07, and 08 rather than stopping after the gap inventory.

The new outputs comprise 27 candidates for previously uncovered aliases, five distinct alternatives for aliases that already had earlier unreviewed candidates, and the two Batch 02 clarity revisions above.

Batch 05 includes `bargain` v3 as the current inset candidate; its earlier v2 source remains preserved and rejected because alpha ≥8 touched the canvas edge.

Batch 06 includes `private_guards` v2 as a contrast alternative and `permanent_seal` v3 as the current clean original; permanent-seal v1/v2 remain preserved because the distant low-opacity speck persisted through the v2 edit.

Every current candidate has its own prompt record, retained ImageGen source, processed PNG, candidate DDS, strict DDS decode-to-PNG pixel equality result, and native / nearest 4× / nearest 8× decoded review copies.

All new ImageGen generation/edit calls requested a genuine transparent background, and the alpha channel was preserved through processing and DDS conversion; no opaque/chroma substitute or local primitive redraw was used.

The full 34-row current lineage table, including exact source dimensions/alpha bounds and source, processed, DDS, and review-image paths, is in [the active manifest](../../../assets/029_riches_found/repair_2026_10_07_decisions/manifest.md).

The current review sheets are `decision_icons_batch01_compact_v2_2026_10_08.png`, `decision_icons_batch02_current_2026_10_08.png`, `decision_icons_batch05_current_2026_10_08.png`, `decision_icons_batch06_current_2026_10_08.png`, `decision_icons_batch07_2026_10_08.png`, and `decision_icons_batch08_2026_10_08.png` under `docs/assets/029_riches_found/repair_2026_10_07_decisions/candidate/contact_sheets/`.

The current Batches 05–08 and Batch 02 revision candidates were also composited into the exact vanilla dark decision-row slot; their alpha 1–4 fringe pixels produce only 1–3 channel-value changes in the native-size crop and no visible detached flecks.

All current-generation and Batch 02 revision candidates remain `needs_user_review`; contact sheets communicate candidate coverage, not semantic approval.

## Review disposition and next owner action

The parent-approved compositions awaiting final DDS review are the four compact v2 icons in the first table plus housing, port route, pay train, and truce.

The existing nationalize v4 compact candidate is also carried forward as `needs_user_review`; it was not regenerated because it already has a distinct key-in-lock composition, and its earlier versions and prompt lineage remain preserved.

| Alias | Exact ImageGen output | Prompt record | Source PNG and SHA-256 | Processed PNG and SHA-256 | Candidate DDS and SHA-256 | Native / enlarged decoded DDS views |
|---|---|---|---|---|---|---|
| `nationalize` | `C:/Users/klimp/.codex/generated_images/01a116d0-794f-77c2-8780-8cca0aa1b404/exec-8a39690f-a1d4-41ff-b105-2a851c4fe9aa.png` | `prompts/decision_riches_found_nationalize_edit_v4_compact_2026_10_07.md` | `candidate/source_png_v4_compact_2026_10_07/decision_riches_found_nationalize.png`; `353881d34db7b14fc6655f355197d70d17dc35ef2d8e17f8251f988b77d1d83b` | `candidate/processed_png_v4_compact_fit28_2026_10_07/decision_riches_found_nationalize.png`; `bfb8a9bee6f74d324369914fa7080ad74526e5325454f987be866131d31690fd` | `candidate/final_dds_v4_compact_fit28_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_nationalize.dds`; `a36b4c48e64d55c45b79977da2a6bb8eaec6170b8b407f337fac81513101c5c` | `review/decoded_candidate_dds_batch01_fit28/decision_riches_found_nationalize.png` (`bfb8a9bee6f74d324369914fa7080ad74526e5325454f987be866131d31690fd`); `review/enlarged_candidate_dds_batch01_fit28/decision_riches_found_nationalize.png` (`49a956f6578b65d7c1586ad7a1a7c59f71dc465d6834e8eb61264f36c28c28ae`) |

The parent should review the two current Batch 02 clarity revisions and the Batch 05–08 current candidates from the listed source/processed/native/enlarged DDS paths and contact sheets.

No candidate in this handoff was copied into the runtime DDS tree; parent-only review, approval, and runtime promotion remain outstanding.

No unavailable historical prompt was reconstructed, no accepted Batch 02 candidate was regenerated, and no generic cross-family substitute was used.

This continuation used the `chaos-redux-event-assets` and official native `imagegen` skills; no animation workflow was required.

## Append-only current status update — 2026-10-08, after parent final DDS approval

This appendix records the later parent decision and supersedes earlier status statements above only for the eight selected assets listed here; it does not rewrite or invalidate their historical source, candidate, or baseline evidence.

The parent granted final DDS approval for `army_cordon`, `concession_auction`, `drive_deeper`, `mine_police`, `housing`, `port_route`, `pay_train`, and `truce` after review of each actual vanilla-row 32×32 composite and 4× enlargement.

The parent copied the exact selected candidate DDS bytes to their existing runtime paths; a read-only SHA-256 comparison confirms every runtime file matches its selected candidate exactly.

The parent reports that delivered DDS-decoder pixel checks and registry checks passed for all eight; the permanent evidence is in [decision_asset_repair_2026_10_08.md](../../../events/029_riches_found/decision_asset_repair_2026_10_08.md).

| Alias | Selected candidate DDS | Runtime DDS | Matching runtime SHA-256 |
|---|---|---|---|
| `army_cordon` | `docs/assets/029_riches_found/repair_2026_10_07_decisions/candidate/final_dds_v2_compact_fit28_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_army_cordon.dds` | `gfx/interface/decisions/029_riches_found/decision_riches_found_army_cordon.dds` | `2e49e0567bdee1270f9afde744d2082575a999cb67f3c9d3f440725a3778bf50` |
| `concession_auction` | `docs/assets/029_riches_found/repair_2026_10_07_decisions/candidate/final_dds_v2_compact_fit28_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_concession_auction.dds` | `gfx/interface/decisions/029_riches_found/decision_riches_found_concession_auction.dds` | `8ffb58c86a31a10af7555c10e08b4c6c22305a1bea38a23ef8f37aab6af587c3` |
| `drive_deeper` | `docs/assets/029_riches_found/repair_2026_10_07_decisions/candidate/final_dds_v2_compact_fit28_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_drive_deeper.dds` | `gfx/interface/decisions/029_riches_found/decision_riches_found_drive_deeper.dds` | `69401ed02bc426918566c49b00a03f4e19ae2ba6ebf33bedadc90542f53db99e` |
| `mine_police` | `docs/assets/029_riches_found/repair_2026_10_07_decisions/candidate/final_dds_v2_compact_fit28_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_mine_police.dds` | `gfx/interface/decisions/029_riches_found/decision_riches_found_mine_police.dds` | `732859b8aa2786af5a2bdc6c4699a9435d48ac81a1b9249a4e0ca0c73e15c145` |
| `housing` | `docs/assets/029_riches_found/repair_2026_10_07_decisions/candidate/final_dds_v1_compact_fit28_batch02_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_housing.dds` | `gfx/interface/decisions/029_riches_found/decision_riches_found_housing.dds` | `5785adf74933f60e3585fb49c5080e138a27dc65a5869a14009204af79270be8` |
| `port_route` | `docs/assets/029_riches_found/repair_2026_10_07_decisions/candidate/final_dds_v1_compact_fit28_batch02_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_port_route.dds` | `gfx/interface/decisions/029_riches_found/decision_riches_found_port_route.dds` | `0117ed2badd5ad2f7b70982a10689c8c34e786e560f854c9e26f3527669e8347` |
| `pay_train` | `docs/assets/029_riches_found/repair_2026_10_07_decisions/candidate/final_dds_v1_compact_fit28_batch02_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_pay_train.dds` | `gfx/interface/decisions/029_riches_found/decision_riches_found_pay_train.dds` | `075d86d567b8f101fbf83f523886abe3ea98f0d7efed4fc7aeea4473c3be8222` |
| `truce` | `docs/assets/029_riches_found/repair_2026_10_07_decisions/candidate/final_dds_v1_compact_fit28_batch02_2026_10_07/gfx/interface/decisions/029_riches_found/decision_riches_found_truce.dds` | `gfx/interface/decisions/029_riches_found/decision_riches_found_truce.dds` | `523ff542a62e768b32dcf7a58fac200fb43a0cf46e34b449821bf39a7d1db5f0` |

The exact selected prompts were copied byte-for-byte to `docs/events/029_riches_found/asset_provenance_2026_10_08/prompts/`: `decision_riches_found_army_cordon.md`, `decision_riches_found_concession_auction.md`, `decision_riches_found_drive_deeper.md`, `decision_riches_found_mine_police.md`, `decision_riches_found_housing.md`, `decision_riches_found_port_route.md`, `decision_riches_found_pay_train.md`, and `decision_riches_found_truce.md`.

The two earlier runtime promotions remain committed as `f7a08ab4fbb91e07f52ca8f73ee92885284d9f76`; these eight additional runtime copies are present but not yet committed, and the parent will report their commit separately.

Together, ten of the 47 aliases are runtime-changed; 37 remain unapproved, with the 34 current/carry-forward candidates still queued for parent review.

The prior runtime DDS bytes for these eight are recoverable from Git and the active baseline archive as confirmed by the parent; historical baseline hashes above and in `baseline_hashes.md` remain unchanged.

This is partial asset approval only, not completion of the 47-icon family or the Event 029 asset goal.

## Append-only commit confirmation — 2026-10-08

The parent confirms that the eight approved DDS runtime promotions listed in the preceding status appendix were committed as `c606f8d415761de9a626780a117a729706ef3c35`.

Parent reports that index reconciliation verified 17 paths, the eight native runtime DDS byte streams match their selected candidate DDS files, and LFS pointer OIDs and cached objects match after hashing.

The current total is ten of 47 ordinary decision icons runtime-promoted: the prior sanitation/dividend pair in `f7a08ab4fbb91e07f52ca8f73ee92885284d9f76` plus these eight in `c606f8d415761de9a626780a117a729706ef3c35`.

The remaining 37 decision icons are not approved, and other Event 029 asset families remain outstanding; the full asset goal is not complete.

No further production is authorized before the parent reviews the remaining candidate queue.

## Append-only versioned native-row evidence — evacuation v5

The earlier generic evacuation native-row composite is not treated as evidence for v5 because its candidate-version binding was not established.

The following new inspection copies are explicitly bound to the selected v5 DDS `candidate/final_dds_v5_compact_fit28_batch02_2026_10_08/gfx/interface/decisions/029_riches_found/decision_riches_found_evacuation.dds`, SHA-256 `93e74b6d803fa00b062228eef7ad40c623b5fd7457625ab0aca43ea71046f7e2`.

The transparent native decode used as the foreground is `review/parent_dds_review_2026_10_08/batch02_v5/native/decision_riches_found_evacuation.png`, SHA-256 `dcb6f38873a009593b1116de1f28f1666dd44b3ae1a0a6cfaffa233bb8b03706`.

The exact vanilla background is `review/parent_dds_review_2026_10_08/native_ui/vanilla_decision_item_bg_icon_slot_32.png`, SHA-256 `62d9999d89635fe47f623ccb58fa36733bd6baa54c0013ebfa87a7591c2d13a6`; it is the 32×32 icon-slot crop `(14,3)-(46,35)` from the first frame of the inspected vanilla decision row.

| View | Version-bound review PNG | Dimensions | SHA-256 |
|---|---|---|---|
| Native row | `review/parent_dds_review_2026_10_08/native_ui/continuation/decision_riches_found_evacuation_v5_vanilla_row32.png` | 32×32 | `f744e917b43fcc96dda4fc9fa547ac40ad765023884941ba76eeec194f19bac0` |
| Nearest-neighbour enlargement | `review/parent_dds_review_2026_10_08/native_ui/continuation/decision_riches_found_evacuation_v5_vanilla_row32_4x.png` | 128×128 | `0c4254409b86a6d59f23b0fb25e0c6cb5abcd417e5fac2e72dde65db9f49e558` |

The 32×32 preview is the exact alpha composite of that v5 DDS decode over the vanilla slot crop; the 4× view is a nearest-neighbour enlargement of the composite for inspection only.

These version-bound review files do not alter semantic art or runtime assets; no runtime write was made for this check.
