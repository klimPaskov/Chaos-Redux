# Unit audio audit and mastering CLI

Run commands from the mod root with the installed Python 3.9+ and FFmpeg/ffprobe executables on `PATH`.

`inspect` is read-only and measures the source codec, rate, channels, bit depth, sample peak, RMS, DC offset, lead silence, EBU R128 loudness/true peak, FFmpeg `astats` flat factor, direct near-rail sample runs, and active-window spectral centroid.

`audit-tree` measures every supported audio file under the supplied `sound/` tree and reports runtime inventory hashes, byte-identical files, declared family pools, one-sample cues, `prevent_random_repetition` coverage, selection/order `additional_sound_files`, and optional attribution rows. It uses four read-only FFmpeg workers by default; pass `--workers` to change that count.

`batch` stages outputs only for exact entries in a schema-1 allowlist. It verifies the current source SHA-256 against the allowlist and, when supplied, against `pipeline_evidence/baseline_inventory.json`; it requires an existing attribution manifest with a matching row; it rejects missing or clipped sources, non-subsonic sources at or below 200 Hz centroid, super-event sources, and sources longer than 60 seconds. Default staged filenames preserve the source basename and append an eight-character hash of its relative source path, so multiple takes in one cue cannot collide. An explicit `output` value in the allowlist overrides that name. The output directory and all reports must remain outside the active `sound/` tree. Inputs are immutable and existing audio outputs are never overwritten.

## Read-only tree audit

```powershell
python .tools/3d_pipeline/audio/master.py audit-tree `
  --root sound `
  --inventory docs/plans/unit_fix_2026-10/pipeline_evidence/baseline_inventory.json `
  --family-pools docs/plans/unit_fix_2026-10/audio_evidence/family_pools.json `
  --attribution-map docs/plans/unit_fix_2026-10/audio_evidence/attribution_map.json `
  --output docs/plans/unit_fix_2026-10/audio_evidence/sound_tree_audit.json
```

`--family-pools` is optional. A declaration has an exact id, SHA-256, path list, member unit list, and rationale. It documents an accepted shared pool; it does not create unique variants or edit a sound definition.

The attribution map is optional and has this shape:

```json
{
  "entries": {
    "sound/custom_unit/custom_step.wav": {
      "manifest_path": "docs/assets/system/models_3d/custom_unit/audio/ATTRIBUTION.md",
      "source_sha256": "<recorded original-source SHA-256>",
      "match": "custom_step.wav"
    }
  }
}
```

## Explicit allowlist batch

Each entry names the exact installed custom-unit WAV, consumer, role, expected installed-byte hash, and current attribution document. `source_row` is copied verbatim when given; otherwise `match` selects existing lines that contain the exact row token. The manifest file itself and its SHA-256 are retained in every item report. The tool states that the derivative license was not independently reassessed.

```json
{
  "schema": 1,
  "inventory_path": "docs/plans/unit_fix_2026-10/pipeline_evidence/baseline_inventory.json",
  "entries": [
    {
      "source": "sound/custom_unit/custom_step.wav",
      "sha256": "<installed baseline WAV SHA-256>",
      "unit_id": "custom_unit",
      "soundeffect": "custom_unit_step",
      "role": "step",
      "subsonic": false,
      "attribution": {
        "manifest_path": "docs/assets/system/models_3d/custom_unit/audio/ATTRIBUTION.md",
        "source_sha256": "<recorded original-source SHA-256>",
        "match": "custom_step.wav"
      }
    }
  ],
  "family_pools": []
}
```

```powershell
python .tools/3d_pipeline/audio/master.py batch `
  --manifest docs/plans/unit_fix_2026-10/audio_evidence/master_allowlist.json `
  --source-root . `
  --output-root docs/plans/unit_fix_2026-10/audio_evidence/staged `
  --report docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json
```

Role targets are one-shots at -3 dBFS sample peak (±0.8 dB) with RMS near -18 dBFS (±4 dB), steps at -6 dBFS sample peak (±0.8 dB) with EBU loudness near -23 LUFS (±5 LU when the clip is at least 0.4 s), and loops at -20 LUFS integrated (±1 LU) with true peak at or below -1 dBTP. All outputs use `pcm_s16le`, 44.1 kHz, mono. The common recipe applies a 30 Hz high-pass, trims measured lead silence while keeping 10 ms pre-roll, an 8 ms fade-in, and a 50 ms fade-out. A short step whose EBU loudness is gated or unavailable is reported as unavailable; its peak remains the measured level target.

After normalization, the batch measures lead silence again. A remaining lead longer than 20 ms gets up to two measured post-master trims that retain 10 ms pre-roll and reapply the 8 ms fade-in; each input/output hash and measurement is recorded, and the normal role gates run again afterward.

For a looping cue whose inner head/tail RMS still differs by over 3 dB, the batch tries bounded equal-power crossfades formed from the actual recording's tail and head samples. It records each overlap attempt and its measured result, then reapplies endpoint fades, normalizes the crossfaded recording, and checks final loudness, true peak, lead, and loop-edge RMS. If no recorded-sample overlap passes or the final output still misses a gate, the cue remains unresolved and the batch leaves no staged WAV for it. Loop loudness can receive up to three measured gain corrections when true-peak headroom permits; an incompatible -20 LUFS/-1 dBTP pair is reported unresolved.

Clipping is checked directly on decoded samples as repeated near-rail plateaus as well as against `astats`; an `astats` flat-factor zero alone never clears the source. A source with probable clipping or an invalid spectral band receives no derivative. Over-full-scale floating-point samples alone are recorded but do not count as irrecoverable clipping because they can be attenuated without reconstructing lost peaks.

Tracks longer than 60 seconds stay in the tree audit for codec, whole-stream `astats`, EBU loudness, true peak, and hash evidence. The report marks direct rail-run, lead-silence, centroid, and loop-edge checks as exempt for these audit-only tracks; an `astats` flat-factor zero does not stand in for a direct rail scan.
