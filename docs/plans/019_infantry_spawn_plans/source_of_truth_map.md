# Event 019 Documentation Source-of-Truth Map

Date reconciled: 2026-08-22

Scope: current documentation reconciliation after the provider-522, provider-523, and expanded unit-coverage tranches. The 2026-07-18 regional full-flag and whole-event audits remain historical evidence for their bounded surfaces, and they do not close the current provider-extension validation boundary. This map records the current provider inventory, exact equipment contracts, owner gates, support-only CBRN boundary, decisions-only runtime surface, MCP limitations, and plan dispositions.

## Authority order

1. Accepted design remains under `docs/specs/019_infantry_spawn_specs/`. `README.md` routes the current state, and `review/blockers_and_uncertainty.md` carries the live gates and planning-only qualification.
2. Player-facing feature status is summarized by `docs/events/019_infantry_spawn/overview.md` and `docs/events/019_infantry_spawn/systems/triggerable_scenario.md`, which is the SCN-013 implementation-facing documentation. The old `docs/systems/event_system/triggerable_scenarios.md` path is not present in the current tree and must not be used as a source reference.
3. `docs/assets/019_infantry_spawn/manifest.md` and `docs/assets/019_infantry_spawn/gfx_handoff.md` are the available asset evidence surfaces. Their 2026-07-18 completion assertions and former Muster Board rows are historical for the bounded asset tranche, and their former GUI material is archival because the accepted runtime is decisions-only. The restored package retains the named regional raw/master and validation records, but those historical records remain evidence rather than current provider or runtime completion proof.
4. Working plans and subagent handoffs under `docs/plans/019_infantry_spawn_plans/` are evidence with an explicit disposition. Historical files remain available, but supersession notices identify when they must not be used as current instructions.
5. The workbook remains the only editable catalog source. The 2026-07-18 workbook and CSV status is a historical catalog snapshot that recorded Event 19 and SCN-013 as `Fully Functional`; it is not current provider-lifecycle proof, and generated CSVs remain outputs rather than documentation authorities.
6. `docs/specs/019_infantry_spawn_specs/review/decision_only_surface_addendum_2026-08-05.md` is the current player-facing UI decision. It supersedes the former scripted-GUI implementation handoffs while preserving their production provenance as archival evidence; provider coverage and registry status remain owned by the Event 19 systems docs below.

## Current runtime boundary

Event 19 is ID `19`, classification `Minor Repeatable`, unclustered, nonterminal, and has no fixed derivative tag. The live triggerable scenario is `SCN-013`, The Unbidden Muster, because proposed `SCN-008` is owned by Independence Wave.

The live player-facing surface is ordinary decisions and decision categories only. No Event 19 scripted GUI is runtime-wired. Former Muster Board GUI specifications, prompts, handoffs, manifests, and asset packages remain archival provenance and must not be routed as active GUI implementation work.

Claimant identity is male-only at runtime under `subagent_handoffs/019_male_claimant_identity_correction_handoff_2026_07_16.md`; the earlier female-profile and female-commander claims remain rejected historical evidence.

The shared `infantry_spawn_ordinary_management_category_is_relevant` trigger is the lifecycle authority. It excludes completed takeover and achievement-marked claimant or derivative revolt, so the Formation Management and claimant categories disappear on those terminal outcomes even if another claimant row remains. Peaceful closeout remains available while no terminal outcome applies and the live obligations, formations, claimants, transactions, and management operations have cleared; Evolution III and IV capability flags alone do not keep the ordinary categories open.

The Event 19 registry owns exactly one code file, `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`. The current dynamic registry census contains 19 providers, `501-514`, `518`, and `520-523`, with registration plus thirteen Event 19 callbacks per provider.

The current provider coverage ledger records 97 land sub-units, consisting of 50 combat and 47 support definitions. The 19 providers cover all 50 combat definitions and four inseparable support attachments, while the remaining support-only definitions remain parent-owned unless a provider explicitly attaches them.

Provider 513 is structurally covered by the Event 012 readiness manifest and bounded startup call, then remains package-gated until `africa_strange_formation_package_ready` is set. Provider 523 is the Event 014 owner-side provider for all nine cannibal combat bodies, including `cannibal_bone_riders`; its exact owner totals are 7,350 manpower, 990 infantry equipment, and 35 motorized equipment before Event 19 scaling. Provider 521 covers only `chaos_battalion`; CBRN headquarters, regimental support, chemical-tank support, Livens support, and `chemical_agent_payload` remain parent-owned.

