# Mastering recovery follow-up

Status: the source-only recovery pass is complete for the 19 `needs_review` entries in the parent batch. It changed only the audio tooling and wrote candidates and reports under this `audio_evidence/` folder. No source WAV, runtime WAV, sound definition, entity, gameplay file, or parent batch report was edited.

## Inputs and command

The recovery allowlist in [recovery_allowlist.json](recovery_allowlist.json) copies the parent entries’ source paths, expected SHA-256 values, roles, consumer identifiers, and attribution rows. It excludes the two source-quality `unresolved` entries from the parent batch. Its source report was [master_batch.json](master_batch.json), SHA-256 `ec787f36a48db089ef306fb1802736361b0e8d1574de6bedc95577cea61d8e77`; the parent report has the same SHA-256 after this run.

```powershell
python .tools/3d_pipeline/audio/master.py batch --manifest docs/plans/unit_fix_2026-10/audio_evidence/recovery_allowlist.json --source-root . --output-root docs/plans/unit_fix_2026-10/audio_evidence/recovery_staged --report docs/plans/unit_fix_2026-10/audio_evidence/recovery_batch.json
```

The original source files were read by hash and left unchanged. Trims, fades, crossfades, and gain corrections were applied only to derived candidates. Every result preserves its original source SHA, attribution manifest path/hash/row, each intermediate and output hash, exact FFmpeg arguments, and final metrics in [recovery_batch.json](recovery_batch.json). The six unresolved sources were rerun through a diagnostic-only allowlist in [recovery_diagnostics_batch.json](recovery_diagnostics_batch.json); no WAV was staged for them.

## Results

The 19 review entries produced 11 `staged` candidates, 2 `needs_review` candidates, and 6 `unresolved` results. The recovery folder contains 13 WAV candidates: the 11 passing outputs and the 2 outputs retained for RMS review. The six unresolved entries have no output file.

Measured post-master onset correction trimmed each of the four original lead failures using the observed lead duration, kept 10 ms pre-roll, applied an 8 ms fade-in, and remeasured. Final lead silence is 0-9.98 ms on all four. The bone-guard idle vocal and scavenger death cue pass their other gates. The plague-carrier selection and clone-infantry rifle cue remain `needs_review` because their RMS is -23.74 dBFS and -22.94 dBFS against the configured -18 dBFS ±4 dB one-shot band; both retain the -3 dBFS peak target and correct output format.

Nine loop candidates pass after an equal-power blend of recorded tail/head samples followed by fades, loudness normalization, and final measurements. Each report records the selected overlap length, SHA-256 of the source-derived mixed samples, final loop-edge RMS delta, integrated LUFS, true peak, and final output SHA. Loop-edge RMS deltas for those outputs are between 0.33 and 2.59 dB. The output remains ordinary PCM16 WAV built from existing recordings; no tones, noise, or new audio samples were created.

The cave-monster idle now measures -20.0 LUFS with a -4.0 dBTP true peak and loop-edge RMS delta of 1.67 dB. Four other loop sources cannot reach -20 LUFS within the -1 dBTP ceiling after the recorded-source normalization pass: zombie idle moan `-21.5 LUFS / -1.0 dBTP`, plague-carrier idle `-21.8 / -1.0`, scavenger idle vocal `-21.3 / -1.0`, and black-plague rat movement `-21.1 / -1.0`. The report records the requested gain and available true-peak headroom, then leaves each source unresolved.

Two short or unsuitable loop recordings never reached the 3 dB edge gate with the bounded recorded-sample crossfade search: zombie idle moan 03 (0.67 s) and cannibal march idle vocal (1.00 s). They remain unresolved with no final file.

The two parent source-quality blockers, island-reavers death (source SHA-256 `7a4a4356a5cc9bb160d32516add22d58149f08e4556dafd181684c0489141aab`, 18-sample rail run) and battalion idle breath (`222debcb8972edaed5b4b34a620714065cb003836c3fa9fcfce935fb18746b9f`, 15-sample rail run and 92.97 Hz centroid), were excluded from retries and remain unresolved in the original parent report.

## Verification and parent work

All 15 audio tests pass, including direct inspection of real installed vanilla audio, a real gorilla loop crossfade, an unresolved short zombie recording, and a real post-master lead-trim check. The parent-owned `master_batch.json` remained byte-identical at SHA-256 `ec787f36a48db089ef306fb1802736361b0e8d1574de6bedc95577cea61d8e77`.

The parent retains the final provenance review, selection of staged files, and CAS promotion into runtime. It should keep the two RMS-review shots, four loudness/true-peak conflicts, two edge failures, and two clipped sources unresolved unless further accepted source material or a revised design resolves them. No provider call, audio download, Blender operation, or runtime installation occurred in this follow-up.
