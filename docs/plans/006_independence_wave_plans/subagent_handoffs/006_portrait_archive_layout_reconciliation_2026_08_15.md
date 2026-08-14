# Event 006 portrait archive layout reconciliation

Date: 2026-08-15

Status: Documentation-only reconciliation complete; this handoff makes no gameplay, runtime, asset, workbook, central-admission, or Join completion claim.

## Scope and source-of-truth map

The current portrait archive authority is `docs/assets/portraits/006_independence_wave/`.

Original source files are kept directly in that parent directory.

Exactly one child directory, `processed/`, contains processed assets and metadata.

No image files named with the `156x210` archive-retention convention are kept in either the parent or `processed/`; `156x210` remains a deterministic processing size in the grounded portrait workflow, not a retained archive shelf.

Runtime DDS and GFX files remain separate from the evidence archive, including engine-facing paths such as `gfx/leaders/006_independence_wave/` and the relevant `interface/` registrations.

The current layout is stated in the resume packet current override, the Event 006 overview current overrides, the Northern and Western Europe package reference, the Pacific package reference, and the IW-012 asset section.

The archive is evidence and ComfyUI input only; archive presence does not grant DDS, GFX, character, runtime, package, attestation, or formable admission.

## Files changed

| File | Reconciled section | Change |
| --- | --- | --- |
| `docs/events/006_independence_wave/iw012_ice_package.md` | `## Assets` | Replaced the current `portraits_generated_png` and nested-shelf wording with the consolidated parent-plus-`processed/` layout and explicit no-retained-`156x210` rule. |
| `docs/events/006_independence_wave/northern_western_europe_packages.md` | Historical regional portrait paragraph and shelf index | Replaced the current 83-master shelf statement with the authoritative layout and labeled the dated 83-master index as historical traceability. |
| `docs/events/006_independence_wave/pacific_country_packages.md` | Installed-scan/portrait evidence continuation and shelf index | Removed the current-sounding 63-master shelf continuation, stated the consolidated archive layout, and labeled the dated 83-master index as historical traceability. |
| `docs/events/006_independence_wave/overview.md` | Current portrait overrides, IW-177 paragraph, asset-wiring section, and historical bridge wording | Replaced current 80/83-style shelf authority claims with the flat-parent-plus-`processed/` layout and marked 80/81/82 shelf records as dated traceability. |
| `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` | Current portrait archive layout override | Clarified the single-parent layout, exactly one `processed/` child, no retained `156x210` files, and separate runtime DDS/GFX surfaces. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_portrait_archive_layout_reconciliation_2026_08_15.md` | This handoff | Records the source-of-truth map, dispositions, validation, and remaining historical references. |

The quality simplifications/blockers spec was inspected but did not require a patch because its current portrait policy already describes the evidence-only and gated promotion boundary without a stale archive path or current master count.

## Superseded sections and dispositions

| Prior wording or surface | Disposition |
| --- | --- |
| Current 80/83-master or 63-row/68-file shelf claims in the overview and regional package docs | Superseded for current status by the consolidated archive layout; dated count paragraphs remain only where explicitly labeled historical traceability. |
| Current `docs/assets/006_independence_wave/portraits_generated_png` reference in IW-012 | Removed as a current reference and replaced with the authoritative archive path. |
| Current shelf authority wording in the resume packet | Reconciled in place; the older dated 83-master paragraph remains historical documentation authority only. |
| Historical 80/81/82/83 counts and dated source-placeholder evidence | Left unchanged or explicitly labeled historical to preserve traceability, as requested. |
| Specs, gameplay docs, assets, workbook, central admission, and Join surfaces | Left unchanged and out of scope. |

No document was deleted, merged, promoted to gameplay authority, or marked as runtime-complete.

## Contradiction audit

Resolved contradictions were the current-sounding 80/83/63-master shelf claims and the old `portraits_generated_png` path, which conflicted with the approved physical archive layout.

The remaining old count and path references are explicitly dated historical records, including the 2026-08-03 resume paragraph's `source_placeholder_2026_08_03` tranche, and therefore do not contradict the current archive authority.

No open current portrait-archive contradiction remains in the scoped direct Event 006 markdown files or the current resume-packet section.

The concurrent package-arithmetic edits visible in the Northern and Western Europe and Pacific package documents were preserved and are not part of this reconciliation.

## Remaining historical references

| File and section | Remaining reference | Why it remains |
| --- | --- | --- |
| `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md:105` | Historical 83 original-size masters and `docs/assets/006_independence_wave/source_placeholder_2026_08_03/` | The paragraph is explicitly labeled `Historical documentation authority (2026-08-03; traceability only)`. |
| `docs/events/006_independence_wave/overview.md:164,178,180` | Dated v102 and 2026-08-02 80/74/6 shelf records | The sections are dated historical evidence and now state that the count is traceability-only. |
| `docs/events/006_independence_wave/overview.md:387,391` | 81-master snapshot and 80/81/82 shelf wording | The bridge and follow-up sentence explicitly identify the wording as historical and point to the current archive-layout override. |
| `docs/events/006_independence_wave/northern_western_europe_packages.md:32,38` | 63-row/68-file and 83-master records | Both are explicitly marked dated regional or shelf-index traceability. |
| `docs/events/006_independence_wave/pacific_country_packages.md:75` | 83-master shelf-index record | Explicitly marked historical traceability. |

Future documentation agents should not promote these dated references back to current authority without a new user-approved archive decision.

## Duplicate, superseded, and stale-document audit

No duplicate current archive authority was found in the named docs after reconciliation; all current statements point to the same parent and `processed/` layout.

No old prompt, manifest, or report inside the named documentation scope required a current-reference patch.

No docs were deleted; historical sections were retained and labeled rather than erased.

## Markdown hard-wrap audit

The affected current archive statements in the Pacific package continuation and the other patched sections are now one physical line per prose sentence.

Existing unrelated hard-wrapped prose and dated evidence blocks elsewhere in the event docs were not mass-reflowed because that would exceed the portrait-archive scope and risk concurrent edits.

Intentional headings, list items, tables, and historical paragraphs were preserved.

## Validation evidence

The initial physical archive check for this reconciliation reported exactly one child directory, `processed`, with 46 files directly in the parent and 122 files in `processed`; both parent and processed filename scans returned no `156x210` image files.

Post-reconciliation IW-051 source research added two original YAK source images directly in the parent and their processed provenance/crop evidence under `processed/`. The current physical archive check therefore reports exactly one child directory, `processed`, with 48 files directly in the parent and 137 files in `processed`; the parent and processed filename and image-dimension scans still return no `156x210` files.

A focused search across the direct Event 006 markdown scope, the resume packet, and the simplifications/blockers spec found no remaining `portraits_generated_png` reference.

The same search found only the historical count/path records listed above, each explicitly labeled historical or traceability-only.

`git diff --check` was run against the five edited source documents and reported no whitespace errors; the handoff was then added as the sixth documentation change.

No MCP route was used because this task reconciles documentation and physical archive paths only and does not inspect an event, focus, map, GUI, technology, or weighted-logic surface.

No game launch, binary image inspection, asset conversion, workbook export, or runtime validation was performed because those surfaces are outside the requested docs-only scope.

## Parent decisions and remaining risks

No parent decision is required for the current archive layout; it is treated as user-approved authority in this handoff.

The parent should review the concurrent package-arithmetic edits in the two regional documents before committing the shared worktree, then commit only the intended scoped changes.

The remaining historical `source_placeholder_2026_08_03` path may be mistaken for an active archive by future readers despite its label; a future archival pass may add a dedicated historical-archive note, but that is not required for this reconciliation.

Some older evidence packages referenced by the overview remain under their historical package-local paths; they are evidence history and not current consolidated archive authority.

No simplification or unapproved fallback was introduced by this documentation change.
