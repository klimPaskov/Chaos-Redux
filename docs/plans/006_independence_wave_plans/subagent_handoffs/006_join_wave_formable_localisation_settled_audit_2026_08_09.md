# Event 006 join-wave and grouped formable localisation audit

Date: 2026-08-09

Owner: `/root/join_formable_loc_settled`

## Result

**PASS.** The settled filesystem has no remaining localisation or documentation defect in this audit scope.

The Join the Independence Wave report, Event Details text, event-catalog Details field, and join documentation now state the exact public eligibility threshold: the country has lost at least half its former states, has lost at least two states in total, and retains only states belonging to one prepared homeland.

The 20-day report timeout remains fail-safe because the first option in `chaosx.nr6.36` is the refusal path. Refusal and expiry both route through hidden Event `chaosx.nr6.38`, clear the matching plan, record the declined history payload, and apply the dynamic cooldown. Acceptance remains the second option and routes through hidden Event `chaosx.nr6.37`. No gameplay behavior was changed.

The grouped state-puzzle surface has all fourteen summary keys and all fifty state-hover tooltip keys referenced by the generated GUI. The summaries retain dynamic qualifying counts and family-specific denominators. All seventeen attached decision categories point to `independence_wave_formable_state_puzzle_scripted_gui` according to the existing category attachment audit.

## Changed files and keys

- `localisation/english/006_independence_wave_join_l_english.yml`
  - `chaosx.nr6.36.d`
- `localisation/english/chaosx_gui_l_english.yml`
  - `chaosx.events_log.window.event_details.independence_wave`
- `docs/events/006_independence_wave/join_wave.md`
  - removed the em dash from the heading and split the semicolon sentence
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
  - `Events!C7`
- `docs/spreadsheets/chaos_redux_events_catalog.csv`
  - regenerated from the workbook
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`
  - regenerated unchanged from the workbook
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`
  - regenerated unchanged from the workbook

No scripted localisation, variable formatter, event target, or gameplay token was added, removed, or renamed.

## Before and after

### Vagueness

Before, the join report said only that the country's borders had contracted. After, it states the public loss threshold and exact-homeland condition.

### Bloat and obvious explanation

The join report no longer repeats that the country can join the independence wave after the title and threshold already establish that premise. The choice remains concrete: dissolve the old state and continue as the prepared country.

### Repetition

The Event Details text and workbook Details cell now use the same join eligibility wording. The existing rival-bloc dynamic additions remain appended only in Event Details.

### Overcomplication

No new clauses or implementation terminology were introduced. The event report uses two direct conditions and one visible consequence.

### Style-rule repair

The scoped join document no longer contains an em dash or sentence semicolon. No internal `FORM-*` identifier, task label, prompt fragment, tuning note, or implementation-history wording appears in the inspected player-facing localisation, Event Details prose, or catalog Details field.

## Audit lists

- Missing keys: none among the 12 join/report/history keys, 14 grouped family summary keys, or 50 state-hover tooltip keys.
- Duplicate keys: none among those inspected keys across English localisation.
- Scripted localisation issues: none in the four join-history payload branches or the grouped count/status functions.
- Dynamic text opportunities: completed for the join target, refusal cooldown, history primary/secondary actors, state owner/controller/core status, per-state formation status, qualifying numerator, and family denominator.
- Cross-surface mismatches: the join eligibility wording was corrected across the report, Event Details, workbook, CSV, and documentation. No remaining mismatch was found in those fields.
- Encoding concerns: none. The three inspected localisation dependencies use UTF-8 with BOM.
- Sourced quotations: none occur on the inspected surfaces.

## Resolved follow-up

The shared generator now emits `Formation status` instead of the over-narrow `Required control` label. The regenerated runtime contains 442 updated hover keys. All 50 Event 006 state-puzzle tooltips use `Formation status`, retain their family-specific dynamic qualification function, and contain no remaining `Required control` label. The generated localisation remains UTF-8 with BOM.

## Validation evidence

- `hoi4.event_inspect` traced `chaosx.nr6.36` downstream. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1659e24a9788cb51deda24deba99e14e02e142f290f8ad32a4dc52c538cba7a/65898351a854580bd9670286064cdab3548514aa12561df99f63375441bb10d8/event-trace-550da12aba6a.json`.
- `hoi4.event_render` produced the report-option view. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2b815951b476a2b65f40523d5b6d289a972f5ac15bf94224d3f411366e964a2/36e28eaad8495ff3a21313ab50c910cc7f23a371904f2ff635e26e29b87da349/event-options-550da12aba6a-manifest.json`.
- `hoi4.gui_inspect` inspected `chaosx_independence_wave_formable_state_puzzle_window`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7da9bad9cfd0654d776c2c94beacfcd5c1da7d60e580a461ca7786a34714f27/3dab52f07ec3fa93ba39a803cb71fa6e2f6072796e5e5163bf933fb1092744e3/gui-inspect.fc2200e9c790f7c3.json`.
- `hoi4.gui_render` rendered normal, long-text, and missing-localisation review states at 1920x1080 and 1366x768. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5cf4a0e6908e754ba9e1bae29b05ae013092399118afcfe42cedf62d2833fe9/9782bfa7dee9f2d441108debfc2780c6e180f60f3c20bf7aeda57b839e2782e0/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.
- The GUI MCP route reports workspace-wide index collisions, truncated global diagnostics, unresolved scripted contexts, and aggregate overlap from mutually exclusive family overlays being activated together. It does not provide clean family-by-family overflow proof. Source dimensions show every summary remains the existing short generic string inside a 440-pixel text box; live family-specific overflow remains user-owned.
- The catalog exporter completed successfully with 183 Events rows, 14 Clusters rows, and 12 Scenarios rows. Events CSV SHA-256: `0c309f8bea4b45136b38d99c52eecaadfb197b493e49ea00142a787ad7fbc0f8`.

## Skipped meaningful validation

No live in-game text rendering was performed, as required by repository policy. The MCP GUI scenario cannot isolate one activation helper or prove runtime mutual exclusion, so family-by-family tooltip placement and live font overflow remain unresolved rather than treated as source-equivalent evidence.

## Simplifications and blockers

No gameplay simplification or fallback was introduced. No localisation, documentation, encoding, source-generation, or cross-surface wording blocker remains in this audit scope. No plan handoff was needed.
