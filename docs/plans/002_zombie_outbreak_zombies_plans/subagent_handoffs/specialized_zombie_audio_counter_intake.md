# Specialized zombie audio and counter intake

Status: `intake_complete_runtime_work_pending`.

This is a read-only evidence and routing intake for the seven non-armored specialized zombie sub-units: `infected_zombies`, `rabid_zombies`, `parasitic_zombies`, `mutant_zombies`, `undead_zombies`, `necrotic_zombies`, and `demonic_zombies`.

No Meshy, Blender, provider, balance, audio-source download, audio processing, counter generation, placeholder creation, gameplay edit, runtime edit, or static/manual fallback was performed. Estimated and consumed credits for this intake are both `0`.

## Evidence boundary

Everything under “observed” or “current” below is source-file evidence from the installed game or current repository. Everything under “planned”, “proposed”, or “required future” is a handoff target and is not evidence that runtime wiring exists or works.

The current source files prove that all seven specialized sub-units still use `sprite = zombies`, that the shared `zombies_entity` exists, that the shared entity invokes four zombie soundeffects, and that seven pairs of counter sprite registrations and DDS files exist. They do not prove a distinct model, entity, sound identity, sourced-audio package, bespoke counter package, live selection binding, or in-game playback/rendering for any specialized unit.

## Inspected installed precedents

| Surface | Exact installed path | Relevant identifiers or behavior | SHA-256 |
| --- | --- | --- | --- |
| Infantry entity | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset` | `infantry_rifle_entity`; states `attack`, `defend`, `support_attack`, `move`, `retreat`, `death`, `idle`, and `training`; body `move` states invoke `infantry_move_animation`; weapon child entities invoke `infantry_rifle_attack`, `infantry_rifle_cartridge`, and MG equivalents at timed events; entity scale `0.8` | `6AB4BE22BC0757C93F8132F7E247910592A5D8595EAF431D33F23DF03F32AA2D` |
| Counter definitions | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx` | `GFX_unit_infantry_icon_medium` and `GFX_unit_infantry_icon_medium_white`, both `noOfFrames = 2` | `0D7B62CAF328B3C296EC27AB85318F3CC78CC760B02923538BF5240815963335` |
| Soundeffects | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/soundeffects.asset` | `infantry_move_animation`, `infantry_rifle_attack`, `infantry_rifle_cartridge`, `infantry_mg_attack`, and related wrappers | `CB13BE6F368723DD48BE9D9544F7B7B50CFD228B850C88EF55600187BA65B01F` |
| Sound sources | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/sound.asset` | The underlying `animations/infantry_*.wav` registrations consumed by the wrappers | `263A6DFD6C53C4881E1133C403AF0AE3ED68DF40821B14FF7FD69CD66C48C2D9` |
| Infantry voice precedent | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/integrated_dlc/dlc018_together_for_victory/sound/vo.asset` | Country-tag templates `<TAG>_infantry_idle`, `<TAG>_infantry_move_out`, `<TAG>_infantry_neutral_combat`, `<TAG>_infantry_positive_combat`, and `<TAG>_infantry_retreat`; inspected concrete `ENG_*` registrations | `4CBFA03F8CCB3BB99A9F387C966ED3D61B2BD7A006398854B1554604244B6080` |
| Large infantry counter | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds` | `152x42`, two adjacent `76x42` frames, uncompressed 32-bit DDS | `B33A8E3B69CC789EB0E31BA99F4E5BA4E5B0A8B51EC1A7A7F709C3516F720C23` |
| On-map infantry counter | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds` | `60x12`, two adjacent `30x12` frames, uncompressed 32-bit DDS | `58AB78662C2A64A519B8D5D144582E7B2785915BD0A0A822696D87A9DE6F766C` |

The offline graphical-asset reference confirms that `noOfFrames` divides a sprite strip into consumer-addressed frames. The offline entity reference confirms that entity-state `event` blocks can invoke a `soundeffect`, optionally at a specified state time. No installed official documentation file specifically documenting entity audio or counter consumers exists under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`; the installed source files above are therefore the decisive local precedents for these surfaces.

## Current Chaos Redux source evidence

