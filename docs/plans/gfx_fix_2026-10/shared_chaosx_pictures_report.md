# Shared Chaos Redux pictures GFX repair report

Status: in progress, with 11 of 16 findings delivered and 5 severity-3 findings queued for the final image tranche.

Scope is limited to the `shared_chaosx_pictures` findings in `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` and `gfx_issues.json`.

## Accepted severity-1 repairs

The parent reviewed both processed previews on 2026-10-06 and accepted their visual treatment. The report image uses the repository's standard tilted-card processor, and the news image is an opaque black-and-white period scene. Both existing sprite names and texture paths remain valid, so no `.gfx` edit is required for these two rows.

| Finding | Status | Target `.gfx` / sprite | Runtime DDS | Target size | Source mode |
|---|---|---|---|---:|---|
| Severity 1: `GFX_report_foreign_liaison` | Handed off; parent visual review accepted, live consumer review pending | `interface/chaosx_pictures.gfx` / `GFX_report_foreign_liaison` | `gfx/event_pictures/005_soviet_collapse/report_foreign_liaison.dds` | 210x176 | Native ImageGen, opaque documentary scene; standard report-card processing |
| Severity 1: `GFX_news_greenland_sold` | Handed off; parent visual review accepted, live consumer review pending | `interface/chaosx_pictures.gfx` / `GFX_news_greenland_sold` | `gfx/event_pictures/092_greenland_sale/news_greenland_sold.dds` | 397x153 | Native ImageGen, opaque documentary scene; black-and-white crop and contrast processing |

### `GFX_report_foreign_liaison` evidence

Generated source PNG: `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/report_foreign_liaison_source.png` (SHA-256 `25404b7c39dfff5b110647194564abc7bf988f332ee2aebbdd64e4f8e93b113b`).

ImageGen prompt: "Use case: historical-scene. Asset type: source art for a Hearts of Iron IV report event image; the repository will apply its standard tilted paper-card treatment after generation. Scene/backdrop: a restrained 1930s diplomatic conference room with dark wood, tall windows, a plain table, and period papers with no legible writing. Subject: three anonymous male diplomats in late-1930s suits seated around the table, one passing a sealed folder; faces are incidental and not individually recognizable. Style/medium: candid 1930s press photograph, natural documentary realism, neutral monochrome tonal base with fine film grain. Composition/framing: medium-wide, table and exchange centered, leave room around the scene for a later cover crop to 210x176. Lighting/mood: soft overcast window light, guarded and formal. Constraints: opaque full-canvas photograph only; do not draw any tilted card, border, paper mat, frame, or drop shadow because those are applied later; no flags, no logos, no readable text, no modern objects, no watermark, no extra people, no theatrical expressions or poster styling."

Processed preview: `docs/assets/gfx_fix_shared_chaosx_pictures/processed/report_foreign_liaison.png` (210x176 RGBA, SHA-256 `acf712c4ce24548185ce2601d786c6f05a0b92445c3b54c936a655c433cd3e7a`).

Before-state runtime DDS snapshot: `docs/assets/gfx_fix_shared_chaosx_pictures/source_runtime/report_foreign_liaison_before.dds` (SHA-256 `7ac6e7f7404a0fc9f93441e52491c427be5b68b230b84f65e8974de4c30a1f5e`); its decoded PNG is `docs/assets/gfx_fix_shared_chaosx_pictures/source_runtime/report_foreign_liaison_before.png`.

Final runtime DDS: `gfx/event_pictures/005_soviet_collapse/report_foreign_liaison.dds` (210x176, SHA-256 `3557a1c114ae0ecab3925a4b577ac0c2d58f601cea0833ea95f21aefe0213804`).

Pixel round-trip is exact between the final DDS decode and the processed PNG. The processed card has alpha range 0-255 and all four canvas corners are transparent. The before snapshot shows the modern three-official podium photograph identified by the raw issue record. Parent source lookup found this sprite only in the GFX registry and no event or common-GUI consumer, so there is no active event ID or in-game consumer check for this row.

### `GFX_news_greenland_sold` evidence

Generated source PNG: `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/news_greenland_sold_source.png` (SHA-256 `5be1ccdbad9f5c5f81369c0955d24ab18d9094d77a6db0a685567a5919fdbd48`).

