# Event 006 rejected portrait evidence cleanup plan

Date: 2026-07-16

Status: executed after the acceptance gate passed. The exact transaction and preservation evidence are recorded in `006_rejected_portrait_evidence_cleanup_execution_2026_07_16.md`; this file remains the historical pre-delete plan.

## Direction and hard boundary

Every Event 006 leader, commander, collective, commission, council, board, committee, directorate, and other character portrait must present an unmistakably male subject or all-male group in a vanilla Hearts of Iron IV portrait style.

Only these two runtime DDS files are approved exemptions:

- `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds`
- `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds`

No other large portrait, small commander card, source image, processed image, contact sheet, or prior approval inherits an exemption.

The in-flight directory `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/` was treated as protected production. This audit does not evaluate its partial contents and does not authorize any change inside it.

The deletion sets below become safe only after the replacement package passes the acceptance gate in this plan. Until then, they remain rollback and comparison evidence.

## Current runtime coverage boundary

The runtime directory currently contains 32 Event 006 portrait DDS files:

- 22 large portraits and 10 small commander cards.
- Two large portraits are the approved Rupprecht and Matthes exemptions.
- 30 existing runtime files are non-exempt and therefore require accepted replacement coverage or an explicit retirement decision.
- 24 non-exempt files are currently registered in Event 006 interface files. These comprise 16 large portraits and 8 small commander cards for AFX, AGX, AJX, BAY, BRI, RHI, SCO, and WLS.
- Six non-exempt files for ACX and AEX are present in the runtime directory but are not registered by the current Event 006 portrait interface files. These comprise four large portraits and two small commander cards.

The ACX and AEX files must not silently escape the all-male requirement. Before evidence cleanup, the replacement package must either cover all six or a separate reviewed change must retire the unused runtime files and document why they are no longer Event 006 portrait assets. This plan does not authorize runtime retirement.

## Mandatory acceptance gate

Do not delete any path in this plan until all of the following are true:

1. Production in `portrait_regeneration_male_hoi4_2026_07_16/` is declared frozen by its owner.
2. Its manifest identifies every intended runtime DDS path and every interface sprite consumer.
3. All 30 current non-exempt runtime DDS files are covered by accepted replacements, or the six unregistered ACX and AEX files have an explicit reviewed retirement decision.
4. Every non-exempt large portrait has a source image, processed PNG, final DDS, decoded DDS review image, generation or source metadata, and a direct comparison sheet.
5. Every non-exempt small commander card has an independently composed or deliberately reframed source that remains legible at 65 by 67 pixels. A stale crop copied from an old rejected portrait is not acceptable.
6. A post-production visual audit explicitly confirms male presentation and unmistakable vanilla-HOI4 portrait language for every non-exempt row. Generic painterly, photorealistic, modern illustration, mixed-gender collective, and gender-ambiguous results fail the gate.
7. The Rupprecht and Matthes rows are the only exclusions in the new audit. Their existing provenance and review evidence remains linked.
8. Final runtime paths and sprite names are unchanged unless a separate reviewed wiring change documents each intentional rename.
9. A new hash ledger covers every accepted runtime portrait DDS and its final evidence artifacts.
10. Current source-of-truth documents and manifests point to the accepted package and do not claim that a rejected 2026-07-15 review proves visual acceptance.
11. The NWE flag tooling and ledger have been separated from rejected portrait output so a later flag-only build cannot recreate deleted portrait directories or restore stale portrait hashes.
12. A reference scan finds no current document, manifest, tool, or handoff that depends on a path scheduled for deletion, apart from explicitly retained historical supersession records.

## Exact conditional deletion set

### Five rejected evidence directories

These directories are portrait-only evidence packages and may be deleted whole after the acceptance gate passes:

