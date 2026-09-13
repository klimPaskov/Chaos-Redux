# Event021 achievement alpha-edge repair handoff

Status: the two v2 repaired states were parent-reviewed and promoted. The exact promotion record is `docs/assets/021_random_civil_war/validation/alpha_edge_repair_2026-09-02/parent_promotion_v2.json`.

## Ready pair

The following two parent-accepted not-eligible candidates are byte-frozen under `docs/assets/021_random_civil_war/validation/alpha_edge_repair_2026-09-02/stable_parent_ready/`.

| Achievement id | Sprite id | Source candidate SHA-256 | Processed SHA-256 | Final PNG SHA-256 | Final DDS SHA-256 |
| --- | --- | --- | --- | --- | --- |
| `021_random_civil_war_fractals_of_sovereignty_not_eligible` | `GFX_achievement_021_random_civil_war_fractals_of_sovereignty_not_eligible` | `E0BD3175315822F95EC0D2FC78E6C24A7AC957A3FE84712268E5620510179C14` | `168BB117E317CD630209894615528B835C691549072DBF276C571B8BCA21BEDC` | `D9BB3D8ED79983E9BE02B4778CF367554A42482AE37295BB18B7BEFB4EB7BDD5` | `4AC42D6B4FEA300B32AE17E0E5CC0B4E04D577CA324BCE36D44F377173F3010E` |
| `021_random_civil_war_war_within_a_war_not_eligible` | `GFX_achievement_021_random_civil_war_war_within_a_war_not_eligible` | `B1D0DC96C5BAFA444AA794E19D1BA4D5E83F79FC66B77BF4B97963A9D975CBCA` | `BF5598B9995AD6C41D75B1946326040E34A70671959E87628D86BCEB60BCC970` | `F46DDF563D23A3D96BD27D56BD6D545F6551005448FD022A16AB77C00455300E` | `90C48A4502BFDA8DB63C1D10D76FE1359D496ED07FFF2DEEFE1F53CDEA0ED653` |

All frozen DDS candidates are strict 64x64 legacy BGRA files of 16,512 bytes. The parent can promote the frozen `final_dds/` files to the corresponding runtime destinations listed in [promotion_scope.json](../../../assets/021_random_civil_war/validation/alpha_edge_repair_2026-09-02/promotion_scope.json). The frozen file inventory and hashes are also in [stable_parent_ready/manifest.json](../../../assets/021_random_civil_war/validation/alpha_edge_repair_2026-09-02/stable_parent_ready/manifest.json).

Fractals not-eligible uses the existing alpha-treated source lineage at `docs/assets/021_random_civil_war/source_png/achievements/021_random_civil_war_fractals_of_sovereignty_not_eligible.png`. War Within not-eligible uses the accepted deterministic fallback lineage at `docs/assets/021_random_civil_war/processed_png/achievements/fallback/021_random_civil_war_war_within_a_war_not_eligible_checkerboard_fallback_source.png`.

## Former parent-rejected pair

The v1 candidates remain explicitly non-promotable evidence and are not represented in the frozen folder. Their separate v2 candidates were reviewed and promoted as recorded below.

| Achievement id | Status | Defect |
| --- | --- | --- |
| `021_random_civil_war_fractals_of_sovereignty_grey` | `V1_REJECTED; V2_PROMOTED` | V1 retained a thin light-gray matte contour. V2 localized shell removal was parent-reviewed on dark/light source, processed and decoded-DDS boards, preserving the internal silver bevel. |
| `021_random_civil_war_the_terms_hold_not_eligible` | `V1_REJECTED; V2_PROMOTED` | V1 retained broad white matte residue in the lower rifle/ribbon/X gaps. V2 localized component removal was parent-reviewed on dark/light source, processed and decoded-DDS boards, preserving the subject and red cross. |

The v1 rejected artifacts and hashes remain in the current validation tree, and the former all-four scope is preserved as [promotion_scope_v1_historical.json](../../../assets/021_random_civil_war/validation/alpha_edge_repair_2026-09-02/promotion_scope_v1_historical.json). The v2 follow-up candidates are separately recorded in `rejected_v2_scope.json` and the parent promotion record; no v1 artifact was promoted.

## Rejected v2 review package

The two rejected states now have separate v2 source, processed, triplet, final DDS, decoded DDS, and dark/light review paths. Both remain `PENDING_PARENT_REVIEW`; neither is a promotion claim.

