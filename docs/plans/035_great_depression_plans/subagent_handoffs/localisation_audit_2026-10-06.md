# Event 35 localization and asset audit

Date: 2026-10-06.

Disposition: source-level localization key and asset-path checks pass for the audited surfaces, with one remaining tooltip wording pattern and one stale asset-manifest reference. Current Event 35 MCP rendering and the live national-spirit view remain unresolved.

This was a read-only audit. I changed only this handoff file and did not edit gameplay, localization, GFX, assets, or the workbook.

## Event text and tooltip coverage

`python .tools/report_colour_audit.py --event 035` returned `total keys with colour: 0` before the final copy edits in progress. The parent reports a second run after those edits also returned zero. The script walks visible country and news event title/description text and recursively follows scripted-localization `GetX` calls; it excludes option names and hidden events, which are outside the G1 title/description rule.

A bounded source scan of the 24 Event 35 event roots and the related `chaosx.news.40` and `chaosx.news.95` definitions found 60 title, description, and option-name references, all defined in English localization. The transitive Event 35 scripted-localization closure reached 17 `GetGreatDepression*` methods, with no missing output keys or undefined Event 35 methods.

A source scan found 167 explicit `custom_trigger_tooltip`, `custom_effect_tooltip`, and `complete_effect_tooltip` key references in Event 35-owned source, and every referenced key exists in English localization. This proves reference resolution; it does not independently prove that every effect block has a tooltip.

The visible-requirement scan found 69 exposed flag names across Event 35 decisions and their called scripted triggers. It initially found `great_depression_center_factory_occupation_active` without localization. The parent added `great_depression_center_factory_occupation_active: "The center's factories are occupied by workers."` in `localisation/english/035_great_depression_l_english.yml`, and I verified the definition at line 1033 against its state-trigger use at line 1105. No other missing flag key appeared in that bounded scan.

The remaining copy issue is the repeated use of “national-response slot” and “external-response slot” in `great_depression_can_start_*` and related requirement text. The tooltips resolve, but these phrases describe the action-slot mechanism instead of the conflict the player sees. Consider wording them as an existing response being underway when that condition blocks a choice.

The old repeated-cause fallback issue from the 2026-09-01 localization handoff no longer applies: `GetGreatDepressionCauseTwo` and `GetGreatDepressionCauseThree` fall back to the empty `great_depression.causes.no_suffix` key. I found no player-facing transaction, snapshot, pilot, or ledger UI jargon in the scoped localization files.

## Twelve national-spirit assets

All twelve Round 2 source PNGs, processed PNGs, and runtime DDS files exist at the paths listed in `docs/assets/035_great_depression/manifest.md`. I decoded all twelve source/processed/runtime images with Pillow: source masters are about 1176–1179 by 1334–1337, and processed PNGs and DDS files are all 60x68 RGBA with alpha values from 0 through 255.

The twelve runtime filenames each have a matching sprite and texture path in `interface/035_great_depression.gfx`, and the corresponding `picture` values are present in `common/ideas/035_great_depression_ideas.txt`. The per-icon manifest rows map source PNG, processed PNG, DDS, and sprite. `docs/assets/035_great_depression/audit/runtime_dds_inventory.json` reports 80 decoded DDS files; `audit/asset_audit.md` records zero decode errors and keeps the live national-spirit consumer marked `needs_live_game`.

I inspected `docs/assets/035_great_depression/audit/idea_round2/round2_review_sheet.png`. The twelve subjects are distinct and I saw no obvious clipping, unintended background, or missing artwork. This is offline image review and does not prove live game rendering or final-size legibility in the running consumer.

Two asset-documentation caveats remain. `docs/assets/035_great_depression/audit/asset_audit.md` says its exact icon records are in `docs/assets/035_great_depression/icon_manifest.json`, but that JSON file is absent; the 12-row Round 2 table in `manifest.md` is present. Also, the manifest records the generation route as “gptimage MCP” rather than naming the current skill's native `$imagegen` call. The source files, alpha, dimensions, GFX wiring, and image appearance are verified, while this audit cannot independently equate that recorded route with the current skill's required generation route.

The recorded 60x68 canvas is consistent with the consumer-specific evidence in `audit/asset_audit.md`: vanilla `interface/countrydiplomacyview.gui:national_spirit_ideas_grid` uses a 60x68 slot. This is an accepted consumer-size exception to the skill's general 64x64 default.

## MCP and visual evidence limits

The connected workspace ID returned by `hoi4.reference_context` was `mod_chaos_redux_ea3b2d67c2c0`. Its Event context returned the installed `effects_documentation.md` `news_event` section at lines 5053–5077, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and the offline wiki Event Modding localization section at lines 49–75, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.

The Localization context returned the installed `loc_formatter_documentation.md` heading at lines 1–2, revision `1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08`, and the offline wiki Localization “Usage of Bindable Localization” section at lines 276–346, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.

The context responses omitted other required reference sections. Targeted `hoi4.reference_search` calls for `news_event`, `has_global_flag`, `check_variable`, and variable targeting remained pending and were manually terminated after the bounded wait. I read the corresponding local files directly as fallback: installed `effects_documentation.md` lines 5053–5077, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`; installed `triggers_documentation.md` lines 2110–2134 and 3991–4004, SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`; offline wiki `Data structures - Hearts of Iron 4 Wiki.md` lines 123–125 and 551–553, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`; offline wiki `Triggers - Hearts of Iron 4 Wiki.md` lines 452–473 and 571–599, SHA-256 `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`; and offline wiki `Effects - Hearts of Iron 4 Wiki.md` lines 901 and 948–951, SHA-256 `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.

The bounded `hoi4.event_inspect` lint call for `chaosx.nr35.2` did not return within roughly 150 seconds and was terminated. The single `hoi4.event_render` overview call for the same event remained pending for roughly 90 seconds and was terminated. No fresh event artifact, revision, or diagnostics were returned, so this is a route blocker rather than a clean MCP result.

For the requested native category baseline, `hoi4.gui_inspect` rejected `scenario.country: "USA"` immediately because the live schema expects a record. I did not guess its internal fields. A retry with only the supplied scenario ID and date remained pending for roughly 60 seconds, as did a matching 1920x1080 `hoi4.gui_render` request; both were terminated. The expected consumer is the vanilla `decision_category_desc` in `interface/countrydecisionview.gui`, and Event 35 does not link a scripted GUI to this category. No visual wrapping or after-render verdict is available from this pass.

No game or Excel workbook was opened. No live-game validation was performed; the user remains responsible for checking the category text and twelve national-spirit icons in the running game.

Skills used: `chaos-redux-events` and `chaos-redux-event-assets`, for read-only audit guidance.
