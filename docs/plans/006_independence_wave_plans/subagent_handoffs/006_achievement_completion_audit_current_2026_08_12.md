# Event 006 achievement completion audit (2026-08-12)

## Disposition

The Event 006 achievement surface is a static source PASS for the accepted sixteen-row matrix.

This receipt does not claim live unlock behavior, save/load persistence, focused GUI presentation, or whole-event completion.

The remaining reachability and runtime boundary is carried by the current whole-event HOLD / PARTIAL authority, including the unadmitted signature packages and the unavailable current MCP artifact manifest.

The current Event 006 authority at the time of this receipt was 30 content-attested packages, 27 compatible reservation groups, 163 unattested selectable rows, and 38 runtime adapters; the 2026-08-13 IW-044 promotion supersedes those counts with 31/28/162/39. This achievement receipt does not alter those gates.

## Matrix and source coverage

The authoritative matrix is `docs/specs/006_independence_wave_specs/matrices/006_achievement_matrix.csv`.

All 16 matrix IDs are defined exactly once in `common/achievements/chaos_redux_achievements.txt`.

All 16 IDs bind their `happened` clause to one corresponding final proof trigger in `common/scripted_triggers/006_independence_wave_achievement_triggers.txt`.

All 16 IDs have a matching English `NAME`, `DESC`, and dynamic completion tooltip in `localisation/english/006_independence_wave_achievements_l_english.yml`, with the file retaining the required UTF-8 BOM.

The four hidden rows are `chaosx_006_volga_bulgaria`, `chaosx_006_assyria_survives`, `chaosx_006_radical_bloc`, and `chaosx_006_every_flag_survival`; the remaining twelve rows are visible.

The proof-trigger source preserves the shared sovereign gate and the row-specific origin, host, league, formable, route, scenario, patron, arbitration, and remnant disqualifiers described by the matrix.

## Icon ladder coverage

Each of the 16 IDs has all three engine filename states under `gfx/achievements/`: the complete texture, `_grey`, and `_not_eligible`.

The resulting 48 DDS files all carry valid DDS headers, are 64×64 pixels, and have the same 16,512-byte payload size used by the installed Event 006 achievement family.

The achievement definitions intentionally rely on the engine's ID-based `gfx/achievements/<achievement_id>.dds` lookup; no separate Event 006 sprite alias is required for these definitions.

## Runtime and reachability limits

Current static source review does not prove that every completion flag or date variable can be written in a live campaign, nor that the hidden signature rows can be reached while their carrier packages remain fail-closed.

The current `hoi4` achievement-adjacent event/focus/probability inspection path is blocked before source scanning by `ARTIFACT_MANIFEST_INVALID` / `Artifact provenance manifest is invalid` for workspace `mod_chaos_redux_ea3b2d67c2c0`.

No current MCP artifact, live unlock, GUI click-path, save/load, or balance claim is made from this audit.

## Validation record

The matrix-to-source check found 16/16 definitions, 16/16 final proof triggers, 16/16 localisation triplets, and 16/16 icon triplets.

The existing static Event 006 allocator, scenario, flag, GUI-matrix, and protected-tag audits remain the current shared-system receipts; this audit made no gameplay or asset edits.