| Source | Observed facts | SHA-256 |
| --- | --- | --- |
| `common/units/zombies.txt` | All seven specialized sub-units currently use `sprite = zombies` and `map_icon_category = infantry` | `37A0A724E7B928FFCF9B58FAFE15BE6265C40845A690E9E5BF6DA80F61CB43A8` |
| `gfx/entities/chaosx_zombies.gfx` | Registers only `chaosx_zombies_mesh` and the shared `idle`, `move`, `attack`, and `death` animation IDs | `750A9D24EB1AC835EABF18FD2D1FF5271E0FEED221958B0A57D96E09D5F3435F` |
| `gfx/entities/chaosx_zombies.asset` | Registers only `zombies_entity`; `attack`, `defend`, and `support_attack` invoke `chaosx_zombie_attack`; `move` and `retreat` invoke `chaosx_zombie_move`; `death` invokes `chaosx_zombie_death`; `idle` invokes `chaosx_zombie_idle`; `training` has no sound | `911A6F63300A345ABF55EC46BAB11C189AF2337FA1956B7CD8764416E1013BD6` |
| `sound/chaosx_zombies_sound.asset` | Defines the shared base zombie sources and wrappers plus the tag-level `ZZZ_infantry_idle` entry in category `Voices` | `64CFBA7D1F2F24CFBC5C99AB02C7AA1C657B429E46B3E53023DFA110C80248B4` |
| `sound/chaosx_sound.asset` | Registers the four shared wrappers in the mod sound category: `chaosx_zombie_attack`, `chaosx_zombie_death`, `chaosx_zombie_idle`, and `chaosx_zombie_move` | `164173DCC06F6427B35349A135BE9DAD28304D42316E668BAA104E9B05220E1C` |
| `interface/chaosx_subuniticons.gfx` | Registers large and `_medium_white` on-map sprites for all seven specialized IDs, each with `noOfFrames = 2` | `020FA077F9D874C2B310E87FED84A1E87AC84E6D0828A6760DCCC21DF4BD605C` |

Because every specialized sub-unit resolves the same `sprite = zombies`, every one currently resolves `zombies_entity` and the same four entity-state soundeffects. The source does not expose a separate specialized entity-state sound consumer until the parent switches each sub-unit to its own sprite stem after all model, animation, audio, counter, and reimport receipts exist.

### Current base-zombie WAV inventory

The following runtime files were inspected for format, duration, and checksum. They are current shared base-zombie assets, not approved specialized-unit sources.