ImageGen prompt: "Use case: historical-scene. Asset type: full-canvas Hearts of Iron IV news event photograph, final target 397x153. Scene/backdrop: a remote west Greenland fjord settlement in the late 1930s, steep rocky mountains and snow beyond a calm harbor, low wooden houses clustered along the shoreline, one small period fishing boat. Subject: the distinctive Greenland coast and settlement, with no people needed. Style/medium: authentic black-and-white 1930s press photograph, natural documentary realism, crisp midtone detail, restrained film grain and high but printable contrast. Composition/framing: very wide horizontal panorama composed for a 397x153 crop, harbor and buildings across the middle third, mountain silhouette readable above them, no important detail at the extreme top or bottom. Mood: quiet, remote, politically consequential without modern editorial polish. Constraints: opaque full canvas; no map, no labels, no signs, no flags, no logos, no readable text, no modern structures or equipment, no watermark, no border or UI frame."

Processed preview: `docs/assets/gfx_fix_shared_chaosx_pictures/processed/news_greenland_sold.png` (397x153 RGB, SHA-256 `c174f0656500425c6b9edc0a9cb059ab93db0dae7cc9a95ca6ee9a0ed85cb42d`).

Before-state runtime DDS snapshot: `docs/assets/gfx_fix_shared_chaosx_pictures/source_runtime/news_greenland_sold_before.dds` (SHA-256 `9161735a6997d1997efb7eb3e41557aba13b7f2d43fe6f34709ff4051f4fc96f`); its decoded PNG is `docs/assets/gfx_fix_shared_chaosx_pictures/source_runtime/news_greenland_sold_before.png`.

Final runtime DDS: `gfx/event_pictures/092_greenland_sale/news_greenland_sold.dds` (397x153, SHA-256 `d634d6db22878da854becdb6e24781b7db93490c940d944ceca51afd749da69a`).

Pixel round-trip is exact between the final DDS decode and the processed PNG, and all output pixels are opaque. The before snapshot shows the labeled atlas-style map identified by the raw issue record. Parent source lookup confirmed the active consumer is `chaosx.news.73` in `events/_chaosx_news.txt`; the Greenland-sale decision schedules the news event two days later.

### Asset manifest and `.gfx` handoff

| Sprite | Source PNG | Processed PNG | Final DDS | Background mode | `.gfx` owner | Use note |
|---|---|---|---|---|---|---|
| `GFX_report_foreign_liaison` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/report_foreign_liaison_source.png` | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/report_foreign_liaison.png` | `gfx/event_pictures/005_soviet_collapse/report_foreign_liaison.dds` | Opaque source; transparent corners from the standard report-card processor | `interface/chaosx_pictures.gfx` | Sepia 1930s diplomatic-table report image at 210x176; preserve the existing sprite and texture path. |
| `GFX_news_greenland_sold` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/news_greenland_sold_source.png` | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/news_greenland_sold.png` | `gfx/event_pictures/092_greenland_sale/news_greenland_sold.dds` | `consumer_opaque` | `interface/chaosx_pictures.gfx` | Black-and-white 1930s Greenland coast news image at 397x153; preserve the existing sprite and texture path. |

Contact sheet produced from the owning `.gfx` family with the trailer `gfx_sheets.py` utility is retained under `docs/assets/gfx_fix_shared_chaosx_pictures/contact_sheets/severity1_contact_sheet/`. The report JPGs under `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/` were regenerated during the shared session; their current hashes are not treated as before-state evidence. The source runtime DDS snapshots above are authoritative for this tranche.

## Severity-2 findings delivered

Nine severity-2 pictures have generated sources, processed previews, final DDS files, preserved before-state snapshots, and narrowed before/after sheets. The parent accepted their period subjects, framing, and native crops after reviewing the paired before/after sheets. All existing sprite names, `.gfx` definitions, and runtime paths remain unchanged.

All five report pictures use native ImageGen opaque source art and the repository's `process_report_event_image.py` card treatment, producing 210x176 sepia images with transparent corners and a subtle tilted paper frame. The four news pictures use native ImageGen opaque source art, a crop to 397x153, grayscale conversion, and modest period-press contrast. All nine final DDS files decode pixel-exactly to their processed PNGs.

