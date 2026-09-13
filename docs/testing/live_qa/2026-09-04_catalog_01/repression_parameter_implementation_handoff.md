# Repression parameter migration implementation handoff

Disposition: `implemented` for the accepted source migration.
Acceptance basis: the parent reviewed `repression_parameter_startup_plan.md` and explicitly delegated exactly its eight TXT files, the owner API Markdown, and QA evidence under the user's authorized safe parser repair.
Runtime validation remains parent-owned.
This handoff makes no live-game or complete GUI acceptance claim.

## Implementation

The 11 existing helper contracts retain their IDs and country payer scope.
All 114 calls were re-enumerated from live source and migrated together.
The 104 external calls immediately initialize unscoped temporary `camp_site_cost_state_id` before boolean invocation.
The ten nested helper calls forward that input through boolean invocation.
The quote calculator alone enters `var:camp_site_cost_state_id` to read building levels.
There are 39 external inputs from decision `FROM.id`, 51 from `camp_selected_state_id`, and 14 from `camp_rework_action_state_id`.
The six negated ledger shortage predicates initialize outside `NOT`.
Payment calls initialize independently of the preceding execution guard.
Existing retained output initialization, formulas, inclusive gates, resource debits, reserves, action payloads, route guards, and cleanup remain intact.

| Changed runtime file, relative to `common/` | Migrated calls |
| --- | ---: |
| `decisions/camp_repression_generic_decisions.txt` | 12 |
| `scripted_effects/camp_repression_action_dispatcher_effects.txt` | 14 |
| `scripted_effects/camp_repression_rework_effects.txt` | 12 |
| `scripted_effects/camp_repression_site_cost_effects.txt` | 5 |
| `scripted_triggers/camp_repression_site_cost_triggers.txt` | 5 |
| `scripted_guis/camp_repression_ledger_scripted_gui.txt` | 6 |
| `scripted_localisation/camp_repression_ledger_scripted_localisation.txt` | 6 |
| `scripted_localisation/camp_repression_site_cost_scripted_localisation.txt` | 54 |

`common/scripted_effects/camp_repression_site_cost_effects.md` documents the required temporary input, country payer, nested forwarding, independent payment initialization, negation rule, and boolean example.
The startup plan records its parent acceptance and implementation evidence.
The exact helper-ID totals and all before/after call lines are in `repression_parameter_evidence/migration_manifest.json`.

No constants, weights, AI hints, formulas, resource amounts, layout, GFX, icons, event targets, flags, persistent caches, or on-actions were added or changed.
No new cleanup is required for the temporary input.
Existing labor reserve cleanup is preserved.
Concurrent `ai_hint_pp_cost` edits present at backup time are preserved exactly.

## Backups, application, and recovery

`pre_patch_repression_parameters/` contains byte-for-byte immediate backups of all nine modified files and reference copies of the unchanged site-cost constants and ledger interface.
`repression_parameter_evidence/migration_manifest.json` records original and candidate SHA-256 values.
The complete transaction checked live original hashes before application, checked each file again immediately before its write, and verified each written hash.
`repression_parameter_evidence/application.json` records nine successful guarded writes.
Rollback was not needed.
The task-specific migration utility includes conditional recovery that restores only a candidate still matching its own write, so concurrent edits are not overwritten.
No staging or commit was performed.

## Source validation

`repression_parameter_evidence/source_validation_live.json` records validation against the applied runtime files.
Its strict source interpreter evaluates the actual quote, gate, and payment bodies, using intended macro substitution for the original source and boolean calls with the explicit input for the migrated source.
It uses Decimal arithmetic and nearest rounding with a half-up tie convention.
It is a source model and does not execute the HOI4 parser.

- All eight runtime files reverse exactly to the original parsed script structure after removing only the documented migration, preserving unrelated gameplay and AI tokens.
- All 114 call mappings, immediate input initializers, inherited nested inputs, and the six negative contexts were checked.
- Thirty combinations cover the five payment families across marker-only, level-one, level-five, Gulag-only, combined-building, and single alternate-building sites.
- Before/after quoted temporaries, balances, and native debit operations match for all cases.
- Exact affordability passes and each individual resource one unit below the threshold fails.
- Every paid resource is debited once, and labor reserve snapshots are retained and cleared by the existing cleanup helper.
- Repeated input state IDs `1, 2, 1, 2` produce inspection quotes `13, 25, 13, 25` in the same modeled temporary context.
- SHA-256 checks confirm the site-cost constant table and ledger interface bytes are unchanged.