| Exact path | Files | Bytes observed | Reason |
| --- | ---: | ---: | --- |
| `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/` | 117 | 64,959,632 | Rejected fictional large portrait sources, processed outputs, metadata, review sheets, decode evidence, old small artifacts, prompts, hashes, and tooling. It excludes the two approved real-person exemptions. |
| `docs/assets/006_independence_wave/nwe_package_portraits_2026_07_15/` | 69 | 28,857,660 | Rejected RHI, BAY, SCO, and WLS package portraits plus small cards and supporting evidence. Its mixed-gender institutional-collective direction directly conflicts with the all-male requirement. |
| `docs/assets/006_independence_wave/live_afx_agx_portrait_regen_2026_07_15/` | 18 | 3,539,182 | Rejected AFX and AGX comparison, prompt, metadata, hash, validation, and manifest evidence. |
| `docs/assets/006_independence_wave/bri_package_2026_07_15/` | 15 | 4,235,615 | Rejected BRI civic leader, commander, and commander-small evidence only. This directory contains no independent BRI flag, focus, decision, or advisor art that must survive. |
| `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/` | 58 | 1,756,600 | Rejected ten-card army-small dossier package, including retained DDS copies, metadata, contact sheets, hashes, validation, and tooling. |

Together these five directories contain 277 files and 103,348,689 bytes as observed during this audit.

### Rejected portrait subdirectories inside the mixed top-level NWE tree

These exact subdirectories may be deleted after acceptance. Their sibling `flags/` directories must remain:

- `docs/assets/006_independence_wave/source_png/generated_nwe/command_portraits/`
- `docs/assets/006_independence_wave/source_png/generated_nwe/institutional_portraits/`
- `docs/assets/006_independence_wave/source_png/generated_nwe/registered_command_portraits/`
- `docs/assets/006_independence_wave/source_png/generated_nwe/registered_institutional_portraits/`
- `docs/assets/006_independence_wave/processed_png/generated_nwe/command_portraits/`
- `docs/assets/006_independence_wave/processed_png/generated_nwe/command_portraits_small/`
- `docs/assets/006_independence_wave/processed_png/generated_nwe/institutional_portraits/`
- `docs/assets/006_independence_wave/dds_decoded_png/generated_nwe/command_portraits/`
- `docs/assets/006_independence_wave/dds_decoded_png/generated_nwe/command_portraits_small/`
- `docs/assets/006_independence_wave/dds_decoded_png/generated_nwe/institutional_portraits/`

### Rejected top-level NWE portrait contact sheets

These four files are portrait-only evidence and may be deleted after acceptance:

- `docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_command_portraits_contact_sheet.png`
- `docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_institutional_portraits_contact_sheet.png`
- `docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_final_dds_decoded_contact_sheet.png`
- `docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_officer_small_dds_decoded_contact_sheet.png`

The broad name `006_nwe_generated_final_dds_decoded_contact_sheet.png` does not indicate flag coverage. Its manifest identifies it as portrait review evidence, so it belongs in the deletion set.

The ten mixed-tree portrait directories and four contact sheets contain 54 files and 52,273,606 bytes as observed during this audit. With the five rejected packages, the complete conditional deletion set contains 331 files and 155,622,295 bytes.

### Conditional retirement of the obsolete mixed portrait handoff

The following file is safe to delete only after its one useful flag note is migrated to the flag-only manifest and the accepted replacement package supplies its own portrait handoff:

- `docs/assets/006_independence_wave/northern_western_europe_generated_art_gfx_handoff.md`

The file is otherwise a copy-ready registration handoff for rejected large portraits and small cards. Leaving it as an active handoff after cleanup risks reintroducing rejected art.

## Mixed files that must be migrated, not blindly deleted

### NWE builder

`docs/assets/006_independence_wave/_tooling/build_nwe_generated_art.py` currently handles flags and portraits together. Its `--scope flags` path still prepares portrait directories, and its hash writer scans portrait roots and runtime portrait paths. If run after cleanup, it can recreate rejected directory structure and stale portrait ledger rows.

Before deletion, refactor it into genuinely flag-only behavior or replace it with a dedicated flag builder. A flag-only invocation must not create portrait directories, inspect `gfx/leaders`, decode portrait DDS files, or write portrait hashes.

### Mixed hash ledger

`docs/assets/006_independence_wave/generated_nwe_hashes.sha256` contains valid flag rows and rejected portrait rows. Regenerate it from the corrected flag-only workflow. Preserve the filename if current flag documentation relies on it, or introduce a clearly named flag-only ledger and update every reference. Do not hand-preserve old portrait hash rows as acceptance evidence.

### Mixed manifest

Rewrite `docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md` as a flag-only manifest. Remove the institutional portrait inventory, officer portrait inventory, portrait layout, portrait contact sheets, small dossier references, and portrait completion claims. Preserve the ACX, AFX, AGX, and AJX generated flag inventory and its historical comparison evidence.