A future family adds one owner-side registration and the complete thirteen-callback contract from its existing integration surface. It does not edit an Event 19 family list, equipment selector, localisation selector, picture selector, or second registry file. Future land units and concrete equipment also require the CXT extension contract and owner-side idempotent setup registration documented in `docs/testing/chaosx_test_country.md`.

Derivative opening packages now reconcile their received local economy and logistics through `infantry_spawn_derivative_reconcile_starting_local_assets` and retire a fragile-start burden through `infantry_spawn_derivative_resolve_opening_local_asset_shortfall`. The source contract persists transferred-state industry, population, infrastructure, rail, ports, supply, resources, standard stockpiles, private-ledger liabilities, active formations, and owner-published custom-equipment token and amount arrays; it classifies fragile, strained, or viable without creating factories, infrastructure, supply assets, or a generic economy grant. The focus inventory effect records the proof that the temporary shortfall burden was resolved, and the helper contract is documented in `common/scripted_effects/chaosx_dynamic_effects.md`.

## Historical regional flag evidence

The asset manifest and regional remediation handoff record the following 91-row source/runtime chain for the bounded 2026-07-18 asset tranche. The restored package retains the raw/master, validation, and checksum paths named below, so this section records provenance evidence while remaining separate from current provider-extension and runtime completion claims.

1. **91 raw sources:** unmodified built-in ImageGen full-flag raws under
   `docs/assets/019_infantry_spawn/source_png/flags/regional_full_flag_raw/`.
   The claimant/zombie tranche has 35 rows, ghost has 28, and golem has 28.
   The seven GHOST_BASE prompt records were recovered exactly in their existing
   ghost-owned prompt/provenance files. Those protected files were not edited.
2. **91 spot masters:** deterministic 820x520 RGB masters under
   `docs/assets/019_infantry_spawn/processed_png/flags/regional_spot_colour_masters/`.
3. **273 native PNGs:** normal, medium, and small outputs under
   `docs/assets/019_infantry_spawn/processed_png/flags/`, at 82x52, 41x26, and
   10x7 respectively.
