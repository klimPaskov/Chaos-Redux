# Humanoid zombie unit-audio companion handoff

Status: `candidate audio packages delivered; parent acceptance and runtime wiring pending`.

This bounded handoff covers exactly `zombies`, `infected_zombies`, `rabid_zombies`, and `undead_zombies`. The base package is a separate source-backed candidate set; existing shared runtime WAVs were left untouched and were not copied or reused. This handoff does not edit sound definitions, entity files, unit files, GFX, localisation, event files, or gameplay files.

## Delivered package roots

| Unit | Package note | Final candidates | Source and format receipts |
| --- | --- | ---: | --- |
| `zombies` | `docs/assets/002_zombie_outbreak/models_3d/zombies/sound/source_provenance.md` | `derived/` contains nine WAVs, including named physical-contact `_02` candidates | `evidence/source_ffprobe.csv`, `evidence/derived_ffprobe.csv`, `evidence/source_checksums.csv`, `evidence/derived_checksums.csv`, `evidence/audition/ffplay_receipts.csv` |
| `infected_zombies` | `docs/assets/002_zombie_outbreak/models_3d/infected_zombies/sound/source_provenance.md` | `derived/` contains nine WAVs, including named physical-contact `_02` candidates | `evidence/source_ffprobe.csv`, `evidence/derived_ffprobe.csv`, `evidence/source_checksums.csv`, `evidence/derived_checksums.csv`, `evidence/audition/ffplay_receipts.csv` |
| `rabid_zombies` | `docs/assets/002_zombie_outbreak/models_3d/rabid_zombies/sound/source_provenance.md` | `derived/` contains seven WAVs | `evidence/source_ffprobe.csv`, `evidence/derived_ffprobe.csv`, `evidence/source_checksums.csv`, `evidence/derived_checksums.csv`, `evidence/audition/ffplay_receipts.csv` |
| `undead_zombies` | `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/sound/source_provenance.md` | `derived/` contains seven WAVs | `evidence/source_ffprobe.csv`, `evidence/derived_ffprobe.csv`, `evidence/source_checksums.csv`, `evidence/derived_checksums.csv`, `evidence/audition/ffplay_receipts.csv` |

Every final candidate is `pcm_s16le`, 44,100 Hz, mono, 16-bit, and each file decoded through `ffprobe` and returned exit code 0 from a bounded `ffplay` playback audition. Source originals, page snapshots, CC0 and CC-BY-SA legal snapshots, extraction lineage, source hashes, and final hashes remain package-local. The four packages contain 32 final candidate WAVs in total.

## Shipping license companions

When the parent wires either named physical `_02` candidate for base or infected zombies, copy that package's exact `runtime_attribution.txt` beside the accepted runtime WAVs. `zombies/sound/runtime_attribution.txt` is 4,476 bytes with SHA-256 `cee2967a90244d78d5fe1631ac3a64e339f92131b7e5c8ccb7e487f1998f8daf`; `infected_zombies/sound/runtime_attribution.txt` is 4,539 bytes with SHA-256 `b36aa44027456d017fa15109c7e0bdf0f445d3fc1f42667867f0366f18aefe81`. Each file names the exact source pages/downloads, the CC0 punch and CC-BY-SA 3.0 body-fall terms, required attribution, linked qubodup recording credit, license snapshot paths, mechanical modifications, and the `_01` `rejected_for_physical_semantics` status. If bundled license texts are required, copy the exact package-local `source/licenses/cc0-1.0.html`, `source/licenses/cc0-1.0-legalcode.en.html`, `source/licenses/cc-by-sa-3.0.html`, and `source/licenses/cc-by-sa-3.0-legalcode.en.html` files referenced by those companions.

## Required role coverage

Each delivered package contains `selection_01`, `idle_01`, `move_01`, `attack_windup_01`, `attack_impact_01`, `death_vocal_01`, and `death_body_01`. The proposed runtime wrappers are `chaosx_<slug>_idle`, `chaosx_<slug>_move`, `chaosx_<slug>_attack`, and `chaosx_<slug>_death`; parent wiring should copy the derived files into `sound/002_zombie_outbreak/zombies/<slug>/` and keep windup/impact and vocal/body contact as separate entity events.

For `zombies` and `infected_zombies`, the preserved `_01` attack-impact and death-body files came from unlabeled artisticdude pack members. The new `_02` candidates use the explicitly named Delta12 Studio `punch_1.ogg` and remaxim `fall.wav` sources; prefer these when a named unarmed impact or body-fall/thud is required. Their CC0 and CC-BY-SA provenance, exact attribution, source hashes, and derived hashes are recorded in the package notes. Rabid and undead physical-contact candidates remain tied to explicitly titled Fleshy Bone Break/Snap and Bones rattle source families, respectively.

Role identity follows the parent brief: base uses the artisticdude zombie pack plus Gbox footsteps for a decayed shambler, with the named `fall.wav` body-fall and `punch_1.ogg` unarmed-impact reserves; infected uses the artisticdude zombie pack plus Gbox footsteps for wet breath and desperate human contact, with the same named physical-contact reserves; rabid uses Darsycho snarls, Zane Little Music wet breaks, Exewin death voice, and Gbox footsteps for fast feral lunge and wet impact; undead uses saturn91 zombie calls, congusbongus bone-rattle adaptation with the linked CC0 blukotek/Piotr Zaczek recording, Exewin death voice, and Gbox footsteps for dry rattle and tattered humanoid contact.