### Mixed prompt record

Trim `docs/assets/006_independence_wave/prompts/006_nwe_generated_art.md` to its flag prompts and flag provenance. Remove or clearly archive the rejected portrait prompt section after the old source directories are deleted. The rejected prompt wording must not remain a current production recipe.

## Assets and records that must remain

### Approved exemption evidence

Preserve all existing provenance and review evidence for the only two approved exemptions, including:

- `docs/assets/006_independence_wave/source_png/portraits/bay_rupprecht_of_bavaria_source.jpg`
- `docs/assets/006_independence_wave/source_png/portraits/rhi_josef_friedrich_matthes_source.jpg`
- The related Rupprecht and Matthes files under `docs/assets/006_independence_wave/source_png/portraits/imagegen_edits/`
- `docs/assets/006_independence_wave/processed_png/portraits/portrait_bay_rupprecht_of_bavaria.png`
- `docs/assets/006_independence_wave/processed_png/portraits/portrait_rhi_josef_friedrich_matthes.png`
- Their metadata JSON files under the Event 006 portrait evidence tree
- Their canonical and process-review contact sheets under `docs/assets/006_independence_wave/contact_sheets/portraits/`
- `docs/assets/006_independence_wave/real_portrait_visual_review_2026_07_15.md`
- `docs/assets/006_independence_wave/prompts/006_real_portrait_imagegen_provenance_2026_07_15.md`
- `docs/assets/006_independence_wave/northern_western_europe_gfx_handoff.md`

The similarly named `northern_western_europe_gfx_handoff.md` is not the rejected generated-art handoff. It preserves the two exemptions and the blocked BRI source record and must remain.

### BRI non-portrait and provenance assets

The rejected `bri_package_2026_07_15/` directory contains no unique non-portrait final art. Its documented non-portrait dependencies live elsewhere and must remain untouched:

- Vanilla BRI Gwenn-ha-du flags.
- Vanilla BRI historical political portraits and advisor art.
- Existing shared Event 006 focus and decision icons.
- `interface/006_independence_wave_brittany_portraits.gfx` until accepted replacement art is wired and verified.
- All current BRI runtime DDS files until the replacement transaction is accepted. This cleanup plan does not authorize runtime deletion.

Preserve the following negative-source and rights record even though it is not accepted portrait art:

- `docs/assets/006_independence_wave/bri_francois_debeauvais_source_research_2026_07_15.md`
- `docs/assets/006_independence_wave/source_png/portraits/bri_francois_debeauvais_group_source.jpg`
- `docs/assets/006_independence_wave/source_png/portraits/candidates/bri_francois_debeauvais_1932_ouest_eclair_rejected_us_rights.png`
- `docs/assets/006_independence_wave/source_png/portraits/candidates/bri_francois_debeauvais_1933_breiz_atao_rejected_rights_record.png`
- `docs/assets/006_independence_wave/contact_sheets/portraits/portrait_bri_francois_debeauvais_source_candidate_canonical_blocked.png`

These files document why the historical candidate is blocked and prevent unsafe future reuse. They may be moved to a dedicated provenance archive in a separately approved cleanup, but they should not be erased as part of visual replacement.

### NWE flag assets in the mixed tree

Preserve these flag assets and supporting evidence:

- `docs/assets/006_independence_wave/source_png/generated_nwe/flags/`
- `docs/assets/006_independence_wave/processed_png/generated_nwe/flags/`
- `docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_flags_contact_sheet.png`
- `docs/assets/006_independence_wave/contact_sheets/006_nwe_generated_historical_flags_raw_vs_flat_contact_sheet.png`
- `docs/assets/006_independence_wave/006_nwe_historical_flag_comparison.md`
- `docs/assets/006_independence_wave/source_png/country_symbols/`
- `docs/assets/006_independence_wave/source_svg/country_symbols/`
- All runtime ACX, AFX, AGX, and AJX flag triplets.

### Independent non-portrait packages

Preserve these whole packages and trees:

