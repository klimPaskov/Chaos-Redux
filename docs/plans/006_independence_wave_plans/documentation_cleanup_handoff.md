# Event 006 documentation cleanup handoff

> **Historical/superseded routing notice (2026-07-28):** This CHU/Galimzhan cleanup handoff records its at-time v30 and 51-master scope. Use `006_source_of_truth_map.md`, `006_independence_wave_resume_packet.md`, and `subagent_handoffs/006_event_completion_audit_v31_2026_07_28.md` for current Event 006 counts and authority.

Date: 2026-07-28.

Scope: reconcile Event 006 documentation after parent promotion of the independently audited CHU Galimzhan Ibrahimov v2 country-leader DDS. Gameplay, localisation, GFX, spreadsheet, and runtime source files were outside this cleanup.

## Current source-of-truth map

| Surface | Current authority | Disposition |
| --- | --- | --- |
| Accepted design | `docs/specs/006_independence_wave_specs/` | Accepted design unchanged. |
| Whole-event status | `subagent_handoffs/006_event_completion_audit_v30_2026_07_28.md` | **HOLD / PARTIAL**. v30 supersedes v23 and v28 for whole-event disposition. |
| Current routing | `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` | Reconciled to the 51-master flat shelf and Galimzhan v2 promotion. |
| Public event documentation | `docs/events/006_independence_wave.md` | Reconciled to v30, 51 flat masters, no normalized shelf PNGs, no advisor derivatives, and the promoted DDS hash. |
| CHU/ASY portrait ledger | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/manifest.md` and `gfx_handoff.md` | Galimzhan v2 is `runtime_promoted`. The other five rows remain source-only, blocked, or needs-user-review. |
| Galimzhan promotion | `subagent_handoffs/006_galimzhan_portrait_v2_runtime_promotion_2026_07_28.md` | One existing CHU consumer was promoted. CHU remains outside runtime content attestation. |
| Portrait shelf | `docs/assets/006_independence_wave/portraits_generated_png/README.md`, `MANIFEST.md`, and `PRE_RESIZE_MANIFEST.md` | Exactly 51 original-size RGB masters, one flat directory, no normalized 156x210 PNGs, no advisor or small/dossier derivatives. |

## Plan and handoff dispositions

| Document or tranche | Disposition | Reason or boundary |
| --- | --- | --- |
| Galimzhan v2 independent audit and runtime promotion | Promoted for one existing consumer | Visual and provenance gates passed. Final DDS SHA-256 is `977e0f8d359930f75e01e380a36893ef6a8f25a5b1ce5bbd8cc3c2f3abf6b5f5`. This is not CHU package admission. |
| IW-043/IW-058 source-research handoff | Historical snapshot with current promotion amendment | Its initial no-DDS language now applies only to the pre-promotion state. Five other rows retain their source gates. |
| Portrait shelf flattening handoff | Historical and superseded for count | The former 49-master layout is retained as traceability. Current shelf is 51 flat masters. |
| Portrait shelf completeness re-audit | Historical and superseded for count | The former 49-master and 83-normalized count is not current. No files were deleted by this cleanup. |
| Galimzhan v1 independent audit | Superseded evidence | v1 remains provenance and visual traceability. v2 is the approved promotion candidate. |
| Event 006 v23 completion audit | Historical whole-event evidence | v30 is current whole-event authority. v23 bounded findings remain useful only where carried forward by v30. |
| Other CHU/ASY route portraits | Queued or blocked | Shamil Usmanov is blocked by source resolution. Velidi Togan needs role and rights review. The three ASY rows retain their documented blocked or legacy-continuity decisions. |

## Contradictions reconciled

- `docs/events/006_independence_wave.md` described a 49-master shelf and v23 as current whole-event authority. It now records the 51-master flat shelf, v30 as current authority, v23 as historical, and the parent-promoted DDS hash.
- `006_source_of_truth_map.md` had a stale final portrait-shelf addendum saying the v2 DDS promotion had not occurred. It now records the promoted existing CHU consumer, hash, no normalized shelf PNGs, and no advisor or small/dossier derivatives.
- `006_source_of_truth_map.md` described the static visual row as candidate-only and called v23 the whole-event authority. Both statements now distinguish the parent-promoted Galimzhan consumer from the still-held CHU/ASY package and identify v30 as current authority.
- `006_independence_wave_resume_packet.md` described Galimzhan as a reviewed candidate without a DDS in one continuation bullet. That bullet now records the existing consumer and final hash. Its 49/50 and v23 references remain explicitly historical.
- `006_iw043_iw058_portrait_research_2026_07_28.md` and the v1 portrait audit retain their original no-wire findings as historical snapshots, followed by a current v2 promotion amendment.

## Duplicate or superseded documents retained

The v23, v28, v29, v1 portrait, shelf-flattening, and shelf-completeness handoffs remain in place for audit traceability. Their old counts, old authority labels, and pre-promotion portrait conclusions are now marked historical where they could be mistaken for current routing. No gameplay or spreadsheet document was removed.

## Stale prompt or instruction check

The v2 repaint prompt remains the current generation record. The v1 prompt and pre-promotion source-research wording are retained as historical evidence. No current prompt instructs the parent to redo Galimzhan, recreate normalized shelf copies, add advisor art, or promote CHU package admission.

## Validation performed

- `Get-FileHash -Algorithm SHA256 gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds` matches `977e0f8d359930f75e01e380a36893ef6a8f25a5b1ce5bbd8cc3c2f3abf6b5f5`.
- The runtime DDS is present at 131168 bytes, and the parent promotion handoff records the 156x210 legacy BGRA conversion and stable sprite path.
- The shelf was checked for 51 root PNG masters, zero child directories, and zero normalized 156x210 PNGs.
- Targeted `rg` checks confirm that current Event 006 docs use v30 and the 51-master state, while remaining 49/50 and v23 phrases are explicitly historical or bounded evidence.
- The asset manifest and GFX handoff retain the final DDS path, hash, stable sprite, conversion evidence, and five-row source gates.

## Skipped meaningful validation

No Hearts of Iron IV process, event execution, save/load case, GUI interaction, country-package admission, or spreadsheet comparison was run because this task was documentation-only and those checks remain parent-owned or outside scope.

## Remaining contradictions and parent decisions

- CHU remains outside compile-time content attestation despite the single approved Galimzhan portrait consumer. The parent must retain the package HOLD until all grounded rows and the full package audit pass.
- Galimzhan source provenance retains the documented Kazan State University page and photographer uncertainty. The v2 audit records this uncertainty without blocking the bounded DDS promotion.
- The five other CHU/ASY portrait rows remain source-only, blocked, or needs-user-review. No generated or generic portrait substitute is authorized.
- v30 still carries the broader Event 006 **HOLD / PARTIAL** gaps for live waves, focus geometry, decisions and missions, package admission, scenario matrix, AI, balance, super-event 6001, and runtime evidence.
