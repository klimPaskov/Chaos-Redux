# Event 006 repair-artifact cleanup

Date: 2026-08-30

## Status

Implemented as a parser-surface cleanup only. No gameplay, localization, asset, admission, probability, or runtime definition changed.

## Change

Removed the stale tracked snapshot `common/scripted_triggers/006_independence_wave_triggers.repair.tmp`.

The snapshot used the non-parser `.tmp` extension and had no source caller. Its top-level trigger identifier set matched the 149 identifiers in `common/scripted_triggers/006_independence_wave_triggers.txt`, while the canonical `.txt` contains the later candidate-registry, absent-release, and dormant-safety repairs. Keeping both files only duplicated a pre-repair source snapshot in the mod tree.

The canonical trigger registry remains the sole Event 006 trigger source. Per-country definition files remain separate because `common/country_tags/006_independence_wave_countries.txt` maps each tag to its own country-definition path; no country-definition merge was attempted.

## Evidence

- Before cleanup, both trigger snapshots exposed 149 unique top-level identifiers with no identifier-set difference.
- The removed file was not a `.txt` parser input and had no non-document references.
- The canonical `.txt` was not edited.
- No live HOI4, save/load, or MCP engine completion claim is made.

## Follow-up

The current source-of-truth map and resume packet record the removal. The older 2026-08-29 completion snapshot may retain its warning as historical context; it is not current source authority.
