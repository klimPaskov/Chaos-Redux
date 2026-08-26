# Event 006 FORM-39 formable-registry merge — 2026-08-26

## Scope

This bounded source-layout pass consolidates the two FORM-39 parser files into the existing Event 006 formable-family registries. It does not change the FORM-39 contract, readiness gate, admission boundary, decision ownership, or runtime behavior.

## Files changed

- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt` now contains the exact body of `006_independence_wave_form39_triggers.txt` under a FORM-39 source marker.
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` now contains the exact body of `006_independence_wave_form39_effects.txt` under a FORM-39 source marker.
- `docs/events/006_independence_wave/form39_melanesian_federation.md` points to the canonical trigger/effect registries and the already-consolidated formable decision receiver.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` record the source-layout amendment.
- The standalone `common/scripted_triggers/006_independence_wave_form39_triggers.txt` and `common/scripted_effects/006_independence_wave_form39_effects.txt` parser files are removed.

## Preservation checks

- The original 17 FORM-39 trigger definitions and 20 effect definitions are copied without identifier or executable-body changes after LF normalization.
- The `FORM39_FIJ_ANCHOR`, `FORM39_PNG_ANCHOR`, and `FORM39_WPG_ANCHOR` constants remain file-scoped in the canonical trigger/effect receivers and have no name collision with existing registry constants.
- The source tree contains no current reference to the removed FORM-39 trigger/effect filenames.
- FORM-39 remains fail-closed behind its existing FIJ/PNG/WPG, MFX identity, flag, consent, and package research gates.

## Validation and limits

The parent should run the maintained Event 006 allocator and parser-oriented checks after reviewing the diff. This is source-layout evidence only. No Hearts of Iron IV executable, save, live FORM-39 congress, or runtime release was launched or claimed.

## Simplifications, omissions, and blockers

None introduced by this merge. Existing FORM-39 asset, package-research, identity, and runtime-evidence holds remain unchanged.