4. **273 runtime TGAs:** bottom-left-origin files under
   `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

The manifest names the processor and evidence as:

- processor: `docs/assets/019_infantry_spawn/_tooling/process_event_019_regional_flags.py`
- processor SHA-256: `d87e879184d5a28a52736b80af4bc0ce70abd9744de47210b1f6a7c3db15ece6`
- validation: `docs/assets/019_infantry_spawn/regional_flag_validation_2026_07_18.json`
- checksums: `docs/assets/019_infantry_spawn/regional_flag_checksums_2026_07_18.sha256`
- recorded runtime: Python 3.9.12, Pillow 11.1.0, NumPy 2.0.2
- validator status: `candidate_requires_independent_visual_review`

The manifest reports 91 identity rows, 7 region rows, 91 tag rows, 273 runtime TGA rows, and passing visual/runtime review rows. The independent remediation re-audit handoff `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md` is PASS for that historical asset tranche. The machine JSON retains its immutable literal `candidate_requires_independent_visual_review` processor-state value, which is superseded for approval by the separate PASS handoff and was not edited.

## Prompt and provenance disposition

The 7/18 claimant/zombie, ghost, and golem raw prompt/provenance records are
the current production evidence. The ghost prompt and provenance records are
ghost-owned and were deliberately left unchanged. The 7/16 motif prompt and
generation-provenance files are retained only as historical superseded records.

## Current plan and handoff disposition

| Plan or handoff | Disposition | Current reading |
| --- | --- | --- |
| `subagent_handoffs/019_dynamic_unit_provider_api_completion_2026-08-22.md` | implemented, corrected current evidence | The 19-provider registration/callback contract, 50-combat coverage, nine provider-523 bodies, owner-side future-family onboarding, and 43 parent-owned support-only definitions are recorded; the whole-event gate remains open. |
| `subagent_handoffs/019_dynamic_unit_provider_decision_audit_2026-08-22.md` | queued with reason | The continuation resolves dynamic obligation visibility, four-or-fewer ordinary request rows, icon-first provider costs, and mission-slot gating; owner approval remains required for the truthful exact standardization/settlement four-type presentation, while category-density save-state proof and decision/localisation integration remain open. |
| `subagent_handoffs/019_dynamic_unit_provider_localisation_audit_2026-08-22.md` | implemented for bounded scope; integration review open | The 19-provider presentation-token migration and bounded localisation repairs are recorded, while decision-audit integration findings remain open. |
| `subagent_handoffs/019_dynamic_unit_provider_probability_audit_2026-08-22.md` | blocked by tool limitation | The custom provider pool discovers zero normalized candidates and direct effect-derived weights remain unresolved; no exact odds claim is allowed. |
| `subagent_handoffs/019_final_derivative_country_audit_2026-08-22.md` | open with documented blockers | The local-asset gap is resolved by owner follow-up and the restored asset package supersedes the audit-time provenance gap, but the named probability route and strict ghost-weaker-than-parent proof remain unresolved. |
| `subagent_handoffs/019_final_focus_tree_audit_2026-08-22.md` | implemented with non-blocking warnings | The local-asset resolver call and focus geometry follow-up are recorded; parent review still owns the warning disposition. |
| `subagent_handoffs/019_final_catalog_alignment_2026-08-22.md` | implemented, historical catalog authority only | Event 19 and SCN-013 rows are aligned, but workbook `Fully Functional` status is a 2026-07-18 tranche snapshot and does not close the current provider gate. |
| `subagent_handoffs/019_decision_only_surface_2026-08-05.md` | promoted to current spec | This handoff is the accepted runtime UI decision: ordinary decisions and categories only, with former scripted-GUI artifacts archival. |
| `019_near_completion_improvement_addendum_2026_07_16.md` and dated closure audits | superseded by named current docs | Their `Fully Functional`, no-closure, and former GUI claims remain historical evidence for bounded tranches and are not active instructions. |
| `docs/assets/019_infantry_spawn/manifest.md` and `gfx_handoff.md` | historical evidence retained | The restored package is preserved, but former GUI rows are archival and asset PASS/catalog language is not current provider or whole-event proof. |

## Runtime and registry documentation

The one Event 019 registry code file remains `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`. `common/scripted_triggers/chaosx_dynamic_triggers.md` was inspected and remains current for the derivative classifier and registry/scenario contract. The current provider census is 19 IDs (`501-514`, `518`, `520-523`), with 14 required surfaces per provider (registration plus thirteen Event 19 callbacks). Event 016 providers `504-510` use their history-derived gates, and provider `522` is a separate Aryan clone adapter gated by `germany_mengele_is_germany_scope`, `germany_mengele_program_active`, the completed cloning-project and master-race-claim flags, and `mengele_aryan_clone_refinement_tech`. Providers 504 and 522 use ten combat battalions with 1,000 manpower, 90 infantry equipment, and 1 clone equipment per battalion, with a 1,000 manpower, 180 infantry equipment, and 2 clone equipment sustainment contract. Provider 521 records only the combat `chaos_battalion`; CBRN support-only bodies and `chemical_agent_payload` remain parent-owned. Provider 513 is structurally covered and package-gated until Event 012 sets `africa_strange_formation_package_ready`; static package evidence includes all eight combat/support unit definitions, eight meshes/entities, packaged DDS maps, and 49 sound files. The tracked owner manifest and its startup call make that package authority source-reachable. Provider 523 covers all nine Event 014 cannibal irregular combat units, with `cannibal_bone_riders` added by the owner-side CXT extension and included in the same exact provider manifest. Every provider supplies presentation tokens, profile-to-equipment resolution, and custom-equipment snapshot publication through the same generic provider-ID dispatch. The live owner publishers expose 20 custom equipment identifiers across the 19 custom profile values `130-148`; clone and Aryan-clone providers intentionally share profile `142` while retaining distinct provider identities. Event 19 retains only ordinary profiles `100-129`. No second registry file, family-list edit, equipment-list edit, or scripted-localisation family switch is implied by the provider route.

The selected-family spawn verifier is now manifest-aware. It accepts a committed provider obligation tail of zero, two, seven, or sixteen rows, derives expected manpower liability and equipment debt from the committed manifest totals, and proves sequential obligation UIDs, generation/lot/unit ownership, issued versus outstanding amounts, zero payment/salvage state, outstanding status, profile-appropriate debt, and aligned tail counts before commit. Provider 518's cave package intentionally contributes zero obligation rows because both manifest needs are zero.

The coal-golem model document is a separate non-gating visual extension. Provider 503 and the live `coal_golem` unit remain covered by the existing `sprite = infantry` definition and counter assets; its optional custom 3D mesh/entity package is blocked by rigging failure, but no Event 19 specification requires that package for provider or event completion.

The fresh read-only `hoi4.event_inspect` scan for `chaosx.nr19.1` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics and a bounded-analysis deferral. Its stable artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/568dc44f09d8ed2b886eb449235559a9d2dc28541918f2dedcc2e72a7f6490f8/527beb2e1a085d1e08c72ad44022dcd4ba243f9cc11495d0e369df28db7aabf6/event-scan-23147097ed55.json`. The installed probability adapter still cannot expose normalized odds for the dynamic provider pool, as recorded in `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_dynamic_unit_provider_probability_audit_2026-08-22.md`. These limitations are evidence boundaries rather than completion claims.

