# Event 006 tag architecture documentation alignment handoff

> **Historical architecture snapshot.** This 2026-07-15 alignment handoff is
> retained for change history. Use the canonical candidate registry CSV for
> identity, the current installed-map binding CSV for anchors/hosts/bindings,
> and the tag collision/reuse audit for safety. Its `102/91/13` summary is
> explanatory; it does not replace those sources or carry current runtime
> admission status.

Date: 2026-07-15

## Scope completed

Aligned the Event 006 source-of-truth narrative, research reports, quality records, checklists, package manifest, and signature dossiers with the accepted installed tag and vanilla-identity architecture.

This was a documentation-only curation tranche. No gameplay, localisation, scripted localisation, GUI, GFX, asset, audio, CSV matrix, workbook, skill, or tag-audit source file was edited by this subagent.

## Accepted architecture recorded

- Total packages: **206**.
- Custom Event 6 countries: **102**.
- Registered vanilla-tag reuses: **91**.
- Non-selectable vanilla route overlays: **13**.
- Unique nonblank resolved carrier tags: **191**; only `CHU` and `BIA` are
  intentionally shared.
- Selectable installed-map pool: **138 bound and 55 unbound**.
- Superseded pre-overlay map result: **149 bound and 57 unbound**.
- Current dispositions: 9 automatic, 44 automatic if not living, 73 automatic if unique, 27 high-chaos, 7 route-only, 30 specific-community, 3 scenario, and 13 vanilla-route-overlay-only.

The historical `149/57` result remains only where it is explicitly labeled superseded all-row evidence. Eleven overlays were previously counted as bound. `IW-102` and `IW-105` were previously counted as unbound and now use `overlay_carrier_route`, so neither remains in the selectable unbound list.

## Identifier decisions recorded

Registered-tag migrations:

- `IW-038 RUT`
- `IW-042 GAL`
- `IW-043 CHU`
- `IW-096 BIA`
- `IW-133 BAN`
- `IW-150 ATJ`
- `IW-153 POK`
- `IW-155 BLI`
- `IW-157 WPG`
- `IW-167 CHM`
- `IW-171 OKN`
- `IW-172 ANU`
- `IW-178 PNG`

Custom remaps:

- `IW-021 ICX` (parent post-review correction; `AUX` is a Windows-reserved device basename)
- `IW-087 HYX`
- `IW-124 HZX`
- `IW-161 IAX`
- `IW-162 IBX` (parent post-review correction; `GFX` is the engine-reserved graphics namespace)

Intentional shared tags:

- `CHU` is shared by `IW-043` and `IW-046`.
- `BIA` is shared by `IW-096` and `IW-107`.
- Both pairs require package flags and mutual exclusion. Tag identity alone must not assign content.

`IW-153` Dayak Federation reuses vanilla `POK`, the Dayak Republic of West Borneo, and retires `FWX`. Its compatibility adapter must preserve `POK` history, characters, cores, `INS` releasable membership, and `indonesia_transfer_POK` behavior. The package remains `specific_community_variant_only` and unbound.

Overlay-only rows:

- `IW-005 BEL_flanders`
- `IW-022 CRO` with the dynamic `dalmatia` identity
- `IW-025 HUN` with the dynamic `vojvodina` identity
- `IW-035 LIT` with `LIVONIA`
- `IW-059 neo_mesopotamia`
- `IW-085 LBA` under the Cyrenaica autonomy identity
- `IW-101 COG_kingdom_of_kongo`
- `IW-102 COG_kingdom_of_kuba`
- `IW-105 COG_kingdom_of_loango`
- `IW-156` on democratic `TNE`
- `IW-196 antilles`
- `IW-197 CHL_mapuche_state`
- `IW-204 kingdom_of_araucania_and_patagonia`

## Files changed

- `docs/specs/006_independence_wave_specs/README.md`
  - Replaced the stale universal-tag statement and `128/78` architecture with `102/91/13`.
  - Reconciled the selectable pool to `138/55`.
  - Marked all compatibility adapters and overlay hooks as implementation obligations.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md`
  - Added the three-way representation architecture and eight current dispositions.
  - Recorded all registered migrations, custom remaps, shared-tag rules, exact overlays, and the `IW-153 POK` preservation contract.
  - Reclassified `149/57` as superseded pre-overlay evidence and made `138/55` the selectable pool.
  - Removed the obsolete `BIA` exclusivity and `DRX` assertion.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`
  - Extended the package contract to cover exact vanilla overlays.
  - Replaced the old seven-disposition totals with the current eight-disposition totals.
  - Split selectable-country validation from overlay validation.
- `docs/specs/006_independence_wave_specs/research/006_signature_country_research_dossiers.md`
  - Updated resolved-representation paragraphs for `IW-043 CHU`, `IW-059 neo_mesopotamia`, `IW-096 BIA`, `IW-150 ATJ`, `IW-161 IAX`, and `IW-197 CHL_mapuche_state`.
  - Corrected Mesopotamia and Mapuche map wording so neither reads as a standalone release.
