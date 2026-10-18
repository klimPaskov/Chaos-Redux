# Audio mastering recovery 2 handoff

Status: the bounded true-peak/limiter follow-up is implemented and validated for the reviewed 19-entry allowlist. It writes only into this `recovery2_evidence/` folder and changes no runtime sound, source WAV, sound definition, entity, or parent batch report.

The report is [recovery2_batch.json](recovery2_batch.json), and the 17 passing derived WAVs are in [staged/](staged/). The two short loops that could not meet the measured 3 dB loop-edge gate remain unresolved with no staged candidate: `sound/002_zombie_outbreak/zombies/zombie_idle_moan_03.wav` and `sound/014_cannibalism/units/cannibal_march_predation_column/cannibal_march_predation_column_idle_vocal.wav`.

## Reproduction command

Run from the mod root with Python 3.9+ and FFmpeg/ffprobe on `PATH`:

```powershell
python .tools/3d_pipeline/audio/master.py batch --manifest docs/plans/unit_fix_2026-10/audio_evidence/recovery_allowlist.json --source-root . --output-root docs/plans/unit_fix_2026-10/audio_evidence/recovery2_evidence/staged --report docs/plans/unit_fix_2026-10/audio_evidence/recovery2_evidence/recovery2_batch.json
```

This is the reproducible command for the evidence paths; the reviewed one-pass candidate files were moved into `recovery2_evidence/staged/` after mastering without audio reprocessing, then every file hash was checked against the report. The allowlist remains SHA-256 `f54be677c554c0d9177dd13ed84118d821d5219b2b4ea33566c3fb49d7da8e63`.

## Results

The final evidence contains 17 staged candidates, zero `needs_review` candidates, and two unresolved short-loop sources. The four previously reported loop loudness/true-peak conflicts now pass without loosening the gates: zombie idle moan is -20.2 LUFS / -1.0 dBTP / 2.77 dB edge delta after 1.50 dB measured maximum limiter reduction; plague-carrier idle is -20.7 LUFS / -1.0 dBTP / 1.66 dB after 6.00 dB; scavenger idle vocal is -20.4 LUFS / -1.0 dBTP / 2.92 dB after 1.50 dB; and black-plague rat movement is -20.9 LUFS / -1.0 dBTP / 0.45 dB after 1.50 dB.

The two one-shots that had failed the RMS review now pass the existing -18 dBFS ±4 dB band while retaining the -3 dBFS peak target: plague-carrier selection measures -21.94 dBFS RMS and clone-infantry rifle measures -21.86 dBFS RMS. Each selected limiter pass measures approximately 3.00 dB maximum gain reduction, with its sample-aligned measurement, `alimiter` input/output hashes, loudness-normalization command, and final hash retained in the JSON report.

Both one-shot results sit near the lower edge of the allowed RMS band: the plague-carrier selection clears it by about 0.06 dB and the clone-infantry rifle by about 0.14 dB. The gates and tolerances were not widened.

The limiter sweep is bounded to a requested peak push of 0–6.5 dB and the maximum aligned sample gain reduction is recorded for every attempt. The highest reading is 6.50000046 dB, less than one-millionth of a decibel above the ceiling from float-sample arithmetic; no audio target was relaxed. The four named loop recoveries use 1.50, 6.00, 1.50, and 1.50 dB respectively.

The outputs remain derivatives of the existing recorded bytes: 30 Hz high-pass, measured lead trim, 8 ms fade-in, 50 ms fade-out, equal-power head/tail crossfades only where needed, bounded real-sample limiting, EBU loudness normalization, and final measurements. No samples were synthesized, no audio was downloaded, and no long super-event track was processed.

The read-only sound-tree report is [sound_tree_audit.json](sound_tree_audit.json), SHA-256 `ace33f5bd5c6f93f498eab8e8caece6a7d7801170a2b9a123ac4bcb14c5a9f21`. It measured all 311 supported files under `sound/` with four workers, including 71 long-form files kept audit-only, and had zero analysis errors. Its 209 active cue rows include 173 single-sample cues, 53 cue rows without `prevent_random_repetition = yes`, and attribution-map matches for 12 of 209 path rows. The audit found 54 undeclared cross-unit duplicate groups; no accepted family-pool declaration file was provided to this CLI, so these groups remain flagged and no unique takes or approved pools were invented.

