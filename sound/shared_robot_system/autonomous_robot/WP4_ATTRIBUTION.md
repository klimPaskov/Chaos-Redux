# Robot burst recording attribution

`autonomous_robot_mg_report.wav` and `autonomous_robot_mg_short_burst.wav` derive from “Machine gun firing (blanks. In studio shoot).wav” by Cymeon, https://freesound.org/people/Cymeon/sounds/205901/, CC0 1.0.
The original archived HQ recording has SHA-256 `f8117a396c4d75e0977e797c42e2559574c8d67080152608396c8686790147ac`.
Changes: a dry 100 ms recorded report excerpt, eleven repetitions at 0.25 second intervals for the 2.6 second sustained burst, and four repetitions at 0.1667 second intervals for the 0.6 second braced burst, with fades, DC removal, mastering and mono PCM16/44.1 kHz conversion.
This edits and assembles recorded samples and generates no source-free waveform.
Installed long-burst SHA-256: `daf6e4237a257946d5190a6cb0bfbd08fd471d03e51db28f895974995a4ebad7`.
Installed short-burst SHA-256: `f0bed756ce43767c2606f7438c011a58a8dcc712e0da1695400d28b8134372ba`.

The two guns intentionally share this declared robot weapon pool.
Attack and support attack use one long cue per gun; defend uses one short cue per braced gun burst.
The effect limits each cue to two audible sources at volume 0.36 and preserves the recorded cadence without random playback-rate changes.
The source description identifies machine-gun blanks but does not identify the gun model.

Original archive paths, mastering measurements and installed-byte proofs are recorded in `docs/plans/unit_fix_2026-10/wp4_audio_evidence/provenance_index.md`, the two robot batch reports, and `install/accepted_tranche1.json`.
Attribution and licenses for unchanged recordings remain in `ATTRIBUTION.txt`.

## Short contact and casing repairs

`autonomous_robot_impact_footfall.wav` combines already archived “Metal drop thump” by stephan (public-domain dedication via PDSounds, https://commons.wikimedia.org/wiki/File:Metal_drop_thump.ogg) and “Door knocker audio” by Mx. Granger (CC0 1.0, https://commons.wikimedia.org/wiki/File:Door_knocker_audio.ogg).
Original SHA-256 values: `b8f5506893d2871c86f5c7e01305bff788dfe156a265e63bb9b00cbbd51647c5` and `3362b0bd105382bd8f5e0d268b8e7318233abd966c43449241bfee1f35b47c35`.
Mechanical edits cut the metal recording at 0.072721–0.272721 seconds and the knock at 0.441950–0.561950 seconds, mix them at −9 dB each, then fade/master the 0.200-second mono PCM16 recording at 44.1 kHz to the footstep role gate.
Installed SHA-256: `b7a8eab4b8790f63df32472c75b3f10be1d13da96c3d547eb9cc7b63b9904942`.

`autonomous_robot_casings_02.wav` uses “Bullet casings falling” by barryshamir, CC0 1.0, https://freesound.org/people/barryshamir/sounds/834236/.
The archived HQ source has SHA-256 `6508d83460fefbe5a74c22ac0e75117e15d074a89bedd03c4709ce469b00fdf5`.
The selected excerpt is 3.280–3.980 seconds, faded/mastered into a 0.700-second mono PCM16 recording at 44.1 kHz so it ends before the next casing cue.
Installed SHA-256: `443f4a2bc0db471f37bb143c68987b9f1b1c8fa6fd6fb009834a3101a203b638`.
No audio was generated or downloaded for either repair.

## Wreck blast

`autonomous_robot_wreck_blast.wav` uses “Dynamite explosion in the mountain” by felix.blume, CC0 1.0, https://freesound.org/people/felix.blume/sounds/251401/.
The archived HQ preview has SHA-256 `03ede4462a6657fdd181fa65f9aab9d6fcc181be6cdbb2fb461ee2aa638da318`.
Changes retain a two-second excerpt, remove DC/subsonic bias, apply an 8 ms entry fade and 50 ms release, and master to -3 dBFS in mono PCM16 at 44.1 kHz.
Installed SHA-256: `85806914dfbf0a60eeda78f446938d808cc94e82febbe5432fb4f854983addc5`.
The preserved transformation and install receipts are `docs/plans/unit_fix_2026-10/wp4_audio_evidence/reports/robot_blast_batch.json` and `install/accepted_tranche4.json`.

## Complete existing-source cue repairs

`autonomous_robot_hydraulic_release.wav` uses “Hydraulic Truck Brakes by Filmscore” by Filmscore (CC0 1.0, https://freesound.org/people/Filmscore/sounds/823069/).
Verified immutable source SHA-256: `29537bae2513c8448b1076189bb005a0c37a4f3ea8f202f7dfb5b897e32a90e5`.
Mechanical source trimming where applicable, entry/release fades, level mastering and mono PCM16 at 44.1 kHz preserve the declared sound identity.
Installed derivative SHA-256: `da0c5f6c8c5bbcec8934a6b5146307996e6986f426de28b43e48e26c18f1fd33`.
Original sources, selected candidates, exact transformations and measured receipts are retained in `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/wp4_audio_takeover/receipt.json` while the model repair remains active.

`autonomous_robot_gun_heave.wav` uses “080223-002-freight-elevator.wav by joshs” by joshs (CC0 1.0, https://freesound.org/people/joshs/sounds/203392/).
Verified immutable source SHA-256: `4b472a619f344d0377e99e997a4c1630c17f0015356b954b9be93dfb8effb68b`.
Mechanical source trimming where applicable, entry/release fades, level mastering and mono PCM16 at 44.1 kHz preserve the declared sound identity.
Installed derivative SHA-256: `f1852b729f8b18a61a5c9292a01de201f908e49daae99a301db3f66fd6970e0a`.
Original sources, selected candidates, exact transformations and measured receipts are retained in `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/wp4_audio_takeover/receipt.json` while the model repair remains active.

`autonomous_robot_idle_loop.wav` uses “Cordless Screwdriver” by Maximilian Schönherr (CC BY-SA 4.0, https://commons.wikimedia.org/wiki/File:Akkuschrauber_%E2%80%93_Cordless_Screwdriver.ogg).
Verified immutable source SHA-256: `a53525ce339297e1536a6efe0c0d7a6d867e53567e40edc2b8e2ff1376d112cb`.
Mechanical processing selects the original motor recording at 10–14 seconds, fades/masters the loop to −20 LUFS and converts to mono PCM16 at 44.1 kHz; measured loudness rises 6.2 LU relative to the retained runtime loop.
This adapted motor recording remains licensed under CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/.
Installed derivative SHA-256: `1a2b54b595bd7363e4fc90924767b5610e035f8a976524060bf0434595694070`.
Original sources, selected candidates, exact transformations and measured receipts are retained in `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/wp4_audio_takeover/receipt.json` while the model repair remains active.

No audio was downloaded, synthesized or recorded by the agent; no auditory, spoken-word or live playback acceptance is asserted.
