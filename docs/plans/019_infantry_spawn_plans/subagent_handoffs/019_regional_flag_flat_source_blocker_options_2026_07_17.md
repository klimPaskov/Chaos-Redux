# Event 019 regional flag flat-source blocker and approval options

> **Historical blocker, superseded 2026-07-18:** This document records the
> pre-route owner decision state. The owner selected the deterministic
> spot-colour route, and the current 7/18 candidate contains 91 independent
> full-flag raws, 91 spot masters, and the complete 273-row native/runtime
> ladder. Visual/runtime rows pass, but independent remediation re-audit,
> parent documentation/workbook reconciliation, and final completion audit
> remain pending. The rejected options and old `regional_variants/` paths below
> are archival evidence, not current blockers or source instructions.

Date: 2026-07-17

## Outcome

The requested 91-source regional flag regeneration is incomplete and blocked at source acceptance. Built-in ImageGen consistently introduced spatial tonal falloff, lighting, highlight, or dimensional shading into full-colour flag fields. Under `chaos-redux-event-assets` line 887, those results cannot be accepted as flat orthographic flag masters. Line 885 also forbids removing the defect with a solid-fill normalizer, aggressive palette quantizer, vector trace, or local recolour that becomes the design source.

- Accepted separate full-colour flat ImageGen masters: **0/91**.
- Regenerated source masters promoted to `regional_variants/`: **0/91**.
- Runtime TGA triplets rewritten: **0/91** (**0/273 files**).
- Further generation stopped after the materially different prompt/reference methods below failed the same acceptance gate.

## Existing finals remained unchanged

