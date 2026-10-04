# Event 028 idea icon regeneration handoff, 2026-10-04

Disposition: accepted and queued original replacement production under the parent/user full-repair assignment. Historical source recovery remains exhausted within the exact authorized roots; the new icons are not recovered historical masters. Final status is recorded per icon below and in the staged manifest.

## Ownership and scope

Owner: Event028 IDEA/NATIONAL-SPIRIT icon production subagent.

This handoff covers only the eight idea icons: four static dust stages, the shared preparedness/dust-protection icon, recovery burden, main-crater material control, and fragment-material control. All art, source PNGs, processed PNGs, DDS candidates, per-icon prompts, review evidence, contact sheets, manifest, and temporary GFX handoff are staged under docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/.

The parent accepted original-image regeneration after the source-recovery handoff reported 0 of 45 historical masters recovered. The 2026-10-03 parent asset audit and asset-record handoff remain the runtime inventory evidence. Historical DDS files and round-trip PNGs are not treated as source artwork and are not upscaled or repainted.

No project subagent was spawned. No runtime DDS, GFX, gameplay, GUI, localisation, spreadsheet, or Git index/commit was changed.

## Reference and consumer evidence

Canonical idea family used: C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/ideas/. The contact sheet was inspected before seven individual full-size references. Their exact paths, native dimensions, hashes, and review notes are in the staged manifest. The current canonical Vanilla library records build Operation Postern v1.19.2.0.a729 (d245), extracted 2026-07-16.

The exact installed-vanilla 64x64 idea precedent is gfx/interface/ideas/idea_war_economy.dds (SHA-256 B757D64EC1A737517BF2845D172B0CC511B4B5EC8FC85E2A28ACEAF9BBE3C482). Installed interface/ideas.gfx lines 1191-1194 define GFX_idea_war_economy and point to that native-size DDS. The DDS is 64x64, 16,512 bytes, one-level BGRA; its decoded image was emitted and viewed individually, with alpha range 0-255.

Current mod consumer registrations are in interface/028_asteroid_incoming.gfx (SHA-256 EDEDE7E51B0AC62B7A63BD3FA6C96A2F55F5BEAEFE7E778CFBF20FC0AE73BEFF). Exact sprites, aliases, runtime DDS paths, idea ids, and stage dispositions are listed per row in the staged manifest.

The national_spirit_backgrounds contact sheet and catalog were reviewed. No catalog component is layered under these icons because the available background_template entries are medallion backdrops that do not fit the inspected unframed idea family and consumers.

## Accepted visual direction

Use eight independent native ImageGen outputs with genuine transparent unused canvas. The shared family treatment is a compact, aged HOI4 idea painting with a centered symbolic subject, dark painted contour, readable value contrast, restrained material highlights, and no full focus frame or background medallion.

The four dust stages have deliberately different subjects and severity signals: thinly veiled amber sun for Residual Haze; a globe swallowed by a broad particulate curtain for Global Dust Veil; frost locking an industrial gear for Impact Winter; and a nearly sealed dark sun under heavy ice and impact ash for Severe Impact Winter.

The shared preparedness/dust-protection subject is a period civil-defence particulate respirator with a serviceable filter. Recovery burden is a rail section crushed beneath debris. Main-crater material is one broad dense fused iron-nickel plate. Fragment material is a distinct cluster of smaller dense metal fragments in fractured basalt. Minerals use realistic compressed and metallic material rather than fantasy crystals or glow.

## Per-icon production ledger

The ledger is updated after each individual ImageGen call and processing pass. Every candidate retains its exact submitted prompt, actual tool receipt, original output path and hash, alpha evidence, processed file and hash, decoded DDS round-trip and hash, reference mapping, consumer, and disposition.