| File | Format | Duration | SHA-256 |
| --- | --- | ---: | --- |
| `sound/002_zombie_outbreak/zombies/zombie_idle_moan_01.wav` | PCM float 32-bit, 44.1 kHz, stereo | 2.116848 s | `63A28AAF9A39A7F12595C47AD83AA75786015E8534B64B2408F13FD4AEF88321` |
| `sound/002_zombie_outbreak/zombies/zombie_idle_moan_02.wav` | PCM float 32-bit, 44.1 kHz, stereo | 1.917982 s | `0104F58C0553ECE097A957366CC892CBB322C0F7E7D0A58E0B0F749DDE1BD9B4` |
| `sound/002_zombie_outbreak/zombies/zombie_idle_moan_03.wav` | PCM float 32-bit, 44.1 kHz, stereo | 0.670794 s | `F7C21F3FA799F02BD60F42267E899FC7613140021E1124A5EF36429DEA3AD953` |
| `sound/002_zombie_outbreak/zombies/zombie_move_step_01.wav` | PCM float 32-bit, 44.1 kHz, mono | 0.153923 s | `435E6ECB3D7F29EC133922DC6449875E4526A8B71BF083CAE05DB2547BD09B59` |
| `sound/002_zombie_outbreak/zombies/zombie_move_step_02.wav` | PCM float 32-bit, 44.1 kHz, mono | 0.168730 s | `B03DD2A67516104B85F4BFC41C7C24CF15C591A758F4C605F34AC0ADD4092718` |
| `sound/002_zombie_outbreak/zombies/zombie_move_step_03.wav` | PCM float 32-bit, 44.1 kHz, mono | 0.316712 s | `0AF59E237CADC330442BF83716B99D3010EBDD4B008C6FBD23CA0CD690F4DB2F` |
| `sound/002_zombie_outbreak/zombies/zombie_move_step_04.wav` | PCM float 32-bit, 44.1 kHz, mono | 0.333016 s | `AA5AAD67C60D04C53485D43532D39309CB743AB07764DC0944CAA0D017625673` |
| `sound/002_zombie_outbreak/zombies/zombie_move_step_05.wav` | PCM float 32-bit, 44.1 kHz, mono | 0.313764 s | `B336F07522207B56EB85665E595C1956E115CC1A136AFFA360176DC0DC75CC16` |
| `sound/002_zombie_outbreak/zombies/zombie_move_step_06.wav` | PCM float 32-bit, 44.1 kHz, mono | 0.245669 s | `2634498FBCFB4838D8F204853000143FE2C3038313050F21314F57D9471053BF` |
| `sound/002_zombie_outbreak/zombies/zombie_attack_01.wav` | PCM float 32-bit, 44.1 kHz, stereo | 0.336689 s | `34CEA5744A2BC2D23B2189318530D765944ADB57488E9E84F5F2D2582E5DB40D` |
| `sound/002_zombie_outbreak/zombies/zombie_attack_02.wav` | PCM float 32-bit, 44.1 kHz, stereo | 0.750000 s | `4591611620F3130AB83D198DE68B23C71AA8BDB02412407BF6BBAB12CFAB01B6` |
| `sound/002_zombie_outbreak/zombies/zombie_attack_03.wav` | PCM float 32-bit, 44.1 kHz, stereo | 0.874989 s | `CC015ED64A4248277533B26DE2C4534B91ECCAA22E59913439D630CEC7B12C93` |
| `sound/002_zombie_outbreak/zombies/zombie_death_01.wav` | PCM float 32-bit, 44.1 kHz, stereo | 0.312494 s | `3628684303DB5AB62EC0EDD3115A6BF835A5073AD466985C927DBC74E91DFEAE` |
| `sound/002_zombie_outbreak/zombies/zombie_death_02.wav` | PCM float 32-bit, 44.1 kHz, stereo | 0.562494 s | `3C80BCD1419CDCA8D99AF277EE40CA376A8283141FC947D6DFFECF7FD12A9F89` |
| `sound/002_zombie_outbreak/zombies/zombie_death_03.wav` | PCM float 32-bit, 44.1 kHz, stereo | 0.500000 s | `FA405B4808EAD0874829E93E0C3E893D3CD2470538D0026112089F9BE2F1187F` |

The comment in `sound/chaosx_zombies_sound.asset` says these WAVs derive from CC0 candidates documented in a zombie model audio handoff, but no durable source URLs, attribution records, original-download paths, or license receipts were found in the scoped current handoffs. That comment is not enough to establish reusable source provenance for the seven specialized packages. Future specialized audio must therefore obtain and preserve its own defensible Internet-source and license evidence; these current WAVs must not be copied as a fallback.

## Selection and order-consumer limitation

The installed voice precedent resolves infantry voice names by country or original tag, not by sub-unit ID or `sprite` token. For the zombie country, the engine-consumed selection identifier is `ZZZ_infantry_idle`. The related order/combat templates are `ZZZ_infantry_move_out`, `ZZZ_infantry_neutral_combat`, `ZZZ_infantry_positive_combat`, and `ZZZ_infantry_retreat`.

`sound/chaosx_zombies_sound.asset` currently defines only `ZZZ_infantry_idle`. That definition reaches the infantry selection consumer for the `ZZZ` identity; it cannot distinguish infected, rabid, parasitic, mutant, undead, necrotic, demonic, base, Wendigo, armored, or any other infantry sub-unit under the same country/original tag. Merely defining `chaosx_infected_zombies_select` or another unit-specific selection soundeffect would not create a consumer.

Parent-owned choice: either deliberately accept one shared `ZZZ_infantry_idle` selection identity for all ZZZ infantry and document that limitation, or provide and validate a separate actual per-subunit selection consumer before claiming specialized selection coverage. No static/manual substitute is authorized. The same limitation applies to the four tag-level order/combat/retreat templates.

## Entity-state sound role contract

The future specialized entities can distinguish unit sound identities because entity states resolve through the unit-specific `sprite` stem. Use these stable wrapper patterns in the future sound-definition file: `chaosx_<unit>_idle`, `chaosx_<unit>_move`, `chaosx_<unit>_attack`, and `chaosx_<unit>_death`; underlying sourced variations should use `chaosx_<unit>_<role>_<nn>`.

