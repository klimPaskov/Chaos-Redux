# Event 006 country-registry documentation cleanup handoff

Date: 2026-07-19

Mode: documentation-only reconciliation. No gameplay, localisation, asset,
advisor, workbook, spreadsheet, or design-spec part was edited. No commit was
created; the parent owns the shared-worktree commit.

## Current source-of-truth map

| Surface | Current authority | Disposition |
| --- | --- | --- |
| Country identity, representation, resolved tags | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` | Canonical: 206 rows; 102 custom `X` shells, 91 registered-tag reuse rows (89 unique reused carriers), 13 overlay-only rows |
| Current anchors, hosts, and package bindings | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` | Canonical installed-map snapshot: 138 selectable bound, 55 selectable unbound, and 13 overlay rows |
| Tag safety, vanilla-identity reuse, overlays, intentional sharing | `docs/specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md` | Canonical safety/reuse evidence; only `CHU` (`IW-043`/`IW-046`) and `BIA` (`IW-096`/`IW-107`) are intentionally shared |
| Current routing/status | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` | Updated to point to the three-file authority set |

The registry computes 191 unique nonblank resolved carrier tags. The binding
CSV still contains the historical all-row 149/57 split in its supporting audit;
selection uses the current 138/55 selectable split after excluding 13 overlays.

## Plan and handoff dispositions

| Artifact | Disposition | Action/evidence |
| --- | --- | --- |
| `006_country_tag_registry_handoff.md` | Superseded | Banner and headings now identify the 128-new-tag/107-shell/21-inert ledger as historical and route to the canonical files |
| `006_documentation_curator_handoff.md` | Superseded | First 2026-07-14 `149/57`, `78`, and `128` curation ledger is explicitly historical |
| `006_repository_explorer_handoff.md` | Superseded | Initial `78/128` registry and placeholder findings are blocked from current routing |
| `006_installed_tag_and_vanilla_identity_audit_handoff.md` | Superseded first-pass evidence | Its `103/90` and `128/78` tables/hashes are labeled at-time evidence |
| `006_current_installed_map_binding_audit_handoff.md` | Implemented evidence with historical ledger | Its 149/57 result is labeled original all-row evidence; current CSV remains authoritative |
| `006_package_allocator_integration_handoff.md` | Historical allocator snapshot | Its 149/57 and 128-shell coverage figures are labeled at-time implementation evidence; current selection/identity comes from the canonical files |
| `006_country_registry_api_handoff.md` | Left unchanged, concurrent implementation evidence | It reports runtime arrays/collections and points to the new country-registry system doc owned by another agent; it does not replace the canonical CSV/binding/audit set |
| `006_tag_architecture_documentation_alignment_handoff.md` | Historical architecture snapshot | Its 102/91/13 reconciliation remains useful context; canonical files govern current identity/binding/safety |
| Runtime package registry template and country-package auditor brief | Current routing docs | Both now name the candidate CSV, binding CSV, and collision/reuse audit with explicit ownership boundaries |
| Accepted gameplay plans/addenda | Left unchanged | No implementation plan was promoted, rejected, or newly queued by this documentation-only pass |

No accepted gameplay plan was promoted, rejected, or newly queued by this
cleanup. No assets or advisor material were touched.

## Contradictions and duplicates

Resolved by explicit supersession or authority routing:

- 128 custom/new tags vs 102 custom shells, 78/90/103 reuse ledgers vs 91 reuse
  rows, and 21 inert identities vs the current 206-row registry.
- 149 bound / 57 unbound all-row evidence vs the 138 bound / 55 unbound
  selectable pool; the former is retained only as historical evidence because
  13 rows are overlays.
- `research/006_package_research_resolution.csv` being treated as the identity
  authority; it is now documented as supporting research beneath the candidate
  registry, binding CSV, and collision/reuse audit.

No contradiction remains inside the current three-file authority set. Historical
ledgers intentionally remain in place for traceability and must not be deleted.

## If patching were not allowed

The proposed cleanup would be to add superseded banners to the listed historical
handoffs, add the three-file authority block to the source map/resume/README,
and route the country-package auditor through the same files. Those actions are
already applied in this pass.

## Stale prompt/instruction audit

- The country-package auditor brief previously named only the candidate CSV; it
  now requires the binding CSV and collision/reuse audit and states which file
  owns each decision.
- The old tag-registry, explorer, first-pass identity, and first curator
  handoffs now carry prominent superseded notices.
- The allocator handoff's old all-row coverage table is explicitly labeled a
  historical implementation snapshot so its `149/57` and `128` figures do not
  reopen identity work.
- No other Event 006 prompt was found asserting the obsolete 128/78/103/90
  identity ledger. Asset/advisor prompts were left unchanged by scope.

## Files changed

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_package_allocator_integration_handoff.md`
- `docs/plans/006_independence_wave_plans/package_bindings/006_runtime_package_registry_template.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_country_tag_registry_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_current_installed_map_binding_audit_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_documentation_curator_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_installed_tag_and_vanilla_identity_audit_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_repository_explorer_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_tag_architecture_documentation_alignment_handoff.md`
- `docs/specs/006_independence_wave_specs/README.md`
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry_summary.md`
- `docs/specs/006_independence_wave_specs/prompts/independence_wave_subagent_routing_and_briefs.md`

## Validation and remaining risks

- Parsed both canonical CSVs with PowerShell: 206 registry rows; 102/91/13
  representation counts; 191 unique nonblank carrier tags; shared tags exactly
  `CHU` and `BIA`; 138/55 selectable binding split plus 13 overlays.
- Used targeted `rg` checks for obsolete ledgers, canonical-file references,
  and superseded handoff markers; reviewed the exact documentation diff.
- Skipped gameplay parsing, engine execution, localisation/asset checks, and
  workbook export because this task changed documentation only.
- Re-run the installed tag audit if the installed mod set or country registry
  changes; the current tag-safety and binding evidence are environment
  snapshots. Parent-wide Event 006 runtime/admission work remains unchanged.

## Parent decisions

1. Keep the historical handoffs for traceability; route all new identity or
   binding work through the three canonical files.
2. Do not treat 191 unique carriers as 191 playable packages: the 13 overlays
   remain non-selectable and CHU/BIA require their package-specific mutexes.
3. Preserve the existing current map/tag audit snapshots until an installed
   environment change justifies a rerun.
