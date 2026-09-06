# Event 006 flag and formable visual repair audit — 2026-09-06

Date: 2026-09-06 (Europe/Kyiv).

Owner: bounded Event 006 flag, formable state-puzzle, emblem, and faction-mark visual audit.

Status: complete as a fail-closed bounded audit; no source, processed preview, DDS, TGA, GFX, gameplay, or package file was changed by this tranche. Every reviewed row is technically complete, blocked, or needs_user_review, and no unresolved candidate was promoted.

## Scope and authority

The audit covered the 102 Event 006 registered country tags, their normal/medium/small flag ladders and ideology aliases, the formable state-puzzle packages, the FORM-05 and FORM-48 emblems, the reserved shared league-emblem contract, and the available vanilla faction-logo references.

The Chaos Redux event-assets guidance was read from .agents/skills/chaos-redux-event-assets/SKILL.md, including the canonical-reference, flag-ladder, state-puzzle, manifest, DDS, handoff, and blocker sections.

The canonical vanilla presentation references were inspected at .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md, .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md, flags/contact_sheet.png, and icons/factions/contact_sheet.png.

Existing source authority remains docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_flag_provenance_research_2026-09-05.md, docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_flag_emblem_source_repair_2026-09-05.md, and docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_visual_asset_audit_2026-09-03.md.

## ASSET-044 flag ladders

python .tools/audit_event6_flags.py --strict reports 102 registered tags, 102 complete flag families, and zero incomplete families.

The runtime census is 1,530 TGAs: 510 files under each of gfx/flags/, gfx/flags/medium/, and gfx/flags/small/, covering each tag plus _communism, _democratic, _fascism, and _neutrality.

A fresh read-only binary check found zero issues across all 1,530 files: normal flags are 82x52 and 17,074 bytes, medium flags are 41x26 and 4,282 bytes, small flags are 10x7 and 298 bytes, every file is TGA type 2 with 32-bit pixels and descriptor 8 (bottom-left origin), and every alpha channel is exactly (255,).

All 306 tag-and-size families have zero variant divergence; the five names in each family are byte-identical. This is alias equality only and does not establish an ideology-specific design, source ownership, licence, date, era fit, or route meaning.

The durable review sheets inspected included docs/assets/006_independence_wave/event006_missing_flags_2026_08_02_chunk3/contact_sheets/final_size_ladder_enlarged_contact_sheet.png, docs/assets/006_independence_wave/event006_missing_flags_2026_08_02_chunk_cox_ebx/contact_sheets/final_size_ladder_enlarged_contact_sheet.png, docs/assets/006_independence_wave/form01_02_04_flags_2026_07_15/contact_sheets/final_size_ladder_native_contact_sheet.png, docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/contact_sheets/006_form05_flag_sources_and_ladders.png, docs/assets/006_independence_wave/form09_balkan_federation_flag_2026_08_09/review_contact_sheet.png, docs/assets/006_independence_wave/form48_pacific_assets_2026_07_17/contact_sheets/006_form48_flag_sources_and_ladders.png, and docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_flags_contact_sheet.png.

The inspected ladders have clean flat fields, expected small-size simplification, no visible clipping, no waving-fabric treatment, no unintended opaque padding, and no obvious source-to-size identity swap.

The 2026-09-05 provenance handoff remains authoritative for the source gates: BWX is blocked; the fourteen chunk-3 rows GMX, GZX, HAX, HDX, HEX, IBX, GIX, GRX, HFX, HGX, HKX, HPX, HSX, and HUX remain needs_user_review; NWE bases ACX, AFX, AGX, and AJX are technically handed off while their 48 suffix aliases remain needs_user_review; GLC remains a conditional installed-vanilla carrier with period and redistribution uncertainty; and the CHU/ASY custom opening families remain needs_user_review.

### Alias-removal decision