- `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/`
- `docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/`
- `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/`
- `docs/assets/006_independence_wave/form01_02_04_flags_2026_07_15/`
- `docs/assets/006_independence_wave/low_countries_form03_2026_07_15/`
- `docs/assets/006_independence_wave/low_countries_form03_progression/`
- `docs/assets/006_independence_wave/mediterranean_danube_flag_sources_2026_07_15/`
- `docs/assets/006_independence_wave/mediterranean_danube_generated_flags_2026_07_15/`
- `docs/assets/006_independence_wave/super_events/`
- All top-level achievement, decision, focus, idea, event-picture, and super-event source, processed, decoded, manifest, and handoff trees.
- All top-level non-portrait country-symbol and SVG inputs.

No gameplay script, localisation, `.gfx`, `.gui`, runtime DDS, runtime flag, spreadsheet, or the in-flight replacement directory belongs in this cleanup transaction.

## Current documents that must be updated after acceptance

The following current documents directly describe the rejected evidence as active or point current readers toward it:

| Document | Required update |
| --- | --- |
| `docs/assets/006_independence_wave/manifest.md` | Replace the 2026-07-15 fictional portrait source-of-truth, BRI package, and army-small references with the accepted male-HOI4 package. Keep NWE flags, the two exemptions, and the Debeauvais rights blocker. |
| `docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md` | Convert to flag-only authority. Remove rejected portrait and small-card inventories and completion claims. |
| `docs/assets/006_independence_wave/northern_western_europe_generated_art_gfx_handoff.md` | Retire after migrating the flag lookup note and accepting the new portrait handoff. |
| `docs/assets/006_independence_wave/prompts/006_nwe_generated_art.md` | Keep the flag prompt record. Remove or archive the rejected portrait recipe. |
| `docs/assets/006_independence_wave/northern_western_europe_source_manifest.md` | Keep historical flag evidence, exemption evidence, and Debeauvais blocker. Redirect generated portrait references to the accepted package. |
| `docs/assets/006_independence_wave/gfx_handoff.md` | Preserve the exemption registrations. Replace the link to the rejected mixed generated-art handoff with the accepted portrait handoff. |
| `docs/events/006_independence_wave/northern_western_europe_packages.md` | Replace rejected BRI, army-small, portrait-regeneration, hash, and visual-acceptance references with accepted package evidence while keeping gameplay wording aligned. |
| `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Promote the accepted package and post-production audit. Mark all 2026-07-15 fictional portrait and army-small authorities superseded. Keep flag-only and exemption authorities current. |
| `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` | Replace portrait and small-dossier completion claims, checksums, and next-step guidance with the accepted package status. |
| `docs/plans/006_independence_wave_plans/asset_research/006_generated_fictional_art_inventory.md` | Mark produced portrait rows superseded and link their replacement. Keep any still-valid non-portrait inventory. |
| `docs/plans/006_independence_wave_plans/asset_research/006_package_asset_coverage.md` | Update Event 006 portrait coverage rows after acceptance. Do not rewrite unrelated future-package research. |
| `docs/plans/006_independence_wave_plans/asset_research/006_real_portrait_and_symbol_sources.md` | Preserve the exemption and source-rights research. Change only any statement that treats rejected fictional visuals as current. |

The replacement package should add a dedicated final portrait manifest, hash ledger, comparison review, and GFX handoff. Those files should be named as stable authorities before they are promoted into the source-of-truth map.

## Historical handoffs and audits to mark superseded

Historical implementation and audit records should normally remain for traceability. Their portrait-specific conclusions must be marked superseded or bounded by a prominent note. Their unrelated gameplay, balance, map, flag, and admission findings remain historical evidence unless separately invalidated.

| Historical record | Supersession boundary |
| --- | --- |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_character_portrait_regeneration_handoff_2026_07_15.md` | Entire fictional portrait visual result, hashes, and approval status. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_package_portrait_regeneration_handoff_2026_07_15.md` | Entire RHI, BAY, SCO, and WLS fictional portrait visual result and mixed-gender collective direction. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_army_small_dossier_correction_2026_07_15.md` | Entire old small-card visual result and acceptance evidence. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_generated_art_handoff.md` | Portrait sections only. Flag production and historical flag conclusions remain current after ledger cleanup. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_country_package_audit_2026_07_15.md` | Portrait and art-acceptance sections only. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_afx_agx_release_readiness_audit_2026_07_16.md` | Old portrait hashes, old comparison evidence, and visual fallback conclusion. Gameplay findings remain historical. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wallonia_frisia_package_handoff.md` | Stable portrait inventory and visual-review claim. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_bay_country_package_reaudit_2026_07_15.md` | Generated fictional portrait hash and acceptance evidence. Rupprecht exemption evidence remains current. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_bri_country_package_audit_2026_07_15.md` | BRI fictional portrait and small-card visual acceptance. Gameplay audit findings remain historical. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_bri_country_package_implementation_2026_07_15.md` | Old BRI portrait manifest and small-card evidence. Debeauvais rights blocker remains current. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_bri_ajx_commit_readiness_reaudit_2026_07_16.md` | Portrait review, hashes, small-card evidence, and any visual dossier claim based on rejected art. Gameplay commit-safety findings remain historical. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_ajx_country_package_implementation_2026_07_15.md` | Fictional portrait hash and visual-acceptance claim. Flag ledger conclusions remain after flag-only regeneration. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_ajx_admission_reaudit_2026_07_16.md` | Portrait, small-card, asset-ledger, and advisor visual claims that use rejected evidence. Gameplay admission findings remain historical. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_sco_wls_release_readiness_promotion_2026_07_16.md` | Large and small portrait visual evidence. Gameplay and formable promotion findings remain historical. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_rhi_bay_gameplay_handoff_2026_07_15.md` | The statement that all approved portraits already exist, except for the two named exemptions. Gameplay wiring and stable sprite-name findings remain historical. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_rhi_bay_final_admission_audit_2026_07_16.md` | Visual acceptance proof for non-exempt portraits. Structural wiring findings remain historical and should point to the new audit after acceptance. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_afx_final_admission_audit_2026_07_16.md` | Old visual evidence only. Presence and wiring findings remain structurally useful, subject to the replacement audit. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw003_cornwall_map_feasibility_2026_07_16.md` | ACX portrait-file existence is a dated inventory, not visual acceptance. Update only if the unregistered ACX runtime files are later retired. The map blocker remains independent. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_advisor_icon_withdrawal_audit_2026_07_16.md` | Runtime portrait inventory is a pre-regeneration snapshot. Advisor-icon withdrawal findings remain current. |

