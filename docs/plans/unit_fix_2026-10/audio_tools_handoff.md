# Audio tooling implementation handoff

Disposition: implemented within the authorized shared pipeline scope.
Final parent integration is recorded in `pipeline_report.md`, `audio_evidence/install/manifest.json` and the package reports: 135 installed recordings, 74 held paths, 21 passing focused audio tests and one source-dependent skip.
Historical intermediate test counts and pending-promotion statements below are superseded by those final artifacts; full sound-package acceptance remains open.

## Files owned by this task

- `.tools/3d_pipeline/audio/master.py` provides `inspect`, explicit-allowlist `batch`, and whole-tree `audit-tree` commands.
- `.tools/3d_pipeline/audio/metrics.py` records `ffprobe`, `astats`, EBU R128, spectral-centroid, lead-silence, RMS, direct rail-run, and SHA-256 evidence without changing inputs.
- `.tools/3d_pipeline/audio/inventory.py` reads the baseline consumer inventory, including `sound_cues` and `additional_sound_files`, parses soundeffect variant and `prevent_random_repetition` coverage, retains exact attribution rows, and reports duplicates against declared family pools.
- `.tools/3d_pipeline/audio/README.md` documents the schema, commands, metric bands, and safety behavior.
- `.tools/3d_pipeline/audio/tests/` contains 12 focused tests for inventory rows, nullable samples, direct clipping evidence, attribution parsing, output-name collisions, and real installed audio inspection.
- `docs/plans/unit_fix_2026-10/audio_evidence/` contains the read-only sound-tree report, baseline attribution map, real-recording batch allowlist and report, vanilla reference report, and one staged integration derivative.

## Parent API

Run the full read-only audit from the mod root with:

```powershell
python .tools/3d_pipeline/audio/master.py audit-tree --root sound --inventory docs/plans/unit_fix_2026-10/pipeline_evidence/baseline_inventory.json --attribution-map docs/plans/unit_fix_2026-10/audio_evidence/attribution_map.json --workers 4 --output docs/plans/unit_fix_2026-10/audio_evidence/sound_tree_audit.json
```

For an approved subset, provide a schema-1 manifest with one exact entry per installed WAV. Every entry needs `source` relative to the repository and under `sound/`, the expected installed-byte `sha256`, `unit_id`, the exact `soundeffect`, `role` (`shot`, `step`, or `loop`), and an `attribution` object containing an existing `manifest_path` plus an exact `source_row` or a `match` token. `inventory_path` is recommended so the tool also binds each row to the parent’s baseline. `attribution.source_sha256` may carry the recorded installed preimage; the report preserves its basis and never describes it as a verified checksum of the original Internet file.

```powershell
python .tools/3d_pipeline/audio/master.py batch --manifest docs/plans/unit_fix_2026-10/audio_evidence/master_allowlist.json --source-root . --output-root docs/plans/unit_fix_2026-10/audio_evidence/staged --report docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json
```

The batch rejects a stale source hash, a source without a matching existing attribution row, a source under a path other than `sound/`, a probable direct flat-top, a non-subsonic source whose active-window median centroid is at or below 200 Hz, a super-event source, or any source longer than 60 seconds. It writes only to the requested evidence directory and never overwrites audio. An explicit per-entry `output` is honored, including the parent’s proposed `aNNN.wav` paths; without one, the destination keeps the source basename and adds an eight-character hash of the relative source path, so takes in the same soundeffect do not collide.

## Processing and gates

Every derivative is mono `pcm_s16le`, 44.1 kHz, with metadata removed, a 30 Hz second-order high-pass, measured lead trimming with 10 ms pre-roll, an 8 ms fade-in, and a 50 ms fade-out. The role targets are one-shot peak -3 dBFS within 0.8 dB and RMS -18 dBFS within 4 dB; step peak -6 dBFS within 0.8 dB and, for clips at least 0.4 seconds with usable EBU measurement, -23 LUFS within 5 LU; and loop -20 LUFS within 1 LU, true peak at or below -1 dBTP, and inner head/tail RMS within 3 dB after excluding the fades.

Clipping decisions use decoded source samples as well as `astats`; an `astats` flat-factor zero alone does not clear a source. The direct detector counts near-rail samples at absolute amplitude at least 0.999 and marks a probable flat top when one channel has a repeated rail run of at least three samples and at least six near-rail samples overall. A nonzero flat factor without a direct plateau is recorded as a warning and does not reject the source by itself. Over-full-scale float samples without repeated rail plateaus can be attenuated; a probable clipped plateau is left unresolved because processing cannot restore it.

Tracks longer than 60 seconds are included in the sound-tree audit for format, whole-stream `astats`, EBU loudness, true peak, and checksums, but the report marks direct rail-run, onset, centroid, and loop-edge checks exempt for those audit-only tracks. Batch cannot master them.

## Validation and evidence

`py_compile` and all 12 unit tests passed. The test suite includes real read-only inspection of the installed vanilla infantry movement clip and verifies that an `astats` zero cannot override direct clipping evidence, while a nonzero `astats` factor alone is not treated as clipping.