The whole-tree audit can be reproduced from the mod root with:

```powershell
python .tools/3d_pipeline/audio/master.py audit-tree --root sound --inventory docs/plans/unit_fix_2026-10/pipeline_evidence/baseline_inventory.json --attribution-map docs/plans/unit_fix_2026-10/audio_evidence/attribution_map.json --output docs/plans/unit_fix_2026-10/audio_evidence/recovery2_evidence/sound_tree_audit.json --workers 4
```

## Parent CLI and installation compatibility

The read-only inspector accepts the parent integration's flag form as well as the prior positional input form. `--force` permits replacing an existing JSON report; it does not bypass or alter the measured gates. The requested probe was run and saved to `audio_evidence/final_source_probe.json`; it reports the original forest-giant source's shot role checks, with the sample peak and RMS passing and PCM signed-16 codec/bit-depth checks failing on the unmastered source bytes.

```powershell
python .tools/3d_pipeline/audio/master.py inspect --input sound/012_africa/units/forest_giants/chaosx_forest_giants_attack.wav --role shot --output docs/plans/unit_fix_2026-10/audio_evidence/final_source_probe.json --force
```

The recovery report retains its original row fields. The separate [recovery2_install_compatible.json](recovery2_install_compatible.json) adds the established `source_relative_path`, `source_sha256`, `destination_path`, `output_sha256`, `before`, `after`, `checks`, and `processing` aliases for the 17 `staged` rows; the two unresolved rows are listed under `excluded_results` and are not install candidates. Rebuild this view without remastering audio with:

```powershell
python .tools/3d_pipeline/audio/master.py compat-report --input-report docs/plans/unit_fix_2026-10/audio_evidence/recovery2_evidence/recovery2_batch.json --output docs/plans/unit_fix_2026-10/audio_evidence/recovery2_evidence/recovery2_install_compatible.json
```

The compatibility view is SHA-256 `555272c21b2d9a1050a609f8215031efd80550fafacd4f3327cb047be40c1d8e`, references the unchanged recovery report by SHA-256, and its 17 aliased destination files were rechecked against their output hashes. The requested source probe report is SHA-256 `5c1d696aeca335deee5030862714bb027fc180791e0c320fc95a0a983b54347b`.

## Integrity, tests, and remaining work

The unchanged parent report `audio_evidence/master_batch.json` remains SHA-256 `ec787f36a48db089ef306fb1802736361b0e8d1574de6bedc95577cea61d8e77`. The reviewed allowlist remains hash-identical. All 17 staged output files exist, their SHA-256 values match the report, all output reports include codec/astats/R128/direct-sample analysis, and every staged item passes its listed codec, rate, channel, bit-depth, lead, flat-top, spectrum, role loudness/peak, and loop-edge checks.

The final recovery report is SHA-256 `e277faf5be6a49d26fd81bf305b0b873ada14e0ae3e36bb11e9f95ff78cf360a`. The audit used FFmpeg and ffprobe `N-123778-g3b55818764-20260331`.

`python -m py_compile .tools/3d_pipeline/audio/master.py .tools/3d_pipeline/audio/metrics.py .tools/3d_pipeline/audio/inventory.py .tools/3d_pipeline/audio/tests/test_master_gates.py` passed. `python -m unittest discover -s .tools/3d_pipeline/audio/tests -v` passed all 19 tests, including the parent flag-based inspector probe, the compatibility-report schema, a real-recording bounded-limiter measurement, an installed vanilla infantry reference, recorded-loop crossfade checks, and post-master onset trimming.

The two fundamentally unsuitable short loops remain unresolved. The parent report's island-reavers death and battalion idle-breath source-quality blockers were excluded from this recovery and remain unresolved there; this pass does not attempt to reconstruct clipped or spectrally unsuitable source material. Parent provenance review, final allowlist selection, and CAS installation remain pending; no claim of runtime or in-game completion is made.
