# Event 018 cave-monster static closure audit — 2026-08-10

## Disposition

Status: `needs_user_review`.

Static closure is not granted. The engine-facing files are present, internally connected, checksum-stable against the promoted production hashes, and structurally parseable through the locked Paradox format stack. No runtime asset defect was found in the mesh, animation, material, entity, sound-definition, or counter registrations.

The package nevertheless retains real non-live validation gaps that the user's no-HOI4 boundary does not erase: the existing handoff still assigns parent review of idle/move readability, the installed audio, and the ten counter strips; the temporary preview/contact-sheet evidence was deleted with `docs/assets/018_resources_found/`; and no equivalent durable visual or audio review artifact remains to rerun those checks. The exact audio trim/fade/normalization commands were also not promoted. The prior `needs_user_review` and `implemented_pending_live_review` labels therefore remain honest and were not changed.

HOI4 was not launched. In-game presentation, entity-state transitions, audible density, and map-zoom readability were not tested, as explicitly required by the user.

## Scope and files changed

This was a bounded static audit. No model, texture, animation, entity, sound, counter, gameplay, localisation, GUI, spreadsheet, or temporary `docs/assets` file was created or changed.

Created:

- `docs/plans/018_resources_found_plans/subagent_handoffs/event018_cave_monster_static_closure_2026-08-10.md`.

The authorized existing handoff and integration addendum were inspected but not edited because the evidence does not support closure.

## Dependency and route evidence

- `MESHY_API_KEY` was present and nonblank before repository intake. The value was not exposed.
- Current dependency lock: `.tools/3d_pipeline/config/dependencies.lock.json`, SHA-256 `D764E440754241E58A066A7BE8F95F97B7D682B3568AC9FF46D49A33C092EF16`.
- Current live-schema lock: `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`, SHA-256 `DBB9CAD7FB12AFE81ECA05A2F381EF4251C035F4D22BF17856A2F6D41F16A62D`.
- Current adapter configuration: `.tools/3d_pipeline/config/blender_hoi4_adapter.json`, SHA-256 `225D5BE4E7517B2C340EDF2D0F7AD522A7940664B09A7A193F68C5941D45748B`.
- Official Meshy route recorded by the lock: `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, wrapper `.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd`, schema revision `live-declaration-2026-08-05`.
- Current locked Blender HOI4 adapter: `chaosx_blender_hoi4` 1.2.2. The historical production handoff records adapter 1.2.0; this audit used no Blender mutation and did not rewrite historical lineage.
- Blender lock: 5.1.2 build `ec6e62d40fa9`. The executable's Windows file metadata reports the 5.1 product line. Blender was not started.
- `io_pdx_mesh`: 0.91.0. Installed manifest SHA-256 `C6865CEB3CE323BD54255BB37FF860E03607BD2AABED4057E9DCBE04C29682EC`; locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`, exactly matching `.tools/3d_pipeline/vendor/io_pdx_mesh/blender-io_pdx_mesh.zip`.
- No provider, balance, paid, Blender, or adapter operation was called. Audit credit consumption was zero. Historical lineage remains one legacy Meshy image-to-3D task `019fd394-e30c-7fbb-b0da-ee8078b86c38`, 20 estimated and 30 consumed credits, with no paid retry or downstream provider operation. Meshy 7 is required for future generation.

## Actual-byte mesh and animation audit

The installed `io_pdx_mesh.pdx_data.read_meshfile` parser read the current runtime `.mesh` and all four current runtime `.anim` bytes directly.

### Mesh

- `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster.mesh`: 1,876,278 bytes; SHA-256 `60C256EC1D958F77A93B6F9019A4B7C60072EA2F6B13E69C3672B84C474A491C`.
- Parsed object: `Mesh_0.001`.
- Parsed topology: 18,927 exported vertices, 30,000 triangles, maximum triangle index 18,926, one UV set, normals and tangents present.
- Parsed skin: four influence slots, 17-bone skeleton, no zero-weight vertex, every weight sum exactly 1.0, no positive bone index outside 0–16, and no weighted negative bone index.
- Parsed material: `PdxMeshAdvanced`; diffuse `resources_found_cave_monster_diffuse.dds`; normal `resources_found_cave_monster_normal.dds`; specular `resources_found_cave_monster_spec.dds`.
- Parsed AABB: minimum `[-4.1943497658, -0.0031263828, -6.5398874283]`; maximum `[4.1915650368, 7.3532309532, 6.5516967773]`; dimensions `[8.3859148026, 7.3563573360, 13.0915842056]`.
- The exact parsed vertical extent is 7.3563573360, while the promoted handoff records 7.3518247977. At entity scale 0.8 those become 5.8850858688 and 5.8814598382. The difference is small, but the deleted production evidence no longer preserves the exclusion or measurement convention needed to reconcile it. This is a crosswalk precision gap, not evidence of a visibly broken model.

