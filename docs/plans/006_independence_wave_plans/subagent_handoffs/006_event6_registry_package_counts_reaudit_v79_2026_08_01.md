# Event 006 registry and package-count re-audit v79

Date: 2026-08-01

Role: bounded documentation and source-count auditor

Scope: recount the current Event 006 candidate registry, direct country-definition surface, runtime adapter rows, compile-time attestation IDs, compatible reservation groups, and automatic/SCN-008 capacity after the IW-018 ARX admission. This handoff does not edit gameplay, localisation, assets, spreadsheets, or historical handoff bodies.

## Disposition

The current source/static count authority is **fourteen exact content-attested packages across thirteen compatible reservation groups and fourteen distinct anchors**. The current allocator still reports 149 publisher blocks, 126 automatic/high-chaos selectable packages, and 138 SCN-008 ranked packages. The earlier thirteen-package/twelve-group/thirteen-anchor snapshot is historical and must not be used for current package counts after the IW-018 ARX admission in commit `493a7cfb5`.

The allocator and registry count audits pass. Whole Event 006 remains **HOLD / PARTIAL**: the 14- and 20-country automatic bands remain fail-closed despite the static fourteen-package pool because complete package, host-survival, reservation, transaction, and synchronized source evidence is not established for the upper bands. IW-043 CHU, IW-058 ASY, IW-179 FSM, IW-093 DOX, and IW-098 SOK remain fail-closed; IW-014 CAT, IW-030 MNT, IW-177 FIJ, and the shared IW-046 CHU row are also not content-attested.

## Current source-of-truth map

