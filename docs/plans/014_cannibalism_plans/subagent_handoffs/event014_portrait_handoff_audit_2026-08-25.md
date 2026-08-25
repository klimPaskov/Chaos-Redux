# Event 014 portrait handoff audit

Audit date: 2026-08-25.

Scope: read-only audit of the CBA-CBH regional warlord portrait package, its 64 stable aliases and 16 unique runtime textures, and the protected static `hannibal.dds` and `hannibal_wendigo.dds` textures. This audit changed only this handoff; it did not change images, gameplay, characters, GFX, localisation, or RunPod state.

## Verdict

Status: **BLOCKED / needs_user_review**. The current warlord package has strong file-level crop, hash, DDS, and wiring evidence, but it cannot be accepted as a completed portrait-worker handoff under the current portrait-production contract.

- No explicit `chaosx_portrait_creator` execution receipt, worker handoff, or route marker was found in the current Event 014 evidence. The retained v7 contracts record format checks and parent-requested framing work, not ownership by that portrait worker.
- The 16 contracts classify the source as `sourced_modern_fictional_2d_direct_user_authorized` HATE art by Adrian Smith, hosted/referenced by Alkony and credited to CMON. The current skill gate requires native ImageGen evidence for fictional or impossible one-person portraits; the direct-source branch therefore does not satisfy the current mode gate. No regeneration or substitution was performed.
- The required durable archive `docs/assets/portraits/014_cannibalism/` is absent. The retained package is under the temporary Event 014 workspace `docs/assets/014_cannibalism/portrait_source_recovery_v6/selected/`.
- Every retained `*_source_crop.json` points its `master` and normalized command at the deleted `docs/assets/014_cannibalism/portrait_source_recovery_v6/candidates_external/hate_art/individual/` input directory. The co-located `*_original.jpg` copies survive, but the recorded source command is no longer reproducible from the workspace.
- Attribution and source URLs are recorded in `provenance_matrix.md`, the source-page archive, and each contract. Rights are only `reference_only_user_authorized`; no permissive redistribution licence or public-domain basis is asserted, and this audit does not grant one.
- The retained source-page reference is `https://alkony.enerla.net/english/the-nexus/board-games-nexus/board-game/hate-board-game-base-set-hate-board-game-coolminiornot-2019-board-game-base-set-review`; the package also records the per-image source URLs and CMON attribution in the matrix and contracts. No native ImageGen prompt, seed, or generation evidence is retained.
- The contracts label the set `source_placeholder/direct_source_2d`; worker 156x210/native-format checks and 4x-nearest-neighbour contact-sheet review are recorded, but the final parent recrop/live-consumer review is still marked pending. This audit does not promote that state to complete.
- No explicit styled-final replacement request is recorded, so `replacement_pending` is not evidenced. The current `source_placeholder` labels do not waive the route, mode, archive, rights, or review blockers above.
- The older July 2026 imagegen handoffs point to removed `leader_portraits_refresh/...` packages and cannot be used as current native-ImageGen prompt/source evidence.

## CBA-CBH warlord evidence

The exact shared evidence prefix is `docs/assets/014_cannibalism/portrait_source_recovery_v6/selected/`. For each basename below, the retained paths are `<prefix>/<basename>_original.jpg`, `<prefix>/<basename>_source_crop.png`, `<prefix>/<basename>_source_crop.json`, `<prefix>/<basename>_156x210.png`, and `<prefix>/<basename>.txt`; the runtime path is `gfx/leaders/014_cannibalism/<basename>.dds`.

The hash column is `original SHA-256 / source-crop SHA-256 / processed PNG SHA-256 / runtime DDS SHA-256`. All listed processed PNGs are 156x210 RGB, all listed runtime DDS files are 156x210, 131168 bytes, one-level uncompressed BGRA, and the retained v7 validation records DDS round-trip equality.

