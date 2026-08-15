# Specialized zombie audio-source handoff

Status: **research/evidence complete; runtime integration incomplete and parent-owned**.

Scope was limited to Internet audio-source research for `infected_zombies`, `rabid_zombies`, `parasitic_zombies`, `mutant_zombies`, `undead_zombies`, `necrotic_zombies`, and `demonic_zombies`. The base zombies package and all armored variants were not changed. No current shared base-zombie WAV was used as a source or fallback.

## Work and cost boundaries

- Meshy/provider calls: none.
- Paid credits estimated/consumed: 0 / 0.
- Blender calls: none.
- Runtime, gameplay, GFX/interface, localisation, unit, entity, sound-definition, and model files changed: none.
- Audio creation, synthesis, recording, generation, and manual authorship: none.
- Mechanical audio transformations: none. ZIP extraction only reproduced archive members for inspection; no trim, fade, normalization, channel conversion, resampling, codec conversion, or pitch processing was performed.
- Commit: none, as required.
- Dependency-lock/route-schema/Blender/io_pdx_mesh/provider-task evidence: not applicable to this bounded no-provider/no-Blender research tranche. No dependency route was invoked or claimed.

## Observed engine consumers

The installed vanilla `gfx/entities/units_infantry.asset` binds movement audio through an entity state event (`event = { sound = { soundeffect = "infantry_move_animation" } }`) on `move`/`march_move`. It exposes attack, support-attack, move, retreat, death, and idle states that can host parent-authored sound events.

The installed vanilla `integrated_dlc/dlc018_together_for_victory/sound/vo.asset` defines the `Voices` category and hardcoded country/original-tag infantry templates such as `GER_infantry_idle`, `GER_infantry_neutral_combat`, `GER_infantry_positive_combat`, `GER_infantry_retreat`, and `GER_infantry_move_out`. This is a tag-wide infantry route, not a sub-unit or sprite route. `sound/soundeffects.asset` separately defines global `select_army` and army movement/order UI effects.

The parent brief does not name the owning country/original tags or enumerate ordinary infantry consumers under those identities. Therefore exact selection/acknowledgement binding is **blocked for all seven units**. If specialized and ordinary infantry coexist under the same tag, a zombie voice assigned to `<TAG>_infantry_idle` would affect all infantry and cannot provide per-subunit distinction. The preserved voice candidates may be used only after the parent resolves the tag-wide consumer impact or proves a separate bounded consumer; they may not replace global `select_army`.

Read-only local inspection found the existing shared base-zombie sound package in `sound/chaosx_zombies_sound.asset` and its entity events in `gfx/entities/chaosx_zombies.asset`. Those current shared WAVs and wrappers were deliberately not reused, edited, copied, or treated as fallback candidates.

## Observed source and licence evidence

All accepted source pages state CC0 1.0/public-domain dedication and permit modification and commercial reuse. Source-page HTML snapshots, CC0 legal-code snapshots, immutable downloads, extracted archive members, complete hashes, and technical metadata are package-local. Creator, title, source URL, direct-download URL, terms, download date, archive lineage, candidate paths, durations, hashes, and proposed synchronization points are recorded in each `source_provenance.md`.

| Unit | Accepted source families | Package evidence |
|---|---|---|
| `infected_zombies` | artisticdude, **Zombies Sound Pack**; GboxMikeFozzy, **Footsteps** | `docs/assets/002_zombie_outbreak/models_3d/infected_zombies/sound/` |
| `rabid_zombies` | Darsycho, **Monster snarls**; GboxMikeFozzy, **Footsteps**; Zane Little Music, **Fleshy Bone Break/Snap SFX**; Exewin, **Death sounds** | `docs/assets/002_zombie_outbreak/models_3d/rabid_zombies/sound/` |
| `parasitic_zombies` | qubodup, **Insect or alien scream**; rubberduck, **40 CC0 water/splash/slime SFX**; GboxMikeFozzy, **Footsteps**; Exewin, **Death sounds** | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/sound/` |
| `mutant_zombies` | ianzazz, **Zombie noises and moans**; trazzz123, **CC0 Deep Monster Roar**; Zane Little Music, **Fleshy Bone Break/Snap SFX**; GboxMikeFozzy, **Footsteps**; Exewin, **Death sounds** | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/sound/` |
| `undead_zombies` | congusbongus, **Bones rattle**, adapted from blukotek/Piotr Zaczek’s CC0 **bone shell** recording; saturn91, **Zomby sfx pack**; Exewin, **Death sounds**; GboxMikeFozzy, **Footsteps** | `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/sound/` |
| `necrotic_zombies` | rubberduck, **25 CC0 mud SFX**; pauliuw, **Slimy monster or murder sounds (9)**; saturn91, **Zomby sfx pack**; GboxMikeFozzy, **Footsteps** | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/sound/` |
| `demonic_zombies` | Tim Rockk, **demon voice**; Vinrax, **Horror scream1**; trazzz123, **CC0 Deep Monster Roar**; Zane Little Music, **Fleshy Bone Break/Snap SFX**; GboxMikeFozzy, **Footsteps** | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/sound/` |

