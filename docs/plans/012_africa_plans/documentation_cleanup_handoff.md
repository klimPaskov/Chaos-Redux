# Event 012 Africa documentation cleanup handoff

Date: 2026-07-29.

Scope: release-candidate reconciliation of Event 012 documentation, dated plans, subagent handoffs, visual asset status, and stale cross-references. This handoff does not change gameplay, localisation, GFX, GUI, binary assets, or the event catalog workbook.

## Source-of-truth map

| Surface | Current source of truth | Evidence or boundary |
| --- | --- | --- |
| Accepted design | `docs/specs/012_africa_specs/` | The accepted specification remains authoritative for intended mechanics, routes, counts, and required surfaces. |
| Release-candidate status | `docs/events/012_africa.md` | This is the current reconciled ledger for Event 012 status and unresolved decisions. |
| Event subsystem mechanics | `docs/events/012_africa_charter_autonomy_and_focus_ai.md`, `docs/events/012_africa_evolutions.md`, and `docs/events/012_africa_world_order.md` | These remain subsystem authorities and were not merged or deleted. |
| Visual row status | `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv` and its notes file | The 239 rows now use explicit release dispositions instead of `planned`. |
| Gameplay implementation | Current `common/`, `events/`, `localisation/`, and `interface/` files | Implementation is evidence of what exists, not permission to silently alter the accepted design. |
| Historical working ledger | `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` | Retained as historical evidence; its old queued/blocked asset counts are not current release status. |
| Asset provenance | Named manifests under `docs/assets/` and `docs/super_events/` | Manifests remain owner evidence; this pass did not rewrite out-of-scope asset manifests. |
| Spreadsheet catalog | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Owned by `chaosx_spreadsheet_doc_worker`; not opened or edited. |

## Current release dispositions

The accepted Event 012 identity is tier 4, Minor Fire-Once, Formables cluster 6, Severe member severity, and entry event `chaosx.nr12.1`. The current implementation ledger records 51 host playbooks, 22 full and 29 compact, a generic-tree-only host focus loader, 102 parameterized action IDs, Africa-only Scramble aftermath closure, 16 existing-tag priority packages, and the explicit runtime gates `africa_strange_formation_package_ready` and `africa_world_package_implementation_ready`.

The current visual matrix has 239 rows and no `planned` values: 43 `installed_runtime`, 28 `installed_dormant`, 12 `deferred_runtime_gated`, 133 `deferred_controlled_pool`, 16 `deferred_model_required`, 7 `deferred_unique_package_required`, and 0 `pending_runtime_blocker`.

The filesystem and registered `.gfx` evidence covers 23 Event 012 report/news/super-event pictures, 12 Charter static textures, two real Charter frame sheets with static fallbacks, 13 focus-family textures, 132 achievement DDS files, 16 sovereign portraits, seven carrier flag ladders, and the selected priority-member decision and report textures. These assets are installed, promotion-gated, or intentionally deferred according to the matrix and current owner gates.

South Africa is intentionally excluded from ordinary host selection by the generic-focus safety gate and remains external Allied contact, civil-war, and settlement content. Older SAF host-witness and playbook documents are deferred design reconciliation and a full-content blocker, not an active release-candidate registration blocker.

## Unresolved plan and handoff disposition