- `docs/specs/006_independence_wave_specs/research/006_research_completion_report.md`
  - Reconciled representation and disposition totals.
  - Distinguished superseded all-row evidence from the selectable pool.
  - Added the thirteen compatibility adapters and thirteen overlay hooks to remaining implementation work.
- `docs/specs/006_independence_wave_specs/quality/package_manifest.md`
  - Added current architecture and disposition metrics.
  - Labeled the old file counts and checksum table as superseded 2026-07-14 packaging evidence instead of presenting stale hashes as current.
- `docs/specs/006_independence_wave_specs/quality/research_validation_report.md`
  - Replaced old tag counts, dispositions, and `149/57` current-state claims.
  - Recorded both intentional shared tags and zero unintended duplicates.
  - Added the migration, remap, overlay, and `POK` validation obligations.
- `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md`
  - Replaced stale tag and binding counts.
  - Made compatibility adapters and overlay hooks explicit blockers.
- `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md`
  - Replaced universal resolved-tag checks with representation checks.
  - Added unchecked compatibility-adapter and overlay-hook completion gates.
- `docs/specs/006_independence_wave_specs/quality/research_acceptance_checklist.md`
  - Recorded blank `resolved_tag` as intentional for overlay rows.
  - Added the shared-tag, remap, `POK`, overlay, and selectable-pool acceptance facts.
  - Kept adapter and overlay implementation unchecked.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_tag_architecture_documentation_alignment_handoff.md`
  - Added this curation handoff.

## Documentation disposition

Promoted into current source-of-truth narrative:

- the `102/91/13` representation architecture
- the `138/55` selectable pool
- the thirteen registered migrations
- the five custom remaps
- the two intentional shared tags
- the thirteen exact overlay identities
- the `IW-153 POK` compatibility obligations

Superseded but retained as labeled historical evidence:

- the `149 bound and 57 unbound` pre-overlay map result
- the 2026-07-14 package file counts and checksum table

Rejected as obsolete current assertions:

- `78` registered reuses and `128` custom tags
- `103` custom tags and `90` registered reuses after the final Dayak identity audit
- a resolved standalone tag for every package
- `BIA` exclusive to Biafra and `DRX` for Edo Benin
- standalone Event 6 countries for the thirteen overlay rows
- active signature assignments `BQX`, `CGX`, `FTX`, `GEX`, and `HOX`

Queued implementation obligations:

- thirteen registered-tag compatibility adapters
- thirteen additive overlay hooks
- package-flag and mutual-exclusion enforcement for the shared `CHU` and `BIA` pairs
- complete `POK` preservation for `IW-153`

No accepted plan or source document was rejected beyond the obsolete assertions listed above. No fallback or substitute representation was introduced.

## Validation evidence

- Parsed the current candidate registry and confirmed exactly 206 rows, 102 custom tags, 91 registered reuses, and 13 overlays.
- Confirmed all 102 custom tags match the required `X` suffix pattern and are unique.
- Recomputed all eight disposition totals from the registry.
- Verified every accepted registered migration and custom remap against the current registry.
- Verified that the only shared nonblank resolved tags are `BIA` and `CHU`, with the exact intended package pairs.
- Joined the current package bindings to the non-overlay registry and independently reproduced 138 bound and 55 unbound selectable packages.
- Confirmed `IW-153` resolves to `POK`, remains `specific_community_variant_only`, and remains unbound.
- Confirmed the exact thirteen overlay package IDs and that all use the non-selectable overlay disposition.
- Searched all Event 006 Markdown outside the preserved tag-audit source and found no active `78/128`, `103/90`, prior adapter-count, `DRX` Benin, or retired signature-tag assertion.
- Reviewed the documentation diff for the Chaos Redux prose restrictions used by `chaos-redux-events`.

## Skipped validation and why

- No gameplay parser, game launch, route execution, focus assignment, AI, localisation, asset, or workbook validation was run because this tranche made documentation changes only.
- No checksum table was regenerated. The old table is deliberately retained and labeled superseded historical evidence.

## Remaining risks and parent follow-up

1. Do not treat identifier alignment as adapter implementation.
2. Keep every overlay out of automatic, high-chaos, scenario, and manual country selection.
3. Preserve vanilla behavior whenever a reused tag lacks the Event 6 package flag.
4. Implement and audit the shared `CHU` and `BIA` package-flag and mutual-exclusion paths.
5. Preserve all named `POK` surfaces before enabling any `IW-153` Event 6 content.
6. Rerun the installed registry audit if the game build, Workshop set, local mods, aliases, or Chaos Redux tag surfaces change.

## Skills used

- `chaos-redux-subagents`
- `chaos-redux-events`

No skill was created or updated.
