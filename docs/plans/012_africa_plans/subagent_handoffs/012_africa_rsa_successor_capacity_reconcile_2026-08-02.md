# Event 012 RSA successor capacity reconciliation

Date: 2026-08-02.

Status: Implemented source repair; live-save acceptance remains open.

## Scope

RSA exile succession copies the suppressed host's surviving relationship arrays, then resets the successor's action, target, dossier, and project caps to opening values.

Without a post-copy reconciliation, a successor with enough cooperative members could keep undersized opening caps even though the canonical relationship registry had crossed the Charter and continental thresholds.

## Change

`common/scripted_effects/012_africa_rsa_effects.txt` now calls `africa_reconcile_relationship_counts_and_caps` after successor member generations and autonomy are rebuilt.

The shared helper derives all relationship counts from the copied arrays and expands action, selected-target, dossier, and living-core caps at the documented thresholds.

## Expected behavior

- A successor with fewer than the configured thresholds retains its opening caps.
- A successor with Charter- or continental-threshold cooperative members receives the same caps as an ordinary host transition.
- No relationship, integration, or target is invented; the helper only reconciles the copied successor roster.

## Validation boundary

Static source inspection confirmed the helper runs inside the exile-patron scope after both copied member and peace-exemption arrays are generation-stamped.

The bounded `hoi4_event_inspect` lint for `chaosx.nr12.1` returned status `ok` with no blocking diagnostics, while its workspace-wide helper analysis remained deferred by the adapter.

No Hearts of Iron IV executable or live save was launched, so threshold-crossing cap expansion remains open acceptance work.