| Requirement | Filename / sprite | Tool receipt and source | Processed / DDS round-trip | Disposition |
| --- | --- | --- | --- | --- |
| E028-IDEA-01 | asteroid_residual_haze.png / GFX_idea_asteroid_incoming_residual_haze | v001-v005 receipts retained; selected v005 source SHA-256 7770D08F7DE7D6FAC1181D7B1C1AD2C108506EDCE2149821149817423EEDD443 | processed SHA-256 0C349C37B9E87CE768DE44D764B9EEC0DC8848CC628B66B3552C1356274C6C5A; canonical BGRA DDS round-trip is exact | needs_user_review; parent visual review pending |
| E028-IDEA-02 | asteroid_global_dust_veil.png / GFX_idea_asteroid_incoming_global_dust_veil | v001-v003 receipts retained; selected v003 source SHA-256 9A091E0F032D764216632DADB41FA9F0D9BE6FF64BE68C01681F9B2368808DA4 | processed SHA-256 7829D25DA6398A38EDF20B3CFF62803561EE4799713FD8F9B76DAF92B0AFD870; canonical BGRA DDS round-trip is exact | needs_user_review; parent visual review pending |
| E028-IDEA-03 | asteroid_impact_winter.png / GFX_idea_asteroid_incoming_impact_winter | v001-v004 receipts retained; v001 SHA-256 7732AAE3EDCCF7E5A96734DD4F744612117CC1ED1087764630B7AE15E4E1577C; v002 SHA-256 DD09059C50170E75956491020FE7CA1B82B1202826629473E3E7A089917C8AA1; v003 SHA-256 5B141E5C398AAE32A5EF7E37ECC0CB47BBD28688FCFF1715C5B817EA26EDD955; v004 SHA-256 BCDE7F9A3738CFD4D631AF71D36CA0561D9BC59771667B8D74ECB7FC48186732 | no processed preview or DDS; all sources and three contrast reviews retained | blocked: four attempts fail clipping or edge-colour validation |
| E028-IDEA-04 | asteroid_severe_impact_winter.png / GFX_idea_asteroid_incoming_severe_impact_winter | v001 rejected; selected v002 source SHA-256 62B12D1C7142571A8CD012491E3FEFF9002C1BF715C01025BFB589E0759E1F51 | processed SHA-256 5ABE9C44629DBC316B0B0F2513A90AF6AA8358A6A2BEB7F3C5340B00552ACD9F; canonical BGRA DDS round-trip is exact | needs_user_review; parent visual review pending |
| E028-IDEA-05 | asteroid_dust_protection.png / GFX_idea_asteroid_incoming_preparedness and GFX_idea_asteroid_incoming_dust_protection | v001 rejected; selected v002 source SHA-256 59EEB76D37171FCEA3A0D177E16A35410EF9FCB1EFF25BA0E1698038DD4A50BC | processed SHA-256 FF12AA75B39E7F7FEF05B7286877EA9FAA18EEE8B6B764B03BC52DF28B5B6835; canonical BGRA DDS round-trip is exact | needs_user_review; parent visual review pending |
| E028-IDEA-06 | asteroid_recovery_burden.png / GFX_idea_asteroid_incoming_recovery_burden | v001 source SHA-256 C080A767EEF6105249C4E1641E9438FF415E79E8D406D7A16509D9A56D841055 | processed SHA-256 56668DF86857D32AF91A10CC945D325A94184AC859E90FED84C716FE904F65FC; canonical BGRA DDS round-trip is exact | needs_user_review; parent visual review pending |
| E028-IDEA-07 | asteroid_main_crater_material.png / GFX_idea_asteroid_incoming_main_crater_material | v001 source SHA-256 6B441E209101040A988FD2526C2CF42286A72821425EDA1BCD7E8E205D3F2183 | processed SHA-256 3415EA39D73899015B03C158F3D25F6BDB4C6E5D56FC495C558C1EF65BE8C05F; canonical BGRA DDS round-trip is exact | needs_user_review; parent visual review pending; idea icon, not 32x32 state icon |
| E028-IDEA-08 | asteroid_fragment_material.png / GFX_idea_asteroid_incoming_minerals | v001 source SHA-256 4E9DF01F6AF0B8A2EF960340294E9FD83925BEAC8BFFBF64F5243F856414D824 | processed SHA-256 4A218F9EBA3087404C66CC168AFE6A685D0EABFAE0E13D7364718879EB455242; canonical BGRA DDS round-trip is exact | needs_user_review; parent visual review pending |

### Impact Winter blocked item

Four native ImageGen candidates were retained, with no processing or DDS conversion. Exact source paths, prompt paths, tool-reported output paths, SHA-256 identities, alpha bounds, and contrast reviews are recorded in reviews/asteroid_impact_winter_blocked_lineage.json. V001-v004 are preserved under rejected/. The gear's central bore is intentional transparent space. Status is blocked because no attempt passed the complete-edge and edge-colour review; no background removal, local recolour, matte repair, substitute, or runtime replacement was applied.

