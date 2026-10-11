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
