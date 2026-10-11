# WP4 firing and recorded-audio tranche

Historical tranche record, superseded for current implementation and open requirements by [WP4 gun troopers repair report](wp4_gun_troopers_report.md), including its 11 October takeover review.
Measurements below describe the archived tranche candidates; they do not replace the current report's selected-file hashes, finite particle review or subsequent audio work.

Disposition: implemented source wiring and installed recorded-audio replacements; visual and live playback acceptance remain pending.
Acceptance basis: the user's explicit WP4 assignment, its per-model tickets, and the requirement to mirror vanilla's one-emission-per-burst pattern.
This is a bounded firing/audio tranche, not completion of the nine-model repair package.

## Delivered consumers

| Consumer | Firing change | Recorded audio |
|---|---|---|
| Assassin Cadre, Shadow Company, Master Assassin | Attack/support/defend flash spawns 9/12/9 → 3/4/3, retaining each first authored burst and adding one smoke emission per burst | Shared 0.3 s dry SMG burst; two distinct 0.9 s death takes at 0.3 s |
| Silent Guard | Attack/support/defend flash spawns 6/6/3 → 2/2/1, with one smoke emission per burst | The declared 039 infantry-family burst/death pool through its own wrappers |
| Mechanized Assassin | One barrel flash and timed sound per cycle at attack 0.7667 s, support 0.9667 s, defend 0.2333 s | Installed vanilla MG sources, with random onset/playback changes omitted; defend uses only takes 02–05, which fit its 1.6667 s cycle |
| Clone Infantry | One muzzle flash and one bolt cartridge in attack, defend and support; attack/support lead into the existing defend action | Source-bound 0.45 s recorded Lee-Enfield report replaces the inherited simulated cue |
| Portal Raider | Finite laser discharge particles at the existing authored times | Source-bound one-second electrical loop, −20 LUFS, starts once in idle/guard, maximum one audible source |
| Alien Infantry | Finite laser discharge particles at the existing authored times | Other audio repair remains open |
| Autonomous Robot | Attack/support flash and smoke spawns 22/22 → 2/2; defend 8/8 → 2/2; one emission and cue per gun/burst | Dry recorded 2.6 s sustained and 0.6 s braced bursts, volume 0.36/max two audible sources, retaining each gun's first discharge time |

The 039 infantry burst uses three distinct archived gunshot transients, trimmed and faded individually rather than retaining long reverberant tails.
The robot burst deliberately assembles existing recorded reports at the current action's cadence; the two guns share one declared weapon pool.
Both infantry flash/smoke pairs are intentional vanilla-style combinations.
Cadre/Guard cartridge effects remain absent because their installed meshes have no measured ejection locator.
Energy weapons eject no brass.

## Installed recording measurements

| Runtime recording | Duration | Peak / RMS dBFS | Source | Proof |
|---|---:|---|---|---|
| 039 infantry attack | 0.300 s | −3 / −16.18 | Vincent Svedberg, uploaded by Tabasco; archive CC BY 3.0 | `wp4_audio_evidence/reports/039_batch_dry.json`, `install/accepted_tranche2.json` |
| 039 death takes 02/03 | 0.900 s each | −3 / −17.29 and −17.82 | thebardofblasphemy, CC0 | `wp4_audio_evidence/reports/039_batch.json`, `install/accepted_tranche1.json` |
| Robot long burst | 2.600 s | −3 / −19.25 | Cymeon, CC0 | `wp4_audio_evidence/reports/robot_long_batch.json`, `install/accepted_tranche1.json` |
| Robot braced burst | 0.600 s | −3 / −17.59 | Cymeon, CC0 | `wp4_audio_evidence/reports/robot_short_batch.json`, `install/accepted_tranche1.json` |
| Clone rifle report | 0.450 s | −3 / −18.17 | kyles, CC0 | `wp4_audio_evidence/reports/clone_rifle_final_inspect.json`, `install/accepted_tranche3.json` |
| Portal electrical loop | 1.000 s | −7.62 peak; −20 LUFS | Hansjörg Malthaner (Varkalandar), CC BY 4.0 | `wp4_audio_evidence/reports/portal_loop_batch.json`, `install/accepted_tranche3.json` |