A fresh read-only `hoi4.focus_inspect` request for `common/national_focus/019_infantry_spawn_derivative_focus.txt` and `infantry_spawn_derivative_focus_tree` timed out after 180 seconds, so the current focus handoff remains the available MCP evidence rather than a newly refreshed result. A fresh read-only `hoi4.gui_inspect` request against the historical `infantry_spawn_muster_board_window` returned `GUI_INSPECTED` with zero inspected Event 19 elements, one missing and one approximated fidelity item, and global source/validation diagnostics truncated at the fixed 2,000-result ceiling; its archival artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/914ce3f03e91ed43b86b1545d73870f090c20102a5756faba685bddafddcbaf9/dc265e14c48c42b6f5f7fd71ea4ad80a70db523f9a9623406daec9dbd471c286/gui-inspect.4a7b909e843b8b82.json`. The former Muster Board GUI has no active runtime consumer, so this result is limitation evidence rather than current GUI proof; archived 2026-08-05 GUI handoffs also retain prior `SCAN_BYTE_LIMIT` limitations.

## Superseded or archival material

The following are historical evidence and must not be treated as the current
source/runtime chain:

- `docs/assets/019_infantry_spawn/source_png/flags/regional_variants/`
- `docs/assets/019_infantry_spawn/regional_flag_validation_2026_07_16.json`
- `docs/assets/019_infantry_spawn/regional_flag_checksums_2026_07_16.sha256`
- 7/16 motif/composite notes, prompts, provenance, validation, and contact
  sheets, including the files with explicit supersession banners
- `subagent_handoffs/019_regional_flag_assets_handoff_2026_07_16.md`
- `subagent_handoffs/019_regional_flag_flat_source_blocker_options_2026_07_17.md`
- `subagent_handoffs/019_regional_flag_flatness_rescue_2026_07_16.md`
- `subagent_handoffs/019_final_claimant_identity_closure_2026_07_16.md` and `subagent_handoffs/019_claimant_identity_specialist_reaudit_2026_07_16.md` retain rejected female-profile and female-commander evidence; they are superseded by `subagent_handoffs/019_male_claimant_identity_correction_handoff_2026_07_16.md`, which is the current male-only claimant identity authority.

The three 7/18 raw-tranche handoffs remain valid as tranche evidence, but their
raw-only boundary is historical after the common postprocess. Their banners
route readers to this map and the independent validation record. The separate
remediation re-audit PASS handoff is the approval authority for the current
regional candidate.

## Historical 2026-07-18 closure status

- Parent workbook/catalog reconciliation and export are complete.
- Parent package inventory reconciliation is complete. The current
  `review/package_contents.md` verifies all 33 files with no missing, extra, or
  mismatched rows and records the 4,342-character goal prompt.
- The mandatory final whole-event completion audit is PASS with P0/P1/P2 = 0.

The 2026-07-18 audit recorded Event 019 and SCN-013 as `Fully Functional` for
that historical tranche. The approved engine-constrained exact-transfer and
controlled-combat-trial contracts, regional asset gate, workbook/catalog
reconciliation, package inventory, and final audit were resolved for their
bounded surfaces. That status does not include the later provider-522 or expanded
unit-coverage extension, and no current whole-event completion claim is made here.
No fallback or unapproved substitute is recorded here.