The archived startup first causes and parser cascades are documented in the accepted plan.
Their disappearance requires the parent's next engine parser validation.
No new logs were requested and no game process was operated by this subagent.

## MCP and visual evidence

The existing fixture source is `docs/plans/system_camp_repression_rework_plans/ui_polish_2026-09-05/scenarios.json`.
The exact copied arguments are `repression_parameter_evidence/gui_render_arguments.json`.
The matched scenarios are `sites_all_orders`, `sites_empty`, and `sites_long_name_locked`, at 1920×1080, UI scale 1, normal state, and generated scenarios disabled.
The fixtures retain their explicit per-control visibility, displayed values, and locked-state annotations.

The before inspection and render returned passing structural validation without hard diagnostics, revision `5b55cabecec6b42bcc12943f834aef996e8dd6843567c317e08e83b95285ff24`.
Their complete tool summaries and artifact references are `gui_before_inspect.json` and `gui_before_render.json` under `repression_parameter_evidence/`.
The matched after inspection and render also passed structural validation without hard diagnostics, revision `8e35f34bc589841ad25596b6c70fed301fd394f745d14a85f4a62ae3e8d1d41c`.
Their summaries and artifact references are `gui_after_inspect.json` and `gui_after_render.json`.
`gui_before_after_comparison.json` independently compares exact before/after artifact hashes and sizes, rather than treating the render tool's default self-comparison as a historical comparison.
All 18 PNG/SVG artifacts are identical, including full, cropped, click-region, source-map, state-matrix, and scenario-matrix views.
The fidelity report and validation artifacts are also unchanged.
Source graph and source-linked layout JSON hashes changed as expected when the scripted helper call source changed.
The decoded scenario matrix `gui_scenario_matrix.png` was visually reviewed across the three named cases.
`gui_fidelity.json` was decoded, hash-verified, and reviewed directly.
The recovered baseline image is `before_cropped.png` in the same directory.
Its SHA-256 is `59912d1f8fdc0c0763ee7f48d5a90bb71cfa350440423aa9a272f34182e11ce2`.
A 61,440-byte artifact response contained only 46,957 base64 characters instead of the required 81,920 and was discarded.
Recovery used 56 validated byte ranges of 6,000 bytes or the final tail, then independently verified decoded length, PNG signature, and artifact SHA-256.
`before_cropped_ranges.json` records the exact ranges and provenance.

Visual review of the baseline shows `[dynamic_loc]` placeholders in the selected-site cost/status area and crowded or clipped cost text in those cards.
The MCP fidelity summary records eight unresolved dynamic-text/visibility items.
The unresolved fields are the scripted GUI's `visible` predicate, `GetCampUiSelectedSiteStatus`, the four `GetCampUiSiteLabor*` amounts, `GetCampUiSiteInspectPoliticalPower`, the three `GetCampUiSiteDismantle*` amounts, the four `GetCampUiSiteEvidence*` amounts, and `GetCampUiSiteRestrictedPoliticalPower` on both restricted-order cards.
Each grouped card is one fidelity item, yielding seven text items and one visibility item.
These supplied fixtures do not establish live building levels or balances for executing the site-cost helpers, and the offline renderer does not execute their temporary-variable contract.
No values were invented to mask those gaps and no layout changes were made.
Those visible limits remain parent-owned and prevent an overall GUI acceptance claim.

## Remaining limits and omissions

Engine parsing, dynamic state scope resolution, and temporary lifetime across trigger/effect/helper/localisation boundaries remain unverified by the source model.
Missing or invalid dynamic state pointers have no fabricated source-model behavior or fallback.
The earlier event trace explicitly excluded helper projections despite `expandHelpers: true`, so it provides no helper-execution proof.
AI scoring was not analyzed or changed, and no probability validation is claimed.
No gameplay simplification was made.
Skills used: events, decisions/missions, subagents, and scripted GUI.
No skills were created or changed.
