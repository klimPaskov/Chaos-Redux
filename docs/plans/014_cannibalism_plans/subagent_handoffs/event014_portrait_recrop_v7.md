# Event 014 sourced warlord portrait recrop v7 handoff

## Outcome

The sixteen parent-approved modern fictional HATE warlord identities were recropped from their immutable archived originals to exact 156x210 HOI4 portrait composition. The corrective pass makes each face prominent at native texture size while retaining head/shoulders or chest-up framing and the strongest available mask, paint, skull, bone, trophy, or weapon cue. No source identity, artwork, or character mapping was substituted.

This tranche remains the direct-source user-authorized branch. No ImageGen, RunPod, Meshy, Blender, archival or historical photo, generic replacement, repaint, redesign, or 3D portrait workflow was used. The user remains the only operator for any future RunPod HOI4-style final.

## Exact approved mapping

1. `leader_CBA_warlord_middle_east` -> UmCal Champion
2. `leader_CBA_warlord_south_america` -> UmCal Prince
3. `leader_CBB_warlord_middle_east` -> UmCal Warrior 1
4. `leader_CBC_warlord_south_america` -> UmCal Warrior 2
5. `leader_CBC_warlord` -> UmCal Warrior 3
6. `leader_CBD_warlord_north_america` -> UmGra Champion
7. `leader_CBD_warlord_south_america` -> UmGra Prince
8. `leader_CBE_warlord_north_america` -> UmGra Warrior 1
9. `leader_CBE_warlord_south_america` -> UmGra Warrior 2
10. `leader_CBE_warlord` -> UmGra Warrior 3
11. `leader_CBF_warlord_africa` -> UmKator Champion
12. `leader_CBF_warlord_oceania` -> UmKator Prince
13. `leader_CBF_warlord` -> UmKator Warrior 1
14. `leader_CBH_warlord_north_america` -> UmKator Youngblood
15. `leader_CBH_warlord_south_america` -> UmRak Champion
16. `leader_CBH_warlord` -> UmRak Youngblood

## Source, rights, and crop evidence

- [provenance_matrix.md](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/provenance_matrix.md) records each attributed Alkony source page, direct image URL, Adrian Smith attribution, CMON/CoolMiniOrNot credit, source-page archive, rights status, NoAI screen, source hash, crop box, source-crop hash, processed PNG hash, runtime DDS hash, identity rationale, and review verdict.
- The sixteen immutable approved source copies remain the `*_original.jpg` files under [selected](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/), byte-identical to the archived external HATE masters used for this recrop.
- The exact v7 source rectangles are recorded in the adjacent `*_source_crop.json` files and repeated in the matrix. They use the source's native 26:35 crop aspect and preserve pixels without stretching.
- The processed candidates are the adjacent `*_156x210.png` files. All are RGB, exactly 156x210, and contain no card border, text, UI, logo, or prison background.
- Entry 06 (`leader_CBD_warlord_north_america`) uses the approved `[304,100,616,520]` source rectangle. Its source crop remains immutable; only border-connected near-neutral white backdrop pixels were bounded-cleaned in the processed candidate. The exact operation and hash are recorded in [entry 06 backdrop cleanup evidence](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/leader_CBD_warlord_north_america_backdrop_cleanup_recrop_v7.md).

## Framing review artifacts

- [Before contact sheet](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/selected_16_contact_sheet_4x_mapping_order_before_recrop_v7.jpg) preserves the too-full-body v6 review state.
- [After contact sheet](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/selected_16_contact_sheet_4x_mapping_order_after_recrop_v7.jpg) shows the tightened v7 crops enlarged 4x with the mapping order.
- [Before/after contact sheet](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/selected_16_contact_sheet_4x_mapping_order_before_after_recrop_v7.jpg) pairs each v6 crop beside its v7 replacement.
- [Native 156x210 review sheet](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/selected_16_contact_sheet_native_after_recrop_v7.png) was reviewed at final texture dimensions. All sixteen faces are readable with head/shoulders or chest-up composition and preserved disturbing character cues.
- The named current review sheet [selected_16_contact_sheet_4x_mapping_order.jpg](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/selected_16_contact_sheet_4x_mapping_order.jpg) now contains the v7 after-recrops.

## Runtime installation and wiring

- All sixteen runtime files under `gfx/leaders/014_cannibalism/` were regenerated from the v7 processed PNGs with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 156 --height 210`.
- Each output is 131168 bytes, DDS legacy uncompressed BGRA, 156x210, and roundtrips to the source PNG pixels exactly. The full machine-readable evidence is [portrait_recrop_v7_validation.json](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/portrait_recrop_v7_validation.json) and [portrait_recrop_v7_validation.tsv](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/portrait_recrop_v7_validation.tsv).
- Before and after runtime hashes are preserved in [runtime_hashes_before_recrop_v7.tsv](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/runtime_hashes_before_recrop_v7.tsv) and [runtime_hashes_after_recrop_v7.tsv](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/runtime_hashes_after_recrop_v7.tsv). The per-alias DDS hashes are also repeated in the provenance matrix and contracts.
- Existing `interface/014_cannibalism.gfx` stable aliases already point to these sixteen runtime paths and required no edit. No character identity, traits, gameplay, localisation, event, focus, decision, country, or unrelated UI files were changed.
- The sixteen installed aliases retain the `source_placeholder/direct_source_2d` replacement state because these are approved direct source portraits, not user-supplied HOI4-style finals. `replacement_pending` is false for this direct-source installation branch; no user final was requested or operated by this worker.

## Protected-file proof

[protected_hashes_recrop_v7.tsv](../../../assets/014_cannibalism/portrait_source_recovery_v6/selected/protected_hashes_recrop_v7.tsv) records byte-for-byte equality before and after for every protected file:

- `gfx/leaders/014_cannibalism/hannibal.dds` — `5c48c9a5b503c3185dcb38ee1aabc403d7668094079b78a20010323930d10b88`
- `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` — `26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717`
- `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds` — `f67a1b33a1d4f9b9b1b5ec0d6fb716ad1f2342083e9992550b5dd7356f590587`
- `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds` — `f0dfa61ea29293f8393711f97eb67524d336cb6c2a2d55734c0c38484219d18b`

## Validation and remaining scope

- The v7 validator reports `PASS` for all sixteen portraits: source-master equality, exact crop rectangles, 156x210 PNG dimensions, DDS header/dimensions/masks/size, PNG-to-DDS decoded pixel equality, stable GFX path presence, and protected-file equality.
- The source evidence is attributed and archived, with `reference_only_user_authorized` rights status and no permissive-license claim. No explicit NoAI statement was found on the reviewed source page or direct image as of 2026-08-24.
- No replacement art was necessary. If a styled HOI4 final is requested later, the user must supply and review it; this worker does not operate RunPod.
- Live HOI4 session validation was not performed because the user owns live consumer review. The stable alias wiring and file-level runtime evidence are complete.
- No simplifications, identity substitutions, or unrelated edits were made. Concurrent worktree changes outside the owned portrait files and this handoff were preserved and are not part of the scoped commit.
