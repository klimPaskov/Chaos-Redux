# Event 006 grounded portrait manifest reconciliation — 2026-07-29

This is a documentation-only handoff for the grounded CHU portrait source ledgers. It does not claim Event 006 completion and it does not authorize character, DDS, `.gfx`, or gameplay wiring.

## Files changed

- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/manifest.md`
- This handoff.

## Source-of-truth map

| Surface | Current disposition |
| --- | --- |
| Mediterranean/Volga/Assyria ledger row 12 | Historical museum-only Musa Dzhalil evidence; explicitly `superseded` for the former CHU river-security mapping. |
| Companion retry ledger Musa candidate | Current `CHU_independence_wave_bolgar_civic_presidium` candidate from `source_masters/volga/chu_musa_dzhalil_commons_1930s.jpg`; independent visual audit PASS, source-rights review open. Master SHA-256: `c7e92f3b1e939cfcfcc67a06ab455ab101b8f04509aab75a245d7da97a74869f`. |
| Companion retry ledger Togan candidate | Current `CHU_independence_wave_river_security_directorate` candidate from `source_masters/volga/chu_validi_bashkortostan.jpg`; independent visual audit PASS, user rights/provenance and Bashkir-to-CHU route-role review open. Master SHA-256: `23d3403f15b766107458361891ff3e010b5cfde3f85ff80c0efaf204b4bc6026`. |
| Source-locked repaint and audit evidence | Retained under `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/` and the existing visual-audit handoff; evidence only. |

## Reconciliation and dispositions

| Item | Disposition |
| --- | --- |
| Old Musa river-security mapping | Superseded in place and retained as historical evidence; no file deletion. |
| Musa 1930s visual result | Visual gates are complete and PASS; source/rights gate remains `needs_user_review`. |
| Togan visual result | Visual gates are complete and PASS; source/rights and Bashkir-to-CHU role gates remain `needs_user_review` (the retry ledger retains its legacy `needs_review` label). |
| DDS/GFX/runtime work | Not started and remains parent-owned. |

## Contradictions and remaining risks

The stale wording that treated both new candidates as awaiting a visual audit was replaced with completed visual-audit language and explicit open source/role gates. The remaining risks are unresolved Wikimedia Commons/museum rights and author/provenance review for both sources, plus an explicit parent decision on whether a Bashkir historical figure fits the fictional CHU river-security role. No prompt or gameplay documentation was changed; stale prompt review remains out of scope.

## Parent follow-up

Resolve the Musa source-rights disposition, resolve Togan source-rights and Bashkir-to-CHU role approval, then decide whether to run a fresh processing/DDS pass. Until those decisions are recorded, keep both candidates unwired and treat this handoff as evidence only.

## Meaningful validation

Targeted `rg` checks confirmed the old Musa row is labeled `superseded`, the med_eurasia note records independent visual PASS with open gates, and the stale phrases `until the independent visual audit is complete` and `until the independent visual audit passes` are absent from the two reconciled manifests. No gameplay, character, `.gfx`, DDS, or unrelated documentation path was edited.