### Animations

| Runtime file | Bytes | SHA-256 | Parsed FPS | Parsed samples | Duration | Joints | Static conclusion |
| --- | ---: | --- | ---: | ---: | ---: | ---: | --- |
| `resources_found_cave_monster_idle.anim` | 25,276 | `A8EA9301744231054D3DA131AAF7D2EF264E13FD48A5F737325BA531DC9762D0` | 24 | 49 | 2.000 s | 17 | first/last root translation equal; scale samples all 1.0 |
| `resources_found_cave_monster_move.anim` | 14,367 | `077D8ADCB45484215DB7BA6F4F45D95B184785358441DA67980B0D061EB52246` | 24 | 25 | 1.000 s | 17 | first/last root translation equal; scale samples all 1.0 |
| `resources_found_cave_monster_attack.anim` | 17,798 | `13D54654770BD0E82846F847F4CDD14535755F061BA83DB2254F821FD2BB19AA` | 24 | 33 | 1.333 s | 17 | first/last root translation equal; scale samples all 1.0 |
| `resources_found_cave_monster_death.anim` | 20,660 | `5A4677B24D0CB4ED3F506DDB1666B263AABF6D3CDB098255560DF6F773E1601A` | 24 | 37 | 1.500 s | 17 | deliberate terminal root displacement of -0.431584 on the sampled collapse axis; scale samples all 1.0 |

Every sample array was consumed exactly according to the joint channel declarations; there were no truncated or surplus translation, quaternion, or scale samples. This is actual-byte parser evidence, not a filename or existence check. It does not replace the missing visual review of the motion read.

## Material and texture audit

All three model DDS files have valid 128-byte legacy DDS headers, 1024 by 1024 declared and decoded dimensions, 32-bit BGRA masks, `DDSCAPS_TEXTURE`, and exact byte length `128 + 1024 * 1024 * 4`.

| Runtime texture | SHA-256 | Decoded channel evidence |
| --- | --- | --- |
| `resources_found_cave_monster_diffuse.dds` | `A876F57B87A36A79FE7A320D4445BD112CBA957474028E1E5680C0439626FE11` | nonempty RGB, opaque alpha |
| `resources_found_cave_monster_normal.dds` | `9EF36A184A57A7BD451A6F90C6CB23D50CFC884EE6EE7FBF0958ABB0F3309D19` | populated packed normal channels |
| `resources_found_cave_monster_spec.dds` | `9CFC7A88676CE46E4F017381DB38860BDBF84555C1BC59020C2D0FE4D2B88CDF` | R 0–1, G 31–33, B 0–134, A 95–212; not a raw grayscale roughness map |

`gfx/entities/018_resources_found_cave_monster.gfx` binds the parsed mesh object name `Mesh_0.001`, the three exact texture basenames, and `PdxMeshAdvanced`. Its SHA-256 is `99E2196F8EA4A5A7E7FB483E631EA429C3BFA8D225FC83AF3B2E69CB6D5F2931`.

## Action and entity consumer audit

- Animation registry SHA-256: `DD93E540F5A518CFDB606A325B0B42033EC0B0C156EF41A29D9C40AC6542851A`.
- Entity asset SHA-256: `72F8AD8EEACB9770727D9A4B488E4117326F614153F7AAEAFE0DDBF018B7548A`.
- The mesh registration exposes idle, move, attack, and death animation IDs, and the animation registry resolves each ID to the existing runtime `.anim` basename.
- The canonical entity binds idle/training, move/retreat, attack/defend/support attack, and death to the expected action IDs. Loop and next-state metadata agree with the intended semantic roles.
- Entity scale is 0.8 exactly once.
- All five `common/units/018_resources_found_cave_broods.txt` sprite tokens resolve through exact `<sprite>_entity` aliases cloning `resources_found_cave_monster_entity`.
- The five named DHO templates contain the matching brood sub-units. No runtime definition points into `docs/assets/018_resources_found/`.

## Sound consumer and runtime-byte audit

Sound-definition SHA-256: `F0B02F305B7BA83B042506B3BA5FFC39F077F81361A9A7D83D3A9B0EB1667460`.

Every referenced file exists as mono 44.1 kHz 16-bit PCM WAV, and every entity soundeffect resolves to a declared wrapper and source.