| Sprite | Active consumer | Source PNG and SHA-256 | Processed PNG and SHA-256 | Before DDS SHA-256 | Final DDS and SHA-256 |
|---|---|---|---|---|---|
| `GFX_report_railway_sovereignty` | Unconsumed sprite; only registered in `interface/chaosx_pictures.gfx` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/report_railway_sovereignty_source.png` (`79e56bac2a756e1ccd26b67cc1577f23cc91fa897988e7cbc800b2be224b0218`) | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/report_railway_sovereignty.png` (`b7a6155ae98eb5ab9353a0df29c695f6143688f6f0f40355b1fa533e5c02995a`) | `e5b257156a35c3a06416f860a87e02a14c82756bcbe6b0bc9a1347e2b8fb06b4` | `gfx/event_pictures/005_soviet_collapse/report_railway_sovereignty.dds` (`887c2b7c4638ab260d1da1697a2161999047abbeacef5da007e0102dcb83f3db`) |
| `GFX_report_event_random_war` | `chaosx.nr4.2`, `chaosx.nr4.3`, `chaosx.nr4.4` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/report_event_random_war_source.png` (`68ce811dc9d69c6b46219f306919df2c10260720f70ae1cdceaf0e0bb3ec4fc6`) | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/report_event_random_war.png` (`2f44db4a2c92c4e72a654cb90714bad84e114ed415b961a81462c91395f33152`) | `0ac8ecc5f850eec6e332ac65171b5032ec188fe330776fbc3bb7dc592d48c0b7` | `gfx/event_pictures/004_random_war/report_event_random_war.dds` (`c97e6cf23aa700390a0f0106c7de7cb882ff2f9114f4b68c0d4cb7a68900ac0a`) |
| `GFX_report_event_greenland` | `chaosx.nr92.2`, `chaosx.nr92.3`, `chaosx.nr92.4` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/report_event_greenland_source.png` (`a2a90c2c0eaa1765fbb6e275d876451e6ef67c0a7c7c0ee500a7d959edf9507d`) | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/report_event_greenland.png` (`28b67100eb0cd06d41b9ccce32851d5cf7c1f642a39fd6018b298614395ca4db`) | `8a358c620538d1bb5f14fd031e823d90c5afe7192a6ae7a97104fd72acd6f5b0` | `gfx/event_pictures/092_greenland_sale/report_event_greenland.dds` (`19676262ea93d34f02471000dc21aa1b33490e5a8e246e0cce6e933d969787da`) |
| `GFX_news_california` | `chaosx.news.65` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/news_california_source.png` (`39189cee6ce40953b43a73459df97ec84fe56b63d96b61ccf145b6cf99e95adb`) | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/news_california.png` (`a4e2b5ab654e3e2f7e7725bc4ca83bb69277cc4eb5b50115105b3ebeaa12febe`) | `8ca9abda558dc1d8c89d3ec9c5b0f0a7d42a114da573ee870d300cabca592716` | `gfx/event_pictures/074_japan_california/news_california.dds` (`a1c7cc7b4bc10a0c09c70e77608578a3216536613d879dded9b9e320bdbbd2a7`) |
| `GFX_report_event_california` | `chaosx.nr74.2` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/report_event_california_source.png` (`4d8a6ea1ea7d8c5ee5f5de87a46108b8bc52959faad8568179b6a155c87a84a5`) | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/report_event_california.png` (`506189cc4bbf0b3a6a0d6d2ba3dd58f49671f9f8dc51bca41b52740684a26a3a`) | `185a38689da625df5944485bc156977944a8fdb683852eae413b4b34cac054fe` | `gfx/event_pictures/074_japan_california/report_event_california.dds` (`56f004fccc39344290b59bb4f40fa5d0459bfeae34965bca79e8689702ba8e78`) |
| `GFX_news_galicia` | `chaosx.news.74` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/news_galicia_source.png` (`2066832c22e150021f0093dcabc3704fb2edfc9a8708e80a2677cbbc31b1f047`) | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/news_galicia.png` (`c3684413ce911966c87dac5cd7b29f44e9e7a88d84c8db94b9ea406bd6490019`) | `423588231b1780ae7aa94bd2d302983ebb1f3856ad257ceeb721d98956e806d2` | `gfx/event_pictures/093_portugal_galicia/news_galicia.dds` (`1dbd2bc3fd2e25e9a2c101e473a46941cccabfd0abdea9afb668afa002e3f0ab`) |
| `GFX_news_old_great_bulgaria` | `chaosx.news.51` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/news_old_great_bulgaria_source.png` (`5922039fa8921ca9d3f7937720c130777f0d35352a8eb8869ed88220faf88a2e`) | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/news_old_great_bulgaria.png` (`e15a6628fadc2a7348cef2732d9e99ebdd4bd91e7ec1119c8d4151df9f9293ab`) | `ab080c2bd67b4cb68a1fbf27ae9b013c6d72df4825059ffac19a7f82b6d2452d` | `gfx/event_pictures/048_old_great_bulgaria/news_old_great_bulgaria.dds` (`a4f4f7419a1cfe742632e8155c8c008d31f46430068c48d87cbf5d816878e689`) |
| `GFX_report_event_old_great_bulgaria` | `chaosx.nr48.2`, `chaosx.nr5_custom.36` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/report_event_old_great_bulgaria_source.png` (`a541f71117fb2893ad734332a43792a16b217dc8335dc2491c77d2b55f3e3fa5`) | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/report_event_old_great_bulgaria.png` (`d3eae78c476a9ab23a333b6cdfb90f8c293ffc6022f27787e2bdd73611cc6c21`) | `4334e006d559aba1682c6114fcea12458d7aaa0385d34b9228066da8c4adda4b` | `gfx/event_pictures/048_old_great_bulgaria/report_event_old_great_bulgaria.dds` (`97cb055ec390279757036274e95c23538cc103a117e8b74b055479dd9615dd7b`) |
| `GFX_news_infrastructure_project` | `chaosx.news.54` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/news_infrastructure_project_source.png` (`0c0cbf7d178e4aef65670bb3b4e2e508e84c996ab43b983f37c5bd5fe02c13be`) | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/news_infrastructure_project.png` (`774efb614cafc5d63ed3ba9f18af1328225f15002dd4e06d3bc63d3de48cda2b`) | `d908c9e25b36d1489fcd3863abbf9651ee9968179387a2ee04c9be31cf94fd17` | `gfx/event_pictures/055_great_infrastructure_project/news_infrastructure_project.dds` (`6f183502aef65e0df06bbf1f7f3448263bacbfe35a314b7463df2bfb3bf42d53`) |