- The existing 91 files in `docs/assets/019_infantry_spawn/source_png/flags/regional_variants/` are SHA-256-identical to the 91 frozen copies in `regional_reference_inputs/`: **91 checked, 0 mismatches**.
- `regional_flag_checksums_2026_07_16.sha256` contains 273 runtime TGA records. The current files under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` match all 273 recorded hashes: **273 checked, 0 mismatches**.
- No normal, medium, or small flag file was overwritten during this tranche.

## Rejected full-colour candidate batch

Forty-two separately generated full-flag candidates were copied into `source_png/flags/rejected_generation_evidence_2026_07_16/full_colour_candidates/`. None is an accepted source. Every candidate used its own built-in ImageGen result and was rejected under the tightened flat-field review.

| Runtime tag | Built-in result | SHA-256 |
|---|---|---|
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE` | `exec-a052df77-f3ba-4c85-bb9a-4ae498be0ed7.png` | `65ffdceee6cdfa20925d195c1e8d0ccfe1d9b8d72e8886a34eb500681564d847` |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_MIDDLE_EAST` | `exec-f75d57fd-6ac0-4f7b-91d7-658a0afe2921.png` | `dc04b95de7d5cf840b1278e864c8c7f54af437c0616c4f088d3ca229d1392439` |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_AFRICA` | `exec-8413e861-61a5-4c25-ac6f-eae20e172dfb.png` | `3a9d380733538219f8073b0c305cc656eccb80e9f6b21dde80669ca7b60ea609` |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_ASIA` | `exec-042a3daf-a057-4857-af6a-918e7c8d803a.png` | `daafd537b65d9b1c0dddacaf4f9f88559e982e4b513acc79d66e5e31b7b0e302` |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_AUSTRALIA` | `exec-1fac6fa8-1d9e-48fd-9b95-548346928cfd.png` | `08b5ee8bb378b66242fab2a4eca4ec256a6b01cb52101b5d8ce276c543769adb` |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_NORTH_AMERICA` | `exec-b1e5d6a6-af99-472a-b6cd-4ef2cfa2d297.png` | `ea798d10873e633150acc18389180cd10f0d1ad9d71a160f1fe390d072077dee` |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_SOUTH_AMERICA` | `exec-7bba806e-eea4-4ea5-9dc8-dcf11b665b11.png` | `4d8eac002548a6d2182a7f24cd9c86d710c819177aacd4fc8e702fa7edbf8b31` |
| `INFANTRY_SPAWN_ZOMBIE_BASE_EUROPE` | `exec-c3dcc458-0866-405e-be3c-3a9052fd4f88.png` | `383dc889d8e8415bd90160dd355d5d378b13a77801fe150054f461d1b8d98315` |
| `INFANTRY_SPAWN_ZOMBIE_BASE_MIDDLE_EAST` | `exec-3c9e3eba-74d0-4f5d-b47e-200372f96f0b.png` | `c5b87c0e07ba2ae42877e5e31b4918dc485377694400d07999eff310448e621a` |
| `INFANTRY_SPAWN_ZOMBIE_BASE_AFRICA` | `exec-53b90007-e392-4a6b-9ba0-d2c8a660aabf.png` | `d58f8efb6804ab931bc13b17bb9e5da9414bb783ee47da432e623286fbcc067c` |
| `INFANTRY_SPAWN_ZOMBIE_BASE_ASIA` | `exec-f836ae36-270a-4e00-bb7a-b538a0c575ee.png` | `20b4eaf690505ef6c62e770066a74ee1821f574248a6d01714aabfe7383772e2` |
| `INFANTRY_SPAWN_ZOMBIE_BASE_AUSTRALIA` | `exec-3d448870-8274-4533-a038-7eb24786cef4.png` | `66afd2cedfb7f9ae23feaf72869914e7c502e14f8326d01e7e7655eed11b7f32` |
| `INFANTRY_SPAWN_ZOMBIE_BASE_NORTH_AMERICA` | `exec-b4e09b2f-4511-4aef-8199-0acf3352c551.png` | `1b8bf2f4e4dbdf1cfb13f639321219131f07a20a92cc2ca801d9fcf1ba66bd1d` |
| `INFANTRY_SPAWN_ZOMBIE_BASE_SOUTH_AMERICA` | `exec-09f0f3d6-f062-41a4-a063-609fce59a79e.png` | `35550422ab9b7bd85a12fc60e072f9e85fded7c1e1387be55559b004e2d690fe` |
| `INFANTRY_SPAWN_ZOMBIE_CLAIMANT_EUROPE` | `exec-f4c0fa1e-c49b-48ba-857d-593358307e3a.png` | `c962491b95dd8046bec2c3a55a44788c33de4dbe46e88800427eb2e4e02d8428` |
| `INFANTRY_SPAWN_ZOMBIE_CLAIMANT_MIDDLE_EAST` | `exec-4adc8d86-6ffb-46cd-834b-a1dd6d00324b.png` | `d7da57180408e0728317151ebcc5d020c6309419e2f6ad8cb9657fb485094629` |
| `INFANTRY_SPAWN_ZOMBIE_CLAIMANT_AFRICA` | `exec-a9e8fded-d6f1-4126-805c-f92d641780d4.png` | `3fddeff7fb9f3da284e43393849de758777d83a0e96d4d29724423f0d84a0ab4` |
| `INFANTRY_SPAWN_ZOMBIE_CLAIMANT_ASIA` | `exec-4d89dae0-8cb1-4926-8e26-4f6f904d05ab.png` | `55b4efd7b2f97479d32a5a1db60930a5641049ec645a56362478b69ef92dce97` |
| `INFANTRY_SPAWN_ZOMBIE_CLAIMANT_AUSTRALIA` | `exec-36141997-5f16-4b7c-b592-1df352e38a93.png` | `a4ced7b00f18cf4946809387c696c21125fed16567b377c50984c20fd837bf72` |
| `INFANTRY_SPAWN_ZOMBIE_CLAIMANT_NORTH_AMERICA` | `exec-a029a49d-969f-4934-9e24-830c54240221.png` | `337f9b9b680ad024525948524027e31c9bed69d6a29a1c320475f14b42e85d51` |
| `INFANTRY_SPAWN_ZOMBIE_CLAIMANT_SOUTH_AMERICA` | `exec-e24dfb72-3cc4-4fad-b485-df1ee05454df.png` | `7c869334757fcfc33187c67fa475adc8165f73b08a2e439488baf3512f9312fa` |
| `INFANTRY_SPAWN_ZOMBIE_COLLECTIVE_EUROPE` | `exec-a6f645f1-e525-4572-b4fa-e1cc004c2934.png` | `5dbe51b1e928465d0ac5cb915332102eaccf6cec26f8fa34aa2ef383451976ad` |
| `INFANTRY_SPAWN_ZOMBIE_COLLECTIVE_MIDDLE_EAST` | `exec-0699ed8e-94e3-4340-b775-9a1585db8123.png` | `58272e5205a7cbf5c674daa6e394b5aa408420de34ed042f54dac6a22b7e3eb1` |
| `INFANTRY_SPAWN_ZOMBIE_COLLECTIVE_AFRICA` | `exec-46d34fef-a997-43ec-8d9d-1d5db7b75513.png` | `6ed3ed41c014b1d1fc023c701a892ae16b1ff2da57e09974e6edc6b4c38d385f` |
| `INFANTRY_SPAWN_ZOMBIE_COLLECTIVE_ASIA` | `exec-f92022d8-05e3-43e0-906d-67bba2b89d58.png` | `a2ea654aec63bd47d95cf9a8511d3a24f3b1eeeb89ed3bc6aa82153272e846d0` |
| `INFANTRY_SPAWN_ZOMBIE_COLLECTIVE_AUSTRALIA` | `exec-cd1236f7-58a7-4ee4-b186-bde3e9f1f9f1.png` | `fc5918de90a529fff59f03382e68ba01ad97dfb7f598bbc5ddc7736fc2a5861e` |
| `INFANTRY_SPAWN_ZOMBIE_COLLECTIVE_NORTH_AMERICA` | `exec-096b99b0-317d-4639-b76d-5aef09fe64ed.png` | `df4c9c664b4c52205690a1caad3658545b4250ae6c51852055d615ca7cfa4324` |
| `INFANTRY_SPAWN_ZOMBIE_COLLECTIVE_SOUTH_AMERICA` | `exec-82ad84de-609f-414e-9f3c-237c41da963e.png` | `300835f7db411aa9277be289c5c856e81cbcd54f343e5403f46ba17dd6873ba9` |
| `INFANTRY_SPAWN_ZOMBIE_SPECIES_EUROPE` | `exec-cb2f8df6-bc36-4f5a-a1f1-992b7c1ed44f.png` | `c1f11ff6cc773325d5ff5f2290364840ec2c926f63e83540741fdcf835dfe2af` |
| `INFANTRY_SPAWN_ZOMBIE_SPECIES_MIDDLE_EAST` | `exec-6a7b002e-8a92-4bb2-88fe-a77346bbd0d2.png` | `4cffc5c1c1b3678dbbfacff88a9d886f72d9fa1188573fdc1b07c4ccb4bcda9a` |
| `INFANTRY_SPAWN_ZOMBIE_SPECIES_AFRICA` | `exec-e4cc71fe-c9b0-4511-ba18-dea9b7460c70.png` | `281485869256c7265e8e249b2e6c236ccf17965036ffe9fdcedfa1f5c33dfdb3` |
| `INFANTRY_SPAWN_ZOMBIE_SPECIES_ASIA` | `exec-64ee63da-5816-4410-9868-3872216c5342.png` | `25b9f0b3a281e5a21917729e5f4f1d13bb3d96b09d05ff1d19f058fcf24d9abe` |
| `INFANTRY_SPAWN_ZOMBIE_SPECIES_AUSTRALIA` | `exec-3d423424-500e-4387-950d-4a3760a353f9.png` | `64dd47199fa98df9e0f8e91b13b46762b5dd1b711ad93a74641fa01ad02949f4` |
| `INFANTRY_SPAWN_ZOMBIE_SPECIES_NORTH_AMERICA` | `exec-90e52ec9-f615-404e-a2d9-5e4f297bd3ac.png` | `eae2c34d7b47eab0664c17d220d8fffa47db753c2133331f2f22777f2c3464ab` |
| `INFANTRY_SPAWN_ZOMBIE_SPECIES_SOUTH_AMERICA` | `exec-a023fd4f-8f90-4e3b-8c30-219cbcf6b20e.png` | `6d05e276218252c3c5e4242c941cbe4f60a5fa082b7914a6f052685fbaa95e08` |
| `INFANTRY_SPAWN_GHOST_BASE_EUROPE` | `exec-2fa201c7-ad5f-4c41-ad95-991ec717a209.png` | `0796537b4745852c72b9f25188bfd44b16aa85265b87131c8ae5cd6241246fb6` |
| `INFANTRY_SPAWN_GHOST_BASE_MIDDLE_EAST` | `exec-cf299094-3b37-43c3-9f99-b62499901e9c.png` | `ffca1492a7c9785d53243030bc2b4cd8d74dcb430afdab44eb8f3673688897d1` |
| `INFANTRY_SPAWN_GHOST_BASE_AFRICA` | `exec-cbcb9a98-a0ed-46f8-a0a7-666e295f25dd.png` | `92f812d86e523e3b2818597c7d90517456767b93ca020bb5337f72cab0231d10` |
| `INFANTRY_SPAWN_GHOST_BASE_ASIA` | `exec-9e61a730-e741-45c0-9b44-08e6ff8d6be3.png` | `39e87de52456f93e5da4b4ae8e56092d7df833b41b44d68f5b26b40d871689e7` |
| `INFANTRY_SPAWN_GHOST_BASE_AUSTRALIA` | `exec-e9b015c0-0d4d-4490-b0bf-a9d2e5813bc2.png` | `6c7a3cd6b17d3f79b1e498a9490339797b04ba9df65ab3399e14096699e8dfef` |
| `INFANTRY_SPAWN_GHOST_BASE_NORTH_AMERICA` | `exec-3eb5804b-75d1-44d9-acea-5380eaad49cd.png` | `4ea3d41e262a90265790d22b51597db8900952fdda0fe67f7521186e4e2db37a` |
| `INFANTRY_SPAWN_GHOST_BASE_SOUTH_AMERICA` | `exec-3c49f1c5-d49b-4121-918c-a570348df24a.png` | `bcc2fc0eb5d5670629cfed0229cad1d4b753db2650688b1aafc717aeebdecdcc` |