| Runtime WAV | Duration | SHA-256 | Entity synchronization |
| --- | ---: | --- | --- |
| `resources_found_cave_monster_idle.wav` | 24.240000 s | `2F3C569FA0333ECBE870D93B71B4B0E094FBDFD5CA4F107885A7155D9BE95AAA` | idle state entry |
| `resources_found_cave_monster_move_foot_01.wav` | 0.280000 s | `8ECD3DC57E6E53D687740E386DEDB811A5E804D8B244BD3CDB3DA5C686AB62CF` | move/retreat 0.125 s |
| `resources_found_cave_monster_move_foot_02.wav` | 0.280000 s | `1B83E1257BD6FFEA65DC78866782E2D0A8D4387C570471B60B3769BA2667C2C0` | move/retreat 0.375 s |
| `resources_found_cave_monster_move_foot_03.wav` | 0.274671 s | `DA7AE70FFC077E635E8938CDF4E6868272CDCDAB0F690E218BD63DC1983937E5` | move/retreat 0.625 s |
| `resources_found_cave_monster_move_foot_04.wav` | 0.280000 s | `9AE099698780D71DBF60B47710179E84830C57E48E8EBB67E4608D4774142300` | move/retreat 0.875 s |
| `resources_found_cave_monster_attack_bounded.wav` | 0.841723 s | `0437FB79CF23B8BA7D7B9A70E0CE95F72525A111E60D03AE5F16CAE193635949` | attack/defend/support attack 0.60 s |
| `resources_found_cave_monster_death_bounded.wav` | 1.500000 s | `CBBEE82F59FB93FCC7D9D569B3F4664DE32E5BFA8A7D3E402CA502A7528A6ADD` | death 0.75 s |

The integration addendum's first evidence paragraph still names the untrimmed move/attack/death durations 6.384, 9.020, and 6.000 seconds. Those are historical pre-trim values, not the current runtime files measured above.

### Recovered source identities

The temporary originals are intentionally absent. The parent independently reconstructed the following durable source identities during this closure pass:

1. Idle: `https://commons.wikimedia.org/wiki/File:Alligatorbellow1.ogg`; direct identity `https://commons.wikimedia.org/wiki/Special:Redirect/file/Alligatorbellow1.ogg`; U.S. Fish and Wildlife Service, public domain; prior original SHA-256 `72A5612E99B6A941D751EFBCCF1E44F816C06C7884E3108C5298A2BA84B25169`. A fresh download matched exactly.
2. Move: `https://commons.wikimedia.org/wiki/File:Walking-on-gravel-38827.ogg`; direct identity `https://commons.wikimedia.org/wiki/Special:Redirect/file/Walking-on-gravel-38827.ogg`; CC0 1.0; prior original SHA-256 `14990DE1FD15418B55A2C939B0A99348446E613C1C4A5A307E49A87D228DE5EF`. A fresh download matched exactly.
3. Attack: `https://commons.wikimedia.org/wiki/File:Lion_raring-sound1TamilNadu178.ogg`; direct identity `https://upload.wikimedia.org/wikipedia/commons/7/7d/Lion_raring-sound1TamilNadu178.ogg`; author `தகவலுழவன்`; public-domain self-release; prior original SHA-256 `AB237D0F960E83412251D0C11F69959F3C2E8D3B14595F7181C3056F7FA18BF7`. Wikimedia rate limiting prevented a fresh byte-hash comparison in this pass.
4. Death: `https://commons.wikimedia.org/wiki/File:Assorted_gravel_rock_and_stones.ogg`; direct identity `https://upload.wikimedia.org/wikipedia/commons/a/a3/Assorted_gravel_rock_and_stones.ogg`; author `stephan`; public-domain release; prior original SHA-256 `BC254F5C70EE0252FDC79278F83E5428B6953807CFC21805052E6A617F2BB330`. Wikimedia rate limiting prevented a fresh byte-hash comparison in this pass.

The durable evidence establishes mono conversion, 44.1 kHz PCM conversion, four movement slices, and bounded attack/death trims. It does not preserve the exact source intervals, fade lengths, gain or normalization values, or normalized command line. That transformation-recipe loss is a non-live provenance gap.

## Counter consumer and runtime-byte audit

