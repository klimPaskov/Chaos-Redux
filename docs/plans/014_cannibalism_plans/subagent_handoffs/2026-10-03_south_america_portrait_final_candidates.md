# Event 014 South America Portrait Final Installation Handoff

Disposition: the eight parent-approved South America DDS finals are installed at their existing runtime paths. The full Event 014 portrait matrix remains incomplete.

## Authority and review

The user reports that the parent approved source/framing and the final native DDS set for CBA-CBH, including selected CBD v02. The final review receipt is `docs/plans/014_cannibalism_plans/evidence/2026-10-03_south_america_portrait_parent_review.json`. Its scope is these eight regional finals within the full 56-portrait goal, not full-event or live-game completion.

CBD v01 remains preserved as rejected action lineage because its field spoon appeared intact. CBD v02 shows two jagged separated spoon-shaft parts in the same hand and is selected for both the processed PNG and canonical runtime DDS. The other seven candidates remain their parent-approved v01 sources without iteration.

The initial eight assets used one built-in native ImageGen call each. CBD received one additional parent-requested native edit using only CBD v01 as its edit target. Exact route paths, prompts, source dimensions, hashes, and lineage are in the asset package metadata. No CLI or API generation, RunPod, Meshy, Blender, or HOI4 process was used.

## Installed crosswalk

The selected DDS bytes were copied to the eight existing texture paths referenced by `GFX_portrait_CBA_warlord_south_america` through `GFX_portrait_CBH_warlord_south_america` in `interface/014_cannibalism.gfx` at lines 174, 182, 190, 198, 206, 214, 222, and 230. CBD's installed bytes derive from `processed_png/leader_CBD_warlord_south_america_156x210_v02.png`; its stable DDS basename remains `leader_CBD_warlord_south_america.dds`.

The complete source, processed PNG, candidate DDS, decoded-pixel, and runtime path/hash crosswalk is in `docs/assets/014_cannibalism/portrait_finals_2026-10-03/south_america/manifest.md` and `metadata/dds_roundtrip_audit.json`. The selected-source contact sheets are `review/south_america_native_4x2_contact_sheet_v02.png` and `review/south_america_nearest4_4x2_contact_sheet_v02.png`; the decoded DDS contact sheets are `review/south_america_dds_decoded_native_4x2_contact_sheet.png` and `review/south_america_dds_decoded_nearest4_4x2_contact_sheet.png`.

## Conversion and preservation receipt

All eight files were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` as 156x210 legacy uncompressed 32-bit BGRA, one image level, no mipmaps, and opaque alpha. Header schema, 131168-byte lengths, alpha, exact PNG-to-decoded-RGBA equality, unique file/pixel hashes, and contact-sheet pixel equality passed in `metadata/dds_roundtrip_audit.json`.

Immediately before installation, `metadata/runtime_preinstall_snapshot_2026-10-03.json` recorded all 60 Event 014 leader DDS paths and hashes, `interface/014_cannibalism.gfx`, and `common/characters/014_cannibalism_characters.txt`. Only the eight authorized South America target DDS files were backed up under `evidence/runtime_before_install/`. The installation receipt is `metadata/runtime_install_receipt_2026-10-03.json`; it records each preinstall hash, backup hash, candidate hash, and installed hash. Every installed DDS hash matches its parent-approved candidate DDS hash.

No runtime GFX or character file was changed. The two canonical static Hannibal DDS files and both animated Hannibal sheets are unchanged. No non-target DDS changed during the install window.

Sixteen North America and Oceania regional DDS paths changed between the original candidate-stage snapshot and this immediate preinstall snapshot, eight slots in each region. Their exact paths and earlier/preinstall SHA-256 values are listed in the install receipt as concurrent non-target changes. They were preserved without reset or rewrite.

## Remaining coverage

All 56 regional final DDS slots are now present and individually parent-approved across Europe, Asia, Africa, Middle East, North America, South America, and Oceania, eight per region. Africa and Middle East manifests still report the global cross-region uniqueness review as open, so this handoff does not claim full Event 014 portrait-matrix or event completion. This handoff also makes no engine-consumption or live-game acceptance claim. No simplification or South America slot omission was made, and no commit was created.

Skills used: `chaos-redux-event-assets`, its `references/portrait-production.md`, and the official built-in `imagegen` skill.