| Runtime basename and retained source identity | Original / crop / final dimensions | Hashes: original / crop / PNG / DDS | Recorded state |
|---|---:|---|---|
| `leader_CBA_warlord_middle_east` — UmCal Champion | 639x626 / 260x350 / 156x210 | `709941d00812c74426bc3da5ee75c9444b406cf1b75bc11b7cfb70b0127ae486` / `0bad6a799df250ca52d96f218be0e0d7f1e3567e60cbfa41e1cea8b461ca3e1d` / `9bc8efd4ab2a46f3834481180062983e30d0d75a447327d1874de3af178fc1d9` / `c6c8b35972fd90c40a87b3260064094e429c8c3aa4f6a8d8ec807b7f3098f5fb` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBA_warlord_south_america` — UmCal Prince | 639x636 / 260x350 / 156x210 | `502d754c06da147a1dfe6ef5db5a291a8279354cc5146dad074d47feb5f97cd7` / `a98c3c0efda86e188a3d042becc68101abf2be2baae57124c47d1a7b2b1616a9` / `643c0ebd506c75d99296feb08d8557eae31f059c598f96a0cc13e61196c99f93` / `de435c5d9e05b1742348fb476903ade185f71870c30f9eaee097a063ab8d255d` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBB_warlord_middle_east` — UmCal Warrior 1 | 639x670 / 260x350 / 156x210 | `9abe67aaa3980881fb106a07f3c9a8b5314b41d1df028a5fa42239eadab1455c` / `fbe1b17583cd86830471f9e6ceaee6c0a92cd5bfa6f4070b1746a34bdaa8b5c6` / `d3bddf8b52181573c54e8fb3fa3c524fb210c8c929426f65a869e13e3fa67e81` / `b7d084dcdac9f75ce9b85b751d238a170d7a4d0e18837c89c5a83dfbc967d795` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBC_warlord_south_america` — UmCal Warrior 2 | 639x708 / 260x350 / 156x210 | `3b5103ba13f00503a88609795e89569d3789ae41702cc3df5d3cc6105054f5a6` / `a60f093ab88a1baf953ab448ba51c817088e0347e369d97cca5f35e24a52d2a7` / `2d73b26b01a01bd63b2230540589a77e1e45331776ded9d5dde298fa5aa8de0d` / `0982e8e559932f3c591f86d4b5529bcf5734502015eb9fa3f562db3ff2f82b9c` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBC_warlord` — UmCal Warrior 3 | 639x650 / 260x350 / 156x210 | `0b45fbbf20df74c811304a4c18134fb3820585ecdf833bcb195f0d69d3bf756f` / `fd4d76b55b9c23b86bd6126363a5c980920fad4debe5129ebfe5ef17923aa1f1` / `0b942af3117df6b846a2dd860e618c55a88ceee1a03b97bcbd806dc686a3483c` / `48e341f4cef25e001443d1f1f03a5b61ea4b22e2a99cf580eef7dfe4b6b86dd1` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBD_warlord_north_america` — UmGra Champion | 920x920 / 312x420 / 156x210 | `7b459af75368acd858996163833eb7f7a27f915124d1961003e5c6f69eaf8691` / `f4ce6506eee50d5a29b397a7adf5307380f9c510f286c5a7822ccb19f527ed35` / `61f39495612b55b662990cb4a7350e3289db8e49e9e88e7ff7e7c4391b3f2dc6` / `de5f1724a8552ea514807dd625ac6d2a2a08d0f4fb374e9de29dded305da3ab5` | `source_placeholder`; special backdrop cleanup retained |
| `leader_CBD_warlord_south_america` — UmGra Prince | 639x774 / 260x350 / 156x210 | `e252e82e96aadcad805cf7b7a9d75ca388366ba263ebd0f530b4938c0d027b5c` / `c9fa055a0434f8cfdd352f7f3a165ddd4c68562744d926b2c4eceff148b93459` / `4c45f2bfefa74d66fed5fb4cc3a60d2ebb37b1a73e6a08421ab859051a387218` / `1da0c1cb9af5101506d0c2e40c5a6d154d5e61def98e0dcbfd0c40b9c5cd2a07` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBE_warlord_north_america` — UmGra Warrior 1 | 639x659 / 260x350 / 156x210 | `c05d86f699274505b86ac60a7d0bf2c26411ec683c27eb71a62f59edda780bb9` / `00349e3939e5f723866adbd3d8d18ca73ba22a0da80cd46cc6e45fbb33cec311` / `10a809056712a8f170d59b4b42408f70d11de1fbb8ef975870dafbbd48338a9a` / `19ac68a8bbe2c4575fd598cbfc13ecaae03c9cea9bff2fa8a3972e80c1e29099` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBE_warlord_south_america` — UmGra Warrior 2 | 639x681 / 260x350 / 156x210 | `2129af54948660f87e1351d789961f69c26ca6910558ae59277bcac589a10c2d` / `3d34b02dbfc8d8c8c032da46bb125a9f7d00fadb779266ff27dea5df54d6c2ce` / `0dfe6507c81070719b991ebe46153574e28a7894fdcbe18482704eed462aa5e1` / `9116b2e0b49f1b57f8e41e6faab1429e141ab8d2d33638e1f9069be8c65b37c4` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBE_warlord` — UmGra Warrior 3 | 639x671 / 260x350 / 156x210 | `259dc113ec50c0bf39c4b5eaa5458973b80055b79f833805f6a2219257886c3a` / `56c578c7ffccaaace0545ac1da14d78979b5f6cfca93e16f8c0e509fc30ebdaf` / `56f628d1ab076801db6162981b57c861a0d0e339a4265a89f4501d6f234126b3` / `ad551fc190b873d93fbe9fe17907d285d6c3dac5722cdea7ead96370ed190c10` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBF_warlord_africa` — UmKator Champion | 639x628 / 260x350 / 156x210 | `2f86fb72cbf6fdf6b422876a5c3b2debe1563e66bb7bfedbf9790d09eef533ef` / `66f4efc5df7d0385b8d96dd11fe35f94e97a566e5267c9da6c1e475a50e529dd` / `8bee4bcb75d94577ead0fd910c8abc6cf49d9ecdcf0ef2e4abf89066d840da06` / `a36bc1fd5d2b8334d996139fbde75ceec6d221ff2337b652f1f4bc0edc9a2a07` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBF_warlord_oceania` — UmKator Prince | 497x600 / 260x350 / 156x210 | `e28e9b5224306e4562ee1500ae5731f8c7f5f6efd109eb9f07a5cbad00629419` / `d3fbf6c8f879eafa0811f7672e4e6be6346b9952d82b00ef2f11288728a3c078` / `d004ab7b520e2a26b9215bdbc286a6d58e6e1aa1ae6f8dcb75a21e054c73e7ad` / `0160a0463e044a110e763ba590d71c66990bb0485cdaf9991c708f84f3a85c1a` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBF_warlord` — UmKator Warrior 1 | 606x600 / 260x350 / 156x210 | `5d083f9e9bbb87665229f87bde0d9d608467a2d2613d090b642faf932c403e1e` / `e49374a4fe62f3859cd848badbb3bdc1562529c30f33bea65ba9ef4e754d87e8` / `f0f15c69d9b7ccd76a2263f4d6e562513f33b7aaffd5e5d713d290df09cb0603` / `0e2fabef510fe103453e69ddb4f1b8e5fd66f7871d7ff60d6d63eec6e4923970` | `source_placeholder`; reused by CBG regional aliases |
| `leader_CBH_warlord_north_america` — UmKator Youngblood | 577x600 / 223x300 / 156x210 | `7a72ea9660c2ff97ce2512457fb55a8db99a692e631b51c9654751a2443535b1` / `c6ea722d0e064b869ae3de7a59deffc6a771c272cea6b3e00ded4aa085a80b83` / `5f9faa8f9ecd35a016d6d3afde3dd62a6bbec3c5d02b128075563a5fd1fcee12` / `aff4159b8faf950b25404e6ed81c1040117e33f1cb309cd107e27309de6fc3f1` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBH_warlord_south_america` — UmRak Champion | 598x600 / 260x350 / 156x210 | `c9db8fbd240418a45ea84717f9d0e142dedd081f61504b651280540058aec66a` / `e6725ee483ff04bf3093b76d3c0e2b544afbf3fc89a258db0241fbdcdebf4fa1` / `65c2114ce68574fcd6cb02747b4b1b39585ec033d47b4120d7c2fefce184b65f` / `e5f8643a9a2bf85ddbca4955752327e2c5f754232c7cccee3329eb65303669da` | `source_placeholder`; v7 crop/runtime checks recorded |
| `leader_CBH_warlord` — UmRak Youngblood | 571x600 / 260x350 / 156x210 | `0eb86c7de71f03d857afa08bbdb62a7ef8bbd40fe250a369b1814cfdb9fcb2fe` / `965d291a463438bc1575dba35ae46bed75f90823686fdc2abac09b8785c1f0c7` / `afdcf3c2bab92c99d1169e56f924a56bc930e9c8dee500e5e24694dc453ea62b` / `2e7401457a4c9e3df428a85c392137f623bd6ad56864783adf0104cf58e71896` | `source_placeholder`; v7 crop/runtime checks recorded |