| Achievement id | v2 source candidate SHA-256 | v2 processed SHA-256 | v2 final PNG SHA-256 | v2 final DDS SHA-256 | Repair and review state |
| --- | --- | --- | --- | --- | --- |
| `021_random_civil_war_fractals_of_sovereignty_grey` | `2555DEE2A7B46ED71822AA65096914A76747DFD13E79A91910C55CE08F6B872E` | `537AD19B49FCB487C7767C3B0ACB06926ADFC0A57B766D79BCBE5813F25F6FA3` | `9BD8460F54060EE7AB96883EDDACFF3480BB3685EC829DF49342636773107B2B` | `8A80A3375A676F2D07EEA80417DF41DDC2696EB73C01D792B519AD4E91E4BE1B` | Localized neutral outer-alpha shell removal, chroma ≤24, luma ≥140, source-alpha distance ≤2, 9,306 source-alpha pixels removed. Parent must confirm the matte contour is gone without loss of silver bevel. |
| `021_random_civil_war_the_terms_hold_not_eligible` | `E95545F8B8E47A53421EA46E5EC9B55A13DF95CD2D7EA9744F577828D0D04DA4` | `FCF6DC99BE5A986A1E8D24F54C075B56BA7002E222487AD533A856A17DF42BB6` | `8858DF17356E93820F2BFB299A2896D7F9882B2BEDD936071FF5F652F8041661` | `E5CF14418360C7249EA0EA87F523D43CA331352C6DF69C9DBDF2DEE99EF2AA70` | Localized neutral component removal in the four inspected ROIs, chroma ≤24, luma ≥200, enclosed luma ≥235, 18 components and 5,365 source-alpha pixels removed. Parent must confirm the lower-rifle/ribbon matte gaps are clean without subject loss. |

The v2 final DDS files are exact 64x64, one-level, uncompressed legacy BGRA files of 16,512 bytes. Strict processor audits passed source-layer/template equality for both triplets, and the v2 evidence report records processed-to-Lanczos, final-PNG-to-DDS, and final-to-template equality. This is technical integrity evidence only, not a visual pass.

Exact evidence is under [reviews_v2_evidence](../../../assets/021_random_civil_war/validation/alpha_edge_repair_2026-09-02/reviews_v2_evidence/): `source/{dark,light}/` contains native 1,254px original and candidate composites; `processed/{dark,light}/` contains native 64px and 4× reviews; `final_png/{dark,light}/` contains native and 4× final-PNG reviews; and `final_dds/{dark,light}/` contains native and 4× decoded-DDS reviews. The strict decoded DDS PNGs are under `decoded_dds_v2/`. The exact paths and hashes are in [rejected_v2_scope.json](../../../assets/021_random_civil_war/validation/alpha_edge_repair_2026-09-02/rejected_v2_scope.json) and [v2_evidence_report.json](../../../assets/021_random_civil_war/validation/alpha_edge_repair_2026-09-02/reports/v2_evidence_report.json).

The original source lineage remains untouched: Fractals grey is based on `docs/assets/021_random_civil_war/source_png/achievements/021_random_civil_war_fractals_of_sovereignty_grey.png`, and Terms Hold not-eligible is based on `docs/assets/021_random_civil_war/source_png/achievements/021_random_civil_war_the_terms_hold_not_eligible.png`. Native transparent ImageGen repair attempts had already failed validation, so this package uses only the permitted least-destructive deterministic alpha fallback; no alternate generator, broad regeneration, stable-pair write, or runtime write was used.

## Scope and provenance

This handoff covers only the four named achievement states. The five other triplet outputs are evidence-only companions: `021_random_civil_war_fractals_of_sovereignty`, `021_random_civil_war_the_terms_hold`, `021_random_civil_war_the_terms_hold_grey`, `021_random_civil_war_war_within_a_war`, and `021_random_civil_war_war_within_a_war_grey`.

The source, processed layer, final PNG, decoded DDS, and dark/light reviews for the accepted pair remain in the validation tree. The exact templates and unchanged red-cross overlay were retained through the achievement triplet processor; no GFX, gameplay, shared manifest, old source, or runtime file was edited.

Native transparent ImageGen repair attempts were rejected where they changed canvas/alpha broadly, produced opaque checkerboard output, or changed subject identity. The accepted War Within source retains the previously recorded least-destructive local fallback with the original source preserved. The pending pair may receive only localized, least-destructive alpha repair after individual dark/light source and native-size review; no broad regeneration is authorized by this handoff.

This is not certification of the whole Event021 asset family. The two repaired states are promoted based on the parent review described above; all other Event021 owned and reused asset rows still require their own coverage and consumer evidence.
