# Event 016 alien infantry Meshy firearm revalidation

Status: **V13 remains the accepted package; no regeneration or additional paid Meshy operation is justified**. The integrated firearm, genuine preset shooting action, genuine preset death action, six other distinct requested roles, final PDX bytes, and restored provider source artifacts are verified. Runtime muzzle/effect binding, strict audio-role gaps, parent consumer review, and live in-game acceptance remain unresolved.

## Scope and decision

This pass touched only `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/` and this handoff. No gameplay, entity, `.asset`, `.gfx`, sound-definition, localisation, decision, event, focus-tree, or spreadsheet file was edited.

The accepted provider geometry already contains the laser pistol as part of one Meshy-generated character mesh. Fresh reimport views show the weapon retained by the right hand in every critical phase; no separate gun prop, manual parenting, constraint, weapon bone, manual weighting, whole-rig substitute, transform-only action, or Blender-authored replacement motion was used.

## Locked route evidence

- `MESHY_API_KEY` hard gate: passed without exposing the key.
- Repository environment probe with live Meshy schema/balance: no findings; live balance 12 credits.
- Meshy MCP: official `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, SDK 1.29.0, compatibility revision `meshy-7-v5`, exact image model `meshy-7`.
- Dependency lock SHA-256: `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`.
- Meshy schema lock SHA-256: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- Blender adapter config SHA-256: `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.
- Blender 5.1.2 build `ec6e62d40fa9`; `chaosx_blender_hoi4` 1.10.14 health request `80c001abc32b4e0c839b70f6a4b7d7d0`; io_pdx_mesh 0.91.0 with locked ZIP SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- The required separate bridge probe initially found `127.0.0.1:9876` closed. The lock-selected Blender executable was started hidden with the required `blender_mcp` command, process 39384, and the second probe passed.

## Provider lineage and credits

| Stage or role | Meshy task | Preset/action | Live result | Credits |
| --- | --- | --- | --- | --- |
| accepted generation | `01a03dc3-905a-7d02-aba6-05500f877b97` | Meshy 7 image-to-3D | `SUCCEEDED` | 30 |
| remesh | `01a03dc9-8951-79ad-bc08-ae94ad607dfe` | triangle remesh | `SUCCEEDED` | 5 |
| rig | `01a03dcf-f0ba-7b67-b769-5a2678b03a40` | 24-bone Meshy rig | `SUCCEEDED` | 5 |
| idle | `01a03dd1-23a5-7728-9c09-f09683d64ffe` | 0 `Idle` | `SUCCEEDED` | 3 |
| move | `01a03dd1-28ea-7ba5-b6cc-dde26e5b2d01` | 692 `walking_2_inplace` | `SUCCEEDED` | 3 |
| laser attack | `01a03dd1-2d74-70b2-a151-e8d98c82e4de` | 223 `Draw_and_Shoot_from_Back_1` | `SUCCEEDED` | 3 |
| defend | `01a03dd1-31cc-7729-9612-26eb8f7d44c3` | 89 `Combat_Stance` | `SUCCEEDED` | 3 |
| support attack | `01a03dd1-35e5-7f37-a601-70982bdf5f74` | 234 `Walk_Forward_While_Shooting` | `SUCCEEDED` | 3 |
| retreat | `01a03dd1-3a02-7f38-8f3c-0236be3dc57e` | 685 `Walk_Backward_with_Gun_inplace` | `SUCCEEDED` | 3 |
| death | `01a03dd1-3dd9-772c-b0cd-9f7dc4de1fe4` | 183 `Shot_and_Fall_Backward` | `SUCCEEDED` | 3 |

Historical V13 production consumed 91 credits including the rejected 30-credit generation that omitted the gun. This revalidation consumed 0 credits and left the balance at 12.

## Genuine animation evidence

Fresh actual-byte reimport used `export/v13_firearm_preset/alien_infantry.mesh` with each final `.anim`. Role-order adapter request IDs are idle `14f0da7ee55c42d6b156cf830afa3dbd`, move `494d325dd20d4d649f2b40cc40fdfe26`, laser attack `557e9557048540f4bba7cd975989d21d`, defend `dfbb5f5300c84133ab6ce3b41af1ead9`, support attack `2b1f46f9e6984a158342add202ba8dbc`, retreat `d25ea42ad0a54a38bad95bc8e02940af`, and death `45f84dfe4b6a4412a0a37aedaad0f6ff`.

- Laser attack frames 1, 60, 118, 177, and 236 prove rest, draw, aimed two-hand support, reaction/recovery, and return to rest; the curated frame-145 view proves the cyan-tipped muzzle aimed away from the body at the selected discharge phase. The right-hand integrated grip is retained, and the left hand reaches the weapon only as part of the genuine Meshy preset motion.
- Support attack is a separate advancing-fire Meshy preset, not an alias of laser attack. Frames 1, 50, and 99 show advancing gait variation while maintaining the firing relationship.
- Death frames 1, 27, 54, 80, and 106 prove hit reaction, backward fall, impact, and terminal settling. Bounds height falls from 7.3910303 to 1.9005785, and the firearm remains integrated through the collapse.
- Idle, move, defend, and retreat each have distinct Meshy source task/action IDs and fresh five-phase reimport reports. Ground-contact deviations in the sampled reports remain within approximately `0.00001` source units.