OpenGameArt source URLs and every direct-download URL are written in the package provenance files. The upstream undead bone-rattle recording was separately verified on Freesound as **bone shell** by blukotek/Piotr Zaczek, recorded from mixed shells and released under CC0; its source-page snapshot is preserved with the derivative pack evidence.

## Proposed role coverage and synchronization

These are proposals, not runtime facts. Exact frame numbers cannot be assigned until the parent accepts each model action and its FPS/frame range. Package provenance uses normalized phases so the parent can bind exact frames after action audit.

| Unit | Idle | Move/contact | Attack/impact | Special | Death | Selection/order |
|---|---|---|---|---|---|---|
| infected | Zombie-pack vocal at idle phase 0.20–0.35; clip audition required | Foot plants | Wind-up vocal at 0.00–0.15; candidate hit at 0.55–0.70, both audition-gated | No semantic action supplied; pending parent definition | Collapse-start vocal; audition required | **Blocked: owning tag/original tag not supplied; route is tag-wide** |
| rabid | Trimmed snarl in long idle | Fast foot plants | Snarl at lunge start; fleshy contact at 0.55–0.70 | Frenzy/lunge start | Death voice at loss of balance; optional contact accent | **Blocked: owning tag/original tag not supplied; route is tag-wide** |
| parasitic | Bounded bubble/slime ambience | Foot plant, selective slime contact | Insect shriek at wind-up; slime impact at 0.55–0.70 | Parasite rupture/expulsion contact | Death voice at collapse; optional slime body contact | **Blocked: owning tag/original tag not supplied; route is tag-wide** |
| mutant | Mutated moan in long idle | Heavy foot plants | Fast vocal at wind-up; wet break at 0.55–0.70 | Rare mutation roar at special-action start | Death voice at collapse; optional wet body contact | **Blocked: owning tag/original tag not supplied; route is tag-wide** |
| undead | Zombie call in long idle | Foot plant plus sparse bone rattle | Vocal at wind-up; bone contact only for visible bony strike | Reanimation rise or pronounced joint snap | Death voice at collapse; bone rattle at body contact | **Blocked: owning tag/original tag not supplied; route is tag-wide** |
| necrotic | Zombie call in long idle | Foot plant plus occasional mud drag | Vocal at wind-up; slimy contact at 0.55–0.70 | Visible necrotic discharge/rupture | Wet body-contact cue at 0.75–0.90; vocal pairing requires audition | **Blocked: owning tag/original tag not supplied; route is tag-wide** |
| demonic | Demon growl in long idle | Foot plants | Fight grunt at wind-up; fleshy contact at 0.55–0.70 | Rare demonic laugh/roar at special-action or long-idle start | Explicit demon-death voice at collapse; body contact at 0.75–0.90 | **Blocked: owning tag/original tag not supplied; route is tag-wide** |

## Proposed runtime identifier families

The parent may revise these before creating sound definitions. They are proposals only:

- `chaosx_infected_zombies_<role>_sound_<nn>` and `chaosx_infected_zombies_<role>_sfx`
- `chaosx_rabid_zombies_<role>_sound_<nn>` and `chaosx_rabid_zombies_<role>_sfx`
- `chaosx_parasitic_zombies_<role>_sound_<nn>` and `chaosx_parasitic_zombies_<role>_sfx`
- `chaosx_mutant_zombies_<role>_sound_<nn>` and `chaosx_mutant_zombies_<role>_sfx`
- `chaosx_undead_zombies_<role>_sound_<nn>` and `chaosx_undead_zombies_<role>_sfx`
- `chaosx_necrotic_zombies_<role>_sound_<nn>` and `chaosx_necrotic_zombies_<role>_sfx`
- `chaosx_demonic_zombies_<role>_sound_<nn>` and `chaosx_demonic_zombies_<role>_sfx`