| Entity state | Required wrapper | Action synchronization rule | Consumer limitation |
| --- | --- | --- | --- |
| `idle` | `chaosx_<unit>_idle` | One-shot vocal/ambient event at an authored nonrepeating phase or state entry; do not assume a loop merely because the animation loops | Repeating behavior depends on the final entity event timing and trigger policy |
| `move` | `chaosx_<unit>_move` | Foot, drag, wing, or body contact at exact contact frames in `chaosx_<unit>_move` | Exact frames are blocked until the final action exists |
| `retreat` | `chaosx_<unit>_move` unless a sourced retreat role is explicitly approved | Match retreat locomotion contacts | Reuse is a proposed role mapping, not a licensed-audio substitute |
| `attack` | `chaosx_<unit>_attack` | Strike, bite, claw, spore release, or impact onset at the exact authored contact phase | Exact phase is unit-specific and blocked until the final action exists |
| `defend` | `chaosx_<unit>_attack` unless a separate sourced role is approved | Match the defend action's attack/contact event | Parent must confirm the final defend animation mapping |
| `support_attack` | `chaosx_<unit>_attack` unless a separate sourced role is approved | Match the support-attack contact event | Parent must confirm the final support-attack animation mapping |
| `death` | `chaosx_<unit>_death` | Vocal termination and/or body impact at the exact terminal collapse phase | Exact phase is blocked until the final death action exists |
| `training` | none by default | No sound unless a sourced and deliberately consumed training role is added | Current base entity is silent in this state |

Per-unit source-search direction, not authored audio: infected should emphasize wet breath, dragging contacts, a desperate lunge, and collapse; rabid should emphasize snarling pant, fast hunting contacts, bite/lunge, and abrupt death; parasitic should emphasize fungal rasp/click, growth creak, spore/strike release, and infested collapse; mutant should emphasize heavy respiration, massed footfalls, a powerful slam/roar, and body impact; undead should emphasize dry rattle/whisper, restrained bone or clothing contacts, jaw/hand strike, and brittle collapse; necrotic should emphasize desiccated rasp, dragging scrape, elongated swipe, and dry crumble; demonic should emphasize inhuman breath, digitigrade contact and wing membrane movement, screech/claw impact, and a wing/body crash.

Every future file must be an immutable clearly licensed Internet source or a documented mechanical derivative permitted by that license. Generated, synthesized, recorded, manually authored, placeholder, unlicensed, or provenance-unclear audio remains forbidden.

## Counter sprite contract and current limitation

The installed definition and skill-local families establish the exact land-counter contract:

- Large sprite: `GFX_unit_<subunit_id>_icon_medium` -> `gfx/interface/counters/divisions_large/unit_<subunit_id>_icon.dds`, `152x42`, `noOfFrames = 2`, frames `76x42`.
- On-map sprite: `GFX_unit_<subunit_id>_icon_medium_white` -> `gfx/interface/counters/divisions_small/onmap_unit_<subunit_id>_icon.dds`, `60x12`, `noOfFrames = 2`, frames `30x12`.
- Frame 0 is the normal unit-specific silhouette. In the large vanilla family it is compact muted green with a dark outline and soft modeled shading.
- Frame 1 is the alternate/template schematic state: a separate sparse pale/white glyph inside a dark outlined panel, not a white repaint of frame 0.
- Transparent unused canvas, centered compact bounds, restrained shading, readable native-size contrast, and exact no-gap frame boundaries are required.

The canonical reference families are `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/`. Their contact sheets have SHA-256 `CD7ABDF70B38498D03744990BA91BFFF808686B1E8891049B8A78AD58E9B4243` and `23374FC38F26FC382DF60800C1086E074AC6BE46CDCD86B3EADDE686A99C8C26` respectively.

Sampled dominant opaque green values from installed vanilla large infantry frame 0 include RGB `73,106,73` (`#496A49`), `74,107,74` (`#4A6B4A`), `83,114,83` (`#537253`), and `100,128,100` (`#648064`). These are palette anchors with antialiasing, shadow, and highlight variation; arbitrary green is forbidden.

All seven current large DDS files are byte-identical DXT1 `152x42` files with SHA-256 `6409846E58734FA198FF1D1D6B37863C65FB058FAFE16E6F47E66CD0FD1AC291`. All seven current on-map DDS files are byte-identical DXT1 `60x12` files with SHA-256 `8EAFD2BF7B2FB65EA48E0BE01E5D5741B4F5DB2BCAD0302C409DA7130E5D3623`. Visual inspection shows the same green skull plus the same schematic “Z” strip repeated for every unit. These files satisfy path and frame-count evidence only; they do not satisfy the required bespoke seven-unit counter package and must not be promoted as final specialized art.