The refreshed reports are `validation/reimport_revalidation_2026_08_26_{idle,move,laser_attack,defend,support_attack,retreat,death}.json`. Their SHA-256 hashes are respectively `B851FCE4BDBE90DBBE179103EFA9E8434303902F0862A235C4E52A9C08363455`, `D69A6B1E023C8C46A59EFCDD89ED020F7AFDCEC89647AF5D02385082E72F3054`, `2224E58DC8B099220BC9DB1F0A5290ECBA5333408F5990278B5D2346A9E3B2E1`, `7D9A97FEB0669C66E153DBC5EE54C97C5876B4BD930A9FAB76DBB6DF408711D0`, `6B0D40EC4E8E742EEAB3B91180533B4A1A9351316340F76288521292E2293C1E`, `E5C27640D1A43CDBE67567B0CAE2F784902A4B606C12AAE18CAA5E0C6BF6B871`, and `043B1CC3BC4E4BF05C383E8EE84B31D125A9F3EA5944725E7C86EA6153B592D7`.

## Provider source restoration and final hashes

`provider/downloads/v13_firearm_revalidation/download_manifest.json` records the restored accepted generation GLB, remesh GLB, rig FBX, and seven action FBX files. Every action FBX hash matches its pre-existing immutable provenance record; critical matches are laser attack `5CB8EA5140D6F43222527695EB5F1658D5D258641DCD6B2677FC5C0ED4340996` and death `7A4C9264704E2CCF9CFD831AC3798D985C9FB42EAF63A72D0D401EE9397642C5`.

Final runtime candidates remain byte-identical to the accepted manifest: mesh `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342`; idle `D6936AE996DBE998DBEE0633B4DCAC346B6C5D974FC643ACA62AAC73719CB2EF`; move `727BCA51B68EEA445198C1029331FF06F15F69215358ABC9CC29A4064096217F`; laser attack `288209BC4B9CBB3D19A629C2277DF7816CDF33B475EA68BF0D368F7C2E2150F0`; defend `F07A8BC46D68F72DD622014CE31BA9420A3CC1FF419BF3690D44D5F42E9E3A73`; support attack `DADC3823EA4C2FE5F21F10DAE310F52D54E5379A124C01CDEE3AA954F4EE3061`; retreat `DB9E72F782A19C84A7C4C8CF429654D0BAAAC59A7999B381CA9267DD598BD2DC`; death `D8D26A8B7A6F01ADCB64103885171C837DB36CB7BBB6A6A15EB6C2D66F15D7A0`.

## Vanilla precedents and unchanged companion status

- Model/entity: installed `gfx/models/units/western_european_infantry.mesh` and `gfx/entities/units_infantry.asset#infantry_rifle_entity`, with source height 7.3518242835, entity scale 0.8, effective runtime height 5.8814594268, forward -Y, and up +Z.
- Counter: installed `interface/subuniticons.gfx` entries for the two-frame infantry large and on-map counters, installed `unit_infantry_icon.dds` and `onmap_unit_infantry_icon.dds`, and the skill-local land-counter reference families. The bespoke alien counter outputs remain present; no counter was edited in this pass.
- Sound: installed `units_infantry.asset` state-event precedent and tag-wide infantry voice consumers. Existing CC0 laser, movement, idle, and death sources remain unchanged; selection/acknowledgement, impact, and special-action coverage remains blocked exactly as recorded in `runtime/sound_handoff.md`.

## Blockers and parent work

- `blocked`: no supported authored muzzle locator/effect point exists. The adapter schema exposes no locator-create operation, the accepted rig has no muzzle bone, and the cyan cap cannot be treated as an authored node. No origin/hand inference or manual weapon edit was used.
- `blocked`: strict selection/acknowledgement is tag-wide rather than per-subunit, and no accepted sourced impact or special-action audio exists.
- `parent_required`: review the already promoted runtime consumer and state/event timing, resolve a supported effect-point route, keep all runtime paths outside `docs/assets`, and validate live playback in game.
- `not_claimed`: live consumer acceptance and in-game completion.

No required skeletal role is blocked: idle, move, laser attack, defend, support attack, retreat, and death all have distinct genuine Meshy preset sources and final `.anim` bytes. No simplification or fallback was introduced.

## Files changed or added

- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md`.
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/handoff.md`.
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/provider/downloads/v13_firearm_revalidation/` accepted provider artifacts and `download_manifest.json`.
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/validation/reimport_revalidation_2026_08_26_*.json`, fresh proof blends, and generated preview evidence.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_firearm_revalidation_2026-08-26.md`.

Meaningful validation skipped: no live Hearts of Iron IV session was launched, and no in-game playback or positional particle/audio acceptance is claimed. The package remains bounded to provider, Blender, export/reimport, and handoff evidence.