Suggested entity-event role tokens are `idle`, `move`, `attack_vocal`, `attack_impact`, unit-specific `special`, and `death`. Selection/acknowledgement must instead use the exact resolved `<TAG>_infantry_idle`, `<TAG>_infantry_move_out`, `<TAG>_infantry_neutral_combat`, `<TAG>_infantry_positive_combat`, and `<TAG>_infantry_retreat` templates only after the parent audits every infantry consumer under that country/original tag. Do not invent unit-specific `select`/`order` wrappers without a proven consumer.

## Complete file/checksum evidence

Each `evidence_checksums.csv` exhaustively lists every package-local file except itself, including immutable downloads, extracted members, HTML licence/source snapshots, `source_checksums.csv`, `audio_inventory.csv`, and `source_provenance.md`. The checksum of each exhaustive ledger is listed here, completing the checksum chain for every package-local file:

Repository note: `docs/assets/` is ignored by `.gitignore`, so these evidence files exist on disk but do not appear in ordinary `git status`. The parent must review and intentionally preserve or force-add them according to the event workspace policy; this worker did not alter `.gitignore`.

| Unit | Files listed | `evidence_checksums.csv` SHA-256 |
|---|---:|---|
| infected | 58 | `ea24973133780f89cce343dbffaef788770b151aacd29c9816882beced218a7c` |
| rabid | 37 | `8339ec44f4847839d246af6ca260364d85703dd905af4b3dda7ac229794e133c` |
| parasitic | 63 | `4089ca70088f105e9fe356a10d1961bc522080206988922d502005ac94279c05` |
| mutant | 39 | `9069573620ebf9eb1a5a916785a5afbd451a76ce4e6e7f2da5019a3a2c703a7d` |
| undead | 39 | `322c1a24a5948b0f2480f2025f6cdca5dea9b60aba7e7637341bb6a0682a4549` |
| necrotic | 46 | `dc31a51aa7fc9499af6e19b57ab09a5727089931c83eb9a54ff6801ebabee7d5` |
| demonic | 89 | `dd36429b6ef21a09b8a5b1d11c32f4b27e299a38b2df0d13b2700e3253776183` |

`source_checksums.csv` in each package provides a source-only view. `audio_inventory.csv` lists every valid audio member with duration, codec, sample rate, channels, available bit-depth metadata, and SHA-256. Archive resource-fork entries beginning `._` in the infected pack were preserved as immutable archive evidence but rejected from audio inventory because they are not valid audio streams.

## Validation performed

- Confirmed every direct download completed with non-zero content and every selected ZIP opened through standard archive extraction.
- Probed every non-resource-fork WAV/OGG/MP3/FLAC with `ffprobe`; valid-audio counts are infected 25, rabid 27, parasitic 53, mutant 27, undead 28, necrotic 37, and demonic 77.
- Recorded source audio formats and identified that many originals are not already in the locally documented HOI4 delivery format. Parent conversion is required after clip acceptance; no source was silently treated as runtime-ready.
- Verified source-page snapshots contain the accepted title/creator/licence evidence and preserved CC0 1.0 legal-code snapshots.
- Verified the seven package roots and this handoff are the only intended write surfaces for this task.

## Blockers, review gates, and remaining parent work

- **Blocked:** selection/order voice binding for all seven units. Vanilla exposes country/original-tag-wide infantry voice templates, while the parent brief supplies no owning tags or consumer enumeration; per-subunit distinction is unavailable when ordinary and zombie infantry share the tag.
- **Needs parent audition:** all long files that require extracting a short cue; all numeric infected zombie-pack clips because the publisher supplies pack-level role tags but not per-clip semantics; optional vocal pairing for necrotic death.
- **Needs action/frame audit:** exact frame numbers, loop policy, and root/contact synchronization cannot be finalized until accepted idle/move/attack/special/death actions exist.
- **Parent-owned:** final candidate acceptance, any licence-permitted mechanical trim/fade/silence removal/normalization/channel conversion/resampling/codec conversion, HOI4 sound and soundeffect definitions, category registration, entity animation events, runtime file placement, exact frame binding, and in-game validation.
- **Not claimed:** runtime wiring, in-game completion, model completion, counter completion, or overall seven-unit completion.

No unlicensed, vague-royalty-free, generated, synthesized, manually authored, placeholder, or current shared base-zombie audio was accepted.
