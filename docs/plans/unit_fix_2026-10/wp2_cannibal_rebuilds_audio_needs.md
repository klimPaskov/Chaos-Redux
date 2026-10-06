# WP2 Cannibal rebuilds (014) - Audio delivery and held-source needs

This package has 27 unique active mod sound paths: 24 are installed and 3 are held. Consumer counts are path-scoped; a shared pool path appears once per relevant package report.

## Installed file facts

The final install has 24 unique path(s) for this package, by file role: loop 4, shot 16, step 4. Each installed row maps to the authoritative install manifest and has an actual-workspace hash match. The global 135-file set is provenance-eligible and decodes as PCM signed 16-bit, 44.1 kHz mono.

The installed derivative SHA is the one listed in the install manifest; the before SHA matches the captured baseline. Mastering is file-level evidence only and does not establish soundeffect state, role, repetition, contact timing, or live-game suitability.

## Held active paths

This package has 3 held path(s): 1 have a blocking provenance row, 1 lack a final per-file provenance row, and 1 are marked provenance-eligible but are absent from the final install. All held bytes match the original baseline SHA-256.

### `sound/014_cannibalism/units/cannibal_feast_guard/cannibal_feast_guard_selection.wav`
Consumers: cannibal_feast_guard / cannibal_feast_guard_selection.wav.
Before/current SHA-256: `75d9ea2486fb570dfb30334d7e77654a2ba6cb43a74afea99503bc706d647605` / `75d9ea2486fb570dfb30334d7e77654a2ba6cb43a74afea99503bc706d647605`; unchanged: `true`; bytes: 88,316.
Review status: no exact per-file entry exists in `provenance_review.json`; license/source-member provenance is not asserted.
Needed: inspect the existing package archive, identify the actual recorded member and license, and link original-source SHA, source URL/creator, and derived runtime SHA. No substitute recording is proposed here.

### `sound/014_cannibalism/units/cannibal_feast_guard/cannibal_feast_guard_training.wav`
Consumers: cannibal_feast_guard / cannibal_feast_guard_training_sfx / cannibal_feast_guard_training_source, cannibal_feast_guard / cannibal_feast_guard_training.wav.
Before/current SHA-256: `efbe3b475e633a9f11d6c3bc97ba0432407d411efa7e36071fb07fedfdd4b839` / `efbe3b475e633a9f11d6c3bc97ba0432407d411efa7e36071fb07fedfdd4b839`; unchanged: `true`; bytes: 16,656.
Review status: `blocked`; unit `cannibal_feast_guard`; role `shot`; master batch `staged`; original archive state `unavailable_current_source_chain_not_proven`.
Recorded source: title absent; creator not recorded; license not recorded; URL not recorded; original SHA `not recorded`; original path `not recorded`.
Held reason: No source member/license is assigned to this runtime training cue in the per-file row or Event 014 role mapping.
Existing references: `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/manifest.json:348` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: resolve the stated source/member/license/SHA contradiction with a source-to-current-runtime hash link, or retain the original held bytes and document the decision. Do not promote a staged output on filename alone.

### `sound/014_cannibalism/units/cannibal_island_reavers/cannibal_island_reavers_death.wav`
Consumers: cannibal_island_reavers / cannibal_island_reavers_death_sfx / cannibal_island_reavers_death_source, cannibal_island_reavers / cannibal_island_reavers_death.wav.
Before/current SHA-256: `7a4a4356a5cc9bb160d32516add22d58149f08e4556dafd181684c0489141aab` / `7a4a4356a5cc9bb160d32516add22d58149f08e4556dafd181684c0489141aab`; unchanged: `true`; bytes: 194,118.
Review status: `eligible`; unit `cannibal_island_reavers`; role `shot`; master batch `unresolved`; original archive state `archival_gap`.
Recorded source: Male pain grunts; creator stilgar; uploader Fae; license Public domain; URL https://commons.wikimedia.org/wiki/File:Male_pain_grunts.ogg; original SHA `not recorded`; original path `not recorded`.
Existing references: `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/audio/sound_design_handoff.md:16` (existing per-runtime row; not standalone license proof); `docs/plans/unit_fix_2026-10/audio_evidence/allowlist.json:1` (current path/SHA index only); `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json:1` (processing status and output SHA only).
No separate candidate recording is recorded on this provenance row.
Needed: owner decision on this eligible mapping because the active runtime path is not in the final install list; do not infer that a candidate should replace the held file.

## Recording need: island reavers death