The CBD North America source has the retained backdrop-cleanup notes and contact sheets; the other exact crop boxes are in their co-located JSON files and `docs/assets/014_cannibalism/portrait_source_recovery_v6/selected/provenance_matrix.md`. The source-page archive contains 16 HTML pages under `docs/assets/014_cannibalism/portrait_source_recovery_v6/selected/source_pages/`, but it is not at the required durable portrait archive path.

## Canonical Hannibal textures

| Runtime asset | Observed file evidence | Current wiring and review state |
|---|---|---|
| `gfx/leaders/014_cannibalism/hannibal.dds` | 156x210; 174608 bytes; SHA-256 `5c48c9a5b503c3185dcb38ee1aabc403d7668094079b78a20010323930d10b88`; valid 32-bit BGRA DDS; mipmap count 8; opaque alpha | Referenced by `GFX_portrait_CBL_hannibal` and `GFX_cannibalism_revealed_portrait_static` in `interface/014_cannibalism.gfx`. No current original, source crop, processed PNG, provenance contract, or independent static-portrait review is retained. |
| `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` | 156x210; 174608 bytes; SHA-256 `26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717`; valid 32-bit BGRA DDS; mipmap count 8; opaque alpha | Referenced by `GFX_portrait_ZZZ_hannibal_wendigo` and `GFX_cannibalism_wendigo_portrait_static` in `interface/014_cannibalism.gfx`. No current original, source crop, processed PNG, provenance contract, or independent static-portrait review is retained. |

