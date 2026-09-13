# Event 006 flag asset audit handoff — 2026-09-13

## Disposition

This bounded audit is complete with no runtime flag edits. The accepted ASSET-044 flag ladders and accepted route/formable basenames pass the mechanical and visual checks below. The package remains `needs_user_review` or `blocked` where the accepted provenance handoff records unresolved historical identity, source rights, provider terms, or parent-owned route admission. No blocked identity was promoted to playable content.

Audit owner: bounded Event 006 flag-family auditor/repairer.

Audit date: 2026-09-13, Europe/Kyiv.

## Authority and required references

- Accepted registry: `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv`, row `ASSET-044`.
- Accepted runtime manifest: `docs/assets/006_independence_wave/manifest.md`.
- Prior technical repair boundary: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_flag_formable_visual_repair_2026-09-06.md`.
- Latest provenance and rights gate: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_flag_provenance_research_2026-09-12.md`.
- Latest completion update: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_asset_audit_completion_update_2026-09-12.md`.
- Flag rules: `.agents/skills/chaos-redux-event-assets/SKILL.md`.
- Coordination and handoff rules: `.agents/skills/chaos-redux-subagents/SKILL.md`.
- Offline references read: `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md` and `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`.
- Canonical vanilla references read and visually opened: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/contact_sheet.png`, `README.md`, and `CATALOG.md`.
- Installed vanilla examples and documentation were inspected under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/` and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

## Runtime inventory audited

### Standard Event 006 tags

The accepted `common/country_tags/006_independence_wave_countries.txt` roster contains 102 Event 006 X-tags. Each tag was checked at `gfx/flags/<TAG>.tga`, `gfx/flags/medium/<TAG>.tga`, and `gfx/flags/small/<TAG>.tga`, together with `_communism`, `_democratic`, `_fascism`, and `_neutrality` aliases in each size directory.

Inventory: 102 tags × 5 accepted names × 3 sizes = 1,530 runtime TGAs.

Result: 102/102 complete families, 0 missing ladders, 0 malformed files, and 0 path or basename errors.

### Route and formable basenames

The current runtime route audit covered 44 basenames × 3 sizes = 132 TGAs, consisting of the 40 current `common/countries/cosmetic.txt` entries plus the four YAK route basenames referenced by the current scripted route effects. The four YAK names are audited as runtime files but remain a parent-owned identity/wiring review item because no current cosmetic definition was found.

The accepted LCX package deliberately supplies one base ladder only, so missing LCX ideology aliases are not a defect. KCX, NUX, and RLX retain the five-name shared-design alias ladders documented by their package manifest. FORM-05 MIX and FORM-48 PFX/HBX alias policy remains package-defined and was not normalized here.

Result: 44/44 route/formable basenames have all three size files, 0 missing ladders, 0 malformed files, and 0 wrong runtime paths.

## Mechanical flag checks

The standard roster passed exact header, geometry, alpha, and payload checks for all 1,530 files.

| Runtime family | Count | Dimensions | TGA type/depth | Origin descriptor | Alpha | Payload |
| --- | ---: | --- | --- | --- | --- | --- |
| `gfx/flags` | 510 | 82×52 | type 2 / 32-bit | `0x08`, bottom-left | min=max=255 | 17,074 bytes |
| `gfx/flags/medium` | 510 | 41×26 | type 2 / 32-bit | `0x08`, bottom-left | min=max=255 | 4,282 bytes |
| `gfx/flags/small` | 510 | 10×7 | type 2 / 32-bit | `0x08`, bottom-left | min=max=255 | 298 bytes |

The route/formable audit passed exact headers, dimensions, payload lengths, and opaque alpha for all 132 files. Forty-four normal and 44 medium files use descriptor `0x08`; 36 small files use descriptor `0x08`; eight small files use descriptor `0x00`, all in the NAV and YAK route packages. Descriptor `0x00` is a valid bottom-left-origin convention used by installed vanilla small flags and is explicitly recorded by the NAV/Sakha package evidence, so these files were preserved rather than rewritten.

No accidental transparency, top-origin bit, upside-down pixel order, invalid TGA type, invalid depth, truncated payload, or wrong dimension was found.

### Alias and duplicate policy

All 306 standard tag-size families have exactly one SHA-256 value across the base name and four ideology aliases, proving byte-identical synchronization for the accepted shared-design policy. This is an alias result, not evidence that every identity is semantically cleared for play.

The previously identified 228 identical suffix files associated with unresolved BWX, chunk-3, NWE, and related ownership/provenance families were not deleted or rewritten. No vanilla/base flag was replaced, and no route-specific alias was collapsed.

Current concurrent-boundary files were rechecked without editing:

- `gfx/flags/AXX.tga` and its four aliases: `55b1dbc417cf1a5d14f45a6f1537c56baa3e6c192ce586e6c9b392db2b4e02cb` at normal size, `58ea23655f8d5a14ebe85d700aab3d7e1a02658ab2b09282eb14e9f41ded2c1a` at medium size, and `aaf2541128fe25dce539875795100a4384d5c805562332f02df4be5891fffde8` at small size.
- `gfx/flags/BLX.tga` and its four aliases: `002f71a61a30cfcff839c22e8fb19c8691c153c5fe7d0461952d0e8e765e7678` at normal size, `8fcf5c38394e3dc2134c89f64445c892e392d794b44791b39100118b69a70ec7` at medium size, and `8079d1e3bd470b81d0ed0112aedc69995325954ea44cbc5d2763c749bce29110` at small size.

The BLX package checksum ledger still records older hashes, so this is an owner/package reconciliation item rather than a safe mechanical replacement. AXX also has a documented prior concurrent hash change. Neither family was changed by this audit.

## Visual evidence

Every target family was opened through decoded contact sheets, not evaluated from dimensions alone.

Fresh current-worktree evidence is under `docs/assets/006_independence_wave/_tooling/flag_audit_2026_09_13/`:

- `event006_registered_flags_01.png` through `event006_registered_flags_06.png` show all 102 standard tags as normal, medium, and small base ladders; byte-identical ideology aliases were verified independently by SHA.
- `event006_cosmetic_route_flags_01.png` through `event006_cosmetic_route_flags_03.png` show 41 route/formable basenames across the three sizes.
- `event006_long_formable_flags.png` shows `IDEL_URAL_COMPACTX`, `VOLGA_URAL_FEDERATIONX`, and `MESOPOTAMIAN_FEDERATIONX` across all three sizes.
- `event006_changed_families_aliases.png` shows all five current normal-size AXX and BLX aliases.

The sheets show consistent upright orientation, clean flat fields, no clipped canvas, expected normal-to-medium-to-small reduction, and readable emblem colour masses at 10×7. The route small files using descriptor `0x00` are visually upright and match their package sheets.

Previously retained source/package sheets were also reopened for comparison: `event006_missing_flags_2026_08_02/contact_sheets/final_size_ladder_enlarged_contact_sheet.png`, `event006_missing_flags_2026_08_02_chunk3/contact_sheets/final_size_ladder_enlarged_contact_sheet.png`, `event006_missing_flags_2026_08_02_chunk_cox_ebx/contact_sheets/final_size_ladder_enlarged_contact_sheet.png`, `contact_sheets/006_nwe_generated_flags_contact_sheet.png`, `form01_02_04_flags_2026_07_15/contact_sheets/final_size_ladder_native_contact_sheet.png`, `form05_mediterranean_assets_2026_07_16/contact_sheets/006_form05_flag_sources_and_ladders.png`, `form09_balkan_federation_flag_2026_08_09/review_contact_sheet.png`, `form48_pacific_assets_2026_07_17/contact_sheets/006_form48_flag_sources_and_ladders.png`, and `iw043_iw058_generated_visuals_2026_07_18/contacts/flags/flags_ladders_contact_sheet.png`.

## Source, processed, final, and runtime evidence

No new visual source was selected and no new PNG, TGA, or DDS was generated by this audit. Existing package sources, processed masters, package TGAs, DDS round-trip evidence, contact sheets, and SHA ledgers remain authoritative.

The standard Event 006 source and runtime packages are recorded in `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/manifest.md`, `gfx_handoff.md`, and `metadata/flag_validation.json`, with the chunk-3 and COX–EBX packages in their corresponding `manifest.md`, `gfx_handoff.md`, and metadata files. NWE source and final evidence are recorded by `docs/assets/006_independence_wave/northern_western_europe_generated_art_gfx_handoff.md`, `generated_nwe_hashes.sha256`, and the `source_png/generated_nwe/flags/`, `processed_png/generated_nwe/flags/`, and runtime TGA paths named there.

Accepted route/formable source and final evidence was reviewed in these package manifests and handoffs: `form01_02_04_flags_2026_07_15`, `low_countries_form03_2026_07_15`, `form05_mediterranean_assets_2026_07_16`, `form09_balkan_federation_flag_2026_08_09`, `form39_melanesian_federation_identity_2026_07_27`, `form48_pacific_assets_2026_07_17`, `iw013_nav_flags_2026_08_13`, `iw031_kosovo_flags_2026_08_09`, `iw038_ruthenia_flags_2026_08_10`, `iw040_kuban_flags_2026_08_12`, `iw045_bashkiria_flags_2026_08_14`, `iw047_mari_flags_2026_08_14`, `iw051_sakha_flags_2026_08_15`, and `iw043_iw058_generated_visuals_2026_07_18`.

Those packages retain source masters, processed PNG previews, final package TGA ladders, and repository-converter DDS evidence where the package contract calls for it. DDS files are review/evidence copies; HOI4 flag lookup consumes the TGA basenames under `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small`.

The exact source paths, runtime basenames, selected current hashes, and package-level hash-ledger references are summarized in `docs/assets/006_independence_wave/_tooling/flag_audit_2026_09_13/gfx_handoff.md`.

## Status and blockers

Technical flag status is `PASS` for all audited standard and route/formable ladders.

Provenance and identity status remains fail-closed per the 2026-09-12 handoff:

- BWX remains `blocked` because the dated Soviet Mordovian ASSR reference does not attest a neutral Erzya–Moksha federal identity and the generated package lacks sufficient provider/licence evidence.
- The 14 chunk-3 families remain `blocked` or `needs_user_review` because generated source/provider terms and identity evidence are unresolved.
- NWE aliases ACX/AFX/AGX/AJX remain unresolved for ownership/compatibility; `AEX` is an Event 005 asset and was not touched.
- GLC remains a vanilla carrier with unresolved modern-shield provenance and redistribution terms.
- CHU opening/Volga Bulgaria and ASY route families remain generated route identities with unresolved provider terms and parent admission review.
- NAV, KOS, RUT, KUB, BSK, MEL, YAK, and MFX route packages retain their package-specific generated-source, attribution, route-admission, or prompt-evidence gates. They are not evidence of universal historical 1936 flags.
- YAK has four technically complete route ladders but no current `common/countries/cosmetic.txt` definitions; this is a parent-owned wiring/identity blocker outside this flag-only audit.
- FORM-03 LCX remains deliberately base-only; FORM-06 and later unaccepted formable candidates remain blocked. No missing fictional flag was generated because no accepted source brief authorized one.
- Planned or historical-only names such as `FER_INDEPENDENCE_WAVE_PROVISIONALX` and `ASX_INDEPENDENCE_WAVE_CONSTITUTIONALX` have no accepted current runtime source package in the ASSET-044 authority and were not created.

## Files changed by this audit

- Added the fresh decoded contact-sheet evidence under `docs/assets/006_independence_wave/_tooling/flag_audit_2026_09_13/`.
- Added `docs/assets/006_independence_wave/_tooling/flag_audit_2026_09_13/gfx_handoff.md`.
- Added this dated handoff.

No file under `gfx/flags/`, `gfx/flags/medium/`, or `gfx/flags/small/` was changed. No source package, processed PNG, final DDS, `.gfx`, gameplay, localisation, country, or spreadsheet file was changed. No staging or commit was performed.

## Parent follow-up

Keep all unresolved identities fail-closed until the provenance handoff is resolved, reconcile the stale BLX package checksum ledger in the owning package, decide whether and when YAK route cosmetics receive accepted definitions, and preserve the AXX concurrent-boundary hash unless the owning package explicitly reconciles it. The current technical flag audit does not authorize any of those identity or wiring changes.