No audio was generated, synthesized, recorded, manually authored, layered into a new cue, or replaced with an unlicensed/default/test sound. Mechanical processing was limited to the source-permitted trim/fade/normalization/channel/resample/PCM conversion recorded in each package note.

## Animation synchronization proposal

The handoff intentionally supplies semantic normalized phases rather than frame numbers. Use idle vocal at 0.20–0.35 of the accepted idle action, movement at foot-plant/contact, attack windup at 0.00–0.15, attack impact at 0.55–0.70, death vocal at 0.00–0.25, and death body contact at 0.75–0.90. The parent must substitute each accepted action's actual FPS and frame range; the current parent report places base non-death candidates at 24 FPS and the death candidate at 30 FPS, with exact mappings and pending flags preserved in the action receipts. No blanket FPS assumption is encoded. For base and infected, the `_02` physical files follow the same normalized phases as their `_01` role counterparts.

Defend and support_attack may reuse the attack wrapper only where an accepted action has a corresponding contact. Retreat may reuse the move wrapper at retreat foot contacts. Training is silent by default. Exact frame acceptance remains blocked until the parent completes action acceptance and provides the final action receipts.

## Selection, acknowledgement, and retreat limitation

Selection candidates are present for all four units, but the exact selection consumer is unresolved. The known infantry voice route is country/original-tag wide through `<TAG>_infantry_idle`, with related tag-wide order templates `<TAG>_infantry_move_out`, `<TAG>_infantry_neutral_combat`, `<TAG>_infantry_positive_combat`, and `<TAG>_infantry_retreat`. A unit-specific soundeffect name cannot create a subunit consumer and must not replace another infantry voice or global `select_army`.

Parent decision: either deliberately accept one shared `ZZZ_infantry_idle`/order identity for all ZZZ infantry, or prove a separate per-subunit selection consumer before binding. Until then, selection, acknowledgement, and retreat are `needs_parent_review` for runtime binding even though the entity-state candidates are ready.

## Parent wiring proposals

| Unit | Entity wrappers | Proposed runtime directory | Selection proposal | Parent-owned files |
| --- | --- | --- | --- | --- |
| `zombies` | `chaosx_zombies_{idle,move,attack,death}` | `sound/002_zombie_outbreak/zombies/zombies/` | `chaosx_zombies_selection_01.wav` only after shared-tag decision | sound definitions, category registration, entity event wiring, unit/entity/GFX wiring, live-game review |
| `infected_zombies` | `chaosx_infected_zombies_{idle,move,attack,death}` | `sound/002_zombie_outbreak/zombies/infected_zombies/` | `chaosx_infected_zombies_selection_01.wav` only after shared-tag decision | sound definitions, category registration, entity event wiring, unit/entity/GFX wiring, live-game review |
| `rabid_zombies` | `chaosx_rabid_zombies_{idle,move,attack,death}` | `sound/002_zombie_outbreak/zombies/rabid_zombies/` | `chaosx_rabid_zombies_selection_01.wav` only after shared-tag decision | sound definitions, category registration, entity event wiring, unit/entity/GFX wiring, live-game review |
| `undead_zombies` | `chaosx_undead_zombies_{idle,move,attack,death}` | `sound/002_zombie_outbreak/zombies/undead_zombies/` | `chaosx_undead_zombies_selection_01.wav` only after shared-tag decision | sound definitions, category registration, entity event wiring, unit/entity/GFX wiring, live-game review |

The package-local final files are evidence candidates; no runtime path currently points to `docs/assets/`. Parent must review each candidate in context, choose variation policy, copy accepted WAVs, and record destination/source hash equality.

## Licensing confidence and uncertainty

Licensing confidence is `high` for all selected families because each source page identifies its creator and explicitly marks the work CC0 1.0 or CC-BY-SA 3.0, and each package retains the page plus applicable legal-code snapshots. The base and infected body-fall candidate uses CC-BY-SA 3.0 and carries the required `Falling body` by remaxim, OpenGameArt.org, attribution; their unarmed-impact candidate is the CC0 Delta12 Studio `punch.ogg` file. The undead bone chain has an additional linked Freesound source page confirming the `bone shell` recording by blukotek/Piotr Zaczek is CC0; the shipped candidate is the explicitly CC0-marked congusbongus adaptation pack. The base and infected packages use the same CC0 artisticdude pack as separately preserved downloads, with package-local hashes and page snapshots.

The principal uncertainties are semantic rather than rights-related: artisticdude's 24 zombie files are unlabeled individually, Darsycho's long snarls and the multi-file packs were bounded to first segments for one-shot candidates, and this model cannot accept audio input for subjective listening. The parent should audition the `_02` files in the game context, adjust only license-permitted mechanical trims/fades/levels, and reject any role whose identity or pacing does not fit the accepted model action.

## Validation and cost

Source and derived `ffprobe` receipts record codec, sample rate, channels, bit depth, and duration for every valid audio member and final WAV. `ffplay` receipts show exit code 0 for all 32 delivered final candidates. This is a decoder/playback check only and does not establish semantic listening acceptance. Source download cost is 0; no Meshy or Blender operation was used. No Git commit was created per parent instruction.

No fallback or simplification was used for the four delivered packages. The base `zombies` runtime files remain untouched; the separate source-backed base candidate package is documented and ready for parent review. The old unlabeled physical candidates remain preserved alongside the new named `_02` candidates. Exact semantic identity, tag-wide selection/acknowledgement/retreat binding, action-specific FPS/frame mapping, and final runtime acceptance remain parent gates.