The 228 identical suffix files are the four aliases at all three sizes for BWX, ACX, AFX, AGX, AJX, and the fourteen chunk-3 tags listed above.

HOI4 can fall back from a missing ideology-specific flag to the unsuffixed tag family, so deletion is technically fallback-compatible in isolation.

Deletion is not safe within the current accepted scope because the NWE package quarantines its 48 aliases pending an explicit cross-event ownership/compatibility policy, the BWX and chunk-3 rows retain blocked or needs_user_review provenance, and the prior source handoff explicitly forbids alias deletion without that policy.

No alias was removed, relabelled, or promoted. A future cleanup requires a separately accepted cross-event policy, a consumer scan, and synchronized package-manifest/hash updates.

### Concurrent flag-byte boundary

The working tree contains concurrent changes that this tranche deliberately preserved.

gfx/flags/AXX_communism.tga currently has SHA-256 55b1dbc417cf1a5d14f45a6f1537c56baa3e6c192ce586e6c9b392db2b4e02cb, matching the accepted AXX base bytes; its old HEAD pointer was a1a3e3ed317d58b7641158bfda9901466a87ac5bb2a96c1aabc325b6424fafac.

The current BLX base and four suffixes at each ladder size are byte-identical and pass the standard TGA checks, with current base hashes 002f71a61a30cfcff839c22e8fb19c8691c153c5fe7d0461952d0e8e765e7678 normal, 8fcf5c38394e3dc2134c89f64445c892e392d794b44791b39100118b69a70ec7 medium, and 8079d1e3bd470b81d0ed0112aedc69995325954ea44cbc5d2763c749bce29110 small.

The FORM-09 package docs/assets/006_independence_wave/form09_balkan_federation_flag_2026_08_09/checksums.json still records the previous normal/medium/small hashes c34689d84c7b2d7b656990ceaac5d85c61667dbf5dfb3810802e3c9ed5b1296f, 24ae5865b48ab9dc36611a69b94680cabd69697311425c184e1f3b0b44718ded, and 93923619801e9255999120c5f1e884e14f5a6bacfea9bf680ba392c4b4449c59.

The current BLX pixels are pixel-identical to the reviewed processed_flat_master.png at all three target dimensions and are now uncompressed type-2 ladders, but the package checksum record needs owner reconciliation after the concurrent change is accepted. No BLX file or package record was overwritten here.

## Formable state-puzzle packages

The 14 Event 006 families are registered through interface/chaosx_formable_state_puzzles.gfx and interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui.

| Family | Manifest assets | Runtime DDS | GFX refs | Accepted state IDs |
| --- | ---: | ---: | ---: | --- |
| FORM-01 | 8 | 8 | 8 | 14, 121, 122, 133 |
| FORM-02 | 10 | 10 | 10 | 100, 121, 133, 331, 337 |
| FORM-03 | 6 | 6 | 6 | 6, 34, 36 |
| FORM-04 | 4 | 4 | 4 | 42, 51 |
| FORM-05 | 6 | 6 | 6 | 1, 114, 115 |
| FORM-07 | 6 | 6 | 6 | 165, 171, 792 |
| FORM-08 | 4 | 4 | 4 | 82, 84 |
| FORM-09 | 12 | 12 | 12 | 104, 105, 106, 184, 185, 802 |
| FORM-12 | 10 | 12 | 10 | 249, 397, 399, 651, 833 |
| FORM-13 | 10 | 12 | 10 | 249, 397, 399, 651, 833 |
| FORM-16 | 6 | 6 | 6 | 229, 230, 231 |
| FORM-18 | 6 | 6 | 6 | 413, 421, 676 |
| FORM-39 | 6 | 6 | 6 | 523, 636, 669 |
| FORM-48 | 6 | 6 | 6 | 378, 629, 684 |

The accepted consumer manifests account for 100 assets and all 100 have matching GFX texture references. A full runtime check found all 104 DDS files decodable with declared dimensions, exact legacy length, non-empty alpha, and no header or length issue.