### Residual Haze rejected attempt

The first built-in ImageGen call returned an original 1254x1254 RGBA PNG at C:/Users/klimp/.codex/generated_images/01a103a9-fc50-74d1-ac9f-b02aaad3a17d/exec-c02e8b80-bbaf-4ffd-b9fd-12d4701d5a9c.png. Its SHA-256 is 50A67FE9A12B349E26FC84CF4691BF1A974C24BC20E1AD1071981B820FA52376. Native transparency passed with alpha range 0-255 and zero-alpha corners, but visible bounds reached the left canvas edge. It is rejected for clipping and retained unchanged under rejected/asteroid_residual_haze_v001_clipped_source.png.

The focused second ImageGen edit returned a 1254x1254 RGBA PNG at C:/Users/klimp/.codex/generated_images/01a103a9-fc50-74d1-ac9f-b02aaad3a17d/exec-a52fb267-561e-46c6-b88a-1cf9687c67a0.png, SHA-256 63E34E9CE34AC91834827ACDA3B732C9F6030E60AC6F72B57CA684AC659D51E6. It has alpha range 0-255, zero-alpha corners, and bounds [97,53,1176,1212], so no subject clipping remains. At native 64x64 the broad veil reads as an orbital ring around a bronze planet, which weakens the Residual Haze meaning. Its 64x64 processed PNG, BGRA DDS candidate, and pixel-equal DDS round-trip are preserved under rejected/asteroid_residual_haze_v002_saturn_like/ rather than accepted source/processed paths.

The v002 edit prompt requested 8 percent edge clearance; the actual minimum source margin was 42 pixels (3.3 percent) and becomes about 2 pixels at 64x64. That margin remains clear, but the semantic reading is the rejection reason. The v003 focused edit also retained a ring-like reading: its 1254x1254 source hash is 93FC6FC42BB27C9230765586D9A72DD6D8CEB8AF3D9FC31516C101A52BE09462, alpha range 0-255, corner alpha 0, and bounds [97,52,1210,1182]. It is preserved unchanged under rejected/asteroid_residual_haze_v003_ring_like_source.png.

The fresh v004 generation returned 1254x1254 RGBA at C:/Users/klimp/.codex/generated_images/01a103a9-fc50-74d1-ac9f-b02aaad3a17d/exec-5ab47078-5bf9-490a-b33e-7d5d92f1e93a.png, SHA-256 698A65FD7C154AEC7D66E9DC5FE39D2F9CC92EC8FE4C8D6C0F848216EB06071F. It has alpha range 0-255 and transparent corners, but visible bounds [0,21,1230,1254] touch the left and bottom canvas edges. It is rejected for clipping and retained at rejected/asteroid_residual_haze_v004_clipped_source.png. The focused v005 edit targets that exact image and asks only to scale and center the same emblem, restoring its clipped outer edge.

The v005 edit returned a 1254x1254 RGBA source at C:/Users/klimp/.codex/generated_images/01a103a9-fc50-74d1-ac9f-b02aaad3a17d/exec-a40f2482-4af8-46b6-bd70-4ac9007dfbe8.png, SHA-256 7770D08F7DE7D6FAC1181D7B1C1AD2C108506EDCE2149821149817423EEDD443. Its alpha range is 0-255, all corners are transparent, and bounds [105,52,1037,1214] leave clear canvas margins. Its 64x64 processed PNG uses premultiplied-alpha LANCZOS downsampling and has bounds [9,9,55,55], zero-alpha corners, and no observed halo or unintended holes. The selected source/processed/DDs hashes and exact pixel-equal round-trip evidence are in reviews/asteroid_residual_haze_lineage.json.

## Conversion and review gate

Parent correction dated 2026-10-04: the BC3/DXT5 request was mistaken. The exact asset-skill contract is one-level legacy uncompressed BGRA at the native 64x64 idea canvas, and the installed Vanilla idea DDS precedent is BGRA. The correction changed format documentation only and did not trigger image regeneration. All seven staged DDS outputs use only .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py and passed strict header, alpha, and pixel-equal round-trip checks. No custom encoder, compressed variant, or runtime write was made.