These protected static files are mipped existing textures; the standard one-level 156x210 BGRA output would be 131168 bytes. This is an observed legacy-format exception, not a request to replace them. The animated sheets remain separately protected: `leader_CBL_hannibal_sheet.dds` is 1872x210, 1572608 bytes, SHA-256 `f67a1b33a1d4f9b9b1b5ec0d6fb716ad1f2342083e9992550b5dd7356f590587`; `leader_ZZZ_hannibal_wendigo_sheet.dds` is 2496x210, 2096768 bytes, SHA-256 `f0dfa61ea29293f8393711f97eb67524d336cb6c2a2d55734c0c38484219d18b`.

## Runtime wiring audit

- `interface/014_cannibalism.gfx` defines 64 CBA-CBH warlord aliases resolving to 16 unique existing DDS paths. No alias path is missing. The stable names are consumed by `picture = GFX_portrait_[WARLORD_SLOT]_warlord_[WARLORD_REGION]` in `common/scripted_effects/014_cannibalism_effects.txt` at the dynamic warlord and integrated-corps creation sites.
- `common/scripted_localisation/014_cannibalism_scripted_localisation.txt` supplies the CBA-CBH slot and Europe/Asia/Africa/Middle East/North America/South America/Oceania token variants. The CBA-CBH warlords are dynamically created, so they are not character entries in `common/characters/014_cannibalism_characters.txt`; the static Hannibal entries are wired there to the two named GFX sprites.
- No runtime path points into `docs/assets/014_cannibalism` or the absent `docs/assets/portraits` archive.

## Reference and validation evidence

The matching installed-vanilla leader reference family was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`, including `contact_sheet.png` and the eight 156x210 references `afg_mohammed_zahir_shah.png`, `africa_generic_1.png`, `den_thorvald_stauning.png`, `eth_haile_selassie.png`, `fin_carl_mannerheim.png`, `ice_sveinn_bjornsson.png`, `ire_eamon_de_valera.png`, and `lux_charlotte.png`. The references confirm the leader-role dimensions and framing family; no vanilla art was substituted.

Read-only checks matched `docs/assets/014_cannibalism/portrait_source_recovery_v6/selected/portrait_recrop_v7_validation.json` (`status: PASS`, `count: 16`, and round-trip equality for each warlord DDS), the per-asset contracts, the v7 contact sheets, and the current runtime hashes. The required converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` was not rerun because this audit made no PNG/DDS changes. Native ImageGen verification, durable-archive promotion, source-command repair, static Hannibal provenance recovery, independent final portrait review, live HOI4 review, and RunPod work were intentionally skipped.

## Blockers and handoff boundary

1. A portrait-worker route receipt and independent portrait-worker review are missing.
2. The current fictional source branch is direct user-authorized HATE art rather than the native ImageGen route required by the current skill gate.
3. The durable per-portrait archive under `docs/assets/portraits/014_cannibalism/` does not exist.
4. The recorded source masters and normalized extraction commands reference deleted files.
5. The source is reference-only/user-authorized with no asserted permissive redistribution licence.
6. The canonical static Hannibal textures have no current source/provenance/crop/review package and use an observed eight-mip legacy DDS format.
7. Final parent/live-consumer review remains pending.

The user remains the sole operator of RunPod for any grounded HOI4-style replacement. This audit neither opens nor operates RunPod and does not claim completion or authorize image replacement.