Exactly four runtime files are not in any accepted manifest or GFX consumer: gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_256_unresolved.dds, gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_256_qualifying.dds, gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_256_unresolved.dds, and gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_256_qualifying.dds.

The four orphan files have retained source and processed previews under the matching docs/formables/state_puzzles/006_form12_state_puzzle/{source,processed}/ and docs/formables/state_puzzles/006_form13_state_puzzle/{source,processed}/ directories.

The state-256 unresolved source and processed PNGs are 21x22 with SHA-256 a00a7c674e423343d2b1bb7aa0347b61bf38362f51ec83670fc84e49fbcbb626, and their decoded runtime DDS is 21x22, 1,976 bytes, with SHA-256 4fdc83caabb2d8350c1ea34196afa1f87a23d57c3e697566977d983ec551f5cb.

The state-256 qualifying source and processed PNGs are 21x22 with SHA-256 85f5a56a7184cd8d75eb63a264d2febc6e7350ef7af907193795beab6096fc57, and their decoded runtime DDS is 21x22, 1,976 bytes, with SHA-256 771d4b633bc4a3c47519a6d9c68199f89a259946e36fcd7c08052cabf1b653c4.

The Form12 and Form13 orphan pairs are pixel-identical from source PNG through processed PNG and decoded DDS, and the Form12 and Form13 bytes are identical because they share the same accepted state geometry registry record.

The accepted source geometry is the installed map registry docs/formables/state_registry/generated/state_geometry_registry.json with registry hash 9777af66b45f2539296e2cc1efaf5b0a8d6146b087f31b2bc1a4c646cc0cc6c5, map hash e131d30e5dcb13d9c2a8598f820a2de0ae9828f3a24f2bddc1bcfff40f71660a, and map revision 5070618991ee5bd9f3076ed92beecfc6a0788c12333e35fc0b648631e800002d.

A read-only manifest/DDS audit over all 100 accepted assets found zero source/processed/runtime/hash/dimension/header/decode errors and zero unresolved-versus-qualifying alpha-bbox mismatches.

The 52 decoded unresolved/qualifying pairs, including the four orphan state-256 pairs, all have matching alpha bounding boxes and are visually distinct only through colour/opacity treatment; no independent border, texture, hatch, label, or other non-colour cue was visible in the inspected zooms.

This is a needs_user_review presentation-contract gap against the event-assets requirement for non-colour distinction between unresolved and qualifying pieces. No mass reprocessing was attempted because the outline/texture treatment, palette, and accepted presentation amendment are not specified by the current consumer owner.

The 14 family projection previews were inspected as a complete montage, with individual FORM-48 unresolved and qualifying projections checked for seam wrapping and canvas bounds. No clipping or incorrect projection placement was found.

The four state-256 files are retained as unused_orphan evidence rather than deleted or promoted. The current consumer state lists intentionally exclude state 256, and an extra asset cannot satisfy an absent accepted row without an explicit design amendment naming its consumer.

## Formable emblems and faction/league marks

The only installed Event 006 formable emblem DDS files are gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds and gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds.

| Family | Source and processed paths | Runtime and sprite | Source / processed / runtime SHA-256 |
| --- | --- | --- | --- |
| FORM-05 / MIX | docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/source_png/emblems/independence_wave_formable_form_05_imagegen_raw.png; alpha master beside it; processed processed_png/emblems/independence_wave_formable_form_05.png | gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds; GFX_independence_wave_formable_form_05 in interface/006_independence_wave_small_assets.gfx | raw 474c47021df519ad38ef179b4c7ebf472569f9ba150ee337fdd5a281a5437575; processed bb488bd2a16873d1cfacee71eb4ac58072178c51fdb6f1f8bb8faf9dd579f9b1; DDS 08dddf415c532570848d022b6e2391e634fd08539ba129e26db518289a594db4 |
| FORM-48 / PFX | docs/assets/006_independence_wave/form48_pacific_assets_2026_07_17/source_png/emblems/independence_wave_formable_form_48_imagegen_raw.png; alpha master beside it; processed processed_png/emblems/independence_wave_formable_form_48.png | gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds; GFX_independence_wave_formable_form_48 in interface/006_independence_wave_small_assets.gfx | raw 5f6bae5775858c2ad15cd38b7f36fac339996aa50088cb67df8773ea31fa8446; processed 9eefdccb957de84587a8a5bd8272fe7cca289fce63ad690c49a58350dba8066e; DDS 6cfa1b3a342f588f17b42802d189c72e6aab6f7c0e12cb3349aedde8e2ecd222 |

