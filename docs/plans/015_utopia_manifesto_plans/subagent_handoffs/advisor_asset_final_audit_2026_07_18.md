# Event 015 advisor and visual-asset final audit — 2026-07-18

## Verdict

**PASS.** I found no P0/P1/P2 asset defect and made no correction to the visual package. The active v5 advisor package is independently visually approved, processed through the required reusable renderer, decoded from the installed DDS files, and exact-pixel verified. The 21 active ImageGen flag compositions and four institutional tableau masters have independent built-in ImageGen source evidence. The Choice and Assignment balance-transition packages meet the frame-by-frame animation contract.

The processor-side advisor record intentionally remains `candidate_requires_visual_approval`: the processor is not allowed to self-approve. The separate approval record and installed validation are the authoritative completion evidence.

## Scope and source-of-truth files

I read the parent asset prompt/handoffs and the following active package surfaces:

- `docs/assets/015_utopia_manifesto/manifest.md`
- `docs/assets/015_utopia_manifesto/gfx_handoff.md`
- `docs/assets/015_utopia_manifesto/icon_animation_handoff.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/asset_workflow_and_identity_regeneration_handoff_2026_07_15.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/advisor_icon_correction_handoff.md` (historical context only)
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/advisor_hoi4_style_gap_audit_2026_07_16.md` (historical prior failure only)
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/asset_completion_final_requirement_reaudit_2026_07_16.md` (historical static audit only)
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/advisor_validation_2026_07_16.json`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/approvals/advisor_v5_independent_visual_approval_2026_07_16.json`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/advisor_installed_validation_2026_07_16.json`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/advisor_portrait_source_manifest.json`
- the retired advisor dossier asset kit
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/imagegen_source_evidence_2026_07_15.json`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/flag_identity_validation_2026_07_15.json`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/institutional_portrait_validation_2026_07_15.json`
- both animation directories under `docs/assets/015_utopia_manifesto/animations/utopia_balance_to_choice/` and `.../utopia_balance_to_assignment/`

Required asset skills read:

- `.agents/skills/chaos-redux-event-assets/SKILL.md` — SHA-256 `CE0A2EDFA691F1896AADE1ED6A3EA261C8D19813C74BFFCC38ABB9200005398D`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md` — SHA-256 `6A4E68DC4E5A89F0B7B8FC8984C0B9CB64665046EAEFD728BD41056375CB0D98`

Subagent scope restriction: I did not read repository `AGENTS.md`, the offline wiki, vanilla gameplay files, or vanilla documentation. This was an asset-only visual/provenance audit; the named Chaos Redux visual reference folders and asset skills were the applicable references.

## Advisor dossier audit

### Renderer/provenance contract

