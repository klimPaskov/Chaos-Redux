# Event 006 icon audit hash reconciliation

Date: 2026-09-05. This narrow evidence repair reconciles the Event 006 icon build report with the hydrated achievement DDS files.

## Files changed

- `docs/assets/006_independence_wave/_tooling/icon_build_report.json`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_icon_audit_hash_reconciliation_2026-09-05.md`

## Repair

The report already contained the current hydrated hashes in the 45 achievement family `runtime_sha256` fields, but the parallel `dds_audit` rows still held the prior object hashes. Each of those 45 `dds_audit.sha256` values now matches the SHA-256 of its installed `gfx/achievements/chaosx_006_*.dds` file.

No image bytes, dimensions, alpha treatment, filenames, sprite definitions, gameplay consumers, or achievement definitions changed. The repair closes a metadata/evidence mismatch only.

## Validation

The report parser reads 78 DDS audit rows with zero missing files and zero hash mismatches. The Event 006 allocator, strict flag, country API, FORM-16, SCN-008, and Statehood Ledger GUI semantic validators remain green. No live Hearts of Iron IV, save/load, or runtime-completion claim is made.

## Disposition

Implemented. The broader visual audit remains `HOLD/PARTIAL` because grounded portrait rights and identity, formable emblem coverage, flag provenance, GUI dynamic-state proof, and super-event 23 audio/firing reachability remain open.