| Document | Disposition | Current interpretation and next owner |
| --- | --- | --- |
| `012_africa_achievements_handoff.md` | Superseded wording, retained evidence | All 44 three-state icon triplets are installed as 132 DDS files. Owner-system milestone and disqualifier callsite review remains open. |
| `012_africa_runtime_core_audit_handoff.md` | Accepted release-candidate evidence, retained audit | The Event 12-only selected-enemy Event 013 wrapper call is audited against unchanged Event 013 sources with exact target and output receipts. Strange-force consumers remain gated and model-free until an approved package exists. |
| `012_africa_decision_mission_release_candidate_audit_handoff.md` | Updated evidence | Charter Ledger DDS is present and registered. The prior pending-DDS blocker is closed; gameplay and GUI acceptance remain separate. |
| `012_africa_priority_member_packages_handoff.md` | Superseded asset wording, retained gameplay evidence | Sixteen portraits, 35 ideas, 16 mechanic decisions, 16 force decisions, 16 post-settlement decisions, eight shared decisions, four reports, and seven carrier ladders have current installed evidence. Full package, provenance, and runtime acceptance remain open. |
| `012_africa_focus_icon_assets_handoff.md` | Superseded integration wording, retained production evidence | Thirteen family textures and 13 regular plus 13 shine registrations are present. Broader per-final-focus expansion remains deferred. |
| `012_africa_super_event_audio_research_handoff.md` | Historical research with corrected production status | Roles 2 and 3 have later dormant production candidates; roles 1 and 4 remain production-blocked. No audio is runtime-wired. |
| `012_africa_super_event_audio_production_handoff.md` | Dormant production evidence | Produced candidates remain unwired until the four-role package can be registered atomically. |
| `subagent_handoffs/012_africa_charter_gui_handoff_2026_07_24.md` | Superseded queued-texture wording | Twelve static textures and two real frame sheets are present and registered; final 16/16 exact-path review is complete and the registration scan reports no active blocker. The source handoff's older in-progress sentence is overridden by its release-candidate correction and this row. |
| `subagent_handoffs/012_africa_country_rc_audit_2026_07_29.md` | Historical count corrected | Sixteen sovereign portraits are installed; seven carrier flag ladders are being integrated. Carrier ownership and reachability risks remain open. |
| `subagent_handoffs/012_africa_independence_wave_tag_loading_country_audit_2026_07_24.md` | Historical reachability evidence | The seven carrier presentation ladders are installed on existing identities and remain usable through bounded promotion; Event 006 allocator provenance and unbound paths remain unresolved. |
| `subagent_handoffs/012_africa_acceptance_ledger_reconciliation_2026_07_24.md` | Superseded by this handoff and `docs/events/012_africa.md` | Retained as the 2026-07-24 baseline; its missing-art and mostly-queued claims predate current filesystem evidence. |
| `012_africa_implementation_source_map.md` | Historical source-map baseline | Accepted design provenance remains useful, but current asset and status dispositions come from the release-candidate document and matrix. |
| `012_africa_ai_actions_77_92_handoff_2026_07_18.md` | Queued audit evidence | The bounded late-action dispatcher does not prove all 64 AI profiles or campaign simulations. |
| `012_africa_focus_architecture_handoff.md` | Queued audit evidence | Focus route, AI, topology, icon, and live-consumer audits remain open. |
| `012_africa_world_order.md` | Active subsystem evidence | Africa-only Scramble closure and world-package readiness gate are retained as the current world-order contract. |

## Contradictions and resolutions

1. The achievement handoff previously contained 44 row-level `triplet missing` phrases while all 132 DDS files existed. Every row now records `triplet installed`; only owner-system proof and disqualifiers remain open.
2. The runtime-core handoff now records accepted Event 13 wrapper evidence against unchanged Event 13 sources and retains the strange-formation readiness gate.
3. The priority-member handoff described portraits and broad visual families as unresolved while current folders and registrations contain the installed subset. A correction records promotion-gated evidence without promoting the gameplay package.
4. The decision handoff said the Charter Ledger DDS was pending, and the focus handoff said `.gfx` registration was pending. Both are superseded by current file and registration checks; broader route and per-focus requirements remain open.
5. The matrix suggested filenames for two Africa-is-one images differ from registered paths. The Charter header path is final at `gfx/interface/012_africa/charter_header_plate.dds`; registered `.gfx` paths remain authoritative.
6. The audio research handoff said roles 2 and 3 had no produced files, while the later production handoff records dormant candidates. The research handoff now points to the production handoff for current status.
7. The historical acceptance ledger marks most asset rows queued or blocked. It is explicitly superseded for visual status by the 239-row matrix and this handoff.