A bounded counter-art worker has since staged fourteen distinct source PNGs under `docs/assets/002_zombie_outbreak/models_3d/<unit>/counters/source/{large,small}/` for the seven active units. These are source candidates only: the required processed alpha PNGs, final native-size DDS strips, decoded round trips, contact sheet, and parent handoff are not present yet, so no runtime counter has been replaced.

Required future counter-artist handoff path: `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/specialized_zombie_counter_art_handoff.md`. The future `chaosx_icon_artist` prompt must use `fork_context=false`, name all fourteen exact DDS destinations, require seven distinct role-readable silhouettes, preserve the two-frame semantics above, and return ImageGen source PNGs, saved prompts, processed alpha PNGs, decoded DDS round trips, native-size comparison/contact-sheet evidence, manifest entries, and parent review status.

## Seven-unit runtime destination crosswalk

The paths and identifiers in this table are the accepted planned destinations derived from the seven job files and `specialized_zombie_3d_models_plan.md`. They are not current runtime registrations.

| Sub-unit | Planned sprite/entity/model destination | Planned entity sound wrappers and WAV folder | Existing counter destinations requiring bespoke replacement |
| --- | --- | --- | --- |
| `infected_zombies` | `sprite = infected_zombies`; `chaosx_infected_zombies_entity`; `gfx/models/units/chaosx_infected_zombies/`; shared registrations in `gfx/entities/chaosx_specialized_zombies.gfx` and `.asset` | `chaosx_infected_zombies_{idle,move,attack,death}`; `sound/002_zombie_outbreak/zombies/infected_zombies/` | `gfx/interface/counters/divisions_large/unit_infected_zombies_icon.dds`; `gfx/interface/counters/divisions_small/onmap_unit_infected_zombies_icon.dds` |
| `rabid_zombies` | `sprite = rabid_zombies`; `chaosx_rabid_zombies_entity`; `gfx/models/units/chaosx_rabid_zombies/`; shared specialized `.gfx` and `.asset` | `chaosx_rabid_zombies_{idle,move,attack,death}`; `sound/002_zombie_outbreak/zombies/rabid_zombies/` | `gfx/interface/counters/divisions_large/unit_rabid_zombies_icon.dds`; `gfx/interface/counters/divisions_small/onmap_unit_rabid_zombies_icon.dds` |
| `parasitic_zombies` | `sprite = parasitic_zombies`; `chaosx_parasitic_zombies_entity`; `gfx/models/units/chaosx_parasitic_zombies/`; shared specialized `.gfx` and `.asset` | `chaosx_parasitic_zombies_{idle,move,attack,death}`; `sound/002_zombie_outbreak/zombies/parasitic_zombies/` | `gfx/interface/counters/divisions_large/unit_parasitic_zombies_icon.dds`; `gfx/interface/counters/divisions_small/onmap_unit_parasitic_zombies_icon.dds` |
| `mutant_zombies` | `sprite = mutant_zombies`; `chaosx_mutant_zombies_entity`; `gfx/models/units/chaosx_mutant_zombies/`; shared specialized `.gfx` and `.asset` | `chaosx_mutant_zombies_{idle,move,attack,death}`; `sound/002_zombie_outbreak/zombies/mutant_zombies/` | `gfx/interface/counters/divisions_large/unit_mutant_zombies_icon.dds`; `gfx/interface/counters/divisions_small/onmap_unit_mutant_zombies_icon.dds` |
| `undead_zombies` | `sprite = undead_zombies`; `chaosx_undead_zombies_entity`; `gfx/models/units/chaosx_undead_zombies/`; shared specialized `.gfx` and `.asset` | `chaosx_undead_zombies_{idle,move,attack,death}`; `sound/002_zombie_outbreak/zombies/undead_zombies/` | `gfx/interface/counters/divisions_large/unit_undead_zombies_icon.dds`; `gfx/interface/counters/divisions_small/onmap_unit_undead_zombies_icon.dds` |
| `necrotic_zombies` | `sprite = necrotic_zombies`; `chaosx_necrotic_zombies_entity`; `gfx/models/units/chaosx_necrotic_zombies/`; shared specialized `.gfx` and `.asset` | `chaosx_necrotic_zombies_{idle,move,attack,death}`; `sound/002_zombie_outbreak/zombies/necrotic_zombies/` | `gfx/interface/counters/divisions_large/unit_necrotic_zombies_icon.dds`; `gfx/interface/counters/divisions_small/onmap_unit_necrotic_zombies_icon.dds` |
| `demonic_zombies` | `sprite = demonic_zombies`; `chaosx_demonic_zombies_entity`; `gfx/models/units/chaosx_demonic_zombies/`; shared specialized `.gfx` and `.asset` | `chaosx_demonic_zombies_{idle,move,attack,death}`; `sound/002_zombie_outbreak/zombies/demonic_zombies/` | `gfx/interface/counters/divisions_large/unit_demonic_zombies_icon.dds`; `gfx/interface/counters/divisions_small/onmap_unit_demonic_zombies_icon.dds` |