The parent reviews the native and enlarged contact sheets and each icon before runtime promotion. Staged art and DDS files do not prove live-game behavior; the user owns HOI4 validation.

## Parent DDS format correction and exact staged outputs

The parent corrected the earlier BC3/DXT5 request on 2026-10-04: the requested format was mistaken, and the strict contract is a one-level legacy uncompressed BGRA DDS at native 64x64. No custom encoder or compressed version was created, and the format correction did not trigger image regeneration. The seven existing converter outputs below use only the required repository tool and each passed strict 128-byte BGRA header checks, 64x64 dimensions, 16,512-byte length, alpha range 0-255, and exact decoded-pixel equality against the processed PNG.

| Requirement | Exact staged DDS | SHA-256 |
| --- | --- | --- |
| E028-IDEA-01 | docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/dds_candidate/asteroid_residual_haze.dds | 0518CCDD5B7FE74FB79A664629B5F153F043182B7B119F971BD541253B6C7A9C |
| E028-IDEA-02 | docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/dds_candidate/asteroid_global_dust_veil.dds | C2F7205D51DA91DD32D3E400CCBF5926759B07D9A3853E52BEEF07904BB47DCB |
| E028-IDEA-04 | docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/dds_candidate/asteroid_severe_impact_winter.dds | C29464B0E919EA52DB467302DAA260DC2C5CA8725BC0D45B3CFA4DE7566EEC1D |
| E028-IDEA-05 | docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/dds_candidate/asteroid_dust_protection.dds | D2B78377B03EEE904991771A128ADFEACC04E413DE0E187A0762BE3587D95CD7 |
| E028-IDEA-06 | docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/dds_candidate/asteroid_recovery_burden.dds | EF55B32E63401EB4AB08ED44230B935EC64E15319A60AE286810F8F02F889F4E |
| E028-IDEA-07 | docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/dds_candidate/asteroid_main_crater_material.dds | C649AD67DDC7B332416B0E3320034D2165553FECFE353E0531F452145CE93EAE |
| E028-IDEA-08 | docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/dds_candidate/asteroid_fragment_material.dds | 65146DD2770F3A477BBE981617469A41B219AC24DE611E67F900477717FFB62F |

The reviewed stage sheets are docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/contact_sheets/idea_icons_native_lineage_v001.png (SHA-256 B3552F1E63424A916EC4580EF07748CE1E2DE667C11AA5E6B3BD606F9B138A40) and docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/contact_sheets/idea_icons_smooth_4x_v001.png (SHA-256 CF10426AABCCF30DAB2C75E00559C0C275360B9D07369066BEE7FC3EF8355AB6). The blocked Impact Winter row shows rejected v004 review evidence and explicitly has no selected processed PNG or DDS.

## Evidence revisions

- AGENTS.md: 38E479CB75828BA888860BE8BC3739F9286C0D925CC7D8DE5ECD3B8DADEC46CF
- chaos-redux-event-assets/SKILL.md: 7A728CCBAB2CCF3483B1932A99BA971622F5086767BD2CFA76C313A4EF02B279
- chaos-redux-subagents/SKILL.md: 06079FB7E7C01BF09A5FEA1FFABDFBB73B99FCECDDD28EF7720415FBBCEEDA61
- official imagegen/SKILL.md: 706D4D96E1D5C9E6023FE3CCABBA1BB34B364024D344FD25B8515EC7D28FE3C4
- official imagegen/references/prompting.md: D957A45CB24FE2CF1A85858674FC533F15A5F4621355F559A13A93168999C2DD
- official imagegen/references/sample-prompts.md: 76CC8A2988EFB6E844A99FF9908B2B11CC07467510FC909002ABCC0EE3F0701B
- Part 9 visual/audio direction: 84D700D60E6E627E1F01DF0F6B97C9DC88C346647396BA6200BE8252A48F3209
- Event 028 asset prompt: 5EBA720782D83018D17560E7B63DEDF003F03F6704741BE519E2292464D70669
- Part 3 impact damage/aftermath: F81C3B5C3FDBAF72879DE8AF5C34A1DF1D93926D2EA5DF5D9640C4F6878973E0
- Part 4 dust/global recovery: 503C1B916D28D05776947C64DDB044FE1EFB10CFA2FFA072FE8237721691AB92
- Parent asset audit: 7596D1B0EB492CC11C6834D0AB59BEB1A73B713D00395C17E35B03F798F41EA9
- Parent asset records: 6D873659A29B79A907B732AABD5B2E0AD90231CF18F0B69C6BBFC096B9F4C4F0
- Parent source recovery handoff: 3A0C6B23B1CE459B7360556D0F2226BB59194B517A82E786EAA5CE27A52D150C
- Mineral uncapped-armour handoff: C6E9B9F00F6740BF92187ADF37BE650C0EC4B43191D8266EA83CF1EAA0E861FD
- Current interface/028_asteroid_incoming.gfx: EDEDE7E51B0AC62B7A63BD3FA6C96A2F55F5BEAEFE7E778CFBF20FC0AE73BEFF