The full audit in [sound_tree_audit.json](audio_evidence/sound_tree_audit.json) covered 311 audio files with zero analysis errors. Against the current baseline inventory SHA-256 `6b87475048580ee78e33ccf052d1f67be5002099b3c5db17092dfb1baece633d`, it found 209 unique mod `sound/` paths used by active unit consumers and 24 external installed-vanilla references; all 24 external files exist and match their baseline hashes, and no active mod sound path is missing. The 102 other files in `sound/` are outside this model-consumer inventory and remain audit-only. The report records 71 tracks over 60 seconds as long-form exemptions.

The consumer audit records 209 soundeffect cues: 173 have one sample; `prevent_random_repetition` is present on 156, absent on 43, and unavailable or ambiguous on 10. The duplicate audit found 54 cross-unit byte-identical groups with no family-pool declaration supplied to this run. These groups remain flagged for the parent to declare only where the shared sound identity is intentional; no fake takes were created and no sound definitions were edited.

The attribution map in [attribution_map.json](audio_evidence/attribution_map.json) maps 12 existing forest-giant and stone-cohort file rows. The remaining 197 active mod paths are marked `not_mapped_to_existing_attribution_manifest` in the report because no exact row was supplied for those paths; this is a mapping gap, not proof that no package provenance document exists. The tool preserves exact matched text and the attribution document SHA-256, and always records `derivative_license_verified = false` unless a parent performs that review.

The real-recording integration batch used `sound/012_africa/units/forest_giants/chaosx_forest_giants_attack.wav`. Its installed source was `pcm_f32le`, 44.1 kHz mono, 1.507075 seconds, SHA-256 `c1bf32450c72f8dc2b51688b1ae63bfd6e949f476e0f8ec6dc33e4e994906836`; the staged output is `docs/plans/unit_fix_2026-10/audio_evidence/staged/forest_giants/chaosx_forest_giants_attack_sfx/chaosx_forest_giants_attack_e4a6a3ac.mastered.wav`, `pcm_s16le`, 44.1 kHz mono, sample peak -3.00 dBFS, RMS -21.59 dBFS, integrated loudness -19.8 LUFS, true peak -3.0 dBTP, centroid 4,199.88 Hz, and SHA-256 `3c2248e6583eb5d0aacf392c8cf300f38b7914f3ffa0a01a3fe16169993771fb`. Direct decoded samples show no flat-top run; FFmpeg reported a nonzero flat factor of 4.436975, preserved as a warning. The matched `ATTRIBUTION.md` row is CC0, but it does not contain the installed preimage SHA, so the report explicitly leaves derivative-license verification false.

## Reference evidence and remaining parent work

The offline Sound modding wiki snapshot is `paradox_wiki/Sound modding - Hearts of Iron 4 Wiki.md`, SHA-256 `904c1909fcb8a6ac3d3f6bb5286eca216bb996513a3bc0788f12f96ab7cc6e4f`; lines 15-17 specify the general WAV/rate/bit-depth guidance, lines 42-85 describe soundeffect variants and `prevent_random_repetition`, and line 120 describes repetition prevention. Its generic 32-bit-float note differs from the inspected installed infantry file and the 3D pipeline runtime guidance, so the final runtime contract follows the measured installed sample and the project plan.

The installed vanilla precedent is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/sound.asset`, SHA-256 `263a6dfd6c53c4881e1133c403af0ae3ed68df40821b14ff7fd69cd66c48c2d9`, lines 2044-2045. Its `infantry_move_animation` wrapper is in `sound/soundeffects.asset`, SHA-256 `cb13be6f368723dd48be9d9544f7b7b50cfd228b850c88ef55600187ba65b01f`, lines 908-927, with ten takes and no `prevent_random_repetition` field in that block. The measured reference WAV is `sound/animations/infantry_move_animation_01.wav`, SHA-256 `48a81c96d743a4911b2e124e2af3fe15e91a5b797e0cc714e3c8c86853b4fe16`: signed 16-bit PCM, 44.1 kHz mono, peak -2.38 dBFS, RMS -22.65 dBFS, EBU -23.3 LUFS, true peak -2.4 dBTP, centroid 3,174.88 Hz, and no direct flat-top run. Its inspection report is [vanilla_infantry_move_01_coarseframes_inspection.json](audio_evidence/vanilla_infantry_move_01_coarseframes_inspection.json).

The local tool versions were Python 3.9.12 and FFmpeg/ffprobe `N-123778-g3b55818764-20260331`. No Meshy or Blender operation was needed, no paid call or download occurred, and no runtime WAV, sound definition, entity, or gameplay file was changed. The staged forest-giant derivative is evidence only. The parent should supply reviewed allowlist entries for files with resolved provenance, choose intentional family-pool declarations, carry the 197 unmapped attribution rows as unresolved until matched, and own the runtime CAS copy and sound-definition decisions.

Guidance applied: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`; no skill files were changed.