Each model folder is planned to contain `chaosx_<unit>.mesh`, `chaosx_<unit>_{idle,move,attack,death}.anim`, `animation_chaosx_<unit>.asset`, and the verified PDX material DDS maps. Future specialized sound definitions should live in a parent-selected runtime `.asset`, with `sound/chaosx_specialized_zombies_sound.asset` proposed as the stable shared definition file; the parent must also register the final wrappers in the appropriate sound category consumer. Neither file exists as specialized runtime wiring at this intake state.

## Remaining parent-owned choices and blockers

1. Decide whether all ZZZ infantry deliberately share `ZZZ_infantry_idle` and any future `ZZZ_infantry_*` order voices, or provide an actual validated per-subunit selection consumer. Unit-specific soundeffect names without a consumer are not coverage.
2. Approve `sound/chaosx_specialized_zombies_sound.asset` and the seven event-scoped WAV folders as the stable runtime naming layout, or record a different layout before Internet sourcing begins.
3. For every unit and role, choose clearly licensed source candidates, preserve the original download and source page/direct-download URLs, attribution, usage terms, transformation permission, download date, duration, and SHA-256, then record every mechanical derivative and checksum. No such specialized sources exist yet.
4. After each final action exists, set exact state-event times or frame/phase mappings for idle, movement contacts, attack contact, and death impact. The current intake cannot truthfully provide frame numbers because the specialized actions do not exist.
5. Complete the already-started bounded counter-art worker with `fork_context=false` and the exact handoff path above. Require seven distinct large strips and seven distinct on-map strips; the current byte-identical skull/Z files are not acceptable finals.
6. Review native-size counter contact sheets and decoded DDS round trips before runtime promotion. The parent owns `interface/chaosx_subuniticons.gfx`, `common/units/zombies.txt`, final `.gfx`/`.asset` model registration, sound registration, source-to-runtime synchronization, and live in-game validation.
7. Keep every specialized `sprite` switch blocked until its mesh, four animations, PDX textures, reimport evidence, sourced-audio receipt, bespoke counter receipt, and hash synchronization are all present. No current source evidence satisfies that promotion gate.
8. The pre-existing model-production handoff still records pending visual approvals for six of the seven references, the seven-package provider-credit shortfall, and missing extra-recovery limits. This intake resolves the previously missing installed sound/counter precedent and destination mapping only; it does not clear those separate blockers.

## Validation performed

Meaningful validation included exact source inspection of the installed infantry entity, counter definitions and DDS files, sound and voice definitions; inspection of the current zombie unit, entity, sound, category, and counter definitions; SHA-256 comparison of all fourteen specialized counter DDS files; decoded DDS dimensions, frame boundaries, alpha bounds, dominant palette sampling, and visual comparison against the two skill-local land-counter contact sheets; and codec, sample rate, channel count, duration, byte size, and SHA-256 inspection of all fifteen current base-zombie WAV files.

Validation intentionally skipped: Internet sound sourcing and license verification, audio transformation/listening acceptance, animation-frame synchronization, final counter processing/contact-sheet approval/DDS round trips, specialized model/entity creation, runtime edits, source-to-runtime synchronization, provider work, Blender work, and in-game validation. Source-counter candidate presence and distinct file hashes were observed, but they are not final counter evidence. Those activities require artifacts that do not yet exist.

## Files changed

- `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/specialized_zombie_audio_counter_intake.md`

No simplification or fallback was used. The current shared selection limitation and repeated counter assets are recorded as unresolved evidence, not presented as completed specialized runtime behavior.