Installed-vanilla precedent:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`: `GFX_unit_mountaineers_icon_medium` and `GFX_unit_mountaineers_icon_medium_white`, each with two frames.
- Large DDS: `gfx/interface/counters/divisions_large/unit_mountain_icon.dds`, 152 by 42, SHA-256 `5FEE91E79BEE9A0256F61EC1A06079B4EFED89D8220272983237EAE52488D557`.
- On-map DDS: `gfx/interface/counters/divisions_small/onmap_unit_mountain_icon.dds`, 60 by 12, SHA-256 `1F0FA721A4C92C4306A26DA5D791804998F504CB0DC9560874D57D5A2EA46E62`.
- Skill-local families inspected: `units/land/counters_large/contact_sheet.png`, SHA-256 `CD7ABDF70B38498D03744990BA91BFFF808686B1E8891049B8A78AD58E9B4243`; `units/land/map_counters/contact_sheet.png`, SHA-256 `23374FC38F26FC382DF60800C1086E074AC6BE46CDCD86B3EADDE686A99C8C26`.
- Vanilla large-counter palette evidence includes RGB 73/106/73; current large left frames contain the expected olive family, including 62/89/62 and nearby 63/90/63, 64/92/64, and 66/95/66 values. The right frames are separate grayscale schematic states.

All ten runtime counters decode successfully, use valid legacy 32-bit BGRA DDS headers, preserve two-frame canvases, contain real alpha, and are registered with `noOfFrames = 2` in `interface/chaosx_subuniticons.gfx`.

| Consumer | Large 152x42 SHA-256 | On-map 60x12 SHA-256 |
| --- | --- | --- |
| `cave_monster_brood` | `66780DC57FB379D4C1289AE8A81EB29FE09B8FC537503506C31B32A31F69F448` | `A529C4121C978CB91EADB9F71888E3C5A3A89EA49F87C62D8C551953A9F33075` |
| `cave_stone_phalanx_brood` | `25EF88CF7F293C12FABD7566FD4A5F37A33C323E34D41DF3A8634B21725D6D78` | `85AE98829D9D7FEF4B89788E7A74B8CCDE9BD66D6A621DC986A85B0769251D7E` |
| `cave_burrow_war_brood` | `75950783C46DF3B79EBCAE85768C3510AC6DFB4FB4BF7717820697BD3D9DA71B` | `24AC90A985703F2C3C5BBCCB5EF5A91D5DC320597B5DBFD946486195A320A60E` |
| `cave_scree_tide_brood` | `CEEE07B2126C50A6F7C3F8941BDB3FE9DAAFAC83D23982358DD0E26C5A43B17B` | `D369ABE1E928F5310774F56E30693F6B2CDAE40AB4FC0D30AF29ABBC6DDBDE39` |
| `cave_anchor_guard_brood` | `89381B6416F3763A9F0DFECAE0F03D6E88E830C6641B31D8DD362694E100FB1D` | `AB6F3C061D6279F35C071C4CE7780ACCD45769FECA7C7AB6A053CA8562FA79E2` |

The selected source PNGs, prompts, processed-alpha PNGs, decoded comparison sheets, and icon-artist handoff were not promoted outside the deleted temporary workspace. The runtime bytes are valid, but the old handoff's requested parent visual review cannot be repeated from durable evidence.

## Meaningful validation performed

- Parsed the actual runtime `.mesh` and all four `.anim` byte streams through installed `io_pdx_mesh` 0.91.0.
- Audited mesh object name, topology, indices, skin weights, skeleton, material names, AABB, animation sample arrays, FPS, frame/sample counts, root endpoints, and scale samples.
- Validated all model and counter DDS headers, exact lengths, decoded dimensions, alpha ranges, material channel statistics, and counter frame canvases.
- Measured every runtime WAV's format, duration, byte size, and SHA-256; resolved every sound wrapper and timed entity hook.
- Proved all five sub-unit sprite tokens resolve through exact entity aliases to the canonical model.
- Proved all ten counter sprites resolve to existing DDS files with the correct two-frame declarations.
- Verified current runtime paths contain no reference into the intentionally absent temporary workspace.

## Skipped or unavailable meaningful validation

- No HOI4 launch or live-consumer test, by explicit user instruction.
- No Blender reimport rerun because the deterministic job root was intentionally deleted and must not be recreated; actual-byte parsing was used instead.
- No model or animation preview rerender; that would require Blender mutation/output and the surviving durable package contains no preview files.
- No audible listening review; this environment performed byte and metadata inspection only.
- No counter contact-sheet visual review; the production contact sheets are absent.
- No fresh hash match for the attack and death source OGG files because Wikimedia rate limited those two requests.

## Blockers and remaining parent work

1. Decide whether to accept the previously documented producer visual conclusions as sufficient, or obtain a new bounded non-live preview/contact-sheet review. Without that decision, idle/move readability and the ten counter visuals remain `needs_user_review`.
2. Review the seven runtime WAVs audibly, especially the 24.24-second idle one-shot and repeated state changes. Static syntax cannot prove audible density or stop behavior.
3. Reconcile the parser AABB height with the promoted source-height crosswalk, or document the exact prior exclusion/measurement convention.
4. If complete transformation provenance remains required, reconstruct and record the exact source intervals, fades, gain/normalization values, and conversion commands. Do not infer them from runtime duration alone.
5. Keep the in-game limitation explicit: no live map model, animation state, sound playback, counter readability, or scale presentation claim exists from this audit.

No simplification or fallback was introduced by this audit.