## Rejected method pilots

All retained pilots live under `source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/`. They are test evidence only.

| Pilot file | Built-in result | SHA-256 | Verdict |
|---|---|---|---|
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_flat_test.png` | `exec-e1f41718-9397-406e-8292-9ae647b1eae4.png` | `e8e4903f7a614216be4c1df5094ada5cf1d6136352a8c3ac3576d61fe57e6ce4` | Exact four-ink vector/prepress prompt retained tonal lighting and changed the central identity. |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_flat_edit_test.png` | `exec-071217ad-0285-40b7-826d-042d2a308d39.png` | `0f597614c8fbdbbdc9487c6b9284cd1f4f831d48935884a1a7c3203417dc54c3` | Geometry-locked flattening edit changed symbols and retained tonal falloff. |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_indexed_test.png` | `exec-c74d35fc-f319-4716-8e5a-195eaeacb2a7.png` | `2c1f23bfb5b583bf13bddbd71acad70eac3320f1851953ed58d27ffa9482ee44` | Palette-indexed sprite language retained a lit crimson field. |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_binary_test_2.png` | `exec-6b8cb977-0fe6-483c-9981-b78a7ae84c46.png` | `1063a5fdcb6de6f29160dba755905117b0c7e171b50c5132f37ac9e63f35bd8d` | Flat source, but monochrome; rejected as an unapproved route-palette simplification. |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_twoink_test.png` | `exec-09c04234-e576-4d1b-b559-9f80a5b84690.png` | `0ab5d0f60e24f5d32935f8d11cbd55f8d49a624036de2755c02c27a274195a96` | Crimson/ivory two-ink prompt retained spatial falloff. |
| `INFANTRY_SPAWN_GHOST_BASE_EUROPE_binary_test.png` | `exec-37a4485f-574b-44d7-9d69-3671e7407e47.png` | `b823e47fa57381e4d2c20907909b249ed2c09d3f27105988b380088136a99d01` | Flat source, but monochrome; rejected as an unapproved route-palette simplification. |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_colored_print_pilot.png` | `exec-ede25046-1fb6-4ea3-90b7-619260a4eb06.png` | `3cc7d5e5129260765b24319461baa7f8f0028449e675c881773ddf4daec62cc8` | Three-ink linocut registration proof retained red radial falloff and shaded emblems. |
| `INFANTRY_SPAWN_ZOMBIE_SPECIES_AFRICA_colored_print_pilot.png` | `exec-c4a379bf-6d49-4279-8e62-839173b2954a.png` | `6f7561e65b84633472ff4591a1876eeb41dfb7e6cd823b0606866e5ddf137bc6` | Screen-separation proof retained cream and red shading. |
| `INFANTRY_SPAWN_GHOST_BASE_AUSTRALIA_colored_print_pilot.png` | `exec-d8b237f7-87ea-4478-9db3-697e7753b5dc.png` | `5163be0cd8c0b534efca104e572d56d8391fb57bb861aae79414320899f5aceb` | Pochoir proof retained strong blue falloff and shaded gold/white shapes. |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_dual_reference_pilot.png` | `exec-2795b439-96db-4d83-916f-257aea833106.png` | `2c4c6bcbcb20283e06a2c12f7dfa6ad977d63692fe3932c0f14b017993af9a3e` | Design plus flat-vanilla-style reference still produced vignetted red/black fields and shaded emblems. |
| `INFANTRY_SPAWN_GHOST_BASE_AUSTRALIA_dual_reference_pilot.png` | `exec-362ae5a6-6bea-4c69-8d17-560d076557da.png` | `62d6f685259973c8bd6bfa4ebcab4c92b09ba99c4dd5f3907bd9cf7ea4c337f7` | Design plus flat-vanilla-style reference retained blue, white, and gold tonal variation. |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_cel_color_key_pilot.png` | `exec-1e8e72ea-d087-4262-9273-b9672a6d4a3a.png` | `52448edda3ef38dba7fa19b06764ea2f12593d278a324f7adf23cc7566aa5773` | Palette-indexed cel colour-key language retained red radial falloff and shaded shapes. |
| `INFANTRY_SPAWN_ZOMBIE_SPECIES_AFRICA_cel_color_key_pilot.png` | `exec-841987e3-6220-407d-b24e-e5e0610b5da8.png` | `635d64f72035631c10c94970946b9fbed6103a3aeaad09d375afeb9d4c60a67e` | Cel colour-key language retained tonal variation in bone and red fields. |
| `INFANTRY_SPAWN_GHOST_BASE_AUSTRALIA_cel_color_key_pilot.png` | `exec-e8783654-760f-423f-a248-df5ed8f2e4b3.png` | `45f37e3817a68104045914d48d14ea880ec052567a12061e67eae8472f0bd262` | Cel colour-key language retained a strong blue gradient and shaded white/gold regions. |

