# Base Zombie Runtime Reference Evidence

This record captures the local references consulted before parent-owned HOI4 entity, animation, particle, and sound wiring for the base zombie.

## Reference route availability

On 2026-09-26, the connected tool catalog was checked for `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`; none of these routes is exposed in this task. The required local files were read directly instead, and the Paradox wiki was not accessed on the web.

## Offline Paradox wiki snapshot

| Source | Lines read | SHA-256 | Use |
|---|---:|---|---|
| `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md` | 25–50, 52–160, 169–183 | `74FF51B8EA0924281EB1C067300B52DC373EA9D112341BBB9C34FCB1A11D2D6A` | PDX mesh registration, animation id mapping, entity states, event timing, particles, sound scopes, and `.anim` registration. |
| `paradox_wiki/Sound modding - Hearts of Iron 4 Wiki.md` | 19–120 | `904C1909FCB8A6AC3D3F6BB5286ECA216BB996513A3BC0788F12F96AB7CC6E4F` | Sound and soundeffect declarations, file paths, 3D playback, looping, falloff, and variation fields. |

## Installed-game documentation

The installed documentation folder contains no Markdown section dedicated to `.asset`/`.gfx` entity definitions, PDX meshes, skeletal animations, or entity-attached sound events. `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` lines 7981–7988 documents the scripted `sound_effect` effect; its SHA-256 is `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`. This scripted effect documentation does not specify entity sound-event syntax, so the local entity wiki section and installed vanilla examples above supply that reference.

## Installed vanilla precedents

| Source | Lines inspected | SHA-256 | Relevant precedent |
|---|---:|---|---|
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset` | 11–52, 139–155, 1944–1946 | `6AB4BE22BC0757C93F8132F7E247910592A5D8595EAF431D33F23DF03F32AA2D` | Infantry combat and training states, entity scale `0.8`, the base infantry entity clone, and the vanilla death-state `blood_particle` event. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/infantry.gfx` | 76–110 | `6439FB7FC1A94E9B2F20368F18BD73526B2ABB9A559B62E58A2C2768396E71D4` | Vanilla infantry mesh path and mapping of runtime animation ids to registered animation asset names. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/soundeffects.asset` | 907–927 | `CB13BE6F368723DD48BE9D9544F7B7B50CFD228B850C88EF55600187BA65B01F` | Vanilla `infantry_move_animation` soundeffect configuration used by the infantry entity move state. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/sound.asset` | 2042–2090 | `263A6DFD6C53C4881E1133C403AF0AE3ED68DF40821B14FF7FD69CD66C48C2D9` | Vanilla infantry-movement sound registrations and their `.wav` file paths. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/particles.gfx` | 5–15 | `AF261D416ACCB89C4FD222B41E2846BEE8DC1D20DEF37B7B232C67DDB8D50D35` | Vanilla `blood_particle` registration referenced by infantry death events. |

## Wiring implications

The parent-owned entity must map every registered mesh animation id to the accepted `.anim` registration and every unit state to a distinct action. State events can bind a source soundeffect and particle to an authored action phase and node. The mesh and entity scale must agree with the measured vanilla infantry crosswalk in the model job; source height is `7.3518242835 m`, entity scale is `0.8`, and effective runtime height is `5.8814594268 m`.

These references establish syntax and precedent only. They do not prove that the current zombie export, `.gfx` registrations, sound paths, particle timing, or live-game consumer are correct; those require the actual final exported assets and parent-owned wiring evidence.
