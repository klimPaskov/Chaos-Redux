# Event 6 FORM-03 charter-and-works asset manifest

## Scope and ownership

This package contains the FORM-03 focus, idea/national-spirit,
decision-family icons, and charter-convention report scene accepted in section 17.3 of
`docs/plans/006_independence_wave_plans/006_form03_language_industry_progression_addendum_2026_07_15.md`.
It does not contain flags, portraits, animation, gameplay script, localisation,
GUI, or `.gfx` edits.

Every icon was generated independently with built-in ImageGen.  Focus, idea,
and decision artwork was composed for its own target surface; no icon is a
resize, crop, recolour, or relabel of another family.  Exact prompts and the
built-in source output identifiers are retained in `prompts/focus_prompts.md`,
`prompts/idea_prompts.md`, and `prompts/decision_prompts.md`.

The independently produced 210x176 report scene is retained under
`report_scene/`. Its complete requirement-to-runtime row, provenance,
processing record, validation, checksums, and review paths are in
`report_scene/submanifest.md`.

## Report scene — accepted family `ASSET-048`

| Asset | Live consumers | Source package | Runtime DDS | Sprite | Status |
|---|---|---|---|---|---|
| `report_event_006_form03_charter_convention` | `chaosx.nr6.300` through `chaosx.nr6.308` | `report_scene/` | `gfx/event_pictures/006_independence_wave/report_event_006_form03_charter_convention.dds` (210x176 BGRA) | `GFX_report_event_006_form03_charter_convention`, registered in `interface/006_independence_wave_event_pictures.gfx` | `wired`; all nine events consume the registered sprite |

## Exact path roots

The shortened roots used in the registry below expand to these exact
repository-relative paths:

- `S/` = `docs/assets/006_independence_wave/low_countries_form03_progression/source_png/`
- `P/` = `docs/assets/006_independence_wave/low_countries_form03_progression/processed_png/`
- `D/` = `docs/assets/006_independence_wave/low_countries_form03_progression/dds/`
- `GF/` = `gfx/interface/goals/006_independence_wave/form03/`
- `GI/` = `gfx/interface/ideas/006_independence_wave/form03/`
- `GD/` = `gfx/interface/decisions/006_independence_wave/form03/`

All DDS files under `D/` are byte-identical retained copies of their runtime
counterparts under `GF/`, `GI/`, or `GD/`.

## Reference and processing provenance