The exact severity-2 ImageGen prompt set is retained at `docs/assets/gfx_fix_shared_chaosx_pictures/prompts/severity2_prompts.md`. The pre-replacement source sheet is `docs/assets/gfx_fix_shared_chaosx_pictures/contact_sheets/completed_11_before/shared_chaosx_pictures_1.jpg` (SHA-256 `acc8596b03548e2fd26e487b79d926635d3961164e556f526cf49666bd48bcbf`). The current-runtime output sheet is `docs/assets/gfx_fix_shared_chaosx_pictures/contact_sheets/completed_11_after/shared_chaosx_pictures_1.jpg` (SHA-256 `df3c943ef115f7a66edf6c752f8e904014de2ff56c8d5d2fb7c41bb32cf433b5`). Both are narrowed trailer `gfx_sheets.py` outputs for the 11 completed sprites; the before sheet reads the preserved original DDS snapshots. Older review JPGs were regenerated during the shared session and are not treated as before-state evidence.

### Severity-2 prompt and source mode

Each listed source PNG was generated with native ImageGen from the exact prompt stored under `docs/assets/gfx_fix_shared_chaosx_pictures/prompts/severity2_prompts.md`. Report scenes are opaque source art before repository card processing; news scenes are opaque, full-canvas period press images with no readable text or modern props.

## Remaining finding statuses

These five severity-3 findings remain queued.

| Severity | Sprite | Current or proposed runtime path | Active consumer | Status |
|---:|---|---|---|---|
| 3 | `GFX_news_alien_spacecraft` | `gfx/event_pictures/036_alien_spacecraft/news_alien_spacecraft.dds` | `chaosx.news.41` | Queued: replace the turbine cutaway with a black-and-white documentary-style alien craft or wreck. |
| 3 | `GFX_news_balkans` | `gfx/event_pictures/045_third_balkan_war/news_balkans.dds` | Unconsumed sprite; only registered in `interface/chaosx_pictures.gfx` | Queued: replace the labeled map with a black-and-white period scene or unlabeled aged map. |
| 3 | `GFX_news_failed_research` | `gfx/event_pictures/060_research_failure/news_failed_research.dds` | `chaosx.news.68` | Queued: restore period press contrast and retain a distinct research-failure subject. |
| 3 | `GFX_report_event_alien_spacecraft` | `gfx/event_pictures/036_alien_spacecraft/report_event_alien_spacecraft.dds` | `chaosx.nr36.2`, `chaosx.nr16.18` | Queued: replace the stealth-bomber silhouette with a sepia saucer or wreck scene. |
| 3 | `GFX_report_event_tibet` | Current alias path `gfx/event_pictures/003_holy_realm/report_event_lhasa.dds`; proposed unique path `gfx/event_pictures/003_holy_realm/report_event_tibet.dds` | `germany_mengele.40`-`.44`, `.47`, `.95` | Queued: create a distinct sepia monastery or plateau scene and ask the parent to point this sprite at the unique path. |

## Remaining live checks

After parent integration, confirm the report images appear with transparent corners and the tilted thin border for `chaosx.nr4.2`, `.3`, `.4`, `chaosx.nr92.2`, `.3`, `.4`, `chaosx.nr74.2`, `chaosx.nr48.2`, and `chaosx.nr5_custom.36`. Confirm the news images appear without labels or crop loss for `chaosx.news.73`, `.54`, `.65`, `.74`, and `.51`. The foreign-liaison and railway-sovereignty report sprites have no active event consumer, so no in-game consumer check exists for those two rows because they are registry-only assets.
