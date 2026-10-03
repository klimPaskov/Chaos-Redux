# Feast Cohort current manifest recovery

Disposition: implemented for the new current manifest link and selected-byte receipt reconciliation; package acceptance remains incomplete.
Acceptance basis: the user-authorized Event 014 continuation and the existing selected `11014` runtime handoff, with no production reopening or runtime change.

The missing `manifest.json` link resolves to a new reconciled current record, not a claimed recovery of the original JSON.
The previous markdown is preserved in `docs/plans/014_cannibalism_plans/evidence/2026-10-03_model_manifest_recovery/historical_cannibal_feast_cohort_manifest_2026-10-03.md`.
The parent reviewed the initial worker draft, normalized its source path relative to the actual package, checked the retained model-ready image hash, and linked all eight selected export/reimport records.

## Verified facts

- The model-ready `refs/original/meshy_input.png` exists and matches the recorded `F2E2B8705068932E771FC04D140E70D69ECBBF5DBAD3E6CDA8C86494A5F9AC21` hash.
- The selected `exports/cannibal_feast_cohort_11014.mesh` and all eight `_11014.anim` files match installed runtime bytes.
- Each selected animation has its actual export and reimport report linked by source path, role, hash, frame count and FPS in `cohort_selected_action_records.json`.
- The selected reimport records refer to the `11014` mesh and show the retained 24-bone rig, geometry and sampled action bounds.
- Installed material maps and state audio cues retain the hashes measured by the parent's seven-package runtime audit.
- The existing source selection and provider task IDs are recorded from the input/job/handoff receipts with their evidence limits.

The earlier seven-action local-authoring report has a different death frame count from the selected 55-frame runtime action.
It is a historical candidate record, not current semantic acceptance of the selected action set.
Selected exports and reimports establish file identity; they do not establish missing provider input/response lineage or complete role/contact acceptance.

## Unresolved evidence

The selected raw Um'Gra Youngblood source JPEG with recorded SHA-256 `80D34425CCC5F21E63FA378F6129DE4ED502020F2E59F8A09C7D69883D37AC9C` remains absent.
A bounded local image-hash search found no matching bytes; browsing its recorded source page returned a verification interstitial and did not recover the source.
No alternative image was adopted.
The exact native preparation prompt and selected provider response linkage remain absent.
The three source DDS files named by the texture-conversion report are absent, and that report contains no final map hashes; their copy relation to the installed maps remains unresolved.
The source-audio record and installed cue mapping preserve their known hashes and unmapped extra derivative without inventing a license or new sound.
The retained mesh topology report records open boundaries; no topology or motion acceptance is inferred from this metadata pass.
Live visual/model/audio/counter acceptance remains user-owned and incomplete.

## Changed files and limits

- `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/manifest.json` and `manifest.md`: new current metadata records with known selected assets and explicit unresolved fields.
- `docs/plans/014_cannibalism_plans/evidence/2026-10-03_model_manifest_recovery/cohort_selected_action_records.json`: selected action export/reimport identities.
- This handoff.

No model, texture, animation, audio, gameplay, GFX, GUI, job intake or existing report was modified.
No provider, Blender or HOI4 operation was performed.
No simplification or fallback was introduced, and this metadata repair does not establish full Event 014 completion.
Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-events` and `chaos-redux-shared-git-commit`.