Reference inspection used the canonical skill-local library at
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`:

- `README.md` and the national-focus, idea/national-spirit, and decision rows
  in `CATALOG.md`
- `contact_sheets/icons.png`
- all three review PNGs in each of `icons/national_focus/`, `icons/ideas/`,
  and `icons/decisions/`

The exact cataloged vanilla source families were
`gfx/interface/goals/*.dds`, `gfx/interface/ideas/*.dds`, and
`gfx/interface/decisions/*.dds`.  Reference PNGs were used only for style,
scale, silhouette, and transparency review; none was copied, traced, edited,
or shipped.

Transparency followed the built-in ImageGen chroma-key path.  Each raw source
was generated against a flat removable green field and processed with:

```text
python C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py --input <source> --out <keyed> --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill --force
```

The retained `process_icons.py` then performed only alpha-bound cropping,
aspect-preserving resize, centered placement, one-pixel dark silhouette, and a
restrained soft shadow.  It did not draw or replace artwork.  Final conversion
used `.tools/convert_to_dds.py` with the exact target width and height.

## Asset registry

### Focus icons — accepted family `ASSET-018`

All six focus DDS files have base and shine sprite registrations.  The shine
sprite uses the same texture with `gfx/FX/buttonstate.lua`.

| Asset | Gameplay focus | Prompt evidence | Source PNG | Processed PNG | Package / runtime DDS | Sprite names | Artist handoff record |
|---|---|---|---|---|---|---|---|
| `goal_independence_wave_form03_open_charter_convention` | `independence_wave_form03_open_charter_convention` | `prompts/focus_prompts.md`, matching heading; built-in ImageGen | `S/goal_independence_wave_form03_open_charter_convention_imagegen_source.png` (1312x1199) | `P/goal_independence_wave_form03_open_charter_convention.png` (94x86 RGBA) | `D/goal_independence_wave_form03_open_charter_convention.dds`; `GF/goal_independence_wave_form03_open_charter_convention.dds` (94x86 BGRA) | `GFX_goal_independence_wave_form03_open_charter_convention`; `GFX_goal_independence_wave_form03_open_charter_convention_shine` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `goal_independence_wave_form03_define_public_service_guarantees` | `independence_wave_form03_define_public_service_guarantees` | `prompts/focus_prompts.md`, matching heading; built-in ImageGen | `S/goal_independence_wave_form03_define_public_service_guarantees_imagegen_source.png` (1174x1340) | `P/goal_independence_wave_form03_define_public_service_guarantees.png` (94x86 RGBA) | `D/goal_independence_wave_form03_define_public_service_guarantees.dds`; `GF/goal_independence_wave_form03_define_public_service_guarantees.dds` (94x86 BGRA) | `GFX_goal_independence_wave_form03_define_public_service_guarantees`; `GFX_goal_independence_wave_form03_define_public_service_guarantees_shine` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `goal_independence_wave_form03_establish_delta_works_board` | `independence_wave_form03_establish_delta_works_board` | `prompts/focus_prompts.md`, matching heading; built-in ImageGen | `S/goal_independence_wave_form03_establish_delta_works_board_imagegen_source.png` (1311x1200) | `P/goal_independence_wave_form03_establish_delta_works_board.png` (94x86 RGBA) | `D/goal_independence_wave_form03_establish_delta_works_board.dds`; `GF/goal_independence_wave_form03_establish_delta_works_board.dds` (94x86 BGRA) | `GFX_goal_independence_wave_form03_establish_delta_works_board`; `GFX_goal_independence_wave_form03_establish_delta_works_board_shine` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `goal_independence_wave_form03_build_federal_appeals_and_examinations` | `independence_wave_form03_build_federal_appeals_and_examinations` | `prompts/focus_prompts.md`, matching heading; built-in ImageGen | `S/goal_independence_wave_form03_build_federal_appeals_and_examinations_imagegen_source.png` (1174x1340) | `P/goal_independence_wave_form03_build_federal_appeals_and_examinations.png` (94x86 RGBA) | `D/goal_independence_wave_form03_build_federal_appeals_and_examinations.dds`; `GF/goal_independence_wave_form03_build_federal_appeals_and_examinations.dds` (94x86 BGRA) | `GFX_goal_independence_wave_form03_build_federal_appeals_and_examinations`; `GFX_goal_independence_wave_form03_build_federal_appeals_and_examinations_shine` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `goal_independence_wave_form03_harmonize_corridor_standards` | `independence_wave_form03_harmonize_corridor_standards` | `prompts/focus_prompts.md`, matching heading; built-in ImageGen | `S/goal_independence_wave_form03_harmonize_corridor_standards_imagegen_source.png` (1312x1199) | `P/goal_independence_wave_form03_harmonize_corridor_standards.png` (94x86 RGBA) | `D/goal_independence_wave_form03_harmonize_corridor_standards.dds`; `GF/goal_independence_wave_form03_harmonize_corridor_standards.dds` (94x86 BGRA) | `GFX_goal_independence_wave_form03_harmonize_corridor_standards`; `GFX_goal_independence_wave_form03_harmonize_corridor_standards_shine` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `goal_independence_wave_form03_submit_low_countries_compact` | `independence_wave_form03_submit_low_countries_compact` | `prompts/focus_prompts.md`, matching heading; built-in ImageGen | `S/goal_independence_wave_form03_submit_low_countries_compact_imagegen_source.png` (1312x1199) | `P/goal_independence_wave_form03_submit_low_countries_compact.png` (94x86 RGBA) | `D/goal_independence_wave_form03_submit_low_countries_compact.dds`; `GF/goal_independence_wave_form03_submit_low_countries_compact.dds` (94x86 BGRA) | `GFX_goal_independence_wave_form03_submit_low_countries_compact`; `GFX_goal_independence_wave_form03_submit_low_countries_compact_shine` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |

### Idea / national-spirit icons — accepted family `ASSET-026`

| Asset | Gameplay idea | Prompt evidence | Source PNG | Processed PNG | Package / runtime DDS | Sprite name | Artist handoff record |
|---|---|---|---|---|---|---|---|
| `idea_independence_wave_form03_provisional_charter` | `independence_wave_form03_provisional_charter` | `prompts/idea_prompts.md`, matching heading; built-in ImageGen | `S/idea_independence_wave_form03_provisional_charter_imagegen_source.png` (1254x1254) | `P/idea_independence_wave_form03_provisional_charter.png` (64x64 RGBA) | `D/idea_independence_wave_form03_provisional_charter.dds`; `GI/idea_independence_wave_form03_provisional_charter.dds` (64x64 BGRA) | `GFX_idea_independence_wave_form03_provisional_charter` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `idea_independence_wave_form03_charter_without_works` | `independence_wave_form03_charter_without_works` | `prompts/idea_prompts.md`, matching heading; built-in ImageGen | `S/idea_independence_wave_form03_charter_without_works_imagegen_source.png` (1254x1254) | `P/idea_independence_wave_form03_charter_without_works.png` (64x64 RGBA) | `D/idea_independence_wave_form03_charter_without_works.dds`; `GI/idea_independence_wave_form03_charter_without_works.dds` (64x64 BGRA) | `GFX_idea_independence_wave_form03_charter_without_works` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `idea_independence_wave_form03_industrial_directorate` | `independence_wave_form03_industrial_directorate` | `prompts/idea_prompts.md`, matching heading; built-in ImageGen | `S/idea_independence_wave_form03_industrial_directorate_imagegen_source.png` (1254x1254) | `P/idea_independence_wave_form03_industrial_directorate.png` (64x64 RGBA) | `D/idea_independence_wave_form03_industrial_directorate.dds`; `GI/idea_independence_wave_form03_industrial_directorate.dds` (64x64 BGRA) | `GFX_idea_independence_wave_form03_industrial_directorate` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `idea_independence_wave_form03_dual_compromise` | `independence_wave_form03_dual_compromise` | `prompts/idea_prompts.md`, matching heading; built-in ImageGen | `S/idea_independence_wave_form03_dual_compromise_imagegen_source.png` (1254x1254) | `P/idea_independence_wave_form03_dual_compromise.png` (64x64 RGBA) | `D/idea_independence_wave_form03_dual_compromise.dds`; `GI/idea_independence_wave_form03_dual_compromise.dds` (64x64 BGRA) | `GFX_idea_independence_wave_form03_dual_compromise` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `idea_independence_wave_form03_ratified_confederation` | `independence_wave_form03_ratified_confederation` | `prompts/idea_prompts.md`, matching heading; built-in ImageGen | `S/idea_independence_wave_form03_ratified_confederation_imagegen_source.png` (1254x1254) | `P/idea_independence_wave_form03_ratified_confederation.png` (64x64 RGBA) | `D/idea_independence_wave_form03_ratified_confederation.dds`; `GI/idea_independence_wave_form03_ratified_confederation.dds` (64x64 BGRA) | `GFX_idea_independence_wave_form03_ratified_confederation` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `idea_independence_wave_form03_charter_rupture` | `independence_wave_form03_charter_rupture` | `prompts/idea_prompts.md`, matching heading; built-in ImageGen | `S/idea_independence_wave_form03_charter_rupture_imagegen_source.png` (1254x1254) | `P/idea_independence_wave_form03_charter_rupture.png` (64x64 RGBA) | `D/idea_independence_wave_form03_charter_rupture.dds`; `GI/idea_independence_wave_form03_charter_rupture.dds` (64x64 BGRA) | `GFX_idea_independence_wave_form03_charter_rupture` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |

### Decision-family icons — accepted family `ASSET-038`

| Asset | Current gameplay family | Prompt evidence | Source PNG | Processed PNG | Package / runtime DDS | Sprite name | Artist handoff record |
|---|---|---|---|---|---|---|---|
| `decision_independence_wave_form03_language` | `independence_wave_form03_convene_language_convention`; `independence_wave_form03_open_multilingual_service_examinations`; `independence_wave_form03_publish_member_language_codes`; `independence_wave_form03_establish_federal_language_appeals`; `independence_wave_form03_extend_protected_local_services` | `prompts/decision_prompts.md`, matching heading; built-in ImageGen | `S/decision_independence_wave_form03_language_imagegen_source.png` (1254x1254) | `P/decision_independence_wave_form03_language.png` (32x32 RGBA) | `D/decision_independence_wave_form03_language.dds`; `GD/decision_independence_wave_form03_language.dds` (32x32 BGRA) | `GFX_decision_independence_wave_form03_language` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `decision_independence_wave_form03_works` | `independence_wave_form03_reconnect_sambre_meuse_corridor`; `independence_wave_form03_coordinate_frisian_waterway_standards`; `independence_wave_form03_standardize_rail_and_customs_manifests`; `independence_wave_form03_request_development_compact_technical_mission`; `independence_wave_form03_fund_associate_corridor_share` | `prompts/decision_prompts.md`, matching heading; built-in ImageGen | `S/decision_independence_wave_form03_works_imagegen_source.png` (1254x1254) | `P/decision_independence_wave_form03_works.png` (32x32 RGBA) | `D/decision_independence_wave_form03_works.dds`; `GD/decision_independence_wave_form03_works.dds` (32x32 BGRA) | `GFX_decision_independence_wave_form03_works` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `decision_independence_wave_form03_member_vote` | founding-delegation authorization/withholding, `independence_wave_form03_join_as_autonomous_member`, `independence_wave_form03_invite_sovereign_corridor_partners`, and `independence_wave_form03_implement_member_language_guarantees` | `prompts/decision_prompts.md`, matching heading; built-in ImageGen | `S/decision_independence_wave_form03_member_vote_imagegen_source.png` (1254x1254) | `P/decision_independence_wave_form03_member_vote.png` (32x32 RGBA) | `D/decision_independence_wave_form03_member_vote.dds`; `GD/decision_independence_wave_form03_member_vote.dds` (32x32 BGRA) | `GFX_decision_independence_wave_form03_member_vote` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `decision_independence_wave_form03_ratification` | `independence_wave_form03_ratify_confederal_charter`; `independence_wave_form03_resubmit_confederal_charter` | `prompts/decision_prompts.md`, matching heading; built-in ImageGen | `S/decision_independence_wave_form03_ratification_imagegen_source.png` (1254x1254) | `P/decision_independence_wave_form03_ratification.png` (32x32 RGBA) | `D/decision_independence_wave_form03_ratification.dds`; `GD/decision_independence_wave_form03_ratification.dds` (32x32 BGRA) | `GFX_decision_independence_wave_form03_ratification` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `decision_independence_wave_form03_repair` | `independence_wave_form03_reopen_charter_talks`; `independence_wave_form03_repair_language_settlement`; `independence_wave_form03_repair_industrial_compact` | `prompts/decision_prompts.md`, matching heading; built-in ImageGen | `S/decision_independence_wave_form03_repair_imagegen_source.png` (1254x1254) | `P/decision_independence_wave_form03_repair.png` (32x32 RGBA) | `D/decision_independence_wave_form03_repair.dds`; `GD/decision_independence_wave_form03_repair.dds` (32x32 BGRA) | `GFX_decision_independence_wave_form03_repair` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |
| `decision_independence_wave_form03_withdrawal` | `independence_wave_form03_withdraw_from_autonomous_membership` | `prompts/decision_prompts.md`, matching heading; built-in ImageGen | `S/decision_independence_wave_form03_withdrawal_imagegen_source.png` (1254x1254) | `P/decision_independence_wave_form03_withdrawal.png` (32x32 RGBA) | `D/decision_independence_wave_form03_withdrawal.dds`; `GD/decision_independence_wave_form03_withdrawal.dds` (32x32 BGRA) | `GFX_decision_independence_wave_form03_withdrawal` | `handed_off`; matching external `.gfx` entry already present; this tranche did not edit it |

## SHA-256 checksums

Each row records the retained ImageGen source, final processed PNG, and final
DDS checksum.  The package DDS and runtime DDS share the recorded DDS hash.

| Asset | Source SHA-256 | Processed SHA-256 | DDS SHA-256 |
|---|---|---|---|
| `decision_independence_wave_form03_language` | `96aa5a4ec5e02be837df643ca0d597993943f448b16e2f61383b27f127253767` | `cb0a1d55f221913a10d9c2d5c07455bba3221867c10bc23eb713747d01fe1db2` | `e1f2ffdd011934f0003eb72f9ee3bb24732b4ca4502400c6ae52b0fa4eee0efc` |
| `decision_independence_wave_form03_member_vote` | `2629a610f1d74aec6d3ca377204e56ad1a6467646ec5d5f55b15db40dbb375a2` | `27e1db814817ee562573b111f5940c6b196b7e5fd862e7c4b878424cff9ebbb5` | `9ffb013259b86aaa723b79f766708dba8d558e0fcb5e1460959b457dd3696c58` |
| `decision_independence_wave_form03_ratification` | `fdbf80039f27a57f9d52beffa20e05263da51dcd52652cd272a500371f52caed` | `40fa9c160cff4680e0b2df6a3664d2c3bb713431cddb8118827dfa0672e112e0` | `e51b9eb5835dbde761a42d3925d8df8fd83c6c1e814dca69e5bf027cd63d6dfa` |
| `decision_independence_wave_form03_repair` | `15c796183138fb0131b6edef1f3a1b3b3bc2e964a3a0ed6661ef1882d7b7881b` | `56b98ee284d504fda0fccf75e7071c85b61ea300d5e1d847c6027bf15faccab4` | `9cdedd1e29df73e2ed2067ae11438fb2219fa9c21ffc73af1eb840fe487f163e` |
| `decision_independence_wave_form03_withdrawal` | `f2aaf39fccc5bc9c0bcc93f04cf5c4a1441303e1ce8658f5e5adf67c754d536d` | `9a49f70e482476fc2d451586e4aa67d8c29f9ec805095099f19d10d9075b0012` | `2e096daaedbebca57623936c0e85b0d78fb42677e83ba966ea14484fb52e895f` |
| `decision_independence_wave_form03_works` | `18c4ce18fb6f9d34b48b210b0eed775065f86fe28ed2a5f07609a3a33a0de1f3` | `57adcc24bf1f881d4217081ad9a32e30291adfe9b347b7cc4bcfce2726804438` | `2e664cc81d2d69d5620d5140a0b6609f89334fad4ebcfca2d066f465a9044b96` |
| `goal_independence_wave_form03_build_federal_appeals_and_examinations` | `8c8d4fce84c81177751f8b5d6460823fe3ff62880aaf5593ab9c8eb49a36b952` | `f1442bd59919fcae4d4763b9f08635b4a4108e69c5420855f7d82e6e6bd955ee` | `b315f6b3f5a9fdce2fe25d81ef1d45fdb3a88d2b5830351743b61b84e84d4811` |
| `goal_independence_wave_form03_define_public_service_guarantees` | `cf59447cdc5352eb6ee923a194abaae7ddce585052f9f8731f0865ee9838768e` | `9fe70dbbed239bf86920eb9f946d3d34022e2a1694f13f6b20a2fc1933c11be8` | `4c5863c99c24331686eef793e68c9ed125fbf33df7b2485109eb62a74d4dadae` |
| `goal_independence_wave_form03_establish_delta_works_board` | `8d50de9b0ddadc21262645728ac36796b852c4071d1dbd1dda3316d107c01621` | `4d54fd681b3b631464206e06ba592350afc5729889602668bfaeac4320dda3dd` | `71260623504f95f4f290000a8a83ab24acf5ca20f961473e9ac61a8adab5f565` |
| `goal_independence_wave_form03_harmonize_corridor_standards` | `5c181d2c6da93dc69bb5cecca941a21f333ddb876d806acf02c47df322c3ec32` | `f76ddd20cd7db8785278402b3208151a6bef4ed0c287794d3409bca6ba015255` | `052e4bdde777e1acfa162adcd35817d3069186405f89af0b463864096ad27077` |
| `goal_independence_wave_form03_open_charter_convention` | `7150032610d420d9e307f404e57f4a7d012646397bc0798f9a88d14c596d4895` | `db7454a58465df98bdf0ed8659d68049eec6c3c55840bed764684650c2b52621` | `6bd58f044cbf1bbecae8a365e92796a4b5424947f3ab94a18116dd49860fe542` |
| `goal_independence_wave_form03_submit_low_countries_compact` | `cf62319e26cf8088938e98e85a0d4942bdca850203e5a258f509815036addfd7` | `d81dd34871ba8b3845faa14d036c6ab665ca5a9a8d3ce9fc558632c7775a83ff` | `33fcb3f61471c0d8e24b82f00eca96c2058e76b832a73d58b70e2c1aadcddf3b` |
| `idea_independence_wave_form03_charter_rupture` | `b0a749fd33214f3e900d9250ff26fe0a5db1af4ac2d35c811e6131cc5229a212` | `d021d898eb0de0ad903aa093ba92eafb2c9a70e10ee39702e1d9b5405d69a019` | `416f35220f206b96f1065d78970248980f9ea7a08de2b19ebd9a52e20400babd` |
| `idea_independence_wave_form03_charter_without_works` | `564a4bac3fb6f7ffad0d76d282a1637b921f0ae05e28c9d891803cc5ad8bc52b` | `815b378133e0973e9d7055cff86560537fe1bdb7e4ee919a4f376a66657fc3f3` | `da4d849a4401b976f71ed4cab4716dc0bae3eb4576c47cc95246f9a196a43cdc` |
| `idea_independence_wave_form03_dual_compromise` | `5894708691bc3b69222f27122594cee47ef03878a6fb07eb3653fd79cad3f997` | `886017b99d1c16111b48844fc2d590fbdd5ab35f0166002918d03b7bdffeaef9` | `b0d428c017ee4015656843b1f37e78f2f59e2ff4d192e840a516d57668871d90` |
| `idea_independence_wave_form03_industrial_directorate` | `b8fd00f055ed6da4780d1d778d0051421f3486ee555da3e59878606a82a7c8a5` | `4f6423c31dfcb77411327fc9068a706d6464bde9e872849da04c7936344b4252` | `7ab014fb10c8dd7eeaa091dd842bbcfaf320305d8a2b8bf7bc22c158863bfdc8` |
| `idea_independence_wave_form03_provisional_charter` | `63dcd2c73f645d26e061f6eefd274c88f7ba427d0ed69cf65e3e6faefa5c9440` | `6f1988d8f9ec5a6452b3580b48f2db68e02e4d1b13e729c5e4e8693924c742fd` | `f888ad8f5b096a351d59f78722a535f9882333102a96e9db73228953b846ff27` |
| `idea_independence_wave_form03_ratified_confederation` | `44052b1f8420220250ae25da39b62eb6c57b9a1d0d80b34b95e46a958bb72909` | `48fb20e07c5240f35abbc8eb84f1b66e8c8f756d2f7a62c62481dc6892c06518` | `f61d477097c295c2c6fa2688d5a2cbdb48afda326c9e82265a200af26c694a7b` |

## Review and validation

Review sheets retained in `contact_sheets/`:

- `form03_goal_native.png`
- `form03_goal_enlarged_nearest.png`
- `form03_idea_native.png`
- `form03_idea_enlarged_nearest.png`
- `form03_decision_native.png`
- `form03_decision_enlarged_nearest.png`

Native and enlarged sheets were inspected.  All three families remain distinct
at target size, unused canvas is transparent, corner alpha is zero, subjects
are centered, and no green fringe, white matte, fake checkerboard, opaque
square, or readable generated text is visible.

All 18 icon DDS files pass the complete uncompressed one-level BGRA check: 128-byte
legacy header, `DDS_HEADER` size 124, `DDS_PIXELFORMAT` at byte 76 with flags
65 and the standard BGRA masks, `DDSCAPS_TEXTURE` at byte 108, declared target
dimensions, and exact file length `128 + width * height * 4`.  Pillow decoding
of every runtime DDS is pixel-identical to its processed PNG, including alpha.
Package and runtime DDS copies are byte-identical.

The report DDS independently passes the same legacy-header and exact-length
checks at 210x176, has real alpha with four transparent corners, and decodes
pixel-identically to its processed PNG. The parent visually accepted its source,
native card, and enlarged decoded review.

## Honest status and blockers

- Asset production status: `wired` for all 18 icons and the report scene.
- Sprite status: matching registrations already exist in
  `interface/006_independence_wave_form03.gfx`, created outside this bounded
  asset tranche.  This tranche did not edit or claim ownership of that file.
- Blockers: none.
- Simplifications or fallback art: none.  No CLI model, alternate generator,
  locally drawn primitive substitute, resized cross-family art, placeholder,
  or reused report-image substitute was used.
- No progression attestation, family readiness, package readiness, runtime
  content attestation, or SCN-008 readiness value was set or changed.
