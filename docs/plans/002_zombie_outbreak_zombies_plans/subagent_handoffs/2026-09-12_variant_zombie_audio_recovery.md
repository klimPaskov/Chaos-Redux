# Variant zombie sourced-audio recovery

Disposition: source acquisition and mechanical preparation **implemented**; cue acceptance and final synchronization **needs_user_review**; selection/order engine binding **blocked**.

The explicit parent task dated 2026-09-12 authorized recovering missing sourced-audio evidence and making licensed mechanical derivatives for `parasitic_zombies`, `mutant_zombies`, `necrotic_zombies`, and `demonic_zombies`.
The four `sound\` roots were absent at intake, consistent with each job's `evidence\inherited_companions.json` and inconsistent with the completed-source claims in `specialized_zombie_audio_source_handoff.md`.
This work creates fresh, verified source packages; it does not invent or reproduce the missing historical checksums.
The parent subsequently confirmed that no final actions are accepted and authorized keeping subjective audition explicitly pending.
The parent then authorized a narrow physical-contact repair after source descriptions failed to support generic body-floor and ordinary unarmed-hit claims.
The four `runtime_attribution.txt` companions and the physical `_02` candidates below are the current provenance handoff.

## Delivered files

All job-local paths below are relative to `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\assets\002_zombie_outbreak\models_3d\`.

| Package root | Valid source-audio candidates | Derived WAVs | Provisional timing rows | Files in exhaustive ledger |
|---|---:|---:|---:|---:|
| `parasitic_zombies\sound\` | 29 | 11 | 15 | 95 |
| `mutant_zombies\sound\` | 34 | 11 | 14 | 98 |
| `necrotic_zombies\sound\` | 59 | 11 | 14 | 122 |
| `demonic_zombies\sound\` | 84 | 11 | 14 | 147 |

The 206 source-audio count is package-local and includes independently preserved copies of shared licensed source families.
There are 44 derived WAVs, eleven per package: nine current role proposals covering selection, acknowledgement/order, idle, two movement contacts, attack vocal, ordinary unarmed impact, death vocal and body-floor impact, plus two preserved unscheduled impact accents.
Every derivative is PCM signed 16-bit little-endian (`pcm_s16le`), 44100 Hz, mono, with a duration between 0.2250 and 1.7000 seconds.
Each package includes:

- `originals\<source_id>\`: original downloads, including original ZIP archives.
- `extracted\<source_id>\`: byte-identical audio archive members; archive-only entries remain preserved in their original ZIP.
- `derived\<unit>_<cue>.wav`: eleven concrete candidates, including physical `attack_impact_02` and `death_impact_02` and the two preserved restricted older impact files.
- `manifest.md`, `cue_manifest.json`, and `derived_cues.csv`: explicit asset status, exact source/archive/member/derived SHA-256 hashes, source URLs and attribution, trim spans in seconds and 44100 Hz samples, gain, fades, complete ffmpeg arguments, and ffprobe receipts.
- `source_provenance.md`, `source_checksums.csv`, and `audio_inventory.csv`: all licensed source families, original/member hashes and decoded metadata, including currently unselected alternatives.
- `evidence\source_pages\`, `evidence\source_page_registry.json`, `evidence\approved_sources\`, `evidence\licenses\`, and `evidence\acquisition_receipts.json`: primary-page HTML, the immutable initial pre-acquisition registry, later source approval decisions, CC0 and CC-BY-SA license snapshots, download URLs/headers/retrieval dates, archive membership and technical receipts.
- `runtime_attribution.txt`: all eleven cue source titles, creators, source/direct URLs, exact original/archive/member/derived hashes, license snapshot filenames and hashes, mechanical transformations, provisional synchronization and explicit candidate/not-auditioned status.
- `semantic_fit_review.json`, `role_candidate_selection.json`, `evidence\physical_source_verification.json`, `evidence\physical_source_copy_receipts.json`, and `evidence\physical_recovery_intake_checksums.json`: physical-role evidence, current proposals, exact origin/destination copy hashes, and proof that all prior original/extracted/derived audio bytes were preserved.
- `evidence\pre_physical_recovery\` and `evidence\rejected_sync_candidates.json`: prior cue/timing/crosswalk/QC records and the removed unsupported grasp-only impact proposals.
- `synchronization_provisional.json` and `.csv`, plus `evidence\action_timing_snapshot.json`: exact candidate action paths/hashes, named phases, FPS, event-time calculations and cue hashes.
- `requirement_to_runtime.json` and `.csv`: 17 rows per package covering all nine cues and eight action-synchronization requirements, with intended consumer and explicit review/blocker status.
- `sound_design_handoff.md`, `evidence\consumer_and_intake.json`, `evidence\local_consumer_reference.md`, and `evidence\final_validation.json`: consumer inspection, current versus historical evidence, sound direction/mix proposals, and actual validation results.
- `audition.html`: local playback controls for each cue and links to its source; no audition is claimed merely because this page exists.
- `evidence_checksums.csv`: every package file except the ledger itself.

The parasitic package also preserves six mechanical acquisition/processing/evidence scripts under `sound\evidence\`.
The initial acquisition/derivation/finalization scripts describe the original tranche; current physical-contact records are produced by `recover_physical_contacts.py` and `finalize_physical_recovery.py`.
The original downloads are non-shipping evidence, and no runtime file references the new package roots.
`docs\assets\` is ignored by Git; the retained on-disk packages must remain available while acceptance is pending.
The parent owns any durable evidence promotion and event-workspace lifecycle decision.

## Verified sources and licensing

Twelve source families state CC0 1.0; the thirteenth, Falling body, is offered under CC-BY-SA 3.0 among alternative licenses, and this package selects CC-BY-SA 3.0.
The exact current attachment URLs were recorded before acquisition.
Originals, HTML snapshots, retrieval dates, headers, original/member checksums and complete technical metadata are preserved in each consuming package.
The [CC0 legal code](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en), [CC-BY-SA 3.0 deed](https://creativecommons.org/licenses/by-sa/3.0/) and [CC-BY-SA 3.0 legal code](https://creativecommons.org/licenses/by-sa/3.0/legalcode.en) are archived.
CC0 credits are voluntary; Falling body attribution, change notice and share-alike terms are mandatory for the selected license.

| Source title and current primary page | Creator | Packages / use |
|---|---|---|
| [Slimy monster or murder sounds(9)](https://opengameart.org/content/slimy-monster-or-murder-sounds9) | pauliuw | Parasitic and necrotic wet contacts; parasitic short idle cue |
| [Insect or alien scream](https://opengameart.org/content/insect-or-alien-scream) | qubodup | Parasitic selection, acknowledgement and attack-vocal excerpts |
| [Footsteps](https://opengameart.org/content/footsteps-0) | GboxMikeFozzy | All four source packages; selected movement contacts for parasitic, mutant and demonic |
| [Death sounds](https://opengameart.org/content/death-sounds-0) | Exewin | Parasitic, mutant and necrotic collapse voices |
| [Zombie noises and moans](https://opengameart.org/content/zombie-noises-and-moans) | ianzazz | Mutant voice candidates |
| [Zomby sfx pack](https://opengameart.org/content/zomby-sfx-pack) | saturn91 | Necrotic selection, order, idle and attack candidates |
| [25 CC0 mud sfx](https://opengameart.org/content/25-cc0-mud-sfx) | rubberduck | Necrotic wet movement accents; earlier death impact preserved as an unscheduled wet accent |
| [Fleshy Bone Break/Snap SFX](https://opengameart.org/content/fleshy-bone-breaksnap-sfx) | Zane Little Music | Mutant/demonic conditional fracture accents; rejected for generic body-floor and ordinary-hit bindings |
| [CC0 Deep Monster Roar](https://opengameart.org/content/cc0-deep-monster-roar) | trazzz123 | Archived mutant/demonic alternative; not selected into a derived cue |
| [demon voice](https://opengameart.org/content/demon-voice) | Tim Rockk | Explicitly named demon growls, snarl, fight grunt and death recording |
| [Horror scream1](https://opengameart.org/content/horror-scream1) | Vinrax | Archived demonic alternative; not selected into a derived cue |
| [Rpg Sound Effect Pack: punch](https://opengameart.org/content/rpg-sound-effect-pack) | Delta12 Studio | All four ordinary unarmed-strike `_02` candidates, CC0 |
| [Falling body](https://opengameart.org/content/falling-body) | remaxim | All four body-floor `_02` candidates, CC-BY-SA 3.0; creator credits qubodup |

The source names and creators above follow the actual primary pages rather than unverified title/creator combinations in earlier candidate lists.
The qubodup and ianzazz sources also appear in the older audio handoff.
No existing shared base-zombie runtime WAV was copied or used as an input.
The original eleven source families were freshly acquired; the physical repair copies the approved sibling job's original `punch_1.ogg` and `fall.wav` plus source/license snapshots after verifying the current publisher and license pages.

## Physical-contact repair and shipping attribution

The current source page describes Falling body as a dead zombie body hitting the ground.
It credits [Stupid Falls](https://freesound.org/people/qubodup/sounds/50941/) by qubodup, whose page describes recording a body dropping onto carpet and currently states CC0.
The punch source publisher describes effects made for its own game and tutorial, categorizes the collection with punch, and publishes the selected file in its punch entry.
These descriptions support physical candidates; material, perceived mass, claw texture, mix and exact phase fit still require audition.

The exact original copy origin is `docs\assets\002_zombie_outbreak\models_3d\zombies\sound\source\original\`.
Every destination is under one of the four owned sound roots, with separate origin/destination hash receipts.
No source or derived audio bytes in the sibling job were modified.

| Role / source | Package-local original | Original SHA-256 | New derived filename pattern | Derived SHA-256 |
|---|---|---|---|---|
| Ordinary unarmed impact; [punch original](https://opengameart.org/sites/default/files/punch_1.ogg) | `originals\unarmed_impact\punch_1.ogg` | `816049cd8090dd1412fceeae3c097cb32b8482d2f8711306609ffd57ae52d586` | `derived\<unit>_attack_impact_02.wav` | `1f46c961d58915c6961e698a80be1f3a1bda45f95b414f4afb5efcd86a6b7092` |
| Body-floor landing; [fall original](https://opengameart.org/sites/default/files/fall.wav) | `originals\body_fall\fall.wav` | `7d0fccc8488d1d272d93343c12ea92f1b84122c40db2f2c7c4a39fb0de9a0804` | `derived\<unit>_death_impact_02.wav` | `bb7ec81f6971a745218baf4142bfd6549a03a3f5ba449912b32ec702872fbfa6` |

The new files preserve the complete decoded source event: punch spans samples `[0, 9923)` at 44100 Hz, 0.225011338 seconds, with +18 dB gain; body fall spans `[0, 33676)`, 0.763628118 seconds, with -9.907733837 dB gain.
Both use a 5 ms fade-in, 30 ms fade-out, mono conversion, 44100 Hz resampling, metadata removal and PCM s16le conversion.
The punch reaches about -14.04 dBFS because the +18 dB upward-gain ceiling is retained; the body fall reaches about -9 dBFS.
No full-source trimming, layering, pitch alteration or synthesized weight enhancement was performed in this repair.
Identical recordings and identical mechanical recipes produce byte-identical physical WAVs across the four unit packages; the vocal identities remain separately sourced.

The original `attack_impact` and `death_impact` WAVs remain byte-identical to intake.
Bone-break source descriptions do not support a generic body-floor landing; those death candidates are explicitly rejected for that role.
Bone-break attack candidates only support an explicit fracture/injury accent, while slime and mud support wet accents.
The older impact records have empty current soundeffect memberships and no current timing proposals; they must not be added alongside the `_02` files as random variants of the ordinary contact effects.
The parasitic idle squish is identified only as a quiet wet-body accent, mutant idle as a moan candidate, necrotic idle as a call candidate, and necrotic mud movement as wet contact; no unverified breathing or dry-footstep claim is retained.

Required body-fall credit is included verbatim in each `runtime_attribution.txt`: Falling body by remaxim, OpenGameArt.org, licensed CC-BY-SA 3.0, based on Stupid Falls by qubodup, with source/license URLs and a mechanical-change notice.
Every body-fall derivative retains CC-BY-SA 3.0.
The legal code explicitly treats synchronizing a phonogram with moving images as an adaptation; the parent must resolve compliant synchronized runtime distribution before promotion.
This handoff does not assert that the license obligation ends at the WAV or that the whole mod automatically receives a particular license.
The license snapshot paths are `evidence\licenses\CC-BY-SA-3.0-deed.html` and `evidence\licenses\CC-BY-SA-3.0-legalcode.en.html`; their exact hashes are in each attribution packet and exhaustive ledger.

## Mechanical derivation and review limits

Allowed processing consisted only of archive extraction, threshold-guided removal of leading/trailing low-level material, bounded excerpts, amplitude normalization, short fades, mono conversion, resampling, metadata stripping and WAV codec conversion.
The original files remain immutable.
No worker-created recording, synthesis, generated waveform, placeholder, sound overlay, pitch shift or time stretch was used.
The exact original/archive/member-to-derived chain is in every `cue_manifest.json` row; no source hash is inferred from a filename.

Analysis used a 44100 Hz mono decode, a -42 dBFS signal threshold, a 10 ms leading margin and up to 25 ms trailing margin, followed by the explicitly recorded duration limit and offset for that cue.
Peak targets are -12 dBFS for idle/movement, -9 dBFS for impacts and -8 dBFS for other vocals, with upward gain limited to 18 dB.
Fades and gain can make the measured peak slightly quieter than the target.
All 44 candidates decode successfully, have finite non-silent signals and correct frame counts, and contain zero saturated PCM samples.
The initial threshold-guided recipe above applies to the preserved original nine-cue sets; the eight physical `_02` files use the complete-source recipe described in the repair section.

Toolchain: FFmpeg and ffprobe `N-123778-g3b55818764-20260331`; absolute executable paths and full build/version output are in each `evidence\toolchain.json`.
The installed vanilla `integrated_dlc\dlc018_together_for_victory\sound\ger\de_Idle_001.wav` was directly probed and matches the chosen PCM s16le/44100 Hz/mono/16-bit format.
This actual consumer precedent and the explicit parent delivery contract take priority over the offline Sound modding page's float-WAV suggestion.

Subjective audition was not performed.
The audio-emission route returned `audio content omitted because you do not support audio input`.
Cue semantics therefore rely on the inspected publisher descriptions and source-member names, supported by objective waveform/decoder checks; listening is not claimed.
Numeric source members, bounded insect excerpts, and the 1.7-second beginning of `DL DEMON DIES.wav` particularly require parent/human audition before final acceptance.

## Consumers and synchronization

Read-only inspection covered installed vanilla `gfx\entities\units_infantry.asset`, `sound\soundeffects.asset`, `integrated_dlc\dlc018_together_for_victory\sound\vo.asset`, the exact vanilla selection WAV, relevant `documentation\effects_documentation.md` entries, offline Sound/Entity/Unit modding, and the eleven required core wiki pages.
No dedicated sound-documentation Markdown was found under installed `sound\` or `gfx\entities\`.
The installed infantry entity uses sound events in movement states, and the voice definitions implement the country/original-tag-wide infantry templates in the `Voices` category.

The inspected mod subunits use:

| Sprite / entity family | Exact subunit consumers |
|---|---|
| `chaosx_parasitic_zombies` | `parasitic_zombies` |
| `chaosx_mutant_zombies` | `mutant_zombies` |
| `chaosx_necrotic_zombies` | `necrotic_zombies`, `armored_necrotic_zombies` |
| `chaosx_demonic_zombies` | `demonic_zombies`, `armored_demonic_zombies` |

Stable proposed records are `chaosx_<unit>_<role>_sound_<nn>` and `chaosx_<unit>_<role>_sfx`.
Proposed runtime WAV paths are `sound/002_zombie_outbreak/<unit>/<unit>_<cue>.wav`.
These names are proposals and do not establish a runtime binding.
Every cue is a one-shot, and idle is an intermittent creature/body cue rather than a manufactured seamless loop.

Every unit has provisional mappings for `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`.
Necrotic timing is read from `evidence\action_specs_depth_v3\`; parasitic death is read from `evidence\action_specs_contact_v19\death.json`; other timing uses the respective `evidence\action_specs\` files.
Parasitic death retains the supplied 30 FPS phases 1 alive, 9 knees fail, 17 reach/fall, 25 impact, 37 settle and 49 still.
The source snapshots record exact hashes without asserting that a native candidate has been accepted or exported.

Proposed event times subtract each original WAV's objectively detected signal-onset offset from `(phase_frame - frame_start) / fps`, clamped at zero.
The physical `_02` cues instead align the largest absolute sample transient to the candidate phase; the tables also retain onset and peak values so the parent can review the estimate.
The tables include phase names, frame/time, cue hash and candidate source hash.
The final timing check found a late necrotic training call and a second demonic parry cue crossing their provisional action boundaries; the final sparse cue proposals keep one training effort/primary parry contact at the earlier named phase.
The repair removed four support impact proposals at grasp/clamp/hook/latch phases because those phases do not establish a strike impulse; support vocals remain proposed.
All 57 current proposal rows have their entire cue tail within the inspected candidate action boundary.
This arithmetic is provisional and is not final skeletal contact or audible synchronization evidence.
No separate special action was supplied, so no special action or sound was invented.

## Simplifications, omissions, and blockers

- **Blocked:** exact selection/order binding for all four units, because the owning country/original tags and all infantry consumers under them are unresolved.
  The engine-consumed templates are `<TAG>_infantry_idle`, `<TAG>_infantry_move_out`, `<TAG>_infantry_neutral_combat`, `<TAG>_infantry_positive_combat`, and `<TAG>_infantry_retreat`.
  This route is tag-wide, and a per-unit `_selection_sfx` name alone cannot create per-subunit selection.
  The package must not override unrelated ordinary infantry, another zombie family, existing `ZZZ_infantry_idle`, or global `select_army`.
- **Needs review:** all cue audition/final selection; final action selection and phase/contact alignment; final parent mix values and active runtime definitions.
- **Needs license integration review:** the CC-BY-SA 3.0 Falling body candidate requires attribution, change notice, share-alike and review of the phonogram/moving-image synchronization-as-adaptation term before runtime promotion.
- **Preserved with limited/rejected semantics:** the eight older ordinary-attack/body-floor impact candidates; source semantics support only wet or explicit fracture accents, with no current event binding.
  The eight `_02` physical candidates supply the requested ordinary strike and body-floor source coverage but remain not auditioned.
- **Parent-owned and not performed:** copying candidates into engine-facing folders, `.asset`/entity/sound/category wiring, job/shared-manifest changes, final source-to-runtime hash synchronization, and overall completion review.
- **Out of this bounded task:** models, geometry, rigs, actions, textures, counters, GFX, gameplay, localisation, and shared lock changes.
  This handoff makes no new acceptance claim about those companions.
- **Skipped meaningful validation:** subjective listening because audio input is unsupported; final synchronized playback because no final actions are accepted; live-game testing because it belongs to the user.
- No source-free or unlicensed audio fallback, generated sound, omitted mandatory source-audio role, or other unauthorized simplification was used.

## Integrity, cost, and remaining parent work

Every current shared base-zombie WAV and `sound\chaosx_zombies_sound.asset` still matches its recorded input hash.
The exhaustive ledgers were checked against the full package file inventories and their hashes.
The ledger excludes only itself; its final checksum closes that chain below.

| Package | `evidence_checksums.csv` SHA-256 |
|---|---|
| parasitic | `d70f2f9dd77fef6181f41a36fd9748a452303855f4f9a080f307a618e36290bc` |
| mutant | `c50d4da6b43f4fac5c0a3dfbba86da21d49b5b11ca13369983ae92865af9e97e` |
| necrotic | `a131012a6880acce72bb541a69de0518ff0a5d7bc82e80e6fba9c5bcb62874bb` |
| demonic | `0ff72d76c734c9977e9619d15368c1572f8d1670d314a45151780e91d8190700` |

| Shipping provenance companion, relative to the model roots above | SHA-256 |
|---|---|
| `parasitic_zombies\sound\runtime_attribution.txt` | `692cd2fc5780fc2f8e95c81c8b8e66b35a2ab1edc1df193f5ed2f9dc4a460359` |
| `mutant_zombies\sound\runtime_attribution.txt` | `6834ddce0c664e9c776ab6f1336a7b559940a248582c31645a363a0969e14288` |
| `necrotic_zombies\sound\runtime_attribution.txt` | `f85a961eb9903a4d46491fcb40ab5230535828431c3507a02a496b21f62ebdbc` |
| `demonic_zombies\sound\runtime_attribution.txt` | `917924c58a0f9b9f711bc7a22b25a7d29610174d718d190ae704cd8007411069` |

Meshy/provider operations, provider task IDs, paid credits estimated/consumed: **none, none, 0 / 0**.
Blender, io_pdx_mesh and model dependency-lock/schema checks are not applicable because no model route was used.
No API key, provider balance, Blender adapter or model operation was queried.
No Git commit was made: these are review-pending audio packages with parent-owned runtime integration, and the shared event work is still active.

The parent should review `audition.html`, accept source members and excerpts, select final skeletal actions, recalculate all phase bindings, resolve tag-wide selection scope, wire accepted runtime copies/definitions, verify source-to-destination hashes, and retain the explicit blockers in the model/event completion report.
Final source-to-runtime synchronization result: **pending; no runtime copy or binding was performed**.
No in-game completion is claimed.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
No skills were created or changed.