All seven replacements decode as mono PCM16 at 44.1 kHz and pass the locked role gates.
The portal loop's inner head/tail RMS difference is 2.58 dB.
Installation receipts preserve target preimages, source/candidate/report hashes, measurements, source attribution and destination verification.
Runtime attribution is retained beside the audio files; the complete source index is `wp4_audio_evidence/provenance_index.md`.
The first sustained CZ candidate and the loud first death take failed their RMS gates and were not installed.

## Source review and validation limits

The exact installed vanilla infantry MG, mechanized entity, particle registry and soundeffect precedents were read alongside the offline wiki.
`wp4_evidence/references.json` retains source paths, cited line spans and source hashes.
The connected session exposes no HOI4 reference/validation routes; local reading and pipeline parsers do not constitute engine acceptance.
`wp4_evidence/entity_baseline.json` preserves the pre-edit entity blocks, including clone inheritance, rather than reading changed source as a baseline.
`wp4_evidence/particle_crosswalk_interim.json` and `bindings_interim.json` retain counts, actual delivered locator names, effective inherited scales and resolved cues.
The inherited tranche named `wp4_wiring_audit.md` as an independent wiring-audit handoff, but that file is absent in the takeover workspace and cannot support an audit claim.
Current source and copy checks are instead identified in the takeover report.

The shared lint counts MG smoke as another flash and reports intentional same-time flash/smoke emissions as overlaps.
Its unfiltered findings must be retained, with these cases distinguished from actual repeated flashes or uncontrolled smoke.
The robot's two parallel gun cues are intentional weapon-pair polyphony; the quieter two-source cap is part of this accepted repair.
Authored discharge/contact proof, visible flash area and duration, material/deformation review and actual playback remain separate acceptance gates.

## Remaining work

The package's UV rebakes, holes/winding repairs, class-specific material maps, cloth weights, recoil, idle and gait/action repairs remain in `wp4_gun_troopers_report.md`.
All installed mesh/action hashes remain unchanged by this tranche.
Cadre/Guard need measured cartridge locators; the model worker may not replace an occupied WP3 Blender scene.
The dedicated mechanized destruction cue and remaining clone/portal/alien/robot source repairs are separate pending audio work.
The source-bound 039 burst is one composite variation; its three component shots are distinct recordings, while additional composite variants remain a separate take-coverage requirement.
No substituted model or unverified recording is treated as accepted output.

## Orchestrator playback and filming checks

Use a 1936 save, select a country with room for staging, run `e chaosx_test`, and allow the CXT receiver to initialize.
Use one single-battalion division per WP4 sub-unit so each chosen sprite is unambiguous; the three 039 derivatives must be separate divisions.
Capture idle, move, attack, support attack, defend and death for every entity, using the existing showcase setup.
For combat, wait until the division has reached its combat position and lock the crop to its entity position rather than a motion detector.
Capture at least two full action cycles at the same zoom and audio settings.

Check the 039 infantry for one compact flash/smoke emission per burst, no extra stacked fireball, audible dry three-round reports and alternating death takes.
Measure each flash's visible duration ≤0.5 s and orange area <1,500 pixels; this tranche has no filmed proof of that gate.
Check the mechanized unit for one flash/report per cycle in all three firing states and no defend tail extending into the next cycle.
Check the clone for muzzle reports at 0.75 s in attack and 1.0 s in support/defend, cartridges at 1.5833/1.8333 s, and continued braced fire after attack/support transitions.
Check the portal hum across several idle cycles, after a guard/idle transition, and when leaving those states; it must not restart each cycle or accumulate loops.
Check the robot for a visible body without the old smoke column, two timed dry gun bursts with a quieter mix, and short braced bursts in defend.
Re-film all nine WP4 models after their pending model acceptance gates are addressed; retain the source crop and audio setting evidence with the showcase.