## Duplicate or superseded documents

- `docs/events/012_africa.md` is the central index; the three subsystem event documents remain intentionally separate authorities rather than duplicates.
- `subagent_handoffs/012_africa_acceptance_ledger_reconciliation_2026_07_24.md` is retained as a dated baseline and superseded for release status.
- `012_africa_implementation_source_map.md` is retained for accepted design provenance and superseded for current asset disposition.
- The achievement, priority-member, decision, focus-icon, Charter-GUI, country, and audio research handoffs retain historical evidence with explicit correction sections instead of deletion.
- No documentation file was deleted or merged destructively.

## Stale prompt or instruction list

- `docs/assets/012_africa/focus_icons_imagegen/gfx_handoff.md` and its manifest still use tranche-era wording that says `.gfx` registration is pending. They are outside this cleanup scope and should be corrected by the asset owner without changing stable IDs.
- Historical pending-DDS and queued-texture phrases remain inside retained old audit sections where the new correction notices explicitly supersede them. Achievement row dispositions were rewritten to `triplet installed`.
- `docs/specs/012_africa_specs/prompts/africa_goal_prompt.md` remains an accepted completion instruction, not a status report; it was not rewritten to hide open surfaces.

## Parent decisions required

1. Decide whether to normalize the two Africa-is-one suggested filenames in a separate owner patch while preserving registered runtime paths.
2. Decide when the seven carrier flag ladders have completed bounded Event 006 ownership and package promotion acceptance.
3. Decide whether the broader per-final-focus icon requirement remains queued or is narrowed to the 13 current family consumers.
4. Decide when the six continent packages and The World can satisfy `africa_world_package_implementation_ready`.
5. Obtain native/full-string review and placement for the two deferred Afaan Oromoo strings, or explicitly reject them without substitutes.

## Files changed by this cleanup

- `docs/events/012_africa.md`
- `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv`
- `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix_notes.md`
- `docs/plans/012_africa_plans/012_africa_achievements_handoff.md`
- `docs/plans/012_africa_plans/012_africa_runtime_core_audit_handoff.md`
- `docs/plans/012_africa_plans/012_africa_decision_mission_release_candidate_audit_handoff.md`
- `docs/plans/012_africa_plans/012_africa_priority_member_packages_handoff.md`
- `docs/plans/012_africa_plans/012_africa_focus_icon_assets_handoff.md`
- `docs/plans/012_africa_plans/012_africa_implementation_source_map.md`
- `docs/plans/012_africa_plans/012_africa_super_event_audio_research_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_acceptance_ledger_reconciliation_2026_07_24.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_charter_gui_handoff_2026_07_24.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_country_rc_audit_2026_07_29.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_independence_wave_tag_loading_country_audit_2026_07_24.md`
- `docs/plans/012_africa_plans/documentation_cleanup_handoff.md`

## Validation and skipped checks

Targeted path and registration checks confirmed the current image, Charter, focus, achievement, portrait, decision, report, and carrier-flag evidence described above. The final 16/16 Charter exact-path review, focus and decision reaudits, and registration scan report no active blocker. The Event 12-only Event 13 wrapper call was rechecked against unchanged Event 13 sources. The matrix was imported after editing and confirmed 239 rows, no `planned` values, and the seven disposition counts recorded in `docs/events/012_africa.md`.

No in-game launch, save test, workbook edit, binary visual re-authoring, or gameplay audit was performed because those surfaces remain parent-owned or outside this documentation scope. The working tree contains concurrent unrelated changes; no commit was created.

## Remaining risks

The documentation is internally cross-referenced for the release-candidate status, but gameplay acceptance, owner-system achievement proof, Event 013 integration, carrier provenance, GUI animation acceptance, world-package implementation, audio rights/wiring, native language review, and broad controlled-pool asset production remain open. The parent should use this handoff and `docs/events/012_africa.md` before starting another implementation tranche.