The retained death file has probable clipped flat tops (`master_batch.json`: `source_has_probable_clipped_flat_tops`).
Its licensed mapping is eligible, but gain changes cannot restore the clipped signal.
First check the already archived public-domain Male pain grunts recording by stilgar/uploader Fae for a clean distinct take, with a target length about 2.2 seconds matching the recorded excerpt brief.
The existing candidate page is https://commons.wikimedia.org/wiki/File:Male_pain_grunts.ogg; bind the exact recorded member and original/derived hashes before production.
If that archive has no suitable take, the orchestrator must source a recorded male death grunt/body fall under public-domain, CC0, or an attributable CC BY/CC BY-SA license after obtaining sourcing permission.
The current cue stays in place until its package installs an accepted replacement.

## Recording requirements from the user-authored plan

The following brief is transcribed from section 2 of `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md` (SHA-256 `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`). It records the requested role, timing/length, and source-license choices. It is a production brief, not approval for an existing candidate or runtime file.

- `cannibal_feast_cohort`: from the batch: swish lengthened to 0.3-0.5 s at -6 dBFS, impact -3 dBFS with true-peak limiting, distinct movement/selection/training takes (currently byte copies of march and feast_guard files), footsteps at -18 dB peak.
- `cannibal_feast_guard`: from the batch: death re-derived at -3 dBFS with denoise, longer whoosh, -3 dBFS impact, a distinct training take, two footsteps; per-tag voices in `014_cannibalism_voices.asset` with leading silence trimmed.
- `cannibal_island_reavers`: from the batch: death re-derived at -3 dBFS without limiting and denoised (the worst-clipped file in the family); training replaced with a wood/spear thrust or exertion grunt at -3 dBFS from the CC0 packs (the sword clash is the wrong identity); impact limited to -3 dBFS; idle/selection silences trimmed; footsteps at -18 dB peak.
- `cannibal_scavenger_warband`: from the batch: new death take (not the march's), 0.3-0.5 s whoosh, two footsteps, a training exertion grunt from the same CC0 grunt pack; events retimed to the re-authored swing (swish at the wind-up, impact at the strike frame).

No recording source was downloaded or created for this documentation update. Per-file source binding and licensing gaps listed above remain the audio install gate.
## Remaining runtime checks

The package definitions and actions remain unchanged. Final entity lint records current unresolved event-sample overlaps, cycle/state mismatches, missing contact evidence, and measured event/contact offsets as shown in the main package report. Successful PCM mastering does not clear those findings.

Source-tree audit reports 209 active cues, 173 single-sample cues, 52 duplicate groups, and 52 undeclared cross-unit duplicate groups. Source sharing, state/take choice, event timing, and player-facing role fit remain unaccepted.

No source downloads or new recordings were performed. Source URLs and license families above are copied only from existing per-file provenance/candidate records; an unapproved candidate is not treated as a license or runtime match.

## Evidence source hashes
- `docs/plans/unit_fix_2026-10/audio_evidence/recovery_batch.json` - SHA-256 `148ffb5a39ce96a1ee6cd532b72dc5426ff5d3abbeccb4afe5a7eba734e533d8`.
- User-authored recording brief `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md` - SHA-256 `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`.

- `docs/plans/unit_fix_2026-10/audio_evidence/install/manifest.json` - SHA-256 `72054623f8c388f79f7a8a0c71881025add5efe505c5ae4317db1e3c5ba1ecb5`
- `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json` - SHA-256 `ec787f36a48db089ef306fb1802736361b0e8d1574de6bedc95577cea61d8e77`
- `docs/plans/unit_fix_2026-10/audio_evidence/provenance_review.json` - SHA-256 `bd4e36c9edbba24c926a2306efb4190541c3f6b90290e9f9a3a0c6111f74b577`
- `docs/plans/unit_fix_2026-10/audio_evidence/recovery2_evidence/recovery2_batch.json` - SHA-256 `e277faf5be6a49d26fd81bf305b0b873ada14e0ae3e36bb11e9f95ff78cf360a`
- `docs/plans/unit_fix_2026-10/audio_evidence/sound_tree_after.json` - SHA-256 `532aae613a6eaab88e21067aa75222fb8a8da8a77ed9d1792363b7cb8d7bb275`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/baseline_inventory.json` - SHA-256 `6b87475048580ee78e33ccf052d1f67be5002099b3c5db17092dfb1baece633d`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/contact_peak_evidence.json` - SHA-256 `b6193d744c0b10f3d4c6bf464799934010ab07f6ed9991d04ac89bce68a96af8`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/entity_lint_after.json` - SHA-256 `a388fae714faf098968191b752e99193a82fdd37a28daf6bf6b6ca372dfe42bc`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/final_inventory.json` - SHA-256 `d1f72e1456c6a09cdce948df00590534414b91518c8241ec36ca3e11ccb6bb6b`