Both emblems are 128x128 legacy uncompressed BGRA8888 DDS with real transparency and alpha range 0–255, and each decoded DDS is pixel-identical to its processed PNG.

docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/contact_sheets/006_form05_ui_icons_contact_sheet.png and docs/assets/006_independence_wave/form48_pacific_assets_2026_07_17/contact_sheets/006_form48_emblem_source_and_runtime.png were inspected at native target scale. Both current emblems are clean, centered, and free of opaque square backgrounds or clipped edges.

The shared GFX_independence_wave_league_emblem contract has no DDS, sprite definition, source package, or approved consumer. The canonical vanilla faction contact sheet was used only as a presentation reference; no vanilla faction logo was copied or reused.

FORM-01, FORM-02, FORM-03, FORM-04, FORM-06, FORM-07, FORM-08, FORM-09, FORM-10, FORM-11, FORM-12, FORM-13, FORM-14, FORM-15, FORM-16, FORM-17, FORM-18, and FORM-19 through FORM-47 remain blocked or needs_user_review under the 2026-09-05 emblem/source handoff because their exact emblem identity, route owner, source/rights treatment, or stable consumer is unresolved. Existing flags and state-puzzle pieces are not emblem sources, and no flag was cropped, relabelled, or promoted.

## Parent handoff

The exact accepted emblem basenames are independence_wave_formable_form_05 and independence_wave_formable_form_48, with sprites GFX_independence_wave_formable_form_05 and GFX_independence_wave_formable_form_48.

The reserved but unproduced shared basename remains independence_wave_league_emblem, with reserved sprite GFX_independence_wave_league_emblem; do not create it until universal-versus-family ownership, source, rights, motif, palette, and consumer are accepted.

The exact Event 006 flag runtime convention remains gfx/flags/<TAG>.tga, gfx/flags/medium/<TAG>.tga, and gfx/flags/small/<TAG>.tga, with the four ideology suffix names resolving through the same tag stem when their ownership policy is accepted.

No report, news, super-event, portrait, gameplay, GFX, or GUI file was changed by this bounded tranche. Existing report/super-event audit evidence remains in the 2026-09-03 visual-asset handoff.

## Files changed

Only this dated handoff was added: docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_flag_formable_visual_repair_2026-09-06.md.

No final asset, source file, processed PNG, DDS, TGA, .gfx, .gui, manifest, or gameplay file was changed, staged, or committed by this tranche.

## Remaining blockers and simplifications

No simplification or unsafe fallback was used.

The 228 identical suffix aliases remain preserved because ownership and route policy are unresolved, despite engine fallback being technically possible.

The four state-256 files remain preserved as documented orphan evidence because the current accepted consumer excludes them; deletion or promotion requires an explicit accepted amendment.

The unresolved-versus-qualifying state-piece pairs need an accepted non-colour cue treatment before the state-puzzle visual contract can be called fully compliant.

BWX, chunk-3, NWE suffix, GLC, CHU/ASY, FORM-39, unresolved formable emblem, and shared league-emblem source/rights/identity/consumer gates remain governed by the prior fail-closed handoffs.

No commit was created, per the parent task boundary.