| Surface | Current count or set | Authoritative evidence |
| --- | --- | --- |
| Candidate package registry | 206 unique package rows | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` |
| Selectable/overlay decomposition | 193 selectable rows and 13 route-only overlay rows | Candidate registry `automatic_pool_disposition` and `tag_resolution` fields |
| Installed-map binding split | 138 selectable rows bound, 55 selectable rows unbound, and 13 overlays | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` |
| Custom Event 006 country-tag declarations | 102 rows, all custom tags ending in `X` | `common/country_tags/006_independence_wave_countries.txt` and the current `audit_hoi4_country_tags.py` run |
| Direct researched country definitions | 85 individual country-definition files | 102 tag declarations minus 17 inert unresolved reservations; the 17 unresolved rows all point to `006_independence_wave_unresearched_reservations.txt` |
| Physical Event 006-prefixed country files | 87 files: 85 direct definitions, one inert shared reservation file, and one separate formable/cosmetic file | `common/countries/` read-only inventory |
| Registered-tag reuse | 91 registry rows using 89 unique vanilla carriers | Fresh installed-tag audit and canonical registry |
| Central runtime adapter allowlist | 22 IDs: IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-030, IW-043, IW-058, IW-093, IW-098, IW-173, IW-177, IW-179, IW-184 | `has_independence_wave_runtime_package_adapter_for_execution_id` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` |
| Exact package-wrapper helpers | 22 unique IDs; the wrapper surface includes IW-046 where the central adapter allowlist includes IW-030 | `is_independence_wave_exact_package_iw_NNN_tag_available` across Event 006 package-trigger files |
| Publisher/reservation blocks | 149 unique package publishers | `.tools/audit_event6_allocator.py` and `common/scripted_effects/006_independence_wave_packages_region_*_effects.txt` |
| Compile-time content attestation | 14 IDs: IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-017, IW-018, IW-019, IW-173, and IW-184 | `has_independence_wave_runtime_package_content_attestation_for_execution_id` and the current ARX post-wire audit |
| Compatible attested reservation groups | 13 unique groups | Attested package loaders and `006_current_map_reservation_groups.csv` |
| Attested anchor witnesses | 14 pairwise-distinct anchors | Attested package loaders and `.tools/audit_event6_allocator.py` |
| Automatic/high-chaos selector capacity | 126 selectable packages | `.tools/audit_event6_allocator.py` |
| SCN-008 ranked capacity | 138 distinct ranked packages | `.tools/audit_event6_allocator.py` |
| Automatic ladder | 6, 8, 10, 14, and 20; World Collapse also targets 20 | `common/script_constants/006_independence_wave_constants.txt` and allocator audit |

The attested package-to-group/anchor mapping is:

| Package | Group | Anchor |
| --- | --- | ---: |
| IW-001 | RG-121-120-133 | 121 |
| IW-002 | RG-122 | 122 |
| IW-004 | RG-14 | 14 |
| IW-006 | RG-34 | 34 |
| IW-007 | RG-36 | 36 |
| IW-008 | RG-RHINE-SAAR | 51 |
| IW-009 | RG-52-53-54 | 52 |
| IW-010 | RG-RHINE-SAAR | 42 |
| IW-012 | RG-100 | 100 |
| IW-017 | RG-1 | 1 |
| IW-018 | RG-114 | 114 |
| IW-019 | RG-115 | 115 |
| IW-173 | RG-629 | 629 |
| IW-184 | RG-378 | 378 |

The thirteen attested groups have a static maximum sum of fourteen packages because RG-RHINE-SAAR admits exactly two distinct packages (IW-008 anchor 51 and IW-010 anchor 42) and the other twelve groups admit one each. This static sum does not clear the upper automatic-band gates.

## Unresolved plan and handoff disposition

| Evidence or plan | Disposition |
| --- | --- |
| `006_iw018_arx_postwire_package_audit_v78_2026_08_01.md` | **Current admission evidence.** IW-018 ARX is admitted after its sourced roster, runtime DDS/GFX, consumer-role, and post-wire package audit. |
| `006_iw173_haw_country_package_audit_v45_2026_08_01.md` and `006_iw173_samuel_wilder_king_portrait_audit_v46_2026_08_01.md` | **Current admission evidence.** IW-173 HAW remains admitted as the additive non-ruling King consumer while the vanilla ruling roster is preserved. |
| `006_event6_completion_audit_v73_2026_08_01.md` and earlier v70-v72 audits | **Dated pre-ARX evidence.** Preserve the bodies; their thirteen-package count is superseded by the current source and allocator after commit `493a7cfb5`. |
| `006_registry_api_closure_v35_2026_07_29.md` | **Historical registration authority.** Its 206/102/85/17/138/55/13 registry decomposition remains valid; its earlier allocator attestation count is not current. |
| `006_iw043_chu_country_package_audit_v58_2026_08_01.md` | **Fail-closed.** The visual evidence does not admit CHU. Keep CHU package admission separate from source-only portrait PASS results. |
| `006_iw058_asy_package_closure_audit_v80_2026_08_01.md` | **Fail-closed.** ASY remains outside the attestation gate pending complete sourced-roster and package proof. |
| `006_iw030_montenegro_country_package_audit_v52_2026_08_01.md` | **Fail-closed.** MNT has an adapter and visual evidence, but rights and complete package admission remain open. |
| `006_iw014_cat_package_implementation_2026-08-01.md` and FORM-07 adapter handoff | **Implementation draft / fail-closed.** CAT remains outside attestation pending the Iberian identity/flag contract and complete NAV/GLC package adapters. |
| Existing tag-audit JSON `tag_audit/006_installed_tag_collision_audit_2026_08_01.json` | **Superseded report artifact.** Its dispatch hash predates IW-018 and its 13-ID runtime list is stale; do not use it as current attestation authority. |

## Contradictions and stale current surfaces

1. The current source map's top authority and allocator source state 14/13/14, but lower historical/current prose in `docs/events/006_independence_wave/overview.md` still says 13/12/13 and omits IW-018 from the exact list at lines 41, 76, 82, 98, and 182. Those paragraphs need a parent-owned documentation reconciliation; they were not rewritten in this count-only pass.
2. `docs/events/006_independence_wave/northern_western_europe_packages.md:30` still describes the event-wide count as thirteen packages across twelve groups and thirteen anchors. Its regional nine-package count remains valid; only the event-wide suffix is stale.
3. `docs/assets/006_independence_wave/manifest.md:288` omits IW-018 from the exact portrait-compliant package list, `:423` still says IW-006 is one of twelve packages, and `:525-533` still carries the earlier thirteen-package/61-master current section. The dated 56-master section at `:501-520` is historical and should remain marked as such.
4. The portrait shelf evidence is internally inconsistent and outside this bounded gameplay-count audit: the README says 61, the flat `PRE_RESIZE_MANIFEST.md` contains 63 data rows, the shelf contains 68 physical PNG files, and five files (the four ARX masters plus the CHU Mirsaid master) are not listed in that manifest. The current Event 006 prose generally says 63. No asset or manifest files were edited here.
5. The central adapter allowlist has IW-030 while the exact-wrapper helper inventory has IW-046 instead. This is a source-surface distinction around the custom MNT adapter and shared CHU row, not admission evidence. The parent should decide whether the mismatch is intentional before changing either registry.
6. Historical handoffs and prompts that say thirteen attestations, twelve groups, or twenty adapter IDs are retained for traceability. They must not be silently rewritten or promoted over the post-ARX source and current allocator output.

## Duplicate and superseded documents

- Preserve `006_event6_completion_audit_v73_2026_08_01.md`, the v70-v72 audits, and the older v5-v69 handoffs as dated evidence.
- Treat `006_iw018_arx_postwire_package_audit_v78_2026_08_01.md`, the current source map authority section, and the current allocator output as the post-ARX count authority.
- Treat `tag_audit/006_installed_tag_collision_audit_2026_08_01.json` as a stale generated report because its dispatch file hash is `eca89ec6...`, while the current dispatch source hashes to `0e0550d1...` after ARX admission.
- Do not delete or rewrite historical handoff bodies. Add a current supersession note only if the parent later chooses to reconcile their indexes.

## Stale prompt or instruction list

No in-scope current prompt file was found that authorizes a different package-count authority. The stale instructions are historical handoffs and generated reports: the 2026-07-29 Soviet admission matrix still describes a twenty-ID adapter set and a twelve-package attestation snapshot, and the pre-ARX tag-audit JSON still records thirteen IDs. They remain evidence-only and should not drive new implementation work.

## Recommended parent decisions

1. Promote 14 packages/13 compatible groups/14 anchors as the sole current Event 006 package-count authority and add IW-018 ARX to every current exact-set list.
2. Keep IW-043 CHU, IW-058 ASY, IW-179 FSM, IW-093 DOX, and IW-098 SOK fail-closed, with no advisor, dossier, operative, commander-small, or `_small` fallback assets.
3. Keep IW-014 CAT, IW-030 MNT, IW-177 FIJ, and IW-046 CHU out of content attestation until their complete package contracts pass independent audits.
4. Keep the 14- and 20-country bands fail-closed even though the static attested group sum is fourteen; no capacity claim should be inferred from registry, adapter, or publisher counts alone.
5. Reconcile current overview, NWE, asset-manifest, README, and resume prose to the post-ARX source counts in a later documentation-only pass. Resolve the 63-row/68-file portrait inventory before any final asset closure claim.
6. Decide whether the IW-030/IW-046 adapter-wrapper difference is an intentional custom-adapter boundary or requires a source correction. Do not change the central allowlist during this documentation audit.

## Proposed cleanup if patching is deferred

If the parent defers the documentation patch, preserve the current source and allocator as authoritative, add a supersession note to the current overview/NWE/asset index surfaces, refresh the full installed-tag report against the current dispatch hash, and reconcile the portrait shelf manifest only after the ARX/CHU evidence files receive an explicit disposition. No gameplay fallback or silent package promotion is proposed.

## Meaningful validation performed

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 14 attested packages, 13 compatible groups, 14 distinct anchors, the 6/8/10/14/20 ladder, World Collapse 20, and the Event 005-before-Event 006 reservation order.
- `python -B .tools/audit_hoi4_country_tags.py --workshop-root C:\__event6_no_workshop__ --local-mod-root C:\__event6_no_local__ --write-reports --report-dir .tmp\event6_registry_audit_v79` passed its repository/vanilla registry checks with 206 candidate rows, 102 Event 006 country-tag rows, 7 formable/cosmetic rows, 109 owned identifiers, 85 owned history filenames, 91 reused rows across 89 unique vanilla tags, 13 overlay rows, the current 14-ID runtime attestation list, and zero scanned collisions. The constrained roots were used to avoid rewriting the tracked full-environment report while checking current source after ARX.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan --workshop-root C:\__event6_no_workshop__ --local-mod-root C:\__event6_no_local__` passed with 136 protected Event 006/Soviet tags and zero country-definition or identity-surface collisions in the constrained scan.
- A direct read-only source recount found 102 Event 006 tag declarations, 85 direct country-definition paths, 17 inert shared-reservation references, 22 central adapter IDs, 22 unique exact-wrapper helpers, 14 attested IDs, 13 attested groups, and 14 distinct attested anchors. The installed-map attested-group maximum sums to 14 because RG-RHINE-SAAR has capacity two.
- A read-only portrait-shelf check found 63 data rows in `PRE_RESIZE_MANIFEST.md`, 68 physical shelf PNGs, and the README's stale 61-master statement. No asset or manifest file was changed.

## Validation not sufficient for whole-event completion

- The full Workshop/local-mod collision scan was not rerun in this bounded pass; the default broad `audit_chaosx_country_tags.py --surface-scan` exceeded the 120-second command window, so the constrained zero-collision run is not a replacement for a fresh installed-environment report.
- No live game, save/load, scenario playback, or MCP runtime execution was performed. Those remain optional future QA under the current source/static acceptance authority.
- No row-level package, formable, focus-geometry, AI/balance, audio, achievement, or catalog completion claim is made by this count audit.

## Files changed

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_registry_package_counts_reaudit_v79_2026_08_01.md`

No gameplay, localisation, asset, spreadsheet, source-spec, current implementation, or historical handoff file was changed. No unrelated worktree edits were reverted.

## Remaining risks

- Current documentation surfaces still contain both post-ARX 14/13/14 prose and stale 13/12/13 or 13/61 prose until the parent reconciles them.
- The current static package pool is not a whole-event completion proof and does not by itself authorize upper-band automatic waves.
- The full installed Workshop collision report and the five unindexed portrait shelf files need parent-owned reconciliation before final closure.