`vanilla_flat_style_reference.png` is a mechanical PNG view of vanilla `ARM.tga` used only as the second rendering-style reference for the dual-reference test; SHA-256 `f95ec564a8b04fd83343b83eb387f16adeac544c0e27d632c87b5ac6d8bbd7c3`.

Two earlier claimant-Europe tonal pilots (`exec-d47eaabb-b013-4b06-b687-6f38e55b2f78.png` and `exec-915cb14d-5903-4e79-bd39-92ef4df32457.png`) were rejected before repository retention. No-output safety stops occurred for request ids `af439f81-d013-4f9f-9179-b05451ff7513`, `e5617fdb-807e-428a-bbb0-56c2bb77febd`, `e5e01b9e-25f8-4e72-a27c-4d5e71e1ae80`, `87d7d811-1eef-47b0-b4a2-00177b45b5b6`, `f525d313-1db6-4754-9df7-4a37d247bc3b`, and `3d794a4c-a55a-473a-931b-e7acaa702ed5`; successful neutral-worded retries were still subject to visual rejection.

## Fixed 27-slot comparison-sheet cleanup

The legacy `contact_sheets/event_019_portrait_vanilla_comparison_contact_sheet.png` human-reference presentation was retired. Its pixels were replaced with a 1800x2772 formation-only source/runtime review containing:

- 20 claimant army/muster sources beside their runtime-size outputs;
- 6 derivative massed-host sources beside their runtime-size outputs;
- 1 neutral unassigned-muster source beside its runtime-size output.

No human leader reference panel remains. Active mentions were removed or rewritten in the asset manifest, the 27-slot crosswalk, and the fixed-slot regeneration handoff. The 27 fixed source, processed, and runtime identity assets themselves were not modified.

## Files changed by this subtask

### Documentation and review surface

- `docs/assets/019_infantry_spawn/manifest.md`
- `docs/assets/019_infantry_spawn/notes/claimant_portrait_asset_crosswalk_2026_07_16.md`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_full_portrait_regeneration_handoff_2026_07_16.md`
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_portrait_vanilla_comparison_contact_sheet.png`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_flag_flat_source_blocker_options_2026_07_17.md`

### Frozen references: 91 files

Created `docs/assets/019_infantry_spawn/source_png/flags/regional_reference_inputs/INFANTRY_SPAWN_<IDENTITY>_<REGION>_source.png` for every Cartesian-product row below (13 identities times 7 regions equals 91 exact files):

- identities: `CLAIMANT_BREAKAWAY`, `ZOMBIE_BASE`, `ZOMBIE_CLAIMANT`, `ZOMBIE_COLLECTIVE`, `ZOMBIE_SPECIES`, `GHOST_BASE`, `GHOST_CLAIMANT`, `GHOST_COLLECTIVE`, `GHOST_SPECIES`, `GOLEM_BASE`, `GOLEM_CLAIMANT`, `GOLEM_COLLECTIVE`, `GOLEM_SPECIES`;
- regions: `EUROPE`, `MIDDLE_EAST`, `AFRICA`, `ASIA`, `AUSTRALIA`, `NORTH_AMERICA`, `SOUTH_AMERICA`.

### Rejected full-colour candidates: 42 files

Created `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/full_colour_candidates/INFANTRY_SPAWN_<IDENTITY>_<REGION>_imagegen_raw.png` for every combination of these six identities and all seven regions listed above:

- `CLAIMANT_BREAKAWAY`
- `ZOMBIE_BASE`
- `ZOMBIE_CLAIMANT`
- `ZOMBIE_COLLECTIVE`
- `ZOMBIE_SPECIES`
- `GHOST_BASE`

### Rejected method evidence: 15 files

- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_binary_test_2.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_cel_color_key_pilot.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_colored_print_pilot.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_dual_reference_pilot.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_flat_edit_test.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_flat_test.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_indexed_test.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY_EUROPE_twoink_test.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_GHOST_BASE_AUSTRALIA_cel_color_key_pilot.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_GHOST_BASE_AUSTRALIA_colored_print_pilot.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_GHOST_BASE_AUSTRALIA_dual_reference_pilot.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_GHOST_BASE_EUROPE_binary_test.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_ZOMBIE_SPECIES_AFRICA_cel_color_key_pilot.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/INFANTRY_SPAWN_ZOMBIE_SPECIES_AFRICA_colored_print_pilot.png`
- `docs/assets/019_infantry_spawn/source_png/flags/rejected_generation_evidence_2026_07_16/pilot_methods/vanilla_flat_style_reference.png`

No gameplay, localisation, `.gfx`, specification, workbook, CSV, processed regional PNG, regional contact sheet, validation JSON, checksum file, or runtime TGA was changed.

## Approval decision boundary

Work can resume only after one of these explicit decisions:

1. **Keep the current rules and provide a source-authoring capability that emits full-colour, spatially constant ImageGen fields.** Then generate all 91 separately, visually accept every raw, and only afterward process the three runtime sizes. This is the only option that satisfies the current request and skill unchanged.
2. **Explicitly amend the flag-processing rule to permit a documented deterministic spot-colour normalization/recolour pass on each independent full-flag ImageGen result.** The unmodified generated result and processed master would both be retained with exact arguments and hashes. This is currently prohibited by line 885 and cannot be assumed.
3. **Explicitly approve a monochrome two-ink regional package.** Two binary pilots achieved the flat-field requirement, but this changes the established route palettes and was rejected during parent review. It requires an explicit design change.
4. **Explicitly replace the separate-built-in-ImageGen requirement with another authored source mode, such as separately commissioned flat vector masters.** This changes the user request and the current generated-flag rule, so it cannot be inferred.

Accepting the current shaded candidates is not an approval option under the existing flat-flag contract.