## Parent runtime promotion record — 2026-10-04

The parent completed the before-hash check and promoted all eight accepted candidates to the exact existing runtime DDS paths listed below. This record supersedes the earlier stage-only and promotion-pending status text above. Before promotion, the parent verified every existing runtime DDS hash against the current baseline and backed up the originals under docs/assets/028_asteroid_incoming/regeneration/ideas/v001_20261004/runtime_before_20261004/. All eight new runtime DDS files are byte-identical to the accepted staged candidates.

| Requirement | Exact promoted runtime DDS | SHA-256 |
| --- | --- | --- |
| E028-IDEA-01 | gfx/interface/ideas/028_asteroid_incoming/asteroid_residual_haze.dds | 0518CCDD5B7FE74FB79A664629B5F153F043182B7B119F971BD541253B6C7A9C |
| E028-IDEA-02 | gfx/interface/ideas/028_asteroid_incoming/asteroid_global_dust_veil.dds | C2F7205D51DA91DD32D3E400CCBF5926759B07D9A3853E52BEEF07904BB47DCB |
| E028-IDEA-03 | gfx/interface/ideas/028_asteroid_incoming/asteroid_impact_winter.dds | A24A12E0EC920148920D4E162F8678249CF0469D4358E2D23FB50A7A56D5E14A |
| E028-IDEA-04 | gfx/interface/ideas/028_asteroid_incoming/asteroid_severe_impact_winter.dds | C29464B0E919EA52DB467302DAA260DC2C5CA8725BC0D45B3CFA4DE7566EEC1D |
| E028-IDEA-05 | gfx/interface/ideas/028_asteroid_incoming/asteroid_dust_protection.dds | D2B78377B03EEE904991771A128ADFEACC04E413DE0E187A0762BE3587D95CD7 |
| E028-IDEA-06 | gfx/interface/ideas/028_asteroid_incoming/asteroid_recovery_burden.dds | EF55B32E63401EB4AB08ED44230B935EC64E15319A60AE286810F8F02F889F4E |
| E028-IDEA-07 | gfx/interface/ideas/028_asteroid_incoming/asteroid_main_crater_material.dds | C649AD67DDC7B332416B0E3320034D2165553FECFE353E0531F452145CE93EAE |
| E028-IDEA-08 | gfx/interface/ideas/028_asteroid_incoming/asteroid_fragment_material.dds | 65146DD2770F3A477BBE981617469A41B219AC24DE611E67F900477717FFB62F |

The parent verified the promoted outputs as 16,512-byte, one-level legacy BGRA DDS files: 128-byte header plus 64x64x4 pixel payload, no FourCC. Impact Winter's v004_parentcrop_v001 is accepted parent mechanical normalization of the unchanged v004 source, not a fifth ImageGen call or a painter fallback. The original producer rejection remains historical; the independent parent edge proof and accepted disposition remain documented in the staged lineage without rewriting the producer criteria.

The v003 family contact sheets are frozen at the accepted pre-promotion review point; their “promotion pending” captions are superseded by this record. No source, prompt, receipt, contact sheet, semantic choice, GFX declaration, or other runtime asset was changed by this documentation update. The parent performed runtime promotion; no live-game validation is claimed, and the user owns HOI4 validation.

No asset substitution or unapproved fallback was used.
The original producer's four-attempt Winter block and seven-row review-pending stage are historical and are superseded by the parent acceptance and runtime promotion above.
All eight current idea rows are parent-art-accepted and runtime-promoted; native consumer acceptance and full Event 028 completion remain open.
