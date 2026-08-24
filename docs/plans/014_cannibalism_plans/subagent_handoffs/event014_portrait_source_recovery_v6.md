# Event 014 portrait source recovery v6 handoff

## Outcome

The sixteen retained Event 014 warlord portrait aliases now use the parent-approved male HATE concept-art identities. Each source is a modern fictional two-dimensional image credited to Adrian Smith and hosted/referenced by Alkony from the CMON/CoolMiniOrNot HATE product family. Each source was archived, reviewed for attribution and NoAI restrictions, cropped without stretching to an exact 156x210 RGB portrait, converted to a HOI4-compatible DDS, and installed behind the existing stable alias.

The user-authorized direct-source branch was used for this tranche. No existing ImageGen portrait was used as a source, no ImageGen redesign was made, no RunPod was operated, and no Meshy, Blender, raw 3D render, or other 3D portrait workflow was used.

## Exact approved mapping

The runtime mapping order is also reproduced in the final contact sheet and the full provenance matrix.

1. leader_CBA_warlord_middle_east -> UmCal Champion
2. leader_CBA_warlord_south_america -> UmCal Prince
3. leader_CBB_warlord_middle_east -> UmCal Warrior 1
4. leader_CBC_warlord_south_america -> UmCal Warrior 2
5. leader_CBC_warlord -> UmCal Warrior 3
6. leader_CBD_warlord_north_america -> UmGra Champion
7. leader_CBD_warlord_south_america -> UmGra Prince
8. leader_CBE_warlord_north_america -> UmGra Warrior 1
9. leader_CBE_warlord_south_america -> UmGra Warrior 2
10. leader_CBE_warlord -> UmGra Warrior 3
11. leader_CBF_warlord_africa -> UmKator Champion
12. leader_CBF_warlord_oceania -> UmKator Prince
13. leader_CBF_warlord -> UmKator Warrior 1
14. leader_CBH_warlord_north_america -> UmKator Youngblood
15. leader_CBH_warlord_south_america -> UmRak Champion
16. leader_CBH_warlord -> UmRak Youngblood

## Source and processing evidence

- Full title, direct image URL, source-page URL, official CMON secondary URL, Adrian Smith attribution, rights status, NoAI screen, crop box, source hash, source-crop hash, final PNG hash, role-fit rationale, and PASS verdict are in [provenance_matrix.md](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/provenance_matrix.md).
- The sixteen immutable source copies are the *_original.jpg files under [selected](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/). The direct source URLs and archived HTML source pages are recorded in each co-located provenance contract and in the matrix.
- The sixteen exact final crops are the *_156x210.png files under [selected](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/). They are RGB, 156x210, preserve the 26:35 source aspect ratio, remove card borders/text/UI/logos, and retain head/shoulders/upper torso plus the strongest available bone, paint, trophy, or bloodied-weapon cue.
- The refreshed 4x4 visual review artifact is [selected_16_contact_sheet_4x_mapping_order.jpg](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/selected_16_contact_sheet_4x_mapping_order.jpg). Entry 06 is now on the same neutral dark background as the other fifteen portraits.
- Entry 06 backdrop evidence is [leader_CBD_warlord_north_america_backdrop_cleanup.md](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/leader_CBD_warlord_north_america_backdrop_cleanup.md). Its immutable source crop is unchanged; only border-connected near-neutral white background pixels were replaced with RGB [0, 0, 0] using connected-components detection and a 3x3 edge feather before the exact resize.

## Runtime installation

- The exact sixteen runtime files under gfx/leaders/014_cannibalism/ were regenerated from the selected PNGs with .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py using --width 156 --height 210.
- Every installed DDS is 131168 bytes, has a DDS header, width 156, height 210, 32-bit uncompressed RGBA-compatible masks, and a unique SHA256. Complete post-install hashes are in [runtime_hashes_after_install.tsv](../../../assets/014_cannibalism/portrait_source_recovery_v6/runtime_hashes_after_install.tsv); pre-install hashes are preserved in [runtime_hashes_before_install.tsv](../../../assets/014_cannibalism/portrait_source_recovery_v6/runtime_hashes_before_install.tsv).
- interface/014_cannibalism.gfx already contained all sixteen stable file aliases and required no edit. No character identity, traits, gameplay, localisation, event, focus, decision, country, or unrelated UI files were changed.
- The protected files and both protected sheets remain byte-for-byte unchanged. Their pre-install hashes are preserved in [protected_hashes_before_runtime_install.tsv](../../../assets/014_cannibalism/portrait_source_recovery_v6/protected_hashes_before_runtime_install.tsv).

## Validation result

- Sixteen PNGs validated as RGB 156x210 with unique hashes.
- Sixteen DDS files validated as 156x210, 32-bit uncompressed, 131168-byte outputs with unique hashes.
- All sixteen stable GFX DDS references were found in interface/014_cannibalism.gfx.
- Sixteen source-crop JSON packages parse, every processed hash matches its PNG, every filled provenance-contract hash matches its TXT, and no [REQUIRED] template remains.
- The final contact sheet validates at 2616x3568 RGB and was visually reviewed after the entry 06 dark-background cleanup.
- Protected Hannibal portrait and sheet hashes remain exactly: hannibal.dds 5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88; hannibal_wendigo.dds 26D7566F7B93D17C4D7FDE5B262AB8B6E4B04FBA0B862315404D6A33ABE34717; leader_CBL_hannibal_sheet.dds F67A1B33A1D4F9B9B1B5EC0D6FB716AD1F2342083E9992550B5DD7356F590587; leader_ZZZ_hannibal_wendigo_sheet.dds F0DFA61EA29293F8393711F97EB67524D336CB6C2A2D55734C0C38484219D18B.

## Rights and remaining risks

The source pages attribute the art to Adrian Smith and credit the image family to CoolMiniOrNot/CMON, but no permissive redistribution license or public-domain basis was asserted. Each contract records reference_only_user_authorized status. No explicit NoAI or AI-prohibition statement was found on the reviewed source page or direct image as of 2026-08-24. This is not a claim of unrestricted third-party licensing and remains the user-authorized source-art branch.

No simplifications or source substitutions were made. Female Shamans, group/product-layout images, generic miniature photos, raw 3D renders, modern civilian leads, undead/monster-only leads, and the previously deleted portrait files were not used. The only remaining external dependency is the parent’s final live-game review of the installed source-art portraits; no live HOI4 session was launched by this subagent.