Do not supersede these still-valid records wholesale:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_northern_western_europe_asset_source_handoff.md`. Its Rupprecht and Matthes approval and Debeauvais rejection remain current.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_round_number_balance_preflight_2026_07_15.md`. Its exemption hash statement remains current.

An unrelated Event 015 tooling-migration handoff also names some old Event 006 paths as historical migration evidence. It is not a current Event 006 authority and should not be edited by this cleanup. If reference scans retain it as an explicit historical exception, the source-of-truth map should make that status clear.

## Cleanup order

1. Freeze and audit the new male-HOI4 production package.
2. Resolve all 30 non-exempt runtime rows, including the six unregistered ACX and AEX files.
3. Wire accepted runtime replacements without changing stable paths or sprites unless a reviewed wiring change requires it.
4. Produce the final replacement manifest, hash ledger, decoded comparison sheets, and portrait GFX handoff.
5. Refactor or replace the mixed NWE builder so flag-only work cannot touch portraits.
6. Regenerate the NWE ledger as flag-only and rewrite the mixed NWE manifest and prompt record.
7. Update current documentation and source-of-truth routing.
8. Mark historical portrait-specific claims superseded while preserving unrelated findings.
9. Run the pre-delete reference and coverage checks.
10. Delete only the exact conditional deletion paths listed above.
11. Run the post-delete preservation and non-recreation checks.
12. Record the deletion transaction and final audit result in a new handoff.

## Suggested validation

### Pre-delete runtime and consumer inventory

```powershell
Get-ChildItem -LiteralPath 'gfx/leaders/006_independence_wave' -File -Filter '*.dds' |
	Sort-Object Name |
	Select-Object Name, Length

rg -n 'gfx/leaders/006_independence_wave/.+\.dds' interface/006_independence_wave*.gfx
rg -n 'GFX_portrait_' common/characters common/scripted_effects history/countries -g '*006*'
```

Compare the results to the accepted manifest. The only exempt runtime rows must be Rupprecht and Matthes.

### Character gender metadata audit

```powershell
rg -n -i -g '006_independence_wave*.txt' -g '*Event 006*.txt' '\b(female|gender)\b\s*=' common events history
```