- Processor: `the retired portrait-processing utility`, SHA-256 `E248979F21784C016E69C5458B9925C32177D6AF29F2CCA1A82BFAAFFBE1F23C`.
- Processor metadata is v5.0, target `65x67`, Python `3.9.12`, Pillow `11.1.0`, and records the visible-art contract `crop_grade_resize_angle_alpha_shadow_composite_validate_export_only`; frame and paper are ImageGen-authored overlays, not procedurally drawn card art.
- Converter: `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, SHA-256 `D8AA0BA6A16BA8B6B698CCD6CF599B90E81DB6F6C6132009F07115C728F6B8A0`.
- Source portrait manifest SHA-256 `AE2566DD1C3D2E8C2A522908110AB0A970A1911E23F454A091BF6272B26DBE95`; all 16 source records are unique built-in ImageGen outputs, exact source PNG copies, and `approved_for_processing` with explicit crop/face boxes.
- Overlay manifest SHA-256 `8F355B36BA2A3A621C8B8E4AD0B1048EC50737E352F1D6D1A02A79AE4DD0C0DB`; frame and paper roles are separate built-in ImageGen sources with pinned alpha cleanup, not a primitive redraw.
- Current candidate validator SHA-256 `A9F66F9EC050FA032E3CE9C66226631AD00498F9CDD355B090521BD81D31090B`; its processor SHA is `E248979F21784C016E69C5458B9925C32177D6AF29F2CCA1A82BFAAFFBE1F23C`, render config SHA is `E9F8D54D1EA7FC8845BF22675C09686ACC7196556A56F96F5A1B46268B134637`, pinned alpha SHA is `5D33AFDD1ADC0349E33B52BB141DDD1449107FD34727D19FCC45BCD7809D2993`, and paper-family SHA is `C751CBE5F1178C8B894C56A4CEBE01BB4DAE88AE859B7238C2C68F39A6224DBC`. All 16 candidate reconstruction, identity, face/background, paper, style-band, and unsupported-RGB gates pass.
- Independent visual approval record SHA-256 `E68C0B4900CB725EDF430A3DB61514554FF9581972B416E7A033435282D5A44E`; reviewer is `/root/advisor_visual_review`, separate from producer. It records native and 4x six-reference approval for all 16 cards.

### Visual criteria and result

I inspected the 16-card enlarged nearest-neighbour contact sheet and the canonical vanilla advisor reference contact sheet. At final-size/readability scale the cards have distinct faces, readable silhouettes, consistent tilted charcoal dossier frame, pale memo/paper insert, transparent unused corners, no white halo, no fake checkerboard, no clipped face, no holes, no modern-photo residue, and no generic/simple-shape substitute. The per-asset comparison for `advisor_utopia_manifesto_advocate_of_limits` also passes against all six canonical references. The enlarged review sheet SHA-256 is `82B232BA1E0978019459523973C3674E9A2D35A1CD8FE4CC1D17B33B64241C94` (same decoded contact-sheet SHA).

The visual family is a close vanilla-style dossier match: one human portrait, dark angled card, memo/paper accent, transparent corners, and strong small-size contrast. I observed no concrete frame/paper mismatch requiring regeneration. Literal pixel identity with vanilla is neither expected nor claimed; the pass is a visual-family/readability approval supported by the independent approval record.

### Installed DDS proof

`advisor_installed_validation_2026_07_16.json` SHA-256 `92C8F84195971107ECE01BAECDCA9BBAB32C2CBAB744EFB60E5792169222B4A8` reports `passed`, 16 approved assets, visual approval present, exact package/runtime byte equality, exact decoded DDS RGBA equality to approved PNG, one-level uncompressed BGRA 32-bit, and `65x67` dimensions.

I independently parsed every package DDS and runtime DDS. For all 16: file length is `17,548` bytes (`128 + 65*67*4`), header is one-level uncompressed BGRA (`pfsize=32`, `flags=65`, `fourcc=0`, `bitcount=32`, masks `R=0xff0000 G=0xff00 B=0xff A=0xff000000`, caps `0x1000`), runtime bytes equal package bytes, decoded RGBA equals processed PNG RGBA, decoded verification PNG equals processed PNG RGBA, and alpha spans `0..255`.

Per-asset approved PNG SHA / installed DDS SHA:

| Identifier | Approved PNG | Installed DDS |
| --- | --- | --- |
| `advisor_utopia_manifesto_advocate_of_limits` | `aabb2128972197a614d7d272cb42065825b6c3775b283084c62244d3ec03ba68` | `cb32182ce42b3ee633ecafa549b9f35e13d52471cd99a108225f6b3a53d5b383` |
| `advisor_utopia_manifesto_chief_surveyor` | `bacf1a0abdf64d925d809ea6a8df58b31695badafdcb3a2ff5ae0fdd9e5ce9e4` | `3b6f269e929c90086425083e471ac400b3ac7d235d99b392e185da8bd7821796` |
| `advisor_utopia_manifesto_civic_engineer` | `68c996cc6811bcfe4d0f06de70cacb793a14a48280372c18a304483e479c9a02` | `40ba783849117d08330d23e9efeda5ac18ffe32e1ac4a85d7e2ab3f37a4827df` |
| `advisor_utopia_manifesto_constitutional_jurist` | `8ec6c7873b360d029d3c427622423604ea40fdcfae8c1859683c0076091569ac` | `6f01df69c5f2eaa3e170a84b27ab495648610813f6cdc166f559eca1627412a6` |
| `advisor_utopia_manifesto_contract_broker` | `4d3be76ba2f74dea32cde769a4857ecd53e9d0b94feff8d1cc27982b74698f94` | `04d31ae3376e4e6688048d0a4969ecfb77df3dc9f6b6d17195aaf7d6cb8191bc` |
| `advisor_utopia_manifesto_council_organizer` | `4a2ca6d361f2cae91cb966a2b1f0a5564732b1e7bd72adea42c57e64b8aa5e76` | `34c5d0b22f55b00201b5d2df4f8fd0b774f91ba886efbacb31474b194f84177c` |
| `advisor_utopia_manifesto_general_provisioner` | `1a632dcf44f2962a349c535327623812c00afba5be3083e523eece6126652293` | `dafdf0fd0942150eea93abf40caa1bddfad933b2c226f4350702066f98bd8fc1` |
| `advisor_utopia_manifesto_interpreter` | `feb260d288e438190ac59bbc1faaebc5c77cf91a33b89b5b830adf896d45caf9` | `d00d8db11a3165de7444976be684925817c5dc4228aa717f1723eddea469a4e4` |
| `advisor_utopia_manifesto_keeper_of_stores` | `4b46432011983666501032b5012aeea1dc1fa8b6961fc65622acb5221a68cc0c` | `aac081f4cfc4d07472bc48f6d1ed6232e4c8bc3157830321e00be2498a4c7664` |
| `advisor_utopia_manifesto_league_envoy` | `3bdbb475ee0d44edafbf622da20d3b76b489ae3233ed6da39521e31246a6fd69` | `56cf040a0b08d22032697050404591c7cff2ac8bf17c5b2d7f280e56c8fe58e4` |
| `advisor_utopia_manifesto_public_auditor` | `372cb012248a87ed71f5ca83807317899aaad7f02657a661678c8bfb0219221f` | `54015d1067baa798cc8840cc7f85ee57baa93144e75960b266749376fe56e27b` |
| `advisor_utopia_manifesto_secretary_of_callings` | `d5e73a35af0c23021b009c8e363d4e4fdad83799b4c26003cf6cdae575a9f0f4` | `bc7e42d7a4304eca18718e0a4158b3f82e9325c538b0250ee91d3602d38f8b73` |
| `advisor_utopia_manifesto_social_workshop_planner` | `364ead83013c2f15e4b363d6af139fd0bbc64eaec64931403532707fc92583d8` | `b99c44e93c800e709ece84360cb305118c328bace673360d3f464e1cd4d2883a` |
| `advisor_utopia_manifesto_standards_engineer` | `068e187e8f81a9eada2f52116ca56693af5532061782a7549a4127bde419c790` | `b724ae0d8a8522161072311863a8718f1a8b32175ae961af1f491407b1aad3af` |
| `advisor_utopia_manifesto_steward_of_service` | `4615eb4b872937397d288d475420fe1eb541a165b27487e8923799e81f4c83e4` | `66a5956fa6d5a90a470e0c8c93ef88c34adc3b23712544dffa5a51e522a31a76` |
| `advisor_utopia_manifesto_surveyor_of_shores` | `f266d10852ec89f8c3e868175d5bafe93e417cae0aee8220cfa854aa45985d1c` | `b047201c3064d8acb43932c3ff255727b5913576d06f1de63c4bfb9a86b8f11a` |

### Runtime registration

Read-only `rg` checks found all 16 stable sprite names `GFX_portrait_utopia_manifesto_*_small` in `interface/015_utopia_manifesto.gfx`, all 16 texture paths under `gfx/leaders/015_utopia_manifesto/advisors/`, and all 16 character definitions in `common/characters/015_utopia_manifesto_characters.txt` pointing to the matching sprite. A transient regex check returned `expected=16`, `registered_texture_exists=16`, `missing=[]`.

## ImageGen flags and institutional tableaux

- `imagegen_source_evidence_2026_07_15.json` SHA-256 `7F892568CED49D74EB0D7E9CDFE3A796AEE4DCE13200B3F7A16B3FB2B16B6E18` reports `status=passed`, 21 independent flag compositions, four institutional tableaux, 25 distinct built-in ImageGen handles, and exact byte equality of every package source to its recorded built-in output.
- Command: `python -B docs/assets/015_utopia_manifesto/route_identity_2026_07_14/_tooling/verify_imagegen_source_evidence.py`.
- Output: `Verified 25 independent package sources against exact built-in ImageGen output bytes.` The verifier script SHA-256 is `1711136294C2627799DB2E5543467B816C2C913704BDE32FB192B562077884FD`.
- `flag_identity_validation_2026_07_15.json` SHA-256 `14026C95CA9D3B8B9355A770D49658B05BE738F06319252722F6EBD3E7EC1E65` reports 21 unique independent compositions, 25 wired stems (including four documented aliases), 75 runtime TGAs at main/medium/small sizes, opaque alpha, decoded pixel equality, and distinct processed hashes per route ideology. The source contact sheet SHA-256 is `EF841B80628A1C1CBB4BE99B2C9EE3CA7070AA5D48489012004AEDB8599058DE`; visual inspection found detailed heraldic/institutional motifs rather than primitive geometric placeholders.
- `institutional_portrait_validation_2026_07_15.json` SHA-256 `0DA653422920087A28794A577963860B0DD2FBE2252353DE241BF256C02D655D` reports four distinct 156x210 masters, package/runtime equality, decoded equality, and visual approval against bundled vanilla leader references. Command: `python -B docs/assets/015_utopia_manifesto/route_identity_2026_07_14/_tooling/validate_corrected_institutional_portraits.py`. Output: `Validated 4 corrected institutional portrait DDS files.` The validator SHA-256 is `E7FEF12315F2A0274410BDCF527570BA82D96D11C776C80375FE215F02D51B57`.
- I inspected the institutional source and processed contacts (SHA-256 `CC5B97CC41F65F34E1C86645AEEF14B6203D3424F82BAFAA261BE39FA97B24B8` and `2C005E5F809CC62875BF0C95BF453D7E0CA6D2C7D0E88E570E759377E5B2A655`). All four show empty chambers/tables/seals/ledgers only: no people, heads, faces, bodies, hands, crowds, silhouettes, statues, mannequins, framed portraits, or human shadows.

## Choice and Assignment animation audit

Both packages were read as complete frame-by-frame packages, including `brief.md`, `frame_plan.md`, `prompts.md`, `manifest.md`, `gfx_gui_handoff.md`, `visual_review.md`, eight source frames, eight processed frames, source/processed contacts, sheet PNG/DDS, static fallback, GIF preview, provenance, processing, and validation reports.

### Choice

- Validation report SHA-256 `65026985F34116011D450B54B4B694F128D3042CD872DACF58DEAF75462D4F50`.
- Eight unique source and processed hashes; each frame is `158x24`; horizontal sheet is `1264x24`; static fallback is frame 007; review GIF has 8 frames with durations `200,200,200,200,200,200,200,700 ms`.
- Consecutive processed RGB mean RMS differences are `6.39, 6.7569, 6.3465, 17.9497, 15.7343, 10.6324, 8.634`, proving non-identical states. Source provenance SHA-256 `BA710C0C055235A1CFF833D748158948F416F04B91E75295864D57FBC018B5E5` states every accepted frame is a separate built-in ImageGen output and no processed frame is transform-synthesized.
- Runtime sheet DDS SHA-256 `cd0440db72fce608ee20cd0f5496ede0f9396ed1756aed72c694c9586f2ca13c`; static DDS SHA-256 `126081178829c4e7092e72b52c774e07388c39b9626518a4eee4c414bca0b953`.
- Visual source/contact inspection shows a closed mechanism, gate/latch release, branching rails, and open fork; no people, text, UI labels, or transform-only motion.

### Assignment

- Validation report SHA-256 `F80C48F4F3964C88909729A4FA42A24387F41F46466D11085DBED9365993DEFD`.
- Eight unique source and processed hashes; each frame is `158x24`; horizontal sheet is `1264x24`; static fallback is frame 007; review GIF has 8 frames with durations `200,200,200,200,200,200,200,700 ms`.
- Consecutive processed RGB mean RMS differences are `7.3938, 15.2606, 12.9391, 18.6058, 16.7001, 19.8503, 11.6189`, proving non-identical states. Source provenance SHA-256 `A41BE22609A4C83318E73658E62C4660E03CDE1478F48953E75A673CFF286496` states every accepted frame is a separate built-in ImageGen output and no processed frame is transform-synthesized.
- Runtime sheet DDS SHA-256 `cfb74421c21b650b061042f738cd735aeb338e0c3cb96d2624aceb0d46ca8241`; static DDS SHA-256 `202a9ab4120cec445d07ef4b0509a57baff8e8ef9272a722c9be204d281efd62`.
- Visual source/contact inspection shows tokens entering a comb/rail, row formation, grid rise, and final placement; no people, text, UI labels, or transform-only motion.

## Commands and checks performed

1. Read the parent prompt/manifests/handoffs and the two required asset skills.
2. Used `rg --files` to locate active route-identity tooling, manifests, review sheets, animation packages, and references.
3. Used `Get-Content -Raw` on the current JSON/manifests and `Get-FileHash -Algorithm SHA256` on the processor, converter, validators, manifests, approvals, validation reports, contact sheets, and animation provenance files. Hashes above are from this audit run.
4. Ran `python -B docs/assets/015_utopia_manifesto/route_identity_2026_07_14/_tooling/verify_imagegen_source_evidence.py`; exact output recorded above.
5. Ran `python -B docs/assets/015_utopia_manifesto/route_identity_2026_07_14/_tooling/validate_corrected_institutional_portraits.py`; exact output recorded above.
6. Ran a transient PowerShell here-string piped to Python (not saved to the repository) that parsed every advisor DDS header and decoded BGRA payload, comparing package DDS, runtime DDS, processed PNG, and decoded verification PNG. It returned `count=16`, `all=true`; results are summarized in the installed DDS proof above.
7. Ran read-only `rg` checks against `interface/015_utopia_manifesto.gfx`, `common/characters/015_utopia_manifesto_characters.txt`, `interface/015_utopia_manifesto_ledger.gui`, and `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` for advisor sprites, texture paths, animation sprites, GUI placement, and visibility flags.
8. Visually inspected enlarged nearest-neighbour advisor contact, decoded advisor contact, canonical vanilla advisor contact, the advocate six-reference comparison, ImageGen frame/paper sources and alpha overlays, flag ImageGen source contact, institutional source/processed contacts, and both animation source/processed contacts.

## Files changed by this audit

Only this audit handoff was added:

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/advisor_asset_final_audit_2026_07_18.md`

No PNG, DDS, TGA, source manifest, validator, GFX, GUI, character, gameplay, localisation, or parent documentation file was edited. No image was regenerated because no concrete visual defect was found.

## Remaining limits

- This is an independent asset/package audit, not an in-game rendering session; runtime UI capture and live animation timing were not exercised.
- Vanilla-style approval is visual-family/readability approval, not a claim of pixel identity with vanilla art.
- The processor validator remains candidate-only by design; use the separate independent approval JSON plus installed validation as the completion evidence.
- Historical v2 audit/handoff records remain in their existing rejected/superseded locations and were not rewritten in this audit.