This is a metadata check, not a substitute for visual inspection. Institutional character names may remain institutional, but their portrait art must visibly present an all-male group or a single male officeholder.

### Old-authority reference scan

```powershell
rg -n 'portrait_regeneration_2026_07_15|nwe_package_portraits_2026_07_15|live_afx_agx_portrait_regen_2026_07_15|bri_package_2026_07_15|army_small_dossier_correction_2026_07_15|generated_nwe/(command_portraits|institutional_portraits|registered_command_portraits|registered_institutional_portraits)' docs
```

Every surviving result must be an explicit supersession record, this cleanup plan, or the unrelated historical Event 015 migration record. No current manifest, source-of-truth document, build script, or active handoff may depend on a deleted path.

### Post-delete path checks

```powershell
$deleted = @(
	'docs/assets/006_independence_wave/portrait_regeneration_2026_07_15',
	'docs/assets/006_independence_wave/nwe_package_portraits_2026_07_15',
	'docs/assets/006_independence_wave/live_afx_agx_portrait_regen_2026_07_15',
	'docs/assets/006_independence_wave/bri_package_2026_07_15',
	'docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15'
)

$deleted | ForEach-Object {
	[pscustomobject]@{ Path = $_; Exists = Test-Path -LiteralPath $_ }
}

$protected = @(
	'docs/assets/006_independence_wave/afx_unique_assets_2026_07_16',
	'docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15',
	'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16',
	'docs/assets/006_independence_wave/source_png/generated_nwe/flags',
	'docs/assets/006_independence_wave/processed_png/generated_nwe/flags',
	'docs/assets/006_independence_wave/super_events'
)

$protected | ForEach-Object {
	[pscustomobject]@{ Path = $_; Exists = Test-Path -LiteralPath $_ }
}
```

All `$deleted` rows must report `False`. All `$protected` rows must report `True`.

### Flag-only non-recreation check

Run the corrected flag-only builder in a clean temporary output area first. Confirm that it creates no portrait directories, reads no runtime portrait DDS file, and produces a ledger with no `gfx/leaders` row. Only then use it on the canonical flag evidence tree.

### Final runtime evidence check

Recompute hashes for all 32 runtime DDS files. Confirm that the accepted ledger covers 30 non-exempt rows or documents an approved retirement for each absent ACX or AEX row. Confirm that the two exempt hashes still match their preserved provenance record. Review decoded large and small outputs at native size and on a representative HOI4 leader interface background.

## Risks and unresolved decisions

- The replacement package was still being written during this audit, so no claim is made about its coverage, quality, filenames, hashes, or acceptance.
- The six unregistered ACX and AEX runtime files need an explicit keep-and-replace or retire decision. Evidence cleanup must not make that decision implicitly.
- Refactoring the mixed NWE builder is mandatory. Deleting evidence before this is fixed would allow later flag work to recreate rejected portrait structure and stale hashes.
- The mixed NWE hash ledger cannot remain authoritative in its current form.
- Old contact sheets, hashes, and statements such as accepted, visually approved, or HOI4 style cannot be used to approve the replacement package.
- Historical handoffs should remain for traceability unless the documentation curator explicitly chooses a different retention policy. Their portrait conclusions must be visibly superseded.
- The blocked Debeauvais source record is a provenance safeguard, not rejected-art clutter.

## Handoff result

This audit identifies a conditional deletion set of 331 portrait-evidence files totaling 155,622,295 bytes, plus one obsolete mixed portrait GFX handoff after its flag note is migrated. It identifies the exact flag, exemption, BRI provenance, and independent non-portrait assets that must remain. It also maps the current documents that require replacement references and the historical records whose portrait conclusions must be marked superseded.

No deletion, runtime edit, gameplay edit, GFX edit, spreadsheet edit, or change inside the in-flight production directory was performed.

## Simplifications, omissions, and blockers

No cleanup action was simplified or replaced with a fallback. Deletion is intentionally blocked until the acceptance gate passes. The in-flight package was intentionally not assessed because it is still being written and was explicitly outside this task's allowed write and review surface.

## Skills used

- `chaos-redux-subagents` for bounded documentation ownership, handoff structure, and parent-review requirements.
- `chaos-redux-event-assets` for source, processed, DDS, decoded review, metadata, manifest, contact-sheet, preservation, and asset-handoff classification.

No skill was created or updated during this audit.
